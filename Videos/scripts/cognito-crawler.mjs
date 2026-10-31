#!/usr/bin/env node
/**
 * cognito-crawler.mjs — F189 P1: discover + extract for the Cognito video map.
 *
 * Task T-VIDEOMAP-P1. Two-level, sitemap-driven, plain-HTTP (no headless
 * render needed — video data sits in each page's RSC payload; verified live
 * 2026-10-31):
 *
 *   Level 1 (subtopics): the sitemap's /coursesubtopic/<shelf>[-tiers]_<ref>
 *     pages (1,166 in-scope). These are landing/nav pages: they carry the
 *     course's lesson links (/courses/.../notes/<opaqueId>/<ref>-<slug>).
 *     GCSE shelves embed the full course nav (~86 links); A-level shelves
 *     carry the page's own lesson (canonical) + next-lesson link — the union
 *     across a shelf's subtopic pages reconstructs the full lesson list.
 *
 *   Level 2 (lessons): the union of /notes/ links per shelf, deduped by
 *     <opaqueId>/<slug>. Each lesson page carries the actual video payload:
 *     "subtopicVideoURL":"https://www.youtube.com/embed/<ID>" plus
 *     "type":"video","source":"https://www.youtube.com/embed/<ID>" body
 *     subelements. This is where F189's worked example (aGDFNZApXXI) lives.
 *
 * Etiquette: robots.txt for cognito.org/cognitoedu.org is `Allow: /`
 * (checked 2026-10-31); identifying UA; default concurrency 6 with jittered
 * delays; retry with backoff; raw HTML cached locally (Videos/.cache/,
 * gitignored) so re-runs re-extract without re-fetching.
 *
 * Scope: the 11 direct-match shelves (F189 §3). Every other shelf in the
 * sitemap is captured as census only (plan §3: "adding boards later is a
 * config change, not a redesign").
 *
 * Outputs (into Videos/inventory/ by default):
 *   cognito-lessons.json   — inventory (schema syllabai.video-inventory/1):
 *                            per shelf, subtopic rows + lesson rows (videos)
 *   cognito-lessons.csv    — flat lesson view (one row per lesson page)
 *   cognito-shelves.json   — every shelf in the sitemap (in-scope flag)
 *   run-stats.json         — fetch stats, failures, wall time
 *
 * Usage:
 *   node cognito-crawler.mjs                       # full run (both levels)
 *   node cognito-crawler.mjs --shelves b2-gcse-iedexcel --limit 6
 *   node cognito-crawler.mjs --no-fetch            # re-extract from cache only
 *   node cognito-crawler.mjs --level lessons       # skip level 1 fetches
 */
import { createHash } from "node:crypto";
import { mkdir, readFile, writeFile, stat } from "node:fs/promises";
import path from "node:path";

const VERSION = "1.1.0";
const SCHEMA = "syllabai.video-inventory/1";
const TASK_ID = "T-VIDEOMAP-P1";

const UA =
  "SyllabAI-VideoMap-P1/1.1 (+https://github.com/SyllabAI/syllabai-resources tree Videos/; " +
  "educational inventory crawl; robots-respecting; contact via repo issue)";

// F189 §3 — the 11 direct-match shelves and their expected subtopic counts.
const EXPECTED = {
  "b2-gcse-iedexcel": 86, // IGCSE Edexcel Biology   -> 4BI1
  "c2-gcse-iedexcel": 78, // IGCSE Edexcel Chemistry -> 4CH1
  "p2-gcse-iedexcel": 99, // IGCSE Edexcel Physics   -> 4PH1
  "m2-gcse-iedexcel": 142, // IGCSE Edexcel Maths     -> 4MA1
  "b2-gcse-cie": 85, // IGCSE CIE Biology        -> 0610
  "c2-gcse-cie": 77, // IGCSE CIE Chemistry      -> 0620
  "p2-gcse-cie": 92, // IGCSE CIE Physics        -> 0625
  "m2-gcse-cie": 145, // IGCSE CIE Maths          -> 0580
  "b3-alevel-cie": 139, // A-level CIE Biology      -> 9700
  "c3-alevel-cie": 130, // A-level CIE Chemistry    -> 9701
  "p3-alevel-cie": 93, // A-level CIE Physics      -> 9702
};
const EXPECTED_TOTAL = Object.values(EXPECTED).reduce((a, b) => a + b, 0);

const SHELF_LABEL = {
  "b2-gcse-iedexcel": "GCSE Biology (IGCSE Edexcel)",
  "c2-gcse-iedexcel": "GCSE Chemistry (IGCSE Edexcel)",
  "p2-gcse-iedexcel": "GCSE Physics (IGCSE Edexcel)",
  "m2-gcse-iedexcel": "GCSE Maths (IGCSE Edexcel)",
  "b2-gcse-cie": "GCSE Biology (IGCSE CIE)",
  "c2-gcse-cie": "GCSE Chemistry (IGCSE CIE)",
  "p2-gcse-cie": "GCSE Physics (IGCSE CIE)",
  "m2-gcse-cie": "GCSE Maths (IGCSE CIE)",
  "b3-alevel-cie": "A-Level Biology (CIE)",
  "c3-alevel-cie": "A-Level Chemistry (CIE)",
  "p3-alevel-cie": "A-Level Physics (CIE)",
};

const ROW_RE =
  /\/coursesubtopic\/(?<code>[bcpm]\d)-(?<level>ks3|gcse|alevel|ib|ap)-(?<board>[a-z0-9]+?)(?<tiers>(?:-[a-z0-9]{1,3})*?)_(?<ref>.+)$/;
const NOTES_LINK_RE =
  /(?:href="|\\?"url\\?":\\?"|https:\/\/cognito\.org)((?:https:\/\/cognito(?:edu)?\.org)?\/courses\/[a-z0-9-]+\/[a-z0-9-]+(?:\/[a-z0-9-]+)*\/notes\/[A-Za-z0-9]+\/[A-Za-z0-9._-]+)/g;

// ---------- CLI ----------
const argv = process.argv.slice(2);
function flag(name, def) {
  const i = argv.indexOf(`--${name}`);
  if (i === -1) return def;
  const v = argv[i + 1];
  return v && !v.startsWith("--") ? v : true;
}
const SITEMAP_URL = flag("sitemap", "https://cognitoedu.org/sitemap-subtopics.xml");
const HERE = path.dirname(new URL(import.meta.url).pathname);
const VIDEOS_DIR = path.resolve(HERE, "..");
const OUT_DIR = path.resolve(VIDEOS_DIR, flag("out", "inventory"));
const CACHE_DIR = path.resolve(VIDEOS_DIR, flag("cache", ".cache"));
const CONCURRENCY = Math.max(1, parseInt(flag("concurrency", "6"), 10));
const DELAY_MS = Math.max(0, parseInt(flag("delay-ms", "150"), 10));
const RETRIES = Math.max(0, parseInt(flag("retries", "3"), 10));
const LIMIT = flag("limit") ? parseInt(flag("limit"), 10) : null;
const SHELVES = flag("shelves")
  ? String(flag("shelves")).split(",").map((s) => s.trim()).filter(Boolean)
  : null;
const LEVEL = flag("level", "both"); // both | subtopics | lessons
const NO_FETCH = argv.includes("--no-fetch");
const REFRESH = argv.includes("--refresh");
const BASE_COMMIT = flag("base-commit", "") || "";
const VERBOSE = argv.includes("--verbose");

const inScope = (shelf) => (SHELVES ? SHELVES.includes(shelf) : shelf in EXPECTED);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const sha256 = (s) => createHash("sha256").update(s).digest("hex");
const log = (...a) => console.log(new Date().toISOString(), ...a);

function decodeEntities(s) {
  return s
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#0?39;/g, "'")
    .replace(/&apos;/g, "'")
    .replace(/&ndash;/g, "\u2013")
    .replace(/&mdash;/g, "\u2014")
    .replace(/&#x27;/g, "'")
    .replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(parseInt(d, 10)))
    .trim();
}
const stripTags = (s) => decodeEntities(s.replace(/<[^>]*>/g, " ").replace(/\s+/g, " ")).trim();

function cacheKey(url) {
  return url.replace(/^https?:\/\//, "").replace(/[^A-Za-z0-9._-]+/g, "_").slice(0, 190) + ".html";
}

async function fetchText(url) {
  let lastErr = null;
  for (let attempt = 0; attempt <= RETRIES; attempt++) {
    try {
      const ac = new AbortController();
      const t = setTimeout(() => ac.abort(), 30_000);
      const res = await fetch(url, {
        headers: { "user-agent": UA, accept: "*/*" },
        redirect: "follow",
        signal: ac.signal,
      });
      clearTimeout(t);
      const text = await res.text();
      return { status: res.status, text, finalUrl: res.url };
    } catch (e) {
      lastErr = e;
      if (attempt < RETRIES) await sleep(1000 * 2 ** attempt);
    }
  }
  throw lastErr ?? new Error("fetch failed");
}

// ---------- extraction ----------
function lessonKeyFromUrl(u) {
  const m = /\/notes\/([A-Za-z0-9]+)\/([A-Za-z0-9._-]+)\/?$/.exec(u);
  return m ? `${m[1]}/${m[2]}` : u;
}

function extractNotesLinks(html, baseUrl) {
  // unescape RSC-escaped slashes so payload URLs match markup URLs
  const hay = html.replace(/\\\//g, "/");
  const out = new Map(); // key -> absolute url
  for (const m of hay.matchAll(NOTES_LINK_RE)) {
    let u = m[1];
    if (u.startsWith("/")) u = `https://cognitoedu.org${u}`;
    u = u.replace(/^http:/, "https:").split("#")[0];
    out.set(lessonKeyFromUrl(u), u);
  }
  return [...out.entries()].map(([key, url]) => ({ key, url }));
}

function extractLessonRef(slug) {
  const m = /^(\d+(?:\.\d+)*)-/.exec(slug);
  return m ? m[1] : null;
}

// shelf guard: /courses/<level>/<subject>/<board>[/tier]/notes/...
function linkBelongsToShelf(url, shelfRow) {
  const m = /^https:\/\/cognito(?:edu)?\.org\/courses\/([^/]+)\//.exec(url);
  if (!m) return false;
  const level = m[1];
  const segs = url.split("/");
  return (
    level === shelfRow.level &&
    segs.includes(shelfRow.board)
  );
}

export function extractVideoPayload(html) {
  const title = stripTags((html.match(/<title[^>]*>([\s\S]*?)<\/title>/i)?.[1]) ?? "");
  const h1 = stripTags((html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i)?.[1]) ?? "");
  const ogTitle = decodeEntities(html.match(/property="og:title" content="([^"]*)"/)?.[1] ?? "");

  const videoIds = [];
  const embedRe = /youtube(?:-nocookie)?\.com\/(?:embed|v)\/([A-Za-z0-9_-]{11})/g;
  for (const m of html.matchAll(embedRe)) if (!videoIds.includes(m[1])) videoIds.push(m[1]);

  let primaryVideoId = null;
  const pm = html.match(/\\?"subtopicVideoURL\\?"\s*:\s*\\?"(https:[^"\\\s]+)\\?"/);
  if (pm) {
    const id = (pm[1].match(/embed\/([A-Za-z0-9_-]{11})/) || [])[1] ?? null;
    if (id) primaryVideoId = id;
  }

  let subelementVideoCount = 0;
  const subRe = /\\?"type\\?"\s*:\s*\\?"video\\?"/g;
  for (const m of html.matchAll(subRe)) {
    const ctx = html.slice(m.index, m.index + 600);
    if (/youtube(?:-nocookie)?\.com\/(?:embed|v)\/[A-Za-z0-9_-]{11}/.test(ctx)) subelementVideoCount++;
  }

  // NOTE: every lesson page carries the `.notes-paywalled` layout wrapper, so
  // its presence is NOT a gate signal. The honest signal is simply whether
  // Cognito served the video payload to the (logged-out) session — recorded
  // as videoId == null. Verified by render probes 2026-10-31: guest-gated
  // lessons expose no video even after hydration (A-level chem/phys: all;
  // most other shelves: a subset).

  return { title, h1, ogTitle, videoIds, primaryVideoId, subelementVideoCount };
}

// ---------- shared crawl runner ----------
async function crawlAll(items, { label, run, onDone }) {
  let idx = 0;
  let ok = 0, fail = 0, cacheHits = 0;
  const failures = [];

  async function worker() {
    while (true) {
      const i = idx++;
      if (i >= items.length) return;
      const item = items[i];
      const cpath = path.join(CACHE_DIR, cacheKey(item.url));
      let html = null, status = null, fetchedAt = null, error = null;
      const cStat = await stat(cpath).catch(() => null);
      if (!REFRESH && cStat) {
        html = await readFile(cpath, "utf8");
        status = 200;
        fetchedAt = cStat.mtime.toISOString();
        cacheHits++;
      } else if (!NO_FETCH) {
        try {
          const r = await fetchText(item.url);
          status = r.status;
          fetchedAt = new Date().toISOString();
          if (r.status === 200 && r.text.length > 1000) {
            html = r.text;
            await writeFile(cpath, html);
          } else {
            error = `HTTP ${r.status}`;
          }
        } catch (e) {
          error = String(e?.cause?.code || e?.message || e).slice(0, 120);
        }
      } else {
        error = "no-fetch mode and page not cached";
      }
      if (html) {
        item.httpStatus = status;
        item.fetchedAt = fetchedAt;
        item.error = null;
        ok++;
        run(item, html);
      } else {
        fail++;
        item.httpStatus = status;
        item.fetchedAt = fetchedAt ?? null;
        item.error = error ?? "unknown";
        failures.push({ url: item.url, status, error });
        if (VERBOSE) log(`  FAIL ${item.url} ${status ?? ""} ${error ?? ""}`);
      }
      if (VERBOSE || (i + 1) % 100 === 0 || i + 1 === items.length) {
        log(`${label} ${i + 1}/${items.length} (ok=${ok} fail=${fail} cached=${cacheHits})`);
      }
      onDone?.(item, html);
      await sleep(DELAY_MS * (0.5 + Math.random()));
    }
  }
  await Promise.all(Array.from({ length: CONCURRENCY }, () => worker()));
  return { ok, fail, cacheHits, failures };
}

// ---------- main ----------
async function main() {
  const started = new Date();
  await mkdir(OUT_DIR, { recursive: true });
  await mkdir(CACHE_DIR, { recursive: true });

  // -- stage A: sitemap -------------------------------------------------
  const smCache = path.join(CACHE_DIR, "sitemap-subtopics.xml");
  let sitemapXml, sitemapFetchedUtc, sitemapStatus;
  const smStat = await stat(smCache).catch(() => null);
  if (!REFRESH && smStat) {
    sitemapXml = await readFile(smCache, "utf8");
    sitemapFetchedUtc = smStat.mtime.toISOString();
    sitemapStatus = 200;
    log("sitemap: using cache");
  } else {
    log("sitemap: fetching", SITEMAP_URL);
    const r = await fetchText(SITEMAP_URL);
    sitemapStatus = r.status;
    sitemapFetchedUtc = new Date().toISOString();
    if (r.status !== 200) {
      console.error(`FATAL: sitemap fetch HTTP ${r.status}`);
      process.exit(2);
    }
    sitemapXml = r.text;
    await writeFile(smCache, sitemapXml);
  }
  const sitemapSha = sha256(sitemapXml);
  const locs = [...sitemapXml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
  log(`sitemap: ${locs.length} URLs, sha256 ${sitemapSha.slice(0, 12)}…`);

  // -- stage B: parse rows, shelf census ---------------------------------
  const subByShelf = new Map();
  const allShelves = new Map();
  let unparsed = 0;
  for (const url of locs) {
    const m = ROW_RE.exec(url);
    if (!m) {
      unparsed++;
      continue;
    }
    const shelf = `${m.groups.code}-${m.groups.level}-${m.groups.board}`;
    if (!allShelves.has(shelf)) allShelves.set(shelf, { shelf, urls: [] });
    allShelves.get(shelf).urls.push(url);
    if (!inScope(shelf)) continue;
    if (!subByShelf.has(shelf)) subByShelf.set(shelf, []);
    subByShelf.get(shelf).push({
      url,
      shelf,
      courseCode: m.groups.code,
      level: m.groups.level,
      board: m.groups.board,
      tierTokens: (m.groups.tiers || "").replace(/^-/, "").split("-").filter(Boolean),
      ref: m.groups.ref,
    });
  }
  log(
    `parsed ${locs.length - unparsed} subtopic rows over ${allShelves.size} shelves;`,
    `${unparsed} non-lesson URLs (courserevise etc.) captured as census only`
  );

  const scopeShelves = SHELVES ?? [...subByShelf.keys()];
  const subItems = scopeShelves.flatMap((s) => subByShelf.get(s) ?? []);
  const limited = LIMIT ? subItems.slice(0, LIMIT) : subItems;
  log(`in-scope: ${scopeShelves.length} shelves, ${limited.length} subtopic pages`);

  // -- stage C1: subtopic pages -> lesson links ---------------------------
  const lessonLinksByShelf = new Map(); // shelf -> Map(key -> url)
  const getLinks = (shelf) => {
    if (!lessonLinksByShelf.has(shelf)) lessonLinksByShelf.set(shelf, new Map());
    return lessonLinksByShelf.get(shelf);
  };

  const c1 = await crawlAll(limited, {
    label: "subtopics",
    run: (item, html) => {
      Object.assign(item, extractVideoPayload(html));
      const links = extractNotesLinks(html, item.url);
      const same = links.filter((l) => linkBelongsToShelf(l.url, item));
      item.lessonLinkCount = same.length;
      item.crossShelfLinkCount = links.length - same.length;
      // the page's own lesson: absolute cognito.org href or canonical tag
      const selfAbs = same.find((l) => l.url.startsWith("https://cognito.org/"));
      const canon =
        html.match(/<link[^>]+rel="canonical"[^>]+href="([^"]+)"/)?.[1] ??
        html.match(/href="([^"]+)"[^>]*rel="canonical"/)?.[1] ?? null;
      item.selfLessonUrl = canon
        ? canon.startsWith("http")
          ? canon
          : `https://cognitoedu.org${canon}`
        : selfAbs?.url ?? null;
      // union is always built (from cache when possible) so that
      // `--level lessons` re-runs can reconstruct the link set cheaply
      for (const l of same) getLinks(item.shelf).set(l.key, l.url);
    },
  });
  let lessonTotal = 0;
  for (const shelf of scopeShelves) {
    const n = getLinks(shelf).size;
    lessonTotal += n;
    log(`  shelf ${shelf}: ${n} unique lesson links from ${subByShelf.get(shelf)?.length ?? 0} subtopic pages`);
  }
  log(`level 1 done: ${lessonTotal} unique lesson URLs across ${scopeShelves.length} shelves`);

  // -- stage C2: lesson pages -> video payloads ---------------------------
  const lessonRows = new Map(); // key -> row
  if (LEVEL !== "subtopics") {
    const lessonItems = [];
    for (const shelf of scopeShelves) {
      for (const [key, url] of getLinks(shelf)) {
        const slug = url.split("/").pop();
        lessonItems.push({ url, key, shelf, slug, lessonRef: extractLessonRef(slug) });
      }
    }
    const limitedLessons = LIMIT ? lessonItems.slice(0, LIMIT) : lessonItems;
    log(`level 2: fetching ${limitedLessons.length} lesson pages`);
    await crawlAll(limitedLessons, {
      label: "lessons",
      run: (item, html) => {
        Object.assign(item, extractVideoPayload(html));
        item.method = "rsc-payload";
        lessonRows.set(item.key, { ...item });
      },
    });
  }

  // -- stage D: outputs ---------------------------------------------------
  const generatedUtc = new Date().toISOString();
  const shelvesOut = {};
  let subTotal = 0, lessonCountTotal = 0, videosTotal = 0, withPrimary = 0;
  for (const shelf of scopeShelves) {
    const subs = limited.filter((r) => r.shelf === shelf);
    const lessons = [...lessonRows.values()].filter((r) => r.shelf === shelf);
    const shelfVideos = lessons.reduce((a, r) => a + (r.videoIds?.length ?? 0), 0);
    subTotal += subs.length;
    lessonCountTotal += lessons.length;
    videosTotal += shelfVideos;
    withPrimary += lessons.filter((r) => r.primaryVideoId).length;
    shelvesOut[shelf] = {
      label: SHELF_LABEL[shelf] ?? shelf,
      expectedCount: EXPECTED[shelf] ?? null,
      subtopicCount: subs.length,
      lessonCount: lessons.length,
      discoveredLessonLinks: getLinks(shelf).size,
      videosTotal: shelfVideos,
      lessonsWithPrimaryVideo: lessons.filter((r) => r.primaryVideoId).length,
      subtopics: subs.map(({ url, ref, tierTokens, title, h1, httpStatus, fetchedAt, error, selfLessonUrl, lessonLinkCount, crossShelfLinkCount }) => ({
        url, ref, tierTokens, title, h1, selfLessonUrl, lessonLinkCount, crossShelfLinkCount, httpStatus, fetchedAt, error,
      })),
      lessons: lessons.map(({ url, key, slug, lessonRef, title, h1, ogTitle, primaryVideoId, videoIds, subelementVideoCount, httpStatus, fetchedAt, error }) => ({
        url, key, slug, lessonRef, title, h1, ogTitle, primaryVideoId, videoIds,
        videoCount: videoIds?.length ?? 0, subelementVideoCount,
        method: "rsc-payload", httpStatus, fetchedAt, error,
      })),
    };
  }

  const inventory = {
    schema: SCHEMA,
    task: TASK_ID,
    reviewState: "draft-p1", // raw crawl data only — NO alignment claims yet (AGENT.md law 2/3)
    generator: { name: "cognito-crawler.mjs", version: VERSION },
    provenance: {
      sitemapUrl: SITEMAP_URL,
      sitemapSha256: sitemapSha,
      sitemapUrlCount: locs.length,
      sitemapFetchedUtc,
      sitemapHttpStatus: sitemapStatus,
      baseCommit: BASE_COMMIT,
      method:
        "two-level plain-HTTP crawl: (1) sitemap-subtopics.xml -> 1,166 in-scope /coursesubtopic " +
        "pages -> union of /notes/ lesson links per shelf; (2) fetch each lesson page and extract " +
        "video IDs from its embedded RSC payload (subtopicVideoURL + type:video subelements). " +
        "No headless render required (verified 2026-10-31).",
      robots: "cognito.org/robots.txt and cognitoedu.org/robots.txt: User-Agent: * -> Allow: / (checked 2026-10-31)",
      userAgent: UA,
      concurrency: CONCURRENCY,
      delayMs: DELAY_MS,
    },
    scope: { shelves: scopeShelves, expectedCounts: EXPECTED, expectedTotal: EXPECTED_TOTAL },
    totals: {
      subtopicPages: subTotal,
      lessonPages: lessonCountTotal,
      fetchOkSubtopics: c1.ok,
      fetchFailedSubtopics: c1.fail,
      videosTotal,
      lessonsWithPrimaryVideo: withPrimary,
    },
    shelves: shelvesOut,
    generatedUtc,
  };
  await writeFile(path.join(OUT_DIR, "cognito-lessons.json"), JSON.stringify(inventory, null, 2) + "\n");

  // CSV (lesson level — the alignment input)
  const csv = [
    "shelf,lessonRef,slug,title,primaryVideoId,videoCount,videoIds,httpStatus,lessonUrl",
    ...scopeShelves.flatMap((s) =>
      shelvesOut[s].lessons.map((r) =>
        [
          s, r.lessonRef ?? "", r.slug,
          `"${(r.title || r.h1 || "").replace(/"/g, '""')}"`,
          r.primaryVideoId ?? "", r.videoCount, `"${(r.videoIds ?? []).join("|")}"`,
          r.httpStatus ?? "", r.url,
        ].join(",")
      )
    ),
  ].join("\n");
  await writeFile(path.join(OUT_DIR, "cognito-lessons.csv"), csv + "\n");

  // shelves census (every shelf in the sitemap)
  const shelvesCensus = {
    schema: "syllabai.video-shelf-census/1",
    task: TASK_ID,
    sitemapUrl: SITEMAP_URL,
    sitemapSha256: sitemapSha,
    note: "All shelves discovered in sitemap-subtopics.xml. inScope = the 11 direct-match shelves of F189 §3; the rest are captured so adding boards later is a config change (plan §3). Non-lesson URLs (courserevise etc.) are not listed.",
    totalSitemapUrls: locs.length,
    totalSubtopicRows: locs.length - unparsed,
    totalNonLessonUrls: unparsed,
    shelves: [...allShelves.values()].map(({ shelf, urls }) => ({
      shelf,
      subtopicCount: urls.length,
      expectedCount: EXPECTED[shelf] ?? null,
      inScope: inScope(shelf),
      discoveredLessonLinks: inScope(shelf) ? getLinks(shelf).size : null,
      sampleUrl: urls[0],
    })),
    generatedUtc,
  };
  await writeFile(path.join(OUT_DIR, "cognito-shelves.json"), JSON.stringify(shelvesCensus, null, 2) + "\n");

  const wallS = Math.round((Date.now() - started.getTime()) / 100) / 10;
  const runStats = {
    task: TASK_ID,
    generator: VERSION,
    startedUtc: started.toISOString(),
    generatedUtc,
    wallSeconds: wallS,
    sitemap: { url: SITEMAP_URL, sha256: sitemapSha, urls: locs.length, status: sitemapStatus },
    subtopics: { attempted: limited.length, ...c1, concurrency: CONCURRENCY, delayMs: DELAY_MS },
    lessons: { attempted: lessonRows.size, mode: LEVEL },
    baseCommit: BASE_COMMIT,
  };
  await writeFile(path.join(OUT_DIR, "run-stats.json"), JSON.stringify(runStats, null, 2) + "\n");

  log(`done in ${wallS}s: subtopics ok=${c1.ok} fail=${c1.fail}; lessons=${lessonCountTotal}; videosTotal=${videosTotal}`);
  if (c1.fail > 0) {
    log(`WARNING: ${c1.fail} subtopic pages failed — see ${path.join(OUT_DIR, "run-stats.json")}`);
    process.exitCode = 1;
  }
}

main().catch((e) => {
  console.error("FATAL:", e);
  process.exit(2);
});
