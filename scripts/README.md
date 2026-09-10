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
