#!/usr/bin/env node
/**
 * build-content-map.mjs — F189 P2 §5 Step 5: build the committed hub content
 * file from the OWNER-REVIEWED draft.
 *
 * Input : Videos/drafts/igcse-biology-19/video-map.draft.json (reviewState
 *         owner-reviewed-p2 — run align-apply-review.mjs first) + spine.json
 * Output: <outDir>/igcse-biology-19.json  (schema hub.video-map/1, ONLY
 *         reviewed:true rows) and <outDir>/registry.json (loader index).
 *
 * Gates enforced here (plan §8): review law (zero reviewed:false in output),
 * referential integrity (every spec code exists in the course spine; every
 * video id ^[\w-]{11}$; no duplicate video ids; every mapping.video exists in
 * videos[]), coverage census recomputed from the emitted mappings and
 * asserted — never hand-written.
 *
 * Usage: node build-content-map.mjs <outDir>   (e.g. the hub clone's
 *        apps/hub/content/video-map/ directory)
 */

import { readFileSync, mkdirSync, writeFileSync, existsSync } from "node:fs";
import { createHash } from "node:crypto";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const VIDEOS = resolve(__dirname, "..");
const COURSE = "igcse-biology-19";
const D = join(VIDEOS, "drafts", COURSE);
const outDir = resolve(process.argv[2] || ".");
if (!existsSync(outDir)) mkdirSync(outDir, { recursive: true });

const sha256 = (p) => createHash("sha256").update(readFileSync(p)).digest("hex");

const draft = JSON.parse(readFileSync(join(D, "video-map.draft.json"), "utf8"));
const spine = JSON.parse(readFileSync(join(D, "spine.json"), "utf8"));
const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.json"), "utf8"));

if (draft.reviewState !== "owner-reviewed-p2") {
  throw new Error(`review law: draft reviewState is "${draft.reviewState}" — run align-apply-review.mjs first`);
}

// ------------------------------------------------------------------- gates
const errors = [];
const specByCode = new Map(
  spine.curriculum.nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n])
);
const reviewedRows = draft.mappings.filter((m) => m.reviewed === true);
const unreviewed = draft.mappings.length - reviewedRows.length;

for (const m of reviewedRows) {
  for (const code of m.specs) {
    if (!specByCode.has(code)) errors.push(`${m.lessonRef}: spec ${code} not in spine`);
  }
  if (!/^[\w-]{11}$/.test(m.video)) errors.push(`${m.lessonRef}: bad video id ${m.video}`);
  if (!m.reviewer || !m.reviewedUtc) errors.push(`${m.lessonRef}: reviewed row missing reviewer/reviewedUtc`);
}
const videoById = new Map(draft.videos.map((v) => [v.id, v]));
for (const v of draft.videos) {
  if (!/^[\w-]{11}$/.test(v.id)) errors.push(`videos[]: bad id ${v.id}`);
}
if (new Set(draft.videos.map((v) => v.id)).size !== draft.videos.length) {
  errors.push("videos[]: duplicate ids");
}
for (const m of reviewedRows) {
  if (!videoById.has(m.video)) errors.push(`${m.lessonRef}: mapping references unknown video ${m.video}`);
}
if (errors.length) {
  console.error("GATE FAILURES:\n" + errors.map((e) => "  - " + e).join("\n"));
  process.exit(1);
}

// ------------------------------------------------------------------ census
const mappedSpecs = new Set(reviewedRows.flatMap((m) => m.specs));
const mappedVideos = new Set(reviewedRows.map((m) => m.video));
const coverage = {
  specPointsTotal: specByCode.size,
  specPointsMapped: mappedSpecs.size,
  specPointsUnmapped: specByCode.size - mappedSpecs.size,
  videosTotal: draft.videos.length,
  videosMapped: mappedVideos.size,
  videosUnmapped: draft.videos.length - mappedVideos.size,
  mappingRows: reviewedRows.length,
  byConfidence: {
    high: reviewedRows.filter((m) => m.confidence === "high").length,
    medium: reviewedRows.filter((m) => m.confidence === "medium").length,
    low: reviewedRows.filter((m) => m.confidence === "low").length,
  },
};
// assert the draft's own reviewed census agrees (it was recomputed there too)
const dc = draft.coverage.reviewed;
if (dc && (dc.specPointsMapped !== coverage.specPointsMapped || dc.mappingRows !== coverage.mappingRows || dc.videosMapped !== coverage.videosMapped)) {
  throw new Error("census mismatch between draft.coverage.reviewed and recomputed coverage");
}

// ------------------------------------------------------------------ output
const strip = (m) => {
  const { method, reviewNote, ...rest } = m;
  return rest;
};
const content = {
  schema: "hub.video-map/1",
  course: COURSE,
  qual: draft.qual,
  source: draft.source,
  review: {
    task: draft.task,
    ruledUtc: verdicts.ruledUtc,
    ruling: verdicts.source,
    reviewer: verdicts.reviewer,
    evidenceBasis: verdicts.evidenceBasis,
    rowsApproved: reviewedRows.length,
    rowsRejected: unreviewed,
    rejects: (verdicts.rejects || []).map(({ lessonRef, video, spec, reason }) => ({ lessonRef, video, spec, reason })),
  },
  videos: draft.videos,
  mappings: reviewedRows.map(strip),
  coverage,
  inputs: {
    spine: { file: `apps/hub/spines/${COURSE}.json`, sha256: draft.inputs.spine.sha256 },
    draft: {
      repo: "SyllabAI/syllabai-resources",
      path: `Videos/drafts/${COURSE}/video-map.draft.json`,
      task: draft.task,
      reviewAppliedUtc: verdicts.ruledUtc,
    },
  },
  generatedUtc: new Date().toISOString(),
};

const registryPath = join(outDir, "registry.json");
let registry = { schema: "syllabai-hub.video-map-registry/1", generatedUtc: "", courses: {} };
if (existsSync(registryPath)) registry = JSON.parse(readFileSync(registryPath, "utf8"));
registry.courses[COURSE] = {
  videos: coverage.videosTotal,
  mapped: coverage.videosMapped,
  shelf: draft.source.shelf,
  updatedUtc: new Date().toISOString(),
};
registry.generatedUtc = new Date().toISOString();

writeFileSync(join(outDir, `${COURSE}.json`), JSON.stringify(content, null, 1) + "\n");
writeFileSync(registryPath, JSON.stringify(registry, null, 1) + "\n");

console.log(`wrote ${join(outDir, `${COURSE}.json`)}`);
console.log(`wrote ${registryPath}`);
console.log(
  `CENSUS (shipped): specs ${coverage.specPointsMapped}/${coverage.specPointsTotal} · videos ${coverage.videosMapped}/${coverage.videosTotal} · rows ${coverage.mappingRows} (${coverage.byConfidence.high}H/${coverage.byConfidence.medium}M/${coverage.byConfidence.low}L) · review law: ${unreviewed} unreviewed rows left in draft, 0 in content`
);
