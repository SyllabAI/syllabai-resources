## Improper Integration

- Improper integration is a type of definite integration where the function being integrated is undefined at the limits given.

Consider the graph of the function $f(x) = \frac{1}{x}$

![Screenshot 2024-09-08 at 4.44.58 PM.png](../../../assets/1fd610f79824-66dd802f8a81ac4b1882eed01a6d819ed60f58368b986752.44)

Here:

- As $x$ approaches 0, $f(x)$ approaches $\infty$
  - This is written as $x \rightarrow 0$, $f(x) \rightarrow \infty$
- As $x$ approaches $\infty$, $f(x)$ approaches 0
  - This is written as $x \rightarrow \infty$, $f(x) \rightarrow 0$
- This is true for the negative $x$ and $y$ axis as well.

---

**<center>Example</center>**
The function $f$ is defined by
$$
\frac{1}{(4x + 2)^2}, \quad x > -\frac{1}{2}
$$
Find $\int_{1}^{\infty} f(x) \~dx$.
**<center>Answer</center>**
We begin by integrating
$$
\int_{1}^{\infty} (4x + 2)^{-2} = \left( \frac{(4x + 2)^{-2 + 1}}{4 \times (-2 + 1)} \right)_{1}^{\infty}
$$
Substitute a dummy variable, $t$, for the upper limit and evaluate the definite integral
$$
\left(\frac{-1}{16t + 8} \right) - \left( \frac{-1}{16(1) + 8} \right)
$$
As $t \rightarrow \infty$, $\frac{-1}{16t + 8} \rightarrow 0$.
$$
0 + \frac{1}{24}
$$
So the answer to the improper integral is $\frac{1}{24}$.

$$
\phantom{invis}
$$

**<center>Example 2</center>**
Evaluate whether the integral $\int_{0}^{2} \frac{5}{x^2} \~dx$ is defined or undefined.
**<center>Answer</center>**
We begin by integrating
$$
\int_{0}^{2} 5x^{-2} \~dx = \left( \frac{5x^{-2 + 1}}{-2 + 1} \right)_{0}^{2}
$$
Substitute a dummy variable, $t$, for the lower limit and evaluate the definite integral
$$
\left(\frac{-5}{2} \right) - \left( - \frac{5}{t} \right)
$$
As $t \rightarrow 0$, $-\frac{5}{t} \rightarrow \infty$.
$$
\frac{-5}{2} + \infty
$$
As there is no finite value given to this improper integral, it is undefined.