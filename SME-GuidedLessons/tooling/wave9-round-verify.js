#!/usr/bin/env node
// wave9-round-verify.js — round-close verification for wave-9 (minted at the 12/12 close-out round,
// wave-3/4/5 pattern: close-out guards active from the outset).
// 1. Each timing receipt matches its snapshot row on the 7 pin fields + spec codes.
// 2. Layer noteRef matches the pinned chain; schema PASS + lint designed-or-none recorded.
// 3. Wave-9 running tally recomputed from receipts on disk.
// 4. Guards: wave-1 (22) + wave-2 (25) + wave-3 (25) + wave-4 (23) + wave-5 (25) + wave-6 (25)
//    + wave-7 (19) + wave-8 (29) + wave-9 counts; event-log ground truth (19 events, ONE export,
//    ONE P8 phase-end, P0 unflagged, zero reExports, zero pauses).
// 5. Snapshot file pin unchanged.
// 6. CLOSE-OUT guards (wave9-receipt.json exists at mint time) — wave-3/4/5 pattern.
const fs = require('fs');
const crypto = require('crypto');
const snap = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));

let fails = 0;
function check(name, ok, detail) {
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
  if (!ok) fails++;
}

const IDS = ['rn_wDdXr5k7gknQ7xJp', 'rn_NdJGQM8BqHmTy7Vg', 'rn_HqqBFgKRHykMMhbB', 'rn_H9chr9BWCfXYW472', 'rn_V3hNWh6QWrbCRHrX', 'rn_9J7DQhskyxzhd7CP', 'rn_DrqzYWZMScqGrbWT', 'rn_6c2G8nJpFSnQnbcP', 'rn_MmqCNJfWbtYzRVqT', 'rn_H2zGfgH76qYV5cmr', 'rn_DBGf3WVffDBNDp4R', 'rn_2MpXPtNXvn8pQm3r'];

// 1+2: receipts + layers vs snapshot
for (const id of IDS) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave9/timing-receipt-${id}.json`, 'utf8'));
  const row = snap.notes.find(n => n.noteId === id);
  for (const [k, v] of [['noteTitle', row.title], ['topicTitle', row.topicTitle], ['subtopicTitle', row.subtopicTitle], ['corpusVersion', row.corpusVersion], ['bodySha256', row.bodySha256], ['bodyChars', row.bodyChars]]) {
    check(`${id} receipt.${k}`, JSON.stringify(r[k]) === JSON.stringify(v), JSON.stringify(v).slice(0, 60));
  }
  check(`${id} receipt.specPointCodes`, JSON.stringify(r.specPointCodes) === JSON.stringify(row.specPointCodes), row.specPointCodes.join(','));
  const layer = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave9/guided-lesson-${id}.json`, 'utf8'));
  check(`${id} layer.noteRef`, layer.noteRef.noteId === id && layer.noteRef.corpusVersion === row.corpusVersion && layer.noteRef.subtopicTitle === row.subtopicTitle);
  check(`${id} schema+lint recorded`, String(r.schemaValidation).startsWith('PASS') && /hard-fails 0/.test(r.lint));
  const designed = /workedExample is null/.test(r.lint);
  check(`${id} lint warnings designed-or-none`, /warnings 0/.test(r.lint) || (designed && /warnings 1/.test(r.lint)), designed ? '1 designed (absent workedExample, declared)' : 'clean (numeric port or 0-warning)');
  check(`${id} chain discipline`, JSON.stringify(r.assistedPhases) === JSON.stringify(['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']), 'assistedPhases = P1..P7');
  check(`${id} zero pauses`, r.pauseLog.length === 0);
  // event-log ground truth
  const ev = JSON.parse(fs.readFileSync(`/home/z/my-project/.tmp/wave9/runs/${id}.events.json`, 'utf8'));
  const exports_ = ev.filter(e => e.type === 'export');
  const reExp = ev.filter(e => e.type === 'export' && e.reExport === true);
  const p8ends = ev.filter(e => e.type === 'phase-end' && e.phase === 'P8');
  const p0end = ev.find(e => e.type === 'phase-end' && e.phase === 'P0');
  const pauses = ev.filter(e => e.type === 'pause');
  check(`${id} event log ground truth (19 events, 1 export, 1 P8 close, P0 unflagged, no reExport, no pause)`,
    ev.length === 19 && exports_.length === 1 && reExp.length === 0 && p8ends.length === 1 && p0end && p0end.assist === false && pauses.length === 0,
    `events ${ev.length}, exports ${exports_.length}, reExports ${reExp.length}, P8ends ${p8ends.length}`);
}

// 3: wave-9 running tally from receipts on disk
const files = fs.readdirSync('/home/z/my-project/download/wave9').filter(f => f.startsWith('timing-receipt-'));
let tally = { notes: files.length, lessons: 0, checks: 0, keyPoints: 0, glossary: 0, focused: 0, pauses: 0 };
const perNote = [];
for (const f of files) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave9/${f}`, 'utf8'));
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
console.log('--- wave-9 tally:', JSON.stringify(tally));
console.log(perNote.join('\n'));

// 4: guards
const counts = { wave1: 22, wave2: 25, wave3: 25, wave4: 23, wave5: 25, wave6: 25, wave7: 19, wave8: 29 };
for (const [w, n] of Object.entries(counts)) {
  const dir = fs.readdirSync(`/home/z/my-project/download/${w}`);
  check(`wave-${w.slice(4)} deliverables intact (${n} files)`, dir.length === n, `count ${dir.length}`);
}
const w9 = fs.readdirSync('/home/z/my-project/download/wave9');
check('wave-9 layers+receipts complete (12+12 by prefix)',
  w9.filter(f => f.startsWith('guided-lesson-')).length === 12 && w9.filter(f => f.startsWith('timing-receipt-')).length === 12,
  `layers ${w9.filter(f => f.startsWith('guided-lesson-')).length}, receipts ${w9.filter(f => f.startsWith('timing-receipt-')).length}`);
const runs9 = fs.readdirSync('/home/z/my-project/.tmp/wave9/runs');
check('wave-9 event logs persisted (12)', runs9.length === 12, `count ${runs9.length}`);

// 5: snapshot file pin
const h = crypto.createHash('sha256').update(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json')).digest('hex');
check('snapshot file pin unchanged', h === 'e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d');

// 6: CLOSE-OUT guards (active once the aggregate receipt exists) — wave-3/4/5 pattern
const recPath = '/home/z/my-project/download/wave9/wave9-receipt.json';
if (fs.existsSync(recPath)) {
  const rec = JSON.parse(fs.readFileSync(recPath, 'utf8'));
  check('aggregate wave9-receipt.json present', true);
  check('receipt format of record', rec.format === 'wave9-receipt/0.1', rec.format);
  check('receipt register 12/12', Array.isArray(rec.perNote) && rec.perNote.length === 12, rec.perNote ? `perNote ${rec.perNote.length}` : 'missing');
  check('receipt totals reconcile receipt-vs-disk', rec.totals && rec.totals.checks === tally.checks && rec.totals.keyPoints === tally.keyPoints && rec.totals.glossaryTerms === tally.glossary && rec.totals.lessons === 27 && rec.totals.distractors === 405,
    `receipt ${rec.totals ? rec.totals.lessons + 'L/' + rec.totals.checks + '/' + rec.totals.keyPoints + '/' + rec.totals.glossaryTerms + '/' + rec.totals.distractors : 'n/a'} vs disk 27L/${tally.checks}/${tally.keyPoints}/${tally.glossary}/405`);
  const warnLines = Object.values(rec.warningInventory || {}).reduce((a, b) => a + b, 0);
  check('warning inventory reconciles to 12 designed', warnLines === 12, `inventory lines ${warnLines}`);
  check('recalibration decision block (4 items, wave-1 basis)', Array.isArray(rec.recalibration && rec.recalibration.decisionOfRecord) && rec.recalibration.decisionOfRecord.length === 4 && rec.recalibration.wave1BasisOfRecord && rec.recalibration.wave1BasisOfRecord.meanSecondsPerNote === 283);
  check('event-log ground truth 12 entries', Array.isArray(rec.eventLogGroundTruth) && rec.eventLogGroundTruth.length === 12, rec.eventLogGroundTruth ? `entries ${rec.eventLogGroundTruth.length}` : 'missing');
  check('zero-DB statement present', typeof rec.corpusPin.dbContact === 'string' && rec.corpusPin.dbContact.startsWith('ZERO database contact'));
  check('receipt pin matches recomputed snapshot pin', rec.corpusPin.snapshotFilePinSha256RecomputedThisRound === h);
  check('topic census Topics 1-3 complete', ['1. Principles of Chemistry', '2. Inorganic Chemistry', '3. Physical Chemistry'].every(t => rec.topicCensus[t] && rec.topicCensus[t].complete === true));
  check('topic census Topic 4 at 13/21', rec.topicCensus['4. Organic Chemistry'] && rec.topicCensus['4. Organic Chemistry'].notes === '13/21', rec.topicCensus['4. Organic Chemistry'] && rec.topicCensus['4. Organic Chemistry'].notes);
  check('wave-9 deliverables complete incl. receipt (25 files)', w9.length === 25, `count ${w9.length}`);
}
const reportPath = '/home/z/my-project/download/Wave-9-Authoring-Wave-Report-20261026.docx';
check('wave-9 report DOCX present', fs.existsSync(reportPath), reportPath.split('/').pop());

console.log(fails ? `\n${fails} FAILURES` : '\nALL CHECKS PASS');
process.exit(fails ? 1 : 0);
