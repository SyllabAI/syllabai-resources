---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r7370
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r7370
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7370
  old_site_id: Q149
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
      evidence: 'simultaneous (cosθ)x − (sinθ)y = 2, (sinθ)x + (cosθ)y = 1: determinant cos^2θ + sin^2θ
        = 1 is why the system is solvable for every θ'
      rationale: 'Canonical UGM title: “How many solutions do these simultaneous trig equations have?”;
        exam provenance: Oxford University Mathematics Aptitude Test, 2008, Q1C'
      validation_status: SUGGESTED
    title: use the identities / tan i and cos i sin i + cos i / 1
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2008, Q1C
task: T-UGM-IMPORT-5
interactive:
- src: //www.geogebratube.org/material/iframe/id/d7zWPYq7/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# How many solutions do these simultaneous trig equations have?

## Question

The simultaneous equations in \(x\),\(y\), \[(\cos\theta)x - (\sin\theta)y = 2\] \[(\sin\theta)x + (\cos\theta)y = 1\] are solvable

1. for all values of \(\theta\) in the range \(0 \leq \theta < 2\pi\);

---

1. except for one value of \(\theta\) in the range \(0 \leq \theta < 2\pi\);

---

1. except for two values of \(\theta\) in the range \(0 \leq \theta < 2\pi\);

---

1. except for three values of \(\theta\) in the range \(0 \leq \theta < 2\pi\).

## Suggestion

In this applet, the blue line is \(x\sin \theta + y\cos \theta = 1\), and the red line is \(x\cos \theta - y\sin \theta= 2\).

How will each of the lines change as we change \(\theta\)?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/d7zWPYq7/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/d7zWPYq7)

The intersection point, \(A\), represents the solution to the simultaneous equations. For which values of \(\theta\) is the point \(A\) uniquely defined?

## Solution

**Method 1**

We write \(c\) for \(\cos\theta\) and \(s\) for \(\sin\theta\), so the equations become \[cx-sy=2, \qquad sx+cy=1;\] We multiply by \(c\) and \(s\) respectively and then add to eliminate \(y\), giving \[c^2x-csy = 2c, \qquad s^2x+csy = s,\] so \[2c+s = (c^2+s^2)x = x.\] Similarly, we can eliminate \(x\), since \[csx - s^2y = 2s, \qquad csx + c^2y = c\] so \[c - 2s = (s^2+c^2)y = y.\] Hence we have \(x = 2\cos\theta + \sin\theta\) and \(y = \cos\theta - 2\sin\theta\), which are valid solutions for any value of \(\theta\), and the answer is (a).

**Method 2**

For a given \(\theta\), each equation represents a straight line.

So we will have exactly one solution unless the lines coincide, or are parallel, that is, unless they have the same gradient.

The gradient of the first line is \(\dfrac{\cos \theta}{\sin \theta}\), while the gradient of the second is \(-\dfrac{\sin \theta}{\cos \theta}\).

These can only be equal if \(\dfrac{\cos \theta}{\sin \theta}=-\dfrac{\sin \theta}{\cos \theta}\), which is true if and only if \(\cos^2 \theta + \sin^2 \theta = 0\), which is never true.

So there is always exactly one solution for any given \(\theta\), and the answer is (a).

**Method 3**

*This requires [compound angle formulae](https://undergroundmathematics.org/glossary/compound-angle-formula)*

If we square and add the two equations, we get \(x^2 + y^2 = 5\). Thus any solution must be of the form \[x = \sqrt{5}\cos\alpha, y = \sqrt{5}\sin\alpha, \quad 0\leq \alpha < 2\pi.\]

Substituting this back into our equations (since squaring may have introduced extra solutions), we have \[\cos(\theta + \alpha) = \dfrac{2}{\sqrt{5}}, \sin(\theta + \alpha) = \dfrac{1}{\sqrt{5}}.\]

Thus \(\theta + \alpha\) is in the first quadrant, and for any \(\theta\) there is exactly one solution for \(\alpha\), and the answer is (a).
