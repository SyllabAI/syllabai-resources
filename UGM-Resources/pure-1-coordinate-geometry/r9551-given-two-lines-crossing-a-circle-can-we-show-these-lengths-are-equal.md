---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r9551
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r9551
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9551
  old_site_id: Q9
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
      evidence: 'Lines through circle points S, T, U, V on x^2+(y-c)^2=r^2; substitution gives quadratics in s and t; p+q=0 — substituting lines into the circle equation is 1.3.'
      rationale: 'Canonical UGM title: “Given two lines crossing a circle, can we show these lengths are equal?”; exam provenance: UCLES 2009 Q1'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 2009 Q1
task: T-UGM-IMPORT-3
---

# Given two lines crossing a circle, can we show these lengths are equal?

## Question

The points \(S\), \(T\), \(U\) and \(V\) have coordinates \((s,ms)\), \((t,mt)\), \((u,nu)\) and \((v,nv)\) respectively. The lines \(SV\) and \(UT\) meet the line \(y = 0\) at the points with coordinates \((p,0)\) and \((q,0)\), respectively. Show that \[p = \frac{(m - n)sv}{ms - nv},\] and write down a similar expression for \(q\).

Given that \(S\) and \(T\) lie on the circle \(x^2 + (y - c)^2 = r^2\), find a quadratic equation satisfied by \(s\) and by \(t\), and hence determine \(st\) and \(s + t\) in terms of \(m\), \(c\) and \(r\).

Given that \(S\), \(T\), \(U\) and \(V\) lie on the above circle, show that \(p + q = 0\).

## Suggestion

Could we draw a sketch to keep track of what is going on?

Could we work out the equations of the straight lines involved in this problem?

What are the coordinates of \(S\)?

If we have a quadratic equation whose roots are \(s\) and \(t\), how are \(st\) and \(s + t\) related to the coefficients of this equation?

## Solution

We begin by finding the equation of the line \(SV\).

Its gradient is \[M = \frac{ms-nv}{s-v},\] and as it passes through the point \((s, ms)\), the line has equation \[y - ms = \frac{ms - nv}{s - v}(x - s)\] (using the general form of the equation of a straight line of gradient \(M\) passing through \((x_1,y_1)\), namely \(y-y_1=M(x-x_1)\)).

This meets the line \(y = 0\) at the point \((p,0)\), so \(p\) satisfies \[-ms = \frac{ms - nv}{s - v}(p - s).\]

Rearranging gives the required result for

\(p\)

. We have

\[\begin{align*} && p - s &= \frac{ms(v-s)}{ms - nv},\quad \text{assuming $ms - nv \neq 0$}&&\quad\\ \Longrightarrow\quad&& p &= \frac{s(ms - nv) + ms(v-s)}{ms - nv}\\ \Longrightarrow\quad&& p &= \frac{(m-n)sv}{ms - nv}. \end{align*}\]

Our argument fails if \(s=v\), as then the line \(SV\) is vertical. But in this case, \(p = s = v\), which agrees with the given formula.

Relabelling \(p \mapsto q\), \(s \mapsto t\) and \(v \mapsto u\) gives the equivalent result for \(q\). We have \[q = \frac{(m - n)tu}{mt - nu}.\]

Since

\(S\)

and

\(T\)

lie on the circle,

\(s\)

and

\(t\)

are solutions of the equation (using

\(z\)

as the variable, so as not to confuse ourselves with the equation of the circle itself):

\[\begin{align*} z^2 + (mz - c)^2 = r^2\\ \iff\quad& (1 + m^2)z^2 - 2mcz + (c^2 - r^2) = 0\\ \iff\quad& z^2 - \frac{2mc}{1 + m^2}z + \frac{c^2 - r^2}{1 + m^2} = 0. \end{align*}\]

Note that we may divide by \(1 + m^2\) because it’s positive, and so we are certainly not dividing by \(0\).

If the roots of the quadratic equation \(z^2 + bz + c = 0\) are \(z = s\) and \(z = t\), then \(s + t = -b\) and \(st = c\).

You can check this for yourself by expanding \(x^2 + bx + c = (z - s)(z - t)\) and comparing coefficients.

Considering the sum and the product of the roots for our quadratic in \(z\), we discover \[st = \frac{c^2 - r^2}{1 + m^2}\] and \[s + t = \frac{2mc}{1 + m^2}.\]

If \(U\) and \(V\) lie on the circle, then by interchanging letters we have \[uv = \frac{c^2 - r^2}{1 + n^2}\] and \[u + v = \frac{2nc}{1 + n^2}.\]

Using our expressions for

\(p\)

and

\(q\)

from above, we now have

\[\begin{align*} p + q &= \frac{(m - n)sv}{ms - nv} + \frac{(m-n)tu}{mt - nu}\\ &= \frac{(m - n)}{(ms - nv)(mt - nu)}(stm(u + v) - nuv(s + t))\\ &= \frac{(m - n)}{(ms - nv)(mt - nu)}\left(m \frac{c^2 - r^2}{m^2 + 1} \frac{2cn}{n^2 + 1} - n \frac{c^2 - r^2}{n^2 + 1} \frac{2cm}{m^2 + 1} \right)\\ &= 0, \end{align*}\]

using the sum and product results from above.

It is possible to interpret this question with a diagram (try to match all the parts of this question with the picture below).

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/YeSE3TTD)

The circle \(x^2 + (y-c)^2 = r^2\) appears here in black. Both \(r\) and \(c\) can be varied. The two lines through the origin \(y = mx\) and \(y = nx\) are in green.
