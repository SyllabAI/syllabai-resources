#!/usr/bin/env python3
"""
T-C10 rework (operator spot-check 2026-09-11, sheet entry #7) — REJECT
`Definition of combustion` -> 4CH1-4.15 and remap 4.15 onto the sibling
S4-b note that actually states the causal relationship.

Operator finding (recorded verbatim in the review record):
  4.15 requires explaining how combustion of sulfur IMPURITIES in
  hydrocarbon fuels produces sulfur dioxide. The combustion note only
  proves the impurity premise ("All these fuels contain carbon,
  hydrogen and small quantities of sulfur") and lists "oxides of
  sulfur" among combustion products without linking the two; the old
  rationale itself deferred formation detail to the acid-rain note.

Rework:
  REMOVE  4CH1-4.15 from `Definition of combustion - ...md`
          (note keeps 4.11 / 4.12 / 4.13 — >=1-mapping gate still satisfied)
  ADD     4CH1-4.15 on `Nitrogen Oxides & Sulfur Dioxide ... 2017.md`
          evidence (verbatim in that note, line "The sulfur dioxide
          produced from the combustion of fossil fuels dissolves in
          rainwater droplets to form sulfuric acid"): the causal
          fragment "The sulfur dioxide produced from the combustion
          of fossil fuels" — the 4.15 causal claim stated in-note.
          confidence: medium (the "impurities in hydrocarbon fuels"
          framing is contextual, not verbatim in this note; keeps it
          in the PR-review-first queue).

Idempotent: safe to re-run (no-op if the rework is already applied).
Output formatting matches the existing decisions files (indent=2,
compact mapping objects, trailing newline).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
S4 = HERE / "c10_decisions" / "S4.json"

COMB = ("Chemistry IGCSE Revision Notes/4. Organic Chemistry/b. Crude Oil/"
        "Definition of combustion - IGCSE Chemistry Revision Notes.md")
NOX = ("Chemistry IGCSE Revision Notes/4. Organic Chemistry/b. Crude Oil/"
       "Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry "
       "Revision Notes 2017.md")

NEW_415 = {
    "code": "4CH1-4.15",
    "confidence": "medium",
    "evidence": "The sulfur dioxide produced from the combustion of fossil fuels",
    "rationale": (
        "Remapped after the operator spot-check (2026-09-11) rejected the "
        "combustion-note mapping, whose evidence proved only the fuel-impurity "
        "premise. This note states the 4.15 causal relationship directly - "
        "combustion of fossil fuels producing sulfur dioxide - while the "
        "acid-rain consequences are carried separately by the 4.16 mapping."
    ),
}


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


def main() -> int:
    data = json.loads(S4.read_text(encoding="utf-8"))
    changed = []

    comb = data[COMB]["mappings"]
    before = len(comb)
    comb[:] = [m for m in comb if m["code"] != "4CH1-4.15"]
    if len(comb) != before:
        changed.append(f"removed 4CH1-4.15 from combustion note ({before} -> {len(comb)} mappings)")
    if not comb:
        print("FAIL: combustion note would have zero mappings")
        return 1

    nox = data[NOX]["mappings"]
    if any(m["code"] == "4CH1-4.15" for m in nox):
        changed.append("4.15 already present on NOx note (idempotent re-run)")
    else:
        nox.append(NEW_415)
        nox.sort(key=lambda m: float(m["code"].split("-")[1].rstrip("C")))
        changed.append(f"added 4CH1-4.15 to NOx note ({len(nox)} mappings)")

    S4.write_text(dump_decisions(data), encoding="utf-8")
    for c in changed:
        print("-", c)
    print("S4.json updated:", S4)
    return 0


if __name__ == "__main__":
    sys.exit(main())
