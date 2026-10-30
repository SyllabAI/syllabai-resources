# Adapter Specification: `guided-lesson/0.5` → `hub/lesson-import/1.4` + `sme-question-package/1.1` (R3 mixed check types)

**Status:** OF RECORD — R3-CHECK-TYPES stage-A pilot generation (Alcohols tranche)
**Adapter id:** `guided-lesson-0.5--hub-lesson-import-1.4`
**Absorbed directive:** operator trace `1a189fd011119961` ("R-3 — mixed check types") queued the wave; operator trace `1a18a0218b7f44fd` ("probe and execute") executed stage A.
**Queue of record:** R3-MIXED-CHECK-TYPES-QUEUED-20261030 (hub-side lane receipt; hub contract probed at 100% single-select MCQ — 112 packages × 1,195 questions × 4,760 options, zero kind data upstream-to-downstream)
**Baseline:** this spec extends ADAPTER-SPEC-guided-lesson-0.4-to-hub-1.3.md (0.4 → 1.3, unchanged and still of record for the v6 feed); the pilot outputs are the figures-2.2 (1.3 / 1.0) bytes mutated by ONLY the declared deltas below.

---

## 1. What changed and why

The hub's guided checks are 100% single-select MCQ. The SME lesson of record (2026-10-26 recheck, live-confirmed) carries a MIXED taxonomy per lesson set: exactly 5 items = 1 multiple-choice (auto-graded) + 2 recall + 1 explain-why + 1 application, the written kinds keyword auto-graded with the model answer shown. R-3 ports that taxonomy to the authored format and the renderer — ADDITIVELY: nothing converted, nothing deleted, the 1,195 existing MCQs byte-identical (conservation gate).

Stage A is the PILOT tranche only: the walked Alcohols subtopic set (rn_2MpXPtNXvn8pQm3r + rn_8T5GfPn2q7sY2YCh = 4 lessons) carries 16 authored written items (8 recall, 4 explain-why, 4 application — 2 recall + 1 explain-why + 1 application per lesson, mirroring the SME set shape). Stage B (corpus rollout, ~956 items) remains OPERATOR-GATED and is not part of this generation.

## 2. Source contract (input of record)

Source format **`guided-lesson/0.5`** — schema of record at `integration/schema/guided-lesson.0.5.schema.json` (draft-07, `additionalProperties: false`). Identical to 0.4 except:

1. `format.const = "guided-lesson/0.5"`.
2. `check.maxItems` relaxed `5 → 9` (5 MCQ + up to 4 written items per lesson).
3. Optional written-kind check branch (if/then): `kind` in `{recall, explain-why, application}` requires `modelAnswer` (non-empty string) and forbids `options`; optional `keywords` (1–20 non-empty strings). `kind` absent or `"mcq"` keeps the 0.4 MCQ shape exactly (exactly one keyed correct, every option explained, distractors name misconceptions).

**Authoring law (stage A of record):** each written item is spec-anchored to its lesson's keyPoints and carries `modelAnswer` + a generous synonym/inflection-bearing `keywords` set. The `anchor` field used at authoring time is provenance-only and stripped from the emitted source bytes.

**Immutability law upheld:** the 0.5 generation is a NEW namespace (`integration/source-0.5/`), carrying ONLY the 2 pilot notes; the other 110 notes remain at source-0.4. D-1 ×2: 0.5 == 0.4 minus declared deltas (`format`, appended check items).

## 3. Target (normative schemas)

| Target | `$id` | File | Grain |
|---|---|---|---|
| Hub lesson import (R3) | `hub/lesson-import/1.4` | `schema/hub-lesson-import.1.4.schema.json` | one file per note |
| Question package (R3) | `sme-question-package/1.1` | `schema/sme-question-package.1.1.schema.json` | one file per note |

Both targets are GENERATION-UNION minors: the consts become enums (`format`, `adapter`, `source.sourceFormat`) so the 110 untouched 1.3-format lessons and 110 1.0-format packages validate unchanged under the same schemas (single ajv compile per target at the import gate). 1.4 additionally relaxes `checkRefs.maxItems 5 → 9` and the item pattern to `Q[1-9]`. 1.1 additionally relaxes the question id pattern to `Q[1-9]` and adds the written-kind branch: `kind` in `{recall, explain-why, application}` requires `modelAnswer`, allows optional `keywords`, and forces `options` to be EMPTY; `kind` absent or `"mcq"` keeps the 1.0 shape byte-for-byte (minItems 3 options via the else branch; the base options schema deliberately carries no minItems so the branches never AND-conflict). Unknown `kind` values fail the schema (hard gate) and would warn at this pipeline (designed-warning mechanism).

## 4. Field maps (declared deltas)

The pilot outputs are the **figures-2.2 bytes mutated by exactly these deltas** (D-2 ×2 each):

| Path (lesson, 2 files) | Rule |
|---|---|
| `format` | `"hub/lesson-import/1.3"` → `"hub/lesson-import/1.4"` |
| `adapter` | → `"guided-lesson-0.5--hub-lesson-import-1.4"` |
| `source` block | `sourceFormat` → `"guided-lesson/0.5"`; `sourceLayerSha256` → sha256(0.5 file); `pinnedRef` → commit A |
| `lesson.modules[].checkRefs` | extended with `::Q6..::Q9` (module order; 5 → 9 per pilot module) |

| Path (package, 2 files) | Rule |
|---|---|
| `format` | `"sme-question-package/1.0"` → `"sme-question-package/1.1"` |
| `adapter` | → `"guided-lesson-0.5--hub-lesson-import-1.4"` |
| `source` block | `sourceFormat` → `"guided-lesson/0.5"`; `sourceLayerSha256` → sha256(0.5 file); `pinnedRef` → commit A |
| `questions` | rebuilt module-grain: per module, the 5 originals (byte-deep-equal) then the 4 written items `{id, moduleId, stem, misconceptionClass, kind, modelAnswer, keywords?, options: []}` — ids minted `<noteId>::L<n>::Q6..Q9` |

Everything else — figures layer (captions + bindings), glossary, worked examples, prose — byte-identical to 1.3.

## 5. Derived identity grammar

Unchanged from the 0.1 spec §5. Written questions continue the per-lesson ordinal (`::Q6..::Q9` after the 5 MCQs).

## 6. Rendering semantics (normative for the hub)

- **MCQ path untouched byte-for-byte** at both renderer sites (`guided-check.tsx` read layer, `guided-flow.tsx` check stage).
- **Written kinds** render a labelled free-text input (textarea), submit → verdict (`role="status"`) + the model answer, which is ALWAYS shown on settle (correct or not — the model answer IS the teaching moment).
- **Grading law:** case-insensitive whole-token match of the learner text against `keywords[]` (both sides tokenized on `[a-z0-9]+` runs); ≥1 hit → correct; 0 hits → not-quite + model answer; empty submit → blocked (mirror of `continueDisabledUntilChoice` spirit); keywords absent → reveal-only (model answer shown, no verdict) — fail-closed, never a silent wrong grade.
- **Tally integrity:** the keyword-hit boolean rides the existing `onAnswer(id, picked, correct)` signature (`picked` carries the learner's text); answered/correct tallies, module gating, and recalibration are unchanged.
- **Fail-closed:** a written item without `modelAnswer` renders stem + reveal-only (never gradeable, never blank); an unknown `kind` renders reveal-only.
- **A11y:** `<label for>` on the input, `role="status"` verdict, native keyboard operability.

## 7. Conservation law

**Extended walk of record:** on questions with `kind != mcq`, the §7 stream walk additionally pushes `modelAnswer` then each `keyword` (after the options walk). Old packages carry no `kind`, so the walk is byte-neutral for them — the 110 non-pilot per-note streams equal the figures-2.2 (1.3) anchors EXACTLY (proven ×110 in the pipeline). The 2 pilot notes add the 16 written items' tokens (stem, misconceptionClass, modelAnswer, keywords — written kinds carry no options). Grand stream 1,429,907 chars (+3,143 vs 1.3's 1,426,764); wave subtotals ×10 recomputed in the v6 note order (manifest v7 conservation block).

MCQ conservation: the 10 original questions per pilot package appear deep-equal in the 1.1 arrays; the 110 non-pilot packages are byte-identical (sha256 ×110 vs manifest v6); distractor census unchanged at 3,565 (written kinds carry no options).

## 8. Gate inventory (run of record: r3-check-types-pipeline)

| Gate | Asserts | Result |
|---|---|---|
| P0 | commit A resolves; source-0.5 + schema 0.5 bytes == commit A blobs | green |
| C-1/C-2 | manifest v6 shape; 224 local bytes == v6 shas ×112 notes; sourceLayerSha256 + pinnedRef wiring ×112 | green |
| D-1 | 0.5 == 0.4 minus declared deltas ×2 | green |
| C-6 | ajv: sources ×2 vs 0.5; outputs ×4 vs union schemas; 220 untouched artifacts vs union schemas | green |
| written ×16 | id grammar, modelAnswer, keywords ≥1, options empty | green |
| MCQ conservation | originals deep-equal in 1.1 arrays ×2 (+8 count) | green |
| C-5 | checkRefs ↔ questions bidirectional 1:1 in order ×2 | green |
| D-2 | outputs minus declared deltas deep-equal the 1.3/1.0 bytes ×4 | green |
| C-9 | 110 package shas byte-identical vs manifest v6 | green |
| G-E | 110 non-pilot stream anchors == 1.3 exactly; pilots re-anchored; grand + waves ×10 | green |

Totals: 33/33 gates pass, 0 failures (gate log embedded in the promotion receipt).

## 9. Versioning

Optional-field addition + union consts, new adapter id, two new target `$id`s, three new integration namespaces (`source-0.5/`, `hub-import-1.4/`, `question-packages-1.1/`), zero mutation of prior generations (v2–v6 feeds remain importable by their unmodified runner constants). The hub runner accepts the new feed (`r3-check-types-v7`, manifest v7 @ the promotion commit) alongside the existing ones, with feed-gated evolutions (written-kind G-D exemption, pilot pin map, lesson-kind census map, declared 4-file revision delta).

## 10. Conformance run of record

Stage-A pilot generation, 2026-10-30: pipeline `tooling/r3-check-types-pipeline.js`; manifest `hub-import-manifest-v7.json`; transform record `records/INT-3-transform-record-r3-check-types.json`; promotion receipt `records/R3-CHECK-TYPES-1.0-PROMOTION-20261030.json`; hub-side feed consumed by `run_import.mjs` FEED=r3-check-types-v7 (hub PR of record follows the resources merge). Stage B remains operator-gated.
