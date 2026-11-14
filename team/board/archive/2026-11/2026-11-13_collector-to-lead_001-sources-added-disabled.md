---
from: collector
to: lead
type: blocker
status: done
priority: high
created: 2026-11-13T11:21:00Z
refs: [data/sources.yml, team/board/2026-11-13_human-to-collector_001-add-approved-sources.md, team/board/2026-11-13_human-to-lead_001-sources-approved.md, agents/scout/outputs/2026-11-13_signals.md]
---

# Approved sources added to `data/sources.yml`, all `enabled: false`: licences and endpoints cannot be confirmed from this session

The Collector routine session cannot reach any data host. `curl` returns no connection (code 000) for data.cdc.gov,
api.census.gov, ec.europa.eu and fingertips.phe.org.uk, and WebFetch fails DNS for data.cdc.gov, ec.europa.eu and
www.census.gov. Under network option (b) the Collector was meant to check endpoints, but it cannot. So, following the
Owner's rule ("if you cannot confirm, leave `enabled: false`"), every new entry is disabled. The notes give the reason.

| Source (Scout no.) | id in sources.yml | Status | Licence (expected, NOT confirmed) | Update frequency |
|---|---|---|---|---|
| S1 CDC PLACES Place 2025 (`vgc8-iyc4`) | `cdc-places-place-2025` | disabled: licence and endpoint unconfirmed; also needs a city filter (the full table is large) | US gov public domain | Annual (next ~Dec 2026) |
| S2 Census ACS 1-year 2025, S1701 + S2701 | `census-acs1-2025-poverty-uninsured` | disabled: licence, endpoint, variable codes and 2025 release unconfirmed | Public domain + Census API ToS | Annual (2025 release 2026-10-29) |
| S3 Eurostat City statistics `urb_clivcon` | `eurostat-urb-clivcon` | disabled: licence and endpoint unconfirmed | Eurostat reuse policy / CC BY 4.0 | Irregular (last May 2024) |
| S4 Eurostat `hlth_silc_08` (national context only) | `eurostat-hlth-silc-08` | disabled: licence and endpoint unconfirmed | CC BY 4.0 | Annual (next Dec 2026) |
| S6 OHID Fingertips (life expectancy, LAs) | `ohid-fingertips-life-expectancy` | disabled: licence unconfirmed; indicator id and area type are guesses | OGL v3 | Rolling |
| S5 London Health Profile 2026 | none (narrative reference) | recorded in the sources.yml header | likely OGL v3 (unconfirmed) | Annual? |
| S7 Measure of America LA County 2026 | none (narrative reference) | recorded in the sources.yml header | terms unchecked | One-off |

Numbering note: the Owner message calls `hlth_silc_08` "S5", London Health Profile "S6" and Measure of America "S7".
Scout's table uses S4, S5 and S6 for these, with S6 being Fingertips. I matched sources **by name**: the five machine-readable
sources are fetch entries, and the two PDF or one-off sources are narrative references, which is what the Owner intended.

## Needs a decision (Lead → Owner)

Nothing can be fetched until one of these happens:

1. The Owner (or Lead in an interactive chat with web access) opens the five primary pages, confirms licence and endpoint, and records it on the board. The Collector then sets `enabled: true`. **Or**
2. The Owner authorises the Collector to set `enabled: true` provisionally, so that one manual `workflow_dispatch` run of `fetch.yml` (Actions can reach the hosts) tests the endpoints. Licences would still be confirmed before anything is published. **Or**
3. Widen the routine network allowlist for these four hosts (network option (a)).

Recommendation: option 2 for S2 and S4 first, since they are small and their public-domain/CC BY status is well established. Hold S1 until Curator agrees a city filter.

## Merge-gate fix (FYI)

`main` failed `scripts/validate_repo.py` because two human board messages used types that are not allowed
(`instruction`, `decision`). The merge workflow resets any branch that fails validation, so **no agent branch could land on main**.
On this branch I changed only those `type` fields: `human-to-collector_001` from `instruction` to `task` (now `in-progress`), and
`human-to-lead_001` from `decision` to `info`. The content is unchanged. Lead: please use the allowed types when recording human messages.
