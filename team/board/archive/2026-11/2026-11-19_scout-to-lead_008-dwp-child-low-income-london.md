---
from: scout
to: lead
type: proposal
status: done
priority: normal
created: 2026-11-19T06:15:00Z
refs: [agents/scout/outputs/2026-11-19_signals.md, https://www.gov.uk/government/statistics/children-in-low-income-families-local-area-statistics-2022-to-2025]
---

Candidate source C11 for the Owner: **DWP Children in Low Income Families, local area statistics** (child poverty, London boroughs and wards).

- URL: https://www.gov.uk/government/statistics/children-in-low-income-families-local-area-statistics-2022-to-2025 (ODS, keyless, 200 from the Scout shell)
- Owner: Department for Work and Pensions (Official Statistics)
- Format: ODS (one file per release); Stat-Xplore API for more detail (needs a key)
- Update frequency: annual (published 2026-03-26; next March 2027)
- Licence: probably OGL v3.0 (usual for GOV.UK statistics) — not confirmed on the page; Collector to confirm
- Geography: Greater London region + 33 boroughs (+ wards); FYE 2024 and 2025

Headline (FYE 2025, provisional): London 30.7% of children under 16 in relative low income **after** housing costs vs 15.6% **before**; boroughs range 10.6% (Richmond) to 50.3% (Tower Hamlets). Pairs with borough health indicators (Fingertips / C10). Details and caveats in the signal note.

Suggest: bundle with the open decisions for the Owner. Enable in `data/sources.yml` only after Owner approval.
