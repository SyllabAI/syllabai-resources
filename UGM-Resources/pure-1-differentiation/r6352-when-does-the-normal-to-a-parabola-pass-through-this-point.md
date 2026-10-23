---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r6352
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r6352
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6352
  old_site_id: Q158
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
  spec_points:
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: normal to y=x^2 at (a,a^2) through (0,1) — normal equation plus solve for a (two values)
      rationale: 'Canonical UGM title: "When does the normal to a parabola pass through this point?";
        exam provenance: Oxford University Mathematics Aptitude Test, 2009, Q4'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2009, Q4
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/FmXAYk4W/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does the normal to a parabola pass through this point?

## Question

As shown in the diagram below: \(C\) is the parabola with equation \(y=x^2\); \(P\) is the point \((0,1)\); \(Q\) is the point \((a,a^2)\) on \(C\); \(L\) is the normal to \(C\) which passes through \(Q\).

1. Find the equation of \(L\).

---

1. For what values of \(a\) does \(L\) pass through \(P\)?

---

1. Determine \(\big |QP\big |^2\) as a function of \(a\), where \(\big |QP\big |\) denotes the distance from \(P\) to \(Q\).

---

1. Find a point \(R\), in the \(xy\)-plane but not on \(C\), such that \(\big |RQ\big |\) is smallest for a unique value of \(a\). Briefly justify your answer.

## Interactive graph

As shown in the diagram below: \(C\) is the parabola with equation \(y=x^2\); \(P\) is the point \((0,1)\); \(Q\) is the point \((a,a^2)\) on \(C\); \(L\) is the normal to \(C\) which passes through \(Q\).

1. For what values of \(a\) does \(L\) pass through \(P\)?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/FmXAYk4W/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/FmXAYk4W)

## Solution

Firstly we need to find the gradient of \(C\) at \(Q\). To do this we differentiate \(y=x^2\) to get \[\frac{dy}{dx}=2x,\] and so at \(Q\) the gradient of \(C\) is \(2a\).

Now we use the fact that (gradient of normal) \(\times\) (gradient of tangent) \(= -1\), so the gradient of \(L\) is \(-\dfrac{1}{2a}\).

BUT beware! This causes trouble when \(a=0\), so we’ll have to consider this case separately.

Now \(L\) is a straight line of the form \(y=mx+c\), where \(m\) is the gradient and \(c\) is a constant.

So we substitute in \(y=a^2\), \(x=a\) and \(m=-\dfrac{1}{2a}\) to find that \(c=a^2 + \dfrac{1}{2}\), and the equation of \(L\) is \[y=-\frac{1}{2a} x + \frac{1}{2} + a^2, \quad\quad (a \neq 0),\] and when \(a=0\), the coordinates of \(Q\) are \((0,0)\) and the gradient at \(Q\) is \(0\), so the equation of the normal \(L\) is \[x=0.\]

First we should notice that \(a=0\) is a solution, as the line \(x=0\) passes through \(P\).

Then we substitute the coordinates of \(P\) into the equation for \(L\) (\(a \neq 0\)) to find the other possible values for \(a\).

So \[1=-\frac{1}{2a}(0) + \frac{1}{2} + a^2,\] which we can rearrange to get \[a^2=\frac{1}{2},\] and so our solutions are \[a=\pm \frac{1}{\sqrt{2}}, 0.\]

We can use Pythagoras here, giving

\[\big |QP\big |^2 = (a^2-1)^2 + (a-0)^2 = a^4-2a^2 +1 +a^2 = a^4 - a^2 +1.\]

Note that \(\dfrac{d}{da}\big |QP\big |^2 = 4a^3-2a = 2a(2a^2-1) = 0\) when \(a=\pm \dfrac{1}{\sqrt{2}}, 0\).

Thus the points on the parabola we’ve identified where \(L\) goes through \(P\) are stationary points for \(\big |QP\big |^2\), and thus for \(\big |QP\big |\).

There are lots of possible answers!

Perhaps the simplest example is a point of the form \((0,-b)\) for some positive \(b\), since it’s easy to see that the unique point on \(C\) which it is closest to is the origin.

Any point \(R\) on \(L\) and ‘outside’ the parabola will count, since \(Q\) will be the unique point closest to \(R\) (because the parabola’s gradient is always increasing).

But as \(Q\) moves around the parabola, any point ‘outside’ \(C\) will be on some normal through \(Q\), and so will be a possible \(R\).

In fact, the only points not closest to a unique point on \(C\) (and which are not on \(C\) itself) are the points on the positive \(y\)-axis.
