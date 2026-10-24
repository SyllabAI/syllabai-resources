#!/usr/bin/env node
// wave2-wave-receipt.js — builds the wave-2 aggregate receipt of record from the twelve
// per-note timing receipts, the twelve exported layers, the pinned corpus snapshot and the
// twelve persisted event logs. Wave-1 pattern (scripts/wave1-wave-receipt.js), with three
// wave-2-specific duties the close-out owes the pacing file's RECALIBRATION POINTS clause:
//   1. recompute mean s/note, s/ch and phase shares from THIS wave's receipts;
//   2. disclose the drift against the wave-1 estimators, with the event-log ground truth
//      that explains it (pre-write batch flow: P0-P7 closures are ms-scale wave-wide);
//   3. record the absorption decision of record (estimator basis freeze).
// Also reconciles the wave's lint warning inventory against the round-by-round narrative
// tally (they differ: 6 designed lines vs the narrative "4"; receipts are authoritative).
// Output: download/wave2/wave2-receipt.json
const fs = require('fs');
const crypto = require('crypto');

const DL = '/home/z/my-project/download/wave2';
const RUNS = '/home/z/my-project/.tmp/wave2/runs';
const SNAP = '/home/z/my-project/.tmp/wave1/corpus-snapshot.json';
const MAN = '/home/z/my-project/.tmp/wave1/snapshot-manifest.json';
const PHASES = ['P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'];

// register of record: wave-2 order of authoring, cross-checked against the pacing file's
// wavePlan[0] register below (position, id, title, subtopic, bodyChars, specPoints).
const ROSTER = [
  { noteId: 'rn_2VnK66PqbvFKdKYt', title: 'The Three States of Matter', subtopic: 'States of Matter', bodyChars: 4876, specPointCodes: ['4CH1-1.1', '4CH1-1.2'], genre: 'definitional states + interconversion' },
  { noteId: 'rn_S7GPh8BBPBbmhYKm', title: 'Diffusion & Dilution', subtopic: 'States of Matter', bodyChars: 3150, specPointCodes: ['4CH1-1.3'], genre: 'process explanation (A1 named contingency note)' },
  { noteId: 'rn_cTk2cs2h2BKQ3y3B', title: 'Solubility', subtopic: 'States of Matter', bodyChars: 2515, specPointCodes: ['4CH1-1.4', '4CH1-1.5C', '4CH1-1.6C'], genre: 'concepts + solubility-curve reading, arithmetic example' },
  { noteId: 'rn_QVmDs8X4szpds3cP', title: 'Practical: Investigate the Solubility of a Solid in Water at a Specific Temperature', subtopic: 'States of Matter', bodyChars: 3308, specPointCodes: ['4CH1-1.5C', '4CH1-1.7C'], genre: 'practical method + percentage arithmetic' },
  { noteId: 'rn_TWGVV6RXN3Ktqb9h', title: 'Element, Compound or Mixture', subtopic: 'Elements, Compounds & Mixtures', bodyChars: 1615, specPointCodes: ['4CH1-1.8'], genre: 'classification, workedExample-null' },
  { noteId: 'rn_RvgxXR36425BFMcx', title: 'Pure Substance vs Mixture', subtopic: 'Elements, Compounds & Mixtures', bodyChars: 2317, specPointCodes: ['4CH1-1.8', '4CH1-1.9'], genre: 'comparison + melting/boiling evidence, arithmetic example' },
  { noteId: 'rn_YBWYstSRgM2QPzQq', title: 'Separation Techniques', subtopic: 'Elements, Compounds & Mixtures', bodyChars: 6829, specPointCodes: ['4CH1-1.10'], genre: 'five-technique procedural, largest of the wave' },
  { noteId: 'rn_R3ptwxGTTvdBFvyP', title: 'Interpreting Chromatograms', subtopic: 'Elements, Compounds & Mixtures', bodyChars: 3445, specPointCodes: ['4CH1-1.11', '4CH1-1.12'], genre: 'data reading + Rf arithmetic' },
  { noteId: 'rn_TsfqyK9BYMtN2Bfd', title: 'Practical: Investigating Paper Chromatography', subtopic: 'Elements, Compounds & Mixtures', bodyChars: 4079, specPointCodes: ['4CH1-1.10', '4CH1-1.13'], genre: 'practical method + error analysis, workedExample-null' },
  { noteId: 'rn_kb2VkFMdBTbmG33t', title: 'Atoms: Definitions & Structure', subtopic: 'Atomic Structure', bodyChars: 4984, specPointCodes: ['4CH1-1.14', '4CH1-1.15', '4CH1-1.16'], genre: 'calibration-note reuse (fixture L1) + counting particles' },
  { noteId: 'rn_vzGMZxqQtWYVWB7h', title: 'Calculate Relative Atomic Mass', subtopic: 'Atomic Structure', bodyChars: 2471, specPointCodes: ['4CH1-1.16', '4CH1-1.17'], genre: 'weighted-average calculation, stepwise arithmetic' },
  { noteId: 'rn_b3XCzdtfQddbJjVf', title: 'Periodic Table: Basics', subtopic: 'The Periodic Table', bodyChars: 1618, specPointCodes: ['4CH1-1.18'], genre: 'arrangement vocabulary, smallest of the wave, workedExample-null' },
];

const sha256 = b => crypto.createHash('sha256').update(b).digest('hex');
const snap = JSON.parse(fs.readFileSync(SNAP, 'utf8'));
const manifest = JSON.parse(fs.readFileSync(MAN, 'utf8'));
const filePin = sha256(fs.readFileSync(SNAP));

// ---- load receipts + layers, hard-assert the invariants before minting anything ----
const receipts = ROSTER.map(r => JSON.parse(fs.readFileSync(`${DL}/timing-receipt-${r.noteId}.json`, 'utf8')));
const layers = ROSTER.map(r => JSON.parse(fs.readFileSync(`${DL}/guided-lesson-${r.noteId}.json`, 'utf8')));
const assert = (ok, msg) => { if (!ok) { console.error('ASSERT FAIL: ' + msg); process.exit(1); } };

ROSTER.forEach((r, i) => {
  const rec = receipts[i], layer = layers[i];
  assert(rec.noteId === r.noteId, `receipt order ${r.noteId}`);
  assert(layer.noteRef && layer.noteRef.noteId === r.noteId, `layer noteRef ${r.noteId}`);
  assert(layer.noteRef.corpusVersion === 'sme-revision-notes-igcse-chemistry-19-2026-09-18', `layer noteRef corpusVersion ${r.noteId}`);
  assert(layer.noteRef.subtopicTitle === r.subtopic, `layer noteRef subtopic ${r.noteId}`);
  assert(rec.noteTitle === r.title, `title ${r.noteId}: ${rec.noteTitle} vs ${r.title}`);
  assert(rec.bodyChars === r.bodyChars, `bodyChars ${r.noteId}`);
  assert(JSON.stringify(rec.specPointCodes) === JSON.stringify(r.specPointCodes), `spec codes ${r.noteId}`);
  assert(rec.corpusVersion === 'sme-revision-notes-igcse-chemistry-19-2026-09-18', `corpusVersion ${r.noteId}`);
  const row = snap.notes.find(n => n.noteId === r.noteId);
  assert(row && rec.bodySha256 === row.bodySha256, `bodySha256 vs snapshot ${r.noteId}`);
  assert(String(rec.schemaValidation).startsWith('PASS'), `schema PASS ${r.noteId}`);
  assert(JSON.stringify(rec.assistedPhases) === JSON.stringify(['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']), `assistedPhases P1..P7 ${r.noteId}`);
  assert(rec.pauseLog.length === 0, `zero pauses ${r.noteId}`);
  assert(layer.lessons.length === 2, `2 lessons ${r.noteId}`);
  assert(layer.lessons.reduce((a, L) => a + L.check.length, 0) === 10, `10 checks ${r.noteId}`);
  // cross-check the register against the pacing file of record
  const pacing = JSON.parse(fs.readFileSync('/home/z/my-project/download/wave-pacing-open-20261024.json', 'utf8'));
  const reg = pacing.wavePlan[0].register.find(e => e.noteId === r.noteId);
  assert(reg && reg.title === r.title && reg.bodyChars === r.bodyChars &&
    JSON.stringify(reg.specPointCodes) === JSON.stringify(r.specPointCodes), `wavePlan register ${r.noteId}`);
});

// ---- event-log ground truth (the flow-variation evidence) ----
const P0P7 = [];
const eventGroundTruth = ROSTER.map((r) => {
  const ev = JSON.parse(fs.readFileSync(`${RUNS}/${r.noteId}.events.json`, 'utf8'));
  let p17ms = 0, p8ms = 0, exports = 0, reExports = 0, p8Ends = 0;
  for (let i = 0; i < ev.length; i++) {
    const e = ev[i], prev = ev[i - 1];
    if (e.type === 'phase-end' && e.phase === 'P8') { p8Ends++; if (prev && prev.type === 'phase-start') p8ms += e.ts - prev.ts; }
    else if (e.type === 'phase-end' && e.phase && prev && prev.type === 'phase-start') p17ms += e.ts - prev.ts;
    if (e.type === 'export') { exports++; if (e.reExport) reExports++; }
  }
  assert(p8Ends === 1, `exactly ONE P8 phase-end (idempotence) ${r.noteId}`);
  P0P7.push(p17ms);
  return { noteId: r.noteId, p0toP7Ms: p17ms, p8WindowMs: p8ms, exportEvents: exports, reExportEvents: reExports };
});

// ---- per-note rows of record ----
const perNote = ROSTER.map((r, i) => {
  const rec = receipts[i], layer = layers[i];
  const we = layer.noteAssets.workedExample;
  return {
    noteId: r.noteId,
    noteTitle: rec.noteTitle,
    topicTitle: rec.topicTitle,
    subtopicTitle: rec.subtopicTitle,
    specPointCodes: rec.specPointCodes,
    bodyChars: rec.bodyChars,
    bodySha256: rec.bodySha256,
    rosterGenre: r.genre,
    lessons: layer.lessons.length,
    lessonTitles: layer.lessons.map(L => L.title),
    checks: layer.lessons.reduce((a, L) => a + L.check.length, 0),
    keyPoints: layer.lessons.reduce((a, L) => a + L.keyPoints.length, 0),
    workedExample: we === null ? 'null (designed declaration: none in source note)' : (String(rec.lint).includes('no arithmetic expression found') ? 'present, non-numeric (designed declaration)' : 'present, arithmetic verified'),
    phaseSeconds: rec.phaseSeconds,
    totalSeconds: rec.totalSeconds,
    wallClockSpanSeconds: rec.wallClockSpanSeconds,
    pauseLog: rec.pauseLog,
    assistedPhases: rec.assistedPhases,
    schemaValidation: rec.schemaValidation,
    lintHardFails: 0,
    lintWarningLines: (String(rec.lint).match(/\[WARNING\]/g) || []).length,
    layerFile: rec.layerFile,
    receiptFile: `${DL}/timing-receipt-${r.noteId}.json`,
  };
});

const totals = {
  notes: perNote.length,
  lessons: perNote.reduce((a, n) => a + n.lessons, 0),
  keyPoints: perNote.reduce((a, n) => a + n.keyPoints, 0),
  checks: perNote.reduce((a, n) => a + n.checks, 0),
  glossaryTerms: layers.reduce((a, l) => a + l.noteAssets.glossary.length, 0),
  bodyChars: perNote.reduce((a, n) => a + n.bodyChars, 0),
  focusedSeconds: perNote.reduce((a, n) => a + n.totalSeconds, 0),
  focusedHours: +(perNote.reduce((a, n) => a + n.totalSeconds, 0) / 3600).toFixed(2),
  meanSecondsPerNote: Math.round(perNote.reduce((a, n) => a + n.totalSeconds, 0) / perNote.length),
  wallSecondsAll: perNote.reduce((a, n) => a + n.wallClockSpanSeconds, 0),
  loggedPauses: perNote.reduce((a, n) => a + n.pauseLog.length, 0),
};
totals.meanSecondsPerLesson = +(totals.focusedSeconds / totals.lessons / 1).toFixed(1);
totals.secondsPerChar = +(totals.focusedSeconds / totals.bodyChars).toFixed(4);

const phaseAggregate = Object.fromEntries(PHASES.map(p => [p, perNote.reduce((a, n) => a + n.phaseSeconds[p], 0)]));
const phaseShare = Object.fromEntries(PHASES.map(p => [p, +((phaseAggregate[p] / totals.focusedSeconds) * 100).toFixed(1)]));

// ---- warning inventory + reconciliation against the round-by-round narrative tally ----
const warningInventory = {};
perNote.forEach((n, i) => {
  (String(receipts[i].lint).match(/\[WARNING\] (\S+) @ \S+: (.+)/g) || []).forEach(l => {
    const key = l.replace(/\[WARNING\] (\S+) @ \S+: (.+)/, '$1: $2');
    warningInventory[key] = (warningInventory[key] || 0) + 1;
  });
});

// ---- recalibration checkpoint (pacing file RECALIBRATION POINTS clause) ----
const W1 = { notes: 10, bodyChars: 40614, focusedSeconds: 2830, meanSecondsPerNote: 283, secondsPerChar: 0.0697, phaseSharePercent: { P0: 31.2, P1: 4.5, P2: 7.7, P3: 5.1, P4: 9.3, P5: 5.7, P6: 4.0, P7: 26.3, P8: 6.1 } };
const recalibration = {
  format: 'wave-recalibration/0.1 (pacing file wave-pacing-open/0.1, RECALIBRATION POINTS clause)',
  computedAt: new Date().toISOString(),
  recomputedFromWave2Receipts: {
    meanSecondsPerNote: totals.meanSecondsPerNote,
    secondsPerChar: totals.secondsPerChar,
    meanSecondsPerLesson: totals.meanSecondsPerLesson,
    phaseSharePercent: phaseShare,
  },
  eventLogGroundTruth: {
    method: 'phase spans recomputed from the twelve persisted event logs at millisecond resolution',
    p0toP7PerNoteMs: { min: Math.min(...P0P7), max: Math.max(...P0P7), note: 'sub-second on every note — phase-flag closures only; authoring sat outside the instrumented chain wave-wide' },
    p8WindowMs: { notes1to8: '28,648-77,386 ms (export machinery incl. in-flight fix and re-export cycles)', notes9to12: '23-26 ms (single-pass exports inside fully batched invocations)' },
    idempotence: 'exactly ONE P8 phase-end per note across all twelve logs, including the five notes that re-exported (re-export events never re-close a phase) — save() patch live proof, fifth and sixth consecutive production rounds',
  },
  wave1BasisOfRecord: W1,
  driftDisclosure: {
    meanSecondsPerNote: 'wave-2 nominal 35 s vs wave-1 283 s — an 8.1x deflation, structural not behavioural: the wave-2 clocks measure chain execution (flag closures + export windows), while wave-1 clocked authoring inside the phases',
    secondsPerChar: 'wave-2 0.0101 s/ch vs wave-1 0.0697 s/ch — same structural cause',
    phaseShare: 'wave-2 nominal P8 99.5% vs wave-1 P0 31.2% + P7 26.3% — the wave-2 share is an export-window artefact of the pre-write flow',
    refinementOfRoundNotes: 'the round-by-round narrative characterised notes 1-8 as sequential (29-78 s) vs notes 9-12 as batch (0 s); the event logs show both were pre-write batch chains — notes 1-8 simply carried heavy P8 windows (lint/fix/re-export cycles) while notes 9-12 exported single-pass. The event-log ground truth supersedes the round notes on this point.',
  },
  decisionOfRecord: [
    'The planning estimator of record REMAINS the wave-1 instrumented basis: 283 s/note, 0.0697 s/ch, wave-1 phase shares. Wave-2 receipts are reclassified of record as export-gate telemetry (schema verdict, lint state, chain-order discipline, idempotence proof, wall spans) and are NOT used to restate the pacing estimators.',
    'Re-timing a paced round is DECLINED: under the batch authoring posture the instrument would still measure the chain window, not authoring effort — a re-timed round produces another non-comparable number. Instrumented measurement comparable to wave-1 re-opens only if authoring returns inside the P0-P8 chain, which is an authoring-posture choice, not a measurement fix.',
    'Receipts continue on every future wave regardless (measurement discipline, not gate), each carrying its own event-log ground-truth block; focused tallies are never compared across waves with different authoring placement.',
    'The corpus-wide exposure arithmetic of record is unchanged: bands 28/56/93 author-days; the 0.2 h/topic floor remains never quotable as a human rate; wave means remain pipeline rates under declared assistance.',
  ],
};

// ---- receipt of record ----
const receipt = {
  format: 'wave2-receipt/0.1',
  wave: 'wave-2 (OPEN posture, topic T1 Principles of Chemistry, 12 notes of the 102-note remaining register)',
  generatedAt: new Date().toISOString(),
  protocolOfRecord: 'A1 spec section 7 measurement discipline under the operator OPEN posture (trace 1a1683ec43a016a9; brief A5-Posture-Decision-Brief-Open-20261023.docx), paced by wave-pacing-open/0.1; receipts are measurement discipline, not admission control; wave-2 receipts additionally carry the event-log ground truth per the recalibration checkpoint decision.',
  posture: 'OPEN (build it fully) — operator decision of record, trace 1a1683ec43a016a9',
  corpusPin: {
    corpusVersion: 'sme-revision-notes-igcse-chemistry-19-2026-09-18',
    snapshotFile: SNAP,
    snapshotFilePinSha256RecomputedThisRound: filePin,
    snapshotManifest: manifest,
    censusOfRecord: { topics: 4, subtopics: 28, notes: 112, perTopicNotes: [40, 36, 15, 21] },
    dbContact: 'ZERO database contact for the entire wave — all twelve bodies read from the pinned local snapshot (per-note SHA-verified before authoring each round); the wave-1 snapshot pull remains the single DB contact of the programme',
  },
  registerNote: 'the 12-note register is the pacing file wavePlan wave-2 register verbatim (cross-asserted at receipt build); it spans definitional, procedural, classification, comparison, practical, data-reading and calculation genres at both size extremes of the wave (6,829 ch Separation Techniques to 1,618 ch Periodic Table: Basics), and reuses the calibration note as a production authoring seed (note 10, L1).',
  totals,
  phaseAggregateSeconds: phaseAggregate,
  phaseSharePercent: phaseShare,
  eventLogGroundTruth: eventGroundTruth,
  flowVariationDisclosure: 'All twelve layers were authored outside the instrumented chain (pre-written working copies; the P0-P7 chain commands ran as ms-scale flag closures — 191-222 ms per note from the event logs). The receipts therefore record chain-execution time: P8 export windows of 29-78 s on notes 1-8 (which included in-flight lint/fix and re-export cycles) and 0 s (sub-resolution, 23-26 ms) on notes 9-12 (single-pass exports). The focused tally 418 s is chain telemetry, not authoring effort, and is NOT comparable to wave-1 — see the recalibration block, which owns the absorption decision.',
  recalibration,
  perNote,
  warningInventory,
  warningReconciliation: {
    inventoryOfRecord: '6 designed lint warning lines across 6 notes: workedExample-null declarations on notes 1, 2, 5, 9, 12 (sources carry no worked example) and one no-arithmetic declaration on note 7 (ported non-numeric example). Zero non-designed warnings survived to export on any note.',
    reconciliation: 'the round-by-round worklog tally from the 6/12 round onward read "4 designed warnings (notes 5, 7, 9, 12)", dropping notes 1-2, whose workedExample-null declarations were present in their receipts from first export (the 1-2 round stage summary itself counted "2 designed warnings"). The receipts are authoritative; the narrative tally is corrected to 6 by this receipt. The round verifier designed-or-none check passes on all twelve either way.',
  },
  integrityRecord: {
    warningTallyCorrection: 'see warningReconciliation — receipts authoritative over the narrative tally.',
    flowVariationRefinement: 'event-log ground truth supersedes the per-round sequential-vs-batch characterisation; disclosed in recalibration.driftDisclosure.',
    patchLiveProof: 'the wave-1 save() omission stayed patched all wave: blocked first exports (notes 1, 2, 4, 5, 7) persisted their event logs and every re-export ran idempotent (exactly one P8 phase-end per note; verified by assert at receipt build).',
    chainDiscipline: 'all twelve receipts carry assistedPhases exactly P1..P7 (P0 read-only unflagged, P8 closed mechanically by export); asserted at receipt build.',
    ajvPattern: 'ajv went missing at the harness path after sandbox recycles and was reinstalled --no-save before any export or verification, per the documented recurring pattern.',
    toolingNotes: 'arithmetic-scanner handling of record: note 8 formulated "Rf value: 3 / 6 = 0.5" to avoid the scanner latching a non-numeric lhs (Rf); note 11 formulated the rubidium weighted average stepwise ((72 x 85) + (28 x 87) = 8556; 8556 / 100 = 85.56; rounded in a stated step) because the flat one-line form mis-evaluates under operator precedence (6144.36).',
  },
  reader: {
    numberofRecord: 'no human-rate number is quotable from wave-2 (chain telemetry under pre-write batch flow, declared-assisted). Planning continues on the wave-1 instrumented basis (283 s/note, 0.0697 s/ch) and the 28/56/93 author-day bands.',
    caveat: 'All figures are model-drafted under the operator OPEN posture with per-phase declared assistance. The focused tally measures the P0-P8 chain window, not authoring effort, under the batch flow disclosed above; the exposure bands remain the only corpus-wide arithmetic of record.',
  },
};

const OUT = `${DL}/wave2-receipt.json`;
fs.writeFileSync(OUT, JSON.stringify(receipt, null, 1));
console.log('WAVE RECEIPT OF RECORD:', OUT);
console.log(`notes ${totals.notes} | lessons ${totals.lessons} | keyPoints ${totals.keyPoints} | checks ${totals.checks} | glossary ${totals.glossaryTerms} | bodyChars ${totals.bodyChars}`);
console.log(`focused(chain telemetry) ${totals.focusedSeconds}s | mean ${totals.meanSecondsPerNote}s/note | ${totals.secondsPerChar} s/ch | wall ${totals.wallSecondsAll}s | pauses ${totals.loggedPauses}`);
console.log('phase share % (nominal):', JSON.stringify(phaseShare));
console.log('P0-P7 event-log ms per note: min', Math.min(...P0P7), 'max', Math.max(...P0P7));
console.log('warnings:', Object.entries(warningInventory).map(([k, v]) => v + 'x ' + k.slice(0, 60)).join(' | '));
console.log('ALL ASSERTS PASSED — receipt minted');
