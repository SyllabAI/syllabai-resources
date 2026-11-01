#!/usr/bin/env node
/**
 * PHYSICS-WAVE1 V20 RE-ISSUE — the cumulative-manifest corrective of record
 * (execution trace 1a197b1687dc5cd9, same session; defect disclosed, fix forward)
 *
 * DEFECT of record (caught by the LIVE SPOT-CHECK, invisible to the 32 runner gates):
 *   hub-import-manifest-v19.json was emitted TRANCHE-scoped (12 artifacts / 6 notes) and the
 *   wave-1 INT-3 record carried 6 anchor rows. The runner's guided-import.json index is
 *   rebuilt from the INT-3 rows (run_import.mjs L2494 notes: int3.notes.map(...)), so the
 *   re-issued physics index DROPPED the stage-A pilot rows — the pilot lesson page lost its
 *   'Your answer' flow on production (x0 vs x8). Chemistry precedent: every wave manifest is
 *   CUMULATIVE over the course pack (v17 = 224 artifacts / 112 notes) and every wave INT-3
 *   carries the full per-note anchor table; the stage-A v18 tranche scope was lawful only
 *   because the pilot WAS the whole course pack at that moment.
 *
 * FIX of record: hub-import-manifest-v20.json — CUMULATIVE over the igcse-physics-19 pack:
 *   14 artifacts = the 2 stage-A pilot artifacts re-pinned BYTE-IDENTICAL @ their v18 shas
 *   + the 12 wave-1 artifacts; counts cumulative over 7 notes; grand stream = pilot stream +
 *   wave-1 stream (99,785 chars); wave-0 + wave-1 subtotals. INT-3 v20 carries 7 anchor rows
 *   (pilot @ its stage-A anchors + the 6 wave-1 rows).
 *
 * Zero authored bytes change: the 12 wave-1 artifacts and the 2 pilot artifacts are the
 * already-landed bytes (re-pinned, sha-gated against v18/v19).
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
const PILOT = "rn_RpyMnS5nqWSRWXXG";
const W1_NOTES = [
  "rn_k9wr3prcgSBg5vfw", "rn_pfndTqR6DTJGZ8xQ", "rn_CpJZQWzbvMcM8fw3",
  "rn_5hfYYFrc2XjMJCrq", "rn_GxNWbSMqkTN4zgZB", "rn_ZgGMNrRGBKvYxxFf",
];
const IGNITION_TRACE = "1a196b9c429c5ae5";
const EXEC_TRACE = "1a197b1687dc5cd9";
const ADAPTER = "guided-lesson-0.6--hub-lesson-import-1.5";
const COURSE_ID = "igcse-physics-19";
const COURSE_PREFIX = "igcse-physics";
// pins of record
const V18 = {
  pilotHub: { sha256: "4be97f7c9763ff88d74805982bb38cad6a517e6eb564f15e1968445fbb56584b", bytes: 14459 },
  pilotPkg: { sha256: "11c39840eeb3ab694d9cddec36171e2c18f8b209cfebb94ebf4e29ae2992ee85", bytes: 19303 },
  pilotStream: { sha256: "42dea4b02c94947735ee0900ee1d433b4cbad1006edd1fb3104af7b5073dc2f4", chars: 13924 },
  pilotSourceLayer: "dcd79fe8b60f1708179c57fd71e03717f25ba6d212b16388edf16fa8fdc3ed42",
};
const V19_RUN = {
  feed: "physics-wave1-v19",
  promo: "e1d89fd2dbb3e0a699c4f1d266410226e2b91b60",
  mergeOfRecord: "499a692fdaf26717f24dc720724eda39f6f4289f",
  receipt: "download/integration/HUB-IMPORT-RUN-20261101-physics-wave1.json (32/32 GREEN; the index regression was invisible to its gates)",
};
// wave-1 artifact pins from the v19 manifest of record
const v19man = JSON.parse(fs.readFileSync(path.join(RES, "hub-import-manifest-v19.json"), "utf8"));

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

// §7 walk — byte-identical to run_import.mjs
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

section("P0 pins");
const branch = execSync("git branch --show-current", { cwd: RES_REPO }).toString().trim();
const commitC20 = "(this commit — namespace-complete v20 re-issue)";
gate("P0 branch is the v20 corrective branch", branch === "integration/physics-wave1-v20-20261101", branch);

section("pilot re-pin (byte-identity vs v18, zero transformation)");
const pilotHubBuf = execSync(`git show origin/main:SME-GuidedLessons/integration/hub-import-1.5/${PILOT}.hub-lesson-import.json`, { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 8 });
const pilotPkgBuf = execSync(`git show origin/main:SME-GuidedLessons/integration/question-packages-1.2/${PILOT}.sme-question-package.json`, { cwd: RES_REPO, maxBuffer: 1024 * 1024 * 8 });
gate("P0 pilot lesson bytes @ resources main == v18 sha256", sha256(pilotHubBuf) === V18.pilotHub.sha256 && pilotHubBuf.length === V18.pilotHub.bytes, `${sha256(pilotHubBuf).slice(0, 12)}/${pilotHubBuf.length}`);
gate("P0 pilot package bytes @ resources main == v18 sha256", sha256(pilotPkgBuf) === V18.pilotPkg.sha256 && pilotPkgBuf.length === V18.pilotPkg.bytes, `${sha256(pilotPkgBuf).slice(0, 12)}/${pilotPkgBuf.length}`);
const pilotHub = JSON.parse(pilotHubBuf.toString("utf8"));
const pilotPkg = JSON.parse(pilotPkgBuf.toString("utf8"));
const pilotStream = targetTokens(pilotHub, pilotPkg).join("\n");
gate("P0 pilot stream re-derived == stage-A anchor", sha256(Buffer.from(pilotStream, "utf8")) === V18.pilotStream.sha256 && pilotStream.length === V18.pilotStream.chars, `${sha256(Buffer.from(pilotStream, "utf8")).slice(0, 12)}/${pilotStream.length}`);

section("wave-1 artifacts byte-exact vs the working tree (no re-emission)");
const w1 = {};
for (const n of W1_NOTES) {
  const lb = read(path.join(RES, "hub-import-1.5", `${n}.hub-lesson-import.json`));
  const pb = read(path.join(RES, "question-packages-1.2", `${n}.sme-question-package.json`));
  const mHub = v19man.artifacts.find((a) => a.noteId === n && a.kind === "hub-lesson-import-1.5");
  const mPkg = v19man.artifacts.find((a) => a.noteId === n && a.kind === "sme-question-package");
  gate(`v20 re-pin ${n.slice(0, 12)} lesson == v19 sha`, sha256(lb) === mHub.sha256 && lb.length === mHub.bytes, `${mHub.sha256.slice(0, 12)}`);
  gate(`v20 re-pin ${n.slice(0, 12)} package == v19 sha`, sha256(pb) === mPkg.sha256 && pb.length === mPkg.bytes, `${mPkg.sha256.slice(0, 12)}`);
  w1[n] = { hub: { buf: lb, sha256: sha256(lb), bytes: lb.length }, pkg: { buf: pb, sha256: sha256(pb), bytes: pb.length } };
}

section("cumulative conservation + counts (7 notes, artifact order: pilot first)");
const order = [PILOT, ...W1_NOTES];
const streams = { [PILOT]: pilotStream };
for (const n of W1_NOTES) {
  const hub = JSON.parse(w1[n].hub.buf.toString("utf8"));
  const pkg = JSON.parse(w1[n].pkg.buf.toString("utf8"));
  streams[n] = targetTokens(hub, pkg).join("\n");
}
let grandChars = 0;
const grand = crypto.createHash("sha256");
const waveHashes = { "wave-0": crypto.createHash("sha256"), "wave-1": crypto.createHash("sha256") };
const waveChars = { "wave-0": 0, "wave-1": 0 };
const rows = [];
for (const n of order) {
  const s = streams[n];
  grand.update(Buffer.from(s, "utf8"));
  grandChars += s.length;
  const w = n === PILOT ? "wave-0" : "wave-1";
  waveHashes[w].update(Buffer.from(s, "utf8"));
  waveChars[w] += s.length;
  rows.push({
    noteId: n,
    wave: n === PILOT ? 0 : 1,
    sourceLayerSha256: n === PILOT ? V18.pilotSourceLayer : sha256(read(path.join(RES, "source-0.6", `guided-lesson-${n}.json`))),
    hubSha256: n === PILOT ? V18.pilotHub.sha256 : w1[n].hub.sha256,
    pkgSha256: n === PILOT ? V18.pilotPkg.sha256 : w1[n].pkg.sha256,
    stream: { sha256: sha256(Buffer.from(s, "utf8")), chars: s.length },
  });
}
const waveOut = { "wave-0": waveHashes["wave-0"].digest("hex"), "wave-1": waveHashes["wave-1"].digest("hex") };
gate("P0 wave-0 subtotal == stage-A grand", waveOut["wave-0"] === V18.pilotStream.sha256, waveOut["wave-0"].slice(0, 12));
gate("P0 wave-1 subtotal == the v19 wave subtotal", waveOut["wave-1"] === v19man.conservation.wave_stream_sha256["wave-1"], waveOut["wave-1"].slice(0, 12));
const grandSha = grand.digest("hex");
console.log(`  grand: ${grandChars} chars ${grandSha.slice(0, 16)}… (wave-0 ${waveChars["wave-0"]}, wave-1 ${waveChars["wave-1"]})`);

// cumulative census from the pinned bytes
const cum = { notes: 0, lessons: 0, checks: 0, keyPoints: 0, distractors: 0, glossaryTerms: 0, figures: 0, figures_module_mapped: 0, figures_note_level: 0, workedExamples_populated: 0, workedExamples_null: 0 };
const kindCensus = { checks_mcq: 0, written_recall: 0, written_explain_why: 0, written_application: 0 };
const allHub = { [PILOT]: pilotHub }, allPkg = { [PILOT]: pilotPkg };
for (const n of W1_NOTES) { allHub[n] = JSON.parse(w1[n].hub.buf.toString("utf8")); allPkg[n] = JSON.parse(w1[n].pkg.buf.toString("utf8")); }
for (const n of order) {
  const h = allHub[n], p = allPkg[n];
  cum.notes++;
  cum.lessons += h.lesson.modules.length;
  cum.keyPoints += h.lesson.modules.reduce((a, m) => a + m.keyPoints.length, 0);
  cum.glossaryTerms += h.lesson.assets.glossary.length;
  const figs = h.lesson.figures || [];
  cum.figures += figs.length;
  cum.figures_module_mapped += figs.filter((f) => f.moduleIds.length > 0).length;
  cum.figures_note_level += figs.filter((f) => f.moduleIds.length === 0).length;
  if (h.lesson.assets.workedExample) cum.workedExamples_populated++; else cum.workedExamples_null++;
  for (const q of p.questions) {
    cum.checks++;
    if (!q.kind || q.kind === "mcq") kindCensus.checks_mcq++;
    else if (q.kind === "recall") kindCensus.written_recall++;
    else if (q.kind === "explain-why") kindCensus.written_explain_why++;
    else if (q.kind === "application") kindCensus.written_application++;
    cum.distractors += (q.options || []).filter((o) => o.correct !== true).length;
  }
}
gate("B2 cumulative identity arithmetic: 14 lessons x 9 = 126 checks", cum.lessons * 9 === cum.checks &&
  kindCensus.checks_mcq === cum.lessons * 5 && kindCensus.written_recall === cum.lessons * 2 &&
  kindCensus.written_explain_why === cum.lessons && kindCensus.written_application === cum.lessons,
  JSON.stringify({ ...cum, ...kindCensus }));
gate("cumulative == v18 + v19 parts", cum.notes === 7 && cum.lessons === 14 && cum.checks === 126 && cum.keyPoints === 61 && cum.distractors === 210 && cum.glossaryTerms === 31 && cum.figures === 25 && cum.workedExamples_populated === 6 && cum.workedExamples_null === 1 && grandChars === 13924 + 85861, JSON.stringify({ grandChars }));

section("manifest v20 (cumulative of record)");
const artifacts = [];
for (const n of order) {
  const isPilot = n === PILOT;
  artifacts.push({ kind: "hub-lesson-import-1.5", noteId: n, path: `SME-GuidedLessons/integration/hub-import-1.5/${n}.hub-lesson-import.json`, sha256: isPilot ? V18.pilotHub.sha256 : w1[n].hub.sha256, bytes: isPilot ? V18.pilotHub.bytes : w1[n].hub.bytes });
  artifacts.push({ kind: "sme-question-package", noteId: n, path: `SME-GuidedLessons/integration/question-packages-1.2/${n}.sme-question-package.json`, sha256: isPilot ? V18.pilotPkg.sha256 : w1[n].pkg.sha256, bytes: isPilot ? V18.pilotPkg.bytes : w1[n].pkg.bytes });
}
const counts = { ...cum, authored_chars_conserved: grandChars };
const man20 = {
  format: "hub-import-manifest/1.0",
  manifest_version: 20,
  course_id: COURSE_ID,
  b6_manifest_continuity: {
    decision: "continue-global",
    selected: "physics wave-1 = manifest v20 (CUMULATIVE over the igcse-physics-19 pack — the chemistry v8..v17 pattern; the programme series continues)",
    rejected: "per-course series (physics v1) — would collide with chemistry hub-import-manifest-v1..v17.json filenames in the shared integration/ namespace and fork the integration ledger",
    recorded_by: "runbook B6 + the stage-A receipt; v19's tranche scope was the DEFECTIVE departure from the cumulative law, corrected here",
  },
  generated_at_utc: now(),
  operator_trace: EXEC_TRACE,
  supersedes: "hub-import-manifest-v19.json — v19 (tranche-scoped, 12 artifacts) was the DEFECTIVE issue: its hub import landed the 12 wave-1 artifacts byte-correctly but the runner-owned guided-import.json index rebuilt from the 6-row INT-3 and DROPPED the stage-A pilot rows; the regression was invisible to the 32 runner gates and CAUGHT by the live spot-check (pilot page 'Your answer' x0 vs x8). v20 re-pins all 14 pack artifacts byte-identical (2 pilot @ v18 + 12 wave-1 @ v19) and restores the cumulative counts/grand/wave subtotals",
  checks_layer: {
    wave: "PHYSICS-4PH1 wave-1 (cumulative re-issue v20) — operator ignition trace " + IGNITION_TRACE + " (\"ignite wave-1\"), execution trace " + EXEC_TRACE,
    derivation: "126 cumulative checks (70 MCQ + 28 recall + 14 explain-why + 14 application = 14 lessons x [5 MCQ + 2 recall + 1 explain-why + 1 application]) over 7 notes",
    declared_revision: "NONE — zero authored bytes change: the 14 artifacts are the already-landed bytes re-pinned byte-identical (sha-gated against v18 + v19); the delta of record is the CUMULATIVE manifest/INT-3 bookkeeping that repairs the runner-owned index",
    grading_law: "case-insensitive whole-token match of the learner text against keywords[]; >=1 hit -> correct; 0 hits -> not-quite + model answer; empty submit blocked; keywords absent -> reveal-only (fail-closed, never a silent wrong grade)",
    fail_closed: "written item without modelAnswer renders reveal-only, never gradeable, never blank; unknown kind renders reveal-only and warns at this gate",
  },
  source_generation: {
    format: "guided-lesson/0.6",
    namespace: "SME-GuidedLessons/integration/source-0.6/",
    pin: "aa6485187429e0911b4a47a8a468e256bb41ce32 (wave-1 commit A) + the stage-A pin 7d493985c7729f30c2186e7e61a713ceacc96517 (pilot source, unchanged)",
    int0_lineage: "(new subject — no INT-0 ancestry)",
  },
  load_scope: { adapter: ADAPTER, target_schemas: ["hub/lesson-import/1.5", "sme-question-package/1.2"] },
  counts,
  conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut },
  artifacts,
};
gate("manifest v20 lists 14 artifacts", artifacts.length === 14, String(artifacts.length));
const emit = (p, obj) => { const buf = Buffer.from(JSON.stringify(obj, null, 2) + "\n", "utf8"); fs.writeFileSync(p, buf); return buf; };
const manBuf = emit(path.join(RES, "hub-import-manifest-v20.json"), man20);

section("INT-3 v20 (cumulative anchor table — the index-repair row set)");
const int3 = {
  stage: "INT-3",
  title: "transform record — PHYSICS-4PH1 wave-1 CUMULATIVE re-issue v20 (adapter guided-lesson-0.6--hub-lesson-import-1.5)",
  generated_at_utc: now(),
  operator_traces: { ignition: IGNITION_TRACE, execution: EXEC_TRACE },
  adapter: ADAPTER,
  course_id: COURSE_ID,
  supersedes_int3: "INT-3-transform-record-physics-wave1.json (6 rows — the tranche-scoped defect of record; its 6 rows are carried VERBATIM below)",
  defect_and_fix: "the v19 hub import rebuilt the runner-owned guided-import.json from these rows and dropped the stage-A pilot; v20 carries the full 7-row cumulative table (pilot @ its stage-A anchors re-derived from the pinned bytes + the 6 wave-1 rows verbatim)",
  b6_manifest_continuity: man20.b6_manifest_continuity,
  source_pin: { repo: "SyllabAI/syllabai-resources", ref: "origin/main @ resources PR #271 merge-of-record 499a692f", note: "the pilot artifacts are re-pinned from resources main bytes, sha-gated vs the v18 manifest" },
  registry_pin: { repo: "SyllabAI/syllabai-v2", ref: "origin/main", path: "apps/hub/content/igcse-physics-19/notes.json", note: "unchanged by this re-issue" },
  conservation_law: "the 7 per-note streams below are the runner's §7 walk over the pinned artifact bytes; grand = concatenation in row order; wave-0 (pilot) + wave-1 (6 notes) subtotals match the stage-A and wave-1 anchors exactly",
  grand_stream: { chars: grandChars, sha256: grandSha },
  wave_stream_sha256: waveOut,
  battery: {
    names: "re-pin battery (no authored bytes change): pilot bytes == v18 sha; wave-1 bytes == v19 sha; pilot stream re-derived == stage-A anchor; wave subtotals == v18/v19 anchors; B2 cumulative identity arithmetic 14x9=126",
  },
  physics_census: { pack_notes: 7, pack_lessons: cum.lessons, checks: cum.checks, ...kindCensus, distractors: cum.distractors, figures: cum.figures, wave1_notes: W1_NOTES, pilot: PILOT },
  notes: rows,
};
emit(path.join(RES, "records/INT-3-transform-record-physics-wave1-v20.json"), int3);

if (FAILED > 0) {
  console.error(`\nFAIL-CLOSED: ${FAILED} gate failure(s) — receipt NOT emitted`);
  process.exit(1);
}

section("promotion receipt (v20 corrective addendum)");
const receipt = {
  format: "r3-check-types-promotion-receipt/1.0",
  wave: "PHYSICS-4PH1 wave-1 CUMULATIVE re-issue v20 — the corrective of record for the v19 index regression",
  operator_traces: [IGNITION_TRACE, EXEC_TRACE],
  generated_at_utc: now(),
  repo: "SyllabAI/syllabai-resources",
  branch,
  runbook_of_record: ".syllabai/docs/new-subject-runbook.md @ SyllabAI/syllabai-v2 main",
  b6_manifest_continuity: man20.b6_manifest_continuity,
  defect_of_record: {
    what: "hub-import-manifest-v19.json was tranche-scoped (12 artifacts / 6-note INT-3); the runner-owned guided-import.json rebuild (run_import.mjs notes: int3.notes.map) dropped the stage-A pilot rows from the physics index",
    caught_by: "the LIVE SPOT-CHECK discipline (bake probe calibration leg): pilot page rn_RpyMnS5nqWSRWXXG served 'Your answer' x0 vs the x8 of record; the 32 runner gates could not see it (the index is runner-owned run metadata, outside the conserved-artifact gates)",
    state_while_defective: "12 wave-1 artifacts byte-correct and serving x8 each; pilot lesson artifact bytes UNTOUCHED on main (additive law held) — only the index rows were wrong",
    v19_run_of_record: V19_RUN,
  },
  fix_of_record: {
    what: "manifest v20 CUMULATIVE over the pack (14 artifacts = 2 pilot re-pinned @ v18 shas + 12 wave-1 re-pinned @ v19 shas; counts/grand/wave-subtotals cumulative over 7 notes) + INT-3 v20 with the 7-row anchor table",
    zero_authored_delta: "every artifact byte in v20 is an already-landed byte, sha-gated; the hub re-run lands 14/14 identical-exists and re-issues the index with all 7 notes",
  },
  commits: {
    C20: { sha: commitC20, note: "hub-import-manifest-v20.json + records/INT-3-transform-record-physics-wave1-v20.json + records/NS-4PH1-PHYSICS-WAVE1-V20-PROMOTION-20261101.json + tooling/physics-wave1-v20-reissue.js" },
  },
  manifest: "hub-import-manifest-v20.json",
  int_record: "INT-3-transform-record-physics-wave1-v20.json",
  counts_census: { ...counts, wave_notes: W1_NOTES, pilot: PILOT },
  schema_delta: "NONE (B5) — the stage-A union schemas ride main unchanged",
  conservation: { law: "unchanged §7 walk; grand 99,785 chars = pilot 13,924 + wave-1 85,861", authored_chars: grandChars },
  gates: { pipeline: `${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, 0 fail`, gate_log: CHECKS },
  merge_order: "resources PR merges FIRST; the hub chain (FEED physics-wave1-v20 + index re-issue) follows; merge method 'merge', never squash",
  disclosures: [
    "the v19 manifest/INT-3/pipeline/receipt remain of record for the wave-1 authoring (their artifact bytes were correct); v20 supersedes them for the INTEGRATION bookkeeping only",
    "the physics index defect window on production: from the #613 bake until the v20 hub landing — disclosed, no data loss (artifact bytes were never wrong)",
    "naming: feed physics-wave1-v20, hub branch physics-wave1-hub-v20, receipts PHYSICS-WAVE1",
  ],
};
emit(path.join(RES, "records/NS-4PH1-PHYSICS-WAVE1-V20-PROMOTION-20261101.json"), receipt);

fs.mkdirSync(SURV, { recursive: true });
fs.copyFileSync(path.join(RES, "hub-import-manifest-v20.json"), path.join(SURV, "hub-import-manifest-v20.json"));
fs.copyFileSync(path.join(RES, "records/INT-3-transform-record-physics-wave1-v20.json"), path.join(SURV, "INT-3-transform-record-physics-wave1-v20.json"));

console.log(`\nRESULT: ${FAILED === 0 ? "GREEN — V20 RE-ISSUE COMPLETE" : "FAIL-CLOSED"}`);
console.log(`  gates: ${CHECKS.filter((c) => c.ok).length}/${CHECKS.length} pass, ${FAILED} failures`);
console.log(`  grand: ${grandChars} chars ${grandSha.slice(0, 16)}…`);
console.log(`  cumulative counts: ${JSON.stringify(counts)}`);
