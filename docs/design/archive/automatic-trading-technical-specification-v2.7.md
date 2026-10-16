# MDsquare context-aware intraday system

Version 2.7 - 14 October 2026. Requirements synthesis only; no project implementation. Authoritative consolidated specification. Current scope: NIFTY/BANKNIFTY underlying analysis, notifications and paper trade lifecycle. Trading edge unvalidated; application not implemented.

This document replaces the accumulated v1.x design amendments. The current skill is v0.11.0; its proposed decision contract remains schema v0.9.0. Earlier specifications, strategy discussions and templates are historical research unless consistent with this document. Prior specifications are preserved in [v2.0 archive](archive/automatic-trading-technical-specification-v2.0.md) and [v1.9 archive](archive/automatic-trading-technical-specification-v1.9.md).

## 1. Product and scope

Create a new repository, proposed name `MDsquare_Auto_Trading`, reusing audited concepts from `MDsquare_Quant_Investing`. One Brooks-inspired skill identifies context-supported opportunities, constructs a trade plan and reviews supplied open trades as data arrives. Code maintains prices, calculations, durable state, event triggers and validation. The objective is a reproducible decision process whose usefulness can be measured prospectively.

Current output is underlying price-action analysis and explicitly simulated trade management, not orders on the spot index. Options, contract selection, real broker orders and live capital activation are deferred. No option quotes are required. A future execution extension must separately specify the actual instrument and risk conversion.

Do not require daily/monthly trade quotas. Trade frequency, setup quality and profitability are measured outcomes, not promises. Source-book examples and all inspected dates are development material.

## 2. The trading policy

Keep higher-timeframe background, intraday regime, local leg and signal sequence separate. A daily bull market can contain an intraday bear trend. A bullish bar inside a range can be a range leg rather than a new bull trend.

| Current context | Working policy |
| --- | --- |
| Bull trend | Assess continuation longs at suitable corrective/test locations; initial opposing attempts are not automatically major reversals |
| Bear trend | Corresponding continuation-short policy |
| Tight trading range | No new candidates inside it, regardless of pattern name; observe credible escape |
| Wide established range | Assess longs near previously identified lower edge and shorts near upper edge, with inward evidence and target room; avoid middle |
| Credible transition | Reassess using structural challenge, opposing strength, acceptance/follow-through/test evidence |
| Unknown / ambiguous | WAIT or INSUFFICIENT_DATA, explaining the missing discriminator |

Brooks's market-inertia teaching motivates continuity as a working thesis. The 80% formulation is not a measured index win rate or sizing input. Inertia applies to ranges too: a strong internal leg or edge excursion does not establish a successful breakout. Conversely, once outside acceptance is credible, do not blindly fade the old boundary.

Every family follows context -> location -> sequence -> confirmation -> opposing evidence -> conditional plan. Breakouts can establish new context but are not exempt from that gate. Distinguish short directional flags from independent tight two-sided congestion; ambiguous classification means WAIT. Tight-range entry prohibition does not automatically close an already filled trade.

### Persistent swing thesis

Each update proposes a versioned swing context: initiating mechanism/anchors, direction, phase, defended structure, invalidation, strongest opposition, entry routes and causal projection. Code persists accepted revisions; prior summaries remain hypotheses. Five-minute entry signals may participate in longer intraday swings. Distinguish directional correction from independent two-sided congestion. A parent swing does not reset because a few candles overlap, nor persist after meaningful structural failure. Completed 15/60-minute evidence can clarify the parent structure without using developing bars as confirmed evidence. See [swing context](brooks-index-analysis/references/swing-context.md).

## 3. Setup controls and initial eligibility

| Category | Research-pilot defaults |
| --- | --- |
| Breakout | breakout_continuation_long/short, breakout_pullback_long/short |
| Bullish momentum | bull_first_pullback |
| Bearish momentum | bear_first_pullback |
| Bullish mild | bull_high2 |
| Bearish mild | bear_low2 |
| Sideways | range_failed_breakout_long, range_failed_breakout_short |
| Reversals | opening_reversal_bull/bear |

The skill includes contextual guidance for first/microchannel pullbacks, double-test flags, wedge pullbacks, range double tests, opening breakouts/reversals, major/wedge reversals and final flags. The twelve-ID profile is research coverage, not automatic enablement. Each route requires supplied switches and complete operational rules/policy. Other catalog IDs remain observations until separately defined/configured/evaluated. H2/L2 can occur in strong trends despite their mild-category home.

Category off overrides child on. Category on does not activate every child. Direction/mode/definition/context eligibility also apply. Disable actions invalidate affected untriggered plans through explicit revisions; existing positions retain management/protection. Do not relabel disabled ideas to bypass switches.

One episode can have multiple tags. Define identity from underlying, causal boundary/leg, direction and correction/thesis version; use a supplied durable ID. Preserve one primary plan per episode. Fixed primary-label precedence and simultaneous-index policy must be declared before scoring. No repeated entries, extended expiry or renamed duplicates without an explicit new-structure/re-entry rule.

## 4. One skill, one update, two outputs

Use [brooks-index-analysis](brooks-index-analysis/SKILL.md), version 0.11.0. It reviews supplied open trades first, then eligible new opportunities. References progressively cover regime, setup qualification, economics, management, context/handover, contrast examples and source study. Books are reference evidence, not operational instructions or full texts to include in each prompt.

Use the [decision contract](brooks-index-analysis/references/decision.md), schema 0.9.0. Proposed envelope:

- Context identity/hash, cutoff, configuration and processor generation.
- Open-trade inventory status: KNOWN or UNKNOWN. Unknown is not flat.
- `new_trade_assessments`: context, location, primary thesis, contradictory evidence, candidate/wait/skip/insufficient-data and optional complete plan.
- `open_trade_reviews`: one review per supplied open trade; unknown inventory uses null plus missing-state explanation.

New CANDIDATE requires an enabled supported setup, verified numeric trigger/stop/target geometry, prospective trigger and supplied validity policy. Qualitative scenarios or missing precision/policy use WAIT. Missing identity may permit research analysis but never a submittable application decision. Model output cannot establish fill/state changes.

The application validates schema, prices/bar IDs, cutoff availability, switches, trigger status, expiry, episode consumption, context freshness and processor assignment. One accepted decision per logical job; late/malformed responses remain logged and cannot arm plans. No validator has yet been implemented.

## 5. Trade plan and trader's equation

For each complete idea record setup/context thesis, signal evidence, entry trigger, structural invalidation and operational stop, initial objective, optional stretch projection, expiry and failure conditions. Choose the structural stop first; do not tighten it arbitrarily to manufacture reward/risk.

| Thesis | Initial target reference | Conditional extension |
| --- | --- | --- |
| Trend continuation | First opposition or justified leg-1=leg-2 under declared target mode | Nearer prior extremes can be checkpoints when passage is supported |
| Accepted breakout/test | First opposition or justified established range-height projection | Broken boundaries remain evidence checkpoints |
| Wide-range rotation | Defensible internal level / midpoint | Far-edge test only if subsequently supported under policy |
| Enabled emerging reversal | First opposing structure | Further leg/trend scenario only with sufficient strength |

Declare MEASURED_SWING, FIRST_OPPOSITION or RANGE_ROTATION mode before entry. Classify nearer levels as CHECKPOINT/MAJOR_OPPOSITION/UNRESOLVED with evidence. A supported measured swing can commit its projection as the initial target; a checkpoint is not an automatic exit. Serious/unresolved opposition can veto that plan. Filled targets/anchors do not extend after favorable candles.

Measured moves are scenarios, not mandatory exact distances or fixed durations. Record anchors and distinguish confirmed from provisional corrective endpoints. Evaluate room again at acceptance/trigger; late entry may destroy the original geometry. Do not move targets farther away to rescue the ratio.

For long E/S/T: risk R=E-S, reward W=T-E; short reverses the distances. Require positive distances. Brooks's equation compares p*W with (1-p)*R. With compatible friction C, the binary scenario is p*W-(1-p)*R-C; required break-even p=(R+C)/(R+W). Unknown friction gives gross threshold only, not zero assumed costs.

p concerns this target-before-loss/holding policy, not general directional confidence. Without compatible calibration it remains null; report required probability and evidence strength, with expectancy UNVERIFIED. A supported complete research plan need not invent p to become a candidate. Any statistical admission gate must be explicitly supplied. Partials/additions/early exits require episode payoff-distribution evaluation, not blind use of the binary formula.

## 6. Open-trade management

Supply authoritative episode/trade ID, original thesis and anchors, actual simulated entry events/size, average price, remaining size, original/current stop/targets, committed risk, exit policy, add-on plan, pending actions and state revision.

| Recommendation | Meaning |
| --- | --- |
| HOLD | Thesis intact; normal correction does not defeat it |
| TAKE_PROFIT | Committed objective reached under current policy |
| REDUCE | A declared partial/protection policy applies; size/fraction supplied |
| CLOSE | Stop/thesis invalidation or declared time/session exit applies |
| ADD_WATCH | Supported preplanned zone; missing authorization/confirmation/risk prevents addition |
| ADD_CANDIDATE | Finite enabled add plan and all current conditions/risk checks pass |
| REVIEW_REQUIRED | State/data/chronology prevents reliable judgment |

Simple baseline: structural stop and one primary objective. Trailing, partials and time/no-progress exits require explicit policies. Do not improvise new numerical thresholds. Stop tightening uses confirmed structure and policy; no widening. A range/first-opposition objective does not silently become a measured-swing target. A checkpoint touch does not close a measured-swing position unless supplied policy says so. Entry-plan expiry is distinct from position holding/exit time.

Commitments and protection require independent event logic, not the next five-minute AI response. If a stop/target event already led to an exit or an action is pending, do not duplicate it. Historical stop/target touches with unknown ordering are ambiguous. The skill recommends; confirmed application events update the journal.

## 7. Planned adverse additions

Include potential add zones in the trade plan; default WATCH_ONLY until a finite policy is supplied. This supersedes the original blanket exclusion of averaging down for underlying research. It does not authorize actual orders.

Before first entry specify source-based zone, confirmation, tranche sizes, maximum adds, unchanged common stop, add expiry, total committed episode/account risk and combined-position exit policy. Initial allocation reserves planned capacity. For every proposed add verify intact thesis, no stop breach, correct zone/confirmation, current data, valid count/expiry, no pending duplicate, total risk and remaining objective.

For linear declared paper units, total long stop risk is sum(q_i*(E_i-S)) plus compatible friction; short mirrors it. Monetary interpretation requires an actual defined instrument/point value, which is deferred. Improved average entry does not imply lower total loss. No martingale, stop widening or addition after invalidation. Missing sizes/budget/policy means observation only.

## 8. Data and causal context

Preferred source candidate: repaired Upstox integration. Use genuine 1m OHLC/ticks, not one LTP sample per minute. Verify interval-start/end semantics, timezone, source finality and historical/live consistency before trusting bars. Preserve source event time, receipt/recovery time and revisions.

Canonical aggregation groups by instrument and exchange-calendar session. Standard 5m examples are [09:15,09:20), [09:20,09:25) IST. Require five distinct final minutes; no cross-index mixing, fabricated forward fills, auction/post-close inclusion or silent duplicate repair. Missing data blocks affected eligibility until verified recovery; late recovery never becomes a fresh historical entry.

Runtime retention: rolling 30 calendar days intraday, at least 12 months daily, derived weekly/monthly. Research archive is longer and continuous across regimes. Retention differs from bounded model context: recent 5m bars, useful 15/60m structure, daily/weekly background and causal relevant levels, plus open trades/plans/config. Exact packet budget is benchmarked rather than sending all history each call.

Current session extrema include only observed prices. Developing larger bars are provisional; pivots publish after their actual confirmation. Prior summaries retain evidence/timestamp and are hypotheses. Spot volume/OI is unavailable for traded-volume analysis; no fabricated VWAP. Optional enrichment is separately sourced and evaluated.

## 9. Runtime, shared state and provider switching

Use a maintained collector/context service, analysis worker, application validator, paper trigger/management engine, durable journal and notification outbox. One skill serves both identification and management, but does not replace this runtime.

Central PostgreSQL stores canonical bars/current plans/trades/config/jobs; immutable object storage keeps raw/history/context/response bundles. Chat sessions and repository snapshots are caches. Both providers obtain the same versioned context through tested authenticated adapters. Any cloud environment must prove networking, secrets, tools, scheduling and persistence; portability is a contract, not assumed platform capability.

Every eligible closed 5m context is assessed. Two indices imply up to 150 separate assessments in a normal 75-boundary session, excluding retries. Joint assessments are a separately tested alternative. Record latency, missed triggers, tool/token/run costs and budget exhaustion. Stale results pause new risk; data capture and existing protection continue independently.

For midday switching, preflight the incoming provider, revoke old generation, build coherent handover snapshot, obtain acknowledgment/deltas, then activate new assignment. Reject late old responses and duplicate accepted jobs. Preserve pending/consumed episodes, stops/targets, expiry, risk and notification state. A provider outage leaves a visible gap, not retroactive trades or arbitrary fallback. No provider selection by hindsight returns.

## 10. Cloud-to-local synchronization

Keep schemas/code/config and appropriate manifests in the repo; runtime history and decisions persist centrally. Bootstrap portable environments from verified bundles/context service. Do not rely on end-of-day export or chat transcripts.

Explicit workspace sync downloads/imports deltas idempotently into the local database using event cursors, hashes, revisions and recovery checks. Git pull alone does not hydrate data. Include raw/canonical changes, decisions, trade events, management recommendations, simulated fills, routing and config changes. Interrupted sync resumes without duplicate trades or overwriting historical availability.

Verify data access/storage/transmission rights under provider terms before redistribution. Do not commit tokens or log authorization headers. Keep raw immutable lineage and source provenance.

## 11. Reuse from Quant Investing

Inspected source: `/Users/makkenasrinivas/PycharmProjects/MDsquare_Quant_Investing/`. Prior inspection was read-only static analysis, not running-system verification. The source did not report a Git repository. Preserve an owner-selected hashed snapshot and avoid importing modules with DB/auth side effects.

Reuse normalization, subscription lifecycle, catalog ideas, alert metadata and replay concepts through audited extraction. Rewrite the V3 protobuf adapter/finality/recovery, per-instrument aggregation and typed configuration. Remove TLS-disable paths, constructor table drops, secret/header logging and mutation retry assumptions. Do not reuse mocked order success/details as live state. Detailed path evidence is in [source reuse audit](project-synthesis/source-reuse-audit.md); future order components are outside current implementation scope.

## 12. Evidence and unbiased evaluation

Public audit: 60 files, 30 sessions per index across six selected month blocks; Jan 4, 2023 repeats complete sessions in both files and is quarantined. Twenty-nine paired sessions pass internal checks under an unverified minute-end hypothesis. All inspected dates are development-only. No source-price reconciliation, numeric setup performance or calibrated probability has been established.

Ten qualitative book cases are draft annotations from two charts, not independent holdout evidence. Contrast references help interpretation; they are not tests passed. Freeze definitions, model/skill/config and exit/add policies before scoring; record every attempted trial including discarded results.

Use contiguous chronological development/validation/untouched evaluation, partition by sessions, purge overlapping outcome horizons and retain failures/no-trade windows. Inspecting a holdout to fix the strategy consumes it. Public historical data may be known to a pretrained model; prospective frozen shadow/paper runs are the stronger check.

Compare AI with a simple fixed baseline under identical underlying event, risk, stop/target/add and friction assumptions. Distinguish context/sequence agreement, underlying episode outcome and operational reliability. Report eligible assessments, abstentions, opportunities, accepted/missed triggers, episode net results, drawdown, correlated exposure, management revisions, addition loss concentration and operating costs.

Hypothetical spot-index marks are simulation outcomes, not executable broker P&L. Specify entry/stop/target event marking and slippage/ambiguity. Measure uncertainty by session/block preserving repeated-trade and paired-index dependence. Do not count tranches or recurring labels as independent trades. Numerical success thresholds and forward window must be registered before outcomes are opened; elapsed months alone do not establish success.

## 13. Implementation order

| Stage | Deliverable | Acceptance evidence |
| --- | --- | --- |
| 1. Data foundation | Verified two-index adapter, calendar, canonical/revision storage | Timestamp/source reconciliation, duplicate/gap/session fixtures, continuity/restart |
| 2. Research contracts | Context/episode schema, unified output validator, numerical labels, baseline | Causal cutoff discipline, full plan geometry, ambiguity and switch enforcement |
| 3. Shadow skill | Every eligible close plus every supplied open-trade review, notifications | Measured latency/cost, all failures retained, no invented state/authority |
| 4. Underlying paper lifecycle | Trigger marking, fixed stops/targets, durable management and bounded-add policy | No retroactive fills/duplicate actions; event chronology/risk correctly tracked |
| 5. Frozen evaluation | Chronological and prospective report | Predeclared evidence/uncertainty/reliability criteria, including failure or inconclusive outcome |
| Later, separate | Actual instrument/option execution | New instrument/risk/fill specification and explicit live authorization |

Stop/target and stale-result behavior, provider handover, pending actions, data outages, DB restart, sync recovery, expired entries and bounded adds are engineering tests. They do not prove trading edge.

## 14. Remaining choices

Before code setup: repo location/hosting, first runtime, notification channel and data access. Before armable paper strategy: operational trend/range/sequence definitions, trigger buffer/late-entry tolerance, plan expiry/re-entry, target/exit policy, paper units/friction, risk cap, simultaneous-index tie-break and add policy. Before evaluation: baseline, primary endpoint, uncertainty method, test/forward dates and acceptance thresholds.

These unknowns do not block ingestion or qualitative chart review. They block claims of calibrated profitability and applicable paper risk actions. Do not invent answers merely to make the design look complete.

## 15. Current deliverables and precedence

- This specification: authoritative system design and scope.
- [Unified skill](brooks-index-analysis/SKILL.md) and [contract](brooks-index-analysis/references/decision.md): operative draft reasoning/output instructions.
- [Experiment charter](project-synthesis/experiment-charter.template.json) and [strategy cards](project-synthesis/strategy-cards.template.json): incomplete registration templates, not executable configuration.
- [Expanded audit](project-synthesis/expanded-data-audit.json), manifests and inspected-date registry: evidence/provenance.
- Earlier doctrine/readiness notes: supporting historical synthesis only where consistent; option sections are deferred.

The next implementation milestone is reliable causal data and auditable unified assessments. Pattern coverage, profitable-looking selected charts, an elegant skill and a few months of paper activity do not independently establish an edge.

### v0.4 evaluation separation

Keep the completed cloud v0.3 replay/policy unchanged. v0.4 is a new development revision. Evaluate identification (eligible causal entry routes and context), target choice (same frozen entries/stops under first-opposition versus measured-swing policy), and execution (actual latency/expiry/fill path) separately. Freeze opportunity labels before viewing outcomes, retain missed/failed/abstained episodes, and use untouched sessions for evidence. October 9 is diagnosis material, not proof the revision works. Runtime should cache invariant context, update only causal deltas and maintain pending/protective events independently; benchmark actual response latency rather than treating an invented one-minute delay as measured performance.

## Brooks principle coverage (v2.2)

The authoritative skill now loads a shared [operating doctrine](brooks-index-analysis/references/brooks-principles.md) before setup interpretation. It covers market cycle/inertia, pressure/always-in, causal levels/tests, pattern quality, breakout failures, minor/major reversals, entry economics, measured objectives, protection, holding/scaling and discipline. [Coverage register](brooks-index-analysis/references/principle-coverage.md) maps all 78 Reversals chapter-25 guidelines and records incomplete three-book study and deliberate exclusions. Volume/OI/options remain excluded by user scope. The twelve research IDs and disabled-by-default application status remain unchanged.

Contract v0.5 adds qualitative market_read and controlling principle_conflicts; these are observations, not probability estimates or a scoring engine. Application adapters must explicitly adopt the revised contract. Existing frozen replay results, policies and cloud tasks are not retroactively revised. New evaluation must freeze the new skill plus operational rules and use unseen sessions. No runtime or execution validator is supplied by this document.

## Three-book synthesis (v2.3)

Trends and Trading Ranges now supply explicit source-backed [decision guidance](brooks-index-analysis/references/trends-and-ranges.md), with all 26/32 chapter openings and deeper selected passages recorded in [coverage](brooks-index-analysis/references/three-book-coverage.md). Reversals chapter-25 guidelines remain one shared foundation. Source coverage is not full chapter/chart review or strategy validation.

Interpretation now distinguishes spike versus mature channel, first-pullback types, actual interrupted H/L attempts, overlapping breakout tests, evolving session profiles, and phase-appropriate trailing/exit evidence. Target guidance separates leg equality, spike extension, range height and measuring-gap projection. Application must supply permitted methods, anchor conventions and causal confirmation rules before use. Twelve research setup IDs, switches and WATCH_ONLY addition defaults retain their existing meaning. Source study does not add execution styles or silently change old trials.

## 16. Structure continuity, opposition and plan admission (v2.4)

This section establishes v2.4 requirements, refined by the v2.5 adjudication section below. The current skill is v0.10.0 and decision schema v0.9.0; subsequent sections refine these requirements. Earlier v0.4/v0.5/v0.6 sections describe provenance, not current interface versions. No production runtime or strategy validation is delivered by this specification.

### Persistent swing map

Store per instrument the accepted parent swing, active leg, full correction and relevant nested pauses. Each node references its parent, originating bars/source revisions, available/confirmation timestamps, phase, defended structure and next discriminator. Preserve complete correction segments and attempted resumptions. Model responses propose a base-revision delta with evidence; application validation assigns identity and commits the revision atomically with the accepted decision. Late breakout confirmation cannot discard earlier visible correction bars or initialize the peak from the confirmation bar blindly. Source corrections create later revisions, never rewrite prior knowledge.

The accepted map remains a hypothesis about the market, separate from authoritative trade/plan inventory. New classification cannot reset exposure. A local bearish/bullish leg can coexist with a parent range; regime, swing and signal remain distinct layers. Unknown ancestry blocks an affected new plan rather than selecting a nearby convenient stop.

### Opposition service and assessment

Build a causal level ledger from prior session/week, parent range, completed opening range, full swing/correction, local rejections and permitted projections. Code calculates and retrieves facts; the skill classifies relevant opposition using cited rejection/acceptance evidence and a passage thesis. Scan the actual entry-to-target path through daily AND intraday structure. Do not treat only previous-day extremes as barriers or turn every prior extreme into a universal veto. Relevant unresolved/major opposition prevents an unsupported beyond-barrier plan; a nearer objective needs independent justification and valid economics.

Persist level origin, scope, availability, source revision, tests/rejections, accepted crossings, classification and discriminator. Updates affect the thesis review, not a filled position's immutable original stop/target. Retain unresolved barriers across provider handover.

### Plan admission

Before CANDIDATE require evidence-backed consistency checks: context/location; complete correction ancestry; stop-to-thesis match; target-to-thesis match; opposition coverage; intent/economics; timing/identity; inventory/policy. Semantic ambiguity means WAIT, known disqualification SKIP, and missing required evidence INSUFFICIENT_DATA. Model PASS does not prove economic expectancy. Application recomputes numeric/source/identity/assignment/expiry/deduplication checks before arming. All failed or stale proposals remain logged.

Initial entry stops depend on family: entire corrective swing for qualified pullback entry, initiating base/defended structure for breakout, failed excursion for range rotation. Existing-position trailing is a separate policy. No arbitrary stop-distance floor, universally mandatory 2R, target stretching, averaging or extra indicators is activated by this revision. Cost/risk/ratio conventions still need registration. Normal small opposite movement is not automatically thesis invalidation; original independent protection and declared exit policy remain active.

### Storage additions and handover

| Logical record | Required responsibility |
| --- | --- |
| swing_map_revisions / swing_nodes | Accepted per-instrument revisions, parent/correction ancestry, causal anchors and revision history |
| level_evidence / opposition_assessments | Causal level facts separated from versioned semantic judgments and coverage limitations |
| plan_consistency_assessments | Check results/evidence linked to immutable decision, skill/config/context versions |
| source_interval_quality / reconciliation_runs | Suspect intervals, independent reference, discrepancies and explicit resolution |
| interpretation_reviews / execution_events | Independent context scoring versus actual timings/fill disposition |

Names are logical storage requirements, not existing tables. Use the existing event journal/transaction boundary; avoid a second exposure authority. Mid-session processor handover includes map/opposition/quality revisions, unresolved ancestry and pending amendments alongside accepted episodes, configuration, assignment generation and event watermark. Local synchronization imports immutable records and accepted revision events idempotently, verifies hashes/manifests and preserves historical availability. Repo snapshots are transport/cache; the durable journal/database remains authoritative.

### Source repair and frozen evaluation

The existing community source shows identical flat bars over 15:15–15:25 on all ten sampled dates. That is an unresolved provenance issue. Preserve raw data; record suspect intervals; reconcile exact source semantics/values against authenticated broker/primary history and log outcomes before calling them verified. Credentials/source access and a collector implementation are still required. Do not manufacture OHLC or reliable late-session fills. This update has not repaired or downloaded replacement prices.

Score three linked streams independently: cutoff-based interpretation, execution timing/events, and fixed-policy episode outcomes. Instrument actual request/response/validation/arm latency before selecting the execution replay delay. An earlier one-minute hypothesis is not a measured cloud latency. No retroactive fills or outcome-based deletion of decisions.

All ten inspected September/October dates and the previous replay/audit examples remain development. Register skill/model/config hashes, source manifests, anchor/stop/target/expiry conventions, baselines, latency/cost scenarios and reporting thresholds before designating uninspected chronological blocks. Evaluation status stays PLANNED until those data/inspection/registration conditions are fulfilled. No profitable edge or promotion follows from this documentation.

### Required acceptance cases before implementation release

1. Late acceptance retains the already-visible full correction, including a deeper earlier extreme; a nested pause does not become the parent stop.
2. Two signals in a genuine tight range do not create trend permission; a supported compact flag is not declared a range solely from overlap.
3. A local trend leg beneath/above the parent range boundary requires explicit parent-opposition assessment.
4. A strong rejected intraday extreme between entry and target cannot disappear because the target ratio looks attractive.
5. Initial correction protection is distinct from permission to trail a filled trade; no stop widening or invented fills.
6. Stale map revision or old provider generation cannot overwrite accepted state; unresolved evidence survives handover and local sync.
7. Corrected/padded prices remain separate revisions; historical decisions do not gain later confirmation or availability.
8. A missed pre-arming trigger is an execution miss; a later profitable chart cannot turn it into a fill or overwrite interpretation.

These cases define verification work. Current documentation/link checks do not establish that an application, model or discretionary strategy passes them.

## 17. Decision adjudication and requirements closure (v2.5)

Current work is requirements synthesis, not application implementation. No new repository, collector, validator, database, broker interface or replay strategy is requested by this revision. The [context-adjudication guidance](brooks-index-analysis/references/context-adjudication.md) specifies the controlling distinctions without introducing numerical trading thresholds.

### Evidence and interpretation boundaries

Keep observed market facts, interpreted structure and registered policy separate. Preserve four layers: higher-timeframe background, provisional intraday regime, parent swing/range rotation and local signal. Day type cannot use a completed-day label at an earlier cutoff. A daily bias neither automatically authorizes nor vetoes a local setup; parent structure/opposition decides its eligibility.

The full correction begins with the earliest relevant opposing activity after the interpreted initiating leg, including inside bars and interrupted resumptions. A trigger crossing alone does not prove completion. Ending it and creating a distinct next correction requires the registered progress/confirmation evidence. Late acceptance cannot reset an already-visible peak/correction to its confirmation candle. When defensible alternatives change the stop/count, retain alternatives and WAIT; missing relevant observations instead produce INSUFFICIENT_DATA.

### Passage and geometry

Classify an obstacle using scope, origin, rejection/acceptance evidence and parent context. CHECKPOINT needs a supported passage thesis and failure discriminator; MAJOR_OPPOSITION defeats the proposed beyond-level thesis; UNRESOLVED needs confirmation or a separately justified inward plan. A plausible passage scenario is not the same as observed outside acceptance. Initiating breakouts use their own declared confirmation policy; they are not unconditionally forced to wait for a retest or every later obstacle to break.

Match setup, intent, full structure protection and objective before calculating economics. New pullbacks can protect their complete correction; initiating breakouts use their relevant base, tested breakouts their full test/parent defense, and range failures their excursion. A favorable ratio cannot substitute for this match. No universal minimum point stop, mandatory 2R, bar-size rejection threshold or invented calibrated probability is required. Parameter registration still controls any numeric admission rule.

### Management decision precedence

Authoritative events/pending actions precede interpretation. Known protective/target/session events follow the supplied event/exit policy; missing or ambiguous state requires review, never invented fills. Without such an event, intact defense and ordinary corrective movement support HOLD. Sustained opposing acceptance or evidenced defeat of the objective/structural premise may justify a policy-supported CLOSE before the stop. A forming range triggers review, not an automatic exit or an improvised timeout. Original geometry, current hypothesis and proposed action remain distinct. No stop widening, automatic reversal, fractions or scaling policy is added.

### Requirements that remain open

[Policy-registration requirements](project-synthesis/policy-registration-requirements.md) lists conventions needed before an armable paper strategy: structure prominence/completion, family-specific breakout acceptance, signal/counting, buffers, anchor conventions, risk/economics, expiry/reentry, management, additions, data admission and frozen evaluation. Older research defaults are not current requirements unless explicitly adopted. These choices are not silently set from previously inspected outcomes.

[Acceptance cases](project-synthesis/requirements-acceptance-cases.md) supplies 18 original cutoff scenarios covering ancestry, context, opposition, geometry, management, handover, later data revisions and latency misses. Their independent evaluation status is NOT_RUN. Record agreement, disagreement and uncertainty separately from outcomes; consulting future P&L is not a valid way to settle interpretive disagreement.

The source-quality reconciliation gap and untouched-data/model/latency registration remain unresolved. Requirements are more precise; no runtime, primary-data repair, independent skill evaluation or profitability validation has been completed by this revision.

## 18. Recursive three-book synthesis and compatibility (v2.6)

This is requirements/skill synthesis only. No application repository, classifier, broker integration, executable validator or new market replay was created. [Iterative review](project-synthesis/recursive-synthesis-review.md) records five passes: source coverage, interpretation conflicts, geometry/policy feasibility, adversarial cases and dependency/readiness closure.

### Coverage and claim boundaries

[Three-book traceability](project-synthesis/three-book-requirements-traceability.md) maps all 83 chapter topics to 30 requirement families. Mapping from contents and selected passages does not establish complete reading, every-chart interpretation or applicability/profitability on these indices. The prior 78 numbered Reversals guideline summaries remain qualitative coverage, not 78 enabled strategies. This pass read/revisited 56 selected Trends/Trading Ranges text pages; exact pages and incomplete Reversals access are recorded in the skill coverage register. Additional iCloud Reversals extraction did not return bytes and is not counted as reviewed.

### Current context and signal requirements

Skill v0.10.0 adds [market-cycle and pattern hierarchy](brooks-index-analysis/references/market-cycle-and-patterns.md). Schema v0.9.0 adds `market_cycle_assessment` and `signal_assessment` to the existing envelope. Phase hypotheses distinguish initiating strength, tight directional channels, broad channels, ranges and transitions, with parent scope and unresolved breakout alternatives. They complement rather than replace coarse regime/swing state. Day type remains provisional; a nested local range does not erase the parent initiative.

Signal qualification depends on context and registered mode. A conservative same-direction strong-bar filter is a project variant, not a universal Brooks requirement; a supported strong trend may offer weak-looking continuation setups. A large opposing bar may be correction or exhaustion, while a strong reversal bar cannot replace missing reversal context. Prospective setup bars, trigger crossings, actual/hypothetical fills, entry bars and later follow-through have different availability. Never require future follow-through as evidence already known at initial decision.

### Hierarchy, maturation and failure sequences

H1/H2/L1/L2 needs parent corrective structure and interruption/renewal evidence. Multiple crossings inside an uninterrupted opposing channel can be one complex first leg. First-pullback types differ by bar/minor-line/MA/MA-gap/major-structure scope and need not appear in a fixed order. Record observations without creating new episode permission or enabling a disabled family.

Microchannels, double tests, wedges, triangles and inside/outside patterns have different meanings by parent context. Broad-channel tests can return beyond the breakout price without defeating full parent defense. Line breaks and climaxes warn of change but do not prove a confirmed major reversal; early reversal participation and eventual major-trend classification are distinct. Potential final flags remain hypotheses until causal failure evidence appears. The source's advanced countertrend, limit, close-entry, scalping and scaling methods remain knowledge coverage, not execution enablement.

### Projection, opposition and feasibility

A conditional objective must use the registered causal anchor convention and full opposition assessment. Confluence is not independent probability calibration. Initial risk is available before entry; later adverse excursion/clarified actual risk cannot be imported backward. A full-base stop plus one-range-height target generally cannot satisfy 2R at an outside breakout entry. Detect that incompatible policy combination before outcome testing rather than manufacture a narrow stop or farther target. There is no universally mandatory initial ratio or stop point distance in this design.

[Compatibility audit](project-synthesis/brooks-compatibility-audit.md) documents 22 tensions and their resolutions. Original chapter/source teaching, project adaptation, registered numerical convention and measured evidence must remain distinguishable.

### Session and participation requirements

Retain opening-continuation/reversal alternatives, parent daily/weekly location, morning initiative through midday balance, and late-resumption possibilities without forecasting the final session. NSE session/calendar/tick/instrument definitions require explicit adaptation; US source clock-time and frequency/probability examples are not copied as index rules. Optional causal MA context needs a registered definition and warm-up; it is not a new mandatory indicator. Volume/OI/options remain outside user scope.

Evaluate enabled initiating, first-pullback, second-entry and test routes under their distinct policies. Record eligibility versus policy exclusion versus latency/expiry/consumption. More routes or looser filters do not automatically supply sufficient profitable trades, and no quota applies. Twelve research IDs remain the profile; newly recognized source families stay observational/deferred until separately defined and evaluated.

### Closure and remaining work

[34 acceptance cases](project-synthesis/requirements-acceptance-cases.md) cover the distinctions above; independent evaluation status is NOT_RUN. [Policy registration](project-synthesis/policy-registration-requirements.md) remains required for operational definitions and owner risk/economic thresholds. Untouched chronology, model/version registration, actual provider latency and primary-source data reconciliation remain open. The previous 15:15–15:25 flat intervals are not repaired by this review.

Next requirements evidence priorities are independent cutoff disagreement review of ancestry/opposition, a small explicit operational policy, deeper source/chart study where incomplete, and primary-source reconciliation. Implementation and performance testing remain separate authorized future stages. No claim of “greatest intraday system,” learned model weights, complete three-book mastery or proven monthly profitability follows from this package.

## 19. Simple operating baseline and complexity boundary (v2.7)

This section sets the default operating scope; earlier detailed chapters remain reference requirements rather than mandates for separate services, exhaustive graphs or long per-candle reports. Requirements synthesis continues; no project implementation is requested.

Use [the simple operating playbook](brooks-index-analysis/references/simple-operating-playbook.md): supplied position review, context, location, enabled setup, one structural stop/initial objective and a concise decision. Preserve the existing category/individual switches and twelve-ID research coverage. Group opportunities for presentation as trend pullback, meaningful breakout/test, wide-range edge failure and qualified opening reversal; these are not new independent engines.

Maintain a compact per-index snapshot: current parent context, active swing, complete current correction/extreme, relevant obstacle(s), authoritative pending/open/consumed state and supplied original geometry. Retain revision/provenance history in the journal; reference older evidence instead of duplicating it. A generalized graph of all past swings, perpetual alternative-thesis ensemble and a separate service for each logical record are not minimum requirements. Detailed map nodes are elaborations only where needed to resolve ambiguity or satisfy integration review. Late confirmation/nested pauses still cannot erase ancestry.

Basic management is fixed original protection/objective, HOLD through normal corrections, and evidenced exit or declared session/protective events. No automatic scaling, partials, breakeven, trailing, reverse-on-signal, adaptive targets, indicator voting or provider consensus is added. Supported add zones remain WATCH_ONLY without registered bounded policy. Optional policies are not silently removed, but they are not prerequisites for the simple baseline.

For each five-minute update, print only context/action, relevant setup/location, eligible geometry and controlling reason/discriminator. Structured evidence/identity is stored separately for audit; do not expose nested schema/check trees in the user flow. Load additional source/reference guidance for a specific unresolved question, not every chapter at every candle. Old broad study/evaluation assets are not recurring model input.

Future implementation needs a data/context path, one analysis worker using the skill, durable journal/validation, independent paper protective-event handling and notification delivery. These are logical responsibilities that can be modules in one service with one authoritative store; this document does not require microservices or multiple databases. Provider switching uses the same snapshot and authoritative journal; no second account/state authority is created.

Simplicity retains the essentials: causal genuine data, full relevant structure, obstacle/geometry consistency, authoritative inventory, no duplicate/missed historical fills, and separate interpretation/execution/outcome evaluation. It reduces structural machinery and output burden; it does not remove data reconciliation, required numeric policy or independent evidence. The 34 review scenarios and deeper books remain development references, not a 34-item admission checklist.
