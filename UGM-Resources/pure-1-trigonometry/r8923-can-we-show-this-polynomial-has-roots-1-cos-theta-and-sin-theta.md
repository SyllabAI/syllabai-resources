---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r8923
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r8923
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8923
  old_site_id: Q139
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
      evidence: cubic with roots 1, cosθ, sinθ — factorisation closes with the sin^2+cos^2=1 identity
        (polynomial carrier rides 1.1.4)
      rationale: 'Canonical UGM title: “Can we show this polynomial has roots $1$, $\cos\theta$ and $\sin\theta$?”;
        exam provenance: Oxford University Mathematics Aptitude Test, Specimen 1, Q2'
      validation_status: SUGGESTED
    title: use the identities / tan i and cos i sin i + cos i / 1
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, Specimen 1, Q2
task: T-UGM-IMPORT-5
---

# Can we show this polynomial has roots $1$, $\cos\theta$ and $\sin\theta$?

## Question

1. Show, with working, that \[\begin{equation} x^3 - (1 + \cos\theta + \sin\theta)x^2 + (\cos\theta\sin\theta + \cos\theta + \sin\theta)x - \sin\theta\cos\theta, \qquad \label{eq:1} \end{equation}\] equals \[(x - 1)(x^2 - (\cos\theta + \sin\theta)x + \cos\theta\sin\theta).\] Deduce that the cubic in \(\eqref{eq:1}\) has roots \[1, \qquad \cos\theta, \qquad \sin\theta.\]

---

1. Give the roots when \(\theta = \dfrac{\pi}{3}\).

---

1. Find all values of \(\theta\) in the range \(0 \leq \theta < 2\pi\) such that two of the three roots are equal.

---

1. What is the greatest possible difference between two of the roots, and for what values of \(\theta\) in the range \(0 \leq \theta < 2\pi\) does this greatest difference occur? Show that for each such \(\theta\) the cubic \(\eqref{eq:1}\) is the same.

## Solution

1. Show, with working, that \[\begin{equation} x^3 - (1 + \cos\theta + \sin\theta)x^2 + (\cos\theta\sin\theta + \cos\theta + \sin\theta)x - \sin\theta\cos\theta, \label{eq:1repeat} \end{equation}\] equals \[(x - 1)(x^2 - (\cos\theta + \sin\theta)x + \cos\theta\sin\theta).\]

The simplest way to show this is to start with the factorised expression and multiply it out. If we write

\(c\)

for

\(\cos\theta\)

and

\(s\)

for

\(\sin\theta\)

we have

\[\begin{align*} (x - 1)(x^2 - (c + s)x + cs) &= [x^3 - (c+s)x^2 + csx] - [x^2 -(c+s)x + cs]\\ &= x^3 - (1 + c + s)x^2 + (cs + c + s)x - cs. \end{align*}\]

Deduce that the cubic in \(\eqref{eq:1repeat}\) has roots \[1, \qquad \cos\theta, \qquad \sin\theta.\]

If we factorise the quadratic above further we get \[x^2 - (c+s)x + cs = (x-c)(x-s),\] and so the three roots of the cubic are \(1\), \(c\) and \(s\).

In this case, the three roots are \(1\), \(c = \cos \dfrac{\pi}{3} = \dfrac{1}{2}\) and \(s = \sin \dfrac{\pi}{3} = \dfrac{\sqrt{3}}{2}\).

There are three possible cases:

1. \(s = 1\), which only occurs in the given range when \(\theta = \pi/2\);

---

1. \(c = 1\), in which case \(\theta = 0\);

---

1. \(s = c\), that is, \(\tan\theta = 1\) and \(\theta = \pi/4\) or \(5\pi/4\).

There are three cases.

1. we take the difference between \(1\) and \(s\), which is largest when \(s = -1\), in which case the difference is \(2\).

---

1. we take the difference between \(1\) and \(c\), which is largest when \(c = -1\), in which case the difference is \(2\).

---

1. we take the difference between \(c\) and \(s\). Here it is impossible for one to be \(1\) and the other to be \(-1\) at the same time, so their difference must be less than \(2\).

More precisely, we could say that for case (3), the difference between \(c\) and \(s\) is largest when \(\big\vert c - s\big\vert\) is largest, which is when \(\sqrt{2}\big\vert\cos \big(x + \dfrac{\pi}{4}\big)\big\vert\) is largest.

The largest possible value here is \(\sqrt{2} < 1\), so we can rule this out.

Cases (1) and (2) occur at \(\theta = 3\pi/2\) and \(\theta = \pi\) respectively.

Show that for each such \(\theta\) the cubic \(\eqref{eq:1repeat}\) is the same.

When \(c = -1\) then \(s = 0\), and when \(s = -1\) then \(c = 0\). Since the cubic is symmetric in \(s\) and \(c\), the cubic will be the same in each case.

We can calculate the polynomial explicitly in each case as a check to get

\[(x-1)(x-0)(x+1) = x^3 - x.\]
