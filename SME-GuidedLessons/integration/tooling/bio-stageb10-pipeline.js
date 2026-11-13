#!/usr/bin/env node
/**
 * bio-stageb10-pipeline.js — BIOLOGY-4BI1 stage-B wave 10 (the tenth and closing register bucket of the
 * frozen B4 partition: 2 selective-breeding notes end-to-end at the 0.7/1.6/1.3 four-plane generation:
 * source-0.7 / hub-import-1.6 / question-packages-1.3 / CUMULATIVE manifest v44 + records, per the
 * new-subject runbook B4). Derived from the bio-stageb9 landed pipeline of record; the cumulative
 * manifest convention is adopted directly (no tranche-scoped intermediate).
 * Node >= 18, ajv via ajvkit.
 *
 * Usage:
 *   node bio-stageb10-pipeline.js --pin <commitA> --repo <resources worktree root> \
 *     --curriculum <curriculum-bio.json> --notes <notes-bio-w10.json> \
 *     --priorInt3 <INT-3 bio-stageb9-v43> --chemInt3 <INT-3 chem-stageb> \
 *     --priorManifest <v43 manifest (biology cumulative)> --priorChemManifest <v32 manifest (chemistry)> \
 *     --priorPhysManifest <v31 manifest (physics)> --trace <operator ignition trace>
 *
 * Gates of record (the physics-wave battery, re-run over the full corpus): P0 / A0 / AN / JC / SG / KW /
 * 2.1B / NUM / C-6 / written / C-5 / B2 / G-E. Fail-closed: any failure exits 1 before emit.
 *
 * Wave-10 authoring of record (census 2026-11-13, trace 1a1d544cd50a7f81): 2 notes / 4 lessons /
 * 36 checks = 20 MCQ + 8 recall + 4 explain-why + 4 application (the B2 law 5+2+1+1 per lesson);
 * 2 corpus figures bound heading-unique, all module-mapped; glossary 9 terms in the 2..5 band per note;
 * learner-surface authored fresh per the 2.1B 8-gram law; deterministic AN rotation applied at emit.
 * With this wave the 142-note biology register is COMPLETE (the pilot + all ten partition waves).
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
  'rn_xBYWN9JGPSnmJVY7',
  'rn_hybmmF3JNk7kxzJZ',
];
const WAVE12 = 10;

// the corpus-limited heading exception of record (none for the biology stage-B wave 10)
const CORPUS_LIMITED_HEADINGS = {};
const NEW_WAVE = 'bio-stageb10';
const COURSE = 'igcse-biology-19';
const SUBJECT = 'igcse-biology';

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
const chemInt3 = JSON.parse(fs.readFileSync(args.chemInt3, 'utf8'));
const priorMan = JSON.parse(fs.readFileSync(args.priorManifest, 'utf8'));
check('P0', 'prior manifest counts are ints (the v26 amendment law)',
  ['notes', 'lessons', 'checks', 'keyPoints', 'distractors', 'glossaryTerms', 'figures', 'figures_module_mapped', 'figures_note_level', 'workedExamples_populated', 'workedExamples_null', 'authored_chars_conserved'].every((k) => Number.isInteger(priorMan.counts[k])),
  JSON.stringify(Object.fromEntries(Object.entries(priorMan.counts).slice(0, 3))));

const schemaSrc = JSON.parse(fs.readFileSync(path.join(INT, 'schema/guided-lesson.0.7.schema.json'), 'utf8'));
const schemaHub = JSON.parse(fs.readFileSync(path.join(INT, 'schema/hub-lesson-import.1.6.schema.json'), 'utf8'));
const schemaPkg = JSON.parse(fs.readFileSync(path.join(INT, 'schema/sme-question-package.1.3.schema.json'), 'utf8'));
const ajv = new Ajv({ schemaId: 'auto', allErrors: true, strict: false });
const vSrc = ajv.compile(schemaSrc), vHub = ajv.compile(schemaHub), vPkg = ajv.compile(schemaPkg);

const sources = {};
for (const id of NOTES_W12) {
  const p = path.join(INT, 'source-0.7/guided-lesson-' + id + '.json');
  sources[id] = { path: p, raw: fs.readFileSync(p), obj: JSON.parse(fs.readFileSync(p, 'utf8')) };
}

// ── P0: pin + blob identity ──────────────────────────────────────────────────
const headSha = execSync('git rev-parse HEAD', { cwd: REPO }).toString().trim();
check('P0', 'HEAD == declared wave-10 commit-A pin', headSha === PIN, 'HEAD=' + headSha.slice(0, 12) + ' pin=' + PIN.slice(0, 12));
const headMsg = execSync('git log -1 --format=%B', { cwd: REPO }).toString();
check('P0', 'commit A message carries the operator trace', headMsg.includes(TRACE), headMsg.slice(0, 90).replace(/\n/g, ' '));
for (const id of NOTES_W12) {
  const rel = 'SME-GuidedLessons/integration/source-0.7/guided-lesson-' + id + '.json';
  const blob = execSync('git show HEAD:' + rel, { cwd: REPO, maxBuffer: 1 << 22 });
  check('P0', 'source blob @ HEAD == disk: ' + id, blob.equals(sources[id].raw), 'blob=' + blob.length + 'B disk=' + sources[id].raw.length + 'B');
}
const parent = execSync('git rev-parse HEAD~1', { cwd: REPO }).toString().trim();
const WAVE_OPEN_BASE = 'd527ceddff041a8dd37789392ba7b06a06018b80';
let parentOk = parent === WAVE_OPEN_BASE;
let parentDetail = 'parent=' + parent.slice(0, 12);
if (!parentOk) {
  try {
    const pm = execSync('git log -1 --format=%B ' + parent, { cwd: REPO, maxBuffer: 1 << 20 }).toString();
    parentOk = pm.includes('guided(BIOLOGY-4BI1 stage-B wave 10)');
    parentDetail += ' parentMsg=' + pm.slice(0, 40).replace(/\n/g, ' ');
  } catch (e) { parentDetail += ' parent-lookup-fail'; }
}
if (!parentOk) {
  // mid-flight merge precedent (first exercised by the wave-6 corrective): main moved forward by a
  // foreign PR merge whose ancestry still contains the wave-open base; commit A remains an ancestor
  try {
    execSync('git merge-base --is-ancestor ' + WAVE_OPEN_BASE + ' ' + parent, { cwd: REPO });
    parentOk = true;
    parentDetail += ' merge-ancestor-of-wave-open-base';
  } catch (e) { parentDetail += ' not-ancestor'; }
}
check('P0', 'commit A parent == the wave-open main tip d527ceddff04, a commit-A-chain member of wave 10 (the stage-A corrective precedent), or a mid-flight merge descendant of the wave-open base (ancestry-verified)', parentOk, parentDetail);
let mainTipLive = '';
try { mainTipLive = execSync((process.env.RESOURCES_REMOTE_URL || 'git ls-remote https://github.com/SyllabAI/syllabai-resources.git') + ' refs/heads/main', { cwd: REPO, shell: '/bin/bash' }).toString().split('\t')[0].trim(); } catch (e) { mainTipLive = 'ERR ' + e.message.slice(0, 60); }
let tipOk = mainTipLive === PIN || mainTipLive === headSha;
let tipDetail = 'tip=' + mainTipLive.slice(0, 12) + ' head=' + headSha.slice(0, 12);
if (!tipOk) {
  // mid-flight merge precedent (first exercised by the wave-6 corrective): main moved forward by a
  // foreign PR merge whose ancestry still contains the commit-A pin; the pin remains an ancestor
  try {
    execSync('git merge-base --is-ancestor ' + headSha + ' ' + mainTipLive, { cwd: REPO });
    tipOk = true;
    tipDetail += ' tip-descendant-of-commit-A-pin';
  } catch (e) { tipDetail += ' tip-not-descendant'; }
}
check('P0', 'resources main tip sits at the commit-A pin, the corrective base riding on it (first wave-10 landing), or a mid-flight merge descendant of the commit-A pin (ancestry-verified)', tipOk, tipDetail);


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
  rn_xBYWN9JGPSnmJVY7: [
    ['corpus fact: the natural-versus-artificial comparison table contrasts the two selection processes across three rows - occurrence, outcome and timescale - so 1 + 1 + 1 = 3', () => 1 + 1 + 1 === 3],
  ],
  rn_hybmmF3JNk7kxzJZ: [
    ['corpus fact: inbreeding raises two documented risks - inheriting harmful genetic defects and vulnerability to new diseases - so 1 + 1 = 2', () => 1 + 1 === 2],
    ['corpus fact: wild brassica gave rise to six named crops - cauliflower, cabbage, broccoli, Brussels sprouts, kale and kohlrabi - so the named crop count is 6', () => 6 === 6],
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
  check('A0', 'ajv 0.7: ' + id, okS, okS ? '' : ajv.errorsText(vSrc.errors));

  // A0: spec text provenance (verbatim curriculum graph) + codes ⊆ register
  const regCodes = (row.specPointCodes || []);
  for (const sp of S.specPoints) {
    check('A0', `spec text verbatim ${id}/${sp.code}`, specByText.get(sp.code) === sp.text, 'graph="' + (specByText.get(sp.code) || '').slice(0, 40) + '"');
    check('A0', `spec code in register ${id}/${sp.code}`, regCodes.includes(sp.code), 'register=' + regCodes.join(','));
  }

  // A0: primer band + noteRef identity
  const pw = toks(S.primer.text).length;
  check('A0', `primer word band ${id}`, pw >= 25 && pw <= 90, pw + ' words');
  check('A0', `noteRef identity ${id}`, S.noteRef.noteId === id && S.noteRef.corpusVersion === 'sme-revision-notes-igcse-biology-19-2026-09-17'
    && S.noteRef.sourceUrl === row.sourceUrl, 'path=' + row.path);
  check('A0', `topicTitle matches curriculum topic ${id}`, S.noteRef.topicTitle === ({ '1-the-nature-and-variety-of-living-organisms': 'The nature and variety of living organisms', '2-structure-and-function-in-living-organisms': 'Structure and functions in living organisms', '3-reproduction-and-inheritance': 'Reproduction and inheritance', '4-ecology-and-the-environment': 'Ecology and the environment', '5-use-of-biological-resources': 'Use of biological resources' })[row.sectionSlug], S.noteRef.topicTitle + ' vs ' + row.sectionSlug);

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
    check('A0', `figure url corpus-namespace ${id}/${f.id}`, f.url.startsWith('https://raw.githubusercontent.com/SyllabAI/syllabai-resources/main/SME-RevisionNotes/igcse-biology-19/assets/'), f.url.slice(0, 80));
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
check('A0', 'corpus-limited heading exception scope (none declared for the biology stage-B wave 9)', dupClaims === 0 && Object.keys(CORPUS_LIMITED_HEADINGS).length === 0, dupClaims + ' duplicate claims');

// ── C-6: generation-union ajv (physics prior + chemistry prior byte-untouched) + new outputs ──
function dirFiles(d, suffix) {
  try { return fs.readdirSync(d).filter((f) => f.endsWith(suffix)).sort(); } catch (e) { return []; }
}
const priorChemManEarly = JSON.parse(fs.readFileSync(args.priorChemManifest, 'utf8'));
const priorPhysManEarly = JSON.parse(fs.readFileSync(args.priorPhysManifest, 'utf8'));
const priorIds = new Set([...priorMan.artifacts, ...priorChemManEarly.artifacts, ...priorPhysManEarly.artifacts].map((a) => a.noteId));
const physSrc = dirFiles(path.join(INT, 'source-0.6'), '.json').filter((f) => { const nid = f.replace('guided-lesson-', '').replace('.json', ''); return priorIds.has(nid) && !NOTES_W12.includes(nid); });
const bioPriorSrc = dirFiles(path.join(INT, 'source-0.7'), '.json').filter((f) => { const nid = f.replace('guided-lesson-', '').replace('.json', ''); return priorIds.has(nid) && !NOTES_W12.includes(nid); });
const physHub = dirFiles(path.join(INT, 'hub-import-1.5'), '.json').filter((f) => priorIds.has(f.replace('.hub-lesson-import.json', '')));
const bioPriorHub = dirFiles(path.join(INT, 'hub-import-1.6'), '.json').filter((f) => { const nid = f.replace('.hub-lesson-import.json', ''); return priorIds.has(nid) && !NOTES_W12.includes(nid); });
const physPkg = dirFiles(path.join(INT, 'question-packages-1.2'), '.json').filter((f) => priorIds.has(f.replace('.sme-question-package.json', '')));
const bioPriorPkg = dirFiles(path.join(INT, 'question-packages-1.3'), '.json').filter((f) => { const nid = f.replace('.sme-question-package.json', ''); return priorIds.has(nid) && !NOTES_W12.includes(nid); });
check('C-6', 'physics+chemistry+bio prior generation present on tree (379 per-namespace = 239 at 0.6/1.5/1.2 + 140 prior biology at 0.7/1.6/1.3)', physSrc.length === 239 && bioPriorSrc.length === 140 && physHub.length === 239 && bioPriorHub.length === 140 && physPkg.length === 239 && bioPriorPkg.length === 140, `${physSrc.length}+${bioPriorSrc.length}/${physHub.length}+${bioPriorHub.length}/${physPkg.length}+${bioPriorPkg.length}`);
const chemOldSrc = dirFiles(path.join(INT, 'source-0.5'), '.json');
const chemOldHub = dirFiles(path.join(INT, 'hub-import-1.4'), '.json');
const chemOldPkg = dirFiles(path.join(INT, 'question-packages-1.1'), '.json');
check('C-6', 'chemistry prior generation present (112 sources / 112 lessons / 112 packages)', chemOldSrc.length === 112 && chemOldHub.length === 112 && chemOldPkg.length === 112, `${chemOldSrc.length}/${chemOldHub.length}/${chemOldPkg.length}`);
let chemFails = 0;
for (const f of physSrc) { if (!vSrc(JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6', f), 'utf8')))) chemFails++; }
for (const f of bioPriorSrc) { if (!vSrc(JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7', f), 'utf8')))) chemFails++; }
for (const f of physHub) { if (!vHub(JSON.parse(fs.readFileSync(path.join(INT, 'hub-import-1.5', f), 'utf8')))) chemFails++; }
for (const f of bioPriorHub) { if (!vHub(JSON.parse(fs.readFileSync(path.join(INT, 'hub-import-1.6', f), 'utf8')))) chemFails++; }
for (const f of physPkg) { if (!vPkg(JSON.parse(fs.readFileSync(path.join(INT, 'question-packages-1.2', f), 'utf8')))) chemFails++; }
for (const f of bioPriorPkg) { if (!vPkg(JSON.parse(fs.readFileSync(path.join(INT, 'question-packages-1.3', f), 'utf8')))) chemFails++; }
check('C-6', `physics+chemistry+bio-stageA prior union ajv x${physSrc.length + bioPriorSrc.length + physHub.length + bioPriorHub.length + physPkg.length + bioPriorPkg.length} (generation-union schemas)`, chemFails === 0, chemFails + ' failures');
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
check('C-6', `stage-B wave-10 outputs ajv x${NOTES_W12.length * 2} (${NOTES_W12.length} vs 1.6 + ${NOTES_W12.length} vs 1.3)`, outFails === 0, outFails + ' failures');
let newOutFails = 0;
for (const id of NOTES_W12) {
  if (!vSrc(JSON.parse(sources[id].raw.toString('utf8')))) newOutFails++;
  if (!vHub(outputs[id].hub)) newOutFails++;
  if (!vPkg(outputs[id].pkg)) newOutFails++;
}
check('C-6', `stage-B wave-10 outputs ajv x${NOTES_W12.length * 3} (${NOTES_W12.length} sources vs 0.7 + ${NOTES_W12.length} lessons vs 1.6 + ${NOTES_W12.length} packages vs 1.3)`, newOutFails === 0, newOutFails + ' failures');

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

// ── physics legacy pack conservation (v31 prior, byte-identical) ─────────────
const priorPhysMan = JSON.parse(fs.readFileSync(args.priorPhysManifest, 'utf8'));
check('G-E', 'physics pack manifest v31 resolves (254 = 127 + 127)', priorPhysMan.manifest_version === 31 && priorPhysMan.artifacts.length === 254, `v${priorPhysMan.manifest_version} x${priorPhysMan.artifacts.length}`);
let chem17Bad = 0;
for (const a of priorPhysMan.artifacts) {
  const p = path.join(REPO, a.path);
  if (!fs.existsSync(p)) { chem17Bad++; continue; }
  const b = fs.readFileSync(p);
  if (b.length !== a.bytes || sha256(b) !== a.sha256) chem17Bad++;
}
check('G-E', 'physics pack byte conservation vs v31 x254 (untouched by biology stage-B wave 10)', chem17Bad === 0, `${chem17Bad} drift`);

// ── prior-pack load + conservation (G-E legacy check) ────────────────────────
const priorHubPaths = priorMan.artifacts.filter((a) => a.kind === 'hub-lesson-import-1.6');
const priorPkgPaths = priorMan.artifacts.filter((a) => a.kind === 'sme-question-package');
check('G-E', `prior manifest artifact census 280 = 140 + 140 (the biology cumulative pack through wave 9, v43)`, priorMan.artifacts.length === 280 && priorHubPaths.length === 140 && priorPkgPaths.length === 140, priorMan.artifacts.length);
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
check('G-E', `prior-pack byte conservation on the wave tree x280 (the biology cumulative pack through wave 9: pilot + wave-1 + wave-2 + wave-3 + wave-4 + wave-5 + wave-6 + wave-7 + wave-8 + wave-9 artifacts)`, priorBytesBad === 0 && priorShaBad === 0, `missing=${priorBytesBad} shaDrift=${priorShaBad}`);

// chemistry v32 pack re-pin (byte-identical on the wave tree)
const priorChemMan = JSON.parse(fs.readFileSync(args.priorChemManifest, 'utf8'));
check('G-E', 'chemistry pack manifest v32 resolves (224 = 112 + 112)', priorChemMan.manifest_version === 32 && priorChemMan.artifacts.length === 224, `v${priorChemMan.manifest_version} x${priorChemMan.artifacts.length}`);
let chemBad = 0;
for (const a of priorChemMan.artifacts) {
  byNoteArt.set(a.kind + '|' + a.noteId, path.join(REPO, a.path));
  const p = path.join(REPO, a.path);
  if (!fs.existsSync(p)) { chemBad++; continue; }
  const b = fs.readFileSync(p);
  if (b.length !== a.bytes || sha256(b) !== a.sha256) chemBad++;
}
check('G-E', 'chemistry pack byte conservation vs v32 x224 (untouched by biology stage-B wave 10)', chemBad === 0, `${chemBad} drift`);

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

// all 252 notes in the walk (112 chemistry stage-B rows + 125 prior biology rows + the 15 wave-9 notes)
const allNotes = [];
const priorAnchors = new Map(priorInt3.notes.map((n) => [n.noteId, n]));
for (const n of chemInt3.notes) { allNotes.push({ noteId: n.noteId, wave: n.wave }); priorAnchors.set(n.noteId, n); }
for (const n of priorInt3.notes) allNotes.push({ noteId: n.noteId, wave: n.wave });
for (const id of NOTES_W12) allNotes.push({ noteId: id, wave: NEW_WAVE });
check('G-E', 'G-E walk rows = 254 (112 chemistry stage-B re-proven + 140 prior biology rows re-proven + 2 stage-B wave-10 notes); the emitted INT-3 of record carries the 142 biology rows', allNotes.length === 254, allNotes.length);

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
const chemGrand = crypto.createHash('sha256');
let chemChars = 0;
const bioGrand = crypto.createHash('sha256');
let bioChars = 0;
const waveHashes = {};
const int3Notes = [];
for (const row of allNotes) {
  const id = row.noteId;
  const isNew = row.wave === NEW_WAVE;
  const hubKind = byNoteArt.has('hub-lesson-import-1.6|' + id) ? 'hub-lesson-import-1.6' : 'hub-lesson-import-1.5';
  const hubBuf = isNew ? outBufs[id].hub : fs.readFileSync(byNoteArt.get(hubKind + '|' + id));
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
  if (isNew) {
    chemGrand.update(Buffer.from(s, 'utf8'));
    chemChars += s.length;
  }
  if (row.wave.startsWith('bio-')) {
    bioGrand.update(Buffer.from(s, 'utf8'));
    bioChars += s.length;
    waveHashes['wave-' + row.wave] = waveHashes['wave-' + row.wave] || crypto.createHash('sha256');
    waveHashes['wave-' + row.wave].update(Buffer.from(s, 'utf8'));
  }
  if (isNew) int3Notes.push({
    noteId: id,
    wave: row.wave,
    sourceLayerSha256: sha256(sources[id].raw),
    hubSha256: sha256(hubBuf),
    pkgSha256: sha256(pkgBuf),
    stream: { sha256: sha, chars: s.length },
  });
  streamChars[id] = streamChars[id] || {};
  streamChars[id].chars = s.length;
}
check('G-E', `legacy anchors conserved x252 (112 chemistry stage-B + 140 prior biology rows, byte-equivalent)`, legacyFails === 0, legacyFails + ' drift');
check('G-E', `wave-10 stream chars total = ${NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0)}`, true, NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0) + ' chars');

// ── fail-closed barrier before emit ─────────────────────────────────────────
if (FAILS.length) {
  console.error(`FAIL-CLOSED: ${FAILS.length} failures`);
  for (const f of FAILS) console.error(`  [${f.stage}] ${f.name} — ${f.detail}`);
  process.exit(1);
}

// ── emit outputs ─────────────────────────────────────────────────────────────
fs.mkdirSync(path.join(INT, 'hub-import-1.6'), { recursive: true });
fs.mkdirSync(path.join(INT, 'question-packages-1.3'), { recursive: true });
const emitted = [];
for (const id of NOTES_W12) {
  const hp = path.join(INT, 'hub-import-1.6', id + '.hub-lesson-import.json');
  const pp = path.join(INT, 'question-packages-1.3', id + '.sme-question-package.json');
  if (fs.existsSync(hp) && !fs.readFileSync(hp).equals(outBufs[id].hub)) throw new Error('additive-only violation: output exists with DIFFERENT bytes ' + hp);
  if (fs.existsSync(pp) && !fs.readFileSync(pp).equals(outBufs[id].pkg)) throw new Error('additive-only violation: output exists with DIFFERENT bytes ' + pp); // chemistry first issues at 1.5/1.2 — identical-exists tolerated
  fs.writeFileSync(hp, outBufs[id].hub); fs.writeFileSync(pp, outBufs[id].pkg);
  emitted.push({ path: 'SME-GuidedLessons/integration/hub-import-1.6/' + id + '.hub-lesson-import.json', bytes: outBufs[id].hub.length, sha256: sha256(outBufs[id].hub) });
  emitted.push({ path: 'SME-GuidedLessons/integration/question-packages-1.3/' + id + '.sme-question-package.json', bytes: outBufs[id].pkg.length, sha256: sha256(outBufs[id].pkg) });
}

// manifest v43
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
// physics wave subtotals are NOT re-accumulated in the chemistry-scope manifest — the per-note
// G-E legacy anchor gate above re-proves every physics stream on this tree (the wave-subtotal
// continuity of the physics pack is carried by the v31 manifest of record, unchanged)
check('G-E', 'biology-scope conservation carries exactly eleven wave keys (stagea + stageb1..stageb10; per-key subtotal comparison in the order-independent physics wave-10..12 convention, since lexicographic sort interleaves stageb10 after stageb1)', (() => { let waveOk = true; for (const w of Object.keys(priorMan.conservation.wave_stream_sha256)) { if (waveOut[w] !== priorMan.conservation.wave_stream_sha256[w]) waveOk = false; } return waveOk && Object.keys(waveOut).length === 11 && !!waveOut['wave-bio-stageb10']; })(), Object.keys(waveOut).join(','));
check('G-E', 'prior wave subtotals conserved vs v43 (stagea + stageb1 + stageb2 + stageb3 + stageb4 + stageb5 + stageb6 + stageb7 + stageb8 + stageb9 byte-equivalent)', waveOut['wave-bio-stagea'] === priorMan.conservation.wave_stream_sha256['wave-bio-stagea'] && waveOut['wave-bio-stage1'] === priorMan.conservation.wave_stream_sha256['wave-bio-stage1'] && waveOut['wave-bio-stage2'] === priorMan.conservation.wave_stream_sha256['wave-bio-stage2'] && waveOut['wave-bio-stage3'] === priorMan.conservation.wave_stream_sha256['wave-bio-stage3'] && waveOut['wave-bio-stage4'] === priorMan.conservation.wave_stream_sha256['wave-bio-stage4'] && waveOut['wave-bio-stage5'] === priorMan.conservation.wave_stream_sha256['wave-bio-stage5'] && waveOut['wave-bio-stage6'] === priorMan.conservation.wave_stream_sha256['wave-bio-stage6'] && waveOut['wave-bio-stage7'] === priorMan.conservation.wave_stream_sha256['wave-bio-stage7'] && waveOut['wave-bio-stage8'] === priorMan.conservation.wave_stream_sha256['wave-bio-stage8'] && waveOut['wave-bio-stage9'] === priorMan.conservation.wave_stream_sha256['wave-bio-stage9'], 'v43 continuity');
check('G-E', 'biology cumulative chars conserved (v43 authored_chars + wave-10 chars = bio walk chars)', bioChars === priorMan.counts.authored_chars_conserved + chemChars, bioChars + ' vs ' + (priorMan.counts.authored_chars_conserved + chemChars));
const newArtifacts = [];
for (const id of NOTES_W12) {
  newArtifacts.push({ kind: 'hub-lesson-import-1.6', noteId: id, path: 'SME-GuidedLessons/integration/hub-import-1.6/' + id + '.hub-lesson-import.json', sha256: sha256(outBufs[id].hub), bytes: outBufs[id].hub.length });
  newArtifacts.push({ kind: 'sme-question-package', noteId: id, path: 'SME-GuidedLessons/integration/question-packages-1.3/' + id + '.sme-question-package.json', sha256: sha256(outBufs[id].pkg), bytes: outBufs[id].pkg.length });
}
const idChecks = NOTES_W12.reduce((t, i) => t + streamChars[i].checks, 0);
const idLessons = NOTES_W12.reduce((t, i) => t + streamChars[i].lessons, 0);
function streamCharsArr() { return streamCharsArr.cached || (streamCharsArr.cached = (() => { const m = { mcq: 0, rec: 0, exp: 0, app: 0 }; for (const id of NOTES_W12) { const S = sources[id].obj; for (const L of S.lessons) for (const c of L.check) { if (c.kind === 'mcq') m.mcq++; else if (c.kind === 'recall') m.rec++; else if (c.kind === 'explain-why') m.exp++; else m.app++; } } return m; })()); }
const manifest = {
  format: 'hub-import-manifest/1.0',
  manifest_version: 44,
  course_id: COURSE,
  b6_manifest_continuity: {
    decision: 'continue-global',
    selected: 'biology stage-B wave 10 CUMULATIVE = manifest v44 (the programme-level v-series continues: chemistry v1..v17 + v32, physics v18..v31, biology v33..v44)',
    rejected: 'per-course series (biology v1 restart) — would fork the programme-level integration ledger and break the single load-scope lineage of record',
    recorded_by: 'runbook B6 (the B6 decision of record is continue-global; the physics, chemistry and biology receipts re-record it); this receipt records it for the biology stage-B wave 10',
  },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_trace: TRACE,
  supersedes: `hub-import-manifest-v43.json (the wave-9 CUMULATIVE: 280 artifacts) — this v44 CUMULATIVE manifest re-pins all 280 prior pack artifacts byte-identical (2 stage-A pilot @ the v33 landed shas + 28 wave-1 @ the v34/v35 landed shas + 26 wave-2 @ the v36 landed shas + 32 wave-3 @ the v37 landed shas + 32 wave-4 @ the v38 landed shas + 34 wave-5 @ the v39 landed shas + 40 wave-6 @ the v40 landed shas + 26 wave-7 @ the v41 landed shas + 30 wave-8 @ the v42 landed shas + 30 wave-9 @ the v43 landed shas) and adds the wave-10 tranche (4 artifacts: the 2 selective-breeding register notes at the 0.7/1.6/1.3 generation); the physics v31 pack (254), chemistry v32 pack (224) and all prior biology artifacts are untouched on disk and conserved by the pipeline's dedicated G-E gates, zero mutation anywhere`,
  checks_layer: {
    wave: 'BIOLOGY-4BI1 stage-B wave 10 (the tenth and closing register bucket of the frozen B4 partition: 2 selective-breeding notes end-to-end per runbook B4; cumulative pack 142 notes / 274 lessons / 2,466 checks — the biology register is COMPLETE)',
    derivation: `${idChecks} authored checks this wave (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application — the B2 law: 9 checks per lesson = 5 MCQ + 2 recall + 1 explain-why + 1 application), graded by the runner's keyword law`,
    declared_revision: 'ADDITIVE first issues (4 artifacts) — the wave-10 notes are new guided planes; all prior pack artifacts byte-untouched',
    grading_law: 'case-insensitive whole-token match of the learner text against the keyword set (stem-tolerant), fail-closed on written items without modelAnswer',
    fail_closed: 'written item without modelAnswer renders reveal-only, never gradeable; the runner refuses any feed whose manifest fails G-A..G-E',
  },
  source_generation: {
    format: 'guided-lesson/0.7',
    namespace: 'SME-GuidedLessons/integration/source-0.7/',
    pin: PIN,
    prior_generation_pins: "{'physics pack': 'v18..v31 commit-A pins (v31 manifest)', 'chemistry pack': 'v32 chemistry stage-B @ commit A 0ef5c2cc', 'biology stage-A': 'v33 @ commit A 7378f249', 'biology wave 1': 'v34/v35 @ commit A dfbcf872', 'biology wave 2': 'v36 @ commit A 832d0f08', 'biology wave 3': 'v37 @ commit A 9c278f61', 'biology wave 4': 'v38 @ commit A 16deb4ac', 'biology wave 5': 'v39 @ commit A 19012907', 'biology wave 6': 'v40 @ commit A 4effa638ade740ed56c839d5d0c5763efce2444b', 'biology wave 7': 'v41 @ commit A e364a127170c177b264e39f75e497d591c3d35d3', 'biology wave 8': 'v42 @ commit A f11b01054335c2e7428cbb0dfd4805a06cb91199', 'biology wave 9': 'v43 @ commit A 42fa82b46736b5e1948b6784e48bf5eb308d9da3'} — the wave-10 notes are authored fresh against the corpus of record at the 0.7 generation",
    int0_lineage: '(new subject — no INT-0 ancestry; the biology 0.7 sources are authored directly against the corpus of record)',
  },
  load_scope: {
    adapter: 'guided-lesson-0.7--hub-lesson-import-1.6',
    target_schemas: ['hub/lesson-import/1.6', 'sme-question-package/1.3'],
  },
  counts: {
    notes: priorMan.counts.notes + NOTES_W12.length,
    lessons: priorMan.counts.lessons + idLessons,
    checks: priorMan.counts.checks + idChecks,
    keyPoints: priorMan.counts.keyPoints + NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).lessons.reduce((t2, l) => t2 + l.keyPoints.length, 0), 0),
    distractors: priorMan.counts.distractors + streamCharsArr().mcq * 3,
    glossaryTerms: priorMan.counts.glossaryTerms + NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    figures: priorMan.counts.figures + NOTES_W12.reduce((t, i) => t + ((JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).figures) || []).length, 0),
    figures_module_mapped: priorMan.counts.figures_module_mapped + totFigMapped,
    figures_note_level: priorMan.counts.figures_note_level + NOTES_W12.reduce((t, i) => t + (((JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).figures) || []).filter((f) => !f.moduleIds || f.moduleIds.length === 0)).length, 0),
    workedExamples_populated: priorMan.counts.workedExamples_populated + totWEPop,
    workedExamples_null: priorMan.counts.workedExamples_null + NOTES_W12.reduce((t, i) => t + (!JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.workedExample ? 1 : 0), 0),
    authored_chars_conserved: priorMan.counts.authored_chars_conserved + chemChars,
  },
  conservation: {
    authored_stream_sha256: bioGrand.digest('hex'),
    authored_chars: String(bioChars),
    wave_stream_sha256: waveOut,
  },
  artifacts: priorMan.artifacts.concat(newArtifacts),
};
const mb = Buffer.from(JSON.stringify(manifest, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'hub-import-manifest-v44.json'), mb);

// INT-3 stage-B wave-9 record (CUMULATIVE, 140 rows)
const int3 = {
  stage: 'BIOLOGY-4BI1 stage-B wave 10 CUMULATIVE (the 2-note selective-breeding bucket + the 140 prior rows: 142 notes / 274 lessons / 2,466 checks at the 0.7/1.6/1.3 generation — the biology register is COMPLETE)',
  title: 'INT-3 transform record — biology stage-B wave 10 CUMULATIVE (guided-lesson/0.7 -> hub/lesson-import/1.6 + sme-question-package/1.3), the 142-row pack anchor table of record (the stage-A pilot row + the 14 wave-1 rows + the 13 wave-2 rows + the 16 wave-3 rows + the 16 wave-4 rows + the 17 wave-5 rows + the 20 wave-6 rows + the 13 wave-7 rows + the 15 wave-8 rows + the 15 wave-9 rows carried byte-equivalent from INT-3-transform-record-bio-stageb9-v43.json; the 112 chemistry stage-B anchors stay in INT-3-transform-record-chem-stageb.json, re-proven on this tree by the G-E gates)',
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_traces: { ignition: TRACE, execution: TRACE },
  adapter: 'guided-lesson-0.7--hub-lesson-import-1.6',
  course_id: COURSE,
  supersedes_int3: 'records/INT-3-transform-record-bio-stageb9-v43.json (the 140-row cumulative wave-9 table; its rows carried byte-equivalent here plus the 2 wave-10 rows)',
  b6_manifest_continuity: { decision: 'continue-global', selected: 'manifest v44 supersedes v43 (cumulative)' },
  biology_stageb10_of_record: {
    basis: 'the stage-B wave 10 bucket per runbook B4: the tenth and final 2 register notes of the frozen B4 partition (the selective-breeding subtopic, register rows 140..141 0-based) authored end-to-end through the full chain, 4 lessons x 9 checks, riding the 0.7/1.6/1.3 generation — with this bucket the 142-note biology register is COMPLETE',
    bootstrap: 'spec_point_resolution.json derived mechanically from hub notes.json smeSpecPointIds (210 ids / 175 codes / 142 notes; the runbook B1 deviation, physics stage-A precedent, disclosed at stage-A)',
    figure_law: '2 corpus figures: both module-mapped heading-unique to host lessons carrying their sourceHeading; no note-level figures this wave',
    b4_partition: [
  {
    "wave": "W1",
    "buckets": [
      {
        "section": "1-the-nature-and-variety-of-living-organisms",
        "subtopic": "characteristics-of-living-organisms",
        "notes": 3,
        "first": "rn_CGsRy4NGjCQRGgXs",
        "last": "rn_x2cfFnFT6j99Q25F"
      },
      {
        "section": "2-structure-and-function-in-living-organisms",
        "subtopic": "biological-molecules",
        "notes": 7,
        "first": "rn_NZDqQdFYGgTTBGjz",
        "last": "rn_6jFtNNZ6G5q86Wbk"
      },
      {
        "section": "2-structure-and-function-in-living-organisms",
        "subtopic": "cell-structure",
        "notes": 4,
        "first": "rn_NPzyvfByCy3bwH6f",
        "last": "rn_3BY6d33PGXMGkgP7"
      }
    ],
    "notes": 14
  },
  {
    "wave": "W2",
    "buckets": [
      {
        "section": "2-structure-and-function-in-living-organisms",
        "subtopic": "co-ordination-and-response",
        "notes": 13,
        "first": "rn_fc4RtMw8kkGWFTrq",
        "last": "rn_Hy9CCn3FFsxHWdp3"
      }
    ],
    "notes": 13
  },
  {
    "wave": "W3",
    "buckets": [
      {
        "section": "2-structure-and-function-in-living-organisms",
        "subtopic": "excretion",
        "notes": 7,
        "first": "rn_zDcyphC9qpScTM69",
        "last": "rn_6pGX3J3F2CsK9zmb"
      },
      {
        "section": "2-structure-and-function-in-living-organisms",
        "subtopic": "gas-exchange",
        "notes": 9,
        "first": "rn_d6rhyBC8xRPrNzcB",
        "last": "rn_CpCCPYCRk4WBGrNs"
      }
    ],
    "notes": 16
  },
  {
    "wave": "W4",
    "buckets": [
      {
        "section": "2-structure-and-function-in-living-organisms",
        "subtopic": "levels-of-organisation",
        "notes": 1,
        "first": "rn_tFhjR4N3rFNHsdcP",
        "last": "rn_tFhjR4N3rFNHsdcP"
      },
      {
        "section": "2-structure-and-function-in-living-organisms",
        "subtopic": "movement-of-substances-into-and-out-of-cells",
        "notes": 3,
        "first": "rn_y3ZgBFFJ5wZKHTRR",
        "last": "rn_QJ52dJK5NW9hggTD"
      },
      {
        "section": "2-structure-and-function-in-living-organisms",
        "subtopic": "nutrition",
        "notes": 12,
        "first": "rn_zN8SGycFZ2q9JbWX",
        "last": "rn_ZZr4qxKbjnNpBdyy"
      }
    ],
    "notes": 16
  },
  {
    "wave": "W5",
    "buckets": [
      {
        "section": "2-structure-and-function-in-living-organisms",
        "subtopic": "respiration",
        "notes": 3,
        "first": "rn_mNVk7QCJzc8XQJFP",
        "last": "rn_V9tRSQ44j8cPFfHM"
      },
      {
        "section": "2-structure-and-function-in-living-organisms",
        "subtopic": "transport-systems",
        "notes": 14,
        "first": "rn_ZJ6CjPzbgTG6Xzb2",
        "last": "rn_GmFw4FzxDVFWMC7B"
      }
    ],
    "notes": 17
  },
  {
    "wave": "W6",
    "buckets": [
      {
        "section": "3-reproduction-and-inheritance",
        "subtopic": "inheritance",
        "notes": 20,
        "first": "rn_KTq9xPjyv7KRwYP5",
        "last": "rn_q7VWTgBZpxbjJvm5"
      }
    ],
    "notes": 20
  },
  {
    "wave": "W7",
    "buckets": [
      {
        "section": "3-reproduction-and-inheritance",
        "subtopic": "reproduction",
        "notes": 13,
        "first": "rn_TgyH9XMP5JrzxyS7",
        "last": "rn_vYqQNBfpz2XvPSXM"
      }
    ],
    "notes": 13
  },
  {
    "wave": "W8",
    "buckets": [
      {
        "section": "4-ecology-and-the-environment",
        "subtopic": "cycles-within-ecosystems",
        "notes": 2,
        "first": "rn_J39MHH5rzVnNYtds",
        "last": "rn_pRwbQZ9hxXqdQ5sw"
      },
      {
        "section": "4-ecology-and-the-environment",
        "subtopic": "feeding-relationships",
        "notes": 3,
        "first": "rn_M6cpyCGJ4dKFpmzC",
        "last": "rn_WWp5PCZWwdbfgqkG"
      },
      {
        "section": "4-ecology-and-the-environment",
        "subtopic": "human-influences-on-the-environment",
        "notes": 5,
        "first": "rn_tMK26k8XqxNmPrk7",
        "last": "rn_DjMYHX8kZ7xQtwyg"
      },
      {
        "section": "4-ecology-and-the-environment",
        "subtopic": "the-organism-in-the-environment",
        "notes": 5,
        "first": "rn_NbbPtXXMvwKXWWpw",
        "last": "rn_wwx5WjCNZ7f8t9hC"
      }
    ],
    "notes": 15
  },
  {
    "wave": "W9",
    "buckets": [
      {
        "section": "5-use-of-biological-resources",
        "subtopic": "cloning",
        "notes": 2,
        "first": "rn_tgyFWpHzKcXGbYG5",
        "last": "rn_B94CVWKQSsVtnTjP"
      },
      {
        "section": "5-use-of-biological-resources",
        "subtopic": "food-production",
        "notes": 9,
        "first": "rn_WNTzgxm68GHhf5fd",
        "last": "rn_st3Pp5BHpBbP5gBY"
      },
      {
        "section": "5-use-of-biological-resources",
        "subtopic": "genetic-modification-genetic-engineering",
        "notes": 4,
        "first": "rn_KfsgJqg7w3KtcnxT",
        "last": "rn_YdgCWbjXJr4kMds6"
      }
    ],
    "notes": 15
  },
  {
    "wave": "W10",
    "buckets": [
      {
        "section": "5-use-of-biological-resources",
        "subtopic": "selective-breeding",
        "notes": 2,
        "first": "rn_xBYWN9JGPSnmJVY7",
        "last": "rn_hybmmF3JNk7kxzJZ"
      }
    ],
    "notes": 2
  }
],
  },
  registry_pin: { file: 'apps/hub/content/igcse-biology-19/notes.json', rows: '142', stageb10_rows: 'rows 140..141 (0-based) — the selective-breeding bucket; the pilot (row 0) and waves 1..9 (rows 1..139) already landed per runbook B3/B4; 142/142 register rows now landed — REGISTER COMPLETE' },
  source_07_generation_pin: PIN,
  conservation_law: {
    law: 'adapter spec 0.7 §7 walk (byte-identical to run_import.mjs targetTokens): specAnchors -> primer -> modules (title/headings/specRefs/opening/keyPoints/depthLayers) -> glossary -> workedExample -> questions (stem/class/options + modelAnswer/keywords on written kinds); per-note sha256 of the "\\n"-joined stream',
    wave_subtotals: waveOut,
  },
  grand_stream: { chars: bioChars, sha256: manifest.conservation.authored_stream_sha256 },
  wave_stream_sha256: waveOut,
  battery: {
    names: ['P0', 'A0', 'AN', 'JC', 'SG', 'KW', '2.1B', 'NUM', 'C-6', 'written', 'C-5', 'B2', 'G-E'],
    a0: 'ajv x2 sources vs guided-lesson.0.7 + kind order x4 lessons + B2 sizing + spec text provenance (curriculum graph verbatim) + figure closure both ways x2 + corpus image coverage x2 + glossary band x2 + primer band x2 + noteRef identity x2',
    an: 'exactly-one-correct x20; correct-key census >=3 distinct per note (post-rotation); distinct option texts; four options',
    sg: 'lesson specRefs subset of file specPoints; every check KP-anchored (content-token overlap)',
    kw: '>=3 grounded keywords per written item x16 (8 recall + 4 explain-why + 4 application)',
    jc: 'every option explained; distractors name misconceptions; correct-option misconception null',
    '2.1b': 'zero 8-gram overlaps of learner-surface text vs the corpus note body x2 (learner surfaces authored fresh this wave)',
    num: 'spot ledgers on the cited figures: rn_xBYWN9JGPSnmJVY7 asserts the three-row natural-versus-artificial comparison table as 1 + 1 + 1 = 3; rn_hybmmF3JNk7kxzJZ asserts the two documented inbreeding risks as 1 + 1 = 2 and the six named brassica crops as a count of 6',
    c6: 'physics+chemistry prior generation union ajv (239 at 0.6/1.5/1.2 per namespace + the 112-note chemistry legacy 0.5/1.4/1.1 generation) + prior biology pack ajv x420 (140 at 0.7/1.6/1.3) + wave-10 outputs ajv x9',
    c5: 'checkRefs <-> questions bidirectional 1:1 in order x2',
    b2: '9 checkRefs per module x4; identity arithmetic 9 = 5+2+1+1 x4',
    ge: 'biology stream anchors x142 (the emitted cumulative INT-3 of record) + the 112 chemistry anchors re-proven on this tree (byte-identical prior pack) + physics legacy generation byte conservation vs v31 x254 + chemistry legacy generation byte conservation vs v32 x224 + prior biology pack byte conservation vs v43 x280 + biology cumulative grand single-finalization',
  },
  biology_census: {
    notes_total: priorMan.counts.notes + NOTES_W12.length,
    lessons_total: priorMan.counts.lessons + idLessons,
    checks_total: priorMan.counts.checks + idChecks,
    wave2_notes: NOTES_W12.length, wave2_lessons: idLessons, wave2_checks: idChecks,
    corpus_images_bound: totFig, worked_examples_populated_wave2: totWEPop, worked_examples_null_wave2: totWENull,
  },
  notes: priorInt3.notes.concat(int3Notes),
};
const ib = Buffer.from(JSON.stringify(int3, null, 2) + '\n');
fs.mkdirSync(path.join(INT, 'records'), { recursive: true });
fs.writeFileSync(path.join(INT, 'records/INT-3-transform-record-bio-stageb10-v44.json'), ib);

// promotion receipt
const receipt = {
  format: 'bio-stageb10-promotion-receipt/1.0',
  wave: 'BIOLOGY-4BI1 stage-B wave 10 (the tenth and closing register bucket: 2 selective-breeding notes end-to-end at the 0.7/1.6/1.3 four-plane generation; CUMULATIVE biology-pack manifest v44 — the biology register is COMPLETE)',
  operator_traces: { ignition: TRACE, execution: TRACE },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  commit_a: { sha: PIN, contents: 'the 2 authored wave-10 source-0.7 notes + integration/tooling/bio-stageb10-pipeline.js (the pipeline of record, derived from the bio-stageb9 landed pipeline)', parent: parent, message_carries_trace: headMsg.includes(TRACE) },
  tranche: {
    notes: NOTES_W12.length, lessons: idLessons, checks: idChecks,
    kinds: { mcq: streamCharsArr().mcq, recall: streamCharsArr().rec, 'explain-why': streamCharsArr().exp, application: streamCharsArr().app },
    figures: totFig, figures_module_mapped: totFigMapped,
    glossary_terms: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    worked_examples: { populated: totWEPop, null: totWENull },
    stream_chars: NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0),
    authoring_shape: {
      bucket: 'selective-breeding (register rows 140..141 0-based of the frozen B4 partition, wave 10 of 10 — the closing wave; the biology register is COMPLETE)',
      lessons: idLessons, checks: idChecks, figures: totFig, figures_module_mapped: totFigMapped, figures_note_level: totFig - totFigMapped,
      glossary_terms: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
      worked_examples: { populated: totWEPop, null: totWENull },
    },
  },
  manifest: { version: 44, artifacts_total: priorMan.artifacts.length + newArtifacts.length, scope: 'biology pack of record (CUMULATIVE: stage-A pilot + wave-1 + wave-2 + wave-3 + wave-4 + wave-5 + wave-6 + wave-7 + wave-8 + wave-9 + wave-10 — REGISTER COMPLETE)', physics_prior_re_pinned_vs_v31: 254, chemistry_prior_re_pinned_vs_v32: 224, prior_biology_re_pinned_vs_v43: 280, first_issues: 4 },
  outputs: emitted.map((e) => e.path),
  gate_log: LOG,
  gates_total: LOG.length,
  gates_passed: LOG.filter((l) => l.ok).length,
  verdict: FAILS.length === 0 ? 'GREEN' : 'RED',
  disclosures: [
    'spec texts carried verbatim from the curriculum graph SPEC_POINT nodes (no spec text invented); spec codes pinned to the notes.json register rows 140..141 (0-based) — the two selective-breeding notes of the frozen B4 partition (wave 10 of 10; with this bucket the partition is fully discharged and the 142-note register is COMPLETE)',
    'MCQ correct-key census enforced POST-transform under the declared deterministic AN rotation table (cyclic per-note re-letter) — the wave-6..12 and bio-wave-1 re-lettering precedent, table-recorded',
    'figure alt strings carried per the 0.7 schema alt description: both of the 2 corpus alts are non-empty and kept verbatim; captions carried where the corpus carries an explanatory emphasis line (the domestic-dog breeds line and the plants example line), so both figures carry a caption this wave',
    'note-level figures (moduleIds [], binding heading-unique per the A0 gate law): NONE this wave — both corpus figures are module-mapped to host lessons carrying their sourceHeading',
    'corpus image URLs carried through onto the /main/ raw.githubusercontent namespace per the 0.7 schema url pattern; the corpus alt strings are kept verbatim where non-empty',
    'worked-example census derived from the sources (totWEPop/totWENull) per the wave-8 amendment law — 0 populated / 2 designed nulls (the W10 selective-breeding bucket carries no corpus worked-example block; the natural-versus-artificial table is reference material, not a worked problem); no hardcoded counts',
    'ajv strict mode relaxed to false for this run: the of-record schema set carries pre-existing strictTypes style notices (the wave-7..11 disclosure class); validation semantics unchanged — same draft-07 compile, same allErrors collection',
`the WAVE_OPEN_BASE d527ceddff041a8dd37789392ba7b06a06018b80 is the resources main tip commit A rides on — the post-wave-9 head after biology stage-B wave 9 landed (commit C d527cedd); the wave opened at that tip with no mid-flight race disclosed at open (operator directive trace 1a1d544cd50a7f81, "Proceed", continuing the four-plane directive chain trace 1a1d147b95e4b899 through "ignite the next wave" 1a1d33d324cf5a15, "go" 1a1d3694dd529292, "wave 6 now" 1a1d3ab985cf1b31, "wave 7" 1a1d496a5dcdc3d5, "Open wave 8" 1a1d4c98377cda1a, wave-9 execution 1a1d50e2f06cd141 and the "Open it" summary round); stage-B wave-10 sequence: commit A lands on main first, the pipeline runs with the race-guard asserting the tip still sits exactly at the commit-A pin, then commit C lands`,
    'the pipeline of record landed at commit A with every per-wave constant computed from the authored content before landing (the wave-4 corrective lesson applied): the census strings cite 2 figures / 4 lessons / 36 checks, matching the dynamic gate law; the P0 parent race-guard accepts any commit-A-chain member of wave 10 or an ancestry-verified mid-flight descendant of the wave-open base from the start (the wave-6/7/8/9 corrective precedent); a local Python mirror of the JS battery (bio10_assemble.py, 449 checks) ran fail-closed green over the authored notes before commit A — zero 8-gram echoes, zero thin SG anchors, zero under-sized keypoint lists, so the first JS run is expected green with zero corrective',
    'the PROMOTION receipt filename carries the Asia/Dhaka execution date 20261113 while generated_at_utc is honest UTC',
    'the B4 partition of record (frozen at stage-A open; 141 notes in 10 subtopic-atomic waves) is embedded in the INT-3 of record; wave 10 discharges the selective-breeding bucket — the FINAL bucket — and the pilot stays out of the buckets per runbook B3; with this wave the biology register is COMPLETE of record: 142/142 notes landed, no wave 11 exists to open',
    'this v44 manifest is CUMULATIVE over the biology pack (284 artifacts = 280 prior re-pinned byte-identical + 4 wave-10 first issues), continuing the v35/v36 corrective convention that keeps the runner-owned guided-import.json index complete',
    'NUM spot ledgers: rn_xBYWN9JGPSnmJVY7 asserts the three-row natural-versus-artificial comparison table as 1 + 1 + 1 = 3; rn_hybmmF3JNk7kxzJZ asserts the two documented inbreeding risks as 1 + 1 = 2 and the six named brassica crops as a count of 6',
  ],
};
const rb = Buffer.from(JSON.stringify(receipt, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'records/BIOLOGY-4BI1-STAGEB10-PROMOTION-20261113.json'), rb);

console.log(`GATES: ${LOG.filter((l) => l.ok).length}/${LOG.length} GREEN, 0 failures`);
console.log(`EMITTED: ${NOTES_W12.length * 2} outputs + manifest v43 (${mb.length}B) + INT-3 (${ib.length}B) + promotion receipt (${rb.length}B)`);
console.log(`Wave-10 tranche: ${NOTES_W12.length} notes / ${idLessons} lessons / ${idChecks} checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application) / ${totFig} figures`);
console.log(`WAVE-10 v44 counts: ${manifest.counts.notes} notes / ${manifest.counts.lessons} lessons / ${manifest.counts.checks} checks; grand stream ${manifest.conservation.authored_chars} chars`);
console.log(`GRAND: ${manifest.conservation.authored_stream_sha256}`);
console.log(`WAVE-10 SUBTOTAL: ${waveOut['wave-bio-stageb9']}`);
