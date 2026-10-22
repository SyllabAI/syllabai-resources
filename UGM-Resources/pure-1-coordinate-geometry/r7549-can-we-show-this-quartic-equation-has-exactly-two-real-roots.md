---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r7549
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r7549
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7549
  old_site_id: None
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'y=x^2 and the circle x^2+y^2-4x+2y-4=0 sketched together show the quartic has exactly two real roots — intersection-of-graphs as equation-roots verbatim; quarti'
      rationale: 'Canonical UGM title: “Can we show this quartic equation has exactly two real roots?”; exam provenance: UCLES 1980 Q3'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1980 Q3
task: T-UGM-IMPORT-3
---

# Can we show this quartic equation has exactly two real roots?

## Question

Sketch in the same diagram the graphs of \(y = x^2\) and \(x^2 + y^2 - 4x + 2y - 4 = 0\). Hence or otherwise show that the equation \(x^4 + 3x^2 - 4x - 4 = 0\) has two and only two real roots.

Find the positive root of the equation correct to one decimal place.

## Suggestion

What kind of a curve does the first equation give?

How about the second? Can we complete the square here to make the equation clearer?

## Solution

The graph of the equation

\(y = x^2\)

is a parabola, while the graph of the equation

\(x^2 + y^2 - 4x + 2y - 4 = 0\)

is a circle, since

\[\begin{align*} x^2 + y^2 - 4x + 2y - 4 = 0 &\iff \left( (x-2)^2 - 4 \right) + \left( (y+1)^2 - 1 \right) - 4 = 0 \\ &\iff (x-2)^2 + (y+1)^2 = 9. \end{align*}\]

That is, the centre of the circle is \((2,-1)\) and the radius is \(3\).

Sketch of the parabola \(y = x^2\) and the circle \(x^2 + y^2 - 4x + 2y - 4 = 0\).

Consider the simultaneous equations

\[\begin{align*} y &= x^2, \\ x^2 + y^2 - 4x + 2y - 4 &= 0. \end{align*}\]

As the diagram above shows, there are exactly two real solutions to this pair of equations.

If we substitute the first equation into the second, the second equation becomes

\[\begin{equation*} x^2 + (x^2)^2 - 4x + 2(x^2) - 4 = 0. \end{equation*}\]

That is,

\[\begin{equation*} x^4 + 3x^2 - 4x - 4 = 0. \end{equation*}\]

Thus \(x^4 + 3x^2 - 4x - 4 = 0\) has exactly two real roots.

From our diagram, this root appears to be around \(x = 1.4\).

With this in mind, we’ll let

\[\begin{equation*} f(x) = x^4 + 3x^2 - 4x - 4 \end{equation*}\]

and calculate \(f(x)\) for various values of \(x\) around \(x = 1.4\). By using a calculator, we have the following table.

| \(x\) | \(f(x)\) |
|---|---|
| \(1.3\) | \(-1.2739\) |
| \(1.4\) | \(0.1216\) |
| \(1.5\) | \(1.8125\) |

As there is a sign change and the function is continuous, the root we seek must fall between \(1.3\) and \(1.4\).

By using a calculator again, we see that \(f(1.35) = -0.610994\), and so the root therefore falls between \(1.35\) and \(1.4\).

Thus, to one decimal place, the root is equal to \(1.4\).

In fact, the root equals \(1.392030791\!\ldots\).

We could also have located the root, to one decimal place, by using trial and improvement.
