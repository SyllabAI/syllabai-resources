## Combinations of Random Variables

  - Expectations of combinations of random variables:

$$E\left( aX + bY \right) = aE\left( X \right) + bE\left( Y \right)$$

  - Variance of combinations of independent random variables:

$$\text{Var}\left( aX + bY + c \right) = a^{2}\text{Var}\left( X \right) + b^{2}\text{Var}\left( Y \right)$$

$$\text{Var}\left( X \pm Y \right) = Var\left( X \right) + Var(Y)$$

  - Combinations of identically distributed random variables having mean
    $\mu$ and variance $\sigma^{2}$

$E\left( 2X \right) = 2\mu$ and
$E\left( X_{1} \right) + E\left( X_{2} \right) = 2\mu$

$\text{Var}\left( 2X \right) = 4\sigma^{2}$ and
$\text{Var}\left( X_{1} + X_{2} \right) = 2\sigma^{2}$

**<span class="underline">{IS Ex 6b} Question 3:</span>**

It is given that $X_{1}$ and $X_{2}$ are independent, and
$E\left( X_{1} \right) = E\left( X_{2} \right) = \mu$,
$\text{Var}\left( X_{1} \right) = Var\left( X_{2} \right) = \sigma^{2}$.
Find $E(\overline{X})$ and $\text{Var}\left( \overline{X} \right)$,
where $\overline{X} = \frac{1}{2}(X_{1} + X_{2})$

**<span class="underline">Solution:</span>**

*Split the variance into individual components*

$$\text{Var}\left( \frac{1}{2}\left( X_{1} + X_{2} \right) \right) = \left( \frac{1}{2} \right)^{2}\text{Var}\left( X_{1} \right) + \left( \frac{1}{2} \right)^{2}\text{Var}\left( X_{2} \right)$$

*Substitute given values, hence*

$$\text{Var}\left( \frac{1}{2}\left( X_{1} + X_{2} \right) \right) = \frac{1}{4}\sigma^{2} + \frac{1}{4}\sigma^{2} = \frac{1}{2}\sigma^{2}$$