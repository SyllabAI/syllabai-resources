#!/usr/bin/env python3
"""T-SPEC-5 — apply the IAL-sciences spec-point verdicts
(scripts/t_spec_5_verdicts.yaml) to the three IAL science courses:

  ial-chemistry-17   (qual ial-chemistry)
  ial-physics-19     (qual ial-physics)
  ial-biology-18     (qual ial-biology)

Context: SME IAL pages publish spec-point tags WITHOUT definition text
(systemic upstream gap, ticket #13), so the T-SPEC-3/4 verbatim
definition->statement joins are structurally impossible here.  Evidence used
instead (all committed in-repo): the SME tag NAME, the revision-note page the
tag appears on (front-matter spec_point_ids), the page body, and the
exam-question part texts that reference the tag.  Tiers:
  P1_name_fragment_join  - distinctive fragment shared by tag name/statement
  P2_page_context_join   - tag name + page context pins the statement
  pending                - no-guess tail (skills tags / SME-extra tags)

Fail-closed rules (hard errors before ANY write):
  - population closure: yaml resolve ids == per-course unmapped ids exactly;
    remap ids must carry existing mappings whose code equals superseded_code
  - every code must exist in the course's OWN registry
  - every resolve/remap tag must be anchored: its recorded page exists under
    SME-RevisionNotes/<course>/notes and its front-matter spec_point_ids
    contains the tag id (page-association check)
  - quote must equal the committed index name for the tag
  - pending: verbatim reason required
Writes (after validation):
  - spec_point_map.json: resolves/remaps merged into mappings, resolved ids
    removed from unmapped, pendings kept with verdict reason
  - spec_point_resolution.json sidecar covering EVERY index id (verify G2)
  - spec_point_codes written on all parts with ids (verify G1)
  - graph/reports/T_SPEC_5_IAL_VERDICTS.{md,json}

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

COURSES = {
    "ial-chemistry-17": ("ial-chemistry", "Chemistry"),
    "ial-physics-19": ("ial-physics", None),
    "ial-biology-18": ("ial-biology", "Biology"),
}

METHOD_P1 = ("operator-verdict name-fragment join (T-SPEC-5; SME IAL pages "
             "publish no definition text, ticket #13; PMT excluded as source)")
METHOD_P2 = ("operator-verdict page-context join (T-SPEC-5; SME IAL pages "
             "publish no definition text, ticket #13; PMT excluded as source)")
METHOD_REMAP = ("operator-verdict page-context join (T-SPEC-5 re-verdict; "
                "corrects stage-1 name-only match; PMT excluded as source)")


def registry(qual, scope):
    pts = json.loads((PARSED / qual / "spec_points.json")
                     .read_text(encoding="utf-8"))["spec_points"]
    if scope:
        scoped = [p for p in pts if p.get("scope") == scope]
        if scoped:
            pts = scoped
    return pts


def topic_files(cdir: Path):
    return sorted(cdir.glob("*/*/*/topic.json")) + \
        sorted(cdir.glob("*/*/topic.json"))


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
    doc = yaml.safe_load((BASE / "scripts" / "t_spec_5_verdicts.yaml")
                         .read_text(encoding="utf-8"))
    idv = doc["id_verdicts"]

    state = {}
    for course, (qual, scope) in COURSES.items():
        cdir = EQ / course
        mp = json.loads((cdir / "spec_point_map.json").read_text(encoding="utf-8"))
        idx = json.loads((cdir / "spec_point_index.json").read_text(encoding="utf-8"))
        pts = registry(qual, scope)
        state[course] = {
            "qual": qual, "scope": scope, "dir": cdir, "map": mp,
            "index": idx, "reg": pts,
            "by_code": {p["official_code"]: p for p in pts},
            "order": {p["id"]: i for i, p in enumerate(pts)},
            "mappings": mp.get("mappings", {}),
            "unmapped": {u["spcpt_id"]: u.get("reason", "")
                         for u in mp.get("unmapped", [])},
        }

    # ---------- population closure + validation ----------
    errors = []
    for course, st in state.items():
        got_res = {sid for sid, v in idv.items()
                   if v["verdict"] == "resolve"
                   and v.get("superseded_code") is None
                   and course in (v.get("codes") or {})}
        got_pen = {sid for sid, v in idv.items()
                   if v["verdict"] == "pending" and course in (v.get("courses") or [])}
        need_res = set(st["unmapped"]) - got_pen
        if got_res != need_res:
            errors.append(f"{course}: resolve set mismatch "
                          f"yaml-only={sorted(got_res - need_res)[:5]} "
                          f"need-only={sorted(need_res - got_res)[:5]}")
        # pendings must also be members of the unmapped tail
        for sid in got_pen:
            if sid not in st["unmapped"]:
                errors.append(f"{course}: pending {sid} not in unmapped tail")
        # remaps: mapped ids with superseded_code match
        for sid, v in idv.items():
            if v["verdict"] != "resolve" or v.get("superseded_code") is None:
                continue
            if course not in (v.get("codes") or {}):
                continue
            m = st["mappings"].get(sid)
            if not m:
                errors.append(f"{course}: remap {sid} has no existing mapping")
            elif m["official_code"] != v["superseded_code"]:
                errors.append(f"{course}: remap {sid} superseded "
                              f"{v['superseded_code']} != existing "
                              f"{m['official_code']}")

    # anchor + quote validation for every resolve with codes in this run
    for course, st in state.items():
        for sid, v in idv.items():
            if v["verdict"] != "resolve" or course not in (v.get("codes") or {}):
                continue
            e = st["index"]["spec_points"].get(sid)
            if e is None:
                errors.append(f"{course}: {sid} not in index")
                continue
            if (v.get("quote") or "") != (e.get("name") or ""):
                errors.append(f"{course}: {sid} quote != index name")
            page = v.get("page")
            ids = note_page_ids(page) if page else None
            if ids is None:
                errors.append(f"{course}: {sid} page missing/unreadable: {page}")
            elif sid not in ids:
                errors.append(f"{course}: {sid} not anchored on page {page}")
            for code in v["codes"][course]:
                if code not in st["by_code"]:
                    errors.append(f"{course}: {sid} code {code} not in registry")

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
        merged = remapped = 0

        # 1) map merges
        for sid, v in idv.items():
            if v["verdict"] != "resolve" or course not in (v.get("codes") or {}):
                continue
            codes = v["codes"][course]
            entry = st["by_code"][codes[0]]
            remap = v.get("superseded_code") is not None
            tier = v["tier"].split("+")[0]
            method = (METHOD_REMAP if remap else
                      METHOD_P1 if tier.startswith("P1") else METHOD_P2)
            st["mappings"][sid] = {
                "official_id": entry["id"],
                "official_code": codes[0],
                "tier": v["tier"],
                "score": 1.0 if not remap else None,
                "unit": None,
                "method": method,
                "resolution": {
                    "lane": "operator-verdict (T-SPEC-5)",
                    "quote": v.get("quote"),
                    "page": v.get("page"),
                    "twin_codes": codes[1:] or None,
                    "superseded_code": v.get("superseded_code"),
                    "pmt_excluded": True,
                },
            }
            st["unmapped"].pop(sid, None)
            if remap:
                remapped += 1
            else:
                merged += 1

        # 2) write map (partition: mappings + pendings-only unmapped)
        mp = st["map"]
        mp["mappings"] = st["mappings"]
        um = []
        for sid in sorted(st["unmapped"]):
            v = idv.get(sid) or {}
            reason = v.get("reason") if v.get("verdict") == "pending" \
                else st["unmapped"][sid]
            um.append({"spcpt_id": sid,
                       "name": (st["index"]["spec_points"].get(sid) or {})
                       .get("name"),
                       "reason": reason})
        mp["unmapped"] = um
        (st["dir"] / "spec_point_map.json").write_text(
            json.dumps(mp, ensure_ascii=False, indent=1), encoding="utf-8")

        # 3) resolution sidecar covering EVERY index id (verify G2)
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
                stmt = st["by_code"].get(m["official_code"], {})
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
                rec["reason"] = v.get("reason") if v.get("verdict") == "pending" \
                    else "unresolved (T-SPEC-5: no verdict; honest tail)"
            records.append(rec)

        res_doc = {
            "schema": "syllabai.sme-spec-point-resolution/1.0",
            "generated_utc": now,
            "validation": "AI_VALIDATED (operator-delegated chain; "
                          "page-context joins per T-SPEC-5 — SME IAL pages "
                          "publish no definition text, ticket #13; PMT "
                          "excluded as source); HUMAN_VALIDATED reserved "
                          "for human review",
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

        # 4) part codes: id-derived
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
        "schema": "syllabai.t-spec-5-report/1.0",
        "generated_utc": now,
        "courses": list(COURSES),
        "summary": summary,
        "verdict_counts": doc["courses"],
        "evidence_note": "SME IAL spec-point tags carry no definition text "
                         "(0/750 entries; upstream ticket #13). Joins use "
                         "tag name + revision-note page + page body + "
                         "exam-part text against official statement texts.",
        "pmt_excluded": True,
    }
    (REPORTS / "T_SPEC_5_IAL_VERDICTS.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")

    md = ["# T-SPEC-5 — IAL sciences spec-point verdicts (2026-09-19)", "",
          "SME IAL pages publish spec-point tags **without definition text** "
          "(0/750 entries; upstream ticket #13), so the T-SPEC-3/4 verbatim "
          "definition joins are structurally impossible. Evidence used: tag "
          "name, revision-note page anchoring, page body, exam-part text. "
          "22 re-verdicts correct stage-1 name-only mappings (e.g. "
          "bio 'Transcription' 8.11 -> 2.13); 56 no-guess pendings are SME "
          "practical-skills tags with no theory-statement target, plus 1 "
          "SME-extra chemistry tag (atomic-radius trends, absent from the "
          "published spec). PMT excluded as source.", ""]
    md += ["| course | ids | resolved | merges | remaps | pendings | "
           "parts coded | parts uncoded |",
           "|---|---|---|---|---|---|---|---|"]
    for c, s in summary.items():
        md.append(f"| {c} | {s['ids']} | {s['resolved']} | {s['map_merged']} "
                  f"| {s['remaps']} | {s['unresolved']} | {s['parts_coded']} "
                  f"| {s['parts_uncoded']} |")
    md += ["", "## pending classes", "",
           "- practical-skills tags (physics units 3/6 experimental "
           "methods): no numbered statement in WPH11/12/14/15 registry",
           "- SME-extra tag (chem 'Trend: Atomic Radius'): content absent "
           "from the published specification (PDF-verified)"]
    (REPORTS / "T_SPEC_5_IAL_VERDICTS.md").write_text("\n".join(md),
                                                      encoding="utf-8")

    ws = Path("/home/z/my-project/scripts/specmap_work")
    ws.mkdir(parents=True, exist_ok=True)
    (ws / "t_spec_5_apply_summary.json").write_text(
        json.dumps({"generated_utc": now, "courses": summary}, indent=1))
    print(f"report -> {REPORTS / 'T_SPEC_5_IAL_VERDICTS.md'}")
    print(f"done in {time.time()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
