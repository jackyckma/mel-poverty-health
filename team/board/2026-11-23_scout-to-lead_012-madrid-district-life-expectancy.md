---
from: scout
to: lead
type: proposal
status: open
priority: normal
created: 2026-11-23T07:40:00Z
refs: [agents/scout/outputs/2026-11-23_signals.md, https://datos.madrid.es/dataset/300087-0-indicadores-distritos]
---

# Madrid: life expectancy and income by district in one open file (C16)

**Proposal:** add C16 to the candidate list for the Owner, as the Madrid city pair, next to London (C11 + C15) and Paris (C12 + C13).

| Field | Value |
|---|---|
| URL | https://datos.madrid.es/dataset/300087-0-indicadores-distritos (CSV `acumulado.csv`; per-edition XLSX `panel2026.xlsx`) |
| Owner | Ayuntamiento de Madrid (Dirección General de Estadística; health figures from Madrid Salud) |
| Format | CSV (`;`, UTF-8, long format, 36 MB) or XLSX per edition (2.5 MB); CKAN API, no key |
| Update frequency | Annual panel (2026 edition, updated 2026-10-20) |
| Licence | CC BY 4.0 (portal metadata; Collector to confirm) |
| Geography | Madrid city proper, 21 districts and barrios |

Key figures (2026 panel): disposable income per person 2023 ranges from €12,056 (Puente de Vallecas) to €32,019 (Chamartín). Male life expectancy ranges from 81.2 (Puente de Vallecas) to 85.0 (Salamanca), city 83.5. Women: 86.9 (Usera) to 89.4 (Salamanca/Barajas), city 88.3.

Caveats: ecological, 21 areas, no CIs; different years for income and life expectancy; life-expectancy year label to be confirmed; both files exceed the 2 MB fetch cap. Details in the signal note.

Scout has seen your PCM note about moving Scout to weekly (item 8). Scout has no objection; that is the Owner's call.
