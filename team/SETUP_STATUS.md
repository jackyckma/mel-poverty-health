# Setup status (instance)

Onboarding and later chats **update this file** after each step so a new session can resume. **[Lead-chat]** owns edits (on explicit setup flow). Actors: **[Admin]** prepares access; **[Owner]** runs the team; **[Lead-chat]** is the onboarding Claude chat.

| Step | Actor | Status | Notes |
|------|-------|--------|-------|
| Framework Template repository enabled | [Admin] | done | Confirmed: instance was generated from it |
| Claude + GitHub access for Owner | [Admin] / [Owner] | done | Lead-chat can read/write `jackyckma/mel-poverty-health` via GitHub connector |
| Instance repo created from template | [Lead-chat] or [Owner] | done | `jackyckma/mel-poverty-health`, created by Owner via Use this template link (2026-11-13) |
| Visibility chosen (public / private) | [Owner] | done | Public. Topic: poverty and health |
| Placeholders filled (`README.md`, `team/mandate.md`) | [Lead-chat] | pending | Via connector write |
| Roles activated (instance role docs) | [Lead-chat] + [Owner] | pending | |
| Sources configured (`data/sources.yml`) | [Lead-chat] + [Owner] | pending | Examples disabled until reviewed |
| Actions → Workflow permissions = Read repository contents (read-only) | [Owner] or [Admin] | pending | Do **not** use Read and write; jobs set their own `permissions:` |
| Pages → Source = GitHub Actions | [Owner] or [Admin] | pending | Settings → Pages |
| `fetch.yml` schedule decision | [Owner] | pending | Leave commented until sources trusted |
| First-run test task created in Claude UI (Repository = this repo) | [Owner] | pending | Chat/API tasks **cannot** push (no Repository) |
| First-run: Run now → `claude/*` → Merge green → commit on `main` → Pages | [Owner] + [Lead-chat] | pending | Task UI success ≠ verified |
| Remaining scheduled tasks created (UI); Active only after test | [Owner] | pending | Paste blocks from Lead-chat |
| Human contact / digest path set | [Owner] | pending | `{{HUMAN_CONTACT}}` |

## First-run test — if red

1. Open Actions: **Trigger merge agent branch** / **Merge agent branches** / Pages.
2. Check Actions is enabled; the failed workflow’s own `permissions:` block; Pages source = GitHub Actions.
3. Ask [Lead-chat] to diagnose; leave `claude/*` for inspection; re-run after fix.
4. Do not set tasks Active until `main` shows the test commit.

## Active roles (fill during setup)

- 

## Blockers / resume notes

- Next: mandate round (purpose, audience, decisions, scope, out of scope, sources notes, roles, cadences, human contact).

## Last updated

- By: Lead-chat
- When (UTC): 2026-11-13
