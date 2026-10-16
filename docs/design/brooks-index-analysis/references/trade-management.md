# Open-trade tracking, exits and planned additions

One skill interprets new opportunities and supplied open-trade state. Durable trade state, fills, protection and event monitoring must be maintained by the application. A skill call alone cannot continuously watch prices, preserve reliable positions or execute orders. Recommendations never count as fills.

## Required state

For each open episode use supplied trade/episode ID, direction, actual entry fills and quantities or declared paper units, average entry, original/current stop, original target/method/anchors, remaining size, realized exits, pending actions, committed risk budget, add-on plan, entry thesis, state revision, relevant event watermark and as-of price/bar context. Read entry plan and subsequent accepted amendments; do not reconstruct them from chat memory.

No supplied open-trade inventory is UNKNOWN, not 'no open trades.' Ask for/retrieve it through available tools; do not invent positions. With missing state, return REVIEW_REQUIRED for the affected trade and preserve known protection. Missing add-on details block additions; missing numerical target does not prevent identifying clear thesis failure if facts suffice.

Review open trades before proposing new risk. Entry-category disable does not suppress management of an existing trade. Missing broker details are irrelevant to underlying paper interpretation, but missing fills/quantity/risk means no claim that a monetary addition is safe.

## Swing continuity and committed objective

Review the original swing thesis, phase, defended structure and measured-move premise against current bars. Normal correction or a small opposite setup does not by itself justify closing a supported swing. Equally, meaningful opposing acceptance or structural failure can defeat it before the protective stop. Cite the discriminator. A checkpoint touch is not TAKE_PROFIT when the committed target is a measured-swing objective and policy has no partial exit there. Do not replace a fixed first-opposition target with a measured target after price rallies. Preserve authoritative stop/target and pending actions.

## Simple baseline management

Use the accepted policy: one structural stop and one primary target, with optional predefined trailing/partial/timeout rules. Do not invent numerical exit thresholds, time limits, partial fractions or a new target each bar.

| Current evidence/state | Recommendation |
| --- | --- |
| Supplied stop breached or thesis definitively invalidated | CLOSE unless already closed/exit pending; no addition or widening |
| Primary objective reached under the accepted fixed-target policy | TAKE_PROFIT for remaining quantity; not merely 'maybe continue' |
| Sustained opposing evidence defeats the entry premise before stop | CLOSE or policy-defined REDUCE, with precise supporting facts |
| Normal correction, intact thesis/stop and usable remaining objective | HOLD; one opposing candle alone is not an automatic exit |
| Strong continuation with a confirmed new swing | HOLD or propose a policy-authorized protective tightening; never invent a hindsight swing |
| Range rotation reaches its intended internal objective | TAKE_PROFIT per plan; no automatic conversion to a trend swing |
| Tight range develops after entry | No new risk; review loss of urgency, remaining objective and supplied no-progress policy. HOLD/REDUCE/CLOSE depends on that evidence/policy, not an automatic blanket exit |
| Time/no-progress/session cutoff condition is met | CLOSE/REDUCE according to the accepted condition, irrespective of hope for recovery |
| Planned exit/add action already pending | Report its status; no duplicate action until state/revision confirms what occurred |
| Required trade or market state unreliable | REVIEW_REQUIRED; no new risk or fabricated hold certainty |

Recognize disappointment, climactic/opposing behavior and weakening follow-through in context. They can justify management review but do not mechanically imply a major reversal. A new opposite setup does not automatically reverse the existing position. Follow the existing exit policy first; fresh opposite entry needs a separate eligible episode.

## Exit timing

Evaluate thesis changes on completed analysis bars. Protective stop, committed target and time-bound triggers must be monitored by independent event/code logic at the required frequency; they do not wait for the next AI response. If supplied events show a breach between calls, use that event and current trade state. Historical OHLC touching both stop and target leaves ordering ambiguous: return REVIEW_REQUIRED/replay ambiguity, not a favorable assumed fill.

An entry-plan expiry prevents a new entry; it does not close a filled trade unless the accepted position policy explicitly uses that timestamp. Position holding horizon, add-on validity and entry validity are separate. An AI/provider outage cannot disable existing protective monitoring.

## Planned averaging into an adverse move

Support identifying a potential add zone, but distinguish ADD_WATCH from ADD_CANDIDATE. This is bounded planned scale-in, not doubling down until recovery. [Brooks discusses scaling into adverse moves](https://www.brookstradingcourse.com/es/live-trades/scaling-in-to-avoid-loss/); adopting it requires an explicit policy and separate episode-level evaluation.

Before initial entry, record: contextual add zone and source anchors; additional confirmation, if required; exact maximum adds; tranche sizes; unchanged common invalidation/stop; maximum total committed risk; add expiry; target/exit policy for the combined position; and failure conditions. Smaller initial size must reserve capacity for the planned tranches. No supplied enable/size/budget means additions are WATCH_ONLY, not candidates; still explain a supported zone when evidence permits.

Every add must satisfy all of these:

- Original thesis remains valid; adverse movement is an allowed correction/test, not credible opposing acceptance or structural failure.
- The declared zone is reached and its confirmation is observed; data is current, action not already pending/filled, add count and expiry valid.
- Stop has not been breached and will not be widened; no averaging after invalidation.
- Combined worst planned stop loss including all filled/proposed tranches and pending reservations stays within the original committed episode/account budget under supplied units/costs. Never treat a better average price as reduced total exposure.
- Combined target/exit remains credible; no automatic distant target, unlimited rearming or martingale sizing.

For LONG with tranche entries E_i, sizes q_i, common stop S and known linear point value v, planned stop loss is sum[q_i*(E_i-S)*v] plus compatible friction. SHORT reverses distance. Weighted average is sum(q_i*E_i)/sum(q_i). If actual instrument/point value/risk policy is unavailable, report only declared paper-unit arithmetic or a qualitative zone; do not claim real monetary risk is bounded. Stop slippage remains additional risk.

Original hypothetical illustration: long 1 paper unit at 100, stop 94, preplanned second unit at 97. Average becomes 98.5, but stop risk increases from 6 to 9 point-units, not decreases. A total cap of 6 blocks that add; a cap of 9 reserved before initial entry may permit it if all other conditions hold. These are invented unit examples, not suggested trade sizes or index levels.

For this draft, add policy defaults WATCH_ONLY and partial/trailing rules OFF unless explicitly supplied. User may configure them for research without another skill. No order is placed. Do not reject a valid management review simply because additions are off.

## Stable recommendations

Per trade return one primary action: HOLD, TAKE_PROFIT, REDUCE, CLOSE, ADD_WATCH, ADD_CANDIDATE or REVIEW_REQUIRED. Hard invalidation/committed exit takes precedence over additions and new entries. Optional stop-tightening proposal may accompany HOLD only under policy. No widening; no taking partials without a supplied valid fraction/size policy.

Reference supplied trade ID, state revision, context cutoff, evidence, original versus current thesis, exact applicable exit/add levels and remaining size where available. Recommendations reference pending action IDs when supplied; the application validates/idempotently commits them. The AI cannot mark a trade closed, revised or enlarged until an authoritative event confirms it.

## Trend phase and trailing interpretation (v0.6)

A confirmed defended higher low after renewed directional progress differs from a minor low inside a developing upper range. The former may justify tightening under policy; the latter can be crossed during normal range rotation. Premature breakeven stops can eject an intact small-pullback swing. No automatic breakeven, partial fraction or trailing threshold is added. Assess weakening continuation/projection premises and make an evidenced policy-authorized exit proposal when the objective becomes unrealistic; keeping a committed target does not require holding after thesis failure. Protective stop events and independent monitoring retain precedence. See [source management distinctions](trends-and-ranges.md#8-trade-mathematics-and-management-fidelity).

## Requested swing baseline (v0.7)

Hold through normal small opposite bars when the defended swing and original target premise remain intact. Review sustained opposing acceptance and major structure failure; do not convert every opposite setup into an exit. Report original structural stop separately from any tactical proposal. Full-swing stop selection occurs before entry; after entry no widening is permitted. Wider initial price risk requires proportionally fewer paper units under the unchanged risk budget. Source chapter 29 distinguishes minor pullback extremes from confirmed swing structure and warns against protection at a weak pause in a developing upper range.
