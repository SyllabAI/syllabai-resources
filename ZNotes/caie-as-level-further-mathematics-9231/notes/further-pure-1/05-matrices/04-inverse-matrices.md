## Inverse matrices
- Given a square matrix, $A$, it's inverse is written as $A^{-1}$.
The inverse of a square matrix $A$ is a matrix that, when multiplied by $A$, results in the identity matrix. This identity is written below

$$
AA^{-1} = A^{-1}A = I
$$

- A matrix without an inverse is known as a singular matrix
  - This implies that a matrix has no inverse if its determinant is equal to 0
- A matrix with an inverse is known as a non-singular matrix
  - This implies that a matrix has an inverse if its determinant is not equal to 0

It should also be known that
$$
(AB)^{-1} = B^{-1}A^{-1}
$$
### **Finding the inverse matrix**

**<center>2x2 matrix</center>**

Let $A$ be a $2\times2$ matrix such that

$$
A = \begin{pmatrix}
   a & b \\
   c & d
\end{pmatrix}
$$

So we can find $A^{-1}$ by
$$
A^{-1} = \frac{1}{ad - bc}\begin{pmatrix}
   d & -b \\
   -c & a
\end{pmatrix}
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

First, we find all the minor $2\times2$ matrices


$$
A = \begin{pmatrix} 
\begin{vmatrix} e & f \\ h & i \end{vmatrix} & -\begin{vmatrix} d & f \\ g & i \end{vmatrix} & \begin{vmatrix} d & e \\ g & h \end{vmatrix} \\
-\begin{vmatrix} b & c \\ h & i \end{vmatrix} & \begin{vmatrix} a & c \\ g & i \end{vmatrix} & -\begin{vmatrix} a & b \\ g & h \end{vmatrix} \\
\begin{vmatrix} b & c \\ e & f \end{vmatrix} & -\begin{vmatrix} a & c \\ d & f \end{vmatrix} & \begin{vmatrix} a & b \\ d & e \end{vmatrix}
\end{pmatrix}
$$

For simplicity, we will denote each minor as $M_{ij}$ where $i$ represents the row and $j$ represents the column of the minor.

$$
M_{11} = \begin{vmatrix} e & f \\ h & i \end{vmatrix}~ M_{12} = \begin{vmatrix} d & f \\ g & i \end{vmatrix} ~ M_{13} = \begin{vmatrix} d & e \\ g & h \end{vmatrix} \\ 
M_{21} = \begin{vmatrix} b & c \\ h & i \end{vmatrix} ~ M_{22} = \begin{vmatrix} a & c \\ g & i \end{vmatrix} ~ M_{23} = \begin{vmatrix} a & b \\ g & h \end{vmatrix} \\
M_{31} = \begin{vmatrix} b & c \\ e & f \end{vmatrix} ~ M_{32} = \begin{vmatrix} a & c \\ d & f \end{vmatrix} ~ M_{33} = \begin{vmatrix} a & b \\ d & e \end{vmatrix}
$$

Substituting in $M_{ij}$, we get

$$
A = \begin{pmatrix} 
M_{11} & -M_{12} & M_{13} \\
-M_{21} & M_{22} & -M_{23} \\
M_{31} & -M_{32} & M_{33}
\end{pmatrix}
$$

Next, we must transpose the matrix, which means the elements in each row and column are interchanged.

$$
\begin{pmatrix} 
M_{11} & -M_{21} & M_{31} \\
-M_{12} & M_{22} & -M_{32} \\
M_{13} & -M_{23} & M_{33}
\end{pmatrix}
$$

We can now find the inverse by multiplying it with the determinant of the matrix

$$
A^{-1} = \frac{1}{det(A)}\begin{pmatrix} 
M_{11} & -M_{21} & M_{31} \\
-M_{12} & M_{22} & -M_{32} \\
M_{13} & -M_{23} & M_{33}
\end{pmatrix}
$$
