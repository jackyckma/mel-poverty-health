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
