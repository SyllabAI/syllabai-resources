## Particle Collisions

If a particle has initial position $\vec{r}_0$ and velocity vector $\vec{v}$, then position at time $t$ is:

$$
\vec{r}(t) = \vec{r}_0 + \vec{v}t
$$

Used to:

* Find when particles meet (collide)

* Determine position at a given time

* Check if paths intersect

**Example:** Particle Collision

Two particles $A$ and $B$ move in a plane.

$A$: initial position $\begin{pmatrix}1 \ 2\end{pmatrix}$, velocity $\begin{pmatrix}3 \ 1\end{pmatrix}$

$B$: initial position $\begin{pmatrix}4 \ 0\end{pmatrix}$, velocity $\begin{pmatrix}1 \ 2\end{pmatrix}$

Find if/when they collide.

* Step 1: Write position vectors as functions of $t$:

$$
\vec{r}_A(t) = \begin{pmatrix}1 + 3t \ 2 + t \end{pmatrix}, \quad
\vec{r}_B(t) = \begin{pmatrix}4 + t \ 2t \end{pmatrix}
$$

* Step 2: Set $\vec{r}_A(t) = \vec{r}_B(t)$ and solve for $t$ by comparing components:

$$
1 + 3t = 4 + t \implies 2t = 3 \implies t = \frac{3}{2}
$$

$$
2 + t = 2t \implies t = 2
$$

**Conclusion:** Particles do not collide since the two $t$ values differ. They never occupy the same position at the same time.