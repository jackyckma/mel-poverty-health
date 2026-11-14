---
from: collector
to: lead
type: info
status: in-progress
priority: high
created: 2026-11-14T07:40:00Z
refs: [data/sources.yml, data/fetch_status.json, data/raw/cdc-places-place-2025/latest.csv, team/board/2026-11-13_human-to-collector_002-small-fetch-test.md, team/board/2026-11-13_lead-to-collector_003-eurostat-url-fix.md, team/board/2026-11-13_lead-to-collector_002-fingertips-area-type.md]
---

# Fetch test results (Action run 2026-11-13 12:41 UTC) and fixes

New today: data.cdc.gov, ec.europa.eu and fingertips.phe.org.uk **are reachable** from the Collector session (they were refused yesterday), so the fixes below were checked live.

| Source | Action result | Today |
|--------|---------------|-------|
| `cdc-places-place-2025` | **OK**. 4 rows (LA, Chicago, NYC, Houston), 794 bytes, all 14 selected columns present. | Added `locationname` to `$select` (Lead suggestion). Checked live: returns "New York" etc. Data gap: Houston `foodinsecu_*` and `housinsecu_*` are blank in the source (not a fetch error). |
| `eurostat-hlth-silc-08` | **FAIL**. HTTP 400 (wrong codes `quantile`, `TOOEFW`). | Applied the corrected URL from lead-to-collector 003. Checked live: HTTP 200, 138 values, 4.9 KB, dataset updated 2026-10-20. Notes say country level. Still enabled. |
| `ohid-fingertips-life-expectancy` | disabled | **Stays disabled: too big.** England-wide is 14.3 MB (89,565 rows). London-only variant (`&parent_area_type_id=6&parent_area_code=E12000007`) is 3.4 MB (20,341 rows, 33 London areas). Both are above the 2 MB cap in human-to-collector 002. Most rows are deprivation-decile breakdowns within each area, which fit the topic. |
| `census-acs1-2025-poverty-uninsured`, `eurostat-urb-clivcon` | disabled | No change (key needed; not authorised). |

## Asks

1. **Owner:** please re-run `fetch.yml` manually so the fixed Eurostat URL and the new CDC column are tested by the Action.
2. **Owner decision:** raise the size cap for the London-only Fingertips file (3.4 MB) or keep it off. I will not enable it without that.

Licences are still unconfirmed; now that hosts are reachable, Lead or Scout can check the publisher pages.
