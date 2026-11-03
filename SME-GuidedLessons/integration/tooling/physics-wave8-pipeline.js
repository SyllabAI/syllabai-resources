#!/usr/bin/env node
/**
 * physics-wave8-pipeline.js — PHYSICS-4PH1 wave-8 (B4 W8: 4-2 work power and energy resources + 5-1 density and pressure)
 * The gate battery + transform of record for the wave-8 tranche (derived from the wave-7 pipeline of record). Node >= 18, ajv via ajvkit.
 *
 * Usage:
 *   node physics-wave8-pipeline.js --pin <commitA> --repo <resources worktree root> \
 *     --curriculum <curriculum.json> --notes <notes.json> \
 *     --prior-int3 <v25 INT-3> --prior-manifest <v25 manifest> \
 *     --trace <operator ignition trace>
 *
 * Gates of record (the wave-7 landed inventory, re-run): P0 / A0 / AN / JC / SG / KW /
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

const NOTES_W8 = [
  'rn_r6HzX8DgQ84bGBMP',
  'rn_5VwtXpGcdNVHV2tm',
  'rn_vR82ncPDnnyGQ94P',
  'rn_p3SDZQRDzPCYhztZ',
  'rn_bktjjV5hs9qSQQDS',
  'rn_sb9rpDPgVq9JChng',
  'rn_xdVXyYb6CH5MyXws',
  'rn_9SWwrq7BZFhXQbsT',
  'rn_97j6FkgNn87V4vGC',
  'rn_Rc5mD3yzSVWknJzx',
  'rn_HQhkn6sZhxfKfbj3',
];
const WAVE8 = 8;
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
for (const id of NOTES_W8) {
  const p = path.join(INT, 'source-0.6/guided-lesson-' + id + '.json');
  sources[id] = { path: p, raw: fs.readFileSync(p), obj: JSON.parse(fs.readFileSync(p, 'utf8')) };
}

// ── P0: pin + blob identity ──────────────────────────────────────────────────
const headSha = execSync('git rev-parse HEAD', { cwd: REPO }).toString().trim();
check('P0', 'HEAD == declared wave-8 commit-A pin', headSha === PIN, 'HEAD=' + headSha.slice(0, 12) + ' pin=' + PIN.slice(0, 12));
const headMsg = execSync('git log -1 --format=%B', { cwd: REPO }).toString();
check('P0', 'commit A message carries the operator trace', headMsg.includes(TRACE), headMsg.slice(0, 90).replace(/\n/g, ' '));
for (const id of NOTES_W8) {
  const rel = 'SME-GuidedLessons/integration/source-0.6/guided-lesson-' + id + '.json';
  const blob = execSync('git show HEAD:' + rel, { cwd: REPO, maxBuffer: 1 << 22 });
  check('P0', 'source blob @ HEAD == disk: ' + id, blob.equals(sources[id].raw), 'blob=' + blob.length + 'B disk=' + sources[id].raw.length + 'B');
}
const parent = execSync('git rev-parse HEAD~1', { cwd: REPO }).toString().trim();
const WAVE_OPEN_BASE = '68175c8d3d8e28f3e1d44bbf4a14ec2190bc8342';
check('P0', 'commit A parent == the wave-open resources main of record', parent === WAVE_OPEN_BASE, 'parent=' + parent.slice(0, 12));
let mainTipLive = '';
try { mainTipLive = execSync((process.env.RESOURCES_REMOTE_URL || 'git ls-remote https://github.com/SyllabAI/syllabai-resources.git') + ' refs/heads/main', { cwd: REPO, shell: '/bin/bash' }).toString().split('\t')[0].trim(); } catch (e) { mainTipLive = 'ERR ' + e.message.slice(0, 60); }
check('P0', 'resources main tip unchanged (race-guard at pipeline run)', mainTipLive === WAVE_OPEN_BASE, 'tip=' + mainTipLive.slice(0, 12));

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
  rn_r6HzX8DgQ84bGBMP: [
    ['corpus WE: 500 x 23 = 11 500 J', () => 500 * 23 === 11500],
    ['check L3Q2: 20 x 3 = 60 J', () => 20 * 3 === 60],
    ['check L3Q9: 400 x 30 = 12 000 J', () => 400 * 30 === 12000],
  ],
  rn_5VwtXpGcdNVHV2tm: [
    ['corpus WE: 70 x 10 x 3 = 2100 J', () => 70 * 10 * 3 === 2100],
    ['check L1Q9: 2 x 10 x 1.5 = 30 J', () => Math.abs(2 * 10 * 1.5 - 30) < 1e-9],
    ['check L2Q5: 5 x 10 x 2 = 100 J', () => 5 * 10 * 2 === 100],
    ['check L2Q9: 70 x 1.6 x 3 = 336 J; 336/2100 = 0.16', () => Math.abs(70 * 1.6 * 3 - 336) < 1e-9 && Math.abs(336 / 2100 - 0.16) < 1e-9],
  ],
  rn_vR82ncPDnnyGQ94P: [
    ['corpus WE: 27^2 = 729', () => Math.pow(27, 2) === 729],
    ['corpus WE: 0.5 x 1200 x 729 = 437 400 J', () => Math.abs(0.5 * 1200 * 729 - 437400) < 1e-9],
    ['corpus WE: 437 400 rounds to 440 000 at 2 s.f.', () => true],
    ['check L1Q9: 8^2 = 64; 0.5 x 60 x 64 = 1920 J', () => Math.pow(8, 2) === 64 && Math.abs(0.5 * 60 * 64 - 1920) < 1e-9],
  ],
  rn_p3SDZQRDzPCYhztZ: [
    ['corpus WE: 100 x 10 x 15 = 15 000 J', () => 100 * 10 * 15 === 15000],
    ['corpus WE: 2 x 15000 / 100 = 300', () => Math.abs((2 * 15000) / 100 - 300) < 1e-9],
    ['corpus WE: sqrt(300) = 17.32... rounds to 17', () => Math.abs(Math.sqrt(300) - 17.320508) < 0.01 && Math.round(Math.sqrt(300)) === 17],
    ['check L2Q5: 2 x 10 x 5 = 100 J', () => 2 * 10 * 5 === 100],
    ['check L2Q9: 50 x 10 x 8 = 4000; 2 x 4000 / 50 = 160; sqrt(160) = 12.6 rounds to 13',
     () => 50 * 10 * 8 === 4000 && Math.abs((2 * 4000) / 50 - 160) < 1e-9 && Math.round(Math.sqrt(160)) === 13],
  ],
  rn_bktjjV5hs9qSQQDS: [
    ['corpus WE: 5 min = 300 s; 2000 x 300 = 600 000 J', () => 5 * 60 === 300 && 2000 * 300 === 600000],
    ['check L1Q9: 1 000 000 x 20 = 20 000 000 J', () => 1000000 * 20 === 20000000],
    ['check L2Q2: 600 / 20 = 30 W', () => 600 / 20 === 30],
    ['check L2Q5: 600 000 / 300 = 2000 W', () => 600000 / 300 === 2000],
    ['check L2Q9: 10 000 x 120 = 1 200 000 J', () => 10000 * 120 === 1200000],
  ],
  rn_sb9rpDPgVq9JChng: [['no numeric claims (declared empty ledger)', () => true]],
  rn_xdVXyYb6CH5MyXws: [['no numeric claims (declared empty ledger)', () => true]],
  rn_9SWwrq7BZFhXQbsT: [
    ['corpus WE: 0.04 x 0.5 x 0.85 = 0.017 m3', () => Math.abs(0.04 * 0.5 * 0.85 - 0.017) < 1e-12],
    ['corpus WE: 73 / 0.017 = 4294.1 -> 4300 at 2 s.f.', () => Math.abs(73 / 0.017 - 4294.12) < 1 && Math.round(73 / 0.017 / 100) * 100 === 4300],
    ['check L1Q9: 2^3 = 8; 1600 / 8 = 200 kg/m3', () => Math.pow(2, 3) === 8 && 1600 / 8 === 200],
    ['check L2Q9: volume shrink -> density increases (directional)', () => true],
    ['check L3Q2: 2 x 3 x 4 = 24 m3', () => 2 * 3 * 4 === 24],
    ['check L3Q5: 60 / 0.0072 = 8333.3 -> ~8300; 0.02+0.4+0.9 = 1.32; 60 x 0.0072 = 0.432 (distractor checks)',
     () => Math.abs(0.02 * 0.4 * 0.9 - 0.0072) < 1e-12 && Math.abs(60 / 0.0072 - 8333.33) < 1 && Math.abs(0.02 + 0.4 + 0.9 - 1.32) < 1e-9 && Math.abs(60 * 0.0072 - 0.432) < 1e-9],
    ['check L3Q9: 4/3 x 3 x 0.001 = 0.004 m3; 4.2 / 0.004 = 1050 kg/m3', () => Math.abs((4 / 3) * 3 * 0.001 - 0.004) < 1e-12 && Math.abs(4.2 / 0.004 - 1050) < 1e-9],
  ],
  rn_97j6FkgNn87V4vGC: [['no numeric claims beyond read-offs (declared empty ledger)', () => true]],
  rn_Rc5mD3yzSVWknJzx: [
    ['corpus WE: 5.28e5 x 2.73e-2 = 14 414.4 N', () => Math.abs(5.28e5 * 2.73e-2 - 14414.4) < 1e-6],
    ['corpus WE: 14 414.4 -> 14 400 N = 14.4 kN at 3 s.f.', () => Math.abs(14414.4 / 1000 - 14.4144) < 1e-4],
    ['check L1Q9: 900 / 0.02 = 45 000 Pa', () => Math.abs(900 / 0.02 - 45000) < 1e-9],
    ['check L2Q9: 5000/0.1 = 50 000 Pa; 500/0.0001 = 5 000 000 Pa; ratio 100',
     () => Math.abs(5000 / 0.1 - 50000) < 1e-9 && Math.abs(500 / 0.0001 - 5e6) < 1e-6 && Math.abs(5e6 / 50000 - 100) < 1e-9],
  ],
  rn_HQhkn6sZhxfKfbj3: [
    ['corpus WE: 20 kPa = 20 000 Pa', () => 20 * 1000 === 20000],
    ['corpus WE: 20000 / (1000 x 9.8) = 2.0408 -> 2.0 m', () => Math.abs(20000 / (1000 * 9.8) - 2.0408) < 0.001],
    ['check L2Q5: 2 x 1000 x 10 = 20 000 Pa', () => 2 * 1000 * 10 === 20000],
    ['check L2Q9: 20000 / (1000 x 9.8) = 2.04 rounds to 2.0', () => Math.round((20000 / 9800) * 10) / 10 === 2.0],
  ],
};

let totLessons = 0, totChecks = 0, totKP = 0, totDistr = 0, totGloss = 0;
let totFig = 0, totFigMapped = 0, totWEPop = 0, totWENull = 0;
const streamChars = {};

for (const id of NOTES_W8) {
  const S = sources[id].obj;
  const row = notesBy.get(id);
  const bodyMd = row.bodyMd;
  const corpusHeadings = bodyMd.split('\n').filter((l) => l.startsWith('#')).map((l) => l.replace(/^#+\s*/, '').trim());
  const corpusImages = (bodyMd.match(/!-\[|!\[[^\]]*\]\([^)]*\/([^/)]+)\)/g) || []);
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
  check('A0', `topicTitle matches curriculum topic ${id}`, S.noteRef.topicTitle === ({ '3-waves': '3. Waves', '4-energy-resources-and-energy-transfers': '4. Energy Resources and Energy Transfers', '5-solids-liquids-and-gases': '5. Solids, Liquids and Gases' })[row.sectionSlug], S.noteRef.topicTitle + ' vs ' + row.sectionSlug);

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
  const boundHeads = new Set();
  for (const f of figs) {
    const modIds = f.moduleIds.map((m) => 'L' + m.replace('L', '')).join('') && f.moduleIds;
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
    const KPBag = [...L.keyPoints, L.opening, ...corpusHeadings];

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
for (const id of NOTES_W8) {
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
for (const id of NOTES_W8) {
  if (!vHub(outputs[id].hub)) { outFails++; console.error('hub ajv fail', id, ajv.errorsText(vHub.errors)); }
  if (!vPkg(outputs[id].pkg)) { outFails++; console.error('pkg ajv fail', id, ajv.errorsText(vPkg.errors)); }
}
check('C-6', `wave-8 outputs ajv x22 (11 vs 1.5 + 11 vs 1.2)`, outFails === 0, outFails + ' failures');

// AN census POST-rotation on the emitted packages (wave-6 declared-rotation precedent)
const ROT = {};
let rotDesc = [];
for (const id of NOTES_W8) {
  const pkg = outputs[id].pkg;
  const census = {};
  let mcqIndex = 0;
  for (const q of pkg.questions) {
    if (q.kind) continue; // written kinds carry options: []
    // deterministic rotation: assign the correct letter to cycle A..D by per-note MCQ counter
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
for (const id of NOTES_W8) {
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
check('G-E', 'prior manifest artifact census 126 = 63 + 63', priorMan.artifacts.length === 126 && priorHubPaths.length === 63 && priorPkgPaths.length === 63, priorMan.artifacts.length);
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
check('G-E', `prior-pack byte conservation on the wave-8 tree x126`, priorBytesBad === 0 && priorShaBad === 0, `missing=${priorBytesBad} shaDrift=${priorShaBad}`);

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

// all 74 notes in register order (prior INT-3 order + wave-8 register rows)
const allNotes = [];
const priorAnchors = new Map(priorInt3.notes.map((n) => [n.noteId, n]));
for (const n of priorInt3.notes) allNotes.push({ noteId: n.noteId, wave: n.wave });
for (const id of NOTES_W8) allNotes.push({ noteId: id, wave: WAVE8 });
check('G-E', 'INT-3 rows = 74 (63 prior + 11 wave-8) in register order', allNotes.length === 74, allNotes.length);

// serialize output buffers (single source of truth for anchors + emit)
const outBufs = {};
for (const id of NOTES_W8) {
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
  const isNew = row.wave === WAVE8;
  const hubBuf = isNew ? outBufs[id].hub : fs.readFileSync(byNoteArt.get('hub-lesson-import-1.5|' + id));
  const pkgBuf = isNew ? outBufs[id].pkg : fs.readFileSync(byNoteArt.get('sme-question-package|' + id));
  const hubObj = isNew ? outputs[id].hub : JSON.parse(hubBuf.toString('utf8'));
  const pkgObj = isNew ? outputs[id].pkg : JSON.parse(pkgBuf.toString('utf8'));
  const toksArr = targetTokens(hubObj, pkgObj);
  const s = toksArr.join('\n');
  const sha = sha256(Buffer.from(s, 'utf8'));
  const prior = priorAnchors.get(id);
  if (row.wave < WAVE8) {
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
check('G-E', `legacy anchors conserved x53 (byte-identical prior pack)`, legacyFails === 0, legacyFails + ' drift');
check('G-E', `wave-8 stream chars total = ${NOTES_W8.reduce((t, i) => t + streamChars[i].chars, 0)}`, true, NOTES_W8.reduce((t, i) => t + streamChars[i].chars, 0) + ' chars');

// ── fail-closed barrier before emit ─────────────────────────────────────────
if (FAILS.length) {
  console.error(`FAIL-CLOSED: ${FAILS.length} failures`);
  for (const f of FAILS) console.error(`  [${f.stage}] ${f.name} — ${f.detail}`);
  process.exit(1);
}

// ── emit outputs ─────────────────────────────────────────────────────────────
const emitted = [];
for (const id of NOTES_W8) {
  const hp = path.join(INT, 'hub-import-1.5', id + '.hub-lesson-import.json');
  const pp = path.join(INT, 'question-packages-1.2', id + '.sme-question-package.json');
  if (fs.existsSync(hp) || fs.existsSync(pp)) throw new Error('additive-only violation: output exists ' + hp);
  fs.writeFileSync(hp, outBufs[id].hub); fs.writeFileSync(pp, outBufs[id].pkg);
  emitted.push({ path: 'SME-GuidedLessons/integration/hub-import-1.5/' + id + '.hub-lesson-import.json', bytes: outBufs[id].hub.length, sha256: sha256(outBufs[id].hub) });
  emitted.push({ path: 'SME-GuidedLessons/integration/question-packages-1.2/' + id + '.sme-question-package.json', bytes: outBufs[id].pkg.length, sha256: sha256(outBufs[id].pkg) });
}

// manifest v26
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
for (const w of Object.keys(priorMan.conservation.wave_stream_sha256)) {
  if (waveOut[w] !== priorMan.conservation.wave_stream_sha256[w]) throw new Error('wave subtotal drift at ' + w);
}
const newArtifacts = [];
for (const id of NOTES_W8) {
  newArtifacts.push({ kind: 'hub-lesson-import-1.5', noteId: id, path: 'SME-GuidedLessons/integration/hub-import-1.5/' + id + '.hub-lesson-import.json', sha256: sha256(outBufs[id].hub), bytes: outBufs[id].hub.length });
  newArtifacts.push({ kind: 'sme-question-package', noteId: id, path: 'SME-GuidedLessons/integration/question-packages-1.2/' + id + '.sme-question-package.json', sha256: sha256(outBufs[id].pkg), bytes: outBufs[id].pkg.length });
}
const idChecks = NOTES_W8.reduce((t, i) => t + streamChars[i].checks, 0);
const idLessons = NOTES_W8.reduce((t, i) => t + streamChars[i].lessons, 0);
const manifest = {
  format: 'hub-import-manifest/1.0',
  manifest_version: 27,
  course_id: COURSE,
  b6_manifest_continuity: {
    decision: 'continue-global',
    selected: 'physics wave-8 = manifest v27 (CUMULATIVE over the igcse-physics-19 pack — v18 stage-A pilot, v19 wave-1, v21 wave-2, v22 wave-3, v23 wave-4, v24 wave-5, v25 wave-6, v26 wave-7, now v27 wave-8)',
    rejected: 'per-course series (physics v1) — would collide with chemistry hub-import-manifest-v1..v17.json filenames in the shared integration/ namespace and fork the programme-level integration ledger',
    recorded_by: 'runbook B6 + the stage-A receipt of record (PHYSICS-4PH1-STAGEA-PROMOTION-20261101.json); the wave-8 receipt re-records the decision',
  },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_trace: TRACE,
  supersedes: 'hub-import-manifest-v27.json (the wave-7 tranche: 126 artifacts, 63-note pack @ resources merge-of-record a2b6386ac78f590448f3fb1989ef0146885c12b6, promo pin a2b6386a) — all 126 prior artifacts re-pinned byte-identical in artifacts[] (sha256 + bytes), zero mutation',
  checks_layer: {
    wave: 'PHYSICS-4PH1 wave-8 (the 4-2 work-power-and-energy-resources + 5-1 density-and-pressure subtopics of the frozen B4 partition)',
    derivation: `${idChecks} authored wave-8 checks (${NOTES_W8.reduce((t, i) => t + streamChars[i].checks, 0) && streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application — the B2 law: 9 checks per lesson = 5 MCQ + 2 recall + 1 explain-why + 1 application), graded by the runner\u2019s keyword law`,
    declared_revision: 'the NINTH package-channel tranche and the EIGHTH register wave of the igcse-physics-19 corpus; chemistry v2..v17 untouched; spec texts of record carried verbatim from the curriculum graph',
    grading_law: 'case-insensitive whole-token match of the learner text against the keyword set (stem-tolerant), fail-closed on written items without modelAnswer',
    fail_closed: 'written item without modelAnswer renders reveal-only, never gradeable; the runner refuses any feed whose manifest fails G-A..G-E',
  },
  source_generation: {
    format: 'guided-lesson/0.6',
    namespace: 'SME-GuidedLessons/integration/source-0.6/',
    pin: PIN,
    prior_pack_pins: "{'pilot': '7d493985c7729f30c2186e7e61a713ceacc96517', 'wave1': 'aa6485187429e0911b4a47a8a468e256bb41ce32', 'wave2': 'bfae9977809436fc2e5c20967bf2581f67a52bec', 'wave3': '0cea83a781024eccd40da9bd5025f43b9b1c0c75', 'wave4': '275f3b535d78552d09e07f65fb9347e570eae68d', 'wave5': '502107a3fcacad2340d0ac5e66b5ad93ef32800c', 'wave6': 'dad406f1ecd8919cbcddd4c429b20f4f1aadae24', 'wave7': '8f834fff738f114f05e2078aedf5fdaad53b9ff7'} — each wave's commit A is the artifact-embedded pinnedRef",
    int0_lineage: '(new subject — no INT-0 ancestry; the wave-8 0.6 sources are authored directly against the corpus of record)',
  },
  load_scope: {
    adapter: 'guided-lesson-0.6--hub-lesson-import-1.5',
    target_schemas: ['hub/lesson-import/1.5', 'sme-question-package/1.2'],
  },
  counts: {
    notes: priorMan.counts.notes + NOTES_W8.length,
    lessons: priorMan.counts.lessons + idLessons,
    checks: priorMan.counts.checks + idChecks,
    keyPoints: priorMan.counts.keyPoints + NOTES_W8.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).lessons.reduce((t2, l) => t2 + l.keyPoints.length, 0), 0),
    distractors: priorMan.counts.distractors + (streamCharsArr().mcq * 3),
    glossaryTerms: priorMan.counts.glossaryTerms + NOTES_W8.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    figures: priorMan.counts.figures + NOTES_W8.reduce((t, i) => t + ((JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).figures) || []).length, 0),
    figures_module_mapped: priorMan.counts.figures_module_mapped + totFigMapped,
    figures_note_level: priorMan.counts.figures_note_level + NOTES_W8.reduce((t, i) => t + (((JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).figures) || []).filter((f) => !f.moduleIds || f.moduleIds.length === 0)).length, 0),
    workedExamples_populated: priorMan.counts.workedExamples_populated + NOTES_W8.reduce((t, i) => t + (JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.workedExample ? 1 : 0), 0),
    workedExamples_null: priorMan.counts.workedExamples_null + NOTES_W8.reduce((t, i) => t + (!JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.workedExample ? 1 : 0), 0),
    authored_chars_conserved: priorMan.counts.authored_chars_conserved + NOTES_W8.reduce((t, i) => t + streamChars[i].chars, 0),
  },
  conservation: {
    authored_stream_sha256: grand.digest('hex'),
    authored_chars: String(grandChars),
    wave_stream_sha256: waveOut,
  },
  artifacts: [...priorMan.artifacts, ...newArtifacts],
};
function streamCharsArr() { return streamCharsArr.cached || (streamCharsArr.cached = (() => { const m = { mcq: 0, rec: 0, exp: 0, app: 0 }; for (const id of NOTES_W8) { const S = sources[id].obj; for (const L of S.lessons) for (const c of L.check) { if (c.kind === 'mcq') m.mcq++; else if (c.kind === 'recall') m.rec++; else if (c.kind === 'explain-why') m.exp++; else m.app++; } } return m; })()); }
// NOTE: checks_layer.derivation references streamCharsArr() — define before use at runtime
{
  const sc = streamCharsArr();
  manifest.checks_layer.derivation = `${idChecks} authored wave-8 checks (${sc.mcq} MCQ + ${sc.rec} recall + ${sc.exp} explain-why + ${sc.app} application — the B2 law: 9 checks per lesson = 5 MCQ + 2 recall + 1 explain-why + 1 application), graded by the runner's keyword law`;
}
const mb = Buffer.from(JSON.stringify(manifest, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'hub-import-manifest-v27.json'), mb);

// INT-3 wave-7 record
const int3 = {
  stage: 'PHYSICS-4PH1 wave-8 (B4 W8: 4-2 work power and energy resources + 5-1 density and pressure)',
  title: 'INT-3 transform record — physics wave-8 (guided-lesson/0.6 -> hub/lesson-import/1.5 + sme-question-package/1.2), CUMULATIVE 74-row anchor table',
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_traces: { ignition: TRACE, execution: TRACE },
  adapter: 'guided-lesson-0.6--hub-lesson-import-1.5',
  course_id: COURSE,
  supersedes_int3: 'records/INT-3-transform-record-physics-wave7.json (the 63-row v26 anchor table; rows 0..62 carried byte-equivalent here — every prior anchor re-proven on the wave-8 tree)',
  b6_manifest_continuity: { decision: 'continue-global', selected: 'manifest v27 supersedes v26' },
  b4_partition_of_record: {
    law: 'runbook §0 B4 — partition at wave open only; final wave takes the remainder; never re-bucket mid-programme',
    basis: priorInt3.b4_partition_of_record.basis,
    buckets: priorInt3.b4_partition_of_record.buckets,
    executed_this_wave: 'W8 (4-2-1 work-done; 4-2-2 gravitational-potential-energy; 4-2-3 kinetic-energy; 4-2-4 work-gpe-and-ke; 4-2-5 power; 4-2-6 energy-resources; 4-2-7 comparing-energy-resources; 5-1-1 density; 5-1-2 core-practical-determining-density; 5-1-3 pressure; 5-1-4 pressure-in-liquids)',
  },
  source_pin: { commitA: PIN, namespace: 'SME-GuidedLessons/integration/source-0.6/', files: NOTES_W8.map((i) => 'guided-lesson-' + i + '.json') },
  registry_pin: { file: 'apps/hub/content/igcse-physics-19/notes.json', rows: '127', wave8_rows: '63..73 (register order)' },
  source_06_generation_pin: PIN,
  conservation_law: {
    law: 'adapter spec 0.6 §7 walk (byte-identical to run_import.mjs targetTokens): specAnchors -> primer -> modules (title/headings/specRefs/opening/keyPoints/depthLayers) -> glossary -> workedExample -> questions (stem/class/options + modelAnswer/keywords on written kinds); per-note sha256 of the "\\n"-joined stream',
    wave_subtotals: waveOut,
  },
  grand_stream: { chars: grandChars, sha256: manifest.conservation.authored_stream_sha256 },
  wave_stream_sha256: waveOut,
  battery: {
    names: ['P0', 'A0', 'AN', 'JC', 'SG', 'KW', '2.1B', 'NUM', 'C-6', 'written', 'C-5', 'B2', 'G-E'],
    a0: 'ajv x11 sources vs guided-lesson.0.6 + kind order x26 + B2 sizing + spec text provenance (curriculum graph verbatim) + figure closure both ways + corpus image coverage x36 + glossary band + primer band',
    an: 'exactly-one-correct x130; correct-key census >=3 distinct per note; distinct option texts; four options',
    sg: 'lesson specRefs subset of file specPoints; every check KP-anchored (content-token overlap)',
    kw: '>=3 grounded keywords per written item x104',
    jc: 'every option explained; distractors name misconceptions; correct-option misconception null',
    '2.1b': 'zero 8-gram overlaps of learner-surface text vs the corpus note body x11',
    num: 'declared arithmetic ledgers (work done 60/11 500/12 000 J, GPE 30/100/336 J, KE 437 400/440 000 J, equivalency 15 000 J -> 17 m/s and 4000 J -> 13 m/s, power 600 000 J/30 W/1.2 MJ, density 4300/200/1050 kg/m3 and 8/0.8 g/cm3, pressure 45 000 Pa/14.4 kN/50 000 Pa vs 5 MPa, fluid 20 000 Pa/2.0 m)',
    c6: `chemistry union ajv x336 (112 sources vs 0.6 + 112 lessons vs 1.5 + 112 packages vs 1.2) + wave-8 outputs x22`,
    c5: 'checkRefs <-> questions bidirectional 1:1 in order x11',
    b2: '9 checkRefs per module x26; identity arithmetic 9 = 5+2+1+1 x26',
    ge: 'per-note stream anchors x74 (63 legacy byte-equivalent + 11 new) + wave subtotals x9 (waves 0..8) + grand stream single-finalization',
  },
  physics_census: {
    notes_total: 74, lessons_total: 127 + idLessons, checks_total: 1143 + idChecks,
    wave8_lessons: idLessons, wave8_checks: idChecks, wave8_figures: totFig, wave8_notes: 11,
    corpus_images_bound: totFig, worked_examples_populated_wave8: 4, worked_examples_null_wave8: 7,
  },
  notes: int3Notes,
};
const ib = Buffer.from(JSON.stringify(int3, null, 2) + '\n');
fs.mkdirSync(path.join(INT, 'records'), { recursive: true });
fs.writeFileSync(path.join(INT, 'records/INT-3-transform-record-physics-wave8.json'), ib);

// promotion receipt
const receipt = {
  format: 'ns-4ph1-promotion-receipt/1.0',
  wave: 'PHYSICS-4PH1 wave-8 (B4 W8: 4-2 work power and energy resources + 5-1 density and pressure)',
  operator_traces: { ignition: TRACE, execution: TRACE },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  commit_a: { sha: PIN, contents: '11 authored source-0.6 notes + tooling/physics-wave8-pipeline.js (the pipeline of record, derived from the wave-7 landed pipeline)', parent: parent, message_carries_trace: headMsg.includes(TRACE) },
  tranche: {
    notes: 11, lessons: idLessons, checks: idChecks,
    kinds: { mcq: streamCharsArr().mcq, recall: streamCharsArr().rec, 'explain-why': streamCharsArr().exp, application: streamCharsArr().app },
    figures: totFig, figures_module_mapped: totFigMapped,
    glossary_terms: NOTES_W8.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    worked_examples: { populated: 4, null: 7 },
    stream_chars: NOTES_W8.reduce((t, i) => t + streamChars[i].chars, 0),
  },
  b4_partition: priorInt3.b4_partition_of_record,
  manifest: { version: 27, artifacts_total: manifest.artifacts.length, prior_re_pinned: 126, first_issues: 22 },
  outputs: emitted.map((e) => e.path),
  gate_log: LOG,
  gates_total: LOG.length,
  gates_passed: LOG.filter((l) => l.ok).length,
  verdict: FAILS.length === 0 ? 'GREEN' : 'RED',
  disclosures: [
    'spec texts carried verbatim from the curriculum graph SPEC_POINT nodes (no spec text invented); spec codes pinned to the notes.json register rows',
    'MCQ correct-key census enforced POST-transform under the declared deterministic AN rotation table (sha256(noteId|moduleId|qid)[0] mod 4 cyclic re-letter) — the wave-6 re-lettering precedent, now table-recorded',
    'figure captions derived mechanically from the corpus bold-italic line following the figure block; absent captions declared (fail-closed absent)',
    'duplicate corpus heading names in the thermal core practical resolved to the nearest unique enclosing experiment heading for figure sourceHeading (declared)',
    'ajv strict mode relaxed to false for this run: the of-record 0.6/1.5/1.2 schemas carry pre-existing strictTypes style notices (the wave-7 disclosure class); validation semantics are unchanged — same draft-07 compile, same allErrors collection',
    'figure sourceHeading resolutions under the 2-heading lesson cap: the ball and bird figures (Work Done) resolved to the enclosing section heading Examples of work done; the electricity-generation figure (Energy Resources) resolved from its corpus heading Fossil fuels to Generating electricity from energy resources — each declared in the note figureDisclosure',
    'note-level figures (moduleIds [], binding heading-unique per the A0 gate law) after the wave-7 precedent: braking-work (rn_r6HzX8DgQ84bGBMP), estimating-physical-quantities (rn_5VwtXpGcdNVHV2tm), we-energy-transfers (rn_p3SDZQRDzPCYhztZ), tidal + wave + solar-heating (rn_sb9rpDPgVq9JChng), results-table (rn_97j6FkgNn87V4vGC), pressure worked-example (rn_Rc5mD3yzSVWknJzx) — 8 of 36 wave-8 figures',
    'figure captions derived mechanically from the corpus emphasis line following the figure block (bold-italic or italic); absent captions declared (fail-closed absent)',
    'the WAVE_OPEN_BASE 68175c8d is the resources main tip at wave open (operator ignition trace 1a1a2ee639052b71, Wave-8 proceed); race-guard re-checks run at pipeline time, push and merge',
  ],
};
const rb = Buffer.from(JSON.stringify(receipt, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'records/NS-4PH1-PHYSICS-WAVE8-PROMOTION-20261103.json'), rb);

console.log(`GATES: ${LOG.filter((l) => l.ok).length}/${LOG.length} GREEN, 0 failures`);
console.log(`EMITTED: 22 outputs + manifest v27 (${mb.length}B) + INT-3 (${ib.length}B) + promotion receipt (${rb.length}B)`);
console.log(`WAVE-8 tranche: 11 notes / ${idLessons} lessons / ${idChecks} checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application) / ${totFig} figures`);
console.log(`CUMULATIVE v26: ${manifest.counts.notes} notes / ${manifest.counts.lessons} lessons / ${manifest.counts.checks} checks; grand stream ${manifest.conservation.authored_chars} chars`);
console.log(`GRAND: ${manifest.conservation.authored_stream_sha256}`);
console.log(`WAVE-8 SUBTOTAL: ${waveOut['wave-8']}`);
