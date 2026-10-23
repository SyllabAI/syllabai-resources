---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/general-solutions
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/food-for-thought
- level/introducing
resource_identity:
  ugm_id: general-solutions
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Introducing
  ref: 9026
  old_site_id: F4_RT12_2
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
  - code: 1.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: if tan A = tan B, what are A and B? — structure of trig solution sets; extends beyond
        P1's specified interval to general solutions (extension recorded)
      rationale: 'Canonical UGM title: “General solutions”'
      validation_status: SUGGESTED
    title: find all the solutions of simple trigonometrical equations lying in a specified interval (general
      forms of solution are not included).
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/general-solutions/download/teacher-notes.pdf
  kind: printable
interactive:
- src: //www.geogebratube.org/material/iframe/id/wpNxQgP6/width/590/height/436/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
- src: //www.geogebratube.org/material/iframe/id/KnhSdbEH/width/590/height/436/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
- src: //www.geogebratube.org/material/iframe/id/T3bGC4wb/width/590/height/436/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# General solutions

> Excerpt: The first question asks students what they can say about $A$ and $B$ if $\tan A=\tan B$. This resource offers interactive graphs to help students find general solutions of trigonometric equations and understand the relationship between solutions.

## Problem

- If \(\tan A=\tan B\), what can we say about \(A\) and \(B\)?

What about the corresponding questions for sine and cosine?

- If \(\cos A=\cos B\), what can we say about \(A\) and \(B\)?

- If \(\sin A=\sin B\), what can we say about \(A\) and \(B\)?

Suggestion: Think about the graphs of the trigonometric functions!

## Interactive graphs and solution

Here is a graph of \(y=\tan x\), showing the solutions of \(\tan x=a\).

You can slide the point on the \(y\)-axis to change the value of \(a\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/wpNxQgP6/width/590/height/436/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/wpNxQgP6)

How does this help you answer the question?

Solution

We can see from the graph that \(y=\tan x\) has a period of \(\pi\). This means that \(\tan(x+n\pi) = \tan x\) for all integers \(n\).

Therefore \(\tan A=\tan B=a\) if and only if \(A = B + n\pi\) for some integer \(n\). In other words, \(A\) and \(B\) can only differ by an integer multiple of \(\pi\).

If, for example, \(\tan A =\tan B = 1\), then \(A = \dfrac{\pi}{4}+n\pi\) for some integer \(n\). We’d also have \(B = \dfrac{\pi}{4}+m\pi\) for some integer \(m\), and so \[A = B + k\pi\quad \text{where $k$ is an integer.}\]

More generally, if \(\tan A=\tan B = a\), then \(A = \arctan a + n\pi\) and \(B = \arctan a + m\pi\), where \(n\) and \(m\) are integers, so \(A = B+ k\pi\) where \(k\) is an integer.

Please note that \(\arctan\) and \(\tan^{-1}\) mean the same thing and both are widely used in books and online. Similarly, you may see \(\arcsin\) or \(\sin^{-1}\) and \(\arccos\) or \(\cos^{-1}\).

Here is a graph of \(y=\cos x\), showing the solutions of \(\cos x=a\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/KnhSdbEH/width/590/height/436/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/KnhSdbEH)

Solution

We can see from the graph that \(y=\cos x\) has a period of \(2\pi\). This means that \(\cos(x+2n\pi) = \cos x\) for all integers \(n\).

Looking at the graph above, solutions to \(\cos x=a\) fall into two types (what we might call the ‘left-hand solutions’ and the ‘right-hand solutions’). For example, if \(a = \dfrac{1}{2}\), then we can call \(\dfrac{\pi}{3}\) a right-hand solution, and \(-\dfrac{\pi}{3}\) a left-hand solution.

This means that any solution to \(\cos x = a\) is of the form \[\text{(a right-hand solution)}+ 2n\pi \quad \text{or} \quad \text{(a left-hand solution)} + 2n\pi \quad \text{for some integer $n$.}\]

For example, if \(\cos x= \dfrac{1}{2}\), then \(x = \dfrac{\pi}{3} + 2n\pi\) or \(x = -\dfrac{\pi}{3} + 2n\pi\) for some integer \(n\).

Therefore, if \(\cos A = \cos B = a\), then \[A = \arccos a + 2n\pi \quad \text{or} \quad A = -\arccos a + 2n\pi,\] and \[B = \arccos a + 2m\pi \quad \text{or} \quad B = -\arccos a + 2m\pi,\]

where \(m\) and \(n\) are integers. This means that \(A = B + 2k\pi\) or \(A = -B + 2k\pi\), where \(k\) is an integer.

Here is a graph of \(y=\sin x\), showing the solutions of \(\sin x=a\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/T3bGC4wb/width/590/height/436/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/T3bGC4wb)

Solution

The period of \(\sin x\) is also \(2\pi\) and again the solutions to \(\sin x=a\) fall into two types. For example, if \(a = \tfrac{1}{2}\), then we can call \(\tfrac{\pi}{6}\) a left-hand solution and \(\pi -\tfrac{\pi}{6}\) a right-hand solution. Any solution to \(\sin x = a\) is therefore of the form \[\text{(a right-hand solution)}+ 2n\pi \quad \text{or} \quad \text{(a left-hand solution)} + 2n\pi \quad\text{for some integer $n$.}\]

If, for example, $\sin x = \dfrac{1}{2}$, then $A = \dfrac{\pi}{6} + 2n\pi$ or $A = \pi-\dfrac{\pi}{6} + 2n\pi$ for some integer $n$.

If \(\sin A = \sin B = a\), then we can say \(A\) and \(B\) have the following forms \[A = \arcsin a + 2n\pi \quad \text{or} \quad A = \pi -\arcsin a + 2n\pi,\quad \text{where $n$ is an integer,}\] \[B = \arcsin a + 2m\pi \quad \text{or} \quad B = \pi -\arcsin a + 2m\pi \quad \text{where $m$ is an integer.}\]

This means \(A = B + 2k\pi\) or \(A = \pi-B + 2k\pi\), where \(k\) is an integer.

We can think of \(y=\sin x\) as a translation of \(y=\cos x\), by \(\tfrac{\pi}{2}\) in the positive \(x\) direction. The symmetry of \(y=\cos x\) about the \(y\)-axis then means \(y=\sin x\) is symmetric about \(x = \tfrac{\pi}{2}\), and the solutions for \(\sin x = a\) are symmetrical about this line. Therefore we could write the solutions of \(\sin x=a\) as \[x = \left(\arcsin a - \dfrac{\pi}{2}\right) + 2n\pi + \dfrac{\pi}{2} \quad \text{or} \quad x = \left(\dfrac{\pi}{2} - \arcsin a\right) + 2n\pi + \dfrac{\pi}{2}.\]
