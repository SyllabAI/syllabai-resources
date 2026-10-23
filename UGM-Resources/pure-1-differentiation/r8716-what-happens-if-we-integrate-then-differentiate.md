---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r8716
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r8716
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8716
  old_site_id: Q210
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2010, Q1I
task: T-UGM-IMPORT-7
---

# What happens if we integrate, then differentiate?

## Question

For a positive number \(a\), let \[I(a) = \int_0^a \! \left(4 - 2^{x^2} \right) \, dx.\]

Then \(\dfrac{dI}{da}=0\) when \(a\) equals

1. \(\dfrac{1 + \sqrt{5}}{2}\),

---

1. \(\sqrt{2}\),

---

1. \(\dfrac{\sqrt{5} - 1}{2}\),

---

1. \(1\).

## Suggestion

We are looking for the stationary point of \(I\). What does this mean geometrically?

As \(a\) increases, for which points does \(I(a)\) increase and for which points does it decrease? What does this tell us about where the stationary points have to lie?

## Solution

For a positive number \(a\), let \[I(a) = \int_0^a \! \left(4 - 2^{x^2} \right) \, dx.\]

Then \(\dfrac{dI}{da}=0\) when \(a\) equals

1. \(\frac{1 + \sqrt{5}}{2}\),

---

1. \(\sqrt{2}\),

---

1. \(\frac{\sqrt{5} - 1}{2}\),

---

1. \(1\).

**Approach 1**

We want to find a stationary point of \(I(a)\), though it may not be clear exactly how to differentiate an expression in this form. As \(I(a)\) is the (signed) area of the curve above the \(x\)-axis between \(0\) and \(a\), we want to find a point in which the area is neither increasing nor decreasing.

Let \(f(x) = 4 - 2^{x^2}\), so that \(I(a) = \int_0^a f(x) \, dx\). Then if \(f(a)>0\), the area must increase if \(a\) increases by a small amount. Similarly if \(f(a)<0\), the area must decrease. This is by considering that the new areas added will be entirely above and entirely below the \(x\)-axis in each case respectively. This picture also tells us that the rate at which the area changes is smallest when \(f(a)\) is smallest. Therefore, the stationary points must occur when \(f(a)=0\).

So \(\frac{dI}{da}= 0\) when \(4- 2^{a^2} = 0\). Hence \(a^2 = 2\), which gives that \(a = \sqrt{2}\) (as \(a\) is positive).

Therefore the answer is (b).

**Approach 2**

We may recall that, in many ways, integration can be seen as the opposite of differentiation. Therefore we may initially guess that \(\frac{dI}{da}= 4- 2^{a^2}\). To show that this is true, suppose that \(4-2^{x^2}\) integrates to the function \(F(x)\). That is, \(F\) is the function satisfying \(F'(x)=4-2^{x^2}\). Then we have that

\[I(a) = \int_0^a \! \left(4 - 2^{x^2} \right) \, dx = \bigl[ F(x) \bigr]_0^a = F(a) - F(0)\]

and so

\[\frac{dI}{da}= F'(a) = 4- 2^{a^2}\]

as \(F(0)\) is a constant. Hence the derivative is \(0\) when \(a=\sqrt{2}\), similarly to above.

As before, the answer is (b).

In the two arguments above, you may not be completely convinced by some of the assertions that have been made. For example, in the first approach, we asserted that if \(f(a)>0\), then the area must increase if \(a\) increases by a small amount. What if \(f\) decreases very quickly? Would there always be some amount by which we can increase \(a\) so that the area still increases? In the second approach, if we cannot write down an expression for the integral \(F(x)\) explicitly, must it always exist? This result is known as the [fundamental theorem of calculus](https://undergroundmathematics.org/glossary/fundamental-theorem-of-calculus) and is explored when studying mathematics at university.
