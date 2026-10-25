---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r5237
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r5237
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5237
  old_site_id: Q46
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
      evidence: normal to the ellipse x^2/a^2 + y^2/b^2 = 1 at (a cos theta, b sin theta) proved as ax/cos
        theta - by/sin theta = a^2 - b^2 - parametric differentiation with the eccentricity consequence
      rationale: 'Canonical UGM title: What can we say if a normal to an ellipse passes through this point?'
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

# What can we say if a normal to an ellipse passes through this point?

## Question

Prove that the equation of the normal to the ellipse \(x^2/a^2 + y^2/b^2=1\) at the point \(P\,(a\cos\theta,b\sin\theta)\) is \[\frac{ax}{\cos \theta} - \frac{by}{\sin \theta} = a^2-b^2.\]

If there is a value of \(\theta\) between \(0\) and \(\pi/2\) such that the normal at \(P\) passes through one end of the minor axis, show that the eccentricity of the ellipse must be greater than \(1/\sqrt{2}\).

## Suggestion

Prove that the equation of the normal to the ellipse \(x^2/a^2+y^2/b^2=1\) at the point \(P\,(a\cos\theta,b\sin\theta)\) is \[\frac{ax}{\cos \theta} - \frac{by}{\sin \theta} = a^2-b^2.\]

If \(x = f(t), y = g(t)\), what is \(\dfrac{dy}{dx}\) in terms of \(t\)?

Or could we use [implicit differentiation](https://undergroundmathematics.org/glossary/implicit-differentiation)?

You might use this applet to explore the problem.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/ew26SakK/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/ew26SakK)

What is the eccentricity of an ellipse?

The eccentricity, \(e\), is a measure of how “squashed” the ellipse is. It can be defined in terms of the major and minor axes. \[e = \sqrt{1-\dfrac{b^2}{a^2}}\]

## Solution

Prove that the equation of the normal to the ellipse \(x^2/a^2+y^2/b^2=1\) at the point \(P\,(a\cos\theta,b\sin\theta)\) is \[\frac{ax}{\cos \theta} - \frac{by}{\sin \theta} = a^2-b^2.\]

Implicitly differentiating

the equation of the ellipse with respect to

\(x\)

, we find

\[\frac{2x}{a^2} + \frac{2y}{b^2} \frac{dy}{dx} = 0\]

and therefore

\[\begin{align*} \frac{dy}{dx} &= - \frac{b^2x}{a^2y} \\ &= - \frac{b^2 a \cos \theta}{a^2 b \sin \theta} \\ &= - \frac{b \cos \theta}{a \sin \theta}. \end{align*}\]

Alternatively, we could say \(x=a\cos\theta, y=b\sin\theta\) which gives on differentiating \(\dfrac{dx}{d\theta}=-a\sin \theta, \dfrac{dy}{d\theta}=b\cos \theta\).

Now dividing these gives us \[\frac{dy}{dx} = \frac{dy/d\theta}{dx/d\theta}=-\frac{b\cos\theta}{a\sin\theta}.\]

Since the normal is perpendicular to the tangent, it has slope \[m = -\frac{1}{dy/dx} = \frac{a \sin \theta}{b \cos \theta}.\]

Hence the equation of the line is \[y - b\sin\theta = \frac{a \sin \theta}{b \cos \theta}\left(x - a \cos \theta\right)\] which we can rearrange to obtain \[a^2 - b^2 = \frac{ax}{\cos \theta} - \frac{by}{\sin\theta}\] as required.

The minor axis is the shortest diameter of the ellipse (a diameter of the ellipse is a chord that passes through the centre).

The ends have coordinates \((0,\pm b)\) (assuming that \(a \geq b>0\), which we can say without loss of generality).

If we know there is a value of \(\theta\) between \(0\) and \(\pi/2\) such that the normal at \(P\) passes through one end of the minor axis, then from the diagram, this normal must pass through \((0, -b)\).

Substituting \((0,-b)\) into the equation of the normal gives \[a^2 - b^2 = \frac{b^2}{\sin\theta} \qquad \implies \qquad \left(\frac{a}{b}\right)^2 = 1 +\frac{1}{\sin\theta}.\]

But now since \(0 < \sin\theta < 1\) we conclude \[\left(\frac{a}{b}\right)^2 > 2 \qquad \implies \qquad \frac{b^2}{a^2} < \frac{1}{2}.\]

If an ellipse is a ‘squashed’ circle, then the eccentricity measures the degree of ‘squashedness’. We have the standard result that \(e = \sqrt{1-\dfrac{b^2}{a^2}}\).

In our case, the eccentricity \[e = \sqrt{1-\frac{b^2}{a^2}} > \sqrt{1 - \frac 1 2} = \frac{1}{\sqrt{2}}\] as required.
