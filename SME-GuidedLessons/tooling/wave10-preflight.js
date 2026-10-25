#!/usr/bin/env node
// wave10-preflight.js — full pre-flight over the 12 authored layers: ajv schema + a1-lint
// per layer, designed-or-none tally, cadence tally. ALL must pass before any chain fires.
const fs = require('fs');
const { execFileSync } = require('child_process');
const Ajv = require('/home/z/node_modules/ajv');

const SNAP = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave1/corpus-snapshot.json', 'utf8'));
const REG = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave10/wave10-register.json', 'utf8'));
const ajv = new Ajv({ allErrors: true, strict: false });
const validate = ajv.compile(JSON.parse(fs.readFileSync('/home/z/my-project/scripts/guided-lesson.0.1.schema.json', 'utf8')));

let fails = 0;
const DESIGNED = 'workedExample is null — declared as none in source note';
const tally = { notes: 0, lessons: 0, checks: 0, keyPoints: 0, glossary: 0, distractors: 0, designed: 0, ports: 0, otherWarnings: 0 };

for (const r of REG.register) {
  const id = r.noteId;
  const p = `/home/z/my-project/.tmp/wave10/layer-${id}.json`;
  const layer = JSON.parse(fs.readFileSync(p, 'utf8'));
  const okSchema = validate(layer);
  if (!okSchema) { fails++; console.log(`FAIL schema ${id}:`, JSON.stringify(validate.errors)); }
  let lintOut = '';
  try { lintOut = execFileSync('node', ['/home/z/my-project/scripts/a1-lint.js', p, '--note', id], { encoding: 'utf8' }); }
  catch (e) { lintOut = e.stdout || e.message; }
  const m = lintOut.match(/hard-fails (\d+), warnings (\d+)/);
  const hard = m ? +m[1] : -1, warns = m ? +m[2] : -1;
  if (hard !== 0) { fails++; console.log(`FAIL lint ${id}: hard=${hard}\n${lintOut}`); }
  const isPort = layer.noteAssets.workedExample !== null;
  const clean = warns === 0 || (warns === 1 && lintOut.includes(DESIGNED));
  if (!clean) { fails++; console.log(`FAIL designed-or-none ${id}: warnings=${warns}\n${lintOut}`); }
  tally.notes++;
  tally.lessons += layer.lessons.length;
  tally.keyPoints += layer.lessons.reduce((a, l) => a + l.keyPoints.length, 0);
  tally.checks += layer.lessons.reduce((a, l) => a + l.check.length, 0);
  tally.distractors += layer.lessons.reduce((a, l) => a + l.check.reduce((b, c) => b + c.options.filter(o => !o.correct).length, 0), 0);
  tally.glossary += layer.noteAssets.glossary.length;
  if (isPort) tally.ports++; else tally.designed++;
  // spec coverage cross-check
  const row = SNAP.notes.find(n => n.noteId === id);
  const declared = new Set(layer.specPoints.map(s => s.code));
  const refs = new Set(layer.lessons.flatMap(l => l.specRefs));
  for (const c of row.specPointCodes) if (!refs.has(c)) { fails++; console.log(`FAIL spec coverage ${id}: ${c} unreferenced`); }
  for (const c of refs) if (!row.specPointCodes.includes(c)) { fails++; console.log(`FAIL invented code ${id}: ${c}`); }
  for (const c of declared) if (!row.specPointCodes.includes(c)) { fails++; console.log(`FAIL declared-not-of-record ${id}: ${c}`); }
  for (const s of layer.specPoints) if (s.text !== REG.specTexts[s.code]) { fails++; console.log(`FAIL spec text mismatch ${id}: ${s.code}`); }
  console.log(`OK ${id} (${row.title}): schema ${okSchema ? 'PASS' : 'FAIL'}, lint hard ${hard}, warnings ${warns}${warns === 1 && lintOut.includes(DESIGNED) ? ' (designed)' : ''}`);
}

console.log('--- cadence tally ---');
console.log(JSON.stringify(tally));
console.log(fails ? `PREFLIGHT FAILS: ${fails}` : 'ALL PREFLIGHT CHECKS PASS (designed-or-none achieved before any chain)');
process.exit(fails ? 1 : 0);
