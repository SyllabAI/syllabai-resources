#!/usr/bin/env node
/**
 * align-extract-lessons.mjs — F189 P2 (T-VIDEOMAP-P2): lesson-content enrichment
 * for alignment.
 *
 * P1 recorded WHAT video each lesson embeds; alignment needs WHAT the lesson
 * teaches. This script fetches the raw HTML of every lesson that carries a
 * primary video (guest-visible set) and pulls the semantic fields out of the
 * RSC flight payload the same way P1 did:
 *
 *   - description            one-line summary of the lesson
 *   - keyPoints[].text       the lesson's own learning points
 *   - keySummary             closing summary (when present)
 *   - videoCaptions[]        captions of type:"video" subelements (per-spec
 *                            teaching clips embedded in the lesson page)
 *   - intro                  the ":::intro … :::" markdown block
 *
 * Politeness mirrors P1: identifying UA, low concurrency, jittered delays,
 * retry + backoff, resumable raw cache under Videos/.cache/p2/ (gitignored).
 *
 * Usage:
 *   node align-extract-lessons.mjs <shelfId> [--refetch]
 *     shelfId defaults to b2-gcse-iedexcel
 *
 * Output:
 *   Videos/drafts/<course>/lesson-enrichment.json   (committed provenance)
 */

import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const VIDEOS = resolve(__dirname, "..");
const SHELF_ID = process.argv[2] || "b2-gcse-iedexcel";
const REFETCH = process.argv.includes("--refetch");

// course slug that owns this shelf (single lane today — triple biology only)
const COURSE = "igcse-biology-19";
const OUT_DIR = join(VIDEOS, "drafts", COURSE);
const CACHE_DIR = join(VIDEOS, ".cache", "p2");

const UA =
  "SyllabAI-VideoMap/1.0 (F189 P2 content alignment; contact via github.com/SyllabAI)";
const CONCURRENCY = 4;
const JITTER_MS = [250, 700];
const RETRIES = 3;

// ---------------------------------------------------------------- utilities
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const jitter = () =>
  JITTER_MS[0] + Math.floor(Math.random() * (JITTER_MS[1] - JITTER_MS[0]));

function decodeEntities(s) {
  return s
    .replace(/\\u0026/g, "&")
    .replace(/\\u003C/gi, "<")
    .replace(/\\u003E/gi, ">")
    .replace(/\\"/g, '"')
    .replace(/\\n/g, "\n")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&#x27;|&#39;/g, "'")
    .replace(/&quot;/g, '"')
    .replace(/&nbsp;/g, " ");
}

/** Robust fetch with retry/backoff; returns html text. */
async function fetchHtml(url) {
  for (let attempt = 1; attempt <= RETRIES; attempt++) {
    try {
      const res = await fetch(url, {
        headers: { "user-agent": UA, accept: "text/html" },
        redirect: "follow",
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return await res.text();
    } catch (err) {
      if (attempt === RETRIES) throw err;
      await sleep(800 * attempt * attempt);
    }
  }
}

// --------------------------------------------------------------- extraction

/** Grab an escaped-JSON string field (first match) from the RSC payload. */
function rscString(html, field, minLen = 0, maxLen = 600) {
  const re = new RegExp(`\\\\?"${field}\\\\?"\\s*:\\s*\\\\?"((?:[^"\\\\]|\\\\.){${minLen},${maxLen}})\\\\?"`);
  const m = html.match(re);
  return m ? decodeEntities(m[1]).trim() : null;
}

/**
 * The lesson's OWN description (not the site meta description). In the RSC
 * payload the lesson element serialises as
 *   ..."description":"<text>","intro":...
 * so anchor on the following "intro" key to skip the site-wide description
 * that appears earlier in the flight data.
 */
function rscLessonDescription(html) {
  const re = /\\\\?"description\\\\?"\s*:\s*\\\\?"((?:[^"\\\\]|\\\\.){15,400}?)\\\\?"\s*,\s*\\\\?"intro\\\\?"/g;
  const m = html.match(re);
  if (!m) return null;
  let t = decodeEntities(m[1]).trim();
  // the payload nests the lesson object one escape level deeper in places;
  // unwrap a serialized "description":"…","intro" if the capture contains it
  const inner = t.match(/\\?"description\\?"\s*:\s*\\?"((?:[^"\\]|\\.){10,400}?)\\?"\s*,\s*\\?"intro/);
  if (inner) t = decodeEntities(inner[1]).trim();
  return t;
}

/** All keyPoint texts in payload order. */
function rscKeyPoints(html) {
  const out = [];
  const re = /\\\\?"text\\\\?"\s*:\s*\\\\?"((?:[^"\\\\]|\\\\.){5,500}?)\\\\?"/g;
  for (const m of html.matchAll(re)) {
    const t = decodeEntities(m[1]).trim();
    if (t && !out.includes(t)) out.push(t);
  }
  return out;
}

/** type:"video" subelements: { id, caption } in payload order. */
function rscVideoSubelements(html) {
  const out = [];
  const re = /\\\\?"type\\\\?"\s*:\s*\\\\?"video\\\\?"[^}]{0,800}?\\\\?"source\\\\?"\s*:\s*\\\\?"https:\/\/www\.youtube\.com\/embed\/([\w-]{11})[^}]{0,800}/g;
  for (const m of html.matchAll(re)) {
    const block = m[0];
    const cap = block.match(/\\\\?"caption\\\\?"\s*:\s*\\\\?"((?:[^"\\\\]|\\\\.){0,300}?)\\\\?"/);
    const id = m[1];
    if (!out.some((v) => v.id === id)) {
      out.push({ id, caption: cap ? decodeEntities(cap[1]).trim() : null });
    }
  }
  return out;
}

/** The ":::intro … :::" markdown block. */
function rscIntro(html) {
  const m = html.match(/:::intro\\n([\s\S]{0,600}?)\\n:::/);
  return m ? decodeEntities(m[1]).trim() : null;
}

function extract(html) {
  return {
    description: rscLessonDescription(html),
    keyPoints: rscKeyPoints(html),
    keySummary: rscString(html, "keySummary", 15, 800),
    videoSubelements: rscVideoSubelements(html),
    intro: rscIntro(html),
  };
}

// --------------------------------------------------------------------- main

const inv = JSON.parse(readFileSync(join(VIDEOS, "inventory", "cognito-lessons.json"), "utf8"));
const shelf = inv.shelves[SHELF_ID];
if (!shelf) {
  console.error(`shelf ${SHELF_ID} not found in inventory`);
  process.exit(1);
}
const targets = shelf.lessons.filter(
  (r) => r.httpStatus === 200 && r.primaryVideoId
);
console.log(
  `enriching ${targets.length}/${shelf.lessons.length} lessons of ${SHELF_ID} (video-carrying set)`
);
mkdirSync(CACHE_DIR, { recursive: true });
mkdirSync(OUT_DIR, { recursive: true });

const rows = [];
let done = 0;
const queue = [...targets];

async function worker() {
  while (queue.length) {
    const lesson = queue.shift();
    const safeKey = lesson.key.replace(/[^A-Za-z0-9._-]/g, "_");
    const cachePath = join(CACHE_DIR, `${safeKey}.html`);
    let html;
    if (!REFETCH && existsSync(cachePath)) {
      html = readFileSync(cachePath, "utf8");
    } else {
      await sleep(jitter());
      html = await fetchHtml(lesson.url);
      writeFileSync(cachePath, html);
    }
    const ext = extract(html);
    rows.push({
      key: lesson.key,
      url: lesson.url,
      lessonRef: lesson.lessonRef,
      h1: lesson.h1,
      primaryVideoId: lesson.primaryVideoId,
      videoIds: lesson.videoIds,
      ...ext,
    });
    done++;
    if (done % 10 === 0 || done === targets.length) {
      console.log(`  ${done}/${targets.length}`);
    }
  }
}

await Promise.all(Array.from({ length: CONCURRENCY }, worker));

rows.sort((a, b) => a.url.localeCompare(b.url));
const out = {
  schema: "syllabai.lesson-enrichment/1",
  task: "T-VIDEOMAP-P2",
  course: COURSE,
  shelf: SHELF_ID,
  generatedUtc: new Date().toISOString(),
  method: "rsc-payload (same extractor family as P1 crawl; description/keyPoints/videoCaptions)",
  provenance: {
    inventory: "Videos/inventory/cognito-lessons.json",
    rawCache: "Videos/.cache/p2/ (gitignored)",
    userAgent: UA,
  },
  lessons: rows,
};
const outPath = join(OUT_DIR, "lesson-enrichment.json");
writeFileSync(outPath, JSON.stringify(out, null, 2) + "\n");

// honest run summary
const withDesc = rows.filter((r) => r.description).length;
const withKp = rows.filter((r) => r.keyPoints.length > 0).length;
const withCaps = rows.filter((r) => r.videoSubelements.some((v) => v.caption)).length;
console.log(`\nwrote ${outPath}`);
console.log(
  `fields populated: description ${withDesc}/${rows.length}, keyPoints ${withKp}/${rows.length}, captions ${withCaps}/${rows.length}`
);
