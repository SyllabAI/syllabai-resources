---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/integral-chasing
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/fluency-exercise
- level/developing
resource_identity:
  ugm_id: integral-chasing
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 8245
  old_site_id: C2_RT11_1
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
- path: https://undergroundmathematics.org/calculus-of-powers/integral-chasing/download/teacher-notes.pdf
  kind: printable
---

# Integral chasing

> Excerpt: Students work out four definite integrals, giving results in terms of unknowns whose values can then be determined. The task offers lots of practice of algebra skills and integration together.

## Problem

Below is a selection of integrals, some of which you cannot do without performing others first and some that require the use of other mathematical skills.

Can you find the missing positive numbers \(a\) to \(d\)?

\[\text{(1)} \ \int_a^5 10x+3 \, dx = 114\]

\[\text{(2)} \ \int_{2a}^9 b\sqrt{x}+\dfrac{a}{\sqrt{x}}\, dx=42\]

\[\text{(3)} \ \int_{\frac{1}{2}}^1 \dfrac{1}{x^5}-\dfrac{1}{x^2} \, dx=\dfrac{c+1}{4}\]

\[\text{(4)} \ \int^{c+2}_6 x^{\frac{b}{a}}\left(\sqrt{x}-\dfrac{1}{\sqrt{x}}\right) \, dx=ab^ad^a\]

Test your solution

*Once you have found the missing positive numbers \(a\) to \(d\), can you use them in the statement below to test your values?*

The area formed by the \(x\)-axis, the lines \(x=b\) and \(x=d\), and the curve \(y=(x-2a)(x+1)\) is \(\dfrac{cd}{a(a+b)}\).

Remember, when we are looking at *area*, what must we check about the curve between the lines \(x=b\) and \(x=d\) when it is plotted?

## Solution

We have four integrals to look at, but only two of them contain just one of the letters—(1) and (3).

We could start with the first integral,

\[\text{(1)} \ \int_a^5 10x+3 \, dx = 114.\]

We can see that the value the integral takes is positive, so we have an area formed between \(10x+3\) and the \(x\)-axis.

This can only happen when \(0<a<5\), since \(a\) is also positive. We now have a good feeling for the sort of value for \(a\) we are looking for.

If we perform the integration we get the following,

\[\text{(1)} \ \int_a^5 10x+3 \, dx = \left[5x^2+3x \right]^5_a = (5\times 5^2+3\times 5)-(5a^2+3a) = 114.\]

Simplifying the above we find that,

\[\begin{align*} 140-5a^2-3a &=114\\ \implies 5a^2+3a-26 &=0 \end{align*}\]

The prime factor decomposition of \(26\) is \(2\times 13\). Trying the possible combinations leads us to \((5x+13)(x-2)\). Given that \(a\) is positive, we must have \(a=2\).

Is this sensible?

Well, we thought above that \(0<a<5\) and we have found a value that fits with this.

Which integral could we tackle next?

Integral 2

For this integral it is a good idea to rewrite the integrand and we can also fill in the value for \(a\).

\[\int_{2a}^9 b\sqrt{x}+\dfrac{a}{\sqrt{x}}\, dx= \int_{4}^9 bx^{\frac{1}{2}}+2x^{-\frac{1}{2}} \, dx.\]

Why is it helpful that \(9\) and \(4\) are the numbers we require to substitute in?

Performing the integration and solving a linear equation in \(b\), we find that \(b=3\).

Integral 3

This integral does not depend on any of the unknowns. It is again useful to rewrite the integrand.

\[\int_{\frac{1}{2}}^1 \dfrac{1}{x^5}-\dfrac{1}{x^2} \, dx=\int_{\frac{1}{2}}^1 x^{-5}-x^{-2} \, dx.\]

Performing the integration and solving a linear equation in \(c\), we find that \(c=10\).

Integral 4

This equation contains all four of the unknowns so is best kept til last. As before, we start by rewriting the integrand and substituting in the values for \(a\), \(b\) and \(c\).

\[\int^{c+2}_6 x^{\frac{b}{a}}\left(\sqrt{x}-\dfrac{1}{\sqrt{x}}\right) \, dx=\int^{12}_6 x^{\frac{3}{2}}\left(x^{\frac{1}{2}}-x^{-\frac{1}{2}}\right) \, dx=\int^{12}_6 x^2-x \, dx.\]

We can also substitute our values for \(a\), \(b\) and \(c\) into the right hand side of the original equation to give \(ab^ad^a=2\times 3^2\times d^2\).

\[\int^{12}_6 x^2-x \, dx=18d^2.\]

Performing the integration and solving a quadratic equation in \(d\), we find that \(d=5\).

Test your solution - explained

The area formed between the \(x\)-axis and the lines \(x=b\) and \(x=d\), and the curve \(y=(x-2a)(x+1)\) is \(\dfrac{cd}{a(a+b)}\).

To check that we have found the correct values for \(a\), \(b\), \(c\) and \(d\) we can evaluate the integral between the given \(x\) values,

\[\int_b^d (x-2a)(x+1) \, dx=\int_3^5 (x-4)(x+1) \, dx\]

and check it is equal to \(\dfrac{cd}{a(a+b)}=5\).

But we are not told about the *integral*, we are told that the *area* formed between the curve and the \(x\)-axis is \(5\). This means we need to be careful if our curve crosses the \(x\)-axis.

Sketching the curve \(y=(x-4)(x+1)=x^2-3x-4\) reveals that the curve crosses the \(x\)-axis at \(x=4\). So we must separately calculate the areas between the \(x\) values \(3\) and \(4\), and \(4\) and \(5\).

Sketch of curve

The curve \(y=(x-4)(x+1)\)

We can thus split our integral up into two

\[\int_3^4 x^2-3x-4 \, dx,\]

which will give the negative value \(-\dfrac{13}{6}\) and

\[\int_4^5 x^2-3x-4 \, dx,\]

which will give the positive value \(\dfrac{17}{6}\).

Therefore, the total area formed between the curve, the lines \(x=3\) and \(x=5\), and the \(x\)-axis is \(\dfrac{13}{6} + \dfrac{17}{6} = 5\).
