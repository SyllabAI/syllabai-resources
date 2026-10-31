# Matrices

## Eigenvalues & Eigenvectors

* Eigenvector: vectors who do not change direction after a matrix is being applied to them.
* Eigenvalues: the scale factors of the eigenvectors after a matrix is applied to them
* Eigenvectors & eigenvalues has the relation:

  $Ax = \lambda x$
* To determine a characteristic equation, use:

  $det(A- \lambda I) = 0$

**Example:**

Find the eigenvalues, and eigenvectors for the following matrix \n $\begin{pmatrix} 10 & -6 \ 12 & -7 \end{pmatrix}$

Solution:

Using the characteristic equation

$det(A- \lambda I) = 0$

 \n $Det(\begin{pmatrix} 10 & -6 \ 12 & -7 \end{pmatrix} - \lambda \begin{pmatrix} 1 & 0  \ 0 & 1 \end{pmatrix} = \begin{vmatrix} 10-\lambda & -6 \ 12 & -7- \lambda \end{vmatrix} $

Form an equation and solve to find eigenvalues

$(10 - \lambda)(-7- \lambda) - (-6)(12) = 0$

$\lambda^2 -3\lambda + 2 = 0$

$\lambda = 2 or 1$

Next, find the eigenvectors by multiplying by original matrix and solving equation by putting values

Using $Ax = \lambda x$

$\lambda = 2$     $\begin{pmatrix} 10 & -6 \ 12 & -7 \end{pmatrix} \begin{pmatrix} x\ y \end{pmatrix} = \begin{pmatrix} 2x \ 2y \end{pmatrix}$

$10x - 6y = 2x$

→ $8x = 6y$

→ $\frac{4}{3}x = y$

Eigenvector: $\begin{pmatrix} 3\ 4 \end{pmatrix}$

$\lambda = 1$    $\begin{pmatrix} 10 & -6 \ 12 & -7 \end{pmatrix} \begin{pmatrix} x\ y \end{pmatrix} = \begin{pmatrix} x \ y \end{pmatrix}$

$10x-6y = x$

→ $9x = 6y$

→ $3x = 2y$

→ $\frac{3}{2} x = y$

Eigenvector: $\begin{pmatrix} 2\ 3 \end{pmatrix}$

Hence, we have found

$\lambda = 2, \begin{pmatrix} 3\ 4 \end{pmatrix}$.   $\lambda = 1, \begin{pmatrix} 2\ 3 \end{pmatrix}$