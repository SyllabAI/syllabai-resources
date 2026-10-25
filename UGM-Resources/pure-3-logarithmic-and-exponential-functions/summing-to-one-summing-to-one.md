---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/summing-to-one
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/building-blocks
- level/developing
resource_identity:
  ugm_id: summing-to-one
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 5170
  old_site_id: "A4_RT2_3"
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
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "2 log_9 3 = 1, 'how many log_81 3 do you need to add together to make one' - sums of logarithms equated to 1 via the laws and the definition, integers x,y with log_6 x + log_6 y = 1"
      rationale: "Canonical UGM title: Summing to one"
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

# Summing to one

> Excerpt: This task explores the behaviour of logarithms to different bases, by asking for solutions to equations in which sums of logarithms are equal to one.

## Problem 1

\[\log_3 3=1\]

\[\log_9 3+ \log_9 3 =1\]

\[\log_{27} 3 + \dots +\log_{27} 3= 1\]

How many \(\log_{81} 3\) do you need to add together to make one?

## Solution 1

\[\log_3 3=1\]

\[\log_9 3+ \log_9 3 =1\]

\[\log_{27} 3 + \dots +\log_{27} 3= 1\]

Perhaps some logical first thoughts would be that the second equation, \[\log_9 3+\log_9 3=1,\] can be rewritten as \[2\log_9 3 = 1,\] and so \[\log_9 3 = \frac{1}{2}.\]

We now have that \(\log_3 3=1\) and that \(\log_9 3=\frac{1}{2}\) but what is \(\log_{27}3\)?

Remember that we also know that \(\log_3 3=1\) because \(3^1=3\), and that \(\log_9 3=\frac{1}{2}\) because \(9^{\frac{1}{2}}=3\).

This is because of one of the defining statements about logarithms: \(\log_a x = y\) means \(x=a^y\) for real numbers \(x>0\) and \(y\).

We can now ask the question, to what power do we raise \(27\) to get the result \(3\)? If we think about powers of \(3\) then we can quickly confirm that \(27 = 3^3\) and so \(27^{\frac{1}{3}}=3\).

Now we have that \(\log_{27} 3 = \frac{1}{3}\) and therefore \[\log_{27} 3 + \log_{27} 3 +\log_{27} 3= 1,\] or equivalently, \[\log_{27} 3 + 2\log_{27} 3 = 1,\] or \[\log_{27} 3 + \log_{27} 9 = 1.\]

An alternative approach would be to use the statement \[\log_x ab = \log_x a + \log_x b.\] We can use this to rewrite the second equation, \[\log_9 3+\log_9 3=1,\] as \[\log_9 (3 \times 3) = \log_9 9 = 1.\]

Knowing that \[\log_x x = 1\] we can now think of the third equation as

\[\log_{27} (3a)=1\] where \(3a = 27\) and therefore \(a=9\) as before, \[\log_{27} 3 + \log_{27} 9 = 1.\]

How many \(\log_{81} 3\) do you need to add together to make one?

We can use exactly the same thinking to address this problem. We could consider \(81^n=3\) and recognise that \(81 = 3^4\) so \(n=\frac{1}{4}\).

This tells us that we will need four lots of \(\log_{81} 3\) to make one, \[4\log_{81}3=1.\]

This thinking relies on us recognising, or quickly deducing that \(81\) is the fourth power of \(3\). If the base of the logarithm were something less familiar, for instance \(2187\) (the seventh power of \(3\)), then this method is less convenient.

Alternatively we could have used the laws of logs to conclude that \[\log_{81} 3+\log_{81} b = \log_{81} (3b) = 1\] and so \(3b = 81\) and hence \(b = 27\).

Then we have \[\log_{81} 3 + \log_{81} 27 = 1.\] But, remember that the question asks how many lots of \(\log_{81} 3\) we need so we need to make one. This means that we need to write \(\log_{81} 27\) in terms of \(\log_{81}3\).

To do this we should first recognise that \(27 = 3^3\) so we can write that \[\log_{81}27 = \log_{81}3^3 = 3\log_{81}3.\]

We have used the statement \[\log_a x^y = y\log_a x.\]

Now we have \[\log_{81}3 + \log_{81}27 = \log_{81}3 + 3\log_{81}3,\] and therefore \[4\log_{81}3= 1.\]

## Problem 2

Can we choose integers \(x\) and \(y\) so that:

\[\log_6 x +\log_6 y =1?\]

How many different ways are there to do this?

How about using \(\log_{12}\)?

How about using \(\log_{24}\)?

How might your answers change if the equations were instead of the form \[\log_n x - \log_n y = 1?\]

## Solution 2

If we use the statement \[\log_x ab = \log_x a + \log_x b\] we can rewrite the equation, \[\log_6 x+\log_6 y=1,\] as \[\log_6 (x \times y)= 1.\]

Knowing that \(\log_x x = 1\) we can see that in the equation above \(x \times y = 6\).

Six has two pairs of factors: \(1 \times 6\) and \(2 \times 3\), so there are two possible ways to choose integers \(x\) and \(y\) so that \(\log_6 x + \log_6 y = 1\):

\[\log_6 1 + \log_6 6 = 1\] and \[\log_6 2 + \log_6 3 = 1.\]

Why did we not consider pairs of integers \(x\) and \(y\) such as \(-1 \times -6\)?

In theory, if we thought about evaluating each term in the equation we might try to choose a value of \(x\) that is a power of \(6\). We might choose something like \(x=36\) so that \(\log_6 36 = 2\).

What is the problem that we would encounter if we tried this approach?

What further information does this give us about the values of \(x\) and \(y\)?

How about using \(\log_{12}\)?

Taking the same approach as above we have that \[\log_{12} x + \log_{12} y = \log_{12} (x \times y) = 1.\]

By the same reasoning as the previous example we can conclude that \(x \times y = 12\) and as \(12\) has three pairs of factors there will be three possible ways to choose integers \(x\) and \(y\) so that \(\log_{12} x + \log_{12} y = 1\):

\[\log_{12} 1 + \log_{12} 12 = 1,\]

or

\[\log_{12} 2 + \log_{12} 6 = 1,\]

or

\[\log_{12} 3 + \log_{12} 4 = 1.\]

How about using \(\log_{24}\)?

\(24\) has four pairs of factors so there will be four possible ways to choose integers \(x\) and \(y\) so that \(\log_{24} x + \log_{24} y = 1\):

\[\log_{24} 1 + \log_{24} 24 = 1,\] \[\log_{24} 2 + \log_{24} 12 = 1,\] \[\log_{24} 3 + \log_{24} 8 = 1,\]

and

\[\log_{24} 4 + \log_{24} 6 = 1.\]

In all of the examples above we have only considered positive values of \(x\) and \(y\). Why?
