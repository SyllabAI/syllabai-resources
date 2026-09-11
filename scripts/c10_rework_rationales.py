#!/usr/bin/env python3
"""
T-C10 PR review rework (2026-09-11, AI review pass) — rewrite the rationales
of six confirmed mappings for honest contributory wording.

Why: the review confirmed all six mappings under the §0.0 mapping contract
(contributory many-to-many coverage), but five rationales used misleading
"deferral" phrasing ("the dedicated ... note carries ...", "lives in", "the
indicator note carries ...") that misframes the mapping as pointing
elsewhere instead of claiming its own contribution, and one (1.17 S1-e) was
imprecise about what the note contributes. The rationale is provenance
metadata describing the note's contribution; accuracy matters because the
next phases (T-C11 concept graph) consume these strings.

Scope — evidence, confidence, tier, validation state, mapping sets: ALL
UNCHANGED. Only the rationale text of the six mappings below. Note bodies
stay byte-identical (the applier regenerates front matter from decisions).

Idempotent: safe to re-run (no-op once applied).
Output formatting matches the existing decisions files (compact mapping
objects, indent 2, trailing newline) — same dump_decisions() as
c10_rework_415.py / c10_promote.py.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEC_DIR = HERE / "c10_decisions"

# (file, note-key, code) -> new rationale
REWORKS = {
    ("S4.json", "Chemistry IGCSE Revision Notes/4. Organic Chemistry/b. Crude Oil/"
        "Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry "
        "Revision Notes 2017.md", "4CH1-4.15"): (
        "Remapped after the operator spot-check (2026-09-11) rejected the "
        "combustion-note mapping, whose evidence proved only the fuel-impurity "
        "premise. The note's 'From sulfur dioxide' subsection teaches the 4.15 "
        "relationship in-note - combustion of fossil fuels producing sulfur "
        "dioxide - while the fuel-impurity premise (fuels containing small "
        "quantities of sulfur) is taught in the sibling combustion note of the "
        "same subsection, a legitimate distributed coverage under the mapping "
        "contract; the acid-rain consequences are carried by the 4.16 mapping."),
    ("S1.json", "Chemistry IGCSE Revision Notes/1. Principles of Chemistry/"
        "a. States of Matter/Solubility - IGCSE Chemistry Revision Notes.md",
        "4CH1-1.4"): (
        "Teaches the solvent term definitionally in context ('the liquid is "
        "called the solvent') and uses solute / saturated solution operationally "
        "in the solubility-curve discussion; the Solutions note carries the four "
        "1.4 term definitions as a separate mapping - contributory coverage, "
        "not sole coverage."),
    ("S1.json", "Chemistry IGCSE Revision Notes/1. Principles of Chemistry/"
        "c. Atomic Structure/Atoms Definitions & Structure  Edexcel IGCSE "
        "Chemistry Revision Notes 2017.md", "4CHI-1.16".replace("4CHI", "4CH1")): (
        "The terms table defines all four 1.16 terms - atomic number, mass "
        "number, isotope and relative atomic mass (the quoted Ar row, incl. the "
        "carbon-12 standard); the calculation of Ar from isotopic abundances is "
        "1.17's content in the dedicated RAM note."),
    ("S2.json", "Chemistry IGCSE Revision Notes/2. Inorganic Chemistry/"
        "f. Acids, Alkalis & Titrations/Acids, Alkalis & Neutralisation - "
        "IGCSE Revision Notes.md", "4CHI-2.29".replace("4CHI", "4CH1")): (
        "Introduces the pH scale itself - a numerical scale showing how acidic "
        "or alkaline a solution is, measuring the hydrogen ions present - the "
        "conceptual foundation of 2.29; the 0-14 classification bands are taught "
        "in the indicator note's 2.29 mapping."),
    ("S3.json", "Chemistry IGCSE Revision Notes/3. Physical Chemistry/"
        "b. Rates of Reaction/Explaining Rates  Edexcel IGCSE Chemistry "
        "Revision Notes 2017.md", "4CHI-3.10".replace("4CHI", "4CH1")): (
        "Collision-theory sections explaining the concentration, pressure, "
        "temperature and surface-area effects on rate; the catalyst factor of "
        "3.10 is taught in the rate-of-reaction and catalysts notes."),
    ("S1.json", "Chemistry IGCSE Revision Notes/1. Principles of Chemistry/"
        "e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  "
        "Edexcel IGCSE Chemistry Revision Notes 2017.md", "4CHI-1.17".replace("4CHI", "4CH1")): (
        "Cross-subsection contributory mapping: the note opens with the Ar "
        "derivation basis (Ar calculated from the mass number and relative "
        "abundances of all the isotopes) before moving to Mr; the 1.17 "
        "calculation skill - equation and worked examples - is carried by the "
        "dedicated relative-atomic-mass note in S1-c."),
}


def dump_decisions(data: dict) -> str:
    """Match the existing decisions-file style exactly (compact mapping
    objects on single lines, indent 2)."""
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


def main() -> int:
    changed_any = False
    for (fname, note_key, code), new_rationale in REWORKS.items():
        path = DEC_DIR / fname
        data = json.loads(path.read_text(encoding="utf-8"))
        if note_key not in data:
            print(f"FAIL: note key not in {fname}: {note_key!r}")
            return 1
        mapping = next((m for m in data[note_key]["mappings"] if m["code"] == code), None)
        if mapping is None:
            print(f"FAIL: {code} not mapped on note in {fname}")
            return 1
        if mapping["rationale"] == new_rationale:
            print(f"- {code} @ {note_key.split('/')[-1][:60]}: already reworked (idempotent)")
            continue
        old_ev, old_conf = mapping["evidence"], mapping["confidence"]
        mapping["rationale"] = new_rationale
        # hard invariants: only the rationale may change
        assert mapping["evidence"] == old_ev and mapping["confidence"] == old_conf
        assert "validation" not in mapping
        path.write_text(dump_decisions(data), encoding="utf-8")
        print(f"- {code} @ {note_key.split('/')[-1][:60]}: rationale reworked "
              f"({len(old_conf)} -> conf unchanged, evidence unchanged)")
        changed_any = True
    if changed_any:
        print("next: python3 scripts/c10_map_notes.py (gated re-apply; note "
              "front matter picks up the new rationales, bodies byte-identical)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
