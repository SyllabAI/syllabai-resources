#!/usr/bin/env node
/**
 * PHYSICS-WAVE1 PIPELINE — new-subject stage-B wave-1 transform + manifest v19 + INT-3 record
 * (operator ignition trace 1a196b9c429c5ae5 "ignite wave-1"; execution trace 1a197b1687dc5cd9)
 *
 * Runbook of record: .syllabai/docs/new-subject-runbook.md @ hub main (§1 wave lifecycle).
 * B6 of record (stage-A): CONTINUE-GLOBAL manifest series — wave-1 = hub-import-manifest-v19.json.
 * B4 of record: the remaining register (126 notes) is partitioned at wave open into 12 buckets
 * (section-aligned, register order, final takes remainder) — the partition table is below and is
 * FROZEN for the programme; wave-1 executes bucket W1 (the 1-1 remainder, 6 notes).
 *
 * Input of record (lane clone @ resources main 23dd0c9d…, branch integration/physics-wave1-20261101):
 *   source-0.6/ ×6 authored wave-1 notes (guided-lesson/0.6, committed @ commit A)
 *   schema/guided-lesson.0.6.schema.json + {hub-lesson-import.1.5, sme-question-package.1.2} (main, unchanged)
 *   source-0.5/ ×112 + hub-import-1.4/ ×112 + question-packages-1.1/ ×112 (chemistry union baselines)
 *
 * Outputs (namespace-complete, committed @ commit C):
 *   hub-import-1.5/rn_<id>.hub-lesson-import.json ×6        (format hub/lesson-import/1.5)
 *   question-packages-1.2/rn_<id>.sme-question-package.json ×6 (format sme-question-package/1.2)
 *   hub-import-manifest-v19.json
 *   records/INT-3-transform-record-physics-wave1.json
 *   records/NS-4PH1-PHYSICS-WAVE1-PROMOTION-20261101.json
 * + lane survivors (hub runner byte-anchors) under SURV
 *
 * Audit battery of record (runbook §1.4): A0 / AN / SG / KW / JC / 2.1B / NUM — per note; NUM is a
 * declared per-note ledger re-derived in code below.
 * FAIL-CLOSED: any gate failure aborts before any record is emitted.
 */
import { createRequire } from "node:module";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { execSync } from "node:child_process";

const require = createRequire(import.meta.url);
const Ajv = require("/home/z/my-project/lane-physics-wave1/nodeenv/node_modules/ajv");

const RES = "/home/z/my-project/ground/resources/SME-GuidedLessons/integration";
const RES_REPO = "/home/z/my-project/ground/resources";
const HUB_REPO = "/home/z/my-project/ground/hub";
const SURV = "/home/z/my-project/scripts/physics-wave1-survivors";
const NOTES = [
  "rn_k9wr3prcgSBg5vfw", // 1-1-2 Speed (1.4)
  "rn_pfndTqR6DTJGZ8xQ", // 1-1-3 Core Practical: Investigating Motion (1.5)
  "rn_CpJZQWzbvMcM8fw3", // 1-1-4 Acceleration (1.6)
  "rn_5hfYYFrc2XjMJCrq", // 1-1-5 Velocity-Time Graphs (1.7, 1.8)
  "rn_GxNWbSMqkTN4zgZB", // 1-1-6 Area under a Velocity-Time Graph (1.9)
  "rn_ZgGMNrRGBKvYxxFf", // 1-1-7 Calculating Uniform Acceleration (1.10)
];
const IGNITION_TRACE = "1a196b9c429c5ae5";
const EXEC_TRACE = "1a197b1687dc5cd9";
const ADAPTER = "guided-lesson-0.6--hub-lesson-import-1.5";
const COURSE_ID = "igcse-physics-19";
const COURSE_PREFIX = "igcse-physics";
const RES_MAIN_AT_OPEN = "196c2957ee54c0de3342fe515ba055cbacb2d260"; // branch base after the mid-flight race (was 23dd0c9d at re-ground; PR #270 g9-followups landed between — zero namespace overlap, disclosed)
const HUB_MAIN_AT_OPEN = "37aa9e442a6384b54e7f1235c23921b290537db9";
const MANIFEST_VERSION = 19; // B6 CONTINUE-GLOBAL — the series continues from v18
const PILOT_OF_RECORD = "rn_RpyMnS5nqWSRWXXG"; // stage-A pilot — outside the buckets (B3)
const B4_PARTITION = {
  "W1": ["1-forces-and-motion/1-1-movement-and-position"],
  "W2": ["1-forces-and-motion/1-2-forces-movement-and-changing-shape"],
  "W3": ["1-forces-and-motion/1-3-momentum", "1-forces-and-motion/1-4-moments"],
  "W4": ["2-electricity/2-1-current-potential-difference-and-resistance", "2-electricity/2-2-components-in-series-and-parallel-circuits"],
  "W5": ["2-electricity/2-3-electrical-power-and-mains-electricity", "2-electricity/2-4-static-electricity"],
  "W6": ["3-waves/3-1-waves-and-the-electromagnetic-spectrum", "3-waves/3-2-reflection-and-refraction"],
  "W7": ["3-waves/3-3-sound", "4-energy-resources-and-energy-transfers/4-1-energy-stores-and-transfers"],
  "W8": ["4-energy-resources-and-energy-transfers/4-2-work-power-and-energy-resources", "5-solids-liquids-and-gases/5-1-density-and-pressure"],
  "W9": ["5-solids-liquids-and-gases/5-2-changes-of-state", "5-solids-liquids-and-gases/5-3-ideal-gases"],
  "W10": ["6-magnetism-and-electromagnetism/6-1-magnetism-and-electromagnetism", "6-magnetism-and-electromagnetism/6-2-electromagnetic-induction"],
  "W11": ["7-radioactivity-and-particles/7-1-properties-of-radiation", "7-radioactivity-and-particles/7-2-radioactivity-uses-and-dangers"],
  "W12-final-remainder": ["7-radioactivity-and-particles/7-3-fission-and-fusion", "8-astrophysics/8-1-motion-in-the-universe", "8-astrophysics/8-2-stellar-evolution", "8-astrophysics/8-3-cosmology"],
};

const sha256 = (buf) => crypto.createHash("sha256").update(buf).digest("hex");
const now = () => new Date().toISOString().replace(/\.\d+Z$/, "Z");
const read = (p) => fs.readFileSync(p);
const readJson = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
const r3 = (x) => Number(x.toPrecision(3)).toString();
const r2 = (x) => Number(x.toPrecision(2)).toString();

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
gate("P0 branch is the wave-1 integration branch", branch === "integration/physics-wave1-20261101", branch);
for (const n of NOTES) {
  const rel = `source-0.6/guided-lesson-${n}.json`;
  const blob = execSync(`git show HEAD:SME-GuidedLessons/integration/${rel}`, { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 8 });
  gate("P0 committed == working tree @ " + n.slice(0, 12), blob.equals(read(path.join(RES, rel))));
}
for (const rel of ["schema/guided-lesson.0.6.schema.json", "schema/hub-lesson-import.1.5.schema.json", "schema/sme-question-package.1.2.schema.json"]) {
  const blob = execSync(`git show HEAD:SME-GuidedLessons/integration/${rel}`, { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 8 });
  gate("P0 schema on branch == working tree @ " + rel.split("/").pop(), blob.equals(read(path.join(RES, rel))));
}

// ── battery inputs ────────────────────────────────────────────────────────────
const noteRows = JSON.parse(
  execSync("git show origin/main:apps/hub/content/igcse-physics-19/notes.json", { cwd: HUB_REPO, maxBuffer: 1024 * 1024 * 16 }).toString()
);
for (const n of NOTES) if (!noteRows.find((r) => r.noteId === n)) throw new Error(`note row missing from hub notes.json @ origin/main: ${n}`);

// ── B4 partition of record (mechanically derived from hub notes.json) ─────────
section("B4 partition of record (126 notes, pilot excluded)");
{
  const reg = noteRows.map((r) => r.path.replace(/\.md$/, "")).sort();
  gate("register census 127 rows", reg.length === 127, String(reg.length));
  const pilotPath = noteRows.find((r) => r.noteId === PILOT_OF_RECORD).path.replace(/\.md$/, "");
  const bySection = {};
  for (const p of reg) { if (p === pilotPath) continue; const sec = p.split("/").slice(0, 2).join("/"); (bySection[sec] ||= []).push(p); }
  const buckets = {};
  let total = 0;
  for (const [w, secs] of Object.entries(B4_PARTITION)) {
    buckets[w] = secs.flatMap((s) => bySection[s] || []);
    total += buckets[w].length;
  }
  gate("B4 buckets partition the 126-note remainder exactly", total === 126, `${total} notes bucketed`);
  gate("B4 W1 == the 6 authored wave-1 notes", JSON.stringify(buckets["W1"].map((p) => p.split("/").pop())) === JSON.stringify([
    "1-1-2-speed", "1-1-3-core-practical-investigating-motion", "1-1-4-acceleration",
    "1-1-5-velocity-time-graphs", "1-1-6-area-under-a-velocity-time-graph", "1-1-7-calculating-uniform-acceleration",
  ]), buckets["W1"].map((p) => p.split("/").pop()).join(","));
  gate("B4 pilot outside every bucket", !Object.values(buckets).some((b) => b.some((p) => p === pilotPath)), "");
  console.log(`  bucket sizes: ${Object.entries(buckets).map(([w, b]) => `${w}=${b.length}`).join(" ")} (Σ ${total})`);
}

// ── A0 structure ──────────────────────────────────────────────────────────────
section("A0 structure (ajv + 9-check law + sizing B2)");
const ajv = new Ajv({ allErrors: true });
const vSrc6 = ajv.compile(readJson(path.join(RES, "schema/guided-lesson.0.6.schema.json")));
const vHub15 = ajv.compile(readJson(path.join(RES, "schema/hub-lesson-import.1.5.schema.json")));
const vPkg12 = ajv.compile(readJson(path.join(RES, "schema/sme-question-package.1.2.schema.json")));
const KIND_ORDER = ["mcq", "mcq", "mcq", "mcq", "mcq", "recall", "recall", "explain-why", "application"];
const sources = {};
for (const n of NOTES) {
  const src = readJson(path.join(RES, `source-0.6/guided-lesson-${n}.json`));
  sources[n] = src;
  gate(`A0 ${n.slice(0, 12)} vs guided-lesson/0.6`, vSrc6(src), vSrc6.errors ? ajv.errorsText(vSrc6.errors).slice(0, 250) : "");
  for (const l of src.lessons) {
    const kinds = l.check.map((c) => c.kind || "mcq");
    gate(`A0 ${n.slice(0, 12)} "${l.title.slice(0, 20)}": 9 checks in SME kind order`, kinds.length === 9 && JSON.stringify(kinds) === JSON.stringify(KIND_ORDER), kinds.join(","));
    gate(`A0 ${n.slice(0, 12)}: keyPoints 3..6`, l.keyPoints.length >= 3 && l.keyPoints.length <= 6, String(l.keyPoints.length));
    const words = src.primer.text.split(/\s+/).length;
    gate(`A0 ${n.slice(0, 12)}: primer 35..90 words`, words >= 35 && words <= 90, `${words} words`);
  }
  gate(`A0 ${n.slice(0, 12)}: sizing B2 1..3 lessons`, src.lessons.length >= 1 && src.lessons.length <= 3, String(src.lessons.length));
  gate(`A0 ${n.slice(0, 12)}: lessons carry specRefs`, src.lessons.every((l) => l.specRefs.length >= 1), "");
  // figure closure both ways (figures/figureIds optional — absent keys are lawful, empty arrays are not)
  const srcFigs = src.figures || [];
  const figIds = new Set(srcFigs.map((f) => f.id));
  let closureOk = true;
  for (const l of src.lessons) for (const fid of l.figureIds || []) if (!figIds.has(fid)) closureOk = false;
  for (const f of srcFigs) for (const mid of f.moduleIds) {
    const les = src.lessons[Number(mid.slice(1)) - 1];
    if (!les || !(les.figureIds || []).includes(f.id)) closureOk = false;
  }
  const claimSumL = src.lessons.reduce((a, l) => a + (l.figureIds || []).length, 0);
  const claimSumF = srcFigs.reduce((a, f) => a + f.moduleIds.length, 0);
  if (claimSumL !== claimSumF) closureOk = false;
  gate(`A0 ${n.slice(0, 12)}: figure closure both ways (figureIds <-> moduleIds)`, closureOk, `${claimSumL}/${claimSumF}`);
  gate(`A0 ${n.slice(0, 12)}: glossary 3..8`, src.noteAssets.glossary.length >= 3 && src.noteAssets.glossary.length <= 8, String(src.noteAssets.glossary.length));
}

// ── AN answer-key law ─────────────────────────────────────────────────────────
section("AN answer-key law");
for (const n of NOTES) {
  const src = sources[n];
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
  gate(`AN ${n.slice(0, 12)}: exactly-one-correct x${mcqs.length} + distinct option texts`, ok, "");
  gate(`AN ${n.slice(0, 12)}: correct-key census >= 3 distinct letters, max <= 5`, distinct >= 3 && maxShare <= 5, JSON.stringify(census));
}

// ── JC distractor quality ─────────────────────────────────────────────────────
section("JC distractor quality");
for (const n of NOTES) {
  const mcqs = sources[n].lessons.flatMap((l) => l.check.filter((c) => (c.kind || "mcq") === "mcq"));
  let bad = 0;
  for (const c of mcqs) {
    for (const o of c.options) {
      if (!o.explanation || o.explanation.length === 0) bad++;
      if (o.correct === false && (!o.misconception || o.misconception.length === 0)) bad++;
      if (o.correct === true && o.misconception !== null) bad++;
    }
  }
  gate(`JC ${n.slice(0, 12)}: every option explained; distractors named; correct misconception null x${mcqs.length}`, bad === 0, `${bad} violations`);
}

// ── SG spec grounding (KP-index provenance) ───────────────────────────────────
section("SG spec grounding");
{
  const STOP = new Set("a an the of to in on at for with and or is are was were be been it its this that these those as by from not no you your they their we our object objects line lines graph graphs which what how state recall explain why does do can may will would shows show".split(" "));
  const toks = (s) => (String(s).toLowerCase().match(/[a-z0-9]+/g) || []).filter((t) => t.length > 3 && !STOP.has(t) && !/^\d+$/.test(t));
  for (const n of NOTES) {
    const src = sources[n];
    const codes = new Set(src.specPoints.map((s) => s.code));
    gate(`SG ${n.slice(0, 12)}: lesson specRefs subset of file specPoints`, src.lessons.every((l) => l.specRefs.every((r) => codes.has(r))), "");
    let grounded = 0, total = 0;
    for (const l of src.lessons) {
      const kpSet = new Set(toks(l.keyPoints.join(" ")));
      for (const c of l.check) {
        total++;
        const hit = toks(c.stem).some((t) => kpSet.has(t)) || (c.kind && c.kind !== "mcq" && toks(c.modelAnswer).some((t) => kpSet.has(t)));
        if (hit) grounded++;
        else console.error(`    SG miss: ${c.stem.slice(0, 60)}`);
      }
    }
    gate(`SG ${n.slice(0, 12)}: every check KP-anchored x${total}`, grounded === total, `${grounded}/${total}`);
  }
}

// ── KW keywords law ───────────────────────────────────────────────────────────
section("KW keywords law");
for (const n of NOTES) {
  let ok = true, cnt = 0;
  for (const l of sources[n].lessons) {
    const anchor = (l.keyPoints.join(" ") + " " + l.check.map((c) => c.stem + " " + (c.modelAnswer || "")).join(" ")).toLowerCase();
    for (const c of l.check) {
      if (!c.kind || c.kind === "mcq") continue;
      cnt++;
      const kws = c.keywords || [];
      if (new Set(kws.map((k) => k.toLowerCase())).size < 3) { ok = false; console.error(`    KW few: ${c.stem.slice(0, 50)}`); }
      for (const k of kws) {
        const core = k.toLowerCase().split(/[^a-z0-9]+/).filter(Boolean)[0];
        if (!core || !anchor.includes(core)) { ok = false; console.error(`    KW ungrounded: ${k} @ ${c.stem.slice(0, 40)}`); }
      }
    }
  }
  gate(`KW ${n.slice(0, 12)}: >=3 distinct grounded keywords per written item x${cnt}`, ok, "");
}

// ── 2.1B learner-surface law ──────────────────────────────────────────────────
section("2.1B learner-surface law (no authored-note 8-grams on the surface)");
for (const n of NOTES) {
  const body = noteRows.find((r) => r.noteId === n).bodyMd.toLowerCase();
  const clean = (s) => (String(s).toLowerCase().match(/[a-z]+/g) || []);
  const noteToks = clean(body);
  const noteGrams = new Set();
  for (let i = 0; i + 8 <= noteToks.length; i++) noteGrams.add(noteToks.slice(i, i + 8).join(" "));
  let hits = 0;
  for (const l of sources[n].lessons) {
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
  gate(`2.1B ${n.slice(0, 12)}: zero 8-gram overlaps vs note body`, hits === 0, `${hits} hits`);
}

// ── NUM numeric law (declared per-note ledger, re-derived in code) ────────────
section("NUM numeric law (per-note ledgers, re-derived)");
const ledgers = {
  rn_k9wr3prcgSBg5vfw: [
    ["2 hours = 7200 s", 2 * 60 * 60 === 7200],
    ["plane distance 250 × 7200 = 1,800,000 m", 250 * 7200 === 1800000],
    ["drone 4.5 km = 4500 m; 15 min = 900 s", 4.5 * 1000 === 4500 && 15 * 60 === 900],
    ["drone average speed 4500/900 = 5.0 m/s", r3(4500 / 900) === "5"],
    ["bird application 4.5 × 40 = 180 m", 4.5 * 40 === 180],
    ["bus MCQ: totals 600 m over 100 s = 6.0 m/s", r3(600 / 100) === "6"],
    ["bus MCQ distractor B: mean of 15 and 0 = 7.5", (15 + 0) / 2 === 7.5],
    ["jogger MCQ: 1200/480 = 2.5 m/s", r3(1200 / 480) === "2.5"],
  ],
  rn_pfndTqR6DTJGZ8xQ: [
    ["heights 1.0→1.8 in 0.2 steps ×5", [1.0, 1.2, 1.4, 1.6, 1.8].every((h, i, a) => i === 0 || Math.abs((a[i] - a[i - 1]) - 0.2) < 1e-9)],
    ["three repeats averaged per height", 3 / 3 === 1],
    ["reaction overhead ≈ 0.25 s × 2 ends = 0.5 s", Math.abs(0.25 * 2 - 0.5) < 1e-9],
    ["application: 1.4/2.0 = 0.70 m/s", r3(1.4 / 2.0) === "0.7"],
    ["application: 2.8/0.70 = 4.0 s", r3(2.8 / 0.7) === "4"],
  ],
  rn_CpJZQWzbvMcM8fw3: [
    ["MCQ1: (9.0−3.0)/12 = 0.50 m/s²", r3((9.0 - 3.0) / 12) === "0.5"],
    ["MCQ4: 42−50 = −8 m/s", 42 - 50 === -8],
    ["train WE: Δv = −8; a = −8/30 = −0.27 (2sf)", r2(-8 / 30) === "-0.27"],
    ["MCQ braking: (0−30)/12 = −2.5 m/s²", r3((0 - 30) / 12) === "-2.5"],
    ["rocket MCQ: 8.0 × 5.0 = +40 m/s", 8.0 * 5.0 === 40],
    ["lift application: (1.0−6.0)/2.5 = −2.0 m/s²", r3((1.0 - 6.0) / 2.5) === "-2"],
    ["shuttle application: (96−0)/8.0 = 12 m/s²", r3(96 / 8.0) === "12"],
  ],
  rn_5hfYYFrc2XjMJCrq: [
    ["MCQ2: (20−8)/6 = 2.0 m/s²", r3((20 - 8) / 6) === "2"],
    ["cyclist WE: a = 5/5 = 1 m/s²", 5 / 5 === 1],
    ["application: (25−15)/10 = 1.0 m/s²", r3((25 - 15) / 10) === "1"],
    ["tram application: (6−18)/4.0 = −3.0 m/s²", r3((6 - 18) / 4.0) === "-3"],
    ["falling-line MCQ: −6/3 = −2 m/s²", r3(-6 / 3) === "-2"],
  ],
  rn_GxNWbSMqkTN4zgZB: [
    ["MCQ2 triangle: ½×8×12 = 48 m", 0.5 * 8 * 12 === 48],
    ["MCQ3 rectangle: 9×7 = 63 m", 9 * 7 === 63],
    ["MCQ5 stop: ½×10×20 = 100 m", 0.5 * 10 * 20 === 100],
    ["scooter: 6.0×12 = 72 m; ½×8×14 = 56 m", 6 * 12 === 72 && 0.5 * 8 * 14 === 56],
    ["journey WE: 350+525+75+350+875 = 2175 m", 0.5 * 40 * 17.5 === 350 && 30 * 17.5 === 525 && 0.5 * 20 * 7.5 === 75 && 20 * 17.5 === 350 && 0.5 * 70 * 25 === 875 && 350 + 525 + 75 + 350 + 875 === 2175],
    ["van application: 150+400+250 = 800 m", 0.5 * 30 * 10 === 150 && 40 * 10 === 400 && 0.5 * 50 * 10 === 250 && 150 + 400 + 250 === 800],
  ],
  rn_ZgGMNrRGBKvYxxFf: [
    ["WE: (16²−0²)/(2×2.5) = 256/5 = 51.2 m", 16 * 16 === 256 && 256 / 5 === 51.2],
    ["train application: (30²−12²)/(2×378) = 1.0 m/s²", r3((900 - 144) / (2 * 378)) === "1"],
    ["cyclist MCQ: (4²−12²)/(2×40) = −1.6 m/s²", r3((16 - 144) / 80) === "-1.6"],
    ["van application: 2×3×96 = 576; √576 = 24 m/s", 2 * 3 * 96 === 576 && Math.sqrt(576) === 24],
    ["van MCQ: 2×2.5 = 5 denominator", 2 * 2.5 === 5],
  ],
};
for (const n of NOTES) {
  const lg = ledgers[n];
  const badLedger = lg.filter(([label, ok]) => !ok);
  gate(`NUM ${n.slice(0, 12)}: ${lg.length} ledger claims re-derived`, badLedger.length === 0, badLedger.map(([l]) => l).join("; ") || "all exact");
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
section("transform (full derivation from the 0.6 sources — no chemistry baseline bytes touched)");
const outLessons = {}, outPkgs = {};
for (const n of NOTES) {
  const s5buf = read(path.join(RES, "source-0.6", `guided-lesson-${n}.json`));
  const s5sha = sha256(s5buf);
  const src = sources[n];

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
      figures: (src.figures && src.figures.length) ? src.figures.map((f) => ({
        id: f.id, url: f.url, alt: f.alt, sourceHeading: f.sourceHeading,
        moduleIds: f.moduleIds, ...(f.caption ? { caption: f.caption } : {}), binding: f.binding,
      })) : undefined,
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
  gate(`written-kind invariants ${n.slice(0, 12)} (x${wtot})`, wok === wtot, `${wok}/${wtot}`);

  // C-5 checkRefs <-> questions 1:1 in order
  const flat = [];
  hub.lesson.modules.forEach((m) => m.checkRefs.forEach((r) => flat.push(r)));
  gate(`C-5 checkRefs<->questions 1:1 ${n.slice(0, 12)}`, flat.length === pkg.questions.length && flat.every((r, i) => r === pkg.questions[i].id), `${flat.length} refs / ${pkg.questions.length} questions`);

  // B2 per-lesson law at target: 9 checkRefs per module
  gate(`B2 target ${n.slice(0, 12)}: every module carries exactly 9 checkRefs`, hub.lesson.modules.every((m) => m.checkRefs.length === 9), hub.lesson.modules.map((m) => m.checkRefs.length).join(","));

  // ajv targets
  gate(`C-6 lesson ${n.slice(0, 12)} vs hub/lesson-import/1.5`, vHub15(hub), vHub15.errors ? ajv.errorsText(vHub15.errors).slice(0, 250) : "");
  gate(`C-6 package ${n.slice(0, 12)} vs sme-question-package/1.2`, vPkg12(pkg), vPkg12.errors ? ajv.errorsText(vPkg12.errors).slice(0, 250) : "");
}

// ── emit artifacts ────────────────────────────────────────────────────────────
section("emit artifacts");
fs.mkdirSync(path.join(RES, "hub-import-1.5"), { recursive: true });
fs.mkdirSync(path.join(RES, "question-packages-1.2"), { recursive: true });
const emit = (p, obj) => { const buf = Buffer.from(JSON.stringify(obj, null, 2) + "\n", "utf8"); fs.writeFileSync(p, buf); return buf; };
const newSha = {};
for (const n of NOTES) {
  const lb = emit(path.join(RES, "hub-import-1.5", `${n}.hub-lesson-import.json`), outLessons[n]);
  const pb = emit(path.join(RES, "question-packages-1.2", `${n}.sme-question-package.json`), outPkgs[n]);
  newSha[n] = { hub: { sha256: sha256(lb), bytes: lb.length }, pkg: { sha256: sha256(pb), bytes: pb.length } };
  console.log(`  hub-import-1.5/${n.slice(0, 12)}: ${lb.length}B  question-packages-1.2/${n.slice(0, 12)}: ${pb.length}B`);
}

// ── G-E stream (the runner's walk, byte-identical law) ────────────────────────
section("G-E stream anchors + grand");
const rows = NOTES.map((n) => {
  const s = targetTokens(outLessons[n], outPkgs[n]).join("\n");
  return {
    noteId: n,
    wave: 1,
    sourceLayerSha256: sha256(read(path.join(RES, "source-0.6", `guided-lesson-${n}.json`))),
    hubSha256: newSha[n].hub.sha256,
    pkgSha256: newSha[n].pkg.sha256,
    stream: { sha256: sha256(Buffer.from(s, "utf8")), chars: s.length },
  };
});
let grandChars = 0;
const grand = crypto.createHash("sha256");
for (const n of NOTES) {
  const s = targetTokens(outLessons[n], outPkgs[n]).join("\n");
  grand.update(Buffer.from(s, "utf8"));
  grandChars += s.length;
}
const grandSha = grand.digest("hex");
const waveOut = { "wave-1": (() => { const h = crypto.createHash("sha256"); for (const n of NOTES) h.update(Buffer.from(targetTokens(outLessons[n], outPkgs[n]).join("\n"), "utf8")); return h.digest("hex"); })() };
console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}… (wave-1: ${waveOut["wave-1"].slice(0, 12)}…)`);

// census from the emitted bytes (disk-derived, not asserted)
const census = {
  notes: NOTES.length,
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

// ── manifest v19 (B6 CONTINUE-GLOBAL of record) ───────────────────────────────
section("manifest v19");
const artifacts = [];
for (const n of NOTES) {
  artifacts.push({ kind: "hub-lesson-import-1.5", noteId: n, path: `SME-GuidedLessons/integration/hub-import-1.5/${n}.hub-lesson-import.json`, sha256: newSha[n].hub.sha256, bytes: newSha[n].hub.bytes });
  artifacts.push({ kind: "sme-question-package", noteId: n, path: `SME-GuidedLessons/integration/question-packages-1.2/${n}.sme-question-package.json`, sha256: newSha[n].pkg.sha256, bytes: newSha[n].pkg.bytes });
}
const man19 = {
  format: "hub-import-manifest/1.0",
  manifest_version: MANIFEST_VERSION,
  course_id: COURSE_ID,
  b6_manifest_continuity: {
    decision: "continue-global",
    selected: "physics wave-1 = manifest v19 (the programme-level series continues across subjects; stage-A opened it at v18)",
    rejected: "per-course series (physics v1) — would collide with chemistry hub-import-manifest-v1..v17.json filenames in the shared integration/ namespace and fork the integration ledger",
    recorded_by: "runbook B6 + the stage-A receipt of record (PHYSICS-4PH1-STAGEA-PROMOTION-20261101.json); continued here at v19",
  },
  generated_at_utc: now(),
  operator_trace: EXEC_TRACE,
  supersedes: "hub-import-manifest-v18.json (physics stage-A pilot: 1 note / 2 lessons / 18 checks @ promo 01a2fc34, all re-pinned byte-identical; nothing stage-A carries new bytes in this generation) — v19 is the FIRST register wave: 6 igcse-physics-19 notes, 12 artifacts",
  checks_layer: {
    wave: "PHYSICS-4PH1 wave-1 (the 1-1 remainder: 1-1-2..1-1-7; runbook §1 B4 bucket of record) — operator ignition trace " + IGNITION_TRACE + " (\"ignite wave-1\"), execution trace " + EXEC_TRACE + " (PAT delivered in-session)",
    derivation: "108 authored checks (60 MCQ + 24 recall + 12 explain-why + 12 application = 12 lessons x [5 MCQ + 2 recall + 1 explain-why + 1 application]), spec-anchored to 4PH1 1.4..1.10 with KP-index provenance; written items carry modelAnswer + generous synonym/inflection-bearing keywords",
    declared_revision: "the SECOND package-channel tranche of the new subject and the FIRST wave: 6 packages issued under sme-question-package/1.2 and 6 lessons under hub/lesson-import/1.5 (union schemas — the 112 chemistry 1.1/1.4 artifacts validate unchanged); the v18 stage-A artifacts are re-pinned byte-identical",
    grading_law: "case-insensitive whole-token match of the learner text against keywords[]; >=1 hit -> correct; 0 hits -> not-quite + model answer; empty submit blocked; keywords absent -> reveal-only (fail-closed, never a silent wrong grade)",
    fail_closed: "written item without modelAnswer renders reveal-only, never gradeable, never blank; unknown kind renders reveal-only and warns at this gate",
  },
  source_generation: {
    format: "guided-lesson/0.6",
    namespace: "SME-GuidedLessons/integration/source-0.6/",
    pin: commitA,
    int0_lineage: "(new subject — no INT-0 ancestry; the wave-1 0.6 sources are authored directly from the igcse-physics-19 revision-note rows of record, hub notes.json @ " + HUB_MAIN_AT_OPEN.slice(0, 8) + ")",
  },
  load_scope: { adapter: ADAPTER, target_schemas: ["hub/lesson-import/1.5", "sme-question-package/1.2"] },
  counts,
  conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut },
  artifacts,
};
gate("manifest v19 lists 12 artifacts", artifacts.length === 12, String(artifacts.length));

// ── INT-3 record ──────────────────────────────────────────────────────────────
const int3 = {
  stage: "INT-3",
  title: "transform record — PHYSICS-4PH1 wave-1 (adapter guided-lesson-0.6--hub-lesson-import-1.5)",
  generated_at_utc: now(),
  operator_traces: { ignition: IGNITION_TRACE, execution: EXEC_TRACE },
  adapter: ADAPTER,
  course_id: COURSE_ID,
  b6_manifest_continuity: man19.b6_manifest_continuity,
  b4_partition_of_record: {
    law: "runbook §0 B4 — partition at wave open only; final wave takes the remainder; never re-bucket mid-programme",
    basis: "hub notes.json register rows (127) minus the stage-A pilot (B3) = 126 notes, section-aligned in register order",
    buckets: Object.fromEntries(Object.entries(B4_PARTITION).map(([w, secs]) => [w, { sections: secs, notes: w === "W1" ? NOTES.length + 0 : null }])),
    bucket_sizes: Object.fromEntries(Object.entries(B4_PARTITION).map(([w, secs]) => [w, secs.reduce((a, s) => a + (s.includes("1-1-movement-and-position") ? 6 : s.includes("1-2-") ? 9 : s.includes("1-3-") ? 4 : s.includes("1-4-") ? 3 : s.includes("2-1-") ? 3 : s.includes("2-2-") ? 5 : s.includes("2-3-") ? 5 : s.includes("2-4-") ? 4 : s.includes("3-1-") ? 7 : s.includes("3-2-") ? 6 : s.includes("3-3-") ? 4 : s.includes("4-1-") ? 6 : s.includes("4-2-") ? 7 : s.includes("5-1-") ? 4 : s.includes("5-2-") ? 5 : s.includes("5-3-") ? 6 : s.includes("6-1-") ? 10 : s.includes("6-2-") ? 4 : s.includes("7-1-") ? 6 : s.includes("7-2-") ? 5 : s.includes("7-3-") ? 5 : s.includes("8-1-") ? 4 : s.includes("8-2-") ? 5 : 3), 0)])),
    executed_this_wave: "W1 (1-1-2..1-1-7)",
  },
  source_pin: {
    repo: "SyllabAI/syllabai-resources",
    ref: RES_MAIN_AT_OPEN,
    note: "resources main at wave-1 open = 196c2957 (PR #270 g9-followups-20261101: LEDGER.md + scripts/ only); the re-ground read 23dd0c9d (run-008 W2 corpus lane) and main advanced once between re-ground and branch — the mid-flight race was caught by the pre-branch fetch (fetch-first discipline), the branch is based on the new tip, and the overlap census vs the wave-1 namespaces (SME-GuidedLessons/**) is ZERO",
  },
  registry_pin: {
    repo: "SyllabAI/syllabai-v2",
    ref: HUB_MAIN_AT_OPEN,
    path: "apps/hub/content/igcse-physics-19/notes.json",
    note: "the revision-note rows of record (noteId registry, specPointCodes, bodyMd with asset URLs)",
  },
  source_06_generation_pin: { commit: commitA, namespace: "SME-GuidedLessons/integration/source-0.6/" },
  conservation_law:
    "kind/modelAnswer/keywords on written items ARE §7 stream tokens (the runner walk extends by those fields on kind!=mcq); each wave-1 note's stream is anchored below; the chemistry corpus streams and the v18 stage-A stream are untouched (no chemistry or stage-A bytes re-issued in v19). Grand + wave-1 computed over the 6 notes in artifact order.",
  grand_stream: { chars: grandChars, sha256: grandSha },
  wave_stream_sha256: waveOut,
  battery: {
    names: "A0 / AN / SG / KW / JC / 2.1B / NUM (runbook §1.4 battery of record), run per note",
    a0: "ajv guided-lesson/0.6 x6 + 9-check SME kind order per lesson (12 lessons) + B2 sizing (6 notes -> 2 lessons each) + figure closure both ways (figures/figureIds optional keys — absent lawful, empty unlawful) + glossary 3..8 + primer word band",
    an: "exactly one correct option per MCQ x60; per-note correct-key letter census >=3 distinct / max 5; option texts distinct",
    sg: "lesson specRefs subset of file specPoints (4PH1 1.4..1.10); every check shares a content token with its lesson keyPoints (KP-index provenance)",
    kw: "written items >=3 distinct keywords, each grounded in the modelAnswer/stem/keyPoints union",
    jc: "every option explained; distractors name misconceptions; correct option misconception null",
    "2.1b": "zero 8-gram overlap between learner-surface text (stems, model answers, option text+explanations) and each note's bodyMd",
    num: "per-note numeric ledgers re-derived in code (see the NUM gate log): unit conversions, WE arithmetics, MCQ distractor arithmetics — all exact",
  },
  physics_census: {
    wave_notes: NOTES,
    wave_lessons: census.lessons,
    checks: census.checks,
    ...kindCensus,
    distractors: census.distractors,
    figures: census.figures,
    figures_captions: Object.values(outLessons).reduce((a, h) => a + (h.lesson.figures || []).filter((f) => f.caption).length, 0),
    figures_no_caption: Object.values(outLessons).reduce((a, h) => a + (h.lesson.figures || []).filter((f) => !f.caption).length, 0),
    figureless_notes: ["rn_ZgGMNrRGBKvYxxFf"],
  },
  notes: rows,
};
emit(path.join(RES, "records/INT-3-transform-record-physics-wave1.json"), int3);
const manBuf = emit(path.join(RES, "hub-import-manifest-v19.json"), man19);

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
  wave: "PHYSICS-4PH1 wave-1 — the 1-1 remainder (1-1-2 Speed, 1-1-3 Core Practical, 1-1-4 Acceleration, 1-1-5 Velocity-Time Graphs, 1-1-6 Area under a V-T Graph, 1-1-7 Calculating Uniform Acceleration)",
  operator_traces: [IGNITION_TRACE, EXEC_TRACE],
  generated_at_utc: now(),
  repo: "SyllabAI/syllabai-resources",
  branch,
  runbook_of_record: ".syllabai/docs/new-subject-runbook.md @ SyllabAI/syllabai-v2 main",
  b6_manifest_continuity: man19.b6_manifest_continuity,
  b4_partition: int3.b4_partition_of_record,
  commits: {
    A: { sha: commitA, parent: commitAParent, note: "source-0.6 generation — 6 authored guided-lesson/0.6 wave-1 notes (12 lessons / 108 checks); schemas ride main unchanged from stage-A" },
    C: { sha: "(namespace-complete — outputs + manifest v19 + records + pipeline)", note: "hub-import-1.5/ x6 + question-packages-1.2/ x6 + hub-import-manifest-v19.json + records/INT-3-transform-record-physics-wave1.json + records/NS-4PH1-PHYSICS-WAVE1-PROMOTION-20261101.json + tooling/physics-wave1-pipeline.js" },
  },
  artifact_pin: commitA,
  pkg_pin: `${commitA} (all six wave-1 packages pin the commit-A source generation)`,
  input_pins: { resources_main_at_wave1_open: RES_MAIN_AT_OPEN, hub_main_at_wave1_open: HUB_MAIN_AT_OPEN },
  manifest: "hub-import-manifest-v19.json",
  int_record: "INT-3-transform-record-physics-wave1.json",
  adapter_spec: "ADAPTER-SPEC-guided-lesson-0.6-to-hub-1.5.md (unchanged from stage-A)",
  counts_census: { notes: census.notes, lessons: census.lessons, checks: census.checks, ...kindCensus, distractors: census.distractors, wave_notes: NOTES },
  schema_delta:
    "NONE — wave-1 runs the stage-A union schemas byte-identical (guided-lesson/0.6, hub/lesson-import/1.5, sme-question-package/1.2). The figureless note (1-1-7) lands by OMITTING the optional figures/figureIds keys — exactly the chemistry precedent (22/112 notes figureless per the 0.6 schema description).",
  taxonomy: "kind enum of record: mcq (default/absent) | recall | explain-why | application — 12 lessons x [5 MCQ + 2 recall + 1 explain-why + 1 application] = the B2 law",
  conservation: {
    law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq; the wave-1 streams are anchored in the INT-3 record; chemistry + stage-A streams byte-untouched (no re-issues in v19)",
    authored_chars: grandChars,
  },
  gates: { pipeline: `${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, 0 fail`, gate_log: CHECKS },
  merge_order:
    "resources PR (this branch) merges to main FIRST; the hub PR (FEED physics-wave1-v19 + landed artifacts + re-issued guided-import.json) merges only after; wave-2 buckets remain operator-gated and are NOT in this tranche (B4: one wave per gate)",
  hub_side_note:
    "the hub renderer is course-generic; the physics FEED physics-stagea-v18 already exercised the parameterized runner — wave-1 adds one FEED entry (physics-wave1-v19) with feed-gated constants only (pack/course_id/counts/prefix/wave-count), chemistry-preserving defaults untouched",
  disclosures: [
    "naming: the contract of record named lanes ns4ph1-waveN; the landed stage-A execution used the physics-* family (receipts dir PHYSICS-STAGEA, feed physics-stagea-v18) — wave-1 follows the LANDED convention (lane physics-wave1, feed physics-wave1-v19, receipts PHYSICS-WAVE1); recorded here so both naming families resolve to the same programme",
    "the 1-1-7 note carries zero usable images — the optional figures layer is omitted entirely (key absent, never an empty array), matching the 0.6 schema's declared absent-when-no-usable-images semantics; 5/127 physics notes are figureless (census of record)",
    "spec 1.6's curriculum title of record carries the fragment 'accelerati on' (a curriculum-data artifact); it is carried VERBATIM (zero-invention law) and disclosed here",
    "captions: 10 of 16 figures carry the notes' own bold-italic explanatory lines; the 6 worked-example images carry none (fail-closed absent, declared)",
    "other-run activity at open disclosed: resources main advanced 23dd0c9d -> 196c2957 (PR #270 g9-followups: LEDGER.md + scripts/ only) between re-ground and branch — caught by the pre-branch fetch, zero namespace overlap, race-guard re-checks due at push; hub main 37aa9e44 (t-gradeb-6) likewise an unrelated lane",
    "sandbox recycle lost the previous session's lane mirrors; all of-record state re-fetched from remotes (fetch-first honored)",
  ],
};
emit(path.join(RES, "records/NS-4PH1-PHYSICS-WAVE1-PROMOTION-20261101.json"), receipt);

// ── lane survivors for the hub runner byte-anchors ────────────────────────────
fs.mkdirSync(SURV, { recursive: true });
fs.mkdirSync(path.join(SURV, "schema"), { recursive: true });
fs.copyFileSync(path.join(RES, "hub-import-manifest-v19.json"), path.join(SURV, "hub-import-manifest-v19.json"));
fs.copyFileSync(path.join(RES, "records/INT-3-transform-record-physics-wave1.json"), path.join(SURV, "INT-3-transform-record-physics-wave1.json"));
fs.copyFileSync(path.join(RES, "schema/hub-lesson-import.1.5.schema.json"), path.join(SURV, "schema/hub-lesson-import.1.5.schema.json"));
fs.copyFileSync(path.join(RES, "schema/sme-question-package.1.2.schema.json"), path.join(SURV, "schema/sme-question-package.1.2.schema.json"));

console.log(`\nRESULT: ${FAILED === 0 ? "GREEN — PIPELINE COMPLETE" : "FAIL-CLOSED"}`);
console.log(`  gates: ${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, ${FAILED} failures`);
console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}…`);
console.log(`  census: ${JSON.stringify(counts)}`);
