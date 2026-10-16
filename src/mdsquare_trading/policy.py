"""Mechanical admission is necessary, not proof of Brooks interpretation or edge."""
from datetime import time
from mdsquare_trading.domain import number, timestamp
from mdsquare_trading.store import digest

SETUPS = {
    'breakout_continuation_long': 'breakout', 'breakout_continuation_short': 'breakout',
    'breakout_pullback_long': 'breakout', 'breakout_pullback_short': 'breakout',
    'bull_first_pullback': 'bullish_momentum', 'bear_first_pullback': 'bearish_momentum',
    'bull_high2': 'bullish_mild', 'bear_low2': 'bearish_mild',
    'range_failed_breakout_long': 'sideways', 'range_failed_breakout_short': 'sideways',
    'opening_reversal_bull': 'reversals', 'opening_reversal_bear': 'reversals',
}


def economics(entry, stop, target, cost):
    entry, stop, target, cost = map(number, (entry, stop, target, cost))
    risk, reward = abs(entry - stop), abs(target - entry)
    if not risk or not reward or cost < 0:
        raise ValueError('Invalid risk/reward/cost')
    return {'risk_points': risk, 'reward_points': reward, 'reward_risk': reward / risk,
            'break_even_probability': (risk + cost) / (risk + reward),
            'estimated_success_probability': None, 'positive_expectancy_established': False}


def validate_candidate(candidate, job, policy):
    if policy.get('paper_policy_registered') is not True:
        raise ValueError('Paper policy is not registered')
    setup = candidate['setup']
    if setup not in SETUPS or policy['categories'].get(SETUPS[setup]) is not True or policy['setups'].get(setup) is not True:
        raise ValueError('Setup/category disabled')
    if job['data_quality']['status'] != 'READY':
        raise ValueError('Data quality blocks candidates')
    regime = candidate['regime']
    if regime not in ('BULL_TREND','BEAR_TREND','WIDE_RANGE','TRANSITION'):
        raise ValueError('Tight/unknown context blocks candidates')
    is_range = setup.startswith('range_failed_breakout_')
    if is_range != (regime == 'WIDE_RANGE'):
        raise ValueError('This foundation implements range entries only through genuine failed-breakout routes')
    if candidate.get('trade_intent') != ('RANGE_ROTATION' if is_range else 'SWING'):
        raise ValueError('Declare the matching trade intent before geometry')
    direction = candidate['direction']
    expected_long = setup.endswith(('long','bull')) or setup.startswith('bull_')
    if direction not in ('LONG','SHORT') or (direction == 'LONG') != expected_long:
        raise ValueError('Setup/direction mismatch')
    if regime == 'BULL_TREND' and direction == 'SHORT' or regime == 'BEAR_TREND' and direction == 'LONG':
        raise ValueError('Unsupported countertrend context; establish transition first')
    if regime == 'WIDE_RANGE' and candidate['location'] != ('LOWER_EDGE' if direction == 'LONG' else 'UPPER_EDGE'):
        raise ValueError('Range entry must originate at the correct outer edge')
    for key in ('context_reason','sequence_reason','contradiction','stop_reason','target_reason','opposition_reason'):
        if not isinstance(candidate.get(key), str) or not candidate[key].strip():
            raise ValueError(f'Missing {key}')
    bars = {b['id']: b for b in job['five_minute']}
    evidence = candidate['evidence_bar_ids']
    if not isinstance(evidence, list) or not evidence or any(b not in bars for b in evidence):
        raise ValueError('Unknown/empty causal evidence')
    correction = candidate['correction_bar_ids']
    if not isinstance(correction, list) or not correction or any(b not in bars for b in correction):
        raise ValueError('Unknown correction/base evidence')
    entry, stop, target = map(number, (candidate['entry'],candidate['stop'],candidate['target']))
    if not (0 < stop < entry < target if direction == 'LONG' else 0 < target < entry < stop):
        raise ValueError('Inconsistent entry/stop/target')
    buffer = number(policy['stop_buffer_points'])
    if buffer < 0:
        raise ValueError('Negative stop buffer')
    first, last = min(bars[b]['start'] for b in correction), max(bars[b]['start'] for b in correction)
    full = [b for b in bars.values() if first <= b['start'] <= last]
    extreme = min(b['low'] for b in full) if direction == 'LONG' else max(b['high'] for b in full)
    if (direction == 'LONG' and stop > extreme - buffer) or (direction == 'SHORT' and stop < extreme + buffer):
        raise ValueError('Stop fails to protect cited correction/base')
    latest = job['five_minute'][-1]
    if (direction == 'LONG' and entry <= latest['high']) or (direction == 'SHORT' and entry >= latest['low']):
        raise ValueError('Stop-style entry must remain prospective')
    expiry = timestamp(candidate['expires_at'])
    if expiry <= timestamp(job['as_of']) or expiry.date() != timestamp(job['as_of']).date():
        raise ValueError('Expiry must be prospective within session')
    if timestamp(job['as_of']).time() >= time.fromisoformat(policy['session_entry_cutoff']):
        raise ValueError('Entry cutoff reached')
    if expiry.time() > time.fromisoformat(policy['session_flat_at']):
        raise ValueError('Entry expiry extends beyond flat cutoff')
    projection = candidate['projection']
    anchors = []
    for anchor in projection['anchors']:
        if anchor['bar_id'] not in bars or anchor['field'] not in ('open','high','low','close'):
            raise ValueError('Unknown target anchor')
        anchors.append(bars[anchor['bar_id']][anchor['field']])
    method = projection['method']
    if method == 'LEG_EQUALITY' and len(anchors) == 3:
        a, b, c = anchors
        calculated = c + (b - a)
    elif method == 'SPIKE_EXTENSION' and len(anchors) == 2:
        a, b = anchors
        calculated = b + (b - a)
    elif method == 'RANGE_HEIGHT' and len(anchors) == 2:
        low, high = anchors
        if low >= high:
            raise ValueError('Reversed range anchors')
        calculated = high + (high - low) if direction == 'LONG' else low - (high - low)
    elif method == 'FIRST_OPPOSITION' and len(anchors) == 1:
        calculated = anchors[0]
    else:
        raise ValueError('Unsupported projection/anchor count')
    if abs(calculated - target) > 1e-6:
        raise ValueError('Target inconsistent with supplied causal projection')
    if method in ('LEG_EQUALITY','SPIKE_EXTENSION') and ((anchors[1] > anchors[0]) != (direction == 'LONG')):
        raise ValueError('Projection direction inconsistent')
    result = economics(entry, stop, target, policy['round_trip_cost_points'])
    if number(policy['minimum_reward_risk']) <= 0:
        raise ValueError('Minimum reward/risk must be positive')
    if result['reward_risk'] < number(policy['minimum_reward_risk']) or result['reward_points'] <= number(policy['round_trip_cost_points']):
        raise ValueError('Configured economics insufficient')
    # Identity comes from structure, not a model's arbitrary episode string or setup alias.
    episode = digest({'instrument':job['instrument'],'direction':direction,'correction':sorted(correction)})
    return {**candidate, 'id':episode, 'instrument':job['instrument'], 'status':'PENDING',
            'created_at':job['as_of'], 'economics':result}
