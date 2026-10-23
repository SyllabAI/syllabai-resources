---
created: 2026-10-23T14:47:57 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/circular-slice
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/rich-example
- level/developing
resource_identity:
  ugm_id: circular-slice
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 2
  resource_type_label: Rich example
  level: Developing
  ref: 7726
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-circular-measure.json (P3c lane 4) @ syllabai-experimental b52cf1bf
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-4
assets:
- path: https://undergroundmathematics.org/chain-rule/circular-slice/assets/circular-slice-worksheet.pdf
  kind: printable
- path: https://undergroundmathematics.org/chain-rule/circular-slice/download/teacher-notes.pdf
  kind: printable
---

# Circular slice

> Excerpt: Students are asked to solve $\int_a^b \sqrt{1-x^2} \, dx$ by substitution, before looking at how they can link their answer to a geometric representation of the problem.

## Problem

Use the substitution \(x = \cos \theta\) to find

\[\int_a^b \sqrt{1-x^2} \, dx\]

Check your solution

If

\(x = \cos \theta\)

then

\(\dfrac{dx}{d\theta} = -\sin \theta\)

, meaning we can write

\(dx = -\sin \theta \, d\theta.\)

\[\begin{align*} \int_a^b \sqrt{1-x^2} \, dx &= \int\limits_{\arccos a}^{\arccos b} \!\!\!\! \sqrt{1-\cos^2 \theta} \times -\sin \theta \, d\theta \\ &= \int\limits_{\arccos a}^{\arccos b} \!\!\!\! -\sin^2 \theta \, d\theta \\ \end{align*}\]

We can’t integrate \(\sin^2 \theta\) directly, instead we need to recognise that we can rewrite it in terms of \(\cos 2\theta\).

You might have noticed that the limits have changed. Why is this the case?

\[\begin{align*} \int\limits_{\arccos a}^{\arccos b} \!\!\!\! - \sin^2 \theta \, d\theta &= \int\limits_{\arccos a}^{\arccos b} \!\!\!\! \left(\frac{1}{2} \cos 2\theta - \frac{1}{2}\right) \, d\theta \\ &= \left[\frac{1}{4}\sin 2\theta - \frac{1}{2}\theta \right]_{\arccos a}^{\arccos b} \\ &= \left[\frac{1}{2}\sin\theta \cos \theta - \frac{1}{2}\theta \right]_{\arccos a}^{\arccos b} \end{align*}\]

From here we could substitute in our values of \(\theta\) but we will get expressions like \(\sin(\arccos b)\) which can be difficult to work with. Instead it will be helpful to rewrite our expression in terms of \(x\).

The functions \(\sin \theta\), \(\cos \theta\) and \(\theta\) appear. We know \(\cos \theta = x\), as this is our original substitution, and therefore \(\theta = \arccos x\). For \(\sin \theta\) we can think of \(\sin^2\theta + \cos^2 \theta = 1\), or a right angle triangle with a hypotenuse of \(1\) and base of \(x\), both of which give us the same result: \(\sin \theta = \sqrt{1-x^2}.\)

\[\begin{align*} &= \left[\frac{1}{2}x\sqrt{1-x^2} - \frac{1}{2}\arccos x \right]_{x=a}^{x=b} \\ &= \frac{1}{2}b\sqrt{1-b^2} - \frac{1}{2}\arccos b - \frac{1}{2}a\sqrt{1-a^2} + \frac{1}{2}\arccos a \end{align*}\]

How does your answer to \(\displaystyle{\int_a^b \sqrt{1-x^2} \, dx}\) relate to the following diagram?

## Suggestion

Look carefully at the diagram above.

- Do you know any information that you can add to the diagram?

- Are there lengths and areas that you can work out?

Further suggestions can be found by working through the questions below:

| Find \(p\) in terms of \(a\) . Solution As this is a unit circle the hypotenuse of the triangle is \(1\) . Therefore \(p = \sqrt{1-a^2}\) . |  |
|---|---|
| Find \(\theta\) in terms of \(a\) . Solution As we know all three sides of the triangle there are multiple ways we could write the angle, but the simplest way would be to use \(\cos\theta = \frac{a}{1}\) which means \(\theta = \arccos{a}.\) |  |
| Find \(\phi\) and the shaded area in terms of \(a\) and \(b\) . It will be helpful to find the area of the sector using radians rather than degrees. Solution We already know one angle marked in the digram below, \(\arccos a.\) The other can be found in the same way and is \(\arccos b.\) Therefore \(\phi = \arccos a - \arccos b\) . The area of a sector \(= \frac{1}{2}r^2\theta,\) and \(r = 1\) , so the area is \(\frac{1}{2}(\arccos a - \arccos b).\) |  |

## Solution

Firstly we might notice that the diagram has an area shaded between lines which could be \(x=a\) and \(x = b\), so this could be represented by an integral between \(a\) and \(b\). The curve appears to be a semicircle with radius \(1\). A unit circle has equation \(x^2 + y^2 = 1\), but if this is rearranged to find \(y\) then we get \(y = \pm\sqrt{1-x^2}\). The positive root, gives us a semicircle above the \(x\)-axis as all the \(y\)-values must be positive. Therefore the shaded area is represented by the integral \[\displaystyle{\int_a^b \sqrt{1-x^2} \, dx},\] which we have already worked out using the substitution \(x = \cos \theta\) to get \[\displaystyle{\int_a^b \sqrt{1-x^2} \, dx} = \frac{1}{2}b\sqrt{1-b^2} - \frac{1}{2}\arccos b - \frac{1}{2}a\sqrt{1-a^2} + \frac{1}{2}\arccos a.\]

**Finding the area with geometry**

As it is part of a semicircle, we can break the area down into more familiar shapes. We can find the area of the triangle and the sector shaded below.

The green triangle has area \(\frac{1}{2}b\sqrt{1-b^2}\) and the orange sector has area \(\frac{1}{2}(\arccos a - \arccos b)\), (to see why, look at the [suggestion](https://undergroundmathematics.org/chain-rule/circular-slice/suggestion) section). We can also find the area of the triangle with base \(a\) which is \(\frac{1}{2}a\sqrt{1-a^2}\).

The total area is found by adding the orange sector and the green triangle with base \(b\), then subtracting the triangle with base \(a\). This gives us \[\frac{1}{2}b\sqrt{1-b^2} + \frac{1}{2}(\arccos a - \arccos b) - \frac{1}{2}a\sqrt{1-a^2}.\]

The geometric pieces can be thought about in a number of ways. You might have started from the answer of the integral which can be written in the form \[\displaystyle{\int_a^b \sqrt{1-x^2} \, dx} = F(b) - F(a),\] where \(F(b) = \frac{1}{2}b\sqrt{1-b^2} - \frac{1}{2}\arccos b\) and \(F(a) = \frac{1}{2}a\sqrt{1-a^2} - \frac{1}{2}\arccos a.\)

Can you see which areas are represented by \(F(b)\) and \(F(a)\)?
