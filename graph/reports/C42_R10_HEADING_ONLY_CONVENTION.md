# C42 R10 — The Heading-Only Chunk Convention Decision (`c42-heading-only-convention-1`)

| | |
|---|---|
| **Task ID** | T-C42 R10 (the third R1-shaped verdict round of the K2-B rework loop, scope §7) |
| **Decision ID** | `c42-heading-only-convention-1` |
| **Date** | 2026-10-03 |
| **Operator directive** | "an R1-shaped round over the R9 inventory (then R7/R8/R9 again), the heading-only-chunk convention decision" (2026-10-03, zai-web) — the directive's third clause orders this decision |
| **Mode** | Operator-delegate (the C12/C13 convention): the ruling is recorded here for the human operator's final sign-off; it is reviewable and reversible by the operator before R5. Zero promotion happens anywhere in this round. |
| **Enforcement** | Mechanically enforced by the R13 re-gate fill (`scripts/c42_r13_regate_fill.py`) and audited by its check battery; fail-closed. |

---

## 1. The problem this decision closes

The c40 chunker (`c40-chunk-convention-1`, pinned) cuts each note into chunks whose
text is "its own heading + rendered content" (the C10 heading-quote lesson). Where a
section carries no rendered content beyond its heading, the chunk's text IS the
heading. Under the fill standard, such a chunk **cannot be semantically confirmed
from its own content** — there is nothing beyond the heading to quote or weigh — so
every fresh judgment of one lands as a HOLD ("evidence insufficient to decide").

The class is **structural, not defective**. Ground truth (computed through the pinned
chunker over all 191 notes): **204 of the 862 anchored chunk rows (~24%) are
heading-only** (norm(text) == norm(heading)); 110 of them sit in the exact stratum.
Their joins are inherited from the corpus's own `spec_point` span markers — the same
mechanism every anchored row rides — and across three verdict rounds (R1, R6, R10)
and two full re-gates (R4, R9) the class has produced exactly **zero note-level
rejects attributable to the heading-only chunks themselves**: every REJECT in the
loop's history was a content-row finding.

Until now the class was handled ad-hoc per row: the operator RETAIN-ruled two rows at
R1, the R4/R9 fills HOLDed freshly-sampled class members explicitly, and the R9 sheet
carried 13 HOLD rows (11 fresh + 2 carried). Left as-is, the loop cannot converge:
even with every R9 REJECT repaired, unconfirmable HOLDs re-appear in every fresh
draw of the exact stratum, and the R5 §18 apply could never promote the class. The
operator's directive orders this closed by decision, not by waiver.

## 2. The decision

**A heading-only chunk is a structural slice of the corpus's own spec_point span —
not a semantic defect and not an evidence-free row. Its chunk→SP row carries the
SPAN's standing, resolved per row by the following fail-closed evidence ladder:**

- **H1 — verdict standing.** The row's span anchor carries an operator id-verdict
  (R1 AFFIRM/CORRECT, R6 CORRECT, R10 CORRECT) or an R10 recorded note-level
  "join stands" adjudication (`note_level_adjudications` in the R10 verdict record)
  → **CONFIRM**, with provenance naming the round, the anchor id and the ruling.

- **H2 — content standing.** The row's note carries at least one CONFIRM verdict at
  R4 or R9 on the same `spec_code` whose own chunk is NOT heading-only (i.e. real
  rendered content of the same note, joined to the same code, already confirmed by
  a prior round's judgment) → **CONFIRM**, with provenance naming the confirming
  row(s). The corpus's span marker scopes the heading-only chunk to exactly the
  content those rows teach; the span's confirmed content is the row's evidence.

- **H3 — no positive evidence → HOLD (fail-closed).** A heading-only row resolved
  by neither H1 nor H2 stays **HOLD** — explicit, recorded, never silently
  confirmed, never re-rejected for being heading-only. It un-holds automatically at
  a later round the moment H1 or H2 becomes true (e.g. a content row of its note is
  sampled and confirmed).

**What the decision deliberately does NOT do:**

- It does **not** allow a heading-only row's own prior CONFIRM (including the
  C40-era carried confirms of heading-only rows, the loosest gate in the chain) to
  satisfy H2 — that would be the exact circularity the convention closes. Only
  content-row confirms count.
- It does **not** count a REJECT-free history alone as evidence (absence of findings
  is not a finding); there is no "clean history" branch.
- It does **not** touch chunk identity, the chunker, or any chunk bytes (the
  `c40-chunk-convention-1` forward contract and the W3 invariant are unaffected);
  the decision moves verdicts, never rows.
- It does **not** promote anything: H1/H2 CONFIRMs are review-surface verdicts with
  recorded provenance; the store stays `SUGGESTED` until the operator fires R5.

**R5 eligibility:** H1/H2-resolved rows are ordinary CONFIRM rows for the §18 apply.
H3 rows are NOT auto-promoted: they ride R5 only with the operator's explicit
sign-off of this convention plus a per-row listing, or stay `SUGGESTED` (recorded,
not forced) — the operator's choice at gate 3.

## 3. Detection (mechanical, fail-closed)

A chunk is heading-only iff `norm(chunk text) == norm(chunk heading)` under the
shared `norm()` of the pinned c40 chunker, computed from a fresh re-chunking at
every fill (never from the store's cached `chars` field). The detector is a
pure function of chunk bytes; any drift between the store row and the fresh
re-chunking fails the fill's mechanical layer first.

## 4. Application to the 13 rows on the R9 sheet (computed, not assumed)

| # | Code | Note (slug) | Ord | R9 source | Ladder | Resolves via |
|---|---|---|---|---|---|---|
| 1 | 4MA1-1.2A | algebraic-fractions | 0 | r9-fresh HOLD | **H1** | R10 CORRECT `spcpt_pqWsmktWyMCRfTk6` (1.2A → 2.2C; the row rides the repaired join) |
| 2 | 4MA1-1.8D | related-calculations | 0 | r9-fresh HOLD | **H1** | R10 note-level adjudication: the 1.8D join STANDS (ord-3 estimation-to-check surface) |
| 3 | 4MA1-1.4C | algebraic-roots-and-indices | 0 | r1-section-override HOLD | **H2** | content confirms: R4/R9 rows of the same note on 4MA1-1.4C (2, non-heading-only) |
| 4 | 4MA1-1.7E | sharing-in-a-ratio | 0 | r9-fresh HOLD | **H2** | content confirms: 2 (R4/R9, same note + code) |
| 5 | 4MA1-1.9A | operations-with-standard-form | 2 | r9-fresh HOLD | **H2** | content confirm: ord 4 "Division" (R9 fresh CONFIRM, same note + code) |
| 6 | 4MA1-3.3I | drawing-graphs-from-tables | 0 | r9-fresh HOLD | **H3** | no verdict on the anchor; zero content-row confirms of the note — HOLD (fail-closed) |
| 7 | 4MA1-4.6C | the-alternate-segment-theorem | 0 | r9-fresh HOLD | **H2** | content confirm: 1 |
| 8 | 4MA1-4.9C | adding-and-subtracting-areas | 0 | r9-fresh HOLD | **H2** | content confirms: 2 |
| 9 | 4MA1-4.10D | surface-area | 0 | r1-section-override HOLD | **H2** | content confirms: 4 (the R1-REATTRIBUTE'd sections and siblings) |
| 10 | 4MA1-5.1D | introduction-to-vectors | 0 | r9-fresh HOLD | **H2** | content confirms: 2 |
| 11 | 4MA1-5.1G | vector-proof | 0 | r9-fresh HOLD | **H3** | no verdict on the anchor; zero content-row confirms — HOLD (fail-closed) |
| 12 | 4MA1-6.2B | averages-from-tables | 0 | r9-fresh HOLD | **H2** | content confirms: 5 (the mode-wording artifact class the R1 record already RETAIN-ruled) |
| 13 | 4MA1-6.3G | relative-and-expected-frequency | 0 | r9-fresh HOLD | **H2** | content confirm: 1 |

**Result: 11 of 13 resolve to CONFIRM on positive evidence (2 × H1 + 9 × H2); 2 stay
HOLD under H3** (`drawing-graphs-from-tables` ord 0, `vector-proof` ord 0 — their
notes have never had any content row sampled-and-confirmed; they un-hold the moment
one is). The two H3 rows do not block the gate: even with both drawn, the R13 exact
stratum computes ≈ 97.9% ≥ 90%.

## 5. Store-wide effect at the R13 re-gate

Every heading-only row in the sample is resolved by the same ladder mechanically;
each verdict's provenance names its branch and its evidence reference(s). The
remaining HOLD population after R13 is expected to be small, explicit, and
monotonically shrinking as content rows accumulate confirms — a convergent design,
in place of the previous non-converging per-row ad-hoc HOLDs.

## 6. Provenance chain

- Directive: the operator's R10 directive, third clause (2026-10-03, zai-web).
- Evidence base: the R4/R9 review verdict records, the R1/R6/R10 verdict records,
  the pinned c40 chunker's fresh re-chunking, the T-C32 join's wording census.
- Decision record: this file (+ the JSON mirror `C42_R10_HEADING_ONLY_CONVENTION.json`).
- Enforcement: `scripts/c42_r13_regate_fill.py` (the ladder, per-row provenance),
  audited by `scripts/c42_r13_regate_check.py`.
- Sign-off: the human operator retains final sign-off; reversible before R5.
