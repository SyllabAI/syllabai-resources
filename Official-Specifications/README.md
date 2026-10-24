# Official Specifications (Pearson Edexcel)

Official exam-board specification PDFs for every qualification behind the 39 SME courses in `../SME-ExamQuestion/` and `../SME-RevisionNotes/`. 20 qualifications, 39/39 courses covered.

## How these were found

- **36/39 courses**: SME course landing pages expose `props.pageProps.courseExamSpecificationPdfLink` (rendered as the "Exam specification" card) pointing at the official PDF on `qualifications.pearson.com`.
- **3 Science Double Award courses**: SME leaves the link `null` (no card); the 4SD0 PDF came from Pearson's own qualification page (`edexcel-international-gcses/international-gcse-science-double-award-2017.html`).
- **1 stale link**: SME's Business URL now serves the Pearson CDN's HTTP-200 HTML 404 page; replaced with the current URL from Pearson's `business-2017.html` qualification page (recorded in `spec.json` as `sme_source_url`).

## Layout

```
Official-Specifications/
  manifest.json                      # schema 1.0: provenance + per-qualification records
  <qualification-slug>/              # one dir per official qualification
    <original-pearson-filename>.pdf  # unmodified download
    spec.json                        # source URL, sha1, bytes, pages, cover_code,
                                     # spec_codes, issue, sme_courses, fetched_utc
```

Qualification slugs group SME courses that share one official spec (e.g. `ial-maths` covers all ten `ial-maths-20-*` units plus `ial-further-maths-18-further-pure-1` — one 2018 IAL Maths specification spanning WMA/WFM/WPM/WST/WDM units).

## Qualification inventory

| qualification | cover code(s) | issue | pages | SME courses |
|---|---|---|---|---|
| ial-biology | XBI11/YBI11 | 2 | 78 | 1 |
| ial-chemistry | XCH11/YCH11 | 1 | 108 | 1 |
| ial-maths | XMA01/XFM01/XPM01/YMA01/YFM01/YPM01 | 3 | 99 | 10 |
| ial-physics | XPH11/YPH11 | 3 | 87 | 1 |
| igcse-accounting | 4AC1 | 1 | 50 | 2 |
| igcse-biology | 4BI1 | 3 | 56 | 1 |
| igcse-biology-modular | 4XBI1 | 2 | 56 | 2 |
| igcse-business | 4BS1 | 1 | 41 | 1 |
| igcse-chemistry | 4CH1 | 3 | 58 | 1 |
| igcse-chemistry-modular | 4XCH1 | 2 | 58 | 2 |
| igcse-economics | 4XEC1 | 1 | 54 | 1 |
| igcse-english-literature | 4ET1 | 2 | 46 | 1 |
| igcse-further-maths | 4PM1 | 1 | 52 | 1 |
| igcse-geography | 4GE1 | 4 | 57 | 1 |
| igcse-ict | 4IT1 | 2 | 47 | 1 |
| igcse-maths-a | 4MA1 | 2 | 70 | 2 |
| igcse-maths-a-modular | 4XMAF/4XMAH | 2 | 66 | 4 |
| igcse-physics | 4PH1 | 4 | 62 | 1 |
| igcse-physics-modular | 4XPH1 | 2 | 64 | 2 |
| igcse-science-double-award | 4SD0 | 4 | 96 | 3 |

`cover_code` is read from the PDF cover (authoritative qualification code); `spec_codes` in `spec.json` additionally lists every unit/qualification code found in the document text (e.g. the IAL W-unit codes WCH11–16, or the 4SD0 cross-references inside the individual science specs).

## Notes

- IAL 2018 qualifications pair an International Advanced Subsidiary code (`X…`) with an International Advanced Level code (`Y…`); the `W…` codes are unit codes for the international-only exam route. Modular 2024 International GCSEs carry `4X…` codes (`4XMAF`/`4XMAH` = Foundation/Higher tiers).
- The `igcse-chemistry` copy is sha1-identical to the legacy `../international-gcse-chemistry-2017-specification.pdf` used for the 4CH1 spec-point mapping.
- Verification: `scripts/sme_spec_verify.py` (G1–G5: schema totals, sha1/page integrity, 39-course coverage with no duplicates, codes present, legacy-copy identity) — ALL PASS.
- These are official Pearson Edexcel documents, downloaded from Pearson's public CDN; provenance per file in `spec.json`.

## Legacy qualification — 4CH0 (SIB BL-002, 2026-10-25, trace 1a16f5bd6146b01d)

`igcse-chemistry-legacy-4ch0/` — official documents for the **legacy A*-G Edexcel International
GCSE Chemistry (4CH0)** qualification (final sessions January 2019), acquired for the Subject
Intelligence build's HIS family (longitudinal comparison). Three unmodified Pearson-CDN
downloads + per-file provenance in the directory's own `spec.json`:

| file | what | pages | sha1 |
| --- | --- | --- | --- |
| `IGCSE Chemistry (4CH0) Issue 3.pdf` | legacy specification, Issue 3 | 32 | `1ca8219b0207c20d7a0c21e7fe3da9a6ba9bec94` |
| `INT_GCSE_CHEM_SPECSAMS_ISS5_comb.PDF` | specification + sample assessment material, Issue 5 combined | 118 | `51e6505a41278aeb351653ecca9bc4fb137f2bbf` |
| `IGCSE2009_Chemistry_SAMs.pdf` | sample assessment materials booklet (2009 spec) | 70 | `0853b039d40c73dadef57bb8ef52b701a0cf9d21` |

**Scope note:** this directory is deliberately **outside `manifest.json`** — that manifest and
its `sme_spec_verify.py` gates cover the live qualifications behind the 39 SME courses, and 4CH0
backs no SME course. The legacy dir is self-documented (spec.json carries source URLs, sha1s,
byte counts, page counts, cover codes, fetched_utc); everything in it is classified
LEGACY — HISTORICAL in the SIB library (`SubjectIntelligence/CHEMISTRY_4CH1/source_manifest.yaml`
v1.1, `SRC-LEGACY-SPEC-4CH0`) and must never ground current-curriculum artifacts. Companion
legacy assessment material (complete 4CH0 QP/MS archive + 34 examiner reports) lives in
`SyllabAI/syllabai-pastpapers@past-papers/pearson-edexcel/international-gcse/chemistry/4ch0/`
(wave report: that repo's `docs/ER-ACQUISITION-2026-10-25.md`).

## Teaching & learning materials — 4CH1 (SIB BL-005, 2026-10-25, trace 1a16fa5034655795)

`igcse-chemistry/teaching-and-learning-materials/` + two root files — official Pearson
teaching, practical and assessment-support documents for the **live International GCSE
Chemistry (4CH1)** specification, acquired for the Subject Intelligence build's six-group
corpus (teaching/sequencing + practical-guidance + command-word + exemplar classes).
30 unmodified Pearson-CDN downloads; per-file provenance (source URL, sha256, bytes,
pages, identity evidence, tier, SI classification) in `igcse-chemistry/teaching-materials.json`.

Tier-1 gap-closers (verified by printed-text / OOXML-structure identity):

| file | what |
| --- | --- |
| `international-gcse-chemistry-scheme-of-work.docx` | official **scheme of work** (topic sequencing evidence) |
| `gstt-int-gcse-chemistry.pdf` | Getting Started teaching guide |
| `Chemical-bonding-FINAL.pdf` / `Chemical-equilibrium-FINAL.pdf` | topic teaching guides |
| `biology-chemistry-physics-core-practical-guide.pdf` | **core practicals guide** (practical-guidance group) |
| `practical-terminology-in-int-gcse-science.pdf` | practical terminology guidance |
| `int-gcse-command-words.docx` | **command word definitions** |
| 2 exemplar-with-commentary PDFs | examiner-commented exemplar responses |
| `international-gcse-Chemistry-2017-SAM.pdf` | official sample assessment materials (root) |
| `notice-of-changes-january-and-november-series.pdf` | series-structure change notice (root; assessment identity) |
| `international-gcse-chemistry-linear-course-planner.pptx` | linear course planner |

Tier-2 supplementary (19 files): maths-skills guides (9), transferable-skills mappings (2),
cross-board/level mappings (3), lab setup guides (2), core-practical video playlist (1),
training recording transcript (1), sciences-suite mapping guide (1).

**Scope note:** deliberately **outside `manifest.json`** (same law as the legacy 4CH0 dir) —
these documents back the SIB library, not the 39-SME-course spec manifest. Discovery: the
coursematerials page's own Algolia index (catalog snapshot 239 rows); 30 rows placed, 209
rows disclosed-not-taken in `teaching-materials.json` (35 teacher-training packs available
ungated as a bulk class awaiting operator order, 25 silver-gated 401 rows = operator queue,
143 exam-material rows already held of record in `syllabai-pastpapers`, plus admin/page/
already-held rows). SI registry: `SubjectIntelligence/CHEMISTRY_4CH1/source_manifest.yaml`
v1.2 (`SRC-TL-4CH1`, `SRC-SAMS-4CH1`).

## CIE qualifications (T-SPECS-CIE-1, 2026-10-18)

Official Cambridge International Education syllabus PDFs for every qualification behind the 44 `cie-*` SME courses in `../SME-ExamQuestion/` and `../SME-RevisionNotes/`. 33 qualifications — one per unique syllabus edition — 44/44 courses covered. Each `<qualification>/spec.json` carries the source URL, edition window, SHA-1, byte size, page count, cover code and the SME courses it covers; `manifest.json` totals now span both boards.

### How these were found

- **40 lanes → 29 PDFs**: SME course landing pages expose `props.pageProps.courseExamSpecificationPdfLink` pointing at the official PDF on `cambridgeinternational.org` — the same discovery mechanism as the Edexcel side.
- **3 lanes → 3 PDFs**: SME leaves the card null on the three `-25` IGCSE lanes (`igcse-accounting-25`, `igcse-english-language-25`, `igcse-environmental-management-25`); the newest published edition was taken from the official Cambridge qualification page (the convention SME itself uses on `cie-igcse-business-25` / `cie-igcse-economics-25`).
- **1 lane → 1 PDF**: stale card — `cie-as-english-general-paper-21` points at the retired 2022-2024 edition (HTTP 404); substituted with the newest published edition (2028-2030), the dead link preserved as `sme_source_url` (the Edexcel stale-business-link precedent).

Qualification slugs carry the edition window (`<subject>-<window>`); one subject attached to different editions registers as separate qualifications, mirroring how SME maintains edition-specific course lanes.

### Qualification inventory (CIE)

| qualification | cover code | edition | pages | SME courses |
|---|---|---|---|---|
| cie-a-level-accounting-2023-2025 | 9706 | 2023-2025 | 40 | 1 |
| cie-a-level-biology-2025-2027 | 9700 | 2025-2027 | 73 | 1 |
| cie-a-level-business-2023-2025 | 9609 | 2023-2025 | 46 | 1 |
| cie-a-level-chemistry-2025-2027 | 9701 | 2025-2027 | 98 | 1 |
| cie-a-level-computer-science-2024-2025 | 9618 | 2024-2025 | 48 | 1 |
| cie-a-level-economics-2023-2025 | 9708 | 2023-2025 | 43 | 1 |
| cie-a-level-maths-2023-2025 | 9709 | 2023-2025 | 59 | 5 |
| cie-a-level-physics-2025-2027 | 9702 | 2025-2027 | 68 | 1 |
| cie-as-english-general-paper-2028-2030 | 8021 | 2028-2030 | 25 | 1 |
| cie-as-environmental-management-2025-2027 | 8291 | 2025-2027 | 49 | 1 |
| cie-igcse-accounting-2023-2025 | 0452 | 2023-2025 | 26 | 1 |
| cie-igcse-accounting-2027-2029 | 0452 | 2027-2029 | 30 | 1 |
| cie-igcse-biology-2023-2025 | 0610 | 2023-2025 | 61 | 1 |
| cie-igcse-business-2023-2025 | 0450 | 2023-2025 | 30 | 1 |
| cie-igcse-business-2027-2029 | 0264 | 2027-2029 | 33 | 1 |
| cie-igcse-chemistry-2023-2025 | 0620 | 2023-2025 | 59 | 1 |
| cie-igcse-computer-science-2023-2025 | 0478 | 2023-2025 | 55 | 1 |
| cie-igcse-economics-2023-2025 | 0455 | 2023-2025 | 30 | 1 |
| cie-igcse-economics-2027-2029 | 0455 | 2027-2029 | 37 | 1 |
| cie-igcse-english-language-2024-2026 | 0500 | 2024-2026 | 36 | 1 |
| cie-igcse-english-language-2027-2029 | 0500 | 2027-2029 | 42 | 1 |
| cie-igcse-english-literature-2023-2025 | 0475 | 2023-2025 | 35 | 1 |
| cie-igcse-environmental-management-2027-2029 | 0680 | 2027-2029 | 50 | 1 |
| cie-igcse-further-maths-additional-maths-2025-2027 | 0606 | 2025-2027 | 31 | 1 |
| cie-igcse-geography-2025-2026 | 0460 | 2025-2026 | 44 | 2 |
| cie-igcse-history-2024-2026 | 0470 | 2024-2026 | 44 | 1 |
| cie-igcse-ict-2023-2025 | 0417 | 2023-2025 | 43 | 1 |
| cie-igcse-maths-2025-2027 | 0580 | 2025-2027 | 71 | 2 |
| cie-igcse-maths-international-maths-2025-2027 | 0607 | 2025-2027 | 72 | 2 |
| cie-igcse-physics-2023-2025 | 0625 | 2023-2025 | 61 | 1 |
| cie-igcse-religious-studies-2025-2027 | 0490 | 2025-2027 | 45 | 1 |
| cie-igcse-science-co-ordinated-sciences-double-award-2025-2027 | 0973 | 2025-2027 | 108 | 3 |
| cie-igcse-science-combined-science-2023-2024 | 0653 | 2023-2024 | 65 | 3 |

Code observations: the 2027-2029 redeveloped IGCSE Business syllabus carries the renumbered code **0264**; Co-ordinated Sciences (Double Award) 2025-2027 is **0973** (the 9-1 redeveloped line). The lane year tags are SME course tags, not syllabus codes.
