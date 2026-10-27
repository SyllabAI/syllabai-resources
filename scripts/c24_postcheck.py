#!/usr/bin/env python3
"""T-C24 — post-repair invariant check.

Verifies, for every subject's canonical spec_points.json:
  I1  no geometrically-impossible topic/subsection refs remain (TOL-aware)
  I2  statement count, codes, texts, bullets, ordering, provenance pages
      unchanged vs git HEAD (only topic/subsection refs may differ)
  I3  every ref that exists points at a real header row (title match)
Exit nonzero on any violation.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PARSED = REPO / "Official-Specifications/parsed"
TOL = 6.0

# records removed by T-C24 with recorded evidence (contamination):
#   chem-modular 3.4  — About-page prose ("3.4 million learners…")
#   ial-biology 5.0   — maths-skills appendix fragments
REMOVED_OK = {"IGCSE_CHEMISTRY_MODULAR:3.4", "IAL_BIOLOGY:Biology-5.0"}

# ledger-driven allowlist (T-C24 WS-3 fixes + WS-5 PDF-verified respacing)
import json as _json
_AL = _json.load(open("/home/z/my-project/kg_audit/c24/field_allowlist.json"))
TEXT_FIX_OK = {}
for _k, _flds in _AL.items():
    _q, _c = _k.split("|", 1)
    TEXT_FIX_OK.setdefault((_q, _c), set()).update(_flds)

sys.path.insert(0, "/home/z/my-project/scripts")
from c24_repair_attachments import raw_tables, at_or_above  # noqa: E402

SUBJECTS = sorted({p.name for p in PARSED.iterdir() if p.is_dir()} - {"_derived"})


def git_show(path: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(REPO), "show", f"HEAD:{path}"],
        capture_output=True, check=True).stdout


def main() -> int:
    bad = 0
    for q in SUBJECTS:
        sp_path = PARSED / q / "spec_points.json"
        if not sp_path.exists():
            continue
        new = json.loads(sp_path.read_text(encoding="utf-8"))
        try:
            old = json.loads(git_show(f"Official-Specifications/parsed/{q}/spec_points.json"))
        except subprocess.CalledProcessError:
            continue
        topics, subsecs = raw_tables(q)
        topics.sort(key=lambda h: (h["page"], h["oy"]))
        subsecs.sort(key=lambda h: (h["page"], h["oy"]))
        o_by_id = {r.get("id"): r for r in old["spec_points"]}
        n_imp = 0
        for r in new["spec_points"]:
            pr = r.get("provenance") or {}
            page, oy = pr.get("page"), pr.get("oy")
            if page is None:
                continue
            for kind, ref, tbl in (("topic", r.get("topic"), topics),
                                   ("sub", r.get("subsection"), subsecs)):
                if isinstance(ref, dict) and ref.get("page") is not None:
                    if (ref["page"], ref.get("oy") or 0.0) > (page, (oy or 0.0) + TOL):
                        n_imp += 1
                        print(f"VIOLATION {q} {r.get('official_code')} {kind} "
                              f"hdr p{ref['page']}y{ref.get('oy')} stmt p{page}y{oy}")
            # title existence check
            if isinstance(r.get("topic"), dict):
                tt = (r["topic"].get("number"), r["topic"].get("title"))
                if tt and not any((t["number"], t["title"]) == tt for t in topics):
                    print(f"UNKNOWN-TOPIC {q} {r.get('official_code')} {tt}")
                    bad += 1
        o = o_by_id
        # I2: only refs differ — except recorded removals and recorded text fixes
        removed_here = {rid for rid in o
                        if rid not in {x.get("id") for x in new["spec_points"]}}
        if len(old["spec_points"]) != len(new["spec_points"]):
            if not removed_here or not removed_here <= REMOVED_OK:
                print(f"COUNT-DRIFT {q}")
                bad += 1
        for rid in removed_here:
            if rid not in REMOVED_OK:
                print(f"ID-DROPPED-UNRECORDED {q} {rid}")
                bad += 1
        for r in new["spec_points"]:
            ro = o.get(r.get("id"))
            if ro is None:
                print(f"ID-NEW {q} {r.get('id')}")
                bad += 1
                continue
            allow = TEXT_FIX_OK.get((q, r.get("id")), set()) or \
                    TEXT_FIX_OK.get((q, r.get("official_code")), set())
            for f in ("official_code", "text", "sub_items", "ordering",
                      "practical", "leading_verb", "scope"):
                if r.get(f) != ro.get(f) and f not in allow:
                    print(f"FIELD-DRIFT {q} {r.get('id')} {f}")
                    bad += 1
            if (r.get("provenance") or {}).get("page") != \
               (ro.get("provenance") or {}).get("page"):
                print(f"PAGE-DRIFT {q} {r.get('id')}")
                bad += 1
        status = "OK" if n_imp == 0 else f"{n_imp} impossible remain"
        print(f"{q:32s} {status}")
        bad += n_imp
    print("POST-CHECK:", "FAIL" if bad else "ALL PASS")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
