#!/usr/bin/env python3
"""
repair_c13_quotes.py — T-SPEC-1 task ②: author fresh verbatim section quotes
for the 12 c13 worklist mappings whose evidence resolves only to the note
title/excerpt region (worklist reason verbatim: "author a fresh verbatim
section quote").

Discipline:
- The NOTE-LEVEL mapping (code <-> note, HUMAN_VALIDATED by operator 2026-09-11)
  is NOT changed. Only the evidence quote is refined to a body-passage quote so
  the c13 substrate can anchor it to a content chunk (G4 re-verifies).
- Every new quote is verified, BEFORE writing, to be a normalized substring of
  exactly one non-intro chunk of ITS note, using the substrate's own
  chunk_note + norm (imported from scripts/c13_chunk_sp_substrate.py).
- Validation state fields are untouched (status/by/date preserved).
- --check-only verifies without writing.

Usage: python3 repair_c13_quotes.py [--check-only]
"""
import json
import re
import sys
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
sys.path.insert(0, str(BASE / "scripts"))
import c13_chunk_sp_substrate as c13  # noqa: E402

NOTES = BASE / "Chemistry IGCSE Revision Notes"

# (note relative path, spec code, new evidence quote — verbatim body text)
REPAIRS = [
    ("1. Principles of Chemistry/a. States of Matter/Changing states of matter - IGCSE Chemistry Revision Notes.md",
     "4CH1-1.1",
     "| Arrangement of particles | Regular arrangement | Randomly arranged | Randomly arranged | | Movement of particles | Vibrate about a fixed position | Move around each other | Move quickly in all directions |"),
    ("1. Principles of Chemistry/a. States of Matter/Changing states of matter - IGCSE Chemistry Revision Notes.md",
     "4CH1-1.2",
     "- Melting is when a solid changes into a liquid - Heat / thermal energy absorbed by the particles is transformed into kinetic energy - This causes the particles to vibrate more and start to move / flow - Melting happens at a specific temperature, known as the melting point (m.p.)"),
    ("1. Principles of Chemistry/d. The Periodic Table/Metals & non-metals in the Periodic Table - IGCSE Chemistry.md",
     "4CH1-1.20",
     "| Electrical conductivity | Good conductor of electricity | Poor conductors of electricity | | Type of oxide | Basic oxides | Acidic oxides (some are neutral) |"),
    ("1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md",
     "4CH1-1.28",
     "- Step 2 - use the molar ratio from the balanced symbol equation - 2 moles of magnesium produce 2 moles of magnesium oxide - The ratio is 1 : 1 - Therefore, 0.25 moles of magnesium oxide is produced - Step 3 - calculate the mass of magnesium oxide"),
    ("1. Principles of Chemistry/f. Ionic Bonding/Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md",
     "4CH1-1.41",
     "- Ionic compounds have high melting and boiling points because: - They have giant ionic lattices - There are strong electrostatic forces of attraction between oppositely charged ions in all directions - The forces need lots of thermal energy to overcome them"),
    ("1. Principles of Chemistry/f. Ionic Bonding/Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md",
     "4CH1-1.43",
     "- Ionic compounds are poor conductors in the solid state - The ions are in fixed positions in the lattice - They are therefore unable to move and carry a charge - Ionic compounds are good conductors of electricity in the molten state or in solution - When the ionic compound is melted or dissolved in water, the ions are able to move and carry a charge"),
    ("1. Principles of Chemistry/h. Metallic Bonding/Metallic bonding - IGCSE Chemistry Revision Notes.md",
     "4CH1-1.52C",
     "!Structure & bonding in a metal, IGCSE & GCSE Chemistry revision notes Metallic bonds exist between positive metal ions and delocalised electrons - Most metals have high melting and boiling points"),
    ("1. Principles of Chemistry/h. Metallic Bonding/Metallic bonding - IGCSE Chemistry Revision Notes.md",
     "4CH1-1.53C",
     "- There are strong electrostatic forces of attraction between the positive metal ions and the negative delocalised electrons within the metal lattice structure - These needs lots of energy to be broken"),
    ("2. Inorganic Chemistry/d. Reactivity Series/Metal displacement - IGCSE Chemistry Revision Notes.md",
     "4CH1-2.16",
     "- The reactivity between two metals can be compared using displacement reactions in salt solutions of one of the metals - This is easily seen as the more reactive metal slowly disappears from the solution, displacing the less reactive metal"),
    ("2. Inorganic Chemistry/d. Reactivity Series/Metals Reacting with Water & Acids  Edexcel IGCSE Chemistry Revision Notes 2017.md",
     "4CH1-2.15",
     "- Only metals above hydrogen in the reactivity series will react with dilute acids - The more reactive the metal then the more vigorous the reaction will be"),
    ("2. Inorganic Chemistry/d. Reactivity Series/Metals Reacting with Water & Acids  Edexcel IGCSE Chemistry Revision Notes 2017.md",
     "4CH1-2.17",
     "| Potassium | Reacts violently | | Sodium | Reacts quickly | | Lithium | Reacts less strongly | | Calcium | Reacts less strongly |"),
    ("2. Inorganic Chemistry/e. Extraction & Uses of Metals/Metals and their uses - IGCSE Chemistry Revision Notes.md",
     "4CH1-2.25C",
     "| Aircraft bodies | High strength-to-weight ratio (low density) | | Saucepans | Very good conductor of heat and unreactive | | Overhead electrical cables | Very good conductor of electricity | | Food cans | Non-toxic, resistant to corrosion and resistant to acidic food stuffs |"),
]


def chunks_of(note_path: Path):
    text = note_path.read_text(encoding="utf-8")
    _, body = c13.front_matter_split(text)
    return c13.chunk_note(body), text


def anchor_chunk(note_path: Path, quote: str):
    """Return (ok, detail): quote must be a normalized substring of exactly one
    non-intro chunk of the note."""
    chunks, _ = chunks_of(note_path)
    nq = c13.norm(quote)
    hits = []
    for ch in chunks:
        if ch.get("is_intro"):
            continue
        if nq and nq in c13.norm(ch["text"]):
            hits.append(ch.get("heading") or f"chunk{ch.get('index')}")
    return (len(hits) == 1, ", ".join(hits) if hits else
            ("no anchor" if not hits else f"ambiguous: {hits}"))


def old_evidence_unanchored(note_path: Path, old: str):
    chunks, _ = chunks_of(note_path)
    nq = c13.norm(old)
    for ch in chunks:
        if ch.get("is_intro"):
            continue
        if nq and nq in c13.norm(ch["text"]):
            return False  # actually anchors to a body chunk — leave alone
    return True


def yaml_dquote(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def replace_evidence(raw: str, code: str, new_quote: str):
    """Replace the evidence scalar inside the `  - code: <code>` block of the
    frontmatter. The block runs until the next `  - code:` or end of
    frontmatter. evidence spans until the next key at the same indent."""
    fm_end = raw.index("\n---", 3)
    fm = raw[:fm_end]
    m = re.search(r"(?ms)^  - code: " + re.escape(code) + r"\n(.*?)(?=^  - code: |\Z)", fm)
    if not m:
        raise SystemExit(f"code block not found in frontmatter: {code}")
    block = m.group(0)
    new_block, n = re.subn(
        r"(?ms)^      evidence: .*?(?=^      \w)",
        "      evidence: " + yaml_dquote(new_quote) + "\n",
        block, count=1)
    if n != 1:
        raise SystemExit(f"evidence span not replaced for {code}")
    return raw.replace(block, new_block, 1)


def main():
    check_only = "--check-only" in sys.argv
    failures = []
    for rel, code, quote in REPAIRS:
        np = NOTES / rel
        if not np.exists():
            failures.append((code, f"note missing: {rel}"))
            continue
        ok, detail = anchor_chunk(np, quote)
        fm = c13.front_matter_split(np.read_text(encoding="utf-8"))[0]
        m = re.search(r"(?ms)^  - code: " + re.escape(code) +
                      r"\n(.*?)(?=^  - code: |\Z)", fm)
        old_ev = re.search(r"(?ms)^      evidence: (.*?)(?=^      \w)", m.group(0)) if m else None
        old = old_ev.group(1) if old_ev else "?"
        status = "ANCHOR-OK" if ok else "ANCHOR-FAIL"
        print(f"[{status}] {code} -> {detail}")
        if not ok:
            failures.append((code, detail))
    if failures:
        print(f"\n{len(failures)} failure(s) — adjust quotes")
        for c, d in failures:
            print(" ", c, d)
        return 1
    if check_only:
        print("\nall 12 quotes anchor to exactly one non-intro chunk (check-only)")
        return 0

    # apply
    import yaml  # local validation of edited frontmatter
    for rel, code, quote in REPAIRS:
        np = NOTES / rel
        raw = np.read_text(encoding="utf-8")
        before = yaml.safe_load(c13.front_matter_split(raw)[0])
        entry_before = next(p for p in
                            before["spec_map"]["spec_points"] if p["code"] == code)
        raw2 = replace_evidence(raw, code, quote)
        after = yaml.safe_load(c13.front_matter_split(raw2)[0])
        entry_after = next(p for p in
                           after["spec_map"]["spec_points"] if p["code"] == code)
        assert entry_after["provenance"]["evidence"] == quote, code
        # every other field preserved verbatim
        eb, ea = dict(entry_before["provenance"]), dict(entry_after["provenance"])
        assert eb.pop("evidence") != ea.pop("evidence") or True
        eb["evidence"], ea["evidence"] = None, None
        assert eb == ea, f"provenance drift for {code}"
        assert entry_before["code"] == entry_after["code"]
        assert raw2.count("\n---") >= 1
        np.write_text(raw2, encoding="utf-8")
        print(f"written: {code} ({rel[:60]}...)")
    print("\nall 12 evidence quotes repaired; validation fields untouched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
