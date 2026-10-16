# Plan consistency before accepting a new trade

Version 0.8.0. These are reasoning and proposed validation requirements, not an implemented runtime gate or evidence of profitability. Use after context/sequence interpretation and before CANDIDATE. Existing protection is always retained independently.

## One thesis, one coherent plan

Declare `trade_intent` SWING or RANGE_ROTATION and `target_mode` MEASURED_SWING, FIRST_OPPOSITION or RANGE_ROTATION. A swing can use first opposition if supplied policy supports that objective; do not imply that every swing must reach 2R. Do not pair a minor-pause stop with a parent-swing objective without an explicitly configured tactical variant. No such variant is enabled by default.

Record `plan_consistency` with status PASS/FAIL/UNRESOLVED, the supplied policy revision, semantic checks below, mechanical checks when computable, controlling reason and evidence. Each check has a stable name, PASS/FAIL/UNRESOLVED status, evidence/anchor references and a short explanation. PASS means the plan is internally supported under current evidence, not a proven profitable trade.

| Check | Evidence needed |
| --- | --- |
| context_and_location | Parent regime, independent swing or range-rotation rationale; no tight-range entry or unqualified range-middle swing |
| correction_ancestry | Full relevant correction/base/failed excursion retained; no confirmation-time reset or replacement by a nested pause |
| stop_matches_thesis | Specific defended structure and breach meaning; full corrective entry stop versus base stop versus failed-excursion stop; no arbitrary distance padding |
| objective_matches_thesis | Permitted method/convention, causal anchors and endpoint confirmation; scenario travel credible in this context |
| opposition_coverage | Relevant daily AND parent/local intraday obstacles assessed; beyond-obstacle passage justified or target constrained |
| intent_and_economics | Positive risk/reward; configured ratio/cost policy passed at eligible entry without shrinkage or target stretching; probability provenance separate |
| timing_and_identity | Completed available signal, still-prospective trigger, configured expiry, unconsumed episode, current config/assignment and data revision |
| inventory_and_policy | Authoritative inventory supplied for application submission; permitted setup/category/risk reservation; no duplicate exposure |

Report numerical risk relative to observed bar sizes as a diagnostic when available. It is not automatically a universal rejection threshold or a reason to widen a filled stop. Initial risk is an entry-time fact; future maximum adverse excursion is an outcome.

## Disposition

- All required semantic checks and computable mechanical checks must pass for a complete research CANDIDATE. Probability may remain unverified if the supplied paper policy allows it; do not mark expectancy favorable.
- Known unsuitable context, stop/target inconsistency, inadequate economics, forbidden or consumed entry means SKIP. Missing structure/source evidence means INSUFFICIENT_DATA. Pending confirmation or unresolved interpretation/policy means WAIT.
- A WAIT can describe alternatives and a next discriminator but contains no armable trigger/stop/target fields. Avoid silently switching intent or anchors just to pass the checks.
- Application submission also requires verified identity, assignment, policy and authoritative state. Code recomputes prices/projections/geometry and checks revisions/finality. Semantic judgments cannot be proven by a schema validator; retain supporting evidence for review.
- A new-trade FAIL must not remove an existing trade's stop/target, invent a close, or widen protection. Manage supplied positions using their committed thesis and exit policy.
