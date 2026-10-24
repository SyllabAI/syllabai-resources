---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/to-log-or-not-to-log
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/problem-requiring-decisions
- level/developing
resource_identity:
  ugm_id: to-log-or-not-to-log
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 6
  resource_type_label: Problem requiring decisions
  level: Developing
  ref: 5413
  old_site_id: "A4_RT8_1"
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
  - code: 3.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "equations sorted by solve method: 3^x=81 by inspection, 3^x=43 by logarithms, 5^{2x}-5^x=... by substitution - 'just because there is an exponential, you don't always have to use logarithms'; the method-decision task for indicial equations (flips the lane-9 nonOverlapByReference row of record)"
      rationale: "Canonical UGM title: To log or not to log?"
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

# To log or not to log?

> Excerpt: Students are asked to sort a collection of equations (involving exponentials) according to the tools and methods required to solve them. Just because there is an exponential, you don't always have to use logarithms...

## Problem

Some equations involving powers or indices can be solved using logarithms… but not all.

Think about how you could go about solving the following equations. Sort them according to the tools or methods you would use.

\(3^x=81\)

\(x^5=50\)

\(3^x=43\)

\(5^{2x}-5^x-6=0\)

\(5^x+4^x=8\)

\(5^x+2\times5^{1-x}=7\)

\(3^{2x}-3=24\)

\(2^{2x}-9\times2^x+8=0\)

\(\sqrt{2x-3}=5\)

\(5^x-x^5=3\)

\(16^{\frac{3}{x}}=8\)

\(\left(\dfrac{13}{16}\right)^{3x}=\dfrac{3}{4}\)

You might find it helpful to have the equations [printed on cards](https://undergroundmathematics.org/exp-and-log/to-log-or-not-to-log/components/cards.pdf) that you can rearrange as you sort them.

Can you write some other equations to go in each of your sorting categories?

Possible categories

You could use the following headings to categorise your equations

- Solve using indices

- Solve using logarithms

- Rewrite or rearrange first

- Can’t solve exactly

Alternatively, since some equations may come under more than one heading, you could draw this as a Venn diagram.

## Interactive card sorter

Use this interactive sorter to group the cards according to the tools or methods you would use to solve them. You could use the suggested headings or make your own.

Possible categories

You could use the following headings to categorise your equations

- Solve using indices

- Solve using logarithms

- Rewrite or rearrange first

- Can’t solve exactly

Alternatively, since some equations may come under more than one heading, you could draw this as a Venn diagram.

\(3^x=81\)

\(x^5=50\)

\(3^x=43\)

\(5^{2x}-5^x-6=0\)

\(5^x+4^x=8\)

\(5^x+2\times5^{1-x}=7\)

\(3^{2x}-3=24\)

\(2^{2x}-9\times2^x+8=0\)

\(\sqrt{2x-3}=5\)

\(5^x-x^5=3\)

\(16^{\frac{3}{x}}=8\)

\(\left(\dfrac{13}{16}\right)^{3x}=\dfrac{3}{4}\)

Can you write some other equations to go in each of your sorting categories?

## Solution

Some equations involving powers or indices can be solved using logarithms… but not all.

Think about how you could go about solving the following equations. Sort them according to the tools or methods you would use.

(A) \(3^x=81\)

We know that

\[81=9\times9=3^4\]

so we can say that

\(x=4\)

using only our knowledge of powers of

\(3\)

. Note that we could instead use logarithms to solve this equation,

\[\begin{align*} \log_3{3^x}&=\log_3{81}\\ x&=\log_3{81} \end{align*}\]

so we could classify this equation as “either indices or logarithms”.

(B) \(x^5=50\)

To solve this equation, remember that the inverse of raising to a power is a root or a fractional power. So we can solve it using indices, \[x=50^\frac{1}{5}=\sqrt[5]{50} \text{ .}\]

(C) \(3^x=43\)

This looks very similar to the first equation, but since \(43\) is not an exact power of \(3\) we have to use logarithms if we want an exact solution.

Have a go at estimating the solution.

(D) \(5^{2x}-5^x-6=0\)

The laws of indices tell us that

\(5^{2x}=(5^x)^2\)

so this is a quadratic equation which we can factorise

\[\begin{align*} (5^x)^2-(5^x)-6&=0\\ (5^x-3)(5^x+2)&=0\\ 5^x&=3 \text{ or } -2 \text{ .} \end{align*}\]

Now, \(5^x\) cannot be negative so we have only one solution, for which we shall need logarithms. \[x=\log_5 3\] So we could classify this equation as requiring rearrangement and logarithms.

(E) \(5^x+4^x=8\)

We don’t know a way to solve this exactly. How could we find an approximate solution?

What’s wrong with this?

\[\begin{align*} \log{(5^x+4^x)}&=\log{8}\\ \log{5^x}+\log{4^x}&=\log{8}\\ x\log5+x\log4&=\log8\\ x&=\frac{\log8}{\log5+\log4} \end{align*}\]

(F) \(5^x+2\times5^{1-x}=7\)

It may not be immediately obvious what kind of equation this is, so we want to manipulate it into a more useful form. What can we do to the equation so there is no \(-x\) in the index of the second term?

Solution

We can split the second term,

\[5^{1-x}=5\times5^{-x}\]

and then multiply the equation through by

\(5^x\)

,

\[\begin{align*} (5^x)^2+2\times5\times5^{-x}\times5^x&=7\times5^x\\ (5^x)^2+10&=7\times5^x \end{align*}\]

which is a quadratic in

\(5^x\)

that we can factorise,

\[\begin{align*} (5^x)^2-7(5^x)+10&=0\\ (5^x-2)(5^x-5)&=0\\ 5^x&=2 \text{ or } 5 \text{ .} \end{align*}\]

One of the solutions can now be written down using indices while the other requires logarithms. So we can classify this equation as requiring rearrangement, indices *and* logarithms.

(G) \(3^{2x}-3=24\)

This could be treated as a quadratic in

\(3^x\)

, but a bit of rearrangement reveals a simpler method to solve it.

\[\begin{align*} 3^{2x}&=27\\ 2x&=3 \end{align*}\]

It’s always worth looking for simpler methods before embarking on complicated ones. In this case, gathering the constant terms together was the inviting first step.

(H) \(2^{2x}-9\times2^x+8=0\)

This is another quadratic, this time in \(2^x\).

Solution

\[2^{2x}=(2^x)^2\] so \[(2^x-8)(2^x-1)=0 \text{ .}\]

This can be solved using only rearrangement and indices.

(I) \(\sqrt{2x-3}=5\)

Logarithms are not going to help, but squaring both sides will.

(J) \(5^x-x^5=3\)

This is another example of an equation we don’t know how to solve exactly. We could use a numerical method such as trial and improvement to find an approximate solution.

How many solutions are there? Most numerical methods work best if you know roughly where the solution is. A sketch of \(y=5^x\) and \(y=x^5\) might help.

(K) \(16^{\frac{3}{x}}=8\)

What’s gone wrong here?

\[\begin{align*} 16^{\frac{3}{x}}&=8\\ 2^{\frac{3}{x}}&=1\\ \frac{2^3}{2^x}&=1\\ 2^3&=2^x\\ x&=3 \end{align*}\]

A solution using logarithms

Take the logarithm of both sides and rearrange…

\[\begin{align*} \frac{3}{x}\log16&=\log8\\ x&=\frac{3\log16}{\log8} \text{ .} \end{align*}\]

A solution using indices

Cube root of both sides…

\[16^{\frac{1}{x}}=\sqrt[3]8=2\]

then raise both sides to the power

\(x\)

,

\[\begin{align*} 16^1&=2^x\\ x&=4 \text{ .} \end{align*}\]

Have the two methods given the same answer? Which method do you prefer?

(L) \(\big(\frac{13}{16}\big)^{3x}=\frac{3}{4}\)

We are going to have to use logarithms on this one.

Why would indices not give us a solution?

There is a fundamental difference between equations involving the unknown, \(x\), raised to a fixed power (such as \(x^5\)) and equations involving a constant raised to an unknown power (such as \(5^x\)). How is this difference reflected in the methods required to solve the equations?

Here is a possible arrangement of the equations

Note that we have been a bit imprecise about the meanings of the overlapping regions and about what we mean by rearrangement, so your solution may look quite different.

There are a few equations that look similar but appear on opposite sides of the above diagram. Can you explain why?
