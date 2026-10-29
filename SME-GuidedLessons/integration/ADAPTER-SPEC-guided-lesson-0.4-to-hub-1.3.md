# Adapter Specification: `guided-lesson/0.4` → `hub/lesson-import/1.3` (figures binding layer)

**Status:** OF RECORD — figures-2.2 generation
**Adapter id:** `guided-lesson-0.4--hub-lesson-import-1.3`
**Absorbed directive:** operator traces `1a18923d3913e2ed` ("queue the follow-up — concept-grain mapping so each diagram binds to the specific lesson that teaches it") and `1a1892c0212a94fd` ("probe and execute")
**Queue of record:** FIGURES-2-2-CONCEPT-GRAIN-QUEUED-20261030 (hub-side lane receipt; 112-file census forecast: 200 figures / 90 notes / 122 module-mapped, wholesale claims measured at exactly 14)
**Baseline:** this spec extends ADAPTER-SPEC-guided-lesson-0.3-to-hub-1.2.md (0.3 → 1.2, unchanged and still of record for the v5 feed); the 0.4 → 1.3 generation is the figures-2.1 (captions, 1.2) byte baseline plus ONLY the declared deltas below.

---

## 1. What changed and why

The captions generation taught every diagram to SPEAK (figure.caption), but the claims were still note-grain: 14 figures carried `moduleIds` listing EVERY guided lesson of the note (and, in lockstep, every module's `figureIds` listed every figure) — the flagship sample renders the same five Alcohols diagrams in both lessons. The operator's directive: each diagram binds to the SPECIFIC guided lesson that teaches it.

The binding surface was measured, not assumed: `lesson.figures[].sourceHeading` ↔ `lesson.modules[].sourceHeadings` both exist of record — but a naive heading→lesson join does NOT discriminate (the sample's two lessons declare IDENTICAL sourceHeadings `["Alcohols","A molecule of ethanol"]`). The binding therefore runs a deterministic rule chain that falls through to caption↔lesson-text evidence, and fails closed.

**Conservation stance:** `moduleIds` / `figureIds` / `binding` are NOT §7 stream tokens. The canonical authored stream is unchanged by construction, proven per note: every per-note stream anchor equals the figures-2.1 (captions, 1.2) generation exactly (INT-3-transform-record-figures-2.2.json, `matches12: true` ×112; grand + wave streams equal manifest v5 of record, hence v4).

## 2. Source contract (input of record)

Source format **`guided-lesson/0.4`** — schema of record at `integration/schema/guided-lesson.0.4.schema.json` (draft-07, `additionalProperties: false`). Identical to 0.3 except:

1. `format.const = "guided-lesson/0.4"`.
2. Optional `figures[].binding` (`enum: heading-unique | sole-lesson | content-overlap | note-level | unresolved`) — the rule of record that produced the claim set.
3. `figures[].moduleIds` and `lessons[].figureIds` VALUES narrowed in lockstep (the closure is recomputed, both directions).
4. `lessons[].figureIds.minItems` relaxed `1 → 0` — a guided lesson may teach no diagrams after narrowing (3 lessons land empty: rn_HNXFQt7vM32g6PMv L2, rn_bGgYrQXP2tqrYwdV L1, rn_vVdP57QhDYSVfZgy L2).

**Binding rule chain (deterministic, nothing authored):**

| Rule | Condition | Action | Census |
|---|---|---|---|
| `heading-unique` (90) | figure.sourceHeading listed by exactly one lesson's sourceHeadings | bind there | verification-only — all 90 already single-claimed |
| `sole-lesson` (0) | note has exactly one lesson | bind to it | no single-lesson note carries module-mapped figures |
| `content-overlap` (12) | heading listed by 2+ lessons AND caption present: caption tokens ∩ lesson teaching text (title + keyPoints + opening + depthLayers), threshold of record **top ≥ 2 AND margin ≥ 1** | bind to the single winner | 12/12 captioned shared-heading figures elected (scores of record in the INT record) |
| `note-level` (78) | `moduleIds: []` | untouched — page-fallback only, never rebound | 78 |
| `unresolved` (20) | no decisive rule (18 heading-not-listed in multi-lesson notes; 2 shared-heading-uncaptioned: rn_4tzwS4GZjPybwtkS fig-02, rn_tvwj4VZ6yFscPJfD fig-01) | **keep existing claims**, record `binding: "unresolved"` | fail-closed; of these, 2 keep wholesale claims (14 → 2) |

No teaching string, check, glossary term, or worked-example byte is touched. The only mutations are the three binding fields and the format const.

**Immutability law upheld:** the 0.4 generation is a NEW namespace (`integration/source-0.4/`), re-derived from the 0.3 layer at the figures-2.1 commit A (`71922d1510ee9e00400667670b40f36e1ae5d456`'s parent main `5586acae1627d965049bac92de1ea9d1cc70c42c`); `source-0.3/` untouched. Determinism D-1 ×112: 0.4 == 0.3 minus declared deltas (`format`, `figures[].binding`, `figures[].moduleIds`, `lessons[].figureIds`). C-3 ×112: the rule chain recomputes identically from the emitted 0.4 bytes (cold, no side inputs).

## 3. Target (normative schema)

| Target | `$id` | File | Grain |
|---|---|---|---|
| Hub lesson import (binding) | `hub/lesson-import/1.3` | `schema/hub-lesson-import.1.3.schema.json` | one file per note |

1.3 is a mechanical copy of **the figures-2.1 1.2 outputs** (which carry the captions layer) with: `format`/`adapter` consts bumped; `source.sourceFormat` pinned to `guided-lesson/0.4`; `source.sourceLayerSha256` = sha256 of the per-note 0.4 file; `source.pinnedRef` = the source-0.4 promotion commit (commit A); optional `lesson.figures[].binding` (verbatim passthrough); `lesson.figures[].moduleIds` and `lesson.modules[].figureIds` narrowed in lockstep; `definitions.module.properties.figureIds.minItems` relaxed `1 → 0`. `sme-question-package/1.0` is NOT re-versioned: the 112 package artifacts are byte-identical to the v2/v3/v4/v5 generation (sha256 re-verified ×112).

## 4. Field maps (declared deltas)

The 0.3 → 1.2 maps apply; the 1.3 outputs are the **figures-2.1 1.2 bytes mutated by exactly these deltas**:

| Path | Rule |
|---|---|
| `format` | `"hub/lesson-import/1.2"` → `"hub/lesson-import/1.3"` |
| `adapter` | `"guided-lesson-0.3--hub-lesson-import-1.2"` → `"guided-lesson-0.4--hub-lesson-import-1.3"` |
| `source` block | `sourceFormat` → `"guided-lesson/0.4"`; `sourceLayerSha256` → sha256(0.4 file); `pinnedRef` → commit A |
| `lesson.figures[]` | rebuilt in key order `id,url,alt,sourceHeading,caption,binding,moduleIds`; `binding` + narrowed `moduleIds` verbatim from source-0.4 |
| `lesson.modules[].figureIds` | recomputed from the narrowed `figure.moduleIds` (closure both ways; may be empty) |

Determinism gate (D-2): every 1.3 output with the declared deltas removed is `deepEqual` to the figures-2.1 1.2 of-record bytes ×112. Cross-layer passthrough (C-2c): 1.3 figures == source-0.4 figures ×112. Closure (C-5): figureIds ↔ moduleIds both directions ×112 under the narrowed values.

## 5. Derived identity grammar

Unchanged from the 0.1 spec §5. Figure ids remain carried verbatim (`fig-NN`, note-scoped); lesson/module ids remain `<noteId>::L<n>` by ordinal.

## 6. Placement semantics (UNCHANGED from the 0.3→1.2 §6)

Module figures render **after the module's "Key points of understanding" block, before the confidence fieldset** — caption-first, with the `"sourceHeading — from the revision note"` provenance line. The binding layer changes WHICH guided lesson renders each diagram, not HOW a diagram renders: a figure bound to L2 appears in L2's flow only (after L2's key points); the other lessons no longer list it. Unresolved rows keep their existing claims and therefore render exactly as the 1.2 generation rendered them (fail-closed, no learner-visible regression). Note-level figures (`moduleIds: []`) remain page-fallback only. Rendering keeps the plain `<img>` hotlink path, `alt` mandatory, no new hosting, no asset copying.

## 7. Conservation law

**Unchanged and proven against the figures-2.1 generation.** The §7 stream walk is byte-identical (binding/claims are not stream tokens). Acceptance: per-note stream sha256+chars equal the 1.2 anchors ×112 (computed both directions: 1.3 vs 1.2 bytes per note); grand stream (1,426,764 chars) and wave subtotals ×10 equal manifest v5 of record (hence v4). Any future binding change that altered an authored string would break these equalities and fail the channel.

## 8. Gate inventory (run of record: figures-2-2-binding-pipeline)

| Gate | Asserts | Result |
|---|---|---|
| C-1 | 112 notes == manifest v5 lesson artifacts; schemas carry optional binding + closed objects + minItems relaxation | green |
| C-2 | upstream fidelity: 1.2 `sourceLayerSha256` == sha256(source-0.3 bytes) ×112; figures passthrough both layers ×112 | green |
| C-3 | binding rule chain recomputes identically from emitted 0.4 bytes ×112 | green |
| C-4 | binding invariants: narrowed → single claim; unresolved → original claims kept; census row for every module-mapped figure | green |
| D-1 | 0.4 == 0.3 minus declared deltas ×112 | green |
| D-2 | 1.3 == 1.2 minus declared deltas ×112 | green |
| C-5 | figureIds ↔ moduleIds closure both ways ×112 (narrowed) | green |
| C-6 | ajv draft-07 ×112 vs `guided-lesson/0.4`, ×112 vs `hub/lesson-import/1.3`, ×112 packages vs 1.0 | green |
| C-8 | per-note stream 1.3 == 1.2 (1.2 bytes) ×112 | green |
| C-9 | package shas unchanged ×112 | green |
| C-10 | grand + wave subtotals ×10 == manifest v5; manifest v6 lists 224; claim-changing narrows == 12; wholesale kept == 2 (was 14) | green |
| V | cold re-verify from emitted bytes: schemas + artifact shas + INT anchors + pinnedRef wiring + per-figure binding recompute + stream recompute ×112 (876 checks) | green |

Totals: source phase 452/452, transform phase 1015/1015, verify phase 876/876.

## 9. Versioning

Optional-field addition + value narrowing in the claim fields, new adapter id, new target `$id`, new integration namespaces (`source-0.4/`, `hub-import-1.3/`), zero mutation of prior generations (v2/v3/v4/v5 feeds remain importable by the unmodified runner constants). The hub runner accepts the new feed (`figures-2-2-v6`, manifest v6 @ the promotion commit) alongside the existing ones.

## 10. Conformance run of record

Full-corpus binding generation, 2026-10-30: pipeline `tooling/figures-2-2-binding-pipeline.js`; manifest `hub-import-manifest-v6.json`; transform record `records/INT-3-transform-record-figures-2.2.json`; promotion receipt `records/FIGURES-2.2-PROMOTION-20261030.json`; hub-side feed consumed by `run_import.mjs` FEED=figures-2-2-v6 (hub PR of record follows).
