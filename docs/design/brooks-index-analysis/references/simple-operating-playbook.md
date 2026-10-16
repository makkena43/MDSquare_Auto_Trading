# Simple operating playbook

Version 0.13.0. The default five-minute workflow for the unified skill. Detailed references explain difficult cases; they are not separate strategy engines or a checklist to print at every candle. This is requirements guidance, not implemented trading software.

## The everyday flow

First read supplied open positions, pending plans and current evidence. Unknown inventory is not flat. Review every supplied open trade, then assess a new opportunity if allowed.

1. **Context:** bull trend, bear trend, wide range, tight range or unresolved transition. Use daily background without letting it override intraday behavior. Retain the current swing/correction; ordinary overlap or one opposite bar need not change it.
2. **Location:** trend pullback/test, meaningful breakout, or correct wide-range edge. Avoid genuine tight congestion and range-middle entries. Identify the nearest meaningful obstacle and any stronger barrier on the path to the objective.
3. **Setup:** recognize a relevant enabled entry, cite its actual sequence and completed confirmation. A pattern without supporting context is not enough. Breakouts can change context under their declared policy. Weak-looking trend signals and strong-looking countertrend signals need contextual interpretation.
4. **Plan:** choose one structural stop and one supported initial target. Protect the complete correction/base/excursion appropriate to the thesis. Use a causal measured move for a supported swing or an inward objective for range rotation. Calculate the supplied-policy economics; skip if room is inadequate. Do not shrink the stop, stretch the target or invent probability.
5. **Decision:** CANDIDATE when all requirements are complete; WAIT for developing/ambiguous evidence; SKIP a known unsuitable opportunity; INSUFFICIENT_DATA for required missing/unreliable evidence. Already crossed/missed/expired plans do not become historical fills.

This is one reasoning flow. Do not mechanically enumerate all twelve IDs, all book principles, all timeframes or every possible projection. Use the setup that best describes the opportunity, with secondary observations only when they change the decision.

## Where each entry fits

| Context/opportunity | Typical enabled route | What matters most |
| --- | --- | --- |
| Supported trend corrects | First pullback, H2/L2, breakout test/resumption | Full correction, continuing parent swing, room to justified objective |
| Meaningful boundary breaks | Breakout continuation or actual pullback/test | Configured acceptance, credible change, still-prospective entry |
| Established wide range rejects its edge | Genuine failed breakout or declared H2/L2 inward variant | Correct outer edge, real enabled sequence, inward confirmation and room |
| Opening initiative credibly fails | Qualified enabled opening reversal | Failed attempt at known structure, opposing evidence and new-direction confirmation |

These are presentation groups, not new setup IDs, category switches or independent engines. Existing category/individual controls still govern. Additional wedges/microchannels/double tests can explain context without creating extra entries.

## Keep only decision-relevant state

Carry the current parent context, active swing, complete current correction/extreme, meaningful obstacle(s), original/pending plan and authoritative inventory. A compact snapshot can reference prior history instead of duplicating it. Retrieve an older slice only when needed to answer a specific structural question. Do not require a general-purpose graph of every historical swing or continuous multiple-thesis tracking.

Preserve ancestry and revisions when they affect decisions. A nested pause cannot erase an earlier correction extreme; later acceptance cannot shift already-observed structure. Those facts can be recorded as a small thesis record with referenced evidence. Detailed swing-map/ledger representations are optional elaborations for ambiguous cases and implementation review; causal identity, availability and handover consistency remain required.

## Open trades: the simple baseline

- **HOLD:** original structure/objective remains defensible; a small opposing move or checkpoint touch alone is not a close signal.
- **TAKE_PROFIT/CLOSE:** supplied objective/protective event or session policy applies, or cited evidence defeats the premise under the declared exit policy. Actual events establish fills/closures, not the recommendation.
- **REVIEW_REQUIRED:** authoritative state or essential evidence is missing/ambiguous. Preserve known protection.

No automatic breakeven, partials, trailing, reversing or averaging is required in the simple baseline. Those remain separately configured possibilities; add zones can be WATCH_ONLY. Never widen a filled stop or use a new target to rescue the trade.

## Compact user-facing response

Use one short result per index:

- **Context and action:** current behavior; candidate/wait/skip or open-position action.
- **Setup and location:** only when relevant.
- **Entry / stop / target:** only for a complete new candidate, or supplied original protection during open-trade review.
- **Reason:** controlling evidence, strongest relevant contradiction and what would change the decision.

A WAIT/SKIP does not include an armable numeric plan. Do not print schema, revision trees or eight check statuses unless requested. Required provenance/evidence belongs in the structured record/history, not repeated user prose. Calibrated probability is unknown unless compatible evidence exists.

## Load detail only when it changes the answer

Use the economics reference for plan geometry; swing/adjudication guidance when ancestry or regime is unclear; market-cycle guidance for unusual signal/phase behavior; management for supplied positions; contract/context for structured submissions or handover. Source coverage, compatibility audits and acceptance scenarios are development/review material, not recurring candle input.

The source-quality gap, policy registration and independent evaluation remain open. Simplicity does not create an edge or authorize orders; it removes unnecessary reporting and structural machinery while retaining the decisive constraints.

## Each new candle: retain, revise, or withdraw

Keep the current view when new evidence is a normal correction or adds no meaningful structural information. Update observed extremes and evidence without inventing a new thesis. Revise the view when actual opposing acceptance or lost structure warrants it; state which prior condition changed. If context is unresolved, WAIT rather than repeatedly oscillate bull/bear from bar color.

Do not use a fixed number of opposite bars as a universal reversal/exit rule. The relevant question is whether the original defended structure and expected movement remain credible under the supplied policy. A daily background can persist while an intraday swing changes.

| Supplied opportunity/position state | What the next review does |
| --- | --- |
| Flat, no valid pending plan | Assess one relevant new opportunity through the normal flow |
| Unfilled valid pending plan | Retain its original trigger, expiry and episode; review premise, but do not rearm the same idea or roll expiry forward |
| Pending premise defeated/expiry reached | Recommend withdrawal or report the supplied expiry event; cancellation is not assumed until authoritative confirmation |
| Open position | Review original stop/objective and thesis first; new annotations do not replace the committed plan |
| Exit/cancel already pending | Refer to the existing action; do not create a duplicate or claim completion |
| Closed/missed/expired episode | Preserve the result; a later opportunity needs distinct structure and the declared reentry policy |
| State or relevant source evidence unavailable | REVIEW_REQUIRED for an affected open position; INSUFFICIENT_DATA/WAIT for the affected new interpretation |

Entry-plan expiry blocks a future fill; it does not expire a filled position. A protective stop closes the trade under its policy but does not prove the entire parent trend reversed. Likewise, reaching a fixed objective does not prove a market top/bottom or authorize an opposite entry. Keep market interpretation separate from episode facts.

## Same pattern, different answer

These are illustrative interpretations, not completed numerical trade plans or evaluated historical cases.

| Observation | Context/location | Working response |
| --- | --- | --- |
| H2 | Supported bull swing, full corrective structure, no unaddressed target barrier | Assess an enabled continuation long; CANDIDATE only if current confirmation, geometry and policy are complete |
| H2 | Strong bear trend without credible change | SKIP the unsupported continuation-long thesis; a count does not establish reversal |
| H2-shaped bounce | Bottom of established wide range | Assess inward rotation under a complete enabled route; do not assume a failed excursion occurred when it did not |
| H2 | Middle/top of a persistent range | Avoid the poorly located long; pattern name does not create room |
| Strong opposite bar | Intact swing with limited opposing success | Review as correction; no automatic entry/exit reversal |
| Strong opposite movement | Defeated defended structure or credible opposing acceptance | Revise context and review the original position under exit policy |
| Strong breakout | Meaningful outer boundary and required acceptance | Assess the initiating route or actual test route; do not demand an invented retest |
| Strong bar near a range edge | Boundary is still defended | Treat breakout as unresolved, not automatically a trend |

Apply the corresponding relationships for L2/shorts. Other patterns follow the same context/location/confirmation logic; H2 is an example, not the sole strategy. Observe only the relevant alternative that could change the decision.

## Quiet output, complete history

Assess each eligible completed candle and preserve its decision/evidence in history. User-facing notifications should focus on a new qualified opportunity, material premise change, supplied fill/exit/expiry, or a data/state issue affecting a decision. Do not notify the same unchanged WAIT or reissue the same candidate each candle. Exact notification preferences remain configurable. This does not imply a notification service already exists.

## The small policy needed before numerical paper decisions

Keep setup/category switches, confirmation/trigger conventions, stop/target method and buffer, expiry/reentry, paper units/cost/risk limits and management/session cutoff explicit. These may be a compact configuration, not many separate engines. Unchosen values remain requirements gaps. Do not inherit prior research parameters silently or multiply policy branches to make every chart produce a trade.

## Breakouts and trend days: the short rule

Distinguish fresh escape, continuation in an existing strong trend and late acceleration into opposition. Judge present behavior rather than the eventual day label. First-entry/H1-L1 routes can suit very strong context; do not always demand H2/L2. More confirmation can make the entry too late. A directional tight channel differs from horizontal tight congestion. Use the existing enabled route and declared variant, one defended structure and one justified objective; no chase, fabricated retest or automatic countertrend trade. Read [the focused reference](breakouts-and-trend-days.md) only when this distinction changes the answer.

For wide-range edges, a declared H2/L2 range-rotation variant can qualify without an outside excursion; a failed-breakout route still needs the actual failure. These interpretations use existing IDs and explicit policy, never silent enablement or range-middle chasing.

For reversal evidence, separate a normal correction, supported opposite swing and confirmed major reversal. A supported enabled new-direction route can qualify before the final MTR label; a pattern name alone cannot. A failed trade can lead to continuation, balance or reversal, so preserve its result and reassess rather than automatically reverse.

Use session timing as context and declared policy: the open can alternate before accepting direction; midday balance does not erase the morning initiative or guarantee its resumption; a late supported setup still needs permitted time. Opening-range size and a gap do not lock the day type. New evidence changes the current interpretation without rewriting earlier decisions.
