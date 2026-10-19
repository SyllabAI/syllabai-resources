# C33 — Subject-#2 K2-C-1 Gate Record — igcse-maths-a (4MA1 Higher), Lane C Batch B01

| | |
|---|---|
| **Task ID** | T-C33 (K2-C-1 of the C31 K2 scope — Lane C, batch B01 of 16) |
| **Version** | 1.0 — batch B01 authored to the verdict gate. NOTHING is promoted; the maths-a concepts store does not exist yet and nothing in this landing creates it. The verdict step is reserved to the operator. |
| **Date** | 2026-10-01 |
| **Operator directive** | "K2-C-1" (2026-10-01, zai-web, inline) — gate K2-C-1 of the C31 §8 sequence (commission → author → review → verdict), with K2-B not yet run: the C31 scope record §6 explicitly provides for early Lane C batches before Lane B, so B01 proceeds on the notes-join + ratified spec-text substrate alone |
| **Baseline** | syllabai-resources `origin/main` @ `feb0e1c9caceb527661d5683b997edb612349164` (T-C32 K2-A Lane A landing; local == remote, tree clean at commissioning time) |
| **Predecessors** | `C31_IGCSE_MATHS_A_K2_SCOPE` (§5 batch plan, §8 gate row, §3 coverage-profile standing input); `C32_IGCSE_MATHS_A_K2A_LANE_A` (the notes-join substrate every Lane C batch anchors on); the chemistry C11 §16 machinery (11 batches — the replayed pattern) |
| **Verification** | `scripts/c33_maths_a_batch01_check.py` → `graph/reports/C33_BATCH01_CHECK.json` (G1–G7 all PASS, exit 0) |

---

## 1. What was commissioned and authored

The operator's **K2-C-1** directive commissioned batch **B01** — the first Lane C
slice of the 16-batch plan (C31 §5): the 12 specification points
`4MA1-1.1A..4MA1-1.2D` (`global_order` 1–12 of the ratified K1 store). The batch
replays the chemistry §16 per-batch machinery at first-batch state:

- **Commissioning record** — `scripts/c33_maths_a_batch01_authorization.yaml`
  (sha256_16 `da599532b55f51c8`): the directive verbatim, the scope unlocked
  (B01 only) and the 9 standing invariants (zero silent promotion; byte-verified
  quotes; the join-carried evidence allow-list; no corpus writes; no chemistry
  work; no AI attribution in validation state).
- **Decision record** — `scripts/c33_maths_a_batch01_decisions.yaml`
  (sha256_16 `d82a983945c91cbb`): **11 concept nodes / 12 authored
  REQUIRES_PREREQUISITE edges / 5 held candidates / 12 command kinds / 2
  operator-reserved identity decisions**, 47 evidence anchors across 13 node
  attachments and 12 edges.
- **Pass-2 record** — `scripts/c33_maths_a_batch01_review_pass2.yaml`
  (sha256_16 `e876c58cd9042552`): the adversarial second pass — 11/11 nodes
  CONFIRM, 12/12 edges CONFIRM, 5/5 held AGREE, zero re-authoring cases
  (FP-B01-1..3 / FN-B01-1..2 recorded as questions and resolutions).
- **Review sheet** — `graph/reports/C33_BATCH01_REVIEW_SHEET.md` (sha256_16
  `dca6919d3f3437d8`, + `.json` twin `45f703c72234b1be`): the batch's operator
  gate surface — slice codes, coverage profile, the full diff-review bundle and
  the held-quarantine state.

## 2. The coverage profile (the C31 §3 standing per-batch statement)

The slice is an **assumed-knowledge slice**: all 12 rows are
Foundation-applicability (papers 4MA1/1F and 4MA1/2F; "Foundation statements are
assumed knowledge for Higher Tier papers" per the store's own applicability
rule). The C31 honesty rules are honored to the letter: subtopic titles for
1.1/1.2 are null in the ratified store (the official specification numbers its
content subsections without titles) and are **never invented**; zero
damage-flagged rows sit in the slice.

| measure | value |
|---|---|
| Notes-joined SPs (NOTE evidence possible) | **4** — 1.1F, 1.1G, 1.2A, 1.2B (one joined note each, via the T-C32 K2-A artifact) |
| Spec-text-only SPs (SPEC evidence only) | **8** — 1.1A, 1.1B, 1.1C, 1.1D, 1.1E, 1.1H, 1.2C, 1.2D |
| MS-evidenced SPs | 1 — 1.2C via the fractions topic `mark-schemes.md` (a PARTIAL MS-documentation shape, the chemistry batch-3/4/10 precedent) |
| Evidence anchor mix | 47 anchors: 18 NOTE / 25 SPEC / 4 MARK_SCHEME |
| Misconceptions minted | **0** — the three B01-topic mark-scheme files document correct procedures only; no Reject-class row exists (the chemistry MS-Reject contract honored by abstention, held as B01-H-04) |

The **unjoined-corpus negative control** (this batch's structural negative
control, replacing chemistry's single carved-out SP): the corpus teaches the
slice's surfaces on nearby pages (negative-numbers, mathematical-operations,
hcf-and-lcm, prime-factor-decomposition, basic-fractions, adding-and-
subtracting), but none of those pages carries a slice-SP anchor in the
operator-worked join — so **none of them is cited anywhere** in the record, and
every NOTE row is machine-verified to cite its note **for exactly the SP that
note is joined to**.

## 3. Machine verification

`scripts/c33_maths_a_batch01_check.py` — zero-LLM, deterministic, read-only
toward graph/, corpora and parsed/** (writes only its own report):

| Gate | Asserts |
|---|---|
| **G1** `commissioning_record` | AUTHORIZED; verbatim directive `K2-C-1`; scope bounds + 9 invariants |
| **G2** `record_shape` | 11/12/5/12/2 counts; every slice SP covered; all CONCEPT; all SUGGESTED; edge vocabulary |
| **G3** `preverify_gates` | `c33_maths_a_batch01_preverify.py` 21/21 (shape, coverage, first-batch store state = exactly the 5 K1 stores, evidence allow-list, boundary + promotion discipline) |
| **G4** `quote_probe_gates` | `c33_maths_a_batch01_quote_probe.py` — 47/47 anchors verbatim under the batch-8 G03/c11.4 convention; every NOTE row backed by its join pair (persistent cat-file channel: 5 git-batch reads + 1 disk) |
| **G5** `review_reproducible` | the committed sheet byte-equals a fresh deterministic build |
| **G6** `freeze_integrity` | HEAD == `feb0e1c9…`; zero out-of-footprint paths (corpora, parsed canonical, chemistry + maths-a stores untouched) |
| **G7** `standing_checkers` | `graph_check.py` + `check_no_hardcode.py` exit 0 |

Result: **G1–G7 all PASS, exit 0** — `graph/reports/C33_BATCH01_CHECK.json`.

The term-audit probe (`c33_maths_a_batch01_term_audit_probe.py`, authoring aid)
audited the batch's 60 candidate terms against the whole ratified 188-row
wording + topics surface: 15 terms match, none wrongly minted against a
non-slice row, and the audit records the **future-batch boundary map** — 6
non-slice SP codes sharing candidate vocabulary (`4MA1-1.2F`, `4MA1-1.2I`,
`4MA1-1.3B`, `4MA1-1.4D`, `4MA1-1.4E`, `4MA1-1.7A`) that B02.. inherit as their
boundary-ruling starting point (notably HCF/LCM at 1.4E behind the 1.1H
vocabulary).

## 4. What the verdict gate decides

The review sheet's §2/§3/§4 carry one operator checkbox per row: 11 nodes,
12 edges, 5 held candidates, plus the two identity decisions:

- **B01-ID-01** — 1.1A+1.1C+1.1D authored as ONE node
  (`4MA1-CON-INTEGERS-AND-DIRECTED-NUMBERS`); the integer-definition note
  quotes reach that family only through the TYPES-OF-NUMBER edge, because the
  notes page is joined to 1.1G only.
- **B01-ID-02** — the 1.2D row's two bundled demands split into TWO nodes
  (`…-ORDERING-FRACTIONS`, `…-FRACTION-OF-A-QUANTITY`), both CORE at 1.2D; the
  sibling edge between them is held (B01-H-02).

At the verdict session: verdicts encode through an intake-conformance check
(the chemistry pattern), then — and only then — the §18 apply step
materializes the first maths-a K2 stores (concepts / concept_edges /
spec_command_kinds) with exactly the promoted rows plus the 13 derived
PART_OF rows (one per node attachment). Zero silent promotion stands; the
held quarantine starts here and is preserved forward.

## 5. Scope guards honored this landing

Zero bytes in `graph/igcse-chemistry/**`, `parsed/**` canonical JSON, or the
SME corpora; the maths-a graph dir still carries exactly the 5 K1 stores (the
registry has not grown — G3/G6); the K1 stores unedited; no core or hub
serving change; no K2-B/K2-D work; the chemistry C11 program untouched. The
footprint is exactly: 6 scripts (`c33_maths_a_batch01_{authorization,decisions,
review_pass2}.yaml` + `{preverify,quote_probe,term_audit_probe,review_build,
check}.py`), 4 reports (`C33_BATCH01_REVIEW_SHEET.md`, `C33_BATCH01_REVIEW.json`,
`C33_BATCH01_CHECK.json`, this record's md+json twin).

## 6. Next gates

| gate | what it needs |
|---|---|
| **operator verdicts for B01** | the review sheet (§2/§3/§4 + identity decisions) — verdict template lands with the verdict session |
| **K2-C-2** | the operator commissions B02 (global_order 13–24); its packet inherits the term audit's 6-code boundary map and the B01 held quarantine |
| **K2-B** | still open (chunk substrate); C31 §6 permits it in parallel with early Lane C batches |
