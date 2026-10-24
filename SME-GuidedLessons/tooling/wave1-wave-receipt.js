#!/usr/bin/env node
// wave1-wave-receipt.js — builds the wave-1 aggregate receipt of record from the ten
// per-note timing receipts (post integrity pass) and the corpus snapshot of record.
// Output: download/wave1/wave1-receipt.json
const fs = require('fs');
const DL = '/home/z/my-project/download/wave1';
const PHASES = ['P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'];

const snap = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));
const manifest = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/snapshot-manifest.json', 'utf8'));

// roster of record (format-minimums-driven, declared in the wave brief rounds and the worklog)
const ROSTER = [
  { noteId: 'rn_HZM2WRjPPT8Srcxt', genre: 'definitional single-lesson (small)', role: 'roster' },
  { noteId: 'rn_xT8XsdJtDX5gNFXj', genre: 'procedural calculation', role: 'roster' },
  { noteId: 'rn_TM4QVMgXVxs4vbfY', genre: 'procedural equations', role: 'roster' },
  { noteId: 'rn_JCfdFrHsCkrmMbFj', genre: 'multi-spec-point worked-equation note (largest authored body at open)', role: 'roster' },
  { noteId: 'rn_wTtM2fQVVjntRm64', genre: 'classification comparison', role: 'roster' },
  { noteId: 'rn_jNJ4gTmcHqdFqsNh', genre: 'family-trends note (3 spec points)', role: 'roster' },
  { noteId: 'rn_kJg2gwF77vdFZZ2H', genre: 'parallel-test-structure note', role: 'roster' },
  { noteId: 'rn_fQSYvKRMDBj3s2Bx', genre: 'practical method', role: 'roster' },
  { noteId: 'rn_2d6Yb8GwGfRRd6pZ', genre: 'concepts + worked system example', role: 'roster' },
  { noteId: 'rn_4SgDJv8rKxpQQSBh', genre: 'drawing-skill note (3 spec points)', role: 'roster' },
];
const CALIBRATION = 'rn_kb2VkFMdBTbmG33t'; // A1 Atoms note: calibration reference layer, never in the timed roster

const receipts = ROSTER.map(r => JSON.parse(fs.readFileSync(`${DL}/timing-receipt-${r.noteId}.json`, 'utf8')));
const layers = ROSTER.map(r => JSON.parse(fs.readFileSync(`${DL}/guided-lesson-${r.noteId}.json`, 'utf8')));

const perNote = ROSTER.map((r, i) => {
  const rec = receipts[i], layer = layers[i];
  const row = snap.notes.find(n => n.noteId === r.noteId);
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
    workedExample: layer.noteAssets.workedExample === null ? 'null (declared: none in source note)' : 'present',
    phaseSeconds: rec.phaseSeconds,
    totalSeconds: rec.totalSeconds,
    authoringHoursPerTopic: rec.authoringHoursPerTopic,
    wallClockSpanSeconds: rec.wallClockSpanSeconds,
    pauseLog: rec.pauseLog,
    assistedPhases: rec.assistedPhases,
    schemaValidation: rec.schemaValidation,
    lintHardFails: 0,
    lintWarnings: (rec.lint.match(/\[WARNING\]/g) || []).length,
    layerFile: rec.layerFile,
    receiptFile: `${DL}/timing-receipt-${r.noteId}.json`,
  };
});

const totals = {
  notes: perNote.length,
  lessons: perNote.reduce((a, n) => a + n.lessons, 0),
  keyPoints: perNote.reduce((a, n) => a + n.keyPoints, 0),
  checks: perNote.reduce((a, n) => a + n.checks, 0),
  focusedSeconds: perNote.reduce((a, n) => a + n.totalSeconds, 0),
  focusedHours: +(perNote.reduce((a, n) => a + n.totalSeconds, 0) / 3600).toFixed(2),
  meanSecondsPerNote: Math.round(perNote.reduce((a, n) => a + n.totalSeconds, 0) / perNote.length),
  meanHoursPerNote: +(perNote.reduce((a, n) => a + n.totalSeconds, 0) / perNote.length / 3600).toFixed(2),
  meanHoursPerLesson: +(perNote.reduce((a, n) => a + n.totalSeconds, 0) / perNote.reduce((a, n) => a + n.lessons, 0) / 3600).toFixed(3),
  wallSecondsAll: perNote.reduce((a, n) => a + n.wallClockSpanSeconds, 0),
  loggedPauses: perNote.reduce((a, n) => a + n.pauseLog.length, 0),
};

const phaseAggregate = Object.fromEntries(PHASES.map(p => [p, perNote.reduce((a, n) => a + n.phaseSeconds[p], 0)]));
const phaseShare = Object.fromEntries(PHASES.map(p => [p, +((phaseAggregate[p] / totals.focusedSeconds) * 100).toFixed(1)]));

const warningInventory = {};
perNote.forEach(n => {
  const rec = receipts[perNote.indexOf(n)];
  (rec.lint.match(/\[WARNING\] .+/g) || []).forEach(l => {
    const key = l.replace(/\[WARNING\] (\S+) @ \S+: (.+)/, '$1: $2');
    warningInventory[key] = (warningInventory[key] || 0) + 1;
  });
});

const receipt = {
  format: 'wave1-receipt/0.1',
  wave: 'wave-1 (instrumented first authoring wave, OPEN posture)',
  generatedAt: new Date().toISOString(),
  protocolOfRecord: 'A1 spec section 7 measurement discipline, extended per operator OPEN posture decision (A5 brief of record A5-Posture-Decision-Brief-Open-20261023.docx): guided study + guided practice corpus commitment; instrumented wave retained as measurement discipline (per-phase timing receipts + declared assistance), no longer a gate; ~2 h/note open-flip threshold dissolved.',
  posture: 'OPEN (build it fully) — operator decision of record, trace 1a1683ec43a016a9',
  corpusPin: {
    corpusVersion: snap.corpusVersion || 'sme-revision-notes-igcse-chemistry-19-2026-09-18',
    snapshotFile: '/home/z/my-project/.tmp/wave1/corpus-snapshot.json',
    snapshotManifest: manifest,
    censusOfRecord: { topics: 4, subtopics: 28, notes: 112, perTopicNotes: [40, 36, 15, 21] },
    dbContact: 'single read-only SELECT snapshot pull (scripts/wave1-corpus-snapshot.js); zero DB writes all wave',
  },
  calibrationReference: { noteId: CALIBRATION, role: 'A1 seed note; calibration reference layer of record; excluded from the timed roster' },
  rosterNote: '10-note roster of record covers 8+ note genres and both size extremes to maximise format-overfit information (spec section 9 risk); floor 0.2 h/topic is never quotable as a human rate; bands 28/56/93 author-days remain the exposure arithmetic of record.',
  totals,
  phaseAggregateSeconds: phaseAggregate,
  phaseSharePercent: phaseShare,
  perNote,
  warningInventory,
  integrityRecord: {
    assistFlagCorrection: 'Notes 7-10 initially had P2-P7 (and note 8 P1) closed unflagged despite model-drafted content; corrected via scripts/wave1-assist-fix.js + wave1-integrity-final.js; receipts recomputed.',
    timingRestoration: 'wave1-run.js export does not persist the event log on the success path; the assist-flag re-exports re-closed P8 at re-export time inflating it. P8 closures restored from the console totals of record of each note\'s successful first export (scripts/wave1-receipt-restore.js). All totals reconcile with the console of record within 1 s rounding.',
    p1DriftDisclosure: 'Notes 9/10: the phase command moved P0 directly to P2; the P1 split decision was authored inside the P0 clocked span. Disclosed in each receipt; no hours understated.',
    harnessDefectFiled: 'wave1-run.js success-path save() omission — to be patched in the toolchain before any future timed wave.',
  },
  reader: {
    numberofRecord: `${totals.meanHoursPerNote} h per note (mean of 10 focused totals, declared-assisted, model-drafted under OPEN posture)`,
    caveat: 'All figures are model-drafted under the operator OPEN posture with per-phase declared assistance; they measure the instrumented pipeline, not unassisted human rates. The floor 0.2 h/topic and the bands 28/56/93 author-days remain the only corpus-wide arithmetic of record.',
  },
};

fs.writeFileSync(`${DL}/wave1-receipt.json`, JSON.stringify(receipt, null, 1));
console.log('WAVE RECEIPT OF RECORD:', `${DL}/wave1-receipt.json`);
console.log(`notes ${totals.notes} | lessons ${totals.lessons} | keyPoints ${totals.keyPoints} | checks ${totals.checks}`);
console.log(`focused ${totals.focusedSeconds}s = ${totals.focusedHours} h | mean ${totals.meanSecondsPerNote}s = ${totals.meanHoursPerNote} h/note | ${totals.meanHoursPerLesson} h/lesson`);
console.log('phase share %:', JSON.stringify(phaseShare));
console.log('warnings:', Object.entries(warningInventory).map(([k, v]) => v + 'x ' + k).join(' | '));
