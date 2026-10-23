---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r9817
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r9817
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9817
  old_site_id: Q148
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: sin^8x + cos^6x = 1 solution count — identity plus bounding argument
      rationale: 'Canonical UGM title: “When is $\sin^8 x+\cos^6 x$ equal to $1$?”; exam provenance: Oxford
        University Mathematics Aptitude Test, 2011, Q1I'
      validation_status: SUGGESTED
    title: use the identities / tan i and cos i sin i + cos i / 1
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2011, Q1I
task: T-UGM-IMPORT-5
---

# When is $\sin^8 x+\cos^6 x$ equal to $1$?

## Question

In the range \(0\le x < 2\pi\) the equation \[\sin^8 x + \cos^6 x = 1\] has

1. \(3\) solutions,

---

1. \(4\) solutions,

---

1. \(6\) solutions,

---

1. \(8\) solutions.

## Solution

There are at least two ways we could tackle this problem:

**Method 1**

It’s easy to see that

1. \(\sin x=0, \cos x=1\) at \(x = 0\),

---

1. \(\sin x = 0, \cos x = -1\) at \(x = \pi\),

---

1. \(\sin x = 1, \cos x =0\) at \(x = \pi/2,\) and

---

1. \(\sin x = -1, \cos x = 0\) at \(x = 3\pi/2\),

so we definitely have four solutions.

Are there any solutions where \(\sin x\) and \(\cos x\) are both non-zero?

In this case, we know that \(0 < \sin^2x < 1\) and \(0 < \cos^2x < 1\).

Now for any \(y\) between \(0\) and \(1\), \(y^4<y\) and \(y^3<y\).

So we know that \[\sin^8x=(\sin^2x)^4<\sin^2x, \cos^6x=(\cos^2x)^3<\cos^2x.\]

Thus \[\sin^8x+\cos^6x<\sin^2x+\cos^2x=1.\]

So our equation only holds for our four cases above, and there are exactly four solutions; the answer is (b).

**Method 2**

For convenience, let’s write \(s=\sin x\) and \(c=\cos x\).

\[\begin{align*} &s^8+c^6=1\\ \iff\quad& s^8+(1-s^2)^3=1\\ \iff\quad& s^8-s^6+3s^4-3s^2+1=1\\ \iff\quad& s^2(s^6-s^4+3s^2-3)=0\\ \iff\quad& s^2(s^2-1)(s^4+3)=0. \end{align*}\]

(We could equivalently substitute \(s^2 = 1 - c^2\).)

So there are solutions when \(s^2=0\), \(s^2=1\) and \(s^4=-3\) (the last has no real solutions).

So we require \(\sin x=0\) or \(\sin x=\pm 1\).

As in the method above, the solutions in the relevant range are \(x=0, \pi, \pi/2, 3\pi/2\), and the answer is (b).
