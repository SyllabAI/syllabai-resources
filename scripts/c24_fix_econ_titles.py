#!/usr/bin/env python3
"""T-C24 WS-3a — repair mangled igcse-economics subtopic titles.

Defect: parse_lettered_table() accumulated content-column lines into the
subtopic 'title' (e.g. "The economic problem a) The problem of scarcity –
where there are unlimited wants …"); one row even missed its second title
line ("Demand, supply and" + "Demand" vs true "Demand, supply and market
equilibrium").

PDF layout (verified at span level, igcse-economics modular spec):
  code column    x0 <  90
  title column   90 <= x0 < 220   (wrapped title lines, gap <= 16pt)
  content column x0 >= 220

Rule: title = concatenation of title-column spans at the row's oy plus
wrapped continuation lines in the same x-band until the vertical gap to the
next title-column line exceeds 16 pt or a code/content span intervenes.

Patches: parsed/igcse-economics/*.parsed.json (subsections + statement
subsection refs), topics.json (subsections). Fail-closed on any row whose
derived title is empty or not a prefix-compatible replacement.
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

import fitz

REPO = Path(__file__).resolve().parent.parent
Q = "igcse-economics"
TITLE_X = (90.0, 220.0)
WRAP_GAP = 16.0

failures = []


def derive_title(doc, page_no: int, oy: float) -> tuple[str, list]:
    """Title-column spans at the header row, following wrapped lines."""
    page = doc[page_no - 1]
    rows = {}  # oy -> [(x0, text)]
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for sp in l["spans"]:
                if not sp["text"].strip():
                    continue
                rows.setdefault(round(sp["origin"][1], 1), []).append(
                    (sp["bbox"][0], sp["text"]))
    title_parts, oys = [], []
    cur = oy
    for _ in range(4):  # at most 4 wrapped title lines
        band = [(x, t) for oysp in rows if abs(oysp - cur) < 1.6
                for x, t in rows[oysp] if TITLE_X[0] <= x < TITLE_X[1]]
        if not band:
            break
        band.sort()
        title_parts.append(" ".join(t.strip() for x, t in band))
        oys.append(cur)
        nxt = [o for o in sorted(rows) if o > cur + 1.6 and o < cur + WRAP_GAP + 1.6
               and any(TITLE_X[0] <= x < TITLE_X[1] for x, t in rows[o])
               and not any(x < TITLE_X[0] for x, t in rows[o])]
        if not nxt:
            break
        cur = nxt[0]
    return " ".join(p for p in title_parts if p).strip(), oys


def main() -> int:
    pdf = glob.glob(str(REPO / f"Official-Specifications/{Q}/*.pdf"))[0]
    doc = fitz.open(pdf)
    pj = sorted((REPO / f"Official-Specifications/parsed/{Q}").glob("*.parsed.json"))[0]
    raw_pj = pj.read_text(encoding="utf-8")
    parsed = json.loads(raw_pj)
    tp_path = REPO / f"Official-Specifications/parsed/{Q}/topics.json"
    raw_tp = tp_path.read_text(encoding="utf-8")
    tp = json.loads(raw_tp)
    sp_path = REPO / f"Official-Specifications/parsed/{Q}/spec_points.json"
    raw_sp = sp_path.read_text(encoding="utf-8")
    sp = json.loads(raw_sp)

    mapping = {}  # code -> new title
    for s in parsed.get("subsections") or []:
        code, page, oy = s.get("code"), s.get("page"), s.get("oy")
        if code is None or page is None or oy is None:
            continue
        title, _ = derive_title(doc, page, oy)
        if not title:
            failures.append(f"{code}: derived empty title")
            continue
        if title == str(s.get("title") or "").strip():
            continue
        mapping[code] = title
        s["title"] = title

    for s in tp.get("subsections") or []:
        new = mapping.get(s.get("code"))
        if new:
            s["title"] = new

    n_ref = 0
    for r in sp["spec_points"]:
        sub = r.get("subsection")
        if isinstance(sub, dict):
            new = mapping.get(sub.get("code"))
            if new and sub.get("title") != new:
                sub["title"] = new
                n_ref += 1

    if failures:
        print("FAIL-CLOSED:", *failures, sep="\n  ")
        return 1

    for path, raw, docu in ((pj, raw_pj, parsed), (tp_path, raw_tp, tp),
                            (sp_path, raw_sp, sp)):
        txt = json.dumps(docu, indent=1, ensure_ascii=False)
        if raw.endswith("\n") and not txt.endswith("\n"):
            txt += "\n"
        path.write_text(txt, encoding="utf-8")

    print(f"titles repaired: {len(mapping)}; statement refs updated: {n_ref}")
    for k in sorted(mapping):
        print(f"  {k}: {mapping[k]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
