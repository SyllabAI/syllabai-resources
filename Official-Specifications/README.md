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
