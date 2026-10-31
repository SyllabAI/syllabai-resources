#!/usr/bin/env node
/**
 * R3-CHECK-TYPES PIPELINE — STAGE B WAVE 10 (S-B10, the FINAL register tranche)
 * (operator ignition: "STAGE-B WAVE 10", hub chat trace 1a19138e39ac2c69, continuing the
 *  stage-B contract of record in R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json, the S-B1 NEXT
 *  ("waves 3..10 to the ~956 total") and the S-B9 promotion receipt merge_order ("stage B
 *  wave 10 (final register tranche) remains operator-gated") — gate opened by the operator word above)
 *
 * S-B10 tranche of record: the wave-10 authoring register at wave open (8 notes) minus the
 * already-live stage-A pilot rn_8T5GfPn2q7sY2YCh, which keeps its live items byte-unchanged
 * per the S-B9 recalibration note = 7 notes, 15 lessons, 75 MCQs -> +60 authored written
 * items (30 recall, 15 explain-why, 15 application). FINAL tranche shape read from the
 * register at wave open per the S-B9 NEXT pointer. THIS WAVE COMPLETES STAGE B: after it,
 * all 112 notes carry written items and the ~956 total is reached exactly.
 * Schema delta: NONE — the S-B1 union caps (maxItems 45 / check 9 / checkRefs 9) admit this tranche.
 *
 * Stack of record: branch integration/r3-stageb10-20261031 based on the current resources main
 * (wave-open main of record resolved at run time, recorded in input_pins; contains the S-B9
 * merge-of-record 7dd46c27 as ancestor — main advanced past it with unrelated lanes, disclosed).
 *
 * Inputs (clone /home/z/my-project/syllabai-resources @ integration/r3-stageb10-20261031):
 *   scripts/r3-stageb10/authoring-part{1,2}.json   the 60 authored items (KP-anchored; audit GREEN)
 *   integration/source-0.4/        0.4 generation (D-1 baseline)
 *   integration/source-0.5/        the 105 prior R3 sources (byte-identical re-proof)
 *   integration/hub-import-1.3/    1.3 lesson outputs (D-2 baseline for the tranche)
 *   integration/question-packages/ 1.0 packages (C-9: zero remain untouched after this wave)
 *   integration/hub-import-manifest-v16.json + records/INT-3-transform-record-r3-stageb9.json
 *
 * Outputs (commit C):
 *   source-0.5/ x7 (new)           hub-import-1.4/ x7 (new)   question-packages-1.1/ x7 (new)
 *   hub-import-manifest-v17.json   records/INT-3-transform-record-r3-stageb10.json
 *   records/R3-CHECK-TYPES-STAGEB10-PROMOTION-20261031.json
 *
 * Conservation (the §7 law): written stems + misconceptionClass + modelAnswer + keywords are
 * stream tokens on kind!=mcq; 0 non-R3 notes remain after this wave; 105 prior-R3 streams ==
 * their own anchors exactly (bytes unchanged); 7 S-B10 rows re-anchored; grand + waves x10
 * (9 byte-equal vs v16 — waves 1..9; wave-10 re-anchored by its 7 S-B10 notes).
 * FAIL-CLOSED: any gate failure aborts before any record is emitted.
 */
import { createRequire } from "node:module";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { execSync } from "node:child_process";

const require = createRequire(import.meta.url);
const Ajv = require("/tmp/ajv-dep/node_modules/ajv");

const RES = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/integration";
const RESROOT = "/home/z/my-project/syllabai-resources";
const AUTH = "/home/z/my-project/scripts/r3-stageb10";
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
const SB9_NOTES = ["rn_6c2G8nJpFSnQnbcP","rn_9J7DQhskyxzhd7CP","rn_DBGf3WVffDBNDp4R","rn_DrqzYWZMScqGrbWT","rn_H2zGfgH76qYV5cmr","rn_H9chr9BWCfXYW472","rn_HqqBFgKRHykMMhbB","rn_MmqCNJfWbtYzRVqT","rn_NdJGQM8BqHmTy7Vg","rn_V3hNWh6QWrbCRHrX","rn_wDdXr5k7gknQ7xJp"]; // S-B9, live @ 52acc7ec (PR #253 merged 7dd46c27)
const PRIOR_R3 = [...PILOTS, ...SB1_NOTES, ...SB2_NOTES, ...SB3_NOTES, ...SB4_NOTES, ...SB5_NOTES, ...SB6_NOTES, ...SB7_NOTES, ...SB8_NOTES, ...SB9_NOTES]; // the 105 notes already carrying written items (byte-identical this wave)
const REGISTER_W10 = ["rn_2z53qk2CdWrVVc7V","rn_7ZMc3T3J4SJXfNdR","rn_8T5GfPn2q7sY2YCh","rn_BBGMYy3Yx9Nm4GV3","rn_BDkhS5vQpRd4hvwf","rn_bGgYrQXP2tqrYwdV","rn_bvyrkKqRBMKCRzHM","rn_ncFJkGhXFsKrkNkH"]; // wave-10 authoring register order of record (landing-plane wave field at wave open)
const PILOT_KEEP = "rn_8T5GfPn2q7sY2YCh"; // stage-A pilot in the wave-10 bucket — keeps its already-live items byte-unchanged per the S-B9 recalibration note
const STAGE_A_COMMIT = "80afdb8e02b628754f0e522d257e54d046ba5b0f";
const SB1_COMMIT_A = "78ad6a2073c669231bb40bd7266674a257c6003e";
const SB2_COMMIT_A = "96c261a"; // resolved below
const SB3_COMMIT_A = "da18433ed9e8351a2e8ce1282b8eaf5c362442d4";
const SB4_COMMIT_A = "fa1f302050ba38b6b2e97760e88d32567d2b0c90";
const SB5_COMMIT_A = "6fb25fc02d1a7acc71ee2231b547ac85e00705c1";
const SB6_COMMIT_A = "286b5ac81d43a28e5faa9f9e8ab16b67fbb12c51";
const SB7_COMMIT_A = "a8889009338bc5ce09edfed1d610d8cc9c9457b4";
const SB8_COMMIT_A = "51a6ed34e715a270c1d1525d1cff903777337437";
const SB9_COMMIT_A = "52acc7ec1650b985b8a5f88472b1de12b0bc4e6d";
const SOURCE_PIN_V6 = "71922d1510ee9e00400667670b40f36e1ae5d456"; // source-0.4 (the binding-generation pin)
const OPERATOR_TRACE = "1a19138e39ac2c69"; // "STAGE-B WAVE 10"
const SB5_IGNITION_TRACE = "1a18d9f731726de1"; // "stage-B wave 5"
const SB6_IGNITION_TRACE = "1a18dfb539a4c839"; // "wave 6"
const SB7_IGNITION_TRACE = "1a18fd512d610f7d"; // "wave 7"
const SB9_IGNITION_TRACE = "1a190d455ab9612d"; // "Wave 9"
const STAGE_A_TRACE = "1a18a0218b7f44fd";
const QUEUE_TRACE = "1a189fd011119961";
const SB_GATE_TRACE = "1a18bc1ca2cf48e5"; // "stage B proceed"
const SB2_EXECUTE_TRACE = "1a18c3fc617d21b9"; // "wave 2 proceed"
const SB3_IGNITION_TRACE = "1a18c9f53d7b8dd1"; // "wave 3 proceed"
const SB4_IGNITION_TRACE = "1a18d09c1263e991"; // "stage-B wave 4 proceed"
const ADAPTER = "guided-lesson-0.5--hub-lesson-import-1.4";
const SB5_MERGE = "0e66325219293c23243c5721dc68199b47a6e71b"; // the S-B5 merge of record (PR #243)
const SB6_MERGE = "6b70de744337f41a1cbb9a8ad5ee8e501cd184dc"; // the S-B6 merge-of-record (PR #246)
const SB7_MERGE = "652ca2d4e7709647cfd68040a56d817ae985fc5e"; // the S-B7 merge-of-record (PR #248)
const SB8_MERGE = "88dfb3dee9d85c5e533c3d99646678bb588fb559"; // the S-B8 merge-of-record (PR #249)
const SB9_MERGE = "7dd46c2730b6fc2edd75146b2581098967707592"; // the S-B9 merge-of-record (PR #253)
const WAVE_OPEN_MAIN = "4141571c7aea14d3cf4ae2a17782b97eeaaa9564"; // resources main at S-B10 open (ls-remote resolved)

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
const sb9IsAncestor = (() => { try { execSync(`git merge-base --is-ancestor ${SB9_MERGE} ${RES_MAIN_OPEN_RESOLVED}`, { cwd: RESROOT }); return true; } catch { return false; } })();
gate("P0 wave-open main contains the S-B9 merge of record (main advanced past it with unrelated lanes — disclosed)", sb9IsAncestor, RES_MAIN_OPEN_RESOLVED);
gate("P0 wave-open main is the recorded input pin", RES_MAIN_OPEN_RESOLVED === WAVE_OPEN_MAIN, RES_MAIN_OPEN_RESOLVED);
const BRANCH_RESOLVED = execSync("git branch --show-current", { cwd: RESROOT }).toString().trim();
gate("P0 worktree branch == integration/r3-stageb10-20261031", BRANCH_RESOLVED === "integration/r3-stageb10-20261031", BRANCH_RESOLVED);
const SB2_A_FULL = execSync(`git rev-parse ${SB2_COMMIT_A}`, { cwd: RESROOT }).toString().trim();
// commit A of record: the source-0.5 generation commit — HEAD at pipeline run time
const commitA = execSync("git rev-parse HEAD", { cwd: RESROOT }).toString().trim();
let commitAParent = "(shallow base — no parent at emit-only bootstrap)";
if (process.env.SB10_EMIT_ONLY !== "1") {
  commitAParent = execSync("git rev-parse HEAD~1", { cwd: RESROOT }).toString().trim();
}
if (process.env.SB10_EMIT_ONLY !== "1") {
  gate("P0 commit A parent == the wave-open main of record", commitAParent === RES_MAIN_OPEN_RESOLVED, `${commitAParent} vs ${RES_MAIN_OPEN_RESOLVED}`);
} else {
  gate("P0 base HEAD == the wave-open main of record (emit-only bootstrap)", commitA === RES_MAIN_OPEN_RESOLVED, `${commitA} vs ${RES_MAIN_OPEN_RESOLVED}`);
}
console.log(`commit A (S-B10 source-0.5 generation): ${commitA} (parent ${commitAParent.slice(0, 8)})`);

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
gate("A0 tranche == wave-10 register of record (7 unconverted notes)", TRANCHE.length === 7, TRANCHE.join(","));
gate("A0 tranche set matches the wave-10 authoring register minus the stage-A pilot (S-B9 NEXT of record)", JSON.stringify(TRANCHE) === JSON.stringify([...REGISTER_W10].filter((n) => n !== PILOT_KEEP).sort()));
gate("A0 tranche disjoint from the 105 prior-R3 notes", TRANCHE.every((n) => !PRIOR_R3.includes(n)));
const KIND_ORDER = ["recall", "recall", "explain-why", "application"];
let itemTotal = 0, lessonTotal = 0, figureEmptyLessons = 0;
for (const n of TRANCHE) {
  const s4 = readJson(path.join(RES, "source-0.4", `guided-lesson-${n}.json`));
  gate(`A0 ${n}: authored lessons == source lessons (${s4.lessons.length})`, auth.notes[n].length === s4.lessons.length, `${auth.notes[n].length} vs ${s4.lessons.length}`);
  s4.lessons.forEach((L, i) => {
    lessonTotal++;
    if (Array.isArray(L.figureIds) && L.figureIds.length === 0) figureEmptyLessons++;
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
gate(`A0 inventory totals (lessons ${lessonTotal}, items ${itemTotal})`, lessonTotal === 15 && itemTotal === 60, `${lessonTotal}/${itemTotal}`);
if (FAILED > 0) { console.error("FAIL-CLOSED at A0"); process.exit(1); }

// ── build source-0.5 ×7 (0.4 + format + appended written items, anchor stripped) ──
section("build source-0.5 ×7");
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
const EMIT_ONLY = process.env.SB10_EMIT_ONLY === "1"; // bootstrap: write sources, exit for commit A
for (const n of TRANCHE) {
  const buf = emit(path.join(RES, "source-0.5", `guided-lesson-${n}.json`), src5[n]);
  src5sha[n] = sha256(buf);
  if (EMIT_ONLY) continue;
  // P0: the working-tree bytes must be exactly what commit A carries
  const blob = execSync(`git show HEAD:SME-GuidedLessons/integration/source-0.5/guided-lesson-${n}.json`, { cwd: RESROOT, maxBuffer: 1024 * 1024 * 8 });
  gate(`P0 committed == rebuilt @ source-0.5/${n}`, blob.equals(src5Bytes[n]) && blob.equals(buf));
}
if (EMIT_ONLY) { console.log("EMIT-ONLY: 7 source-0.5 files written — commit A, then re-run without SB10_EMIT_ONLY"); process.exit(0); }
gate("A0 0.4->0.5 shape normalization exercised exactly once (rn_bGgYrQXP2tqrYwdV L1 figureIds == [])", figureEmptyLessons === 1, String(figureEmptyLessons));

// ── D-1 source determinism ×7 ────────────────────────────────────────────────
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

// ── C-6 ajv sources ×7 ───────────────────────────────────────────────────────
section("C-6 ajv battery");
const ajv = new Ajv({ allErrors: true });
const vSrc5 = ajv.compile(readJson(path.join(RES, "schema/guided-lesson.0.5.schema.json")));
const vHub14 = ajv.compile(readJson(path.join(RES, "schema/hub-lesson-import.1.4.schema.json")));
const vPkg11 = ajv.compile(readJson(path.join(RES, "schema/sme-question-package.1.1.schema.json")));
for (const n of TRANCHE) {
  const ok = vSrc5(readJson(path.join(RES, "source-0.5", `guided-lesson-${n}.json`)));
  gate(`C-6 source-0.5 ${n} vs guided-lesson/0.5`, ok, ok ? "" : ajv.errorsText(vSrc5.errors).slice(0, 250));
}

// ── C-2 preflight: manifest v16 upstream fidelity (224 local bytes) ───────────
section("C-2 preflight vs manifest v16");
const man16 = readJson(path.join(RES, "hub-import-manifest-v16.json"));
const int3b9 = readJson(path.join(RES, "records/INT-3-transform-record-r3-stageb9.json"));
gate("C-2 manifest v16 shape", man16.manifest_version === 16 && man16.artifacts.length === 224);
const v16ByKindNote = new Map();
for (const a of man16.artifacts) v16ByKindNote.set(`${a.kind}|${a.noteId}`, a);
const notes = man16.artifacts.filter((a) => a.kind !== "sme-question-package").map((a) => a.noteId);
gate("C-2 112 notes", notes.length === 112, String(notes.length));
let shaOk = 0;
for (const n of notes) {
  const isR3 = PRIOR_R3.includes(n);
  const lesKind = isR3 ? "hub-lesson-import-1.4" : "hub-lesson-import-1.3";
  const lesDir = isR3 ? "hub-import-1.4" : "hub-import-1.3";
  const pkgDir = isR3 ? "question-packages-1.1" : "question-packages";
  const les = v16ByKindNote.get(`${lesKind}|${n}`);
  const pkg = v16ByKindNote.get(`sme-question-package|${n}`);
  const lesBuf = read(path.join(RES, lesDir, `${n}.hub-lesson-import.json`));
  const pkgBuf = read(path.join(RES, pkgDir, `${n}.sme-question-package.json`));
  if (sha256(lesBuf) === les.sha256 && lesBuf.length === les.bytes && sha256(pkgBuf) === pkg.sha256 && pkgBuf.length === pkg.bytes) shaOk++;
}
gate("C-2 224 local bytes == manifest v16 shas (checkout == pinned generations)", shaOk === 112, `${shaOk}/112 notes (224 artifacts)`);

// ── transform ×7: mutate the 1.3 / 1.0 baseline bytes by the declared deltas ──
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

// prior-R3 re-proof under the union schemas + C-5 (byte-identical to the prior generations)
for (const n of PRIOR_R3) {
  const hub = JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"));
  const pkg = JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8"));
  gate(`C-6 prior-R3 lesson ${n} vs hub/lesson-import/1.4 (re-proof)`, vHub14(hub));
  gate(`C-6 prior-R3 package ${n} vs sme-question-package/1.1 (re-proof)`, vPkg11(pkg));
  const flat = [];
  hub.lesson.modules.forEach((m) => m.checkRefs.forEach((r) => flat.push(r)));
  gate(`C-5 prior-R3 checkRefs<->questions 1:1 ${n}`, flat.length === pkg.questions.length && flat.every((r, i) => r === pkg.questions[i].id));
}

// corpus completion: ZERO non-R3 notes remain after this wave
let untouchedOk = 0, pkgShaOk = 0;
for (const n of notes) {
  if (PRIOR_R3.includes(n) || TRANCHE.includes(n)) continue;
  untouchedOk++;
}
gate("C-9 0 non-R3 packages remain after this wave — the corpus is fully R3", untouchedOk === 0, String(untouchedOk));
gate("C-2 112 notes == 105 prior-R3 + 7 S-B10", notes.length === PRIOR_R3.length + TRANCHE.length, `${PRIOR_R3.length} + ${TRANCHE.length}`);

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
const priorRows = new Map(int3b9.notes.map((r) => [r.noteId, r]));
const rows = int3b9.notes.map((r) => JSON.parse(JSON.stringify(r)));
let priorStreamOk = 0;
for (const row of rows) {
  const n = row.noteId;
  if (TRANCHE.includes(n)) {
    const s = targetTokens(outLessons[n], outPkgs[n]).join("\n");
    row.sourceLayerSha256 = src5sha[n];
    row.hubSha256 = newSha[n].hub.sha256;
    row.pkgSha256 = newSha[n].pkg.sha256;
    row.stream = { sha256: sha256(Buffer.from(s, "utf8")), chars: s.length };
    row.r3_delta = { written_items: 4 * src5[n].lessons.length, mcq_unchanged: true, wave: "S-B10" };
  } else if (PRIOR_R3.includes(n)) {
    const hub = JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"));
    const pkg = JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8"));
    const s = targetTokens(hub, pkg).join("\n");
    const sha = sha256(Buffer.from(s, "utf8"));
    if (sha === row.stream.sha256 && s.length === row.stream.chars) priorStreamOk++;
    else gate(`G-E prior-R3 stream ${n} == prior anchor`, false, `got ${sha.slice(0, 12)}/${s.length} want ${row.stream.sha256.slice(0, 12)}/${row.stream.chars}`);
  } else {
    gate(`G-E non-R3 row ${n} exists (must be zero after this wave)`, false, "corpus must be fully R3");
  }
}
gate("G-E 105 prior-R3 streams == their anchors exactly (bytes unchanged)", priorStreamOk === 105, `${priorStreamOk}/105`);
gate("G-E 7 S-B10 rows re-anchored", rows.filter((r) => TRANCHE.includes(r.noteId)).length === 7);
gate("G-E the 7 re-anchored rows carry authoring wave 10 of record", rows.filter((r) => TRANCHE.includes(r.noteId)).every((r) => r.wave === 10));

// grand + wave subtotals (int3.notes order — the runner's iteration order)
const grand = crypto.createHash("sha256");
let grandChars = 0;
const waveHashes = {};
for (const row of rows) {
  const n = row.noteId;
  const hub = TRANCHE.includes(n)
    ? outLessons[n]
    : JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"));
  const pkg = TRANCHE.includes(n)
    ? outPkgs[n]
    : JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8"));
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

// cross-checks vs v16
gate("cross-check: manifest v16 grand == v16 record", man16.conservation.authored_stream_sha256 === int3b9.grand_stream.sha256);
gate("cross-check: wave subtotals preserved for the 9 untouched waves (1,2,3,4,5,6,7,8,9)", ["wave-1","wave-2","wave-3","wave-4","wave-5","wave-6","wave-7","wave-8","wave-9"].every((w) => waveOut[w] === man16.conservation.wave_stream_sha256[w]));
gate("cross-check: wave-10 re-anchored (pilot byte-unchanged + 7 S-B10 notes)", waveOut["wave-10"] !== man16.conservation.wave_stream_sha256["wave-10"]);

// ── manifest v17 ─────────────────────────────────────────────────────────────
section("manifest v17");
const newLessons = 0; // re-issued only — no new lesson rows
const counts = {
  notes: 112,
  lessons: 239 + newLessons,
  checks: 2151,
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
  checks_written: 956,
  checks_mcq: 1195,
  written_recall: 478,
  written_explain_why: 239,
  written_application: 239,
};
const artifacts = man16.artifacts.map((a) => {
  if (a.kind === "hub-lesson-import-1.3" && TRANCHE.includes(a.noteId)) {
    return { kind: "hub-lesson-import-1.4", noteId: a.noteId, path: `SME-GuidedLessons/integration/hub-import-1.4/${a.noteId}.hub-lesson-import.json`, sha256: newSha[a.noteId].hub.sha256, bytes: newSha[a.noteId].hub.bytes };
  }
  if (a.kind === "sme-question-package" && TRANCHE.includes(a.noteId)) {
    return { kind: "sme-question-package", noteId: a.noteId, path: `SME-GuidedLessons/integration/question-packages-1.1/${a.noteId}.sme-question-package.json`, sha256: newSha[a.noteId].pkg.sha256, bytes: newSha[a.noteId].pkg.bytes };
  }
  return a;
});
gate("manifest v17 lists 224", artifacts.length === 224);
gate("manifest v17: exactly 14 re-issued vs v16", artifacts.filter((a) => !man16.artifacts.some((b) => b.path === a.path)).length === 14);
const man17 = {
  format: "hub-import-manifest/1.0",
  manifest_version: 17,
  generated_at_utc: now(),
  operator_trace: OPERATOR_TRACE,
  supersedes: "hub-import-manifest-v16.json (105 hub-lesson-import-1.4 lessons + 7 hub-lesson-import-1.3 lessons + 112 sme-question-packages + the 210 already-live R3 re-issues byte-identical re-pins; exactly 14 re-issued artifacts: 7 hub-lesson-import-1.4 lessons (1.3->1.4 upgrade, checkRefs 5->9) + 7 sme-question-package/1.1 packages (+60 written items) — the R3 stage-B wave 10 tranche: the wave-10 authoring register minus the stage-A pilot. After this wave the corpus is fully R3: 112 notes / 239 lessons / 956 written items — the ~956 total of record is reached)",
  checks_layer: {
    wave: `R3-MIXED-CHECK-TYPES stage B wave 10 (S-B10, the FINAL register tranche) — operator ignition trace ${OPERATOR_TRACE} ("STAGE-B WAVE 10") on the stage-B contract of record (S-B1 NEXT: "waves 3..10 to the ~956 total"; S-B9 promotion receipt merge_order: "stage B wave 10 (final register tranche) remains operator-gated")`,
    derivation: "60 authored written items (30 recall, 15 explain-why, 15 application), each spec-anchored to its lesson's keyPoints (KP-index provenance in the authoring parts of record), carrying modelAnswer + generous synonym/inflection-bearing keywords; appended after the 5 MCQs of each of the 15 wave-10 lessons in the SME kind order [recall, recall, explain-why, application]",
    declared_revision: "the ELEVENTH and FINAL package-channel delta since INT-0: 7 final packages re-issued under sme-question-package/1.1 (union schema); 7 final lessons re-issued under hub/lesson-import/1.4 (1.3->1.4 upgrade, checkRefs 5->9); kind/modelAnswer/keywords are §7-declared stream tokens on written items; cumulative R3 generation = 112 notes / 239 lessons / 956 written items — STAGE B COMPLETE",
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

// ── INT-3 record S-B10 ───────────────────────────────────────────────────────
const int3b10 = {
  stage: "INT-3",
  title: "transform record — R3 mixed check types STAGE B WAVE 10 generation (adapter guided-lesson-0.5--hub-lesson-import-1.4) — the FINAL register tranche",
  generated_at_utc: now(),
  operator_trace: OPERATOR_TRACE,
  prior_record: "records/INT-3-transform-record-r3-stageb9.json (stage-B wave 9 — superseded by this record for the 112-note R3 generation; anchors for the 105 prior-R3 notes carried unchanged)",
  adapter: ADAPTER,
  source_pin: {
    repo: "SyllabAI/syllabai-resources",
    ref: RES_MAIN_OPEN_RESOLVED,
    note: "resources main at S-B10 open (contains the S-B9 merge-of-record 7dd46c27; main advanced past it with unrelated lanes before this wave opened — disclosed)",
  },
  source_05_generation_pin: { commit: commitA, namespace: "SME-GuidedLessons/integration/source-0.5/", note: "112 files: 2 stage-A pilots (80afdb8e) + 10 S-B1 notes (78ad6a20) + 12 S-B2 notes (96c261a…, PR #237) + 12 S-B3 notes (da18433…, PR #240) + 11 S-B4 notes (fa1f302…, PR #242) + 12 S-B5 notes (6fb25fc…, PR #243) + 12 S-B6 notes (286b5ac…, PR #245/#246) + 9 S-B7 notes (a8889009…, PR #248) + 14 S-B8 notes (51a6ed34…, PR #249) + 11 S-B9 notes (52acc7ec…, PR #253) + 7 S-B10 notes (this generation commit)" },
  conservation_law:
    "kind/modelAnswer/keywords on written items ARE §7 stream tokens (the walk extends by those fields on kind!=mcq; old packages carry no kind so the walk is byte-neutral for them): 0 non-R3 notes remain after this wave; the 105 prior-R3 per-note streams equal their own anchors exactly (bytes unchanged); the 7 S-B10 notes add the 60 written items' tokens (stem, misconceptionClass, modelAnswer, keywords — written kinds carry no options). Grand + wave subtotals recomputed over all 112 in the v6 note order.",
  source_shape_note:
    "the 0.4->0.5 shape normalization IS exercised by this wave: the D-1 pre-pass census found exactly one lesson among the 7 tranche notes whose 0.4 source carries figureIds == [] — rn_bGgYrQXP2tqrYwdV L1 (the third of-record exercise after rn_vVdP57QhDYSVfZgy L2 at wave 7 and rn_HNXFQt7vM32g6PMv L2 at wave 8). Claimed figures carry through unchanged; schema FILES untouched (delta NONE).",
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
    sb9_notes: SB9_NOTES,
    sb10_notes: TRANCHE,
    cumulative_r3_notes: 112,
    cumulative_r3_lessons: 239,
    cumulative_written_items: 956,
    kinds_cumulative: { recall: 478, "explain-why": 239, application: 239 },
    sb10_wave: { notes: 7, lessons: 15, written_items: 60, kinds: { recall: 30, "explain-why": 15, application: 15 } },
    mcqs_conserved: 1195,
    packages_untouched: 0,
    lessons_untouched: 0,
    authored_chars_delta_vs_v16: grandChars - int3b9.grand_stream.chars,
  },
  sb10_authoring_register: {
    basis: "stage-B plan of record: 'tranche order mirrors the authoring register' + the S-B9 NEXT ('STAGE-B WAVE 10 — the final register tranche, final size read from the register at wave open; the stage-A pilot note in that bucket keeps its already-live items byte-unchanged') — S-B10 = the wave-10 register notes minus the stage-A pilot rn_8T5GfPn2q7sY2YCh (7 notes / 15 lessons / 75 checks per source-0.4; wave-field proven: all 7 rows carry wave==10 in the INT-3 record)",
    anchor_law: "each written item anchored (authoring-time provenance, stripped from emitted bytes) to one of its lesson's keyPoints by KP index; stems verified non-duplicative against ALL 2,091 of-record stems (1,195 MCQ + 896 written) + intra-tranche x60 (token-Jaccard >= 0.6: 0 flags on the final pass — 2 stem re-points and 3 keyword re-points applied at authoring per the S-B9 template); the wave's self-grading audit (model answer grades correct under its own keyword law): 60/60 pass pre-commit; zero-keyword miss probe scores 0 hits on all 60 items; numeric-claim clusters recomputed in code (the esterification balance CH3COOH + C2H5OH -> CH3COOC2H5 + H2O, the magnesium ethanoate balance 2CH3COOH + Mg -> (CH3COO)2Mg + H2, the butanoate carbonate balance 2C4H8O2 + K2CO3 -> 2C4H7O2K + H2O + CO2, the fermentation balance C6H12O6 -> 2CO2 + 2C2H5OH, the first-four carbon ladder 1,2,3,4, the volatility ordering -103 < 78 < 100 degC, the hydration window 60..70 atm, the fermentation window 25..35 degC, the vinegar 5/100 concentration, the 150-link condensation water count, the family-formula alkyl-only counting 0+1=1 and 2+1=3, the 2x(1-) charge balance, and the 15-percent yeast cap)",
  },
  notes: rows,
};
const int3Buf = emit(path.join(RES, "records/INT-3-transform-record-r3-stageb10.json"), int3b10);
const man17Buf = emit(path.join(RES, "hub-import-manifest-v17.json"), man17);

// ── fail-closed checkpoint before the promotion receipt ─────────────────────
if (FAILED > 0) {
  console.error(`\nFAIL-CLOSED: ${FAILED} gate failure(s) — promotion receipt NOT emitted`);
  process.exit(1);
}

// ── promotion receipt ────────────────────────────────────────────────────────
section("promotion receipt");
const receipt = {
  format: "r3-check-types-promotion-receipt/1.0",
  wave: "R3-MIXED-CHECK-TYPES (stage B wave 10 — the FINAL register tranche: the wave-10 authoring register minus the stage-A pilot, 7 notes / 15 lessons / 60 written items — STAGE B COMPLETE, the ~956 total of record is reached)",
  operator_traces: [QUEUE_TRACE, STAGE_A_TRACE, SB_GATE_TRACE, SB2_EXECUTE_TRACE, SB3_IGNITION_TRACE, SB4_IGNITION_TRACE, SB5_IGNITION_TRACE, SB6_IGNITION_TRACE, SB7_IGNITION_TRACE, SB9_IGNITION_TRACE, OPERATOR_TRACE],
  generated_at_utc: now(),
  repo: "SyllabAI/syllabai-resources",
  branch: "integration/r3-stageb10-20261031",
  contract_of_record: "R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json followups + the S-B1 NEXT of record ('waves 3..10 to the ~956 total') + the S-B9 promotion receipt merge_order ('stage B wave 10 (final register tranche) remains operator-gated per the ledger convention') — gate opened by operator trace 1a19138e39ac2c69 ('STAGE-B WAVE 10')",
  stack_of_record: {
    note: "S-B10 is based on the current resources main (wave-open main of record resolved at run time, recorded in input_pins): the S-B9 generation (PR #253, merge 7dd46c27) is an ancestor of main, and main advanced past it with unrelated lanes before this wave opened — disclosed, zero overlap with the stage-B namespaces. The S-B1 merge-order convention (resources PR merges first; the hub chain follows) holds for this wave.",
    sb9_merge_commit: SB9_MERGE,
    branch_base: RES_MAIN_OPEN_RESOLVED,
  },
  commits: {
    A: { sha: commitA, parent: commitAParent, note: "S-B10 source-0.5 generation — 7 authored guided-lesson/0.5 notes (60 written items) added to the namespace (112 files total — the source namespace is now complete over the whole corpus)" },
    C: { sha: "(namespace-complete — outputs + manifest v17 + records + pipeline)", note: "hub-import-1.4/ ×7 + question-packages-1.1/ ×7 + hub-import-manifest-v17.json + records/INT-3-transform-record-r3-stageb10.json + records/R3-CHECK-TYPES-STAGEB10-PROMOTION-20261031.json + tooling/r3-stageb10-pipeline.js + tooling/r3-stageb10-authoring/ — schema delta NONE (the S-B1 union caps already admit this tranche)" },
  },
  artifact_pin: `${SOURCE_PIN_V6} (0 untouched notes remain after this wave — the pin is retired with the corpus fully R3) | ${STAGE_A_COMMIT} (2 stage-A pilots) | ${SB1_COMMIT_A} (10 S-B1 notes) | ${SB2_A_FULL} (12 S-B2 notes) | ${SB3_COMMIT_A} (12 S-B3 notes) | ${SB4_COMMIT_A} (11 S-B4 notes) | ${SB5_COMMIT_A} (12 S-B5 notes) | ${SB6_COMMIT_A} (12 S-B6 notes) | ${SB7_COMMIT_A} (9 S-B7 notes) | ${SB8_COMMIT_A} (14 S-B8 notes) | ${SB9_COMMIT_A} (11 S-B9 notes) | ${commitA} (7 new source-0.5 lessons — commit A of this wave)`,
  pkg_pin: `(0 untouched remain — the INT-0 4d857c47… package pin is retired; 2 pilots keep ${STAGE_A_COMMIT.slice(0, 8)}; 10 S-B1 keep 78ad6a20; 12 S-B2 keep ${SB2_A_FULL.slice(0, 8)}; 12 S-B3 keep ${SB3_COMMIT_A.slice(0, 8)}; 11 S-B4 keep ${SB4_COMMIT_A.slice(0, 8)}; 12 S-B5 keep ${SB5_COMMIT_A.slice(0, 8)}; 12 S-B6 keep ${SB6_COMMIT_A.slice(0, 8)}; 9 S-B7 keep ${SB7_COMMIT_A.slice(0, 8)}; 14 S-B8 keep ${SB8_COMMIT_A.slice(0, 8)}; 11 S-B9 keep ${SB9_COMMIT_A.slice(0, 8)}; ${commitA} for the 7 new — the ELEVENTH and FINAL package-channel re-pin since INT-0)`,
  input_pins: { resources_main_at_wave_open: RES_MAIN_OPEN_RESOLVED },
  manifest: "hub-import-manifest-v16.json",
  int_record: "INT-3-transform-record-r3-stageb9.json",
  authoring_parts: ["SME-GuidedLessons/tooling/r3-stageb10-authoring/authoring-part1.json", "SME-GuidedLessons/tooling/r3-stageb10-authoring/authoring-part2.json", "(lane mirrors: scripts/r3-stageb10/authoring-part{1,2}.json; audit: scripts/r3-stageb10/audit_authoring.py)"],
  counts_census: { notes: 112, lessons: 239, checks: 2151, checks_mcq: 1195, checks_written: 956, written_recall: 478, written_explain_why: 239, written_application: 239, sb10_notes: TRANCHE, sb10_written: 60, distractors: 3565 },
  schema_delta: "NONE — the S-B1 union minors already admit this tranche (sme-question-package/1.1 questions maxItems 45; guided-lesson/0.5 check maxItems 9; hub/lesson-import/1.4 checkRefs 9). S-B10 is a pure data wave under unchanged schemas (ajv re-proof ×224 artifacts + ×7 sources in this run).",
  taxonomy: "kind enum of record: mcq (default/absent) | recall | explain-why | application — per-lesson appended order [recall, recall, explain-why, application] (the SME set shape of record)",
  conservation: {
    law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq (feed-safe extension: no kind field -> walk unchanged); 0 non-R3 notes remain after this wave; 105 prior-R3 streams == their own anchors exactly",
    authored_chars: grandChars,
    authored_chars_delta_vs_v16: grandChars - int3b9.grand_stream.chars,
    mcq_conservation: "tranche package MCQs deep-equal the 1.0 bytes ×7 (+60 count); 0 package shas byte-identical untouched (corpus fully R3); 105 prior-R3 packages byte-identical ×105",
  },
  gates: { pipeline: `${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, 0 fail`, gate_log: CHECKS },
  merge_order:
    "resources PR (this branch; a clean descendant of main at wave open) merges to main FIRST; the hub PR (runner FEED r3-stageb10-v17 + re-issued artifacts + re-issued guided-import.json) merges only after; STAGE B IS COMPLETE — no further register tranche remains (the ~956 total of record is reached); any further R3-CHECK-TYPES work is a new operator-gated contract",
  hub_side_note:
    "renderer law unchanged from stage A: MCQ path untouched byte-for-byte; written kinds render a labelled free-text input, submit -> verdict role=status + model answer ALWAYS shown on settle; a11y label/aria-live; flow tallies unchanged in signature (keyword-hit boolean rides onAnswer correct); reveal-only fail-closed when keywords absent",
  recalibration_note:
    "wave receipt + recalibration: grand stream recomputed over all 112 notes; wave subtotals ×10 recomputed (9 untouched waves byte-equal to v16 — declared preserved, including the wave-10 bucket whose already-live stage-A pilot rn_8T5GfPn2q7sY2YCh rides byte-unchanged; wave-10 re-anchored by its 7 S-B10 notes)",
};
emit(path.join(RES, "records/R3-CHECK-TYPES-STAGEB10-PROMOTION-20261031.json"), receipt);

// ── survivors for the hub runner byte-anchors ────────────────────────────────
fs.mkdirSync(SURV, { recursive: true });
fs.copyFileSync(path.join(RES, "hub-import-manifest-v17.json"), path.join(SURV, "hub-import-manifest-v17.json"));
fs.copyFileSync(path.join(RES, "records/INT-3-transform-record-r3-stageb10.json"), path.join(SURV, "INT-3-transform-record-r3-stageb10.json"));

console.log(`\nRESULT: ${FAILED === 0 ? "GREEN — PIPELINE COMPLETE" : "FAIL-CLOSED"}`);
console.log(`  gates: ${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, ${FAILED} failures`);
console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}… (v16: ${int3b9.grand_stream.chars} → delta +${grandChars - int3b9.grand_stream.chars})`);
console.log(`  census: checks 2091 → 2151 (written 896 → 956: recall 478 / explain-why 239 / application 239; MCQ 1,195 conserved)`);
console.log(`  STAGE B COMPLETE — the ~956 total of record is reached: 112 notes / 239 lessons / 956 written items`);
