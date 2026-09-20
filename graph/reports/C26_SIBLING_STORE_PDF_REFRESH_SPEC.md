# T-C26 — Sibling-store PDF-refresh spec (v1.1, executed)

**Date:** 2026-09-20 (spec v1.0 proposed pre-execution; v1.1 records execution status) · **Author lane:** definitive-swap closeout (C25) + this round · **Status:** EXECUTED — see `C26_SIBLING_STORE_REFRESH_RECORD.md`
**Repos:** `SyllabAI/syllabai-resources` · **Curriculum scope:** IGCSE Chemistry 4CH1 only (binding R1)
**Wording authority:** `international-gcse-chemistry-2017-specification.pdf` (sha1 `3ad641b7…`) via `Official-Specifications/parsed/igcse-chemistry/*.json` (canonical-builder-2.0, PDF-direct) (binding R2)

## 1. Mission

Close the last open item of the C23 definitive swap: the five sibling stores still carried
OCR-lineage statement text and truthful-but-stale `statement_text_policy: verbatim from md OCR`
meta lines. Refresh their wording from the canonical PDF-direct parse, keep every ratified
enrichment, and bring their meta/lineage blocks to the definitive standard. After T-C26, **no**
store in `graph/` claims the retired OCR md as its wording source.

## 2. Phase-0 inventory (verified 2026-09-20, re-verified after workspace reset #5)

| Store | Records | Text fields | Canonical source | Mapping | Refresh type |
|---|---|---|---|---|---|
| `graph/topics.yaml` | 4 topics + 28 subtopics | `title`, `title_md`; subtopic `header_source` (`md-table` = OCR-era) | `topics.json` (8 canonical topics incl. front/back matter; **28 subsections, 1:1 by letter**) | topics: filter canonical to the 4 content topics (`4CH1-T3..T6`) | **Verbatim refresh** (titles — turned out congruent) + `header_source` upgrade |
| `graph/practicals.yaml` | 12 | `summary` | `practicals.json` (**12, 1:1 by ordering**; `summary` + `spec_point` + `page`) | 1:1 | **Verbatim refresh** (label prefix stripped per C23 leading-verb rule) |
| `graph/assessment_objectives.yaml` | 3 AOs + 2 papers | `title`, `weighting_overall`, `weighting_by_paper`; papers block | `assessment_objectives.json` (**3 statements, 1:1**; flag `ao-dash-lost` on AO2 text-layer cell) | 1:1 by AO code | **Verbatim refresh + flag resolution**; papers have **no canonical source** → ratified overlay |
| `graph/command_words.yaml` | 25 | `command_word`, `definition`, `category` | `command_words.json` (**25, 1:1**; `command_word` + `definition` + `page`) | 1:1 (punctuation-insensitive identity) | **Verbatim refresh**; `category` stays ratified |
| `graph/relationships.yaml` | 210 edges | **none** — pure structure (`from`/`to`/`relation`/`order`) | n/a | n/a | **No wording refresh.** Referential-integrity pass (214 distinct endpoints) + meta refresh |

**Evidence coupling: zero.** No `file:` references to any of the five stores exist in
`concepts.yaml`, `concept_edges.yaml`, `spec_chunk_mappings.yaml`, or `spec_command_kinds.yaml`.
Unlike C23, **no quote re-anchor pass was required**.

## 3. Non-goals and standing guards

- Node states (`concepts.yaml`, `concept_edges.yaml`) byte-untouched.
- `_derived/**` untouched (already definitive via T-C24's emit round).
- 2012-Jan escalations and the data bridge: not approached.
- Damage doctrine: flagged, never silently fixed — every change and flag resolution is in
  `C26_WORDING_DIFF_LEDGER.json`.
- No hand-edits to emitted stores: emitter-only (graph-as-code).

## 4. Execution (as-run)

- **Phase 0:** field map frozen (`scripts/c26_field_map.yaml`); PDF cross-checks of the
  adjudication sites (pages 19, 27, 28, 35 via `pdftotext -layout`).
- **Phase 1:** `scripts/c26_emit_definitive_sibling_stores.py` — stdlib-only, deterministic
  (byte-identical re-runs **including the ledger**; baseline is always `git show HEAD:` so the
  emitter is idempotent), explicit meta overrides (no `dict(old_meta)` blind inheritance —
  the C25 lesson), per-record provenance (`wording_source`, `pdf_page`, `pdf_sha1`).
- **Phase 2 (operator-delegate adjudications):**
  1. **PR-09** — canonical parse truncated after `change:` (bullet-colon class); old store
     ALSO truncated (`…displacement reacti`). Bullets restored verbatim from PDF p27:
     `• salts dissolving in water • neutralisation reactions • displacement reactions •
     combustion reactions.` (inline, store convention).
  2. **PR-10** — old store summary truncated mid-word (`…between marbl`); canonical
     PDF-direct text adopted (`…between marble chips and dilute hydrochloric acid`, p28
     spot-checked).
  3. **AO2 weighting** — canonical text-layer cell damaged (`38 42%` + parser annotation);
     resolved to `38–42%` by PDF p35 Total row (renders `38–42%` for AO2) + column arithmetic
     (`23.2–25.7 + 14.8–16.3 = 38.0–42.0`).
  4. **En-dash adoption** — weightings restored to PDF en-dash verbatim (AO1/AO3 overall +
     all 12 `weighting_by_paper` values from canonical `unit_weightings`).
  5. **Command words** — `What,Why,Which` → `What, Why, Which` (identity); 7 definitions
     adopted from canonical (bullet glyphs for DISCUSS, curly apostrophe for EVALUATE,
     en-dash for EXPLAIN, spacing repairs for JUSTIFY/PLOT/SKETCH).
- **Phase 3:** battery `scripts/c26_postcheck.py` — **ALL PASS (8/8)**: counts preserved;
  semantic diff = intended-only (every changed leaf path ledgered); refreshed wording ==
  canonical; overrides verbatim; damage-class sweep 0 hits; 214/214 relationship endpoints +
  subtopic spec_points refs resolve; meta audit (no `md OCR`, live generators, `c09` only as
  retired lineage); working-tree changes = intended files only.
- **Phase 4:** single commit with records + pins; push on `syllabai-resources`.

## 5. Results (ledger totals)

12 wording changes · 1 identity change · 15 field adoptions · 13 flag resolutions
(all five flag classes — `title-differs-md-vs-pdf`, `subsection-header-missing-in-md`,
`lost-space`, `unknown-leading-verb`, `ao-range-dash-missing` — resolved with recorded
evidence; no flags added). **Two truncation-damage records found and repaired (PR-09, PR-10)
— a damage class the character-class sweep cannot see, caught only by the wording refresh.**

## 6. Post-close (Phase 5)

The C25 record's open item (five sibling stores on the OCR lineage) is closed by this round;
per record-immutability, the closure is noted here, not by editing the C25 record. The five
stores' `generator` fields now name the live pipeline (`c26_emit…`); `c09` appears only as
retired lineage.

## 7. Risks realized / notes

- The en-dash/curly-quote adoption changes bytes that some consumers may compare
  ASCII-normalized — the canonical parse and the definitive spec store already carry these
  glyphs (C23 precedent), so sibling stores are now consistent with them.
- `papers` block (marks/duration/weighting) has no canonical source and is provenance-marked
  `ratified-overlay` untouched.
- Workspace reset #5 occurred mid-round (disk exhaustion from the full SME corpora clone);
  the round was re-based on a blobless+sparse clone (`--filter=blob:none`) without loss —
  C25 commit `9ea8d113` verified as ancestor of the new head before work resumed.
