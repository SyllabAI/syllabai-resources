# Videos — Cognito video map (F189)

Working home for the **specification-point → video map** feature (plan doc:
[`docs/F189-VIDEO-MAP-PLAN.md`](docs/F189-VIDEO-MAP-PLAN.md)). The map's goal is
not a videos page — it is a first-class dataset: every spec point of every
SyllabAI course bound to the best free teaching video for it, starting with a
Cognito pilot. Owner instruction (2026-10-31): all video-map outputs, scripts,
docs and trackers live in this folder.

## Layout

```
Videos/
  README.md                    this file
  docs/
    F189-VIDEO-MAP-PLAN.md     the living plan (imported from syllabai-v2 docs/, amendments appended)
    P1-CRAWL-REPORT.md         P1 run report: method, evidence, anomalies, gates
  scripts/
    cognito-crawler.mjs        sitemap-driven two-level crawler (subtopics -> lessons), RSC-payload extractor
    cognito-maths-render.mjs   headless-render extractor for the two maths shelves (agent-browser CLI)
    cognito-maths-merge.mjs    folds maths render results into the inventory
    validate-inventory.mjs     P1 gate runner (V1–V6, optional live spot-check)
  inventory/
    cognito-lessons.json       THE P1 deliverable — schema syllabai.video-inventory/1
    cognito-lessons.csv        flat lesson view (1,275 rows)
    cognito-shelves.json       every shelf in the sitemap (39), in-scope flags
    run-stats.json             last crawl run's fetch stats
  trackers/
    P1-INVENTORY-TRACKER.md    per-shelf status, gaps, decisions needed
    P2-ALIGNMENT-TRACKER.md    first-course alignment status, gaps, review load
  drafts/                      DRAFT alignment area — never enters any content/ dir
    igcse-biology-19/          P2: draft video map + review file + coverage report + inputs
  .cache/                      raw HTML + render logs (gitignored, resumable)
```

## Status (2026-11-01)

| Phase | State | Evidence |
| --- | --- | --- |
| P0 — Probe | ✅ done | F189 §2 |
| **P1 — Crawler + inventory** | ✅ **done — all gates green** | `inventory/cognito-lessons.json`, `docs/P1-CRAWL-REPORT.md`, `validate-inventory.mjs --live 5` |
| **P2 — First course map (igcse-biology-19)** | ✅ **MERGED** — owner ruling "approve all except 4.16" (104/105 rows) | hub `apps/hub/content/video-map/igcse-biology-19.json` @ `51ec8fffe` (PR #574); closure PR #265 |
| **P2B — External-channels sweep: biology (owner ask)** | 🟢 **self-review applied (delegated, 2026-11-09) — 25/28 rows approved, verdicts in-draft; hub merge shipped** | `drafts/igcse-biology-19/video-map.draft.external.json` + `review-file-external.md` (28 rows: 19 medium / 9 low, all `reviewed: false`, oEmbed 27/27); census 165/176 if fully approved |
| **P2C — All-subjects sweep (owner ask)** | 🟢 **self-review applied (delegated, 2026-11-09) — 221/238 rows approved (7+1+2+1 rejects), verdicts in-draft; hub files shipped** | 6 per-course drafts (`drafts/<course>/video-map.draft.external.json`) + `drafts/review-file-external-p2c.md` + `docs/P2C-COURSE-CENSUS.md`; 248 rows (chem 94 / phys 102 / maths 7 / CIE trio 45 pilots), oEmbed 214/214 |
| **P2D — CIE A-level trio lane (owner ask)** | 🟢 **self-review applied (delegated, 2026-11-09) — 273/303 rows approved (6+14+10 rejects, 19 spec trims), verdicts in-draft; hub files shipped** | 3 per-course drafts (`drafts/cie-a-level-{biology,chemistry,physics}-25/`) + `drafts/review-file-external-p2d.md`; 303 rows (bio 104M/35L, chem 75M/28L, phys 46M/15L), identity 264/264 (104 oEmbed + 160 FSL 401 → thumbnail-fallback), all `reviewed: false` + `boardMismatch: true` |
| **P2E — PhysicsOnline lane, physics trio (owner ask)** | 🟢 **self-review applied (delegated, 2026-11-10) — 291/303 rows approved (12 full-row rejects, 3 spec trims), verdicts in-draft; hub files shipped** | `drafts/{cie-a-level-physics-25,cie-igcse-physics-23,igcse-physics-19}/video-map.draft.external-p2e.json` + `drafts/review-file-external-p2e.md`; @PhysicsOnline 1,080 uploads 100% net-new, oEmbed 229/229; coverage 66→131/303 (CIE A-level), 16→76/294 (CIE IGCSE), 142→146/195 (Edexcel IGCSE) |
| **P3 — Hub surface** | ✅ **MERGED** — loader + `/courses/[course]/videos` route + course-card mount | hub PR #906 (`lib/video-map.ts` + tests, `videoMap` flag live); data via hub PR #888 (10 courses) |
| P4 — Scale | pending | plan §9 |

Headline numbers: **1,166/1,166 in-scope subtopic pages crawled** (4 stale-404
rows recorded), **1,275 lesson pages** inventoried, **740 video-ID references**
extracted (730 lessons with a primary video). **542 lessons are guest-gated** —
Cognito serves no video to a logged-out session — including the *whole* A-level
chemistry and physics shelves.

P2 (first course, `igcse-biology-19`): **137/176 spine spec points drafted**
(78%), 72/73 guest-visible videos mapped, every row carries confidence +
evidence and is `reviewed: false` until the owner review (plan §5 Step 4).
Key finding (amendment A6): Cognito's chapter numbering is NOT the spec
numbering — refs are never join keys; alignment runs on lesson content.

## Reproduce

```bash
node Videos/scripts/cognito-crawler.mjs          # ~4 min: subtopics + science lessons
node Videos/scripts/cognito-maths-render.mjs     # ~30 min: maths shelves via headless render
node Videos/scripts/cognito-maths-merge.mjs      # fold maths rows in + regenerate CSV
node Videos/scripts/validate-inventory.mjs --live 5

# P2 — first-course alignment draft (igcse-biology-19)
node Videos/scripts/align-extract-lessons.mjs b2-gcse-iedexcel   # enrich video lessons (cached, resumable)
node Videos/scripts/align-deterministic.mjs                      # lexical evidence pass
node Videos/scripts/align-build-draft.mjs                        # draft + review file + coverage (gates enforced)
node Videos/scripts/align-spotcheck.mjs 5                        # live spot-check gate (§8.5)
```

The crawler is resumable (raw HTML cached in `Videos/.cache/`); re-runs
re-extract without re-fetching. Politeness: identifying UA, concurrency 6 with
jittered delays, retry+backoff, `robots.txt` re-checked per run (`Allow: /`).
