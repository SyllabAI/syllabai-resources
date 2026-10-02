# C38 — Subject-#2 K2-C-6 Gate Record — igcse-maths-a (4MA1 Higher), Lane C Batch B06

| | |
|---|---|
| **Task ID** | T-C38 (K2-C-6 of the C31 K2 scope — Lane C, batch B06 of 16) |
| **Version** | 1.0 — batch B06 authored to the verdict gate. NOTHING is promoted; the maths-a concepts store still does not exist and nothing in this landing creates it. The verdict step is reserved to the operator. |
| **Date** | 2026-10-02 |
| **Operator directive** | "K2-C-6" (2026-10-02, zai-web, inline) — gate K2-C-6 of the C31 §8 sequence (commission → author → review → verdict), with K2-B not yet run and the B01..B05 verdicts not yet recorded: the C31 scope record §6 provides for early Lane C batches before Lane B, and B01..B05 remain authored-to-gate packets whose SUGGESTED rows promote only through the operator's own verdicts, so B06 proceeds on the notes-join + ratified spec-text substrate alone at the same first-apply store state. The T-C37 record anticipated exactly this commissioning (the B06 packet inherits the B05 audit's superseding 3-code boundary map and all five held quarantines, with TWO future-batch holds landing in this slice — B05-H-06, the 2.2E double/triple-bracket family whose pages are join-carried to 2.2E, and B04-H-06, the 2.5A inverse-proportion family the ÷5-division row documents) |
| **Baseline** | syllabai-resources `origin/main` @ `303cac270f48d3af3224fc1a1592eb6450c65c32` (T-C37 K2-C-5 B05 authored-to-gate landing) at commissioning time; re-based over `6c12ecf63678e3d1814eba682d664f44cb82714a` (PR #16 — the chemistry c12 test-repair, single file `scripts/c12_negative_test.py`, verified disjoint) for landing; the battery's freeze gate re-run at the landing baseline |
| **Predecessors** | `C37_IGCSE_MATHS_A_K2C5_BATCH05` (the replayed pattern, the superseding 3-code boundary map and the B05 held quarantine this packet inherits — B05-H-06 LANDS in this slice); `C36_IGCSE_MATHS_A_K2C4_BATCH04` (whose B04-H-06 hold ALSO LANDS here); `C35_IGCSE_MATHS_A_K2C3_BATCH03`, `C34_IGCSE_MATHS_A_K2C2_BATCH02` and `C33_IGCSE_MATHS_A_K2C1_BATCH01` (the B01/B02/B03 quarantines, inherited through the chain); `C31_IGCSE_MATHS_A_K2_SCOPE` (§5 batch plan, §8 gate row, §3 coverage-profile standing input); `C32_IGCSE_MATHS_A_K2A_LANE_A` (the notes-join substrate every Lane C batch anchors on); `C30_MATHS_A_TIER_DEDUPE_LEDGER` (the Foundation variants that explain this batch's substrate alignment on 2.2D/2.2E); the chemistry C11 §16 machinery incl. the batch-10/11 misconception shapes |
| **Verification** | `scripts/c38_maths_a_batch06_check.py` → `graph/reports/C38_BATCH06_CHECK.json` (G1–G7 all PASS, exit 0) |

---

## 1. What was commissioned and authored

The directive `K2-C-6` fired the SIXTH Lane C batch of the C31 §8 sequence. The
commissioning record `scripts/c38_maths_a_batch06_authorization.yaml` authorizes exactly
one batch — the 12 specification points **4MA1-2.2D..4MA1-2.5A (global_order 61–72)** —
and reserves the verdict step to the operator. The slice spans the 2.2 tail that closes
the algebraic-manipulation block (completing the square; algebraic proof; the Foundation
simple-quadratic factorising row), the whole of 2.3 (notational conventions; substitution;
formulae from contexts; deriving; changing the subject where the subject appears once),
the whole of 2.4 (solving linear equations; setting them up from given data) and the 2.5
head (direct and inverse proportion with their graphical representations). Like B02..B05
it is a MIXED-TIER slice — 8 Foundation rows plus FOUR Higher rows (2.2D, 2.2E, 2.3A,
2.5A) — and all 12 rows carry zero damage flags. Subtopic titles for 2.2/2.3/2.4/2.5 are
NULL in the ratified topics store and are NOT invented (null-by-design honored).

AUTHORED (`scripts/c38_maths_a_batch06_decisions.yaml`):

- **12 CONCEPT nodes** (one per slice SP family): completing-the-square, algebraic-proof,
  factorising-simple-quadratics (the x² + bx + c family — the mirror of B05's authored
  2.2B node), rearranging-formulae-harder-cases (the subject-twice/powered arm 2.3A's own
  wording names), algebraic-notation-conventions (the B05 audit's 2.3B prediction
  landing), substitution, formulae-from-context, deriving-formulae,
  rearranging-formulae (subject appears once), solving-linear-equations,
  forming-and-solving-equations, direct-and-inverse-proportion
- **3 MISCONCEPTION nodes** — the EIGHTH, NINTH and TENTH maths-a mints, each on a
  mark-scheme row that documents the wrong-answer class with the corrective content in
  the same file (the chemistry contract): `4MA1-MIS-INVERSE-OPERATION-ORDER` riding 2.3F
  on the rearranging-formulae MS Q10 order rows ("If you divide the left hand side by 3,
  then subtract 2 from both sides, you get the incorrect answer of x = y/3 − 2" + two
  siblings); `4MA1-MIS-SUBJECT-POWER-MISHANDLING` riding 2.3A on the rearranging-formulae
  MS Q23 power rows ("If you square both sides and then multiply the powers together on
  the y, you will get the incorrect answer of w = y⁶" + two siblings — the arm 2.3A's own
  wording names: "a power of the subject occurs"); `4MA1-MIS-INVERSE-VARIATION-DIVISION-
  CONFUSION` riding 2.5A on the algebra-toolkit MS Q8 ÷5 row ("You may get the incorrect
  answer of ÷5 if you confuse dividing by 2 with dividing by an x value that is
  doubled") — the LANDING of the row B05 pre-announced (cited NOWHERE in B05, the
  B04-H-06 sibling whose home family is this batch's 2.5A row). NONE of the EIGHT prior
  maths-a classes is re-minted; the factorising MS "allowing sign errors" rows remain
  credit-tolerance annotations, and the NOTE-page "common error"/"common mistake" rows
  (formulas-where-subject-appears-twice.md, solving-linear-equations.md) are not
  mark-scheme documentation — all recorded with dispositions, never minted; mint-vs-
  trivia and home rows operator-reserved B06-ID-02/03
- **14 edges** (8 REQUIRES_PREREQUISITE — the in-slice teaching sequence: completing the
  square on the quadratic fluency it transforms; algebraic proof on the factorising its
  chains perform; harder rearranging on the appears-once mechanic it extends;
  rearranging on the familiar-formulae stock it operates on; substitution on the
  notational conventions it presumes; forming-and-solving on the solve mechanic it ends
  in and the expression-deriving it starts from; proportion on the
  rearrange-to-standard-form move its own MS row names — + 3 WRONG_ANSWER_PATTERN +
  3 REMEDIATED_BY, remediation target = WAP target per the B1-E-25 pattern)
- **8 held candidates** (B06-H-01..08 — three CROSS-BATCH-TARGET-UNPROMOTED [to B05's
  expanding-products node behind factorising and behind the solving walks; B06-H-03 the
  LANDING of held B04-H-06, the would-be edge from this batch's 2.5A node now aimed at
  B04's direct-proportion node], one CROSS-BATCH-TARGET-FUTURE-BATCH-flavoured landing
  re-record [B06-H-02 the LANDING of held B05-H-06 — the would-be edges from B05's
  expanding-products node now aimed at the authored 2.2E node, with the B05-ID-03
  home-row question now naming the concrete alternative], and four
  COVERAGE-UNJOINED-SUBSTRATE [the direct-proportion page joined to B04's 1.7D;
  completing-the-square.md joined to 2.7B; solving-linear-equations.md joined to the
  in-slice neighbour 2.4B; both rearranging pages joined to 2.3F while 2.3A carries
  zero joins]; B01..B05 quarantines inherited untouched, all 37 prior held ids preserved)
- **12 command kinds** (10 APPLY_PROCEDURE + 2 UNDERSTAND_RELATION — the two
  'understand'-leading rows 2.2F and 2.3A carry UNDERSTAND_RELATION forward; KNOW_TERM
  has no instance, recorded) / 3 operator-reserved identity decisions (B06-ID-01 the
  2.2B/2.2F quadratic-factorising mirror pair authored as TWO nodes on the store's own
  row split — the mirror of the B05-ID-01 bounds ruling; B06-ID-02 the power-class
  mint's home row 2.3A vs 2.3F; B06-ID-03 the three mints' mint-vs-trivia rulings and
  the division-confusion/order-class home rows). 100 evidence anchors (25 NOTE / 37 SPEC
  / 38 MARK_SCHEME), every quote byte-verified under the batch-8 G03/c11.4 convention;
  the UNJOINED-CORPUS NEGATIVE CONTROL runs at sixth-batch strength — every NOTE
  citation is one of the 14 join-carried notes and PAIR-BACKED (node attachments at
  their SP; edge evidence at an endpoint SP, the B02 strength carried forward); the
  uncited-join census is EMPTY — all 14 join-carried pages cited, each for exactly the
  SP it is joined to, the third fully-cited batch of the series, no anchor padded; the
  corpus's unjoined neighbours (completing-the-square — joined to 2.7B; direct-proportion
  — joined to B04's 1.7D; equations-and-problem-solving — joined to 4.11C; the
  algebra-toolkit and substitution pages — joined to B05's rows; et al.) are cited
  NOWHERE. SLICE-HONESTY DISCOVERY (FP-B06-1, recorded on the affected derivation notes,
  never repaired): the three higher-preferred rows' substrate sits exactly as the C30
  tier-dedupe ledger's Foundation texts demand — factorising (common factors) for 2.2D;
  simple bracket expansion for 2.2E alongside the Higher proof page; and 2.3A carrying
  ZERO joins with the twice/powered substrate on 2.3F's anchors (the appears-twice page
  is literally named for the 2.3A arm) — the nodes CORE the ratified Higher wordings and
  cite the pages for the shared substrate. SLICE HONESTY: subtopic titles for
  2.2/2.3/2.4/2.5 are NULL in the ratified topics store and are NOT invented; 0
  damage-flagged rows; the second FULL MS-evidence profile of the series (all 12 SPs —
  a property of the mark-scheme-dense slice, no anchor padded).

## 2. The coverage profile (the C31 §3 standing per-batch statement)

| measure | value |
|---|---|
| slice SPs | 12 (global_order 61–72) |
| tier mix | 4 Higher (2.2D, 2.2E, 2.3A, 2.5A) + 8 Foundation (2.2F, 2.3B, 2.3C, 2.3D, 2.3E, 2.3F, 2.4A, 2.4B) |
| notes-joined SPs | 6 (2.2D, 2.2E, 2.2F, 2.3F, 2.4B, 2.5A) — 15 join rows over 14 distinct note files (the double-bracket page joins twice, once per anchor) |
| spec-text-only SPs | 6 (2.3A, 2.3B, 2.3C, 2.3D, 2.3E, 2.4A) |
| MS-evidenced SPs | 12 — ALL slice rows (the second full MS profile of the series) |
| join-carried but uncited pages | 0 — the EMPTY uncited-join census |
| damage-flagged rows in the slice | 0 |
| misconceptions minted | 3 (the eighth, ninth and tenth maths-a mints; no prior class re-minted) |
| practicals | none (the maths-a practicals store is 0-row by design) |

## 3. Machine verification

`scripts/c38_maths_a_batch06_check.py` — G1–G7 ALL PASS, exit 0
(`graph/reports/C38_BATCH06_CHECK.json`):

- **G1** commissioning record AUTHORIZED, verbatim directive `K2-C-6`, 10 standing
  invariants
- **G2** record shape — 12 CONCEPT + 3 MISCONCEPTION nodes / 14 edges (8 RP + 3 WAP +
  3 REMEDIATED_BY) / 8 held / 12 command kinds / 3 identity decisions; every slice SP
  covered; zero promotions (SUGGESTED everywhere)
- **G3** preverify `c38_maths_a_batch06_preverify.py` 35/35 (incl. sixth-batch store
  state = exactly the 5 K1 stores, B01+B02+B03+B04+B05 unapplied; the 3
  higher-preferred rows carry the tier_dedupe_note; the B05 boundary map's 2.3B
  IN-SLICE; 37 prior held ids preserved)
- **G4** quote probe 100/100 (persistent cat-file channel, 22 git-batch reads + 1 disk;
  kinds 25 NOTE / 37 SPEC / 38 MARK_SCHEME)
- **G5** review sheet byte-reproducible (json twin modulo generated_utc)
- **G6** freeze integrity @ `6c12ecf63678e3d1814eba682d664f44cb82714a` (the PR #16 c12 test-repair merge 6c12ecf verified disjoint before landing — single file scripts/c12_negative_test.py) — zero
  out-of-footprint paths; the corpus, the parsed canonical plane and every store
  byte-identical
- **G7** standing checkers graph_check + check_no_hardcode green

Term audit (`c38_maths_a_batch06_term_audit_probe.py`): 66 terms → 8 match terms, all
in-slice except three non-slice codes — the audit SUPERSEDES B05's as the B07..
boundary-ruling map {4MA1-1.7C, 4MA1-1.7D (B04's rows via the proportion vocabulary),
4MA1-2.7B new (the solving-quadratics row the 'completing the square' vocabulary
shares — the page named for B06's 2.2D substance lives there)}; the B05-inherited 2.3B
is now IN-SLICE (the audit prediction landing) and 1.4C/3.4B/1.6A/1.6B/4.4C/6.2A/6.2D/
6.3G remain future.

## 4. What the verdict gate decides

The verdict step (12+3 nodes, 14 edges, 8 held checkboxes + 3 identity decisions) is
RESERVED to the operator. A `scripts/c38_maths_a_batch06_verdicts.yaml` template lands
with the verdict session; verdicts encode through the intake-conformance check, the §18
apply step then (and only then) materializes/grows the maths-a
concepts/concept_edges/spec_command_kinds stores with exactly the promoted rows from ALL
authored batches — B01's (13), B02's (14), B03's (14), B04's (12), B05's (12) and B06's
(12) derived PART_OF rows (77 total) materialize there — and all six quarantines
(B01-H-01..05, B02-H-01..08, B03-H-01..08, B04-H-01..08, B05-H-01..08, B06-H-01..08 =
45 held ids) rule together. Nothing here is live until the operator's verdicts land.

## 5. Scope guards honored this landing

Zero bytes in `graph/igcse-chemistry/**`, `parsed/**` canonical JSON, or the SME corpora;
the C25–C30 and C31–C37 records unedited; no core or hub serving changes; no K3/K4 work;
the maths-a graph dir still carries exactly the 5 K1 stores (machine-verified G3/G6);
the parallel chemistry C11 program untouched; every authored row carries the batch
provenance namespace (extraction_pass c38-k2c-batch-06, tier AI_SUGGESTED) with zero AI
attribution in any validation state.

## 6. Next gates

- **K2-C-7** (B07, global_order 73–84) — separately commissioned by operator directive;
  inherits this batch's superseding 3-code boundary map {1.7C, 1.7D, 2.7B}, the landed
  holds' would-be edges (now aimed at authored nodes), and all six quarantines
- **K2-B** (Lane B chunk substrate) — still open; constructible in parallel per C31 §6
- **The B01..B06 verdict sessions** — six authored-to-gate packets now await the
  operator's per-row verdicts; the §18 apply follows the verdict encoding, all 77
  derived PART_OF rows and all six quarantines ruling together
- **K2-D** (Lane D substrate rows) — after Lane C batches have promoted concepts
