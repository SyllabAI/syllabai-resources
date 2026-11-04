---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/index-issues
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: index-issues
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 7665
  old_site_id: A4_RT11_2
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-algebra
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-algebra
    validation_status: SUGGESTED
  spec_points:
  - code: E2.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Equations designed to surface what fractional and negative indices mean and when they
        are defined — the E2.4.1 register verbatim.
      rationale: 'Canonical UGM title: “Index issues”'
      validation_status: SUGGESTED
  - code: E2.4.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Equations designed to surface what fractional and negative indices mean and when they
        are defined — the E2.4.1 register verbatim.
      rationale: 'Canonical UGM title: “Index issues”'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-19
---

# Index issues

> Excerpt: This is a set of equations designed to help students think about what fractional and negative indices mean, and when they are or are not defined. Students will practise their manipulation of indices as they work through the questions.

## Problem

\(\sqrt{x}\) or \(x^{\frac{1}{2}}\)? Whichever we prefer, we need to be comfortable working with indices and roots in either form.

Below is a series of equations, for which you should think about the following questions.

For what values of \(x\) and \(y\) do these statements make sense?

What are the possible values for the expressions?

1. \((xy)^\frac{1}{2}=x^\frac{1}{2}y^\frac{1}{2}\)
2. \((xy)^{\frac{5}{3}}=x^{\frac{5}{3}}y^{\frac{5}{3}}\)
3. \((xy)^{\frac{2}{3}}=x^{\frac{2}{3}}y^{\frac{2}{3}}\)
4. \((xy)^{-\frac{1}{2}}= x^{-\frac{1}{2}}y^{-\frac{1}{2}}\)
5. \((xy)^\frac{1}{2} = x^\frac{1}{3}y^\frac{2}{3}\)
6. \((xy)^{-2}= x^{2}y^{2}\)
7. \(\left(\frac{x}{y}\right)^{-\frac{1}{3}} = x^{-\frac{1}{3}}y^{\frac{1}{3}}\)
8. \(\left(\frac{x}{y}-\frac{1}{y}\right)^{\frac{1}{2}}= y^{-\frac{1}{2}}(x-1)^\frac{1}{2}\)

- Try specific values of \(x\) and \(y\)
- What is the difference between the values you can square root and the values you can cube root?

**Suggestion**

## Solutions

Is the left-hand side the same as the right-hand side?

\((xy)^\frac{1}{2}= \sqrt{xy} = \sqrt{x}\sqrt{y} = x^\frac{1}{2}y^\frac{1}{2}\)

It would seem so from the reasoning above, however what happens if \(x = -2\) and \(y = -8\)? \(\sqrt{xy}\) will give us an answer of \(4\) but \(\sqrt{x}\sqrt{y}\) will not be defined.

We can only get a real value from a square root when the number is not negative, so \(x≥0\) and \(y≥0\).

The overall value of the expression \((xy)^\frac{1}{2}\) (and therefore \(x^\frac{1}{2}y^\frac{1}{2}\)) will also be \(≥ 0\).

We have said that the value of the expressions \((xy)^\frac{1}{2}\) and \(x^\frac{1}{2}y^\frac{1}{2}\) will be \(≥ 0\). But will they always be positive? We may think not, as a square root has two solutions: a positive and a negative one.

However, the square root symbol \(\sqrt{}\), and writing something as raised to the power of \(\frac{1}{2}\), denotes the *principal* root, which is always the positive root. If we take a square root, as part of rearranging an equation then we may need to write \(\pm\sqrt{}\) or \(\pm(\quad)^\frac{1}{2}\) depending on the situation.

Can you think of an equation which involves taking a square root where you will always want the positive root only?

\((xy)^{\frac{5}{3}} = \left(\sqrt[3]{xy}\right)^5 = \left(\sqrt[3]{x}\right)^5 \left(\sqrt[3]{y}\right)^5 = x^{\frac{5}{3}}y^{\frac{5}{3}}\)

Is there anywhere this chain of reasoning breaks down? Does it make a difference if we write \(\sqrt[3]{x^5}\) instead of \(\left(\sqrt[3]{x}\right)^5\)?

We can cube root any real value, positive or negative, so \(x, y \in \mathbb{R}\). What values can \((xy)^{\frac{5}{3}}\) take?

1. \((xy)^{\frac{2}{3}}= x^{\frac{2}{3}}y^{\frac{2}{3}}\)

\((xy)^{\frac{2}{3}}= \left(\sqrt[3]{xy}\right)^2 = \left(\sqrt[3]{x}\right)^2 \left(\sqrt[3]{y}\right)^2 = x^{\frac{2}{3}}y^{\frac{2}{3}}\)

We know we can cube root any number, so \(x, y \in \mathbb{R}\). The value of \((xy)^{\frac{2}{3}}\) however, is restricted. How is it different from the value of \((xy)^{\frac{5}{3}}\) and why is that?

A cube root can give a positive or negative answer. Raising a negative to the power of \(5\) (or any odd number), will give you a negative answer so \((xy)^{\frac{5}{3}}\) can take any value. This is unlike \((xy)^{\frac{2}{3}}\), as squaring any number will always result in a positive answer. So \((xy)^{\frac{2}{3}}\) is restricted to being greater than or equal to zero.

**Explanation**

This is similar to the first question. It only involves square roots, so we know \(x\) and \(y\) cannot be negative. What happens to either side of the equation if \(x\) or \(y = 0\)?

On first glance, we might easily dismiss this as being incorrect. The question that was asked though, is ‘for what values of \(x\) and \(y\) do these statements make sense?’ Are there any values of \(x\) and \(y\) when this equation would be true?

If \(x=0\) or \(y = 0\), then the equation is satisfied, but to see if there are any other possibilities we should try to solve this equation.

\[(xy)^\frac{1}{2} = x^\frac{1}{3}y^\frac{2}{3}\]

For the left hand side to be defined, \(xy≥0\). In addition, \(x\) and \(y\) cannot be negative. Can you explain why?

We can write \[x^{\frac{1}{2}}y^{\frac{1}{2}}=x^{\frac{1}{3}}y^{\frac{2}{3}},\]

then divide by \(x^{\frac{1}{3}}y^{\frac{1}{2}}\), assuming \(x,y \neq 0\),to get

\[x^{\frac{1}{6}} = y^{\frac{1}{6}}.\]

Therefore

\[x = y\]

is a solution for \(x, y >0\), along with \(x=0\) or \(y=0\).

This is perhaps more solutions than we might have first thought. Can you see why this happens? Try some numbers if you are not sure.

Once again, this is not true for all values, but may still be true for certain values of \(x\) and \(y\).

It can also be written

\[\dfrac{1}{(xy)^2} = x^{2}y^{2},\]

so we can see that if \(x\) or \(y\) was zero the left-hand side would not exist, therefore \(x,y \neq0\).

We can multiply by \((xy)^{2}\)

\[1= x^4y^4,\]

then take the fourth root. This gives us a positive and negative value so we get

\[1 = xy \text{ or} -1 = xy,\]

giving us the solutions

\[x = \frac{1}{y} \text{ and } x = -\frac{1}{y}.\]

From the \(\left(\frac{x}{y}\right)\) on the left hand side we can see that \(y \neq0\), even though it could be on the right hand side.

On the right hand side we have \(x^{-\frac{1}{3}}\) which is \(\frac{1}{\sqrt[3]{x}}\) and so \(x \neq0\).

Otherwise we can cube root any value so \(x,y \in \mathbb{R}\) except for \(x, y \neq0\) and the value of the expressions can also take any value except \(0\).

On the left hand side we require \(y \neq0\) and \(\frac{x}{y}-\frac{1}{y} ≥ 0\), which implies that \(x ≥ 1\)or \(x≤1\) depending on whether \(y\) is positive or negative.

On the right hand side we have \(y^{-\frac{1}{2}}\) which requires \(y >0\), and \((x-1)^\frac{1}{2}\) which also requires \(x ≥ 1\).

Putting these together gives us \(y >0\) and \(x≥1\) and the value of either side of the equation must be \(≥0\).

Remember that although square rooting something gives us a positive and negative solution, the notation of ‘to the power of \(\frac{1}{2}\)’ denotes the *principal root* which is positive.
