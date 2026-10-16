# Persistent swing context and participation

Version 0.8.0. A swing thesis is a causal interpretation, not a forecast, fill or binding market fact. Maintain it across completed candles and recheck its evidence. Application code persists accepted thesis revisions; the model proposes them. This reference governs swing interpretation; the regime, setup and economics references govern their respective details.

## Establish the swing before naming the entry

Identify the meaningful initiating move: accepted boundary breakout, opening attempt that failed with new-direction follow-through, or established directional leg resuming from a correction. Cite the origin, challenged structure, initiating/follow-through bars and first defensible correction. Do not label an ordinary internal range leg a new trend because it is strong.

Keep four distinct layers: daily/weekly location; intraday market regime; active directional swing or range rotation; local signal sequence. Five-minute entries may participate in swings extending across many candles. Completed 15/60-minute structure can clarify the parent swing, but neither higher-timeframe alignment nor a fixed holding duration is mandatory. Never use an unfinished higher-timeframe bar as confirmed evidence.

For each update retain: supplied thesis ID/revision, direction, initiating mechanism and anchors, evidence cutoff, parent regime, phase, defended structure, structural invalidation, opposing evidence, first obstacle and its significance, optional measured-move scenario, available entry routes, and next observable discriminator. Missing IDs remain null; describe structure without claiming durable state. Prior summaries are hypotheses and must be checked against prices.

## Phases and changes

| Phase | Interpretation | Entry/management implication |
| --- | --- | --- |
| FORMING | Directional initiative exists; acceptance/continuation unresolved | Observe or use a fully qualified enabled initiating family; no assumed full trend |
| IMPULSE | Supported directional displacement/follow-through | Assess breakout continuation without requiring this family to invent a pullback |
| CORRECTION | Opposing movement tests a still-defensible swing | Assess first or second pullback as supported; do not automatically reverse direction |
| RESUMPTION | Completed evidence supports renewed movement | Assess prospective continuation with current geometry; do not backfill a missed trigger |
| EXTENDED | Remaining distance or exhaustion/opposition makes a new entry unattractive | No chase; existing position follows its committed objective and policy |
| TRANSITION | Meaningful structural challenge/opposing acceptance weakens the swing | Maintain alternatives; no automatic countertrend entry |
| INVALIDATED | Stated structural/thesis conditions failed | Withdraw affected pending ideas; review open-trade protection; never rescue with additions |
| UNKNOWN | Relevant structure or data absent/ambiguous | WAIT/INSUFFICIENT_DATA; retain uncertainty |

Phase is not a required linear sequence. A trend can correct repeatedly or change directly to transition. Explain changes with old and new evidence, not a new label on every candle. Distinguish weakening thesis from an actual protective-stop event.

## Correction versus independent range

A compact directional pause may retain impulse structure, limited opposing progress and a defensible continuation test despite overlapping candles. An independent range has meaningful two-sided acceptance, repeated rejection at shared edges and loss of directional progress. Width/overlap alone is insufficient. Cite preceding impulse, corrective depth/character, defended level and opposing effort. Do not rename genuine tight congestion a flag to bypass the entry prohibition. Ambiguity means WAIT.

A tight local range can exist inside a wide parent range; do not enter inside it. A clear flag is not automatically an independent tight range, but its entry still requires a qualified resumption/test under the selected family. In a broad channel, allow deeper corrections without automatically assuming a reversal; room and structural integrity still control entry.

## Opposition must be classified, not ignored

Label each relevant obstacle CHECKPOINT, MAJOR_OPPOSITION or UNRESOLVED, citing its causal origin and evidence. A prior extreme can be a checkpoint for a strong supported continuation; repeated failure at a defended range boundary can be major opposition. Proximity alone does not decide. State why passage is plausible and what observed rejection would defeat that assessment.

Strong context does not authorize inventing a target beyond serious opposition. If the beyond-obstacle thesis is not supported, target inward under policy or reject the swing entry. An established range ceiling remains meaningful until credible outside acceptance occurs. Do not require outside acceptance to an extent that silently turns the breakout-continuation family into breakout-pullback; use each family's supplied confirmation policy.

## Participation without a trade quota

For a supported swing consider distinct enabled routes: initiating breakout continuation; first controlled pullback/H1 or L1; deeper H2/L2; breakout test/resumption. Qualified opening reversals can establish a new swing but need actual failure and opposing strength. Do not demand H2 from a trend that has not produced a second corrective attempt. Do not relabel an already-triggered first entry as a new second entry.

One parent swing can contain several correction opportunities, but each needs a distinct causal episode and declared exposure/reentry policy. Several labels on the same correction remain one episode. No duplicate risk or unplanned stacking. Record why a potentially eligible route was not taken: disabled, incomplete structure, bad location/geometry, actual latency, expired plan, consumed episode, or missing data/policy. A countertrend signal in an intact strong swing is an observation unless credible change or an independently qualified wide-range rotation supports it.

## Measured-move integration

Use the economics reference for leg equality, spike extension, range-height or measuring-gap projections. These are distinct methods, with policy-selected anchor conventions; do not silently substitute one for another. Select anchors when available, record confirmation cutoff and invalidate scenarios when their premise fails. At plan creation choose RANGE_ROTATION, FIRST_OPPOSITION or MEASURED_SWING target mode under supplied policy. A measured swing can use a justified measured-move objective as its initial committed target and retain nearer opposition as checkpoints. It need not take profit automatically at every prior high/low.

Do not convert a filled first-opposition trade into a measured swing after favorable candles, or move anchors/targets to improve the result. No automatic partials, trailing or additions. A subsequent scenario revision remains separate from committed position facts; protective stop and target always follow authoritative policy/state.

## Contrast cases for development

- Strong bull impulse followed by a shallow overlapping pause: study a first continuation route; do not force H2 or declare a range from overlap alone.
- Strong bull bar reaching an already defended wide-range ceiling without acceptance: remain range-aware; do not excuse poor location with a measured-move label.
- Strong bear swing plus one bullish recovery: maintain correction/reversal alternatives; a marginal new-low failure is not an established range floor.
- Prior high is a checkpoint in a supported bull swing: document why continuation beyond it is plausible and freeze the projection before entry; do not auto-exit just because the level exists.
- Three failed passes of meaningful resistance with material opposing strength: reassess major opposition/transition; do not retain the bull label mechanically.
- Valid anticipated entry whose trigger crosses before actual decision acceptance: record missed execution separately from pattern quality; never count a retroactive fill.

These are hypothetical contrasts, not measured index performance or historical answer keys. [Brooks on missed swing trades and measured moves](https://www.brookstradingcourse.com/ask-al/missing-swing-trades-measured-moves-spikes/) motivates the distinction; operational classification requires separate evaluation.

## Persistent swing map and revision delta (v0.8)

Use a compact map of the relevant parent swing, its active directional leg and complete correction. A local flag may be nested inside it; the smallest visible pause is not automatically the parent correction. Preserve preceding context until observed evidence supports change.

For each relevant node propose these fields, using supplied IDs/revisions or null:

- `node_id`, `parent_node_id`, `kind` (SWING/LEG/CORRECTION/LOCAL_PAUSE), `direction`, `phase`, `origin_anchor`, `end_anchor` or null, `available_at` and `confirmation_status`.
- `origin_anchor` and each defended/end anchor contain a supplied bar/level ID, price field and value, source revision, `available_at` and `confirmed_at` or null. An observed extreme differs from a confirmed turn.
- `correction_ancestry`: all relevant contiguous correction segments from the first opposing activity, their full extreme, attempted resumptions, actual trigger crossings and renewed corrections. Cite interruptions; do not count colors alone.
- `defended_structure`: the full swing/correction/base reference, why its breach defeats this thesis, and confirmation evidence. Initial entry protection and existing-position trailing eligibility are distinct.
- `parent_regime`, `parent_range_id` or null, `opposition_level_refs`, `projection_ref`, `next_discriminator` and controlling opposing evidence.

Return `swing_map_update` with `base_revision`, `as_of`, `proposed_nodes`, `changes` and `unresolved_ancestry`. Each change includes supplied node reference or null, old/new phase or anchor, effective evidence cutoff, cited bars and reason. This is a proposal: code assigns durable identity and commits accepted revisions atomically; the model cannot assert acceptance. Local reconstruction without supplied identity remains research-only.

### Continuity rules

1. Extend the existing correction when its resumption failed to produce meaningful new directional progress. A nested pause or an interrupted first entry does not erase its earlier extreme.
2. A new accepted breakout can revise the swing thesis; preserve the prior node and connect the new initiative with an evidenced transition. Determine its peak and correction from the already-visible initiative, not automatically from the confirmation candle. Late acceptance cannot make earlier correction bars disappear.
3. A meaningful new higher high/lower low and a defended corrective turn may justify a new leg and a confirmed structure proposal. Cite the original correction and observed progress. Application policy decides whether an existing stop may tighten.
4. Keep a local strong leg separate from the parent day's range. Crossing an interior balance edge does not itself prove escape from the parent range. Major parent boundaries remain opposition.
5. Ambiguous ancestry means WAIT for the affected new plan and retain the ambiguity. Missing relevant earlier bars means INSUFFICIENT_DATA. Neither permits selecting the nearest convenient extreme.
6. Revisions preserve previous values, cutoff, rationale and input hash. A source correction creates a new revision with later availability; it never rewrites what was knowable in an old decision.

## Opposition ledger (v0.8)

Evaluate relevant levels between entry and objective from every applicable layer: prior sessions/week, parent intraday range, completed opening range, full swing/correction, rejected local extremes, breakout bases and configured causal projections. Do not scan only the previous day's high/low. Bound retrieval to levels relevant to this plan and record insufficient coverage.

For each relevant level return `level_ref` or null, price/zone, origin type, timeframe/parent scope, source anchors, `available_at`, rejection/test evidence and accepted-crossing evidence through the current cutoff. Return CHECKPOINT, MAJOR_OPPOSITION or UNRESOLVED with a reason. Touches and intrabar excursions are not accepted passage; use the supplied acceptance convention. A strong rejected excursion can matter before there are multiple tests; no universal wick threshold or number of touches is introduced.

For a proposed target beyond a level, record the specific `passage_thesis`, its support and `failure_discriminator`. Repeated range-edge rejection, credible opposing strength and lost progress weigh against calling it a checkpoint. Proximity and an attractive ratio cannot make opposition disappear. Credible contextual change can make a prior boundary a checkpoint; a mechanical prior-extreme veto is not universal Brooks doctrine.

An unresolved/major barrier between entry and target prevents an unsupported beyond-barrier CANDIDATE. Use a nearer supported target only when it independently fits the intent/economics policy, otherwise WAIT/SKIP. Existing fixed targets are not changed by this check. During management, update observed rejection/acceptance separately from original committed objective and exit policy.
