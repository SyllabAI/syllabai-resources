# Adapter Specification: `guided-lesson/0.1` → Hub Import Schema Family + `sme-question-package`

**Status:** OF RECORD — wave-10 pilot deliverable
**Adapter id:** `guided-lesson-0.1--hub-lesson-import-1.0`
**Absorbed directive:** operator trace `1a1751f592e67391` ("start the adapter spec")
**Landed under:** operator trace `1a1774a86c1b5a41` ("land it"), ROUND-PILOT-LANDING-20261026
**Baseline:** INT-0 pin — `SyllabAI/syllabai-resources` @ commit `4d857c472fd725597ac21db189542c8f12c82dba` (MANIFEST v9, 499 entries, corpus complete 112/112)

---

## 1. Why this spec exists

The integration plan (Ten-Wave-Retrospective-Brief, Section 9 / Table 3) requires an INT-3 transform stage, but the contracts package contains **no guided mapping**: the hub's import schema family has no entry for the guided-lesson layer format the authoring lane produced, and no question-bank contract exists for the explained check items embedded in each layer. This spec is therefore the **only net-new contract deliverable** of the integration channel. It defines two target schemas normatively, fixes the field maps between source and targets, decides the confidence-gate semantics (previously open), and states the conservation law that any conforming transform must satisfy. The wave-10 pilot (INT-1..INT-5) is the first conformance run of this adapter.

## 2. Source contract (input of record)

Source format **`guided-lesson/0.1`** — schema of record at `scripts/guided-lesson.0.1.schema.json` (draft-07, `additionalProperties: false` throughout). One file per revision note; required top-level: `format`, `noteRef` (noteId, corpusVersion, topicTitle, subtopicTitle, sourceUrl), `specPoints[]` (code + official text), `primer` (text + prerequisiteSubtopic), `lessons[]` (1–5; title, sourceHeadings[1–2], specRefs[], opening, keyPoints[3–6], confidenceGate, depthLayers{low,medium}, check[1–5]), `noteAssets` (glossary[3–8], workedExample or null).

Two wave-10-specific source treatments are first-class in this adapter (both data-driven, both preserved):

- **Three-code data-driven flattening.** Notes whose `specPointCodes` carry three codes (e.g. `4CH1-4.34C / 4.35C / 4.37C`) flatten into lessons by data, not by rule: lesson `specRefs` partition the declared code set (1+2 or 2+1 groupings observed). The adapter maps this structure verbatim — it never re-groups codes.
- **Arithmetic-verified worked-example port.** The Carboxylic acids layer ports the propanoic-acid calculation from the note body (steps in expression-first single-equals form, e.g. `3 - 1 = 2`, `2 x 2 + 1 = 5`), arithmetic verified at stated significant figures. The other seven wave-10 layers declare designed `workedExample: null`. The adapter passes both forms through untouched; the pilot re-verifies the arithmetic independently (INT-2 gate G10).

## 3. Target family (normative schemas minted by this spec)

| Target | `$id` | File | Grain |
|---|---|---|---|
| Hub lesson import | `hub/lesson-import/1.0` | `schema/hub-lesson-import.1.0.schema.json` | one file per note |
| SME question package | `sme-question-package/1.0` | `schema/sme-question-package.1.0.schema.json` | one file per note |

Rationale for the split: the hub consumes **teaching surfaces** (primer, modules, depth layers, gate policy, glossary, worked example), while the question bank consumes **assessable items** (stems, options, explanations, misconceptions). Embedding questions in the lesson import would couple two independent lifecycles (lesson re-ordering vs question banking); the adapter therefore **moves** checks to the package and leaves ordered **`checkRefs`** in each module. Both schemas are draft-07 with `additionalProperties: false` — unknown fields fail closed, exactly like the source contract.

## 4. Field maps

### 4.1 `guided-lesson/0.1` → `hub/lesson-import/1.0`

| Source path | Target path | Rule |
|---|---|---|
| `noteRef.corpusVersion` | `source.corpusVersion` | verbatim |
| `noteRef.noteId` | `source.noteId` | verbatim; also feeds derived ids (§5) |
| `noteRef.topicTitle` / `subtopicTitle` / `sourceUrl` | `lesson.topicTitle` / `subtopicTitle` / `sourceUrl` | verbatim |
| `specPoints[]` | `lesson.specAnchors[]` | verbatim (code, text), order preserved |
| `primer` | `lesson.primer` | verbatim (text, prerequisiteSubtopic), null preserved |
| `lessons[i].title` | `lesson.modules[i].title` | verbatim |
| `lessons[i].sourceHeadings` | `lesson.modules[i].sourceHeadings` | verbatim, order preserved |
| `lessons[i].specRefs` | `lesson.modules[i].specRefs` | verbatim, order preserved |
| `lessons[i].opening` | `lesson.modules[i].opening` | verbatim |
| `lessons[i].keyPoints` | `lesson.modules[i].keyPoints` | verbatim, order preserved |
| `lessons[i].depthLayers` | `lesson.modules[i].depthLayers` | verbatim (low, medium × restatement/analogy/examPointer) |
| `lessons[i].confidenceGate` | `lesson.modules[i].gatePolicy` | **mapped, semantics decided (§6)** |
| `lessons[i].check` | `lesson.modules[i].checkRefs` | **moved** to package; ordered ids here (§5) |
| `noteAssets.glossary[]` | `lesson.assets.glossary[]` | verbatim (term, definition, firstLesson) |
| `noteAssets.workedExample` | `lesson.assets.workedExample` | verbatim or null |

### 4.2 `guided-lesson/0.1` → `sme-question-package/1.0`

| Source path | Target path | Rule |
|---|---|---|
| `lessons[i].check[k].stem` | `questions[q].stem` | verbatim |
| `lessons[i].check[k].misconceptionClass` | `questions[q].misconceptionClass` | verbatim |
| `lessons[i].check[k].options[]` | `questions[q].options[]` | verbatim (key, text, correct, explanation, misconception), null preserved on the correct option |
| — (derived) | `questions[q].id`, `questions[q].moduleId` | derived per §5 |

`questions[]` order is module order, then check order — the flattening is deterministic and lossless.

## 5. Derived identity grammar

Derived ids are the **only** strings a conforming transform may invent (structural, not authored):

```
lesson (hub)      : igcse-chemistry::rn_<noteId>
module            : rn_<noteId>::L<i>            i = 1..5, layer order
question          : rn_<noteId>::L<i>::Q<k>      k = 1..5, check order within lesson i
package           : igcse-chemistry::rn_<noteId>
```

Provenance is pinned structurally: both target files carry a `source` block with `sourceFormat: "guided-lesson/0.1"`, `noteId`, `corpusVersion`, `sourceLayerSha256` (sha256 of the ingested source layer file at the pin) and `pinnedRef` (the INT-0 commit). Any future re-transform from a different pin produces a different `pinnedRef` and is detectable by construction.

## 6. Confidence-gate semantics — DECIDED

The source `confidenceGate` block is authoring metadata with a runtime contract. The adapter maps it 1:1 to `gatePolicy` with the following decided semantics:

1. `ratings: ["low","medium","high"]` → `ratingsScale` (same three values, same order). The scale is positional metadata of the write-once gate; the hub must present exactly these three self-rating choices.
2. `continueDisabledUntilChoice: true` → `gatePolicy.continueDisabledUntilChoice`, **preserved and import-blocking**: the source schema pins this to `true` by construction, and the adapter asserts it. A source file that somehow carries `false` is not importable — the hub must never render a lesson whose continue control is not gated on an explicit self-rating.
3. `resumeWithoutReRate: true` → `gatePolicy.resumeWithoutReRate`, **preserved and import-blocking** (same rationale): a resumed session restores the prior rating and must not re-prompt.
4. `postCheckRecalibration: <bool>` → `gatePolicy.postCheckRecalibration`, verbatim passthrough. When `true`, the hub recalibrates the learner's depth-layer default after each passed check; when `false`, the initial rating holds for the module.

The gate is **per module** (it always was per lesson; modules are the hub's lesson unit). The gate is not learner data, not surface copy, and is excluded from the conservation stream (§7); it is instead pinned by the metadata equality gate (§8, M-gate).

## 7. Conservation law (INT-3 acceptance invariant)

**Law.** A conforming transform is a pure restructure: every authored string in the source appears exactly once in the targets, and every count is preserved 1:1. Any divergence is a hard failure — the channel never silently drops or rewords content.

**Canonical authored stream.** Concatenate, joined by `\n`, in exactly this order (identical walk applied to source and targets):

1. **Spec anchors:** for each specPoint/anchor in file order: `code`, then `text`.
2. **Primer:** `text`; then `prerequisiteSubtopic` if non-null.
3. **Module teaching,** in module order, per module: `title`; each `sourceHeadings` entry; each `specRefs` entry; `opening`; each `keyPoints` entry; `depthLayers.low.restatement`, `.analogy`, `.examPointer`; `depthLayers.medium.restatement`, `.analogy`, `.examPointer`.
4. **Assets:** each glossary entry (`term`, `definition` — `firstLesson` is numeric, pinned by the M-gate, not in the stream); if `workedExample` non-null: `prompt`, each `steps` entry, `finalAnswer`.
5. **Questions,** in module order then check order: `stem`, `misconceptionClass`, then per option in order: `key`, `text`, `explanation`, `misconception` if non-null.

Excluded by definition (structural/derived, pinned by other gates): `format`/`adapter`/`source` blocks, all derived ids, `correct` booleans, `firstLesson`, `ratingsScale` membership, gate booleans, `noteRef` identity fields (pinned verbatim by the M-gate below).

**Acceptance:** `sha256(source_stream) == sha256(target_stream)` **and** `len(source_stream) == len(target_stream)`, computed per note and wave-totalled. Any transform that rewords, trims, normalises whitespace, or reorders authored content breaks equality and fails INT-3.

## 8. Gate inventory (replayed at INT-2/INT-3/INT-5)

| Gate | Stage | Asserts |
|---|---|---|
| S | INT-2/INT-5 | ajv draft-07 validation, fail-closed (source vs `guided-lesson/0.1`; targets vs both §3 schemas) |
| C1 | INT-2 | check integrity: exactly one `correct: true` per item; unique option keys; `misconception` non-null on every distractor, null on the correct option; explanations non-empty |
| C2 | INT-2 | spec-code set equality: `specPoints[].code` == union(`lessons[].specRefs`) (three-code flattening integrity) |
| C3 | INT-2 | cadence: counts vs wave receipt of record (8 notes / 17 lessons / 85 checks / 85 keyPoints / 255 distractors / 42 glossary / 20,546 bodyChars declared) |
| C4 | INT-2 | gate contract: `ratings` == 3 values, both const-true invariants hold (authoring side) |
| C5 | INT-2 | receipt cross-check ×8: noteId, lesson titles in order, spec codes, per-note counts, workedExample declaration (present/null) matches layer truth |
| C6 | INT-2 | event-log ground truth ×8: single export, zero re-exports, P0 unflagged, single P8 close, zero pauses |
| C7 | INT-2 | arithmetic re-verification: every equation `expr = result` in a non-null workedExample recomputed and matched at the stated precision; null declarations consistent |
| M | INT-3/INT-5 | metadata equality: noteRef fields, glossary `firstLesson`, gate booleans, `correct` flags — verbatim 1:1 |
| Q | INT-3/INT-5 | count conservation: lessons/keyPoints/checks/options/distractors/glossary/checkRefs 1:1; question ids ↔ checkRefs bidirectional |
| Φ | INT-3/INT-5 | stream conservation (§7): sha256 + length equality, per note and wave-total |
| X | INT-5 | cold-read cross-reference: every manifest artifact sha256 matches disk; every `checkRefs` id resolves to a package question and vice versa |

## 9. Versioning and error handling

- Targets are versioned by `$id` (`hub/lesson-import/1.0`, `sme-question-package/1.0`). A future `1.1` that only adds optional fields is additive; any change to conservation-relevant maps requires a new adapter id (`guided-lesson-0.1--hub-lesson-import-1.1`) and a fresh pilot.
- Transforms **fail closed**: unknown source fields (impossible under the source schema, defended in depth), missing optional-with-null fields, count drift, or stream inequality abort the stage with a per-item failure table; no partial artifacts are published (stage output lands atomically after all gates pass).
- The adapter never mutates the source corpus. Wave artifacts are immutable at the INT-0 pin (additive-only law); re-transforms read the pin and write to a new integration namespace.

## 10. Conformance run of record

First conformance run: **wave-10 pilot** (8 layers, 25 manifest entries @ pin `4d857c47`), stages INT-1 (mechanical ingest, per-file sha256), INT-2 (gate replay S/C1..C7), INT-3 (transform + M/Q/Φ), INT-4 (load, integration manifest v1), INT-5 (surface smoke, S/M/Q/Φ/X re-run cold + rendered sample). Pilot green arms full-corpus promotion (all 112 layers) behind explicit operator go, with QA sampling between pilot and full run per the integration plan.
