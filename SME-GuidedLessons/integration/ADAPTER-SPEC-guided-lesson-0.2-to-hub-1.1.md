# Adapter Specification: `guided-lesson/0.2` → `hub/lesson-import/1.1` (figures layer)

**Status:** OF RECORD — figures-0.2 generation
**Adapter id:** `guided-lesson-0.2--hub-lesson-import-1.1`
**Absorbed directive:** operator trace `1a1820011919e8b9` ("go, run the full 112-note figures chain")
**Proposal of record:** SCHEMA-0.2-FIGURES-PROPOSAL-20261028.md (sourcing decision trace `1a1800f3b8c138e5`; placement evidence receipt `SME-GUIDED-STUDY-figures-walk-20261028.json`)
**Baseline:** this spec extends ADAPTER-SPEC-guided-lesson-0.1-to-hub.md (0.1 → 1.0, unchanged and still of record for the v2 feed); the 0.2 → 1.1 generation re-runs the SAME field maps on a figures-carrying source generation.

---

## 1. What changed and why

The guided-lesson/0.1 corpus carries no figures: the schema is `additionalProperties: false` throughout, so the parent revision notes' own diagrams (194 assets, hotlinked in production note pages since the corpus scrape) could not reach the guided surface. The proposal of record resolves this as a strictly additive format bump: source `guided-lesson/0.2` (optional top-level `figures[]` + optional per-lesson `figureIds[]`), target `hub/lesson-import/1.1` (optional `lesson.figures[]` + optional `modules[].figureIds[]`). Everything else — every teaching string, every derived id, every gate — is the 0.1 → 1.0 adapter of record re-run verbatim.

**Conservation stance:** figures carry NO authored prose. They are structured references (url, alt, sourceHeading provenance, lesson-claim ordinals) into the parent note's own image assets. The canonical authored stream (0.1 spec §7) is unchanged by construction, and this generation proves it per note: every per-note stream anchor equals the INT-3 fullcorpus record exactly (INT-3-transform-record-figures-0.2.json, `matchesLegacy: true` ×112; grand + wave streams equal manifest v2 of record).

## 2. Source contract (input of record)

Source format **`guided-lesson/0.2`** — schema of record at `integration/schema/guided-lesson.0.2.schema.json` (draft-07, `additionalProperties: false`). Identical to 0.1 except:

1. `format.const = "guided-lesson/0.2"`.
2. Optional top-level `figures[]`: `id` (`^fig-[0-9]{2}$`, note-scoped, bodyMd order), `url` (pattern pinned to `SME-RevisionNotes/igcse-chemistry-19/assets/` — the sourcing decision is machine-checkable), `alt` (minLength 1), `sourceHeading` (nearest preceding note heading, verbatim), `moduleIds[]` (claiming lesson ordinals `L1..L5`; empty = note-level).
3. Optional per-lesson `figureIds[]` (minItems 1 when present) — closure with `figures[].moduleIds` is lint-enforced both ways.

The mapping from note bodies is the deterministic pipeline of record (`tooling/figures-0.2-pipeline.js`, receipt `FIG4-mapping-receipt-20261028.json`): bodyMd segmented by headings → each image attaches to its nearest preceding heading → joins lessons via `sourceHeadings` (exact match, then normalized-substring fallback; fallback joins audited 21/21). Full corpus: 200 figures / 90 notes; 122 module-mapped, 78 note-level (moduleIds `[]`); match modes 101 exact / 21 fuzzy / 78 none. Notes without figures (22) emit no `figures[]` key — valid 0.2 by construction.

**Immutability law (0.1 spec §9) upheld:** the 0.2 generation is a NEW namespace (`integration/source-0.2/`), re-derived from the 0.1 wave artifacts at the grounding pin; the wave-N/ artifacts are untouched. `source.pinnedRef` in every 1.1 output points at the source-0.2 promotion commit; `source.sourceLayerSha256` is the sha256 of the ingested 0.2 source layer file.

## 3. Target (normative schema)

| Target | `$id` | File | Grain |
|---|---|---|---|
| Hub lesson import (figures) | `hub/lesson-import/1.1` | `schema/hub-lesson-import.1.1.schema.json` | one file per note |

1.1 is a mechanical copy of 1.0 with: format/adapter consts bumped; `source.sourceFormat` pinned to `guided-lesson/0.2`; optional `lesson.figures[]` (verbatim passthrough of source figures); optional `modules[].figureIds[]` (verbatim from the source lesson's `figureIds`). `sme-question-package/1.0` is NOT re-versioned: questions are untouched, the 112 package artifacts are byte-identical to the v2 generation (per-file sha256 re-verified at the grounding pin).

## 4. Field maps

All 0.1 → 1.0 maps (0.1 spec §4.1/§4.2) apply verbatim. The figures deltas:

| Source path (0.2) | Target path (1.1) | Rule |
|---|---|---|
| `figures[]` | `lesson.figures[]` | verbatim passthrough (id, url, alt, sourceHeading, moduleIds), order preserved |
| `lessons[i].figureIds[]` | `lesson.modules[i].figureIds[]` | verbatim passthrough, order preserved |

Determinism gate (C-7): the re-transform of every note equals the of-record 1.0 output field-for-field after removing ONLY the declared deltas (`format`, `adapter`, `source` block, `lesson.figures`, `modules[].figureIds`) — verified ×112 in the pipeline run of record.

## 5. Derived identity grammar

Unchanged from the 0.1 spec §5 (lesson `igcse-chemistry::rn_<noteId>`, module `rn_<noteId>::L<i>`, question `rn_<noteId>::L<i>::Q<k>`, package `igcse-chemistry::rn_<noteId>`). Figure ids are NOT derived: they are carried verbatim (`fig-NN`, note-scoped) from the source generation.

## 6. Placement semantics (decided, evidence-backed)

Module figures render **immediately after the module's opening plain-words text, before the key points** in the confidence-gate stage — the SME-faithful placement resolved by the live evidence walk (SME shows its figures inline inside the "In plain words" explanation; key points live on the pre-lesson gate, so "after key points" was never the benchmark behavior). Note-level figures (`moduleIds: []`) are **page-fallback only**: they render in the "read as a page" static fallback (honestly labelled as coming from the revision note) and on the note page itself (where they always rendered via bodyMd), never inside the adaptive lesson flow. Rendering uses the same plain `<img>` hotlink path as the notes reader, `alt` mandatory, no new hosting, no asset copying.

## 7. Conservation law

**Unchanged and strengthened.** The §7 stream walk is byte-identical (figures fields are not stream tokens). Acceptance for this generation: per-note stream sha256+chars equal the INT-3 fullcorpus anchors ×112; grand stream (1,347,771 chars) and wave subtotals ×10 equal manifest v2 of record. Any future figures change that altered an authored string would break these equalities and fail the channel.

## 8. Gate inventory (run of record: fig4-pipeline, checks 902/902 + map 653/653)

| Gate | Asserts |
|---|---|
| C-1 | notes corpus 112; census 200 figures / 90 notes == of-record grounding; max figures/note ≤ 99 |
| C-2 | 112 upstream 0.1 artifacts @ pin; v2 manifest kinds 112/112; 1.0 outputs + 112 packages byte-verified @ pin (sha256 == v2 manifest) |
| C-4 | every figure URL basename ∈ upstream assets dir (194/194 1:1) |
| C-5 | figureIds ↔ moduleIds closure, both directions, ×112 |
| C-6 | ajv draft-07 ×112 vs `guided-lesson/0.2` and ×112 vs `hub/lesson-import/1.1` |
| C-7 | adapter determinism ×112 (re-transform == 1.0 of-record minus declared deltas) |
| C-8 | per-note stream anchors ×112 == INT-3 fullcorpus record |
| C-9 | package shas unchanged ×112 |
| C-10 | grand stream + wave subtotals ×10 == manifest v2 of record; manifest v3 lists 224 |
| V | cold re-verify from emitted bytes: schemas + stream + artifact shas + pinnedRef wiring ×112 |

## 9. Versioning

This generation follows the 0.1 spec §9 law: optional-field-only additions, new adapter id, new target `$id`, new integration namespace, zero mutation of prior generations (v2 feed remains importable by the unmodified runner constants). The hub runner accepts both feeds (dual-format: manifest v2 @ the promotion commit for the 1.0 generation; manifest v3 @ the figures-0.2 promotion commit for this generation).

## 10. Conformance run of record

Full-corpus figures generation, 2026-10-28: pipeline `tooling/figures-0.2-pipeline.js` (map 653/653, transform 902/902 checks green); manifest `hub-import-manifest-v3.json`; transform record `records/INT-3-transform-record-figures-0.2.json`; promotion receipt `records/FIGURES-0.2-PROMOTION-20261028.json`; hub-side feed consumed by `run_import.mjs` FEED=figures-0.2-v3 (hub PR of record).
