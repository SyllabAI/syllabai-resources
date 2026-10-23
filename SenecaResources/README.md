# SenecaResources — Seneca Resource Hub content for SyllabAI's subjects/courses (strict Edexcel/CIE-only)

Landing zone for Seneca Learning resources that match the courses registered in
the SyllabAI hub (`syllabai-v2` `apps/hub/content/courses.json`, 94 courses:
Edexcel IGCSE/IAL + Cambridge IGCSE/A-Level/AS). Filtered out of Seneca's full
Resource Hub harvest so downstream import work only sees material that maps to
a SyllabAI lane **and carries an explicit Edexcel or Cambridge (CIE) board tag**.

**Landed**: 2026-10-23 · base commit `840e1a5` · generator:
`seneca_vs_registry.py` (strict lanes) + `seneca_copy_to_resources.py` (sandbox
`scripts/`, Task 19 + addendum). Rebuilt once: the first landing (46,495 rows)
also carried boardless/AQA rows; the operator directed strict Edexcel/CIE-only
and the directory was rebuilt at 33,354 rows before commit.

## Provenance

| | |
|---|---|
| Source corpus | `syllabai-experimental/senecalearning/resources/captures/resource-hub-content/` (session 11 full-content harvest, snapshot 2026-10-23) |
| Source size | 70 subject files, 207,006 rows, gzip JSONL |
| Harvest | `seneca_resourcehub_full_harvest.py` (paginated `tutor-resources /api/v2/query-resources`, ≤1 req/s, ageGroup sharding) |
| Approvals | Operator content-storage approval 2026-10-23 ("We have permission to use their resources"; session-11 addendum in `senecalearning/docs/IP-AND-COPYRIGHT-NOTES.md`) + operator directives for this copy (Task 19: syllabai-lane filter; addendum: strict Edexcel/CIE-only) |
| Rows copied | **33,354 of 207,006** (16.1%) across 16 subject files; 13,141 rows excluded for carrying no Edexcel/CIE board tag |

## Filter definition

A row is copied iff all three hold:

1. its subject file is one SyllabAI subjects map to (subject synonyms: Maths /
   Mathematics / Further Maths → `Maths`; ICT → `ICT`; Environmental
   Management → `Environmental Science`; Accounting → no Seneca subject file
   exists), **and**
2. it carries a level tag in `{iGCSE, International A Level, A Level}` —
   first-match precedence `iGCSE > International A Level > A Level > GCSE`, so
   a row tagged both GCSE and iGCSE counts as iGCSE (SyllabAI has no GCSE
   lanes; GCSE-only rows are excluded), **and**
3. it carries a SyllabAI board tag:
   - `CIE` — tags intersect `{Cambridge International, CIE}` → feeds Cambridge lanes
   - `Edexcel` — tags intersect `{Edexcel, Edexcel iGCSE}`, or `{International
     A Level}` alone (IAL is Edexcel-owned) → feeds Edexcel lanes
   - rows with neither (AQA / OCR / WJEC / boardless) are **excluded**
     (13,141 rows at allowed levels).

Deliberately NOT mapped (checked, negligible/irrelevant):
`Information_Technology` (CIE A-Level IT 9626 — not offered),
`Information_and_Communication_Technology` (62 rows), `Co-ordinated_Science`
(9 iGCSE rows; double-award content properly lives in the Biology/Chemistry/
Physics files), `Science_Practicals` (1 row).

## Layout

```
SenecaResources/
├── README.md                          ← this file
├── MANIFEST-by-subject.csv            ← per-file counts, board split, sha256
├── MANIFEST-course-lanes.csv          ← all 94 courses × lane coverage + crosswalk verdict join
├── by-subject/<Subject>.jsonl.gz      ← filtered rows, original JSONL lines verbatim
└── courses/edexcel-igcse-chemistry/   ← 14-course family + family-index.json, verbatim
      (the igcse-chemistry-19 / 4CH1 pilot lane; free course = 286 sections + 1,430 EQs)
```

## Coverage (rows copied per subject file)

| subject file | copied | courseSection | examQuestion | quiz | CIE | Edexcel |
|---|---:|---:|---:|---:|---:|---:|
| Biology | 8,022 | 2,604 | 5,137 | 281 | 4,026 | 3,996 |
| Chemistry | 5,591 | 2,480 | 2,919 | 192 | 2,849 | 2,742 |
| Physics | 5,458 | 2,984 | 2,295 | 179 | 2,899 | 2,559 |
| History | 4,418 | 1,421 | 2,681 | 316 | 3,186 | 1,232 |
| English Literature | 2,764 | 1,880 | 432 | 452 | 388 | 2,376 |
| Geography | 2,370 | 959 | 1,194 | 217 | 1,139 | 1,231 |
| Business | 1,280 | 714 | 195 | 371 | 378 | 902 |
| Maths | 1,148 | 1,013 | 21 | 114 | 504 | 644 |
| ICT | 653 | 650 | 0 | 3 | 392 | 261 |
| Economics | 631 | 404 | 64 | 163 | 21 | 610 |
| Computer Science | 554 | 366 | 128 | 60 | 274 | 280 |
| English Language | 359 | 268 | 0 | 91 | 115 | 244 |
| Religious Studies | 43 | 0 | 0 | 43 | 28 | 15 |
| English | 37 | 0 | 0 | 37 | 17 | 20 |
| Science | 24 | 0 | 3 | 21 | 6 | 18 |
| Environmental Science | 2 | 0 | 0 | 2 | 2 | 0 |
| **total** | **33,354** | **15,743** | **15,069** | **2,542** | **16,224** | **17,130** |

Free/Premium split: 27,099 free / 6,255 premium (tier tag per row).

No copy exists for **Accounting** (5 SyllabAI courses): Seneca has no iGCSE/
A-Level Accounting subject file — only ACA professional content. This matches
the crosswalk's NONE verdicts.

## Row schema (unchanged from source)

Common: `id, type, title, region, timeCreated, publisher, tags {tagTypeId →
[{id, value}]}`. Type-specific `content`:

- **courseSection** — `description` (course path breadcrumb, e.g. `"English
  Language: Edexcel iGCSE - Specification B > Writing Structure"`),
  `topicNotes` (full revision body), `imageUrl`, `previewUrl`, `contentUrl`
- **examQuestion** — `questionTitleMd` (stem), `markScheme`, `generationScript`,
  `topicBreadcrumbs`
- **quiz** — `quizSummary` (PII-scrubbed at harvest)

## Course-lane manifest

`MANIFEST-course-lanes.csv` joins every registry course to its strict Seneca
lane (subject file × level tag × board class) and carries the strict crosswalk
verdict (`seneca-vs-registry-coverage.csv`). Lane counts overlap between
courses that share a lane (e.g. both CIE iGCSE Chemistry years) — the
by-subject row counts above are the authoritative unique totals.

## Reconciliation & errata

- Per-course lane counts here reconcile **exactly** with the strict
  `seneca-vs-registry-coverage.csv` (v3, regenerated 2026-10-23; verdicts
  BACKED 54 / PARTIAL 34 / NONE 6).
- **Erratum 1 (v1 crosswalk)**: harvest filenames use underscores
  (`English_Language.jsonl.gz`) while lane keys used spaces
  (`"English Language"`), silently dropping 5 multi-word subject files
  (English Language / English Literature / Computer Science / Religious
  Studies / Environmental Science) from Task 18's resource pools. Fixed via
  canonicalisation (v2); Axis-1 taxonomy counts were unaffected.
- **Revision 2 (v3, operator directive)**: strict Edexcel/CIE-only — the
  "other" class (AQA/OCR/boardless rows) no longer feeds any course lane and
  is excluded from the copy (−13,141 rows vs the first landing). Edexcel-lane
  pool columns shrank accordingly; verdict counters were unchanged (54/34/6).

## IP posture

Seneca-authored content stored under the operator's 2026-10-23 content-storage
approval. PII scrubbed at harvest; credentials/JWTs never stored. Takedown
applies: if the approval is withdrawn, delete this directory. Licence
reference from Seneca is still pending (open item since session 11). Do not
paste this content into docs, issues, PRs or commits outside this corpus
directory.

## Regeneration

```
python3 scripts/seneca_copy_to_resources.py     # sandbox: /home/z/my-project/scripts/
python3 scripts/seneca_vs_registry.py           # refreshes the coverage CSV it reconciles against
```

Idempotent: rebuilds `by-subject/` and both manifests from the source captures;
`courses/edexcel-igcse-chemistry/` is copied verbatim from the harvest.
