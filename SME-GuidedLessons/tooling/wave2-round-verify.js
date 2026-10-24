#!/usr/bin/env node
// wave2-round-verify.js — CLOSE-OUT verification for wave-2 (register 12/12 + close-out artifacts).
// 1. Each new timing receipt matches its snapshot row on the 7 pin fields.
// 2. Layer body of each new layer matches the pinned bodySha256 chain (receipt<->snapshot).
// 3. Running wave-2 tally recomputed from the twelve receipts on disk.
// 4. Guard: wave-1 deliverables (22 files) + wave-2 files present and unchanged count-wise.
// 5. Close-out guards (minted at the 12/12 close-out round): aggregate wave2-receipt.json
//    present and internally consistent (totals reconcile to the receipts; warning inventory
//    reconciles to 6 designed lines; recalibration block carries the estimator-basis decision);
//    wave-2 report DOCX present in download/.
const fs = require('fs');
const crypto = require('crypto');
const snap = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));
const pinFile = JSON.parse(fs.readFileSync('/home/z/my-project/download/wave1/snapshot-pin-reverify-20261024.json', 'utf8'));

let fails = 0;
function check(name, ok, detail) {
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
  if (!ok) fails++;
}

// 1+2: receipts vs snapshot
const newIds = ['rn_vzGMZxqQtWYVWB7h', 'rn_b3XCzdtfQddbJjVf'];
for (const id of newIds) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave2/timing-receipt-${id}.json`, 'utf8'));
  const row = snap.notes.find(n => n.noteId === id);
  for (const [k, v] of [['noteTitle', row.title], ['topicTitle', row.topicTitle], ['subtopicTitle', row.subtopicTitle], ['corpusVersion', row.corpusVersion], ['bodySha256', row.bodySha256], ['bodyChars', row.bodyChars]]) {
    check(`${id} receipt.${k}`, JSON.stringify(r[k]) === JSON.stringify(v), JSON.stringify(v).slice(0, 60));
  }
  check(`${id} receipt.specPointCodes`, JSON.stringify(r.specPointCodes) === JSON.stringify(row.specPointCodes), row.specPointCodes.join(','));
  const layer = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave2/guided-lesson-${id}.json`, 'utf8'));
  check(`${id} layer.noteRef`, layer.noteRef.noteId === id && layer.noteRef.corpusVersion === row.corpusVersion);
  // receipt bodySha256 must match the pin file's per-note hash entry if present
  const pinRow = (pinFile.checks || []).find(c => String(c.noteId) === id);
  if (pinRow) check(`${id} pin-file hash agrees`, pinRow.bodySha256 === row.bodySha256);
  check(`${id} schema+lint recorded`, String(r.schemaValidation).startsWith('PASS') && /hard-fails 0/.test(r.lint));
  const designed = /workedExample is null/.test(r.lint) || /no arithmetic expression found/.test(r.lint);
  check(`${id} lint warnings designed-or-none`, /warnings 0/.test(r.lint) || (designed && /warnings 1/.test(r.lint)), designed ? '1 designed (non-numeric or absent workedExample, declared)' : 'clean');
}

// 3: wave-2 running tally from receipts on disk
const files = fs.readdirSync('/home/z/my-project/download/wave2').filter(f => f.startsWith('timing-receipt-'));
let tally = { notes: files.length, checks: 0, keyPoints: 0, glossary: 0, focused: 0, pauses: 0 };
const perNote = [];
for (const f of files) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave2/${f}`, 'utf8'));
  const layer = JSON.parse(fs.readFileSync(r.layerFile, 'utf8'));
  const checks = layer.lessons.reduce((a, L) => a + L.check.length, 0);
  tally.checks += checks;
  tally.keyPoints += layer.lessons.reduce((a, L) => a + L.keyPoints.length, 0);
  tally.glossary += layer.noteAssets.glossary.length;
  tally.focused += r.totalSeconds;
  tally.pauses += r.pauseLog.length;
  perNote.push(`${r.noteId}: ${layer.lessons.length}L ${checks}chk ${r.totalSeconds}s`);
}
console.log('--- wave-2 tally:', JSON.stringify(tally));
console.log(perNote.join('\n'));

// 4: guards
const w1 = fs.readdirSync('/home/z/my-project/download/wave1');
check('wave-1 deliverables intact (22 files incl. pin reverify)', w1.length === 22, `count ${w1.length}`);
const w2 = fs.readdirSync('/home/z/my-project/download/wave2');
const h = crypto.createHash('sha256').update(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json')).digest('hex');
check('snapshot file pin unchanged', h === 'e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d');

// 5: close-out guards
const recPath = '/home/z/my-project/download/wave2/wave2-receipt.json';
check('aggregate wave2-receipt.json present', fs.existsSync(recPath));
if (fs.existsSync(recPath)) {
  const rec = JSON.parse(fs.readFileSync(recPath, 'utf8'));
  check('receipt format of record', rec.format === 'wave2-receipt/0.1', rec.format);
  check('receipt register 12/12', Array.isArray(rec.perNote) && rec.perNote.length === 12);
  check('receipt totals reconcile (checks 120 / keyPoints 137 / glossary 86)',
    rec.totals.checks === tally.checks && rec.totals.keyPoints === tally.keyPoints && rec.totals.glossaryTerms === tally.glossary,
    `receipt ${rec.totals.checks}/${rec.totals.keyPoints}/${rec.totals.glossaryTerms} vs disk ${tally.checks}/${tally.keyPoints}/${tally.glossary}`);
  const invLines = Object.values(rec.warningInventory || {}).reduce((a, b) => a + b, 0);
  check('warning inventory reconciles to 6 designed lines', invLines === 6, `inventory total ${invLines}`);
  check('recalibration block carries the estimator-basis decision',
    !!(rec.recalibration && rec.recalibration.decisionOfRecord && rec.recalibration.decisionOfRecord.length >= 4 &&
       /wave-1 instrumented basis/.test(rec.recalibration.decisionOfRecord[0])),
    `${(rec.recalibration?.decisionOfRecord || []).length} decision items`);
  check('event-log ground truth carried (12 entries, idempotence asserted)',
    Array.isArray(rec.eventLogGroundTruth) && rec.eventLogGroundTruth.length === 12);
  check('zero-database-contact statement of record', /ZERO database contact/.test(rec.corpusPin.dbContact || ''));
}
const reportPath = '/home/z/my-project/download/Wave-2-Authoring-Wave-Report-20261025.docx';
check('wave-2 report DOCX present', fs.existsSync(reportPath), reportPath.split('/').pop());
check('wave-2 deliverables complete incl. receipt (25 files)', w2.length === 25, `count ${w2.length}`);

console.log(fails ? `\n${fails} FAILURES` : '\nALL CHECKS PASS');
process.exit(fails ? 1 : 0);
