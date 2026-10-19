# Edexcel IGCSE Chemistry (4CH1) — SME Exam Questions

> Course folder of the multi-course `SME-ExamQuestion/igcse-chemistry-19/` corpus — see `../README.md` for the registry.

Scraped corpus of **Save My Exams** exam questions (topic questions) for
Edexcel IGCSE Chemistry, syllabus 2017 (4CH1). Every question carries its
mark scheme / model answer, per-part marks, command word, original paper
provenance, and SME spec-point references. Topics mirror the revision-notes
corpus in `../../Chemistry IGCSE Revision Notes/` (section/subtopic tree is the same).

**Provenance & authorization:** scraped from savemyexams.com under the
operator's documented SME authorization — see `../../LICENSE-DATA.md`
("Amendment 2026-09-17 — Save My Exams authorization (operator attestation)").
Questions are attributed to their original Edexcel papers where SME records
that provenance (per-part `source_paper`).

## Layout

    SME-ExamQuestion/igcse-chemistry-19/
      manifest.json                     course-level index + totals
      spec_point_index.json             SME spec-point ids -> name + definition
                                        (harvested from all 112 note pages)
      spec_point_resolution.json        spcpt_ -> official 4CH1 code table
                                        (AI_VALIDATED, operator-delegated;
                                        see VALIDATION.md)
      VALIDATION.md                     validation record for the resolution
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
  - `spec_point_ids`: SME spec-point ids (raw)
  - `spec_point_codes`: resolved official 4CH1 codes (e.g. `4CH1-1.25`),
    ordered by the registry's global order — see `VALIDATION.md`
    (AI_VALIDATED under operator delegation 2026-09-17)
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
- spec points resolved: 162 (SME) -> 154 distinct 4CH1 codes in use;
  1404/1404 parts tagged (parts without SME ids: 46)

## Regeneration

    scripts/sme_examq_scrape.py --out SME-ExamQuestion
    python3 scripts/sme_spcpt_harvest.py          # needs network; cached
    python3 scripts/sme_spcpt_resolve.py --apply  # offline; deterministic
    python3 scripts/sme_spcpt_verify.py           # offline gates + spot-check

(public pages only; no credentials needed; idempotent per topic)

## Question <-> revision-note linkage

Two layers, both present in the data:

1. **Subtopic layer** (SME-native): `topic.json.subtopics[]` carries each
   subtopic's `revision_note_id` and `related_revision_notes_folder` points
   at the matching notes folder.
2. **Spec-point layer** (resolved): each part's `spec_point_codes` intersect
   with the notes' `spec_map` codes in `../../Chemistry IGCSE Revision Notes/`,
   giving note-level links even when SME groups statements differently.
