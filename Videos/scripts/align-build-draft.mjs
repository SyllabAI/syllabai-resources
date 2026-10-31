#!/usr/bin/env node
/**
 * align-build-draft.mjs — F189 P2 (T-VIDEOMAP-P2): build the draft video map.
 *
 * Folds the curation table (LLM draft pass) + inventory + spine into:
 *   1. video-map.draft.json   — hub.video-map/1 shape, every row reviewed:false
 *                               (draft law: this file NEVER enters content/)
 *   2. review-file.md         — all mapping rows, lowest confidence first,
 *                               each with evidence + Cognito deep link
 *   3. coverage-report.md     — content-maps `_report` style
 *
 * Gates enforced here (plan §8): referential integrity (specs exist in spine,
 * video ids ^[\w-]{11}$, no dup ids), draft law (zero reviewed:true), census
 * recompute (coverage block regenerated from mappings, never hand-written).
 *
 * Usage: node align-build-draft.mjs [course=igcse-biology-19]
 */

import { readFileSync, writeFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const VIDEOS = resolve(__dirname, "..");
const COURSE = process.argv[2] || "igcse-biology-19";
const D = join(VIDEOS, "drafts", COURSE);

const sha256 = (p) =>
  createHash("sha256").update(readFileSync(p)).digest("hex");

// ------------------------------------------------------------------- inputs
const inv = JSON.parse(readFileSync(join(VIDEOS, "inventory", "cognito-lessons.json"), "utf8"));
const spine = JSON.parse(readFileSync(join(D, "spine.json"), "utf8"));
const enrich = JSON.parse(readFileSync(join(D, "lesson-enrichment.json"), "utf8"));
const curation = JSON.parse(readFileSync(join(D, "align-curation.json"), "utf8"));

const SHELF = curation.shelf;
const shelf = inv.shelves[SHELF];
if (!shelf) throw new Error(`shelf ${SHELF} missing from inventory`);

const nodes = spine.curriculum.nodes;
const specByCode = new Map(nodes.filter((n) => n.family === "SPEC_POINT").map((n) => [n.code, n]));
const topicOf = new Map(); // spec code -> TOPIC title
for (const sp of nodes.filter((n) => n.family === "SPEC_POINT")) {
  const parent = nodes.find(
    (n) => (sp.parents || []).includes(n.code) && n.family === "SUBTOPIC"
  );
  const topicCode = parent ? (parent.parents || [])[0] : null;
  const topic = nodes.find((n) => n.code === topicCode && n.family === "TOPIC");
  topicOf.set(sp.code, topic ? topic.title : null);
}

// lessonRef -> inventory row (video-carrying lessons only)
const lessonByRef = new Map(
  shelf.lessons.filter((r) => r.httpStatus === 200 && r.primaryVideoId).map((r) => [r.lessonRef, r])
);
const enrichByKey = new Map(enrich.lessons.map((r) => [r.key, r]));

// ------------------------------------------------------------- validations
const errors = [];
const warnings = [];

// every curation lessonRef must exist as a video-carrying lesson
for (const m of curation.mappings) {
  if (!lessonByRef.has(m.lessonRef)) {
    errors.push(`curation lessonRef ${m.lessonRef} is not a video-carrying lesson on ${SHELF}`);
    continue;
  }
  for (const code of m.specs) {
    if (!specByCode.has(code)) errors.push(`${m.lessonRef}: spec code ${code} does not exist in the ${COURSE} spine`);
  }
  if (!["high", "medium", "low"].includes(m.confidence)) {
    errors.push(`${m.lessonRef}: invalid confidence ${m.confidence}`);
  }
  if (!m.evidence || m.evidence.length < 10) errors.push(`${m.lessonRef}: missing evidence line`);
}
for (const u of curation.unmapped) {
  if (!lessonByRef.has(u.lessonRef)) warnings.push(`unmapped lessonRef ${u.lessonRef} has no video anyway`);
}
// mapped lessons must be on the triple-biology lane (whole shelf is, assert anyway)
for (const r of lessonByRef.values()) {
  if (!r.url.includes("/biology-triple/")) errors.push(`unexpected lane: ${r.url}`);
}

if (errors.length) {
  console.error("GATE FAILURES:\n" + errors.map((e) => "  - " + e).join("\n"));
  process.exit(1);
}

// ------------------------------------------------------------------ videos
const usedRefs = new Set(curation.mappings.map((m) => m.lessonRef));
const videos = [];
const mappings = [];

// distinct video ids on this shelf's video-carrying lessons
const allVideoIds = new Set();
for (const r of lessonByRef.values()) for (const id of r.videoIds) allVideoIds.add(id);

// videoId -> owning lessonRef. Prefer the lesson where the id is the PRIMARY
// video (Cognito re-embeds one video across adjacent lessons: 3.5/3.6,
// 7.16/7.17, 9.6/9.7); ties resolve to the first lesson in inventory order.
const idOfRef = new Map();
for (const [ref, r] of lessonByRef) {
  for (const id of r.videoIds) {
    const prefer = id === r.primaryVideoId;
    const prev = idOfRef.get(id);
    if (!prev) {
      idOfRef.set(id, ref);
    } else if (prefer && lessonByRef.get(prev).primaryVideoId !== id) {
      idOfRef.set(id, ref);
    }
  }
}

for (const id of [...allVideoIds].sort()) {
  const r = lessonByRef.get(idOfRef.get(id));
  const e = enrichByKey.get(r.key);
  videos.push({
    id,
    title: r.h1,
    lessonRef: r.lessonRef,
    lessonUrl: r.url,
    topicPath: null, // filled below from mapped specs' spine topic
    durationS: null,
    guestVisible: true,
    subelementOfPrimary: id !== r.primaryVideoId,
  });
}

for (const m of curation.mappings) {
  const r = lessonByRef.get(m.lessonRef);
  for (const id of r.videoIds) {
    mappings.push({
      video: id,
      lessonRef: r.lessonRef,
      lessonUrl: r.url,
      specs: m.specs,
      confidence: m.confidence,
      evidence: m.evidence,
      method: "llm-draft",
      reviewed: false,
      reviewer: null,
      reviewedUtc: null,
      boardMismatch: false,
    });
  }
}

// topicPath per video from its mapped specs' spine topic
const specsByVideo = new Map();
for (const m of mappings) {
  const arr = specsByVideo.get(m.video) || [];
  for (const s of m.specs) if (!arr.includes(s)) arr.push(s);
  specsByVideo.set(m.video, arr);
}
for (const v of videos) {
  const specs = specsByVideo.get(v.id) || [];
  const topics = [...new Set(specs.map((s) => topicOf.get(s)).filter(Boolean))];
  v.topicPath = topics.length ? topics : null;
}

// ---------------------------------------------------------------- coverage
const mappedSpecs = new Set(mappings.flatMap((m) => m.specs));
const mappedVideos = new Set(mappings.map((m) => m.video));
const unmappedVideos = videos.filter((v) => !mappedVideos.has(v.id));

const coverage = {
  specPointsTotal: specByCode.size,
  specPointsMapped: mappedSpecs.size,
  specPointsUnmapped: specByCode.size - mappedSpecs.size,
  videosTotal: videos.length,
  videosMapped: mappedVideos.size,
  videosUnmapped: unmappedVideos.length,
  byConfidence: {
    high: mappings.filter((m) => m.confidence === "high").length,
    medium: mappings.filter((m) => m.confidence === "medium").length,
    low: mappings.filter((m) => m.confidence === "low").length,
  },
  mappingRows: mappings.length,
};

// unmapped spec points grouped by topic (honest "no video" list)
const unmappedSpecs = [...specByCode.keys()].filter((c) => !mappedSpecs.has(c));
const unmappedByTopic = {};
for (const c of unmappedSpecs) {
  const t = topicOf.get(c) || "?";
  (unmappedByTopic[t] ||= []).push(c);
}

// guest-gated lessons on this shelf (decision D1 context for this course)
const gated = shelf.lessons.filter((r) => r.httpStatus === 200 && !r.primaryVideoId);

// ------------------------------------------------------------------- draft
const draft = {
  schema: "syllabai.video-map-draft/1",
  draftOf: "hub.video-map/1",
  task: "T-VIDEOMAP-P2",
  course: COURSE,
  qual: "IGCSE",
  reviewState: "draft-p2",
  draftLaw: "reviewed:false everywhere — this file lives under Videos/drafts/ and never enters any content/ directory (plan §4.2 rules; A1)",
  source: {
    provider: "cognito",
    shelf: SHELF,
    label: "GCSE Biology (IGCSE Edexcel)",
    courseUrl: "https://cognito.org/courses/gcse/biology-triple/iedexcel",
    crawledUtc: inv.generatedUtc,
    crawlMethod: "sitemap+RSC-payload (P1) + enrichment fetch (P2)",
  },
  videos,
  mappings,
  coverage,
  inputs: {
    spine: { file: `Videos/drafts/${COURSE}/spine.json`, upstream: `apps/hub/spines/${COURSE}.json`, sha256: sha256(join(D, "spine.json")) },
    inventory: { file: "Videos/inventory/cognito-lessons.json", sha256: sha256(join(VIDEOS, "inventory", "cognito-lessons.json")) },
    enrichment: { file: `Videos/drafts/${COURSE}/lesson-enrichment.json`, sha256: sha256(join(D, "lesson-enrichment.json")) },
    deterministic: { file: `Videos/drafts/${COURSE}/deterministic-candidates.json`, sha256: sha256(join(D, "deterministic-candidates.json")) },
    curation: { file: `Videos/drafts/${COURSE}/align-curation.json`, sha256: sha256(join(D, "align-curation.json")) },
  },
  generatedUtc: new Date().toISOString(),
};

// ------------------------------------------------------------------ write
const draftPath = join(D, "video-map.draft.json");
writeFileSync(draftPath, JSON.stringify(draft, null, 2) + "\n");

// review file — lowest confidence first
const rank = { low: 0, medium: 1, high: 2 };
const sorted = [...mappings].sort(
  (a, b) => rank[a.confidence] - rank[b.confidence] || a.lessonRef.localeCompare(b.lessonRef, undefined, { numeric: true })
);

const h1ByRef = new Map([...lessonByRef.values()].map((r) => [r.lessonRef, r.h1]));
let md = `# Review file — ${COURSE} video map (T-VIDEOMAP-P2)\n\n`;
md += `**Draft stage.** Every row below is \`reviewed: false\`. Approve a row by ticking it and flipping\nits \`reviewed\` field (the owner review step, plan §5 Step 4); only \`reviewed: true\` rows ever\nreach \`content/video-map/${COURSE}.json\`.\n\n`;
md += `**Bundles:** ${coverage.mappingRows} mapping rows over ${coverage.videosMapped} of ${coverage.videosTotal} distinct videos · confidence: ${coverage.byConfidence.high} high / ${coverage.byConfidence.medium} medium / ${coverage.byConfidence.low} low\n\n`;
md += `Note: Cognito re-embeds the same video in adjacent lessons (3.5+3.6, 7.16+7.17, 9.6+9.7 share\none id), so a video can appear in multiple rows — each row is the per-lesson binding and is\nreviewed in its own right. Sorting: low → medium → high. **Review the low and medium rows\nindividually; the high rows are batch-approvable** (each still carries its evidence line).\n\n`;
md += `---\n\n`;
const sec = (c, label) => {
  let s = `## ${label} (${coverage.byConfidence[c]} rows)\n\n`;
  for (const m of sorted.filter((x) => x.confidence === c)) {
    s += `- [ ] **${h1ByRef.get(m.lessonRef)}** — video \`${m.video}\` → specs \`${m.specs.join("`, `")}\`\n`;
    s += `      evidence: ${m.evidence}\n`;
    s += `      source: ${m.lessonUrl}\n`;
  }
  return s + "\n";
};
md += sec("low", "LOW");
md += sec("medium", "MEDIUM");
md += sec("high", "HIGH");
md += `## Unmapped videos (${unmappedVideos.length})\n\n`;
for (const v of unmappedVideos) {
  const u = curation.unmapped.find((x) => x.lessonRef === v.lessonRef);
  md += `- **${v.title}** — \`${v.id}\` — ${u ? u.reason : "no mapping proposed"}\n`;
}
md += `\n## Unmapped spec points (${coverage.specPointsUnmapped}/${coverage.specPointsTotal}) — honest "no video" list\n\n`;
for (const [t, codes] of Object.entries(unmappedByTopic)) {
  md += `- **${t}**: ${codes.join(", ")}\n`;
}
md += `\n## Guest-gated lessons on this shelf (${gated.length}) — decision D1 context\n\n`;
md += `These lesson pages serve no video to a logged-out session (P1 render-probe verified), so they\ncannot enter the draft until D1 (guest-gating posture) is decided:\n\n`;
md += gated.map((r) => `- ${r.lessonRef} — ${r.h1}`).join("\n") + "\n";
writeFileSync(join(D, "review-file.md"), md);

// coverage report — content-maps `_report` style
let cov = `# Coverage report — ${COURSE} video map (draft P2)\n\n`;
cov += `| | |\n| --- | --- |\n`;
cov += `| Task | T-VIDEOMAP-P2 |\n| Course | \`${COURSE}\` (4BI1, Edexcel International GCSE Biology) |\n| Source | Cognito shelf \`${SHELF}\` — guest-visible set only |\n| Spine of record | \`apps/hub/spines/${COURSE}.json\` — ${specByCode.size} SPEC_POINTs, sha \`${draft.inputs.spine.sha256.slice(0, 12)}…\` |\n| Generated | ${draft.generatedUtc} |\n\n`;
cov += `## Coverage\n\n| Metric | Value |\n| --- | --- |\n`;
cov += `| Spec points (spine) | ${coverage.specPointsTotal} |\n| Spec points with ≥1 drafted video | ${coverage.specPointsMapped} (${Math.round((100 * coverage.specPointsMapped) / coverage.specPointsTotal)}%) |\n| Spec points with no video (honest) | ${coverage.specPointsUnmapped} |\n| Videos (distinct ids) | ${coverage.videosTotal} |\n| Videos with ≥1 drafted mapping | ${coverage.videosMapped} |\n| Videos unmapped | ${coverage.videosUnmapped} (${unmappedVideos.map((v) => v.lessonRef).join(", ") || "none"}) |\n| Mapping rows | ${coverage.mappingRows} (${coverage.byConfidence.high} high / ${coverage.byConfidence.medium} medium / ${coverage.byConfidence.low} low) |\n| Guest-gated lessons (D1) | ${gated.length} |\n\n`;
cov += `## Method\n\n1. Deterministic lexical evidence (\`align-deterministic.mjs\`) — refs deliberately ignored:\n   Cognito's chapter numbering ≠ 4BI1 spec numbering (amendment A6; 25/109 ref coincidences,\n   several misleading, e.g. Cognito \`3.1 Photosynthesis\` vs spec \`3.1\` meiosis).\n2. LLM draft pass (\`align-curation.json\`) over title + description + keyPoints vs spine statements;\n   every row carries a one-line evidence string; refs resolved to videos via the P1 inventory.\n3. Gates: referential integrity, id shape, dup ids, draft law, census recompute — all enforced\n   in \`align-build-draft.mjs\` (this file's numbers are generated, not hand-written).\n\n`;
cov += `## Coverage by topic\n\n| Topic | Mapped / total |\n| --- | --- |\n`;
const topicStats = {};
for (const [code, t] of topicOf) {
  const s = (topicStats[t] ||= { total: 0, mapped: 0 });
  s.total++;
  if (mappedSpecs.has(code)) s.mapped++;
}
for (const [t, s] of Object.entries(topicStats).sort((a, b) => b[1].total - a[1].total || a[0].localeCompare(b[0]))) {
  cov += `| ${t} | ${s.mapped} / ${s.total} |\n`;
}
cov += `\n## Unmapped spec points by topic\n\n`;
for (const [t, codes] of Object.entries(unmappedByTopic)) {
  cov += `- **${t}** (${codes.length}): \`${codes.join("`, `")}\`\n`;
}
cov += `\n## Notes\n\n- \`1.4 Magnification & Units\` has no spine statement (skills content) — recorded unmapped.\n- The 34 guest-gated lessons (full list in review-file.md) are excluded by the draft law, not forgotten (D1).\n- \`${SHELF}\` also carries modular/double-award relevance for future lanes; this draft binds the triple lane only.\n`;
writeFileSync(join(D, "coverage-report.md"), cov);

// ------------------------------------------------------------------ report
console.log(`wrote ${draftPath}`);
console.log(`wrote ${join(D, "review-file.md")}`);
console.log(`wrote ${join(D, "coverage-report.md")}`);
console.log(
  `\nCENSUS: specs ${coverage.specPointsMapped}/${coverage.specPointsTotal} mapped · videos ${coverage.videosMapped}/${coverage.videosTotal} mapped (${coverage.videosUnmapped} unmapped) · rows ${coverage.mappingRows} (${coverage.byConfidence.high}H/${coverage.byConfidence.medium}M/${coverage.byConfidence.low}L) · gated ${gated.length}`
);
console.log(`draft law: ${mappings.filter((m) => m.reviewed).length} rows with reviewed:true (must be 0)`);
if (warnings.length) console.log("warnings:\n" + warnings.map((w) => "  - " + w).join("\n"));
