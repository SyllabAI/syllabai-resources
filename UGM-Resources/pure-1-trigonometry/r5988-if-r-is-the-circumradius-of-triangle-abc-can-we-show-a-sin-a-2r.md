---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r5988
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r5988
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5988
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-compound-angles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-compound-angles
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics A 2, QP 840/2, 1973, Q15
task: T-UGM-IMPORT-5
---

# If $R$ is the circumradius of triangle $ABC$, can we show $a\:/\sin A = 2R$?

## Question

With the usual notation prove that

\[\begin{equation*} \frac{a}{\sin A} = 2R \end{equation*}\]

where \(R\) is the radius of the circumcircle of the triangle \(ABC\).

[You need consider only the case when the angle \(A\) is acute.]

Hence or otherwise deduce that

1. \(a \cos A + b \cos B = c \cos (A-B)\),

---

1. \(a \cos A + b \cos B + c \cos C = 4 R \sin A \sin B \sin C\).

## Solution

In the diagram on the left we have used the facts that

- the perpendicular from the centre bisects the chord \(BC\), and

- the angle at the centre is twice the angle at the circumference.

Now we can see that \(R \sin A = \dfrac{a}{2}\). Alternatively, in the diagram on the right we have used the facts that

- the angles subtended at the circumference are equal, and

- the angle in a semi-circle is a right-angle.

This shows us that \(\sin A = \dfrac{a}{2R}\).

Either of these gives us \(\dfrac{a}{\sin A} = 2R\) as required.

We will use the identities \(\sin 2x = 2\sin x \cos x\), \(\sin (\pi - x) = \sin x\), and \(\sin x + \sin y = 2\sin \dfrac{x+y}{2}\cos \dfrac{x-y}{2}\).

Now

\[\begin{align*} a\cos A + b\cos B &= \frac{a}{\sin A} \sin A \cos A + \frac{b}{\sin B} \sin B \cos B\\ &= 2R\sin A \cos A + 2R \sin B \cos B\\ &= R(\sin 2A + \sin 2B)\\ &= R(2\sin (A+B)\cos (A-B))\\ &= 2R\sin (\pi-A-B)\cos (A-B))\\ &= 2R \sin C \cos (A-B)\\ &= \dfrac{c}{\sin C}\sin C \cos (A-B)\\ &= c\cos (A-B), \end{align*}\]

as required.

We’ll use the additional identities \(\cos x + \cos y = 2\cos\dfrac{x+y}{2}\cos\dfrac{x-y}{2}\), and \(\cos\left(\dfrac{\pi}{2}-x\right) = \sin x\).

We have

\[\begin{align*} a \cos A + b \cos B + c \cos C &= \dfrac{a}{\sin A}\sin A \cos A + \dfrac{b}{\sin B}\sin B \cos B + \dfrac{c}{\sin C}\sin C \cos C\\ &= 2R(\sin A \cos A + \sin B \cos B + \sin C \cos C)\\ &= R(\sin 2A + \sin 2B + 2\sin C\cos C)\\ &= R (2\sin (A+B)\cos(A-B) + 2 \sin C \cos C)\\ &= R (2\sin C \cos(A-B) + 2\sin C \cos C)\\ &= 2R \sin C (\cos(A-B)+\cos C)\\ &= 4R \sin C \left(\cos \dfrac{A+C-B}{2} \cos \dfrac{A-B-C}{2}\right)\\ &= 4R \sin C \cos \left(\dfrac{\pi}{2}-B\right) \cos \left(\dfrac{\pi}{2}-A\right)\\ &= 4R \sin A \sin B \sin C. \end{align*}\]
