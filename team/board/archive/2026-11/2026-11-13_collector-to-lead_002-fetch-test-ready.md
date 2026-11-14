---
from: collector
to: lead
type: info
status: done
priority: high
created: 2026-11-13T07:45:00Z
refs: [data/sources.yml, team/board/2026-11-13_human-to-collector_002-small-fetch-test.md, team/board/2026-11-13_lead-to-collector_001-endpoint-checks.md]
---

# Filtered fetch test ready: 2 sources provisionally enabled

Done per `human-to-collector_002`. Owner can now run `fetch.yml` manually once. Schedule not touched; no `.github/`, `scripts/` or `framework/` edits; no keys.

| id | Enabled | Final URL (filters) | Expected size | Note |
|---|---|---|---|---|
| `cdc-places-place-2025` | **yes (provisional)** | `https://data.cdc.gov/resource/vgc8-iyc4.csv?$select=stateabbr,placename,placefips,totalpopulation,diabetes_adjprev,diabetes_adj95ci,depression_adjprev,depression_adj95ci,access2_adjprev,access2_adj95ci,foodinsecu_adjprev,foodinsecu_adj95ci,housinsecu_adjprev,housinsecu_adj95ci&$where=placefips%20in(%270644000%27,%27644000%27,%273651000%27,%271714000%27,%274835000%27)&$limit=10` | 4 rows, under 5 KB | Filter is on `placefips` (the field the Lead confirmed), not `locationname`: in the place GIS-friendly table the name column is believed to be `placename`, and FIPS avoids name ambiguity. LA listed with and without leading zero. `placename`, `stateabbr`, `totalpopulation`, `*_adj95ci` are assumed names; if one is wrong Socrata returns HTTP 400 naming the column and I will fix it. |
| `eurostat-hlth-silc-08` | **yes (provisional)** | `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/hlth_silc_08?format=JSON&lang=EN&unit=PC&reason=TOOEFW&sex=T&age=Y_GE16&geo=DE&geo=ES&geo=FR&geo=IT&quantile=TOTAL&quantile=QU1&quantile=QU2&quantile=QU3&quantile=QU4&quantile=QU5&sinceTimePeriod=2020` | about 150 values, under 20 KB | National only. DE/ES/FR/IT = countries with EU cities above 2M (Berlin, Madrid, Paris, Rome). Reason TOOEFW = too expensive, too far or waiting list. Codes from Eurostat codelists, not checked live. |
| `ohid-fingertips-life-expectancy` | no | unchanged | n/a | Area type 502 for London boroughs could not be confirmed (fingertips.phe.org.uk refused by this session's proxy). Lead chat could check `https://fingertips.phe.org.uk/api/area_types` and tell me the id for current upper-tier LAs. |
| `census-acs1-2025-poverty-uninsured` | no | unchanged | n/a | **For Owner:** Census API needs a key; `fetch.py` cannot send one. Needs an Owner decision on key storage (Actions secret name only) and a script change by Lead/human. |
| `eurostat-urb-clivcon` | no | unchanged | n/a | Not checked; not authorised. |

The Collector session still cannot reach any of these hosts (proxy `connect_rejected`, checked 2026-11-13 run 3), so the test relies on the Action. After the Owner's manual run, my next run reviews `data/fetch_status.json` and `data/raw/` and reports OK/FAIL per source. Licences remain unconfirmed; nothing is published until Lead and Owner confirm them.
