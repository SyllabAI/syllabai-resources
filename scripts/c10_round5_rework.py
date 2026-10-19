#!/usr/bin/env python3
"""
T-C10 round-5 rework (2026-09-11) — apply the two rationale corrections
recorded (but deliberately not applied) by the round-5 exhaustive review.

Why: the round-5 review confirmed all 150 remaining mappings under the
frozen guide §0.0 contributory + §8 command-kind contract, but recorded two
rationale wording corrections in PHASE2_ROUND5_REVIEW_SHEET.md §7 /
C10_ROUND5_REVIEW.json `corrected_rationales`:

  R5-001 4CH1-1.1   overstatement repair  (rationale claimed an 'energy'
                                         column in the states table; the
                                         energy content is actually taught
                                         in the state-change prose)
  R5-016 4CH1-1.19  under-description repair (rationale omitted the
                                         position-to-configuration
                                         relationship section that carries
                                         the deduction-from-position skill)

The review protocol for CONFIRM verdicts retains the evidence quote exactly
and rewrites an inaccurate rationale; the store was left unchanged pending
operator approval. The operator has now approved the round-5 outcome
("Ratify the 59 and promote 150"), so this wording pass executes the two
recorded corrections verbatim from the machine record — nothing is invented
here: every corrected string is read from C10_ROUND5_REVIEW.json and must
match byte-for-byte.

Scope — evidence, confidence, tier, validation state, mapping sets: ALL
UNCHANGED. Only the rationale text of the two mappings below. Note bodies
stay byte-identical (the applier regenerates front matter from decisions).

Idempotent: safe to re-run (no-op once applied).
Output formatting matches the existing decisions files (compact mapping
objects, indent 2, trailing newline) — same dump_decisions() as
c10_promote.py / c10_rework_rationales.py.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEC_DIR = HERE / "c10_decisions"
REVIEW = HERE.parent / "graph" / "reports" / "C10_ROUND5_REVIEW.json"


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
    review = json.loads(REVIEW.read_text(encoding="utf-8"))
    corrections = review["corrected_rationales"]
    pairs = {p["idx"]: p for p in review["reviewed_pairs"]}
    if len(corrections) != 2:
        sys.exit(f"FAIL: expected exactly 2 round-5 corrections, got "
                 f"{len(corrections)}")

    # locate every correction target in the decisions store by exact
    # (note key, code) identity — no filename hardcoding
    targets = []
    for c in corrections:
        p = pairs.get(c["idx"])
        if p is None or p["code"] != c["code"]:
            sys.exit(f"FAIL: correction idx {c['idx']} does not match a "
                     f"reviewed pair code {c['code']!r}")
        if not p.get("rationale_correction"):
            sys.exit(f"FAIL: pair idx {c['idx']} carries no "
                     f"rationale_correction flag")
        targets.append((p["note"], p["code"], c["corrected_rationale"]))

    changed_any = False
    for note_key, code, new_rationale in targets:
        fname = None
        for f in sorted(DEC_DIR.glob("S*.json")):
            if note_key in json.loads(f.read_text(encoding="utf-8")):
                fname = f
                break
        if fname is None:
            sys.exit(f"FAIL: note key not found in any decision file: "
                     f"{note_key!r}")
        data = json.loads(fname.read_text(encoding="utf-8"))
        mapping = next((m for m in data[note_key]["mappings"]
                        if m["code"] == code), None)
        if mapping is None:
            sys.exit(f"FAIL: {code} not mapped on note in {fname.name}")
        if mapping["rationale"] == new_rationale:
            print(f"- {code} @ {Path(note_key).stem[:60]}: already "
                  f"reworked (idempotent)")
            continue
        old_ev, old_conf = mapping["evidence"], mapping["confidence"]
        old_val = mapping.get("validation")
        mapping["rationale"] = new_rationale
        # hard invariants: ONLY the rationale may change
        assert mapping["evidence"] == old_ev
        assert mapping["confidence"] == old_conf
        assert mapping.get("validation") == old_val
        fname.write_text(dump_decisions(data), encoding="utf-8")
        print(f"- {code} @ {Path(note_key).stem[:60]}: rationale corrected "
              f"(evidence + confidence + validation unchanged)")
        changed_any = True

    if changed_any:
        print("next: python3 scripts/c10_map_notes.py (gated re-apply; note "
              "front matter picks up the corrected rationales, note bodies "
              "byte-identical)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
