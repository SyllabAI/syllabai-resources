#!/usr/bin/env python3
"""T-SPEC-4 — apply the physics-family spec-point verdicts
(scripts/t_spec_4_verdicts.yaml) to the four physics courses:

  igcse-physics-19                          (qual igcse-physics)
  igcse-physics-modular-24-unit-1           (qual igcse-physics-modular)
  igcse-physics-modular-24-unit-2           (qual igcse-physics-modular)
  igcse-science-double-award-17-physics     (qual igcse-science-double-award, scope Physics)

Fail-closed rules (hard errors before ANY write):
  - population closure: verdict ids == per-course unmapped ids + registry-gap
    ids (indexed-but-absent-from-map), exactly
  - every resolve code must exist in the course's OWN registry universe
    (SDA filtered to scope Physics — same universe verify G1 enforces)
  - V1 evidence: committed SME definition must be token-contained in the
    registry statement text
  - V2 evidence: registry statement text must be token-contained in the
    committed SME definition; every recorded sub_item must be token-contained
    in BOTH the definition and the statement's own sub_items; statements
    without sub_items need >=5 statement tokens (guards lead-only joins)
  - V2 multi evidence: as V2 for the primary, plus the twin statement text
    token-contained in the same committed definition
  - operator-override: requires ticket + verbatim reason; code must exist in
    the registry; clearly marked in every record (chemistry T-SPEC-2e
    precedent — operator opinion, re-verdict supported)
  - pending: courses + verbatim reason required
Token validation is punctuation-normalised at token edges ONLY (SME pages
carry trailing periods inside bullets, e.g. "white dwarf."); containment is
otherwise exact.

Writes (after validation passes):
  - spec_point_map.json: verdict resolutions merged into mappings, removed
    from unmapped (map lane — flashcard inheritance + spec-links read this);
    pending ids appended so mappings+unmapped partitions every index id
  - spec_point_resolution.json sidecar covering EVERY index id (verify G2)
  - spec_point_codes written on all parts with ids (id-derived) — verify G1
  - graph/reports/T_SPEC_4_PHY_VERDICTS.{md,json}

PMT (PhysicsAndMathsTutor) excluded as an evidence source (operator
instruction 2026-09-18); no PMT content appears in any record.
"""
import json
import sys
import time
from collections import Counter
from pathlib import Path

import yaml

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
PARSED = BASE / "Official-Specifications" / "parsed"
REPORTS = BASE / "graph" / "reports"

sys.path.insert(0, str(BASE / "scripts"))
import sme_spcpt_sibling_map as sm  # ntokens, _stem

COURSES = {
    "igcse-physics-19": ("igcse-physics", None),
    "igcse-physics-modular-24-unit-1": ("igcse-physics-modular", None),
    "igcse-physics-modular-24-unit-2": ("igcse-physics-modular", None),
    "igcse-science-double-award-17-physics": ("igcse-science-double-award", "Physics"),
}

METHOD_VERBATIM = ("operator-verdict-definition-verbatim "
                   "(T-SPEC-4; PMT excluded as source)")
METHOD_OVERRIDE = ("operator-override (T-SPEC-4; ticket #11; clearly marked "
                   "operator opinion; re-verdict supported; PMT excluded as source)")

_STRIP = ".,;:!?\"'()[]"


def vtok(s: str) -> set:
    """ntokens with punctuation-normalised token edges (both sides)."""
    out = set()
    for t in sm.ntokens(s or ""):
        t2 = t.strip(_STRIP)
        if not t2:
            continue
        out.add(t2)
        out.add(sm._stem(t2))
    return out


def registry(qual, scope):
    pts = json.loads((PARSED / qual / "spec_points.json")
                     .read_text(encoding="utf-8"))["spec_points"]
    if scope:
        scoped = [p for p in pts if p.get("scope") == scope]
        if scoped:
            pts = scoped
    return pts


def topic_files(cdir: Path):
    return sorted(cdir.glob("*/*/*/topic.json")) + sorted(cdir.glob("*/*/topic.json"))


def main() -> int:
    t0 = time.time()
    doc = yaml.safe_load((BASE / "scripts" / "t_spec_4_verdicts.yaml").read_text())
    idv = doc["id_verdicts"]

    # ---------- load per-course state ----------
    state = {}
    for course, (qual, scope) in COURSES.items():
        cdir = EQ / course
        mp = json.loads((cdir / "spec_point_map.json").read_text(encoding="utf-8"))
        idx = json.loads((cdir / "spec_point_index.json").read_text(encoding="utf-8"))
        pts = registry(qual, scope)
        state[course] = {
            "qual": qual, "scope": scope, "dir": cdir,
            "map": mp, "index": idx, "reg": pts,
            "by_code": {p["official_code"]: p for p in pts},
            "order": {p["id"]: i for i, p in enumerate(pts)},
            "mappings": mp.get("mappings", {}),
            "unmapped": {u["spcpt_id"]: u.get("reason", "") for u in mp.get("unmapped", [])},
        }

    # registry-gap ids: in index but in neither mappings nor unmapped
    gaps = {}
    for course, st in state.items():
        covered = set(st["mappings"]) | set(st["unmapped"])
        for sid in st["index"]["spec_points"]:
            if sid not in covered:
                gaps.setdefault(sid, []).append(course)

    # ---------- population closure ----------
    errors = []
    need = {}
    for course, st in state.items():
        for sid in st["unmapped"]:
            need.setdefault(sid, set()).add(course)
    for sid, cs in gaps.items():
        need.setdefault(sid, set()).update(cs)

    yids = set(idv)
    if yids != set(need):
        errors.append(f"population mismatch: yaml-only={sorted(yids - set(need))} "
                      f"need-only={sorted(set(need) - yids)}")
    for sid, cs in need.items():
        v = idv.get(sid) or {}
        if v.get("verdict") == "resolve":
            want = set(v.get("codes") or {})
        else:
            want = set(v.get("courses") or [])
        if want != cs:
            errors.append(f"{sid}: verdict course set {sorted(want)} != required {sorted(cs)}")

    # ---------- evidence validation ----------
    for sid, v in idv.items():
        if v["verdict"] == "pending":
            if not (v.get("courses") and v.get("reason")):
                errors.append(f"{sid}: pending without courses/reason")
            continue
        if v["verdict"] != "resolve":
            errors.append(f"{sid}: unknown verdict {v['verdict']!r}")
            continue
        tier = v.get("tier", "")
        for course, code in (v.get("codes") or {}).items():
            st = state[course]
            if code not in st["by_code"]:
                errors.append(f"{sid}: code {code} not in {course} registry")
                continue
            stmt = st["by_code"][code]
            e = st["index"]["spec_points"].get(sid) or {}
            dtext = (e.get("definition") or "").strip()
            if dtext == "nan":
                dtext = ""
            dtok = vtok(dtext)
            stok = vtok(stmt.get("text") or "")
            if tier == "operator-override":
                if not v.get("ticket") or not v.get("reason"):
                    errors.append(f"{sid}: override requires ticket + reason")
                continue
            if not dtok:
                errors.append(f"{sid}: no committed definition to join against")
                continue
            if tier == "V1_definition_fragment_in_statement":
                if not dtok.issubset(stok):
                    errors.append(f"{sid}/{course}: V1 def not contained in {code} text")
            elif tier.startswith("V2_statement_contained_in_definition"):
                if not stok.issubset(dtok):
                    errors.append(f"{sid}/{course}: V2 statement {code} not contained in def")
                if len(stok) < 5 and not stmt.get("sub_items"):
                    errors.append(f"{sid}/{course}: V2 statement too short without sub_items")
                rec_si = v.get("sub_items") or []
                stmt_si = stmt.get("sub_items") or []
                if stmt_si and not rec_si:
                    errors.append(f"{sid}/{course}: V2 on sub_item statement without "
                                  f"recorded sub_items (lead-only joins refused)")
                for si in rec_si:
                    if not vtok(si).issubset(vtok(" | ".join(stmt_si))):
                        errors.append(f"{sid}/{course}: recorded sub_item not in {code} "
                                      f"sub_items: {si!r}")
                    if not vtok(si).issubset(dtok):
                        errors.append(f"{sid}/{course}: recorded sub_item not in "
                                      f"committed definition: {si!r}")
                if stmt_si and not any(vtok(si).issubset(dtok) for si in stmt_si):
                    errors.append(f"{sid}/{course}: no statement sub_item verbatim in def")
                if tier == "V2_statement_contained_in_definition_multi":
                    twin_codes = (v.get("twin_codes") or {})
                    tc = twin_codes.get(course)
                    if not tc:
                        errors.append(f"{sid}/{course}: multi tier without twin code")
                    elif tc not in st["by_code"]:
                        errors.append(f"{sid}/{course}: twin {tc} not in {course} registry")
                    elif not vtok(st["by_code"][tc].get("text") or "").issubset(dtok):
                        errors.append(f"{sid}/{course}: twin {tc} text not contained in def")
            else:
                errors.append(f"{sid}: unknown tier {tier!r}")

    if errors:
        print("VALIDATION FAILED — no writes performed:")
        for e in errors:
            print("  -", e)
        return 1

    # ---------- apply ----------
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    summary = {}

    for course, (qual, scope) in COURSES.items():
        st = state[course]
        cdir = st["dir"]
        merged_into_map = 0

        # 1) map merge
        for sid, v in idv.items():
            if v["verdict"] != "resolve" or course not in v.get("codes", {}):
                continue
            code = v["codes"][course]
            entry = st["by_code"][code]
            override = v["tier"] == "operator-override"
            st["mappings"][sid] = {
                "official_id": entry["id"],
                "official_code": code,
                "tier": v["tier"],
                "score": None if override else 1.0,
                "unit": None,
                "method": METHOD_OVERRIDE if override else METHOD_VERBATIM,
                "resolution": {
                    "lane": "operator-verdict (T-SPEC-4)",
                    "quote": v.get("quote"),
                    "sub_items": v.get("sub_items"),
                    "twin_codes": (v.get("twin_codes") or {}).get(course),
                    "ticket": v.get("ticket"),
                    "pmt_excluded": True,
                },
            }
            st["unmapped"].pop(sid, None)
            merged_into_map += 1

        # 2) write map (mappings + partition-completing unmapped list)
        mp = st["map"]
        mp["mappings"] = st["mappings"]
        present = set()
        um = []
        for sid in sorted(st["unmapped"]):
            reason = st["unmapped"][sid] or (idv.get(sid, {}).get("reason")
                                             if idv.get(sid, {}).get("verdict") == "pending"
                                             else None) or "unresolved (T-SPEC-4 tail)"
            um.append({"spcpt_id": sid, "name": None, "reason": reason})
        mp["unmapped"] = um
        for u in mp["unmapped"]:
            u["name"] = (st["index"]["spec_points"].get(u["spcpt_id"], {}) or {}).get("name")
            present.add(u["spcpt_id"])
        for sid, v in idv.items():
            if v.get("verdict") == "pending" and course in (v.get("courses") or []) \
                    and sid not in present:
                mp["unmapped"].append({
                    "spcpt_id": sid,
                    "name": (st["index"]["spec_points"].get(sid, {}) or {}).get("name"),
                    "reason": v["reason"],
                })
        (cdir / "spec_point_map.json").write_text(
            json.dumps(mp, ensure_ascii=False, indent=1), encoding="utf-8")

        # 3) resolution sidecar covering EVERY index id (verify G2)
        part_refs = Counter()
        for f in topic_files(cdir):
            t = json.loads(f.read_text(encoding="utf-8"))
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    for s in p.get("spec_point_ids") or []:
                        part_refs[s] += 1

        records = []
        for sid, e in st["index"]["spec_points"].items():
            rec = {"id": sid, "sme_name": e.get("name"),
                   "sme_definition": e.get("definition"),
                   "referenced_by_parts": part_refs.get(sid, 0)}
            m = st["mappings"].get(sid)
            if m:
                stmt = st["by_code"].get(m["official_code"], {})
                rec.update({
                    "resolved_code": m["official_code"],
                    "official_id": m["official_id"],
                    "official_wording": stmt.get("text"),
                    "tier": m["tier"], "score": m.get("score"),
                    "method": m.get("method"), "unit": m.get("unit"),
                    "flag": m.get("flag"), "recheck": m.get("recheck"),
                })
            else:
                v = idv.get(sid) or {}
                rec["resolved_code"] = None
                rec["reason"] = v.get("reason") if v.get("verdict") == "pending" \
                    else "unresolved (T-SPEC-4: no verdict; honest tail)"
            records.append(rec)

        res_doc = {
            "schema": "syllabai.sme-spec-point-resolution/1.0",
            "generated_utc": now,
            "validation": "AI_VALIDATED (operator-delegated chain; verbatim "
                          "definition/statement joins per T-SPEC-4; one "
                          "clearly-marked operator override per ticket #11); "
                          "HUMAN_VALIDATED reserved for human review",
            "counts": {
                "ids": len(records),
                "resolved": sum(1 for r in records if r.get("resolved_code")),
                "unresolved": sum(1 for r in records if not r.get("resolved_code")),
            },
            "unresolved_allowlist_note": "parts whose ids are all unresolved stay "
                                         "uncoded by design (no-guess discipline)",
            "resolved": records,
        }
        (cdir / "spec_point_resolution.json").write_text(
            json.dumps(res_doc, ensure_ascii=False, indent=1), encoding="utf-8")

        # 4) part codes: id-derived
        coded = uncoded = 0
        for f in topic_files(cdir):
            t = json.loads(f.read_text(encoding="utf-8"))
            changed = False
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    sids = p.get("spec_point_ids") or []
                    if not sids:
                        continue
                    codes, seen = [], set()
                    for s in sids:
                        m = st["mappings"].get(s)
                        if m and m["official_code"] not in seen:
                            codes.append(m["official_code"])
                            seen.add(m["official_code"])
                    codes.sort(key=lambda c: st["order"].get(
                        st["by_code"][c]["id"], 10**9))
                    if codes:
                        p["spec_point_codes"] = codes
                        coded += 1
                        changed = True
                    else:
                        uncoded += 1
            if changed:
                f.write_text(json.dumps(t, ensure_ascii=False, indent=1),
                             encoding="utf-8")

        res_n = res_doc["counts"]["resolved"]
        summary[course] = {
            "ids": len(records), "resolved": res_n,
            "unresolved": res_doc["counts"]["unresolved"],
            "map_merged": merged_into_map,
            "parts_coded": coded, "parts_uncoded": uncoded,
        }
        print(f"[{course}] resolved {res_n}/{len(records)} ids "
              f"(+{merged_into_map} map merges); parts coded {coded}, "
              f"uncoded {uncoded}")

    # ---------- report ----------
    REPORTS.mkdir(parents=True, exist_ok=True)
    report = {
        "schema": "syllabai.t-spec-4-report/1.0",
        "generated_utc": now,
        "courses": list(COURSES),
        "summary": summary,
        "id_verdicts": {
            sid: {k: val for k, val in v.items() if k != "rationale"}
            for sid, v in idv.items()
        },
        "upstream_ticket": 11,
        "pmt_excluded": True,
    }
    (REPORTS / "T_SPEC_4_PHY_VERDICTS.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")

    md = ["# T-SPEC-4 — physics family spec-point verdicts (2026-09-19)", ""]
    md += ["Verbatim definition/statement joins on the physics tail; one "
           "clearly-marked operator override (Galactic redshift -> 8.17P, "
           "ticket #11); 32 honest pendings with zero content anchors "
           "(2 video tags + 30 SDA page-only tags, ticket #11). PMT excluded "
           "as source.", ""]
    md += ["| course | ids | resolved | map merges | parts coded | parts uncoded |",
           "|---|---|---|---|---|---|"]
    for c, s in summary.items():
        md.append(f"| {c} | {s['ids']} | {s['resolved']} | {s['map_merged']} | "
                  f"{s['parts_coded']} | {s['parts_uncoded']} |")
    md += ["", "## id verdicts", ""]
    for sid, v in idv.items():
        name = v.get("quote", "")[:60]
        md.append(f"- `{sid}` {v['verdict']} {v.get('tier','')} — {name}…")
    md.append("")
    (REPORTS / "T_SPEC_4_PHY_VERDICTS.md").write_text("\n".join(md), encoding="utf-8")

    Path("/home/z/my-project/scripts/specmap_work").mkdir(parents=True, exist_ok=True)
    (Path("/home/z/my-project/scripts/specmap_work") / "t_spec_4_apply_summary.json").write_text(
        json.dumps({"generated_utc": now, "courses": summary}, indent=1))
    print(f"report -> {REPORTS / 'T_SPEC_4_PHY_VERDICTS.md'}")
    print(f"done in {time.time()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
