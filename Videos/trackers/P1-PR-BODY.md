# PR body — Videos: F189 P1 (Cognito video-map crawler + inventory)

> Ready-to-file body for branch `videos/p1-crawler` → `main` (SyllabAI/syllabai-resources).
> Filing needs a PAT with Contents + PR write:
> `GH_TOKEN=<pat> git push https://github.com/SyllabAI/syllabai-resources.git videos/p1-crawler`
> then open the PR with this body (title below). Task T-VIDEOMAP-P1.

**Title:** `Videos: F189 P1 — Cognito video-map crawler + 1,275-lesson inventory (T-VIDEOMAP-P1)`

---

## What this is

Phase 1 of the F189 video map (plan: `Videos/docs/F189-VIDEO-MAP-PLAN.md`):
the crawler tooling and the full crawl inventory for the 11 direct-match
Cognito shelves, per the owner's instruction that all video-map outputs,
scripts, docs and trackers live in a new `Videos/` folder. **This PR adds one
new directory and touches nothing else.**

| | |
| --- | --- |
| Base commit | `652ca2d` |
| Deliverable | `Videos/inventory/cognito-lessons.json` — schema `syllabai.video-inventory/1`, `reviewState: draft-p1` |
| Scale | 1,166/1,166 in-scope subtopic pages · 1,275 lesson pages · 740 video IDs |
| Gates | `Videos/scripts/validate-inventory.mjs --live 5` → ALL GATES GREEN (V1–V6, 5/5 live spot-checks) |

## Contents (14 files)

- `Videos/README.md` — folder guide, phase status, reproduce commands
- `Videos/docs/F189-VIDEO-MAP-PLAN.md` — the living plan, imported with
  append-only amendments (§12 A1–A5: tooling home, RSC-payload method
  correction, subtopic-vs-lesson clarification, guest-gating open question)
- `Videos/docs/P1-CRAWL-REPORT.md` — method, run narrative, evidence, anomalies
- `Videos/scripts/cognito-crawler.mjs` — two-level sitemap-driven crawler
  (RSC-payload extraction; polite: identifying UA, concurrency 6 + jitter,
  retries, robots `Allow: /` re-checked per run)
- `Videos/scripts/cognito-maths-render.mjs` — headless render for the two
  maths shelves (their lesson data is client-fetched; agent-browser CLI)
- `Videos/scripts/cognito-maths-merge.mjs` — folds render rows into the inventory
- `Videos/scripts/validate-inventory.mjs` — P1 gate runner (V1–V6 + `--live N`)
- `Videos/inventory/cognito-lessons.{json,csv}`, `cognito-shelves.json`,
  `run-stats.json` — the data (raw crawl only; zero alignment claims)
- `Videos/trackers/P1-INVENTORY-TRACKER.md` — per-shelf state, honest gaps,
  decisions needed (D1–D3), P2 next steps

## Honest gaps (recorded, not hidden)

- **542 of 1,275 lessons are guest-gated** — Cognito serves no video to a
  logged-out session (render-probe verified), including the entire A-level
  chemistry (`c3-alevel-cie`) and physics (`p3-alevel-cie`) shelves. Decision
  D1 in the tracker.
- **4 stale sitemap entries** (HTTP 404) recorded as rows — Cognito's sitemap
  lists pages it no longer serves.
- `.notes-paywalled` markup exists on every page — layout, not a gate signal
  (report §4.3); the only honest signal is whether a video was served.

## Law compliance (AGENT.md)

- Draft-until-review: `reviewState: draft-p1`; **zero** alignment/mapping
  fields anywhere (validated by gate V4). Mappings are P2+, review-gated.
- Provenance: sitemap sha256, per-row `fetchedAt`/`httpStatus`/`method`,
  base commit, tool versions.
- Nothing invented to fill gaps (law 3): gated = null, never guessed.

## Review notes

- `Videos/.cache/` (438 MB raw HTML) is gitignored by design — resumable
  crawl state, never committed.
- The inventory JSON (1.6 MB) is data, intentionally committed as the P1
  artifact; diffs on future re-crawls read as dataset deltas.
- No hub/runtime code is touched; no schema the hub consumes changes in this
  PR (that's P2/P3, per plan §9 order: dataset exists before any UI).
