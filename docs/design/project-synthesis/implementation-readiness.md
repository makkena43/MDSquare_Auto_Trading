> **Precedence:** The [v2.3 canonical specification](../automatic-trading-technical-specification.md) and [unified skill](../brooks-index-analysis/SKILL.md) govern the current design. This earlier synthesis is supporting background; options and real execution are deferred.

# Project synthesis and implementation readiness

Version 0.1.0 - 11 October 2026. Complements technical specification v1.6; use these evaluation requirements where earlier draft wording is less specific. This is design and descriptive data research. No fitted strategy, performance backtest, trading application, broker access or cloud deployment has been created.

## Recommended scope

Build a portable, auditable research and paper-trading system for NIFTY and BANKNIFTY. A versioned Brooks-inspired skill interprets each eligible closed five-minute context. Code handles normalization, features, validation, triggers, risk and execution. AI cannot authorize missing limits, invent quotes, change protective orders or force a daily trade quota.

Keep six pilot IDs: H2 long, L2 short, breakout-pullback long/short and range failed-breakout long/short. Seven category switches remain supported. Momentum-specific and major-reversal families remain observational until separately defined and evaluated. Pilot-enabled means eligible for research, not proven profitable or live-enabled. Long calls/puts are still a proposed first execution scope requiring owner confirmation.

## Expanded evidence

Before fetching prices, recorded five target blocks: January 2019, March 2020, February 2021, June 2022 and January 2023. Selected the first five published session directories in calendar order in each, both indices. Added the five previously inspected February 2023 sessions. All downloads succeeded.

This selection is transparent but purposive, not random or representative: blocks were chosen with knowledge of broad historical conditions, and first-week sampling can overweight month-opening/events. The next research archive must contain contiguous months, ordinary sessions and failures. All dates inspected here are development material, never final holdout.

Source: [community archive](https://github.com/aeron7/nifty-banknifty-intraday-data), commit `906fc2378b82e50de78f62844a3ecb3f9306a85d`. Selection records, URLs, hashes and audit results accompany this document. Source lineage, timezone and interval-label convention remain unverified. Raw files are retained under `work/research-synthesis/raw/` and earlier `work/public-index-data/`.

| Check | Finding |
| --- | --- |
| Coverage downloaded | 30 sessions per index, six blocks |
| Files / raw rows | 60 / 23,437 |
| Duplicate defect | Jan 4, 2023 repeats all 378 rows exactly in each index file; 375 regular duplicate labels per file |
| Metrics eligibility | 29 paired sessions; duplicate files quarantined, not silently repaired |
| OHLC envelope/finite/positive checks | No failures |
| Expected regular labels | No missing labels under 09:16–15:30 minute-end hypothesis |
| Extra rows | Pre-open and post-close labels, some as late as 17:32 |
| Volume/OI | All zero; treated as unavailable for index analysis |
| Provisional 5m bars | 4,350 across 58 accepted files under unverified timestamp convention |
| Within-session 5m return correlation | Median 0.897; range 0.806–0.964 across 29 paired sessions |

Internal consistency is not exchange-price accuracy. No independent price reconciliation was performed. Observed label coverage does not prove exchange-calendar completeness or real-time availability. Correlation is descriptive, not a fixed future exposure estimate.

### Descriptive volatility

Median session high-minus-low range divided by opening price. These full-session summaries are retrospective and forbidden in earlier candle context.

| Block | Accepted sessions per index | NIFTY median range | BANKNIFTY median range |
| --- | --- | --- | --- |
| Jan 2019 | 5 | 1.070% | 1.172% |
| Mar 2020, first five sessions | 5 | 1.898% | 3.198% |
| Feb 2021, first five sessions | 5 | 1.813% | 3.179% |
| Jun 2022 | 5 | 1.233% | 1.001% |
| Jan 2023 | 4 | 0.984% | 1.438% |
| Feb 2023, previously reviewed | 5 | 1.184% | 2.264% |

BANKNIFTY is not uniformly more volatile in these small blocks. Shared exposure limits and evaluated volatility scaling are preferable to treating indices independently or applying arbitrary fixed point thresholds. This does not establish profitable thresholds.

The audit also records close-path efficiency: absolute change between first/last 5m closes divided by the sum of absolute successive close changes. It is descriptive; low full-day efficiency can coexist with useful local trends. No thresholds were fitted, setups counted, trades simulated or profits calculated.

## Design decisions sufficiently specified

| Decision | Consequence |
| --- | --- |
| Separate spot ideas and option execution | Different contracts/readiness/reports; index points do not establish option P&L |
| Shared account risk authority | Both indices reserve combined exposure atomically |
| Collector/exits independent of AI | Model outages block new decisions while existing protection continues |
| Durable central state | PostgreSQL and object archive are authoritative; chat/workspace are caches |
| Provider-neutral context/decision contract | Mid-session switching uses generation fencing; stale old results rejected |
| Raw plus canonical revision storage | Preserve native labels, mapping, availability and finality |
| Compact skill and bounded context | Do not send archives/books with each candle |
| Explicit local synchronization | Verified incremental DB import; Git alone cannot hydrate DB |
| Observation versus execution switches | A visible pattern need not arm an order |
| Frozen evaluation versions | Model/skill/config changes require new attribution and evidence |

Upstox is the candidate for authenticated backfill/live integration because the existing project uses it. [Historical V3](https://upstox.com/developer/api-documentation/v3/get-historical-candle-data/) documents minute history from January 2022; older public files cannot validate pre-2022 Upstox behavior. Existing components require the remediation in the main specification.

## Required data acceptance

1. Independently verify minute-start versus minute-end semantics and timezone. Preserve native labels; quarantine unresolved sources. Standard five-minute intervals remain [09:15,09:20), etc., based on the exchange session.
2. Log deduplication transforms. Identical repeats may be collapsed through a recorded rule; conflicting duplicates cannot use arbitrary last-row-wins. Never mix instruments or forward-fill fake OHLC.
3. Use maintained calendars and explicit auction/post-close handling. Retain official daily close separately from the last intraday value.
4. Preserve availability and revisions. A later recovery or correction cannot become knowledge in an earlier decision. Archives lacking reception metadata get estimated-availability flags and cannot prove live-equivalent finality.
5. Keep rolling 30 calendar days intraday for runtime, at least 12 months daily context, and a longer continuous research archive. These selected sessions are an ingestion sample, not the performance archive.
6. Daily/weekly facts, EMA/ATR, pivots and summaries must be causal. Current session high/low uses only observed bars; final-day extremes and not-yet-confirmed pivots are forbidden.
7. Record source/hash/transform/missingness/access rights in manifests. Keep secrets out of repo/data bundles and verify permitted cloud storage/transmission before distributing data.

## Four distinct evaluation questions

1. Can the AI interpret setups consistently from available evidence?
2. Do those underlying plans show useful forward behavior?
3. Are the actual selected option trades profitable after spreads, fills, constraints and costs?
4. Does the running system reproduce that behavior at real latency and failure rates?

Explanation quality and classification agreement do not answer profitability. The ten book cases are single-annotator qualitative development examples; they do not yet cover all six pilot IDs numerically. Independently reviewed index cases must include failed patterns and no-trade windows.

## Preventing backtest overfitting

### Register the experiment

Freeze skill/setup/config hashes, code/context version, model/provider/settings, source manifests, contract/exit/risk policies, costs, latency, benchmarks, test periods and acceptance criteria before scoring. Log every attempted configuration, including discarded failures. Prompt edits, category toggles, provider choices, targets and exits all count as trials.

Selecting a winner among many trials inflates apparent performance. [Backtest-overfitting research](https://escholarship.org/uc/item/4w1110bb) and the [Deflated Sharpe Ratio paper](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf) address that selection problem. Supporting diagnostics cannot replace causal data or prospective evidence. None has been computed here.

### Partition chronologically

- Keep all dates inspected here in development. Acquire continuous history, record inspected dates, then designate later disjoint validation/test blocks before opening their outcomes.
- Tune definitions on development and select among logged candidates on validation. Walk-forward adaptation, if used, follows a predeclared schedule using only preceding information. Report every fold.
- Split by entire sessions/contiguous blocks, not random overlapping candles. Purge overlap in label/trade horizons at boundaries. Legitimately preceding warm-up context is allowed; future observations are not.
- Evaluate final holdout once for a frozen candidate. Looking at it to fix the strategy consumes it. Further claims require fresh untouched data or prospective evidence; no repeated peeking and stopping when profitable.
- Public historical examples may be known through model pretraining. Replay is unseen relative to our tuning, not proof of model ignorance. Restrict tools to cutoff context, hide future/source-chart information and disclose memorization risk. Prospective runs are the stronger check.
- Plan a frozen forward paper window. Roughly 60 trading sessions is a suggested planning floor, not proof or an automatic promotion rule. Extend when independent episodes/regimes are insufficient. Do not manufacture trade volume.

### Replay the production contracts

Use the same context, validator, expiry, triggers, risk and contract selector in replay/live. Inject latency measured during shadow runs. A plan can arm only after decision receipt/acceptance. Earlier trigger crossings are missed opportunities, never retroactive fills.

OHLC can leave entry/stop/target ordering unknown, even at 1m. Flag ambiguous episodes and report pessimistic/optimistic bounds rather than assume favorable ordering. Credible option fills need executable bid/ask and liquidity; neither candle touches nor historical last prices guarantee fills or queue position.

Retain model refusals, malformed JSON, outages, stale context, retries and budget exhaustion. No repeated inference until a losing decision becomes profitable. Persist original request/response and disposition. Later recomputation never replaces an accepted decision's reported result.

### Compare fairly

Compare the frozen AI policy with a simple deterministic pilot-family baseline and no-trade benchmark under identical data, costs, risk, selection and exits. Other directional baselines must be predeclared. Do not optimize alternatives on final holdout.

Evaluate one provider first. Add switching/fallback later, without hindsight selection of which provider was right per candle. Upgrades create new versions. Measure stochastic sensitivity on predefined development repetitions; never report the best repetition as the strategy.

### Report uncertainty and failures

Report all eligible assessments, abstentions, candidates, expiry, accepted-time misses, fills, operational failures, turnover, exposure, net expectancy, daily returns, drawdown/tail loss, spread/slippage/fees and AI/runtime costs. Show both pooled and setup/index/regime/time breakdowns with uncertainty.

Estimate uncertainty by sessions/blocks preserving clustered trades and paired-index dependence. Raw trade counts are not independent observations. Report best-day/block concentration, removal sensitivity and cost/latency stress under predeclared rules. Never delete unfavorable events post hoc.

Select economic and risk thresholds before final evaluation. Proposed research criterion: positive net expectancy with an uncertainty interval excluding zero, acceptable predeclared drawdown, and cost/latency robustness. This is a proposed standard, not a guarantee or achieved result. Sparse subgroups remain inconclusive. Capital/drawdown limits require owner choice.

## Details still to freeze

| Choice | Why | Interim stance |
| --- | --- | --- |
| Signal qualification/H2-L2 counting | Nested legs invite relabeling | Explicit evidence/count ambiguity; wait when unresolved |
| Opening range/tolerance/volatility scaling | Many knobs invite overfitting | Small documented hypothesis set, no indiscriminate grid search |
| Trigger buffer/expiry/re-entry | Changes trade frequency and fills | Freeze before scoring; draft one-interval expiry is a hypothesis |
| Targets/exits | Correct direction can still lose | One explicit baseline; alternatives count as trials |
| Option selection | Expiry/delta/spread affect outcomes | Point-in-time metadata/quotes and owner-approved policy |
| Correlated risk | Both indices share exposure | Fixed account policy, never AI-selected limits |
| Provider/budget | Version and latency affect decisions | One tested processor first; no return-based switching |
| Promotion criteria | Moving goals manufacture success | Predeclare economics, uncertainty and reliability gates |

## Implementation sequence

| Stage | Deliverable | Gate |
| --- | --- | --- |
| A. Data feasibility | Broker reconciliation, timestamp/calendar contract, fixtures | Proven raw-to-canonical mapping; extras/duplicates/gaps handled |
| B. Research harness | Event-time replay, snapshots, cutoff cases, trial ledger | No future/availability violations; failures retained |
| C. Live shadow | Collector plus non-actionable AI observations | Actual cadence/persistence/recovery/latency/cost measured |
| D. Paper pipeline | Real option metadata/quotes, triggers, simulated fills | Fixed risk/exit policy; post-acceptance fills; uncertainty visible |
| E. Frozen evaluation | Chronological and prospective reports | Predeclared gates met or explicitly inconclusive/failed |
| F. Limited live, later | Approved bounded execution | Explicit activation and broker/reconciliation/kill-switch drills |

Stages A–C are useful even if profitability remains uncertain. Repo location and first runtime need selection before coding; missing economic limits need not block collection, but block paper performance claims/live activation as applicable. Do not prioritize order placement ahead of data/replay.

Operational verification covers wrong timestamps/instruments, duplicate/conflicting updates, late finality, special sessions, token expiry, model timeout, malformed responses, provider handover, trigger before arming, stale option quotes, order timeout after acceptance, partial fills/cancel races, DB restart, sync interruption and budget exhaustion. Entries fail closed while protection/reconciliation retains independent authority. Engineering correctness and market profitability are separate gates.

## Readiness conclusion

The design is concrete enough to begin the data foundation once repo/runtime choices are settled. It is not sufficient to promise an edge or launch automatic orders. The next evidence priorities are independently verified historical/live candles, numerical cutoff cases for all six pilot IDs, and a frozen prospective protocol. Additional chart reading cannot replace those checks.
