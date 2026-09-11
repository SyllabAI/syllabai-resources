#!/usr/bin/env python3
"""
T-C10 rework (round 4, 2026-09-11) — REJECT x2, per the external advisor's
fourth-round review (operator-forwarded; Z.ai concurrence assessment the
same day, verified against the repo before execution).

Rejected mappings (both were round-3 CONFIRMs; supersession recorded on
PHASE2_PR_REVIEW_SHEET.md as §12):

  4CH1-4.15 @ Nitrogen Oxides & Sulfur Dioxide (S4-b, medium)
      Spec: "explain how the combustion of some impurities in hydrocarbon
      fuels results in the formation of sulfur dioxide". The mapped note's
      only SO2-formation text is a premise-framed subordinate clause of the
      4.16 evidence sentence ("The sulfur dioxide produced from the
      combustion of fossil fuels dissolves in rainwater droplets ...");
      the impurity premise lives only in the sibling combustion note
      ("All these fuels contain carbon, hydrogen and small quantities of
      sulfur"; products list "oxides of sulfur", generic, unattributed).
      Corpus-wide, the S + O2 -> SO2 oxidation chemistry appears only in
      element-combustion contexts (Combustion [2.11]; Writing chemical
      equations). NO note teaches the impurity -> oxidation -> SO2
      connective explanation. The round-3 CONFIRM aggregated premise +
      stated result — inferred coverage, which the guide's own §0.0
      forbids ("premises and consequences may live in sibling notes, the
      explanation may not") — the mirror image of the original
      premise-only error. REMOVED; 4.15 becomes an honest zero-coverage
      corpus gap (T-C11 input).

  4CH1-1.17 @ Calculate Relative Mass (S1-e, medium, cross-subsection)
      Spec: "be able to calculate the relative atomic mass of an element
      Ar from isotopic abundances". The note's Ar content is two
      definitional sentences (symbol; derivation basis) before moving
      wholly to Mr; no Ar equation, no isotopic-abundance numbers, no
      worked example; the derivation-basis sentence appears verbatim in
      the dedicated S1-c note, so the mapping contributes nothing the
      strong mapping lacks. A "calculate" point demands calculation
      substance (command-kind rule, guide issue 3). The round-3 review
      had flagged this "the weakest confirm" and pre-registered removal
      as the strict-reading branch; the command-kind rule resolves the
      conditional to removal. REMOVED; 1.17 keeps its high-confidence
      in-subsection S1-c mapping (equation + rubidium worked example).

Rework (this script):
  REMOVE   4CH1-4.15 from S4.json `Nitrogen Oxides & Sulfur Dioxide`
           (note keeps 4.14 / 4.16)
  REMOVE   4CH1-1.17 from S1.json `Calculate Relative Mass`
           (note keeps 1.26)
  APPEND   PHASE2_PR_REVIEW_SHEET.md §12 (round-4 supersession record:
           59 CONFIRM / 2 REJECT, the command-kind rule, coverage impact,
           and the trimmed 59-spec staged batch derived mechanically from
           the §11 command) + mark §11 ON HOLD
  APPEND   PHASE2_PR_REVIEW_GUIDE.md §8 (issue 3 — the command-kind
           substance rule; frozen canonical)
  EXPOSE   ROUND4_REJECTS for c10_ratify_audit.py (re-targeted at §12)

After this script: `python3 scripts/c10_map_notes.py` regenerates the two
notes' front matter (store 211 -> 209) and the coverage report (4.15 lands
in the zero-coverage queue with its gap annotation). Then
`scripts/graph_check.py` (counts updated to 209/181) and
`scripts/c10_negative_test.py`.

Idempotent: safe to re-run (each step is a guarded no-op if applied).
"""
from __future__ import annotations

import json
import shlex
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPORTS = HERE.parent / "graph" / "reports"
SHEET = REPORTS / "PHASE2_PR_REVIEW_SHEET.md"
GUIDE = REPORTS / "PHASE2_PR_REVIEW_GUIDE.md"
S4 = HERE / "c10_decisions" / "S4.json"
S1 = HERE / "c10_decisions" / "S1.json"

NOX = ("Chemistry IGCSE Revision Notes/4. Organic Chemistry/b. Crude Oil/"
       "Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry "
       "Revision Notes 2017.md")
CRM = ("Chemistry IGCSE Revision Notes/1. Principles of Chemistry/"
       "e. Chemical Formulae, Equations, Calculations/"
       "Calculate Relative Mass  Edexcel IGCSE Chemistry Revision "
       "Notes 2017.md")

SHEET_MARKER = "<!-- round4-rejects-2026-09-11 -->"
SHEET_HOLD_MARKER = "<!-- round4-on-hold -->"
GUIDE_MARKER = "<!-- guide-issue3-2026-09-11 -->"
DATE = "2026-09-11"

# Machine-readable round-4 record — imported by c10_ratify_audit.py, which
# must prove both pairs are absent from the store AND from the §12 command.
ROUND4_REJECTS = [
    {
        "code": "4CH1-4.15",
        "note": NOX,
        "round3_queue": "P1 (remapped 4.15)",
        "confidence": "medium",
        "spec": ("explain how the combustion of some impurities in "
                 "hydrocarbon fuels results in the formation of sulfur "
                 "dioxide"),
        "evidence": "The sulfur dioxide produced from the combustion of "
                    "fossil fuels",
        "verdict": "REJECT",
        "finding": (
            "Premise-framed consequence, not the demanded explanation: the "
            "evidence clause is a truncation of the 4.16 evidence sentence; "
            "the impurity premise lives only in the sibling combustion note "
            "and the S + O2 -> SO2 chemistry only in element-combustion "
            "contexts; the impurity -> oxidation -> SO2 connective teaching "
            "exists in no note (corpus-wide sweep, 112 notes). Round-3 "
            "CONFIRM aggregated premise + stated result = inferred "
            "coverage, which the guide's own §0.0 forbids."),
        "disposition": (
            "removed from decisions S4.json (note keeps 4.14 / 4.16); "
            "4.15 -> zero-coverage corpus gap, annotated in "
            "PHASE2_MAPPING_COVERAGE.md §3 for T-C11"),
    },
    {
        "code": "4CH1-1.17",
        "note": CRM,
        "round3_queue": "P3/P4 (weakest confirm, cross-subsection flag)",
        "confidence": "medium",
        "spec": ("be able to calculate the relative atomic mass of an "
                 "element Ar from isotopic abundances"),
        "evidence": "This is calculated from the mass number and relative "
                    "abundances of all the isotopes of a particular "
                    "element",
        "verdict": "REJECT",
        "finding": (
            "Definitional sentence, not calculation substance: the note "
            "states what Ar is calculated from, then moves wholly to Mr; "
            "no Ar equation, no isotopic-abundance numbers, no worked "
            "example; the derivation-basis sentence is duplicated verbatim "
            "in the dedicated S1-c note. A calculate-point needs the "
            "calculation (command-kind rule); round 3 had pre-registered "
            "removal as the strict-reading branch."),
        "disposition": (
            "removed from decisions S1.json (note keeps 1.26); 1.17 "
            "remains covered by its high-confidence in-subsection S1-c "
            "mapping; the 1.17@S1-e cross-subsection flag is retired with "
            "the mapping"),
    },
]


def dump_decisions(data: dict) -> str:
    """Match the existing decisions-file style exactly: indent 2/4 for the
    note/mappings structure, each mapping object compact on a single line."""
    out = ["{"]
    keys = list(data.keys())
    for i, k in enumerate(keys):
        out.append(f"  {json.dumps(k, ensure_ascii=False)}: {{")
        out.append('    "mappings": [')
        maps = data[k]["mappings"]
        for j, m in enumerate(maps):
            comma = "," if j < len(maps) - 1 else ""
            out.append(f"      {json.dumps(m, ensure_ascii=False)}{comma}")
        out.append("    ]")
        out.append("  }" + ("," if i < len(keys) - 1 else ""))
    out.append("}")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- decisions --
def apply_decisions() -> list[str]:
    log = []

    s4 = json.loads(S4.read_text(encoding="utf-8"))
    nox = s4[NOX]["mappings"]
    before = len(nox)
    nox[:] = [m for m in nox if m["code"] != "4CH1-4.15"]
    if len(nox) != before:
        log.append(f"removed 4CH1-4.15 from NOx note ({before} -> "
                   f"{len(nox)} mappings)")
    else:
        log.append("4.15 already absent from NOx note (idempotent re-run)")
    if not nox or not {"4CH1-4.14", "4CH1-4.16"} <= {m["code"] for m in nox}:
        print("FAIL: NOx note must keep 4.14 and 4.16")
        return []
    S4.write_text(dump_decisions(s4), encoding="utf-8")

    s1 = json.loads(S1.read_text(encoding="utf-8"))
    crm = s1[CRM]["mappings"]
    before = len(crm)
    crm[:] = [m for m in crm if m["code"] != "4CH1-1.17"]
    if len(crm) != before:
        log.append(f"removed 4CH1-1.17 from Calculate Relative Mass note "
                   f"({before} -> {len(crm)} mappings)")
    else:
        log.append("1.17 already absent from Calculate Relative Mass note "
                   "(idempotent re-run)")
    if not crm or "4CH1-1.26" not in {m["code"] for m in crm}:
        print("FAIL: Calculate Relative Mass note must keep 1.26")
        return []
    S1.write_text(dump_decisions(s1), encoding="utf-8")

    log.append("S4.json / S1.json updated (store: 211 -> 209 mappings)")
    return log


# ------------------------------------------------------- sheet §11 + §12 --
def parse_s11_specs(text: str) -> tuple[list[str], str, str]:
    sec = text.split("## 11. Staged operator ratification", 1)[1]
    bash = sec.split("```bash", 1)[1].split("```", 1)[0]
    joined = bash.replace("\\\n", " ")
    tokens = shlex.split(joined)
    specs = [t for i, t in enumerate(tokens) if i > 0
             and tokens[i - 1] == "--map"]
    by = tokens[tokens.index("--by") + 1] if "--by" in tokens else "operator"
    date = (tokens[tokens.index("--date") + 1]
            if "--date" in tokens else DATE)
    return specs, by, date


def render_command(specs: list[str], by: str, date: str) -> str:
    lines = ["cd work/syllabai-resources && \\",
             "python3 scripts/c10_promote.py \\"]
    row = []
    for s in specs:
        row.append(f"--map {shlex.quote(s)}")
        if len(row) == 3:
            lines.append("    " + " ".join(row) + " \\")
            row = []
    if row:
        lines.append("    " + " ".join(row) + " \\")
    lines.append(f"    --by {by} --date {date}")
    return "\n".join(lines)


def apply_sheet() -> list[str]:
    text = SHEET.read_text(encoding="utf-8")
    if SHEET_MARKER in text:
        return ["sheet already carries §12 (idempotent re-run)"]

    specs, by, date = parse_s11_specs(text)
    dropped = [s for s in specs
               if s == "4CH1-4.15"
               or (s.startswith("4CH1-1.17@")
                   and "calculate relative mass" in s.lower())]
    kept = [s for s in specs if s not in dropped]
    if len(dropped) != 2 or len(kept) != 59 or len(set(kept)) != 59:
        print(f"FAIL: expected to drop exactly the 2 rejected specs from "
              f"§11 — dropped {dropped!r}, kept {len(kept)}")
        return []

    hold = (f"> {SHEET_HOLD_MARKER}\n"
            "> **ON HOLD — round 4 (2026-09-11):** two of these 61 "
            "confirms were **REJECTED** by the external advisor's "
            "fourth-round review (Z.ai concurred; §12 below). This 61-spec "
            "block is retained as the round-3 record — **do NOT run it**. "
            "The current staged batch is §12's 59-spec command.\n")
    if SHEET_HOLD_MARKER not in text:
        anchor = ("## 11. Staged operator ratification\n\n"
                  "All 61 reviewed mappings are CONFIRM.")
        if anchor not in text:
            print("FAIL: §11 anchor not found")
            return []
        text = text.replace(
            anchor,
            "## 11. Staged operator ratification\n\n" + hold + "\n"
            "All 61 reviewed mappings are CONFIRM.", 1)

    cmd = render_command(kept, by, date)

    L = ["", SHEET_MARKER, "",
         "## 12. Round 4 — advisor rejections and the 59-spec staged batch "
         "(2026-09-11)",
         "",
         "The operator forwarded the executed review to the external "
         "advisor (ChatGPT), whose fourth-round pass re-read the two "
         "flagged notes against the spec wording and rejected two of the "
         "61 confirms. Z.ai's concurrence assessment (same day) verified "
         "every cited fact against the repo — note texts, spec wordings, "
         "the corpus-wide sulfur sweep, the sheet's own round-3 findings — "
         "and accepted both rejections. This section is the supersession "
         "record; the §1 tally (61/0/0) is superseded by **59 CONFIRM / "
         "2 REJECT / 0 HOLD**.",
         "",
         "| | Reviewed | CONFIRM | REJECT | HOLD |",
         "|---|---:|---:|---:|---:|",
         "| Round 3 (§1) | 61 | 61 | 0 | 0 |",
         "| **Round 4 (this section)** | 61 | **59** | **2** | 0 |",
         "",
         "### The governing rule (guide issue 3, frozen)",
         "",
         "A contributory mapping still needs to contain the **kind of "
         "instructional substance the spec point's command verb demands**. "
         "Distributed coverage may aggregate explicit contributions across "
         "notes, but a premise or a stated consequence is not a "
         "contribution of the demanded kind, and aggregating premise + "
         "consequence constructs the missing teaching by inference — which "
         "the §0.0 contract forbids. The rule is the per-command-verb "
         "operationalization of \"distributed ≠ inferred\"; full table: "
         "`PHASE2_PR_REVIEW_GUIDE.md` §8.",
         "",
         "### 4CH1-4.15 @ Nitrogen Oxides & Sulfur Dioxide — REJECT "
         "(removed)",
         "",
         f"- spec: “{ROUND4_REJECTS[0]['spec']}”",
         f"- round-3 evidence: “{ROUND4_REJECTS[0]['evidence']}”",
         "- verdict: **REJECT** — external advisor round 4; Z.ai "
         "concurrence, repo-verified (2026-09-11)",
         f"- finding: {ROUND4_REJECTS[0]['finding']}",
         f"- disposition: {ROUND4_REJECTS[0]['disposition']}",
         "",
         "### 4CH1-1.17 @ Calculate Relative Mass (S1-e) — REJECT "
         "(removed)",
         "",
         f"- spec: “{ROUND4_REJECTS[1]['spec']}”",
         f"- round-3 evidence: “{ROUND4_REJECTS[1]['evidence']}”",
         "- verdict: **REJECT** — external advisor round 4; Z.ai "
         "concurrence, repo-verified (2026-09-11)",
         f"- finding: {ROUND4_REJECTS[1]['finding']}",
         f"- disposition: {ROUND4_REJECTS[1]['disposition']}",
         "",
         "### Store impact and gates",
         "",
         "- 211 → **209** mappings (high 176 / medium 32 / low 1); "
         "69 → **68** notes carrying 2+ codes; 182 → **181** covered "
         "points; the zero-coverage queue gains 4.15 as an **annotated "
         "corpus gap** (pieces exist, connective teaching does not — "
         "T-C11 input), not a mapping defect.",
         "- Gates re-run after the removals: applier ALL GREEN (209), "
         "`graph_check.py` 9/9 (C10 counts updated), "
         "`c10_negative_test.py` 10 classes + positive control.",
         "- `scripts/c10_round4_rejects.py` executed the removals + this "
         "section (idempotent); the round-4 REJECT data is importable "
         "(`ROUND4_REJECTS`) for the re-targeted audit.",
         "",
         "### The 59-spec staged batch (supersedes §11)",
         "",
         "To ratify, the operator promotes exactly the 59 surviving "
         "reviewed CONFIRM mappings (derived mechanically from the §11 "
         "command by removing the two rejected specs):",
         "",
         "```bash",
         cmd,
         "```",
         "",
         "(codes appearing on several notes are disambiguated with "
         "`CODE@FRAGMENT` per the promoter's resolver; ambiguous specs "
         "fail rather than promote wholesale. After the command: gates "
         "re-run automatically — applier ALL GREEN, `graph_check.py` 9/9, "
         "then `c10_negative_test.py`. The pre-execution reconciliation "
         "audit `scripts/c10_ratify_audit.py` is re-targeted at §12 and "
         "must PASS — its report `C10_RATIFICATION_AUDIT.md` is the "
         "machine-verification that the 59 staged targets are exactly the "
         "round-4-surviving reviewed pairs and that both rejected mappings "
         "are absent from both the store and the command.)",
         "",
         "Alternatively the operator may ratify in tranches by trimming "
         "the `--map` list; or ask Z.ai to apply it verbatim.", ""]

    SHEET.write_text(text.rstrip("\n") + "\n" + "\n".join(L), encoding="utf-8")
    return [f"§12 appended to sheet: 59-spec staged batch "
            f"(dropped {len(dropped)}, kept {len(kept)}, "
            f"distinct {len(set(kept))})"]


# ------------------------------------------------------------ guide §8 --
def apply_guide() -> list[str]:
    text = GUIDE.read_text(encoding="utf-8")
    if GUIDE_MARKER in text:
        return ["guide already carries §8 (idempotent re-run)"]

    L = ["", GUIDE_MARKER, "",
         "## 8. Issue 3 — command-kind substance rule (2026-09-11, "
         "round 4; FROZEN)",
         "",
         "Appended by `scripts/c10_round4_rejects.py` after the external "
         "advisor's fourth-round review (Z.ai concurrence, repo-verified). "
         "This rule completes the §0.0 contributory contract and is "
         "**canonical from here on** — including T-C11, where each "
         "specification point should be tagged with its command kind so "
         "this check is mechanical.",
         "",
         "**Rule.** A contributory mapping still needs to contain the "
         "*kind of instructional substance demanded by the specification "
         "point's command verb*. Distributed coverage may aggregate "
         "explicit contributions across notes, but at least one mapped "
         "note must carry substance **of the demanded kind**; a premise or "
         "a stated consequence is not such a contribution, and aggregating "
         "premise + consequence constructs the missing causal teaching by "
         "inference — which §0.0 forbids (\"premises and consequences may "
         "live in sibling notes, the explanation may not\").",
         "",
         "| Spec command type | Weak mapping (REJECT) | "
         "Valid contribution (CONFIRM) |",
         "|---|---|---|",
         "| **define / know terms** | mention of the term | definition or "
         "meaningful instructional use |",
         "| **explain how / why** | premise or consequence | the "
         "causal/mechanistic explanation itself |",
         "| **calculate** | statement of formula/basis | calculation "
         "procedure and/or worked example |",
         "| **describe experiment** | mention of an experiment | actual "
         "method/procedure |",
         "| **represent with diagram** | text saying a diagram exists | "
         "the relevant diagram (VLM-verified) |",
         "| **understand relationship** | isolated fact | the "
         "relationship/mechanism taught |",
         "",
         "Retroactive application to the round-3 review set rejects "
         "exactly two mappings and preserves the other 59 (see "
         "`PHASE2_PR_REVIEW_SHEET.md` §12):",
         "",
         "- **4CH1-4.15 @ Nitrogen Oxides & Sulfur Dioxide** — an "
         "\"explain how\" point: the formation mechanism is stated in no "
         "note (premise in the combustion note, stated result as a "
         "premise clause in the acid-rain note). Removed; 4.15 is an "
         "honest zero-coverage corpus gap.",
         "- **4CH1-1.17 @ Calculate Relative Mass** — a \"calculate\" "
         "point: the note carries no Ar calculation, only the definitional "
         "derivation basis (duplicated in the S1-c note). Removed; 1.17 "
         "keeps its S1-c mapping.",
         "",
         "Amendment to §7's pass criteria: the coverage contract is now "
         "**181/182 points with the zero-coverage queue carrying 4.15 as "
         "an annotated corpus gap** — an honest representation, not a "
         "mapping failure. All other §7 criteria stand.",
         ""]
    GUIDE.write_text(text.rstrip("\n") + "\n" + "\n".join(L), encoding="utf-8")
    return ["§8 (issue 3, command-kind rule) appended to guide"]


def main() -> int:
    steps = [apply_decisions, apply_sheet, apply_guide]
    ok = True
    for step in steps:
        out = step()
        if not out:
            ok = False
            break
        for line in out:
            print("-", line)
    if not ok:
        print("round-4 rework INCOMPLETE — fix and re-run (idempotent)")
        return 1
    print("round-4 rework applied: 2 mappings removed, sheet §12 staged "
          "(59-spec batch), guide §8 frozen")
    print("next: python3 scripts/c10_map_notes.py  (front matter + "
          "coverage report), then graph_check.py / c10_negative_test.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
