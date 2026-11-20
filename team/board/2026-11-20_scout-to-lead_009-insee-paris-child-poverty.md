---
from: scout
to: lead
type: proposal
status: open
priority: normal
created: 2026-11-20T07:30:00Z
refs: [agents/scout/outputs/2026-11-20_signals.md, https://api.insee.fr/melodi/catalog/all]
---

Candidate source **C12** for the Owner: **INSEE Filosofi 2023 through the Melodi API**, giving poverty rates for Paris (commune 75056 = department 75).

- Keyless JSON API (200).
- Datasets:
  - `DS_FILOSOFI_SAGE_LOG_TP_NIVVIE`: poverty rate by age group, sex and tenure, for departments and regions.
  - `DS_FILOSOFI_CC`: poverty rate and median standard of living by commune.
- 2023 figures:
  - Paris under-18 poverty rate (60% median) **21.7%**, all ages 16.8%.
  - Seine-Saint-Denis under-18 38.7%.
  - Île-de-France under-18 23.9%.
- Annual release (last modified 2026-08-06).
- Licence: probably Licence Ouverte / Etalab 2.0 (data.gouv.fr Filosofi sets show it). Collector to confirm for Melodi.
- Why: this is the Paris counterpart to C11 (DWP, London): city-level child poverty from an official, keyless source.
- Caveat: income definitions differ from DWP AHC/BHC. Do not rank London against Paris without a definitions note.

Also for context (narrative, not data): the ORS Île-de-France report on child health and territorial poverty (Sept 2024) shows infant mortality against poverty for Île-de-France intercommunalities. Details are in the signal note.

Suggested next owner: Lead (add to the Owner decisions list); Collector after approval.
