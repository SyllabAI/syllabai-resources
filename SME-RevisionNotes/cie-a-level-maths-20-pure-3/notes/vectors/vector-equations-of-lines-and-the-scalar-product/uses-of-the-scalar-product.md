---
note_id: "rn_NCy2hgSCyFxjqhc4"
title: "Uses of the Scalar Product"
source: https://www.savemyexams.com/a-level/maths/cie/20/pure-3/revision-notes/vectors/vector-equations-of-lines-and-the-scalar-product/uses-of-the-scalar-product
path: vectors/vector-equations-of-lines-and-the-scalar-product/uses-of-the-scalar-product
updated_at: "2026-08-19T09:37:28.018Z"
spec_point_ids: ["spcpt_GjkGPBQxw5qX3wHd"]
spec_point_codes: []
guided_study: true
---

# Uses of the Scalar Product

## Uses of the Scalar Product

> **Spec point** — `spcpt_GjkGPBQxw5qX3wHd`

## Uses of the scalar product

This revision note covers several applications of the scalar product for vectors – namely, how you can use the scalar product to:

- find the angle between vectors or lines
- test whether vectors or lines are perpendicular
- find the closest distance from a point to a line

### How do I find the angle between two vectors?

- Recall that a formula for the scalar (or ‘dot’) between vectors $a$ and $b$ is

$a \times b = \left| a \right| \left| b \right| \cos \\theta$

- where $θ$ is the angle between the vectors when they are placed **‘base to base’**

  - that is, when the vectors are positioned so that they start at the same point
- We arrange this formula to make $\mathrm{cos}θ$ the subject:

  - $\cos \\theta = \frac{a \times b}{\left| a \right| \left| b \right|}$
- To find the angle between two vectors

  - Calculate the scalar product between them
  - Calculate the magnitude of each vector
  - Use the formula to find $\mathrm{cos}θ$
  - Use inverse trig to find $θ$

### How do I find the angle between two lines in 3D?

- To find the angle between two lines, find the angle between their **direction vectors**

- For example, if the lines have equations $r=a_{1}+sd_{1}$ and $r=a_{2}+td_{2}$, then the angle $θ$ between the lines is given by

$\\theta = \cos ^{- 1} ( \frac{d_{1} \times d_{2} }{\left| d_{1} \right| \left| d_{2} \right|} )$

### How do I know if vectors or lines are perpendicular?

- Two (non-zero) vectors $a$ and $b$ are **perpendicular** if, and only if, $a \times b = 0$

  - If the **a **and **b **are perpendicular then:
  
    - $\\theta = 90^{\circ} \Leftrightarrow \cos \\theta = 0 \Leftrightarrow \left| a \right| \left| b \right| \cos \\theta = 0 \Leftrightarrow a \times b = 0$
  - If  $a \times b = 0$ then:
  
    - $\left| a \right| \left| b \right| \cos \\theta = 0 \Leftrightarrow \cos \\theta = 0 \Leftrightarrow \\theta = 90^{\circ} \Leftrightarrow$ **a **and **b **are perpendicular
  - For example, the vectors $2i-3j+5k$ and $-4i-j+k$ ** **are perpendicular since

$( 2 i - 3 j + 5 k ) \times ( - 4 i - j + k ) = 2 \times ( - 4 ) + ( - 3 ) \times ( - 1 ) + 5 \times 1 = - 8 + 3 + 5 = 0$

### How do I find the shortest distance from a point to a line?

- Suppose that we have a line $l$ with equation $r=a+td$  and a point** **$P$ not on $l$
- Let $F$ be the **point on** $l$ which is **closest to **$P$ (sometimes called the **foot of the perpendicular**)

  - Then the line between $F$ and $P$ will be perpendicular to the line $l$
- To find the closest point $F$

  - Call $f=\overset{\rightarrow}{\mathrm{OF}}$ and $p=\overset{\rightarrow}{OP}$
  - Since $F$ lies on $l$, we have $f=a+t_{0}d$, for a unique real number $t_{0}$
  - Find the vector $\overset{\rightarrow}{FP}$ using $p-f$
  - $\overset{\rightarrow}{FP}$ **is perpendicular to **$d$ so form an equation using $( p - f ) \times d = 0$
  - Solve this equation to find the value of $t_{0}$
  - Use the value of $t_{0}$ to find $f$
- The **shortest distance** between the point $P$ and the line $l$ is the **length **$\left| \vec{FP} \right|$
- Note that the **shortest distance between the point and the line** is sometimes referred to as the **length of the perpendicular**

![7-3-4-foot-of-the-perpendicular](../../../assets/77610fab03a0-7-3-4-foot-of-the-perpendicular.png)

> **Worked Example**
> ![7-3-4-uses-of-scalar-product-we-solution-part-1](assets/8ad1fbf783a7-7-3-4-uses-of-scalar-product-we-solution-part-1.png)
> 
> ![7-3-4-uses-of-scalar-product-we-solution-part-2](assets/3b2c18056eae-7-3-4-uses-of-scalar-product-we-solution-part-2.png)

> **Exam Hint**
> It can be easier and clearer to work with column vectors when dealing with scalar products.
