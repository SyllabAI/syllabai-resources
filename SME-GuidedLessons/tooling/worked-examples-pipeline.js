#!/usr/bin/env node
// WE-4 PIPELINE — the worked-example recovery wave pipeline of record.
//
//   phase=apply                load authored WE batches -> apply to the 86 null source-0.2 files
//                              (mirror == merged main, FIG-5 byte-verified), emit out-we/source-0.2 (112)
//   phase=transform --pinned-ref <commit A sha>
//                              emit out-we/hub-import-1.1 (112, pinnedRef=A) + manifest v4 + INT record
//   phase=verify               cold re-verify from emitted outputs
//
// Declared deltas of record: workedExample null->object on exactly the 86 census notes (provenance
// declared per note); figures layer untouched; question packages byte-identical (INT-0 pins).
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const TMP = '/home/z/my-project/.tmp/fig4';
const MIRROR = path.join(TMP, 'out', 'source-0.2');        // == merged main (spot-verified 5/5 + FIG-5 112/112)
const PKGDIR = path.join(TMP, 'cache', 'packages');
const OUT = '/home/z/my-project/.tmp/we1/out';
const AUTH = '/home/z/my-project/scripts/we-authored';
const DL = '/home/z/my-project/download';
const OPERATOR_TRACE = '1a183e5ea252e9b5'; // "the worked-example recovery wave (86 declared nulls — the last per-lesson scaffold delta)"
const INT0_PIN = '4d857c472fd725597ac21db189542c8f12c82dba';
const sha256 = (b) => crypto.createHash('sha256').update(b).digest('hex');
const now = () => new Date().toISOString().replace(/\.\d+Z$/, 'Z');
const j2 = (o) => JSON.stringify(o, null, 2) + '\n';
const j1 = (o) => JSON.stringify(o, null, 1);
const deepEqual = (a, b) => JSON.stringify(a) === JSON.stringify(b);

const ARGS = Object.fromEntries(process.argv.slice(2).map((a, i, arr) => a.startsWith('--') ? [a.slice(2), arr[i + 1]] : []).filter(x => x[0]));
const PHASE = ['apply', 'transform', 'verify'].includes(process.argv[2]) ? process.argv[2] : null;
if (!PHASE) { console.error('usage: we4-pipeline.js apply|transform|verify [--pinned-ref <sha>]'); process.exit(2); }

const CHECKS = []; const FAILS = [];
function check(name, ok, detail) { CHECKS.push({ name, ok: !!ok, detail: detail || '' }); if (!ok) FAILS.push({ name, detail: detail || '' }); return !!ok; }
function report() {
  console.log(`\nCHECKS: ${CHECKS.filter(c => c.ok).length}/${CHECKS.length} pass, ${FAILS.length} FAIL`);
  for (const f of FAILS.slice(0, 25)) console.log('  FAIL:', f.name, '—', String(f.detail).slice(0, 200));
  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(path.join(OUT, `pipeline-${PHASE}-checks.json`), j2({ phase: PHASE, ts: now(), operator_trace: OPERATOR_TRACE, checks: CHECKS, fails: FAILS }));
  if (FAILS.length) process.exit(1);
}

// ── census of record (we1) ────────────────────────────────────────────────────
const census = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/we1-census.json', 'utf8'));
const NULL_IDS = census.nullNoteIds;                 // 86
const POP_IDS = census.populatedNoteIds;             // 26

// ── load authored batches ─────────────────────────────────────────────────────
function loadAuthored() {
  const map = {};
  for (const f of fs.readdirSync(AUTH).filter(f => /^T\d-[a-e]\.json$/.test(f)).sort()) {
    const batch = JSON.parse(fs.readFileSync(path.join(AUTH, f), 'utf8'));
    for (const [noteId, v] of Object.entries(batch)) {
      if (map[noteId]) throw new Error(`duplicate authored noteId ${noteId} in ${f}`);
      map[noteId] = v;
    }
  }
  return map;
}

// ── arithmetic lint (adapter gate C7 law) ────────────────────────────────────
function evalExpr(s) {
  if (!/\d/.test(s)) return null;                              // must contain a digit
  const t = s
    .replace(/(\d)\s*[x×]\s*(?=[\d(])/g, '$1*')                // x/× between number and digit/( -> multiply
    .replace(/[x×]/g, 'x')                                     // any leftover x is a variable -> reject below
    .replace(/÷/g, '/')
    .trim();
  if (/[a-zA-Z^]/.test(t)) return null;                        // letters (variables/formulas)/caret -> not arithmetic
  if (!/^[-+*/().\d\s]+$/.test(t)) return null;
  try {
    const v = Function(`"use strict";return (${t})`)();
    return (typeof v === 'number' && isFinite(v)) ? v : null;
  } catch { return null; }
}
// longest pure-arithmetic suffix of the lhs segment, with boundary guards
// (no mid-token starts out of chemical formulae like CuSO4 / C3H8; no ratio members after "n : ")
function arithTail(lhs) {
  const m = lhs.match(/(-?[0-9][0-9\s+\-×x÷*/.()]*)$/);
  if (!m) return null;
  const tail = m[1];
  const before = lhs.slice(0, lhs.length - tail.length).replace(/[ \t]+$/, '');
  const prev = before.slice(-1);
  if (prev && /[0-9.\-x×A-Za-z]/.test(prev)) return null;      // mid-token start (chem formula / glued number)
  if (prev === ':') {                                          // ratio context "n : m = ..." — skip
    const beforeColon = before.slice(0, -1).replace(/[ \t]+$/, '').slice(-1);
    if (/[0-9]/.test(beforeColon)) return null;
  }
  return tail;
}
// rhs leading number, with optional scientific notation "7.71 × 10^-3"
function parseRhs(seg) {
  const m = seg.match(/^\s*(-?[0-9][0-9.]*)?(?:\s*[x×]\s*10\^?\s*(-?[0-9]+))?/);
  if (!m || m[1] === undefined) return null;
  const mant = Number(m[1]);
  const dec = (m[1].split('.')[1] || '').length;
  if (m[2] !== undefined) return { value: mant * Math.pow(10, Number(m[2])), tol: 0.5 * Math.pow(10, -dec) * Math.pow(10, Number(m[2])) };
  return { value: mant, tol: Math.max(0.5 * Math.pow(10, -dec), 1e-9) };
}
function lintStep(step) {
  const bad = [];
  const segs = step.split('=');
  for (let i = 1; i < segs.length; i++) {
    const r = parseRhs(segs[i]);
    if (r === null) continue;                                  // rhs not a bare number -> not an arithmetic assertion
    const tail = arithTail(segs[i - 1]);
    if (tail === null) continue;
    const v = evalExpr(tail);
    if (v === null) continue;
    if (Math.abs(v - r.value) > r.tol) bad.push(`"${tail.trim()}= ${r.value}" (recomputed ${Number(v.toPrecision(8))})`);
  }
  return bad;
}
function lintWorkedExample(we) {
  const errs = [];
  if (!we || typeof we !== 'object') { errs.push('missing'); return errs; }
  if (typeof we.prompt !== 'string' || we.prompt.length < 10) errs.push('prompt');
  if (!Array.isArray(we.steps) || we.steps.length < 1) errs.push('steps');
  if (typeof we.finalAnswer !== 'string' || we.finalAnswer.length < 3) errs.push('finalAnswer');
  const arith = [];
  for (const s of we.steps || []) for (const b of lintStep(s)) arith.push(b);
  if (arith.length) errs.push('arithmetic: ' + arith.join(' | '));
  return errs;
}

// ── canonical authored stream — adapter spec §7 (verbatim runner walk) ───────
function targetTokens(hub, pkg) {
  const s = []; const les = hub.lesson;
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
  }
  return s;
}
const weTokens = (we) => [we.prompt, ...we.steps, we.finalAnswer].join('\n');

// ── PHASE 1: apply ────────────────────────────────────────────────────────────
async function phaseApply() {
  const Ajv = require('/home/z/node_modules/ajv');
  const ajv = new Ajv({ allErrors: true });
  const v02 = ajv.compile(JSON.parse(fs.readFileSync('/home/z/my-project/scripts/fig4-guided-lesson.0.2.schema.json', 'utf8')));
  const auth = loadAuthored();
  fs.mkdirSync(path.join(OUT, 'source-0.2'), { recursive: true });

  // G-A: authored coverage == exactly the 86 nulls
  const authIds = Object.keys(auth).sort();
  check('W-A1', authIds.length === 86, `authored notes ${authIds.length}`);
  check('W-A2', deepEqual(authIds, [...NULL_IDS].sort()), 'authored set == census null set (no overlap with populated, none missing)');

  // G-B: every authored WE passes schema-shape + style + arithmetic lint
  let lintFails = 0;
  for (const [noteId, v] of Object.entries(auth)) {
    const errs = lintWorkedExample(v.workedExample);
    if (errs.length) { lintFails++; check('W-B ' + noteId, false, errs.join(' | ')); }
    if (!['body-ported', 'body-derived', 'authored'].includes(v.provenance)) { lintFails++; check('W-Bp ' + noteId, false, `provenance ${v.provenance}`); }
  }
  check('W-B', `authored lint x86 (shape + provenance + arithmetic)`, lintFails === 0, `${lintFails} failures`);

  // G-C: apply to the 86; emit all 112
  const revised = new Set();
  for (const f of fs.readdirSync(MIRROR).filter(f => /^guided-lesson-rn_.*\.json$/.test(f)).sort()) {
    const srcBuf = fs.readFileSync(path.join(MIRROR, f));
    const src = JSON.parse(srcBuf.toString('utf8'));
    const noteId = src.noteRef.noteId;
    if (auth[noteId]) {
      const orig = JSON.parse(JSON.stringify(src));
      src.noteAssets.workedExample = auth[noteId].workedExample;
      const ok02 = v02(src);
      check('W-C ' + noteId, ok02, ok02 ? 'revised 0.2 ajv PASS' : ajv.errorsText(v02.errors).slice(0, 200));
      // the ONLY change is workedExample: strip it from both and compare
      const stripWE = (o) => { const c = JSON.parse(JSON.stringify(o)); delete c.noteAssets.workedExample; return c; };
      check('W-D ' + noteId, deepEqual(stripWE(src), stripWE(orig)), 'delta confined to noteAssets.workedExample');
      revised.add(noteId);
    }
    fs.writeFileSync(path.join(OUT, 'source-0.2', f), Buffer.from(j1(src), 'utf8'));
  }
  check('W-E', revised.size === 86, `revised ${revised.size}/86`);
  // the 26 populated notes are byte-identical to the mirror
  let identical = 0;
  for (const noteId of POP_IDS) {
    const f = `guided-lesson-${noteId}.json`;
    if (sha256(fs.readFileSync(path.join(OUT, 'source-0.2', f))) === sha256(fs.readFileSync(path.join(MIRROR, f)))) identical++;
    else check('W-F ' + noteId, false, 'populated note must be byte-identical');
  }
  check('W-F', identical === 26, `populated notes byte-identical ${identical}/26`);

  // G-G: lint ALL 112 workedExamples from emitted outputs (originals included)
  let allFails = 0;
  for (const f of fs.readdirSync(path.join(OUT, 'source-0.2')).sort()) {
    const j = JSON.parse(fs.readFileSync(path.join(OUT, 'source-0.2', f), 'utf8'));
    const we = j.noteAssets.workedExample;
    const errs = we ? lintWorkedExample(we) : [];
    if (errs.length) { allFails++; check('W-G ' + j.noteRef.noteId, false, errs.join(' | ')); }
  }
  check('W-G', 'arithmetic+shape lint x112 (86 authored + 26 of record)', allFails === 0, `${allFails} failures`);
  report();
}

// ── PHASE 2: transform ────────────────────────────────────────────────────────
function phaseTransform() {
  const pinnedRef = ARGS['pinned-ref'];
  if (!pinnedRef || !/^[0-9a-f]{40}$/.test(pinnedRef)) { console.error('--pinned-ref <40-hex commit A> required'); process.exit(2); }
  const Ajv = require('/home/z/node_modules/ajv');
  const ajv = new Ajv({ allErrors: true });
  const v02 = ajv.compile(JSON.parse(fs.readFileSync('/home/z/my-project/scripts/fig4-guided-lesson.0.2.schema.json', 'utf8')));
  const v11 = ajv.compile(JSON.parse(fs.readFileSync('/home/z/my-project/scripts/fig4-hub-lesson-import.1.1.schema.json', 'utf8')));
  const man3 = JSON.parse(fs.readFileSync(path.join(TMP, 'out', 'hub-import-manifest-v3.json'), 'utf8'));
  const int3fig = JSON.parse(fs.readFileSync(path.join(TMP, 'out', 'INT-3-transform-record-figures-0.2.json'), 'utf8'));
  const int3ByNote = new Map(int3fig.notes.map(x => [x.noteId, x]));
  fs.mkdirSync(path.join(OUT, 'hub-import-1.1'), { recursive: true });
  const auth = loadAuthored();

  const recordNotes = []; let grand = crypto.createHash('sha256'); let grandChars = 0;
  const waveHashes = {}; let hubFails = 0; let streamFails = 0; let pkgFails = 0;
  const man3Lesson = new Map(man3.artifacts.filter(a => a.kind === 'hub-lesson-import-1.1').map(a => [a.noteId, a]));
  const man3Pkg = new Map(man3.artifacts.filter(a => a.kind === 'sme-question-package').map(a => [a.noteId, a]));
  const weTotals = { provenance: { 'body-ported': 0, 'body-derived': 0, 'authored': 0 }, addedChars: 0 };

  for (const f of fs.readdirSync(path.join(OUT, 'source-0.2')).sort()) {
    const src02buf = fs.readFileSync(path.join(OUT, 'source-0.2', f));
    const src = JSON.parse(src02buf.toString('utf8'));
    const noteId = src.noteRef.noteId;
    const isRevised = revised0.has(noteId);
    if (!v02(src)) { hubFails++; check('T-A ' + noteId, false, ajv.errorsText(v02.errors).slice(0, 150)); }
    const pkg = JSON.parse(fs.readFileSync(path.join(PKGDIR, `${noteId}.sme-question-package.json`, ), 'utf8'));
    if (sha256(fs.readFileSync(path.join(PKGDIR, `${noteId}.sme-question-package.json`))) !== man3Pkg.get(noteId).sha256) { pkgFails++; check('T-P ' + noteId, false, 'package sha drift vs v3'); }
    // adapter 1.1 — full field map (verbatim FIG-4 transform) + figures passthrough
    const figs = src.figures || [];
    const hub = {
      format: 'hub/lesson-import/1.1',
      adapter: 'guided-lesson-0.2--hub-lesson-import-1.1',
      source: { sourceFormat: 'guided-lesson/0.2', noteId, corpusVersion: src.noteRef.corpusVersion, sourceLayerSha256: sha256(src02buf), pinnedRef },
      lesson: {
        id: `igcse-chemistry::${noteId}`,
        topicTitle: src.noteRef.topicTitle, subtopicTitle: src.noteRef.subtopicTitle, sourceUrl: src.noteRef.sourceUrl,
        specAnchors: src.specPoints.map(x => ({ code: x.code, text: x.text })),
        primer: { text: src.primer.text, prerequisiteSubtopic: src.primer.prerequisiteSubtopic },
        modules: src.lessons.map((l, i) => {
          const m = {
            id: `${noteId}::L${i + 1}`, title: l.title, sourceHeadings: l.sourceHeadings, specRefs: l.specRefs,
            opening: l.opening, keyPoints: l.keyPoints,
            depthLayers: l.depthLayers,
            gatePolicy: { ratingsScale: l.confidenceGate.ratings, continueDisabledUntilChoice: l.confidenceGate.continueDisabledUntilChoice, resumeWithoutReRate: l.confidenceGate.resumeWithoutReRate, postCheckRecalibration: l.confidenceGate.postCheckRecalibration },
            checkRefs: l.check.map((_, k) => `${noteId}::L${i + 1}::Q${k + 1}`),
          };
          if (l.figureIds) m.figureIds = l.figureIds;
          return m;
        }),
        assets: { glossary: src.noteAssets.glossary, workedExample: src.noteAssets.workedExample },
      },
    };
    if (figs.length) hub.lesson.figures = figs.map(x => ({ id: x.id, url: x.url, alt: x.alt, sourceHeading: x.sourceHeading, moduleIds: x.moduleIds }));
    if (!v11(hub)) { hubFails++; check('T-B ' + noteId, false, ajv.errorsText(v11.errors).slice(0, 200)); }
    // adapter determinism vs the 1.0 of-record outputs: only declared deltas allowed
    // (figures landed in v3; workedExample on exactly the 86 census notes)
    const legacy = JSON.parse(fs.readFileSync(path.join(TMP, 'cache', 'hubimport010', `${noteId}.hub-lesson-import.json`, ), 'utf8'));
    const strip = (h) => { const c = JSON.parse(JSON.stringify(h)); delete c.lesson.figures; c.lesson.modules.forEach(m => delete m.figureIds); delete c.format; delete c.adapter; delete c.source; return c; };
    const sNew = strip(hub), sOld = strip(legacy);
    let detOk;
    if (isRevised) {
      detOk = deepEqual(sNew.lesson.assets.glossary, sOld.lesson.assets.glossary)
        && deepEqual(sNew.lesson.specAnchors, sOld.lesson.specAnchors)
        && deepEqual(sNew.lesson.primer, sOld.lesson.primer)
        && deepEqual(sNew.lesson.modules, sOld.lesson.modules)
        && deepEqual(sNew.lesson.topicTitle, sOld.lesson.topicTitle)
        && deepEqual(sNew.lesson.subtopicTitle, sOld.lesson.subtopicTitle)
        && deepEqual(sNew.lesson.sourceUrl, sOld.lesson.sourceUrl)
        && sOld.lesson.assets.workedExample == null
        && JSON.stringify(sNew.lesson.assets.workedExample) === JSON.stringify(auth[noteId].workedExample);
    } else {
      detOk = deepEqual(sNew, sOld);
    }
    if (!detOk) { hubFails++; check('T-C ' + noteId, false, isRevised ? 'non-WE field drift detected' : 'determinism drift on unrevised note'); }
    // stream: new chars == v3 INT-3 anchor chars + WE block (the sharp per-note conservation law)
    const toks = targetTokens(hub, pkg); const s = toks.join('\n'); const streamSha = sha256(Buffer.from(s, 'utf8'));
    const anchorChars = int3ByNote.get(noteId).stream.chars;
    const added = isRevised ? ('\n' + weTokens(auth[noteId].workedExample)).length : 0; // code units — anchors of record use JS string length (FIG-4 law)
    if (isRevised) {
      if (s.length !== anchorChars + added) { streamFails++; check('T-D ' + noteId, false, `chars ${s.length} != v3 anchor ${anchorChars} + WE ${added}`); }
      weTotals.addedChars += added;
      weTotals.provenance[auth[noteId].provenance]++;
    } else {
      if (s.length !== anchorChars) { streamFails++; check('T-D ' + noteId, false, `unrevised stream drift ${s.length} vs ${anchorChars}`); }
    }
    grand.update(Buffer.from(s, 'utf8')); grandChars += s.length;
    const w = 'wave-' + weWave(noteId);
    waveHashes[w] = waveHashes[w] || crypto.createHash('sha256'); waveHashes[w].update(Buffer.from(s, 'utf8'));
    recordNotes.push({
      wave: weWave(noteId), noteId, revised: isRevised,
      weProvenance: isRevised ? auth[noteId].provenance : null,
      sourceLayerSha256: sha256(src02buf), hubSha256: sha256(Buffer.from(j2(hub), 'utf8')),
      pkgSha256: man3Pkg.get(noteId).sha256,
      stream: { chars: s.length, sha256: streamSha },
      addedChars: isRevised ? added : 0,
      figures: figs.length,
    });
    fs.writeFileSync(path.join(OUT, 'hub-import-1.1', `${noteId}.hub-lesson-import.json`), Buffer.from(j2(hub), 'utf8'));
  }
  check('T-A', 'ajv 0.2 x112', true, '');
  check('T-B', 'ajv 1.1 x112 + adapter determinism (declared deltas only)', hubFails === 0, `${hubFails} failures`);
  check('T-D', 'stream law x112: chars == v3 anchor + declared WE block', streamFails === 0, `${streamFails} failures`);
  check('T-P', 'packages byte-identical x112 (v3/v2 shas)', pkgFails === 0, `${pkgFails} drift`);
  check('T-E', 'stream walk covers all 112', recordNotes.length === 112, `${recordNotes.length}`);

  // manifest v4
  const waveOut = {}; for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
  const grandSha = grand.digest('hex');
  const man4 = {
    format: 'hub-import-manifest/1.0',
    manifest_version: 4,
    generated_at_utc: now(),
    operator_trace: OPERATOR_TRACE,
    supersedes: 'hub-import-manifest-v3.json (the 112 sme-question-package artifacts stay byte-identical; all 112 hub-lesson-import artifacts re-pin to the new source generation — 86 carry the worked-example delta, 26 are pin-only revisions)',
    worked_examples_layer: {
      wave: 'WE-1 worked-example recovery wave (operator trace ' + OPERATOR_TRACE + ')',
      declared_revision: 'noteAssets.workedExample null->object on exactly the 86 census notes (scripts/we1-census.json); the 26 populated notes byte-identical at the 0.2 layer',
      provenance_counts: weTotals.provenance,
      placement_law: 'hub renders the worked example as the "An example" stage inside module 1 of each lesson (first-module placement law of record — guided-flow.tsx / noteId page.tsx); no renderer change required',
      provenance_classes: 'body-ported = worked example ported from the note body; body-derived = constructed from the note body content with numbers instantiated; authored = authored from the note teaching content',
      arithmetic_lint: 'gate C7 replay: every pure-arithmetic "expr = result" step recomputed and matched at stated precision (scripts/we4-pipeline.js lintStep)',
      stream_delta: 'declared — authored stream grows by exactly the 86 WE blocks (per-note proof in the INT record); grand + wave subtotals recomputed',
    },
    source_generation: { format: 'guided-lesson/0.2', namespace: 'SME-GuidedLessons/integration/source-0.2/', pin: pinnedRef, int0_lineage: INT0_PIN },
    load_scope: { adapter: 'guided-lesson-0.2--hub-lesson-import-1.1', target_schemas: ['hub/lesson-import/1.1', 'sme-question-package/1.0'] },
    counts: { notes: 112, lessons: 239, checks: 1195, keyPoints: 1212, distractors: 3565, glossaryTerms: 654, figures: 200, figures_module_mapped: 122, figures_note_level: 78, workedExamples_populated: 112, workedExamples_null: 0, authored_chars_conserved: grandChars, authored_chars_v3_baseline: 1347771, added_chars: weTotals.addedChars },
    conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut, equals_v2: false, delta_declared: true, added_chars: weTotals.addedChars, note: 'per-note stream anchors == v3 anchors + declared WE blocks (INT-3-transform-record-worked-examples-1.0.json)' },
    artifacts: [
      ...recordNotes.map(n => ({ kind: 'hub-lesson-import-1.1', noteId: n.noteId, path: `SME-GuidedLessons/integration/hub-import-1.1/${n.noteId}.hub-lesson-import.json`, sha256: n.hubSha256, bytes: fs.statSync(path.join(OUT, 'hub-import-1.1', `${n.noteId}.hub-lesson-import.json`)).size })),
      ...recordNotes.map(n => ({ kind: 'sme-question-package', noteId: n.noteId, path: `SME-GuidedLessons/integration/question-packages/${n.noteId}.sme-question-package.json`, sha256: man3Pkg.get(n.noteId).sha256, bytes: man3Pkg.get(n.noteId).bytes })),
    ],
  };
  check('T-F', man4.artifacts.length === 224, `manifest v4 artifacts ${man4.artifacts.length}`);
  fs.writeFileSync(path.join(OUT, 'hub-import-manifest-v4.json'), j2(man4));

  // INT record
  const rec = {
    stage: 'INT-3', title: 'transform record — worked-examples 1.0 generation (adapter guided-lesson-0.2--hub-lesson-import-1.1)',
    generated_at_utc: now(), operator_trace: OPERATOR_TRACE,
    adapter: 'guided-lesson-0.2--hub-lesson-import-1.1',
    source_02_generation_pin: { commit: pinnedRef, namespace: 'SME-GuidedLessons/integration/source-0.2/' },
    baseline: { manifest: 'hub-import-manifest-v3.json', authored_chars: 1347771 },
    conservation_law: 'worked examples are the only authored delta: every per-note stream equals the v3 anchor plus exactly the declared WE block; the 26 populated notes are unchanged',
    grand_stream: { chars: grandChars, sha256: grandSha },
    wave_stream_sha256: waveOut,
    worked_examples: { revised: recordNotes.filter(n => n.revised).length, provenance_counts: weTotals.provenance, added_chars: weTotals.addedChars },
    notes: recordNotes,
  };
  fs.writeFileSync(path.join(OUT, 'INT-3-transform-record-worked-examples-1.0.json'), j2(rec));
  console.log(`TRANSFORM DONE: 112 x 1.1 emitted @ pin ${pinnedRef.slice(0, 8)}; stream ${grandChars} chars (v3 ${1347771} + ${weTotals.addedChars} WE); provenance`, weTotals.provenance);
  report();
}

// wave lookup: wave number of record per note (from the FIG-4 mapping receipt)
let fig4Receipt = null;
function weWave(noteId) {
  if (!fig4Receipt) fig4Receipt = JSON.parse(fs.readFileSync(path.join(DL, 'FIG4-mapping-receipt-20261028.json'), 'utf8'));
  const n = fig4Receipt.notes.find(x => x.noteId === noteId);
  return n ? n.wave : 0;
}

// ── PHASE 3: verify ───────────────────────────────────────────────────────────
function phaseVerify() {
  const rec = JSON.parse(fs.readFileSync(path.join(OUT, 'INT-3-transform-record-worked-examples-1.0.json'), 'utf8'));
  const man4 = JSON.parse(fs.readFileSync(path.join(OUT, 'hub-import-manifest-v4.json'), 'utf8'));
  const auth = loadAuthored();
  let nOk = 0;
  for (const n of rec.notes) {
    const srcBuf = fs.readFileSync(path.join(OUT, 'source-0.2', `guided-lesson-${n.noteId}.json`));
    const hubBuf = fs.readFileSync(path.join(OUT, 'hub-import-1.1', `${n.noteId}.hub-lesson-import.json`));
    const hub = JSON.parse(hubBuf.toString('utf8'));
    const shaOk = sha256(srcBuf) === n.sourceLayerSha256 && sha256(hubBuf) === n.hubSha256;
    const pinOk = hub.source.sourceLayerSha256 === n.sourceLayerSha256 && hub.source.pinnedRef === rec.source_02_generation_pin.commit;
    const weOk = n.revised
      ? JSON.stringify(hub.lesson.assets.workedExample) === JSON.stringify(auth[n.noteId].workedExample)
      : JSON.stringify(hub.lesson.assets.workedExample) === JSON.stringify(JSON.parse(fs.readFileSync(path.join(MIRROR, `guided-lesson-${n.noteId}.json`), 'utf8')).noteAssets.workedExample);
    if (shaOk && pinOk && weOk) nOk++;
    else check('V ' + n.noteId, false, `sha=${shaOk} pin=${pinOk} we=${weOk} (revised=${n.revised})`);
  }
  check('V-1', nOk === 112, `cold re-verify ${nOk}/112`);
  check('V-2', man4.artifacts.length === 224, `manifest v4 lists ${man4.artifacts.length}`);
  check('V-3', rec.notes.length === 112, `INT record ${rec.notes.length} notes`);
  const revisedN = rec.notes.filter(n => n.revised).length;
  check('V-4', revisedN === 86, `revised ${revisedN}/86`);
  report();
}

// revised set: shared between phases (recomputed from census == authored map)
const revised0 = new Set(NULL_IDS);

(PHASE === 'apply' ? Promise.resolve(phaseApply()) : PHASE === 'transform' ? Promise.resolve(phaseTransform()) : Promise.resolve(phaseVerify())).catch(e => { console.error('FATAL', e); process.exit(1); });
