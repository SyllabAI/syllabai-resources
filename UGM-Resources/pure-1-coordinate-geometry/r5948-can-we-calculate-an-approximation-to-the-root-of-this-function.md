---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r5948
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r5948
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5948
  old_site_id: None
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'chord through (a,f(a)) and (b,f(b)), its x-intercept — line-from-two-points construction riding numerical-methods context (recorded medium).'
      rationale: 'Canonical UGM title: “Can we calculate an approximation to the root of this function?”; exam provenance: UCLES 1978 Q16'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'chord through (a,f(a)) and (b,f(b)), its x-intercept — line-from-two-points construction riding numerical-methods context (recorded medium).'
      rationale: 'Canonical UGM title: “Can we calculate an approximation to the root of this function?”; exam provenance: UCLES 1978 Q16'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1978 Q16
task: T-UGM-IMPORT-3
---

# Can we calculate an approximation to the root of this function?

## Question

It is known that the equation

\(f(x) = 0\)

has only one real root in the interval

\(a < x < b\)

and that

\(f(a) < 0\)

,

\(f(b) > 0\)

. The two points

\(A\)

and

\(B\)

lie on the graph of

\(f(x)\)

and have coordinates

\((a,f(a))\)

and

\((b,f(b))\)

respectively. By finding where the line

\(AB\)

cuts the axis of

\(x\)

, show that

\[\begin{equation*} \frac{af(b) - bf(a)}{f(b) - f(a)} \end{equation*}\]

is an approximation to the root.

For the equation \(x^2 + x^\frac{1}{2} - 37 = 0\), find two consecutive integers between which a root of the equation lies.

Using the method given in the first part of the question, calculate an approximation to the root, giving three significant figures in your answer.

## Suggestion

How could we find where the line \(AB\) cuts the \(x\)-axis?

You may find the resource [In-betweens](https://undergroundmathematics.org/thinking-about-geometry/in-betweens) helpful here.

## Solution

A diagram is a good start.

The point where the line \(AB\) meets the \(x\)-axis is usually a better approximation to the root of \(f(x)\) between \(x = a\) and \(x = b\) than either \(x=a\) or \(x=b\).

**Approach 1: Find the equation of the line \(AB\)**

If a line goes through the points \((p,q)\) and \((r,s)\), its gradient is \(\dfrac{s-q}{r-p}\).

If \((x,y)\) is some point in the plane, then the gradient of the line through \((p,q)\) and \((x,y)\) is \(\frac{y-q}{x-p}\).

Then the point \((x,y)\) will lie on the line if and only if these two gradients are equal, so we can write the equation of the line as \[\frac{y-q}{x-p}=\frac{s-q}{r-p}.\]

Alternatively, we could have used the general formula \(y-y_1=m(x-x_1)\) to write it as \[y-q=\frac{s-q}{r-p}(x-p).\] These are, of course, the same equation.

In our case, therefore, the line between \((a,f(a))\) and \((b,f(b))\) has equation \[\frac{y-f(a)}{x-a}=\frac{f(b)-f(a)}{b-a}.\]

We find the \(x\)-intercept of this line by putting \(y = 0\), giving \[\frac{-f(a)}{x-a}=\frac{f(b)-f(a)}{b-a}.\]

If we now rearrange this to make \(x\) the subject, we first find \[x-a = -f(a)\frac{b-a}{f(b)-f(a)}.\] Adding \(a\) to both sides and putting everything over a common denominator, we find \[x = \frac{af(b) - bf(a)}{f(b) - f(a)},\] as required.

**Approach 2: Using similar triangles**

If we add a few lines to the above sketch, we find that we have some similar triangles. (This is one of the methods which was explored in [In-betweens](https://undergroundmathematics.org/thinking-about-geometry/in-betweens).)

We let \(c\) be the \(x\)-coordinate of the point where \(AB\) crosses the \(x\)-axis, and have indicated various lengths on the diagram. From the similar triangles (the red and blue ones), we find that \[\frac{c-a}{b-a}=\frac{-f(a)}{f(b)-f(a)}.\] Now multiplying both sides by \(b-a\) gives \[c-a=\frac{-(b-a)f(a)}{f(b)-f(a)}.\] Finally, adding \(a\) to both sides and simplifying gives \[c=\frac{af(b)-bf(a)}{f(b)-f(a)}\] as required.

As a first approximation to save us some work, we notice that \(37\approx 6^2\). So trying values of \(x\) near \(6\) seems to be a sensible thing to do.

When \(x=5\), \(x^2 + x^\frac{1}{2} - 37 \approx -9.8\) and when \(x=6\), \(x^2 + x^\frac{1}{2} - 37 \approx 1.4\). So a root lies between \(x=5\) and \(x=6\).

Looking at \(f(x)\), we see that \(f(0) < 0\), and that \(f(x)\) grows without bound as \(x\) increases.

So working upwards from \(x=0\) is guaranteed to lead to a pair of integers \(n\) and \(n+1\) such that \(f(n) < 0\) and \(f(n+1) \ge 0\).

With

\(f(x) = x^2 + x^\frac{1}{2} - 37 = 0\)

,

\(a = 5\)

and

\(b = 6\)

, we find (using a calculator) that

\[\begin{equation*} \frac{af(b) - bf(a)}{f(b) - f(a)} = 5.870736179\!\dotsc \end{equation*}\]

which, to three significant figures, is \(5.87\). This is an approximation to the root of \(f(x)\) between \(x = a = 5\) and \(x = b = 6\), as required.

It turns out that the true solution is \(5.880060910\!\dotsc\), so our approximation is quite an accurate one in this case.

We can repeatedly apply the above idea.

If we call our first approximation \(x_1\), then we can calculate the value of \(f(x_1)\). It turns out that \(f(x_1)<0\). Since \(f(6)>0\), we can repeat the process with \(x_1\) replacing \(a\) and \(b\) remaining as \(6\).

If we continue doing this, we will progressively home in on the root.

This approach to finding the root of a function is termed the *secant method*, so named because the line segment \(AB\) is called a secant to the curve, that is, a line segment joining two points on the curve.

It is also known as the *linear interpolation* method.
