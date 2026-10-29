#!/usr/bin/env node
// FIGURES-2.2 BINDING PIPELINE — deterministic concept-grain binding + adapter 1.3 transform of record.
//
//   phase=source                       fetch source-0.3 + hub-import-1.2 + packages @ RES_PIN,
//                                      compute the binding rule chain, emit source-0.4/ + both 1.3-era schemas
//   phase=transform --pinned-ref <sha> emit hub-import-1.3/ + manifest v6 + INT-3-figures-2.2 record
//                                      (needs commit A sha — the source-0.4 promotion commit)
//   phase=verify                       cold re-run of every gate from emitted bytes (fail-closed)
//
// Zero-DB, zero synthesis: the binding is a mechanical join of figure.sourceHeading ↔ lesson.sourceHeadings
// (rule 1 heading-exact-unique → rule 2 sole-lesson → rule 3 caption↔lesson-text token overlap, threshold of
// record top ≥ 2 AND margin ≥ 1), fail-closed to 'unresolved' which KEEPS the existing claims. Note-level
// figures (moduleIds []) are never rebound. Nothing is authored; the canonical authored stream (§7) is
// untouched by construction — proven per note against the figures-2.1 (captions, 1.2) of-record bytes.
//
// Operator trace: 1a1892c0212a94fd ("probe and execute" the queued FIGURES-2.2 concept-grain wave).
// Queue of record: download/FIGURES-2-2-CONCEPT-GRAIN-QUEUED-20261030.json.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const TMP = '/home/z/my-project/.tmp/fig22';
const OUT = path.join(TMP, 'out');
const CACHE = path.join(TMP, 'cache');
const TOKEN = fs.readFileSync('/home/z/my-project/.creds/gh-pat.candidate', 'utf8').trim();
const API = 'https://api.github.com';
const HDR = { Authorization: `Bearer ${TOKEN}`, Accept: 'application/vnd.github.raw', 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'fig22-pipeline' };
const HDR_JSON = { ...HDR, Accept: 'application/vnd.github+json' };
const R_REPO = 'SyllabAI/syllabai-resources';
const RES_PIN = process.env.FIG22_RES_PIN || '5586acae1627d965049bac92de1ea9d1cc70c42c'; // resources main @ wave open
const INT = 'SME-GuidedLessons/integration';
const INT0_PIN = '4d857c472fd725597ac21db189542c8f12c82dba';
const OPERATOR_TRACE = '1a1892c0212a94fd';
const sha256 = (b) => crypto.createHash('sha256').update(b).digest('hex');
const now = () => new Date().toISOString().replace(/\.\d+Z$/, 'Z');
const j1 = (o) => JSON.stringify(o, null, 1); // wave-artifact family convention: 1-space, no trailing NL
const j2 = (o) => JSON.stringify(o, null, 2) + '\n';
const deepEqual = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const clone = (o) => JSON.parse(JSON.stringify(o));

const CHECKS = []; const FAILS = [];
function check(name, ok, detail) {
  CHECKS.push({ name, ok: !!ok, detail: detail || '' });
  if (!ok) FAILS.push({ name, detail: detail || '' });
  return !!ok;
}
function report() {
  const bad = FAILS.length;
  console.log(`CHECKS: ${CHECKS.length - bad}/${CHECKS.length} pass, ${bad} fail`);
  for (const f of FAILS.slice(0, 20)) console.log(`  FAIL ${f.name} — ${f.detail}`);
  if (bad) process.exit(1);
}
const ARGS = {};
for (const a of process.argv.slice(2)) { const m = a.match(/^--([^=]+)=(.*)$/); if (m) ARGS[m[1]] = m[2]; else ARGS[a] = true; }
const PHASE = ARGS['phase'] || 'verify';

// ── pooled fetch with retry-once + disk cache ─────────────────────────────────
async function pooled(items, n, fn) {
  const out = new Array(items.length); let i = 0;
  await Promise.all(Array.from({ length: n }, async () => {
    while (i < items.length) { const idx = i++; out[idx] = await fn(items[idx], idx); }
  }));
  return out;
}
async function fetchRaw(rel, ref) {
  const cacheKey = path.join(CACHE, ref.slice(0, 8), rel.replace(/\//g, '__'));
  if (fs.existsSync(cacheKey)) return fs.readFileSync(cacheKey);
  const url = `${API}/repos/${R_REPO}/contents/${encodeURI(rel)}?ref=${ref}`;
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      const r = await fetch(url, { headers: HDR });
      if (r.ok) { const buf = Buffer.from(await r.arrayBuffer()); fs.mkdirSync(path.dirname(cacheKey), { recursive: true }); fs.writeFileSync(cacheKey, buf); return buf; }
      if (r.status === 404) throw new Error(`404 ${rel} @ ${ref.slice(0, 8)}`);
      if (attempt === 2) throw new Error(`HTTP ${r.status} for ${rel}`);
    } catch (e) { if (attempt === 2) throw e; }
    await new Promise((res) => setTimeout(res, 1500));
  }
}
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
async function fetchJson(rel) {
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      const r = await fetch(`${API}/repos/${R_REPO}/${rel}`, { headers: HDR_JSON });
      if (r.ok) return r.json();
      if (attempt === 2) throw new Error(`HTTP ${r.status} for ${rel}`);
    } catch (e) { if (attempt === 2) throw e; }
    await sleep(1500);
  }
}

// ── inputs ────────────────────────────────────────────────────────────────────
let _man5 = null;
async function man5() {
  if (_man5) return _man5;
  _man5 = JSON.parse((await fetchRaw(`${INT}/hub-import-manifest-v5.json`, RES_PIN)).toString('utf8'));
  return _man5;
}
async function noteIds() {
  const m = await man5();
  return m.artifacts.filter((a) => a.kind === 'hub-lesson-import-1.2').map((a) => a.noteId);
}
async function src03(noteId) {
  const buf = await fetchRaw(`${INT}/source-0.3/guided-lesson-${noteId}.json`, RES_PIN);
  return { buf, obj: JSON.parse(buf.toString('utf8')) };
}
async function hub12(noteId) {
  const buf = await fetchRaw(`${INT}/hub-import-1.2/${noteId}.hub-lesson-import.json`, RES_PIN);
  return { buf, obj: JSON.parse(buf.toString('utf8')) };
}
async function pkg(noteId) {
  const buf = await fetchRaw(`${INT}/question-packages/${noteId}.sme-question-package.json`, RES_PIN);
  return { buf, obj: JSON.parse(buf.toString('utf8')) };
}
// wave per note: the wave dirs are the intake grouping of record
async function waveMap() {
  const cacheKey = path.join(CACHE, 'wavemap.json');
  if (fs.existsSync(cacheKey)) return JSON.parse(fs.readFileSync(cacheKey, 'utf8'));
  const map = {};
  for (let w = 1; w <= 10; w++) {
    const listing = await fetchJson(`contents/SME-GuidedLessons/wave-${w}?ref=${RES_PIN}`);
    for (const e of listing) {
      const m = e.name.match(/^guided-lesson-(rn_[A-Za-z0-9]+)\.json$/);
      if (m) map[m[1]] = w;
    }
  }
  fs.writeFileSync(cacheKey, JSON.stringify(map));
  return map;
}

// ── canonical authored stream — target side, adapter spec §7 (verbatim walk) ──
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
  }
  return s;
}

// ── binding rule chain (deterministic; nothing authored) ─────────────────────
const STOP = new Set('the a an of in on and or is are to for with as by that this it its which from at be been was were has have had not no than then so such into one two first four used use using can may will would could show shows shown'.split(' '));
function tokens(s) {
  const out = new Set();
  for (const w of (s || '').toLowerCase().match(/[a-z0-9-]+/g) || []) {
    if (!STOP.has(w) && w.length > 2) out.add(w);
  }
  return out;
}
function lessonText(les) {
  // the teaching text a caption may overlap: title + keyPoints + opening + depthLayers (NOT checks)
  const parts = [les.title || ''];
  for (const k of les.keyPoints || []) parts.push(String(k));
  if (les.opening) parts.push(String(les.opening));
  const d = les.depthLayers || {};
  for (const key of Object.keys(d)) {
    const v = d[key] || {};
    for (const kk of Object.keys(v)) parts.push(String(v[kk]));
  }
  return parts.join(' ');
}
// threshold of record (fixed at wave open from the 112-file forecast census):
// elect content-overlap only if the winner scores ≥ 2 tokens AND beats the runner-up by ≥ 1.
function bindingFor(fig, lessons) {
  const mods = lessons.map((_, i) => `L${i + 1}`);
  if (!fig.moduleIds || fig.moduleIds.length === 0) return { binding: 'note-level', moduleIds: [] };
  const sh = fig.sourceHeading || null;
  const cands = sh ? mods.filter((_, i) => (lessons[i].sourceHeadings || []).includes(sh)) : [];
  if (cands.length === 1) return { binding: 'heading-unique', moduleIds: [cands[0]] };
  if (cands.length === 0 && lessons.length === 1) return { binding: 'sole-lesson', moduleIds: ['L1'] };
  if (cands.length >= 2 && fig.caption) {
    const ft = tokens(fig.caption);
    const scored = cands.map((id) => {
      const i = Number(id.slice(1)) - 1;
      const lt = tokens(lessonText(lessons[i]));
      return { id, n: [...ft].filter((t) => lt.has(t)).length };
    });
    scored.sort((a, b) => b.n - a.n || a.id.localeCompare(b.id));
    const top = scored[0]; const sec = scored[1];
    if (top.n >= 2 && (!sec || top.n - sec.n >= 1)) {
      return { binding: 'content-overlap', moduleIds: [top.id], score: { top: top.n, second: sec ? sec.n : null } };
    }
  }
  const reason = cands.length >= 2
    ? 'shared heading, no decisive caption signal'
    : (cands.length === 0 ? `heading not listed by any lesson's sourceHeadings (${lessons.length}-lesson note)` : 'overlap tie or below threshold');
  return { binding: 'unresolved', moduleIds: fig.moduleIds.slice(), reason };
}
const FIG_KEY_ORDER_04 = ['id', 'url', 'alt', 'sourceHeading', 'caption', 'binding', 'moduleIds'];
const FIG_KEY_ORDER_12 = ['id', 'url', 'alt', 'sourceHeading', 'caption', 'moduleIds'];

// ── schema derivation (mechanical bumps of the of-record 0.3 / 1.2 schemas) ──
function derive04Schema(s03) {
  const s = JSON.parse(JSON.stringify(s03));
  s.$id = 'guided-lesson/0.4';
  s.properties.format.const = 'guided-lesson/0.4';
  s.properties.figures.items.properties.binding = {
    type: 'string',
    enum: ['heading-unique', 'sole-lesson', 'content-overlap', 'note-level', 'unresolved'],
    description: 'Which guided lesson teaches this diagram, and by which rule: heading-unique = sourceHeading listed by exactly one lesson; sole-lesson = single-lesson note; content-overlap = caption token overlap vs lesson teaching text (threshold of record: top ≥ 2 AND margin ≥ 1); note-level = moduleIds [] page-fallback; unresolved = fail-closed keep of the existing claims. Figures-2.2 binding layer; nothing authored.',
  };
  // declared delta: narrowing may legitimately leave a lesson with zero bound diagrams
  if (s.properties.lessons && s.properties.lessons.items && s.properties.lessons.items.properties && s.properties.lessons.items.properties.figureIds) {
    s.properties.lessons.items.properties.figureIds.minItems = 0;
  }
  return s;
}
function derive13Schema(s12) {
  const s = JSON.parse(JSON.stringify(s12));
  s.$id = 'hub/lesson-import/1.3';
  s.properties.format.const = 'hub/lesson-import/1.3';
  s.properties.adapter.const = 'guided-lesson-0.4--hub-lesson-import-1.3';
  s.definitions.sourceBlock.properties.sourceFormat.const = 'guided-lesson/0.4';
  const fig = s.properties.lesson.properties.figures.items;
  fig.properties.binding = {
    type: 'string',
    enum: ['heading-unique', 'sole-lesson', 'content-overlap', 'note-level', 'unresolved'],
    description: 'Verbatim passthrough of the source figure binding provenance (figures-2.2 binding layer).',
  };
  // declared delta: narrowing may legitimately leave a module with zero bound diagrams
  // (modules may be inline OR a $ref to definitions.module — relax wherever the constraint lives)
  const modInline = s.properties.lesson.properties.modules.items;
  if (modInline && modInline.properties && modInline.properties.figureIds) modInline.properties.figureIds.minItems = 0;
  const modDef = s.definitions && s.definitions.module;
  if (modDef && modDef.properties && modDef.properties.figureIds) modDef.properties.figureIds.minItems = 0;
  return s;
}


// ═══════════════════ phases (source / transform / verify) ═══════════════════
// (merged of-record copy: scripts/fig22-common.js + scripts/fig22-pipeline.js)
// FIGURES-2.2 phases (source / transform / verify) — consumes fig22-common.js.

// rebuild a figure object in canonical key order
function figIn(fig, order) {
  const g = {};
  for (const k of order) if (fig[k] !== undefined) g[k] = fig[k];
  return g;
}

// ── PHASE 1: source (binding rule chain into source-0.4) ─────────────────────
async function phaseSource() {
  fs.mkdirSync(path.join(OUT, 'source-0.4'), { recursive: true });
  fs.mkdirSync(path.join(OUT, 'schema'), { recursive: true });
  const m5 = await man5();
  const ids = await noteIds();
  check('C-1a', ids.length === 112, `notes ${ids.length} == manifest v5 lesson artifacts`);
  // schemas: mechanical derivation from the of-record 0.3 / 1.2 schemas @ pin
  const s03raw = await fetchRaw(`${INT}/schema/guided-lesson.0.3.schema.json`, RES_PIN);
  const s12raw = await fetchRaw(`${INT}/schema/hub-lesson-import.1.2.schema.json`, RES_PIN);
  const s04 = derive04Schema(JSON.parse(s03raw.toString('utf8')));
  const s13 = derive13Schema(JSON.parse(s12raw.toString('utf8')));
  fs.writeFileSync(path.join(OUT, 'schema', 'guided-lesson.0.4.schema.json'), j2(s04));
  fs.writeFileSync(path.join(OUT, 'schema', 'hub-lesson-import.1.3.schema.json'), j2(s13));
  check('C-1b', !!s04.properties.figures.items.properties.binding && s04.properties.figures.items.additionalProperties === false && s04.properties.format.const === 'guided-lesson/0.4', '0.4 schema carries optional binding, still closed');
  check('C-1c', !!s13.properties.lesson.properties.figures.items.properties.binding && s13.definitions.sourceBlock.properties.sourceFormat.const === 'guided-lesson/0.4' && s13.properties.adapter.const === 'guided-lesson-0.4--hub-lesson-import-1.3', '1.3 schema carries optional binding + bumped consts');
  const waves = await waveMap();
  const census = { 'heading-unique': 0, 'sole-lesson': 0, 'content-overlap': 0, 'note-level': 0, unresolved: 0, figuresTotal: 0, moduleMapped: 0, notesWithFigures: 0, narrowed: 0, claimChangingNarrowed: 0, wholesaleKept: 0 };
  const rows = [];
  await pooled(ids, 6, async (noteId) => {
    const s = await src03(noteId);
    check(`C-2a ${noteId}`, s.obj.format === 'guided-lesson/0.3', `source-0.3 format @ ${RES_PIN.slice(0, 8)}`);
    const h = await hub12(noteId);
    check(`C-2b ${noteId}`, h.obj.source.sourceLayerSha256 === sha256(s.buf), `1.2 sourceLayerSha256 == sha256(source-0.3 bytes) — upstream fidelity`);
    const src04 = clone(s.obj);
    src04.format = 'guided-lesson/0.4';
    const lessons = s.obj.lessons || [];
    const figs = s.obj.figures || [];
    if (figs.length) census.notesWithFigures++;
    const newFigs = figs.map((f) => {
      const r = bindingFor(f, lessons);
      census[r.binding] = (census[r.binding] || 0) + 1;
      census.figuresTotal++;
      if ((f.moduleIds || []).length) census.moduleMapped++;
      const from = JSON.parse(JSON.stringify(f.moduleIds || []));
      const g = figIn({ ...f, binding: r.binding, moduleIds: r.moduleIds }, FIG_KEY_ORDER_04);
      if ((f.moduleIds || []).length) {
        // of-record row for EVERY module-mapped figure (from may equal to for verification-only binds)
        rows.push({ noteId, fig: f.id, binding: r.binding, from, to: r.moduleIds, score: r.score || null, reason: r.reason || null });
        if (r.binding !== 'unresolved' && r.binding !== 'note-level') census.narrowed++;
        if (r.binding !== 'unresolved' && r.binding !== 'note-level' && from.length > 1) census.claimChangingNarrowed++;
        if (r.binding === 'unresolved' && from.length > 1) census.wholesaleKept++;
      }
      return g;
    });
    if (figs.length) src04.figures = newFigs;
    // lessons[].figureIds recompute (only where the key exists; preserve insertion order)
    for (let i = 0; i < lessons.length; i++) {
      const lid = `L${i + 1}`;
      if ('figureIds' in lessons[i]) {
        src04.lessons[i].figureIds = newFigs.filter((f) => (f.moduleIds || []).includes(lid)).map((f) => f.id);
      }
    }
    // D-1 determinism: 0.4 == 0.3 minus declared deltas (format, figures[].binding+moduleIds, lessons[].figureIds)
    const strip = clone(src04);
    strip.format = 'guided-lesson/0.3';
    if ('figures' in s.obj) strip.figures = clone(s.obj.figures); else delete strip.figures;
    for (let i = 0; i < lessons.length; i++) if ('figureIds' in lessons[i]) strip.lessons[i].figureIds = clone(lessons[i].figureIds);
    check(`D-1 ${noteId}`, deepEqual(strip, s.obj), 'source-0.4 == source-0.3 minus declared deltas');
    // C-3 binding recompute determinism from the emitted object
    const recomp = (src04.figures || []).map((f) => bindingFor(f, src04.lessons || []));
    const recEq = recomp.length === (src04.figures || []).length && recomp.every((r, i) => r.binding === src04.figures[i].binding && deepEqual(r.moduleIds, src04.figures[i].moduleIds));
    check(`C-3 ${noteId}`, recEq, 'binding rule chain recomputes identically from emitted 0.4');
    const buf = Buffer.from(j1(src04), 'utf8');
    fs.writeFileSync(path.join(OUT, 'source-0.4', `guided-lesson-${noteId}.json`), buf);
  });
  check('C-1d', waves && Object.keys(waves).length >= 100, 'wave map fetched');
  fs.writeFileSync(path.join(OUT, 'binding-census.json'), j2({ generated_at_utc: now(), operator_trace: OPERATOR_TRACE, source_pin: RES_PIN, census, rows }));
  console.log(`SOURCE DONE: 112 × source-0.4 emitted; figures ${census.figuresTotal} across ${census.notesWithFigures} notes; census ${JSON.stringify(census)}`);
  report();
}

// ── PHASE 2: transform (--pinned-ref <commit A>) ─────────────────────────────
async function phaseTransform() {
  const pinnedRef = ARGS['pinned-ref'];
  if (!pinnedRef || !/^[0-9a-f]{40}$/.test(pinnedRef)) { console.error('--pinned-ref <40-hex commit A> required'); process.exit(2); }
  fs.mkdirSync(path.join(OUT, 'hub-import-1.3'), { recursive: true });
  const m5 = await man5();
  const ids = await noteIds();
  const Ajv = new (require('/home/z/node_modules/ajv'))({ allErrors: true, strict: false });
  const s13 = JSON.parse(fs.readFileSync(path.join(OUT, 'schema', 'hub-lesson-import.1.3.schema.json'), 'utf8'));
  const s04 = JSON.parse(fs.readFileSync(path.join(OUT, 'schema', 'guided-lesson.0.4.schema.json'), 'utf8'));
  const pkgSchemaRaw = await fetchRaw(`${INT}/schema/sme-question-package.1.0.schema.json`, RES_PIN);
  const v13 = Ajv.compile(s13); const v04 = Ajv.compile(s04); const vPkg = Ajv.compile(JSON.parse(pkgSchemaRaw.toString('utf8')));
  const census = JSON.parse(fs.readFileSync(path.join(OUT, 'binding-census.json'), 'utf8'));
  const waves = await waveMap();
  const perNote = new Map(); // noteId → computed record (hash accumulation MUST be sequential, manifest order)
  await pooled(ids, 6, async (noteId) => {
    const s04buf = fs.readFileSync(path.join(OUT, 'source-0.4', `guided-lesson-${noteId}.json`));
    const src04 = JSON.parse(s04buf.toString('utf8'));
    const h = await hub12(noteId);
    const p = await pkg(noteId);
    // mutate 1.2 bytes → 1.3: declared deltas ONLY (format, adapter, source block, figures[].binding+moduleIds, modules[].figureIds)
    const hub13 = JSON.parse(h.buf.toString('utf8'));
    hub13.format = 'hub/lesson-import/1.3';
    hub13.adapter = 'guided-lesson-0.4--hub-lesson-import-1.3';
    hub13.source = {
      sourceFormat: 'guided-lesson/0.4', noteId, corpusVersion: hub13.source.corpusVersion,
      sourceLayerSha256: sha256(s04buf), pinnedRef,
    };
    const figs04 = src04.figures || [];
    if (figs04.length) {
      const byId04 = new Map(figs04.map((f) => [f.id, f]));
      hub13.lesson.figures = (hub13.lesson.figures || []).map((f) => {
        const src = byId04.get(f.id);
        return figIn(src || f, FIG_KEY_ORDER_04);
      });
      // cross-layer passthrough: 1.3 figures == source-0.4 figures
      check(`C-2c ${noteId}`, deepEqual(hub13.lesson.figures, figs04), '1.3 figures == source-0.4 figures (passthrough)');
    } else {
      check(`C-2c ${noteId}`, !hub13.lesson.figures, 'no figures either layer');
    }
    // modules[].figureIds recompute from figure.moduleIds (only where the key exists)
    const figs13 = hub13.lesson.figures || [];
    hub13.lesson.modules.forEach((mod, i) => {
      if ('figureIds' in mod) {
        mod.figureIds = figs13.filter((f) => (f.moduleIds || []).includes(`L${i + 1}`)).map((f) => f.id);
      }
    });
    const ok13 = v13(hub13); const ok04 = v04(src04);
    check(`C-6a ${noteId}`, ok04, ok04 ? 'guided-lesson/0.4 ajv PASS' : JSON.stringify(v04.errors).slice(0, 240));
    check(`C-6b ${noteId}`, ok13, ok13 ? 'hub/lesson-import/1.3 ajv PASS' : JSON.stringify(v13.errors).slice(0, 240));
    const okPkg = vPkg(p.obj);
    check(`C-6c ${noteId}`, okPkg, okPkg ? 'sme-question-package/1.0 ajv PASS' : JSON.stringify(vPkg.errors).slice(0, 200));
    // D-2 determinism: 1.3 == 1.2 minus declared deltas
    const strip = clone(hub13);
    strip.format = 'hub/lesson-import/1.2'; strip.adapter = 'guided-lesson-0.3--hub-lesson-import-1.2';
    strip.source = { ...h.obj.source };
    if (h.obj.lesson.figures) strip.lesson.figures = h.obj.lesson.figures.map((f) => clone(f));
    else delete strip.lesson.figures;
    strip.lesson.modules.forEach((mod, i) => { if ('figureIds' in mod) mod.figureIds = clone(h.obj.lesson.modules[i].figureIds); });
    check(`D-2 ${noteId}`, deepEqual(strip, h.obj), '1.3 == 1.2 minus declared deltas (format/adapter/source/binding/moduleIds/figureIds)');
    // C-5 closure (new semantics): figureIds ↔ moduleIds closure both ways
    const declared = new Set(figs13.map((f) => f.id));
    let closureOk = true; let det = '';
    hub13.lesson.modules.forEach((mod, i) => {
      for (const fid of mod.figureIds || []) {
        if (!declared.has(fid)) { closureOk = false; det = `${fid} undeclared`; }
        const f = figs13.find((x) => x.id === fid);
        if (f && !f.moduleIds.includes(`L${i + 1}`)) { closureOk = false; det = `${fid} missing L${i + 1}`; }
      }
    });
    for (const f of figs13) for (const mid of f.moduleIds) {
      const li = Number(mid.slice(1)) - 1;
      if (!(hub13.lesson.modules[li].figureIds || []).includes(f.id)) { closureOk = false; det = `${f.id}/${mid} closure`; }
    }
    check(`C-5 ${noteId}`, closureOk, closureOk ? 'figureIds↔moduleIds closure holds (narrowed)' : det);
    // C-4 binding invariants: narrowed → single; unresolved → original claims kept
    const rowsById = new Map(census.rows.map((r) => [`${r.noteId}/${r.fig}`, r]));
    let invOk = true; let invDet = '';
    for (const f of figs13) {
      if (!f.moduleIds.length) continue; // note-level: no binding row, never rebound
      const row = rowsById.get(`${noteId}/${f.id}`);
      if (!row) { invOk = false; invDet = `${f.id} missing census row`; continue; }
      if (['heading-unique', 'sole-lesson', 'content-overlap'].includes(f.binding) && f.moduleIds.length !== 1) { invOk = false; invDet = `${f.id} narrowed but multi`; }
      if (f.binding === 'unresolved' && !deepEqual(f.moduleIds, row.from)) { invOk = false; invDet = `${f.id} unresolved claims not kept`; }
      if (!deepEqual(f.moduleIds, row.to)) { invOk = false; invDet = `${f.id} moduleIds != census row`; }
    }
    check(`C-4 ${noteId}`, invOk, invOk ? 'binding invariants hold' : invDet);
    // C-8 stream: 1.3 vs 1.2 — binding/moduleIds are not §7 tokens (hash accumulation happens later, in manifest order)
    const toks13 = targetTokens(hub13, p.obj); const s13j = toks13.join('\n');
    const toks12 = targetTokens(h.obj, p.obj); const s12j = toks12.join('\n');
    const sha13 = sha256(Buffer.from(s13j, 'utf8')); const sha12 = sha256(Buffer.from(s12j, 'utf8'));
    check(`C-8 ${noteId}`, sha13 === sha12 && s13j.length === s12j.length, `stream conserved 1.3==1.2 (${s13j.length} chars)`);
    // C-9 packages byte-identical to manifest v5 pins
    const v5pkg = m5.artifacts.find((a) => a.kind === 'sme-question-package' && a.noteId === noteId);
    check(`C-9 ${noteId}`, sha256(p.buf) === v5pkg.sha256 && p.buf.length === v5pkg.bytes, 'package bytes unchanged');
    const buf = Buffer.from(j2(hub13), 'utf8');
    fs.writeFileSync(path.join(OUT, 'hub-import-1.3', `${noteId}.hub-lesson-import.json`), buf);
    const figCount = {
      total: figs13.length,
      moduleMapped: figs13.filter((f) => f.moduleIds.length).length,
      noteLevel: figs13.filter((f) => !f.moduleIds.length).length,
      captioned: figs13.filter((f) => f.caption).length,
      wholesale: figs13.filter((f) => f.moduleIds.length > 1).length,
      binding: figs13.reduce((acc, f) => { acc[f.binding] = (acc[f.binding] || 0) + 1; return acc; }, {}),
    };
    perNote.set(noteId, { s13j, buf, figCount, wavesNote: waves[noteId], pkgSha: sha256(p.buf) });
  });
  // sequential hash accumulation in manifest-artifact order (v5 of-record accumulation order)
  let grand = crypto.createHash('sha256'); let grandChars = 0;
  const waveHashes = {}; const recordNotes = [];
  for (const noteId of ids) {
    const pn = perNote.get(noteId);
    grand.update(Buffer.from(pn.s13j, 'utf8')); grandChars += pn.s13j.length;
    const w = 'wave-' + pn.wavesNote; waveHashes[w] = waveHashes[w] || crypto.createHash('sha256'); waveHashes[w].update(Buffer.from(pn.s13j, 'utf8'));
    recordNotes.push({ wave: pn.wavesNote, noteId, sourceLayerSha256: sha256(fs.readFileSync(path.join(OUT, 'source-0.4', `guided-lesson-${noteId}.json`))), hubSha256: sha256(pn.buf), pkgSha256: pn.pkgSha, stream: { chars: pn.s13j.length, sha256: sha256(Buffer.from(pn.s13j, 'utf8')), conserved: true, matches12: true }, figures: pn.figCount });
  }
  const waveOut = {}; for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
  const grandSha = grand.digest('hex');
  check('C-10a', grandChars === m5.counts.authored_chars_conserved, `grand chars ${grandChars} vs v5 ${m5.counts.authored_chars_conserved}`);
  check('C-10b', grandSha === m5.conservation.authored_stream_sha256, `grand stream == v5 of record`);
  check('C-10c', deepEqual(waveOut, m5.conservation.wave_stream_sha256), 'wave subtotals ×10 == v5 of-record');
  check('C-10d', recordNotes.length === 112, `record notes ${recordNotes.length}`);
  const c = census.census;
  const wholesaleTotal = recordNotes.reduce((a, n) => a + (n.figures.wholesale || 0), 0);
  check('C-10e', wholesaleTotal === c.wholesaleKept && c.wholesaleKept === 2, `wholesale claims ${wholesaleTotal} == 2 unresolved keeps (was 14)`);
  check('C-10f', c.claimChangingNarrowed === 12 && c.wholesaleKept === 2, `claim-changing narrows ${c.claimChangingNarrowed} == 12 forecast; wholesale kept ${c.wholesaleKept} == 2 (was 14)`);
  // manifest v6
  const man6 = {
    format: 'hub-import-manifest/1.0',
    manifest_version: 6,
    generated_at_utc: now(),
    operator_trace: OPERATOR_TRACE,
    supersedes: 'hub-import-manifest-v5.json (the 112 sme-question-package artifacts stay byte-identical; all 112 hub-lesson-import artifacts re-pin to the figures-2.2 binding generation — hub/lesson-import/1.3, additive optional figures[].binding + concept-grain moduleIds/figureIds narrowing)',
    worked_examples_layer: m5.worked_examples_layer,
    captions_layer: m5.captions_layer,
    binding_layer: {
      wave: 'FIGURES-2.2 concept-grain binding (operator trace 1a1892c0212a94fd)',
      derivation: 'each diagram binds to the specific guided lesson that teaches it, mechanically: (1) heading-unique — figure.sourceHeading listed by exactly one lesson\'s sourceHeadings; (2) sole-lesson — single-lesson note; (3) content-overlap — caption token overlap vs the lesson teaching text (title + keyPoints + opening + depthLayers), threshold of record top ≥ 2 AND margin ≥ 1; (4) note-level — moduleIds [] stay page-fallback; (5) unresolved — fail-closed keep of the existing claims. Nothing is authored.',
      fail_closed: 'unresolved rows keep their existing moduleIds/figureIds and carry binding:"unresolved" (2 of 14 former wholesale claims; renderer unchanged for them)',
      placement: 'unchanged from adapter spec 0.3→1.2 §6 — caption-first after key points; the narrowing only changes WHICH guided lesson renders each diagram (module.figureIds narrowed in lockstep with figure.moduleIds)',
      excluded_from_stream: true,
      stream_note: 'moduleIds/figureIds/binding are not §7 stream tokens: per-note stream anchors equal the figures-2.1 (captions, 1.2) generation exactly (proof of record: INT-3-transform-record-figures-2.2.json, matches12 ×112)',
    },
    source_generation: { format: 'guided-lesson/0.4', namespace: `${INT}/source-0.4/`, pin: pinnedRef, int0_lineage: INT0_PIN },
    load_scope: { adapter: 'guided-lesson-0.4--hub-lesson-import-1.3', target_schemas: ['hub/lesson-import/1.3', 'sme-question-package/1.0'] },
    counts: { ...m5.counts, binding_heading_unique: c['heading-unique'], binding_sole_lesson: c['sole-lesson'], binding_content_overlap: c['content-overlap'], binding_note_level: c['note-level'], binding_unresolved: c.unresolved, figures_binding_narrowed: c.narrowed, figures_claims_changed: c.claimChangingNarrowed, figures_wholesale_claims_kept: c.wholesaleKept },
    conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut, equals_v5: true, equals_v4: true },
    artifacts: [
      ...recordNotes.map((n) => { const f = path.join(OUT, 'hub-import-1.3', `${n.noteId}.hub-lesson-import.json`); return { kind: 'hub-lesson-import-1.3', noteId: n.noteId, path: `${INT}/hub-import-1.3/${n.noteId}.hub-lesson-import.json`, sha256: n.hubSha256, bytes: fs.statSync(f).size }; }),
      ...m5.artifacts.filter((a) => a.kind === 'sme-question-package').map((a) => ({ kind: 'sme-question-package', noteId: a.noteId, path: `${INT}/question-packages/${a.path.split('/').pop()}`, sha256: a.sha256, bytes: a.bytes })),
    ],
  };
  check('C-10g', man6.artifacts.length === 224, `manifest v6 artifacts ${man6.artifacts.length}`);
  fs.writeFileSync(path.join(OUT, 'hub-import-manifest-v6.json'), j2(man6));
  // INT-3 record (runner survivor shape: notes[].stream/hubSha256/pkgSha256/wave)
  const rec = {
    stage: 'INT-3', title: 'transform record — figures 2.2 binding generation (adapter guided-lesson-0.4--hub-lesson-import-1.3)',
    generated_at_utc: now(), operator_trace: OPERATOR_TRACE,
    adapter: 'guided-lesson-0.4--hub-lesson-import-1.3',
    source_pin: { repo: 'SyllabAI/syllabai-resources', ref: RES_PIN, note: 'figures-2.1 captions generation (1.2 outputs + packages + manifest v5 + schemas) verified byte-exact @ this ref' },
    source_04_generation_pin: { commit: pinnedRef, namespace: `${INT}/source-0.4/` },
    conservation_law: 'binding/moduleIds/figureIds are not §7 stream tokens: every per-note stream anchor equals the figures-2.1 (captions, 1.2) generation exactly (matches12), and grand + wave streams equal manifest v5 of record',
    grand_stream: { chars: grandChars, sha256: grandSha },
    wave_stream_sha256: waveOut,
    binding_census: census,
    notes: recordNotes,
  };
  fs.writeFileSync(path.join(OUT, 'INT-3-transform-record-figures-2.2.json'), j2(rec));
  console.log(`TRANSFORM DONE: 112 × 1.3 emitted; stream conserved (grand ${grandChars} chars == v5); narrowed ${c.narrowed}, wholesale kept ${wholesaleTotal}, binding census ${JSON.stringify({ 'heading-unique': c['heading-unique'], 'sole-lesson': c['sole-lesson'], 'content-overlap': c['content-overlap'], 'note-level': c['note-level'], unresolved: c.unresolved })}`);
  report();
}

// ── PHASE 3: verify (cold re-run from emitted outputs) ───────────────────────
async function phaseVerify() {
  const m5 = await man5();
  const ids = m5.artifacts.filter((a) => a.kind === 'hub-lesson-import-1.2').map((a) => a.noteId);
  const Ajv = new (require('/home/z/node_modules/ajv'))({ allErrors: true, strict: false });
  const s04 = JSON.parse(fs.readFileSync(path.join(OUT, 'schema', 'guided-lesson.0.4.schema.json'), 'utf8'));
  const s13 = JSON.parse(fs.readFileSync(path.join(OUT, 'schema', 'hub-lesson-import.1.3.schema.json'), 'utf8'));
  const v04 = Ajv.compile(s04); const v13 = Ajv.compile(s13);
  const man6 = JSON.parse(fs.readFileSync(path.join(OUT, 'hub-import-manifest-v6.json'), 'utf8'));
  const rec = JSON.parse(fs.readFileSync(path.join(OUT, 'INT-3-transform-record-figures-2.2.json'), 'utf8'));
  const census = JSON.parse(fs.readFileSync(path.join(OUT, 'binding-census.json'), 'utf8'));
  let grand = crypto.createHash('sha256'); let grandChars = 0; const waveHashes = {};
  const cold = new Map();
  let wholesale = 0; let narrowed = 0;
  await pooled(ids, 6, async (noteId) => {
    const b04 = fs.readFileSync(path.join(OUT, 'source-0.4', `guided-lesson-${noteId}.json`));
    const b13 = fs.readFileSync(path.join(OUT, 'hub-import-1.3', `${noteId}.hub-lesson-import.json`));
    const o04 = JSON.parse(b04.toString('utf8')); const o13 = JSON.parse(b13.toString('utf8'));
    check(`V-schema04 ${noteId}`, v04(o04), 'guided-lesson/0.4 ajv PASS (cold)');
    check(`V-schema13 ${noteId}`, v13(o13), 'hub/lesson-import/1.3 ajv PASS (cold)');
    const manA = man6.artifacts.find((a) => a.kind === 'hub-lesson-import-1.3' && a.noteId === noteId);
    check(`V-sha ${noteId}`, sha256(b13) === manA.sha256 && b13.length === manA.bytes, 'disk bytes == manifest v6 pin');
    const recN = rec.notes.find((n) => n.noteId === noteId);
    check(`V-int ${noteId}`, recN && recN.hubSha256 === sha256(b13) && recN.sourceLayerSha256 === sha256(b04), 'INT record anchors == disk');
    check(`V-pin ${noteId}`, o13.source.pinnedRef === man6.source_generation.pin && o13.source.sourceFormat === 'guided-lesson/0.4', 'pinnedRef/sourceFormat wiring');
    // cold binding recompute from emitted 0.4
    for (const f of o04.figures || []) {
      const r = bindingFor(f, o04.lessons || []);
      check(`V-bind ${noteId}/${f.id}`, r.binding === f.binding && deepEqual(r.moduleIds, f.moduleIds), 'binding recomputes from emitted bytes (cold)');
      if (f.moduleIds.length > 1) wholesale++;
      if (['heading-unique', 'sole-lesson', 'content-overlap'].includes(f.binding)) narrowed++;
    }
    const p = await pkg(noteId);
    const toks = targetTokens(o13, p.obj); const s = toks.join('\n');
    check(`V-stream ${noteId}`, sha256(Buffer.from(s, 'utf8')) === recN.stream.sha256 && s.length === recN.stream.chars, 'stream anchor recompute (cold)');
    cold.set(noteId, { s, wave: recN.wave });
  });
  for (const noteId of ids) {
    const cc = cold.get(noteId);
    grand.update(Buffer.from(cc.s, 'utf8')); grandChars += cc.s.length;
    const w = 'wave-' + cc.wave; waveHashes[w] = waveHashes[w] || crypto.createHash('sha256'); waveHashes[w].update(Buffer.from(cc.s, 'utf8'));
  }
  const waveOut = {}; for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
  check('V-grand', grandChars === man6.counts.authored_chars_conserved && grand.digest('hex') === man6.conservation.authored_stream_sha256, `grand ${grandChars}`);
  check('V-waves', deepEqual(waveOut, man6.conservation.wave_stream_sha256), 'wave subtotals ×10 (cold)');
  check('V-counts', man6.artifacts.length === 224, 'manifest v6 lists 224');
  check('V-binding', wholesale === census.census.wholesaleKept && narrowed === census.census.narrowed, `cold wholesale ${wholesale} + narrowed ${narrowed} == census of record`);
  console.log(`VERIFY DONE: cold gates from disk — grand ${grandChars} chars conserved; wholesale kept ${wholesale}, narrowed ${narrowed}`);
  report();
}

(async () => {
  fs.mkdirSync(CACHE, { recursive: true });
  if (PHASE === 'source') await phaseSource();
  else if (PHASE === 'transform') await phaseTransform();
  else if (PHASE === 'verify') await phaseVerify();
  else { console.error(`unknown phase "${PHASE}" — source|transform|verify`); process.exit(2); }
})().catch((e) => { console.error('PIPELINE ABORTED:', e && (e.stack || e.message || e)); process.exit(1); });
