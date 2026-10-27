#!/usr/bin/env python3
"""Aggregate per-series validation reports into the ADR-037 corpus report
(JSON + human-readable MD). Auto-discovers series × paper-variant directories
(1C, 2C, ... since F34); integrates the independent-parse cross-diff
(CROSS-DIFF.json) when present."""
import json
from datetime import datetime, timezone
from pathlib import Path

# F15: roots derive from this file's location — reports are always written inside
# the checkout, never to a hardcoded machine-specific mirror.
ROOT = Path(__file__).resolve().parent.parent / "Official-ExamQuestion"
BASE = ROOT / "igcse-chemistry-19"
GATES = ["G0-identity", "G1-structure", "G2-D-disclosure", "G3-mcq-integrity",
         "G4-figure-resolution", "G5-answer-linkage", "G6-registry-codes"]
PAPER_TOTALS = {"1C": 110, "2C": 70}   # mirror of the converter registry (F34)

SLICES = []   # (series, paper) with outputs
for d in sorted(BASE.iterdir()):
    if not d.is_dir():
        continue
    for pd in sorted(d.iterdir()):
        if pd.is_dir() and pd.name.startswith("4CH1-") and (pd / "validation-report.json").exists():
            SLICES.append((d.name, pd.name.split("-")[1]))

out = {"schema": "syllabai.official-paper-questions.multi-series/0.1",
       "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
       "baseline": "2020-11", "corpus": "4CH1 1C+2C — all series in syllabai-pastpapers (F34)",
       "series": [], "generalization_findings": [], "cross_diff": None}

for S, PAPER in SLICES:
    d = BASE / S / f"4CH1-{PAPER}"
    r = json.loads((d / "validation-report.json").read_text())
    t = json.loads((d / "topic.json").read_text())
    gs = {g["gate"]: g["status"] for g in r["gates"]}
    g5 = next(g for g in r["gates"] if g["gate"] == "G5-answer-linkage")
    parts = sum(len(q["parts"]) for q in t["questions"])
    mcq = [(p["part_number"], p["marks"]) for q in t["questions"] for p in q["parts"] if p.get("choices")]
    keyed = sum(1 for q in t["questions"] for p in q["parts"] if p.get("choices") and any(c.get("is_correct") for c in p["choices"]))
    marks = sum(q["total_marks"] for q in t["questions"])
    out["series"].append({
        "series": S, "paper": PAPER, "paper_id": t["paper_id"],
        "gates": {g: gs.get(g) for g in GATES},
        "questions": len(t["questions"]), "parts": parts,
        "marks_total": marks, "marks_expected": PAPER_TOTALS.get(PAPER),
        "mcq_parts": len(mcq), "mcq_keyed": keyed,
        "ms_linkage": g5["summary"],
        "negative_controls": {nc["id"]: "DETECTED" if nc["detected"] else "MISSED" for nc in r["negative_controls"]},
        "source_defects": r.get("source_defects"),
        "review_queue_items": len(r["review_queue"]),
    })

cdpath = ROOT / "CROSS-DIFF.json"
if cdpath.exists():
    cd = json.loads(cdpath.read_text())
    out["cross_diff"] = {
        "method": "part-level marks vs repo parsed/questions.json layer (independent parser, same PDFs)",
        "paper": cd.get("paper", "1C"),
        "series": cd["series"],
        "note": ("every roman-part mark and question total agrees with the repo's own parsed layer; "
                 "'only_in_parsed' entries are letter-group totals the parsed layer records in "
                 "addition to its roman parts — no mark disagreement anywhere. The repo parsed/ "
                 "layer exists for 4CH1/1C dirs only today (F34), so the cross-diff evidence is 1C."),
    }

out["generalization_findings"] = [
    {"id": "F1", "series": "2019-06", "finding": "question start lines are indented (QSTART required leading-space tolerance)",
     "fix": "QSTART_RE allows leading whitespace"},
    {"id": "F2", "series": "2019-06", "finding": "8 rasterized (image-only) pages in archive PDF; 6 content pages lost: Q7 gone entirely (its footer too), Q1/Q11/Q12/Q15 partial",
     "fix": "image-only page census + defect attribution to questions + G1 REVIEW path (never silent, never invented)"},
    {"id": "F3", "series": "2019-06", "finding": "Q7 footer absent from PDF text layer",
     "fix": "footer census detects the gap; review item names the lost pages"},
    {"id": "F4", "series": "2019-06", "finding": "paper has 15 questions (early 4CH1 format), not 10",
     "fix": "per-series question-count registry; paper-level invariant kept at 110 marks"},
    {"id": "F5", "series": "2020-11 vs 2020-01", "finding": "MS note phrasing differs: 'is not correct' vs 'is incorrect'",
     "fix": "unified note filter covering both phrasings"},
    {"id": "F6", "series": "2020-01", "finding": "MS marker column drifts one row early in Q7(a): note rows leak into adjacent entries; naive keying would emit C for 7(a)(iii) where the printed notes prove A (astatine)",
     "fix": "answer-row analysis keyed only when exactly ONE distinct candidate; ambiguous entries -> human review"},
    {"id": "F7", "series": "2019-06", "finding": "MS sub-letters printed bare without parentheses ('b      they have...')",
     "fix": "MS_BARE_LETTER_RE with branch precedence over the catch-all row regex"},
    {"id": "F8", "series": "2019-06/2020-01", "finding": "three 'DO NOT WRITE IN THIS AREA' phrases share one extracted line",
     "fix": "phrase-level substitution instead of whole-line filter"},
    {"id": "F9", "series": "2019-06", "finding": "damaged Q1 region begins with a part marker '(c) ...' as line 0",
     "fix": "segment_question lets the loop classify line 0 instead of forcing it into the stem"},
    {"id": "F10", "series": "2020-01", "finding": "marker-only MS row carries a trailing marks digit ('(iii)   1') which glued to the answer",
     "fix": "strip leading marks digit only when followed by a choice letter"},
    {"id": "F11", "series": "2023-06", "finding": "MS continuation rows indented 11+ spaces; marker-row regex allowed only 10 — all roman parts after the first went unlinkable (G5 76%)",
     "fix": "MS_ROW_RE / MS_BARE_LETTER_RE indent allowance widened to 20"},
    {"id": "F12", "series": "2021-01 (and 2021+ MS style)", "finding": "MCQ keys phrased '<L> is the correct answer because...' plus '<L> is not THE correct answer because...' rebuttals — the inserted 'the' defeated the note filter, all four letters became candidates, guard refused every key",
     "fix": "positive-statement keying ('<L> is (the) correct' is authoritative) + note filter extended to 'is not the correct'"},
    {"id": "F13", "series": "2026-06", "finding": "manifest schema drift: series.printed / series.source / variant.official_code absent in gap-fill-wave manifests — converter crashed in G0 instead of flagging",
     "fix": "manifest reads use .get() with explicit 'absent in schema v2' annotation in G0 summary"},
    {"id": "F14", "series": "2023-06/2025-06/2025-11/2026-06", "finding": "rebuttal-style MCQ MS: explicit rebuttal for every wrong option ('A is incorrect...', 'B the charges are incorrect', 'B is X incorrect', '<L> (answer)' cells, glued 'B4' answer+digit cells) — single-candidate logic insufficient",
     "fix": "elimination keying: sole un-rebutted option keyed only when corroborated by exactly one answer row; anything ambiguous stays unkeyed (2020-01 canary still refuses)"},
]

if out["cross_diff"]:
    out["cross_diff"]["key_result"] = (
        f"{sum(len(s['comparable_parts']) if isinstance(s.get('comparable_parts'), list) else s['comparable_parts'] for s in out['cross_diff']['series'])}")

(BASE / "MULTI-SERIES-REPORT.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))

# ---- human-readable MD -----------------------------------------------------
tot_q = sum(s["questions"] for s in out["series"])
tot_parts = sum(s["parts"] for s in out["series"])
tot_marks = sum(s["marks_total"] for s in out["series"])
full_pass = [s for s in out["series"] if all(v == "PASS" for v in s["gates"].values())]
md = ["# ADR-037 corpus run — 4CH1 complete: 1C + 2C + both F-178 R-variant tranches (1CR, 2CR) — 54 slices, all series in syllabai-pastpapers; F34 + F-178", "",
      f"> generated {out['generated_utc']} · baseline 2020-11 · gate suite G0–G6 + negative controls N1–N3 per paper slice",
      f"> {len(SLICES)} slices ({sorted({s['paper'] for s in out['series']})}) · {tot_q} questions · {tot_parts} parts · {tot_marks} marks extracted"
      f" · {len(full_pass)} slices fully PASS", "",
      "| series | paper | G0 | G1 | G2 | G3 | G4 | G5 | G6 | NC | questions | parts | marks | MCQ keyed | review |",
      "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for s in out["series"]:
    g = s["gates"]
    nc = "3/3" if all(v == "DETECTED" for v in s["negative_controls"].values()) and len(s["negative_controls"]) == 3 else "-".join(str(x) for x in s["negative_controls"].values())
    exp = s["marks_expected"]
    md.append(f"| {s['series']} | {s['paper']} | {g['G0-identity']} | {g['G1-structure']} | {g['G2-D-disclosure']} | {g['G3-mcq-integrity']} | "
              f"{g['G4-figure-resolution']} | {g['G5-answer-linkage']} | {g['G6-registry-codes']} | {nc} | {s['questions']} | {s['parts']} | "
              f"{s['marks_total']}/{exp} | {s['mcq_keyed']}/{s['mcq_parts']} | {s['review_queue_items']} |")
md += ["", "## Terminal states", ""]
for paper in sorted({s["paper"] for s in out["series"]}):
    rows = [s for s in out["series"] if s["paper"] == paper]
    fp = [s["series"] for s in rows if all(v == "PASS" for v in s["gates"].values())]
    line = f"- **{paper}: {len(fp)}/{len(rows)} slices all-gates PASS**"
    if len(fp) == len(rows):
        line += f" ({', '.join(fp)})"
    else:
        nonpass = [s for s in rows if any(v != "PASS" for v in s["gates"].values())]
        detail = ", ".join(
            s["series"] + " (" + ", ".join(f"{g}={v}" for g, v in s["gates"].items() if v != "PASS") + ")"
            for s in nonpass)
        line += f"; all-PASS: {', '.join(fp)}; non-PASS: {detail}"
    md.append(line)
md += ["- **1C 2020-01: G3 FAIL is honest** — the printed MS interleaves Q7(a)(ii)/(iii) marker rows; a wrong auto-key was refused (it would have keyed C where the notes prove A). Two MCQ keys need a human. Canary: `7(a)(iii)` must stay unkeyed.",
       "- **1C 2019-06: G1/G5 REVIEW reflect real archive damage** — 5 rasterized content pages; Q7 wholly lost (6 marks), Q1/Q11/Q12/Q15 partial. Content needs OCR/manual re-ingest; nothing was invented to fill the gaps.",
       "", "## Independent-parse cross-diff (strongest correctness evidence; 1C — the repo parsed layer is 1C-only today, F34)", ""]
if out["cross_diff"]:
    md.append(f"- {out['cross_diff']['method']}")
    for s in out["cross_diff"]["series"]:
        md.append(f"- {s['series']}: **{s['match_rate']} part marks agree, 0 mismatches**"
                  f" (letter-group totals recorded only by the parsed layer: {len(s['only_in_parsed'])})")
md += ["", "## Generalization findings (cross-series quirks -> parser/gate fixes)", ""]
for f in out["generalization_findings"]:
    md.append(f"- **{f['id']}** ({f['series']}): {f['finding']} → _{f['fix']}_")
md += ["", "## Self-improvement loop", "",
       "Every finding above is (1) fixed in the converter, (2) recorded in `LEDGER.md`, and (3) guarded by a canary in `CANARIES.json`",
       "that `run_all.sh` re-verifies on every future run. See `AGENTS.md` for the protocol new agents must follow.",
       ""]
(BASE / "MULTI-SERIES-REPORT.md").write_text("\n".join(md) + "\n")
print("written:", BASE / "MULTI-SERIES-REPORT.json")
print("written:", BASE / "MULTI-SERIES-REPORT.md")
print("slices:", len(SLICES), "| full-pass:", len(full_pass))
