"""Conservative OHLC paper events; ambiguity is never an invented fill."""
from datetime import time, timedelta
from mdsquare_trading.domain import timestamp


def advance(store, policy, as_of):
    as_of = timestamp(as_of)
    emitted = []
    with store.db:
        store.db.execute('BEGIN IMMEDIATE')
        for plan in store.plans(active=True):
            if plan['status'] == 'REVIEW_REQUIRED':
                continue
            created = timestamp(plan['created_at'])
            for bar in store.candles(plan['instrument'], 1):
                if bar.start < created or bar.end > as_of or bar.observed_at > as_of:
                    continue
                last = timestamp(plan['last_processed']) if plan.get('last_processed') else None
                if last and bar.start <= last:
                    continue
                event = None
                first_expected = created.replace(second=0,microsecond=0)
                if created.second or created.microsecond:
                    first_expected += timedelta(minutes=1)
                if (last and bar.start != last + timedelta(minutes=1)) or (last is None and bar.start != first_expected):
                    plan['status'] = 'REVIEW_REQUIRED'
                    event = 'MISSING_MINUTE_DURING_PLAN'
                elif plan['status'] == 'PENDING' and (bar.start >= timestamp(plan['expires_at']) or
                        bar.start.time() >= time.fromisoformat(policy['session_entry_cutoff'])):
                    plan['status'], event = 'EXPIRED', 'PAPER_ENTRY_EXPIRED'
                elif plan['status'] == 'PENDING' and bar.end > timestamp(plan['expires_at']):
                    plan['status'], event = 'REVIEW_REQUIRED', 'EXPIRY_WITHIN_MINUTE'
                elif plan['status'] == 'OPEN' and bar.start.time() >= time.fromisoformat(policy['session_flat_at']):
                    plan['status'], event, plan['exit_price'] = 'CLOSED', 'PAPER_SESSION_CLOSE', bar.open
                else:
                    long = plan['direction'] == 'LONG'
                    new_fill = False
                    if plan['status'] == 'PENDING' and (bar.high >= plan['entry'] if long else bar.low <= plan['entry']):
                        fill = max(plan['entry'], bar.open) if long else min(plan['entry'], bar.open)
                        if (fill >= plan['target'] if long else fill <= plan['target']):
                            plan['status'], event = 'REVIEW_REQUIRED', 'GAP_BEYOND_TARGET'
                        else:
                            plan['status'], plan['fill_price'], plan['filled_at'] = 'OPEN', fill, bar.start.isoformat()
                            new_fill = True
                            event = 'PAPER_ENTRY'
                    if plan['status'] == 'OPEN':
                        stop = bar.low <= plan['stop'] if long else bar.high >= plan['stop']
                        target = bar.high >= plan['target'] if long else bar.low <= plan['target']
                        gapped_entry = (bar.open >= plan['entry'] if long else bar.open <= plan['entry'])
                        gap_stop = bar.open <= plan['stop'] if long else bar.open >= plan['stop']
                        gap_target = bar.open >= plan['target'] if long else bar.open <= plan['target']
                        if not new_fill and gap_stop:
                            plan['status'], event, plan['exit_price'] = 'CLOSED', 'PAPER_STOP', bar.open
                        elif not new_fill and gap_target:
                            plan['status'], event, plan['exit_price'] = 'CLOSED', 'PAPER_TARGET', plan['target']
                        elif stop and target or new_fill and not gapped_entry and stop:
                            plan['status'], event = 'REVIEW_REQUIRED', 'AMBIGUOUS_INTRAMINUTE_ORDER'
                        elif stop:
                            plan['status'], event = 'CLOSED', 'PAPER_STOP'
                            plan['exit_price'] = min(bar.open, plan['stop']) if long else max(bar.open, plan['stop'])
                        elif target:
                            plan['status'], event, plan['exit_price'] = 'CLOSED', 'PAPER_TARGET', plan['target']
                plan['last_processed'] = bar.start.isoformat()
                if event:
                    payload = {'type':event, 'plan_id':plan['id'], 'instrument':plan['instrument'],
                               'bar_id':bar.id, 'status':plan['status'], 'simulation':True}
                    if plan['status'] == 'CLOSED':
                        sign = 1 if plan['direction'] == 'LONG' else -1
                        plan['net_points'] = sign * (plan['exit_price'] - plan['fill_price']) - policy['round_trip_cost_points']
                        payload['net_points'] = plan['net_points']
                    store.event(payload)
                    emitted.append(payload)
                store.save_plan(plan)
                if plan['status'] not in ('PENDING','OPEN'):
                    break
    return emitted
