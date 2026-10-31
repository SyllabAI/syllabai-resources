## Proof of Derivatives

- If $y = f(x)$, $\frac{d^ny}{dx^n} = f^{n}(x)$ is given, assume $\frac{d^ky}{dx^k} = f^{k}(x)$ is true for $P_k$. Differentiate $\frac{d^ky}{dx^k} = f^{k}(x)$ to show $P_k$ implies $P_{k + 1}$.



---



**<center>Example:</center>**

Find the ${n}$th derivative of ${x}{e}^{{x}}$

**<center>Solution:</center>**

**Step 1:**

$$
\frac{{d}}{{{dx}}}\left( {x}{e}^{{x}} \right){= x}{e}^{{x}}{+}{e}^{{x}}
$$

$$
\frac{{d}^{{2}}}{{d}{x}^{{2}}}\left( {x}{e}^{{x}} \right){= x}{e}^{{x}}{+}{e}^{{x}}{+}{e}^{{x}}
$$

$$
\frac{{d}^{{3}}}{{d}{x}^{{3}}}{(x}{e}^{{x}}{) = x}{e}^{{x}}{+}{e}^{{x}}{+}{e}^{{x}}{+}{e}^{{x}}
$$

**Step 2:**

We can see that the pattern that for the ${n}$th derivative,
there are $n$ number of $e^x$

**Step 3:**

$$
\frac{{d}^{{n}}}{{d}{x}^{{n}}}\left( {x}{e}^{{x}} \right){= x}{e}^{{x}}{+ n}{e}^{{x}}
$$

**Step 4:**

Let ${n = k}$

$$
\frac{{d}^{{k}}}{{d}{x}^{{k}}}\left( {x}{e}^{{x}} \right){= x}{e}^{{x}}{+ k}{e}^{{x}}
$$

To find ${n = k + 1}$,differentiate expression:

$$
\frac{{d}^{{k + 1}}}{{d}{x}^{{k + 1}}}\left( {x}{e}^{{x}} \right){= x}{e}^{{x}}{+}{e}^{{x}}{+ k}{e}^{{x}}
$$

$$
{= x}{e}^{{x}}{+}\left( {k + 1} \right){e}^{{x}}
$$

Prove that formula gives the same result as ${n = k + 1}$

$$
\frac{{d}^{{k + 1}}}{{d}{x}^{{k + 1}}}{= x}{e}^{{x}}{+}\left( {k + 1} \right){e}^{{x}}
$$

**Conclusion:**

By the Principle of Mathematical Induction ${x}{e}^{{x}}{+ n}{e}^{{x}}$ is the ${n}$th derivative of ${x}{e}^{{x}}$ for all ${n \geq 1}$.
