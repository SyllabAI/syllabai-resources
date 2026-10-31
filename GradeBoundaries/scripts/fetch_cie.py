#!/usr/bin/env python3
"""Fetch Cambridge International grade-threshold PDFs (known-ID registry).

CIE serves per-syllabus threshold tables at unguessable /Images/<id>-... URLs
and renders its listing pages client-side, so mechanical crawling is not
possible today. This fetcher runs on a curated ID registry below (each entry
verified by downloading + checking the syllabus number inside the parsed
text). New sessions/syllabi land by extending CIE_IDS — the discovery recipe
(search `cambridgeinternational.org Images <subject>-<code>-<session>
grade-threshold-table`) is documented in GradeBoundaries/README.md.
"""
from __future__ import annotations

import argparse
import json
import re

from gb_common import (RAW, http_get, manifest_append, manifest_lookup,
                       now_utc, pdf_ok, session_slug, sha256_bytes)

BASE = "https://www.cambridgeinternational.org/Images"

# syllabus -> session -> (document id, url filename). CIE serves documents
# only under their full published name; the id alone 404s.
CIE_IDS: dict[str, dict[str, tuple[int, str]]] = {
    "0620": {  # Chemistry IGCSE
        "June 2025": (741360, "741360-chemistry-0620-june-2025-grade-threshold-table.pdf"),
        "June 2026": (762856, "762856-chemistry-0620-june-2026-grade-threshold-table.pdf"),
    },
    "0625": {  # Physics IGCSE
        "June 2024": (716106, "716106-physics-0625-june-2024-grade-threshold-table.pdf"),
        "June 2026": (762857, "762857-physics-0625-june-2026-grade-threshold-table.pdf"),
    },
    "0580": {  # Mathematics (without coursework) IGCSE
        "June 2025": (741420, "741420-mathematics-without-coursework-0580-june-2025-grade-threshold-table.pdf"),
        "June 2026": (762852, "762852-mathematics-without-coursework-0580-june-2026-grade-threshold-table.pdf"),
    },
    "9609": {  # Business IAL
        "June 2026": (761507, "761507-business-9609-june-2026-grade-threshold-table.pdf"),
    },
    "9700": {  # Biology IAL
        "June 2026": (761524, "761524-biology-9700-june-2026-grade-threshold-table.pdf"),
    },
    "9701": {  # Chemistry IAL
        "June 2026": (761525, "761525-chemistry-9701-june-2026-grade-threshold-table.pdf"),
    },
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    ok = 0
    for code, sessions in sorted(CIE_IDS.items()):
        out_dir = RAW / "cie" / code
        out_dir.mkdir(parents=True, exist_ok=True)
        for session, (doc_id, fname) in sorted(sessions.items()):
            dest = out_dir / f"{session}.pdf"
            if dest.exists() and not args.force and manifest_lookup(
                    f"cie-{code}", session):
                ok += 1
                print(f"cie {code} {session}: cached")
                continue
            url = f"{BASE}/{fname}"
            http_code, body, final = http_get(url)
            if http_code == 200 and pdf_ok(body):
                dest.write_bytes(body)
                manifest_append(f"cie-{code}", session, url, final,
                                sha256_bytes(body), len(body))
                ok += 1
                print(f"cie {code} {session}: fetched {len(body)} bytes")
            else:
                print(f"cie {code} {session}: MISSING (http {http_code})")
    print(f"CIE TOTAL {ok} docs")
    (RAW / "cie" / "ID-REGISTRY.json").write_text(json.dumps(
        {"generated": now_utc(), "ids": CIE_IDS}, indent=2))


if __name__ == "__main__":
    main()
