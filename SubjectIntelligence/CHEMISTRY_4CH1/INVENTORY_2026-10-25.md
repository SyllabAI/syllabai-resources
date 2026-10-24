# Source Inventory — 4CH1 Subject Intelligence Build (2026-10-25)

**Method:** read-only sweep, zero writes. `syllabai-resources` swept via a local blobless clone's
`git ls-tree -r` (full 82,234-path tree — the GitHub trees API truncates on this repo at ~39k
entries, a known hazard filed as LEDGER F16). `syllabai-pastpapers`, `syllabai-experimental` and
`syllabai-parser` swept via the trees API. Cross-reads: `books/CATALOG.md`,
`Official-Specifications/igcse-chemistry/spec.json`, `LICENSE-DATA.md`, `LEDGER.md`,
`graph/igcse-chemistry/specification_points.yaml` header. Machine-readable, per-source detail:
`source_manifest.yaml` (same directory; ids cited below). *(Moved from docs/ 2026-10-25, SIB-LIBRARY-003 — course-specific docs live in the course library.)*

## Verdict against the six minimum-corpus groups (requirements §5)

| # | Group | Verdict | Evidence |
|---|---|---|---|
| 1 | Official spec + validated SpecificationPoint registry | **PRESENT** | `SRC-SPEC-4CH1` (Issue 3, 58 pp, sha1 `3ad641b7…`, official Pearson URL of record) + `SRC-GRAPH-4CH1` (182 spec points verbatim-wording, 52 C-points, 4 topics, 28 subtopics, 12 practicals, 25 command words, canonical KG golden) |
| 2 | Current student book + official teaching/support material | **PARTIAL** | `SRC-BOOK-4CH1-SB1` — CATALOG row 1: `books/pearson-edexcel/international-gcse/chemistry/4ch1/student-book.pdf`, sha256 `d48020e0…`, 383 pp, 54,298,792 B, parse v3 (1,234 chunks) VALIDATED, 29-chapter doc `e6c0db50…` live. Teaching guide / scheme of work: **ABSENT** (GAP-SRC-004) |
| 3 | Complete QP/MS corpus, identities preserved | **PRESENT** | `SRC-QPMS-4CH1` — `Official-ExamQuestion/igcse-chemistry-19/`, 575 files, **16 sessions 2019-06 → 2026-06, 54 papers**: 1C ×16, 2C ×16, 1CR ×11, 2CR ×11; each paper carries `questions.md`, `mark-scheme(s).md`, cropped figure assets; parse pipeline scarred and canaried in `LEDGER.md` (F1–F19) |
| 4 | Official examiner reports | **ABSENT** | Zero examiner-report artifacts in any repo swept (GAP-SRC-001, severity HIGH). This is the single biggest hole against requirements §2A |
| 5 | Validated SME notes + question↔spec mappings | **PRESENT** | `SRC-SME-NOTES-4CH1` (420 files; the 112 DB-registered EXTERNAL_NOTES docs + assets, per-note provenance front matter per T-C09/T-C10) + `SRC-SPECLINKS-4CH1` (`spec-links/igcse-chemistry-19.json`). Additional SUPPLEMENTARY: `SRC-EXT-NOTES-4CH1` (392 files) and `SRC-PMT-4CH1` (1,189 files, Units 1–4 canonical QP/MS JSON + notes + PDF banks) |
| 6 | Practical guidance, data sheets, reference material | **PARTIAL** | 12 Core Practicals registry of record (`graph/igcse-chemistry/practicals.yaml`) + practical statements inside the spec. Standalone periodic table / data sheet: **ABSENT** as a standalone artifact (GAP-SRC-003, LOW) — evidence exists embedded in the spec PDF, the SB1 back matter (PERIODIC TABLE page) and per-question exam assets |

**Legacy group — 4CH0 (requirements §5 final line):** **ABSENT** repo-wide, zero path hits
(GAP-SRC-002, MEDIUM). `HIS` family stays OPTIONAL in `manifest.yaml` until acquired.

## What exists beyond the six groups

| Source | Class | Census | Role in the build |
|---|---|---|---|
| `SRC-SME-EXAMQ-4CH1` — `SME-ExamQuestion/igcse-chemistry-19/` | SUPPLEMENTARY | 675 files, topic-organized under the 4 spec units | question-archetype + misconception mining at topic grain (paper identity dissolved — cite `SRC-QPMS-4CH1` for official identity) |
| `SRC-LESSONS-4CH1` — `CourseLessons/.../chemistry-4ch1/` | SUPPLEMENTARY | 302 files, QA receipts per pack | teaching-sequencing evidence (PED family) pending an official scheme of work |
| `SRC-RAG-PKG-4CH1` — books-intake release asset | SUPPLEMENTARY | 824 files in zip (sha256 `9efdd9d6…` of record) | re-provisioning insurance; superseded chunk generations — do not cite for grounding |
| `SRC-ROOT-BOOK-COPIES-4CH1` — two root PDFs | SUPPLEMENTARY, provenance-pending | 2 files | pre-books-plane intake copies; adjudicate (dedupe vs `SRC-BOOK-4CH1-SB1`, or retire) before any artifact grounding |

## Gaps to acquire (nothing here blocks a start on the evidence that exists)

1. **Examiner reports** (GAP-SRC-001, HIGH) — official Pearson examiner reports for available
   4CH1 sessions. Highest-value acquisition; gates only the EXM-01..05 rows, not the build.
2. **4CH0 legacy corpus** (GAP-SRC-002, MEDIUM) — legacy spec + representative papers/books;
   must land as `LEGACY — HISTORICAL`.
3. **Teaching guide / scheme of work** (GAP-SRC-004, LOW) — recommended, not blocking.
4. **Standalone data sheet / periodic table** (GAP-SRC-003, LOW) — optional convenience intake.

## Hard constraints carried into the library

- Sources stay in their canonical repos; the library points, never copies (requirements §4).
- `SRC-GRAPH-4CH1` and `SRC-SPECLINKS-4CH1` are authoritative — SIB artifacts read them and must
  never mutate them (protocol §7; AGENT.md rules 1/3/5).
- SME notes keep their existing mappings and validation states (AGENT.md rule 4; requirements §2C).
- Coverage claims are limited by this inventory: the corpus is strong on assessment evidence
  (54 papers) and explanations (book + notes), blind on examiner sentiment and pre-2019 history.
