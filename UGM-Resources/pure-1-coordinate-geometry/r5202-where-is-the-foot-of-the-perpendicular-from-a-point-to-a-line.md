---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r5202
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r5202
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5202
  old_site_id: Q10
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: geometry-of-equations
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: geometry-of-equations
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'perpendicularity via gradients and line equations; STEP III depth is extension beyond P1 routine.'
      rationale: 'Canonical UGM title: “Where is the foot of the perpendicular from a point to a line?”; exam provenance: UCLES 2003 Q7'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'perpendicularity via gradients and line equations; STEP III depth is extension beyond P1 routine.'
      rationale: 'Canonical UGM title: “Where is the foot of the perpendicular from a point to a line?”; exam provenance: UCLES 2003 Q7'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 2003 Q7
task: T-UGM-IMPORT-3
---

# Where is the foot of the perpendicular from a point to a line?

## Question

In the \(x\)–\(y\) plane, the point \(A\) has coordinates \((a,0)\) and the point \(B\) has coordinates \((0,b)\), where \(a\) and \(b\) are positive. The point \(P\), which is distinct from \(A\) and \(B\), has coordinates \((s,t)\). \(X\) and \(Y\) are the [feet of the perpendiculars](https://undergroundmathematics.org/glossary/foot-of-a-perpendicular) from \(P\) to the \(x\)-axis and \(y\)-axis respectively, and \(N\) is the foot of the perpendicular from \(P\) to the line \(AB\). Show that the coordinates \((x,y)\) of \(N\) are given by \[x = \frac{ab^2 - a(bt - as)}{a^2 + b^2}, \quad y = \frac{a^2b + b(bt - as)}{a^2 + b^2}.\]

Show that, if \[\left(\frac{t - b}{s}\right)\left(\frac{t}{s - a}\right) = -1,\] then \(N\) lies on the line \(XY\).

Give a geometrical interpretation of this result.

## Interactive diagram

Use this applet to explore the behaviour as \(A\), \(B\) and \(P\) are moved.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/tA6xk6yg)

What can you say about the position of \(P\) when \(N\) is on \(XY\)?

You can show the circle that has \(AB\) as a diameter.

## Solution

Here’s a diagram of the situation.

You might also like to experiment with the situation in a more dynamic way using the [GeoGebra applet here](https://undergroundmathematics.org/geometry-of-equations/r5202/interactive).

The gradient of the line \(AB\) is \(\frac{-b}{a}\), so the line has equation \(y=-\frac{b}{a}(x-a)\), which rearranges to \(bx+ay=ab\) or \(\frac{x}{a}+\frac{y}{b}=1\), which has a nice symmetry to it.

As the line \(AB\) has gradient \(-\frac{b}{a}\), it follows that the line perpendicular line \(NP\) has gradient \(\frac{a}{b}\). So \(NP\), passing through \(P(s,t)\) has equation \(y-t = \frac{a}{b}(x - s)\), which we can rearrange to get \(ax-by=as-bt\).

Now we know that

\(AB\)

and

\(NP\)

intersect at

\(N\)

, so to find the coordinates of

\(N\)

we solve the simultaneous equations

\[\begin{align} &&bx+ay&=ab\label{eq:1}&&\quad\\ \text{and}\quad&&ax-by&=as-bt.\label{eq:2} \end{align}\]

Adding \(b\times\eqref{eq:1}\) to \(a\times\eqref{eq:2}\) gives \[(a^2+b^2)x=ab^2+a^2s-abt\] so \[x=\frac{ab^2+a^2s-abt}{a^2+b^2}=\frac{ab^2-a(bt-as)}{a^2+b^2}.\]

Similarly, subtracting \(b\times\eqref{eq:2}\) from \(a\times\eqref{eq:1}\) gives \[(a^2+b^2)y=a^2b-abs+b^2t\] so \[y=\frac{a^2b-abs+b^2t}{a^2+b^2}=\frac{a^2b+b(bt-as)}{a^2+b^2}\] as required.

The points \(X\) and \(Y\) have coordinates \((s,0)\) and \((0,t)\) respectively, so by the same argument as for \(AB\), we see that the equation of the line \(XY\) is \[tx+sy = st.\]

Now

\(N\)

lies on this line exactly when

\[\begin{align*} &t\frac{ab^2-a(bt-as)}{a^2+b^2} + s\frac{a^2b+b(bt-as)}{a^2+b^2}=st\\ \iff\quad& ab^2t-at(bt-as) + a^2bs + bs(bt-as) = st(a^2+b^2)\\ \iff\quad& ab^2t - abt^2 +a^2st + a^2bs + b^2st - abs^2 = a^2st + b^2st\\ \iff\quad& ab^2t - abt^2 + a^2bs - abs^2 = 0\\ \iff\quad& bt - t^2 + as - s^2 = 0\quad\text{as $ab$ is non-zero}\\ \iff\quad& t(b-t) + s(a-s) = 0. \end{align*}\]

Then assuming that \(s\) and \(a-s\) are non-zero, we can divide by them to see that \(N\) lies on this line exactly when \[\frac{t(b-t)}{s(a-s)}+1=0,\] which is equivalent to the condition we were asked to show (and in fact stronger, as we have shown that this is also a necessary condition).

A geometrical interpretation of this result is that \(\dfrac{t - b}{s}\) and \(\dfrac{t}{s - a}\) are the gradients of \(BP\) and \(AP\) respectively. So if \(BP\) and \(AP\) are perpendicular, then \(N\) lies on \(XY\).

And what does this mean? We know that the angle in a semi-circle is a right angle.

So \(N\) lies on \(XY\) exactly when \(P\) lies on the circle with \(AB\) as diameter.

You can explore this further by showing the circle in the [GeoGebra applet](https://undergroundmathematics.org/geometry-of-equations/r5202/interactive).
