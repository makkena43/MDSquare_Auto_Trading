# MDsquare context-aware intraday system

Version 2.2 - 13 October 2026. Authoritative consolidated specification. Current scope: NIFTY/BANKNIFTY underlying analysis, notifications and paper trade lifecycle. Trading edge unvalidated; application not implemented.

This document replaces the accumulated v1.x design amendments. The current skill and its decision contract are v0.5.0. Earlier specifications, strategy discussions and templates are historical research unless consistent with this document. Prior specifications are preserved in [v2.0 archive](archive/automatic-trading-technical-specification-v2.0.md) and [v1.9 archive](archive/automatic-trading-technical-specification-v1.9.md).

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

Use [brooks-index-analysis](brooks-index-analysis/SKILL.md), version 0.4.0. It reviews supplied open trades first, then eligible new opportunities. References progressively cover regime, setup qualification, economics, management, context/handover, contrast examples and source study. Books are reference evidence, not operational instructions or full texts to include in each prompt.

Use the [decision contract](brooks-index-analysis/references/decision.md), schema 0.4.0. Proposed envelope:

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
