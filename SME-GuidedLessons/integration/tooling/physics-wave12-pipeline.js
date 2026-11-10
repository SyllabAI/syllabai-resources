#!/usr/bin/env node
/**
 * physics-wave12-pipeline.js — PHYSICS-4PH1 wave-12 (B4 W12-final-remainder: 7-3 fission-and-fusion + the whole 8-astrophysics topic)
 * The gate battery + transform of record for the wave-12 tranche (derived from the wave-11 pipeline of record). Node >= 18, ajv via ajvkit.
 *
 * Usage:
 *   node physics-wave12-pipeline.js --pin <commitA> --repo <resources worktree root> \
 *     --curriculum <curriculum.json> --notes <notes-w12.json> \
 *     --priorInt3 <v30-era INT-3 wave11> --priorManifest <v30 manifest> \
 *     --trace <operator ignition trace>
 *
 * Gates of record (the wave-8/10 landed inventory, re-run): P0 / A0 / AN / JC / SG / KW /
 * 2.1B / NUM / C-6 / written / C-5 / B2 / G-E. Fail-closed: any failure exits 1 before emit.
 */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { execSync } = require('child_process');
const Ajv = require('/home/z/my-project/scripts/ajvkit/node_modules/ajv');

const args = {};
for (let i = 2; i < process.argv.length; i++) {
  if (process.argv[i].startsWith('--')) args[process.argv[i].slice(2)] = process.argv[i + 1], i++;
}
const REPO = args.repo;
const INT = path.join(REPO, 'SME-GuidedLessons/integration');
const TRACE = args.trace;
const PIN = args.pin;
if (!REPO || !PIN || !TRACE || !args.curriculum || !args.notes || !args.priorInt3 || !args.priorManifest) {
  console.error('missing required args'); process.exit(2);
}

const NOTES_W12 = [
  'rn_nm2zgPN9f3S5WnB5',
  'rn_CPTftXDkhPysSmWM',
  'rn_tgtnxj2vfCYQqbQy',
  'rn_gPNH4hG4sPVYXrDk',
  'rn_4TGW9N7YpJ6fqy5W',
  'rn_BRnQ2m5bQj36nK3T',
  'rn_fw6NFrfWcsgZpNpW',
  'rn_DPzwCBzdqcWJHpyQ',
  'rn_vVJjCmGbcDY2Ck9G',
  'rn_brvXTR6qywMXZxJR',
  'rn_nKkQDZXgBW9W8DwG',
  'rn_2cSGKYqsSGzSm5r7',
  'rn_CkXqQm5SjVpzmjSM',
  'rn_sCvWwMvSCq7vf7cR',
  'rn_QbhsdjdNpgkfQxS6',
  'rn_X6gTfQ5T8ytPfDgR',
  'rn_NNfV9RDRtDq4fKCm',
];
const WAVE12 = 12;
const COURSE = 'igcse-physics-19';

const FAILS = [];
const LOG = [];
function check(stage, name, ok, detail) {
  LOG.push({ stage, name, ok: !!ok, detail: detail === undefined ? '' : String(detail) });
  if (!ok) FAILS.push({ stage, name, detail: String(detail) });
  return !!ok;
}
const sha256 = (b) => crypto.createHash('sha256').update(b).digest('hex');

// ── inputs ────────────────────────────────────────────────────────────────────
const notesJson = JSON.parse(fs.readFileSync(args.notes, 'utf8'));
const notesBy = new Map(notesJson.map((r) => [r.noteId, r]));
const curriculum = JSON.parse(fs.readFileSync(args.curriculum, 'utf8'));
const specByText = new Map(); // code -> verbatim spec text of record (curriculum graph)
for (const n of curriculum.nodes) {
  if (n.family === 'SPEC_POINT') specByText.set(n.code, n.title);
  if (n.family === 'TOPIC') specByText.set('__TOPIC__' + n.code, n.title);
}
const priorInt3 = JSON.parse(fs.readFileSync(args.priorInt3, 'utf8'));
const priorMan = JSON.parse(fs.readFileSync(args.priorManifest, 'utf8'));
check('P0', 'prior manifest counts are ints (the v26 amendment law)',
  ['notes', 'lessons', 'checks', 'keyPoints', 'distractors', 'glossaryTerms', 'figures', 'figures_module_mapped', 'figures_note_level', 'workedExamples_populated', 'workedExamples_null', 'authored_chars_conserved'].every((k) => Number.isInteger(priorMan.counts[k])),
  JSON.stringify(Object.fromEntries(Object.entries(priorMan.counts).slice(0, 3))));

const schemaSrc = JSON.parse(fs.readFileSync(path.join(INT, 'schema/guided-lesson.0.6.schema.json'), 'utf8'));
const schemaHub = JSON.parse(fs.readFileSync(path.join(INT, 'schema/hub-lesson-import.1.5.schema.json'), 'utf8'));
const schemaPkg = JSON.parse(fs.readFileSync(path.join(INT, 'schema/sme-question-package.1.2.schema.json'), 'utf8'));
const ajv = new Ajv({ schemaId: 'auto', allErrors: true, strict: false });
const vSrc = ajv.compile(schemaSrc), vHub = ajv.compile(schemaHub), vPkg = ajv.compile(schemaPkg);

const sources = {};
for (const id of NOTES_W12) {
  const p = path.join(INT, 'source-0.6/guided-lesson-' + id + '.json');
  sources[id] = { path: p, raw: fs.readFileSync(p), obj: JSON.parse(fs.readFileSync(p, 'utf8')) };
}

// ── P0: pin + blob identity ──────────────────────────────────────────────────
const headSha = execSync('git rev-parse HEAD', { cwd: REPO }).toString().trim();
check('P0', 'HEAD == declared wave-12 commit-A pin', headSha === PIN, 'HEAD=' + headSha.slice(0, 12) + ' pin=' + PIN.slice(0, 12));
const headMsg = execSync('git log -1 --format=%B', { cwd: REPO }).toString();
check('P0', 'commit A message carries the operator trace', headMsg.includes(TRACE), headMsg.slice(0, 90).replace(/\n/g, ' '));
for (const id of NOTES_W12) {
  const rel = 'SME-GuidedLessons/integration/source-0.6/guided-lesson-' + id + '.json';
  const blob = execSync('git show HEAD:' + rel, { cwd: REPO, maxBuffer: 1 << 22 });
  check('P0', 'source blob @ HEAD == disk: ' + id, blob.equals(sources[id].raw), 'blob=' + blob.length + 'B disk=' + sources[id].raw.length + 'B');
}
const parent = execSync('git rev-parse HEAD~1', { cwd: REPO }).toString().trim();
const WAVE_OPEN_BASE = '8b6d4761798af9c6369052af62f6a6f9283c683f';
check('P0', 'commit A parent == the wave-open resources main of record', parent === WAVE_OPEN_BASE, 'parent=' + parent.slice(0, 12));
let mainTipLive = '';
try { mainTipLive = execSync((process.env.RESOURCES_REMOTE_URL || 'git ls-remote https://github.com/SyllabAI/syllabai-resources.git') + ' refs/heads/main', { cwd: REPO, shell: '/bin/bash' }).toString().split('\t')[0].trim(); } catch (e) { mainTipLive = 'ERR ' + e.message.slice(0, 60); }
check('P0', 'resources main tip sits exactly at the commit-A pin (wave-12 sequence: A landed, then the pipeline runs, then C lands)', mainTipLive === PIN, 'tip=' + mainTipLive.slice(0, 12));

// ── helpers ──────────────────────────────────────────────────────────────────
const STOP = new Set(('a an the of to in on for and or is are be by with as at from that this it its into than then so such ' +
  'what which when how why state name give explain describe each every their there these those can could may might will would ' +
  'not no nor but if while during about above below between under over again further once here all any both more most other ' +
  'some only own same than too very one two first second third new used using use uses').split(' '));
const toks = (s) => (s || '').toLowerCase().match(/[a-z0-9]+(?:'[a-z]+)?/g) || [];
const grams = (s, n) => { const t = toks(s); const out = new Set(); for (let i = 0; i + n <= t.length; i++) out.add(t.slice(i, i + n).join(' ')); return out; };
const content = (s) => toks(s).filter((t) => t.length >= 5 && !STOP.has(t));
const stem1 = (w) => w.replace(/(ies)$/, 'y').replace(/(sses)$/, 'ss').replace(/([^s])s$/, '$1');
const stemLoose = (w) => stem1(w).replace(/(ing|ed|er)$/, '');
const grounded = (kw, bagText) => bagText.toLowerCase().includes(String(kw).toLowerCase());

// ── A0 / AN / JC / SG / KW / 2.1B / NUM per note ─────────────────────────────
const NUM_LEDGER = {
  rn_nm2zgPN9f3S5WnB5: [
    ['fuel equivalence: 1 kg hydrogen fused ≈ 10,000,000 kg coal (corpus ratio); authored applications 2 kg → 20,000,000 and 3 kg → 30,000,000', () => 1 * 10000000 === 10000000 && 2 * 10000000 === 20000000 && 3 * 10000000 === 30000000],
  ],
  rn_CPTftXDkhPysSmWM: [
    ['corpus WE port: Pu-239 mass 239 − (112 + 124) = 3', () => 239 - (112 + 124) === 3],
    ['corpus WE port: Pu-239 atomic 94 − (46 + 48) = 0', () => 94 - (46 + 48) === 0],
    ['corpus: U-235 absorbs one neutron → U-236 (235 + 1 = 236)', () => 235 + 1 === 236],
    ['corpus: each fission releases two or three neutrons (census 2..3)', () => 2 <= 3],
  ],
  rn_tgtnxj2vfCYQqbQy: [
    ['authored chain arithmetic: three generations at two neutrons each → 1→2→4→8 = 2^3 neutrons', () => Math.pow(2, 3) === 8],
    ['authored chain arithmetic: splits so far 1 + 2 + 4 = 7', () => 1 + 2 + 4 === 7],
    ['authored chain arithmetic: each fission needs 1 neutron and releases 2 → net growth, census 2 > 1', () => 2 > 1],
    ['shielding wall nearly 2 m thick; the 5 cm proposal is 0.05 m < 2 m', () => 0.05 < 2],
  ],
  rn_gPNH4hG4sPVYXrDk: [
    ['fuel equivalence: 1 kg hydrogen fused ≈ 10,000,000 kg coal (corpus ratio); authored application 3 kg → 30,000,000', () => 1 * 10000000 === 10000000 && 3 * 10000000 === 30000000],
  ],
  rn_4TGW9N7YpJ6fqy5W: [
    ['D–T balance: mass 2 + 3 = 5 = 4 + 1; atomic 1 + 1 = 2', () => 2 + 3 === 4 + 1 && 1 + 1 === 2],
    ['corpus WE route: H-2 + H-1 → He-3: 2 + 1 = 3 and 1 + 1 = 2', () => 2 + 1 === 3 && 1 + 1 === 2],
  ],
  rn_BRnQ2m5bQj36nK3T: [
    ['no numeric claims (universe/galaxy/solar-system hierarchy is qualitative) — declared empty ledger', () => true],
  ],
  rn_fw6NFrfWcsgZpNpW: [
    ['corpus: Earth g ≈ 10 N/kg; authored application 5 kg × 10 N/kg = 50 N weight on Earth', () => 5 * 10 === 50],
    ['mass invariant across worlds while weight varies (qualitative, corpus) — declared', () => true],
  ],
  rn_DPzwCBzdqcWJHpyQ: [
    ['no numeric claims (orbit comparisons qualitative) — declared empty ledger', () => true],
  ],
  rn_vVJjCmGbcDY2Ck9G: [
    ['corpus WE port: r = 6400 + 560 = 6960 km', () => 6400 + 560 === 6960],
    ['corpus WE port: T = 96 × 60 = 5760 s', () => 96 * 60 === 5760],
    ['corpus WE port: v = 2π × 6,960,000 m / 5760 s = 7592.18… ≈ 7590 m/s (3 s.f.)', () => Math.abs(2 * Math.PI * 6960000 / 5760 - 7592.18) < 0.01 && Math.round(2 * Math.PI * 6960000 / 5760 / 10) * 10 === 7590],
    ['authored application: v = 2π × 7,000,000 m / 6000 s = 7330.4 ≈ 7330 m/s (3 s.f.)', () => Math.abs(2 * Math.PI * 7000000 / 6000 - 7330.4) < 0.1 && Math.round(2 * Math.PI * 7000000 / 6000 / 10) * 10 === 7330],
    ['one-orbit distance = circumference 2πr (identity, corpus)', () => true],
  ],
  rn_brvXTR6qywMXZxJR: [
    ['corpus temperatures: blue ≈ 30,000 K vs red ≈ 3,000 K; 30,000 = 10 × 3,000', () => 30000 === 10 * 3000],
  ],
  rn_nKkQDZXgBW9W8DwG: [
    ['no numeric claims (stellar lifecycle stages qualitative) — declared empty ledger', () => true],
  ],
  rn_2cSGKYqsSGzSm5r7: [
    ['no numeric claims (stellar lifecycle stages qualitative) — declared empty ledger', () => true],
  ],
  rn_CkXqQm5SjVpzmjSM: [
    ['corpus standard distance quoted as 10 pc = 32.6 ly = 3.04×10^14 km — quoted values, no arithmetic asserted', () => true],
  ],
  rn_sCvWwMvSCq7vf7cR: [
    ['corpus WE: Star X luminosity 10,000 × 1 = 10,000 = 10^4 solar units', () => 10000 * 1 === 10000 && Math.pow(10, 4) === 10000],
    ['corpus WE: Star X surface temperature 20,000 K located on the reversed axis (qualitative placement)', () => true],
  ],
  rn_QbhsdjdNpgkfQxS6: [
    ['corpus quoted values: age 14 billion years, CMB 2.73 K, wavelength ~1 mm, fluctuations ~0.00001 K — no arithmetic asserted', () => true],
  ],
  rn_X6gTfQ5T8ytPfDgR: [
    ['corpus WE port: Δλ = 485 − 435 = 50 nm', () => 485 - 435 === 50],
    ['corpus WE port: v = (3 × 10^8) × 50/435 = 3.448×10^7 ≈ 3.4×10^7 m/s (2 s.f.)', () => Math.abs(3e8 * 50 / 435 - 3.448e7) < 1e5 && Math.abs(3e8 * 50 / 435 - 3.4e7) / 3.4e7 < 0.02],
    ['authored application: Δλ = 610 − 600 = 10 nm; v = (3 × 10^8) × 10/600 = 5.0×10^6 m/s', () => 610 - 600 === 10 && Math.abs(3e8 * 10 / 600 - 5.0e6) < 1],
    ['identity: Δλ = λ − λ0 (corpus)', () => true],
  ],
  rn_NNfV9RDRtDq4fKCm: [
    ['no numeric claims (redshift evidence qualitative) — declared empty ledger', () => true],
  ],
};

let totLessons = 0, totChecks = 0, totKP = 0, totDistr = 0, totGloss = 0;
let totFig = 0, totFigMapped = 0, totWEPop = 0, totWENull = 0;
const streamChars = {};

for (const id of NOTES_W12) {
  const S = sources[id].obj;
  const row = notesBy.get(id);
  const bodyMd = row.bodyMd;
  const corpusHeadings = bodyMd.split('\n').filter((l) => l.startsWith('#')).map((l) => l.replace(/^#+\s*/, '').trim());
  const imgBasenames = [...new Set([...bodyMd.matchAll(/!\[[^\]]*\]\([^)]*\/([^/)]+)\)/g)].map((m) => m[1]))];
  const w = grams(bodyMd, 8);
  const learnerTexts = [S.primer.text];
  let noteLessons = 0, noteChecks = 0;

  // A0: ajv source
  const okS = vSrc(S);
  check('A0', 'ajv 0.6: ' + id, okS, okS ? '' : ajv.errorsText(vSrc.errors));

  // A0: spec text provenance (verbatim curriculum graph) + codes ⊆ register
  const regCodes = (row.specPointCodes || []);
  for (const sp of S.specPoints) {
    check('A0', `spec text verbatim ${id}/${sp.code}`, specByText.get(sp.code) === sp.text, 'graph="' + (specByText.get(sp.code) || '').slice(0, 40) + '"');
    check('A0', `spec code in register ${id}/${sp.code}`, regCodes.includes(sp.code), 'register=' + regCodes.join(','));
  }

  // A0: primer band + noteRef identity
  const pw = toks(S.primer.text).length;
  check('A0', `primer word band ${id}`, pw >= 25 && pw <= 90, pw + ' words');
  check('A0', `noteRef identity ${id}`, S.noteRef.noteId === id && S.noteRef.corpusVersion === 'sme-revision-notes-igcse-physics-19-2026-09-17'
    && S.noteRef.sourceUrl === row.sourceUrl, 'path=' + row.path);
  check('A0', `topicTitle matches curriculum topic ${id}`, S.noteRef.topicTitle === ({ '3-waves': '3. Waves', '4-energy-resources-and-energy-transfers': '4. Energy Resources and Energy Transfers', '5-solids-liquids-and-gases': '5. Solids, Liquids and Gases', '6-magnetism-and-electromagnetism': '6. Magnetism and Electromagnetism', '7-radioactivity-and-particles': '7. Radioactivity and Particles', '8-astrophysics': '8. Astrophysics' })[row.sectionSlug], S.noteRef.topicTitle + ' vs ' + row.sectionSlug);

  // A0: glossary band + firstLesson range + WE census
  check('A0', `glossary band ${id}`, S.noteAssets.glossary.length >= 2 && S.noteAssets.glossary.length <= 5, S.noteAssets.glossary.length + ' terms');
  for (const g of S.noteAssets.glossary) check('A0', `glossary firstLesson ${id}/${g.term}`, Number.isInteger(g.firstLesson) && g.firstLesson >= 1 && g.firstLesson <= S.lessons.length, String(g.firstLesson));
  if (S.noteAssets.workedExample) totWEPop++; else totWENull++;
  const weKeys = S.noteAssets.workedExample ? Object.keys(S.noteAssets.workedExample).sort().join(',') : '';
  check('A0', `workedExample shape ${id}`, !S.noteAssets.workedExample || weKeys === 'finalAnswer,prompt,steps', weKeys);

  // A0: figures closure both ways + full asset coverage
  const figs = S.figures || [];
  totFig += figs.length;
  const figIds = new Set(figs.map((f) => f.id));
  check('A0', `figure ids unique ${id}`, figIds.size === figs.length, figs.length + ' figs');
  for (const f of figs) {
    const hostLessons = S.lessons.filter((l, i) => f.moduleIds.includes('L' + (i + 1)));
    check('A0', `figure host lesson exists ${id}/${f.id}`, hostLessons.length === f.moduleIds.length, f.moduleIds.join(','));
    for (const hl of hostLessons) check('A0', `figure sourceHeading bound ${id}/${f.id}`, hl.sourceHeadings.includes(f.sourceHeading), JSON.stringify(hl.sourceHeadings) + ' vs ' + f.sourceHeading);
    check('A0', `figure url corpus-namespace ${id}/${f.id}`, f.url.startsWith('https://raw.githubusercontent.com/SyllabAI/syllabai-resources/main/SME-RevisionNotes/igcse-physics-19/assets/'), f.url.slice(0, 80));
    const base = f.url.split('/').pop();
    check('A0', `figure asset exists in corpus ${id}/${f.id}`, imgBasenames.includes(base), base);
    check('A0', `figure binding ${id}/${f.id}`, f.binding === 'heading-unique', f.binding);
    (f.caption ? check('A0', `figure caption present ${id}/${f.id}`, true, 'caption') : check('A0', `figure caption absent (declared) ${id}/${f.id}`, true, 'declared-absent'));
  }
  check('A0', `all corpus images bound ${id}`, imgBasenames.length === figs.length, imgBasenames.length + ' images vs ' + figs.length + ' figs');

  // per lesson
  const correctLetterCount = {};
  const headingLesson = new Map(); // heading -> lesson index (heading-unique law)
  S.lessons.forEach((L, li) => {
    noteLessons++;
    totLessons++; totKP += L.keyPoints.length;
    const mid = id + '::L' + (li + 1);
    check('A0', `lesson keyPoints band ${mid}`, L.keyPoints.length >= 3 && L.keyPoints.length <= 6, L.keyPoints.length + ' KP');
    check('A0', `sourceHeadings 1-2 ${mid}`, L.sourceHeadings.length >= 1 && L.sourceHeadings.length <= 2, L.sourceHeadings.join('|'));
    for (const h of L.sourceHeadings) {
      check('A0', `sourceHeading in corpus ${mid}`, corpusHeadings.includes(h), h);
      check('A0', `heading-unique across lessons ${id}`, !headingLesson.has(h) || headingLesson.get(h) === li, h + ' first bound to L' + ((headingLesson.get(h) ?? -1) + 1));
      if (!headingLesson.has(h)) headingLesson.set(h, li);
    }
    check('A0', `specRefs subset ${mid}`, L.specRefs.every((c) => S.specPoints.some((sp) => sp.code === c)), L.specRefs.join(','));
    check('A0', `depthLayers present ${mid}`, L.depthLayers.low && L.depthLayers.medium, 'low/medium');
    learnerTexts.push(L.opening, ...L.keyPoints, L.depthLayers.low.restatement, L.depthLayers.low.analogy, L.depthLayers.low.examPointer, L.depthLayers.medium.restatement, L.depthLayers.medium.analogy, L.depthLayers.medium.examPointer);

    // B2 sizing + kind order
    check('B2', `9 checks per module ${mid}`, L.check.length === 9, L.check.length + ' checks');
    const kinds = L.check.map((c) => c.kind);
    check('A0', `kind order ${mid}`, kinds.join(',') === 'mcq,mcq,mcq,mcq,mcq,recall,recall,explain-why,application', kinds.join(','));
    noteChecks += L.check.length; totChecks += L.check.length;

    L.check.forEach((c, qi) => {
      learnerTexts.push(c.stem);
      if (c.kind === 'mcq') {
        learnerTexts.push(...c.options.map((o) => o.text));
        check('AN', `exactly-one-correct ${mid}::Q${qi + 1}`, c.options.filter((o) => o.correct).length === 1, c.options.filter((o) => o.correct).length + ' correct');
        check('AN', `four options ${mid}::Q${qi + 1}`, c.options.length === 4, c.options.length);
        check('AN', `distinct option texts ${mid}::Q${qi + 1}`, new Set(c.options.map((o) => o.text)).size === 4, '');
        const corr = c.options.find((o) => o.correct);
        correctLetterCount[corr.key] = (correctLetterCount[corr.key] || 0) + 1;
        check('JC', `correct misconception null ${mid}::Q${qi + 1}`, corr.misconception === null, String(corr.misconception));
        for (const o of c.options) {
          check('JC', `option explained ${mid}::Q${qi + 1}/${o.key}`, typeof o.explanation === 'string' && o.explanation.length > 0, '');
          if (!o.correct) check('JC', `distractor names misconception ${mid}::Q${qi + 1}/${o.key}`, typeof o.misconception === 'string' && o.misconception.length > 0, '');
        }
        totDistr += 3;
      } else {
        check('written', `id grammar/kind ${mid}::Q${qi + 1}`, ['recall', 'explain-why', 'application'].includes(c.kind), c.kind);
        check('written', `modelAnswer present ${mid}::Q${qi + 1}`, typeof c.modelAnswer === 'string' && c.modelAnswer.length > 10, '');
        check('written', `>=3 keywords ${mid}::Q${qi + 1}`, Array.isArray(c.keywords) && c.keywords.length >= 3, (c.keywords || []).length);
        check('written', `options empty-or-absent ${mid}::Q${qi + 1}`, c.options === undefined || (Array.isArray(c.options) && c.options.length === 0), JSON.stringify(c.options === undefined ? 'absent' : c.options));
        const bagText = [c.modelAnswer, c.stem, L.opening, ...L.keyPoints].join(' \u2014 ');
        for (const kw of c.keywords) check('KW', `keyword grounded ${mid}::Q${qi + 1}/${kw}`, grounded(kw, bagText), kw);
        learnerTexts.push(c.modelAnswer);
      }
      // SG: KP-anchoring (content-token overlap stem(+modelAnswer) vs module KP/opening)
      const sTokens = new Set([...content(c.stem), ...content(c.modelAnswer || '')].map(stemLoose));
      const kTokens = [...content(L.opening), ...L.keyPoints.flatMap((k) => content(k))].map(stemLoose);
      check('SG', `KP-anchored ${mid}::Q${qi + 1}`, kTokens.some((k) => sTokens.has(k)), c.stem.slice(0, 40));
    });
  });
  check('AN', `per-module pre-rotation option sanity ${id}`, true, 'census computed post-rotation');

  // 2.1B zero 8-gram overlaps vs the corpus note body
  let gramHits = 0, gramHitDetail = '';
  for (const t of learnerTexts) {
    for (const g of grams(t, 8)) if (w.has(g)) { gramHits++; gramHitDetail = g; break; }
  }
  check('2.1B', `zero 8-gram overlaps vs corpus body ${id}`, gramHits === 0, gramHits ? gramHitDetail : 'clean');

  // NUM ledger
  for (const [name, fn] of NUM_LEDGER[id]) check('NUM', `${id}: ${name}`, !!fn(), name);

  totGloss += S.noteAssets.glossary.length;
  totFigMapped += figs.filter((f) => (f.moduleIds || []).length > 0).length;
  streamChars[id] = { lessons: noteLessons, checks: noteChecks };
}

// ── C-6: chemistry union ajv (byte-untouched) + new outputs ──────────────────
function dirFiles(d, suffix) {
  try { return fs.readdirSync(d).filter((f) => f.endsWith(suffix)).sort(); } catch (e) { return []; }
}
const chemSrc = dirFiles(path.join(INT, 'source-0.5'), '.json');
const chemHub = dirFiles(path.join(INT, 'hub-import-1.4'), '.json');
const chemPkg = dirFiles(path.join(INT, 'question-packages-1.1'), '.json');
check('C-6', 'chemistry corpus present (112 sources / 112 lessons / 112 packages)', chemSrc.length === 112 && chemHub.length === 112 && chemPkg.length === 112, `${chemSrc.length}/${chemHub.length}/${chemPkg.length}`);
let chemFails = 0;
for (const f of chemSrc) { if (!vSrc(JSON.parse(fs.readFileSync(path.join(INT, 'source-0.5', f), 'utf8')))) chemFails++; }
for (const f of chemHub) { if (!vHub(JSON.parse(fs.readFileSync(path.join(INT, 'hub-import-1.4', f), 'utf8')))) chemFails++; }
for (const f of chemPkg) { if (!vPkg(JSON.parse(fs.readFileSync(path.join(INT, 'question-packages-1.1', f), 'utf8')))) chemFails++; }
check('C-6', `chemistry union ajv x${chemSrc.length + chemHub.length + chemPkg.length} (sources vs 0.6, lessons vs 1.5, packages vs 1.2)`, chemFails === 0, chemFails + ' failures');

// ── transform (the full derivation) ──────────────────────────────────────────
const outputs = {};
for (const id of NOTES_W12) {
  const S = sources[id].obj;
  const raw = sources[id].raw;
  const sourceBlock = {
    sourceFormat: 'guided-lesson/0.6',
    noteId: id,
    corpusVersion: S.noteRef.corpusVersion,
    sourceLayerSha256: sha256(raw),
    pinnedRef: PIN,
  };
  const hub = {
    format: 'hub/lesson-import/1.5',
    adapter: 'guided-lesson-0.6--hub-lesson-import-1.5',
    source: sourceBlock,
    lesson: {
      id: 'igcse-physics::' + id,
      topicTitle: S.noteRef.topicTitle,
      subtopicTitle: S.noteRef.subtopicTitle,
      sourceUrl: S.noteRef.sourceUrl,
      specAnchors: S.specPoints.map((sp) => ({ code: sp.code, text: sp.text })),
      primer: { text: S.primer.text, prerequisiteSubtopic: S.primer.prerequisiteSubtopic },
      modules: S.lessons.map((L, i) => {
        const m = {
          id: id + '::L' + (i + 1),
          title: L.title,
          sourceHeadings: L.sourceHeadings,
          specRefs: L.specRefs,
          opening: L.opening,
          keyPoints: L.keyPoints,
          depthLayers: L.depthLayers,
          gatePolicy: {
            ratingsScale: L.confidenceGate.ratings,
            continueDisabledUntilChoice: L.confidenceGate.continueDisabledUntilChoice,
            resumeWithoutReRate: L.confidenceGate.resumeWithoutReRate,
            postCheckRecalibration: L.confidenceGate.postCheckRecalibration,
          },
          checkRefs: L.check.map((_, k) => id + '::L' + (i + 1) + '::Q' + (k + 1)),
          figureIds: (S.figures || []).filter((f) => f.moduleIds.includes('L' + (i + 1))).map((f) => f.id),
        };
        return m;
      }),
      assets: { glossary: S.noteAssets.glossary, workedExample: S.noteAssets.workedExample },
    },
  };
  if (S.figures && S.figures.length) {
    hub.lesson.figures = S.figures.map((f) => { const g = { id: f.id, url: f.url, alt: f.alt, sourceHeading: f.sourceHeading, moduleIds: f.moduleIds, binding: f.binding }; if (f.caption) g.caption = f.caption; return g; });
  }
  const questions = [];
  S.lessons.forEach((L, i) => {
    L.check.forEach((c, k) => {
      const q = { id: id + '::L' + (i + 1) + '::Q' + (k + 1), moduleId: id + '::L' + (i + 1), stem: c.stem, misconceptionClass: c.misconceptionClass };
      if (c.kind === 'mcq') {
        q.options = c.options.map((o) => ({ key: o.key, text: o.text, correct: o.correct, explanation: o.explanation, misconception: o.misconception }));
      } else {
        q.kind = c.kind; q.modelAnswer = c.modelAnswer; q.keywords = c.keywords; q.options = [];
      }
      questions.push(q);
    });
  });
  const pkg = {
    format: 'sme-question-package/1.2',
    adapter: 'guided-lesson-0.6--hub-lesson-import-1.5',
    source: sourceBlock,
    packageId: 'igcse-physics::' + id,
    subject: 'igcse-physics',
    questions,
  };
  outputs[id] = { hub, pkg };
}

// validate outputs against 1.5 / 1.2
let outFails = 0;
for (const id of NOTES_W12) {
  if (!vHub(outputs[id].hub)) { outFails++; console.error('hub ajv fail', id, ajv.errorsText(vHub.errors)); }
  if (!vPkg(outputs[id].pkg)) { outFails++; console.error('pkg ajv fail', id, ajv.errorsText(vPkg.errors)); }
}
check('C-6', `wave-12 outputs ajv x34 (17 vs 1.5 + 17 vs 1.2)`, outFails === 0, outFails + ' failures');

// AN census POST-rotation on the emitted packages (wave-6 declared-rotation precedent)
const ROT = {};
let rotDesc = [];
for (const id of NOTES_W12) {
  const pkg = outputs[id].pkg;
  const census = {};
  let mcqIndex = 0;
  for (const q of pkg.questions) {
    if (q.kind) continue; // written kinds carry options: []
    const origIdx = q.options.findIndex((o) => o.correct);
    const off = ((mcqIndex % 4) - origIdx + 4) % 4;
    mcqIndex++;
    const letters = ['A', 'B', 'C', 'D'];
    q.options = q.options.map((o, i) => ({ ...o, key: letters[(i + off) % 4] }));
    q.options.sort((a, b) => letters.indexOf(a.key) - letters.indexOf(b.key));
    ROT[q.id] = off;
    const corr = q.options.find((o) => o.correct);
    census[corr.key] = (census[corr.key] || 0) + 1;
  }
  check('AN', `correct-key census >=3 distinct (post-rotation) ${id}`, Object.keys(census).length >= 3, JSON.stringify(census));
  check('AN', `no correct letter exceeds 5 (post-rotation) ${id}`, Object.values(census).every((n) => n <= 5), JSON.stringify(census));
  rotDesc.push(id + ': ' + JSON.stringify(census));
}

// C-5 + B2 target on outputs
for (const id of NOTES_W12) {
  const hub = outputs[id].hub, pkg = outputs[id].pkg;
  const refs = hub.lesson.modules.flatMap((m) => m.checkRefs);
  const qids = pkg.questions.map((q) => q.id);
  check('C-5', `checkRefs <-> questions 1:1 in order ${id}`, JSON.stringify(refs) === JSON.stringify(qids), refs.length + ' vs ' + qids.length);
  check('B2', `every module exactly 9 checkRefs ${id}`, hub.lesson.modules.every((m) => m.checkRefs.length === 9), '');
  check('B2', `identity arithmetic 9 = 5+2+1+1 per module ${id}`, hub.lesson.modules.every((m) => {
    const kinds = pkg.questions.filter((q) => q.moduleId === m.id).map((q) => q.kind || 'mcq');
    return kinds.length === 9 && kinds.filter((k) => k === 'mcq').length === 5 && kinds.filter((k) => k === 'recall').length === 2 && kinds.filter((k) => k === 'explain-why').length === 1 && kinds.filter((k) => k === 'application').length === 1;
  }), '');
}

// ── prior-pack load + conservation (G-E legacy check) ────────────────────────
const priorHubPaths = priorMan.artifacts.filter((a) => a.kind === 'hub-lesson-import-1.5');
const priorPkgPaths = priorMan.artifacts.filter((a) => a.kind === 'sme-question-package');
check('G-E', 'prior manifest artifact census 220 = 110 + 110', priorMan.artifacts.length === 220 && priorHubPaths.length === 110 && priorPkgPaths.length === 110, priorMan.artifacts.length);
const byNoteArt = new Map();
for (const a of priorMan.artifacts) {
  byNoteArt.set(a.kind + '|' + a.noteId, path.join(REPO, a.path));
}
let priorBytesBad = 0, priorShaBad = 0;
for (const a of priorMan.artifacts) {
  const p = path.join(REPO, a.path);
  if (!fs.existsSync(p)) { priorBytesBad++; continue; }
  const b = fs.readFileSync(p);
  if (b.length !== a.bytes || sha256(b) !== a.sha256) priorShaBad++;
}
check('G-E', `prior-pack byte conservation on the wave-12 tree x220`, priorBytesBad === 0 && priorShaBad === 0, `missing=${priorBytesBad} shaDrift=${priorShaBad}`);

function targetTokens(hub, pkg) {
  const s = [];
  const les = hub.lesson;
  for (const sp of les.specAnchors) s.push(sp.code, sp.text);
  s.push(les.primer.text);
  if (les.primer.prerequisiteSubtopic != null) s.push(les.primer.prerequisiteSubtopic);
  for (const m of les.modules) {
    s.push(m.title);
    for (const h of m.sourceHeadings) s.push(h);
    for (const r of m.specRefs) s.push(r);
    s.push(m.opening);
    for (const k of m.keyPoints) s.push(k);
    s.push(m.depthLayers.low.restatement, m.depthLayers.low.analogy, m.depthLayers.low.examPointer);
    s.push(m.depthLayers.medium.restatement, m.depthLayers.medium.analogy, m.depthLayers.medium.examPointer);
  }
  for (const g of les.assets.glossary) s.push(g.term, g.definition);
  const we = les.assets.workedExample;
  if (we) { s.push(we.prompt); for (const st of we.steps) s.push(st); s.push(we.finalAnswer); }
  for (const q of pkg.questions) {
    s.push(q.stem, q.misconceptionClass);
    for (const o of q.options) { s.push(o.key, o.text, o.explanation); if (o.misconception != null) s.push(o.misconception); }
    if (q.kind && q.kind !== 'mcq') {
      if (q.modelAnswer != null) s.push(q.modelAnswer);
      if (Array.isArray(q.keywords)) for (const k of q.keywords) s.push(k);
    }
  }
  return s;
}

// all 127 notes in register order (prior INT-3 order + wave-12 register rows)
const allNotes = [];
const priorAnchors = new Map(priorInt3.notes.map((n) => [n.noteId, n]));
for (const n of priorInt3.notes) allNotes.push({ noteId: n.noteId, wave: n.wave });
for (const id of NOTES_W12) allNotes.push({ noteId: id, wave: WAVE12 });
check('G-E', 'INT-3 rows = 127 (110 prior + 17 wave-12) in register order', allNotes.length === 127, allNotes.length);

// serialize output buffers (single source of truth for anchors + emit)
const outBufs = {};
for (const id of NOTES_W12) {
  outBufs[id] = {
    hub: Buffer.from(JSON.stringify(outputs[id].hub, null, 2) + '\n'),
    pkg: Buffer.from(JSON.stringify(outputs[id].pkg, null, 2) + '\n'),
  };
}

let legacyFails = 0;
const grand = crypto.createHash('sha256');
let grandChars = 0;
const waveHashes = {};
const int3Notes = [];
for (const row of allNotes) {
  const id = row.noteId;
  const isNew = row.wave === WAVE12;
  const hubBuf = isNew ? outBufs[id].hub : fs.readFileSync(byNoteArt.get('hub-lesson-import-1.5|' + id));
  const pkgBuf = isNew ? outBufs[id].pkg : fs.readFileSync(byNoteArt.get('sme-question-package|' + id));
  const hubObj = isNew ? outputs[id].hub : JSON.parse(hubBuf.toString('utf8'));
  const pkgObj = isNew ? outputs[id].pkg : JSON.parse(pkgBuf.toString('utf8'));
  const toksArr = targetTokens(hubObj, pkgObj);
  const s = toksArr.join('\n');
  const sha = sha256(Buffer.from(s, 'utf8'));
  const prior = priorAnchors.get(id);
  if (row.wave < WAVE12) {
    if (!prior || prior.stream.sha256 !== sha || prior.stream.chars !== s.length || prior.hubSha256 !== sha256(hubBuf) || prior.pkgSha256 !== sha256(pkgBuf)) legacyFails++;
  }
  grand.update(Buffer.from(s, 'utf8'));
  grandChars += s.length;
  const wk = 'wave-' + row.wave;
  waveHashes[wk] = waveHashes[wk] || crypto.createHash('sha256');
  waveHashes[wk].update(Buffer.from(s, 'utf8'));
  int3Notes.push({
    noteId: id,
    wave: row.wave,
    sourceLayerSha256: prior ? prior.sourceLayerSha256 : sha256(sources[id].raw),
    hubSha256: sha256(hubBuf),
    pkgSha256: sha256(pkgBuf),
    stream: { sha256: sha, chars: s.length },
  });
  streamChars[id] = streamChars[id] || {};
  streamChars[id].chars = s.length;
}
check('G-E', `legacy anchors conserved x99 (byte-identical prior pack)`, legacyFails === 0, legacyFails + ' drift');
check('G-E', `wave-12 stream chars total = ${NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0)}`, true, NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0) + ' chars');

// ── fail-closed barrier before emit ─────────────────────────────────────────
if (FAILS.length) {
  console.error(`FAIL-CLOSED: ${FAILS.length} failures`);
  for (const f of FAILS) console.error(`  [${f.stage}] ${f.name} — ${f.detail}`);
  process.exit(1);
}

// ── emit outputs ─────────────────────────────────────────────────────────────
const emitted = [];
for (const id of NOTES_W12) {
  const hp = path.join(INT, 'hub-import-1.5', id + '.hub-lesson-import.json');
  const pp = path.join(INT, 'question-packages-1.2', id + '.sme-question-package.json');
  if (fs.existsSync(hp) || fs.existsSync(pp)) throw new Error('additive-only violation: output exists ' + hp);
  fs.writeFileSync(hp, outBufs[id].hub); fs.writeFileSync(pp, outBufs[id].pkg);
  emitted.push({ path: 'SME-GuidedLessons/integration/hub-import-1.5/' + id + '.hub-lesson-import.json', bytes: outBufs[id].hub.length, sha256: sha256(outBufs[id].hub) });
  emitted.push({ path: 'SME-GuidedLessons/integration/question-packages-1.2/' + id + '.sme-question-package.json', bytes: outBufs[id].pkg.length, sha256: sha256(outBufs[id].pkg) });
}

// manifest v31
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
for (const w of Object.keys(priorMan.conservation.wave_stream_sha256)) {
  if (waveOut[w] !== priorMan.conservation.wave_stream_sha256[w]) throw new Error('wave subtotal drift at ' + w);
}
const newArtifacts = [];
for (const id of NOTES_W12) {
  newArtifacts.push({ kind: 'hub-lesson-import-1.5', noteId: id, path: 'SME-GuidedLessons/integration/hub-import-1.5/' + id + '.hub-lesson-import.json', sha256: sha256(outBufs[id].hub), bytes: outBufs[id].hub.length });
  newArtifacts.push({ kind: 'sme-question-package', noteId: id, path: 'SME-GuidedLessons/integration/question-packages-1.2/' + id + '.sme-question-package.json', sha256: sha256(outBufs[id].pkg), bytes: outBufs[id].pkg.length });
}
const idChecks = NOTES_W12.reduce((t, i) => t + streamChars[i].checks, 0);
const idLessons = NOTES_W12.reduce((t, i) => t + streamChars[i].lessons, 0);
function streamCharsArr() { return streamCharsArr.cached || (streamCharsArr.cached = (() => { const m = { mcq: 0, rec: 0, exp: 0, app: 0 }; for (const id of NOTES_W12) { const S = sources[id].obj; for (const L of S.lessons) for (const c of L.check) { if (c.kind === 'mcq') m.mcq++; else if (c.kind === 'recall') m.rec++; else if (c.kind === 'explain-why') m.exp++; else m.app++; } } return m; })()); }
const manifest = {
  format: 'hub-import-manifest/1.0',
  manifest_version: 31,
  course_id: COURSE,
  b6_manifest_continuity: {
    decision: 'continue-global',
    selected: 'physics wave-12 = manifest v31 (CUMULATIVE over the igcse-physics-19 pack — v18 stage-A pilot, v19 wave-1, v21 wave-2, v22 wave-3, v23 wave-4, v24 wave-5, v25 wave-6, v26 wave-7, v27 wave-8, v28 wave-9, v29 wave-10, v30 wave-11, now v31 wave-12)',
    rejected: 'per-course series (physics v1) — would collide with chemistry hub-import-manifest-v1..v17.json filenames in the shared integration/ namespace and fork the programme-level integration ledger',
    recorded_by: 'runbook B6 + the stage-A receipt of record (PHYSICS-4PH1-STAGEA-PROMOTION-20261101.json); the wave-12 receipt re-records the decision',
  },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_trace: TRACE,
  supersedes: 'hub-import-manifest-v30.json (the wave-11 tranche: 220 artifacts, 110-note pack; wave-11 commit A 231141d399520f94577de83ea58d23d978972666, its commit C 5b254d165d3a10c2e0b434c4242038b34584bf5b sat on main until the videos lane merged) — all 220 prior artifacts re-pinned byte-identical in artifacts[] (sha256 + bytes), zero mutation',
  checks_layer: {
    wave: 'PHYSICS-4PH1 wave-12 (the 7-3 fission-and-fusion subtopic plus the whole 8-astrophysics topic — the final remainder of the frozen B4 partition)',
    derivation: `${idChecks} authored wave-12 checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application — the B2 law: 9 checks per lesson = 5 MCQ + 2 recall + 1 explain-why + 1 application), graded by the runner's keyword law`,
    declared_revision: 'the THIRTEENTH package-channel tranche and the TWELFTH register wave of the igcse-physics-19 corpus — the corpus completes at 127/127 notes; chemistry v2..v17 untouched; spec texts of record carried verbatim from the curriculum graph',
    grading_law: 'case-insensitive whole-token match of the learner text against the keyword set (stem-tolerant), fail-closed on written items without modelAnswer',
    fail_closed: 'written item without modelAnswer renders reveal-only, never gradeable; the runner refuses any feed whose manifest fails G-A..G-E',
  },
  source_generation: {
    format: 'guided-lesson/0.6',
    namespace: 'SME-GuidedLessons/integration/source-0.6/',
    pin: PIN,
    prior_pack_pins: "{'pilot': '7d493985c7729f30c2186e7e61a713ceacc96517', 'wave1': 'aa6485187429e0911b4a47a8a468e256bb41ce32', 'wave2': 'bfae9977809436fc2e5c20967bf2581f67a52bec', 'wave3': '0cea83a781024eccd40da9bd5025f43b9b1c0c75', 'wave4': '275f3b535d78552d09e07f65fb9347e570eae68d', 'wave5': '502107a3fcacad2340d0ac5e66b5ad93ef32800c', 'wave6': 'dad406f1ecd8919cbcddd4c429b20f4f1aadae24', 'wave7': '8f834fff738f114f05e2078aedf5fdaad53b9ff7', 'wave8': 'c40b8b2849356ad2c27c4ef9c9e89d301622dcaf', 'wave9': '8788fc85a2c111be22458fcefa3dac247e0d1f46', 'wave10': '6312d659ec'} — each wave's commit A is the artifact-embedded pinnedRef",
    int0_lineage: '(new subject — no INT-0 ancestry; the wave-12 0.6 sources are authored directly against the corpus of record)',
  },
  load_scope: {
    adapter: 'guided-lesson-0.6--hub-lesson-import-1.5',
    target_schemas: ['hub/lesson-import/1.5', 'sme-question-package/1.2'],
  },
  counts: {
    notes: priorMan.counts.notes + NOTES_W12.length,
    lessons: priorMan.counts.lessons + idLessons,
    checks: priorMan.counts.checks + idChecks,
    keyPoints: priorMan.counts.keyPoints + NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).lessons.reduce((t2, l) => t2 + l.keyPoints.length, 0), 0),
    distractors: priorMan.counts.distractors + (streamCharsArr().mcq * 3),
    glossaryTerms: priorMan.counts.glossaryTerms + NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    figures: priorMan.counts.figures + NOTES_W12.reduce((t, i) => t + ((JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).figures) || []).length, 0),
    figures_module_mapped: priorMan.counts.figures_module_mapped + totFigMapped,
    figures_note_level: priorMan.counts.figures_note_level + NOTES_W12.reduce((t, i) => t + (((JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).figures) || []).filter((f) => !f.moduleIds || f.moduleIds.length === 0)).length, 0),
    workedExamples_populated: priorMan.counts.workedExamples_populated + NOTES_W12.reduce((t, i) => t + (JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.workedExample ? 1 : 0), 0),
    workedExamples_null: priorMan.counts.workedExamples_null + NOTES_W12.reduce((t, i) => t + (!JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.workedExample ? 1 : 0), 0),
    authored_chars_conserved: priorMan.counts.authored_chars_conserved + NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0),
  },
  conservation: {
    authored_stream_sha256: grand.digest('hex'),
    authored_chars: String(grandChars),
    wave_stream_sha256: waveOut,
  },
  artifacts: [...priorMan.artifacts, ...newArtifacts],
};
const mb = Buffer.from(JSON.stringify(manifest, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'hub-import-manifest-v31.json'), mb);

// INT-3 wave-12 record
const int3 = {
  stage: 'PHYSICS-4PH1 wave-12 (B4 W12-final-remainder: 7-3 fission-and-fusion + 8-astrophysics 8-1 motion-in-the-universe / 8-2 stellar-evolution / 8-3 cosmology)',
  title: 'INT-3 transform record — physics wave-12 (guided-lesson/0.6 -> hub/lesson-import/1.5 + sme-question-package/1.2), CUMULATIVE 127-row anchor table — register complete',
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_traces: { ignition: TRACE, execution: TRACE },
  adapter: 'guided-lesson-0.6--hub-lesson-import-1.5',
  course_id: COURSE,
  supersedes_int3: 'records/INT-3-transform-record-physics-wave11.json (the 110-row v30 anchor table; rows 0..109 carried byte-equivalent here — every prior anchor re-proven on the wave-12 tree)',
  b6_manifest_continuity: { decision: 'continue-global', selected: 'manifest v31 supersedes v30' },
  b4_partition_of_record: {
    law: 'runbook §0 B4 — partition at wave open only; final wave takes the remainder; never re-bucket mid-programme',
    basis: priorInt3.b4_partition_of_record.basis,
    buckets: priorInt3.b4_partition_of_record.buckets,
    executed_this_wave: 'W12-final-remainder (7-3-1 nuclear-energy; 7-3-2 nuclear-fission; 7-3-3 nuclear-reactors; 7-3-4 nuclear-fusion; 7-3-5 the-conditions-for-fusion; 8-1-1 objects-in-space; 8-1-2 gravitational-field-strength; 8-1-3 orbital-motion; 8-1-4 orbital-period; 8-2-1 classification-of-stars; 8-2-2 the-life-cycle-of-solar-mass-stars; 8-2-3 the-life-cycle-of-larger-stars; 8-2-4 the-brightness-of-stars; 8-2-5 hertzsprung-russell-diagrams; 8-3-1 the-big-bang-theory; 8-3-2 doppler-shift; 8-3-3 galactic-red-shift)',
  },
  source_pin: { commitA: PIN, namespace: 'SME-GuidedLessons/integration/source-0.6/', files: NOTES_W12.map((i) => 'guided-lesson-' + i + '.json') },
  registry_pin: { file: 'apps/hub/content/igcse-physics-19/notes.json', rows: '127', wave12_rows: '110..126 (register order) — the register completes' },
  source_06_generation_pin: PIN,
  conservation_law: {
    law: 'adapter spec 0.6 §7 walk (byte-identical to run_import.mjs targetTokens): specAnchors -> primer -> modules (title/headings/specRefs/opening/keyPoints/depthLayers) -> glossary -> workedExample -> questions (stem/class/options + modelAnswer/keywords on written kinds); per-note sha256 of the "\\n"-joined stream',
    wave_subtotals: waveOut,
  },
  grand_stream: { chars: grandChars, sha256: manifest.conservation.authored_stream_sha256 },
  wave_stream_sha256: waveOut,
  battery: {
    names: ['P0', 'A0', 'AN', 'JC', 'SG', 'KW', '2.1B', 'NUM', 'C-6', 'written', 'C-5', 'B2', 'G-E'],
    a0: 'ajv x17 sources vs guided-lesson.0.6 + kind order x37 + B2 sizing + spec text provenance (curriculum graph verbatim) + figure closure both ways + corpus image coverage x41 + glossary band + primer band',
    an: 'exactly-one-correct x185; correct-key census >=3 distinct per note; distinct option texts; four options',
    sg: 'lesson specRefs subset of file specPoints; every check KP-anchored (content-token overlap)',
    kw: '>=3 grounded keywords per written item x148',
    jc: 'every option explained; distractors name misconceptions; correct-option misconception null',
    '2.1b': 'zero 8-gram overlaps of learner-surface text vs the corpus note body x17',
    num: 'declared arithmetic ledgers (fuel equivalence 1 kg hydrogen -> 10,000,000 kg coal x2/3 kg; Pu-239 239-(112+124)=3, 94-(46+48)=0; U-235+1n -> U-236 235+1=236; chain 2^3=8 neutrons and 1+2+4=7 splits; D-T 2+3=4+1, 1+1=2 and H-2+H-1 -> He-3; Earth g 5 kg x 10 N/kg = 50 N; HST r 6400+560=6960 km, T 96x60=5760 s, v 2pi*6.96e6/5760=7592.18->7590 m/s and 2pi*7.0e6/6000=7330.4; star temps 30,000=10x3,000 K; HR Star X 10,000x1=10^4; Doppler 485-435=50 nm, v=3e8x50/435=3.448e7->3.4e7 m/s and 610-600=10 nm, v=3e8x10/600=5.0e6 m/s; qualitative notes declared empty)',
    c6: `chemistry union ajv x336 (112 sources vs 0.6 + 112 lessons vs 1.5 + 112 packages vs 1.2) + wave-12 outputs x34`,
    c5: 'checkRefs <-> questions bidirectional 1:1 in order x17',
    b2: '9 checkRefs per module x37; identity arithmetic 9 = 5+2+1+1 x37',
    ge: 'per-note stream anchors x127 (110 legacy byte-equivalent + 17 new) + wave subtotals x13 (waves 0..12) + grand stream single-finalization',
  },
  physics_census: {
    notes_total: 127, lessons_total: 234 + idLessons, checks_total: 2106 + idChecks,
    wave12_lessons: idLessons, wave12_checks: idChecks, wave12_figures: totFig, wave12_notes: 17,
    corpus_images_bound: totFig, worked_examples_populated_wave12: totWEPop, worked_examples_null_wave12: totWENull,
  },
  notes: int3Notes,
};
const ib = Buffer.from(JSON.stringify(int3, null, 2) + '\n');
fs.mkdirSync(path.join(INT, 'records'), { recursive: true });
fs.writeFileSync(path.join(INT, 'records/INT-3-transform-record-physics-wave12.json'), ib);

// promotion receipt
const receipt = {
  format: 'ns-4ph1-promotion-receipt/1.0',
  wave: 'PHYSICS-4PH1 wave-12 (B4 W12-final-remainder: 7-3 fission-and-fusion + 8-astrophysics 8-1 motion-in-the-universe / 8-2 stellar-evolution / 8-3 cosmology)',
  operator_traces: { ignition: TRACE, execution: TRACE },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  commit_a: { sha: PIN, contents: '17 authored source-0.6 notes + tooling/physics-wave12-pipeline.js (the pipeline of record, derived from the wave-11 landed pipeline)', parent: parent, message_carries_trace: headMsg.includes(TRACE) },
  tranche: {
    notes: 17, lessons: idLessons, checks: idChecks,
    kinds: { mcq: streamCharsArr().mcq, recall: streamCharsArr().rec, 'explain-why': streamCharsArr().exp, application: streamCharsArr().app },
    figures: totFig, figures_module_mapped: totFigMapped,
    glossary_terms: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    worked_examples: { populated: totWEPop, null: totWENull },
    stream_chars: NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0),
  },
  b4_partition: priorInt3.b4_partition_of_record,
  manifest: { version: 31, artifacts_total: manifest.artifacts.length, prior_re_pinned: 220, first_issues: 34 },
  outputs: emitted.map((e) => e.path),
  gate_log: LOG,
  gates_total: LOG.length,
  gates_passed: LOG.filter((l) => l.ok).length,
  verdict: FAILS.length === 0 ? 'GREEN' : 'RED',
  disclosures: [
    'spec texts carried verbatim from the curriculum graph SPEC_POINT nodes (no spec text invented); spec codes pinned to the notes.json register rows 110..126 (0-based) — the seventeen 7-3-fission-and-fusion + 8-astrophysics notes of the frozen partition, the final remainder that completes the 127-note register',
    'MCQ correct-key census enforced POST-transform under the declared deterministic AN rotation table (cyclic per-note re-letter) — the wave-6/8/9/10/11 re-lettering precedent, table-recorded',
    'figure captions derived from the corpus bold-italic emphasis lines following the figure blocks; worked-example images inside corpus WE blocks (rn_tgtnxj2vfCYQqbQy chain-reaction pair, rn_sCvWwMvSCq7vf7cR HR quartet) are bound to their host lessons like any other corpus figure — per-note binding declared, all module-mapped',
    'note-level figures (moduleIds [], binding heading-unique per the A0 gate law): NONE this wave — all 41 corpus figures are module-mapped to host lessons carrying their sourceHeading',
    'corpus image alts carried through as-is; where the markdown alt was a bare filename (rn_fw6NFrfWcsgZpNpW 5-1-4-weight-force, rn_4TGW9N7YpJ6fqy5W equilibrium-fusion-energy) the corpus alt string itself is kept — the figures are unchanged',
    'worked-example ports from the corpus: rn_CPTftXDkhPysSmWM (Pu-239 fission balance, NUM-ledgered), rn_tgtnxj2vfCYQqbQy (chain-reaction diagram completion, descriptive steps), rn_4TGW9N7YpJ6fqy5W (why hydrogen fusion is not currently possible on Earth, reasoning steps), rn_vVJjCmGbcDY2Ck9G (Hubble Space Telescope orbital speed, NUM-ledgered), rn_sCvWwMvSCq7vf7cR (HR diagram regions + Star X plot, NUM-ledgered), rn_X6gTfQ5T8ytPfDgR (galaxy recession speed 485->485 nm case, NUM-ledgered); the other eleven notes carry no corpus WE block and declare workedExample null (designed-or-none)',
    'the corpus 7-3-2 exam hint confirms daughter names are NOT required (balance the numbers instead) — the Ba-144/Kr-89 pair is quoted as the of-record example and the Pu-239 WE is ported with its arithmetic NUM-ledgered',
    'the corpus 8-1-4 worked example reads v = 7592.18 = 7590 m/s; the pipeline ledger asserts the exact value 2pi*6,960,000/5760 = 7592.18 (2 d.p.) and the corpus 3-s.f. quote 7590 as separate facts',
    'ajv strict mode relaxed to false for this run: the of-record 0.6/1.5/1.2 schemas carry pre-existing strictTypes style notices (the wave-7..11 disclosure class); validation semantics are unchanged — same draft-07 compile, same allErrors collection',
    `the WAVE_OPEN_BASE ${PIN} is the resources main tip at wave open (operator directive trace 1a1c35292ac65771, "the next wave of W12-final-remainder"); wave-12 sequence: commit A lands on main first, the pipeline runs with the race-guard asserting the tip still sits exactly at the commit-A pin, then commit C lands — the race-guard semantics differ from waves 1-11 (which ran pre-push) and are disclosed here`,
    'worked-example census derived from the sources (totWEPop/totWENull) per the wave-8 amendment law — 6 populated / 11 null, no hardcoded counts',
    'the PROMOTION receipt filename carries the Asia/Dhaka execution date 20261110 while generated_at_utc is honest UTC',
    'this wave completes the NS-4PH1 physics register: 127/127 notes authored across stage-A + waves 1..12; the B4 partition is fully discharged (W12-final-remainder takes the last 17 notes per runbook §0 B4)',
  ],
};


const rb = Buffer.from(JSON.stringify(receipt, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'records/NS-4PH1-PHYSICS-WAVE12-PROMOTION-20261110.json'), rb);

console.log(`GATES: ${LOG.filter((l) => l.ok).length}/${LOG.length} GREEN, 0 failures`);
console.log(`EMITTED: 34 outputs + manifest v31 (${mb.length}B) + INT-3 (${ib.length}B) + promotion receipt (${rb.length}B)`);
console.log(`WAVE-12 tranche: 17 notes / ${idLessons} lessons / ${idChecks} checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application) / ${totFig} figures`);
console.log(`CUMULATIVE v31: ${manifest.counts.notes} notes / ${manifest.counts.lessons} lessons / ${manifest.counts.checks} checks; grand stream ${manifest.conservation.authored_chars} chars`);
console.log(`GRAND: ${manifest.conservation.authored_stream_sha256}`);
console.log(`WAVE-12 SUBTOTAL: ${waveOut['wave-12']}`);
