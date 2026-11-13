---
from: human
to: collector
type: task
status: in-progress
priority: high
created: 2026-11-13T12:20:00Z
refs: [data/sources.yml, team/board/2026-11-13_lead-to-collector_001-endpoint-checks.md, team/board/2026-11-13_collector-to-lead_001-sources-added-disabled.md]
---

# Authorised: small, filtered fetch test (provisional enable)

The Owner (Jacky) authorised this on 2026-11-13 in the Lead chat. It answers the three options in the Collector's blocker message: this is option 2, with limits.

## What you may do

Set `enabled: true` provisionally, and only on **filtered** versions of these sources, so that one manual run of `fetch.yml` (GitHub Actions) can test the endpoints:

- `cdc-places-place-2025`: US scope is the four cities above 2 million population (New York, Los Angeles, Chicago, Houston), city proper. Use a SoQL filter on `locationname` and `stateabbr`, and `$select` only the identifiers plus a small set of poverty-adjacent and health measures (for example `diabetes_adjprev`, `depression_adjprev`, `access2_adjprev`, `foodinsecu_adjprev`, `housinsecu_adjprev`) with their 95% CI columns. Check the filter against the live dataset field names in the Lead message `lead-to-collector_001`.
- `eurostat-hlth-silc-08`: add dimension filters (a few countries, last few years, one reason, one age band, all income quintiles) so the response stays small. National level only.
- `ohid-fingertips-life-expectancy`: enable only after you have confirmed the area type for London boroughs. If you cannot confirm it, leave it disabled and say why.

## What you must not do

- Do not enable `census-acs1-2025-poverty-uninsured`. The Census API needs a key and `scripts/fetch.py` cannot use one. Keep it disabled. Note this on the board for the Owner.
- Do not enable `eurostat-urb-clivcon` (unchecked).
- Do not enable any source whose expected download is above about 2 MB. Keep it disabled and say why.
- Do not edit `.github/`, `scripts/`, or `framework/`. Do not turn on the `fetch.yml` schedule. Do not put a key or secret in `sources.yml`.

## Then

1. Update `data/sources.yml` (keep the example entry disabled) and push as usual.
2. Post a board `info` message to Lead listing, per source: final URL (with filters), enabled yes/no, expected size, and any reason it stays off.
3. The Owner runs `fetch.yml` manually. On your next run, review `data/fetch_status.json` and `data/raw/`, and report OK/FAIL per source on the board.

Licences are still unconfirmed. Nothing is published until Lead and Owner confirm them from each publisher's own page.
