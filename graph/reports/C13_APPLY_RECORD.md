# C13 apply record — operator promotion EXECUTED

- Apply: `scripts/c13_apply_promotion.py@1.0.0` at resources `a091f9d379`; gate `88dc8dd6a3`
- Gate: Part A 42/42 CONFIRM (100% >= 90%); Part B 13/13 decided (12 AUTHOR + 1 DEFER) — **PASSES**
- Reproduction proof: substrate tool re-run **byte-identical** to the input store
- Re-verification: all 209 anchored rows G4-verified mechanically at apply time
- Promoted: 209 anchored rows SUGGESTED→HUMAN_VALIDATED (+1 reified supplementary) = 210 HUMAN_VALIDATED anchored rows; worklist gap row (4CH1-4.15) stays SUGGESTED

## Supplementary anchors reified

- `4CH1-3.3` @ ordinal 3 of `3. Physical Chemistry/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md` (same upstream quote mechanically verified; reviewer-recommended)

## Supplementary recommendations DEFERRED (not invented here)

- `4CH1-3.3` @ ordinals [1, 3] of `3. Physical Chemistry/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md` — ordinal equals the primary row
- `4CH1-1.50` @ ordinals [5, 9] of `1. Principles of Chemistry/g. Covalent Bonding/Giant covalent structures - IGCSE Chemistry Revision Notes.md` — upstream quote does not anchor in the recommended chunk (operator quote authoring required; not invented here)
- `4CH1-1.50` @ ordinals [5, 9] of `1. Principles of Chemistry/g. Covalent Bonding/Giant covalent structures - IGCSE Chemistry Revision Notes.md` — upstream quote does not anchor in the recommended chunk (operator quote authoring required; not invented here)
- `4CH1-1.5C` @ ordinals [5] of `1. Principles of Chemistry/a. States of Matter/Investigating solubility - IGCSE Chemistry Revision Notes.md` — upstream quote does not anchor in the recommended chunk (operator quote authoring required; not invented here)

## Remaining for the §8(d) spec-resolution axis

- T-C06 notes ingestion (documents/document_chunks for the SME notes corpus)
- benchmark snapshot v2 (snap-002) over the promoted store — §8(d) becomes SCOREABLE
