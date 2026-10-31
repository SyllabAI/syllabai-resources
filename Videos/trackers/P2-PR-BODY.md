# PR body — Videos: F189 P2 (igcse-biology-19 alignment draft)

> **FILED 2026-10-31 as PR #256 and MERGED same day** — https://github.com/SyllabAI/syllabai-resources/pull/256
> Branch `videos/p2-align-igcse-biology-19` (`d709b04`) → `main`. Merge commit
> `019947e` (mergeable_state `clean`; sole check `sync` completed success at
> 12:33Z after a 25-minute run, consistent with history). Branch deleted after
> merge. Base of record `56e3e3b`; no drift between filing and merge. Task
> T-VIDEOMAP-P2. Owner review of the 105 rows (`drafts/igcse-biology-19/review-file.md`)
> remains OPEN — nothing is `reviewed: true` yet, Step 5 (commit to
> `content/`) is blocked on it.

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

## Relation to the SME spec-links map (notes / exam questions / flashcards)

Same spine, same law, different join. The SME-* corpus was mapped in
`spec-links/` (`syllabai.learner-spec-links/1.0`): every note, exam-question
part and flashcard joined to official codes via SME's own native `spcpt_*`
anchors, provenance-tiered (T1–T4 / S1–S2 / C1–C3, never guessed), with
`pending` anchors rendered, never dropped. This video map targets the **same
official codes of the same spine of record** (`igcse-biology-19`, 4BI1,
176 statements) under the same philosophy — per-row provenance, honest
unmapped lists, review-gated before serving. The difference is the join
surface: Cognito videos carry **no native spec anchors at all**, and
Cognito's chapter numbering actively misleads (amendment A6: only 25/109
refs coincide with spec codes, several misleadingly — Cognito `3.1
Photosynthesis` vs spec `3.1` meiosis). So instead of an anchor→code join,
we run lexical evidence + LLM draft with per-row confidence/evidence — the
high/medium/low tiers are the analogue of the spec-links provenance tiers,
and `review-file.md` is the analogue of the operator-verdict pass.
Destination shape matches too: a per-course JSON the hub can render
(`content/video-map/<slug>.json` at Step 5), kept `reviewed: false` until
owner review flips rows — the draft law is the analogue of "pending renders
as pending, never silently dropped".

## Review notes

- **Zero `reviewed: true` rows anywhere in this PR** (draft law, plan §4.2).
  The review file is the owner's surface: 2 low + 30 medium rows need
  individual review; 73 high rows are batch-approvable on evidence.
- The draft never enters `content/` — path-enforced by this PR's file list.
- `Videos/.cache/` remains gitignored (raw fetch cache, resumable).
- No hub/runtime code touched; dataset-before-UI ordering preserved (§9).
