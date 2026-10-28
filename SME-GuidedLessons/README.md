# SME-GuidedLessons — the guided-lesson authoring programme (exports of record)

> For every note in the 112-note IGCSE Chemistry revision-notes register, this
> programme authors a **guided lesson** (schema `guided-lesson.0.1`: two-layer
> reading core + 10 checks + key points + glossary + ported worked example),
> wave by wave, under a hard dual gate. This folder is the **durable home of
> every export of record**: the lesson layers, the timing receipts, the chain
> event logs, the pinned corpus snapshot, the pacing register of record, the
> gate tooling, and the wave reports. Any agent (or human) can arrive here cold
> and verify the whole chain from register row to export receipt.

## Why a new folder (decision record, operator trace `1a16f959b77972c1`)

The operator asked for this work to be saved either in a new folder or inside
`SME-RevisionNotes/`. The decision: **new top-level folder `SME-GuidedLessons/`**, because:

1. `SME-RevisionNotes/` is the **source corpus of record** (per-syllabus notes +
   manifest, RAG-ingested). Per `AGENT.md` rule 4, provenance / source identity /
   review state must stay unambiguous for corpus artifacts — mixing derived
   programme exports and gate telemetry into the source corpus would blur it.
2. `CourseLessons/` is a **different programme** with its own doctrine
   (interactive HTML Lessons, stage flow S0–S4, gates G1–G4, `lesson-prose@2.0.0`).
   The `guided-lesson.0.1` wave exports are a different artefact class; folding
   them in would create a false provenance association.
3. The `SME-*` family (`SME-RevisionNotes`, `SME-ExamQuestion`, `SME-Flashcards`)
   is the established naming class for SME-authored derived artifacts —
   `SME-GuidedLessons/` joins it and leaves room for waves 4+ (78 notes remain).

## What lives here

| Path | Purpose |
|---|---|
| `wave-1/`, `wave-2/`, `wave-3/`, `wave-4/`, `wave-5/`, `wave-6/`, `wave-7/`, `wave-8/`, `wave-9/`, `wave-10/` | The exports of record per wave: `guided-lesson-rn_<id>.json` (the lesson layer) + `timing-receipt-rn_<id>.json` (export-gate telemetry). All ten waves carry their aggregate `wave<N>-receipt.json` (wave receipt of record, minted at each close-out with the recalibration block and event-log ground truth); wave-1 carries the `snapshot-pin-reverify-20261024.json`. |
| `event-logs/wave-<N>/` | The P0–P8 chain logs (`rn_<id>.events.json`) — one per note. Wave-1 also carries the per-note `note-body.md` extracts used during the instrumented first run. |
| `corpus-snapshot.json` | The **pinned authoring substrate**: all 112 note bodies, sha256 `e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d`. Every round re-verifies this pin; body text is read from here, never from a live DB. |
| `pacing/wave-pacing-open-20261024.json` | The **register of record**: all 112 notes with wave plan, subtopics, body char counts, spec point codes. |
| `tooling/` | The gate + harness + verifier scripts: `a1-lint.js` (the lint gate), `wave1-run.js` (the authoring harness, incl. the save() patch lineage), `wave<N>-round-verify.js` (per-round verifiers, wave-3's carrying the close-out guards), `wave3-row-dump.js`, `wave3-schema-check.js`, `wave3-p0flag-repair.js` (the disclosed P0-flag repair tool), the wave receipt builders (`wave<N>-wave-receipt.js`) and report generators (`wave<N>-report*.js`). Paths inside are sandbox-absolute (`/home/z/my-project/...`) — they are records of how gates were run. |
| `reports/` | Wave report deliverables (docx): Wave-1 instrumented-authoring report, Wave-2 report, Wave-3 report, Wave-4 report, Wave-5 report, Wave-6 report, Wave-7 report, Wave-8 report, Wave-9 report, Wave-10 report. |
| `MANIFEST.json` | Machine twin: per-file sha256 + byte counts for every file in this folder. Verify with `sha256sum -c`-style tooling of your choice. |

## Status — 112 / 112 notes authored — CORPUS COMPLETE — ALL 28 SUBTOPICS CLOSED

| Wave | Notes | Register rows | Subtopic band | Files |
|---|---|---|---|---|
| wave-1 | 10 | register[0..9] | States & Solutions → Separation techniques (instrumented calibration run) | 22 |
| wave-2 | 12 | register[10..21] | Atoms, formulas, electrolysis band | 25 |
| wave-3 | 12 | register[22..33] | Chemical Formulae, Equations, Calculations → Ionic Bonding | 25 |
| wave-4 | 11 | register[34..44] | Ionic Bonding tail → Covalent → Metallic → Electrolysis (topic-closing) | 23 |
| wave-5 | 12 | register[45..56] | T2 Inorganic Chemistry: Group 1 tail → Group 7 → Gases in the Atmosphere → Reactivity Series opener | 25 |
| wave-6 | 12 | register[57..68] | T2 Inorganic Chemistry: Reactivity Series close → Extraction & Uses of Metals → Acids, Alkalis & Titrations → Acids, Bases & Salt Preparations opener | 25 |
| wave-7 | 9 | register[69..77] | T2 Inorganic Chemistry: Acids, Bases & Salt Preparations close → Chemical Tests close (TOPIC 2 COMPLETES) | 19 |
| wave-8 | 14 | register[78..91] | T3 Physical Chemistry: Energetics → Rates of Reaction → Reversible Reactions & Equilibria (TOPIC 3 OPENS AND COMPLETES) | 29 |
| wave-9 | 12 | register[92..103] | T4 Organic Chemistry: Introduction → Crude Oil → Alkanes → Alkenes close; Alcohols open (TOPIC 4 OPENS) | 25 |
| wave-10 | 8 | register[104..111] | T4 Organic Chemistry: Alcohols → Carboxylic acids → Esters → Synthetic polymers close (CORPUS COMPLETE) | 17 |

**The register is COMPLETE of record: 112/112 notes authored across ten waves — all four topics and all 28 subtopics closed.** Topic 1, Principles of Chemistry, 40/40 across all nine subtopics. Topic 2, Inorganic Chemistry, 36/36 across all eight subtopics (closed across waves 5–7). Topic 3, Physical Chemistry, 15/15 across all three subtopics (opened and closed inside wave-8). Topic 4, Organic Chemistry, 21/21 across all eight subtopics (opened in wave-9, closed in wave-10: Alcohols, Carboxylic acids, Esters and Synthetic polymers). Cumulative totals of record: 239 lessons / 1,195 explained checks / 1,212 key points / 654 glossary entries / 3,565 named-misconception distractors over 361,272 source characters — the authored character count now equals the pinned corpus character count exactly, the closing identity of the programme. Waves 1–10 are CLOSED of record (wave receipts `wave1/…/wave10-receipt.json`, wave reports in `reports/`, recalibration checkpoints discharged — every checkpoint since wave-2 reaffirms the same decision: estimator basis frozen at the wave-1 instrumented 283 s/note; receipts are export-gate telemetry). Wave-10 ran as the fifth fully single-ignition wave (zero repairs, zero re-exports, zero pauses), swept both pre-flight guards clean for the first time (zero source-fidelity runs, zero uniformity flags), and carried 7 designed workedExample-null declarations plus the programme's first numeric port since wave-8 (the Carboxylic Acids note ships its own arithmetic worked examples; the propanoic-acid case was ported in substance and arithmetic-verified by the lint).

**REGISTER COMPLETE:** no wave-11 exists to open — the pacing file's schedule is fully discharged and every one of the 112 notes carries its guided-lesson layer, timing receipt and event log. Any future work attaches to revision or re-authoring rounds (the per-note receipts and event logs remain the audit trail of record) or to downstream flows consuming the corpus; the standing disciplines — pin verification, parity-proofed spec resolution, the pre-flight gates and the idempotent export harness — persist as scripts under `tooling/` ready to run again if the register ever changes.

## The hard laws of this programme (as run)

1. **Dual gate before any export:** ajv `8.20.0` against the `guided-lesson.0.1`
   schema + `a1-lint.js` (accept-vocabulary / forbidden-vocabulary / scanner
   rules). Lint posture: **designed-or-none** — a `workedExample: null` must be
   a designed null (declared), never an omission.
2. **Snapshot pin must MATCH every round:** recompute sha256 of
   `corpus-snapshot.json` before touching anything; a mismatch aborts the round.
3. **The "copy it" red line:** the worked example is ported from the source
   note's own example, verbatim in substance — never paraphrased, never invented.
4. **Chain discipline:** P0 closes unflagged (read-only), the first
   `phase P1` command carries NO flag, P2–P8 close with `--assist` →
   `assistedPhases = P1..P7` exactly; one export event, one P8 phase-end, zero
   pauses per note. (W3 notes 5–6 carry a disclosed repair: an erroneous
   `--assist` on the first P1 command was repaired via
   `tooling/wave3-p0flag-repair.js`; the logs carry `reExport: true` transparency
   events and the layers were untouched. W4 ran the corrected pattern natively
   on its first full wave, and W5 repeated it: single ignition, twelve logs clean,
   zero re-exports, zero pauses, P0 guard clean throughout.)
5. **Receipts are export-gate telemetry** (standing disclosure: batch-flow phase
   clocks read 0 s); the planning estimator basis remains wave-1's 283 s/note.
6. **Lane hygiene:** zero DB writes, zero production-surface contact, zero
   Vercel, tokens never echoed.

## Provenance chain

- **Source notes of record:** `SME-RevisionNotes/cie-igcse-chemistry-23/`
  (upstream corpus of the platform DB the snapshot was minted from).
- **Bodies of record:** pinned 2026-10-23 via a read-only DB SELECT into
  `corpus-snapshot.json` (444,822 bytes) — every round since runs **zero-DB**.
- **Spec texts of record:** waves 1–4 read from the `syllabai-v2` content pack
  (wave-8 generalised the flattening: multi-bullet statements draw their semicolon
  clauses from the pack's own `official_bullets` field — 3.8 and 3.22C in wave-8;
  wave-9 scanned all 30 codes data-driven and found none; wave-10 found 3 (4.31C, 4.32C
  and 4.47), each flattened from the pack's own bullets verbatim);
  (`apps/hub/content/igcse-chemistry-19/curriculum.json`), read-only; wave-5 resolved all
  16 codes, wave-6 all 19 and wave-7 all 11 codes zero-DB from this repo's knowledge graph
  (`graph/igcse-chemistry/specification_points.yaml`), each wave parity-proven 4/4
  against the prior wave's of-record texts before use (wave-7's probes restricted to the
  non-flattened codes — colon-ending pack wordings are exactly the documented flattening
  class).
- **Saved here:** 2026-10-25, lane `w0a`, session
  `web-e79a3bd8-5bc9-4aae-abe2-eb5f5d3964dd`. Initial landing: operator trace
  `1a16f959b77972c1`, single Git-Data-API commit `7dbdf2ba` on `main` (the repo is ~5.6
  GB — clone-impractical in the sandbox; see LEDGER F16 for why verification here uses
  the contents API, never the recursive `git/trees` endpoint). Wave-3 close-out append
  (wave receipt + wave report + tooling + manifest refresh): operator trace
  `1a16fa91188c8f3d`, same single-commit method. Wave-4 append (wave-4 deliverables +
  event logs + report + tooling + manifest v3 refresh): operator trace
  `1a16fbc3d4b5b749`, same single-commit method. Wave-5 append (wave-5 deliverables +
  event logs + report + tooling x8 + manifest v4 refresh): operator trace
  `1a1725e0cd20eb8d`, same single-commit method. Wave-6 append (wave-6 deliverables +
  event logs + report + tooling x9 + manifest v5 refresh): operator "Continue"
  ignition on the recorded wave-6 next step, same single-commit method. Wave-7 append
  (wave-7 deliverables + event logs + report + tooling x9 + manifest v6 refresh):
  operator "Wave-7 — 9" ignition on the recorded wave-7 next step, same single-commit
  method. Wave-8 append (wave-8 deliverables + event logs + report + tooling x25
  including the per-note layer builders + manifest v7 refresh): operator trace
  `1a174751135ae18d` verbatim "Go wave-8", same single-commit method. Wave-9 append
  (wave-9 deliverables + event logs + report + tooling x23 including the per-note layer
  builders + manifest v8 refresh): operator trace `1a174b960e367b61` verbatim "Go wave-9",
  same single-commit method. Wave-10 append (wave-10 deliverables + event logs + report
  + tooling x19 including the per-note layer builders + manifest v9 refresh, the FINAL
  append of the register): operator trace `1a174e627dda7171` verbatim "Go wave-10",
  same single-commit method.

## Integration — downstream import (of record)

The full authored corpus is promoted for hub import via adapter `guided-lesson-0.1--hub-lesson-import-1.0` (spec: `integration/ADAPTER-SPEC-guided-lesson-0.1-to-hub.md`, target schemas `hub/lesson-import/1.0` + `sme-question-package/1.0`). Contents: `integration/hub-import/` 112 lesson-import files, `integration/question-packages/` 112 question packages (1,195 explained checks), `integration/hub-import-manifest-v2.json` (per-file sha256), `integration/records/` stage records of record (wave-10 pilot GREEN trace `1a1774a86c1b5a41`; full-corpus promotion GREEN trace `1a17763c15632259` "promote"). Gates at promotion: per-file sha256 ingest 499/499 @ pin `4d857c472fd725597ac21db189542c8f12c82dba` (356/356 content EXACT + 3 disclosed stale-index auxiliary entries), deterministic gate replay ×112, closing identity reconciled exactly (112 notes / 239 lessons / 1,195 checks / 1,212 key points / 654 glossary terms / 3,565 distractors / 361,272 source chars), authored-char stream conservation 1,347,771 chars sha256-equal pre/post transform, wave-10 pilot idempotence 8/8 byte-identical, seeded QA sampling 12/12 green.


## Figures layer (0.2) — 2026-10-28

The guided-lesson corpus now carries a strictly additive figures generation: `integration/source-0.2/` (112 × `guided-lesson/0.2`, operator trace 1a1820011919e8b9) re-derived from the wave artifacts with the parent revision notes' own diagrams mapped deterministically to lessons (200 figures / 90 notes; 122 module-mapped, 78 note-level page-fallback-only). Schema `integration/schema/guided-lesson.0.2.schema.json`; adapter 1.1 + manifest v3 in `integration/`; authored stream byte-conserved vs the v2 generation (per-note anchors == INT-3 fullcorpus record). See `ADAPTER-SPEC-guided-lesson-0.2-to-hub-1.1.md`.
