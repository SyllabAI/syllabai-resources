#!/usr/bin/env node
/**
 * validate-inventory.mjs — F189 P1 gate runner.
 *
 * Task T-VIDEOMAP-P1. Validates Videos/inventory/cognito-lessons.json against
 * the P1 exit gate ("inventory.json for all 11 shelves; schema check green",
 * plan §9) and the laws that matter downstream (AGENT.md: no manufactured
 * coverage, provenance preserved, draft-until-reviewed):
 *
 *   V1  header/provenance complete (schema, task, reviewState, sitemap sha256,
 *       timestamps, base commit, method, robots statement)
 *   V2  census: all 11 shelves present with EXACTLY the F189 §3 subtopic
 *       counts; total = 1,166; shelf census file parses to 3,871 lesson rows
 *   V3  row integrity: unique urls/keys; video ids match ^[\w-]{11}$;
 *       primaryVideoId ∈ videoIds; videoCount consistent; URLs are Cognito;
 *       every row carries httpStatus + fetchedAt + method
 *   V4  draft law: no alignment/mapping fields anywhere (raw crawl data only)
 *   V5  worked example: 1.1 Characteristics of Living Organisms → aGDFNZApXXI
 *   V6  spot-check (--live N): re-fetch N random video-bearing rows, re-extract,
 *       video ids must match (gate §8.5 analog)
 *
 * Usage: node validate-inventory.mjs [--live 5]
 * Exit 0 = all gates green; 1 = failures (printed).
 */
import { readFile } from "node:fs/promises";
import path from "node:path";

const HERE = path.dirname(new URL(import.meta.url).pathname);
const VIDEOS_DIR = path.resolve(HERE, "..");
const INV = path.resolve(VIDEOS_DIR, "inventory", "cognito-lessons.json");
const SHELVES = path.resolve(VIDEOS_DIR, "inventory", "cognito-shelves.json");
const STATS = path.resolve(VIDEOS_DIR, "inventory", "run-stats.json");

const argv = process.argv.slice(2);
const liveN = (() => {
  const i = argv.indexOf("--live");
  return i === -1 ? 0 : parseInt(argv[i + 1] ?? "5", 10) || 0;
})();

const EXPECTED = {
  "b2-gcse-iedexcel": 86, "c2-gcse-iedexcel": 78, "p2-gcse-iedexcel": 99,
  "m2-gcse-iedexcel": 142, "b2-gcse-cie": 85, "c2-gcse-cie": 77,
  "p2-gcse-cie": 92, "m2-gcse-cie": 145, "b3-alevel-cie": 139,
  "c3-alevel-cie": 130, "p3-alevel-cie": 93,
};
const EXPECTED_TOTAL = Object.values(EXPECTED).reduce((a, b) => a + b, 0);
const ID_RE = /^[A-Za-z0-9_-]{11}$/;
const ISO_RE = /^\d{4}-\d{2}-\d{2}T/;

const fails = [];
const pass = (m) => console.log(`  PASS  ${m}`);
const fail = (m) => { fails.push(m); console.log(`  FAIL  ${m}`); };
const warn = (m) => console.log(`  WARN  ${m}`);

const inv = JSON.parse(await readFile(INV, "utf8"));
const allRows = Object.values(inv.shelves).flatMap((s) => s.lessons);

console.log("== V1 header / provenance");
{
  const p = inv.provenance ?? {};
  const checks = [
    ["schema === syllabai.video-inventory/1", inv.schema === "syllabai.video-inventory/1"],
    ["task recorded", inv.task === "T-VIDEOMAP-P1"],
    ["reviewState draft (no shipping claims)", inv.reviewState === "draft-p1"],
    ["sitemap sha256 (64 hex)", typeof p.sitemapSha256 === "string" && /^[a-f0-9]{64}$/.test(p.sitemapSha256)],
    ["sitemap url", /^https:\/\/(www\.)?cognito(edu)?\.org\//.test(p.sitemapUrl ?? "")],
    ["sitemap fetchedAt ISO", ISO_RE.test(p.sitemapFetchedUtc ?? "")],
    ["base commit recorded", typeof p.baseCommit === "string" && p.baseCommit.length >= 7],
    ["method described", typeof p.method === "string" && p.method.length > 40],
    ["robots statement", typeof p.robots === "string" && p.robots.includes("Allow")],
    ["generatedUtc ISO", ISO_RE.test(inv.generatedUtc ?? "")],
  ];
  for (const [m, ok] of checks) ok ? pass(m) : fail(m);
}

console.log("== V2 census vs F189 §3");
{
  let total = 0;
  for (const [shelf, exp] of Object.entries(EXPECTED)) {
    const s = inv.shelves[shelf];
    if (!s) { fail(`shelf ${shelf} missing`); continue; }
    total += s.subtopicCount;
    s.subtopicCount === exp
      ? pass(`${shelf}: subtopics ${s.subtopicCount}/${exp}`)
      : fail(`${shelf}: subtopics ${s.subtopicCount} != expected ${exp}`);
  }
  total === EXPECTED_TOTAL
    ? pass(`subtopic total ${total}/${EXPECTED_TOTAL}`)
    : fail(`subtopic total ${total} != ${EXPECTED_TOTAL}`);

  const sh = JSON.parse(await readFile(SHELVES, "utf8"));
  sh.totalSubtopicRows === 3871
    ? pass(`shelf census: 3,871 lesson rows over ${sh.shelves.length} shelves`)
    : fail(`shelf census totalSubtopicRows ${sh.totalSubtopicRows} != 3871`);
}

console.log("== V3 row integrity");
{
  const urlSeen = new Map(), keySeen = new Map();
  let dupUrl = 0, dupKey = 0, badId = 0, badPrimary = 0, badCount = 0, badHost = 0, missingMeta = 0;
  const HOST = /^https:\/\/(www\.)?cognito(edu)?\.org\//;
  for (const [shelf, s] of Object.entries(inv.shelves)) {
    for (const r of s.lessons) {
      if (urlSeen.has(r.url)) dupUrl++; else urlSeen.set(r.url, shelf);
      const k = `${shelf}:${r.key}`;
      if (keySeen.has(k)) dupKey++; else keySeen.set(k, r.url);
      if (!HOST.test(r.url)) badHost++;
      for (const id of r.videoIds ?? []) if (!ID_RE.test(id)) badId++;
      if (r.primaryVideoId && !(r.videoIds ?? []).includes(r.primaryVideoId)) badPrimary++;
      if ((r.videoCount ?? 0) !== (r.videoIds ?? []).length) badCount++;
      if (!Number.isInteger(r.httpStatus) || !ISO_RE.test(r.fetchedAt ?? "") || !r.method) missingMeta++;
    }
  }
  dupUrl === 0 ? pass(`lesson urls unique (${urlSeen.size})`) : fail(`${dupUrl} duplicate lesson urls`);
  dupKey === 0 ? pass("lesson keys unique per shelf") : fail(`${dupKey} duplicate keys`);
  badHost === 0 ? pass("all lesson urls are cognito hosts") : fail(`${badHost} non-cognito urls`);
  badId === 0 ? pass("every video id matches ^[\\w-]{11}$") : fail(`${badId} malformed video ids`);
  badPrimary === 0 ? pass("primaryVideoId always member of videoIds") : fail(`${badPrimary} primaryVideoId not in videoIds`);
  badCount === 0 ? pass("videoCount == videoIds.length") : fail(`${badCount} videoCount mismatches`);
  missingMeta === 0 ? pass("every row has httpStatus + fetchedAt + method") : fail(`${missingMeta} rows missing provenance fields`);
}

console.log("== V4 draft law (no alignment claims)");
{
  const banned = ["spec", "specs", "spine", "mappings", "confidence", "reviewed", "specPoint", "specCode"];
  const hits = [];
  for (const [shelf, s] of Object.entries(inv.shelves)) {
    for (const r of s.lessons) for (const b of banned) if (b in r) hits.push(`${shelf}:${r.slug}:${b}`);
  }
  hits.length === 0
    ? pass("no spec-point/mapping fields on any row (raw inventory only)")
    : fail(`alignment fields present: ${hits.slice(0, 5).join(", ")}`);
}

console.log("== V5 worked example (F189 §2)");
{
  const row = inv.shelves["b2-gcse-iedexcel"].lessons.find((r) => r.slug === "1.1-characteristics-of-living-organisms");
  !row ? fail("worked-example lesson not found")
    : row.primaryVideoId === "aGDFNZApXXI"
      ? pass("1.1 Characteristics of Living Organisms → aGDFNZApXXI")
      : fail(`worked example got ${row.primaryVideoId}, expected aGDFNZApXXI`);
}

console.log("== V6 live spot-check");
if (liveN > 0) {
  const withVideo = allRows.filter((r) => r.primaryVideoId && r.method === "rsc-payload");
  const sample = [...withVideo].sort(() => Math.random() - 0.5).slice(0, liveN);
  let ok = 0;
  for (const r of sample) {
    try {
      const res = await fetch(r.url, { headers: { "user-agent": "SyllabAI-VideoMap-P1/1.1 (spot-check; robots-respecting)" } });
      const html = await res.text();
      const ids = [...new Set([...html.matchAll(/youtube(?:-nocookie)?\.com\/(?:embed|v)\/([A-Za-z0-9_-]{11})/g)].map((m) => m[1]))];
      const still = ids.includes(r.primaryVideoId);
      still ? pass(`spot-check ${r.slug} → ${r.primaryVideoId} still live`)
            : fail(`spot-check ${r.url}: recorded ${r.primaryVideoId}, live: [${ids.join(",") || "none"}]`);
      if (still) ok++;
    } catch (e) {
      fail(`spot-check ${r.url}: fetch error ${String(e).slice(0, 80)}`);
    }
    await new Promise((res) => setTimeout(res, 700));
  }
  console.log(`  (${ok}/${sample.length} spot-checks confirmed)`);
} else {
  warn("skipped (pass --live N to re-verify N random rows against production)");
}

console.log("== honest-gap summary");
{
  const gated = allRows.filter((r) => r.httpStatus === 200 && !r.primaryVideoId).length;
  const notFound = allRows.filter((r) => r.httpStatus !== 200).length;
  console.log(`  lessons: ${allRows.length} | with video: ${allRows.length - gated - notFound} | guest-gated (no video served to logged-out session): ${gated} | page not found: ${notFound}`);
  for (const [shelf, s] of Object.entries(inv.shelves)) {
    const g = s.lessons.filter((r) => r.httpStatus === 200 && !r.primaryVideoId).length;
    if (s.lessons.length && g === s.lessons.length) warn(`${shelf}: 0 guest-visible videos — whole shelf is guest-gated (P2 decision needed)`);
  }
}

console.log(fails.length === 0 ? "\nRESULT: ALL GATES GREEN" : `\nRESULT: ${fails.length} GATE FAILURES`);
process.exit(fails.length === 0 ? 0 : 1);
