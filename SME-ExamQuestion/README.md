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

## Spec-point index harvest

11 of 39 courses carry `spec_point_index.json` (SME-native
`spcpt_` id → name / definition / note linkage, harvested from that
course's revision-note pages; coverage vs question-part ids is recorded
in each index): `igcse-chemistry-19` (T-SME-EQ-1, also resolved to
official 4CH1 codes) + the 10 single-segment courses (T-SME-EQ-2:
ial-biology-18, ial-chemistry-17, ial-further-maths-18-further-pure-1,
ial-physics-19, igcse-business-19, igcse-economics-17,
igcse-english-literature-16, igcse-further-maths-19, igcse-geography-19,
igcse-ict-17 — 1,157 note pages, 0 fetch failures; every course at 100%
part-id coverage except igcse-english-literature-16 at 110/131, where
SME publishes no notes for the An Inspector Calls / Romeo & Juliet /
Macbeth assessment points). The remaining 29 courses (ial-maths units,
modular-24 units, maths-a foundation/higher, accounting variants,
science-double-award sciences) need variant-aware notes mapping — a
later batch. No official spec codes are invented for non-chemistry
courses: only 4CH1 has a registry here.

## Pipeline

    scripts/sme_examq_courses.py        # registry from sitemaps
    scripts/sme_examq_scrape_all.py --course <slug>
    scripts/sme_examq_scrape_all.py --update-registry
    scripts/sme_notes_discover.py       # notes URLs per course from sitemaps
    scripts/sme_spcpt_harvest_all.py --courses <slug,slug,...>
    scripts/sme_spcpt_harvest_verify.py # G1-G5 gates over harvested indexes

(public pages only; no credentials; resumable per page)
