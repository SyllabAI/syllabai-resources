---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r6653
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r6653
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6653
  old_site_id: Q14
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 2011 Q['Q1']
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/r6653/images/q14graph1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r6653/images/q14graph2.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r6653/images/q14graph3.png
  kind: figure
---

# Can we solve this equation with a sum of square roots?

## Question

1. Sketch the curve \(y = \sqrt{1 - x} + \sqrt{3 + x}\). Use your sketch to show that only one real value of \(x\) satisfies \[\sqrt{1 - x} + \sqrt{3 + x} = x + 1,\] and give this value.
2. Determine graphically the number of real values of \(x\) that satisfy \[2\sqrt{1 - x} = \sqrt{3 + x} + \sqrt{3 - x}.\] Solve this equation.

## Suggestion

For what values of \(x\) is \(y\) defined?

Try evaluating the function \(y = f(x)\) for some integer values of \(x\). What does this suggest about the function?

Are there any stationary points? If so, where and of what type?

## Solution

First, we identify some key properties of the graph \(y = \sqrt{1 - x} + \sqrt{3 + x}\) so we can sketch it.

- The right-hand side is defined only for \(-3 \leq x \leq 1\), so the endpoints are at \((-3,2)\) and \((1,2)\).
- If we evaluate the function (let’s call it \(f\)) at a few points, we find that \[\begin{align*} f(-3) &= 2, \\ f(-2) &= 1 + \sqrt{3}, \\ f(-1) &= 2\sqrt{2}, \\ f(0) &= 1 + \sqrt{3}, \\ f(1) &= 2. \end{align*}\]  This suggests that the function is symmetrical about the line \(x = -1\). In fact, we can show this, since \[\sqrt{1 - x} + \sqrt{3 + x} = \sqrt{2 - (x+1)} + \sqrt{2 + (x+1)}.\] So our curve is the graph of \(y = g(x) = \sqrt{2 - x} + \sqrt{2 + x}\) shifted \(1\) to the left, and it’s easy to see that the graph of \(y = g(x)\) is symmetrical about the \(y\)-axis.

- Although this is not essential to sketch the curve, we can differentiate to find the stationary points. We have \[\frac{dy}{dx} = \frac{-1}{2\sqrt{1 - x}} + \frac{1}{2\sqrt{3 + x}}\] so to find the stationary points we find when this is zero. We have \[\sqrt{1 - x} = \sqrt{3 + x}\] \[\Longrightarrow 1 - x = 3 + x\] \[\Longrightarrow x = -1,\] and we can check that \(x = -1\) really does give derivative \(0\).

Clearly this is a maximum because the other points evaluated have values smaller than \(2\sqrt{2}\).

- We can also see that the gradient at the endpoints must be infinite, because when the expression for the derivative is evaluated at either of them, one of the fractions will be of the form \(\frac{1}{0}\).

This gives us enough information to sketch the curve.

> [figure: Graph of the curve described. It starts at x = minus 3, increases to a maximum at x = minus 1, then decreases until x = 1 where the graph stops. — `https://undergroundmathematics.org/combining-functions/r6653/images/q14graph1.png`] (image not included in the text import; path of record).

Now to solve the equation given, we also plot the graph of \(y = x + 1\) and find where they intersect.

> [figure: The same curve with the new line plotted. They touch at (1,2) and no other points. — `https://undergroundmathematics.org/combining-functions/r6653/images/q14graph2.png`] (image not included in the text import; path of record).

So we clearly see that \(x = 1\) is the only (real) solution.

---

Here we use a similar method, and sketch the graphs of the curves \(y = \sqrt{3 + x} + \sqrt{3 - x}\) and \(y = 2\sqrt{1 - x}\).

The first is essentially the same curve as in (i), but defined on the interval \(-3 \leq x \leq 3\), with its maximum at \((0,2\sqrt{3})\) and symmetry about the \(y\)-axis.

The second curve is similar to the graph of \(\sqrt{x}\), with a translation, reflection and enlargement applied to it:

1. Translation of one unit to the left: \(x \mapsto 1 + x\)
2. Reflection in the \(y\)-axis: \(x \mapsto - x\)
3. Enlargement by a scale factor of 2: \(f(x) \mapsto 2f(x)\)

We can also see that the graph passes through \((1,0)\) and \((0,2)\).

From this, we sketch the two graphs on the same axes.

> [figure: The two curves described. The first is as in the first diagram, and the second begins at x = 1 and increases as x decreases. — `https://undergroundmathematics.org/combining-functions/r6653/images/q14graph3.png`] (image not included in the text import; path of record).

These curves intersect only once, when \(x < 0\).

We use algebra to solve the equation:

\[\begin{align*} 2\sqrt{1 - x} &= \sqrt{3 + x} + \sqrt{3 - x} \\ \Longrightarrow 4(1 - x) &= 3 + x + 2\sqrt{3 + x}\sqrt{3 - x} + 3 - x \\ \iff 4 - 4x &= 6 + 2\sqrt{(3 + x)(3 - x)} \\ \iff 1 + 2x &= -\sqrt{9 - x^2} \\ \Longrightarrow 1 + 4x + 4x^2 &= 9 - x^2 \\ \iff 5x^2 + 4x - 8 &= 0. \end{align*}\]

We can solve this quadratic equation, to find that

\[\begin{align*} x &= \frac{-4 \pm \sqrt{16 + 4\times5\times8}}{10} \\ &= \frac{-4 \pm \sqrt{16\times11}}{10} \\ &= \frac{-4 \pm 4\sqrt{11}}{10} \\ &= \frac{-2}{5}(1 \pm \sqrt{11}). \end{align*}\]

Then one of these roots is positive and one is negative. However, only the negative root is a valid solution, as the sketch shows. So the solution of this equation is \[x = \frac{-2}{5}(1 + \sqrt{11}).\]
