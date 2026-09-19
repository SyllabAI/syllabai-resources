#!/usr/bin/env python3
"""T-C24 WS-3 — PDF cross-check adjudication engine for text-level findings.

Takes the live actionable findings from the T-C23 Task B inventory, locates
the flagged record in the REPAIRED canonical parsed JSONs (or the definitive
store / _derived YAML), and cross-checks the flagged fragment against the
official PDF (PyMuPDF text extraction, whitespace-normalized).

Verdicts:
  FALSE_POSITIVE_NOTATION   fragment is correct notation (oxidation states,
                            unit annotations) — the bracket regex over-fires
  CONFIRMED_PDF_VERBATIM    the flagged text is exactly what the PDF prints
                            (wording authority = PDF) — keep, recorded
  PARSER_ARTIFACT_FIXED     parse damage (dup word, leaked markup, lost
                            space) that the PDF contradicts — FIX applied
  BULLETS_CAPTURED          colon lead-in: the PDF prints bullet items after
                            the colon — captured into sub_items
  NEEDS_MANUAL              engine could not decide

Writes kg_audit/c24/text_adjudication.json and prints the ledger.
"""
from __future__ import annotations

import glob
import json
import re
import sys
from pathlib import Path

import fitz
import yaml

REPO = Path(__file__).resolve().parent.parent
PARSED = REPO / "Official-Specifications/parsed"
INVENTORY = Path("/home/z/my-project/kg_audit/c23scan/inventory.json")
OUT = Path("/home/z/my-project/kg_audit/c24/text_adjudication.json")

ACTIONABLE = {
    "lost-space-paren", "lost-space-comma", "dup-token", "markdown-leak",
    "html-entity", "latex-fragment", "fullwidth-punct", "cjk-leak",
    "placeholder-empty", "bullet-leadin-without-items",
}

ROMAN = re.compile(r"\((?:X{0,2}(?:IX|IV|V?I{0,3}))\)")
UNIT_W = {"V", "A", "W", "s", "m", "K", "g", "kg", "mol", "N", "J", "Hz", "ohm",
          "mA", "cm3", "dm3", "mol2"}
UNIT = re.compile(r"\((?:%s)\)" % "|".join(UNIT_W))
DUP = re.compile(r"\b(\w{3,})\s+\1\b")


def ns(s: str) -> str:
    """Whitespace-free, case-folded form for alignment."""
    return re.sub(r"\s+", "", str(s)).lower()


def pdf_respace(pdf_path: str, page_no: int, field: str):
    """Locate the field in the PDF page by whitespace-free matching and
    return the PDF's own spacing for the same character run, or None."""
    if page_no is None:
        return None
    pt = norm(page_text(pdf_path, page_no))
    ptns = ns(pt)
    fns = ns(field)
    i = ptns.find(fns)
    if i < 0:
        return None
    # map the no-space run back to spaced PDF text
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


def norm(s: str) -> str:
    s = (str(s).replace("\u2019", "'").replace("\u2018", "'")
         .replace("\u201c", '"').replace("\u201d", '"')
         .replace("\u2013", "-").replace("\u2014", "-").replace("\u00a0", " "))
    return re.sub(r"\s+", " ", s).strip()


def page_text(pdf_path: str, page_no: int) -> str:
    doc = fitz.open(pdf_path)
    try:
        return doc[page_no - 1].get_text("text")
    finally:
        doc.close()


def pdf_contains(pdf_path: str, page_no: int, fragment: str) -> bool:
    if page_no is None:
        return False
    pt = norm(page_text(pdf_path, page_no))
    return norm(fragment) in pt


def respace_check(rec, pdf_path, pg, text, fixes, key):
    """Final fallback: whitespace-free locate + PDF-truth respacing."""
    rsp = pdf_respace(pdf_path, pg, text)
    if rsp is None:
        rec["verdict"] = "NEEDS_MANUAL"
        rec.setdefault("evidence", "no whitespace-free match on PDF page")
        return
    if norm(rsp) == norm(text):
        rec["verdict"] = "CONFIRMED_PDF_VERBATIM"
        rec["evidence"] = f"whitespace-free match; PDF spacing identical (p{pg})"
        return
    fixes.setdefault(key, text)
    rec["verdict"] = "PARSER_ARTIFACT_FIXED"
    rec["evidence"] = f"PDF respaced (p{pg}): {rsp!r}"


def load_records(q: str):
    d = json.loads((PARSED / q / "spec_points.json").read_text(encoding="utf-8"))
    return {str(r.get("official_code")): r for r in d["spec_points"]}, d


def main() -> int:
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))
    live = [e for e in inv if e["class"] in ACTIONABLE
            and "PRE-SWAP" not in e["file"] and "retired" not in e["file"]]
    cache = {}
    pdfs = {}
    out = []
    fixes = {}  # (qual, code) -> dict of field fixes

    for e in live:
        f, cls, loc, sample = e["file"], e["class"], e["locator"], e["sample"]
        rec = {
            "file": f, "class": cls, "locator": loc, "sample": sample,
            "verdict": None, "evidence": "",
        }
        m = re.match(r"parsed/([^/]+)/spec_points\.json", f)
        if m:
            q = m.group(1)
            if q not in cache:
                cache[q] = load_records(q)
            rmap, _ = cache[q]
            code = loc.split(":")[0].replace("-dup", "")
            r = rmap.get(code)
            if r is None and ":" in code:
                # synthetic-id locator (heading_bullets): IGCSE_<Q>:S3.056
                suffix = code.rsplit(":", 1)[-1]
                r = rmap.get(suffix)
                if r is not None:
                    code = suffix
            if r is None:
                rec["verdict"] = "NEEDS_MANUAL"
                rec["evidence"] = "record not found by locator"
                out.append(rec)
                continue
            fld = loc.split(":")[1] if ":" in loc else "text"
            fld = fld.split("[")[0]
            text = str(r.get(fld) or "")
            pdf = pdfs.get(q) or (pdfs.__setitem__(q, glob.glob(
                str(REPO / f"Official-Specifications/{q}/*.pdf"))[0] or None),
                pdfs.get(q))[1]
            pg = (r.get("provenance") or {}).get("page")
            # ---- class-specific adjudication ----
            if cls == "lost-space-paren":
                frag = sample.strip()
                ctx_i = text.find(frag[:3])
                ctx = text[max(0, ctx_i - 30): ctx_i + 40]
                if ROMAN.search(frag) or ROMAN.search(ctx):
                    rec["verdict"] = "FALSE_POSITIVE_NOTATION"
                    rec["evidence"] = f"oxidation-state notation in context: {ctx!r}"
                elif UNIT.search(frag) or UNIT.search(ctx):
                    rec["verdict"] = "FALSE_POSITIVE_NOTATION"
                    rec["evidence"] = f"unit annotation in context: {ctx!r}"
                else:
                    respace_check(rec, pdf, pg, text, fixes, (q, code, fld))
            elif cls == "lost-space-comma":
                if pdf_contains(pdf, pg, text):
                    rec["verdict"] = "CONFIRMED_PDF_VERBATIM"
                    rec["evidence"] = f"full field text found verbatim on PDF p{pg}"
                else:
                    fixed = re.sub(r",(?=[A-Za-z])", ", ", text)
                    if pdf_contains(pdf, pg, fixed):
                        fixes.setdefault((q, code, fld), text)
                        rec["verdict"] = "PARSER_ARTIFACT_FIXED"
                        rec["evidence"] = f"PDF shows comma+space; fixed to: {fixed!r}"
                    else:
                        rec["verdict"] = "NEEDS_MANUAL"
            elif cls == "dup-token":
                mm = DUP.search(text)
                dupw = mm.group(1) if mm else sample.split()[0]
                single = DUP.sub(r"\1", text)
                if pdf_contains(pdf, pg, single) and not pdf_contains(pdf, pg, text):
                    fixes.setdefault((q, code, fld), text)
                    rec["verdict"] = "PARSER_ARTIFACT_FIXED"
                    rec["evidence"] = (f"PDF prints the word once; "
                                       f"dup {dupw!r} collapsed")
                elif pdf_contains(pdf, pg, text):
                    rec["verdict"] = "CONFIRMED_PDF_VERBATIM"
                    rec["evidence"] = "PDF also prints the doubled word"
                else:
                    rsp_single = pdf_respace(pdf, pg, single)
                    if rsp_single is not None and ns(rsp_single) == ns(single):
                        fixes.setdefault((q, code, fld), text)
                        rec["verdict"] = "PARSER_ARTIFACT_FIXED"
                        rec["evidence"] = (f"PDF prints the word once (p{pg}); "
                                           f"dup {dupw!r} collapsed to: {rsp_single!r}")
                    else:
                        rec["verdict"] = "NEEDS_MANUAL"
                        rec["evidence"] = f"dup {dupw!r} neither form found on p{pg}"
            elif cls in ("markdown-leak", "html-entity", "latex-fragment",
                         "fullwidth-punct", "cjk-leak", "placeholder-empty"):
                clean = re.sub(r"\*\*|##", "", text)
                clean = re.sub(r"&[a-z]{2,8};|&#\d+;", " ", clean)
                if pdf_contains(pdf, pg, clean) and clean != text:
                    fixes.setdefault((q, code, fld), text)
                    rec["verdict"] = "PARSER_ARTIFACT_FIXED"
                    rec["evidence"] = f"PDF-true text: {clean!r}"
                elif pdf_contains(pdf, pg, text):
                    rec["verdict"] = "CONFIRMED_PDF_VERBATIM"
                else:
                    respace_check(rec, pdf, pg, text, fixes, (q, code, fld))
                    if rec["verdict"] == "NEEDS_MANUAL" and not rec.get("evidence"):
                        rec["evidence"] = f"page {pg} text does not contain field"
            elif cls == "bullet-leadin-without-items":
                pt = norm(page_text(pdf, pg or 1))
                i = pt.find(norm(text)[:60])
                tail = pt[i:i + 400] if i >= 0 else ""
                has_bullets = "\u2022" in pt[(i + len(norm(text[:60]))) if i >= 0 else 0:
                                             (i + 400) if i >= 0 else 400]
                rec["verdict"] = "NEEDS_MANUAL"
                rec["evidence"] = f"PDF p{pg} tail after lead-in: {tail[60:260]!r}"
                rec["has_bullets_after"] = bool(has_bullets)
            out.append(rec)

        elif "POST-SWAP" in f or "_derived" in f:
            # store / _derived findings are adjudicated against the canonical
            # chemistry record + PDF; they resolve together with WS-6/WS-7
            rec["verdict"] = "DEFER_TO_WS6_WS7"
            rec["evidence"] = ("resolved with the definitive-store/_derived "
                               "adjudication (same underlying records)")
            out.append(rec)
        else:
            rec["verdict"] = "NEEDS_MANUAL"
            rec["evidence"] = "unhandled file shape"
            out.append(rec)

    OUT.write_text(json.dumps({"adjudications": out, "fixes": [list(k) for k in fixes]},
                              indent=1, ensure_ascii=False), encoding="utf-8")
    from collections import Counter
    print("verdicts:", dict(Counter(r["verdict"] for r in out)))
    for r in out:
        if r["verdict"] in ("NEEDS_MANUAL", "PARSER_ARTIFACT_FIXED"):
            print(f"  [{r['verdict']}] {r['file']} {r['locator']} :: {r['evidence'][:110]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
