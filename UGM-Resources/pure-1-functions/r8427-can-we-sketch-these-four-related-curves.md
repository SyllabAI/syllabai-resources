---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r8427
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r8427
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8427
  old_site_id: Q2019
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
  exam_reference: UCLES 1988 Q['Q11'] [9205/2]
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagi1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagi2.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagii1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagii2.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagii3.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagi2.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagiii1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagiv1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagiv2.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagiv3.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagiv4.png
  kind: figure
---

# Can we sketch these four related curves?

## Question

Sketch, on separate diagrams, the curves \[\text{(i)}\ y=\frac{x-a}{x},\qquad \text{(ii)}\ y=\frac{x^2-a^2}{x^2},\] where \(a\) is a positive constant.

[The equations of any asymptotes should be stated, together with the coordinates of any intersections with the axes.]

Hence sketch the curves \[\text{(iii)}\ y = \left|\frac{x-a}{x}\right|,\qquad \text{(iv)}\ y^2 = \frac{x^2-a^2}{x^2}.\]

## Suggestion

When sketching curves, it is helpful to ask:

1. Where are the intersections with the axes?
2. What happens as \(x\) tends to \(\pm \infty\)? Are there horizontal asymptotes? Asymptotes at an angle?
3. What are the vertical asymptotes?
4. Are there any stationary points?
5. Is there any symmetry?

Can we write our equation for (i) as \(y=p+\frac{q}{x}\) for some \(p\) and \(q\)?

Can we view this as the combination of two transformations of a simpler curve?

How is our equation for (ii) similar to that for (i)? How is it different?

Will these functions look similar to the ones from the first part at all?

## Solution (i)+(ii)

Sketch, on separate diagrams, the curves \[\text{(i)}\ y=\frac{x-a}{x},\qquad \dots\] where \(a\) is a positive constant.

[The equations of any asymptotes should be stated, together with the coordinates of any intersections with the axes.]

We begin by rewriting the given function as

\[\begin{equation} y=1-\frac{a}{x}.\label{eq:1} \end{equation}\]

When sketching curves, a useful strategy in many cases is to see if the function can be written in terms of other functions whose graphs we already know.

In this case, we can start by considering the graph of the basic function \(\frac{1}{x}\). It has a vertical asymptote at \(x=0\) and a horizontal asymptote at \(y=0\).

We will now try to manipulate this curve until we obtain the graph of equation \(\eqref{eq:1}\). Multiplying the curve by \(-1\) is a reflection in the \(x\)-axis. This gives us the curve \(y=-\frac{1}{x}\), as shown below. We note that the equations of the asymptotes are the same in this case.

> [figure:  — `https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagi1.png`] (image not included in the text import; path of record).

Next we consider multiplication by \(a\). As \(a\) is a positive constant, this can be interpreted as a stretching in the \(y\)-direction by a factor of \(a\) and so only has the effect of changing the scale on the graph.

We now note that addition by a constant is equivalent to a shift of its graph in the \(y\)-direction. In the sketch below we see the graph of \(y=1-\frac{a}{x}\), as required. The asymptotes are also translated by \(1\) in the \(y\)-direction and so the equations of the new asymptotes are \(y=1\) and \(x=0\). We also note that the curve intersects the \(x\)-axis when \(x=a\), by substituting \(y=0\) into the equation.

> [figure:  — `https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagi2.png`] (image not included in the text import; path of record).

Sketch, on separate diagrams, the curves \[\dots,\qquad \text{(ii)}\ y=\frac{x^2-a^2}{x^2},\] where \(a\) is a positive constant.

[The equations of any asymptotes should be stated, together with the coordinates of any intersections with the axes.]

As with (i), we begin by rewriting the equation as

\[\begin{equation} y=1-\frac{a^2}{x^2}. \label{eq:2} \end{equation}\]

Similarly to before, we aim to sketch the graph of \(y=\frac{1}{x^2}\) and then use tranformations until we obtain the graph of equation \(\eqref{eq:2}\).

We know that the graph of \(y=\frac{1}{x^2}\) must be similar to that of \(y=\frac{1}{x}\), with smaller values increasing their distance from the \(x\)-axis and larger values decreasing their distance from the \(x\) axis. The \(y\) values are also positive and so any negative parts of the graph are reflected upwards in the \(x\)-axis.

> [figure:  — `https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagii1.png`] (image not included in the text import; path of record).

Multiplication by \(-a^2\) is a reflection in the \(x\)-axis followed by a stretch by a factor of \(a^2\) in the \(y\) direction.

> [figure:  — `https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagii2.png`] (image not included in the text import; path of record).

Finally, addition by \(1\) shifts the graph upwards by one unit. We also note that the curve intersects the \(x\)-axis at the points \(x=a\) and \(x=-a\), by substituting \(y=0\) into equation \(\eqref{eq:2}\). Similarly to before, our final asymptotes are also shifted upwards by one unit and so are \(y=1\) and \(x=0\).

> [figure:  — `https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagii3.png`] (image not included in the text import; path of record).

Is there a way to use the graph of \(y=\frac{x-a}{x}\) to sketch this curve directly?

## Solution (iii)+(iv)

Hence sketch the curves \[\text{(iii)}\ y = \left|\frac{x-a}{x}\right|,\qquad \dots\]

As we already have a sketch of the graph \(y=\frac{x-a}{x}\), we need only consider the effect that taking the absolute value has on the graph.

> [figure:  — `https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagi2.png`] (image not included in the text import; path of record).

Every point on the curve with a positive \(y\) co-ordinate is fixed and every point with a negative \(y\) co-ordinate is reflected in the \(x\)-axis. This gives us the following sketch.

> [figure:  — `https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagiii1.png`] (image not included in the text import; path of record).

Hence sketch the curves \[\dots,\qquad \text{(iv)}\ y^2 = \frac{x^2-a^2}{x^2}.\]

#### Approach 1

We start by rewriting our equation as

\[\begin{equation} y=\pm \sqrt{1-\frac{a^2}{x^2}}. \label{equation} \end{equation}\]

Firstly, we note that if \(-a<x<a\), then \(1-\frac{a^2}{x^2} <0\) and so \(\eqref{equation}\) has no solutions. This means that our curve only has points with \(x\ge a\) or \(x \le -a\). We will consider the sketch of \(y=1-\frac{a^2}{x^2}\), from (ii), in this range and aim to plot the square roots. This is, for each point \((x,y)\) on this curve, we want to include the points \((x,\pm \sqrt{y})\) in our sketch of \(\eqref{equation}\).

> [figure:  — `https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagiv1.png`] (image not included in the text import; path of record).

If \(y<1\), then the vertical distance decreases and, if \(y>1\), the vertical distance increases. Therefore, we get the following graph for the positive root \(y=+\sqrt{1-\frac{a^2}{x^2}}\).

> [figure:  — `https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagiv2.png`] (image not included in the text import; path of record).

To plot the other root \(y=-\sqrt{1-\frac{a^2}{x^2}}\), we can simply add the reflection in the \(x\)-axis.

We now need only consider the points \((\pm a,0)\) and the angles that the curves make at these points. Comparing to the graph of \(y=\sqrt{x}\), we would not expect the curve to be sharp at these points. Hence, we will include the information that the curve intersects the \(x\)-axis at right-angles in our final sketch.

> [figure:  — `https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagiv3.png`] (image not included in the text import; path of record).

Similarly to before, the equations of the asymptotes are \(y=\pm 1\) and the points of intersection are at \(x=\pm a\).

The full details as to why this argument works will be touched on at university-level, but there are a number of ways that we can convince ourselves of this result none-the-less. For example, would we expect these points to be sharp if we rewrote the curve in the form \(x=\pm\frac{a}{\sqrt{1-y^2}}\)? Alternatively, what would we expect if we used calculus to calculate the gradient of the curve at these points? What does this tell us?

#### Approach 2

We begin by rewriting our equation as

\[\begin{equation} y^2 + \left(\frac{a}{x}\right)^2 = 1. \label{eq:4} \end{equation}\]

As this looks similar to the equation for a circle, we will begin by considering the graph of the unit circle \(y^2+x^2=1\).

To get the graph of equation \(\eqref{eq:4}\), we want to swap the \(x\) for \(\frac{a}{x}\). This is equivalent to finding another point \(x'\) such that \(xx'=a\) (i.e. point \(x'\) for which the [geometric mean](https://undergroundmathematics.org/glossary/geometric-mean) of \(x\) and \(x'\) are on the lines \(x=\pm\sqrt{a}\)). This is equivalent to inversion in the lines \(x=\pm\sqrt{a}\) and so each half of the circle can be projected outwards in the \(x\)-direction, as shown.

> [figure:  — `https://undergroundmathematics.org/combining-functions/r8427/images/q2019diagiv4.png`] (image not included in the text import; path of record).
