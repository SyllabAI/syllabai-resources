# P5 — Cognito channel completion (T-VIDEOMAP-P5)

Owner ask (chat 2026-11-12): *"file it as the next lane (P5)"* — map the unmapped
remainder of the Cognito Edu channel onto the courses whose children inherit.

## Pool

- Channel enumeration: **529 public uploads** (`inventory/channels/cognito-uploads.json`).
  Re-enumerated 2026-11-12 before the lane: **0 delta** — the 545–548 channel-header
  count includes members-only/shorts the public `/videos` tab does not expose.
- Already mapped before P5: **224** unique Cognito videos across 41 courses.
- Unmapped remainder: **309**. Honest no-target skips: **55** (20 KS3 — the spine
  starts at IGCSE; 28 psychology — no SyllabAI course; 7 platform/exam-service
  announcements — sewage filter). Routed into the lane: **254**.

## Routing (title-prefix shape of the channel)

| route | videos | rows shipped | rejects |
| --- | --- | --- | --- |
| cie-a-level-biology-25 (A-Level Biology — the channel's only A-level subject) | 70 | 60 | 10 |
| cie-igcse-chemistry-23 (GCSE Chemistry) | 74 | 62 | 12 |
| cie-igcse-physics-23 (GCSE Physics) | 82 | 73 | 9 |
| cie-igcse-biology-23 (GCSE Biology) | 26 | 12 | 14 |
| igcse-maths-a-18-higher (GCSE Maths — pool already exhausted by P4) | 2 | 1 | 1 |
| **total** | **254** | **208** | **46** |

Zero A-level chemistry/physics/maths uploads exist on the channel; those lanes get
nothing here (their Cognito shelf sites are guest-gated too).

## Method

1. Re-enumerate (`scripts/p2b/channel_enumerate.py`) → 0 delta vs the P4 cache.
2. oEmbed identity sweep **254/254 live, author `Cognito`**
   (`scripts/p5/p5_oembed_sweep.py`, `inventory/channels/candidate-oembed-p5.json`).
3. Subject routing + top-8 SPEC_POINT candidates per video via idf token overlap
   against the content-plane spine (`scripts/p5/p5_candidates.py`).
4. LLM title-to-spec adjudication under the tightened binding rule (the title must
   name the spec's distinctive content), per subject cluster.
5. Delegated self-review (owner chat 2026-11-09 standing ruling): programmatic
   re-verification (identity, spine membership, no duplicates against the existing
   union, confidence never high) + judgment pass — **5 full-row drops + 2 spec
   trims** (reasons in the per-course verdicts), borderline low rows kept and named
   in `drafts/review-file-external-p5.md`.

## Emit + cascade

Builder gains a P5 section placed **before** the P4 inherit loop: the 5 parent
courses are appended first (second-lane shape, P2F pattern — upstream sections
rewrite fresh, P5 appends, re-runs stay idempotent), then the inherit section
cascades the enriched parent rows through the committed containment map
(`drafts/_p4/inheritance-map.json`, purely spine-derived — no re-derivation needed).
P5 rows are medium/low, satisfying the inherit gate's title-only posture.

Result: **14 courses grew** (5 parents + 9 children); 39 files churn only
`generatedUtc` (emit law). Parent-side distinct spec coverage **+371**:

| course | specs | rows |
| --- | --- | --- |
| cie-igcse-chemistry-23 | 17 → **137**/252 | 15 → 77 |
| cie-a-level-biology-25 | 138 → **177**/257 | 133 → 193 |
| cie-igcse-physics-23 | 76 → **155**/294 | 103 → 176 |
| cie-igcse-biology-23 | 13 → **30**/388 | 13 → 25 |
| igcse-maths-a-18-higher | 5/188 | 5 → 6 |
| cie-as-biology-25 (inherited) | 68 → **96**/123 | 66 → 112 |
| co-ordinated double-award chemistry (inherited) | 14 → **108**/181 | 14 → 70 |
| co-ordinated double-award physics (inherited) | 56 → **103**/221 | 71 → 133 |
| combined-science chemistry (inherited) | 6 → **27**/82 | 6 → 29 |

## Gates

- Full emit exit 0; all review-law/integrity gates pass; 0 `reviewed:false` in content.
- Hub video-map tests **16/16 (1055 expects)** incl. the corpus-at-rest census over
  all 53 flagged courses (zod parse + zero-weight anchors + join integrity).
- Corpus spec-join census: **100%** (every lesson-row spec joins its render-plane spine).
- `next build` compiled + prerendered; DOM check on the prerendered videos pages:
  P5 evidence lines present on every P5 course (e.g. chem-23 170 row cards /
  146 P5 evidence lines; co-ord chem 135 cards / 116 P5 lines) and the P5-untouched
  control (igcse-chemistry-19) renders exactly its #940-verified 143 cards.

Hub data re-ship: SyllabAI/syllabai-v2 `hub/p5-cognito-completion`.
