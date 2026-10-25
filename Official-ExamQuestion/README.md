# Official-ExamQuestion — extracted official past-paper questions

> Defined by **ADR-039** (`syllabai` repo, 2026-10-24 — supersedes ADR-037's verbatim-first
> and no-LLM clauses): *the pipeline improves; provenance discloses* — any tool may correct,
> clarify or enrich any serving field, every departure from the extracted source layer is
> machine-disclosed (`edit_status` + `edits[]` + `value_trace`), and graded values (marks,
> mark_points, MCQ keys) must corroborate the mark scheme of record. ADR-037's extraction
> layer remains the deterministic baseline disclosure is measured against; identity (G0),
> structure (G1), figure resolution (G4), answer linkage (G5) and registry (G6) are
> unchanged. This directory remains the derived, serving-side counterpart of the
> byte-frozen `SyllabAI/syllabai-pastpapers` archive, mirroring `../SME-ExamQuestion/`.

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
      questions.md             human-readable render (choices keyed, figure crops embedded, mark-scheme answers)
    assets/*.png            figure crops rendered from the QP PDF at 150 dpi
      validation-report.json   G0–G6 gate receipts + negative controls + review queue

    scripts/official_examq_extract.py    the converter (deterministic; no LLM in the loop)

## The gates (fail-closed; a paper ships only when they pass)

| Gate | Property |
|------|----------|
| G0 identity | sha256(QP/MS) match `manifest.yaml`; registry paper_id wins over printed text (the "June 2020" ↔ Nov-2020 mislabel is the canonical example) |
| G1 structure | Σ part marks = printed question total; Σ question totals = paper total |
| G2-D disclosure | `edit_status` matches reality: `extracted` parts 5-gram-overlap ≥0.95 with their own source lines; `corrected`/`enriched` parts carry a complete `edits[]` (field, kind, tool, evidence_ref) and a consistent `value_trace` — undisclosed edits fail loudly; disclosed edits are lawful |
| G3 MCQ integrity | options match the printed set (Edexcel A–D) or carry a disclosed, evidenced correction; exactly one MS-keyed answer; unresolved → review, never silently auto-keyed |
| G4 figures | every mention resolves to a page-anchored asset record; the crop pass renders croppable figures to assets/*.png (126/158 at v0.5) |
| G7 solutions | every MS-linked part carries solution_md + mark_points summing to the part marks |
| G5 answers | positional linkage into the official MS; coverage reported; unmatched → review |
| G6 registry | spec codes must exist in the SME spec-point resolution registry or be documented gaps → review; nothing fabricated |

Negative controls run every session and target **undisclosed** mutation (ADR-039 §5): a
bumped mark must surface as a value_trace violation, a one-word paraphrase must surface
as a missing `edits[]` entry, and a fake spec code is still refused by G6 — all three
MUST be DETECTED, else the run is void.

## Per-course handover (SME EQ → Official EQ on Past Papers)

On the hub, a course's Past Papers "Interactive" buttons are served by the SME
Exam-Questions sets (their parsed `sourcePaper` provenance) until this pipeline
completes for that course. The handover to the Official sets is then a mandatory
three-receipt stage: **H1** baseline census of what SME currently connects to Past
Papers, **H2** per-paper comparison whose rule is "any SME coverage the Official
output would serve worse is a blocker", **H3** cutover — official sets ship on the
dedicated hub plane (`official-papers.json`, never the Exam Questions tree) and the
SME sets retire from past-paper matching for the course, recorded in `LEDGER.md`.
Full protocol in `AGENTS.md` ("The handover rule"); chemistry (igcse-chemistry-19)
is the executed precedent.

## Status (full-corpus run, converter v0.3)

> **Doctrine note (ADR-039, 2026-10-24):** figures below are historical receipts of the
> ADR-037 era and stand as recorded. "Verbatim" gate references read as G2-D disclosure
> from converter v0.15.0 onward; the 54 slices re-issue with explicit `/0.2` provenance
> fields on the next full-corpus run.

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
- Open work: human review queues (2020-01 MCQ keys, 10 crop-verify + 32 crop-pending, `pending-llm`
  spec tagging), 2019-06 re-ingest, then new courses per ADR-037 §6 (4XCH1 modular,
  4SD0 shared papers).

## Status — igcse-physics-19 (second lane, landed Task 16, MS-parser wave Task 17)

- **53 of 58 census paper dirs of 4PH1 (all 17 series, 2019-06 … 2026-06) are converted
  and LANDED under ADR-039**: 520 questions, 2,171 parts, 4,790 marks, converter v0.19.0.
  **Every slice passes every gate (G0–G7) and the battery is 83/83.** The Task 17
  MS-table parser wave (F72) closed the Task 16 disclosed deltas: G5 answer linkage is
  corpus-complete (2,171/2,171 parts carry their verbatim MS block; baseline was 1,235),
  G3 MCQ keying is 134/138 — the 4 remaining fails are QP-side structural classes
  (choice-label extraction drops + non-MCQ question typing), disclosed in LANE-STATUS,
  never guessed.
- 5 dirs dispositioned with standing receipts: 2020-11 1PR/2P/2PR (no QP in archive,
  `na:pmt-not-listed`), 2019-06 1P (image-only scan, OCR wave open), 2023-06 2P
  (archive bytes are an Examiners' Report — pastpapers repair owed).
- Full disclosure, open waves and receipts: `igcse-physics-19/LANE-STATUS.md`;
  per-slice matrix: `igcse-physics-19/MULTI-SERIES-REPORT.{md,json}`. Hub handover
  NOT started (the hub still serves the SME sets for physics).

