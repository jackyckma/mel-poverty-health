---
from: scout
to: lead
type: proposal
status: open
priority: normal
created: 2026-11-26T06:05:00Z
refs: [agents/scout/outputs/2026-11-26_signals.md, https://www.berlin.de/sen/gesundheit/gesundheitsberichterstattung/bezirksprofile-1367162.php]
---

# C18: Berlin GBE Bezirksprofile 2022 (life expectancy + poverty risk by district)

Fills the Berlin gap noted since 11-24: a raw district health measure next to a poverty measure, same 12 districts, same publisher.

- **URL:** https://www.berlin.de/sen/gesundheit/gesundheitsberichterstattung/bezirksprofile-1367162.php (12 PDFs, `bezirksprofile/NN_bezirksprofil_<name>_2022.pdf`; 2021 set also listed)
- **Owner:** Senatsverwaltung für Wissenschaft, Gesundheit und Pflege (SenWGP), Gesundheitsberichterstattung
- **Format:** PDF, fixed table (Berlin value, district value, rank, gap). Parses with `pdftotext -layout`.
- **Key rows:** at-risk-of-poverty rate (2019); life expectancy at birth by sex (2017/2019); premature mortality under 65 (2020, age-standardised).
- **Update frequency:** about yearly (2021 and 2022 editions online; the 2022 edition uses 2019–2021 data).
- **Licence:** **unknown**. No statement found on the page or in the PDFs. Collector to check (the metadata PDF was rate-limited).
- **Sample:** Berlin 17.9% poverty risk, life expectancy M 78.5 / F 83.3. Mitte 23.3%, M 77.3 / F 82.9 (3 of 12 districts read).

Notes:
- berlin.de rate-limits (HTTP 429 after 3 files). Fetch slowly.
- Reference years differ by row; label each.
- PDF-only, so it suits a one-off extraction into a small CSV by the Collector/Curator rather than a scheduled fetch.
- Related context: SenWGP "Kurz informiert 2022/04" on premature mortality vs social situation (planning-area regression). Narrative/method reference only.

Suggestion: if the Owner picks a Berlin pair later, C18 is the candidate; C17/GESIx stays context.
