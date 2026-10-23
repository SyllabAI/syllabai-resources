---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r7378
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r7378
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7378
  old_site_id: Q88
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-triangles-to-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-triangles-to-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.5.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: x^2+y^2+4x cosθ+8y sinθ+10=0 represents a circle iff 4cos^2θ+16sin^2θ>10 — the deciding
        sin^2θ range comes from the identity (circle-equation carrier rides 1.3.2)
      rationale: 'Canonical UGM title: “When does this equation in $x, y$ and $\theta$ represent a circle?”;
        exam provenance: Oxford University Mathematics Aptitude Test, 2011, Q1F'
      validation_status: SUGGESTED
    title: use the identities / tan i and cos i sin i + cos i / 1
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2011, Q1F
task: T-UGM-IMPORT-5
interactive:
- src: //www.geogebratube.org/material/iframe/id/UQrH6fY9/width/500/height/450/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does this equation in $x, y$ and $\theta$ represent a circle?

## Question

*[Choose the one correct answer and explain your reasoning.]*

Given \(\theta\) in the range \(0\leq \theta < \pi\), the equation \[x^2+y^2+4x \cos\theta+8y \sin\theta+10=0\] represents a circle for

1. \(0<\theta<\dfrac{\pi}{3}\);

---

1. \(\dfrac{\pi}{4}<\theta<\dfrac{3\pi}{4}\);

---

1. \(0<\theta<\dfrac{\pi}{2}\);

---

1. all values for \(\theta\).

## Suggestion

What is the general form for the equation of a circle? Can we manipulate this equation into that form?

## Solution

This applet shows the curve \(x^2+y^2+4x \cos\theta+8y \sin\theta+10=0\). We can vary \(\theta\) in the range \(0\leq \theta < \pi\).

What happens to the centre and radius of the circle?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/UQrH6fY9/width/500/height/450/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/UQrH6fY9)

By completing the square we obtain \[(x+2 \cos\theta)^2- 4\cos^2\theta+(y + 4\sin\theta)^2-16\sin^2\theta+10=0.\]

Then by rearranging we get \[(x+2\cos\theta)^2+(y+4\sin\theta)^2=4\cos^2\theta + 16\sin^2\theta-10.\]

Since \(\sin^2\theta + \cos^2\theta=1\), we see that the right-hand side becomes \[4\cos^2\theta + 16\sin^2\theta-10 = 12\sin^2\theta-6.\]

So the equation defines a circle of radius \(\sqrt{12 \sin^2\theta-6}\), for \(\sin^2\theta>\dfrac{1}{2}\).

In the range \(0\leq \theta < \pi\), we have \(\sin\theta\geq0\) so we need \(\sin \theta >\dfrac{1}{\sqrt2}\).

Hence the answer is (b).
