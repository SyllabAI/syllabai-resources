# C40 — K2 Lane B substrate review sheet FILLED (operator-delegate)

**Generated:** 2026-10-02T08:04:53+00:00  |  **Baseline:** `f3b0634ffeaf842d687d0a555e5e5757a10959d7`
**Reviewer:** Super Z (GLM agent), acting as operator-delegate under the operator's lane directive (fire K2-B, 2026-10-02, zai-web); the human operator retains final sign-off; per the anti-forgery rule nothing here flips the store

## Method

- **Mechanical layer:** every sampled row re-verified by script — quote-in-chunk
  containment under the shared `norm()`, chunk `sha256_16`/heading/chars agreement
  with a fresh re-chunking, 1:1 mapping-id presence in the store, all rows
  SUGGESTED — **468/468 PASS**.
- **Semantic layer:** per-row topical fidelity against the SP's official wording
  and the chunk content, root-caused at the NOTE-JOIN level (the T-SPEC
  resolution's note→SP pairs) with section-level overrides where the note is
  right but the sampled section is not.

## Result

| Part | Rows | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|
| A total | 468 | 351 | 117 | 0 | 75.0% |
| A stratum exact (score == 1.0) | 98 | 53 | 45 | 0 | 54.1% |
| A stratum partial (score < 1.0) | 238 | 177 | 61 | 0 | 74.4% |
| A stratum none (score n/a) | 132 | 121 | 11 | 0 | 91.7% |
| B (worklist) | 79 | 79 DEFER | | | 79/79 decided |

**Gate outcome: FAILS** — Part A per-class precision is below the 90% gate on the
exact (54.1%) and partial (74.4%) strata; the none stratum passes (91.7%) but the
gate requires every class. **The promotion is NOT authorized by this fill.** The
store stays `SUGGESTED`.

## The defect inventory (the fill's product)

- **45 note-level joins** are semantically wrong — the T-SPEC
  resolution file maps the note to an unrelated SP, and the deterministic T-C32
  id-join inherits it (examples: 'Vector Diagrams'→6.1C cumulative frequency,
  'Tree Diagrams'→6.1C, 'Bar Charts & Pictograms'→6.1A histograms,
  'Negative Numbers'→1.4A surds, 'Exchange Rates'→3.4C differentiation,
  'Coordinates'→3.3B graph transformations, 'Mean Median & Mode'→6.2B spread).
  Every sampled chunk of such a note rejects with the root cause recorded.
- **16 section-level scope differences** — the note is rightly joined
  but the sampled section teaches a different SP's content (examples: the
  number-line section under the Cartesian-graph SP 2.8D; the sphere/cone
  sections under the cylinder SP 4.10D).
- The C31 §3 wording crosscheck (202/202 EXACT) verified registry CONSISTENCY
  (resolution wording == store wording for the mapped code), not name→code
  semantics — this fill is the first gate to measure the semantics, working as
  designed.

## Disposition

Zero silent promotion; zero silent repair. The rework path — a T-SPEC
resolution-repair round over the implicated joins, then the T-C32 join re-run
and the substrate re-build — is the operator's decision. The substrate's
SUGGESTED surface, its census, and the 111-code coverage bound all stand.

