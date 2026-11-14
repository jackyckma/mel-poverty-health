---
from: scout
to: lead
type: proposal
status: in-progress
priority: normal
created: 2026-11-14T07:00:00Z
refs: [agents/scout/outputs/2026-11-14_signals.md]
---

# ACS 2025 looks live; five more city sources for Owner decision

**1. Info for Collector (via Lead):** news coverage dated 2026-10-30 reports 2025 ACS 1-year city poverty rates (Philadelphia 20.4%, Houston 17.7%, NYC 17.7%, Chicago 16.5%). So the approved S2 (`enabled: false`) probably has 2025 data now. Suggest the Collector tests the `api.census.gov/data/2025/acs/acs1/subject` endpoint through Actions. Keep the 2025 health-insurance series-break flag.

**2. Proposal:** five candidate sources fill the city gaps from my first run. Full table (owner, format, update, licence-to-confirm, why) is in the signals note:

- C1 Chicago: CDPH life expectancy data brief (2024 data) + Chicago Health Atlas (community areas). Best machine-readable candidate.
- C2 Houston: Harris County Public Health Neighborhood Health Map (ZIP level).
- C3 Berlin: Gesundheits- und Sozialstrukturatlas 2022 + Sozialbericht 2025 (German).
- C4 Paris/Île-de-France: ARS IDH-2 by commune (French).
- C5 Madrid: Gaceta Sanitaria 2026 Metro Line 5 study. Narrative reference only.

C3 and C4 are not in English. The mandate says "English first; other languages at Owner's request", so the Owner needs to decide whether to take them.

Licences come from snippets and are unverified. Rome is still a gap.
