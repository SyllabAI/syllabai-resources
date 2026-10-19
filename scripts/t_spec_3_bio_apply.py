#!/usr/bin/env python3
"""T-SPEC-3 — apply the biology-family spec-point verdicts
(scripts/t_spec_3_verdicts.yaml) to the four biology courses:

  igcse-biology-19                        (qual igcse-biology)
  igcse-biology-modular-24-unit-1         (qual igcse-biology-modular)
  igcse-biology-modular-24-unit-2         (qual igcse-biology-modular)
  igcse-science-double-award-17-biology   (qual igcse-science-double-award, scope Biology)

Fail-closed rules (hard errors before ANY write):
  - population closure: verdict ids == per-course unmapped ids + registry-gap
    ids (indexed-but-absent-from-map), exactly
  - every resolve code must exist in the course's OWN registry universe
    (SDA filtered to scope Biology — same universe verify G1 enforces)
  - V1 evidence: the committed SME definition/quote must be token-contained
    in the registry statement text (sub_item checks included)
  - V3 evidence: quote must be token-contained in a committed flashcard front
  - part verdicts: part must exist, anchor the merged id, quotes must be
    token-contained in the named committed field
Writes (after validation passes):
  - spec_point_map.json: verdict entries merged into mappings, removed from
    unmapped (map lane — flashcard inheritance reads this)
  - spec_point_resolution.json sidecar covering EVERY index id (verify G2)
  - spec_point_codes written on all parts with ids (id-derived, superseded
    by part verdicts where present) — verify G1 universe
  - graph/reports/T_SPEC_3_BIO_VERDICTS.{md,json}

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
FC = BASE / "SME-Flashcards"

sys.path.insert(0, str(BASE / "scripts"))
import sme_spcpt_sibling_map as sm  # ntokens

COURSES = {
    "igcse-biology-19": ("igcse-biology", None),
    "igcse-biology-modular-24-unit-1": ("igcse-biology-modular", None),
    "igcse-biology-modular-24-unit-2": ("igcse-biology-modular", None),
    "igcse-science-double-award-17-biology": ("igcse-science-double-award", "Biology"),
}
MERGED_ID = "spcpt_YKpJHS4ZTM4qnrV7"  # Xylem & Phloem — the only id with part verdicts

METHOD_V1 = "operator-verdict-definition-verbatim (T-SPEC-3; PMT excluded as source)"
METHOD_V3 = "operator-verdict-content-convergent (T-SPEC-3; PMT excluded as source)"


def registry(qual, scope):
    pts = json.loads((PARSED / qual / "spec_points.json")
                     .read_text(encoding="utf-8"))["spec_points"]
    if scope:
        scoped = [p for p in pts if p.get("scope") == scope]
        pts = scoped or pts
    return pts


def topic_files(cdir: Path):
    return sorted(cdir.glob("*/*/*/topic.json")) + sorted(cdir.glob("*/*/topic.json"))


def main() -> int:
    t0 = time.time()
    doc = yaml.safe_load((BASE / "scripts" / "t_spec_3_verdicts.yaml").read_text())
    idv, partv = doc["id_verdicts"], doc["part_verdicts"]

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
            "by_oid": {p["id"]: p for p in pts},
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
    need = {}   # sid -> set(courses) where verdict required
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
        want = {c for c in cs if c in v.get("codes", {})} if v.get("verdict") == "resolve" \
            else set(v.get("courses") or [])
        if want != cs:
            errors.append(f"{sid}: verdict course set {sorted(want)} != required {sorted(cs)}")

    # ---------- evidence validation ----------
    for sid, v in idv.items():
        if v["verdict"] == "pending":
            continue
        for course, code in (v.get("codes") or {}).items():
            st = state[course]
            if code not in st["by_code"]:
                errors.append(f"{sid}: code {code} not in {course} registry")
                continue
            stmt = st["by_code"][code]
            hay = sm.ntokens(stmt.get("text") or "")
            q = sm.ntokens(v.get("quote") or "")
            if v["tier"] != "V3_convergent" and q and not q.issubset(hay):
                errors.append(f"{sid}: quote not contained in {course} {code} statement text")
            si = v.get("sub_item")
            if si:
                subs = " | ".join(stmt.get("sub_items") or [])
                if not sm.ntokens(si).issubset(sm.ntokens(subs)):
                    errors.append(f"{sid}: sub_item {si!r} not in {course} {code} sub_items")
            twin = (v.get("twin") or {}).get(course)
            if twin and twin not in st["by_code"]:
                errors.append(f"{sid}: twin {twin} not in {course} registry")
        if v["tier"] == "V3_convergent":
            q = sm.ntokens(v.get("quote") or "")
            fronts = []
            for course in v["codes"]:
                for df in FC.glob(f"{course}/*/*/deck.json"):
                    d = json.loads(df.read_text(encoding="utf-8"))
                    fronts += [(c.get("front_md") or "") for c in d.get("cards", [])]
            if not any(q.issubset(sm.ntokens(f)) for f in fronts):
                errors.append(f"{sid}: V3 quote not found in any committed flashcard front")

    # ---------- part verdict validation ----------
    part_cache = {}
    for pid, v in partv.items():
        course = v["course"]
        st = state[course]
        hit = None
        for f in topic_files(st["dir"]):
            t = json.loads(f.read_text(encoding="utf-8"))
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    if p.get("id") == pid:
                        hit = (f, t, q, p)
        if not hit:
            errors.append(f"part {pid}: not found in {course}")
            continue
        part_cache[pid] = hit
        _, _, _, p = hit
        if MERGED_ID not in (p.get("spec_point_ids") or []):
            errors.append(f"part {pid}: does not anchor the merged id {MERGED_ID}")
        for c in v["codes"]:
            if c not in st["by_code"]:
                errors.append(f"part {pid}: code {c} not in {course} registry")
        for ev in v.get("quotes") or []:
            field, text = ev["field"], ev["text"]
            hay = sm.ntokens(p.get(field) or "")
            if not sm.ntokens(text).issubset(hay):
                errors.append(f"part {pid}: quote not contained in committed {field}")

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

        # 1) map merge: verdict resolutions enter the map lane (flashcard
        #    inheritance + spec-links read mappings)
        for sid, v in idv.items():
            if v["verdict"] != "resolve" or course not in v["codes"]:
                continue
            code = v["codes"][course]
            entry = st["by_code"][code]
            st["mappings"][sid] = {
                "official_id": entry["id"],
                "official_code": code,
                "tier": v["tier"],
                "score": 1.0 if v["tier"] == "V1_definition_verbatim" else None,
                "unit": None,
                "method": METHOD_V1 if v["tier"] == "V1_definition_verbatim" else METHOD_V3,
                "resolution": {
                    "lane": "operator-verdict (T-SPEC-3)",
                    "quote": v.get("quote"),
                    "sub_item": v.get("sub_item"),
                    "twin_codes": (v.get("twin") or {}).get(course),
                    "pmt_excluded": True,
                },
            }
            st["unmapped"].pop(sid, None)
            merged_into_map += 1

        # write map: mappings + rebuilt unmapped list (restore names for
        # remaining unmapped entries from the index; pending-verdict registry
        # gaps (indexed-but-never-in-map, e.g. KW2X5) are appended so the
        # map's mappings+unmapped partition covers every index id again)
        mp = st["map"]
        mp["mappings"] = st["mappings"]
        mp["unmapped"] = [{"spcpt_id": sid, "name": None, "reason": reason}
                          for sid, reason in sorted(st["unmapped"].items())]
        for u in mp["unmapped"]:
            u["name"] = (st["index"]["spec_points"].get(u["spcpt_id"], {}) or {}).get("name")
        present = {u["spcpt_id"] for u in mp["unmapped"]}
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

        # 2) resolution sidecar covering EVERY index id (verify G2)
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
                stmt = st["by_oid"].get(m["official_id"], {})
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
                    else "unresolved (T-SPEC-3: no verdict; honest tail)"
            records.append(rec)

        res_doc = {
            "schema": "syllabai.sme-spec-point-resolution/1.0",
            "generated_utc": now,
            "validation": "AI_VALIDATED (operator-delegated chain; verbatim-"
                          "definition joins per T-SPEC-3); HUMAN_VALIDATED "
                          "reserved for human review",
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

        # 3) part codes: id-derived, superseded by part verdicts
        coded = uncoded = superseded = 0
        for f in topic_files(cdir):
            t = json.loads(f.read_text(encoding="utf-8"))
            changed = False
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    sids = p.get("spec_point_ids") or []
                    if not sids:
                        continue
                    pv = partv.get(p["id"])
                    if pv and pv["course"] == course:
                        codes, seen = [], set()
                        for c in sorted(pv["codes"],
                                        key=lambda c: st["order"].get(
                                            st["by_code"][c]["id"], 10**9)):
                            if c not in seen:
                                codes.append(c)
                                seen.add(c)
                        superseded += 1
                    else:
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
            "part_verdicts_applied": superseded,
        }
        print(f"[{course}] resolved {res_n}/{len(records)} ids "
              f"(+{merged_into_map} map merges); parts coded {coded}, "
              f"uncoded {uncoded}, part-verdicts {superseded}")

    # ---------- report ----------
    REPORTS.mkdir(parents=True, exist_ok=True)
    report = {
        "schema": "syllabai.t-spec-3-report/1.0",
        "generated_utc": now,
        "courses": list(COURSES),
        "summary": summary,
        "id_verdicts": {
            sid: {k: val for k, val in v.items() if k != "rationale"}
            for sid, v in idv.items()
        },
        "part_verdicts": partv,
        "pmt_excluded": True,
    }
    (REPORTS / "T_SPEC_3_BIO_VERDICTS.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")

    md = ["# T-SPEC-3 — biology family spec-point verdicts (2026-09-19)", ""]
    md += ["Verbatim-definition joins on the honest biology tail; PMT excluded "
           "as source. Registry-coverage gaps repaired: "
           "spcpt_nNMTzc3PZPpMmSx9 (resolved 3.30/4.30/3.30), "
           "spcpt_KW2X5RdVFhDMwSws (unresolved, blocks nothing).", ""]
    md += ["| course | ids | resolved | map merges | parts coded | parts uncoded | part-verdicts |",
           "|---|---|---|---|---|---|---|"]
    for c, s in summary.items():
        md.append(f"| {c} | {s['ids']} | {s['resolved']} | {s['map_merged']} | "
                  f"{s['parts_coded']} | {s['parts_uncoded']} | "
                  f"{s['part_verdicts_applied']} |")
    md += ["", "## id verdicts", ""]
    for sid, v in idv.items():
        name = v.get("quote", "")[:60]
        md.append(f"- `{sid}` {v['verdict']} {v.get('tier','')} — {name}…")
    md += ["", "## part verdicts (supersede lane)", ""]
    for pid, v in partv.items():
        md.append(f"- `{pid}` ({v['course']}) -> {v['codes']}")
    md.append("")
    (REPORTS / "T_SPEC_3_BIO_VERDICTS.md").write_text("\n".join(md), encoding="utf-8")

    Path("/home/z/my-project/scripts/specmap_work").mkdir(parents=True, exist_ok=True)
    (Path("/home/z/my-project/scripts/specmap_work") / "t_spec_3_apply_summary.json").write_text(
        json.dumps({"generated_utc": now, "courses": summary}, indent=1))
    print(f"report -> {REPORTS / 'T_SPEC_3_BIO_VERDICTS.md'}")
    print(f"done in {time.time()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
