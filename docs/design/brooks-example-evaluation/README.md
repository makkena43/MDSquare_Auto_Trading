# Brooks example evaluation pack

Version 0.1.0, 2026-10-11. This is an original qualitative annotation pack for development, not a trained model, trading application or proof of profitability.

These records use a research-only annotation scope. A CANDIDATE label here means a conditional qualitative idea. It does not satisfy the production skill's numeric trigger/invalidation/target, expiry, identity and policy requirements, and cannot be submitted to its validator. Production analysis with insufficient price precision must use WAIT or INSUFFICIENT_DATA as specified by its contract.

## Files

- `cases.jsonl`: ten cutoff-specific descriptions without expected answers or later outcomes.
- `answer-key.jsonl`: separate draft interpretations, conditions and limitations.
- `cases.md`: readable review document containing both descriptions and answers. Do not give it to a processor being evaluated.
- `export_prompt.py`: exports one case as a provider-independent text prompt. No API, credentials or network calls.

## Run a case

Run `python3 export_prompt.py T03` from this directory and give only its output to the processor. Keep the answer key and `cases.md` outside its accessible evaluation workspace. Having them in the same repository does not enforce separation. The exporter removes book/figure identity from the prompt, although a model may still recognize a famous example.

The processor returns JSON with `decision`, `primary_setup_id`, `supporting_evidence`, `conflicting_evidence`, `conditional_trigger`, `invalidation`, `target_reference`, `missing_data`, and `execution_ready`. Candidate plans must be conditional and execution readiness false. Missing exact data may justify INSUFFICIENT_DATA; reviewers should distinguish refusing numerical execution from refusing a supported qualitative observation.

## Review rubric

Score each dimension 0 (wrong/missing), 1 (partly supported), or 2 (well supported):

1. Cutoff discipline: no later bars, completed future tests, later annotations or known outcome used.
2. Context: distinguishes trend strength, weak correction and range congestion.
3. Setup: identifies the actual sequence; distinguishes signal from future trigger; acknowledges uncertain counts.
4. Decision/config: respects disabled families and does not force a trade from a pattern label.
5. Plan: trigger, structural invalidation and target refer to visible evidence, with missing exact levels disclosed.

Treat fabricated numeric prices/probabilities, future evidence, an actionable disabled setup, or claimed execution readiness as a failed case regardless of total score. Do not treat agreement with this single-annotator key as proof of correctness. Record justified disagreements and obtain independent review before treating labels as authoritative.

Compare processors using the same prompt, skill/config version and model settings. Record provider/model, run timestamp, response, rubric scores and reviewer comments. Multiple cutoffs on one chart are correlated examples: split by chart/session, not by individual case.

## What this pack establishes

The cases test instruction following and qualitative reasoning, including WAIT and SKIP. They do not test fills, stop execution, profitability or measured win rate. They contain two chart sources, not ten independent markets. No historical trade outcomes are scored.

The annotations were prepared with full-book access, so author hindsight may influence draft labels even though prompt evidence excludes later events. Raw chart labels and trend lines can themselves incorporate hindsight. Therefore this pack is not a blind holdout or a validated causal reconstruction. Numeric OHLC and independently reviewed cutoff charts are required for stronger evaluation. No chart crops are included; an evaluator must not open the full book chart mid-case.

Coverage currently includes bullish H2/breakout-pullback context and bearish major-reversal observation. It does not establish bearish L2 or sideways failed-breakout coverage, and does not enable reversal trading. Add genuine source cases for missing families rather than mirror existing cases and count them as independent evidence.

For NIFTY/BANKNIFTY validation, prepare chronological unseen candle windows with daily/session context available only as of the decision, retain failures and no-trade windows, and assess executable option outcomes with spreads, slippage and fees separately. Set risk and success criteria before inspecting holdout outcomes.
