## Normal approximation

- The binomial distribution can be used to approximate a normal distribution.

<center>Let X follow a binomial distribution such that</center>
$$
X \sim B(n, p)
$$
$$
E(X) = \mu = np
$$
$$
Var(X) = \sigma^2 = np(1 - p) = npq
$$

<center>Using this, we can approximate a normal distribution:</center>
$$
X \sim N(np, npq)
$$

Conditions to approximate a normal distribution:

- $np > 5$
- $nq > 5$

### **Continuity Correction**

- A continuity correction must be applied as a binomial distribution is a **discrete** distribution, while a normal distribution is a **continuous** distribution.
  - This can be thought of as making a histogram continuous by manipulating an interval's lower and upper bounds.
    Due to this, we must **add** or **subtract 0.5** according to the inequality in the probability.

$$
z = \frac{x \pm 0.5 - \mu}{\sigma}
$$

Consider a constant $a$


|Probability|Continuity correction|Notes|
|:---|:---|:---|
|$P(x > a)$|$P(x > a + 0.5)$|Does not include $a$|
|$P(x \geq a)$|$P(x > a - 0.5)$|Includes $a$|
|$P(x < a)$|$P(x < a - 0.5)$|Does not include $a$|
|$P(x \leq a)$|$P(x < a + 0.5)$|Includes $a$|
|$P(a < x < b)$|$P(a + 0.5 < x < b - 0.5)$|Does not include $a$ or $b$|

---

**<center>Example</center>**

On a certain road 20% of the vehicles are trucks, 16% are buses and
remainder are cars. A random sample of 125 vehicles is taken. Using a
suitable approximation, find the probability that more than 73 are cars.

**<center>Answer</center>**

First we find the probability of the cars

$$
1 - \left( 0.16 + 0.2 \right) = 0.64
$$

So the binomial distribution is

$$
X\sim B(125, 0.64)
$$

First we check if a normal approximation can be used*

$125 \times 0.64 = 80$ and $125 \times \left( 1 - 0.64 \right) = 45$

Both conditions are satisfied so we can approximate a normal distribution.

$$
X\ \sim\ B\left( 125,\ 0.64 \right)\ \  \rightarrow \ \ \ X\ \sim\ N\left( 80,\ 28.8 \right)
$$

Apply the continuity correction

$$
P\left( X > 73 \right) = P(X \geq 73.5)
$$

Now we can find the probability

$$
P\left( X \geq 73.5 \right) = 1 - P\left( X \leq 73.5 \right)
$$

Next we standardise this value

$$
Z = \frac{73.5 - 80}{\sqrt{28.8}} = - 1.211
$$

As it is a negative value, we must subtract by one again

$$
1 - (1 - P\left( Z < - 1.211 \right) = P(Z < 1.211) = \phi(1.211)
$$

Using the normal table

$$
P = 0.8871
$$