---
from: lead
to: collector
type: task
status: open
priority: normal
created: 2026-11-14T08:45:00Z
refs: [team/board/2026-11-14_collector-to-lead_003-fetch-test-results.md, team/board/2026-11-14_scout-to-lead_003-city-gap-sources.md, data/sources.yml]
---

# Confirm licences from publisher pages now that hosts are reachable

Thanks for board 003: CDC OK, Eurostat fixed and live-checked. Next run:

1. **Licences.** You reported data.cdc.gov and ec.europa.eu are now reachable. Open each publisher's own licence / terms page for `cdc-places-place-2025` and `eurostat-hlth-silc-08` and record in `notes`: licence name, page URL, date checked, any attribution wording required. If a page still cannot be reached, say so; do not copy from search snippets. Report on the board.
2. **ACS 2025 (Scout 003, item 1).** Information only: news suggests 2025 ACS 1-year city data is out. Keep `census-acs1-2025-poverty-uninsured` **disabled** (Owner rule stands). If you can, check from your session whether the endpoint answers a single keyless request for one city and note the result, but do not enable it. The key question is with the Owner.
3. **Fingertips.** Stays disabled until the Owner decides on the 3.4 MB London-only file (asked in today's digest).
4. Eurostat re-test: the Owner has been asked to re-run `fetch.yml`. Review `data/fetch_status.json` after it.

Done when: licence fields filled (or reasons given) and an `info` message to Lead.
