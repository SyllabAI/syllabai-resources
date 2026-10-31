#!/usr/bin/env python3
"""Parse Cambridge International grade-threshold PDFs.

Two tables per document:
  - "Component grade thresholds": per-component minimum raw marks (some
    routes are A*–G, some 9–1; the '-' column pattern marks grades a
    component cannot award).
  - "Syllabus grade thresholds": per-route (component combination) weighted
    thresholds — the real grade ladder for the qualification.
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

GRADE_TOKENS_9_1 = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
GRADE_TOKENS_A_STAR = ["A*", "A", "B", "C", "D", "E", "F", "G"]


def vals_ok(vals: list[str]) -> bool:
    return all(re.fullmatch(r"\d{1,4}|[\u2013\u2014\-*.,]", v) for v in vals)


def sniff_ladder(header_tail: str) -> list[str] | None:
    toks = header_tail.split()
    letters = [t for t in toks if re.fullmatch(r"A\*|[A-G]|9|[1-8]", t)]
    if len(letters) >= 5:
        return [t.upper() if not t.isdigit() else t for t in letters]
    return None


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
    mode: str | None = None       # components | routes

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line.strip():
            continue
        low = line.lower()
        if "component grade thresholds" in low \
                or "minimum raw mark required for grade" in low:
            mode = "components"
            continue
        if "syllabus grade thresholds" in low \
                or "overall thresholds" in low:
            mode = "routes"
            continue
        n = norm_ws(line)
        # a ladder header line: CIE prints the ladder as a trailing run of
        # grade labels, sometimes after a prefix word ('Component  A B .. G',
        # 'weighted  A* A B .. G', or a bare '9 8 .. 1 U' line)
        toks = n.split()
        tail: list[str] = []
        for t in reversed(toks):
            if re.fullmatch(r"A\*|[A-G]|9|[1-8]|U", t):
                tail.insert(0, t.upper() if not t.isdigit() else t)
            else:
                break
        if len(tail) >= 4:
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
            # route rows come in two shapes:
            #   2026+ : <combo digits/commas> <maxWeighted> <values…>
            #   2025- : <Option code> <maxWeighted> <combo digits/commas> <values…>
            vals_n = len(ladder)
            vals = toks[-vals_n:]
            if len(toks) < vals_n + 2:
                continue
            if re.fullmatch(r"[\d,]+", toks[0]):
                max_i = len(toks) - vals_n - 1
                try:
                    max_mark = int(toks[max_i])
                except ValueError:
                    continue
                combo_toks = toks[:max_i]
                option = None
            elif toks[1].isdigit() and len(toks) >= vals_n + 3:
                option = toks[0]
                max_mark = int(toks[1])
                combo_toks = toks[2:len(toks) - vals_n]
            else:
                continue
            combo_raw = "".join(combo_toks)
            if not re.fullmatch(r"[\d,]+", combo_raw) or not vals_ok(vals):
                continue
            combo = re.sub(r"[,\s]+", "+", combo_raw.strip(",")).rstrip("+")
            if not combo:
                continue
            boundaries, w = parse_value_tokens(" ".join(vals), ladder)
            warns += [f"route {combo}: {x}" for x in w]
            if boundaries:
                routes.append({
                    "combination": combo,
                    "option": option,
                    "maxWeightedMark": max_mark,
                    "boundaries": boundaries,
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
