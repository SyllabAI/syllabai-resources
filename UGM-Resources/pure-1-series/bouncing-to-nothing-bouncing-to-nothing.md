---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/bouncing-to-nothing
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/rich-example
- level/developing
resource_identity:
  ugm_id: bouncing-to-nothing
  station: sequences
  station_title: Sequences
  resource_type_id: 2
  resource_type_label: Rich example
  level: Developing
  ref: 9023
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: sequences
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: sequences
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: 'bouncing ball: heights ×3/4 each bounce — total distance before stopping is a GP sum
        to infinity (mechanics context, suvat as vehicle)'
      rationale: 'Canonical UGM title: "Bouncing to nothing"'
      validation_status: SUGGESTED
    title: 'Questions may involve more than one progression. geometric progression, and the formula
      for the sum to infinity of a convergent geometric progression.: • use the condition for the convergence
      of a'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-6
assets:
- path: https://undergroundmathematics.org/sequences/bouncing-to-nothing/download/teacher-notes.pdf
  kind: printable
---

# Bouncing to nothing

> Excerpt: Students use projectile motion and sequences to work out what happens to a bouncing ball.

## Problem

A ball is thrown horizontally at a speed of \(\quantity{2}{m\,s^{-1}}\) from a point \(\quantity{1.25}{m}\) above \(O\) which is on a flat horizontal surface. After each bounce it reaches a height which is \(75\%\) of its maximum height after the previous bounce. Ignore air resistance and take the acceleration of gravity, \(g\), to be \(\quantity{10}{m\,s^{-2}}\).

- Sketch the trajectory of the ball.

- Calculate \(t_n\), the time the ball is in the air between the \(n^\text{th}\) and \((n+1)^\text{th}\) bounces.

- How far from \(O\) does the ball get before it stops bouncing?

## Solution

In between bounces, the ball is a projectile in free-fall so it’s trajectory will follow a parabola. After each bounce it joins a different parabola, with a maximum at \(75\%\) of the height of the previous one.

This diagram might raise a number of questions which probably can’t be answered without doing some calculations that we’ll get onto later.

- Are all the parabolic sections the same “width”?

- If not, how are they related?

- How does the time taken for each section vary?

- Does this sequence of parabolas continue indefinitely?

Between bounces, the ball is a projectile moving under gravity. We can treat the horizontal and vertical motions as independent of one another. The horizontal motion has no effect on the time between bounces.

Vertically, let’s start by thinking about the first section, before the first bounce. The ball starts with zero vertical velocity and we want to know the time taken to fall under gravity through a distance

\(\quantity{\frac{5}{4}}{m}\)

.

\[\begin{align*} s&=ut+\frac{1}{2}at^2 \\ \frac{5}{4} &=0+\frac{1}{2}10t^2 \\ t^2&=\frac{1}{4} \end{align*}\]

So the time for this section, \(t_0=\frac{1}{2}\).

We can do a similar calculation for \(t_n\) (for \(n\ge1\)), using the reduced maximum height. The height after the \(n^\text{th}\) bounce will be \[\frac{5}{4}\times\left(\frac{3}{4}\right)^n.\] So the constant acceleration formula for the downward journey gives us \[\frac{5}{4}\times\left(\frac{3}{4}\right)^n = 0+\frac{1}{2}10t^2\] and so the time for the whole section (up and down) will be \[t_n=2\times\sqrt{\frac{1}{5}\times\frac{5}{4}\times\left(\frac{3}{4}\right)^n} = \left(\frac{\sqrt{3}}{2}\right)^n.\]

Why did we include a factor of \(2\) at the start of this expression?

This starts to answer some of our earlier questions. Each section of the trajectory takes less time than the previous one, by a factor of \(\sqrt{3}/2\). Assuming the horizontal velocity is a constant \(\quantity{2}{m\,s^{-1}}\), what is the distance between successive bounces?

This might seem like a strange question – does it not keep bouncing forever?

We could take a pragmatic approach such as, “in reality a ball won’t appear to be bouncing when the height gets below a few centimetres. Find out how many bounces that will take and add up the times or distances for that many bounces.” Instead, we have considered a theoretical ball for which any bounce can be measured…

The times for the sections of the trajectory form a sequence, \[\frac{1}{2}, \frac{\sqrt{3}}{2}, \left(\frac{\sqrt{3}}{2}\right)^2, \left(\frac{\sqrt{3}}{2}\right)^3, \cdots\] Apart from the first term, \(t_0\), this is a geometric sequence with first term, \(t_1=\frac{\sqrt{3}}{2}\) and common ratio \(\frac{\sqrt{3}}{2}\).

As the common ratio is less than one we can calculate the sum to infinity of its terms. \[\sum_{n=0}^\infty t_n = \frac{1}{2} + \frac{\sqrt{3}/2}{1-\sqrt{3}/2} = \frac{7}{2}+2\sqrt{3} \approx7.0\]

Surprisingly, this tells us that although the ball bounces an infinite number of times, the time between bounces gets shorter and shorter, so that after \(7\) seconds all the bounces have been completed and the ball no longer moves vertically at all!

Assuming the horizontal velocity is a constant \(\quantity{2}{m\,s^{-1}}\), the ball will be about \(\quantity{14}{m}\) from \(O\) when it stops bouncing. After that it will be rolling along the ground.

If we had based our calculation on a finite number of bounces we would have found a shorter distance than this.

In reality, the horizontal velocity would probably not be constant, but how it changes at each bounce is hard to model.

Some more questions to think about…

- What assumptions were made in the model of this situation? How might the answer be different if we had made different assumptions?

- Can you think of any other effects that might change the outcome?

- If we tried this experimentally what do you think would actually happen? Do you think this model would be accurate?

- If we varied the initial height, how would the total bouncing time change?

- If we drew a curve through the maximum points of all the parabolic sections, what shape would the curve be? [Express \(x\) and \(y\) in terms of \(n\)…]
