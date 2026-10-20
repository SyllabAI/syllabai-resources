# Official-ExamQuestion — extracted official past-paper questions

> Defined by **ADR-037** (`syllabai` repo): *official-paper questions are EXTRACTED, never
> regenerated* — verbatim-first conversion with fail-closed gates. This directory is the
> derived, serving-side counterpart of the byte-frozen `SyllabAI/syllabai-pastpapers`
> archive, mirroring the layout of `../SME-ExamQuestion/`.

## Why this lives here and NOT in syllabai-pastpapers

- `syllabai-pastpapers` is the **archive of record**: official PDF bytes + manifests +
  parsed markdown, frozen for identity and licensing (`LICENSE-DATA.md`). It must stay
  byte-stable and free of derived, editable teaching content.
- This directory is **derived serving content** in the schema shape the app already
  consumes, with one-way provenance back to the archive (`paper_id` + `qp_sha256` +
  `ms_sha256` + per-part `source_page`). Derivation flows `pastpapers → resources`,
  never the reverse; a re-ingested/corrected PDF orphans its derivatives at G0.

## Layout (mirrors SME-ExamQuestion)

    Official-ExamQuestion/<spec-folder>/<series>/<paper>/
      topic.json               syllabai.official-paper-questions/0.1
      questions.md             human-readable render (choices keyed, assets noted)
      validation-report.json   G0–G6 gate receipts + negative controls + review queue

    scripts/official_examq_extract.py    the converter (deterministic; no LLM in the loop)

## The gates (fail-closed; a paper ships only when they pass)

| Gate | Property |
|------|----------|
| G0 identity | sha256(QP/MS) match `manifest.yaml`; registry paper_id wins over printed text (the "June 2020" ↔ Nov-2020 mislabel is the canonical example) |
| G1 structure | Σ part marks = printed question total; Σ question totals = paper total |
| G2 verbatim | every `problem_md` 5-gram-overlaps ≥0.95 with its own extracted source lines — any post-hoc edit fails loudly |
| G3 MCQ integrity | options exactly as printed (Edexcel A–D), exactly one MS-keyed answer; unresolved → review, never auto-keyed |
| G4 figures | every table/diagram/grid/apparatus mention resolves to a page-anchored asset record (crop-required until the crop pass) |
| G5 answers | positional linkage into the official MS; coverage reported; unmatched → review |
| G6 registry | spec codes must exist in the SME spec-point resolution registry or be documented gaps → review; nothing fabricated |

Negative controls run every session: a bumped mark, a one-word paraphrase, and a fake
spec code MUST be DETECTED by G1/G2/G6 respectively, else the run is void.

## Status (full-corpus run, converter v0.3)

- **All 16 series of 4CH1/1C present in syllabai-pastpapers are converted**: 169
  questions, 930 parts, 1754/1760 marks extracted, every MCQ keyed except two
  honest 2020-01 refusals, negative controls 3/3 on every series.
- **14/16 series: all gates PASS.** The two exceptions are correct terminal states,
  not defects: 2020-01 G3 FAIL (honest refusal — interleaved MS marker rows, see
  canary C1/C2) and 2019-06 G1/G5 REVIEW (rasterized archive pages; Q7 wholly lost,
  attributed, nothing invented).
- **Independent-parse agreement**: part-level marks match the repo's own
  `parsed/questions.json` layer 161/161 across 2024-06, 2025-06, 2026-06
  (`CROSS-DIFF.json`).
- Agent operations: `AGENTS.md` (protocol + improvement loop), `LEDGER.md` (findings
  F1–F14), `CANARIES.json` + `check_canaries.py` (regression assertions),
  `run_all.sh` (one-command full-corpus run), `CHANGELOG.md` (converter history).
- Open work: human review queues (2020-01 MCQ keys, figure crops, `pending-llm`
  spec tagging), 2019-06 re-ingest, then new courses per ADR-037 §6 (4XCH1 modular,
  4SD0 shared papers).
