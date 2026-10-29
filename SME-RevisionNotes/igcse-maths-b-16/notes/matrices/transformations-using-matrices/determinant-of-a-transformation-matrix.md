---
note_id: "rn_pmqtYNXCYJXbcP56"
title: "Determinant of a Transformation Matrix"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/transformations-using-matrices/determinant-of-a-transformation-matrix
path: matrices/transformations-using-matrices/determinant-of-a-transformation-matrix
updated_at: "2026-01-14T14:31:38.409Z"
spec_point_ids: ["spcpt_5SJ9rhJbhSwKtDbv"]
spec_point_codes: []
guided_study: false
---

# Determinant of a Transformation Matrix

## Determinant of a transformation matrix

> **Spec point** — `spcpt_5SJ9rhJbhSwKtDbv`

## Determinant of a transformation matrix

### What does the determinant of a transformation matrix represent?

- When a 2×2 matrix is used to represent a **transformation**

  - the **determinant **of the matrix is the **area scale factor** of the transformation
  - I.e. the **area** of a transformed shape is equal to
  
    - the area of the original shape
    - times the determinant of the transformation matrix
- The **determinant** of a 2×2 matrix $( \begin{gathered} a b \\ c d \end{gathered} )$ is $ad-bc$

> **Worked Example**
> A triangle has vertices with coordinates (1, -3), (7, -3) and (3, 1).
> 
> (a) Find the coordinates of the vertices of the image triangle when that triangle is transformed by the matrix $M = ( \begin{gathered} - \sqrt{3} & - 1 \\ 1 - \sqrt{3} \end{gathered} )$.
> 
> **Answer:**
> 
> > *You can represent the triangle as a 2×3 matrix of vertices*
> 
> - *This will be the coordinates of the vertices as column vectors, but written in a single matrix*
> 
> $( \begin{gathered} 1 7 3 \\ - 3 & - 3 & 1 \end{gathered} )$
> 
> > *To transform the triangle, multiply its matrix by the transformation matrix* $M$
> 
> $\begin{gathered} ( \begin{gathered} - \sqrt{3} & - 1 \\ 1 - \sqrt{3} \end{gathered} ) ( \begin{gathered} 1 7 3 \\ - 3 & - 3 & 1 \end{gathered} ) \\ = ( \begin{gathered} ( - \sqrt{3} ) \times 1 + ( - 1 ) \times ( - 3 ) & ( - \sqrt{3} ) \times 7 + ( - 1 ) \times ( - 3 ) & ( - \sqrt{3} ) \times 3 + ( - 1 ) \times 1 \\ 1 \times 1 + ( - \sqrt{3} ) \times ( - 3 ) & 1 \times 7 + ( - \sqrt{3} ) \times ( - 3 ) & 1 \times 3 + ( - \sqrt{3} ) \times 1 \end{gathered} ) \\ = ( \begin{gathered} 3 - \sqrt{3} & 3 - 7 \sqrt{3} & - 1 - 3 \sqrt{3} \\ 1 + 3 \sqrt{3} & 7 + 3 \sqrt{3} & 3 - \sqrt{3} \end{gathered} ) \end{gathered}$
> 
> > *Write the new vertices as coordinates*
> 
> **Final answer:** $( 3 - \sqrt{3} , 1 + 3 \sqrt{3} )$**, **$( 3 - 7 \sqrt{3} , 7 + 3 \sqrt{3} )$** and **$( - 1 - 3 \sqrt{3} , 3 - \sqrt{3} )$
> ** **
> 
> (b) Find the area of the image triangle.
> 
> **Answer:**
> 
> > *The original and transformed triangles look like this:*
> 
> ![A graph showing two triangles. The larger triangle has vertices with surds, and the smaller triangle below has vertices at (1,-3), (3,1), and (7,-3).](assets/7220d16bc884-38404-picture1.png)
> 
> *Trying to calculate the area of the transformed triangle directly would be quite challenging, to say the least!*
> 
> > *However the area of the original triangle is easy to calculate*
> 
> - *It has a base of 6, and a height of 4*
> - *Use* $\mathrm{Area}=\frac{1}{2}\times\mathrm{base}\times\mathrm{height}$
> 
> $\mathrm{area} \mathrm{of} \mathrm{original} \mathrm{triangle}=\frac{1}{2}\times6\times4=12$
> 
> > *Find the determinant of the transformation matrix* $M = ( \begin{gathered} - \sqrt{3} & - 1 \\ 1 - \sqrt{3} \end{gathered} )$
> 
> - *The **determinant** of a 2×2 matrix *$( \begin{gathered} a b \\ c d \end{gathered} )$ *is* $ad-bc$
> 
> `| determinant of M | = ( - sqrt( 3 ) x ( - sqrt( 3 ) - ( - 1 ) x 1 | | _ = 3 - ( - 1 ) | | _ = 4 |`
> 
> > *That is the area scale factor of the transformation*
> 
> - *So multiply the original area by 4 to find the transformed area*
> 
> $12\times4=48$
> 
> **Final answer:** **Area of the image triangle is 48**
