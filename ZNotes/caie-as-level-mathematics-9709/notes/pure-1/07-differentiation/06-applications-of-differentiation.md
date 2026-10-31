## Applications of Differentiation

* Differentiation can be used in modelling situations
  * Such as finding the maximum or minimum volume/area a model can have.
* If the variables in an equation vary with time, or any other variable, their rates of change can be connected using

$$

\frac{dy}{dx} = \frac{dt}{dx} \times \frac{dy}{dt}
$$


---

**<center>Example </center>**

The volume, $V$, of a spherical balloon is increasing at a constant rate of 50 cm$^3$/s. Find the rate of increase of the radius when the radius is 10 cm.

**<center>Answer</center>**

We are given $\frac{dV}{dt} = 50$, and are asked to find the value of $\frac{dr}{dt}$.

To solve the question, we first note that the volume of a sphere is given by

$$

V = \frac{4}{3} \pi r^3
$$

By differentiating the formula for a volume of a sphere, we get

$$

\frac{dV}{dr} = 4 \pi r^2
$$

So at $r = 10$

$$

\frac{dV}{dr} = 4 \pi (10)^2 = 400 \pi
$$

Using the connected rates of change formula, or chain rule:

$$

\frac{dV}{dr} = \frac{dt}{dr} \times \frac{dV}{dt}
$$

We can substitute in our values

$$

400 \pi = \frac{dt}{dr} \times 50
$$

$$

\frac{dt}{dr} = \frac{400 \pi}{50} = 8 \pi
$$

To find the value of $\frac{dr}{dt}$ we can take the reciprocal of the result

$$

\frac{dt}{dr} = \frac{1}{8 \pi}
$$



