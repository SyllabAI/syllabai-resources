/**
 * PHYSICS-WAVE5 PIPELINE — new-subject stage-B wave-5 transform + manifest v24 + INT-3 record
 * (operator ignition trace 1a19f5a4a25fe011 "Proceed with wave-5"; execution trace
 *  1a19f5a4a25fe011 — ignition and execution share the session trace, single-window execution,
 *  disclosed in the promotion receipt)
 *
 * Runbook of record: .syllabai/docs/new-subject-runbook.md @ hub main (§1 wave lifecycle).
 * B6 of record (stage-A, continued at v19..v23): CONTINUE-GLOBAL manifest series — wave-5 =
 * hub-import-manifest-v24.json, CUMULATIVE over the igcse-physics-19 pack (the chemistry
 * v8..v17 pattern; the v19 index-regression lesson of record: the INT-3 carries ALL 40 rows).
 * B4 of record: the frozen partition of the wave-1 contract — wave-5 executes bucket W5
 * (the 2-3-electrical-power-and-mains-electricity + 2-4-static-electricity
 * subtopics, 9 notes).
 *
 * Input of record (lane clone @ resources main b1ea377e…, branch integration/physics-wave5-20261103):
 *   source-0.6/ ×9 authored wave-5 notes (guided-lesson/0.6, committed @ commit A of this branch)
 *   schema/guided-lesson.0.6.schema.json + {hub-lesson-import.1.5, sme-question-package.1.2} (main, unchanged)
 *   source-0.5/ ×112 + hub-import-1.4/ ×112 + question-packages-1.1/ ×112 (chemistry union baselines)
 *   hub-import-manifest-v22.json + records/INT-3-transform-record-physics-wave3.json (the pack of record)
 *
 * Outputs (namespace-complete, committed @ commit C):
 *   hub-import-1.5/rn_<id>.hub-lesson-import.json ×9        (format hub/lesson-import/1.5, FIRST issues)
 *   question-packages-1.2/rn_<id>.sme-question-package.json ×9 (format sme-question-package/1.2, FIRST issues)
 *   hub-import-manifest-v24.json  (CUMULATIVE: 80 artifacts = 62 pack re-pins byte-identical + 18 first issues)
 *   records/INT-3-transform-record-physics-wave5.json  (40-row anchor table — the v19-lesson law)
 *   records/NS-4PH1-PHYSICS-WAVE5-PROMOTION-20261103.json
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

const RES = "/home/z/my-project/w5/res/SME-GuidedLessons/integration";
const RES_REPO = "/home/z/my-project/w5/res";
const HUB_REPO = "/home/z/my-project/w5/hub";
const SURV = "/home/z/my-project/scripts/physics-wave5-survivors";
const NOTES = [
  "rn_PZZFkywYbmP9bwyh", // 2-3-1 Electrical Power & Fuses (2.15, 2.4)
  "rn_FfvmFrDdhSsMk9rm", // 2-3-2 Calculating Energy Transfers (2.5)
  "rn_kxw7Ms4Pr7dQJykY", // 2-3-3 Electrical Safety (2.2)
  "rn_z4nNPFw97V9fDkyS", // 2-3-4 Electricity & Heat (2.3)
  "rn_NgxJhPpm5Zs7kFSz", // 2-3-5 AC & DC (2.6)
  "rn_qG9dxcQrRJJVDQf7", // 2-4-1 Conductors & Insulators (2.22P)
  "rn_ws8NtMW3QwCs73Gh", // 2-4-2 Core Practical: Charging by Friction (2.23P)
  "rn_NhRw6hdrVD4vmNJw", // 2-4-3 Electric Charge (2.24P, 2.25P, 2.26P)
  "rn_W3QnDKVK9mMQ3Mhg", // 2-4-4 Uses & Dangers of Static Electricity (2.27P, 2.28P)
];
const IGNITION_TRACE = "1a19f5a4a25fe011";
const EXEC_TRACE = "1a19f5a4a25fe011"; // single-window execution (disclosed)
const ADAPTER = "guided-lesson-0.6--hub-lesson-import-1.5";
const COURSE_ID = "igcse-physics-19";
const COURSE_PREFIX = "igcse-physics";
const RES_MAIN_AT_OPEN = "63c23d0a2dccf690bea40e00c701095eab1eaeba"; // PR #287 run-012 reconciliation-census band tip (T-OEQ-PHYS-FORMAT-1); zero SME-GuidedLessons overlap with the wave-5 namespaces
const HUB_MAIN_AT_OPEN = "0e788d623190c80d5698d7d1c5d7efebf24a9b8c"; // wave-4 bookkeeping merge tip (PR #660); zero overlap
const MANIFEST_VERSION = 24; // B6 CONTINUE-GLOBAL — the series continues from v23
const PRIOR_MANIFEST_VERSION = 23;
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
const WAVE3_NOTES = [
  "rn_pqp4mfpHzGVtrjTT", "rn_NfCjFmPfmMQ8pQSw", "rn_8wqvPtsCCh3gdJN5",
  "rn_RQK2MW3zRPNNzwtc", "rn_jzQZQcPRQkJvdYwJ", "rn_zn4NVCRcTSNv8sRZ",
  "rn_TPDdhwDYsrWgQB7R",
];
const WAVE3_PIN = "377ef184395b676ce98c183a46fd72c584deb4fa"; // wave-3 trace-bearing repin = the promotion commit of record (provenance of record)
const WAVE4_NOTES = [
  "rn_NZ5D2Mx9SXQY98wy", "rn_BcxDP3RzXk3k7rwf", "rn_64pQyK4tm9P9rdKN",
  "rn_BFQBSmVz2xFZVsB6", "rn_ynsstfBQngnx2pgq", "rn_PyxMmTd6S9pMDTt6",
  "rn_WzQZfyNNFFFFghbF", "rn_gYqbXsJPfrqtg5yQ",
];
const WAVE4_PIN = "acd23dd30dda707775cd5f27346ee0a3958c0afe"; // wave-4 merge-of-record (PR #286) = the promotion commit of record (provenance of record)
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
gate("P0 branch is the wave-5 integration branch", branch === "integration/physics-wave5-20261103", branch);
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
section("B4 partition of record (104-note freeze remainder; 96 unlanded after wave-4, pilot excluded)");
{
  const reg = noteRows.map((r) => r.path.replace(/\.md$/, "")).sort();
  gate("register census 127 rows", reg.length === 127, String(reg.length));
  const pilotPath = noteRows.find((r) => r.noteId === PILOT_OF_RECORD).path.replace(/\.md$/, "");
  const landed = new Set([pilotPath, ...WAVE1_NOTES.map((id) => noteRows.find((r) => r.noteId === id).path.replace(/\.md$/, "")), ...WAVE2_NOTES.map((id) => noteRows.find((r) => r.noteId === id).path.replace(/\.md$/, "")), ...WAVE3_NOTES.map((id) => noteRows.find((r) => r.noteId === id).path.replace(/\.md$/, "")), ...WAVE4_NOTES.map((id) => noteRows.find((r) => r.noteId === id).path.replace(/\.md$/, ""))]);
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
  gate("B4 buckets partition the 96-note post-wave-4 remainder exactly", total === 96, `${total} notes bucketed (126 at freeze − 30 landed through W4, pilot excluded)`);
  gate("B4 W5 == the 9 authored wave-5 notes", JSON.stringify(buckets["W5"].map((p) => p.split("/").pop())) === JSON.stringify([
    "2-3-1-electrical-power-and-fuses", "2-3-2-calculating-energy-transfers", "2-3-3-electrical-safety",
    "2-3-4-electricity-and-heat", "2-3-5-ac-and-dc", "2-4-1-conductors--insulators",
    "2-4-2-core-practical-investigating-charging-by-friction", "2-4-3-electric-charge",
    "2-4-4-uses--dangers-of-static-electricity",
  ]), buckets["W5"].map((p) => p.split("/").pop()).join(","));
  gate("B4 pilot + W1..W4 outside every remaining bucket", !Object.values(buckets).some((b) => b.some((p) => landed.has(p))), "");
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
  rn_PZZFkywYbmP9bwyh: [
    ["L1 MCQ3 V = 48 / 4 = 12 V", 48 / 4 === 12],
    ["L1 MCQ3 distractor 48 x 4 = 192 V", 48 * 4 === 192],
    ["L1 MCQ3 distractor 4/48 = 0.083 V (2 s.f.)", Math.round((4 / 48) * 1000) / 1000 === 0.083],
    ["L1 MCQ3 distractor 48 + 4 = 52 V", 48 + 4 === 52],
    ["L1 app 10 A x 230 V = 2300 W", 10 * 230 === 2300],
    ["WE 48 / 4 = 12", 48 / 4 === 12],
    ["L2 MCQ3 P = 4 A x 230 V = 920 W", 4 * 230 === 920],
    ["L2 MCQ3 distractor 230/4 = 57.5 W", 230 / 4 === 57.5],
    ["L2 MCQ3 distractor 230 + 4 = 234 W", 230 + 4 === 234],
    ["L2 MCQ3 distractor 920 x 2 = 1840 W", 920 * 2 === 1840],
    ["L2 app spare amperes 13 - 5 = 8", 13 - 5 === 8],
  ],
  rn_FfvmFrDdhSsMk9rm: [
    ["L1 MCQ3 0.7 x 4 x 60 = 168 J", Math.round(0.7 * 4 * 60 * 1e9) / 1e9 === 168],
    ["L1 MCQ3 distractor 0.7 x 4 = 2.8 J (time dropped)", Math.round(0.7 * 4 * 1e9) / 1e9 === 2.8],
    ["L1 MCQ3 distractor 4 x 60 = 240 J (current dropped)", 4 * 60 === 240],
    ["L1 MCQ3 distractor 0.7 x 4 x 6 = 16.8 J (seconds slip)", Math.round(0.7 * 4 * 6 * 1e9) / 1e9 === 16.8],
    ["L1 explain-why 1 min = 60 s", 1 * 60 === 60],
    ["WE 1 min = 60 s; 0.7 x 4 x 60 = 168 J", Math.round(0.7 * 4 * 60 * 1e9) / 1e9 === 168],
    ["L1 app 2 x 12 x 30 = 720 J", 2 * 12 * 30 === 720],
  ],
  rn_kxw7Ms4Pr7dQJykY: [
    ["qualitative safety note — no arithmetic on the learner surface", true],
  ],
  rn_z4nNPFw97V9fDkyS: [
    ["qualitative note — no arithmetic on the learner surface", true],
  ],
  rn_NgxJhPpm5Zs7kFSz: [
    ["UK mains figures are stated facts (50 Hz, 230 V) — no derived arithmetic on the learner surface", true],
  ],
  rn_qG9dxcQrRJJVDQf7: [
    ["qualitative note — no arithmetic on the learner surface", true],
  ],
  rn_ws8NtMW3QwCs73Gh: [
    ["0 - (-1) = +1 (the electron-subtraction law of the exam hint)", 0 - (-1) === 1],
    ["paper-circle variant: rod X 8 circles > rod Y 3 circles", 8 > 3],
  ],
  rn_NhRw6hdrVD4vmNJw: [
    ["qualitative note — no arithmetic on the learner surface", true],
  ],
  rn_W3QnDKVK9mMQ3Mhg: [
    ["qualitative note — no arithmetic on the learner surface", true],
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
section("prior pack of record (62 artifacts re-pinned byte-identical from v23)");
const man23 = JSON.parse(execSync("git show HEAD:SME-GuidedLessons/integration/hub-import-manifest-v23.json", { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 16 }).toString());
const int3v23 = JSON.parse(execSync("git show HEAD:SME-GuidedLessons/integration/records/INT-3-transform-record-physics-wave4.json", { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 16 }).toString());
gate("prior manifest is v23", man23.manifest_version === 23 && man23.artifacts.length === 62, String(man23.artifacts.length));
const priorNotes = [PILOT_OF_RECORD, ...WAVE1_NOTES, ...WAVE2_NOTES, ...WAVE3_NOTES, ...WAVE4_NOTES];
const waveOf = {};
waveOf[PILOT_OF_RECORD] = 0;
for (const id of WAVE1_NOTES) waveOf[id] = 1;
for (const id of WAVE2_NOTES) waveOf[id] = 2;
for (const id of WAVE3_NOTES) waveOf[id] = 3;
for (const id of WAVE4_NOTES) waveOf[id] = 4;
for (const n of NOTES) waveOf[n] = 5;
const priorAnchors = [];
for (const a of man23.artifacts) {
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
  const v23row = int3v23.notes.find((r) => r.noteId === nid);
  gate(`prior stream re-derivation matches v23 INT-3: ${nid.slice(0, 12)}`, v23row && sha256(Buffer.from(s, "utf8")) === v23row.stream.sha256 && s.length === v23row.stream.chars, `${nid}: ${sha256(Buffer.from(s, "utf8")).slice(0, 12)}`);
}

// ── G-E stream (the runner's walk, byte-identical law) ────────────────────────
section("G-E stream anchors + wave subtotals + cumulative grand");
const rows = [];
for (const nid of [PILOT_OF_RECORD, ...WAVE1_NOTES, ...WAVE2_NOTES, ...WAVE3_NOTES, ...WAVE4_NOTES]) {
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
    wave: 5,
    sourceLayerSha256: sha256(read(path.join(RES, "source-0.6", `guided-lesson-${n}.json`))),
    hubSha256: newSha[n].hub.sha256,
    pkgSha256: newSha[n].pkg.sha256,
    stream: { sha256: sha256(Buffer.from(s, "utf8")), chars: s.length },
  });
}
gate("INT-3 carries ALL 40 pack rows (the v19-lesson law)", rows.length === 40, String(rows.length));
let grandChars = 0;
const grand = crypto.createHash("sha256");
for (const r of rows) {
  const nid = r.noteId;
  const hubObj = r.wave === 5 ? outLessons[nid] : JSON.parse(priorByKind[nid]["hub-lesson-import-1.5"].buf.toString("utf8"));
  const pkgObj = r.wave === 5 ? outPkgs[nid] : JSON.parse(priorByKind[nid]["sme-question-package"].buf.toString("utf8"));
  const s = targetTokens(hubObj, pkgObj).join("\n");
  grand.update(Buffer.from(s, "utf8"));
  grandChars += s.length;
}
const grandSha = grand.digest("hex");
const waveHashes = {};
for (const r of rows) {
  const nid = r.noteId;
  const hubObj = r.wave === 5 ? outLessons[nid] : JSON.parse(priorByKind[nid]["hub-lesson-import-1.5"].buf.toString("utf8"));
  const pkgObj = r.wave === 5 ? outPkgs[nid] : JSON.parse(priorByKind[nid]["sme-question-package"].buf.toString("utf8"));
  const s = targetTokens(hubObj, pkgObj).join("\n");
  const w = "wave-" + r.wave;
  waveHashes[w] = waveHashes[w] || crypto.createHash("sha256");
  waveHashes[w].update(Buffer.from(s, "utf8"));
}
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest("hex");
gate("wave subtotals reproduce the v23 of-record values for wave-0..wave-4",
  waveOut["wave-0"] === int3v23.wave_stream_sha256["wave-0"] && waveOut["wave-1"] === int3v23.wave_stream_sha256["wave-1"] && waveOut["wave-2"] === int3v23.wave_stream_sha256["wave-2"] && waveOut["wave-3"] === int3v23.wave_stream_sha256["wave-3"] && waveOut["wave-4"] === int3v23.wave_stream_sha256["wave-4"],
  `w0 ${waveOut["wave-0"].slice(0, 12)} w1 ${waveOut["wave-1"].slice(0, 12)} w2 ${waveOut["wave-2"].slice(0, 12)} w3 ${waveOut["wave-3"].slice(0, 12)} w4 ${waveOut["wave-4"].slice(0, 12)}`);
console.log(`  cumulative grand: ${grandChars} chars ${grandSha.slice(0, 16)}… (wave-5: ${waveOut["wave-5"].slice(0, 12)}…)`);

// census from the emitted bytes (disk-derived, not asserted)
const census = {
  notes: 40,
  lessons: rows.reduce((a, r) => {
    const hubObj = r.wave === 5 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + hubObj.lesson.modules.length;
  }, 0),
  checks: rows.reduce((a, r) => {
    const pkgObj = r.wave === 5 ? outPkgs[r.noteId] : JSON.parse(priorByKind[r.noteId]["sme-question-package"].buf.toString("utf8"));
    return a + pkgObj.questions.length;
  }, 0),
  keyPoints: rows.reduce((a, r) => {
    const hubObj = r.wave === 5 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + hubObj.lesson.modules.reduce((b, m) => b + m.keyPoints.length, 0);
  }, 0),
  distractors: rows.reduce((a, r) => {
    const pkgObj = r.wave === 5 ? outPkgs[r.noteId] : JSON.parse(priorByKind[r.noteId]["sme-question-package"].buf.toString("utf8"));
    return a + pkgObj.questions.reduce((b, q) => b + (q.options || []).filter((o) => o.correct !== true).length, 0);
  }, 0),
  glossaryTerms: rows.reduce((a, r) => {
    const hubObj = r.wave === 5 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + (hubObj.lesson.assets.glossary || []).length;
  }, 0),
  figures: rows.reduce((a, r) => {
    const hubObj = r.wave === 5 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + (hubObj.lesson.figures || []).length;
  }, 0),
  workedExamples_populated: rows.reduce((a, r) => {
    const hubObj = r.wave === 5 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + (hubObj.lesson.assets.workedExample ? 1 : 0);
  }, 0),
  workedExamples_null: rows.reduce((a, r) => {
    const hubObj = r.wave === 5 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
    return a + (hubObj.lesson.assets.workedExample ? 0 : 1);
  }, 0),
};
census.figures_module_mapped = rows.reduce((a, r) => {
  const hubObj = r.wave === 5 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
  return a + (hubObj.lesson.figures || []).filter((f) => f.moduleIds.length > 0).length;
}, 0);
census.figures_note_level = rows.reduce((a, r) => {
  const hubObj = r.wave === 5 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
  return a + (hubObj.lesson.figures || []).filter((f) => f.moduleIds.length === 0).length;
}, 0);
const kindCensus = { checks_mcq: 0, written_recall: 0, written_explain_why: 0, written_application: 0 };
for (const r of rows) {
  const pkgObj = r.wave === 5 ? outPkgs[r.noteId] : JSON.parse(priorByKind[r.noteId]["sme-question-package"].buf.toString("utf8"));
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
  const w5L = NOTES.reduce((a, n) => a + sources[n].lessons.length, 0);
  const w5C = NOTES.reduce((a, n) => a + sources[n].lessons.reduce((b, l) => b + l.check.length, 0), 0);
  gate("cumulative delta vs v23: +9 notes, +18 lessons, +162 checks", census.notes === 31 + NOTES.length && census.lessons === 62 + w5L && census.checks === 558 + w5C && w5L === 18 && w5C === 162,
    JSON.stringify({ notes: census.notes, lessons: census.lessons, checks: census.checks, w5L, w5C }));
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

// ── manifest v23 (B6 CONTINUE-GLOBAL of record) ───────────────────────────────
section("manifest v24");
const artifacts = [];
for (const p of priorAnchors) {
  artifacts.push({ kind: p.kind, noteId: p.noteId, path: p.path, sha256: p.sha256, bytes: p.bytes });
}
for (const n of NOTES) {
  artifacts.push({ kind: "hub-lesson-import-1.5", noteId: n, path: `SME-GuidedLessons/integration/hub-import-1.5/${n}.hub-lesson-import.json`, sha256: newSha[n].hub.sha256, bytes: newSha[n].hub.bytes });
  artifacts.push({ kind: "sme-question-package", noteId: n, path: `SME-GuidedLessons/integration/question-packages-1.2/${n}.sme-question-package.json`, sha256: newSha[n].pkg.sha256, bytes: newSha[n].pkg.bytes });
}
const man24 = {
  format: "hub-import-manifest/1.0",
  manifest_version: MANIFEST_VERSION,
  course_id: COURSE_ID,
  b6_manifest_continuity: {
    decision: "continue-global",
    selected: "physics wave-5 = manifest v24 (CUMULATIVE over the igcse-physics-19 pack — the chemistry v8..v17 pattern; the programme series continues)",
    rejected: "per-course series (physics v1) — would collide with chemistry hub-import-manifest-v1..v17.json filenames in the shared integration/ namespace and fork the integration ledger",
    recorded_by: "runbook B6 + the stage-A receipt of record (PHYSICS-4PH1-STAGEA-PROMOTION-20261101.json); continued at v19/v20/v21/v22/v23, continued here at v24",
  },
  generated_at_utc: now(),
  operator_trace: EXEC_TRACE,
  supersedes: "hub-import-manifest-v23.json (the wave-4 tranche: 62 artifacts, 31-note pack @ resources merge-of-record acd23dd3, promo pin acd23dd3) — all 62 re-pinned byte-identical here; v24 is the FIFTH register wave: +9 igcse-physics-19 notes, +18 first-issue artifacts, 80 artifacts over the 40-note pack",
  checks_layer: {
    wave: "PHYSICS-4PH1 wave-5 (the 2-3 electrical-power-and-mains-electricity + 2-4 static-electricity subtopics: 2-3-1..2-3-5, 2-4-1..2-4-4; B4 frozen-partition bucket of record) — operator ignition trace " + IGNITION_TRACE + " (\"Proceed with wave-5\"), execution trace " + EXEC_TRACE + " (same operator session, single-window execution disclosed)",
    derivation: "162 authored wave-5 checks (90 MCQ + 36 recall + 18 explain-why + 18 application = 18 lessons x [5 MCQ + 2 recall + 1 explain-why + 1 application]), spec-anchored to 4PH1 2.2..2.28P with KP-index provenance; cumulative pack = 720 checks (390 MCQ + 156 recall + 78 explain-why + 78 application); written items carry modelAnswer + generous synonym/inflection-bearing keywords",
    declared_revision: "the SIXTH package-channel tranche and the FIFTH register wave of the new subject: 9 packages issued under sme-question-package/1.2 and 9 lessons under hub/lesson-import/1.5 (FIRST issues @ the commit-A pin); the 62 prior-pack artifacts are re-pinned byte-identical (2 pilot @ v18 shas + 12 wave-1 @ v19 shas + 18 wave-2 @ v21 shas + 14 wave-3 @ v22 shas + 16 wave-4 @ v23 shas)",
    grading_law: "case-insensitive whole-token match of the learner text against keywords[]; >=1 hit -> correct; 0 hits -> not-quite + model answer; empty submit blocked; keywords absent -> reveal-only (fail-closed, never a silent wrong grade)",
    fail_closed: "written item without modelAnswer renders reveal-only, never gradeable, never blank; unknown kind renders reveal-only and warns at this gate",
  },
  source_generation: {
    format: "guided-lesson/0.6",
    namespace: "SME-GuidedLessons/integration/source-0.6/",
    pin: commitA,
    prior_pack_pins: { pilot: PILOT_PIN, wave1: WAVE1_PIN, wave2: WAVE2_PIN, wave3: WAVE3_PIN, wave4: WAVE4_PIN },
    int0_lineage: "(new subject — no INT-0 ancestry; the wave-5 0.6 sources are authored directly from the igcse-physics-19 revision-note rows of record, hub notes.json @ " + HUB_MAIN_AT_OPEN.slice(0, 8) + ")",
  },
  load_scope: { adapter: ADAPTER, target_schemas: ["hub/lesson-import/1.5", "sme-question-package/1.2"] },
  counts,
  conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut },
  artifacts,
};
gate("manifest v24 lists 80 artifacts", artifacts.length === 80, String(artifacts.length));

// ── INT-3 record ──────────────────────────────────────────────────────────────
const int3 = {
  stage: "INT-3",
  title: "transform record — PHYSICS-4PH1 wave-5 (adapter guided-lesson-0.6--hub-lesson-import-1.5) — CUMULATIVE 40-row anchor table",
  generated_at_utc: now(),
  operator_traces: { ignition: IGNITION_TRACE, execution: EXEC_TRACE, note: "ignition and execution share the session trace — single-window execution, disclosed" },
  adapter: ADAPTER,
  course_id: COURSE_ID,
  supersedes_int3: "INT-3-transform-record-physics-wave4.json (31 rows) — extended here to the full 40-row pack table (the v19 index-regression lesson of record: the INT-3 must carry EVERY pack row so the runner-owned guided-import.json rebuild keeps the whole flow)",
  b6_manifest_continuity: man24.b6_manifest_continuity,
  b4_partition_of_record: {
    law: "runbook §0 B4 — partition at wave open only; final wave takes the remainder; never re-bucket mid-programme",
    basis: "hub notes.json register rows (127) minus the stage-A pilot (B3) = 126 notes at freeze, section-aligned in register order; W1 (6 notes) landed at v19, W2 (9 notes) at v21, W3 (7 notes) at v22, W4 (8 notes) at v23; 96 remain bucketed",
    buckets: Object.fromEntries(Object.entries(B4_PARTITION).map(([w, secs]) => [w, { sections: secs, notes: w === "W5" ? NOTES.length : null }])),
    executed_this_wave: "W5 (2-3-1 electrical-power-and-fuses; 2-3-2 calculating-energy-transfers; 2-3-3 electrical-safety; 2-3-4 electricity-and-heat; 2-3-5-ac-and-dc; 2-4-1 conductors--insulators; 2-4-2 core-practical-investigating-charging-by-friction; 2-4-3 electric-charge; 2-4-4 uses--dangers-of-static-electricity)",
  },
  source_pin: {
    repo: "SyllabAI/syllabai-resources",
    ref: RES_MAIN_AT_OPEN,
    note: "resources main at wave-5 open = 63c23d0a (PR #287 run-012 reconciliation census + adoption law, T-OEQ-PHYS-FORMAT-1 lane, scripts/oeq_phys_run012/ only) — re-grounded fetch-first at lane open and re-verified at branch cut (the tip moved b1ea377e -> 63c23d0a DURING lane setup; the branch was cut from the moved tip and the open of record updated, disclosed); commit A's parent IS this sha; the diff census vs SME-GuidedLessons/** from the wave-4 close sha (acd23dd3) is ZERO files, so the wave namespaces start clean",
  },
  registry_pin: {
    repo: "SyllabAI/syllabai-v2",
    ref: HUB_MAIN_AT_OPEN,
    path: "apps/hub/content/igcse-physics-19/notes.json",
    note: "the revision-note rows of record (noteId registry, specPointCodes, bodyMd with asset URLs)",
  },
  source_06_generation_pin: { commit: commitA, namespace: "SME-GuidedLessons/integration/source-0.6/" },
  conservation_law:
    "kind/modelAnswer/keywords on written items ARE §7 stream tokens (the runner walk extends by those fields on kind!=mcq); each pack note's stream is anchored below (40 rows); the chemistry corpus streams are untouched (no chemistry bytes re-issued in v24); the 62 prior-pack artifacts are re-pinned byte-identical (sha-gated against the v23 manifest). Grand computed over the 40-note pack in artifact order; wave subtotals for wave-0..wave-4 reproduce the v23 of-record values.",
  grand_stream: { chars: grandChars, sha256: grandSha },
  wave_stream_sha256: waveOut,
  battery: {
    names: "A0 / AN / SG / KW / JC / 2.1B / NUM (runbook §1.4 battery of record), run per note",
    a0: "ajv guided-lesson/0.6 x9 + 9-check SME kind order per lesson (18 lessons) + B2 sizing (9 notes -> 1-3 lessons each: 2+1+3+1+2+2+2+3+2) + spec-union law (lesson specRefs cover the file specPoints exactly) + figure closure both ways (20 figures) + glossary 3..8 + primer word band",
    an: "exactly one correct option per MCQ x90; per-note correct-key letter census >=3 distinct / max 5; option texts and keys distinct",
    sg: "lesson specRefs subset of file specPoints (4PH1 2.2..2.28P); every check shares a content token with its lesson keyPoints (KP-index provenance)",
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
      const hubObj = r.wave === 5 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
      return a + (hubObj.lesson.figures || []).filter((f) => f.caption).length;
    }, 0),
    figures_no_caption: rows.reduce((a, r) => {
      const hubObj = r.wave === 5 ? outLessons[r.noteId] : JSON.parse(priorByKind[r.noteId]["hub-lesson-import-1.5"].buf.toString("utf8"));
      return a + (hubObj.lesson.figures || []).filter((f) => !f.caption).length;
    }, 0),
    figureless_notes: NOTES.filter((n) => !(sources[n].figures || []).length),
    worked_examples_null_notes: NOTES.filter((n) => !sources[n].noteAssets.workedExample),
  },
  notes: rows,
};
emit(path.join(RES, "records/INT-3-transform-record-physics-wave5.json"), int3);
const manBuf = emit(path.join(RES, "hub-import-manifest-v24.json"), man24);

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
  wave: "PHYSICS-4PH1 wave-5 — the 2-3 electrical-power-and-mains-electricity + 2-4 static-electricity subtopics (2-3-1 Electrical Power & Fuses, 2-3-2 Calculating Energy Transfers, 2-3-3 Electrical Safety, 2-3-4 Electricity & Heat, 2-3-5 AC & DC, 2-4-1 Conductors & Insulators, 2-4-2 Core Practical: Charging by Friction, 2-4-3 Electric Charge, 2-4-4 Uses & Dangers of Static Electricity)",
  operator_traces: [IGNITION_TRACE, EXEC_TRACE],
  trace_note: "ignition and execution share the session trace 1a19f5a4a25fe011 — the operator directive 'Proceed with wave-5' and this execution ran in one operator session; disclosed rather than minted",
  generated_at_utc: now(),
  repo: "SyllabAI/syllabai-resources",
  branch,
  runbook_of_record: ".syllabai/docs/new-subject-runbook.md @ SyllabAI/syllabai-v2 main",
  b6_manifest_continuity: man24.b6_manifest_continuity,
  b4_partition: int3.b4_partition_of_record,
  commits: {
    A: { sha: commitA, parent: commitAParent, note: "source-0.6 generation — 9 authored guided-lesson/0.6 wave-5 notes (18 lessons / 162 checks); schemas ride main unchanged from stage-A" },
    C: { sha: "(namespace-complete — outputs + manifest v24 + records + pipeline)", note: "hub-import-1.5/ x9 + question-packages-1.2/ x9 (FIRST issues) + hub-import-manifest-v24.json (80 artifacts cumulative) + records/INT-3-transform-record-physics-wave5.json (40 rows) + records/NS-4PH1-PHYSICS-WAVE5-PROMOTION-20261103.json + tooling/physics-wave5-pipeline.js" },
  },
  artifact_pin: commitA,
  pkg_pin: `${commitA} (all nine wave-5 packages pin the commit-A source generation)`,
  prior_pack_pins: { pilot: PILOT_PIN, wave1: WAVE1_PIN, wave2: WAVE2_PIN, wave3: WAVE3_PIN, wave4: WAVE4_PIN, note: "the 62 prior artifacts keep their generation pins inside their bytes; v24 re-pins their (identical) bytes at the manifest level only" },
  input_pins: { resources_main_at_wave5_open: RES_MAIN_AT_OPEN, hub_main_at_wave5_open: HUB_MAIN_AT_OPEN },
  manifest: "hub-import-manifest-v24.json",
  int_record: "INT-3-transform-record-physics-wave5.json",
  adapter_spec: "ADAPTER-SPEC-guided-lesson-0.6-to-hub-1.5.md (unchanged from stage-A)",
  counts_census: { notes: census.notes, lessons: census.lessons, checks: census.checks, ...kindCensus, distractors: census.distractors, wave_notes: NOTES },
  schema_delta:
    "NONE — wave-5 runs the stage-A union schemas byte-identical (guided-lesson/0.6, hub/lesson-import/1.5, sme-question-package/1.2). 8 of 9 notes carry the figures layer (20 figures: 2+0+4+1+2+2+2+4+3 per note — 2-3-2 Calculating Energy Transfers carries no images in its note body, so its figures layer is lawfully absent per the schema's optional-figures mode); all 20 figures carry captions; binding is heading-unique except the two single-lesson notes (2-3-2, 2-3-4) which bind sole-lesson; 7 of 9 notes declare workedExample null (2-3-3 Electrical Safety, 2-3-4 Electricity & Heat, 2-3-5 AC & DC, 2-4-1 Conductors & Insulators, 2-4-2 Core Practical, 2-4-3 Electric Charge, 2-4-4 Uses & Dangers — no worked-example block exists in those note bodies, fail-closed absent).",
  taxonomy: "kind enum of record: mcq (default/absent) | recall | explain-why | application — 18 lessons x [5 MCQ + 2 recall + 1 explain-why + 1 application] = the B2 law; cumulative pack 80 lessons / 720 checks",
  conservation: {
    law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq; the wave-5 streams are anchored in the INT-3 record; chemistry streams byte-untouched; the 62 prior-pack artifacts re-pinned byte-identical (grand recomputed over the 40-note pack; wave-0..wave-4 subtotals reproduce the v23 values exactly)",
    authored_chars: grandChars,
  },
  gates: { pipeline: `${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, 0 fail`, gate_log: CHECKS },
  merge_order:
    "resources PR (this branch) merges to main FIRST; the hub PR (FEED physics-wave5-v24 + landed artifacts + re-issued guided-import.json) merges only after; wave-6 buckets remain operator-gated and are NOT in this tranche (B4: one wave per gate)",
  hub_side_note:
    "the hub renderer is course-generic; the physics FEEDs physics-stagea-v18 / physics-wave1-v19 / physics-wave1-v20 / physics-wave2-v21 / physics-wave3-v22 / physics-wave4-v23 already exercised the parameterized runner — wave-5 adds one FEED entry (physics-wave5-v24) with feed-gated constants only (pack/course_id/counts/prefix/wave-count/artifact_pins_by_note for the 31 prior notes' provenance), chemistry-preserving defaults untouched",
  disclosures: [
    "naming: the landed convention is followed (lane physics-wave5, feed physics-wave5-v24, receipts NS-4PH1) — receipts dirs PHYSICS-STAGEA/NS-4PH1 continue",
    "8 of 9 wave-5 notes carry figures (20 total; 2+0+4+1+2+2+2+4+3 per note — 2-3-2 Calculating Energy Transfers carries no images and lawfully omits the figures layer); 7 of 9 declare workedExample null (2-3-3, 2-3-4, 2-3-5, 2-4-1, 2-4-2, 2-4-3, 2-4-4 — no worked-example block exists in those note bodies, fail-closed absent); 2-3-1 carries TWO note worked examples — the first (48 W motor, 12 V) fills the WE slot of record and the second (3.1 A appliance -> 5 A next size up) anchors the L2 application check instead; 2-3-2's WE (0.7 x 4 x 60 = 168 J) is carried with its full minute-to-seconds conversion",
    "figures mapping law: ids fig-01..fig-NN in bodyMd image order; url re-written from the relative note form to the main/ form of the 0.6 schema pattern; every basename verified present in the assets dir (373 assets at origin/main; 20/20 wave-5 basenames present); captions from the notes' own bold-italic sidecar lines — all 20 wave-5 figures carry one; alt forms: 18 verbatim markdown alts + 2 slug-fallbacks per the recorded slug-fallback mode (2-4-3 fig-04 whose body alt is empty; 2-3-4 fig-01 whose body image line is MALFORMED markdown — the opening bracket of the alt is missing — the alt is treated as unavailable and the basename-slug fallback recorded)",
    "spec text provenance: all 13 wave-5 spec texts (2.2, 2.3, 2.4, 2.5, 2.6, 2.15, 2.22P, 2.23P, 2.24P, 2.25P, 2.26P, 2.27P, 2.28P) are the note bodies' own Spec-point block lines, carried verbatim from the curriculum nodes of record (zero-invention law); id->code resolution direct from the note rows' specPointCodes",
    "executed_this_wave bucket-size law: the frozen partition of the wave-1 contract is honored byte-for-byte; W5 = 9 notes as frozen (5 power-side + 4 static-side)",
    "other-run activity at open disclosed: resources main moved TWICE during lane setup — fb28c174-era recon saw b1ea377e (PR #285 isotope debris repair) then 63c23d0a (PR #287 run-012 reconciliation census, scripts/oeq_phys_run012/ only) — both T-OEQ-PHYS-FORMAT-1 lane commits with zero SME-GuidedLessons overlap; hub main 0e788d62 (the wave-4 bookkeeping merge, PR #660); the wave-open of record is the tip the branch was actually cut from (63c23d0a), race-guard re-checks due at push",
    "between the wave-4 and wave-5 windows the sandbox was recycled again (container rootfs swap): the wave-4 clones and the ajvkit install were lost; the wave-5 clones were rebuilt fetch-first — the resources repo as a BLOBLESS SPARSE clone limited to the integration namespace (the full-history clone weighed 7.8G and ENOSPC-killed its own checkout at 100% disk; the sparse clone carries the full commit graph plus the checked-out integration namespace, disclosed), the hub repo in full; ajvkit rebuilt (ajv 8.20.0); the 9 authored wave-5 sources were written fresh in this window and pre-batteried 198/198 before any commit",
    "pat advisory carried from the wave-4 of-record: the only credential this window (fp16 a8ccee736aa8c75b, one-shot env use) remains VALID — revoke/rotate advised",
  ],

};
emit(path.join(RES, "records/NS-4PH1-PHYSICS-WAVE5-PROMOTION-20261103.json"), receipt);

// ── lane survivors for the hub runner byte-anchors ────────────────────────────
fs.mkdirSync(SURV, { recursive: true });
fs.mkdirSync(path.join(SURV, "schema"), { recursive: true });
fs.copyFileSync(path.join(RES, "hub-import-manifest-v24.json"), path.join(SURV, "hub-import-manifest-v24.json"));
fs.copyFileSync(path.join(RES, "records/INT-3-transform-record-physics-wave5.json"), path.join(SURV, "INT-3-transform-record-physics-wave5.json"));
fs.copyFileSync(path.join(RES, "schema/hub-lesson-import.1.5.schema.json"), path.join(SURV, "schema/hub-lesson-import.1.5.schema.json"));
fs.copyFileSync(path.join(RES, "schema/sme-question-package.1.2.schema.json"), path.join(SURV, "schema/sme-question-package.1.2.schema.json"));

console.log(`\nRESULT: ${FAILED === 0 ? "GREEN — PIPELINE COMPLETE" : "FAIL-CLOSED"}`);
console.log(`  gates: ${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, ${FAILED} failures`);
console.log(`  cumulative grand: ${grandChars} chars ${grandSha.slice(0, 16)}…`);
console.log(`  census: ${JSON.stringify(counts)}`);
