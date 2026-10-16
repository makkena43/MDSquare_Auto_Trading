# MDSquare Auto Trading

A working market-data and paper-research foundation for NIFTY and BANKNIFTY. Upstox data feeds one local SQLite journal; ChatGPT or Claude can review the same exported context using the unified Brooks skill. **There is no broker-order implementation.**

## Start

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
mdsquare init
mdsquare assign chatgpt
```

Supply an Upstox access token through `UPSTOX_ACCESS_TOKEN` in your environment, or reuse your existing Quant Investing YAML **without copying it**:

```sh
export UPSTOX_LEGACY_CONFIG=/absolute/path/to/MDsquare_Quant_Investing/src/main/resources/application.yml
mdsquare backfill
mdsquare poll
mdsquare run
```

`backfill` requests the previous 30 calendar days of one-minute candles and 90 calendar days of daily context for both indices. `poll` refreshes the current session once. `run` polls every 60 seconds until interrupted; launch it during regular market hours. Holidays/special sessions need an authoritative calendar integration before unattended operation. Invalid credentials fail clearly without printing tokens. No token, configuration secret, database or generated market data belongs in Git.

## Review in ChatGPT or Claude

```sh
mdsquare export-context NIFTY --out runtime/nifty-context.json
mdsquare export-context BANKNIFTY --out runtime/banknifty-context.json
```

Supply the JSON and [Brooks skill](docs/skills/brooks-index-analysis/SKILL.md) from this repository to your analysis environment. The database retains the rolling history; the compact context shows the latest 150 completed five-minute candles (about two sessions), up to 60 daily bars, policy, original active paper plans and processor generation. Referenced active-plan evidence is retained. Fetch older structure when needed with `mdsquare export-history NIFTY --start 2026-10-01T09:15:00+05:30 --end 2026-10-02T15:30:00+05:30 --out runtime/older-slice.json`. These display limits are configurable and are not strategy filters. It excludes unfinished bars and data not observed by the cutoff. Missing current-session candles block candidates; gaps are never filled with invented prices. There is no automatic model API connection or cloud scheduler yet.

Return a `foundation.v1` review as described in [the review interface](docs/review-interface.md), then import it into the authoritative local database:

```sh
mdsquare submit runtime/review.json
mdsquare events
mdsquare backup runtime/handover.sqlite3
```

Switch provider with `mdsquare assign claude`, then export fresh contexts. Old-generation outputs are rejected. The worker does not own inventory and cannot declare its own fills. Provider changes preserve original paper plans. For another host, transfer a closed/consistent database backup and repository, stop the previous writer, then assign a new processor; this version does not coordinate two simultaneous database authorities. Import returned cloud reviews into the same database; automatic bidirectional database sync is not implemented.

## Trading behavior

The supplied policy deliberately leaves all setups off and `paper_policy_registered=false`. Numerical entry/stop/expiry/economic rules were not finalized during synthesis; code must not silently choose them. Register a reviewed paper policy before accepting candidates. Categories override individual setup switches. No monthly trade quota, fixed point stop or universal 2R is imposed.

The AI interprets context and structure. Code checks causal references, direction, structural-stop coverage, supported projection arithmetic, configured economics, expiry, freshness, processor generation, duplicate episodes and original plan state. Mechanical checks cannot establish semantic pattern quality, full correction ancestry or profitability. This is a smaller implemented interface, **not full implementation of proposed design schema 0.9.0**.

Paper stop entries are armed only after admission, never backfilled at the analysis cutoff. Subsequent one-minute OHLC drives events. Missing sequence or ambiguous stop/target ordering freezes the affected plan as `REVIEW_REQUIRED`; no favorable ordering is invented. Gap stops use the worse opening price. Intraminute admission/entry uncertainty is handled conservatively by excluding the admission-overlapping minute. Prices are underlying research points, not tradable index contracts or monetary P&L. Premise-exit/withdraw reviews are journaled recommendations, not automatically executed. Original stops/targets are not widened or replaced.

`events` exposes a durable notification journal; delivery to Telegram/email/etc., acknowledgement/retry and notification preferences remain to implement. The loop records events rather than making claims of live notification delivery.

## Design, reuse and verification

- [Implemented versus remaining](docs/implementation.md)
- [Upstox reuse audit](docs/upstox-reuse.md)
- [Consolidated design](docs/design/automatic-trading-technical-specification.md)
- [Deep session-example study](docs/design/project-synthesis/session-example-study.md)

```sh
pytest -q
```

Tests cover API encoding/authentication/retry, closed-bar causality, missing data, corrections, geometry, handover, duplicate decisions, paper gap/ambiguity handling and database backup. They do not establish a profitable edge. Book examples and previously inspected dates remain development material.
