---
from: scout
to: lead
type: info
status: done
priority: low
created: 2026-11-18T07:20:00Z
refs: [agents/scout/outputs/2026-11-18_signals.md, https://ec.europa.eu/eurostat/databrowser/view/hlth_silc_08/default/table]
---

# Eurostat hlth_silc_08: cost barrier to care by income quintile

Details in `agents/scout/outputs/2026-11-18_signals.md`. No approval asked; add to the open Eurostat question for the Owner if useful.

- `hlth_silc_08` (updated 2026-10-20): unmet need for medical examination because "too expensive", people 16+, by income quintile. **National**, not cities.
- EU27 2025: lowest income fifth 2.0% vs highest 0.3%. France 3.9% vs 0.4%; Italy 3.0% vs 0.3%; Greece 14.5% vs 3.3%. The lowest fifth is higher in every country checked.
- It pairs with `hlth_silc_21` (cities category, no income split). Neither gives named cities. Same licence and keyless API as the existing Eurostat source.
- Watch list: CDC PLACES 2026 not out yet; ISTAT SDMX timed out; C9 still 403.
