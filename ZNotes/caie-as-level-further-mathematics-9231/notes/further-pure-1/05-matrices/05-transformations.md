## Transformations

- The syllabus only requires you to know transformations for $2\times2$ matrices
- The order of the transformations is read from the right-most to the left-most matrix being multiplied
  - Example: For a matrix $A$ in $CBA$, $B$ is the first transformation and $C$ is the second transformation.

| Transformation | Matrix |
|----|----|
| Stretch by a scale factor of factor $\mathbf{k}$ in the x-direction | $\begin{pmatrix} k & 0 \\\\ 0 & 1 \end{pmatrix}$ |
| Stretch by a scale factor of factor $\mathbf{k}$ in the y-direction | $ \begin{pmatrix} 1 & 0 \\\\ 0 & k \end{pmatrix} $ |
| Enlargement with the center of enlargement the origin by a scale factor of factor $\mathbf{k}$ | $ \begin{pmatrix} k & 0 \\\\ 0 & k \end{pmatrix} $ |
| Reflection in the x-axis | $ \begin{pmatrix} 1 & 0 \\\\ 0 & - 1 \end{pmatrix} $ |
| Reflection in the y-axis | $ \begin{pmatrix} -1 & 0 \\\\ 0 & 1 \end{pmatrix} $ |
| Reflection in the line $𝒚 = 𝒙$ | $ \begin{pmatrix} 0 & 1 \\\\ 1 & 0 \end{pmatrix} $ |
| Rotation about the origin by $\mathbf{\theta}$ in the anticlockwise direction | $ \begin{pmatrix} \cos\theta & - \sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} $ |
|Shear in $x$ direction | $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ |
|Shear in $y$ direction | $\begin{pmatrix} 1 & 0 \\ k & 1 \end{pmatrix}$ |