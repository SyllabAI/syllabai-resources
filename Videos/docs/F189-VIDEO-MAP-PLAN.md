# F189 — Video Map: specification points → videos (Cognito pilot)

**Status:** DRAFT v0.1 — 2026-10-31 · living plan, expected to be amended as
phases land (amendments append-only, like the registry audit ruling).
**Owner:** SyllabAI
**Related:** ADR-029 (committed, immutable content posture) · T-SENECA-001
(`lib/seneca-hub.ts` — the third-party-provider precedent this follows) ·
`apps/hub/spines/*` (the spec-point spine the map binds to) ·
`apps/hub/content-maps/*` (the reconciliation-report format the map's coverage
block imitates) · F184 decay/strengths (future consumer).

---

## 1. Why — the map is the product

The goal of this feature is **not** a videos page. The goal is a
**first-class dataset**: every specification point of every SyllabAI course,
bound to the best free teaching videos for it, starting with Cognito. Once
the map exists and is trustworthy, a family of future features consumes it
(§10): spec-point coverage percentages, "watch next" recommendations driven by
the F184 decay/strengths model, question→video links after a wrong answer,
revision plans with video steps. Getting the **data model and the review
workflow right** matters more than getting any single UI surface shipped
fast.

**Decisions locked for v0.1** (owner, 2026-10-31):

| Decision | Choice |
| --- | --- |
| Pilot source | Cognito (cognito.org), all shelves that overlap SyllabAI courses |
| Binding granularity | **Lesson→spec-point(s), many-to-many** (one lesson may cite 1..N spec points; a spec point may list 0..N lessons) |
| Storage | **`apps/hub/content/video-map/<slug>.json`** per course, loaded like the Seneca registry (static, committed, no DB) |
| Student surface | **Dedicated Videos lane**: tile on the course page + `/courses/<slug>/videos` subpage |
| Curation | **Draft + review**: crawler/LLM drafts with confidence scores; only reviewed mappings ship |
| Scope | All direct-match Cognito shelves (sciences + maths, IGCSE + A-level), 1,166 lesson pages (§3) |

---

## 2. What the feasibility probe proved (2026-10-31)

Everything below was verified live today against production Cognito and live
`main` of this repo. No guessing.

**Cognito (cognito.org — `cognitoedu.org` redirects there):**

- `sitemap.xml` → `sitemap-subtopics.xml` enumerates **12,049 lesson pages**;
  each URL encodes `course-level-board` and (at GCSE) the **spec ref**:
  `/coursesubtopic/b2-gcse-iedexcel-t_1.01`. The sitemap is a complete crawl
  index — no scraping of course pages needed for discovery.
- Course URL grammar: `/courses/<level>/<subject>/<board>` (e.g.
  `/courses/gcse/biology-triple/iedexcel`); lesson URLs:
  `/courses/gcse/biology-triple/iedexcel/notes/TGVNQ3NhbnA/1.1-characteristics-of-living-organisms`
  — the **lesson slug carries the spec ref** (`1.1-…`).
- Pages are client-rendered (no video data in raw HTML), but a headless
  render of the lesson page exposes everything needed. **Worked example**
  (`…iedexcel/notes/TGVNQ3NhbnA/1.1-characteristics-of-living-organisms`,
  fetched with a headless browser today):
  - H1: `1.1 - Characteristics of Living Organisms`
  - player: `https://www.youtube-nocookie.com/embed/aGDFNZApXXI` →
    **video ID `aGDFNZApXXI`**
  - the course page names the syllabus outright (25× `4BI1` on the IGCSE
    Edexcel Biology course page).
- A-level lesson URLs don't carry spec refs (random suffixes); alignment
  there relies on on-page spec references + lesson titles + spine matching
  (§5, Step 3).

**SyllabAI (live `main`):**

- `apps/hub/spines/<slug>.json` — per-course curriculum DAG:
  `curriculum.nodes[]` with `family: TOPIC | SUBTOPIC | SPEC_POINT`, where a
  spec point is `{code: "1.1.1", title: "understand that…", parents:
  ["<subtopicNode>", …], scope: "AS Level", order}`. Spec-point `code` is the
  map's join key (course-scoped, so no cross-course ambiguity).
- `apps/hub/content-maps/<slug>.json` — the existing reconciliation-report
  format (inputs with sha256, coverage block, unmapped lists): the video-map's
  coverage/reporting block imitates this so the two read the same way.
- `apps/hub/content/flags.json` + `lib/seneca-hub.ts` — the gating law to
  copy: flag file/key/slug **ABSENT = OFF**, honest empty states, one-flip
  kill, zod-validated static JSON via `loadContentJson`, server-only.
- `[course]/` route slots live beside `seneca/`, `specification/`,
  `strengths/` → a new `videos/` subpage slot follows the house pattern.

---

## 3. Source landscape — Cognito shelves × SyllabAI registry

Cognito's subtopic sitemap parses into exactly 3,871 lesson pages over 10
courses × boards. The **direct-match** subset (same board as a SyllabAI
lane):

| Cognito shelf | Lesson pages | SyllabAI lanes (registry slug → syllabus) | Alignment |
| --- | --- | --- | --- |
| `b2-gcse-iedexcel` Biology | 86 | `igcse-biology-19` → **4BI1** (+ modular 4XBI1 units, double-award 4SD0 biology) | **Direct** — page carries the 4BI1 spec refs |
| `c2-gcse-iedexcel` Chemistry | 78 | `igcse-chemistry-19` → **4CH1** (+ modular, double-award chemistry) | **Direct** |
| `p2-gcse-iedexcel` Physics | 99 | `igcse-physics-19` → **4PH1** (+ modular, double-award physics) | **Direct** |
| `b2-gcse-cie` Biology | 85 | `cie-igcse-biology-23` → **0610** (+ combined 0653 / co-ordinated 0973 biology lanes) | **Direct** |
| `c2-gcse-cie` Chemistry | 77 | `cie-igcse-chemistry-23` → **0620** (+ combined lanes) | **Direct** |
| `p2-gcse-cie` Physics | 92 | `cie-igcse-physics-23` → **0625** (+ combined lanes) | **Direct** |
| `b3-alevel-cie` Biology | 139 | `cie-as-biology-25`, `cie-a-level-biology-25` → **9700** | **Direct** (CIE A-level shelf) |
| `c3-alevel-cie` Chemistry | 130 | `cie-as-chemistry-25`, `cie-a-level-chemistry-25` → **9701** | **Direct** |
| `p3-alevel-cie` Physics | 93 | `cie-as-physics-25`, `cie-a-level-physics-25` → **9702** | **Direct** |
| `m2-gcse-cie` Maths | 145 | `cie-igcse-maths-25-core/-extended` → **0580**; `…maths-international-maths-23-*` → 0607 | **Direct-ish** — verify 0607 vs 0580 ref overlap in draft |
| `m2-gcse-iedexcel` Maths | 142 | `igcse-maths-a-18-foundation/-higher` → **4MA1** (+ modular units; 4MB1 separate) | **Direct-ish** — tier split maps to foundation/higher |
| **Total direct** | **1,166** | | |

**Deliberately out of v0.1 (honest gaps, revisit later):**

- **Edexcel IAL** (`ial-biology-18` YBI11, `ial-chemistry-17` YCH11,
  `ial-physics-19` YPH11): Cognito's A-level shelf is **AQA / CIE / OCR
  only** — no Edexcel International A-level. Candidate: topical re-use of the
  `alevel-cie` shelves (CIE ≈ IAL in coverage, different spec numbering).
  Phase-2 decision, flagged per-video as `boardMismatch: true` if shipped.
- **A-level Maths / Further Maths** (YMA01, YFM01, 4PM1, 0606): no Cognito
  shelf at all (`m3` doesn't exist in the sitemap). Needs a second source
  later; out of scope.
- Other Cognito shelves (AQA/OCR GCSE+A-level, SQA, KS3, IB, AP): no
  SyllabAI lanes yet. The crawler should still capture the sitemap rows so
  adding boards later is a config change, not a redesign.

---

## 4. Data model

### 4.1 File layout

```
apps/hub/content/video-map/
  <slug>.json              one file per SyllabAI course with mappings
  registry.json            slug → {videos: n, mapped: n, shelf, updatedUtc}  (loader index)
apps/hub/content/flags.json            + "videoMap" flag key (kill-switch)
apps/hub/src/lib/video-map.ts          loader (zod, server-only, React cache)
apps/hub/src/app/courses/[course]/videos/page.tsx   the lane
```

One file per course (not per shelf) because the hub's unit of serving is the
course; two registry lanes can share one Cognito shelf (e.g. 4BI1 triple and
4SD0 double-award biology cite the same `b2-gcse-iedexcel` shelf).

### 4.2 Schema `hub.video-map/1`

```jsonc
{
  "schema": "hub.video-map/1",
  "course": "igcse-biology-19",
  "qual": "IGCSE",
  "source": {
    "provider": "cognito",
    "shelf": "b2-gcse-iedexcel",
    "label": "GCSE Biology (IGCSE Edexcel)",
    "courseUrl": "https://cognito.org/courses/gcse/biology-triple/iedexcel",
    "crawledUtc": "2026-11-02T…Z",
    "crawlMethod": "sitemap+headless-render"
  },
  "videos": [
    {
      "id": "aGDFNZApXXI",
      "title": "1.1 - Characteristics of Living Organisms",
      "lessonRef": "1.1",
      "lessonUrl": "https://cognito.org/courses/…/notes/TGVNQ3NhbnA/1.1-…",
      "topicPath": ["The Nature & Variety of Organisms"],
      "durationS": null
    }
  ],
  "mappings": [
    {
      "video": "aGDFNZApXXI",
      "specs": ["1.1.1", "1.1.2"],
      "confidence": "high",
      "evidence": "lesson ref 1.1 == spec section 1.1; title match",
      "reviewed": true,
      "reviewer": "…", "reviewedUtc": "…",
      "boardMismatch": false
    }
  ],
  "coverage": {
    "specPointsTotal": 165, "specPointsMapped": 142,
    "videosTotal": 86, "videosMapped": 84, "videosUnmapped": 2
  },
  "inputs": {
    "spine": {"file": "apps/hub/spines/igcse-biology-19.json", "sha256": "…"},
    "sitemap": {"url": "https://cognito.org/sitemap-subtopics.xml", "sha256": "…"}
  },
  "generatedUtc": "…"
}
```

Field notes:

- `id` — YouTube video id, `^[\w-]{11}$` (validated).
- `lessonRef` — `null` for A-level pages (URLs carry opaque ids there).
- `durationS` — filled from YouTube oEmbed at crawl time if available;
  `null` is honest when unknown.
- `specs` — spine `SPEC_POINT` codes, course-scoped (must exist in that
  course's spine — validation gate, §8).

Rules:

- **`reviewed: false` never renders.** The draft pipeline writes drafts into
  `scripts/video-map/drafts/` (not into `content/`); only reviewed mappings
  enter a committed `content/video-map/<slug>.json`.
- Many-to-many by design (locked decision): one lesson → 1..N spec points;
  a spec point accumulates 0..N lessons. A spec point with zero videos is a
  normal, honest state; the lane shows what exists and says nothing about
  the rest.
- Amendments to mappings are append-with-reason, not silent overwrites —
  same spirit as the registry audit ruling.

---

## 5. Draft pipeline (crawl → extract → align → review → commit)

All crawler code lives under `scripts/video-map/` (build-time tooling, never
shipped to the hub runtime). The repo already has Playwright configured
(`apps/hub/playwright.config.ts`); the crawler uses Playwright (or the
`agent-browser` CLI) for the render step — no new infra.

**Step 1 — Discover.** Fetch `sitemap-subtopics.xml`, parse the URL grammar,
keep shelves in scope (§3). Output: `inventory.json` (1,166 rows today).

**Step 2 — Extract.** For each lesson URL, headless-render (rate-limited,
~1 req / 2 s, identifying UA, robots.txt re-checked at run start), then
collect: YouTube video ID from the `youtube-nocookie.com/embed/` iframe,
H1 title, lesson ref (slug prefix), topic breadcrumb. Idempotent: a local
cache keyed by URL + date prevents re-crawling unchanged pages; a re-crawl
only diffs.

**Step 3 — Align (the draft).** Two passes, cheapest first:
1. **Deterministic pre-pass** — lesson ref (e.g. `1.1`) / title-prefix match
   against spine SUBTOPIC and SPEC_POINT codes; board-spec sections carried
   on the page (the 4BI1 case). Expected to resolve the majority of GCSE
   rows with `confidence: high`.
2. **LLM draft pass** — for the remainder (all A-level rows at minimum):
   prompt with the lesson title + topic path + spine spec-point titles, ask
   for 1..N spec-point codes + a confidence + a one-line evidence string.
   Anything below threshold lands `confidence: low` and **must** be
   human-reviewed.

**Step 4 — Review.** The draft emits, per course: a review file (all
mappings sorted by confidence, low-confidence first, each with evidence and
a deep link to the Cognito lesson) and a coverage report in the
content-maps `_report` style. The owner reviews low/medium rows in batch;
reviewed rows flip `reviewed: true`. This step is the product's quality law:
**no unreviewed mapping ever ships.**

**Step 5 — Commit.** Batched house-style patches (one patch per course file
+ registry/flags as separate patches; assertion-checked, `--check` dry-run,
byte-compare, CI green) — the same flow as batches 0003–0017. Patches stay
reviewable because each `video-map/<slug>.json` is a pure data file.

---

## 6. Hub runtime — the Videos lane

- **`lib/video-map.ts`** mirrors `lib/seneca-hub.ts`: server-only, zod,
  `loadContentJson`, React `cache`, `getVideoMapForCourse(slug)`. Gating law
  identical: flag key `videoMap` in `content/flags.json`; flag/key/slug
  ABSENT = OFF → `null`; every surface renders its honest empty state.
  Registry missing = feature absent for that deployment. One-flip kill per
  course (remove the slug) or globally (remove the key).
- **Course page:** the resource tiles grow a **Videos tile** (count =
  `videosTotal`, exactly like the other tiles' count honesty rules — no
  fabricated numbers; the tile is absent when the course has no reviewed
  mappings).
- **`/courses/<slug>/videos`** subpage: videos grouped by `topicPath`
  (Cognito's topic structure), each row = thumbnail
  (`https://i.ytimg.com/vi/<id>/mqdefault.jpg`) + title + lesson ref +
  spec-point chips it covers + **click-to-load** privacy-enhanced embed
  (`youtube-nocookie`) + "Watch on YouTube" link + a one-line attribution
  ("Lesson by Cognito — free revision platform"). Server-rendered, static,
  no client data fetching; the embed loads only on click (privacy + page
  weight). Per-course `VideoObject` JSON-LD follows the 0011 pattern.
- Subpage H1/breadcrumb follow the course-header anatomy (0009/0010
  contract): board → level → course → "Videos".

---

## 7. Legal & etiquette

- **Embedding** via the official (privacy-enhanced) YouTube player is the
  YouTube ToS-compliant path. No downloading, no re-hosting, no
  metadata-scraping beyond public pages, no autoplay.
- **Cognito** publishes free content; we link and attribute every lesson
  (course link in the map file, per-row attribution in the lane). The crawl
  is polite (rate-limited, cached, sitemap-driven). A short courtesy note to
  Cognito is recommended before public launch — free platforms usually
  welcome the discovery traffic; if they object, the flag kills the surface
  without a code deploy and the data files can be dropped in one patch.
- **Spec-point texts** quoted in the map stay within the spine's existing
  licensing posture (boards' spec statements are already referenced there).

---

## 8. Verification gates (all must be green per patch batch)

1. **Schema:** every `video-map/<slug>.json` validates against
   `hub.video-map/1` (zod at build time + a CI step).
2. **Referential integrity:** every `mappings[].specs[]` code exists as a
   `SPEC_POINT` node in that course's spine; every `videos[].id` matches
   `^[\w-]{11}$`; no duplicate video ids within a file.
3. **Review law:** zero mappings with `reviewed: false` in `content/` (CI
   assertion — the draft area is outside `content/` by path).
4. **Coverage census:** regenerate the coverage block from the mappings and
   assert it matches the committed block (no hand-edited numbers) —
   content-maps `_report` style.
5. **Live spot-check:** N random rows per batch (≥5): the Cognito lesson URL
   still resolves and still embeds the recorded video id.
6. **Hub CI:** existing `verify` + `hub` lanes green; the lane degrades to
   its honest empty state with the flag off (asserted in the PR
   description, same as the Seneca gate).

---

## 9. Phases

| Phase | Content | Exit gate | Est. |
| --- | --- | --- | --- |
| **P0 — Probe** | done — this document + live worked example | §2 evidence table | ✅ |
| **P1 — Crawler + schema** | `scripts/video-map/` crawler + inventory for the 1,166 pages + schema + empty-file skeletons + validation gate | `inventory.json` for all 11 shelves; schema check green | ~1 day |
| **P2 — First course end-to-end** | draft + review + commit for **`igcse-biology-19`** (4BI1, the probe course): 86 videos | reviewed file on main; every gate §8 green | ~1 day |
| **P3 — Hub surface** | `lib/video-map.ts` + Videos tile + `/videos` lane + flag; PR batch (house style) | CI green; empty-state verified; lane live behind flag | ~1 day |
| **P4 — Scale** | remaining 10 shelves → files (sciences IGCSE/CIE A-level, maths), review in batches | all direct-match courses mapped or honestly empty | ~2–4 days agent + review batches |
| **P5 — Future consumers** | §10 | each its own plan doc | later |

Phase order is deliberate: the dataset exists before any UI (P2 before P3),
so the feature can't ship a pretty shell over an empty map.

---

## 10. Future consumers (the reason the map is "the product")

- **Spec-point coverage %** per course — "142 of 165 spec points have video
  teaching" — the honest version of the retired fake progress rings (0013).
- **Strengths→video**: F184 decay model names a weak spec point → one
  click shows its teaching video (the learner loop the hub currently
  can't close).
- **Question→video**: after a wrong answer, link the video(s) covering that
  question's spec point (the map is already spec-keyed; questions are
  spec-mapped via `content-maps`).
- **Revision plans** with video steps per session.
- **Second sources** (FreeScienceLessons, Cognito's future shelves, board
  channels): the schema's `source.provider` and per-video granularity make
  adding a provider additive, not a redesign.

---

## 11. Open questions (living — amend as decided)

1. **IAL lanes** (YBI11/YCH11/YPH11): accept CIE-A-level topical mapping with
   `boardMismatch: true`, or hold until a better source exists? → decide at
   P4.
2. **Duration metadata:** pull via YouTube oEmbed per video at crawl time
   (nice for the lane) — check oEmbed quota posture before committing.
3. **Tier split** on GCSE maths (foundation/higher) and triple/double-award
   re-use: does a double-award lane cite a subset of the triple shelf's
   videos? Needs one probe lesson-diff before P4.
4. **Cognito content drift:** re-crawl cadence (suggest: monthly, diff-only)
   and what happens when a video id dies (coverage block catches it; the
   spot-check gate catches it per batch).
5. **0607 International Maths** vs 0580 shelf overlap — verify in the draft
   pass (§3 note).

---

## Appendix A — URL grammar (as observed 2026-10-31)

```
sitemap:   https://cognito.org/sitemap-subtopics.xml     (12,049 URLs)
lesson:    /coursesubtopic/<course>-<level>-<board>[-tier]_<ref>   (GCSE: ref = spec section)
           /coursesubtopic/<course>-alevel-<board>_<id>            (A-level: opaque id)
course:    /courses/<level>/<subject>/<board>
lesson:    /courses/<level>/<subject>/<board>/notes/<opaque>/<ref>-<slug>
course codes: b1/c1/p1 = KS3 · b2/c2/p2/m2 = GCSE · b3/c3/p3 = A-Level
boards:    aqa, cie, edexcel (UK), iedexcel (International), ocra, ocrb, ocr, sqa5, default
```

**Worked example (extracted live):** lesson
`/courses/gcse/biology-triple/iedexcel/notes/TGVNQ3NhbnA/1.1-characteristics-of-living-organisms`
→ H1 `1.1 - Characteristics of Living Organisms` →
`youtube-nocookie.com/embed/aGDFNZApXXI` → binds to `igcse-biology-19` spine
spec points under section 1.1.

## Appendix B — shelf census (sitemap, 2026-10-31)

| Shelf | Pages | Shelf | Pages |
| --- | --- | --- | --- |
| GCSE Biology · cie | 85 | A-Level Biology · cie | 139 |
| GCSE Biology · iedexcel | 86 | A-Level Chemistry · cie | 130 |
| GCSE Chemistry · cie | 77 | A-Level Physics · cie | 93 |
| GCSE Chemistry · iedexcel | 78 | GCSE Maths · cie | 145 |
| GCSE Physics · cie | 92 | GCSE Maths · iedexcel | 142 |
| GCSE Physics · iedexcel | 99 | **Direct-match total** | **1,166** |

(Other shelves captured by the crawler but out of v0.1 scope: AQA/OCR/SQA
GCSE, AQA/OCR A-level, KS3, IB/AP — see §3.)

---

## 12. Amendments (append-only — never rewrite the body above)

### A1 — 2026-10-31 · P1 executed; home moved to `Videos/` (owner instruction)

All video-map tooling, outputs, docs and trackers now live in
`Videos/` of **SyllabAI/syllabai-resources** (owner instruction, 2026-10-31):
`Videos/scripts/` supersedes the `scripts/video-map/` path named in §5; drafts
stay outside any content directory exactly as §5 required. The P1 deliverable
`Videos/inventory/cognito-lessons.json` uses schema
`syllabai.video-inventory/1` for the **draft stage**; `hub.video-map/1` (§4.2)
remains the schema for committed `content/video-map/<slug>.json` files.

### A2 — 2026-10-31 · §2 correction: science lesson pages embed the video in raw HTML

Live re-verification during P1: the science shelves' lesson pages carry the
full lesson payload in the page's RSC flight data
(`subtopicVideoURL` + `type:"video"` subelements with the YouTube embed) —
**plain HTTP extraction works; no headless render needed**. The §2 note
("client-rendered, no video data in raw HTML") was true only of the
`/coursesubtopic/` landing pages, not the `/notes/` lesson pages. The maths
shelves (`m2-gcse-*`) DO fetch lesson data client-side via
`api-2.cognitoedu.org/graphql` — for those two shelves P1 used the headless
render (the original §2 method), reading the hydrated YouTube iframe.

### A3 — 2026-10-31 · §3 clarification: subtopic pages vs lesson pages

The sitemap's 1,166 in-scope `/coursesubtopic/` pages are **subtopic
landing/nav pages**, not lesson pages; videos live on the `/notes/` (sciences)
or `/lessons/` (maths) pages they link to. P1 therefore crawled both levels:
1,166 subtopic pages (census gate, exact match to the §3 table) and **1,275
lesson pages** (the union of their lesson links, deduped by opaque id + slug).
The §9 P1 exit gate "inventory.json for all 11 shelves" is met at both levels;
lesson-level is the alignment input for P2.

### A4 — 2026-10-31 · New finding: guest-gating (new open question 6)

Cognito serves the video payload to logged-out sessions for **730 of 1,275**
lessons only; 542 are guest-gated (no video even after full hydration —
render-probe verified), including the **entire** `c3-alevel-cie` and
`p3-alevel-cie` shelves. The crawl is honest: gated lessons simply carry
`videoId: null`. New open question (complements §7 etiquette):

> **6. Guest-gated videos:** accept partial guest-visible coverage, or crawl
> with a Cognito account (a real etiquette/ToS posture change needing owner
> sign-off), or convert the §7 courtesy note into a requirements conversation
> with Cognito? → decide before P4; blocks A-level chemistry/physics and
> tails of every other shelf.

Evidence: `Videos/docs/P1-CRAWL-REPORT.md` §4; per-shelf table in
`Videos/trackers/P1-INVENTORY-TRACKER.md`.

### A5 — 2026-10-31 · P1 exit gate MET

`Videos/scripts/validate-inventory.mjs --live 5`: V1 provenance, V2 census
(11/11 shelves exact, 1,166/1,166, 3,871-row shelf census), V3 row integrity
(unique, `^[\w-]{11}$`, Cognito-host-only), V4 draft law (zero alignment
fields), V5 worked example (`aGDFNZApXXI`), V6 live spot-check 5/5 —
**ALL GATES GREEN**. Phase table: **P1 ✅ done** (P0 ✅, P2 next:
`igcse-biology-19`).

### A6 — 2026-10-31 · P2 finding: §5 Step 3 pass 1 adapted — Cognito's chapter numbering is NOT the spec numbering

The deterministic pre-pass (§5 Step 3 pass 1) assumed GCSE lesson refs align
with spec refs ("the 4BI1 case"). Live P2 verification on `b2-gcse-iedexcel`:
**only 25/109 lesson refs coincide with spine codes, and several coincide
misleadingly** — Cognito organises its course in its own chapters 1–11 (plus
10.x core practicals and 11.x skills), while 4BI1 has 5 spec sections. E.g.
Cognito `3.1 Photosynthesis` vs spec `3.1` (meiosis) would auto-map wrongly.
Ref matching is therefore **demoted to a trap warning** (P1 tracker gap 4
extends from subtopic refs to lesson refs), and the deterministic pass is
re-scoped as a **lexical evidence scorer** (`align-deterministic.mjs`: token
overlap of lesson title/description/keyPoints against spine statements, refs
deliberately ignored) whose output feeds the LLM curation pass. The alignment
itself remains LLM-drafted with per-row evidence, confidence labels and the
review gate (§5 Step 4) — the quality law is unchanged. Recorded in
`Videos/drafts/igcse-biology-19/coverage-report.md` §Method.

### A7 — 2026-10-31 · P2 finding: video references vs distinct videos

Shelf totals count id **references** (one lesson can embed several; Cognito
re-embeds one video across adjacent lessons — observed pairs 3.5+3.6,
7.16+7.17, 9.6+9.7). `hub.video-map/1` `videos[]` therefore lists **distinct**
ids (73 on this shelf) while `mappings[]` carries a row **per lesson binding**
(the many-to-many law of §4.2 in its first real exercise). Per-mapping
`lessonRef`/`lessonUrl` fields (draft schema only) keep shared-video rows
unambiguous for review.
