---
from: scout
to: lead
type: info
status: done
priority: normal
created: 2026-11-13T07:00:00Z
refs: []
---

# Scout can search the web but cannot reach data hosts from its session

On 2026-11-13 the routine's egress proxy refused shell connections (`curl`) to data.cdc.gov, api.census.gov,
ec.europa.eu, fingertips.phe.org.uk, countyhealthrankings.org and cityhealthdashboard.com (CONNECT 403).
WebFetch also failed (DNS) for census.gov and the news sites. Only WebSearch worked, so Scout signals are based on
search snippets and are not checked against primary pages.

Impact: Scout cannot check endpoints or licences directly. This matches the base doc's expectation; mechanical fetch should run in
GitHub Actions (`fetch.yml`).
Options for the Owner: (a) allow these domains in the routine environment's network policy, or (b) accept that Scout runs on
search only and that Collector/Actions check endpoints. Possible `needs-human` item if (a) is wanted.
