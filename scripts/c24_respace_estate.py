#!/usr/bin/env python3
"""T-C24 WS-5 — estate-wide space-injection repair (PDF-authoritative).

The parser's span join (' '.join over visual-line spans) fabricated spaces
inside tight multi-span constructs: '(Ar)' -> '( A r )',
'(propan-1-ol only)' -> '( propan-1-ol only )', '(Lactobacillus)' ->
'( Lactobacillus )' — 501 occurrences across 15 subjects (+19 in the
definitive store). Glyph-geometry proof (chemistry 1.16): the print shows
ZERO gap between '(', 'A', subscript 'r' and ')'.

Repair: for every canonical spec_points.json text/bullet field containing
the artifact pattern, locate the field on its PDF page by whitespace-free
matching and adopt the PDF's own spacing for that exact character run
(pdf_respace). Fields that cannot be located (stacked-formula token-order
scrambles) are left unchanged and recorded. Provenance pages are trusted
from the parse.

Writes kg_audit/c24/respaced_estate.json. Idempotent by construction
(respaced text re-matches with identical spacing).
"""
from __future__ import annotations

import glob
import json
import re
import sys
from pathlib import Path

import fitz

REPO = Path(__file__).resolve().parent.parent
PARSED = REPO / "Official-Specifications/parsed"
OUT = Path("/home/z/my-project/kg_audit/c24/respaced_estate.json")

ARTIFACT = re.compile(r"\(\s+\S|\S\s+\)")
TOL = 6.0
failures = []


def norm(s: str) -> str:
    s = (str(s).replace("\u2019", "'").replace("\u2018", "'")
         .replace("\u201c", '"').replace("\u201d", '"')
         .replace("\u2013", "-").replace("\u2014", "-").replace("\u00a0", " "))
    return re.sub(r"\s+", " ", s).strip()


def ns(s: str) -> str:
    return re.sub(r"\s+", "", str(s)).lower()


def page_text(doc, page_no: int) -> str:
    return doc[page_no - 1].get_text("text")


def pdf_respace(doc, page_no: int, field: str):
    pt = norm(page_text(doc, page_no))
    ptns = ns(pt)
    fns = ns(field)
    i = ptns.find(fns)
    if i < 0:
        return None
    count, j = 0, 0
    while count < i and j < len(pt):
        if not pt[j].isspace():
            count += 1
        j += 1
    start = j
    while count < i + len(fns) and j < len(pt):
        if not pt[j].isspace():
            count += 1
        j += 1
    return pt[start:j]


def main() -> int:
    ledger = {"fixed": 0, "unmatched": 0, "records": []}
    for qdir in sorted(PARSED.iterdir()):
        if not qdir.is_dir() or qdir.name.startswith("_"):
            continue
        sp_path = qdir / "spec_points.json"
        if not sp_path.exists():
            continue
        pdfs = sorted(glob.glob(str(REPO / f"Official-Specifications/{qdir.name}/*.pdf")))
        if not pdfs:
            continue
        doc = fitz.open(pdfs[0])
        raw = sp_path.read_text(encoding="utf-8")
        data = json.loads(raw)
        changed = 0
        for rec in data["spec_points"]:
            pg = (rec.get("provenance") or {}).get("page")
            if pg is None:
                continue
            fields = [("text", rec.get("text"))]
            for i, b in enumerate(rec.get("sub_items") or []):
                fields.append((f"sub_items[{i}]", b))
            for fld, val in fields:
                if not val or not ARTIFACT.search(str(val)):
                    continue
                rsp = pdf_respace(doc, pg, str(val))
                if rsp is None:
                    ledger["unmatched"] += 1
                    ledger["records"].append({
                        "qual": qdir.name, "code": rec.get("official_code"),
                        "field": fld, "verdict": "UNMATCHED_PDF",
                        "text": str(val)[:200]})
                    continue
                if rsp != val:
                    if fld == "text":
                        rec["text"] = rsp
                    else:
                        idx = int(re.search(r"\[(\d+)\]", fld).group(1))
                        rec["sub_items"][idx] = rsp
                    changed += 1
                    ledger["records"].append({
                        "qual": qdir.name, "code": rec.get("official_code"),
                        "field": fld, "verdict": "RESPACED",
                        "before": str(val)[:200], "after": rsp[:200]})
        if changed:
            txt = json.dumps(data, indent=1, ensure_ascii=False)
            if raw.endswith("\n") and not txt.endswith("\n"):
                txt += "\n"
            sp_path.write_text(txt, encoding="utf-8")
        doc.close()
        ledger["fixed"] += changed
        print(f"{qdir.name:28s} fields respaced: {changed}")
    OUT.write_text(json.dumps(ledger, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"total respaced: {ledger['fixed']}, unmatched (documented): {ledger['unmatched']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
