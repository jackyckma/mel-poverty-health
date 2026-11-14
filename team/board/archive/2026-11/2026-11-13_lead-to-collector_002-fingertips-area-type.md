---
from: lead
to: collector
type: info
status: done
priority: normal
created: 2026-11-13T12:50:00Z
refs: [data/sources.yml, team/board/2026-11-13_collector-to-lead_002-fetch-test-ready.md]
---

# Fingertips area type 502 confirmed

Checked from the Lead chat on 2026-11-13 against `https://fingertips.phe.org.uk/api/area_types`: area type **502** is "Upper tier local authorities (post 4/23)" (short name "Counties & UAs (from Apr 2023)"). Indicator 90366 (life expectancy at birth, ONS) was confirmed earlier.

This is England-wide, not London only. Filtering to London boroughs happens after the fetch (Curator), not in the URL. The response size is unchecked; expect well under 2 MB, but verify the downloaded file size after the first run.

Decision for this round: leave `ohid-fingertips-life-expectancy` disabled until the Owner's first manual `fetch.yml` run on CDC PLACES and Eurostat has been reviewed. You may then enable it provisionally (the confirmation condition in `human-to-collector_002` is now met) and report its size.

Note for readable output: in the CDC PLACES table `placename` holds the place code and the city name is in `locationname`. Consider adding `locationname` to the `$select` when you next edit that URL.

Not verified from the Lead chat: the filtered CDC PLACES and filtered Eurostat URLs (the fetch tool refused the first; the second returned the earlier unfiltered page). The Actions run is the real test.
