# Instance role: Data Collector

Follow `team/roles/_base/data-collector.md`, plus:

## Activation

- [x] Active

## Domain specifics

| Slot | Value |
|------|-------|
| Cadence | Daily |
| Source owners | Owner has set no initial sources. Scout proposes; Owner approves before a source is enabled in `data/sources.yml`. |
| Freshness SLA | Daily check; many health and poverty datasets update yearly or less, so record each source's own update frequency and do not treat unchanged data as a failure. |
| Auth / secrets location (never commit values) | GitHub Actions secrets names only |
| Notes | No initial source scope: find sources independently (official statistics, public health agencies, city open data, reputable research and news). Coverage: US and European cities above 2 million. Prefer primary sources. |
