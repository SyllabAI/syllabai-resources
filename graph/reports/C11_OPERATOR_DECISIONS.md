# T-C11 Operator Decisions — Session 41 (2026-09-11)

Execution of the operator's review decision round, against resources HEAD
`4eba8ea` / syllabai HEAD `bbf4e08` (both verified clean before work). This
document is the round record: the two executed REVIEW_REQUIRED verdicts, the
two medium-confidence presentations (item 4/5 of the operator's list —
presented BEFORE any promotion, decision PENDING), the yield-triple ontology
ruling, and the zero-promotion audit. Machine record:
`graph/reports/C11_OPERATOR_DECISIONS.json`.

**Nothing was promoted this round.** No edge identity has been explicitly
ratified by the operator: the two REVIEW_REQUIRED decisions are REJECT and
HOLD, the two medium-confidence judgments are presented-pending, and the 31
SUGGESTED edges await per-row confirmation. Promoted count: **0**
(`scripts/c11_promotions.yaml` has zero entries — verified). The promotion
guards were nevertheless fully exercised (audit below).

---

## 1. Decisions executed

| REVIEW_REQUIRED edge | operator verdict | execution | graph effect |
|---|---|---|---|
| `4CH1-PR-03 REQUIRES_PREREQUISITE 4CH1-CON-MOLE` | **REJECT** (verbatim reasons recorded) | decision-record re-authoring per §7/§10: the edge left the authored set and is permanently preserved as rejected candidate **HELD-13** with the operator's reasons verbatim, decided_by/decided_date/review_reference, and full history | edge removed from `graph/concept_edges.yaml` (66 → 65 edges); NOT promotable ever (held/rejected candidates are not edges — G13 / c11.13 / c11_promote.py all fail closed, machine-tested T19/T20) |
| `4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AVOGADRO-LAW` | **HOLD** (verbatim reasons recorded) | `operator_decision` block (verdict HOLD, operator, 2026-09-11, reasons verbatim) on the edge in the decision record; rendered into the review sheet §3.1 + §8 | edge REMAINS in the graph as REVIEW_REQUIRED; not eligible for promotion; do not convert to ACCEPT or REJECT merely to complete the pilot |

Both decision records live in three coherent places (no drift possible): the
decision record (`scripts/c11_pilot_decisions.yaml`, source of truth), the
authoritative review sheet (`graph/reports/C11_PILOT_REVIEW_SHEET.md` §3.1/§8,
re-rendered from the decision record by `scripts/c11_review_render.py`), and
its machine record (`C11_PILOT_REVIEW.json` → `operator_decisions`).

**All 12 other held candidates remain out of HUMAN_VALIDATED** (operator
item 7): the promotions record is empty; held candidates are not edges and are
categorically refused by the promotion pathway (T05 HELD-04, T19 HELD-13
machine tests); the graph carries 0 `validation_status: HUMAN_VALIDATED`
(machine-checked c11.10).

## 2. Medium-confidence judgments — presented for operator decision (PENDING)

Per the operator's items 4–5, the exact source/target/evidence/rationale for
each judgment, presented BEFORE any promotion. **Neither is promoted; neither
is decided.** They are marked PENDING in the decision record and the review
sheet (§3.2 operator column) and must not be promoted until the operator
explicitly rules on them.

### Judgment A — `4CH1-CON-MOLAR-GAS-VOL EXPLAINED_BY 4CH1-CON-AVOGADRO-LAW`

| # | field | value |
|---|---|---|
| 1 | source node | `4CH1-CON-MOLAR-GAS-VOL` — concept "Molar gas volume at RTP (24 dm3)", CORE under 4CH1-1.35C |
| 2 | relation type | `EXPLAINED_BY` (explained → explainer), one of 3 EXPLAINED_BY edges in the pilot |
| 3 | target node | `4CH1-CON-AVOGADRO-LAW` — concept "Avogadro's Law", ENRICHMENT under 4CH1-1.35C |
| 4 | exact evidence | `"From the molar gas volume the following formula triangle can be derived"` — byte-verified (T-C10 norm) against the source note; this is the ONLY evidence anchor on the edge. The note's law section states the law itself ("Avogadro's Law states that at the same conditions of temperature and pressure, equal amounts of gase…") in the same note, but no sentence states "the law explains/derives the molar volume" |
| 5 | evidence source | NOTE `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md` — T-C10 HUMAN_VALIDATED @ 4CH1-1.35C (2026-09-11) |
| 6 | rationale (pass-1) | derivation method `SINGLE_SOURCE_CAUSAL_TEACHING`, confidence capped at medium: the same note section teaches the law and then the molar volume and its formula triangle; the law grounds why one fixed volume per mole exists at given conditions — but the note presents the 24 dm3 value as measured ("was found to be"), not derived from the law, so the explanatory link is tight yet not stated as a derivation |
| 7 | pass-2 verdict | **CONFIRM_WITH_NOTE** — finding **FP-1**: the anchored quote supports the molar-volume → formula-triangle link, not law → molar-volume; the law → molar-volume link rests on section adjacency and the law's semantic content. "Kept; flagged." |
| 8 | why the automated system cannot safely resolve it | The anchored sentence does not teach the asserted explanatory relation itself — it teaches a different link (molar volume → formula). Asserting law → molar-volume therefore requires reconstructing the explanation from section adjacency, exactly the FC-1/FC-2 boundary shape the system quarantines; the confidence model already capped it at medium, and session-40's Task-3 rule-4 audit upheld EXPLAINED_BY discipline only "with 1 flagged edge" — this one. Whether adjacency-plus-semantics is assertable as EXPLAINED_BY is a relation-class judgment reserved for the operator. |
| 9 | independent semantic assessment (this round) | The physical relation is real (equal moles ↔ equal volumes at fixed T,P is precisely why a fixed molar volume exists), and the note does teach law and molar volume in one section — but the evidence CLASS overstates the anchor: the honest derivation label for section-ordering evidence is TEACH_SEQUENCE_WITHIN_NOTE (cap medium), not SINGLE_SOURCE_CAUSAL_TEACHING. The FP-1 weakness is therefore real and unmitigated beyond the medium band. A cleaner resolution would be an anchor that explicitly derives the 24 dm3 from the law or vice versa. |
| 10 | recommendation to the operator | **HOLD — do not promote on current evidence.** Resolution paths: (i) the operator explicitly accepts the adjacency-grounding weakness and ratifies the identity as-is; (ii) the operator rejects it; or (iii) defer to the expansion round with a decision-record revision that either re-anchors (a corpus source that states the derivation) or re-classifies the derivation method to TEACH_SEQUENCE_WITHIN_NOTE. None of these is open on the present corpus without the operator's call. |

### Judgment B — `4CH1-MIS-EQ-SUBSCRIPT REMEDIATED_BY 4CH1-CON-CONSERVATION-MASS`

| # | field | value |
|---|---|---|
| 1 | source node | `4CH1-MIS-EQ-SUBSCRIPT` — misconception "Balancing equations by altering subscripts" (pattern_class ERRONEOUS_BELIEF), no SP attachment (misconception nodes are unattached) |
| 2 | relation type | `REMEDIATED_BY` (misconception → remediation concept), one of 2 REMEDIATED_BY edges in the pilot |
| 3 | target node | `4CH1-CON-CONSERVATION-MASS` — concept "Law of Conservation of Mass", CORE under 4CH1-1.25 / SUPPORTING under 4CH1-1.26 |
| 4 | exact evidence | `"You cannot do this because it changes what the substance is"` — byte-verified; the corrective sentence of the same Examiner Tips block whose error-documentation sentence ("A common mistake when balancing symbol equations is to add, change or remove small numbers…") grounds the companion MISCONCEPTION_OF edge (high confidence) |
| 5 | evidence source | NOTE `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Writing chemical equations - IGCSE Chemistry Revision Notes.md` — T-C10 HUMAN_VALIDATED @ 4CH1-1.25 (2026-09-11) |
| 6 | rationale (pass-1) | derivation method `EXAMINER_TIP_EXPLICIT`, confidence capped at medium: the corrective content is "balance with coefficients because atoms (not substances) are conserved" — but the tip's OWN argument is substance-identity ("it changes what the substance is"), and mapping the remediation to CON-CONSERVATION-MASS rather than keeping it note-local is a judgment flagged for review |
| 7 | pass-2 verdict | **CONFIRM_WITH_NOTE** — kept at medium; session-40 Task-3 rule-5 audit flagged it as the one partial concern in the REMEDIATED_BY class |
| 8 | why the automated system cannot safely resolve it | The error itself is unambiguously documented (the MISCONCEPTION_OF edge is high-confidence), but the REMEDIATED_BY TARGET selection requires deciding WHICH taught concept corrects the belief. The tip's explicit argument is substance-identity — the exact corrective concept (coefficients alter amounts, subscripts alter substance) is a chemical-formulae-interpretation concept that has NO node in the pilot slice (boundary gap, FN-2). Conservation of mass grounds why coefficient-balancing works, but the note never says "because mass is conserved, balance with coefficients". Choosing between the best-available in-slice approximation and a not-yet-minted exact concept is an ontology/mapping decision the machine must not make. |
| 9 | independent semantic assessment (this round) | The remediation path is pedagogically real: a learner who internalizes conservation-of-mass (atoms are conserved, so coefficients balance) has the standard corrective for subscript-altering. But the edge's target is an approximation, not the exact corrective concept the evidence names; the honest reading is that the corpus's remediation for THIS misconception is the substance-identity argument. The cleaner fix — minting a coefficients-vs-subscripts concept in the expansion round — was already recommended by session-40 Task 3. |
| 10 | recommendation to the operator | **HOLD — promotable only if the operator explicitly accepts the approximation** (remediation-via-conservation as the in-slice target). Alternative paths: (i) reject the edge and let the misconception keep only its MISCONCEPTION_OF relation until the exact corrective concept is minted; (ii) defer to the expansion round and re-target after boundary minting. The companion MISCONCEPTION_OF edge (high confidence) is unaffected by this choice. |

## 3. Ontology decision — yield triple (resolved as an ontology ruling)

Resolved per the operator's item 6 as an **ontology decision** (not a mapping
decision): **the yield triple stays split — no merge.** Full ruling with the
generalized operand-definition rule recorded in `C11_ARCHITECTURE.md` §20
(OD-1): the triple is two definitions + one calculation procedure (§8 minting
rule; the 1.32/1.33 definition-vs-procedure precedent), the three are
independently assessable so merging would corrupt mastery attribution, and the
same-anchor PERCENT-YIELD → {YIELD, THEOR-YIELD} edge pair is the honest
representation of the formula's operand structure, not a split artifact. The
generalized rule (one procedure concept + one concept per distinctly-taught
operand definition, one prerequisite edge per operand) now governs the §16
expansion. A future merge remains operator-only. Additionally recorded as
**OD-2**: the operator's verbatim rule from the REJECT decision — "Do not
treat table labels or incidental terminology as instructional evidence" —
codified as an evidence-admissibility rule for the expansion round.

## 4. Promotion audit (zero promotions, guards fully exercised)

| check | result |
|---|---|
| promotions record | `scripts/c11_promotions.yaml` — **0 entries** (nothing ratified: REJECT + HOLD + 2 PENDING + 31 unconfirmed SUGGESTED) |
| promotion by exact identity only | machine-enforced (3-token spec, parse-level rejection of partial/wildcard); T03 malformed-spec test green |
| no promotion by node / relation type / confidence / batch | nothing was promoted; the pathway has no batch/wildcard surface at all; PART_OF refused (T06); held candidates refused (T05 HELD-04; **T19 HELD-13 — the operator-rejected identity fails closed at the tool**) |
| rejected + held candidates remain in the audit record | HELD-13 preserved in the decision record held list + review sheet §4 + C11_PILOT_REVIEW.json; the other 12 candidates unchanged |
| graph ⟷ promotions two-way audit | c11.10/c11.13 green (graph_check ALL PASS reading the REAL repo files) |
| anti-forgery | G10 + c11.13: no HUMAN_VALIDATED in the decision record; operator_decision blocks are review state and are never emitted to the graph; T10/T15 green |
| forged promotion of the rejected identity | **T20 green** — a hand-forged promotion entry for `PR-03 → CON-MOLE` makes the generator fail closed with the HELD-13 diagnosis and leaves the graph untouched (permanence guard) |
| promotion mechanism suite | `scripts/c11_promote_test.py` — **27/27 PASS** in a sandbox repo copy (25 previous + T19/T20 new) |

## 5. Machine state after this round (all live, re-verified)

- graph_check: **ALL PASS** — 29 nodes / **65 edges** (33 PART_OF + 32
  semantic) / **0 HUMAN_VALIDATED**; negative control 4CH1-4.15 uncovered
  (0 concepts, 0 edges, 0 coverage — `4CH1-4.15` appears only as the meta
  `negative_control` declaration).
- c11_negative_test: **14/14 PASS** (12 corruption classes + positive control
  + byte-identical idempotence) at the 65-edge state.
- c11_task4_variants: **3/3 PASS** (4.15 spec-wording / topical-similarity /
  uncovered-remediation lures all machine-rejected).
- c11_promote_test: **27/27 PASS**.
- Deterministic regeneration: **byte-identical** (generator re-run leaves all
  three graph YAML files unchanged at the new state; promotion state remains a
  pure function of (decision record, promotions file) with zero promotions).
- Graph diff vs `e218259` snapshot: exactly the REJECT — the
  PR-03 → CON-MOLE edge block removed and the meta counts updated
  (66→65 edges, RP 26→25, RR 2→1); all other 65 edges byte-identical,
  evidence/provenance/confidence preserved verbatim.

## 6. Recorded defects / observations (for the expansion round, not fixed here)

- **CORRECTED (session 43, 2026-09-12 — report/data drift):** the defect
  previously recorded here ("corrupted entry `"aximum yield"`") misdescribed
  the store. The alias has been `maximum yield` (byte-stable) in both
  `scripts/c11_pilot_decisions.yaml` and `graph/concepts.yaml` across all
  committed revisions; the string `aximum yield` never existed in any data
  file — it existed only in report text (this document, the `.json`, the
  §16 gate report, and the renderer literal), all corrected 2026-09-12. The
  genuine open issue is that the alias `maximum yield` is **unevidenced** —
  the phrase appears nowhere in the pilot corpus (see the session-43 alias
  audit, `C11_REVIEW_PACKAGE.md` §7); disposition (drop / re-evidence / keep)
  awaits the operator. The concept alias itself was not modified.
- HELD-13's history field records that re-adding the rejected identity
  requires an explicit operator decision and a new extraction pass.
