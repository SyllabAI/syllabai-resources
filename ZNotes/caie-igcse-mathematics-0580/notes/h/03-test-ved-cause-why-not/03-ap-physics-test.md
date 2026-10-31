Example: Nonuniform Rob

A rob of length *L* has linear density varying with position:

$$
\lambda(x) = \lambda_0 \frac{x}{L}, \quad 0 \le x \le L
$$

* Total Mass

$$
M = \int_0^L \lambda(x), dx = \int_0^L \lambda_0 \frac{x}{L}, dx = \frac{\lambda_0 L}{2}
$$

* Center of mass

$$
x_{\text{COM}} = \frac{1}{M} \int_0^L x \lambda(x), dx
= \frac{1}{\lambda_0 L / 2} \int_0^L x \cdot \lambda_0 \frac{x}{L}, dx
= \frac{2L}{3}
$$