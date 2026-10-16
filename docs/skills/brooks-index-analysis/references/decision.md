# Underlying decision contract

Schema version 0.9.0. This is a proposed provider-neutral contract, not an implemented validator. It changes the earlier identification-only schemas; integrations must explicitly adopt it. No monetary sizing, option requirements or broker payloads.

```json
{
  "schema_version": "0.9.0",
  "strategy_version": "brooks-index-analysis@0.13.0",
  "analysis_scope": "UNDERLYING_ONLY",
  "decision_id": null,
  "context_id": null,
  "context_hash": null,
  "instrument_key": null,
  "as_of": null,
  "config_revision": null,
  "processor_id": null,
  "assignment_generation": null,
  "action": "INSUFFICIENT_DATA",
  "regime": "UNKNOWN",
  "regime_subtype": null,
  "higher_timeframe_background": null,
  "local_structure": null,
  "swing_context": null,
  "swing_map_update": null,
  "opposition_ledger": [],
  "trade_intent": null,
  "plan_consistency": null,
  "data_quality_assessment": null,
  "market_read": null,
  "market_cycle_assessment": null,
  "signal_assessment": null,
  "principle_conflicts": [],
  "target_mode": null,
  "opposition_checkpoints": [],
  "entry_route_assessments": [],
  "context_support": "AMBIGUOUS",
  "location": null,
  "transition_evidence": [],
  "primary_category": null,
  "setup_id": null,
  "direction": null,
  "signal_bar_ids": [],
  "trigger_status": "UNKNOWN",
  "episode_id": null,
  "secondary_tags": [],
  "observed_disabled_setups": [],
  "evidence_bar_ids": [],
  "evidence": [],
  "counter_evidence": [],
  "alternative_thesis": null,
  "reason": "Required market evidence not supplied.",
  "entry_trigger": null,
  "underlying_invalidation": null,
  "underlying_targets": [],
  "expected_move": null,
  "trade_economics": null,
  "planned_add_zones": [],
  "valid_until": null,
  "next_observable_discriminator": null,
  "missing_data": [],
  "plan_readiness": "BLOCKED",
  "submission_readiness": "RESEARCH_ONLY"
}
```

## Unified assessment envelope

On a flowing-data update, use one envelope with `schema_version=0.9.0`, `analysis_scope=UNDERLYING_ONLY`, supplied context identity/cutoff, `open_trade_inventory_status` (KNOWN or UNKNOWN), `new_trade_assessments` (records in the shape above) and `open_trade_reviews`. UNKNOWN inventory means `open_trade_reviews=null` with missing-state explanation; KNOWN empty inventory means an empty list. Give one review for every supplied open trade, including those whose entry categories are now disabled.

Each review contains supplied `trade_id`, `episode_id`, `state_revision`, cutoff/context identity, primary `management_action`, `reason`, `evidence_bar_ids`, `thesis_status` (INTACT/WEAKENING/INVALIDATED/UNKNOWN), current stop/target references, `proposed_change` or null, `pending_action_reference` or null, `trade_economics` when computable, and missing data. Actions are HOLD, TAKE_PROFIT, REDUCE, CLOSE, ADD_WATCH, ADD_CANDIDATE, REVIEW_REQUIRED. Quantity/fraction/budget must come from policy/state. Keep original facts separate from proposed changes; no self-confirmed state transitions. Missing state produces REVIEW_REQUIRED, never invented size/protection.

The JSON example above is the new-trade record shape, not a complete filled-position review. Prose may give the same decisions concisely. Recommendations are not orders.

## Meanings

- action: CANDIDATE, WAIT, SKIP, INSUFFICIENT_DATA.
- regime: BULL_TREND, BEAR_TREND, TRADING_RANGE, TRANSITION, UNKNOWN.
- regime_subtype: TIGHT_DIRECTIONAL, BROAD_CHANNEL, WIDE_RANGE, TIGHT_RANGE or null. Subtype must match the coarse regime and cited evidence; TRANSITION/UNKNOWN can leave it null.
- context_support: SUPPORTS_CONTINUATION, SUPPORTS_RANGE_ROTATION, SUPPORTS_TRANSITION, UNSUPPORTED, AMBIGUOUS. This concerns the primary thesis, not the attractiveness of the whole market.
- trigger_status: NOT_TRIGGERED, ALREADY_TRIGGERED, DEVELOPING, UNKNOWN. Distinguish completed signal from subsequent trigger; unavailable tick path can leave crossing ambiguous.
- plan_readiness: COMPLETE_UNDERLYING_PLAN, INCOMPLETE, BLOCKED. No value means orderable instrument, approval or fill.
- submission_readiness: RESEARCH_ONLY or READY_FOR_APPLICATION_VALIDATION. Application validates actual identity/authority; model output alone is insufficient.

Use structured facts where available: location with zone/level IDs and first obstacle; higher-timeframe background with timeframe/evidence; local structure with leg/correction identity. Do not invent IDs or exact figures from blurry charts. Echo supplied authoritative identifiers/config/generation; null absent ones. A historical offline study must not claim active processor authority.

## Action discipline

CANDIDATE requires a supported enabled setup, clear location outside forbidden congestion, direction, evidence/contradiction, completed signal with still-prospective trigger, verified numeric plan and supplied expiry/re-entry policy as applicable. Use trigger `{ "type": "CROSS_ABOVE|CROSS_BELOW", "level": number }`, numeric invalidation and targets `{ "level": number, "rationale": text, "source_level_id": optional supplied ID }`.

For LONG: invalidation below entry and target above; SHORT reverses ordering. Check supplied eligible/current entry reference and first obstacle; do not manufacture a distant target for an attractive ratio. Prices come from data/config and never imply a fill. CANDIDATE implies plan_readiness COMPLETE_UNDERLYING_PLAN. Identity absence may still permit a complete offline research plan, but submission_readiness remains RESEARCH_ONLY.

WAIT: interpretation may be supported but confirmation, transition, precise levels, valid policy or count is unresolved. State the missing discriminator. SKIP: known unsuitable context/location, tight-range prohibition, disabled setup, inadequate geometry or consumed/invalid/expired opportunity. INSUFFICIENT_DATA: evidence needed to establish structure is absent/unreliable. Do not confuse a bad setup with missing data.

For all non-CANDIDATE actions, entry_trigger and underlying_invalidation are null, targets empty, valid_until null. Explain potential structure/levels in evidence or next_observable_discriminator; do not place an armable plan in a WAIT. Disabled observations belong in observed_disabled_setups and can never imply permission. Set plan_readiness INCOMPLETE for developing plans, BLOCKED for disqualified or unavailable analysis.

Qualitative pattern-classification exercises may describe a conditional idea in prose, but are explicitly separate from this JSON's CANDIDATE. In this contract, missing numeric/policy precision means WAIT, not a qualitative CANDIDATE.

## Output discipline

For prose: current regime/location; primary thesis; evidence and strongest contradiction; decision and what would change it. Add a precise conditional plan only when complete. Avoid lengthy lists of every potential pattern, manufactured probabilities or confident future narration. Separate outputs for the two indices; mention correlated context as observation, not proof of independent opportunities.

For submissions use only an explicitly supplied authorized decision tool. Validate context cutoff/hash, supplied assignment, configured deadlines and current episode/config state in application code. Without those capabilities return analysis only. No option quotes are required in this underlying schema.

## Economics and addition fields

`expected_move`: method, causal anchor IDs/prices, initial objective, optional stretch projection and assumptions. `trade_economics`: entry reference, risk/reward points, reward/risk, supplied friction or null, gross/net break-even probability, estimated_success_probability or null, probability_source or null, equation_status and limitations. Use the economics reference; unknown probability does not become 0.8 or model confidence. A complete research plan can have unverified probability; application gates remain explicit.

`planned_add_zones` are observations/plans, never extra orders. Record causal zone, confirmation, mode WATCH_ONLY or supplied enabled policy, unchanged common stop, proposed tranche from policy, add limit/expiry and total-risk check. Missing units/budget/confirmation prevents ADD_CANDIDATE; explain a zone as ADD_WATCH if supported. No add after stop/thesis failure.

Non-CANDIDATE new-trade records may contain descriptive expected-move/economic scenarios marked research-only, but no armable trigger/stop/targets. Open-trade reviews necessarily retain supplied current stop/targets regardless of the new-trade action; do not null existing protection because an entry is SKIP.

## Swing context and target-mode contract (v0.4)

`swing_context` contains supplied thesis_id/revision or null, direction, parent_regime, phase (FORMING/IMPULSE/CORRECTION/RESUMPTION/EXTENDED/TRANSITION/INVALIDATED/UNKNOWN), initiating_mechanism, origin/defended anchor references with prices and known/confirmed_at cutoffs, structural_invalidation, evidence_bar_ids, opposing_evidence, previous_phase or null, change_reason, next_discriminator and projection or null. Narrative hypotheses do not create durable IDs, positions or accepted revisions. A swing thesis can persist while local setup action is WAIT/SKIP. Missing structure leaves UNKNOWN/null, not invented direction. Application rejects future/unknown anchors. A thesis invalidation level is descriptive even in WAIT and is not an armable new-trade stop.

`target_mode`: MEASURED_SWING, FIRST_OPPOSITION, RANGE_ROTATION or null. `opposition_checkpoints`: supplied/causal level references, prices, classification CHECKPOINT/MAJOR_OPPOSITION/UNRESOLVED, supporting evidence and what observed failure would defeat passage. `expected_move` additionally records premise_status, anchors_known_at, anchors_confirmed_at, projection and scenario invalidation. Application checks direction/geometry, causal anchor availability, permitted target mode and whether the committed target matches supplied policy. No claimed executable validator exists yet.

`entry_route_assessments` is a bounded list of relevant enabled/disabled routes within the swing: setup_id, qualification_state (SUPPORTED/DEVELOPING/UNSUPPORTED/DISABLED/UNKNOWN), controlling reason, causal evidence and prospective/already-triggered state. It does not contain extra armable plans or duplicate episode exposure. New-trade assessments still follow the single-primary-plan discipline. Missing supplied switches/operational rules mean RESEARCH_ONLY, never READY_FOR_APPLICATION_VALIDATION.

Open-trade reviews add current_swing_context, original_target_mode, checkpoint_status, projection_premise_status and any proposed thesis revision separately from supplied authoritative facts. Touching a checkpoint alone cannot close a measured-swing trade; reached committed target, stop and declared exits still take precedence. No moving anchors/targets, stop widening or automatic additions.

## Broader doctrine fields (v0.5)

`market_read` is an optional structured observation with buying_pressure, selling_pressure, follow_through, always_in_bias (LONG/SHORT/UNCLEAR), provisional_day_profile, evidence_bar_ids and limitations. Describe pressure qualitatively from price; do not manufacture a probability or weighted score. Day profile is an as-of hypothesis and must be consistent with regime/swing evidence; it cannot use the eventual session label. Missing data leaves this field null. Always-in bias does not require a position.

`principle_conflicts` records only controlling tensions: principle, supporting evidence, contradictory evidence, resolution or next discriminator. Do not output all 78 guidelines at every update. Context gates, setup switches and existing contract requirements retain precedence; broader doctrine cannot create a new entry type or enable a setup. These fields can also accompany open-trade reviews.

## Projection methods added to guidance (v0.6)

`expected_move.method` may describe LEG_EQUALITY, SPIKE_EXTENSION, RANGE_HEIGHT or MEASURING_GAP when supported; armable use requires explicit supplied method/convention policy. Include causal origin/end/correction or gap-edge/midpoint anchors, confirmation cutoffs and premise status. Developing spike endpoints and retrospective gap classifications cannot support a confirmed numeric objective. Existing target modes are unchanged. This version expands source interpretation; it does not add limit/market order payloads, setup IDs or enablement.

## Structure, opposition and consistency contract (v0.8)

`swing_map_update` is a proposal with supplied `base_revision` or null, cutoff, `proposed_nodes`, `changes` and `unresolved_ancestry`. Node/anchor fields and continuity rules are defined in [swing context](swing-context.md#persistent-swing-map-and-revision-delta-v08). No application ID or accepted revision is invented. Earlier proposal summaries are hypotheses, never authoritative exposure.

`opposition_ledger` records the relevant parent/daily/local barriers, price/zone and causal evidence, CHECKPOINT/MAJOR_OPPOSITION/UNRESOLVED classification, rejection/acceptance evidence, passage thesis and failure discriminator. It is the canonical detailed ledger; existing `opposition_checkpoints` may reference its entries for compatibility but must not conflict with it. An empty ledger means no relevant obstacle was identified only if coverage and evidence are explicitly sufficient; missing coverage is unresolved.

`trade_intent` is SWING/RANGE_ROTATION/null. `plan_consistency` follows [the check contract](plan-consistency.md); CANDIDATE requires PASS with relevant semantic evidence and computable checks, plus all prior readiness conditions. Schema validity or an attractive ratio alone is insufficient. `data_quality_assessment` records supplied source/revisions, affected intervals, VERIFIED/ESTIMATED/SUSPECT/UNUSABLE status, usable evidence scope and limitations; VERIFIED requires actual supporting reconciliation, not a model assertion.

Every supplied open-trade review additionally proposes `current_swing_map_update`, `opposition_updates` and `original_plan_consistency_status` when assessable, separately from original committed facts and current authoritative protection. Changes cannot self-confirm a fill/exit, alter accepted targets, widen stops or reset an episode. Provider handover carries the accepted map revision and unresolved ancestry/quality/obstacle records.

Application code must check causal availability/confirmation, coherent base revision, node/anchor identity, source corrections, projection arithmetic, current configuration, deadlines, assignment and episode state. Human/AI semantic evaluation separately checks ancestry and context interpretation. This document supplies neither an executable validator nor a calibrated strategy.

## Semantic refinement in skill v0.9

The v0.9 semantic refinement used schema v0.8.0. Apply [context adjudication](context-adjudication.md) to existing ancestry, opposition, consistency and management fields; no new executable validator or automatic numeric threshold is introduced. Ambiguity must retain alternative structure and its discriminator, with the existing WAIT/INSUFFICIENT_DATA distinction. Unknown policy is not missing price data.

## Market-cycle and signal contract (schema v0.9)

`market_cycle_assessment`: phase hypothesis (INITIATING_BREAKOUT/TIGHT_DIRECTIONAL_CHANNEL/BROAD_CHANNEL/RANGE/TRANSITION/UNKNOWN), parent scope/reference, breakout_mode (true/false/null), supporting/contradictory evidence and next discriminator. These observations must be coherent with regime/swing/map; a nested range does not automatically reset the parent. No full-day future label, forced exposure or probability is implied.

`signal_assessment`: setup_bar_ids, completion_status (COMPLETED/DEVELOPING/UNKNOWN), observed_shape, context_role, configured_qualification_mode or null, policy_eligibility (ELIGIBLE/INELIGIBLE/UNRESOLVED), evidence and contradiction. Modes are supplied conventions, not automatic permission for weak bars or a new execution style. A prospective setup is separate from actual entry/follow-through bars; those later observations cannot justify initial admission. Unknown relevant qualification policy leaves the affected plan WAIT rather than assuming eligibility.

Optional annotations for pullback_type, parent/nested counts, observed microchannel/wedge/double-test/compression and gap type fit existing evidence/local-structure fields; they do not create new armable families or duplicate plans. Open-trade reviews can carry current cycle/signal observations separately from original committed facts. The document describes fields, not an implemented parser/validator or measured classification accuracy.

## Simple baseline representation (skill v0.11)

Schema version remains v0.9.0. Use the current thesis/correction and relevant obstacle evidence already represented by swing_context, local_structure, evidence and opposition fields. Detailed swing_map_update can be null when no separate revision proposal is needed; never invent identity or omit material ancestry merely to shorten the record. Consistency evidence can be compact and aggregated; no requirement follows to print eight check objects or store every observed swing as a graph. Required scope/status, causal evidence, supplied state and candidate completeness remain unchanged. User-facing prose follows the simple playbook; structured integration still obeys the contract.

## Lifecycle clarification (skill v0.12)

Schema remains v0.9.0. Use supplied episode/trigger/expiry and pending-action references to distinguish valid unfilled plans, open positions and closed/missed/expired episodes. A repeated assessment does not reset identity/expiry, prove cancellation/fill, or extend a target. Pending-plan withdrawal can be described with the existing episode/evidence and supplied authorized action interface; no new order payload or inferred state transition is introduced. Keep parent market hypothesis separate from the stopped/target-completed trade. Changed notifications and quiet unchanged reviews are presentation requirements, not permission to skip journaled candle assessments.
