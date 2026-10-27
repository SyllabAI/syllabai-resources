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
| G9 learner-surface | the question works in the REAL syllabai-v2 renderer (rendered-question benchmark; `benchmark/README.md`) | any rendered/interaction/solution check FAIL; NOT_RUN never counts as a pass |

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

## Status — igcse-physics-19 (second lane, landed Task 16; MS-parser wave Task 17; QP-side wave Task 18; crop-eyeball + spec-labels waves Task 21)

- **53 of 58 census paper dirs of 4PH1 (all 17 series, 2019-06 … 2026-06) are converted
  and LANDED under ADR-039**: 520 questions, 2,171 parts, 4,790 marks, converter v0.24.0.
  **Every slice passes every gate (G0–G7), the lane is 53/53 fully PASS.** Task 17 (F72)
  closed G5 corpus-wide (2,171/2,171 parts carry their verbatim MS block); Task 18 (F85,
  the QP-side wave) closed G3 corpus-wide (135/135 keyed); **Task 21 (F99 the crop-eyeball
  wave + F100 the spec-labels wave) cleared the human-review surface and completed spec
  tagging**: all 65 review-flagged assets eyeballed (23 crops accepted, 5 wrong-region
  crops rejected to honest stubs, 7 recropped at eyeballed boxes, 12 stubs resolved by
  manual crops — every replacement rect proof-rendered before shipping) and all 2,171
  parts terminal (2,106 registry-validated llm-spec-wave codes + 65 no-spec-point
  decisions + 0 pending-llm). The withheld surface is now EMPTY and the asset review
  flags are zero.
- 5 dirs dispositioned with standing receipts — and the two conversion gaps CLOSED
  by Task 22 (F101/F102): 2019-06 1P recovered through the OCR source layer, the
  2023-06 2P repair-reconversion consumed, and the 2020-11 NO-QP trio stays
  `na:pmt-not-listed` (one-round source probe receipted). **The lane is 55/55
  fully PASS at converter v0.25.0** (LANE-STATUS.md is the disclosure of record).
- **Hub handover LANDED (F103, H3 cutover)**: the hub's Past Papers plane serves
  `official-papers.json` — 55 official sets (540 questions / 2,254 parts / 4,970
  marks) exported from this corpus (manifest `importSource.ref` = the corpus
  commit of record). The older "hub still serves the SME sets" state above is
  historical.
- **Learner-surface verification (G9)**: the rendered-question benchmark
  (`benchmark/`) drives the real syllabai-v2 renderer over 8 frozen cases
  spanning all three lanes — 8/8 PASS at `benchmark_version` 1; receipts in
  `benchmark/receipts/`.

