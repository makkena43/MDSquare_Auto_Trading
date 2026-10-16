# Quant Investing reuse audit

Inspected the user-owned `MDsquare_Quant_Investing` project before implementing this adapter:

| Existing component | Reused/adapted concept | Deliberate change |
| --- | --- | --- |
| `src/main/python/service/intraday_data_fetcher.py` | Token-based authentication, candle array mapping and idempotent upserts | Preserve timezone, validate OHLC, no table drop on startup, SQLite local authority |
| `src/main/python/service/historical_data_fetcher.py` | Config reading, history normalization and persistence | Separate day/minute intervals, bounded V3 date chunks, no hardcoded daily label for minute data |
| `src/main/python/api/upstox_v3_client.py` | Bearer headers, bounded request timeout/retry | GET market-data only, no order methods/database-order side effects, no raw headers/body logging, no auth-error retry |

This is an adaptation of the useful components, not direct import of the old order-oriented class. The old project remains unchanged. Credentials are read at runtime from `UPSTOX_ACCESS_TOKEN` or an explicitly supplied legacy YAML path (`app.access_token`, falling back to `upstox.access_token`). No automatic login, refresh grant, broker orders or secret copying is introduced.

Verified against official Upstox V3 [intraday](https://upstox.com/developer/api-documentation/v3/get-intra-day-candle-data/) and [historical](https://upstox.com/developer/api-documentation/v3/get-historical-candle-data/) documentation on 16 October 2026. Instrument keys are URL-encoded. Fetch one-minute data for both indices and aggregate only complete five-minute windows; optional volume/OI fields are not used by price-action reasoning. Daily context remains a separate timeframe.

A real read-only connection check and backfill succeeded for both indices using the existing local configuration. Runtime data/exports are ignored by Git. Public repository publication, data redistribution and deployment are not automatic consequences of running ingestion.
