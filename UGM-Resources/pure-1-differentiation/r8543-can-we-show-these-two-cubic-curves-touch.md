---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r8543
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r8543
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8543
  old_site_id: Q23
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
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: show the parametrised cubic touches y=x^3 — tangency via equal gradients across a parameter
        family
      rationale: 'Canonical UGM title: "Can we show these two cubic curves touch?"; exam provenance:
        UCLES STEP Mathematics I, 2007, Q8'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: show the parametrised cubic touches y=x^3 — tangency via equal gradients across a parameter
        family
      rationale: 'Canonical UGM title: "Can we show these two cubic curves touch?"; exam provenance:
        UCLES STEP Mathematics I, 2007, Q8'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES STEP Mathematics I, 2007, Q8
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/NCk55VUa/width/700/height/500/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Can we show these two cubic curves touch?

## Question

A curve is given by the equation

\[\begin{equation*} y = ax^3 - 6ax^2 + (12a + 12)x - (8a + 16), \label{eq:1}\tag{$*$} \end{equation*}\]

where

\(a\)

is a real number. Show that this curve touches the curve with equation

\[\begin{equation*} y = x^3 \label{eq:2}\tag{$*{*}$} \end{equation*}\]

at \((2,8)\). Determine the coordinates of any other point of intersection of the two curves.

1. Sketch on the same axes the curves \(\eqref{eq:1}\) and \(\eqref{eq:2}\) when \(a = 2\).

---

1. Sketch on the same axes the curves \(\eqref{eq:1}\) and \(\eqref{eq:2}\) when \(a = 1\).

---

1. Sketch on the same axes the curves \(\eqref{eq:1}\) and \(\eqref{eq:2}\) when \(a = -2\).

## Interactive graph

A curve is given by the equation

\[\begin{equation*} y = ax^3 - 6ax^2 + (12a + 12)x - (8a + 16), \label{eqi:1}\tag{$*$} \end{equation*}\]

where

\(a\)

is a real number. Show that this curve touches the curve with equation

\[\begin{equation*} y = x^3 \label{eqi:2}\tag{$*{*}$} \end{equation*}\]

at \((2,8)\).

You might like to use this applet to explore the behaviour of the curve \(\eqref{eqi:1}\) as \(a\) varies. The blue curve is \(y=x^3\) \(\eqref{eqi:2}\).

You can also zoom in or out if that helps to see the behaviour of the curves.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/NCk55VUa/width/700/height/500/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/NCk55VUa)

As \(a\) varies, you might notice the following.

- The curves always touch at \((2,8)\) as the question suggests.

- What happens to the red curve when \(a=0\)?

- Are there any values of \(a\) for which the curves do not intersect again?

## Solution

A curve is given by the equation

\[\begin{equation*} y = ax^3 - 6ax^2 + (12a + 12)x - (8a + 16), \label{eq:1repeat}\tag{$*$} \end{equation*}\]

where

\(a\)

is a real number. Show that this curve touches the curve with equation

\[\begin{equation*} y = x^3 \label{eq:2repeat}\tag{$*{*}$} \end{equation*}\]

at \((2,8)\). Determine the coordinates of any other point of intersection of the two curves.

Let \[f(x) = ax^3 - 6ax^2 + (12a + 12)x - (8a + 16)\] and \[g(x) = x^3.\]

To find the points of intersection, we set

\(f(x) = g(x)\)

to get

\[\begin{align*} & ax^3 - 6ax^2 + (12a + 12)x - (8a + 16) = x^3 \\ \iff & (a - 1)x^3 - 6ax^2 + (12a + 12)x - (8a + 16) = 0 \\ \iff & (x - 2)[(a - 1)x^2 - (4a + 2)x + (4a + 8)] = 0 \\ \iff & (x - 2)^2[(a - 1)x - (2a + 4)] = 0. \end{align*}\]

So the points of intersection have coordinates (2,8) and \[\left(\frac{2a+4}{a-1},\left[\frac{2a+4}{a-1}\right]^3\right).\]

The double root for \(x = 2\) means that we have a touching there; the two curves are tangent to each other at \((2,8)\).

Alternatively…

To show that the curves \(\eqref{eq:1repeat}\) and \(\eqref{eq:2repeat}\) *touch* at \((2,8)\), we need to show that both curves pass through \((2,8)\) and that the gradients of the curves are equal at this point.

Now \[f(2) = 8a - 24a + 2(12a + 12) - (8a + 16) = 8\] and \[g(2) = 8,\] so both curves pass through the point \((2,8)\).

Also \[f'(2) = 12a - 24a + (12a + 12) = 12\] and \[g'(2) = 12,\] so the curves have the same gradient at the point \((2,8)\).

Therefore the curves \(\eqref{eq:1repeat}\) and \(\eqref{eq:2repeat}\) touch at \((2,8)\).

1. Sketch on the same axes the curves \(\eqref{eq:1repeat}\) and \(\eqref{eq:2repeat}\) when \(a = 2\).

When \(a = 2\), \(\eqref{eq:1repeat}\) becomes \[y = 2x^3 - 12x^2 + 36x - 32.\] From above, we have that the two graphs intersect at \((8,512)\) and touch at \((2,8)\).

Now differentiating gives

\[\frac{dy}{dx} = 6x^2 - 24x + 36,\]

so stationary points occur when

\[\begin{align*} & 6x^2 - 24x + 36 = 0 \\ \iff & x^2 - 4x + 6 = 0 \\ \iff & (x - 2)^2 = -2. \end{align*}\]

This equation has no real solutions, so there are no stationary points.

Further, we can see from this equation that \(y'>0\) for all \(x\), and so \(y\) is an increasing function.

Since \(y<0\) when \(x=1\) but \(y>0\) when \(x=2\), we know that it has a root (which must be the only root since \(y\) is increasing) somewhere between \(1\) and \(2\).

We also know that \(\eqref{eq:1repeat}\) with \(a = 2\) intersects the \(y\) axis at \((0,-32)\).

So when \(a = 2\), the graphs must have the following shape.

1. Sketch on the same axes the curves \(\eqref{eq:1repeat}\) and \(\eqref{eq:2repeat}\) when \(a = 1\).

When \(a = 1\), \(\eqref{eq:1repeat}\) becomes \[y = x^3 - 6x^2 + 24x - 24.\] The two graphs touch at \((2,8)\) but do not intersect elsewhere because \(\dfrac{2a+4}{a-1}\) is undefined when \(a = 1\).

Differentiating gives

\[\frac{dy}{dx} = 3x^2 - 12x + 24,\]

so stationary points occur when

\[\begin{align*} & 3x^2 - 12x + 24 =0 \\ \iff & x^2 - 4x + 8 = 0 \\ \iff & (x - 2)^2 = -4. \end{align*}\]

This equation has no real solutions, so there are no stationary points.

Again, this means that \(y'>0\) for all \(x\), and so \(y\) is an increasing function.

Since \(y<0\) at \(x=1\) but \(y>0\) at \(x=2\), we know that the graph of \(y\) crosses the \(x\)-axis somewhere between \(x=1\) and \(x=2\), which should help our sketch.

We also know that \(\eqref{eq:1repeat}\) with \(a = 1\) intersects the \(y\) axis at \((0,-24)\).

So when \(a=1\), the graphs have the following shape.

1. Sketch on the same axes the curves \(\eqref{eq:1repeat}\) and \(\eqref{eq:2repeat}\) when \(a = -2\).

When \(a = -2\), \(\eqref{eq:1repeat}\) becomes \[y = -2x^3 + 12x^2 - 12x=-2x(x^2-6x+6).\] We can find that \(y\) has roots at \(x=0,3\pm\sqrt{3}\), or approximately \(x=0, 1.3,4.7\).

The two graphs intersect at \((0,0)\) and touch at \((2,8)\).

Differentiating gives

\[\frac{dy}{dx} = -6x^2 + 24x - 12,\]

so stationary points occur when

\[\begin{align*} & -6x^2 + 24x - 12 = 0 \\ \iff & x^2 - 4x + 2 = 0 \\ \iff & x = 2 \pm \sqrt{2}. \end{align*}\]

So there are stationary points at \(x \approx 3.4\) and \(x \approx 0.6\).

So when \(a=-2\), the graphs have the following shape.
