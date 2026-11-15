#!/usr/bin/env python3
"""Build docs/data/*.json from data/processed/ for the static dashboard.

Offline-safe: always ensures docs/data/dashboard.json exists (may be empty
series) so Pages renders without network.

Freshness uses collection time (`input_fresh_at` from transform / fetch_status),
not transform clock time, so reprocessing cached snapshots cannot look fresh.
The browser also recomputes staleness on load (see docs/dashboard.js).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_summary(processed: Path) -> dict[str, Any]:
    path = processed / "summary.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"updated_at": None, "input_fresh_at": None, "row_count": 0, "sources": []}


def load_fetch_status(root: Path) -> dict[str, Any]:
    path = root / "data" / "fetch_status.json"
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def build_series(processed: Path) -> list[dict[str, Any]]:
    """Simple series: row counts per source file."""
    series = []
    if not processed.exists():
        return series
    for path in sorted(processed.glob("*.json")):
        if path.name == "summary.json":
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        count = len(data) if isinstance(data, list) else 1
        series.append({"label": path.stem, "value": count})
    return series


# ---------------------------------------------------------------------------
# Instance hooks (MEL poverty-health). Drafted by data-curator 2026-11-15,
# per board lead-to-curator 001. Honest-method rules: every view names source,
# date and geography; gaps are listed; no poverty-vs-health claim until
# poverty-side data lands; the page is an internal draft until the Owner
# approves publication.
# ---------------------------------------------------------------------------

SOURCE_CITES = {
    "cdc-places-place-2025": "CDC PLACES 2025 release, dataset vgc8-iyc4 (Public Domain; CDC NCCDPHP Division of Population Health)",
    "eurostat-hlth-silc-08": "Source: Eurostat (hlth_silc_08), EU-SILC. Modified (filtered, reshaped) by MEL; Eurostat is not responsible for this output",
}

PUBLICATION_STATUS = "Internal draft: not for publication until the Owner approves (via MEL Lead)."


def load_rows(processed: Path, source_id: str) -> list[dict[str, Any]]:
    path = processed / f"{source_id}.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return [r for r in data if isinstance(r, dict) and r.get("measure_id")] if isinstance(data, list) else []


def collected_at(fetch_status: dict[str, Any], source_id: str) -> str:
    entry = (fetch_status.get("sources") or {}).get(source_id) or {}
    return entry.get("last_success") or "never collected"


def city_charts(processed: Path, fetch_status: dict[str, Any]) -> list[dict[str, Any]]:
    charts = []
    sid = "cdc-places-place-2025"
    rows = load_rows(processed, sid)
    measures: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        measures.setdefault(r["measure_id"], []).append(r)
    for mid, mrows in measures.items():
        mrows = sorted(mrows, key=lambda r: r.get("geo_name") or "")
        missing = [r["geo_name"] for r in mrows if r.get("value") is None]
        charts.append(
            {
                "id": f"cdc-{mid}",
                "title": f"{mrows[0].get('measure_label', mid)}: US cities over 2M (city proper)",
                "type": "bar",
                "labels": [r["geo_name"] for r in mrows],
                "values": [r.get("value") for r in mrows],
                "ci95_low": [r.get("ci95_low") for r in mrows],
                "ci95_high": [r.get("ci95_high") for r in mrows],
                "source": SOURCE_CITES[sid],
                "geography": "US Census place (city proper)",
                "date": f"{mrows[0].get('period', '')}; collected {collected_at(fetch_status, sid)}",
                "note": "Age-adjusted model-based estimates with 95% CI."
                + (f" No value in source for: {', '.join(missing)}." if missing else ""),
            }
        )
    return charts


def national_charts(processed: Path, fetch_status: dict[str, Any]) -> list[dict[str, Any]]:
    sid = "eurostat-hlth-silc-08"
    rows = [r for r in load_rows(processed, sid) if r.get("value") is not None]
    if not rows:
        return []
    # Latest year that every country has, so bars compare like with like.
    by_geo: dict[str, set[str]] = {}
    for r in rows:
        by_geo.setdefault(r["geo_code"], set()).add(r["period"])
    common = set.intersection(*by_geo.values()) if by_geo else set()
    if not common:
        return []
    year = max(common)
    keep = {"quant_inc=QU1": "poorest fifth", "quant_inc=QU5": "richest fifth"}
    labels, values = [], []
    for geo in sorted(by_geo):
        for bd, name in keep.items():
            hit = [r for r in rows if r["geo_code"] == geo and r["period"] == year and bd in r.get("breakdown", "")]
            if hit:
                labels.append(f"{geo} {name}")
                values.append(hit[0]["value"])
    return [
        {
            "id": "eurostat-unmet-need-quintile",
            "title": f"Unmet need for medical examination (cost, distance or waiting list), by income fifth, {year} (%)",
            "type": "bar",
            "labels": labels,
            "values": values,
            "source": SOURCE_CITES[sid],
            "geography": "Country (national context only, not city)",
            "date": f"{year}; collected {collected_at(fetch_status, sid)}",
            "note": "Self-reported, people 16+. National figures: they do not describe any single city.",
        }
    ]


def gap_lines(processed: Path, fetch_status: dict[str, Any]) -> list[str]:
    lines = []
    for sid, entry in sorted((fetch_status.get("sources") or {}).items()):
        if sid.startswith("example-"):
            continue
        if entry.get("skipped") == "disabled":
            lines.append(f"{sid}: not collected (source disabled).")
        elif entry.get("last_error") and not entry.get("last_success"):
            lines.append(f"{sid}: never collected (last error: {entry['last_error']}).")
        elif entry.get("last_error"):
            lines.append(f"{sid}: last fetch failed; showing data collected {entry.get('last_success')}.")
        missing = [r for r in load_rows(processed, sid) if r.get("value") is None]
        if missing:
            sample = sorted({f"{r.get('geo_name')} {r.get('breakdown') if sid.startswith('eurostat') else r.get('measure_id')} {r.get('period') if sid.startswith('eurostat') else ''}".strip() for r in missing})[:6]
            lines.append(f"{sid}: {len(missing)} cells blank in source (e.g. {'; '.join(sample)}).")
    return lines


def instance_sections(processed: Path, fetch_status: dict[str, Any], input_fresh_at: str | None, stale: bool) -> list[dict[str, Any]]:
    gaps = gap_lines(processed, fetch_status)
    fresh = input_fresh_at or "never"
    loaded = []
    if load_rows(processed, "cdc-places-place-2025"):
        loaded.append("CDC PLACES for US cities")
    if any(r.get("value") is not None for r in load_rows(processed, "eurostat-hlth-silc-08")):
        loaded.append("Eurostat EU-SILC national context")
    loaded_text = "; ".join(loaded) if loaded else "none yet"
    return [
        {
            "id": "overview",
            "title": "Overview",
            "body": (
                "Poverty and health in US and European cities over 2 million people. "
                f"Data collected: {fresh}{' (STALE)' if stale else ''}. "
                f"Loaded: {loaded_text}. Health and access measures only so far. "
                "No poverty-vs-health comparison is shown until poverty-side data is loaded. "
                + PUBLICATION_STATUS
            ),
        },
        {
            "id": "city-comparisons",
            "title": "City comparisons",
            "body": (
                "US cities: CDC PLACES, city proper, age-adjusted model estimates with 95% CI. "
                "European cities: no city-level data yet (Eurostat urb_* disabled). "
                "Bars compare cities within one source and one definition only. Correlation is not causation."
            ),
        },
        {
            "id": "news-signals",
            "title": "News signals",
            "body": "Not wired yet. Scout news items are signals, not evidence, and are not shown as data.",
        },
        {
            "id": "data-gaps",
            "title": "Data gaps and method notes",
            "body": " ".join(gaps) if gaps else "No gaps recorded by the pipeline.",
        },
    ]


def resolve_input_fresh_at(summary: dict[str, Any], fetch_status: dict[str, Any]) -> str | None:
    if summary.get("input_fresh_at"):
        return summary["input_fresh_at"]
    # Fall back: oldest last_success among sources named in the summary.
    # Do NOT use transform clock (`updated_at`) — that would fake freshness.
    times: list[str] = []
    sources = fetch_status.get("sources") or {}
    wanted = summary.get("sources") or list(sources.keys())
    for sid in wanted:
        entry = sources.get(sid) or {}
        if entry.get("last_success"):
            times.append(entry["last_success"])
    if times:
        return min(times)
    return None


def is_stale(stamp: str | None, stale_hours: float) -> bool:
    if not stamp:
        return True
    try:
        then = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
        age_h = (datetime.now(timezone.utc) - then.astimezone(timezone.utc)).total_seconds() / 3600.0
        return age_h > stale_hours
    except (TypeError, ValueError):
        return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build dashboard JSON under docs/data/")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument(
        "--stale-hours",
        type=float,
        default=48.0,
        help="Mark dashboard stale if input freshness older than this many hours",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()
    processed = root / "data" / "processed"
    out_dir = root / "docs" / "data"
    out_dir.mkdir(parents=True, exist_ok=True)

    summary = load_summary(processed)
    fetch_status = load_fetch_status(root)
    series = build_series(processed)
    input_fresh_at = resolve_input_fresh_at(summary, fetch_status)
    row_count = int(summary.get("row_count") or 0)
    # last_updated reflects observation freshness, not transform/build clock.
    # Empty / never-collected instances stay null + stale (honest "no data yet").
    if input_fresh_at:
        last_updated = input_fresh_at
        built_at = utc_now()
        stale = is_stale(input_fresh_at, args.stale_hours)
    else:
        last_updated = None
        built_at = None if row_count == 0 else utc_now()
        stale = True

    dashboard = {
        "title": "MEL dashboard",
        "last_updated": last_updated,
        "built_at": built_at,
        "input_fresh_at": input_fresh_at,
        "stale": stale,
        "stale_after_hours": args.stale_hours,
        "summary": {
            "row_count": row_count,
            "sources": summary.get("sources", []),
        },
        "publication_status": PUBLICATION_STATUS,
        "sections": instance_sections(processed, fetch_status, input_fresh_at, stale),
        "charts": city_charts(processed, fetch_status)
        + national_charts(processed, fetch_status)
        + [
            {
                "id": "rows-by-source",
                "title": "Pipeline check: processed rows by source",
                "type": "bar",
                "labels": [s["label"] for s in series],
                "values": [s["value"] for s in series],
            }
        ],
    }

    out_path = out_dir / "dashboard.json"
    out_path.write_text(json.dumps(dashboard, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
