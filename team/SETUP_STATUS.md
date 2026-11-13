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
| Sources configured (`data/sources.yml`) | [Lead-chat] + [Owner] | pending | Scout proposed 7 candidates (board 001); awaiting Owner approval. Example entry stays disabled |
| Actions → Workflow permissions = Read repository contents (read-only) | [Owner] or [Admin] | done | Owner reported done 2026-11-13 (not independently verified by Lead-chat) |
| Pages → Source = GitHub Actions | [Owner] or [Admin] | done | Owner reported; dashboard shell loads at https://jackyckma.github.io/mel-poverty-health/ |
| `fetch.yml` schedule decision | [Owner] | pending | Leave commented until sources approved and checked |
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

- Owner decisions open: (1) approve / drop the 7 Scout candidate sources; (2) network policy: allow data hosts for routines, or rely on Actions `fetch.yml` for fetching (Scout board 002).
- Scout's licences come from search snippets and are unverified; Scout's session cannot reach data hosts.
- Lead prompt still contains the inert FIRST-RUN TEST clause; can be removed.
- Next: Lead digest run; after approval, Collector adds sources to `data/sources.yml`, then decide `fetch.yml` schedule.

## Last updated

- By: Lead-chat
- When (UTC): 2026-11-13
