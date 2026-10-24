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
| `wave-1/`, `wave-2/`, `wave-3/`, `wave-4/` | The exports of record per wave: `guided-lesson-rn_<id>.json` (the lesson layer) + `timing-receipt-rn_<id>.json` (export-gate telemetry). All four waves carry their aggregate `wave<N>-receipt.json` (wave receipt of record, minted at each close-out with the recalibration block and event-log ground truth); wave-1 carries the `snapshot-pin-reverify-20261024.json`. |
| `event-logs/wave-<N>/` | The P0–P8 chain logs (`rn_<id>.events.json`) — one per note. Wave-1 also carries the per-note `note-body.md` extracts used during the instrumented first run. |
| `corpus-snapshot.json` | The **pinned authoring substrate**: all 112 note bodies, sha256 `e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d`. Every round re-verifies this pin; body text is read from here, never from a live DB. |
| `pacing/wave-pacing-open-20261024.json` | The **register of record**: all 112 notes with wave plan, subtopics, body char counts, spec point codes. |
| `tooling/` | The gate + harness + verifier scripts: `a1-lint.js` (the lint gate), `wave1-run.js` (the authoring harness, incl. the save() patch lineage), `wave<N>-round-verify.js` (per-round verifiers, wave-3's carrying the close-out guards), `wave3-row-dump.js`, `wave3-schema-check.js`, `wave3-p0flag-repair.js` (the disclosed P0-flag repair tool), the wave receipt builders (`wave<N>-wave-receipt.js`) and report generators (`wave<N>-report*.js`). Paths inside are sandbox-absolute (`/home/z/my-project/...`) — they are records of how gates were run. |
| `reports/` | Wave report deliverables (docx): Wave-1 instrumented-authoring report, Wave-2 report, Wave-3 report, Wave-4 report. |
| `MANIFEST.json` | Machine twin: per-file sha256 + byte counts for every file in this folder. Verify with `sha256sum -c`-style tooling of your choice. |

## Status — 45 / 112 notes authored — TOPIC 1 COMPLETE

| Wave | Notes | Register rows | Subtopic band | Files |
|---|---|---|---|---|
| wave-1 | 10 | register[0..9] | States & Solutions → Separation techniques (instrumented calibration run) | 22 |
| wave-2 | 12 | register[10..21] | Atoms, formulas, electrolysis band | 25 |
| wave-3 | 12 | register[22..33] | Chemical Formulae, Equations, Calculations → Ionic Bonding | 25 |
| wave-4 | 11 | register[34..44] | Ionic Bonding tail → Covalent → Metallic → Electrolysis (topic-closing) | 23 |

Waves 1–4 are **CLOSED of record** (wave receipts `wave1/wave2/wave3/wave4-receipt.json`, wave reports in `reports/`, recalibration checkpoints discharged — every checkpoint since wave-2 reaffirms the same decision: estimator basis frozen at the wave-1 instrumented 283 s/note; receipts are export-gate telemetry). **Topic 1, Principles of Chemistry, is COMPLETE of record: 40/40 notes across all nine subtopics** (States of Matter, Elements Compounds & Mixtures, Atomic Structure, The Periodic Table, Chemical Formulae Equations & Calculations, Ionic Bonding, Covalent Bonding, Metallic Bonding, Electrolysis). Programme position: 45/112 notes (40.2 percent), 9 of 28 subtopics closed outright, cumulative 94 lessons / 470 checks / 487 key points / 290 glossary entries. Wave-4 ran the corrected invocation pattern natively on its first full wave (zero repairs, zero re-exports, zero pauses) and carried 11 designed declarations (9 workedExample-null + 2 non-numeric ported examples).

**NEXT (operator-gated):** wave-5 open — 12 notes (30,208 chars, 18 spec points) opening Topic 2, Inorganic Chemistry: Group 1 tail → Group 7 (Halogens) → Gases in the Atmosphere. All wave-5 artefacts append to this folder on the standing convention.

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
   on its first full wave: zero repairs, zero re-exports, zero pauses, and the
   P0 assist===false guard clean on all eleven logs.)
5. **Receipts are export-gate telemetry** (standing disclosure: batch-flow phase
   clocks read 0 s); the planning estimator basis remains wave-1's 283 s/note.
6. **Lane hygiene:** zero DB writes, zero production-surface contact, zero
   Vercel, tokens never echoed.

## Provenance chain

- **Source notes of record:** `SME-RevisionNotes/cie-igcse-chemistry-23/`
  (upstream corpus of the platform DB the snapshot was minted from).
- **Bodies of record:** pinned 2026-10-23 via a read-only DB SELECT into
  `corpus-snapshot.json` (444,822 bytes) — every round since runs **zero-DB**.
- **Spec texts of record:** read from the `syllabai-v2` content pack
  (`apps/hub/content/igcse-chemistry-19/curriculum.json`), read-only.
- **Saved here:** 2026-10-25, lane `w0a`, session
  `web-e79a3bd8-5bc9-4aae-abe2-eb5f5d3964dd`. Initial landing: operator trace
  `1a16f959b77972c1`, single Git-Data-API commit `7dbdf2ba` on `main` (the repo is ~5.6
  GB — clone-impractical in the sandbox; see LEDGER F16 for why verification here uses
  the contents API, never the recursive `git/trees` endpoint). Wave-3 close-out append
  (wave receipt + wave report + tooling + manifest refresh): operator trace
  `1a16fa91188c8f3d`, same single-commit method. Wave-4 append (wave-4 deliverables +
  event logs + report + tooling + manifest v3 refresh): operator trace
  `1a16fbc3d4b5b749`, same single-commit method. Waves 5+ append on this convention.
