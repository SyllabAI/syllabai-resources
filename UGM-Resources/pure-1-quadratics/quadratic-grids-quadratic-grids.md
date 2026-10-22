---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/quadratic-grids
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/rich-example
- level/introducing
resource_identity:
  ugm_id: quadratic-grids
  station: quadratics
  station_title: Quadratics
  resource_type_id: 2
  resource_type_label: Rich example
  level: Introducing
  ref: 6090
  old_site_id: E1_RT2_2
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Structure/multiplication-grid identities for quadratics.
      rationale: 'Canonical UGM title: “Quadratic grids”'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-1
---

# Quadratic grids

> Excerpt: This resource explores a method for factorising quadratic expressions using multiplication grids.

## Warm-up

In this resource, we are going to explore a method for factorising quadratic expressions using multiplication grids. We begin with a warm-up activity, which explores multiplication grids and builds up some of the ideas required for the factorising problem.

This multiplication grid for expanding \((x+4)(2x-3)\) is partially filled in. Fill in the rest of the grid to expand the brackets.

|  | \(x\) | \(+4\) |
| --- | --- | --- |
| \(2x\) | \(2x^2\) |  |
| \(-3\) |  | \(-12\) |

|  | \(x\) | \(+4\) |
| --- | --- | --- |
| \(2x\) | \(2x^2\) | \(+8x\) |
| \(-3\) | \(-3x\) | \(-12\) |

Therefore \((x+4)(2x-3) = 2x^2+8x-3x-12 = 2x^2+5x-12\).

**Solution**

What patterns do you notice in the grids as you expand the following brackets using this method?

1. \((x+5)(x+2)\)
2. \((x-1)(2x+3)\)
3. \((2x-3)(3x-2)\)
4. \((px+r)(qx+s)\)

- There seem to be some common factors in some of the rows and columns.
- There seems to be some relationship between the two diagonals in each grid.

**Things you might focus on**

How could this help in factorising quadratics?

## Warm-up solution

We begin by expanding the brackets using the grid method.

1. \((x+5)(x+2)\)

|  | \(x\) | \(+5\) |
| --- | --- | --- |
| \(x\) | \(x^2\) | \(+5x\) |
| \(+2\) | \(+2x\) | \(+10\) |

Therefore \((x+5)(x+2)=x^2+7x+10\).

1. \((x-1)(2x+3)\)

|  | \(x\) | \(-1\) |
| --- | --- | --- |
| \(2x\) | \(2x^2\) | \(-2x\) |
| \(+3\) | \(+3x\) | \(-3\) |

Therefore \((x-1)(2x+3)=2x^2+x-3\).

1. \((2x-3)(3x-2)\)

|  | \(2x\) | \(-3\) |
| --- | --- | --- |
| \(3x\) | \(6x^2\) | \(-9x\) |
| \(-2\) | \(-4x\) | \(+6\) |

Therefore \((2x-3)(3x-2)=6x^2-13x+6\).

1. \((px+r)(qx+s)\)

|  | \(px\) | \(+r\) |
| --- | --- | --- |
| \(qx\) | \(pqx^2\) | \(+rqx\) |
| \(+s\) | \(+psx\) | \(+rs\) |

Therefore \((px+r)(qx+s)=pqx^2+rqx+psx+rs\).

#### There seem to be some common factors in some of the rows and columns

Did you notice that the heading for each row and column is a [highest common factor](https://undergroundmathematics.org/glossary/highest-common-factor) of that row and column? For example, in question 3, \(2x\) is a highest common factor (hcf) of \(6x^2\) and \(-4x\), \(-3\) is an hcf of \(-9x\) and \(+6\), \(3x\) is an hcf of \(6x^2\) and \(-9x\) and \(-2\) is an hcf of \(-4x\) and \(+6\).

#### There seems to be some relationship between the two diagonals in each grid

Did you notice the products of the terms on the diagonals are equal to each other? For example, in question 1, one diagonal has \(x^2\) and \(+10\), the product of these terms is \(10x^2\). The other diagonal has \(+5x\) and \(+2x\), the product of these terms is also \(10x^2\).

The generalised form in question 4 can help explain this pattern:

- The \(x^2\) and constant terms multiply to \(pqx^2\times rs=pqrsx^2\).
- The other two cells (the \(x\) terms) multiply to \(psx\times qrx=pqrsx^2\).

So the products of the terms on the diagonals are the same.

This will help us when factorising quadratics.

## Problem

How can we use the multiplication grid method to help us factorise quadratics?

How can we factorise \(6x^2+7x+2\) using a multiplication grid?

The \(6x^2\) term is the product of the \(x\) terms, so goes in the top left cell.

The constant term \(+2\) is the product of constant terms, so goes in the bottom right cell.

So our grid starts out as

|  | \(\ldots x\) | \(\ldots\) |
| --- | --- | --- |
| \(\ldots x\) | \(6x^2\) |  |
| \(\ldots\) |  | \(+2\) |

**Which terms would you put in the grid first and why?**

The missing two entries inside the grid must add up to \(+7x\).

From the warm-up we know the products of the terms on the two diagonals are equal.

The product of \(6x^2\) and \(+2\) gives \(+12x^2\).

Therefore we need to find a pair of \(x\) terms that has a product of \(+12x^2\) and a sum of \(+7x\).

Pairs of \(x\) terms with a product of \(+12x^2\) are \(+12x\) and \(+x\), \(-12x\) and \(-x\), \(+6x\) and \(+2x\), \(-6x\) and \(-2x\), \(+4x\) and \(+3x\), \(-4x\) and \(-3x\).

Only \(+4x\) and \(+3x\) sum to \(+7x\) so we can now fill in the grid completely.

|  | \(\ldots x\) | \(\ldots\) |
| --- | --- | --- |
| \(\ldots x\) | \(6x^2\) | \(+4x\) |
| \(\ldots\) | \(+3x\) | \(+2\) |

Does it matter which way round the \(+4x\) and \(+3x\) go? Try both ways and see what happens.

**How do you work out the other numbers in the grid?**

We fill in the outside of the grid by looking for the highest common factor of the first column.

|  | \(3x\) | \(\ldots\) |
| --- | --- | --- |
| \(\dots x\) | \(6x^2\) | \(+4x\) |
| \(\ldots\) | \(+3x\) | \(+2\) |

We then fill in the rest of the grid to make the multiplication work.

|  | \(3x\) | \(+2\) |
| --- | --- | --- |
| \(2x\) | \(6x^2\) | \(+4x\) |
| \(+1\) | \(+3x\) | \(+2\) |

 So what is the factorisation of

\(6x^2+7x+2\)

?

**What do we do next?**

\[6x^2+7x+2 = (3x+2)(2x+1)\]

**Factorisation**

### Factorising quadratics

Here are a few quadratic expressions you can use for practising this method.

1. \(4x^2+7x+3\)
2. \(3x^2+13x-10\)
3. \(6x^2-5x+1\)
4. \(4x^2-2x-12\)
5. \(2x^2-3xy-2y^2\)

#### Reflecting

We filled in the outside of the grid by finding the highest common factor of the first column. Did we need to use the first column or could we have used the first row? Could we have used another row or column? Can you explain your reasoning.

How does this method of factorising quadratics compare to other methods you know?

You may wish to explore these ideas further in [Factorisable quadratics](https://undergroundmathematics.org/quadratics/factorisable-quads).

## Solution

We can partially fill in a multiplication grid with this quadratic:

|  | \(\ldots x\) | \(\ldots\) |
| --- | --- | --- |
| \(\ldots x\) | \(4x^2\) |  |
| \(\ldots\) |  | \(+3\) |

The remaining two cells must add to \(+7x\) and multiply to \(12x^2\), so they are \(+4x\) and \(+3x\), giving:

|  | \(\ldots x\) | \(\ldots\) |
| --- | --- | --- |
| \(\ldots x\) | \(4x^2\) | \(+4x\) |
| \(\ldots\) | \(+3x\) | \(+3\) |

We fill in the outside of the grid by looking for the highest common factor of the first column, which in this case is \(x\).

|  | \(x\) | \(\ldots\) |
| --- | --- | --- |
| \(\ldots x\) | \(4x^2\) | \(+4x\) |
| \(\ldots\) | \(+3x\) | \(+3\) |

We then fill in the rest of the grid to make the multiplication work.

|  | \(x\) | \(+1\) |
| --- | --- | --- |
| \(4x\) | \(4x^2\) | \(+4x\) |
| \(+3\) | \(+3x\) | \(+3\) |

 The completed grid is as follows.

 So

\(4x^2+7x+3= (x+1)(4x+3)\)

.

**Factorisation**

We can partially fill in a multiplication grid with this quadratic:

|  | \(\ldots x\) | \(\ldots\) |
| --- | --- | --- |
| \(\ldots x\) | \(3x^2\) |  |
| \(\ldots\) |  | \(-10\) |

The remaining two cells must add to \(+13x\) and multiply to \(-30x^2\), so they are \(-2x\) and \(+15x\), giving:

|  | \(\ldots x\) | \(\ldots\) |
| --- | --- | --- |
| \(\ldots x\) | \(3x^2\) | \(-2x\) |
| \(\ldots\) | \(+15x\) | \(-10\) |

We fill in the outside of the grid by looking for the highest common factor of the first column and then fill in the rest of the grid to make the multiplication work.

|  | \(3x\) | \(-2\) |
| --- | --- | --- |
| \(x\) | \(3x^2\) | \(-2x\) |
| \(+5\) | \(+15x\) | \(-10\) |

 The completed grid is as follows.

 So

\(3x^2+13x-10= (3x-2)(x+5)\)

.

**Factorisation**

We can partially fill in a multiplication grid with this quadratic:

|  | \(\ldots x\) | \(\ldots\) |
| --- | --- | --- |
| \(\ldots x\) | \(6x^2\) |  |
| \(\ldots\) |  | \(+1\) |

The remaining two cells must add to \(-5x\) and multiply to \(6x^2\), so they are \(-2x\) and \(-3x\), giving:

|  | \(\ldots x\) | \(\ldots\) |
| --- | --- | --- |
| \(\ldots x\) | \(6x^2\) | \(-2x\) |
| \(\ldots\) | \(-3x\) | \(+1\) |

We fill in the outside of the grid by looking for the highest common factor of the first column and then fill in the rest of the grid to make the multiplication work.

|  | \(3x\) | \(-1\) |
| --- | --- | --- |
| \(2x\) | \(6x^2\) | \(-2x\) |
| \(-1\) | \(-3x\) | \(+1\) |

 The completed grid is as follows.

 So

\(6x^2-5x+1=(3x-1)(2x-1)\)

.

**Factorisation**

We can partially fill in a multiplication grid with this quadratic:

|  | \(\ldots x\) | \(\ldots\) |
| --- | --- | --- |
| \(\ldots x\) | \(4x^2\) |  |
| \(\ldots\) |  | \(-12\) |

The remaining two cells must add to \(-2x\) and multiply to \(-48x^2\), so they are \(+6x\) and \(-8x\), giving:

|  | \(\ldots x\) | \(\ldots\) |
| --- | --- | --- |
| \(\ldots x\) | \(4x^2\) | \(+6x\) |
| \(\ldots\) | \(-8x\) | \(-12\) |

In this question, there are two ways that we can fill in the outside of the grid, depending on whether we start by finding the highest common factor of the first column or of the first row. (Alternatively, if we always start by finding the highest common factor of the first column, there are two different ways depending upon which way round we put the \(-8x\) and \(+6x\) in the grid.)

|  | \(2x\) | \(-4\) |
| --- | --- | --- |
| \(2x\) | \(4x^2\) | \(-8x\) |
| \(+3\) | \(+6x\) | \(-12\) |

So \(4x^2-2x-12= (2x-4)(2x+3)\).

|  | \(x\) | \(-2\) |
| --- | --- | --- |
| \(4x\) | \(4x^2\) | \(-8x\) |
| \(+6\) | \(+6x\) | \(-12\) |

So \(4x^2-2x-12= (x-2)(4x+6)\).

In the previous questions, it made no difference which one we started with. Why are there two possible answers in this case?

**Factorisation**

Why are there two different possibilities here?

Our quadratic has a factor of \(2\), and so our two factorisations each have a term which has a factor of \(2\):

So actually these are the same factorisation, just with the factor of \(2\) included in the two different brackets. It is a good idea to take out any common factors from the answer as well, as then the structure of the quadratic becomes a little clearer.

In fact, it would probably be easier to take out the common factor of \(2\) before beginning to factorise: we then have \[4x^2-2x-12=2(2x^2-x-6).\]

The resulting quadratic \(2x^2-x-6\) is also easier to factorise, as the numbers involved are smaller.

\[\begin{align*} (4x+6)(x-2)&= 2(2x+3)(x-2)\\ (2x+3)(2x-4)&= 2(2x+3)(x-2) \end{align*}\]

**Explanation**

This looks a little different, as there are now appearances of \(x\) and \(y\). But we can still partially fill in a multiplication grid, only this time, the factors are going to involve \(x\) and \(y\) which means the grid will have this form:

|  | \(\ldots x\) | \(\ldots y\) |
| --- | --- | --- |
| \(\ldots x\) | \(2x^2\) |  |
| \(\ldots y\) |  | \(-2y^2\) |

The remaining two cells must add to \(-3xy\) and multiply to \(-4x^2y^2\).

Pairs of \(xy\) terms which multiply to \(-4x^2y^2\) are \(4xy\) and \(-xy\), \(-4xy\) and \(xy\), \(2xy\) and \(-2xy\). Only \(-4xy\) and \(+xy\) sum to \(-3xy\). This gives the grid:

|  | \(\ldots x\) | \(\ldots y\) |
| --- | --- | --- |
| \(\ldots x\) | \(2x^2\) | \(-4xy\) |
| \(\ldots y\) | \(+xy\) | \(-2y^2\) |

We can now fill in the outside of the grid:

|  | \(x\) | \(-2y\) |
| --- | --- | --- |
| \(2x\) | \(2x^2\) | \(-4xy\) |
| \(+y\) | \(+xy\) | \(-2y^2\) |

 So

\(2x^2-3xy-2y^2=(x-2y)(2x+y)\)

.

**Factorisation**

### Reflecting

How does this method of factorising quadratics compare to other methods you know?

You may have learnt some other methods, and using whichever seems most appropriate to the context is often sensible.
