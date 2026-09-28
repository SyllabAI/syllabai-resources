#!/usr/bin/env python3
"""s104_verify_question_package.py — offline 1:1 replay of the hub join
against a built sme-question-package, BEFORE any core import happens.

This is the layer-3 verification gate (RUNBOOK §4.4/§6): it simulates exactly
what syllabai-core will serve after the ingest and what
src/app/api/core/questions/route.ts will derive, and proves:

  1. every hub topic's questions resolve a family by ref
     sme-eq-<topicSlug>-q<order> (except the expected collision exclusions);
  2. per family: core MCQ member rows ↔ hub MCQ parts (count, marks, option
     labels) and flattened structured part marks ↔ hub structured part marks
     pairwise — the same checks joinQuestion() applies;
  3. family marks (sum over member rows) equals the hub question's totalMarks;
  4. every package primaryTopicCode/secondaryTopicCode is covered by the
     curriculum draft's node codes (when --draft is supplied);
  5. the skipped set is EXACTLY the expected collision exclusions.

Exit code 0 = the package is import-ready; nonzero = do not import.

Usage:
    python3 scripts/s104_verify_question_package.py \
        --hub-repo /path/to/syllabai-hub \
        --course igcse-maths-a-18-higher \
        --package build/layer3/igcse-maths-a-18-higher.package.json \
        [--draft build/layer3/4ma1-curriculum-draft.json] \
        [--expect-excluded build/layer3/igcse-maths-a-18-higher.build-report.json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MCQ_TYPE = "multiple_choice"
SME_REF_RE = re.compile(r"^(sme-eq-.*)-q(\d+)(-p(\d+)|-s)?$")


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


class Check:
    def __init__(self) -> None:
        self.passed = 0
        self.failed: list[str] = []

    def check(self, cond: bool, msg: str) -> None:
        if cond:
            self.passed += 1
        else:
            self.failed.append(msg)


def family_base(ref: str) -> str | None:
    m = SME_REF_RE.match(ref or "")
    return f"{m.group(1)}-q{m.group(2)}" if m else None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--hub-repo", required=True, type=Path)
    ap.add_argument("--course", required=True)
    ap.add_argument("--package", required=True, type=Path)
    ap.add_argument("--draft", type=Path, default=None)
    ap.add_argument("--expect-excluded", type=Path, default=None,
                    help="the s104 build report; its excluded set must equal the replay skips")
    args = ap.parse_args()

    ck = Check()
    topics = json.loads((args.hub_repo / "content" / args.course / "questions.json").read_text())
    pkg = json.loads(args.package.read_text())
    if pkg.get("packageVersion") != "1.0":
        fail("unsupported package version")

    # ── reassemble the rows the ingest will emit into families ────────────
    families: dict[str, dict] = {}
    for q in pkg["questions"]:
        base = family_base(q["externalRef"])
        ck.check(base is not None, f"package ref outside the SME convention: {q['externalRef']}")
        if base is None:
            continue
        fam = families.setdefault(base, {"members": [], "primary": set(), "secondary": set()})
        if q["questionType"] == "MCQ_SINGLE":
            fam["members"].append({
                "type": "mcq", "marks": q["marks"],
                "options": [o["label"] for o in q["options"]],
            })
        else:
            option_parts = [p for p in q["parts"] if p.get("options")]
            plain_parts = [p for p in q["parts"] if not p.get("options")]
            # mixed emission: option parts became -pK MCQ rows, plain parts one -s row
            for i, p in enumerate(option_parts, start=1):
                fam["members"].append({
                    "type": "mcq", "marks": p["marks"],
                    "options": [o["label"] for o in p["options"]],
                })
            if plain_parts or not option_parts:
                fam["members"].append({
                    "type": "structured",
                    "marks": sum(p["marks"] for p in plain_parts) if option_parts else q["marks"],
                    "parts": [{"label": p["label"], "marks": p["marks"]} for p in plain_parts]
                    if option_parts
                    else [{"label": p["label"], "marks": p["marks"]} for p in q["parts"]],
                })
        fam["primary"].add(q["primaryTopicCode"])
        fam["secondary"].update(q.get("secondaryTopicCodes") or [])

    def join_question(fam: dict, hub_q: dict) -> tuple[bool, str]:
        members = fam["members"]
        core_mcq = [m for m in members if m["type"] == "mcq"]
        core_struct = [m for m in members if m["type"] == "structured"]
        hub_mcq = [p for p in hub_q["parts"] if p.get("questionType") == MCQ_TYPE]
        hub_struct = [p for p in hub_q["parts"] if p.get("questionType") != MCQ_TYPE]
        if len(core_mcq) != len(hub_mcq):
            return False, f"mcq member count {len(core_mcq)} != hub {len(hub_mcq)}"
        core_parts = [pt for m in core_struct for pt in m["parts"]]
        if len(core_parts) != len(hub_struct):
            return False, f"structured part count {len(core_parts)} != hub {len(hub_struct)}"
        for i, (c, h) in enumerate(zip(core_mcq, hub_mcq)):
            if c["marks"] != h["marks"]:
                return False, f"mcq member {i} marks {c['marks']} != hub {h['marks']}"
            hub_labels = [c2["label"] for c2 in (h.get("choices") or [])]
            if hub_labels and not all(lbl in c["options"] for lbl in hub_labels):
                return False, f"mcq member {i} labels {c['options']} do not cover hub {hub_labels}"
        for i, (c, h) in enumerate(zip(core_parts, hub_struct)):
            if c["marks"] != h["marks"]:
                return False, f"structured part {i} marks {c['marks']} != hub {h['marks']}"
        fam_total = sum(m["marks"] for m in members)
        if fam_total != hub_q["totalMarks"]:
            return False, f"family marks {fam_total} != hub totalMarks {hub_q['totalMarks']}"
        return True, ""

    skipped: list[dict] = []
    joined = 0
    claimed_refs: set[str] = set()  # the hub route's claimedRefs guard, mirrored
    topic_summary: list[dict] = []
    for topic in topics:
        t_slug = topic["topicSlug"]
        t_joined = 0
        for q in topic["questions"]:
            ref = f"sme-eq-{t_slug}-q{q['order']}"
            fam = families.get(ref)
            if fam is None:
                skipped.append({"topicSlug": t_slug, "order": q["order"], "id": q["id"], "ref": ref,
                                "reason": "no family (expected: excluded collision)"})
                continue
            if ref in claimed_refs:
                skipped.append({"topicSlug": t_slug, "order": q["order"], "id": q["id"], "ref": ref,
                                "reason": "ref already claimed by an earlier question "
                                          "(hub claimedRefs guard — honest local-only)"})
                continue
            ok, why = join_question(fam, q)
            if not ok:
                skipped.append({"topicSlug": t_slug, "order": q["order"], "id": q["id"], "ref": ref,
                                "reason": why})
                continue
            claimed_refs.add(ref)
            joined += 1
            t_joined += 1
        topic_summary.append({"topicSlug": t_slug, "questions": len(topic["questions"]),
                              "joined": t_joined})

    # ── draft coverage (when supplied) ────────────────────────────────────
    draft_codes: set[str] = set()
    if args.draft:
        draft = json.loads(args.draft.read_text())
        ns = re.sub(r"\W+", "", draft["code"]).upper()
        draft_codes.add(f"{ns}-ROOT")
        for u in draft["units"]:
            draft_codes.add(f"{ns}-{u['code']}")
            for t in u["topics"]:
                draft_codes.add(f"{ns}-{u['code']}-{t['code']}")
                for s in t["subtopics"]:
                    draft_codes.add(f"{ns}-{u['code']}-{s['code']}")
        for q in pkg["questions"]:
            for c in [q["primaryTopicCode"], *(q.get("secondaryTopicCodes") or [])]:
                ck.check(c in draft_codes,
                         f"{q['externalRef']}: topic code {c} missing from the curriculum draft")

    # ── expected exclusions ───────────────────────────────────────────────
    expect = None
    if args.expect_excluded:
        report = json.loads(args.expect_excluded.read_text())
        expect = {(e["topicSlug"], e["order"], e["id"]) for e in report["excluded"]}
        got = {(s["topicSlug"], s["order"], s["id"]) for s in skipped}
        ck.check(got == expect,
                 f"skipped set != expected exclusions: got {sorted(got)}, expected {sorted(expect)}")

    hub_total = sum(len(t["questions"]) for t in topics)
    ck.check(joined + len(skipped) == hub_total,
             f"joined {joined} + skipped {len(skipped)} != hub questions {hub_total}")

    result = {
        "course": args.course,
        "package": str(args.package),
        "corpusVersion": pkg.get("corpusVersion"),
        "hubQuestions": hub_total,
        "families": len(families),
        "joined": joined,
        "skipped": skipped,
        "topicSummary": topic_summary,
        "draftCoverageChecked": bool(args.draft),
        "checksPassed": ck.passed,
        "checksFailed": ck.failed,
        "verdict": "PASS" if not ck.failed else "FAIL",
    }
    out = args.package.with_suffix(".verify-report.json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n")

    print(f"families {len(families)} | joined {joined}/{hub_total} | skipped {len(skipped)}")
    for s in skipped:
        print(f"  skipped: {s['topicSlug']} q{s['order']} {s['id']} — {s['reason']}")
    print(f"checks: {ck.passed} passed, {len(ck.failed)} failed")
    for f in ck.failed:
        print(f"  FAILED: {f}")
    print(f"report: {out}")
    if ck.failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
