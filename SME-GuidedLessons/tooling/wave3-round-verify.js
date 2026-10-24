#!/usr/bin/env node
// wave3-round-verify.js — round-close verification, extended in place per round (latest: W3 notes 11-12, the wave's tail pair; wave at 12/12).
// 1. Each new timing receipt matches its snapshot row on the 7 pin fields.
// 2. Layer noteRef matches the pinned chain; schema PASS + lint designed-or-none recorded.
// 3. Wave-3 running tally recomputed from receipts on disk.
// 4. Guards: wave-1 (22 files) + wave-2 (25 files incl. aggregate receipt) + wave-3 counts.
// 5. Snapshot file pin unchanged.
const fs = require('fs');
const crypto = require('crypto');
const snap = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));

let fails = 0;
function check(name, ok, detail) {
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
  if (!ok) fails++;
}

// 1+2: new receipts vs snapshot
const newIds = ['rn_Syxyh4Fct8KFg8NQ', 'rn_mBqgkpZ3hbSBmWCC', 'rn_N4HX8tqbdhTQcHyS', 'rn_VyXFNyxZHZGkxqTG', 'rn_vXPcH3vS8wv7BFkK', 'rn_pWzTTBv3B4yGFfj3', 'rn_yj4y972FxCWnDnSg', 'rn_Hkwmd9GSp3gdxxR5', 'rn_4tzwS4GZjPybwtkS', 'rn_T55t3HNsgyZcXZtN', 'rn_mbcBZkygY4YpG2bf', 'rn_8Nv33F4dD3kkZnY6'];
for (const id of newIds) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave3/timing-receipt-${id}.json`, 'utf8'));
  const row = snap.notes.find(n => n.noteId === id);
  for (const [k, v] of [['noteTitle', row.title], ['topicTitle', row.topicTitle], ['subtopicTitle', row.subtopicTitle], ['corpusVersion', row.corpusVersion], ['bodySha256', row.bodySha256], ['bodyChars', row.bodyChars]]) {
    check(`${id} receipt.${k}`, JSON.stringify(r[k]) === JSON.stringify(v), JSON.stringify(v).slice(0, 60));
  }
  check(`${id} receipt.specPointCodes`, JSON.stringify(r.specPointCodes) === JSON.stringify(row.specPointCodes), row.specPointCodes.join(','));
  const layer = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave3/guided-lesson-${id}.json`, 'utf8'));
  check(`${id} layer.noteRef`, layer.noteRef.noteId === id && layer.noteRef.corpusVersion === row.corpusVersion && layer.noteRef.subtopicTitle === row.subtopicTitle);
  check(`${id} schema+lint recorded`, String(r.schemaValidation).startsWith('PASS') && /hard-fails 0/.test(r.lint));
  const designed = /workedExample is null/.test(r.lint) || /no arithmetic expression found/.test(r.lint);
  check(`${id} lint warnings designed-or-none`, /warnings 0/.test(r.lint) || (designed && /warnings 1/.test(r.lint)), designed ? '1 designed (non-numeric or absent workedExample, declared)' : 'clean');
  check(`${id} chain discipline`, JSON.stringify(r.assistedPhases) === JSON.stringify(['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']), 'assistedPhases = P1..P7');
  check(`${id} zero pauses`, r.pauseLog.length === 0);
}

// 3: wave-3 running tally from receipts on disk
const files = fs.readdirSync('/home/z/my-project/download/wave3').filter(f => f.startsWith('timing-receipt-'));
let tally = { notes: files.length, checks: 0, keyPoints: 0, glossary: 0, focused: 0, pauses: 0 };
const perNote = [];
for (const f of files) {
  const r = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave3/${f}`, 'utf8'));
  const layer = JSON.parse(fs.readFileSync(r.layerFile, 'utf8'));
  const checks = layer.lessons.reduce((a, L) => a + L.check.length, 0);
  tally.checks += checks;
  tally.keyPoints += layer.lessons.reduce((a, L) => a + L.keyPoints.length, 0);
  tally.glossary += layer.noteAssets.glossary.length;
  tally.focused += r.totalSeconds;
  tally.pauses += r.pauseLog.length;
  perNote.push(`${r.noteId}: ${layer.lessons.length}L ${checks}chk ${r.totalSeconds}s`);
}
console.log('--- wave-3 tally:', JSON.stringify(tally));
console.log(perNote.join('\n'));

// 4: guards
const w1 = fs.readdirSync('/home/z/my-project/download/wave1');
check('wave-1 deliverables intact (22 files incl. pin reverify)', w1.length === 22, `count ${w1.length}`);
const w2 = fs.readdirSync('/home/z/my-project/download/wave2');
check('wave-2 deliverables intact (25 files incl. aggregate receipt)', w2.length === 25, `count ${w2.length}`);
const w3 = fs.readdirSync('/home/z/my-project/download/wave3');
check('wave-3 deliverables complete (24 files: 12 layers + 12 receipts)', w3.length === 24, `count ${w3.length}`);
const runs3 = fs.readdirSync('/home/z/my-project/.tmp/wave3/runs');
check('wave-3 event logs persisted (12)', runs3.length === 12, `count ${runs3.length}`);
// notes-5-6 repair transparency: both logs must carry exactly one reExport:true export
for (const id of ['rn_vXPcH3vS8wv7BFkK', 'rn_pWzTTBv3B4yGFfj3']) {
  const ev = JSON.parse(fs.readFileSync(`/home/z/my-project/.tmp/wave3/runs/${id}.events.json`, 'utf8'));
  const reExp = ev.filter(e => e.type === 'export' && e.reExport === true);
  const p8ends = ev.filter(e => e.type === 'phase-end' && e.phase === 'P8');
  const p0end = ev.find(e => e.type === 'phase-end' && e.phase === 'P0');
  check(`${id} reExport trail (1 re-export, single P8 close, P0 unflagged)`, reExp.length === 1 && p8ends.length === 1 && p0end.assist === false, `exports ${ev.filter(e => e.type === 'export').length}, reExports ${reExp.length}`);
}

// 5: snapshot file pin
const h = crypto.createHash('sha256').update(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json')).digest('hex');
check('snapshot file pin unchanged', h === 'e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d');

console.log(fails ? `\n${fails} FAILURES` : '\nALL CHECKS PASS');
process.exit(fails ? 1 : 0);
