"""Provider-neutral analysis jobs with one authoritative database and generation."""
from datetime import datetime, time, timedelta
import json
from mdsquare_trading.domain import IST, INSTRUMENTS, aggregate, timestamp
from mdsquare_trading.store import canonical, digest
from mdsquare_trading.policy import validate_candidate


def assign(store, processor):
    if not isinstance(processor, str) or not processor.strip():
        raise ValueError('Processor label required')
    with store.db:
        store.db.execute('BEGIN IMMEDIATE')
        current = store.state('processor', {'generation':0})
        result = {'processor_id':processor, 'generation':current['generation'] + 1}
        store.set_state('processor', result)
        store.event({'type':'PROCESSOR_ASSIGNED', **result})
    return result


def context(store, instrument, policy, as_of, persist=True):
    as_of = timestamp(as_of)
    assignment = store.state('processor')
    if assignment is None:
        raise ValueError('Assign a processor first')
    minutes = [b for b in store.candles(instrument, 1) if
               b.start.date() >= as_of.date() - timedelta(days=policy['history_calendar_days'])]
    five = aggregate(minutes, as_of, policy['settle_seconds'])
    daily = [b for b in store.candles(instrument, 1440) if b.end <= as_of and b.observed_at <= as_of
             and b.start.date() >= as_of.date() - timedelta(days=policy['daily_calendar_days'])]
    current = [b for b in five if b.start.date() == as_of.date()]
    status, issues = 'READY', []
    is_session = (as_of.weekday() < 5 and as_of.date().isoformat() not in policy['holidays']
                  and time(9,15) <= as_of.time() < time(15,30))
    if not is_session:
        status, issues = 'MARKET_CLOSED', ['Outside configured regular session; special sessions not inferred']
    else:
        expected = (as_of - timedelta(seconds=policy['settle_seconds'])).replace(second=0,microsecond=0)
        expected = expected.replace(minute=expected.minute - expected.minute % 5)
        opening = datetime.combine(as_of.date(), time(9,15), IST)
        required = set()
        cursor = opening
        while cursor < expected:
            required.add(cursor)
            cursor += timedelta(minutes=5)
        missing = required - {b.start for b in current}
        if not current or missing or current[-1].end != expected:
            status = 'INCOMPLETE'
            issues.append('Current-session five-minute candles incomplete or delayed; gaps never filled')
    active = [p for p in store.plans(True) if p['instrument']==instrument]
    retained_ids = {b for p in active for key in ('evidence_bar_ids','correction_bar_ids') for b in p.get(key,[])}
    shown = {b.id:b for b in five[-policy['context_five_minute_bars']:]}
    shown.update({b.id:b for b in five if b.id in retained_ids})
    compact_five = sorted(shown.values(), key=lambda b:b.start)
    job = {'schema_version':'foundation.v1', 'skill_version':'0.13.0', 'instrument':instrument,
           'as_of':as_of.isoformat(), **assignment, 'policy_hash':digest(policy), 'policy':policy,
           'five_minute':[b.record() for b in compact_five], 'daily':[b.record() for b in daily[-policy['context_daily_bars']:]],
           'history_availability':{'five_minute_bars_available':len(five), 'five_minute_bars_shown':len(compact_five),
                                  'older_data':'Use export-history for a specific older slice; do not invent absent structure'},
           'data_quality':{'status':status,'issues':issues,'daily_bars':len(daily),
                           'historical_coverage_verified':False},
           'inventory_scope':'LOCAL_PAPER_ONLY', 'inventory_status':'KNOWN',
           'active_plans':active,
           'analysis_instructions':'Use docs/skills/brooks-index-analysis/SKILL.md. Review supplied trades first. No invented context, probabilities or fills.'}
    job['context_id'] = digest(job)
    if persist:
        store.save_job(job)
    return job


def submit(store, review, policy, now):
    """Admit a foundation.v1 research review; not the full proposed 0.9 contract."""
    now = timestamp(now)
    with store.db:
        store.db.execute('BEGIN IMMEDIATE')
        row = store.db.execute('SELECT payload FROM jobs WHERE id=?', (review['context_id'],)).fetchone()
        if row is None:
            raise ValueError('Unknown context')
        job = json.loads(row[0])
        supplied_hash = job.pop('context_id')
        if digest(job) != supplied_hash:
            raise ValueError('Corrupt stored context')
        job['context_id'] = supplied_hash
        assignment = store.state('processor')
        if review.get('processor_id') != assignment['processor_id'] or review.get('generation') != assignment['generation'] or any(job[k] != assignment[k] for k in assignment):
            raise ValueError('Stale/unassigned processor generation')
        if digest(policy) != job['policy_hash']:
            raise ValueError('Policy changed since context export')
        if store.db.execute('SELECT 1 FROM decisions WHERE job_id=?', (supplied_hash,)).fetchone():
            raise ValueError('Context already reviewed')
        age = (now - timestamp(job['as_of'])).total_seconds()
        if not 0 <= age <= policy['max_decision_age_seconds']:
            raise ValueError('Expired/future context')
        instrument = job['instrument']
        # Reject data corrections/new completed candles or state changes since export.
        current = context(store, instrument, policy, timestamp(job['as_of']), persist=False)
        if current['context_id'] != supplied_hash:
            raise ValueError('Data or paper inventory changed since export')
        reviews = review.get('open_trade_reviews')
        expected = {p['id'] for p in job['active_plans']}
        if not isinstance(reviews, list) or len(reviews) != len(expected) or {r.get('plan_id') for r in reviews} != expected:
            raise ValueError('Every supplied active plan needs exactly one review')
        for item in reviews:
            if item.get('action') not in ('HOLD','CLOSE_RECOMMENDATION','WITHDRAW_RECOMMENDATION','REVIEW_REQUIRED') or not item.get('reason'):
                raise ValueError('Invalid trade review')
        action = review['action']
        if action not in ('WAIT','SKIP','INSUFFICIENT_DATA','CANDIDATE') or not isinstance(review.get('reason'),str) or not review['reason'].strip():
            raise ValueError('Invalid action/reason')
        if action != 'CANDIDATE' and review.get('candidate') is not None:
            raise ValueError('Non-candidate cannot carry an armable plan')
        if action == 'CANDIDATE':
            if expected:
                raise ValueError('One active paper plan per instrument')
            plan = validate_candidate(review['candidate'], job, policy)
            if timestamp(plan['expires_at']) <= now:
                raise ValueError('Candidate already expired at admission')
            if store.db.execute('SELECT 1 FROM plans WHERE id=?', (plan['id'],)).fetchone():
                raise ValueError('Consumed episode cannot be rearmed')
            minute_bars = [b for b in store.candles(instrument, 1) if b.observed_at <= now]
            if not minute_bars or max(b.end for b in minute_bars) < now.replace(second=0,microsecond=0) - timedelta(minutes=1):
                raise ValueError('Recent one-minute evidence required at candidate admission')
            for bar in minute_bars:
                if bar.end > timestamp(job['as_of']) and bar.observed_at <= now:
                    crossed = bar.high >= plan['entry'] if plan['direction'] == 'LONG' else bar.low <= plan['entry']
                    if crossed:
                        raise ValueError('Entry crossed after export; no retroactive arm/fill')
            # Do not claim to arm at the earlier export time.
            plan['created_at'] = now.isoformat()
            store.save_plan(plan)
        store.db.execute('INSERT INTO decisions VALUES (?,?)', (supplied_hash,canonical(review)))
        store.event({'type':'ANALYSIS_REVIEW','context_id':supplied_hash,'instrument':instrument,
                     'action':action,'reason':review['reason'],'open_trade_reviews':reviews})
    return review
