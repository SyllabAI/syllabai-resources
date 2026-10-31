## Linear Interpolation

* in a given interval $[a,b]$ where root $x_1$ lies, calculate their corresponding y values

* substitute these values into the formula $\frac{b- x_1}{x_1 - a} = \left\| \frac{y_b}{y_a} \right\|$, derived from using similar triangles

* solve for $x_1$ to obtain an approximate root within interval $[a,b]$

### example question

* use linear interpolation to find an approximate root in the equation $f(x) = x^3 -  5x^2 + 2x + 5$ at interval $[-1,0]$

  * $f(-1) = -3$ and $f(0) = 5$

  * substitute into formula: $\frac{0 - x_1}{x_1 + 1} = \frac{5}{3}$

  * $-3x_1 = 5(x_1 + 1)$

  * $-3x_1 - 5x_1 = 5$

  * $-8x_1 = 5$

  * $x_1 = -\frac{5}{8}$