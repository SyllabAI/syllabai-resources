## Proof of Divisibility

- if f(n) is given as being divisible by $b$, assume $f(k)$ is divisible by $b$ for $P_k$ and show that $f(k + 1) - f(k) = ab$, which leads to $P_k$ implying $P_{k+1}$



---


Question 2:

It is given that $\phi\left(n\right)=5^n\left(4n + 1\right)-1$, for ${n = 1,2,3 \cdots}$ Prove, by mathematical induction, that $\mathbf{\phi}\left( {n} \right)$ is divisible by 8 for every positive integer ${n}$

**<center>Solution:</center>**

**Step 1:**

Let ${n = 1}$

$$
{\therefore}{\phi}\left( {1} \right){= 5}\left( {4 + 1} \right){- 1 = 8}{\times}{3}
$$

Our formula is true for $\mathbf{n = 1}$

**Step 2:**

Assume formula is true for ${n = k}$ for an integer
${k}$

$$
\mathbf{\phi}\left( \mathbf{k} \right)\mathbf{=}\mathbf{5}^{\mathbf{k}}\left( \mathbf{4}\mathbf{k + 1} \right)\mathbf{- 1\  = 8}\mathbf{p}
$$

Where $\mathbf{p}$ is just a dummy value

Let ${n = k + 1}$

$$
\mathbf{\phi}\left( \mathbf{k + 1} \right)\mathbf{=}\mathbf{5}^{\mathbf{k + 1}}\left( \mathbf{4}\left( \mathbf{k + 1} \right)\mathbf{+ 1} \right)\mathbf{- 1}
$$

$$
\mathbf{\rightarrow}\mathbf{\phi}\left( \mathbf{k + 1} \right)\mathbf{=}\mathbf{5}^{\mathbf{k}}\left( \mathbf{5} \right)\left( \mathbf{4}\mathbf{k + 5} \right)\mathbf{- 1}
$$

$$
\mathbf{\rightarrow}\mathbf{\phi}\left( \mathbf{k + 1} \right)\mathbf{=}\mathbf{5}^{\mathbf{k}}\left( \mathbf{20}\mathbf{k + 25} \right)\mathbf{- 1}
$$

Calculate
$\mathbf{\phi}\left( \mathbf{k + 1} \right)\mathbf{-}\mathbf{\phi}\left( \mathbf{k} \right)$

$$
\mathbf{\phi}\left( \mathbf{k + 1} \right)\mathbf{-}\mathbf{\phi}\left( \mathbf{k} \right)\mathbf{=}\mathbf{5}^{\mathbf{k}}\left( \mathbf{20}\mathbf{k + 25} \right)\mathbf{- 1 -}\left( \mathbf{5}^{\mathbf{k}}\left( \mathbf{4}\mathbf{k + 1} \right)\mathbf{- 1} \right)
$$

$$
\mathbf{\phi}\left( \mathbf{k + 1} \right)\mathbf{- \phi}\left( \mathbf{k} \right)\mathbf{\  =}\mathbf{5}^{\mathbf{k}}\left( \mathbf{20}\mathbf{k + 25} \right)\mathbf{- 1 -}\mathbf{5}^{\mathbf{k}}\left( \mathbf{4}\mathbf{k + 1} \right)\mathbf{\  + 1\ }
$$

$$
\mathbf{\phi}\left( \mathbf{k + 1} \right)\mathbf{- \phi}\left( \mathbf{k} \right)\mathbf{=}\mathbf{5}^{\mathbf{k}}\left( \mathbf{20}\mathbf{k + 25 - 4}\mathbf{k - 1} \right)
$$

$$
\mathbf{\phi}\left( \mathbf{k + 1} \right)\mathbf{- \phi}\left( \mathbf{k} \right)\mathbf{=}\mathbf{5}^{\mathbf{k}}\left( \mathbf{16}\mathbf{k + 24} \right)
$$

$$
\mathbf{\phi}\left( \mathbf{k + 1} \right)\mathbf{- \phi}\left( \mathbf{k} \right)\mathbf{=}\mathbf{5}^{\mathbf{k}}\left( \mathbf{8} \right)\left( \mathbf{2}\mathbf{k + 3} \right)
$$

Add $\mathbf{\phi}\left( \mathbf{k} \right)$to both sides

$$
\mathbf{\phi}\left( \mathbf{k + 1} \right)\mathbf{=}\mathbf{5}^{\mathbf{k}}\left( \mathbf{8} \right)\left( \mathbf{2}\mathbf{k + 3} \right)\mathbf{+}\mathbf{\phi}\left( \mathbf{k} \right)
$$

From the equation, because
$\mathbf{\phi}\left( \mathbf{k} \right)$*divisible by 8, therefore*
$\mathbf{\phi}\left( \mathbf{k + 1} \right)$*is also divisible by 8.*

**Conclusion:**

Thus, since $\mathbf{\phi}\left( \mathbf{1} \right)$is true and
$\mathbf{\phi}\left( \mathbf{k} \right)\mathbf{\rightarrow}\mathbf{\phi}\left( \mathbf{k + 1} \right)$
is true by mathematical induction for $n \geq 0$
