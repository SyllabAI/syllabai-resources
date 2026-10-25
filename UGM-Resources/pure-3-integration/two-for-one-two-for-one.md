---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/two-for-one
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/food-for-thought
resource_identity:
  ugm_id: two-for-one
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 5833
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-trig-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-trig-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: 'INT 1/x dx over positive and negative intervals - when and why ln x versus ln|x|: the
        modulus-sign convention IS the 3.5.1 1/(ax+b) list-item knowledge, with the odd-function area
        reasoning and ln(-x) gradient-function check (flips the lane-10 non-overlap row of record routed
        ''P3 3.5 Integration'')'
      rationale: 'Canonical UGM title: Two for one'
      validation_status: SUGGESTED
    title: extend the idea of ‘reverse differentiation’ to Including examples such as ax + b 1 include
      the integration of e , , ax + b sin( ax + b ) , cos( ax + b ) , sec ( ax + b ) and 2 2 x + a
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# Two for one

> Excerpt: What do we get when we integrate $\frac{1}{x}$? $\ln x$ or $\ln |x|$? In this task, students are asked to think about when and why we use the modulus sign.

## Problem

Solve the following integrals:

- \(\displaystyle{\int_{2}^{3} \dfrac{1}{x} \, dx}\)

- \(\displaystyle{\int_{-3}^{-2} \dfrac{1}{x} \, dx}\)

What’s the same and what’s different about your solutions?

Did you make any assumptions, and if so, what were they?

Sketch the following functions along with their gradient functions on the same set of axes.

- \(f(x) = \ln (x)\)

- \(g(x) = \ln (-x)\)

What are the domains of \(f(x)\) and \(g(x)\)?

Using your sketch to help you, write down the derivatives of \(f(x)\) and \(g(x)\).

What do you notice about the derivatives \(f'(x)\) and \(g'(x)\)?

## Suggestion

Use the applet to check your sketches of \(f(x)\), \(g(x)\) and their gradient functions.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/uJbx2Du6/width/614/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/uJbx2Du6)

## Solution

A good starting point is to draw a diagram.

As \(\tfrac{1}{x}\) is an odd function, the two shaded areas that represent the integrals should be the same. However, one of the areas is below the \(x\)-axis which suggests that \[\displaystyle{\int_{-3}^{-2} \dfrac{1}{x} \, dx} = - \displaystyle{\int_{2}^{3} \dfrac{1}{x} \, dx}.\]

If we solve the first integral we get

\[\begin{align*} \displaystyle{\int_{2}^{3} \dfrac{1}{x} \, dx} &= \big[\ln x \big]_{2}^{3} \\ &= \ln (3) - \ln (2) \\ &= \ln \frac{3}{2}. \end{align*}\]

What are the problems with this calculation to find the second integral?

\[\begin{align*} \displaystyle{\int_{-3}^{-2} \dfrac{1}{x} \, dx} &= \big[\ln x \big]_{-3}^{-2} \\ &= \ln (-2) - \ln (-3) \\ &= \ln \frac{2}{3} \end{align*}\]

The function

\(\ln x\)

is only defined for

\(x >0\)

so

\(\ln (-2)\)

and

\(\ln (-3)\)

do not exist. For

\(x < 0\)

we can write

\[\displaystyle{\int \dfrac{1}{x} \, dx} = \ln |x| +c, \]

which means that we could solve the second integral like this:

\[\begin{align*} \displaystyle{\int_{-3}^{-2} \dfrac{1}{x} \, dx} &= \big[\ln |x| \big]_{-3}^{-2} \\ &= \ln |-2| - \ln |-3| \\ &= \ln 2 - \ln 3 \\ &= \ln \frac{2}{3}. \end{align*}\]

Does this match with our geometrical reasoning at the beginning? We thought that \[\displaystyle{\int_{-3}^{-2} \dfrac{1}{x} \, dx} = - \displaystyle{\int_{2}^{3} \dfrac{1}{x} \, dx},\]

and using the laws of logarithms we can show that \(\ln \frac{2}{3} = -\ln \frac{3}{2}\), which is as expected.

Taking the absolute value of \(x\) means that we aren’t trying to take the logarithm of a negative number. Why is it possible to do this? We explore below why the integral can be written in this form.

The domain of \(f(x) = \ln x\) is \(x > 0\) and the domain of \(g(x) = \ln(-x)\) is \(x < 0\).

The gradient function of \(f(x)\) is \(f'(x) = \tfrac{1}{x}, x >0\).

As \(\ln(-x)\) is a reflection of \(\ln x\) in the \(y\)-axis, the gradient of \(\ln(-x)\) will be the negative of the gradient of \(\ln x\) at symmetrical points. By also looking at the sketch of the gradient function of \(g(x)\), it seems reasonable to conclude that \(g'(x) = \tfrac{1}{x}\), when \(x <0\).

If you already know the chain rule, you may have calculated the gradient of

\(g(x)\)

this way:

\[\begin{align*} g'(x) &= \dfrac{1}{-x} \times -1 \\ &= \dfrac{1}{x}. \end{align*}\]

Interestingly, the two functions \(f\) and \(g\), differentiate to different sections of the same function, \(\tfrac{1}{x}\). It seems that the function \(\tfrac{1}{x}\) has two different antiderivatives, depending on the domain. This means we can write the integral of \(\tfrac{1}{x}\) as a piecewise function.

\[\int \dfrac{1}{x} \, dx = \begin{cases} \ln x + c & \text{if } x > 0 \\ \ln(-x) + d & \text{if } x < 0 \end{cases}\]

But \(\ln |x|\) can also be written as a piecewise function

\[\ln |x| = \begin{cases} \ln x & \text{if } x > 0 \\ \ln(-x) & \text{if } x < 0 \end{cases}\]

and so the integral is sometimes written as

\[\int \dfrac{1}{x} \, dx = \ln |x| + c.\]

The absolute value sign isn’t there to let us take logarithms of negative numbers, but because we are actually combining two different antiderivative functions. While writing \(\ln |x|\) is a way to encompass both functions, we need to be careful that we remember that it is two separate functions, one for \(x > 0\) and one for \(x < 0\).
