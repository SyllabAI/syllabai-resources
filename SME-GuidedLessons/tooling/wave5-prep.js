#!/usr/bin/env node
// wave5-prep.js — WAVE-5 OPEN entry discipline (trace 1a1725e0cd20eb8d "wave-5 open").
// Zero-DB: bodies + pins from the local snapshot of record; spec texts from the graph
// content pack specification_points.yaml (parity-proven against wave-4 of-record texts).
const fs = require('fs');
const crypto = require('crypto');
const yaml = require('/home/z/node_modules/js-yaml');

const SNAP = '/home/z/my-project/.tmp/wave1/corpus-snapshot.json';
const PACE = '/home/z/my-project/download/wave-pacing-open-20261024.json';
const PACK = '/home/z/my-project/.tmp/wave5/specification_points.yaml';
const OUT = '/home/z/my-project/.tmp/wave5';

const snap = JSON.parse(fs.readFileSync(SNAP, 'utf8'));
const pace = JSON.parse(fs.readFileSync(PACE, 'utf8'));
const pack = yaml.load(fs.readFileSync(PACK, 'utf8'));

let fails = 0;
function check(name, ok, detail) {
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
  if (!ok) fails++;
}

// ── 1. register vs snapshot (wave-4 four-way pattern) ──
const w5 = pace.wavePlan.find(w => w.wave === 5);
check('wavePlan wave-5 present', !!w5, w5 ? w5.topic : 'missing');
const ids = w5.register.map(r => r.noteId);
check('register 12 notes', ids.length === 12, `count ${ids.length}`);
check('register unique IDs', new Set(ids).size === 12);
check('register chars total 30208', w5.register.reduce((a, r) => a + r.bodyChars, 0) === 30208, `sum ${w5.register.reduce((a, r) => a + r.bodyChars, 0)}`);
check('register spec points 18 (multiplicity)', w5.register.reduce((a, r) => a + r.specPointCodes.length, 0) === 18);

// zero overlap with waves 1-4
const prior = new Set();
for (const w of ['wave1', 'wave2', 'wave3', 'wave4']) {
  const dir = `/home/z/my-project/download/${w}`;
  for (const f of fs.readdirSync(dir).filter(f => f.startsWith('timing-receipt-'))) {
    prior.add(JSON.parse(fs.readFileSync(`${dir}/${f}`, 'utf8')).noteId);
  }
}
check('zero overlap with waves 1-4 receipts', ids.every(id => !prior.has(id)), `prior pool ${prior.size}`);

// register vs snapshot rows (7 pin fields + codes)
for (const r of w5.register) {
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
for (const p of (pack.points || pack.spec_points || pack.nodes || [])) {
  const code = (p.code || '').replace(/^4CH1-/, '');
  byCode[code] = p;
}
if (!Object.keys(byCode).length) { // fallback: scan raw entries
  const raw = yaml.load(fs.readFileSync(PACK, 'utf8'));
  const scan = (o) => { if (Array.isArray(o)) o.forEach(scan); else if (o && typeof o === 'object') { if (o.code && o.official_wording) byCode[String(o.code).replace(/^4CH1-/, '')] = o; else Object.values(o).forEach(scan); } };
  scan(raw);
}
check('spec pack parsed', Object.keys(byCode).length > 100, `entries ${Object.keys(byCode).length}`);

// parity proof vs wave-4 of-record texts
const parityProbes = [['rn_J7ZcTWyRxRgWQ45R', '1.39'], ['rn_FCnWFz9MhgsqnZGM', '1.37'], ['rn_FCnWFz9MhgsqnZGM', '1.40'], ['rn_jVwPmjqHbqQkXcjG', '1.41']];
let parityOk = 0;
for (const [nid, code] of parityProbes) {
  const layer = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave4/guided-lesson-${nid}.json`, 'utf8'));
  const sp = layer.specPoints.find(s => s.code === '4CH1-' + code);
  const packText = byCode[code] && byCode[code].official_wording;
  const match = sp && packText && sp.text === packText;
  if (match) parityOk++;
  else console.log(`  parity detail ${code}: layer=${JSON.stringify(sp && sp.text).slice(0, 80)} pack=${JSON.stringify(packText).slice(0, 80)}`);
}
check('pack parity vs wave-4 of-record texts (4 probes)', parityOk === parityProbes.length, `${parityOk}/${parityProbes.length} exact`);

// resolve wave-5 codes
const w5codes = [...new Set(w5.register.flatMap(r => r.specPointCodes))].sort();
const texts = {};
let missing = [];
for (const cFull of w5codes) {
  const c = cFull.replace(/^4CH1-/, '');
  const p = byCode[c];
  if (p && p.official_wording) texts[cFull] = p.official_wording; else missing.push(cFull);
}
check('all wave-5 codes resolved from pack', missing.length === 0, missing.length ? 'missing ' + missing.join(',') : w5codes.length + ' codes');
// Documented normalisation (wave-4 treatment extended): multi-bullet statements flattened
// to semicolon clauses, wording verbatim. Bullet fragments extracted from the pack itself.
const BULLETS = {
  '2.15': 'water; dilute hydrochloric or sulfuric acid',
  '2.16': 'metals and metal oxides; metals and aqueous solutions of metal salts',
  '2.19': 'barrier methods; galvanising; sacrificial protection',
};
for (const [code, frag] of Object.entries(BULLETS)) {
  const k = '4CH1-' + code;
  if (texts[k] && texts[k].endsWith(':')) texts[k] = texts[k] + ' ' + frag;
}
console.log('--- wave-5 spec texts ---');
for (const c of w5codes) console.log(`  ${c}: ${JSON.stringify(texts[c])}`);

// ── 3. bodies end to end ──
fs.mkdirSync(`${OUT}/bodies`, { recursive: true });
let totalChars = 0;
for (const r of w5.register) {
  const row = snap.notes.find(n => n.noteId === r.noteId);
  fs.writeFileSync(`${OUT}/bodies/${r.noteId}.md`, row.body);
  totalChars += row.body.length;
  const headings = (row.body.match(/^#{1,6} .*$/gm) || []).map(h => h.replace(/^#+\s*/, ''));
  console.log(`BODY ${r.noteId} "${row.title}" ${row.body.length}ch | headings: ${headings.join(' | ')}`);
}
check('bodies extracted chars == 30208', totalChars === 30208, `sum ${totalChars}`);

// snapshot pin
const pin = crypto.createHash('sha256').update(fs.readFileSync(SNAP)).digest('hex');
check('snapshot pin MATCH', pin === 'e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d');

// persist the prepared register of record
fs.writeFileSync(`${OUT}/wave5-register.json`, JSON.stringify({
  format: 'wave5-register/0.1', at: new Date().toISOString(), ignitionTrace: '1a1725e0cd20eb8d',
  topic: w5.topic, register: w5.register, specTexts: texts, snapshotPin: pin,
}, null, 1));
console.log(fails ? `\n${fails} FAILURES` : '\nALL PREP CHECKS PASS');
process.exit(fails ? 1 : 0);
