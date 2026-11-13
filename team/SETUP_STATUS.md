# Setup status (instance)

Onboarding and later chats **update this file** after each step so a new session can resume. **[Lead-chat]** owns edits (on explicit setup flow). Actors: **[Admin]** prepares access; **[Owner]** runs the team; **[Lead-chat]** is the onboarding Claude chat.

| Step | Actor | Status | Notes |
|------|-------|--------|-------|
| Framework Template repository enabled | [Admin] | done | Confirmed: instance was generated from it |
| Claude + GitHub access for Owner | [Admin] / [Owner] | done | Lead-chat can read/write `jackyckma/mel-poverty-health` via GitHub connector |
| Instance repo created from template | [Lead-chat] or [Owner] | done | `jackyckma/mel-poverty-health`, created by Owner via Use this template link (2026-11-13) |
| Visibility chosen (public / private) | [Owner] | done | Public. Topic: poverty and health |
| Placeholders filled (`README.md`, `team/mandate.md`) | [Lead-chat] | done | 2026-11-13. Proposed defaults (city definition, out of scope) await Owner confirmation. US scope for now: New York, Los Angeles, Chicago, Houston (city proper), confirmed by Owner |
| Roles activated (instance role docs) | [Lead-chat] + [Owner] | done | Lead+PCM, Collector, Curator+Analyst, Scout; all daily |
| Sources configured (`data/sources.yml`) | [Lead-chat] + [Owner] | in progress | Owner approved all 7 candidates. Provisionally enabled (filtered): CDC PLACES, Eurostat hlth_silc_08. Disabled: Census (needs key, fetch.py cannot send one), Fingertips (area type 502 now confirmed; enable after first run), Eurostat urb_clivcon (unchecked). Licences unconfirmed |
| Actions → Workflow permissions = Read repository contents (read-only) | [Owner] or [Admin] | done | Owner reported done 2026-11-13 (not independently verified by Lead-chat) |
| Pages → Source = GitHub Actions | [Owner] or [Admin] | done | Owner reported; dashboard shell loads at https://jackyckma.github.io/mel-poverty-health/ |
| `fetch.yml` schedule decision | [Owner] | pending | Leave commented until the manual test is reviewed and licences confirmed |
| First-run test task created in Claude UI (Repository = this repo) | [Owner] | done | Lead task created with Repository set; ran 2026-11-13 |
| First-run: Run now → `claude/*` → Merge green → commit on `main` → Pages | [Owner] + [Lead-chat] | done | Lead-chat verified: commit `4988057` on `main`, `claude/*` branch merged, Pages live |
| Remaining scheduled tasks created (UI); Active only after test | [Owner] | done | Scout, Collector, Curator all landed on `main`. Lead has not yet produced a digest |
| Small filtered fetch test: Collector enables sources | [Owner] + [Collector] | done | Collector commit `ca98005` on `main`; board collector-to-lead 002 |
| Small filtered fetch test: manual `fetch.yml` run in Actions | [Owner] | pending | See `team/onboarding/FIRST_DATA_FETCH.md` Part B/C. Read OK/FAIL lines; green tick alone proves nothing |
| Licences confirmed from publishers' pages | [Owner] + [Lead-chat] | pending | Nothing published until done |
| Human contact / digest path set | [Owner] | done | Owner via Lead chat; digests also in `agents/mel-lead/outputs/` |

## First-run test: if red

1. Open Actions: **Trigger merge agent branch** / **Merge agent branches** / Pages.
2. Check Actions is enabled; the failed workflow’s own `permissions:` block; Pages source = GitHub Actions.
3. Ask [Lead-chat] to diagnose; leave `claude/*` for inspection; re-run after fix.
4. Do not set tasks Active until `main` shows the test commit.

## Active roles (fill during setup)

- MEL Lead + PCM (`mel-lead`), daily
- Data Collector (`data-collector`), daily
- Data Curator + Dashboard Analyst (`data-curator`), daily
- Scout (`scout`), daily

## Blockers / resume notes

- Next: [Owner] runs `fetch.yml` manually (Actions tab), reads the OK/FAIL lines, tells Lead-chat "fetched". Lead-chat then checks `data/fetch_status.json` and `data/raw/` on `main`.
- Open Owner decision: Census API key (fetch.py has no key support; needs a script change and an Actions secret), or drop Census for now.
- Lead-chat could not verify the two filtered URLs beforehand; the Actions run is the real test.
- Lead prompt still contains the inert FIRST-RUN TEST clause; can be removed.
- Lead task has not produced a digest yet.

## Last updated

- By: Lead-chat
- When (UTC): 2026-11-13
