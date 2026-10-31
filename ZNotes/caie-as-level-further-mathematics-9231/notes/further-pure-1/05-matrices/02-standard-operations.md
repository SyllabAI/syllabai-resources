## Standard operations

### **Addition and Subtraction**

- To add/subtract matrices, you must add/subtract each corresponding element in each matrix.
- Matrices can only be added/subtracted if they have the same dimensions.
  - For example, two $2\times2$ matrices can be added/subtracted but a $2\times3$ and a $3\times2$ matrix cannot.
- Matrix addition/subtraction is commutative
  - $A \pm B = B \pm A$
###    <center>For a 2x2 matrix</center>
$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\pm
\begin{pmatrix}
e & f \\
g & h
\end{pmatrix}
=
\begin{pmatrix}
a \pm e & b \pm f \\
c \pm g & d \pm h
\end{pmatrix}
$$

### <center>For a 3x3 matrix</center>

$$
\begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}
\pm
\begin{pmatrix}
j & k & l \\
m & n & o \\
p & q & r
\end{pmatrix}
=
\begin{pmatrix}
a \pm j & b \pm k & c \pm l\\
d \pm m & e \pm n & f \pm o \\
g \pm p & h \pm q & i \pm r
\end{pmatrix}
$$

### **Multiplication**

- To multiply matrices, sum the product of each element's row in the first matrix with the corresponding element's column in the second matrix.
- The number of columns in the left matrix must match the number of rows in the right matrix
  - For example, $3\times1$ and $1\times3$ can be multiplied with eachother
- Matrix multiplication is **not** commutative
  - $AB ~ \cancel{=} ~ BA$
- Matrix multiplication is associative
  - $A(BC) = (AB)C$

### <center>For a 2x2 matrix</center>

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\pm
\begin{pmatrix}
e & f \\
g & h
\end{pmatrix}
=
\begin{pmatrix}
ae \pm bg & af \pm bh \\
ce \pm dg & cf \pm dh
\end{pmatrix}
$$

### <center>For a 3x3 matrix</center>
$$
\begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}
\times
\begin{pmatrix}
j & k & l \\
m & n & o \\
p & q & r
\end{pmatrix}
=
\begin{pmatrix}
aj + bm + cp & ak + bn + cq & al + bo + cr \\
dj + em + fp & dk + en + fq & dl + eo + fr \\
gj + hm + ip & gk + hn + iq & gl + ho + ir
\end{pmatrix}
$$

### **Matrix raised to a natural number**

- In general, for a square matrix, $A^n = \underbrace{A \times A \times \cdots \times A}_{\text{n times}}$ [Where $n$ is a natural number]

$$
\begin{pmatrix}
a & b \
c & d
\end{pmatrix}^n = \underbrace{\begin{pmatrix}
a & b \\
c & d
\end{pmatrix} \times \begin{pmatrix}
a & b \\
c & d
\end{pmatrix} \times \cdots \times \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}}_{\text{n times}}

$$

### **Scalar multiplication**

- A scalar multiple is a constant that is multiplied by each element in the matrix

$$
\mu
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
=\begin{pmatrix}
a\mu & b\mu \\
c\mu & d\mu
\end{pmatrix}
$$