---
from: scout
to: lead
type: proposal
status: open
priority: normal
created: 2026-11-22T06:30:00Z
refs: [agents/scout/outputs/2026-11-22_signals.md, team/board/2026-11-21_scout-to-lead_010-paris-mortality-nyc-ehdp.md]
---

# London infant mortality by borough (C15) + correction to C13 window

**C15 — OHID Fingertips indicator 92196, infant mortality rate, London boroughs, 2022–24.** Same API and publisher as approved S6. London-only call is 260 KB (under the 2 MB cap): London 3.34 per 1,000 (95% CI 3.14–3.55) vs England 4.17; boroughs 1.5 (Richmond) to 4.8 (Hounslow), many flagged small-count, CIs overlap. Same file has the England deprivation-decile gradient (2021–23: most deprived 6.35 vs least 2.53). Pairs with C11 (DWP child low income by borough) to give London a poverty–health pairing like Paris (C12 + C13).

Proposal: put C15 to the Owner with C11; if approved, Collector adds it as a sibling of S6 using the London-only URL in the note. Licence as for S6 (OGL v3 expected, Collector to confirm).

**Correction to board 010 (C13):** INSEE `MOR_INF_RT_3Y` "2023" is most likely **2022–2024 (centred)**, not 2021–2023. Inferred by comparing with the annual France series; INSEE does not state it. Label as inferred.

CDC PLACES 2026 still not out.
