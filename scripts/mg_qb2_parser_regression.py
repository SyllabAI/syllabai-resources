#!/usr/bin/env python3
"""Parser regression: run the PATCHED anchor rule over the QB-1 GCSE source PDFs
(staged aside in mg_work/pdfs_gcse_stale/) and compare per-topic question counts
with the T-MG-QB-1 run-001 of-record results (mg_work/logs/qb_extract_results.json)."""
import json
import os
import sys

sys.path.insert(0, "/home/z/my-project/scripts/mg")
import fitz  # noqa: E402
from mg_qb2_extract import parse_questions, valid_pdf  # noqa: E402

WORK = "/home/z/my-project/mg_work"
cat = json.load(open(f"{WORK}/catalog/gcse_edexcel_catalog.json"))
of_record = {r["code"]: r for r in json.load(open(f"{WORK}/logs/qb_extract_results.json"))["results"]}

mismatch, checked, missing = [], 0, []
for t in cat["topics"]:
    code, slug = t["code"], t["site_slug"]
    rec = of_record.get(code)
    if not rec or rec.get("status") != "ok":
        continue
    ws = f"{WORK}/pdfs_gcse_stale/{code}-ws.pdf"
    book = f"{WORK}/pdfs_gcse_stale/{code}.pdf"
    ws_ok = os.path.exists(ws) and valid_pdf(ws) is not None
    book_ok = os.path.exists(book) and valid_pdf(book) is not None
    if not ws_ok and not book_ok:
        missing.append(code)
        continue
    doc = valid_pdf(ws) if ws_ok else valid_pdf(book)
    qs = parse_questions(doc, None)
    if ws_ok and len(qs) < 2 and book_ok:
        bdoc = valid_pdf(book)
        if bdoc is not None:
            bqs = parse_questions(bdoc, None)
            if len(bqs) > len(qs):
                qs = bqs
    checked += 1
    if len(qs) != rec["questions"]:
        mismatch.append({"code": code, "slug": slug, "of_record": rec["questions"], "patched": len(qs)})

print(f"checked {checked} GCSE topics of record; missing PDFs: {len(missing)}")
print(f"mismatches: {len(mismatch)}")
for m in mismatch[:20]:
    print(" ", m)

out = {
    "purpose": "T-MG-QB-2 run-001 hardening check: patched anchor rule (column-relative x <= 75pt) "
               "vs T-MG-QB-1 run-001 of-record per-topic question counts on the GCSE corpus",
    "checked": checked, "missing_pdfs": missing, "divergent_topics": mismatch,
    "recovered_undercounts": [m for m in mismatch if m["patched"] > m["of_record"]],
    "deflated_overcounts": [m for m in mismatch if m["patched"] < m["of_record"]],
    "ground_truth_spot_checks": [
        {"code": "8.7", "finding": "ws truly has 4 questions (IGCSE Sequences Higher, 1 page Q1-Q4); "
                                   "of-record 8 was inflated by sequence-term false anchors"},
        {"code": "4.17", "finding": "ws truly has >=5 questions (Q1 and Q5 visible on page 1); "
                                    "of-record 4 was an undercount"},
        {"code": "3.2", "finding": "booklet questions are images; text layer is fraction fragments; "
                                   "of-record 3 were fragment strips, patched 0 is the honest state"},
    ],
}
with open(f"{WORK}/logs/qb2_parser_regression.json", "w") as f:
    json.dump(out, f, indent=1)
print("saved logs/qb2_parser_regression.json")
