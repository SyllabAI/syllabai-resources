## Linear Transformation

A transformation in the $x$ and $y$ plane dimensions can be defined by describing the matrix used to transform one coordinate to another, often referred to as the image

* if we have matrix $M$, we can use it to transform a position vector $S$ and create a image of $S$ ($S’$) by multiplying them together

### Example question

* $S$ has the coordinate $\begin{pmatrix} 4 \\ -5 \end{pmatrix}$, use $M = \begin{bmatrix} 6 & 3 \\ -8 & 2 \end{bmatrix}$ to create a image of $S$
* $\begin{bmatrix} 6 & 3 \\ -8 & 2 \end{bmatrix} \begin{bmatrix} 4 \\ -5 \end{bmatrix} = S’$
* $\begin{bmatrix} (6+4) + (3-5) \\ (-8+4) + (2-5) \end{bmatrix}$
* $\begin{bmatrix} 10 - 2 \\ -4 - 3 \end{bmatrix}$
* $\begin{bmatrix} 8 \\ -7 \end{bmatrix} = S’$

---

## Reflections and rotations

* there are various identities used to reflect and rotate matrices

  * a reflection in the $y$ axis $= \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$

  * a reflection in the $x$ axis $= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$

  * a reflection in line $y=x$ (a diagonal line) $= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$

  * a reflection in line $y=-x$ (a diagonal line) $= \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$