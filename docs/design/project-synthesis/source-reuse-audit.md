# Source component reuse audit

Static inspection of `/Users/makkenasrinivas/PycharmProjects/MDsquare_Quant_Investing/`, preserved from specification v1.9. These findings identify concepts to reuse and defects to repair; runtime behavior has not been verified. Order-related components apply only to a later execution phase.

## 4. Reuse matrix and mandatory remediation

Paths in this table are relative to the inspected source root.

| Source and evidence | Useful component | Decision / required changes |
|---|---|---|
| `src/main/python/websocket/marketdata/WebSocketDataFetcher.py:58–184` | Authorize, subscribe, decode, normalize, yield separation | Adapt control flow; replace with current V3 authorization and official V3 protobuf; retain TLS verification; separate index and option decoders; add lifecycle, timestamps, recovery and completion semantics |
| Same file `:20–22` | Configurable TLS | Remove production ability to disable certificate/hostname verification |
| Same file `:191–195` | Example entry point | Rewrite: instance method is invoked without an instance and an async generator is passed to `asyncio.run` |
| `src/main/python/strategy/WebSocketEnhancer.py:40–160` | Subscription union, latest-data cache, reconnect idea | Reimplement; V2 URL, JSON decoding and receive-time timestamps are not a valid current feed adapter |
| `src/main/python/service/HistoricalDataFetcher.py` and `historical_data_fetcher.py:102–204` | OHLC normalization and historical warm-up/upsert concepts | Consolidate duplicate classes; validate current endpoint/SDK; preserve actual interval and timezone; handle optional OI and variable candle lengths. Lowercase formatter hardcodes `1day` despite configurable interval |
| `src/main/python/service/intraday_data_fetcher.py:47–75,82–181` | Intraday REST recovery and deduplication | Extract parsing/upsert only. Constructor setup drops `intraday_data`; replace with migrations and non-destructive persistence. Parse timestamps with timezone rather than stripping the offset |
| `src/main/python/process/DataFetcher.py:35–80` | Five-minute OHLC aggregation formula | Rewrite engine: resampling does not group by instrument, so combined histories can mix indices; no completeness/session gating; missing legacy imports |
| `src/main/python/service/option_chain_fetcher.py:30–124` | Contract discovery and metadata persistence | Rename to contract catalog. It calls `get_option_contracts` and stores metadata, not live chain prices/Greeks. Add lot size/tick size and separate chain snapshots |
| `src/main/python/service/OptionStrategyEvaluator.py` | Expiry lookup and ATM/ITM/OTM grouping concepts | Adapt as contract-selection helper after audit; not evidence of a Brooks entry model or complete execution system |
| `src/main/python/alerts/price_alerts.py:17–91` | Threshold direction, expiry, cooldown metadata | Extract pure evaluation concepts; in-memory state and 3600-second default cooldown are unsuitable defaults for durable intraday alerts. Add persistent outbox and notification transport |
| `src/main/python/api/upstox_v3_client.py:218–282` | HTTP request wrapper outline | Rewrite mutation handling: retries are method-agnostic; a timed-out POST may have already placed an order. Full prepared headers are logged at line 239, including Authorization |
| Same file `:318–340,462–489,496–530` | Order interfaces | Reject live reuse: order book is mocked empty; cancellation is mocked successful; order details are mocked complete. These responses cannot drive position state |
| Same file `:32–80,418–453` | Config and DB coupling | Replace constructor DDL and `db_conn=None` dereference; validate endpoint per operation rather than one versioned base URL. Paper is the new default; old sandbox default is false |
| `src/main/python/login/upstox_login_automated.py:24–118` | OAuth callback and token-exchange sequence | Adapt flow only: remove auth-code/passcode logging, YAML token writes and all-interface callback binding. Implement state validation, bounded callback lifetime and supported user login |
| `src/main/python/login/upstox_auth.py:67` | Alternate auth helper | Do not reuse: static AST parse fails with mismatched bracket; URL text appears malformed |
| `src/main/python/utils/config_loader.py` | YAML loading | Replace with typed settings, explicit config location and secret-provider references; fail clearly instead of returning empty config |
| `src/main/python/backtesting/HistoricalDataStreamer.py`; `models/backtesting_engine.py` | Replay/reporting concepts | Audit/extract only. New event-time replay must share live strategy interfaces and model actual option fills; no claim that portfolio backtest is an options simulator |
| `src/main/python/strategy/*.py~` | Archived price-action research | Reference only; restoring backup files wholesale is prohibited. Evaluate individually for look-ahead, fabricated instruments, expiry assumptions and dependencies |
| `requirements.txt:1–5` | pandas/Postgres ecosystem | Create pinned dependency/lock files. Existing root list omits feed/runtime imports including Upstox SDK, websockets, protobuf, PyYAML, pytz and requests |

Reused files must have provenance records (source path, SHA-256, extraction date, changes, licence/ownership confirmation) and characterization fixtures before integration. Do not copy `.venv`, logs, database dumps, tokens, application YAML, model weights or backups into Git.

