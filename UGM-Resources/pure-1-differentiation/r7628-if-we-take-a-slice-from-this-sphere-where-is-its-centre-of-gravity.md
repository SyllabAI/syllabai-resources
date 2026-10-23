---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r7628
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r7628
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7628
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
  exam_reference: O&C O level General Mathematics 2, 1967, Q4
task: T-UGM-IMPORT-7
---

# If we take a slice from this sphere, where is its centre of gravity?

## Question

A portion of a solid sphere of radius \(a\) is cut off by means of a plane whose distance from the centre of the sphere is \(\frac{1}{2}a\). Find the volume of the portion cut off.

Find also the distance from the circular plane face of the centre of gravity of this portion.

## Solution

Here is a section through the centre of the sphere. With this choice of axes, the equation of the circle is \(x^2+y^2 = a^2\), and hence \(y^2=a^2-x^2\).  and so the curve in the first quadrant is given by $y = \sqrt{a^2-x^2}$.

The portion cut off is shown in grey. Its volume can be found by revolving the circular arc for \(\frac{a}{2} < x < a\) about the \(x\)-axis.

We can view this as a solid of revolution defined by the function \begin{equation*} y = \sqrt{a^2 - x^2}, \quad\frac{a}{2} < x < a. \end{equation*} Thus the required volume is

\[\begin{align*} \int_{a/2}^a \pi y^2 \:dx &= \pi \int_{a/2}^a a^2 - x^2 \:dx \\ &= \pi \left[ a^2x - \frac{x^3}{3} \right]_{a/2}^a \\ &= \pi \left( a^3 - \frac{a^3}{3} - \frac{a^3}{2} + \frac{a^3}{24} \right) \\ &= \pi a^3 \left( \frac{24 - 8 - 12 + 1}{24} \right ) \\ &= \frac{5}{24} \pi a^3. \end{align*}\]

By symmetry, the centre of gravity (or [centre of mass](https://undergroundmathematics.org/glossary/centre-of-mass)) lies on the \(x\)-axis in our diagram. To find out where on the axis, we take [moments](https://undergroundmathematics.org/glossary/moment-of-a-force) about \(O\) and treat the sphere as having density of \(1\).

We divide the grey solid into discs, each with its centre \(x\) from \(O\), with thickness \(\delta x\) and radius \(y\). The volume of a disc is \(\pi y^2 \delta x\).

The moment of each disc about \(O\) is \(x \pi y^2 \delta x\).

We now let the thickness of the discs tend to zero, at which point the sum of these moments becomes an integral. Let the centre of mass of the grey portion be at a distance \(\bar x\) from \(O\).

\[\begin{align*} \bar x \frac{5}{24} \pi a^3 &= \int_{a/2}^a x \pi y^2 \:dx\\ &= \pi\int_{a/2}^a x(a^2 - x^2) \:dx \\ &= \pi\left[ \frac{a^2x^2}{2} - \frac{x^4}{4} \right]_{a/2}^a\\ &= \pi\left( \frac{a^4}{2} - \frac{a^4}{4} - \frac{a^4}{8} + \frac{a^4}{64} \right) \\ &= \pi\frac{9}{64} a^4, \end{align*}\]

and therefore

\[\begin{equation*} \bar x = \frac{\frac{9}{64} \pi a^4}{\frac{5}{24} \pi a^3} = \frac{27}{40} a. \end{equation*}\]

The required distance from the plane is therefore

\[\begin{equation*} \frac{27}{40} a - \frac{1}{2} a = \frac{7}{40} a. \end{equation*}\]

It is interesting to note that the centre of mass is not the same as the point which has exactly half the mass of the grey solid on each side of it. This latter point, \(\bar X\), can be found by integration and is such that \(\bar X \approx 0.6571 a\), whereas the centre of mass, \(\bar x = 0.675 a\).

This is equivalent to the distinction between the median and the mean of the distribution of mass.

It is interesting that $X$ is *not* the same as the point $\dfrac{a}{2} < X' < a$ at which exactly half of the mass is on one side of $X'$. The point $X'$ is such that \begin{equation*} \int_{a/2}^{X'} \pi (a^2 - x^2)\:dx = \int_{X'}^a \pi (a^2 - x^2) \:dx; \end{equation*} after cancelling by $\pi$, we have \begin{equation*} \left[ a^2x - \frac{x^3}{3} \right]_{a/2}^{X'} = \left[ a^2x - \frac{x^3}{3} \right]_{X'}^a \end{equation*} which, after expanding both sides and rearranging, becomes the equation \begin{equation*} \frac{2}{3} X'^3 - 2a^2X' + \frac{9}{8} a^3 = 0. \end{equation*} Since $X'$ lies between $\dfrac{a}{2}$ and $a$, we can write $X' = \beta a$ for some $\beta$ lying between $\dfrac{1}{2}$ and $1$. The above becomes \begin{equation*} \beta^3 - 3\beta + \frac{27}{16} = 0. \end{equation*} It's not too difficult to solve this exactly. The only solution in our region of interest is $\beta \approx 0.657055$, so \begin{equation*} X' \approx 0.657055 a \end{equation*} whereas \begin{equation*} X = \frac{27}{40} a = 0.675a. \end{equation*} In statistical terms, we are really saying here that the mean and the median for a given distribution need not coincide.
