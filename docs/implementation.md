# Implementation checkpoint: v0.1.0

The first data-to-review-to-paper-event vertical slice is implemented. Design documents are requirements, not a claim that every section is executable.

## Working

- Read-only Upstox V3 historical/current-session data and existing Quant Investing credential compatibility.
- One-minute persistence, complete five-minute aggregation, rolling 30-calendar-day context and separate daily history.
- SQLite authoritative paper state, immutable jobs/reviews, correction events and generation-based provider handover.
- Portable JSON context for any assistant that can read the repository skill; returned reviews are ingested into the same local journal.
- Basic structural/directional/anchor/economic checks and explicit disabled/unregistered policy behavior.
- Prospective simulated entries, original protective levels, worse-price gap stops and ambiguity/missing-data review states.
- Durable events exposed through the command line and consistent database backup for host transfer.

## Still required

The deep economics/geometry synthesis was interrupted and remains partial; existing source guidance is available, not independently validated. No calibrated model probability or proven index profitability is supplied. A fully registered operational policy, automated semantic pattern/context evaluation, parent-ancestry adjudication, real model transport, notification delivery, authoritative exchange calendar, automatic synchronization, cross-host single-writer enforcement, correction reconciliation and human review resolution remain necessary before unattended paper operation. Premise exit/withdraw recommendations are journaled but not executed automatically. The complete proposed schema and its richer lifecycle have not been implemented.

No orders, options, live positions, contract sizing, API-key purchase or broker write endpoints exist. This implementation does not use the old project's order code or modify its database. Broader mirrored design/evaluation references are development material and are never included automatically in a live model prompt; answer keys must be excluded from independent evaluations.

## Verification

Offline tests run without secrets or broker calls. A separate explicitly performed read-only smoke check fetched today's 375 one-minute bars for each index. Backfill returned 7,875 prior one-minute bars and 62 daily bars per index; combined with today, the local database holds 8,250 one-minute and 62 daily bars per index. Counts describe this fetch, not guaranteed future coverage or strategy results. No long-running daemon or cloud deployment was started.

Default compact model context retains 150 five-minute bars and up to 60 daily bars; the full rolling history remains in SQLite and can be exported by a specific time slice. This avoids repeatedly sending the entire archive to a model. These display limits do not certify sufficient historical context for every setup.
