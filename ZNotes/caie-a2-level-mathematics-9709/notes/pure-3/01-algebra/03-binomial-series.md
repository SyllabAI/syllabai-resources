## Binomial Series

Expanding $\left( 1 + x \right)^{n}$ where $\left\| x \right\| < 1$

$$1 + \frac{n}{1}x + \frac{n\left( n - 1 \right)}{1 \times 2}x^{2} + \frac{n\left( n - 1 \right)\left( n - 2 \right)}{1 \times 2 \times 3}x^{3} + \ldots$$

- **Factor case:** if constant is not 1, pull out a factor from
  brackets to make it 1 & use general equation. Do not forget the
  indices.

- **Substitution case:** if bracket contains more than one $x$ term
  (e.g. ($2 - x + x^{2}$)) then make the last part $u$, expand and
  then substitute back in.

- **Finding the limit of** $x$ **in expansion:\
  **E.g. $\left( 1 + ax \right)^{n}$, limit can be found by
  substituting $\text{ax}$ between the modulus sign in
  $\left\| x \right\| < 1$ and altering it to have only $x$ in the
  modulus

**{S15-P31} Question 3:**

Show that, for small values of $x^{2},$

$$\left( 1 - {2x}^{2} \right)^{- 2} - \ \left( 1 + 6x^{2} \right)^{\frac{2}{3}\ } \approx kx^{4},$$

where the value of the constant $k$ is to be determined.

**<center>Solution:</center>**

*Expand* $\left( 1 - {2x}^{2} \right)^{- 2}$ *until the* $x^{4}$
*term*

$$\left( 1 + x \right)^{- 2} = 1 + \left( - 2 \right)x + \frac{- 2\left( \left( - 2 \right) - 1 \right)}{1 \times 2}x^{2}$$

$$= 1 - 2x + 3x^{2}$$

$$\left( 1 - 2x^{2} \right)^{- 2} = 1 - 2\left( 2x^{2} \right) + 3\left( 2x^{2} \right)^{2} = 1 + 4x^{2} + 12x^{4}$$

*Expand* $\ \left( 1 + 6x^{2} \right)^{\frac{2}{3}\ }$ *until the*
$x^{4}$ *term*

$$\left( 1 + x \right)^{\frac{2}{3}} = 1 + \left( \frac{2}{3} \right)x + \frac{\frac{2}{3}\left( \left( \frac{2}{3} \right) - 1 \right)}{1 \times 2}x^{2}$$

$$= 1 + \frac{2}{3}x - \frac{1}{9}x^{2}$$

$$\left( 1 + 6x^{2} \right)^{\frac{2}{3}} = 1 + \frac{2}{3}\left( 6x^{2} \right) - \frac{1}{9}\left( 6x^{2} \right)^{2} = 1 + 4x^{2} - 4x^{4}$$

*Subtract the terms of the expansion of*
$\left( 1 + 6x^{2} \right)^{\frac{2}{3}\ }$ *from those of*
$\left( 1 - {2x}^{2} \right)^{- 2}$

$$(1 - 4x^{2} + 12x^{4}) - (\ 1 + 4x^{2} - 4x^{4})$$

$$= - 8x^{2} + 16x^{4}$$

*The value of* $k$ *is:*

$$16$$