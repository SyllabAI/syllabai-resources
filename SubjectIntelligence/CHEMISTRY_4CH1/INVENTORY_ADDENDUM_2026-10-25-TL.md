# Inventory Addendum 2 — Teaching & Learning acquisition (BL-005, 2026-10-25)

**Trace:** 1a16fa5034655795 (operator: "There are some documents in official pearson
website … what about these?" — the coursematerials Teaching-and-learning-materials
category). **Base:** manifest v1.1 (post BL-001/002). **Result:** manifest v1.2.

## What was swept

The operator-linked Pearson coursematerials page for International GCSE Chemistry 2017,
via the page's own embedded Algolia catalog (app `L639T95U5A`, index
`qualifications-uk_LIVE_master-content`, search key read from the public page HTML — same
issuing-body catalog class as BL-001; no third-party mirrors). Course filter:
`Pearson-UK:Specification-Code/igcse17-chemistry` (both path forms). Full snapshot of
record: **239 rows** — 173 Exam-materials / 60 Teaching-and-learning-materials /
4 Specification-and-sample-assessments / 2 page rows. Catalog snapshot retained at the
acquisition workspace; per-row dispositions in
`Official-Specifications/igcse-chemistry/teaching-materials.json`.

## What was placed (30 files, all identity-verified)

- **Tier-1 gap-closers (11):** official **scheme of work** (DOCX), Getting Started guide
  (28 pp), topic teaching guides — Chemical bonding (9 pp) + Chemical equilibrium (7 pp),
  **core practicals guide** (211 pp, GAP-SRC-003 texture), practical terminology guidance
  (8 pp), **command word definitions** (DOCX), exemplars with examiner commentary
  (89 pp + 26 pp), official **SAMs** (88 pp), series-structure change notice (Jan→Nov,
  assessment-identity input), linear course planner (PPTX).
- **Tier-2 supplementary (19):** maths-skills guides (9), transferable-skills mappings (2),
  cross-board/level mappings (3), lab setup guides (2), core-practical video playlist (1),
  training recording transcript (1), sciences-suite mapping guide (1).
- Verification law held: PDF magic + printed-text identity tokens / ZIP CRC + OOXML
  structure; 30/30 unique sha256; placement re-verified post-copy.

## Six-groups effect

| group | before | after |
| --- | --- | --- |
| 2. student book + teaching/support material | PARTIAL (no teaching guide) | **PRESENT** (SRC-TL-4CH1) |
| 4. examiner reports | PARTIAL | PARTIAL (unchanged — every session with a public ER is covered; residuals are publishing gaps, not acquisition misses) |
| 6. practical guidance / data sheets | PARTIAL | **PRESENT** (residual: optional standalone periodic-table/data sheet — GAP-SRC-003 LOW, evidence embedded) |

GAP-SRC-004 **RESOLVED**. Six-groups scoreboard: **5 PRESENT + 1 PARTIAL** (group 4).

## Disclosed-not-taken (209 rows — nothing silent, nothing fabricated)

- 143 exam-materials rows — QP/MS/ER class already held of record in `syllabai-pastpapers`.
- 35 teacher-training packs (Getting Ready to Teach / Welcome to Pearson / Understanding
  Assessment / Exam Insights / regional events) — available ungated as a bulk class;
  operator order required before bulk intake.
- 25 silver-gated rows (`/content/dam/secure/silver/…`, 401 anonymous) — operator queue,
  same class as the Nov-2025/June-2026 PEF residual (GAP-SRC-001).
- Admin/page/already-held rows (results-day PDF, UK-suite comparison, site pages, the
  already-held spec PDF).
