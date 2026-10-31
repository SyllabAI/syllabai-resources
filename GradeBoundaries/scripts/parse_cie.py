#!/usr/bin/env python3
"""Parse Cambridge International grade-threshold PDFs.

Two tables per document:
  - "Component grade thresholds": per-component minimum raw marks (some
    routes are A*–G, some 9–1; the '-' column pattern marks grades a
    component cannot award).
  - "Syllabus grade thresholds": per-route (component combination) weighted
    thresholds — the real grade ladder for the qualification.

AS & A Level documents carry three award sections under "Syllabus grade
thresholds": Cambridge International A Level (linear assessment), A Level
(staged assessment, carry-forward combinations like 31+41+87) and
Cambridge International AS Level (lowercase a–e ladder). Each route row is
tagged with the award section it was parsed from, so the hub can serve the
right ladder per course level; IGCSE documents have no section header and
tag routes with award=null.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from gb_common import (PARSED, RAW, fail, manifest_lookup, monotonic_ok,
                       norm_ws, now_utc, parse_value_tokens,
                       pdftotext_layout)

GRADE_TOKEN_RE = re.compile(r"A\*|[A-G]|\d-\d|9|[1-8]|U", re.IGNORECASE)
A_STAR_LIKE = re.compile(r"A\*|\d-\d")


def vals_ok(vals: list[str]) -> bool:
    return all(re.fullmatch(r"\d{1,4}|[\u2013\u2014\-*.,]", v) for v in vals)


def ladder_tail(toks: list[str]) -> list[str] | None:
    """Trailing run of grade labels on a header line (case-insensitive).

    A header's tail is either the whole line (bare ladder like
    '9 8 7 6 5 4 3 2 1 U') or is preceded by a word containing letters
    ('Maximum weighted mark  A* A B .. G').  A DATA row's tail is preceded
    by another number ('Component 43  40  20 15 11 9 8 7 6'), which must
    NOT be mistaken for a ladder — that is the guard below.
    """
    tail: list[str] = []
    for t in reversed(toks):
        if GRADE_TOKEN_RE.fullmatch(t):
            tail.insert(0, t.upper() if not t.isdigit() else t)
        else:
            break
    if len(tail) < 4:
        return None
    if len(tail) == len(toks):
        return tail                      # bare ladder line
    head = toks[:len(toks) - len(tail)]
    if re.search(r"[A-Za-z\u2013\u2014]", head[-1]):
        return tail                      # '… mark  A* A B C D E'
    return None                          # numbers before tail → data row


def parse_cie_pdf(pdf: Path) -> dict:
    lines = pdftotext_layout(pdf)
    joined = "\n".join(lines)
    m = re.search(r"syllabus\s+(\d{4})", joined, re.I)
    code = m.group(1) if m else pdf.parent.name
    sm = re.search(r"syllabus\s+\d{4}\s*\(([^)]+)\)", joined, re.I)
    title = sm.group(1).strip() if sm else code
    sesm = re.search(r"(June|January|March|November)\s+(\d{4})", joined)
    session = f"{sesm.group(1)} {sesm.group(2)}" if sesm else pdf.stem

    components: list[dict] = []
    routes: list[dict] = []
    warns: list[str] = []
    ladder: list[str] | None = None
    mode: str | None = None        # components | routes
    award: str | None = None       # A-Level-linear | A-Level-staged | AS

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line.strip():
            continue
        low = line.lower()
        if "component grade thresholds" in low \
                or "minimum raw mark required for grade" in low:
            mode = "components"
            award = None
            ladder = None
            continue
        if "syllabus grade thresholds" in low \
                or "overall thresholds" in low:
            mode = "routes"
            award = None
            ladder = None
            continue
        if mode == "routes":
            # award-section headers (AS & A Level documents only). Exact
            # standalone lines — the page-2 syllabus title line (e.g.
            # 'Cambridge International AS Level Environmental Management
            # (8291)') must not fire these.
            stripped = line.strip()
            if stripped == "Cambridge International A Level (linear assessment)":
                award = "A-Level-linear"
                ladder = None
                continue
            if stripped == "Cambridge International A Level (staged assessment)":
                award = "A-Level-staged"
                ladder = None
                continue
            if stripped == "Cambridge International AS Level":
                award = "AS"
                ladder = None
                continue
        n = norm_ws(line)
        toks = n.split()
        tail = ladder_tail(toks)
        if tail:
            ladder = tail
            continue
        if mode == "components" and ladder:
            m = re.match(r"^(Component\s+\d+)\s+(\d+)\s+(\S.*)$", n)
            if m:
                boundaries, w = parse_value_tokens(m.group(3), ladder)
                warns += [f"{m.group(1)}: {x}" for x in w]
                if boundaries:
                    components.append({
                        "code": m.group(1).replace("Component ", ""),
                        "title": f"Component {m.group(1).split()[-1]}",
                        "maxMark": int(m.group(2)),
                        "boundaries": boundaries,
                        "ok": monotonic_ok(boundaries, ladder),
                    })
                continue
        if mode == "routes" and ladder:
            vals_n = len(ladder)
            if len(toks) < vals_n + 2:
                continue
            # shapes: [<Option>] <combo digits/commas…> <maxWeighted> <vals…>
            head = toks[:-vals_n]
            if not re.fullmatch(r"\d{1,5}", head[-1]):
                continue
            try:
                max_mark = int(head[-1])
            except ValueError:
                continue
            combo_toks = head[:-1]
            opt: list[str] = []
            while combo_toks and not re.fullmatch(r"[\d,]+", combo_toks[0]):
                opt.append(combo_toks.pop(0))
            option = " ".join(opt) or None
            combo_raw = "".join(combo_toks)
            vals = toks[-vals_n:]
            if not re.fullmatch(r"[\d,]+", combo_raw) or not vals_ok(vals):
                continue
            combo = re.sub(r"[,\s]+", "+", combo_raw.strip(",")).rstrip("+")
            if not combo:
                continue
            boundaries, w = parse_value_tokens(" ".join(vals), ladder)
            warns += [f"route {combo}: {x}" for x in w]
            if boundaries:
                # Award inference for documents WITHOUT explicit award
                # sections (2025-and-earlier AS & A Level format prints one
                # combined options table; AS routes carry '–' under A*).
                # Never applied to IGCSE documents (0xxx) where A* is a
                # real grade and tier-capped routes print '–' under A*.
                row_award = award
                if row_award is None and code[0] in "89":
                    if not A_STAR_LIKE.fullmatch(ladder[0]):
                        row_award = "AS"   # ladder has no A* grade: AS award
                    elif boundaries.get("A*") is None:
                        row_award = "AS"   # A* column present but '–'
                    else:
                        row_award = "A-Level"
                routes.append({
                    "combination": combo,
                    "option": option,
                    "maxWeightedMark": max_mark,
                    "boundaries": boundaries,
                    "award": row_award,
                    "ok": monotonic_ok(boundaries, ladder),
                })
            continue

    for c in components + routes:
        if not c.get("ok", False):
            warns.append(f"non-monotonic ladder: {c}")

    return {
        "schema": "syllabai.grade-boundaries.source/1",
        "family": f"cie-{code}",
        "session": session,
        "syllabus": {"code": code, "title": title},
        "source": {},
        "components": components,
        "routes": routes,
        "gradeLadder": ladder,
        "parse_warnings": warns,
        "parsed_at": now_utc(),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--codes", nargs="*", help="syllabus codes subset")
    args = ap.parse_args()
    total = 0
    for code_dir in sorted((RAW / "cie").glob("0*")) + \
            sorted((RAW / "cie").glob("8*")) + \
            sorted((RAW / "cie").glob("9*")):
        code = code_dir.name
        if args.codes and code not in args.codes:
            continue
        out_dir = PARSED / "cie" / code
        out_dir.mkdir(parents=True, exist_ok=True)
        for pdf in sorted(code_dir.glob("*.pdf")):
            doc = parse_cie_pdf(pdf)
            meta = manifest_lookup(f"cie-{code}", pdf.stem) or {}
            doc["source"] = {
                "url": meta.get("url"),
                "file": meta.get("file", str(pdf.relative_to(RAW.parent))),
                "sha256": meta.get("sha256"),
                "fetched_at": meta.get("fetched_at"),
            }
            (out_dir / f"{pdf.stem}.json").write_text(
                json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
            total += 1
            print(f"cie {code} {pdf.stem}: {len(doc['components'])} components, "
                  f"{len(doc['routes'])} routes, {len(doc['parse_warnings'])} warns")
    print(f"CIE PARSED {total} docs")
    sys.exit(0 if total > 0 else 2)


if __name__ == "__main__":
    main()
