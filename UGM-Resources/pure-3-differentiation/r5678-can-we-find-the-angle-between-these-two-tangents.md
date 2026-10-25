---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r5678
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r5678
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5678
  old_site_id: Q1029
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
      evidence: tangent to the hyperbola xy = c^2 through the parabola focus, the a^4 = 2c^4 condition
        and the acute angle between the tangents - parametric/implicit derivative work on both conics
      rationale: 'Canonical UGM title: Can we find the angle between these two tangents?'
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

# Can we find the angle between these two tangents?

## Question

The point \(P\) on the hyperbola \(xy=c^2\) is such that the tangent to the hyperbola at \(P\) passes through the focus of the parabola \(y^2=4ax\). Find the coordinates of \(P\) in terms of \(a\) and \(c\).

If \(P\) also lies on the parabola, prove that \(a^4=2c^4\), and calculate the acute angle between the tangents to the two curves at \(P\).

## Suggestion

Every parabola has a special point, called the focus. If you imagine turning the parabola into a mirror, and turning it to face the sun, then all of the sun’s rays would be reflected by the parabola through its focus. For the parabola, \(y^2 = 4ax\), the focus is at \((a,0).\)

You might like to take a look at our [Parabolic Mirrors](https://undergroundmathematics.org/quadratics/parabolic-mirrors) resource.

What’s the equation of a line with gradient \(m\) that passes through \((a,0)\)? Where does this line intersect \(xy=c^2\)?

If the line is a tangent, how many times does it intersect the curve?

What does this tell us about \(m\)? Once we’ve found \(m\), can we find \(P\)?

If \(P\) also lies on the parabola, prove that \(a^4=2c^4\) …

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/pH7QhttG/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/pH7QhttG)

The blue curve here is the hyperbola \(xy = c^2\), while the red curve is the parabola \(y^2=4ax\).

The green line is the tangent to the hyperbola though the parabola’s focus \(F\), which touches the hyperbola at \(P\).

The values of \(a^4\) and \(2c^4\) are given. Can we use this to verify what the question asks us to show?

… and calculate the acute angle between the tangents to the two curves at \(P\).

How is the gradient of a line linked to the angle it makes with the \(x\)-axis?

Or as an alternative method… the [dot product](https://undergroundmathematics.org/glossary/dot-product) of two vectors can help us find the angle between them.

## Solution

It is a standard result that the focus of the parabola

\(y^2=4ax\)

is at

\((a,0)\)

. The general equation of a straight line with gradient

\(m\)

passing through

\((a,0)\)

is

\[y=m(x-a).\]

This will intersect the curve

\(xy=c^2\)

when:

\[\begin{align} x\times m(x-a) &= c^2 \notag \\ \Longrightarrow \quad mx^2 -amx-c^2 &= 0. \label{eq:1} \end{align}\]

If

\(y=m(x-a)\)

is to be tangent to the hyperbola

\(xy=c^2,\)

then

\(\eqref{eq:1}\)

will have a repeated root, which means the discriminant of this quadratic will be

\(0\)

. This gives

\[\begin{align} a^2m^2-4\times m \times (-c^2)&=0 \notag \\ \Longrightarrow \quad m(a^2m+4c^2) &=0 \notag \\ \Longrightarrow \quad m=-\frac{4c^2}{a^2}. \label{eq:grad-of-tangent} \end{align}\]

We have ignored the \(m=0\) solution, as this is the horizontal asymptote of \(xy=c^2\). We now have \[x=\frac{am\pm \sqrt{0}}{2m}=\frac{a}{2}.\] Since \(P\) lies on \(xy=c^2\), the corresponding \(y\)-coordinate is \[y=\frac{c^2}{x}=\frac{2c^2}{a}\] so \[P=\left(\frac{a}{2},\frac{2c^2}{a}\right).\]

If

\(P\)

also lies on the parabola then

\(P\)

satisfies

\(y^2=4ax,\)

so

\[\begin{align} \left(\frac{2c^2}{a}\right)^2 &= 4a\left(\frac{a}{2}\right) \notag \\ \Longrightarrow \quad \frac{4c^4}{a^2} &= 2a^2 \notag \\ \Longrightarrow \quad 2c^4 &= a^4. \label{eq:c4a4} \end{align}\]

… and calculate the acute angle between the tangents to the two curves at \(P\).

If a line of gradient \(m\) cuts the \(x\)-axis at an angle \(\theta\), then \(m = \tan \theta\). From the following diagram, we see that we need to find \(\alpha - \theta\).

What is the gradient of the parabola, \(y^2 = 4ax\), at \(P\)? We can either [differentiate implicitly](https://undergroundmathematics.org/glossary/implicit-differentiation) or take the square root, \[y = 2\sqrt{ax} \implies \frac{dy}{dx} = 2\sqrt{a}\times\frac{1}{2}x^{-1/2} = \sqrt{\dfrac{a}{x}}.\]

Since the \(x\)-coordinate of \(P\) is \(\dfrac{a}{2}\), we have the gradient \(\tan \theta = \sqrt{\dfrac{a}{a/2}} = \sqrt{2}\).

From our earlier work, \(\eqref{eq:grad-of-tangent}\) and \(\eqref{eq:c4a4}\), we know \(\tan \alpha = -\dfrac{4c^2}{a^2} = -\dfrac{4}{\sqrt{2}} = -2\sqrt{2}\).

Now we can use a standard trig identity to find

\[\begin{align*} \tan(\alpha-\theta) &= \dfrac{\tan \alpha - \tan \theta}{1+\tan \alpha \tan \theta}\\ &= \dfrac{ -2\sqrt{2}-\sqrt{2}}{1-2\sqrt{2}\sqrt{2}} \\ &= \sqrt{2}.\\ \end{align*}\]

Hence the angle between the tangents at \(P\) is \(\arctan \sqrt{2}\approx 0.955^c \approx 54.7^\circ\).

It turns out that \(\theta=\alpha-\theta\) and the triangle in the above diagram is isosceles.

Instead of using the identity, we could have calculated \(\arctan{\sqrt{2}}\) and \(\arctan{\left(-2\sqrt{2}\right)}\) and taken the difference.

Alternatively, we could find the angle between the two lines using the [dot product](https://undergroundmathematics.org/glossary/dot-product) of the two direction vectors.

The tangent to the parabola has gradient \(\sqrt{2}\) so its direction vector can be written as \[\mathbf{a} = \begin{pmatrix}1 \\ \sqrt{2}\end{pmatrix}\] and the tangent to the hyperbola can be written as \[\mathbf{b} = \begin{pmatrix}1 \\ -2\sqrt{2}\end{pmatrix}.\]

The dot product can then be computed as

\[\begin{align*} \mathbf{a}\cdot\mathbf{b} &= 1-2\sqrt{2}\sqrt{2}=-3 \\ &= |\mathbf{a}| \: |\mathbf{b}| \cos\theta = \sqrt{1+2}\sqrt{1+4\times2}\cos\theta \\ \implies\quad \cos\theta &= -\frac{1}{\sqrt{3}} \end{align*}\]

This actually gives us the obtuse angle but it’s then easy to find the acute one.
