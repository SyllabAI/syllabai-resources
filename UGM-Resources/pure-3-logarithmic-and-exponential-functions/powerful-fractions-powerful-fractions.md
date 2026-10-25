---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/powerful-fractions
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: powerful-fractions
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 8042
  old_site_id: "A1_RT12_2"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: thinking-about-algebra
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-algebra
    validation_status: SUGGESTED
  spec_points:
  - code: 3.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "(10^a+1)/(10^a+2) vs (10^b+1)/(10^b+2) - inequality comparison of fractions with the unknown in the index; monotonicity of 10^x drives the answer; prior routing of record: lane-5 '2.2'"
      rationale: "Canonical UGM title: Powerful fractions"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-10
---

# Powerful fractions

> Excerpt: Students are asked to compare algebraic fractions involving indices. Alongside practising their manipulation skills there are different approaches to the problem that can give students an opportunity to develop different ways of thinking.

## Problem

Two fractions are shown below.

\[\textrm{Fraction} \ A: \frac{10^a +1}{10^a +2} \qquad \textrm{Fraction} \ B: \frac{10^b + 1}{10^b + 2}\]

For what values of \(a\) and \(b\) will fraction A be greater than fraction B?

How might your thinking change if instead we had these two fractions?

\[\textrm{Fraction} \ C: \frac{10^c +1}{10^c -1} \qquad \textrm{Fraction} \ D: \frac{10^d + 1}{10^d -1}\]

For what values of \(c\) and \(d\) will fraction C be greater than fraction D?

## Suggestion

What happens when you substitute values in place of \(a\) and \(b\)?

Think about \(a=0\) and \(b=1\), giving the fractions \[A: \frac{10^0 +1}{10^0 +2} \qquad B: \frac{10^1 +1}{10^1 +2}.\]

Which fraction has the bigger result in this situation?

What happens when you substitute different values in place of \(a\) and \(b\)?

- Which fraction has the bigger result in each case?

How do the numerators and denominators of the two fractions compare?

- What is the same and what’s different?

- How could you use any similarities to help you to simplify the problem?

Could you take an approach based on inequalities?

## Solution part 1

In order to compare two fractions, they need to have the same denominator. In this case we could multiply the two denominators together to give a common denominator of \((10^a + 2)(10^b +2)\).

Writing each fraction with this common denominator we get \[\textrm{Fraction} \ A: \frac{10^a +1}{10^a + 2}=\frac{(10^a + 1)(10^b + 2)}{(10^a+2)(10^b + 2)}\] and \[\textrm{Fraction} \ B: \frac{10^b + 1}{10^b + 2}=\frac{(10^b+1)(10^a+2)}{(10^b+2)(10^a+2)}.\]

Is this common denominator, \((10^a+2)(10^b+2)\), a positive or negative quantity?

- Does it depend on the values of \(a\) and \(b\)?

- Does it make a difference to our next steps when we come to compare the two fractions?

We can now compare \[\textrm{Numerator} \ A: (10^a + 1)(10^b + 2) \quad \textrm{and} \quad \textrm{Numerator} \ B: (10^b +1)(10^a+2).\]

There are several ways in which we could do this. One strategy might be to expand the brackets and compare the terms \[\textrm{Numerator} \ A: (10^a+1)(10^b+2)=10^{a+b}+2\times10^a + 10^b + 2\] and \[\textrm{Numerator} \ B: (10^b+1)(10^a+2)=10^{a+b}+2\times10^b+10^a+2.\]

Only the middle terms differ so if we consider this part of the numerator of \(A\): \[C: 2\times10^a+10^b\] and the equivalent part of the numerator of \(B\): \[D: 2\times10^b+10^a.\]

If \(a>b\) then in expression C the first term will dominate and in expression D the second term will dominate. Since the first term of C is double the second term in D, expression C must be greater.

Similarly, if \(b>a\) then in expression C the second term will dominate and in expression D the first term will dominate. Since the first term of D is double the second term of C expression D must be greater.

This means that overall if \(a>b\) then \[\textrm{Fraction} \ A > \textrm{Fraction} \ B\] and if \(b>a\) then \[\textrm{Fraction} \ B > \textrm{Fraction} \ A.\]

We could have reached this solution more quickly if we had noticed at the above expressions (showing the differing middle terms) can be reduced to \[C: 10^a \quad D: 10^b.\]

Thinking about this graphically we see that \(10^x\) is an increasing function and so fraction A will be greater than fraction B when \(a>b\).

We should check that this makes sense when we substitute values in place of \(a\) and \(b\). Substituting \(a=1\) and \(b=0\) into fractions A and B gives \[A: \frac{10^1+1}{10^1+2} = \frac{11}{12}\] and \[B: \frac{10^0+1}{10^0+2} = \frac{2}{3}.\]

Then we can show that \(\frac{11}{12}>\frac{2}{3}\) and our solution holds.

An inequalities approach

We could have approached this question slightly differently if we had started from the initial requirement that fraction A is greater than fraction B.

Writing this as an inequality we have \[\frac{10^a + 1}{10^a + 2} > \frac{10^b + 1}{10^b + 2}.\]

Multiplying through by each denominator in turn we obtain the inequality \[(10^a + 1)(10^b + 2) > (10^b + 1)(10^a + 2).\]

We seem to have assumed that both denominators are positive here.

- Is this always the case?

- What would change if one or both of the denominators were in fact negative?

Expanding the brackets on either side of the inequality gives us \[10^{a+b} + 2 \times 10^a + 10^b > 10^{a+b} + 10^a + 2 \times 10^b\] which can be simplified to \[10^a > 10^b.\]

If we remember that \(10^x\) is an increasing function then we know that for fraction A to be greater than fraction B we require that \(a>b\).

## Solution part 2

If we take a step back and compare this pair of fractions to the first pair we will hopefully notice that it is only the denominators that have changed.

- The second term in each denominator has changed from \(+2\) to \(-1\).

How does this affect the value of the denominator?

In the first example the denominator was always positive. Is this still the case?

We might try to substitute values in place of \(c\) and \(d\) in order to get a sense of what is happening. There are four scenarios that we will need to consider:

1. What happens if both \(c\) and \(d\) are positive?

---

1. What happens if both \(c\) and \(d\) are negative?

---

1. What happens if just one of \(c\) or \(d\) is positive?

---

1. What happens if \(c\) or \(d\) is zero?

Now we might choose to take a similar approach as for the first pair of fractions. Re-writing this pair of fractions with a common denominator we have \[\textrm{Fraction} \ C: \frac{(10^c +1)(10^d - 1)}{(10^c -1)(10^d -1)} \qquad \textrm{Fraction} \ D: \frac{(10^d + 1)(10^c - 1)}{(10^d -1)(10^c - 1)}.\]

If either \(c\) or \(d\) is zero then the fractions are undefined (the denominator will be zero). For each of the other scenarios we might first consider whether or not the resulting fraction is positive or negative:

| Scenario | Sign of fraction \(C\) | Sign of fraction \(D\) | Conclusion |
|---|---|---|---|
| \(c>0\) , \(d>0\) | \(\dfrac{(+)(+)}{(+)(+)}=+\) | \(\dfrac{(+)(+)}{(+)(+)}=+\) | Inconclusive |
| \(c<0\) , \(d<0\) | \(\dfrac{(+)(-)}{(-)(-)}=-\) | \(\dfrac{(+)(-)}{(-)(-)}=-\) | Inconclusive |
| \(c>0\) , \(d<0\) | \(\dfrac{(+)(-)}{(+)(-)}=+\) | \(\dfrac{(+)(+)}{(+)(-)}=-\) | Fraction \(C\) > Fraction \(D\) |
| \(c<0\) , \(d>0\) | \(\dfrac{(+)(+)}{(-)(+)}=-\) | \(\dfrac{(+)(-)}{(-)(+)}=+\) | Fraction \(C\) < Fraction \(D\) |

This means that we only need to investigate the first two scenarios. In both cases the denominators will be positive and so we can consider the numerators alone: \[\textrm{Numerator} \ C: (10^c + 1)(10^d - 1) = 10^{c+d} - 10^c + 10^d - 1\] and \[\textrm{Numerator} \ D: (10^d + 1)(10^c - 1) = 10^{c+d} + 10^c - 10^d - 1.\]

As before, it is only the middle terms which differ so we consider this part of the numerator of \(C\): \[10^d - 10^c\] and the equivalent part of the numerator of \(D\): \[10^c - 10^d.\]

Now, if \(c>0\) and \(d>0\) then fraction \(C\) will be greater than fraction \(D\) when \(d>c\).

We should check this makes sense. If we take \(c=1\) and \(d=2\) then we get \[\textrm{Fraction} \ C: \frac{10^1 + 1}{10^1 - 1} = \frac{11}{9}\] and \[\textrm{Fraction} \ D: \frac{10^2 + 1}{10^2 - 1} = \frac{101}{99}.\]

We can use equivalent fractions to show that \(\dfrac{11}{9} > \dfrac{101}{99}\) and our solution holds.

If \(c<0\) and \(d<0\) then fraction \(C\) will again be greater than fraction \(D\) when \(d>c\).

Once again, we should check that this makes sense. If we take \(c=-2\) and \(d=-1\) then we get \[\textrm{Fraction} \ C: \frac{10^{-2} + 1}{10^{-2} - 1} = -\frac{101}{99}\] and \[\textrm{Fraction} \ D: \frac{10^{-1} + 1}{10^{-1} - 1} = -\frac{11}{9}.\]

We can show that \(-\dfrac{101}{99} > -\dfrac{11}{9}\) and our solution holds.

A summary of our conclusions is below, relating the original scenarios proposed.

| Question | Answer |
|---|---|
| What happens if both \(c\) and \(d\) are positive? | Fraction \(C\) > Fraction \(D\) when \(d>c\) |
| What happens if both \(c\) and \(d\) are negative? | Fraction \(C\) > Fraction \(D\) when \(d>c\) |
| What happens if just one of \(c\) or \(d\) is negative? | Fraction \(C\) > Fraction \(D\) when \(c>0\) and \(d<0\) |
| What happens if \(c\) or \(d\) is zero? | Fraction \(C\) or Fraction \(D\) respectively will be undefined. |

We might like to think of this problem graphically.

We can see that \(y=\dfrac{10^x + 1}{10^x - 1}\) is decreasing on the interval \((-\infty, 0)\) and also on \((0, \infty)\) (this is in contrast to the first problem in which the function was increasing).

Think about how each of the four questions posed above relates to regions of the graph.
