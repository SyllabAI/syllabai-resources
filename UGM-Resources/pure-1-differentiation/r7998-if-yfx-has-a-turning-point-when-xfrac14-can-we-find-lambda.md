---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r7998
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r7998
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7998
  old_site_id: Q91
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: turning point of f(x)=(x-2)^2-lambda(x+1)(x+2) at x=1/4 fixes lambda — derivative condition
        load-bearing; the equal-roots part is the 1.1 discriminant skill (recorded)
      rationale: 'Canonical UGM title: "If $y=f(x)$ has a turning point when $x=\frac{1}{4}$, can we
        find $\lambda$?"; exam provenance: UCLES A level Mathematics A 1 and Pure Mathematics 1, 1983,
        Q10'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: turning point of f(x)=(x-2)^2-lambda(x+1)(x+2) at x=1/4 fixes lambda — derivative condition
        load-bearing; the equal-roots part is the 1.1 discriminant skill (recorded)
      rationale: 'Canonical UGM title: "If $y=f(x)$ has a turning point when $x=\frac{1}{4}$, can we
        find $\lambda$?"; exam provenance: UCLES A level Mathematics A 1 and Pure Mathematics 1, 1983,
        Q10'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics A 1 and Pure Mathematics 1, 1983, Q10
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/ncg9qQXB/width/600/height/400/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# If $y=f(x)$ has a turning point when $x=\frac{1}{4}$, can we find $\lambda$?

## Question

It is given that \[f(x)=(x-2)^2-\lambda(x+1)(x+2).\]

1. Find the values of \(\lambda\) for which the equation \(f(x)=0\) has two equal roots.

---

1. Show that, when \(\lambda=2\), \(f(x)\) has a maximum value of \(25\).

---

1. Given that the curve \(y=f(x)\) has a turning point when \(x=\dfrac{1}{4}\), find the value of \(\lambda\) and sketch the curve for this value of \(\lambda\).

## Suggestion

Could we express \(f(x)\) in the form \(ax^2+bx+c\)?

What is the condition for an equation to have two equal roots?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/ncg9qQXB/width/600/height/400/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/ncg9qQXB)

Here the curve \(y=f(x)\) is in red, while the line \(x = \frac{1}{4}\) is in blue.

## Solution

By expanding

\(f(x)\)

we obtain

\[\begin{align*} f(x) &= x^2-4x+4-\lambda(x^2+3x+2) \\ &= (1-\lambda)x^2-(4+3\lambda)x+4-2\lambda. \end{align*}\]

For the equation

\(f(x)=0\)

to have two equal roots, the

discriminant

must be zero. So we want to solve

\[\begin{align*} 0 &= [-(4+3\lambda)]^2-4(1-\lambda)(4-2\lambda) \\ &= 16+24\lambda+9\lambda^2-4(4-6\lambda+2\lambda^2) \\ &= \lambda^2+48\lambda \\ &= \lambda(\lambda+48), \end{align*}\]

and so \(\lambda = 0\) or \(\lambda=-48\).

When \(\lambda=2\), we have \(f(x)=-x^2-10x\).

We find the maximum of \(f(x)\) by completing the square.

We can write \(f(x)=-(x+5)^2+25\), and since \(-(x+5)^2\) is strictly negative, we see that the maximum value of \(f(x)\) is \(25\), which occurs when \(x=-5\).

Alternatively we could find the derivative \(f'(x)\) and set this equal to zero to find the turning point.

Or we could find the roots of \(f(x)=0\), and use the symmetry of the parabola.

We have \[f'(x)=2(1-\lambda)x-(4+3\lambda).\]

We know that \(f'\left(\dfrac{1}{4}\right)=0\), since there is a turning point at \(x=\dfrac{1}{4}\).

So \[2(1-\lambda)\left(\frac{1}{4}\right)-4-3\lambda=0,\] and so \[1-\lambda-8-6\lambda=0,\] on multiplying the equation by \(2\). This simplifies to \(\lambda = -1\).

For this value of \(\lambda\), we have \(f(x)=2x^2-x+6\).

To sketch this graph we observe that the \(y\)-intercept is \(6\), and that \(x=\dfrac{1}{4}\) gives a minimum, since the coefficient of the \(x^2\) term is positive.

We calculate that \[f\left(\frac{1}{4}\right)=\frac{2}{16}-\frac{1}{4}+6=\frac{2-4+96}{16}=\frac{94}{16}=\frac{47}{8}.\]
