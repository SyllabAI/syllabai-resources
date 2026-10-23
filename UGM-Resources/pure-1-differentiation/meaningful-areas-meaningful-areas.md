---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/meaningful-areas
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/investigation
- level/developing
resource_identity:
  ugm_id: meaningful-areas
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 7
  resource_type_label: Investigation
  level: Developing
  ref: 6999
  old_site_id: C3_RT9_1
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
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/calculus-of-powers/meaningful-areas/download/teacher-notes.pdf
  kind: printable
---

# Meaningful areas

> Excerpt: Students are asked to find the areas of regions between the graphs of a set of functions. This can be done by integration but we explore a variety of other techniques that can be used and make connections with other areas of mathematics.

## Problem

In [Curve match](https://undergroundmathematics.org/thinking-about-functions/curve-match) we asked you to match the curves on the diagram below with the following functions.

\[y=\sqrt{x} \quad y=x^2 \quad y=x \quad y=\dfrac{x^2+x}{2} \quad \text{and } \quad y=2\sqrt{x}-x\]

Now we’d like you to look at the different regions enclosed by the curves.

- Which do you think is the smallest region? How can you check?

- How big are the other regions?

- Try to explain why certain regions are the size they are.

Think about what techniques you can use and how you can reduce the number of calculations you need to do.

You might find it helpful to start by matching the curves, or you could check this in [Curve match](https://undergroundmathematics.org/thinking-about-functions/curve-match).

## Things you might have noticed

In [Curve match](https://undergroundmathematics.org/thinking-about-functions/curve-match) we asked you to match the curves on the diagram below with the following functions.

\[y=\sqrt{x} \quad y=x^2 \quad y=x \quad y=\dfrac{x^2+x}{2} \quad \text{and } \quad y=2\sqrt{x}-x\]

Now we’d like you to look at the different regions enclosed by the curves.

- Which do you think is the smallest region? How can you check?

Think about what techniques you can use and how you can reduce the number of calculations you need to do.

Which curve is which?

Details of how you can work this out can be found in [Curve match](https://undergroundmathematics.org/thinking-about-functions/curve-match), but from top to bottom we have \(y = 2\sqrt{x} - x\), then \(y = \sqrt{x}\), then \(y = x\), then \(y = \dfrac{x^2 + x}{2}\), and finally \(y = x^2\) at the bottom.

It looks as if the region between \(y=\dfrac{x^2+x}{2}\) and \(y=x^2\) or the region between \(y=x\) and \(y=\dfrac{x^2+x}{2}\) could be the smallest, but it’s difficult to tell which is smaller just by looking.

One way to check which region is smaller is to use integration to find the areas. In order to find the area enclosed by \(y=\dfrac{x^2+x}{2}\) and \(y=x^2\) we could first find the area under \(y=\dfrac{x^2+x}{2}\), the upper boundary of the region, and subtract the area under the \(y=x^2\), the lower boundary of the region we want. However, because integration is [linear](https://undergroundmathematics.org/glossary/linear-operator), we could instead integrate the difference beween the two functions, as follows.

\[\int_{0}^{1} \dfrac{x^2+x}{2} -x^2\, dx = \int_{0}^{1} \dfrac{x-x^2}{2}\, dx = \int_{0}^{1} \dfrac{x}{2}-\dfrac{x^2}{2}\, dx = \left[ \dfrac{x^2}{4}-\dfrac{x^3}{6}\right]_{0}^{1} = \left(\dfrac{1}{4}-\dfrac{1}{6}\right) = \dfrac{1}{12}\]

Similarly, the area of the region between \(y=x\) and \(y=\dfrac{x^2+x}{2}\) is given by

\[\int_{0}^{1} x-\dfrac{x^2+x}{2}\, dx = \int_{0}^{1} \dfrac{x-x^2}{2}\, dx\]

What does this tell you? Can you explain it?

You may have found that the areas of regions in the diagram can be found in several ways. We will illustrate a few of these here.

Using symmetry

Now that we know the size of the blue and purple regions, we can do some calculations based on symmetry.

For example, we know that \(y=\sqrt{x}\) and \(y=x^2\) (for the section of the graph shown) are reflections of each other in the line \(y=x\) because they are the graphs of inverse functions. Therefore the area between \(y=\sqrt{x}\) and \(y=x\) is the same as the area between \(y=x\) and \(y=x^2\), which is the sum of the areas of the blue and purple regions.

Using composite shapes

From the diagram we can see that the area of the region between \(y=x\), the \(x\)-axis and the line \(x=1\) is \(\tfrac{1}{2}.\) Therefore the area between \(y=x^2\) and the \(x\)-axis is \(\tfrac{1}{3}.\)

Using means

We used symmetry about the line \(y=x\) to calculate the area of the region between \(y=\sqrt{x}\) and \(y=x.\) Even though \(y=2\sqrt{x}-x\) and \(y=\sqrt{x}\) are not the graphs of inverse functions, we can use a symmetry-based argument to explain why the region between \(y=2\sqrt{x}-x\) and \(y=\sqrt{x}\) is the same size as the region between \(y=\sqrt{x}\) and \(y=x.\) In this case, we are using symmetry about a mean value, and the following diagram illustrates these two uses of symmetry.

Can you use this idea to explain why the region between \(y=x\) and \(y=\dfrac{x^2+x}{2}\) is the same size as the region between \(y=\dfrac{x^2+x}{2}\) and \(y=x^2\)?

It is worth noting that by using symmetry in various forms we have been able to find the areas of all the regions enclosed by the curves by only doing one integral.

Would we still be able to do this if we started by finding a different integral?

**Further things to investigate**

- The area of the region between \(y=x^2\), the \(x\)-axis and the line \(x=1\) is \(\tfrac{1}{3}.\) Can we find a function whose graph splits this region into areas of \(\tfrac{1}{6}\)?

- Can you find other functions whose graphs pass through \((0,0)\) and \((1,1)\) and bound regions of area \(\tfrac{1}{12}\)?

The curves in this problem all pass through \((0,0)\) and \((1,1).\) This made calculating the definite integrals quite simple. How do you think our use of symmetry, means and composite shapes would have been affected if the curves didn’t all meet at these points? What if we only wanted to know about regions from \(x=0\) to \(x=\tfrac{1}{2}\)?
