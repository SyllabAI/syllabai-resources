---
created: 2026-10-26T03:35:52 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-numbers/staircase-sequences
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-numbers
- type/investigation
resource_identity:
  ugm_id: staircase-sequences
  station: thinking-about-numbers
  station_title: Thinking about Numbers
  resource_type_id: 7
  resource_type_label: Investigation
  level: Introducing
  ref: 7292
  old_site_id: A1_RT1_1
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: thinking-about-numbers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-numbers
    validation_status: SUGGESTED
  spec_points:
  - code: 3.6.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-14 cross-map (cross-map-p3-iteration.json (P3c
        lane 14) @ syllabai-experimental 2d93dd7)
      evidence: 'The solution sets up the self-similar fixed point (''If I call that x... x seems to reappear
        inside itself: x = 1 + 1/x''), rearranges to x^2 - x - 1 = 0 and identifies the limit as its positive
        root (1+sqrt(5))/2, with the term table (1, 2, 1.5, 1.666..., 1.6, 1.625, ...) a convergent sequence
        of approximations observed to alternate either side of the root - the 3.6.2 idea and the 3.6.3
        relation between x = F(x) and the equation being solved, in an exploratory register.'
      rationale: 'Canonical UGM title: Staircase sequences'
      validation_status: SUGGESTED
    title: understand the idea of, and use the notation for, a sequence of approximations which converges
      to a root of an equation
  - code: 3.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-14 cross-map (cross-map-p3-iteration.json (P3c
        lane 14) @ syllabai-experimental 2d93dd7)
      evidence: 'The solution sets up the self-similar fixed point (''If I call that x... x seems to reappear
        inside itself: x = 1 + 1/x''), rearranges to x^2 - x - 1 = 0 and identifies the limit as its positive
        root (1+sqrt(5))/2, with the term table (1, 2, 1.5, 1.666..., 1.6, 1.625, ...) a convergent sequence
        of approximations observed to alternate either side of the root - the 3.6.2 idea and the 3.6.3
        relation between x = F(x) and the equation being solved, in an exploratory register.'
      rationale: 'Canonical UGM title: Staircase sequences'
      validation_status: SUGGESTED
    title: understand how a given simple iterative formula of the form x = F( x ) relates to the equation
      being solved, and use a given iteration, or an iteration based on a given rearrangement of an equation,
      to determine a root to a prescribed degree of accuracy.
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-iteration.json (P3c lane 14) @ syllabai-experimental 2d93dd7
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-14
---

# Staircase sequences

> Excerpt: Given two sequences involving continued fractions, students are asked to pose questions and explore. The resource offers practice at manipulating fractions and offers an opportunity to introduce the idea of limits.

## Problem

Consider the sequence \[1, \quad 1 + \cfrac{1}{1}, \quad 1 + \cfrac{1}{1 + \cfrac{1}{1}}, \quad 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}, \quad \dotsc\]

What do you make of it?

What about this sequence? \[1, \quad 1 + \cfrac{1}{2}, \quad 1 + \cfrac{1}{2 + \cfrac{1}{2}}, \quad 1 + \cfrac{1}{2 + \cfrac{1}{2 + \cfrac{1}{2}}}, \quad \dotsc\]

What other sequences might you try?

What questions would you ask about these sequences?

## Possible questions

Consider the sequence \[1, \quad 1 + \cfrac{1}{1}, \quad 1 + \cfrac{1}{1 + \cfrac{1}{1}}, \quad 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}, \quad \dotsc .\]

What do you make of it?

In playing around with the sequence you may well have asked some questions.

Here are some questions we asked about these sequences that you might like to think about, if you have not already considered them.

- What might this notation mean?

- Can I write these as more conventional fractions? In other words, what do they equal?

- How do I expect the sequence to continue?

- Does the sequence have a last term?

- Can I predict what happens to the terms of the sequence a long way down the line?

- Are the terms in the sequence getting larger or smaller?

- Can I efficiently work out the value of each term of the sequence?

- Do I notice anything interesting about the numbers in the fractions?

## Things you might have noticed

Consider the sequence \[1, \quad 1 + \cfrac{1}{1}, \quad 1 + \cfrac{1}{1 + \cfrac{1}{1}}, \quad 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}, \quad \dotsc .\]

What do you make of it?

What might this notation mean?

Can I write these as more conventional fractions? In other words, what do they equal?

The first term in the sequence is just \(1\).

The next is \(1 + \cfrac{1}{1} = 2\) in a familiar way.

Then we have a less familiar expression, but we can work through it ‘from the bottom up’ to make sense of it. We have \[1 + \cfrac{1}{1 + \cfrac{1}{1}} = 1 + \cfrac{1}{2} = \frac{3}{2}.\]

And then, similarly, \[1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}} = 1 + \cfrac{1}{1 + \cfrac{1}{2}} = 1 + \cfrac{2}{3} = \frac{5}{3}.\]

How do I expect the sequence to continue?

Does the sequence have a last term?

If I look at the original form of the sequence, I can imagine it going on forever, with more and more layers. I might need to think a bit more about what the conventional fractions look like as the sequence continues.

Can I predict what happens to the terms of the sequence a long way down the line?

Are the terms in the sequence getting larger or smaller?

It might be helpful to study a few more terms of the sequence, and then to collect the information in a way that helps us to make sense of it.

| Term of sequence | Fraction | Decimal |
|---|---|---|
| \(1\) | \(\dfrac{1}{1}\) | \(1\) |
| \(1 + \cfrac{1}{1}\) | \(\dfrac{2}{1}\) | \(2\) |
| \(1 + \cfrac{1}{1 + \cfrac{1}{1}}\) | \(\dfrac{3}{2}\) | \(1.5\) |
| \(1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}\) | \(\dfrac{5}{3}\) | \(1.666\dots\) |
| \(1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}}\) | \(\dfrac{8}{5}\) | \(1.6\) |
| \(1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}}}\) | \(\dfrac{13}{8}\) | \(1.625\) |
| \(1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}}}}\) | \(\dfrac{21}{13}\) | \(1.615\dots\) |
| \(1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}}}}}\) | \(\dfrac{34}{21}\) | \(1.619\dots\) |

It looks as though the terms alternately get larger and smaller, and it looks as though they might be tending to a limit that’s \(1.61...\) (not sure what the other decimal places might be yet).

We could try to think carefully about whether the terms will continue to alternately get larger and smaller. You could explore this further in [Comparing continued fractions](https://undergroundmathematics.org/thinking-about-algebra/comparing-continued-fractions).

I’d like to know whether the sequence really does tend to a limit. If it does, then it ought to be represented by \[1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \dots}}}}}.\] If I call that \(x\), then I could notice that \(x\) seems to reappear inside itself: \[x = 1 + \frac{1}{x}.\] And now I can rearrange to get a quadratic: it’s the same as the equation \[x^2 - x - 1 = 0.\] I can solve that using the quadratic formula. I find that \[x = \frac{1 \pm \sqrt{5}}{2},\] and since clearly \(x\) is positive I know that \[x = \frac{1 + \sqrt{5}}{2}.\] So it seems that the sequence really does tend to a limit, and that limit is \(\frac{1 + \sqrt{5}}{2} = 1.618...\) (which fits with my observations from the table above). In fact, it looks as though the sequence is alternately larger and smaller than this limit.

Can I efficiently work out the value of each term of the sequence?

I got bored while working out the table, so I found myself looking for shortcuts. I noticed that rather than working from the bottom up each time, I could use the previous term in the sequence: roughly speaking, \[\textrm{new term } = 1 + \frac{1}{\textrm{last term}}.\]

I can be a bit more formal if I use some symbols. If I know that one term of the sequence is \(\frac{a}{b}\), then the next is \[1 + \frac{1}{\bigl(\frac{a}{b}\bigr)} = 1 + \frac{b}{a} = \frac{a + b}{a}.\]

I wrote brackets around the \(\frac{a}{b}\) in the first fraction, so that I know what the numerator and denominator are. If I’d written \(\dfrac{1}{\frac{a}{b}}\) without brackets, I might have got confused and thought it meant \(\dfrac{\bigl(\frac{1}{a}\bigr)}{b}\).

So to find the numerator of the next term, I add the numerator and denominator of the last term, and to find the denominator of the next term, I simply take the numerator of the last term. And I can check that fits with the terms I found in my table.

Do I notice anything interesting about the numbers in the fractions?

I happen to recognise that each term in the sequence is the ratio of consecutive [Fibonacci numbers](https://undergroundmathematics.org/glossary/fibonacci-sequence). I can see why that is true using the reasoning above, that tells me how to find one term from the next.

So I’ve learned that the ratio of one consecutive Fibonacci number to the previous one converges to the golden ratio, \(\frac{1 + \sqrt{5}}{2}\).

The second sequence was: \[1, \quad 1 + \cfrac{1}{2}, \quad 1 + \cfrac{1}{2 + \cfrac{1}{2}}, \quad 1 + \cfrac{1}{2 + \cfrac{1}{2 + \cfrac{1}{2}}}, \quad \dotsc .\]

Using similar ideas, can you find what the sequence converges to?
