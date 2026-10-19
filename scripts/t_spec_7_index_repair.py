#!/usr/bin/env python3
"""T-SPEC-7 index repair: harvest indexes missed part-referenced tags.

For each of the 14 lanes: part-referenced ids absent from the lane's index
are repaired by (1) adding a proper index entry (global tag name/definition
from a sibling lane's index), (2) extending the resolution sidecar with the
tag's T-SPEC-7 verdict when its code is in the lane's pool (else an honest
pending record), (3) writing the mapping + part codes, and (4) recomputing
the index coverage counts.
"""
import json
import re
from collections import Counter
from pathlib import Path

import yaml

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
PARSED = BASE / "Official-Specifications" / "parsed"
WORK = Path("/home/z/my-project/scripts/specmap_work")
SUFFIX = {"igcse-accounting", "igcse-geography", "igcse-english-literature"}
LANES = {
    "igcse-accounting-17-financial-statements": ("igcse-accounting", None),
    "igcse-accounting-17-introduction-to-bookkeeping-and-accounting": ("igcse-accounting", None),
    "igcse-business-19": ("igcse-business", None),
    "igcse-economics-17": ("igcse-economics", None),
    "igcse-english-literature-16": ("igcse-english-literature", None),
    "igcse-geography-19": ("igcse-geography", None),
    "igcse-ict-17": ("igcse-ict", None),
    "igcse-further-maths-19": ("igcse-further-maths", None),
    "igcse-maths-a-18-foundation": ("igcse-maths-a", "F"),
    "igcse-maths-a-18-higher": ("igcse-maths-a", "ALL"),
    "igcse-maths-a-modular-24-foundation-unit-1": ("igcse-maths-a-modular", "U1F"),
    "igcse-maths-a-modular-24-foundation-unit-2": ("igcse-maths-a-modular", "U2F"),
    "igcse-maths-a-modular-24-higher-unit-1": ("igcse-maths-a-modular", "U1FH"),
    "igcse-maths-a-modular-24-higher-unit-2": ("igcse-maths-a-modular", "U2FH"),
}
idv = yaml.safe_load((BASE / "scripts" / "t_spec_7_verdicts.yaml").read_text())["id_verdicts"]

# global tag metadata across ALL lane indexes
global_meta = {}
for lane in LANES:
    idx = json.loads((EQ / lane / "spec_point_index.json").read_text())
    for sid, e in idx["spec_points"].items():
        if e.get("name") and sid not in global_meta:
            global_meta[sid] = {"name": e.get("name"), "definition": e.get("definition") or "",
                                "subtopic_slugs": e.get("subtopic_slugs") or []}

def pool_codes(qual, mode):
    pts = json.loads((PARSED / qual / "spec_points.json").read_text())["spec_points"]
    if qual in SUFFIX:
        return {p["id"].rsplit(":", 1)[-1] for p in pts}, {p["id"].rsplit(":", 1)[-1]: p for p in pts}
    if mode in (None, "ALL"):
        sel = pts
    elif mode == "F":
        sel = [p for p in pts if p.get("scope") != "H"]
    elif mode == "U1F":
        sel = [p for p in pts if p.get("scope") == "U1F"]
    elif mode == "U2F":
        sel = [p for p in pts if p.get("scope") == "U2F"]
    elif mode == "U1FH":
        sel = [p for p in pts if p.get("scope") in ("U1F", "U1H")]
    else:
        sel = [p for p in pts if p.get("scope") in ("U2F", "U2H")]
    return {p["official_code"] for p in sel}, {p["official_code"]: p for p in sel}

repaired = Counter()
for lane, (qual, mode) in LANES.items():
    cdir = EQ / lane
    idx = json.loads((cdir / "spec_point_index.json").read_text())
    mp = json.loads((cdir / "spec_point_map.json").read_text())
    res = json.loads((cdir / "spec_point_resolution.json").read_text())
    by_res = {r["id"]: r for r in res["resolved"]}
    pool, by_code = pool_codes(qual, mode)
    ghosts = set()
    for f in list(cdir.glob("*/*/*/topic.json")) + list(cdir.glob("*/*/topic.json")):
        t = json.loads(f.read_text())
        for q in t.get("questions", []):
            for p in q.get("parts", []):
                ghosts.update(s for s in (p.get("spec_point_ids") or [])
                              if s not in idx["spec_points"])
    if not ghosts:
        continue
    for sid in sorted(ghosts):
        v = idv.get(sid) or {}
        crec = (v.get("courses") or {}).get(lane) or {}
        verdict = crec.get("verdict") or v.get("verdict")
        meta = global_meta.get(sid, {})
        code = crec["codes"][0] if crec.get("codes") else None
        ok = code is not None and code in pool
        # 1) index entry
        idx["spec_points"][sid] = {"name": meta.get("name"),
                                   "definition": meta.get("definition") or "",
                                   "notes": [], "subtopic_slugs": meta.get("subtopic_slugs") or []}
        # 2) resolution record
        rec = by_res.get(sid) or {"id": sid, "sme_name": meta.get("name"),
                                  "sme_definition": meta.get("definition") or "",
                                  "referenced_by_parts": 0}
        if ok and verdict == "resolve":
            prov = mp["mappings"].get(sid)
            mp["mappings"][sid] = {
                "official_id": by_code[code]["id"], "official_code": code,
                "tier": v.get("tier"), "score": 1.0, "unit": None,
                "method": "operator-verdict (T-SPEC-7 index-repair lane)",
                "resolution": {"lane": "operator-verdict (T-SPEC-7 index repair)",
                               "quote": v.get("quote"), "page": v.get("page"),
                               "pmt_excluded": True}}
            rec.update({"resolved_code": code, "official_id": by_code[code]["id"],
                        "official_wording": by_code[code].get("text"),
                        "tier": v.get("tier"), "score": 1.0,
                        "method": "operator-verdict (T-SPEC-7 index-repair lane)",
                        "unit": None})
            repaired[(lane, "resolved")] += 1
        else:
            rec["resolved_code"] = None
            rec["reason"] = crec.get("reason") or (
                "no-guess pending: part-referenced tag recovered by the T-SPEC-7 "
                "index repair; no verdict record for this lane")
            mp["unmapped"] = [u for u in mp.get("unmapped", []) if u["spcpt_id"] != sid]
            mp["unmapped"].append({"spcpt_id": sid, "name": meta.get("name"),
                                   "reason": rec["reason"]})
            repaired[(lane, "pending")] += 1
        by_res[sid] = rec
    # 3) part codes for ghosts now mapped
    for f in list(cdir.glob("*/*/*/topic.json")) + list(cdir.glob("*/*/topic.json")):
        t = json.loads(f.read_text())
        changed = False
        for q in t.get("questions", []):
            for p in q.get("parts", []):
                sids = p.get("spec_point_ids") or []
                codes, seen = [], set()
                for s in sids:
                    m = mp["mappings"].get(s)
                    if m and m["official_code"] not in seen:
                        codes.append(m["official_code"])
                        seen.add(m["official_code"])
                if codes and codes != p.get("spec_point_codes"):
                    p["spec_point_codes"] = codes
                    changed = True
        if changed:
            f.write_text(json.dumps(t, ensure_ascii=False, indent=1), encoding="utf-8")
    # 4) coverage recompute
    missing = idx["coverage"].get("missing_from_index") or []
    idx["coverage"]["missing_from_index"] = [s for s in missing if s not in idx["spec_points"]]
    nmiss = len(idx["coverage"]["missing_from_index"])
    actual = sum(1 for f in (list(cdir.glob("*/*/*/topic.json")) + list(cdir.glob("*/*/topic.json")))
                 for q in json.loads(f.read_text()).get("questions", [])
                 for p in q.get("parts", []))
    idx["coverage"] = {"question_part_ids_total": actual,
                       "covered_by_index": actual - nmiss,
                       "missing_from_index": idx["coverage"]["missing_from_index"]}
    res["counts"] = {"ids": len(res["resolved"]),
                     "resolved": sum(1 for r in res["resolved"] if r.get("resolved_code")),
                     "unresolved": sum(1 for r in res["resolved"] if not r.get("resolved_code"))}
    res["resolved"] = list(by_res.values())
    res["generated_utc"] = res["generated_utc"]  # preserve
    (cdir / "spec_point_index.json").write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    (cdir / "spec_point_resolution.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    (cdir / "spec_point_map.json").write_text(json.dumps(mp, ensure_ascii=False, indent=1), encoding="utf-8")

print("index repair:", dict(repaired))
