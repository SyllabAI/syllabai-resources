---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/inverse-or-not
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: inverse-or-not
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 8344
  old_site_id: F4_RT12_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-triangles-to-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-triangles-to-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.5.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: one graph is y=arctan(tan x), another y=tan(arctan x) — inverse trig notation and principal
        values made visible
      rationale: 'Canonical UGM title: “Inverse or not?”'
      validation_status: SUGGESTED
      primaryPick: true
    title: use the notations sin x , cos­ x , tan x to denote No specialised knowledge of these functions
      is the principal values of the inverse trigonometric required, but understanding of them as examples
      of relations inverse functions is expected. sin i
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/inverse-or-not/components/graphs-cards.pdf
  kind: printable
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/inverse-or-not/download/teacher-notes.pdf
  kind: printable
---

# Inverse or not?

> Excerpt: This graph-matching problem can be used to introduce the principal-value ranges of $\arcsin$, $\arccos$ and $\arctan$ and to reinforce ideas of what happens when functions are composed, using specific examples such as $\arcsin(\sin x).$

## Problem

Take a look at the three graphs below.

| Graph A | Graph B |
|---|---|
| Graph C |  |

One of the graphs shows \(y=\arctan(\tan x).\) Another shows \(y=\tan (\arctan x)\). Which graphs are these, and why? (The small open circles on the graphs indicate that these points are excluded.)

Please note that \(\arctan\) and \(\tan^{-1}\) mean the same thing and both are widely used in books and online. Similarly, \(\arcsin\) and \(\sin^{-1}\) mean the same as one another, as do \(\arccos\) and \(\cos^{-1}\).

If you want to know more about \(\arctan x\), \(\arcsin x\) and \(\arccos x\) before working on this task, you may find it helpful to look at [Inverse trigonometric functions](https://undergroundmathematics.org/trigonometry-triangles-to-functions/inverse-trig-functions).

More graphs

Match these equations to the graphs below and explain your reasoning.

\[y=\arcsin(\sin x)\]

\[y=\sin(\arcsin x)\]

\[y=\arccos(\cos x)\]

\[y=\cos(\arccos x)\]

For which values of \(x\) is \(\tan(\arctan x)=x\)? What about \(\arctan(\tan x)=x\)?

What can you say about the solutions of similar equations, such as \(\sin(\arcsin x)=x\) or \(\arccos(\cos x)=x\)?

## Solution

Take a look at the three graphs below.

| Graph A | Graph B | Graph C |
|---|---|---|

One of the graphs shows

\(y=\arctan(\tan x)\)

. Another shows

\(y=\tan (\arctan x)\)

. Which graphs are these, and why?

As \(\tan x\), \(\sin x\) and \(\cos x\) are periodic functions, there are many values of \(x\) that give the same value of \(\tan x\), \(\sin x\) or \(\cos x\). This means that inverse functions such as \(\arctan x\) and \(\arcsin x\) have to be very carefully defined. You can read more about this in [Inverse trigonometric functions](https://undergroundmathematics.org/trigonometry-triangles-to-functions/inverse-trig-functions), and these ideas are used in this solution.

Looking at the three graphs, I notice that Graph C looks like a graph of \(y=x\) for all real values of \(x.\) In contrast, Graph B looks like a graph of \(y=x\) but only for \(x\) in the [interval](https://undergroundmathematics.org/glossary/interval-notation) \(\left(\frac{-\pi}{2}, \frac{\vphantom{-}\pi}{2}\right)\). Having thought about Graph B, I can now think of Graph A as a repeating version of Graph B, with period \(\pi\).

To see which graphs show the functions \(\arctan(\tan x)\) and \(\tan (\arctan x)\) I can think about [domains](https://undergroundmathematics.org/glossary/domain) and [ranges](https://undergroundmathematics.org/glossary/range-of-a-function).

When composing functions \(f(x)\) and \(g(x)\) to form \(g(f(x))\), I need to think about the domain of \(f(x)\). I need to check that any output of \(f\) is in the domain of \(g\) and what these outputs are, so the range of \(g(f(x))\) depends on the domain and range of \(f\) as well as the range of \(g\).

Starting with the inner function in \(\arctan(\tan x)\), I know that \(\tan x\) is defined for all real \(x\) except where \(x=\frac{(2n+1)\pi}{2}\). This is the domain of \(\tan x\). The range is the whole of the real numbers. This means the input to the outer \(\arctan\) function is all the real numbers, so the output for \(\arctan\) is its [principal value range](https://undergroundmathematics.org/glossary/inverse-trigonometric-function), which is the interval \(\left(-\frac{\pi}{2},\frac{\pi}{2}\right)\). Therefore, the graph of \(\arctan(\tan x)\) has a domain which is the whole of the \(x\)-axis except the points where \(x=\frac{(2n+1)\pi}{2}\), and the range is \(\left(-\frac{\pi}{2},\frac{\pi}{2}\right)\), so Graph A shows \(y=\arctan(\tan x)\).

I’ll now use similar thinking to work out which is the graph of \(y= \tan (\arctan x)\). This time \(\arctan x\) is the inner function. Its domain is the whole of the real numbers, but the range is \(\left(-\frac{\pi}{2},\frac{\pi}{2}\right)\).

This graph shows \(y= \tan x\) for \(x\) in the interval \(\left(-\frac{\pi}{2},\frac{\pi}{2}\right)\). Can you use it to explain why Graph C must show \(y=\tan (\arctan x)\)?

Match these equations to the graphs below and explain your reasoning.

\[y=\arcsin(\sin x)\]

\[y=\sin(\arcsin x)\]

\[y=\arccos(\cos x)\]

\[y=\cos(\arccos x)\]

| Graph D | Graph E | Graph F |
|---|---|---|
| Graph G | Graph H | Graph J |

One thing I notice is that all four of the functions map \(0\) to \(0\), so the graphs must pass through the origin. This eliminates Graph G.

The domain of \(\sin x\) is all real \(x\) and the range is the interval \([-1,1]\). The domain of \(\arcsin x\) is the interval \([-1,1]\), and the principal value range is \(\left[-\frac{\pi}{2},\frac{\pi}{2}\right]\) (see [Inverse trigonometric functions](https://undergroundmathematics.org/trigonometry-triangles-to-functions/inverse-trig-functions) for more explanation).

So the function \(\arcsin(\sin x)\) is defined for all real \(x\) and has range \(\left[-\frac{\pi}{2},\frac{\pi}{2}\right]\). Within the domain \(\left[-\frac{\pi}{2},\frac{\pi}{2}\right]\) the function will map \(x\) to itself so the graph will look like that of \(y=x\). So this one must be Graph D.

Notice that as \(x\) increases from \(\frac{\pi}{2}\) to \(\frac{3\pi}{2}\), \(\sin x\) decreases from \(1\) to \(-1\) and so \(\arcsin(\sin x)\) decreases from \(\frac{\pi}{2}\) to \(-\frac{\pi}{2}\). And then this pattern continues, forming a zig-zag graph.

The domain of \(\arcsin x\) is the interval \([-1,1]\) and it is undefined elsewhere. Within this domain it has range \(\left[-\frac{\pi}{2},\frac{\pi}{2}\right]\), and these values as input to \(\sin x\) produce values in the range \([-1,1]\). So the graph will look like \(y=x\) restricted to the domain \(-1\le x\le1\), which is Graph E.

\(\cos x\) is defined for all real \(x\) and has range \([-1,1]\). \(\arccos x\) is defined on the domain \([-1,1]\) and its principal value range is \([0,\pi]\). So the domain of this composition is all the real numbers and its range is\([0,\pi]\). The only graph that matches this is J.

By way of a check, as \(x\) increases from \(0\) to \(\pi\), the value of \(\cos x\) decreases from \(1\) to \(-1\) and so \(\arccos(\cos x)\) increases from \(0\) to \(\pi\). On this domain, the graph looks like \(y=x\). As \(x\) increases further from \(\pi\) to \(2\pi\), \(\cos x\) increases from \(-1\) to \(1\) and \(\arccos(\cos x)\) decreases from \(\pi\) to \(0\). Hence we get a zig-zag pattern.

\(\arccos x\) is defined only for \(x\) in the interval \([-1,1]\). It’s range is \([0,\pi]\) and \(\cos\) of these values has range \([-1,1]\). So our graph will look like \(y=x\) restricted to the domain \([-1,1]\), and it must be Graph E, the same as for equation (2).

It is interesting to note that \(\cos x\) and \(\arccos x\) are decreasing functions on these intervals but the composition of the functions is increasing. Is this the case for *any* pair of decreasing functions?

As Graph C is \(y=\tan(\arctan x)\), it must be that \(\tan(\arctan x)=x\) for all real \(x\).

Graph A shows \(y=\arctan(\tan x)\), so \(\arctan(\tan x)=x\) only for \(x\) in the interval \(\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right)\) as this is the only part of the graph for which \(y=x\) matches the graph of \(y=\arctan(\tan x)\).

To illustrate what happens if \(x\) is outside this interval, let’s try \(x=\tfrac{4\pi}{3}\). I know \(\tan \tfrac{4\pi}{3} = \sqrt{3}\), but \(\arctan \sqrt{3}= \tfrac{\pi}{3}\). Therefore \(\arctan\left(\tan \tfrac{4\pi}{3}\right)= \arctan \sqrt{3}=\tfrac{\pi}{3}\). Generalising from this example, I can see that if \(x\) is outside the interval \(\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right)\) and \(\tan x\) is defined, then \(\arctan(\tan x)\) takes \(x\) to the corresponding value inside the interval \(\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right)\).

We can draw corresponding conclusions for the \(\sin\) and \(\cos\) compositions by looking at graphs D, E and J.
