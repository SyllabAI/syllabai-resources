---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r5584
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r5584
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5584
  old_site_id: null
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
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics A 2, 1973, Q17
task: T-UGM-IMPORT-7
---

# Can we find the centre of mass of a solid hemisphere?

## Question

The region in the first quadrant enclosed by the curve \(y = \dfrac{b(a^2 - x^2)^{1/2}}{a}\) and the lines \(y = 0\), \(x = 0\), \(x = ka\) \((0 < k \le 1)\), is rotated through four right angles about the \(x\)-axis to form a solid of revolution. Show that the volume of the solid is \(\tfrac{1}{3} \pi ab^2k(3-k^2)\).

If this solid is of uniform density find the coordinates of its centre of mass.

By considering the case \(b = a\), \(k = 1\), show that the centre of mass of a uniform solid hemisphere of radius \(a\) is at a distance \(\tfrac{3}{8}a\) from the centre.

## Solution

The volume of revolution of a curve around the

\(x\)

-axis is given by the expression

\[\begin{equation*} \int \pi y^2 dx. \end{equation*}\]

So the volume we need is

\[\begin{align*} \int_0^{ka} \pi b^2 \frac{a^2 - x^2}{a^2} \:dx = \frac{\pi b^2}{a^2} \left[ a^2x - \frac{x^3}{3} \right]_0^{ka} &= \frac{\pi b^2}{a^2} \left( ka^3 - \frac{k^3a^3}{3} \right) \\ &= \pi b^2 ka \left( 1 - \frac{k^2}{3} \right) \\ &= \frac{1}{3} \pi ab^2k (3-k^2). \end{align*}\]

As this solid has rotational symmetry around the \(x\)-axis, the centre of mass lies on the \(x\)-axis, let’s say at \((\bar{x},0)\).

The moment of our solid about an axis through \(O\) (setting its density to \(1\)) is therefore \(\frac{1}{3}\pi ab^2k (3-k^2) \times \bar{x}.\)

This must equal the sum of the moments of the infinitesimal cylinders we added in the first part of the question.

This is (in the limit)

\[\begin{align*} \int_0^{ka} \pi y^2x \:dx &= \int_0^{ka} \pi b^2 \frac{a^2x - x^3}{a^2} \:dx\\ &= \frac{\pi b^2}{a^2} \left[ \dfrac{a^2x^2}{2} - \frac{x^4}{4} \right]_0^{ka}\\ &= \frac{\pi b^2}{a^2} \left( \dfrac{a^4k^2}{2} - \frac{a^4k^4}{4}\right)\\ &= \frac{\pi a^2b^2k^2}{4}(2 -k^2). \end{align*}\]

Thus

\[\begin{align*} \frac{\pi a^2b^2k^2}{4}(2 -k^2)&=\frac{1}{3} \pi ab^2k (3-k^2)\bar{x}\\ \implies \frac{ak}{4}(2 -k^2)&=\frac{1}{3}(3-k^2)\bar{x}\\ \implies 3ak(2 -k^2)&=4(3-k^2)\bar{x}\\ \implies \bar{x} &= \dfrac{3ak(2 -k^2)}{4(3-k^2)}. \end{align*}\]

By taking

\(b = a\)

and

\(k = 1\)

, we have that

\[\begin{equation*} y = \sqrt{a^2 - x^2} \end{equation*}\]

and so

\[\begin{equation*} x^2 + y^2 = a^2. \end{equation*}\]

This is the equation of a circle, centred at the origin and with radius \(a\).

Our area will rotate to a perfect hemisphere, since our integral’s limits are

\(0\)

and

\(a\)

, and so

\(x=ka\)

is tangent to the circle. Moreover,

\[\begin{equation*} \bar{x} = \frac{3ak(2 - k^2)}{4(3-k^2)} = \frac{3a(2 - 1^2)}{4(3 - 1^2)} = \frac{3a}{8}, \end{equation*}\]

and so the centre of mass of a uniform solid hemisphere of radius \(a\) is at a distance \(\dfrac{3}{8}a\) from the centre.
