## Distance between two lines
### **Distance between parallel lines**
To find the shortest distance between two parallel lines
- Choose any point on one of the lines and then find the shortest distance from the point to the second line
   - We may choose any point from one of the lines as the distance between two parallel lines is always constant.

You can use the distance from a **point to a line** formula
$$
d = \text{|}(p - a)\text{|} \times \hat{b}
$$
Or the distance from a **point to a plane** formula
$$
d = \frac{\text{|} \hat{n} \cdot (p - a)\text{|}}{\text{|} \hat{n} \text{|}}
$$
### **Distance between skewed lines**
Skewed lines are lines which are not parallel and never intersect.
![Screenshot 2024-11-03 at 12.35.19 PM.png](../../../assets/73a37ecf78cf-672719c039de4629d926af13260a5724788bb0f9881c0c87.35)

- Consider two 3D lines, $r_1 = a_1 + \lambda b_1$ and $r_2 = a_2 + \mu b_2$. 
   - Using the two lines, we can find vector $\overrightarrow{PQ}$ as $a_1 - a_2$

The shortest distance, $d$, is represented by the magnitude of the dot product of $a_1 - a_2$ and the perpendicular vector to both lines.
$$
d = \text{|}(a_1 - a_2) \cdot \hat{n}\text{|} = \text{|}\frac{(a_1 - a_2) \cdot b_1 \times b_2}{\text{|}b_1 \times b_2 \text{|}}\text{|}
$$

Where:
- $a_1$ and $a_2$ are the position vectors of the known points on the lines
- $b_1$ and $b_2$ are the direction vectors of the lines
---

**<center>Example 1</center>**
The plane $\Pi$ has the equation $-2x - 5y + 5z = 25$, and contains the line $l_1: r = -5j + \lambda(5i + 2k)$ and is parallel to $l_2: 4i + 2j - 2k + \mu(j + k)$.
Find the distance between $\Pi$ and $l_2$.
**<center>Answer</center>**
First we find the vector that connects the plane and the point
$$
\begin{pmatrix}
   0 \\
   -5 \\
0 
\end{pmatrix}
 -
\begin{pmatrix}
   4 \\
   2 \\
-2
\end{pmatrix}
=
\begin{pmatrix}
   -4 \\
   -7 \\
2
\end{pmatrix}
$$
Now we use the formula to find the shortest distance from a point to a plane
$$
\frac{1}{\sqrt{(-2)^2 + (-5)^2 + (5)^2}} \text{|} 
\begin{pmatrix}
   -4 \\
   -7 \\
2
\end{pmatrix}
\cdot
\begin{pmatrix}
   -2 \\
   -5 \\
5
\end{pmatrix}
\text{|}
= \frac{53}{\sqrt{54}}
$$
**<center>Example 2</center>**
Find the shortest distance between $l_1: r = 3i + 3k + \lambda(i + 4j + 4k)$ and $l_2: r = 3i - 5j - 6k + \mu(5j + 6k)$.
**<center>Answer</center>**
We first find the vector that connects both skew lines.
$$
(3i - 5j - 6k) - (3i + 3k) = -5j - 9k
$$
Next we find the common perpendicular of the direction vectors of both lines

$$
\begin{vmatrix}
   i & j & k \\
   1 & 4 & 4 \\
0 & 5 & 6
\end{vmatrix}
= 4i - 6j + 5k
$$
Now we can use the formula for the distance between skew lines
$$
\text{|}\frac{\begin{pmatrix}
   0 \\
   -5 \\
-9
\end{pmatrix} 
\cdot 
\begin{pmatrix}
   4 \\
   -6 \\
5
\end{pmatrix}}{\sqrt{(4)^2 + (-6)^2 + (5)^2}}\text{|}
= \frac{15}{\sqrt{77}}
$$