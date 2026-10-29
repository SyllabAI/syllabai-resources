# Adapter Specification: `guided-lesson/0.3` → `hub/lesson-import/1.2` (figures captions layer)

**Status:** OF RECORD — figures-2.1 generation
**Adapter id:** `guided-lesson-0.3--hub-lesson-import-1.2`
**Absorbed directive:** operator traces `1a188a15ac19ed05` ("you are not using the diagrams properly — SME explains") and `1a188c14685e2965` ("probe and execute the wave")
**Audit of record:** FIGURES-USAGE-AUDIT-20261030 (hub-side lane receipt; 200 figures / 90 notes — 143 coalescible captions, 16 table-embedded, 3 bullets-embedded, 38 caption-less)
**Baseline:** this spec extends ADAPTER-SPEC-guided-lesson-0.2-to-hub-1.1.md (0.2 → 1.1, unchanged and still of record for the v3/v4 feeds); the 0.3 → 1.2 generation is the v4 (worked-examples-1.0) byte baseline plus ONLY the declared deltas below.

---

## 1. What changed and why

The figures-0.2 layer carried each parent note's diagrams as bare references (`id`, `url`, `alt`, `sourceHeading`, `moduleIds`). The operator's finding of record: SME does not LIST its diagrams — it EXPLAINS with them. In the SME source layer (syllabai.sme-revision-note/1.0), each figure block is followed by its own explanatory line (bold-italic caption paragraph), the prose references the diagrams ("…are shown below"), and table figures ARE the table's data (displayed formulae). The 1.1 generation coalesced none of this: figure blocks carry `caption: null` in the SME model (the caption lives in the ADJACENT paragraph block), so the live corpus had 0/200 captions and the flow rendered a provenance-labelled gallery before any teaching.

The fix is strictly additive: source `guided-lesson/0.3` (optional `figures[].caption`), target `hub/lesson-import/1.2` (same optional field, verbatim passthrough). Every teaching string, every derived id, every gate is the v4 of-record unchanged.

**Conservation stance:** captions carry NO authored prose — they are the parent note's OWN explanatory lines, recovered positionally. The canonical authored stream (§7 walk) is unchanged by construction, proven per note: every per-note stream anchor equals the v4 (worked-examples-1.0) generation exactly (INT-3-transform-record-figures-2.1.json, `matchesV4: true` ×112; grand + wave streams equal manifest v4 of record).

## 2. Source contract (input of record)

Source format **`guided-lesson/0.3`** — schema of record at `integration/schema/guided-lesson.0.3.schema.json` (draft-07, `additionalProperties: false`). Identical to 0.2 except:

1. `format.const = "guided-lesson/0.3"`.
2. Optional `figures[].caption` (`type: string`, `minLength: 1`) — the note's own explanatory line, coalesced mechanically from the sidecar at `integration/source-0.3` build time.

**Derivation rules (deterministic, nothing authored):**

| Class | Rule | Census |
|---|---|---|
| `coalesced` (143) | the `paragraph` block immediately following the `figure` block, bold-italic house style (`***…***`) → inner text | 143 |
| `row-context` (16) | figure inside a `table` block → `"<column header> — <row label>"` from verbatim table cells | 16 |
| `inline` (3) | figure inside a `bullets`/`paragraph` block → the introducing line, image syntax and emphasis markers stripped | 3 |
| none (38) | no adjacent explanatory line → **no caption key** (fail-closed: 36 standalone-no-cap + 2 inline-no-text) | 38 |

Whitespace-only normalization is applied (runs of whitespace → single space). No word is added, removed, or reordered anywhere.

**Immutability law upheld:** the 0.3 generation is a NEW namespace (`integration/source-0.3/`), re-derived from the 0.2 layer at the worked-examples-1.0 commit A (`8ea8c63a46d75fc54733900dfecf5d3c5c93bbde`); `source-0.2/` untouched. Determinism D-1 ×112: 0.3 == 0.2 minus declared deltas (`format`, `figures[].caption`).

## 3. Target (normative schema)

| Target | `$id` | File | Grain |
|---|---|---|---|
| Hub lesson import (captions) | `hub/lesson-import/1.2` | `schema/hub-lesson-import.1.2.schema.json` | one file per note |

1.2 is a mechanical copy of **the v4 1.1 outputs** (which carry the worked-examples layer) with: `format`/`adapter` consts bumped; `source.sourceFormat` pinned to `guided-lesson/0.3`; `source.sourceLayerSha256` = sha256 of the per-note 0.3 file; `source.pinnedRef` = the source-0.3 promotion commit (commit A); optional `lesson.figures[].caption` (verbatim passthrough). `sme-question-package/1.0` is NOT re-versioned: the 112 package artifacts are byte-identical to the v2/v3/v4 generation (sha256 re-verified ×112).

## 4. Field maps (declared deltas)

The 0.2 → 1.1 maps apply; the 1.2 outputs are the **v4 1.1 bytes mutated by exactly these deltas**:

| Path | Rule |
|---|---|
| `format` | `"hub/lesson-import/1.1"` → `"hub/lesson-import/1.2"` |
| `adapter` | `"guided-lesson-0.2--hub-lesson-import-1.1"` → `"guided-lesson-0.3--hub-lesson-import-1.2"` |
| `source` block | `sourceFormat` → `"guided-lesson/0.3"`; `sourceLayerSha256` → sha256(0.3 file); `pinnedRef` → commit A |
| `lesson.figures[].caption` | inserted (key order `id,url,alt,sourceHeading,caption,moduleIds`) verbatim from source-0.3; absent where the source has none |

Determinism gate (D-2, the C-7 analog): every 1.2 output with the declared deltas removed is `deepEqual` to the v4 1.1 of-record bytes ×112. Cross-layer passthrough (C-2c): 1.2 figures minus caption == source-0.3 figures minus caption ×112.

## 5. Derived identity grammar

Unchanged from the 0.1 spec §5. Figure ids remain carried verbatim (`fig-NN`, note-scoped).

## 6. Placement semantics (SUPERSEDES the 0.2 spec §6)

Module figures render **after the module's "Key points of understanding" block, before the confidence fieldset** — caption-first: each figure carries its `caption` as the teaching line (when present) and the provenance line `"<sourceHeading> — from the revision note"`; the 1.1-era block-level label ("Diagrams from the revision note") is REMOVED. Rationale of record: the 0.2 §6 after-opening placement mirrored SME's position but without the captions that do the explaining — the operator's finding is that the diagrams must be USED (caption + point-of-use), not listed. Uncaptioned figures render the provenance line only (fail-closed, no invented copy). Note-level figures (`moduleIds: []`) remain page-fallback only, never inside the lesson flow. Rendering keeps the plain `<img>` hotlink path, `alt` mandatory, no new hosting, no asset copying.

## 7. Conservation law

**Unchanged and proven against the v4 generation.** The §7 stream walk is byte-identical (captions are not stream tokens). Acceptance: per-note stream sha256+chars equal the v4 (worked-examples-1.0) anchors ×112 (computed both directions: 1.2 vs 1.1 bytes per note); grand stream (1,426,764 chars) and wave subtotals ×10 equal manifest v4 of record. Any future captions change that altered an authored string would break these equalities and fail the channel.

## 8. Gate inventory (run of record: figures-2-1-captions-pipeline)

| Gate | Asserts | Result |
|---|---|---|
| C-1 | 112 notes == manifest v4 lesson artifacts; schemas carry optional caption + closed objects | green |
| C-2 | upstream fidelity: 1.1 `sourceLayerSha256` == sha256(source-0.2 bytes) ×112; figures passthrough both layers ×112 | green |
| D-1 | 0.3 == 0.2 minus declared deltas ×112 | green |
| D-2 | 1.2 == v4 1.1 minus declared deltas ×112 | green |
| C-5 | figureIds ↔ moduleIds closure unchanged ×112 | green |
| C-6 | ajv draft-07 ×112 vs `guided-lesson/0.3`, ×112 vs `hub/lesson-import/1.2`, ×112 packages vs 1.0 | green |
| C-8 | per-note stream 1.2 == 1.1 (v4 bytes) ×112 | green |
| C-9 | package shas unchanged ×112 | green |
| C-10 | grand + wave subtotals ×10 == manifest v4; manifest v5 lists 224 | green |
| V | cold re-verify from emitted bytes: schemas + artifact shas + INT anchors + pinnedRef wiring + stream recompute ×112 (675 checks) | green |

Totals: source phase 340/340, transform phase 789/789, verify phase 675/675.

## 9. Versioning

Optional-field-only additions, new adapter id, new target `$id`, new integration namespaces (`source-0.3/`, `hub-import-1.2/`), zero mutation of prior generations (v2/v3/v4 feeds remain importable by the unmodified runner constants). The hub runner accepts the new feed (`figures-2-1-v5`, manifest v5 @ the promotion commit) alongside the existing three.

## 10. Conformance run of record

Full-corpus captions generation, 2026-10-30: pipeline `tooling/figures-2-1-captions-pipeline.js`; manifest `hub-import-manifest-v5.json`; transform record `records/INT-3-transform-record-figures-2.1.json`; promotion receipt `records/FIGURES-2.1-PROMOTION-20261030.json`; hub-side feed consumed by `run_import.mjs` FEED=figures-2-1-v5 (hub PR of record follows).
