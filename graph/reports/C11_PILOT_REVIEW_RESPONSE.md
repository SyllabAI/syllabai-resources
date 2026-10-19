# T-C11 Pilot Review Response — Session 40 (operator review-round tasking)

Response to the operator's six-task review instruction, executed against
resources HEAD `e218259` / syllabai HEAD `afb1d99` (both verified clean before
work). Machine record: `graph/reports/C11_PILOT_REVIEW_RESPONSE.json`.
Companion gate report: `graph/reports/C11_S16_GATE_REPORT.md`.

**Standing baseline (re-verified this session):** graph_check 11/11 PASS ·
c11_negative_test 14/14 PASS · deterministic regeneration byte-identical ·
4CH1-4.15 zero manufactured coverage · 0 HUMAN_VALIDATED T-C11 edges ·
promotions record empty.

**Headline verdicts (Task 1):**

| REVIEW_REQUIRED edge | pass-2 | this review (pass 3) | action taken |
|---|---|---|---|
| `4CH1-PR-03 REQUIRES_PREREQUISITE 4CH1-CON-MOLE` | REJECT | **REJECT** (concordant) | none — operator settles; recommendation recorded |
| `4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AVOGADRO-LAW` | HOLD | **HOLD** (concordant) | none — operator settles; recommendation recorded |

Neither edge was silently resolved, neither was promoted, and nothing else in
the graph was promoted: the live store remains **0 HUMAN_VALIDATED edges**
with the frozen 29/66/12 shape byte-identical.

---

## Task 1 — Human review package: the two REVIEW_REQUIRED edges

### Edge 1 — `4CH1-PR-03 REQUIRES_PREREQUISITE 4CH1-CON-MOLE`

| # | field | value |
|---|---|---|
| 1 | source node | `4CH1-PR-03` — pilot practical node "Determine the formula of a metal oxide" (MgO by combustion / CuO by reduction), spec 4CH1-1.36 |
| 2 | relation type | `REQUIRES_PREREQUISITE` |
| 3 | target node | `4CH1-CON-MOLE` — concept "The mole (unit of amount of substance)", CORE under 4CH1-1.27 |
| 4 | exact evidence | `"| moles | a / Ar | a / Ar |"` (MgO results table) — the CuO table carries the parallel `"| moles | a / Mr | b / Mr |"` row. Byte-verified in the source file under the T-C10 norm. These two table-row labels are the ONLY occurrences of "mole(s)" in the entire note — the prose (Aim, Method, Steps 1–3) never names the concept. |
| 5 | evidence source | NOTE `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Investigating metal oxide formulas - IGCSE Revision Notes.md` — T-C10 HUMAN_VALIDATED @ 4CH1-1.36 + 1.31 + 1.33 (2026-09-11) |
| 6 | rationale (pass-1) | derivation method `IMPLICIT_USE`, confidence capped at medium: the practical's results tables label the mass/Ar quotient as "moles" — the concept is used implicitly, never named in prose; possibly subsumed by the two-edge path PR-03 → EXP-FORMULA-DEDUCTION → MOLE |
| 7 | pass-2 adversarial verdict | **REJECT** — "Subsumed transitively via PR-03 → EXP-FORMULA-DEDUCTION → MOLE; the 'moles' table-row label is implicit use only. Pass-1 emitted as REVIEW_REQUIRED; pass 2 would not emit at all." |
| 8 | why the automated system could not safely resolve it | (a) The evidence class is IMPLICIT_USE — a table-row label, not prose teaching and not use-without-reteaching — and the confidence model caps it at medium precisely because such evidence cannot establish a direct dependency. (b) The graph already asserts PR-03 REQUIRES_PREREQUISITE CON-EXP-FORMULA-DEDUCTION (high, USED_WITHOUT_RETEACHING) and CON-EXP-FORMULA-DEDUCTION REQUIRES_PREREQUISITE CON-MOLE (high, USED_WITHOUT_RETEACHING); learning dependencies compose transitively, but deciding whether a direct edge adds reviewable information beyond the path is a semantic judgment — the MOLAR-MASS → {MR, AR} pair proves transitively-reachable edges CAN be semantically distinct, so the machine rules correctly refuse to auto-collapse the direct edge. |
| 9 | independent semantic assessment | The practical's analysis procedure (mass → ÷Ar → ratio → formula) IS the CON-EXP-FORMULA-DEDUCTION method, already asserted as the practical's dependency; the mole concept enters only INSIDE that method, as an implicit table label. A learner who has mastered the deduction method can execute the practical without the named 1.27 concept (mole as the unit of amount of substance) — the note never demands it. The direct edge is therefore redundant with the transitive path (the same failure class as HELD-04, TRANSITIVELY_SUBSUMED) and rests on weaker evidence than either path edge. |
| 10 | recommended decision | **REJECT** — do not promote. At the expansion round, re-author the decision record to drop this edge (with the subsumption rationale); until then it stays in the graph as REVIEW_REQUIRED for the operator to settle. |

### Edge 2 — `4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AVOGADRO-LAW`

| # | field | value |
|---|---|---|
| 1 | source node | `4CH1-CON-GAS-VOL-CALC` — concept "Gas volume calculation", CORE under 4CH1-1.35C |
| 2 | relation type | `REQUIRES_PREREQUISITE` |
| 3 | target node | `4CH1-CON-AVOGADRO-LAW` — concept "Avogadro's Law", ENRICHMENT under 4CH1-1.35C |
| 4 | exact evidence | `"Therefore, the volume of oxygen needed would be = 5 moles x 150 cm3"` — propane worked example (C3H8 + 5O2 → 3CO2 + 4H2O). Byte-verified. The example's preceding line reads "The balanced equation shows that 5 moles of oxygen are needed to completely react with 1 mole of propane" — ratio scaling, no invocation of the law. The note names Avogadro's Law only in its own section (and the front-matter/excerpt lines), never in any worked example. |
| 5 | evidence source | NOTE `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md` — T-C10 HUMAN_VALIDATED @ 4CH1-1.35C (2026-09-11) |
| 6 | rationale (pass-1) | derivation method `IMPLICIT_USE`, medium cap: the worked example computes gas volumes straight from molar ratios (volume ratios track mole ratios — Avogadro's Law applied) without ever naming the law; the target being an ENRICHMENT concept further argues for review before the edge is trusted |
| 7 | pass-2 adversarial verdict | **HOLD** — "The worked example applies volume-ratios-track-mole-ratios without naming the law; the dependency may be on CON-MOLAR-RATIO instead (which has no direct edge here). Operator to settle." |
| 8 | why the automated system could not safely resolve it | Three defensible representations compete and the corpus cannot arbitrate: (a) a genuine prerequisite on the law — but the examples never invoke it, and making an ENRICHMENT concept (not demanded by 1.35C) a prerequisite of a CORE calculation would make non-demanded content load-bearing in the learner model; (b) an application of CON-MOLAR-RATIO (1.29) — the example's operative skill (read the 5:1 ratio, scale the volume) is ratio reasoning, but no GAS-VOL-CALC → CON-MOLAR-RATIO edge exists in this graph (pass-1 correctly did not smuggle a different identity under this REVIEW_REQUIRED edge); (c) grounding-only — already represented as MOLAR-GAS-VOL EXPLAINED_BY AVOGADRO-LAW (medium, FP-1-flagged). Choosing requires either corpus evidence the note does not contain or a pedagogical-architecture decision reserved for the operator. |
| 9 | independent semantic assessment | HOLD is correct. The note teaches the law as a named statement and then never references it; the worked example runs purely on the balanced equation's molar ratio. The named-prerequisite reading fails the "genuine learning dependency, not topical similarity" test AS EVIDENCED; the ratio-skill reading is more faithful to the corpus but is a different edge identity; the law's pedagogical contribution is already carried by the (separately flagged, medium-confidence) EXPLAINED_BY edge into MOLAR-GAS-VOL. |
| 10 | recommended decision | **HOLD** — do not promote on current evidence. Resolution paths for the expansion round: (i) author `4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-RATIO` with the worked-example quote as USED_WITHOUT_RETEACHING evidence (cross-SP 1.35C → 1.29, mirroring the existing GAS-VOL-CALC → MOLE-MASS-CONV cross-SP edge), keeping the law as enrichment grounding; or (ii) promote the direct edge only if a corpus source explicitly invokes the law in a calculation. Neither is open on the present corpus. |

Concordance: this review agrees with both pass-2 verdicts (REJECT/HOLD); no
pass-3 verdict contradicts any pass-1 emission or pass-2 verdict.

---

## Task 2 — Audit of the 12 held candidates

Nothing was promoted; every disposition below is a review recommendation only.
Overriding a hold remains re-authoring the decision record (operator action),
never a promotion and never a hand-edit.

| id | candidate | relation | hold reason | evidence weakness | recommended disposition |
|---|---|---|---|---|---|
| HELD-01 | "rounding non-integer empirical ratios" (1.5 → 2) | MISCONCEPTION_OF (would-be) | INSUFFICIENT_EVIDENCE_MISCONCEPTION | examiner tip prescribes correct practice; names no mistake, documents no wrong answer | CONFIRM_HOLD — plausibly real (FN-1); revisit only with mark-scheme/question-distractor evidence (T-C06 or deeper Unit-1 MS mining) |
| HELD-02 | (CON-CONCENTRATION, "solution strength") | COMMONLY_CONFUSED_WITH | NO_TARGET_NODE_PLUS_WEAK_CLASS | documents colloquial usage, not a student confusion pair; no slice node for the target | CONFIRM_HOLD — revisit only if boundary minting creates the node AND confusion evidence is documented |
| HELD-03 | (CON-MOLE, CON-AVOGADRO-CONST) | EXPLAINED_BY | RELATION_CLASS_AMBIGUOUS | equally defensible as EXPLAINED_BY, definitional containment, or RELATED_TO | CONFIRM_HOLD — corpus does not pin the class |
| HELD-04 | (CON-GAS-VOL-CALC, CON-MOLE) | REQUIRES_PREREQUISITE | TRANSITIVELY_SUBSUMED | covered by GAS-VOL-CALC → MOLAR-GAS-VOL → MOLE; no reviewable information added | CONFIRM_HOLD → recommend recording as REJECTED at the next decision-record revision |
| HELD-05 | (CON-MOLAR-RATIO, CON-EQ-SYMBOL) | REQUIRES_PREREQUISITE | TRANSITIVELY_SUBSUMED_PLUS_DEFENSIONAL | ratio concept definitionally bound to balanced equations; REACTING-MASS already carries both | CONFIRM_HOLD → recommend REJECTED at revision (density control) |
| HELD-06 | (CON-EMP-MOL-CALC, CON-MOLE-MASS-CONV) | REQUIRES_PREREQUISITE | TAUGHT_INLINE | procedure re-teaches its own per-element mass/Ar division (mention ≠ dependency) | CONFIRM_HOLD → recommend REJECTED at revision (the exact tasking rule) |
| HELD-07 | (CON-CONCENTRATION, solute/solvent/solution) | REQUIRES_PREREQUISITE | TAUGHT_INLINE_PLUS_BOUNDARY | definitions re-taught inline AND concepts belong to out-of-slice notes | CONFIRM_HOLD — expansion must settle the boundary-minting policy (FN-2) before this can resolve |
| HELD-08 | (CON-EMPIRICAL-FORMULA, CON-MOLECULAR-FORMULA) | RELATED_TO | RESIDUAL_CLASS_DISCIPLINE | the pair already carries a dependency edge; RELATED_TO would duplicate it | CONFIRM_HOLD → recommend REJECTED at revision (residual class must stay empty by discipline) |
| HELD-09 | SO2-from-impurities / combustion / acid-rain cluster @ 4CH1-4.15 | EXPLAINED_BY (+ REMEDIATED_BY / MISCONCEPTION_OF companions) | NEGATIVE_CONTROL_4_15 (status: rejected) | premise and stated consequence sit in DIFFERENT notes; the demanded causal mechanism is taught nowhere | CONFIRM_REJECT — the canonical negative-control rejection (round-4 T-C10 precedent) |
| HELD-10 | (CON-EXP-FORMULA-DEDUCTION, CON-EMP-MOL-CALC) | REQUIRES_PREREQUISITE | RELATION_CLASS_AMBIGUOUS | "application-of vs requires" undecidable; the method embeds the ratio steps inline | CONFIRM_HOLD — best REVIEW_REQUIRED-style candidate for the expansion round |
| HELD-11 | CFEC1 MS Q4(a)(ii)–(iii) "0.44 for 1 mark only" / "0.0004" | WRONG_ANSWER_PATTERN | EVIDENCE_AMBIGUOUS_EXTRACTION | pinned PDF-table extraction garbles the question context; values/units unreconstructable without the paired QP | CONFIRM_HOLD — revisit when the paired question paper is pinned (T-C06) |
| HELD-12 | "products written first" word-equation confusion | MISCONCEPTION_OF | EXAM_TECHNIQUE_NOT_MISCONCEPTION | Careful annotation is question-reading guidance, not an erroneous belief | CONFIRM_HOLD → recommend REJECTED at revision |

### Failure-class clustering — YES, the 12 holds form four stable classes

The holds are not twelve individual exceptions; they cluster into four stable
failure classes, now documented as first-class generation rules in
`C11_ARCHITECTURE.md §19`:

- **FC-1 evidence-sufficiency** — HELD-01, HELD-11 (evidence missing, implicit, or ambiguous relative to the class's bar)
- **FC-2 relation-class misfit** — HELD-02, HELD-03, HELD-10, HELD-12 (no defensible single class, or wrong relation family)
- **FC-3 redundancy / normalization** — HELD-04, HELD-05, HELD-06, HELD-07 (true but adds no reviewable information: subsumed / taught-inline / boundary)
- **FC-4 negative-control enforcement** — HELD-09 (manufactured coverage from premise + consequence; the only outright rejection)

Validation of the taxonomy: the two REVIEW_REQUIRED edges instantiate the same
classes (Edge 1 = FC-3 with FC-1 evidence; Edge 2 = FC-2 with FC-1 evidence) —
the held list and the RR quarantine are the same discipline applied at
different pipeline points (abstain vs emit-with-quarantine). FC-3 is
deliberately NOT machine-enforced (MOLAR-MASS → {MR, AR} demonstrates
transitively-reachable but semantically-distinct edges); FC-4 is fully
machine-enforced. Per-class emit-or-abstain policy for the expansion round is
specified in §19.

---

## Task 3 — Relation-semantics review (all 66 edges, 7 rules)

| # | rule under test | finding | verdict |
|---|---|---|---|
| 1 | REQUIRES_PREREQUISITE = genuine learning dependency, not topical similarity | All 26 RP edges audited: 24 SUGGESTED each rest on DEFINITIONAL_DEPENDENCY / USED_WITHOUT_RETEACHING / EXPLICIT_TEACH_SEQUENCE evidence (procedure steps, formula statements, definition chains) — no topical-similarity edges found. The two borderline cases are exactly the RR pair (implicit-use evidence), now resolved REJECT/HOLD (Task 1). Abstention evidence: HELD-02 (topical/colloquial candidate held), HELD-04–07 (redundant dependency candidates held). Recorded granularity caveats, not defects: FP-2 (yield-split artifacts — vanish under an operator merge), FP-3 (REACTING-MASS → EQ-SYMBOL covers equation-interpretation and -writing in one concept). | **UPHELD** |
| 2 | RELATED_TO not used as a weak substitute for an unsupported prerequisite | 0 RELATED_TO and 0 COMMONLY_CONFUSED_WITH edges — complete abstention from the residual classes. The one natural candidate (HELD-08) was held precisely because the pair already carries a dependency edge. Machine rule requires relation_class_rationale for any residual-class edge; none was ever assertable. | **UPHELD (by abstention)** |
| 3 | MISCONCEPTION_OF requires actual misconception evidence | The single MISCONCEPTION_OF edge (MIS-EQ-SUBSCRIPT → CON-EQ-SYMBOL) rests on an explicit examiner tip that NAMES the mistake ("A common mistake when balancing symbol equations is to add, change or remove small numbers…"); pattern_class ERRONEOUS_BELIEF matches the relation (frozen triple distinction, machine-checked). Held discipline: HELD-01 (no documented error), HELD-12 (exam technique, not a belief). Machine: G11 + negative-test class 12. | **UPHELD** |
| 4 | EXPLAINED_BY requires actual explanatory evidence | EQ-SYMBOL ← CONSERVATION-MASS: single-sentence causal teaching ("The Law of Conservation of Mass enables us to balance chemical equations, since…") — the strongest evidence class. YIELD ← YIELD-FACTORS: same-section causal teaching with five enumerated causes. MOLAR-GAS-VOL ← AVOGADRO-LAW: **the one live concern (FP-1)** — the anchored quote supports molar-volume → formula, not law → molar-volume; the link rests on section adjacency and empirical phrasing ("was found to be"). Kept at medium confidence with the flag: defensible as SUGGESTED, but this edge should be treated as review-gated — NOT recommended for promotion without the operator explicitly accepting the FP-1 weakness. | **UPHELD with 1 flagged edge** |
| 5 | REMEDIATED_BY requires evidence the target addresses the misconception/need | MIS-CONC-UNIT ← CON-VOL-CONVERSION: direct match — the MS-documented wrong answer ("failing to divide by 1000") is exactly what the target's Examiner-Tips block corrects ("To go from cm3 to dm3: divide by 1000"). MIS-EQ-SUBSCRIPT ← CON-CONSERVATION-MASS: **partial concern** — the corrective sentence argues substance identity ("it changes what the substance is"), conservation is the section's grounding for coefficient-balancing; kept at medium with the note, cleaner fix = mint a coefficients-vs-subscripts concept in expansion. | **UPHELD with 1 medium-confidence judgment flagged** |
| 6 | PART_OF structurally distinct from pedagogical dependency | PART_OF edges are DERIVED deterministically from node attachments (33 edges, concept→SP containment with role), machine-checked to equal the declared attachments exactly (c11.7); REQUIRES_PREREQUISITE edges are AUTHORED concept→concept learning dependencies with evidence anchors. Different derivation, direction, and schema role; the new promotion pathway (§18) explicitly excludes PART_OF. No PART_OF edge encodes a dependency and vice versa. | **UPHELD (machine-enforced)** |
| 7 | premise + consequence in separate notes cannot become a causal/explanatory edge | HELD-09 is the live rejection. Machine-enforced at three layers: G05 (no attachment to 4.15 is possible), G07/c11.6 (NOTE anchors must resolve through T-C10 HUMAN_VALIDATED coverage of an attached SP — the combustion and acid-rain notes map to 4.11–4.13 / 4.14–4.16, outside the slice), negative-test classes 10–11, plus the three new task-4 variant lures (below). | **UPHELD (machine-tested)** |

---

## Task 4 — Negative-control verification (4CH1-4.15, canonical)

Machine state at the close of this round:

| suite | result |
|---|---|
| frozen `c11_negative_test.py` (classes 10 = 4.15 attachment via acid-rain note; 11 = EXPLAINED_BY from premise+consequence notes; + positive control + byte-identical idempotence) | **14/14 PASS** |
| NEW `c11_task4_variants.py` — the operator's named lures: **V1** 4.15 attachment quoting the OFFICIAL spec wording as the SPEC anchor (semantic relatedness via the specification itself); **V2** 4.15 attachment via the combustion note ("sulfur exists in fuels", 4.11–4.13 coverage); **V3** REMEDIATED_BY path assembled from byte-true quotes of the uncovered acid-rain/combustion notes | **3/3 PASS — all machine-rejected (c11.5 / c11.6)** |
| live graph state | 4.15: **0 concepts, 0 edges, 0 coverage** (graph_check: "negative control 4CH1-4.15 uncovered") |

Verified failure modes: attachment to 4.15 is structurally impossible (G05 —
regardless of anchor kind, including quoting the SP's own official wording);
NOTE anchors that do not resolve through T-C10 HUMAN_VALIDATED coverage of an
attached SP are inadmissible (c11.6 — this kills topical-similarity lures and
remediation paths built from genuinely-quoted but uncovered notes);
MARK_SCHEME anchors are misconception-class only. Remediation of the 4.15 gap
remains a corpus decision (new note / student-book OCR teaching the
mechanism), never a graph-side inference.

---

## Task 5 — Promotion tooling: built and tested; NOTHING promoted

Interpretation note (explicit, for the operator to overrule if read
differently): the tasking conditions the promotion of the two RR edges on
their being ACCEPTED. They received REJECT and HOLD, so neither was promoted
and no batch was derived. The mechanism itself was still built and machine-
tested because §16's gate list independently requires "promotion mechanism
tested" — an inert, operator-command-gated tool promotes nothing and violates
nothing (fail-safe reading). The live store remains 0 HUMAN_VALIDATED.

Built this round (details in `C11_ARCHITECTURE.md §18`):

- `scripts/c11_promote.py` — exact `(source_node, relation, target_node)`
  identity promotion; evidence pre-verified before anything is written;
  idempotent; fail-closed on malformed specs, unknown identities, held
  candidates, PART_OF, bad dates, AI attribution.
- `scripts/c11_promotions.yaml` — the operator-side promotion record
  (currently **zero entries**).
- `c11_concept_pilot.py` G13 gate + emission: promoted edges carry
  HUMAN_VALIDATED + validated_by/date; evidence/provenance/confidence
  preserved verbatim; zero promotions emits the exact frozen bytes.
- `graph_check.py` c11.10/c11.13: graph ⟷ promotions-record two-way audit,
  decision-record anti-forgery, stale-graph and attribution-drift detection —
  always reading the REAL repo files so graph copies cannot cheat them.
- `scripts/c11_promote_test.py` — **25/25 PASS** (T01–T18) in a sandbox repo
  copy: positive (promotion, determinism, idempotence, byte-preservation,
  RR-edge pathway) + negative (14 fail-closed classes).

"Do not promote the entire pilot automatically / first promote only the
individually ratified edges": honored — no edge has been individually ratified
by the operator, so nothing was promoted. The 31 pass-2-confirmed SUGGESTED
edges and 29 nodes await the operator's review-sheet decisions; a promotion
batch derived mechanically from those confirms will use the same
exact-identity tooling.

---

## Machine state after this round (all live)

- graph_check: **11/11 PASS** — 29 nodes / 66 edges (33 PART_OF + 33
  semantic) / **0 HUMAN_VALIDATED**; negative control 4.15 uncovered.
- c11_negative_test: **14/14 PASS** (frozen suite untouched).
- c11_task4_variants: **3/3 PASS** (new).
- c11_promote_test: **25/25 PASS** (new).
- Deterministic regeneration: **byte-identical** at zero promotions (graph/
  unchanged vs the e218259 frozen snapshot).
- Pilot snapshot: the three graph YAML files are untouched by this round; all
  additions are scripts and reports.
