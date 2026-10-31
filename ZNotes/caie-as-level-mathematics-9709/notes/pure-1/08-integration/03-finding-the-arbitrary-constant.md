## Finding the arbitrary constant

- To be able to find the value of the constant we must be given a point on the curve.

Consider a point $(e, f)$ on the curve $G(x)$, where $G(x)=F(x) + c$. We are given a derivative $f(x)$. To find the original equation:
$$
\int f(x) \~dx = F(x) + c
$$
Using the points given
$$
f = F(e) + c \implies c = f - F(e)
$$

---

**<center>Example</center>**
A curve is such that $\frac{dy}{dx} = 2x^2 - 5$. Given that the point $(3, 8)$ lies on the curve, find the equation of the curve.
**<center>Answer</center>**
We begin by integrating the derivative given.
$$
\int 2x^2 - 5 \~dx = \frac{2x^{2 + 1}}{2 + 1} - 5x + c
$$
Giving us
$$
y = \frac{2x^3}{3} - 5x + c
$$
We can now substitute in the points given in the question
$$
8 = \frac{2(3)^3}{3} - 5(3) + c \implies c = +5
$$
So the equation of the curve is
$$
y = \frac{2x^3}{3} - 5x + 5
$$