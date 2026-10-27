# SME Exam Questions — multi-course corpus (Edexcel + Cambridge/CAIE)

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

## Cambridge (CAIE) extension — T-SME-CAMBRIDGE (2026-10-17)

Added by operator directive (trace 1a1472e1880cc011): the attested SME corpora extended to the Cambridge lanes on savemyexams.com — 8 `a-level/cie` full-course lanes (AS+A2), 2 `as/cie` lanes where a-level has no counterpart, 24 `igcse/cie` lanes; O Level out of scope (no Edexcel equivalent). Scraper: `scripts/sme_cambridge_examq_scrape.py` (compiled set-page model, corpus schema 1.1, curriculum page-sourced). Same authorization — LICENSE-DATA.md SME attestation. spcpt/spec-index harvest not yet run for these lanes (no `spec_index` blocks yet — honestly absent).

## 2026-10-26 scrape lane — AS lanes, geography 21, history 17, CIE leaf-gap fill

Operator directive 2026-10-26 (zai-web trace 1a178211cb946f29 "Order a scrape
lane"), following the SME-COVERAGE-AUDIT r0 live-sitemap diff:

- **12 new lanes**: 8 AS courses scraped (biology 25, business 23, chemistry 25,
  computer-science 19, maths 20 as 4 unit lanes — pure-1/pure-2/mechanics/PS1,
  physics 25); 3 recorded honestly empty (as accounting 21, a-level geography 21,
  Edexcel igcse history 17 — all three are past-papers-only stubs on SME:
  topic-questions 404 / zero embedded sets, probed live this lane). Geography 21
  was absent from the 2026-10-17 census; the 7 AS lanes reverse the 2026-10-17
  "subset-view" exclusion per operator order (content overlaps the a-level
  lanes' AS sections by design — syllabai mirrors SME's own catalog).
- **Leaf-gap fill (10 courses re-scraped --force)**: SME landings link only ONE
  leaf-type per topic on several courses (structured/theory/alt-to-practical
  legs reachable only via the sitemap), so the original landing-only discovery
  under-scraped them. Discovery now merges the sitemap census
  (`scripts/sme_cambridge_examq_scrape.py` 2026-10-26 patch). Filled: CIE
  IGCSE sciences theory+ATP legs (chem 528→1300 q, bio 586→995, phys
  662→1197), cie-igcse-accounting-21 SQ leg (+73 q), CIE A-Level sciences SQ
  legs (chem 1003→1336, bio 930→1252, phys 1049→1310), igcse-economics-17
  (+3 topics), ial-biology-18 (+1 synoptic topic), ial-physics-19 (+1 SQ page
  via surgical topic rebuild — its landing links only 6 of 37 SQ pages).
- Edexcel-side note: igcse-history-17 was scraped by the Cambridge toolchain
  (honest-empty probe); the missing `sme_examq_courses.py` (cited by the 49
  Edexcel course manifests) is still absent from scripts/ at main HEAD.
- Observation for the operator: the AS maths tree carries a **pure-2** lane
  SME never published on the A-Level tree — candidate to fill the registered
  `cie-a-level-maths-20-pure-2` skeleton (ruling 2026-10-22), operator decision.
- spec_point_index/registry (v2 courses.json) rows for the new lanes are a
  follow-up; corpus refresh 2026-10-26.

| course | status | topics | questions | assets |
|---|---|---|---|---|
| cie-a-level-accounting-21 | no_topic_questions_on_sme | 0 | 0 | 0 |
| cie-a-level-biology-25 | scraped | 44 | 1252 | 1116 |
| cie-a-level-business-23 | scraped | 33 | 692 | 29 |
| cie-a-level-chemistry-25 | scraped | 90 | 1336 | 1351 |
| cie-a-level-computer-science-19 | scraped | 45 | 1060 | 136 |
| cie-a-level-economics-23 | no_topic_questions_on_sme | 0 | 0 | 0 |
| cie-a-level-geography-21 | no_topic_questions_on_sme | 0 | 0 | 0 |
| cie-a-level-maths-20-mechanics | scraped | 10 | 304 | 332 |
| cie-a-level-maths-20-pure-1 | scraped | 22 | 725 | 363 |
| cie-a-level-maths-20-pure-3 | scraped | 24 | 791 | 182 |
| cie-a-level-maths-20-probability-and-statistics-1 | scraped | 10 | 276 | 253 |
| cie-a-level-maths-20-probability-and-statistics-2 | scraped | 9 | 254 | 544 |
| cie-a-level-physics-25 | scraped | 76 | 1310 | 1744 |
| cie-as-accounting-21 | no_topic_questions_on_sme | 0 | 0 | 0 |
| cie-as-biology-25 | scraped | 24 | 1011 | 772 |
| cie-as-business-23 | scraped | 19 | 293 | 16 |
| cie-as-chemistry-25 | scraped | 51 | 1075 | 855 |
| cie-as-computer-science-19 | scraped | 29 | 264 | 92 |
| cie-as-english-general-paper-21 | no_topic_questions_on_sme | 0 | 0 | 0 |
| cie-as-environmental-management-20 | scraped | 22 | 70 | 46 |
| cie-as-maths-20-mechanics | scraped | 10 | 304 | 332 |
| cie-as-maths-20-probability-and-statistics-1 | scraped | 10 | 276 | 253 |
| cie-as-maths-20-pure-1 | scraped | 22 | 726 | 366 |
| cie-as-maths-20-pure-2 | scraped | 15 | 490 | 140 |
| cie-as-physics-25 | scraped | 32 | 1005 | 1137 |
| cie-igcse-accounting-21 | scraped | 21 | 315 | 2 |
| cie-igcse-accounting-25 | no_topic_questions_on_sme | 0 | 0 | 0 |
| cie-igcse-biology-23 | scraped | 21 | 995 | 988 |
| cie-igcse-business-23 | scraped | 25 | 478 | 8 |
| cie-igcse-business-25 | scraped | 29 | 576 | 33 |
| cie-igcse-chemistry-23 | scraped | 28 | 1300 | 1177 |
| cie-igcse-computer-science-23 | scraped | 30 | 280 | 54 |
| cie-igcse-economics-20 | scraped | 39 | 612 | 31 |
| cie-igcse-economics-25 | scraped | 36 | 625 | 34 |
| cie-igcse-english-language-20 | scraped | 3 | 9 | 0 |
| cie-igcse-english-language-25 | scraped | 5 | 30 | 0 |
| cie-igcse-english-literature-21 | scraped | 15 | 95 | 0 |
| cie-igcse-environmental-management-25 | scraped | 14 | 72 | 20 |
| cie-igcse-further-maths-additional-maths-25 | scraped | 17 | 256 | 134 |
| cie-igcse-geography-20 | scraped | 21 | 483 | 431 |
| cie-igcse-geography-25 | scraped | 30 | 384 | 187 |
| cie-igcse-history-18 | scraped | 18 | 321 | 6 |
| cie-igcse-ict-21 | scraped | 23 | 313 | 32 |
| cie-igcse-maths-25-core | scraped | 44 | 1022 | 899 |
| cie-igcse-maths-25-extended | scraped | 55 | 1171 | 1113 |
| cie-igcse-maths-international-maths-23-core | scraped | 45 | 912 | 714 |
| cie-igcse-maths-international-maths-23-extended | scraped | 55 | 1159 | 1067 |
| cie-igcse-physics-23 | scraped | 24 | 1197 | 1466 |
| cie-igcse-religious-studies-23 | scraped | 21 | 72 | 0 |
| cie-igcse-science-co-ordinated-sciences-double-award-23-biology | scraped | 19 | 236 | 89 |
| cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry | scraped | 26 | 378 | 135 |
| cie-igcse-science-co-ordinated-sciences-double-award-23-physics | scraped | 21 | 320 | 174 |
| cie-igcse-science-combined-science-23-biology | scraped | 14 | 37 | 26 |
| cie-igcse-science-combined-science-23-chemistry | scraped | 20 | 41 | 17 |
| cie-igcse-science-combined-science-23-physics | scraped | 14 | 41 | 23 |
