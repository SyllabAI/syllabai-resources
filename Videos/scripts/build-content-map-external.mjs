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
const CONTENT = join(HUB, "apps/hub/content");

const sha256 = (p) => createHash("sha256").update(readFileSync(p)).digest("hex");
const REJECTS_OF = (v, task) => (v.rejects || []).map((r) => ({ ...r, lane: task }));

/**
 * Mirror-drift gate: apps/hub/spines/<course>.json is the emit-time
 * validation reference, apps/hub/content/<course>/curriculum.json is the
 * RENDER plane of record. When the two drift, rows pass every gate here and
 * still join nothing at render time — the exact igcse-chemistry-19 failure
 * (87 rows validated against the stale bare-code mirror while the render
 * spine carried the canonical 4CH1- register: join 0, badge 119/182, every
 * lesson row invisible since the P4 pass). Spec codes were re-issued
 * canonically by the subject-identity lanes; the mirrors must follow. This
 * gate makes any future re-issue a build-time break instead of a silent
 * render void. (igcse-geography-19 drifted the same way; it has no video
 * rows yet, so only the mirror itself was repaired.)
 */
function assertSpineMirror(course, spine) {
  const cf = join(CONTENT, course, "curriculum.json");
  if (!existsSync(cf)) return; // no content-plane curriculum — other gates own that
  const cs = new Set(
    JSON.parse(readFileSync(cf, "utf8")).nodes
      .filter((n) => n.family === "SPEC_POINT").map((n) => n.code)
  );
  const ss = new Set(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => n.code)
  );
  const offenders = [...ss].filter((c) => !cs.has(c));
  if (offenders.length || cs.size !== ss.size)
    errors.push(
      `${course}: SPINE MIRROR DRIFT — apps/hub/spines/${course}.json SPEC_POINT codes differ from ` +
      `apps/hub/content/${course}/curriculum.json (the render plane of record); first offenders: ` +
      `${offenders.slice(0, 3).join(", ")}. Re-sync the spines/ mirror before emitting — rows would ` +
      `pass emit validation and join nothing at render time.`
    );
}

const FRESH = [
  "igcse-chemistry-19", "igcse-physics-19", "igcse-maths-a-18-higher",
  "cie-igcse-biology-23", "cie-igcse-chemistry-23", "cie-igcse-physics-23",
  "cie-a-level-biology-25", "cie-a-level-chemistry-25", "cie-a-level-physics-25",
];
const MERGE = ["igcse-biology-19"];
// P2E: a SECOND external lane (PhysicsOnline) for the three physics courses —
// draft + verdicts live in video-map.draft.external-p2e.json / owner-review-verdicts.p2e.json
const P2E = ["cie-a-level-physics-25", "cie-igcse-physics-23", "igcse-physics-19"];
// P4 scale pass: 8 NEW direct-match external lanes (4 shelf-direct Cognito maths
// + 4 mechanics cross-subject) run the standard fresh path below. The 35 inherit
// courses are NOT drafted per-course: they are derived at build time from the
// committed containment map (drafts/_p4/inheritance-map.json) applied to the
// owner-approved parent rows — no new LLM mapping decisions, derivation itself
// spot-checked (drafts/_p4/owner-review-verdicts.p4-inherit.json).
const P4_FRESH = [
  "cie-igcse-maths-25-extended", "cie-igcse-further-maths-additional-maths-25",
  "igcse-maths-b-16", "igcse-further-maths-19",
  "cie-a-level-maths-20-mechanics", "cie-as-maths-20-mechanics",
  "ial-maths-20-mechanics-1", "ial-maths-20-mechanics-2",
];

const errors = [];
const registryPath = join(MAPDIR, "registry.json");
const registry = existsSync(registryPath)
  ? JSON.parse(readFileSync(registryPath, "utf8"))
  : { schema: "syllabai-hub.video-map-registry/1", generatedUtc: "", courses: {} };

for (const course of [...FRESH, ...MERGE, ...P4_FRESH]) {
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
  assertSpineMirror(course, spine);

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

// ================================================= P5 Cognito completion lane =====
// The unmapped remainder of the Cognito Edu channel pool (208 owner-reviewed
// rows) appended onto the five parent courses whose children inherit below.
// Runs BEFORE the P4 inherit section so child courses cascade through the
// committed containment map with the enriched parent rows (P5 rows are
// medium/low — the title-only posture the inherit gate requires). Second-lane
// shape mirrors P2F: upstream sections rewrite fresh, this section appends,
// a full re-run stays idempotent. Rejected videos stay out of videos[] and
// live in the verdicts ledger (owner-review-verdicts.p5.json).
const P5 = ["cie-a-level-biology-25", "cie-igcse-biology-23", "cie-igcse-chemistry-23", "cie-igcse-physics-23", "igcse-maths-a-18-higher"];
for (const course of P5) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p5.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p5.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p5 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const content = JSON.parse(readFileSync(join(MAPDIR, `${course}.json`), "utf8"));

  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p5 row leaking into content (${m.video})`);
    if (m.method !== "llm-draft-external")
      errors.push(`${course}: p5 row missing method (${m.video})`);
    if (m.boardMismatch !== true)
      errors.push(`${course}: p5 row must carry boardMismatch:true (${m.video})`);
    if (!m.specs || m.specs.length === 0)
      errors.push(`${course}: p5 rows are spec rows — specs must be non-empty (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p5 video id ${m.video}`);
    for (const code of m.specs || [])
      if (!specByCode.has(code)) errors.push(`${course}: p5 spec ${code} not in spine (${m.video})`);
  }
  const haveKeys = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeys.has(k)) errors.push(`${course}: duplicate p5 row across union ${k}`);
    haveKeys.add(k);
  }
  const haveVids = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVids.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p5 video ${v.id} missing provider/watchUrl`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecs = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVids = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecs.size,
    specPointsUnmapped: specByCode.size - allSpecs.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVids.size,
    videosUnmapped: content.videos.length - mappedVids.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p5Lane = {
    lane: "external-channels-p5 (cognito completion)", task: verdicts.task,
    ruling: verdicts.source, reviewer: verdicts.reviewer, ruledUtc: verdicts.ruledUtc,
    evidenceBasis: verdicts.evidenceBasis,
    rowsApproved: draft.mappings.length, rowsRejected: (verdicts.rejects || []).length,
    rejects: REJECTS_OF(verdicts, verdicts.task),
  };
  content.review.lanes = [
    ...(content.review.lanes || [{
      lane: "external-channels (primary)", task: content.review.task,
      ruling: content.review.ruling, reviewer: content.review.reviewer,
      ruledUtc: content.review.ruledUtc, evidenceBasis: content.review.evidenceBasis,
      rowsApproved: content.review.rowsApproved, rowsRejected: content.review.rowsRejected,
      rejects: content.review.rejects || [],
    }]),
    p5Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p5 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p5 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p5.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLane = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLane.includes("p5-cognito") ? baseLane : baseLane + " + p5-cognito",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p5 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} cognito completion rows) · 0 reviewed:false in content`
  );
}

// ================================================= P6 PhysicsOnline completion lane =====
// The unmapped remainder of the PhysicsOnline channel pool (113 owner-reviewed
// rows) appended onto the three physics parent courses whose children inherit
// below. Runs BEFORE the P4 inherit section so child courses cascade through
// the committed containment map with the enriched parent rows (P6 rows are
// medium/low — the title-only posture the inherit gate requires). Second-lane
// shape mirrors P5: upstream sections rewrite fresh, this section appends,
// a full re-run stays idempotent. Rejected videos stay out of videos[] and
// live in the verdicts ledger (owner-review-verdicts.p6.json).
const P6 = ["cie-a-level-physics-25", "cie-igcse-physics-23", "igcse-physics-19"];
for (const course of P6) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p6.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p6.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p6 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const content = JSON.parse(readFileSync(join(MAPDIR, `${course}.json`), "utf8"));

  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p6 row leaking into content (${m.video})`);
    if (m.method !== "llm-draft-external")
      errors.push(`${course}: p6 row missing method (${m.video})`);
    if (m.boardMismatch !== true)
      errors.push(`${course}: p6 row must carry boardMismatch:true (${m.video})`);
    if (!m.specs || m.specs.length === 0)
      errors.push(`${course}: p6 rows are spec rows — specs must be non-empty (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p6 video id ${m.video}`);
    for (const code of m.specs || [])
      if (!specByCode.has(code)) errors.push(`${course}: p6 spec ${code} not in spine (${m.video})`);
  }
  const haveKeysP6 = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP6.has(k)) errors.push(`${course}: duplicate p6 row across union ${k}`);
    haveKeysP6.add(k);
  }
  const haveVidsP6 = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP6.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p6 video ${v.id} missing provider/watchUrl`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP6 = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP6 = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP6.size,
    specPointsUnmapped: specByCode.size - allSpecsP6.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP6.size,
    videosUnmapped: content.videos.length - mappedVidsP6.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p6Lane = {
    lane: "external-channels-p6 (physicsonline completion)", task: verdicts.task,
    ruling: verdicts.source, reviewer: verdicts.reviewer, ruledUtc: verdicts.ruledUtc,
    evidenceBasis: verdicts.evidenceBasis,
    rowsApproved: draft.mappings.length, rowsRejected: (verdicts.rejects || []).length,
    rejects: REJECTS_OF(verdicts, verdicts.task),
  };
  content.review.lanes = [
    ...(content.review.lanes || [{
      lane: "external-channels (primary)", task: content.review.task,
      ruling: content.review.ruling, reviewer: content.review.reviewer,
      ruledUtc: content.review.ruledUtc, evidenceBasis: content.review.evidenceBasis,
      rowsApproved: content.review.rowsApproved, rowsRejected: content.review.rowsRejected,
      rejects: content.review.rejects || [],
    }]),
    p6Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p6 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p6 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p6.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLaneP6 = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP6.includes("p6-physicsonline") ? baseLaneP6 : baseLaneP6 + " + p6-physicsonline",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p6 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} physicsonline completion rows) · 0 reviewed:false in content`
  );
}

// ================================================= P4 inheritance lane =====
// 35 child courses derive their external lane from ONE parent course's
// owner-approved rows via the committed containment map. Child spec -> best
// parent spec at containment >= 0.55 (and >= 3 informative tokens, else the
// match is degenerate); every parent row bound to that parent spec is
// re-emitted against the child spec with method inherited-external.
const inhMap = JSON.parse(readFileSync(join(VIDEOS, "drafts/_p4/inheritance-map.json"), "utf8"));
const inhVerdicts = JSON.parse(readFileSync(join(VIDEOS, "drafts/_p4/owner-review-verdicts.p4-inherit.json"), "utf8"));
for (const [child, entry] of Object.entries(inhMap.parents)) {
  const parent = entry.parent;
  // Parent state is read from the EMITTED parent content file (written by the main
  // loop above): its videos array is the full assembled union (site + external
  // lanes) and its mappings the reviewed union. Only external-method rows are
  // eligible for inheritance; video entries resolve from the union (a P2B external
  // row may legitimately reference a site-lane video entry).
  const pcontent = JSON.parse(readFileSync(join(MAPDIR, `${parent}.json`), "utf8"));
  const prows = pcontent.mappings.filter((r) => r.method === "llm-draft-external");
  const pvideos = [...pcontent.videos];
  for (const r of prows) {
    if (r.reviewed !== true)
      errors.push(`p4-inherit ${child}: parent ${parent} row ${r.video} not reviewed:true`);
    if (r.confidence === "high")
      errors.push(`p4-inherit ${child}: parent ${parent} row ${r.video} is high — title-only posture violated`);
  }
  const spine = JSON.parse(readFileSync(join(SPINES, `${child}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(child, spine);
  for (const cspec of Object.keys(entry.specMap))
    if (!specByCode.has(cspec)) errors.push(`p4-inherit ${child}: specMap code ${cspec} not in child spine`);
  if (errors.length) break;

  // derive: video -> set of child specs triggered via mapped parent specs
  const rowsByVideo = new Map();
  for (const [cspec, m] of Object.entries(entry.specMap)) {
    for (const prow of prows) {
      if (prow.specs.includes(m.parentSpec)) {
        if (!rowsByVideo.has(prow.video)) rowsByVideo.set(prow.video, new Set());
        rowsByVideo.get(prow.video).add(cspec);
      }
    }
  }
  const primaryRow = new Map(prows.map((r) => [r.video, r]));
  const videos = pvideos.filter((v) => rowsByVideo.has(v.id));
  const mappings = [...rowsByVideo.entries()].map(([vid, specs]) => {
    const prow = primaryRow.get(vid) || prows.find((r) => r.video === vid);
    return {
      video: vid, lessonRef: null, lessonUrl: null, specs: [...specs].sort(),
      confidence: prow.confidence === "high" ? "medium" : prow.confidence,
      evidence: prow.evidence
        + ` (inherited from the owner-approved ${parent} external lane via spec-title containment >= ${inhMap.threshold}; Videos/drafts/_p4/inheritance-map.json)`,
      method: "inherited-external", reviewed: true, boardMismatch: true,
      reviewer: inhVerdicts.reviewer, reviewedUtc: inhVerdicts.ruledUtc,
      inherit: { from: parent, threshold: inhMap.threshold, map: "Videos/drafts/_p4/inheritance-map.json" },
    };
  });
  for (const m of mappings) {
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`p4-inherit ${child}: bad video id ${m.video}`);
    if (m.method !== "inherited-external") errors.push(`p4-inherit ${child}: bad method (${m.video})`);
    for (const code of m.specs)
      if (!specByCode.has(code)) errors.push(`p4-inherit ${child}: spec ${code} not in spine (${m.video})`);
  }
  if (new Set(videos.map((v) => v.id)).size !== videos.length)
    errors.push(`p4-inherit ${child}: duplicate video ids`);
  if (errors.length) break;

  const allSpecs = new Set(mappings.flatMap((m) => m.specs));
  const coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecs.size,
    specPointsUnmapped: specByCode.size - allSpecs.size,
    videosTotal: videos.length, videosMapped: videos.length, videosUnmapped: 0,
    mappingRows: mappings.length,
    byConfidence: {
      high: 0,
      medium: mappings.filter((m) => m.confidence === "medium").length,
      low: mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const parentPaths = P2E.includes(parent)
    ? [`Videos/drafts/${parent}/video-map.draft.external.json`, `Videos/drafts/${parent}/video-map.draft.external-p2e.json`]
    : [`Videos/drafts/${parent}/video-map.draft.external.json`];
  const content = {
    schema: "hub.video-map/1",
    course: child,
    qual: pcontent.qual,
    source: {
      provider: `inherited (${pcontent.source.external ? pcontent.source.external.provider : pcontent.source.provider})`,
      label: child,
      method: `deterministic spec-title-containment inheritance (>= ${inhMap.threshold}, min 3 informative tokens) of the owner-approved external-lane rows of ${parent}; map: Videos/drafts/_p4/inheritance-map.json; no new LLM mapping decisions`,
      enumeratedUtc: pcontent.source.external ? pcontent.source.external.enumeratedUtc : pcontent.source.enumeratedUtc,
    },
    review: {
      task: inhVerdicts.task,
      ruledUtc: inhVerdicts.ruledUtc,
      ruling: inhVerdicts.source,
      reviewer: inhVerdicts.reviewer,
      evidenceBasis: inhVerdicts.evidenceBasis,
      rowsApproved: mappings.length,
      rowsRejected: 0,
      rejects: [],
      lanes: [{
        lane: `inherited-external (from ${parent})`, task: inhVerdicts.task,
        ruling: inhVerdicts.source, reviewer: inhVerdicts.reviewer, ruledUtc: inhVerdicts.ruledUtc,
        evidenceBasis: inhVerdicts.evidenceBasis,
        rowsApproved: mappings.length, rowsRejected: 0, rejects: [],
      }],
      selfReviewNote:
        "Inherited rows derive deterministically from owner-approved parent rows; the containment map is "
        + "committed and spot-checked (owner chat 2026-11-09 'approve and review yourself'). The parent "
        + "lanes carry the title-only evidence rulings; below-threshold child specs stay honestly unmapped.",
    },
    videos,
    mappings,
    coverage,
    inputs: {
      spine: { file: `apps/hub/spines/${child}.json`, sha256: sha256(join(SPINES, `${child}.json`)) },
      inheritanceMap: {
        repo: "SyllabAI/syllabai-resources", path: "Videos/drafts/_p4/inheritance-map.json",
        task: inhVerdicts.task, reviewAppliedUtc: inhVerdicts.ruledUtc,
      },
      parentDraft: { repo: "SyllabAI/syllabai-resources", course: parent, paths: parentPaths, task: inhVerdicts.task },
    },
    generatedUtc: new Date().toISOString(),
  };
  writeFileSync(join(MAPDIR, `${child}.json`), JSON.stringify(content, null, 1) + "\n");
  registry.courses[child] = {
    videos: coverage.videosTotal,
    mapped: coverage.videosMapped,
    shelf: null,
    lane: "external-channels (inherited)",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${child}: SHIPPED (inherited from ${parent}) specs ${coverage.specPointsMapped}/${coverage.specPointsTotal} · videos ${coverage.videosMapped}/${coverage.videosTotal} · rows ${coverage.mappingRows} (${coverage.byConfidence.medium}M/${coverage.byConfidence.low}L) · 0 reviewed:false in content`
  );
}

// ================================================= P2F Edexcel-native lane =====
// 4 courses gain ANCHOR rows (docs/ANCHOR-GRANULARITY.md): course-level
// past-paper walkthroughs bound by machine-verified Edexcel paper codes
// (method "paper-code", confidence high, boardMismatch false — same-board) and
// topic-level rows by idf containment (tier 1 >= 3 tokens >= 0.55 medium;
// tier 2 >= 2 idf-distinctive tokens low). Anchor rows carry specs:[] and
// lessonRef:null — ZERO spec weight (accounting rule §4): coverage numerators
// stay lesson-level-only. Appends onto the file the sections above just wrote
// (main loop for igcse-chemistry-19, P4 inherit section for the IAL trio);
// upstream sections always rewrite fresh, so a full re-run stays idempotent.
const P2F = ["ial-biology-18", "ial-chemistry-17", "ial-physics-19", "igcse-chemistry-19"];
const ANCHOR_LEVELS = new Set(["course", "topic", "subtopic", "subject"]);
for (const course of P2F) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p2f.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p2f.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p2f reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const nodeByCode = new Map(spine.curriculum.nodes.map((n) => [n.code, n]));
  const specTotal = spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").length;
  assertSpineMirror(course, spine);
  const content = JSON.parse(readFileSync(join(MAPDIR, `${course}.json`), "utf8"));

  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p2f row leaking into content (${m.video})`);
    if (m.method !== "llm-draft-external" && m.method !== "paper-code")
      errors.push(`${course}: p2f row has unexpected method (${m.video})`);
    if (typeof m.boardMismatch !== "boolean")
      errors.push(`${course}: p2f row must carry boardMismatch — same-board paper-code rows are legitimately false (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p2f video id ${m.video}`);
    const a = m.anchor;
    if (!a || !ANCHOR_LEVELS.has(a.level))
      errors.push(`${course}: p2f row must carry anchor.level in course|topic|subtopic|subject (${m.video})`);
    else if (a.level === "course" && a.ref !== course)
      errors.push(`${course}: p2f course anchor ref must be the course itself (${m.video})`);
    else if (a.level === "topic" || a.level === "subtopic") {
      const n = nodeByCode.get(a.ref);
      if (!n || n.family !== a.level.toUpperCase())
        errors.push(`${course}: p2f anchor ${a.ref} is not a ${a.level.toUpperCase()} node in the spine (${m.video})`);
      if (m.specs.length !== 0 || m.lessonRef != null)
        errors.push(`${course}: p2f anchor rows carry specs:[] and lessonRef:null (${m.video})`);
    }
  }
  const haveKeys = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeys.has(k)) errors.push(`${course}: duplicate p2f row across union ${k}`);
    haveKeys.add(k);
  }
  const haveVids = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVids.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p2f video ${v.id} missing provider/watchUrl`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecs = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVids = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specTotal,
    specPointsMapped: allSpecs.size,
    specPointsUnmapped: specTotal - allSpecs.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVids.size,
    videosUnmapped: content.videos.length - mappedVids.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p2fLane = {
    lane: "external-channels-p2f (edexcel-native anchors)", task: verdicts.task,
    ruling: verdicts.source, reviewer: verdicts.reviewer, ruledUtc: verdicts.ruledUtc,
    evidenceBasis: verdicts.evidenceBasis,
    rowsApproved: draft.mappings.length, rowsRejected: (verdicts.rejects || []).length,
    rejects: REJECTS_OF(verdicts, verdicts.task),
  };
  content.review.lanes = [
    ...(content.review.lanes || [{
      lane: "external-channels (primary)", task: content.review.task,
      ruling: content.review.ruling, reviewer: content.review.reviewer,
      ruledUtc: content.review.ruledUtc, evidenceBasis: content.review.evidenceBasis,
      rowsApproved: content.review.rowsApproved, rowsRejected: content.review.rowsRejected,
      rejects: content.review.rejects || [],
    }]),
    p2fLane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p2f = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p2f = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p2f.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLane = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLane.includes("ednative-p2f") ? baseLane : baseLane + " + ednative-p2f",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p2f specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} anchor rows, zero spec weight) · 0 reviewed:false in content`
  );
}

if (errors.length) {
  console.error("GATE FAILURES:\n" + errors.map((e) => "  - " + e).join("\n"));
  process.exit(1);
}
writeFileSync(registryPath, JSON.stringify(registry, null, 1) + "\n");
console.log(`wrote ${registryPath} (${Object.keys(registry.courses).length} courses)`);

// ------------------------------------------------ flags.json videoMap.courses
// Skip-if-current: once P3 landed (PR #906) the status text is live; rewriting
// it on every emit would churn flags.json (and fight the file's \uXXXX escaping).
const flagsPath = join(HUB, "apps/hub/content/flags.json");
const flags = JSON.parse(readFileSync(flagsPath, "utf8"));
const want = ["igcse-biology-19", ...FRESH, ...P4_FRESH, ...Object.keys(inhMap.parents)];
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
    "live (T-VIDEOMAP-P3+P4): lib/video-map.ts loader + /courses/[course]/videos lane shipped for the "
    + "courses below (igcse-biology-19 site+external; 9 external-channels courses incl. the CIE A-level trio; "
    + "P4 scale pass: 4 shelf-direct Cognito maths lanes, 4 mechanics cross-subject lanes, 35 inherited lanes "
    + "derived from owner-approved parent rows via the committed containment map). "
    + "Links resolve lessonUrl (site lane, Cognito) then watchUrl (external lanes, YouTube). Rows are "
    + "owner-reviewed (title-only evidence, confidence + boardMismatch disclosed per row; inherited rows carry "
    + "their derivation in inherit); the loader re-filters reviewed:true as defense in depth. One-flip kill "
    + "unchanged: remove the slug (per-course) or the videoMap key (global).";
  writeFileSync(flagsPath, JSON.stringify(flags, null, 1) + "\n");
  console.log(`wrote ${flagsPath} (videoMap.courses now ${flags.flags.videoMap.courses.length} courses)`);
}
