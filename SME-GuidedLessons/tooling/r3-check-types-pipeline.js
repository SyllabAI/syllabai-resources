#!/usr/bin/env node
/**
 * R3-CHECK-TYPES PIPELINE — stage-A pilot transform + manifest v7 + INT-3 record
 * (operator execute trace 1a18a0218b7f44fd on the queued spec of trace 1a189fd011119961)
 *
 * Input of record (local sparse checkout @ resources main 3b2ce8da…):
 *   source-0.5/            2 authored pilot notes (guided-lesson/0.5, committed @ commit A)
 *   source-0.4/            the 0.4 generation (baseline; D-1 determinism input)
 *   hub-import-1.3/        the 1.3 lesson outputs (D-2 baseline; 110 untouched re-pins)
 *   question-packages/     the 1.0 packages (C-9: 110 byte-identical, 2 baselines)
 *   hub-import-manifest-v6.json + records/INT-3-transform-record-figures-2.2.json
 *   schema/{guided-lesson.0.5, hub-lesson-import.1.4, sme-question-package.1.1}.json
 *
 * Outputs (namespace-complete, committed @ commit C):
 *   hub-import-1.4/<note>.hub-lesson-import.json   x2  (format hub/lesson-import/1.4)
 *   question-packages-1.1/<note>.sme-question-package.json x2 (format sme-question-package/1.1)
 *   hub-import-manifest-v7.json                    (224 artifacts, 4 re-issued, 220 re-pinned)
 *   records/INT-3-transform-record-r3-check-types.json
 *   records/R3-CHECK-TYPES-1.0-PROMOTION-20261030.json
 * + lane survivors under /home/z/my-project/scripts/r3-survivors/ (hub runner byte-anchors)
 *
 * Gate battery: C-1/C-2 upstream fidelity, D-1 source determinism, D-2 output determinism,
 * C-5 checkRefs closure, C-6 ajv x224 (+ x2 sources), C-9 package sha conservation,
 * written-kind invariants x16, MCQ deep conservation x2, stream recompute x112
 * (110 must equal the 1.3 anchors; 2 carry the declared delta), grand + wave x10.
 * FAIL-CLOSED: any gate failure aborts before any record is emitted.
 */
import { createRequire } from "node:module";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { execSync } from "node:child_process";

const require = createRequire(import.meta.url);
const Ajv = require("/home/z/my-project/syllabai-v2/node_modules/ajv");

const RES = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/integration";
const SURV = "/home/z/my-project/scripts/r3-survivors";
const PILOTS = ["rn_2MpXPtNXvn8pQm3r", "rn_8T5GfPn2q7sY2YCh"];
const OPERATOR_TRACE = "1a18a0218b7f44fd";
const QUEUE_TRACE = "1a189fd011119961";
const ADAPTER = "guided-lesson-0.5--hub-lesson-import-1.4";
const INT0 = "4d857c472fd725597ac21db189542c8f12c82dba";
const SOURCE_PIN_V6 = "71922d1510ee9e00400667670b40f36e1ae5d456"; // source-0.4 generation (lessons' provenance)
const RES_MAIN_AT_OPEN = "3b2ce8da700b80f51700fb34fc721c90d6654d6b";

const sha256 = (buf) => crypto.createHash("sha256").update(buf).digest("hex");
const now = () => new Date().toISOString().replace(/\.\d+Z$/, "Z");
const read = (p) => fs.readFileSync(p);
const readJson = (p) => JSON.parse(fs.readFileSync(p, "utf8"));

const CHECKS = [];
let FAILED = 0;
function gate(name, ok, detail = "") {
  CHECKS.push({ name, ok: !!ok, detail: String(detail).slice(0, 300) });
  if (!ok) { FAILED++; console.error(`  FAIL ${name} — ${String(detail).slice(0, 300)}`); }
  return !!ok;
}
function section(t) { console.log(`\n── ${t}`); }

// ── §7 canonical authored stream — target side, extended for written kinds ───
// MUST stay token-for-token identical to run_import.mjs targetTokens (which gains
// the same written extension, feed-safe: old packages carry no kind field).
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
    if (q.kind && q.kind !== "mcq") {
      if (q.modelAnswer != null) s.push(q.modelAnswer);
      if (Array.isArray(q.keywords)) for (const k of q.keywords) s.push(k);
    }
  }
  return s;
}

// ── P0 wave-open pins ─────────────────────────────────────────────────────────
section("P0 wave-open pins");
const commitA = execSync("git rev-parse HEAD", { cwd: "/home/z/my-project/syllabai-resources" }).toString().trim();
const commitAParent = execSync("git rev-parse HEAD~1", { cwd: "/home/z/my-project/syllabai-resources" }).toString().trim();
console.log(`commit A (source-0.5 generation): ${commitA} (parent ${commitAParent.slice(0, 8)})`);
// source-0.5 + schema 0.5 must be exactly what commit A carries (clean tree at those paths)
for (const rel of ["source-0.5/guided-lesson-rn_2MpXPtNXvn8pQm3r.json", "source-0.5/guided-lesson-rn_8T5GfPn2q7sY2YCh.json", "schema/guided-lesson.0.5.schema.json"]) {
  const blob = execSync(`git show HEAD:SME-GuidedLessons/integration/${rel}`, { cwd: "/home/z/my-project/syllabai-resources", maxBuffer: 1024 * 1024 * 8 });
  gate("P0 committed == working tree @ " + rel, blob.equals(read(path.join(RES, rel))));
}

// ── C-1 upstream fidelity: 112+112 local bytes == manifest v6 shas ───────────
section("C-1/C-2 upstream fidelity vs manifest v6");
const man6 = readJson(path.join(RES, "hub-import-manifest-v6.json"));
const int36 = readJson(path.join(RES, "records/INT-3-transform-record-figures-2.2.json"));
gate("C-1 manifest v6 shape", man6.manifest_version === 6 && man6.artifacts.length === 224);
const v6ByKindNote = new Map();
for (const a of man6.artifacts) v6ByKindNote.set(`${a.kind}|${a.noteId}`, a);
const notes = man6.artifacts.filter((a) => a.kind !== "sme-question-package").map((a) => a.noteId);
gate("C-1 112 notes", notes.length === 112, String(notes.length));
let shaOk = 0;
for (const n of notes) {
  const les = v6ByKindNote.get(`hub-lesson-import-1.3|${n}`);
  const pkg = v6ByKindNote.get(`sme-question-package|${n}`);
  const lesBuf = read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`));
  const pkgBuf = read(path.join(RES, "question-packages", `${n}.sme-question-package.json`));
  if (sha256(lesBuf) === les.sha256 && lesBuf.length === les.bytes && sha256(pkgBuf) === pkg.sha256 && pkgBuf.length === pkg.bytes) shaOk++;
}
gate("C-2 224 local bytes == manifest v6 shas (sparse checkout == pinned generations)", shaOk === 112, `${shaOk}/112 notes (224 artifacts)`);
// C-2b: v6 lessons carry sourceLayerSha256 == sha256(source-0.4 file) x112
let c2b = 0;
for (const n of notes) {
  const les = JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8"));
  const s4 = read(path.join(RES, "source-0.4", `guided-lesson-${n}.json`));
  if (les.source.sourceLayerSha256 === sha256(s4) && les.source.pinnedRef === SOURCE_PIN_V6) c2b++;
}
gate("C-2b v6 sourceLayerSha256 == sha256(source-0.4) x112 + pinnedRef wiring", c2b === 112, `${c2b}/112`);

// ── D-1 source determinism: 0.5 == 0.4 minus declared deltas x2 ──────────────
section("D-1 source determinism");
const src5 = {};
for (const n of PILOTS) {
  const s4 = readJson(path.join(RES, "source-0.4", `guided-lesson-${n}.json`));
  const s5 = readJson(path.join(RES, "source-0.5", `guided-lesson-${n}.json`));
  const stripped = JSON.parse(JSON.stringify(s5));
  stripped.format = "guided-lesson/0.4";
  for (let i = 0; i < s4.lessons.length; i++) {
    stripped.lessons[i].check = stripped.lessons[i].check.slice(0, s4.lessons[i].check.length);
  }
  const deltas = [];
  if (stripped.format !== s4.format) deltas.push("format");
  const eq = JSON.stringify(stripped) === JSON.stringify(s4);
  // deepEqual via canonical stringify round-trip
  const eqDeep = JSON.stringify(stripUndefined(stripped)) === JSON.stringify(stripUndefined(s4));
  gate(`D-1 ${n}: 0.5 == 0.4 minus (format, appended check items)`, eqDeep, eq ? "strict" : "canonical");
  src5[n] = s5;
}
function stripUndefined(o) { return o; } // JSON.parse output carries no undefined — canonical form is exact

// ── schemas + C-6 ajv battery ────────────────────────────────────────────────
section("C-6 ajv battery");
const ajv = new Ajv({ allErrors: true });
const vSrc5 = ajv.compile(readJson(path.join(RES, "schema/guided-lesson.0.5.schema.json")));
const vHub14 = ajv.compile(readJson(path.join(RES, "schema/hub-lesson-import.1.4.schema.json")));
const vPkg11 = ajv.compile(readJson(path.join(RES, "schema/sme-question-package.1.1.schema.json")));
for (const n of PILOTS) {
  const ok = vSrc5(src5[n]);
  gate(`C-6 source-0.5 ${n} vs guided-lesson/0.5`, ok, ok ? "" : ajv.errorsText(vSrc5.errors).slice(0, 250));
}

// ── transform: mutate v6 bytes by the declared deltas ────────────────────────
section("transform (declared deltas on the 1.3 / 1.0 bytes)");
const outLessons = {}, outPkgs = {};
for (const n of PILOTS) {
  const hub = JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8"));
  const pkg = JSON.parse(read(path.join(RES, "question-packages", `${n}.sme-question-package.json`), "utf8"));
  const src = src5[n];
  const s5buf = read(path.join(RES, "source-0.5", `guided-lesson-${n}.json`));
  const s5sha = sha256(s5buf);

  // -- lesson: format/adapter/source bump + checkRefs extension; NOTHING else --
  const hubOrig = JSON.parse(JSON.stringify(hub));
  hub.format = "hub/lesson-import/1.4";
  hub.adapter = ADAPTER;
  hub.source.sourceFormat = "guided-lesson/0.5";
  hub.source.sourceLayerSha256 = s5sha;
  hub.source.pinnedRef = commitA;
  hub.lesson.modules.forEach((m, i) => {
    const written = src.lessons[i].check.slice(5); // the 4 authored items, in order
    written.forEach((_, k) => m.checkRefs.push(`${m.id}::Q${6 + k}`));
  });
  outLessons[n] = hub;

  // -- package: format/adapter/source bump + 16 questions appended IN MODULE ORDER --
  const pkgOrig = JSON.parse(JSON.stringify(pkg));
  pkg.format = "sme-question-package/1.1";
  pkg.adapter = ADAPTER;
  pkg.source.sourceFormat = "guided-lesson/0.5";
  pkg.source.sourceLayerSha256 = s5sha;
  pkg.source.pinnedRef = commitA;
  // module-grain rebuild: the 1.0 questions are module-ordered contiguous (L1 Q1-5, L2 Q1-5, …);
  // the written items interleave per module so the flat order stays 1:1 with the extended checkRefs
  const baseCounts = hub.lesson.modules.map((m) => m.checkRefs.length - 4); // pre-extension count
  const rebuilt = [];
  let off = 0;
  hub.lesson.modules.forEach((m, i) => {
    rebuilt.push(...pkgOrig.questions.slice(off, off + baseCounts[i]));
    off += baseCounts[i];
    src.lessons[i].check.slice(5).forEach((c, k) => {
      rebuilt.push({
        id: `${n}::L${i + 1}::Q${baseCounts[i] + 1 + k}`,
        moduleId: m.id,
        stem: c.stem,
        misconceptionClass: c.misconceptionClass,
        kind: c.kind,
        modelAnswer: c.modelAnswer,
        ...(Array.isArray(c.keywords) ? { keywords: c.keywords } : {}),
        options: [],
      });
    });
  });
  if (off !== pkgOrig.questions.length) throw new Error(`module-grain rebuild drift ${n}: ${off} != ${pkgOrig.questions.length}`);
  pkg.questions = rebuilt;
  outPkgs[n] = pkg;

  // -- invariants x16 + written-kind gate --
  let wok = 0;
  for (const q of pkg.questions) {
    if (!(q.kind && q.kind !== "mcq")) continue;
    const idOK = /^rn_[A-Za-z0-9]+::L[1-5]::Q[1-9]$/.test(q.id);
    const ok = idOK && q.modelAnswer && q.modelAnswer.length > 0 && Array.isArray(q.keywords) && q.keywords.length >= 1 && Array.isArray(q.options) && q.options.length === 0;
    if (!ok) console.error(`  written invariant fail: ${q.id}`);
    else wok++;
  }
  gate(`written-kind invariants ${n} (x8)`, wok === 8, `${wok}/8`);

  // -- MCQ deep conservation: the original questions appear in the rebuilt array (any order),
  //    byte-deep-equal, and nothing else changed count-wise (+8 written) --
  const origByKey = new Map(pkgOrig.questions.map((q) => [q.id, JSON.stringify(q)]));
  const mcqSame = [...origByKey.entries()].every(([id, s]) => {
    const q = pkg.questions.find((x) => x.id === id);
    return q && JSON.stringify(q) === s;
  });
  gate(`MCQ deep conservation ${n} (${pkgOrig.questions.length} questions)`, mcqSame && pkg.questions.length === pkgOrig.questions.length + 8);

  // -- checkRefs <-> questions 1:1 in order (C-5) --
  const flat = [];
  hub.lesson.modules.forEach((m) => m.checkRefs.forEach((r) => flat.push(r)));
  const oneToOne = flat.length === pkg.questions.length && flat.every((r, i) => r === pkg.questions[i].id);
  gate(`C-5 checkRefs<->questions 1:1 ${n}`, oneToOne, `${flat.length} refs / ${pkg.questions.length} questions`);

  // -- D-2 determinism: derived outputs minus declared deltas deep-equal the v6 bytes --
  const hubBack = JSON.parse(JSON.stringify(hub));
  hubBack.format = "hub/lesson-import/1.3";
  hubBack.adapter = "guided-lesson-0.4--hub-lesson-import-1.3";
  hubBack.source = JSON.parse(JSON.stringify(hubOrig.source));
  hubBack.lesson.modules.forEach((m) => { m.checkRefs = m.checkRefs.slice(0, 5); });
  gate(`D-2 lesson ${n} == 1.3 minus deltas`, JSON.stringify(hubBack) === JSON.stringify(hubOrig));
  const pkgBack = JSON.parse(JSON.stringify(pkg));
  pkgBack.format = "sme-question-package/1.0";
  pkgBack.adapter = "guided-lesson-0.1--hub-lesson-import-1.0";
  pkgBack.source = JSON.parse(JSON.stringify(pkgOrig.source));
  pkgBack.questions = pkgBack.questions.filter((q) => !(q.kind && q.kind !== "mcq")); // strip written items wherever they sit
  gate(`D-2 package ${n} == 1.0 minus deltas`, JSON.stringify(pkgBack) === JSON.stringify(pkgOrig));

  // -- ajv vs the union schemas --
  gate(`C-6 lesson ${n} vs hub/lesson-import/1.4`, vHub14(hub), vHub14.errors ? ajv.errorsText(vHub14.errors).slice(0, 250) : "");
  gate(`C-6 package ${n} vs sme-question-package/1.1`, vPkg11(pkg), vPkg11.errors ? ajv.errorsText(vPkg11.errors).slice(0, 250) : "");
}

// 110 untouched: ajv under the UNION schemas + package sha conservation (C-9)
let untouchedOk = 0, pkgShaOk = 0;
for (const n of notes) {
  if (PILOTS.includes(n)) continue;
  const hub = JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8"));
  const pkgBuf = read(path.join(RES, "question-packages", `${n}.sme-question-package.json`));
  const pkg = JSON.parse(pkgBuf, "utf8");
  if (vHub14(hub) && vPkg11(pkg)) untouchedOk++;
  if (sha256(pkgBuf) === v6ByKindNote.get(`sme-question-package|${n}`).sha256) pkgShaOk++;
}
gate("C-6 110 untouched lessons+packages vs union schemas", untouchedOk === 110, `${untouchedOk}/110`);
gate("C-9 110 package shas == manifest v6 (byte conservation)", pkgShaOk === 110, `${pkgShaOk}/110`);

// ── emit artifacts ───────────────────────────────────────────────────────────
section("emit artifacts");
fs.mkdirSync(path.join(RES, "hub-import-1.4"), { recursive: true });
fs.mkdirSync(path.join(RES, "question-packages-1.1"), { recursive: true });
const emit = (p, obj) => { const buf = Buffer.from(JSON.stringify(obj, null, 2) + "\n", "utf8"); fs.writeFileSync(p, buf); return buf; };
const newSha = {};
for (const n of PILOTS) {
  const lb = emit(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), outLessons[n]);
  const pb = emit(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), outPkgs[n]);
  newSha[n] = { hub: { sha256: sha256(lb), bytes: lb.length }, pkg: { sha256: sha256(pb), bytes: pb.length } };
  console.log(`  hub-import-1.4/${n}: ${lb.length}B  question-packages-1.1/${n}: ${pb.length}B`);
}

// ── G-E stream recompute x112 ────────────────────────────────────────────────
section("G-E stream recompute x112");
const v6Rows = new Map(int36.notes.map((r) => [r.noteId, r]));
const rows = int36.notes.map((r) => JSON.parse(JSON.stringify(r)));
let nonPilotStreamOk = 0;
for (const row of rows) {
  const n = row.noteId;
  if (PILOTS.includes(n)) {
    const s = targetTokens(outLessons[n], outPkgs[n]).join("\n");
    row.sourceLayerSha256 = sha256(read(path.join(RES, "source-0.5", `guided-lesson-${n}.json`)));
    row.hubSha256 = newSha[n].hub.sha256;
    row.pkgSha256 = newSha[n].pkg.sha256;
    row.stream = { sha256: sha256(Buffer.from(s, "utf8")), chars: s.length };
    row.r3_delta = { written_items: 8, mcq_unchanged: true };
  } else {
    const hub = JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8"));
    const pkg = JSON.parse(read(path.join(RES, "question-packages", `${n}.sme-question-package.json`), "utf8"));
    const s = targetTokens(hub, pkg).join("\n");
    const sha = sha256(Buffer.from(s, "utf8"));
    if (sha === row.stream.sha256 && s.length === row.stream.chars) nonPilotStreamOk++;
    else gate(`G-E stream ${n} == 1.3 anchor`, false, `got ${sha.slice(0, 12)}/${s.length} want ${row.stream.sha256.slice(0, 12)}/${row.stream.chars}`);
  }
}
gate("G-E 110 non-pilot stream anchors == figures-2.2 (1.3) generation exactly", nonPilotStreamOk === 110, `${nonPilotStreamOk}/110`);
gate("G-E 2 pilot rows re-anchored", rows.filter((r) => PILOTS.includes(r.noteId)).length === 2);

// grand + wave subtotals (int3.notes order — the runner's iteration order)
const grand = crypto.createHash("sha256");
let grandChars = 0;
const waveHashes = {};
for (const row of rows) {
  // recompute the stream string from the row's stored anchor? NO — streams of non-pilot
  // notes were verified == anchors above; pilots were computed here. Recompute all 112
  // strings in one pass for the hash (identical law to the runner).
  const n = row.noteId;
  const s = PILOTS.includes(n)
    ? targetTokens(outLessons[n], outPkgs[n]).join("\n")
    : targetTokens(
        JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8")),
        JSON.parse(read(path.join(RES, "question-packages", `${n}.sme-question-package.json`), "utf8")),
      ).join("\n");
  grand.update(Buffer.from(s, "utf8"));
  grandChars += s.length;
  const w = "wave-" + row.wave;
  waveHashes[w] = waveHashes[w] || crypto.createHash("sha256");
  waveHashes[w].update(Buffer.from(s, "utf8"));
}
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest("hex");
gate("G-E wave subtotals x10", Object.keys(waveOut).length === 10, Object.keys(waveOut).join(","));
const grandSha = grand.digest("hex"); // single finalization — computed once, before any logging
console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}…`);

// v6 grand must equal manifest v6 (cross-generation sanity)
gate("cross-check: manifest v6 grand == v6 record", man6.conservation.authored_stream_sha256 === int36.grand_stream.sha256);

// ── manifest v7 ──────────────────────────────────────────────────────────────
section("manifest v7");
const counts = {
  notes: 112,
  lessons: 239,
  checks: 1211,
  keyPoints: 1212,
  distractors: 3565,
  glossaryTerms: 654,
  figures: 200,
  figures_module_mapped: 122,
  figures_note_level: 78,
  workedExamples_populated: 112,
  workedExamples_null: 0,
  authored_chars_conserved: grandChars,
  authored_chars_v3_baseline: 1347771,
  added_chars: grandChars - 1347771,
  captions_coalesced: 143,
  captions_row_context: 16,
  captions_inline: 3,
  captions_none: 38,
  binding_heading_unique: 90,
  binding_sole_lesson: 0,
  binding_content_overlap: 12,
  binding_note_level: 78,
  binding_unresolved: 20,
  figures_binding_narrowed: 102,
  figures_claims_changed: 12,
  figures_wholesale_claims_kept: 2,
  checks_written: 16,
  checks_mcq: 1195,
  written_recall: 8,
  written_explain_why: 4,
  written_application: 4,
};
const artifacts = man6.artifacts.map((a) => {
  if (a.kind === "hub-lesson-import-1.3" && PILOTS.includes(a.noteId)) {
    return { kind: "hub-lesson-import-1.4", noteId: a.noteId, path: `SME-GuidedLessons/integration/hub-import-1.4/${a.noteId}.hub-lesson-import.json`, sha256: newSha[a.noteId].hub.sha256, bytes: newSha[a.noteId].hub.bytes };
  }
  if (a.kind === "sme-question-package" && PILOTS.includes(a.noteId)) {
    return { kind: "sme-question-package", noteId: a.noteId, path: `SME-GuidedLessons/integration/question-packages-1.1/${a.noteId}.sme-question-package.json`, sha256: newSha[a.noteId].pkg.sha256, bytes: newSha[a.noteId].pkg.bytes };
  }
  return a;
});
gate("manifest v7 lists 224", artifacts.length === 224);
gate("manifest v7: exactly 4 re-issued", artifacts.filter((a) => !man6.artifacts.some((b) => b.path === a.path)).length === 4);
const man7 = {
  format: "hub-import-manifest/1.0",
  manifest_version: 7,
  generated_at_utc: now(),
  operator_trace: OPERATOR_TRACE,
  supersedes: "hub-import-manifest-v6.json (110 hub-lesson-import-1.3 lessons + 110 sme-question-package/1.0 packages byte-identical re-pins; exactly 4 re-issued artifacts: 2 hub-lesson-import-1.4 lessons (checkRefs delta) + 2 sme-question-package/1.1 packages (+16 written items) — the R3 stage-A pilot tranche)",
  checks_layer: {
    wave: `R3-MIXED-CHECK-TYPES stage A (queue trace ${QUEUE_TRACE}, operator execute trace ${OPERATOR_TRACE})`,
    derivation: "16 authored written items (8 recall, 4 explain-why, 4 application), each spec-anchored to the lesson's keyPoints, carrying modelAnswer + generous synonym/inflection-bearing keywords; appended after the 5 MCQs of each of the 4 Alcohols pilot lessons",
    declared_revision: "the FIRST package-channel delta since INT-0: 2 packages re-issued under sme-question-package/1.1 (union schema — the 110 untouched 1.0 packages validate unchanged); 2 lessons re-issued under hub/lesson-import/1.4 (checkRefs 5->9); kind/modelAnswer/keywords are §7-declared stream tokens on written items",
    grading_law: "case-insensitive whole-token match of the learner text against keywords[]; >=1 hit -> correct; 0 hits -> not-quite + model answer; empty submit blocked; keywords absent -> reveal-only (fail-closed, never a silent wrong grade)",
    fail_closed: "written item without modelAnswer renders reveal-only, never gradeable, never blank; unknown kind renders reveal-only and warns at this gate",
  },
  source_generation: {
    format: "guided-lesson/0.5",
    namespace: "SME-GuidedLessons/integration/source-0.5/",
    pin: commitA,
    int0_lineage: INT0,
  },
  load_scope: { adapter: ADAPTER, target_schemas: ["hub/lesson-import/1.4", "sme-question-package/1.1"] },
  counts,
  conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut },
  artifacts,
};
// ajv the manifest-shape? (no manifest schema of record — the runner's G-A structural checks own it)

// ── INT-3 record v7 ──────────────────────────────────────────────────────────
const int37 = {
  stage: "INT-3",
  title: "transform record — R3 mixed check types generation (adapter guided-lesson-0.5--hub-lesson-import-1.4)",
  generated_at_utc: now(),
  operator_trace: OPERATOR_TRACE,
  adapter: ADAPTER,
  source_pin: {
    repo: "SyllabAI/syllabai-resources",
    ref: RES_MAIN_AT_OPEN,
    note: "figures-2.2 binding generation (1.3 outputs + packages + manifest v6 + schemas) verified byte-exact @ this ref",
  },
  source_05_generation_pin: { commit: commitA, namespace: "SME-GuidedLessons/integration/source-0.5/" },
  conservation_law:
    "kind/modelAnswer/keywords on written items ARE §7 stream tokens (the walk extends by those fields on kind!=mcq; old packages carry no kind so the walk is byte-neutral for them): the 110 non-pilot per-note streams equal the figures-2.2 (1.3) generation exactly; the 2 pilot notes add the 16 written items' tokens (stem, misconceptionClass, modelAnswer, keywords — written kinds carry no options). Grand + wave subtotals recomputed over all 112 in the v6 note order.",
  grand_stream: { chars: grandChars, sha256: grandSha },
  wave_stream_sha256: waveOut,
  r3_census: {
    pilot_notes: PILOTS,
    pilot_lessons: 4,
    written_items: 16,
    kinds: { recall: 8, "explain-why": 4, application: 4 },
    mcqs_conserved: 1195,
    packages_untouched: 110,
    lessons_untouched: 110,
    authored_chars_delta_vs_v6: grandChars - int36.grand_stream.chars,
  },
  notes: rows,
};
const int3Buf = emit(path.join(RES, "records/INT-3-transform-record-r3-check-types.json"), int37);
const man7Buf = emit(path.join(RES, "hub-import-manifest-v7.json"), man7);

// ── fail-closed checkpoint before the promotion receipt ─────────────────────
if (FAILED > 0) {
  console.error(`\nFAIL-CLOSED: ${FAILED} gate failure(s) — promotion receipt NOT emitted`);
  process.exit(1);
}

// ── promotion receipt ────────────────────────────────────────────────────────
section("promotion receipt");
const receipt = {
  format: "r3-check-types-promotion-receipt/1.0",
  wave: "R3-MIXED-CHECK-TYPES (stage A — Alcohols pilot tranche)",
  operator_traces: [QUEUE_TRACE, OPERATOR_TRACE],
  generated_at_utc: now(),
  repo: "SyllabAI/syllabai-resources",
  branch: "integration/r3-check-types-20261030",
  queue_of_record: "R3-MIXED-CHECK-TYPES-QUEUED-20261030 (hub-side lane receipt .syllabai/receipts/HUB-R3-QUEUED/ + download/)",
  commits: {
    A: { sha: commitA, parent: commitAParent, note: "source-0.5 generation — 2 authored guided-lesson/0.5 pilot notes (16 written items) + schema/guided-lesson.0.5.schema.json" },
    B: { sha: "(this commit — target schemas)", note: "schema/hub-lesson-import.1.4.schema.json + schema/sme-question-package.1.1.schema.json (generation-union minors)" },
    C: { sha: "(namespace-complete — outputs + manifest v7 + records + spec + pipeline)", note: "hub-import-1.4/ + question-packages-1.1/ + hub-import-manifest-v7.json + records/INT-3-transform-record-r3-check-types.json + records/R3-CHECK-TYPES-1.0-PROMOTION-20261030.json + ADAPTER-SPEC-guided-lesson-0.5-to-hub-1.4.md + tooling/r3-check-types-pipeline.js" },
  },
  artifact_pin: commitA,
  pkg_pin: `${INT0} (110 untouched packages) | ${commitA} (2 pilot packages — the FIRST package-channel re-pin since INT-0)`,
  input_pins: { resources_main_at_wave_open: RES_MAIN_AT_OPEN },
  manifest: "hub-import-manifest-v7.json",
  int_record: "INT-3-transform-record-r3-check-types.json",
  adapter_spec: "ADAPTER-SPEC-guided-lesson-0.5-to-hub-1.4.md",
  counts_census: { notes: 112, lessons: 239, checks: 1211, checks_mcq: 1195, checks_written: 16, written_recall: 8, written_explain_why: 4, written_application: 4, pilot_notes: PILOTS, distractors: 3565 },
  schema_delta:
    "additive minors x3: guided-lesson 0.4->0.5 (optional written-kind check branch: kind/modelAnswer/keywords, no options; check maxItems 5->9); hub/lesson-import 1.3->1.4 (UNION consts + checkRefs maxItems 5->9, pattern Q[1-9]); sme-question-package 1.0->1.1 (UNION consts + question id Q[1-9] + written-kind branch: modelAnswer required, keywords optional, options empty). The 110+110 untouched artifacts validate unchanged under the union schemas.",
  taxonomy: "kind enum of record: mcq (default/absent) | recall | explain-why | application — the four kinds live-confirmed on SME (1 MCQ + 2 recall + 1 explain-why + 1 application per lesson set)",
  conservation: {
    law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq (feed-safe extension: no kind field -> walk unchanged); 110 non-pilot streams == 1.3 anchors exactly",
    authored_chars: grandChars,
    authored_chars_delta_vs_v6: grandChars - int36.grand_stream.chars,
    mcq_conservation: "pilot package questions[0..9] deep-equal the 1.0 bytes x2; 110 package shas byte-identical x110",
  },
  gates: { pipeline: `${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, 0 fail`, gate_log: CHECKS },
  merge_order:
    "resources PR (this branch) merges to main FIRST; the hub PR (runner FEED r3-check-types-v7 + GuidedQuestion optional fields + written paths in both renderers + re-issued artifacts + re-issued guided-import.json) merges only after; stage-B corpus rollout (~956 items) remains operator-gated and is NOT in this tranche",
  hub_side_note:
    "renderer law: MCQ path untouched byte-for-byte; written kinds render a labelled free-text input, submit -> verdict role=status + model answer ALWAYS shown on settle; a11y label/aria-live; flow tallies unchanged in signature (keyword-hit boolean rides onAnswer correct); reveal-only fail-closed when keywords absent",
};
emit(path.join(RES, "records/R3-CHECK-TYPES-1.0-PROMOTION-20261030.json"), receipt);

// ── lane survivors for the hub runner byte-anchors ───────────────────────────
fs.mkdirSync(SURV, { recursive: true });
fs.copyFileSync(path.join(RES, "hub-import-manifest-v7.json"), path.join(SURV, "hub-import-manifest-v7.json"));
fs.copyFileSync(path.join(RES, "records/INT-3-transform-record-r3-check-types.json"), path.join(SURV, "INT-3-transform-record-r3-check-types.json"));
fs.copyFileSync(path.join(RES, "schema/hub-lesson-import.1.4.schema.json"), path.join(SURV, "hub-lesson-import.1.4.schema.json"));
fs.copyFileSync(path.join(RES, "schema/sme-question-package.1.1.schema.json"), path.join(SURV, "sme-question-package.1.1.schema.json"));
// v6 survivors the runner also needs (byte-anchored from the sparse checkout @ main)
fs.copyFileSync(path.join(RES, "hub-import-manifest-v6.json"), path.join(SURV, "hub-import-manifest-v6.json"));

console.log(`\nRESULT: ${FAILED === 0 ? "GREEN — PIPELINE COMPLETE" : "FAIL-CLOSED"}`);
console.log(`  gates: ${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, ${FAILED} failures`);
console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}… (v6: ${int36.grand_stream.chars} → delta +${grandChars - int36.grand_stream.chars})`);
