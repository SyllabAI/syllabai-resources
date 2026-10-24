#!/usr/bin/env node
// wave1-run.js — run harness for the instrumented first authoring wave (A1 protocol of
// record, spec section 7). Append-only event log per note; export computes per-phase
// seconds, wall-clock span, pause log and declared-assistance flags, then validates +
// lints the layer file and files the receipt beside it. Lane-local; zero network.
// Usage:
//   node scripts/wave1-run.js start   <noteId>                      # P0 begins
//   node scripts/wave1-run.js phase   <noteId> <P0..P8> [--assist]  # close current phase, open next
//   node scripts/wave1-run.js pause   <noteId> <reason-code>        # logged pause (interruption|reference|break)
//   node scripts/wave1-run.js resume  <noteId>
//   node scripts/wave1-run.js export  <noteId> <layerJsonPath>      # P8 close: validate, lint, receipt, file
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

// Test seam (save()-defect patch, 2026-10-24): WAVE1_RUNS_DIR / WAVE1_DL_DIR may redirect the
// run-log and deliverable dirs for regression testing against scratch copies. Unset behavior
// is identical to the wave-1 harness of record.
const W = process.env.WAVE1_RUNS_DIR || '/home/z/my-project/.tmp/wave1/runs';
const DL = process.env.WAVE1_DL_DIR || '/home/z/my-project/download/wave1';
const PHASES = ['P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'];

const [cmd, noteId, ...rest] = process.argv.slice(2);
const file = path.join(W, `${noteId}.events.json`);
const events = fs.existsSync(file) ? JSON.parse(fs.readFileSync(file, 'utf8')) : [];
function save() { fs.mkdirSync(W, { recursive: true }); fs.writeFileSync(file, JSON.stringify(events, null, 1)); }
function lastOpen() { return [...events].reverse().find(e => e.type === 'phase-start' || e.type === 'pause'); }

if (cmd === 'start') {
  if (events.length) { console.error('run already started for ' + noteId); process.exit(1); }
  events.push({ ts: Date.now(), type: 'phase-start', phase: 'P0', assist: false });
  save(); console.log(`RUN ${noteId}: P0 (load and read) clock started`);
} else if (cmd === 'phase') {
  const [phase, flag] = rest;
  const open = lastOpen();
  if (!open || open.type !== 'phase-start') { console.error('no open phase (paused? resume first)'); process.exit(1); }
  events.push({ ts: Date.now(), type: 'phase-end', phase: open.phase, assist: flag === '--assist' });
  const next = PHASES[PHASES.indexOf(phase)] || phase;
  events.push({ ts: Date.now(), type: 'phase-start', phase: next, assist: false });
  save();
  console.log(`RUN ${noteId}: ${open.phase} closed${flag === '--assist' ? ' (declared-assisted)' : ''}; ${next} clock started`);
} else if (cmd === 'pause') {
  const open = lastOpen();
  if (!open || open.type !== 'phase-start') { console.error('nothing open to pause'); process.exit(1); }
  events.push({ ts: Date.now(), type: 'pause', phase: open.phase, reason: rest[0] || 'unspecified' });
  save(); console.log(`RUN ${noteId}: paused during ${open.phase} (${rest[0]})`);
} else if (cmd === 'resume') {
  const p = [...events].reverse().find(e => e.type === 'pause');
  if (!p) { console.error('no pause to resume'); process.exit(1); }
  events.push({ ts: Date.now(), type: 'phase-start', phase: p.phase, assist: false, resumed: true });
  save(); console.log(`RUN ${noteId}: resumed ${p.phase}`);
} else if (cmd === 'export') {
  const layerPath = rest[0];
  // DEFECT PATCH of record (filed in wave1-receipt.json integrityRecord: success-path save()
  // omission). Before this patch, export mutated the event log in memory but only called
  // save() on the BLOCKED path — a successful export left the on-disk log stale with the
  // last phase still open, so any re-export re-closed that phase at Date.now(), swallowing
  // the whole wall-clock gap into its seconds (the wave-1 P8 inflation 972/370/80 s vs the
  // true closures 261/315/214/283 s). Fix, two parts:
  //   1. persist at mutation time — save() runs immediately after the export event is
  //      pushed, BEFORE validation/lint; success and blocked paths both persist the log.
  //   2. idempotent re-export — when the last event is already an `export`, the open phase
  //      was closed by that prior export, so no phase-end is pushed and the new export
  //      event carries reExport:true. A re-export can never re-close a phase again.
  const reExport = events.length > 0 && events[events.length - 1].type === 'export';
  const open = lastOpen();
  if (!reExport && open && open.type === 'phase-start') {
    events.push({ ts: Date.now(), type: 'phase-end', phase: open.phase, assist: false });
  }
  events.push(Object.assign({ ts: Date.now(), type: 'export' }, reExport ? { reExport: true } : {}));
  save(); // persist the mutation immediately (append-only log discipline: every command persists its own writes)
  // compute receipt
  const phaseSec = {}; let assistFlags = {}; let pauses = [];
  let openPhase = null, openTs = 0;
  const start = events[0].ts;
  for (const e of events) {
    if (e.type === 'phase-start') { openPhase = e.phase; openTs = e.ts; if (e.resumed) openTs = e.ts; }
    else if (e.type === 'pause') { phaseSec[openPhase] = (phaseSec[openPhase] || 0) + (e.ts - openTs) / 1000; pauses.push({ phase: openPhase, reason: e.reason, seconds: Math.round((e.ts - openTs) / 1000) }); openPhase = null; }
    else if (e.type === 'phase-end') { if (openPhase) { phaseSec[openPhase] = (phaseSec[openPhase] || 0) + (e.ts - openTs) / 1000; if (e.assist) assistFlags[openPhase] = true; openPhase = null; } }
    else if (e.type === 'export') { if (openPhase) { phaseSec[openPhase] = (phaseSec[openPhase] || 0) + (e.ts - openTs) / 1000; openPhase = null; } }
  }
  const totalSec = PHASES.reduce((a, p) => a + (phaseSec[p] || 0), 0);
  const wallSpanSec = (events[events.length - 1].ts - start) / 1000;
  // validate + lint
  const schema = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/guided-lesson.0.1.schema.json', 'utf8'));
  const Ajv = require('/home/z/node_modules/ajv');
  const ajv = new Ajv({ allErrors: true, strict: false });
  const layer = JSON.parse(fs.readFileSync(layerPath, 'utf8'));
  const validate = ajv.compile(schema);
  const schemaOk = validate(layer);
  let lintOut = '', lintOk = false;
  try {
    lintOut = execFileSync('node', ['/home/z/my-project/scripts/a1-lint.js', layerPath, '--note', noteId], { encoding: 'utf8' });
    lintOk = true;
  } catch (e) { lintOut = e.stdout || e.message; lintOk = false; }
  if (!schemaOk || !lintOk) {
    console.log('SCHEMA:', schemaOk ? 'PASS' : 'FAIL\n' + JSON.stringify(validate.errors, null, 1));
    console.log(lintOut);
    console.error('EXPORT BLOCKED: fix violations and re-export');
    // save() no longer needed here: the log was already persisted at mutation time above.
    process.exit(1);
  }
  // file deliverables
  fs.mkdirSync(DL, { recursive: true });
  const layerOut = path.join(DL, `guided-lesson-${noteId}.json`);
  fs.copyFileSync(layerPath, layerOut);
  const snap = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));
  const row = snap.notes.find(n => n.noteId === noteId);
  const receipt = {
    format: 'wave1-timing-receipt/0.1',
    noteId, noteTitle: row.title, topicTitle: row.topicTitle, subtopicTitle: row.subtopicTitle,
    corpusVersion: row.corpusVersion, bodySha256: row.bodySha256, bodyChars: row.bodyChars,
    specPointCodes: row.specPointCodes,
    protocol: 'A1 spec section 7 (single author, single session, declared assistance per phase, corpus pinned to snapshot of record)',
    declaredAssistance: 'model-drafted under operator OPEN posture; per-phase assist flags of record: ' + (Object.keys(assistFlags).length ? Object.keys(assistFlags).join(', ') : 'none') + '; unflagged phases produced no drafted content (P0 read-only, P8 mechanical)',
    phaseSeconds: Object.fromEntries(PHASES.map(p => [p, Math.round(phaseSec[p] || 0)])),
    totalSeconds: Math.round(totalSec),
    authoringHoursPerTopic: +(totalSec / 3600).toFixed(2),
    wallClockSpanSeconds: Math.round(wallSpanSec),
    pauseLog: pauses,
    assistedPhases: Object.keys(assistFlags),
    schemaValidation: 'PASS (ajv draft-07, additionalProperties false)',
    lint: lintOut.trim(),
    exportedAt: new Date().toISOString(),
    layerFile: layerOut,
  };
  const receiptOut = path.join(DL, `timing-receipt-${noteId}.json`);
  fs.writeFileSync(receiptOut, JSON.stringify(receipt, null, 1));
  console.log('SCHEMA: PASS');
  console.log(lintOut);
  console.log(`EXPORTED ${layerOut}`);
  console.log(`RECEIPT  ${receiptOut}`);
  console.log(`TOTAL ${receipt.totalSeconds}s = ${receipt.authoringHoursPerTopic} h | wall ${receipt.wallClockSpanSeconds}s | pauses ${pauses.length}`);
} else { console.error('unknown command'); process.exit(2); }
