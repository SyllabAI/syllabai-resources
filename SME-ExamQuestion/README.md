# SME Exam Questions — Edexcel IGCSE Chemistry (4CH1)

Scraped corpus of **Save My Exams** exam questions (topic questions) for
Edexcel IGCSE Chemistry, syllabus 2017 (4CH1). Every question carries its
mark scheme / model answer, per-part marks, command word, original paper
provenance, and SME spec-point references. Topics mirror the revision-notes
corpus in `../Chemistry IGCSE Revision Notes/` (section/subtopic tree is the same).

**Provenance & authorization:** scraped from savemyexams.com under the
operator's documented SME authorization — see `../LICENSE-DATA.md`
("Amendment 2026-09-17 — Save My Exams authorization (operator attestation)").
Questions are attributed to their original Edexcel papers where SME records
that provenance (per-part `source_paper`).

## Layout

    SME-ExamQuestion/
      manifest.json                     course-level index + totals
      <section-slug>/<topic-slug>/
        topic.json    structured corpus: questions -> parts -> problem/solution
        questions.md  human-readable question paper (images inline)
        mark-schemes.md  human-readable mark scheme / model answers
        assets/       question images (original CDN format: webp/png/gif)

## topic.json schema (syllabai.sme-exam-questions/1.0)

- `questions[]`: `id`, `difficulty` (easy/medium/hard), `style`, `total_marks`
- `questions[].parts[]`:
  - `marks`, `command_word`, `question_type` (`structured` | `multiple_choice`)
  - `source_paper`: `{date, number, question_number, question_part}` (provenance)
  - `spec_point_ids`: SME spec-point ids (raw; resolution to 4CH1 codes is downstream)
  - `problem_md` / `solution_md`: Markdown render of the TipTap docs
  - `choices[]` (MCQ): `label`, `is_correct`, `text_md`
  - `equations[]`: KaTeX `latex` + raw Wiris `mathml` (lossless re-processing)
- `subtopics[]`: SME subtopic slugs + `revision_note_id` (maps to the notes corpus)

## Rendering conventions

- Equations are KaTeX (`$...$`); raw MathML kept in `equations[]`.
- Chemical formulas use `<sub>`/`<sup>` HTML tags.
- Examiner commentary renders as blockquotes (`> ...`) in `mark-schemes.md`.
- The highlighted final answer renders as `**Final answer:** ...`.
- Bold lines in `mark-schemes.md` are SME's creditable marking statements
  (their `examMark` text-mark); authoritative per-part marks live in
  `part.marks`.
- Images reference `assets/…` relatively.

## Totals

- topics: 28 · questions: 524 · parts: 1404
- marks: 3708 · assets: 585 · equations (KaTeX): 461

## Regeneration

    scripts/sme_examq_scrape.py --out SME-ExamQuestion

(public pages only; no credentials needed; idempotent per topic)
