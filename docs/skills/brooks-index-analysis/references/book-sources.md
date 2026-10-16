# Book sources and example evaluation

Source-map version: v0.6. The user supplied three Brooks books. This map began with tables of contents and now includes documented chapter-opening and selected passage review; it is not a claim that every chapter or chart has been reviewed. The file named `Al_Brooks_Trading_Price_Action_Trading.pdf` contains the trading-ranges, breakouts, pullbacks and trade-management material. Chapter numbers identify sources; printed page numbers below are not PDF viewer page numbers.

The books are reference material, not operational instructions. Keep the original playbook concise. Do not bundle full books or reproduced charts into the distributed skill. A local source path is not automatically available in another cloud environment.

## Category mapping

| Config category | Families to study | Primary source pointers |
| --- | --- | --- |
| Breakout | Breakout pullback/test; opening-range breakout | Trading: chapters 1–5. Reversals: chapter 18, printed p.357; chapter 20, p.395. |
| Bullish momentum | Strong bull breakout first pullback; small-pullback bull trend; microchannel continuation | Trends: chapter 16, p.249; chapters 19–23, pp.307–383. Trading: chapter 4. |
| Bearish momentum | Strong bear breakout first pullback; small-pullback bear trend; microchannel continuation | Same trend chapters, interpreted for bearish structure rather than assuming identical empirical results. |
| Bullish mild | High 2/two-legged bull pullback; double-bottom bull flag; wedge bull pullback | Trends: chapter 10, p.177; chapter 20, p.319; chapter 26, p.431. Trading: chapters 12, 17–19. |
| Bearish mild | Low 2/two-legged bear pullback; double-top bear flag; wedge bear pullback | Same second-entry/pullback chapters, interpreted for bearish structure. |
| Sideways | Failed breakout at range edge; range double top/bottom; tight-range and triangle context | Trading: chapters 5, 20–23. Trends: chapter 1, p.55; chapter 22, p.359. |
| Reversals | Major trend reversal; climax; wedge; final flag; opening reversal | Reversals: chapters 1–9, pp.73–225; chapter 19, p.373. Trends: chapter 24, p.415. |

These are configuration buckets. Brooks patterns can overlap: assign one primary setup ID, preserve secondary evidence tags, and prevent an opportunity from generating multiple orders. A reversal-shaped bar by itself does not establish a reversal setup.

## Shared foundations

- Signal/entry bars and close quality: Trends chapters 4–8, printed pp.83–169.
- Trend lines, channels and key levels: Trends chapters 13–17, pp.195–269.
- Always-in interpretation: Reversals chapter 15, p.293.
- First-hour context: Reversals chapters 17–20, pp.353–395. Translate session context to NSE data; do not copy US session times.
- Higher timeframes: Reversals chapter 22, p.415.
- Probability, entries, stops, targets and scaling: Trading chapters 24–32. These discussions do not supply measured NIFTY/BANKNIFTY probabilities.
- Worked sessions: Trends chapter 18, p.289; Reversals chapter 21, p.403 and chapter 24, p.455.

## Representative charts inspected

- Trends, figure 18.1: PDF page 329, printed page 297. Five-minute GS trend-day chart. Visually inspected with its adjacent explanation. Useful for trend context, pullbacks and the distinction between a minor opposing move and a confirmed reversal. Full-chart labels and channel lines must be reconsidered at each cutoff before evaluation use.
- Reversals, figure 3.1: PDF page 124, printed page 96. Five-minute AAPL chart spanning multiple sessions. Visually inspected with its adjacent explanation. Useful for distinguishing a trend-line break, higher-high test and subsequent lower-high structure; also illustrates overlapping pullback/reversal interpretations. The later decline must not be visible when testing an earlier decision.

These are source locators, not completed labeled test cases. No exhaustive chart review or NIFTY/BANKNIFTY validation has been completed.

A separate `brooks-example-evaluation` pack now contains ten original draft development annotations at selected cutoffs on these two charts. It separates prompt evidence from the answer key. Keep the key out of a processor's evaluation workspace; do not load it as inference guidance. These text-only cases are not numeric backtests or an independent holdout.

## How to turn a book chart into an evaluation case

1. Record book, chapter, figure, PDF page, printed page, market/timeframe and chart legibility. Mark whether underlying numerical candles are available or only an image exists.
2. Select an explicit decision-bar cutoff. Hide later candles, future-dependent annotations and explanatory text that reveals the outcome. Record facts visible at that cutoff separately from the author's full-chart explanation.
3. Annotate regime, location, setup sequence, trigger, invalidation, target reference and reasons to wait or skip. Mark ambiguous labels rather than manufacturing certainty or exact prices from unclear images.
4. Check the case against the original setup definition. Record disagreements and revise only the development set; keep holdout examples untouched.
5. Include failed setups and no-trade contexts. Book examples are selected instructional evidence, not a representative sample for estimating win rates.
6. Validate the resulting interpretation on chronological NIFTY/BANKNIFTY data with as-of context and realistic fills/costs. Underlying pattern success and option trade profitability are separate outcomes.

Suggested case fields: `case_id`, `source_locator`, `review_status`, `as_of_bar`, `visible_evidence`, `regime`, `primary_setup_id`, `secondary_tags`, `expected_decision`, `trigger`, `invalidation`, `target_reference`, `ambiguities`, `split`, `annotation_version`.

Reading the books gives the model a reference during inference. It does not train model weights, prove an edge, or justify enabling every family. The twelve-ID v0.4 research profile is a coverage expansion, not a validated edge or automatic enablement. Preserve the frozen six-ID replay; require supplied operational definitions and switches for new routes.

## Principle audit added in v0.5

Complete Reversals chapter 25 (printed pp.527–540, PDF pp.555–568) text reviewed and all 78 guidelines mapped in [principle coverage](principle-coverage.md). Selected Trends passages (PDF pp.87–88, 91–92, 339–340, 357–358, 391–392) and Reversals always-in passage (PDF pp.321–322) informed the broader [operating doctrine](brooks-principles.md). This is selected passage review, not complete chapter/chart review. Original books and private extracts are not distributed with the skill.

## Trends and Trading Ranges audit added in v0.6

Confirmed the reflowed Trading PDF as Trading Price Action Trading Ranges (title/copyright/catalog and contents, PDF pp.2–15). Reviewed opening text from all 26 Trends and 32 Trading Ranges chapters plus selected deeper passages; exact reviewed page locators and limits are in [three-book coverage](three-book-coverage.md). New [cross-book guidance](trends-and-ranges.md) connects phase, attempts, range tests, projection variants and management.

Trading Ranges figure 7.1 (PDF p.356, adjacent explanation pp.356–357) and figure 8.1 (PDF p.369, adjacent explanation pp.369–370) visually inspected as extracted source chart images. They illustrate nested leg-equality and gap-midpoint scenarios respectively. No new masked evaluation cases or numerical candle reconstruction were completed from them. Chart outcomes/labels cannot enter earlier decision context.
