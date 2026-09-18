#!/usr/bin/env python3
"""T-SPEC-2e — apply the operator-override labels (S0 opinion tier) to the 6
honest pendings left by T-SPEC-2c, per operator instruction of 2026-09-18
("Label them ourselves now").

Fail-closed rules:
  - YAML overrides must match the T-SPEC-2c pendings population exactly
  - each part must exist, carry exactly the YAML spec_point_ids, and have NO
    existing spec_point_codes (pendings are uncoded by construction)
  - every code must exist in the course's own official registry
  - every evidence quote must be token-contained (sm.ntokens) in the part's
    committed problem_md/solution_md
  - map lane (spec_point_map.json) is NEVER rewritten; the referenced ids
    stay honestly unresolved in the sidecars (the override is part-level)

Also renders graph/reports/T_SPEC_2E_OPERATOR_OVERRIDE.{md,json}.
PMT (PhysicsMathsTutor) excluded as an evidence source (operator instruction
2026-09-18); no PMT content appears in any record.
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
import sme_spcpt_sibling_map as sm  # ntokens

COURSES = {
    "igcse-chemistry-modular-24-unit-1": "igcse-chemistry-modular",
    "igcse-chemistry-modular-24-unit-2": "igcse-chemistry-modular",
}


def topic_files(cdir: Path):
    return sorted(cdir.glob("*/*/*/topic.json")) + sorted(cdir.glob("*/*/topic.json"))


def registry(qual: str):
    return json.loads((PARSED / qual / "spec_points.json")
                      .read_text(encoding="utf-8"))["spec_points"]


def find_part(cdir: Path, pid: str):
    for f in topic_files(cdir):
        t = json.loads(f.read_text(encoding="utf-8"))
        for q in t.get("questions", []):
            for p in q.get("parts", []):
                if p.get("id") == pid:
                    return f, t, q, p
    return None, None, None, None


def validate(doc, pendings, regs):
    errors = []
    ov = doc["overrides"]
    yids, tids = set(ov), set(pendings)
    if yids != tids:
        errors.append(f"population mismatch: yaml-only={sorted(yids - tids)} "
                      f"2c-pendings-only={sorted(tids - yids)}")
    for pid, o in ov.items():
        course = o["course"]
        if course not in COURSES:
            errors.append(f"{pid}: unknown course {course}")
            continue
        reg_by_code = {p["official_code"]: p for p in regs[course]}
        for c in o["codes"]:
            if c not in reg_by_code:
                errors.append(f"{pid}: code {c} not in {course} registry")
        f, t, q, p = find_part(EQ / course, pid)
        if p is None:
            errors.append(f"{pid}: part not found in {course}")
            continue
        if sorted(p.get("spec_point_ids") or []) != sorted(o["ids"]):
            errors.append(f"{pid}: spec_point_ids {p.get('spec_point_ids')} "
                          f"!= yaml {o['ids']}")
        if p.get("spec_point_codes"):
            errors.append(f"{pid}: part already has spec_point_codes "
                          f"{p['spec_point_codes']} — override would overwrite")
        body = " ".join([p.get("problem_md") or "", p.get("solution_md") or ""])
        btok = sm.ntokens(body)
        for quote in o.get("quotes", []):
            qt = sm.ntokens(quote["text"])
            missing = qt - btok
            if missing:
                errors.append(f"{pid}: quote not verbatim in committed part "
                              f"(missing {sorted(missing)[:6]})")
    return errors


def main() -> int:
    check_only = "--check" in sys.argv
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    doc = yaml.safe_load((BASE / "scripts" / "t_spec_2e_operator_override.yaml")
                         .read_text(encoding="utf-8"))
    ov = doc["overrides"]
    pendings = json.loads((REPORTS / "T_SPEC_2C_PART_VERDICTS.json")
                          .read_text(encoding="utf-8"))["summary"]["pendings"]
    regs = {c: registry(q) for c, q in COURSES.items()}

    errors = validate(doc, pendings, regs)
    if errors:
        print("FAIL-CLOSED VALIDATION ERRORS:")
        for e in errors:
            print("  -", e)
        return 1
    print(f"validation: OK ({len(ov)} operator overrides on the 2c pendings "
          f"population; codes in registry; quotes verbatim in parts)")
    if check_only:
        return 0

    summary = {}
    for course in COURSES:
        reg = regs[course]
        reg_order = {p["id"]: i for i, p in enumerate(reg)}
        touched = []
        for pid, o in ov.items():
            if o["course"] != course:
                continue
            f, t, q, p = find_part(EQ / course, pid)
            codes = sorted(o["codes"],
                           key=lambda c: reg_order[
                               next(x["id"] for x in reg
                                    if x["official_code"] == c)])
            p["spec_point_codes"] = codes
            changed = True
            f.write_text(json.dumps(t, ensure_ascii=False, indent=1),
                         encoding="utf-8")
            touched.append({"part": pid, "codes": codes,
                            "tickets": o["tickets"]})

        # recount parts from topic.json (ground truth; also repairs the
        # stale 2b-era manifest counts the lost 2c apply never refreshed)
        coded = uncoded = 0
        for f2 in topic_files(EQ / course):
            t2 = json.loads(f2.read_text(encoding="utf-8"))
            for q2 in t2.get("questions", []):
                for p2 in q2.get("parts", []):
                    if p2.get("spec_point_ids"):
                        if p2.get("spec_point_codes"):
                            coded += 1
                        else:
                            uncoded += 1

        # surgical sidecar update (records stay; ids stay honestly unresolved)
        spath = EQ / course / "spec_point_resolution.json"
        sdoc = json.loads(spath.read_text(encoding="utf-8"))
        sdoc["generated_utc"] = now
        add = (" + operator-override lane T-SPEC-2e (S0 opinion tier, "
               "operator instruction 2026-09-18; tickets #6/#7/#8; PMT "
               "excluded as source) — part-level codes only, id-level "
               "unresolved records unchanged pending upstream statement text")
        sdoc["validation"] = sdoc.get("validation", "") + add
        sdoc["operator_override"] = {
            "decision_record": "scripts/t_spec_2e_operator_override.yaml",
            "tier": doc["meta"]["tier"],
            "applied_utc": now,
            "parts": touched,
        }
        spath.write_text(json.dumps(sdoc, ensure_ascii=False, indent=1),
                         encoding="utf-8")

        mpath = EQ / course / "manifest.json"
        man = json.loads(mpath.read_text(encoding="utf-8"))
        man["spec_point_resolution"]["counts"].update({
            "parts_total": coded + uncoded,
            "parts_with_codes": coded,
            "parts_left_uncoded_no_guess_tail": uncoded,
        })
        man["spec_point_resolution"]["pipeline"].append(
            "scripts/t_spec_2e_override_apply.py")
        man["spec_point_resolution"]["updated_utc"] = now
        mpath.write_text(json.dumps(man, ensure_ascii=False, indent=1),
                         encoding="utf-8")

        summary[course] = {"override_parts": len(touched),
                           "parts_total": coded + uncoded,
                           "parts_with_codes": coded,
                           "no_guess_tail": uncoded}
        print(f"[{course}] overrides applied: {len(touched)}; "
              f"parts coded {coded}/{coded + uncoded} "
              f"(no-guess tail {uncoded})")

    render(doc, summary, now)
    return 0


def render(doc, summary, now):
    ov = doc["overrides"]
    lines = [
        "# T-SPEC-2e — operator-override record: the 6 honest pendings", "",
        f"Generated: {now}", "",
        "Per operator instruction of 2026-09-18 (\"Label them ourselves now\"),",
        "the 6 T-SPEC-2c pendings received nearest-neighbour codes in a",
        "dedicated **S0_operator_override** opinion tier. Upstream requests",
        "SyllabAI/syllabai-resources#6 / #7 / #8 document that no official",
        "statement for these skills exists in any Pearson chemistry universe",
        "(linear 4CH1, modular 2024, IAL) nor in SME's registries; the tickets",
        "stay open and these labels MUST be re-verdicted if SME publishes",
        "statement text for the referenced tags. Map lane untouched; id-level",
        "unresolved sidecar records unchanged. PMT excluded as a source.", "",
        "| part | course | codes | tickets |", "|---|---|---|---|",
    ]
    for pid, o in ov.items():
        lines.append(f"| `{pid}` | {o['course'].replace('igcse-chemistry-', '')} "
                     f"| {', '.join(o['codes'])} | {', '.join(o['tickets'])} |")
    lines.append("")
    lines.append("## Per-course outcome")
    lines.append("")
    lines.append("| course | overrides applied | parts coded | no-guess tail |")
    lines.append("|---|---|---|---|")
    for c, s in summary.items():
        lines.append(f"| {c} | {s['override_parts']} | "
                     f"{s['parts_with_codes']}/{s['parts_total']} | "
                     f"{s['no_guess_tail']} |")
    lines.append("")
    lines.append("## Overrides (full rationale)")
    lines.append("")
    for pid, o in ov.items():
        lines.append(f"### {pid} → {', '.join(o['codes'])}")
        lines.append(f"- tier: {doc['meta']['tier']}")
        lines.append(f"- tickets: {', '.join(o['tickets'])}")
        for quote in o.get("quotes", []):
            lines.append(f"- evidence ({quote['field']}, verbatim): "
                         f"{quote['text']!r}")
        lines.append(f"- rationale: {o['rationale']}")
        lines.append(f"- supersedes T-SPEC-2c pending: {o['supersedes_pending']}")
        lines.append("")
    out = REPORTS / "T_SPEC_2E_OPERATOR_OVERRIDE.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    (REPORTS / "T_SPEC_2E_OPERATOR_OVERRIDE.json").write_text(
        json.dumps({"task": "T-SPEC-2e", "generated_utc": now,
                    "tier": doc["meta"]["tier"],
                    "decision_record": "scripts/t_spec_2e_operator_override.yaml",
                    "upstream_requests": ["#6", "#7", "#8"],
                    "excluded_sources": ["PMT (PhysicsMathsTutor) — excluded "
                                         "entirely per operator instruction "
                                         "2026-09-18"],
                    "courses": summary, "overrides": ov},
                   ensure_ascii=False, indent=1))
    print("wrote", out)


if __name__ == "__main__":
    sys.exit(main())
