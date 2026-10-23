---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r9341
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r9341
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9341
  old_site_id: Q2000
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: counting-and-binomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: counting-and-binomials
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics 1, 1952, Q4
task: T-UGM-IMPORT-6
---

# In how many ways can we arrange $4$ white, $3$ black, and $2$ red marbles?

## Question

1. Show that there are \({}^{10}C_4\) ways of arranging six similar white and four similar black marbles in line. [*Editorial note: \({}^{10}C_4\) is an alternative notation for \(\tbinom{10}{4}\).*] Find the number of ways of arranging four white, three black, and two red marbles in line, assuming that marbles of the same colour are indistinguishable. [A numerical answer is required.]

---

1. A bag contains six white and four black marbles. Find the chance that, if two marbles are drawn together, they are both black.

## Suggestion

Could we label all the marbles, so the whites, for example, become \(W_1, W_2, ... W_6\)?

How many possible ways to order the marbles in line are there now?

Now what happens if we take off the labels? How much duplication is there in our answer?

Again, could we start by labelling the marbles? How many possibilities are there now?

Now what happens if we take off the labels? How much duplication is there in our answer?

**Approach 1:**

Following the idea of part (i), how many ways are there of choosing two marbles from the ten in the bag?

**Approach 2**

Could we draw these two marbles one after the other, instead of drawing them together?

## Solution

Let’s first label the marbles. The white marbles can be numbered from 1 to 6, and the black ones from 1 to 4.

One possible order of the labelled marbles is

We have 10 choices for the first marble in the line. For the second marble, we now have \(9\) remaining possibilities.

For the third marble, we have \(8\) possibilities, and so on.

We then have \(7\), \(6\), \(5\), \(4\), \(3\), \(2\), \(1\) possibilities for remaining marbles.

In total, we therefore have \[10 \times 9 \times 8 \times \dotsb \times 2 \times 1 = 10!\] possible ways to order the ten *labelled* marbles.

What if the marbles are *unlabelled*?

If we swap any marbles of the same colour, we do not change the order of the black and white marbles.

These two arrangements will look identical, and thus will only be counted once.

Therefore there are fewer ways of ordering unlabelled marbles than labelled ones.

We can mix up the unlabelled white marbles in \(6!\) ways, and all of those arrangements will look identical.

We therefore have too many arrangements in the count of \(10!\) by a factor of \(6!\) altogether.

Similarly, the four black marbles can be rearranged in \(4!\) ways, each looking the same and counting once.

We therefore have too many arrangements in the count of \(10!\) by a further factor of \(4!\) altogether.

Therefore the number of unlabelled orders is \[\frac{\text{number of labelled orders}}{6!4!}=\frac{10!}{6!4!} =\binom{10}{4}.\]

As before, we will first compute how many possibilities there are in the case where the marbles are labelled, and then use this result to deduce the number of possibilities in the unlabelled case.

There are \(9\) marbles in total. If the marbles are labelled, then we have \(9!\) possible orders.

If the marbles are now unlabelled, there are \(4!\) possible labellings for the four white marbles, \(3!\) labellings for the three black marbles, and \(2!\) for the two red marbles.

So each unlabelled order gives rise to \(4!3!2!\) labelled orders.

Therefore, as before, the number of unlabelled orders is \[\frac{\text{number of labelled orders}}{4!3!2!} = \frac{9!}{4!3!2!} = 1260.\]

The expression \(\dfrac{9!}{4! 3! 2!}\) is called a *multinomial coefficient*.

For natural numbers \(k_1\), \(k_2\), …, \(k_s\) with \(k_1 + k_2 + \dotsb + k_s = n\), we define the multinomial coefficient \(\dbinom{n}{k_1, k_2, \dotsc, k_s}\) to be \[\dfrac{n!}{k_1! k_2! \dotsm k_s!}.\]

In the above approach we computed \(\dbinom{9}{4, 3, 2}\).

Just as the binomial coefficient \(\dbinom{n}{r}=\dbinom{n}{r,n-r}\) is the coefficient of \(x^ry^{n-r}\) in the expansion of the binomial expression \((x+y)^n\), the multinomial coefficient \(\dbinom{9}{4,3,2}\) is the coefficient of \(x^4y^3z^2\) in the expansion of \((x+y+z)^9\).

The general multinomial coefficient \(\dbinom{n}{k_1, k_2, \dotsc, k_s}\) is likewise the coefficient of \(x_1^{k_1}x_2^{k_2}\dotsm x_s^{k_s}\) in the expansion of \((x_1+x_2+\dotsb+x_s)^n\).

**Approach 1:**

Let us consider the marbles to be labelled.

Then for drawing two marbles together we have \(\dbinom{10}{2}\) possibilities.

Also, there are \(\dbinom{4}{2}\) possible ways to draw two black marbles, as there are four black marbles in total.

Therefore the chance that, when drawing two marbles, they are both black is \[\frac{\dbinom{4}{2}}{\dbinom{10}{2}} = \frac{6}{45} = \frac{2}{15}.\]

**Approach 2:**

Notice that drawing two marbles at the same time is the same as drawing two marbles consecutively without replacing the first marble.

Drawing the first marble, we have a chance (probability) of \(\dfrac{4}{10}=\dfrac{2}{5}\) for it to be black, as there are four black marbles and ten marbles in total.

For the second marble, we have a chance of \(\dfrac{3}{9} = \dfrac{1}{3}\) that it’s black, as there are nine marbles left, and three of them are black.

Therefore, in total we have a chance of \[\frac{2}{5} \times \frac{1}{3} = \frac{2}{15}\] for both marbles to be black.
