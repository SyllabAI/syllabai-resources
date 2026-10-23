---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/slices-of-pi
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: slices-of-pi
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 7866
  old_site_id: G3_RT11_1
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
  - code: 1.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: semicircle divided by inequalities in sinθ, cosθ, tanθ — exact values and identities read
        off graphs
      rationale: 'Canonical UGM title: “Slices of $\pi$”'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  - code: 1.5.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: semicircle divided by inequalities in sinθ, cosθ, tanθ — exact values and identities read
        off graphs
      rationale: 'Canonical UGM title: “Slices of $\pi$”'
      validation_status: SUGGESTED
    title: use the identities / tan i and cos i sin i + cos i / 1
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/slices-of-pi/download/teacher-notes.pdf
  kind: printable
---

# Slices of $\pi$

> Excerpt: When is $\sin \theta$ bigger than $\cos \theta$?  When is $\tan \theta$ smaller than $\cos \theta$?  In this resource, inequalities of the form $\sin \theta < \tan \theta < \cos \theta$ have been used to slice up a semi-circle.  Which inequality defines each slice?

## Problem

Take a look at the diagram below.

We’ve used inequalities involving \(\sin \theta\), \(\cos \theta\) and \(\tan \theta\) to divide the semicircle into sectors.

Each sector in the diagram is defined by a different inequality.

For example, one sector is defined by the angles \(\theta\) between \(0\) and \(\pi\) for which \(\cos \theta < \sin \theta < \tan \theta.\)

Another sector is defined by \(\cos \theta< \tan \theta < \sin \theta.\)

Questions

- Can you work out which inequality has been used to define each sector?

- Which is the biggest sector?

- If you extended the diagram to make a complete circle, how many extra sectors would you need?

## Things you might have noticed

Take a look at the diagram below.

We’ve used inequalities involving \(\sin \theta\), \(\cos \theta\) and \(\tan \theta\) to divide the semicircle into sectors. Each sector in the diagram is defined by a different inequality. For example, one sector is defined by the angles \(\theta\) between \(0\) and \(\pi\) for which \(\cos \theta < \sin \theta < \tan \theta.\) Another sector is defined by \(\cos \theta< \tan \theta < \sin \theta.\)

- Can you work out which inequality has been used to define each sector?

There are many ways to approach this problem, and we will illustrate a few of them here. If you have used different approaches, or used similar approaches but for different parts of the problem, you might find it interesting to compare the methods.

| We need to think about how \(\sin \theta\) , \(\cos \theta\) and \(\tan \theta\) behave in relation to each other. From the shapes and symmetries of the graphs \(y=\sin \theta\) , \(y=\cos \theta\) and \(y=\tan \theta\) , we can see that the green sector is defined by \(\cos \theta < \sin \theta < \tan \theta\) the yellow sector is defined by \(\tan \theta < \cos \theta < \sin \theta\) the blue sector is defined by \(\cos \theta < \tan \theta < \sin \theta\) . |  |
|---|---|

However, we may need to do a bit more work to complete the sketch graphs. For example, do the graphs \(y=\tan \theta\) and \(y=\sin \theta\) cross between \(\theta = 0\) and \(\theta =\dfrac{\pi}{2}\)? Here are a couple of ways to think about this.

Using identities

Can you explain why the identity \(\tan \theta \equiv \dfrac{\sin \theta}{\cos \theta}\) tells us the following?

- For \(\theta\) between \(0\) and \(\dfrac{\pi}{2}\), \(\sin \theta < \tan \theta\).

- The graphs of \(y=\tan \theta\) and \(y=\sin \theta\) only meet when \(\theta\) is a multiple of \(\pi\).

Using a unit circle diagram

| We can compare side lengths of triangles in the unit circle diagram to obtain inequalities relating \(\sin \theta\) , \(\cos \theta\) and \(\tan \theta\) . In this way we can show that \(\sin \theta < \tan \theta\) for all values of \(\theta\) between \(0\) and \(\dfrac{\pi}{2}.\) (Hint: which triangle has \(\tan \theta\) as its hypotenuse?) |  |
|---|---|

Thinking more generally, we can also use the diagram to show the following.

- For small values of \(\theta\), \(\sin \theta < \tan \theta <\cos \theta\). This defines the red sector.

- \(\cos \dfrac{\pi}{4} = \sin \dfrac{\pi}{4}\)

- For \(\theta\) between \(\dfrac{\pi}{4}\) and \(\dfrac{\pi}{2}\), \(\cos \theta < \sin \theta < \tan \theta\), which defines the green sector, as we also saw before from the graph.

We now only need to decide which inequality defines the orange sector. You may find it helpful to look at the graphs or to visualise a point moving round the unit circle.

Using continuity

If we think about the behaviour of the functions as \(\theta\) increases from \(0\), we first have \(\sin \theta < \tan \theta < \cos \theta\) (which defines the red sector). Another inequality must define the orange sector, and then we have \(\cos \theta < \sin \theta < \tan \theta\) for \(\theta\) between \(\dfrac{\pi}{4}\) and \(\dfrac{\pi}{2}\), which defines the green sector.

As \(\tan \theta\) and \(\cos \theta\) are [continuous](https://undergroundmathematics.org/glossary/continuous-function) between \(0\) and \(\dfrac{\pi}{4}\), there must be some value of \(\theta\) between \(0\) and \(\dfrac{\pi}{4}\) where the graphs \(y=\tan \theta\) and \(y=\cos \theta\) cross over.

Therefore the inequality that defines the orange sector is \(\sin \theta < \cos \theta < \tan \theta\). Why is this the only option?

Why is the boundary between the green and yellow sectors different from the boundaries between other sectors?

The boundary of the orange and green sectors is at \(\theta=\dfrac{\pi}{4}\), and therefore the green sector is larger than the red sector. However, the yellow or blue sectors may be bigger than the green sector. Here are a few ways to tackle this problem.

Using exact values

What is the value of the different functions at \(\dfrac{3\pi}{4}\)?

Solving an equation

What are the solutions of \(\tan \theta = \cos \theta\)? Identities may help to make this into a simpler equation to solve.

Do you need to solve this equation completely to decide which sector is the largest?

It may be of interest that solutions of \(\tan \theta = \cos \theta\) are related to the [golden ratio](https://undergroundmathematics.org/glossary/golden-ratio).

Using symmetry

From the symmetry of the graphs, the angle between the boundary of the yellow and blue sectors and \(\theta=\pi\) must be the same as the angle between \(\theta=0\) and the boundary of the red and orange sectors. In other words, the blue and red sectors are the same size. What does this tell us about the sizes of the other sectors?

If you used more than one approach, can you connect them? For example, can you connect the symmetry argument with solving \(\tan \theta = \cos \theta\)?

To complete the circle we can use similar methods to those discussed above. Another approach might be to consider the possible orderings of \(\sin \theta\), \(\cos \theta\) and \(\tan \theta\).

Different orderings

How many ways can the functions \(\sin \theta\), \(\cos \theta\) and \(\tan \theta\) be ordered?

- Which of these ways of ordering occur between \(\theta =0\) and \(\theta=\pi\)?

- Which ways might be repeated?

- Will all these ways of ordering occur between \(\theta=0\) and \(\theta =2\pi\)?

Can you explain how the behaviour of the functions gives us these sectors and inequalities?

There were many ways to approach this problem. Instead of considering all three functions at the same time, we could have considered pairs of functions.

- When is \(\sin \theta < \cos \theta\)?

- When is \(\sin \theta < \tan \theta\)?

- When is \(\tan \theta < \cos \theta\)?

Can you see how these inequalities feature in the diagram above?
