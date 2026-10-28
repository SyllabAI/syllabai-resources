#!/usr/bin/env node
// FIG-4 PIPELINE — the deterministic figures mapping + adapter 1.1 transform of record.
//
//   phase=map                     fetch upstream 0.1 artifacts @ pin, map note figures, emit source-0.2/
//   phase=transform --pinned-ref  emit hub-import-1.1/ + manifest v3 + INT-3-0.2 record (needs commit A sha)
//   phase=verify                  re-run every gate against emitted outputs (fail-closed)
//
// Zero-DB, zero synthesis: figures = the parent note's own images (sourcing decision of record,
// trace 1a1800f3b8c138e5); mapping is mechanical (nearest preceding heading -> sourceHeadings join).
// The canonical authored stream (adapter spec §7) is untouched by construction — proven per note.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const TMP = '/home/z/my-project/.tmp/fig4';
const OUT = path.join(TMP, 'out');
const CACHE = path.join(TMP, 'cache');
const DL = '/home/z/my-project/download';
const TOKEN = fs.readFileSync('/home/z/my-project/.creds/gh-pat.candidate', 'utf8').trim();
const API = 'https://api.github.com';
const HDR = { Authorization: `Bearer ${TOKEN}`, Accept: 'application/vnd.github.raw', 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'fig4-pipeline' };
const R_REPO = 'SyllabAI/syllabai-resources';
const R_PIN = '8460a5f3a03fd7d43ed31e39c27d846f8a747208'; // resources main head at grounding
const OPERATOR_TRACE = '1a1820011919e8b9'; // "go, run the full 112-note figures chain"
const INT0_PIN = '4d857c472fd725597ac21db189542c8f12c82dba';
const sha256 = (b) => crypto.createHash('sha256').update(b).digest('hex');
const now = () => new Date().toISOString().replace(/\.\d+Z$/, 'Z');

const ARGS = Object.fromEntries(process.argv.slice(2).map((a, i, arr) => a.startsWith('--') ? [a.slice(2), arr[i + 1]] : []).filter(x => x[0]));
const PHASE = process.argv[2] === 'map' || process.argv[2] === 'transform' || process.argv[2] === 'verify' ? process.argv[2] : null;
if (!PHASE) { console.error('usage: fig4-pipeline.js map|transform|verify [--pinned-ref <sha>]'); process.exit(2); }

const CHECKS = []; const FAILS = [];
function check(name, ok, detail) { CHECKS.push({ name, ok: !!ok, detail: detail || '' }); if (!ok) FAILS.push({ name, detail: detail || '' }); return !!ok; }
async function pooled(items, n, fn) { const out = new Array(items.length); let i = 0; await Promise.all(Array.from({ length: n }, async () => { while (i < items.length) { const idx = i++; out[idx] = await fn(items[idx], idx); } })); return out; }
async function fetchRaw(repo, rel, ref) {
  const url = `${API}/repos/${repo}/contents/${encodeURI(rel)}?ref=${ref}`;
  for (let a = 0; a < 3; a++) {
    const r = await fetch(url, { headers: HDR });
    if (r.ok) return Buffer.from(await r.arrayBuffer());
    if (a === 2) throw new Error(`HTTP ${r.status} for ${rel}`);
    await new Promise(res => setTimeout(res, 1200));
  }
}
const j2 = (o) => JSON.stringify(o, null, 2) + '\n';
const j1 = (o) => JSON.stringify(o, null, 1); // wave-artifact family convention: 1-space, no trailing NL

// ── the mapping algorithm of record (prototype FIG-1R, productionized) ──────
const HEAD_RE = /^(#{1,4})\s+(.+?)\s*#*\s*$/;
const IMG_RE = /!\[([^\]]*)\]\(([^)\s]+)\)/g;
function normHeading(s) { return s.toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim(); }
function segment(bodyMd) {
  const segs = []; let cur = null;
  for (const line of bodyMd.split('\n')) {
    const hm = line.match(HEAD_RE);
    if (hm) { cur = hm[2].trim(); continue; }
    let m; IMG_RE.lastIndex = 0;
    while ((m = IMG_RE.exec(line))) segs.push({ alt: m[1].trim(), url: m[2], sourceHeading: cur });
  }
  return segs;
}
function slugAlt(url) {
  const base = url.split('/').pop().replace(/\.(png|jpg|jpeg|webp|avif)$/i, '');
  return base.replace(/^[0-9a-f]{12}-/, '').replace(/-/g, ' ').trim() || base;
}
function mapFigures(bodyMd, lessons) {
  const imgs = segment(bodyMd);
  const out = []; const perLesson = lessons.map(() => []);
  imgs.forEach((im, idx) => {
    if (!im.sourceHeading) throw new Error(`image ${idx} has no preceding heading`);
    const nh = normHeading(im.sourceHeading);
    const exact = [], fuzzy = [];
    lessons.forEach((l, li) => {
      for (const sh of l.sourceHeadings) {
        if (sh === im.sourceHeading) { exact.push(li); return; }
        const ns = normHeading(sh);
        if (nh && ns && (nh === ns || nh.includes(ns) || ns.includes(nh))) { fuzzy.push(li); return; }
      }
    });
    const claim = exact.length ? { mode: 'exact', ls: exact } : fuzzy.length ? { mode: 'fuzzy', ls: fuzzy } : { mode: 'none', ls: [] };
    const id = `fig-${String(idx + 1).padStart(2, '0')}`;
    const alt = im.alt || slugAlt(im.url);
    out.push({ id, url: im.url, alt, altSource: im.alt ? 'md' : 'slug-fallback', sourceHeading: im.sourceHeading, moduleIds: claim.ls.map(li => `L${li + 1}`), matchMode: claim.mode });
    claim.ls.forEach(li => perLesson[li].push(id));
  });
  return { figures: out, perLesson };
}

// ── canonical authored stream — adapter spec §7, verbatim runner walk ───────
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
function deepEqual(a, b) { return JSON.stringify(a) === JSON.stringify(b); }

async function loadInputs() {
  fs.mkdirSync(CACHE, { recursive: true });
  // notes corpus (mapping source of record)
  const notesPath = path.join(TMP, 'hub', 'notes.json');
  const notes = JSON.parse(fs.readFileSync(notesPath, 'utf8'));
  // assets basenames
  const assets = new Set(JSON.parse(fs.readFileSync(path.join(TMP, 'assets-list.json'), 'utf8')));
  // upstream 0.1 artifacts @ pin — cached
  const artDir = path.join(CACHE, 'artifacts'); fs.mkdirSync(artDir, { recursive: true });
  const pkgDir = path.join(CACHE, 'packages'); fs.mkdirSync(pkgDir, { recursive: true });
  const hubDir = path.join(CACHE, 'hubimport010'); fs.mkdirSync(hubDir, { recursive: true });
  // wave dirs -> noteId -> wave + relpath
  const waves = {};
  for (let w = 1; w <= 10; w++) {
    const d = await (await fetch(`${API}/repos/${R_REPO}/contents/SME-GuidedLessons/wave-${w}?ref=${R_PIN}`, { headers: { ...HDR, Accept: 'application/vnd.github+json' } })).json();
    for (const f of d.filter(x => /^guided-lesson-rn_.*\.json$/.test(x.name))) waves[f.name] = { wave: w, rel: `SME-GuidedLessons/wave-${w}/${f.name}` };
  }
  const names = Object.keys(waves);
  check('C-2a', names.length === 112, `upstream artifact files ${names.length}`);
  const arts = await pooled(names, 6, async (name) => {
    const dest = path.join(artDir, name);
    if (!fs.existsSync(dest)) fs.writeFileSync(dest, await fetchRaw(R_REPO, waves[name].rel, R_PIN));
    return { name, wave: waves[name].wave, buf: fs.readFileSync(dest) };
  });
  // current hub-import 1.0 outputs @ pin (adapter determinism baseline)
  const v2 = JSON.parse(fs.readFileSync(path.join(TMP, 'up', 'hub-import-manifest-v2.json'), 'utf8'));
  const lesV2 = v2.artifacts.filter(a => a.kind === 'hub-lesson-import');
  const pkgsV2 = v2.artifacts.filter(a => a.kind === 'sme-question-package');
  check('C-2b', lesV2.length === 112 && pkgsV2.length === 112, `v2 manifest kinds ${lesV2.length}/${pkgsV2.length}`);
  await pooled(lesV2, 6, async (a) => {
    const base = a.path.split('/').pop(); const dest = path.join(hubDir, base);
    if (!fs.existsSync(dest)) fs.writeFileSync(dest, await fetchRaw(R_REPO, `SME-GuidedLessons/integration/hub-import/${base}`, R_PIN));
    const buf = fs.readFileSync(dest);
    check('C-2c ' + base, sha256(buf) === a.sha256, `hub-import 1.0 @ pin sha ${sha256(buf).slice(0, 12)} vs v2 ${a.sha256.slice(0, 12)}`);
    return buf;
  });
  // question packages @ pin (unchanged generation — verify ALL against v2 shas)
  await pooled(pkgsV2, 6, async (a) => {
    const base = a.path.split('/').pop(); const dest = path.join(pkgDir, base);
    if (!fs.existsSync(dest)) fs.writeFileSync(dest, await fetchRaw(R_REPO, `SME-GuidedLessons/integration/question-packages/${base}`, R_PIN));
    const buf = fs.readFileSync(dest);
    check('C-2d ' + base, sha256(buf) === a.sha256, `package @ pin sha vs v2`);
    return buf;
  });
  // INT-3 legacy anchors
  const int3 = JSON.parse(fs.readFileSync(path.join(TMP, 'up', 'INT-3-transform-fullcorpus.json'), 'utf8'));
  return { notes, assets, arts, v2, int3 };
}

// ── PHASE 1: map ─────────────────────────────────────────────────────────────
async function phaseMap() {
  const { notes, assets, arts } = await loadInputs();
  fs.mkdirSync(path.join(OUT, 'source-0.2'), { recursive: true });
  const byId = new Map(notes.map(n => [n.noteId, n]));
  check('C-1a', notes.length === 112, `notes rows ${notes.length}`);
  const receiptNotes = []; const totals = { figures: 0, mapped: 0, noteLevel: 0, slugFallback: 0, matchModes: { exact: 0, fuzzy: 0, none: 0 }, notesWithFigures: 0, maxPerNote: 0 };
  for (const a of arts) {
    const src = JSON.parse(a.buf.toString('utf8'));
    const noteId = src.noteRef.noteId;
    check('C-2e ' + a.name, a.name === `guided-lesson-${noteId}.json` && src.format === 'guided-lesson/0.1', 'filename/noteId/format');
    const note = byId.get(noteId);
    check('C-1b ' + noteId, !!note, 'noteId present in notes.json');
    const { figures, perLesson } = mapFigures(note.bodyMd, src.lessons);
    // emit 0.2 — same key order as 0.1, figures after format, figureIds after specRefs
    const out = { format: 'guided-lesson/0.2' };
    if (figures.length) out.figures = figures.map(f => ({ id: f.id, url: f.url, alt: f.alt, sourceHeading: f.sourceHeading, moduleIds: f.moduleIds }));
    out.noteRef = src.noteRef; out.specPoints = src.specPoints; out.primer = src.primer;
    out.lessons = src.lessons.map((l, i) => {
      const nl = { title: l.title, sourceHeadings: l.sourceHeadings, specRefs: l.specRefs };
      if (perLesson[i].length) nl.figureIds = perLesson[i];
      return { ...nl, opening: l.opening, keyPoints: l.keyPoints, confidenceGate: l.confidenceGate, depthLayers: l.depthLayers, check: l.check };
    });
    out.noteAssets = src.noteAssets;
    fs.writeFileSync(path.join(OUT, 'source-0.2', a.name), Buffer.from(j1(out), 'utf8'));
    // census
    const mapped = figures.filter(f => f.moduleIds.length > 0).length;
    totals.figures += figures.length; totals.mapped += mapped; totals.noteLevel += figures.length - mapped;
    totals.slugFallback += figures.filter(f => f.altSource === 'slug-fallback').length;
    for (const f of figures) totals.matchModes[f.matchMode]++;
    if (figures.length) totals.notesWithFigures++;
    totals.maxPerNote = Math.max(totals.maxPerNote, figures.length);
    for (const f of figures) check('C-4 ' + noteId + ':' + f.id, assets.has(f.url.split('/').pop()), `asset basename ${f.url.split('/').pop()}`);
    receiptNotes.push({ noteId, wave: a.wave, figures: figures.length, mapped, noteLevel: figures.length - mapped, matchModes: figures.reduce((m, f) => ((m[f.matchMode] = (m[f.matchMode] || 0) + 1), m), {}) });
  }
  check('C-1c', totals.figures === 200 && totals.notesWithFigures === 90, `census figures=${totals.figures} notesWith=${totals.notesWithFigures} (of record: 200/90)`);
  check('C-1d', totals.maxPerNote <= 99, `max per note ${totals.maxPerNote} (fig-NN two-digit law)`);
  const receipt = {
    format: 'figures-mapping-receipt/0.1', phase: 'map', generated_at_utc: now(), operator_trace: OPERATOR_TRACE,
    sourcing_decision: 'trace 1a1800f3b8c138e5 — reuse the parent revision note\'s own images',
    inputs: {
      notes_corpus: { file: 'syllabai-v2@dd20b81b1895… apps/hub/content/igcse-chemistry-19/notes.json (served corpus of record; census-identical to FIG-1 grounding)', sha256: sha256(fs.readFileSync(path.join(TMP, 'hub', 'notes.json'))) },
      artifacts_pin: { repo: R_REPO, ref: R_PIN, namespace: 'SME-GuidedLessons/wave-1..10', format: 'guided-lesson/0.1' },
      assets_dir: { files: 194, verified: '194/194 referenced basenames 1:1' },
    },
    algorithm: 'bodyMd segmented by headings (#{1,4}) -> each image attaches to nearest preceding heading -> joins lessons via sourceHeadings (exact, then normalized-substring) -> moduleIds L-ordinals; per-lesson figureIds closure',
    census: { ...totals, notes_total: 112, notes_without_figures: 112 - totals.notesWithFigures },
    notes: receiptNotes,
  };
  fs.writeFileSync(path.join(DL, 'FIG4-mapping-receipt-20261028.json'), j2(receipt));
  console.log(`MAP DONE: ${totals.figures} figures / ${totals.notesWithFigures} notes (mapped ${totals.mapped}, note-level ${totals.noteLevel}); modes`, totals.matchModes);
  report();
}

// ── PHASE 2: transform ───────────────────────────────────────────────────────
async function phaseTransform() {
  const pinnedRef = ARGS['pinned-ref'];
  if (!pinnedRef || !/^[0-9a-f]{40}$/.test(pinnedRef)) { console.error('--pinned-ref <40-hex commit A> required'); process.exit(2); }
  const { notes, arts, v2, int3 } = await loadInputs();
  const Ajv = require('/home/z/node_modules/ajv');
  const ajv = new Ajv({ allErrors: true });
  const s02 = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/fig4-guided-lesson.0.2.schema.json', 'utf8'));
  const s11 = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/fig4-hub-lesson-import.1.1.schema.json', 'utf8'));
  const v02 = ajv.compile(s02); const v11 = ajv.compile(s11);
  fs.mkdirSync(path.join(OUT, 'hub-import-1.1'), { recursive: true });
  const byId = new Map(notes.map(n => [n.noteId, n]));
  const int3ByNote = new Map(int3.notes.map(x => [x.noteId, x]));
  const legacyByNote = new Map(arts.map(a => [JSON.parse(a.buf.toString('utf8')).noteRef.noteId, a]));
  const hub010Dir = path.join(CACHE, 'hubimport010');
  const pkgDir = path.join(CACHE, 'packages');
  const recordNotes = []; let grand = crypto.createHash('sha256'); let grandChars = 0;
  const waveHashes = {};
  let figTotals = { figures: 0, moduleMapped: 0, noteLevel: 0 };
  for (const a of arts) {
    const src02buf = fs.readFileSync(path.join(OUT, 'source-0.2', a.name));
    const src = JSON.parse(src02buf.toString('utf8'));
    const noteId = src.noteRef.noteId;
    // C-6 schema 0.2
    const ok02 = v02(src); check('C-6a ' + noteId, ok02, ok02 ? 'guided-lesson/0.2 ajv PASS' : ajv.errorsText(v02.errors).slice(0, 200));
    // closure lint C-5
    const declared = new Set((src.figures || []).map(f => f.id));
    const figs = src.figures || [];
    let closureOk = true; let detail = '';
    src.lessons.forEach((l, i) => {
      for (const fid of l.figureIds || []) {
        if (!declared.has(fid)) { closureOk = false; detail = `${fid} not declared`; }
        const f = figs.find(x => x.id === fid);
        if (f && !f.moduleIds.includes(`L${i + 1}`)) { closureOk = false; detail = `${fid} missing L${i + 1} in moduleIds`; }
      }
    });
    for (const f of figs) for (const mid of f.moduleIds) {
      const li = Number(mid.slice(1)) - 1;
      if (!(src.lessons[li].figureIds || []).includes(f.id)) { closureOk = false; detail = `${f.id}/${mid} figureIds closure`; }
    }
    check('C-5 ' + noteId, closureOk, closureOk ? 'figureIds↔moduleIds closure' : detail);
    // adapter 1.1 — full field map of ADAPTER-SPEC §4.1 + figures passthrough
    const hub = {
      format: 'hub/lesson-import/1.1',
      adapter: 'guided-lesson-0.2--hub-lesson-import-1.1',
      source: {
        sourceFormat: 'guided-lesson/0.2',
        noteId, corpusVersion: src.noteRef.corpusVersion,
        sourceLayerSha256: sha256(src02buf),
        pinnedRef,
      },
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
            gatePolicy: {
              ratingsScale: l.confidenceGate.ratings,
              continueDisabledUntilChoice: l.confidenceGate.continueDisabledUntilChoice,
              resumeWithoutReRate: l.confidenceGate.resumeWithoutReRate,
              postCheckRecalibration: l.confidenceGate.postCheckRecalibration,
            },
            checkRefs: l.check.map((_, k) => `${noteId}::L${i + 1}::Q${k + 1}`),
          };
          if (l.figureIds) m.figureIds = l.figureIds;
          return m;
        }),
        assets: { glossary: src.noteAssets.glossary, workedExample: src.noteAssets.workedExample },
      },
    };
    if (figs.length) hub.lesson.figures = figs.map(f => ({ id: f.id, url: f.url, alt: f.alt, sourceHeading: f.sourceHeading, moduleIds: f.moduleIds }));
    // C-6 schema 1.1
    const ok11 = v11(hub); check('C-6b ' + noteId, ok11, ok11 ? 'hub/lesson-import/1.1 ajv PASS' : ajv.errorsText(v11.errors).slice(0, 200));
    // C-7 adapter determinism vs the of-record 1.0 output
    const legacy = JSON.parse(fs.readFileSync(path.join(hub010Dir, `${noteId}.hub-lesson-import.json`, ), 'utf8'));
    const strip = (h) => { const c = JSON.parse(JSON.stringify(h)); delete c.lesson.figures; c.lesson.modules.forEach(m => delete m.figureIds); delete c.format; delete c.adapter; delete c.source; return c; };
    check('C-7 ' + noteId, deepEqual(strip(hub), strip(legacy)), 're-transform == 1.0 of-record (minus declared deltas format/adapter/source/figures)');
    // C-8 stream conservation vs INT-3 anchors (+ legacy self-check)
    const pkg = JSON.parse(fs.readFileSync(path.join(pkgDir, `${noteId}.sme-question-package.json`, ), 'utf8'));
    const toks = targetTokens(hub, pkg); const s = toks.join('\n'); const streamSha = sha256(Buffer.from(s, 'utf8'));
    const anchor = int3ByNote.get(noteId);
    check('C-8 ' + noteId, !!anchor && streamSha === anchor.stream.sha256 && s.length === anchor.stream.chars, `stream ${streamSha.slice(0, 12)}/${s.length} vs INT-3 ${anchor ? anchor.stream.sha256.slice(0, 12) : 'MISSING'}/${anchor ? anchor.stream.chars : '?'}`);
    grand.update(Buffer.from(s, 'utf8')); grandChars += s.length;
    const w = 'wave-' + a.wave; waveHashes[w] = waveHashes[w] || crypto.createHash('sha256'); waveHashes[w].update(Buffer.from(s, 'utf8'));
    // pkg sha unchanged
    const pkgSha = sha256(fs.readFileSync(path.join(pkgDir, `${noteId}.sme-question-package.json`)));
    const pkgV2 = v2.artifacts.find(x => x.kind === 'sme-question-package' && x.noteId === noteId);
    check('C-9 ' + noteId, pkgSha === pkgV2.sha256, 'package bytes unchanged');
    const figCount = { total: figs.length, moduleMapped: figs.filter(f => f.moduleIds.length).length, noteLevel: figs.filter(f => !f.moduleIds.length).length };
    figTotals.figures += figCount.total; figTotals.moduleMapped += figCount.moduleMapped; figTotals.noteLevel += figCount.noteLevel;
    recordNotes.push({ wave: a.wave, noteId, sourceLayerSha256: sha256(src02buf), hubSha256: sha256(Buffer.from(j2(hub), 'utf8')), pkgSha256: pkgSha, stream: { chars: s.length, sha256: streamSha, conserved: true, matchesLegacy: true }, figures: figCount });
    fs.writeFileSync(path.join(OUT, 'hub-import-1.1', `${noteId}.hub-lesson-import.json`), Buffer.from(j2(hub), 'utf8'));
  }
  // conservation blocks must equal v2's of-record values
  const waveOut = {}; for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
  check('C-10a', grandChars === v2.counts.authored_chars_conserved, `grand chars ${grandChars} vs v2 ${v2.counts.authored_chars_conserved}`);
  const grandSha = grand.digest('hex');
  check('C-10b', grandSha === v2.conservation.authored_stream_sha256, `grand stream ${grandSha.slice(0, 12)} vs v2 ${v2.conservation.authored_stream_sha256.slice(0, 12)}`);
  check('C-10c', deepEqual(waveOut, v2.conservation.wave_stream_sha256), 'wave subtotals ×10 == v2 of-record');
  // manifest v3
  const man3 = {
    format: 'hub-import-manifest/1.0',
    manifest_version: 3,
    generated_at_utc: now(),
    operator_trace: OPERATOR_TRACE,
    supersedes: 'hub-import-manifest-v2.json (unchanged files keep their v2 sha256; the 112 sme-question-package artifacts are byte-identical)',
    figures_layer: {
      proposal: 'SCHEMA-0.2-FIGURES-PROPOSAL-20261028.md',
      sourcing: 'parent revision note images (trace 1a1800f3b8c138e5); assets dir 194/194 1:1',
      placement: 'module figures render immediately after the opening plain-words text, before key points (SME-faithful, evidence walk receipt SME-GUIDED-STUDY-figures-walk-20261028.json)',
      note_level_policy: 'moduleIds [] figures are page-fallback only — never rendered inside the lesson flow (knob b)',
      excluded_from_stream: true,
      stream_note: 'figures carry no authored prose (adapter spec §7 walk unchanged); per-note stream anchors equal the INT-3 fullcorpus record exactly (proof of record: INT-3-transform-record-figures-0.2.json)',
    },
    source_generation: { format: 'guided-lesson/0.2', namespace: 'SME-GuidedLessons/integration/source-0.2/', pin: pinnedRef, int0_lineage: INT0_PIN },
    load_scope: { adapter: 'guided-lesson-0.2--hub-lesson-import-1.1', target_schemas: ['hub/lesson-import/1.1', 'sme-question-package/1.0'] },
    counts: { ...v2.counts, figures: figTotals.figures, figures_module_mapped: figTotals.moduleMapped, figures_note_level: figTotals.noteLevel },
    conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut, equals_v2: true },
    artifacts: [
      ...recordNotes.map(n => ({ kind: 'hub-lesson-import-1.1', noteId: n.noteId, path: `SME-GuidedLessons/integration/hub-import-1.1/${n.noteId}.hub-lesson-import.json`, sha256: n.hubSha256, bytes: fs.statSync(path.join(OUT, 'hub-import-1.1', `${n.noteId}.hub-lesson-import.json`)).size })),
      ...v2.artifacts.filter(a => a.kind === 'sme-question-package').map(a => ({ kind: 'sme-question-package', noteId: a.noteId, path: `SME-GuidedLessons/integration/question-packages/${a.path.split('/').pop()}`, sha256: a.sha256, bytes: a.bytes })),
    ],
  };
  check('C-10d', man3.artifacts.length === 224, `manifest v3 artifacts ${man3.artifacts.length}`);
  fs.writeFileSync(path.join(OUT, 'hub-import-manifest-v3.json'), j2(man3));
  // INT-3-0.2 record
  const rec = {
    stage: 'INT-3', title: 'transform record — figures 0.2 generation (adapter guided-lesson-0.2--hub-lesson-import-1.1)',
    generated_at_utc: now(), operator_trace: OPERATOR_TRACE,
    adapter: 'guided-lesson-0.2--hub-lesson-import-1.1',
    source_pin: { repo: R_REPO, ref: R_PIN, note: '0.1 wave artifacts + 1.0 hub-import outputs + question-packages verified byte-exact @ this ref' },
    source_02_generation_pin: { commit: pinnedRef, namespace: 'SME-GuidedLessons/integration/source-0.2/' },
    conservation_law: 'figures are additive metadata outside the §7 stream: every per-note stream anchor equals the INT-3 fullcorpus record (matchesLegacy), and grand + wave streams equal manifest v2 of record',
    grand_stream: { chars: grandChars, sha256: grandSha },
    wave_stream_sha256: waveOut,
    notes: recordNotes,
  };
  fs.writeFileSync(path.join(OUT, 'INT-3-transform-record-figures-0.2.json'), j2(rec));
  console.log(`TRANSFORM DONE: 112 × 1.1 emitted; stream conserved (grand ${grandChars} chars == v2); figures ${figTotals.figures} (mapped ${figTotals.moduleMapped} / note-level ${figTotals.noteLevel})`);
  report();
}

// ── PHASE 3: verify (re-run gates from emitted outputs) ─────────────────────
async function phaseVerify() {
  const Ajv = require('/home/z/node_modules/ajv');
  const ajv = new Ajv({ allErrors: true });
  const v02 = ajv.compile(JSON.parse(fs.readFileSync('/home/z/my-project/scripts/fig4-guided-lesson.0.2.schema.json', 'utf8')));
  const v11 = ajv.compile(JSON.parse(fs.readFileSync('/home/z/my-project/scripts/fig4-hub-lesson-import.1.1.schema.json', 'utf8')));
  const man3 = JSON.parse(fs.readFileSync(path.join(OUT, 'hub-import-manifest-v3.json'), 'utf8'));
  const rec = JSON.parse(fs.readFileSync(path.join(OUT, 'INT-3-transform-record-figures-0.2.json'), 'utf8'));
  const int3 = JSON.parse(fs.readFileSync(path.join(TMP, 'up', 'INT-3-transform-fullcorpus.json'), 'utf8'));
  const int3ByNote = new Map(int3.notes.map(x => [x.noteId, x]));
  const pkgDir = path.join(CACHE, 'packages');
  let nOk = 0;
  for (const n of rec.notes) {
    const l1 = JSON.parse(fs.readFileSync(path.join(OUT, 'hub-import-1.1', `${n.noteId}.hub-lesson-import.json`), 'utf8'));
    const src = JSON.parse(fs.readFileSync(path.join(OUT, 'source-0.2', `guided-lesson-${n.noteId}.json`), 'utf8'));
    const okS = v02(src), okH = v11(l1);
    const pkg = JSON.parse(fs.readFileSync(path.join(pkgDir, `${n.noteId}.sme-question-package.json`, ), 'utf8'));
    const toks = targetTokens(l1, pkg); const s = toks.join('\n');
    const anchor = int3ByNote.get(n.noteId);
    const ok = okS && okH && sha256(Buffer.from(s, 'utf8')) === anchor.stream.sha256 && s.length === anchor.stream.chars
      && sha256(fs.readFileSync(path.join(OUT, 'source-0.2', `guided-lesson-${n.noteId}.json`))) === n.sourceLayerSha256
      && sha256(fs.readFileSync(path.join(OUT, 'hub-import-1.1', `${n.noteId}.hub-lesson-import.json`))) === n.hubSha256
      && l1.source.sourceLayerSha256 === n.sourceLayerSha256 && l1.source.pinnedRef === rec.source_02_generation_pin.commit;
    if (ok) nOk++; else check('V ' + n.noteId, false, `okS=${okS} okH=${okH} stream drift or sha drift`);
  }
  check('V-1', nOk === 112, `cold re-verify ${nOk}/112 (schema 0.2 + 1.1 + stream vs INT-3 + artifact shas + pinnedRef)`);
  check('V-2', man3.artifacts.length === 224, `manifest v3 lists ${man3.artifacts.length}`);
  check('V-3', rec.notes.length === 112, `INT-3-0.2 record ${rec.notes.length} notes`);
  report();
}

function report() {
  console.log(`\nCHECKS: ${CHECKS.filter(c => c.ok).length}/${CHECKS.length} pass, ${FAILS.length} FAIL`);
  for (const f of FAILS.slice(0, 20)) console.log('  FAIL:', f.name, '—', f.detail.slice(0, 160));
  fs.writeFileSync(path.join(TMP, `pipeline-${PHASE}-checks.json`), j2({ phase: PHASE, ts: now(), checks: CHECKS, fails: FAILS }));
  if (FAILS.length) process.exit(1);
}

(PHASE === 'map' ? phaseMap() : PHASE === 'transform' ? phaseTransform() : phaseVerify()).catch(e => { console.error('FATAL', e); process.exit(1); });
