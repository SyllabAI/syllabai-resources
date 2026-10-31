## Cumulative Distribution Function (CDF)

* Gives the probability of the random value being less than the value $x$
  - $P(X < x)$ or $P(X \leq x)$


- Represented by $F\left( x \right)$, the integral of $f(x)$

$$
F\left( x \right) = \int_{- \infty}^{t}{f\left( x \right)}\text{ dx}
$$

![Screenshot 2024-11-27 at 4.23.11 PM.png](../../../assets/b2a7711a1a59-667c162c3112117423e6e03202bac407602d39b741065ce8.23)

Looking at the graph:

- It is impossible to have a value of $X$ smaller than $- \infty$ or larger than $\infty$ so:

$$
F\left( - \infty \right) = 0\text{\quad\quad}F\left( \infty \right) = 1
$$

- As $x$ increases, $F\left( x \right)$ either increases or remains constant but never decreases.

- $F\left( x \right)$ is a continuous function even if $f\left( x \right)$ is discontinuous.

- Useful Relations:

  - $P\left( c < X < d \right) = F\left( d \right) - F\left( c \right)$
  - $P\left( X > a \right) = 1 - F\left( a \right)$

- Median: the value of $x$ for which $F\left( x \right) = 0.5$

  - $n$th percentile $\rightarrow F(x) = \frac{n}{100}$

---

**<span class="underline">Example:</span>**

Given that:

$$
f(x) = \begin{cases} k & 0 < x < 1 \\ 4k & 1 < x < 3 \\ 0 & \text{otherwise} \end{cases}
$$

1. Find the value of $k$
2. Find $F\left( x \right)$
3. Find the difference between the median and the fifth percentile of
   $X$

**<span class="underline">Solution:</span>**

**<span class="underline">Part (i):</span>**

The total area must equal 1 hence

$$
\int_{0}^{1}k + \int_{1}^{3}{4k} = \left\lbrack \text{kx} \right\rbrack_{0}^{1} + \left\lbrack 4kx \right\rbrack_{1}^{3} = 1
$$

$$
= \left( k - 0 \right) + \left( 12k - 4k \right) = 9k = 1
$$

$$
\therefore k = \frac{1}{9}
$$

**<span class="underline">Part (ii):</span>**

Integrate each case separately from its $- \infty$ to $x$

For the first interval $0 \leq x \leq 1$

$$
F\left( x \right) = \int_{0}^{x}\frac{1}{9} = \left\lbrack \frac{1}{9}x \right\rbrack_{0}^{x} = \frac{1}{9}x
$$

We must split next interval $0 \leq x \leq 3$ as

$$
F\left( x \right) = P\left( X \leq 3 \right) = P\left( X \leq 1 \right) + P\left( 1 \leq x \leq 3 \right)
$$

and $P\left( X \leq 1 \right) = F\left( 1 \right) = \frac{1}{9}$

$$
\therefore F\left( x \right) = \frac{1}{9} + \int_{1}^{x}{4 \times \frac{1}{9}}
$$

$$
= \frac{1}{9} + \left\lbrack 4 \times \frac{1}{9}x \right\rbrack_{1}^{x} = \frac{4}{9}x - \frac{3}{9}
$$

Writing in correct notation and fixing intervals (adding equal signs to inequalities)

$$
F(x) = \begin{cases} \frac{1x}{9} & 0 \leq x \leq 1 \\ \frac{4x}{9} - \frac{3}{9} & 1 \leq x \leq 3 \\ 1 & x > 3 \end{cases}
$$

**<span class="underline">Part (iii):</span>**

To find the median, you must check in which interval it lies. Do this by substituting the maximum value for $x$ in the first case

$$
\frac{1}{9} \times 1 = \frac{1}{9} < \frac{1}{2}
$$

This means the median does not lie in this interval $\therefore$

$$
\frac{4}{9}x - \frac{3}{9} = 0.5
$$

$$
x = \frac{15}{8}
$$

The fifth percentile lies in the first interval as
$\frac{1}{20} < \frac{1}{9}$ so

$$
\frac{1}{9}x = \frac{1}{20}
$$

$$
x = \frac{9}{20}
$$

Find the difference

$$
\frac{15}{8} - \frac{9}{20} = \frac{57}{40}
$$