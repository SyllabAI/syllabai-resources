## Proof of Summation

- If $\sum_{r = 1}^{n} f(r) = g(n)$ is given, assume $\sum_{r = 1}^{k} f(r) = g(k)$ is true for $P_k$ and add $f(k + 1)$ to $g(k)$ to show that $P_k$ implies $P_{k + 1}$.



---


**<span class="underline">Question 2:</span>**

Prove by induction that, for all $\mathbf{N \geq 1}$,

$$
\sum_{\mathbf{n = 1}}^{\mathbf{N}}\frac{\mathbf{n + 2}}{\mathbf{n}\left( \mathbf{n + 1} \right)\mathbf{2}^{\mathbf{n}}}\mathbf{= 1 -}\frac{\mathbf{1}}{\left( \mathbf{N + 1} \right)\mathbf{2}^{\mathbf{N}}}
$$

**<center>Solution:</center>**

**Step 1:**

Let $\mathbf{N = 1}$

$$
\frac{\mathbf{1 + 2}}{\mathbf{1}\left( \mathbf{1 + 1} \right)\mathbf{2}^{\mathbf{1}}}\mathbf{=}\frac{\mathbf{3}}{\mathbf{4}}
$$

Using the given formula:

$$
\mathbf{1 -}\frac{\mathbf{1}}{\left( \mathbf{1 + 1} \right)\mathbf{2}^{\mathbf{1}}}\mathbf{= 1 -}\frac{\mathbf{1}}{\mathbf{4}}\mathbf{=}\frac{\mathbf{3}}{\mathbf{4}}
$$

Therefore, true for $\mathbf{N = 1}$

**Step 2:**

Assume formula true for $\mathbf{N = k}$

When $\mathbf{N = k}$

$$
\mathbf{1 -}\frac{\mathbf{1}}{\left( \mathbf{k + 1} \right)\mathbf{2}^{\mathbf{k}}}
$$

When $\mathbf{N = k + 1}$

$$
\mathbf{1 -}\frac{\mathbf{1}}{\left( \mathbf{k + 1 + 1} \right)\mathbf{2}^{\mathbf{k + 1}}}\mathbf{= 1 -}\frac{\mathbf{1}}{\left( \mathbf{k + 2} \right)\mathbf{2}^{\mathbf{k + 1}}}
$$

If the formula is true then

$$
\sum_{\mathbf{n = 1}}^{\mathbf{k + 1}}\frac{\mathbf{n + 2}}{\mathbf{n}\left( \mathbf{n + 1} \right)\mathbf{2}^{\mathbf{n}}}\mathbf{=}\sum_{\mathbf{n = 1}}^{\mathbf{k}}\frac{\mathbf{n + 2}}{\mathbf{n}\left( \mathbf{n + 1} \right)\mathbf{2}^{\mathbf{n}}}\mathbf{+}\left( \mathbf{k + 1} \right)^{\mathbf{\text{th}}}\mathbf{\text{\ term}}
$$

$$
\mathbf{= 1 -}\frac{\mathbf{1}}{\left( \mathbf{k + 1} \right)\mathbf{2}^{\mathbf{k}}}\mathbf{+}\frac{\mathbf{k + 3}}{\left( \mathbf{k + 1} \right)\left( \mathbf{k + 2} \right)\mathbf{2}^{\mathbf{k + 1}}}
$$

$$
\mathbf{= 1 -}\frac{\mathbf{2}\left( \mathbf{k + 2} \right)\mathbf{- k - 3}}{\left( \mathbf{k + 1} \right)\left( \mathbf{k + 2} \right)\mathbf{2}^{\mathbf{k + 1}}}
$$

$$
\mathbf{= 1 -}\frac{\mathbf{2}\mathbf{k + 4 - k - 3}}{\left( \mathbf{k + 1} \right)\left( \mathbf{k + 2} \right)\mathbf{2}^{\mathbf{k + 1}}}
$$

$$
\mathbf{= 1 -}\frac{\mathbf{k + 1}}{\left( \mathbf{k + 1} \right)\left( \mathbf{k + 2} \right)\mathbf{2}^{\mathbf{k + 1}}}
$$

$$
\mathbf{= 1 -}\frac{\mathbf{1}}{\left( \mathbf{k + 2} \right)\mathbf{2}^{\mathbf{k + 1}}}
$$

**Conclusion:**

Since $P_1$ is true, and $P_k$ implies $P_{k + 1}$, the summation is true for all $\mathbf{N \geq 1}$.
