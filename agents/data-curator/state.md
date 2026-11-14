# State: data-curator

| Field | Value |
|-------|-------|
| Role docs last read | `team/process.md`, `team/roles/_base/data-curator.md`, `team/roles/_base/dashboard-analyst.md`, `team/roles/data-curator.md`, `team/mandate.md` (main @ 6f6f7de, 2026-11-14) |
| Last run (UTC) | 2026-11-14T08:45Z |
| Current assignments | none addressed to `curator`; own proposal `2026-11-14_curator-to-lead_001-transform-hook-proposal.md` awaiting Lead |
| Open items | Lead decision on transform/dashboard hook patch; city list (`cities.csv`) waits for a primary population source with year; dashboard sections still placeholder |
| Known issues | Generic transform (JSON `payload` blob); `all_rows.csv` DictWriter raises on extra keys; Eurostat JSON-stat not flattened; `fetch.yml` cron off, so dashboard turns stale after 2026-11-15 12:41 UTC without a manual run; Houston food/housing insecurity missing in source; CDC PLACES licence unconfirmed |
| Next planned actions | After the next Action run: check `locationname` arrived, review Eurostat output; rebuild `data/processed/curated/us_cities_cdc_places_2025.csv` only if the raw snapshot changed; draft hook patch if Lead agrees; verify PLACES measure labels and the HRSN-module reason for Houston gaps |
