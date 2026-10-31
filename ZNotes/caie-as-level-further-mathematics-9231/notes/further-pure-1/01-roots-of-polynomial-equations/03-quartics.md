## Quartics

Finally, let us now consider a **quartic** with roots, $\alpha$, $\beta$, $\gamma$ and $\delta$, such that:

$$
ax^4 + bx^3 + cx^2 + dx + e = a(x - \alpha)(x - \beta)(x - \gamma)(x - \delta)
$$

**Dividing** both sides by **a** and then **expanding** the right hand side gives us:

$$
x^4 + \frac{bx^3}{a} + \frac{cx^2}{a} + \frac{dx}{a} + \frac{e}{a}
$$

$$
=
$$

$$
x^4 - (\alpha + \beta + \gamma + \delta)x^3 + (\alpha\beta + \alpha\gamma + \alpha\delta + \beta\gamma + \beta\delta + \gamma\delta)x^2 - (\alpha\beta\gamma + \alpha\beta\delta + \alpha\gamma\delta + \beta\gamma\delta)x + (\alpha\beta\gamma\delta)
$$

Upon **comparing coefficients** we can deduce that:

$$
\text{Sum of roots taken one at a time} = \sum \alpha = \alpha + \beta + \gamma + \delta = \frac{-b}{a}
$$

$$
\text{Sum of roots taken two at a time} = \sum \alpha\beta = \alpha\beta + \alpha\gamma + \alpha\delta + \beta\gamma + \beta\delta + \gamma\delta = \frac{c}{a}
$$

$$
\text{Sum of roots taken three at a time} = \sum \alpha\beta\gamma = \alpha\beta\gamma + \alpha\beta\delta + \alpha\gamma\delta + \beta\gamma\delta = \frac{-d}{a}
$$

$$
 \text{Product of roots} = \sum \alpha\beta\gamma\delta = \alpha\beta\gamma\delta = \frac{e}{a}
$$

Thus, a **quartic** can also be written as:

$$
x^4 - \left(\sum \alpha \right)x^3 + \left(\sum \alpha\beta \right)x^2 - \left(\sum \alpha\beta\gamma \right)x + \left(\sum \alpha\beta\gamma\delta \right)
$$



