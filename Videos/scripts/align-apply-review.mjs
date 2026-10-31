#!/usr/bin/env node
/**
 * align-apply-review.mjs — F189 P2 §5 Step 4: apply the owner's review verdicts.
 *
 * Reads owner-review-verdicts.json (default: approve; explicit rejects listed)
 * and applies it, in place, to:
 *   1. video-map.draft.json — approved rows flip reviewed:true (+reviewer,
 *      reviewedUtc); rejected rows stay reviewed:false and carry a reviewNote
 *      (append-with-reason, plan §4.2 rules — nothing is silently deleted);
 *      reviewState → owner-reviewed-p2; coverage gains a recomputed
 *      `reviewed` census (what would ship).
 *   2. review-file.md — approved rows' checkboxes ticked; the rejected row
 *      gets a REJECTED annotation; header records the ruling + evidence basis.
 *
 * NEVER run align-build-draft.mjs after this — it is the pre-review builder
 * and resets every row to reviewed:false.
 *
 * Usage: node align-apply-review.mjs [course=igcse-biology-19]
 */

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const VIDEOS = resolve(__dirname, "..");
const COURSE = process.argv[2] || "igcse-biology-19";
const D = join(VIDEOS, "drafts", COURSE);

const verdicts = JSON.parse(readFileSync(join(D, "owner-review-verdicts.json"), "utf8"));
const draftPath = join(D, "video-map.draft.json");
const draft = JSON.parse(readFileSync(draftPath, "utf8"));

const isRejected = (m) =>
  (verdicts.rejects || []).some(
    (r) => r.lessonRef === m.lessonRef && r.video === m.video && m.specs.includes(r.spec)
  );

let approved = 0;
let rejected = 0;
const rejectedRows = [];

for (const m of draft.mappings) {
  m.reviewer = verdicts.reviewer;
  m.reviewedUtc = verdicts.ruledUtc;
  if (isRejected(m)) {
    m.reviewed = false;
    m.reviewNote = `REJECTED by owner (${verdicts.ruledUtc.slice(0, 10)}) — ruling "${verdicts.source}": ${
      (verdicts.rejects.find((r) => r.lessonRef === m.lessonRef && r.video === m.video && m.specs.includes(r.spec)) || {}).reason
    }`;
    rejected++;
    rejectedRows.push(m);
  } else {
    m.reviewed = true;
    approved++;
  }
}

// reviewed census — recomputed from the mappings, never hand-written
const reviewedRows = draft.mappings.filter((m) => m.reviewed);
const rvSpecs = new Set(reviewedRows.flatMap((m) => m.specs));
const rvVideos = new Set(reviewedRows.map((m) => m.video));
draft.coverage.reviewed = {
  mappingRows: reviewedRows.length,
  specPointsMapped: rvSpecs.size,
  specPointsUnmapped: draft.coverage.specPointsTotal - rvSpecs.size,
  videosMapped: rvVideos.size,
  byConfidence: {
    high: reviewedRows.filter((m) => m.confidence === "high").length,
    medium: reviewedRows.filter((m) => m.confidence === "medium").length,
    low: reviewedRows.filter((m) => m.confidence === "low").length,
  },
};
draft.reviewState = "owner-reviewed-p2";
draft.draftLaw =
  "draft law honoured end-to-end: built reviewed:false (align-build-draft.mjs), review applied in place 2026-11-01 " +
 `("${verdicts.source}" — ${approved} approved, ${rejected} rejected with reviewNote); only reviewed:true rows ` +
 "enter content/video-map/ (plan §4.2 rules; A1)";
draft.generatedUtc = new Date().toISOString();

writeFileSync(draftPath, JSON.stringify(draft, null, 2) + "\n");

// ---------------------------------------------------------------- review file
const rfPath = join(D, "review-file.md");
let rf = readFileSync(rfPath, "utf8");

// 1. header — draft-stage note becomes the review record
rf = rf.replace(
  /\*\*Draft stage\.\*\*[\s\S]*?reach `content\/video-map\/igcse-biology-19\.json`\./,
  `**Review applied (${verdicts.ruledUtc.slice(0, 10)}).** Owner ruling, verbatim: "${verdicts.source}" — ` +
  `${approved} of ${approved + rejected} rows approved and flipped to \`reviewed: true\`; the rejected row is annotated ` +
  `below and stays \`reviewed: false\` (it never ships). Evidence basis: page keyPoints + oEmbed identity sweep ` +
  `(73/73 official titles, caption-validation.json/.md); the transcript thread is CLOSED after 30 logged paths, so ` +
  `medium rows are topic-consistent, clause-level unverified. Only \`reviewed: true\` rows reach ` +
  `\`content/video-map/${COURSE}.json\` (plan §5 Step 5).`
);

// 2. tick approved rows (every line whose row signature matches an approved row)
const tickSig = (m) => `video \`${m.video}\` → specs \`${m.specs.join("`, `")}\``;
const rejectedSigs = new Set(rejectedRows.map(tickSig));
let ticked = 0;
rf = rf
  .split("\n")
  .map((line) => {
    if (!line.startsWith("- [ ]")) return line;
    const vid = (line.match(/video `([^`]+)`/) || [])[1];
    const specPart = (line.match(/specs ((?:`[^`]+`)(?:, `[^`]+`)*)/) || [])[1];
    const specs = specPart ? [...specPart.matchAll(/`([^`]+)`/g)].map((x) => x[1]) : null;
    if (!vid || !specs) return line;
    const key = `video \`${vid}\` → specs \`${specs.join("`, `")}\``;
    if (rejectedSigs.has(key)) return line; // stays unticked
    ticked++;
    return line.replace("- [ ]", "- [x]", 1);
  })
  .join("\n");

// 3. annotate the rejected row (after its evidence line)
for (const m of rejectedRows) {
  const sig = tickSig(m);
  const re = new RegExp(
    `(- \\[ \\] \\*\\*[^*]+\\*\\* — ${sig.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\n      evidence: [^\\n]+\\n)`
  );
  if (!re.test(rf)) throw new Error(`rejected row line not found in review file: ${sig}`);
  rf = rf.replace(
    re,
    `$1      **REJECTED by owner (2026-11-01)** — see reviewNote in video-map.draft.json; spec falls back to the honest no-video list.\n`
  );
}

// 4. annotate approved-but-flagged rows (4.12 carried a reject-unless-scanned note)
rf = rf.replace(
  /(video `cickRHnPKvc` → specs `4\.12`\n      evidence: [^\n]+\n)/,
  `$1      **APPROVED by owner (2026-11-01)** — ruling covered this row ("all except 4.16"); the validation note stands as a caveat: a 60-second scrub of the CO/haemoglobin clause can reopen it (append-with-reason, plan §4.2).\n`
);

writeFileSync(rfPath, rf);

// ------------------------------------------------------------------- report
console.log(`applied verdicts from ${join(D, "owner-review-verdicts.json")}`);
console.log(`approved: ${approved} · rejected: ${rejected} · checkboxes ticked: ${ticked}`);
console.log(`reviewed census: specs ${draft.coverage.reviewed.specPointsMapped}/${draft.coverage.specPointsTotal} · videos ${draft.coverage.reviewed.videosMapped}/${draft.videos.length} · rows ${draft.coverage.reviewed.mappingRows} (${draft.coverage.reviewed.byConfidence.high}H/${draft.coverage.reviewed.byConfidence.medium}M/${draft.coverage.reviewed.byConfidence.low}L)`);
if (ticked !== approved) throw new Error(`tick mismatch: ticked ${ticked} != approved ${approved}`);
if (rf.includes("- [ ] ") && rejected === 0) throw new Error("unticked rows remain but no rejects recorded");
