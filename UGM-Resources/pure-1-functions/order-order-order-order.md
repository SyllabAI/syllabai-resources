---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/order-order
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/investigation
- level/introducing
resource_identity:
  ugm_id: order-order
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 7
  resource_type_label: Investigation
  level: Introducing
  ref: 5176
  old_site_id: F2_RT1_2
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
  spec_points:
  - code: 1.2.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Sketch transformed graphs for translations (-2,0)/(0,-4) and stretches x3 // x, 1/2 //
        y; write equations in terms of f. Investigation covering the full 1.2.5 list (pattern exemplar).
      rationale: 'Canonical UGM title: “Order! Order!”; cross-mapped primary pick of record (UGM-Enrichment
        perSpecPoint primaryPick, T-UGM-MODE1-2 (syllabai-resources))'
      validation_status: SUGGESTED
      primaryPick: true
    title: understand and use the transformations of the Including use of the terms 'translation', 'reflection'
      graph of y = f( x ) given by and 'stretch' in describing transformations. Questions y = f( x ) +
      a , y = f( x + a ) , may involve algebraic or trigonometric functions, or other graphs with given
      features. y = a f( x ) , y = f( ax ) and simple combinations of these.
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/order-order/images/original-fx.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/original-fx.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/fx-1.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/fx-2.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/fx-3.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/fx-4.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/original-fx.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/fx-12.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/fx-13.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/fx-14.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/fx-23.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/fx-24.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/order-order/images/fx-34.svg
  kind: figure
---

# Order! Order!

> Excerpt: Students are asked to think about and describe combinations of graph transformations with a view to seeing when the order matters and when it does not.

## Warm-up

Here is a graph of a function, \(f(x)\).

> [figure: Cubic shaped graph crossing the x-axis at -1 and touching it at 2, and crossing the y-axis at 4 — `https://undergroundmathematics.org/combining-functions/order-order/images/original-fx.svg`] (image not included in the text import; path of record).

For each of the following transformations, sketch the transformed graph and write its equation in terms of \(f\).

Translation by \(\begin{pmatrix}-2\\0\end{pmatrix}\)

Translation by \(\begin{pmatrix}0\\-4\end{pmatrix}\)

Stretch by factor \(3\) parallel to \(x\)

Stretch by factor \(\frac{1}{2}\) parallel to \(y\)

To get an idea of what a transformed graph looks like, identify a few key points on the graph and apply the transformations to those points. What would be the key points on our \(f(x)\) graph? You might find that some points are not so informative with certain transformations.

**Things to think about**

## Warm-up solution

Here is a graph of a function, \(f(x)\).

> [figure: Cubic shaped graph crossing the x-axis at -1 and touching it at 2, and crossing the y-axis at 4 — `https://undergroundmathematics.org/combining-functions/order-order/images/original-fx.svg`] (image not included in the text import; path of record).

For each of the following transformations, sketch the transformed graph and write its equation in terms of \(f\).

Translation by \(\begin{pmatrix}-2\\0\end{pmatrix}\)

This is a translation to the left by \(2\) units.

> [figure: The translated graph crosses the x-axis at -3, has its local maximum at (-2,4) and its local minimum at the origin — `https://undergroundmathematics.org/combining-functions/order-order/images/fx-1.svg`] (image not included in the text import; path of record).

Algebraically, when translating \(2\) units left we replace \(x\) with \(x+2\), so we can write \[y=f(x+2).\]

The graph is translated \(4\) units downwards.

> [figure: The translated graph has its local maximum at the origin and its local minimum at (2,-4) — `https://undergroundmathematics.org/combining-functions/order-order/images/fx-2.svg`] (image not included in the text import; path of record).

We can write this as

\[y=f(x)-4.\]

You can think of this as replacing \(y\) with \(y+4\), which is consistent with how we treated \(x\) in the first example.

The graph is made \(3\) times as wide.

> [figure: The stretched graph still has its maximum at (0,4) and its minimum is now at (6,0) — `https://undergroundmathematics.org/combining-functions/order-order/images/fx-3.svg`] (image not included in the text import; path of record).

We replace the \(x\) with \(\frac{x}{3}\), so we can write this as \[y=f\left(\frac{x}{3}\right).\]

The graph is made half as tall.

> [figure: The stretched graph still has its minimum where it touches the x-axis at 2 but now the maximum is at (0,2) — `https://undergroundmathematics.org/combining-functions/order-order/images/fx-4.svg`] (image not included in the text import; path of record).

We replace \(y\) with \(2y\) and write this as \[y=\frac{1}{2}\;f(x).\]

## Main problem

What happens if we apply more than one transformation to a graph?

Choose two of these transformations and apply them in turn starting with the function \(f(x)\). Sketch the resulting graph after you have applied one transformation and then the other. Does it matter which order you apply the two transformations?

Does the order matter for all pairs, some pairs or none of the pairs?

> [figure: Cubic shaped graph crossing the x-axis at -1 and touching it at 2, and crossing the y-axis at 4 — `https://undergroundmathematics.org/combining-functions/order-order/images/original-fx.svg`] (image not included in the text import; path of record).

Translation by \(\begin{pmatrix}-2\\0\end{pmatrix}\)

Translation by \(\begin{pmatrix}0\\-4\end{pmatrix}\)

Stretch by factor \(3\) parallel to \(x\)

Stretch by factor \(\frac{1}{2}\) parallel to \(y\)

Would your answer be different if we had chosen a different set of transformations? Or a different starting function?

## Solution

Transformations (1) and (2)

Applying (1) then (2) translates the graph \(2\) units to the left and then \(4\) units down. Applying (2) then (1) translates it down then left. The result is the same; the order does not matter.

> [figure: The transformed graph touches the x-axis at 2 and crosses at 4, and crosses the y-axis at -4 — `https://undergroundmathematics.org/combining-functions/order-order/images/fx-12.svg`] (image not included in the text import; path of record).

One of the key points on the graph is the local maximum at \((0,4)\). Applying the transformations in either order takes this point to \((-2,0)\) as shown dotted in the diagram.

Algebraically, we replace \(x\) with \(x+2\), and replace \(y\) with \(y+4\), giving us \[y+4=f(x+2) \quad\implies\quad y=f(x+2)-4.\]

Transformations (1) and (3)

Applying (1) then (3) translates the graph \(2\) units to the left and then stretches it horizontally. The local maximum at \((0,4)\) moves to \((-2,4)\) which is then stretched away from the \(y\)-axis to \((-6,4)\).

Applying (3) to the point \((0,4)\) does not move it as it is on the \(y\)-axis. Transformation (1) then moves it to \((-2,4)\). This time, the order has made a difference to where the local maximum ends up and we get two different graphs, as shown here in blue and green.

> [figure: The result of the transformation by (1) followed by (3) is a curve which crosses the x-axis, at -9 and touches it at the origin and has a local maximum at (-6,4); The result of transformation by (3) followed by (1) is a curve which crosses the x-axis at -5 and touches it at 4 and has a local maximum at (-2,4) — `https://undergroundmathematics.org/combining-functions/order-order/images/fx-13.svg`] (image not included in the text import; path of record).

What is it that makes the order matter this time whereas it didn’t matter for transformations (1) and (2)?

How are the two resulting graphs related? What is the transformation from one to the other?

The green and blue graphs are related by a horizontal translation through a distance of \(4\). This is the difference between a translation of \(2\), and a translation of \(2\) that is then scaled up by a factor of \(3\).

The order matters because both transformations are acting horizontally.

**The transformation**

Algebraically, transformation (1) replaces

\(x\)

with

\(x+2\)

while (3) replaces

\(x\)

with

\(\frac{x}{3}\)

. So the different orders look like this.

\[\begin{align*} y&=f(x) \quad\stackrel{(1)}{\longrightarrow}\quad y=f(x+2) \quad\stackrel{(3)}{\longrightarrow}\quad y=f\left(\frac{x}{3}+2\right) \\ y&=f(x) \quad\stackrel{(3)}{\longrightarrow}\quad y=f\left(\frac{x}{3}\right) \quad\stackrel{(1)}{\longrightarrow}\quad y=f\left(\frac{x+2}{3}\right) \end{align*}\]

Transformations (1) and (4)

> [figure: The transformed graph crosses the x-axis at -3 and touches it at the origin and has a local maximum at (-2,2) — `https://undergroundmathematics.org/combining-functions/order-order/images/fx-14.svg`] (image not included in the text import; path of record).

The order does not matter. Algebraically we have \(y=\frac{1}{2}\,f(x+2)\).

Transformations (2) and (3)

> [figure: The transformed graph touches the x-axis at the origin and crosses it at 9, and has a local minimum at (6,-4) — `https://undergroundmathematics.org/combining-functions/order-order/images/fx-23.svg`] (image not included in the text import; path of record).

The order does not matter. Algebraically we have \(y=f\left(\frac{x}{3}\right)-4\).

Transformations (2) and (4)

> [figure: The result of the transformation by (2) followed by (4) crosses the y-axis at -2 and has the local minimum at (2,-4); The result of transformation by (4) followed by (2) touches the x-axis at the origin and has the local minimum at (2,-2) — `https://undergroundmathematics.org/combining-functions/order-order/images/fx-24.svg`] (image not included in the text import; path of record).

The order does matter. Algebraically, transformation (2) replaces

\(y\)

with

\(y+4\)

while (4) replaces

\(y\)

with

\(2y\)

. So the different orders look like this.

\[\begin{align*} y&=f(x) \quad\stackrel{(2)}{\longrightarrow}\quad y+4=f(x) \quad\stackrel{(4)}{\longrightarrow}\quad 2y+4=f(x) \implies y=\frac{1}{2}\big(f(x)-4\big) \\ y&=f(x) \quad\stackrel{(4)}{\longrightarrow}\quad 2y=f(x) \quad\stackrel{(2)}{\longrightarrow}\quad 2(y+4)=f(x) \implies y=\frac{1}{2}\,f(x)-4 \end{align*}\]

As before, how are the two resulting graphs related?

Transformations (3) and (4)

> [figure: The transformed graph has the local maximum where it crosses the y axis at 2 and the local minimum where it touches the x axis at 6 — `https://undergroundmathematics.org/combining-functions/order-order/images/fx-34.svg`] (image not included in the text import; path of record).

The order does not matter. Algebraically we have \(y=\frac{1}{2}\,f\left(\frac{x}{3}\right)\).

Of our four transformations, (1) and (3) are in the \(x\) direction while (2) and (4) are in the \(y\) direction. The order matters whenever we combine a stretch and a translation in the same direction.

In each of the cases (1)(3) and (2)(4) above, the resulting graphs are related by a translation. Can you explain the magnitude of the translation in each case?

The function used in this example has the shape of a cubic. The same conclusions would be true of any other function, but notice that with simple functions such as \(f(x)=x^2\) you cannot distinguish visually between a horizontal and a vertical stretch.

**Conclusion**

How would a translation by \(\begin{pmatrix}3\\-2\end{pmatrix}\) behave when combined with other transformations?

What if we combined three of the original transformations? Would the order always matter?
