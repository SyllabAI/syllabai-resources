# C42 — K2-B Rework, R1: T-SPEC Resolution Repair Record — igcse-maths-a (4MA1 Higher)

| | |
|---|---|
| **Task ID** | T-C42 R1 (the operator verdict round of the C42 scope, gate 1) |
| **Date** | 2026-10-02 |
| **Operator directive** | "fire R1" (2026-10-02, zai-web, inline) — arming the C42 scope's R1 stage |
| **Reviewer** | Super Z (GLM agent), operator-delegate under the fired R1 directive; the human operator retains final sign-off; per the anti-forgery rule nothing here promotes store rows (the C40 substrate stays `SUGGESTED`; the C41-promoted 73 edges are untouched) |
| **Verdict record** | `scripts/c42_repair_verdicts.yaml` (operator-owned; 45 id-level + 1 residual + 16 section rows) |
| **Amended file** | `SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json` — in place, per the T-SPEC series precedent (t_spec_7_index_repair / t_spec_8_apply) and the C31 §4.4 dated-exception path; baseline git blob `3a0b5dc48a65fb54` verified before the single write |
| **Audit** | `scripts/c42_resolution_repair_check.py` → C1–C8 ALL PASS (two-way agreement, counts, zero-drift on 176 non-surface rows, code domain, idempotency, the standing `sme_spcpt_verify.py` gate set, diff surface) |

---

## 1. The key finding: most "defective" joins were wording-tier artifacts

The R1 round's central discovery is that **the C40 fill's semantic gate compared every
chunk against the store's operative (Higher-preferred) wording alone**, while the
ratified C30 tier-dedupe ledger records, for 54 shared codes, the Foundation statement
of the same official code. Adjudicated against BOTH tier wordings, the 45 note-level
rejects split as:

| Disposition | n | Meaning |
|---|---|---|
| **AFFIRM** | 21 | the join's code was already correct — the ledger's Foundation wording matches the note verbatim (e.g. 2.2B-F *"collect like terms"*, 2.2A-F *"evaluate expressions by substituting numerical values for letters"*, 4.8A-F *"know, understand and use Pythagoras' theorem in two dimensions"*, 6.2B-F *"calculate the mean, median, mode and range for a discrete data set"*, 6.3D-F *"find probabilities from a Venn diagram"*, 4.11B-F *"use and interpret maps and scale drawings"*, 4.6B-F *"understand chord and tangent properties of circles"*, 6.1A-F *"use different methods of presenting data Pictograms, bar charts"*, 3.3B-F Cartesian-coordinates conventions, 3.3E-F midpoint, 3.3F-F conversion graphs, 3.3G-F gradient, 3.1A-F term-to-term/position-to-term, 4.11A-F similar-figure lengths, 4.10A-F names of solids, 6.1C-F/6.2C-F/6.3A-adjacent stats rows) |
| **CORRECT** | 22 | the code genuinely changes (the old row taught unrelated content at every tier) |
| **UNRESOLVED** | 2 | no canonical row teaches the note's content — the wrong code was CLEARED, never forced |

**Standing instruction for R4 (the re-gate):** the re-fill's semantic layer MUST consult
both tier wordings (store operative wording + ledger `foundation.text` per code) —
otherwise it will re-reject exactly the 21 affirmed joins and the gate can never pass.

## 2. Surface 1 — the 22 code corrections

Exchange Rates 3.4C→**1.10C** (converting between currencies, verbatim); Negative
Numbers 1.4A→**1.1C** (directed numbers in practical situations); Powers & Roots
1.4A→**1.4B** (F: squares, square roots, cubes and cube roots); Introduction to Ratios
1.7B→**1.7A** (ratio notation/simplification); Upper & Lower Bounds 1.10B→**1.8A**
(solve problems using bounds); Using a Calculator 4.5C→**1.11A** (verbatim); Algebraic
Notation 1.3A→**2.1A** (F: symbols represent numbers/variables); Formulas where Subject
Appears Twice 2.3F→**2.3A** (H: subject may appear twice, verbatim); Deciding the
Quadratic Method 2.7D→**2.7B** (formula/completing-the-square); Parallel Lines
4.1B→**3.3G** (H: equation of a parallel line — the note teaches algebra despite living
in the geometry tree); Inverse Functions 3.3I→**3.2D** (composite/inverse functions);
Trigonometric Graphs 3.3F→**3.3A** (H wording explicitly names y = sin x / cos x / tan x
graphs); Distance-Time Graphs 3.3F→**4.4F** (average speed/distance/time; 3.3A-F
recorded as the alternative); Length of a Line 3.3G→**4.8A** (F: Pythagoras in two
dimensions = the distance formula; moderate, flagged for R4); Conditional Probability
6.3B→**6.3C** (verbatim); Probability Tree Diagrams 6.1C→**6.3A** (draw and use tree
diagrams); Probabilities from Venn Diagrams 1.5E→**6.3D** (F: find probabilities from a
Venn diagram, verbatim); Interpreting Cumulative Frequency Diagrams 6.1B→**6.1C** (use
cumulative frequency diagrams); Representing Vectors as Diagrams 6.1C→**5.1A**
(magnitude and direction); Volume 4.10F→**4.10E** (prisms incl. cuboids and cylinders;
the cone/sphere tail ↔ 4.10A recorded for R4); Angles in Cyclic Quadrilaterals
4.2B→**4.6C** (clause iv, verbatim); Angles in the Same Segment 4.6A→**4.6C** (clause
iii, verbatim).

The 2 **UNRESOLVED** clearings: *Mathematical Symbols* (a general symbols glossary — no
canonical row) and *Problem Solving with Areas* (a composite real-life applications page
— no canonical row). Both carry the standing verifier's required `reason`, preserve the
prior wrong values inside `repair.prior`, and enter the allowlist note.

## 3. Surface 2 — the C32 residual

`spcpt_QWXhzVp2S3VYZdZc` ("Discrete & Continuous Data") **stays UNRESOLVED**. The
round tested the C32 scorer's recorded proposals (6.2C IQR / 6.3G / 6.1B — none teaches
data types) against the row's own PDF-verified reason ("the 4MA1 print has no standalone
discrete/continuous statement") and rejected all three. The two substrate worklist chunk
rows remain recorded-not-forced.

## 4. Surface 3 — the 16 section-level dispositions (the R3 override map)

Landed as `scripts/c42_section_overrides.yaml` (operator-owned, R3-facing; the c40 tool
will consume it fail-closed — an override naming a code outside the 188 fails the build):

| Disposition | n | Rows |
|---|---|---|
| **REATTRIBUTE** | 12 | basic-fractions §6→1.2A (simplifying fractions, verbatim); basic-percentages §2→1.6E (finding a percentage of an amount; 1.6D sibling recorded); solving-linear-inequalities §3→2.8C (number-line representation, verbatim); quadratic-graphs §4→2.2D (completing the square — the fill's 2.7B hint refined: finding a turning point is not equation-solving), §5→3.4C (differentiation on quadratics); drawing-straight-line-graphs §1→3.3I (plotting from a table), §3→3.3H (y = mx + c drawing); basic-angle-properties §4→4.2B (quadrilateral angle sum); right-angled-trigonometry §6→4.8C (F: 2D trig problems — shortest distance); surface-area §2→4.10C (cubes/cuboids/prisms), §4→4.10A (cone), §5→4.10A (sphere) |
| **RETAIN** | 4 | algebraic-roots-and-indices §0 and surface-area §0 (heading-only chunks — the semantic gate cannot verify them; a known R4 re-fill limitation to handle explicitly); surface-area §1 (generic note intro rides the note's SP per the C40 convention); averages-from-tables §2 (the mode IS 6.2B-F wording — the same artifact class as the AFFIRM set, caught by the ledger) |

## 5. The amendment in place

Every surface row gained `repair` provenance (task/round/date/disposition/prior
values/verdict ref/evidence); AFFIRM and ledger-sourced CORRECT rows additionally had
their statement re-pointed to the Foundation wording (bare `IGCSE_MATHS_A:{code}` id +
ledger `foundation.text`), so each row is self-consistent with the verdict evidence.
Top-level: `repair` block, dated `validation` clause, recomputed `counts`
(**222 ids / 216 resolved / 6 unresolved**), allowlist note extended with the two
cleared ids. Zero drift on the 176 non-surface rows (C3, byte-level); 16 legacy rows
with bare ids on Higher-store codes were noted, not touched (outside the verdict
surface).

## 6. R0 census (evidence base for the EQ-side decision)

996 EQ part references declared across the 45 ids (40/45 with parts), 1,133 raw id
occurrences in the corpus JSONs (0 ids absent). spec-links: 6 maths-a files committed;
only 1–3 anchor-id hits each, **0 wrong-code hits** — negligible direct exposure.
`s104_build_question_package.py` does not consume the resolution substrate; no maths-a
kg export exists. External consumers (core/hub RAG serving) are not audited here. The
EQ-side and spec-links refresh decisions remain the operator's, armed by this census
(`graph/reports/C42_R0_BLAST_RADIUS_CENSUS.json`).

## 7. Staleness by design (until R2/R3)

The C32 notes-join, the C40 chunk substrate and the spec-links surface are now stale
relative to the amended resolution — exactly as the C42 scope's stage sequence
prescribes; they refresh at R2 (join re-run) and R3 (substrate re-build + override
consumption), after which R4 re-gates and R5 applies. Nothing else was written this
round: chemistry, parsed canonical bundles, the Lane C stores and the C25–C41 records
are byte-untouched (C8).
