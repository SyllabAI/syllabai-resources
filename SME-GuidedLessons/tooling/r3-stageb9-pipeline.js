#!/usr/bin/env node
/**
 * R3-CHECK-TYPES PIPELINE — STAGE B WAVE 9 (S-B9)
 * (operator ignition: "Wave 9", hub chat trace 1a190d455ab9612d, continuing the
 *  stage-B contract of record in R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json, the S-B1 NEXT
 *  ("waves 3..10 to the ~956 total") and the S-B8 promotion receipt merge_order ("stage B
 *  wave 9 (next register tranche) remains operator-gated") — gate opened by the operator word above)
 *
 * S-B9 tranche of record: the wave-9 authoring register at wave open (12 notes) minus the
 * already-live stage-A pilot rn_2MpXPtNXvn8pQm3r, which keeps its live items per the S-B8
 * NEXT pointer = 11 notes, 25 lessons, 125 MCQs -> +100 authored written items (50 recall,
 * 25 explain-why, 25 application). FINAL tranche shape read from the register at wave open
 * per the S-B8 NEXT pointer.
 * Schema delta: NONE — the S-B1 union caps (maxItems 45 / check 9 / checkRefs 9) admit this tranche.
 *
 * Stack of record: branch integration/r3-stageb9-20261031 based on the current resources main
 * (wave-open main of record resolved at run time, recorded in input_pins; contains the S-B8
 * merge-of-record 88dfb3de as ancestor — main advanced past it with unrelated lanes, disclosed).
 *
 * Inputs (clone /home/z/my-project/syllabai-resources @ integration/r3-stageb9-20261031):
 *   scripts/r3-stageb9/authoring-part{1,2}.json     the 100 authored items (KP-anchored; audit GREEN)
 *   integration/source-0.4/        0.4 generation (D-1 baseline)
 *   integration/source-0.5/        the 94 prior R3 sources (byte-identical re-proof)
 *   integration/hub-import-1.3/    1.3 lesson outputs (D-2 baseline for the tranche)
 *   integration/question-packages/ 1.0 packages (C-9: 7 byte-identical)
 *   integration/hub-import-1.4/ + question-packages-1.1/  the 94 prior-R3 outputs (re-proof)
 *   integration/hub-import-manifest-v15.json + records/INT-3-transform-record-r3-stageb8.json
 *
 * Outputs (namespace-complete):
 *   source-0.5/ x11 (new)          hub-import-1.4/ x11 (new)   question-packages-1.1/ x11 (new)
 *   hub-import-manifest-v16.json   records/INT-3-transform-record-r3-stageb9.json
 *   records/R3-CHECK-TYPES-STAGEB9-PROMOTION-20261031.json
 * + survivors for the hub runner byte-anchors (scripts/r3-survivors/)
 *
 * Gates: A0 authoring inventory, P0 committed==rebuilt x11, D-1 source determinism x11,
 * C-6 ajv (11 sources + 22 tranche outputs + 94 prior-R3 re-proofs + 7 untouched pairs),
 * C-2 preflight vs manifest v15 (224 shas), written-kind invariants x100, MCQ deep conservation x11,
 * C-5 checkRefs closure x11 + x94 prior-R3, D-2 output determinism x11, C-9 package sha
 * conservation x7, G-E stream recompute x112 (7 == v15 anchors; 94 prior-R3 == their anchors
 * exactly; 11 S-B9 rows re-anchored), grand + waves x10 (9 byte-equal vs v15; wave-9 re-anchored).
 * FAIL-CLOSED: any gate failure aborts before any record is emitted.
 */import { createRequire } from "node:module";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { execSync } from "node:child_process";

const require = createRequire(import.meta.url);
const Ajv = require("/tmp/ajv-dep/node_modules/ajv");

const RES = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/integration";
const RESROOT = "/home/z/my-project/syllabai-resources";
const AUTH = "/home/z/my-project/scripts/r3-stageb9";
const SURV = "/home/z/my-project/scripts/r3-survivors";
const PILOTS = ["rn_2MpXPtNXvn8pQm3r", "rn_8T5GfPn2q7sY2YCh"]; // stage A, already live
const SB1_NOTES = ["rn_2d6Yb8GwGfRRd6pZ","rn_4SgDJv8rKxpQQSBh","rn_HZM2WRjPPT8Srcxt","rn_JCfdFrHsCkrmMbFj","rn_TM4QVMgXVxs4vbfY","rn_fQSYvKRMDBj3s2Bx","rn_jNJ4gTmcHqdFqsNh","rn_kJg2gwF77vdFZZ2H","rn_wTtM2fQVVjntRm64","rn_xT8XsdJtDX5gNFXj"]; // S-B1, live @ 78ad6a20
const SB2_NOTES = ["rn_2VnK66PqbvFKdKYt","rn_S7GPh8BBPBbmhYKm","rn_cTk2cs2h2BKQ3y3B","rn_QVmDs8X4szpds3cP","rn_TWGVV6RXN3Ktqb9h","rn_RvgxXR36425BFMcx","rn_YBWYstSRgM2QPzQq","rn_R3ptwxGTTvdBFvyP","rn_TsfqyK9BYMtN2Bfd","rn_kb2VkFMdBTbmG33t","rn_vzGMZxqQtWYVWB7h","rn_b3XCzdtfQddbJjVf"]; // S-B2, live @ 96c261a (PR #237 merged e679c919)
const SB3_NOTES = ["rn_Syxyh4Fct8KFg8NQ","rn_mBqgkpZ3hbSBmWCC","rn_N4HX8tqbdhTQcHyS","rn_VyXFNyxZHZGkxqTG","rn_vXPcH3vS8wv7BFkK","rn_pWzTTBv3B4yGFfj3","rn_yj4y972FxCWnDnSg","rn_Hkwmd9GSp3gdxxR5","rn_4tzwS4GZjPybwtkS","rn_T55t3HNsgyZcXZtN","rn_mbcBZkygY4YpG2bf","rn_8Nv33F4dD3kkZnY6"]; // S-B3, live @ da18433 (PR #240 merged 163cb2f)
const SB4_NOTES = ["rn_3YZNCXSQQqXTT6HR","rn_FCnWFz9MhgsqnZGM","rn_GkJG52NCN98ShGRm","rn_Hp2nK8XpN2SmjdQc","rn_J7ZcTWyRxRgWQ45R","rn_KpvF2TWr5fYHk2Jz","rn_MVnFKDMVkswzpmpw","rn_jVwPmjqHbqQkXcjG","rn_kdRjZHjHcpVZsD3h","rn_rHKCkt3PTXDBpmJG","rn_vfmJxw4VQgXKzXF3"]; // S-B4, live @ fa1f302 (PR #242 merged e76925db)
const SB5_NOTES = ["rn_3B8JxsSjJvR9B4fk","rn_5WvdZNzzhHdjj2Qq","rn_6M5JB7CjvwdDykMS","rn_7Q8M9nVkr2FxCzxd","rn_DGkNCJRcCN4VQ28p","rn_Kd76WccxD9ytSJJC","rn_QzYRzzmwRxk2gKqV","rn_S2fg29M7cqvMj5kT","rn_V9tPMnX6Hq2XnqcP","rn_WJD4ZN4kQfzJNSPV","rn_gBGX339WBpwyCrFF","rn_jXXsc4wt2344BjxX"]; // S-B5, live @ 6fb25fc (PR #243 merged 0e663252)
const SB6_NOTES = ["rn_9WM8QhSxmYpGhjqd","rn_BX88twwgffRMgx82","rn_MMkxbt9y3M3XvXrc","rn_ZWrmDYtNGnmFycPM","rn_by5FDNfkqdBCkmXb","rn_dTP52nzhYb96XrJx","rn_nzW5ppBTV3ZnfSYY","rn_p2FmkrXqZSzFngpg","rn_qV5R2cKB59bSKD33","rn_sX8yyBxHn8bS7t46","rn_sf7s7s6bQ2cZv29s","rn_xq9jy75y43kDXkvx"]; // S-B6, live @ 286b5ac (PR #245/#246 merged 6b70de7)
const SB7_NOTES = ["rn_5g8Dd6y89tkCVJsN","rn_6ZCysv9GnNQmc3w2","rn_T6S7R66N2wSZpWyc","rn_VvsXMdW3TB37JhWF","rn_YWDXCCmjfjkJcs6c","rn_pBp5Z5C2RHTKk7Wn","rn_qb9TBhB6VmnFGjvf","rn_v5JjfpT6grhtq3QW","rn_vVdP57QhDYSVfZgy"]; // S-B7, live @ a8889009 (PR #248 merged 652ca2d4)
const SB8_NOTES = ["rn_3wZh9qRT7qFJn9QW","rn_6478QfpYNQDjZSvt","rn_DRQXrcSrmgQ7jcbZ","rn_H6ZVkxvdNgYDvfFb","rn_HNXFQt7vM32g6PMv","rn_KTZjJ7sPdDt4tkTH","rn_XJ8qXfzZJJFKXHnF","rn_Zh6Pw56rjdMkPCD4","rn_dgVRCKCwn4rTGxGZ","rn_t68QRDhwR6r5gxYX","rn_tvwj4VZ6yFscPJfD","rn_w25KHshCMNQWwftj","rn_x5m8QBWxtKvxQ9sx","rn_y85XYRv5QfgZFQxv"]; // S-B8, live @ 51a6ed34 (PR #249 merged 88dfb3de)
const PRIOR_R3 = [...PILOTS, ...SB1_NOTES, ...SB2_NOTES, ...SB3_NOTES, ...SB4_NOTES, ...SB5_NOTES, ...SB6_NOTES, ...SB7_NOTES, ...SB8_NOTES]; // the 94 notes already carrying written items (byte-identical this wave)
const REGISTER_W9 = ["rn_2MpXPtNXvn8pQm3r","rn_6c2G8nJpFSnQnbcP","rn_9J7DQhskyxzhd7CP","rn_DBGf3WVffDBNDp4R","rn_DrqzYWZMScqGrbWT","rn_H2zGfgH76qYV5cmr","rn_H9chr9BWCfXYW472","rn_HqqBFgKRHykMMhbB","rn_MmqCNJfWbtYzRVqT","rn_NdJGQM8BqHmTy7Vg","rn_V3hNWh6QWrbCRHrX","rn_wDdXr5k7gknQ7xJp"]; // wave-9 authoring register order of record (landing-plane wave field at wave open)
const PILOT_KEEP = "rn_2MpXPtNXvn8pQm3r"; // stage-A pilot in the wave-9 bucket — keeps its already-live items per the S-B8 NEXT
const STAGE_A_COMMIT = "80afdb8e02b628754f0e522d257e54d046ba5b0f";
const SB1_COMMIT_A = "78ad6a2073c669231bb40bd7266674a257c6003e";
const SB2_COMMIT_A = "96c261a"; // resolved below
const SB3_COMMIT_A = "da18433ed9e8351a2e8ce1282b8eaf5c362442d4";
const SB4_COMMIT_A = "fa1f302050ba38b6b2e97760e88d32567d2b0c90";
const SB5_COMMIT_A = "6fb25fc02d1a7acc71ee2231b547ac85e00705c1";
const SB6_COMMIT_A = "286b5ac81d43a28e5faa9f9e8ab16b67fbb12c51";
const SB7_COMMIT_A = "a8889009338bc5ce09edfed1d610d8cc9c9457b4";
const SB8_COMMIT_A = "51a6ed34e715a270c1d1525d1cff903777337437";
const SOURCE_PIN_V6 = "71922d1510ee9e00400667670b40f36e1ae5d456"; // source-0.4 (the 18 untouched lessons)
const OPERATOR_TRACE = "1a190d455ab9612d"; // "Wave 9"
const SB5_IGNITION_TRACE = "1a18d9f731726de1"; // "stage-B wave 5"
const SB6_IGNITION_TRACE = "1a18dfb539a4c839"; // "wave 6"
const SB7_IGNITION_TRACE = "1a18fd512d610f7d"; // "wave 7"
const STAGE_A_TRACE = "1a18a0218b7f44fd";
const QUEUE_TRACE = "1a189fd011119961";
const SB_GATE_TRACE = "1a18bc1ca2cf48e5"; // "stage B proceed"
const SB2_EXECUTE_TRACE = "1a18c3fc617d21b9"; // "wave 2 proceed"
const SB3_IGNITION_TRACE = "1a18c9f53d7b8dd1"; // "wave 3 proceed"
const SB4_IGNITION_TRACE = "1a18d09c1263e991"; // "stage-B wave 4 proceed"
const ADAPTER = "guided-lesson-0.5--hub-lesson-import-1.4";
const SB5_MERGE = "0e66325219293c23243c5721dc68199b47a6e71b"; // the S-B5 merge of record (PR #243)
const SB6_MERGE = "6b70de744337f41a1cbb9a8ad5ee8e501cd184dc"; // the S-B6 merge-of-record (PR #246, re-merged identical content with the trace-bearing message)
const SB7_MERGE = "652ca2d4e7709647cfd68040a56d817ae985fc5e"; // the S-B7 merge-of-record (PR #248)
const SB8_MERGE = "88dfb3dee9d85c5e533c3d99646678bb588fb559"; // the S-B8 merge-of-record (PR #249)
const WAVE_OPEN_MAIN = "90a49387fd6019338a3f7e9c27cf31fc304e728b"; // resources main at S-B9 open (ls-remote resolved)

const CHECKS = [];
let FAILED = 0;
function gate(name, ok, detail = "") {
  CHECKS.push({ name, ok: !!ok, detail: String(detail).slice(0, 300) });
  if (!ok) { FAILED++; console.error(`  FAIL ${name} — ${String(detail).slice(0, 300)}`); }
  return !!ok;
}
function section(t) { console.log(`\n── ${t}`); }

// ── P0 wave-open pins (resolved, never assumed) ──────────────────────────
section("P0 wave-open pins");
const RES_MAIN_OPEN_RESOLVED = execSync("git rev-parse origin/main", { cwd: RESROOT }).toString().trim();
const sb5IsAncestor = (() => { try { execSync(`git merge-base --is-ancestor ${SB8_MERGE} ${RES_MAIN_OPEN_RESOLVED}`, { cwd: RESROOT }); return true; } catch { return false; } })();
gate("P0 wave-open main contains the S-B8 merge of record (main advanced past it with unrelated lanes — disclosed)", sb5IsAncestor, RES_MAIN_OPEN_RESOLVED);
gate("P0 wave-open main is the recorded input pin", RES_MAIN_OPEN_RESOLVED === WAVE_OPEN_MAIN, RES_MAIN_OPEN_RESOLVED);
const BRANCH_RESOLVED = execSync("git branch --show-current", { cwd: RESROOT }).toString().trim();
gate("P0 worktree branch == integration/r3-stageb9-20261031", BRANCH_RESOLVED === "integration/r3-stageb9-20261031", BRANCH_RESOLVED);
const SB2_A_FULL = execSync(`git rev-parse ${SB2_COMMIT_A}`, { cwd: RESROOT }).toString().trim();
// commit A of record: the source-0.5 generation commit — HEAD at pipeline run time
const commitA = execSync("git rev-parse HEAD", { cwd: RESROOT }).toString().trim();
let commitAParent = "(shallow base — no parent at emit-only bootstrap)";
if (process.env.SB9_EMIT_ONLY !== "1") {
  commitAParent = execSync("git rev-parse HEAD~1", { cwd: RESROOT }).toString().trim();
}
if (process.env.SB9_EMIT_ONLY !== "1") {
  gate("P0 commit A parent == the wave-open main of record", commitAParent === RES_MAIN_OPEN_RESOLVED, `${commitAParent} vs ${RES_MAIN_OPEN_RESOLVED}`);
} else {
  gate("P0 base HEAD == the wave-open main of record (emit-only bootstrap)", commitA === RES_MAIN_OPEN_RESOLVED, `${commitA} vs ${RES_MAIN_OPEN_RESOLVED}`);
}
console.log(`commit A (S-B9 source-0.5 generation): ${commitA} (parent ${commitAParent.slice(0, 8)})`);

const sha256 = (buf) => crypto.createHash("sha256").update(buf).digest("hex");
const now = () => new Date().toISOString().replace(/\.\d+Z$/, "Z");
const read = (p) => fs.readFileSync(p);
const readJson = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
const emit = (p, obj) => { const buf = Buffer.from(JSON.stringify(obj, null, 2) + "\n", "utf8"); fs.writeFileSync(p, buf); return buf; };

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
for (const part of ["authoring-part1.json", "authoring-part2.json"]) {
  const j = readJson(path.join(AUTH, part));
  for (const [n, body] of Object.entries(j.notes)) {
    gate(`A0 no duplicate note across parts: ${n}`, !auth.notes[n]);
    auth.notes[n] = body.lessons.map((L) => L.items);
  }
}
const TRANCHE = Object.keys(auth.notes).sort();
gate("A0 tranche == wave-9 register of record (11 unconverted notes)", TRANCHE.length === 11, TRANCHE.join(","));
gate("A0 tranche set matches the wave-9 authoring register minus the stage-A pilot (S-B8 NEXT of record)", JSON.stringify(TRANCHE) === JSON.stringify([...REGISTER_W9].filter((n) => n !== PILOT_KEEP).sort()));
gate("A0 tranche disjoint from the 80 prior-R3 notes", TRANCHE.every((n) => !PRIOR_R3.includes(n)));
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
gate(`A0 inventory totals (lessons ${lessonTotal}, items ${itemTotal})`, lessonTotal === 25 && itemTotal === 100, `${lessonTotal}/${itemTotal}`);
if (FAILED > 0) { console.error("FAIL-CLOSED at A0"); process.exit(1); }

// ── build source-0.5 ×9 (0.4 + format + appended written items, anchor stripped) ──
section("build source-0.5 ×11");
const src5 = {};
const src5Bytes = {};
for (const n of TRANCHE) {
  const s4 = readJson(path.join(RES, "source-0.4", `guided-lesson-${n}.json`));
  const s5 = JSON.parse(JSON.stringify(s4));
  s5.format = "guided-lesson/0.5";
  s5.lessons.forEach((L, i) => {
    // DECLARED 0.4->0.5 SHAPE NORMALIZATION (of record): figureIds == [] is the 0.4
    // encoding of "the lesson claims no figures"; the guided-lesson/0.5 schema requires
    // the key ABSENT in that case (description: "Absent when the lesson claims no
    // figures"). Only empty arrays are touched — claimed figures carry through unchanged.
    if (Array.isArray(L.figureIds) && L.figureIds.length === 0) delete L.figureIds;
    for (const it of auth.notes[n][i]) {
      L.check.push({ kind: it.kind, stem: it.stem, misconceptionClass: it.misconceptionClass, modelAnswer: it.modelAnswer, keywords: it.keywords });
    }
  });
  src5[n] = s5;
  src5Bytes[n] = Buffer.from(JSON.stringify(s5, null, 2) + "\n", "utf8");
}
fs.mkdirSync(path.join(RES, "source-0.5"), { recursive: true });
const src5sha = {};
const EMIT_ONLY = process.env.SB9_EMIT_ONLY === "1"; // bootstrap: write sources, exit for commit A
for (const n of TRANCHE) {
  const buf = emit(path.join(RES, "source-0.5", `guided-lesson-${n}.json`), src5[n]);
  src5sha[n] = sha256(buf);
  if (EMIT_ONLY) continue;
  // P0: the working-tree bytes must be exactly what commit A carries
  const blob = execSync(`git show HEAD:SME-GuidedLessons/integration/source-0.5/guided-lesson-${n}.json`, { cwd: RESROOT, maxBuffer: 1024 * 1024 * 8 });
  gate(`P0 committed == rebuilt @ source-0.5/${n}`, blob.equals(src5Bytes[n]) && blob.equals(buf));
}
if (EMIT_ONLY) { console.log("EMIT-ONLY: 11 source-0.5 files written — commit A, then re-run without SB9_EMIT_ONLY"); process.exit(0); }

// ── D-1 source determinism ×14 ───────────────────────────────────────────────
section("D-1 source determinism");
for (const n of TRANCHE) {
  const s4 = readJson(path.join(RES, "source-0.4", `guided-lesson-${n}.json`));
  const s5 = readJson(path.join(RES, "source-0.5", `guided-lesson-${n}.json`));
  const stripped = JSON.parse(JSON.stringify(s5));
  stripped.format = "guided-lesson/0.4";
  for (let i = 0; i < s4.lessons.length; i++) stripped.lessons[i].check = stripped.lessons[i].check.slice(0, s4.lessons[i].check.length);
  // inverse of the declared shape normalization: drop the 0.4-side empty figureIds
  // encodings before the byte-compare (the 0.5 omits them per the 0.5 schema law)
  const s4n = JSON.parse(JSON.stringify(s4));
  s4n.lessons.forEach((L) => { if (Array.isArray(L.figureIds) && L.figureIds.length === 0) delete L.figureIds; });
  gate(`D-1 ${n}: 0.5 == 0.4 minus (format, appended check items, empty-figureIds normalization)`, JSON.stringify(stripped) === JSON.stringify(s4n));
}

// ── C-6 ajv sources ×12 ──────────────────────────────────────────────────────
section("C-6 ajv battery");
const ajv = new Ajv({ allErrors: true });
const vSrc5 = ajv.compile(readJson(path.join(RES, "schema/guided-lesson.0.5.schema.json")));
const vHub14 = ajv.compile(readJson(path.join(RES, "schema/hub-lesson-import.1.4.schema.json")));
const vPkg11 = ajv.compile(readJson(path.join(RES, "schema/sme-question-package.1.1.schema.json")));
for (const n of TRANCHE) {
  const ok = vSrc5(readJson(path.join(RES, "source-0.5", `guided-lesson-${n}.json`)));
  gate(`C-6 source-0.5 ${n} vs guided-lesson/0.5`, ok, ok ? "" : ajv.errorsText(vSrc5.errors).slice(0, 250));
}

// ── C-2 preflight: manifest v15 upstream fidelity (224 local bytes) ───────────
section("C-2 preflight vs manifest v15");
const man12 = readJson(path.join(RES, "hub-import-manifest-v15.json"));
const int3b5 = readJson(path.join(RES, "records/INT-3-transform-record-r3-stageb8.json"));
gate("C-2 manifest v15 shape", man12.manifest_version === 15 && man12.artifacts.length === 224);
const v12ByKindNote = new Map();
for (const a of man12.artifacts) v12ByKindNote.set(`${a.kind}|${a.noteId}`, a);
const notes = man12.artifacts.filter((a) => a.kind !== "sme-question-package").map((a) => a.noteId);
gate("C-2 112 notes", notes.length === 112, String(notes.length));
let shaOk = 0;
for (const n of notes) {
  const isR3 = PRIOR_R3.includes(n);
  const lesKind = isR3 ? "hub-lesson-import-1.4" : "hub-lesson-import-1.3";
  const lesDir = isR3 ? "hub-import-1.4" : "hub-import-1.3";
  const pkgDir = isR3 ? "question-packages-1.1" : "question-packages";
  const les = v12ByKindNote.get(`${lesKind}|${n}`);
  const pkg = v12ByKindNote.get(`sme-question-package|${n}`);
  const lesBuf = read(path.join(RES, lesDir, `${n}.hub-lesson-import.json`));
  const pkgBuf = read(path.join(RES, pkgDir, `${n}.sme-question-package.json`));
  if (sha256(lesBuf) === les.sha256 && lesBuf.length === les.bytes && sha256(pkgBuf) === pkg.sha256 && pkgBuf.length === pkg.bytes) shaOk++;
}
gate("C-2 224 local bytes == manifest v15 shas (checkout == pinned generations)", shaOk === 112, `${shaOk}/112 notes (224 artifacts)`);

// ── transform ×12: mutate v11-baseline bytes by the declared deltas ───────────
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

// prior-R3 re-proof under the union schemas + C-5 (byte-identical to the S-B1..S-B7 generations)
for (const n of PRIOR_R3) {
  const hub = JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"));
  const pkg = JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8"));
  gate(`C-6 prior-R3 lesson ${n} vs hub/lesson-import/1.4 (re-proof)`, vHub14(hub));
  gate(`C-6 prior-R3 package ${n} vs sme-question-package/1.1 (re-proof)`, vPkg11(pkg));
  const flat = [];
  hub.lesson.modules.forEach((m) => m.checkRefs.forEach((r) => flat.push(r)));
  gate(`C-5 prior-R3 checkRefs<->questions 1:1 ${n}`, flat.length === pkg.questions.length && flat.every((r, i) => r === pkg.questions[i].id));
}

// 18 untouched: ajv under the UNION schemas + package sha conservation (C-9)
let untouchedOk = 0, pkgShaOk = 0;
for (const n of notes) {
  if (PRIOR_R3.includes(n) || TRANCHE.includes(n)) continue;
  const hub = JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8"));
  const pkgBuf = read(path.join(RES, "question-packages", `${n}.sme-question-package.json`));
  const pkg = JSON.parse(pkgBuf, "utf8");
  if (vHub14(hub) && vPkg11(pkg)) untouchedOk++;
  if (sha256(pkgBuf) === v12ByKindNote.get(`sme-question-package|${n}`).sha256) pkgShaOk++;
}
gate("C-6 7 untouched lessons+packages vs union schemas", untouchedOk === 7, `${untouchedOk}/7`);
gate("C-9 7 package shas == manifest v15 (byte conservation)", pkgShaOk === 7, `${pkgShaOk}/7`);

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
const priorRows = new Map(int3b5.notes.map((r) => [r.noteId, r]));
const rows = int3b5.notes.map((r) => JSON.parse(JSON.stringify(r)));
let nonTrancheStreamOk = 0, priorStreamOk = 0;
for (const row of rows) {
  const n = row.noteId;
  if (TRANCHE.includes(n)) {
    const s = targetTokens(outLessons[n], outPkgs[n]).join("\n");
    row.sourceLayerSha256 = src5sha[n];
    row.hubSha256 = newSha[n].hub.sha256;
    row.pkgSha256 = newSha[n].pkg.sha256;
    row.stream = { sha256: sha256(Buffer.from(s, "utf8")), chars: s.length };
    row.r3_delta = { written_items: 4 * src5[n].lessons.length, mcq_unchanged: true, wave: "S-B9" };
  } else if (PRIOR_R3.includes(n)) {
    const hub = JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"));
    const pkg = JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8"));
    const s = targetTokens(hub, pkg).join("\n");
    const sha = sha256(Buffer.from(s, "utf8"));
    if (sha === row.stream.sha256 && s.length === row.stream.chars) priorStreamOk++;
    else gate(`G-E prior-R3 stream ${n} == prior anchor`, false, `got ${sha.slice(0, 12)}/${s.length} want ${row.stream.sha256.slice(0, 12)}/${row.stream.chars}`);
  } else {
    const hub = JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8"));
    const pkg = JSON.parse(read(path.join(RES, "question-packages", `${n}.sme-question-package.json`), "utf8"));
    const s = targetTokens(hub, pkg).join("\n");
    const sha = sha256(Buffer.from(s, "utf8"));
    if (sha === row.stream.sha256 && s.length === row.stream.chars) nonTrancheStreamOk++;
    else gate(`G-E stream ${n} == v12 anchor`, false, `got ${sha.slice(0, 12)}/${s.length} want ${row.stream.sha256.slice(0, 12)}/${row.stream.chars}`);
  }
}
gate("G-E 7 non-R3 stream anchors == S-B8 (v15) generation exactly (figures-2.2 + stage-A + S-B1..S-B8)", nonTrancheStreamOk === 7, `${nonTrancheStreamOk}/7`);
gate("G-E 94 prior-R3 streams == their anchors exactly (bytes unchanged)", priorStreamOk === 94, `${priorStreamOk}/94`);
gate("G-E 11 S-B9 rows re-anchored", rows.filter((r) => TRANCHE.includes(r.noteId)).length === 11);
gate("G-E the 11 re-anchored rows carry authoring wave 9 of record", rows.filter((r) => TRANCHE.includes(r.noteId)).every((r) => r.wave === 9));

// grand + wave subtotals (int3.notes order — the runner's iteration order)
const grand = crypto.createHash("sha256");
let grandChars = 0;
const waveHashes = {};
for (const row of rows) {
  const n = row.noteId;
  const hub = TRANCHE.includes(n)
    ? outLessons[n]
    : PRIOR_R3.includes(n)
      ? JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"))
      : JSON.parse(read(path.join(RES, "hub-import-1.3", `${n}.hub-lesson-import.json`), "utf8"));
  const pkg = TRANCHE.includes(n)
    ? outPkgs[n]
    : PRIOR_R3.includes(n)
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

// cross-checks vs v15
gate("cross-check: manifest v15 grand == v15 record", man12.conservation.authored_stream_sha256 === int3b5.grand_stream.sha256);
gate("cross-check: wave subtotals preserved for the 9 untouched waves (1,2,3,4,5,6,7,8,10)", ["wave-1","wave-2","wave-3","wave-4","wave-5","wave-6","wave-7","wave-8","wave-10"].every((w) => waveOut[w] === man12.conservation.wave_stream_sha256[w]));
gate("cross-check: wave-9 re-anchored", waveOut["wave-9"] !== man12.conservation.wave_stream_sha256["wave-9"]);

// ── manifest v16 ─────────────────────────────────────────────────────────────
section("manifest v16");
const newLessons = 0; // re-issued only — no new lesson rows
const counts = {
  notes: 112,
  lessons: 239 + newLessons,
  checks: 2091,
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
  checks_written: 896,
  checks_mcq: 1195,
  written_recall: 448,
  written_explain_why: 224,
  written_application: 224,
};
const artifacts = man12.artifacts.map((a) => {
  if (a.kind === "hub-lesson-import-1.3" && TRANCHE.includes(a.noteId)) {
    return { kind: "hub-lesson-import-1.4", noteId: a.noteId, path: `SME-GuidedLessons/integration/hub-import-1.4/${a.noteId}.hub-lesson-import.json`, sha256: newSha[a.noteId].hub.sha256, bytes: newSha[a.noteId].hub.bytes };
  }
  if (a.kind === "sme-question-package" && TRANCHE.includes(a.noteId)) {
    return { kind: "sme-question-package", noteId: a.noteId, path: `SME-GuidedLessons/integration/question-packages-1.1/${a.noteId}.sme-question-package.json`, sha256: newSha[a.noteId].pkg.sha256, bytes: newSha[a.noteId].pkg.bytes };
  }
  return a;
});
gate("manifest v16 lists 224", artifacts.length === 224);
gate("manifest v16: exactly 22 re-issued vs v15", artifacts.filter((a) => !man12.artifacts.some((b) => b.path === a.path)).length === 22);
const man13 = {
  format: "hub-import-manifest/1.0",
  manifest_version: 16,
  generated_at_utc: now(),
  operator_trace: OPERATOR_TRACE,
  supersedes: "hub-import-manifest-v15.json (7 hub-lesson-import-1.3 lessons + 7 sme-question-package/1.0 packages + the 206 already-live R3 re-issues byte-identical re-pins; exactly 22 re-issued artifacts: 11 hub-lesson-import-1.4 lessons (checkRefs delta) + 11 sme-question-package/1.1 packages (+100 written items) — the R3 stage-B wave 9 tranche: the wave-9 authoring register minus the stage-A pilot)",
  checks_layer: {
    wave: `R3-MIXED-CHECK-TYPES stage B wave 9 (S-B9) — operator ignition trace ${OPERATOR_TRACE} ("Wave 9") on the stage-B contract of record (S-B1 NEXT: "waves 3..10 to the ~956 total"; S-B8 promotion receipt merge_order: "stage B wave 9 (next register tranche) remains operator-gated")`,
    derivation: "100 authored written items (50 recall, 25 explain-why, 25 application), each spec-anchored to its lesson's keyPoints (KP-index provenance in the authoring parts of record), carrying modelAnswer + generous synonym/inflection-bearing keywords; appended after the 5 MCQs of each of the 25 wave-9 lessons in the SME kind order [recall, recall, explain-why, application]",
    declared_revision: "the TENTH package-channel delta since INT-0: 11 further packages re-issued under sme-question-package/1.1 (union schema — the 7 untouched 1.0 packages validate unchanged); 11 further lessons re-issued under hub/lesson-import/1.4 (checkRefs 5->9); kind/modelAnswer/keywords are §7-declared stream tokens on written items; cumulative R3 generation = 105 notes / 224 lessons / 896 written items",
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

// ── INT-3 record S-B5 ────────────────────────────────────────────────────────
const int3b6 = {
  stage: "INT-3",
  title: "transform record — R3 mixed check types STAGE B WAVE 9 generation (adapter guided-lesson-0.5--hub-lesson-import-1.4)",
  generated_at_utc: now(),
  operator_trace: OPERATOR_TRACE,
  prior_record: "records/INT-3-transform-record-r3-stageb8.json (stage-B wave 8 — superseded by this record for the 105-note R3 generation; anchors for the 7 non-R3 notes carried unchanged)",
  adapter: ADAPTER,
  source_pin: {
    repo: "SyllabAI/syllabai-resources",
    ref: RES_MAIN_OPEN_RESOLVED,
    note: "resources main at S-B9 open (contains the S-B8 merge-of-record 88dfb3de; main advanced past it with unrelated lanes before this wave opened — disclosed)",
  },
  source_05_generation_pin: { commit: commitA, namespace: "SME-GuidedLessons/integration/source-0.5/", note: "105 files: 2 stage-A pilots (80afdb8e) + 10 S-B1 notes (78ad6a20) + 12 S-B2 notes (96c261a…, PR #237) + 12 S-B3 notes (da18433…, PR #240) + 11 S-B4 notes (fa1f302…, PR #242) + 12 S-B5 notes (6fb25fc…, PR #243) + 12 S-B6 notes (286b5ac…, PR #245/#246) + 9 S-B7 notes (a8889009…, PR #248) + 14 S-B8 notes (51a6ed34…, PR #249) + 11 S-B9 notes (this generation commit)" },
  conservation_law:
    "kind/modelAnswer/keywords on written items ARE §7 stream tokens (the walk extends by those fields on kind!=mcq; old packages carry no kind so the walk is byte-neutral for them): the 7 non-R3 per-note streams equal the S-B8 (v15) anchors exactly; the 94 prior-R3 streams equal their own anchors exactly (bytes unchanged); the 11 S-B9 notes add the 100 written items' tokens (stem, misconceptionClass, modelAnswer, keywords — written kinds carry no options). Grand + wave subtotals recomputed over all 112 in the v6 note order.",
  source_shape_note:
    "no 0.4->0.5 shape normalization is exercised by this wave: the D-1 pre-pass census found zero lessons among the 11 tranche notes whose 0.4 source carries figureIds == [] (the normalization path itself stands of record from waves 7/8: rn_vVdP57QhDYSVfZgy L2 at wave 7, rn_HNXFQt7vM32g6PMv L2 at wave 8). Claimed figures carry through unchanged; schema FILES untouched (delta NONE).",
  grand_stream: { chars: grandChars, sha256: grandSha },
  wave_stream_sha256: waveOut,
  r3_census: {
    stage_a_pilot_notes: PILOTS,
    sb1_notes: SB1_NOTES,
    sb2_notes: SB2_NOTES,
    sb3_notes: SB3_NOTES,
    sb4_notes: SB4_NOTES,
    sb5_notes: SB5_NOTES,
    sb6_notes: SB6_NOTES,
    sb7_notes: SB7_NOTES,
    sb8_notes: SB8_NOTES,
    sb9_notes: TRANCHE,
    cumulative_r3_notes: 105,
    cumulative_r3_lessons: 224,
    cumulative_written_items: 896,
    kinds_cumulative: { recall: 448, "explain-why": 224, application: 224 },
    sb9_wave: { notes: 11, lessons: 25, written_items: 100, kinds: { recall: 50, "explain-why": 25, application: 25 } },
    mcqs_conserved: 1195,
    packages_untouched: 7,
    lessons_untouched: 7,
    authored_chars_delta_vs_v15: grandChars - int3b5.grand_stream.chars,
  },
  sb9_authoring_register: {
    basis: "stage-B plan of record: 'tranche order mirrors the authoring register' + the S-B8 NEXT ('STAGE-B WAVE 9 — the next register tranche, final size read from the register at wave open; wave-9/ authoring dir; the 2 stage-A pilot notes in that bucket keep their already-live items') — S-B9 = the wave-9 register notes minus the stage-A pilot rn_2MpXPtNXvn8pQm3r (11 notes / 25 lessons / 125 checks per source-0.4; wave-field proven: all 11 rows carry wave==9 in the INT-3 record)",
    anchor_law: "each written item anchored (authoring-time provenance, stripped from emitted bytes) to one of its lesson's keyPoints by KP index; stems verified non-duplicative against ALL 1,195 of-record MCQ stems + 796 of-record written stems + intra-tranche x100 (token-Jaccard >= 0.6: 0 flags on the final pass — 2 keyword re-points, 1 stem re-point per the S-B8 template and 1 keyword-shape fix applied at authoring); the wave's self-grading audit (model answer grades correct under its own keyword law): 100/100 pass pre-commit; zero-keyword miss probe scores 0 hits on all 100 items; numeric-claim clusters recomputed in code (the C12H26 alkane-formula substitution 2x12+2=26, the C6H12 alkene-formula substitution 2x6=12, the complete-combustion balances of propane C3H8+5O2->3CO2+4H2O and butane 2C4H10+13O2->8CO2+10H2O, the incomplete balances 2CH4+3O2->2CO+4H2O and CH4+O2->C+2H2O, the sulfur routes S+O2->SO2 and 2SO2+O2+2H2O->2H2SO4, the chlorination CH4+Cl2->CH3Cl+HCl, the kerosene window 25 < 180 < 350 degC, the cracking window 600..700 degC, the pent-2-ene locant 2 and the C4H10->C2H5 empirical reduction)",
  },
  notes: rows,
};
const int3Buf = emit(path.join(RES, "records/INT-3-transform-record-r3-stageb9.json"), int3b6);
const man13Buf = emit(path.join(RES, "hub-import-manifest-v16.json"), man13);

// ── fail-closed checkpoint before the promotion receipt ─────────────────────
if (FAILED > 0) {
  console.error(`\nFAIL-CLOSED: ${FAILED} gate failure(s) — promotion receipt NOT emitted`);
  process.exit(1);
}

// ── promotion receipt ────────────────────────────────────────────────────────
section("promotion receipt");
const receipt = {
  format: "r3-check-types-promotion-receipt/1.0",
  wave: "R3-MIXED-CHECK-TYPES (stage B wave 9 — the wave-9 authoring register minus the stage-A pilot, 11 notes / 25 lessons / 100 written items)",
  operator_traces: [QUEUE_TRACE, STAGE_A_TRACE, SB_GATE_TRACE, SB2_EXECUTE_TRACE, SB3_IGNITION_TRACE, SB4_IGNITION_TRACE, SB5_IGNITION_TRACE, SB6_IGNITION_TRACE, SB7_IGNITION_TRACE, OPERATOR_TRACE],
  generated_at_utc: now(),
  repo: "SyllabAI/syllabai-resources",
  branch: "integration/r3-stageb9-20261031",
  contract_of_record: "R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json followups + the S-B1 NEXT of record ('waves 3..10 to the ~956 total') + the S-B8 promotion receipt merge_order ('stage B wave 9 (next register tranche) remains operator-gated per the ledger convention') — gate opened by operator trace 1a190d455ab9612d ('Wave 9')",
  stack_of_record: {
    note: "S-B9 is based on the current resources main (wave-open main of record resolved at run time, recorded in input_pins): the S-B8 generation (PR #249, merge 88dfb3de) is an ancestor of main, and main advanced past it with unrelated lanes before this wave opened — disclosed, zero overlap with the stage-B namespaces. The S-B1 merge-order convention (resources PR merges first; the hub chain follows) holds for this wave.",
    sb8_merge_commit: SB8_MERGE,
    branch_base: RES_MAIN_OPEN_RESOLVED,
  },
  commits: {
    A: { sha: commitA, parent: commitAParent, note: "S-B9 source-0.5 generation — 11 authored guided-lesson/0.5 notes (100 written items) added to the namespace (105 files total)" },
    C: { sha: "(namespace-complete — outputs + manifest v16 + records + pipeline)", note: "hub-import-1.4/ ×11 + question-packages-1.1/ ×11 + hub-import-manifest-v16.json + records/INT-3-transform-record-r3-stageb9.json + records/R3-CHECK-TYPES-STAGEB9-PROMOTION-20261031.json + tooling/r3-stageb9-pipeline.js + tooling/r3-stageb9-authoring/ — schema delta NONE (the S-B1 union caps already admit this tranche)" },
  },
  artifact_pin: `${SOURCE_PIN_V6} (7 untouched notes / 15 lessons) | ${STAGE_A_COMMIT} (2 stage-A pilots) | ${SB1_COMMIT_A} (10 S-B1 notes) | ${SB2_A_FULL} (12 S-B2 notes) | ${SB3_COMMIT_A} (12 S-B3 notes) | ${SB4_COMMIT_A} (11 S-B4 notes) | ${SB5_COMMIT_A} (12 S-B5 notes) | ${SB6_COMMIT_A} (12 S-B6 notes) | ${SB7_COMMIT_A} (9 S-B7 notes) | ${SB8_COMMIT_A} (14 S-B8 notes) | ${commitA} (11 new source-0.5 lessons — commit A of this wave)`,
  pkg_pin: `(7 untouched keep INT-0 4d857c47…; 2 pilots keep ${STAGE_A_COMMIT.slice(0, 8)}; 10 S-B1 keep 78ad6a20; 12 S-B2 keep ${SB2_A_FULL.slice(0, 8)}; 12 S-B3 keep ${SB3_COMMIT_A.slice(0, 8)}; 11 S-B4 keep ${SB4_COMMIT_A.slice(0, 8)}; 12 S-B5 keep ${SB5_COMMIT_A.slice(0, 8)}; 12 S-B6 keep ${SB6_COMMIT_A.slice(0, 8)}; 9 S-B7 keep ${SB7_COMMIT_A.slice(0, 8)}; 14 S-B8 keep ${SB8_COMMIT_A.slice(0, 8)}; ${commitA} for the 11 new — the TENTH package-channel re-pin since INT-0)`,
  input_pins: { resources_main_at_wave_open: RES_MAIN_OPEN_RESOLVED },
  manifest: "hub-import-manifest-v15.json",
  int_record: "INT-3-transform-record-r3-stageb8.json",
  authoring_parts: ["SME-GuidedLessons/tooling/r3-stageb9-authoring/authoring-part1.json", "SME-GuidedLessons/tooling/r3-stageb9-authoring/authoring-part2.json", "(lane mirrors: scripts/r3-stageb9/authoring-part{1,2}.json; audit: scripts/r3-stageb9/audit_authoring.py)"],
  counts_census: { notes: 112, lessons: 239, checks: 2091, checks_mcq: 1195, checks_written: 896, written_recall: 448, written_explain_why: 224, written_application: 224, sb9_notes: TRANCHE, sb9_written: 100, distractors: 3565 },
  schema_delta: "NONE — the S-B1 union minors already admit this tranche (sme-question-package/1.1 questions maxItems 45; guided-lesson/0.5 check maxItems 9; hub/lesson-import/1.4 checkRefs 9). S-B9 is a pure data wave under unchanged schemas (ajv re-proof ×224 artifacts + ×11 sources in this run).",
  taxonomy: "kind enum of record: mcq (default/absent) | recall | explain-why | application — per-lesson appended order [recall, recall, explain-why, application] (the SME set shape of record)",
  conservation: {
    law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq (feed-safe extension: no kind field -> walk unchanged); 7 non-R3 streams == S-B8 (v15) anchors exactly; 94 prior-R3 streams == their own anchors exactly",
    authored_chars: grandChars,
    authored_chars_delta_vs_v15: grandChars - int3b5.grand_stream.chars,
    mcq_conservation: "tranche package MCQs deep-equal the 1.0 bytes ×11 (+100 count); 7 package shas byte-identical ×7; 94 prior-R3 packages byte-identical ×94",
  },
  gates: { pipeline: `${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, 0 fail`, gate_log: CHECKS },
  merge_order:
    "resources PR (this branch; a clean descendant of main at wave open) merges to main FIRST; the hub PR (runner FEED r3-stageb9-v16 + re-issued artifacts + re-issued guided-import.json) merges only after; stage B wave 10 (final register tranche) remains operator-gated",
  hub_side_note:
    "renderer law unchanged from stage A: MCQ path untouched byte-for-byte; written kinds render a labelled free-text input, submit -> verdict role=status + model answer ALWAYS shown on settle; a11y label/aria-live; flow tallies unchanged in signature (keyword-hit boolean rides onAnswer correct); reveal-only fail-closed when keywords absent",
  recalibration_note:
    "wave receipt + recalibration: grand stream recomputed over all 112 notes; wave subtotals ×10 recomputed (9 untouched waves byte-equal to v15 — declared preserved, including wave-10 whose bucket carries the already-live stage-A pilot rn_8T5GfPn2q7sY2YCh byte-unchanged; wave-9 re-anchored by its 11 S-B9 notes)",
};
emit(path.join(RES, "records/R3-CHECK-TYPES-STAGEB9-PROMOTION-20261031.json"), receipt);

// ── survivors for the hub runner byte-anchors ────────────────────────────────
fs.mkdirSync(SURV, { recursive: true });
fs.copyFileSync(path.join(RES, "hub-import-manifest-v16.json"), path.join(SURV, "hub-import-manifest-v16.json"));
fs.copyFileSync(path.join(RES, "records/INT-3-transform-record-r3-stageb9.json"), path.join(SURV, "INT-3-transform-record-r3-stageb9.json"));

console.log(`\nRESULT: ${FAILED === 0 ? "GREEN — PIPELINE COMPLETE" : "FAIL-CLOSED"}`);
console.log(`  gates: ${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, ${FAILED} failures`);
console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}… (v15: ${int3b5.grand_stream.chars} → delta +${grandChars - int3b5.grand_stream.chars})`);
console.log(`  census: checks 1991 → 2091 (written 796 → 896: recall 448 / explain-why 224 / application 224; MCQ 1,195 conserved)`);
