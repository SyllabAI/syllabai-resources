---
created: 2026-10-24T04:45:46 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/additional-integrals
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/package-of-problems
resource_identity:
  ugm_id: additional-integrals
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 7826
  old_site_id: C3_RT6_3
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.8.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-8 cross-map (cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd)"
      evidence: "given definite integrals of f and g over [0,3], evaluate linear combinations, reversed limits and shifted-argument integrals — linearity and order-reversal properties of the definite integral are the tested skill"
      rationale: "Canonical UGM title: \"Additional integrals\"; exam provenance: UCLES Additional Mathematics 1, QP 8175/1, 1985 Q9."
      validation_status: SUGGESTED
    title: "evaluate definite integrals"
  mapped_date: '2026-10-24'
  mapper: cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES Additional Mathematics 1, QP 8175/1, 1985 Q9."
task: T-UGM-IMPORT-8
---

# Additional integrals

> Excerpt: This problem asks students to think about links between two given integrals and other related integrals.

## Problem

Which of the integrals below can be evaluated if we know that

\[\large{\int_0^3 f(x) \ dx = 7 \ \text{and} \ \int_0^3 g(x)\ dx =4\text{?}}\]

\[\int_0^3 (f(x)+2g(x))\ dx\]

\[\int_0^3 f(x)g(x)\ dx\]

\[\int_0^6 f(x) \ dx\]

\[\int_0^3 (g(x)+2) \ dx\]

\[\int_3^0 \!f(x) \ dx \, \times \int^3_0 \!g(x) \ dx\]

\[\int^3_{-3} g(x) \ dx\]

\[\int_{-3}^{3} f(x) \ dx\]

\[\int^2_{-1} f(x+1) \ dx\]

Which of the integrals can be evaluated if we have the following extra information?

1. \(f(x)\) is symmetric about \(x=3\)

---

1. \(g(x)\) is an odd function

---

1. \(f(x)\) is an even function

## Things you might have noticed

Which of the integrals below can be evaluated if we know that

\[\int_0^3 f(x) \ dx = 7 \ \text{and} \ \int_0^3 g(x)\ dx =4\text{?}\]

How are the functions we are being asked to integrate related to \(f(x)\) and \(g(x)\)?

Are the limits of these new integrals the same as the original integrals, or are they related to the original limits in a way that we can make use of?

As you read, you may find it helpful to sketch some possible graphs of the functions involved. You could consider some particular examples that you’re comfortable working with, or try to work with more general sketch graphs of \(f(x)\) and \(g(x).\)

A. \(\int_0^3 (f(x)+2g(x))\ dx\)

The limits for this integral coincide with the ones we are given, so now we need to think about the function \(f(x)+2g(x)\).

Consider the graph of \(y=f(x)+2g(x)\). For any \(x\)-value the corresponding \(y\)-value is the sum of \(f(x)\) and \(2g(x)\). We can think of \(f(x)+2g(x)\) as a sum of heights where the *height* in this case is the \(y\)-coordinate of each of the functions \(y=f(x)\) and \(y=g(x)\), so we can treat the integral of \(f(x)+2g(x)\) as a sum of integrals,

\[\begin{align*} \int_0^3 (f(x)+2g(x))\ dx&=\int_0^3 f(x)\ dx+\int_0^3 2g(x)\ dx\\ &=\int_0^3 f(x)\ dx+\int_0^3 g(x)\ dx+\int_0^3 g(x)\ dx\\ &=7+4+4\\ &=15. \end{align*}\]

Can we make a statement about what this means for integrating \(\int ng(x) \ dx\), where \(n\) is any real number?

B. \(\int_0^3 f(x)g(x)\ dx\)

The limits for this integral coincide with the ones we are given, but since we don’t know anything more about the functions \(f(x)\) and \(g(x)\), we can’t say anything about the function \(f(x)g(x)\) or its integral.

You may find it interesting to compute some definite integrals of functions you can integrate and compare these with the integral of their product over the same interval. Which functions have products that you know how to integrate?

D. \(\int_0^3 (g(x)+2) \ dx\)

The limits for the integral coincide with the ones we are given. If we assume that \(g(x)\) is positive between \(0\) and \(3\) then we can think about this as a calculation of area: we are *adding* \(2\) to the height of the curve for each value of \(x\) in the interval \([0,3]\), so in total we are adding a rectangle of height \(2\) and width \(3\) to the area \(\int_0^3 g(x)\ dx\). Therefore,

\[\int_0^3 (g(x)+2)\ dx=\int_0^3 g(x)\ dx + 6=4+6=10.\]

What happens if \(g(x)\) is negative for some values of \(x\) between \(0\) and \(3\)? Can we still evaluate \(\int_0^3 (g(x)+2)\ dx=\int_0^3 g(x)\ dx + 6\) if that happens?

E. \(\int_3^0 f(x) \ dx \times \int^3_0 g(x) \ dx\)

We know \(\int_0^3 g(x)\ dx=4.\) We also know that \(\int_0^3 f(x)\ dx=7\), but how is this related to \(\int_3^0 f(x)\ dx\)?

By the [Fundamental Theorem of Calculus](https://undergroundmathematics.org/glossary/fundamental-theorem-of-calculus), if the function \(f(x)\) is continuous on the interval \([0,3]\) and \(F'(x)=f(x)\) then

\[\int_0^3 f(x) \ dx=F(3)-F(0).\]

So,

\[\int_3^0 f(x) \ dx=F(0)-F(3)=-(F(3)-F(0))=-\int_0^3 f(x) \ dx=-7.\]

Therefore,

\[\int_3^0 f(x) \ dx \times \int^3_0 g(x) \ dx= -7 \times 4 = -28.\]

H. \(\int^2_{-1} f(x+1) \ dx\)

Here we are integrating over an interval of the same length as before, since \([-1,2]\) is a translation of \([0,3]\) by one unit to the left. This translation of the limits allows us to evaluate the integral \(\int^2_{-1} f(x+1) \ dx\) because the curve has also been translated by one unit in the negative \(x\) direction.

Therefore, \(\int^2_{-1} f(x+1) \ dx = \int^3_0 f(x) \ dx = 7.\)

If \(a\) is any real number and \(\int^{q}_{p} f(x-a) \ dx = 7\), how could \(p\), \(q\) and \(a\) be related? What assumptions are we making about \(f\)?

For the remaining integrals we need more information, but we could try to use the additional pieces of information to help us.

C. \(\int_0^6 f(x) \ dx\)

If \(f(x)\) is symmetric about \(x=3\) then we know, for example, that \(f(4)=f(2)\), \(f(5)=f(1)\) and in general, \(f(3+k)=f(3-k)\) for any real number \(k.\) This means that the line \(x=3\) splits the integral \(\int_0^6 f(x) \ dx\) in half, so \(\int_0^6 f(x) \ dx= 2\int_0^3 f(x) \ dx=14.\)

How could you use manipulation of the limits of the integrals and functions to show that \(\int_0^6 f(x) \ dx = 14\)?

F. \(\int^3_{-3} g(x) \ dx\)

As \(g(x)\) is odd, \(g(-x)=-g(x).\) Therefore \[\int^0_{-3} g(x) \ dx = \int^3_{0} g(-x) \ dx= -\int^3_{0} g(x) \ dx.\] It follows that \(\int^3_{-3} g(x) \ dx=0.\)

How is this argument linked to the symmetry of the graph of \(g(x)\)?

G. \(\int_{-3}^{3} f(x) \ dx\)

As \(f(x)\) is even, \(f(-x) = f(x)\) and the \(y\)- axis is a line of symmetry. We can use a similar argument to the one we used for \(\int_0^6 f(x) \ dx\) to show that \(\int^{3}_{-3} f(x) \ dx = 2\int_0^3 f(x) \ dx = 14.\) Can you combine this with our earlier discussion of translations?

## Taking it further

Based on the ideas in this resource, what other related integrals involving \(f(x)\) and \(g(x)\) can we evaluate if we know that

\[\int_0^3 f(x) \ dx = 7 \ \text{and} \ \int_0^3 g(x)\ dx =4\text{?}\]

What related integrals can we *not* evaluate without knowing more about the functions?
