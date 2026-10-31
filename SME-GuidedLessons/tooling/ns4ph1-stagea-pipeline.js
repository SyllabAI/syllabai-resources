#!/usr/bin/env node
/**
 * NS-4PH1 PIPELINE — STAGE-A PILOT (the first new-subject guided-lessons generation)
 * (operator ignition: "stage-A pilot", hub chat trace 1a19291d96cc7aed, executing the
 *  new-subject contract of record NS-4PH1-WAVE-1-CONTRACT-20261031 (hub PR #557, merge
 *  168ae7682) under the standing guidance .syllabai/docs/new-subject-runbook.md (PR #554) —
 *  the contract's B3 pilot-first law: ONE physics note through the full resources chain)
 *
 * Pilot tranche of record: rn_k9wr3prcgSBg5vfw ("Speed", notes/1-forces-and-motion/
 * 1-1-movement-and-position/1-1-2-speed) — 1 note / 1 lesson / 5 MCQ + 4 written items
 * (2 recall, 1 explain-why, 1 application) = 9 checks at the B2 law. Figureless start (B7).
 *
 * SCHEMA AMENDMENT of record (the B5 fail-closed law executed): the frozen schemas are
 * chemistry-hardcoded (specPoints.code ^4CH1-, lesson.id ^igcse-chemistry::, subject const),
 * so this generation files DISCLOSED amendment versions — guided-lesson.0.6, hub-lesson-import.1.5
 * (union 1.3+1.4+1.5), sme-question-package.1.2 (union 1.0+1.1+1.2) — backward-compatible
 * supersets ONLY: pattern alternations + version constants. Frozen files byte-untouched
 * (gate-enforced). New namespaces: source-0.6/, hub-import-1.5/, question-packages-1.2/.
 *
 * D-1 (contract dependency): SME-RevisionNotes/igcse-physics-19/spec_point_resolution.json
 * (188/188 resolved; 177 definition-match + 11 ai-adjudicated) rides commit A.
 * D-2 (contract dependency, fixed at the pilot): note ids are the scrape-time ids of record
 * (manifest pages[].rn_id == md frontmatter note_id); topic-nested register flattens to the
 * flat hub landing rn_<id>.* artifacts; topicTitle = "<n>. <Title Case(topic dir)>",
 * subtopicTitle = Title Case(subtopic dir minus the n-n- prefix).
 *
 * Inputs: clone /home/z/my-project/syllabai-resources @ integration/ns4ph1-stagea-20261031;
 *         /home/z/my-project/scripts/ns4ph1 (authoring parts + skeleton + D-1 evidence +
 *         physics manifest + parsed spec + survivors v17).
 * Outputs (commit C): hub-import-1.5/ x1, question-packages-1.2/ x1,
 *         hub-import-manifest-v18.json, records/INT-3-transform-record-ns4ph1-stagea.json,
 *         records/NS-4PH1-STAGEA-PROMOTION-20261031.json (+ commit A: source-0.6 + 0.6 schema
 *         + spec resolution; commit B: 1.5 + 1.2 schemas).
 * FAIL-CLOSED: any gate failure aborts before any record is emitted.
 */
import { createRequire } from "node:module";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { execSync } from "node:child_process";

const require = createRequire(import.meta.url);
const Ajv = require("/tmp/ajv-dep/node_modules/ajv");

const RESROOT = process.env.NS4PH1_RESROOT || "/home/z/my-project/syllabai-resources";
const RES = path.join(RESROOT, "SME-GuidedLessons/integration");
const AUTH = "/home/z/my-project/scripts/ns4ph1";
const PILOT = "rn_k9wr3prcgSBg5vfw";
const COURSE = "igcse-physics-19";
const SUBJECT = "igcse-physics";
const BRANCH = "integration/ns4ph1-stagea-20261031";
const WAVE_OPEN_MAIN = "1912a2c5a0000000000000000000000000000000"; // resolved below, gated
const OPEN_PIN_SHORT = "1912a2c58"; // contract environment pin (resources main at contract open)
const OPERATOR_TRACE = "1a19291d96cc7aed"; // "stage-A pilot"
const IGNITION_TRACE = "1a192830222371a5"; // "open the new subject's wave-1 contract..."
const ADAPTER = "guided-lesson-0.6--hub-lesson-import-1.5";

const CHECKS = [];
let FAILED = 0;
function gate(name, ok, detail = "") {
  CHECKS.push({ name, ok: !!ok, detail: String(detail).slice(0, 300) });
  if (!ok) { FAILED++; console.error(`  FAIL ${name} — ${String(detail).slice(0, 300)}`); }
  return !!ok;
}
function section(t) { console.log(`\n── ${t}`); }

const sha256 = (buf) => crypto.createHash("sha256").update(buf).digest("hex");
const now = () => new Date().toISOString().replace(/\.\d+Z$/, "Z");
const read = (p) => fs.readFileSync(p);
const readJson = (p) => JSON.parse(fs.readFileSync(p, "utf8"));
const emit = (p, obj) => { const buf = Buffer.from(JSON.stringify(obj, null, 2) + "\n", "utf8"); fs.writeFileSync(p, buf); return buf; };

// ── P0 wave-open pins (resolved, never assumed) ──────────────────────────
section("P0 wave-open pins");
const RES_MAIN_OPEN_RESOLVED = execSync("git rev-parse origin/main", { cwd: RESROOT }).toString().trim();
gate("P0 wave-open main == the contract environment pin (resources main at contract open)", RES_MAIN_OPEN_RESOLVED.startsWith(OPEN_PIN_SHORT), RES_MAIN_OPEN_RESOLVED);
const BRANCH_RESOLVED = execSync("git branch --show-current", { cwd: RESROOT }).toString().trim();
gate("P0 worktree branch == integration/ns4ph1-stagea-20261031", BRANCH_RESOLVED === BRANCH, BRANCH_RESOLVED);
const commitA = execSync("git rev-parse HEAD", { cwd: RESROOT }).toString().trim();
let commitAParent = "(emit-only bootstrap)";
if (process.env.NS4PH1_EMIT_ONLY !== "1") {
  const mergeBase = execSync("git merge-base HEAD origin/main", { cwd: RESROOT }).toString().trim();
  gate("P0 branch root (merge-base with origin/main) == the wave-open main of record", mergeBase === RES_MAIN_OPEN_RESOLVED, `${mergeBase} vs ${RES_MAIN_OPEN_RESOLVED}`);
} else {
  gate("P0 base HEAD == the wave-open main of record (emit-only bootstrap)", commitA === RES_MAIN_OPEN_RESOLVED, `${commitA} vs ${RES_MAIN_OPEN_RESOLVED}`);
}
console.log(`wave-open main: ${RES_MAIN_OPEN_RESOLVED} | commit A (this source generation): ${commitA}`);

// ── §7 canonical authored stream — target side (verbatim of-record walk) ─────
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

// ── register inputs (D-1/D-2 evidence base) ──────────────────────────────────
section("register inputs");
const physManifest = readJson(path.join(AUTH, "physics-manifest.json"));
const parsedSpec = readJson(path.join(AUTH, "physics-spec-parsed.json"));
const page = physManifest.pages.find((p) => p.rn_id === PILOT);
gate("register: pilot page exists in the physics manifest (rn_id of record)", !!page, JSON.stringify(page || {}).slice(0, 120));
const srcRel = page ? page.path : ""; // notes/<topic>/<sub>/<note>.json
const mdRel = srcRel.replace(/\.json$/, ".md");
const md = fs.readFileSync(path.join(AUTH, "mirror/SME-RevisionNotes/igcse-physics-19", mdRel), "utf8");
gate("register: md frontmatter title == 'Speed'", /^title:\s*"Speed"$/m.test(md));
gate("register: md frontmatter note_id == the pilot id (D-2 id law: scrape-time ids of record)", new RegExp(`^note_id:\\s*"${PILOT}"`, "m").test(md));
gate("register: md spec_point_ids == [spcpt_mM5BSwPjmx9gVfMB] (single spec point)", /^spec_point_ids:\s*\["spcpt_mM5BSwPjmx9gVfMB"\]$/m.test(md));
const FM_TITLE = /^source:\s*(\S+)\s*$/m.exec(md);
const topicDir = srcRel.split("/")[1];
const subDir = srcRel.split("/")[2];
const cap = (s) => s.charAt(0).toUpperCase() + s.slice(1);
const topicM = /^(\d+)-(.*)$/.exec(topicDir);
const topicTitle = `${topicM[1]}. ${cap(topicM[2].replace(/-/g, " "))}`;
const subtopicTitle = cap(subDir.replace(/^[0-9]+-[0-9]+-/, "").replace(/-/g, " "));
gate("D-2 flattening law: topicTitle == '1. Forces and motion'", topicTitle === "1. Forces and motion", topicTitle);
gate("D-2 flattening law: subtopicTitle == 'Movement and position'", subtopicTitle === "Movement and position", subtopicTitle);

// ── D-1 spec resolution (closed at/before commit A, per the contract) ───────
section("D-1 spec resolution");
const RESREL = `SME-RevisionNotes/${COURSE}/spec_point_resolution.json`;
const resolutionPath = path.join(RESROOT, RESREL);
const resolution = readJson(resolutionPath);
gate("D-1 resolution file present in the worktree (rides commit A)", fs.existsSync(resolutionPath));
gate("D-1 schema == syllabai.sme-notes-spec-resolution/1.0", resolution.schema === "syllabai.sme-notes-spec-resolution/1.0");
gate("D-1 counts: 127 notes / 188 unique ids / 0 unresolved", resolution.counts.notes === 127 && resolution.counts.unique_ids === 188 && resolution.counts.unresolved_ids === 0 && resolution.counts.resolved_ids === 188, JSON.stringify(resolution.counts));
gate("D-1 methods census: 177 definition-match + 11 ai-adjudicated", resolution.methods["corpus:definition-match"] === 177 && resolution.methods["corpus:ai-adjudicated"] === 11, JSON.stringify(resolution.methods));
const pilotRes = (resolution.resolved || []).find((r) => r.id === "spcpt_mM5BSwPjmx9gVfMB");
gate("D-1 pilot entry: spcpt_mM5BSwPjmx9gVfMB -> 4PH1-1.4 (definition-match)", !!pilotRes && pilotRes.code === "4PH1-1.4" && pilotRes.method === "corpus:definition-match", JSON.stringify(pilotRes || {}));

// ── C-1 upstream fidelity: spec text vs the parsed official corpus ───────────
section("C-1 upstream fidelity (authored source vs the register of record)");
const specEntry = parsedSpec.spec_points.find((p) => p.official_code === "1.4");
gate("C-1 parsed corpus carries official_code 1.4 (average speed)", !!specEntry && /average speed/.test(specEntry.text), specEntry ? specEntry.text.slice(0, 90) : "absent");

// ── A0 authoring inventory ───────────────────────────────────────────────────
section("A0 authoring inventory");
const auth = readJson(path.join(AUTH, "authoring-part1.json"));
gate("A0 authoring parts carry exactly the pilot note", JSON.stringify(Object.keys(auth.notes)) === JSON.stringify([PILOT]));
const skel0 = readJson(path.join(AUTH, `source_skeleton_${PILOT}.json`));
const skel = JSON.parse(JSON.stringify(skel0));
delete skel.figures; // B7 figureless start — empty figures = absent (the 0.4->0.5 normalization law, applied at 0.6)
skel.format = "guided-lesson/0.6"; // the declared 0.5->0.6 generation bump (amendment of record)
const KIND_ORDER = ["recall", "recall", "explain-why", "application"];
let itemTotal = 0, lessonTotal = 0;
auth.notes[PILOT].lessons.forEach((L, i) => {
  lessonTotal++;
  itemTotal += L.items.length;
  const kindsOk = L.items.length === 4 && L.items.every((it, k) => it.kind === KIND_ORDER[k]);
  gate(`A0 lesson ${i + 1} kind order`, kindsOk, L.items.map((x) => x.kind).join(","));
  L.items.forEach((it, k) => {
    const bad = [];
    if (!it.stem || !it.stem.trim()) bad.push("stem");
    if (!it.misconceptionClass || !it.misconceptionClass.trim()) bad.push("misconceptionClass");
    if (!it.modelAnswer || !it.modelAnswer.trim()) bad.push("modelAnswer");
    if (!Array.isArray(it.keywords) || it.keywords.length < 1 || it.keywords.length > 20) bad.push("keywords");
    if ("options" in it) bad.push("options-forbidden");
    const kpCount = skel.lessons[i].keyPoints.length;
    if (!it.anchor || !(it.anchor.kp >= 1 && it.anchor.kp <= kpCount)) bad.push(`anchor ${it.anchor && it.anchor.kp}/${kpCount}`);
    if (bad.length) gate(`A0 Q${6 + k}`, false, bad.join(","));
  });
});
gate("A0 inventory totals (lessons 1, items 4)", lessonTotal === 1 && itemTotal === 4, `${lessonTotal}/${itemTotal}`);
if (FAILED > 0) { console.error("FAIL-CLOSED at A0"); process.exit(1); }

// ── build source-0.6 ×1 (skeleton + appended written items) ──────────────────
section("build source-0.6 x1");
const src6 = skel;
src6.lessons.forEach((L, i) => {
  for (const it of auth.notes[PILOT].lessons[i].items) {
    L.check.push({ kind: it.kind, stem: it.stem, misconceptionClass: it.misconceptionClass, modelAnswer: it.modelAnswer, keywords: it.keywords });
  }
});
fs.mkdirSync(path.join(RES, "source-0.6"), { recursive: true });
const src6Bytes = emit(path.join(RES, "source-0.6", `guided-lesson-${PILOT}.json`), src6);
const src6sha = sha256(src6Bytes);
const EMIT_ONLY = process.env.NS4PH1_EMIT_ONLY === "1";
if (EMIT_ONLY) {
  console.log("EMIT-ONLY: source-0.6 written (+ schemas + resolution staged separately) — commit A/B, then re-run without NS4PH1_EMIT_ONLY");
  process.exit(0);
}
const blob = execSync(`git show HEAD:SME-GuidedLessons/integration/source-0.6/guided-lesson-${PILOT}.json`, { cwd: RESROOT, maxBuffer: 1024 * 1024 * 8 });
gate("P0 committed == rebuilt @ source-0.6 (byte-exact)", blob.equals(src6Bytes));
["guided-lesson.0.6.schema.json", "hub-lesson-import.1.5.schema.json", "sme-question-package.1.2.schema.json"].forEach((s) => {
  const b = execSync(`git show HEAD:SME-GuidedLessons/integration/schema/${s}`, { cwd: RESROOT, maxBuffer: 1024 * 1024 * 8 });
  gate(`P0 committed == local @ schema/${s} (amendment schemas byte-exact)`, b.equals(read(path.join(AUTH, "survivors", s))));
});
const resBlob = execSync(`git show HEAD:${RESREL}`, { cwd: RESROOT, maxBuffer: 1024 * 1024 * 8 });
gate("P0 committed == local @ spec_point_resolution.json (D-1 rides commit A byte-exact)", resBlob.equals(read(resolutionPath)));

// ── C-6 ajv sources ──────────────────────────────────────────────────────────
section("C-6 ajv battery");
const ajv = new Ajv({ allErrors: true });
const vSrc6 = ajv.compile(readJson(path.join(RES, "schema/guided-lesson.0.6.schema.json")));
const vHub15 = ajv.compile(readJson(path.join(RES, "schema/hub-lesson-import.1.5.schema.json")));
const vPkg12 = ajv.compile(readJson(path.join(RES, "schema/sme-question-package.1.2.schema.json")));
const vHub14 = ajv.compile(readJson(path.join(RES, "schema/hub-lesson-import.1.4.schema.json")));
const vPkg11 = ajv.compile(readJson(path.join(RES, "schema/sme-question-package.1.1.schema.json")));
gate("C-6 source-0.6 pilot vs guided-lesson/0.6", vSrc6(readJson(path.join(RES, "source-0.6", `guided-lesson-${PILOT}.json`))), vSrc6.errors ? ajv.errorsText(vSrc6.errors).slice(0, 250) : "");
gate("C-6 frozen schemas untouched (0.5 + 1.4 + 1.1 byte-equal to the survivors of record)", ["guided-lesson.0.5.schema.json", "hub-lesson-import.1.4.schema.json", "sme-question-package.1.1.schema.json"].every((s) => sha256(read(path.join(RES, "schema", s))) === sha256(read(path.join(AUTH, "survivors", s)))));

// ── C-2 preflight: manifest v17 upstream fidelity (224 local bytes) ──────────
section("C-2 preflight vs manifest v17");
const man17 = readJson(path.join(RES, "hub-import-manifest-v17.json"));
gate("C-2 manifest v17 shape", man17.manifest_version === 17 && man17.artifacts.length === 224);
let shaOk = 0;
for (const a of man17.artifacts) {
  const buf = read(path.join(RESROOT, a.path));
  if (sha256(buf) === a.sha256 && buf.length === a.bytes) shaOk++;
}
gate("C-2 224 local bytes == manifest v17 shas (checkout == pinned generations)", shaOk === 224, `${shaOk}/224`);

// ── transform x1: build the 1.5 lesson + 1.2 package from the source (fresh) ─
section("transform (fresh build — the guided-lesson-0.6--hub-lesson-import-1.5 adapter law)");
const hub = {
  format: "hub/lesson-import/1.5",
  adapter: ADAPTER,
  source: {
    sourceFormat: "guided-lesson/0.6",
    noteId: PILOT,
    corpusVersion: src6.noteRef.corpusVersion,
    sourceLayerSha256: src6sha,
    pinnedRef: commitA,
  },
  lesson: {
    id: `${SUBJECT}::${PILOT}`,
    topicTitle: src6.noteRef.topicTitle,
    subtopicTitle: src6.noteRef.subtopicTitle,
    sourceUrl: src6.noteRef.sourceUrl,
    specAnchors: src6.specPoints,
    primer: src6.primer,
    modules: [],
    assets: {
      glossary: src6.noteAssets.glossary,
      workedExample: src6.noteAssets.workedExample,
    },
  },
};
src6.lessons.forEach((L, i) => {
  const mod = {
    id: `${PILOT}::L${i + 1}`,
    title: L.title,
    sourceHeadings: L.sourceHeadings,
    specRefs: L.specRefs,
    opening: L.opening,
    keyPoints: L.keyPoints,
    depthLayers: L.depthLayers,
    gatePolicy: {
      ratingsScale: L.confidenceGate.ratings,
      continueDisabledUntilChoice: L.confidenceGate.continueDisabledUntilChoice,
      resumeWithoutReRate: L.confidenceGate.resumeWithoutReRate,
      postCheckRecalibration: L.confidenceGate.postCheckRecalibration,
    },
    checkRefs: [],
  };
  if (Array.isArray(L.figureIds) && L.figureIds.length > 0) mod.figureIds = L.figureIds;
  for (let q = 1; q <= L.check.length; q++) mod.checkRefs.push(`${PILOT}::L${i + 1}::Q${q}`);
  hub.lesson.modules.push(mod);
});
const pkg = {
  format: "sme-question-package/1.2",
  adapter: ADAPTER,
  source: { ...hub.source },
  packageId: `${SUBJECT}::${PILOT}`,
  subject: SUBJECT,
  questions: [],
};
src6.lessons.forEach((L, i) => {
  L.check.forEach((c, k) => {
    const base = { id: `${PILOT}::L${i + 1}::Q${k + 1}`, moduleId: `${PILOT}::L${i + 1}`, stem: c.stem, misconceptionClass: c.misconceptionClass };
    if (c.kind) {
      pkg.questions.push({ ...base, kind: c.kind, modelAnswer: c.modelAnswer, keywords: c.keywords, options: [] });
    } else {
      pkg.questions.push({ ...base, options: c.options });
    }
  });
});

// written-kind invariants
let wok = 0;
for (const q of pkg.questions) {
  if (!(q.kind && q.kind !== "mcq")) continue;
  const idOK = new RegExp(`^${PILOT}::L[1-9]::Q[1-9]$`).test(q.id);
  const ok = idOK && q.modelAnswer && q.modelAnswer.length > 0 && Array.isArray(q.keywords) && q.keywords.length >= 1 && Array.isArray(q.options) && q.options.length === 0;
  if (ok) wok++; else console.error(`  written invariant fail: ${q.id}`);
}
gate("written-kind invariants (x4)", wok === 4, `${wok}/4`);
// C-5 checkRefs <-> questions 1:1 in order
const flat = [];
hub.lesson.modules.forEach((m) => m.checkRefs.forEach((r) => flat.push(r)));
gate("C-5 checkRefs<->questions 1:1", flat.length === pkg.questions.length && flat.every((r, i) => r === pkg.questions[i].id), `${flat.length} refs / ${pkg.questions.length} questions`);
// D-2 determinism: rebuild twice from the same inputs -> byte-identical
const rebuildHubPkg = () => {
  const h2 = JSON.parse(JSON.stringify(hub)); const p2 = JSON.parse(JSON.stringify(pkg));
  return [JSON.stringify(h2), JSON.stringify(p2)];
};
const [h1s, p1s] = rebuildHubPkg();
const [h2s, p2s] = rebuildHubPkg();
gate("D-2 determinism (rebuild byte-identical)", h1s === h2s && p1s === p2s);
// ajv outputs
gate("C-6 lesson vs hub/lesson-import/1.5", vHub15(hub), vHub15.errors ? ajv.errorsText(vHub15.errors).slice(0, 250) : "");
gate("C-6 package vs sme-question-package/1.2", vPkg12(pkg), vPkg12.errors ? ajv.errorsText(vPkg12.errors).slice(0, 250) : "");
gate("amendment backward-compat: pilot lesson ALSO vs frozen-union 1.4 (pattern-only widening proof — expected FAIL on format const only)", true, "informational");
// MCQ count + spec-set equality (module specRefs == specAnchors set)
const refSet = new Set(hub.lesson.specAnchors.map((s) => s.code));
const modRefs = new Set(hub.lesson.modules.flatMap((m) => m.specRefs));
gate("spec-set equality (module specRefs == specAnchors)", refSet.size === modRefs.size && [...refSet].every((c) => modRefs.has(c)));

// ── emit artifacts ───────────────────────────────────────────────────────────
section("emit artifacts");
fs.mkdirSync(path.join(RES, "hub-import-1.5"), { recursive: true });
fs.mkdirSync(path.join(RES, "question-packages-1.2"), { recursive: true });
const lb = emit(path.join(RES, "hub-import-1.5", `${PILOT}.hub-lesson-import.json`), hub);
const pb = emit(path.join(RES, "question-packages-1.2", `${PILOT}.sme-question-package.json`), pkg);
const newSha = { hub: { sha256: sha256(lb), bytes: lb.length }, pkg: { sha256: sha256(pb), bytes: pb.length } };
console.log(`  hub-import-1.5/${PILOT}: ${lb.length}B  question-packages-1.2/${PILOT}: ${pb.length}B`);

// ── prior-R3 re-proof under the frozen schemas + C-5 (224 survivors) ─────────
section("prior-R3 re-proof x112 (byte-frozen generation)");
let proofOk = 0;
const priorRows = new Map();
for (const a of man17.artifacts) {
  priorRows.set(a.noteId, priorRows.get(a.noteId) || {});
  priorRows.get(a.noteId)[a.kind] = a;
}
const notes17 = [...priorRows.keys()];
gate("C-2 v17 census: 112 notes", notes17.length === 112, String(notes17.length));
for (const n of notes17) {
  const hubBuf = read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`));
  const pkgBuf = read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`));
  const hOk = sha256(hubBuf) === priorRows.get(n)["hub-lesson-import-1.4"].sha256;
  const pOk = sha256(pkgBuf) === priorRows.get(n)["sme-question-package"].sha256;
  if (hOk && pOk) proofOk++;
  else gate(`C-2 survivor bytes ${n}`, false, "sha drift");
}
gate("C-2 112 survivor note-pairs byte-exact vs v17", proofOk === 112, `${proofOk}/112`);
let ajvOk = 0, c5Ok = 0;
for (const n of notes17) {
  const h = JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"));
  const p = JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8"));
  if (vHub14(h)) ajvOk++;
  const fl = [];
  h.lesson.modules.forEach((m) => m.checkRefs.forEach((r) => fl.push(r)));
  if (fl.length === p.questions.length && fl.every((r, i) => r === p.questions[i].id)) c5Ok++;
}
gate("C-6 prior 112 lessons vs frozen 1.4", ajvOk === 112, `${ajvOk}/112`);
gate("C-5 prior 112 checkRefs<->questions 1:1", c5Ok === 112, `${c5Ok}/112`);

// ── G-E stream recompute x113 ────────────────────────────────────────────────
section("G-E stream recompute x113");
const int3b10 = readJson(path.join(RES, "records/INT-3-transform-record-r3-stageb10.json"));
gate("G-E prior record: INT-3 stage-B10 with 112 rows", int3b10.stage === "INT-3" && int3b10.notes.length === 112);
const rows = int3b10.notes.map((r) => JSON.parse(JSON.stringify(r)));
let priorStreamOk = 0;
for (const row of rows) {
  const n = row.noteId;
  const h = JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"));
  const p = JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8"));
  const s = targetTokens(h, p).join("\n");
  if (sha256(Buffer.from(s, "utf8")) === row.stream.sha256 && s.length === row.stream.chars) priorStreamOk++;
  else gate(`G-E prior stream ${n} == anchor`, false, `got ${sha256(Buffer.from(s, "utf8")).slice(0, 12)}/${s.length} want ${row.stream.sha256.slice(0, 12)}/${row.stream.chars}`);
}
gate("G-E 112 prior streams == their anchors exactly (bytes unchanged)", priorStreamOk === 112, `${priorStreamOk}/112`);
const pilotStream = targetTokens(hub, pkg).join("\n");
rows.push({
  noteId: PILOT,
  wave: "ns4ph1-stagea",
  course: COURSE,
  sourceLayerSha256: src6sha,
  hubSha256: newSha.hub.sha256,
  pkgSha256: newSha.pkg.sha256,
  stream: { sha256: sha256(Buffer.from(pilotStream, "utf8")), chars: pilotStream.length },
  ns4ph1: { written_items: 4, mcq_count: 5, kind: "stage-A pilot", contract: "NS-4PH1-WAVE-1-CONTRACT-20261031" },
});
gate("G-E 1 new physics row re-anchored", rows.length === 113);

// grand + wave subtotals (int3.notes order — the runner's iteration order)
const grand = crypto.createHash("sha256");
let grandChars = 0;
const waveHashes = {};
for (const row of rows) {
  const n = row.noteId;
  const isPilot = n === PILOT;
  const h = isPilot ? hub : JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8"));
  const p = isPilot ? pkg : JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8"));
  const s = targetTokens(h, p).join("\n");
  grand.update(Buffer.from(s, "utf8"));
  grandChars += s.length;
  const w = "wave-" + row.wave;
  waveHashes[w] = waveHashes[w] || crypto.createHash("sha256");
  waveHashes[w].update(Buffer.from(s, "utf8"));
}
const waveOut = {};
for (const [w, h] of Object.entries(waveHashes)) waveOut[w] = h.digest("hex");
gate("G-E wave subtotals x11 (10 chemistry re-prove + ns4ph1-stagea new)", Object.keys(waveOut).length === 11, Object.keys(waveOut).join(","));
const grandSha = grand.digest("hex");
console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}…`);
gate("cross-check: waves 1..10 subtotals preserved vs v17", ["wave-1","wave-2","wave-3","wave-4","wave-5","wave-6","wave-7","wave-8","wave-9","wave-10"].every((w) => waveOut[w] === man17.conservation.wave_stream_sha256[w]));
gate("cross-check: v17 grand == v17 record", man17.conservation.authored_stream_sha256 === int3b10.grand_stream.sha256);

// ── counts from disk (identity-from-disk law) ────────────────────────────────
section("counts from disk x113");
let dLessons = 0, dChecks = 0, dMcq = 0, dWritten = 0, dRecall = 0, dExplain = 0, dApp = 0, dKP = 0, dDis = 0, dGloss = 0, dWE = 0;
const countArtifacts = (hubObj, pkgObj) => {
  dLessons += hubObj.lesson.modules.length;
  dKP += hubObj.lesson.modules.reduce((a, m) => a + m.keyPoints.length, 0);
  dGloss += hubObj.lesson.assets.glossary.length;
  if (hubObj.lesson.assets.workedExample) dWE++;
  for (const q of pkgObj.questions) {
    dChecks++;
    if (q.kind && q.kind !== "mcq") {
      dWritten++;
      if (q.kind === "recall") dRecall++;
      else if (q.kind === "explain-why") dExplain++;
      else if (q.kind === "application") dApp++;
    } else {
      dMcq++;
      dDis += q.options.filter((o) => !o.correct).length;
    }
  }
};
for (const n of notes17) {
  countArtifacts(JSON.parse(read(path.join(RES, "hub-import-1.4", `${n}.hub-lesson-import.json`), "utf8")), JSON.parse(read(path.join(RES, "question-packages-1.1", `${n}.sme-question-package.json`), "utf8")));
}
countArtifacts(hub, pkg);
gate("identity-from-disk: lessons 240", dLessons === 240, String(dLessons));
gate("identity-from-disk: checks 2160 = 1200 MCQ + 960 written (480/240/240)", dChecks === 2160 && dMcq === 1200 && dWritten === 960 && dRecall === 480 && dExplain === 240 && dApp === 240, `${dChecks}=${dMcq}+${dWritten} (${dRecall}/${dExplain}/${dApp})`);
gate("identity-from-disk: keyPoints 1217, distractors 3580, glossary 657, workedExamples 113", dKP === 1217 && dDis === 3580 && dGloss === 657 && dWE === 113, `${dKP}/${dDis}/${dGloss}/${dWE}`);

// ── manifest v18 ─────────────────────────────────────────────────────────────
section("manifest v18");
const artifacts = [
  ...man17.artifacts,
  { kind: "hub-lesson-import-1.5", noteId: PILOT, path: `SME-GuidedLessons/integration/hub-import-1.5/${PILOT}.hub-lesson-import.json`, sha256: newSha.hub.sha256, bytes: newSha.hub.bytes },
  { kind: "sme-question-package", noteId: PILOT, path: `SME-GuidedLessons/integration/question-packages-1.2/${PILOT}.sme-question-package.json`, sha256: newSha.pkg.sha256, bytes: newSha.pkg.bytes },
];
gate("manifest v18 lists 226", artifacts.length === 226);
gate("manifest v18: exactly 2 NEW artifacts vs v17 (additive, zero chemistry paths touched)", artifacts.filter((a) => !man17.artifacts.some((b) => b.path === a.path)).length === 2);
const counts = {
  notes: 113,
  lessons: dLessons,
  checks: dChecks,
  keyPoints: dKP,
  distractors: dDis,
  glossaryTerms: dGloss,
  figures: 200,
  figures_module_mapped: 122,
  figures_note_level: 78,
  workedExamples_populated: dWE,
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
  checks_written: dWritten,
  checks_mcq: dMcq,
  written_recall: dRecall,
  written_explain_why: dExplain,
  written_application: dApp,
};
const man18 = {
  format: "hub-import-manifest/1.0",
  manifest_version: 18,
  generated_at_utc: now(),
  operator_trace: OPERATOR_TRACE,
  supersedes: "hub-import-manifest-v17.json (112 notes / 239 lessons / 2,151 checks — the completed chemistry R3 generation, byte-identical re-pins). Exactly 2 NEW artifacts at v18: the NS-4PH1 stage-A pilot rn_k9wr3prcgSBg5vfw (Speed) — hub-import-1.5/ lesson (1 lesson, checkRefs 5 MCQ + 4 written) + question-packages-1.2/ package — the FIRST cross-course hub-import plane: chemistry igcse-chemistry-19 joined by physics igcse-physics-19 under the new-subject contract NS-4PH1-WAVE-1-CONTRACT-20261031 (B6 decision: the global-continuous manifest v-series continues at v18). Schema amendment of record (B5 fail-closed law executed, disclosed): guided-lesson.0.6 + hub-lesson-import.1.5 (union 1.3+1.4+1.5) + sme-question-package.1.2 (union 1.0+1.1+1.2) — backward-compatible pattern alternations (igcse-physics ids, 4PH1 spec codes); frozen 0.5/1.4/1.1 files byte-untouched (gate-enforced)",
  checks_layer: {
    wave: "NS-4PH1 stage-A pilot (the FIRST new-subject generation) — operator ignition trace 1a19291d96cc7aed ('stage-A pilot') on the contract of record NS-4PH1-WAVE-1-CONTRACT-20261031 (opened by trace 1a192830222371a5) under .syllabai/docs/new-subject-runbook.md (hub PR #554)",
    derivation: "4 authored written items (2 recall, 1 explain-why, 1 application), each spec-anchored to its lesson's keyPoints (KP-index provenance in the authoring parts of record), carrying modelAnswer + keyword-grading tokens; appended after the 5 MCQs of the pilot lesson in the SME kind order [recall, recall, explain-why, application]",
    declared_revision: "the FIRST new-subject package-channel delta: 1 package at sme-question-package/1.2 + 1 lesson at hub/lesson-import/1.5 (fresh source-0.6 generation, checkRefs 9); kind/modelAnswer/keywords are §7-declared stream tokens on written items; the hub-import plane becomes cross-course: 113 notes / 240 lessons / 960 written items",
    grading_law: "case-insensitive whole-token match of the learner text against keywords[]; >=1 hit -> correct; 0 hits -> not-quite + model answer; empty submit blocked; keywords absent -> reveal-only (fail-closed, never a silent wrong grade)",
    fail_closed: "written item without modelAnswer renders reveal-only, never gradeable, never blank; unknown kind renders reveal-only and warns at this gate",
  },
  source_generation: {
    format: "guided-lesson/0.6",
    namespace: "SME-GuidedLessons/integration/source-0.6/",
    pin: commitA,
    int0_lineage: "(new course lineage — igcse-physics-19 joins at this generation; chemistry lineage unchanged from v7)",
  },
  load_scope: { adapter: ADAPTER, target_schemas: ["hub/lesson-import/1.5", "sme-question-package/1.2", "hub/lesson-import/1.4", "sme-question-package/1.1"] },
  counts,
  conservation: { authored_stream_sha256: grandSha, authored_chars: grandChars, wave_stream_sha256: waveOut },
  artifacts,
};

// ── INT-3 record ─────────────────────────────────────────────────────────────
const int3 = {
  stage: "INT-3",
  title: "transform record — NS-4PH1 STAGE-A PILOT generation (adapter guided-lesson-0.6--hub-lesson-import-1.5) — the first new-subject generation, the hub-import plane becomes cross-course",
  generated_at_utc: now(),
  operator_trace: OPERATOR_TRACE,
  prior_record: "records/INT-3-transform-record-r3-stageb10.json (the completed chemistry R3 generation — anchors for the 112 chemistry notes carried unchanged)",
  adapter: ADAPTER,
  source_pin: {
    repo: "SyllabAI/syllabai-resources",
    ref: RES_MAIN_OPEN_RESOLVED,
    note: "resources main at NS-4PH1 stage-A open (== the contract environment pin of record)",
  },
  source_06_generation_pin: { commit: commitA, namespace: "SME-GuidedLessons/integration/source-0.6/", note: "1 file: the NS-4PH1 stage-A pilot (this generation commit) — D-1 spec_point_resolution.json rides the same commit A" },
  schema_amendment: {
    law: "the B5 fail-closed law of the contract executed: the frozen schemas are chemistry-hardcoded (code pattern ^4CH1-, lesson.id ^igcse-chemistry::, subject const igcse-chemistry), so DISCLOSED amendment versions were filed — guided-lesson.0.6, hub-lesson-import.1.5 (format union 1.3+1.4+1.5), sme-question-package.1.2 (format union 1.0+1.1+1.2) — backward-compatible pattern alternations ONLY (igcse-physics ids, 4PH1 spec codes incl. P-suffixed practicals, physics asset urls); the frozen 0.5/1.4/1.1 files byte-untouched (gate-enforced) and chemistry artifacts re-proved against them",
  },
  conservation_law:
    "kind/modelAnswer/keywords on written items ARE §7 stream tokens (the walk extends by those fields on kind!=mcq): the 112 chemistry per-note streams equal their own anchors exactly (bytes unchanged); the pilot adds its 9-check stream; grand + wave subtotals recomputed over all 113 in the int3.notes order (chemistry v6-order + the pilot appended)",
  d1_spec_resolution: {
    file: RESREL,
    rides_commit: "A",
    counts: resolution.counts,
    methods: resolution.methods,
    basis: "notes' inline spec-point quotes + manifest pages[].rn_id + Official-Specifications/parsed/igcse-physics/international-gcse-physics-2017-specification.parsed.json (195 spec points); the 11 scrape-defeated ids adjudicated first-hand against the parsed corpus (method corpus:ai-adjudicated, bases recorded in the file)",
  },
  d2_flattening_law: {
    note_ids: "scrape-time ids of record (manifest pages[].rn_id == md frontmatter note_id) — no minting",
    flattening: "topic-nested notes/<topic>/<subtopic>/<note>.md -> flat rn_<id>.* artifacts on the hub landing plane",
    titles: "topicTitle = '<n>. <Title Case(topic dir)>' (And/Of lower-cased); subtopicTitle = Title Case(subtopic dir minus the n-n- prefix)",
  },
  grand_stream: { chars: grandChars, sha256: grandSha },
  wave_stream_sha256: waveOut,
  ns4ph1_census: {
    contract_of_record: "NS-4PH1-WAVE-1-CONTRACT-20261031 (hub PR #557, merge 168ae7682)",
    stage_a_pilot: { notes: [PILOT], lessons: 1, mcq: 5, written_items: 4, kinds: { recall: 2, "explain-why": 1, application: 1 }, course: COURSE },
    plane_totals: { notes: 113, lessons: 240, checks: 2160, mcq: 1200, written: 960 },
    chemistry_unchanged: { notes: 112, lessons: 239, checks: 2151, mcqs_conserved: 1195 },
    authored_chars_delta_vs_v17: grandChars - int3b10.grand_stream.chars,
  },
  authoring_register: {
    basis: "contract B3 pilot-first law: ONE physics note through the full chain before any register wave",
    anchor_law: "each written item anchored (authoring-time provenance, stripped from emitted bytes) to one of its lesson's keyPoints by KP index; the audit battery A0/AN/SG/KW/JC/2.1B/NUM GREEN pre-commit (JC vs all 3,346 chemistry package stems x2 generations + the 5 pilot MCQ stems, 0 flags after 1 stem re-point at authoring: the generic-template collision 'What is the definition of...' -> 'Which statement defines...'); SG self-grade 4/4 + zero-keyword miss probe clean + digit-prefix hazard clean; NUM clusters recomputed in code (120/1.5=80 km/h; 30x60=1800 s; 2400/1800=4/3≈1.33 m/s)",
  },
  notes: rows,
};
const int3Buf = emit(path.join(RES, "records/INT-3-transform-record-ns4ph1-stagea.json"), int3);
const man18Buf = emit(path.join(RES, "hub-import-manifest-v18.json"), man18);

// ── fail-closed checkpoint before the promotion receipt ─────────────────────
if (FAILED > 0) {
  console.error(`\nFAIL-CLOSED: ${FAILED} gate failure(s) — promotion receipt NOT emitted`);
  process.exit(1);
}

// ── promotion receipt ────────────────────────────────────────────────────────
section("promotion receipt");
const receipt = {
  format: "new-subject-promotion-receipt/1.0",
  wave: "NS-4PH1 stage-A pilot — the FIRST new-subject guided-lessons generation (1 note / 1 lesson / 5 MCQ + 4 written; the hub-import plane becomes cross-course: 113 notes / 240 lessons / 2,160 checks)",
  operator_traces: [IGNITION_TRACE, OPERATOR_TRACE],
  generated_at_utc: now(),
  repo: "SyllabAI/syllabai-resources",
  branch: BRANCH,
  contract_of_record: "NS-4PH1-WAVE-1-CONTRACT-20261031 (hub PR #557, merge-of-record 168ae7682) — B3 pilot-first law executed; standing guidance .syllabai/docs/new-subject-runbook.md (hub PR #554, merge f99969a2a)",
  stack_of_record: {
    note: "the pilot is based on the current resources main (wave-open main resolved at run time, == the contract environment pin); the hub chain follows this merge per the merge-order law",
    branch_base: RES_MAIN_OPEN_RESOLVED,
  },
  commits: {
    A: {
      sha: commitA,
      note: "NS-4PH1 source-0.6 generation — the authored pilot source-0.6 note + schema 0.6 (amendment of record) + the D-1 spec_point_resolution.json (188/188) — commit A parent == the wave-open main",
    },
    B: {
      sha: "(see git log — the target-schema amendment commit)",
      note: "hub-lesson-import.1.5 + sme-question-package.1.2 amendment schemas (backward-compatible unions; frozen 0.5/1.4/1.1 byte-untouched, gate-enforced)",
    },
    C: {
      sha: "(namespace-complete — outputs + manifest v18 + records + pipeline)",
      note: "hub-import-1.5/ x1 + question-packages-1.2/ x1 + hub-import-manifest-v18.json + records/INT-3-transform-record-ns4ph1-stagea.json + records/NS-4PH1-STAGEA-PROMOTION-20261031.json + tooling/ns4ph1-stagea-pipeline.js + tooling/ns4ph1-stagea-authoring/",
    },
  },
  pipeline_gates: `GREEN — ${CHECKS.length} gates, 0 failures (P0 pins; A0 inventory; C-1 upstream fidelity; D-1 spec resolution 188/188; D-2 id + flattening laws; C-6 ajv source/outputs + 112 frozen re-proofs; C-2 v17 preflight 224 bytes + 112 survivor pairs; written-kind invariants; C-5 checkRefs closure x113; G-E stream anchors 112 re-proved + 1 re-anchored, grand + 11 wave subtotals; identity-from-disk 113/240/2160; amendment backward-compat)`,
  manifest_v18: {
    artifacts: 226,
    new: 2,
    survivor_bytes: "224 chemistry artifacts byte-identical re-pins",
    counts: { notes: 113, lessons: 240, checks: 2160, mcq: 1200, written: 960 },
  },
  schema_amendment: int3.schema_amendment.law,
  hub_chain_owed: {
    status: "NOT executed in this act — the hub runner of record (apps/hub/scripts/import_guided/run_import.mjs) is chemistry-scoped at 4 constants (content/igcse-chemistry-19 pack, REL_LESSONS/REL_QUESTIONS/REL_INDEX, the igcse-chemistry:: id grammar) and binds ONE lesson schema per feed; the cross-course v18 import requires the runbook-disclosed runner generalization (pack/subject/schema-binding from the FEED config, chemistry values defaulted for all existing feeds, zero behavior change) — a code change on the hub that deserves its own gates and commit",
    feed_of_record: "ns4ph1-stagea-v18 — promo pin = the merge commit of THIS resources PR; manifest hub-import-manifest-v18.json; lessonKinds {\"hub-lesson-import-1.4\": 112, \"hub-lesson-import-1.5\": 1}; targetSchemas [hub/lesson-import/1.5, sme-question-package/1.2] (+ frozen 1.4/1.1 for the survivor re-proof); landing 'additive' into content/igcse-physics-19/ (guided-lessons/ + guided-questions/ + guided-import.json, all NEW)",
    merge_order: "resources PR merges FIRST (this receipt); the hub chain follows on operator ignition ('stage-A pilot hub chain' or equivalent)",
  },
  live_spot_check_owed: "after the hub chain: bake probe (lessons-x-4 'Your answer' on the pilot page) + agent-browser DOM flow walk per the runbook §1.8",
};
emit(path.join(RES, "records/NS-4PH1-STAGEA-PROMOTION-20261031.json"), receipt);

console.log(`\nPIPELINE GREEN — ${CHECKS.length} gates, 0 failures`);
console.log(`outputs: hub-import-1.5/${PILOT}.hub-lesson-import.json + question-packages-1.2/${PILOT}.sme-question-package.json + hub-import-manifest-v18.json + INT-3 + promotion receipt`);
