#!/usr/bin/env node
// wave9-prep.js — WAVE-9 OPEN entry discipline (trace 1a174b960e367b61 verbatim "Go wave-9").
// Zero-DB: bodies + pins from the local snapshot of record (pin re-verified); spec texts
// from the graph content pack specification_points.yaml (parity re-proven against wave-5
// of-record texts). Mirror of wave8-prep.js with wave-9 duties.
const fs = require('fs');
const crypto = require('crypto');
const yaml = require('/home/z/node_modules/js-yaml');

const SNAP = '/home/z/my-project/.tmp/wave1/corpus-snapshot.json';
const PACE = '/home/z/my-project/download/wave-pacing-open-20261024.json';
const PACK = '/home/z/my-project/.tmp/wave5/specification_points.yaml';
const OUT = '/home/z/my-project/.tmp/wave9';

const snap = JSON.parse(fs.readFileSync(SNAP, 'utf8'));
const pace = JSON.parse(fs.readFileSync(PACE, 'utf8'));
const pack = yaml.load(fs.readFileSync(PACK, 'utf8'));

let fails = 0;
function check(name, ok, detail) {
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
  if (!ok) fails++;
}

// ── 1. register vs snapshot (four-way pattern) ──
const w9 = pace.wavePlan.find(w => w.wave === 9);
check('wavePlan wave-9 present', !!w9, w9 ? w9.topic : 'missing');
const ids = w9.register.map(r => r.noteId);
check('register 12 notes', ids.length === 12, `count ${ids.length}`);
check('register unique IDs', new Set(ids).size === 12);
check('register chars total 37482', w9.register.reduce((a, r) => a + r.bodyChars, 0) === 37482, `sum ${w9.register.reduce((a, r) => a + r.bodyChars, 0)}`);
const specMult = w9.register.reduce((a, r) => a + r.specPointCodes.length, 0);
check('register spec points 30 (multiplicity)', specMult === 30, `sum ${specMult}`);

// zero overlap with waves 1-8
const prior = new Set();
for (const w of ['wave1', 'wave2', 'wave3', 'wave4', 'wave5', 'wave6', 'wave7', 'wave8']) {
  const dir = `/home/z/my-project/download/${w}`;
  for (const f of fs.readdirSync(dir).filter(f => f.startsWith('timing-receipt-'))) {
    prior.add(JSON.parse(fs.readFileSync(`${dir}/${f}`, 'utf8')).noteId);
  }
}
check('prior receipt pool 92', prior.size === 92, `pool ${prior.size}`);
check('zero overlap with waves 1-8 receipts', ids.every(id => !prior.has(id)));

// register vs snapshot rows (7 pin fields + codes)
for (const r of w9.register) {
  const row = snap.notes.find(n => n.noteId === r.noteId);
  if (!row) { check(`${r.noteId} in snapshot`, false); continue; }
  const okRow = row.title === r.title && row.subtopicTitle === r.subtopic && row.bodyChars === r.bodyChars &&
    JSON.stringify(row.specPointCodes) === JSON.stringify(r.specPointCodes);
  check(`${r.noteId} register==snapshot (title/subtopic/chars/codes)`, okRow, `${row.title} | ${row.subtopicTitle} | ${row.bodyChars}ch`);
  const bodySha = crypto.createHash('sha256').update(row.body).digest('hex');
  check(`${r.noteId} bodySha256 recomputed==row`, bodySha === row.bodySha256, row.bodySha256.slice(0, 16) + '...');
}

// ── 2. spec texts from the graph pack ──
const byCode = {};
const scan = (o) => { if (Array.isArray(o)) o.forEach(scan); else if (o && typeof o === 'object') { if (o.code && o.official_wording) byCode[String(o.code).replace(/^4CH1-/, '')] = o; else Object.values(o).forEach(scan); } };
scan(pack);
check('spec pack parsed', Object.keys(byCode).length > 100, `entries ${Object.keys(byCode).length}`);

// parity proof vs wave-5 of-record texts. Probe set EXCLUDES 2.19: that code carries the
// documented wave-5 flattening treatment (pack text ends with ':' + bullet fragments joined
// with semicolons), so exact parity there would contradict the flattening of record.
const parityProbes = [['rn_5WvdZNzzhHdjj2Qq', '2.13'], ['rn_3B8JxsSjJvR9B4fk', '2.18'], ['rn_QzYRzzmwRxk2gKqV', '2.12'], ['rn_jXXsc4wt2344BjxX', '2.8C']];
let parityOk = 0;
for (const [nid, code] of parityProbes) {
  const layer = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave5/guided-lesson-${nid}.json`, 'utf8'));
  const sp = layer.specPoints.find(s => s.code === '4CH1-' + code);
  const packText = byCode[code] && byCode[code].official_wording;
  const match = sp && packText && sp.text === packText;
  if (match) parityOk++;
  else console.log(`  parity detail ${code}: layer=${JSON.stringify(sp && sp.text).slice(0, 80)} pack=${JSON.stringify(packText).slice(0, 80)}`);
}
check('pack parity vs wave-5 of-record texts (4 probes)', parityOk === parityProbes.length, `${parityOk}/${parityProbes.length} exact`);

// resolve wave-9 codes; carry official_bullets for the flattening treatment
const w9codes = [...new Set(w9.register.flatMap(r => r.specPointCodes))].sort((a, b) => {
  const pa = a.replace('4CH1-', '').split('.').map(x => parseFloat(x));
  const pb = b.replace('4CH1-', '').split('.').map(x => parseFloat(x));
  return pa[0] - pb[0] || pa[1] - pb[1];
});
const texts = {};
let missing = [];
for (const cFull of w9codes) {
  const c = cFull.replace(/^4CH1-/, '');
  const p = byCode[c];
  if (p && p.official_wording) texts[cFull] = p.official_wording; else missing.push(cFull);
}
check('all wave-9 codes resolved from pack', missing.length === 0, missing.length ? 'missing ' + missing.join(',') : w9codes.length + ' unique codes');
// Documented normalisation (wave-4/5 treatment, generalised wave-8): multi-bullet statements
// flattened to semicolon clauses, wording verbatim, fragments taken from the pack's own
// official_bullets (not re-worded).
const flattened = [];
for (const cFull of w9codes) {
  const p = byCode[cFull.replace(/^4CH1-/, '')];
  if (p && Array.isArray(p.official_bullets) && texts[cFull].endsWith(':')) {
    const frags = p.official_bullets.map(b => String(b).replace(/\.$/, ''));
    texts[cFull] = texts[cFull] + ' ' + frags.join('; ');
    flattened.push(cFull);
  }
}
check('flattening treatment disclosed (data-driven, no hardcode)', flattened.every(c => byCode[c.replace(/^4CH1-/, '')].official_bullets.length > 0), flattened.join(',') || 'none this wave');
console.log('--- wave-9 spec texts ---');
for (const c of w9codes) console.log(`  ${c}: ${JSON.stringify(texts[c])}`);

// ── 3. bodies end to end ──
fs.mkdirSync(`${OUT}/bodies`, { recursive: true });
let totalChars = 0;
for (const r of w9.register) {
  const row = snap.notes.find(n => n.noteId === r.noteId);
  fs.writeFileSync(`${OUT}/bodies/${r.noteId}.md`, row.body);
  totalChars += row.body.length;
  const headings = (row.body.match(/^#{1,6} .*$/gm) || []).map(h => h.replace(/^#+\s*/, ''));
  console.log(`BODY ${r.noteId} "${row.title}" ${row.body.length}ch | headings: ${headings.join(' | ')}`);
}
check('bodies extracted chars == 37482', totalChars === 37482, `sum ${totalChars}`);

// snapshot pin
const pin = crypto.createHash('sha256').update(fs.readFileSync(SNAP)).digest('hex');
check('snapshot pin MATCH', pin === 'e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d');

// persist the prepared register of record
fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(`${OUT}/wave9-register.json`, JSON.stringify({ format: 'wave9-register/0.1', trace: '1a174b960e367b61', wave: 9, topic: w9.topic, register: w9.register, specTexts: texts, pin }, null, 1));
console.log(fails ? `PREP FAILS: ${fails}` : 'ALL PREP CHECKS PASS');
process.exit(fails ? 1 : 0);
