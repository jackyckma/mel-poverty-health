# Setup status (instance)

Onboarding and later chats **update this file** after each step so a new session can resume. **[Lead-chat]** owns edits (on explicit setup flow). Actors: **[Admin]** prepares access; **[Owner]** runs the team; **[Lead-chat]** is the onboarding Claude chat.

| Step | Actor | Status | Notes |
|------|-------|--------|-------|
| Framework Template repository enabled | [Admin] | done | Confirmed: instance was generated from it |
| Claude + GitHub access for Owner | [Admin] / [Owner] | done | Lead-chat can read/write `jackyckma/mel-poverty-health` via GitHub connector |
| Instance repo created from template | [Lead-chat] or [Owner] | done | `jackyckma/mel-poverty-health`, created by Owner via Use this template link (2026-11-13) |
| Visibility chosen (public / private) | [Owner] | done | Public. Topic: poverty and health |
| Placeholders filled (`README.md`, `team/mandate.md`) | [Lead-chat] | done | 2026-11-13. Proposed defaults (city definition, out of scope) await Owner confirmation |
| Roles activated (instance role docs) | [Lead-chat] + [Owner] | done | Lead+PCM, Collector, Curator+Analyst, Scout; all daily |
| Sources configured (`data/sources.yml`) | [Lead-chat] + [Owner] | in progress | Owner approved all 7 Scout candidates (2026-11-13). Board instruction to Collector posted; Collector adds entries and confirms licences on its next run |
| Actions → Workflow permissions = Read repository contents (read-only) | [Owner] or [Admin] | done | Owner reported done 2026-11-13 (not independently verified by Lead-chat) |
| Pages → Source = GitHub Actions | [Owner] or [Admin] | done | Owner reported; dashboard shell loads at https://jackyckma.github.io/mel-poverty-health/ |
| `fetch.yml` schedule decision | [Owner] | pending | Leave commented until sources are in and a manual fetch is checked |
| First-run test task created in Claude UI (Repository = this repo) | [Owner] | done | Lead task created with Repository set; ran 2026-11-13 |
| First-run: Run now → `claude/*` → Merge green → commit on `main` → Pages | [Owner] + [Lead-chat] | done | Lead-chat verified: commit `4988057` on `main`, `claude/*` branch merged, Pages live |
| Remaining scheduled tasks created (UI); Active only after test | [Owner] | done | Scout `78fa02f`, Collector `eca90f7`, Curator `8eb4d3f` all landed on `main`, no stray `claude/*` branches (Lead-chat verified). Lead has not yet produced a digest |
| Human contact / digest path set | [Owner] | done | Owner via Lead chat; digests also in `agents/mel-lead/outputs/` |

## First-run test — if red

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

- Decided 2026-11-13: all 7 sources approved; network policy option (b) (routine allowlist unchanged; Actions `fetch.yml` fetches).
- Next: run Collector (adds sources, confirms licences), then check `data/sources.yml` and the board; then Owner decides on `fetch.yml` schedule after a manual fetch is checked.
- Scout's licences came from search snippets and are unverified until Collector confirms.
- Lead prompt still contains the inert FIRST-RUN TEST clause; can be removed.

## Last updated

- By: Lead-chat
- When (UTC): 2026-11-13
