---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/average-speed
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: average-speed
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 8281
  old_site_id: C1_RT12_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: introducing-calculus
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: introducing-calculus
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/introducing-calculus/average-speed/download/teacher-notes.pdf
  kind: printable
---

# Average speed

> Excerpt: This resource has two interesting situations that require students to think carefully about how average speed is calculated, and in turn, think about different types of averages.

## Situation 1

|  | \(0\) - \(3\) miles | \(3\) - \(4\) miles |
|---|---|---|
| Driver \(1\) | \(\quantity{50}{mph}\) | \(\quantity{50}{mph}\) |
| Driver \(2\) | \(\quantity{75}{mph}\) | ? |

- The two drivers travel along the road shown in the diagram above. They pass the two average speed cameras at the same time as each other.  How far apart will the cars be after the first driver has gone \(1\) mile? What will be the greatest distance between the two drivers and when will it occur? What is the average speed of the second driver? What was the second driver’s speed for the last mile?

Suggestion

Sketching a distance-time graph from the information in the table might be a useful starting point.

## Solution 1

The graph above shows the information we were given in the table, with the speeds of the drivers represented by the gradients of the lines. How can we use it to help us solve the problem?

It is always a good idea to sketch a graph of a situation. It can help you visualise situations, highlight differences and similarities, and offer you a geometric way to solve a problem.

1. How far apart will the cars be after the first driver has gone \(\quantity{1}{mile}\)?

After driving \(\quantity{1}{mile}\) at \(\quantity{50}{mph}\) the first driver has been travelling for \(\dfrac{1}{50}\)th of an hour or \(1.2\) minutes. Therefore the second driver has travelled a distance of \(75\times\dfrac{1}{50} = \quantity{1.5}{miles}\) so the cars are \(\quantity{0.5}{miles}\) apart.

We could also have thought about the ratio of the speeds. The second driver is going \(1\frac{1}{2}\) times as fast as the first driver, so he will travel \(1\frac{1}{2}\) times as far in the same time.

1. What will be the greatest distance between the two drivers and when will it occur?

Both drivers arrive at the second speed camera together so we could add in the second driver’s journey to the graph.

The cars will be the greatest distance away from each other when the second driver has travelled \(\quantity{3}{miles}\). This occurs at \(\dfrac{3}{75}\)ths of an hour or \(2.4\) minutes. In this time, the first driver will have travelled \(50\times\dfrac{3}{75}=\quantity{2}{miles}\). The gap between them will be \(\quantity{1}{mile}\).

1. What is the average speed of the second driver?

Both cars travel the same distance in the same amount of time, so the second driver must also be averaging \(50\) mph in the situation above.

1. What was the second driver’s speed for the last mile?

The line we have drawn in represents the second part of their journey. The speed of the car is equal to the distance divided by the time taken.

We know the coordinates of A and B so we can calculate the speed as, \[\dfrac{4-3}{\frac{4}{50}-\frac{3}{75}}=\quantity{25}{mph}.\]

An algebraic approach

If we hadn’t drawn the graph we could have taken an algebraic approach to finding the solution. To work out the speed of the second driver once he has slowed down we need to consider his overall journey in two sections.

In the first section we know the speed and the distance so we have \[t_1=\dfrac{3}{75}.\]

In the second section we only know the distance so we can write \[t_2=\dfrac{1}{v},\] where \(v\) is the speed.

Subscripts can be very useful in questions like this, so as not to get confused. The times for each section will be different, which could be easily forgotten if we just used \(t\) for both equations.

As \(\text{average speed} = \dfrac{\text{total distance}}{\text{total time}}\), for the overall journey, with an average speed of \(50\) mph and a distance of \(\quantity{4}{miles}\), we have

\[50 = \dfrac{4}{t_1+t_2}.\]

Rearranging this equation gives us the total time,

\[t_1 +t_2=\dfrac{4}{50}.\]

You might have also found the total time by working out the time that the first driver took.

Substituting in the equations for \(t_1\) and \(t_2\) from above we get

\[\dfrac{3}{75}+\dfrac{1}{v}= \dfrac{4}{50}.\]

Solving for \(v\) gives us a speed of \(\quantity{25}{mph}\). So our driver must travel at \(\quantity{25}{mph}\) to make their average speed \(\quantity{50}{mph}\) over the \(\quantity{4}{miles}\).

## Situation 2

We are still along the same stretch of road, with a speed limit of \(\quantity{50}{mph}\), and the average speed cameras set at \(\quantity{4}{miles}\) apart. In this instance our first driver spends the same amount of time driving at \(\quantity{46}{mph}\) as he does at \(\quantity{62}{mph}\). Our second driver drives the first half of the distance at \(\quantity{46}{mph}\) and the second half at \(\quantity{62}{mph}\).

- What are the average speeds of each driver? Will either of them be caught speeding?

- What happens if the speed cameras are \(\quantity{10}{miles}\) apart instead? What changes?

Suggestion

It’s often a good idea to sketch a graph, even if you don’t need it to solve the problem. If you sketch the distance-time graphs here, it can help you visualise the two situations and highlight the differences between them. Look back at the [solution](https://undergroundmathematics.org/introducing-calculus/average-speed/solution-1) for the first situation to see how the graphs were used.

## Solution 2

What are the average speeds of each driver? Will either of them be caught speeding?

Let’s start with the first driver, who travels half the time at \(\quantity{46}{mph}\) and half the time at \(\quantity{62}{mph}\). This is represented by the graph above.

We have two different ways to think about the journey; as a whole, and split into its two pieces.

We can write the speeds of the two pieces as \[46=\dfrac{p}{\frac{1}{2}t}\quad\text{and}\quad 62 = \dfrac{q}{\frac{1}{2}t},\] where \(p\) and \(q\) are the distances travelled.

The journey as a whole can be written as \[\text{average speed} = \dfrac{p+q}{t}.\]

We know that \(p+q = 4\) but it turns out that substituting this into the equation is not helpful.

Therefore we can substitute in values for \(p\) and \(q\) in terms of \(t\), \[\textrm{ average speed } = \dfrac{23t+31t}{t},\] which leaves us with an average speed of \(\quantity{54}{mph}\).

What do you notice about the average speed? Could you have reasoned through this answer more easily, without doing the calculations?

Now we come to the driver who travels half the distance at each speed. Again we can think about the parts of the journey and the journey as a whole.

The separate parts can be written \[46 = \dfrac{2}{t_1} \quad \textrm{and} \quad 62 = \dfrac{2}{t_2}.\]

Will they spend a longer time travelling at \(\quantity{46}{mph}\) or at \(\quantity{62}{mph}\)?

The whole journey gives us

\[\text{average speed}=\dfrac{4}{t_1+t_2}.\]

Rearranging the above equations to find \(t_1\) and \(t_2\) and then substituting these in gives

\[\text{average speed}=\dfrac{4}{\dfrac{2}{46}+\dfrac{2}{62}}= \quantity{52.8}{mph}\ \text{($3$ sf)}.\]

Do you think that either driver will be given a speeding ticket?

What happens if the speed cameras are \(\quantity{10}{miles}\) apart instead? What changes?

Did you find that anything changed as the distance increased? Does this surprise you? Can you prove your findings for any distance?

Check your solution

If we look back at the equations we solved for the first driver, when the times were equal, we had \(p+q\) as the distance, which we knew equalled \(4\), but we did not need to use this fact.

Whatever the distance, we would have the same first set of equations \[46=\dfrac{p}{\frac{1}{2}t}\quad \textrm{and}\quad 62 = \dfrac{q}{\frac{1}{2}t},\] and the same second equation \[\text{average speed} = \dfrac{p+q}{t},\] where \(p+q=\) total distance travelled.

We could rearrange these to write \[\dfrac{\dfrac{46t}{2}+\dfrac{62t}{2}}{t} = \dfrac{46+62}{2}=54,\] so the distance does not affect the average speed.

It is the same in the second case, although perhaps less obvious. If instead of \(4\) miles we have \(2d\) miles, then we get the equations \[46 = \dfrac{d}{t_1} \quad \text{and}\quad 62 = \dfrac{d}{t_2}\] and \[\text{average speed}=\dfrac{2d}{t_1+t_2}.\]

Rearranging the first two equations in terms of \(t_1\) and \(t_2\) means we we can write this as \[\text{average speed}=\dfrac{2d}{\dfrac{d}{46}+\dfrac{d}{62}}\] and simplify it to \[\text{average speed}= \dfrac{2}{\dfrac{1}{46}+\dfrac{1}{62}}= \quantity{52.8}{mph}\text{ (3 sf)}.\]

Therefore this average also does not depend on the distance travelled.

Can you also explain graphically why the average speed for each situation does not depend on the total distance?

We have calculated two different average speeds. Often when people say ‘average’ they mean one particular type. Think about other averages you have met - do either of these two calculations remind you of averages you already know?

For equal distance spent at each speed

\[\textrm{average speed} = \dfrac{2}{\dfrac{1}{46}+\dfrac{1}{62}},\]

and for equal time spent at each speed

\[\textrm{average speed} = \dfrac{46+62}{2}.\]

To think more about this go to the [Averages](https://undergroundmathematics.org/introducing-calculus/average-speed/averages) section.

## Averages

We have calculated two different average speeds. Often when people say ‘average’ they mean one particular type. Think about other averages you have met - do either of these two calculations remind you of averages you already know?

For equal distance spent at each speed

\[\textrm{average speed} = \dfrac{2}{\dfrac{1}{46}+\dfrac{1}{62}},\]

and for equal time spent at each speed

\[\textrm{average speed} = \dfrac{46+62}{2}.\]

When people say ‘the average’ they are usually saying ‘the mean’. You know there is more than one type of average, but informally using ‘the average’ is often acceptable.

However it might surprise you that even saying ‘the mean’ is not enough, as there is also more than one type of mean. The mean you are most familiar with is actually called the ‘arithmetic mean’.

\[\text{arithmetic mean of $x_1$, ..., $x_n$ is } \dfrac{1}{n}(x_1 + x_2 + \dotsb + x_n).\]

You may have spotted that when finding the average for equal times, we arrived at \[\dfrac{46+62}{2},\] which is the arithmetic mean of \(46\) and \(62\).

What is probably less familiar is the scenario of equal distance which led to \[\dfrac{2}{\dfrac{1}{46}+\dfrac{1}{62}},\] which is the [harmonic mean](https://undergroundmathematics.org/glossary/harmonic-mean) of \(46\) and \(62\).

There are three means known as Pythagorean means, which are the arithmetic mean, the harmonic mean and the geometric mean. For positive numbers

\(x_1\)

, …,

\(x_n\)

, these are given by

\[\begin{align*} \text{arithmetic mean} &= \dfrac{x_1 + x_2 + ... + x_n}{n}\\ \text{harmonic mean} &= \dfrac{n}{\dfrac{1}{x_1}+\dfrac{1}{x_2} + ...+ \dfrac{1}{x_n}}\\ \text{geometric mean} &= \sqrt[n]{\vphantom{()}x_1x_2...x_n}. \end{align*}\]

Let us make our driving examples more general. We already know that the distance does not affect the means when we are driving for an equal time or an equal distance.

If we make the speeds \(u\) and \(v\), what is the average speed when driving an equal time at each speed?

Solution

\[u = \dfrac{d_1}{t} \textrm{ and } v = \dfrac{d_2}{t},\]

so the average speed would be

\[\dfrac{d_1+d_2}{2t} = \dfrac{ut+vt}{2t} = \dfrac{u+v}{2},\]

which is our arithmetic mean of \(u\) and \(v\).

If our speeds remain \(u\) and \(v\), what is the average speed when each is driven for an equal distance?

Solution

This time

\[u = \dfrac{d}{t_1} \textrm{ and } v= \dfrac{d}{t_2},\]

so the average speed would be

\[\dfrac{2d}{t_1+t_2}=\dfrac{2d}{\dfrac{d}{u}+\dfrac{d}{v}} = \dfrac{2}{\dfrac{1}{u}+\dfrac{1}{v}},\]

which is the harmonic mean of \(u\) and \(v\), and can also be written in the form

\[\dfrac{2uv}{u+v}.\]

Will one of the averages always be bigger than the other?

Suggestion

In which of the situations do you spend the longest time at the faster speed?

Solution

We can see from the graph that travelling for an equal length of time at both speeds means that you spend longer travelling at the higher speed than when you travel an equal distance at both speeds. Therefore you will cover the distance in a quicker time and have a greater average speed.

We can also prove this algebraically. If we subtract the harmonic mean (equal distance), away from the arithmetic mean (equal time), we get

\[\dfrac{u+v}{2}-\dfrac{2uv}{u+v} = \dfrac{u^2+v^2+2uv-4uv}{2(u+v)}.\]

If we then simplify the numerator we have

\[\dfrac{u^2-2uv+v^2}{2(u+v)},\]

which can be factorised to

\[\dfrac{(u-v)^2}{2(u+v)}.\]

The numerator will never be negative as it is squared, and the denominator will always be positive as \(u\) and \(v\) are always positive. Therefore

\[\dfrac{(u-v)^2}{2(u+v)}≥0.\]

So the average speed when driving for equal time will always be greater than or equal to the average speed when driving for equal distances.

The result in the question above generalises to more than two speeds. In fact the harmonic mean is always less than or equal to the geometric mean, which is always less than or equal to the arithmetic mean for the same set of positive numbers.

The part of this result that is used the most often only involves the arithmetic and geometric means.

\[\dfrac{1}{n}(x_1 + x_2 + ... + x_n) ≥ \sqrt[n]{\vphantom{()}x_1x_2...x_n}\]

This is more commonly known as the [AM-GM inequality](https://undergroundmathematics.org/glossary/am-gm-inequality), and appears more regularly than you might think. You might like to try this [review question](https://undergroundmathematics.org/polynomials/r6546) or [this one](https://undergroundmathematics.org/thinking-about-algebra/r7865) that it appears in.

Let us now think about a type of question you may well have seen before.

If the (arithmetic) mean height of a class of 30 pupils is \(1.24\)m, and the mean height of a class of \(20\) pupils is \(1.42\)m, what is the mean height of all the pupils?

Suggestion

What is the total height of all \(50\) pupils?

Solution

We cannot just take the mean of \(1.24\) and \(1.42\) as they are unequally weighted.

One way is to work out the total height of each class.

The class with \(30\) pupils has a total height of \(30 \times 1.24 = 37.2\)m.

The class with \(20\) pupils has a total height of \(20 \times 1.42 = 28.4\)m.

So the average height of all \(50\) pupils is

\[\dfrac{30 \times 1.24+ 20 \times 1.42}{50} = 1.312\textrm{m}\]

A different way of thinking about it is the proportion each class contributes to the average. The class with \(30\) pupils accounts for \(\frac{3}{5}\) of the total and so we could write the calculation

\[\text{average height} = \dfrac{3}{5}\times1.24+\dfrac{2}{5}\times1.42.\]

This is what we call a *weighted arithmetic mean*, as the two different heights are contributing unequal amounts to the mean.

Now let us consider a car travelling at a speed \(u\) for a time \(t_1\) and then travelling at speed \(v\) for time \(t_2\). What is its average speed?

We have

\[u = \dfrac{d_1}{t_1} \textrm{ and } v = \dfrac{d_2}{t_2},\]

so the average speed is given by

\[\dfrac{d_1+d_2}{t_1+t_2}.\]

If we rearrange the formulae for \(u\) and \(v\) to get them in terms of \(d_1\) and \(d_2\) then we can substitute these into the formala for average speed to get

\[\dfrac{ut_1+vt_2}{t_1+t_2},\]

which can be written as

\[\dfrac{t_1}{t_1+t_2}\times u + \dfrac{t_2}{t_1+t_2}\times v,\]

which is a weighted arithmetic mean, where we are taking the proportion of time that has been travelled at each speed into account.

From this general case we can return to our special case of equal times.

If you make \(t_1 = t_2\), can you show the formula simplifies to the arithmetic mean?

If you start again, you can rearrange the formulae for \(u\) and \(v\) to get them in terms of \(t_1\) and \(t_2\), and so get a formula for average speed in terms of \(u\), \(v\), \(d_1\) and \(d_2\) that is a weighted harmonic mean. Can you return to our special case of equal distances from your formula?
