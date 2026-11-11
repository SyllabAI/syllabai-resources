# Review file — P4 scale pass (external lanes, delegated self-review)

Recorded 2026-11-11. Owner chat 2026-11-09: *"For now, approve and review yourself"* — delegated self-review standard unchanged since P2B: medium kept when the title names the spec's distinctive content; low kept only for genuine inline partial support; reject on keyword-adjacency, wrong-branch binds, or sewage. Cross-subject (mechanics) rows were held to a higher bar. Applied by `p4_apply_review.py` (mirrors `apply_self_review.py`).

## Verdict summary (8 lanes)

| course | rows kept | spec-level rejects | full-row drops |
| --- | --- | --- | --- |
| cie-igcse-maths-25-extended | 118 | 4 | — |
| cie-igcse-further-maths-additional-maths-25 | 3 | 5 | — |
| igcse-maths-b-16 | 107 | 1 | — |
| igcse-further-maths-19 | 31 | 3 | — |
| cie-a-level-maths-20-mechanics | 65 | 0 | — |
| cie-as-maths-20-mechanics | 65 | 0 | — |
| ial-maths-20-mechanics-1 | 43 | 2 | — |
| ial-maths-20-mechanics-2 | 41 | 0 | — |

## Reject ledger

### cie-igcse-maths-25-extended (4)

- `3kE_Q-JdlO4` → `E2.5.6` — 'Factorising Quadratics - Part 1 - (When the x² Coefficient is 1)' names the factorisation technique that is E2.2.4's own spec; E2.5.6's distinctive frame is 'Solve quadratic equations by factorisation, completing the square and by use of the quadratic formula' — no solving, completing the square or formula is title-evidenced. Ride-along on the E2.2.4 binding; rejected at medium.
- `nfLb8MPO99U` → `E2.5.6` — 'Factorising Quadratics - Part 2 - (When the x² Coefficient is More Than 1)' same pattern: title names factorising expressions (E2.2.4), not the solve-quadratic-equations frame of E2.5.6. Ride-along; rejected at medium.
- `b9ODSx3RJAE` → `E2.6.4` — 'Solving Inequalities by Plotting them on a Graph' names plotting inequalities on a graph, which is E2.6.3's exact topic; E2.6.4's distinctive task is the reverse direction — 'List inequalities that define a given region' (linear programming) — not title-evidenced. Ride-along on the E2.6.3 binding; rejected at medium.
- `8-4KQw8unfY` → `E4.4.2` — 'Similar Shapes' names the similarity domain (E4.4.1's lengths frame and E4.4.3's problem-solving survive), but E4.4.2's distinctive frame is 'relationships between lengths and areas ... surface areas and volumes of similar solids' (k/k²/k³ scale factors) — the evidence itself marks the area/volume relationships 'only supporting', i.e. not title-evidenced. Same pattern as the owner's 4.16-style identity rejects.

### cie-igcse-further-maths-additional-maths-25 (5)

- `u-YNzmlZWeg` → `2.5.1` — 'Solving Algebraic Inequalities with 1 Inequality Sign' is the GCSE linear-inequality lesson; spec 2.5 is 'Find the solution set for quadratic inequalities either graphically or algebraically' (2.5.1 '–3 < x < 4' is an example solution-set form). Same word 'inequalities', different topic (linear vs quadratic); the row's evidence even describes 'two inequality signs', mismatching this video. Keyword-adjacent; rejected at low.
- `u-YNzmlZWeg` → `2.5.2` — Same video: 'x < 1 or x > 6' is the solution-set example shape of a quadratic inequality, not the topic of a single-sign linear-inequality lesson; quadratic-inequality work is not title-evidenced. Keyword-adjacent; rejected at low.
- `L_AfY1Bqosk` → `2.5.1` — 'Solving Algebraic Inequalities with 2 Inequality Signs' teaches compound linear inequalities (e.g. 1 < 2x+1 < 7); the resemblance to 2.5.1's '–3 < x < 4' example form is surface-only — the spec's distinctive content is quadratic inequalities solved graphically or algebraically. Keyword-adjacent; rejected at low.
- `L_AfY1Bqosk` → `2.5.2` — Same video: compound-linear double inequalities are not the 'x < 1 or x > 6' quadratic solution-set topic of 2.5.2; no quadratic inequality work is title-evidenced. Keyword-adjacent; rejected at low.
- `Ry5-WEiTUs4` → `13.3.2` — 'GCSE Physics - Resolving Vectors & Scale Drawing | How to Find Resultant Forces' names force resultants and scale drawing; 13.3.2 is 'solving problems using vector geometry, with a diagram given in more complex cases' (equating like vectors, unknown scalars) — vector geometry is not named and the evidence itself concedes the video is physics-branded. Keyword-adjacent on 'vectors', bound to the wrong sub-clause of 13.3; rejected at low.

### igcse-maths-b-16 (1)

- `8-4KQw8unfY` → `6H` — 'Similar Shapes' names the similarity domain (6G's 'Similarity: areas and volumes of similar figures' survives on that head topic), but 6H's distinctive frame is 'Prove the similarity of two triangles' — proof work and the SSS/SAS/ASA/RHS-style conditions are not title-evidenced, and the evidence itself concedes proof is 'only supporting'. Ride-along on the 6G binding; rejected at medium.

### igcse-further-maths-19 (3)

- `871OBfK5o2M` → `5B` — 'Types of Number Sequences - Arithmetic vs Geometric' names sequence-type recognition; 5B is 'Arithmetic and geometric series' — nth-term and sum-of-terms formulae — and the evidence itself concedes 'series sums not named'. Same 'arithmetic/geometric' words, different topic (sequence classification vs series summation); keyword-adjacent, rejected at low. (The same title is correctly kept in the additional-maths lane against 12.3.1, whose distinctive content IS progression recognition.)
- `Wcv0f5PpTv0` → `10A` — 'Area of a Sector and Length of an Arc of a Circle (Circles Part 3)' is the degree-measure GCSE treatment; 10A's distinctive content is 'Radian measure, including use for arc length and area of sector' — the radian clause is the head of this spec point and the evidence concedes 'radian measure not named'. Degree-based arc/sector work is not title-evidenced for a radian-measure spec; rejected at low.
- `CnHgqfBSgco` → `10C` — 'Pythagoras' Theorem And How To Use It' is the basic right-triangle theorem lesson; 10C is 'Applications to simple problems in two or three dimensions (including angles between a line and a plane and between two planes)' — the evidence concedes the 3D plane-angle clause is not named and offers only generic 2D use. Title names a tool, not the spec's applied-problems frame; keyword-adjacent, rejected at low.

### ial-maths-20-mechanics-1 (2)

- `M_0FRIX8wIM` → `2.2` — GCSE 'Speed' is keyword-adjacent only: 2.2 is 'Application of vectors to displacements, velocities, accelerations and forces in a plane' — speed is not among the spec's listed quantities (it is the scalar side of 2.1, to which this video is not bound) and no vectors/in-a-plane mathematical framing is title-evidenced
- `xH4w97eUBgw` → `2.2` — GCSE 'Speed' is keyword-adjacent only: 2.2 is 'Application of vectors to displacements, velocities, accelerations and forces in a plane' — speed is not among the spec's listed quantities (it is the scalar side of 2.1, to which this video is not bound) and no vectors/in-a-plane mathematical framing is title-evidenced

## Inheritance lane (35 courses)

Not drafted per-course; derivation spot-check instead (12 pairs, six lane families). Finding: three degenerate 1.0-containment matches on trivially short spec titles ('Calculate with money.', 'E = Q this equation', 'r = BQ a magnetic field'), one of which carried a parent row and would have emitted a wrong row. Fix: ≥3-informative-token guard in `build-p4-inheritance.py`; map regenerated; all three excluded; re-verified. Verdicts: `drafts/_p4/owner-review-verdicts.p4-inherit.json` (rejects: none — the fix is structural).

Applied 2026-11-11T14:52:28Z.
