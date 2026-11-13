# State: data-collector

| Field | Value |
|-------|-------|
| Role docs last read | `team/process.md`, `team/roles/_base/data-collector.md`, `team/roles/data-collector.md`, `team/mandate.md`, `data/sources.yml`, `data/fetch_status.json` @ main fb9924f (2026-11-13) |
| Last run (UTC) | 2026-11-13T07:45Z (scheduled) |
| Current assignments | `team/board/2026-11-13_human-to-collector_002-small-fetch-test.md` (in-progress: filters set, 2 sources enabled, waiting on Owner manual `fetch.yml` run); `human-to-collector_001` (in-progress) |
| Open items | Review first manual Action fetch and report OK/FAIL per source on the board (`collector-to-lead_002` lists the URLs). Fingertips area type id for London boroughs (asked Lead to check). |
| Known issues | Collector session proxy rejects data.cdc.gov, ec.europa.eu, fingertips.phe.org.uk, api.census.gov. `fetch_status.json` empty; `data/raw/` empty. CDC PLACES column names other than `placefips` and `*_adjprev` assumed, unverified. Eurostat dimension codes unverified live. Census needs API key (Owner decision). Licences all unconfirmed. |
| Next planned actions | After the manual run: check `fetch_status.json` last_error per source, inspect `data/raw/<id>/latest.*` (row count, columns, size), fix filter/column errors from Action messages, board OK/FAIL report. Enable Fingertips once Lead confirms area type. Close 001/002 when fetching works. |
