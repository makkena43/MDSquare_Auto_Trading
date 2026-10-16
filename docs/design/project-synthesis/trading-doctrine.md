> **Precedence:** The [v2.3 canonical specification](../automatic-trading-technical-specification.md) and [unified skill](../brooks-index-analysis/SKILL.md) govern the current design. This earlier synthesis is supporting background; options and real execution are deferred.

# Trading doctrine and deeper strategy review

Version 0.1.0, 11 October 2026. Original design hypotheses, not a claim of professional trading credentials, demonstrated edge or completed performance testing. Companion to implementation-readiness.md and technical specification v1.6. No new strategy fitting or code implementation is performed here.

## The trading proposition

The hypothesis is that a versioned AI playbook can distinguish useful continuation or range-failure opportunities from superficially similar weak patterns, using causal market context, and that a fixed executable policy can capture enough movement to exceed option costs and operating costs. This contains three testable claims: interpretation consistency, economic usefulness and practical executability. Failure of any one can make the whole project unprofitable.

The most promising initial role for AI is context assessment and disciplined rejection: where the pattern occurs, strength of the preceding move, competing interpretations, remaining target room and what would invalidate the thesis. AI does not gain a measured probability merely by recognizing a familiar diagram. Keep every eligible five-minute assessment as requested, but do not require an actionable plan at every assessment.

The pattern is only one part of a trade. The complete object is regime + location + observable sequence + confirmation + entry timing + structural invalidation + attainable target + executable contract + account exposure. A missing economic or execution component can reject an otherwise valid pattern.

## What the evidence currently supports

Our public-data audit supports ingestion/replay planning: 30 sessions per index downloaded, one paired date quarantined for exact duplication, 29 internally consistent paired sessions under an unverified timestamp convention. Descriptive return correlation and volatility variation justify shared risk accounting and evaluation across regimes. They establish neither pattern frequency nor expectancy. Five selected sessions in a month are not its complete distribution.

The supplied books and Brooks's [pattern overview](https://www.brookstradingcourse.com/price-action/10-best-price-action-trading-patterns/) provide terminology and examples. His discussion acknowledges overlapping labels and the importance of context. That is a reason to record one opportunity with multiple evidence tags, not multiple positions. Generalized probabilities on that page are not NIFTY/BANKNIFTY estimates and will not be imported into sizing or scores.

## Distinguish taxonomy from trading regimes

Keep the user's seven categories as enable/disable controls. Bullish/bearish describe direction; momentum/mild describe contextual behavior; breakout/reversal/sideways describe mechanisms. They are not mutually exclusive market states and do not represent seven independent sources of profit.

Use a separate regime assessment. The existing coarse enum remains BULL_TREND, BEAR_TREND, TRADING_RANGE, TRANSITION or UNKNOWN. Proposed optional subtypes carry the distinctions below without silently changing the current schema. Each assessment cites current evidence and alternatives; no subtype is a calibrated probability.

| Observable condition | Favored research behavior | Common failure |
| --- | --- | --- |
| Directional impulse / tight continuation | With-direction pullback assessment; avoid chasing a missed impulse | Calling each new extreme a top/bottom |
| Directional move with broad corrective swings | H2/L2 near defensible structure; smaller conviction about continuation | Treating broad channels as tight trends |
| Established range with room between edges | Failed breakout back toward an internal reference | Buying/selling in the middle or fading a strong accepted break |
| Compressed overlap / tight range | Wait for clearer structure; observe break attempts | Small targets overwhelmed by spreads and confirmation delay |
| Transition after structural break | Track both continuation and reversal scenarios | Declaring a new opposite trend on the first opposing bar |
| Unknown or contradictory context | Wait/insufficient data with explicit missing evidence | Forcing a regime label to produce a trade |

Regime updates need observable event reasons. Record what changed: acceptance outside a prior boundary, a structural failure, a retest or sustained overlap. Do not flip regimes solely because the current candle changes color. Numerical hysteresis is a hypothesis to specify/test, not an arbitrary hidden rule.

## The three pilot families as economic hypotheses

| Family | Hypothesis to test | Necessary context | Rejection / competing interpretation |
| --- | --- | --- | --- |
| H2/L2 continuation | The corrective sequence ends and the prior directional leg resumes before meaningful structural failure | Defensible prior direction, corrective attempts counted from available bars, location with room | Ambiguous counting, congestion, exhausted target room, deeper correction becoming a range |
| Breakout pullback | A previously identified boundary has been overcome; its test supports continuation | Boundary known before the break, outside acceptance, actual test/resumption evidence | One spike without acceptance, repeated closes back inside, pullback already invalid, late chasing |
| Range failed breakout | Price returns to an established range and can travel toward an internal reference | Range established beforehand, edge excursion, completed inward return, usable distance | Range invented from later reversals, strong outside acceptance, interior noise, confirmation near target |

These are original operational hypotheses. Before scoring, specify equality/tick treatment, nested H2/L2 counting, swing confirmation, acceptance/test qualification and the maximum permissible trigger-to-invalidation distance. Conservative ambiguity handling must be uniform, not adjusted to whichever interpretation wins.

Start by measuring continuation families and range failures separately. Range trades are not automatically suitable for long options: confirmation and spread may consume their smaller available move. Keep all six pilot IDs in research, but permit each index/family/contract cohort to remain unproven or disabled for execution independently. No profitable-family selection on final holdout.

## Location and target construction

Build a causal level map: prior completed session/week extremes and closes; current observed open/high/low; completed opening range; published swing levels; pre-existing range boundaries. Every level carries source, creation time, confirmation time, price tolerance and expiry/update rule. Nearby levels are zones with provenance, not dozens of lines that ensure a hindsight match.

Choose the thesis's first meaningful opposing obstacle before entry. A measured move is a projection, not guaranteed travel. A range midpoint is a candidate destination, not proof the midpoint will be reached. Daily alignment can contextualize an intraday move but cannot force it to agree with the daily direction.

Evaluate target room from the price available after acceptance/at trigger, not only the original signal high/low. A trade that looked attractive on the signal bar may be unattractive after delayed confirmation. Record both original and executable geometry. Reject if the configured economics no longer hold; do not move the target farther away to rescue reward/risk.

## Time and confirmation are part of the strategy

Separate four clocks: source bar availability, model acceptance, actual underlying trigger and option execution. The five-minute bar close is not the fill time. Collector finalization, inference and queue delays can consume the opportunity. Missing the trade is a valid result.

Evaluate latest usable entry displacement, quote deterioration and remaining time to the configured target/flatten boundary. Thresholds must be fixed in the charter. Never buy a late signal merely because the direction subsequently proved right. Trigger monitoring and exits operate at the required event frequency independently of five-minute AI calls.

Describe session phases relative to the maintained calendar: opening discovery, established session and approach to entry cutoff/flatten. Time-of-day is a research dimension, not a claim that a fixed lunch or opening filter improves NIFTY. Known scheduled events are as-of risk context; later explanations of a price spike are forbidden inputs.

First-hour opportunities may lack a stable intraday range but have prior-session context. Do not automatically impose a long waiting period on every setup or assume the first bar is sufficient. Opening-range duration is a versioned parameter; observing an opening range does not enable an opening-breakout setup that is currently disabled.

## Opportunity episodes, not repeated candle trades

Give related proposals an episode identity: underlying, direction, causal boundary/leg, correction sequence and thesis version. An H2 and breakout-pullback interpretation can refer to one episode. One position cannot become multiple trades because the AI renames the same structure.

Use a fixed primary-label precedence for bookkeeping and preserve secondary tags. Following entry, future candles may assess the market but cannot re-enter the consumed episode automatically. Define re-entry requirements explicitly: new corrective structure, new signal, independent current geometry and risk eligibility. A stop-out alone does not create permission to try again.

Pending plans must expire, invalidate or be explicitly amended. A new AI call cannot repeatedly roll expiry forward or quietly shift invalidation. An episode journal records why a plan changed and whether new evidence truly supports a distinct opportunity.

The earlier one-five-minute-interval expiry proposal may miss legitimate slow trigger sequences. Treat it as an engineering hypothesis to evaluate, not established Brooks practice. Compare a small predeclared set on development/validation; freeze before final evaluation.

## Option expression can reverse the economics

An underlying thesis specifies direction and structure. A contract expresses it with sensitivity to price, time and implied volatility; those inputs influence premium. See [OCC/OIC on option Greeks](https://prd-web.optionseducation.org/advancedconcepts/understanding-options-greeks). A correct directional view can lose if its move is too small, too slow, expensive to enter/exit, or accompanied by adverse volatility repricing. Greeks are local sensitivities, not assured P&L.

Avoid selecting the cheapest premium as a proxy for low risk. Evaluate point-in-time expiry, moneyness/delta, spread, depth, quote age, premium exposure and actual lot affordability. Select through a frozen deterministic policy; record why alternatives were rejected. Do not use current-day end-of-day liquidity or future best-performing strike to choose a historical contract.

As checked on 11 October 2026, [current NSE specifications](https://www.nseindia.com/static/products-services/equity-derivatives-contract-specifications) list NIFTY weekly/monthly options and BANKNIFTY monthly plus quarterly contracts. An [older BANKNIFTY weekly page](https://www.nseindia.com/static/products-services/equity-derivatives-bank-nifty-option-contract-specification-weekly), updated in 2021, remains accessible. Therefore historical option results must be stratified by actual contract era and time to expiry; today’s policy cannot synthesize historical or current contracts from a fixed weekday. Runtime broker contract metadata is authoritative for selection after validation.

Suggested initial experiment scope is one documented liquid contract cohort per index and no expiry-session execution until separately evaluated. This is a proposal, not an activated restriction or a proven optimum. ATM versus ITM and short versus longer dated choices are trials, not free optimization knobs. Missing usable quotes means underlying-only research.

## Define three kinds of risk separately

1. Underlying thesis invalidation: the market observation that defeats the idea.
2. Planned executable loss: option quantity, actual entry/exit conditions, premium protection and expected friction. This can be exceeded by gaps or failures.
3. Conservative capital exposure: premium paid plus charges for unlevered long options, alongside account-wide reservations. A stop is not a guaranteed maximum loss.

Do not set the underlying invalidation solely to fit a desired quantity. If the correct structure and lot affordability cannot fit the risk policy, skip the trade. Do not approximate an assured option stop from delta times underlying points.

Report R with one declared monetary denominator fixed at entry; show planned loss and conservative premium exposure separately. A report must not switch denominators between winning and losing trades. Raw points, premium percentage and monetary R are distinct metrics.

Both indices share exposure. Use account-level reservation plus a fixed policy for simultaneous similar-direction candidates; initial conservative proposal is one directional exposure episode at a time. If selecting between them, use predeclared executable eligibility/tie-break criteria, not model confidence or hindsight best performer. Opposite call/put ideas are not automatically a hedge; use a tested exposure policy.

## Exits deserve equal specification

Freeze an initial exit policy before measuring any entry edge. Define protective premium behavior, underlying invalidation, target handling, time/no-progress exit, entry cutoff and session flatten. Distinguish tick-based protective action from bar-confirmed discretionary thesis reassessment. Neither depends on an AI being available.

A simple first hypothesis: structural underlying invalidation plus explicit premium protection, one predefined target and mandatory session flatten. A time/no-progress rule is a separately declared component. This is not a validated policy or numerical recommendation.

Automatic breakeven at a small favorable move can truncate valid retests; partial profit-taking changes payoff and may be impossible with a single lot. Do not promise scaling/partials before integer-lot feasibility is established. Evaluate trailing/partials as new trials rather than adding them after a disappointing test. AI may explain changed context, but the initial policy must not permit unbounded discretionary exit improvisation.

## Trade economics and enough opportunities

For an illustrative binary model, with gross average win W, gross average loss L and average per-trade friction C, expectancy is p*W - (1-p)*L - C. Break-even win rate is (L+C)/(W+L). These averages must use consistent monetary units and include the actual payoff distribution when estimated; this formula is not a calibration method.

Illustration only: W=1R, L=1R, C=0.15R and p=55% yields -0.05R per trade; break-even is 57.5%. A seemingly good hit rate can still lose. These numbers are not broker cost estimates, a suggested target or measured strategy results. Daily AI/runtime costs must also be included in account economics without double-counting them in per-trade C.

Trade frequency must be measured through a funnel: eligible contexts -> qualified episodes -> accepted plans -> timely triggers -> option/risk-eligible executions -> fills -> net outcomes. Loss at each step matters. Monthly observations are not independent simply because there are many candles or two indices.

Track MFE/MAE and time to excursions as post-trade diagnostics only. They can diagnose late entries and exit mismatch, but selecting perfect hindsight exits creates another overfitting trial. No minimum monthly profit probability can be inferred before observing costs, payoff, clustering and instability.

## Prove AI contribution explicitly

Use paired shadow policies on identical contexts: deterministic pilot baseline, AI-assisted pilot and no-trade/account-cost reference. Freeze contract/exit/risk/fill rules for fair comparisons. Measure differences in bad entries avoided, useful entries missed, incremental net results, drawdown, abstention, operational latency and cost. More fluent explanations are not evidence of improved trading.

Avoid evaluator anchoring: prior processor/session summaries remain hypotheses with expiry and evidence IDs; each assessment receives current facts and contradictory evidence. A provider change may change interpretation, but not account facts or consumed episodes. Repeated stochastic runs belong to predefined development sensitivity tests, never hindsight selection of the best answer.

Compare pooled account outcomes and per-family outcomes, preserving day/paired-index dependence. Choose economic endpoints before holdout; do not declare success because one of many metrics is favorable. If AI does not add stable economic/reliability value, retain it for review/notifications or simplify the strategy. The charter must allow that conclusion.

## Gaps discovered in the current drafts

| Gap | Required resolution before strategy implementation/scoring |
| --- | --- |
| Qualitative examples use CANDIDATE without numeric prices while production requires numeric fields | Explicit research-only annotation type; such examples never submit to production decision validator |
| Strong acceptance, useful range, material break and good signal remain qualitative | Operational definitions, ambiguity handling and independently reviewed cutoff cases |
| Coarse regime loses tight versus broad structure | Optional context subtype with evidence and transition reason; version schema before adoption |
| Candidate expiry and late-entry geometry insufficiently evaluated | Acceptance-time displacement, expiry/re-entry policy and latency stress |
| Outcome depends on underspecified exits/contracts | Freeze policies before entry performance claims |
| Cross-index plan selection lacks a concrete tie-break | Fixed executable eligibility/priority; no hindsight or model confidence ranking |
| Historical contract regimes differ from today | Point-in-time master and era/expiry cohorts; no identical-expiry assumption |
| Repeated signals can inflate trades and sample size | Episode IDs and consumed/re-entry rules |
| Book case labels are not independent ground truth | Reviewer disagreement/ambiguity registry; score justified abstention separately |
| Source timestamps/availability are unverified | Data foundation gate remains mandatory |

## Concrete decisions before coding the strategy

### Admission scenarios to specify before testing

| Scenario | Required behavior |
| --- | --- |
| Valid H2 but prior resistance is very close | Recognize the pattern; reject execution if configured geometry/economics fails |
| Range edge break has strong outside follow-through | Do not fade it merely because an edge was exceeded; reassess breakout context |
| Trigger crossed while AI was still processing | Record missed trigger; do not create a historical fill or chase automatically |
| Signal still valid but accepted entry is materially worse | Recheck frozen late-entry/target-room rule; do not stretch target or tighten structural stop to fit |
| One lot exceeds the risk or premium cap | Skip execution; preserve the underlying observation |
| Both indices qualify in the same direction | Apply shared reservations and fixed tie-break; never double risk by treating correlated ideas independently |
| Broad daily bull context, valid local bear sequence | Record conflict and assess local eligibility; do not impose an automatic daily-direction veto |
| A disabled reversal overlaps an enabled continuation tag | Do not relabel to bypass config; evaluate the actual enabled thesis independently |
| Setup changes name on the next bar | Preserve episode identity; require genuinely new structure for another plan |
| Provider changes with an armed plan | Preserve its expiry/consumption and account facts; new interpretation cannot reset risk |
| Target and invalidation both touched inside one historical bar | Flag chronology ambiguity; no favorable assumed fill ordering |
| Attractive spot setup, stale option quote | Underlying observation can remain; execution blocked |

### Two synthetic economic examples

These prices are invented illustrations, not observations or trade recommendations. A long plan at 22,010, structural invalidation 21,980 and first obstacle 22,040 has 30 points on each side. If the usable entry is delayed to 22,025 with the same structure, room is now 15 points versus 45 points of underlying risk. The original diagram is unchanged, but its executable geometry has deteriorated. This ratio still says nothing definitive about option payoff.

For a synthetic option quote of bid 100 / ask 102, buying at 102 and later selling at bid 101 loses one premium unit before fees, even if the later quote is bid 101 / ask 103 and its midpoint has risen. Directional premium movement can be smaller than the cost of crossing the spread. Actual outcomes require quantities, quotes, costs and timing.

Prepare a frozen strategy card for each pilot family: eligible regimes, level construction, sequence counting, signal quality, confirmation, maximum late-entry displacement, invalidation, target method, expiry, re-entry, contract cohort and exits. Parameters can remain unset during ingestion work, but unset strategy/risk fields block arming and scoring economic results.

Recommended sequencing: (1) verified data and episode/context contracts; (2) numerical labels/counterexamples and simple baseline; (3) AI shadow interpretation with full missed/failed-decision records; (4) actual option paper pipeline; (5) frozen chronological plus prospective evaluation; (6) separately authorized limited execution. Avoid completing a large execution platform before determining whether the decision policy adds value.

## Trading judgment

This is a credible research project because it can make observations, versions and execution constraints explicit. Its central unresolved issue is economic edge, especially after confirmation delay and long-option friction. Adding patterns, more context or another provider can add complexity without improving that edge. The first success criterion should be a reproducible decision policy that handles uncertainty and no-trade conditions; profitability is a separate measured gate.
