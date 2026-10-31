## The PGF

* The PGF can be written as a single summation:

$$
G_{X}\left( t \right) = \sum_{x}^{}{t^{x_{i}}\text{\ P}\left( X = x_{i} \right)}
$$

Or in its expanded form:

$$

G_{X}(t) = P(X = x_0)t^{x_0} + P(X = x_1)t^{x_1} + P(X = x_2)t^{x_2} + \cdots + P(X = x_i)t^i
$$

* Notice that the expression for $G_{X}\left( t \right)$ is the same as that for the expectation function, $E\left( t^{X} \right)$, and so:

$$
G_{X}\left( t \right) = \sum_{x}^{}{t^{x_{i}}\text{\ P}\left( X = x_{i} \right)} = E\left( t^{X} \right)
$$

* The variable $t$ is called a dummy variable in this case, and has no significance itself, but $t$ does have an important role in finding the expectation of $X$.

**<span class="underline">Example:</span>**

Consider the Probability distribution:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|----|----|----|----|----|----|----|----|
| $P\left( X = x \right)$ | 0.1 | 0.2 | 0.3 | 0.15 | 0.1 | 0.1 | 0.05 |

**<span class="underline">Solution:</span>**

Apply the general form of the PGF:

$$
G_{X}\left( t \right) = \sum_{x}^{}{t^{x_{i}}\text{\ P}\left( X = x_{i} \right)}
$$

$$
G_{X}\left( t \right) = 0.1t^{0} + 0.2t^{1} + 0.3t^{2} + 0.15t^{3} + 0.1t^{4} + 0.1t^{5} + 0.05t^{6}
$$

