# T-C42 R10 — R1-Shaped Verdict Round over the R9 Defect Inventory (Resolution Repair Record)

| | |
|---|---|
| **Task ID** | T-C42 R10 — the third R1-shaped verdict round of the K2-B rework loop (scope §7) |
| **Date** | 2026-10-03 |
| **Operator directive** | "an R1-shaped round over the R9 inventory (then R7/R8/R9 again), the heading-only-chunk convention decision" (2026-10-03, zai-web) |
| **Baseline** | syllabai-resources `origin/main` @ `a872cdd` (the R9 re-gate commit; local == remote after fetch, tree clean at round start) |
| **Inventory** | the R9 re-gate's defect inventory: 10 REJECT rows (`scripts/c42_r9_fresh_verdicts.yaml`) = 2 note-level-class + 7 section-level + 1 unresolved-class section; the R9 gate FAILED at Part A exact-stratum 76.8% < 90% (total 95.0%) |
| **Review mode** | operator-delegate (the C12/C13 convention); the human operator retains final sign-off; zero promotion (the substrate stays `SUGGESTED`, the C41-promoted 73 edges untouched; the §18 apply stays R5 / operator gate 3) |
| **Verification** | `scripts/c42_r10_resolution_repair_check.py` → `graph/reports/C42_R10_RESOLUTION_REPAIR_CHECK.json` (C1–C8) |

---

## 1. What fired

The R9 re-gate (the loop's second iteration, commit `a872cdd`) closed with a FAIL
and a named next-operator decision: *"verdict on the R9 defect inventory (an
R1-shaped repair round over the 2 note-level-class joins + 6 section-level rows +
1 unresolved-class section, then R7/R8/R9 re-run again), a convention decision on
the heading-only chunk class, or accept the substrate as-is and re-scope — the
operator's call to fire; nothing self-repairs."* The operator's R10 directive
exercised the first two options in one instruction. Per the scope §7 loop
discipline, the round fired only on that explicit instruction.

Lane numbering follows the loop's iteration-2 precedent (the directive "R1-shaped
verdict round … then R2/R3/R4 re-run" executed as R6/R7/R8): this verdict round is
**R10**, the join re-run is **R11**, the substrate re-build is **R12**, the re-gate
is **R13**. **R5 stays reserved** for the §18 substrate apply (operator gate 3).

The R9 record's parenthetical count ("6 section-level rows") under-enumerates its
own inventory; the authoritative surface is the R9 fill record + fresh verdicts
file: **7 section-level REJECT rows** (types-of-number ords 7 and 8, ratios-and-fdp
ord 2, converting-between-fdp ord 1, classifying-stationary-points ord 2,
basic-percentages ord 1, range-and-quartiles ord 4). This round's P5 pin derives
the surface deterministically from the fresh verdicts file, so the declared
surface and the record agree by construction.

## 2. Surfaces and dispositions

### Surface 1 — id-level (2 anchors, derived deterministically from the R9 fresh roots)

| Anchor | Note | Prior | Disposition | New code | Evidence anchor |
|---|---|---|---|---|---|
| `spcpt_GVgyB5BVfNDYGf8M` | Expanding Triple Brackets | `4MA1-2.2E` | **CORRECT** | `4MA1-2.2A` (Higher) | the note teaches the product of THREE linear expressions — 2.2A's Higher wording verbatim ('expand the product of two or more linear expressions'); 2.2E's Higher wording is algebra-for-proofs AND its C30 ledger Foundation wording covers two brackets only, so the both-tier check exonerates neither tier of 2.2E. R9 row `998c7d61c8cfb1a8` |
| `spcpt_pqWsmktWyMCRfTk6` | Simplifying Algebraic Fractions | `4MA1-1.2A` | **CORRECT** | `4MA1-2.2C` (Higher) | the note teaches manipulating ALGEBRAIC fractions — 2.2C verbatim; 1.2A is numerical-fraction equivalence. Corroboration: all three sibling notes in the same corpus tree join H-2.2C correctly. R9 row `6ab17e03c20b4d95` |

0 anchors cleared this round — the resolution counts stay **222/214/8**.

### Surface 2 — residual continuity (1 row)

`spcpt_QWXhzVp2S3VYZdZc` ("Discrete & Continuous Data") re-affirmed **KEPT
UNRESOLVED** — the R1 PDF-verified reason stands (re-affirmed at R6); nothing in
the R9 inventory touches it.

### Surface 3 — section-level (7 REATTRIBUTE + 1 DEMOTE, all verdicted; 0 extension rows)

| Key | Current | Action | Target | Evidence anchor |
|---|---|---|---|---|
| types-of-number::7 | `4MA1-1.1G` | REATTRIBUTE | `4MA1-1.4B` (ledger) | square numbers — the C30 ledger Foundation wording ('calculate squares, square roots, cubes and cube roots'); the R6 ord-9 class, ords 7–8 unsampled there. R9 row `41dcd33bd8bca1d9` |
| types-of-number::8 | `4MA1-1.1G` | REATTRIBUTE | `4MA1-1.4B` (ledger) | cube numbers — same class. R9 row `0df9dfd058a1ec92` |
| ratios-and-fdp::2 | `4MA1-1.7B` | REATTRIBUTE | `4MA1-1.7E` | ratio+FDP word problems — 1.7E verbatim; the note-level join stands via its divide-in-a-ratio sections. R9 row `9ae9976901a946fe` |
| converting-between-fdp::1 | `4MA1-1.2G` | REATTRIBUTE | `4MA1-1.6C` | percentage→decimal — 1.6C verbatim. R9 row `e54fc84c271915b3` |
| classifying-stationary-points::2 | `4MA1-3.4C` | REATTRIBUTE | `4MA1-3.4D` | graph-shape classification — 3.4D verbatim; the operator's own R6 ord-3 class. R9 row `db3eb3cb32adf399` |
| basic-percentages::1 | `4MA1-1.6F` | REATTRIBUTE | `4MA1-1.6A` (ledger) | what-a-percentage-is — the C30 ledger Foundation wording; the R1 ord-2 class on this note. R9 row `bcba14c9e69b6c10` |
| range-and-quartiles::4 | `4MA1-6.2B` | REATTRIBUTE | `4MA1-6.2C` | find-the-quartiles procedure — 6.2C's IQR surface; 6.2B is the spread-CONCEPT demand. R9 row `26b042684607e045` |
| related-calculations::2 | `4MA1-1.8D` | **DEMOTE_TO_WORKLIST** | — (no target exists) | inverse-operations content; no canonical 188 row teaches it (the only 'inverse' wordings are 1.2H multiplicative inverses, 2.5A inverse proportion, 3.2D inverse functions). The scope §4 R1 menu's DEMOTE action, exercised for the first time in the loop. R9 row `988bcf024c79e126` |

### The note-level adjudication the R9 record left open (1)

The R9 fresh root for related-calculations ord 2 recorded *"the note-level join
1.8D looks like a T-SPEC-era name-fragment approximation"* — an open question,
not a verdict. **Adjudicated at R10: the note-level join STANDS.** The note's
ord-3 section ("What types of related calculations are there?", 2423 chars)
carries genuine estimation-to-check content — an Exam Hint ("Use estimation to
check your answer is sensible. Rounding numbers to one significant figure can
help you estimate the correct order of magnitude") and a full worked example
("Estimate 68.8 ÷ 4.3 by rounding each number to one significant figure; 70 ÷ 4 =
17.5") — which is 1.8D's demand ('use estimation to evaluate approximations to
numerical calculations') taught verbatim. 1.8D is not a C30 ledger code
(Foundation-only, the same estimation wording at both tiers), so this is not a
wording-tier artifact. Consequence: the note keeps its 1.8D anchor (ords 0, 1, 3
stay anchored; ord 0 is the heading-only class, resolved by the convention), and
only the ord-2 section DEMOTEs. The R11 join census is unchanged except as the
two re-points move it.

### The heading-only-chunk convention decision (the directive's third clause)

**`c42-heading-only-convention-1`** — recorded in full at
`graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md` (+ JSON mirror). Summary: a
heading-only chunk (norm(text) == norm(heading), ~204 of 862 anchored rows) is a
**structural slice of the corpus's own spec_point span**, not a semantic defect;
its row carries the SPAN's standing via a fail-closed evidence ladder —
**H1** verdict standing (an operator id-verdict or an R10 note-level "stands"
adjudication on the anchor) → **H2** content standing (≥1 content-row CONFIRM of
the same note + code at R4/R9) → **H3** otherwise HOLD, explicit and recorded
(un-holds automatically when H1/H2 becomes true). A heading-only row's own prior
CONFIRM (including C40-era carried confirms) never satisfies H2 — only
content-row confirms count; a reject-free history alone is never evidence.
Applied to the 13 HOLD rows on the R9 sheet: **11 resolve to CONFIRM on positive
evidence (2 × H1 + 9 × H2); 2 stay HOLD under H3**
(`drawing-graphs-from-tables` ord 0, `vector-proof` ord 0 — zero content confirms
anywhere; they un-hold the moment one accumulates). H3 rows are not auto-promoted
at R5: they ride the §18 apply only with the operator's explicit per-row sign-off.
The human operator retains final sign-off on the convention itself and may reverse
it before R5.

### Observations recorded, not verdicted (2)

1. **expanding-squared-brackets note-join** — the corpus's "Expanding Squared
   Brackets" note also joins 2.2E and reads closer to the expansion family than to
   algebra-for-proofs; never sampled by any reject surface, so per §7 nothing
   self-repairs beyond this round's inventory. Recorded for a future operator look.
2. **scorer noise** — the R10 proposals packet's top-1s are deliberately noisy
   (e.g. Expanding Triple Brackets → 1.1F; Related Calculations → 1.10C); the
   verdicts adjudicate on the R9 root evidence + the ratified wordings.

## 3. Amendment mechanics

`scripts/c42_r10_resolution_repair_apply.py` (the gated merge point): baseline
blob `466250eaa21fada2` verified pre-write (the R6-repaired file at `a872cdd`);
preconditions P1–P7 fail-closed; the R6 repair block preserved via
`repair_history`; all 2 surface rows carry R10 provenance (disposition + prior
values verbatim + verdict ref + evidence); both re-points follow the tier
convention (2.2A and 2.2C are Higher-tier codes → `IGCSE_MATHS_A:H-2.2A` /
`IGCSE_MATHS_A:H-2.2C` with the store's operative wordings); counts recomputed
(**222/214/8 — unchanged**); dated validation clause appended; deterministic
byte-identical re-runs (idempotent verify-only after the marker). The
R12-facing override map `scripts/c42_section_overrides_r10.yaml` is derived
deterministically from the verdict record (7 verdicted REATTRIBUTE + 1 verdicted
DEMOTE_TO_WORKLIST + the note-level adjudication pinning the
related-calculations anchor as STANDING + the convention reference) and re-emitted
on every run.

## 4. Audit (C1–C8)

`scripts/c42_r10_resolution_repair_check.py` — results recorded in
`graph/reports/C42_R10_RESOLUTION_REPAIR_CHECK.json`:

- **C1** verdicts↔file agreement (2 CORRECT with prior values preserved verbatim
  and matching the R9-recorded wrong codes; residual marker) — baseline-free.
- **C2** counts consistency (222/214/8; zero newly-cleared ids).
- **C3** zero-drift: all 219 non-surface rows byte-identical to the pre-R10 blob
  (`a872cdd`'s resolution file — the R6-repaired state).
- **C4** code domain: every non-null resolved_code ∈ the canonical 188.
- **C5** top-level: R10 repair block (with the R1+R6 blocks in repair_history),
  validation clause, convention + adjudication references.
- **C6** idempotency: re-running the apply verifies and does not rewrite.
- **C7** downstream: `sme_spcpt_verify.py` green (BASE re-pointed, the standing
  script unmodified); the R12 override projection equals the verdict record
  (7 REATTRIBUTE + 1 DEMOTE, the adjudication, no subsumed entries).
- **C8** commit state: the R10 round artifacts committed and git-clean.

## 5. Scope guards and staleness

Chemistry, parsed canonical bundles, the Lane C stores (concepts 82 /
concept_edges 157 = 84 PART_OF + 73 semantic / kinds 72), `spec-links/**`, the
C25–C41 records and the C42 scope/R0–R9 records byte-untouched. The diff surface
of this round is exactly: the amended resolution file + the R10 scripts/verdicts/
overrides + the proposals + the convention record + this record.

**Stale by design after R10:** the T-C32 notes-join, the C40/C42-R12 chunk
substrate and spec-links are now stale relative to the amended resolution — they
refresh at R11/R12; the R13 re-gate re-renders the review surface; spec-links
refresh remains a separate follow-up armed by the R0 census; the
`sme_spcpt_verify` legacy BASE pointer stays on the operator queue.

## 6. What this round does not do

Nothing self-repairs beyond the declared surface. The DEMOTE is a recorded
worklist disposition, not a deletion (the chunk and its identity stay in the
substrate's worklist class). The convention decision promotes nothing: it governs
how the R13 fill *judges* the class, under per-row provenance, reversible by the
operator. The store stays `SUGGESTED`; R5 stays the operator's choice and is NOT
armed by this round — only a GREEN R13 re-gate can arm it.
