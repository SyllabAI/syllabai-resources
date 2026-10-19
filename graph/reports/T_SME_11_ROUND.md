# T-SME-11 — Missing-subjects round: ELA 4EA1, Maths B 4MB1, Science (Double Award) Modular 4XSD1

**Date:** 2026-09-19 · **Operator tasking:** "some subjects are missing …
download the notes, flashcards and exam questions and also organize and
process them like the rest. And you also have to download the official
specification, parse it (like the rest) and map it to the resources."

## 1. Catalog diff (live SME sitemaps vs repo registry, 2026-09-19)

Live Edexcel IGCSE/IAL course roots: **49**. Repo had **39**. The 10 missing
courses, in 3 subject families:

| Family | SME lanes | Notes pages | Topic questions | Flashcards |
|---|---|---|---|---|
| English Language A (4EA1, 2016) | paper-1, paper-2, paper-3 (module courses) | 68 | paper-1: 100 q / paper-2: 65 q / paper-3: none | 6 decks / 298 cards; paper-3 none |
| Maths B (4MB1, 2016) | maths-b-16 | 200 | none (shell page, 0 published sets) | 62 decks / 1,082 cards |
| Science (Double Award) (Modular) (4XSD1, 2024) | 6 unit lanes | 282 | none (0 published sets on all 6) | none (course-level flag `has_published_flashcard_sets: false`) |

Every gap above is SME-side (census recorded in
`scripts/sme_catalog_work/availability.json`), not scraper-side; nothing was
synthesized. Tools: `sme_catalog_enum_v2.py`, `sme_availability_census.py`
(workspace scripts; evidence JSONs committed under
`scripts/t_spec_10_work/sme11/` — see §6).

## 2. What was added

### 2.1 Notes — `SME-RevisionNotes/` (39 → 49 courses, 3,195 → 3,743 pages)
`sme_notes_scrape.py --courses <10>` with a discover cache rebuilt for 49
courses (`build_notes_discover_cache.py` from the live sitemap catalog).
Zero fetch failures; 1,180 new assets; SME TipTap `revisionNote` docs parse
unchanged on the new site. Registry manifest + README regenerated (49
courses).

### 2.2 Exam questions — `SME-ExamQuestion/` (39 → 49 lanes, 41 scraped)
SME's frontend changed since Sep-17: topic questions are no longer compiled
per topic on one leaf page; each exam-session question **set** is its own
page. New committed scraper `scripts/sme_examq_setpage_scrape.py` reproduces
the corpus conventions exactly (same schema `syllabai.sme-exam-questions/1.1`,
same part atomization incl. `source_paper` provenance, `spec_point_ids`,
solutions) with per-set orchestration; `question_sets[]` carries the session
sets and questions[] flatten with per-question `set_slug` (schema already
supported it).

- `igcse-english-language-a-16-paper-1…`: 2 topics, 29 session sets,
  **100 questions / 1,980 marks**, 0 missing, 0 asset failures
- `igcse-english-language-a-16-paper-2…`: 2 topics, 33 session sets,
  **65 questions / 1,950 marks**, 0 missing, 0 asset failures
- The 8 lanes without SME topic questions got lane folders with v1.1
  manifests carrying `status_note: no_topic_questions_on_sme` + zero totals
  (`create_no_tq_lanes.py`).

`scripts/sme_examq_scrape.py` was generalized minimally for reuse (URL-shape
tail match, label from the COURSE registry, conditional notes pointer);
chemistry behavior unchanged (not re-run). The missing multi-course driver
`sme_examq_courses.py` (referenced by the registry but never committed) is
superseded by `t_sme_11_registry_update.py`.

### 2.3 Flashcards — `SME-Flashcards/` (34 → 37 courses with decks)
REGISTRY extended (+3 with paths, +7 recorded `missing_on_sme`); 68 decks /
1,380 cards scraped, 0 failures (maths-b 62 decks/1,082 cards; ELA 6
decks/298 cards). `map_flashcards.py`: 61 maths-b cards inherit spec links
from their notes; ELA cards pending (their course maps are largely pending —
see §3).

### 2.4 Official specifications — `Official-Specifications/` (20 → 23 quals)
- 4EA1 + 4MB1: discovered from SME course-root
  `courseExamSpecificationPdfLink` (cache extended to all 49 lanes).
- 4XSD1: SME leaves the field null on all six modular unit pages (as it did
  for the 2017 linear course); URL read off the Pearson qualification page
  `science-double-award-2024-modular.html` →
  `international-gcse-science-da-modular-specification.pdf`, recorded in the
  downloader's MANUAL map.
- All validated (PDF magic, page counts, spec-code probe, sha1):
  4EA1 46p issue 7, 4MB1 50p issue 1, 4XSD1 96p issue 2.
  Manifest: 23 qualifications, **49/49 courses covered, 0 missing**.

### 2.5 Parsing — `Official-Specifications/parsed/<3 new quals>/`
`spec_parser.py` FAMILY extended; canonical bundles via `build_canonical.py`
(spec_points/topics/practicals/AOs/command_words + parse_report):

- `igcse-science-double-award-modular` → **code_column** (same layout as the
  single-science modular specs): 412 raw → **411 points** after one recorded
  parse repair (`t_sme_11_parse_repair.py`: preamble "over 3.4 million
  students…" misparsed as statement 3.4; genuine numbering starts page 17).
  0 flags; 25 practicals; per-science prefixes (Biology-/Chemistry-/Physics-).
- `igcse-maths-b` → **further_maths** family (numbered sections, lettered
  statements, Notes column): **98 points**, 2 notation flags (math-fragment
  assembly on f(x)/ds-dt rows), 10 topics.
- `igcse-english-language-a` → **english_lang_a** (generalized
  `parse_english_lit`: region auto-detection, `Section/Assignment X:`-colon
  strands, author column x≈374): **26 points** (AO strands + anthology
  set-text rows + skills bullets), 3 components.

Existing quals were NOT regenerated in this environment (pymupdf version
drift reflows span gaps); only the three new parse dirs + shared reports are
added. `sme_spcpt_verify.py` `course_registry` extended with
`igcse-english-language-a` (suffix-keyed registry, like english-literature).

## 3. Mapping (initial tiered auto-join, honest tails)

`sme_spcpt_harvest_all.py` built `spec_point_index.json` for all 10 lanes
(ELA parts 100% index-covered; 0 fetch failures). `map_spec_points.py`
(+ `t_sme_11_apply.py` writing the resolution sidecars and part codes):

| Lane | ids | resolved | unresolved |
|---|---|---|---|
| ELA paper-1 / paper-2 / paper-3 | 150 / 97 / 24 | 26 / 12 / 1 | 124 / 85 / 23 |
| maths-b-16 | 215 | 32 | 183 |
| SDA-mod bio-u1 / bio-u2 | 59 / 99 | 50 / 96 | 9 / 3 |
| SDA-mod chem-u1 / chem-u2 | 77 / 43 | 43 / 13 | 34 / 30 |
| SDA-mod phys-u1 / phys-u2 | 64 / 76 | 54 / 66 | 10 / 10 |

Resolved rows are T1/T2/T3 verbatim-or-near registry joins (SDA units,
definitions present) and unflagged S1 name matches (name-only regimes);
**flagged (S2 ambiguous / T4 fuzzy) and weak joins stay unresolved with
recorded reasons** — the no-guess discipline. 393 resolved / 511 honest
pendings overall; part-level codes written for the ELA question parts.

## 4. Learner impact + gates

- `build_learner_spec_links.py --all`: **46,780 items** (+1,279), 37,128
  coded; parts stay 100% coded corpus-wide.
- `sme_spcpt_verify.py`: **ALL GATES PASSED** (49 courses; uncoded tail
  remains allowlisted by the documented no-guess rule).
- `sme_spcpt_corpus_gap_report.py` / sibling machinery untouched (new lanes
  have no sibling-history yet).

## 5. Honest gaps (all SME-side, none blocking)

1. ELA paper-3, maths-b, SDA-modular ×6: no topic questions on SME.
2. ELA paper-3 + SDA-modular ×6: no flashcards on SME.
3. ELA course maps are largely pending: 4EA1's registry is
   component/skills-shaped and its SME tags are name-only — closing these
   needs an operator reasoning round (T-SPEC-style) like the humanities
   lanes, not more scraping.
4. maths-b pendings: SME maths tags are name-only; the T-SPEC-6 pattern
   (page-context joins) applies in a later verdict round.

## 6. Artifacts

- Scrapers: `scripts/sme_examq_setpage_scrape.py` (new),
  `scripts/t_sme_11_apply.py` (new), `scripts/t_sme_11_registry_update.py`
  (new), `scripts/t_sme_11_parse_repair.py` (new),
  `scripts/create_no_tq_lanes.py` (new); generalized
  `sme_examq_scrape.py`, `sme_flashcards_scrape.py`, `sme_spec_download.py`,
  `spec_parser.py`, `sme_spcpt_verify.py`.
- Evidence (workspace): `scripts/t_spec_10_work/sme11/` — catalog_v2.json,
  availability.json, spec-discovery notes.
