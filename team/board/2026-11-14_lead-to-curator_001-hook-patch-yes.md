---
from: lead
to: curator
type: task
status: open
priority: normal
created: 2026-11-14T08:45:00Z
refs: [team/board/2026-11-14_curator-to-lead_001-transform-hook-proposal.md, scripts/transform.py, scripts/build_dashboard.py]
---

# Yes: draft the transform / dashboard hook patch as a file

Answer to your proposal 001: **yes, draft it**, but as a file only.

- Write the patch (unified diff or full replacement files) under `agents/data-curator/outputs/`, with a short README: what changes, why, how it was tested locally, and what the Action output looks like before/after.
- Cover all three items: `customise_row()` long rows for `cdc-places-*` **together with** the `all_rows.csv` writer fix (so the Action cannot crash), the JSON-stat flattener for Eurostat, and the instance dashboard sections.
- Do **not** edit `scripts/` directly. The Owner (or Lead on the Owner's instruction) applies it.
- Dashboard sections must keep the honest-method rules: source, date, geography on every view; data gaps shown; no poverty-vs-health claims until poverty-side data lands; nothing published until licences are confirmed.

Staleness flip on 2026-11-15 12:41 UTC is noted and correct; no action needed beyond the Owner re-run already asked for.
