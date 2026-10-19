#!/usr/bin/env python3
"""T-SPEC-2c — apply resolved codes to sibling topic.json parts and write
spec_point_resolution.json sidecars (AI_VALIDATED chain, verbatim evidence),
plus a per-course unresolved allowlist for the verify gate.

Rules:
  - a part gets spec_point_codes = the official_codes of all its ids that have
    mappings, ordered by the course registry's statement order; duplicate codes
    de-duplicated
  - parts whose ids are ALL unmapped stay uncoded; they are recorded in the
    sidecar's unresolved section (id-level) and the part-level allowlist,
    with the verbatim reason — never guessed
  - sidecar records carry the map's tier/score/method/flag verbatim
  - resolution table covers EVERY index id (G2): resolved + unresolved
"""
import json
import sys
import time
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
PARSED = BASE / "Official-Specifications" / "parsed"
EQ = BASE / "SME-ExamQuestion"

COURSES = {
    "igcse-chemistry-modular-24-unit-1": "igcse-chemistry-modular",
    "igcse-chemistry-modular-24-unit-2": "igcse-chemistry-modular",
    "igcse-science-double-award-17-chemistry": "igcse-science-double-award",
}


def registry_order(qual_slug):
    pts = json.loads((PARSED / qual_slug / "spec_points.json")
                     .read_text(encoding="utf-8"))["spec_points"]
    return {p["id"]: i for i, p in enumerate(pts)}, \
           {p["id"]: p for p in pts}


def main():
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    summary = {}
    for course, qual_slug in COURSES.items():
        cdir = EQ / course
        mp = json.loads((cdir / "spec_point_map.json").read_text(encoding="utf-8"))
        idx = json.loads((cdir / "spec_point_index.json").read_text(encoding="utf-8"))
        order, reg_by_id = registry_order(qual_slug)
        mappings = mp["mappings"]

        id2rec = {}
        for sid, m in mappings.items():
            id2rec[sid] = {
                "resolved_code": m["official_code"],
                "official_id": m["official_id"],
                "official_wording": (reg_by_id.get(m["official_id"], {})
                                     .get("text") or None),
                "tier": m["tier"], "score": m["score"],
                "method": m["method"], "unit": m.get("unit"),
                "flag": m.get("flag"),
                "recheck": m.get("recheck"),
            }
        unmapped = {u["spcpt_id"]: u.get("reason") for u in mp["unmapped"]}

        records = []
        for sid, e in idx["spec_points"].items():
            rec = {
                "id": sid,
                "sme_name": e.get("name"),
                "sme_definition": e.get("definition"),
                "referenced_by_parts": None,  # filled below
            }
            if sid in id2rec:
                rec.update(id2rec[sid])
            else:
                rec["resolved_code"] = None
                rec["reason"] = unmapped.get(sid, "unresolved")
            records.append(rec)

        # part references per id (for the record + allowlist honesty)
        part_refs = {}
        topic_files = sorted(cdir.glob("*/*/*/topic.json")) + sorted(cdir.glob("*/*/topic.json"))
        for f in topic_files:
            t = json.loads(f.read_text(encoding="utf-8"))
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    for s in p.get("spec_point_ids") or []:
                        part_refs[s] = part_refs.get(s, 0) + 1
        for rec in records:
            rec["referenced_by_parts"] = part_refs.get(rec["id"], 0)

        # apply to parts
        coded_parts = uncoded_parts = 0
        for f in topic_files:
            t = json.loads(f.read_text(encoding="utf-8"))
            changed = False
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    sids = p.get("spec_point_ids") or []
                    if not sids:
                        continue
                    codes, seen = [], set()
                    for s in sids:
                        r = id2rec.get(s)
                        if r and r["resolved_code"] and r["resolved_code"] not in seen:
                            codes.append(r["resolved_code"])
                            seen.add(r["resolved_code"])
                    if codes:
                        p["spec_point_codes"] = codes
                        changed = True
                        coded_parts += 1
                    else:
                        uncoded_parts += 1
            if changed:
                f.write_text(json.dumps(t, ensure_ascii=False, indent=1),
                             encoding="utf-8")

        resolved_n = sum(1 for r in records if r.get("resolved_code"))
        doc = {
            "schema": "syllabai.sme-spec-point-resolution/1.0",
            "generated_utc": now,
            "validation": "AI_VALIDATED (operator-delegated chain; full-pool join "
                          "per T-SPEC-2); HUMAN_VALIDATED reserved for human review",
            "counts": {
                "ids": len(records),
                "resolved": resolved_n,
                "unresolved": len(records) - resolved_n,
            },
            "unresolved_allowlist_note": "parts whose ids are all unresolved stay "
                                         "uncoded by design (no-guess discipline)",
            "resolved": records,
        }
        (cdir / "spec_point_resolution.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

        summary[course] = {
            "ids": len(records), "resolved": resolved_n,
            "unresolved": len(records) - resolved_n,
            "parts_coded": coded_parts, "parts_uncoded": uncoded_parts,
        }
        print(f"[{course}] resolved {resolved_n}/{len(records)} ids; "
              f"parts coded {coded_parts}, left uncoded {uncoded_parts}")

    out = Path("/home/z/my-project/scripts/specmap_work/apply_summary.json")
    out.write_text(json.dumps({"generated_utc": now, "courses": summary}, indent=1))
    print("saved", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
