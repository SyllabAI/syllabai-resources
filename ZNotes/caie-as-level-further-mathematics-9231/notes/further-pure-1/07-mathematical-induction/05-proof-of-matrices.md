## Proof of Matrices

- If $A^n$ and $A$ are given, assume $A^k$ is true for $P_k$ and determine $A^kA$ to show that $P_k$ implies $P_{k + 1}$.



---

**<center>Example:</center>**

The matrix $B = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$ is raised to the power $n$ to give $B^n \begin{pmatrix} 2^n & 2^n - 1 \\ 0 & 1 \end{pmatrix}$. Prove this is true by mathematical induction.

**<center>Solution</center>**

**Step 1:**

Let $n = 1$
$$
B^1 = \begin{pmatrix} 2^1 & 2^1 - 1 \\ 0 & 1 \end{pmatrix} = B = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} = B
$$
Hence, true for when $n = 1$.

**Step 2:**

Assume the statement to be true for some positive integer $n = k$

$$
B^k = \begin{pmatrix} 2^k & 2^k - 1 \\ 0 & 1 \end{pmatrix}
$$


When $n = k + 1$
$$
B^kB = \begin{pmatrix} 2^k & 2^k - 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}
$$

$$
\begin{pmatrix} 2 \times 2^k & 2^k + 2^k - 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2^{k + 1} & 2^{k + 1} - 1 \\ 0 & 1 \end{pmatrix} = B^{k + 1}
$$

Therefore $P_k$ implies $P_{k + 1}$.

**Conclusion:**

Since the statement is true for $P_1$ and $P_k$ implies $P_{k + 1}$, by mathematical induction $P_n$ is true for all $n \geq 1$.
