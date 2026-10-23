---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r6067
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r6067
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6067
  old_site_id: Q107
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2007, Q3
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/Q76Rn4yH/width/600/height/300/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Can we find the area under a parabola?

## Question

Let \[I(c)=\int_0^1 ((x-c)^2 +c^2)dx\] where \(c\) is a real number.

1. Sketch \(y=(x-1)^2+1\) for the values \(-1\le x\le 3\) and show on your graph the area represented by the integral \(I(1)\).

---

1. Without explicitly calculating \(I(c)\), explain why \(I(c) \ge 0\) for any value of \(c\).

---

1. Calculate \(I(c)\).

---

1. What is the minimum value of \(I(c)\) (as \(c\) varies)?

---

1. What is the maximum value of \(I(\sin \theta)\) as \(\theta\) varies?

## Suggestion

Let \[I(c)=\int_0^1 ((x-c)^2 +c^2)\:dx\] where \(c\) is a real number.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/Q76Rn4yH/width/600/height/300/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/Q76Rn4yH)

The curve here is \(y = (x-c)^2 + c^2\), and the white area is \(I(c)\). The size of the white area is given by the height of the red bar at the right.

What is always true about \((x-c)^2\) and \(c^2\)?

Can we complete the square here?

Notice we’re asked for the MAXIMUM value here…

## Solution

We have \(y=(x-1)^2+1\) so since \((x-1)^2 \ge 0\), with equality if and only if \(x=1\), the minimum value of \(y\) is \(1\), which occurs when \(x=1\).

Rewriting as \(y=x^2-2x+2\), we see that the \(y\)-intercept is at \(y=2\). This gives us enough information to sketch the graph.

Here is the area represented by the integral.

The integrand \((x-c)^2+c^2\) is greater than or equal to zero for any real \(c\) since \((x-c)^2\) and \(c^2\) are both squares of real numbers and so are both greater than or equal to zero. So we must have the integral of their sum greater than or equal to zero.

Or we could say that \(y=(x-c)^2+c^2\) is a parabola pointing downwards with vertex \((c, c^2)\), which is above the \(x\)-axis, and so the integral is positive.

We have

\[\begin{align*} I(c) &= \int_0^1 ((x-c)^2+c^2)dx\\ &=\left[ \frac{(x-c)^3}{3} +c^2x \right]_0^1\\ &=\frac{(1-c)^3}{3} + c^2 + \frac{c^3}{3}\\ &=2c^2-c+\frac{1}{3}. \end{align*}\]

Using the expression for

\(I(c)\)

we calculated above, and completing the square, we have

\[\begin{align*} I(c) &= 2c^2-c+\frac{1}{3}\\ &= 2\left(c-\frac{1}{4}\right)^2 - \frac{1}{8} + \frac{1}{3}\\ &= 2\left(c-\frac{1}{4}\right)^2 + \frac{5}{24}. \end{align*}\]

So the minimum value that \(I(c)\) can take is \(5/24\). (This occurs when \(c=1/4\).)

Note that from our work above, the MINIMUM value of \(I(\sin\theta)\) happens when \(\theta = \arcsin (0.25)\).

Now \(c=\sin \theta\) varies between between \(-1\) and \(1\), so we need to find the maximum value of \(I\) over this range.

We worked out earlier that the overall minimum of \(I\) occurs at \(c=1/4\), and since \(I\) is quadratic, it is symmetric about this point, and increasing for larger and smaller values of \(c\).

So the maximum value of \(I(c)\) over the range \(-1 \le c \le 1\) occurs at \(c=-1\), the furthest point from \(x=1/4\) in the range.

So the maximum value of \(I(\sin \theta)\) is \(I(-1)=10/3\).
