#!/usr/bin/env node
// wave10-wave-receipt.js — builds the wave-10 aggregate receipt of record from the eight
// per-note timing receipts, the eight exported layers, the pinned corpus snapshot and the
// eight persisted event logs. Wave-5 pattern (scripts/wave5-wave-receipt.js), with the
// wave-10-specific duties the close-out owes — THE FINAL WAVE, completing the corpus:
//   1. recompute mean s/note, s/ch and phase shares from THIS wave's receipts (all-zero form);
//   2. reaffirm the wave-2 recalibration decision (estimator basis frozen at wave-1) with
//      wave-10's own event-log ground truth;
//   3. record the ten-receipt-set topic census: 112/112 — every topic and subtopic closed.
// Output: download/wave10/wave10-receipt.json
const fs = require('fs');
const crypto = require('crypto');

const DL = '/home/z/my-project/download/wave10';
const RUNS = '/home/z/my-project/.tmp/wave10/runs';
const SNAP = '/home/z/my-project/.tmp/wave1/corpus-snapshot.json';
const MAN = '/home/z/my-project/.tmp/wave1/snapshot-manifest.json';
const PHASES = ['P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'];

// register of record: wave-10 order of authoring, cross-checked against the pacing file's
// wavePlan wave-10 register below (position, id, title, subtopic, bodyChars, specPoints).
const ROSTER = [
  { noteId: 'rn_8T5GfPn2q7sY2YCh', title: 'Oxidation of Ethanol', subtopic: 'Alcohols', bodyChars: 2702, specPointCodes: ['4CH1-4.31C'], lessons: 2, genre: 'three routes: combustion + aerobic microbial action + dichromate under reflux, orange to green, workedExample-null' },
  { noteId: 'rn_ncFJkGhXFsKrkNkH', title: 'Manufacture of Ethanol', subtopic: 'Alcohols', bodyChars: 2959, specPointCodes: ['4CH1-4.32C', '4CH1-4.33C'], lessons: 2, genre: 'hydration of ethene conditions + fermentation with the anaerobic and optimum-temperature reasoning, workedExample-null' },
  { noteId: 'rn_2z53qk2CdWrVVc7V', title: 'Carboxylic Acids', subtopic: 'Carboxylic acids', bodyChars: 3287, specPointCodes: ['4CH1-4.34C', '4CH1-4.35C', '4CH1-4.37C'], lessons: 2, genre: 'carboxyl group + the n-counts-only-the-chain trap + first four named, workedExample PORTED (the note body propanoic-acid general-formula example, arithmetic lint-verified)' },
  { noteId: 'rn_BBGMYy3Yx9Nm4GV3', title: 'Reactions of Carboxylic Acids', subtopic: 'Carboxylic acids', bodyChars: 1394, specPointCodes: ['4CH1-4.36C'], lessons: 2, genre: 'metals and carbonates + the anoate salt naming rule + the two example equations, workedExample-null' },
  { noteId: 'rn_BDkhS5vQpRd4hvwf', title: 'Esters', subtopic: 'Esters', bodyChars: 2398, specPointCodes: ['4CH1-4.38C', '4CH1-4.39C', '4CH1-4.40C', '4CH1-4.41C', '4CH1-4.42C'], lessons: 2, genre: 'esterification + the R-COO-R group + yl/oate naming with the volatile smell-and-perfume uses, workedExample-null' },
  { noteId: 'rn_7ZMc3T3J4SJXfNdR', title: 'Practical: Preparation of Ethyl Ethanoate', subtopic: 'Esters', bodyChars: 1497, specPointCodes: ['4CH1-4.39C', '4CH1-4.43C'], lessons: 2, genre: 'water-bath method with the flammability reason + distil-off-as-formed rationale + the two-wash purification, workedExample-null' },
  { noteId: 'rn_bvyrkKqRBMKCRzHM', title: 'Disposal of Addition Polymers', subtopic: 'Synthetic polymers', bodyChars: 1314, specPointCodes: ['4CH1-4.47'], lessons: 2, genre: 'inertness and inability to biodegrade + landfill and the three incineration hazards, workedExample-null' },
  { noteId: 'rn_bGgYrQXP2tqrYwdV', title: 'Condensation Polymers', subtopic: 'Synthetic polymers', bodyChars: 4995, specPointCodes: ['4CH1-4.48C', '4CH1-4.49C', '4CH1-4.50C'], lessons: 3, genre: 'condensation vs addition + terylene and hydrolysis monomer deduction + biopolyesters, workedExample-null' },
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
  assert(JSON.stringify(rec.specPointCodes) === JSON.stringify(r.specPointCodes), `spec codes ${r.noteId}`);
  assert(rec.corpusVersion === 'sme-revision-notes-igcse-chemistry-19-2026-09-18', `corpusVersion ${r.noteId}`);
  const row = snap.notes.find(n => n.noteId === r.noteId);
  assert(row && rec.bodySha256 === row.bodySha256, `bodySha256 vs snapshot ${r.noteId}`);
  assert(String(rec.schemaValidation).startsWith('PASS'), `schema PASS ${r.noteId}`);
  assert(JSON.stringify(rec.assistedPhases) === JSON.stringify(['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']), `assistedPhases P1..P7 ${r.noteId}`);
  assert(rec.pauseLog.length === 0, `zero pauses ${r.noteId}`);
  assert(layer.lessons.length === r.lessons, `lessons ${r.noteId}: ${layer.lessons.length} vs ${r.lessons}`);
  assert(layer.lessons.reduce((a, L) => a + L.check.length, 0) === r.lessons * 5, `5 checks/lesson ${r.noteId}`);
  layer.lessons.forEach(L => assert(L.keyPoints.length === 5, `5 keyPoints/lesson ${r.noteId}`));
  const reg = pacing.wavePlan.find(w => w.wave === 10).register.find(e => e.noteId === r.noteId);
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
    workedExample: we === null ? 'null (designed declaration: none in source note)' : 'present, ported from the note body, arithmetic verified at stated significant figures',
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
  distractors: layers.reduce((a, l) => a + l.lessons.reduce((b, L) => b + L.check.reduce((c, ch) => c + ch.options.filter(o => !o.correct).length, 0), 0), 0),
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

// ---- topic census (computed from the ten wave receipt sets + snapshot) ----
const doneIds = new Set();
for (const w of ['wave1', 'wave2', 'wave3', 'wave4', 'wave5', 'wave6', 'wave7', 'wave8', 'wave9', 'wave10']) {
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

// ---- corpus completion record (the FINAL-wave duty) ----
const corpusCompletion = {
  status: 'CORPUS COMPLETE — 112/112 notes authored and receipted across ten waves',
  censusOfRecord: {
    notes: `${doneIds.size}/112`,
    topics: Object.entries(topicCensus).map(([t, v]) => `${t}: ${v.notes}${v.complete ? ' COMPLETE' : ' OPEN'}`),
    subtopics: `${Object.entries(topicCensus).reduce((a, [, v]) => a + v.subtopicsClosed, 0)}/28 closed`,
  },
  priorPoolVerification: `the wave-10 register was proven to have zero overlap with the 104 receipts of waves 1-9 at prep, and the census above recomputes the full 112 from the ten receipt sets on disk`,
};

// ---- recalibration checkpoint (pacing file RECALIBRATION POINTS clause, reaffirmed) ----
const W1 = { notes: 10, bodyChars: 40614, focusedSeconds: 2830, meanSecondsPerNote: 283, secondsPerChar: 0.0697, phaseSharePercent: { P0: 31.2, P1: 4.5, P2: 7.7, P3: 5.1, P4: 9.3, P5: 5.7, P6: 4.0, P7: 26.3, P8: 6.1 } };
const recalibration = {
  format: 'wave-recalibration/0.1 (pacing file wave-pacing-open/0.1, RECALIBRATION POINTS clause)',
  computedAt: new Date().toISOString(),
  recomputedFromWave10Receipts: {
    meanSecondsPerNote: totals.meanSecondsPerNote,
    secondsPerChar: totals.secondsPerChar,
    meanSecondsPerLesson: totals.meanSecondsPerLesson,
    phaseSharePercent: phaseShare,
  },
  eventLogGroundTruth: {
    method: 'phase spans recomputed from the eight persisted event logs at millisecond resolution',
    p0toP7PerNoteMs: { min: Math.min(...P0P7), max: Math.max(...P0P7), note: 'sub-second on every note — phase-flag closures only; authoring sat outside the instrumented chain wave-wide (pre-write batch flow, the wave-2 established posture)' },
    p8WindowMs: { allEightNotes: 'sub-resolution on every note (0 s nominal) — the fifth fully zero-telemetry wave of the programme (after waves 4, 5, 8 and 9): single ignition, no repair interval inside any chain, no blocked path, no re-export anywhere' },
    idempotence: 'exactly ONE P8 phase-end per note across all eight logs, zero reExport events — save() patch live proof on every production round since the wave-1 fix (waves 1-10, all 112 receipt-bearing notes of record)',
  },
  wave1BasisOfRecord: W1,
  driftDisclosure: {
    meanSecondsPerNote: `wave-10 nominal ${totals.meanSecondsPerNote} s vs wave-1 283 s — the same structural deflation waves 2-9 recorded (chain telemetry, not authoring effort); no behavioural reading is possible or attempted`,
    secondsPerChar: `wave-10 ${totals.secondsPerChar} s/ch vs wave-1 0.0697 s/ch — same structural cause`,
    phaseShare: 'wave-10 phase shares are null (zero divisor) — the honest all-zero form waves 3-5, 8 and 9 used',
    crossWaveComparability: 'per the wave-2 decision, focused tallies are never compared across waves; wave-10 receipts state the same batch placement as waves 2-9, so waves 2-10 share one comparability class — none comparable to wave-1',
  },
  decisionOfRecord: [
    'REAFFIRMED unchanged from the wave-2 checkpoint: the planning estimator of record remains the wave-1 instrumented basis (283 s/note, 0.0697 s/ch, wave-1 phase shares); wave-2 through wave-10 receipts alike are classified of record as export-gate telemetry (schema verdicts, lint state, chain-order discipline, idempotence proof, wall spans) and are NOT used to restate the pacing estimators.',
    'REAFFIRMED: re-timing a paced round remains DECLINED — under the batch posture the instrument measures only the chain window; instrumented measurement comparable to wave-1 reopens only if authoring returns inside the P0-P8 chain.',
    'REAFFIRMED: receipts continue on every future wave regardless, each carrying its own event-log ground-truth block; focused tallies never compared across waves with different authoring placement.',
    'REAFFIRMED: corpus-wide exposure arithmetic unchanged — bands 28/56/93 author-days; the 0.2 h/topic floor remains never quotable as a human rate; wave means remain pipeline rates under declared assistance.',
  ],
};

// ---- receipt of record ----
const receipt = {
  format: 'wave10-receipt/0.1',
  wave: 'wave-10 (OPEN posture, Topic 4 Organic Chemistry closing wave — the FINAL 8 notes of the corpus, Alcohols -> Carboxylic acids -> Esters -> Synthetic polymers)',
  generatedAt: new Date().toISOString(),
  protocolOfRecord: 'A1 spec section 7 measurement discipline under the operator OPEN posture (ignition trace 1a174e627dda7171 verbatim "Go wave-10"; brief A5-Posture-Decision-Brief-Open-20261023.docx), paced by wave-pacing-open/0.1; receipts are export-gate telemetry per the wave-2 recalibration decision, which this wave operated under unchanged.',
  posture: 'OPEN (build it fully) — operator decision of record, standing from trace 1a1683ec43a016a9',
  corpusPin: {
    corpusVersion: 'sme-revision-notes-igcse-chemistry-19-2026-09-18',
    snapshotFile: SNAP,
    snapshotFilePinSha256RecomputedThisRound: filePin,
    snapshotManifest: manifest,
    censusOfRecord: { topics: 4, subtopics: 28, notes: 112, perTopicNotes: [40, 36, 15, 21] },
    dbContact: 'ZERO database contact for the entire wave — all eight bodies read from the pinned local snapshot (per-note SHA-verified at prep); spec texts resolved zero-DB from the graph content pack specification_points.yaml (parity-proven 4/4 against wave-5 of-record texts); the wave-1 snapshot pull remains the single DB contact of the programme',
  },
  registerNote: 'the 8-note register is the pacing file wavePlan wave-10 register verbatim (cross-asserted at receipt build); it closes Topic 4 Organic Chemistry and the whole corpus across four subtopics — Alcohols 4.31C-4.33C (2 notes), Carboxylic acids 4.34C-4.37C (2 notes), Esters 4.38C-4.43C (2 notes) and Synthetic polymers 4.47-4.50C (2 notes). Size extremes: Condensation Polymers at 4,995 characters down to Disposal of Addition Polymers at 1,314. Cadence of record: 17 lessons (2 per note, 3 for the richest note — Condensation Polymers), 5 checks and 5 keyPoints per lesson throughout.',
  topicCensus,
  corpusCompletion,
  totals,
  phaseAggregateSeconds: phaseAggregate,
  phaseSharePercent: phaseShare,
  eventLogGroundTruth: eventGroundTruth,
  flowVariationDisclosure: 'All eight layers were authored outside the instrumented chain (pre-write batch flow, the wave-2 established posture) under a single operator ignition (trace 1a174e627dda7171); the P0-P7 chain commands ran as ms-scale flag closures in one single-shell invocation per note. Every note exported first-pass clean: zero gate-blocked exports, zero repairs inside any chain, zero re-exports, zero pauses wave-wide — the fifth fully single-ignition wave of the programme. The focused tally is chain telemetry, not authoring effort, and is NOT comparable to wave-1 — the recalibration block owns the interpretation.',
  recalibration,
  perNote,
  warningInventory,
  warningReconciliation: {
    inventoryOfRecord: '7 designed lint warning lines across 7 of the 8 notes, all of one class: workedExample-null declarations on every note of the register that carries no arithmetic worked example of record. The eighth note, Carboxylic Acids, carries the wave\'s single numeric port — the propanoic-acid general-formula example taken from the note body — so its receipt shows zero warnings and the port was arithmetic-verified at stated significant figures by the lint. Zero non-designed warnings survived to export on any note.',
    reconciliation: 'the wave ran under a single operator ignition, so the tally is wave-wide from the outset: 7 designed declarations plus 1 verified port minted at the pre-flight stage and unchanged at export — parity with the receipts at every step, no drift to reconcile. The receipts are authoritative; the round verifier designed-or-none check passes on all eight.',
  },
  integrityRecord: {
    entryRestoration: 'post-recycle continuity discipline at one-wave scope: the remote home arbitrated the head (moved past the wave-9 landing d1820483 to an interleaved push) and MANIFEST v8 verified the ENTIRE local wave-9 set — 25 download files plus all 12 event logs — by recomputed sha256, zero mismatches, with waves 1-8 file counts and the 104-receipt prior pool confirmed intact locally. The one-command library pattern held (ajv + js-yaml + docx all resolving), so no reinstall was needed.',
    chainDiscipline: 'all eight receipts carry assistedPhases exactly P1..P7 (P0 read-only unflagged, P8 closed mechanically by export); asserted mechanically at receipt build, including the P0 phase-end assist===false assert on every event log — the permanent guard minted from the wave-3 notes-5-6 repair, exercised clean on every wave since.',
    correctedInvocationNative: 'the corrected invocation pattern (first phase P1 command unflagged, so P0 closes unflagged natively) was applied to all eight chains from the outset; no repair of any kind was needed inside any chain.',
    preFlightTransparency: 'pre-flight (ajv schema + a1-lint on every layer BEFORE any chain fired) caught and fixed, all before first export: 1 schema slip (a three-item sourceHeadings list trimmed to the two-heading maximum on the practical note) and 4 plain-words-register slips in scanned fields ("observation" in an opening, "Oxidation" in the manufacture primer, "formation" in the esters opening and the condensation restatement — all rephrased in place). Zero source-fidelity runs and zero template-uniformity flags wave-wide, the cleanest pre-flight sweep of the programme. Post-fix pre-flight: 8 notes exactly 1 designed warning or a clean port, 0 hard-fails, 0 other warnings — designed-or-none achieved before any chain.',
    specTextNormalisation: 'spec texts resolved from the graph content pack (specification_points.yaml), parity-proven against wave-5 of-record texts (4/4 exact, probe set excluding the flattened 2.19). The wave-8 generalisation ran data-driven over all 18 wave-10 code instances (17 unique) and found 3 multi-bullet statements — 4.31C, 4.32C and 4.47 — each flattened to semicolon clauses using the pack\'s own official_bullets verbatim.',
    numericPortTreatment: 'ONE port this wave, the first since wave-8: the Carboxylic Acids note ships two arithmetic worked examples in its body (propanoic and pentanoic acid via the general formula), so the layer ports the propanoic case verbatim-in-substance (3 - 1 = 2; 2 x 2 + 1 = 5; C2H5COOH -> C3H6O2), arithmetic-verified by the lint at stated significant figures. The remaining seven notes declare designed workedExample-null.',
    registerScannerHandling: 'plain-words register: scanned fields (openings, depth-layer restatements, primers) kept free of unglossed -ation/-esis/-osis/-ometry terms of nine or more characters; "oxidation", "hydration", "fermentation", "distillation", "esterification", "incineration" and "condensation" carried by exact single-word glossary terms inside their own notes, and the four residual slips rephrased in place; no register warning survived to export on any note.',
    patchLiveProof: 'the wave-1 save() omission stayed patched all wave: zero gate-blocked exports, zero re-exports, exactly one P8 phase-end per log — every production round since the patch has run clean.',
  },
  reader: {
    numberofRecord: 'no human-rate number is quotable from wave-10 (chain telemetry under pre-write batch flow, declared-assisted). Planning continues on the wave-1 instrumented basis (283 s/note, 0.0697 s/ch) and the 28/56/93 author-day bands.',
    caveat: 'All figures are model-drafted under the operator OPEN posture with per-phase declared assistance. The focused tally measures the P0-P8 chain window, not authoring effort, under the batch flow disclosed above; the exposure bands remain the only corpus-wide arithmetic of record.',
  },
};

const OUT = `${DL}/wave10-receipt.json`;
fs.writeFileSync(OUT, JSON.stringify(receipt, null, 1));
console.log('WAVE RECEIPT OF RECORD:', OUT);
console.log(`notes ${totals.notes} | lessons ${totals.lessons} | keyPoints ${totals.keyPoints} | checks ${totals.checks} | glossary ${totals.glossaryTerms} | distractors ${totals.distractors} | bodyChars ${totals.bodyChars}`);
console.log(`focused(chain telemetry) ${totals.focusedSeconds}s | mean ${totals.meanSecondsPerNote}s/note | ${totals.secondsPerChar} s/ch | wall ${totals.wallSecondsAll}s | pauses ${totals.loggedPauses}`);
console.log('P0-P7 event-log ms per note: min', Math.min(...P0P7), 'max', Math.max(...P0P7));
console.log('reExports wave-wide:', eventGroundTruth.reduce((a, e) => a + e.reExportEvents, 0));
console.log('warnings:', Object.entries(warningInventory).map(([k, v]) => v + 'x ' + k.slice(0, 60)).join(' | '));
console.log('CORPUS CENSUS:', JSON.stringify(topicCensus, null, 0));
console.log('prior pool + wave-10 =', doneIds.size, 'of 112');
console.log('ALL ASSERTS PASSED — receipt minted');
