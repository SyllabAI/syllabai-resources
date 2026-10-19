#!/usr/bin/env python3
"""T-SPEC-2d — update sibling course manifests with spec_point_resolution
stats (mirroring igcse-chemistry-19's pattern) and emit the operator review
sheet for the unresolved tail (never guessed; operator-verdict lane).
"""
import difflib
import json
import sys
import time
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
PARSED = BASE / "Official-Specifications" / "parsed"
REPORTS = BASE / "graph" / "reports"

sys.path.insert(0, str(BASE / "scripts"))
import sme_spcpt_sibling_map as sm  # reuse norm/ntokens/statement_text


def registry(qual, scope):
    pts = json.loads((PARSED / qual / "spec_points.json")
                     .read_text(encoding="utf-8"))["spec_points"]
    if scope:
        scoped = [p for p in pts if p.get("scope") == scope]
        pts = scoped or pts
    return pts


def main():
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    sheet = ["# T-SPEC-2 — sibling-course spec-join review sheet (unresolved tail)",
             "",
             f"Generated: {now}",
             "",
             "The ids below are part-referenced but remain **unresolved** after the",
             "full-pool join + note-coverage rescue (T-SPEC-2). Per the no-guess",
             "discipline (AGENT.md rules 2/3) they were **not** mapped; they stay in",
             "each course's `spec_point_resolution.json` with `resolved_code: null`",
             "and their parts stay uncoded (verify allowlist). Operator verdicts can",
             "promote them via the c10/c12-style evidence lanes.",
             ""]

    for course, (qual, scope) in sm.COURSES.items():
        cdir = EQ / course
        mp = json.loads((cdir / "spec_point_map.json").read_text(encoding="utf-8"))
        idx = json.loads((cdir / "spec_point_index.json").read_text(encoding="utf-8"))
        res = json.loads((cdir / "spec_point_resolution.json").read_text(encoding="utf-8"))
        reg = registry(qual, scope)

        # part refs
        part_refs = {}
        parts_total = parts_coded = 0
        for f in sorted(cdir.glob("*/*/*/topic.json")) + sorted(cdir.glob("*/*/topic.json")):
            t = json.loads(f.read_text(encoding="utf-8"))
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    sids = p.get("spec_point_ids") or []
                    if not sids:
                        continue
                    parts_total += 1
                    if p.get("spec_point_codes"):
                        parts_coded += 1
                    for s in sids:
                        part_refs[s] = part_refs.get(s, 0) + 1

        # manifest update (mirror chemistry pattern)
        mpath = cdir / "manifest.json"
        man = json.loads(mpath.read_text(encoding="utf-8"))
        distinct_codes = len({r["resolved_code"] for r in res["resolved"]
                              if r.get("resolved_code")})
        man["spec_point_resolution"] = {
            "schema": "syllabai.sme-spec-point-resolution/1.0",
            "validated": res["validation"],
            "index_file": "spec_point_index.json",
            "resolution_file": "spec_point_resolution.json",
            "counts": {
                "sme_spec_points": len(idx["spec_points"]),
                "resolved": res["counts"]["resolved"],
                "unresolved": res["counts"]["unresolved"],
                "distinct_codes_in_use": distinct_codes,
                "parts_total": parts_total,
                "parts_with_codes": parts_coded,
                "parts_left_uncoded_no_guess_tail": parts_total - parts_coded,
            },
            "pipeline": [
                "scripts/sme_spcpt_sibling_backfill.py",
                "scripts/sme_spcpt_sibling_map.py",
                "scripts/sme_spcpt_sibling_apply.py",
                "scripts/sme_spcpt_verify.py",
            ],
            "updated_utc": now,
        }
        mpath.write_text(json.dumps(man, ensure_ascii=False, indent=1),
                         encoding="utf-8")

        # review sheet section
        notes = sm.note_section_text(course)
        unmapped = mp["unmapped"]
        sheet.append(f"## {course}")
        sheet.append("")
        sheet.append(f"- resolved: {res['counts']['resolved']}/{res['counts']['ids']} ids; "
                     f"parts coded {parts_coded}/{parts_total}; "
                     f"unresolved ids below: {len(unmapped)}")
        sheet.append("")
        for u in unmapped:
            sid = u["spcpt_id"]
            e = idx["spec_points"].get(sid) or {}
            name = e.get("name") or ""
            sheet.append(f"### {sid}  ({u['reason'][:80]}...)" if False else
                         f"### {sid}")
            sheet.append(f"- name: {name!r}")
            sheet.append(f"- referenced by parts: {part_refs.get(sid, 0)}")
            sheet.append(f"- stage-1 reason: {u['reason']}")
            secs = notes.get(sid)
            if secs:
                excerpt = list(secs.values())[0][:300]
                sheet.append(f"- anchored note section (verbatim RN excerpt): "
                             f"{excerpt!r}")
                # top-3 candidates by statement-token coverage
                scored = []
                for p in reg:
                    stoks = sm.ntokens(sm.statement_text(p))
                    if not stoks:
                        continue
                    cov = 0.0
                    for seg in list(secs.values())[:3]:
                        cov = max(cov, len(stoks & sm.ntokens(seg)) / len(stoks))
                    scored.append((cov, p))
                scored.sort(key=lambda x: (-x[0], str(x[1]["official_code"])))
                sheet.append("- top candidates by note-coverage:")
                for cov, p in scored[:3]:
                    sheet.append(f"  - {p['official_code']} cov={cov:.2f} "
                                 f"{sm.statement_text(p)[:100]!r}")
            else:
                sheet.append("- no SME statement text available in committed corpora "
                             "(cross-cutting id)")
            sheet.append("")

    out = REPORTS / "T_SPEC_2_SIBLING_REVIEW_SHEET.md"
    out.write_text("\n".join(sheet), encoding="utf-8")
    print("wrote", out, f"({len(sheet)} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
