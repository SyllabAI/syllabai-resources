# T-C11 Operator Review Package — Session 43 (2026-09-12)

Built read-only from the decision record and live store at resources `3b70dde` / syllabai `6d36fb0` (both fast-forwarded from the Session-41 clones before any work — T-C12 had advanced). Machine record: `graph/reports/C11_REVIEW_PACKAGE.json`. Verdict template (operator-owned): `scripts/c11_review_verdicts.yaml`.

**This package carries NO promotion authority and NO §16 authorization.**

> Do not promote anything. Do not modify the authoritative graph. Do not
> open §16. Do not begin S1-remainder/S2/S3/S4 expansion.

Nothing was promoted; `graph/*.yaml` are byte-untouched; the promotions record remains at zero entries. The concept alias under audit below was NOT modified — its disposition is the operator's.

---

## 0. Tasking record

Operator tasking (session 43): the C11 audit + review-preparation round with **no promotion authority and no §16 authorization**. Required contents: (1) 31 individual edge dossiers; (2) 29 individual concept dossiers; (3) a 13-entry held/rejected appendix incl. HELD-13, HOLD vs REJECT distinguished, all existing decisions preserved, no reopening; (4) OD-1/OD-2 ratification slots marked PENDING, provenance unchanged; (5) machine pre-triage FC-1..FC-4 / likely-safe / likely-ambiguous; (6) the `maximum yield` alias audit with the phantom `aximum yield` report text corrected but the concept alias untouched; (7) a quantified review reduction; (8) batch-forecast instrumentation. Operational directive: reconcile to the current remote HEAD first (done — §0.1).

### 0.1 Reconciliation record

| repo | session-41 clone | reconciled HEAD | mode | what moved |
|---|---|---|---|---|
| resources | `4ac4a82` | `3b70dde` | ff-only, tree clean | RAG corpus guidance doc + 2 Google-Drive-sync CI commits; `graph/` and C11 scripts untouched |
| syllabai (tracker) | `6ef49f2` | `6d36fb0` | ff-only, tree clean | session-42 T-C12 record (P0 closed + P1 IAL placement; 2 baseline ratification flags — pastpapers corpus, out of scope here), ADR-020, RAG research, dashboard/Drive CI |

All four gates re-verified green at the reconciled HEAD before authoring (graph_check ALL PASS 29/65/0-HV; negative 14/14; task4 variants 3/3; promote 27/27). Every evidence quote was additionally re-verified independently under the T-C10 norm() by this package's builder: 78/78 byte-true.

## 1. How to use this package

- **Verdict vocabulary** (edges & nodes): `CONFIRM / REJECT / HOLD / MERGE / SPLIT`. MERGE and SPLIT are operator-only identity decisions.
- **Where to record**: `scripts/c11_review_verdicts.yaml` (operator-owned template rendered with this package). Hand-edits there are the sanctioned pathway; hand-edits to `graph/*.yaml` are silently reverted by the generator.
- **Application**: the next session applies verdicts via the §18 promotion pathway (`scripts/c11_promote.py`, exact identities only) and §7 decision-record re-authoring for REJECT/MERGE/SPLIT — the HELD-13 precedent.
- **Reading order for minimum effort**: §2 summary → §6 OD slots → the two PENDING presentations (C11_OPERATOR_DECISIONS.md §2) → §7 alias audit → bulk-confirm §3/§4 groups → spot-read dossiers as desired.

## 2. Executive surface

| surface | count | pre-triage split |
|---|---|---|
| edge dossiers (§3) | 31 | 26 likely-safe · 2 FC-3 (OD-1-linked) · 1 ambiguous · 2 PENDING |
| concept dossiers (§4) | 29 | 27 likely-safe · 2 FC-2 identity (OD-1-linked) |
| held/rejected appendix (§5) | 13 | 11 HELD + 2 REJECTED — decisions preserved, no reopening |
| OD ratification slots (§6) | 2 | both PENDING OPERATOR RATIFICATION |
| alias audit (§7) | 47 aliases | 25 verbatim · 4 variant · 18 unevidenced — 1 special case (`maximum yield`) |

**Review reduction (headline):** the 60 per-row verdicts collapse to **~7 actual decisions** — OD-1, OD-2, the two PENDING judgments, one granularity edge, the alias policy, and the `maximum yield` disposition — plus bulk CONFIRM/REJECT commands over the pre-triaged groups. See §8 for the quantification and §9 for the forecast instrumentation.

---

## 3. Edge dossiers (31 SUGGESTED authored edges awaiting per-row verdicts)

Order = decision-record order. The REVIEW_REQUIRED operator-HOLD edge (`CON-GAS-VOL-CALC REQUIRES_PREREQUISITE CON-AVOGADRO-LAW`) is NOT in this list — it already carries an operator verdict (HOLD, stays in the graph, not promotable; see §5 legend). The two PENDING-gated edges are **E-26 and E-29** and reference their existing 10-field presentations.

### E-01 — 4CH1-CON-MOLE-MASS-CONV REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-MASS

| field | value |
|---|---|
| exact triple | `4CH1-CON-MOLE-MASS-CONV` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MOLAR-MASS` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculating moles and mass - IGCSE Chemistry Revision Notes.md` — "The mass is calculated by moles x molar mass" |
| evidence admissibility | ADMISSIBLE — explicit definition sentence (byte-verified) |
| rationale (pass-1) | The conversion formula (mass = moles x molar mass and rearrangements) contains the molar mass; the mapped note teaches molar mass first, then the conversion. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-01 |

### E-02 — 4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLE

| field | value |
|---|---|
| exact triple | `4CH1-CON-MOLAR-MASS` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MOLE` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculating moles and mass - IGCSE Chemistry Revision Notes.md` — "The mass of 1 mole of a substance is known as the molar mass" |
| evidence admissibility | ADMISSIBLE — explicit definition sentence (byte-verified) |
| rationale (pass-1) | Molar mass is defined per mole ("the mass of 1 mole"); the definition presupposes the mole concept. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-02 |

### E-03 — 4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-MR

| field | value |
|---|---|
| exact triple | `4CH1-CON-MOLAR-MASS` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MR` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculating moles and mass - IGCSE Chemistry Revision Notes.md` — "For a compound, it is the same as the relative molecular or formula mass in grams" |
| evidence admissibility | ADMISSIBLE — explicit definition sentence (byte-verified) |
| rationale (pass-1) | Molar mass of a compound is defined numerically as its Mr in grams; the mapped note links them explicitly and uses Mr in every compound worked example. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-03 |

### E-04 — 4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-AR

| field | value |
|---|---|
| exact triple | `4CH1-CON-MOLAR-MASS` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-AR` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculating moles and mass - IGCSE Chemistry Revision Notes.md` — "For an element, it is the same as the relative atomic mass written in grams" |
| evidence admissibility | ADMISSIBLE — explicit definition sentence (byte-verified) |
| rationale (pass-1) | Molar mass of an element is defined as its Ar in grams; the mapped note links them explicitly (Na/He/Li examples). |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE (transitively-reachable; §19 semantic-distinctness precedent — pass-2 addressed the pair)** — FC-3 machine-flag (informational): target transitively reachable via other RP edges — §19: reachable ≠ redundant; per-edge semantic judgment |
| pass-2 verdict | CONFIRM_WITH_NOTE — "Both Ar and Mr edges are real (element vs compound definitions are adjacent bullets); not double-counting." |
| recommendation | CONFIRM — bulk-eligible; the reachability machine-flag is the §19 MOLAR-MASS→{MR, AR} precedent (reachable ≠ redundant: element vs compound definitions) and pass-2 explicitly dismissed double-counting |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-04 |

### E-05 — 4CH1-CON-MR REQUIRES_PREREQUISITE 4CH1-CON-AR

| field | value |
|---|---|
| exact triple | `4CH1-CON-MR` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-AR` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md` — "To calculate the Mr of a substance, you have to add up the relative atomic masses of all the atoms present in the formula" |
| evidence admissibility | ADMISSIBLE — explicit definition sentence (byte-verified) |
| rationale (pass-1) | Mr is computed BY summing Ar values (the 1.26 demand itself); every worked example in the mapped note takes Ar values as inputs without re-deriving them. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-05 |

### E-06 — 4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLE-MASS-CONV

| field | value |
|---|---|
| exact triple | `4CH1-CON-REACTING-MASS` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MOLE-MASS-CONV` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Reacting mass calculations - IGCSE Chemistry Revision Notes.md` — "Step 1 - calculate the moles of magnesium" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | Every worked example opens with moles = mass/Mr as a given step; the mole-mass conversion is never re-taught in this note (it is the 1.28 note's job). |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-06 |

### E-07 — 4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-RATIO

| field | value |
|---|---|
| exact triple | `4CH1-CON-REACTING-MASS` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MOLAR-RATIO` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Reacting mass calculations - IGCSE Chemistry Revision Notes.md` — "Step 2 - use the molar ratio from the balanced symbol equation" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | Step 2 of the three-step procedure uses the molar ratio as a given; the ratio concept is exercised, not taught, here. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-07 |

### E-08 — 4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-EQ-SYMBOL

| field | value |
|---|---|
| exact triple | `4CH1-CON-REACTING-MASS` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-EQ-SYMBOL` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Reacting mass calculations - IGCSE Chemistry Revision Notes.md` — "Then, the ratio between the substances is identified using the balanced chemical equation" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | The procedure presupposes the ability to read a balanced equation (provided ready-made in both worked examples); equation writing/balancing is the 1.25 note's job. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_AMBIGUOUS (granularity note)** — granularity: pass-2 FP-3 note |
| pass-2 verdict | CONFIRM_WITH_NOTE — "Granularity note: the operative dependency is on *interpreting* a given balanced equation; CON-EQ-SYMBOL also covers writing/balancing. Right at the available concept granularity; note for expansion." |
| recommendation | CONFIRM likely (high confidence, pass-2 concordant; the granularity point is an expansion-round concern) — or HOLD if an interpret-equations concept should be minted first |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-08 |

### E-09 — 4CH1-CON-PERCENT-YIELD REQUIRES_PREREQUISITE 4CH1-CON-THEOR-YIELD

| field | value |
|---|---|
| exact triple | `4CH1-CON-PERCENT-YIELD` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-THEOR-YIELD` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculate percentage yield - IGCSE Chemistry Revision Notes.md` — "The percentage yield compares the actual yield to the theoretical yield" |
| evidence admissibility | ADMISSIBLE — explicit definition sentence (byte-verified) |
| rationale (pass-1) | The denominator object of the 1.30 formula; the comparison is meaningless without the theoretical-yield concept. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **FC-3 (OD-1-linked)** — FC-3: same-anchor operand pair (OD-1-linked; vanishes under merge) |
| pass-2 verdict | CONFIRM_WITH_NOTE — "Split artifact: if the yield nodes are merged, this edge disappears. CONFIRM at current granularity." |
| recommendation | CONFIRM jointly with the OD-1 ratification — the pair mirrors the formula's operand structure and vanishes under an operator merge; do not confirm individually before ruling OD-1 |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-09 |

### E-10 — 4CH1-CON-PERCENT-YIELD REQUIRES_PREREQUISITE 4CH1-CON-YIELD

| field | value |
|---|---|
| exact triple | `4CH1-CON-PERCENT-YIELD` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-YIELD` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculate percentage yield - IGCSE Chemistry Revision Notes.md` — "The percentage yield compares the actual yield to the theoretical yield" |
| evidence admissibility | ADMISSIBLE — explicit definition sentence (byte-verified) |
| rationale (pass-1) | The numerator object of the 1.30 formula. Same anchor quote as the THEOR-YIELD edge — both components of the one taught comparison; review may merge these two edges with the numerator/denominator pair if the split is judged too fine. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **FC-3 (OD-1-linked)** — FC-3: same-anchor operand pair (OD-1-linked; vanishes under merge) |
| pass-2 verdict | CONFIRM_WITH_NOTE — "Split artifact (same anchor quote as the THEOR-YIELD edge): both components of the one taught comparison. Merge candidate alongside the node merges." |
| recommendation | CONFIRM jointly with the OD-1 ratification — the pair mirrors the formula's operand structure and vanishes under an operator merge; do not confirm individually before ruling OD-1 |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-10 |

### E-11 — 4CH1-CON-THEOR-YIELD REQUIRES_PREREQUISITE 4CH1-CON-REACTING-MASS

| field | value |
|---|---|
| exact triple | `4CH1-CON-THEOR-YIELD` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-REACTING-MASS` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculate percentage yield - IGCSE Chemistry Revision Notes.md` — "It is calculated from the balanced equation and the reacting masses" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | The note states the theoretical yield's derivation basis (balanced equation + reacting masses) as a given — cross-SP dependency 1.30 -> 1.29; the reacting-mass procedure is not re-taught here. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-11 |

### E-12 — 4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA

| field | value |
|---|---|
| exact triple | `4CH1-CON-EMP-MOL-CALC` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-EMPIRICAL-FORMULA` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md` — "Write the final empirical formula" |
| evidence admissibility | ADMISSIBLE — explicit definition sentence (byte-verified) |
| rationale (pass-1) | The procedure's step 6 outputs an empirical formula; steps 5-6 operate on the simplest-whole-number-ratio definition taught in the same note's definition section (and demanded by 1.32). |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-12 |

### E-13 — 4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE

| field | value |
|---|---|
| exact triple | `4CH1-CON-EMP-MOL-CALC` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MOLE` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md` — "Calculate the moles of each element" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | Procedure step 4 instructs "Calculate the moles of each element" without the note ever defining the mole (the 1.27 note's job) — textbook use-without-reteaching. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-13 |

### E-14 — 4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AR

| field | value |
|---|---|
| exact triple | `4CH1-CON-EMP-MOL-CALC` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-AR` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md` — "Write the relative atomic mass of each element" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | Procedure step 3 uses Ar values as given inputs; where Ar values come from is never taught in this note (the 1.26/periodic-table territory). |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-14 |

### E-15 — 4CH1-CON-MOLECULAR-FORMULA REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA

| field | value |
|---|---|
| exact triple | `4CH1-CON-MOLECULAR-FORMULA` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-EMPIRICAL-FORMULA` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md` — "Find the relative formula mass of the empirical formula" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | The molecular-formula derivation procedure (note step 1-3) takes the empirical formula as its input and scales it; the taught relationship table (methane/ethane/ethene/benzene) presupposes both concepts. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-15 |

### E-16 — 4CH1-CON-MOLECULAR-FORMULA REQUIRES_PREREQUISITE 4CH1-CON-MR

| field | value |
|---|---|
| exact triple | `4CH1-CON-MOLECULAR-FORMULA` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MR` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md` — "Add the relative atomic masses of all the atoms in the empirical formula" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | The scaling factor is Mr(molecular)/Mr(empirical); both Mr computations are used as given skills (the 1.26 note's job). |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-16 |

### E-17 — 4CH1-CON-WATER-CRYST REQUIRES_PREREQUISITE 4CH1-CON-EMP-MOL-CALC

| field | value |
|---|---|
| exact triple | `4CH1-CON-WATER-CRYST` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-EMP-MOL-CALC` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md` — "The steps for empirical formula can be adapted for hydrated salt / water of crystallisation calculations" |
| evidence admissibility | ADMISSIBLE — explicit teaching sequence in the note |
| rationale (pass-1) | The note explicitly teaches the hydrated-salt determination as an ADAPTATION of the empirical-formula steps (same note, later section); the examiner tip reinforces: "it is an application of deducing empirical formulae". |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-17 |

### E-18 — 4CH1-CON-EXP-FORMULA-DEDUCTION REQUIRES_PREREQUISITE 4CH1-CON-MOLE

| field | value |
|---|---|
| exact triple | `4CH1-CON-EXP-FORMULA-DEDUCTION` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MOLE` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Simple compound formulae - IGCSE Chemistry Revision Notes.md` — "The principle is to use mass measurements before and after a reaction and then convert masses into moles" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | The deduction method's core move is mass -> moles; the note never defines the mole (the 1.27 note's job). |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-18 |

### E-19 — 4CH1-PR-03 REQUIRES_PREREQUISITE 4CH1-CON-EXP-FORMULA-DEDUCTION

| field | value |
|---|---|
| exact triple | `4CH1-PR-03` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-EXP-FORMULA-DEDUCTION` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Investigating metal oxide formulas - IGCSE Revision Notes.md` — "Divide each of the two masses by the relative atomic masses of the element" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | Practical->conceptual: both 1.36 practicals (MgO by combustion, CuO by reduction) perform exactly the mass-difference deduction method as their analysis step (Steps 1-3 of the Results sections), without re-teaching its principle. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-19 |

### E-20 — 4CH1-CON-CONC-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE

| field | value |
|---|---|
| exact triple | `4CH1-CON-CONC-CALC` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MOLE` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Solution concentration - IGCSE Chemistry Revision Notes.md` — "Calculate the amount of solute, in moles, present in 2.5 dm3 of a solution whose concentration is 0.2 mol / dm3" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | Every 1.34C formula instance computes an amount in moles; the mole is never defined in this note (the 1.27 note's job). |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-20 |

### E-21 — 4CH1-CON-CONC-CALC REQUIRES_PREREQUISITE 4CH1-CON-VOL-CONVERSION

| field | value |
|---|---|
| exact triple | `4CH1-CON-CONC-CALC` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-VOL-CONVERSION` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Solution concentration - IGCSE Chemistry Revision Notes.md` — "Remember: The volume needs to be in dm3" |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | The rule is stated once and then enforced as a Remember-warning in worked examples 2 and 3; the mark-scheme wrong-answer pattern (failing to divide by 1000) independently confirms this is the operative sub-skill where candidates fail. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-21 |

### E-22 — 4CH1-CON-MOLAR-GAS-VOL REQUIRES_PREREQUISITE 4CH1-CON-MOLE

| field | value |
|---|---|
| exact triple | `4CH1-CON-MOLAR-GAS-VOL` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MOLE` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md` — "At room temperature and pressure, the volume occupied by one mole of any gas was found to be 24 dm3 or 24,000 cm3" |
| evidence admissibility | ADMISSIBLE — explicit definition sentence (byte-verified) |
| rationale (pass-1) | The molar gas volume is defined per mole ("the volume occupied by one mole of any gas"); the definition presupposes the mole concept. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-22 |

### E-23 — 4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-GAS-VOL

| field | value |
|---|---|
| exact triple | `4CH1-CON-GAS-VOL-CALC` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MOLAR-GAS-VOL` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md` — "Volume = Moles x Molar Volume" |
| evidence admissibility | ADMISSIBLE — explicit definition sentence (byte-verified) |
| rationale (pass-1) | The calculation formula is stated in terms of the molar volume (both the dm3 and cm3 forms with their respective constants). |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-23 |

### E-24 — 4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE-MASS-CONV

| field | value |
|---|---|
| exact triple | `4CH1-CON-GAS-VOL-CALC` —**REQUIRES_PREREQUISITE**→ `4CH1-CON-MOLE-MASS-CONV` |
| relation class | REQUIRES_PREREQUISITE (25 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md` — "To answer these type of questions you must first convert grams to moles and then calculate the volume." |
| evidence admissibility | ADMISSIBLE — worked-example step using the concept without re-teaching it |
| rationale (pass-1) | Cross-SP dependency 1.35C -> 1.28: the mass-route gas questions explicitly chain grams -> moles -> volume with the mole-mass conversion used as a given. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-24 |

### E-25 — 4CH1-CON-EQ-SYMBOL EXPLAINED_BY 4CH1-CON-CONSERVATION-MASS

| field | value |
|---|---|
| exact triple | `4CH1-CON-EQ-SYMBOL` —**EXPLAINED_BY**→ `4CH1-CON-CONSERVATION-MASS` |
| relation class | EXPLAINED_BY (3 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Writing chemical equations - IGCSE Chemistry Revision Notes.md` — "The Law of Conservation of Mass enables us to balance chemical equations, since no atoms can be lost or created" |
| evidence admissibility | ADMISSIBLE — causal teaching in one source (confidence-capped where adjacency-grounded) |
| rationale (pass-1) | Single-anchor causal teaching: the one sentence teaches the explanatory link itself ("enables us to ... since ..."). This is the relation the 4.15 negative-control class forbids constructing from premise+consequence aggregation. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-25 |

### E-26 — 4CH1-CON-MOLAR-GAS-VOL EXPLAINED_BY 4CH1-CON-AVOGADRO-LAW

| field | value |
|---|---|
| exact triple | `4CH1-CON-MOLAR-GAS-VOL` —**EXPLAINED_BY**→ `4CH1-CON-AVOGADRO-LAW` |
| relation class | EXPLAINED_BY (3 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md` — "From the molar gas volume the following formula triangle can be derived" |
| evidence admissibility | ADMISSIBLE — causal teaching in one source (confidence-capped where adjacency-grounded) |
| rationale (pass-1) | The same note section teaches the law ("equal amounts of gases occupy the same volume of space") and then the molar volume and its formula triangle; the law grounds why one fixed volume per mole exists at given conditions. Medium confidence: the note presents the 24 dm3 value as measured ("was found to be") rather than derived from the law — the explanatory link is tight but not stated as a derivation. |
| confidence / status | medium / SUGGESTED — **operator_decision PENDING** |
| failure-class pre-triage | **FC-1+FC-2 (PENDING judgment)** — FC-1: medium confidence or implicit-evidence derivation; FC-2: relation-class concern (pass-2 / ambiguity note); PENDING: operator decision already presented (10-field), awaiting ruling |
| pass-2 verdict | CONFIRM_WITH_NOTE — "FP-concern finding: the anchored quote ("From the molar gas volume the following formula triangle can be derived") supports molar-volume->formula, not law->molar-volume; the law->molar-volume link is section order + semantics ("was found to be" is empirical phrasing). CONFIRM at confidence medium; the medium band already encodes this weakness." |
| recommendation | Decision already presented 10-field in C11_OPERATOR_DECISIONS.md §2 — recommendation there is HOLD; rule on the presentation, not on this row alone |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-26 |

### E-27 — 4CH1-CON-YIELD EXPLAINED_BY 4CH1-CON-YIELD-FACTORS

| field | value |
|---|---|
| exact triple | `4CH1-CON-YIELD` —**EXPLAINED_BY**→ `4CH1-CON-YIELD-FACTORS` |
| relation class | EXPLAINED_BY (3 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Calculate percentage yield - IGCSE Chemistry Revision Notes.md` — "In practice, you never get 100% yield in a chemical process for several reasons" |
| evidence admissibility | ADMISSIBLE — causal teaching in one source (confidence-capped where adjacency-grounded) |
| rationale (pass-1) | Single anchor teaches the explanation of the actual-yield shortfall (five enumerated causes: equipment residue, reversibility, separation/purification losses, side reactions, transfer losses) in the same section that defines the yields. |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-27 |

### E-28 — 4CH1-MIS-EQ-SUBSCRIPT MISCONCEPTION_OF 4CH1-CON-EQ-SYMBOL

| field | value |
|---|---|
| exact triple | `4CH1-MIS-EQ-SUBSCRIPT` —**MISCONCEPTION_OF**→ `4CH1-CON-EQ-SYMBOL` |
| relation class | MISCONCEPTION_OF (1 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Writing chemical equations - IGCSE Chemistry Revision Notes.md` — "A common mistake when balancing symbol equations is to add, change or remove small numbers in the chemical formula of a substance" |
| evidence admissibility | ADMISSIBLE — examiner tip explicitly documents the error and/or corrective |
| rationale (pass-1) | The misconception is ABOUT balancing symbol equations (the target concept); the tip names the mistake explicitly — evidence class per the frozen §8A.11 hierarchy ("explicit SME/examiner statements"). |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-28 |

### E-29 — 4CH1-MIS-EQ-SUBSCRIPT REMEDIATED_BY 4CH1-CON-CONSERVATION-MASS

| field | value |
|---|---|
| exact triple | `4CH1-MIS-EQ-SUBSCRIPT` —**REMEDIATED_BY**→ `4CH1-CON-CONSERVATION-MASS` |
| relation class | REMEDIATED_BY (2 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Writing chemical equations - IGCSE Chemistry Revision Notes.md` — "You cannot do this because it changes what the substance is" |
| evidence admissibility | ADMISSIBLE — examiner tip explicitly documents the error and/or corrective |
| rationale (pass-1) | The corrective content: balance with coefficients because atoms (not substances) are conserved. Medium confidence — the tip's own argument is substance-identity ("it changes what the substance is"); mapping the remediation to CON-CONSERVATION-MASS (vs. keeping the remediation note-local) is a judgment flagged for review. |
| confidence / status | medium / SUGGESTED — **operator_decision PENDING** |
| failure-class pre-triage | **FC-1+FC-2 (PENDING judgment)** — FC-1: medium confidence or implicit-evidence derivation; FC-2: relation-class concern (pass-2 / ambiguity note); PENDING: operator decision already presented (10-field), awaiting ruling |
| pass-2 verdict | CONFIRM_WITH_NOTE — "The tip itself argues substance identity ("it changes what the substance is"); conservation is the section grounding for coefficient-balancing. Alternative: mint a coefficients-vs-subscripts concept in expansion. CONFIRM at medium." |
| recommendation | Decision already presented 10-field in C11_OPERATOR_DECISIONS.md §2 — recommendation there is HOLD; rule on the presentation, not on this row alone |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-29 |

### E-30 — 4CH1-MIS-CONC-UNIT WRONG_ANSWER_PATTERN 4CH1-CON-CONC-CALC

| field | value |
|---|---|
| exact triple | `4CH1-MIS-CONC-UNIT` —**WRONG_ANSWER_PATTERN**→ `4CH1-CON-CONC-CALC` |
| relation class | WRONG_ANSWER_PATTERN (1 in the pilot graph incl. PART_OF) |
| source evidence | [MARK_SCHEME] `CFEC2_MS_P1.txt` — "an answer of 10(.0) for 1 mark (i.e. failing to divide by 1000)" |
| evidence admissibility | ADMISSIBLE — mark-scheme-documented wrong answer |
| rationale (pass-1) | The pattern manifests in concentration-calculation question contexts (MS Q4: 0.096/24 with (25 x 0.4)/1000 — an amount-from-concentration question); kept distinct from MISCONCEPTION_OF (no belief is documented — only the wrong answer and its cause). |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-30 |

### E-31 — 4CH1-MIS-CONC-UNIT REMEDIATED_BY 4CH1-CON-VOL-CONVERSION

| field | value |
|---|---|
| exact triple | `4CH1-MIS-CONC-UNIT` —**REMEDIATED_BY**→ `4CH1-CON-VOL-CONVERSION` |
| relation class | REMEDIATED_BY (2 in the pilot graph incl. PART_OF) |
| source evidence | [NOTE] `Solution concentration - IGCSE Chemistry Revision Notes.md` — "Don't forget your unit conversions" |
| evidence admissibility | ADMISSIBLE — examiner tip explicitly documents the error and/or corrective |
| rationale (pass-1) | The Examiner-Tips block of the 1.34C-mapped note is precisely the corrective content for the documented wrong answer ("To go from cm3 to dm3 : divide by 1000"). |
| confidence / status | high / SUGGESTED |
| failure-class pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (high confidence, explicit evidence class, pass-2 concordant, zero machine flags) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row E-31 |

---

## 4. Concept dossiers (29 nodes awaiting per-row verdicts)

### N-01 — `4CH1-CON-EQ-WORD` Word equation

| field | value |
|---|---|
| concept identity | `4CH1-CON-EQ-WORD` — Word equation |
| node kind | CONCEPT · concept (mixed demand) |
| SpecificationPoint attachments | `4CH1-1.25` CORE (write) |
| exact source evidence (4CH1-1.25) | [NOTE] "Word equations show the reactants and products of a chemical reaction using their full chemical names" |
| aliases (+ evidence) | word equations [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Writing chemical equations - IGCSE Chemistry Revision Notes.md] |
| placement (PART_OF) | `4CH1-1.25` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-01 |

### N-02 — `4CH1-CON-EQ-SYMBOL` Balanced symbol (chemical) equation

| field | value |
|---|---|
| concept identity | `4CH1-CON-EQ-SYMBOL` — Balanced symbol (chemical) equation |
| node kind | CONCEPT · concept (mixed demand) |
| SpecificationPoint attachments | `4CH1-1.25` CORE (write) |
| exact source evidence (4CH1-1.25) | [NOTE] "A symbol equation must be balanced to give the correct ratio of reactants and products" |
| aliases (+ evidence) | symbol equation [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Writing chemical equations - IGCSE Chemistry Revision Notes.md]; chemical equation [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md]; balanced equation [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md]; balancing equations [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Writing chemical equations - IGCSE Chemistry Revision Notes.md] |
| placement (PART_OF) | `4CH1-1.25` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-02 |

### N-03 — `4CH1-CON-EQ-STATE-SYM` State symbols (s), (l), (g), (aq)

| field | value |
|---|---|
| concept identity | `4CH1-CON-EQ-STATE-SYM` — State symbols (s), (l), (g), (aq) |
| node kind | CONCEPT · concept (mixed demand) |
| SpecificationPoint attachments | `4CH1-1.25` CORE (write) |
| exact source evidence (4CH1-1.25) | [NOTE] "You need to be confident using the state symbols (s), (l), (g) and (aq)" |
| aliases (+ evidence) | state symbol [VARIANT @ 'state symbols' @ Writing chemical equations - IGCSE Chemistry Revision Notes.md] |
| placement (PART_OF) | `4CH1-1.25` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-03 |

### N-04 — `4CH1-CON-CONSERVATION-MASS` Law of Conservation of Mass

| field | value |
|---|---|
| concept identity | `4CH1-CON-CONSERVATION-MASS` — Law of Conservation of Mass |
| node kind | CONCEPT · concept (mixed demand) |
| SpecificationPoint attachments | `4CH1-1.25` CORE (write); `4CH1-1.26` SUPPORTING (calculate) |
| exact source evidence (4CH1-1.25) | [NOTE] "Atoms cannot be created or destroyed, so if they exist in the reactants then they absolutely must be in the products!" |
| exact source evidence (4CH1-1.26) | [NOTE] "In accordance with the Law of Conservation of Mass, the sum of the relative formula masses of the reactants will be the same as the sum of the relative formula masses of the products" |
| aliases (+ evidence) | conservation of mass [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Writing chemical equations - IGCSE Chemistry Revision Notes.md] |
| placement (PART_OF) | `4CH1-1.25` CORE; `4CH1-1.26` SUPPORTING |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-04 |

### N-05 — `4CH1-CON-AR` Relative atomic mass (Ar)

| field | value |
|---|---|
| concept identity | `4CH1-CON-AR` — Relative atomic mass (Ar) |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.26` CORE (calculate); `4CH1-1.28` CORE (understand) |
| exact source evidence (4CH1-1.26) | [NOTE] "The relative atomic mass of every element is given on the Periodic Table. It is the larger of the two numbers." |
| exact source evidence (4CH1-1.28) | [SPEC] "calculations involving amount of substance, relative atomic mass" |
| aliases (+ evidence) | relative atomic mass [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md]; Ar [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md] |
| placement (PART_OF) | `4CH1-1.26` CORE; `4CH1-1.28` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-05 |

### N-06 — `4CH1-CON-MR` Relative formula mass (Mr)

| field | value |
|---|---|
| concept identity | `4CH1-CON-MR` — Relative formula mass (Mr) |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.26` CORE (calculate); `4CH1-1.28` CORE (understand) |
| exact source evidence (4CH1-1.26) | [NOTE] "To calculate the Mr of a substance, you have to add up the relative atomic masses of all the atoms present in the formula" |
| exact source evidence (4CH1-1.28) | [SPEC] "relative formula mass" |
| aliases (+ evidence) | relative molecular mass [UNEVIDENCED]; relative formula mass [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md]; Mr [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md] |
| placement (PART_OF) | `4CH1-1.26` CORE; `4CH1-1.28` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** — alias-audit: 1 unevidenced alias(es) — see §7 |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-06 |

### N-07 — `4CH1-CON-MOLE` The mole (unit of amount of substance)

| field | value |
|---|---|
| concept identity | `4CH1-CON-MOLE` — The mole (unit of amount of substance) |
| node kind | CONCEPT · term definition (KNOW_TERM demand) |
| SpecificationPoint attachments | `4CH1-1.27` CORE (know) |
| exact source evidence (4CH1-1.27) | [SPEC] "know that the mole(mol) is the unit for the amount of a substance" |
| aliases (+ evidence) | amount of substance [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Solution concentration - IGCSE Chemistry Revision Notes.md]; chemical amount [VARIANT @ 'chemical amounts' @ Calculating moles and mass - IGCSE Chemistry Revision Notes.md]; mol [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md] |
| placement (PART_OF) | `4CH1-1.27` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-07 |

### N-08 — `4CH1-CON-AVOGADRO-CONST` Avogadro constant

| field | value |
|---|---|
| concept identity | `4CH1-CON-AVOGADRO-CONST` — Avogadro constant |
| node kind | CONCEPT · enrichment content (taught substantively; demanded by no SP) |
| SpecificationPoint attachments | `4CH1-1.27` ENRICHMENT (know) |
| exact source evidence (4CH1-1.27) | [NOTE] "The number of atoms, molecules or ions in a mole (1 mol) of a given substance is the Avogadro constant." |
| aliases (+ evidence) | Avogadro's constant [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md] |
| placement (PART_OF) | `4CH1-1.27` ENRICHMENT |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE (pass-2 note)** |
| pass-2 verdict | CONFIRM_WITH_NOTE — "ENRICHMENT role is right: 1.27 wording demands only the unit; the constant is taught enrichment. Keep node for expansion (mole deepening)." |
| recommendation | CONFIRM — bulk-eligible; read the one-line pass-2 note first |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-08 |

### N-09 — `4CH1-CON-MOLAR-MASS` Molar mass

| field | value |
|---|---|
| concept identity | `4CH1-CON-MOLAR-MASS` — Molar mass |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.28` CORE (understand) |
| exact source evidence (4CH1-1.28) | [NOTE] "The mass of 1 mole of a substance is known as the molar mass" |
| aliases (+ evidence) | mass of 1 mole [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md] |
| placement (PART_OF) | `4CH1-1.28` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-09 |

### N-10 — `4CH1-CON-MOLE-MASS-CONV` Mole-mass conversion

| field | value |
|---|---|
| concept identity | `4CH1-CON-MOLE-MASS-CONV` — Mole-mass conversion |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.28` CORE (understand) |
| exact source evidence (4CH1-1.28) | [NOTE] "Therefore we have to be able to convert between moles and grams" |
| aliases (+ evidence) | converting between moles and grams [VARIANT @ 'convert between moles and grams' @ Calculating moles and mass - IGCSE Chemistry Revision Notes.md]; moles and mass calculations [UNEVIDENCED] |
| placement (PART_OF) | `4CH1-1.28` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** — alias-audit: 1 unevidenced alias(es) — see §7 |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-10 |

### N-11 — `4CH1-CON-MOLAR-RATIO` Molar ratio from balanced equations

| field | value |
|---|---|
| concept identity | `4CH1-CON-MOLAR-RATIO` — Molar ratio from balanced equations |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.29` CORE (calculate) |
| exact source evidence (4CH1-1.29) | [NOTE] "Remember the molar ratio of a balanced equation gives you the ratio of the amounts of each substance in the reaction." |
| aliases (+ evidence) | mole ratio [UNEVIDENCED]; ratio of amounts [UNEVIDENCED] |
| placement (PART_OF) | `4CH1-1.29` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE (pass-2 note)** — alias-audit: 2 unevidenced alias(es) — see §7 |
| pass-2 verdict | CONFIRM_WITH_NOTE — "CORE under 1.29 is right; consider also SUPPORTING under 1.28 in expansion (the 1.28 note mentions molar ratios but does not demand them). Not a pilot change." |
| recommendation | CONFIRM — bulk-eligible; read the one-line pass-2 note first |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-11 |

### N-12 — `4CH1-CON-REACTING-MASS` Reacting mass calculation

| field | value |
|---|---|
| concept identity | `4CH1-CON-REACTING-MASS` — Reacting mass calculation |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.29` CORE (calculate) |
| exact source evidence (4CH1-1.29) | [SPEC] "calculate reacting masses using experimental data and chemical equations" |
| aliases (+ evidence) | calculating reacting masses [UNEVIDENCED]; mass calculations from equations [UNEVIDENCED] |
| placement (PART_OF) | `4CH1-1.29` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** — alias-audit: 2 unevidenced alias(es) — see §7 |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-12 |

### N-13 — `4CH1-CON-YIELD` Yield (actual yield)

| field | value |
|---|---|
| concept identity | `4CH1-CON-YIELD` — Yield (actual yield) |
| node kind | CONCEPT · operand DEFINITION under a CALCULATE point (OD-1: the procedure node is CON-PERCENT-YIELD) |
| SpecificationPoint attachments | `4CH1-1.30` CORE (calculate) |
| exact source evidence (4CH1-1.30) | [NOTE] "The actual yield is the recorded amount of product obtained" |
| aliases (+ evidence) | actual yield [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate percentage yield - IGCSE Chemistry Revision Notes.md]; yield of a reaction [UNEVIDENCED] |
| placement (PART_OF) | `4CH1-1.30` CORE |
| potential duplicate / overlap | pass-2 merge candidate: Split-first policy honored; merge candidate with CON-THEOR-YIELD if the operator judges the split too fine (aliases make the merge trivial).; member of the OD-1 yield triple — merge question is the OD-1 ratification, not a per-node decision; alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **FC-2 identity (OD-1-linked)** — FC-2: identity — pass-2 merge candidate (OD-1 governs); alias-audit: 1 unevidenced alias(es) — see §7; OD-1: member of the yield triple (ratification governs) |
| pass-2 verdict | CONFIRM_WITH_NOTE — "Split-first policy honored; merge candidate with CON-THEOR-YIELD if the operator judges the split too fine (aliases make the merge trivial)." |
| recommendation | CONFIRM-split if OD-1 is ratified; MERGE is the operator-only alternative (re-versions nodes, removes the operand edge pair) — do not decide this node before ruling OD-1 |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-13 |

### N-14 — `4CH1-CON-THEOR-YIELD` Theoretical yield

| field | value |
|---|---|
| concept identity | `4CH1-CON-THEOR-YIELD` — Theoretical yield |
| node kind | CONCEPT · operand DEFINITION under a CALCULATE point (OD-1: the procedure node is CON-PERCENT-YIELD) |
| SpecificationPoint attachments | `4CH1-1.30` CORE (calculate) |
| exact source evidence (4CH1-1.30) | [NOTE] "The theoretical yield is the amount of product that would be obtained under perfect practical and chemical conditions" |
| aliases (+ evidence) | maximum yield [UNEVIDENCED] |
| placement (PART_OF) | `4CH1-1.30` CORE |
| potential duplicate / overlap | pass-2 merge candidate: Merge candidate with CON-YIELD (see above); distinct derivation basis justifies the split at pilot granularity.; member of the OD-1 yield triple — merge question is the OD-1 ratification, not a per-node decision; alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **FC-2 identity (OD-1-linked)** — FC-2: identity — pass-2 merge candidate (OD-1 governs); alias-audit: 1 unevidenced alias(es) — see §7; OD-1: member of the yield triple (ratification governs) |
| pass-2 verdict | CONFIRM_WITH_NOTE — "Merge candidate with CON-YIELD (see above); distinct derivation basis justifies the split at pilot granularity." |
| recommendation | CONFIRM-split if OD-1 is ratified; MERGE is the operator-only alternative (re-versions nodes, removes the operand edge pair) — do not decide this node before ruling OD-1 |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-14 |

### N-15 — `4CH1-CON-PERCENT-YIELD` Percentage yield

| field | value |
|---|---|
| concept identity | `4CH1-CON-PERCENT-YIELD` — Percentage yield |
| node kind | CONCEPT · calculation procedure (CALCULATE demand; the OD-1 procedure node of the yield triple) |
| SpecificationPoint attachments | `4CH1-1.30` CORE (calculate) |
| exact source evidence (4CH1-1.30) | [SPEC] "calculate percentage yield" |
| aliases (+ evidence) | percentage yield calculation [UNEVIDENCED] |
| placement (PART_OF) | `4CH1-1.30` CORE |
| potential duplicate / overlap | member of the OD-1 yield triple — merge question is the OD-1 ratification, not a per-node decision; alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** — alias-audit: 1 unevidenced alias(es) — see §7; OD-1: member of the yield triple (ratification governs) |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-15 |

### N-16 — `4CH1-CON-YIELD-FACTORS` Factors reducing yield

| field | value |
|---|---|
| concept identity | `4CH1-CON-YIELD-FACTORS` — Factors reducing yield |
| node kind | CONCEPT · enrichment content (taught substantively; demanded by no SP) |
| SpecificationPoint attachments | `4CH1-1.30` ENRICHMENT (calculate) |
| exact source evidence (4CH1-1.30) | [NOTE] "In practice, you never get 100% yield in a chemical process for several reasons" |
| aliases (+ evidence) | reasons for less than 100 percent yield [UNEVIDENCED]; yield losses [UNEVIDENCED] |
| placement (PART_OF) | `4CH1-1.30` ENRICHMENT |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE (pass-2 note)** — alias-audit: 2 unevidenced alias(es) — see §7 |
| pass-2 verdict | CONFIRM_WITH_NOTE — "ENRICHMENT role correct (SP demands calculation only); the five enumerated causes are substantive teaching. Retain for recommendation use." |
| recommendation | CONFIRM — bulk-eligible; read the one-line pass-2 note first |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-16 |

### N-17 — `4CH1-CON-EMPIRICAL-FORMULA` Empirical formula

| field | value |
|---|---|
| concept identity | `4CH1-CON-EMPIRICAL-FORMULA` — Empirical formula |
| node kind | CONCEPT · term definition (KNOW_TERM demand) |
| SpecificationPoint attachments | `4CH1-1.32` CORE (know); `4CH1-1.33` CORE (calculate) |
| exact source evidence (4CH1-1.32) | [SPEC] "know what is meant by the terms empirical formula and molecular formula" |
| exact source evidence (4CH1-1.33) | [SPEC] "calculate empirical and molecular formulae from experimental data" |
| aliases (+ evidence) | simplest whole number ratio formula [UNEVIDENCED] |
| placement (PART_OF) | `4CH1-1.32` CORE; `4CH1-1.33` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** — alias-audit: 1 unevidenced alias(es) — see §7 |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-17 |

### N-18 — `4CH1-CON-MOLECULAR-FORMULA` Molecular formula

| field | value |
|---|---|
| concept identity | `4CH1-CON-MOLECULAR-FORMULA` — Molecular formula |
| node kind | CONCEPT · term definition (KNOW_TERM demand) |
| SpecificationPoint attachments | `4CH1-1.32` CORE (know); `4CH1-1.33` CORE (calculate) |
| exact source evidence (4CH1-1.32) | [NOTE] "The molecular formula is the formula that shows the number and type of each atom in a molecule" |
| exact source evidence (4CH1-1.33) | [SPEC] "calculate empirical and molecular formulae from experimental data" |
| aliases (+ evidence) | (none) |
| placement (PART_OF) | `4CH1-1.32` CORE; `4CH1-1.33` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-18 |

### N-19 — `4CH1-CON-EMP-MOL-CALC` Empirical and molecular formula calculation

| field | value |
|---|---|
| concept identity | `4CH1-CON-EMP-MOL-CALC` — Empirical and molecular formula calculation |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.33` CORE (calculate) |
| exact source evidence (4CH1-1.33) | [NOTE] "Empirical formula calculations are very methodical" |
| aliases (+ evidence) | empirical formula calculation [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md]; molecular formula calculation [UNEVIDENCED]; deducing formulae of hydrated salts [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md] |
| placement (PART_OF) | `4CH1-1.33` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** — alias-audit: 1 unevidenced alias(es) — see §7 |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-19 |

### N-20 — `4CH1-CON-EXP-FORMULA-DEDUCTION` Experimental formula deduction (mass-difference method)

| field | value |
|---|---|
| concept identity | `4CH1-CON-EXP-FORMULA-DEDUCTION` — Experimental formula deduction (mass-difference method) |
| node kind | CONCEPT · experimental method (DESCRIBE_EXPERIMENT demand) |
| SpecificationPoint attachments | `4CH1-1.31` CORE (understand); `4CH1-1.36` CORE (know) |
| exact source evidence (4CH1-1.31) | [NOTE] "The principle is to use mass measurements before and after a reaction and then convert masses into moles" |
| exact source evidence (4CH1-1.36) | [NOTE] "To determine the empirical formula of magnesium oxide by combustion of magnesium" |
| aliases (+ evidence) | deducing formulae by experiment [UNEVIDENCED]; formula from mass measurements [UNEVIDENCED] |
| placement (PART_OF) | `4CH1-1.31` CORE; `4CH1-1.36` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** — alias-audit: 2 unevidenced alias(es) — see §7 |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-20 |

### N-21 — `4CH1-CON-WATER-CRYST` Water of crystallisation and hydrated salts

| field | value |
|---|---|
| concept identity | `4CH1-CON-WATER-CRYST` — Water of crystallisation and hydrated salts |
| node kind | CONCEPT · experimental method (DESCRIBE_EXPERIMENT demand) |
| SpecificationPoint attachments | `4CH1-1.31` CORE (understand) |
| exact source evidence (4CH1-1.31) | [SPEC] "salts containing water of crystallisation" |
| aliases (+ evidence) | hydrated salt [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md]; water of crystallisation [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md] |
| placement (PART_OF) | `4CH1-1.31` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-21 |

### N-22 — `4CH1-CON-CONCENTRATION` Concentration of a solution

| field | value |
|---|---|
| concept identity | `4CH1-CON-CONCENTRATION` — Concentration of a solution |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.34C` CORE (understand) |
| exact source evidence (4CH1-1.34C) | [NOTE] "Concentration refers to the amount of solute there is in a specific volume of the solvent" |
| aliases (+ evidence) | concentration [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Solution concentration - IGCSE Chemistry Revision Notes.md] |
| placement (PART_OF) | `4CH1-1.34C` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-22 |

### N-23 — `4CH1-CON-CONC-CALC` Concentration calculation (mol/dm3)

| field | value |
|---|---|
| concept identity | `4CH1-CON-CONC-CALC` — Concentration calculation (mol/dm3) |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.34C` CORE (understand) |
| exact source evidence (4CH1-1.34C) | [NOTE] "Calculate the concentration of a solution of sodium hydroxide, NaOH, in mol / dm3" |
| aliases (+ evidence) | concentration calculations [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Solution concentration - IGCSE Chemistry Revision Notes.md]; amount of substance from concentration [UNEVIDENCED] |
| placement (PART_OF) | `4CH1-1.34C` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** — alias-audit: 1 unevidenced alias(es) — see §7 |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-23 |

### N-24 — `4CH1-CON-VOL-CONVERSION` Volume unit conversion (cm3/dm3)

| field | value |
|---|---|
| concept identity | `4CH1-CON-VOL-CONVERSION` — Volume unit conversion (cm3/dm3) |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.34C` CORE (understand) |
| exact source evidence (4CH1-1.34C) | [NOTE] "To convert cm3 to dm3, divide by 1000" |
| aliases (+ evidence) | converting cm3 to dm3 [VARIANT @ 'convert cm3 to dm3' @ Solution concentration - IGCSE Chemistry Revision Notes.md] |
| placement (PART_OF) | `4CH1-1.34C` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE (pass-2 note)** |
| pass-2 verdict | CONFIRM_WITH_NOTE — "The split is validated independently by the mark-scheme wrong-answer pattern (MS Q4a) — keep as its own mastery unit." |
| recommendation | CONFIRM — bulk-eligible; read the one-line pass-2 note first |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-24 |

### N-25 — `4CH1-CON-MOLAR-GAS-VOL` Molar gas volume at RTP (24 dm3)

| field | value |
|---|---|
| concept identity | `4CH1-CON-MOLAR-GAS-VOL` — Molar gas volume at RTP (24 dm3) |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.35C` CORE (understand) |
| exact source evidence (4CH1-1.35C) | [SPEC] "the molar volume of a gas(24dm3and24000cm3at room temperature and pressure(rtp))" |
| aliases (+ evidence) | molar volume [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md]; molar gas volume [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md] |
| placement (PART_OF) | `4CH1-1.35C` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-25 |

### N-26 — `4CH1-CON-GAS-VOL-CALC` Gas volume calculation

| field | value |
|---|---|
| concept identity | `4CH1-CON-GAS-VOL-CALC` — Gas volume calculation |
| node kind | CONCEPT · calculation procedure (CALCULATE demand) |
| SpecificationPoint attachments | `4CH1-1.35C` CORE (understand) |
| exact source evidence (4CH1-1.35C) | [NOTE] "The formula can be used to calculate the number of moles of gases from a given volume or vice versa" |
| aliases (+ evidence) | calculating gas volumes [UNEVIDENCED]; converting moles into volumes [VERBATIM @ Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md] |
| placement (PART_OF) | `4CH1-1.35C` CORE |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** — alias-audit: 1 unevidenced alias(es) — see §7 |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-26 |

### N-27 — `4CH1-CON-AVOGADRO-LAW` Avogadro's Law

| field | value |
|---|---|
| concept identity | `4CH1-CON-AVOGADRO-LAW` — Avogadro's Law |
| node kind | CONCEPT · enrichment content (taught substantively; demanded by no SP) |
| SpecificationPoint attachments | `4CH1-1.35C` ENRICHMENT (understand) |
| exact source evidence (4CH1-1.35C) | [NOTE] "Avogadro’s Law states that at the same conditions of temperature and pressure, equal amounts of gases occupy the same volume of space" |
| aliases (+ evidence) | (none) |
| placement (PART_OF) | `4CH1-1.35C` ENRICHMENT |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE (pass-2 note)** |
| pass-2 verdict | CONFIRM_WITH_NOTE — "ENRICHMENT role right; the law grounds but is not demanded by 1.35C." |
| recommendation | CONFIRM — bulk-eligible; read the one-line pass-2 note first |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-27 |

### N-28 — `4CH1-MIS-EQ-SUBSCRIPT` Balancing equations by altering subscripts

| field | value |
|---|---|
| concept identity | `4CH1-MIS-EQ-SUBSCRIPT` — Balancing equations by altering subscripts |
| node kind | MISCONCEPTION · documented student error (misconception / wrong-answer pattern; unattached by design) |
| SpecificationPoint attachments | (unattached) |
| aliases (+ evidence) | changing formula subscripts to balance [UNEVIDENCED] |
| placement (PART_OF) |  |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** — alias-audit: 1 unevidenced alias(es) — see §7 |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-28 |

### N-29 — `4CH1-MIS-CONC-UNIT` Failing to convert cm3 to dm3 in concentration calculations

| field | value |
|---|---|
| concept identity | `4CH1-MIS-CONC-UNIT` — Failing to convert cm3 to dm3 in concentration calculations |
| node kind | MISCONCEPTION · documented student error (misconception / wrong-answer pattern; unattached by design) |
| SpecificationPoint attachments | (unattached) |
| aliases (+ evidence) | failing to divide by 1000 [VERBATIM @ scripts/c11_evidence/CFEC2_MS_P1.txt] |
| placement (PART_OF) |  |
| potential duplicate / overlap | alias-collision check: clean |
| confidence / status | high / SUGGESTED |
| pre-triage | **LIKELY_SAFE** |
| pass-2 verdict | CONFIRM |
| recommendation | CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant) |
| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / SPLIT) — record in `c11_review_verdicts.yaml` row N-29 |

---

## 5. Held / rejected appendix (13 entries — informational, no reopening)

**Channel legend.** `HELD` = abstained at generation: evidence-complete or deliberately withheld, NOT in the graph, NOT promotable, awaiting future evidence or an operator decision — but this package does not reopen any of them. `REJECTED` = permanently refused and machine-guarded (not an edge; promotion categorically refused: T19/T20). A third quarantine channel exists outside this list: the operator **HOLD** on the REVIEW_REQUIRED edge `CON-GAS-VOL-CALC → CON-AVOGADRO-LAW` — that edge IS in the graph, stays REVIEW_REQUIRED, is not promotable, and is not to be converted to ACCEPT/REJECT merely to complete the pilot.

### HELD-01 — HELD

| field | value |
|---|---|
| channel | HELD (abstained — awaiting evidence/decision, not promotable, not in the graph) |
| candidate | MISCONCEPTION node "rounding non-integer empirical ratios" (e.g. 1.5 -> 2) MISCONCEPTION_OF CON-EMP-MOL-CALC |
| evidence (recorded at generation) | "Empirical & Molecular Formulae Examiner Tips: "The molar ratio must be a whole number. If you don't get a whole number when calculating the ratio of atoms in an empirical formula, such as 1.5, multiply that and the other ratios to achieve whole numbers"" |
| reason | INSUFFICIENT_EVIDENCE_MISCONCEPTION — the tip prescribes correct practice but names no mistake and documents no wrong answer; the specific mishandling (rounding/truncating) would be invented. §8A.11 forbids LLM-imagined student errors. No slice mark scheme documents this error. |
| failure class | FC-1 |
| pass-2 review | AGREE_HOLD — "Right call: examiner tip implies practice, not a documented error. Revisit only if a mark scheme documents the rounding error." |

### HELD-02 — HELD

| field | value |
|---|---|
| channel | HELD (abstained — awaiting evidence/decision, not promotable, not in the graph) |
| candidate | COMMONLY_CONFUSED_WITH(CON-CONCENTRATION, "solution strength") |
| evidence (recorded at generation) | "Solution concentration note: "Concentration is sometimes commonly referred to as strength"" |
| reason | NO_TARGET_NODE_PLUS_WEAK_CLASS — the statement documents colloquial usage, not a student confusion pair; "strength" is not a slice concept (boundary gap, out-of-slice). Minting a stub node to receive the edge would violate the pilot scope rule. |
| failure class | FC-2 |
| pass-2 review | AGREE_HOLD — "Right call: colloquial-usage statement, target out of slice." |

### HELD-03 — HELD

| field | value |
|---|---|
| channel | HELD (abstained — awaiting evidence/decision, not promotable, not in the graph) |
| candidate | EXPLAINED_BY(CON-MOLE, CON-AVOGADRO-CONST) — "the Avogadro constant quantifies the mole" |
| evidence (recorded at generation) | "Calculating moles and mass: "The number of atoms, molecules or ions in a mole (1 mol) of a given substance is the Avogadro constant."" |
| reason | RELATION_CLASS_AMBIGUOUS — equally defensible as EXPLAINED_BY, a definitional PART_OF, or RELATED_TO; no single clearly-correct relation class. Emitting any one would assert semantics the corpus does not pin down. |
| failure class | FC-2 |
| pass-2 review | AGREE_HOLD — "Right call: relation-class genuinely undecidable from the corpus." |

### HELD-04 — HELD

| field | value |
|---|---|
| channel | HELD (abstained — awaiting evidence/decision, not promotable, not in the graph) |
| candidate | REQUIRES_PREREQUISITE(CON-GAS-VOL-CALC, CON-MOLE) |
| evidence (recorded at generation) | "Calculate Gas Volumes: "The formula can be used to calculate the number of moles of gases from a given volume or vice versa"" |
| reason | TRANSITIVELY_SUBSUMED — covered by CON-GAS-VOL-CALC -> CON-MOLAR-GAS-VOL -> CON-MOLE; an explicit edge adds no reviewable information (density control). |
| failure class | FC-3 |
| pass-2 review | AGREE_HOLD — "Right call: transitively subsumed." |

### HELD-05 — HELD

| field | value |
|---|---|
| channel | HELD (abstained — awaiting evidence/decision, not promotable, not in the graph) |
| candidate | REQUIRES_PREREQUISITE(CON-MOLAR-RATIO, CON-EQ-SYMBOL) |
| evidence (recorded at generation) | "Reacting mass calculations: "the molar ratio of a balanced equation gives you the ratio of the amounts"" |
| reason | TRANSITIVELY_SUBSUMED_PLUS_DEFENSIONAL — the ratio concept is definitionally bound to balanced equations, but CON-REACTING-MASS already carries both dependencies; an extra edge would duplicate the chain (density control). |
| failure class | FC-3 |
| pass-2 review | AGREE_HOLD — "Right call: density control." |

### HELD-06 — HELD

| field | value |
|---|---|
| channel | HELD (abstained — awaiting evidence/decision, not promotable, not in the graph) |
| candidate | REQUIRES_PREREQUISITE(CON-EMP-MOL-CALC, CON-MOLE-MASS-CONV) |
| evidence (recorded at generation) | "Empirical & Molecular Formulae: "Calculate the moles of each element" (step 4: Moles = mass/Ar)" |
| reason | TAUGHT_INLINE — the empirical procedure re-teaches its own per-element mass/Ar division as procedure steps 3-4; the compound-level mole-mass conversion procedure (mass = moles x Mr) is not presupposed. Mention ≠ dependency (the tasking rule). The true prerequisites (CON-MOLE, CON-AR) are emitted. |
| failure class | FC-3 |
| pass-2 review | AGREE_HOLD — "Right call: taught-inline (the exact mention-vs-dependency distinction the tasking demands)." |

### HELD-07 — HELD

| field | value |
|---|---|
| channel | HELD (abstained — awaiting evidence/decision, not promotable, not in the graph) |
| candidate | REQUIRES_PREREQUISITE(CON-CONCENTRATION, solute/solvent/solution concepts) |
| evidence (recorded at generation) | "Solution concentration: "A solute is a solid substance that dissolves into a liquid"" |
| reason | TAUGHT_INLINE_PLUS_BOUNDARY — the 1.34C note re-teaches solute/solvent/solution definitions inline (so no learning dependency), and those concepts belong to the S1-a solutions notes (out of slice; boundary gap). |
| failure class | FC-3 |
| pass-2 review | AGREE_HOLD — "Right call: taught-inline + boundary." |

### HELD-08 — HELD

| field | value |
|---|---|
| channel | HELD (abstained — awaiting evidence/decision, not promotable, not in the graph) |
| candidate | RELATED_TO(CON-EMPIRICAL-FORMULA, CON-MOLECULAR-FORMULA) |
| evidence (recorded at generation) | "E&MF note relationship table (methane CH4/CH4, ethane CH3/C2H6, ethene, benzene)" |
| reason | RESIDUAL_CLASS_DISCIPLINE — the pair already carries REQUIRES_PREREQUISITE(MOLECULAR, EMPIRICAL); RELATED_TO is reserved for evidenced NON-dependency associations and must not duplicate a dependency pair. |
| failure class | FC-2 |
| pass-2 review | AGREE_HOLD — "Right call: residual-class discipline." |

### HELD-09 — REJECTED

| field | value |
|---|---|
| channel | REJECTED (permanent, machine-guarded) |
| candidate | EXPLAINED_BY("SO2 formation from fuel impurities" concept, "combustion of hydrocarbon fuels" concept) and REMEDIATED_BY / MISCONCEPTION_OF companions attached to 4CH1-4.15 |
| evidence (recorded at generation) | "Definition of combustion note: "All these fuels contain carbon, hydrogen and small quantities of sulfur"; Nitrogen Oxides & Sulfur Dioxide note: "The sulfur dioxide produced from the combustion of fossil fuels dissolves in rainwater"" |
| reason | NEGATIVE_CONTROL_4_15 — premise (sulfur impurities in fuels, mapped to 4.11-4.13) + stated consequence (SO2 -> acid rain, mapped to 4.14/4.16) present in DIFFERENT notes; the demanded "explain how" causal mechanism is taught nowhere. Aggregating premise + consequence constructs the missing teaching by inference — forbidden by §0.0/guide §8 (the exact round-4 T-C10 rejection). No concept may attach to 4.15 (no validated T-C10 coverage exists). |
| failure class | FC-4 |
| pass-2 review | AGREE_REJECT — "Right call: the 4.15 negative control — premise+consequence aggregation is exactly the forbidden inference." |

### HELD-10 — HELD

| field | value |
|---|---|
| channel | HELD (abstained — awaiting evidence/decision, not promotable, not in the graph) |
| candidate | REQUIRES_PREREQUISITE(CON-EXP-FORMULA-DEDUCTION, CON-EMP-MOL-CALC) |
| evidence (recorded at generation) | "Simple compound formulae: "Using the moles of reactants and products it is possible to deduce molar ratios and hence an empirical formula"" |
| reason | RELATION_CLASS_AMBIGUOUS — "application-of vs requires" is undecidable from the corpus: the deduction method embeds the ratio-simplification steps inline (Steps 1-3 re-teach them compactly), so it is unclear whether the procedure is presupposed or re-taught. |
| failure class | FC-2 |
| pass-2 review | AGREE_HOLD — "Right call: application-of vs requires is undecidable; good REVIEW-required-style candidate for the expansion round." |

### HELD-11 — HELD

| field | value |
|---|---|
| channel | HELD (abstained — awaiting evidence/decision, not promotable, not in the graph) |
| candidate | WRONG_ANSWER_PATTERN node from CFEC1 MS Q4(a)(ii)-(iii) ("0.44 for 1 mark only" / "0.0004") |
| evidence (recorded at generation) | "CFEC1_MS_P1.txt page 4: "M1 44 / M2 cm3 / M2 0.00044(0)" with "0.44 for 1 mark only" and "0.0004" in the reject column" |
| reason | EVIDENCE_AMBIGUOUS_EXTRACTION — the pinned PDF-table extraction garbles the question context (values and units cannot be reconstructed without the question paper, which is not in the pinned evidence set). A wrong-answer-pattern node requires unambiguous assessment context. Revisit when the paired QP is pinned (T-C06 territory). |
| failure class | FC-1 |
| pass-2 review | AGREE_HOLD — "Right call: garbled PDF-table extraction is not load-bearing evidence; revisit with the paired question paper (T-C06)." |

### HELD-12 — HELD

| field | value |
|---|---|
| channel | HELD (abstained — awaiting evidence/decision, not promotable, not in the graph) |
| candidate | MISCONCEPTION node "products written first confuses word-equation construction" MISCONCEPTION_OF CON-EQ-WORD |
| evidence (recorded at generation) | "Writing chemical equations worked example 2: "Careful: This question has all the required information but the products are written first"" |
| reason | EXAM_TECHNIQUE_NOT_MISCONCEPTION — the Careful annotation is question-reading guidance (parse the given information), not a documented erroneous belief about chemistry. §8A.11 evidence classes do not cover it. |
| failure class | FC-2 |
| pass-2 review | AGREE_HOLD — "Right call: exam-technique guidance, not an erroneous belief." |

### HELD-13 — REJECTED

| field | value |
|---|---|
| channel | REJECTED (permanent, machine-guarded) |
| candidate | REQUIRES_PREREQUISITE(PR-03, CON-MOLE) |
| evidence (recorded at generation) | "Investigating metal oxide formulas results tables: "\| moles \| a / Ar \| a / Ar \|" (MgO) and the parallel "\| moles \| b / Mr \| b / Mr \|" row (CuO) — the ONLY occurrences of "mole(s)" in the note, never in prose (Aim/Method/Steps)." |
| reason | OPERATOR_REJECT (2026-09-11) — failure classes FC-3 (transitively subsumed via PR-03 -> CON-EXP-FORMULA-DEDUCTION -> CON-MOLE) with FC-1 evidence basis (IMPLICIT_USE: table-row label only, never substantively taught in the note body). Per the operator rule: do not treat table labels or incidental terminology as instructional evidence. |
| failure class | FC-3 (primary; transitively subsumed) + FC-1 (implicit-use evidence) |
| pass-2 review |  |
| operator decision | REJECT by operator 2026-09-11 — reasons verbatim: ""moles" appears only as a table-row label in the practical note."; "It is not substantively taught in the note body."; "The claimed dependency is also transitively subsumed through the existing formula-deduction → mole path."; "Do not treat table labels or incidental terminology as instructional evidence." |

*(Session-43 finding, documentation-only: HELD-08 is unassigned in the §19 / §16-item-6 failure-class distributions, which count 12 of 13 entries — this appendix assigns it FC-2 (residual-class discipline). ARCHITECTURE.md §19 text is unchanged; flag it for the next revision of that document.)*

---

## 6. Ontology decision ratification slots — PENDING OPERATOR RATIFICATION

Neither slot below is ratified. OD-1 is an **agent-derived ontology recommendation**; OD-2's verbatim rule is operator-issued but its codification as a standing expansion rule is **agent-proposed**. Both provenances are stated exactly and must not be silently relabeled.

### OD-1 — The yield triple stays split (three concept nodes)

**STATUS: PENDING OPERATOR RATIFICATION**

- Provenance: Agent-derived ontology recommendation — session 41, exercising the operator's delegated instruction to resolve the yield-triple question as an ontology decision, on frozen identity-policy grounds (§8). Recorded in C11_ARCHITECTURE.md §20. NOT operator-ratified: it must not be relabeled as ratified without an explicit operator decision.
- Effect if ratified: Becomes a binding generation rule for §16 (one procedure concept + one concept per distinctly-taught operand definition, one prerequisite per operand). The PERCENT-YIELD edge pair (E-09/E-10) and the three yield nodes are then confirmable as-is; a future merge stays operator-only.
- Recorded ruling (verbatim, C11_ARCHITECTURE.md §20):

```markdown
### OD-1 — The yield triple stays split (three concept nodes)

**Question** (pass-2 flag; finding FP-2): should CON-YIELD (actual yield),
CON-THEOR-YIELD (theoretical yield) and CON-PERCENT-YIELD (percentage yield)
merge into one yield concept? The two PERCENT-YIELD → {YIELD, THEOR-YIELD}
prerequisite edges share one anchor sentence, and FP-2 noted both "vanish
under an operator merge".

**Ruling (recorded for the operator; agent-derived from the frozen identity
policy, exercising the operator's delegated session-41 instruction to resolve
the question as an ontology decision): NO MERGE — the three nodes stay
split.**

1. Minting rule (§8): the triple is two definitions + one calculation
   procedure — "a definition, a law, a constant, a calculation procedure, an
   experimental method are distinct concepts". Each node carries distinct
   taught substance: two distinct definition sentences in the 1.30-mapped
   note plus the SPEC-demanded comparison procedure.
2. Definition-vs-procedure split (§8; the 1.32 know-terms vs 1.33-calculate
   precedent) applies directly: 4CH1-1.30 demands a calculation, and the
   operand definitions and the procedure are separate node kinds by frozen
   rule.
3. Mastery attribution: the three are independently assessable (a candidate
   can define theoretical yield without executing the percentage computation
   and vice versa — this very unit separates KNOW_TERM from CALCULATE
   demands, e.g. 1.27 vs 1.28). A merge would credit definitional knowledge
   from procedural mastery and vice versa — exactly the "over-merging
   corrupts mastery attribution" failure; over-splitting is recoverable, the
   reverse is not.
4. The same-anchor edge pair is not a split artifact: "The percentage yield
   compares the actual yield to the theoretical yield" names BOTH operands
   of the one taught comparison — one sentence can ground two distinct
   dependencies (numerator object, denominator object). Edge multiplicity
   mirroring the formula's operand structure is the honest representation,
   not a defect to be normalized away.

**Generalized rule for §16** (why this is an ontology decision, not a mapping
tweak): where an SP demands a calculation procedure whose formula operates on
distinctly-defined operands, mint ONE procedure concept and ONE concept per
distinctly-taught operand definition, and emit one DEFINITIONAL_DEPENDENCY
prerequisite per operand; same-anchor multiplicity is expected and correct.
Directly applicable ahead to 1.34C (concentration vs amount/volume operands)
and every future formula-driven SP.

A future merge remains an operator-only identity decision, recorded on the
review sheet with nodes re-versioned.
```

| **operator ratification** | ______ (RATIFY / RATIFY_WITH_MODIFICATION / REJECT / DEFER) — record in `c11_review_verdicts.yaml` row OD-1 |

### OD-2 — Incidental terminology is not instructional evidence (operator rule)

**STATUS: PENDING OPERATOR RATIFICATION**

- Provenance: The verbatim rule is operator-issued (recorded with the HELD-13 REJECT, session 41). Its codification as a STANDING evidence-admissibility rule for the expansion round is agent-proposed (session 41, C11_ARCHITECTURE §20). The codification — not the rule's wording — awaits ratification.
- Effect if ratified: Becomes a standing expansion-round rule: IMPLICIT_USE evidence alone can never ground promotion; quarantine-or-abstain per FC-1. Affects all future batches' evidence bar.
- Recorded ruling (verbatim, C11_ARCHITECTURE.md §20):

```markdown
### OD-2 — Incidental terminology is not instructional evidence (operator rule)

Operator ruling, recorded verbatim with the REJECT of
`4CH1-PR-03 REQUIRES_PREREQUISITE 4CH1-CON-MOLE` (preserved as rejected
candidate HELD-13, session 41):

> "Do not treat table labels or incidental terminology as instructional
> evidence."

Codified effect: IMPLICIT_USE evidence (table-row labels, incidental
terminology, unnamed concept use) can never ground promotion of an edge on
its own. Such candidates are quarantined (REVIEW_REQUIRED) or abstained
(HELD) per the FC-1 policy (§19); promotion of any implicit-use edge requires
the operator to explicitly accept the weakness. This upgrades the §6
derivation cap (IMPLICIT_USE caps at medium) from a confidence statement to
an operator-confirmed evidence-admissibility rule for the expansion round.

Rulings pending operator input: none currently queued beyond the two PENDING
medium-confidence presentations (MOLAR-GAS-VOL EXPLAINED_BY AVOGADRO-LAW;
MIS-EQ-SUBSCRIPT REMEDIATED_BY CONSERVATION-MASS — see
C11_OPERATOR_DECISIONS.md).
```

| **operator ratification** | ______ (RATIFY / RATIFY_WITH_MODIFICATION / REJECT / DEFER) — record in `c11_review_verdicts.yaml` row OD-2 |

---

## 7. Alias audit — `maximum yield` (concept alias NOT modified)

### 7.1 What the data actually says (counter-confirmation of the session-42 counter-audit)

- `scripts/c11_pilot_decisions.yaml` → `aliases: [maximum yield]`
- `graph/concepts.yaml` → `- maximum yield`
- No committed data revision — `e218259`, `4eba8ea`, `4ac4a82`, `3b70dde` — contains the string `aximum yield`. **The data corruption reported in session-41's defect record never existed in the store.**
- The erroneous `aximum yield` text existed only in report artifacts (`C11_OPERATOR_DECISIONS.md`/`.json`, `C11_S16_GATE_REPORT.md`) and one renderer literal — **report/data drift, corrected this session** (the reports now describe the store byte-accurately; see §10).

### 7.2 The real question: is the alias evidenced?

- The phrase **`maximum yield` occurs 0 times** in the pilot corpus (10 notes, the 12 spec-point texts, 2 pinned mark schemes) and 0 times in the full 112-note markdown corpus → **unevidenced as a verbatim phrase**.
- The word `maximum` occurs in the pilot corpus only here:

  - `Reacting mass calculations - IGCSE Chemistry Revision Notes.`: …pose as shown in the equation below. 2Al2O3 ⟶ 4Al + 3O2 Calculate the maximum possible mass of aluminium, in tonnes, that can be produced from 51 tonnes of alum…
  - `Reacting mass calculations - IGCSE Chemistry Revision Notes.`: …Calculate the mass... - Calculate the minimum mass... - Calculate the maximum mass... - As long as you are consistent, it doesn't matter whether you work in gra…
  - `Investigating metal oxide formulas - IGCSE Revision Notes.md`: …5. Continue heating until the mass of the crucible remains constant (maximum mass), indicating that the reaction is complete 6. Measure the mass of the crucible…

The Reacting-mass occurrences are the theoretical-yield **concept** phrased without the word 'yield' (instructional worked-example text, not a table label — so OD-2 does not directly forbid them); the metal-oxide and solubility occurrences are different senses entirely. The counter-audit's cited phrase 'Maximum amount of product possible' was itself an imprecise paraphrase — it appears nowhere in the markdown corpus or the pinned extractions; this section is the byte-true record.

### 7.3 The alias table at a glance — 25 verbatim / 4 morphological variant / 18 unevidenced (of 47)

| node | alias | status | evidence |
|---|---|---|---|
| `4CH1-CON-EQ-WORD` | word equations | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Writing chemical equations - IGCSE Chemistry Revision Notes.md; SPEC (12 pilot spec points) |
| `4CH1-CON-EQ-SYMBOL` | symbol equation | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Writing chemical equations - IGCSE Chemistry Revision Notes.md; Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-EQ-SYMBOL` | chemical equation | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-EQ-SYMBOL` | balanced equation | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md; Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate percentage yield - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-EQ-SYMBOL` | balancing equations | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Writing chemical equations - IGCSE Chemistry Revision Notes.md; Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-EQ-STATE-SYM` | state symbol | VARIANT | 'state symbols' @ Writing chemical equations - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-CONSERVATION-MASS` | conservation of mass | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Writing chemical equations - IGCSE Chemistry Revision Notes.md; Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md |
| `4CH1-CON-AR` | relative atomic mass | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md; Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-AR` | Ar | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md; Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-MR` | relative molecular mass | UNEVIDENCED | — |
| `4CH1-CON-MR` | relative formula mass | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md; Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md |
| `4CH1-CON-MR` | Mr | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md; Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-MOLE` | amount of substance | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Solution concentration - IGCSE Chemistry Revision Notes.md; SPEC (12 pilot spec points) |
| `4CH1-CON-MOLE` | chemical amount | VARIANT | 'chemical amounts' @ Calculating moles and mass - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-MOLE` | mol | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md; Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Solution concentration - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-AVOGADRO-CONST` | Avogadro's constant | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-MOLAR-MASS` | mass of 1 mole | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-MOLE-MASS-CONV` | converting between moles and grams | VARIANT | 'convert between moles and grams' @ Calculating moles and mass - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-MOLE-MASS-CONV` | moles and mass calculations | UNEVIDENCED | — |
| `4CH1-CON-MOLAR-RATIO` | mole ratio | UNEVIDENCED | — |
| `4CH1-CON-MOLAR-RATIO` | ratio of amounts | UNEVIDENCED | — |
| `4CH1-CON-REACTING-MASS` | calculating reacting masses | UNEVIDENCED | — |
| `4CH1-CON-REACTING-MASS` | mass calculations from equations | UNEVIDENCED | — |
| `4CH1-CON-YIELD` | actual yield | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate percentage yield - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-YIELD` | yield of a reaction | UNEVIDENCED | — |
| `4CH1-CON-THEOR-YIELD` | maximum yield | UNEVIDENCED | — |
| `4CH1-CON-PERCENT-YIELD` | percentage yield calculation | UNEVIDENCED | — |
| `4CH1-CON-YIELD-FACTORS` | reasons for less than 100 percent yield | UNEVIDENCED | — |
| `4CH1-CON-YIELD-FACTORS` | yield losses | UNEVIDENCED | — |
| `4CH1-CON-EMPIRICAL-FORMULA` | simplest whole number ratio formula | UNEVIDENCED | — |
| `4CH1-CON-EMP-MOL-CALC` | empirical formula calculation | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md |
| `4CH1-CON-EMP-MOL-CALC` | molecular formula calculation | UNEVIDENCED | — |
| `4CH1-CON-EMP-MOL-CALC` | deducing formulae of hydrated salts | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md |
| `4CH1-CON-EXP-FORMULA-DEDUCTION` | deducing formulae by experiment | UNEVIDENCED | — |
| `4CH1-CON-EXP-FORMULA-DEDUCTION` | formula from mass measurements | UNEVIDENCED | — |
| `4CH1-CON-WATER-CRYST` | hydrated salt | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md; Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Simple compound formulae - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-WATER-CRYST` | water of crystallisation | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md; Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Simple compound formulae - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-CONCENTRATION` | concentration | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Solution concentration - IGCSE Chemistry Revision Notes.md; scripts/c11_evidence/CFEC1_MS_P1.txt |
| `4CH1-CON-CONC-CALC` | concentration calculations | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Solution concentration - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-CONC-CALC` | amount of substance from concentration | UNEVIDENCED | — |
| `4CH1-CON-VOL-CONVERSION` | converting cm3 to dm3 | VARIANT | 'convert cm3 to dm3' @ Solution concentration - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-MOLAR-GAS-VOL` | molar volume | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md; SPEC (12 pilot spec points) |
| `4CH1-CON-MOLAR-GAS-VOL` | molar gas volume | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md |
| `4CH1-CON-GAS-VOL-CALC` | calculating gas volumes | UNEVIDENCED | — |
| `4CH1-CON-GAS-VOL-CALC` | converting moles into volumes | VERBATIM | Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md |
| `4CH1-MIS-EQ-SUBSCRIPT` | changing formula subscripts to balance | UNEVIDENCED | — |
| `4CH1-MIS-CONC-UNIT` | failing to divide by 1000 | VERBATIM | scripts/c11_evidence/CFEC2_MS_P1.txt |

**Policy question for the operator** (one ruling covers the table): must aliases carry verbatim corpus evidence, or are they retrieval-oriented paraphrases exempt from the evidence discipline? Most unevidenced aliases are transparent paraphrases of the node title ('calculating gas volumes' ~ *Gas volume calculation*); **`maximum yield` is the special case** — a foreign synonym of the *Theoretical yield* title with corpus support only for the concept, never the phrase. Disposition options: DROP / RE-EVIDENCE (ground on 'maximum possible mass') / KEEP (retrieval-exempt) / RENAME (note: 'maximum mass' itself is ambiguous — the metal-oxide note uses it for crucible constant mass). Record in `c11_review_verdicts.yaml`: `alias_policy` + the `maximum yield` row.

**No alias was modified in this session** — the decision record and `graph/concepts.yaml` are byte-identical to `3b70dde`.

---

## 8. Quantified review reduction

| population | groupable (class/bulk) | genuine human semantic judgment |
|---|---|---|
| 31 edges | 28 (26 likely-safe bulk + 2 FC-3 under ONE OD-1 ruling) | 3 (1 granularity + 2 PENDING, already presented 10-field) |
| 29 nodes | 27 (bulk; 22 clean + 5 one-line notes) | 2 (the yield merge pair — governed by OD-1) |
| 13 held/rejected | 13 preserved decisions, 0 reopened | 0 (informational) |

Distributions (machine-countable in the JSON):

```json
{
  "edges": {
    "LIKELY_SAFE": 25,
    "LIKELY_SAFE (transitively-reachable; \u00a719 semantic-distinctness precedent \u2014 pass-2 addressed the pair)": 1,
    "LIKELY_AMBIGUOUS (granularity note)": 1,
    "FC-3 (OD-1-linked)": 2,
    "FC-1+FC-2 (PENDING judgment)": 2
  },
  "nodes": {
    "LIKELY_SAFE": 22,
    "LIKELY_SAFE (pass-2 note)": 5,
    "FC-2 identity (OD-1-linked)": 2
  }
}
```

**Decision load:** Per-row surface 60 verdicts (31 edges + 29 nodes) reduces to ~7 actual decisions: (1) OD-1 ratification [covers 2 nodes + 2 edges], (2) OD-2 ratification, (3–4) the two PENDING judgments [already presented 10-field], (5) the granularity edge, (6) the alias-evidence policy, (7) the 'maximum yield' disposition — plus bulk CONFIRM/REJECT commands over the pre-triaged groups.

---

## 9. Batch forecasting instrumentation

Instrument: `scripts/c11_batch_forecast.py` → `graph/reports/C11_BATCH_FORECAST.json` (written this session; read-only with respect to the graph). The pilot is batch 0; each authorized §16 batch appends a `future_batch_records` entry so forecast error, rates, and false-positive categories are measured, not assumed.

| metric | §16 model prediction (pilot's 12 SPs) | pilot actual | error |
|---|---|---|---|
| nodes | 28.8 | 29 | +0.2 (+0.7%) |
| authored_edges | 33.0 | 32 | -1.0 (-3.0%) |
| held_candidates | 12.0 | 13 | +1.0 (+8.3%) |

| rate | pilot value | formula |
|---|---|---|
| held_rate | 0.2889 | held_candidates / (authored_edges + held_candidates) |
| rejection_rate | 0.0444 | rejected_candidates / (authored_edges + held_candidates) |
| promotion_rate | 0.0 | promoted / total_edges |
| operator_review_rate | 0.9836 | operator-verdict-requiring rows / (authored_edges + nodes) |
| quarantine_rate | 0.2667 | (REVIEW_REQUIRED edges + held candidates) / (authored_edges + held_candidates) |

False-positive categories tracked (pilot history): FP-1 anchor-direction overstatement; FP-2 split-artifact multiplicity (same-anchor operand pairs); FP-3 granularity mismatch; FP-4 implicit-use emission (OD-2 class); FP-5 report/data drift (process-level); FP-6 taxonomy coverage gap (report-level).

---

## 10. Zero-action attestation

- Promotions record `scripts/c11_promotions.yaml`: **unchanged, 0 entries** — nothing promoted, nothing ratified.
- `graph/*.yaml`: **byte-identical to `3b70dde`** (git diff empty; the generator was not re-run to write).
- §16: **not opened**; expansion: **not begun**; DB writes: **none**.
- Concept alias `maximum yield`: **untouched** (§7).
- Store-adjacent writes this session: this package (new files), `C11_BATCH_FORECAST.json` (new), the verdict template (new), and the phantom-text corrections in `C11_OPERATOR_DECISIONS.md`/`.json` + `C11_S16_GATE_REPORT.md` + the renderer literal — report text only, describing the store byte-accurately.

