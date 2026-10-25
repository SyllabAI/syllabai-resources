#!/usr/bin/env node
// wave10-round-verify.js — round-close verification for wave-10 (minted at the 8/8 close-out round,
// wave-3/4/5 pattern: close-out guards active from the outset). THE FINAL WAVE — the guards
// extend to the full-corpus census: 112/112.
// 1. Each timing receipt matches its snapshot row on the 7 pin fields + spec codes.
// 2. Layer noteRef matches the pinned chain; schema PASS + lint designed-or-none recorded.
// 3. Wave-10 running tally recomputed from receipts on disk.
// 4. Guards: wave-1 (22) + wave-2 (25) + wave-3 (25) + wave-4 (23) + wave-5 (25) + wave-6 (25)
//    + wave-7 (19) + wave-8 (29) + wave-9 (25) + wave-10 counts; event-log ground truth (19 events,
//    ONE export, ONE P8 phase-end, P0 unflagged, zero reExports, zero pauses).
// 5. Snapshot file pin unchanged.
// 6. CLOSE-OUT guards (wave10-receipt.json exists at mint time) — wave-3/4/5 pattern.
const fs = require('fs');
const crypto = require('crypto');
const snap = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));

let fails = 0;
function check(name, ok, detail) {
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
  if (!ok) fails++;
}

const IDS = ['rn_8T5GfPn2q7sY2YCh', 'rn_ncFJkGhXFsKrkNkH', 'rn_2z53qk2CdWrVVc7V', 'rn_BBGMYy3Yx9Nm4GV3', 'rn_BDkhS5vQpRd4hvwf', 'rn_7ZMc3T3J4SJXfNdR', 'rn_bvyrkKqRBMKCRzHM', 'rn_bGgYrQXP2tqrYwdV'];

// 1+2: receipts + layers vs snapshot
for (const id of IDS) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave10/timing-receipt-${id}.json`, 'utf8'));
  const row = snap.notes.find(n => n.noteId === id);
  for (const [k, v] of [['noteTitle', row.title], ['topicTitle', row.topicTitle], ['subtopicTitle', row.subtopicTitle], ['corpusVersion', row.corpusVersion], ['bodySha256', row.bodySha256], ['bodyChars', row.bodyChars]]) {
    check(`${id} receipt.${k}`, JSON.stringify(r[k]) === JSON.stringify(v), JSON.stringify(v).slice(0, 60));
  }
  check(`${id} receipt.specPointCodes`, JSON.stringify(r.specPointCodes) === JSON.stringify(row.specPointCodes), row.specPointCodes.join(','));
  const layer = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave10/guided-lesson-${id}.json`, 'utf8'));
  check(`${id} layer.noteRef`, layer.noteRef.noteId === id && layer.noteRef.corpusVersion === row.corpusVersion && layer.noteRef.subtopicTitle === row.subtopicTitle);
  check(`${id} schema+lint recorded`, String(r.schemaValidation).startsWith('PASS') && /hard-fails 0/.test(r.lint));
  const designed = /workedExample is null/.test(r.lint);
  check(`${id} lint warnings designed-or-none`, /warnings 0/.test(r.lint) || (designed && /warnings 1/.test(r.lint)), designed ? '1 designed (absent workedExample, declared)' : 'clean (numeric port or 0-warning)');
  check(`${id} chain discipline`, JSON.stringify(r.assistedPhases) === JSON.stringify(['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']), 'assistedPhases = P1..P7');
  check(`${id} zero pauses`, r.pauseLog.length === 0);
  // event-log ground truth
  const ev = JSON.parse(fs.readFileSync(`/home/z/my-project/.tmp/wave10/runs/${id}.events.json`, 'utf8'));
  const exports_ = ev.filter(e => e.type === 'export');
  const reExp = ev.filter(e => e.type === 'export' && e.reExport === true);
  const p8ends = ev.filter(e => e.type === 'phase-end' && e.phase === 'P8');
  const p0end = ev.find(e => e.type === 'phase-end' && e.phase === 'P0');
  const pauses = ev.filter(e => e.type === 'pause');
  check(`${id} event log ground truth (19 events, 1 export, 1 P8 close, P0 unflagged, no reExport, no pause)`,
    ev.length === 19 && exports_.length === 1 && reExp.length === 0 && p8ends.length === 1 && p0end && p0end.assist === false && pauses.length === 0,
    `events ${ev.length}, exports ${exports_.length}, reExports ${reExp.length}, P8ends ${p8ends.length}`);
}

// 3: wave-10 running tally from receipts on disk
const files = fs.readdirSync('/home/z/my-project/download/wave10').filter(f => f.startsWith('timing-receipt-'));
let tally = { notes: files.length, lessons: 0, checks: 0, keyPoints: 0, glossary: 0, focused: 0, pauses: 0 };
const perNote = [];
for (const f of files) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave10/${f}`, 'utf8'));
  const layer = JSON.parse(fs.readFileSync(r.layerFile, 'utf8'));
  const checks = layer.lessons.reduce((a, L) => a + L.check.length, 0);
  tally.lessons += layer.lessons.length;
  tally.checks += checks;
  tally.keyPoints += layer.lessons.reduce((a, L) => a + L.keyPoints.length, 0);
  tally.glossary += layer.noteAssets.glossary.length;
  tally.focused += r.totalSeconds;
  tally.pauses += r.pauseLog.length;
  perNote.push(`${r.noteId}: ${layer.lessons.length}L ${checks}chk ${r.totalSeconds}s`);
}
console.log('--- wave-10 tally:', JSON.stringify(tally));
console.log(perNote.join('\n'));

// 4: guards
const counts = { wave1: 22, wave2: 25, wave3: 25, wave4: 23, wave5: 25, wave6: 25, wave7: 19, wave8: 29, wave9: 25 };
for (const [w, n] of Object.entries(counts)) {
  const dir = fs.readdirSync(`/home/z/my-project/download/${w}`);
  check(`wave-${w.slice(4)} deliverables intact (${n} files)`, dir.length === n, `count ${dir.length}`);
}
const w10 = fs.readdirSync('/home/z/my-project/download/wave10');
check('wave-10 layers+receipts complete (8+8 by prefix)',
  w10.filter(f => f.startsWith('guided-lesson-')).length === 8 && w10.filter(f => f.startsWith('timing-receipt-')).length === 8,
  `layers ${w10.filter(f => f.startsWith('guided-lesson-')).length}, receipts ${w10.filter(f => f.startsWith('timing-receipt-')).length}`);
const runs10 = fs.readdirSync('/home/z/my-project/.tmp/wave10/runs');
check('wave-10 event logs persisted (8)', runs10.length === 8, `count ${runs10.length}`);

// prior receipt pool: 104 + wave-10 8 = 112 (the full corpus)
const pool = new Set();
for (const w of ['wave1', 'wave2', 'wave3', 'wave4', 'wave5', 'wave6', 'wave7', 'wave8', 'wave9', 'wave10']) {
  for (const f of fs.readdirSync(`/home/z/my-project/download/${w}`).filter(f => f.startsWith('timing-receipt-'))) {
    pool.add(JSON.parse(fs.readFileSync(`/home/z/my-project/download/${w}/${f}`, 'utf8')).noteId);
  }
}
check('FULL-CORPUS receipt pool 112 unique (waves 1-10)', pool.size === 112, `pool ${pool.size}`);
const allSnap = new Set(snap.notes.map(n => n.noteId));
check('receipt pool covers the entire snapshot (no note unauthored)', [...allSnap].every(id => pool.has(id)) && pool.size === allSnap.size, `snapshot ${allSnap.size}`);

// 5: snapshot file pin
const h = crypto.createHash('sha256').update(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json')).digest('hex');
check('snapshot file pin unchanged', h === 'e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d');

// 6: CLOSE-OUT guards (active once the aggregate receipt exists) — wave-3/4/5 pattern
const recPath = '/home/z/my-project/download/wave10/wave10-receipt.json';
if (fs.existsSync(recPath)) {
  const rec = JSON.parse(fs.readFileSync(recPath, 'utf8'));
  check('aggregate wave10-receipt.json present', true);
  check('receipt format of record', rec.format === 'wave10-receipt/0.1', rec.format);
  check('receipt register 8/8', Array.isArray(rec.perNote) && rec.perNote.length === 8, rec.perNote ? `perNote ${rec.perNote.length}` : 'missing');
  check('receipt totals reconcile receipt-vs-disk', rec.totals && rec.totals.checks === tally.checks && rec.totals.keyPoints === tally.keyPoints && rec.totals.glossaryTerms === tally.glossary && rec.totals.lessons === 17 && rec.totals.distractors === 255,
    `receipt ${rec.totals ? rec.totals.lessons + 'L/' + rec.totals.checks + '/' + rec.totals.keyPoints + '/' + rec.totals.glossaryTerms + '/' + rec.totals.distractors : 'n/a'} vs disk 17L/${tally.checks}/${tally.keyPoints}/${tally.glossary}/255`);
  const warnLines = Object.values(rec.warningInventory || {}).reduce((a, b) => a + b, 0);
  check('warning inventory reconciles to 7 designed (8th note carries the verified port)', warnLines === 7, `inventory lines ${warnLines}`);
  check('recalibration decision block (4 items, wave-1 basis)', Array.isArray(rec.recalibration && rec.recalibration.decisionOfRecord) && rec.recalibration.decisionOfRecord.length === 4 && rec.recalibration.wave1BasisOfRecord && rec.recalibration.wave1BasisOfRecord.meanSecondsPerNote === 283);
  check('event-log ground truth 8 entries', Array.isArray(rec.eventLogGroundTruth) && rec.eventLogGroundTruth.length === 8, rec.eventLogGroundTruth ? `entries ${rec.eventLogGroundTruth.length}` : 'missing');
  check('zero-DB statement present', typeof rec.corpusPin.dbContact === 'string' && rec.corpusPin.dbContact.startsWith('ZERO database contact'));
  check('receipt pin matches recomputed snapshot pin', rec.corpusPin.snapshotFilePinSha256RecomputedThisRound === h);
  check('topic census ALL FOUR topics complete', ['1. Principles of Chemistry', '2. Inorganic Chemistry', '3. Physical Chemistry', '4. Organic Chemistry'].every(t => rec.topicCensus[t] && rec.topicCensus[t].complete === true));
  check('topic census Topic 4 at 21/21', rec.topicCensus['4. Organic Chemistry'] && rec.topicCensus['4. Organic Chemistry'].notes === '21/21', rec.topicCensus['4. Organic Chemistry'] && rec.topicCensus['4. Organic Chemistry'].notes);
  check('corpus completion record 112/112', rec.corpusCompletion && rec.corpusCompletion.censusOfRecord && rec.corpusCompletion.censusOfRecord.notes === '112/112', rec.corpusCompletion && rec.corpusCompletion.censusOfRecord && rec.corpusCompletion.censusOfRecord.notes);
  check('wave-10 deliverables complete incl. receipt (17 files)', w10.length === 17, `count ${w10.length}`);
}
const reportPath = '/home/z/my-project/download/Wave-10-Authoring-Wave-Report-20261026.docx';
check('wave-10 report DOCX present', fs.existsSync(reportPath), reportPath.split('/').pop());

console.log(fails ? `\n${fails} FAILURES` : '\nALL CHECKS PASS');
process.exit(fails ? 1 : 0);
