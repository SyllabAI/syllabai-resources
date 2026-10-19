# Transformations using Matrices

Course: igcse-maths-b-16 · Section: Matrices

Source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/flashcards/matrices/transformations-using-matrices/


## Card 1 — keyword_definition (`fl_wMFKtsMnzKVxYN7B`)

**FRONT**

What are the **object** and the **image** in a matrix transformation?


**BACK**

The **object** is the original point `\left(x , y\right)` and the **image** is where that point ends up, written `\left(x ' , y '\right)`.

The dash notation is what keeps the two apart in working and on a diagram.


Spec links: `spcpt_cfsNsZkBNfQ2hWbY`


## Card 2 — question_and_answer (`fl_k4NH2RHj6bbRm8Pr`)

**FRONT**

How do you find the image of the point `\left(x , y\right)` under a matrix?


**BACK**

Write the point as a **column vector** and multiply the transformation matrix by it.

The result is a column vector holding the coordinates of the image point.


Spec links: `spcpt_cfsNsZkBNfQ2hWbY`


## Card 3 — question_and_answer (`fl_RFZrDyqnCNHqkK5K`)

**FRONT**

What is the image of `\left(2 , 3\right)` under `\begin{pmatrix} 4 & 5 \\ 1 & - 2 \end{pmatrix}`?


**BACK**

Multiplying gives `\begin{pmatrix} 4 \times 2 + 5 \times 3 \\ 1 \times 2 + \left(- 2\right) \times 3 \end{pmatrix} = \begin{pmatrix} 23 \\ - 4 \end{pmatrix}`.

Written back as coordinates, the image is `\left(23 , - 4\right)`.


Spec links: `spcpt_cfsNsZkBNfQ2hWbY`


## Card 4 — true_or_false (`fl_wjYvtGHb9vRQpWgW`)

**FRONT**

**True or False?**

The transformation matrix is written to the left of the point's column vector.


**BACK**

**True.**

The matrix goes **first** and the column vector second, as `\mathbf{M} \begin{pmatrix} x \\ y \end{pmatrix}`.

The other order is not even possible, since a $2 \times 1$ matrix cannot multiply a $2 \times 2$ one.


Spec links: `spcpt_cfsNsZkBNfQ2hWbY`


## Card 5 — question_and_answer (`fl_TXMj4xQYSsv8XPhB`)

**FRONT**

The image of $P$ under `\begin{pmatrix} 4 & 5 \\ 1 & - 2 \end{pmatrix}` is `\left(11 , 6\right)`. How can you find $P$?


**BACK**

Call $P$ the point `\left(x , y\right)`, multiply out, then equate the two entries to get $4 x + 5 y = 11$ and $x - 2 y = 6$.

Solving those **simultaneous equations** gives `P = \left(4 , - 1\right)`.


Spec links: `spcpt_cfsNsZkBNfQ2hWbY`


## Card 6 — question_and_answer (`fl_6gVb3SWr9r2QwkMg`)

**FRONT**

How can the inverse matrix be used to undo a transformation?


**BACK**

Multiply the image's column vector by $M^{-1}$, since $M^{-1} M$ is the identity matrix.

So if `\mathbf{M} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x ' \\ y ' \end{pmatrix}` then `\begin{pmatrix} x \\ y \end{pmatrix} = \mathbf{M}^{- 1} \begin{pmatrix} x ' \\ y ' \end{pmatrix}`.


Spec links: `spcpt_cfsNsZkBNfQ2hWbY`


## Card 7 — question_and_answer (`fl_nCSkgxDxfdzXW2wq`)

**FRONT**

How do you build the matrix for a transformation from the unit square?


**BACK**

Find where the two points `\left(1 , 0\right)` and `\left(0 , 1\right)` move to.

Their images become the **first and second columns** of the matrix, in that order.


Spec links: `spcpt_GG7jc43bG3xTkft4`


## Card 8 — fill_in_the_blanks (`fl_pwqrT3XsVbKcpZyK`)

**FRONT**

Under a reflection in the $x$-axis, `\left(1 , 0\right)` stays where it is and `\left(0 , 1\right)` moves to `\left(0 , - 1\right)`. Fill in the two missing entries.

`\begin{pmatrix} \_\_\_\_\_\_ & 0 \\ 0 & \_\_\_\_\_\_ \end{pmatrix}`


**BACK**

The completed matrix is:

`\begin{pmatrix} 1 & 0 \\ 0 & - 1 \end{pmatrix}`

The first column is the image of `\left(1 , 0\right)` and the second column is the image of `\left(0 , 1\right)`.


*Blanks: 0 — answers: []*

Spec links: `spcpt_GG7jc43bG3xTkft4`

Flags: fitb_no_blank_marker


## Card 9 — true_or_false (`fl_w2cGG6mQM2KJv7GM`)

**FRONT**

**True or False?**

A reflection in the $y$-axis leaves the point `\left(1 , 0\right)` where it is.


**BACK**

**False.**

That point moves to `\left(- 1 , 0\right)`, because reflecting in the $y$-axis changes the sign of the $x$-coordinate.

It is `\left(0 , 1\right)` that stays put, which is why the matrix is `\begin{pmatrix} - 1 & 0 \\ 0 & 1 \end{pmatrix}`.


Spec links: `spcpt_GG7jc43bG3xTkft4`


## Card 10 — question_and_answer (`fl_Q8kN9Kcw55kG6XrN`)

**FRONT**

What matrices represent reflections in $y = x$ and in $y = - x$?


**BACK**

Reflection in $y = x$ is `\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}` and reflection in $y = - x$ is `\begin{pmatrix} 0 & - 1 \\ - 1 & 0 \end{pmatrix}`.

Both have zeros on the leading diagonal, so it is the **signs** of the other two entries that tell them apart.


Spec links: `spcpt_GG7jc43bG3xTkft4`


## Card 11 — question_and_answer (`fl_nx8rVtvPNHJbm9Nz`)

**FRONT**

How does the matrix for a reflection in $y = x$ differ from the identity matrix?


**BACK**

Its 1s sit on the **other** diagonal, running from bottom left to top right.

The identity matrix leaves every point exactly where it is, while this one swaps each point's two coordinates over.


Spec links: `spcpt_GG7jc43bG3xTkft4`


## Card 12 — question_and_answer (`fl_g56vK6tDqNrFWCgr`)

**FRONT**

What matrix represents a rotation of 90° anticlockwise about the origin?


**BACK**

It is `\begin{pmatrix} 0 & - 1 \\ 1 & 0 \end{pmatrix}`.

The point `\left(1 , 0\right)` turns to `\left(0 , 1\right)` and `\left(0 , 1\right)` turns to `\left(- 1 , 0\right)`, and those two images become the columns.


Spec links: `spcpt_gkqmXrkrWnQC27tP`


## Card 13 — fill_in_the_blanks (`fl_wTF3F6tvhvZmwrJd`)

**FRONT**

Fill in the two missing entries of the matrix for a rotation of 180° about the origin.

`\begin{pmatrix} \_\_\_\_\_\_ & 0 \\ 0 & \_\_\_\_\_\_ \end{pmatrix}`


**BACK**

The completed matrix is:

`\begin{pmatrix} - 1 & 0 \\ 0 & - 1 \end{pmatrix}`

A half turn sends every point to the opposite side of the origin, so both coordinates change sign.


*Blanks: 0 — answers: []*

Spec links: `spcpt_gkqmXrkrWnQC27tP`

Flags: fitb_no_blank_marker


## Card 14 — question_and_answer (`fl_5XRVXSd9g4grVdHD`)

**FRONT**

What matrix represents a rotation of 270° anticlockwise about the origin?


**BACK**

It is `\begin{pmatrix} 0 & 1 \\ - 1 & 0 \end{pmatrix}`, since a turn of 270° anticlockwise is the same as **90° clockwise**.

The point `\left(1 , 0\right)` moves to `\left(0 , - 1\right)` and `\left(0 , 1\right)` moves to `\left(1 , 0\right)`.


Spec links: `spcpt_gkqmXrkrWnQC27tP`


## Card 15 — question_and_answer (`fl_j3DkkkWVCFbyNK2N`)

**FRONT**

Why do rotation questions always state a direction as well as an angle?


**BACK**

Because a turn of the same size clockwise and anticlockwise gives **different** matrices.

The one exception is 180°, which lands in the same place whichever way you turn.


Spec links: `spcpt_gkqmXrkrWnQC27tP`


## Card 16 — true_or_false (`fl_DR67ZNBJrQqQwrcx`)

**FRONT**

**True or False?**

A rotation of 180° about the origin has the same matrix as an enlargement of scale factor $- 1$.


**BACK**

**True.**

Both send every point `\left(x , y\right)` to `\left(- x , - y\right)`, so both are the matrix $- I$.

The two transformations are described in quite different words but have exactly the same effect.


Spec links: `spcpt_gkqmXrkrWnQC27tP`


## Card 17 — question_and_answer (`fl_KpY2qBPhfsQn3HJm`)

**FRONT**

What matrix represents an enlargement of scale factor $k$ centred on the origin?


**BACK**

It is `\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}`, which is the same as $k I$.

The point `\left(1 , 0\right)` moves to `\left(k , 0\right)` and `\left(0 , 1\right)` to `\left(0 , k\right)`, each sliding along its own axis.


Spec links: `spcpt_H5Sb2tfDwbqy6x2t`


## Card 18 — fill_in_the_blanks (`fl_2TDtS3kqP6rNQfw2`)

**FRONT**

The matrix `\begin{pmatrix} \frac{1}{4} & 0 \\ 0 & \frac{1}{4} \end{pmatrix}` represents a transformation. Fill in the two missing words.

It is an `\_\_\_\_\_\_` of scale factor `\_\_\_\_\_\_` with centre at the origin.


**BACK**

The completed description is:

It is an **enlargement** of scale factor **one quarter** with centre at the origin.

The matrix is $\frac{1}{4} I$, and any multiple of the identity matrix is an enlargement about the origin.


*Blanks: 0 — answers: []*

Spec links: `spcpt_H5Sb2tfDwbqy6x2t`

Flags: fitb_no_blank_marker


## Card 19 — true_or_false (`fl_ctYmqMkQYVn4JXB8`)

**FRONT**

**True or False?**

An enlargement matrix can have negative entries.


**BACK**

**True.**

Negative scale factors are allowed, so `\begin{pmatrix} - \frac{1}{2} & 0 \\ 0 & - \frac{1}{2} \end{pmatrix}` is an enlargement of scale factor $- \frac{1}{2}$.

A negative scale factor turns the shape through 180° about the origin as well as changing its size.


Spec links: `spcpt_H5Sb2tfDwbqy6x2t`


## Card 20 — question_and_answer (`fl_83bFkgB8ns236Hcr`)

**FRONT**

Why are the other two entries of an enlargement matrix always zero?


**BACK**

Because an enlargement about the origin moves `\left(1 , 0\right)` straight along the $x$-axis and `\left(0 , 1\right)` straight along the $y$-axis.

Neither image picks up any component in the other direction, so those two positions stay empty.


Spec links: `spcpt_H5Sb2tfDwbqy6x2t`


## Card 21 — question_and_answer (`fl_wTvkwWpvBTrPxxnJ`)

**FRONT**

Why is a matrix enlargement always centred on the origin?


**BACK**

Multiplying any matrix by the column vector for the origin gives the origin straight back again.

The origin therefore can never move, so it has to be the centre of any enlargement a matrix is able to represent.


Spec links: `spcpt_H5Sb2tfDwbqy6x2t`


## Card 22 — question_and_answer (`fl_6kGV6mWSvtdgzVdD`)

**FRONT**

What does the determinant of a transformation matrix tell you?


**BACK**

Its **size** is the area scale factor, so the image's area is the object's area multiplied by it.

Ignore any minus sign when scaling an area, because an area can never come out negative.


Spec links: `spcpt_5SJ9rhJbhSwKtDbv`


## Card 23 — fill_in_the_blanks (`fl_HfFzw9Rms5MswF9t`)

**FRONT**

A triangle of area 12 is transformed by a matrix whose determinant is 4. Fill in the missing value.

`\text{image area} = 12 \times \_\_\_\_\_\_ = 48`


**BACK**

The completed calculation is:

$\text{image area} = 12 \times 4 = 48$

This is far quicker than working out the coordinates of the image triangle and finding its area from those.


*Blanks: 0 — answers: []*

Spec links: `spcpt_5SJ9rhJbhSwKtDbv`

Flags: fitb_no_blank_marker


## Card 24 — true_or_false (`fl_N7nvHxny2TMJjZVn`)

**FRONT**

**True or False?**

Every reflection matrix has determinant $- 1$.


**BACK**

**True.**

A reflection does not change the area of a shape, so the size of its determinant is 1.

The minus sign records that the shape has been **flipped over**, which is exactly what a reflection does to it.


Spec links: `spcpt_5SJ9rhJbhSwKtDbv`


## Card 25 — question_and_answer (`fl_qzYyrfqkrt7JQv6T`)

**FRONT**

How can a whole triangle be transformed in a single multiplication?


**BACK**

Write its three vertices as the three **columns** of a $2 \times 3$ matrix, then multiply the transformation matrix by that.

The three columns of the answer are the vertices of the image triangle.


Spec links: `spcpt_5SJ9rhJbhSwKtDbv`


## Card 26 — question_and_answer (`fl_V3QbdbFgyGwTNqh4`)

**FRONT**

A transformation has determinant 1. What does that tell you about areas?


**BACK**

Areas are left **unchanged** by the transformation, because the area scale factor is 1.

Rotations are the usual example, since turning a shape does not alter its size at all.


Spec links: `spcpt_5SJ9rhJbhSwKtDbv`


## Card 27 — fill_in_the_blanks (`fl_SHwGb6fcg3rzQP8K`)

**FRONT**

A point is transformed first by $P$ and then by $Q$. Fill in the missing matrix.

`\mathbf{M} = \_\_\_\_\_\_ \mathbf{P}`


**BACK**

The completed result is:

$M = \mathrm{QP}$

The order in the multiplication runs **backwards** from the order in which the transformations actually happen.


*Blanks: 0 — answers: []*

Spec links: `spcpt_5snY7JPdgrqvFRhY`

Flags: fitb_no_blank_marker


## Card 28 — true_or_false (`fl_TMg7pQwHhbq4txV6`)

**FRONT**

**True or False?**

$\mathrm{PQ}$ represents transformation $P$ followed by transformation $Q$.


**BACK**

**False.**

$\mathrm{PQ}$ represents $Q$ **first**, followed by $P$.

The matrix nearest the point's column vector is the one that acts on it first, which is why the written order runs backwards.


Spec links: `spcpt_5snY7JPdgrqvFRhY`


## Card 29 — question_and_answer (`fl_rysDkSWvSFkzFk63`)

**FRONT**

How do you prove a combined transformation result using matrix multiplication?


**BACK**

Write each transformation as its own matrix, then multiply them together in the correct order.

If that product equals the matrix of the single transformation being claimed, the result is proved.


Spec links: `spcpt_5snY7JPdgrqvFRhY`


## Card 30 — question_and_answer (`fl_Pg799TZ9QTWrbtqm`)

**FRONT**

Reflection in the $y$-axis has matrix `\begin{pmatrix} - 1 & 0 \\ 0 & 1 \end{pmatrix}` and reflection in the $x$-axis has matrix `\begin{pmatrix} 1 & 0 \\ 0 & - 1 \end{pmatrix}`. What single matrix is the first followed by the second?


**BACK**

Multiply them as `\begin{pmatrix} 1 & 0 \\ 0 & - 1 \end{pmatrix} \begin{pmatrix} - 1 & 0 \\ 0 & 1 \end{pmatrix}`, putting the **second** transformation on the left.

The product is `\begin{pmatrix} - 1 & 0 \\ 0 & - 1 \end{pmatrix}`, which is a rotation of 180° about the origin.


Spec links: `spcpt_5snY7JPdgrqvFRhY`


## Card 31 — question_and_answer (`fl_n4bfJ6ZCZ9DVZSRT`)

**FRONT**

Once you have the combined matrix, how do you find a point's final image?


**BACK**

Multiply that combined matrix by the point's column vector, just once.

There is no need to apply the two transformations separately, and avoiding that is the whole advantage of combining them.


Spec links: `spcpt_5snY7JPdgrqvFRhY`

