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
  // method gate: site rows carry no method; external lanes carry
  // llm-draft-external; the P9+ committed anchor law adds paper-code rows and
  // the P4 inherit lane adds inherited-external rows to shipped MERGE-course
  // files — the pristine-read keeps them and the P15/P16-era wipe-and-re-add
  // sections own their ids, so the gate must tolerate all three (the P15
  // Belal-Sir anchors on this MERGE course tripped the pre-P9 gate in the
  // P16 replay; disclosed builder fix, 2026-11-20).
  for (const m of rows) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed row leaking into content (${m.video})`);
    if (m.method !== undefined && m.method !== "llm-draft-external"
        && m.method !== "paper-code" && m.method !== "inherited-external")
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

// ================================================= P7 remaining channel pools lane =====
// The unmapped remainder of four previously-mined channel pools (amoeba-sisters /
// freesciencelessons / malmesbury-education / doodlescience; P2B/P2C/P2D precedents)
// — 277 owner-reviewed rows onto the 12 science parent courses. The NINE
// non-inherit-child parents append here (BEFORE the P4 inherit loop) so their
// children cascade through the committed containment map; the THREE ial courses
// (ial-biology-18 / ial-chemistry-17 / ial-physics-19) are themselves inherit
// children — their files are rebuilt fresh by the inherit section — so they
// append AFTER it (P7B below, the P2F shape). Rows are medium/low — the
// title-only posture the inherit gate requires. Second-lane shape mirrors P5/P6:
// upstream sections rewrite fresh, this section appends, re-runs stay idempotent.
// Rejected videos stay out of videos[] and live in the verdicts ledger
// (owner-review-verdicts.p7.json).
const P7 = ["cie-a-level-biology-25", "cie-a-level-chemistry-25", "cie-a-level-physics-25",
            "cie-igcse-biology-23", "cie-igcse-chemistry-23", "cie-igcse-physics-23",
            "igcse-biology-19", "igcse-chemistry-19", "igcse-physics-19"];
const P7B = ["ial-biology-18", "ial-chemistry-17", "ial-physics-19"];
for (const course of P7) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p7.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p7.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p7 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const content = JSON.parse(readFileSync(join(MAPDIR, `${course}.json`), "utf8"));

  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p7 row leaking into content (${m.video})`);
    if (m.method !== "llm-draft-external")
      errors.push(`${course}: p7 row missing method (${m.video})`);
    if (m.boardMismatch !== true)
      errors.push(`${course}: p7 row must carry boardMismatch:true (${m.video})`);
    if (!m.specs || m.specs.length === 0)
      errors.push(`${course}: p7 rows are spec rows — specs must be non-empty (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p7 video id ${m.video}`);
    for (const code of m.specs || [])
      if (!specByCode.has(code)) errors.push(`${course}: p7 spec ${code} not in spine (${m.video})`);
  }
  const haveKeysP7 = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP7.has(k)) errors.push(`${course}: duplicate p7 row across union ${k}`);
    haveKeysP7.add(k);
  }
  const haveVidsP7 = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP7.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p7 video ${v.id} missing provider/watchUrl`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP7 = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP7 = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP7.size,
    specPointsUnmapped: specByCode.size - allSpecsP7.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP7.size,
    videosUnmapped: content.videos.length - mappedVidsP7.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p7Lane = {
    lane: "external-channels-p7 (remaining channel pools)", task: verdicts.task,
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
    p7Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p7 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p7 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p7.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLaneP7 = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP7.includes("p7-channel-pools") ? baseLaneP7 : baseLaneP7 + " + p7-channel-pools",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p7 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} remaining-channel-pools rows) · 0 reviewed:false in content`
  );
}

// ================================================= P8 physics-trio honest-empty fill =====
// Owner anchor (chat 2026-11-13): "the ~50 specs still honest-empty on the physics
// trio". A re-adjudication micro-lane: the full 1,136-video pool remainder surfaced
// against the trio EMPTY spec points only (prior lanes adjudicated videos under
// per-course routing where empty-spec targets that lost the routing race were never
// individually dispositioned). 8 owner-reviewed rows fill 6 distinct specs; the
// 610-entry honest reject ledger lives in owner-review-verdicts.p8.json x3. The
// section appends BEFORE the P4 inherit loop (the P5/P6/P7 shape) so the trio's
// children cascade through the committed containment map.
const P8 = ["cie-a-level-physics-25", "cie-igcse-physics-23", "igcse-physics-19"];
for (const course of P8) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p8.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p8.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p8 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const content = JSON.parse(readFileSync(join(MAPDIR, `${course}.json`), "utf8"));

  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p8 row leaking into content (${m.video})`);
    if (m.method !== "llm-draft-external")
      errors.push(`${course}: p8 row missing method (${m.video})`);
    if (m.boardMismatch !== true)
      errors.push(`${course}: p8 row must carry boardMismatch:true (${m.video})`);
    if (!m.specs || m.specs.length === 0)
      errors.push(`${course}: p8 rows are spec rows — specs must be non-empty (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p8 video id ${m.video}`);
    for (const code of m.specs || [])
      if (!specByCode.has(code)) errors.push(`${course}: p8 spec ${code} not in spine (${m.video})`);
  }
  const haveKeysP8 = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP8.has(k)) errors.push(`${course}: duplicate p8 row across union ${k}`);
    haveKeysP8.add(k);
  }
  const haveVidsP8 = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP8.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p8 video ${v.id} missing provider/watchUrl`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP8 = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP8 = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP8.size,
    specPointsUnmapped: specByCode.size - allSpecsP8.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP8.size,
    videosUnmapped: content.videos.length - mappedVidsP8.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p8Lane = {
    lane: "external-channels-p8 (physics-trio honest-empty fill)", task: verdicts.task,
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
    p8Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p8 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p8 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p8.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLaneP8 = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP8.includes("p8-trio-fill") ? baseLaneP8 : baseLaneP8 + " + p8-trio-fill",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p8 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} physics-trio-fill rows) · 0 reviewed:false in content`
  );
}

// ================================================= P9 Mr Hassaan's Maths Channel completion lane =====
// Owner chat 2026-11-13: "There is this channel call Mr Hassan's maths" -> recon ->
// "file as lane P9". The Mr Hassaan's Maths Channel pool (3,150 public uploads,
// 0 overlap with the shipped union) is paper-code native, so the lane runs the
// ANCHOR-GRANULARITY two-tier shape: Tier B course anchors bound by machine-checkable
// paper codes in titles (WMA11-14 -> ial pure 1-4, WME01/WST01, old-register WMA01/02
// C12/C34 spanning two units with one row per anchored course, CIE 9709 session codes
// and textual Paper-NN forms, CIE 0580 extended papers, Edexcel 4MA1/4MB/4PM) with
// method paper-code / confidence high / boardMismatch false / specs [] (zero spec
// weight, §4); Tier A spec rows for the uncoded teaching/tutorial pool under the
// tightened distinctive-token binding rule with a class-table judgment pass over
// every distinctive-candidate row (method llm-draft-external, medium/low,
// boardMismatch true). Honest skips: Edexcel GCE/9MA0 and OCR/AQA/MEI papers (§6 —
// a GCE paper is evidence about the GCE qualification, no such course in the spine),
// CIE O-Level 4037, no-vocabulary misc. This fills the honest-empty maths spine
// courses (ial-maths-20-pure-1..4, statistics-1, the CIE pure/p&s courses) that went
// empty at P4 precisely because no maths channel pool existed. NEW courses (no
// video-map file yet) are created fresh here; existing courses append (the P5 shape).
// Runs BEFORE the P4 inherit loop so 25-extended / a-18-higher children cascade.
// The two inherit-CHILD courses with P9 rows (cie-igcse-maths-25-core,
// igcse-maths-a-modular-24-higher-unit-1) append AFTER the loop in P9B below.
// ial-further-maths-18-further-pure-1 honestly takes 0 rows (all four routed videos
// were IGCSE-textbook misroutes, dropped in judgment — verdicts ledger is the record).
const P9 = [
  "ial-maths-20-pure-1", "ial-maths-20-pure-2", "ial-maths-20-pure-3", "ial-maths-20-pure-4",
  "ial-maths-20-statistics-1", "ial-maths-20-mechanics-1",
  "cie-a-level-maths-20-pure-1", "cie-a-level-maths-20-pure-2", "cie-a-level-maths-20-pure-3",
  "cie-as-maths-20-pure-1", "cie-as-maths-20-pure-2",
  "cie-a-level-maths-20-mechanics", "cie-as-maths-20-mechanics",
  "cie-a-level-maths-20-probability-and-statistics-1", "cie-a-level-maths-20-probability-and-statistics-2",
  "cie-as-maths-20-probability-and-statistics-1",
  "cie-igcse-maths-25-extended", "igcse-maths-a-18-higher", "igcse-maths-b-16", "igcse-further-maths-19",
];
const P9B = ["cie-igcse-maths-25-core", "igcse-maths-a-modular-24-higher-unit-1"];
for (const course of P9) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p9.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p9.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p9 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const contentPath = join(MAPDIR, `${course}.json`);
  let content;
  if (existsSync(contentPath)) {
    content = JSON.parse(readFileSync(contentPath, "utf8"));
    if (!content.review) errors.push(`${course}: existing content file has no review block`);
    if (!content.inputs) errors.push(`${course}: existing content file has no inputs block`);
    if (errors.length) break;
  } else {
    content = {
      schema: "hub.video-map/1",
      course,
      qual: draft.qual,
      source: {
        provider: draft.source.provider,
        label: course,
        method: draft.source.method,
        enumeratedUtc: draft.source.enumeratedUtc,
      },
      review: {
        task: verdicts.task,
        ruledUtc: verdicts.ruledUtc,
        ruling: verdicts.source,
        reviewer: verdicts.reviewer,
        evidenceBasis: verdicts.evidenceBasis,
        rowsApproved: 0,
        rowsRejected: (verdicts.rejects || []).length,
        rejects: REJECTS_OF(verdicts, verdicts.task),
      },
      videos: [],
      mappings: [],
      coverage: null,
      inputs: {
        spine: { file: `apps/hub/spines/${course}.json`, sha256: sha256(join(SPINES, `${course}.json`)) },
      },
      generatedUtc: new Date().toISOString(),
    };
  }

  // idempotency (the P2B law, video-keyed): the draft is the only source for
  // p9 rows — drop prior p9-lane rows (by video id) and the prior p9 lane
  // entry before re-appending, so a re-emit from post-p9 state is a no-op.
  const p9Vids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p9Vids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("mr-hassaans-maths completion")
  );
  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p9 row leaking into content (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p9 video id ${m.video}`);
    if (m.method === "paper-code") {
      if (!m.anchor || m.anchor.level !== "course" || m.anchor.ref !== course)
        errors.push(`${course}: p9 paper-code row must carry anchor{level:course, ref:course} (${m.video})`);
      if (!m.specs || m.specs.length !== 0)
        errors.push(`${course}: p9 anchor rows carry specs:[] — zero spec weight (§4) (${m.video})`);
      if (m.confidence !== "high")
        errors.push(`${course}: p9 paper-code anchor must be high confidence (${m.video})`);
      if (m.boardMismatch !== false)
        errors.push(`${course}: p9 paper-code anchor is same-qualification — boardMismatch must be false (${m.video})`);
      if (m.kind !== "past-paper-walkthrough")
        errors.push(`${course}: p9 anchor row must carry kind past-paper-walkthrough (${m.video})`);
    } else if (m.method === "llm-draft-external") {
      if (!m.specs || m.specs.length === 0)
        errors.push(`${course}: p9 spec rows must carry non-empty specs (${m.video})`);
      if (m.boardMismatch !== true)
        errors.push(`${course}: p9 spec rows carry the title-only posture — boardMismatch must be true (${m.video})`);
      if (m.confidence !== "medium" && m.confidence !== "low")
        errors.push(`${course}: p9 spec rows are medium/low — high would violate the inherit posture (${m.video})`);
      for (const code of m.specs || [])
        if (!specByCode.has(code)) errors.push(`${course}: p9 spec ${code} not in spine (${m.video})`);
    } else {
      errors.push(`${course}: p9 row has unexpected method ${m.method} (${m.video})`);
    }
  }
  const haveKeysP9 = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP9.has(k)) errors.push(`${course}: duplicate p9 row across union ${k}`);
    haveKeysP9.add(k);
  }
  const haveVidsP9 = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP9.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p9 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p9 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP9 = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP9 = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP9.size,
    specPointsUnmapped: specByCode.size - allSpecsP9.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP9.size,
    videosUnmapped: content.videos.length - mappedVidsP9.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p9Lane = {
    lane: "external-channels-p9 (mr-hassaans-maths completion)", task: verdicts.task,
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
    p9Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p9 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p9 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p9.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(contentPath, JSON.stringify(content, null, 1) + "\n");
  const baseLaneP9 = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP9.includes("p9-mrhassans") ? baseLaneP9 : baseLaneP9 + " + p9-mrhassans",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p9 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} mr-hassaans-maths rows) · 0 reviewed:false in content`
  );
}


// ================================================= P10 two-pool maths completion lane =====
// Owner chat 2026-11-13: recon of two maths channels -> "lane P10".
//   MrArnoldsMaths (UCwa84m5RqSJEkP9pYdeDYnw, 437 uploads) + Maths Deity
//   (UCODyYjai6abd1N5KGc1KacQ, 353 uploads), 0 overlap with the shipped union.
// Maths Deity is IAL module-native: Tier B course anchors by machine-checkable
// module codes in titles ("Edexcel IAL P1..P4 <session> Exam Paper", "Practise
// Paper n", "Edexcel style Pn Practise paper", "hardest questions (on|from)
// (Edexcel IAL) Pn/Mn/Sn") with method paper-code / confidence high /
// boardMismatch false / specs [] (zero spec weight, §4); Tier A spec rows from
// the unit.section marker tutorials routed P1-P4 -> pure-1..4, M1/M2 ->
// mechanics-1/2, S1/S2 -> statistics-1/2, FP1 -> further-pure-1, bound by
// explicit-code class tables over the distinctive-token pre-pass; module-
// structured rows may bind at the disclosed higher title-only bar (confidence
// low, P4 cross-subject-style) where the small dense module spines make df<=3
// structurally unable to discriminate. MrArnoldsMaths is a legacy Edexcel
// GCSE/GCE channel: its GCSE-paper and GCE-core pools are honest no-target
// skips (§6 — qualifications not in the spine); its 22 GCSE topic tutorials
// bind Tier A onto igcse-maths-a-18-higher (inherit PARENT — five children
// cascade at build time). Honest no-targets recorded in the route ledger:
// 260 legacy 1MA0 papers, 44 "Core Maths" GCE core-series tutorials, 26 GCE
// C1-C4/applied, 10 other-board, 27 FP2 (no further-pure-2 course in the
// spine, disclosed). NEW courses (statistics-2, further-pure-1) are created
// fresh here; existing courses append (the P5 shape). Runs BEFORE the P4
// inherit loop so a-18-higher children cascade.
const P10 = [
  "ial-maths-20-pure-1", "ial-maths-20-pure-2", "ial-maths-20-pure-3", "ial-maths-20-pure-4",
  "ial-maths-20-mechanics-1", "ial-maths-20-mechanics-2",
  "ial-maths-20-statistics-1", "ial-maths-20-statistics-2",
  "ial-further-maths-18-further-pure-1", "igcse-maths-a-18-higher",
];
for (const course of P10) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p10.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p10.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p10 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const contentPath = join(MAPDIR, `${course}.json`);
  let content;
  if (existsSync(contentPath)) {
    content = JSON.parse(readFileSync(contentPath, "utf8"));
    if (!content.review) errors.push(`${course}: existing content file has no review block`);
    if (!content.inputs) errors.push(`${course}: existing content file has no inputs block`);
    if (errors.length) break;
  } else {
    content = {
      schema: "hub.video-map/1",
      course,
      qual: draft.qual,
      source: {
        provider: draft.source.provider,
        label: course,
        method: draft.source.method,
        enumeratedUtc: draft.source.enumeratedUtc,
      },
      review: {
        task: verdicts.task,
        ruledUtc: verdicts.ruledUtc,
        ruling: verdicts.source,
        reviewer: verdicts.reviewer,
        evidenceBasis: verdicts.evidenceBasis,
        rowsApproved: 0,
        rowsRejected: (verdicts.rejects || []).length,
        rejects: REJECTS_OF(verdicts, verdicts.task),
      },
      videos: [],
      mappings: [],
      coverage: null,
      inputs: {
        spine: { file: `apps/hub/spines/${course}.json`, sha256: sha256(join(SPINES, `${course}.json`)) },
      },
      generatedUtc: new Date().toISOString(),
    };
  }

  // idempotency (the P2B law, video-keyed): the draft is the only source for
  // p10 rows — drop prior p10-lane rows (by video id) and the prior p10 lane
  // entry before re-appending, so a re-emit from post-p10 state is a no-op.
  const p10Vids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p10Vids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("two-pool maths completion")
  );
  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p10 row leaking into content (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p10 video id ${m.video}`);
    if (m.method === "paper-code") {
      if (!m.anchor || m.anchor.level !== "course" || m.anchor.ref !== course)
        errors.push(`${course}: p10 paper-code row must carry anchor{level:course, ref:course} (${m.video})`);
      if (!m.specs || m.specs.length !== 0)
        errors.push(`${course}: p10 anchor rows carry specs:[] — zero spec weight (§4) (${m.video})`);
      if (m.confidence !== "high")
        errors.push(`${course}: p10 paper-code anchor must be high confidence (${m.video})`);
      if (m.boardMismatch !== false)
        errors.push(`${course}: p10 paper-code anchor is same-qualification — boardMismatch must be false (${m.video})`);
      if (m.kind !== "past-paper-walkthrough")
        errors.push(`${course}: p10 anchor row must carry kind past-paper-walkthrough (${m.video})`);
    } else if (m.method === "llm-draft-external") {
      if (!m.specs || m.specs.length === 0)
        errors.push(`${course}: p10 spec rows must carry non-empty specs (${m.video})`);
      if (m.boardMismatch !== true)
        errors.push(`${course}: p10 spec rows carry the title-only posture — boardMismatch must be true (${m.video})`);
      if (m.confidence !== "medium" && m.confidence !== "low")
        errors.push(`${course}: p10 spec rows are medium/low — high would violate the inherit posture (${m.video})`);
      for (const code of m.specs || [])
        if (!specByCode.has(code)) errors.push(`${course}: p10 spec ${code} not in spine (${m.video})`);
    } else {
      errors.push(`${course}: p10 row has unexpected method ${m.method} (${m.video})`);
    }
  }
  const haveKeysP10 = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP10.has(k)) errors.push(`${course}: duplicate p10 row across union ${k}`);
    haveKeysP10.add(k);
  }
  const haveVidsP10 = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP10.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p10 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p10 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP10 = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP10 = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP10.size,
    specPointsUnmapped: specByCode.size - allSpecsP10.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP10.size,
    videosUnmapped: content.videos.length - mappedVidsP10.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p10Lane = {
    lane: "external-channels-p10 (two-pool maths completion: mrarnoldsmaths + mathsdeity)", task: verdicts.task,
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
    p10Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p10 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p10 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p10.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(contentPath, JSON.stringify(content, null, 1) + "\n");
  const baseLaneP10 = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP10.includes("p10-two-pools") ? baseLaneP10 : baseLaneP10 + " + p10-two-pools",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p10 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} two-pool rows) · 0 reviewed:false in content`
  );
}

// ================================================= P11 multi-cluster uncovered-course lane =====
// Owner chat 2026-11-13: recon of 14 channels across the 10 uncovered subject
// clusters -> "lane P11". Fourteen pools (3,116 uploads, 0 overlap with the
// shipped union): EnhanceTuition (CIE 9708 econ + 9706 accounting), Yi
// MakesItEasy (CIE 0460 geo / 0450 business / Further Maths CP1), Cambridge
// IGCSE/AS/A Study Materials (0450 + 0417 chapter series), James Gan (9618 CS +
// 9702 physics + 9709 maths), IGCSE Online (0455/0478/0620/0625/0580 chapter
// series), IGCSE Computer Science (0478 topical), Purple Shirt History (0470),
// Mindful Maths (IAL D1 WDM11 course + WMA11-14/4MA1 paper walkthroughs),
// Cambridge Accounting + AR Accounting (0452/9706), EVM With Dr Mohamed Saber
// (0680), Mr Salles (CIE 0500/0522 English + Edexcel register), The iGCSE
// Geographer (0460). EconplusDal (760, UK GCE econ) is an honest no-target
// pool (no Edexcel econ qualification in the spine, §6, disclosed). 33 Tier B
// syllabus/paper-code anchors (9708/41, 0455/0620 session papers, WDM11,
// WMA11-14, 4MA1) + 583 Tier A spec rows via the distinctive-token pre-pass,
// explicit-code class tables, section-marker narrowing and per-row
// re-adjudication; 439/439 oEmbed author==channel-of-record; honest skips
// 2,466. Three courses re-adjudicated course-level to honest unmapped
// (igcse-history-17, cie-igcse-history-18, igcse-economics-17 — degenerate
// single-token binds on review). NEW uncovered courses are created fresh here;
// existing covered courses append (the P5 shape). Runs BEFORE the P4 inherit
// loop so a-18-higher children cascade; the inherit-child cie-as-physics-25
// appends in P11B after the inherit loop (the P7B shape).
const P11 = [
  "cie-a-level-accounting-21", "cie-a-level-computer-science-19", "cie-a-level-economics-23",
  "cie-a-level-physics-25",
  "cie-as-accounting-21", "cie-as-computer-science-19",
  "cie-igcse-accounting-21", "cie-igcse-accounting-25", "cie-igcse-business-23", "cie-igcse-business-25",
  "cie-igcse-chemistry-23", "cie-igcse-computer-science-23", "cie-igcse-economics-20", "cie-igcse-economics-25",
  "cie-igcse-english-language-20", "cie-igcse-english-language-25", "cie-igcse-environmental-management-25",
  "cie-igcse-geography-20", "cie-igcse-geography-25", "cie-igcse-ict-21", "cie-igcse-physics-23",
  "ial-further-maths-18-further-pure-1", "ial-maths-20-decision-1",
  "ial-maths-20-pure-1", "ial-maths-20-pure-2", "ial-maths-20-pure-3", "ial-maths-20-pure-4",
  "ial-maths-20-statistics-1",
  "igcse-business-19", "igcse-geography-19", "igcse-ict-17", "igcse-maths-a-18-higher",
];
for (const course of P11) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p11.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p11.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p11 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const contentPath = join(MAPDIR, `${course}.json`);
  let content;
  if (existsSync(contentPath)) {
    content = JSON.parse(readFileSync(contentPath, "utf8"));
    if (!content.review) errors.push(`${course}: existing content file has no review block`);
    if (!content.inputs) errors.push(`${course}: existing content file has no inputs block`);
    if (errors.length) break;
  } else {
    content = {
      schema: "hub.video-map/1",
      course,
      qual: draft.qual,
      source: {
        provider: draft.source.provider,
        label: course,
        method: draft.source.method,
        enumeratedUtc: draft.source.enumeratedUtc,
      },
      review: {
        task: verdicts.task,
        ruledUtc: verdicts.ruledUtc,
        ruling: verdicts.source,
        reviewer: verdicts.reviewer,
        evidenceBasis: verdicts.evidenceBasis,
        rowsApproved: 0,
        rowsRejected: (verdicts.rejects || []).length,
        rejects: REJECTS_OF(verdicts, verdicts.task),
      },
      videos: [],
      mappings: [],
      coverage: null,
      inputs: {
        spine: { file: `apps/hub/spines/${course}.json`, sha256: sha256(join(SPINES, `${course}.json`)) },
      },
      generatedUtc: new Date().toISOString(),
    };
  }

  // idempotency (the P2B law, video-keyed): the draft is the only source for
  // p11 rows — drop prior p11-lane rows (by video id) and the prior p11 lane
  // entry before re-appending, so a re-emit from post-p11 state is a no-op.
  const p11Vids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p11Vids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("multi-cluster uncovered-course")
  );
  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p11 row leaking into content (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p11 video id ${m.video}`);
    if (m.method === "paper-code") {
      if (!m.anchor || m.anchor.level !== "course" || m.anchor.ref !== course)
        errors.push(`${course}: p11 paper-code row must carry anchor{level:course, ref:course} (${m.video})`);
      if (!m.specs || m.specs.length !== 0)
        errors.push(`${course}: p11 anchor rows carry specs:[] — zero spec weight (§4) (${m.video})`);
      if (m.confidence !== "high")
        errors.push(`${course}: p11 paper-code anchor must be high confidence (${m.video})`);
      if (m.boardMismatch !== false)
        errors.push(`${course}: p11 paper-code anchor is same-qualification — boardMismatch must be false (${m.video})`);
      if (m.kind !== "past-paper-walkthrough")
        errors.push(`${course}: p11 anchor row must carry kind past-paper-walkthrough (${m.video})`);
    } else if (m.method === "llm-draft-external") {
      if (!m.specs || m.specs.length === 0)
        errors.push(`${course}: p11 spec rows must carry non-empty specs (${m.video})`);
      if (m.boardMismatch !== true)
        errors.push(`${course}: p11 spec rows carry the title-only posture — boardMismatch must be true (${m.video})`);
      if (m.confidence !== "medium" && m.confidence !== "low")
        errors.push(`${course}: p11 spec rows are medium/low — high would violate the inherit posture (${m.video})`);
      for (const code of m.specs || [])
        if (!specByCode.has(code)) errors.push(`${course}: p11 spec ${code} not in spine (${m.video})`);
    } else {
      errors.push(`${course}: p11 row has unexpected method ${m.method} (${m.video})`);
    }
  }
  const haveKeysP11 = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP11.has(k)) errors.push(`${course}: duplicate p11 row across union ${k}`);
    haveKeysP11.add(k);
  }
  const haveVidsP11 = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP11.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p11 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p11 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP11 = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP11 = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP11.size,
    specPointsUnmapped: specByCode.size - allSpecsP11.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP11.size,
    videosUnmapped: content.videos.length - mappedVidsP11.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p11Lane = {
    lane: "external-channels-p11 (multi-cluster uncovered-course lane: fourteen channel pools)", task: verdicts.task,
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
    p11Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p11 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p11 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p11.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(contentPath, JSON.stringify(content, null, 1) + "\n");
  const baseLaneP11 = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP11.includes("p11-multicluster") ? baseLaneP11 : baseLaneP11 + " + p11-multicluster",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p11 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} multi-cluster rows) · 0 reviewed:false in content`
  );
}

// ================================================= P12 narrow CIE cluster lane =====
// Owner chat 2026-11-13: "run P12" after the P11 exit census left 16 honest-empty
// courses. Narrow scope per the owner-approved recommendation: hunt ONLY the
// clusters where CIE-native channels plausibly exist — 9609 AS+A business (2
// courses), 9696 A-level geography, 8291 AS environmental management, 8021 AS
// general paper — and DECLARE the Edexcel English/history/accounting/econ units
// and RS terminal honest-empty. Eleven pools (3,642 uploads, 0 overlap with the
// shipped union): Cambridge Business Essentials, BizEdMadeSimple, Alt Academy,
// The Teaching Student (9609), The Geography Academy (9696 structured unit
// course), Virtual Pathways + Polymath Institute (8291), Mini Lessons, English
// with Ms Irum, Ace The Exam, Miss Cutu (8021). 6 Tier B session/paper-code
// anchors (9609/42|22|12 O/N/26 predictions; 8021 GP session papers) + 113 Tier A
// spec rows via the deduped distinctive-token rule and the four-gate topic-lecture
// class (verbatim / multi-uniq / title-token / title-pair — full-topic lectures bind
// their topic's SPEC_POINTs as ONE multi-spec row at confidence low, disclosed per
// row); N.M section-marker narrowing; oEmbed 119/119 author_url == channel-of-record;
// honest skips 304 (technique/guidance registers, generic mentions, out-of-lane
// IGCSE registers, channel-internal unit numbering). Degenerate single-generic-token
// binds ("issues"/"changing"/"rural") re-adjudicated to honest skips on review.
// NEW uncovered courses created fresh here (the P11 shape); runs BEFORE the P4
// inherit loop; no P12B post-inherit section (no inherit-child takes P12 rows).
const P12 = [
  "cie-as-business-23", "cie-a-level-business-23", "cie-a-level-geography-21",
  "cie-as-environmental-management-20", "cie-as-english-general-paper-21",
];
for (const course of P12) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p12.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p12.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p12 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const contentPath = join(MAPDIR, `${course}.json`);
  let content;
  if (existsSync(contentPath)) {
    content = JSON.parse(readFileSync(contentPath, "utf8"));
    if (!content.review) errors.push(`${course}: existing content file has no review block`);
    if (!content.inputs) errors.push(`${course}: existing content file has no inputs block`);
    if (errors.length) break;
  } else {
    content = {
      schema: "hub.video-map/1",
      course,
      qual: draft.qual,
      source: {
        provider: draft.source.provider,
        label: course,
        method: draft.source.method,
        enumeratedUtc: draft.source.enumeratedUtc,
      },
      review: {
        task: verdicts.task,
        ruledUtc: verdicts.ruledUtc,
        ruling: verdicts.source,
        reviewer: verdicts.reviewer,
        evidenceBasis: verdicts.evidenceBasis,
        rowsApproved: 0,
        rowsRejected: (verdicts.rejects || []).length,
        rejects: REJECTS_OF(verdicts, verdicts.task),
      },
      videos: [],
      mappings: [],
      coverage: null,
      inputs: {
        spine: { file: `apps/hub/spines/${course}.json`, sha256: sha256(join(SPINES, `${course}.json`)) },
      },
      generatedUtc: new Date().toISOString(),
    };
  }

  // idempotency (the P2B law, video-keyed): the draft is the only source for
  // p12 rows — drop prior p12-lane rows (by video id) and the prior p12 lane
  // entry before re-appending, so a re-emit from post-p12 state is a no-op.
  const p12Vids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p12Vids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("narrow CIE cluster lane")
  );
  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p12 row leaking into content (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p12 video id ${m.video}`);
    if (m.method === "paper-code") {
      if (!m.anchor || m.anchor.level !== "course" || m.anchor.ref !== course)
        errors.push(`${course}: p12 paper-code row must carry anchor{level:course, ref:course} (${m.video})`);
      if (!m.specs || m.specs.length !== 0)
        errors.push(`${course}: p12 anchor rows carry specs:[] — zero spec weight (§4) (${m.video})`);
      if (m.confidence !== "high")
        errors.push(`${course}: p12 paper-code anchor must be high confidence (${m.video})`);
      if (m.boardMismatch !== false)
        errors.push(`${course}: p12 paper-code anchor is same-qualification — boardMismatch must be false (${m.video})`);
      if (m.kind !== "past-paper-walkthrough")
        errors.push(`${course}: p12 anchor row must carry kind past-paper-walkthrough (${m.video})`);
    } else if (m.method === "llm-draft-external") {
      if (!m.specs || m.specs.length === 0)
        errors.push(`${course}: p12 spec rows must carry non-empty specs (${m.video})`);
      if (m.boardMismatch !== true)
        errors.push(`${course}: p12 spec rows carry the title-only posture — boardMismatch must be true (${m.video})`);
      if (m.confidence !== "medium" && m.confidence !== "low")
        errors.push(`${course}: p12 spec rows are medium/low — high would violate the inherit posture (${m.video})`);
      for (const code of m.specs || [])
        if (!specByCode.has(code)) errors.push(`${course}: p12 spec ${code} not in spine (${m.video})`);
    } else {
      errors.push(`${course}: p12 row has unexpected method ${m.method} (${m.video})`);
    }
  }
  const haveKeysP12 = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP12.has(k)) errors.push(`${course}: duplicate p12 row across union ${k}`);
    haveKeysP12.add(k);
  }
  const haveVidsP12 = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP12.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p12 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p12 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP12 = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP12 = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP12.size,
    specPointsUnmapped: specByCode.size - allSpecsP12.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP12.size,
    videosUnmapped: content.videos.length - mappedVidsP12.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p12Lane = {
    lane: "external-channels-p12 (narrow CIE cluster lane: 9609 business / 9696 geography / 8291 EM / 8021 GP)", task: verdicts.task,
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
    p12Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p12 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p12 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p12.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(contentPath, JSON.stringify(content, null, 1) + "\n");
  const baseLaneP12 = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP12.includes("p12-cie-narrow") ? baseLaneP12 : baseLaneP12 + " + p12-cie-narrow",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p12 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} narrow-cluster rows) · 0 reviewed:false in content`
  );
}

// ================================================= P13 Alt Academy family lane =====
// Owner chat 2026-11-14: "file it as lane P13". One brand, nine channels: the CAIE-native
// multi-subject hub @altacademyorg (UCTgPevMIji1ZyP4IPhmwDsQ, 685 uploads) plus eight
// subject channels (chemistry 22, economics 78, maths 77, physics 47, biology 9,
// psychology 14, accounting 53; the business subject channel IS the P12 pool — 75 — not
// re-inventoried). 985 uploads, 0 intra-family overlap, 0 overlap with the shipped union.
// 24 Tier B session/paper-code anchors (CIE paper-number routing per subject: maths
// P1/P2/P3/P4(M1)/P5(S1)/P6(S2), sciences papers 1-3 AS / 4-5 A2, econ/accounting/business
// by paper level; maths shared units anchored to BOTH the AS and A-level course) + 626
// Tier A spec rows: the dominant class is the section-name binding — the Alt Academy format
// "Topic | Section | register" names the syllabus section verbatim in a pipe-field, and
// that TOPIC/SUBTOPIC's SPEC_POINTs bind as ONE multi-spec row at confidence low (verbatim
// field-equality gate, node norm >= 8 chars, SUBTOPIC preferred); four-gate topic lectures
// (verbatim/multi-uniq/title-token/title-pair), N.M section-marker narrowing,
// distinctive-token binds (df<=3) and maths unit-token routing (S2/S1/M1/P1/P2/P3 to the
// spine's unit courses, shared units bound to BOTH the AS and A-level course) complete the
// ladder. oEmbed 587/587 author_url == channel-of-record (0 mismatch, 0 dead). Honest
// skips 310 (guidance/advice/marketing registers, the O-Level register, meta videos, CIE
// 9990 psychology — no spine course, honest no-target — and 2 degenerate generic-token
// binds re-adjudicated to skips on review). 17 pre-inherit courses here; the AS inherit
// children with direct rows (cie-as-chemistry-25, cie-as-physics-25) append in P13B after
// the inherit loop (the P11B shape).
const P13 = [
  "cie-a-level-accounting-21", "cie-a-level-biology-25", "cie-a-level-business-23",
  "cie-a-level-chemistry-25", "cie-a-level-economics-23",
  "cie-a-level-maths-20-mechanics", "cie-a-level-maths-20-probability-and-statistics-1",
  "cie-a-level-maths-20-probability-and-statistics-2", "cie-a-level-maths-20-pure-1",
  "cie-a-level-maths-20-pure-3", "cie-a-level-physics-25",
  "cie-as-accounting-21", "cie-as-business-23",
  "cie-as-maths-20-mechanics", "cie-as-maths-20-probability-and-statistics-1",
  "cie-as-maths-20-pure-1", "cie-as-maths-20-pure-2",
];
for (const course of P13) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p13.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p13.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p13 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const contentPath = join(MAPDIR, `${course}.json`);
  if (!existsSync(contentPath))
    throw new Error(`${course}: p13 targets only existing covered courses — content file missing`);
  const content = JSON.parse(readFileSync(contentPath, "utf8"));
  if (!content.review) errors.push(`${course}: existing content file has no review block`);
  if (!content.inputs) errors.push(`${course}: existing content file has no inputs block`);
  if (errors.length) break;

  // idempotency (the P2B law, video-keyed): the draft is the only source for
  // p13 rows — drop prior p13-lane rows (by video id) and the prior p13 lane
  // entry before re-appending, so a re-emit from post-p13 state is a no-op.
  const p13Vids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p13Vids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("Alt Academy family lane")
  );
  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p13 row leaking into content (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p13 video id ${m.video}`);
    if (m.method === "paper-code") {
      if (!m.anchor || m.anchor.level !== "course" || m.anchor.ref !== course)
        errors.push(`${course}: p13 paper-code row must carry anchor{level:course, ref:course} (${m.video})`);
      if (!m.specs || m.specs.length !== 0)
        errors.push(`${course}: p13 anchor rows carry specs:[] — zero spec weight (§4) (${m.video})`);
      if (m.confidence !== "high")
        errors.push(`${course}: p13 paper-code anchor must be high confidence (${m.video})`);
      if (m.boardMismatch !== false)
        errors.push(`${course}: p13 paper-code anchor is same-qualification — boardMismatch must be false (${m.video})`);
      if (m.kind !== "past-paper-walkthrough")
        errors.push(`${course}: p13 anchor row must carry kind past-paper-walkthrough (${m.video})`);
    } else if (m.method === "llm-draft-external") {
      if (!m.specs || m.specs.length === 0)
        errors.push(`${course}: p13 spec rows must carry non-empty specs (${m.video})`);
      if (m.boardMismatch !== true)
        errors.push(`${course}: p13 spec rows carry the title-only posture — boardMismatch must be true (${m.video})`);
      if (m.confidence !== "medium" && m.confidence !== "low")
        errors.push(`${course}: p13 spec rows are medium/low — high would violate the inherit posture (${m.video})`);
      for (const code of m.specs || [])
        if (!specByCode.has(code)) errors.push(`${course}: p13 spec ${code} not in spine (${m.video})`);
    } else {
      errors.push(`${course}: p13 row has unexpected method ${m.method} (${m.video})`);
    }
  }
  const haveKeysP13 = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP13.has(k)) errors.push(`${course}: duplicate p13 row across union ${k}`);
    haveKeysP13.add(k);
  }
  const haveVidsP13 = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP13.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p13 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p13 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP13 = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP13 = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP13.size,
    specPointsUnmapped: specByCode.size - allSpecsP13.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP13.size,
    videosUnmapped: content.videos.length - mappedVidsP13.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p13Lane = {
    lane: "external-channels-p13 (Alt Academy family lane: 9701/9708/9709/9702/9700/9706/9609 CIE-native hub + 8 subject channels)", task: verdicts.task,
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
    p13Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p13 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p13 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p13.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(contentPath, JSON.stringify(content, null, 1) + "\n");
  const baseLaneP13 = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP13.includes("p13-alt-academy") ? baseLaneP13 : baseLaneP13 + " + p13-alt-academy",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p13 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} alt-academy rows) · 0 reviewed:false in content`
  );
}

// ================================================= P14 channel recon judgment lane =====
// Owner chat 2026-11-16 (the ~31-channel recon) -> 2026-11-17 "Proceed" (= file it as
// P14) -> 2026-11-17 "run the P14 judgment lane". Twelve judgment pools (T1 x10 + T2 x2,
// 18,005 of the 24,395 uploads inventoried at filing; 0 overlap with the shipped union and
// all prior lane inventories) + the Allery-CIE re-adjudication group (41 candidates
// REPRODUCED over the P2F pool of record, 26 shipped). 3,138 owner-reviewed rows onto 34
// courses: 1,012 Tier B paper-code anchors (method paper-code, high, boardMismatch false,
// zero spec weight) + 2,126 spec rows (the P13 ladder extended: section-marker N.M,
// verbatim section-name binding over pipe/dash fields, distinctive-token df<=3, four-gate
// topic lectures; 255 medium / 1,871 low). Laws of record added on top of the P13 ladder:
// CIE paper-number routing incl. the compact ON/MJ/FM session forms and the 9701_w23_qp_42
// paper-store pattern (sciences 1-3 AS / 4-5 A2; 9618 1-2 AS / 3-4 A-level); 0580 papers
// 2/4 -> extended, 1/3 -> core (the P9 law; Zainematics spine-code precedence over O-Level
// branding — 405/411 + 188/188 dual-coded titles route, the O-Level-only remainder skips);
// WMA01 C12/C34 IAL-legacy composites -> two units each (124 ExamSolutions anchors); IAL
// chemistry "Unit N <session>" unit-paper anchors (the P11 W-code analog — 73 Assil
// anchors onto ial-chemistry-17, the spine's biggest deficit at 44/319). ExamSolutions
// bare GCE session walkthroughs SKIP per ANCHOR-GRANULARITY section 6 (the P9 precedent —
// no GCE course in the spine; ~4,500 honest skips). Mega Lecture no-code "AS/A2 <subject>"
// class series routes under the P13 register law (promo strings riding on teaching titles
// do NOT trip the guidance gate). CK / Sir Faizan no-code 9702 teaching series route by
// pool-level physics register (recon-approved). IGCSESUCCESS FLE 0500 register rows bind
// the english-language-20/25 pair; the 0475 literature series is RESERVED (9 titles,
// pending the owner lit-21 decision) — not routed, not skipped. Identity: oEmbed
// 2,900/2,900 unique videos author_url == channel-of-record (0 mismatch, 0 dead; 1
// thumbnail-liveness fallback per the P2D law — XrTzkSfaJBI, oEmbed 401, thumb 200).
// Honest skips 21,527 ledgered by class; every one of the 24,486 dispositions
// (18,046 judgment-pool + 41 Allery + 6,390 NT pool-level + 9 reserved) appears exactly
// once (0 routed-vs-skip collisions, machine-checked in the judgment run). 29 courses
// append here BEFORE the P4 inherit loop (their parent rows cascade); the five P4
// inherit CHILDREN with direct P14 rows (cie-as-biology-25, cie-as-chemistry-25,
// cie-as-physics-25, cie-igcse-maths-25-core, ial-chemistry-17 — scripts/p14/
// p14-courses.json is the committed partition of record) append AFTER the loop in P14B
// below (the P11B/P13B shape).
const P14 = [
  "cie-a-level-biology-25", "cie-a-level-chemistry-25", "cie-a-level-computer-science-19",
  "cie-a-level-maths-20-mechanics", "cie-a-level-maths-20-probability-and-statistics-1",
  "cie-a-level-maths-20-probability-and-statistics-2", "cie-a-level-maths-20-pure-1",
  "cie-a-level-maths-20-pure-3", "cie-a-level-physics-25",
  "cie-as-computer-science-19", "cie-as-maths-20-mechanics",
  "cie-as-maths-20-probability-and-statistics-1", "cie-as-maths-20-pure-1",
  "cie-as-maths-20-pure-2", "cie-igcse-chemistry-23", "cie-igcse-computer-science-23",
  "cie-igcse-english-language-20", "cie-igcse-english-language-25",
  "cie-igcse-further-maths-additional-maths-25", "cie-igcse-maths-25-extended",
  "cie-igcse-physics-23", "ial-maths-20-pure-1", "ial-maths-20-pure-2",
  "ial-maths-20-pure-3", "ial-maths-20-pure-4", "igcse-biology-19", "igcse-chemistry-19",
  "igcse-maths-a-18-higher", "igcse-physics-19",
];
const P14_LANE_NAME = "external-channels-p14 (channel recon judgment lane: ETphysics 9702 session walkthroughs; Prosperity Academy CIE SOLVED 9702/9701/9700; Dr Hanaa Assil IAL chemistry unit papers; Zainematics 0580/9709/0606/9618; Craig'n'Dave CAMBRIDGE 0478 series; Science with Hazel Edexcel-IGCSE; Mega Lecture CIE aggregator; ExamSolutions IAL-legacy composites; Sir Faizan Pasha + CK A-level Physics 9702; IGCSESUCCESS FLE 0500; MrAstburyMaths 4MA1; + the Allery-CIE re-adjudication group)";
for (const course of P14) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p14.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p14.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p14 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const contentPath = join(MAPDIR, `${course}.json`);
  if (!existsSync(contentPath))
    throw new Error(`${course}: p14 targets only existing covered courses — content file missing`);
  const content = JSON.parse(readFileSync(contentPath, "utf8"));
  if (!content.review) errors.push(`${course}: existing content file has no review block`);
  if (!content.inputs) errors.push(`${course}: existing content file has no inputs block`);
  if (errors.length) break;

  // idempotency (the P2B law, video-keyed): the draft is the only source for
  // p14 rows — drop prior rows by video id and the prior p14 lane entry before
  // re-appending, so a re-emit from post-p14 state is a no-op.
  const p14Vids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p14Vids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("channel recon judgment lane")
  );
  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p14 row leaking into content (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p14 video id ${m.video}`);
    if (m.method === "paper-code") {
      if (!m.anchor || m.anchor.level !== "course" || m.anchor.ref !== course)
        errors.push(`${course}: p14 paper-code row must carry anchor{level:course, ref:course} (${m.video})`);
      if (!m.specs || m.specs.length !== 0)
        errors.push(`${course}: p14 anchor rows carry specs:[] — zero spec weight (§4) (${m.video})`);
      if (m.confidence !== "high")
        errors.push(`${course}: p14 paper-code anchor must be high confidence (${m.video})`);
      if (m.boardMismatch !== false)
        errors.push(`${course}: p14 paper-code anchor is same-qualification — boardMismatch must be false (${m.video})`);
      if (m.kind !== "past-paper-walkthrough")
        errors.push(`${course}: p14 anchor row must carry kind past-paper-walkthrough (${m.video})`);
    } else if (m.method === "llm-draft-external") {
      if (!m.specs || m.specs.length === 0)
        errors.push(`${course}: p14 spec rows must carry non-empty specs (${m.video})`);
      if (m.boardMismatch !== true)
        errors.push(`${course}: p14 spec rows carry the title-only posture — boardMismatch must be true (${m.video})`);
      if (m.confidence !== "medium" && m.confidence !== "low")
        errors.push(`${course}: p14 spec rows are medium/low — high would violate the inherit posture (${m.video})`);
      for (const code of m.specs || [])
        if (!specByCode.has(code)) errors.push(`${course}: p14 spec ${code} not in spine (${m.video})`);
    } else {
      errors.push(`${course}: p14 row has unexpected method ${m.method} (${m.video})`);
    }
  }
  const haveKeysP14 = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP14.has(k)) errors.push(`${course}: duplicate p14 row across union ${k}`);
    haveKeysP14.add(k);
  }
  const haveVidsP14 = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP14.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p14 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p14 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP14 = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP14 = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP14.size,
    specPointsUnmapped: specByCode.size - allSpecsP14.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP14.size,
    videosUnmapped: content.videos.length - mappedVidsP14.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p14Lane = {
    lane: P14_LANE_NAME, task: verdicts.task,
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
    p14Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p14 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p14 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p14.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(contentPath, JSON.stringify(content, null, 1) + "\n");
  const baseLaneP14 = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP14.includes("p14-channel-recon") ? baseLaneP14 : baseLaneP14 + " + p14-channel-recon",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p14 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} channel-recon rows) · 0 reviewed:false in content`
  );
}


// ================================================= P15 discovery judgment lane =====
// Owner 2026-11-18: "How about you search for channels and videos to map?" -> the gap-targeted
// discovery sweep (scripts/p15/sweep.json: 24 gap clusters, 231 channels harvested, 208 new)
// -> 19 pools filed (resources PR #358: 5,591 uploads, 0 overlap vs the shipped union 8,783
// incl. P14 AND all prior lane inventories 38,773 AND 0 intra-P15) -> owner "Continue working"
// 2026-11-18 = run the lane. 18 judgment pools (T1 x14 + T2 x4; claires-notes RESERVED — the
// 0475 lit register folds into the lit-21 owner decision point with the IGCSESUCCESS 9).
// 1,562 owner-reviewed rows onto 32 courses: 1,033 Tier B paper-code anchors (method
// paper-code, high, zero spec weight) + 529 spec rows (the P13/P14 ladder: section-marker N.M,
// verbatim section-name binding, distinctive-token df<=3, four-gate topic lectures). New Tier B
// laws of record on top of P14: CIE IGCSE sciences 0610/0620/0625 session/paper registers;
// 0654/0653 shared-paper anchors binding all three sciences of the family (the P13 shared-unit
// double-binding precedent); 0417/4IT0 ICT dual register; 4MA1 maths-A higher/foundation/
// modular-24-unit routing; 0606; 0452/0455/0680/8291/0460/4GE0/0500 shared-code pairs bound to
// both syllabus-year courses (disclosed); IAL WPH/WBI/WCH "Unit N <session>" unit-paper anchors
// (the P14 Assil law analog); 9708. Identity: oEmbed 1,365/1,365 routed videos author_url ==
// channel-of-record via UC id (0 mismatch, 0 dead, 0 thumb fallbacks). Honest skips 3,983
// ledgered by class with exactly-once disposition of all 5,591 accounts (routed + skips + 243
// RESERVED). 21 courses append here BEFORE the P4 inherit loop (their parent rows cascade); the
// 11 P4 inherit CHILDREN with direct P15 rows (scripts/p15/p15-courses.json is the committed
// partition of record) append AFTER the loop in P15B below (the P11B/P13B/P14B shape).
const P15 = [
  "cie-a-level-economics-23",
  "cie-as-environmental-management-20",
  "cie-igcse-accounting-21",
  "cie-igcse-accounting-25",
  "cie-igcse-biology-23",
  "cie-igcse-chemistry-23",
  "cie-igcse-economics-20",
  "cie-igcse-economics-25",
  "cie-igcse-english-language-20",
  "cie-igcse-english-language-25",
  "cie-igcse-environmental-management-25",
  "cie-igcse-further-maths-additional-maths-25",
  "cie-igcse-geography-20",
  "cie-igcse-geography-25",
  "cie-igcse-ict-21",
  "cie-igcse-physics-23",
  "igcse-biology-19",
  "igcse-chemistry-19",
  "igcse-geography-19",
  "igcse-ict-17",
  "igcse-maths-a-18-higher",
];
const P15_LANE_NAME = "external-channels-p15 (discovery judgment lane: chem bio by Hosni \u2014 the sweep's densest find over the two biggest residual gaps, 0610 x342 + WBI x213; CAIE made easier + Learn Today IGCSE + Science and Stuff for the 0610/0620/0625/0654/0653 registers; Nicos Paphitis 0417 x121; Mark Harrison Ed-IGCSE ICT/CS x93 + 0417 x58; The Math Pad 4MA1 x197 + Libra Maths 4MA1 x127 + 0606 x63; Gilbert Phoon + Shawn Hew 0606/0620; Doctor No Does Science WPH x74 \u2014 the P14 Assil law analog; Taughtly 0500 x69; Dr. Maria Emam 0680 x55 + Everything E.M. 0680 x13; GEO-HACKS 0460 x37; Keen Mindz 0452 x64 at 100% register; Learn Economics with Anjuli 0455 + 9708; Belal Sir Ed-IGCSE chem/bio + 0620 with the AQA remainder skipped)";
for (const course of P15) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p15.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p15.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p15 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const contentPath = join(MAPDIR, `${course}.json`);
  if (!existsSync(contentPath))
    throw new Error(`${course}: p15 targets only existing covered courses — content file missing`);
  const content = JSON.parse(readFileSync(contentPath, "utf8"));
  if (!content.review) errors.push(`${course}: existing content file has no review block`);
  if (!content.inputs) errors.push(`${course}: existing content file has no inputs block`);
  if (errors.length) break;

  // idempotency (the P2B law, video-keyed): the draft is the only source for
  // p15 rows — drop prior rows by video id and the prior p15 lane entry before
  // re-appending, so a re-emit from post-p15 state is a no-op.
  const p15Vids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p15Vids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("discovery judgment lane")
  );
  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p15 row leaking into content (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p15 video id ${m.video}`);
    if (m.method === "paper-code") {
      if (!m.anchor || m.anchor.level !== "course" || m.anchor.ref !== course)
        errors.push(`${course}: p15 paper-code row must carry anchor{level:course, ref:course} (${m.video})`);
      if (!m.specs || m.specs.length !== 0)
        errors.push(`${course}: p15 anchor rows carry specs:[] — zero spec weight (§4) (${m.video})`);
      if (m.confidence !== "high")
        errors.push(`${course}: p15 paper-code anchor must be high confidence (${m.video})`);
      if (m.boardMismatch !== false)
        errors.push(`${course}: p15 paper-code anchor is same-qualification — boardMismatch must be false (${m.video})`);
      if (m.kind !== "past-paper-walkthrough")
        errors.push(`${course}: p15 anchor row must carry kind past-paper-walkthrough (${m.video})`);
    } else if (m.method === "llm-draft-external") {
      if (!m.specs || m.specs.length === 0)
        errors.push(`${course}: p15 spec rows must carry non-empty specs (${m.video})`);
      if (m.boardMismatch !== true)
        errors.push(`${course}: p15 spec rows carry the title-only posture — boardMismatch must be true (${m.video})`);
      if (m.confidence !== "medium" && m.confidence !== "low")
        errors.push(`${course}: p15 spec rows are medium/low — high would violate the inherit posture (${m.video})`);
      for (const code of m.specs || [])
        if (!specByCode.has(code)) errors.push(`${course}: p15 spec ${code} not in spine (${m.video})`);
    } else {
      errors.push(`${course}: p15 row has unexpected method ${m.method} (${m.video})`);
    }
  }
  const haveKeysP15 = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP15.has(k)) errors.push(`${course}: duplicate p15 row across union ${k}`);
    haveKeysP15.add(k);
  }
  const haveVidsP15 = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP15.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p15 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p15 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP15 = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP15 = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP15.size,
    specPointsUnmapped: specByCode.size - allSpecsP15.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP15.size,
    videosUnmapped: content.videos.length - mappedVidsP15.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p15Lane = {
    lane: P15_LANE_NAME, task: verdicts.task,
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
    p15Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p15 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p15 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p15.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLaneP15 = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP15.includes("p15-discovery") ? baseLaneP15 : baseLaneP15 + " + p15-discovery",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p15 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} discovery rows, pre-inherit) · 0 reviewed:false in content`
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

// ================================================= P7B — ial append-after-inherit =====
// The three ial courses are inherit children: the inherit section above rebuilds
// their files fresh, so their P7 rows cannot be appended before it. Same lane,
// same drafts, the P2F shape (append after inherit, before P2F anchors).
for (const course of P7B) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p7.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p7.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p7 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const content = JSON.parse(readFileSync(join(MAPDIR, `${course}.json`), "utf8"));

  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p7 row leaking into content (${m.video})`);
    if (m.method !== "llm-draft-external")
      errors.push(`${course}: p7 row missing method (${m.video})`);
    if (m.boardMismatch !== true)
      errors.push(`${course}: p7 row must carry boardMismatch:true (${m.video})`);
    if (!m.specs || m.specs.length === 0)
      errors.push(`${course}: p7 rows are spec rows — specs must be non-empty (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p7 video id ${m.video}`);
    for (const code of m.specs || [])
      if (!specByCode.has(code)) errors.push(`${course}: p7 spec ${code} not in spine (${m.video})`);
  }
  const haveKeysP7b = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP7b.has(k)) errors.push(`${course}: duplicate p7 row across union ${k}`);
    haveKeysP7b.add(k);
  }
  const haveVidsP7b = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP7b.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p7 video ${v.id} missing provider/watchUrl`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP7b = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP7b = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP7b.size,
    specPointsUnmapped: specByCode.size - allSpecsP7b.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP7b.size,
    videosUnmapped: content.videos.length - mappedVidsP7b.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p7bLane = {
    lane: "external-channels-p7 (remaining channel pools)", task: verdicts.task,
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
    p7bLane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p7 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p7 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p7.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLaneP7b = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP7b.includes("p7-channel-pools") ? baseLaneP7b : baseLaneP7b + " + p7-channel-pools",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p7 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} remaining-channel-pools rows, post-inherit) · 0 reviewed:false in content`
  );
}

// ================================================= P9B — inherit-child append-after-inherit =====
// The two inherit-CHILD courses that carry P9 rows (cie-igcse-maths-25-core from
// bare-0580-derived Tier A rows routed onto the core spine, and
// igcse-maths-a-modular-24-higher-unit-1 from 4XMA modular-sample walkthroughs)
// are rebuilt fresh by the inherit section above — their P9 rows cannot be
// appended before it. Same lane, same drafts, the P7B shape.
for (const course of P9B) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p9.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p9.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p9 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const content = JSON.parse(readFileSync(join(MAPDIR, `${course}.json`), "utf8"));

  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p9 row leaking into content (${m.video})`);
    if (m.method !== "llm-draft-external")
      errors.push(`${course}: p9b rows are spec rows — unexpected method (${m.video})`);
    if (m.boardMismatch !== true)
      errors.push(`${course}: p9b row must carry boardMismatch:true (${m.video})`);
    if (!m.specs || m.specs.length === 0)
      errors.push(`${course}: p9b rows are spec rows — specs must be non-empty (${m.video})`);
    if (m.confidence !== "medium" && m.confidence !== "low")
      errors.push(`${course}: p9b rows are medium/low (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p9 video id ${m.video}`);
    for (const code of m.specs || [])
      if (!specByCode.has(code)) errors.push(`${course}: p9 spec ${code} not in spine (${m.video})`);
  }
  const haveKeysP9b = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP9b.has(k)) errors.push(`${course}: duplicate p9 row across union ${k}`);
    haveKeysP9b.add(k);
  }
  const haveVidsP9b = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP9b.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p9 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p9 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP9b = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP9b = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP9b.size,
    specPointsUnmapped: specByCode.size - allSpecsP9b.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP9b.size,
    videosUnmapped: content.videos.length - mappedVidsP9b.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p9bLane = {
    lane: "external-channels-p9 (mr-hassaans-maths completion)", task: verdicts.task,
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
    p9bLane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p9 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p9 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p9.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLaneP9b = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP9b.includes("p9-mrhassans") ? baseLaneP9b : baseLaneP9b + " + p9-mrhassans",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p9 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} mr-hassaans-maths rows, post-inherit) · 0 reviewed:false in content`
  );
}

// ================================================= P11B — inherit-child append-after-inherit =====
// cie-as-physics-25 is an inherit CHILD (rebuilt fresh by the inherit section
// above), so its P11 rows (James Gan 9702 chapter series) cannot be appended
// before it. Same lane, same drafts, the P7B shape.
const P11B = ["cie-as-physics-25"];
for (const course of P11B) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p11.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p11.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p11 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const content = JSON.parse(readFileSync(join(MAPDIR, `${course}.json`), "utf8"));

  // idempotency (the P2B law, video-keyed): the inherit section derived rows
  // for these videos from the PARENT's fresh P11 rows (cie-a-level-physics-25
  // gained the same James Gan pool). Drop prior rows by video id and the prior
  // p11 lane entry before re-appending so the replay is a no-op.
  const p11bVids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p11bVids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("multi-cluster uncovered-course")
  );

  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p11 row leaking into content (${m.video})`);
    if (m.method !== "llm-draft-external")
      errors.push(`${course}: p11b rows are spec rows — unexpected method (${m.video})`);
    if (m.boardMismatch !== true)
      errors.push(`${course}: p11b row must carry boardMismatch:true (${m.video})`);
    if (!m.specs || m.specs.length === 0)
      errors.push(`${course}: p11b rows are spec rows — specs must be non-empty (${m.video})`);
    if (m.confidence !== "medium" && m.confidence !== "low")
      errors.push(`${course}: p11b rows are medium/low (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p11 video id ${m.video}`);
    for (const code of m.specs || [])
      if (!specByCode.has(code)) errors.push(`${course}: p11 spec ${code} not in spine (${m.video})`);
  }
  const haveKeysP11b = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP11b.has(k)) errors.push(`${course}: duplicate p11 row across union ${k}`);
    haveKeysP11b.add(k);
  }
  const haveVidsP11b = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP11b.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p11 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p11 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP11b = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP11b = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP11b.size,
    specPointsUnmapped: specByCode.size - allSpecsP11b.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP11b.size,
    videosUnmapped: content.videos.length - mappedVidsP11b.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p11bLane = {
    lane: "external-channels-p11 (multi-cluster uncovered-course lane: fourteen channel pools)", task: verdicts.task,
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
    p11bLane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p11 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p11 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p11.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLaneP11b = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP11b.includes("p11-multicluster") ? baseLaneP11b : baseLaneP11b + " + p11-multicluster",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p11 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} multi-cluster rows, post-inherit) · 0 reviewed:false in content`
  );
}

// ================================================= P13B — inherit-child append-after-inherit =====
// cie-as-chemistry-25 and cie-as-physics-25 are inherit CHILDREN (rebuilt fresh
// by the inherit section above), so their direct P13 rows (the AS-register
// chemistry walkthrough corpus; the Paper-22 physics walkthrough anchor) cannot
// be appended before it. Same lane, same drafts, the P11B shape. Unlike P11B
// these drafts may carry BOTH methods (paper-code anchors + spec rows), so the
// validation mirrors the P12 section's dual law.
const P13B = ["cie-as-chemistry-25", "cie-as-physics-25"];
for (const course of P13B) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p13.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p13.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p13 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const content = JSON.parse(readFileSync(join(MAPDIR, `${course}.json`), "utf8"));

  // idempotency (the P2B law, video-keyed): the inherit section re-derived the
  // child's rows from the PARENT's fresh P13 rows; drop prior rows by video id
  // and the prior p13 lane entry before re-appending so the replay is a no-op.
  const p13bVids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p13bVids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("Alt Academy family lane")
  );

  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p13 row leaking into content (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p13 video id ${m.video}`);
    if (m.method === "paper-code") {
      if (!m.anchor || m.anchor.level !== "course" || m.anchor.ref !== course)
        errors.push(`${course}: p13b paper-code row must carry anchor{level:course, ref:course} (${m.video})`);
      if (!m.specs || m.specs.length !== 0)
        errors.push(`${course}: p13b anchor rows carry specs:[] — zero spec weight (§4) (${m.video})`);
      if (m.confidence !== "high")
        errors.push(`${course}: p13b paper-code anchor must be high confidence (${m.video})`);
      if (m.boardMismatch !== false)
        errors.push(`${course}: p13b paper-code anchor is same-qualification — boardMismatch must be false (${m.video})`);
      if (m.kind !== "past-paper-walkthrough")
        errors.push(`${course}: p13b anchor row must carry kind past-paper-walkthrough (${m.video})`);
    } else if (m.method === "llm-draft-external") {
      if (m.boardMismatch !== true)
        errors.push(`${course}: p13b row must carry boardMismatch:true (${m.video})`);
      if (!m.specs || m.specs.length === 0)
        errors.push(`${course}: p13b rows are spec rows — specs must be non-empty (${m.video})`);
      if (m.confidence !== "medium" && m.confidence !== "low")
        errors.push(`${course}: p13b rows are medium/low (${m.video})`);
      for (const code of m.specs || [])
        if (!specByCode.has(code)) errors.push(`${course}: p13 spec ${code} not in spine (${m.video})`);
    } else {
      errors.push(`${course}: p13b rows are paper-code or llm-draft-external — unexpected method (${m.video})`);
    }
  }
  const haveKeysP13b = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP13b.has(k)) errors.push(`${course}: duplicate p13 row across union ${k}`);
    haveKeysP13b.add(k);
  }
  const haveVidsP13b = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP13b.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p13 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p13 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP13b = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP13b = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP13b.size,
    specPointsUnmapped: specByCode.size - allSpecsP13b.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP13b.size,
    videosUnmapped: content.videos.length - mappedVidsP13b.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p13bLane = {
    lane: "external-channels-p13 (Alt Academy family lane: 9701/9708/9709/9702/9700/9706/9609 CIE-native hub + 8 subject channels)", task: verdicts.task,
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
    p13bLane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p13 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p13 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p13.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLaneP13b = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP13b.includes("p13-alt-academy") ? baseLaneP13b : baseLaneP13b + " + p13-alt-academy",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p13 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} alt-academy rows, post-inherit) · 0 reviewed:false in content`
  );
}

// ================================================= P14B — inherit-child append-after-inherit =====
// Five P4 inherit CHILDREN carry DIRECT P14 rows (scripts/p14/p14-courses.json is the
// committed partition of record): cie-as-biology-25, cie-as-chemistry-25,
// cie-as-physics-25, cie-igcse-maths-25-core and ial-chemistry-17 are rebuilt fresh by
// the inherit section above (their parent courses gained P14 rows in the P14 section —
// a-level bio/chem/phys, 25-extended and igcse-chemistry-19), so the children's own
// drafts (the 9702 AS session-walkthrough corpus, the Assil IAL unit-paper anchors, the
// 25-core M1/M2 papers) cannot be appended before it. Same lane, same drafts, the
// P11B/P13B shape. These drafts carry BOTH methods (paper-code anchors + spec rows), so
// the validation mirrors the P13B dual law.
const P14B = ["cie-as-biology-25", "cie-as-chemistry-25", "cie-as-physics-25", "cie-igcse-maths-25-core", "ial-chemistry-17"];
for (const course of P14B) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p14.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p14.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p14 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const content = JSON.parse(readFileSync(join(MAPDIR, `${course}.json`), "utf8"));

  // idempotency (the P2B law, video-keyed): the inherit section re-derived the
  // child's rows from the PARENT's fresh P14 rows; drop prior rows by video id
  // and the prior p14 lane entry before re-appending so the replay is a no-op.
  const p14bVids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p14bVids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("channel recon judgment lane")
  );

  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p14 row leaking into content (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p14 video id ${m.video}`);
    if (m.method === "paper-code") {
      if (!m.anchor || m.anchor.level !== "course" || m.anchor.ref !== course)
        errors.push(`${course}: p14b paper-code row must carry anchor{level:course, ref:course} (${m.video})`);
      if (!m.specs || m.specs.length !== 0)
        errors.push(`${course}: p14b anchor rows carry specs:[] — zero spec weight (§4) (${m.video})`);
      if (m.confidence !== "high")
        errors.push(`${course}: p14b paper-code anchor must be high confidence (${m.video})`);
      if (m.boardMismatch !== false)
        errors.push(`${course}: p14b paper-code anchor is same-qualification — boardMismatch must be false (${m.video})`);
      if (m.kind !== "past-paper-walkthrough")
        errors.push(`${course}: p14b anchor row must carry kind past-paper-walkthrough (${m.video})`);
    } else if (m.method === "llm-draft-external") {
      if (m.boardMismatch !== true)
        errors.push(`${course}: p14b row must carry boardMismatch:true (${m.video})`);
      if (!m.specs || m.specs.length === 0)
        errors.push(`${course}: p14b rows are spec rows — specs must be non-empty (${m.video})`);
      if (m.confidence !== "medium" && m.confidence !== "low")
        errors.push(`${course}: p14b rows are medium/low (${m.video})`);
      for (const code of m.specs || [])
        if (!specByCode.has(code)) errors.push(`${course}: p14 spec ${code} not in spine (${m.video})`);
    } else {
      errors.push(`${course}: p14b rows are paper-code or llm-draft-external — unexpected method (${m.video})`);
    }
  }
  const haveKeysP14b = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP14b.has(k)) errors.push(`${course}: duplicate p14 row across union ${k}`);
    haveKeysP14b.add(k);
  }
  const haveVidsP14b = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP14b.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p14 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p14 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP14b = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP14b = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP14b.size,
    specPointsUnmapped: specByCode.size - allSpecsP14b.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP14b.size,
    videosUnmapped: content.videos.length - mappedVidsP14b.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p14bLane = {
    lane: P14_LANE_NAME, task: verdicts.task,
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
    p14bLane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p14 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p14 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p14.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLaneP14b = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP14b.includes("p14-channel-recon") ? baseLaneP14b : baseLaneP14b + " + p14-channel-recon",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p14 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} channel-recon rows, post-inherit) · 0 reviewed:false in content`
  );
}


// ================================================= P15B — inherit-child append-after-inherit =====
// Eleven P4 inherit CHILDREN carry DIRECT P15 rows (scripts/p15/p15-courses.json is the
// committed partition of record): the 0654 co-ordinated-sciences trio, ial-physics-19,
// ial-biology-18, ial-chemistry-17, igcse-maths-a-18-foundation and the igcse-maths-a-modular-24
// units x4 are rebuilt fresh by the inherit section above (their parent courses gained P15 rows
// in the P15 section — the single-science IGCSE trio, maths-a-18-higher and the other P15 pre
// courses), so the children's own drafts (the 0654/0653 shared-paper anchors, the Doctor-No WPH
// unit-paper anchors, Hosni's WBI unit anchors, the Math Pad modular-unit walkthroughs) cannot
// be appended before it. Same lane, same drafts, the P11B/P13B/P14B shape. These drafts carry
// BOTH methods (paper-code anchors + spec rows), so the validation mirrors the P14B dual law.
const P15B = [
  "cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
  "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry",
  "cie-igcse-science-co-ordinated-sciences-double-award-23-physics",
  "ial-biology-18",
  "ial-chemistry-17",
  "ial-physics-19",
  "igcse-maths-a-18-foundation",
  "igcse-maths-a-modular-24-foundation-unit-1",
  "igcse-maths-a-modular-24-foundation-unit-2",
  "igcse-maths-a-modular-24-higher-unit-1",
  "igcse-maths-a-modular-24-higher-unit-2",
];
for (const course of P15B) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p15.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p15.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p15 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const content = JSON.parse(readFileSync(join(MAPDIR, `${course}.json`), "utf8"));

  // idempotency (the P2B law, video-keyed): the inherit section re-derived the
  // child's rows from the PARENT's fresh P15 rows; drop prior rows by video id
  // and the prior p15 lane entry before re-appending so the replay is a no-op.
  const p15bVids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p15bVids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("discovery judgment lane")
  );

  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p15 row leaking into content (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p15 video id ${m.video}`);
    if (m.method === "paper-code") {
      if (!m.anchor || m.anchor.level !== "course" || m.anchor.ref !== course)
        errors.push(`${course}: p15b paper-code row must carry anchor{level:course, ref:course} (${m.video})`);
      if (!m.specs || m.specs.length !== 0)
        errors.push(`${course}: p15b anchor rows carry specs:[] — zero spec weight (§4) (${m.video})`);
      if (m.confidence !== "high")
        errors.push(`${course}: p15b paper-code anchor must be high confidence (${m.video})`);
      if (m.boardMismatch !== false)
        errors.push(`${course}: p15b paper-code anchor is same-qualification — boardMismatch must be false (${m.video})`);
      if (m.kind !== "past-paper-walkthrough")
        errors.push(`${course}: p15b anchor row must carry kind past-paper-walkthrough (${m.video})`);
    } else if (m.method === "llm-draft-external") {
      if (m.boardMismatch !== true)
        errors.push(`${course}: p15b row must carry boardMismatch:true (${m.video})`);
      if (!m.specs || m.specs.length === 0)
        errors.push(`${course}: p15b rows are spec rows — specs must be non-empty (${m.video})`);
      if (m.confidence !== "medium" && m.confidence !== "low")
        errors.push(`${course}: p15b rows are medium/low (${m.video})`);
      for (const code of m.specs || [])
        if (!specByCode.has(code)) errors.push(`${course}: p15 spec ${code} not in spine (${m.video})`);
    } else {
      errors.push(`${course}: p15b rows are paper-code or llm-draft-external — unexpected method (${m.video})`);
    }
  }
  const haveKeysP15b = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP15b.has(k)) errors.push(`${course}: duplicate p15 row across union ${k}`);
    haveKeysP15b.add(k);
  }
  const haveVidsP15b = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP15b.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p15 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p15 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP15b = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP15b = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP15b.size,
    specPointsUnmapped: specByCode.size - allSpecsP15b.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP15b.size,
    videosUnmapped: content.videos.length - mappedVidsP15b.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p15bLane = {
    lane: P15_LANE_NAME, task: verdicts.task,
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
    p15bLane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p15 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p15 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p15.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(join(MAPDIR, `${course}.json`), JSON.stringify(content, null, 1) + "\n");
  const baseLaneP15b = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP15b.includes("p15-discovery") ? baseLaneP15b : baseLaneP15b + " + p15-discovery",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p15 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} discovery rows, post-inherit) · 0 reviewed:false in content`
  );
}

// ================================================= P16 lit-21 opening lane =====
// Owner chat 2026-11-20: "open lit-21" — the P12 terminal declaration is
// overturned for cie-igcse-english-literature-21 (this course ONLY), and the
// 252 RESERVED lit-0475 titles (P14 IGCSESUCCESS 0475 x9 + P15 Claire's Notes
// x243) are adjudicated onto the freshly opened course. Class W set-text work
// binds over the 0475 2023-2025 set-text spine (Songs of Ourselves Vol 1 P4 /
// Vol 2 P3 / Vol 2 P4, the Ted Hughes 15 two-per-line pairs, the prose novels,
// the Stories of Ourselves Vol 2 per-year lists, the per-year drama set
// texts): a title naming a set-text WORK binds EVERY spec point carrying that
// work — multi-year occurrences disclosed per row (the P13 shared-unit
// precedent). Match rule suffix-anchored (span == work, span ends with the
// work at a word boundary, or the title dropped a leading article;
// mid-phrase coincidences like 'night sweat' inside 'The Man with Night
// Sweats' do NOT bind). Confidence medium on author+work verbatim titles, low
// under the title-only posture (work-only scene commentary, multi-work tips
// rows as ONE multi-spec row — the four-gate topic-lecture class analog);
// boardMismatch true on every spec row (the committed builder law). oEmbed
// identity 100/100 author==channel-of-record (0 fallbacks). Honest skips 152
// ledgered (scripts/p16/skips.json by class: guidance/skills 15, out-of-spine
// board 16, character-study 15, no-set-text 106). No paper-code anchors (no
// session codes in the reserved titles) — every row is a spec row.
// Fresh-create (the P12 shape): the course has no video-map file; lit-21
// takes no inherit rows (no containment children), so no P16B section.
const P16 = ["cie-igcse-english-literature-21"];
for (const course of P16) {
  const D = join(VIDEOS, "drafts", course);
  const draft = JSON.parse(readFileSync(join(D, "video-map.draft.external-p16.json"), "utf8"));
  const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.p16.json"), "utf8"));
  if (draft.reviewState !== "owner-reviewed-external")
    throw new Error(`${course}: p16 reviewState is "${draft.reviewState}" — apply review first`);
  const spine = JSON.parse(readFileSync(join(SPINES, `${course}.json`), "utf8"));
  const specByCode = new Map(
    spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
  );
  assertSpineMirror(course, spine);
  const contentPath = join(MAPDIR, `${course}.json`);
  let content;
  if (existsSync(contentPath)) {
    content = JSON.parse(readFileSync(contentPath, "utf8"));
    if (!content.review) errors.push(`${course}: existing content file has no review block`);
    if (!content.inputs) errors.push(`${course}: existing content file has no inputs block`);
    if (errors.length) break;
  } else {
    content = {
      schema: "hub.video-map/1",
      course,
      qual: draft.qual,
      source: {
        provider: draft.source.provider,
        label: course,
        method: draft.source.method,
        enumeratedUtc: draft.source.enumeratedUtc,
      },
      review: {
        task: verdicts.task,
        ruledUtc: verdicts.ruledUtc,
        ruling: verdicts.source,
        reviewer: verdicts.reviewer,
        evidenceBasis: verdicts.evidenceBasis,
        rowsApproved: 0,
        rowsRejected: (verdicts.rejects || []).length,
        rejects: REJECTS_OF(verdicts, verdicts.task),
      },
      videos: [],
      mappings: [],
      coverage: null,
      inputs: {
        spine: { file: `apps/hub/spines/${course}.json`, sha256: sha256(join(SPINES, `${course}.json`)) },
      },
      generatedUtc: new Date().toISOString(),
    };
  }

  // idempotency (the P2B law, video-keyed): the draft is the only source for
  // p16 rows — drop prior p16-lane rows (by video id) and the prior p16 lane
  // entry before re-appending, so a re-emit from post-p16 state is a no-op.
  const p16Vids = new Set(draft.videos.map((v) => v.id));
  content.mappings = content.mappings.filter((m) => !p16Vids.has(m.video));
  content.review.lanes = (content.review.lanes || []).filter(
    (l) => !String(l.lane || "").includes("lit-21 opening lane")
  );
  for (const m of draft.mappings) {
    if (m.reviewed !== true || !m.reviewer || !m.reviewedUtc)
      errors.push(`${course}: unreviewed p16 row leaking into content (${m.video})`);
    if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${course}: bad p16 video id ${m.video}`);
    if (m.method === "llm-draft-external") {
      if (!m.specs || m.specs.length === 0)
        errors.push(`${course}: p16 spec rows must carry non-empty specs (${m.video})`);
      if (m.boardMismatch !== true)
        errors.push(`${course}: p16 spec rows carry the title-only posture — boardMismatch must be true (${m.video})`);
      if (m.confidence !== "medium" && m.confidence !== "low")
        errors.push(`${course}: p16 spec rows are medium/low — high would violate the inherit posture (${m.video})`);
      for (const code of m.specs || [])
        if (!specByCode.has(code)) errors.push(`${course}: p16 spec ${code} not in spine (${m.video})`);
    } else {
      errors.push(`${course}: p16 row has unexpected method ${m.method} (${m.video})`);
    }
  }
  const haveKeysP16 = new Set(content.mappings.map((m) => m.video + "|" + JSON.stringify(m.specs)));
  for (const m of draft.mappings) {
    const k = m.video + "|" + JSON.stringify(m.specs);
    if (haveKeysP16.has(k)) errors.push(`${course}: duplicate p16 row across union ${k}`);
    haveKeysP16.add(k);
  }
  const haveVidsP16 = new Set(content.videos.map((v) => v.id));
  for (const v of draft.videos) {
    if (!haveVidsP16.has(v.id)) content.videos.push(v);
    if (!v.provider || !v.watchUrl) errors.push(`${course}: p16 video ${v.id} missing provider/watchUrl`);
    if (!v.identityMethod) errors.push(`${course}: p16 video ${v.id} missing identityMethod`);
  }
  if (errors.length) break;

  content.mappings = [...content.mappings, ...draft.mappings];
  const allSpecsP16 = new Set(content.mappings.flatMap((m) => m.specs));
  const mappedVidsP16 = new Set(content.mappings.map((m) => m.video));
  content.coverage = {
    specPointsTotal: specByCode.size,
    specPointsMapped: allSpecsP16.size,
    specPointsUnmapped: specByCode.size - allSpecsP16.size,
    videosTotal: content.videos.length,
    videosMapped: mappedVidsP16.size,
    videosUnmapped: content.videos.length - mappedVidsP16.size,
    mappingRows: content.mappings.length,
    byConfidence: {
      high: content.mappings.filter((m) => m.confidence === "high").length,
      medium: content.mappings.filter((m) => m.confidence === "medium").length,
      low: content.mappings.filter((m) => m.confidence === "low").length,
    },
  };
  const p16Lane = {
    lane: "external-channels-p16 (lit-21 opening lane: the P12 terminal declaration overturned by owner decision \"open lit-21\" 2026-11-20 — the P14+P15 RESERVED lit-0475 sets adjudicated onto the freshly opened course; Class W set-text work binds: Songs of Ourselves Vol 1 P4 / Vol 2 P3 / Vol 2 P4 poem guides, the Ted Hughes 15 pair-lines, Othello / A Midsummer Night's Dream / Journey's End / Twelfth Night / A Streetcar Named Desire scene commentary, the Stories of Ourselves Vol 2 story guides)", task: verdicts.task,
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
    p16Lane,
  ];
  content.review.rowsApproved = content.mappings.length;
  content.source.p16 = {
    provider: draft.source.provider, method: draft.source.method,
    enumeratedUtc: draft.source.enumeratedUtc,
  };
  content.inputs.p16 = {
    repo: "SyllabAI/syllabai-resources",
    path: `Videos/drafts/${course}/video-map.draft.external-p16.json`,
    task: verdicts.task, reviewAppliedUtc: verdicts.ruledUtc,
  };
  content.generatedUtc = new Date().toISOString();
  writeFileSync(contentPath, JSON.stringify(content, null, 1) + "\n");
  const baseLaneP16 = registry.courses[course]?.lane || "external-channels";
  registry.courses[course] = {
    videos: content.videos.length,
    mapped: content.coverage.videosMapped,
    shelf: registry.courses[course]?.shelf ?? null,
    lane: baseLaneP16.includes("p16-lit21") ? baseLaneP16 : baseLaneP16 + " + p16-lit21",
    updatedUtc: new Date().toISOString(),
  };
  registry.generatedUtc = new Date().toISOString();
  console.log(
    `${course}: SHIPPED +p16 specs ${content.coverage.specPointsMapped}/${content.coverage.specPointsTotal} · videos ${content.coverage.videosMapped}/${content.coverage.videosTotal} · rows ${content.coverage.mappingRows} (+${draft.mappings.length} lit-21 opening rows) · 0 reviewed:false in content`
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
// Skip-if-current: once P3 landed (PR #906) the lane surface is live; rewriting
// it on every emit would churn flags.json (and fight the file's \uXXXX escaping).
// The status template carries the full lane history (P3+P4+P5+P6+P7) since the
// P6 receipt-sync lane: the P6 emit's skip-if-current had silently left the status
// string at its P4-era text while the P6 commit message claimed P3+P4+P5+P6.
// When the course set is unchanged (P5/P6/P7) the shipped hub flags.json status
// must be hand-synced in the lane PR to match this template.
const flagsPath = join(HUB, "apps/hub/content/flags.json");
const flags = JSON.parse(readFileSync(flagsPath, "utf8"));
const want = [...new Set([
  "igcse-biology-19", ...FRESH, ...P4_FRESH, ...P9, ...P9B, ...P10, ...P11, ...P12, ...P11B, ...P13, ...P13B, ...P14, ...P14B, ...P15, ...P15B, ...P16, ...Object.keys(inhMap.parents),
])];
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
    "live (T-VIDEOMAP-P3+P4+P5+P6+P7+P8+P9+P10+P11+P12+P13+P14+P15): lib/video-map.ts loader + /courses/[course]/videos lane shipped for the "
    + "courses below (igcse-biology-19 site+external; 9 external-channels courses incl. the CIE A-level trio; "
    + "P4 scale pass: 4 shelf-direct Cognito maths lanes, 4 mechanics cross-subject lanes, 35 inherited lanes "
    + "derived from owner-approved parent rows via the committed containment map; "
    + "P5 Cognito completion: 208 owner-reviewed rows onto 5 parents, cascaded to 9 children via the same "
    + "containment map; P6 PhysicsOnline completion: 113 owner-reviewed rows onto the 3 physics parents, "
    + "cascaded to 8 children - ial-physics-19 honestly cascades 0; "
    + "P7 remaining channel pools: 277 owner-reviewed rows onto the 12 science parents, cascaded to 24 children; "
    + "P8 physics-trio honest-empty fill: 8 owner-reviewed rows fill 6 of the trio's 323 empty spec points "
    + "(1,136-video pool remainder re-adjudicated, 610-entry honest reject ledger); "
    + "P9 Mr Hassaan's Maths Channel completion: 3,380 owner-reviewed rows onto 22 maths courses - 2,988 "
    + "course anchors bound by machine-checkable paper codes (zero spec weight, ANCHOR-GRANULARITY sections 4/5/8; "
    + "the channel is paper-code native: IAL WMA/WME/WST + old-register C12/C34, CIE 9709 session codes, CIE 0580 "
    + "extended papers, Edexcel 4MA1/4MB/4PM) + 392 spec rows from the uncoded teaching pool under the tightened "
    + "distinctive-token rule; 13 maths courses leave the honest-empty set (ial pure 1-4, statistics-1, CIE pure "
    + "1-3 and p&s-1/2 at a-level and as; 25-core stays honest-empty - the channel walks extended papers only; "
    + "ial-further-maths-18-further-pure-1 honestly takes 0 rows); GCE/9MA0 and OCR/AQA papers honestly skipped "
    + "per ANCHOR-GRANULARITY section 6; P9 rows on 25-extended and a-18-higher cascade to their inherit children); "
    + "P10 two-pool maths completion: 358 owner-reviewed rows onto 10 maths courses (35 Tier B IAL paper-code anchors + 323 Tier A spec rows; "
    + "statistics-2 and further-pure-1 created fresh, mechanics-2 gains first native rows; legacy 1MA0/GCE/FP2 pools honest no-target); "
    + "P11 multi-cluster uncovered-course lane: 616 owner-reviewed rows onto 33 courses from fourteen channel pools "
    + "(3,116 uploads, 0 overlap with the shipped union): 33 Tier B syllabus/paper-code anchors (9708/41, 0455/0620 session papers, "
    + "WDM11, WMA11-14, 4MA1) + 583 spec rows via the distinctive-token pre-pass, explicit-code class tables, section-marker "
    + "narrowing and per-row re-adjudication; 439/439 oEmbed author==channel-of-record; 22 previously uncovered courses gain "
    + "their first video rows (the CIE IGCSE business/econ/accounting/ICT/CS/EM/geography/English-language pairs, CIE AS+A "
    + "computer science and accounting, CIE A-level economics, Edexcel IGCSE business/geography/ICT, and the last honest-empty "
    + "maths unit ial-maths-20-decision-1 via Mindful Maths' WDM11 chapter course); covered maths/science courses gain increments "
    + "(IAL FP1, pure-1..4 paper anchors, a-18-higher, CIE physics/maths); honest skips 2,466 incl. EconplusDal's UK GCE econ pool "
    + "(760, no Edexcel econ qualification in the spine), GCSE-English register (170), CIE ESL 0510/0511 (54), CIE A-level history "
    + "9489 and O-level US history 0409, predicted/summary compilations; igcse-history-17, cie-igcse-history-18 and "
    + "igcse-economics-17 re-adjudicated course-level to honest unmapped after degenerate single-token binds were caught on review. "
    + "P12 narrow CIE cluster lane: 119 owner-reviewed rows onto the five remaining CIE-native uncovered courses (9609 AS+A "
    + "business x2, 9696 A-level geography, 8291 AS environmental management, 8021 AS general paper) from eleven pools "
    + "(3,642 uploads, 0 overlap with the shipped union): 6 Tier B session/paper-code anchors (9609/42|22|12 O/N/26 predictions, "
    + "8021 GP session papers) + 113 Tier A spec rows via the deduped distinctive-token rule, the four-gate topic-lecture class "
    + "(verbatim / multi-uniq / title-token / title-pair — full-topic lectures bind their topic's spec points as one multi-spec "
    + "row at confidence low, disclosed per row) and N.M section-marker narrowing; oEmbed 119/119 author==channel-of-record; "
    + "honest skips 304 (technique/guidance registers, generic mentions, out-of-lane IGCSE registers); the Edexcel "
    + "English/history/accounting/econ units and RS are declared terminal honest-empty. "
    + "binds re-adjudicated to skips on review. P13 Alt Academy family lane: 650 owner-reviewed rows onto 19 courses "
    + "(650 = 24 Tier B paper-code anchors + 626 Tier A spec rows) from ONE brand's nine channels (the CAIE-native "
    + "multi-subject hub @altacademyorg + 8 subject channels; 985 uploads inventoried, 0 intra-family overlap, 0 overlap "
    + "with the shipped union beyond the 75-video business subject channel that IS the P12 pool): the dominant class is "
    + "the section-name binding (the Alt Academy format names the syllabus section verbatim in a pipe-field — the "
    + "section's TOPIC/SUBTOPIC spec points bind as ONE multi-spec row at confidence low through the verbatim "
    + "field-equality gate, disclosed per row) + distinctive-token binds (df<=3), the four-gate topic-lecture class, N.M "
    + "section-marker narrowing and maths unit-token routing (S2/S1/M1/P1/P2/P3 to the spine's unit courses, shared units "
    + "bound to BOTH the AS and A-level course); CIE paper-number routing per subject for the anchors (sciences papers "
    + "1-3 AS / 4-5 A2; econ/business/accounting by paper level); oEmbed 587/587 author==channel-of-record; honest skips "
    + "310 (guidance/advice/marketing registers, the O-Level register, meta videos, CIE 9990 psychology — no spine "
    + "course — and 2 degenerate generic-token binds re-adjudicated to skips on review); chemistry/econ/accounting/maths "
    + "courses gain their largest single-lane increments (cie-a-level-economics-23 44->134 videos, accounting-21 pair "
    + "roughly triples, maths p&s-1/p&s-2 gain their first real spec coverage); the AS inherit children with direct rows "
    + "(cie-as-chemistry-25, cie-as-physics-25) append post-inherit via P13B. "
    + "P14 channel recon judgment lane: 3,138 owner-reviewed rows onto 34 courses (1,012 Tier B paper-code anchors + 2,126 spec "
    + "rows at 255 medium / 1,871 low) from twelve judgment pools (T1 x10 + T2 x2, 18,005 of the 24,395 uploads inventoried at "
    + "filing, 0 overlap with the shipped union and all prior lane inventories) + the Allery-CIE re-adjudication group (26 "
    + "shipped of 41 candidates reproduced over the P2F pool of record): the P13 gate ladder extended with CIE paper-number "
    + "routing incl. compact ON/MJ/FM session forms and the qp_NN paper-store pattern (ETphysics / Prosperity / CK / Sir "
    + "Faizan 9702; Prosperity 9701/9700), 0580 papers 2/4 extended vs 1/3 core with Zainematics spine-code precedence over "
    + "O-Level branding (405/411 + 188/188 dual-coded titles route; 0606 -> further-maths-additional-25, 9618 -> the CS pair), "
    + "WMA01 C12/C34 IAL-legacy composites -> two units each (124 ExamSolutions anchors), IAL chemistry Unit-N session "
    + "anchors (73 Assil rows onto the 44/319 deficit pool), the Craig'n'Dave CAMBRIDGE 0478 numbered series, Science with "
    + "Hazel's Edexcel-IGCSE register, Mega Lecture no-code AS/A2 class series under the P13 register law and IGCSESUCCESS "
    + "FLE 0500 register rows; ExamSolutions bare GCE session walkthroughs SKIP per ANCHOR-GRANULARITY section 6 (the P9 "
    + "precedent); oEmbed identity 2,900/2,900 unique videos author==channel-of-record (1 thumbnail-liveness fallback "
    + "disclosed per the P2D law); honest skips 21,527 ledgered by class with exactly-once disposition of all 24,486 "
    + "accounts incl. 9 RESERVED lit-21 titles pending the owner decision; the five P4-children with direct rows "
    + "(cie-as-biology-25, cie-as-chemistry-25, cie-as-physics-25, cie-igcse-maths-25-core, ial-chemistry-17) append "
    + "post-inherit via P14B. "
    + "P15 discovery judgment lane: 1,562 owner-reviewed rows onto 32 courses (1,033 Tier B paper-code anchors + 529 spec rows at 529 low / 0 medium) from eighteen discovery pools (T1 x14 + T2 x4; 5,591 uploads found by the gap-targeted search sweep over the corpus residual — 4,711 unmapped spec points, 24 gap clusters, 231 channels harvested, 0 overlap with the shipped union 8,783 incl. P14 AND all prior lane inventories 38,773 AND 0 intra-P15): CIE IGCSE sciences 0610/0620/0625 session/paper registers (chem bio by Hosni — the densest find of the sweep, 0610 x342 + WBI x213 over the two biggest residual gaps — CAIE made easier, Learn Today IGCSE), 0654/0653 shared-paper anchors binding all three sciences of the family (the P13 shared-unit precedent; Science and Stuff), 0417/4IT0 ICT dual register (Nicos Paphitis 0417 x121; Mark Harrison Ed-ICT/CS x93 + 0417 x58), 4MA1 maths-A higher/foundation/modular-24 routing (The Math Pad x197 + Libra Maths x127 — 339 rows onto a-18-higher alone), 0606 additional maths (127 rows onto further-maths-additional-25 via Libra/Gilbert Phoon/Shawn Hew), IAL WPH/WBI/WCH Unit-N session anchors per the P14 Assil law analog (Doctor No Does Science WPH x74 -> ial-physics-19; Hosni WBI -> ial-biology-18), 0452 accounting (Keen Mindz x64 at 100% register), 0455/9708 economics (Learn Economics with Anjuli), 0680/8291 environmental management (Dr. Maria Emam + Everything E.M.), 0460/4GE0 geography (GEO-HACKS), 0500 FLE (Taughtly, both english-language courses), Edexcel IGCSE chemistry/biology (Belal Sir, the AQA-only remainder skipped honestly); oEmbed identity 1,365/1,365 routed videos author==channel-of-record (0 mismatch, 0 dead, 0 thumb fallbacks); honest skips 3,983 ledgered by class with exactly-once disposition of all 5,591 accounts incl. 243 RESERVED lit-0475 titles (Claire Notes) folded into the lit-21 owner decision point; the eleven P4-children with direct rows (the 0654 trio, ial-physics-19, ial-biology-18, ial-chemistry-17, igcse-maths-a-18-foundation, the igcse-maths-a-modular-24 units x4) append post-inherit via P15B. "
    + "P16 lit-21 opening lane: the owner's 2026-11-20 decision \"open lit-21\" overturns the P12 terminal declaration for cie-igcse-english-literature-21 (that course only) and admits the first-ever lit-21 content — the 252 RESERVED lit-0475 titles (P14 IGCSESUCCESS 0475 x9 + P15 Claire's Notes x243) adjudicated onto the freshly opened course: 100 owner-reviewed rows (56 medium / 44 low) binding 101 of 203 spec points through Class W set-text work binds (Songs of Ourselves Vol 1 P4 / Vol 2 P3 / Vol 2 P4 poem guides incl. the full 2025 Part 3 list, the Ted Hughes 15 pair-lines, Othello x23 / A Midsummer Night's Dream x5 / Journey's End x8 / Twelfth Night x2 / A Streetcar Named Desire scene commentary across their per-year drama specs, the Stories of Ourselves Vol 2 story guides); suffix-anchored match rule with the author cross-check, multi-year occurrences disclosed per row (the P13 shared-unit precedent), multi-work tips rows as ONE multi-spec row at low, oEmbed identity 100/100 author==channel-of-record (0 fallbacks); honest skips 152 ledgered by class (scripts/p16/skips.json: no-set-text 106 incl. Macbeth/Kumukanda/the AQA anthologies, character-study 15, out-of-spine board 16, guidance 15); exactly-once disposition of all 252 reserved accounts, 0 collisions. "
    + "Links resolve lessonUrl (site lane, Cognito) then watchUrl (external lanes, YouTube). Rows are "
    + "owner-reviewed (title-only evidence, confidence + boardMismatch disclosed per row; inherited rows carry "
    + "their derivation in inherit); the loader re-filters reviewed:true as defense in depth. One-flip kill "
    + "unchanged: remove the slug (per-course) or the videoMap key (global).";
  writeFileSync(flagsPath, JSON.stringify(flags, null, 1) + "\n");
  console.log(`wrote ${flagsPath} (videoMap.courses now ${flags.flags.videoMap.courses.length} courses)`);
}
