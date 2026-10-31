## Newton-Raphson method

* Newton-Raphson formula:

$$
x_{n+1} = x_n -\frac{f(x_n)}{f’(x_n)}
$$

* exam questions will supply an initial approximation to a root, as well as how many times you will need to perform the Newton-Raphson method

### example question

* $f(x) = x^3 -  5x^2 + 2x + 5$, taking $-0.6$ as a first approximation of $x_0$, apply the Newton-Raphson process once to find a 2nd approximation of $x_0$. Give your answer to 3 d.p
  * $f’(x) = 3x^2 - 10x + 2$

  * $f(-0.6) = 1.784$ and $f’(-0.6) = 9.08$

  * $x_1 = x_0 -\frac{f(x_0)}{f’(x_0)}$

  * $x_1 = -0.6 -\frac{1.784}{9.08}$

  * $x_1 = -0.7964 = -0.796$