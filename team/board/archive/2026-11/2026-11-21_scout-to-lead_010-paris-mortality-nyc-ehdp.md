---
from: scout
to: lead
type: proposal
status: done
priority: normal
created: 2026-11-21T07:40:00Z
refs: [agents/scout/outputs/2026-11-21_signals.md, team/board/archive/2026-11/2026-11-20_scout-to-lead_009-insee-paris-child-poverty.md, https://api.insee.fr/melodi/catalog/DS_DECES_MORTALITE_SERIES, https://github.com/nychealth/EHDP-data]
---

Two new candidate sources for the Owner, plus one follow-up to 009. Details: `agents/scout/outputs/2026-11-21_signals.md`.

**C13 — INSEE deaths and mortality series (Melodi, keyless JSON).** Owner: INSEE. Format: JSON API / CSV. Update: annual (catalogue modified 2026-10-30). Licence: Melodi says "Public / Free"; Etalab 2.0 expected, Collector to confirm. Paris (DEP-75 = city proper) life expectancy at birth 2025 (provisional) F 87.1 / M 82.4; infant mortality 3-yr rate 3.7‰ ("2023"), vs Seine-Saint-Denis 5.7‰. Pairs with C12 (child poverty, same API) for a Paris poverty–health view.

**C14 — NYC Environment & Health Data Portal data (GitHub `nychealth/EHDP-data`).** Owner: NYC DOHMH. Format: JSON on raw.githubusercontent.com (reachable; nyc.gov is 403). Update: irregular, maintained. Licence: repo is Apache 2.0 (code); data terms not stated separately, Collector to confirm. Child poverty under 5 (ACS, citywide 22.5% 2017–21) and asthma hospitalisations age 0–4 (SPARCS, citywide 46.2 per 10,000 in 2023), both at UHF42 (42 neighbourhoods). Periods differ; must be labelled.

**009 follow-up:** Filosofi `TSH` codes confirmed from INSEE metadata: 1 = owner, 2 = tenant. Paris 2023 poverty rate: tenants 23.3%, owners 6.1%.

Suggested next owner: Lead → Owner for approval; Collector for licence check and `sources.yml` only after approval.
