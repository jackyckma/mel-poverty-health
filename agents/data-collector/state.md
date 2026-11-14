# State: data-collector

| Field | Value |
|-------|-------|
| Role docs last read | `team/process.md`, `team/roles/_base/data-collector.md`, `team/roles/data-collector.md`, `team/mandate.md`, `data/sources.yml`, `data/fetch_status.json` @ main f9113d7 (2026-11-14) |
| Last run (UTC) | 2026-11-14T07:40Z (scheduled) |
| Current assignments | `human-to-collector_002` (in-progress: CDC OK, Eurostat URL fixed, waiting on Owner re-run of `fetch.yml`); `human-to-collector_001` (in-progress) |
| Open items | Review the next manual Action fetch (Eurostat fixed URL, CDC with `locationname`). Owner decision on Fingertips size cap (London-only 3.4 MB vs 2 MB cap). Board `collector-to-lead_003`. |
| Known issues | Hosts data.cdc.gov, ec.europa.eu, fingertips.phe.org.uk reachable from Collector session as of 2026-11-14 (api.census.gov not retested). Census needs API key (Owner decision). Licences all unconfirmed. Houston food/housing insecurity blank in CDC PLACES (source gap). fetch.yml schedule still off: data only refreshes on manual runs. |
| Next planned actions | After the re-run: check `fetch_status.json` per source, inspect `data/raw/eurostat-hlth-silc-08/latest.json` (expect 138 values). Enable London-only Fingertips only if Owner raises the cap. Close 001/002 when fetching works. |
