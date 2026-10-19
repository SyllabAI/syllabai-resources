# T-C11 Coverage-Gap Report — Pilot Slice 1.25–1.36

Companion to `C11_PILOT_REPORT.md` (tasking deliverable #12). Everything below
is a *known, deliberate, documented* limitation of the pilot graph — none of it
is silently papered over by graph edges.

---

## 1. The negative control: 4CH1-4.15 (zero coverage, by design)

Spec: "explain how the combustion of some impurities in hydrocarbon fuels
results in the formation of sulfur dioxide" (an EXPLAIN_HOW point).

- T-C10 state: zero validated note mappings (the round-4 rejection; the
  honest zero-coverage corpus gap).
- T-C11 state: zero concepts, zero edges, zero misconception records attached
  to 4.15.
- Corpus reality: the premise ("All these fuels contain carbon, hydrogen and
  small quantities of sulfur", Definition-of-combustion note, mapped
  4.11–4.13) and the stated consequence ("The sulfur dioxide produced from the
  combustion of fossil fuels dissolves in rainwater", Nitrogen-Oxides-&-
  Sulfur-Dioxide note, mapped 4.14/4.16) both exist — in different notes. The
  demanded causal mechanism is taught nowhere.
- Machine enforcement: attachment rule (a concept may attach to SP X only via
  SPEC wording or a note HUMAN_VALIDATED-mapped to X) + edge-anchor
  admissibility make 4.15 coverage structurally impossible. Negative tests 10
  and 11 prove both failure modes are caught.
- Remediation pathway (operator content decision, never graph-side inference):
  commission/write a corpus note teaching the impurity→SO₂ formation
  mechanism, or obtain it from the 383-page student-book OCR (crude-oil /
  atmospheric-pollution chapter), then re-run T-C10-style mapping validation
  before any 4.15 concept is minted.

## 2. Boundary concepts (cross-slice prerequisites not minted)

Real learning dependencies that point outside the pilot slice; deliberately
recorded here instead of becoming nodes (scope rule §14):

| would-be concept | would be prerequisite of | why not minted |
|---|---|---|
| Chemical formulae interpretation (reading Mg(NO₃)₂-type formulae) | CON-MR, CON-EQ-SYMBOL | lives in S1-d (1.23/1.24 territory), outside the slice |
| Solute / solvent / solution | CON-CONCENTRATION | S1-a solutions notes; also re-taught inline in the 1.34C note |
| Isotope abundance → Ar derivation | CON-AR | 1.10/1.17 territory (S1-c); the round-4 1.17 rejection is directly relevant |
| Element symbols / Periodic Table use | CON-AR, CON-EMP-MOL-CALC | pre-S1-e skills |

Expansion requirement: the boundary-minting policy (mint on demand vs.
cross-reference SP nodes) must be decided before Section 2+ slices are built,
or cross-slice prerequisite chains will be structurally missing (FN-2).

## 3. Misconception-evidence inventory (small by evidence discipline)

Only 2 misconception-family nodes exist because only 2 candidates met the
frozen §8A.11 evidence bar:

- 1 ERRONEOUS_BELIEF from an explicit Examiner-Tips "common mistake" statement.
- 1 WRONG_ANSWER_PATTERN from a mark-scheme-documented wrong answer.

Held for insufficient evidence: non-integer-ratio mishandling (HELD-01),
word-equation product-order confusion (HELD-12), CFEC1 Q4 unit pattern
(HELD-11, garbled extraction). The likely expansion sources: all Unit-1/2
mark schemes (~17 files per paper; only 2 pinned), question distractor mining
(Phase 4 / T-C06 territory), and the student-book OCR (misconception
callouts). COMMONLY_CONFUSED_WITH has zero instances corpus-wide in this slice
(HELD-02/03 document the nearest misses).

## 4. EXPLAINED_BY corpus constraint

TODO T-C11 reserves Student-Book page-level EXPLAINED_BY enrichment for after
the full 383-page OCR run. The pilot's 3 EXPLAINED_BY edges all cite
revision-note teaching only. Book-based candidates are out of scope and not
 inventoried here.

## 5. Assessment-evidence pinning

`scripts/c11_evidence/` pins exactly 2 extractions (CFEC1/CFEC2 Unit-1
Paper-1 mark schemes; sha1 aaf918d9332b / 6c63a9e02b71). CFEC1 is cited in
provenance only (MOLAR-RATIO upstream); CFEC2 carries the WRONG_ANSWER_PATTERN
evidence. The remaining ~15 Unit-1 mark schemes (and Unit-2) are unmined — a
bounded, mechanical expansion task with the same pin-extract-verify pattern.

## 6. Graph-side gaps (honest)

- RELATED_TO: 0 edges in the slice (residual-class discipline; see report §2).
  The relation class is fully supported by the schema, gates and checker — its
  zero count reflects the evidence, not a missing capability.
- REVIEW_REQUIRED: 2 edges (PR-03→CON-MOLE; GAS-VOL-CALC→CON-AVOGADRO-LAW) —
  the §8A.13 explicit-uncertainty channel, awaiting the operator.
- Promotion pathway: not built (deliberate — nothing may be promoted during
  the pilot; the c10_promote-style batch tool is a post-review round).
- V2 SQL: CONCEPT node type and COMMONLY_CONFUSED_WITH / WRONG_ANSWER_PATTERN
  relations are not in the live enum; projection documented (architecture
  §13), migration deferred to the DB task.
