# Trade geometry, expected movement and trader's equation

Use for each new plan and relevant open-trade review. Work in underlying price units; options are deferred. No measured probability or profitability is established by these rules.

## Stop first: what defeats the thesis?

Identify structural invalidation from actual causal evidence, then derive the stop reference using supplied buffer/tick policy. Do not start from a desired risk distance and find a convenient nearby candle. Distinguish the structural idea from the operational protective level; if either is missing, disclose it.

- Continuation: relevant corrective extreme / defended structure, not automatically the signal-bar low/high.
- Breakout pullback: the actual test extreme / failure of the defended boundary, with frozen tactical-versus-structural stop rule.
- Wide-range rotation: failure beyond the relevant excursion/edge structure; not arbitrary middle-of-range protection.
- Enabled reversal: the tested extreme whose defeat invalidates that reversal. Disabled families remain observations.

Never widen an existing stop to accommodate an adverse move or addition. A stop-triggered episode is invalid/closed according to supplied authoritative state, not an invitation to rescue it. Price gaps can exceed planned risk; a stop is not a guaranteed fill.

## Expected move is a conditional scenario

Select the context-appropriate anchor before evaluating reward/risk. Record anchor bar IDs, prices, creation/confirmation time and projection method. Do not change anchors after observing a favorable outcome.

| Target mode / context | Committed initial objective | Nearer level treatment |
| --- | --- | --- |
| MEASURED_SWING: supported directional continuation | Leg-1=leg-2 with causal confirmed anchors, when policy allows | Prior extreme may be a checkpoint if passage is supported; major opposition can veto/restrict the plan |
| MEASURED_SWING: accepted initiating breakout or test | Established range-height or initiating-leg projection under policy | Broken boundary/relevant extremes remain evidence checkpoints, not automatic exits |
| FIRST_OPPOSITION: weaker or unresolved extension | First meaningful opposing structure | Do not assume full measured-move travel |
| RANGE_ROTATION: wide established range | Defensible internal level / midpoint | Far edge is not automatically the objective |
| Qualified opening reversal | Justified new-swing projection or first opposition, chosen before entry | A gap magnet alone does not determine the objective |

Target mode comes from supplied policy; absent permission for a measured-swing commitment means scenario-only/WAIT for that plan. Select the objective from the thesis before evaluating reward/risk. Record why each intervening obstacle is checkpoint, major opposition or unresolved. A good ratio alone cannot turn an unsupported projection into a valid target.

Long leg projection: for an identified prior upward leg A->B and a confirmed correction endpoint C, projected D=C+(B-A). Short counterpart: prior down leg A->B, projection D=C-(A-B). Range-height projection: H=upper-lower; upward target upper+H, downward lower-H. These are reference scenarios, not assured distances.

A correction endpoint is not known merely because the next unseen rally eventually starts there. Use available confirmation or label C provisional and withhold a precise armable projection. Nearby opposition can make a full projection unsuitable as the initial target. Keep checkpoint, committed objective and optional non-binding scenario separate. A justified measured-move objective can be the initial target in MEASURED_SWING mode; do not mechanically exit at a nearer checkpoint. Never manufacture a distant target to improve the equation.

'Expect a second leg' does not require exact equality or a fixed number of bars. No universal ten-bar duration, two-leg completion, doubling target or fixed R applies to every trade. [Brooks's measured-move overview](https://www.brookstradingcourse.com/price-action/10-best-price-action-trading-patterns/) motivates the scenarios; their probabilities must be evaluated separately on these indices.

## Geometry and expectancy

For LONG entry E, stop S and target T: risk R=E-S, reward W=T-E. SHORT: R=S-E, W=E-T. Require positive R/W and a prospective valid entry. Compute reward/risk W/R from supplied prices. Recompute geometry at eligible entry after acceptance; do not report stale signal-bar geometry.

Brooks's [trader's equation](https://www.brookstradingcourse.com/price-action-trading-terms-glossary/) compares p*W against (1-p)*R. With average round-trip friction C expressed in the same underlying-equivalent units, binary-outcome expectancy is p*W-(1-p)*R-C; break-even probability is (R+C)/(R+W). Without C, report gross break-even R/(R+W), costs unknown. If break-even exceeds 1, that fixed-payoff model cannot be favorable even at p=1.

p means the probability of this specified objective before this specified loss under this holding/exit policy. It is not merely 'price probably rises,' regime persistence, model confidence or the 80% inertia heuristic. Early exits, partials and additions change outcomes; the simple binary formula then becomes a scenario approximation. Full policy expectancy needs the actual distribution of net episode P&L.

## Probability provenance

When no applicable calibrated estimate is supplied, set estimated_success_probability null. Describe evidence favoring continuation/range rotation or arguing against it; calculate required break-even probability without declaring positive expectancy proven. Do not insert Brooks's generalized 40/60/80% teachings as measured forecasts.

If an estimate is supplied, record source, setup/context cohort, stop/target/horizon/management compatibility, sample and uncertainty. An estimate calibrated for a different payoff geometry or contract cannot be silently transferred. Scenario assumptions are explicitly hypothetical. A plausible pattern and a good ratio can qualify as a research candidate, but profitability remains UNVERIFIED and an application may require a configured probability gate before accepting it.

Suggested equation status: PROBABILITY_UNVERIFIED, ESTIMATED_FAVORABLE, ESTIMATED_UNFAVORABLE or NOT_COMPUTABLE. Favorable requires compatible supplied estimate/costs/policy and still does not guarantee success. No fixed numeric minimum ratio is prescribed; use the owner's frozen policy.

## Open-trade review

Keep original entry geometry and current remaining geometry separate. At current price P, remaining LONG room T-P and downside P-S; SHORT mirrors it. Do not mechanically reuse entry-time p. Decide whether thesis, first objective and exit conditions remain supported. Original entry is a reporting fact, not a reason to hold a thesis that failed or a reason to exit a healthy one just at breakeven.

## Stable plan and causal anchor record

Each projection records method, direction, A/B/C or range-boundary IDs/prices, their known/confirmed-at cutoffs, projection price, current premise status and invalidation. Provisional C or unknown boundary confirmation permits a scenario, not a confirmed numeric target. Preserve original anchors/objective for every filled position; new evidence can invalidate a scenario or propose a policy-authorized revision, never rewrite prior expectations. Record checkpoint rejection/acceptance during management. If targets/partials/trailing are fixed, the skill cannot override them. No probability for reaching the projection is established by geometry.

## Additional source-based projection methods (v0.6)

See [projection geometry](trends-and-ranges.md#7-measured-move-geometries). `SPIKE_EXTENSION` uses D=B+(B−A), with the selected spike start/end convention and endpoint confirmation time. It differs from `LEG_EQUALITY` projected from a subsequent correction endpoint C. `MEASURING_GAP` uses D=M+(M−A), where origin A and gap midpoint M are causally known and a measuring-gap premise is supported. Range-height remains its distinct method. Signed formulas mirror down moves. Record the gap edges, whether the gap is positive/negative, and why it is a plausible measuring gap rather than exhaustion. Unknown/developing endpoints remain scenario-only.

Multiple open/close/high/low conventions can give different targets; the supplied policy must select one before an armable plan. Preserve alternatives as non-binding scenarios, never choose retrospectively. Book guidance permits flexible projections; this system records those revisions separately from committed objectives. No new method is enabled merely because it is documented. Probabilities of equidistant direction and this objective before this stop are different and require compatible provenance.

## Swing-stop and target fidelity (v0.7)

The user requests swing participation with room for normal adverse movement. Declare `trade_intent` before building geometry; do not manage an intended swing as a scalp.

- A swing continuation initially protects the defended major higher low/lower high or initiating structure. A one-bar pause, doji extreme or tiny local flag is not automatically the defended swing. Cite the structure's origin, confirmation and what breaking it would invalidate. If the entry is a full corrective test, its complete extreme can be the structural reference when that test has actually established the defended swing.
- An accepted initiating breakout initially protects the opposite side of the relevant base or initiating swing. A weak first pause after escape has not yet earned a tighter major-swing stop. For a reversal, protect the failed initiative/tested extreme. Distinguish these from separately configured tactical variants.
- A later higher low/lower high becomes eligible for policy-authorized tightening only after observed resumption and new directional progress confirm its role. No automatic breakeven, entry-bar or minor-pause tightening in the requested swing baseline. Never widen a filled trade's original stop.
- Judge ordinary pullback tolerance relative to observed bar size and the initiating structure. A noise-distance diagnostic can reject a proposed tactical-looking stop under a frozen research convention; it must not manufacture a farther arbitrary stop. A wider stop changes sizing, not the monetary risk budget. If the genuine stop is too far for supported reward, skip the trade.
- Select a causally supported leg-equality, spike-extension or range-height objective for a swing. A previous high/low can remain a checkpoint only with evidence that continuation is credible. Major opposition still vetoes/restricts a target; do not push the target outward just to satisfy a ratio. Weak/range context receives inward geometry or a skip, not an artificial swing.
- Brooks describes risk-multiple profit objectives as well as measured moves and opposing structure. A project may freeze a 2R swing eligibility threshold; it is a system choice, not a universal Brooks law. Never use future realized adverse excursion as entry-time “actual risk.” Initial risk is available before entry; realized excursion is an outcome diagnostic.

Source review: supplied Trading Ranges PDF chapter 29, PDF pp.1018–1024 and 1027; chapter 30, pp.1055–1057, 1060, 1063 and 1065–1066. These chapters also describe tactical stops, discretionary tightening and scaling; the requested swing baseline is one explicit adaptation, not every method in the books. Brooks explains the sizing consequence of a more distant stop in [trade management and position sizing](https://www.brookstradingcourse.com/ask-al/trade-management-position-sizing/) and the danger of swinging internal range legs in [trading range days](https://www.brookstradingcourse.com/ask-al/trading-range-day-two-legs-swing/).

Initial entry versus trailing distinction: a new context-qualified H2/L2 or first-pullback entry can protect the entire corrective swing/test once the supplied resumption confirmation is present; it need not always risk back to the origin of the preceding impulse. The requirement for new directional progress before tightening concerns a filled position's trailing stop. Do not use it to replace every new pullback's corrective stop with the entire old impulse. Conversely, an initiating breakout's tiny first pause cannot automatically replace its base protection. Stop selection must match the specific thesis, not use the widest possible historical extreme indiscriminately. Bar-size multiples are diagnostics unless the user's frozen policy explicitly makes them gates.
