---
from: scout
to: lead
type: info
status: open
priority: low
created: 2026-11-17T07:30:00Z
refs: [agents/scout/outputs/2026-11-17_signals.md, https://data.london.gov.uk/dataset/london-health-profile-2z1kq, https://ec.europa.eu/eurostat/databrowser/view/hlth_silc_21/default/table]
---

# New signals: London Health Profile 2026 (C10) and Eurostat "too expensive" in cities

Details in `agents/scout/outputs/2026-11-17_signals.md`. No approval asked; for the Owner's next decision round.

- **C10 London Health Profile 2026** (GLA, London Datastore). PDF only, published 2026-09-10, **no licence field** in Datastore metadata. Links deprivation to healthy life expectancy across boroughs. Narrative-only under your 002 rule; the underlying OHID/ONS series are likely the better primary sources.
- **Eurostat hlth_silc_21** (updated 2026-07-06, 2025 values): unmet medical need because "too expensive", people 16+ living in **cities** (national degree-of-urbanisation category, not named cities). EU27 1.0%, France 2.4%, Italy 1.4%, Germany 0.2%, Spain 0.2%, Greece 8.7% (2025). Open reuse, keyless API. Possible context line for European access-to-care; must be labelled as national urban category.
- **Reuse terms C1/C6/C7:** not found today (C1 page is JS-only, nyc.gov 403, LA County disclaimer URL dead). Set your 002 to done.
