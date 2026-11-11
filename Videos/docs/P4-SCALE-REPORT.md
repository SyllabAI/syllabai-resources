# P4 — Scale pass: the video map across the full 106-course spine census

Task **T-VIDEOMAP-P4** · executed 2026-11-11 · exit gate of plan §9 ("all direct-match courses mapped or honestly empty") scaled to every spine-backed course in the registry.

## 1. Decision matrix

Every one of the **106** spine-backed courses was classified *before* any mapping work (analysis artifact: decision matrix over `apps/hub/spines`; generator committed as `Videos/scripts/build-p4-inheritance.py`, threshold data inline):

| class | n | meaning |
| --- | --- | --- |
| mapped | 10 | external lanes already shipped (P2/P2B-D/P2E) |
| inherit | 35 | child of a mapped course (AS←A-level, modular←linear, double-award←triple, core←extended, IAL←CIE A-level topical) — rows derived at build time |
| shelf-direct | 4 | direct match from the Cognito channel pool, no parent needed (maths courses) |
| mechanics | 4 | maths mechanics units — cross-subject re-binding of approved physics rows |
| honest-empty | 53 | no channel inventory can honestly serve these specs — recorded, not faked |

Key probes that shaped the lanes: AS ⊂ A-level is code-identical for bio/chem (123/123, 204/204 same-code-same-title); foundation ⊂ higher maths is near-exact title reuse; IAL sciences vs CIE A-level have severely divergent spec wording (containment hi55 = 7/170, 19/319, 14/171) — so the IAL science lanes are honestly thin; CIE 0607 international maths reuses the 0580 extended text almost wholesale.

## 2. Lanes executed

### 2a. Shelf-direct (4 Cognito maths lanes)

Pool: the Cognito YouTube channel enumeration (529 uploads; maths-relevant subset shortlisted). Identity: oEmbed sweep on every selected video (128/128 verified, author `Cognito`), title-only evidence, tightened binding rule, sewage filter (channel promos and platform announcements excluded).

| course | rows | videos | specs covered / total |
| --- | --- | --- | --- |
| cie-igcse-maths-25-extended | 118 | 118 | 71/178 |
| cie-igcse-further-maths-additional-maths-25 | 3 | 3 | 3/77 |
| igcse-maths-b-16 | 107 | 107 | 40/98 |
| igcse-further-maths-19 | 31 | 31 | 15/43 |

`cie-igcse-further-maths-additional-maths-25` is a deliberate near-empty: the Cognito pool is a GCSE-shape pool and additional-maths specs are mostly absent from it — 3 honest rows shipped rather than keyword-adjacent padding. A future lane needs a dedicated additional-maths source.

### 2b. Mechanics cross-subject (4 maths mechanics courses)

Source pool: the owner-approved physics external lanes (igcse-physics-19, cie-igcse-physics-23 + P2E, cie-a-level-physics-25 + P2E). The bar is *higher* than same-subject: a row survives only when the video title names the actual mathematical topic (SUVAT, projectiles, Newton's laws, momentum/impulse, moments, work-energy-power). Every row carries `crossSubject: "physics->maths-mechanics"` and `boardMismatch: true`.

| course | rows | specs covered / total |
| --- | --- | --- |
| cie-a-level-maths-20-mechanics | 65 | 17/22 |
| cie-as-maths-20-mechanics | 65 | 17/22 |
| ial-maths-20-mechanics-1 | 43 | 10/12 |
| ial-maths-20-mechanics-2 | 41 | 8/13 |

Honestly unbound by design: modelling-vocabulary, calculus-kinematics, connected-particles/pulley, rigid-body (rods/ladders) and successive-impact specs — no video title evidences them.

### 2c. Inheritance (35 courses, build-time derivation)

No new LLM mapping decisions. A committed containment map (`Videos/drafts/_p4/inheritance-map.json`, generator `Videos/scripts/build-p4-inheritance.py`) binds each child spec to its best parent spec by idf-weighted title-token containment at **≥ 0.55 with a minimum of 3 informative tokens** (shorter titles produce degenerate 1.0 containments — see §4). At build time the builder re-emits every owner-approved parent row bound to the mapped parent spec against the child spec, `method: "inherited-external"`, with the derivation recorded in a per-row `inherit` block. Map-level coverage: 3287 of 4282 child specs map; *emitted* coverage is bounded by where the parents actually have approved rows.

| inherited course (top 6 by rows) | rows | specs covered / total |
| --- | --- | --- |
| igcse-science-double-award-17-physics ← igcse-physics-19 | 140 | 111/147 |
| cie-as-physics-25 ← cie-a-level-physics-25 | 130 | 85/145 |
| igcse-physics-modular-24-unit-1 ← igcse-physics-19 | 113 | 74/94 |
| igcse-science-double-award-modular-24-physics-unit-1 ← igcse-physics-19 | 107 | 70/90 |
| cie-igcse-maths-international-maths-23-extended ← cie-igcse-maths-25-extended | 102 | 59/165 |
| cie-igcse-maths-25-core ← cie-igcse-maths-25-extended | 92 | 51/112 |

Thinnest lanes (all honest): `igcse-maths-a-modular-24-foundation-unit-1` (1 row — the higher course's approved rows simply do not reach those specs yet), `cie-igcse-science-combined-science-23-biology` (2), `igcse-maths-a-18-foundation` (3), IAL sciences (5–10 rows: Edexcel wording diverges from CIE far beyond the containment threshold — a future Edexcel-native channel lane is the real fix, not threshold-lowering).

### 2d. Honest-empty (53 courses, recorded)

No enumerated channel (Cognito, Freesciencelessons, Doodle, Amoeba Sisters, Malmesbury, PhysicsOnline) contains honest teaching content for these specs; nothing was forced:

· cie-a-level-accounting-21 · cie-a-level-business-23 · cie-a-level-computer-science-19
· cie-a-level-economics-23 · cie-a-level-geography-21 · cie-a-level-maths-20-probability-and-statistics-1
· cie-a-level-maths-20-probability-and-statistics-2 · cie-a-level-maths-20-pure-1 · cie-a-level-maths-20-pure-2
· cie-a-level-maths-20-pure-3 · cie-as-accounting-21 · cie-as-business-23
· cie-as-computer-science-19 · cie-as-english-general-paper-21 · cie-as-environmental-management-20
· cie-as-maths-20-probability-and-statistics-1 · cie-as-maths-20-pure-1 · cie-as-maths-20-pure-2
· cie-igcse-accounting-21 · cie-igcse-accounting-25 · cie-igcse-business-23
· cie-igcse-business-25 · cie-igcse-computer-science-23 · cie-igcse-economics-20
· cie-igcse-economics-25 · cie-igcse-english-language-20 · cie-igcse-english-language-25
· cie-igcse-english-literature-21 · cie-igcse-environmental-management-25 · cie-igcse-geography-20
· cie-igcse-geography-25 · cie-igcse-history-18 · cie-igcse-ict-21
· cie-igcse-religious-studies-23 · ial-further-maths-18-further-pure-1 · ial-maths-20-decision-1
· ial-maths-20-pure-1 · ial-maths-20-pure-2 · ial-maths-20-pure-3
· ial-maths-20-pure-4 · ial-maths-20-statistics-1 · ial-maths-20-statistics-2
· igcse-accounting-17-financial-statements · igcse-accounting-17-introduction-to-bookkeeping-and-accounting · igcse-business-19
· igcse-economics-17 · igcse-english-language-a-16-paper-1-non-fiction-texts-and-transactional-writing · igcse-english-language-a-16-paper-2-poetry-and-prose-texts-and-imaginative-writing
· igcse-english-language-a-16-paper-3-coursework · igcse-english-literature-16 · igcse-geography-19
· igcse-history-17 · igcse-ict-17

## 3. Emitted state (hub)

- `registry.json`: **53 courses** (was 10) — lanes: external-channels, external-channels (inherited), site+external.
- mapping rows across all courses: **2827** (prior lanes 930 · shelf-direct 259 · mechanics 214 · inherited 1424); course-sum spec points covered **2349** (a video may serve several courses — the many-to-many ruling).
- `flags.json` `videoMap.courses` = 53, status `live (T-VIDEOMAP-P3+P4)`; per-course `/courses/[course]/videos` lanes now resolve for all 53.
- Gates: builder exit 0; zero `reviewed:false` rows in content (re-verified per file); every mapping spec in its spine; every mapping video in its file's `videos[]`; no duplicate ids.

## 4. Review law (delegated self-review, owner chat 2026-11-09)

- 8 new drafts reviewed row-by-row by delegated reviewers: **15 spec-level rejects** applied (13 shelf-direct, 2 mechanics), 8 rows lost all specs and dropped; verdicts in each draft dir.
- Inheritance derivation spot-checked: 12 (child, spec) pairs across all six lane families; the sample exposed degenerate 1.0-containment matches on trivially short spec titles — one of which carried a parent row and would have emitted a wrong row. Fix: ≥3-informative-token guard; map regenerated; re-verified. Record: `drafts/_p4/owner-review-verdicts.p4-inherit.json`.
- Reject ledger: `drafts/review-file-external-p4.md`.

## 5. Exit gate

Every one of the 106 spine-backed courses is now **classified, and either shipped (53), inheriting (35), cross-served (4), or honestly empty with the reason recorded (53)** — no course is silently absent, and no row exists anywhere on weaker than title-only evidence. Gate met.

## 6. Post-pass correction (2026-11-12) — the spec-code mirror drift

Found during the P2F render pass (hub PR #934's prerender verification): **igcse-chemistry-19's 87 lesson rows joined 0 spec points** — the P4 emit validated row specs against `apps/hub/spines/igcse-chemistry-19.json` (seed-era bare register, `1.1`), while the render joins `apps/hub/content/igcse-chemistry-19/curriculum.json` (canonical `4CH1-1.1` re-issue from the subject-identity lanes). The 119/182 badge was true of the file and false of the page: every lesson row had been invisible since the P4 pass. Census: exactly 2 of 106 mirrors drifted (igcse-chemistry-19, igcse-geography-19 — the latter has no video rows yet; both repaired to the content plane of record, positional within family with title equality asserted).

Fixes, representation-only (no review ruling changes):
- **Drafts re-keyed** onto the canonical register: igcse-chemistry-19 external draft (87 rows, 119 codes) + verdicts (8 rejects); `_p4/inheritance-map.json` parentSpec entries for the 5 chemistry-children lanes (the re-emit exposed this: bare parentSpecs silently dropped 38-row chem-u1 to 0).
- **Emitter hardening**: `assertSpineMirror` gate at all three spine-load sites (main loop, P4 inherit, P2F) — a spines/ vs content/ SPEC_POINT drift is now a build-time break, not a silent render void.
- **Hub re-ship**: 2 mirror spines + igcse-chemistry-19 video-map (specs now join 119/119) + registry; per-course row/spec counts verified byte-equal to the pre-fix values on all 6 chemistry-lineage courses. Hub PR: `hub/spec-code-mirror`; resources PR: `videos/spec-code-mirror`.
