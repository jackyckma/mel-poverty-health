---
from: human
to: lead
type: info
status: open
priority: normal
created: 2026-11-13T11:05:00Z
refs: [team/board/2026-11-13_scout-to-lead_001-candidate-sources.md, team/board/2026-11-13_scout-to-lead_002-network-reach.md]
---

# Owner decisions: sources and network policy

Owner (Jacky) decided on 2026-11-13, in the Lead chat:

1. **Sources:** approve all 7 candidate sources from Scout message 001 (S1 to S7). This is a demo instance, so take them all. Collector adds them to `data/sources.yml`.
   - Keep S5 (Eurostat `hlth_silc_08`) labelled as a national context layer.
   - S6 (London Health Profile, mostly PDF) and S7 (Measure of America LA County, one-off) are narrative references unless a machine-readable file exists. Do not force a fetch entry for them.
   - Licences came from search snippets and are unverified: Collector confirms each licence from the primary page and records it in the source `notes`. Flag any source whose terms do not allow reuse and leave it `enabled: false`.
2. **Network policy:** option (b). Do **not** widen the routine network allowlist. Scout works from search. Collector and the Actions `fetch.yml` check and fetch the endpoints.

Open for the Owner later: whether to enable the `fetch.yml` schedule. Lead: ask the Owner in the digest once the Collector has added the entries and a manual test fetch has been checked.

Lead: route to Collector and Scout, and close Scout messages 001 and 002 when done.
