# P6 — PhysicsOnline channel completion (T-VIDEOMAP-P6)

Owner ask (chat 2026-11-12): *"Start filing it"* — map the unmapped remainder of the
PhysicsOnline channel (Lewis Matheson, the one channel behind gcsephysicsonline.com +
alevelphysicsonline.com) onto the physics parent courses whose children inherit.

## Pool

- Channel enumeration: **1,081 public uploads** (`inventory/channels/physicsonline-uploads.json`,
  channelId `UCZzatyx-xC-Dl_VVUVHYDYw`). Re-enumerated 2026-11-12 before the lane:
  **+1 net vs the P2E enumeration of 1,080 on 2026-11-10** — the P2E lane cached only its
  303-drafted subset, so the delta video is not individually identified.
- Already mapped before P6: **218** distinct PhysicsOnline videos across 16 courses
  (813 mapping rows: the P2E trio 291 rows + maths-mechanics re-adjudication 134 + inherit
  children 388). All 218 still public — 0 gone private/deleted.
- Unmapped remainder: **863**. Honest no-target skips: **390** (217 exam-news/paper/study-
  advice/promo sewage; 117 no-physics-vocabulary misc; 11 pure-maths masterclasses — SyllabAI
  has no A-level pure-maths course; 45 routed-but-no-spine-overlap). Routed into the lane: **473**.

## Routing (title-marker shape of the channel + cross-spine idf)

| route | videos | rows shipped | reject ledger |
| --- | --- | --- | --- |
| cie-a-level-physics-25 (`- A Level Physics` markers + unmarked cross-spine) | 243 | 38 | 205 |
| cie-igcse-physics-23 (`- GCSE Physics` → best of the two IGCSE spines) | 129 | 38 | 91 |
| igcse-physics-19 (GCSE → best of the two IGCSE spines, Edexcel side) | 101 | 37 | 64 |
| **total** | **473** | **113** | **360** |

GCSE-marked and unmarked-physics videos were routed to the parent whose spine gave the best
distinctive-token idf overlap; the binding rule still gates at adjudication. oEmbed identity
sweep **473/473 live, author `Physics Online`** (`scripts/p6/p6_oembed_sweep.py`).

## Method

1. Re-enumerate → 1,081 public uploads (+1 net vs P2E).
2. oEmbed identity sweep **473/473 live, author `Physics Online`**.
3. Top-8 SPEC_POINT candidates per video via idf token overlap against the content-plane
   spine (`scripts/p6/p6_candidates.py`); cross-spine routing for GCSE/unmarked videos
   (`scripts/p6/p6_target_pool.py`).
4. Deterministic binding pre-pass under the tightened binding rule: a spec binds only if the
   title's matched tokens include a token distinctive for the spec (in-course df ≤ 3) —
   generic physics words can never bind (`scripts/p6/p6_adjudicate.py`). 281 binds proposed.
5. **Agent judgment pass over every proposed row** (`scripts/p6/p6_judgment.py`, each
   decision carrying a title-prefix assertion): **113 kept** (re-binds and trims applied
   in-table), **168 full-row drops** with reasons, plus the 192 pre-pass no-binding rejects —
   **360 reject-ledger entries** in total. Misbind classes caught: word-adjacency on
   *bridge* (Wheatstone vs bridge rectifier), *diagram* (Feynman vs circuit), *specific*
   (specific charge vs acoustic impedance), *sheet/formulae* (equation-booklet walkthroughs),
   *symbols* (maths vs circuit), *normal* (contact force vs optics), *flow* (Stokes vs
   current); generic maths-skills/graph-technique videos rejected wholesale; RAEng-sponsored
   "Engineering a Better World" videos rejected as sponsored sewage; full-paper walkthroughs
   and exam-news rejected per the P2E precedent.
6. Delegated self-review (owner chat 2026-11-09 standing ruling): programmatic re-verification
   (identity, spine membership, no duplicates against the existing union, confidence never
   high) + the judgment pass above; borderline low rows kept and named in
   `drafts/review-file-external-p6.md`.

## Emit + cascade

Builder gains a P6 section placed **before** the P4 inherit loop: the 3 parent courses are
appended first (second-lane shape, P5 pattern — upstream sections rewrite fresh, P6 appends,
re-runs stay idempotent), then the inherit section cascades the enriched parent rows through
the committed containment map (`drafts/_p4/inheritance-map.json`, purely spine-derived — no
re-derivation needed). P6 rows are medium/low, satisfying the inherit gate's title-only posture.

Result: **12 courses grew** (3 parents + 9 children; ial-physics-19 honestly cascades 0 —
its containment map binds none of the P6 rows). Parent-side distinct spec coverage **+28**:

| course | specs | rows |
| --- | --- | --- |
| cie-a-level-physics-25 | 131 → **148**/303 | 177 → 215 (+38) |
| cie-igcse-physics-23 | 155 → **162**/294 | 176 → 214 (+38) |
| igcse-physics-19 | 146 → **150**/195 | 179 → 216 (+37) |
| cie-as-physics-25 (inherited) | 85 → **97**/145 | +29 P6-origin rows |
| co-ordinated double-award physics (inherited) | 103 → **110**/221 | +28 P6-origin rows |
| double-award-17 physics (inherited) | 111 → **113**/147 | +34 P6-origin rows |
| da-modular-24 physics unit-1 (inherited) | 70 → **72**/90 | +31 P6-origin rows |
| modular-24 physics unit-1 (inherited) | 74 → **76**/94 | +28 P6-origin rows |
| modular-24 physics unit-2 (inherited) | 70 → **72**/101 | +9 P6-origin rows |
| combined-science physics (inherited) | 23 → **25**/86 | +5 P6-origin rows |
| da-modular-24 physics unit-2 (inherited) | 39/57 | +3 P6-origin rows (0 new specs) |
| ial-physics-19 (inherited) | 6/171 | +0 (no containment bind) |

Total lane footprint: **280 P6-origin rows across 12 courses** (113 parent + 167 cascaded).

## Gates

- Full emit exit 0; all review-law/integrity gates pass; 0 `reviewed:false` in content.
- Hub video-map tests **16/16 (1055 expects)** incl. the corpus-at-rest census over
  all 53 flagged courses (zod parse + zero-weight anchors + join integrity).
- Corpus spec-join census: **100%** — 53 courses, 3,629 mapping rows, 0 spec-join
  violations (every lesson-row spec joins its render-plane spine).
- `next build` compiled + prerendered (4,703 static pages, exit 0); DOM check on the
  prerendered videos pages: P6 video cards render on every P6 course (spot-verified
  card titles on stripped-DOM HTML; watch-link sets full on all 12 courses) and the
  P6-untouched control (igcse-chemistry-19) renders exactly its #940-verified
  **143 cards**.

Hub data re-ship: SyllabAI/syllabai-v2 `hub/p6-physicsonline-completion`.
