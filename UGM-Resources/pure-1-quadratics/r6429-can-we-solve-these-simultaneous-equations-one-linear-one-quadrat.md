---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6429
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6429
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6429
  old_site_id: Q3005
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Canonical linear+quadratic simultaneous system.
      rationale: 'Canonical UGM title: “Can we solve these simultaneous equations, one linear, one quadratic?”;
        exam provenance: UCLES 1983 Q5'
      validation_status: SUGGESTED
    title: solve by substitution a pair of simultaneous e.g. equations of which one is linear and one
      is 2 quadratic
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1983 Q5
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r6429/images/plot-labelled.png
  kind: figure
---

# Can we solve these simultaneous equations, one linear, one quadratic?

## Question

Solve the simultaneous equations

\[\begin{align*} 2x + 4y &= 9, \\ 4x^2 + 16y^2 &= 20x + 4y - 19. \end{align*}\]

## Suggestion

Which of our methods for solving simultaneous equations would be useful here?

Could we think about this problem geometrically by sketching a graph of the equations?

## Solution

We will solve the equations by substitution, rearranging the first (linear) equation and substituting it into the second (quadratic) equation.

We have two choices: we could either write \(2x\) in terms of \(y\) or write \(4y\) in terms of \(x\).

Looking at the second equation, we notice that the \(x\) terms (\(4x^2=(2x)^2\) and \(20x=10(2x)\)) can be easily written in terms of \(2x\), though the coefficients involved are somewhat large, especially if we do not happen to have a calculator handy.

On the other hand, the \(y\) terms (\(16y^2=(4y)^2\) and \(4y\)) are far more straightforward, so we will use this substitution.

We can rearrange the first equation to get \(4y = 9 - 2x\). Substituting this into the second equation, we obtain \[4x^2 + (9-2x)^2 = 20x + (9-2x) - 19.\] Expanding this gives \[4x^2 + (81 - 36x + 4x^2) = 18x - 10,\] which, by bringing everything over to the left-hand side, becomes \[8x^2 - 54x + 91 = 0.\]

We could either work to discover that this factorises as \[(4x-13)(2x-7)=0\] so that \(x=\frac{13}{4}\) or \(x=\frac{7}{2}\), or we could use the [quadratic formula](https://undergroundmathematics.org/glossary/quadratic-equation-solution) to reach the same conclusion.

When \(x=\frac{13}{4}\), \[y = \frac{9 - 2x}{4} = \frac{9 - \tfrac{13}{2}}{4} = \frac{5}{8},\] and when \(x = \tfrac{7}{2}\), \[y = \frac{9 - 2x}{4} = \frac{9 - 7}{4} = \frac{1}{2}.\]

So the two solutions are \[\left( \frac{13}{4}, \frac{5}{8} \right) \quad\text{and}\quad \left( \frac{7}{2}, \frac{1}{2} \right).\]

---

Another way of thinking about these equations is as a pair of curves in the \((x,y)\)-plane. The first equation, \[2x + 4y = 9,\] is that of a straight line. The second equation, \[4x^2 + 16y^2 = 20x + 4y - 19,\] can be rearranged into \[ \left( x - \frac{5}{2} \right)^2 + 4\left( y - \frac{1}{8} \right)^2 = \frac{29}{16}, \] which is an [ellipse](https://undergroundmathematics.org/glossary/ellipse) centred at \((\frac{5}{2},\frac{1}{8})\). In the sketch below, the lines \(y = \tfrac{1}{8}\) and \(x = \tfrac{5}{2}\) are shown in grey.

> [figure: A labelled plot containing the line and the ellipse — `https://undergroundmathematics.org/quadratics/r6429/images/plot-labelled.png`] (image not included in the text import; path of record).

The sketch shows why there are at most two (real) solutions: a straight line and an ellipse cannot intersect more than twice.

We cannot solve this problem accurately by just sketching the graph, but it tells us something about how many solutions there could be.
