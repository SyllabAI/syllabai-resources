# a-level-pure-mathematics-12-vectors — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Components and resultants

![3D axes with a vector from the origin to the point (3,-2,5), with dashed component projections labelled 3i, -2j and 5k](../assets/001-c0e60ea7-31db-48a5-9e06-3d14d4fb7b5e.jpeg)
A vector has magnitude and direction, so in 3D we describe it by how far it moves in the $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{k}$ directions. For example, $3\mathbf{i}-2\mathbf{j}+5\mathbf{k}$ means 3 units in $x$, 2 units in the negative $y$ direction, and 5 units in $z$.

The same vector can be written as a column vector:
$$
\begin{pmatrix}
3\\
-2\\
5
\end{pmatrix}
$$
Here $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{k}$ are unit vectors, each with length 1.

To add or subtract vectors, work component by component. For example,
$$
(x_1\mathbf{i}+y_1\mathbf{j}+z_1\mathbf{k})+(x_2\mathbf{i}+y_2\mathbf{j}+z_2\mathbf{k})=(x_1+x_2)\mathbf{i}+(y_1+y_2)\mathbf{j}+(z_1+z_2)\mathbf{k}
$$
the $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{k}$ parts are combined separately, and the final single vector is the resultant.

## Position vectors and displacement

A position vector tells you where a point is relative to the origin $O$. If point $A$ has position vector $\mathbf{a}$, then $\vec{OA}=\mathbf{a}$.

A displacement vector tells you how to move from one point to another. If $A$ has position vector $\mathbf{a}$ and $B$ has position vector $\mathbf{b}$, then the displacement between them is calculated as:

$$$\vec{AB}=\mathbf{b}-\mathbf{a}$$

This is the head minus tail rule. If you subtract the other way round, you reverse the direction. So $\vec{BA}=\mathbf{a}-\mathbf{b}=-\vec{AB}$, which has the same length as $\vec{AB}$ but points the opposite way.

## Worked example: finding a vector and its length

Suppose points $A$ and $B$ have position vectors $2\mathbf{i}-3\mathbf{j}+4\mathbf{k}$ and $-5\mathbf{i}+\mathbf{j}+6\mathbf{k}$. First find the displacement by subtracting the position vector of $A$ from that of $B$:
$$\vec{AB}=(-5-2)\mathbf{i}+(1-(-3))\mathbf{j}+(6-4)\mathbf{k}=-7\mathbf{i}+4\mathbf{j}+2\mathbf{k}$$

Now use the magnitude formula for a 3D vector. Substitute the three components into the radical expression:
$$|\vec{AB}|=\sqrt{(-7)^2+4^2+2^2}$$
This application is essentially the Pythagorean theorem extended to three perpendicular directions.

Simplify the terms under the radical carefully to find the final scalar value:
$$|\vec{AB}|=\sqrt{49+16+4}=\sqrt{69}$$
The exact length is $\sqrt{69}$, not 69, because the square root operation is a fundamental part of the magnitude formula.

## Routes, midpoints and extending a line

Vectors can be linked like journeys. If you go from $A$ to $B$ and then from $B$ to $C$, the resulting vector $\vec{AC}$ is the sum of the individual paths:
$$
\vec{AB}+\vec{BC}=\vec{AC}
$$
This relationship can be rearranged to find an unknown side vector if the other two are known.

The midpoint of two position vectors is defined as their average. If $A$ has position vector $\mathbf{a}$ and $B$ has position vector $\mathbf{b}$, the midpoint position vector is:
$$
\frac{\mathbf{a}+\mathbf{b}}{2}
$$
To calculate this result, you average the corresponding $x$ and $y$ components separately.

If a line is extended so that $\vec{AB}=\vec{BD}$, you first find the vector $\vec{AB}=\mathbf{b}-\mathbf{a}$. Then add this to the position vector $\mathbf{b}$ to find the new point's position:
$$
\mathbf{d}=\mathbf{b}+\vec{AB}=2\mathbf{b}-\mathbf{a}
$$

## Parallel vectors and simple shape proofs

Consider the trapezium $OABC$, with vertices joined in order $O \to A \to B \to C \to O$:
```
   A ────→ B
  ╱        ╲
 O ────────→ C
```
Here the only vectors shown on the parallel sides are $\vec{AB}$ on the top and $\vec{OC}$ on the bottom, with $\vec{OC}=2\vec{AB}$. Two non-zero vectors are parallel if one is a scalar multiple of the other, so every component is multiplied by the same number.

In coordinate shape questions, calculate the vectors for opposite sides and check whether one is a scalar multiple of the other. Reversing a side changes the sign of the vector but not whether the sides are parallel. A parallelogram has both pairs of opposite sides parallel, while a trapezium has exactly one pair.

In this example, $\vec{AB}=3\mathbf{i}-2\mathbf{j}+\mathbf{k}$ and $\vec{OC}=6\mathbf{i}-4\mathbf{j}+2\mathbf{k}=2\vec{AB}$. So the sides $AB$ and $OC$ are parallel. If $\vec{OA}$ and $\vec{BC}$ are not scalar multiples of each other, then the other pair is not parallel, so $OABC$ is a trapezium rather than a parallelogram.

## Unknown components from a magnitude

Sometimes a magnitude is given and one component is unknown. To solve these, start with the magnitude formula and square both sides to remove the square root. For example, consider the vector magnitude equation $|2\mathbf{i}+m\mathbf{j}-3\mathbf{k}|=7$.

$$$\sqrt{2^2+m^2+(-3)^2}=7$$

Squaring both sides gives the equation $4+m^2+9=49$. Notice that the negative component still becomes positive after squaring, which is a crucial step to remember when dealing with unknown variables.

Simplifying leads to $m^2=36$, hence $m=\pm 6$. There are two answers because a magnitude gives length only; therefore, both positive and negative $\mathbf{j}$ components can produce the same overall magnitude.

## Check yourself

1. Three forces act on a particle: $\mathbf{F}_1=-2\mathbf{i}+5\mathbf{j}+3\mathbf{k}$, $\mathbf{F}_2=6\mathbf{i}-\mathbf{j}-4\mathbf{k}$ and $\mathbf{F}_3=\mathbf{i}+2\mathbf{j}+7\mathbf{k}$. What is the resultant force?

   - $$5\mathbf{i}+6\mathbf{j}+6\mathbf{k}$ ✔

   - $$3\mathbf{i}+6\mathbf{j}+6\mathbf{k}$

   - $$5\mathbf{i}+4\mathbf{j}+10\mathbf{k}$

   - $$9\mathbf{i}+6\mathbf{j}-8\mathbf{k}$

   _Explanation:_ Add each component separately: $-2+6+1=5$, $5-1+2=6$, and $3-4+7=6$, so the resultant is $5\mathbf{i}+6\mathbf{j}+6\mathbf{k}$. Option B is the common wrong choice because it treats the $\mathbf{i}$ component of $\mathbf{F}_3$ as negative instead of positive.

2. What is the magnitude of $\vec{AB}$ if $\vec{AB}=-7\mathbf{i}+4\mathbf{j}+2\mathbf{k}$?

   - $$\sqrt{69}$ ✔

   - $$69$

   - $$\sqrt{53}$

   - $$13$

   _Explanation:_ Magnitude uses the square root of the sum of squares: $\sqrt{(-7)^2+4^2+2^2}=\sqrt{69}$. Option B is the common wrong answer because 69 is the value inside the square root, not the magnitude itself.

3. In quadrilateral $OABC$, suppose $\vec{OC}=2\vec{AB}$ and $\vec{BC}$ is not a scalar multiple of $\vec{OA}$. Which shape must $OABC$ be?

   - Parallelogram

   - Trapezium ✔

   - Rectangle

   - Kite

   _Explanation:_ If $\vec{OC}=2\vec{AB}$, then $\vec{CO}=-2\vec{AB}$, so $AB$ is parallel to $CO$. Also, $\vec{BC}$ not being a scalar multiple of $\vec{OA}$ means $BC$ is not parallel to $OA$. Therefore, the quadrilateral has exactly one pair of opposite sides parallel, so it must be a trapezium.
