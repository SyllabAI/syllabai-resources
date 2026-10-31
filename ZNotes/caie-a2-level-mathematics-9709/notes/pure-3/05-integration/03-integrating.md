##  Integrating $\frac{\mathbf{f}^{\mathbf{'}}\mathbf{(x)}}{\mathbf{f(x)}}$

$$
\int_{}^{}\frac{\mathbf{f}^{\mathbf{'}}\left( \mathbf{x} \right)}{\mathbf{f}\left( \mathbf{x} \right)}dx = \ln\left| f(x) \right| + k
$$

&nbsp;

**<span class="underline">{S10-P32} Question 10:</span>**

By splitting into partial fractions, show that:

$$
\int_{1}^{2}{\frac{2x^{3} - 1}{x^{2}\left( 2x - 1 \right)}\text{dx}} = \frac{3}{2} + \frac{1}{2}\ln\left( \frac{16}{27} \right)
$$

**<center>Solution:</center>**

*Write as partial fractions*

$$
\int_{1}^{2}{\frac{2x^{3} - 1}{x^{2}\left( 2x - 1 \right)}\text{dx}} \equiv \int_{1}^{2}{1 + \frac{2}{x} + \frac{1}{x^{2}} + \frac{3}{2x - 1}\text{dx}}
$$

$$
\equiv x + 2\ln x - x^{- 1} - \frac{3}{2}\ln\left| 2x - 1 \right|
$$

*Substitute the limits*

$$
2 + 2\ln 2 - \frac{1}{2} - \frac{3}{2}\ln 3 - 1 - 2\ln 1 + 1 + \frac{3}{2}\ln 1
$$

$$
\frac{3}{2} + \frac{1}{2}\ln 16 + \frac{1}{2}\ln\frac{1}{3^{3}} \equiv \frac{3}{2} + \frac{1}{2}\ln\frac{16}{27}
$$
