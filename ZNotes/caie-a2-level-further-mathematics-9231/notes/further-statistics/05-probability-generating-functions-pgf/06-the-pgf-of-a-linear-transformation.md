## The PGF of a linear transformation

* $G_{aX + b}\left( t \right) = t^{b}G_{X}\left( t^{a} \right)$
* $G_{aX + bY + cZ + d} = t^{d}G_{X}\left( t^{a} \right) \times G_{Y}\left( t^{b} \right) \times G_{Z}\left( t^{c} \right)$

*In general:*

$$
G_{X_{1} + \ldots + X_{n}}\left( t \right) = G_{X_{1}}\left( t \right) \times \ldots \times G_{X_{n}}\left( t \right)
$$

*This is called The Convolution Theorem*

**<span class="underline">Question 6:</span>
<span class="underline">9231/04/SP/20:</span>**

Aisha has a bag containing 3 red balls and 3 white balls. She selects a
ball at random, notes its colour and returns it to the bag; the same
process is repeated twice more. The number of red balls selected by
Aisha is denoted by $X$.

a) Find the probability generating function $G_{X}\left( t \right)$ of
$\text{X.}$

Basant also has a bag containing 3 red balls and 3 white balls. He
selects three balls at random, without replacement, from his bag. The
number of red balls selected by Basant is denoted by Y.

b) Find the probability generating function $G_{Y}\left( t \right)$ of
$Y$.

The random variable $Z$ is the total number of red balls selected by
Aisha and Basant.

c) Find the probability generating function of $Z$, expressing your
answer as a polynomial.

d) Use the probability generating function of $Z$

to find $E(Z)\ $and $Var(Z)$.

**<span class="underline">Solution:</span>**

a) It’s best to make a Prob. Dist. table first, then make the PGF

| $x$ | 0 | 1 | 2 | 3 |
|----|----|----|----|----|
| $P\left( X = x \right)$ | $\frac{1}{8}$ | $\frac{3}{8}$ | $\frac{3}{8}$ | $\frac{1}{8}$ |

$$
\ \therefore G_{X}\left( t \right) = \frac{1}{8} + \frac{3}{8}t + \frac{3}{8}t^{2} + \frac{1}{8}t^{3}
$$

b) Same as part (a) but this time without replacement.

| $y$ | 0 | 1 | 2 | 3 |
|----|----|----|----|----|
| $P\left( Y = y \right)$ | $\frac{1}{20}$ | $\frac{9}{20}$ | $\frac{9}{20}$ | $\frac{1}{20}$ |

$$
\therefore G_{Y}\left( t \right) = \frac{1}{20} + \frac{9}{20}t + \frac{9}{20}t^{2} + \frac{9}{20}t^{3}
$$

c) Using the Convolution Theorem:

$$
G_{Z}\left( t \right) = G_{X + Y} = G_{X}\left( t \right) \times G_{Y}\left( t \right)
$$

$$
= \left( \frac{1}{8} + \frac{3}{8}t + \frac{3}{8}t^{2} + \frac{1}{8}t^{3} \right) \times
$$

$$
\left( \frac{1}{20} + \frac{9}{20}t + \frac{9}{20}t^{2} + \frac{9}{20}t^{3} \right)
$$

$$
= \frac{1}{160}\left( 1 + 12t + 39t^{2} + 56t^{3} + 39t^{4} + 12t^{5} + t^{6} \right)
$$

d) Recall that:

* $E\left( Z \right) = G\prime_{Z}\left( 1 \right)$
* $\text{Var}\left( Z \right) = G\prime\prime_{X}\left( 1 \right) + G\prime_{X}\left( 1 \right) - \left( G\prime_{X}\left( 1 \right) \right)^{2}$

$$
G\prime_{Z}\left( t \right) = \frac{1}{160}\left( 12 + 78t + 168t^{2} + 156t^{3} + 60t^{4} + 6t^{5} \right)
$$

Let $t = 1$

$$
G\prime_{Z}\left( 1 \right) = \frac{1}{160}\left( 12 + 78 + 168 + 156 + 60 + 6 \right)
$$

$$
\therefore E\left( Z \right) = 3
$$

$$
G_{Z}\left( t \right) = \frac{1}{160}\left( 78 + 336t + 468t^{2} + 240t^{3} + 30t^{4} \right)
$$

Let $t = 1$

$$
G\prime\prime_{Z}\left( 1 \right) = \frac{36}{5}
$$

$$
\text{Var}\left( Z \right) = \frac{36}{5} + 3 - \left( 3 \right)^{2} = \frac{6}{5}
$$

$$
\therefore\text{Var}\left( Z \right) = \frac{6}{5}
$$



