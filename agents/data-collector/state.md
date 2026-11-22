# State: data-collector

| Field | Value |
|-------|-------|
| Role docs last read | `team/process.md`, `team/roles/_base/data-collector.md`, `team/roles/data-collector.md`, `team/mandate.md`, `data/sources.yml`, `data/fetch_status.json` @ main 689d1c6 (2026-11-22) |
| Last run (UTC) | 2026-11-22T07:30Z (scheduled) |
| Current assignments | `human-to-collector_002` (in-progress: waiting on Owner re-run of `fetch.yml`); `human-to-collector_001` (in-progress). `lead-to-collector_004` done. |
| Open items | Review the next manual Action fetch (Eurostat fixed URL, CDC with `locationname`). Owner decisions: Fingertips size cap, Census key. Board `collector-to-lead_003`, `_005`, `_006` (blocker). |
| Known issues | No Action fetch since 2026-11-13 12:41 UTC (only fetch.yml run is run 1, checked 2026-11-22); dashboard stale since 2026-11-15 12:41 UTC; raised as blocker 006. Census API still needs a key (302 to missing_key, 2026-11-15). Licences confirmed for CDC PLACES (Public Domain) and Eurostat hlth_silc_08 (Eurostat reuse, source acknowledged); others unconfirmed. Houston food/housing insecurity blank in CDC PLACES (source gap). fetch.yml schedule off. data.cdc.gov sometimes resets connections from the session (retry worked). |
| Next planned actions | After the re-run: check `fetch_status.json` per source, inspect `data/raw/eurostat-hlth-silc-08/latest.json` (expect 138 values). If still no re-run, do not re-post; note it in the run log and keep blocker 006 open. Enable Fingertips only if the Owner raises the cap. Close 001/002 when fetching works. |
