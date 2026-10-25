#!/usr/bin/env node
// wave6-prep.js — WAVE-6 OPEN entry discipline (operator "Continue" ignition, recorded NEXT
// from the wave-5 close-out). Zero-DB: bodies + pins from the local snapshot of record; spec
// texts from the graph content pack specification_points.yaml (parity-proven against the
// wave-5 of-record texts). Wave-5 pattern: scripts/wave5-prep.js.
const fs = require('fs');
const crypto = require('crypto');
const yaml = require('/home/z/node_modules/js-yaml');

const SNAP = '/home/z/my-project/.tmp/wave1/corpus-snapshot.json';
const PACE = '/home/z/my-project/download/wave-pacing-open-20261024.json';
const PACK = '/home/z/my-project/.tmp/wave6/specification_points.yaml';
const OUT = '/home/z/my-project/.tmp/wave6';

fs.mkdirSync(OUT, { recursive: true });
// provenance: the pack travels with the wave working dir (copied from the wave-5 location,
// which was itself parity-proven at wave-5 open against the wave-4 of-record texts)
if (!fs.existsSync(PACK)) fs.copyFileSync('/home/z/my-project/.tmp/wave5/specification_points.yaml', PACK);

const snap = JSON.parse(fs.readFileSync(SNAP, 'utf8'));
const pace = JSON.parse(fs.readFileSync(PACE, 'utf8'));
const pack = yaml.load(fs.readFileSync(PACK, 'utf8'));

let fails = 0;
function check(name, ok, detail) {
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${detail ? ' — ' + detail : ''}`);
  if (!ok) fails++;
}

// ── 1. register vs snapshot (wave-4 four-way pattern) ──
const w6 = pace.wavePlan.find(w => w.wave === 6);
check('wavePlan wave-6 present', !!w6, w6 ? w6.topic : 'missing');
const ids = w6.register.map(r => r.noteId);
check('register 12 notes', ids.length === 12, `count ${ids.length}`);
check('register unique IDs', new Set(ids).size === 12);
check('register chars total 34316', w6.register.reduce((a, r) => a + r.bodyChars, 0) === 34316, `sum ${w6.register.reduce((a, r) => a + r.bodyChars, 0)}`);
check('register spec points 20 (multiplicity)', w6.register.reduce((a, r) => a + r.specPointCodes.length, 0) === 20, `sum ${w6.register.reduce((a, r) => a + r.specPointCodes.length, 0)}`);

// zero overlap with waves 1-5
const prior = new Set();
for (const w of ['wave1', 'wave2', 'wave3', 'wave4', 'wave5']) {
  const dir = `/home/z/my-project/download/${w}`;
  for (const f of fs.readdirSync(dir).filter(f => f.startsWith('timing-receipt-'))) {
    prior.add(JSON.parse(fs.readFileSync(`${dir}/${f}`, 'utf8')).noteId);
  }
}
check('zero overlap with waves 1-5 receipts', ids.every(id => !prior.has(id)), `prior pool ${prior.size}`);

// register vs snapshot rows (7 pin fields + codes)
for (const r of w6.register) {
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

// parity proof vs wave-5 of-record texts (the pack chain: wave-4 proven at wave-5 open,
// wave-5 proven here — 4 probes against wave-5 layers)
const w5ids = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave5/wave5-register.json', 'utf8')).register.map(r => r.noteId);
const w5layer0 = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave5/guided-lesson-${w5ids[0]}.json`, 'utf8'));
const parityProbes = [[w5ids[0], w5layer0.specPoints[0].code]];
// add three more probes from distinct wave-5 layers
for (const nid of w5ids.slice(1)) {
  const L = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave5/guided-lesson-${nid}.json`, 'utf8'));
  parityProbes.push([nid, L.specPoints[0].code]);
  if (parityProbes.length >= 4) break;
}
let parityOk = 0;
for (const [nid, codeFull] of parityProbes) {
  const layer = JSON.parse(fs.readFileSync(`/home/z/my-project/download/wave5/guided-lesson-${nid}.json`, 'utf8'));
  const sp = layer.specPoints.find(s => s.code === codeFull);
  const packText = byCode[codeFull.replace(/^4CH1-/, '')] && byCode[codeFull.replace(/^4CH1-/, '')].official_wording;
  const match = sp && packText && sp.text === packText;
  if (match) parityOk++;
  else console.log(`  parity detail ${codeFull}: layer=${JSON.stringify(sp && sp.text).slice(0, 80)} pack=${JSON.stringify(packText).slice(0, 80)}`);
}
check('pack parity vs wave-5 of-record texts (4 probes)', parityOk === parityProbes.length, `${parityOk}/${parityProbes.length} exact`);

// resolve wave-6 codes
const w6codes = [...new Set(w6.register.flatMap(r => r.specPointCodes))].sort();
const texts = {};
let missing = [];
for (const cFull of w6codes) {
  const c = cFull.replace(/^4CH1-/, '');
  const p = byCode[c];
  if (p && p.official_wording) texts[cFull] = p.official_wording; else missing.push(cFull);
}
check('all wave-6 codes resolved from pack', missing.length === 0, missing.length ? 'missing ' + missing.join(',') : w6codes.length + ' codes');
// Documented normalisation (wave-4 treatment, wave-5 map extended): multi-bullet statements
// flattened to semicolon clauses, wording verbatim. Bullet fragments extracted from the
// source note bodies of record (the wave-6 bodies carry the bullet lists verbatim).
const BULLETS = {
  // 2.15: identical fragment to the wave-5 of-record flattening (parity chain held)
  '2.15': 'water; dilute hydrochloric or sulfuric acid',
  // 2.20: the four terms enumerated by the note body's own spec-point bullet list (verbatim)
  '2.20': 'oxidation; reduction; redox; oxidising agent',
  // 2.34: the six solubility rules enumerated by the note body's own spec-point bullet list (verbatim)
  '2.34': 'common sodium, potassium and ammonium compounds are soluble; all nitrates are soluble; common chlorides are soluble, except those of silver and lead(II); common sulfates are soluble, except for those of barium, calcium and lead(II); common carbonates are insoluble, except for those of sodium, potassium and ammonium; common hydroxides are insoluble except for those of sodium, potassium and calcium (calcium hydroxide is slightly soluble)',
};
let bulletsApplied = [];
for (const [code, frag] of Object.entries(BULLETS)) {
  const k = '4CH1-' + code;
  if (texts[k] && texts[k].endsWith(':')) { texts[k] = texts[k] + ' ' + frag; bulletsApplied.push(code); }
}
check('bullet flattening applied exactly where wording ends with colon', bulletsApplied.length === 3, bulletsApplied.join(','));
console.log('--- wave-6 spec texts ---');
for (const c of w6codes) console.log(`  ${c}: ${JSON.stringify(texts[c])}`);

// ── 3. bodies end to end ──
fs.mkdirSync(`${OUT}/bodies`, { recursive: true });
let totalChars = 0;
for (const r of w6.register) {
  const row = snap.notes.find(n => n.noteId === r.noteId);
  fs.writeFileSync(`${OUT}/bodies/${r.noteId}.md`, row.body);
  totalChars += row.body.length;
  const headings = (row.body.match(/^#{1,6} .*$/gm) || []).map(h => h.replace(/^#+\s*/, ''));
  console.log(`BODY ${r.noteId} "${row.title}" ${row.body.length}ch | headings: ${headings.join(' | ')}`);
}
check('bodies extracted chars == 34316', totalChars === 34316, `sum ${totalChars}`);

// snapshot pin
const pin = crypto.createHash('sha256').update(fs.readFileSync(SNAP)).digest('hex');
check('snapshot pin MATCH', pin === 'e23e2ab79df6b0e957bf12933779e4701b37c88736d87c20b19bac130553487d');

// persist the prepared register of record
fs.writeFileSync(`${OUT}/wave6-register.json`, JSON.stringify({
  format: 'wave6-register/0.1', at: new Date().toISOString(), ignitionTrace: 'operator-continue-web-e79a3bd8',
  topic: w6.topic, register: w6.register, specTexts: texts, snapshotPin: pin,
}, null, 1));
console.log(fails ? `\n${fails} FAILURES` : '\nALL PREP CHECKS PASS');
process.exit(fails ? 1 : 0);
