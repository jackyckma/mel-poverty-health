# Curator + Analyst review — 2026-11-14 (first real data)

## Freshness check (as of 2026-11-14 ~08:30 UTC, main @ 6f6f7de)
| Artefact | State | Verdict |
|---|---|---|
| `data/fetch_status.json` | `updated_at 2026-11-13T12:41:55Z` (manual test run) | ~20 h old. Fine for an annual source. The cron is still off, so nothing refreshes unless the Owner re-runs `fetch.yml`. |
| `cdc-places-place-2025` | OK, 4 rows | Matches Collector's report. |
| `eurostat-hlth-silc-08` | HTTP 400 in that run | URL fixed by Collector on 11-14; not yet tested by the Action. |
| `data/processed/summary.json` | 4 rows, `input_fresh_at 2026-11-13T12:41:54Z` | Correct. |
| `docs/data/dashboard.json` | `stale:false`, threshold 48 h | Honest now. It will read **stale** after 2026-11-15 12:41 UTC unless the Action runs again. That is the correct behaviour for a manual pipeline, not a bug. |

## Review of the mechanical transform
1. **Generic hook only.** `customise_row()` stores each record as a JSON string in `payload`. Not usable for analysis. I built a tidy long-format file by hand instead: `data/processed/curated/us_cities_cdc_places_2025.csv` (20 rows; see `data/processed/curated/README.md`).
2. **Trap for whoever customises the hook:** `all_rows.csv` uses `csv.DictWriter(fieldnames=["source_id","payload"])` with the default `extrasaction="raise"`. If `customise_row()` returns tidy columns, the transform will **crash**. The writer must change too.
3. **Eurostat is JSON-stat.** When `eurostat-hlth-silc-08` fetches, `iter_records()` sees a dict with no `data/results/items/records` list, so the whole dataset becomes **one** row with a large `payload`. It needs a JSON-stat flattener before it is usable.
4. `build_dashboard.py` only charts "rows per source". Dashboard sections are still the placeholder.

I have not edited `scripts/`. Under `team/process.md` that needs Lead coordination, so I posted a proposal (board curator-to-lead 001).

## Insights (Dashboard Analyst) — internal, not for publication
Source for all: CDC PLACES 2025 release, `vgc8-iyc4`, US Census places (city proper), age-adjusted model-based estimates for adults, fetched 2026-11-13. Licence unconfirmed. These are four US cities only. They are not a sample of "large cities".

- **Uninsured adults (18-64): Houston stands apart.** Houston 24.0% (95% CI 22.1-26.0) vs LA 13.2, Chicago 13.6, NYC 10.6. The intervals do not overlap. *Limit:* PLACES values are model-based small-area estimates, not direct survey counts. State insurance policy differs (TX vs CA/IL/NY). This shows a difference, not its cause.
- **Diagnosed diabetes:** Houston 14.4% (12.9-15.9) is highest. LA 11.9, Chicago 12.4 and NYC 11.5 overlap with each other. Houston's interval overlaps Chicago's (13.6 upper vs 12.9 lower), so the ranking is not firm.
- **Depression:** LA 20.2% (18.3-22.1), Houston 19.5, Chicago 18.7, NYC 16.4 (15.2-17.5). Most intervals overlap. Only NYC vs LA is clearly separated.
- **Food insecurity (~24%) and housing insecurity (~19-20%)** look alike in LA, Chicago and NYC, with overlapping CIs. **Houston has no value for either.** Likely reason: these are social-needs measures that rely on an optional survey module some states do not run. *Unverified:* check the PLACES documentation before stating this reason.
- **No poverty measure yet.** None of this links health to poverty. The poverty side waits on ACS (Census API key decision) and the European side on Eurostat. Until then, any "poverty vs health" comparison would be unsupported.

## Data gaps (for the dashboard "Data gaps and method notes" section)
- Europe: no city-level data yet (Eurostat SILC fix is country level; `urb_clivcon` not authorised).
- US poverty rate: ACS disabled (API key).
- Houston food/housing insecurity: missing in source.
- City list (`cities.csv`): still waiting on a primary population source with a stated year. PLACES `totalpopulation` has no confirmed vintage, so I am not using it as the city-list population source.
