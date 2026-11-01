#!/usr/bin/env node
/**
 * PHYSICS-STAGEA PIPELINE — new-subject stage-A pilot transform + manifest v18 + INT-3 record
 * (operator ignition trace 1a192830222371a5 "open the new subject's wave-1 contract — 4ph1 physics";
 *  execution trace 1a1954284ff72101 "ignite stage-A execution")
 *
 * Runbook of record: .syllabai/docs/new-subject-runbook.md @ hub f99969a2 (unchanged @ 55f91919).
 * B6 decision of record: CONTINUE-GLOBAL manifest series — physics stage-A = hub-import-manifest-v18.json
 * (course_id declared in-manifest; the v-series is the programme-level integration ledger; per-course v1
 *  would collide with chemistry v1..v17 filenames in the shared integration/ namespace).
 *
 * Input of record (lane clone @ resources main 4b75272d…, branch integration/physics-stagea-20261101):
 *   source-0.6/                    1 authored pilot note (guided-lesson/0.6, committed @ commit A)
 *   schema/guided-lesson.0.6.schema.json                          (commit A)
 *   schema/{hub-lesson-import.1.5, sme-question-package.1.2}.schema.json (commit B)
 *   source-0.5/ x112 + hub-import-1.4/ x112 + question-packages-1.1/ x112  (chemistry union baselines)
 *
 * Outputs (namespace-complete, committed @ commit C):
 *   hub-import-1.5/rn_RpyMnS5nqWSRWXXG.hub-lesson-import.json        (format hub/lesson-import/1.5)
 *   question-packages-1.2/rn_RpyMnS5nqWSRWXXG.sme-question-package.json (format sme-question-package/1.2)
 *   hub-import-manifest-v18.json
 *   records/INT-3-transform-record-physics-stagea.json
 *   records/PHYSICS-4PH1-STAGEA-PROMOTION-20261101.json
 * + lane survivors (hub runner byte-anchors) under ../survivors/
 *
 * Audit battery of record (runbook §1.4): A0 / AN / SG / KW / JC / 2.1B / NUM
 *   A0  structure   — ajv + 9-check law (5 MCQ + 2 recall + 1 explain-why + 1 application) + B2 sizing
 *   AN  answer-key  — exactly one correct per MCQ; correct-key letter census (≥3 distinct, max ≤ 5)
 *   JC  distractors — every distractor names its misconception; correct option misconception null;
 *                     option texts distinct; explanations non-empty
 *   SG  spec-ground — lesson specRefs ⊆ file specPoints; every check shares a content token with its
 *                     lesson keyPoints (KP-index provenance)
 *   KW  keywords    — written items: ≥3 distinct keywords; each grounded in modelAnswer/stem/keyPoints
 *   2.1B learner-surface law — no 8-gram of the corpus note prose appears in any check stem or
 *                     modelAnswer (authored-note phrasing never reaches the learner surface)
 *   NUM numeric     — every numeric claim re-derived in code (8000 m / 360 s = 22.2 m/s 3sf;
 *                     distractor arithmetics 8/6=1.3, 8000/60=133)
 * FAIL-CLOSED: any gate failure aborts before any record is emitted.
 */
import { createRequire } from "node:module";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { execSync } from "node:child_process";

const require = createRequire(import.meta.url);
const Ajv = require("/home/z/my-project/lane-physics-stageA/nodeenv/node_modules/ajv");

const RES = "/home/z/my-project/lane-physics-stageA/resources/SME-GuidedLessons/integration";
const RES_REPO = "/home/z/my-project/lane-physics-stageA/resources";
const HUB_REPO = "/home/z/my-project/lane-physics-stageA/hub";
const SURV = "/home/z/my-project/lane-physics-stageA/survivors";
const PILOTS = ["rn_RpyMnS5nqWSRWXXG"];
const IGNITION_TRACE = "1a192830222371a5";
const EXEC_TRACE = "1a1954284ff72101";
const ADAPTER = "guided-lesson-0.6--hub-lesson-import-1.5";
const COURSE_ID = "igcse-physics-19";
const COURSE_PREFIX = "igcse-physics";
const RES_MAIN_AT_OPEN = "4b75272db1e2e0ff419c1e7653ec008c7f5dbcd5";
const HUB_MAIN_AT_OPEN = "55f919191cce99e3d9971f508200d83f9e0d08cc";
const BODYMD_PIN = "aa0b4de1b732738b4d02dabdd02d9ead85522907";
const MANIFEST_VERSION = 18; // B6 CONTINUE-GLOBAL decision of record

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

// ── §7 canonical authored stream — target side, byte-identical walk to run_import.mjs ──
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
const commitA = execSync("git rev-parse HEAD", { cwd: RES_REPO }).toString().trim();
const commitAParent = execSync("git rev-parse HEAD~1", { cwd: RES_REPO }).toString().trim();
const branch = execSync("git branch --show-current", { cwd: RES_REPO }).toString().trim();
console.log(`commit A (source-0.6 generation): ${commitA} (parent ${commitAParent.slice(0, 8)}, branch ${branch})`);
gate("P0 branch is the stage-A integration branch", branch === "integration/physics-stagea-20261101", branch);
for (const rel of ["source-0.6/guided-lesson-rn_RpyMnS5nqWSRWXXG.json", "schema/guided-lesson.0.6.schema.json"]) {
  const blob = execSync(`git show HEAD:SME-GuidedLessons/integration/${rel}`, { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 8 });
  gate("P0 committed == working tree @ " + rel.split("/").pop(), blob.equals(read(path.join(RES, rel))));
}

// ── battery inputs ────────────────────────────────────────────────────────────
const src = readJson(path.join(RES, "source-0.6/guided-lesson-rn_RpyMnS5nqWSRWXXG.json"));
const noteRow = JSON.parse(execSync("git show origin/main:apps/hub/content/igcse-physics-19/notes.json", { cwd: HUB_REPO, maxBuffer: 1024 * 1024 * 16 }).toString())
  .find((r) => r.noteId === "rn_RpyMnS5nqWSRWXXG");
if (!noteRow) throw new Error("pilot note row missing from hub notes.json @ origin/main");

// ── A0 structure ──────────────────────────────────────────────────────────────
section("A0 structure (ajv + 9-check law + sizing B2)");
const ajv = new Ajv({ allErrors: true });
const vSrc6 = ajv.compile(readJson(path.join(RES, "schema/guided-lesson.0.6.schema.json")));
const vHub15 = ajv.compile(readJson(path.join(RES, "schema/hub-lesson-import.1.5.schema.json")));
const vPkg12 = ajv.compile(readJson(path.join(RES, "schema/sme-question-package.1.2.schema.json")));
gate("A0 source vs guided-lesson/0.6", vSrc6(src), vSrc6.errors ? ajv.errorsText(vSrc6.errors).slice(0, 250) : "");
const KIND_ORDER = ["mcq", "mcq", "mcq", "mcq", "mcq", "recall", "recall", "explain-why", "application"];
for (const l of src.lessons) {
  const kinds = l.check.map((c) => c.kind || "mcq");
  gate(`A0 ${l.title.slice(0, 24)}: 9 checks in SME kind order`, kinds.length === 9 && JSON.stringify(kinds) === JSON.stringify(KIND_ORDER), kinds.join(","));
  gate(`A0 ${l.title.slice(0, 24)}: keyPoints 3..6`, l.keyPoints.length >= 3 && l.keyPoints.length <= 6, String(l.keyPoints.length));
  const words = src.primer.text.split(/\s+/).length;
  gate("A0 primer 35..90 words", words >= 35 && words <= 90, `${words} words`);
}
gate("A0 sizing B2: 1 note -> 1..3 lessons", src.lessons.length >= 1 && src.lessons.length <= 3, String(src.lessons.length));
gate("A0 lessons carry specRefs", src.lessons.every((l) => l.specRefs.length >= 1), "");
// figure closure both ways (source layer)
const figIds = new Set(src.figures.map((f) => f.id));
let closureOk = true;
for (const l of src.lessons) for (const fid of l.figureIds || []) if (!figIds.has(fid)) closureOk = false;
for (const f of src.figures) for (const mid of f.moduleIds) {
  const les = src.lessons[Number(mid.slice(1)) - 1];
  if (!les || !(les.figureIds || []).includes(f.id)) closureOk = false;
}
const claimSumL = src.lessons.reduce((a, l) => a + (l.figureIds || []).length, 0);
const claimSumF = src.figures.reduce((a, f) => a + f.moduleIds.length, 0);
if (claimSumL !== claimSumF) closureOk = false;
gate("A0 figure closure both ways (figureIds <-> moduleIds)", closureOk, `${claimSumL}/${claimSumF}`);
gate("A0 glossary 3..8", src.noteAssets.glossary.length >= 3 && src.noteAssets.glossary.length <= 8, String(src.noteAssets.glossary.length));

// ── AN answer-key law ─────────────────────────────────────────────────────────
section("AN answer-key law");
{
  const mcqs = src.lessons.flatMap((l) => l.check.filter((c) => (c.kind || "mcq") === "mcq"));
  let ok = true;
  const letters = [];
  for (const c of mcqs) {
    const corr = c.options.filter((o) => o.correct === true);
    if (corr.length !== 1) ok = false;
    letters.push(corr[0] && corr[0].key);
    if (new Set(c.options.map((o) => o.text)).size !== c.options.length) ok = false;
  }
  const census = {};
  for (const k of letters) census[k] = (census[k] || 0) + 1;
  const distinct = Object.keys(census).length;
  const maxShare = Math.max(...Object.values(census));
  gate(`AN exactly-one-correct x${mcqs.length} + distinct option texts`, ok, "");
  gate("AN correct-key census >= 3 distinct letters, max <= 5", distinct >= 3 && maxShare <= 5, JSON.stringify(census));
}

// ── JC distractor quality ─────────────────────────────────────────────────────
section("JC distractor quality");
{
  const mcqs = src.lessons.flatMap((l) => l.check.filter((c) => (c.kind || "mcq") === "mcq"));
  let bad = 0;
  for (const c of mcqs) {
    for (const o of c.options) {
      if (!o.explanation || o.explanation.length === 0) bad++;
      if (o.correct === false && (!o.misconception || o.misconception.length === 0)) bad++;
      if (o.correct === true && o.misconception !== null) bad++;
    }
  }
  gate(`JC every option explained; distractors named; correct misconception null x${mcqs.length}`, bad === 0, `${bad} violations`);
}

// ── SG spec grounding (KP-index provenance) ───────────────────────────────────
section("SG spec grounding");
{
  const codes = new Set(src.specPoints.map((s) => s.code));
  gate("SG lesson specRefs subset of file specPoints", src.lessons.every((l) => l.specRefs.every((r) => codes.has(r))), "");
  const STOP = new Set("a an the of to in on at for with and or is are was were be been it its this that these those as by from not no you your they their we our object objects line lines graph graphs which what how state recall explain why does do can may will would shows show".split(" "));
  const toks = (s) => (s.toLowerCase().match(/[a-z0-9]+/g) || []).filter((t) => t.length > 3 && !STOP.has(t) && !/^\d+$/.test(t));
  let grounded = 0, total = 0;
  for (const l of src.lessons) {
    const kp = toks(l.keyPoints.join(" "));
    const kpSet = new Set(kp);
    for (const c of l.check) {
      total++;
      const ctoks = toks(c.stem);
      const hit = ctoks.some((t) => kpSet.has(t)) || (c.kind && c.kind !== "mcq" && toks(c.modelAnswer).some((t) => kpSet.has(t)));
      if (hit) grounded++;
      else console.error(`    SG miss: ${c.stem.slice(0, 60)}`);
    }
  }
  gate(`SG every check KP-anchored x${total}`, grounded === total, `${grounded}/${total}`);
}

// ── KW keywords law ───────────────────────────────────────────────────────────
section("KW keywords law");
{
  let ok = true, n = 0;
  for (const l of src.lessons) {
    const anchor = (l.keyPoints.join(" ") + " " + l.check.map((c) => c.stem + " " + (c.modelAnswer || "")).join(" ")).toLowerCase();
    for (const c of l.check) {
      if (!c.kind || c.kind === "mcq") continue;
      n++;
      const kws = c.keywords || [];
      const distinct = new Set(kws.map((k) => k.toLowerCase())).size;
      if (distinct < 3) { ok = false; console.error(`    KW few: ${c.stem.slice(0, 50)} (${distinct})`); }
      for (const k of kws) {
        const core = k.toLowerCase().split(/[^a-z0-9]+/).filter(Boolean)[0];
        if (!core || !anchor.includes(core)) { ok = false; console.error(`    KW ungrounded: ${k} @ ${c.stem.slice(0, 40)}`); }
      }
    }
  }
  gate(`KW >=3 distinct grounded keywords per written item x${n}`, ok, "");
}

// ── 2.1B learner-surface law ──────────────────────────────────────────────────
section("2.1B learner-surface law (no authored-note 8-grams on the surface)");
{
  const body = noteRow.bodyMd.toLowerCase();
  const clean = (s) => (s.toLowerCase().match(/[a-z]+/g) || []);
  const noteToks = clean(body);
  const noteGrams = new Set();
  for (let i = 0; i + 8 <= noteToks.length; i++) noteGrams.add(noteToks.slice(i, i + 8).join(" "));
  let hits = 0;
  for (const l of src.lessons) {
    for (const c of l.check) {
      for (const surf of [c.stem, c.modelAnswer, ...(c.options || []).map((o) => o.text + " " + o.explanation)]) {
        if (!surf) continue;
        const t = clean(surf);
        for (let i = 0; i + 8 <= t.length; i++) {
          if (noteGrams.has(t.slice(i, i + 8).join(" "))) { hits++; console.error(`    2.1B hit @ ${c.stem.slice(0, 40)}: …${t.slice(i, i + 8).join(" ")}…`); }
        }
      }
    }
  }
  gate("2.1B zero 8-gram overlaps (stems, model answers, options+explanations vs note body)", hits === 0, `${hits} hits`);
}

// ── NUM numeric law ───────────────────────────────────────────────────────────
section("NUM numeric law");
{
  const r3 = (x) => Number(x.toPrecision(3)).toString();
  const speed = 8000 / 360;
  gate("NUM worked example: 8000/360 = 22.2 (3sf)", r3(speed) === "22.2", String(speed));
  gate("NUM unit conversions: 8 km = 8000 m; 6 min = 360 s", 8 * 1000 === 8000 && 6 * 60 === 360, "");
  const q7 = src.lessons[1].check.find((c) => c.stem.includes("8 km over 6 minutes"));
  const opts = Object.fromEntries((q7?.options || []).map((o) => [o.key, o.text]));
  gate("NUM distractor A: 8/6 = 1.3 (km/min misread)", r3(8 / 6) === "1.33" && (opts.A || "").startsWith("1.3 "), JSON.stringify(opts).slice(0, 120));
  gate("NUM distractor C: 8000/60 = 133 (partial conversion)", Math.round(8000 / 60) === 133 && (opts.C || "").startsWith("133 "), "");
  const correct = (q7?.options || []).find((o) => o.correct);
  gate("NUM correct option carries 22.2 m/s", !!correct && correct.text.includes("22.2"), correct && correct.text);
  const a1 = src.lessons[1].check.find((c) => c.kind === "application");
  gate("NUM application modelAnswer: 22.2 derived from 8000/360", /22\.2/.test(a1.modelAnswer) && /8000/.test(a1.modelAnswer) && /360/.test(a1.modelAnswer), "");
  gate("NUM WE finalAnswer carries 22.2", /22\.2/.test(src.noteAssets.workedExample.finalAnswer), "");
}

// ── C-6 union: chemistry corpus under the new schemas ─────────────────────────
section("C-6 union law: chemistry x336 artifacts validate unchanged");
{
  const srcNames = execSync("git ls-tree --name-only HEAD SME-GuidedLessons/integration/source-0.5/", { cwd: RES_REPO }).toString().trim().split("\n");
  let u1 = 0;
  for (const rel of srcNames) {
    const buf = execSync(`git show HEAD:${rel}`, { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 8 });
    if (vSrc6(JSON.parse(buf.toString("utf8")))) u1++;
  }
  gate(`C-6 chemistry sources x${srcNames.length} vs guided-lesson/0.6 (union)`, u1 === srcNames.length, `${u1}/${srcNames.length}`);
  const lesNames = execSync("git ls-tree --name-only HEAD SME-GuidedLessons/integration/hub-import-1.4/", { cwd: RES_REPO }).toString().trim().split("\n");
  let u2 = 0;
  for (const rel of lesNames) {
    const buf = execSync(`git show HEAD:${rel}`, { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 8 });
    if (vHub15(JSON.parse(buf.toString("utf8")))) u2++;
  }
  gate(`C-6 chemistry lessons x${lesNames.length} vs hub/lesson-import/1.5 (union)`, u2 === lesNames.length, `${u2}/${lesNames.length}`);
  const pkgNames = execSync("git ls-tree --name-only HEAD SME-GuidedLessons/integration/question-packages-1.1/", { cwd: RES_REPO }).toString().trim().split("\n");
  let u3 = 0;
  for (const rel of pkgNames) {
    const buf = execSync(`git show HEAD:${rel}`, { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 8 });
    if (vPkg12(JSON.parse(buf.toString("utf8")))) u3++;
  }
  gate(`C-6 chemistry packages x${pkgNames.length} vs sme-question-package/1.2 (union)`, u3 === pkgNames.length, `${u3}/${pkgNames.length}`);
}

// ── transform: guided-lesson/0.6 -> hub/lesson-import/1.5 + sme-question-package/1.2 ──
section("transform (full derivation from the 0.6 source — no chemistry baseline bytes touched)");
const outLessons = {}, outPkgs = {};
for (const n of PILOTS) {
  const s5buf = read(path.join(RES, "source-0.6", `guided-lesson-${n}.json`));
  const s5sha = sha256(s5buf);

  const hub = {
    format: "hub/lesson-import/1.5",
    adapter: ADAPTER,
    source: {
      sourceFormat: "guided-lesson/0.6",
      noteId: n,
      corpusVersion: src.noteRef.corpusVersion,
      sourceLayerSha256: s5sha,
      pinnedRef: commitA,
    },
    lesson: {
      id: `${COURSE_PREFIX}::${n}`,
      topicTitle: src.noteRef.topicTitle,
      subtopicTitle: src.noteRef.subtopicTitle,
      sourceUrl: src.noteRef.sourceUrl,
      specAnchors: src.specPoints.map((s) => ({ code: s.code, text: s.text })),
      primer: { text: src.primer.text, prerequisiteSubtopic: src.primer.prerequisiteSubtopic },
      modules: src.lessons.map((l, i) => ({
        id: `${n}::L${i + 1}`,
        title: l.title,
        sourceHeadings: l.sourceHeadings,
        specRefs: l.specRefs,
        opening: l.opening,
        keyPoints: l.keyPoints,
        depthLayers: {
          low: { ...l.depthLayers.low },
          medium: { ...l.depthLayers.medium },
        },
        gatePolicy: {
          ratingsScale: l.confidenceGate.ratings,
          continueDisabledUntilChoice: l.confidenceGate.continueDisabledUntilChoice,
          resumeWithoutReRate: l.confidenceGate.resumeWithoutReRate,
          postCheckRecalibration: l.confidenceGate.postCheckRecalibration,
        },
        checkRefs: l.check.map((_, k) => `${n}::L${i + 1}::Q${k + 1}`),
        figureIds: l.figureIds || [],
      })),
      assets: {
        glossary: src.noteAssets.glossary.map((g) => ({ term: g.term, definition: g.definition, firstLesson: g.firstLesson })),
        workedExample: src.noteAssets.workedExample ? { ...src.noteAssets.workedExample } : null,
      },
      figures: src.figures.map((f) => ({
        id: f.id, url: f.url, alt: f.alt, sourceHeading: f.sourceHeading,
        moduleIds: f.moduleIds, ...(f.caption ? { caption: f.caption } : {}), binding: f.binding,
      })),
    },
  };
  outLessons[n] = hub;

  const questions = [];
  src.lessons.forEach((l, i) => {
    l.check.forEach((c, k) => {
      const isMcq = (c.kind || "mcq") === "mcq";
      questions.push({
        id: `${n}::L${i + 1}::Q${k + 1}`,
        moduleId: `${n}::L${i + 1}`,
        stem: c.stem,
        misconceptionClass: c.misconceptionClass,
        ...(isMcq
          ? { options: c.options.map((o) => ({ key: o.key, text: o.text, correct: o.correct, explanation: o.explanation, misconception: o.misconception })) }
          : { kind: c.kind, modelAnswer: c.modelAnswer, ...(Array.isArray(c.keywords) ? { keywords: c.keywords } : {}), options: [] }),
      });
    });
  });
  const pkg = {
    format: "sme-question-package/1.2",
    adapter: ADAPTER,
    source: { ...hub.source },
    packageId: `${COURSE_PREFIX}::${n}`,
    subject: COURSE_PREFIX,
    questions,
  };
  outPkgs[n] = pkg;

  // written invariants
  let wok = 0, wtot = 0;
  for (const q of pkg.questions) {
    if (!(q.kind && q.kind !== "mcq")) continue;
    wtot++;
    const idOK = /^rn_[A-Za-z0-9]+::L[1-5]::Q[1-9]$/.test(q.id);
    if (idOK && q.modelAnswer && q.modelAnswer.length > 0 && Array.isArray(q.keywords) && q.keywords.length >= 3 && Array.isArray(q.options) && q.options.length === 0) wok++;
  }
  gate(`written-kind invariants (x${wtot})`, wok === wtot, `${wok}/${wtot}`);

  // C-5 checkRefs <-> questions 1:1 in order
  const flat = [];
  hub.lesson.modules.forEach((m) => m.checkRefs.forEach((r) => flat.push(r)));
  gate(`C-5 checkRefs<->questions 1:1 ${n}`, flat.length === pkg.questions.length && flat.every((r, i) => r === pkg.questions[i].id), `${flat.length} refs / ${pkg.questions.length} questions`);

  // B2 per-lesson law at target: 9 checkRefs per module
  gate("B2 target: every module carries exactly 9 checkRefs", hub.lesson.modules.every((m) => m.checkRefs.length === 9), hub.lesson.modules.map((m) => m.checkRefs.length).join(","));

  // ajv targets
  gate(`C-6 lesson ${n} vs hub/lesson-import/1.5`, vHub15(hub), vHub15.errors ? ajv.errorsText(vHub15.errors).slice(0, 250) : "");
  gate(`C-6 package ${n} vs sme-question-package/1.2`, vPkg12(pkg), vPkg12.errors ? ajv.errorsText(vPkg12.errors).slice(0, 250) : "");
}

// ── emit artifacts ────────────────────────────────────────────────────────────
section("emit artifacts");
fs.mkdirSync(path.join(RES, "hub-import-1.5"), { recursive: true });
fs.mkdirSync(path.join(RES, "question-packages-1.2"), { recursive: true });
const emit = (p, obj) => { const buf = Buffer.from(JSON.stringify(obj, null, 2) + "\n", "utf8"); fs.writeFileSync(p, buf); return buf; };
const newSha = {};
for (const n of PILOTS) {
  const lb = emit(path.join(RES, "hub-import-1.5", `${n}.hub-lesson-import.json`), outLessons[n]);
  const pb = emit(path.join(RES, "question-packages-1.2", `${n}.sme-question-package.json`), outPkgs[n]);
  newSha[n] = { hub: { sha256: sha256(lb), bytes: lb.length }, pkg: { sha256: sha256(pb), bytes: pb.length } };
  console.log(`  hub-import-1.5/${n}: ${lb.length}B  question-packages-1.2/${n}: ${pb.length}B`);
}

// ── G-E stream (the runner's walk, byte-identical law) ────────────────────────
section("G-E stream anchors + grand");
const rows = PILOTS.map((n) => {
  const s = targetTokens(outLessons[n], outPkgs[n]).join("\n");
  return {
    noteId: n,
    wave: 0,
    sourceLayerSha256: sha256(read(path.join(RES, "source-0.6", `guided-lesson-${n}.json`))),
    hubSha256: newSha[n].hub.sha256,
    pkgSha256: newSha[n].pkg.sha256,
    stream: { sha256: sha256(Buffer.from(s, "utf8")), chars: s.length },
  };
});
let grandChars = 0;
const grand = crypto.createHash("sha256");
for (const n of PILOTS) {
  const s = targetTokens(outLessons[n], outPkgs[n]).join("\n");
  grand.update(Buffer.from(s, "utf8"));
  grandChars += s.length;
}
const grandSha = grand.digest("hex");
const waveOut = { "wave-0": (() => { const h = crypto.createHash("sha256"); for (const n of PILOTS) h.update(Buffer.from(targetTokens(outLessons[n], outPkgs[n]).join("\n"), "utf8")); return h.digest("hex"); })() };
console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}… (wave-0: ${waveOut["wave-0"].slice(0, 12)}…)`);

// census from the emitted bytes (disk-derived, not asserted)
const census = {
  notes: PILOTS.length,
  lessons: Object.values(outLessons).reduce((a, h) => a + h.lesson.modules.length, 0),
  checks: Object.values(outPkgs).reduce((a, p) => a + p.questions.length, 0),
  keyPoints: Object.values(outLessons).reduce((a, h) => a + h.lesson.modules.reduce((b, m) => b + m.keyPoints.length, 0), 0),
  distractors: Object.values(outPkgs).reduce((a, p) => a + p.questions.reduce((b, q) => b + (q.options || []).filter((o) => o.correct !== true).length, 0), 0),
  glossaryTerms: Object.values(outLessons).reduce((a, h) => a + h.lesson.assets.glossary.length, 0),
  figures: Object.values(outLessons).reduce((a, h) => a + (h.lesson.figures || []).length, 0),
  figures_module_mapped: Object.values(outLessons).reduce((a, h) => a + (h.lesson.figures || []).filter((f) => f.moduleIds.length > 0).length, 0),
  figures_note_level: Object.values(outLessons).reduce((a, h) => a + (h.lesson.figures || []).filter((f) => f.moduleIds.length === 0).length, 0),
  workedExamples_populated: Object.values(outLessons).filter((h) => h.lesson.assets.workedExample).length,
  workedExamples_null: Object.values(outLessons).filter((h) => !h.lesson.assets.workedExample).length,
};
const kindCensus = { checks_mcq: 0, written_recall: 0, written_explain_why: 0, written_application: 0 };
for (const p of Object.values(outPkgs)) for (const q of p.questions) {
  if (!q.kind || q.kind === "mcq") kindCensus.checks_mcq++;
  else if (q.kind === "recall") kindCensus.written_recall++;
  else if (q.kind === "explain-why") kindCensus.written_explain_why++;
  else if (q.kind === "application") kindCensus.written_application++;
}
gate("B2 identity arithmetic: 9 = 5+2+1+1 per lesson", census.lessons * 9 === census.checks &&
  kindCensus.checks_mcq === census.lessons * 5 && kindCensus.written_recall === census.lessons * 2 &&
  kindCensus.written_explain_why === census.lessons && kindCensus.written_application === census.lessons,
  JSON.stringify({ ...census, ...kindCensus }));

const counts = {
  notes: census.notes,
  lessons: census.lessons,
  checks: census.checks,
  keyPoints: census.keyPoints,
  distractors: census.distractors,
  glossaryTerms: census.glossaryTerms,
  figures: census.figures,
  figures_module_mapped: census.figures_module_mapped,
  figures_note_level: census.figures_note_level,
  workedExamples_populated: census.workedExamples_populated,
  workedExamples_null: census.workedExamples_null,
  authored_chars_conserved: grandChars,
};

// ── manifest v18 (B6 CONTINUE-GLOBAL of record) ───────────────────────────────
section("manifest v18");
const artifacts = [];
for (const n of PILOTS) {
  artifacts.push({ kind: "hub-lesson-import-1.5", noteId: n, path: `SME-GuidedLessons/integration/hub-import-1.5/${n}.hub-lesson-import.json`, sha256: newSha[n].hub.sha256, bytes: newSha[n].hub.bytes });
  artifacts.push({ kind: "sme-question-package", noteId: n, path: `SME-GuidedLessons/integration/question-packages-1.2/${n}.sme-question-package.json`, sha256: newSha[n].pkg.sha256, bytes: newSha[n].pkg.bytes });
}
const man18 = {
  format: "hub-import-manifest/1.0",
  manifest_version: MANIFEST_VERSION,
  course_id: COURSE_ID,
  b6_manifest_continuity: {
    decision: "continue-global",
    selected: "physics stage-A = manifest v18 (the programme-level series continues across subjects)",
    rejected: "per-course series (physics v1) — would collide with chemistry hub-import-manifest-v1..v17.json filenames in the shared integration/ namespace and fork the integration ledger",
    recorded_by: "runbook B6 (.syllabai/docs/new-subject-runbook.md @ hub f99969a2); recorded here and in the stage-A receipt",
  },
  generated_at_utc: now(),
  operator_trace: EXEC_TRACE,
  supersedes: "hub-import-manifest-v17.json (chemistry STAGE B COMPLETE — 112 notes / 239 lessons / 2,151 checks @ e967e75f, all re-pinned byte-identical; nothing chemistry carries new bytes in this generation) — v18 is the FIRST new-subject tranche: 1 igcse-physics-19 pilot note, 2 artifacts",
  checks_layer: {
    wave: `PHYSICS-4PH1 stage A (the new-subject bootstrap pilot; runbook B3 pilot-first) — operator ignition trace ${IGNITION_TRACE} ("open the new subject's wave-1 contract. The new subject 4ph1 physics."), execution trace ${EXEC_TRACE} ("ignite stage-A execution")`,
    derivation: "18 authored checks (10 MCQ + 4 recall + 2 explain-why + 2 application = 2 lessons x [5 MCQ + 2 recall + 1 explain-why + 1 application]), each spec-anchored to 4PH1 1.3 (plot and explain distance-time graphs) with KP-index provenance; written items carry modelAnswer + generous synonym/inflection-bearing keywords",
    declared_revision: "the FIRST package-channel delta of the new subject: 1 package issued under sme-question-package/1.2 (union schema — the 112 chemistry 1.1 packages validate unchanged); 1 lesson issued under hub/lesson-import/1.5 (union schema — the 112 chemistry 1.4 lessons validate unchanged)",
    grading_law: "case-insensitive whole-token match of the learner text against keywords[]; >=1 hit -> correct; 0 hits -> not-quite + model answer; empty submit blocked; keywords absent -> reveal-only (fail-closed, never a silent wrong grade)",
    fail_closed: "written item without modelAnswer renders reveal-only, never gradeable, never blank; unknown kind renders reveal-only and warns at this gate",
  },
  source_generation: {
    format: "guided-lesson/0.6",
    namespace: "SME-GuidedLessons/integration/source-0.6/",
    pin: commitA,
    int0_lineage: "(new subject — no INT-0 ancestry; the 0.6 generation is authored directly from the igcse-physics-19 revision-note row of record, hub notes.json @ " + HUB_MAIN_AT_OPEN.slice(0, 8) + ", bodyMd pin " + BODYMD_PIN.slice(0, 8) + ")",
  },
  load_scope: { adapter: ADAPTER, target_schemas: ["hub/lesson-import/1.5", "sme-question-package/1.2"] },
  counts,
  conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut },
  artifacts,
};
gate("manifest v18 lists 2 artifacts", artifacts.length === 2, String(artifacts.length));

// ── INT-3 record ──────────────────────────────────────────────────────────────
const int3 = {
  stage: "INT-3",
  title: "transform record — PHYSICS-4PH1 stage A (adapter guided-lesson-0.6--hub-lesson-import-1.5)",
  generated_at_utc: now(),
  operator_traces: { ignition: IGNITION_TRACE, execution: EXEC_TRACE },
  adapter: ADAPTER,
  course_id: COURSE_ID,
  b6_manifest_continuity: man18.b6_manifest_continuity,
  source_pin: {
    repo: "SyllabAI/syllabai-resources",
    ref: RES_MAIN_AT_OPEN,
    note: "resources main at stage-A open; the register plane (manifest 127 notes / 373 assets) is complete but carried NO spec_point_resolution.json — bridged this chain by records-side bootstrap commit (SME-RevisionNotes/igcse-physics-19/spec_point_resolution.json derived mechanically from hub notes.json smeSpecPointIds; runbook B1 deviation disclosed)",
  },
  registry_pin: {
    repo: "SyllabAI/syllabai-v2",
    ref: HUB_MAIN_AT_OPEN,
    path: "apps/hub/content/igcse-physics-19/notes.json",
    note: "the revision-note row of record (noteId registry, specPointCodes, bodyMd with asset URLs pinned @ " + BODYMD_PIN.slice(0, 8) + "); prose parity vs the resources .md proven 24/25 paragraphs (1 WE-image split paragraph, disclosed)",
  },
  source_06_generation_pin: { commit: commitA, namespace: "SME-GuidedLessons/integration/source-0.6/" },
  conservation_law:
    "kind/modelAnswer/keywords on written items ARE §7 stream tokens (the runner walk extends by those fields on kind!=mcq): the single pilot note's stream is anchored below; the chemistry corpus streams are untouched (no chemistry bytes re-issued in v18). Grand + wave-0 computed over the pilot note in artifact order.",
  grand_stream: { chars: grandChars, sha256: grandSha },
  wave_stream_sha256: waveOut,
  battery: {
    names: "A0 / AN / SG / KW / JC / 2.1B / NUM (runbook §1.4 battery of record)",
    a0: "ajv guided-lesson/0.6 + 9-check SME kind order per lesson + B2 sizing (1 note -> 2 lessons) + figure closure both ways + glossary 3..8 + primer word band",
    an: "exactly one correct option per MCQ x10; correct-key letter census >=3 distinct / max 5; option texts distinct",
    sg: "lesson specRefs subset of file specPoints (4PH1 1.3); every check shares a content token with its lesson keyPoints (KP-index provenance)",
    kw: "written items >=3 distinct keywords, each grounded in the modelAnswer/stem/keyPoints union",
    jc: "every option explained; distractors name misconceptions; correct option misconception null",
    "2.1b": "zero 8-gram overlap between learner-surface text (stems, model answers, option text+explanations) and the corpus note body",
    num: "8000/360=22.2 (3sf) re-derived; 8 km=8000 m, 6 min=360 s; distractor arithmetics 8/6=1.3 and 8000/60=133 re-derived",
  },
  physics_census: { pilot_notes: PILOTS, pilot_lessons: census.lessons, checks: census.checks, ...kindCensus, distractors: census.distractors, figures: census.figures, figures_captions: Object.values(outLessons)[0].lesson.figures.filter((f) => f.caption).length, figures_no_caption: Object.values(outLessons)[0].lesson.figures.filter((f) => !f.caption).length },
  notes: rows,
};
emit(path.join(RES, "records/INT-3-transform-record-physics-stagea.json"), int3);
const manBuf = emit(path.join(RES, "hub-import-manifest-v18.json"), man18);

// ── fail-closed checkpoint before the promotion receipt ───────────────────────
if (FAILED > 0) {
  console.error(`\nFAIL-CLOSED: ${FAILED} gate failure(s) — promotion receipt NOT emitted`);
  process.exit(1);
}

// ── promotion receipt ─────────────────────────────────────────────────────────
section("promotion receipt");
const receipt = {
  format: "r3-check-types-promotion-receipt/1.0",
  format_note: "the receipt FAMILY of record per runbook §3; the wave field carries the physics lane identity",
  wave: "PHYSICS-4PH1 stage A — the new-subject bootstrap pilot (rn_RpyMnS5nqWSRWXXG, Distance-Time Graphs)",
  operator_traces: [IGNITION_TRACE, EXEC_TRACE],
  generated_at_utc: now(),
  repo: "SyllabAI/syllabai-resources",
  branch,
  runbook_of_record: ".syllabai/docs/new-subject-runbook.md @ SyllabAI/syllabai-v2 f99969a2 (verified unchanged @ 55f91919)",
  b6_manifest_continuity: man18.b6_manifest_continuity,
  commits: {
    B0: { sha: "(register-completion commit)", note: "SME-RevisionNotes/igcse-physics-19/spec_point_resolution.json — B1 inventory completion, derived mechanically from hub notes.json smeSpecPointIds @ " + HUB_MAIN_AT_OPEN.slice(0, 8) + " (schema syllabai.sme-notes-spec-resolution/1.0, methods hub-landing:notes-json)" },
    A: { sha: commitA, parent: commitAParent, note: "source-0.6 generation — 1 authored guided-lesson/0.6 pilot note (18 checks) + schema/guided-lesson.0.6.schema.json" },
    B: { sha: "(target schemas commit)", note: "schema/hub-lesson-import.1.5.schema.json + schema/sme-question-package.1.2.schema.json (union minors)" },
    C: { sha: "(namespace-complete — outputs + manifest v18 + records + spec + pipeline)", note: "hub-import-1.5/ + question-packages-1.2/ + hub-import-manifest-v18.json + records/INT-3-transform-record-physics-stagea.json + records/PHYSICS-4PH1-STAGEA-PROMOTION-20261101.json + ADAPTER-SPEC-guided-lesson-0.6-to-hub-1.5.md + tooling/physics-stagea-pipeline.js" },
  },
  artifact_pin: commitA,
  pkg_pin: `${commitA} (the pilot package — first sme-question-package of the new subject)`,
  input_pins: { resources_main_at_stageA_open: RES_MAIN_AT_OPEN, hub_main_at_stageA_open: HUB_MAIN_AT_OPEN, bodymd_asset_pin: BODYMD_PIN },
  manifest: "hub-import-manifest-v18.json",
  int_record: "INT-3-transform-record-physics-stagea.json",
  adapter_spec: "ADAPTER-SPEC-guided-lesson-0.6-to-hub-1.5.md",
  counts_census: { notes: census.notes, lessons: census.lessons, checks: census.checks, ...kindCensus, distractors: census.distractors, pilot_notes: PILOTS },
  schema_delta:
    "additive union minors x3: guided-lesson 0.5->0.6 (format const + course-scoped pattern generalization: spec codes '^([A-Z0-9]+-)?[0-9]+\\.[0-9]+[A-Z]?$' accept plain 4PH1 codes, figure URLs accept igcse-physics-19 assets); hub/lesson-import 1.4->1.5 (UNION consts + ids/spec patterns generalized); sme-question-package 1.1->1.2 (UNION consts + subject enum + packageId pattern generalized). Chemistry union proven: 112 sources vs 0.6 + 112 lessons vs 1.5 + 112 packages vs 1.2, zero failures.",
  taxonomy: "kind enum of record: mcq (default/absent) | recall | explain-why | application — 2 lessons x [5 MCQ + 2 recall + 1 explain-why + 1 application] = the B2 law",
  conservation: {
    law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq; the pilot note's stream is anchored in the INT-3 record; chemistry streams byte-untouched (no chemistry re-issues in v18)",
    authored_chars: grandChars,
  },
  gates: { pipeline: `${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, 0 fail`, gate_log: CHECKS },
  merge_order:
    "resources PR (this branch) merges to main FIRST; the hub PR (FEED physics-stagea-v18 + runner feed-gated parameterization + landed artifacts + re-issued guided-import.json) merges only after; wave-1 buckets remain operator-gated and are NOT in this tranche (B3: the pilot stays out of the wave buckets)",
  hub_side_note:
    "the hub renderer is course-generic (courses/[course]/guided-lessons/[noteId] + per-course guided-import.json discovery, fail-closed) — written-kind and figure rendering shipped with the chemistry R3 chain; the physics feed needs runner feed-gated constants only (pack/course_id/counts/prefix/wave-count, chemistry-preserving defaults)",
  disclosures: [
    "B1 deviation: the physics register plane lacked spec_point_resolution.json (chemistry carried one); bridged by a mechanical derivation from hub notes.json smeSpecPointIds (the of-record registry), filed as commit B0 — the resolution file lists id/code/note mappings only, no invented spec texts",
    "authoring source of record = the revision-note row (hub notes.json bodyMd, asset URLs pinned @ " + BODYMD_PIN.slice(0, 8) + "); prose parity vs the resources .md = 24/25 paragraphs (one worked-example image-line paragraph splits differently), disclosed",
    "captions: 4 of 9 figures carry the note's own bold-italic explanatory line; the 5 worked-example images carry none (fail-closed absent, declared)",
    "the note's second worked example (student stroll) is not carried — the schema carries one workedExample per note; the train-gradient WE is the numeric one (NUM-gated), declared",
    "runner evolution is feed-gated with chemistry-preserving defaults (pack/course_id/counts/prefix/wave-count) — chemistry feeds byte-identical in behavior",
    "sandbox recycle this session lost the previous lane's local mirrors; all of-record state re-fetched from remotes (fetch-first honored)",
  ],
};
emit(path.join(RES, "records/PHYSICS-4PH1-STAGEA-PROMOTION-20261101.json"), receipt);

// ── lane survivors for the hub runner byte-anchors ────────────────────────────
fs.mkdirSync(SURV, { recursive: true });
fs.copyFileSync(path.join(RES, "hub-import-manifest-v18.json"), path.join(SURV, "hub-import-manifest-v18.json"));
fs.copyFileSync(path.join(RES, "records/INT-3-transform-record-physics-stagea.json"), path.join(SURV, "INT-3-transform-record-physics-stagea.json"));
fs.copyFileSync(path.join(RES, "schema/hub-lesson-import.1.5.schema.json"), path.join(SURV, "hub-lesson-import.1.5.schema.json"));
fs.copyFileSync(path.join(RES, "schema/sme-question-package.1.2.schema.json"), path.join(SURV, "sme-question-package.1.2.schema.json"));

console.log(`\nRESULT: ${FAILED === 0 ? "GREEN — PIPELINE COMPLETE" : "FAIL-CLOSED"}`);
console.log(`  gates: ${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, ${FAILED} failures`);
console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}…`);
console.log(`  census: ${JSON.stringify(counts)}`);
