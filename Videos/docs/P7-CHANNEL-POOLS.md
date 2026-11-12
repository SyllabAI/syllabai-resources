# P7 — remaining external channel pools (T-VIDEOMAP-P7)

Owner ask (chat 2026-11-13): *"Proceed with remaining channel pools"* — map the unmapped remainder of the four previously-mined pools (P2B/P2C/P2D took the easy wins) onto the 12 science parent courses whose children inherit. Same title-only posture + tightened binding rule as P2E/P5/P6.

## Pool

- Four pools, re-enumerated fresh before the lane (`scripts/p7/p7_enumerate.py`): **amoeba-sisters 179, freesciencelessons 776, malmesbury-education 72, doodlescience 58 = 1,085 public uploads — 0 deltas on all four** (unlike PhysicsOnline’s +1 before P6).
- Already mapped before P7: **417** pool videos across the union. Unmapped remainder: **668**.
- Routed into the lane: **516** (`scripts/p7/p7_target_pool.py` — subject-marker routing per channel shape + idf best-of across the subject’s four parent spines). Skipped honest-no-target: **152** (73 sewage incl. ALL non-science malmesbury content — English-Lit poem analyses, Spanish/German/French lessons, KS3, DT, PE (no such video-map lane exists); 40 amoeba no-biology-vocabulary; 28 no-spine-overlap; 11 misc).

## Method

1. Re-enumerate (0 deltas) → union-exclude → route (516).
2. Top-8 SPEC_POINT candidates per video via idf token overlap (`scripts/p7/p7_candidates.py`).
3. Deterministic binding pre-pass, tightened rule: a spec binds only on a token with in-course df <= 3 (`scripts/p7/p7_candidates.py`). **388 binds proposed**, 128 no-binding rejects.
4. **Agent judgment pass over every proposed row** (`scripts/p7/p7_judgment_*.py`, title-asserted tables): **277 kept** (M88/L189), **111 full-row drops** with reasons — misbind classes: the IAL CORE-PRACTICAL-13 magnet (spec 6.4 attached to 18 unrelated rows), FSL practise-question calculation drills (P6 generic-drill class), Doodle physics videos idf-routed onto biology specs (cross-subject), AQA-specific content verified absent from the spines (homeobox genes, insect tracheal systems, dialysis, cofactors, potometers, oestrogen-cancer), US-curriculum divergence (amoeba), spine-code verification before every rebind (lac operon 16.3.2, 4.2.1 endocytosis, 7.2.2 apoplast, 8.3.4 sinoatrial, 6.1.4 semi-conservative, 6.2.7 deletion/insertion verified in-spine).
5. Identity: **277/277 verified** (159 oEmbed + 118 thumb-fallback for the freesciencelessons embedding-disabled A-level videos, per the P2D law, `identityMethod` per video). Channel-author discovery: DoodleScience’s oEmbed name has no space — expected-author map corrected pre-ship.
6. Delegated self-review per owner chat 2026-11-09 standing ruling; verdicts `owner-review-verdicts.p7.json` x12 (360+ reject-ledger entries total incl. pre-pass no-binds); review file `drafts/review-file-external-p7.md`.

## Emit + cascade

Builder gains a P7 section (9 non-inherit-child parents, appended BEFORE the P4 inherit loop) **and a P7B section (the three ial courses — themselves inherit children — appended AFTER it, the P2F shape)**: the first emit attempt lost the 85 direct ial rows to the inherit rebuild; the split is the committed fix. Children cascade through the committed containment map.

| course (parent) | rows | medium/low | specs drafted (net new) | course coverage |
| --- | --- | --- | --- | --- |
| cie-a-level-biology-25 | 38 | 10/28 | 40 (+3) | 177 → **180** |
| cie-a-level-chemistry-25 | 14 | 6/8 | 11 (+5) | 108 → **113** |
| cie-a-level-physics-25 | 2 | 1/1 | 4 (+0) | 148 → **148** |
| cie-igcse-biology-23 | 29 | 7/22 | 30 (+22) | 30 → **52** |
| cie-igcse-chemistry-23 | 14 | 3/11 | 18 (+8) | 137 → **145** |
| cie-igcse-physics-23 | 19 | 7/12 | 25 (+7) | 162 → **169** |
| ial-biology-18 | 67 | 19/48 | 50 (+48) | 6 → **54** |
| ial-chemistry-17 | 27 | 10/17 | 27 (+28) | 6 → **34** |
| ial-physics-19 | 1 | 1/0 | 1 (+1) | 6 → **7** |
| igcse-biology-19 | 36 | 14/22 | 29 (+0) | 162 → **162** |
| igcse-chemistry-19 | 11 | 2/9 | 11 (+0) | 119 → **119** |
| igcse-physics-19 | 19 | 8/11 | 22 (+2) | 150 → **152** |

**Total: 277 owner-reviewed rows (M88/L189) onto 12 parent courses; 277 cascaded rows onto 24 child courses** (per-course: cie-as-biology… +28; cie-as-chemistry… +13; cie-as-physics… +1; cie-igcse-science-co-ordinated-science… +19; cie-igcse-science-co-ordinated-science… +9; cie-igcse-science-co-ordinated-science… +12 …). The three ial parents additionally carry 10 spec-level inherited rows derived from the P7-enriched a-level parents (cascade artifacts inside parent files).

## Gates

- Full emit exit 0 (after the P7B split fix); all review-law/integrity gates pass; 0 `reviewed:false` in content.
- Hub video-map tests **16/16** — the ial-chemistry-17 at-rest pin updated 42 → 70 (36 lesson rows = 9 inherited + 27 P7 + 34 zero-weight anchors; anchor law unchanged).
- Independent spec-join census: **100%** — 53 courses, **4,193** rows, 0 violations.
- `next build` compiled + prerendered with DOM check on the videos pages (see hub PR).
