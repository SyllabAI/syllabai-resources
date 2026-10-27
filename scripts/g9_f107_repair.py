#!/usr/bin/env python3
"""
g9_f107_repair.py — F107: the 2023-06 4CH1-2CR 7(c)(i)/(ii) image-answer repair.

DEFECTS OF RECORD (found by the post-merge canary re-run; both evidence-eyeballed
at 300 dpi from the archive of record):

1. 7(c)(i): the printed MS answer cell is a HAND-ANNOTATED PHOTOGRAPH of the QP
   displayed formula with the ester functional group circled in pen. The original
   converter had no image-answer path for this row and captured the marks-column
   digit "1" as BOTH solution_md and mark_points text (the marks-digit leak, C99's
   own documented class). Task 19 hygiene-v2 r0 (4c11a041) then emptied
   solution_md per the F97 honest-empty decision — but the promised fail-visible
   carry (G7 census + review queue) was never materialized and canaries C13/C71
   (which predate the C99 carve-out) have been red on main ever since.
   REPAIR (the F47/C52/C80 doctrine — the same treatment as 2021-01 2CR 7(d)):
   the eyeballed verbatim transcription is materialized into the corpus
   solution_md + mark_points, the F47 ledger (MS-LINK-OVERRIDES.json) carries the
   evidence chain, and a new canary C109 pins the part.

2. 7(c)(ii): the SOLUTION-ENRICH.json authored enrichment says "propanoic acid,
   CH3CH2COOH" with a straight-chain formula — chemically WRONG against the
   printed evidence: the QP displayed formula (p23) is methyl 2-methylpropanoate
   (branched: CH3-CH(CH3)-C(=O)OCH3) and the MS's own 7(c)(ii) image answer draws
   2-methylpropanoic acid ((CH3)2CHCOOH, branched, with the O-H displayed —
   consistent with the printed "REJECT -OH not displayed" note). Mode B
   correction with rendered-page evidence; correction_of_record disclosed in the
   ledger entry. Changes the SERVED solutionMd -> exporter disclosure census
   required (2026-10-27-f107-ms-image-answer.json).

Exactly-once asserted edits; nothing else touched.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLICE = ROOT / "Official-ExamQuestion" / "igcse-chemistry-19" / "2023-06" / "4CH1-2CR"

TRANSCRIPTION = (
    "H        H              O\n"
    "|        |              ||\n"
    "H - C  -   C  -  C\n"
    "|        |     \\\n"
    "H    H - C - H    O - C - H\n"
    "     |                |\n"
    "     H                H\n"
    "\n"
    "(the printed answer cell is a hand-annotated photograph of the QP displayed\n"
    "formula: a pen circle is drawn around the ester functional group - the\n"
    "carbonyl C, its double-bond O and the bridging O, i.e. the C(=O)-O- linkage)"
)

EVIDENCE_REF = (
    "Printed MS of record 2023-06 4CH1-2CR p13: the 7(c)(i) Answer cell is an "
    "embedded hand-annotated photograph - the QP displayed formula redrawn with a "
    "pen circle around the ester functional group (carbonyl C + double-bond O + "
    "bridging O); the text layer has NO extractable answer (pdftotext empty cell; "
    "archive parsed/ms.md prints 'P3 (1 mark)' with no answer text). Marks column "
    "reads 1. The pre-hygiene corpus carried the marks-column digit '1' as the "
    "answer (the marks-digit leak, C99's documented class); Task 19 hygiene-v2 r0 "
    "(4c11a041) emptied it per the F97 honest-empty decision whose promised "
    "fail-visible carry (G7 census + review queue) was never materialized, leaving "
    "canaries C13/C71 red on main. Repaired per the F47 image-answer doctrine "
    "(the 2021-01 2CR 7(d) precedent): the eyeballed verbatim transcription of the "
    "printed drawing is materialized into the corpus (solution_md + mark_points), "
    "the F47 ledger entry carries the evidence chain, canary C109 pins the part. "
    "Nothing is added beyond the drawing's own 2D letter arrangement + the circle's "
    "scope. Evidence: 300-dpi render of MS p13 (answer-cell bbox), QP p23 printed "
    "displayed formula (methyl 2-methylpropanoate, branched)."
)


def exactly_once(old, new, text, label):
    n = text.count(old)
    assert n == 1, f"{label}: expected exactly 1 occurrence, found {n}"
    return text.replace(old, new)


def main():
    # ── 1. the corpus part 7(c)(i) ──────────────────────────────────────────
    tp = SLICE / "topic.json"
    t = json.loads(tp.read_text())
    hit = 0
    already = 0
    for q in t["questions"]:
        for p in q["parts"]:
            if p.get("part_number") == "7(c)(i)":
                hit += 1
                if p.get("edit_status") == "corrected" and p.get("solution_md") == TRANSCRIPTION:
                    already += 1  # idempotent re-run: step 1 already applied
                    continue
                assert p.get("solution_md") == "", "7(c)(i) solution_md not in the expected empty state"
                assert p.get("mark_points") and p["mark_points"][0]["text_md"] == "1", \
                    "7(c)(i) MP text not the marks-digit leak state"
                assert p.get("edit_status") == "extracted", p.get("edit_status")
                p["solution_md"] = TRANSCRIPTION
                p["mark_points"][0]["text_md"] = TRANSCRIPTION
                p["edit_status"] = "corrected"
                p["answer_key_source"] = "ms-link-overrides-ledger"
                p["edits"] = [{
                    "field": "solution_md+mark_points[0].text_md",
                    "kind": "structural-repair",
                    "tool": "g9_f107_repair.py (F107, canary C13/C71 red-state repair)",
                    "evidence_ref": EVIDENCE_REF,
                }]
                p["value_trace"] = {
                    "keys": "n/a",
                    "marks": "ms-printed",
                    "numbers": "source-printed",
                    "solution": "ms-image-eyeball-transcription (F47 ledger 2023-06/2CR/7(c)(i))",
                }
    assert hit == 1, f"expected exactly 1 part 7(c)(i), found {hit}"
    if already:
        print("1. corpus 7(c)(i) already repaired (idempotent skip)")
    else:
        tp.write_text(json.dumps(t, indent=1, ensure_ascii=False) + "\n")
        print("1. corpus 7(c)(i) repaired (transcription materialized, disclosure edits[] added)")

    # ── 2. the F47 ledger entry (MS-LINK-OVERRIDES.json) ────────────────────
    mlo_path = ROOT / "Official-ExamQuestion" / "MS-LINK-OVERRIDES.json"
    mlo = json.loads(mlo_path.read_text())
    assert isinstance(mlo.get("entries"), list), type(mlo.get("entries")).__name__
    key = "2023-06:2CR:7(c)(i)"
    assert not any(e.get("series") == "2023-06" and e.get("paper") == "2CR"
                   and e.get("part") == "7(c)(i)" for e in mlo["entries"]), \
        "ledger entry already present"
    mlo["entries"].append({
        "series": "2023-06",
        "paper": "2CR",
        "part": "7(c)(i)",
        "marks": 1,
        "evidence": (
            "printed MS p13: the 7(c)(i) Answer cell is an embedded hand-annotated "
            "PHOTOGRAPH - the QP displayed formula (methyl 2-methylpropanoate, "
            "branched) redrawn with a pen circle around the ester functional group "
            "(the carbonyl C, its double-bond O and the bridging O). Marks column "
            "reads 1; Notes column empty; page footer '(Total for Question 7 = 9)'. "
            "The text layer has NO extractable answer text for this cell "
            "(pdftotext -layout: empty answer cell; archive parsed/ms.md: 'P3 "
            "(1 mark)', no answer). The original converter read the marks-column "
            "digit as the answer (the marks-digit leak; C99's documented class); "
            "hygiene-v2 r0 emptied the field per F97's honest-empty decision but "
            "the promised census/review-queue carry never materialized and C13/C71 "
            "went red on main. This ledger entry supplies the eyeballed verbatim "
            "transcription of the printed drawing (the F47 doctrine, the C52/C80 "
            "class; render evidence: 300-dpi render of MS p13, answer-cell region; "
            "QP p23 printed displayed formula cross-checked). Nothing is added or "
            "reworded beyond the drawing's own 2D letter arrangement + the circle "
            "scope. Supersedes the honest-empty state recorded in C99's assertion."
        ),
        "ms_lines": [
            "H        H              O",
            "|        |              ||",
            "H - C  -   C  -  C",
            "|        |     \\",
            "H    H - C - H    O - C - H",
            "     |                |",
            "     H                H",
            "(pen circle around the carbonyl C, its double-bond O and the bridging O)",
        ],
        "mark_points": "P3 (1 mark) - no printed answer text",
        "source_page": 13,
    })
    mlo_path.write_text(json.dumps(mlo, indent=1, ensure_ascii=False) + "\n")
    print("2. F47 ledger entry appended:", key)

    # ── 2b. the validation-report application of record (C57 contract) ─────
    rep_path = SLICE / "validation-report.json"
    rep = json.loads(rep_path.read_text())
    applied = rep.setdefault("ms_link_overrides_applied", [])
    if "2023-06:2CR/7(c)(i)" not in applied:
        applied.append("2023-06:2CR/7(c)(i)")
        rep_path.write_text(json.dumps(rep, indent=1, ensure_ascii=False) + "\n")
        print("2b. validation-report ms_link_overrides_applied += 2023-06:2CR/7(c)(i)")
    else:
        print("2b. validation-report already lists the application (idempotent skip)")

    # ── 3. the 7(c)(ii) enrichment correction (Mode B) ──────────────────────
    se_path = ROOT / "Official-ExamQuestion" / "SOLUTION-ENRICH.json"
    se = json.loads(se_path.read_text())
    e = se["entries"]["2023-06-2CR:7-c-ii"]
    old_sol = e["solutionMd"]
    if "propanoic acid, CH₃CH₂COOH" not in old_sol:
        assert "2-methylpropanoic acid" in old_sol, old_sol[:120]
        print("3. enrichment 7-c-ii already corrected (idempotent skip)")
    else:
        assert "(CH3)2CH" not in old_sol
        corrected = (
            "**Answer: 2-methylpropanoic acid, (CH₃)₂CHCOOH.**\n\n"
            "Methanol provides the –OCH₃ half of the ester, so the carboxylic acid must "
            "provide the (CH₃)₂CHC(=O)– half: the printed displayed formula is "
            "methyl 2-methylpropanoate — the carbon next to the ester group carries a "
            "CH₃ branch (H–C(H)(H)–C(H)(CH₃)–C(=O)–O–CH₃) — so joining "
            "2-methylpropanoic acid to methanol, with water eliminated, gives the ester "
            "shown. Its fully displayed formula draws every bond, including the acid "
            "O–H (the MS rejects an undisplayed –OH): the mark-scheme answer cell is a "
            "hand-drawn displayed formula of (CH₃)₂CHCOOH with every H shown.\n"
        )
        e["solutionMd"] = corrected
        e["correction_of_record"] = {
            "field": "solutionMd",
            "kind": "evidence-required-correction (Mode B)",
            "tool": "g9_f107_repair.py (F107)",
            "previous_text": "propanoic acid, CH₃CH₂COOH (straight-chain H–C(H)(H)–C(H)(H)–C(=O)–O–H)",
            "evidence_ref": (
                "Printed MS of record 2023-06 4CH1-2CR p13: the 7(c)(ii) Answer cell is "
                "an embedded hand-drawn displayed formula of the acid WITH THE BRANCH - "
                "H-C(H)(H)-C(H)(CH3)-C(=O)-O-H, i.e. 2-methylpropanoic acid "
                "((CH3)2CHCOOH), O-H displayed (consistent with the printed 'REJECT -OH "
                "not displayed' note). The QP p23 displayed formula of the ester is "
                "methyl 2-methylpropanoate (branched: the carbon next to the ester "
                "group carries a CH3). The previous text misread the printed structure "
                "as the straight-chain propanoic acid - a Mode B graded-semantic error "
                "served to learners. Eyeballed twice at 300 dpi (MS answer-cell crops, "
                "QP diagram crop)."
            ),
            "adjudicated_utc": "2026-10-27",
        }
        se_path.write_text(json.dumps(se, indent=1, ensure_ascii=False) + "\n")
        print("3. enrichment 7-c-ii corrected (2-methylpropanoic acid) + correction_of_record disclosed")

    print("ALL F107 REPAIRS APPLIED")


if __name__ == "__main__":
    main()
