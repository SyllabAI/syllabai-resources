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

All 39 courses (26 IGCSE + 13 IAL) are scraped — see
`manifest.json` for the authoritative per-course status/counts.

## Spec-point index harvest

All 39 courses carry `spec_point_index.json` (SME-native `spcpt_` id →
name / definition / note linkage, harvested from that course's
revision-note pages; coverage vs question-part ids is recorded in each
index and summarized in the registry `manifest.json` `spec_index`
blocks): 5,068 distinct spec points from 3,195 note pages, 0 fetch
failures. Batches: `igcse-chemistry-19` (T-SME-EQ-1, also resolved to
official 4CH1 codes), the 10 single-segment courses (T-SME-EQ-2), and
the 29 variant-aware courses — ial-maths units, modular-24 science
units, maths-a foundation/higher + modular units, accounting variants,
science-double-award sciences (T-SME-EQ-2 batch 2).

Known SME-side gaps, honestly recorded (never fabricated): 326 part-id
references across 14 courses have no note page under their own course
tree — 254 resolve in a sibling tree of the same subject family
(cross-unit/cross-tier tagging, e.g. IAL maths pure-2 questions tagged
with pure-1 points; double-award physics points living in the
triple-award physics notes), and 72 exist nowhere in the SME notes
corpus (English literature set texts 21, maths-a linear tiers 27,
physics-modular 11, IAL pure units 5, chemistry-modular 6, accounting 2
— verified absent from every fetched note page). Ingest should treat
the union of subject-family indexes as the bridge. No official spec
codes are invented for non-chemistry courses: only 4CH1 has a registry
here.

## Pipeline

    scripts/sme_examq_courses.py        # registry from sitemaps
    scripts/sme_examq_scrape_all.py --course <slug>
    scripts/sme_examq_scrape_all.py --update-registry
    scripts/sme_notes_discover.py       # notes URLs per course from sitemaps
    scripts/sme_spcpt_harvest_all.py --courses <slug,slug,...>
    scripts/sme_spcpt_harvest_verify.py # G1-G5 gates over harvested indexes

(public pages only; no credentials; resumable per page)
