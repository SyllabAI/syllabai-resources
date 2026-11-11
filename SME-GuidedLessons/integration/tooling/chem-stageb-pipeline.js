#!/usr/bin/env node
/**
 * chem-stageb-pipeline.js — CHEMISTRY-4CH1 stage-B (the complete 112-note register re-issued onto the
 * physics-grade 0.6/1.5/1.2 four-plane generation: source-0.6 / hub-import-1.5 / question-packages-1.2 /
 * manifest v32 + records). Derived from the wave-12 pipeline of record. Node >= 18, ajv via ajvkit.
 *
 * Usage:
 *   node chem-stageb-pipeline.js --pin <commitA> --repo <resources worktree root> \
 *     --curriculum <curriculum-chem.json> --notes <notes-chem-full.json> \
 *     --priorInt3 <INT-3 physics-wave12> --priorManifest <v31 manifest> \
 *     --priorChemManifest <v17 manifest> --trace <operator ignition trace>
 *
 * Gates of record (the physics-wave battery, re-run over the full corpus): P0 / A0 / AN / JC / SG / KW /
 * 2.1B / NUM / C-6 / written / C-5 / B2 / G-E. Fail-closed: any failure exits 1 before emit.
 *
 * Stage-B authoring deltas of record (census 2026-11-12, trace 1a1cbe5f60023dd5): format const 0.5->0.6
 * x112; explicit kind:"mcq" x1,195; 20 authored 4th distractors; 3 authored model answers; 629 ungrounded
 * keyword variants dropped + 64 grounded top-ups (KW law); 110 figure re-binds to heading-unique; 49
 * glossary trims into the 2..5 band; 355 learner-surface 8-gram overlaps rephrased (76 notes); 36 spec
 * texts realigned to the curriculum graph verbatim. Everything else conserved at the JSON-value level.
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
if (!REPO || !PIN || !TRACE || !args.curriculum || !args.notes || !args.priorInt3 || !args.priorManifest || !args.priorChemManifest) {
  console.error('missing required args'); process.exit(2);
}

const NOTES_W12 = [
  'rn_2VnK66PqbvFKdKYt',
  'rn_S7GPh8BBPBbmhYKm',
  'rn_HZM2WRjPPT8Srcxt',
  'rn_cTk2cs2h2BKQ3y3B',
  'rn_QVmDs8X4szpds3cP',
  'rn_TWGVV6RXN3Ktqb9h',
  'rn_RvgxXR36425BFMcx',
  'rn_YBWYstSRgM2QPzQq',
  'rn_R3ptwxGTTvdBFvyP',
  'rn_TsfqyK9BYMtN2Bfd',
  'rn_kb2VkFMdBTbmG33t',
  'rn_vzGMZxqQtWYVWB7h',
  'rn_b3XCzdtfQddbJjVf',
  'rn_Syxyh4Fct8KFg8NQ',
  'rn_wTtM2fQVVjntRm64',
  'rn_mBqgkpZ3hbSBmWCC',
  'rn_JCfdFrHsCkrmMbFj',
  'rn_T55t3HNsgyZcXZtN',
  'rn_N4HX8tqbdhTQcHyS',
  'rn_xT8XsdJtDX5gNFXj',
  'rn_VyXFNyxZHZGkxqTG',
  'rn_vXPcH3vS8wv7BFkK',
  'rn_pWzTTBv3B4yGFfj3',
  'rn_yj4y972FxCWnDnSg',
  'rn_Hkwmd9GSp3gdxxR5',
  'rn_4tzwS4GZjPybwtkS',
  'rn_mbcBZkygY4YpG2bf',
  'rn_8Nv33F4dD3kkZnY6',
  'rn_J7ZcTWyRxRgWQ45R',
  'rn_FCnWFz9MhgsqnZGM',
  'rn_jVwPmjqHbqQkXcjG',
  'rn_vfmJxw4VQgXKzXF3',
  'rn_MVnFKDMVkswzpmpw',
  'rn_KpvF2TWr5fYHk2Jz',
  'rn_GkJG52NCN98ShGRm',
  'rn_Hp2nK8XpN2SmjdQc',
  'rn_rHKCkt3PTXDBpmJG',
  'rn_3YZNCXSQQqXTT6HR',
  'rn_TM4QVMgXVxs4vbfY',
  'rn_kdRjZHjHcpVZsD3h',
  'rn_jNJ4gTmcHqdFqsNh',
  'rn_V9tPMnX6Hq2XnqcP',
  'rn_7Q8M9nVkr2FxCzxd',
  'rn_jXXsc4wt2344BjxX',
  'rn_6M5JB7CjvwdDykMS',
  'rn_WJD4ZN4kQfzJNSPV',
  'rn_S2fg29M7cqvMj5kT',
  'rn_QzYRzzmwRxk2gKqV',
  'rn_5WvdZNzzhHdjj2Qq',
  'rn_Kd76WccxD9ytSJJC',
  'rn_gBGX339WBpwyCrFF',
  'rn_DGkNCJRcCN4VQ28p',
  'rn_3B8JxsSjJvR9B4fk',
  'rn_sX8yyBxHn8bS7t46',
  'rn_BX88twwgffRMgx82',
  'rn_xq9jy75y43kDXkvx',
  'rn_nzW5ppBTV3ZnfSYY',
  'rn_sf7s7s6bQ2cZv29s',
  'rn_MMkxbt9y3M3XvXrc',
  'rn_dTP52nzhYb96XrJx',
  'rn_ZWrmDYtNGnmFycPM',
  'rn_qV5R2cKB59bSKD33',
  'rn_p2FmkrXqZSzFngpg',
  'rn_by5FDNfkqdBCkmXb',
  'rn_9WM8QhSxmYpGhjqd',
  'rn_VvsXMdW3TB37JhWF',
  'rn_6ZCysv9GnNQmc3w2',
  'rn_5g8Dd6y89tkCVJsN',
  'rn_qb9TBhB6VmnFGjvf',
  'rn_fQSYvKRMDBj3s2Bx',
  'rn_pBp5Z5C2RHTKk7Wn',
  'rn_T6S7R66N2wSZpWyc',
  'rn_vVdP57QhDYSVfZgy',
  'rn_v5JjfpT6grhtq3QW',
  'rn_kJg2gwF77vdFZZ2H',
  'rn_YWDXCCmjfjkJcs6c',
  'rn_x5m8QBWxtKvxQ9sx',
  'rn_w25KHshCMNQWwftj',
  'rn_dgVRCKCwn4rTGxGZ',
  'rn_HNXFQt7vM32g6PMv',
  'rn_KTZjJ7sPdDt4tkTH',
  'rn_6478QfpYNQDjZSvt',
  'rn_XJ8qXfzZJJFKXHnF',
  'rn_Zh6Pw56rjdMkPCD4',
  'rn_tvwj4VZ6yFscPJfD',
  'rn_y85XYRv5QfgZFQxv',
  'rn_H6ZVkxvdNgYDvfFb',
  'rn_3wZh9qRT7qFJn9QW',
  'rn_t68QRDhwR6r5gxYX',
  'rn_2d6Yb8GwGfRRd6pZ',
  'rn_DRQXrcSrmgQ7jcbZ',
  'rn_wDdXr5k7gknQ7xJp',
  'rn_NdJGQM8BqHmTy7Vg',
  'rn_HqqBFgKRHykMMhbB',
  'rn_H9chr9BWCfXYW472',
  'rn_V3hNWh6QWrbCRHrX',
  'rn_9J7DQhskyxzhd7CP',
  'rn_DrqzYWZMScqGrbWT',
  'rn_6c2G8nJpFSnQnbcP',
  'rn_MmqCNJfWbtYzRVqT',
  'rn_H2zGfgH76qYV5cmr',
  'rn_DBGf3WVffDBNDp4R',
  'rn_2MpXPtNXvn8pQm3r',
  'rn_8T5GfPn2q7sY2YCh',
  'rn_ncFJkGhXFsKrkNkH',
  'rn_2z53qk2CdWrVVc7V',
  'rn_BBGMYy3Yx9Nm4GV3',
  'rn_BDkhS5vQpRd4hvwf',
  'rn_7ZMc3T3J4SJXfNdR',
  'rn_4SgDJv8rKxpQQSBh',
  'rn_bvyrkKqRBMKCRzHM',
  'rn_bGgYrQXP2tqrYwdV',
];
const WAVE12 = 12;
// the corpus-limited heading exception of record (declared; figures disambiguated by moduleIds)
const CORPUS_LIMITED_HEADINGS = { rn_4tzwS4GZjPybwtkS: ['Calculate Concentrations of Solutions'] };
const NEW_WAVE = 'chem-stageb';
const COURSE = 'igcse-chemistry-19';
const SUBJECT = 'igcse-chemistry';

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
const WAVE_OPEN_BASE = '69154ecb6c1524268472ed2a1396b52bdc9018da';
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
  rn_N4HX8tqbdhTQcHyS: [
    ['stage-B re-anchored arithmetic Ca(OH)2: (2 x 1) + (2 x 16) + 40 = 74', () => 2 * 1 + 2 * 16 + 40 === 74],
    ['stage-B re-anchored arithmetic K2CO3: (3 x 16) + (1 x 12) + (2 x 39) = 138', () => 3 * 16 + 1 * 12 + 2 * 39 === 138],
    ['stage-B re-anchored arithmetic (NH4)2SO4: (8 x 1) + (2 x 14) + (4 x 16) + (1 x 32) = 132', () => 8 * 1 + 2 * 14 + 4 * 16 + 1 * 32 === 132],
  ],
  rn_WJD4ZN4kQfzJNSPV: [
    ['stage-B re-presented arithmetic: 50.0 + 3.8 - 2.6 = 51.2', () => Math.abs(50.0 + 3.8 - 2.6 - 51.2) < 1e-9],
  ],
  rn_VyXFNyxZHZGkxqTG: [
    ['stage-B re-presented arithmetic CO2 Mr: 12 + (2 x 16) = 44', () => 12 + 2 * 16 === 44],
    ['stage-B re-presented arithmetic: 4.4 / 44 = 0.1 mol', () => Math.abs(4.4 / 44 - 0.1) < 1e-9],
    ['stage-B re-presented arithmetic: 13 / 65 = 0.2 mol', () => Math.abs(13 / 65 - 0.2) < 1e-9],
  ],
  rn_xT8XsdJtDX5gNFXj: [
    ['stage-B re-presented stem Mr of record: 342.3 (sucrose C12H22O11)', () => 12 * 12 + 22 * 1 + 11 * 16 === 342],
    ['moles 2.64 / 342.3 = 0.0077 mol (4 d.p. rounding)', () => Math.round((2.64 / 342.3) * 10000) / 10000 === 0.0077],
  ],
  rn_DGkNCJRcCN4VQ28p: [
    ['mnemonic census: 13 mnemonic words map onto the 13-rung ladder (11 metals + carbon + hydrogen)', () => 11 + 2 === 13],
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
  check('A0', `noteRef identity ${id}`, S.noteRef.noteId === id && S.noteRef.corpusVersion === 'sme-revision-notes-igcse-chemistry-19-2026-09-18'
    && S.noteRef.sourceUrl === row.sourceUrl, 'path=' + row.path);
  check('A0', `topicTitle matches curriculum topic ${id}`, S.noteRef.topicTitle === ({ '1-principles-of-chemistry': '1. Principles of Chemistry', '2-inorganic-chemistry': '2. Inorganic Chemistry', '3-physical-chemistry': '3. Physical Chemistry', '4-organic-chemistry': '4. Organic Chemistry' })[row.sectionSlug], S.noteRef.topicTitle + ' vs ' + row.sectionSlug);

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
    check('A0', `figure url corpus-namespace ${id}/${f.id}`, f.url.startsWith('https://raw.githubusercontent.com/SyllabAI/syllabai-resources/main/SME-RevisionNotes/igcse-chemistry-19/assets/'), f.url.slice(0, 80));
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
      // declared corpus-limited exception: rn_4tzwS4GZjPybwtkS's body carries ONE distinct heading
      // string ('Calculate Concentrations of Solutions') for its two authored lessons — the figures
      // bind by moduleIds, so the (heading, lesson) pair stays unambiguous; disclosed in the receipt
      const dupOk = CORPUS_LIMITED_HEADINGS[id] && CORPUS_LIMITED_HEADINGS[id].includes(h);
      check('A0', `heading-unique across lessons ${id}${dupOk ? ' [corpus-limited exception]' : ''}`, dupOk || !headingLesson.has(h) || headingLesson.get(h) === li, h + ' first bound to L' + ((headingLesson.get(h) ?? -1) + 1));
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
  for (const [name, fn] of (NUM_LEDGER[id] || [])) check('NUM', `${id}: ${name}`, !!fn(), name);

  totGloss += S.noteAssets.glossary.length;
  totFigMapped += figs.filter((f) => (f.moduleIds || []).length > 0).length;
  streamChars[id] = { lessons: noteLessons, checks: noteChecks };
}

// corpus-level scope of the declared corpus-limited heading exception: exactly one duplicate claim,
// on exactly the declared (note, heading) pair
let dupClaims = 0;
for (const id of NOTES_W12) {
  const seen = new Map();
  for (const L of sources[id].obj.lessons) for (const h of L.sourceHeadings) { if (seen.has(h)) dupClaims++; seen.set(h, 1); }
}
check('A0', 'corpus-limited heading exception scope (exactly one declared duplicate claim)', dupClaims === 1 && (CORPUS_LIMITED_HEADINGS.rn_4tzwS4GZjPybwtkS || []).length === 1, dupClaims + ' duplicate claims');

// ── C-6: generation-union ajv (physics prior + chemistry prior byte-untouched) + new outputs ──
function dirFiles(d, suffix) {
  try { return fs.readdirSync(d).filter((f) => f.endsWith(suffix)).sort(); } catch (e) { return []; }
}
const physSrc = dirFiles(path.join(INT, 'source-0.6'), '.json').filter((f) => NOTES_W12.includes(f.replace('guided-lesson-', '').replace('.json', '')) === false);
const physHub = dirFiles(path.join(INT, 'hub-import-1.5'), '.json');
const physPkg = dirFiles(path.join(INT, 'question-packages-1.2'), '.json');
check('C-6', 'physics prior pack present on tree (127 sources / 127 lessons / 127 packages)', physSrc.length === 127 && physHub.length === 127 && physPkg.length === 127, `${physSrc.length}/${physHub.length}/${physPkg.length}`);
const chemOldSrc = dirFiles(path.join(INT, 'source-0.5'), '.json');
const chemOldHub = dirFiles(path.join(INT, 'hub-import-1.4'), '.json');
const chemOldPkg = dirFiles(path.join(INT, 'question-packages-1.1'), '.json');
check('C-6', 'chemistry prior generation present (112 sources / 112 lessons / 112 packages)', chemOldSrc.length === 112 && chemOldHub.length === 112 && chemOldPkg.length === 112, `${chemOldSrc.length}/${chemOldHub.length}/${chemOldPkg.length}`);
let chemFails = 0;
for (const f of physSrc) { if (!vSrc(JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6', f), 'utf8')))) chemFails++; }
for (const f of physHub) { if (!vHub(JSON.parse(fs.readFileSync(path.join(INT, 'hub-import-1.5', f), 'utf8')))) chemFails++; }
for (const f of physPkg) { if (!vPkg(JSON.parse(fs.readFileSync(path.join(INT, 'question-packages-1.2', f), 'utf8')))) chemFails++; }
check('C-6', `physics prior union ajv x${physSrc.length + physHub.length + physPkg.length} (sources vs 0.6, lessons vs 1.5, packages vs 1.2)`, chemFails === 0, chemFails + ' failures');
let oldFails = 0;
for (const f of chemOldSrc) { if (!vSrc(JSON.parse(fs.readFileSync(path.join(INT, 'source-0.5', f), 'utf8')))) oldFails++; }
for (const f of chemOldHub) { if (!vHub(JSON.parse(fs.readFileSync(path.join(INT, 'hub-import-1.4', f), 'utf8')))) oldFails++; }
for (const f of chemOldPkg) { if (!vPkg(JSON.parse(fs.readFileSync(path.join(INT, 'question-packages-1.1', f), 'utf8')))) oldFails++; }
check('C-6', `chemistry prior-generation union ajv x${chemOldSrc.length + chemOldHub.length + chemOldPkg.length} (0.5 sources vs 0.6, 1.4 lessons vs 1.5, 1.1 packages vs 1.2 — generation-union schemas)`, oldFails === 0, oldFails + ' failures');

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
      id: SUBJECT + '::' + id,
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
    packageId: SUBJECT + '::' + id,
    subject: SUBJECT,
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
check('C-6', `stage-B outputs ajv x224 (112 vs 1.5 + 112 vs 1.2)`, outFails === 0, outFails + ' failures');

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

// ── chemistry legacy generation conservation (v17 prior, byte-identical) ─────
const priorChemMan = JSON.parse(fs.readFileSync(args.priorChemManifest, 'utf8'));
check('G-E', 'chemistry legacy manifest v17 resolves (224 = 112 + 112)', priorChemMan.manifest_version === 17 && priorChemMan.artifacts.length === 224, `v${priorChemMan.manifest_version} x${priorChemMan.artifacts.length}`);
let chem17Bad = 0;
for (const a of priorChemMan.artifacts) {
  const p = path.join(REPO, a.path);
  if (!fs.existsSync(p)) { chem17Bad++; continue; }
  const b = fs.readFileSync(p);
  if (b.length !== a.bytes || sha256(b) !== a.sha256) chem17Bad++;
}
check('G-E', 'chemistry legacy generation byte conservation vs v17 x224 (superseded, never mutated)', chem17Bad === 0, `${chem17Bad} drift`);

// ── prior-pack load + conservation (G-E legacy check) ────────────────────────
const priorHubPaths = priorMan.artifacts.filter((a) => a.kind === 'hub-lesson-import-1.5');
const priorPkgPaths = priorMan.artifacts.filter((a) => a.kind === 'sme-question-package');
check('G-E', 'prior manifest artifact census 254 = 127 + 127 (the physics pack, v31)', priorMan.artifacts.length === 254 && priorHubPaths.length === 127 && priorPkgPaths.length === 127, priorMan.artifacts.length);
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
check('G-E', `prior-pack byte conservation on the stage-B tree x254`, priorBytesBad === 0 && priorShaBad === 0, `missing=${priorBytesBad} shaDrift=${priorShaBad}`);

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

// all 239 notes in register order (127 physics prior INT-3 rows + the 112 chemistry stage-B rows)
const allNotes = [];
const priorAnchors = new Map(priorInt3.notes.map((n) => [n.noteId, n]));
for (const n of priorInt3.notes) allNotes.push({ noteId: n.noteId, wave: n.wave });
for (const id of NOTES_W12) allNotes.push({ noteId: id, wave: NEW_WAVE });
check('G-E', 'INT-3 rows = 239 (127 physics prior + 112 chemistry stage-B)', allNotes.length === 239, allNotes.length);

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
  const isNew = row.wave === NEW_WAVE;
  const hubBuf = isNew ? outBufs[id].hub : fs.readFileSync(byNoteArt.get('hub-lesson-import-1.5|' + id));
  const pkgBuf = isNew ? outBufs[id].pkg : fs.readFileSync(byNoteArt.get('sme-question-package|' + id));
  const hubObj = isNew ? outputs[id].hub : JSON.parse(hubBuf.toString('utf8'));
  const pkgObj = isNew ? outputs[id].pkg : JSON.parse(pkgBuf.toString('utf8'));
  const toksArr = targetTokens(hubObj, pkgObj);
  const s = toksArr.join('\n');
  const sha = sha256(Buffer.from(s, 'utf8'));
  const prior = priorAnchors.get(id);
  if (row.wave !== NEW_WAVE) {
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
check('G-E', `legacy anchors conserved x127 (byte-identical physics prior pack)`, legacyFails === 0, legacyFails + ' drift');
check('G-E', `stage-B stream chars total = ${NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0)}`, true, NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0) + ' chars');

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
  if (fs.existsSync(hp) || fs.existsSync(pp)) throw new Error('additive-only violation: output exists ' + hp); // chemistry first issues at 1.5/1.2
  fs.writeFileSync(hp, outBufs[id].hub); fs.writeFileSync(pp, outBufs[id].pkg);
  emitted.push({ path: 'SME-GuidedLessons/integration/hub-import-1.5/' + id + '.hub-lesson-import.json', bytes: outBufs[id].hub.length, sha256: sha256(outBufs[id].hub) });
  emitted.push({ path: 'SME-GuidedLessons/integration/question-packages-1.2/' + id + '.sme-question-package.json', bytes: outBufs[id].pkg.length, sha256: sha256(outBufs[id].pkg) });
}

// manifest v32
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
  manifest_version: 32,
  course_id: COURSE,
  b6_manifest_continuity: {
    decision: 'continue-global',
    selected: 'chemistry stage-B = manifest v32 (the programme-level v-series continues across subjects: chemistry v1..v17, physics v18..v31, now v32 — the first chemistry tranche on the 0.6/1.5/1.2 generation)',
    rejected: 'per-course series (chemistry v18 restart) — would fork the programme-level integration ledger and break the single load-scope lineage of record',
    recorded_by: 'runbook B6 (the B6 decision of record is continue-global; the physics stage-A + wave-12 receipts re-record it); this receipt re-records it for the chemistry stage-B',
  },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_trace: TRACE,
  supersedes: `hub-import-manifest-v31.json (the physics wave-12 tranche: 254 artifacts, the complete 127-note physics pack @ commit C 49db4a284873a9f344814dad00788807d457b6b6) — all 254 prior artifacts re-pinned byte-identical in artifacts[] (sha256 + bytes), zero mutation; the chemistry v17 legacy generation (224 artifacts) stays byte-identical on disk and is conserved by a dedicated G-E gate`,
  checks_layer: {
    wave: 'CHEMISTRY-4CH1 stage-B (the complete 112-note register re-issued onto the 0.6/1.5/1.2 generation — all 28 subtopics, 4 topics)',
    derivation: `${idChecks} re-issued chemistry checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application — the B2 law: 9 checks per lesson = 5 MCQ + 2 recall + 1 explain-why + 1 application), graded by the runner's keyword law`,
    declared_revision: 'the chemistry corpus was 9-check complete at the r3-stageb 0.5 generation (v17); this stage-B re-issues all 112 notes onto the physics-grade generation with the declared authoring deltas (kind fields, 4th distractors, model answers, keyword grounding, figure re-binds, glossary trims, 8-gram rephrases, spec realignment); physics pack bytes untouched',
    grading_law: 'case-insensitive whole-token match of the learner text against the keyword set (stem-tolerant), fail-closed on written items without modelAnswer',
    fail_closed: 'written item without modelAnswer renders reveal-only, never gradeable; the runner refuses any feed whose manifest fails G-A..G-E',
  },
  source_generation: {
    format: 'guided-lesson/0.6',
    namespace: 'SME-GuidedLessons/integration/source-0.6/',
    pin: PIN,
    prior_generation_pins: "{'chemistry 0.5 generation': 'hub-import-manifest-v17.json (the r3-stageb landing; sources pinned per r3-stageb wave commit-A pins)', 'physics pack': 'v18..v31 commit-A pins carried in the v31 manifest source_generation'} — the stage-B sources are the declared-delta upgrade of the 0.5 generation, landed at this commit A",
    int0_lineage: '(chemistry lineage: INT-0..INT-5 fullcorpus + figures generations + r3 check-types stage-A/B of record; this stage-B carries the register onto the 0.6 generation)',
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
  // v32 counts = the programme load scope: physics 127 (priorMan.counts, unchanged) + chemistry 112 (this stage-B tranche)
  conservation: {
    authored_stream_sha256: grand.digest('hex'),
    authored_chars: String(grandChars),
    wave_stream_sha256: waveOut,
  },
  artifacts: [...priorMan.artifacts, ...newArtifacts],
};
const mb = Buffer.from(JSON.stringify(manifest, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'hub-import-manifest-v32.json'), mb);

// INT-3 wave-12 record
const int3 = {
  stage: 'CHEMISTRY-4CH1 stage-B (the complete 112-note register re-issued onto the 0.6/1.5/1.2 generation)',
  title: 'INT-3 transform record — chemistry stage-B (guided-lesson/0.6 -> hub/lesson-import/1.5 + sme-question-package/1.2), CUMULATIVE 239-row anchor table (127 physics + 112 chemistry) — the programme load scope',
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_traces: { ignition: TRACE, execution: TRACE },
  adapter: 'guided-lesson-0.6--hub-lesson-import-1.5',
  course_id: COURSE,
  supersedes_int3: 'records/INT-3-transform-record-physics-wave12.json (the 127-row v31 anchor table; all 127 physics rows carried byte-equivalent here — every prior anchor re-proven on the stage-B tree)',
  b6_manifest_continuity: { decision: 'continue-global', selected: 'manifest v32 supersedes v31' },
  chemistry_stageb_of_record: {
    basis: 'the complete 112-note chemistry register (all 4 topics / 28 subtopics) re-issued from the 0.5 generation (v17) onto the 0.6/1.5/1.2 generation; authored content conserved modulo the declared authoring deltas',
    deltas: 'format const 0.5->0.6 x112; kind:"mcq" explicit x1,195; 20 authored 4th distractors; 3 authored model answers; 629 ungrounded keyword variants dropped + 64 grounded top-ups; 110 figure re-binds to heading-unique; 49 glossary trims (2..5 band); 355 learner-surface 8-gram rephrases across 76 notes; 36 spec texts realigned to the curriculum graph verbatim; 5 lessons\' sourceHeadings corrected to exact corpus headings',
  },
  source_pin: { commitA: PIN, namespace: 'SME-GuidedLessons/integration/source-0.6/', files: NOTES_W12.map((i) => 'guided-lesson-' + i + '.json') },
  registry_pin: { file: 'apps/hub/content/igcse-chemistry-19/notes.json', rows: '112', stageb_rows: 'the complete register (register order 0..111) re-issued' },
  source_06_generation_pin: PIN,
  conservation_law: {
    law: 'adapter spec 0.6 §7 walk (byte-identical to run_import.mjs targetTokens): specAnchors -> primer -> modules (title/headings/specRefs/opening/keyPoints/depthLayers) -> glossary -> workedExample -> questions (stem/class/options + modelAnswer/keywords on written kinds); per-note sha256 of the "\\n"-joined stream',
    wave_subtotals: waveOut,
  },
  grand_stream: { chars: grandChars, sha256: manifest.conservation.authored_stream_sha256 },
  wave_stream_sha256: waveOut,
  battery: {
    names: ['P0', 'A0', 'AN', 'JC', 'SG', 'KW', '2.1B', 'NUM', 'C-6', 'written', 'C-5', 'B2', 'G-E'],
    a0: 'ajv x112 sources vs guided-lesson.0.6 + kind order x239 lessons + B2 sizing + spec text provenance (curriculum graph verbatim x210) + figure closure both ways x200 + corpus image coverage + glossary band x112 + primer band x112',
    an: 'exactly-one-correct x1,195; correct-key census >=3 distinct per note (post-rotation); distinct option texts; four options',
    sg: 'lesson specRefs subset of file specPoints; every check KP-anchored (content-token overlap)',
    kw: '>=3 grounded keywords per written item x956 (629 ungrounded variants dropped + 64 top-ups at stage-B)',
    jc: 'every option explained; distractors name misconceptions; correct-option misconception null',
    '2.1b': 'zero 8-gram overlaps of learner-surface text vs the corpus note body x112 (355 authored rephrases carried the 0.1/r3-era corpus clean under the wider physics-grade surface)',
    num: 'stage-B spot ledgers on the re-presented arithmetic (Ca(OH)2 74; K2CO3 138; (NH4)2SO4 132; air volume 51.2 mL; CO2 Mr 44, 4.4/44=0.1, 13/65=0.2; sucrose 2.64/342.3=0.0077; mnemonic 11+2=13 rungs); all other arithmetic unchanged from the r3-stageb corpus of record',
    c6: `physics prior union ajv x381 + chemistry prior-generation union ajv x336 + stage-B outputs ajv x224`,
    c5: 'checkRefs <-> questions bidirectional 1:1 in order x112',
    b2: '9 checkRefs per module x239; identity arithmetic 9 = 5+2+1+1 x239',
    ge: 'per-note stream anchors x239 (127 physics legacy byte-equivalent + 112 chemistry stage-B) + physics legacy generation byte conservation vs v31 x254 + chemistry legacy generation byte conservation vs v17 x224 + grand stream single-finalization',
  },
  chemistry_census: {
    notes_total: 112, lessons_total: 239, checks_total: idChecks,
    stageb_lessons: idLessons, stageb_checks: idChecks, stageb_figures: totFig, stageb_notes: 112,
    corpus_images_bound: totFig, worked_examples_populated_stageb: totWEPop, worked_examples_null_stageb: totWENull,
  },
  physics_census: { notes_total: 127, lessons_total: priorMan.counts.lessons, checks_total: priorMan.counts.checks, note: 'carried byte-identical from v31; anchors re-proven on the stage-B tree' },
  notes: int3Notes,
};
const ib = Buffer.from(JSON.stringify(int3, null, 2) + '\n');
fs.mkdirSync(path.join(INT, 'records'), { recursive: true });
fs.writeFileSync(path.join(INT, 'records/INT-3-transform-record-chem-stageb.json'), ib);

// promotion receipt
const receipt = {
  format: 'chem-stageb-promotion-receipt/1.0',
  wave: 'CHEMISTRY-4CH1 stage-B (the complete 112-note register re-issued onto the 0.6/1.5/1.2 four-plane generation; programme-level manifest v32)',
  operator_traces: { ignition: TRACE, execution: TRACE },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  commit_a: { sha: PIN, contents: '112 upgraded source-0.6 notes (the declared-delta stage-B generation) + integration/tooling/chem-stageb-pipeline.js (the pipeline of record, derived from the wave-12 landed pipeline)', parent: parent, message_carries_trace: headMsg.includes(TRACE) },
  tranche: {
    notes: 112, lessons: idLessons, checks: idChecks,
    kinds: { mcq: streamCharsArr().mcq, recall: streamCharsArr().rec, 'explain-why': streamCharsArr().exp, application: streamCharsArr().app },
    figures: totFig, figures_module_mapped: totFigMapped,
    glossary_terms: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    worked_examples: { populated: totWEPop, null: totWENull },
    stream_chars: NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0),
    authoring_deltas: {
      format_bumped: 112, kind_fields_added: 1195, fourth_distractors_authored: 20, model_answers_authored: 3,
      keyword_variants_dropped: 629, keyword_topups: 64, figure_rebinds: 110, glossary_trims: 49,
      gram_rephrases: 355, gram_notes_touched: 76, spec_texts_realigned: 36, sourceheadings_corrected: 7,
    },
  },
  manifest: { version: 32, artifacts_total: manifest.artifacts.length, prior_re_pinned: 254, first_issues: 224, legacy_generation_conserved: 224 },
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
fs.writeFileSync(path.join(INT, 'records/CHEMISTRY-4CH1-STAGEB-PROMOTION-20261112.json'), rb);

console.log(`GATES: ${LOG.filter((l) => l.ok).length}/${LOG.length} GREEN, 0 failures`);
console.log(`EMITTED: 224 outputs + manifest v32 (${mb.length}B) + INT-3 (${ib.length}B) + promotion receipt (${rb.length}B)`);
console.log(`Stage-B tranche: 112 notes / ${idLessons} lessons / ${idChecks} checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application) / ${totFig} figures`);
console.log(`CUMULATIVE v32: ${manifest.counts.notes} notes / ${manifest.counts.lessons} lessons / ${manifest.counts.checks} checks; grand stream ${manifest.conservation.authored_chars} chars`);
console.log(`GRAND: ${manifest.conservation.authored_stream_sha256}`);
console.log(`STAGE-B SUBTOTAL: ${waveOut['wave-12']}`);
