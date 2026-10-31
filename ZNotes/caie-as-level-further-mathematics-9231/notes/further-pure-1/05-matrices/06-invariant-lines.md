## Invariant Lines
- An invariant is a line unchanged by a transformation.
  - All points on this line stay the same after a transformation.

To find an invariant line, that passes through the origin, multiply the matrix by $y = mx$ and equate it to $y = mx$. This is done as all the points must be the same, on an invariant line, regardless of a transformation.

$$
\begin{pmatrix}
   a & b \\
   c & d
\end{pmatrix}
\begin{pmatrix}
   y \\
   mx
\end{pmatrix}
=
\begin{pmatrix}
   y \\
   mx
\end{pmatrix}
$$

$$
ax + bmx = y ~\text{and}~ cx + dmx = mx
$$


We can get a quadratic in terms of $m$ using both equations


$$
bm^2 + (a - d)m - c = 0
$$

Solve for $m$ and substitute the value into $y = mx$ to get the invariant line.



---


**<span class="underline">Question:</span>**

The matrix ${A}$ is given by
$$
\begin{pmatrix}
{5} & {k} \\ {- 3} & {- 4} \end{pmatrix}
$$

a) Find the value of ${k}$ for which ${A}$ is singular
it is now given ${k = 6}$ so that ${A =}\begin{pmatrix}
{5} & {6} \\{- 3} & {- 4} \end{pmatrix}$

b) Find the equations of the invariant lines, through the origin, of the
transformation in the x-y plane represented by ${A}$

c) The triangle DEF in the x-y plane is transformed by ${A}$
onto triangle PQR.

i) Given that the area of triangle DEF is
${10, c}{m}^{{2}}$, find the area of triangle
PQR.

ii) Find the matrix which transforms triangle PQR onto triangle DEF.

**<center>Answer</center>**

When ${A}$is singular, means that its determinant is equal to
0\. Using the equation ${ad - bc}$, we find its det.

$${5}\left( {- 4} \right){- k}\left( {- 3} \right){= 0}$$

$${k =}\frac{{20}}{{3}}\quad\mathrm{(Ans\ for\ a)}$$

Use the equation to find invariant lines:
$$
\begin{pmatrix}
{5} & {6} \\ {- 3} & {- 4} \end{pmatrix}\begin{pmatrix}
{t} \\ {\text{mt}} \end{pmatrix}{=}\begin{pmatrix}
{T} \\ {\text{mT}} \end{pmatrix}
$$



 
$$
{\rightarrow}\begin{pmatrix}
{5}{t + 6}{\text{mt}} \\ {- 3}{t - 4}{\text{mt}} \end{pmatrix}{=}\begin{pmatrix}
{T} \\ {\text{mT}} \end{pmatrix}
$$

We now have two equations:

$$
{5}{t + 6}{mt = T\ }\quad{- 3}{t - 4}{mt =}{\text{mT}}
$$

Divide the 1<sup>st</sup> equation with the 2<sup>nd</sup> equation:

$$
\frac{{5 + 6}{m}}{{- 3 - 4}{m}}{=}\frac{{1}}{{m}}
$$

Solve for ${m}$:

$$
{6}{m}^{{2}}{+ 9}{m + 3 = 0}
$$

$$
{m}_1{= - 1} \quad {m}_2{=}\frac{{1}}{{2}}
$$

Therefore, the answers are:

$$
{y = - x}\quad\text{and}\quad{y =}\frac{{1}}{{2}}{x}\quad\mathrm{(Ans\ for\ b)}
$$

Since the determinant shows the factor increase of the area/volume, we will
find the determinant of ${A}$.

$$
{5}\left( {- 4} \right){- 6}\left( {- 3} \right){\  = \  - 2}
$$

Therefore, ignoring the sign, the area of the new triangle is:

$$
{2}{\times}{10 = 20}{c}{m}^{{2}}\quad\mathrm{(Ans\ for\ ci)}
$$

Finding the matrix that transforms the new triangle back to the old
triangle just means that we must find the inverse of the matrix:









$$
{A}^{{- 1}}{ =}\frac{{1}}{{- 2}}\begin{pmatrix}
{- 4} & {- 6} \\ {3} & {5} \end{pmatrix}
$$




$$
{A}^{{- 1}}{=}\begin{pmatrix}
{2} & {3}\\ {-}\frac{{3}}{{2}} & {-}\frac{{5}}{{2}} \end{pmatrix}\quad\mathrm{(Ans\ for\ c\ ii)}
$$