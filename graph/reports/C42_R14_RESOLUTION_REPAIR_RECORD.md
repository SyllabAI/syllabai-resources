# T-C42 R14 — R1-Shaped Repair Round over the R13 Defect Inventory (Resolution Repair Record)

| | |
|---|---|
| **Task ID** | T-C42 R14 — the fourth R1-shaped verdict round of the K2-B rework loop (scope §7) |
| **Date** | 2026-10-04 |
| **Operator directive** | "R14-shaped round over the 6 rows" (2026-10-04, zai-web) — firing the R13 record's next-decision menu option verbatim: "an R14-shaped repair round over the 6-row inventory (5 verbatim-cited REATTRIBUTEs + 1 note-level re-point + 1 DEMOTE recommendation — after which the exact stratum computes ≥90% and the gate PASSES with the H3 rows un-held)" |
| **Baseline** | syllabai-resources `origin/main` @ `a953eec` (the R13 re-gate commit; local == remote after fetch, tree clean at round start) |
| **Inventory** | the R13 re-gate's defect inventory: 6 REJECT rows (`scripts/c42_r13_fresh_verdicts.yaml`) = 1 note-level-class + 4 section-level + 1 unresolved-class section; the R13 gate FAILED at Part A exact-stratum 85/95 = 89.5% < 90% (total 97.9%) |
| **Review mode** | operator-delegate (the C12/C13 convention); the human operator retains final sign-off; zero promotion (the substrate stays `SUGGESTED`, the C41-promoted 73 edges untouched; the §18 apply stays R5 / operator gate 3) |
| **Verification** | `scripts/c42_r14_resolution_repair_check.py` → `graph/reports/C42_R14_RESOLUTION_REPAIR_CHECK.json` (C1–C9) |

---

## 1. What fired

The R13 re-gate (the loop's third iteration, commit `a953eec`) closed with a FAIL
by half a point — Part A total 455/465 = 97.9% but the exact stratum at 85/95 =
89.5% against the ≥90%-per-class gate — and a named next-operator decision:
*"an R14-shaped repair round over the 6-row inventory (5 verbatim-cited
REATTRIBUTEs + 1 note-level re-point + 1 DEMOTE recommendation — after which the
exact stratum computes ≥90% and the gate PASSES with the H3 rows un-held), or
fire R5 on the confirmed rows only, or accept the substrate as-is and re-scope —
the operator's call to fire; nothing self-repairs."* The operator's R14
directive ("R14-shaped round over the 6 rows") exercised exactly the first
option, and only that option: per the scope §7 loop discipline, the round fired
the repair lane alone — the deterministic follow-ons (join re-run, substrate
re-build, re-gate) are separate lanes awaiting explicit instruction, exactly as
the iteration-1 directive separated "fire R1" from "fire R2-R3" and "R4 re-gate".

Lane numbering follows the loop's iteration-2/3 precedent (R6/R7/R8/R9, then
R10/R11/R12/R13): this repair round is **R14**, the join re-run is **R15**, the
substrate re-build is **R16**, the re-gate is **R17**. **R5 stays reserved** for
the §18 substrate apply (operator gate 3).

## 2. Surfaces and dispositions

### Surface 1 — id-level (1 anchor, derived deterministically from the R13 fresh roots)

| Anchor | Note | Prior | Disposition | New code | Evidence anchor |
|---|---|---|---|---|---|
| `spcpt_XWbj3PG2n8tdWF2w` | Composite Functions | `4MA1-3.3I` | **CORRECT** | `4MA1-3.2D` (Higher) | the note teaches composite functions end to end (definition, fg notation, numeric substitution, algebraic composition — all five chunk headings; zero plotting content anywhere) — 3.2D verbatim ('understand and find the composite function fg and the inverse function f-1'); 3.3I's demand is plotting graphs and the note teaches none of it. The anchor row is a T-SPEC-7 `P1_name_fragment_join` (score 1.0) — the same defect class as the R1 45-join inventory and the R10 pair. Corroboration: the sibling inverse-functions note already joins H-3.2D correctly (7 store rows) — the re-point adds a second note to a covered code, the R10 2.2A shape. R13 row `f709e1f7f397909e` |

Consequence: **all 5 of the note's store rows re-attribute wholesale** at R15/R16
with the refreshed join; any carried CONFIRM on the note's rows under the 3.3I
join is superseded by the wholesale re-attribution (the R1 45-join precedent,
189 rows). Census, not work: the anchor carries `referenced_by_parts = 40` EQ
part references riding the wrong code downstream — per the scope §3 discipline
the EQ-side repair is a census item for a separate operator decision (the R0
pattern), never silently absorbed into this notes-lane round.

0 anchors cleared this round — the resolution counts stay **222/214/8**.

### Surface 2 — residual continuity (1 row)

`spcpt_QWXhzVp2S3VYZdZc` ("Discrete & Continuous Data") re-affirmed **KEPT
UNRESOLVED** — the R1 PDF-verified reason stands (re-affirmed at R6 and R10);
nothing in the R13 inventory touches it.

### Surface 3 — section-level (4 REATTRIBUTE + 1 DEMOTE, all verdicted; 0 extension rows)

| Key | Current | Action | Target | Evidence anchor |
|---|---|---|---|---|
| properties-of-2d-shapes::2 | `4MA1-4.2C` | REATTRIBUTE | `4MA1-4.1D` (store) | triangle names/types with side-angle properties — 4.1D verbatim ('understand the terms isosceles, equilateral and right-angled triangles and the angle properties of these triangles'); 4.2C is the parallelogram family; the note-level join stands via its quadrilateral sections (ords 3–7). R13 row `8d1dc5c6897f21cd` |
| properties-of-2d-shapes::8 | `4MA1-4.2C` | REATTRIBUTE | `4MA1-4.6A` (ledger) | circle terminology (circumference, diameter, radius, centre) — the C30 ledger Foundation wording of 4.6A ('recognise the terms centre, radius, chord, diameter, circumference, tangent, arc, sector and segment of a circle'; the store's operative 4.6A wording is the Higher intersecting-chord text); the note-level join stands via its quadrilateral sections. R13 row `04b62ae1a6fbd346` |
| two-way-tables::2 | `4MA1-6.1B` | REATTRIBUTE | `4MA1-6.3E` (store) | probabilities from a two-way table (totals, row/column fractions) — the sample-space determination surface, 6.3E verbatim (a two-way table IS the sample-space representation); 6.1B's Higher demand is cumulative-frequency construction and its Foundation wording covers the tabulation methods that carry the note's ords 0–1; the note-level join stands via its tabulation sections. R13 row `3b7f3ef5aa7f26de` |
| sharing-in-a-ratio::1 | `4MA1-1.7E` | REATTRIBUTE | `4MA1-1.7B` (store) | sharing an amount in a given ratio (add the parts, value of one part, scale) — 1.7B verbatim ('divide a quantity in a given ratio or ratios'); the exact inverse of the R9 ratios-and-fdp ord-2 finding (which moved 1.7B→1.7E; this moves 1.7E→1.7B); the note-level join stands via its word-problem sections (ord 3 CONFIRMed fresh in the same R13 draw). R13 row `e770b78477bf94bf` |
| unit-conversions::2 | `4MA1-4.10F` | **DEMOTE_TO_WORKLIST** | — (no target exists) | metric mass conversion (g/kg/tonne); 4.10F's demand is VOLUME conversion; no canonical 188 row teaches metric mass conversion per se — the nearest surface 1.10B is calculations-WITH-units, not unit conversion, and 4.9A's ledger Foundation wording covers linear and area units only (the R6 ord-1 ruling). The scope §4 R1 menu's DEMOTE action, second exercise (first at R10). The note-level join stands (ords 0, 3 genuine volume/capacity content — ord 3 CONFIRMed fresh at R13; ord 1 is the R6 4.9A ruling). R13 row `bccde73549e9e0e6` |

### The note-level question the R13 record left open (1)

The R13 fresh root for composite-functions ord 1 recorded *"the note-level join
is the defect and all its rows re-attribute wholesale"* — an open question at
the note level, not just the sampled section. **Adjudicated at R14: the
note-level join is RE-POINTED 3.3I → 3.2D** (the surface-1 verdict above). The
note's five chunk headings carry composite-function content exclusively
('Composite functions' — the heading-only class under the standing convention;
'What is a composite function?'; 'What notation is used for composite
functions?'; 'How do I substitute numbers into composite functions?'; 'How do I
find composite functions algebraically?'), the anchor's own resolution row is a
T-SPEC-7 name-fragment join (score 1.0, PMT excluded), and 3.2D is not a C30
ledger code (Higher-only), so the both-tier check rests on the store wording
alone — which the note matches verbatim. Consequence: the anchor moves to
`IGCSE_MATHS_A:H-3.2D` (the Higher-tier official-id convention, R10 precedent);
the R15 join census moves composite-functions from the 3.3I join to the 3.2D
join (3.3I keeps its coverage via the R1 drawing-straight-line-graphs
re-attribution family, ords 1/3).

### The heading-only convention — STANDING, no new decision

**`c42-heading-only-convention-1`** (`graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md`)
is in force unchanged. The 4 fresh H3 HOLD rows on the R13 sheet (bounds ord 0,
rearranging-formulae ord 0, expanding-single-brackets ord 2,
applications-of-trigonometry ord 0) are the convention's fail-closed branch
working as designed: they are **not part of the 6-row repair inventory** and
take no R14 action. They un-hold automatically at the R17 re-gate once H1/H2
becomes true — bounds ord 0 un-holds via H2 with the R13 record in the ladder's
source base (bounds ord 2 CONFIRMed fresh at R13); the others un-hold the moment
a content-row CONFIRM of the same note+code accumulates or an H1 anchor ruling
lands. H3 rows still ride R5 only with the operator's explicit per-row sign-off.

### Observations recorded, not verdicted (4)

1. **eq-blast-radius-composite-functions** — the anchor's 40 EQ part references
   ride the wrong 3.3I code downstream; per the scope §3 discipline the EQ-side
   repair is a census item for a separate operator decision (the R0 pattern).
2. **mass-conversion-near-miss** — the proposals packet's top-1 for
   unit-conversions ord 2 is 1.10B (score 0.193), the same near-miss the R13
   root itself examined and rejected; the DEMOTE adjudicates on the ratified
   wordings.
3. **scorer noise** — the R14 proposals packet's top-1s are deliberately noisy
   (e.g. Composite Functions → 2.1A index notation; sharing-in-a-ratio → 4.11A);
   the verdicts adjudicate on the R13 root evidence + the ratified wordings.
4. **expanding-squared-brackets note-join** — carried unchanged from R10: never
   sampled by any reject surface; per §7 nothing self-repairs beyond this
   round's inventory; recorded for a future operator look.

## 3. Amendment mechanics

`scripts/c42_r14_resolution_repair_apply.py` (the gated merge point): baseline
blob `247e02062f1d4ed9` verified pre-write (the R10-repaired file at `a953eec`;
the SME file materialized from git-show under the sparse checkout); preconditions
P1–P7 fail-closed; the R10 repair block preserved via `repair_history` (the
chain now reads R14 → R10 → R6 → R1); the 1 surface row carries R14 provenance
(disposition + prior values verbatim + verdict ref + evidence); the re-point
follows the tier convention (3.2D is a Higher-tier code → `IGCSE_MATHS_A:H-3.2D`
with the store's operative wording); counts recomputed (**222/214/8 —
unchanged**); dated validation clause appended; deterministic byte-identical
re-runs (idempotent verify-only after the marker). The R16-facing override map
`scripts/c42_section_overrides_r14.yaml` is derived deterministically from the
verdict record (4 verdicted REATTRIBUTE + 1 verdicted DEMOTE_TO_WORKLIST + the
note-level re-point pinning the composite-functions anchor as MOVED + the
standing-convention reference) and re-emitted on every run; the R16 re-build
wires it into the c40 tool alongside the R1/R6/R10 maps (the R12 precedent).

## 4. Audit (C1–C9)

`scripts/c42_r14_resolution_repair_check.py` — results recorded in
`graph/reports/C42_R14_RESOLUTION_REPAIR_CHECK.json`:

- **C1** verdicts↔file agreement (1 CORRECT with prior values preserved verbatim
  and matching the R13-recorded wrong code; residual marker) — baseline-free.
- **C2** counts consistency (222/214/8; zero newly-cleared ids).
- **C3** zero-drift: all 220 non-surface rows byte-identical to the pre-R14 blob
  (`a953eec`'s resolution file — the R10-repaired state).
- **C4** code domain: every non-null resolved_code ∈ the canonical 188.
- **C5** top-level: R14 repair block (with the R1+R6+R10 blocks in
  repair_history), validation clause, standing-convention + re-point references.
- **C6** idempotency: re-running the apply verifies and does not rewrite.
- **C7** downstream: `sme_spcpt_verify.py` green (BASE re-pointed, the standing
  script unmodified); the R16 override projection equals the verdict record
  (4 REATTRIBUTE + 1 DEMOTE, the re-point, no subsumed entries).
- **C8** commit state: the R14 round artifacts committed and git-clean.
- **C9** round artifacts: the proposals packet pins the same declared surfaces
  (1 id-level anchor, 5 section rows, 4 H3 continuity rows listed) and the
  standing convention record remains pinned.

## 5. Scope guards and staleness

Chemistry, parsed canonical bundles, the Lane C stores (concepts 82 /
concept_edges 157 = 84 PART_OF + 73 semantic / kinds 72), `spec-links/**`, the
C25–C41 records and the C42 scope/R0–R13 records byte-untouched. The diff
surface of this round is exactly: the amended resolution file + the R14
scripts/verdicts/overrides + the proposals + this record.

**Stale by design after R14:** the T-C32 notes-join, the C40/C42-R12 chunk
substrate and spec-links are now stale relative to the amended resolution —
they refresh at R15/R16; the R17 re-gate re-renders the review surface;
spec-links refresh remains a separate follow-up armed by the R0 census; the
`sme_spcpt_verify` legacy BASE pointer stays on the operator queue.

## 6. What this round does not do

Nothing self-repairs beyond the declared surface. The DEMOTE is a recorded
worklist disposition, not a deletion (the chunk and its identity stay in the
substrate's worklist class). The standing convention promotes nothing and was
not re-decided. The store stays `SUGGESTED`; R5 stays the operator's choice and
is NOT armed by this round — only a GREEN R17 re-gate can arm it (the R13
record's projection: with the 6 rows repaired, the exact stratum computes ≥90%
and the gate PASSES with the H3 rows un-held). The R15/R16/R17 lanes fire only
on explicit operator instruction.
