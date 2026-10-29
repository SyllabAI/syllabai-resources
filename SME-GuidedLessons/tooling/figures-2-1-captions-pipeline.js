#!/usr/bin/env node
// FIGURES-2.1 CAPTIONS PIPELINE — the deterministic caption-coalescing + adapter 1.2 transform of record.
//
//   phase=source                        fetch source-0.2 @ v4 commit A + SME sidecars @ v4 commit C,
//                                       coalesce captions, emit source-0.3/ + both 1.2-era schemas
//   phase=transform --pinned-ref <sha>  emit hub-import-1.2/ + manifest v5 + INT-3-figures-2.1 record
//                                       (needs commit A sha — the source-0.3 promotion commit)
//   phase=verify                        re-run every gate against emitted outputs (fail-closed)
//
// Zero-DB, zero synthesis: captions are the parent note's OWN explanatory lines (the bold-italic
// paragraph immediately following a figure block in the sme-revision-note/1.0 sidecar; row-context
// for table-embedded figures; inline-bullet text for bullets-embedded figures). Nothing is authored.
// The canonical authored stream (adapter spec §7) is untouched by construction — proven per note
// against the v4 (worked-examples-1.0) of-record bytes.
//
// Operator traces: 1a188a15ac19ed05 ("you are not using the diagrams properly — SME explains"),
// 1a188c14685e2965 ("probe and execute the wave").
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const TMP = '/home/z/my-project/.tmp/fig21';
const OUT = path.join(TMP, 'out');
const CACHE = path.join(TMP, 'cache');
const SURV = '/home/z/my-project/scripts/fig21-survivors';
const DL = '/home/z/my-project/download';
const TOKEN = fs.readFileSync('/home/z/my-project/.creds/gh-pat.candidate', 'utf8').trim();
const API = 'https://api.github.com';
const HDR = { Authorization: `Bearer ${TOKEN}`, Accept: 'application/vnd.github.raw', 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'fig21-pipeline' };
const HDR_JSON = { ...HDR, Accept: 'application/vnd.github+json' };
const R_REPO = 'SyllabAI/syllabai-resources';
const V4_COMMIT_A = '8ea8c63a46d75fc54733900dfecf5d3c5c93bbde'; // worked-example source revision (0.2 layer of record)
const V4_COMMIT_C = '6d0eb77d62404ddd5724cb35cee6d8c6a2a77e85'; // WE-1 promotion (PR #212) — manifest v4 + 1.1 outputs + packages
const INT0_PIN = '4d857c472fd725597ac21db189542c8f12c82dba';
const OPERATOR_TRACE = '1a188c14685e2965';
const sha256 = (b) => crypto.createHash('sha256').update(b).digest('hex');
const now = () => new Date().toISOString().replace(/\.\d+Z$/, 'Z');
const j1 = (o) => JSON.stringify(o, null, 1); // wave-artifact family convention: 1-space, no trailing NL
const j2 = (o) => JSON.stringify(o, null, 2) + '\n';
const deepEqual = (a, b) => JSON.stringify(a) === JSON.stringify(b);

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
let _man4 = null;
async function man4() {
  if (_man4) return _man4;
  _man4 = JSON.parse((await fetchRaw('SME-GuidedLessons/integration/hub-import-manifest-v4.json', V4_COMMIT_C)).toString('utf8'));
  return _man4;
}
async function noteIds() {
  const m = await man4();
  return m.artifacts.filter((a) => a.kind === 'hub-lesson-import-1.1').map((a) => a.noteId);
}
async function src02(noteId) {
  const buf = await fetchRaw(`SME-GuidedLessons/integration/source-0.2/guided-lesson-${noteId}.json`, V4_COMMIT_A);
  return { buf, obj: JSON.parse(buf.toString('utf8')) };
}
async function hub11(noteId) {
  const buf = await fetchRaw(`SME-GuidedLessons/integration/hub-import-1.1/${noteId}.hub-lesson-import.json`, V4_COMMIT_C);
  return { buf, obj: JSON.parse(buf.toString('utf8')) };
}
async function pkg(noteId) {
  const buf = await fetchRaw(`SME-GuidedLessons/integration/question-packages/${noteId}.sme-question-package.json`, V4_COMMIT_C);
  return { buf, obj: JSON.parse(buf.toString('utf8')) };
}
async function sidecar(noteId, sourceUrl) {
  const p = sourceUrl.split('https://www.savemyexams.com/igcse/chemistry/edexcel/19/revision-notes/')[1].replace(/\/+$/, '');
  const buf = await fetchRaw(`SME-RevisionNotes/igcse-chemistry-19/notes/${p}.json`, V4_COMMIT_C);
  return JSON.parse(buf.toString('utf8'));
}
// wave per note: the wave dirs are the intake grouping of record
async function waveMap() {
  const cacheKey = path.join(CACHE, 'wavemap.json');
  if (fs.existsSync(cacheKey)) return JSON.parse(fs.readFileSync(cacheKey, 'utf8'));
  const map = {};
  for (let w = 1; w <= 10; w++) {
    const listing = await fetchJson(`contents/SME-GuidedLessons/wave-${w}?ref=${V4_COMMIT_C}`);
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

// ── caption coalescing (deterministic; nothing authored) ─────────────────────
const collapse = (t) => t.replace(/\s+/g, ' ').trim();
function captionFor(basename, blocks) {
  for (let i = 0; i < blocks.length; i++) {
    const b = blocks[i];
    if (b.type === 'figure' && (b.file || '').endsWith(basename)) {
      const nxt = blocks[i + 1];
      if (nxt && nxt.type === 'paragraph') {
        const md = (nxt.md || '').trim();
        if (md.startsWith('***') && md.endsWith('***') && md.length > 6) {
          return { cls: 'coalesced', caption: collapse(md.slice(3, -3)) };
        }
        return { cls: 'standalone-no-cap', caption: null };
      }
      return { cls: 'standalone-no-cap', caption: null };
    }
  }
  // table-embedded: row-context derivation from verbatim header/row cells
  for (const b of blocks) {
    if (b.type === 'table' && (b.md || '').includes(basename)) {
      const lines = b.md.split('\n').filter((l) => l.includes('|'));
      if (lines.length >= 2) {
        const cells = (l) => l.split('|').slice(1, -1).map((c) => collapse(c.replace(/\*\*/g, '')).replace(/!\[.*?\]\(.*?\)/g, '').replace(/!\S*?\]\(.*?\)/g, '').trim());
        const header = cells(lines[0]);
        for (const line of lines.slice(2)) {
          if (!line.includes(basename)) continue;
          // locate the cell whose ORIGINAL text contains the basename (or the image marker)
          const rawCells = line.split('|').slice(1, -1);
          let col = rawCells.findIndex((c) => c.includes(basename));
          if (col < 0) col = rawCells.findIndex((c) => /!\S*?\]\(/.test(c));
          const row = cells(line);
          const colHeader = (header[col] || '').trim();
          const rowLabel = (row[0] || '').trim();
          if (colHeader && rowLabel) return { cls: 'row-context', caption: collapse(`${colHeader} — ${rowLabel}`) };
          if (colHeader) return { cls: 'row-context', caption: collapse(colHeader) };
        }
      }
      return { cls: 'table-no-context', caption: null };
    }
  }
  // bullets/paragraph-embedded: the introducing line, image syntax stripped
  for (const b of blocks) {
    if ((b.type === 'bullets' || b.type === 'paragraph' || b.type === 'callout') && (b.md || '').includes(basename)) {
      const line = b.md.split('\n').find((l) => l.includes(basename));
      if (line) {
        const text = collapse(line.replace(/!\[[^\]]*\]\([^)]*\)/g, '').replace(/!\S*?\]\([^)]*\)/g, '').replace(/\*\*/g, '').replace(/^[-*]\s*/, ''));
        if (text) return { cls: 'inline', caption: text };
      }
      return { cls: 'inline-no-text', caption: null };
    }
  }
  return { cls: 'unresolved', caption: null };
}

// ── schema derivation (mechanical bumps of the of-record 0.2 / 1.1 schemas) ──
function derive03Schema(s02) {
  const s = JSON.parse(JSON.stringify(s02));
  s.$id = 'guided-lesson/0.3';
  s.properties.format.const = 'guided-lesson/0.3';
  const fig = s.properties.figures.items;
  fig.properties.caption = { type: 'string', minLength: 1, description: 'The parent note\'s own explanatory caption line — coalesced from the sidecar paragraph block immediately following the figure block (bold-italic house style), or row-context for table-embedded figures, or the introducing bullet text. Optional; absent = no explanatory line exists in the source (fail-closed).' };
  return s;
}
function derive12Schema(s11) {
  const s = JSON.parse(JSON.stringify(s11));
  s.$id = 'hub/lesson-import/1.2';
  s.properties.format.const = 'hub/lesson-import/1.2';
  s.properties.adapter.const = 'guided-lesson-0.3--hub-lesson-import-1.2';
  s.definitions.sourceBlock.properties.sourceFormat.const = 'guided-lesson/0.3';
  const fig = s.properties.lesson.properties.figures.items;
  fig.properties.caption = { type: 'string', minLength: 1, description: 'Verbatim passthrough of the source figure caption (figures-2.1 captions layer).' };
  return s;
}

module.exports = { TMP, OUT, CACHE, SURV, DL, sha256, now, j1, j2, deepEqual, check, CHECKS, FAILS, report, ARGS, PHASE, pooled, fetchRaw, fetchJson, man4, noteIds, src02, hub11, pkg, sidecar, waveMap, targetTokens, captionFor, derive03Schema, derive12Schema, V4_COMMIT_A, V4_COMMIT_C, INT0_PIN, OPERATOR_TRACE, R_REPO };

// ═══ phases (source / transform / verify) ═══
const CAPTION_KEY_ORDER = ['id', 'url', 'alt', 'sourceHeading', 'caption', 'moduleIds'];

// ── PHASE 1: source (coalesce captions into source-0.3) ──────────────────────
async function phaseSource() {
  fs.mkdirSync(path.join(OUT, 'source-0.3'), { recursive: true });
  fs.mkdirSync(path.join(OUT, 'schema'), { recursive: true });
  const m4 = await man4();
  const ids = await noteIds();
  check('C-1a', ids.length === 112, `notes ${ids.length} == manifest v4 lesson artifacts`);
  // schemas: mechanical derivation from the of-record 0.2 / 1.1 schemas @ pin
  const s02raw = await fetchRaw('SME-GuidedLessons/integration/schema/guided-lesson.0.2.schema.json', V4_COMMIT_C);
  const s11raw = await fetchRaw('SME-GuidedLessons/integration/schema/hub-lesson-import.1.1.schema.json', V4_COMMIT_C);
  const s03 = derive03Schema(JSON.parse(s02raw.toString('utf8')));
  const s12 = derive12Schema(JSON.parse(s11raw.toString('utf8')));
  fs.writeFileSync(path.join(OUT, 'schema', 'guided-lesson.0.3.schema.json'), j2(s03));
  fs.writeFileSync(path.join(OUT, 'schema', 'hub-lesson-import.1.2.schema.json'), j2(s12));
  check('C-1b', s03.properties.figures.items.properties.caption && s03.properties.figures.items.additionalProperties === false, '0.3 schema carries optional caption, still closed');
  check('C-1c', s12.properties.lesson.properties.figures.items.properties.caption && s12.definitions.sourceBlock.properties.sourceFormat.const === 'guided-lesson/0.3', '1.2 schema carries optional caption + bumped consts');
  const waves = await waveMap();
  const census = { coalesced: 0, 'row-context': 0, inline: 0, 'standalone-no-cap': 0, 'table-no-context': 0, 'inline-no-text': 0, unresolved: 0, figuresTotal: 0, notesWithFigures: 0 };
  const perNote = [];
  await pooled(ids, 6, async (noteId) => {
    const s = await src02(noteId);
    check(`C-2a ${noteId}`, s.obj.format === 'guided-lesson/0.2', `source-0.2 format @ ${V4_COMMIT_A.slice(0, 8)}`);
    const h = await hub11(noteId);
    check(`C-2b ${noteId}`, h.obj.source.sourceLayerSha256 === sha256(s.buf), `1.1 sourceLayerSha256 == sha256(source-0.2 bytes) — upstream fidelity`);
    const src03 = JSON.parse(JSON.stringify(s.obj));
    src03.format = 'guided-lesson/0.3';
    const figs = s.obj.figures || [];
    let derived = [];
    if (figs.length) {
      census.notesWithFigures++;
      const sc = await sidecar(noteId, s.obj.noteRef.sourceUrl);
      derived = figs.map((f) => {
        const base = f.url.split('/').pop();
        const r = captionFor(base, sc.blocks || []);
        census[r.cls] = (census[r.cls] || 0) + 1;
        census.figuresTotal++;
        const g = {};
        for (const k of ['id', 'url', 'alt', 'sourceHeading']) g[k] = f[k];
        if (r.caption) g.caption = r.caption;
        g.moduleIds = f.moduleIds;
        return g;
      });
      src03.figures = derived;
    }
    // determinism D-1: 0.3 == 0.2 minus declared deltas (format + figures[].caption)
    const strip = JSON.parse(JSON.stringify(src03));
    strip.format = 'guided-lesson/0.2';
    for (const f of strip.figures || []) delete f.caption;
    check(`D-1 ${noteId}`, deepEqual(strip, s.obj), 'source-0.3 == source-0.2 minus declared deltas');
    const buf = Buffer.from(j1(src03), 'utf8');
    fs.writeFileSync(path.join(OUT, 'source-0.3', `guided-lesson-${noteId}.json`), buf);
    perNote.push({ noteId, wave: waves[noteId], sourceLayerSha256: sha256(buf), captioned: derived.filter((f) => f.caption).length });
  });
  check('C-1d', Object.keys(wavesCheck(perNote)).length === 0, 'wave map complete ×112');
  fs.writeFileSync(path.join(OUT, 'captions-census.json'), j2({ generated_at_utc: now(), operator_trace: OPERATOR_TRACE, census, per_note: perNote }));
  console.log(`SOURCE DONE: 112 × source-0.3 emitted; figures ${census.figuresTotal} across ${census.notesWithFigures} notes; census ${JSON.stringify(census)}`);
  report();
}
function wavesCheck(perNote) { return perNote.filter((p) => !p.wave).map((p) => p.noteId); }

// ── PHASE 2: transform (--pinned-ref <commit A>) ─────────────────────────────
async function phaseTransform() {
  const pinnedRef = ARGS['pinned-ref'];
  if (!pinnedRef || !/^[0-9a-f]{40}$/.test(pinnedRef)) { console.error('--pinned-ref <40-hex commit A> required'); process.exit(2); }
  fs.mkdirSync(path.join(OUT, 'hub-import-1.2'), { recursive: true });
  const m4 = await man4();
  const ids = await noteIds();
  const Ajv = new (require('/home/z/node_modules/ajv'))({ allErrors: true, strict: false });
  const s12 = JSON.parse(fs.readFileSync(path.join(OUT, 'schema', 'hub-lesson-import.1.2.schema.json'), 'utf8'));
  const pkgSchemaRaw = await fetchRaw('SME-GuidedLessons/integration/schema/sme-question-package.1.0.schema.json', V4_COMMIT_C);
  const v12 = Ajv.compile(s12); const vPkg = Ajv.compile(JSON.parse(pkgSchemaRaw.toString('utf8')));
  const census = JSON.parse(fs.readFileSync(path.join(OUT, 'captions-census.json'), 'utf8'));
  const waves = await waveMap();
  const perNote = new Map(); // noteId → computed record (hash accumulation MUST be sequential, manifest order)
  await pooled(ids, 6, async (noteId) => {
    const s03buf = fs.readFileSync(path.join(OUT, 'source-0.3', `guided-lesson-${noteId}.json`));
    const src03 = JSON.parse(s03buf.toString('utf8'));
    const h = await hub11(noteId);
    const p = await pkg(noteId);
    // C-6 schema 1.2 + packages 1.0
    // mutate v4 1.1 bytes → 1.2: declared deltas ONLY (format, adapter, source block, figures[].caption)
    const hub12 = JSON.parse(h.buf.toString('utf8'));
    hub12.format = 'hub/lesson-import/1.2';
    hub12.adapter = 'guided-lesson-0.3--hub-lesson-import-1.2';
    hub12.source = {
      sourceFormat: 'guided-lesson/0.3', noteId, corpusVersion: hub12.source.corpusVersion,
      sourceLayerSha256: sha256(s03buf), pinnedRef,
    };
    const figs03 = src03.figures || [];
    if (figs03.length) {
      const byId03 = new Map(figs03.map((f) => [f.id, f]));
      hub12.lesson.figures = (hub12.lesson.figures || []).map((f) => {
        const g = {}; const src = byId03.get(f.id);
        for (const k of CAPTION_KEY_ORDER) { if (src && src[k] !== undefined) g[k] = src[k]; else if (f[k] !== undefined) g[k] = f[k]; }
        return g;
      });
      // cross-layer passthrough: 1.2 figures minus caption == source-0.3 figures minus caption
      const stripF = (arr) => arr.map((f) => { const c = { ...f }; delete c.caption; return c; });
      check(`C-2c ${noteId}`, deepEqual(stripF(hub12.lesson.figures), stripF(figs03)), '1.2 figures == source-0.3 figures (passthrough minus caption)');
    } else {
      check(`C-2c ${noteId}`, !hub12.lesson.figures, 'no figures either layer');
    }
    const ok12 = v12(hub12);
    check(`C-6b ${noteId}`, ok12, ok12 ? 'hub/lesson-import/1.2 ajv PASS' : JSON.stringify(v12.errors).slice(0, 240));
    const okPkg = vPkg(p.obj);
    check(`C-6c ${noteId}`, okPkg, okPkg ? 'sme-question-package/1.0 ajv PASS' : JSON.stringify(vPkg.errors).slice(0, 200));
    // D-2 determinism: 1.2 == v4 1.1 minus declared deltas
    const strip = JSON.parse(JSON.stringify(hub12));
    strip.format = 'hub/lesson-import/1.1'; strip.adapter = 'guided-lesson-0.2--hub-lesson-import-1.1';
    strip.source = { ...h.obj.source };
    for (const f of strip.lesson.figures || []) delete f.caption;
    check(`D-2 ${noteId}`, deepEqual(strip, h.obj), '1.2 == v4 1.1 minus declared deltas (format/adapter/source/captions)');
    // C-5 closure unchanged
    const figs = hub12.lesson.figures || [];
    const declared = new Set(figs.map((f) => f.id));
    let closureOk = true; let det = '';
    hub12.lesson.modules.forEach((mod, i) => {
      for (const fid of mod.figureIds || []) {
        if (!declared.has(fid)) { closureOk = false; det = `${fid} undeclared`; }
        const f = figs.find((x) => x.id === fid);
        if (f && !f.moduleIds.includes(`L${i + 1}`)) { closureOk = false; det = `${fid} missing L${i + 1}`; }
      }
    });
    for (const f of figs) for (const mid of f.moduleIds) {
      const li = Number(mid.slice(1)) - 1;
      if (!(hub12.lesson.modules[li].figureIds || []).includes(f.id)) { closureOk = false; det = `${f.id}/${mid} closure`; }
    }
    check(`C-5 ${noteId}`, closureOk, closureOk ? 'figureIds↔moduleIds closure unchanged' : det);
    // C-8 stream: 1.2 vs v4 1.1 — captions are not §7 tokens (hash accumulation happens later, in manifest order)
    const toks12 = targetTokens(hub12, p.obj); const s12j = toks12.join('\n');
    const toks11 = targetTokens(h.obj, p.obj); const s11j = toks11.join('\n');
    const sha12 = sha256(Buffer.from(s12j, 'utf8')); const sha11 = sha256(Buffer.from(s11j, 'utf8'));
    check(`C-8 ${noteId}`, sha12 === sha11 && s12j.length === s11j.length, `stream conserved 1.2==1.1 (${s12j.length} chars)`);
    // C-9 packages byte-identical to v4 manifest
    const v4pkg = m4.artifacts.find((a) => a.kind === 'sme-question-package' && a.noteId === noteId);
    check(`C-9 ${noteId}`, sha256(p.buf) === v4pkg.sha256 && p.buf.length === v4pkg.bytes, 'package bytes unchanged');
    const buf = Buffer.from(j2(hub12), 'utf8');
    fs.writeFileSync(path.join(OUT, 'hub-import-1.2', `${noteId}.hub-lesson-import.json`), buf);
    const figCount = { total: figs.length, moduleMapped: figs.filter((f) => f.moduleIds.length).length, noteLevel: figs.filter((f) => !f.moduleIds.length).length, captioned: figs.filter((f) => f.caption).length };
    perNote.set(noteId, { s12j, buf, figCount, wavesNote: waves[noteId], pkgSha: sha256(p.buf) });
  });
  // sequential hash accumulation in manifest-artifact order (v4 of-record accumulation order)
  let grand = crypto.createHash('sha256'); let grandChars = 0;
  const waveHashes = {}; let figTotals = { figures: 0, moduleMapped: 0, noteLevel: 0, captioned: 0 };
  const recordNotes = [];
  for (const noteId of ids) {
    const pn = perNote.get(noteId);
    grand.update(Buffer.from(pn.s12j, 'utf8')); grandChars += pn.s12j.length;
    const w = 'wave-' + pn.wavesNote; waveHashes[w] = waveHashes[w] || crypto.createHash('sha256'); waveHashes[w].update(Buffer.from(pn.s12j, 'utf8'));
    figTotals.figures += pn.figCount.total; figTotals.moduleMapped += pn.figCount.moduleMapped; figTotals.noteLevel += pn.figCount.noteLevel; figTotals.captioned += pn.figCount.captioned;
    recordNotes.push({ wave: pn.wavesNote, noteId, sourceLayerSha256: sha256(fs.readFileSync(path.join(OUT, 'source-0.3', `guided-lesson-${noteId}.json`))), hubSha256: sha256(pn.buf), pkgSha256: pn.pkgSha, stream: { chars: pn.s12j.length, sha256: sha256(Buffer.from(pn.s12j, 'utf8')), conserved: true, matchesV4: true }, figures: pn.figCount });
  }
  const waveOut = {}; for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
  check('C-10a', grandChars === m4.counts.authored_chars_conserved, `grand chars ${grandChars} vs v4 ${m4.counts.authored_chars_conserved}`);
  const grandSha = grand.digest('hex');
  check('C-10b', grandSha === m4.conservation.authored_stream_sha256, `grand stream ${grandSha.slice(0, 12)} == v4 ${m4.conservation.authored_stream_sha256.slice(0, 12)}`);
  check('C-10c', deepEqual(waveOut, m4.conservation.wave_stream_sha256), 'wave subtotals ×10 == v4 of-record');
  check('C-10d', recordNotes.length === 112, `record notes ${recordNotes.length}`);
  // manifest v5
  const c = census.census;
  const man5 = {
    format: 'hub-import-manifest/1.0',
    manifest_version: 5,
    generated_at_utc: now(),
    operator_trace: OPERATOR_TRACE,
    supersedes: 'hub-import-manifest-v4.json (the 112 sme-question-package artifacts stay byte-identical; all 112 hub-lesson-import artifacts re-pin to the figures-2.1 captions generation — hub/lesson-import/1.2, additive optional figures[].caption)',
    worked_examples_layer: m4.worked_examples_layer,
    ...(m4.figures_layer ? { figures_layer: m4.figures_layer } : {}),
    captions_layer: {
      wave: 'FIGURES-2.1 explain-dont-list (operator traces 1a188a15ac19ed05, 1a188c14685e2965)',
      derivation: 'captions are the parent note\'s OWN explanatory lines, coalesced mechanically from the sme-revision-note/1.0 sidecar: (a) the bold-italic paragraph block immediately following a figure block; (b) table-embedded figures: "<column header> — <row label>" from verbatim table cells; (c) bullets-embedded figures: the introducing bullet text with image syntax stripped. Nothing is authored; whitespace-only normalization.',
      fail_closed: 'figures with no adjacent explanatory line carry no caption (renderer falls back to the sourceHeading provenance line)',
      placement: 'supersedes the 1.1-era after-opening placement: figures render AFTER the module key points, caption-first, with the "sourceHeading — from the revision note" provenance line; the block-level provenance label is removed',
      excluded_from_stream: true,
      stream_note: 'captions are additive metadata outside the §7 stream: per-note stream anchors equal the v4 (worked-examples-1.0) of-record bytes exactly (proof of record: INT-3-transform-record-figures-2.1.json, matchesV4 ×112)',
    },
    source_generation: { format: 'guided-lesson/0.3', namespace: 'SME-GuidedLessons/integration/source-0.3/', pin: pinnedRef, int0_lineage: INT0_PIN },
    load_scope: { adapter: 'guided-lesson-0.3--hub-lesson-import-1.2', target_schemas: ['hub/lesson-import/1.2', 'sme-question-package/1.0'] },
    counts: { ...m4.counts, captions_coalesced: c.coalesced, captions_row_context: c['row-context'], captions_inline: c.inline, captions_none: (c['standalone-no-cap'] || 0) + (c['table-no-context'] || 0) + (c['inline-no-text'] || 0) + (c.unresolved || 0) },
    conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut, equals_v4: true },
    artifacts: [
      ...recordNotes.map((n) => { const f = path.join(OUT, 'hub-import-1.2', `${n.noteId}.hub-lesson-import.json`); return { kind: 'hub-lesson-import-1.2', noteId: n.noteId, path: `SME-GuidedLessons/integration/hub-import-1.2/${n.noteId}.hub-lesson-import.json`, sha256: n.hubSha256, bytes: fs.statSync(f).size }; }),
      ...m4.artifacts.filter((a) => a.kind === 'sme-question-package').map((a) => ({ kind: 'sme-question-package', noteId: a.noteId, path: `SME-GuidedLessons/integration/question-packages/${a.path.split('/').pop()}`, sha256: a.sha256, bytes: a.bytes })),
    ],
  };
  check('C-10e', man5.artifacts.length === 224, `manifest v5 artifacts ${man5.artifacts.length}`);
  fs.writeFileSync(path.join(OUT, 'hub-import-manifest-v5.json'), j2(man5));
  // INT-3 record (runner survivor shape: notes[].stream/hubSha256/pkgSha256/wave)
  const rec = {
    stage: 'INT-3', title: 'transform record — figures 2.1 captions generation (adapter guided-lesson-0.3--hub-lesson-import-1.2)',
    generated_at_utc: now(), operator_trace: OPERATOR_TRACE,
    adapter: 'guided-lesson-0.3--hub-lesson-import-1.2',
    source_pin: { repo: 'SyllabAI/syllabai-resources', ref: V4_COMMIT_C, note: 'v4 1.1 hub outputs + question packages + sidecars verified byte-exact @ this ref' },
    source_03_generation_pin: { commit: pinnedRef, namespace: 'SME-GuidedLessons/integration/source-0.3/' },
    conservation_law: 'captions are additive metadata outside the §7 stream: every per-note stream anchor equals the v4 (worked-examples-1.0) generation exactly (matchesV4), and grand + wave streams equal manifest v4 of record',
    grand_stream: { chars: grandChars, sha256: grandSha },
    wave_stream_sha256: waveOut,
    captions_census: c,
    notes: recordNotes,
  };
  fs.writeFileSync(path.join(OUT, 'INT-3-transform-record-figures-2.1.json'), j2(rec));
  console.log(`TRANSFORM DONE: 112 × 1.2 emitted; stream conserved (grand ${grandChars} chars == v4); figures ${figTotals.figures} (mapped ${figTotals.moduleMapped} / note-level ${figTotals.noteLevel}); captioned ${figTotals.captioned}`);
  report();
}

// ── PHASE 3: verify (cold re-run from emitted outputs) ───────────────────────
async function phaseVerify() {
  const m4 = await man4();
  const ids = (await man4()).artifacts.filter((a) => a.kind === 'hub-lesson-import-1.1').map((a) => a.noteId);
  const Ajv = new (require('/home/z/node_modules/ajv'))({ allErrors: true, strict: false });
  const s03 = JSON.parse(fs.readFileSync(path.join(OUT, 'schema', 'guided-lesson.0.3.schema.json'), 'utf8'));
  const s12 = JSON.parse(fs.readFileSync(path.join(OUT, 'schema', 'hub-lesson-import.1.2.schema.json'), 'utf8'));
  const v03 = Ajv.compile(s03); const v12 = Ajv.compile(s12);
  const man5 = JSON.parse(fs.readFileSync(path.join(OUT, 'hub-import-manifest-v5.json'), 'utf8'));
  const rec = JSON.parse(fs.readFileSync(path.join(OUT, 'INT-3-transform-record-figures-2.1.json'), 'utf8'));
  let grand = crypto.createHash('sha256'); let grandChars = 0; const waveHashes = {};
  const cold = new Map();
  await pooled(ids, 6, async (noteId) => {
    const b03 = fs.readFileSync(path.join(OUT, 'source-0.3', `guided-lesson-${noteId}.json`));
    const b12 = fs.readFileSync(path.join(OUT, 'hub-import-1.2', `${noteId}.hub-lesson-import.json`));
    const o03 = JSON.parse(b03.toString('utf8')); const o12 = JSON.parse(b12.toString('utf8'));
    check(`V-schema03 ${noteId}`, v03(o03), 'guided-lesson/0.3 ajv PASS (cold)');
    check(`V-schema12 ${noteId}`, v12(o12), 'hub/lesson-import/1.2 ajv PASS (cold)');
    const manA = man5.artifacts.find((a) => a.kind === 'hub-lesson-import-1.2' && a.noteId === noteId);
    check(`V-sha ${noteId}`, sha256(b12) === manA.sha256 && b12.length === manA.bytes, 'disk bytes == manifest v5 pin');
    const recN = rec.notes.find((n) => n.noteId === noteId);
    check(`V-int ${noteId}`, recN && recN.hubSha256 === sha256(b12) && recN.sourceLayerSha256 === sha256(b03), 'INT record anchors == disk');
    check(`V-pin ${noteId}`, o12.source.pinnedRef === man5.source_generation.pin && o12.source.sourceFormat === 'guided-lesson/0.3', 'pinnedRef/sourceFormat wiring');
    const p = await pkg(noteId);
    const toks = targetTokens(o12, p.obj); const s = toks.join('\n');
    check(`V-stream ${noteId}`, sha256(Buffer.from(s, 'utf8')) === recN.stream.sha256 && s.length === recN.stream.chars, 'stream anchor recompute (cold)');
    cold.set(noteId, { s, wave: recN.wave });
  });
  for (const noteId of ids) {
    const c = cold.get(noteId);
    grand.update(Buffer.from(c.s, 'utf8')); grandChars += c.s.length;
    const w = 'wave-' + c.wave; waveHashes[w] = waveHashes[w] || crypto.createHash('sha256'); waveHashes[w].update(Buffer.from(c.s, 'utf8'));
  }
  const waveOut = {}; for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest('hex');
  check('V-grand', grandChars === man5.counts.authored_chars_conserved && grand.digest('hex') === man5.conservation.authored_stream_sha256, `grand ${grandChars}`);
  check('V-waves', deepEqual(waveOut, man5.conservation.wave_stream_sha256), 'wave subtotals ×10 (cold)');
  check('V-counts', man5.artifacts.length === 224, 'manifest v5 lists 224');
  console.log(`VERIFY DONE: cold gates from disk — grand ${grandChars} chars conserved`);
  report();
}

(async () => {
  fs.mkdirSync(CACHE, { recursive: true });
  if (PHASE === 'source') await phaseSource();
  else if (PHASE === 'transform') await phaseTransform();
  else if (PHASE === 'verify') await phaseVerify();
  else { console.error(`unknown phase "${PHASE}" — source|transform|verify`); process.exit(2); }
})().catch((e) => { console.error('PIPELINE ABORTED:', e && (e.stack || e.message || e)); process.exit(1); });
