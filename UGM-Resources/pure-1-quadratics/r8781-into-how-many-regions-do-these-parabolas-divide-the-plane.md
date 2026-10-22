---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r8781
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r8781
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8781
  old_site_id: Q77
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Regions bounded by parabolas; line-parabola positions + inequalities.
      rationale: 'Canonical UGM title: “Into how many regions do these parabolas divide the plane?”; exam
        provenance: Oxford (MAT) Specimen 2 Q1J'
      validation_status: SUGGESTED
    title: solve by substitution a pair of simultaneous e.g. equations of which one is linear and one
      is 2 quadratic
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Regions bounded by parabolas; line-parabola positions + inequalities.
      rationale: 'Canonical UGM title: “Into how many regions do these parabolas divide the plane?”; exam
        provenance: Oxford (MAT) Specimen 2 Q1J'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) Specimen 2 Q1J
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r8781/images/quadratics.png
  kind: figure
---

# Into how many regions do these parabolas divide the plane?

## Question

Into how many regions is the plane divided when the following three parabolas are drawn?

\[y = x^2\] \[y = x^2 - 2x\] \[y = x^2 + 2x +2.\]

1. \(4\),
2. \(5\),
3. \(6\),
4. \(7\).

## Suggestion

What do the parabolas look like? Do they intersect each other?

## Solution

One approach is to sketch the three parabolas. We could write their equations (by completing the square) as

\[y = x^2\] \[y = (x-1)^2 - 1\] \[y = (x+1)^2 + 1.\]

So we could describe all three as ‘vertex-down’ parabolas, with their vertices at \((0,0)\), \((1,-1)\) and \((-1,1)\) respectively.

To help us with our sketch, their \(y\)-intercepts are \(0\), \(0\) and \(2\) respectively.

To get from the first curve to the second, we translate \(y = x^2\) right \(1\) and down \(1\).

To get from the first curve to the third, we translate \(y = x^2\) left \(1\) and up \(1\).

So they are congruent copies of each other, with parallel axes of symmetry.

It should be intuitively clear from this that each pair of parabolas will meet in exactly one point.

> [figure: Graph of the three parabolae. They are all the same orientation, and each intersects each of the others once. There are 6 regions in between the curves, and one below all of them. — `https://undergroundmathematics.org/quadratics/r8781/images/quadratics.png`] (image not included in the text import; path of record).

From the graph, we can see that there are seven regions, so the answer is (d).

---

Alternatively, we can solve the equations two at a time. We have

\[y = x^2, \hspace{3mm} y = x^2 - 2x \hspace{3mm} \Longrightarrow \hspace{3mm} x = 0\]\[y = x^2, \hspace{3mm} y = x^2 + 2x +2 \hspace{3mm} \Longrightarrow \hspace{3mm} x = -1\]\[y = x^2 - 2x, \hspace{3mm} y = x^2 + 2x +2 \hspace{3mm} \Longrightarrow \hspace{3mm} x = -\frac{1}{2}\]

This confirms algebraically that each pair of parabolas intersects exactly once.

How many regions do we have? Let’s count them. The first parabola splits the plane into two regions.

Then the second parabola intersects the first parabola once, and so splits the two regions into two, leaving four regions.

Finally, the third parabola crosses each of the other two parabolas once, and so passes through three of the four regions, splitting each of these into two.

So there are now seven regions altogether.

Interestingly, the question of the number of regions formed will be unaffected if we add the same function to each of the three given functions.

For example, if we added \(x^3\) to each of them, each of the graphs would be distorted, but in exactly the same way (vertically speaking), and so the number of regions would be unchanged.

These straight lines are not parallel, and are not [concurrent](https://undergroundmathematics.org/glossary/concurrent), so we can sketch (any) three lines and observe that they divide the plane up into seven regions.

 So if we subtract

\(x^2\)

 from each of the equations, we are left with the three straight lines:

\[\begin{align*} y &= 0\\ y &= -2x\\ y &= 2x + 2. \end{align*}\]
