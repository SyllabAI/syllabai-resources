# Source Inventory ADDENDUM — BL-001/BL-002 executed (2026-10-25, later same day)

**Operator order:** "acquire examiner reports + 4CH0 corpus" (zai-web session
`web-1f157e25-0ed7-4f18-8956-3b2a993bc646`, trace `1a16f5bd6146b01d`) — the two acquisitions
this inventory queued as gaps 1 + 2. Companion wave report (assessment archive):
`SyllabAI/syllabai-pastpapers@docs/ER-ACQUISITION-2026-10-25.md` @ `3632b0e6`.

## What landed

| Gap | Was | Now |
| --- | --- | --- |
| 1. Examiner reports (GAP-SRC-001, HIGH) | ABSENT repo-wide | **ACQUIRED** — 24 official 4CH1 ERs (8/16 held sessions: 2019-06, 2022-06, 2023-06, 2023-11, 2024-06, 2024-11, 2025-06) + 34 official 4CH0 legacy ERs (13/16 sessions) in `syllabai-pastpapers`, Pearson's own public CDN, printed-PDF-text identity verified, per-file sha256 in each paper manifest → `SRC-ER-4CH1`, `SRC-ER-4CH0-LEGACY` |
| 2. Legacy 4CH0 corpus (GAP-SRC-002, MEDIUM) | "ABSENT repo-wide, zero path hits" | **PRESENT** — correction: the QP/MS archive was already complete in `syllabai-pastpapers` (40 paper dirs / 16 sessions 2011-06..2019-01, first-hand re-verified); this run added 34 legacy ERs + official legacy spec corpus (`Issue 3` spec 32 pp / `Issue 5` spec+SAMs 118 pp / 2009 SAMs 70 pp) in `Official-Specifications/igcse-chemistry-legacy-4ch0/` → `SRC-LEGACY-SPEC-4CH0` |

## Inventory correction of record (honesty law)

The v1.0 inventory's "4CH0: zero path hits repo-wide" was **wrong**: the sweep missed the
lowercase `4ch0/` subtree of `syllabai-pastpapers` (case-sensitive matching against the
mixed-case tree; the tree sweep itself predates the API-truncation discipline that the
resources sweep used). Corrected by a first-hand session-by-session walk of the chemistry
subtree @ `3632b0e6`. `source_manifest.yaml` v1.1 carries the correction in
`manifest_history` + `legacy_inventory.detail`. Nothing else in the v1.0 census is affected:
the examiner-report absence claim was true at inventory time (verified again this run — the
only pre-existing ERs were the 2023-06 quartet from wave 8, held with manifests).

## Residual disclosures (requirement: never fabricate)

- **No public ER exists** (zero rows in Pearson's own catalog) for 4CH1 sessions 2020-01,
  2020-11, 2021-01, 2021-11, 2022-01, 2023-01 (COVID-era + January/November international
  series; January IGCSE discontinued after Jan 2023 per the archive's own docs) and for 4CH0
  sessions 2014-01, 2015-06, 2016-01 (name probes return Pearson's identical HTML soft-404 —
  not published). 2021-06 has no ER by construction (cancelled series).
- **Silver-tier (401 anonymous), operator-side queue:** 4CH1 Nov-2025 (×2) + June-2026 (×4)
  PEFs — catalog rows of record exist; anonymous fetch refused.
- **Placed-NOT:** 4CH0 2018-06 1CR/2CR ERs (bytes verified, sha256s of record in the wave
  report) — their QP/MS dirs were never ingested; the no-speculative-folders law (pastpapers
  README §21) forbids creating ER-only paper dirs. Placing them belongs to a future CR-ingest
  wave.
- **Cross-check item (no action):** 4CH1 2023-06 ERs held from wave 8 (Paperlords) left
  byte-untouched; Pearson's own PEF URLs for the same session are filed in the wave report for
  a future F15-class byte adjudication (held-vs-held, different packaging — operator ruling
  required by precedent).

## Six-groups check after this run

| # | Group | Was | Now |
| --- | --- | --- | --- |
| 1 | spec + registry | PRESENT | PRESENT |
| 2 | student book + teaching material | PARTIAL | PARTIAL (teaching guide still absent — GAP-SRC-004) |
| 3 | QP/MS corpus | PRESENT | PRESENT |
| 4 | examiner reports | ABSENT | **PARTIAL → every session with a public ER covered; residuals disclosed** |
| 5 | SME notes + mappings | PRESENT | PRESENT |
| 6 | practicals/data sheets | PARTIAL | PARTIAL (GAP-SRC-003 unchanged) |
| legacy | 4CH0 | ABSENT | **PRESENT (LEGACY — HISTORICAL)** |

The build can now ground the EXM family on real examiner sentiment and unlock HIS — the
remaining pre-generation runs are unchanged: BL-003 (notebook provisioning) → CUR-01..CUR-08.
