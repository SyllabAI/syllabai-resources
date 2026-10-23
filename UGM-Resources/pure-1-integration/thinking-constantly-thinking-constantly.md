---
created: 2026-10-24T04:45:46 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/thinking-constantly
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/building-blocks
resource_identity:
  ugm_id: thinking-constantly
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 8986
  old_site_id: None
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.8.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-8 cross-map (cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd)"
      evidence: "displacement recovered from velocity by integration with initial-condition constants — reverse-process integration plus constant-of-integration evaluation (mechanics context is a wrapper; the lane-7 routing recorded the 1.8 bearing)"
      rationale: "Canonical UGM title: \"Thinking constantly\""
      validation_status: SUGGESTED
    title: "solve problems involving the evaluation of a constant of integration"
  mapped_date: '2026-10-24'
  mapper: cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-8
---

# Thinking constantly

> Excerpt: A kinematics problem focusing on integration constants and how altering the initial conditions affects the movement of an object.

## Warm-up

You are moving along a straight line, with your acceleration given by \[a(t) = 6t - 2.\]

- How fast will you be travelling at \(t=2\)?

- Where will you be on the line at \(t=2\)?

## Warm-up solution

You are moving along a straight line, with your acceleration given by \[a(t) = 6t - 2.\]

- How fast will you be travelling at \(t=2\)?

You can think about the relationship between acceleration, velocity and displacement in two ways.

\[a(t) = \dfrac{d}{dt}\big(v(t)\big)\]

\[v(t) = \dfrac{d}{dt}\big(s(t)\big)\]

\[s(t) = \int{v(t)}\, dt\]

\[v(t) = \int{a(t)}\,dt\]

So we need to integrate the acceleration function to find your velocity function.

\[\begin{align*} v(t) &= \int{(6t - 2)}\,dt\\ v(t) &= 3t^2 - 2t + c \end{align*}\]

What does the constant \(c\) represent in terms of velocity?

We know that \(t=2\). Do we have enough information to say how fast we are going?

If we calculate \(v(2)\) we get

\[\begin{align*} v(2) &= 12 - 4 + c\\ &= 8+c, \end{align*}\]

so we could say our velocity is \(8 + c\) units.

Or we could calculate the integral

\[\begin{align*} \int_{0}^{2}{(6t - 2)}\,dt &= \left[3t^2 - 2t +c \right]^2_0\\ &= v(2) - v(0) \\ &= 8 \end{align*}\]

and say our velocity is \(8\) units faster than it was at \(t = 0\).

In both cases we have accounted for the constant of integration which represents our initial velocity. This is important as we weren’t given any information about our velocity at \(t=0\), so we cannot assume that it was zero.

- Where will you be on the line at \(t=2\)?

To then find your displacement function we need to integrate the velocity function.

\[\begin{align*} s(t) &= \int{(3t^2 - 2t + c)}\,dt\\ s(t) &= t^3 - t^2 + ct + d \end{align*}\]

Why is it important not to forget the constant of integration from the velocity function?

What does the constant \(d\) represent in terms of displacement?

With the displacement function we could calculate

\[\begin{align*} s(2) &= 2^{3} - t^{2} + 2c + d \\ &=4 + 2c +d \end{align*}\]

or

\[\begin{align*} \int_{0}^{2}{(3t^2 - 2t + c)}\,dt &= \left[t^3 - t^2 + ct + d \right]^2_0 \\ &= s(2) - s(0) \\ &= 4 + 2c. \end{align*}\]

One of these gives us your displacement from your starting point, and one gives us your displacement relative to a fixed origin. Which is which?

Under what circumstances would the two answers be the same?

## Main problem

The acceleration function of an object moving in a straight line is given by \[a(t) = \sqrt{t} -2.\]

Determine the velocity and displacement functions, and if possible draw the graphs on software such as [GeoGebra](https://www.geogebra.org/graphing) or [Desmos](https://www.desmos.com/calculator).

Once you have drawn the graphs, answer the following questions. (A GeoGebra applet of the graphs is available [here](https://undergroundmathematics.org/calculus-meets-functions/thinking-constantly/problem-geogebra).)

1. If, at time \(t = 0\), the velocity and displacement are zero, can you describe, draw or imagine what the journey is like? Which direction are you travelling in? Are you speeding up or slowing down?   Suggestion   To draw or describe the journey, think about a straight line with an origin where the object starts (as the displacement is zero). Things change about the journey at the following times: \(t = 4\), \(t= 9\) and \(t = 14\). What are they?

---

1. Approximately, for what value of \(c\) is there no negative velocity? (We are using \(c\) to represent the constant in the velocity function and \(d\) for the constant in the displacement function.)  What feature of the journey changes when there is no negative velocity? What feature of the displacement graph changes when there is no negative velocity?

---

1. The acceleration function is negative for the first \(4\) seconds. What does this mean is happening to the object when  \(c = 0\)? \(c = 3\)? \(c = 2\)?

---

1. Now let’s think about \(c=0\) and \(d=2\). How would you describe the journey, and how does it differ from the journey in question 1?

## Interactive graph

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/GMxHaPhT/width/797/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/GMxHaPhT)

## Solution

Our journey is along a straight line (to think about why see [Speed vs velocity](https://undergroundmathematics.org/introducing-calculus/speed-vs-velocity/thinking-about-journeys)). To describe the journey consistently, let us imagine a line with an origin that represents a displacement of zero and let us define the positive direction as being to the right.

If velocity and displacement are zero at time \(t = 0\), this implies that \(c\) and \(d\) are zero, so we can think of the origin as our starting point.

The times when something about the journey changes are \(t = 4\), \(t= 9\), and \(t = 14\). Can you see why from the graph?

**From \(t = 0\) to \(4\)**

The object starts from rest and travels left, up to a speed of approximately \(3\).

The velocity is negative (to the left) but decreasing, so it means the magnitude (or speed) is actually getting larger.

**From \(t = 4\) to \(9\)**

The object is still going left, but the speed is now decreasing, What happens to the object at \(t = 9\)?

**From \(t = 9\) to \(14\)**

The object is travelling to the right, and the velocity (and speed) is increasing from \(0\). It passes the origin at \(t=14\).

Think about how changes in the journey are represented on the different graphs. For example, when the acceleration is zero, what key features do the different graphs exhibit?

At \(c \approx 2.7\), the velocity graph no longer crosses the \(x\)-axis.

There is now no negative velocity, so the object will always be moving to the right.

If the object is always moving to the right, then the displacement is always increasing. The local maxima and minima of the displacement graph disappear so the displacement function is now an increasing function. Why? What impact does the velocity have on the displacement graph?

1. The acceleration function is negative for the first \(4\) seconds. What does this mean is happening to the object when  \(c = 0\)? \(c = 3\)? \(c = 2\)?

**When \(c =0\)**

We often think about negative acceleration meaning deceleration or slowing down. But if we remember how we described the journey in the first part of the question, we said ‘The object starts from rest and travels left, up to a speed of approximately \(3\)’.

What is happening here?

If the acceleration is negative the velocity is decreasing. Of course, if the velocity is negative and decreasing, its magnitude is increasing, meaning you are travelling faster. So here, the negative acceleration means travelling to the left and speeding up.

**When \(c = 3\)**

This is similar to the question above. Velocity is no longer negative, so our acceleration behaves as we would normally think. During the first \(4\) seconds, the object is slowing down while travelling to the right.

**When \(c = 2\)**

This is a combination of the two cases above. Initially the object slows down as it travels right, but as the velocity reaches zero, the object changes direction, and it starts to speed up as it travels towards the left. At \(t = 4\), it starts to slow down again. (From this point the acceleration is positive, meaning the object is slowing down as it travels left.)

Firstly, changing \(d\) only affects the displacement graph so the velocity and acceleration descriptions from question \(1\) stay the same.

The object now starts \(2\) units to the right of the origin. There are two ways we could think about this. Either the object has changed its starting point by \(2\) units or the origin has moved \(2\) units to the left.

Does that second description seem strange? Remember, we can choose the point from which we want to measure displacement as long as we state what this point is. Often, questions will inform us that displacement equals zero at \(t = 0\). Why do you think this is so common?

Moving our origin is a translation, and we do it to try to make calculations more straightforward. When we think of translations, we might imagine sliding a graph, but we could also imagine sliding the axes, while the graph stays in the same place. This idea of choosing an origin to suit your question can be applied in many areas, and will become more familiar to you as you work with vectors and think about frames of reference.
