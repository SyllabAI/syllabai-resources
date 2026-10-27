#!/usr/bin/env python3
"""T-C24 WS-3 final — apply the four PDF-verified text fixes and write the
complete text-adjudication ledger for every live actionable finding.

Data fixes (each PDF-verified, deterministic, recorded before/after):
  F1 ial-biology 4.6        — capture the three (i)/(ii)/(iii) items the PDF
                              prints after the colon into sub_items
  F2 igcse-further-maths 9A — restore PDF spacing: "of x", "ax, cos"
  F3 igcse-maths-a H-3.1B   — restore PDF spacing: "know and use nth term"
  F4 igcse-business 5.4.1   — restore the true statement + its four bullets;
                              drop mis-attached page furniture (assessment
                              footer, access-arrangement fragments from other
                              sections that the band walk leaked into this
                              record)

Everything else in the live actionable set is adjudicated WITHOUT data
change: FALSE_POSITIVE_NOTATION (oxidation states / units / math notation),
CONFIRMED_PDF_VERBATIM (including three source-printed artifacts the PDF
really contains: maths-a H-3.3E "and and", accounting "**", chemistry 4.49C
colon), or STRUCTURAL_INTERLEAVE (column-interleave chimeras in ial-maths /
geography whose correct repair is a walker redesign, documented with PDF
evidence — deliberately NOT text-patched).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PARSED = REPO / "Official-Specifications/parsed"
ADJ = Path("/home/z/my-project/kg_audit/c24/text_adjudication.json")
OUT = Path("/home/z/my-project/kg_audit/c24/text_fixes.json")

failures = []


def load(q):
    p = PARSED / q / "spec_points.json"
    raw = p.read_text(encoding="utf-8")
    return p, raw, json.loads(raw)


def save(p, raw, doc):
    txt = json.dumps(doc, indent=1, ensure_ascii=False)
    if raw.endswith("\n") and not txt.endswith("\n"):
        txt += "\n"
    p.write_text(txt, encoding="utf-8")


def find(doc, pred):
    return [r for r in doc["spec_points"] if pred(r)]


def main() -> int:
    applied = []

    # ---------- F1 ial-biology 4.6 ----------
    p, raw, doc = load("ial-biology")
    r = find(doc, lambda r: r.get("id") == "IAL_BIOLOGY:Biology-4.6")[0]
    items = [
        "(i) make observations, draw and label plan diagrams of transverse sections of roots, stems and leaves",
        "(ii) make observations, draw and label cells of plant tissues",
        "(iii) identify sclerenchyma fibres, phloem, sieve tubes and xylem vessels and their location.",
    ]
    if r.get("sub_items") not in (None, [], items):
        failures.append(f"F1: unexpected existing sub_items: {r.get('sub_items')!r}")
    else:
        before = json.dumps(r, sort_keys=True)
        r["sub_items"] = items
        applied.append({"fix": "F1", "file": "ial-biology", "code": "4.6",
                        "field": "sub_items", "before": [], "after": items})
        save(p, raw, doc)

    # ---------- F2 igcse-further-maths 9A ----------
    p, raw, doc = load("igcse-further-maths")
    r = find(doc, lambda r: r.get("id") == "IGCSE_FURTHER_MATHS:9A")[0]
    before = str(r["text"])
    after = before.replace("powers ofx (excluding", "powers of x (excluding")
    after = after.replace("sin ax,cos ax,e", "sin ax, cos ax, e")
    if after != before:
        applied.append({"fix": "F2", "file": "igcse-further-maths", "code": "9A",
                        "field": "text", "before": before, "after": after,
                        "note": "residual formula token order (stacked-superscript "
                                "print) documented as extraction artifact"})
        r["text"] = after
        save(p, raw, doc)

    # ---------- F3 igcse-maths-a H-3.1B ----------
    p, raw, doc = load("igcse-maths-a")
    r = find(doc, lambda r: r.get("id") == "IGCSE_MATHS_A:H-3.1B")[0]
    before = str(r["text"])
    after = before.replace("know and usenth term", "know and use nth term")
    if after != before:
        applied.append({"fix": "F3", "file": "igcse-maths-a", "code": "H-3.1B",
                        "field": "text", "before": before, "after": after})
        r["text"] = after
        save(p, raw, doc)

    # ---------- F4 igcse-business 5.4.1 ----------
    p, raw, doc = load("igcse-business")
    r = find(doc, lambda r: r.get("official_code") == "5.4.1")[0]
    before_text = str(r["text"])
    before_items = list(r.get("sub_items") or [])
    after_text = "The concept of quality and its importance in:"
    after_items = [
        "the production of goods and the provision of services:",
        "quality control",
        "total quality management (TQM)",
        "allowing a business to gain a competitive advantage",
    ]
    applied.append({
        "fix": "F4", "file": "igcse-business", "code": "5.4.1",
        "field": "text+sub_items",
        "before": {"text": before_text, "sub_items": before_items},
        "after": {"text": after_text, "sub_items": after_items},
        "evidence": "PDF p23: '5.4.1 The concept of quality and its importance in: "
                    "\u2022 the production of goods and the provision of services: "
                    "o quality control o total quality management (TQM) \u2022 allowing "
                    "a business to gain a competitive advantage'; the dropped "
                    "fragments (assessment footer, access-arrangement text) belong "
                    "to no statement in this region",
    })
    r["text"] = after_text
    r["sub_items"] = after_items
    save(p, raw, doc)

    if failures:
        print("FAIL-CLOSED:", *failures, sep="\n  ")
        return 1

    # ---------- complete adjudication ledger ----------
    adj = json.loads(ADJ.read_text(encoding="utf-8"))
    ledger = {a["file"] + "|" + a["locator"]: a for a in adj["adjudications"]}

    def setv(f, loc, verdict, evidence):
        a = ledger.get(f + "|" + loc)
        if a is None:
            a = ledger.setdefault(f + "|" + loc, {"file": f, "locator": loc,
                                                  "class": "", "sample": ""})
        a["verdict"] = verdict
        a["evidence"] = evidence

    SP = "parsed/igcse-chemistry/spec_points.json"
    SPM = "parsed/igcse-chemistry-modular/spec_points.json"
    IB = "parsed/ial-biology/spec_points.json"
    IM = "parsed/ial-maths/spec_points.json"
    IA = "parsed/igcse-accounting/spec_points.json"
    IBZ = "parsed/igcse-business/spec_points.json"
    IFM = "parsed/igcse-further-maths/spec_points.json"
    IGG = "parsed/igcse-geography/spec_points.json"
    IMA = "parsed/igcse-maths-a/spec_points.json"
    SDA = "parsed/igcse-science-double-award/spec_points.json"

    setv(IB, "4.6", "BULLETS_CAPTURED",
         "PDF p29 prints (i)/(ii)/(iii) items after the colon; captured verbatim into sub_items (fix F1)")
    setv(IFM, "9A:text", "PARSER_ARTIFACT_FIXED",
         "PDF p23 spacing restored ('of x', 'ax, cos') (fix F2); residual formula token order = stacked-superscript extraction artifact, documented")
    setv(IMA, "3.1B:text", "PARSER_ARTIFACT_FIXED",
         "flagged fragment '( n \u2212 1)d' is print-true math notation; the same record's real artifact 'usenth' fixed per PDF 'know and use nth term' (fix F3)")
    setv(IBZ, "5.4.1:text", "PARSER_ARTIFACT_FIXED",
         "statement + four bullets restored from PDF p23; leaked page furniture removed (fix F4)")
    setv(SDA, "3.18:text", "FALSE_POSITIVE_NOTATION",
         "copper(II) sulfate — oxidation-state notation, PDF-verbatim (p42)")
    for f, c, code in ((SP, "4.49C", "4.49C"), (SPM, "8.21C", "8.21C")):
        setv(f, c, "CONFIRMED_PDF_VERBATIM",
             f"PDF prints the colon with no following items ({code}; next statement "
             "follows immediately) — C23 colon-exception stands")
    setv(IM, "1.1", "CONFIRMED_PDF_VERBATIM",
         "PDF p24: colon ends the statement in print ('use methods of proof stated "
         "below:'); 1.2 follows — no bullets exist to capture")
    for f, loc in ((IA, "IGCSE_ACCOUNTING:S3.023:text"),
                   (IA, "IGCSE_ACCOUNTING:S5.030:text")):
        setv(f, loc, "CONFIRMED_PDF_VERBATIM",
             "the PDF literally prints 'Assessment Objectives.**' (p12/p13) — "
             "source-document artifact, faithfully parsed")
    setv(IMA, "3.3E:text", "CONFIRMED_PDF_VERBATIM",
         "the PDF span itself reads 'and and recognise that' (p40 y261.8) — "
         "source-document duplication in the Pearson print, faithfully parsed")
    interleave = (
        "column-interleave chimera (learning column + guidance/table columns "
        "captured into one statement); flagged fragment is a join artifact, "
        "NOT print-true and NOT a space loss — correct repair requires a "
        "column-aware walker re-parse (recommended follow-up), text patch "
        "deliberately withheld")
    for f, loc in ((IM, "2.2:text"), (IM, "2.3:text"), (IM, "5.1:text"),
                   (IM, "5.3:text"), (IGG, "IGCSE_GEOGRAPHY:S3.056:text"),
                   (IGG, "IGCSE_GEOGRAPHY:S9.149:text"),
                   (IGG, "IGCSE_GEOGRAPHY:S9.150:text")):
        setv(f, loc, "STRUCTURAL_INTERLEAVE", interleave)

    records = list(ledger.values())
    for r in records:
        if r["verdict"] == "DEFER_TO_WS6_WS7":
            r["verdict"] = "FALSE_POSITIVE_NOTATION"
            r["evidence"] = ("definitive-store/_derived mirror of the canonical "
                             "records: all are copper(I/II)/lead(II) oxidation-state "
                             "notation, PDF-verbatim (e.g. 2.42 'copper(II) sulfate')")
    out = {"fixes_applied": applied,
           "adjudications": records}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")

    from collections import Counter
    print("fixes applied:", len(applied))
    print("verdicts:", dict(Counter(r["verdict"] for r in records)))
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
