## Proof of Recurrence relations

- If $u_{n + 1} = f(u_n)$ and $u_n = g(n)$ are given, then assume $u_k = g(k)$, for some positive integer k, is true for $P_k$ and input this into $f(u_k)$ to obtain $u_{k + 1}$. Then you can show that $P_k$ implies $P_{k + 1}$. 




---

**<center>Example</center>**

If $u_{n + 1} = 3u_n + 2$, where $u_1 = 1$, prove by mathematical induction that $u_n = 2 \times 3^{n - 1} - 1$ for all positive integers greater than 0.

**<center>Solution</center>**

**Step 1:**

When $n = 1$
$$
u_1 = 2 \times 3^0 - 1 = 1
$$
So $P_1$ is true.

**Step 2:**

Assume true for $n = k$, where k is some positive integer

$$
u_k = 2 \times 3^{k - 1}
$$

Then

$$
u_{k + 1} = 3(2 \times 3^{k - 1} - 1) + 2
$$

This leads to
$$
u_{k + 1} = 2 \times 3^k - 1
$$

**Conclusion:**
As $P_1$ is true, and $P_k$ implies $P_{k + 1}$, by mathematical induction $P_n$ is true for all $n \geq 1$.