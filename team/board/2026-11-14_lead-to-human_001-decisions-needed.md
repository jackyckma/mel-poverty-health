---
from: lead
to: human
type: needs-human
status: open
priority: high
created: 2026-11-14T08:45:00Z
refs: [agents/mel-lead/outputs/2026-11-14_digest.md, team/board/2026-11-14_collector-to-lead_003-fetch-test-results.md, team/board/2026-11-14_curator-to-lead_001-transform-hook-proposal.md, team/board/2026-11-14_scout-to-lead_003-city-gap-sources.md]
---

# Owner decisions needed (2026-11-14)

Details and context in `agents/mel-lead/outputs/2026-11-14_digest.md`.

1. **Re-run `fetch.yml` manually** (Actions → fetch → Run workflow) to test the fixed Eurostat URL and new CDC column. Without it the dashboard goes `stale` after 2026-11-15 12:41 UTC.
2. **Fingertips size cap:** allow the London-only file (3.4 MB) or keep it off?
3. **Census ACS key:** decide how to handle it (Actions secret + script change, or keep disabled). 2025 city poverty data appears to be out; this is the main missing poverty-side source.
4. **Scout city sources C1–C5:** approve any? C3 (Berlin) and C4 (Paris) are not in English.
5. **Mandate defaults:** confirm city definition and out-of-scope list in `team/mandate.md` (still marked proposed).
6. **`fetch.yml` schedule:** keep off for now (Lead recommends: yes, keep off until Eurostat re-test and licences are checked).

---
**Lead update 2026-11-15:** No Owner reply yet; all six items still open. Changes since yesterday:

- **New item 0 (do before item 1):** apply the Curator's hook patch, then re-run `fetch.yml`, so one run tests everything. From the repo root: `patch -p0 < agents/data-curator/outputs/2026-11-15_hook-patch/scripts.diff` and `patch -p0 < agents/data-curator/outputs/2026-11-15_hook-patch/docs.diff`. README in the same folder. Dry run is clean against main.
- **Item 1:** the dashboard is now `stale` (passed 2026-11-15 12:41 UTC). This is correct, honest behaviour.
- **Item 3:** the Collector confirmed a keyless ACS request is redirected to `missing_key.html`. Option (b) "keyless first" is ruled out. Choices are now: key as an Actions secret plus a small `fetch.py` change, or keep it off.
- **Item 6:** licences for CDC PLACES (Public Domain) and Eurostat (free reuse, source acknowledged) are now confirmed from publisher pages. Lead still recommends keeping the schedule off until the Action re-run passes.
- **New item 7 (low priority):** Scout sources C6–C9 (homelessness mortality, rough sleeping, food insecurity). See `team/board/2026-11-15_scout-to-lead_004-homelessness-food-sources.md`.
