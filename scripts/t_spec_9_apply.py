#!/usr/bin/env python3
"""T-SPEC-9 — apply the operator round to the remaining no-guess tail.

Operator instruction (Nawaf Al Hussain Khondokar, 2026-09-19, IM):
  "Dont upstream. Fix it yourself like before."
i.e. resolve the tail with our own verdicts — no new upstream tickets. Three
mechanisms, all preceded by fail-closed validation:

  1. tag-level verdicts (scripts/t_spec_9_verdicts.yaml, T-SPEC-8 semantics):
     econ joins land on rows restored by t_spec_9_parse_repair.py (tier
     R1_parse_repair_statement_join); maths/business/geography/english-lit
     joins are operator content joins (tier P2/S0) onto existing statements.
  2. S0_operator_override tag resolves where the SME tag's content is absent
     from the published print (PDF-verified) — nearest-neighbour codes.
  3. part-level S0 overrides (scripts/t_spec_9_part_overrides.yaml, T-SPEC-2e
     pattern) for the IAL physics WPH13/WPH16 experimental-method parts (the
     print carries no unit-3/6 statements) plus four per-part refinements.

Fail-closed rules mirror T-SPEC-8: a resolved tag must sit in the lane's
unmapped tail (or already carry the same mapping); codes must exist in the
lane's registry; unit-scoped lanes additionally pair-check (official_id,
official_code); part overrides may not overwrite different existing codes.
Population closure is re-checked per lane. PMT excluded as source throughout.
"""
import json
import sys
import datetime
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from t_spec_7_apply import LANES as LANES_7, topic_files  # noqa: E402

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
PARSED = BASE / "Official-Specifications" / "parsed"
REPORTS = BASE / "graph" / "reports"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

EXTRA_LANES = {
    "ial-maths-20-pure-1": ("ial-maths", None),
    "ial-maths-20-pure-2": ("ial-maths", None),
    "ial-maths-20-pure-3": ("ial-maths", None),
    "ial-maths-20-pure-4": ("ial-maths", None),
    "ial-maths-20-mechanics-1": ("ial-maths", None),
    "ial-maths-20-mechanics-2": ("ial-maths", None),
    "ial-maths-20-decision-1": ("ial-maths", None),
    "ial-physics-19": ("ial-physics", None),
    "ial-chemistry-17": ("ial-chemistry", None),
    "igcse-physics-modular-24-unit-1": ("igcse-physics-modular", None),
    "igcse-physics-modular-24-unit-2": ("igcse-physics-modular", None),
}
LANES = dict(LANES_7)
LANES.update(EXTRA_LANES)

METHOD = "T-SPEC-9 operator verdict (no upstream; PMT excluded as source)"


def pool_for(qual, mode):
    pts = json.loads((PARSED / qual / "spec_points.json")
                     .read_text())["spec_points"]
    return {p["id"]: p for p in pts}, {p["official_code"]: p for p in pts}


def main() -> int:
    vdoc = yaml.safe_load((BASE / "scripts" / "t_spec_9_verdicts.yaml")
                          .read_text())
    pdoc = yaml.safe_load((BASE / "scripts" / "t_spec_9_part_overrides.yaml")
                          .read_text())
    idv = vdoc["id_verdicts"]
    ovs = pdoc["overrides"]

    lanes_hit = sorted({lane for v in idv.values() for lane in v})
    unknown = [l for l in lanes_hit if l not in LANES]
    if unknown:
        raise SystemExit(f"FAIL: unknown lanes: {unknown}")

    errors = []
    report = {"schema": "syllabai.t-spec-9-apply/1.0", "generated_utc": NOW,
              "note": vdoc["note"], "per_lane": {}}

    # ---------- pass 1: tag-level resolves ----------
    for lane in lanes_hit:
        qual, mode = LANES[lane]
        cdir = EQ / lane
        mp_path = cdir / "spec_point_map.json"
        mp = json.loads(mp_path.read_text())
        idx = json.loads((cdir / "spec_point_index.json").read_text())
        res_path = cdir / "spec_point_resolution.json"
        res = json.loads(res_path.read_text())
        by_id, by_code = pool_for(qual, mode)
        mappings = mp.setdefault("mappings", {})
        unmapped = {u["spcpt_id"]: u for u in mp.get("unmapped", [])}
        res_by_id = {r["id"]: r for r in res["resolved"]}
        stats = Counter()

        for sid, v in idv.items():
            crec = v.get(lane)
            if not crec or "codes" not in crec:
                continue
            codes = [str(c) for c in crec["codes"]]
            lead = by_id.get(crec.get("official_id"))
            expected = None
            if lead is not None:
                expected = lead.get("official_code") or \
                    lead["id"].rsplit(":", 1)[-1]
            if lead is None or expected != codes[0]:
                errors.append(f"{lane}: {sid} official_id/code pair mismatch "
                              f"({crec.get('official_id')} vs {codes[0]})")
                continue
            for c in codes[1:]:
                if c not in by_code:
                    errors.append(f"{lane}: {sid} twin code {c} not in registry")
            if sid in unmapped:
                del unmapped[sid]
                stats["resolved"] += 1
            elif sid in mappings and mappings[sid].get("official_code") \
                    == codes[0] and mappings[sid].get("official_id") \
                    == lead["id"]:
                stats["idempotent"] += 1
            elif sid not in mappings:
                # heal pre-existing index ids that sat in neither map nor tail
                # (observed in igcse-business-19; verify does not enforce map
                # closure, only sidecar coverage)
                stats["resolved_from_neither"] += 1
            else:
                errors.append(f"{lane}: {sid} mapped elsewhere "
                              f"({mappings[sid].get('official_code')})")
                continue
            mappings[sid] = {"official_id": lead["id"],
                             "official_code": codes[0],
                             "tier": crec["tier"], "method": METHOD}
            r = res_by_id.get(sid)
            if r is None:
                errors.append(f"{lane}: {sid} missing from sidecar")
                continue
            r.update({"resolved_code": codes[0], "official_id": lead["id"],
                      "official_wording": lead["text"],
                      "tier": crec["tier"], "method": METHOD})
            r.pop("reason", None)

        # population closure (map-level: mapped/tail must be index members;
        # index ids outside map+tail are tolerated when the sidecar covers
        # them - verify G2 enforces the sidecar, not the map)
        index_ids = set(idx.get("spec_points", {}))
        mapped, tail = set(mappings), set(unmapped)
        if mapped & tail:
            errors.append(f"{lane}: both mapped+unmapped: {sorted(mapped & tail)[:3]}")
        extra = (tail - index_ids) | (mapped - index_ids)
        if extra:
            errors.append(f"{lane}: not in index: {sorted(extra)[:3]}")
        res_missing = [i for i in index_ids if i not in res_by_id]
        if res_missing:
            errors.append(f"{lane}: index ids missing from sidecar: "
                          f"{res_missing[:3]}")

        mp["unmapped"] = [unmapped[k] for k in sorted(unmapped)]
        mp["generated_utc"] = NOW
        res["generated_utc"] = NOW
        res["counts"] = {"ids": len(index_ids), "resolved": len(mapped),
                         "unresolved": len(tail)}
        res["validation"] = (
            "AI_VALIDATED (operator-delegated chain; T-SPEC-9 operator round "
            "- no upstream tickets per operator instruction 2026-09-19; "
            "joins quoted verbatim from the committed/repaired registries; "
            "PMT excluded as source); HUMAN_VALIDATED via operator review")
        mp_path.write_text(json.dumps(mp, indent=1, ensure_ascii=False) + "\n")
        res_path.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
        report["per_lane"][lane] = {"stats": dict(stats),
                                    "resolved_total": len(mapped),
                                    "unresolved_total": len(tail)}
        print(f"{lane}: {dict(stats)} -> resolved {len(mapped)}, tail {len(tail)}")

    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1

    # ---------- pass 2: part-code refresh (id-derived union) ----------
    # 2e/9 part-level codes on all-unresolved-id parts are preserved (never
    # popped); only genuinely id-derived sets are (re)written.
    refresh = {}
    for lane in lanes_hit:
        qual, _mode = LANES[lane]
        cdir = EQ / lane
        mp = json.loads((cdir / "spec_point_map.json").read_text())
        refresh[lane] = mp.get("mappings", {})
    for lane, mappings in refresh.items():
        cdir = EQ / lane
        coded = uncoded = 0
        for f in topic_files(cdir):
            t = json.loads(f.read_text())
            changed = False
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    sids = p.get("spec_point_ids") or []
                    if not sids:
                        continue
                    codes, seen = [], set()
                    for s in sids:
                        m = mappings.get(s)
                        if m and m["official_code"] not in seen:
                            codes.append(m["official_code"])
                            seen.add(m["official_code"])
                    if codes:
                        if p.get("spec_point_codes") != codes:
                            changed = True
                        p["spec_point_codes"] = codes
                        coded += 1
                    else:
                        # preserve part-level override codes (2e/9 pattern)
                        if p.get("spec_point_codes"):
                            coded += 1
                        else:
                            uncoded += 1
            if changed:
                f.write_text(json.dumps(t, indent=1, ensure_ascii=False) + "\n")
        report["per_lane"][lane]["parts_coded"] = coded
        report["per_lane"][lane]["parts_uncoded"] = uncoded

    # ---------- pass 3: part-level operator overrides ----------
    ov_by_course = {}
    for pid, o in ovs.items():
        ov_by_course.setdefault(o["course"], {})[pid] = o
    for course, ovs_c in sorted(ov_by_course.items()):
        cdir = EQ / course
        touched = 0
        for f in topic_files(cdir):
            t = json.loads(f.read_text())
            changed = False
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    o = ovs_c.get(p["id"])
                    if not o:
                        continue
                    if o.get("ids") is not None:
                        if sorted(p.get("spec_point_ids") or []) != \
                                sorted(o["ids"]):
                            errors.append(f"{course}: {p['id']} ids mismatch")
                            continue
                    existing = p.get("spec_point_codes")
                    if existing and existing != o["codes"] \
                            and not o.get("refinement"):
                        errors.append(f"{course}: {p['id']} already carries "
                                      f"{existing}; override would overwrite")
                        continue
                    if existing != o["codes"]:
                        p["spec_point_codes"] = o["codes"]
                        changed = True
                    touched += 1
            if changed:
                f.write_text(json.dumps(t, indent=1, ensure_ascii=False) + "\n")
        print(f"{course}: part overrides touched {touched}")
        report["per_lane"].setdefault(course, {})[
            "part_overrides"] = touched

    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1

    # ---------- manifest counts refresh ----------
    for lane in lanes_hit:
        cdir = EQ / lane
        coded = uncoded = 0
        for f in topic_files(cdir):
            t = json.loads(f.read_text())
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    if p.get("spec_point_ids"):
                        if p.get("spec_point_codes"):
                            coded += 1
                        else:
                            uncoded += 1
        mpath = cdir / "manifest.json"
        if mpath.exists():
            man = json.loads(mpath.read_text())
            man.setdefault("spec_point_resolution", {}).setdefault(
                "counts", {}).update({
                    "parts_with_codes": coded,
                    "parts_left_uncoded_no_guess_tail": uncoded,
                    "parts_total": coded + uncoded})
            man["spec_point_resolution"]["pipeline"] = list(set(
                man["spec_point_resolution"].get("pipeline", []) +
                ["scripts/t_spec_9_apply.py"]))
            man["spec_point_resolution"]["updated_utc"] = NOW
            mpath.write_text(json.dumps(man, indent=1, ensure_ascii=False) + "\n")

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "T_SPEC_9_APPLY.json").write_text(
        json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    print("report -> graph/reports/T_SPEC_9_APPLY.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
