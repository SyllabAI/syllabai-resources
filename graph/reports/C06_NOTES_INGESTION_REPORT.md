# C06 Notes Ingestion — SME-RevisionNotes/ial-chemistry-17 (T-C06 kickoff)

**Status: CONVERSION COMPLETE + INGESTION STAGED (payload frozen; DB import is operator-executed).**
Date: 2026-09-18. Directive: "Start notes ingestion. And use notes from
`SME-RevisionNotes/ial-chemistry-17`" — the T-C06 kickoff, first tranche through the
canonical notes pipeline.

## 0. What this tranche is

The operator's Save My Exams scraper output for **Edexcel IAL Chemistry (2017
specification)**: schema `syllabai.sme-revision-notes-course/1.0`, 196 note pages
(md + sidecar json pairs under `notes/<section>/<topic>/<leaf>.`), `assets/` (633
files on disk; manifest counts 634 scraped with `asset_failures: 1` — the delta
correlates to the single remote-URL figure ref found in lint), 262 provider
spec-point ids across notes. Course slug `ial-chemistry-17`; curriculum target
`IAL-CHEM-2018` (the V6-seeded ACTIVE curriculum version). Pinned at resources
`69c81cc0f744` — zero drift between pin and this commit's parent.

## 1. Provenance chain (all commits in this change set)

| Artifact | Where | Commit |
|---|---|---|
| `SmeRevisionNoteParser` engine `sme-revision-note/1.0.0` + CLI `SME` mode + 10 tests | syllabai-parser | `14519dc` |
| V29 migration + `Document.Kind` widening + entity `validation_state` + 3 tests | syllabai-core | `9ac219d` |
| This report + lint report + canonical payload + tooling | syllabai-resources | this commit |
| Corpus (input, unchanged) | syllabai-resources | `69c81cc0f744` (parent) |

## 2. Lint (deterministic, `scripts/c06_lint_corpus.py`)

**Verdict PASS** — 196/196 notes, 0 hard findings, 256 warnings (all recorded
provider-corpus facts, none blocking). Full per-note detail:
`SME-RevisionNotes/ial-chemistry-17/reports/C06_LINT_REPORT.json`.

| Check family | Result |
|---|---|
| Front-matter schema (8 required keys, `rn_` id, ISO-8601 `updated_at`) | clean 196/196 |
| Identity agreement md ↔ sidecar ↔ manifest (note_id, title, path leaf) | clean 196/196 |
| H1 = title, exactly one per note | clean 196/196 |
| Spec-point ids ↔ body `> **Spec point**` markers | **262 ↔ 262 exact** |
| Local asset refs resolve to `assets/` | clean (1 remote CDN ref kept verbatim, warned — the `asset_failures: 1` correlate) |
| `<sub>/<sup>` tag balance | clean 196/196 |
| Duplicate note_id / duplicate content fingerprints | none |

Warnings recorded (not blocking): 207 heading-level skips (provider `##`→`####`
structure, preserved verbatim), 36 notes with provider LaTeX, 6 with unicode
sub/sup chars, 5 with formula-adjacent bare digits, 77 figures without alt text,
1 remote figure ref.

## 3. Conversion design (`SmeRevisionNoteParser`, syllabai-parser)

- **Identity**: `CanonicalIdentity` — SHA-256 of the note .md file + engine
  `sme-revision-note` + version `1.0.0` → deterministic documentId. The sidecar
  never touches identity. This matches the core-side derivation check
  (`CanonicalDocumentValidator`) and the DB dedup spine (`uq_documents_checksum`).
- **Elements**: structural Markdown decoded — headings → `HEADING` blocks,
  bullets → `LIST_ITEM`, images → `FigureElement` (text = full original ref,
  sourceName, format, alt), pipe tables → `TableElement` (separator rows
  dropped), blockquote lines (incl. `> **Spec point**`) → `PARAGRAPH` blocks,
  plain prose soft-joined per blank line. Element ids `e%06d` sequential across
  ALL element types in emission order; reading order = emission order.
- **Sections**: every heading opens one (`s%03d`); ALL element types attach —
  figures/tables included (deliberately broader than the GLM adapter's
  text-only sections, which notes need for spec-region provenance).
- **Verbatim posture (v1)**: inline markup (`**`, backticks, `<sub>/<sup>`,
  provider `$...$` LaTeX) preserved byte-exact;
  `notationNormalization=verbatim-v1-no-notation-rewrites` recorded per note.
  The registered T-C06 "LaTeX→HTML sub/sup normalization" step is deferred with
  reason: the LaTeX present is Wiris-rendered chemistry inside math fences —
  applying sub/sup rewriting inside `$...$` would corrupt provider LaTeX, and
  any broader notation map (arrows, fracs) rewrites chemistry wording, which is
  operator-ratified work, not an adapter decision.
- **Sidecar enrichment** (provenance-only, pairing-guarded): authors, reviewers,
  section/topic/subtopic display titles, stats, `is_ai_assisted`, course slug;
  fails closed on schema mismatch or note_id disagreement (wrong-file guard).
- **Provenance params per note**: noteId, notePath, noteUpdatedAt, guidedStudy,
  specPointIds (262 total), specPointCodes, specPointMarkerCount, inlineMathCount,
  figureCount, pageBoundaries=none-in-source, notationNormalization, noteFile.

## 4. Verification performed

1. **Parser unit suite**: 154/154 green (10 new tests) on JDK 25 — deterministic
   double-parse byte-identity, pinned cross-language identity vector, body-flow
   decomposition, verbatim checks, sections, sidecar guards, fail-closed matrix.
2. **Core unit suite**: 673/0/1 green (3 new tests: enum roles, EXTERNAL_NOTES
   lands SUGGESTED, legacy-constructor default).
3. **Batch conversion**: all 196 notes converted TWICE with pinned
   `extractedAt=2026-09-18T00:00:00Z` → **run1 ≡ run2 byte-identical** per file.
4. **Cross-language identity**: Python re-derived the documentId for **all 196**
   notes from the identity formula — 196/196 match the Java-emitted ids (the
   conformance property `CanonicalIdentity` documents, verified batch-wide).
5. **Uniqueness**: 196/196 documentIds distinct (dedup spine safe).

## 5. Payload census (committed at `SME-RevisionNotes/ial-chemistry-17/canonical/`)

| Metric | Value |
|---|---|
| Canonical documents | 196 (schema 1.0, JSON, 5.8 MB) |
| Text blocks | 11,359 |
| Figures | 564 |
| Tables | 30 |
| Sections | 1,420 |
| Integrity spine | `BUNDLE_MANIFEST.json` — per-note source-md sha256, documentId, canonical sha256, counts |

## 6. Core readiness (V29)

`V29__content_corpus_kinds.sql` (additive + reversible, reverse statements in
header): `documents.kind` += `TEXTBOOK` / `EXTERNAL_NOTES` /
`EXTERNAL_QUESTIONS`; `documents.validation_state` added —
`VARCHAR(20) NOT NULL DEFAULT 'SUGGESTED'` with the V20 four-state CHECK —
**corpus imports are born SUGGESTED and nothing serves without human
validation** (write-side state today: no serving predicate reads it yet; the
T-C07/T-C14 predicates remain paper-level joins, so note chunks are fail-closed
unservable regardless — exactly the honest boundary until a serving-eligible
notes surface is built); `questions.provenance` += `EXTERNAL_BANK`.

## 7. Ingestion runbook (staged — NOT executed in this change set)

The DB import is operator-executed (TEACHER/ADMIN credential required; none
supplied to this session). Committed tooling:

```bash
# 1. verify payload integrity + dry run (no network):
python3 scripts/c06_ingest_notes.py SME-RevisionNotes/ial-chemistry-17/canonical

# 2. execute:
CORE_BASE_URL=https://<render-host> INGEST_TOKEN=<teacher-jwt> \
  python3 scripts/c06_ingest_notes.py SME-RevisionNotes/ial-chemistry-17/canonical --execute
```

Expected outcome: 196 created (0 duplicates on first run), `documents.kind =
EXTERNAL_NOTES`, `validation_state = SUGGESTED`, deterministic chunks land
un-embedded (embedding is the separate, re-runnable operation — the existing
per-document embed endpoint or the EmbedBackfill runner covers it when
authorized; model registry discipline unchanged). Idempotent: re-runs return
`duplicate=true` by checksum. `INGESTION_RUN_LOG.json` records every response.

## 8. Honest boundaries — what this change set does NOT claim

1. **No DB rows created.** The payload is staged; production import waits for
   operator execution of §7 (same credential boundary as the live LLM
   benchmark and the embed backfill dispatch).
2. **§8(d) snap v2 is NOT unlocked by this tranche.** The 209-row chunk→SP
   substrate is over the 4CH1 notes corpus; its scoreability needs the 4CH1
   notes ingested and the `c13-chunk-convention-1` chunk identity reproduced —
   that alignment requirement is recorded on the T-C13 row and is the next
   notes-ingestion tranche, not this one.
3. **Remaining T-C06 deliverables** (unchanged, still open on the lane):
   SPEC_POINT node type with namespaced codes; F-168 mapping-provenance
   columns; resolution of the 262 provider `spcpt_*` ids to official IAL
   spec-point codes (PROVIDER-tier mapping facts, human-validated before
   authoritative per §7); the CMC-v1.0 converter for the operator's manual
   4CH1 corpus; serving-eligible notes surface (rides T-C20/fabric).
4. **Scope guards held**: the payload is tool-emitted (never hand-edited); the
   pinned corpus, the C13 sheet/store, gold-v1 and snap-001 are untouched; no
   core serving behavior changed; no curriculum contamination — the tranche
   binds to `IAL-CHEM-2018` only, and the §7 no-cross-curriculum rule stays
   enforced at mapping time (mappings themselves are not created in this
   change set).
