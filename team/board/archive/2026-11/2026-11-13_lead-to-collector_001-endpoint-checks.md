---
from: lead
to: collector
type: info
status: done
priority: normal
created: 2026-11-13T12:10:00Z
refs: [data/sources.yml, team/board/2026-11-13_collector-to-lead_001-sources-added-disabled.md]
---

# Endpoint checks done from the Lead chat (which has web access)

Checked on 2026-11-13 by fetching the URLs. Licences were NOT read from primary pages yet; they remain unconfirmed.

| id in sources.yml | Result |
|---|---|
| `cdc-places-place-2025` | Endpoint works (`vgc8-iyc4`, JSON returned). One row per US place, with measure columns such as `diabetes_crudeprev` and `diabetes_adjprev`, plus 95% CI columns and `placefips`. Needs a city filter before enabling. |
| `census-acs1-2025-poverty-uninsured` | Request returned **Missing Key**: the Census API requires a free API key. The source note saying no key is needed is wrong. Key storage (GitHub Actions secret name only) needs an Owner decision. Variable codes still unverified. |
| `eurostat-hlth-silc-08` | Endpoint works (JSON-stat, last updated 2026-10-20 per the response). The unfiltered response is very large (hundreds of thousands of characters), so add dimension filters before fetching. National level only. |
| `ohid-fingertips-life-expectancy` | Indicator 90366 exists: life expectancy at birth, source ONS. Area type 502 and the deprivation breakdown are still unverified. |
| `eurostat-urb-clivcon` | Not checked yet. |

No change to `enabled` flags is requested yet. Wait for the Owner's decision on how to proceed (provisional enable plus one manual `fetch.yml` run, or confirm licences first).
