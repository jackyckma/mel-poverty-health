# State: data-collector

| Field | Value |
|-------|-------|
| Role docs last read | `team/process.md`, `team/roles/_base/data-collector.md`, `team/roles/data-collector.md`, `team/mandate.md`, `data/sources.yml`, `data/fetch_status.json` @ main be2ef51 (2026-11-13) |
| Last run (UTC) | 2026-11-13T11:21Z |
| Current assignments | `team/board/2026-11-13_human-to-collector_001-add-approved-sources.md` (in-progress: entries added, enabling blocked) |
| Open items | Waiting on Lead/Owner answer to `team/board/2026-11-13_collector-to-lead_001-sources-added-disabled.md` (blocker): confirm licences/endpoints or authorise a provisional enable + manual fetch test |
| Known issues | Collector session cannot reach data.cdc.gov, api.census.gov, ec.europa.eu, fingertips.phe.org.uk (curl 000, WebFetch DNS fail). All 5 mandate sources `enabled: false`. `fetch_status.json` empty; `data/raw/` empty; `fetch.yml` schedule disabled (Owner decides). Fingertips indicator/area ids and ACS variable codes are unverified guesses. PLACES needs a city filter before enabling (size). |
| Next planned actions | On Lead/Owner reply: set `enabled: true` for confirmed sources (S2, S4 first), review the first manual Action fetch in `fetch_status.json` / `data/raw/`, fix endpoint ids from the Action error messages. Close human-to-collector 001 when sources are fetching. Agree PLACES city filter with Curator. |
