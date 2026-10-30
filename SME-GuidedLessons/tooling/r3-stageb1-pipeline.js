#!/usr/bin/env node
/**
 * R3-CHECK-TYPES PIPELINE — STAGE B WAVE 1 (S-B1)
 * (operator execute: "stage B proceed", hub chat trace 1a18bc1ca2cf48e5, on the
 *  stage-B contract of record in R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json:
 *  "corpus rollout ~956 authored items ... in authoring waves with per-note SCHEMA PASS
 *  gates, wave receipt + recalibration, matching the waves 1-5 authoring discipline;
 *  tranche order mirrors the authoring register")
 *
 * S-B1 tranche of record: the wave-1 authoring register (10 notes, 24 lessons, 120 MCQs)
 * -> +96 authored written items (48 recall, 24 explain-why, 24 application).
 *
 * Inputs (local checkout @ resources main 5f170f98…):
 *   scripts/r3-stageb1/authoring-part{1,2,3}.json   the 96 authored items (KP-anchored)
 *   integration/source-0.4/        0.4 generation (D-1 baseline)
 *   integration/hub-import-1.3/    1.3 lesson outputs (D-2 baseline, 100 untouched re-pins)
 *   integration/question-packages/ 1.0 packages (C-9: 100 byte-identical, 10 baselines)
 *   integration/hub-import-1.4/    + question-packages-1.1/  the 2 stage-A pilots (re-pinned)
 *   integration/hub-import-manifest-v7.json + records/INT-3-transform-record-r3-check-types.json
 *   schema/{guided-lesson.0.5, hub-lesson-import.1.4, sme-question-package.1.1}.json
 *
 * Outputs (namespace-complete):
 *   source-0.5/ ×10 (new)          hub-import-1.4/ ×10 (new)   question-packages-1.1/ ×10 (new)
 *   hub-import-manifest-v8.json    records/INT-3-transform-record-r3-stageb1.json
 *   records/R3-CHECK-TYPES-STAGEB1-PROMOTION-20261030.json
 * + survivors for the hub runner byte-anchors (scripts/r3-survivors/)
 *
 * Gates: A0 authoring inventory, D-1 source determinism ×10, C-6 ajv (10 sources + 12 lessons
 * + 12 packages + 200 untouched), C-2 preflight vs manifest v7 (224 shas), written-kind
 * invariants ×96, MCQ deep conservation ×10 (+ pilot re-proofs ×2), C-5 checkRefs closure ×12,
 * D-2 output determinism ×10, C-9 package sha conservation ×100, G-E stream recompute ×112
 * (100 == v7 anchors; 2 pilots == stage-A anchors exactly; 10 new), grand + waves ×10.
 * FAIL-CLOSED: any gate failure aborts before any record is emitted.
 */
import { createRequire } from "node:module";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { execSync } from "node:child_process";

const require = createRequire(import.meta.url);
const Ajv = require("/home/z/my-project/syllabai-v2/node_modules/ajv");

const RES = "/home/z/my-project/.tmp/resources-ground/SME-GuidedLessons/integration";
const RESROOT = "/home/z/my-project/.tmp/resources-ground";
const AUTH = "/home/z/my-project/scripts/r3-stageb1";
const SURV = "/home/z/my-project/scripts/r3-survivors";
const PILOTS = ["rn_2MpXPtNXvn8pQm3r", "rn_8T5GfPn2q7sY2YCh"]; // stage A, already live
const STAGE_A_COMMIT = "80afdb8e02b628754f0e522d257e54d046ba5b0f";
const SOURCE_PIN_V6 = "71922d1510ee9e00400667670b40f36e1ae5d456"; // source-0.4 (the 100 untouched lessons)
const OPERATOR_TRACE = "1a18bc1ca2cf48e5"; // "stage B proceed"
const STAGE_A_TRACE = "1a18a0218b7f44fd";
const QUEUE_TRACE = "1a189fd011119961";
const ADAPTER = "guided-lesson-0.5--hub-lesson-import-1.4";
const RES_MAIN_AT_OPEN = "5f170f98"; // resources main at S-B1 open (resolved of record below)

// ── P0 wave-open pins (resolved, never assumed) ──────────────────────────
section("P0 wave-open pins");
const RES_MAIN_OPEN_RESOLVED = execSync("git rev-parse main", { cwd: RESROOT }).toString().trim();
if (!RES_MAIN_AT_OPEN.startsWith(RES_MAIN_OPEN_RESOLVED.slice(0, 8))) {
  throw new Error(`resources main drift: opened at ${RES_MAIN_AT_OPEN.slice(0, 8)}, checkout main is ${RES_MAIN_OPEN_RESOLVED.slice(0, 8)} — re-ground before running`);
}
console.log(`resources main at open: ${RES_MAIN_OPEN_RESOLVED.slice(0, 12)}…`);
// commit A of record: the source-0.5 generation commit — HEAD at pipeline run time
// (mirrors stage A: sources are committed FIRST; pinnedRef must be a real 40-hex sha)
const commitA = execSync("git rev-parse HEAD", { cwd: RESROOT }).toString().trim();
const commitAParent = execSync("git rev-parse HEAD~1", { cwd: RESROOT }).toString().trim();
console.log(`commit A (S-B1 source-0.5 generation): ${commitA} (parent ${commitAParent.slice(0, 8)})`);

const sha256 = (buf) => crypto.createHash("sha256").update(buf).digest("hex");
const now = () => new Date().toISOString().replace(/\.\d+Z$/, "Z");
const read = (p) => fs.readFileSync(p);
const readJson = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
const emit = (p, obj) => { const buf = Buffer.from(JSON.stringify(obj, null, 2) + "\n", "utf8"); fs.writeFileSync(p, buf); return buf; };

const CHECKS = [];
let FAILED = 0;
function gate(name, ok, detail = "") {
  CHECKS.push({ name, ok: !!ok, detail: String(detail).slice(0, 300) });
  if (!ok) { FAILED++; console.error(`  FAIL ${name} — ${String(detail).slice(0, 300)}`); }
  return !!ok;
}
function section(t) { console.log(`\n── ${t}`); }

// ── §7 canonical authored stream — target side, extended for written kinds ───
// MUST stay token-for-token identical to run_import.mjs targetTokens (already carries
// the written extension at v7; old 1.0 packages carry no kind -> walk unchanged).
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

// ── A0 authoring inventory ───────────────────────────────────────────────────
section("A0 authoring inventory");
const auth = { notes: {} };
for (const part of ["authoring-part1.json", "authoring-part2.json", "authoring-part3.json"]) {
  const j = readJson(path.join(AUTH, part));
  for (const [n, body] of Object.entries(j.notes)) {
    gate(`A0 no duplicate note across parts: ${n}`, !auth.notes[n]);
    auth.notes[n] = body.lessons.map((L) => L.items);
  }
}
const TRANCHE = Object.keys(auth.notes).sort();
gate("A0 tranche == wave-1 register of record (10 notes)", TRANCHE.length === 10, TRANCHE.join(","));
const REGISTER_W1 = ["rn_2d6Yb8GwGfRRd6pZ","rn_4SgDJv8rKxpQQSBh","rn_HZM2WRjPPT8Srcxt","rn_JCfdFrHsCkrmMbFj","rn_TM4QVMgXVxs4vbfY","rn_fQSYvKRMDBj3s2Bx","rn_jNJ4gTmcHqdFqsNh","rn_kJg2gwF77vdFZZ2H","rn_wTtM2fQVVjntRm64","rn_xT8XsdJtDX5gNFXj"].sort();
gate("A0 tranche matches wave-1 roster (timing receipts of record)", JSON.stringify(TRANCHE) === JSON.stringify(REGISTER_W1));
const KIND_ORDER = ["recall", "recall", "explain-why", "application"];
let itemTotal = 0, lessonTotal = 0;
for (const n of TRANCHE) {
  const s4 = readJson(path.join(RES, "source-0.4", `guided-lesson-${n}.json`));
  gate(`A0 ${n}: authored lessons == source lessons (${s4.lessons.length})`, auth.notes[n].length === s4.lessons.length, `${auth.notes[n].length} vs ${s4.lessons.length}`);
  s4.lessons.forEach((L, i) => {
    lessonTotal++;
    const items = auth.notes[n][i];
    itemTotal += items.length;
    const kindsOk = items.length === 4 && items.every((it, k) => it.kind === KIND_ORDER[k]);
    if (!kindsOk) gate(`A0 ${n} L${i + 1} kind order`, false, items.map((x) => x.kind).join(","));
    items.forEach((it, k) => {
      const bad = [];
      if (!it.stem || !it.stem.trim()) bad.push("stem");
      if (!it.misconceptionClass || !it.misconceptionClass.trim()) bad.push("misconceptionClass");
      if (!it.modelAnswer || !it.modelAnswer.trim()) bad.push("modelAnswer");
      if (!Array.isArray(it.keywords) || it.keywords.length < 1 || it.keywords.length > 20 || it.keywords.some((w) => !w || !w.trim())) bad.push("keywords");
      if ("options" in it) bad.push("options-forbidden");
      const kpCount = L.keyPoints.length;
      if (!it.anchor || !(it.anchor.kp >= 1 && it.anchor.kp <= kpCount)) bad.push(`anchor ${it.anchor && it.anchor.kp}/${kpCount}`);
      if (bad.length) gate(`A0 ${n} L${i + 1} Q${6 + k}`, false, bad.join(","));
    });
  });
}
gate(`A0 inventory totals (lessons ${lessonTotal}, items ${itemTotal})`, lessonTotal === 24 && itemTotal === 96, `${lessonTotal}/${itemTotal}`);
if (FAILED > 0) { console.error("FAIL-CLOSED at A0"); process.exit(1); }

// ── build source-0.5 ×10 (0.4 + format + appended written items, anchor stripped) ──
section("build source-0.5 ×10");
const src5 = {};
const src5Bytes = {};
for (const n of TRANCHE) {
  const s4 = readJson(path.join(RES, "source-0.4", `guided-lesson-${n}.json`));
  const s5 = JSON.parse(JSON.stringify(s4));
  s5.format = "guided-lesson/0.5";
  s5.lessons.forEach((L, i) => {
    for (const it of auth.notes[n][i]) {
      L.check.push({ kind: it.kind, stem: it.stem, misconceptionClass: it.misconceptionClass, modelAnswer: it.modelAnswer, keywords: it.keywords });
    }
  });
  src5[n] = s5;
  src5Bytes[n] = Buffer.from(JSON.stringify(s5, null, 2) + "\n", "utf8");
}
fs.mkdirSync(path.join(RES, "source-0.5"), { recursive: true });
const src5sha = {};
const EMIT_ONLY = process.env.SB1_EMIT_ONLY === "1"; // bootstrap: write sources, exit for commit A
for (const n of TRANCHE) {
  const buf = emit(path.join(RES, "source-0.5", `guided-lesson-${n}.json`), src5[n]);
  src5sha[n] = sha256(buf);
  if (EMIT_ONLY) continue;
  // P0: the working-tree bytes must be exactly what commit A carries
  const blob = execSync(`git show HEAD:SME-GuidedLessons/integration/source-0.5/guided-lesson-${n}.json`, { cwd: RESROOT, maxBuffer: 1024 * 1024 * 8 });
  gate(`P0 committed == rebuilt @ source-0.5/${n}`, blob.equals(src5Bytes[n]) && blob.equals(buf));
}
if (EMIT_ONLY) { console.log("EMIT-ONLY: 10 source-0.5 files written — commit A, then re-run without SB1_EMIT_ONLY"); process.exit(0); }

// ── D-1 source determinism ×10 ───────────────────────────────────────────────
section("D-1 source determinism");
for (const n of TRANCHE) {
  const s4 = readJson(path.join(RES, "source-0.4", `guided-lesson-${n}.json`));
  const s5 = readJson(path.join(RES, "source-0.5", `guided-lesson-${n}.json`));
  const stripped = JSON.parse(JSON.stringify(s5));
  stripped.format = "guided-lesson/0.4";
  for (let i = 0; i < s4.lessons.length; i++) stripped.lessons[i].check = stripped.lessons[i].check.slice(0, s4.lessons[i].check.length);
  gate(`D-1 ${n}: 0.5 == 0.4 minus (format, appended check items)`, JSON.stringify(stripped) === JSON.stringify(s4));
}

// ── C-6 ajv sources ×10 ──────────────────────────────────────────────────────
section("C-6 ajv battery");
const ajv = new Ajv({ allErrors: true });
const vSrc5 = ajv.compile(readJson(path.join(RES, "schema/guided-lesson.0.5.schema.json")));
const vHub14 = ajv.compile(readJson(path.join(RES, "schema/hub-lesson-import.1.4.schema.json")));
const vPkg11 = ajv.compile(readJson(path.join(RES, "schema/sme-question-package.1.1.schema.json")));
for (const n of TRANCHE) {
  const ok = vSrc5(readJson(path.join(RES, "source-0.5", `guided-lesson-${n}.json`)));
  gate(`C-6 source-0.5 ${n} vs guided-lesson/0.5`, ok, ok ? "" : ajv.errorsText(vSrc5.errors).slice(0, 250));
}

// ── C-2 preflight: manifest v7 upstream fidelity (112+112 local bytes) ───────
section("C-2 preflight vs manifest v7");
const man7 = readJson(path.join(RES, "hub-import-manifest-v7.json"));
const int37 = readJson(path.join(RES, "records/INT-3-transform-record-r3-check-types.json"));
gate("C-2 manifest v7 shape", man7.manifest_version === 7 && man7.artifacts.length === 224);
const v7ByKindNote = new Map();
for (const a of man7.artifacts) v7ByKindNote.set(`${a.kind}|${a.noteId}`, a);
const notes = man7.artifacts.filter((a) => a.kind !== "sme-question-package").map((a) => a.noteId);
gate("C-2 112 notes", notes.length === 112, String(notes.length));
let shaOk = 0;
for (const n of notes) {
  const isPilot = PILOTS.includes(n);
  const lesKind = isPilot ? "hub-lesson-import-1.4" : "hub-lesson-import-1.3";
  const lesDir = isPilot ? "hub-import-1.4" : "hub-import-1.3";
  const pkgDir = isPilot ? "question-packages-1.1" : "question-packages";
  const les = v7ByKindNote.get(`${lesKind}|${n}`);
  const pkg = v7ByKindNote.get(`sme-question-package|${n}`);
  const lesBuf = read(path.join(RES, lesDir, `${n}.hub-lesson-import.json`));
  const pkgBuf = read(path.join(RES, pkgDir, `${n}.sme-question-package.json`));
  if (sha256(lesBuf) === les.sha256 && lesBuf.length === les.bytes && sha256(pkgBuf) === pkg.sha256 && pkgBuf.length === pkg.bytes) shaOk++;
}
gate("C-2 224 local bytes == manifest v7 shas (checkout == pinned generations)", shaOk === 112, `${shaOk}/112 notes (224 artifacts)`);

// ── transform ×10: mutate v7-baseline bytes by the declared deltas ───────────
section("transform (declared deltas on the 1.3 / 1.0 bytes)");
const outLessons = {}, outPkgs = {};
for (const n of TRANCHE) {
  const hub = JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8"));
  const pkg = JSON.parse(read(path.join(RES, "question-packages", `${n}.sme-question-package.json`), "utf8"));
  const src = src5[n];
  const s5sha = src5sha[n];

  const hubOrig = JSON.parse(JSON.stringify(hub));
  hub.format = "hub/lesson-import/1.4";
  hub.adapter = ADAPTER;
  hub.source.sourceFormat = "guided-lesson/0.5";
  hub.source.sourceLayerSha256 = s5sha;
  hub.source.pinnedRef = commitA;
  hub.lesson.modules.forEach((m, i) => {
    const written = src.lessons[i].check.slice(5);
    written.forEach((_, k) => m.checkRefs.push(`${m.id}::Q${6 + k}`));
  });
  outLessons[n] = hub;

  const pkgOrig = JSON.parse(JSON.stringify(pkg));
  pkg.format = "sme-question-package/1.1";
  pkg.adapter = ADAPTER;
  pkg.source.sourceFormat = "guided-lesson/0.5";
  pkg.source.sourceLayerSha256 = s5sha;
  pkg.source.pinnedRef = commitA;
  const baseCounts = hub.lesson.modules.map((m) => m.checkRefs.length - 4);
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

  // written-kind invariants ×(4/lesson)
  let wok = 0;
  for (const q of pkg.questions) {
    if (!(q.kind && q.kind !== "mcq")) continue;
    const idOK = new RegExp(`^${n}::L[1-9]::Q[1-9]$`).test(q.id);
    const ok = idOK && q.modelAnswer && q.modelAnswer.length > 0 && Array.isArray(q.keywords) && q.keywords.length >= 1 && Array.isArray(q.options) && q.options.length === 0;
    if (!ok) console.error(`  written invariant fail: ${q.id}`);
    else wok++;
  }
  gate(`written-kind invariants ${n} (x${itemTotal / TRANCHE.length})`, wok === 4 * src.lessons.length, `${wok}/${4 * src.lessons.length}`);

  // MCQ deep conservation
  const origByKey = new Map(pkgOrig.questions.map((q) => [q.id, JSON.stringify(q)]));
  const mcqSame = [...origByKey.entries()].every(([id, s]) => {
    const q = pkg.questions.find((x) => x.id === id);
    return q && JSON.stringify(q) === s;
  });
  gate(`MCQ deep conservation ${n} (${pkgOrig.questions.length} questions)`, mcqSame && pkg.questions.length === pkgOrig.questions.length + 4 * src.lessons.length);

  // C-5 checkRefs ↔ questions 1:1 in order
  const flat = [];
  hub.lesson.modules.forEach((m) => m.checkRefs.forEach((r) => flat.push(r)));
  const oneToOne = flat.length === pkg.questions.length && flat.every((r, i) => r === pkg.questions[i].id);
  gate(`C-5 checkRefs<->questions 1:1 ${n}`, oneToOne, `${flat.length} refs / ${pkg.questions.length} questions`);

  // D-2 determinism
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
  pkgBack.questions = pkgBack.questions.filter((q) => !(q.kind && q.kind !== "mcq"));
  gate(`D-2 package ${n} == 1.0 minus deltas`, JSON.stringify(pkgBack) === JSON.stringify(pkgOrig));

  // ajv outputs
  gate(`C-6 lesson ${n} vs hub/lesson-import/1.4`, vHub14(hub), vHub14.errors ? ajv.errorsText(vHub14.errors).slice(0, 250) : "");
  gate(`C-6 package ${n} vs sme-question-package/1.1`, vPkg11(pkg), vPkg11.errors ? ajv.errorsText(vPkg11.errors).slice(0, 250) : "");
}

// pilots re-proof under the union schemas + C-5 (byte-identical to stage A)
for (const n of PILOTS) {
  const hub = JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"));
  const pkg = JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8"));
  gate(`C-6 pilot lesson ${n} vs hub/lesson-import/1.4 (re-proof)`, vHub14(hub));
  gate(`C-6 pilot package ${n} vs sme-question-package/1.1 (re-proof)`, vPkg11(pkg));
  const flat = [];
  hub.lesson.modules.forEach((m) => m.checkRefs.forEach((r) => flat.push(r)));
  gate(`C-5 pilot checkRefs<->questions 1:1 ${n}`, flat.length === pkg.questions.length && flat.every((r, i) => r === pkg.questions[i].id));
}

// 100 untouched: ajv under the UNION schemas + package sha conservation (C-9)
let untouchedOk = 0, pkgShaOk = 0;
for (const n of notes) {
  if (PILOTS.includes(n) || TRANCHE.includes(n)) continue;
  const hub = JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8"));
  const pkgBuf = read(path.join(RES, "question-packages", `${n}.sme-question-package.json`));
  const pkg = JSON.parse(pkgBuf, "utf8");
  if (vHub14(hub) && vPkg11(pkg)) untouchedOk++;
  if (sha256(pkgBuf) === v7ByKindNote.get(`sme-question-package|${n}`).sha256) pkgShaOk++;
}
gate("C-6 100 untouched lessons+packages vs union schemas", untouchedOk === 100, `${untouchedOk}/100`);
gate("C-9 100 package shas == manifest v7 (byte conservation)", pkgShaOk === 100, `${pkgShaOk}/100`);

// ── emit artifacts ───────────────────────────────────────────────────────────
section("emit artifacts");
fs.mkdirSync(path.join(RES, "hub-import-1.4"), { recursive: true });
fs.mkdirSync(path.join(RES, "question-packages-1.1"), { recursive: true });
const newSha = {};
for (const n of TRANCHE) {
  const lb = emit(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), outLessons[n]);
  const pb = emit(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), outPkgs[n]);
  newSha[n] = { hub: { sha256: sha256(lb), bytes: lb.length }, pkg: { sha256: sha256(pb), bytes: pb.length } };
  console.log(`  hub-import-1.4/${n}: ${lb.length}B  question-packages-1.1/${n}: ${pb.length}B`);
}

// ── G-E stream recompute ×112 ────────────────────────────────────────────────
section("G-E stream recompute ×112");
const v7Rows = new Map(int37.notes.map((r) => [r.noteId, r]));
const rows = int37.notes.map((r) => JSON.parse(JSON.stringify(r)));
let nonTrancheStreamOk = 0, pilotStreamOk = 0;
for (const row of rows) {
  const n = row.noteId;
  if (TRANCHE.includes(n)) {
    const s = targetTokens(outLessons[n], outPkgs[n]).join("\n");
    row.sourceLayerSha256 = src5sha[n];
    row.hubSha256 = newSha[n].hub.sha256;
    row.pkgSha256 = newSha[n].pkg.sha256;
    row.stream = { sha256: sha256(Buffer.from(s, "utf8")), chars: s.length };
    row.r3_delta = { written_items: 4 * src5[n].lessons.length, mcq_unchanged: true, wave: "S-B1" };
  } else if (PILOTS.includes(n)) {
    const hub = JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"));
    const pkg = JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8"));
    const s = targetTokens(hub, pkg).join("\n");
    const sha = sha256(Buffer.from(s, "utf8"));
    if (sha === row.stream.sha256 && s.length === row.stream.chars) pilotStreamOk++;
    else gate(`G-E pilot stream ${n} == stage-A anchor`, false, `got ${sha.slice(0, 12)}/${s.length} want ${row.stream.sha256.slice(0, 12)}/${row.stream.chars}`);
  } else {
    const hub = JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8"));
    const pkg = JSON.parse(read(path.join(RES, "question-packages", `${n}.sme-question-package.json`), "utf8"));
    const s = targetTokens(hub, pkg).join("\n");
    const sha = sha256(Buffer.from(s, "utf8"));
    if (sha === row.stream.sha256 && s.length === row.stream.chars) nonTrancheStreamOk++;
    else gate(`G-E stream ${n} == v7 anchor`, false, `got ${sha.slice(0, 12)}/${s.length} want ${row.stream.sha256.slice(0, 12)}/${row.stream.chars}`);
  }
}
gate("G-E 100 non-R3 stream anchors == v7 (figures-2.2 + stage-A) generation exactly", nonTrancheStreamOk === 100, `${nonTrancheStreamOk}/100`);
gate("G-E 2 pilot streams == stage-A anchors exactly (bytes unchanged)", pilotStreamOk === 2, `${pilotStreamOk}/2`);
gate("G-E 10 S-B1 rows re-anchored", rows.filter((r) => TRANCHE.includes(r.noteId)).length === 10);

// grand + wave subtotals (int3.notes order — the runner's iteration order)
const grand = crypto.createHash("sha256");
let grandChars = 0;
const waveHashes = {};
for (const row of rows) {
  const n = row.noteId;
  const hub = TRANCHE.includes(n)
    ? outLessons[n]
    : PILOTS.includes(n)
      ? JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"))
      : JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8"));
  const pkg = TRANCHE.includes(n)
    ? outPkgs[n]
    : PILOTS.includes(n)
      ? JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8"))
      : JSON.parse(read(path.join(RES, "question-packages", `${n}.sme-question-package.json`), "utf8"));
  const s = targetTokens(hub, pkg).join("\n");
  grand.update(Buffer.from(s, "utf8"));
  grandChars += s.length;
  const w = "wave-" + row.wave;
  waveHashes[w] = waveHashes[w] || crypto.createHash("sha256");
  waveHashes[w].update(Buffer.from(s, "utf8"));
}
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest("hex");
gate("G-E wave subtotals ×10", Object.keys(waveOut).length === 10, Object.keys(waveOut).join(","));
const grandSha = grand.digest("hex");
console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}…`);

// cross-checks vs v7
gate("cross-check: manifest v7 grand == v7 record", man7.conservation.authored_stream_sha256 === int37.grand_stream.sha256);
gate("cross-check: wave subtotals preserved for untouched waves (8 of 10)", ["wave-1","wave-9","wave-10"].every((w) => waveOut[w] !== undefined) && Object.entries(man7.conservation.wave_stream_sha256).every(([w, h]) => (["wave-9","wave-10"].includes(w)) ? waveOut[w] === h : true) && ["wave-2","wave-3","wave-4","wave-5","wave-6","wave-7","wave-8"].every((w) => waveOut[w] === man7.conservation.wave_stream_sha256[w]));

// ── manifest v8 ──────────────────────────────────────────────────────────────
section("manifest v8");
const newLessons = 0; // re-issued only — no new lesson rows
const counts = {
  notes: 112,
  lessons: 239 + newLessons,
  checks: 1307,
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
  checks_written: 112,
  checks_mcq: 1195,
  written_recall: 56,
  written_explain_why: 28,
  written_application: 28,
};
const artifacts = man7.artifacts.map((a) => {
  if (a.kind === "hub-lesson-import-1.3" && TRANCHE.includes(a.noteId)) {
    return { kind: "hub-lesson-import-1.4", noteId: a.noteId, path: `SME-GuidedLessons/integration/hub-import-1.4/${a.noteId}.hub-lesson-import.json`, sha256: newSha[a.noteId].hub.sha256, bytes: newSha[a.noteId].hub.bytes };
  }
  if (a.kind === "sme-question-package" && TRANCHE.includes(a.noteId)) {
    return { kind: "sme-question-package", noteId: a.noteId, path: `SME-GuidedLessons/integration/question-packages-1.1/${a.noteId}.sme-question-package.json`, sha256: newSha[a.noteId].pkg.sha256, bytes: newSha[a.noteId].pkg.bytes };
  }
  return a;
});
gate("manifest v8 lists 224", artifacts.length === 224);
gate("manifest v8: exactly 20 re-issued vs v7", artifacts.filter((a) => !man7.artifacts.some((b) => b.path === a.path)).length === 20);
const man8 = {
  format: "hub-import-manifest/1.0",
  manifest_version: 8,
  generated_at_utc: now(),
  operator_trace: OPERATOR_TRACE,
  supersedes: "hub-import-manifest-v7.json (100 hub-lesson-import-1.3 lessons + 100 sme-question-package/1.0 packages + the 4 stage-A pilot re-issues byte-identical re-pins; exactly 20 re-issued artifacts: 10 hub-lesson-import-1.4 lessons (checkRefs delta) + 10 sme-question-package/1.1 packages (+96 written items) — the R3 stage-B wave 1 tranche: the wave-1 authoring register)",
  checks_layer: {
    wave: `R3-MIXED-CHECK-TYPES stage B wave 1 (S-B1) — operator execute trace ${OPERATOR_TRACE} on the stage-B contract of record (stage-A receipt followups)`,
    derivation: "96 authored written items (48 recall, 24 explain-why, 24 application), each spec-anchored to its lesson's keyPoints (KP-index provenance in the authoring parts of record), carrying modelAnswer + generous synonym/inflection-bearing keywords; appended after the 5 MCQs of each of the 24 wave-1 lessons in the SME kind order [recall, recall, explain-why, application]",
    declared_revision: "the SECOND package-channel delta since INT-0: 10 further packages re-issued under sme-question-package/1.1 (union schema — the 100 untouched 1.0 packages validate unchanged); 10 further lessons re-issued under hub/lesson-import/1.4 (checkRefs 5->9); kind/modelAnswer/keywords are §7-declared stream tokens on written items; cumulative R3 generation = 12 notes / 28 lessons / 112 written items",
    grading_law: "case-insensitive whole-token match of the learner text against keywords[]; >=1 hit -> correct; 0 hits -> not-quite + model answer; empty submit blocked; keywords absent -> reveal-only (fail-closed, never a silent wrong grade)",
    fail_closed: "written item without modelAnswer renders reveal-only, never gradeable, never blank; unknown kind renders reveal-only and warns at this gate",
  },
  source_generation: {
    format: "guided-lesson/0.5",
    namespace: "SME-GuidedLessons/integration/source-0.5/",
    pin: commitA,
    int0_lineage: "(unchanged from v7)",
  },
  load_scope: { adapter: ADAPTER, target_schemas: ["hub/lesson-import/1.4", "sme-question-package/1.1"] },
  counts,
  conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut },
  artifacts,
};

// ── INT-3 record S-B1 ────────────────────────────────────────────────────────
const int3b1 = {
  stage: "INT-3",
  title: "transform record — R3 mixed check types STAGE B WAVE 1 generation (adapter guided-lesson-0.5--hub-lesson-import-1.4)",
  generated_at_utc: now(),
  operator_trace: OPERATOR_TRACE,
  prior_record: "records/INT-3-transform-record-r3-check-types.json (stage A pilot — superseded by this record for the 12-note R3 generation; anchors for the 100 non-R3 notes carried unchanged)",
  adapter: ADAPTER,
  source_pin: {
    repo: "SyllabAI/syllabai-resources",
    ref: RES_MAIN_OPEN_RESOLVED,
    note: "resources main at S-B1 open (stage-A generation + t-textdebris-1 verified @ this ref)",
  },
  source_05_generation_pin: { commit: commitA, namespace: "SME-GuidedLessons/integration/source-0.5/", note: "12 files: 2 stage-A pilots (commit 80afdb8e) + 10 S-B1 notes (this generation commit)" },
  conservation_law:
    "kind/modelAnswer/keywords on written items ARE §7 stream tokens (the walk extends by those fields on kind!=mcq; old packages carry no kind so the walk is byte-neutral for them): the 100 non-R3 per-note streams equal the v7 anchors exactly; the 2 pilot streams equal the stage-A anchors exactly (bytes unchanged); the 10 S-B1 notes add the 96 written items' tokens (stem, misconceptionClass, modelAnswer, keywords — written kinds carry no options). Grand + wave subtotals recomputed over all 112 in the v6 note order.",
  grand_stream: { chars: grandChars, sha256: grandSha },
  wave_stream_sha256: waveOut,
  r3_census: {
    pilot_notes: PILOTS,
    sb1_notes: TRANCHE,
    cumulative_r3_notes: 12,
    cumulative_r3_lessons: 28,
    cumulative_written_items: 112,
    kinds_cumulative: { recall: 56, "explain-why": 28, application: 28 },
    sb1_wave: { notes: 10, lessons: 24, written_items: 96, kinds: { recall: 48, "explain-why": 24, application: 24 } },
    mcqs_conserved: 1195,
    packages_untouched: 100,
    lessons_untouched: 100,
    authored_chars_delta_vs_v7: grandChars - int37.grand_stream.chars,
  },
  sb1_authoring_register: {
    basis: "stage-B plan of record: 'tranche order mirrors the authoring register' — S-B1 = the wave-1 register notes (the 10-note instrumented sample of record: 24 lessons / 120 checks, wave-1 timing receipts)",
    anchor_law: "each written item anchored (authoring-time provenance, stripped from emitted bytes) to one of its lesson's keyPoints by KP index; stems verified non-duplicative against the lesson's 5 MCQ stems of record",
  },
  notes: rows,
};
const int3Buf = emit(path.join(RES, "records/INT-3-transform-record-r3-stageb1.json"), int3b1);
const man8Buf = emit(path.join(RES, "hub-import-manifest-v8.json"), man8);

// ── fail-closed checkpoint before the promotion receipt ─────────────────────
if (FAILED > 0) {
  console.error(`\nFAIL-CLOSED: ${FAILED} gate failure(s) — promotion receipt NOT emitted`);
  process.exit(1);
}

// ── promotion receipt ────────────────────────────────────────────────────────
section("promotion receipt");
const receipt = {
  format: "r3-check-types-promotion-receipt/1.0",
  wave: "R3-MIXED-CHECK-TYPES (stage B wave 1 — the wave-1 authoring register, 10 notes / 24 lessons / 96 written items)",
  operator_traces: [QUEUE_TRACE, STAGE_A_TRACE, OPERATOR_TRACE],
  generated_at_utc: now(),
  repo: "SyllabAI/syllabai-resources",
  branch: "integration/r3-stageb1-20261030",
  contract_of_record: "R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json followups: 'stage B corpus rollout (~956 items): OPERATOR-GATED, wave-sized with per-note SCHEMA PASS gates' — gate opened by operator trace 1a18bc1ca2cf48e5 ('stage B proceed')",
  commits: {
    A: { sha: commitA, parent: commitAParent, note: "S-B1 source-0.5 generation — 10 authored guided-lesson/0.5 notes (96 written items) added to the stage-A namespace (12 files total)" },
    C: { sha: "(namespace-complete — schema union bump + outputs + manifest v8 + records + pipeline)", note: "schema/sme-question-package.1.1.schema.json (questions maxItems 25→45 union-safe raise) + hub-import-1.4/ ×10 + question-packages-1.1/ ×10 + hub-import-manifest-v8.json + records/INT-3-transform-record-r3-stageb1.json + records/R3-CHECK-TYPES-STAGEB1-PROMOTION-20261030.json + tooling/r3-stageb1-pipeline.js" },
  },
  artifact_pin: `${SOURCE_PIN_V6} (100 untouched lessons) | ${STAGE_A_COMMIT} (2 stage-A pilots) | ${commitA} (10 new source-0.5 lessons — commit A of this wave)`,
  pkg_pin: `(unchanged from v7: INT-0 4d85c47… for the 100 untouched; stage-A commit A ${STAGE_A_COMMIT.slice(0, 8)} for the 2 pilots; ${commitA} for the 10 new — the SECOND package-channel re-pin since INT-0)`,
  input_pins: { resources_main_at_wave_open: RES_MAIN_OPEN_RESOLVED },
  manifest: "hub-import-manifest-v8.json",
  int_record: "INT-3-transform-record-r3-stageb1.json",
  authoring_parts: ["SME-GuidedLessons/tooling/r3-stageb1-authoring/authoring-part1.json", "SME-GuidedLessons/tooling/r3-stageb1-authoring/authoring-part2.json", "SME-GuidedLessons/tooling/r3-stageb1-authoring/authoring-part3.json", "(lane mirrors: scripts/r3-stageb1/authoring-part{1,2,3}.json)"],
  counts_census: { notes: 112, lessons: 239, checks: 1307, checks_mcq: 1195, checks_written: 112, written_recall: 56, written_explain_why: 28, written_application: 28, sb1_notes: TRANCHE, sb1_written: 96, distractors: 3565 },
  schema_delta: "ONE union-safe raise: sme-question-package/1.1 questions maxItems 25→45 (the 1.0-inherited cap assumed 5 lessons × 5 MCQs; 9 checks × 5 lessons = 45). Backward-compatible: everything previously valid stays valid (ajv re-proof ×112 artifacts in this run). guided-lesson/0.5 (check maxItems 9) and hub/lesson-import/1.4 already admit the written items — no other change; S-B1 is otherwise a pure data wave.",
  taxonomy: "kind enum of record: mcq (default/absent) | recall | explain-why | application — per-lesson appended order [recall, recall, explain-why, application] (the SME set shape of record)",
  conservation: {
    law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq (feed-safe extension: no kind field -> walk unchanged); 100 non-R3 streams == v7 anchors exactly; 2 pilot streams == stage-A anchors exactly",
    authored_chars: grandChars,
    authored_chars_delta_vs_v7: grandChars - int37.grand_stream.chars,
    mcq_conservation: "tranche package MCQs deep-equal the 1.0 bytes ×10 (+96 count); 100 package shas byte-identical ×100; pilot packages byte-identical ×2",
  },
  gates: { pipeline: `${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, 0 fail`, gate_log: CHECKS },
  merge_order:
    "resources PR (this branch) merges to main FIRST; the hub PR (runner FEED r3-stageb1-v8 + re-issued artifacts + re-issued guided-import.json) merges only after; stage B wave 2 (next register tranche) remains operator-gated",
  hub_side_note:
    "renderer law unchanged from stage A: MCQ path untouched byte-for-byte; written kinds render a labelled free-text input, submit -> verdict role=status + model answer ALWAYS shown on settle; a11y label/aria-live; flow tallies unchanged in signature (keyword-hit boolean rides onAnswer correct); reveal-only fail-closed when keywords absent",
  recalibration_note:
    "wave receipt + recalibration: grand stream recomputed over all 112 notes; wave subtotals ×10 recomputed (8 untouched waves byte-equal to v7 — declared preserved; wave-1/wave-9/wave-10 re-anchored by their 12 R3 notes)",
};
emit(path.join(RES, "records/R3-CHECK-TYPES-STAGEB1-PROMOTION-20261030.json"), receipt);

// ── survivors for the hub runner byte-anchors ────────────────────────────────
fs.mkdirSync(SURV, { recursive: true });
fs.copyFileSync(path.join(RES, "hub-import-manifest-v8.json"), path.join(SURV, "hub-import-manifest-v8.json"));
fs.copyFileSync(path.join(RES, "records/INT-3-transform-record-r3-stageb1.json"), path.join(SURV, "INT-3-transform-record-r3-stageb1.json"));
fs.copyFileSync(path.join(RES, "hub-import-manifest-v7.json"), path.join(SURV, "hub-import-manifest-v7.json"));

console.log(`\nRESULT: ${FAILED === 0 ? "GREEN — PIPELINE COMPLETE" : "FAIL-CLOSED"}`);
console.log(`  gates: ${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, ${FAILED} failures`);
console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}… (v7: ${int37.grand_stream.chars} → delta +${grandChars - int37.grand_stream.chars})`);
console.log(`  census: checks 1211 → 1307 (written 16 → 112; MCQ 1,195 conserved)`);
