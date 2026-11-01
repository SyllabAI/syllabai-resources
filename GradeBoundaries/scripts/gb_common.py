#!/usr/bin/env python3
"""GradeBoundaries lane — shared constants + helpers.

Provenance law: every downloaded artifact lands under raw/<family>/<Session>.pdf
with a MANIFEST.jsonl row (url, sha256, bytes, fetched_at, final_url). Re-runs
are idempotent — a file with a recorded sha256 is skipped unless --force.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent          # GradeBoundaries/
RAW = LANE / "raw"
PARSED = LANE / "parsed"
CURATED = LANE / "curated"
HUB_IMPORT = LANE / "hub-import" / "grade-boundaries-1.0"
MAPPING = LANE / "mapping"
MANIFEST = RAW / "MANIFEST.jsonl"

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")

# ---------------------------------------------------------------- sessions --
# The exam sessions any Pearson international boundary doc may exist for.
# Covid-era gaps (Jun 2020/2021 international) simply 404 and are recorded
# as unavailable in the fetch report — absence is data too.
MONTHS = ["january", "june", "october", "november"]
YEARS = list(range(2019, 2027))


def session_list() -> list[str]:
    """['June 2026', 'January 2026', ...] newest-first."""
    out = []
    for y in sorted(YEARS, reverse=True):
        for m in MONTHS:
            out.append(f"{m.capitalize()} {y}")
    return out


def session_slug(session: str) -> str:
    """'January 2023' -> 'january-2023'"""
    m, y = session.split()
    return f"{m.lower()}-{y}"


def session_year(session: str) -> int:
    return int(session.split()[-1])


# ------------------------------------------------------------------ fetch ---
def http_get(url: str, timeout: int = 60) -> tuple[int, bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read(), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, b"", url
    except Exception:
        return 0, b"", url


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def manifest_append(family: str, session: str, url: str,
                    final_url: str, sha: str, size: int) -> None:
    row = {
        "family": family,
        "session": session,
        "file": f"raw/{family}/{session}.pdf",
        "url": url,
        "final_url": final_url,
        "sha256": sha,
        "bytes": size,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    lines = MANIFEST.read_text().splitlines() if MANIFEST.exists() else []
    lines = [ln for ln in lines
             if json.loads(ln).get("file") != row["file"]]
    lines.append(json.dumps(row, sort_keys=True))
    MANIFEST.write_text("\n".join(lines) + "\n")


def manifest_lookup(family: str, session: str) -> dict | None:
    if not MANIFEST.exists():
        return None
    want = f"raw/{family}/{session}.pdf"
    for ln in MANIFEST.read_text().splitlines():
        try:
            row = json.loads(ln)
        except json.JSONDecodeError:
            continue
        if row.get("file") == want:
            return row
    return None


def pdf_ok(b: bytes) -> bool:
    """A real boundary PDF starts with %PDF — the Pearson 404 page does not."""
    return b[:4] == b"%PDF"


# ------------------------------------------------------------------ parse ---
def pdftotext_layout(pdf: Path) -> list[str]:
    """pdftotext -layout lines (layout mode keeps the 2-D column geometry)."""
    out = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        capture_output=True, check=True)
    text = out.stdout.decode("utf-8", "replace")
    return text.splitlines()


def norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


NUM_TOKEN = re.compile(r"^\d{1,4}$")
DASH_TOKEN = re.compile(r"^[\u2013\u2014\-*.,]$")


def parse_value_tokens(tail: str, ladder: list[str]) -> tuple[dict, list[str]]:
    """Parse the trailing value columns of a boundary row against the ladder.

    Returns (boundaries, warnings). Tokens: ints, or dashes for 'not
    available' (greyed rows — unit not offered / nobody sat it), mapped to None.
    """
    tokens = tail.split()
    values: list[int | None] = []
    warns: list[str] = []
    for t in tokens:
        if NUM_TOKEN.match(t):
            values.append(int(t))
        elif DASH_TOKEN.match(t):
            values.append(None)
        else:
            warns.append(f"unparseable value token {t!r}")
    if not values or len(values) != len(ladder):
        warns.append(
            f"column count {len(values)} != ladder {len(ladder)} "
            f"(starts {ladder[:3]}); row tail={tail[:60]!r}")
        return {}, warns
    return {g: v for g, v in zip(ladder, values)}, warns


def monotonic_ok(boundaries: dict, ladder: list[str]) -> bool:
    vals = [boundaries.get(g) for g in ladder if boundaries.get(g) is not None]
    return all(a >= b for a, b in zip(vals, vals[1:]))


def fail(msg: str, code: int = 1) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(code)


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
