---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/irrational-roots
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: irrational-roots
  station: quadratics
  station_title: Quadratics
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 6573
  old_site_id: A2_RT7_2
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Surd roots via formula; surd manipulation in root conditions.
      rationale: 'Canonical UGM title: “Irrational roots”'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-1
---

# Irrational roots

> Excerpt: This problem offers students the opportunity to think about the solutions to quadratic equations in a more challenging context. Students are given an irrational root and work backwards to find the original quadratic polynomial.

## Problem

The roots of quadratic polynomials can be nice, integer values. For example \(x^2+4x+3\) has \(x=-3\) as a root. However, this is not always the case. You will have encountered many quadratic polynomials with roots that are fractions or even irrational numbers.

Convince yourself that \(x=\sqrt{2}\) is a root of the quadratic equation \(x^2-2=0\) and that \(x=\sqrt{3}\) is a root of the quadratic equation \(x^2-3=0\).

- Can you find a quadratic polynomial with integer coefficients which has \(x=1+\sqrt{2}\) as a root?  What is the other root of this polynomial?
- What if instead \(x=1+\sqrt{3}\) is a root? What would the quadratic polynomial be now?  What would the other root be this time?
- Can you generalise your answers to the case where \(1+\sqrt{n}\) is a root?  What about the case where \(m+\sqrt{n}\) is a root?

---

If you think you need to revisit methods of solving quadratic equations you may like to look at these resources: [Quadratic grids](https://undergroundmathematics.org/quadratics/quadratic-grids) and [Factorisable quadratics](https://undergroundmathematics.org/quadratics/factorisable-quads).

## Suggestion

I know that the quadratic factorises as \((x-(1+\sqrt{2}))\) times something. So perhaps I could write the quadratic as \[(x-(1+\sqrt{2}))(ax+b)\] and work out what \(a\) and \(b\) could be.

Alternatively, perhaps I could think about the relation between \(x=\sqrt{2}\) and \(x^2-2=0\), and see where that leads me to if I start with \(x=1+\sqrt{2}\) instead.

As a third possible approach, I could think about the graph of \(y=x^2-2\), which has \(x=\sqrt{2}\) as a solution, and wonder what I would have to do to get \(x=1+\sqrt{2}\) as a solution instead.

As a fourth approach, since \(x\) involves square roots, I could try squaring it to get \(x^2=3+2\sqrt{2}\). Can I somehow use this together with \(x\) to get rid of the \(\sqrt{2}\) part?

## Solution

#### Approach 1

We can approach this problem by thinking about the factorised form of the quadratic polynomial. If \(x=1+\sqrt{2}\) is a root then we can factorise the original quadratic as \((x-(1+\sqrt{2}))(ax+b)\).

If we expand the factorised form we get \[ax^2+(b-a(1+\sqrt{2}))x-b(1+\sqrt{2}).\]

Now, we know that we are looking for a quadratic with integer coefficients so we know that the constant term, \(-b(1+\sqrt{2})\) must be an integer, say \(n\). If \(-b(1+\sqrt{2})=n\), then \[b=-\frac{n}{1+\sqrt{2}}.\] We can rationalise the denominator by multiplying by \(1-\sqrt{2}\) to get

\[\begin{align*} b &{}=-\frac{n(1-\sqrt{2})}{(1+\sqrt{2})(1-\sqrt{2})} \\ &{}=-\frac{n(1-\sqrt{2})}{1-2} \\ &{}=n(1-\sqrt{2}). \end{align*}\]

We are making use of the *difference of two squares* here. \[(a+b)(a-b)=a^2-b^2\]

This gives us a constant term of \(n\).

We also require that the coefficient of \(x\), \(b-a(1+\sqrt{2})\) is an integer. Substituting our value for \(b\) in here gives \(n(1-\sqrt{2})-a(1+\sqrt{2})\).

For this to be an integer we require that \(a=-n\) so that the surds cancel \[n(1-\sqrt{2})+ n(1+\sqrt{2})=2n.\]

So we have a quadratic polynomial of the form \(-nx^2+2nx+n\) or equivalently, \(nx^2-2nx-n\). In the simplest case this is \(x^2-2x-1\).

The other root of the polynomial will be \(x=1-\sqrt{2}\).

#### Approach 2

When we think about the first example, \(x^2-2=0\), we see that it is just \(x=\sqrt{2}\) squared and then rearranged.

So if we start with \(x=1+\sqrt{2}\), we could just square it, but then we get \(x^2=3+2\sqrt{2}\), which hasn’t really helped us.

But if we rearrange it first to get the square root alone on one side, we have \[x-1=\sqrt{2}.\] This can now be squared to get \[(x-1)^2=2,\] which does the job: expanding the brackets gives \(x^2-2x+1=2\), so \(x^2-2x-1=0\) has \(x=1+\sqrt{2}\) as a root.

Working backwards, we see that \((x-1)^2=2\) gives \(x-1=\pm\sqrt{2}\), so the other root is \(x=1-\sqrt{2}\).

#### Approach 3

When we think about the graph of \(y=x^2-2\), a parabola, we see that it has a root at \(x=\sqrt{2}\) and another one at \(x=-\sqrt{2}\). As we want to have a root at \(x=1+\sqrt{2}\), we can translate this parabola \(1\) unit to the right so that it now has a root at \(\sqrt{2}+1\). This can be achieved if we remember that \(f(x)\rightarrow f(x-a)\) corresponds to a horizontal translation \(a\) to the right. In this case, we begin with \(f(x)=x^2-2\) so that \(f(x-1)=(x-1)^2-2=x^2-2x-1\).

Therefore a quadratic polynomial with \(x=1+\sqrt{2}\) as a root is \(x^2-2x-1\), as with the other two approaches.

The second root of \(f(x-1)\) is \(-\sqrt{2}+1\), as the second root \(-\sqrt{2}\) of the original polynomial is also translated \(1\) unit to the right.

The second root could also have been found using the quadratic formula.

#### Approach 4

We have \(x=1+\sqrt{2}\). When we square this, we get \(x^2=3+2\sqrt{2}\). This might remind us of one method of solving simultaneous equations, where we eliminate variables one at a time.

In this case, if we subtract \(2x\) from \(x^2\), we’ll eliminate the \(\sqrt{2}\): \[x^2-2x=(3+2\sqrt{x})-2(1+\sqrt{x})=1,\] so \(x^2-2x-1=0\), and we have our required polynomial.

We can now find the other root of this quadratic by any standard technique, though it is not clear from this approach what the other root will be.

Which of these four approaches do you prefer?

Which of these four approaches can be most easily adapted to other situations?

---

What if instead \(x=1+\sqrt{3}\) is a root? How would the quadratic polynomial look now? What would the other root be this time?

This is a very similar question to that above. It makes sense that we can use the same approaches.

They all give the answer \(x^2-2x-2=0\), and the other root is \(1-\sqrt{3}\).

Think about how the solutions to the first two questions could inform your answer here. Perhaps think about some other particular cases if you are unsure.

## Taking it further

1. Can you find a polynomial (not necessarily a quadratic) with integer coefficients which has \(\sqrt{2}+\sqrt{3}\) as a root? What other roots (if any) does it have?
2. Can you find a polynomial with integer coefficients which has \(1+\sqrt[3]{2}=1+2^{\frac{1}{3}}\) as a root? What other roots (if any) does it have?
3. Can you find a polynomial with integer coefficients which has \(\sqrt[3]{2}+\sqrt[3]{4}=2^{\frac{1}{3}}+2^{\frac{2}{3}}\) as a root? What other roots (if any) does it have?
4. Can you make up some similar questions to the above?  Are there any numbers for which you *cannot* find a polynomial with integer coefficients which has that number as a root?
