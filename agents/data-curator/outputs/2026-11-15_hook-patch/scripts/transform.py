#!/usr/bin/env python3
"""Example transform: data/raw -> data/processed.

Generic starter. Offline-safe: if there is no raw input, writes/keeps an
empty summary and exits 0.

---------------------------------------------------------------------------
CUSTOMISE PER INSTANCE (hook)
---------------------------------------------------------------------------
Edit `customise_row()` and/or `transform_source()` below for your mandate's
schemas. Keep outputs plain CSV or JSON under data/processed/.
---------------------------------------------------------------------------

Usage:
  python scripts/transform.py
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _parse_iso(ts: str) -> datetime | None:
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def derive_input_fresh_at(root: Path, source_ids: list[str]) -> str | None:
    """Oldest successful collection time among contributing sources.

    Re-running transform on cached raw snapshots must not look "fresh". Prefer
    `data/fetch_status.json` last_success values; fall back to raw file mtimes.
    """
    times: list[datetime] = []
    status_path = root / "data" / "fetch_status.json"
    status_sources: dict[str, Any] = {}
    if status_path.exists():
        try:
            status = json.loads(status_path.read_text(encoding="utf-8"))
            status_sources = status.get("sources") or {}
        except json.JSONDecodeError:
            status_sources = {}

    ids = source_ids or list(status_sources.keys())
    for sid in ids:
        entry = status_sources.get(sid) or {}
        parsed = _parse_iso(entry["last_success"]) if entry.get("last_success") else None
        if parsed:
            times.append(parsed)
            continue
        source_dir = root / "data" / "raw" / sid
        if not source_dir.is_dir():
            continue
        candidates = list(source_dir.glob("latest.*")) + list(source_dir.glob("*"))
        files = [p for p in candidates if p.is_file()]
        if not files:
            continue
        newest = max(files, key=lambda p: p.stat().st_mtime)
        times.append(datetime.fromtimestamp(newest.stat().st_mtime, tz=timezone.utc))

    if not times:
        return None
    oldest = min(times)
    return oldest.replace(microsecond=0).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# Instance hooks (MEL poverty-health). Drafted by data-curator 2026-11-15,
# per board lead-to-curator 001. Tidy long rows share TIDY_FIELDS; sources
# without a hook keep the generic one-row-per-record `payload` shape.
# ---------------------------------------------------------------------------

TIDY_FIELDS = [
    "source_id",
    "geo_code",
    "geo_name",
    "geo_level",
    "measure_id",
    "measure_label",
    "breakdown",
    "period",
    "value",
    "ci95_low",
    "ci95_high",
    "unit",
    "status",
    "payload",
]

# CDC PLACES measures fetched by sources.yml. Labels are curator wording from the
# PLACES measure definitions; check them against the PLACES data dictionary.
CDC_PLACES_MEASURES = {
    "diabetes": "Diagnosed diabetes, adults 18+ (%)",
    "depression": "Depression, adults 18+ (%)",
    "access2": "No health insurance, adults 18-64 (%)",
    "foodinsecu": "Food insecurity in past 12 months, adults 18+ (%)",
    "housinsecu": "Housing insecurity in past 12 months, adults 18+ (%)",
}

# Fallback names when `locationname` is absent (2026-11-13 snapshot: `placename`
# held the FIPS code). Keys are 7-digit place FIPS.
CDC_PLACE_NAMES = {
    "0644000": "Los Angeles",
    "1714000": "Chicago",
    "3651000": "New York City",
    "4835000": "Houston",
}


def _num(text: Any) -> float | None:
    if text is None:
        return None
    t = str(text).strip()
    if t == "":
        return None
    try:
        return float(t)
    except ValueError:
        return None


def _parse_ci(text: Any) -> tuple[float | None, float | None]:
    """'( 9.8, 11.4)' -> (9.8, 11.4); blank -> (None, None)."""
    if not text:
        return None, None
    parts = str(text).strip().strip("()").split(",")
    if len(parts) != 2:
        return None, None
    return _num(parts[0]), _num(parts[1])


def cdc_places_rows(source_id: str, row: dict[str, Any]) -> list[dict[str, Any]]:
    fips = str(row.get("placefips") or "").strip()
    if fips.isdigit():
        fips = fips.zfill(7)
    name = str(row.get("locationname") or "").strip()
    if not name or name.isdigit():
        name = CDC_PLACE_NAMES.get(fips, "") or str(row.get("placename") or "").strip()
    state = str(row.get("stateabbr") or "").strip()
    out = []
    for mid, label in CDC_PLACES_MEASURES.items():
        col = f"{mid}_adjprev"
        if col not in row:
            continue  # measure not requested in this snapshot
        value = _num(row.get(col))
        lo, hi = _parse_ci(row.get(f"{mid}_adj95ci"))
        out.append(
            {
                "source_id": source_id,
                "geo_code": fips,
                "geo_name": f"{name}, {state}" if state else name,
                "geo_level": "US Census place (city proper)",
                "measure_id": mid,
                "measure_label": label,
                "breakdown": "age-adjusted",
                "period": "PLACES 2025 release",
                "value": value,
                "ci95_low": lo,
                "ci95_high": hi,
                "unit": "percent",
                "status": "ok" if value is not None else "missing_in_source",
                "payload": "",
            }
        )
    return out


def is_jsonstat(payload: Any) -> bool:
    return (
        isinstance(payload, dict)
        and isinstance(payload.get("id"), list)
        and isinstance(payload.get("size"), list)
        and isinstance(payload.get("dimension"), dict)
        and "value" in payload
    )


JSONSTAT_MAX_CELLS = 50_000  # above this, emit only cells that have a value


def jsonstat_rows(source_id: str, ds: dict[str, Any]) -> list[dict[str, Any]]:
    """Flatten a JSON-stat 2.0 dataset (Eurostat API) to long rows.

    Cells absent from the sparse `value` object are emitted with
    status=missing_in_source so gaps stay visible (small datasets only).
    Eurostat cell flags (e.g. b = break, u = low reliability) go in `status`.
    """
    ids: list[str] = ds["id"]
    sizes: list[int] = [int(n) for n in ds["size"]]
    dims = ds["dimension"]
    codes: list[list[str]] = []
    labels: list[dict[str, str]] = []
    for d in ids:
        cat = (dims.get(d) or {}).get("category") or {}
        index = cat.get("index")
        if isinstance(index, dict):
            ordered = [c for c, _ in sorted(index.items(), key=lambda kv: kv[1])]
        elif isinstance(index, list):
            ordered = list(index)
        else:
            ordered = list((cat.get("label") or {}).keys())
        codes.append(ordered)
        labels.append(cat.get("label") or {})

    values = ds.get("value")
    if isinstance(values, list):
        values = {str(i): v for i, v in enumerate(values) if v is not None}
    values = {str(k): v for k, v in (values or {}).items()}
    status = ds.get("status") or {}
    if isinstance(status, list):
        status = {str(i): v for i, v in enumerate(status) if v}
    status = {str(k): v for k, v in status.items()}

    total = 1
    for n in sizes:
        total *= n
    strides = [1] * len(sizes)
    for i in range(len(sizes) - 2, -1, -1):
        strides[i] = strides[i + 1] * sizes[i + 1]

    geo_dim = "geo" if "geo" in ids else None
    time_dim = "time" if "time" in ids else None
    dataset = str(ds.get("extension", {}).get("id") or source_id)
    level = "country (national context, not city)" if "silc" in source_id else "as labelled by Eurostat"

    cells = range(total) if total <= JSONSTAT_MAX_CELLS else sorted(int(k) for k in values)
    out = []
    for flat in cells:
        pos = [(flat // strides[i]) % sizes[i] for i in range(len(sizes))]
        coord = {ids[i]: codes[i][pos[i]] for i in range(len(ids))}
        varying = [
            f"{d}={coord[d]}"
            for i, d in enumerate(ids)
            if sizes[i] > 1 and d not in (geo_dim, time_dim)
        ]
        fixed = [f"{d}={coord[d]}" for i, d in enumerate(ids) if sizes[i] == 1 and d not in (geo_dim, time_dim)]
        value = values.get(str(flat))
        flag = status.get(str(flat), "")
        if value is None:
            st = "missing_in_source" + (f":{flag}" if flag else "")
        else:
            st = "ok" + (f":{flag}" if flag else "")
        geo = coord.get(geo_dim, "") if geo_dim else ""
        out.append(
            {
                "source_id": source_id,
                "geo_code": geo,
                "geo_name": labels[ids.index(geo_dim)].get(geo, geo) if geo_dim else "",
                "geo_level": level,
                "measure_id": dataset + (";" + ";".join(fixed) if fixed else ""),
                "measure_label": str(ds.get("label") or dataset),
                "breakdown": ";".join(varying),
                "period": coord.get(time_dim, "") if time_dim else "",
                "value": value,
                "ci95_low": None,
                "ci95_high": None,
                "unit": coord.get("unit", ""),
                "status": st,
                "payload": "",
            }
        )
    return out


def customise_row(source_id: str, row: dict[str, Any]) -> dict[str, Any] | list[dict[str, Any]] | None:
    """CUSTOMISE PER INSTANCE: map a raw record to processed row(s), or None to drop.

    May return one dict, a list of dicts (long format), or None.
    Default: keep a shallow JSON object as a single 'payload' column plus source id.
    """
    if source_id.startswith("cdc-places-"):
        return cdc_places_rows(source_id, row)
    return {
        "source_id": source_id,
        "payload": json.dumps(row, ensure_ascii=False) if not isinstance(row, str) else row,
    }


def load_latest_raw(source_dir: Path) -> tuple[str, Any] | None:
    for name in ("latest.json", "latest.csv"):
        path = source_dir / name
        if path.exists():
            text = path.read_text(encoding="utf-8")
            if name.endswith(".json"):
                return "json", json.loads(text)
            return "csv", text
    # Fall back to newest timestamped file
    files = sorted(source_dir.glob("*.json")) + sorted(source_dir.glob("*.csv"))
    if not files:
        return None
    path = files[-1]
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        return "json", json.loads(text)
    return "csv", text


def iter_records(fmt: str, payload: Any) -> list[Any]:
    if fmt == "json":
        if isinstance(payload, list):
            return payload
        if isinstance(payload, dict):
            for key in ("data", "results", "items", "records"):
                if isinstance(payload.get(key), list):
                    return payload[key]
            return [payload]
        return [{"value": payload}]
    # csv
    reader = csv.DictReader(payload.splitlines())
    return list(reader)


def world_bank_rows(payload: Any) -> list[Any] | None:
    """Detect World Bank API shape: [meta, [rows...]]."""
    if isinstance(payload, list) and len(payload) == 2 and isinstance(payload[1], list):
        return payload[1]
    return None


def transform_source(source_id: str, source_dir: Path) -> list[dict[str, Any]]:
    loaded = load_latest_raw(source_dir)
    if not loaded:
        return []
    fmt, payload = loaded
    if fmt == "json" and is_jsonstat(payload):
        return jsonstat_rows(source_id, payload)
    wb = world_bank_rows(payload) if fmt == "json" else None
    if wb is not None:
        records = wb
    else:
        records = iter_records(fmt, payload)
    out: list[dict[str, Any]] = []
    for rec in records:
        if isinstance(rec, dict):
            row = customise_row(source_id, rec)
        else:
            row = customise_row(source_id, {"value": rec})
        if isinstance(row, list):
            out.extend(r for r in row if r)
        elif row:
            out.append(row)
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Transform raw snapshots to data/processed/")
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args(argv)
    root = args.root.resolve()
    raw_root = root / "data" / "raw"
    processed = root / "data" / "processed"
    processed.mkdir(parents=True, exist_ok=True)

    all_rows: list[dict[str, Any]] = []
    if raw_root.exists():
        for source_dir in sorted(p for p in raw_root.iterdir() if p.is_dir()):
            rows = transform_source(source_dir.name, source_dir)
            all_rows.extend(rows)
            out_json = processed / f"{source_dir.name}.json"
            out_json.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")

    source_ids = sorted({r.get("source_id") for r in all_rows if r.get("source_id")})
    summary = {
        "updated_at": utc_now(),  # when this transform ran (not evidence of fresh inputs)
        "input_fresh_at": derive_input_fresh_at(root, source_ids),
        "row_count": len(all_rows),
        "sources": source_ids,
        "row_counts": {sid: sum(1 for r in all_rows if r.get("source_id") == sid) for sid in source_ids},
    }
    (processed / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    # Flat CSV for spreadsheet use. Field list = TIDY_FIELDS plus any extra keys a
    # hook adds, so a new hook can never crash the writer (DictWriter raises on
    # unknown keys). Generic rows simply leave tidy columns blank.
    fieldnames = list(TIDY_FIELDS)
    for row in all_rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    csv_path = processed / "all_rows.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, restval="", extrasaction="ignore")
        writer.writeheader()
        for row in all_rows:
            writer.writerow({k: ("" if v is None else v) for k, v in row.items()})

    print(f"Wrote {len(all_rows)} rows -> {processed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
