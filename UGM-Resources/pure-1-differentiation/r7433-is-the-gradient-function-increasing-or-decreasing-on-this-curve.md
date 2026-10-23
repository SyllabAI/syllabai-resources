---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r7433
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r7433
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7433
  old_site_id: null
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
      evidence: sign table for dy/dx (+/-/0) and its monotonicity (I/D) at six marked points — increasing/decreasing
        behaviour and stationary structure read from a curve
      rationale: 'Canonical UGM title: "Is the gradient function increasing or decreasing on this curve?";
        exam provenance: UCLES O level Additional Mathematics 2, 1973, Q1'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: sign table for dy/dx (+/-/0) and its monotonicity (I/D) at six marked points — increasing/decreasing
        behaviour and stationary structure read from a curve
      rationale: 'Canonical UGM title: "Is the gradient function increasing or decreasing on this curve?";
        exam provenance: UCLES O level Additional Mathematics 2, 1973, Q1'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 2, 1973, Q1
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/vE3yFQQh/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Is the gradient function increasing or decreasing on this curve?

## Question

The figure shows part of a curve passing through \(6\) points \(A,B,C,D,E,F\).

Copy and fill in the following table showing, for each of the points, whether

1. \(\dfrac{dy}{dx}\) is positive (\(+\)), negative (\(-\)), or zero (\(0\)),

---

1. \(\dfrac{dy}{dx}\) is increasing (\(I\)), or decreasing (\(D\)), as \(x\) increases.

|  | \(A\) | \(B\) | \(C\) | \(D\) | \(E\) | \(F\) |
|---|---|---|---|---|---|---|
| \(\dfrac{dy}{dx}\) is \(+,-,\) or \(0\) |  |  |  |  |  |  |
| \(\dfrac{dy}{dx}\) is \(I\) or \(D\) |  |  |  |  |  |  |

Determine which of (a) and which of (b) apply at the point \(\left(3,3\tfrac{1}{3}\right)\) on the curve \(y=x+\dfrac{1}{x}\).

## Solution

The filled in table should look like this:

|  | \(A\) | \(B\) | \(C\) | \(D\) | \(E\) | \(F\) |
|---|---|---|---|---|---|---|
| \(\dfrac{dy}{dx}\) is \(+,-,\) or \(0\) | \(+\) | \(0\) | \(-\) | \(-\) | \(0\) | \(+\) |
| \(\dfrac{dy}{dx}\) is \(I\) or \(D\) | \(D\) | \(D\) | \(D\) | \(I\) | \(I\) | \(I\) |

1. To see whether \(\dfrac{dy}{dx}\) is positive, negative or zero, we can imagine the tangent to the curve at each point and think about its gradient.

---

1. If we imagine the tangent to the curve at a point and move the point along the curve from left to right, we can see that its gradient starts positive and decreases. At \(B\) it changes from positive to negative and is still decreasing. There is a point somewhere between \(C\) and \(D\) where the gradient stops decreasing and starts increasing.  We call this a point of inflection. It happens when the gradient function has a maximum or a minimum. We learn more about this at the next station.

This point is the one point on the curve where the tangent to the curve cuts the curve at its point of contact.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/vE3yFQQh/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/vE3yFQQh)

The derivative of \(y=x+\dfrac{1}{x}\) is \[\frac{dy}{dx}=1-\frac{1}{x^2} ,\] which is positive at \(x=3\).

There are many ways to find if \(\dfrac{dy}{dx}\) is increasing or decreasing, here are three ways you might determine it.

1. **Calculation.** We could evaluate \(\dfrac{dy}{dx}\) at values of \(x\) above and below \(3\) and compare them:        \(x=\)   \(2\)   \(3\)   \(4\)     \(\dfrac{dy}{dx}=\)   \(\dfrac{3}{4}\)   \(\dfrac{8}{9}\)   \(\dfrac{15}{16}\)    We can see that the value of \(\dfrac{dy}{dx}\) increases as \(x\) increases.

---

1. **Algebra.** We could rewrite \(\dfrac{dy}{dx}=\dfrac{x^2-1}{x^2}\). This makes it clear that for \(x\geq 1\) \(\dfrac{dy}{dx}>0\) and as \(x\) gets larger \(\dfrac{dy}{dx}\) gets closer and closer to \(1\), so \(y\) is increasing at \(x=3\).

---

1. **Graph sketching.** A sketch of the graph \(y=1-\dfrac{1}{x^2}\) shows that \(y\) is increasing at \(x=3\). And therefore the gradient of \(y=x+\dfrac{1}{x}\) is increasing.

3. **Stationary points.** We could find the stationary points by solving $\dfrac{dy}{dx}=0$. They are at $x^2=1$ i.e. $x= \pm 1$, so when $x=3$ we have passed any stationary points on the curve and thus the gradient will stay the same sign. Evaluating one other point would then be sufficient. So for instance finding $\dfrac{dy}{dx}=\dfrac{3}{4}$ at $x=2$ tells us it is increasing as $x$ increases.

Can you find any other ways to determine if it is increasing or decreasing?
