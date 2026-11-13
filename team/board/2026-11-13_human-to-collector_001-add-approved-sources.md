---
from: human
to: collector
type: task
status: in-progress
priority: normal
created: 2026-11-13T11:05:00Z
refs: [team/board/2026-11-13_scout-to-lead_001-candidate-sources.md, team/board/2026-11-13_human-to-lead_001-sources-approved.md]
---

# Add the approved sources to `data/sources.yml`

The Owner approved all 7 Scout candidates (see the human-to-lead decision message). On your next run:

- Add entries for S1 to S5 to `data/sources.yml` using the schema in that file (id, name, url, format, enabled, notes). Scout's full table with URLs is in `agents/scout/outputs/2026-11-13_signals.md`, section A.
- Set `enabled: true` only for endpoints that return JSON or CSV the Actions fetcher can use. Confirm licence and endpoint from the primary page. If you cannot confirm, leave `enabled: false` and say why in `notes` and on the board.
- S6 and S7 are narrative references: record them in `notes` or on the board, not as fetch entries, unless a CSV or JSON exists.
- Keep the example entry disabled. Do not edit `.github/`; do not enable the `fetch.yml` schedule (Owner decides later).
- Post a board `info` message to Lead listing each source, its status, licence, and update frequency.
