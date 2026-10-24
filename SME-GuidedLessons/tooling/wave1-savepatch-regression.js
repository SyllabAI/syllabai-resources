#!/usr/bin/env node
// wave1-savepatch-regression.js — regression proof for the wave1-run.js export save() defect
// patch (filed in wave1-receipt.json integrityRecord, patched 2026-10-24).
//
// Scenario reproduced: the on-disk event log in the state a successful save-less export left
// it in (last phase P8 still open). Then a re-export. The ORIGINAL harness re-closes P8 at
// Date.now() -> P8 seconds inflate by the whole inter-export gap (the 972/370/80 s incident).
// The PATCHED harness closes P8 exactly once and re-exports are timing-idempotent.
//
// Runs entirely against scratch dirs (.tmp/wave1/patch-verify/*) via the WAVE1_RUNS_DIR /
// WAVE1_DL_DIR test seams; the of-record runs/ and download/wave1/ are only READ (the layer
// and snapshot), never written. Exit 0 = all assertions pass.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const BASE = '/home/z/my-project/.tmp/wave1/patch-verify';
const LAYER = '/home/z/my-project/download/wave1/guided-lesson-rn_4SgDJv8rKxpQQSBh.json'; // read-only reference
const NOTE = 'rn_4SgDJv8rKxpQQSBh';
const HARNESS_PATCHED = '/home/z/my-project/scripts/wave1-run.js';
const HARNESS_ORIGINAL = '/home/z/my-project/scripts/wave1-run.prepatch.bak.js';
const GAP_MS = 8000;

const results = [];
function check(name, ok, detail) { results.push({ name, ok, detail }); console.log((ok ? 'PASS' : 'FAIL') + '  ' + name + (detail ? '  [' + detail + ']' : '')); }
const sleep = ms => new Promise(r => setTimeout(r, ms));

function freshCase(tag, harness) {
  const runs = path.join(BASE, tag, 'runs');
  const dl = path.join(BASE, tag, 'dl');
  fs.rmSync(path.join(BASE, tag), { recursive: true, force: true });
  fs.mkdirSync(runs, { recursive: true });
  // stale-state seed: P8 open since T0 = now - 300 s (what disk looked like after a
  // successful save-less export in the incident)
  const T0 = Date.now() - 300000;
  fs.writeFileSync(path.join(runs, `${NOTE}.events.json`), JSON.stringify([{ ts: T0, type: 'phase-start', phase: 'P8', assist: false }], null, 1));
  const env = Object.assign({}, process.env, { WAVE1_RUNS_DIR: runs, WAVE1_DL_DIR: dl });
  const runExport = () => execFileSync('node', [harness, 'export', NOTE, LAYER], { encoding: 'utf8', env });
  const receipt = () => JSON.parse(fs.readFileSync(path.join(dl, `timing-receipt-${NOTE}.json`), 'utf8'));
  const log = () => JSON.parse(fs.readFileSync(path.join(runs, `${NOTE}.events.json`), 'utf8'));
  return { runs, dl, runExport, receipt, log };
}

(async () => {
  fs.mkdirSync(BASE, { recursive: true });

  // Guard of record: checksum every file in download/wave1/ before and after — the test
  // must leave the of-record deliverables byte-identical. (Lesson of this round: the raw
  // prepatch harness has the REAL dirs hardcoded and ignored the env seams; the negative
  // control therefore runs a CONTAINED copy with W/DL string-replaced to scratch paths.)
  const crypto = require('crypto');
  const REAL_DL = '/home/z/my-project/download/wave1';
  const dirSha = () => JSON.stringify(fs.readdirSync(REAL_DL).sort().map(f => [f, crypto.createHash('sha256').update(fs.readFileSync(path.join(REAL_DL, f))).digest('hex')]));
  const shaBefore = dirSha();

  // Materialize a CONTAINED copy of the original (defective) harness for the negative
  // control: identical behavior, but its hardcoded W/DL consts point at scratch dirs.
  function materialize(tag, srcPath, runs, dl) {
    if (!srcPath.endsWith('.bak.js')) return srcPath;
    const out = path.join(BASE, tag, 'harness-contained.js');
    let code = fs.readFileSync(srcPath, 'utf8');
    code = code.replace("const W = '/home/z/my-project/.tmp/wave1/runs';", `const W = '${runs}';`);
    code = code.replace("const DL = '/home/z/my-project/download/wave1';", `const DL = '${dl}';`);
    if (code.includes("'/home/z/my-project/.tmp/wave1/runs'")) throw new Error('containment replace failed (W)');
    if (code.includes("const DL = '/home/z/my-project/download/wave1'")) throw new Error('containment replace failed (DL)');
    fs.writeFileSync(out, code);
    return out;
  }

  // ---- CASE A: ORIGINAL harness (negative control — defect must reproduce) ----
  const a = freshCase('original', HARNESS_ORIGINAL);
  const aHarness = materialize('original', HARNESS_ORIGINAL, a.runs, a.dl);
  a.runExport = () => execFileSync('node', [aHarness, 'export', NOTE, LAYER], { encoding: 'utf8' });
  a.runExport();
  const a1 = a.receipt();
  check('A1 original: first export closes P8 at ~300s', Math.abs(a1.phaseSeconds.P8 - 300) <= 3, 'P8=' + a1.phaseSeconds.P8 + 's');
  check('A2 original: disk log still stale after SUCCESSFUL export (defect present)',
    !a.log().some(e => e.type === 'export'), 'events on disk: ' + a.log().map(e => e.type).join(','));
  await sleep(GAP_MS);
  a.runExport();
  const a2 = a.receipt();
  check('A3 original: re-export RE-CLOSES P8 and inflates it (defect reproduced)',
    a2.phaseSeconds.P8 >= a1.phaseSeconds.P8 + GAP_MS / 1000 - 3, 'P8 ' + a1.phaseSeconds.P8 + 's -> ' + a2.phaseSeconds.P8 + 's');

  // ---- CASE B: PATCHED harness (the fix) ----
  const b = freshCase('patched', HARNESS_PATCHED);
  b.runExport();
  const b1 = b.receipt();
  const bLog1 = b.log();
  check('B1 patched: first export closes P8 at ~300s (same semantics)', Math.abs(b1.phaseSeconds.P8 - 300) <= 3, 'P8=' + b1.phaseSeconds.P8 + 's');
  check('B2 patched: disk log PERSISTED on the success path (defect fixed)',
    bLog1.some(e => e.type === 'export'), 'events on disk: ' + bLog1.map(e => e.type).join(','));
  await sleep(GAP_MS);
  b.runExport();
  const b2 = b.receipt();
  const bLog2 = b.log();
  check('B3 patched: re-export does NOT re-close P8 — timing idempotent',
    Math.abs(b2.phaseSeconds.P8 - b1.phaseSeconds.P8) <= 1, 'P8 ' + b1.phaseSeconds.P8 + 's -> ' + b2.phaseSeconds.P8 + 's');
  check('B4 patched: exactly ONE phase-end for P8 in the log (no duplicate closure)',
    bLog2.filter(e => e.type === 'phase-end' && e.phase === 'P8').length === 1,
    'phase-end P8 count=' + bLog2.filter(e => e.type === 'phase-end' && e.phase === 'P8').length);
  check('B5 patched: re-export flagged reExport:true in the event log (audit trail)',
    bLog2[bLog2.length - 1].type === 'export' && bLog2[bLog2.length - 1].reExport === true,
    'last event: ' + JSON.stringify(bLog2[bLog2.length - 1]));
  check('B6 patched: totals match across re-export',
    b1.totalSeconds === b2.totalSeconds, b1.totalSeconds + 's == ' + b2.totalSeconds + 's');

  const failed = results.filter(r => !r.ok);
  check('Z1 of-record download/wave1/ byte-identical after the whole test', dirSha() === shaBefore,
    failed.length ? 'SEE FAILURES ABOVE' : Object.keys(JSON.parse(shaBefore)).length + ' files unchanged');
  console.log('\n' + (failed.length ? 'REGRESSION RESULT: FAIL (' + failed.length + ' failing)' : 'REGRESSION RESULT: ALL PASS (' + results.length + ' assertions)'));
  fs.writeFileSync(path.join(BASE, 'regression-result.json'), JSON.stringify({ at: new Date().toISOString(), gapMs: GAP_MS, results }, null, 1));
  process.exit(failed.length ? 1 : 0);
})().catch(e => { console.error('HARNESS ERROR:', e.message); process.exit(2); });
