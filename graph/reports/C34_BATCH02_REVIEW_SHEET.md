# T-C34 K2-C-2 — Batch B02 Review Sheet — Concept / Prerequisite Graph (igcse-maths-a, 4MA1 Higher)

Slice 4MA1-1.2E–1.4B (global_order 13–24 of the ratified K1 store; a MIXED-TIER slice — 9 Foundation rows plus the first three Higher rows 1.3A/1.4A/1.4B; spanning the 1.2 tail, 1.3 complete and the 1.4 head; subsection titles null by design, never invented) · generated 2026-10-01 · decision record `scripts/c34_maths_a_batch02_decisions.yaml` (pass 1: `c34-k2c-batch-02`) · adversarial pass 2: `scripts/c34_maths_a_batch02_review_pass2.yaml` · commissioning: `scripts/c34_maths_a_batch02_authorization.yaml` (the operator's **K2-C-2** directive, 2026-10-01 — gate K2-C-2 of the C31 §8 sequence) · coverage substrate: the T-C32 K2-A notes join (`Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json`)

**NOTHING in this batch is authoritative.** All 14 nodes (12 concept + 2 misconception) / 10 authored edges are AI_SUGGESTED (SUGGESTED). HUMAN_VALIDATED is reachable only by your promotion command via the §18 pathway after your verdicts are recorded. **Zero promotions exist** — and the B01 packet (T-C33) likewise awaits your verdicts, so the maths-a graph dir still carries exactly the 5 K1 stores and nothing has grown from either batch. This sheet is the batch's operator gate: record verdicts against §2/§2a/§3/§4 below (a `c34_maths_a_batch02_verdicts.yaml` template lands with the verdict session); a later session encodes and applies them.

How to review: for each row check the quoted evidence actually appears in the cited file and actually says what the record claims; then rule on the relation CLASS and direction, not just existence. Machine state: preverify 32/32 PASS, quote probe 61/61 anchors verbatim (26 NOTE / 21 SPEC / 14 MARK_SCHEME), term audit 63 terms audited (8 matches — all in-slice except one new future code), the maths-a graph dir still carries exactly the 5 K1 stores (nothing has grown). The **unjoined-corpus negative control** holds at second-batch strength: every NOTE citation is one of the 11 join-carried notes, pair-backed at its SP (nodes) or at an endpoint SP (edges — a strengthening over B01); the two join-carried-but-UNCITED pages are recorded in the census with dispositions, not padded citations; the corpus's nearby unjoined pages (mixed-numbers-and-improper-fractions — itself joined to B01's 1.2B — hcf-and-lcm, prime-factor-decomposition, laws-of-indices, standard-form, the percentages pages, et al.) are NOT cited anywhere. TWO misconceptions minted (§2a) — the first maths-a mints, on the surds MS Q12 20(a)/(b) documentation (the chemistry MS-Reject contract's mint condition); the mint-vs-exam-trivia question is operator-reserved (B02-ID-03). NO pass-2 finding required re-authoring (FP-B02-1..3 / FN-B02-1..3 are recorded questions and resolutions).

## 1. Totals & second-pass agreement

| | concept nodes | misconception nodes | authored edges | held | derived PART_OF (at apply) |
|---|---|---|---|---|---|
| pass-1 (extraction) | 12 | 2 | 10 | 8 | 14 |
| pass-2 verdicts | 12 CONFIRM | 2 CONFIRM | 10 CONFIRM · 0 HOLD · 0 REJECT | 8/8 AGREE | — |

Raw agreement (NOT κ — single human rater, the architecture §12 convention): nodes 14/14 = 100%; edges 10/10 = 100%; pass-1 quarantined 0 edges as REVIEW_REQUIRED — every doubt was held or resolved on explicit evidence. **Zero pass-2 findings required re-authoring; zero demotions.**

Forecast calibration (the C31 §5 adjusted forecast: 1.0 node / 1.6 edges per SP): B02 runs 12 concept nodes / 6 REQUIRES_PREREQUISITE edges (+2 misconception nodes and their 4 WAP/remediation edges) over 12 SPs = 1.00 node / 0.50 prerequisite edge per SP. The node rate is on forecast. The edge shortfall against 1.6 is **structural, not thin coverage**: the registry is still absent (B01 authored-to-gate, not applied), so the cross-batch boundary-edge class has no targets to reach — six of the eight held candidates (§4) are exactly those would-be edges, quoted with their evidence (three to B01 nodes, three to future-batch families). The 14 derived PART_OF rows materialize at the §18 apply step (one per node attachment, SPEC_VERBATIM derivation), not at this gate.

## 2. Concept nodes (12) — the diff-review bundle

| # | code | title | attaches to (role) | conf | evidence (kind → quote) | pass-2 | operator |
|---|---|---|---|---|---|---|---|
| 1 | `4MA1-CON-EXPRESSING-NUMBERS-AS-FRACTIONS` | Expressing one number as a fraction of another | 4MA1-1.2E (CORE) | high | SPEC: “express a given number as a fraction of another number” | CONFIRM | ☐ |
| 2 | `4MA1-CON-ADDING-SUBTRACTING-FRACTIONS` | Adding and subtracting fractions (and mixed numbers) via common denominators | 4MA1-1.2F (CORE) | high | NOTE: “Find the lowest common denominator” · NOTE: “Add (or subtract) the numerators and write this over a single de…” · NOTE: “Convert any mixed numbers into improper fractions” · SPEC: “use common denominators to add and subtract fractions and mixed …” · MARK_SCHEME: “Rewrite both fractions with a common denominator, in this case 1…” · MARK_SCHEME: “Find a common denominator (common multiple of 6 and 3)” | CONFIRM | ☐ |
| 3 | `4MA1-CON-FRACTION-TO-DECIMAL-OR-PERCENTAGE` | Converting a fraction to a decimal or a percentage | 4MA1-1.2G (CORE) | high | NOTE: “Fractions written over powers of 10 are quicker” · NOTE: “Change fractions into decimals then multiply by 100” · SPEC: “convert a fraction to a decimal or a percentage” | CONFIRM | ☐ |
| 4 | `4MA1-CON-UNIT-FRACTIONS-AS-INVERSES` | Unit fractions as multiplicative inverses | 4MA1-1.2H (CORE) | high | SPEC: “understand and use unit fractions as multiplicative inverses” | CONFIRM | ☐ |
| 5 | `4MA1-CON-MULTIPLYING-DIVIDING-FRACTIONS` | Multiplying and dividing fractions (and mixed numbers) | 4MA1-1.2I (CORE) | high | NOTE: “Always convert mixed numbers into improper fractions before mult…” · NOTE: “The 'flipped' fraction is called a reciprocal fraction” · NOTE: “To find an equivalent fraction, multiply the top and bottom of a…” · SPEC: “multiply and divide fractions and mixed numbers” | CONFIRM | ☐ |
| 6 | `4MA1-CON-RECURRING-DECIMALS-TO-FRACTIONS` | Converting recurring decimals into fractions (the algebraic method) | 4MA1-1.3A (CORE) | high | NOTE: “Recurring decimals are rational numbers, they are not irrational” · NOTE: “They can be written as fractions” · NOTE: “Multiply both sides by 10 repeatedly until two lines have the sa…” · NOTE: “Subtract the two lines which have matching recurring decimal par…” · MARK_SCHEME: “Let $x$ be the recurring decimal” · MARK_SCHEME: “These two equations both contain the trail of recurring 5s, so w…” · SPEC: “convert recurring decimals into fractions” | CONFIRM | ☐ |
| 7 | `4MA1-CON-DECIMAL-PLACE-VALUE` | Decimal place value (positional value of digits across the decimal point) | 4MA1-1.3B (CORE) | high | SPEC: “understand place value” | CONFIRM | ☐ |
| 8 | `4MA1-CON-ORDERING-DECIMALS` | Ordering decimals (comparison by place-value columns) | 4MA1-1.3C (CORE) | high | NOTE: “Write them all with 3 decimal places to determine the order” · MARK_SCHEME: “To compare the numbers, we could write them in a column and exam…” · SPEC: “order decimals” | CONFIRM | ☐ |
| 9 | `4MA1-CON-DECIMAL-TO-FRACTION-OR-PERCENTAGE` | Converting a decimal to a fraction or a percentage | 4MA1-1.3D (CORE) | high | SPEC: “convert a decimal to a fraction or a percentage” | CONFIRM | ☐ |
| 10 | `4MA1-CON-TERMINATING-DECIMALS-ARE-FRACTIONS` | Terminating decimals are fractions (the recognition) | 4MA1-1.3E (CORE) | high | SPEC: “recognise that a terminating decimal is a fraction” | CONFIRM | ☐ |
| 11 | `4MA1-CON-MEANING-OF-SURDS` | The meaning of surds (square roots of non-square integers, exact form) | 4MA1-1.4A (CORE) | high | NOTE: “A surd is the square root of a non-square integer” · NOTE: “Using surds lets you leave answers in exact form” · NOTE: “Roots are the reverse of powers” · NOTE: “Negative numbers do not have a real square root” · SPEC: “understand the meaning of surds” | CONFIRM | ☐ |
| 12 | `4MA1-CON-MANIPULATING-SURDS` | Manipulating surds (simplify, collect, rationalise denominators) | 4MA1-1.4B (CORE) | high | NOTE: “The fraction can be rewritten as an equivalent fraction, but wit…” · NOTE: “Multiply the top and bottom of the fraction by the surd on the d…” · MARK_SCHEME: “Make the denominator rational (by multiplying top-and-bottom by …” · SPEC: “manipulate surds, including rationalising a denominator” | CONFIRM | ☐ |

Identity-policy notes (split-first; merges are operator-only): **B02-ID-01** authors the 1.3B row as its OWN node (`4MA1-CON-DECIMAL-PLACE-VALUE`) although its wording is byte-identical to 1.1B's and B01 authored a place-value node CORE at 1.1B — the decimal context is the store's own 1.3 subtopic placement, and the eventual co-identity/merge is reserved to your verdict. **B02-ID-02** authors the mirror conversions 1.2G/1.3D as TWO nodes (the converting-between-fdp evidence is pair-locked to 1.2G); any single FDP-conversion family merge is yours to rule. The five spec-text-only nodes (expressing-numbers-as-fractions, unit-fractions-as-inverses, decimal-place-value, decimal-to-fraction-or-percentage, terminating-decimals) author from the ratified wording alone per the C31 §3 uncovered-span rule.

## 2a. Misconception nodes (2) — the FIRST maths-a mints

| # | code | title | rides | evidence (kind → quote) | pass-2 | operator |
|---|---|---|---|---|---|---|
| 1 | `4MA1-MIS-SURD-FACTOR-SWAP` | Simplifying √12 as 3√2 (swapping which square factor's root emerges) | 4MA1-1.4B (CORE) | MARK_SCHEME: “She used √12 = 3√2 in the numerator, but √12 = 2√3” · MARK_SCHEME: “√12 = 2√3, not 3√2” | CONFIRM | ☐ |
| 2 | `4MA1-MIS-CONJUGATE-EXPANSION-SIGN` | Dropping the negative on the final term when expanding the conjugate-pair denominator | 4MA1-1.4B (CORE) | MARK_SCHEME: “He expanded the denominator incorrectly (the last term should be…” · MARK_SCHEME: “The last term when expanding the denominator should be -3, not +…” | CONFIRM | ☐ |

Both mints ride 4MA1-1.4B — the surds manipulation surface where the surds MS Q12 rows document the classes. Each carries a WRONG_ANSWER_PATTERN edge and a REMEDIATED_BY edge into `4MA1-CON-MANIPULATING-SURDS` (§3, rows 7–10) — the remediation evidence is the MS's own corrected form in the same row; the note-side corrective surfaces are pair-locked to 1.4A (simplifying-surds) and recorded in the edge derivation notes, not forced past the pair discipline. **B02-ID-03** reserves the mint-vs-exam-trivia ruling to you (the chemistry B10-ID-05 precedent; B01's abstention record stands as the counterfactual).

## 3. Authored semantic edges (10)

| # | edge | conf | derivation | evidence (kind → quote) | pass-2 | operator |
|---|---|---|---|---|---|---|
| 1 | `4MA1-CON-ORDERING-DECIMALS REQUIRES_PREREQUISITE 4MA1-CON-DECIMAL-PLACE-VALUE` | high | USED_WITHOUT_RETEACHING | NOTE: “Write them all with 3 decimal places to determine the order” · SPEC: “understand place value” · SPEC: “order decimals” | CONFIRM | ☐ |
| 2 | `4MA1-CON-TERMINATING-DECIMALS-ARE-FRACTIONS REQUIRES_PREREQUISITE 4MA1-CON-FRACTION-TO-DECIMAL-OR-PERCENTAGE` | high | USED_WITHOUT_RETEACHING | NOTE: “If it has one decimal place, write the digits over 10” · SPEC: “recognise that a terminating decimal is a fraction” | CONFIRM | ☐ |
| 3 | `4MA1-CON-RECURRING-DECIMALS-TO-FRACTIONS REQUIRES_PREREQUISITE 4MA1-CON-FRACTION-TO-DECIMAL-OR-PERCENTAGE` | high | USED_WITHOUT_RETEACHING | NOTE: “Learn simple recurring decimals as fractions” · NOTE: “They can be written as fractions” | CONFIRM | ☐ |
| 4 | `4MA1-CON-MULTIPLYING-DIVIDING-FRACTIONS REQUIRES_PREREQUISITE 4MA1-CON-UNIT-FRACTIONS-AS-INVERSES` | high | USED_WITHOUT_RETEACHING | NOTE: “When dividing fractions you are multiplying by the reciprocal.” · SPEC: “understand and use unit fractions as multiplicative inverses” | CONFIRM | ☐ |
| 5 | `4MA1-CON-MANIPULATING-SURDS REQUIRES_PREREQUISITE 4MA1-CON-MEANING-OF-SURDS` | high | EXPLICIT_TEACH_SEQUENCE | NOTE: “You can multiply numbers under square roots together” · SPEC: “understand the meaning of surds” · SPEC: “manipulate surds, including rationalising a denominator” | CONFIRM | ☐ |
| 6 | `4MA1-CON-FRACTION-TO-DECIMAL-OR-PERCENTAGE REQUIRES_PREREQUISITE 4MA1-CON-DECIMAL-PLACE-VALUE` | high | USED_WITHOUT_RETEACHING | NOTE: “Divide by 100 (move digits two places to the right)” · SPEC: “understand place value” | CONFIRM | ☐ |
| 7 | `4MA1-MIS-SURD-FACTOR-SWAP WRONG_ANSWER_PATTERN 4MA1-CON-MANIPULATING-SURDS` | high | ASSESSMENT_DOCUMENTED | MARK_SCHEME: “She used √12 = 3√2 in the numerator, but √12 = 2√3” | CONFIRM | ☐ |
| 8 | `4MA1-MIS-CONJUGATE-EXPANSION-SIGN WRONG_ANSWER_PATTERN 4MA1-CON-MANIPULATING-SURDS` | high | ASSESSMENT_DOCUMENTED | MARK_SCHEME: “He expanded the denominator incorrectly (the last term should be…” | CONFIRM | ☐ |
| 9 | `4MA1-MIS-SURD-FACTOR-SWAP REMEDIATED_BY 4MA1-CON-MANIPULATING-SURDS` | high | ASSESSMENT_DOCUMENTED | MARK_SCHEME: “√12 = 2√3, not 3√2” | CONFIRM | ☐ |
| 10 | `4MA1-MIS-CONJUGATE-EXPANSION-SIGN REMEDIATED_BY 4MA1-CON-MANIPULATING-SURDS` | high | ASSESSMENT_DOCUMENTED | MARK_SCHEME: “The last term when expanding the denominator should be -3, not +…” | CONFIRM | ☐ |

Rows 1–6 are in-slice REQUIRES_PREREQUISITE rows — the teaching sequence the notes and the ratified wordings themselves establish (ordering decimals and the conversions on decimal place value; terminating-recognition and the recurring method on the conversion fluency; the division procedure on the unit-fraction inverse; surds manipulation on surds meaning). Rows 7–8 are the two documented WRONG_ANSWER_PATTERNs and rows 9–10 their REMEDIATED_BY pairs (the B1-E-25 pattern: remediation target = WAP target). NO REQUIRES_PREREQUISITE edge reaches outside the batch — there is no registry to reach into, and the cross-batch candidates are HELD (§4) with the B01-inherited map as their ruling starting point.

## 4. Held candidates (8) — the abstention record / held-quarantine state

| id | candidate | failure class / reason | pass-2 | operator |
|---|---|---|---|---|
| B02-H-01 | REQUIRES_PREREQUISITE(4MA1-CON-ADDING-SUBTRACTING-FRACTIONS, 4MA1-CON-COMMON-DENOMINATORS [B01 node, CORE at 4… | CROSS-BATCH-TARGET-UNPROMOTED — the natural target is B01's common-denominators node, which is SUGGESTED and unapplied (no maths-a concepts store exists), so the edge has no registry node to resolve to; authoring it woul… | AGREE | ☐ |
| B02-H-02 | REQUIRES_PREREQUISITE(4MA1-CON-ADDING-SUBTRACTING-FRACTIONS, 4MA1-CON-MIXED-NUMBERS-AND-IMPROPER-FRACTIONS [B0… | CROSS-BATCH-TARGET-UNPROMOTED — the target is B01's mixed-numbers node (SUGGESTED, unapplied); no registry node exists. Held; revisit at the post-promotion boundary ruling. | AGREE | ☐ |
| B02-H-03 | REQUIRES_PREREQUISITE(4MA1-CON-MULTIPLYING-DIVIDING-FRACTIONS, 4MA1-CON-EQUIVALENT-FRACTIONS [B01 node, CORE a… | CROSS-BATCH-TARGET-UNPROMOTED — the target is B01's equivalent-fractions node (SUGGESTED, unapplied). Held; revisit at the post-promotion boundary ruling. | AGREE | ☐ |
| B02-H-04 | REQUIRES_PREREQUISITE(4MA1-CON-RECURRING-DECIMALS-TO-FRACTIONS, <algebra toolkit letters-for-unknowns node — f… | CROSS-BATCH-TARGET-FUTURE-BATCH — the target SP family sits in the S2 algebra toolkit, not yet batched; no node exists to resolve to. The algebraic-notation page's contribution is recorded HERE rather than padded onto th… | AGREE | ☐ |
| B02-H-05 | REQUIRES_PREREQUISITE(4MA1-CON-MEANING-OF-SURDS, <powers-and-roots node — future batch, 1.4C+>) | CROSS-BATCH-TARGET-FUTURE-BATCH — the powers/roots SP family (1.4C..) is outside this slice and unbatched; the page itself is correctly cited on the 1.4A node (pair-backed at 1.4A), but the prerequisite EDGE has no node … | AGREE | ☐ |
| B02-H-06 | REQUIRES_PREREQUISITE(4MA1-CON-MANIPULATING-SURDS, <algebraic expansion node — future batch, S2>) | CROSS-BATCH-TARGET-FUTURE-BATCH — the bracket-expansion SP family sits in S2, unbatched; the rationalising procedure cites the expansion mechanics it presupposes but no node exists to resolve to. Held; revisit when the S… | AGREE | ☐ |
| B02-H-07 | 4MA1-MIS-ADDING-DENOMINATORS (the add-the-denominators wrong-answer class at 1.2F/1.2I, carried forward from B… | NO-MS-REJECT-DOCUMENTATION — the chemistry contract mints misconceptions ONLY on mark-scheme-documented wrong-answer classes; the class is real (the note warns against it) but unevidenced at MS level in this corpus. Held… | AGREE | ☐ |
| B02-H-08 | 4MA1-CON-UNIT-FRACTIONS-AS-INVERSES with NOTE evidence from basic-fractions.md (the richer node shape) | COVERAGE-UNJOINED-SUBSTRATE — authoring the node with that content as evidence would assert a note↔SP relevance the operator-worked substrate does not carry (the B01-H-01 class); the authored node carries the ratified wo… | AGREE | ☐ |

The held-quarantine discipline continues from B01: held rows carry failure classes — the batch adds CROSS-BATCH-TARGET-UNPROMOTED and CROSS-BATCH-TARGET-FUTURE-BATCH (the boundary classes the empty registry makes structural) to B01's COVERAGE-UNJOINED-SUBSTRATE, SPEC-ONLY-SURFACE, NO-MS-REJECT-DOCUMENTATION, AVAILABLE-BUT-SURFACE-MINIMAL vocabulary — and are revisit-able at the verdict or at later gates, never silently dropped, never force-authored. The **B01 quarantine (B01-H-01..05) is inherited untouched** and rules alongside this one at the verdict session. B02-H-07 carries B01-H-04's class forward with its new note-side evidence (the joined note's own "Do not add the denominators" warning — still no MS documentation, still held).

## 5. Coverage profile (the C31 §3 standing per-batch statement)

| measure | value |
|---|---|
| slice SPs | 12 (global_order 13–24) |
| tier mix | 9 Foundation-applicability + 3 Higher (4MA1-1.3A, 4MA1-1.4A, 4MA1-1.4B — the first Higher rows of the ratified program) |
| notes-joined SPs (NOTE evidence possible) | 7 (4MA1-1.2F, 4MA1-1.2G, 4MA1-1.2I, 4MA1-1.3A, 4MA1-1.3C, 4MA1-1.4A, 4MA1-1.4B) — 13 join rows over 11 distinct note files |
| spec-text-only SPs (SPEC evidence only) | 5 (4MA1-1.2E, 4MA1-1.2H, 4MA1-1.3B, 4MA1-1.3D, 4MA1-1.3E) |
| MS-evidenced SPs (MARK_SCHEME evidence) | 4 (4MA1-1.2F via the fractions topic MS; 4MA1-1.3A and 4MA1-1.3C via the FDP topic MS; 4MA1-1.4B via the surds topic MS — a PARTIAL MS-documentation shape, the chemistry batch-3/4/10 precedent) |
| join-carried but uncited pages | 2 — the uncited-join census records each with its disposition (see the machine-state appendix) |
| damage-flagged rows in the slice | 0 (the 8 math-fragment-assembly rows live outside this slice) |
| misconceptions minted | 2 — the surds MS Q12 20(a)/(b) documented classes (the first maths-a mints; B01 minted zero on the same contract) |
| practicals | none (the maths-a practicals store is 0-row by design) |

## 6. Verdict instructions

Rule per row on §2 (12 concept nodes), §2a (2 misconception nodes — including the B02-ID-03 mint-vs-trivia ruling), §3 (10 edges) and §4 (8 held), plus the three identity decisions (B02-ID-01 co-identity of the place-value rows; B02-ID-02 the 1.2G/1.3D mirror pair; B02-ID-03 the mints). A `scripts/c34_maths_a_batch02_verdicts.yaml` template accompanies the verdict session; verdicts encode through the intake-conformance check, the §18 apply step then (and only then) materializes/grows the maths-a concepts/concept_edges/spec_command_kinds stores with exactly the promoted rows — B01's and B02's quarantines rule together there. Nothing here is live until your verdicts land.

## 7. Machine-state appendix

| artifact | sha256_16 |
|---|---|
| decisions record | 5c548f576ba141f0 |
| pass-2 record | e361a7e6ca523cfe |
| commissioning record | 8bed477924bf458c |
| review sheet (this file) | deterministic rebuild — the battery byte-compares a fresh build against the committed bytes |

Uncited-join census (the negative control's transparency annex):

- SME-RevisionNotes/igcse-maths-a-18-higher/notes/1-numbers-and-the-number-system/number-toolkit/negative-numbers.md (joined to 4MA1-1.4A; signed-arithmetic content does not state the surds demand — disposition on the 1.4A node's derivation notes)
- SME-RevisionNotes/igcse-maths-a-18-higher/notes/2-equations-formulae-and-identities/algebra-toolkit/algebraic-notation.md (joined to 4MA1-1.3A; letters-for-unknowns content recorded on the held B02-H-04 row instead)

Boundary map for B03.. (the term audit's non-slice matches, 4 codes): 4MA1-1.4D, 4MA1-1.4E, 4MA1-1.7A, 4MA1-1.8B — the B01-inherited codes 1.2F/1.2I/1.3B are now IN-SLICE (their nodes mint here); 1.4D/1.4E/1.7A remain future; 1.8B is this audit's new match ('decimal places' against the rounding row).

