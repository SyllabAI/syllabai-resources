# C34 — Subject-#2 K2-C-2 Gate Record — igcse-maths-a (4MA1 Higher), Lane C Batch B02

| | |
|---|---|
| **Task ID** | T-C34 (K2-C-2 of the C31 K2 scope — Lane C, batch B02 of 16) |
| **Version** | 1.0 — batch B02 authored to the verdict gate. NOTHING is promoted; the maths-a concepts store still does not exist and nothing in this landing creates it. The verdict step is reserved to the operator. |
| **Date** | 2026-10-01 |
| **Operator directive** | "K2-C-2" (2026-10-01, zai-web, inline) — gate K2-C-2 of the C31 §8 sequence (commission → author → review → verdict), with K2-B not yet run and the B01 verdicts not yet recorded: the C31 scope record §6 provides for early Lane C batches before Lane B, and B01 remains an authored-to-gate packet whose SUGGESTED rows promote only through the operator's own verdicts, so B02 proceeds on the notes-join + ratified spec-text substrate alone at the same first-apply store state |
| **Baseline** | syllabai-resources `origin/main` @ `f0f4c2d5929a2e06c92e9f740984e8d68325027a` (T-C33 K2-C-1 B01 authored-to-gate landing; local == remote, tree clean at commissioning time) |
| **Predecessors** | `C33_IGCSE_MATHS_A_K2C1_BATCH01` (the replayed pattern, the 6-code boundary map and the B01 held quarantine this packet inherits); `C31_IGCSE_MATHS_A_K2_SCOPE` (§5 batch plan, §8 gate row, §3 coverage-profile standing input); `C32_IGCSE_MATHS_A_K2A_LANE_A` (the notes-join substrate every Lane C batch anchors on); the chemistry C11 §16 machinery incl. the batch-10/11 misconception shapes (the replayed pattern for the first maths-a mints) |
| **Verification** | `scripts/c34_maths_a_batch02_check.py` → `graph/reports/C34_BATCH02_CHECK.json` (G1–G7 all PASS, exit 0) |

---

## 1. What was commissioned and authored

The operator's **K2-C-2** directive commissioned batch **B02** — the second Lane C
slice of the 16-batch plan (C31 §5): the 12 specification points
`4MA1-1.2E..4MA1-1.4B` (`global_order` 13–24 of the ratified K1 store). The batch
replays the B01/chemistry §16 per-batch machinery at the unchanged second-batch
store state:

- **Commissioning record** — `scripts/c34_maths_a_batch02_authorization.yaml`
  (sha256_16 `8bed477924bf458c`): the directive verbatim, the scope unlocked
  (B02 only) and the 10 standing invariants (zero silent promotion; byte-verified
  quotes; the join-carried evidence allow-list now with explicit pair-back; the
  cross-batch boundary discipline; the misconception contract with the two
  documented classes named; no corpus writes; no chemistry work; no AI attribution
  in validation state).
- **Decision record** — `scripts/c34_maths_a_batch02_decisions.yaml`
  (sha256_16 `5c548f576ba141f0`): **12 concept nodes + 2 misconception nodes /
  10 authored edges (6 REQUIRES_PREREQUISITE + 2 WRONG_ANSWER_PATTERN + 2
  REMEDIATED_BY) / 8 held candidates / 12 command kinds / 3 operator-reserved
  identity decisions**, 61 evidence anchors across 14 node attachments, the two
  node-level MIS evidence blocks and 10 edges.
- **Pass-2 record** — `scripts/c34_maths_a_batch02_review_pass2.yaml`
  (sha256_16 `e361a7e6ca523cfe`): the adversarial second pass — 14/14 nodes
  CONFIRM, 10/10 edges CONFIRM, 8/8 held AGREE, zero re-authoring cases
  (FP-B02-1..3 / FN-B02-1..3 recorded as questions and resolutions).
- **Review sheet** — `graph/reports/C34_BATCH02_REVIEW_SHEET.md` (sha256_16
  `de5f1a9de0a567aa`, + `.json` twin `83a4ceea08a97780`): the batch's operator
  gate surface — slice codes, coverage profile, the full diff-review bundle, the
  misconception-mint section and the held-quarantine state.

## 2. The coverage profile (the C31 §3 standing per-batch statement)

B02 is a **mixed-tier slice** — the first of the program: 9
Foundation-applicability rows plus the first three Higher rows of the ratified
188 (4MA1-1.3A recurring decimals, 4MA1-1.4A surds meaning, 4MA1-1.4B surds
manipulation; papers 4MA1/1H and 4MA1/2H). It spans THREE ratified subtopics
(the 1.2 tail 1.2E–1.2I, 1.3 complete, the 1.4 head 1.4A–1.4B); the C31 honesty
rules are honored to the letter: subtopic titles for 1.2/1.3/1.4 are null in the
ratified topics store and are **never invented**; zero damage-flagged rows sit in
the slice.

| measure | value |
|---|---|
| Notes-joined SPs (NOTE evidence possible) | **7** — 1.2F, 1.2G, 1.2I, 1.3A, 1.3C, 1.4A, 1.4B (13 join rows over 11 distinct note files, via the T-C32 K2-A artifact) |
| Spec-text-only SPs (SPEC evidence only) | **5** — 1.2E, 1.2H, 1.3B, 1.3D, 1.3E |
| MS-evidenced SPs | 4 — 1.2F via the fractions topic mark-schemes.md (the same surface B01 pinned), 1.3A and 1.3C via the FDP topic mark-schemes.md, 1.4B via the surds topic mark-schemes.md (a PARTIAL MS-documentation shape, the chemistry batch-3/4/10 precedent) |
| Evidence anchor mix | 61 anchors: 26 NOTE / 21 SPEC / 14 MARK_SCHEME |
| Misconceptions minted | **2 — the first maths-a mints** (4MA1-MIS-SURD-FACTOR-SWAP, 4MA1-MIS-CONJUGATE-EXPANSION-SIGN): the surds topic MS Q12 20(a)/(b) rows are the first maths-a mark-scheme documentation of wrong-answer classes, satisfying the chemistry contract's mint condition; B01 minted zero on the same contract (the abstention record stands as the counterfactual). The mint-vs-exam-trivia question is operator-reserved (B02-ID-03) |
| Join-carried but uncited pages | 2 — negative-numbers.md (→1.4A) and algebraic-notation.md (→1.3A): neither page states its SP's demand; the honest disposition is recorded (census + derivation notes + the held B02-H-04 row), not a padded citation |

The **unjoined-corpus negative control** runs at second-batch strength: every
NOTE citation is one of the 11 join-carried notes and is **pair-backed** — node
attachments against their attached SP, edge evidence against one of the edge's
endpoint SPs (a strengthening over B01, whose pair-back ran on node attachments
only). The corpus teaches the slice's neighborhood on pages that carry no slice
anchor — mixed-numbers-and-improper-fractions (itself joined to B01's 1.2B, not
citable here), hcf-and-lcm, prime-factor-decomposition, laws-of-indices,
standard-form, the percentages pages, et al. — and **none of them is cited
anywhere** in the record.

## 3. Machine verification

`scripts/c34_maths_a_batch02_check.py` — zero-LLM, deterministic, read-only
toward graph/, corpora and parsed/** (writes only its own report):

| Gate | Asserts |
|---|---|
| **G1** `commissioning_record` | AUTHORIZED; verbatim directive `K2-C-2`; scope bounds + 10 invariants |
| **G2** `record_shape` | 12+2 nodes / 10 edges (6+2+2) / 8 held / 12 command kinds / 3 identity decisions; every slice SP covered; zero promotions (SUGGESTED) |
| **G3** `preverify_gates` | `c34_maths_a_batch02_preverify.py` 32/32 (shape, coverage, mixed-tier honesty, second-batch store state = exactly the 5 K1 stores with B01 unapplied, evidence allow-list with edge pair-back, boundary + misconception contract, B01 inheritance, null-title honesty) |
| **G4** `quote_probe_gates` | `c34_maths_a_batch02_quote_probe.py` — 61/61 anchors verbatim under the batch-8 G03/c11.4 convention; every NOTE row pair-backed (persistent cat-file channel: 12 git-batch reads + 1 disk) |
| **G5** `review_reproducible` | the committed sheet byte-equals a fresh deterministic build |
| **G6** `freeze_integrity` | HEAD == `f0f4c2d5…`; zero out-of-footprint paths (corpora, parsed canonical, chemistry + maths-a stores untouched) |
| **G7** `standing_checkers` | `graph_check.py` + `check_no_hardcode.py` exit 0 |

Result: **G1–G7 all PASS, exit 0** — `graph/reports/C34_BATCH02_CHECK.json`.

The term-audit probe (`c34_maths_a_batch02_term_audit_probe.py`, authoring aid)
audited the batch's 63 candidate terms against the whole ratified 188-row
wording + topics surface: 8 terms match, all landing on their own in-slice rows
except one new future code — **4MA1-1.8B** ("round to a given number of
significant figures or decimal places", matched by the 'decimal places'
vocabulary). The audit **supersedes the B01 audit as the later batches'
boundary-ruling starting point**: of the B01-inherited six codes, 1.2F/1.2I/1.3B
are now IN-SLICE (their nodes mint here) and 1.4D/1.4E/1.7A remain future, so
the B03.. map is `{4MA1-1.4D, 4MA1-1.4E, 4MA1-1.7A, 4MA1-1.8B}`.

## 4. What the verdict gate decides

The review sheet's §2/§2a/§3/§4 carry one operator checkbox per row: 12 concept
nodes, 2 misconception nodes, 10 edges, 8 held candidates, plus the three
identity decisions:

- **B02-ID-01** — the 1.3B row authors as its OWN node
  (`4MA1-CON-DECIMAL-PLACE-VALUE`) although its wording is byte-identical to
  1.1B's and B01 authored a place-value node CORE at 1.1B; the decimal context
  is the store's own 1.3 subtopic placement; the eventual co-identity or merge
  (once B01 promotes) is the operator's call.
- **B02-ID-02** — the mirror conversions 1.2G/1.3D author as TWO nodes, one per
  row; any single FDP-conversion family merge is operator-only (the
  converting-between-fdp evidence is pair-locked to 1.2G).
- **B02-ID-03** — the first maths-a misconception mints stand or fall as
  operator-ruled: genuine wrong-answer patterns worth graph nodes, or
  assessment-local exam trivia (the chemistry B10-ID-05 precedent).

At the verdict session: verdicts encode through an intake-conformance check
(the chemistry pattern), then — and only then — the §18 apply step
materializes the first maths-a K2 stores (concepts / concept_edges /
spec_command_kinds) with exactly the promoted rows from BOTH authored batches
plus the derived PART_OF rows (14 from B02's attachments; 13 from B01's). Zero
silent promotion stands; the B01 held quarantine (B01-H-01..05) and the B02
quarantine (B02-H-01..08 — six of eight rows are cross-batch boundary holds:
three to B01 nodes, three to future-batch families) rule together there and are
preserved forward.

## 5. Scope guards honored this landing

Zero bytes in `graph/igcse-chemistry/**`, `parsed/**` canonical JSON, or the
SME corpora; the maths-a graph dir still carries exactly the 5 K1 stores (the
registry has not grown — G3/G6); the K1 stores unedited; no core or hub
serving change; no K2-B/K2-D work; the chemistry C11 program untouched. The
footprint is exactly: 8 scripts (`c34_maths_a_batch02_{authorization,decisions,
review_pass2}.yaml` + `{preverify,quote_probe,term_audit_probe,review_build,
check}.py`), 5 reports (`C34_BATCH02_REVIEW_SHEET.md`, `C34_BATCH02_REVIEW.json`,
`C34_BATCH02_CHECK.json`, this record's md+json twin).

## 6. Next gates

| gate | what it needs |
|---|---|
| **operator verdicts for B01 + B02** | both review sheets (C33 §2/§3/§4 + identity decisions; C34 §2/§2a/§3/§4 + the three identity decisions) — the verdict template lands with the verdict session; the §18 apply then materializes the first maths-a K2 stores |
| **K2-C-3** | the operator commissions B03 (global_order 25–36); its packet inherits this audit's 4-code boundary map and both held quarantines |
| **K2-B** | still open (chunk substrate); C31 §6 permits it in parallel with early Lane C batches |
