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
