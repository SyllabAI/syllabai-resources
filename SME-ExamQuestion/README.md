# SME Exam Questions — multi-course corpus (Edexcel)

Atomized Save My Exams exam questions (questions + mark schemes +
images + KaTeX equations) for **Edexcel** courses, one folder per
SME course variant. Every question part keeps its SME spec-point
ids; official 4CH1 codes are resolved for `igcse-chemistry-19`
(see that course's `VALIDATION.md`).

**Provenance & authorization:** scraped from savemyexams.com under
the operator's documented SME authorization — see `../LICENSE-DATA.md`
(Amendment 2026-09-17, SME attestation; covers all SME corpora in
this repo).

## Layout

    SME-ExamQuestion/
      manifest.json        this registry (course table + status)
      <course-slug>/
        manifest.json      course-level totals + per-topic state
        spec_point_index.json   (where harvested) SME spec points
        <section>/<topic>/topic.json · questions.md · mark-schemes.md · assets/

Corpus schema: `syllabai.sme-exam-questions/1.1` — vs the chemistry
v1: `question_set` became `question_sets[]` (IAL topics split into
`multiple-choice-questions` + `structured-questions` set pages),
questions carry `set_slug`, and `scrape` tracks `sets_completed` +
`asset_map` (merge-safe resumability).

IGCSE courses: 26 · IAL courses: 0 — see
`manifest.json` for the authoritative per-course status/counts.

## Pipeline

    scripts/sme_examq_courses.py        # registry from sitemaps
    scripts/sme_examq_scrape_all.py --course <slug>
    scripts/sme_examq_scrape_all.py --update-registry

(public pages only; no credentials; resumable per set page)
