---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r7720
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r7720
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7720
  old_site_id: Q4022
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'line of gradient m through (1,2): intercepts give the triangle area, minimised over
        m — classic P1 optimisation'
      rationale: 'Canonical UGM title: "How small can this triangle be?"; exam provenance: UCLES O level
        Additional Mathematics 2, 1964, Q3'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'line of gradient m through (1,2): intercepts give the triangle area, minimised over
        m — classic P1 optimisation'
      rationale: 'Canonical UGM title: "How small can this triangle be?"; exam provenance: UCLES O level
        Additional Mathematics 2, 1964, Q3'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 2, 1964, Q3
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/uA3Jc3q4/width/400/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# How small can this triangle be?

## Question

Write down the equation of the line of gradient \(m\) through the point \((1, 2)\). Find, in terms of \(m\), the intercepts which this line makes on the two axes. A line is drawn through the point \((1, 2)\) to form with the axes a triangle in the first quadrant. Find the least possible area of the triangle.

## Suggestion

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/uA3Jc3q4/width/400/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/uA3Jc3q4)

Can you express the area of the triangle as a function of the gradient, \(m\)?

How can we find the minimum value of a function?

## Solution

We can write the equation as \[y-2=m(x-1)\] or \[y=mx+2-m.\]

The \(y\)-intercept is at \(y=2-m\).

The \(x\)-intercept is given by \(0 = mx + 2 - m\), which yields \(x = 1-\dfrac{2}{m}\).

If \(m = 0\), the line is the horizontal line \(y = 2\), so there’s no \(x\)-intercept.

A line is drawn through the point \((1, 2)\) to form with the axes a triangle in the positive quadrant. Find the least possible area of the triangle.

Note that to form a triangle in the first quadrant, \(m\) must be negative.

The area of the blue triangle is \[A=\frac{1}{2}(2 - m)\left(1-\frac{2}{m}\right) = \frac{1}{2}\left(-m + 4 - \frac{4}{m}\right).\]

So the least area of the triangle is given by the minimum of the function \(A(m) = 2-\dfrac{m}{2}-\dfrac{2}{m}\).

We can sketch this graph by adding the curves \(y=2\), \(y= -\dfrac{x}{2}\) and \(y = -\dfrac{2}{x}\).

For a triangle to be created, \(m\) must be negative, so we’re looking for the minimum that we can see on the graph.

### Approach 1 - Differentiation

We can find the minimum by differentiating \(A\). We have \[\dfrac{dA}{dm}= -\dfrac{1}{2}+\dfrac{2}{m^2}.\]

Therefore \(\dfrac{dA}{dm}=0\) when \(m=\pm 2\). Since \(m\) has to be negative, \(m = -2\).

To check if this is a minimum point consider the gradients either side of \(m=-2\).

| \(m\) | \(-2.1\) | \(-2\) | \(-1.9\) |
|---|---|---|---|
| \(\dfrac{dA}{dm}\) | \(-\dfrac{1}{2}+\dfrac{2}{2.1^2}<0\) | \(0\) | \(-\dfrac{1}{2}+\dfrac{2}{1.9^2}>0\) |

So the least possible area of the triangle is \[A(-2) = 2-\frac{-2}{2}-\frac{2}{-2} = 4.\]

As an alternative to using calculus, we could notice that the two terms \(\dfrac{m}{2}\) and \(\dfrac{2}{m}\) multiply to one and that we are looking for the maximum of their sum.

This is a situation that crops up surprisingly often in mathematics and has a simple solution. It turns out that the maximum of \(\dfrac{m}{2}+\dfrac{2}{m}\) occurs when the two terms are equal.

To see why this is, you might think about the symmetry or you might think about the graphs of \(xy=1\) and \(x+y=k\).

Using this fact leads to the solution \(m=-2\) as above.

The graph of \(A(m)\) also has a stationary point at \(m=+2\). What does this correspond to geometrically?

### Approach 2 - Two numbers multiplying to a constant If two negative numbers have a constant product, as $\dfrac{m}{2}$ and $\dfrac{2}{m}$ do (i.e. $1$), then their sum is maximised when they are equal.

Can you see why? Note we're being asked to minimise $2-\dfrac{m}{2}-\dfrac{2}{m}$, or in other words to maximise $\dfrac{m}{2}+\dfrac{2}{m}$ remembering that our $m$ and therefore this sum is negative. Imagine that we have two positive numbers that can vary. -- If their product is constant, when is their sum a minimum? -- If their sum is constant, when is their product a maximum? These two questions crop up surprisingly often in mathematics, and the answer to both questions is the same - when the two numbers are equal. Have a think about this: you might like to make sketches to help. What happens if we fix $j$ and let $k$ vary, or if we fix $k$ and let $j$ vary? What can we say about the coordinates of the points where the curves meet?

This is when $\dfrac{m}{2}=\dfrac{2}{m}$, which gives $m = \pm 2$, as before. We need $m$ to be negative, so $m = -2$. Thus using either approach the least possible area of the triangle is $$A(-2) = \frac{-(-2)^2 + 4\times(-2) - 4}{2\times(-2)} = \frac{-4 - 8 - 4}{-4} = 4.$$

It is interesting to note that in both approaches we get an option of $m=2$ which we discard because $m$ must be negative. We can easily see that when $m=2$ we are on the branch of the curve of $A$ against $m$ in the 4th quadrant at its maximum point. This local maximum is smaller than the local minimum when $m=-2$, it would be the area where a straight line through the point $(1, 2)$ made no triangle at all in any quadrant, which *might* be seen as a minimum area of $0$!
