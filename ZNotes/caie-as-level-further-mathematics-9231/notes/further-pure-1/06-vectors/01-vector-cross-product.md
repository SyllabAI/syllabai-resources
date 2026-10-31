# Vectors

## Vector cross product

The vector cross product of two vectors, $a$ and $b$, gives us an unit vector that is **perpendicular** to both of them.

 ![](../../../assets/53f9737adad5-66a37f1557f11a489d6e2264541689be3e6fd5cf21c25208.22)

It is defined as

$$

a \times b = |a|~|b|~sin(\theta)~ \hat{n}
$$

<center>Where</center>

$$

\theta = \text{acute angle between vectors} ~ a ~ \text{and} ~ b
$$

$$

\hat{n} = \text{unit vector perpendicular to vectors} ~ a ~ \text{and} ~ b
$$

When given a perpendicular vector

$$
n = \begin{pmatrix}
   n_1 \\
n_2 \\
n_3
\end{pmatrix}
$$

We can find the unit perpendicular vector, $\hat{n}$ , as such

$$
\hat{n} = \begin{pmatrix}
   \frac{n_1}{\text{|}n\text{|}} \\
   \frac{n_2}{\text{|}n\text{|}} \\
\frac{n_3}{\text{|}n\text{|}}
\end{pmatrix}
~~\text{where}~~
\text{|}n\text{|} = \sqrt{(n_1)^2 + (n_2)^2 + (n_3)^2}
$$

### Using the cross product

The cross product, or perpendicular vector to $a$ and $b$, can be found like this:

$$
a \times b = \begin{pmatrix} 
x_1 \\
 y_1 \\
z_1
 \end{pmatrix} 
\times 
\begin{pmatrix} 
x_2 \\
 y_2 \\
 z_2 
\end{pmatrix}
=
\begin{pmatrix} 
y_1z_2 - z_1y_2 \\
 z_1x_2 - x_1z_2 \\
 x_1y_2 - x_2y_1
 \end{pmatrix}
$$

The cross product can also be expressed as the determinant of a matrix:

$$

a \times b = \begin{vmatrix} 
i & j & k \\
 x_1 & y_1 & z_1 \\
 x_2 & y_2 & z_2
 \end{vmatrix}
=
(y_1z_2 - z_1y_2)i - (x_1z_2 - z_1x_2)j + (x_1y_2 - x_2y_1)k
$$

---

$$
\text{Example}
$$

Find the vector perpendicular to the lines
 
$$
a = \begin{pmatrix}  
1 \\
3 \\
4
 \end{pmatrix}
\quad \text{and} \quad
b = \begin{pmatrix}  
2 \\
7 \\
-5
 \end{pmatrix}
$$

$$
\text{Answer}
$$

Using the determinant, we get the vector perpendicular to both lines as

$$
a \times b = \begin{vmatrix} 
i & j & k \\
 1 & 3 & 4 \\
 2 & 7 & -5
 \end{vmatrix}
= -41i + 13j + 1k
$$
