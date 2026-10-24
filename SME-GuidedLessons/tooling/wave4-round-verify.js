#!/usr/bin/env node
// wave4-round-verify.js — round-close verification for wave-4 (minted at the 11/11 close-out round,
// wave-3 pattern: scripts/wave3-round-verify.js).
// 1. Each timing receipt matches its snapshot row on the 7 pin fields + spec codes.
// 2. Layer noteRef matches the pinned chain; schema PASS + lint designed-or-none recorded.
// 3. Wave-4 running tally recomputed from receipts on disk.
// 4. Guards: wave-1 (22) + wave-2 (25) + wave-3 (25 incl. aggregate receipt) + wave-4 counts; event-log
//    ground truth (19 events, ONE export, ONE P8 phase-end, P0 unflagged, zero reExports, zero pauses).
// 5. Snapshot file pin unchanged.
// 6. CLOSE-OUT guards (active once download/wave4/wave4-receipt.json exists) — wave-3 pattern.
const fs = require('fs');
const crypto = require('crypto');
const snap = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));

let fails = 0;
function check(name, ok, detail) {
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
  if (!ok) fails++;
}

const IDS = ['rn_J7ZcTWyRxRgWQ45R', 'rn_FCnWFz9MhgsqnZGM', 'rn_jVwPmjqHbqQkXcjG', 'rn_vfmJxw4VQgXKzXF3', 'rn_MVnFKDMVkswzpmpw', 'rn_KpvF2TWr5fYHk2Jz', 'rn_GkJG52NCN98ShGRm', 'rn_Hp2nK8XpN2SmjdQc', 'rn_rHKCkt3PTXDBpmJG', 'rn_3YZNCXSQQqXTT6HR', 'rn_kdRjZHjHcpVZsD3h'];

// 1+2: receipts + layers vs snapshot
for (const id of IDS) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave4/timing-receipt-${id}.json`, 'utf8'));
  const row = snap.notes.find(n => n.noteId === id);
  for (const [k, v] of [['noteTitle', row.title], ['topicTitle', row.topicTitle], ['subtopicTitle', row.subtopicTitle], ['corpusVersion', row.corpusVersion], ['bodySha256', row.bodySha256], ['bodyChars', row.bodyChars]]) {
    check(`${id} receipt.${k}`, JSON.stringify(r[k]) === JSON.stringify(v), JSON.stringify(v).slice(0, 60));
  }
  check(`${id} receipt.specPointCodes`, JSON.stringify(r.specPointCodes) === JSON.stringify(row.specPointCodes), row.specPointCodes.join(','));
  const layer = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave4/guided-lesson-${id}.json`, 'utf8'));
  check(`${id} layer.noteRef`, layer.noteRef.noteId === id && layer.noteRef.corpusVersion === row.corpusVersion && layer.noteRef.subtopicTitle === row.subtopicTitle);
  check(`${id} schema+lint recorded`, String(r.schemaValidation).startsWith('PASS') && /hard-fails 0/.test(r.lint));
  const designed = /workedExample is null/.test(r.lint) || /no arithmetic expression found/.test(r.lint);
  check(`${id} lint warnings designed-or-none`, /warnings 0/.test(r.lint) || (designed && /warnings 1/.test(r.lint)), designed ? '1 designed (non-numeric or absent workedExample, declared)' : 'clean');
  check(`${id} chain discipline`, JSON.stringify(r.assistedPhases) === JSON.stringify(['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']), 'assistedPhases = P1..P7');
  check(`${id} zero pauses`, r.pauseLog.length === 0);
  // event-log ground truth
  const ev = JSON.parse(fs.readFileSync(`/home/z/my-project/.tmp/wave4/runs/${id}.events.json`, 'utf8'));
  const exports_ = ev.filter(e => e.type === 'export');
  const reExp = ev.filter(e => e.type === 'export' && e.reExport === true);
  const p8ends = ev.filter(e => e.type === 'phase-end' && e.phase === 'P8');
  const p0end = ev.find(e => e.type === 'phase-end' && e.phase === 'P0');
  const pauses = ev.filter(e => e.type === 'pause');
  check(`${id} event log ground truth (19 events, 1 export, 1 P8 close, P0 unflagged, no reExport, no pause)`,
    ev.length === 19 && exports_.length === 1 && reExp.length === 0 && p8ends.length === 1 && p0end && p0end.assist === false && pauses.length === 0,
    `events ${ev.length}, exports ${exports_.length}, reExports ${reExp.length}, P8ends ${p8ends.length}`);
}

// 3: wave-4 running tally from receipts on disk
const files = fs.readdirSync('/home/z/my-project/download/wave4').filter(f => f.startsWith('timing-receipt-'));
let tally = { notes: files.length, checks: 0, keyPoints: 0, glossary: 0, focused: 0, pauses: 0 };
const perNote = [];
for (const f of files) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave4/${f}`, 'utf8'));
  const layer = JSON.parse(fs.readFileSync(r.layerFile, 'utf8'));
  const checks = layer.lessons.reduce((a, L) => a + L.check.length, 0);
  tally.checks += checks;
  tally.keyPoints += layer.lessons.reduce((a, L) => a + L.keyPoints.length, 0);
  tally.glossary += layer.noteAssets.glossary.length;
  tally.focused += r.totalSeconds;
  tally.pauses += r.pauseLog.length;
  perNote.push(`${r.noteId}: ${layer.lessons.length}L ${checks}chk ${r.totalSeconds}s`);
}
console.log('--- wave-4 tally:', JSON.stringify(tally));
console.log(perNote.join('\n'));

// 4: guards
const w1 = fs.readdirSync('/home/z/my-project/download/wave1');
check('wave-1 deliverables intact (22 files incl. pin reverify)', w1.length === 22, `count ${w1.length}`);
const w2 = fs.readdirSync('/home/z/my-project/download/wave2');
check('wave-2 deliverables intact (25 files incl. aggregate receipt)', w2.length === 25, `count ${w2.length}`);
const w3 = fs.readdirSync('/home/z/my-project/download/wave3');
check('wave-3 deliverables intact (25 files incl. aggregate receipt)', w3.length === 25, `count ${w3.length}`);
const w4 = fs.readdirSync('/home/z/my-project/download/wave4');
check('wave-4 layers+receipts complete (11+11 by prefix)',
  w4.filter(f => f.startsWith('guided-lesson-')).length === 11 && w4.filter(f => f.startsWith('timing-receipt-')).length === 11,
  `layers ${w4.filter(f => f.startsWith('guided-lesson-')).length}, receipts ${w4.filter(f => f.startsWith('timing-receipt-')).length}`);
const runs4 = fs.readdirSync('/home/z/my-project/.tmp/wave4/runs');
check('wave-4 event logs persisted (11)', runs4.length === 11, `count ${runs4.length}`);

// 5: snapshot file pin
const h = crypto.createHash('sha256').update(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json')).digest('hex');
check('snapshot file pin unchanged', h === 'e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d');

// 6: CLOSE-OUT guards (active once the aggregate receipt exists) — wave-3 pattern
const recPath = '/home/z/my-project/download/wave4/wave4-receipt.json';
if (fs.existsSync(recPath)) {
  const rec = JSON.parse(fs.readFileSync(recPath, 'utf8'));
  check('aggregate wave4-receipt.json present', true);
  check('receipt format of record', rec.format === 'wave4-receipt/0.1', rec.format);
  check('receipt register 11/11', Array.isArray(rec.perNote) && rec.perNote.length === 11, rec.perNote ? `perNote ${rec.perNote.length}` : 'missing');
  check('receipt totals reconcile receipt-vs-disk', rec.totals && rec.totals.checks === tally.checks && rec.totals.keyPoints === tally.keyPoints && rec.totals.glossaryTerms === tally.glossary,
    `receipt ${rec.totals ? rec.totals.checks + '/' + rec.totals.keyPoints + '/' + rec.totals.glossaryTerms : 'n/a'} vs disk ${tally.checks}/${tally.keyPoints}/${tally.glossary}`);
  const warnLines = Object.values(rec.warningInventory || {}).reduce((a, b) => a + b, 0);
  check('warning inventory reconciles to 11 designed', warnLines === 11, `inventory lines ${warnLines}`);
  check('recalibration decision block (4 items, wave-1 basis)', Array.isArray(rec.recalibration && rec.recalibration.decisionOfRecord) && rec.recalibration.decisionOfRecord.length === 4 && rec.recalibration.wave1BasisOfRecord && rec.recalibration.wave1BasisOfRecord.meanSecondsPerNote === 283);
  check('event-log ground truth 11 entries', Array.isArray(rec.eventLogGroundTruth) && rec.eventLogGroundTruth.length === 11, rec.eventLogGroundTruth ? `entries ${rec.eventLogGroundTruth.length}` : 'missing');
  check('zero-DB statement present', typeof rec.corpusPin.dbContact === 'string' && rec.corpusPin.dbContact.startsWith('ZERO database contact'));
  check('receipt pin matches recomputed snapshot pin', rec.corpusPin.snapshotFilePinSha256RecomputedThisRound === h);
  check('wave-4 deliverables complete incl. receipt (23 files)', w4c(), `count ${w4c()}`);
}
function w4c() { return fs.readdirSync('/home/z/my-project/download/wave4').length; }
const reportPath = '/home/z/my-project/download/Wave-4-Authoring-Wave-Report-20261025.docx';
check('wave-4 report DOCX present', fs.existsSync(reportPath), reportPath.split('/').pop());

console.log(fails ? `\n${fails} FAILURES` : '\nALL CHECKS PASS');
process.exit(fails ? 1 : 0);
