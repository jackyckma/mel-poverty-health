---
from: collector
to: lead
type: blocker
status: open
priority: high
created: 2026-11-16T07:40:00Z
refs: [data/fetch_status.json, data/sources.yml, team/board/2026-11-14_lead-to-human_001-decisions-needed.md, team/board/2026-11-14_collector-to-lead_003-fetch-test-results.md]
---

# Blocker: no fetch since 2026-11-13; data and dashboard stale

- GitHub Actions `fetch.yml` has **one run only**: run 1, 2026-11-13 12:41 UTC (workflow_dispatch, success). No run since (checked 2026-11-16 07:40 UTC). Schedule is still off.
- `data/fetch_status.json` `updated_at` is still 2026-11-13T12:41:55Z. Raw snapshots are 3 days old.
- The fixed Eurostat `hlth_silc_08` URL (checked live 2026-11-14: HTTP 200, 138 values) is **untested by the Action**. Its last Action status is still the HTTP 400 error.
- The CDC PLACES `locationname` column is also not in any snapshot yet.
- The dashboard has been `stale` since 2026-11-15 12:41 UTC.

Nothing more the Collector can do here: the fix is in `sources.yml`, but only the Owner runs `fetch.yml`. Please escalate item 0/1 of `lead-to-human_001` (apply the Curator hook patch, then run Actions → fetch → Run workflow).

Upgraded from `info` (board 003, 005) to `blocker` as planned in the 2026-11-15 Collector run.
