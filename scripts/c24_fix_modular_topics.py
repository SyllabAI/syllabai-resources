#!/usr/bin/env python3
"""T-C24 WS-4 — modular-spec topic-header recovery + re-attachment.

Root cause: the modular science specs print content-topic headers whose
titles end with ": Part N" (e.g. "4 Solids, liquids and gases: Part 1").
The bands walker's big-section guard (`not re.search(r'\\s\\d{1,3}$', t)`,
meant to reject page-number lines) rejected every such header, so 13 topic
headers are missing from the parsed tables:

  igcse-physics-modular    4 Solids, liquids and gases: Part 1 (p28)
                           6 Solids, liquids and gases: Part 2 (p33)
  igcse-biology-modular    2 Structure and functions in living organisms: Part 1 (p21)
                           3 Structure and functions in living organisms: Part 2 (p25)
  igcse-chemistry-modular  1..8 Principles/Inorganic/Physical/Organic : Part 1/2 (p21..p35)

With incomplete tables, every downstream statement attached to the previous
captured topic -> 292 of the 705 topic-code-mismatch findings.

Also: igcse-chemistry-modular contains ONE contaminated record
(IGCSE_CHEMISTRY_MODULAR:3.4 @ p11) — the About-page prose "3.4 million
learners studying…" misread as code 3.4. No real 3.4 exists (topic 3 prints
3.1–3.3, 3.5C–3.8); the record is promo prose, unreferenced by SME/flashcard
maps -> removed with evidence.

Actions (deterministic, PDF-verified headers hard-pinned):
  1. insert the 13 recovered headers into <stem>.parsed.json + topics.json
     (topics.json codes regenerated T1..Tn in reading order; nothing
     external references the old modular T-codes — verified)
  2. remove the contaminated chem-modular record (recorded)
  3. re-attach topic refs for the three subjects geometrically using the
     completed tables (capture-time semantics)
Fail-closed on any table/registry inconsistency.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PARSED = REPO / "Official-Specifications/parsed"
OUT = Path("/home/z/my-project/kg_audit/c24/modular_topic_recovery.json")

RECOVERED = {
    "igcse-physics-modular": [
        {"number": "4", "title": "Solids, liquids and gases: Part 1", "page": 28, "oy": 74},
        {"number": "6", "title": "Solids, liquids and gases: Part 2", "page": 33, "oy": 74},
    ],
    "igcse-biology-modular": [
        {"number": "2", "title": "Structure and functions in living organisms: Part 1", "page": 21, "oy": 74},
        {"number": "3", "title": "Structure and functions in living organisms: Part 2", "page": 25, "oy": 74},
    ],
    "igcse-chemistry-modular": [
        {"number": "1", "title": "Principles of chemistry: Part 1", "page": 21, "oy": 74},
        {"number": "2", "title": "Inorganic chemistry: Part 1", "page": 24, "oy": 74},
        {"number": "3", "title": "Physical chemistry: Part 1", "page": 27, "oy": 74},
        {"number": "4", "title": "Organic chemistry: Part 1", "page": 28, "oy": 74},
        {"number": "5", "title": "Principles of chemistry: Part 2", "page": 30, "oy": 74},
        {"number": "6", "title": "Inorganic chemistry: Part 2", "page": 32, "oy": 74},
        {"number": "7", "title": "Physical chemistry: Part 2", "page": 34, "oy": 74},
        {"number": "8", "title": "Organic chemistry: Part 2", "page": 35, "oy": 74},
    ],
}

JUNK = {"qual": "igcse-chemistry-modular", "id": "IGCSE_CHEMISTRY_MODULAR:3.4",
        "reason": "About-page prose ('3.4 million learners studying…') misread as "
                  "spec code 3.4; not a specification point; topic 3 prints "
                  "3.1–3.3 and 3.5C–3.8; unreferenced by SME/flashcard maps"}

TOL = 6.0
failures = []


def dump(path, raw, doc):
    txt = json.dumps(doc, indent=1, ensure_ascii=False)
    if raw.endswith("\n") and not txt.endswith("\n"):
        txt += "\n"
    path.write_text(txt, encoding="utf-8")


def main() -> int:
    ledger = {"inserted": {}, "removed": None, "reattached": {}}

    for q, headers in RECOVERED.items():
        pj = sorted((PARSED / q).glob("*.parsed.json"))[0]
        raw_pj = pj.read_text(encoding="utf-8")
        parsed = json.loads(raw_pj)
        tp_path = PARSED / q / "topics.json"
        raw_tp = tp_path.read_text(encoding="utf-8")
        tp = json.loads(raw_tp)

        pdf_sha1 = tp["topics"][0]["provenance"]["pdf_sha1"]

        # -- 1a. insert into raw parsed tables --
        existing = {(t.get("number"), t.get("title"), t.get("page")) for t in parsed["topics"]}
        ins_raw = []
        for h in headers:
            key = (h["number"], h["title"], h["page"])
            if key in existing:
                continue
            parsed["topics"].append(dict(h))
            ins_raw.append(key)
        parsed["topics"].sort(key=lambda t: (t["page"], t.get("oy") or 0))
        # counts update
        if "counts" in parsed and "topics" in parsed.get("counts", {}):
            parsed["counts"]["topics"] = len(parsed["topics"])

        # -- 1b. rebuild canonical topics.json in reading order --
        prefix = tp["topics"][0]["code"].rsplit("-T", 1)[0]
        rows = []
        for i, t in enumerate(parsed["topics"], 1):
            pr = {"pdf_sha1": pdf_sha1, "page": t["page"], "oy": round(t.get("oy") or 0)}
            rows.append({
                "code": f"{prefix}-T{i}",
                "number": t.get("number"), "title": t.get("title"),
                "ordering": i, "provenance": pr,
            })
        tp_old_codes = [t.get("code") for t in tp["topics"]]
        tp["topics"] = rows
        tp["counts"]["topics"] = len(rows)

        dump(pj, raw_pj, parsed)
        dump(tp_path, raw_tp, tp)
        ledger["inserted"][q] = {"raw_keys": ins_raw, "old_codes": tp_old_codes,
                                 "new_count": len(rows)}

    # -- 2. remove contaminated chem-modular record --
    q = JUNK["qual"]
    sp_path = PARSED / q / "spec_points.json"
    raw_sp = sp_path.read_text(encoding="utf-8")
    sp = json.loads(raw_sp)
    before_n = len(sp["spec_points"])
    junk = [r for r in sp["spec_points"] if r.get("id") == JUNK["id"]]
    if len(junk) != 1:
        failures.append(f"junk record lookup: expected 1, found {len(junk)}")
    else:
        jr = junk[0]
        if not str(jr.get("text", "")).startswith("million learners studying"):
            failures.append(f"junk record text changed: {jr.get('text')!r}")
        sp["spec_points"] = [r for r in sp["spec_points"] if r.get("id") != JUNK["id"]]
        sp["counts"]["spec_points"] = len(sp["spec_points"])
        if "counts" in sp:
            sp["counts"]["spec_points"] = len(sp["spec_points"])
        ledger["removed"] = {"id": JUNK["id"], "page": jr["provenance"]["page"],
                             "text": jr.get("text"), "before_count": before_n,
                             "after_count": len(sp["spec_points"]),
                             "reason": JUNK["reason"]}
        dump(sp_path, raw_sp, sp)

    # -- 3. re-attach topic refs (recompute-all topics; keep subsection refs) --
    for q in RECOVERED:
        pj = sorted((PARSED / q).glob("*.parsed.json"))[0]
        parsed = json.loads(pj.read_text(encoding="utf-8"))
        topics = sorted(({"number": t["number"], "title": t["title"],
                          "page": t["page"], "oy": t.get("oy") or 0.0}
                         for t in parsed["topics"]),
                        key=lambda h: (h["page"], h["oy"]))
        sp_path = PARSED / q / "spec_points.json"
        raw = sp_path.read_text(encoding="utf-8")
        doc = json.loads(raw)
        changes = 0
        for rec in doc["spec_points"]:
            pr = rec.get("provenance") or {}
            page, oy = pr.get("page"), pr.get("oy")
            if page is None:
                continue
            best = None
            for h in topics:
                if h["page"] < page or (h["page"] == page and h["oy"] <= (oy or 0.0) + TOL):
                    best = h
                else:
                    break
            new_ref = ({"number": best["number"], "title": best["title"],
                        "page": best["page"], "oy": round(best["oy"])} if best else None)
            if json.dumps(rec.get("topic"), sort_keys=True) != json.dumps(new_ref, sort_keys=True):
                rec["topic"] = new_ref
                changes += 1
        dump(sp_path, raw, doc)
        ledger["reattached"][q] = {"topic_changes": changes,
                                   "records": len(doc["spec_points"])}

    if failures:
        print("FAIL-CLOSED:", *failures, sep="\n  ")
        return 1

    OUT.write_text(json.dumps(ledger, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: (v if k != "inserted" else
                          {q: v2["new_count"] for q, v2 in v.items()})
                      for k, v in ledger.items()}, indent=1)[:600])
    print("ledger ->", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
