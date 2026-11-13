# Poverty and health — MEL agent team

This is an **instance** repo for a Monitoring, Evaluation & Learning (MEL) agent team.

| | |
|--|--|
| **Topic** | Poverty and health |
| **Purpose** | Monitor data and news at the junction of poverty and health, and produce charts, analysis and narratives that raise awareness of the topic, using honest and proper methods. |
| **Audience** | Interested general public; academics working in this area |
| **Framework version** | see `FRAMEWORK_VERSION` |

## Start here

- Mandate: [`team/mandate.md`](team/mandate.md)
- How the team works: [`team/process.md`](team/process.md)
- Setup checklist: [`team/SETUP_STATUS.md`](team/SETUP_STATUS.md)
- Operator guide (plain English): [`framework/docs/OPERATING_GUIDE.md`](framework/docs/OPERATING_GUIDE.md)
- Dashboard (GitHub Pages): [`docs/`](docs/)

Talk only to the **MEL Lead**. Human instructions go on the board as `from: human` (see process + operating guide). The Owner (Jacky) is contacted in the Lead chat; daily digests are also saved under `agents/mel-lead/outputs/`.

## This repo and the framework

This repo was created from **mel-agent-framework** (see `FRAMEWORK_VERSION`). The `framework/` folder is a **read-only reference copy** for humans and agents: do not edit it in normal runs. Upgrades happen only via a Lead-led, human-approved framework sync.

Framework design notes and bootstrap prompts live under `framework/`. Instantiation checklist: `framework/INSTANTIATE.md`.

## Active roles

- MEL Lead + Project & Change Manager (combined, slug `mel-lead`) — daily
- Data Collector (slug `data-collector`) — daily
- Data Curator + Dashboard Analyst (combined, slug `data-curator`) — daily
- Scout (slug `scout`) — daily

More roles (e.g. Narrative Designer) can be added later.

## Secrets

Never commit API keys or sensitive personal data. Use GitHub Actions secrets when a source needs credentials.
