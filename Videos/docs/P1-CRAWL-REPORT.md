# P1 crawl report — Cognito video-map inventory

**Task:** T-VIDEOMAP-P1 · **Date:** 2026-10-31 · **Base commit:** `652ca2d4e7709647cfd68040a56d817ae985fc5e`
**Deliverable:** `Videos/inventory/cognito-lessons.json` (schema `syllabai.video-inventory/1`, `reviewState: draft-p1`)
**Gate result:** `validate-inventory.mjs --live 5` → **ALL GATES GREEN** (34 checks, 5/5 live spot-checks)

---

## 1. What was built

Four scripts under `Videos/scripts/` (zero-dependency Node ≥ 18):

| Script | Role |
| --- | --- |
| `cognito-crawler.mjs` (v1.1.0) | Sitemap-driven, two-level crawl: (1) all in-scope `/coursesubtopic/` pages, (2) the union of their `/notes/` lesson links → fetch each lesson and extract video IDs from the page's embedded RSC payload. |
| `cognito-maths-render.mjs` (v1.0.0) | The two maths shelves serve no lesson payload to guests; this renders each maths page with `agent-browser` and reads the hydrated YouTube iframe. Resumable via `Videos/.cache/maths-render.jsonl`. |
| `cognito-maths-merge.mjs` | Converts render rows into inventory lesson rows, updates totals, regenerates the CSV. |
| `validate-inventory.mjs` | P1 gates V1–V6 (below), optional `--live N` spot-check re-fetching random rows against production. |

Etiquette (verified at run start): `cognito.org/robots.txt` and
`cognitoedu.org/robots.txt` are `User-Agent: * → Allow: /`; identifying
User-Agent (`SyllabAI-VideoMap-P1/1.1 …`); concurrency 6 with jittered delays;
retries with exponential backoff; raw HTML cached so re-runs never re-fetch.

## 2. Run narrative (all times UTC, 2026-10-31)

1. **Sitemap** — `https://cognitoedu.org/sitemap-subtopics.xml`, 12,049 URLs,
   sha256 `a9be85d9c0eaf5fc0de13459d69148327a86b4b47231538b4f2cced6e8db1c15`.
   Parses into **3,871 lesson rows over 39 shelves** + 8,178 `/courserevise/`
   flashcard URLs (captured as census only). All 11 direct-match shelves match
   the F189 §3 census exactly (86/78/99/142/85/77/92/145/139/130/93 = 1,166).
2. **Subtopic crawl** — 1,166 pages fetched in ~212 s (concurrency 6).
   **1,162 OK; 4 honest 404s** — stale sitemap entries Cognito no longer serves:
   `b3-alevel-cie_HsWgmekM`, `m2-gcse-cie-h_2.55`, `m2-gcse-iedexcel-h_2.55`,
   `m2-gcse-iedexcel-h_2.61`.
3. **Lesson discovery** — subtopic pages carry the course lesson nav
   (`/notes/<opaqueId>/<ref>-<slug>` links; maths uses `/lessons/…`).
   A shelf-guard (level + board path segments) prevents any cross-course leak;
   cross-shelf links were counted and excluded. Union: **1,004 science lesson URLs**.
4. **Lesson crawl (sciences)** — 1,004 fetched in ~148 s, 1,003 OK, deduped to
   **988 unique science lessons** (some shelves' navs repeat lessons across
   tier variants; dedupe key = opaqueId + slug).
5. **Maths render** — 287 subtopic pages across `m2-gcse-cie` / `m2-gcse-iedexcel`,
   rendered sequentially in `agent-browser` (~30 min wall across resume passes):
   **234 with video**, **50 video-less after ≥ 2 full attempts** (h1 rendered,
   no iframe ever mounted), 3 stale-404s marked terminal.
6. **Merge + validate** — maths rows folded in, CSV regenerated, gates run.

## 3. Method corrections vs F189 §2 (amendment evidence)

F189 recorded "pages are client-rendered (no video data in raw HTML)" and
prescribed headless render for everything. Live re-verification changed the
picture, and the plan doc carries the amendment (§12):

1. **Science shelves DO embed the lesson payload in raw HTML** — the RSC
   flight data contains `"subtopicVideoURL":"https://www.youtube.com/embed/<ID>"`
   plus `"type":"video","source":"…/embed/<ID>"` body subelements. Plain HTTP
   suffices (faster, politer, more robust than rendering).
2. **Maths shelves genuinely have no payload for guests** — their lesson data
   arrives via `POST api-2.cognitoedu.org/graphql`; the video iframe only
   exists in the hydrated DOM → headless render (the plan's original method,
   used exactly there).
3. **The sitemap's `/coursesubtopic/` pages are not lesson pages** — they are
   subtopic landing/nav pages; videos live on `/notes/` (sciences) or
   `/lessons/` (maths) pages that those pages link to. F189's URL grammar
   (Appendix A) is otherwise accurate.

## 4. Findings that change P2 planning

### 4.1 Guest-gating is the dominant gap (542 of 1,275 lessons)

Cognito serves the video payload **only for some lessons when logged out**.
Render-probe verification (guest session, page fully hydrated):

- `b2-gcse-cie` 1.5 Dichotomous Keys: paywall + login wall, **no iframe** —
  gated even after render.
- `c3-alevel-cie` 1.1 The Structure of an Atom: **no video element at all**
  after render.
- Maths `m2-gcse-cie-h_5.24`: iframe **does** mount for guests (took > 25 s in
  some passes — early "no-video" readings were retry artifacts, since fixed by
  attempt-counting in the render script).

Per-shelf guest-visible video coverage:

| Shelf | Lessons | With video (guest) | Guest-gated |
| --- | --- | --- | --- |
| b2-gcse-iedexcel (4BI1) | 109 | 75 | 34 |
| c2-gcse-iedexcel (4CH1) | 93 | 64 | 29 |
| p2-gcse-iedexcel (4PH1) | 113 | 82 | 31 |
| m2-gcse-iedexcel (4MA1) | 142 | 117 | 25 |
| b2-gcse-cie (0610) | 107 | 75 | 32 |
| c2-gcse-cie (0620) | 80 | 55 | 25 |
| p2-gcse-cie (0625) | 121 | 83 | 38 |
| m2-gcse-cie (0580) | 145 | 117 | 28 |
| b3-alevel-cie (9700) | 142 | 62 | 80 |
| **c3-alevel-cie (9701)** | 130 | **0** | **130** |
| **p3-alevel-cie (9702)** | 93 | **0** | **93** |
| **Total** | **1,275** | **730** | **542** |

(videosTotal = 740: 10 lessons embed a second video as a body subelement.)

**Decision needed before P4 (and before P2 maths/A-level alignment):** accept
partial guest-visible coverage, or crawl with a Cognito account (changes the
etiquette posture — needs owner sign-off), or ask Cognito (the plan's §7
courtesy note becomes a requirements conversation). The honest-empty-state law
means a gated lesson is simply a lesson without a video row today; nothing is
invented to fill it.

### 4.2 Lesson counts ≠ subtopic counts (sciences)

The sciences' course navs list more lessons than there are subtopic pages
(e.g. 4BI1: 109 lessons / 86 subtopic pages). Cognito's lesson numbering
(`topic.lesson`) is not the spec-section numbering the sitemap encodes
(`t_1.01`…). **Alignment (P2 Step 3) must bind on the lesson's own `lessonRef`
and title against the spine — not on the subtopic ref.**

### 4.3 `.notes-paywalled` is layout, not a gate signal

Every lesson page carries the `.notes-paywalled` wrapper and
`isAccessibleForFree:false` JSON-LD — including the lessons that DO serve their
video. The only honest signal is whether the payload contains a video.

## 5. Gates (this phase)

| Gate | Check | Result |
| --- | --- | --- |
| V1 | Header/provenance complete (schema, task, sitemap sha256, base commit, method, robots) | ✅ |
| V2 | Census: 11/11 shelves exactly at F189 §3 counts; 1,166/1,166; census file = 3,871 rows / 39 shelves | ✅ |
| V3 | Row integrity: unique urls+keys, `^[\w-]{11}$` ids, primary ∈ videoIds, counts consistent, Cognito hosts only, per-row provenance | ✅ |
| V4 | Draft law: zero alignment/mapping fields on any row (AGENT.md laws 2–3) | ✅ |
| V5 | Worked example: `1.1-characteristics-of-living-organisms` → `aGDFNZApXXI` (F189 §2) | ✅ |
| V6 | Live spot-check: 5 random video rows re-fetched, ids still live (5/5: `mrDxJon0MBE`, `uYubwlPRdCs`, `eSGRpPcJGlA`, `Tn0_L-8amjM`, `0O3NdG0uWM4`) | ✅ |

## 6. Artifacts

- `Videos/inventory/cognito-lessons.json` — 1.6 MB, schema
  `syllabai.video-inventory/1`, `reviewState: draft-p1`, per-shelf subtopic +
  lesson rows with full provenance.
- `Videos/inventory/cognito-lessons.csv` — 1,275 lesson rows, flat.
- `Videos/inventory/cognito-shelves.json` — 39-shelf census (out-of-scope
  boards captured per plan §3).
- `Videos/inventory/run-stats.json` — last run's fetch stats + the 4 stale-404
  rows.
- `Videos/.cache/` — 438 MB raw HTML + render JSONL (gitignored, resumable,
  never committed).
