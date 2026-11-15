---
from: collector
to: lead
type: info
status: done
priority: normal
created: 2026-11-15T07:40:00Z
refs: [team/board/2026-11-14_lead-to-collector_004-licences-and-acs.md, data/sources.yml, data/fetch_status.json]
---

# Licences checked from publisher pages; no new Action fetch yet

Answer to lead-to-collector 004. Recorded in `data/sources.yml` notes.

| Source | Licence | Page (checked 2026-11-15) | Attribution / conditions |
|--------|---------|---------------------------|--------------------------|
| `cdc-places-place-2025` | **Public Domain** | Dataset metadata `https://data.cdc.gov/api/views/vgc8-iyc4.json` (`license: PUBLIC_DOMAIN`) | Metadata attribution: "Centers for Disease Control and Prevention, National Center for Chronic Disease Prevention and Health Promotion, Division of Population Health". No mandatory wording; cite this plus dataset id. |
| `eurostat-hlth-silc-08` | Eurostat reuse policy (free reuse with source acknowledged; site content CC BY 4.0) | `https://ec.europa.eu/eurostat/web/main/help/copyright-notice` | Acknowledge "Source: Eurostat"; state clearly if data are modified; include a disclaimer that Eurostat is not responsible for the modified output. |

Licence checks came from the publisher pages, not from search snippets. The Lead and Owner still decide whether to publish.

**ACS (item 2):** a keyless request for NYC (`2025/acs/acs1/subject`, place 51000, state 36) gives a 302 redirect to `missing_key.html`. So the endpoint still needs a key. The source stays disabled.

**Fetch status (item 4):** `data/fetch_status.json` is unchanged since **2026-11-13 12:41 UTC**. No Action re-run has happened, so the fixed Eurostat URL and the CDC `locationname` column are still untested by the Action. Per the 11-14 digest, the dashboard goes stale after 2026-11-15 12:41 UTC. Owner re-run of `fetch.yml` is still needed.
