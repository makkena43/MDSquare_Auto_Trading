> **Precedence:** The [v2.3 canonical specification](../automatic-trading-technical-specification.md) and [unified skill](../brooks-index-analysis/SKILL.md) govern the current design. This earlier synthesis is supporting background; options and real execution are deferred.

# Context-first trade identification

Draft 0.1.0. Scope: underlying NIFTY/BANKNIFTY price-action interpretation only. Option selection and execution economics are deferred. Definitions are research hypotheses, not validated probabilities. This document refines the trading-doctrine scope; it does not enable new setup IDs or implement code.

## Owner-selected context policy

Applies to every setup family, not only H2/L2:

- Tight trading range: no new trade candidates inside it. Observe/wait for a credible escape and reassess context. A large candle alone does not establish escape.
- Wide established range: assess longs near its previously identified lower boundary and shorts near its upper boundary. Avoid the middle. Require inward/rejection evidence and remaining room; never buy/sell blindly just because price touched an edge.
- Bull trend: continuation is the working thesis; an opposing signal is initially assessed as a potential correction rather than an automatic major reversal.
- Bear trend: continuation is the working thesis; apply the corresponding logic to upward reversal attempts.
- Transition: change the thesis when observable opposing strength/structural failure and subsequent evidence support it. Inertia is not a reason to ignore credible change.

Brooks describes inertia for both trends and ranges: most trend-reversal attempts and most trend-breakout attempts from ranges fail. See his [market-inertia explanation](https://www.brookstradingcourse.com/price-action/what-is-price-action-6-aspects/) and [range guidance](https://www.brookstradingcourse.com/how-to-trade-manual/trading-ranges/). His 80% formulation is a contextual teaching heuristic, not a measured NIFTY/BANKNIFTY probability, guaranteed continuation, or a parameter for sizing/confidence.

Tight versus wide must be assessed causally on the analysis timeframe using boundary width, candle size/overlap, feasible structural invalidation and remaining distance after confirmation. Numerical thresholds are unresolved and must be fixed before scoring. Width alone is insufficient: a wide range can contain local tight congestion. A short pause within a strong trend is not automatically a standalone two-sided tight range; explain the distinction with preceding structure and current evidence. Ambiguous local congestion warrants WAIT rather than bypassing the no-trade rule through a flag label.

Lower/upper boundaries mean observable zones established before entry, not the day's eventual exact low/high. Initially assess an internal target; do not assume travel to the far edge. While price demonstrates sustained acceptance outside, stop applying blind edge-fading logic and evaluate the breakout/transition thesis. No new opening, reversal or range-double-test ID is enabled by this policy; use existing eligible IDs or observation only.

## Decision order

Assess current structure -> location -> sequence -> signal -> available confirmation -> conflicting evidence -> conditional plan or abstention. Pattern counting never establishes direction by itself. Use only evidence available at the cutoff.

Store four distinct observations: higher-timeframe background, current intraday regime, local corrective leg and signal sequence. A daily bull background can coexist with an intraday bear trend. A two-legged downward correction can exist within either a bull trend or a bear trend. Do not collapse those observations into a single bullish/bearish label.

## H2 across contexts

| Context at cutoff | Interpretation | Evidence required | Preferred research decision |
| --- | --- | --- | --- |
| Bull trend with orderly pullback | Potential continuation long | Prior directional strength, corrective first attempt then renewed correction/second attempt, bullish signal, preserved continuation structure and room to visible resistance | Conditional long candidate if fully specified; otherwise WAIT |
| Tight bear trend | Countertrend long attempt | H2 count alone does not show bears lost control; check actual structural break, bullish strength and retest | Usually SKIP continuation-long classification; observe any separately enabled reversal thesis |
| Bear trend weakening after a material break and successful retest | Potential emerging bull/reversal context | Bull impulse, break of relevant bear structure, retest holding and bullish resumption evidence | Reassess regime; do not promote solely because an H2 appeared. Disabled reversal family stays observational |
| Established range near lower edge | Possible range long | Boundary established before current test, downside failure/return inside, credible long signal and room toward an internal reference | Evaluate range-failure thesis; H2 may be supporting evidence, not a second order |
| Established range near upper edge | Long into an opposing boundary | Evidence of genuine outside acceptance would be needed to justify continuation | Usually SKIP long; WAIT for a distinct breakout/test if developing |
| Range middle / tight overlap | Ambiguous small continuation attempt | No favorable location or clear directional control | No trade candidate; WAIT or SKIP under the owner-selected policy |
| Bull trend stretched near major opposing structure | Possible late continuation or exhaustion | Assess preceding expansion, corrective quality, remaining target room and opposing evidence | WAIT/SKIP when the proposed continuation lacks room or structure; do not assume reversal |

L2 is evaluated with the directional relationships reversed, while retaining separate empirical validation. An H2 inside a bear leg can be recognized correctly without becoming an eligible long trade.

## Evidence for context

Use relative observations rather than one-indicator declarations:

- Directional strength: coherent swing progression, close quality, follow-through, overlap and depth of opposing legs.
- Continuation structure: whether the relevant prior swing/breakout boundary still holds; distinguish a minor correction from a material failure.
- Range evidence: repeated rejection/return, overlap and boundaries supported by earlier price action. Future extremes cannot define today's earlier range.
- Transition evidence: meaningful structural break, opposing impulse and subsequent test; one opposite candle is insufficient.
- Location: near a previously identified edge, test or swing versus interior congestion; distance to the first visible obstacle.

No majority vote or arbitrary weighted score is established here. Record evidence for and against the regime, and what future observable event would distinguish competing hypotheses. Uncertain regime is a valid result.

## H2 counting and signal readiness

Identify the corrective sequence, first upward attempt, renewed correction and second attempt from actual candle IDs. Record whether an attempt already crossed its trigger. A completed signal for a prospective second attempt and an already-triggered H2 are different states. Equal highs/tick tolerance and nested legs need fixed definitions. Never identify the second attempt from two green candles alone.

A research candidate needs observable trigger, structural invalidation, target reference and explicit missing evidence. Production CANDIDATE still requires numeric levels, policy expiry and context identity. Qualitative context discussion cannot arm a trade. Do not use future success to justify today's count.

## Compact assessment record

For each proposed setup, record:

1. Higher-timeframe background and intraday regime, with evidence and uncertainty.
2. Location and level provenance.
3. Sequence and signal bar IDs; attempt-count ambiguity and trigger status.
4. Thesis type: continuation, range rotation or reversal observation.
5. Strongest contradicting evidence.
6. Conditional trigger, structural invalidation and first opposing obstacle.
7. Decision: candidate/wait/skip/insufficient data, plus what would change it.

Example original qualitative assessment: intraday bull structure remains intact; correction holds a previously identified breakout area; first upward attempt is followed by renewed correction and a completed bullish second-attempt signal; a prior high remains an obstacle. Interpretation: possible continuation long, conditional on the supplied trigger and available room. If the same sequence occurs inside a strong bear move with no structural change, recognize the count but reject its classification as bull continuation.

## Evaluation design

Build matched examples: similar H2 shapes in bull continuation, strong bear context, range lower edge, range upper edge, range middle and transition. Hide later candles and hindsight annotations. Include failed bull-context H2s and successful countertrend H2s: a sensible decision can lose, and a rejected low-quality idea can win.

Score context, location, sequence and decision consistency separately from later price outcomes. Review disagreement explicitly. Test an independent untouched chronological/prospective set only after definitions are frozen. No numerical win rates, context thresholds or setup frequency have been established.
