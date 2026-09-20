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

41 of the 49 courses (36 IGCSE + 13 IAL) are scraped; the other
8 are honestly empty — see `manifest.json` for the authoritative
per-course status/counts and the empty-lanes section below.

## Set-page model & the T-SME-11 lanes (2026-09)

SME's frontend moved some courses to per-session "question set" pages
(each exam session embeds its own questions). The ELA 4EA1 lanes are
scraped with `scripts/sme_examq_setpage_scrape.py`, which reproduces the
corpus conventions exactly (same topic.json schema, atomization and
renderers) with set-page orchestration; questions carry `set_slug`.

T-SME-11 added 10 lanes to reach 49 courses end-to-end:
ELA paper-1 (100 questions) and paper-2 (65 questions) scraped; ELA
paper-3 (coursework), maths-b (4MB1) and the six science-double-award
modular units (4XSD1) have **no topic questions published on SME** and
are recorded honestly as `no_topic_questions_on_sme` — never
synthesized. New lanes also carry `spec_point_map.json` +
`spec_point_resolution.json` sidecars (T-SPEC mapping), not just
`spec_point_index.json`.

## Empty lanes — live re-verification (2026-09-20)

The 8 empty lanes were re-verified against the live SME frontend; the
gap is SME-side, not a scrape defect (evidence also embedded in each
lane's `status_note`):

- maths-b (4MB1/2016): syllabus-version flag
  `has_published_topic_questions=false`; all 62 topics
  `published_questions_count=0` with empty `question_sets`
  relationships; no topic-questions study-tool link. SME's only exam
  material for Maths B is 52 past-paper entries (family-level
  `/igcse/maths/edexcel/b/past-papers/`) linking Pearson-hosted 4MB1
  PDFs — out of scope for this atomized SME-authored corpus.
- SDA modular units (4XSD1/2024): syllabus flag false; 8/12/13/9/8/10
  topics across the six units, all `published_questions_count=0`;
  per-topic `question_set` relationships hold only unpublished
  `qstnst_` shells.
- ELA paper-3 coursework: module flag
  `has_published_topic_questions=false`; the topic-questions URL's
  question-set payload is the sibling paper-1 session-set listing, not
  Paper 3 content.

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
                                        # (operator-scratch,
                                        #  not committed; retained
                                        #  artifacts:
                                        #  scripts/t_spec_10_work/sme11/)
    scripts/sme_examq_scrape_all.py --course <slug>
    scripts/sme_examq_scrape_all.py --update-registry
    scripts/sme_notes_discover.py       # notes URLs per course from sitemaps
    scripts/sme_spcpt_harvest_all.py --courses <slug,slug,...>
    scripts/sme_spcpt_harvest_verify.py # G1-G5 gates over harvested indexes

(public pages only; no credentials; resumable per page)
