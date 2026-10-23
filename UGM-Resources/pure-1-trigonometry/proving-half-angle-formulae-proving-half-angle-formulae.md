---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/proving-half-angle-formulae
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/scaffolded-task
- level/developing
resource_identity:
  ugm_id: proving-half-angle-formulae
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 3
  resource_type_label: Scaffolded task
  level: Developing
  ref: 6029
  old_site_id: G5_RT5_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-compound-angles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-compound-angles
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-compound-angles/proving-half-angle-formulae/download/teacher-notes.pdf
  kind: printable
---

# Proving half-angle formulae

> Excerpt: Students use diagrams to construct a geometric proof of the formula $\cos^{2} \frac{\theta}{2}=\frac{1}{2}(1+\cos \theta)$.  The same ideas can be adapted to give proofs of related results for $\sin^{2}\tfrac{\theta}{2}$ and $\tan^{2}\tfrac{\theta}{2}$.

## Problem

Take a look at the identities below.

\[\cos^2 \frac{\theta}{2} \equiv \frac{1}{2}(1+\cos \theta) \quad \quad \quad \sin^2 \frac{\theta}{2} \equiv \frac{1}{2}(1-\cos \theta)\]

You may well know enough trigonometric identities to be able to prove these results algebraically, but you could also prove them using geometry. We have provided some diagrams that may help you to prove the result for \(\cos^2 \frac{\theta}{2}\). Can you link the diagrams together to form a proof?

You may find it helpful to group the diagrams together in different ways or look for links between pairs of diagrams. You don’t need to use all the diagrams in your proof and you may prefer to add some of your own diagrams. The diagrams are available as a print out. There is an extra card in case you’d like to include another diagram in your proof.

Suggestion: strategy

It might be easier to prove \(1+\cos \theta \equiv 2\cos^2 \frac{\theta}{2}\).

Can you relate the diagrams to either the left-hand side of the identity or to the right-hand side?

Is there a diagram that shows a length that corresponds to \(1+\cos \theta\)?

Suggestion: diagram

Can you prove the result for \(\sin^2 \frac{\theta}{2}\) in a similar way?

## Possible proof

Take a look at the identities below.

\[\cos^2 \frac{\theta}{2} \equiv \frac{1}{2}(1+\cos \theta) \quad \quad \quad \sin^2 \frac{\theta}{2} \equiv \frac{1}{2}(1-\cos \theta)\]

You may well know enough trigonometric identities to be able to prove these results algebraically, but you could also prove them using geometry. Here are some diagrams that may help you to prove the result for \(\cos^2 \frac{\theta}{2}\). Can you link the diagrams together to form a proof?

You may find it helpful to group the diagrams together in different ways or look for links between pairs of diagrams. You don’t need to use all the diagrams in your proof and you may prefer to add some of your own diagrams. The diagrams are available as a print out. There is an extra card in case you’d like to include another diagram in your proof.

There are many ways to prove this result using these diagrams. Here is one approach.

We are aiming for the result \(1+ \cos \theta \equiv 2\cos^2 \frac{\theta}{2}\) as this is equivalent to the identity we want to prove. We will express the line segment \(CB\) in two different ways. One will involve \(\cos \theta\) and one will involve \(\cos \frac{\theta}{2}\).

\(\cos \theta = \frac{OB}{1}\) so \(OB = \cos \theta\) and therefore \(CB=1+\cos \theta\).

Triangle \(\triangle ACO\) is isosceles and \(\theta\) is the exterior angle at \(O\), so \(\angle ACO = \frac{\theta}{2}\). Looking at the right-angled triangle \(\triangle DCO\), we see that \(\cos \frac{\theta}{2}=CD\). Therefore \(CA=2\cos\frac{\theta}{2}\).

(The first diagram was in the suggestion and may help you to see how triangle \(\triangle COA\) is related to the other triangles on the cards.) In triangle \(\triangle CBA\), \(\cos \frac{\theta}{2} = \frac{CB}{CA}\) and therefore \(CB = 2 \cos^2 \frac{\theta}{2}\).

We have managed to write \(CB\) in two different ways, and so equating these expressions for \(CB\) gives us the result we wanted.

A similar approach could be used to prove that \(2\sin^2 \dfrac{\theta}{2}= 1-\cos \theta\).

From the first diagram we can see that \(BE = 1-\cos\theta\). From the second diagram and using a similar approach to the proof for \(\cos\) above, we see that \(CE=2\) and \(\angle ECA = \frac{\theta}{2}\), so \(EA=2 \sin \frac{\theta}{2}\).

The triangles \(\triangle EAB\) and \(\triangle ACE\) are similar, so \(\angle EAB\) is \(\frac{\theta}{2}\). From triangle \(EAB\) we can see that \(\sin \frac{\theta}{2}= \frac{BE}{AE}\) so \(BE=2 \sin^2 \frac{\theta}{2}\). Equating the two ways we can write \(BE\) gives us the result we wanted.

## Looking again

Take another look at the identities.

\[\cos^2 \frac{\theta}{2} \equiv \frac{1}{2}(1+\cos \theta) \quad \quad \quad \sin^2 \frac{\theta}{2} \equiv \frac{1}{2}(1-\cos \theta)\]

The first says that \(\cos^2 \frac{\theta}{2}\) is the mean of \(1\) and \(\cos \theta\). What does this tell you geometrically?

Suggestion

Can you use this diagram to connect the geometry with this way of looking at the identity?

Can you use the same ideas to think about the identity for \(\sin^2 \frac{\theta}{2}\)?

Can you draw a diagram to illustrate the following results for \(\tan \frac{\theta}{2}\)? \[\tan \frac{\theta}{2} \equiv \frac{\sin \theta}{1+\cos \theta}\] and \[\tan \frac{\theta}{2}\equiv \frac{1-\cos \theta}{\sin \theta}\]

Diagram for \(\tan \theta\)

This diagram could be used to show the two identities for \(\tan \dfrac{\theta}{2}\).

For which values of \(\theta\) are these identities true?
