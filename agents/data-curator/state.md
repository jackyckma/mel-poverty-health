# State: data-curator

| Field | Value |
|-------|-------|
| Role docs last read | `team/process.md`, `team/roles/_base/data-curator.md`, `team/roles/_base/dashboard-analyst.md`, `team/roles/data-curator.md`, `team/mandate.md` (main @ f7d71a0, 2026-11-15) |
| Last run (UTC) | 2026-11-18T08:30Z (no-op: no new Action output; patch still dry-runs clean on main @ 1327cb3) |
| Current assignments | none open; delivered `2026-11-14_lead-to-curator_001-hook-patch-yes.md` (done); own info `2026-11-15_curator-to-lead_002-hook-patch-ready.md` awaiting Owner apply + `fetch.yml` run |
| Open items | Owner applies `outputs/2026-11-15_hook-patch/` then runs `fetch.yml`; city list (`cities.csv`) waits for a primary population source with year; News signals section not wired |
| Known issues | Live `scripts/` still generic until patch applied (payload blob; DictWriter crash trap if a hook is added alone); dashboard stale since 2026-11-15 12:41 UTC, raw now 5 days old (cron off; Collector blocker 006 tracks it); Eurostat never collected; JSON-stat flattener tested on synthetic fixture only; Houston food/housing insecurity blank in source; PLACES measure labels unchecked against data dictionary |
| Next planned actions | After the next Action run: verify Eurostat rows (dimension codes, ~138 values, gaps), `locationname`, `all_rows.csv` header, dashboard sections; compare Action CDC output to curated CSV and retire the curated copy if identical; first internal insight on income-quintile unmet need (national context only) once real Eurostat data lands |
