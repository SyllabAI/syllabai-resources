#!/usr/bin/env node
// wave-pacing-open.js — pacing of the remaining 102 notes under the operator OPEN posture
// (operator: "pace the remaining 102 notes under OPEN", trace 1a169f7a1cd353f5), 2026-10-24.
//
// Pacing basis of record:
//   - measured: wave-1 instrumented receipts (10 notes, focused 2,830 s, mean 283 s/note;
//     per-char rate 2,830 s / 40,614 ch) — the instrumented pipeline rate, model-drafted
//     with per-phase declared assistance; never a human-rate claim;
//   - standing exposure bands of record 28 / 56 / 93 author-days per 112 notes, scaled to
//     the remaining 102 — disclosure arithmetic only;
//   - OPEN semantics: pacing is a SCHEDULE, not a gate. The ~2 h/note open-flip threshold
//     is dissolved; receipts + declared assistance continue as measurement discipline.
// Wave structure: topic-ordered (prerequisite-consistent — primers cite earlier subtopics),
// wave size ~12 at the wave-1 cadence. Register assigns every remaining noteId to a wave.
// Output: download/wave-pacing-open-20261024.json
const fs = require('fs');

const snap = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));
const waveReceipt = JSON.parse(fs.readFileSync('/home/z/my-project/download/wave1/wave1-receipt.json', 'utf8'));
const pinVerify = JSON.parse(fs.readFileSync('/home/z/my-project/download/wave1/snapshot-pin-reverify-20261024.json', 'utf8'));

const ROSTER = ['rn_xT8XsdJtDX5gNFXj','rn_HZM2WRjPPT8Srcxt','rn_JCfdFrHsCkrmMbFj','rn_TM4QVMgXVxs4vbfY','rn_wTtM2fQVVjntRm64','rn_jNJ4gTmcHqdFqsNh','rn_kJg2gwF77vdFZZ2H','rn_fQSYvKRMDBj3s2Bx','rn_2d6Yb8GwGfRRd6pZ','rn_4SgDJv8rKxpQQSBh'];

// ---- measured basis (wave-1 of record) ----
const m = waveReceipt.totals;
const wave1Chars = ROSTER.reduce((a, id) => a + snap.notes.find(n => n.noteId === id).bodyChars, 0);
const meanSecPerNote = m.meanSecondsPerNote;                 // 283
const secPerChar = m.focusedSeconds / wave1Chars;            // ~0.0697
const basis = {
  measuredWave1: {
    notes: m.notes, lessons: m.lessons, checks: m.checks,
    focusedSeconds: m.focusedSeconds, focusedHours: m.focusedHours,
    meanSecondsPerNote: meanSecPerNote, meanHoursPerNote: m.meanHoursPerNote, meanHoursPerLesson: m.meanHoursPerLesson,
    phaseSharePercent: waveReceipt.phaseSharePercent,
    sourceNotesChars: wave1Chars,
    characterOfSample: 'roster deliberately covered 8+ note genres and both size extremes to maximise format-overfit information; thin-note and largest-note cases already measured',
  },
  perCharRateSeconds: +secPerChar.toFixed(5),
  standingBandsOfRecord: {
    source: 'bands 28 / 56 / 93 author-days per 112-note corpus (exposure arithmetic of record; never gates; floor 0.2 h/topic never quotable as a human rate)',
    perNoteHours: [2, 4, +(93 * 8 / 112).toFixed(2)],
    scaledTo102: {
      authorDays: [+(28 * 102 / 112).toFixed(2), +(56 * 102 / 112).toFixed(2), +(93 * 102 / 112).toFixed(2)],
      hours: [28 * 102 / 112 * 8, 56 * 102 / 112 * 8, 93 * 102 / 112 * 8].map(x => +x.toFixed(1)),
    },
  },
};

// ---- remaining notes in canonical (prerequisite-consistent) order ----
const remaining = snap.notes.filter(n => !ROSTER.includes(n.noteId));
if (remaining.length !== 102) { console.error('FATAL: expected 102 remaining, got ' + remaining.length); process.exit(1); }

// ---- wave plan: topic-ordered, size ~12 (wave-1 cadence); T3 rides as one coherent wave ----
const PLAN = [
  { wave: 2,  topicPrefix: 'T1', count: 12 },
  { wave: 3,  topicPrefix: 'T1', count: 12 },
  { wave: 4,  topicPrefix: 'T1', count: 11 },
  { wave: 5,  topicPrefix: 'T2', count: 12 },
  { wave: 6,  topicPrefix: 'T2', count: 12 },
  { wave: 7,  topicPrefix: 'T2', count: 9 },
  { wave: 8,  topicPrefix: 'T3', count: 14 },
  { wave: 9,  topicPrefix: 'T4', count: 12 },
  { wave: 10, topicPrefix: 'T4', count: 8 },
];
const entryConditions = [
  'snapshot pin re-verified zero-DB against the file pins of record (wave-2: snapshot-pin-reverify-20261024.json; later waves: re-run scripts/wave1-pin-verify.js)',
  'harness save() patch in effect (scripts/wave1-run.js 2026-10-24; regression proof .tmp/wave1/patch-verify/regression-result.json)',
  'roster = next notes in topic order; format-minimums check at P1 per note (lessons 1-5, checks 5/lesson, keyPoints 3-6, glossary 3-8, two depth layers)',
  'ajv present (npm install --prefix /home/z ajv --no-save post-recycle; documented recurring pattern)',
  'protocol section 7: single author/session, declared assistance per phase, pauses logged with reason codes, P0 body read end to end from the pinned snapshot',
];
const wavePlan = [];
let idx = 0;
for (const p of PLAN) {
  const notes = remaining.slice(idx, idx + p.count);
  idx += p.count;
  const chars = notes.reduce((a, n) => a + n.bodyChars, 0);
  const topicTitle = notes[0].topicTitle;
  const specPoints = notes.reduce((a, n) => a + n.specPointCodes.length, 0);
  wavePlan.push({
    wave: p.wave,
    topic: `T${p.topicPrefix.slice(1)}: ${topicTitle}`,
    noteCount: notes.length,
    totalBodyChars: chars,
    specPoints: specPoints,
    expectedFocusedHours: {
      meanBased: +(notes.length * meanSecPerNote / 3600).toFixed(2),
      charBased: +(chars * secPerChar / 3600).toFixed(2),
    },
    register: notes.map(n => ({ noteId: n.noteId, title: n.title, subtopic: n.subtopicTitle, bodyChars: n.bodyChars, specPointCodes: n.specPointCodes })),
    entryConditions,
    exit: 'wave receipt (per-wave aggregate of the per-note timing receipts) + wave report; recalibration checkpoint applied before the next wave opens',
  });
}
if (idx !== 102) { console.error('FATAL: wave plan covers ' + idx + ' of 102'); process.exit(1); }

const pacing = {
  format: 'wave-pacing-open/0.1',
  at: new Date().toISOString(),
  operatorInstruction: 'pace the remaining 102 notes under OPEN (trace 1a169f7a1cd353f5)',
  posture: {
    name: 'OPEN (build it fully) — operator decision of record, trace 1a1683ec43a016a9; brief of record A5-Posture-Decision-Brief-Open-20261023.docx',
    semantics: 'guided study + guided practice full-corpus commitment (112 notes, 1:1 with the 28 subtopics); pacing is a SCHEDULE, not a gate; the ~2 h/note open-flip threshold is dissolved; per-phase timing receipts + declared assistance continue as measurement discipline, not admission control',
    floorRule: 'the 0.2 h/topic floor is never quotable as a human rate; the only corpus-wide human-exposure arithmetic of record is the 28/56/93 author-day band set, re-disclosed below',
  },
  preconditionsClosedThisRound: {
    saveDefect: 'PATCHED + regression-proven: wave1-run.js export now persists the event log at mutation time and re-exports are idempotent (never re-close a phase); proof: scripts/wave1-savepatch-regression.js, 10/10 assertions, negative control reproduced the defect (P8 300s -> 308s on re-export), of-record files byte-identical (21 files)',
    snapshotPin: 'RE-VERIFIED zero-DB: 16/16 checks (112/112 body hashes, census 4/28/112 @ 40-36-15-21, 361,272 chars, single corpus_version, canonical order, 10 receipts + wave receipt reconciled); receipt: download/wave1/snapshot-pin-reverify-20261024.json; going-forward file pin e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d',
    dbContact: 'zero this round; waves 2-10 run entirely off the pinned local snapshot (all 112 bodies local) — zero further DB contact planned',
  },
  basis,
  pacingPrinciples: [
    'SCHEDULE NOT GATE: the plan paces the work; it does not admit or block it. Deviations are disclosed at the wave receipt, never hidden.',
    'PREREQUISITE ORDER: waves run T1 -> T2 -> T3 -> T4 and subtopic order within each topic, so every primer cites an already-built earlier subtopic (wave-1 precedent).',
    'MEASURED-LANE ESTIMATORS: mean-based (283 s/note) and char-based (0.0697 s/ch) are both carried; the char-based figure is the more honest extrapolator because the roster over-weights size extremes by design.',
    'BANDS ARE DISCLOSURE: the scaled 25.5 / 51 / 84.75 author-day figures describe plausible unassisted human-author exposure of the remaining corpus; they are not commitments and not gates.',
    'RECEIPT DISCIPLINE CONTINUES: every note exports with per-phase seconds + declared assistance; every wave closes with a wave receipt + wave report (wave-1 pattern).',
    'RECALIBRATION POINTS: at each wave receipt, recompute mean s/note, s/ch and phase shares from that wave\'s receipts, re-state the estimators, and disclose any drift — before the next wave opens.',
    'SESSION SHAPE: turn-boundary pauses are expected and logged; multi-session notes carry honest wall spans (the save() patch keeps re-exports from ever inflating them again).',
  ],
  wavePlan,
  totals: {
    waves: wavePlan.length,
    notes: wavePlan.reduce((a, w) => a + w.noteCount, 0),
    bodyChars: wavePlan.reduce((a, w) => a + w.totalBodyChars, 0),
    specPoints: wavePlan.reduce((a, w) => a + w.specPoints, 0),
    expectedFocusedHoursMeanBased: +(wavePlan.reduce((a, w) => a + w.expectedFocusedHours.meanBased, 0)).toFixed(2),
    expectedFocusedHoursCharBased: +(wavePlan.reduce((a, w) => a + w.expectedFocusedHours.charBased, 0)).toFixed(2),
    corpusAfterCompletion: '112/112 notes authored 1:1 with the 28 subtopics (guided study + guided practice, OPEN commitment closed)',
  },
  standingClosures: [
    'zero DB writes; zero further DB reads planned (snapshot is the pinned source of record)',
    'learner-side metering deferred (A5 of record); not-build classes stay closed',
    'operator-gated standing items remain closed and unconsumed (workflow_dispatch, secret writes, waiter/scheduler; Vercel lane GET-only; DB t0_readonly SELECT-only)',
    'SME content red line: process mechanisms only, never SME content text',
  ],
};

const out = '/home/z/my-project/download/wave-pacing-open-20261024.json';
fs.writeFileSync(out, JSON.stringify(pacing, null, 1));
console.log('PACING OF RECORD:', out);
console.log(`waves ${pacing.totals.waves} | notes ${pacing.totals.notes} | chars ${pacing.totals.bodyChars} | spec points ${pacing.totals.specPoints}`);
console.log(`expected focused: mean-based ${pacing.totals.expectedFocusedHoursMeanBased} h | char-based ${pacing.totals.expectedFocusedHoursCharBased} h`);
console.log('scaled bands (102 notes):', pacing.basis.standingBandsOfRecord.scaledTo102.authorDays.join(' / '), 'author-days (disclosure, not gate)');
for (const w of wavePlan) console.log(`  W${w.wave}  ${w.topic.padEnd(28)} ${String(w.noteCount).padStart(2)} notes  ${String(w.totalBodyChars).padStart(6)} ch  ~${w.expectedFocusedHours.meanBased}h (mean) / ${w.expectedFocusedHours.charBased}h (char)`);
