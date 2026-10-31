# PR body — Videos: F189 P2 (igcse-biology-19 alignment draft)

> Ready-to-file body for branch `videos/p2-align-igcse-biology-19` → `main`
> (SyllabAI/syllabai-resources). Task T-VIDEOMAP-P2. All outputs live under
> `Videos/` per the owner instruction (plan amendment A1); nothing outside
> `Videos/` is touched.

**Title:** `Videos: F189 P2 — igcse-biology-19 alignment draft (137/176 spec points, reviewed:false) (T-VIDEOMAP-P2)`

---

## What this is

Phase 2 of the F189 video map (plan: `Videos/docs/F189-VIDEO-MAP-PLAN.md`):
the **alignment draft** for the first course, `igcse-biology-19` (4BI1), built
on the P1 inventory. **This PR adds draft material under `Videos/drafts/`,
four `Videos/scripts/` tools, two trackers and plan amendments — nothing is
written to any `content/` directory, and every mapping row is
`reviewed: false`** (the draft law, plan §4.2/§5).

| | |
| --- | --- |
| Working set | 75 guest-visible lessons / 73 distinct video ids (76 references) on `b2-gcse-iedexcel` |
| Drafted | 137/176 spine spec points (78%) · 72/73 videos mapped · 105 rows (73 high / 30 medium / 2 low) |
| Gates | referential integrity · id shape · dup ids · draft law (0× reviewed:true) · census recompute · live spot-check 5/5 — ALL GREEN |
| Honest unmapped | 1 video (`1.4 Magnification & Units` — no spine statement) + 42 spec points with no guest-visible video (34 gated lessons, D1) |

## Contents

- `Videos/drafts/igcse-biology-19/`
  - `video-map.draft.json` — the draft (`hub.video-map/1` shape under draft
    schema `syllabai.video-map-draft/1`), full provenance (sha256 of spine,
    inventory, enrichment, candidates, curation)
  - `align-curation.json` — the LLM draft pass output: per-lesson bundles
    with confidence + evidence
  - `deterministic-candidates.json` — lexical evidence scorer output
  - `lesson-enrichment.json` — per-lesson description + keyPoints extracted
    live (RSC payload; resumable cache gitignored under `Videos/.cache/p2/`)
  - `spine.json` — the spine of record fetched from
    `apps/hub/spines/igcse-biology-19.json` (sha-pinned)
  - `review-file.md` — all 105 rows sorted low→high with checkboxes, evidence
    and Cognito deep links; **the owner review surface (plan §5 Step 4)**
  - `coverage-report.md` — content-maps `_report` style; coverage block
    recomputed from mappings, never hand-written
- `Videos/scripts/` — `align-extract-lessons.mjs`, `align-deterministic.mjs`,
  `align-build-draft.mjs`, `align-spotcheck.mjs`
- `Videos/trackers/P2-ALIGNMENT-TRACKER.md` (+ `P2-PR-BODY.md`)
- `Videos/docs/F189-VIDEO-MAP-PLAN.md` — append-only amendments
  **A6** (Cognito's chapter numbering ≠ spec numbering; deterministic pass
  re-scoped to lexical evidence) and **A7** (references vs distinct videos;
  per-binding mapping rows)

## Method (two passes, cheapest first — plan §5 Step 3, adapted per A6)

1. **Deterministic pass** — lexical scorer over title/description/keyPoints
   vs spine statements. Lesson refs are deliberately NOT join keys: Cognito
   organises its course in its own chapters 1–11 (only 25/109 refs coincide
   with spec codes, several misleadingly, e.g. Cognito `3.1 Photosynthesis`
   vs spec `3.1` meiosis).
2. **LLM draft pass** — every one of the 74 mappable lessons bound to 1..N
   spec points with a confidence label and a one-line evidence string;
   anything below the evidence bar stays unmapped rather than guessed.

## Review notes

- **Zero `reviewed: true` rows anywhere in this PR** (draft law, plan §4.2).
  The review file is the owner's surface: 2 low + 30 medium rows need
  individual review; 73 high rows are batch-approvable on evidence.
- The draft never enters `content/` — path-enforced by this PR's file list.
- `Videos/.cache/` remains gitignored (raw fetch cache, resumable).
- No hub/runtime code touched; dataset-before-UI ordering preserved (§9).
