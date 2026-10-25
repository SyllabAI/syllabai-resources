---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r8939
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r8939
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8939
  old_site_id: Q1077
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: normal to x = 5a sec theta, y = 3a tan theta parallel to y = x - parametric differentiation
        of the sec/tan parametrisation with the gradient condition (flips the lane-11 non-overlap row
        of record routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Can we find where the normal is parallel to $y=x$?'
      validation_status: SUGGESTED
    title: find and use the first derivative of a function e.g. which is defined parametrically or implicitly.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Can we find where the normal is parallel to $y=x$?

## Question

A curve has parametric equations \(x=5a\sec\theta,\,y=3a\tan\theta\), where \(-\frac{1}{2}\pi < \theta < \frac{1}{2}\pi\) and \(a\) is a positive constant. Find the coordinates of the point on the curve at which the normal is parallel to the line \(y=x\).

## Suggestion

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/chyP8dHj/width/700/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/chyP8dHj)

How can we find the derivative \(\dfrac{dy}{dx}\) for this curve?

We want the normal to have the same gradient as \(y=x\).

If we know the value of \(\sin\theta\), how can we find the corresponding value of \(\cos\theta\)?

## Solution

Differentiating with respect to

\(\theta\)

, we find that

\[\begin{align*} \frac{dx}{d\theta} &= 5a\sec\theta\tan\theta \\ \frac{dy}{d\theta} &= 3a\sec^2\theta . \end{align*}\]

Thus \[\frac{dy}{dx}=\frac{3a\sec^2\theta}{5a\sec\theta\tan\theta}=\frac{3}{5\sin\theta}.\]

The normal to the curve therefore has gradient \[-\frac{5}{3}\sin\theta.\]

The normal is parallel to \(y=x\) when \[-\frac{5}{3}\sin\theta=1\quad \Longrightarrow \quad \sin\theta=-\frac{3}{5}.\]

By sketching a graph of \(y=\sin\theta\), we can see that there’s a unique value of \(\theta\) in the range \(-\dfrac{\pi}{2}<\theta<\dfrac{\pi}{2}\) for which \(\sin\theta=-\dfrac{3}{5}\).

The blue line in the diagram shows that this corresponds to a positive value of \(\cos\theta\).

Hence, we get that \[\cos^2 \theta = 1 - \sin^2 \theta = 1 - \left(-\frac{3}{5}\right)^2 = \frac{16}{25} \quad \Longrightarrow \quad \cos \theta = \frac{4}{5}\] as \(\cos\theta\) is positive.

\(y=\sin\theta\) (red), \(y=\cos\theta\) (black) and the value of \(\theta\) for which the normal is parallel to \(y=x\) (blue)

Alternatively, using the sketch above, we can see that we are dealing with a \(3-4-5\) triangle, and so the value of cosine we need is \(\cos\theta=\dfrac{4}{5}\).

Thus our coordinates for this value of

\(\theta\)

are

\[\begin{align*} x &= 5a\sec\theta = \frac{5a}{\cos\theta} = \frac{5a\times 5}{4} = \frac{25a}{4}, \\ y &= 3a\tan\theta=3a \times \frac{\sin \theta}{\cos \theta} = 3a\times\left(-\frac{3}{5}\right)\times\left(\frac{5}{4}\right) = -\frac{9a}{4}. \end{align*}\]
