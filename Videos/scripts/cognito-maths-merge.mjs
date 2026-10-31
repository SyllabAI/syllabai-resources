#!/usr/bin/env node
/**
 * cognito-maths-merge.mjs — F189 P1: fold maths render results into the inventory.
 *
 * Task T-VIDEOMAP-P1. cognito-crawler.mjs produces lesson rows for the nine
 * science shelves directly (RSC payload). The two maths shelves have no lesson
 * payload for guests — their videos were captured by cognito-maths-render.mjs
 * (headless render, Videos/.cache/maths-render.jsonl). This script converts
 * each render row into an inventory lesson row and replaces the (empty)
 * maths shelf lesson lists in Videos/inventory/cognito-lessons.json.
 *
 * Run AFTER cognito-crawler.mjs. Idempotent: re-running replaces maths rows
 * again from the same JSONL.
 */
import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const HERE = path.dirname(new URL(import.meta.url).pathname);
const VIDEOS_DIR = path.resolve(HERE, "..");
const INV = path.resolve(VIDEOS_DIR, "inventory", "cognito-lessons.json");
const JSONL = path.resolve(VIDEOS_DIR, ".cache", "maths-render.jsonl");

const lessonKey = (u) => {
  const m = /\/(?:notes|lessons)\/([A-Za-z0-9]+)\/([A-Za-z0-9._-]+)\/?$/.exec(u);
  return m ? `${m[1]}/${m[2]}` : u;
};
const lessonRef = (slug) => (/^(\d+(?:\.\d+)*)-/.exec(slug ?? "") ?? [])[1] ?? null;

const inv = JSON.parse(await readFile(INV, "utf8"));
const rows = (await readFile(JSONL, "utf8"))
  .split("\n")
  .filter((l) => l.trim())
  .map((l) => JSON.parse(l));

const byUrl = new Map(); // requestedUrl -> latest row (last wins)
for (const r of rows) byUrl.set(r.requestedUrl, r);

let merged = 0, missingShelf = 0;
for (const [requestedUrl, r] of byUrl) {
  const shelf = inv.shelves[r.shelf];
  if (!shelf) {
    missingShelf++;
    continue;
  }
  const is404 = r.error === "http-404-stale-sitemap";
  const lessonUrl = r.finalUrl || requestedUrl;
  const slug = lessonUrl.split("/").pop();
  const row = {
    url: lessonUrl,
    requestedUrl, // the /coursesubtopic page that anchors this lesson in the sitemap
    key: lessonKey(lessonUrl),
    slug,
    lessonRef: lessonRef(slug) ?? r.ref ?? null,
    title: r.title ?? null,
    h1: r.h1 ?? null,
    ogTitle: r.title ?? null,
    primaryVideoId: r.videoId ?? null,
    videoIds: r.videoId ? [r.videoId] : [],
    videoCount: r.videoId ? 1 : 0,
    subelementVideoCount: 0,
    method: "headless-render",
    renderAttempts: r.attempts ?? 1,
    noVideoLesson: Boolean(r.noVideoLesson) || undefined,
    httpStatus: is404 ? 404 : 200,
    fetchedAt: r.at,
    error: is404 ? "http-404-stale-sitemap (sitemap lists a page Cognito no longer serves)" : r.error ?? null,
  };
  const idx = shelf.lessons.findIndex((x) => x.requestedUrl === requestedUrl || x.url === requestedUrl);
  if (idx === -1) shelf.lessons.push(row);
  else shelf.lessons[idx] = row;
  merged++;
}

for (const shelfSlug of ["m2-gcse-cie", "m2-gcse-iedexcel"]) {
  const shelf = inv.shelves[shelfSlug];
  shelf.lessons.sort((a, b) => String(a.lessonRef).localeCompare(String(b.lessonRef), undefined, { numeric: true }));
  shelf.lessonCount = shelf.lessons.length;
  shelf.videosTotal = shelf.lessons.reduce((a, r) => a + r.videoCount, 0);
  shelf.lessonsWithPrimaryVideo = shelf.lessons.filter((r) => r.primaryVideoId).length;
}

inv.totals.lessonPages = Object.values(inv.shelves).reduce((a, s) => a + s.lessonCount, 0);
inv.totals.videosTotal = Object.values(inv.shelves).reduce((a, s) => a + s.videosTotal, 0);
inv.totals.lessonsWithPrimaryVideo = Object.values(inv.shelves).reduce(
  (a, s) => a + s.lessonsWithPrimaryVideo, 0);
inv.totals.guestGatedLessons = Object.values(inv.shelves).flatMap((s) => s.lessons)
  .filter((r) => r.httpStatus === 200 && !r.primaryVideoId).length;

// provenance note
inv.provenance.mathsMethod =
  "maths shelves (m2-gcse-cie, m2-gcse-iedexcel): headless render via agent-browser " +
  "(cognito-maths-render.mjs) — guest page loads lesson data via api-2.cognitoedu.org/graphql, " +
  "video read from the hydrated DOM iframe";

// regenerate the flat lesson CSV (post-merge, all 11 shelves)
const csv = [
  "shelf,lessonRef,slug,title,primaryVideoId,videoCount,videoIds,method,httpStatus,lessonUrl",
  ...Object.entries(inv.shelves).flatMap(([slug, sh]) =>
    sh.lessons.map((r) =>
      [
        slug, r.lessonRef ?? "", r.slug,
        `"${(r.title || r.h1 || "").replace(/"/g, '""')}"`,
        r.primaryVideoId ?? "", r.videoCount, `"${(r.videoIds ?? []).join("|")}"`,
        r.method ?? "", r.httpStatus ?? "", r.url,
      ].join(",")
    )
  ),
].join("\n");
await writeFile(path.resolve(VIDEOS_DIR, "inventory", "cognito-lessons.csv"), csv + "\n");
console.log("csv regenerated: cognito-lessons.csv");

await writeFile(INV, JSON.stringify(inv, null, 2) + "\n");
console.log(`merged ${merged} maths rows (missing shelf: ${missingShelf})`);
for (const s of ["m2-gcse-cie", "m2-gcse-iedexcel"]) {
  const sh = inv.shelves[s];
  console.log(`  ${s}: lessons=${sh.lessonCount} withVideo=${sh.lessonsWithPrimaryVideo}`);
}
console.log(`totals: lessonPages=${inv.totals.lessonPages} videosTotal=${inv.totals.videosTotal} guestGated=${inv.totals.guestGatedLessons}`);
