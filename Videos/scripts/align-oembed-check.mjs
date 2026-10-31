#!/usr/bin/env node
/**
 * align-oembed-check.mjs — F189 P2 review-support: video identity sweep.
 *
 * For every distinct video id in a course draft, fetch YouTube's public
 * oEmbed endpoint (unsigned, NOT bot-walled from this environment — verified
 * 2026-10-31) and record the official title + author. This is an
 * *identity* cross-check (does the id resolve, is it a Cognito video, does
 * the video title match the lesson topic), NOT a content check — captions
 * could not be fetched from this environment (see caption-validation.json
 * for the full attempt log).
 *
 * Output: Videos/drafts/<course>/oembed-identities.json
 *
 * Usage: node align-oembed-check.mjs [course=igcse-biology-19]
 */

import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const VIDEOS = resolve(__dirname, "..");
const COURSE = process.argv[2] || "igcse-biology-19";
const draftPath = join(VIDEOS, "drafts", COURSE, "video-map.draft.json");
const outPath = join(VIDEOS, "drafts", COURSE, "oembed-identities.json");

const draft = JSON.parse(readFileSync(draftPath, "utf8"));
const videoIds = [...new Set(draft.videos.map((v) => (typeof v === "string" ? v : v.id)))];

const UA = "SyllabAI-VideoMap/1.0 (F189 P2 identity sweep; contact via github.com/SyllabAI)";
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function oembed(id) {
  const url = `https://www.youtube.com/oembed?url=${encodeURIComponent(`https://www.youtube.com/watch?v=${id}`)}&format=json`;
  const res = await fetch(url, { headers: { "user-agent": UA } });
  if (!res.ok) return { id, status: res.status, ok: false };
  const d = await res.json();
  return {
    id,
    ok: true,
    status: 200,
    title: d.title ?? null,
    author: d.author_name ?? null,
    authorUrl: d.author_url ?? null,
  };
}

const out = { generatedUtc: new Date().toISOString(), course: COURSE, note: "YouTube oEmbed identity sweep over all distinct draft video ids. Identity evidence only — not spoken-content validation (captions unobtainable from this environment, see caption-validation.json).", results: [] };

let okCount = 0;
for (const id of videoIds) {
  let rec = null;
  for (let attempt = 0; attempt < 3 && !rec; attempt++) {
    try {
      rec = await oembed(id);
      if (!rec.ok) rec = null; // retry on non-200
    } catch (e) {
      rec = null;
    }
    if (!rec) await sleep(1500);
  }
  if (!rec) rec = { id, ok: false, status: "unreachable-after-retries" };
  if (rec.ok) okCount++;
  out.results.push(rec);
  process.stdout.write(`${rec.ok ? "ok " : "ERR"} ${id} ${rec.title ?? rec.status}\n`);
  await sleep(400 + Math.floor(Math.random() * 250));
}

out.totals = { videos: videoIds.length, resolved: okCount, unresolved: videoIds.length - okCount };
writeFileSync(outPath, JSON.stringify(out, null, 1) + "\n");
console.log(`\noembed sweep: ${okCount}/${videoIds.length} resolved → ${outPath}`);
process.exit(0);
