# C39 — K2 Lane C §18 Governed Apply — igcse-maths-a B01..B06

**Generated:** 2026-10-02T07:05:59+00:00  |  **Baseline:** `16257a32f48c0706776e86e634047bf40cf94e31`  |  **Store date (deterministic):** 2026-10-02

## What this is

The §18 governed apply authorized by the operator's consolidated review
(PASS WITH NOTES, 2026-10-02, zai-web) over the six authored-to-gate Lane C
packets (B01..B06, global_order 1–72 = 4MA1-1.1A..2.5A). The confirmed
authored surface is materialized at **authority SUGGESTED** (provenance tier
`AI_SUGGESTED`); nothing is HUMAN_VALIDATED; zero promotion entries; all 45
held candidates stay quarantined in the decision records, none emitted.

## Inputs

- Verdict record: `scripts/c39_maths_a_k2c_verdicts.yaml` (operator-owned; DC-01..03 dated corrections)
- Verdict check: `graph/reports/C39_K2C_VERDICT_CHECK.json` — ALL PASS 8/8
- Consolidated review: `graph/reports/C39_K2C_CONSOLIDATED_OPERATOR_REVIEW.md`
  (sha256 `f33aa7b86ff6f6704e7f972fcfda922a56a0c335ec761f4ddfc21ab3a00200c5`, byte-identical to the operator upload)
- Decision records: `c33_maths_a_batch01_decisions.yaml`, `c34_maths_a_batch02_decisions.yaml`, `c35_maths_a_batch03_decisions.yaml`, `c36_maths_a_batch04_decisions.yaml`, `c37_maths_a_batch05_decisions.yaml`, `c38_maths_a_batch06_decisions.yaml`

## Emitted (counts == the authorized verdict surface)

- `graph/igcse-maths-a/concepts.yaml` — **82 nodes** (71 CONCEPT + 11 MISCONCEPTION), sha256_16 `f4c02fd7d023090d`
- `graph/igcse-maths-a/concept_edges.yaml` — **84 derived PART_OF + 73 authored semantic edges** (51 REQUIRES_PREREQUISITE + 11 WRONG_ANSWER_PATTERN + 11 REMEDIATED_BY), sha256_16 `9aeda071a95c27ce`
- `graph/igcse-maths-a/spec_command_kinds.yaml` — **72 rows** (56 APPLY_PROCEDURE + 15 UNDERSTAND_RELATION + 1 KNOW_TERM), sha256_16 `d3af40ffa36a7db5`
- `scripts/graph_paths.yaml` — maths-a registry 5 → **8 stores** (spec_chunk_mappings arrives with K2-B; relationships with the ratified-hierarchy lane)

## Dated corrections carried (P5)

- **DC-01** held = **45** (the review's own §2 table and the artifacts; the
  '47' aggregate prose in the review is corrected here)
- **DC-02** derived PART_OF = **84** (the artifacts' `derived_partof_at_apply` 13/14/14/13/15/15; the C36/C37/C38 record prose
  '77' undercounted B04/B05/B06 attachments — corrected here, records unedited)
- **DC-03** quote probes 490/490 and preverify 192/192 confirmed as stated

## Governance boundary

- Zero silent promotion: every emitted row is CONFIRM-authorized by the
  verdict record; the held/quarantine surface (45 ids) is preserved verbatim
  in the decision records and emitted NOWHERE.
- The §18 exact-identity promotion round (HUMAN_VALIDATED,
  `c11_promote.py` pattern) remains a separate operator gate.
- Boundary: superseding map {4MA1-1.7C, 4MA1-1.7D, 4MA1-2.7B}; landing
  re-records B06-H-02 (← B05-H-06) and B06-H-03 (← B04-H-06) stay HELD.
- K2-B (chunk substrate) has not run; K3/K4 (serving/explorer) deferred by
  the playbook; chemistry and the corpora byte-untouched.

## Post-apply verification

`scripts/c39_maths_a_k2c_apply_check.py` → `graph/reports/C39_K2C_POST_APPLY_CHECK.json`
(counts, no-held-promoted, uniqueness, endpoint resolution, PART_OF ==
attachments, misconception pairing, anchor byte-verification, negative
controls, registry + standing checkers, determinism re-run).

