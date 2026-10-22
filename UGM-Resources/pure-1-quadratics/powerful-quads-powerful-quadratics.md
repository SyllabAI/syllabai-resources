---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/powerful-quads
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: powerful-quads
  station: quadratics
  station_title: Quadratics
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 8475
  old_site_id: E1_RT12_4
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
  - code: 1.1.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Equations quadratic in x^n.
      rationale: 'Canonical UGM title: “Powerful quadratics”; exam provenance: NRICH'
      validation_status: SUGGESTED
    title: recognise and solve equations in x which are quadratic in some function of x . tan
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: NRICH
task: T-UGM-IMPORT-1
import_note: question well prepended (was not among crawled sections)
---

# Powerful quadratics

> Excerpt: This problem offers a thought-provoking challenge, but one which is accessible if students are given some time to think about the problem. It is great for practising both quadratics and laws of indices.

## Question

this would also like sourceUrl http://nrich.maths.org/7041

1. Find all real solutions of the equation \[{\large (x^2 - 7x + 11)^{(x^2 - 11x + 30)} = 1}.\]
2. Find all real solutions of the equation \[{\large (2-x^2)^{(x^2 - 3\sqrt{2}x + 4)} = 1}.\]

## Problem

this would also like sourceUrl http://nrich.maths.org/7041

1. Find all real solutions of the equation \[{\large (x^2 - 7x + 11)^{(x^2 - 11x + 30)} = 1}.\]
2. Find all real solutions of the equation \[{\large (2-x^2)^{(x^2 - 3\sqrt{2}x + 4)} = 1}.\]

## Suggestion

If you were told that two numbers satisfied \[a^b=1,\] could you write down the possible numbers that \(a\) and \(b\) could be?

Can you apply the same logic to this question?

You might have to think hard to find all the solutions to the given equation. There are more than three solutions…

## Solution

There are several possibilities here.

**Case 1.** For any number \(a\) we have \(a^0=1\), so if we solve \(x^2-11x+30=0\) then this will give us some solutions.

**Case 2.** For any number \(b\) we have \(1^b=1\), so if we solve \(x^2-7x+11=1\) we will find more solutions.

**Case 3.** We also have that \((-1)^{2b}=1\) for any number \(b\). So we can solve \(x^2-7x+11=-1\), and then see whether the numbers we get lead to \(x^2-11x+30\) being an even number.

These are the only options, so by dealing with each case in turn we’ll find all the solutions.

For Case 1, we get \[x^2-11x+30=(x-6)(x-5)=0,\] so \(x=5\) and \(x=6\) are solutions.

For Case 2, we solve \[x^2-7x+10=(x-2)(x-5)=0,\] so we have an additional solution, \(x=2\).

Finally, for Case 3 we have that

\[x^2-7x+12=(x-3)(x-4)=0,\]

so we must check:

\[\begin{align*} 3^2-11\cdot 3+30=6 \quad \checkmark\\ 4^2-11\cdot 4 +30=2 \quad \checkmark \end{align*}\]

are both even, so \(x=3\) and \(x=4\) are also solutions.

So the real numbers satisfying the equation are \[x=2,3,4,5, 6.\]

---

There are again three cases to consider:

**Case 1.** \(x^2-3\sqrt{2}x+4=0\),

**Case 2.** \(2-x^2=1\),

**Case 3.** \(2-x^2=-1\) and \(x^2-3\sqrt{2}x+4\) is even.

In Case 1, \[x^2-3\sqrt{2}x+4=(x-\sqrt{2})(x-2\sqrt{2})=0,\] and so we have that \(x=\sqrt{2}\) and \(x=2\sqrt{2}\) are solutions. However, when \(x=\sqrt{2}\), we end up with \(0^0\).

The quantity \(0^0\) is a bit problematic. For some mathematicians there are good reasons to define \(0^0\) to be \(1\), whereas other mathematicians prefer to say that \(0^0\) is undefined.

So we may choose to discard \(x=\sqrt{2}\) as a solution.

In Case 2, we have that \[x^2-1=(x+1)(x-1)=0,\] so \(x=1\) and \(x=-1\) are also solutions.

Solving Case 3, we get \[x^2-3=(x+\sqrt{3})(x-\sqrt{3})=0,\] and so \(x=\pm\sqrt{3}\) are potential solutions. However, we have that \[\sqrt{3}^2\pm3\sqrt{2}\sqrt{3}+4=7\pm3\sqrt{6}\] is not divisible by two (it isn’t even an integer!) so \(x=\pm\sqrt{3}\) are not solutions.

So the values of \(x\) satisfying the equation are \[x=-1, 1, 2\sqrt{2}.\]
