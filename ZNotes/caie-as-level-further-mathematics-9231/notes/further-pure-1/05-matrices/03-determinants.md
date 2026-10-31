## Determinants
- The value of the determinant, of a **square matrix**, is the scale factor for the area of a shape.
  - The value can be positive or negative, but a negative determinant only reflects the shape.
- The determinant of a matrix is represented by $det(A)$ or |$A$|.

### **Properties of a determinant**

- $det(I) = 1 ~\text{[where} ~I~ \text{is the identity matrix]}$


- $det(AB) = det(A) \times det(B)$



- $det(kA) = k^ndet(A) ~\text{[where} ~k~ \text{is a constant, and} ~n~ \text{represents a} ~n \times n~ \text{matrix]}$



- $det(A^{-1}) = \frac{1}{det(A)}$



- $\text{If} ~det(A) = 0~ \text{then the square matrix} ~A~ \text{is called a singular matrix}$


- $\text{If} ~det(A) ~\cancel{=}~ 0~ \text{then the square matrix} ~A~ \text{is called a non-singular matrix}$


### **Finding determinants**
**<center>2x2 matrix</center>**

Let $A$ be a $2 \times 2$ matrix such that

$$
A = \begin{pmatrix}
   a & b \\
   c & d
\end{pmatrix}
$$

So we can find $det(A)$ by

$$
det(A) = \begin{vmatrix}
   a & b \\
   c & d
\end{vmatrix}
= ad - bc
$$

**<center>3x3 matrix</center>**

Let $A$ be a $3\times3$ matrix such that

$$
A = \begin{pmatrix}
  a & b & c \\ 
d & e & f \\ 
g & h & i
\end{pmatrix}
$$

So we can find $det(A)$ by

$$
\det\left( A \right) =~ a\left| \begin{matrix}
e & f \\ h & i \end{matrix} \right| ~-~ b\left| \begin{matrix}
d & f \\ g & i \end{matrix} \right| ~+~ c\left| \begin{matrix}
d & e \\ g & h \end{matrix} \right|
$$

This can be simplified to
$$
det(A) = a(ei - fh) ~-~ b(di - fg) ~+~ c(dh - eg)
$$

- This is called the cofactor expansion method
  - Each $2\times2$ matrix is called a minor, and the determinant of a minor is called its cofactor.

---

**<center>Example</center>**

Find the determinant of
$$
\begin{pmatrix}
  {1} & {2} & {3} \\ {4} & {5} & {6} \\ {7} & {8} & {9} 
\end{pmatrix}
$$
And identify wether it is a singular or non-singular matrix.

**<center>Answer</center>**

$$
det(A) = 1\left| \begin{matrix}
{5} & {6} \\ {8} & {9} \end{matrix} \right|{~-~ 2}\left| \begin{matrix}
{4} & {6} \\ {7} & {9} \end{matrix} \right|{~+~ 3}\left| \begin{matrix}
{4} & {5} \\ {7} & {8} \end{matrix} \right|
$$

Use cofactor expansion to get
$$ 
det(A) =~ 1\left| \begin{matrix}
{5} & {6} \\ {8} & {9} \end{matrix} \right|{~-~ 2}\left| \begin{matrix}
{4} & {6} \\ {7} & {9} \end{matrix} \right|{~+~ 3}\left| \begin{matrix}
{4} & {5} \\ {7} & {8} \end{matrix} \right|
$$

Compute all the cofactors and simplify the equation to get
$$
det(A) = 1(45 - 48) ~-~ 2(36 - 42) ~+~ 3(32 - 35) = 0
$$
As the determinant of this matrix is equal to 0, it is a singular matrix.