#!/usr/bin/env node
// wave7-round-verify.js — round-close verification for wave-7 (minted at the 9/9 close-out
// round, wave-6 pattern: scripts/wave6-round-verify.js).
// 1. Each timing receipt matches its snapshot row on the 7 pin fields + spec codes.
// 2. Layer noteRef matches the pinned chain; schema PASS + lint designed-or-none recorded.
// 3. Wave-7 running tally recomputed from receipts on disk.
// 4. Guards: wave-1 (22) + wave-2 (25) + wave-3 (25) + wave-4 (23) + wave-5 (25) + wave-6 (25)
//    + wave-7 counts; event-log ground truth (19 events, ONE export, ONE P8 phase-end, P0
//    unflagged, zero reExports, zero pauses).
// 5. Snapshot file pin unchanged.
// 6. CLOSE-OUT guards (active once download/wave7/wave7-receipt.json exists) — wave-3/4/5/6 pattern.
const fs = require('fs');
const crypto = require('crypto');
const snap = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));

let fails = 0;
function check(name, ok, detail) {
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
  if (!ok) fails++;
}

const IDS = ['rn_VvsXMdW3TB37JhWF', 'rn_6ZCysv9GnNQmc3w2', 'rn_5g8Dd6y89tkCVJsN', 'rn_qb9TBhB6VmnFGjvf', 'rn_pBp5Z5C2RHTKk7Wn', 'rn_T6S7R66N2wSZpWyc', 'rn_vVdP57QhDYSVfZgy', 'rn_v5JjfpT6grhtq3QW', 'rn_YWDXCCmjfjkJcs6c'];

// 1+2: receipts + layers vs snapshot
for (const id of IDS) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave7/timing-receipt-${id}.json`, 'utf8'));
  const row = snap.notes.find(n => n.noteId === id);
  for (const [k, v] of [['noteTitle', row.title], ['topicTitle', row.topicTitle], ['subtopicTitle', row.subtopicTitle], ['corpusVersion', row.corpusVersion], ['bodySha256', row.bodySha256], ['bodyChars', row.bodyChars]]) {
    check(`${id} receipt.${k}`, JSON.stringify(r[k]) === JSON.stringify(v), JSON.stringify(v).slice(0, 60));
  }
  check(`${id} receipt.specPointCodes`, JSON.stringify(r.specPointCodes) === JSON.stringify(row.specPointCodes), row.specPointCodes.join(','));
  const layer = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave7/guided-lesson-${id}.json`, 'utf8'));
  check(`${id} layer.noteRef`, layer.noteRef.noteId === id && layer.noteRef.corpusVersion === row.corpusVersion && layer.noteRef.subtopicTitle === row.subtopicTitle);
  check(`${id} schema+lint recorded`, String(r.schemaValidation).startsWith('PASS') && /hard-fails 0/.test(r.lint));
  const designed = /workedExample is null/.test(r.lint) || /no arithmetic expression found/.test(r.lint);
  check(`${id} lint warnings designed-or-none`, /warnings 0/.test(r.lint) || (designed && /warnings 1/.test(r.lint)), /warnings 0/.test(r.lint) ? 'clean' : '1 designed declared');
  check(`${id} chain discipline`, JSON.stringify(r.assistedPhases) === JSON.stringify(['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']), 'assistedPhases = P1..P7');
  check(`${id} zero pauses`, r.pauseLog.length === 0);
  // event-log ground truth
  const ev = JSON.parse(fs.readFileSync(`/home/z/my-project/.tmp/wave7/runs/${id}.events.json`, 'utf8'));
  const exports_ = ev.filter(e => e.type === 'export');
  const reExp = ev.filter(e => e.type === 'export' && e.reExport === true);
  const p8ends = ev.filter(e => e.type === 'phase-end' && e.phase === 'P8');
  const p0end = ev.find(e => e.type === 'phase-end' && e.phase === 'P0');
  const pauses = ev.filter(e => e.type === 'pause');
  check(`${id} event log ground truth (19 events, 1 export, 1 P8 close, P0 unflagged, no reExport, no pause)`,
    ev.length === 19 && exports_.length === 1 && reExp.length === 0 && p8ends.length === 1 && p0end && p0end.assist === false && pauses.length === 0,
    `events ${ev.length}, exports ${exports_.length}, reExports ${reExp.length}, P8ends ${p8ends.length}`);
}

// 3: wave-7 running tally from receipts on disk
const files = fs.readdirSync('/home/z/my-project/download/wave7').filter(f => f.startsWith('timing-receipt-'));
let tally = { notes: files.length, checks: 0, keyPoints: 0, glossary: 0, focused: 0, pauses: 0 };
const perNote = [];
for (const f of files) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave7/${f}`, 'utf8'));
  const layer = JSON.parse(fs.readFileSync(r.layerFile, 'utf8'));
  const checks = layer.lessons.reduce((a, L) => a + L.check.length, 0);
  tally.checks += checks;
  tally.keyPoints += layer.lessons.reduce((a, L) => a + L.keyPoints.length, 0);
  tally.glossary += layer.noteAssets.glossary.length;
  tally.focused += r.totalSeconds;
  tally.pauses += r.pauseLog.length;
  perNote.push(`${r.noteId}: ${layer.lessons.length}L ${checks}chk ${r.totalSeconds}s`);
}
console.log('--- wave-7 tally:', JSON.stringify(tally));
console.log(perNote.join('\n'));

// 4: guards
const counts = { wave1: 22, wave2: 25, wave3: 25, wave4: 23, wave5: 25, wave6: 25 };
for (const [w, n] of Object.entries(counts)) {
  const dir = fs.readdirSync(`/home/z/my-project/download/${w}`);
  check(`wave-${w.slice(4)} deliverables intact (${n} files)`, dir.length === n, `count ${dir.length}`);
}
const w7 = fs.readdirSync('/home/z/my-project/download/wave7');
check('wave-7 layers+receipts complete (9+9 by prefix)',
  w7.filter(f => f.startsWith('guided-lesson-')).length === 9 && w7.filter(f => f.startsWith('timing-receipt-')).length === 9,
  `layers ${w7.filter(f => f.startsWith('guided-lesson-')).length}, receipts ${w7.filter(f => f.startsWith('timing-receipt-')).length}`);
const runs7 = fs.readdirSync('/home/z/my-project/.tmp/wave7/runs');
check('wave-7 event logs persisted (9)', runs7.length === 9, `count ${runs7.length}`);

// 5: snapshot file pin
const h = crypto.createHash('sha256').update(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json')).digest('hex');
check('snapshot file pin unchanged', h === 'e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d');

// 6: CLOSE-OUT guards (active once the aggregate receipt exists) — wave-3/4/5/6 pattern
const recPath = '/home/z/my-project/download/wave7/wave7-receipt.json';
if (fs.existsSync(recPath)) {
  const rec = JSON.parse(fs.readFileSync(recPath, 'utf8'));
  check('aggregate wave7-receipt.json present', true);
  check('receipt format of record', rec.format === 'wave7-receipt/0.1', rec.format);
  check('receipt register 9/9', Array.isArray(rec.perNote) && rec.perNote.length === 9, rec.perNote ? `perNote ${rec.perNote.length}` : 'missing');
  check('receipt totals reconcile receipt-vs-disk', rec.totals && rec.totals.checks === tally.checks && rec.totals.keyPoints === tally.keyPoints && rec.totals.glossaryTerms === tally.glossary && rec.totals.lessons === 19,
    `receipt ${rec.totals ? rec.totals.lessons + 'L/' + rec.totals.checks + '/' + rec.totals.keyPoints + '/' + rec.totals.glossaryTerms : 'n/a'} vs disk 19L/${tally.checks}/${tally.keyPoints}/${tally.glossary}`);
  const warnLines = Object.values(rec.warningInventory || {}).reduce((a, b) => a + b, 0);
  check('warning inventory reconciles to 9 designed', warnLines === 9, `inventory lines ${warnLines}`);
  check('warning inventory single class (workedExample-null)', Object.keys(rec.warningInventory || {}).every(k => k.startsWith('arithmetic-truth: workedExample is null')), Object.keys(rec.warningInventory || {}).join(' || ').slice(0, 80));
  check('recalibration decision block (4 items, wave-1 basis)', Array.isArray(rec.recalibration && rec.recalibration.decisionOfRecord) && rec.recalibration.decisionOfRecord.length === 4 && rec.recalibration.wave1BasisOfRecord && rec.recalibration.wave1BasisOfRecord.meanSecondsPerNote === 283);
  check('event-log ground truth 9 entries', Array.isArray(rec.eventLogGroundTruth) && rec.eventLogGroundTruth.length === 9, rec.eventLogGroundTruth ? `entries ${rec.eventLogGroundTruth.length}` : 'missing');
  check('zero-DB statement present', typeof rec.corpusPin.dbContact === 'string' && rec.corpusPin.dbContact.startsWith('ZERO database contact'));
  check('receipt pin matches recomputed snapshot pin', rec.corpusPin.snapshotFilePinSha256RecomputedThisRound === h);
  check('wave-7 deliverables complete incl. receipt (19 files)', w7.length === 19, `count ${w7.length}`);
  check('topic census: T2 complete 36/36 with 8/8 subtopics closed', rec.topicCensus && rec.topicCensus['2. Inorganic Chemistry'] && rec.topicCensus['2. Inorganic Chemistry'].complete === true && rec.topicCensus['2. Inorganic Chemistry'].subtopicsClosed === 8,
    rec.topicCensus ? rec.topicCensus['2. Inorganic Chemistry'].notes : 'missing');
}
const reportPath = '/home/z/my-project/download/Wave-7-Authoring-Wave-Report-20261025.docx';
check('wave-7 report DOCX present', fs.existsSync(reportPath), reportPath.split('/').pop());

console.log(fails ? `\n${fails} FAILURES` : '\nALL CHECKS PASS');
process.exit(fails ? 1 : 0);
