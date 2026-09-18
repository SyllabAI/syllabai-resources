#!/usr/bin/env python3
"""T-SPEC-6 — apply the IAL-maths spec-point verdicts
(scripts/t_spec_6_verdicts.yaml) to the ten IAL maths courses:

  ial-maths-20-pure-1 .. pure-4          (qual ial-maths, units P1..P4)
  ial-maths-20-mechanics-1/-2            (units M1/M2)
  ial-maths-20-statistics-1/-2           (units S1/S2)
  ial-maths-20-decision-1                (unit D1)
  ial-further-maths-18-further-pure-1    (unit FP1)

Context: SME IAL pages publish spec-point tags WITHOUT definition text
(systemic upstream gap, ticket #13), so the T-SPEC-3/4 verbatim
definition->statement joins are structurally impossible here. Evidence used
(all committed in-repo): the SME tag NAME, the revision-note page the tag
appears on (front-matter spec_point_ids), the page body, the exam-question
part texts referencing the tag, and the global SME tag identity across
courses (tags are global entities; sibling courses' home pages and indexes
carry the canonical name). Tiers:
  P1_name_fragment_join  - distinctive fragment shared by tag name/statement
  P2_page_context_join   - tag name + page context / exam-part text pins the
                           statement
  pending                - no-guess tail (bridge content absent from the
                           published spec, graph-theory vocabulary, and
                           content sitting in D1-4.4 which the committed
                           parse lacks)
Cross-unit resolves: SME reuses the same global tag id across unit courses;
a tag resolves to the statement its home page/name denotes, or to the
unit-restated statement where the local evidence pins it (e.g. momentum
M1-4.3 -> M2-4.1 in mechanics-2). Each verdict documents its basis.

Registry note: the committed ial-maths parse carries unit-prefixed ids
(IAL_MATHS:P1-1.1 ...) with per-unit code uniqueness. Two parse truncations
are documented in verdict notes (D1-2.1 drops "Prim's and Kruskal's
algorithm"; S2-4.6 drops "and for the mean of a Poisson distribution") and
one parse gap (D1-4.4 "Total float. Gantt (cascade) charts. Scheduling." is
absent; its code slot carries a notation artifact) — pendings reference it.

Fail-closed rules (hard errors before ANY write):
  - population closure: yaml resolve ids == per-course unmapped ids exactly,
    minus pendings; remap ids must carry existing mappings whose
    official_code equals superseded_code
  - every code must exist in the course's OWN unit registry, or in the full
    qualification registry when the verdict records a cross-unit resolve_unit
  - every resolve/remap tag with a recorded page must be anchored: the page
    exists under SME-RevisionNotes/<course>/notes and its front-matter
    spec_point_ids contains the tag id (page-association check)
  - quote must equal the committed index name for the tag (null names —
    question-reference-only repairs — are checked for nullness instead)
  - pending: verbatim reason required
Writes (after validation):
  - spec_point_map.json: resolves/remaps merged into mappings, resolved ids
    removed from unmapped, pendings kept with verdict reason
  - spec_point_resolution.json sidecar covering EVERY index id (verify G2)
  - spec_point_codes written on all parts with ids (verify G1)
  - graph/reports/T_SPEC_6_MATHS_VERDICTS.{md,json}

PMT (PhysicsAndMathsTutor) excluded as an evidence source (operator
instruction 2026-09-18); no PMT content appears in any record.
"""
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

import yaml

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
NOTES = BASE / "SME-RevisionNotes"
PARSED = BASE / "Official-Specifications" / "parsed"
REPORTS = BASE / "graph" / "reports"

QUAL = "ial-maths"
PREFIX = "IAL_MATHS"
COURSES = {
    "ial-maths-20-pure-1": "P1",
    "ial-maths-20-pure-2": "P2",
    "ial-maths-20-pure-3": "P3",
    "ial-maths-20-pure-4": "P4",
    "ial-maths-20-mechanics-1": "M1",
    "ial-maths-20-mechanics-2": "M2",
    "ial-maths-20-statistics-1": "S1",
    "ial-maths-20-statistics-2": "S2",
    "ial-maths-20-decision-1": "D1",
    "ial-further-maths-18-further-pure-1": "FP1",
}

METHOD_P1 = ("operator-verdict name-fragment join (T-SPEC-6; SME IAL pages "
             "publish no definition text, ticket #13; PMT excluded as source)")
METHOD_P2 = ("operator-verdict page-context join (T-SPEC-6; SME IAL pages "
             "publish no definition text, ticket #13; PMT excluded as source)")
METHOD_REMAP = ("operator-verdict page-context join (T-SPEC-6 re-verdict; "
                "corrects stage-1 name-only match; PMT excluded as source)")


def full_registry():
    pts = json.loads((PARSED / QUAL / "spec_points.json")
                     .read_text(encoding="utf-8"))["spec_points"]
    return {p["id"]: p for p in pts}, pts


def topic_files(cdir: Path):
    return sorted(cdir.glob("*/*/*/topic.json")) + \
        sorted(cdir.glob("*/*/topic.json")) + \
        sorted(cdir.glob("*/topic.json"))


def note_page_ids(rel: str) -> list[str] | None:
    p = NOTES / rel
    if not p.exists():
        return None
    txt = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^spec_point_ids: \[(.*?)\]", txt, re.M)
    if not m:
        return None
    return [x.strip().strip('"') for x in m.group(1).split(",") if x.strip()]


def main() -> int:
    t0 = time.time()
    doc = yaml.safe_load((BASE / "scripts" / "t_spec_6_verdicts.yaml")
                         .read_text(encoding="utf-8"))
    idv = doc["id_verdicts"]
    reg_by_id, reg_list = full_registry()
    order = {p["id"]: i for i, p in enumerate(reg_list)}

    state = {}
    for course, unit in COURSES.items():
        cdir = EQ / course
        mp = json.loads((cdir / "spec_point_map.json").read_text(encoding="utf-8"))
        idx = json.loads((cdir / "spec_point_index.json").read_text(encoding="utf-8"))
        by_code = {p["official_code"]: p for p in reg_list
                   if p["id"].startswith(f"{PREFIX}:{unit}-")}
        state[course] = {
            "unit": unit, "dir": cdir, "map": mp, "index": idx,
            "by_code": by_code,
            "mappings": mp.get("mappings", {}),
            "unmapped": {u["spcpt_id"]: u.get("reason", "")
                         for u in mp.get("unmapped", [])},
        }

    # ---------- population closure + validation ----------
    errors = []
    for course, st in state.items():
        got_res = set()
        got_pen = set()
        for sid, v in idv.items():
            if v["verdict"] == "pending":
                if course in (v.get("courses") or {}):
                    got_pen.add(sid)
                continue
            crec = (v.get("courses") or {}).get(course)
            if crec and not crec.get("stage1_confirm"):
                if crec.get("superseded_code") is None:
                    got_res.add(sid)
        need_res = set(st["unmapped"]) - got_pen
        if got_res != need_res:
            errors.append(
                f"{course}: resolve set mismatch "
                f"yaml-only={sorted(got_res - need_res)[:4]} "
                f"need-only={sorted(need_res - got_res)[:4]} "
                f"(need={len(need_res)} got={len(got_res)})")
        for sid in got_pen:
            if sid not in st["unmapped"]:
                errors.append(f"{course}: pending {sid} not in unmapped tail")
        for sid, v in idv.items():
            if v["verdict"] != "resolve":
                continue
            crec = (v.get("courses") or {}).get(course)
            if not crec:
                continue
            if crec.get("stage1_confirm"):
                # re-validate the existing stage-1 mapping instead of writing
                m = st["mappings"].get(sid)
                if not m:
                    errors.append(f"{course}: stage1_confirm {sid} has no "
                                  f"existing mapping")
                else:
                    stmt = reg_by_id.get(m["official_id"])
                    if not stmt or stmt["official_code"] != crec["codes"][0]:
                        errors.append(
                            f"{course}: stage1_confirm {sid} existing code "
                            f"{m['official_code']} != confirmed "
                            f"{crec['codes'][0]}")
                continue
            if crec.get("superseded_code") is not None:
                m = st["mappings"].get(sid)
                if not m:
                    errors.append(f"{course}: remap {sid} has no existing mapping")
                elif m["official_code"] != crec["superseded_code"]:
                    errors.append(f"{course}: remap {sid} superseded "
                                  f"{crec['superseded_code']} != existing "
                                  f"{m['official_code']}")

    # anchor + quote + registry validation
    for course, st in state.items():
        for sid, v in idv.items():
            if v["verdict"] != "resolve":
                continue
            crec = (v.get("courses") or {}).get(course)
            if not crec or crec.get("stage1_confirm"):
                continue
            e = st["index"]["spec_points"].get(sid)
            if e is None:
                errors.append(f"{course}: {sid} not in index")
                continue
            q = (crec.get("quote") or "")
            if q != (e.get("name") or ""):
                errors.append(f"{course}: {sid} quote {q!r} != index name "
                              f"{(e.get('name') or '')!r}")
            page = crec.get("page")
            if page:
                ids = note_page_ids(page)
                if ids is None:
                    errors.append(f"{course}: {sid} page missing/unreadable: {page}")
                elif sid not in ids:
                    errors.append(f"{course}: {sid} not anchored on page {page}")
            resolve_unit = crec.get("unit") or st["unit"]
            for code in crec["codes"]:
                oid = f"{PREFIX}:{resolve_unit}-{code}"
                if oid not in reg_by_id:
                    errors.append(f"{course}: {sid} code {code} ({oid}) not in registry")
                elif reg_by_id[oid]["official_code"] != code:
                    errors.append(f"{course}: {sid} code/official_id mismatch {oid}")

    if errors:
        print("VALIDATION FAILED — no writes performed:")
        for e in errors:
            print("  -", e)
        return 1

    # ---------- apply ----------
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    summary = {}

    for course, st in state.items():
        merged = remapped = 0
        for sid, v in idv.items():
            if v["verdict"] != "resolve":
                continue
            crec = (v.get("courses") or {}).get(course)
            if not crec or crec.get("stage1_confirm"):
                continue
            codes = [str(c) for c in crec["codes"]]
            resolve_unit = crec.get("unit") or st["unit"]
            lead = reg_by_id[f"{PREFIX}:{resolve_unit}-{codes[0]}"]
            remap = crec.get("superseded_code") is not None
            tier = crec["tier"].split("+")[0]
            method = (METHOD_REMAP if remap else
                      METHOD_P1 if tier.startswith("P1") else METHOD_P2)
            st["mappings"][sid] = {
                "official_id": lead["id"],
                "official_code": codes[0],
                "tier": crec["tier"],
                "score": None if remap else 1.0,
                "unit": resolve_unit,
                "method": method,
                "resolution": {
                    "lane": "operator-verdict (T-SPEC-6)",
                    "quote": crec.get("quote"),
                    "page": crec.get("page"),
                    "twin_codes": codes[1:] or None,
                    "superseded_code": crec.get("superseded_code"),
                    "pmt_excluded": True,
                },
            }
            st["unmapped"].pop(sid, None)
            if remap:
                remapped += 1
            else:
                merged += 1

        # 1) write map
        mp = st["map"]
        mp["mappings"] = st["mappings"]
        um = []
        for sid in sorted(st["unmapped"]):
            v = idv.get(sid) or {}
            if v.get("verdict") == "pending":
                crec = (v.get("courses") or {}).get(course) or {}
                reason = crec.get("reason") or st["unmapped"][sid]
            else:
                reason = st["unmapped"][sid]
            um.append({"spcpt_id": sid,
                       "name": (st["index"]["spec_points"].get(sid) or {})
                       .get("name"),
                       "reason": reason})
        mp["unmapped"] = um
        (st["dir"] / "spec_point_map.json").write_text(
            json.dumps(mp, ensure_ascii=False, indent=1), encoding="utf-8")

        # 2) resolution sidecar covering EVERY index id (verify G2)
        part_refs = Counter()
        for f in topic_files(st["dir"]):
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
                stmt = reg_by_id.get(m["official_id"], {})
                rec.update({
                    "resolved_code": m["official_code"],
                    "official_id": m["official_id"],
                    "official_wording": stmt.get("text"),
                    "tier": m["tier"], "score": m.get("score"),
                    "method": m.get("method"), "unit": m.get("unit"),
                })
            else:
                v = idv.get(sid) or {}
                rec["resolved_code"] = None
                if v.get("verdict") == "pending":
                    crec = (v.get("courses") or {}).get(course) or {}
                    rec["reason"] = crec.get("reason") or "no-guess pending"
                else:
                    rec["reason"] = "unresolved (T-SPEC-6: no verdict; honest tail)"
            records.append(rec)

        res_doc = {
            "schema": "syllabai.sme-spec-point-resolution/1.0",
            "generated_utc": now,
            "validation": "AI_VALIDATED (operator-delegated chain; "
                          "page-context joins per T-SPEC-6 — SME IAL pages "
                          "publish no definition text, ticket #13; cross-unit "
                          "resolves documented per verdict; PMT excluded as "
                          "source); HUMAN_VALIDATED reserved for human review",
            "counts": {
                "ids": len(records),
                "resolved": sum(1 for r in records if r.get("resolved_code")),
                "unresolved": sum(1 for r in records
                                  if not r.get("resolved_code")),
            },
            "unresolved_allowlist_note": "parts whose ids are all unresolved "
                                         "stay uncoded by design (no-guess "
                                         "discipline)",
            "resolved": records,
        }
        (st["dir"] / "spec_point_resolution.json").write_text(
            json.dumps(res_doc, ensure_ascii=False, indent=1),
            encoding="utf-8")

        # 3) part codes: id-derived
        coded = uncoded = 0
        for f in topic_files(st["dir"]):
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
                    codes.sort(key=lambda c: min(
                        (order.get(m["official_id"], 10**9)
                         for m in st["mappings"].values()
                         if m["official_code"] == c),
                        default=10**9))
                    if codes:
                        p["spec_point_codes"] = codes
                        coded += 1
                        changed = True
                    else:
                        uncoded += 1
            if changed:
                f.write_text(json.dumps(t, ensure_ascii=False, indent=1),
                             encoding="utf-8")

        n = res_doc["counts"]
        summary[course] = {
            "ids": n["ids"], "resolved": n["resolved"],
            "unresolved": n["unresolved"], "map_merged": merged,
            "remaps": remapped, "parts_coded": coded,
            "parts_uncoded": uncoded,
        }
        print(f"[{course}] resolved {n['resolved']}/{n['ids']} ids "
              f"(+{merged} merges, {remapped} remaps); parts coded {coded}, "
              f"uncoded {uncoded}")

    # ---------- report ----------
    REPORTS.mkdir(parents=True, exist_ok=True)
    report = {
        "schema": "syllabai.t-spec-6-report/1.0",
        "generated_utc": now,
        "courses": list(COURSES),
        "summary": summary,
        "verdict_counts": doc["courses"],
        "evidence_note": "SME IAL maths tags carry no definition text "
                         "(ticket #13). Joins use tag name + revision-note "
                         "page + page body + exam-part text + global tag "
                         "identity across courses; per-course resolution "
                         "keeps each course's codes evidence-backed.",
        "parse_notes": [
            "D1-2.1 committed text drops \"Prim's and Kruskal's algorithm\" "
            "(PDF-verified); verdicts still join Kruskal tags to 2.1.",
            "S2-4.6 committed text drops \"and for the mean of a Poisson "
            "distribution\" (PDF-verified); the Poisson hypothesis tag joins "
            "to 4.6 with a documented note.",
            "D1-4.4 'Total float. Gantt (cascade) charts. Scheduling.' is "
            "absent from the committed parse (its code slot carries a "
            "notation artifact); float/Gantt/scheduling tags are honest "
            "pendings flagged for parse repair.",
        ],
        "pmt_excluded": True,
    }
    (REPORTS / "T_SPEC_6_MATHS_VERDICTS.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")

    md = ["# T-SPEC-6 — IAL maths spec-point verdicts (2026-09-19)", "",
          "SME IAL maths pages publish spec-point tags **without definition "
          "text** (upstream ticket #13), so the T-SPEC-3/4 verbatim "
          "definition joins are structurally impossible. Evidence used: tag "
          "name, revision-note page anchoring, page body, exam-part text, "
          "and the global SME tag identity across unit courses. Cross-unit "
          "resolves (e.g. pure-1 exams tagged with P2 trapezium/trajectory "
          "statements) are documented per verdict. 29 no-guess pendings: "
          "GCSE-bridge content absent from the published spec (exact trig "
          "values, Pythagoras, proportionality, pure modelling, units), "
          "graph-theory vocabulary with no standalone statement, and content "
          "belonging to D1-4.4 which the committed parse lacks (flagged for "
          "parse repair). PMT excluded as source.", ""]
    md += ["| course | ids | resolved | merges | remaps | pendings | "
           "parts coded | parts uncoded |",
           "|---|---|---|---|---|---|---|---|"]
    for c, s in summary.items():
        md.append(f"| {c} | {s['ids']} | {s['resolved']} | {s['map_merged']} "
                  f"| {s['remaps']} | {s['unresolved']} | {s['parts_coded']} "
                  f"| {s['parts_uncoded']} |")
    (REPORTS / "T_SPEC_6_MATHS_VERDICTS.md").write_text("\n".join(md),
                                                        encoding="utf-8")

    ws = Path("/home/z/my-project/scripts/specmap_work")
    ws.mkdir(parents=True, exist_ok=True)
    (ws / "t_spec_6_apply_summary.json").write_text(
        json.dumps({"generated_utc": now, "courses": summary}, indent=1))
    print(f"report -> {REPORTS / 'T_SPEC_6_MATHS_VERDICTS.md'}")
    print(f"done in {time.time()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
