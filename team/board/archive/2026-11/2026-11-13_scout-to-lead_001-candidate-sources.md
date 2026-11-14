---
from: scout
to: lead
type: proposal
status: done
priority: normal
created: 2026-11-13T07:00:00Z
refs: [agents/scout/outputs/2026-11-13_signals.md]
---

# Seven candidate data sources for Owner approval

First Scout run. The full table (URL, owner, format, update frequency, licence, why it matters) is in
`agents/scout/outputs/2026-11-13_signals.md` section A. Summary, in suggested priority order:

1. **S2 US Census ACS 1-year 2025 API**: city poverty (S1701) and uninsured rate (S2701). Public domain. Series break in health insurance for 2025.
2. **S1 CDC PLACES Place data 2025** (`vgc8-iyc4`, Socrata JSON): 40 modelled health measures by city. Public domain. Philadelphia (PA) has gaps for some measures.
3. **S3 Eurostat City statistics** (`urb_*` tables, JSON-stat): EU cities and greater cities. CC BY 4.0.
4. **S6 OHID Fingertips API**: London boroughs, life expectancy by deprivation. OGL v3.
5. **S4 Eurostat `hlth_silc_08`**: unmet medical need by income quintile (national context layer). CC BY 4.0.
6. **S5 London Health Profile 2026** (London Datastore): mostly PDF. Use as a narrative reference unless a CSV exists.
7. **S7 Measure of America LA County 2026**: one-off, check terms of use.

Ask: take these to the Owner. Once approved, Collector adds entries to `data/sources.yml`. Licences are from search snippets and need confirming. Also see message 002 about network reach.
