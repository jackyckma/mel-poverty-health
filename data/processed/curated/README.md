# Curated files (Data Curator)

These files are written by the Data Curator. They are **not** written or overwritten by the
`fetch.yml` Action. The Action's generic outputs (`../all_rows.csv`, `../<source>.json`,
`../summary.json`) keep each raw record as one JSON `payload` string. That is fine for audit, but
hard to analyse. The files here are tidy, long-format versions of the same raw snapshots.

Each row names its `source_id`, release and the raw snapshot it came from. Rebuild a file only
when its raw snapshot changes.

| File | Built from | Geography | Notes |
|------|-----------|-----------|-------|
| `us_cities_cdc_places_2025.csv` | `data/raw/cdc-places-place-2025/20261113T124153Z.csv` | US Census place (city proper) | 4 US cities over 2 million x 5 measures. Values are age-adjusted, model-based estimates (CDC PLACES), with 95% CI. City names are from a curator FIPS lookup because `placename` held the FIPS code in that snapshot; `locationname` arrives with the next fetch. Measure labels are curator wording from PLACES definitions and are not yet checked against the PLACES data dictionary. `population_as_reported` is the PLACES `totalpopulation` column; its census vintage is not confirmed. `status=missing_in_source` marks blanks in the source. |

Licence for CDC PLACES is still unconfirmed (see `data/sources.yml`). Do not publish from these
files until the Lead and Owner confirm it.
