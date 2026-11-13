---
from: lead
to: collector
type: task
status: open
priority: high
created: 2026-11-13T13:10:00Z
refs: [data/sources.yml, data/fetch_status.json]
---

# Fix `eurostat-hlth-silc-08` URL (HTTP 400)

The Actions run returned HTTP 400. Two defects in the URL, both checked from the Lead chat against the live API:

1. The income dimension is `quant_inc`, not `quantile`. (Values TOTAL, QU1 to QU5 are valid.)
2. `reason=TOOEFW` does not exist in this dataset. Valid `reason` codes: TXP (too expensive), TXP_TFAR_WLIST (too expensive, too far or waiting list), TFAR, NTIME, WLIST, GDOC_UNK, FEAR_DR_HSP, HOPE, NUMT_ND (no unmet needs), OTH.

Use the headline indicator `TXP_TFAR_WLIST`. Also add `freq=A` and keep unit=PC, sex=T, age=Y_GE16, geo DE/ES/FR/IT, sinceTimePeriod=2020.

Corrected URL:

`https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/hlth_silc_08?format=JSON&lang=EN&freq=A&unit=PC&reason=TXP_TFAR_WLIST&sex=T&age=Y_GE16&geo=DE&geo=ES&geo=FR&geo=IT&quant_inc=TOTAL&quant_inc=QU1&quant_inc=QU2&quant_inc=QU3&quant_inc=QU4&quant_inc=QU5&sinceTimePeriod=2020`

Note: Eurostat lists these as the geo codes of countries; city-level coverage is a separate source (`eurostat-urb-clivcon`, still disabled). Label this source "country level" in notes.

Keep the source enabled. The Owner will re-run the fetch Action; verify `data/fetch_status.json` afterwards.
