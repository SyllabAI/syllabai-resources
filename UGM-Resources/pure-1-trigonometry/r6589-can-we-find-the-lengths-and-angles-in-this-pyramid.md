---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r6589
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r6589
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6589
  old_site_id: Q1003
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
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics A 1 and Pure Mathematics 1, QP 9200/1 and 9208/1, 1984, Q12
task: T-UGM-IMPORT-5
---

# Can we find the lengths and angles in this pyramid?

## Question

An equilateral triangle \(ABC\) has side length \(6\) units. The three [altitudes](https://undergroundmathematics.org/glossary/altitude-of-triangle) of the triangle meet at \(N\). Show that \(AN=2\sqrt{3}\) units.

This triangle is the base of a pyramid whose apex \(V\) lies on the line through \(N\) perpendicular to the plane \(ABC\). Given that \(VN=2\) units, prove that \(\widehat{VAN}=30^\circ.\)

The perpendicular from \(A\) to the edge \(VC\) meets \(CV\) produced at \(R\). Prove that \(AR=\frac{3}{2}\sqrt{7}\) units, and find the exact value of \(\cos \widehat{ARB}\).

## Suggestion

Could we draw a picture of \(ABC\) with the altitudes and \(N\) marked? Can you spot any similar triangles? Or right-angled triangles?

Could we draw another picture? In three dimensions this time?

The phrase “\(CV\) produced” means, “the line segment \(CV\) extended”.

Could we draw a picture of \(AVC\), marking in \(R\)? Which lengths in this triangle do we already know?

## Solution

To find the length \(AN\), let’s call the midpoint of \(AC, M\), and the midpoint of \(BC, P\).

Then the triangles \(ANM\) and \(ACP\) are similar, since they are both right-angled, and they also share another angle.

Using Pythagoras, we find that \(AP=\sqrt{6^2-3^2}=\sqrt{36-9}=\sqrt{27}=3\sqrt{3}\). We know that

\[\frac{AN}{3}=\frac{AN}{AM}=\frac{AC}{AP}=\frac{6}{3\sqrt{3}},\]

since the triangles are similar, and so \(AN=\dfrac{6}{\sqrt{3}}=6\dfrac{\sqrt{3}}{3}=2\sqrt{3}\) units.

Alternatively, we could have recognised that \(ANM\) is a standard \(30\)-\(60\)-\(90\) triangle with edges in the ratio \(1:2:\sqrt{3}\).

We know \(AN\), and \(VN\) is given in the question giving \(\tan\widehat{VAN}=\dfrac{2}{2\sqrt 3}=\dfrac{1}{\sqrt 3}\) which we should recognize as \(\tan 30^\circ\) giving \(\widehat{VAN}=30^\circ.\)

Alternatively we find \(AV = 4\), by Pythagoras.

We now have that \[\sin\widehat{VAN}=\frac{2}{4}=\frac{1}{2},\] Therefore \(\widehat{VAN}=30^\circ.\)

The perpendicular from \(A\) to the edge \(VC\) meets \(CV\) produced at \(R\). Prove that \(AR=\dfrac{3}{2}\sqrt{7}\) units, and find the exact value of \(\cos \widehat{ARB}\).

The triangle \(AVC\)

By symmetry, we know that \(AV=VC\). We’ll use the cosine rule to find \(\widehat{ACV}\).

Applying the cosine rule to

\(ACV\)

, we have that

\[\begin{align*} 4^2&=6^2+4^2-2\times 4\times 6\times \cos\widehat{ACV}, \\ 48\cos\widehat{ACV}&=36, \\ \cos\widehat{ACV}&=\frac{3}{4}. \end{align*}\]

Now by right-angled trigonometry, we have that \[\sin\widehat{ACV}=\frac{AR}{6},\] and so \[AR=6\sin\widehat{ACV}=6\sqrt{1-\cos^2\widehat{ACV}}=6\sqrt{\frac{7}{16}}=\frac{6}{4}\sqrt{7}=\frac{3}{2}\sqrt{7}.\]

Alternatively, we could say \(RV = x\), and \(AR = y\), and then use Pythagoras twice to create simultaneous equations that enable us to find \(y\).

We need now to compute \(\cos\widehat{ARB}\).

By symmetry, we have that \(BR=AR\). So we can apply the cosine rule to \(ARB\).

The triangle \(ARB\)

We have that

\[\begin{align*} 6^2&=2\left(\frac{3\sqrt{7}}{2}\right)^2-2\left(\frac{3\sqrt{7}}{2}\right)\left(\frac{3\sqrt{7}}{2}\right)\cos\widehat{ARB}, \\ \implies 36&=\frac{9\times 7}{2}-\frac{9\times 7}{2}\cos\widehat{ARB} \\ \implies 63\cos\widehat{ARB}&=63-72,\\ \implies \cos\widehat{ARB}&=-\frac{9}{63}=-\frac{1}{7}. \end{align*}\]
