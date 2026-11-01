# GradeBoundaries — official grade boundaries corpus & pipeline (T-GRADE band)

Official Edexcel (Pearson) and Cambridge International grade boundaries /
grade thresholds, fetched from the awarding bodies' own published documents,
parsed to a canonical schema, gated, and exported as the hub-import bundle
the `syllabai-v2` Learning Hub mechanically imports for the **Grade
Boundaries** course card and page (table + trend graph + mark-to-grade
calculator).

> Status: **v1 corpus live** — 50/106 hub courses data-backed
> (all Edexcel linear IGCSE incl. Foundation/Higher tiers, all modular 4X
> courses, all IAL sciences/maths, and the seeded CIE syllabi). 56 courses
> render the honest roadmap card until their sources land. The pilot 4CH1
> corpus passes the MathsGenie golden-master parity gate 6/6 exact.

## Layout

```
GradeBoundaries/
├── README.md                     this doctrine
├── SOURCES.yaml                  source registry: families, slug matrix, licences
├── WORKLOG.md                    append-only lane worklog
├── raw/                          downloaded PDFs, byte-exact + MANIFEST.jsonl
│   ├── pearson-int-gcse-linear/<Session>.pdf
│   ├── pearson-int-gcse-modular/<Session>.pdf
│   ├── pearson-ial/<Session>.pdf
│   ├── cie/<syllabus>/<Session>.pdf
│   ├── MANIFEST.jsonl            url, final_url, sha256, bytes, fetched_at per file
│   └── fetch-missing.json        probed-but-absent sessions (absence is data)
├── parsed/                       per-document canonical JSON (source schema/1)
├── curated/
│   └── maths-genie-4ch1-golden.json   the golden-master parity fixture (G2)
├── mapping/
│   ├── hub-course-registry.snapshot.json   the hub registry this map joins
│   └── course-map.yaml           every hub slug -> boundary identity (generated)
├── scripts/                      the pipeline (run order in run_all.sh)
└── hub-import/grade-boundaries-1.0/
    └── bundle.json               the hub serving bundle (schema grade-boundaries/1.0)
```

## Pipeline

```
scripts/fetch_pearson.py   # slug-matrix probe + %PDF-verified download -> raw/ + MANIFEST
scripts/fetch_cie.py       # known-ID registry fetch -> raw/cie/
scripts/parse_pearson.py   # positional (pdfplumber x-coordinate) parser -> parsed/
scripts/parse_cie.py       # threshold-table parser (2 layout generations) -> parsed/
scripts/map_courses.py     # hub registry snapshot -> mapping/course-map.yaml
scripts/validate.py        # G1 schema/monotonic + G2 MG golden parity + G3 coverage
scripts/build_hub_import.py# course map x parsed -> hub-import/grade-boundaries-1.0/bundle.json
scripts/run_all.sh         # the whole chain, fail-loud
```

## Laws

1. **Positional parsing only for Pearson.** pdftotext renders blank
   (greyed-out) cells as whitespace, which silently SHIFTS columns on tiered
   rows (Maths A Foundation prints only grades 5–1) and R-variant rows. Every
   Pearson value is joined to its grade label by x-coordinate, never by token
   order. (The first token-order parser produced 4CH1 June 2026 9=141; the
   true value is 150 — the golden gate caught it. That is why the gate
   exists and why it must never be skipped.)
2. **Provenance law.** A series may only enter the bundle when its source PDF
   has a MANIFEST.jsonl sha256. No sha, no serve.
3. **Golden-master parity (G2).** `curated/maths-genie-4ch1-golden.json`
   (retrieved from mathsgenie.co.uk's published calculator data, trace
   1a191d55e2154601) must match at least one 4CH1 variant row exactly on
   every overlapping session, with >= 6 of 8 sessions present (G3). Mismatch
   = FAIL, the bundle does not ship.
4. **Honest absence.** Courses without data ship as empty-series entries —
   the hub renders the roadmap card, never a stub. Absent Pearson sessions
   are recorded in `raw/fetch-missing.json` (covid-era gaps and
   unpublished docs are facts, not errors).
5. **Tier discipline.** `-foundation`/`-higher` hub slugs only ever serve
   their own tier's rows; blank grade cells parse to null and render as "–".

## CIE discovery law (for the next wave)

CIE renders its threshold listing pages client-side, so crawling is not
possible today. `fetch_cie.py` runs on a verified known-ID registry; extend
`CIE_IDS` by searching for `cambridgeinternational.org Images <subject>-<code>-<session> grade-threshold-table` and verifying the download parses
(run `parse_cie.py --codes <code>` after adding). 56 CIE course rows are
awaiting exactly this mechanical extension.

## Licence note

Boundary documents are published openly by Pearson and Cambridge University
Press & Assessment for candidates and centres. They are stored here unmodified,
with source URL + sha256 per file, purely as the corpus of record for the
platform's boundaries feature — the same posture as the `Past-Papers` repo's
LICENSE-DATA practice. Original documents remain the property of the boards.
