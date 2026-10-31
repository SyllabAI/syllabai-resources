#!/usr/bin/env node
/**
 * cognito-maths-render.mjs — F189 P1, maths-shelf extractor (headless render).
 *
 * Task T-VIDEOMAP-P1. The two maths shelves (m2-gcse-cie, m2-gcse-iedexcel)
 * serve lesson pages WITHOUT the RSC lesson payload the science shelves embed:
 * the lesson content (and its YouTube iframe) is fetched client-side via
 * api-2.cognitoedu.org/graphql. Rather than reverse-engineering that API, this
 * script renders each maths subtopic page in a real browser (agent-browser
 * CLI, the F189 plan's prescribed render tool) and reads the hydrated DOM:
 *
 *   video iframe  iframe[src*="youtube"]  ->  /embed/<ID>
 *   h1            document.querySelector('h1')
 *   canonical url location.href (the /lessons/<id>/<slug> redirect target)
 *
 * One page = one row. Rows append to Videos/.cache/maths-render.jsonl
 * (resume: already-present keys are skipped on re-run). The merge into
 * cognito-lessons.json happens in cognito-maths-merge.mjs.
 *
 * Etiquette: sequential, ~1 s gap, identifying UA via Cognito's own page
 * (no header override needed — agent-browser sends a normal browser UA);
 * robots.txt Allow: / (checked 2026-10-31).
 *
 * Usage:
 *   node cognito-maths-render.mjs                       # all maths pages
 *   node cognito-maths-render.mjs --limit 3             # smoke test
 *   node cognito-maths-render.mjs --shelves m2-gcse-cie # one shelf
 */
import { readFile, appendFile, stat } from "node:fs/promises";
import { spawnSync } from "node:child_process";
import path from "node:path";

const VERSION = "1.0.0";
const TASK_ID = "T-VIDEOMAP-P1";
const HERE = path.dirname(new URL(import.meta.url).pathname);
const VIDEOS_DIR = path.resolve(HERE, "..");
const CACHE_DIR = path.resolve(VIDEOS_DIR, ".cache");
const OUT_JSONL = path.join(CACHE_DIR, "maths-render.jsonl");

const argv = process.argv.slice(2);
function flag(name, def) {
  const i = argv.indexOf(`--${name}`);
  if (i === -1) return def;
  const v = argv[i + 1];
  return v && !v.startsWith("--") ? v : true;
}
const LIMIT = flag("limit") ? parseInt(flag("limit"), 10) : null;
const REVERSE = argv.includes("--reverse");
const SHELVES = flag("shelves")
  ? String(flag("shelves")).split(",").map((s) => s.trim())
  : ["m2-gcse-cie", "m2-gcse-iedexcel"];
const MAX_WAIT_MS = parseInt(flag("max-wait-ms", "25000"), 10);
const GAP_MS = parseInt(flag("gap-ms", "800"), 10);

const ROW_RE =
  /\/coursesubtopic\/(?<code>m2)-(?<level>gcse)-(?<board>[a-z0-9]+?)-(?<tier>h)_(?<ref>.+)$/;

const log = (...a) => console.log(new Date().toISOString(), ...a);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function ab(args, timeoutMs = 90_000) {
  const r = spawnSync("agent-browser", args, { encoding: "utf8", timeout: timeoutMs });
  if (r.status !== 0 && r.stderr && !/launched browser/.test(r.stderr)) {
    return { ok: false, err: (r.stderr || "").trim().slice(0, 200), out: r.stdout || "" };
  }
  return { ok: true, out: (r.stdout || "").trim(), err: (r.stderr || "").trim() };
}

async function main() {
  const started = Date.now();
  // -- build the target list from the cached sitemap ---------------------
  const smCache = path.join(CACHE_DIR, "sitemap-subtopics.xml");
  const xml = await readFile(smCache, "utf8");
  const targets = [];
  for (const m of xml.matchAll(/<loc>([^<]+)<\/loc>/g)) {
    const u = m[1];
    const p = ROW_RE.exec(u);
    if (!p) continue;
    const shelf = `${p.groups.code}-${p.groups.level}-${p.groups.board}`;
    if (!SHELVES.includes(shelf)) continue;
    targets.push({ url: u, shelf, ref: p.groups.ref });
  }
  const unique = [...new Map(targets.map((t) => [t.url, t])).values()];
  let todo = LIMIT ? unique.slice(0, LIMIT) : unique;
  if (REVERSE) todo = [...todo].reverse();
  log(`maths render: ${todo.length} pages across ${SHELVES.join(", ")}${REVERSE ? " (reversed)" : ""}`);

  // -- resume set ---------------------------------------------------------
  // Known-stale sitemap entries (HTTP 404 at stage 1, recorded in run-stats):
  // these pages do not exist and will never render a video.
  const KNOWN_404 = [
    "https://cognitoedu.org/coursesubtopic/m2-gcse-cie-h_2.55",
    "https://cognitoedu.org/coursesubtopic/m2-gcse-iedexcel-h_2.55",
    "https://cognitoedu.org/coursesubtopic/m2-gcse-iedexcel-h_2.61",
  ];
  const done = new Map();
  const attemptsBy = new Map();
  const jl = await stat(OUT_JSONL).catch(() => null);
  if (jl) {
    for (const line of (await readFile(OUT_JSONL, "utf8")).split("\n")) {
      if (!line.trim()) continue;
      try {
        const r = JSON.parse(line);
        done.set(r.requestedUrl, r);
        attemptsBy.set(r.requestedUrl, (attemptsBy.get(r.requestedUrl) ?? 0) + 1);
      } catch {}
    }
    log(`resume: ${done.size} rows already in ${OUT_JSONL}`);
  }
  for (const u of KNOWN_404) {
    if (!done.has(u)) {
      const shelf = u.includes("cie") ? "m2-gcse-cie" : "m2-gcse-iedexcel";
      const row = { requestedUrl: u, shelf, ref: u.split("_")[1], ok: false, videoId: null, h1: null, title: null, finalUrl: null, error: "http-404-stale-sitemap", method: "headless-render", scriptVersion: VERSION, task: TASK_ID, at: new Date().toISOString() };
      await appendFile(OUT_JSONL, JSON.stringify(row) + "\n");
      done.set(u, row);
      log(`marked stale-404: ${u}`);
    }
  }

  // -- ensure a session exists -------------------------------------------
  const sess = flag("session", "cognito-maths");
  const sargs = ["--session", sess];

  let n = 0;
  for (const t of todo) {
    n++;
    const prev = done.get(t.url);
    if (prev && (prev.ok || prev.noVideoLesson || prev.error === "http-404-stale-sitemap")) {
      if (n % 25 === 0) log(`skip ${n}/${todo.length} (terminal)`);
      continue;
    }
    const opened = ab([...sargs, "open", t.url, "--timeout", "45000"]);
    if (!opened.ok && !/✓/.test(opened.out)) {
      log(`  OPEN-FAIL ${t.url}: ${(opened.err || opened.out).slice(0, 120)}`);
      await appendFile(OUT_JSONL, JSON.stringify({ requestedUrl: t.url, shelf: t.shelf, ref: t.ref, ok: false, error: "open-failed", at: new Date().toISOString() }) + "\n");
      continue;
    }
    // poll for the youtube iframe up to MAX_WAIT_MS
    let videoId = null, h1 = null, finalUrl = null, title = null, waited = 0;
    const evalJs =
      'JSON.stringify({v:(document.querySelector(\'iframe[src*="youtube"]\')?.src.match(/embed\\/([\\w-]{11})/)||[])[1]||null,' +
      'h1:document.querySelector("h1")?.textContent||null,' +
      't:document.title,u:location.href})';
    while (waited < MAX_WAIT_MS) {
      await sleep(1200);
      waited += 1200;
      const ev = ab([...sargs, "eval", evalJs], 30_000);
      if (ev.ok && ev.out) {
        try {
          // raw form: stdout is a quoted JSON string -> "..." ; parse twice
          const inner = JSON.parse(ev.out); // -> '{"v":...}' string
          const obj = typeof inner === "string" ? JSON.parse(inner) : inner;
          videoId = obj.v || null; h1 = obj.h1 || null; finalUrl = obj.u || null; title = obj.t || null;
          if (!videoId && !h1 && (!finalUrl || finalUrl === "about:blank")) {
            // daemon idle-exit relaunch: re-open the page and keep polling
            ab([...sargs, "open", t.url, "--timeout", "45000"]);
          }
          if (videoId) break;
        } catch {}
      }
    }
    const row = {
      requestedUrl: t.url, shelf: t.shelf, ref: t.ref,
      ok: Boolean(videoId), videoId, h1, title, finalUrl,
      // terminal video-less verdict only after 2 full attempts with h1 visible
      attempts: (attemptsBy.get(t.url) ?? 0) + 1,
      noVideoLesson: !videoId && Boolean(h1) && (attemptsBy.get(t.url) ?? 0) >= 1,
      waitedMs: waited, method: "headless-render", tool: `agent-browser/cli`, scriptVersion: VERSION,
      task: TASK_ID, at: new Date().toISOString(),
    };
    await appendFile(OUT_JSONL, JSON.stringify(row) + "\n");
    done.set(t.url, row);
    log(`  [${n}/${todo.length}] ${t.shelf} ${t.ref} -> ${videoId ?? "NO-VIDEO"} (${Math.round(waited / 1000)}s)${videoId ? "" : "  " + t.url}`);
    await sleep(GAP_MS);
  }

  const rows = [...done.values()];
  log(`done in ${Math.round((Date.now() - started) / 1000)}s: total=${rows.length} ok=${rows.filter((r) => r.ok).length} noVideo=${rows.filter((r) => r.requestedUrl && !r.ok).length}`);
  log(`rows in ${OUT_JSONL}`);
  ab(["close"], 15_000);
}

main().catch((e) => {
  console.error("FATAL:", e);
  process.exit(2);
});
