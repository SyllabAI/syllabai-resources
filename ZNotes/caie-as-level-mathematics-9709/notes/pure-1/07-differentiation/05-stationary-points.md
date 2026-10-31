## Stationary points

* A stationary, or turning, point is a point on the graph where the gradient is 0.
  * Graphically - The gradient of the tangent, $f\prime(x)$, is horizontal and parallel to the $x$-axis at a stationary point.

 ![](../../../assets/0cb90add1d87-66d2d3bc1b81613ff2c69fdc9ff60bf5c4ba2ba5709945fb.21)

In this case:

* $x_1$ represents a local **maxima**, or a **maximum point**.
* $x_2$ represents a local **minima**, or a **minimum point**.




### **First derivative**

* The first derivative helps us find the $x$ coordinate of the stationary point.

To find the **stationary point**:

* Differentiate the function, $f(x)$, to get the first derivative, $f\prime(x)$.
  * $\frac{d}{dx} ~ f(x) = f\prime(x)$
* Equate $f\prime(x)$ to 0, as the gradient of the tangent at any stationary point is always 0. This will give you the $x$ coordinate of the stationary point.
  * $f\prime(x) = 0$
* Input the value of the $x$ coordinate, or coordinates in some cases, back into the original equation $f(x)$ to get the $y$ coordinate of the stationary point.



### **Second derivative**

* The second derivative helps us find the **nature of the stationary point**.
  * It helps us figure out if the stationary point is a **minima** or **maxima**.

To find the second derivative, **differentiate the first derivative**.

$$

\frac{d}{dx} \left(\frac{d}{dx} \right) = \frac{d}{dx} ~ f\prime(x) = f\prime\prime(x)
$$

It is also denoted by

$$

\frac{d^2}{dx^2} ~\text{or}~ \frac{d^2y}{dx^2}
$$

Inputting the $x$ coordinate of the stationary point into the second derivative, $f\prime\prime(x)$, will tell us the nature of the stationary point:

| Inequality | Nature of stationary point |
|----|----|
| $\frac{d^2y}{dx^2} > 0$ | Minimum point |
| $\frac{d^2y}{dx^2} < 0$ | Maximum point |


---
**<center>Example</center>**

A curve has equation

$$

f(x) = x^2 + \frac{2}{x}
$$

Find the coordinates of the stationary point on $f(x)$ and determine its nature.

**<center>Answer</center>**

To find the coordinate of the stationary point, we find the first derivative and equate it to 0.

$$

\frac{d}{dx} ~ x^2 + 2x^{-1} = 2x - 2x^{-2}
$$

$$

2x - 2x^{-2} = 0 \implies x = 1
$$

Inputting the $x$ coordinate back into the original equation, $f(x)$, will give us the $y$ coordinate of the stationary point.

$$

f(1) = 1^2 + \frac{2}{1} = 3
$$

So the coordinate of the stationary point is

$$

(1, 3)
$$

To find the nature of this stationary point, we find the second derivative by differentiating the first derivative

$$

f\prime\prime(x) = \frac{d}{dx} 2x - 2x^{-2} = 2 + 4x^{-3}
$$

We can now input the $x$ coordinate of the stationary point into $f\prime\prime(x)$

$$

f\prime\prime(1) = 2  + 4(1)^{-3} = 6
$$

As $\frac{d^2}{dx^2} > 0$, this stationary point is a **minima**.