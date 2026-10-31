## Rules of differentiation

**1.Chain Rule**

If $y$ depends on $u$, and $u$ depends on $x$, then:
$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
$$

Example:

Find $\frac{d}{dx} \left( (3x + 2)^5 \right)$

Let $y = u^5$, where $u = 3x + 2$

Then, $\frac{dy}{du} = 5u^4$, $\quad \frac{du}{dx} = 3$

So$$\frac{dy}{dx} = 5(3x + 2)^4 \cdot 3 = 15(3x + 2)^4$$

---

**2.Product Rule**

If $y = uv$, where both $u$ and $v$ are functions of $x$, then:
$$
\frac{dy}{dx} = u \cdot \frac{dv}{dx} + v \cdot \frac{du}{dx}
$$

Example: Find $\frac{d}{dx} \left( x^2 \sin x \right)$

Let $u = x^2$, $v = \sin x$

Then,\
$\frac{du}{dx} = 2x$, $\quad \frac{dv}{dx} = \cos x$

So$$\frac{dy}{dx} = x^2 \cos x + 2x \sin x$$

---

**3.Quotient Rule**

If $y = \frac{u}{v}$, where both $u$ and $v$ are functions of $x$, then:
$$
\frac{dy}{dx} = \frac{v \cdot \frac{du}{dx} - u \cdot \frac{dv}{dx}}{v^2}
$$

Example: Find $\frac{d}{dx} \left( \frac{x^2}{\cos x} \right)$

Let $u = x^2$, $v = \cos x$

Then,\
$\frac{du}{dx} = 2x$, $\quad \frac{dv}{dx} = -\sin x$

So$$\frac{dy}{dx} = \frac{\cos x \cdot 2x - x^2 (-\sin x)}{\cos^2 x} = \frac{2x \cos x + x^2 \sin x}{\cos^2 x}$$