#!/usr/bin/env node
/**
 * build-content-map-external.mjs — T-VIDEOMAP-P2B/P2C/P2D Step 5: emit the
 * OWNER-REVIEWED external-lane drafts into the hub clone as data files.
 *
 * Inputs : Videos/drafts/<course>/video-map.draft.external.json (reviewState
 *          owner-reviewed-external — run apply_self_review.py first) +
 *          owner-review-verdicts.json + the hub clone's spines.
 * Output : <hub>/apps/hub/content/video-map/<course>.json (schema
 *          hub.video-map/1 — ONLY reviewed:true rows) + registry.json update
 *          + flags.json videoMap.courses update.
 *
 * Merge mode: igcse-biology-19 already ships a site-lane map (P2, hub PR
 * #574). Its file is UPDATED: external videos appended (existing site video
 * entries win), approved external mappings appended, review block gains a
 * `lanes` array (site lane untouched, external lane recorded), coverage
 * recomputed over the UNION.
 *
 * Gates (plan §8, adapted): review law (zero reviewed:false in output),
 * referential integrity (every spec code in the spine; ids ^[\w-]{11}$; no
 * duplicate video ids; every mapping.video in videos[]; every external video
 * entry carries provider+watchUrl), coverage census recomputed from the
 * emitted mappings and asserted against the draft — never hand-written.
 *
 * Usage: node build-content-map-external.mjs <hubCloneRoot>
 */

import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { createHash } from "node:crypto";
import { execSync } from "node:child_process";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const VIDEOS = resolve(__dirname, "..");
const HUB = resolve(process.argv[2] || ".");
const MAPDIR = join(HUB, "apps/hub/content/video-map");
const SPINES = join(HUB, "apps/hub/spines");

const sha256 = (p) => createHash("sha256").update(readFileSync(p)).digest("hex");
const REJECTS_OF = (v, task) => (v.rejects || []).map((r) => ({ ...r, lane: task }));

const FRESH = [
  "igcse-chemistry-19", "igcse-physics-19", "igcse-maths-a-18-higher",
  "cie-igcse-biology-23", "cie-igcse-chemistry-23", "cie-igcse-physics-23",
  "cie-a-level-biology-25", "cie-a-level-chemistry-25", "cie-a-level-physics-25",
];
const MERGE = ["igcse-biology-19"];
// P2E: a SECOND external lane (PhysicsOnline) for the three physics courses —
// draft + verdicts live in video-map.draft.external-p2e.json / owner-review-verdicts.p2e.json
const P2E = ["cie-a-level-physics-25", "cie-igcse-physics-23", "igcse-physics-19"];

const errors = [];
const registryPath = join(MAPDIR, "registry.json");
const registry = existsSync(registryPath)
  ? JSON.parse(readFileSync(registryPath, "utf8"))
  : { schema: "syllabai-hub.video-map-registry/1", generatedUtc: "", courses: {} };

for (const course of [...FRESH, ...MERGE]) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external.json"), "utf8"));
  // igcse-biology-19 keeps its P2 site-lane owner-review-verdicts.json untouched;
  // the external-lane verdicts live in owner-review-verdicts.external.json there.
  const vname = MERGE.includes(course) ? "owner-review-verdicts.external.json" : "owner-review-verdicts.json";
  const verdicts = JSON.parse(readFileSync(join(D, vname), "utf8"));
  let p2eDraft = null, p2eVerdicts = null;
  if (P2E.includes(course)) {
    p2eDraft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p2e.json"), "utf8"));
    p2eVerdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p2e.json"), "utf8"));
  }
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );

  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: reviewState is "${draft.reviewState}" — apply review first`);
  if (p2eDraft && p2eDraft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p2e reviewState is "${p2eDraft.reviewState}" — apply review first`);

  let rows = draft.mappings; // extended with site rows (merge mode) and p2e rows below

  // ------------------------------------------------ videos assembly
  let videos, siteMeta = null;
  if (MERGE.includes(course)) {
    // read the PRISTINE site-lane map from origin/main — never this branch's own
    // output (idempotency: the worktree file may already carry merged rows and
    // a merged review block, which would corrupt the lanes/counts)
    const pristine = execSync(
      `git -C "${HUB}" show origin/main:apps/hub/content/video-map/${course}.json`,
      { maxBuffer: 64 * 1024 * 1024 });
    const hubFile = JSON.parse(pristine);
    siteMeta = hubFile;
    const siteIds = new Set(hubFile.videos.map((v) => v.id));
    const ext = draft.videos.filter((v) => !siteIds.has(v.id));
    videos = [...hubFile.videos, ...ext];
    for (const v of ext)
      if (!v.provider || !v.watchUrl) errors.push(`${course}: external video ${v.id} missing provider/watchUrl`);
    // union: site mappings (already owner-reviewed at P2) + approved external rows.
    // Idempotency: if the worktree hub file already carries external rows from a
    // previous emit, drop them here — the draft is the only source for that lane.
    const siteRows = hubFile.mappings.filter((m) => m.method !== "llm-draft-external");
    rows = [...siteRows, ...draft.mappings];
  } else {
    videos = draft.videos;
    for (const v of videos)
      if (!v.provider || !v.watchUrl) errors.push(`${course}: external video ${v.id} missing provider/watchUrl`);
  }
  if (p2eDraft) {
    // second external lane: union videos by id (primary lane's entry wins), append its rows
    const have = new Set(videos.map((v) => v.id));
    for (const v of p2eDraft.videos) {
      if (!have.has(v.id)) { videos.push(v); have.add(v.id); }
      if (!v.provider || !v.watchUrl) errors.push(`${course}: p2e video ${v.id} missing provider/watchUrl`);
    }
    rows = [...rows, ...p2eDraft.mappings];
  }

  // ------------------------------------------------ review-law + integrity gates
  for (const m of rows) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed row leaking into content (${m.video})`);
    if (m.method !== undefined && m.method !== "llm-draft-external")
      errors.push(`${course}: row has unexpected method (${m.video})`);
  }
  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed row leaking into content (${m.video})`);
    if (m.method !== "llm-draft-external")
      errors.push(`${course}: external row missing method (${m.video})`);
    if (m.boardMismatch !== true)
      errors.push(`${course}: external row must carry boardMismatch:true (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad video id ${m.video}`);
    for (const code of m.specs)
      if (!specByCode.has(code)) errors.push(`${course}: spec ${code} not in spine (${m.video})`);
  }
  if (p2eDraft) {
    for (const m of p2eDraft.mappings) {
      if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
        errors.push(`${course}: unreviewed p2e row leaking into content (${m.video})`);
      if (m.method !== "llm-draft-external")
        errors.push(`${course}: p2e row missing method (${m.video})`);
      if (m.boardMismatch !== true)
        errors.push(`${course}: p2e row must carry boardMismatch:true (${m.video})`);
      if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p2e video id ${m.video}`);
      for (const code of m.specs)
        if (!specByCode.has(code)) errors.push(`${course}: p2e spec ${code} not in spine (${m.video})`);
    }
  }
  if (errors.length) break;

  if (new Set(videos.map((v) => v.id)).size !== videos.length)
    errors.push(`${course}: duplicate video ids after assembly`);
  // no duplicate (video, specs) rows across the union
  const seenPairs = new Set();
  for (const m of rows) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (seenPairs.has(k)) errors.push(`${course}: duplicate mapping row ${k}`);
    seenPairs.add(k);
  }
  const videoIds = new Set(videos.map((v) => v.id));
  for (const m of rows)
    if (!videoIds.has(m.video)) errors.push(`${course}: mapping references unknown video ${m.video}`);
  if (errors.length) break;

  // ------------------------------------------------ census (recomputed, asserted)
  const allSpecs = new Set(rows.flatMap((m) => m.specs));
  const mappedVideos = new Set(rows.map((m) => m.video));
  const coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecs.size,
    specPointsUnmapped: specByCode.size - allSpecs.size,
    videosTotal: videos.length,
    videosMapped: mappedVideos.size,
    videosUnmapped: videos.length - mappedVideos.size,
    mappingRows: rows.length,
    byConfidence: {
      high: rows.filter((m) => m.confidence === "high").length,
      medium: rows.filter((m) => m.confidence === "medium").length,
      low: rows.filter((m) => m.confidence === "low").length,
    },
  };
  const dc = draft.coverage;
  {
    // primary-lane census check (both modes: draft.mappings is the external-only primary lane)
    const extRows = draft.mappings;
    const extSpecs = new Set(extRows.flatMap((m) => m.specs));
    if (extSpecs.size !== dc.specPointsDraftedHere || extRows.length !== dc.rows)
      throw new Error(`${course}: census mismatch between draft.coverage and recomputed external rows`);
    if (p2eDraft) {
      const p2eSpecs = new Set(p2eDraft.mappings.flatMap((m) => m.specs));
      if (p2eSpecs.size !== p2eDraft.coverage.specPointsDraftedHere || p2eDraft.mappings.length !== p2eDraft.coverage.rows)
        throw new Error(`${course}: census mismatch between p2e draft.coverage and recomputed rows`);
    }
  }

  // ------------------------------------------------ review provenance
  let review;
  if (siteMeta) {
    // Post-merge re-runs read the MERGED file from origin/main: the site lane then
    // lives in review.lanes[0] and the top-level rows/rejects are the previous
    // UNION — using them as "site" would absorb the external lane and double-count
    // its rejects. Derive the site lane from lanes[0] when present.
    const siteReview = siteMeta.review.lanes ? siteMeta.review.lanes[0] : siteMeta.review;
    const siteRejects = (siteReview.rejects || []).map((r) => ({ ...r, lane: siteReview.task }));
    const extRejects = REJECTS_OF(verdicts, verdicts.task);
    review = {
      ...siteMeta.review,
      lanes: [
        {
          lane: "site (cognito pages)", task: siteReview.task,
          ruling: siteReview.ruling, reviewer: siteReview.reviewer,
          ruledUtc: siteReview.ruledUtc, evidenceBasis: siteReview.evidenceBasis,
          rowsApproved: siteReview.rowsApproved, rowsRejected: siteReview.rowsRejected,
          rejects: siteRejects,
        },
        {
          lane: "external-channels", task: verdicts.task,
          ruling: verdicts.source, reviewer: verdicts.reviewer, ruledUtc: verdicts.ruledUtc,
          evidenceBasis: verdicts.evidenceBasis,
          rowsApproved: draft.mappings.length,
          rowsRejected: extRejects.length,
          rejects: extRejects,
        },
      ],
      rowsApproved: rows.length,
      rowsRejected: siteReview.rowsRejected + extRejects.length,
      rejects: [...siteRejects, ...extRejects],
      selfReviewNote:
        "External lane adjudicated by delegated self-review per owner chat 2026-11-09 "
        + "('For now, approve and review yourself'); site-lane rulings unchanged from the owner's P2 chat ruling.",
    };
  } else {
    const primaryRejects = (verdicts.rejects || []).map(({ lessonRef, video, spec, reason }) => ({ lessonRef, video, spec, reason }));
    review = {
      task: verdicts.task,
      ruledUtc: verdicts.ruledUtc,
      ruling: verdicts.source,
      reviewer: verdicts.reviewer,
      evidenceBasis: verdicts.evidenceBasis,
      rowsApproved: rows.length,
      rowsRejected: primaryRejects.length + (p2eVerdicts ? (p2eVerdicts.rejects || []).length : 0),
      rejects: p2eVerdicts ? [...primaryRejects, ...REJECTS_OF(p2eVerdicts, p2eVerdicts.task)] : primaryRejects,
    };
    if (p2eVerdicts) {
      review.lanes = [
        {
          lane: "external-channels (P2B/P2C/P2D)", task: verdicts.task,
          ruling: verdicts.source, reviewer: verdicts.reviewer, ruledUtc: verdicts.ruledUtc,
          evidenceBasis: verdicts.evidenceBasis,
          rowsApproved: draft.mappings.length, rowsRejected: primaryRejects.length,
          rejects: primaryRejects,
        },
        {
          lane: "external-channels-p2e (physics-online)", task: p2eVerdicts.task,
          ruling: p2eVerdicts.source, reviewer: p2eVerdicts.reviewer, ruledUtc: p2eVerdicts.ruledUtc,
          evidenceBasis: p2eVerdicts.evidenceBasis,
          rowsApproved: p2eDraft.mappings.length, rowsRejected: (p2eVerdicts.rejects || []).length,
          rejects: REJECTS_OF(p2eVerdicts, p2eVerdicts.task),
        },
      ];
      review.selfReviewNote =
        "Both external lanes adjudicated by delegated self-review per owner chat 2026-11-09 "
        + "('For now, approve and review yourself'); the P2E lane adds PhysicsOnline "
        + "(gcsephysicsonline.com + alevelphysicsonline.com) under the same tightened binding rule.";
    }
  }

  const source = siteMeta
    ? {
        ...siteMeta.source,
        external: {
          provider: draft.source.provider,
          method: draft.source.method,
          enumeratedUtc: draft.source.enumeratedUtc,
        },
      }
    : {
        provider: draft.source.provider,
        label: draft.source.label ?? course,
        method: draft.source.method,
        enumeratedUtc: draft.source.enumeratedUtc,
      };
  if (p2eDraft) {
    source.p2e = {
      provider: p2eDraft.source.provider,
      method: p2eDraft.source.method,
      enumeratedUtc: p2eDraft.source.enumeratedUtc,
    };
  }

  const content = {
    schema: "hub.video-map/1",
    course,
    qual: siteMeta ? siteMeta.qual : draft.qual,
    source,
    review,
    videos,
    mappings: rows,
    coverage,
    inputs: {
      spine: { file: `apps/hub/spines/${course}.json`, sha256: sha256(join(SPINES, `${course}.json`)) },
      draft: {
        repo: "SyllabAI/syllabai-resources",
        path: `Videos/drafts/${course}/video-map.draft.external.json`,
        task: verdicts.task,
        reviewAppliedUtc: verdicts.ruledUtc,
      },
      ...(p2eDraft ? {
        p2e: {
          repo: "SyllabAI/syllabai-resources",
          path: `Videos/drafts/${course}/video-map.draft.external-p2e.json`,
          task: p2eVerdicts.task,
          reviewAppliedUtc: p2eVerdicts.ruledUtc,
        },
      } : {}),
    },
    generatedUtc: new Date().toISOString(),
  };
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");

  registry.courses[course] = {
    videos: coverage.videosTotal,
    mapped: coverage.videosMapped,
    shelf: siteMeta ? registry.courses[course]?.shelf ?? "b2-gcse-iedexcel" : null,
    lane: siteMeta ? "site+external-channels" : "external-channels",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();

  console.log(
    `${course}: SHIPPED specs ${coverage.specPointsMapped}/${coverage.specPointsTotal} · videos ${coverage.videosMapped}/${coverage.videosTotal} · rows ${coverage.mappingRows} (${coverage.byConfidence.high}H/${coverage.byConfidence.medium}M/${coverage.byConfidence.low}L) · 0 reviewed:false in content`
  );
}

if (errors.length) {
  console.error("GATE FAILURES:\n" + errors.map((e) => "  - " + e).join("\n"));
  process.exit(1);
}
writeFileSync(registryPath, JSON.stringify(registry, null, 1) + "\n");
console.log(`wrote ${registryPath}`);

// ------------------------------------------------ flags.json videoMap.courses
// Skip-if-current: once P3 landed (PR #906) the status text is live; rewriting
// it on every emit would churn flags.json (and fight the file's \uXXXX escaping).
const flagsPath = join(HUB, "apps/hub/content/flags.json");
const flags = JSON.parse(readFileSync(flagsPath, "utf8"));
const want = ["igcse-biology-19", ...FRESH];
const have = new Set(flags.flags.videoMap.courses);
const coursesCurrent = want.every((c) => have.has(c)) && flags.flags.videoMap.courses.length === want.length;
const statusCurrent = typeof flags.flags.videoMap.status === "string"
  && flags.flags.videoMap.status.startsWith("live (T-VIDEOMAP-P3)");
if (coursesCurrent && statusCurrent) {
  console.log(`flags.json already current (videoMap.courses = ${have.size} courses, status live) — left untouched`);
} else {
  for (const c of want) if (!have.has(c)) flags.flags.videoMap.courses.push(c);
  flags.flags.videoMap.courses.sort();
  flags.flags.videoMap.status =
    "live (T-VIDEOMAP-P3): lib/video-map.ts loader + /courses/[course]/videos lane shipped for the "
    + "courses below (igcse-biology-19 site+external; 9 external-channels courses incl. the CIE A-level trio). "
    + "Links resolve lessonUrl (site lane, Cognito) then watchUrl (external lane, YouTube). Rows are "
    + "owner-reviewed (title-only evidence, confidence + boardMismatch disclosed per row); the loader "
    + "re-filters reviewed:true as defense in depth. One-flip kill unchanged: remove the slug (per-course) "
    + "or the videoMap key (global).";
  writeFileSync(flagsPath, JSON.stringify(flags, null, 1) + "\n");
  console.log(`wrote ${flagsPath} (videoMap.courses now ${flags.flags.videoMap.courses.length} courses)`);
}
