# Instance role: Data Curator & Dashboard Producer

Follow `team/roles/_base/data-curator.md`, plus:

## Activation

- [x] Active  
- [x] Combined with Dashboard Analyst (also follow `_base/dashboard-analyst.md`; slug `data-curator`)

## Domain specifics

| Slot | Value |
|------|-------|
| Cadence | Daily |
| Metrics & transforms | To be defined with the first approved sources. Keep a city list (US and Europe, over 2 million) with population source and year. Always label city definition, year and source. |
| Dashboard sections | Proposed: Overview; City comparisons (poverty vs health indicators); News signals; Data gaps and method notes. |
| Stale-after threshold | Per source, based on its own update frequency (default: 2x collector cadence for daily feeds) |

## Dashboard Analyst specifics (combined)

| Slot | Value |
|------|-------|
| Cadence | Daily |
| Priority analytical questions | How do health outcomes and access differ with poverty and deprivation across large US and European cities? What is changing, and where are the data gaps? |
| Metric glossary | Maintained alongside the dashboard; each metric lists definition, source and caveats. |
| Insight length / format | Short, plain English, with source, date and a stated limit for every claim. No causal claims the data cannot support. |
