## Shortest distance from a point to a plane

![Screenshot 2024-11-03 at 12.11.50 AM.png](../../../assets/ed4816dba6fb-67266947853a987edb0ba70dc21a892d4177ffd878b9a2e4.11)

- Consider a point $P$ with coordinates $(x_1 , y_1, z_1)$ and a **general point** on the plane, $A$, with coordinates $(x_0, y_0, z_0)$.
  - Vector $\overrightarrow{AP}$ is equal to $p - a$ or $(x_1 - x_0, y_1 - y_0, z_1 - z_0)$, and is a vector from a general point $A$ on the plane to the point $P$
 
Clearly, the magnitude of $NP$ is equal to the magnitude of the projection of vector $p - a$ along $\hat{n}$
$$
\text{|}NP\text{|} = \frac{\text{|}\hat{n} \cdot (p - a)\text{|}}{\text{|}\hat{n}\text{|}}
$$
- Note that the bars in the numerator refer to the modulus, or absolute value, and not the magnitude.
  - The bars in the denominator refer to the magnitude of the vector.

### **Shortest distance using the cartesian equation of a plane**
Using the same equation above, if we let $\hat{n}$ have the coordinates $(a, b, c)$, and substitute in the vector $p - a$, we get
$$
\text{|}NP\text{|} = \frac{\text{|}a(x_1 - x_0) + b(y_1 - y_0) + c(y_1 - y_0)\text{|}}{\sqrt{a^2 + b^2 + c^2}}
$$
$$
\text{|}NP\text{|} = \frac{\text{|}(ax_1 + by_1 + cz_1) - (ax_0 + by_0 + cz_0)\text{|}}{\sqrt{a^2 + b^2 + c^2}}
$$
As $ax + by + cz = d$ will always hold true for **any point on the plane**, we can substitute in the value of $d$ as such
$$
\text{|}NP\text{|} = \frac{\text{|}ax_1 + by_1 + cz_1 - d\text{|}}{\sqrt{a^2 + b^2 + c^2}} 
$$

If required, we can find the shortest distance from the origin, $O(0, 0, 0)$, to the plane as such
$$
\text{|}NP\text{|} = \frac{\text{|}a(0) + b(0) + c(0) - d\text{|}}{\sqrt{a^2 + b^2 + c^2}} = \frac{d}{\sqrt{a^2 + b^2 + c^2}}
$$



---
**<center>Example</center>**
Find the shortest distance between the plane $\Pi: -5x + 5y + 2z = 8$, which contains a point $2i + 2j + 4k$, and the point outside the plane $D:2i + j + 3k$.
**<center>Answer</center>**
Using the cartesian formula for the shortest distance
$$
\frac{\text{|}-5(2) + 5(1) + 2(3) - 8\text{|}}{\sqrt{(-5)^2 + (5)^2 + (2)^2}} = \frac{7}{\sqrt{54}}
$$
We can also use the other formula, as we have a known point to the plane.
First we find the vector from the known point on the plane to the point $d$
$$
\begin{pmatrix}
   2 \\
   1 \\
3
\end{pmatrix}
-
\begin{pmatrix}
   2 \\
   2 \\
4
\end{pmatrix}
=
\begin{pmatrix}
   0 \\
   -1 \\
-1
\end{pmatrix}
$$
Next we use the distance formula
$$
\frac{\text{|} \begin{pmatrix}
   0 \\
   -1 \\
-1
\end{pmatrix}
\cdot
\begin{pmatrix}
   -5 \\
   5 \\
2
\end{pmatrix}
\text{|}}
{\sqrt{(-5)^2 + (5)^2 + (2)^2}}
= \frac{7}{\sqrt{54}}
$$
