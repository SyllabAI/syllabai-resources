## Finding Area Under and Between Curves

**1.Find the area between a curve $y = f(x)$ and the $x$-axis from $x = a$ to $x = b$**:

$$\text{Area}  = \int_a^b f(x) dx$$

- If $f(x) \geq 0$ on $(a, b)$, the integral gives the area directly.
- If $f(x)$ is partly negative, split the integral or use absolute values.

**2.Find the area between a curve $y = f(x)$ and a horizontal line $y = c$:**

$$\text{Area} = \int_a^b \|f(x) - c\| dx$$

- Split the integral at points where $f(x) = c$ if needed.

---

**3.If $y = f(x)$ is the upper curve and $y = g(x)$ is the lower curve from $x = a$ to $x = b$**

$$\text{Area} = \int_a^b \left[ f(x) - g(x) \right] dx$$

- Always check which curve is on top before applying the formula.

**4.Find the area under $y = f(x)$ from $x = a$ to $x = b$:**

$$
\int_a^b f(x) dx = F(b) - F(a)
$$

The constant of integration $+c$ cancels out during subtraction and can be ignored.

---

**5.Find the area between $y = x^2$ and $y = x + 2$ between points of intersection.**

1. Solve for points of intersection:
   $
   x^2 = x + 2 \Rightarrow x^2 - x - 2 = 0 \Rightarrow x = -1, 2
   $

2. Determine which curve is on top:
   $
   y = x + 2 > x^2 \text{ on } (-1, 2)
   $

3. Apply the formula:

   $$\text{Area} = \int_{-1}^{2} \left[ (x + 2) - x^2 \right] dx \implies \int_{-1}^{2} (-x^2 + x + 2) dx$$

**6.If:**

- **$y = f(x)$ is above the $x$-axis on $(a, c)$**
- **$y = f(x)$ is below the $x$-axis on $(c, b)$**

Then:

$$\text{Total Area} = \int_a^c f(x) dx + \left\| \int_c^b f(x) dx \right\|$$

Alternatively:

$$\text{Area} = \int_a^b \|f(x)\| dx$$

---

**7.Find area in terms of $y$ instead of $x$:**

1. Rearrange the equation to get $x = f(y)$
2. Integrate with respect to $y$:
   $
   \int_c^d f(y) dy
   $
3. Evaluate:
   $$
   \int_c^d f(y), dy = F(d) - F(c)
   $$

**8.If the region is split at $x = c$, then:**

$$\text{Area} = \int_a^c f(x) dx + \int_c^b g(x) dx$$

Use this when:

- The curves intersect.
- The top or bottom function changes within the interval.