---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/proving-laws-of-logs
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/scaffolded-task
- level/developing
resource_identity:
  ugm_id: proving-laws-of-logs
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 3
  resource_type_label: Scaffolded task
  level: Developing
  ref: 6156
  old_site_id: "A4_RT5_1"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: exp-and-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: exp-and-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "card sort forming a proof that log_c a + log_c b = log_c ab 'for any a,b > 0 and c>0, but c != 1', generalised from numeric examples - the laws of logarithms proved from indices; the canonical 3.2.1 task"
      rationale: "Canonical UGM title: Proving the laws of logarithms"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-10
---

# Proving the laws of logarithms

> Excerpt: Starting with some numeric examples of log laws, students are asked to generalise and then arrange and complete a set of cards to form a proof of one of the laws. This can be extended to cover the other log laws hence encouraging students to understand why they are true.

## Warm-up

Take a look at these results

\[\log_3 2 + \log_3 5 = \log_3 10\] \[\log_2 15 - \log_2 3 = \log_2 5\] \[2\log_5 7 = \log_5 49\] \[\frac{1}{3} \log_5 64 = \log_5 4\] \[(\log_5 7) \times (\log_7 11)=\log_5 11\]

How can you change the input values so that the equations still hold?

What happens if you change the base of the logarithms?

Can you state generalised versions of these results? What conditions must the base and the inputs satisfy?

## Proof sort

The cards below can be arranged to give a proof of the statement

\(\log_c a + \log_c b = \log_c ab\) for any \(a,b > 0\) and \(c>0\), but \(c \neq 1\).

Can you arrange the cards to give a convincing proof? You may need to include some extra algebraic steps or explanations if you think they would help to make the argument clearer or more convincing.

You might want to print out [the cards](https://undergroundmathematics.org/exp-and-log/proving-laws-of-logs/components/cards.pdf) and rearrange them.

Some blank cards have been included in the cards for printing in case you would like to use them to fill in some details.

One challenge we face when trying to prove something is making it clear what our proof is building on. Our starting point here is that we know how to manipulate indices or powers and we know a relationship between indices and logarithms. We will use results about manipulating indices to prove a result about manipulating logarithms.

Therefore \(ab = c^{x+y}\).

We can rewrite these equations to give us two equations involving powers.

Let \(\log_c a =x\) and \(\log_c b =y\).

Therefore \(\log_c ab = \log_c a + \log_c b\), as required.

\(c^x = a\) and \(c^y = b\)

We will prove that \(\log_c a + \log_c b = \log_c ab\) for any \(a,b > 0\) and \(c>0\), but \(c \neq 1\).

*We would like to express \(\log_c ab\) in terms of \(\log_c a\) and \(\log_c b\). If we try to express \(ab\) in terms of \(c\), we might be able to say more about \(\log_c ab\).*

## Solution

Here is one possible way of proving the result (with some extra statements added).

We will prove that \(\log_c a + \log_c b = \log_c ab\) for any \(a,b > 0\) and \(c>0\), but \(c \neq 1\).

*We know how to manipulate powers, so we could try to turn expressions involving logarithms into expressions involving powers. To do this, it might be helpful to name \(\log_c a\) and \(\log_c b\).*

Let \(\log_c a =x\) and \(\log_c b =y\).

We can rewrite these equations to give us two equations involving powers.

\(c^x = a\) and \(c^y = b\)

*We would like to express \(\log_c ab\) in terms of \(\log_c a\) and \(\log_c b\). If we try to express \(ab\) in terms of \(c\), we might be able to say more about \(\log_c ab\).*

\(ab = c^{x}c^{y}\)

Therefore \(ab = c^{x+y}\).

Therefore \(\log_c ab = \log_c a + \log_c b\), as required.

## Adapting the ideas

Can you adapt the ideas in the proof to produce convincing proofs of the following results?

\[\log_c a - \log_c b = \log_c \frac{a}{b}\]

\[n\log_c a = \log_c a^n\]

\[\dfrac{1}{n}\log_c a = \log_c a^{\frac{1}{n}}\]

\[(\log_a b) \times (\log_b c)=\log_a c\]

What conditions must \(a,b,c,n\) satisfy?
