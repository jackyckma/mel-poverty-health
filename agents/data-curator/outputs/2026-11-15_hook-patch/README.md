# Transform and dashboard hook patch (draft, not applied)

Drafted by data-curator on 2026-11-15, as asked in board `2026-11-14_lead-to-curator_001-hook-patch-yes.md`.
**Nothing under `scripts/` or `docs/` has been changed.** The Owner (or the Lead on the Owner's instruction) applies it.

## Files

| File | What it is |
|------|------------|
| `scripts.diff` | Unified diff for `scripts/transform.py` and `scripts/build_dashboard.py` (apply from repo root with `patch -p0 < scripts.diff`) |
| `docs.diff` | Unified diff for `docs/dashboard.js` (curator-owned shell; kept here so everything lands together) |
| `scripts/transform.py`, `scripts/build_dashboard.py`, `docs/dashboard.js` | Full replacement files, same content as the diffs |
| `fixtures/SYNTHETIC_*` | **Synthetic** test inputs (made-up values). Test only. Never copy into `data/raw/`. |

## What changes and why

1. **CDC PLACES long rows + crash-safe CSV writer** (`transform.py`)
   - `customise_row()` may now return a list. For `cdc-places-*` it emits one row per city and measure:
     `geo_code` (7-digit FIPS, zero-padded so `644000` becomes `0644000`), `geo_name`, `geo_level`
     (`US Census place (city proper)`), `measure_id`, `measure_label`, `value`, `ci95_low`, `ci95_high`,
     `unit`, `status` (`ok` or `missing_in_source`).
   - City name: `locationname` when present; otherwise a 4-city FIPS lookup (the 2026-11-13 snapshot has the FIPS code in `placename`).
   - `all_rows.csv` now writes the union of keys (`restval=""`, `extrasaction="ignore"`). The old
     `DictWriter(fieldnames=["source_id","payload"])` raises `ValueError` on any extra key, so the tidy hook without this fix would crash the Action.
   - Sources without a hook keep the old `payload` row (they fill the `payload` column; tidy columns stay blank).
   - `summary.json` gains `row_counts` per source (additive; existing keys unchanged).
2. **JSON-stat flattener for Eurostat** (`transform.py`)
   - Any JSON payload with `id`, `size`, `dimension`, `value` is treated as JSON-stat 2.0 and flattened to long rows.
   - Missing cells (absent from Eurostat's sparse `value`) are emitted with `status=missing_in_source`, so gaps stay visible (up to 50,000 cells; above that, only present cells).
   - Eurostat cell flags go into `status` (for example `ok:b` = break in series).
   - `geo_level` for `*silc*` sources is `country (national context, not city)`.
3. **Instance dashboard sections** (`build_dashboard.py`, `dashboard.js`)
   - Sections: Overview; City comparisons; News signals; Data gaps and method notes.
   - Charts: one bar chart per CDC PLACES measure (cities, city proper, with CI arrays); one Eurostat chart (poorest vs richest income fifth, latest year that **all** countries have); the old rows-by-source chart kept as a pipeline check.
   - Every chart carries `source`, `geography`, `date` (release/year + collection time) and `note` (missing cities named). `dashboard.js` prints them under each chart.
   - `publication_status`: "Internal draft: not for publication until the Owner approves (via MEL Lead)." shown in the summary line.
   - Data gaps section lists disabled sources, never-collected sources (with last error) and blank cells.
   - No poverty-vs-health chart or claim. The Overview says so until poverty-side data lands.
   - Freshness logic is unchanged: `last_updated` is still collection time, `stale` still 48 h.
   - Removed `ticks.precision: 0` on the y axis, so percentages such as 11.9 are not shown as whole numbers.

## How it was tested (locally, 2026-11-15, Python 3, no network)

| Test | Input | Before (current scripts) | After (patch) |
|------|-------|--------------------------|---------------|
| A | Real raw snapshot `data/raw/cdc-places-place-2025/20261113T124153Z.csv` | 4 rows, each a JSON `payload` string; 1 chart "rows by source" = 4 | 20 tidy rows; values and CIs match `data/processed/curated/us_cities_cdc_places_2025.csv`; Houston `foodinsecu`/`housinsecu` = `missing_in_source`; 5 city charts + pipeline chart; gaps section lists Eurostat HTTP 400 and the 3 disabled sources |
| B | Synthetic fixtures (CDC with `locationname`; Eurostat JSON-stat 8 dims, 120 cells, 6 missing, 1 flag) plus one generic JSON source | Eurostat = **1 row** holding the whole dataset; 4 rows total | 125 rows (CDC 4, Eurostat 120 incl. 6 `missing_in_source`, generic 1 with `payload`); Eurostat chart picks 2023 because IT has no 2024; flag shows as `ok:b` |
| C | Old CSV writer + tidy rows | — | Old writer raises `ValueError: dict contains fields not in fieldnames`; new writer OK |
| D | `patch -p0 --dry-run` against `HEAD` copies of `scripts/` and `docs/` | — | Applies cleanly |
| E | `node --check docs/dashboard.js` | — | OK |

Not tested: a real Eurostat response (no Action run since the URL fix) and the real `locationname` column. Both get checked on the first Action run after the patch.

## After applying

- Run `fetch.yml` once (manual). Then the curator checks: Eurostat rows have the expected dimension codes, `locationname` arrived, `all_rows.csv` header, and `docs/data/dashboard.json` sections.
- `data/processed/curated/us_cities_cdc_places_2025.csv` can then be retired in favour of the Action output (curator decides after comparing).
- Labels in `CDC_PLACES_MEASURES` are curator wording; check against the PLACES data dictionary.
