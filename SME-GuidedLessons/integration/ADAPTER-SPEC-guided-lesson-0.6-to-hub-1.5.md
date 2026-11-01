# Adapter Specification: `guided-lesson/0.6` → `hub/lesson-import/1.5` + `sme-question-package/1.2` (PHYSICS-4PH1 stage A)

**Status:** OF RECORD — PHYSICS-4PH1 stage-A pilot generation (the new-subject bootstrap tranche)
**Adapter id:** `guided-lesson-0.6--hub-lesson-import-1.5`
**Absorbed directives:** operator trace `1a192830222371a5` ("open the new subject's wave-1 contract. The new subject 4ph1 physics.") ignited the contract; operator trace `1a1954284ff72101` ("ignite stage-A execution") executed stage A.
**Runbook of record:** `.syllabai/docs/new-subject-runbook.md` @ `SyllabAI/syllabai-v2` `f99969a2` (verified byte-unchanged at `55f91919`); this spec follows §0 B1–B8 and §1 of that runbook.
**Baseline:** this spec extends ADAPTER-SPEC-guided-lesson-0.5-to-hub-1.4.md (unchanged and still of record for the v7+ chemistry feeds). Physics has NO chemistry baseline bytes — the transform is a FULL derivation from the 0.6 source (chemistry artifacts are re-validated as union baselines, never mutated).

---

## 1. What changed and why

A SECOND subject (IGCSE Physics Edexcel 4PH1, course-id `igcse-physics-19`) enters the zero-DB guided-lessons plane via the new-subject runbook. Stage A is the PILOT tranche only: ONE note (`rn_RpyMnS5nqWSRWXXG`, Distance-Time Graphs, spec point 1.3 "plot and explain distance−time graphs") authored as 2 lessons × exactly 9 checks (5 MCQ + 2 recall + 1 explain-why + 1 application — the B2 law). Wave-1 buckets remain OPERATOR-GATED and are not part of this generation (B3: the pilot stays out of the wave buckets).

**B6 decision of record (the runbook's one flagged open decision): CONTINUE-GLOBAL.** The manifest v-series continues across subjects — physics stage-A = `hub-import-manifest-v18.json`. Rejected: per-course series (physics v1) — it would collide with chemistry `hub-import-manifest-v1..v17.json` filenames in the shared `integration/` namespace and fork the programme-level integration ledger (the series is the chain of custody: v9 = the withheld-import disclosure, v17 = STAGE B COMPLETE). The manifest self-declares its subject: v18 carries `course_id: "igcse-physics-19"` + a `b6_manifest_continuity` block; the hub feed binds manifest v18 to the physics pack. Recorded here, in the manifest, and in the stage-A receipt.

## 2. Source contract (input of record)

Source format **`guided-lesson/0.6`** — schema of record at `integration/schema/guided-lesson.0.6.schema.json` (draft-07, `additionalProperties: false`). Identical to 0.5 except:

1. `format` becomes the generation-union enum `["guided-lesson/0.5", "guided-lesson/0.6"]` (the 1.4 union law applied to the source layer).
2. Course-scoped patterns generalized, chemistry-validating: spec codes `^([A-Z0-9]+-)?[0-9]+\.[0-9]+[A-Z]?$` accept BOTH `4CH1-4.29C` and plain 4PH1 codes (`1.3`); figure URLs accept BOTH `igcse-chemistry-19` and `igcse-physics-19` asset namespaces.

**Authoring law (stage A of record):** each written item is spec-anchored to its lesson's keyPoints (KP-index provenance) and carries `modelAnswer` + a generous synonym/inflection-bearing `keywords` set, every keyword grounded in the modelAnswer/stem/keyPoints union (KW gate). The audit battery of record **A0/AN/SG/KW/JC/2.1B/NUM** (runbook §1.4) ran in `tooling/physics-stagea-pipeline.js` — 38/38 gates GREEN, gate log embedded in the promotion receipt.

**Authoring source of record:** the revision-note ROW (hub `apps/hub/content/igcse-physics-19/notes.json` @ `55f91919` — noteId registry, specPointCodes, bodyMd with asset URLs pinned @ `aa0b4de1`); prose parity vs the resources `.md` proven 24/25 paragraphs (one worked-example image-line paragraph splits differently — disclosed). Figures are the parent note's own asset-dir images (machine-verified: every basename resolves in `SME-RevisionNotes/igcse-physics-19/assets/`), bodyMd-ordered, bound heading-unique to lessons. Captions: the note's own bold-italic explanatory line immediately following the figure block; 5 worked-example images carry none (fail-closed absent, declared).

## 3. Target (normative schemas)

| Target | `$id` | File | Grain |
|---|---|---|---|
| Hub lesson import (physics) | `hub/lesson-import/1.5` | `schema/hub-lesson-import.1.5.schema.json` | one file per note |
| Question package (physics) | `sme-question-package/1.2` | `schema/sme-question-package.1.2.schema.json` | one file per note |

Both targets are GENERATION-UNION minors over 1.4/1.1: the consts become enums (`format`, `adapter`, `source.sourceFormat`, package `subject`), the lesson/package-id patterns accept `^(igcse-chemistry|igcse-physics)::rn_[A-Za-z0-9]+$`, and the spec/figure-URL patterns generalize as above. Union proven in the pipeline: 112 chemistry sources vs 0.6 + 112 chemistry lessons vs 1.5 + 112 chemistry packages vs 1.2, zero failures (C-6 ×336). The chemistry generations themselves are byte-untouched.

## 4. Field maps (the full derivation)

| Source (0.6) | Target (1.5 lesson) |
|---|---|
| `noteRef.{noteId, corpusVersion, topicTitle, subtopicTitle, sourceUrl}` | `lesson.{...}` verbatim + `lesson.id = "igcse-physics::<noteId>"` |
| `specPoints[]` | `lesson.specAnchors[]` ({code, text} verbatim) |
| `primer` | `lesson.primer` verbatim |
| `lessons[]` | `lesson.modules[]`: `id = "<noteId>::L<i>"`, title, sourceHeadings, specRefs, opening, keyPoints, depthLayers{low,medium}, `gatePolicy` from `confidenceGate` (`ratings`→`ratingsScale`), `checkRefs = <module>::Q1..Q9` in check order, figureIds |
| `noteAssets.glossary[]` | `lesson.assets.glossary[]` verbatim (term/definition/firstLesson) |
| `noteAssets.workedExample` | `lesson.assets.workedExample` verbatim (or null) |
| `figures[]` | `lesson.figures[]` verbatim (caption carried only when present) |

| Source (0.6) | Target (1.2 package) |
|---|---|
| — | `packageId = "igcse-physics::<noteId>"`, `subject = "igcse-physics"`, `source` = the lesson's source block |
| `lessons[].check[]` in module order | `questions[]`: `{id: "<noteId>::L<i>::Q<k>", moduleId, stem, misconceptionClass, options[...]}` for MCQ; written kinds add `{kind, modelAnswer, keywords?}` and force `options: []` |

Both channels pin `source.sourceLayerSha256 = sha256(source-0.6 file)` and `source.pinnedRef = commit A`.

## 5. Derived identity grammar

Unchanged from the 0.1 spec §5, generalized prefix: `igcse-physics::<noteId>` for lesson/package ids; `<noteId>::L<i>` modules; `<noteId>::L<i>::Q<k>` questions (k = 1..9 per the B2 law).

## 6. Rendering semantics (normative for the hub)

Unchanged from the 0.5 spec §6 — the chemistry R3 chain already shipped the written-kind renderer (labelled free-text input, keyword grading law, model answer always shown on settle, reveal-only fail-closed, a11y) and the figure cards. The hub route is course-generic (`courses/[course]/guided-lessons/[noteId]` + per-course `guided-import.json` discovery, fail-closed `null` for courses without the index). The physics feed requires runner constants only (see §10).

## 7. Conservation law

**Extended walk of record (byte-identical to run_import.mjs targetTokens):** on questions with `kind != mcq`, the §7 stream walk additionally pushes `modelAnswer` then each `keyword`. The pilot note's stream is anchored in the INT-3 record (13,924 chars, sha256 in `grand_stream`); wave bucket `wave-0` (stage-A pilot convention; wave buckets 1..N of the physics register remain operator-gated). The chemistry corpus streams are byte-untouched — v18 re-issues NO chemistry artifacts (declared in the manifest `supersedes`).

## 8. Gate inventory (run of record: physics-stagea-pipeline)

| Gate | Asserts | Result |
|---|---|---|
| P0 | commit A resolves on the integration branch; source-0.6 + 0.6 schema bytes == commit A blobs | green |
| A0 | ajv 0.6 + 9-check SME kind order ×2 lessons + B2 sizing + figure closure both ways + glossary band + primer word band | green |
| AN | exactly-one-correct ×10; correct-key census (≥3 distinct letters, max ≤5); distinct option texts | green |
| JC | every option explained; distractors name misconceptions; correct-option misconception null | green |
| SG | lesson specRefs ⊆ file specPoints; every check KP-anchored (content-token overlap) | green |
| KW | ≥3 distinct grounded keywords per written item ×8 | green |
| 2.1B | zero 8-gram overlaps of learner-surface text vs the corpus note body | green |
| NUM | 8000/360 = 22.2 (3sf); 8 km = 8000 m; 6 min = 360 s; distractor arithmetics 8/6 = 1.3, 8000/60 = 133 | green |
| C-6 | ajv: source vs 0.6; outputs vs 1.5/1.2; chemistry union ×336 (112 sources + 112 lessons + 112 packages) | green |
| written ×8 | id grammar, modelAnswer, ≥3 keywords, options empty | green |
| C-5 | checkRefs ↔ questions bidirectional 1:1 in order | green |
| B2 target | every module carries exactly 9 checkRefs; identity arithmetic 9 = 5+2+1+1 ×2 | green |
| G-E | pilot stream anchor + wave-0 subtotal + grand vs manifest | green |

Totals: 38/38 gates pass, 0 failures (gate log embedded in the promotion receipt).

## 9. Versioning

Optional-field generalization + union consts, new adapter id, three new target/source `$id`s, three new integration namespaces (`source-0.6/`, `hub-import-1.5/`, `question-packages-1.2/`), zero mutation of prior generations (the chemistry v2–v17 feeds remain importable by their unmodified runner constants). The hub runner accepts the new feed (`physics-stagea-v18`, manifest v18 @ the promotion commit) alongside the existing ones, with feed-gated constants (pack/course_id/counts/prefix/wave-count) carrying chemistry-preserving defaults.

## 10. Conformance run of record

Stage-A pilot generation, 2026-11-01: pipeline `tooling/physics-stagea-pipeline.js`; manifest `hub-import-manifest-v18.json`; transform record `records/INT-3-transform-record-physics-stagea.json`; promotion receipt `records/PHYSICS-4PH1-STAGEA-PROMOTION-20261101.json`; hub-side feed consumed by `run_import.mjs` FEED=physics-stagea-v18 (hub PR of record follows the resources merge). Wave-1 bucketing remains operator-gated.

## 11. Disclosures (B1 + provenance)

- **B1 deviation bridged:** the physics register plane lacked `spec_point_resolution.json` (chemistry carries one). Bridged by bootstrap commit B0 on this branch: derived MECHANICALLY from the hub-landing registry (`notes.json` `smeSpecPointIds` — id/code/note mappings only, no spec texts invented; the chemistry file additionally carried an operator HUMAN_VALIDATED legacy record this subject lacks).
- The register manifest itself (`SME-RevisionNotes/igcse-physics-19/manifest.json`, 127 notes / 373 assets / 188 spec links, generated 2026-09-17) is the corpus provenance anchor (`corpusVersion` `sme-revision-notes-igcse-physics-19-2026-09-17`).
