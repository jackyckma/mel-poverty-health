# State: data-collector

| Field | Value |
|-------|-------|
| Role docs last read | `team/process.md`, `team/roles/_base/data-collector.md`, `team/roles/data-collector.md`, `team/mandate.md`, `data/sources.yml`, `data/fetch_status.json` @ main 78fa02f (2026-11-13) |
| Last run (UTC) | 2026-11-13T07:30Z |
| Current assignments | none (no board messages to `collector`) |
| Open items | Waiting on Lead/Owner decision on Scout proposal `team/board/2026-11-13_scout-to-lead_001-candidate-sources.md` (7 candidate sources); once approved, propose `data/sources.yml` entries to Lead |
| Known issues | `data/sources.yml` has only the disabled example entry; `data/fetch_status.json` is empty (`updated_at: null`); `fetch.yml` schedule is still commented out (disabled). Scout reports that routine sessions cannot reach data hosts (`..._002-network-reach.md`), so all fetching must run in Actions |
| Next planned actions | Daily: check sources.yml / fetch_status.json / data/raw for Action results. When sources are approved: draft sources.yml entries (ACS S1701/S2701, CDC PLACES vgc8-iyc4, Eurostat urb_*, Fingertips) with each source's update frequency, and check the first Action fetch |
