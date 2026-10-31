## Equations of SHM

**Displacement:**

$$
x = x_{0}\sin(\omega t)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ x = x_{0}\cos(\omega t)
$$

Both equations give displacement $x$ at time $t$, but your choice depends entirely on where the motion begins at $t = 0$:

* Use $x = x_0 \sin(\omega t)$ when the motion starts at the **equilibrium position** ($x = 0$ at $t = 0$).

* Use $x = x_0 \cos(\omega t)$ when the motion starts at an **extreme position** / maximum amplitude ($x = x_0$ at $t = 0$).

> **Example:** A pendulum pulled to the right by $5\text{ cm}$ and released at $t = 0$ starts at maximum displacement. You must use $x = x_0 \cos(\omega t)$ with $x_0 = 5\text{ cm}$.

**Velocity:**

$v = \pm\omega \sqrt{x_0^2 - x^2}$

This calculates speed at any displacement $x$. Max speed $v_{\max} = \omega x_0$ occurs at $x = 0$.

**Acceleration:**

$$
a = - \omega^{2}x
$$

***Note:*** *The minus sign shows that, when the object is displaced to the right, the direction of its acceleration is to the left.*

**Derivation:**

Assuming motion starts at the equilibrium position ($x = 0$ at $t = 0$):

1. **Displacement:**

   $$x(t) = x_0 \sin(\omega t)$$

2. **Velocity** *(rate of change of displacement, $\frac{dx}{dt}$)*:

   $$v(t) = \frac{d}{dt} \left\[ x_0 \sin(\omega t) \right\] = x_0 \omega \cos(\omega t) = v_0 \cos(\omega t)$$

3. **Acceleration** *(rate of change of velocity, $\frac{dv}{dt}$)*:

   $$a(t) = \frac{d}{dt} \left\[ x_0 \omega \cos(\omega t) \right\] = -x_0 \omega^2 \sin(\omega t)$$

4. **Connecting back to defining equation:**

   Since $x(t) = x_0 \sin(\omega t)$, substitute $x$ into $a(t)$:

   $$a = -\omega^2 x$$