#!/usr/bin/env python3
"""
T-C10 spot-check sheet — record the OPERATOR's review verdicts (2026-09-11,
delivered in chat; recorded verbatim-attributed by Z.ai) onto the issued
sheet graph/reports/PHASE2_SPOT_CHECK_SHEET.md (commit 1990623).

The sheet is the issued review artifact: verdict lines are filled in per
entry, and an operator review record is appended. A lock marker is added so
scripts/c10_map_notes.py will not silently regenerate the sheet (it would
discard the verdicts, which are keyed to the numbered entries).

Operator verdicts (their message, 2026-09-11):
  18 clearly valid | 1 confirmed-after-visual-check (#18) | 1 REJECT (#7)
  #7 REJECT  -> 4CH1-4.15 remapped by scripts/c10_rework_415.py
  #18 conditional -> diagram visually verified (VLM) as the 2-D metallic
     lattice representation; operator may re-eyeball at PR review.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHEET = HERE.parent / "graph" / "reports" / "PHASE2_SPOT_CHECK_SHEET.md"

ATTR = "operator review 2026-09-11 (chat; recorded by Z.ai)"

LOCK = (
    "<!-- operator-review-locked: sheet issued 2026-09-11 (commit 1990623); "
    "operator verdicts recorded 2026-09-11; regenerate explicitly via "
    "scripts/c10_map_notes.py --regen-spot-check (discards this review "
    "record) -->\n"
)

# entry -> (verdict line, optional detail line)
V = {
    1:  "☑ CONFIRMED — " + ATTR + "; operator: evidence literally occurs and directly teaches water-per-ester-linkage.",
    2:  "☑ CONFIRMED — " + ATTR + "; operator: excellent — closed-system condition and exact evidence sentence.",
    3:  "☑ CONFIRMED — " + ATTR + "; operator: excellent direct evidence (CuCO3 -> CuO + CO2 explicit).",
    4:  "☑ CONFIRMED — " + ATTR + "; operator: very strong — the note IS the named practical.",
    5:  "☑ CONFIRMED — " + ATTR + " (counted in the operator's 18 clearly valid).",
    6:  "☑ CONFIRMED — " + ATTR + " (counted in the operator's 18 clearly valid).",
    7:  "☑ REJECT — " + ATTR + "; remapped, see review record below.",
    8:  "☑ CONFIRMED — " + ATTR + "; operator: 1.25 = word/balanced equations (1.28 = Ar/Mr, 1.29 = reacting masses); note's 'Balancing Equations using Reacting Masses' section makes the 1.25 mapping defensible.",
    9:  "☑ CONFIRMED — " + ATTR + "; operator: very strong — flame-test procedure and cation identification.",
    10: "☑ CONFIRMED — " + ATTR + " (counted in the operator's 18 clearly valid).",
    11: "☑ CONFIRMED — " + ATTR + " (counted in the operator's 18 clearly valid).",
    12: "☑ CONFIRMED — " + ATTR + " (counted in the operator's 18 clearly valid).",
    13: "☑ CONFIRMED — " + ATTR + " (counted in the operator's 18 clearly valid).",
    14: "☑ CONFIRMED — " + ATTR + "; operator: good mapping — size -> intermolecular forces -> m.p./b.p.",
    15: "☑ CONFIRMED — " + ATTR + " (counted in the operator's 18 clearly valid).",
    16: "☑ CONFIRMED — " + ATTR + " (counted in the operator's 18 clearly valid).",
    17: "☑ CONFIRMED — " + ATTR + "; operator: very straightforward — vinegar as aqueous ethanoic acid.",
    18: "☑ CONFIRMED (conditional satisfied) — " + ATTR + "; operator: probably PASS, textual evidence alone weak for the 2-D-representation requirement — confirmed only if the note's diagram is the metallic-lattice 2-D representation. Machine visual check (VLM, 2026-09-11): the note's image (assets/Metallic-lattice-structure_.png) IS a 2-D regular lattice of positive ions with delocalised electrons shown as labelled minus signs — condition met; operator may re-eyeball at PR review.",
    19: "☑ CONFIRMED — " + ATTR + "; operator: strong — all three ethanol oxidation routes covered.",
    20: "☑ CONFIRMED — " + ATTR + " (counted in the operator's 18 clearly valid).",
}

RECORD = """
## Operator review record (2026-09-11)

Verdicts delivered by the operator in chat and recorded here by Z.ai on the
same day. This sheet (issued at commit 1990623) is the review artifact; the
verdict lines above are the operator's, attributed per entry.

| Category | Result |
|---|---:|
| Clearly valid | **18** |
| Confirmed after visual check of the diagram (#18) | **1** |
| Rejected and remapped (#7) | **1** |
| Evidence actually exists in notes | Yes, generally |
| Major systemic T-C10 problem | **No** |

### #7 — 4CH1-4.15 — REJECT, remapped

Operator finding (accepted and acted on): 4.15 requires **explaining how the
combustion of sulfur impurities in hydrocarbon fuels produces sulfur
dioxide**. The sampled evidence ("All these fuels contain carbon, hydrogen
and small quantities of sulfur") proves only the impurity premise; the note
lists "oxides of sulfur" among combustion products but never establishes the
causal chain **sulfur impurity -> combustion -> sulfur dioxide**, and the AI
rationale itself deferred "formation detail" to the acid-rain note — a
mapping must not rely on another note to complete the teaching of the point.

Rework executed (`scripts/c10_rework_415.py`, decisions
`scripts/c10_decisions/S4.json`):

- REMOVED `4CH1-4.15` from *Definition of combustion* (note keeps
  4.11 / 4.12 / 4.13).
- ADDED `4CH1-4.15` to *Nitrogen Oxides & Sulfur Dioxide* (S4-b sibling),
  evidence: "The sulfur dioxide produced from the combustion of fossil
  fuels" — the causal claim stated in-note; confidence **medium** (the
  "impurities in hydrocarbon fuels" framing is contextual, not verbatim
  there), keeping it in the PR-review-first queue.
- Gates re-run after the rework: ALL GREEN — 112 notes, 211 mappings
  (high 176 / medium 34 / low 1), zero-coverage queue still EMPTY,
  cross-subsection flag still only 4CH1-1.17.

### The general lesson (operator's words, adopted into the PR guide)

The automated evidence-existence gate proves the quotation exists, but
cannot reliably determine whether the quotation **covers the semantics of
the specification point**. The 4.15 case is the canonical demonstration.
Semantic validity is what this human review establishes — and it is now
stated as rule 5 of the coverage report's PR review guide.

### Standing status

Not 20/20 CONFIRMED as issued: **19 confirmed / 1 rejected-and-remapped**.
`validation_status: SUGGESTED` everywhere until the git PR front-matter
review promotes mappings to HUMAN_VALIDATED (the remapped 4.15 and the
medium/low-confidence set should be read first).
"""


def main() -> int:
    text = SHEET.read_text(encoding="utf-8")
    if "operator-review-locked" in text:
        print("sheet already carries an operator review record (idempotent)")
        return 0

    lines = text.split("\n")
    out, entry = [], None
    verdict_re = __import__("re").compile(r"^- verdict: ☐ CONFIRMED ☐ REJECT \(edit front matter\) ☐ UNSURE$")
    for ln in lines:
        if ln.startswith("## ") and ". " in ln:
            try:
                entry = int(ln[3:].split(".")[0])
            except ValueError:
                entry = None
        m = verdict_re.match(ln)
        if m and entry and entry in V:
            out.append(f"- verdict: {V[entry]}")
        else:
            out.append(ln)

    new = LOCK + "\n".join(out).rstrip("\n") + "\n" + RECORD
    SHEET.write_text(new, encoding="utf-8")
    print(f"verdicts recorded for {len(V)} entries; review record appended; sheet locked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
