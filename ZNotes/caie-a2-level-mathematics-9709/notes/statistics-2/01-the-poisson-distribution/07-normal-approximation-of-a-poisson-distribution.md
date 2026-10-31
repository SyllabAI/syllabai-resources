## Normal Approximation of a Poisson Distribution

* To approximate a Poisson distribution given by:

$$
X\sim P(\lambda)
$$

* If $\lambda > 15$
* Then we can use a normal distribution given by:

$$
X\sim N(\lambda,\lambda)
$$

**Apply continuity correction to limits:**

|    |    |
|----|----|
| **Poisson** | **Normal** |
| 𝑥 = 6 | 5.5≤𝑥≤6.5 |
| 𝑥 > 6 | 𝑥≥6.5 |
| 𝑥 ≥ 6 | 𝑥≥5.5 |
| 𝑥 < 6 | 𝑥≤5.5 |
| 𝑥 ≤ 6 | 𝑥≤6.5 |

**<span class="underline">{IS Ex 10h} Question 11:</span>**

The no. of flaws in a length of cloth, $l$m long has a Poisson
distribution with mean 0.04$l$


1. Find the probability that a 10m length of cloth has fewer than 2
   flaws.
2. Find an approximate value for the probability that a 1000m length of
   cloth has at least 46 flaws.
3. Given that the cost of rectifying $X$ flaws in a 1000m length of
   cloth is $X^{2}$ pence, find the expected cost.

**<span class="underline">Solution:</span>**

**Part (i):**

*Form the parameters of Poisson distribution*

$l = 10$ and $\lambda = 0.04l$

$$
\therefore\lambda = 0.4
$$

*Write down our distribution using correct notation*

$$
X\sim Po\left( 0.4 \right)
$$

*Write the probability required by the question*

$$
P\left( X < 2 \right)
$$

*From earlier equations:*

$$
P\left( X < 2 \right) = e^{- 0.4}\left( \frac{{0.4}^{0}}{0!} + \frac{{0.4}^{1}}{1!} \right) = 0.938
$$

**Part (ii):**

*Using question to form the parameters*

$l = 1000$ and $\lambda = 0.04l$

$$
\therefore\lambda = 40 > 15
$$

Thus, we can use the normal approximation

*Write down our distribution using correct notation*

$$
X\sim Po\left( 40 \right) \rightarrow Y\sim N\left( 40,\ 40 \right)
$$

*Write the probability required by the question*

$$
P\left( X \geq 46 \right)
$$

*Apply continuity correction for the normal distribution*

$$
P\left( Y \geq 45.5 \right)
$$

*Evaluate the probability*

$$
P\left( Y \geq 45.5 \right) = 1 - \Phi\left( \frac{45.5 - 40}{\sqrt{40}} \right) = 0.192
$$

**Part (iii):**

*Using the variance formula*

$$
\text{Var}\left( X \right) = E\left( X^{2} \right) - \left( E\left( X \right) \right)^{2}
$$

*For a Poisson distribution*

$E\left( X \right) = Var\left( X \right) = \lambda$ and
$\lambda = 40$

*Substitute into equation and solve for the unknown*

$$
\therefore 40 = E\left( X^{2} \right) - 40^{2}
$$

$E\left( X^{2} \right) = 1640$ pence

$$
E\left( X^{2} \right) = ₤16.40
$$

Expected cost for rectifying cloth is $₤16.40$