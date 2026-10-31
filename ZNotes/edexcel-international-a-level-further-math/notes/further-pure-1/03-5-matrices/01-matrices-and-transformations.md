# Matrices and transformations

## Matrices

* A matrix is a collection of numbers stores in rows and columns

$$

\begin{bmatrix}
a & b \\ \
c & d
\end{bmatrix}
$$

* above is a 2 x 2 matrix

  * in a $z$ x $w$ matrix, the $z$ is the number of rows and $w$ is the number of columns

* Square matrix - a matrix consisting of the same amount of columns and rows

* Zero matrix - where all elements in a matrix is 0

* Identity matrix - a square matrix in which all diagonal elements from the top left position are 1, with the remaining elements being 0

  * Identity matrices are denoted by $I_k$, with $k$ denoting the size of the matrix

  * $I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$

---

## Matrix addition

* To add matrices together, they first need to be the same size (same number of columns and rows). you then add the numbers in the same position in the matrix

  * Ie. you can only add a 2 x 2 matrix with another 2 x 2 matrix
  * $\begin{bmatrix} 4 & 10 \\ 3 & 9 \end{bmatrix} + \begin{bmatrix} 13 & 5 \\ 8 & 17 \end{bmatrix} = \begin{bmatrix} 17 & 15 \\ 11 & 26 \end{bmatrix}$

---

## Matrix multiplication

* You need to compare their sizes first in order to make sure they are compatible with each other. the columns in the first matrix needs to be the same as the number of rows in the 2nd matrix

  * the product matrix (the final result of the multiplication) will contain the rows of the first matrix and the columns of the 2nd matrix

    * we can multiply a 2 x 2 matrix and a 2 x 3 matrix together as the first matrix’s columns and the second matrix’s rows are the same. the product matrix will now have the rows of the first matrix and the columns of the 2nd matrix (a 2 x 3 matrix)

* It is very important to consider the order in which you multiply the matrices

  * lets make $A =$ a 2 x 2 matrix and $B =$ a 2 x 3 matrix. $AB \neq BA$ (this is for any matrix, even ones with identical sizes)
  * While $AB$ is valid, when comparing $BA$, we compare a 2 x 3 matrix with a 2 x 2 matrix, since $B$’s number of columns doesn’t match $A$’s number of rows, we cant calculate $BA$

* to find the product matrix between 2 compatible matrices (in this case $AB$), start with the first row in $A$ and the first column in $B$, then add their corresponding elements, then finally simplify the numbers from each element added. the final position of this number is determined by the position of the row and column used to calculate the value

### Example question

* Given that $A = \begin{bmatrix} -5 & 8 \\ 7 & 13 \end{bmatrix}$ and $B = \begin{bmatrix} 4 & 9 & 12 \\ -6 & 3 & -7 \end{bmatrix}$ . Find $AB$
* $AB = \begin{bmatrix} (-5 + 4) + (8 - 6) & (-5 + 9) + (8 + 3) & (-5 + 12) + (8 - 7) \\ (7 + 4) + (13 - 6) & (7 + 9) + (13 + 3) & (7 - 12) + (13 - 7) \end{bmatrix}$
* $AB = \begin{bmatrix} -1 + 2 & 4 + 11 & 7 + 1 \\ 11 + 7 & 16 + 16 & -5 + 6 \end{bmatrix}$
* $AB = \begin{bmatrix} 1 & 15 & 8 \\ 18 & 32 & 1 \end{bmatrix}$

---

## Determinant

* the determinant is the scalar value associated with a matrix. For a 2 x 2 matrix $N = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, the determinant for $N$ is $ad - bc$

  * if det $N = 0$, then the matrix is singular

  * if det $N \neq 0$, then the matrix is non-singular

### Example question

* Given that $A = \begin{bmatrix} 5a & -4 \\ -3 & -2b \end{bmatrix}$, find det $A$ in terms of $a$ and $b$

  * det $A = 5a(-2b) - -4(-3)$

  * det $A = -10ab - 12$

  * det $A = -2(5ab + 6)$

---

## Inverse matrices

* any non-singular matrix has a inverse matrix

  * the inverse of $N$ is $N^{-1}$, multiplying these matrices in any order gives the identity matrix $I$

* if $N = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, then $N^{-1} = \frac{1}{det N}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix} $.

### Example question

* Given that $A = \begin{bmatrix} 9 & -7 \\ -8 & 13 \end{bmatrix}$, find $A^{-1}$

  * det $A = -9(-13) - 7(8)$

  * det $A = 61$

  * $A^{-1} = \frac{1}{61}\begin{bmatrix} 13 & 7 \\ 8 & 9 \end{bmatrix}$