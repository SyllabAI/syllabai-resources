---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/two-way-algebra
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/many-ways-problem
- level/introducing
resource_identity:
  ugm_id: two-way-algebra
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Introducing
  ref: 8982
  old_site_id: E2_RT6_1
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-algebra
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-algebra
    validation_status: SUGGESTED
  spec_points:
  - code: E2.5.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Two-way table of equations and inequalities by the types of solutions they give — solving
        linear equations and reading solution structure; E2.5.2 register.
      rationale: 'Canonical UGM title: “Two-way algebra”'
      validation_status: SUGGESTED
  - code: E2.6.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Two-way table of equations and inequalities by the types of solutions they give — solving
        linear equations and reading solution structure; E2.5.2 register.
      rationale: 'Canonical UGM title: “Two-way algebra”'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-19
---

# Two-way algebra

> Excerpt: This resource encourages students to appreciate the different types of solutions that various equations and inequalities can give by asking them to fill in headings and empty cells in a two-way table.

## Problem

Each column and row has a property which some equation or inequality may or may not have. If an example has the properties of the corresponding row and column, then it can appear in that cell.

We have omitted some headings, and some entries in cells. Can you complete the table?

|  |  | Solutions lie between \(1\) and \(6\) |  | All values of \(x\) are solutions |
| --- | --- | --- | --- | --- |
|  | \[x^2 +4 =0\] | \[5x - 3 = 9-x \] |  |  |
| Inequalities |  |  | \[8 -x < 2 - 3x\] |  |
|  | \(y = 3x\) and \(\frac{y}{3} - 1 = x\) |  | \(y = 3x+5\) and \(y = -x-3\) |  |

- Did you have any choice about the row and column headings?
- Can you simplify any of your examples?
- Do all your examples require some ‘solving’ to check they fit the attributes of the cell? If not, can you make it so that they all do?
- If we required all the cells to contain quadratics, would it still be possible to fill all the cells?

## A possible solution

Here is one possible solution.

|  | No real solutions | Solutions lie between \(1\) and \(6\) | Negative solutions only | All values of \(x\) are solutions |
| --- | --- | --- | --- | --- |
| Equations in \(x\) | \[x^2 +4 =0\] | \[5x - 3 = 9-x \] | \[2x - 5 = -12\] | \[(x-1)^2 -1 = x^2 - 2x\] |
| Inequalities | \[x^2<0\] | \[5 < 2x - 3 < 15\] | \[8 -x < 2 - 3x\] | \[x^2 ≥ 0\] |
| Simultaneous equations in \(x\) and \(y\) | \(y = 3x\) and \(\frac{y}{3} - 1 = x\) | \(3y = x\) and \(y = x - 2\) | \(y = 3x+5\) and \(y = -x-3\) | \(y = 2x\) and \(\frac{y}{2}= x\) |

We have put the first row as ‘Equations in \(x\)’, so examples all have a single variable only. How is this different from just writing ‘Equations’? Could simultaneous equations appear here if this was your row heading?

Instead of giving the equation \(5x - 3 = 9-x\), which has a solution between \(1\) and \(6\), we could have written \(x = 2\). This is still an equation, albeit a very simple one, that has the properties required. Is it possible to give all the examples in this form, so you can immediately see whether they have the attributes of their cell?

Do all the examples require some ‘solving’ to check they have the attributes of the cell? If not, can you make it so that they all do?

If you gave an answer such as \(x = \sqrt{-4}\) for an equation that has no real solutions, you can easily see that it matches the properties of the cell. However, you could have written it as \(x^2 + 4 = 0\), so that it requires some manipulation to check it is correct.

It might be best to try to sketch what the answers might look like graphically to help you decide if they are all possible.
