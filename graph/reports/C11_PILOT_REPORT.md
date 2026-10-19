# T-C11 Pilot Report — Concept / Prerequisite / Misconception Graph (1.25–1.36)

Tasking: operator instruction 2026-09-11 ("Begin T-C11 … architecture and pilot
specification … deliberately small and adversarial … 4CH1-4.15 as deliberate
NEGATIVE CONTROL … success = HIGH PRECISION + PROVENANCE + AUDITABILITY +
CORRECT ABSTENTION"). Contract: `C11_ARCHITECTURE.md`. Decision record:
`scripts/c11_pilot_decisions.yaml` (pass `c11-pilot-pass-1`). Adversarial
review: `scripts/c11_pilot_review_pass2.yaml`. Machine artifacts:
`graph/concepts.yaml`, `graph/concept_edges.yaml`,
`graph/spec_command_kinds.yaml`.

**Status: pilot complete; STOPPED at the operator-review gate.** Nothing is
promoted. Full-graph expansion awaits §16 authorization. This report contains
every metric the tasking demanded.

---

## 1. Number of nodes — 29

| family | count | notes |
|---|---|---|
| CONCEPT | 27 | split-first identity policy; aliases on every node |
| MISCONCEPTION (ERRONEOUS_BELIEF) | 1 | balancing-by-altering-subscripts (Examiner-Tip-quoted) |
| MISCONCEPTION (WRONG_ANSWER_PATTERN) | 1 | cm³→dm³ failure (mark-scheme-quoted) |

27 concepts from 12 SPs ≈ 2.25 concepts/SP — deliberately sparse (the §8A.16
anti-failure-mode: no LLM ontology explosion). Multi-part SPs decompose:
1.25 → 3 concepts (word equations / balanced equations / state symbols); 1.28 →
Ar + Mr + molar mass + mole–mass conversion; 1.31 → experimental deduction +
water of crystallisation. Command-kind split made structural: 1.32
(know-terms) definition concepts vs 1.33 (calculate) procedure concept.

## 2. Candidate edges by type — 66 total

| relation | count | of which REVIEW_REQUIRED |
|---|---|---|
| PART_OF (derived from attachments) | 33 | 0 |
| REQUIRES_PREREQUISITE | 26 | 2 |
| EXPLAINED_BY | 3 | 0 |
| MISCONCEPTION_OF | 1 | 0 |
| REMEDIATED_BY | 2 | 0 |
| WRONG_ANSWER_PATTERN | 1 | 0 |
| RELATED_TO | **0** | 0 |
| COMMONLY_CONFUSED_WITH | **0** | 0 |

Zero RELATED_TO / COMMONLY_CONFUSED_WITH is an honest result, not a gap: every
evidenced association in the slice either was a learning dependency, an
explanation, a misconception-class relation, or failed the evidence bar and was
held (HELD-02/03/08). Roles on PART_OF: 29 CORE / 1 SUPPORTING
(CONSERVATION-MASS@1.26 — the Mr-sum consequence, used but not demanded) /
3 ENRICHMENT (Avogadro constant@1.27, yield factors@1.30, Avogadro's law@1.35C
— taught in mapped notes, outside SP demand; the command-kind rule made
mechanical). Multi-step chains: deepest REQUIRES_PREREQUISITE chain = 6 levels
(PERCENT-YIELD → THEOR-YIELD → REACTING-MASS → MOLE-MASS-CONV → MOLAR-MASS →
MR → AR) — pilot tests #3/#4 demonstrated. Cross-SP dependencies: 1.30→1.29,
1.35C→1.28. Practical→conceptual: 2 edges from 4CH1-PR-03 (pilot test #5).

## 3. Accepted / rejected / held

| disposition | count | where |
|---|---|---|
| Accepted (emitted as candidates) | 29 nodes + 66 edges | graph files, all SUGGESTED/REVIEW_REQUIRED |
| Rejected (unsafe — not in graph) | 1 | HELD-09: the 4.15 premise+consequence class (negative control) |
| Held (insufficient evidence / ambiguous / subsumed) | 11 | review sheet §4, reasons per entry |
| REVIEW_REQUIRED (in graph, explicitly uncertain, §8A.13) | 2 edges | review sheet §3.1 |

Both abstention channels demonstrated: 11 held-out-of-graph with named failing
rules (INSUFFICIENT_EVIDENCE_MISCONCEPTION, TAUGHT_INLINE, TRANSITIVELY_SUBSUMED,
RELATION_CLASS_AMBIGUOUS, …) + 2 REVIEW_REQUIRED in-graph. The system said
"insufficient evidence" instead of forcing an edge 12 times.

## 4. Evidence coverage — 100%

85 evidence anchors across 29 nodes + 33 authored edges + 33 attachments:
NOTE 70 / SPEC 13 / MARK_SCHEME 2. Every record carries ≥1 anchor; every quote
byte-verified (T-C10 norm) against its cited file at generation AND at
graph_check (independent re-implementation). Distinct sources: 10 notes (all 9
pilot-slice notes + the negative-control acid-rain note cited only inside the
held list), the spec registry, 1 pinned mark-scheme extraction. Misconception
nodes: 100% source-quoted with remediation evidence (gate c11.11 + negative
class 12).

## 5. Provenance coverage — 100%

Every node/edge carries the full block: tier AI_SUGGESTED, model_version,
extraction_pass, derivation_method (closed vocabulary), derivation_notes,
upstream chain (T-C10 HUMAN_VALIDATED mapping / spec wording / pinned MS
sha), generated_date (pinned). Machine-checked at generation (G01/G03) and at
validation (c11.3). Upstream always resolves to validated T-C10 state — the
provenance hierarchy demanded by the tasking is structurally enforced.

## 6. Confidence distribution

Nodes: 29 high / 0 medium / 0 low (extraction was conservative — only
well-evidenced concepts minted; weak candidates were held, not emitted low).
Edges: 29 high / 4 medium / 0 low. All 4 mediums are cap-enforced:
IMPLICIT_USE (2, the REVIEW_REQUIRED pair), SINGLE_SOURCE_CAUSAL_TEACHING at
reduced honesty (E2 — see FP-1), EXAMINER_TIP_EXPLICIT with judgment-dependent
target (M2 remediation). Zero low-confidence records in-graph by design (low ⇒
held); derivation-method caps are machine-enforced (G09/c11.9 + negative
class 06).

## 7. False-positive findings (adversarial pass 2)

- **FP-1** MOLAR-GAS-VOL EXPLAINED_BY AVOGADRO-LAW: the anchored quote
  supports molar-volume→formula, not law→molar-volume; kept at confidence
  medium with the weakness encoded in the derivation note.
- **FP-2** PERCENT-YIELD → {YIELD, THEOR-YIELD} pair is a split artifact —
  both vanish under an operator merge (identity-policy decision, not a
  defect).
- **FP-3** REACTING-MASS → EQ-SYMBOL: operative dependency is on
  *interpreting* equations; the slice concept covers writing+balancing —
  granularity note for expansion.
No unevidenced edge survived review; no quote failed verification.

## 8. False-negative concerns (documented, honest)

- **FN-1** HELD-01 (non-integer ratio mishandling) is plausibly a real
  misconception but the corpus does not document it — deeper mark-scheme
  mining (only 2 of ~17 Unit-1 MS pinned) or Phase-4 distractor mining may
  surface it.
- **FN-2** Boundary concepts (formulae interpretation, solute/solvent,
  isotope abundance) are real cross-slice prerequisites, deliberately not
  minted — the expansion MUST define the boundary-minting policy.
- **FN-3** Wrong-answer-pattern inventory is minimal by design; the Unit-1/2
  mark-scheme corpus is the expansion source.

## 9. Graph integrity tests — ALL GREEN

- Generator gates: ALL GREEN (12 gate families, fail-closed).
- `graph_check.py`: **11/11 groups** (9 prior + new c11-concepts +
  c11-concept-edges).
- `c11_negative_test.py`: **14/14** — 12 corruption classes caught
  (fabricated quote, duplicate node, undeclared endpoint, self-edge,
  duplicate edge, confidence-cap violation, forged HUMAN_VALIDATED, unknown
  relation, prerequisite cycle, 4.15 attachment, premise+consequence
  EXPLAINED_BY, misconception without remediation) + positive control +
  idempotence.

## 10. Deterministic regeneration — PASS

Re-running `c11_concept_pilot.py` over the unchanged decision record is
byte-identical (verified twice: explicit md5 check + negative-test class 13).
No clock reads, no git reads, pinned dates, sorted canonical emission.

## 11. Second-pass agreement (honest κ substitute)

Raw agreement — explicitly **NOT** Cohen's κ (single human rater; faking a
two-rater statistic would violate the project's honesty constraints):
nodes 29/29 confirmed (100%); edges — of the 31 pass-1-asserted edges, 31
confirmed (100%, 6 with notes); the 2 REVIEW_REQUIRED edges were concordantly
NOT asserted by pass 2 (HOLD/REJECT) — keep-vs-drop is the open operator
decision. No pass-2 verdict contradicts a pass-1 assertion.

## 12. Negative control result (4CH1-4.15)

**Zero manufactured coverage.** No node attaches to 4.15; no edge cites the
premise/consequence notes as admissible anchors (attempting it fails
generation G04/G07 and validation c11.5/c11.6 — negative classes 10 and 11
prove the catch). The premise (combustion note, mapped 4.11–4.13) and stated
consequence (acid-rain note, mapped 4.14/4.16) are both present in the corpus;
the demanded "explain how" mechanism is taught nowhere, and the graph says so
(by absence, structurally). Remediation is a corpus decision (new note or
student-book OCR), never graph-side inference. Full detail:
`C11_COVERAGE_GAP_REPORT.md`.

## 13. Remaining corpus gaps

See `C11_COVERAGE_GAP_REPORT.md` (4.15 + boundary concepts + misconception
evidence inventory + EXPLAINED_BY book-OCR constraint + promotion tooling
status).

## 14. What is deliberately NOT done (awaiting authorization)

- No promotion to HUMAN_VALIDATED (operator-only; promotion tooling to be
  built on request, c10_promote pattern).
- No full-graph generation (§16 criteria: this report + review sheet verdicts
  + scoped expansion plan).
- No DB writes, no V2 migration proposal beyond the documented projection
  (§13 of the architecture).

## 15. Expansion criteria checklist (§16 status)

1. All gates green — **met** (§9).
2. Zero unevidenced edges / 100% provenance — **met** (§4/§5).
3. Held list contains the known traps — **met** (premise+consequence,
   examiner-tip-implied misconception, transitively-subsumed prerequisites,
   taught-inline, relation-class ambiguity).
4. Negative control zero coverage — **met** (§12).
5. Operator review of the pilot sheet — **PENDING** (the gate this report
   stops at: `C11_PILOT_REVIEW_SHEET.md`).
6. Scoped expansion plan — **PENDING** (operator decision after review;
   inputs ready: per-section SP counts, boundary-minting policy question,
   mark-scheme inventory).
