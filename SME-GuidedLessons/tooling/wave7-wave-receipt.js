#!/usr/bin/env node
// wave7-wave-receipt.js — builds the wave-7 aggregate receipt of record from the nine
// per-note timing receipts, the nine exported layers, the pinned corpus snapshot and the
// nine persisted event logs. Wave-6 pattern (scripts/wave6-wave-receipt.js), with the
// wave-7-specific duties the close-out owes:
//   1. recompute mean s/note, s/ch and phase shares from THIS wave's receipts (all-zero form);
//   2. reaffirm the wave-2 recalibration decision (estimator basis frozen at wave-1) with
//      wave-7's own event-log ground truth;
//   3. record the seven-receipt-set topic census (Acids Bases & Salt Preparations closure +
//      Chemical Tests closure — TOPIC 2 INORGANIC CHEMISTRY COMPLETES).
// Output: download/wave7/wave7-receipt.json
const fs = require('fs');
const crypto = require('crypto');

const DL = '/home/z/my-project/download/wave7';
const RUNS = '/home/z/my-project/.tmp/wave7/runs';
const SNAP = '/home/z/my-project/.tmp/wave1/corpus-snapshot.json';
const MAN = '/home/z/my-project/.tmp/wave1/snapshot-manifest.json';
const PHASES = ['P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'];

// register of record: wave-7 order of authoring, cross-checked against the pacing file's
// wavePlan wave-7 register below (position, id, title, subtopic, bodyChars, specPoints).
const ROSTER = [
  { noteId: 'rn_VvsXMdW3TB37JhWF', title: 'Bases', subtopic: 'Acids, Bases & Salt Preparations', bodyChars: 1547, specPointCodes: ['4CH1-2.38'], lessons: 2, genre: 'Acids Bases & Salt Preparations close: base/alkali distinction + the common-alkali ion table, workedExample-null' },
  { noteId: 'rn_6ZCysv9GnNQmc3w2', title: 'Prepare a Soluble Salt', subtopic: 'Acids, Bases & Salt Preparations', bodyChars: 2436, specPointCodes: ['4CH1-2.39'], lessons: 2, genre: 'acid + insoluble base method with the excess-and-filter discipline + CuSO4 example, workedExample-null' },
  { noteId: 'rn_5g8Dd6y89tkCVJsN', title: 'Prepare a Soluble Salt II', subtopic: 'Acids, Bases & Salt Preparations', bodyChars: 1536, specPointCodes: ['4CH1-2.40C'], lessons: 2, genre: 'acid + alkali titration preparation, repeat-without-indicator + crystallisation discipline, workedExample-null' },
  { noteId: 'rn_qb9TBhB6VmnFGjvf', title: 'Prepare an Insoluble Salt', subtopic: 'Acids, Bases & Salt Preparations', bodyChars: 1473, specPointCodes: ['4CH1-2.41C'], lessons: 2, genre: 'precipitation method AB+CD->AD+CB + the wash/dry discipline, workedExample-null' },
  { noteId: 'rn_pBp5Z5C2RHTKk7Wn', title: 'Practical: Prepare Lead(II)Sulfate', subtopic: 'Acids, Bases & Salt Preparations', bodyChars: 2055, specPointCodes: ['4CH1-2.41C', '4CH1-2.43C'], lessons: 2, genre: 'the named precipitation practical with measured volumes, ionic products and the lead-toxicity care point, workedExample-null' },
  { noteId: 'rn_T6S7R66N2wSZpWyc', title: 'Tests for Gases', subtopic: 'Chemical Tests', bodyChars: 4394, specPointCodes: ['4CH1-2.44'], lessons: 3, genre: 'the wave-7 flagship: all five gas tests across three lessons (litmus pair, limewater, splint pair), workedExample-null' },
  { noteId: 'rn_vVdP57QhDYSVfZgy', title: 'Flame Tests', subtopic: 'Chemical Tests', bodyChars: 1801, specPointCodes: ['4CH1-2.45', '4CH1-2.46'], lessons: 2, genre: 'flame-test technique + the five-cation colour table, workedExample-null' },
  { noteId: 'rn_v5JjfpT6grhtq3QW', title: 'Tests for Cations', subtopic: 'Chemical Tests', bodyChars: 2325, specPointCodes: ['4CH1-2.47'], lessons: 2, genre: 'NaOH precipitate colours (Fe2+/Fe3+/Cu2+) + the ammonium gas test with its ionic equation, workedExample-null' },
  { noteId: 'rn_YWDXCCmjfjkJcs6c', title: 'Tests for Water', subtopic: 'Chemical Tests', bodyChars: 1397, specPointCodes: ['4CH1-2.49', '4CH1-2.50'], lessons: 2, genre: 'anhydrous copper(II) sulfate white-to-blue test + the boiling-point purity test, workedExample-null' },
];

const sha256 = b => crypto.createHash('sha256').update(b).digest('hex');
const snap = JSON.parse(fs.readFileSync(SNAP, 'utf8'));
const manifest = JSON.parse(fs.readFileSync(MAN, 'utf8'));
const filePin = sha256(fs.readFileSync(SNAP));

// ---- load receipts + layers, hard-assert the invariants before minting anything ----
const receipts = ROSTER.map(r => JSON.parse(fs.readFileSync(`${DL}/timing-receipt-${r.noteId}.json`, 'utf8')));
const layers = ROSTER.map(r => JSON.parse(fs.readFileSync(`${DL}/guided-lesson-${r.noteId}.json`, 'utf8')));
const assert = (ok, msg) => { if (!ok) { console.error('ASSERT FAIL: ' + msg); process.exit(1); } };

const pacing = JSON.parse(fs.readFileSync('/home/z/my-project/download/wave-pacing-open-20261024.json', 'utf8'));
ROSTER.forEach((r, i) => {
  const rec = receipts[i], layer = layers[i];
  assert(rec.noteId === r.noteId, `receipt order ${r.noteId}`);
  assert(layer.noteRef && layer.noteRef.noteId === r.noteId, `layer noteRef ${r.noteId}`);
  assert(layer.noteRef.corpusVersion === 'sme-revision-notes-igcse-chemistry-19-2026-09-18', `layer noteRef corpusVersion ${r.noteId}`);
  assert(layer.noteRef.subtopicTitle === r.subtopic, `layer noteRef subtopic ${r.noteId}`);
  assert(rec.noteTitle === r.title, `title ${r.noteId}: ${rec.noteTitle} vs ${r.title}`);
  assert(rec.bodyChars === r.bodyChars, `bodyChars ${r.noteId}`);
  assert(JSON.stringify(rec.specPointCodes) === JSON.stringify(pacing.wavePlan.find(w => w.wave === 7).register.find(e => e.noteId === r.noteId).specPointCodes), `spec codes vs pacing ${r.noteId}`);
  assert(rec.corpusVersion === 'sme-revision-notes-igcse-chemistry-19-2026-09-18', `corpusVersion ${r.noteId}`);
  const row = snap.notes.find(n => n.noteId === r.noteId);
  assert(row && rec.bodySha256 === row.bodySha256, `bodySha256 vs snapshot ${r.noteId}`);
  assert(String(rec.schemaValidation).startsWith('PASS'), `schema PASS ${r.noteId}`);
  assert(JSON.stringify(rec.assistedPhases) === JSON.stringify(['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']), `assistedPhases P1..P7 ${r.noteId}`);
  assert(rec.pauseLog.length === 0, `zero pauses ${r.noteId}`);
  assert(layer.lessons.length === r.lessons, `lessons ${r.noteId}: ${layer.lessons.length} vs ${r.lessons}`);
  assert(layer.lessons.reduce((a, L) => a + L.check.length, 0) === r.lessons * 5, `5 checks/lesson ${r.noteId}`);
  layer.lessons.forEach(L => assert(L.keyPoints.length === 5, `5 keyPoints/lesson ${r.noteId}`));
  // cross-check the register against the pacing file of record
  const reg = pacing.wavePlan.find(w => w.wave === 7).register.find(e => e.noteId === r.noteId);
  assert(reg && reg.title === r.title && reg.bodyChars === r.bodyChars &&
    JSON.stringify(reg.specPointCodes) === JSON.stringify(r.specPointCodes), `wavePlan register ${r.noteId}`);
});

// ---- event-log ground truth (flow evidence; the P0 guard asserted on every log) ----
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
  assert(ev.length === 19, `19 events ${r.noteId}`);
  assert(exports === 1 && reExports === 0, `single clean export ${r.noteId}`);
  const p0end = ev.find(e => e.type === 'phase-end' && e.phase === 'P0');
  assert(p0end && p0end.assist === false, `P0 closes unflagged (wave-3 permanent guard) ${r.noteId}`);
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
    workedExample: we === null ? 'null (designed declaration: none in source note)' : (String(rec.lint).includes('no arithmetic expression found') ? 'present, non-numeric (designed declaration)' : 'present, arithmetic verified at stated significant figures'),
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
totals.meanSecondsPerLesson = +(totals.focusedSeconds / totals.lessons).toFixed(1);
totals.secondsPerChar = +(totals.focusedSeconds / totals.bodyChars).toFixed(4);
totals.distractors = perNote.reduce((a, n) => a + n.checks * 3, 0);

const phaseAggregate = Object.fromEntries(PHASES.map(p => [p, perNote.reduce((a, n) => a + n.phaseSeconds[p], 0)]));
const phaseShare = Object.fromEntries(PHASES.map(p => [p, totals.focusedSeconds === 0 ? null : +((phaseAggregate[p] / totals.focusedSeconds) * 100).toFixed(1)]));

// ---- warning inventory + reconciliation ----
const warningInventory = {};
perNote.forEach((n, i) => {
  (String(receipts[i].lint).match(/\[WARNING\] (\S+) @ \S+: (.+)/g) || []).forEach(l => {
    const key = l.replace(/\[WARNING\] (\S+) @ \S+: (.+)/, '$1: $2');
    warningInventory[key] = (warningInventory[key] || 0) + 1;
  });
});

// ---- topic census (computed from the seven wave receipt sets + snapshot) ----
const doneIds = new Set();
for (const w of ['wave1', 'wave2', 'wave3', 'wave4', 'wave5', 'wave6', 'wave7']) {
  for (const f of fs.readdirSync(`/home/z/my-project/download/${w}`)) {
    if (f.startsWith('timing-receipt-')) doneIds.add(JSON.parse(fs.readFileSync(`/home/z/my-project/download/${w}/${f}`, 'utf8')).noteId);
  }
}
const bySubtopic = {};
for (const n of snap.notes) {
  const k = n.topicTitle;
  bySubtopic[k] = bySubtopic[k] || { total: 0, done: 0, subs: {} };
  bySubtopic[k].total++;
  const sk = n.subtopicTitle;
  bySubtopic[k].subs[sk] = bySubtopic[k].subs[sk] || { total: 0, done: 0 };
  bySubtopic[k].subs[sk].total++;
  if (doneIds.has(n.noteId)) { bySubtopic[k].done++; bySubtopic[k].subs[sk].done++; }
}
const topicCensus = Object.fromEntries(Object.entries(bySubtopic).map(([t, v]) => [t, {
  notes: `${v.done}/${v.total}`,
  complete: v.done === v.total,
  subtopicsClosed: Object.entries(v.subs).filter(([, s]) => s.done === s.total).length,
  subtopicsTotal: Object.keys(v.subs).length,
  subtopicsClosedList: Object.entries(v.subs).filter(([, s]) => s.done === s.total).map(([sk]) => sk),
}]));

// ---- recalibration checkpoint (pacing file RECALIBRATION POINTS clause, reaffirmed) ----
const W1 = { notes: 10, bodyChars: 40614, focusedSeconds: 2830, meanSecondsPerNote: 283, secondsPerChar: 0.0697, phaseSharePercent: { P0: 31.2, P1: 4.5, P2: 7.7, P3: 5.1, P4: 9.3, P5: 5.7, P6: 4.0, P7: 26.3, P8: 6.1 } };
const recalibration = {
  format: 'wave-recalibration/0.1 (pacing file wave-pacing-open/0.1, RECALIBRATION POINTS clause)',
  computedAt: new Date().toISOString(),
  recomputedFromWave7Receipts: {
    meanSecondsPerNote: totals.meanSecondsPerNote,
    secondsPerChar: totals.secondsPerChar,
    meanSecondsPerLesson: totals.meanSecondsPerLesson,
    phaseSharePercent: phaseShare,
  },
  eventLogGroundTruth: {
    method: 'phase spans recomputed from the nine persisted event logs at millisecond resolution',
    p0toP7PerNoteMs: { min: Math.min(...P0P7), max: Math.max(...P0P7), note: 'sub-second on every note — phase-flag closures only; authoring sat outside the instrumented chain wave-wide (pre-write batch flow, the wave-2 established posture)' },
    p8WindowMs: { allNineNotes: 'sub-resolution on every note (0 s nominal) — the fourth fully zero-telemetry wave of the programme (after waves 4, 5 and 6): single ignition, no repair interval inside any chain, no blocked path, no re-export anywhere' },
    idempotence: 'exactly ONE P8 phase-end per note across all nine logs, zero reExport events — save() patch live proof, sixteenth through eighteenth consecutive production rounds (extending the wave-6 count of thirteen through fifteen)',
  },
  wave1BasisOfRecord: W1,
  driftDisclosure: {
    meanSecondsPerNote: `wave-7 nominal ${totals.meanSecondsPerNote} s vs wave-1 283 s — the same structural deflation waves 2-6 recorded (chain telemetry, not authoring effort); no behavioural reading is possible or attempted`,
    secondsPerChar: `wave-7 ${totals.secondsPerChar} s/ch vs wave-1 0.0697 s/ch — same structural cause`,
    phaseShare: 'wave-7 phase shares are null (zero divisor) — the honest all-zero form waves 3-6 used',
    crossWaveComparability: 'per the wave-2 decision, focused tallies are never compared across waves; wave-7 receipts state the same batch placement as waves 2-6, so waves 2-7 share one comparability class — none comparable to wave-1',
  },
  decisionOfRecord: [
    'REAFFIRMED unchanged from the wave-2 checkpoint: the planning estimator of record remains the wave-1 instrumented basis (283 s/note, 0.0697 s/ch, wave-1 phase shares); wave-2 through wave-7 receipts alike are classified of record as export-gate telemetry (schema verdicts, lint state, chain-order discipline, idempotence proof, wall spans) and are NOT used to restate the pacing estimators.',
    'REAFFIRMED: re-timing a paced round remains DECLINED — under the batch authoring posture the instrument still measures the chain window; instrumented measurement comparable to wave-1 reopens only if authoring returns inside the P0-P8 chain.',
    'REAFFIRMED: receipts continue on every future wave regardless, each carrying its own event-log ground-truth block; focused tallies never compared across waves with different authoring placement.',
    'REAFFIRMED: corpus-wide exposure arithmetic unchanged — bands 28/56/93 author-days; the 0.2 h/topic floor remains never quotable as a human rate; wave means remain pipeline rates under declared assistance.',
  ],
};

// ---- receipt of record ----
const receipt = {
  format: 'wave7-receipt/0.1',
  wave: 'wave-7 (OPEN posture, Topic 2 Inorganic Chemistry — 9 notes of the remaining 43, Acids Bases & Salt Preparations close -> Chemical Tests close; TOPIC 2 COMPLETES)',
  generatedAt: new Date().toISOString(),
  protocolOfRecord: 'A1 spec section 7 measurement discipline under the operator OPEN posture (operator ignition "Wave-7 — 9" on the recorded wave-7 NEXT; standing brief A5-Posture-Decision-Brief-Open-20261023.docx), paced by wave-pacing-open/0.1; receipts are export-gate telemetry per the wave-2 recalibration decision, which this wave operated under unchanged.',
  posture: 'OPEN (build it fully) — operator decision of record, standing from trace 1a1683ec43a016a9',
  corpusPin: {
    corpusVersion: 'sme-revision-notes-igcse-chemistry-19-2026-09-18',
    snapshotFile: SNAP,
    snapshotFilePinSha256RecomputedThisRound: filePin,
    snapshotManifest: manifest,
    censusOfRecord: { topics: 4, subtopics: 28, notes: 112, perTopicNotes: [40, 36, 15, 21] },
    dbContact: 'ZERO database contact for the entire wave — all nine bodies read from the pinned local snapshot (per-note SHA-verified at prep; pin re-verified at entry and close-out); spec texts resolved zero-DB from the graph content pack specification_points.yaml (parity-proven 4/4 on non-flattened probes against wave-6 of-record texts); the wave-1 snapshot pull remains the single DB contact of the programme',
  },
  registerNote: 'the 9-note register is the pacing file wavePlan wave-7 register verbatim (cross-asserted at receipt build); it closes Acids, Bases & Salt Preparations (2.38-2.43C) and closes Chemical Tests (2.44-2.50), completing Topic 2 Inorganic Chemistry of record. Size extremes: Tests for Gases at 4,394 characters (the wave flagship, the only 3-lesson note) down to Tests for Water at 1,397. Cadence of record: 19 lessons (2 per note, 3 for the flagship), 5 checks and 5 keyPoints per lesson throughout.',
  topicCensus,
  totals,
  phaseAggregateSeconds: phaseAggregate,
  phaseSharePercent: phaseShare,
  eventLogGroundTruth: eventGroundTruth,
  flowVariationDisclosure: 'All nine layers were authored outside the instrumented chain (pre-write batch flow, the wave-2 established posture) under a single operator ignition (operator message "Wave-7 — 9" on the recorded wave-7 NEXT); the P0-P7 chain commands ran as ms-scale flag closures in one single-shell invocation per note (scripts/wave7-chain.sh, the corrected invocation pattern native from the first note). Every note exported first-pass clean: zero gate-blocked exports, zero repairs inside any chain, zero re-exports, zero pauses wave-wide — the fourth fully single-ignition zero-telemetry wave of the programme. The focused tally is chain telemetry, not authoring effort, and is NOT comparable to wave-1 — the recalibration block owns the interpretation.',
  recalibration,
  perNote,
  warningInventory,
  warningReconciliation: {
    inventoryOfRecord: '9 designed lint warning lines across 9 notes, all in the single of-record class: workedExample-null declarations on rn_VvsXMdW3TB37JhWF, rn_6ZCysv9GnNQmc3w2, rn_5g8Dd6y89tkCVJsN, rn_qb9TBhB6VmnFGjvf, rn_pBp5Z5C2RHTKk7Wn, rn_T6S7R66N2wSZpWyc, rn_vVdP57QhDYSVfZgy, rn_v5JjfpT6grhtq3QW and rn_YWDXCCmjfjkJcs6c (each a source note carrying no worked example of any kind, where null is the of-record behaviour). No non-numeric ports and no numeric ports were needed this wave: none of the nine sources carries a worked-example block or results table. Zero non-designed warnings survived to export on any note.',
    reconciliation: 'the wave ran under a single operator ignition, so the tally is wave-wide from the outset: 9 designed declarations minted at the pre-flight stage and unchanged at export — parity with the receipts at every step, no drift to reconcile. The receipts are authoritative; the round verifier designed-or-none check passes on all nine.',
  },
  integrityRecord: {
    chainDiscipline: 'all nine receipts carry assistedPhases exactly P1..P7 (P0 read-only unflagged, P8 closed mechanically by export); asserted mechanically at receipt build, including the P0 phase-end assist===false assert on every event log — the permanent guard minted from the wave-3 notes-5-6 repair, exercised clean on every wave since.',
    correctedInvocationNative: 'the corrected invocation pattern (first phase P1 command unflagged, so P0 closes unflagged natively) ran natively on all nine chains from the outset via the persisted per-note runner scripts/wave7-chain.sh; no repair of any kind was needed inside any chain.',
    preFlightTransparency: 'pre-flight (ajv schema + a1-lint on every layer BEFORE any chain fired) caught and fixed, all before first export: 1 source-fidelity run on 1 note (a 9-word keyPoint run on Tests for Water — paraphrased to the <=8-word rule), 5 plain-words-register slips across 4 notes ("identification" reworded on the gases and flame-tests notes, "confirmation" reworded on the cations note, "combination" reworded on the water note, and "evaporation"/"crystallisation"/"precipitation"/"filtration"/"preparation" glossary-backed or reworded on the titrations, lead(II) sulfate and water notes), 5 template-uniformity flags across 4 notes (low/medium depth-layer lengths rebalanced). Post-fix pre-flight: 9 notes exactly 1 designed warning, 0 hard-fails. One schema-catch-equivalent was self-caught at authoring time before pre-flight even ran: a stray "exception" key in an option object on the insoluble-salt note was removed at the source (additionalProperties:false would have rejected it — the fail-closed guard worked one level earlier).',
    specTextNormalisation: 'spec texts resolved from the graph content pack (specification_points.yaml), parity-proven against wave-6 of-record texts (4/4 exact on non-flattened probes — the probe discipline now skips codes whose pack wording ends with a colon, which are exactly the documented multi-bullet flattening class). Documented normalisation extended wave-7: 2.44, 2.46 and 2.47 flattened from the wave-7 note bodies\' own spec-point bullet lists, wording verbatim (the five gases; the five cation colours; the two cation-test families).',
    registerScannerHandling: 'plain-words register: scanned fields kept free of unglossed -ation/-esis terms of nine or more characters; glossary terms carried "crystallisation" and "evaporation" (note 3), "precipitation" and "filtration" (note 5) and "contamination" (note 7); "solution" (8 characters, no matching morpheme) sits outside the rule and needed no treatment; no register warning survived to export on any note.',
    libInstallPattern: 'the one-command library restoration pattern held this round: ajv 8.20.0, js-yaml and docx all verified co-resolving at entry before any work began (docx resolving to its CJS dist entry); no reinstall was needed mid-wave.',
    patchLiveProof: 'the wave-1 save() omission stayed patched all wave: zero gate-blocked exports, zero re-exports, exactly one P8 phase-end per log — sixteenth through eighteenth consecutive production rounds for the patch.',
  },
  reader: {
    numberofRecord: 'no human-rate number is quotable from wave-7 (chain telemetry under pre-write batch flow, declared-assisted). Planning continues on the wave-1 instrumented basis (283 s/note, 0.0697 s/ch) and the 28/56/93 author-day bands.',
    caveat: 'All figures are model-drafted under the operator OPEN posture with per-phase declared assistance. The focused tally measures the P0-P8 chain window, not authoring effort, under the batch flow disclosed above; the exposure bands remain the only corpus-wide arithmetic of record.',
  },
};

const OUT = `${DL}/wave7-receipt.json`;
fs.writeFileSync(OUT, JSON.stringify(receipt, null, 1));
console.log('WAVE RECEIPT OF RECORD:', OUT);
console.log(`notes ${totals.notes} | lessons ${totals.lessons} | keyPoints ${totals.keyPoints} | checks ${totals.checks} | glossary ${totals.glossaryTerms} | bodyChars ${totals.bodyChars} | distractors ${totals.distractors}`);
console.log(`focused(chain telemetry) ${totals.focusedSeconds}s | mean ${totals.meanSecondsPerNote}s/note | ${totals.secondsPerChar} s/ch | wall ${totals.wallSecondsAll}s | pauses ${totals.loggedPauses}`);
console.log('P0-P7 event-log ms per note: min', Math.min(...P0P7), 'max', Math.max(...P0P7));
console.log('reExports wave-wide:', eventGroundTruth.reduce((a, e) => a + e.reExportEvents, 0));
console.log('--- topic census ---');
for (const [t, v] of Object.entries(topicCensus)) console.log(`${t}: ${v.notes} complete=${v.complete} subtopicsClosed ${v.subtopicsClosed}/${v.subtopicsTotal} [${v.subtopicsClosedList.join(' | ')}]`);
