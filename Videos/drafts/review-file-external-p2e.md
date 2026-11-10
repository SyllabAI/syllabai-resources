# P2E review file — PhysicsOnline lane (T-VIDEOMAP-P2E)

**Source:** @PhysicsOnline — the single YouTube channel behind **gcsephysicsonline.com** and
**alevelphysicsonline.com** (Lewis Matheson, Physics Online Ltd). Both sites are board/topic
front-ends over the same uploads; the A-level site carries a full CIE 9702 topic area.
**Enumeration:** 1,080 uploads (yt-dlp flat playlist, 2026-11-10) — **100% net-new** vs all three
physics courses' existing external lanes (zero id overlap with P2B/P2C/P2D rows).
**Identity:** oEmbed 229/229 of the bound videos; `identityMethod: oembed` on every video entry.
**Evidence posture:** title-only, no high rows; tightened binding rule (title must name the spec's
distinctive content); board fit adjudicated per row (channel is AQA-oriented), `boardMismatch: true`
everywhere. Sewage filter: promo/merch/exam-news/paper-walkthrough/worksheet-answers/"RESULTS"/
Daily-Workout-answer videos excluded (35 shorts + 8 promo-pattern + 26 long paper/answer videos out).

## Draft → self-review (delegated, owner chat 2026-11-09 "approve and review yourself")

| Course | Mappings drafted | Approved | Full-row rejects | Spec trims | Specs shipped (this lane) | Course coverage after merge |
| --- | --- | --- | --- | --- | --- | --- |
| cie-a-level-physics-25 | 138 | 126 | 12 | 2 (4.2.2, 5.2.2) | 92/303 | **131/303** (was 66) |
| cie-igcse-physics-23 | 87 | 87 | 0 | 1 (1.4.3) | 68/294 | **76/294** (was 16) |
| igcse-physics-19 | 78 | 78 | 0 | 0 | 60/195 | **146/195** (was 142) |
| **Σ** | **303** | **291** | **12** | **3** | — | 459 union rows / 3 courses |

## Full-row rejects (every reject reasoned in `owner-review-verdicts.p2e.json`)

- `lw1OMstvsMI` 2.1.9 — "Monkey and Hunter": demonstration title, clause not named.
- `MVY--fncLok` 6.1.6 — "Young Modulus of Nylon": spec clause is a metal in wire form.
- `i3F-A3pq4tc` 6.1.6 / `u6HrAqM1F04` 10.1.5 — "Teaching Ideas" pieces: method not shown.
- `aaDfHS5JVsU` 6.1.5 — stress-strain curve interpretation beyond the definitions clause.
- `MVFGQ8QZAjE` 7.1.1 — jelly-baby wave machine demo, terms not named.
- `DuomJ2B1rao` 7.1.1+7.1.2 — "Introduction to Waves" generic survey (P2B pattern).
- `ZGWlTcx2Mc4` 8.2.1+8.2.2 — "5 Dollar Diffraction" home demo, keyword-adjacent.
- `cXwmBlKndCc` 10.2.5 — subset duplicate of the fuller parallel-derivation rows.
- `AJCUVcXq51o` 10.3.4 — "non-ohmic devices" wording ≠ thermistor/LDR-divider clause.
- `dRSE6fpW3iM` 11.2.3 — quark composition not worded in title.
- `KgWFFGSUVN0` 25.3.2 — IGCSE-level source cannot carry the A2 redshift-ratio clause.

Spec trims: `7x6SpYdkjC4` 4.2.2 (equilibrium clause; 4.1.2 kept) · `byRzUOhmvfo` 5.2.2 (mg∆h applied
not named; 5.1.2 kept) · `6aAo6H8BdxI` 1.4.3 (floating demo without density-data clause; 1.4.1 kept).

## Honest gaps after this lane (physics trio)

- **cie-a-level-physics-25 (131/303, 43%)**: gravitational fields (13), ideal gases/thermal (15–16,
  no Boyle/Charles/latent videos bindable), SHM depth (17), electric fields (18), magnetic force/AC
  (20.2–21), astrophysics beyond redshift (25.1/25.2). The channel's A2 offering is thin; capacitors,
  photoelectric, SUVAT, Young modulus and DC gaps from P2D are now closed.
- **cie-igcse-physics-23 (76/294, 26%)**: magnetism/electromagnetism (4.5), most of thermal particle
  detail, nuclear half-life handling, space physics beyond orbital speed/redshift.
- **igcse-physics-19 (146/195, 75%)**: Edexcel-specific items the AQA-oriented channel does not cover
  (thermistors, ultrasound, momentum practicals detail, astrophysics beyond orbital speed/redshift).

## Pipeline

`Videos/scripts/build-content-map-external.mjs` extended with a P2E lane list (same gates, per-lane
census asserts, `review.lanes` array for two-external-lane courses, `source.p2e` + `inputs.p2e`
provenance). Emitted `apps/hub/content/video-map/<course>.json` for the three courses (union rows:
179 / 103 / 177) + `registry.json`; `flags.json` left untouched (skip-if-current).
