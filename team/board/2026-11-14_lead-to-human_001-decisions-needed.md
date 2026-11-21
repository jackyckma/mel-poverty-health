---
from: lead
to: human
type: needs-human
status: open
priority: high
created: 2026-11-14T08:45:00Z
refs: [agents/mel-lead/outputs/2026-11-14_digest.md, team/board/2026-11-14_collector-to-lead_003-fetch-test-results.md, team/board/2026-11-14_curator-to-lead_001-transform-hook-proposal.md, team/board/2026-11-14_scout-to-lead_003-city-gap-sources.md]
---

# Owner decisions needed (2026-11-14)

Details and context in `agents/mel-lead/outputs/2026-11-14_digest.md`.

1. **Re-run `fetch.yml` manually** (Actions → fetch → Run workflow) to test the fixed Eurostat URL and new CDC column. Without it the dashboard goes `stale` after 2026-11-15 12:41 UTC.
2. **Fingertips size cap:** allow the London-only file (3.4 MB) or keep it off?
3. **Census ACS key:** decide how to handle it (Actions secret + script change, or keep disabled). 2025 city poverty data appears to be out; this is the main missing poverty-side source.
4. **Scout city sources C1–C5:** approve any? C3 (Berlin) and C4 (Paris) are not in English.
5. **Mandate defaults:** confirm city definition and out-of-scope list in `team/mandate.md` (still marked proposed).
6. **`fetch.yml` schedule:** keep off for now (Lead recommends: yes, keep off until Eurostat re-test and licences are checked).

---
**Lead update 2026-11-15:** No Owner reply yet; all six items still open. Changes since yesterday:

- **New item 0 (do before item 1):** apply the Curator's hook patch, then re-run `fetch.yml`, so one run tests everything. From the repo root: `patch -p0 < agents/data-curator/outputs/2026-11-15_hook-patch/scripts.diff` and `patch -p0 < agents/data-curator/outputs/2026-11-15_hook-patch/docs.diff`. README in the same folder. Dry run is clean against main.
- **Item 1:** the dashboard is now `stale` (passed 2026-11-15 12:41 UTC). This is correct, honest behaviour.
- **Item 3:** the Collector confirmed a keyless ACS request is redirected to `missing_key.html`. Option (b) "keyless first" is ruled out. Choices are now: key as an Actions secret plus a small `fetch.py` change, or keep it off.
- **Item 6:** licences for CDC PLACES (Public Domain) and Eurostat (free reuse, source acknowledged) are now confirmed from publisher pages. Lead still recommends keeping the schedule off until the Action re-run passes.
- **New item 7 (low priority):** Scout sources C6–C9 (homelessness mortality, rough sleeping, food insecurity). See `team/board/2026-11-15_scout-to-lead_004-homelessness-food-sources.md`.

---
**Lead update 2026-11-16:** No Owner reply for 2 days; all items still open.

- **Items 0+1 are now a Collector `blocker`** (`2026-11-16_collector-to-lead_006`): `fetch.yml` has run once only (2026-11-13 12:41 UTC). Data is 3 days old, the Eurostat fix is untested, the dashboard is stale. Nothing more the team can do without you.
- **Items 4 and 7:** Scout checked publisher pages for C1–C9 (`agents/scout/outputs/2026-11-16_signals.md`, section A). Open licence: C3 Berlin CSV (CC BY), C8 London CHAIN (CC BY-SA), C5 Madrid (CC BY-NC-ND, narrative only). No licence stated: C1, C2, C4, C6, C7. C9 not reached (403). Lead rule (proposed): no-licence sources are narrative-only (cite headline figures), not republished as data. Please confirm or change.

---
**Lead update 2026-11-17:** No Owner reply for 3 days; all items still open. `fetch.yml` still has one run only (2026-11-13 12:41 UTC); data is 4 days old. Curator confirms the hook patch still dry-runs clean against main.

- **Item 7 addition (low):** Scout found C10 London Health Profile 2026 (GLA, PDF, no licence → narrative only) and Eurostat `hlth_silc_21` (unmet medical need "too expensive", national *cities* category, open reuse, keyless). See `agents/scout/outputs/2026-11-17_signals.md`. Eurostat series would need your OK to add as a source; it must be labelled as a national urban category, not named cities.

---
**Lead update 2026-11-18:** No Owner reply for 4 days; all items still open. `fetch.yml` still has one run only (2026-11-13 12:41 UTC); data is 5 days old.

- **Item 7 addition (low):** Scout found Eurostat `hlth_silc_08` (unmet medical need "too expensive", by income quintile, **national**). EU27 2025: lowest fifth 2.0% vs highest 0.3%; Greece 14.5% vs 3.3%. Same licence and API as existing Eurostat source. Pairs with `hlth_silc_21`. Neither gives named cities, so both are outside the city scope unless you OK national context lines. See `agents/scout/outputs/2026-11-18_signals.md`.

---
**Lead update 2026-11-19:** No Owner reply for 5 days; all items still open. `fetch.yml` still has one run only (2026-11-13 12:41 UTC); data is 6 days old.

- **Item 7 addition (C11, normal):** DWP Children in Low Income Families, local area statistics (London region + 33 boroughs, FYE 2024–2025, provisional, keyless ODS, annual; licence probably OGL v3.0, not yet confirmed). London 30.7% of children under 16 in relative low income after housing costs vs 15.6% before; boroughs 10.6% (Richmond) to 50.3% (Tower Hamlets). First borough-level poverty series; pairs with Fingertips / C10 at the same geography. If you approve, Collector confirms licence before it is enabled. See `agents/scout/outputs/2026-11-19_signals.md` §1.

---
**Lead update 2026-11-20:** No Owner reply for 6 days; all items still open. `fetch.yml` still has one run only (2026-11-13 12:41 UTC); data is 7 days old.

- **Item 7 addition (C12, normal):** INSEE Filosofi 2023 via the Melodi API (keyless JSON; licence probably Licence Ouverte / Etalab 2.0, Collector to confirm). Paris under-18 poverty rate 21.7% (all ages 16.8%); Seine-Saint-Denis under-18 38.7%; Île-de-France 23.9%. Paris counterpart to C11 (London). Caveat: income definitions differ from DWP; no London-vs-Paris ranking without a definitions note. See `agents/scout/outputs/2026-11-20_signals.md`.

---
**Lead update 2026-11-21:** No Owner reply for 7 days; all items still open. `fetch.yml` still has one run only (2026-11-13 12:41 UTC); data is 8 days old.

- **Item 7 addition (C13, normal):** INSEE deaths and mortality series (Melodi, keyless JSON, same API as C12; licence probably Etalab 2.0, Collector to confirm). Paris (city proper) life expectancy at birth 2025 (provisional) F 87.1 / M 82.4; infant mortality 3.7‰ vs Seine-Saint-Denis 5.7‰. With C12 this gives a Paris poverty + health pair from one publisher.
- **Item 7 addition (C14, normal):** NYC Environment & Health Data Portal data (GitHub `nychealth/EHDP-data`, NYC DOHMH). Child poverty under 5 (citywide 22.5%, 2017–21) and asthma hospitalisations age 0–4 (46.2 per 10,000, 2023) for 42 neighbourhoods. Repo licence covers code only; data terms not stated → Collector to confirm, narrative-only until then. Periods differ and must be labelled.
- **C12 follow-up:** Paris 2023 poverty rate tenants 23.3% vs owners 6.1%. See `agents/scout/outputs/2026-11-21_signals.md`.
