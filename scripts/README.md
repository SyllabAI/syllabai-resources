# Corpus maintenance scripts

- `c05_recover_spec_images.py` — one-off (2026-09-10): downloaded the 5
  ocr.z.ai images embedded in the specification markdown from their expiring
  signed URLs into `assets/` and localized the references. Pattern to re-apply
  if a future conversion embeds expiring URLs.
- `c05_repair_clipper_refs.py` — re-runnable: repairs the Obsidian Web
  Clipper `{pageTitle}` image-reference bug across `Chemistry IGCSE Revision
  Notes/`. Run after every new clip batch:
  `python3 scripts/c05_repair_clipper_refs.py`
- `c05_book_ocr.py` — Student Book conversion driver (baidu/Unlimited-OCR).
  Two backends: `--backend vllm` (full 383-page run against the official
  vLLM docker image — see ../BOOK_OCR_RUNBOOK.md) and `--backend space`
  (HF demo Space; pilots/small batches only — ZeroGPU quota). Resumable via
  `manifest.json`; outputs CMC-shaped per-page markdown with front matter.
- `c09_spec_graph_extract.py` — T-C09 Phase 1 (2026-09-11): deterministic,
  zero-LLM specification-skeleton extraction from the 4CH1 Issue-3 spec md,
  cross-checked statement-by-statement against the official PDF. Regenerates
  the whole `graph/` tree (6 YAML files + 2 reports); hard gates abort the
  run on any count/mismatch regression. Re-run after any spec-md change:
  `python3 scripts/c09_spec_graph_extract.py`
  (requires: pyyaml, pymupdf)
- `graph_check.py` — T-C09 Phase 1 validator: schema, `4CH1-*` namespace,
  no cross-curriculum refs, provenance completeness, referential integrity,
  count consistency over `graph/*.yaml`. Zero core-repo dependencies. Run
  after regeneration, and before any git PR that touches `graph/`:
  `python3 scripts/graph_check.py`
  Negative-tested against 8 corruption classes (provenance loss, foreign
  node codes, invented edge relations, membership drift, foreign prose,
  duplicate ordering, cross-check regression, record removal).
- `c10_worksheets.py` — T-C10 Phase 2 (2026-09-11): deterministic worksheet
  generator for the AI mapping pass. Verifies the 28 SME topic-group slugs
  align 1:1 (count + ordering) with the 28 spec subsections, then emits
  per-subsection worksheets (spec statements + note headings/excerpts) into
  `scripts/c10_worksheets/`. Re-run after any note batch change:
  `python3 scripts/c10_worksheets.py`
- `c10_map_notes.py` — T-C10 Phase 2 applier: writes the AI mapping
  decisions (`scripts/c10_decisions/S*.json`) into the 112 notes' front
  matter as `spec_map:` blocks (PROVIDER subsection anchor + AI_SUGGESTED
  point mappings with evidence/confidence/model_version/rationale). HARD
  gates: evidence-verbatim-in-note (anti-hallucination), codes ∈ 182-point
  registry, ≥1 mapping per note, body byte-identical, idempotent re-run,
  G7 promotion-block shape (see `c10_promote.py`). Promotions live in the
  decisions JSON as optional per-mapping `validation` blocks and are
  carried into the front matter as `validation_status: HUMAN_VALIDATED` +
  `validated_by` + `validated_date` — NEVER hand-edit note front matter for
  promotion (the applier regenerates it from decisions). Also regenerates
  `graph/reports/PHASE2_MAPPING_COVERAGE.md`; the spot-check
  sheet is only regenerated if absent (an issued sheet carrying an operator
  review record is preserved — `--regen-spot-check` discards it deliberately):
  `python3 scripts/c10_map_notes.py [--dry-run] [--regen-spot-check]`
- `c10_rework_415.py` — T-C10 operator-review rework (2026-09-11): moves the
  4CH1-4.15 mapping rejected in the operator spot-check (sheet entry #7) from
  the combustion note to the S4-b sibling Nitrogen Oxides & Sulfur Dioxide
  note whose evidence states the causal relationship in-note. Idempotent;
  preserves the decisions files' compact JSON style:
  `python3 scripts/c10_rework_415.py`
- `c10_round4_rejects.py` — T-C10 round-4 rework (2026-09-11): executes the
  external advisor's two fourth-round rejections (Z.ai concurred, repo-
  verified) — REMOVES 4CH1-4.15 from the NOx note (no corpus note teaches
  the impurity -> SO2 formation explanation; 4.15 becomes an annotated
  zero-coverage corpus gap) and 4CH1-1.17 from Calculate Relative Mass
  (a calculate-point needs the calculation; 1.17 keeps its S1-c mapping);
  appends review-sheet §12 (59 CONFIRM / 2 REJECT + the 59-spec staged
  batch derived mechanically from §11, which it marks ON HOLD) and guide
  §8 (issue 3 — the command-kind substance rule, frozen); exposes
  `ROUND4_REJECTS` for the audit. Idempotent:
  `python3 scripts/c10_round4_rejects.py && python3 scripts/c10_map_notes.py`
- `c10_spotcheck_verdicts.py` — records the operator's 20 spot-check verdicts
  (2026-09-11 chat review) onto the issued sheet: per-entry verdict lines
  with attribution + appended review record + lock marker. Idempotent:
  `python3 scripts/c10_spotcheck_verdicts.py`
- `c10_negative_test.py` — T-C10 validator negative tests: 10 corruption
  classes (spec_map removal, invented codes, emptied evidence, corrupted
  anchor, emptied mappings, foreign 4CH0 code, deleted note, premature
  HUMAN_VALIDATED tier, promotion without validated_by/date, stray
  validated_by on a SUGGESTED mapping) injected into a throwaway copy; all
  must be caught, plus a positive control proving a COMPLETE HUMAN_VALIDATED
  block passes:
  `python3 scripts/c10_negative_test.py`
- `c10_promote.py` — T-C10 PR-review promotion helper (2026-09-11): marks
  confirmed mappings as HUMAN_VALIDATED in the decisions JSON (source of
  truth) and re-runs the gated applier in one step, so the front matter
  carries the promotion. `--map CODE` (unique) or `--map CODE@FRAGMENT`
  (disambiguate multi-note codes), `--by/--date` recorded on the promotion,
  `--no-apply` for decisions-only. Idempotent (re-promoting is a no-op):
  `python3 scripts/c10_promote.py --map 4CH1-4.15 --map '4CH1-1.10@chromatography'`
- `c10_pr_review_guide.py` — T-C10 PR front-matter review guide generator
  (2026-09-11): emits `graph/reports/PHASE2_PR_REVIEW_GUIDE.md`, the work
  order for the remaining operator gate in their stated priority order
  (remapped 4.15; the 1 low; the 34 medium — cross-note-deferral-flagged
  first; the 1.17 cross-subsection flag; cross-note deferral candidates;
  diagram-dependent mappings incl. the 3 figure-missing notes). Deterministic
  (decisions JSON + registry + note image-resolution scan); reflects the
  current promotion state when regenerated mid-review. Issue 2 (same day)
  states the mapping contract in §0.0 — mappings are CONTRIBUTORY
  many-to-many relationships (SME notes group and split spec points; measured
  69/112 notes carry 2+ points, 25/182 points covered by 2-3 notes), with
  the reject conditions and the honest §7 closure criterion (risk-prioritized
  validation; unreviewed mappings stay AI_SUGGESTED and must never be
  represented as human-validated):
  `python3 scripts/c10_pr_review_guide.py`
- `c10_pr_review_verdicts.py` — T-C10 PR review EXECUTION sheet generator
  (2026-09-11): renders `graph/reports/PHASE2_PR_REVIEW_SHEET.md` — the
  AI review pass over the whole issued queue (61 distinct mappings: 4.15,
  1.4, all 34 mediums, both 1.17s, the 21-mapping diagram queue, the 7
  missing-figure mappings). Per-mapping verdicts with what was actually
  read (whole notes, sibling checks, VLM image verdicts archived in
  `scripts/c10_vlm_results/`). 61 CONFIRM / 0 REJECT / 0 HOLD; the staged
  operator ratification command (§11) promotes exactly the reviewed set —
  the sheet is the review, NOT the promotion (everything stays SUGGESTED
  on disk until the operator runs it). Idempotent:
  `python3 scripts/c10_pr_review_verdicts.py`
  (Round 4, same day: the advisor + Z.ai review rejected 2 of the 61 — see
  `c10_round4_rejects.py`; sheet §12 supersedes §1/§11 and the batch is 59
  specs.)
- `c10_rework_rationales.py` — T-C10 review rework (2026-09-11): rewrites
  six confirmed mappings' rationales for honest contributory wording
  (4.15, 1.4, 1.16@Atoms, 2.29, 3.10, 1.17@S1-e). Evidence, confidence,
  tier, validation state and mapping sets unchanged; note bodies stay
  byte-identical (front-matter-only regen via the applier). Idempotent:
  `python3 scripts/c10_rework_rationales.py && python3 scripts/c10_map_notes.py`
- `c10_vlm_results/` — archived raw VLM (glm-5v) verdict JSONs for the 21
  diagram-dependent mappings (incl. the prior 1.52C check). Evidence
  artifact backing the review sheet §7; one JSON per mapping.
- `c10_ratify_audit.py` — T-C10 ratification reconciliation audit
  (2026-09-11, READ-ONLY; round-5 dual-batch edition): the
  machine-verifiable check over BOTH staged batches — sheet §12 (59-spec,
  round-4 survivors) and sheet §13 (150-spec, round-5 CONFIRMs, staged by
  `c10_round5_batch.py`). `--phase pre` (default) is the pre-execution
  reconciliation: resolves each section's `--map` specs with the PRODUCTION
  `c10_promote.py` resolver, proves bijection review-record ↔ command for
  both batches (59/59 and 150/150), disjointness (§12 ∩ §13 = ∅) and
  exact-once coverage of the whole 209-mapping store, both round-4 REJECTs
  absent, pre-state 0 promoted / 209 SUGGESTED, store shape, 29 VLM
  files, HEAD descending from the pushed round-5 state. `--phase post`
  verifies the executed state: 209/209 HUMAN_VALIDATED (operator /
  2026-09-11) == §12 ∪ §13 exactly, shape unchanged, all 150 evidence
  quotes retained + the 2 recorded rationale corrections applied
  verbatim, and all 112 note bodies byte-identical to the round-5 review
  state (promotion touches front matter only). Writes
  `graph/reports/C10_RATIFICATION_AUDIT.{json,md}`; mutates nothing else:
  `python3 scripts/c10_ratify_audit.py [--phase pre|post]`
- `graph_check.py` group 6 (`c10-notes-mapping`) — persistent-state check of
  the applied T-C10 mapping (schema, registry membership, provenance
  vocabulary, anchor-vs-slug, foreign codes, totals 112/209/181 — round-4
  baseline after the 2 rejections). Runs as
  part of the normal `graph_check.py` invocation; `--notes-root` points it
  at an alternative tree for testing.
- `c10_round5_enumerate.py` — T-C10 round-5 enumeration + dossier builder
  (2026-09-11, READ-ONLY): computes the exact 150 unreviewed (note, code)
  pairs (store 209 minus the 59 round-4-surviving ratification targets;
  both rejected pairs proven absent) and writes the review dossiers used
  for the exhaustive pass (heading outline + the evidence-enclosing
  markdown section + preceding-section context; image lines compressed).
  Dossiers and targets live OUTSIDE the repo
  (`/home/z/my-project/scripts/round5/`); the mapping store is untouched:
  `python3 scripts/c10_round5_enumerate.py`
- `c10_round5_assemble.py` — T-C10 round-5 artifact assembler (2026-09-11,
  READ-ONLY): merges the 8 batch verdict files (150 verdicts) with the
  enumeration into `graph/reports/C10_ROUND5_REVIEW.json` + the exhaustive
  150-row `graph/reports/PHASE2_ROUND5_REVIEW_SHEET.md` (counts, VLM table,
  REJECT/HOLD records — none —, corrected rationales, coverage impact,
  adversarial observations, pre-review SHA). Hard-completeness asserts
  (idx 1..150, code/note identity, verdict vocabulary); mutates nothing:
  `python3 scripts/c10_round5_assemble.py`
- `c10_vlm_results/round5-*.json` — archived raw VLM (glm-5v) verdict
  JSONs for the 8 diagram-dependent mappings among the 150 (1.40, 1.46,
  3.5C, 3.14C, 4.26, 4.41C, 4.45, 4.49C). Evidence artifact backing the
  round-5 review sheet §5.
- `c10_round5_rework.py` — T-C10 round-5 rationale rework (2026-09-11):
  applies the two rationale corrections recorded (not applied) by the
  round-5 review — 4CH1-1.1 overstatement repair, 4CH1-1.19
  under-description repair — verbatim from `C10_ROUND5_REVIEW.json`
  `corrected_rationales` (byte-for-byte; evidence + confidence +
  validation unchanged; note bodies byte-identical, front-matter
  rationale lines only). Idempotent; followed by the gated applier re-run:
  `python3 scripts/c10_round5_rework.py`
- `c10_round5_batch.py` — T-C10 round-5 promotion stager (2026-09-11):
  derives the §13 150-spec staged batch command mechanically from
  `C10_ROUND5_REVIEW.json` (operator instruction "Ratify the 59 and
  promote 150" — one controlled promotion, no risk/section split) and
  rewrites the sheet's machine region idempotently (END marker preserves
  any execution record). Every spec is proven against the production
  resolver before writing: bare CODE only where the code lives on one
  note, else `CODE@FRAGMENT` via the stem -> parent/stem -> full-path
  ladder; §12 ∩ §13 = ∅ and §12 ∪ §13 = the whole store:
  `python3 scripts/c10_round5_batch.py`
