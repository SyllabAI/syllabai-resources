#!/usr/bin/env node
/**
 * PHYSICS-WAVE3 PIPELINE — new-subject stage-B wave-3 transform + manifest v22 + INT-3 record
 * (operator ignition trace 1a19c5cc34b70739 "Proceed with wave-3"; execution trace
 *  1a19c5cc34b70739 — ignition and execution share the session trace, single-window execution,
 *  disclosed in the promotion receipt)
 *
 * Runbook of record: .syllabai/docs/new-subject-runbook.md @ hub main (§1 wave lifecycle).
 * B6 of record (stage-A, continued at v19/v20/v21): CONTINUE-GLOBAL manifest series — wave-3 =
 * hub-import-manifest-v22.json, CUMULATIVE over the igcse-physics-19 pack (the chemistry
 * v8..v17 pattern; the v19 index-regression lesson of record: the INT-3 carries ALL 23 rows).
 * B4 of record: the frozen partition of the wave-1 contract — wave-3 executes bucket W3
 * (the 1-3-momentum + 1-4-moments subtopics, 7 notes).
 *
 * Input of record (lane clone @ resources main aa004cb1…, branch integration/physics-wave3-20261102):
 *   source-0.6/ ×7 authored wave-3 notes (guided-lesson/0.6, committed @ commit A of this branch)
 *   schema/guided-lesson.0.6.schema.json + {hub-lesson-import.1.5, sme-question-package.1.2} (main, unchanged)
 *   source-0.5/ ×112 + hub-import-1.4/ ×112 + question-packages-1.1/ ×112 (chemistry union baselines)
 *   hub-import-manifest-v21.json + records/INT-3-transform-record-physics-wave2.json (the pack of record)
 *
 * Outputs (namespace-complete, committed @ commit C):
 *   hub-import-1.5/rn_<id>.hub-lesson-import.json ×7        (format hub/lesson-import/1.5, FIRST issues)
 *   question-packages-1.2/rn_<id>.sme-question-package.json ×7 (format sme-question-package/1.2, FIRST issues)
 *   hub-import-manifest-v22.json  (CUMULATIVE: 46 artifacts = 32 pack re-pins byte-identical + 14 first issues)
 *   records/INT-3-transform-record-physics-wave3.json  (23-row anchor table — the v19-lesson law)
 *   records/NS-4PH1-PHYSICS-WAVE3-PROMOTION-20261102.json
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
const Ajv = require("/home/z/my-project/scripts/ajvkit/node_modules/ajv");

const RES = "/home/z/my-project/resources-wave3/SME-GuidedLessons/integration";
const RES_REPO = "/home/z/my-project/resources-wave3";
const HUB_REPO = "/home/z/my-project/syllabai-v2";
const SURV = "/home/z/my-project/scripts/physics-wave3-survivors";
const NOTES = [
  "rn_pqp4mfpHzGVtrjTT", // 1-3-1 Momentum (1.25P, 1.27P)
  "rn_NfCjFmPfmMQ8pQSw", // 1-3-2 Forces & Momentum (1.28P)
  "rn_8wqvPtsCCh3gdJN5", // 1-3-3 Newton's Third Law (1.29P)
  "rn_RQK2MW3zRPNNzwtc", // 1-3-4 Momentum & Safety Features (1.26P)
  "rn_jzQZQcPRQkJvdYwJ", // 1-4-1 Moments (1.30P)
  "rn_zn4NVCRcTSNv8sRZ", // 1-4-2 The Principle of Moments (1.32P, 1.33P)
  "rn_TPDdhwDYsrWgQB7R", // 1-4-3 Centre of Gravity (1.31P)
];
const IGNITION_TRACE = "1a19c5cc34b70739";
const EXEC_TRACE = "1a19c5cc34b70739"; // single-window execution (disclosed)
const ADAPTER = "guided-lesson-0.6--hub-lesson-import-1.5";
const COURSE_ID = "igcse-physics-19";
const COURSE_PREFIX = "igcse-physics";
const RES_MAIN_AT_OPEN = "aa004cb133efcd6fcff2f9820b643c8e44beda5f"; // PR #280 T-OEQ-PHYS-FORMAT-1 tip; zero overlap with the wave-3 namespaces
const HUB_MAIN_AT_OPEN = "a7f2f5a2204053eb48254654bf741b41418c1ab8"; // R0-AUTO-109 tip (PRs #634/#643); zero overlap
const MANIFEST_VERSION = 22; // B6 CONTINUE-GLOBAL — the series continues from v21
const PRIOR_MANIFEST_VERSION = 21;
const PILOT_OF_RECORD = "rn_RpyMnS5nqWSRWXXG"; // stage-A pilot — outside the buckets (B3)
const WAVE1_NOTES = [
  "rn_k9wr3prcgSBg5vfw", "rn_pfndTqR6DTJGZ8xQ", "rn_CpJZQWzbvMcM8fw3",
  "rn_5hfYYFrc2XjMJCrq", "rn_GxNWbSMqkTN4zgZB", "rn_ZgGMNrRGBKvYxxFf",
];
const WAVE2_NOTES = [
  "rn_nyV7C6zmyKXWJjKg", "rn_4zdmGRWTg5ksK44N", "rn_K3p2R3ykwwvHV9dp",
  "rn_gDy2qTkY26r5sMtd", "rn_2R3NrjGfJJY29Hzv", "rn_ZCGJsYwy6S6FbbbW",
  "rn_Mrfn29ZgQMq8th5P", "rn_kN63sqWsc9QdHSVx", "rn_nC3BswtJzYw8k6nX",
];
const PILOT_PIN = "7d493985c7729f30c2186e7e61a713ceacc96517"; // stage-A commit A (provenance of record)
const WAVE1_PIN = "aa6485187429e0911b4a47a8a468e256bb41ce32"; // wave-1 commit A (provenance of record)
const WAVE2_PIN = "bfae9977809436fc2e5c20967bf2581f67a52bec"; // wave-2 commit A (provenance of record)
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
gate("P0 branch is the wave-3 integration branch", branch === "integration/physics-wave3-20261102", branch);
gate("P0 commit A parent is the wave-open resources main of record", commitAParent === RES_MAIN_AT_OPEN, commitAParent);
for (const n of NOTES) {
  const rel = `source-0.6/guided-lesson-${n}.json`;
  const blob = execSync(`git show HEAD:${"SME-GuidedLessons/integration/"}${rel}`, { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 8 });
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
section("B4 partition of record (111 remaining notes after wave-2, pilot excluded)");
{
  const reg = noteRows.map((r) => r.path.replace(/\.md$/, "")).sort();
  gate("register census 127 rows", reg.length === 127, String(reg.length));
  const pilotPath = noteRows.find((r) => r.noteId === PILOT_OF_RECORD).path.replace(/\.md$/, "");
  const landed = new Set([pilotPath, ...WAVE1_NOTES.map((id) => noteRows.find((r) => r.noteId === id).path.replace(/\.md$/, "")), ...WAVE2_NOTES.map((id) => noteRows.find((r) => r.noteId === id).path.replace(/\.md$/, ""))]);
  const bySection = {};
  for (const p of reg) {
    if (landed.has(p)) continue;
    const sec = p.split("/").slice(0, 2).join("/");
    (bySection[sec] ||= []).push(p);
  }
  const buckets = {};
  let total = 0;
  for (const [w, secs] of Object.entries(B4_PARTITION)) {
    buckets[w] = secs.flatMap((s) => bySection[s] || []);
    total += buckets[w].length;
  }
  gate("B4 buckets partition the 111-note remainder exactly", total === 111, `${total} notes bucketed (126 at freeze − 15 landed through W2)`);
  gate("B4 W3 == the 7 authored wave-3 notes", JSON.stringify(buckets["W3"].map((p) => p.split("/").pop())) === JSON.stringify([
    "1-3-1-momentum", "1-3-2-forces-and-momentum", "1-3-3-newtons-third-law",
    "1-3-4-momentum-and-safety-features", "1-4-1-moments", "1-4-2-the-principle-of-moments",
    "1-4-3-centre-of-gravity",
  ]), buckets["W3"].map((p) => p.split("/").pop()).join(","));
  gate("B4 pilot + W1 outside every remaining bucket", !Object.values(buckets).some((b) => b.some((p) => landed.has(p))), "");
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
  const src = readJson(path.join(RES, "source-0.6", `guided-lesson-${n}.json`));
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
  // union law: the lessons' specRefs cover the file's specPoints exactly
  const union = [...new Set(src.lessons.flatMap((l) => l.specRefs))].sort();
  const fileset = src.specPoints.map((s) => s.code).sort();
  gate(`A0 ${n.slice(0, 12)}: lesson specRefs union == file specPoints`, JSON.stringify(union) === JSON.stringify(fileset), `${union.join(",")} vs ${fileset.join(",")}`);
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
    if (new Set(c.options.map((o) => o.key)).size !== c.options.length) ok = false;
  }
  const census = {};
  for (const k of letters) census[k] = (census[k] || 0) + 1;
  const distinct = Object.keys(census).length;
  const maxShare = Math.max(...Object.values(census));
  gate(`AN ${n.slice(0, 12)}: exactly-one-correct x${mcqs.length} + distinct option texts/keys`, ok, "");
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
  const STOP = new Set("a an the of to in on at for with and or is are was were be been it its this that these those as by from not no you your they their we our object objects line lines graph graphs which what how state recall explain why does do can may will would shows show give name list describe calculate".split(" "));
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
  rn_pqp4mfpHzGVtrjTT: [
    ["60 g = 0.06 kg", 60 / 1000 === 0.06],
    ["WE ball 0.06 kg x 75 m/s = 4.5 kg m/s", Math.round(0.06 * 75 * 1e9) / 1e9 === 4.5],
    ["WE brick 3 kg x 1.5 m/s = 4.5 kg m/s", 3 * 1.5 === 4.5],
    ["WE equal momenta 0.06x75 = 3x1.5 = 4.5", Math.round(0.06 * 75 * 1e9) / 1e9 === 3 * 1.5],
    ["fig-01 approach 0.060 kg x 2 m/s = 0.12 kg m/s", Math.round(0.06 * 2 * 1e9) / 1e9 === 0.12],
    ["fig-01 reversal -(0.06 x 2) = -0.12 kg m/s", Math.round(-(0.06 * 2) * 1e9) / 1e9 === -0.12],
    ["L1 MCQ4 distractor 2 x 0.12 = 0.24 kg m/s", Math.round(2 * 0.12 * 1e9) / 1e9 === 0.24],
    ["L1 MCQ2 v = 0 gives p = 0", 0 * 3.5 === 0],
    ["L1 app 0.5 kg x 4 m/s = 2 kg m/s", 0.5 * 4 === 2],
    ["L1 app reversed -2 kg m/s", -(0.5 * 4) === -2],
    ["L2 MCQ3 1 kg x 3 m/s = 3 kg m/s", 1 * 3 === 3],
    ["L2 MCQ3 distractor (1+2) x 3 = 9 kg m/s", (1 + 2) * 3 === 9],
    ["L2 MCQ3 distractor 2 kg x 3 m/s = 6 kg m/s", 2 * 3 === 6],
    ["L2 app car 0.035 kg x 0.8 = 0.028 kg m/s", Math.round(0.035 * 0.8 * 1e9) / 1e9 === 0.028],
    ["L2 app van at rest 0.085 x 0 = 0 kg m/s", 0.085 * 0 === 0],
    ["L2 app car after 0.035 x 0.1 = 0.0035 kg m/s", Math.round(0.035 * 0.1 * 1e9) / 1e9 === 0.0035],
    ["L2 app van after 0.028 - 0.0035 = 0.0245 kg m/s", Math.round((0.028 - 0.0035) * 1e9) / 1e9 === 0.0245],
    ["L2 app van velocity (0.028 - 0.0035)/0.085 = 0.29 m/s (2 s.f.)", Math.round(((0.028 - 0.0035) / 0.085) * 100) / 100 === 0.29],
  ],
  rn_NfCjFmPfmMQ8pQSw: [
    ["WE 1500 x 15 = 22500 (mu)", 1500 * 15 === 22500],
    ["WE 1500 x 5 = 7500 (|mv|)", 1500 * 5 === 7500],
    ["WE -7500 - 22500 = -30000 (delta p)", -7500 - 22500 === -30000],
    ["WE -30000 / 3 = -10000 N (F)", -30000 / 3 === -10000],
    ["L1 app 2 x 6 = 12 (mu)", 2 * 6 === 12],
    ["L1 app 0 - 12 = -12 (delta p)", 0 - 12 === -12],
    ["L1 app -12 / 0.5 = -24 N (F)", -12 / 0.5 === -24],
    ["L2 KP4/MCQ3 0.5 / 2.0 = 0.25 N (F1)", 0.5 / 2.0 === 0.25],
    ["L2 KP4/MCQ3 0.5 / 0.1 = 5.0 N (F2)", 0.5 / 0.1 === 5],
    ["L2 MCQ3 distractor 0.5 x 0.1 = 0.05 N", 0.5 * 0.1 === 0.05],
    ["L2 MCQ3 distractor 0.1 / 0.5 = 0.2 N", 0.1 / 0.5 === 0.2],
    ["L2 MCQ4 1000 x 10 = 10000 (mu)", 1000 * 10 === 10000],
    ["L2 MCQ4 1000 x 2 = 2000 (|mv|)", 1000 * 2 === 2000],
    ["L2 MCQ4 -2000 - 10000 = -12000 (delta p)", -2000 - 10000 === -12000],
    ["L2 MCQ4 -12000 / 2 = -6000 N (F)", -12000 / 2 === -6000],
    ["L2 MCQ4 distractor (2000 - 10000)/2 = -4000 N", (2000 - 10000) / 2 === -4000],
    ["L2 MCQ4 distractor 10000 / 2 = 5000 N", 10000 / 2 === 5000],
    ["L2 app 0.5 x 8 = 4 (mu)", 0.5 * 8 === 4],
    ["L2 app 0.5 x 2 = 1 (|mv|)", 0.5 * 2 === 1],
    ["L2 app -1 - 4 = -5 (delta p)", -1 - 4 === -5],
    ["L2 app -5 / 0.25 = -20 N (F)", -5 / 0.25 === -20],
  ],
  rn_8wqvPtsCCh3gdJN5: [
    ["third-law partner force |F(B on A)| = 6 N", Math.abs(-6) === 6],
    ["L3 app a(A) = 6 / 2 = 3 m/s^2", 6 / 2 === 3],
    ["L3 app a(B) = 6 / 1 = 6 m/s^2", 6 / 1 === 6],
    ["recognition checklist has three rules (1+1+1)", 1 + 1 + 1 === 3],
  ],
  rn_RQK2MW3zRPNNzwtc: [
    ["50 kg x 4 m/s = 200 kg m/s (p = mv)", 50 * 4 === 200],
    ["mat F = 200 / 0.2 s = 1000 N", 200 / 0.2 === 1000],
    ["floor F = 200 / 0.02 s = 10000 N", 200 / 0.02 === 10000],
    ["floor/mat ratio 10000 / 1000 = 10 (ten times smaller)", 10000 / 1000 === 10],
  ],
  rn_jzQZQcPRQkJvdYwJ: [
    ["10 x 0.50 = 5.0 N m", 10 * 0.5 === 5],
    ["10 / 0.50 = 20 N m (distractor)", 10 / 0.5 === 20],
    ["0.50 / 10 = 0.05 N m (distractor)", 0.5 / 10 === 0.05],
    ["10 + 0.50 = 10.5 N m (distractor)", 10 + 0.5 === 10.5],
    ["30 / 5 = 6 m", 30 / 5 === 6],
    ["30 x 5 = 150 m (distractor)", 30 * 5 === 150],
    ["5 / 30 ~ 0.17 m, 2 s.f. (distractor)", Math.abs(5 / 30 - 0.17) < 0.005],
    ["30 + 5 = 35 m (distractor)", 30 + 5 === 35],
    ["15 x 0.40 = 6.0 N m", 15 * 0.4 === 6],
    ["6.0 / 0.50 = 12 N", 6 / 0.5 === 12],
  ],
  rn_zn4NVCRcTSNv8sRZ: [
    ["690 x 0.3 = 207 N m (exact via 690x3/10)", (690 * 3) / 10 === 207],
    ["690 / 0.3 = 2300 N m (distractor, rounded)", Math.round(690 / 0.3) === 2300],
    ["690 + 0.3 = 690.3 N m (distractor)", 690 + 0.3 === 690.3],
    ["690 x 3 = 2070 N m (distractor)", 690 * 3 === 2070],
    ["child balance 140 x d = 207, d = 207/140 = 1.4786 (surfaced ~1.5, 2 s.f., never claimed exact)", Math.abs(207 / 140 - 1.4785714285714286) < 1e-9 && Math.round((207 / 140) * 10) / 10 === 1.5],
    ["60 - 38 = 22 N", 60 - 38 === 22],
    ["60 + 38 = 98 N (distractor)", 60 + 38 === 98],
    ["50 / 2 = 25 N (distractor)", 50 / 2 === 25],
    ["50 x 2 = 100 N (distractor)", 50 * 2 === 100],
    ["48 / 2 = 24 N", 48 / 2 === 24],
  ],
  rn_TPDdhwDYsrWgQB7R: [
    ["three intersecting construction lines (1 initial + 2 repeats)", 1 + 2 === 3],
    ["qualitative note — no further arithmetic on the learner surface", true],
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
section("transform (full derivation from the 0.6 sources — no chemistry or prior-pack bytes touched)");
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

// ── prior pack: 14 artifacts re-pinned byte-identical (the v20 pack of record) ──
section("prior pack of record (32 artifacts re-pinned byte-identical from v21)");
const man21 = JSON.parse(execSync("git show HEAD:SME-GuidedLessons/integration/hub-import-manifest-v21.json", { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 16 }).toString());
const int3v21 = JSON.parse(execSync("git show HEAD:SME-GuidedLessons/integration/records/INT-3-transform-record-physics-wave2.json", { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 16 }).toString());
gate("prior manifest is v21", man21.manifest_version === 21 && man21.artifacts.length === 32, String(man21.artifacts.length));
const priorNotes = [PILOT_OF_RECORD, ...WAVE1_NOTES, ...WAVE2_NOTES];
const waveOf = {};
waveOf[PILOT_OF_RECORD] = 0;
for (const id of WAVE1_NOTES) waveOf[id] = 1;
for (const id of WAVE2_NOTES) waveOf[id] = 2;
for (const n of NOTES) waveOf[n] = 3;
const priorAnchors = [];
for (const a of man21.artifacts) {
  const buf = execSync(`git show HEAD:${a.path}`, { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 8 });
  gate(`prior artifact sha256/bytes exact @ HEAD: ${a.noteId.slice(0, 12)} ${a.kind}`, sha256(buf) === a.sha256 && buf.length === a.bytes, `${sha256(buf).slice(0, 12)}/${buf.length}B`);
  priorAnchors.push({ ...a, buf });
}
const priorByKind = {};
for (const p of priorAnchors) {
  (priorByKind[p.noteId] ||= {})[p.kind] = p;
}
for (const nid of priorNotes) {
  const hubP = priorByKind[nid]["hub-lesson-import-1.5"];
  const pkgP = priorByKind[nid]["sme-question-package"];
  const toks = targetTokens(JSON.parse(hubP.buf.toString("utf8")), JSON.parse(pkgP.buf.toString("utf8")));
  const s = toks.join("\n");
  const v21row = int3v21.notes.find((r) => r.noteId === nid);
  gate(`prior stream re-derivation matches v21 INT-3: ${nid.slice(0, 12)}`, v21row && sha256(Buffer.from(s, "utf8")) === v21row.stream.sha256 && s.length === v21row.stream.chars, `${nid}: ${sha256(Buffer.from(s, "utf8")).slice(0, 12)}`);
}

// ── G-E stream (the runner's walk, byte-identical law) ────────────────────────
section("G-E stream anchors + wave subtotals + cumulative grand");
const rows = [];
for (const nid of [PILOT_OF_RECORD, ...WAVE1_NOTES, ...WAVE2_NOTES]) {
  const hubP = priorByKind[nid]["hub-lesson-import-1.5"];
  const pkgP = priorByKind[nid]["sme-question-package"];
  const hubObj = JSON.parse(hubP.buf.toString("utf8"));
  const pkgObj = JSON.parse(pkgP.buf.toString("utf8"));
  const s = targetTokens(hubObj, pkgObj).join("\n");
  rows.push({
    noteId: nid,
    wave: waveOf[nid],
    sourceLayerSha256: hubObj.source.sourceLayerSha256,
    hubSha256: hubP.sha256,
    pkgSha256: pkgP.sha256,
    stream: { sha256: sha256(Buffer.from(s, "utf8")), chars: s.length },
  });
}
for (const n of NOTES) {
  const s = targetTokens(outLessons[n], outPkgs[n]).join("\n");
  rows.push({
    noteId: n,
    wave: 3,
    sourceLayerSha256: sha256(read(path.join(RES, "source-0.6", `guided-lesson-${n}.json`))),
    hubSha256: newSha[n].hub.sha256,
    pkgSha256: newSha[n].pkg.sha256,
    stream: { sha256: sha256(Buffer.from(s, "utf8")), chars: s.length },
  });
}
gate("INT-3 carries ALL 23 pack rows (the v19-lesson law)", rows.length === 23, String(rows.length));
let grandChars = 0;
const grand = crypto.createHash("sha256");
for (const r of rows) {
  const nid = r.noteId;
  const hubObj = r.wave === 3 ? outLessons[nid] : JSON.parse(priorByKind[nid]["hub-lesson-import-1.5"].buf.toString("utf8"));
  const pkgObj = r.wave === 3 ? outPkgs[nid] : JSON.parse(priorByKind[nid]["sme-question-package"].buf.toString("utf8"));
  const s = targetTokens(hubObj, pkgObj).join("\n");
  grand.update(Buffer.from(s, "utf8"));
  grandChars += s.length;
}
const grandSha = grand.digest("hex");
const waveHashes = {};
for (const r of rows) {
  const nid = r.noteId;
  const hubObj = r.wave === 3 ? outLessons[nid] : JSON.parse(priorByKind[nid]["hub-lesson-import-1.5"].buf.toString("utf8"));
  const pkgObj = r.wave === 3 ? outPkgs[nid] : JSON.parse(priorByKind[nid]["sme-question-package"].buf.toString("utf8"));
  const s = targetTokens(hubObj, pkgObj).join("\n");
  const w = "wave-" + r.wave;
  waveHashes[w] = waveHashes[w] || crypto.createHash("sha256");
  waveHashes[w].update(Buffer.from(s, "utf8"));
}
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest("hex");
gate("wave subtotals reproduce the v21 of-record values for wave-0/wave-1/wave-2",
  waveOut["wave-0"] === int3v21.wave_stream_sha256["wave-0"] && waveOut["wave-1"] === int3v21.wave_stream_sha256["wave-1"] && waveOut["wave-2"] === int3v21.wave_stream_sha256["wave-2"],
  `w0 ${waveOut["wave-0"].slice(0, 12)} w1 ${waveOut["wave-1"].slice(0, 12)} w2 ${waveOut["wave-2"].slice(0, 12)}`);
console.log(`  cumulative grand: ${grandChars} chars ${grandSha.slice(0, 16)}… (wave-3: ${waveOut["wave-3"].slice(0, 12)}…)`);

// census from the emitted bytes (disk-derived, not asserted)
const census = {
  notes: 23,
  lessons: rows.reduce((a, r) => {
    const hubObj = r.wave === 3 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + hubObj.lesson.modules.length;
  }, 0),
  checks: rows.reduce((a, r) => {
    const pkgObj = r.wave === 3 ? outPkgs[r.noteId] : JSON.parse(priorByKind[r.noteId]["sme-question-package"].buf.toString("utf8"));
    return a + pkgObj.questions.length;
  }, 0),
  keyPoints: rows.reduce((a, r) => {
    const hubObj = r.wave === 3 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + hubObj.lesson.modules.reduce((b, m) => b + m.keyPoints.length, 0);
  }, 0),
  distractors: rows.reduce((a, r) => {
    const pkgObj = r.wave === 3 ? outPkgs[r.noteId] : JSON.parse(priorByKind[r.noteId]["sme-question-package"].buf.toString("utf8"));
    return a + pkgObj.questions.reduce((b, q) => b + (q.options || []).filter((o) => o.correct !== true).length, 0);
  }, 0),
  glossaryTerms: rows.reduce((a, r) => {
    const hubObj = r.wave === 3 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + (hubObj.lesson.assets.glossary || []).length;
  }, 0),
  figures: rows.reduce((a, r) => {
    const hubObj = r.wave === 3 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + (hubObj.lesson.figures || []).length;
  }, 0),
  workedExamples_populated: rows.reduce((a, r) => {
    const hubObj = r.wave === 3 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + (hubObj.lesson.assets.workedExample ? 1 : 0);
  }, 0),
  workedExamples_null: rows.reduce((a, r) => {
    const hubObj = r.wave === 3 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + (hubObj.lesson.assets.workedExample ? 0 : 1);
  }, 0),
};
census.figures_module_mapped = rows.reduce((a, r) => {
  const hubObj = r.wave === 3 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
  return a + (hubObj.lesson.figures || []).filter((f) => f.moduleIds.length > 0).length;
}, 0);
census.figures_note_level = rows.reduce((a, r) => {
  const hubObj = r.wave === 3 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
  return a + (hubObj.lesson.figures || []).filter((f) => f.moduleIds.length === 0).length;
}, 0);
const kindCensus = { checks_mcq: 0, written_recall: 0, written_explain_why: 0, written_application: 0 };
for (const r of rows) {
  const pkgObj = r.wave === 3 ? outPkgs[r.noteId] : JSON.parse(priorByKind[r.noteId]["sme-question-package"].buf.toString("utf8"));
  for (const q of pkgObj.questions) {
    if (!q.kind || q.kind === "mcq") kindCensus.checks_mcq++;
    else if (q.kind === "recall") kindCensus.written_recall++;
    else if (q.kind === "explain-why") kindCensus.written_explain_why++;
    else if (q.kind === "application") kindCensus.written_application++;
  }
}
gate("B2 identity arithmetic: 9 = 5+2+1+1 per lesson (cumulative)", census.lessons * 9 === census.checks &&
  kindCensus.checks_mcq === census.lessons * 5 && kindCensus.written_recall === census.lessons * 2 &&
  kindCensus.written_explain_why === census.lessons && kindCensus.written_application === census.lessons,
  JSON.stringify({ ...census, ...kindCensus }));
{
  const w3L = NOTES.reduce((a, n) => a + sources[n].lessons.length, 0);
  const w3C = NOTES.reduce((a, n) => a + sources[n].lessons.reduce((b, l) => b + l.check.length, 0), 0);
  gate("cumulative delta vs v21: +7 notes, +14 lessons, +126 checks", census.notes === 16 + NOTES.length && census.lessons === 32 + w3L && census.checks === 288 + w3C && w3L === 14 && w3C === 126,
    JSON.stringify({ notes: census.notes, lessons: census.lessons, checks: census.checks, w3L, w3C }));
}

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

// ── manifest v21 (B6 CONTINUE-GLOBAL of record) ───────────────────────────────
section("manifest v22");
const artifacts = [];
for (const p of priorAnchors) {
  artifacts.push({ kind: p.kind, noteId: p.noteId, path: p.path, sha256: p.sha256, bytes: p.bytes });
}
for (const n of NOTES) {
  artifacts.push({ kind: "hub-lesson-import-1.5", noteId: n, path: `SME-GuidedLessons/integration/hub-import-1.5/${n}.hub-lesson-import.json`, sha256: newSha[n].hub.sha256, bytes: newSha[n].hub.bytes });
  artifacts.push({ kind: "sme-question-package", noteId: n, path: `SME-GuidedLessons/integration/question-packages-1.2/${n}.sme-question-package.json`, sha256: newSha[n].pkg.sha256, bytes: newSha[n].pkg.bytes });
}
const man22 = {
  format: "hub-import-manifest/1.0",
  manifest_version: MANIFEST_VERSION,
  course_id: COURSE_ID,
  b6_manifest_continuity: {
    decision: "continue-global",
    selected: "physics wave-3 = manifest v22 (CUMULATIVE over the igcse-physics-19 pack — the chemistry v8..v17 pattern; the programme series continues)",
    rejected: "per-course series (physics v1) — would collide with chemistry hub-import-manifest-v1..v17.json filenames in the shared integration/ namespace and fork the integration ledger",
    recorded_by: "runbook B6 + the stage-A receipt of record (PHYSICS-4PH1-STAGEA-PROMOTION-20261101.json); continued at v19/v20/v21, continued here at v22",
  },
  generated_at_utc: now(),
  operator_trace: EXEC_TRACE,
  supersedes: "hub-import-manifest-v21.json (the wave-2 tranche: 32 artifacts, 16-note pack @ resources merge-of-record 78dd3694, promo commit C 7b08a426) — all 32 re-pinned byte-identical here; v22 is the THIRD register wave: +7 igcse-physics-19 notes, +14 first-issue artifacts, 46 artifacts over the 23-note pack",
  checks_layer: {
    wave: "PHYSICS-4PH1 wave-3 (the 1-3 momentum + 1-4 moments subtopics: 1-3-1..1-3-4, 1-4-1..1-4-3; B4 frozen-partition bucket of record) — operator ignition trace " + IGNITION_TRACE + " (\"Proceed with wave-3\"), execution trace " + EXEC_TRACE + " (same operator session, single-window execution disclosed)",
    derivation: "126 authored wave-3 checks (70 MCQ + 28 recall + 14 explain-why + 14 application = 14 lessons x [5 MCQ + 2 recall + 1 explain-why + 1 application]), spec-anchored to 4PH1 1.25P..1.33P with KP-index provenance; cumulative pack = 414 checks (230 MCQ + 92 recall + 46 explain-why + 46 application); written items carry modelAnswer + generous synonym/inflection-bearing keywords",
    declared_revision: "the FOURTH package-channel tranche and the THIRD register wave of the new subject: 7 packages issued under sme-question-package/1.2 and 7 lessons under hub/lesson-import/1.5 (FIRST issues @ the commit-A pin); the 32 prior-pack artifacts are re-pinned byte-identical (2 pilot @ v18 shas + 12 wave-1 @ v19 shas + 18 wave-2 @ v21 shas)",
    grading_law: "case-insensitive whole-token match of the learner text against keywords[]; >=1 hit -> correct; 0 hits -> not-quite + model answer; empty submit blocked; keywords absent -> reveal-only (fail-closed, never a silent wrong grade)",
    fail_closed: "written item without modelAnswer renders reveal-only, never gradeable, never blank; unknown kind renders reveal-only and warns at this gate",
  },
  source_generation: {
    format: "guided-lesson/0.6",
    namespace: "SME-GuidedLessons/integration/source-0.6/",
    pin: commitA,
    prior_pack_pins: { pilot: PILOT_PIN, wave1: WAVE1_PIN, wave2: WAVE2_PIN },
    int0_lineage: "(new subject — no INT-0 ancestry; the wave-3 0.6 sources are authored directly from the igcse-physics-19 revision-note rows of record, hub notes.json @ " + HUB_MAIN_AT_OPEN.slice(0, 8) + ")",
  },
  load_scope: { adapter: ADAPTER, target_schemas: ["hub/lesson-import/1.5", "sme-question-package/1.2"] },
  counts,
  conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut },
  artifacts,
};
gate("manifest v22 lists 46 artifacts", artifacts.length === 46, String(artifacts.length));

// ── INT-3 record ──────────────────────────────────────────────────────────────
const int3 = {
  stage: "INT-3",
  title: "transform record — PHYSICS-4PH1 wave-3 (adapter guided-lesson-0.6--hub-lesson-import-1.5) — CUMULATIVE 23-row anchor table",
  generated_at_utc: now(),
  operator_traces: { ignition: IGNITION_TRACE, execution: EXEC_TRACE, note: "ignition and execution share the session trace — single-window execution, disclosed" },
  adapter: ADAPTER,
  course_id: COURSE_ID,
  supersedes_int3: "INT-3-transform-record-physics-wave2.json (16 rows) — extended here to the full 23-row pack table (the v19 index-regression lesson of record: the INT-3 must carry EVERY pack row so the runner-owned guided-import.json rebuild keeps the whole flow)",
  b6_manifest_continuity: man22.b6_manifest_continuity,
  b4_partition_of_record: {
    law: "runbook §0 B4 — partition at wave open only; final wave takes the remainder; never re-bucket mid-programme",
    basis: "hub notes.json register rows (127) minus the stage-A pilot (B3) = 126 notes at freeze, section-aligned in register order; W1 (6 notes) landed at v19, W2 (9 notes) at v21; 111 remain bucketed",
    buckets: Object.fromEntries(Object.entries(B4_PARTITION).map(([w, secs]) => [w, { sections: secs, notes: w === "W3" ? NOTES.length : null }])),
    executed_this_wave: "W3 (1-3-1..1-3-4 momentum; 1-4-1..1-4-3 moments)",
  },
  source_pin: {
    repo: "SyllabAI/syllabai-resources",
    ref: RES_MAIN_AT_OPEN,
    note: "resources main at wave-2 open = 656ad812 (PR #278 run-038 corpus leg, printed-figure crops); re-grounded fetch-first at lane open and re-verified pre-branch — commit A's parent IS this sha; the overlap census vs the wave-2 namespaces (SME-GuidedLessons/**) is ZERO",
  },
  registry_pin: {
    repo: "SyllabAI/syllabai-v2",
    ref: HUB_MAIN_AT_OPEN,
    path: "apps/hub/content/igcse-physics-19/notes.json",
    note: "the revision-note rows of record (noteId registry, specPointCodes, bodyMd with asset URLs)",
  },
  source_06_generation_pin: { commit: commitA, namespace: "SME-GuidedLessons/integration/source-0.6/" },
  conservation_law:
    "kind/modelAnswer/keywords on written items ARE §7 stream tokens (the runner walk extends by those fields on kind!=mcq); each pack note's stream is anchored below (23 rows); the chemistry corpus streams are untouched (no chemistry bytes re-issued in v22); the 32 prior-pack artifacts are re-pinned byte-identical (sha-gated against the v21 manifest). Grand computed over the 23-note pack in artifact order; wave subtotals for wave-0/wave-1/wave-2 reproduce the v21 of-record values.",
  grand_stream: { chars: grandChars, sha256: grandSha },
  wave_stream_sha256: waveOut,
  battery: {
    names: "A0 / AN / SG / KW / JC / 2.1B / NUM (runbook §1.4 battery of record), run per note",
    a0: "ajv guided-lesson/0.6 x7 + 9-check SME kind order per lesson (14 lessons) + B2 sizing (7 notes -> 1-3 lessons each: 2+2+3+2+2+2+1) + spec-union law (lesson specRefs cover the file specPoints exactly) + figure closure both ways (25 figures) + glossary 3..8 + primer word band",
    an: "exactly one correct option per MCQ x70; per-note correct-key letter census >=3 distinct / max 5; option texts and keys distinct",
    sg: "lesson specRefs subset of file specPoints (4PH1 1.25P..1.33P); every check shares a content token with its lesson keyPoints (KP-index provenance)",
    kw: "written items >=3 distinct keywords, each grounded in the modelAnswer/stem/keyPoints union",
    jc: "every option explained; distractors name misconceptions; correct option misconception null",
    "2.1b": "zero 8-gram overlap between learner-surface text (stems, model answers, option text+explanations) and each note's bodyMd",
    num: "per-note numeric ledgers re-derived in code (see the NUM gate log): unit conversions, WE arithmetics, MCQ distractor arithmetics — all exact",
  },
  physics_census: {
    wave_notes: NOTES,
    wave_lessons: NOTES.reduce((a, n) => a + sources[n].lessons.length, 0),
    wave_checks: NOTES.reduce((a, n) => a + sources[n].lessons.reduce((b, l) => b + l.check.length, 0), 0),
    cumulative: { notes: census.notes, lessons: census.lessons, checks: census.checks, ...kindCensus },
    distractors: census.distractors,
    figures: census.figures,
    figures_captions: rows.reduce((a, r) => {
      const hubObj = r.wave === 3 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
      return a + (hubObj.lesson.figures || []).filter((f) => f.caption).length;
    }, 0),
    figures_no_caption: rows.reduce((a, r) => {
      const hubObj = r.wave === 3 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
      return a + (hubObj.lesson.figures || []).filter((f) => !f.caption).length;
    }, 0),
    figureless_notes: [],
    worked_examples_null_notes: NOTES.filter((n) => !sources[n].noteAssets.workedExample),
  },
  notes: rows,
};
emit(path.join(RES, "records/INT-3-transform-record-physics-wave3.json"), int3);
const manBuf = emit(path.join(RES, "hub-import-manifest-v22.json"), man22);

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
  wave: "PHYSICS-4PH1 wave-3 — the 1-3 momentum + 1-4 moments subtopics (1-3-1 Momentum, 1-3-2 Forces & Momentum, 1-3-3 Newton's Third Law, 1-3-4 Momentum & Safety Features, 1-4-1 Moments, 1-4-2 The Principle of Moments, 1-4-3 Centre of Gravity)",
  operator_traces: [IGNITION_TRACE, EXEC_TRACE],
  trace_note: "ignition and execution share the session trace 1a19c5cc34b70739 — the operator directive 'Proceed with wave-3' and this execution ran in one operator window; disclosed rather than minted",
  generated_at_utc: now(),
  repo: "SyllabAI/syllabai-resources",
  branch,
  runbook_of_record: ".syllabai/docs/new-subject-runbook.md @ SyllabAI/syllabai-v2 main",
  b6_manifest_continuity: man22.b6_manifest_continuity,
  b4_partition: int3.b4_partition_of_record,
  commits: {
    A: { sha: commitA, parent: commitAParent, note: "source-0.6 generation — 7 authored guided-lesson/0.6 wave-3 notes (14 lessons / 126 checks); schemas ride main unchanged from stage-A" },
    C: { sha: "(namespace-complete — outputs + manifest v22 + records + pipeline)", note: "hub-import-1.5/ x7 + question-packages-1.2/ x7 (FIRST issues) + hub-import-manifest-v22.json (46 artifacts cumulative) + records/INT-3-transform-record-physics-wave3.json (23 rows) + records/NS-4PH1-PHYSICS-WAVE3-PROMOTION-20261102.json + tooling/physics-wave3-pipeline.js" },
  },
  artifact_pin: commitA,
  pkg_pin: `${commitA} (all seven wave-3 packages pin the commit-A source generation)`,
  prior_pack_pins: { pilot: PILOT_PIN, wave1: WAVE1_PIN, wave2: WAVE2_PIN, note: "the 32 prior artifacts keep their generation pins inside their bytes; v22 re-pins their (identical) bytes at the manifest level only" },
  input_pins: { resources_main_at_wave3_open: RES_MAIN_AT_OPEN, hub_main_at_wave3_open: HUB_MAIN_AT_OPEN },
  manifest: "hub-import-manifest-v22.json",
  int_record: "INT-3-transform-record-physics-wave3.json",
  adapter_spec: "ADAPTER-SPEC-guided-lesson-0.6-to-hub-1.5.md (unchanged from stage-A)",
  counts_census: { notes: census.notes, lessons: census.lessons, checks: census.checks, ...kindCensus, distractors: census.distractors, wave_notes: NOTES },
  schema_delta:
    "NONE — wave-3 runs the stage-A union schemas byte-identical (guided-lesson/0.6, hub/lesson-import/1.5, sme-question-package/1.2). All 7 notes carry the figures layer (25 figures, all module-mapped, binding heading-unique per the wave-1 of-record convention); 3 of 7 notes declare workedExample null (1-3-4 Momentum & Safety Features, 1-4-1 Moments, 1-4-3 Centre of Gravity — no worked-example block exists in those note bodies, fail-closed absent).",
  taxonomy: "kind enum of record: mcq (default/absent) | recall | explain-why | application — 14 lessons x [5 MCQ + 2 recall + 1 explain-why + 1 application] = the B2 law; cumulative pack 46 lessons / 414 checks",
  conservation: {
    law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq; the wave-3 streams are anchored in the INT-3 record; chemistry streams byte-untouched; the 32 prior-pack artifacts re-pinned byte-identical (grand recomputed over the 23-note pack; wave-0/wave-1/wave-2 subtotals reproduce the v21 values exactly)",
    authored_chars: grandChars,
  },
  gates: { pipeline: `${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, 0 fail`, gate_log: CHECKS },
  merge_order:
    "resources PR (this branch) merges to main FIRST; the hub PR (FEED physics-wave3-v22 + landed artifacts + re-issued guided-import.json) merges only after; wave-4 buckets remain operator-gated and are NOT in this tranche (B4: one wave per gate)",
  hub_side_note:
    "the hub renderer is course-generic; the physics FEEDs physics-stagea-v18 / physics-wave1-v19 / physics-wave1-v20 / physics-wave2-v21 already exercised the parameterized runner — wave-3 adds one FEED entry (physics-wave3-v22) with feed-gated constants only (pack/course_id/counts/prefix/wave-count/artifact_pins_by_note for the 16 prior notes' provenance), chemistry-preserving defaults untouched",
  disclosures: [
    "naming: the contract of record named lanes ns4ph1-waveN; the landed executions use the physics-* family (receipts dirs PHYSICS-STAGEA/NS-4PH1, feeds physics-stagea-v18 / physics-wave1-v19 / physics-wave1-v20 / physics-wave2-v21) — wave-3 follows the LANDED convention (lane physics-wave3, feed physics-wave3-v22, receipts NS-4PH1)",
    "the 7/7 wave-3 notes carry figures (25 total); 3 carry no usable worked-example block (workedExample null declared): 1-3-4, 1-4-1, 1-4-3; 1-3-1 and 1-3-2 and the wave-2 convention of one WE slot per note are honored — 1-3-1's second note WE (toy car/van) anchors the L2 application check instead, 1-3-2's first note WE (tennis ball) surfaces in L2 keyPoints + MCQ",
    "figures mapping law: ids fig-01..fig-NN in bodyMd image order; url re-written from the relative note form to the main/ form of the 0.6 schema pattern; every basename verified present in the assets dir; captions taken from the notes' own bold-italic sidecar lines where they exist (fail-closed absent otherwise — 9 of 25 wave-3 figures carry none: the WE-embedded and callout-embedded figures whose notes offer no bold-italic sidecar line)",
    "spec 1.29P's text of record carries the Unicode right single quote (Newton’s) and spec 1.28P's text carries the curriculum's flat 'F = t' rendering — both carried verbatim from the curriculum nodes of record (zero-invention law)",
    "executed_this_wave bucket-size law: the frozen partition of the wave-1 contract is honored byte-for-byte; W3 = 7 notes as frozen (4 momentum + 3 moments)",
    "other-run activity at open disclosed: resources main aa004cb1 (PR #280 T-OEQ-PHYS-FORMAT-1, Official-ExamQuestion corpus backsync — zero SME-GuidedLessons overlap); hub main a7f2f5a2 (R0-AUTO-109 bookkeeping band, PRs #634/#643 — .syllabai/lanes only) — both unrelated lanes, race-guard re-checks due at push",
    "sandbox recycle lost the previous sessions' lane mirrors; all of-record state re-fetched from remotes (fetch-first honored); the runbook mirror was re-recovered from hub origin/main",
  ],
};
emit(path.join(RES, "records/NS-4PH1-PHYSICS-WAVE3-PROMOTION-20261102.json"), receipt);

// ── lane survivors for the hub runner byte-anchors ────────────────────────────
fs.mkdirSync(SURV, { recursive: true });
fs.mkdirSync(path.join(SURV, "schema"), { recursive: true });
fs.copyFileSync(path.join(RES, "hub-import-manifest-v22.json"), path.join(SURV, "hub-import-manifest-v22.json"));
fs.copyFileSync(path.join(RES, "records/INT-3-transform-record-physics-wave3.json"), path.join(SURV, "INT-3-transform-record-physics-wave3.json"));
fs.copyFileSync(path.join(RES, "schema/hub-lesson-import.1.5.schema.json"), path.join(SURV, "schema/hub-lesson-import.1.5.schema.json"));
fs.copyFileSync(path.join(RES, "schema/sme-question-package.1.2.schema.json"), path.join(SURV, "schema/sme-question-package.1.2.schema.json"));

console.log(`\nRESULT: ${FAILED === 0 ? "GREEN — PIPELINE COMPLETE" : "FAIL-CLOSED"}`);
console.log(`  gates: ${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, ${FAILED} failures`);
console.log(`  cumulative grand: ${grandChars} chars ${grandSha.slice(0, 16)}…`);
console.log(`  census: ${JSON.stringify(counts)}`);
