---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/log-lineup
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/fluency-exercise
- level/developing
resource_identity:
  ugm_id: log-lineup
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 5820
  old_site_id: "A4_RT11_4"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: exp-and-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: exp-and-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "log_4 5, log_2 5, log_3 4, ... ordered without a calculator - exact values and index bounds (3^1<5<3^2); prior routing of record: lane-5 sweepRouting '2.2 Logarithmic and exponential functions'"
      rationale: "Canonical UGM title: Logarithm lineup"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-10
---

# Logarithm lineup

> Excerpt: This can be used as a follow-up to 'Logarithm lattice' or can be used on its own. Students are challenged to arrange a set of log expressions in ascending order.

## Problem

Can you, without using a calculator, arrange these logarithms into order of increasing value?

\[\log_{4} 5 \quad \log_{2} 5 \quad \log_{3} 4 \quad \log_{3} 3 \quad \log_{3} 5 \quad \log_{2} 4 \quad \log_{2} 3\]

Things to think about

- Do you know exact values for any of them?

- Can you find upper and lower bounds for them by comparing with known values?

- Can you compare some of them by thinking about increasing and decreasing functions?

- How might changing the base of logarithms help?

If you have completed [Logarithm lattice](https://undergroundmathematics.org/exp-and-log/log-lattice), you will have put some of these logarithms in order already, but here we explore some different methods.

You might find it helpful to have the logarithms written or [printed on cards](https://undergroundmathematics.org/exp-and-log/log-lineup/components/cards.pdf) that you can rearrange as you sort them.

## Interactive card sorter

\(\log_{4} 5\)

\(\log_{2} 5\)

\(\log_{3} 4\)

\(\log_{3} 3\)

\(\log_{3} 5\)

\(\log_{2} 4\)

\(\log_{2} 3\)

## Things you might have thought about

**Initial observations**

- We can write down exact values for two of these logarithms.

- Since \(\log_3 5\) is the power of \(3\) that would give us \(5\) and \(3^1<5<3^2\) we know the value of \(\log_3 5\) must lie between \(1\) and \(2\). Can you do the same for other logarithms in the list and use the results to put some of them in order?

Logarithms in ascending order so far

**Increasing or decreasing?**

If we take a series of logarithms all with the same base, we might assume that \(\log\) of a bigger number will have a bigger value. In other words, the function \(\log x\) is increasing.

Is this always true, or only for some values of \(x\)? Does it depend on the base of the logarithm?

If it is true for the logarithms in our list, we can use this fact to put some of them in order.

Solution

It is true that the function \(\log x\) is increasing for all values of \(x\) where it is defined, i.e. \(x>0\), as long as the base is greater than \(1\).

What if the base is between \(0\) and \(1\)? For instance, the function \(\log_\frac{1}{2} x\)? Draw the graph or work out some values if you’re unsure.

The logarithms in our list all have bases greater than \(1\), so \[\log_2 3<\log_2 4<\log_2 5\] and \[\log_3 3<\log_3 4<\log_3 5\text{ .}\]

**Changing bases**

If instead, we take a series of logarithms of the same number but to different bases, would these increase or decrease? Think about \(\log_2 8\) and \(\log_4 8\). Can we use this idea to order some of our logarithms?

More generally, we are asking whether the function \(\log_x a\) is increasing or decreasing - does it depend on the value of \(a\)? You could try using graphing software such as [Desmos](https://www.desmos.com/calculator) (find \(\log_a\) on its *functions* menu).

Another way to compare these logarithms of the same number would be to use the rule for changing the base: \[\log_a b=\log_a c \times \log_c b\text{ .}\]

For instance, to compare \(\log_3 5\) and \(\log_4 5\), we could write \(\log_3 5 = \log_3 4\times\log_4 5\) and then note that \(\log_3 4 > 1\), and so \(\log_3 5 > \log_4 5\).

Ascending order diagram

Our network of orderings now looks like this.

**Estimating values**

It is possible to find some other upper and lower bounds within our list of logarithms by using approximations for the square roots of \(2\) and \(3\):

We know that \(2^\frac{1}{2}\approx1.4\), so \(2^\frac{3}{2}=2\times2^\frac{1}{2}\approx2.8\).

Therefore \(\frac{3}{2}\approx\log_2{2.8}\), and hence \(\log_2{3}>\frac{3}{2}\).

Can you use an approximate value of \(\sqrt 3\) to find an upper bound for \(\log_3 5\)?

Solution

We could use the following argument.

\[\begin{align*} 3^\frac{3}{2}&=3\times3^\frac{1}{2}\approx3\times1.7 = 5.1\\ \frac{3}{2}&\approx\log_3{5.1}\\ \log_3{5}&<\frac{3}{2} \end{align*}\]

From this it follows that \(\log_3{5}<\log_2{3}\) which straightens out one more part of our lineup.

**Increasing or decreasing again**

We shall now look at two possible ways of comparing \(\log_3 4\) and \(\log_4 5\) which is the last unknown pairing in our lineup.

Firstly, notice that in each of these remaining logarithms, the base is one less than the number whose logarithm we are taking. We could think of them as values of the function \(\log_x{(x+1)}\). Is this an increasing or decreasing function? Think about its value when \(x=2\) and when \(x\) is very large. You could use [Desmos](https://www.desmos.com/calculator) to explore it.

Solution

This appears to be a decreasing function for \(x>1\) which is the domain we are interested in. When \(x\) gets very large, the value of this function will be very close to \(\log_x {(x)}=1\) and when \(x=2\) its value is \(\log_2 3\) which is certainly bigger than \(1\).

**Different differences**

Another way to compare \(\log_4 5\) and \(\log_3 4\) would be to work out the difference between them, \[d=\log_3 4 - \log_4 5 \text{ .}\] If we can show that the difference is positive then we can put the two logarithms in order.

We can’t work out the difference directly, but we could try the following.

\[\begin{align*} \log_3 4 > \log_4 4 = 1\\ \text{so, } d>1-\log_4 5\\ \text{but, } \log_4 5>1 \end{align*}\]

This looked promising but it has only told us that \(d\) is greater than some negative number, so it is not helpful in this case.

We can rewrite the expression without changing its value:

\[\begin{align*} d&=(\log_3 4 -1)-(\log_4 5 -1)\\ &=(\log_3 4 - \log_3 3)-(\log_4 5 -\log_4 4) \end{align*}\]

Can you use the subtraction law of logarithms to rearrange this and show that \(d>0\)?

Solution

We can complete the argument like this:

\[\begin{align*} d&=(\log_3 4 - \log_3 3)-(\log_4 5 -\log_4 4)\\ &=\log_3 {\frac{4}{3}}-\log_4 {\frac{5}{4}} \end{align*}\]

Now,

\(\log_4 {\frac{5}{4}} < \log_3 {\frac{5}{4}}\)

because

\(\log_x {\frac{5}{4}}\)

is a decreasing function for

\(x>1\)

. Therefore,

\[\begin{align*} d&>\log_3 {\frac{4}{3}}-\log_3 {\frac{5}{4}}\\ &=\log_3 {\Big(\frac{\big(\frac{4}{3}\big)}{\big(\frac{5}{4}\big)}\Big)}\\ &=\log_3 {\big(\frac{16}{15}\big)}\\ &>0 \end{align*}\]

So now we *have* shown that \(d\) is positive, so we can put the two original logarithms in order.

Sometimes, adding zero can help you solve a problem! You may wonder how we knew that subtracting one from each side would help. The answer is that we didn’t know, but…

Looking at this numberline fragment, we already knew the two logarithms were between \(1\) and \(2\). By subtracting the ones, we have effectively compared the two red dotted lengths rather than the two blue dashed lengths. What is it that makes that feel like a worthwhile thing to do?

We have shown alternative methods for some steps of the argument. What are the advantages and disadvantages of the different methods?

Final solution

Finally we have a complete lineup of logarithms.

Can you add some more logarithms to the list and use similar techniques to insert them in the lineup?
