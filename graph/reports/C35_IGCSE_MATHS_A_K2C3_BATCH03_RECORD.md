# C35 — Subject-#2 K2-C-3 Gate Record — igcse-maths-a (4MA1 Higher), Lane C Batch B03

| | |
|---|---|
| **Task ID** | T-C35 (K2-C-3 of the C31 K2 scope — Lane C, batch B03 of 16) |
| **Version** | 1.0 — batch B03 authored to the verdict gate. NOTHING is promoted; the maths-a concepts store still does not exist and nothing in this landing creates it. The verdict step is reserved to the operator. |
| **Date** | 2026-10-02 |
| **Operator directive** | "K2-C-3" (2026-10-02, zai-web, inline) — gate K2-C-3 of the C31 §8 sequence (commission → author → review → verdict), with K2-B not yet run and the B01/B02 verdicts not yet recorded: the C31 scope record §6 provides for early Lane C batches before Lane B, and B01/B02 remain authored-to-gate packets whose SUGGESTED rows promote only through the operator's own verdicts, so B03 proceeds on the notes-join + ratified spec-text substrate alone at the same first-apply store state. The T-C34 record §6 anticipated exactly this commissioning ("K2-C-3 — the operator commissions B03 (global_order 25–36); its packet inherits this audit's 4-code boundary map and both held quarantines") |
| **Baseline** | syllabai-resources `origin/main` @ `10593fc594f57eb3030615a80a0f1e93dad0e75a` (T-C34 K2-C-2 B02 authored-to-gate landing; local == remote, tree clean at commissioning time) |
| **Predecessors** | `C34_IGCSE_MATHS_A_K2C2_BATCH02` (the replayed pattern, the 4-code boundary map and the B02 held quarantine this packet inherits); `C33_IGCSE_MATHS_A_K2C1_BATCH01` (the B01 quarantine, inherited through B02); `C31_IGCSE_MATHS_A_K2_SCOPE` (§5 batch plan, §8 gate row, §3 coverage-profile standing input); `C32_IGCSE_MATHS_A_K2A_LANE_A` (the notes-join substrate every Lane C batch anchors on); the chemistry C11 §16 machinery incl. the batch-10/11 misconception shapes |
| **Verification** | `scripts/c35_maths_a_batch03_check.py` → `graph/reports/C35_BATCH03_CHECK.json` (G1–G7 all PASS, exit 0) |

---

## 1. What was commissioned and authored

The operator's **K2-C-3** directive commissioned batch **B03** — the third Lane C
slice of the 16-batch plan (C31 §5): the 12 specification points
`4MA1-1.4C..4MA1-1.6D` (`global_order` 25–36 of the ratified K1 store). The batch
replays the B01/B02/chemistry §16 per-batch machinery at the unchanged
third-batch store state:

- **Commissioning record** — `scripts/c35_maths_a_batch03_authorization.yaml`
  (sha256_16 `4f0738f5020d45bc`): the directive verbatim, the scope unlocked
  (B03 only) and the 10 standing invariants (zero silent promotion; byte-verified
  quotes; the join-carried evidence allow-list with the B02-strength pair-back;
  the cross-batch boundary discipline; the misconception contract with the two
  documented classes named; no corpus writes; no chemistry work; no AI
  attribution in validation state).
- **Decision record** — `scripts/c35_maths_a_batch03_decisions.yaml`
  (sha256_16 `9a23da85ec47a9c3`): **12 concept nodes + 2 misconception nodes /
  13 authored edges (9 REQUIRES_PREREQUISITE + 2 WRONG_ANSWER_PATTERN + 2
  REMEDIATED_BY) / 8 held candidates / 12 command kinds / 3 operator-reserved
  identity decisions**, 83 evidence anchors across 14 node attachments, the two
  node-level MIS evidence blocks and 13 edges.
- **Pass-2 record** — `scripts/c35_maths_a_batch03_review_pass2.yaml`
  (sha256_16 `c158c8f869360c84`): the adversarial second pass — 14/14 nodes
  CONFIRM, 13/13 edges CONFIRM, 8/8 held AGREE, zero re-authoring cases
  (FP-B03-1..3 / FN-B03-1..3 recorded as questions and resolutions).
- **Review sheet** — `graph/reports/C35_BATCH03_REVIEW_SHEET.md` (sha256_16
  `358de0ac39b89d6e`, + `.json` twin `d916498c25693ce0`): the batch's operator
  gate surface — slice codes, coverage profile, the full diff-review bundle, the
  misconception-mint section and the held-quarantine state.

## 2. The coverage profile (the C31 §3 standing per-batch statement)

B03 is the second **mixed-tier slice** of the program: 7 Higher-applicability
rows (1.4C index laws; the complete 1.5 set-notation run 1.5A–1.5D; 1.6A
repeated percentage change; 1.6B compound interest) plus 5 Foundation rows
(1.4D prime factors, 1.4E HCF/LCM, 1.5E Venn representation, 1.6C percentage
conversions, 1.6D percentages as operators). It spans THREE ratified subtopics
(the 1.4 tail 1.4C–1.4E, 1.5 complete, the 1.6 head 1.6A–1.6D); the C31 honesty
rules are honored to the letter: subtopic titles for 1.4/1.5/1.6 are null in the
ratified topics store and are **never invented**; the 1.5C store wording carries
the canonical parse's spacing artifact verbatim (`use the notationn(A)for the
number of elements in the setA`) — quoted in the store form, never silently
repaired; zero damage-flagged rows sit in the slice.

| measure | value |
|---|---|
| Notes-joined SPs (NOTE evidence possible) | **6** — 1.4C, 1.4D, 1.4E, 1.5B, 1.5C, 1.5E (11 join rows over 9 distinct note files, via the T-C32 K2-A artifact; hcf-and-lcm carries two anchors — HCF and LCM; set-notation-and-venn-diagrams carries two — its notation half joined to 1.5B and its diagrams half to 1.5E) |
| Spec-text-only SPs (SPEC evidence only) | **6** — 1.5A, 1.5D, 1.6A, 1.6B, 1.6C, 1.6D |
| MS-evidenced SPs (node attachments) | 6 — 1.4C via the powers-roots topic MS, 1.4D/1.4E via the prime-factors topic MS (incl. the Q46 Venn-marking criterion row), 1.6A/1.6B via the compound-interest topic MS, 1.6D via the percentages topic MS (a PARTIAL MS-documentation shape, the chemistry batch-3/4/10 precedent; MS evidence also rides three edges — the practical cat-and-dog row, the multiplier rows, the 145%-equivalence bridge) |
| Evidence anchor mix | 83 anchors: 25 NOTE / 32 SPEC / 26 MARK_SCHEME |
| Misconceptions minted | **2 — the second and third maths-a mints** (4MA1-MIS-COMPLEMENT-INTERSECTION-CONFUSION riding 1.5B on the set-notation MS Q7(b) documentation; 4MA1-MIS-PERCENTAGE-QUOTIENT-INVERSION riding 1.6D on the percentages MS Q10/Q11 documentation). The mint-vs-exam-trivia question and both home-row choices are operator-reserved (B03-ID-02/03) |
| Join-carried but uncited pages | 2 — mathematical-operations.md (→1.5C; basic-symbol fluency does not state the n(A) demand) and probability-and-venn-diagrams.md (→1.5E; probability-from-diagrams content recorded on held B03-H-03): neither page states its SP's demand; the honest disposition is recorded (census + derivation notes), not a padded citation |

One authoring-time finding worth the operator's attention: the page's cardinality
**definition** row ("n(A) is the number of elements in set A") sits inside a span
the batch-8 normalization convention cannot verify — a literal `<` in the
such-that example opens a span the next blockquote `>` closes, swallowing the
row. The batch-8 convention is pinned machinery, so the cited anchor is the
worked-example verification row ("n(A) means the number of elements in A"), which
the convention checks byte-exactly — nothing is quoted that the machinery cannot
verify, and the situation is recorded on the node's derivation notes.

The **unjoined-corpus negative control** runs at third-batch strength: every
NOTE citation is one of the 9 join-carried notes and is **pair-backed** — node
attachments against their attached SP, edge evidence against one of the edge's
endpoint SPs (the B02 strength, carried forward). The corpus teaches the slice's
neighborhood on pages that carry no slice anchor — basic-percentages,
percentage-increases-and-decreases, reverse-percentages, converting-between-fdp
(itself joined to B02's 1.2G, not citable here), standard-form,
operations-with-standard-form, types-of-number, et al. — and **none of them is
cited anywhere** in the record.

## 3. Machine verification

`scripts/c35_maths_a_batch03_check.py` — zero-LLM, deterministic, read-only
toward graph/, corpora and parsed/** (writes only its own report):

| Gate | Asserts |
|---|---|
| **G1** `commissioning_record` | AUTHORIZED; verbatim directive `K2-C-3`; scope bounds + 10 invariants |
| **G2** `record_shape` | 12+2 nodes / 13 edges (9+2+2) / 8 held / 12 command kinds / 3 identity decisions; every slice SP covered; zero promotions (SUGGESTED) |
| **G3** `preverify_gates` | `c35_maths_a_batch03_preverify.py` 33/33 (shape, coverage, mixed-tier honesty, third-batch store state = exactly the 5 K1 stores with B01+B02 unapplied, evidence allow-list with edge pair-back, boundary + misconception contract, B01/B02 inheritance, null-title honesty) |
| **G4** `quote_probe_gates` | `c35_maths_a_batch03_quote_probe.py` — 83/83 anchors verbatim under the batch-8 G03/c11.4 convention; every NOTE row pair-backed (persistent cat-file channel: 12 git-batch reads + 1 disk) |
| **G5** `review_reproducible` | the committed sheet byte-equals a fresh deterministic build (json twin compared modulo `generated_utc`) |
| **G6** `freeze_integrity` | HEAD == `10593fc5…`; zero out-of-footprint paths (corpora, parsed canonical, chemistry + maths-a stores untouched) |
| **G7** `standing_checkers` | `graph_check.py` + `check_no_hardcode.py` exit 0 |

Result: **G1–G7 all PASS, exit 0** — `graph/reports/C35_BATCH03_CHECK.json`.

The term-audit probe (`c35_maths_a_batch03_term_audit_probe.py`, authoring aid)
audited the batch's 60 candidate terms against the whole ratified 188-row
wording + topics surface: 18 terms match, all landing on their own in-slice rows
except four non-slice codes — **4MA1-1.1H and 4MA1-1.2A** (B01's rows — the
common-factor/multiple and equivalent-fraction vocabulary the HCF/LCM node
shares; both nodes authored, unapplied), **4MA1-1.6G** (the compound-interest
Foundation twin — the 'compound interest' match confirming held B03-H-07) and
**4MA1-2.1D** ("use index laws in simple cases", the audit's new match). The
audit **supersedes the B02 audit as the later batches' boundary-ruling starting
point**: of the B02-inherited four codes, 1.4D/1.4E are now IN-SLICE (their
nodes mint here) and 1.7A/1.8B drop out (no B03 vocabulary match), so the B04..
map is `{4MA1-1.1H, 4MA1-1.2A, 4MA1-1.6G, 4MA1-2.1D}`.

## 4. What the verdict gate decides

The review sheet's §2/§2a/§3/§4 carry one operator checkbox per row: 12 concept
nodes, 2 misconception nodes, 13 edges, 8 held candidates, plus the three
identity decisions:

- **B03-ID-01** — the Venn mirror rows 1.5B (Higher, with the element-count arm)
  and 1.5E (Foundation) author as TWO nodes; the substrate's own operator-worked
  split of the set-notation page (notation half → 1.5B, diagrams half → 1.5E)
  supports the split; any single Venn-representation family merge is the
  operator's call.
- **B03-ID-02** — the percentage-quotient-inversion mint rides 1.6D (the
  multiplicative-operator row whose direction-sense the error violates),
  although the percentages MS's own questions sit closest to 1.6E (B04's first
  row); the operator rules on the home row and the B04 packet inherits the
  question through its term audit.
- **B03-ID-03** — the two mints stand or fall as operator-ruled: genuine
  wrong-answer patterns worth graph nodes, or assessment-local exam trivia
  (the chemistry B10-ID-05 / B02-ID-03 precedent), AND M1's home row (1.5B vs
  the Foundation twin 1.5E).

At the verdict session: verdicts encode through an intake-conformance check
(the chemistry pattern), then — and only then — the §18 apply step
materializes the first maths-a K2 stores (concepts / concept_edges /
spec_command_kinds) with exactly the promoted rows from ALL authored batches
plus the derived PART_OF rows (14 from B03's attachments; 13 from B01's; 14
from B02's). Zero silent promotion stands; the B01 quarantine (B01-H-01..05),
the B02 quarantine (B02-H-01..08) and the B03 quarantine (B03-H-01..08 — five
of eight rows are cross-batch boundary holds: two to B01/B02 nodes, three to
future-batch families, plus one order-inversion/vocabulary hold) rule together
there and are preserved forward.

## 5. Scope guards honored this landing

Zero bytes in `graph/igcse-chemistry/**`, `parsed/**` canonical JSON, or the
SME corpora; the maths-a graph dir still carries exactly the 5 K1 stores (the
registry has not grown — G3/G6); the K1 stores unedited; no core or hub
serving change; no K2-B/K2-D work; the chemistry C11 program untouched. The
footprint is exactly: 8 scripts (`c35_maths_a_batch03_{authorization,decisions,
review_pass2}.yaml` + `{preverify,quote_probe,term_audit_probe,review_build,
check}.py`), 5 reports (`C35_BATCH03_REVIEW_SHEET.md`, `C35_BATCH03_REVIEW.json`,
`C35_BATCH03_CHECK.json`, this record's md+json twin).

## 6. Next gates

| gate | what it needs |
|---|---|
| **operator verdicts for B01 + B02 + B03** | the three review sheets (C33 §2/§3/§4 + identity decisions; C34 §2/§2a/§3/§4 + the three identity decisions; C35 §2/§2a/§3/§4 + the three identity decisions) — the verdict template lands with the verdict session; the §18 apply then materializes the first maths-a K2 stores |
| **K2-C-4** | the operator commissions B04 (global_order 37–48 — the 1.6 tail 1.6E/1.6F/1.6G and beyond); its packet inherits this audit's 4-code boundary map and all three held quarantines, and rules on the B03-H-06/B03-H-07 pre-recorded boundary questions |
| **K2-B** | still open (chunk substrate); C31 §6 permits it in parallel with early Lane C batches |
