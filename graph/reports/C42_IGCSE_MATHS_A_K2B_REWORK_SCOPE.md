# C42 — K2-B Rework Scope Record — igcse-maths-a (4MA1 Higher)

| | |
|---|---|
| **Task ID** | T-C42 (rework scoping for the K2 Lane B chunk substrate, the C40 fill's named rework path) |
| **Version** | 1.0 — the rework is SCOPED, NOT executed. Every verdict, repair byte, join re-run, store rebuild and apply this scope describes remains behind the operator gates it names (§7). |
| **Date** | 2026-10-02 |
| **Operator directive** | "scope that" (2026-10-02, zai-web, inline) — scoping the rework path the C40 fill record named ("a T-SPEC resolution-repair round over the implicated joins, then the T-C32 join re-run and the substrate re-build — is the operator's decision") |
| **Baseline** | syllabai-resources `origin/main` @ `720b86b` (c40 blank-form generator fix; local == remote, tree clean at scoping time) |
| **Predecessors** | `C39_IGCSE_MATHS_A_K2C_APPLY_RECORD` (the Lane C §18 governed apply: 82 nodes / 84 PART_OF / 73 authored semantic edges; DC-02 reconciled the PART_OF census at 84); `C40_IGCSE_MATHS_A_K2B_LANE_B_RECORD` + `C40_MATHS_A_K2B_REVIEW_FILL_RECORD` (substrate constructed + filled; gate FAILS); `C41_MATHS_A_S18_PROMOTION_RECORD` (the §18 HUMAN_VALIDATED round over the 73 authored semantic edges — complete, standing); `C31_IGCSE_MATHS_A_K2_SCOPE` §6 (Lane B definition) and §7 (standing guards) |
| **Verification** | `scripts/c42_k2b_rework_scope_check.py@31ba25e74a728cef` → `graph/reports/C42_K2B_REWORK_SCOPE_CHECK.json@1fc72333e8296a9a` (G1–G7 all PASS, exit 0; deterministic re-run byte-stable) |

---

## 1. What this scope is

The C40 substrate review fill (operator-delegate, 2026-10-02) measured the chunk
substrate's semantics for the first time and **failed its own gate**: Part A
per-class precision 75.0% overall, with the exact stratum at 54.1% and the
partial stratum at 74.4% against the ≥90%-per-class requirement. The fill did
what the C13 convention demands and nothing more: zero silent promotion, zero
silent repair — the store stays `SUGGESTED`, every REJECT carries its evidence,
and the rework path was left as the operator's decision. This record is that
decision's scoping: it defines the repair lane (R0–R5, §4), the two operator
gates that arm it, the invariants that must survive it (§5), and the
verification battery that machine-checks the scoping itself (§8).

Explicitly out of this scope's motion: the Lane C concept surface
(`concepts.yaml` / `concept_edges.yaml` / `spec_command_kinds.yaml`, including
the 73 semantic edges promoted HUMAN_VALIDATED by C41) is a **protected
standing surface** — the chunk-substrate defect class cannot touch it, and no
stage here writes it. Lane D and the relationships store remain deferred by
the C31 playbook. The K2 exit shape (9 stores) already stands in the registry.

## 2. The defect inventory (machine-verified this assessment)

From `C40_MATHS_A_K2B_REVIEW_FILL_RECORD.md` + the verdict record
`scripts/c40_maths_a_substrate_review_verdicts.yaml` (468 Part A verdict rows;
re-census at G2):

| Measure | Value |
|---|---|
| Part A verdict rows | 468 (351 CONFIRM / 117 REJECT / 0 HOLD) |
| REJECT root classes | **101 note-level + 16 section-level** |
| Distinct note-level defect joins | **45** (note, wrong-code) pairs — 45 distinct notes, 45 distinct anchors, 36 distinct wrong codes |
| Distinct section-level defect notes | **10** (16 rows; the note's join is right, the sampled section teaches a different SP) |
| Part B worklist decisions | 79/79 DEFER (2 unresolved-span chunks pending the C32 residual adjudication + 77 uncovered-SP corpus gaps, the chemistry 4.15 precedent) |
| Store rows riding on the 45 defective joins | **189** anchored rows re-attribute wholesale once the joins are repaired |
| Store rows on the 10 section-level notes | **59** (a subset re-attributes or demotes per verdict) |
| Anchored surface / coverage | 860 anchored rows over 111/188 codes — measured **under the defective mapping**; both numbers recompute at R3 |

The two defect classes have different homes. **Note-level** (101 rejects → 45
joins): the chunk rows inherit a wrong `spec_code` from the note's join; every
section chunk of the note re-attributes together. **Section-level** (16
rejects → 10 notes): the join stands, the sampled section teaches adjacent
content (examples from the fill: the number-line section under the
Cartesian-graph SP 2.8D; sphere/cone sections under the cylinder SP 4.10D; a
plotting-from-a-table section under the gradient SP 3.3F) — the per-note join
granularity cannot express the correction, so these rows need an explicit
disposition mechanism (§4 R1 surface 3).

## 3. The scoping discovery: the defects are id-level, upstream, and wider than the notes lane

Tracing all 45 defective joins to their sources (G3/G4 re-census) settles
where the wrongness lives:

1. **The notes corpus is not the defect.** Each defective note anchors exactly
   one `spcpt_*` id, and the EQ resolution row for that id carries an
   `sme_name` that matches the note title (e.g. `spcpt_XC6PSG6CcXnNDb3Q` is
   named "Exchange Rates" and anchors the note "Exchange Rates"). The
   name→id anchoring is sound.
2. **The resolution verdict is the defect.** The same rows resolve to codes
   that teach unrelated content: "Exchange Rates" → 3.4C (*determine
   gradients, rates of change, stationary points…*), "Negative Numbers" → 1.4A
   (*understand the meaning of surds*), "Vector Diagrams" → 6.1C (*use
   cumulative frequency diagrams*), "Mean, Median & Mode" → 6.2B (*measure of
   spread*). Tier/method fields show these are the T-SPEC-7-era
   `P1_name_fragment_join` / `S1_name_match` operator-verdict rounds (score
   1.0 name-fragment verdicts among them); the defect distribution spans the
   tiers (27 P1 / 12 S1 / 3 P2 / 2 S2 / 1 R1 across the 45).
3. **Why no earlier gate caught it.** The C31 §3 wording crosscheck (202/202
   EXACT) compared the resolution row's `official_wording` against the K1
   store's wording **for the code the row already names** — a
   registry-consistency check that is tautological with respect to code
   choice. The C40 fill is the first semantics gate in the chain, and it
   worked as designed: the defect is now inventoried with evidence, not
   silently repaired.
4. **Blast radius beyond the chunk substrate.** The 45 defective ids are
   id-level facts about the resolution file, so every consumer of those ids
   inherits them:
   - **EQ part tagging**: 40 of the 45 ids carry `referenced_by_parts > 0`,
     summing to **996 part references** in the EQ corpus — the question-side
     spec tagging rides on the same wrong codes wherever that tagging is
     consumed downstream.
   - **The `spec-links/` derived surface**: `build_learner_spec_links.py`
     consumes the maths-a resolution file directly.
   - The C32 notes-join and the C40 substrate (the surfaces whose failure
     triggered this scope).
   The EQ-side and spec-links-side repairs are **census items here, not work
   items** (§4 R0): whether and when to repair them is a separate operator
   decision armed by the R0 census, not silently absorbed into the notes-lane
   rework.

One more census fact the round must carry honestly: the resolution file's own
`counts` (222 ids / 218 resolved / 4 unresolved) is consistent with its
`resolved` array (4 rows carry a null `resolved_code` — the unresolved
allowlist), and its validation string still reads AI_VALIDATED
(operator-delegated; T-SPEC-10; PMT excluded as source) with the
"HUMAN_VALIDATED via operator review" tail. The repair round amends that
string with a dated clause (§4 R1) rather than letting the old claim silently
cover repaired rows.

## 4. The rework lane (R0–R5)

| Stage | Kind | Produces | Gate |
|---|---|---|---|
| **R0 — EQ blast-radius census** | agent, read-only | part-level consumer table for the 45 ids (which surfaces consume those part tags: s104-style packages, RAG, serving), spec-links row count, no repairs | evidence into the R1 packet |
| **R1 — T-SPEC resolution repair round** | **operator verdict round** | three verdict surfaces: (a) **45 id-level repairs** — corrected code ∈ the canonical 188 or UNRESOLVED, never forced; (b) **the C32 residual adjudication** — `spcpt_QWXhzVp2S3VYZdZc` ("Discrete & Continuous Data"), pending since C31 §3; (c) **16 section-level dispositions** — REATTRIBUTE / DEMOTE-to-worklist / RETAIN per row | **Operator gate 1** |
| **R2 — T-C32 join re-run** | agent, deterministic | notes-join refreshed 1:1 from the amended resolution (verbatim-preservation rule unchanged; foreign-code hard-fail; wording crosscheck re-run) | C32 battery re-green |
| **R3 — substrate re-build** | agent, deterministic | `spec_chunk_mappings.yaml` regenerated by the c40 tool: chunk identity invariant (note_path / ordinal / heading / sha256_16 unchanged), only code attribution + anchor fields move; 189 rows re-attribute with the 45 joins; section-level verdicts applied through a fail-closed override map consumed by the tool (no hand edits); coverage + worklist recomputed | C40 landing battery re-green (P1–P10 analog) |
| **R4 — re-gate** | operator-delegate fill + operator evidence | fresh review sheet from the rebuilt store (re-stratified; Part A + Part B), the C12/C13 fill convention, **≥90% per-class** on the new surface; Part B re-decided (the 77-uncovered set will have moved) | **Operator gate 2** (evidence) |
| **R5 — §18 substrate apply** | **operator-gated apply** | SUGGESTED → HUMAN_VALIDATED via the promotions-file convention (the C41 mechanics: exact row identities only, structural diff asserts the non-validation delta is zero, two-way audit) | **Operator gate 3** |

R1 mechanics, pinned so nothing is improvised later:

- **Proposals are deterministic and bind nothing.** Candidate corrected codes
  per id come from the c32-residual scorer convention (difflib ratio + token
  overlap + section-prior, PROPOSAL-ONLY), plus the fill's own per-row
  evidence as the starting context. PMT stays excluded as source. The verdict
  itself is the operator's, in the T-SPEC-7/8/9/10 round shape.
- **The resolution file is amended in place, with per-row provenance.** The
  T-SPEC series precedent (t_spec_7_index_repair / t_spec_8_apply wrote the
  parsed artifacts in-house, "no upstream") makes the file a maintained
  verdict artifact, not a frozen corpus: R1 repairs land as dated per-row
  amendments (`repaired_*` fields + repair-record reference, original verdict
  fields preserved for audit), and the validation string gains a dated repair
  clause. The C32/C40 records' "corpus byte-frozen" language stands unedited —
  it described those lanes' build-time guarantees; this is a separate,
  operator-gated verdict round in the T-SPEC series, the C31 §4.4 exception
  path (dated amendment, not silent override) exactly.
- **The section-level surface is an override map, not a re-join.**
  `scripts/` carries an operator-owned verdict file keyed by
  (note_path, chunk_ordinal); the c40 tool consumes it fail-closed at R3 —
  an override naming a code the store does not contain fails the build.
- **Repair record**: `graph/reports/C42_MATHS_A_RESOLUTION_REPAIR_RECORD.*`
  + the apply/check scripts under `scripts/`, the T-SPEC apply convention.

## 5. Invariants the rework must preserve

- **Chunk identity** — the `c40-chunk-convention-1` forward contract (chunk =
  (note_path, ordinal, heading, sha256_16 of text)) survives R3 untouched;
  repairs move code attribution, never chunk bytes, so the T-C06 ingestion
  contract is unaffected.
- **The Lane C surface** — `concepts.yaml` (82 nodes), `concept_edges.yaml`
  (84 derived PART_OF + 73 semantic edges, 73 HUMAN_VALIDATED via C41),
  `spec_command_kinds.yaml` (72 rows): byte-untouched by every stage; the C41
  promotion record and its round contract stay the standing proof for those
  rows.
- **The 45 wrong codes' coverage arithmetic** — codes that lose their (wrong)
  anchored coverage may drop below the current 111; codes gaining coverage
  rise above it. The 111/188 bound and the 77-uncovered worklist are
  **recomputed at R3, never carried forward as assumptions**; the C31 §3
  bound stays on its own record as a measurement under the defective mapping.
- **Held quarantine** — the 45 Lane C held candidates and the substrate's
  worklist lanes (2 + 79 Part B decisions) remain recorded-not-forced; R1's
  residual verdict resolves ONE item of the 2 unresolved-span lanes, the other
  follows whatever that verdict finds (no forcing).
- **Standing checkers** — `graph_check.py`, `check_no_hardcode.py`,
  `sme_spcpt_verify.py` (code-domain membership — corrected codes stay inside
  the 188) re-green at R2/R3; `sme_notes_verify.py` is chemistry-scoped and
  untouched.

## 6. Scope guards (standing, from C31 §7 unchanged)

Zero bytes in `graph/igcse-chemistry/**` or `parsed/**` canonical JSON (the
notes-join `_derived/` artifact is the documented derived-lane exception; the
resolution-file amendment is the operator-gated R1 exception this scope
requests explicitly); the C25–C41 records unedited — every correction lands as
a dated record of its own; no core or hub serving changes from this repo; no
K3/K4 work; Lane D and the relationships store stay deferred; the parallel
chemistry program and the 49-course corpus surfaces untouched. Scoping adds
**no store bytes, no join re-run, no resolution edit** — this landing is the
scope record, its machine mirror, and the verification battery only.

## 7. The operator gate sequence this scope requests

| Gate | Authorizes | Evidence the operator sees |
|---|---|---|
| **R1 (gate 1)** | the repair verdict round: 45 id-level corrected codes (or UNRESOLVED), the residual adjudication, the 16 section-level dispositions; the in-place resolution amendment + validation-string clause | per-id proposal table + the fill's evidence quotes; the R0 EQ blast-radius census; per-row provenance diff preview |
| **R4 (gate 2)** | the rebuilt substrate's review outcome (and only that) — the ≥90% per-class gate on the new surface | the fresh review sheet + fill record: strata table, remaining defect inventory (if any), Part B re-decisions |
| **R5 (gate 3)** | the §18 substrate apply — SUGGESTED → HUMAN_VALIDATED for exactly the rows the R4 sheet authorizes | the promotions file + two-way audit report, the structural-diff-zero proof |

If R4 fails its gate again, the loop returns to the operator with the new
defect inventory — the rework lane repeats R1-shaped rounds only by explicit
operator instruction; nothing self-repairs.

## 8. Verification battery (this assessment)

`scripts/c42_k2b_rework_scope_check.py` — zero-LLM, deterministic, read-only
toward `graph/`, the SME corpora and `parsed/**` (writes only its own report):

| Gate | Asserts |
|---|---|
| **G1** `baseline_state` | HEAD == `720b86b…`; maths-a registry resolves the 9-store K2 exit shape; C39/C40/C41 records + checks present with the pinned sha256_16s; tree clean of this scope's predecessors |
| **G2** `defect_inventory` | the verdict record: 468 rows, 351/117, roots 101 note-level + 16 section-level; 45 distinct (note, code) joins over 45 notes / 36 distinct codes; 16 section-level over 10 notes; fill-record gate outcome FAIL, `classes_pass: false` |
| **G3** `resolution_substrate` | counts 222/218/4 == observed (4 null-code rows); validation string carries AI_VALIDATED + operator-delegated + T-SPEC-10 + PMT-excluded; every one of the 45 defective anchors resolves in the file; every currently resolved code ∈ the canonical 188 (0 foreign today) |
| **G4** `blast_radius` | 40/45 ids with `referenced_by_parts > 0`, sum == 996; `build_learner_spec_links.py` consumes the maths-a resolution (consumer claim verified in source) |
| **G5** `store_surface` | 939 rows == 860 anchored + 2 anchor-unresolved + 77 unmapped-SP; 189 rows ride on the 45 notes, 59 on the 10 section-level notes; every row SUGGESTED (anti-forgery field scan); 111 codes covered |
| **G6** `protected_surfaces` | concepts 82 / concept_edges 157 (84 + 73) / kinds 72 counts; the 73 HUMAN_VALIDATED semantic edges present; C41 promotions file round contract intact; chemistry stores untouched |
| **G7** `scope_self_consistency` | the scope JSON's stages R0–R5, gate sequence and inventory numbers == this MD; state snapshot recorded |

Result at landing: **G1–G7 all PASS, exit 0** →
`graph/reports/C42_K2B_REWORK_SCOPE_CHECK.json`.
