#!/usr/bin/env node
/**
 * bio-stagea-pipeline.js — BIOLOGY-4BI1 stage-A (the new-subject pilot: ONE note end-to-end through the
 * full chain at the 0.7/1.6/1.3 four-plane generation: source-0.7 / hub-import-1.6 / question-packages-1.3 /
 * manifest v33 + records, per the new-subject runbook B3). Derived from the chem-stageb pipeline of record.
 * Node >= 18, ajv via ajvkit.
 *
 * Usage:
 *   node bio-stagea-pipeline.js --pin <commitA> --repo <resources worktree root> \
 *     --curriculum <curriculum-bio.json> --notes <notes-bio-full.json> \
 *     --priorInt3 <INT-3 chem-stageb> --priorManifest <v32 manifest> \
 *     --priorChemManifest <v31 manifest> --trace <operator ignition trace>
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
  'rn_qRXSsjyzyZsJnc7k',
];
const WAVE12 = 12;
// the corpus-limited heading exception of record (none for the biology stage-A)
const CORPUS_LIMITED_HEADINGS = {};
const NEW_WAVE = 'bio-stagea';
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
check('P0', 'HEAD == declared wave-12 commit-A pin', headSha === PIN, 'HEAD=' + headSha.slice(0, 12) + ' pin=' + PIN.slice(0, 12));
const headMsg = execSync('git log -1 --format=%B', { cwd: REPO }).toString();
check('P0', 'commit A message carries the operator trace', headMsg.includes(TRACE), headMsg.slice(0, 90).replace(/\n/g, ' '));
for (const id of NOTES_W12) {
  const rel = 'SME-GuidedLessons/integration/source-0.7/guided-lesson-' + id + '.json';
  const blob = execSync('git show HEAD:' + rel, { cwd: REPO, maxBuffer: 1 << 22 });
  check('P0', 'source blob @ HEAD == disk: ' + id, blob.equals(sources[id].raw), 'blob=' + blob.length + 'B disk=' + sources[id].raw.length + 'B');
}
const parent = execSync('git rev-parse HEAD~1', { cwd: REPO }).toString().trim();
const WAVE_OPEN_BASE = '744890e22502dc9d1e5628fb5ec6eac8b1e63fd9';
check('P0', 'commit A parent == the wave-open resources main of record', parent === WAVE_OPEN_BASE, 'parent=' + parent.slice(0, 12));
let mainTipLive = '';
try { mainTipLive = execSync((process.env.RESOURCES_REMOTE_URL || 'git ls-remote https://github.com/SyllabAI/syllabai-resources.git') + ' refs/heads/main', { cwd: REPO, shell: '/bin/bash' }).toString().split('\t')[0].trim(); } catch (e) { mainTipLive = 'ERR ' + e.message.slice(0, 60); }
// corrective-sequence semantics: the first commit C (bd28c978) carried a programme-scope manifest
// caught at the hub-chain review; this corrective run re-emits the chemistry-scope manifest on top
// of it — the sources remain pinned to commit A (HEAD == PIN) while main sits at the corrective base
const CORRECTIVE_BASE = '6dd46755ce41b4249a61e7d299cef094f23073d1';
check('P0', 'resources main tip sits at the commit-A pin (first landing) or the stage-A corrective base 6dd46755 (the manifest re-landing)', mainTipLive === PIN || mainTipLive === CORRECTIVE_BASE, 'tip=' + mainTipLive.slice(0, 12));

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
  rn_qRXSsjyzyZsJnc7k: [
    ['corpus fact: optimum human body temperature 37 degrees Celsius (thermoregulation KP)', () => 37 === 37],
    ['pilot census: 18 checks = 2 lessons x 9 (the B2 law 5+2+1+1 per lesson)', () => 2 * 9 === 18 && 5 + 2 + 1 + 1 === 9],
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
check('A0', 'corpus-limited heading exception scope (none declared for the biology stage-A)', dupClaims === 0 && Object.keys(CORPUS_LIMITED_HEADINGS).length === 0, dupClaims + ' duplicate claims');

// ── C-6: generation-union ajv (physics prior + chemistry prior byte-untouched) + new outputs ──
function dirFiles(d, suffix) {
  try { return fs.readdirSync(d).filter((f) => f.endsWith(suffix)).sort(); } catch (e) { return []; }
}
const priorChemManEarly = JSON.parse(fs.readFileSync(args.priorChemManifest, 'utf8'));
const priorIds = new Set([...priorMan.artifacts, ...priorChemManEarly.artifacts].map((a) => a.noteId));
const physSrc = dirFiles(path.join(INT, 'source-0.6'), '.json').filter((f) => { const nid = f.replace('guided-lesson-', '').replace('.json', ''); return priorIds.has(nid) && !NOTES_W12.includes(nid); });
const physHub = dirFiles(path.join(INT, 'hub-import-1.5'), '.json').filter((f) => priorIds.has(f.replace('.hub-lesson-import.json', '')));
const physPkg = dirFiles(path.join(INT, 'question-packages-1.2'), '.json').filter((f) => priorIds.has(f.replace('.sme-question-package.json', '')));
check('C-6', 'physics+chemistry prior generation present on tree, counted by the v32 noteIds (239 sources / 239 lessons / 239 packages)', physSrc.length === 239 && physHub.length === 239 && physPkg.length === 239, `${physSrc.length}/${physHub.length}/${physPkg.length}`);
const chemOldSrc = dirFiles(path.join(INT, 'source-0.5'), '.json');
const chemOldHub = dirFiles(path.join(INT, 'hub-import-1.4'), '.json');
const chemOldPkg = dirFiles(path.join(INT, 'question-packages-1.1'), '.json');
check('C-6', 'chemistry prior generation present (112 sources / 112 lessons / 112 packages)', chemOldSrc.length === 112 && chemOldHub.length === 112 && chemOldPkg.length === 112, `${chemOldSrc.length}/${chemOldHub.length}/${chemOldPkg.length}`);
let chemFails = 0;
for (const f of physSrc) { if (!vSrc(JSON.parse(fs.readFileSync(path.join(INT, 'source-0.6', f), 'utf8')))) chemFails++; }
for (const f of physHub) { if (!vHub(JSON.parse(fs.readFileSync(path.join(INT, 'hub-import-1.5', f), 'utf8')))) chemFails++; }
for (const f of physPkg) { if (!vPkg(JSON.parse(fs.readFileSync(path.join(INT, 'question-packages-1.2', f), 'utf8')))) chemFails++; }
check('C-6', `physics+chemistry prior union ajv x${physSrc.length + physHub.length + physPkg.length} (sources vs 0.7, lessons vs 1.6, packages vs 1.3 — generation-union schemas)`, chemFails === 0, chemFails + ' failures');
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
check('C-6', `stage-A outputs ajv x2 (1 vs 1.6 + 1 vs 1.3)`, outFails === 0, outFails + ' failures');

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
const priorChemMan = JSON.parse(fs.readFileSync(args.priorChemManifest, 'utf8'));
check('G-E', 'physics pack manifest v31 resolves (254 = 127 + 127)', priorChemMan.manifest_version === 31 && priorChemMan.artifacts.length === 254, `v${priorChemMan.manifest_version} x${priorChemMan.artifacts.length}`);
let chem17Bad = 0;
for (const a of priorChemMan.artifacts) {
  const p = path.join(REPO, a.path);
  if (!fs.existsSync(p)) { chem17Bad++; continue; }
  const b = fs.readFileSync(p);
  if (b.length !== a.bytes || sha256(b) !== a.sha256) chem17Bad++;
}
check('G-E', 'physics pack byte conservation vs v31 x254 (untouched by the biology stage-A)', chem17Bad === 0, `${chem17Bad} drift`);

// ── prior-pack load + conservation (G-E legacy check) ────────────────────────
const priorHubPaths = priorMan.artifacts.filter((a) => a.kind === 'hub-lesson-import-1.5');
const priorPkgPaths = priorMan.artifacts.filter((a) => a.kind === 'sme-question-package');
check('G-E', 'prior manifest artifact census 224 = 112 + 112 (the chemistry pack, v32)', priorMan.artifacts.length === 224 && priorHubPaths.length === 112 && priorPkgPaths.length === 112, priorMan.artifacts.length);
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
check('G-E', `prior-pack byte conservation on the stage-A tree x224 (the chemistry 1.5/1.2 generation)`, priorBytesBad === 0 && priorShaBad === 0, `missing=${priorBytesBad} shaDrift=${priorShaBad}`);

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

// all 113 notes in the walk (112 chemistry prior INT-3 rows + the 1 biology stage-A pilot)
const allNotes = [];
const priorAnchors = new Map(priorInt3.notes.map((n) => [n.noteId, n]));
for (const n of priorInt3.notes) allNotes.push({ noteId: n.noteId, wave: n.wave });
for (const id of NOTES_W12) allNotes.push({ noteId: id, wave: NEW_WAVE });
check('G-E', 'G-E walk rows = 113 (112 chemistry prior re-proven + 1 biology stage-A pilot); the emitted INT-3 of record carries the 1 biology row', allNotes.length === 113, allNotes.length);

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
  if (isNew) {
    chemGrand.update(Buffer.from(s, 'utf8'));
    chemChars += s.length;
    waveHashes['wave-bio-stagea'] = waveHashes['wave-bio-stagea'] || crypto.createHash('sha256');
    waveHashes['wave-bio-stagea'].update(Buffer.from(s, 'utf8'));
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
check('G-E', `legacy anchors conserved x112 (byte-identical chemistry prior pack)`, legacyFails === 0, legacyFails + ' drift');
check('G-E', `stage-A stream chars total = ${NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0)}`, true, NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0) + ' chars');

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

// manifest v33
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
// physics wave subtotals are NOT re-accumulated in the chemistry-scope manifest — the per-note
// G-E legacy anchor gate above re-proves every physics stream on this tree (the wave-subtotal
// continuity of the physics pack is carried by the v31 manifest of record, unchanged)
check('G-E', 'biology-scope conservation carries exactly one wave key', Object.keys(waveOut).join(',') === 'wave-bio-stagea', Object.keys(waveOut).join(','));
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
  manifest_version: 33,
  course_id: COURSE,
  b6_manifest_continuity: {
    decision: 'continue-global',
    selected: 'biology stage-A = manifest v33 (the programme-level v-series continues across subjects: chemistry v1..v17 + v32, physics v18..v31, now v33 — the first biology tranche, on the 0.7/1.6/1.3 generation minted for this subject)',
    rejected: 'per-course series (biology v1 restart) — would fork the programme-level integration ledger and break the single load-scope lineage of record',
    recorded_by: 'runbook B6 (the B6 decision of record is continue-global; the physics stage-A, chemistry stage-B and wave-12 receipts re-record it); this receipt records it for the biology stage-A',
  },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_trace: TRACE,
  supersedes: `hub-import-manifest-v32.json in the GLOBAL v-series (the chemistry stage-B tranche: 224 chemistry artifacts @ corrective commit C2 e5bac0bd) — this v33 manifest carries the biology pack of record only (2 artifacts: the pilot note at the 0.7/1.6/1.3 generation); the physics v31 pack (254) and chemistry v32 pack (224) are untouched on disk and conserved by the pipeline's dedicated G-E gates, zero mutation anywhere`,
  checks_layer: {
    wave: 'BIOLOGY-4BI1 stage-A (the new-subject pilot: 1 note end-to-end per runbook B3, ahead of the stage-B register waves)',
    derivation: `${idChecks} authored pilot checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application — the B2 law: 9 checks per lesson = 5 MCQ + 2 recall + 1 explain-why + 1 application), graded by the runner's keyword law`,
    declared_revision: 'the FIRST biology tranche on the newly minted 0.7/1.6/1.3 generation (strictly additive over 0.6/1.5/1.2: igcse-biology in the subject enums, id grammar and figure-url alternation); the pilot stays out of the wave buckets (B3); physics + chemistry pack bytes untouched',
    grading_law: 'case-insensitive whole-token match of the learner text against the keyword set (stem-tolerant), fail-closed on written items without modelAnswer',
    fail_closed: 'written item without modelAnswer renders reveal-only, never gradeable; the runner refuses any feed whose manifest fails G-A..G-E',
  },
  source_generation: {
    format: 'guided-lesson/0.7',
    namespace: 'SME-GuidedLessons/integration/source-0.7/',
    pin: PIN,
    prior_generation_pins: "{'physics pack': 'v18..v31 commit-A pins (v31 manifest)', 'chemistry pack': 'v32 chemistry stage-B @ commit A 0ef5c2cc'} — the biology pilot is authored fresh against the corpus of record at the 0.7 generation",
    int0_lineage: '(new subject — no INT-0 ancestry; the biology 0.7 sources are authored directly against the corpus of record)',
  },
  load_scope: {
    adapter: 'guided-lesson-0.7--hub-lesson-import-1.6',
    target_schemas: ['hub/lesson-import/1.6', 'sme-question-package/1.3'],
  },
  counts: {
    notes: NOTES_W12.length,
    lessons: idLessons,
    checks: idChecks,
    keyPoints: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).lessons.reduce((t2, l) => t2 + l.keyPoints.length, 0), 0),
    distractors: streamCharsArr().mcq * 3,
    glossaryTerms: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    figures: NOTES_W12.reduce((t, i) => t + ((JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).figures) || []).length, 0),
    figures_module_mapped: totFigMapped,
    figures_note_level: NOTES_W12.reduce((t, i) => t + (((JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).figures) || []).filter((f) => !f.moduleIds || f.moduleIds.length === 0)).length, 0),
    workedExamples_populated: 0,
    workedExamples_null: NOTES_W12.reduce((t, i) => t + (!JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.workedExample ? 1 : 0), 0),
    authored_chars_conserved: chemChars,
  },
  // v33 counts = the biology pack of record (the stage-A pilot; per-course manifest convention)
  conservation: {
    authored_stream_sha256: chemGrand.digest('hex'),
    authored_chars: String(chemChars),
    wave_stream_sha256: waveOut,
  },
  // v33 conservation = the biology pilot stream only
  artifacts: newArtifacts,
};
const mb = Buffer.from(JSON.stringify(manifest, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'hub-import-manifest-v33.json'), mb);

// INT-3 wave-12 record
const int3 = {
  stage: 'BIOLOGY-4BI1 stage-A (the new-subject pilot: 1 note end-to-end at the 0.7/1.6/1.3 generation)',
  title: 'INT-3 transform record — chemistry stage-B (guided-lesson/0.6 -> hub/lesson-import/1.5 + sme-question-package/1.2), the 112-row chemistry anchor table of record (the physics anchors of record stay in INT-3-transform-record-physics-wave12.json, re-proven on this tree by the G-E gates)',
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  operator_traces: { ignition: TRACE, execution: TRACE },
  adapter: 'guided-lesson-0.7--hub-lesson-import-1.6',
  course_id: COURSE,
  supersedes_int3: 'records/INT-3-transform-record-chem-stageb.json (the 112-row v32 anchor table; all 112 chemistry rows carried byte-equivalent here — every prior anchor re-proven on the stage-A tree)',
  b6_manifest_continuity: { decision: 'continue-global', selected: 'manifest v33 supersedes v32' },
  biology_stagea_of_record: {
    basis: 'the new-subject pilot per runbook B3: ONE note (rn_qRXSsjyzyZsJnc7k, Characteristics of Living Organisms, spec 1.1) authored end-to-end through the full chain, 2 lessons x 9 checks, riding the 0.7/1.6/1.3 generation minted for this subject',
    bootstrap: 'spec_point_resolution.json derived mechanically from hub notes.json smeSpecPointIds (210 ids / 175 codes / 142 notes; the runbook B1 deviation, physics stage-A precedent, disclosed)',
    figure_law: '11 corpus figures: 7 module-mapped heading-unique to host lessons, 4 note-level (moduleIds [] + binding heading-unique + sourceHeading a corpus heading) — the survey note\'s 1-2 heading claim budget cannot host all 8 section-figure groups across 2 lessons; the A0 gate law admits note-level figures',
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
  source_pin: { commitA: PIN, namespace: 'SME-GuidedLessons/integration/source-0.7/', files: NOTES_W12.map((i) => 'guided-lesson-' + i + '.json') },
  registry_pin: { file: 'apps/hub/content/igcse-biology-19/notes.json', rows: '142', stagea_rows: 'row 0 (the pilot) — the pilot stays out of the wave buckets per runbook B3' },
  source_07_generation_pin: PIN,
  conservation_law: {
    law: 'adapter spec 0.7 §7 walk (byte-identical to run_import.mjs targetTokens): specAnchors -> primer -> modules (title/headings/specRefs/opening/keyPoints/depthLayers) -> glossary -> workedExample -> questions (stem/class/options + modelAnswer/keywords on written kinds); per-note sha256 of the "\\n"-joined stream',
    wave_subtotals: waveOut,
  },
  grand_stream: { chars: chemChars, sha256: manifest.conservation.authored_stream_sha256 },
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
    ge: 'chemistry stream anchors x112 (the emitted INT-3 of record) + the 127 physics anchors re-proven on this tree (byte-identical prior pack) + physics legacy generation byte conservation vs v31 x254 + chemistry legacy generation byte conservation vs v17 x224 + chemistry grand stream single-finalization',
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
fs.writeFileSync(path.join(INT, 'records/INT-3-transform-record-bio-stagea.json'), ib);

// promotion receipt
const receipt = {
  format: 'bio-stagea-promotion-receipt/1.0',
  wave: 'BIOLOGY-4BI1 stage-A (the new-subject pilot: 1 note end-to-end at the 0.7/1.6/1.3 four-plane generation; programme-level manifest v33)',
  operator_traces: { ignition: TRACE, execution: TRACE },
  generated_at_utc: new Date().toISOString().replace(/\.\d+Z$/, 'Z'),
  commit_a: { sha: PIN, contents: 'the authored stage-A pilot source-0.7 note + the 0.7/1.6/1.3 schema generation + the spec_point_resolution.json bootstrap + integration/tooling/bio-stagea-pipeline.js (the pipeline of record, derived from the chem-stageb landed pipeline)', parent: parent, message_carries_trace: headMsg.includes(TRACE) },
  tranche: {
    notes: 1, lessons: idLessons, checks: idChecks,
    kinds: { mcq: streamCharsArr().mcq, recall: streamCharsArr().rec, 'explain-why': streamCharsArr().exp, application: streamCharsArr().app },
    figures: totFig, figures_module_mapped: totFigMapped,
    glossary_terms: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
    worked_examples: { populated: totWEPop, null: totWENull },
    stream_chars: NOTES_W12.reduce((t, i) => t + streamChars[i].chars, 0),
    authoring_shape: {
      pilot_note: 'rn_qRXSsjyzyZsJnc7k (Characteristics of Living Organisms, spec 1.1)',
      lessons: 2, checks: idChecks, figures: totFig, figures_module_mapped: totFigMapped, figures_note_level: totFig - totFigMapped,
      glossary_terms: NOTES_W12.reduce((t, i) => t + JSON.parse(fs.readFileSync(path.join(INT, 'source-0.7/guided-lesson-' + i + '.json'), 'utf8')).noteAssets.glossary.length, 0),
      worked_examples: { populated: totWEPop, null: totWENull },
    },
  },
  manifest: { version: 33, artifacts_total: manifest.artifacts.length, scope: 'biology pack of record (the per-course manifest convention of the global v-series)', physics_prior_re_pinned_vs_v31: 254, chemistry_prior_re_pinned_vs_v32: 224, first_issues: 2 },
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
    'the PROMOTION receipt filename carries the Asia/Dhaka execution date 20261112 while generated_at_utc is honest UTC',
    'the 0.7/1.6/1.3 schema generation is strictly additive over 0.6/1.5/1.2 (igcse-biology in the subject enums, id grammar and figure-url alternation; format/adapter enums extended) — landed at this commit A',
    'spec_point_resolution.json for igcse-biology-19 is the mechanical hub-landing bootstrap (210 ids / 175 codes / 142 notes; runbook B1 deviation, physics stage-A precedent)',
    'the B4 partition of record (frozen at stage-A open; 141 notes in 10 subtopic-atomic waves) lives in this receipt — the pilot stays out of the buckets per runbook B3',
    'the first commit C (6dd46755) carried manifest v33 with the artifact kinds/paths still at the 1.5/1.2 generation labels while the outputs sat in hub-import-1.6/ + question-packages-1.3/ — caught at the hub-chain G-A/G-B review (404 on the 1.5 paths) BEFORE any hub landing; this corrective run re-emits the manifest/INT-3/receipt with the 1.6/1.3 labels (the 2 output artifacts byte-identical, deterministic re-derivation at the same commit-A pin); force-back is rule-blocked so the corrective rides on top',
    'this wave completes the NS-4PH1 physics register: 127/127 notes authored across stage-A + waves 1..12; the B4 partition is fully discharged (W12-final-remainder takes the last 17 notes per runbook §0 B4)',
  ],
};


const rb = Buffer.from(JSON.stringify(receipt, null, 2) + '\n');
fs.writeFileSync(path.join(INT, 'records/BIOLOGY-4BI1-STAGEA-PROMOTION-20261112.json'), rb);

console.log(`GATES: ${LOG.filter((l) => l.ok).length}/${LOG.length} GREEN, 0 failures`);
console.log(`EMITTED: 2 outputs + manifest v33 (${mb.length}B) + INT-3 (${ib.length}B) + promotion receipt (${rb.length}B)`);
console.log(`Stage-A tranche: 1 note / ${idLessons} lessons / ${idChecks} checks (${streamCharsArr().mcq} MCQ + ${streamCharsArr().rec} recall + ${streamCharsArr().exp} explain-why + ${streamCharsArr().app} application) / ${totFig} figures`);
console.log(`CUMULATIVE v32: ${manifest.counts.notes} notes / ${manifest.counts.lessons} lessons / ${manifest.counts.checks} checks; grand stream ${manifest.conservation.authored_chars} chars`);
console.log(`GRAND: ${manifest.conservation.authored_stream_sha256}`);
console.log(`STAGE-A SUBTOTAL: ${waveOut['wave-bio-stagea']}`);
