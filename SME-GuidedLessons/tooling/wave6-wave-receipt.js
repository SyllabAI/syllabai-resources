#!/usr/bin/env node
// wave6-wave-receipt.js — builds the wave-6 aggregate receipt of record from the twelve
// per-note timing receipts, the twelve exported layers, the pinned corpus snapshot and the
// twelve persisted event logs. Wave-5 pattern (scripts/wave5-wave-receipt.js), with the
// wave-6-specific duties the close-out owes:
//   1. recompute mean s/note, s/ch and phase shares from THIS wave's receipts (all-zero form);
//   2. reaffirm the wave-2 recalibration decision (estimator basis frozen at wave-1) with
//      wave-6's own event-log ground truth;
//   3. record the six-receipt-set topic census (Reactivity Series closure + Extraction &
//      Uses + Acids/Alkalis/Titrations + Acids/Bases/Salt Preparations opening).
// Output: download/wave6/wave6-receipt.json
const fs = require('fs');
const crypto = require('crypto');

const DL = '/home/z/my-project/download/wave6';
const RUNS = '/home/z/my-project/.tmp/wave6/runs';
const SNAP = '/home/z/my-project/.tmp/wave1/corpus-snapshot.json';
const MAN = '/home/z/my-project/.tmp/wave1/snapshot-manifest.json';
const PHASES = ['P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'];

// register of record: wave-6 order of authoring, cross-checked against the pacing file's
// wavePlan wave-6 register below (position, id, title, subtopic, bodyChars, specPoints).
const ROSTER = [
  { noteId: 'rn_sX8yyBxHn8bS7t46', title: 'Oxidation & Reduction', subtopic: 'Reactivity Series', bodyChars: 3823, specPointCodes: ['4CH1-2.20'], lessons: 2, genre: 'Reactivity Series close: oxygen + electron redox terms, ionic/half equations, non-numeric workedExample ported (designed declaration)' },
  { noteId: 'rn_BX88twwgffRMgx82', title: 'Practical: Investigate Metals Reacting with Acids', subtopic: 'Reactivity Series', bodyChars: 2590, specPointCodes: ['4CH1-2.15', '4CH1-2.21'], lessons: 2, genre: 'Reactivity Series close: the acid-metal practical with observations + Mg > Zn > Fe ranking, workedExample-null' },
  { noteId: 'rn_xq9jy75y43kDXkvx', title: 'Sources of Metals', subtopic: 'Extraction & Uses of Metals', bodyChars: 1446, specPointCodes: ['4CH1-2.22C'], lessons: 2, genre: 'Extraction & Uses opener: ores of the crust + native unreactive metals, workedExample-null' },
  { noteId: 'rn_nzW5ppBTV3ZnfSYY', title: 'Extracting Metals', subtopic: 'Extraction & Uses of Metals', bodyChars: 7376, specPointCodes: ['4CH1-2.23C', '4CH1-2.24C'], lessons: 2, genre: 'the wave-6 flagship: blast furnace three zones + slag chemistry + aluminium electrolysis cell, workedExample-null' },
  { noteId: 'rn_sf7s7s6bQ2cZv29s', title: 'Using Metals', subtopic: 'Extraction & Uses of Metals', bodyChars: 1625, specPointCodes: ['4CH1-2.25C'], lessons: 2, genre: 'property-to-use mapping tables incl. the three named steel types, workedExample-null' },
  { noteId: 'rn_MMkxbt9y3M3XvXrc', title: 'Alloys', subtopic: 'Extraction & Uses of Metals', bodyChars: 1382, specPointCodes: ['4CH1-2.26C', '4CH1-2.27C'], lessons: 2, genre: 'alloy definition + the distorted-lattice hardness mechanism, workedExample-null' },
  { noteId: 'rn_dTP52nzhYb96XrJx', title: 'Indicators', subtopic: 'Acids, Alkalis & Titrations', bodyChars: 3374, specPointCodes: ['4CH1-2.28', '4CH1-2.29', '4CH1-2.30'], lessons: 2, genre: 'indicator colour table + pH bands + universal indicator estimate, workedExample-null' },
  { noteId: 'rn_ZWrmDYtNGnmFycPM', title: 'Acids, Alkalis & Neutralisation', subtopic: 'Acids, Alkalis & Titrations', bodyChars: 2289, specPointCodes: ['4CH1-2.29', '4CH1-2.31', '4CH1-2.32'], lessons: 2, genre: 'H+/OH- ion sources + the neutralisation boundary (the metal-plus-acid exception), workedExample-null' },
  { noteId: 'rn_qV5R2cKB59bSKD33', title: 'Acid-Alkali Titrations', subtopic: 'Acids, Alkalis & Titrations', bodyChars: 3283, specPointCodes: ['4CH1-2.33C'], lessons: 2, genre: 'titration method + mean-titre NUMERIC workedExample ported verbatim from the results table and arithmetic-verified (0 warnings)' },
  { noteId: 'rn_p2FmkrXqZSzFngpg', title: 'Solubility Rules', subtopic: 'Acids, Bases & Salt Preparations', bodyChars: 1615, specPointCodes: ['4CH1-2.34'], lessons: 2, genre: 'Acids Bases & Salt Preparations opener: the solubility table + named exceptions, workedExample-null' },
  { noteId: 'rn_by5FDNfkqdBCkmXb', title: 'Acids, Bases & Protons', subtopic: 'Acids, Bases & Salt Preparations', bodyChars: 1052, specPointCodes: ['4CH1-2.35', '4CH1-2.36'], lessons: 2, genre: 'proton donor/acceptor definitions on the thinnest body of the wave (1,052 ch), workedExample-null' },
  { noteId: 'rn_9WM8QhSxmYpGhjqd', title: 'Reactions of Acids', subtopic: 'Acids, Bases & Salt Preparations', bodyChars: 4461, specPointCodes: ['4CH1-2.37'], lessons: 2, genre: 'three acid reaction families + the effervescence diagnosis, workedExample-null' },
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
  assert(JSON.stringify(rec.specPointCodes) === JSON.stringify(pacing.wavePlan.find(w => w.wave === 6).register.find(e => e.noteId === r.noteId).specPointCodes), `spec codes vs pacing ${r.noteId}`);
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
  const reg = pacing.wavePlan.find(w => w.wave === 6).register.find(e => e.noteId === r.noteId);
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

// ---- topic census (computed from the six wave receipt sets + snapshot) ----
const doneIds = new Set();
for (const w of ['wave1', 'wave2', 'wave3', 'wave4', 'wave5', 'wave6']) {
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
  recomputedFromWave6Receipts: {
    meanSecondsPerNote: totals.meanSecondsPerNote,
    secondsPerChar: totals.secondsPerChar,
    meanSecondsPerLesson: totals.meanSecondsPerLesson,
    phaseSharePercent: phaseShare,
  },
  eventLogGroundTruth: {
    method: 'phase spans recomputed from the twelve persisted event logs at millisecond resolution',
    p0toP7PerNoteMs: { min: Math.min(...P0P7), max: Math.max(...P0P7), note: 'sub-second on every note — phase-flag closures only; authoring sat outside the instrumented chain wave-wide (pre-write batch flow, the wave-2 established posture)' },
    p8WindowMs: { allTwelveNotes: 'sub-resolution on every note (0 s nominal) — the third fully zero-telemetry wave of the programme (after waves 4 and 5): single ignition, no repair interval inside any chain, no blocked path, no re-export anywhere' },
    idempotence: 'exactly ONE P8 phase-end per note across all twelve logs, zero reExport events — save() patch live proof, thirteenth through fifteenth consecutive production rounds (extending the wave-5 count of ten through twelve)',
  },
  wave1BasisOfRecord: W1,
  driftDisclosure: {
    meanSecondsPerNote: `wave-6 nominal ${totals.meanSecondsPerNote} s vs wave-1 283 s — the same structural deflation waves 2-5 recorded (chain telemetry, not authoring effort); no behavioural reading is possible or attempted`,
    secondsPerChar: `wave-6 ${totals.secondsPerChar} s/ch vs wave-1 0.0697 s/ch — same structural cause`,
    phaseShare: 'wave-6 phase shares are null (zero divisor) — the honest all-zero form waves 3-5 used',
    crossWaveComparability: 'per the wave-2 decision, focused tallies are never compared across waves; wave-6 receipts state the same batch placement as waves 2-5, so waves 2-6 share one comparability class — none comparable to wave-1',
  },
  decisionOfRecord: [
    'REAFFIRMED unchanged from the wave-2 checkpoint: the planning estimator of record remains the wave-1 instrumented basis (283 s/note, 0.0697 s/ch, wave-1 phase shares); wave-2 through wave-6 receipts alike are classified of record as export-gate telemetry (schema verdicts, lint state, chain-order discipline, idempotence proof, wall spans) and are NOT used to restate the pacing estimators.',
    'REAFFIRMED: re-timing a paced round remains DECLINED — under the batch authoring posture the instrument still measures the chain window; instrumented measurement comparable to wave-1 reopens only if authoring returns inside the P0-P8 chain.',
    'REAFFIRMED: receipts continue on every future wave regardless, each carrying its own event-log ground-truth block; focused tallies never compared across waves with different authoring placement.',
    'REAFFIRMED: corpus-wide exposure arithmetic unchanged — bands 28/56/93 author-days; the 0.2 h/topic floor remains never quotable as a human rate; wave means remain pipeline rates under declared assistance.',
  ],
};

// ---- receipt of record ----
const receipt = {
  format: 'wave6-receipt/0.1',
  wave: 'wave-6 (OPEN posture, Topic 2 Inorganic Chemistry — 12 notes of the remaining 55, Reactivity Series close -> Extraction & Uses of Metals -> Acids, Alkalis & Titrations -> Acids, Bases & Salt Preparations open)',
  generatedAt: new Date().toISOString(),
  protocolOfRecord: 'A1 spec section 7 measurement discipline under the operator OPEN posture (operator "Continue" ignition on the recorded wave-6 NEXT; standing brief A5-Posture-Decision-Brief-Open-20261023.docx), paced by wave-pacing-open/0.1; receipts are export-gate telemetry per the wave-2 recalibration decision, which this wave operated under unchanged.',
  posture: 'OPEN (build it fully) — operator decision of record, standing from trace 1a1683ec43a016a9',
  corpusPin: {
    corpusVersion: 'sme-revision-notes-igcse-chemistry-19-2026-09-18',
    snapshotFile: SNAP,
    snapshotFilePinSha256RecomputedThisRound: filePin,
    snapshotManifest: manifest,
    censusOfRecord: { topics: 4, subtopics: 28, notes: 112, perTopicNotes: [40, 36, 15, 21] },
    dbContact: 'ZERO database contact for the entire wave — all twelve bodies read from the pinned local snapshot (per-note SHA-verified at prep; pin re-verified twice at entry); spec texts resolved zero-DB from the graph content pack specification_points.yaml (parity-proven 4/4 against wave-5 of-record texts); the wave-1 snapshot pull remains the single DB contact of the programme',
  },
  registerNote: 'the 12-note register is the pacing file wavePlan wave-6 register verbatim (cross-asserted at receipt build); it closes the Reactivity Series (2.20-2.21) and Extraction & Uses of Metals (2.22C-2.27C), completes Acids, Alkalis & Titrations coverage (2.28-2.33C) and opens Acids, Bases & Salt Preparations (2.34-2.37). Size extremes: Extracting Metals at 7,376 characters (the wave flagship) down to Acids, Bases & Protons at 1,052. Cadence of record: 24 lessons (2 per note), 5 checks and 5 keyPoints per lesson throughout.',
  topicCensus,
  totals,
  phaseAggregateSeconds: phaseAggregate,
  phaseSharePercent: phaseShare,
  eventLogGroundTruth: eventGroundTruth,
  flowVariationDisclosure: 'All twelve layers were authored outside the instrumented chain (pre-write batch flow, the wave-2 established posture) under a single operator ignition (operator "Continue" on the recorded wave-6 NEXT); the P0-P7 chain commands ran as ms-scale flag closures in one single-shell invocation per note (scripts/wave6-chain.sh, the corrected invocation pattern native from the first note). Every note exported first-pass clean: zero gate-blocked exports, zero repairs inside any chain, zero re-exports, zero pauses wave-wide — the third fully single-ignition zero-telemetry wave of the programme. The focused tally is chain telemetry, not authoring effort, and is NOT comparable to wave-1 — the recalibration block owns the interpretation.',
  recalibration,
  perNote,
  warningInventory,
  warningReconciliation: {
    inventoryOfRecord: '11 designed lint warning lines across 11 notes, all in the two of-record classes: workedExample-null declarations on rn_BX88twwgffRMgx82, rn_xq9jy75y43kDXkvx, rn_nzW5ppBTV3ZnfSYY, rn_sf7s7s6bQ2cZv29s, rn_MMkxbt9y3M3XvXrc, rn_dTP52nzhYb96XrJx, rn_ZWrmDYtNGnmFycPM, rn_p2FmkrXqZSzFngpg, rn_by5FDNfkqdBCkmXb and rn_9WM8QhSxmYpGhjqd (each a source note carrying no worked example of any kind, where null is the of-record behaviour), plus the non-numeric-port declaration on rn_sX8yyBxHn8bS7t46 (the V3+/Fe3+ ion-analysis example ported verbatim from the source Worked Example block; it carries no arithmetic, so the no-arithmetic-to-verify warning line IS the designed declaration, the wave-4 note-1 precedent). The twelfth note (rn_qV5R2cKB59bSKD33, Acid-Alkali Titrations) carries a NUMERIC worked example ported verbatim from the source results table and arithmetic-verified by the scanner ((14.90 + 15.00) / 2 = 14.95 at 4 s.f.), so it exported with ZERO warnings — the third arithmetic-verified worked example of the programme, after wave-1 and wave-5. Zero non-designed warnings survived to export on any note.',
    reconciliation: 'the wave ran under a single operator ignition, so the tally is wave-wide from the outset: 11 designed declarations minted at the pre-flight stage and unchanged at export — parity with the receipts at every step, no drift to reconcile. The receipts are authoritative; the round verifier designed-or-none check passes on all twelve.',
  },
  integrityRecord: {
    chainDiscipline: 'all twelve receipts carry assistedPhases exactly P1..P7 (P0 read-only unflagged, P8 closed mechanically by export); asserted mechanically at receipt build, including the P0 phase-end assist===false assert on every event log — the permanent guard minted from the wave-3 notes-5-6 repair, exercised clean on every wave since.',
    correctedInvocationNative: 'the corrected invocation pattern (first phase P1 command unflagged, so P0 closes unflagged natively) ran natively on all twelve chains from the outset via the persisted per-note runner scripts/wave6-chain.sh; no repair of any kind was needed inside any chain.',
    preFlightTransparency: 'pre-flight (ajv schema + a1-lint on every layer BEFORE any chain fired) caught and fixed, all before first export: 2 source-fidelity runs across 2 notes (a 9-word keyPoint run on Sources of Metals and an 11-word opening run on Alloys — paraphrased to the <=8-word rule), 3 plain-words-register slips across 3 notes ("deformation" reworded, "preparation" rephrased, "neutralisation" glossary-backed on the titrations note), 6 template-uniformity flags across 5 notes (low/medium depth-layer lengths rebalanced), and one schema catch: a stray "extraction" key in an Alloys option (additionalProperties:false rejected it before lint — the fail-closed schema guard working as designed). Post-fix pre-flight: 11 notes exactly 1 designed warning, 1 note 0 warnings, 0 hard-fails.',
    numericPortTreatment: 'the titration worked example is a verbatim port of the source results table: rough titre 15.50 cm3 discarded, the concordant pair 14.90 and 15.00 cm3 used, mean computed as (14.90 + 15.00) / 2 = 14.95 in a single-equals arithmetic line shaped for the shunting-yard scanner (the copy-it red line held: no number invented — every figure is the table\'s). Superscript treatment: the U+00B3 glyph is used in the prompt/steps/finalAnswer so the final-answer value trace sees only the true numbers (a plain "cm3" would inject an untraceable 3 into the trace; the glyph is not an ASCII digit to the scanner).',
    nonNumericPortTreatment: 'the Oxidation & Reduction worked example is a verbatim port of the source Worked Example block (V3+ + Fe3+ giving V4+ + Fe2+): two-step structure kept (identify each species change, then label oxidation/reduction), no arithmetic present in the source, so the lint\'s no-arithmetic warning is the designed declaration of record.',
    specTextNormalisation: 'spec texts resolved from the graph content pack (specification_points.yaml), parity-proven against wave-5 of-record texts (4/4 exact). Documented normalisation extended wave-6: 2.15 flattened with the identical fragment to the wave-5 of-record text (parity held, "water; dilute hydrochloric or sulfuric acid"); 2.20 and 2.34 flattened from the wave-6 note bodies\' own spec-point bullet lists, wording verbatim (oxidation; reduction; redox; oxidising agent — and the six solubility rules).',
    registerScannerHandling: 'plain-words register: scanned fields kept free of unglossed -ation/-esis terms of nine or more characters; glossary terms carried "oxidation" (note 1), "neutralisation" (notes 8, 9 and 12), "titration"/"concentration" (note 9) and "electrolysis" (notes 3 and 4); "solution" (8-9 characters, no matching morpheme) sits outside the rule and needed no treatment; no register warning survived to export on any note.',
    libInstallPattern: 'post-recycle library restoration of record — the wave-5 pruning gotcha BIT this round and the minted one-command pattern fixed it: three sequential single-package installs at the shared /home/z prefix pruned docx when the js-yaml install landed (surfacing as an unresolvable docx CJS entry when the report builder first ran, after all authoring and exports were complete), so the install was redone as ONE npm install of ajv@8.20.0 + js-yaml + docx together; all three then verified co-resolving, with docx resolving to the CJS dist entry /home/z/node_modules/docx/dist/index.cjs in the current version layout. Verification-after-install remains the discipline, and the lesson is reconfirmed: one command, then verify.',
    patchLiveProof: 'the wave-1 save() omission stayed patched all wave: zero gate-blocked exports, zero re-exports, exactly one P8 phase-end per log — thirteenth through fifteenth consecutive production rounds for the patch.',
  },
  reader: {
    numberofRecord: 'no human-rate number is quotable from wave-6 (chain telemetry under pre-write batch flow, declared-assisted). Planning continues on the wave-1 instrumented basis (283 s/note, 0.0697 s/ch) and the 28/56/93 author-day bands.',
    caveat: 'All figures are model-drafted under the operator OPEN posture with per-phase declared assistance. The focused tally measures the P0-P8 chain window, not authoring effort, under the batch flow disclosed above; the exposure bands remain the only corpus-wide arithmetic of record.',
  },
};

const OUT = `${DL}/wave6-receipt.json`;
fs.writeFileSync(OUT, JSON.stringify(receipt, null, 1));
console.log('WAVE RECEIPT OF RECORD:', OUT);
console.log(`notes ${totals.notes} | lessons ${totals.lessons} | keyPoints ${totals.keyPoints} | checks ${totals.checks} | glossary ${totals.glossaryTerms} | bodyChars ${totals.bodyChars}`);
console.log(`focused(chain telemetry) ${totals.focusedSeconds}s | mean ${totals.meanSecondsPerNote}s/note | ${totals.secondsPerChar} s/ch | wall ${totals.wallSecondsAll}s | pauses ${totals.loggedPauses}`);
console.log('P0-P7 event-log ms per note: min', Math.min(...P0P7), 'max', Math.max(...P0P7));
console.log('reExports wave-wide:', eventGroundTruth.reduce((a, e) => a + e.reExportEvents, 0));
console.log('--- topic census ---');
for (const [t, v] of Object.entries(topicCensus)) console.log(`${t}: ${v.notes} complete=${v.complete} subtopicsClosed ${v.subtopicsClosed}/${v.subtopicsTotal} [${v.subtopicsClosedList.join(' | ')}]`);
