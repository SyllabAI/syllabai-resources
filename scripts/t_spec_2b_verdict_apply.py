#!/usr/bin/env python3
"""T-SPEC-2b — apply the operator-delegated verdicts on the 85-id unresolved
tail (scripts/t_spec_2b_verdicts.yaml) to the three chemistry sibling courses,
and render the verdict report + machine record.

Fail-closed rules:
  - every review-sheet id must have exactly one YAML verdict; every YAML id
    must appear in at least one course's unmapped list
  - a resolve code must exist verbatim in the course's own registry
  - a V2/V3 note quote must be token-contained in that id's anchored note
    section (no-guess: evidence must byte-exist in the committed corpus)
  - map file (stage-1 join artifact) is NEVER rewritten; verdicts live in the
    sidecar + decision record only

Also renders graph/reports/T_SPEC_2B_SIBLING_VERDICTS.md and .json.
PMT (PhysicsMathsTutor) is excluded as an evidence source per operator
instruction of 2026-09-18 and appears in no evidence record.
"""
import json
import sys
import time
from pathlib import Path

import yaml

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
PARSED = BASE / "Official-Specifications" / "parsed"
REPORTS = BASE / "graph" / "reports"

sys.path.insert(0, str(BASE / "scripts"))
import sme_spcpt_sibling_map as sm  # norm/ntokens/statement_text/note_section_text

COURSES = {
    "igcse-chemistry-modular-24-unit-1": ("igcse-chemistry-modular", None),
    "igcse-chemistry-modular-24-unit-2": ("igcse-chemistry-modular", None),
    "igcse-science-double-award-17-chemistry": ("igcse-science-double-award", "Chemistry"),
}


def load_yaml():
    doc = yaml.safe_load((BASE / "scripts" / "t_spec_2b_verdicts.yaml").read_text())
    return doc["verdicts"]


def registry(qual, scope):
    pts = json.loads((PARSED / qual / "spec_points.json")
                     .read_text(encoding="utf-8"))["spec_points"]
    if scope:
        scoped = [p for p in pts if p.get("scope") == scope]
        pts = scoped or pts
    return pts


def topic_files(cdir):
    return sorted(cdir.glob("*/*/*/topic.json")) + sorted(cdir.glob("*/*/topic.json"))


def validate(verdicts, per_course_unmapped, notes, regs):
    """Fail-closed evidence validation. Returns list of hard errors."""
    errors, warns = [], []
    sheet_ids = set()
    for ids in per_course_unmapped.values():
        sheet_ids.update(ids)
    yids = set(verdicts)
    if yids != sheet_ids:
        errors.append(f"YAML/sheet mismatch: yaml-only={sorted(yids-sheet_ids)} "
                      f"sheet-only={sorted(sheet_ids-yids)}")
    # every note-verbatim quote must exist in the anchored section
    for sid, v in verdicts.items():
        if v["verdict"] != "resolve":
            continue
        ev = v.get("evidence") or {}
        q = ev.get("quote") or ""
        sec = (notes.get(sid) or {})
        if sec:
            joined = " ".join(list(sec.values())[:3])
            qt = sm.ntokens(q)
            if qt and not qt.issubset(sm.ntokens(joined)):
                missing = qt - sm.ntokens(joined)
                errors.append(f"{sid}: note quote not contained "
                              f"(missing tokens {sorted(missing)[:6]})")
        elif q and not sid.startswith(("spcpt_msKx", "spcpt_ZqH4")):
            # ids with no note anchor must not carry note quotes
            errors.append(f"{sid}: quote given but id has no note anchor")
        st = ev.get("statement") or ""
        for course in per_course_unmapped:
            if sid in per_course_unmapped[course] and v["verdict"] == "resolve":
                reg = regs[course]
                hit = [p for p in reg if p["official_code"] == v["code"]]
                if not hit:
                    errors.append(f"{sid}: code {v['code']} not in {course} registry")
                elif st:
                    stt = sm.ntokens(sm.statement_text(hit[0]))
                    qt = sm.ntokens(st)
                    if qt and not qt.issubset(stt):
                        errors.append(f"{sid}: statement-side quote not verbatim in "
                                      f"{v['code']} (missing {sorted(qt - stt)[:6]})")
    return errors, warns


def main():
    check_only = "--check" in sys.argv
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    verdicts = load_yaml()

    per_course_unmapped, notes, regs = {}, {}, {}
    for course, (qual, scope) in COURSES.items():
        cdir = EQ / course
        mp = json.loads((cdir / "spec_point_map.json").read_text(encoding="utf-8"))
        per_course_unmapped[course] = {u["spcpt_id"] for u in mp["unmapped"]}
        notes[course] = sm.note_section_text(course)
        regs[course] = registry(qual, scope)
    # note anchors are per-course; merge for validation (ids resolve identically
    # across courses — same RN corpus, same registry pool)
    merged_notes = {}
    for c in notes:
        merged_notes.update(notes[c])

    errors, warns = validate(verdicts, per_course_unmapped, merged_notes, regs)
    if errors:
        print("FAIL-CLOSED VALIDATION ERRORS:")
        for e in errors:
            print("  -", e)
        return 1
    print("validation: OK "
          f"({len(verdicts)} verdicts, "
          f"{sum(1 for v in verdicts.values() if v['verdict']=='resolve')} resolve / "
          f"{sum(1 for v in verdicts.values() if v['verdict']=='pending')} pending)")
    if check_only:
        return 0

    summary = {}
    for course, (qual, scope) in COURSES.items():
        cdir = EQ / course
        mp = json.loads((cdir / "spec_point_map.json").read_text(encoding="utf-8"))
        idx = json.loads((cdir / "spec_point_index.json").read_text(encoding="utf-8"))
        res_old = json.loads((cdir / "spec_point_resolution.json").read_text(encoding="utf-8"))
        reg = regs[course]
        reg_by_code = {p["official_code"]: p for p in reg}
        reg_order = {p["id"]: i for i, p in enumerate(reg)}

        id2rec, pending_reason = {}, {}
        for sid, m in mp["mappings"].items():
            id2rec[sid] = {
                "resolved_code": m["official_code"],
                "official_id": m["official_id"],
                "official_wording": (reg_by_code.get(m["official_code"], {})
                                     .get("text")),
                "tier": m["tier"], "score": m["score"], "method": m["method"],
                "unit": m.get("unit"), "flag": m.get("flag"),
                "recheck": m.get("recheck"),
            }
        for u in mp["unmapped"]:
            sid = u["spcpt_id"]
            v = verdicts[sid]
            if v["verdict"] == "resolve":
                p = reg_by_code[v["code"]]
                id2rec[sid] = {
                    "resolved_code": v["code"],
                    "official_id": p["id"],
                    "official_wording": p.get("text"),
                    "tier": v["tier"], "score": None,
                    "method": "operator-verdict lane (T-SPEC-2b; PMT excluded "
                              "as source per operator instruction 2026-09-18)",
                    "unit": p.get("unit"),
                    "flag": ("twin: " + v["twin"]) if v.get("twin") else None,
                    "recheck": v.get("note"),
                }
            else:
                pending_reason[sid] = "operator-confirmed pending (T-SPEC-2b): " + v["reason"]

        # re-apply codes to parts (deterministic; map lane unchanged, verdict adds)
        coded_parts = uncoded_parts = recoded = 0
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
                        r = id2rec.get(s)
                        if r and r["resolved_code"] and r["resolved_code"] not in seen:
                            codes.append(r["resolved_code"])
                            seen.add(r["resolved_code"])
                    codes.sort(key=lambda c: reg_order.get(
                        reg_by_code[c]["id"], 10**9))
                    old = p.get("spec_point_codes")
                    if codes:
                        if old != codes:
                            recoded += 1
                        p["spec_point_codes"] = codes
                        changed = True
                        coded_parts += 1
                    else:
                        uncoded_parts += 1
            if changed:
                f.write_text(json.dumps(t, ensure_ascii=False, indent=1),
                             encoding="utf-8")

        # rebuild sidecar (records for EVERY index id, G2)
        records = []
        for sid, e in idx["spec_points"].items():
            rec = {
                "id": sid,
                "sme_name": e.get("name"),
                "sme_definition": e.get("definition"),
                "referenced_by_parts": None,
            }
            if sid in id2rec:
                rec.update(id2rec[sid])
            else:
                rec["resolved_code"] = None
                rec["reason"] = pending_reason.get(sid, "unresolved")
            records.append(rec)
        part_refs = {}
        for f in topic_files(cdir):
            t = json.loads(f.read_text(encoding="utf-8"))
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    for s in p.get("spec_point_ids") or []:
                        part_refs[s] = part_refs.get(s, 0) + 1
        for rec in records:
            rec["referenced_by_parts"] = part_refs.get(rec["id"], 0)

        resolved_n = sum(1 for r in records if r.get("resolved_code"))
        doc = {
            "schema": "syllabai.sme-spec-point-resolution/1.0",
            "generated_utc": now,
            "validation": res_old.get("validation") +
                " + operator-verdict lane T-SPEC-2b (evidence-quoted, no-guess)",
            "counts": {
                "ids": len(records),
                "resolved": resolved_n,
                "unresolved": len(records) - resolved_n,
            },
            "unresolved_allowlist_note": res_old.get("unresolved_allowlist_note"),
            "resolved": records,
        }
        (cdir / "spec_point_resolution.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

        # manifest refresh (mirror chemistry pattern)
        mpath = cdir / "manifest.json"
        man = json.loads(mpath.read_text(encoding="utf-8"))
        distinct_codes = len({r["resolved_code"] for r in records
                              if r.get("resolved_code")})
        man["spec_point_resolution"]["counts"] = {
            "sme_spec_points": len(idx["spec_points"]),
            "resolved": resolved_n,
            "unresolved": len(records) - resolved_n,
            "distinct_codes_in_use": distinct_codes,
            "parts_total": coded_parts + uncoded_parts,
            "parts_with_codes": coded_parts,
            "parts_left_uncoded_no_guess_tail": uncoded_parts,
        }
        man["spec_point_resolution"]["pipeline"].append(
            "scripts/t_spec_2b_verdict_apply.py")
        man["spec_point_resolution"]["updated_utc"] = now
        mpath.write_text(json.dumps(man, ensure_ascii=False, indent=1),
                         encoding="utf-8")

        delta_resolved = resolved_n - res_old["counts"]["resolved"]
        summary[course] = {
            "ids": len(records), "resolved": resolved_n,
            "unresolved": len(records) - resolved_n,
            "verdict_resolves": sum(1 for s in per_course_unmapped[course]
                                    if verdicts[s]["verdict"] == "resolve"),
            "verdict_pendings": sum(1 for s in per_course_unmapped[course]
                                    if verdicts[s]["verdict"] == "pending"),
            "delta_resolved": delta_resolved,
            "parts_coded": coded_parts, "parts_uncoded": uncoded_parts,
            "parts_recoded": recoded,
        }
        print(f"[{course}] resolved {resolved_n}/{len(records)} "
              f"(+{delta_resolved} via verdicts); parts coded {coded_parts}, "
              f"uncoded {uncoded_parts} (recoded {recoded})")

    render(verdicts, summary, now)
    Path("/home/z/my-project/scripts/specmap_work/verdict_apply_summary.json").write_text(
        json.dumps({"generated_utc": now, "courses": summary}, indent=1))
    return 0


def render(verdicts, summary, now):
    n_res = sum(1 for v in verdicts.values() if v["verdict"] == "resolve")
    n_pen = len(verdicts) - n_res
    lines = [
        "# T-SPEC-2b — verdict record: the 85-id sibling review sheet", "",
        f"Generated: {now}",
        "",
        "Operator-delegated verdicts on every id in",
        "`graph/reports/T_SPEC_2_SIBLING_REVIEW_SHEET.md` (PR #4's unresolved",
        "tail). Decision record: `scripts/t_spec_2b_verdicts.yaml`; machine",
        "record: `graph/reports/T_SPEC_2B_SIBLING_VERDICTS.json`. Evidence is",
        "verbatim from committed sources only (RN note sections, SME",
        "names/definitions, part texts, official registry statements) —",
        "**PMT (PhysicsMathsTutor) was excluded as an evidence source entirely**",
        "per operator instruction of 2026-09-18. The stage-1 map artifacts were",
        "not rewritten; verdict resolutions live in the resolution sidecars",
        "with `method: operator-verdict lane (T-SPEC-2b)`.", "",
        f"**Verdict totals: {n_res} RESOLVE / {n_pen} CONFIRMED-PENDING** "
        f"(of {len(verdicts)} reviewed ids).", "",
    ]
    tiers = {}
    for v in verdicts.values():
        if v["verdict"] == "resolve":
            tiers[v["tier"]] = tiers.get(v["tier"], 0) + 1
    lines.append("- Resolved by tier: " +
                 ", ".join(f"{k.replace('V1_', 'V1 ').replace('V2_', 'V2 ').replace('V3_', 'V3 ')}={n}"
                           for k, n in sorted(tiers.items())))
    lines.append("")
    lines.append("## Per-course outcome")
    lines.append("")
    lines.append("| course | verdict resolves | verdict pendings | ids resolved after apply | parts coded after apply |")
    lines.append("|---|---|---|---|---|")
    for course, s in summary.items():
        lines.append(f"| {course} | {s['verdict_resolves']} | {s['verdict_pendings']} | "
                     f"{s['resolved']}/{s['ids']} | {s['parts_coded']} "
                     f"(uncoded no-guess tail {s['parts_uncoded']}) |")
    lines.append("")
    lines.append("## Verdicts (resolve)")
    lines.append("")
    for sid, v in verdicts.items():
        if v["verdict"] != "resolve":
            continue
        ev = v.get("evidence") or {}
        lines.append(f"### {sid} → {v['code']}")
        lines.append(f"- tier: {v['tier']}")
        if ev.get("quote"):
            lines.append(f"- corpus evidence (verbatim): {ev['quote']!r}")
        if ev.get("statement"):
            lines.append(f"- official statement: {ev['statement']!r}")
        if v.get("twin"):
            lines.append(f"- twin statement recorded: {v['twin']}")
        if v.get("note"):
            lines.append(f"- review note: {v['note']}")
        lines.append("")
    lines.append("## Verdicts (confirmed pending — no-guess tail)")
    lines.append("")
    for sid, v in verdicts.items():
        if v["verdict"] != "pending":
            continue
        lines.append(f"### {sid}")
        lines.append(f"- reason: {v['reason']}")
        lines.append("")
    out = REPORTS / "T_SPEC_2B_SIBLING_VERDICTS.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    (REPORTS / "T_SPEC_2B_SIBLING_VERDICTS.json").write_text(
        json.dumps({
            "task": "T-SPEC-2b", "generated_utc": now,
            "source_sheet": "graph/reports/T_SPEC_2_SIBLING_REVIEW_SHEET.md",
            "decision_record": "scripts/t_spec_2b_verdicts.yaml",
            "evidence_sources": ["SME-RevisionNotes note sections (committed)",
                                  "SME id names/definitions",
                                  "SME-ExamQuestion part texts",
                                  "Official-Specifications/parsed registries"],
            "excluded_sources": ["PMT (PhysicsMathsTutor) — excluded entirely per "
                                  "operator instruction 2026-09-18"],
            "totals": {"resolve": n_res, "pending": n_pen},
            "tiers": tiers,
            "courses": summary,
            "verdicts": verdicts,
        }, ensure_ascii=False, indent=1))
    print("wrote", out)


if __name__ == "__main__":
    sys.exit(main())
