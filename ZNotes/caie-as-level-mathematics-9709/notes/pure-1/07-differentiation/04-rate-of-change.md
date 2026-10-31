## Rate of change

* The rate of change of a function can be connected to the rate of change of its gradient.
  * A **positive gradient** means the function has an **increasing** $y$-value as the $x$-value increases. This is called an **increasing function**.
  * A **negative gradient** means the function has a **decreasing** $y$-value as the $x$-value increases. This is called a **decreasing function**.
  * A **gradient of zero** means the function is **neither** decreasing or increasing.

 ![](../../../assets/c195e71111a6-66d2d1701b81613ff2c69f65987d81b206168adb35af24a8.55)

Using the graph above, we can re-write the rate of change as

| Gradient function - $f\prime(x)$ | Gradient | Function - $f(x)$ |
|----|----|----|
| $f\prime(x) > 0$ | Increasing | Increasing function |
| $f\prime(x)$ = 0 | Stationary | Stationary point |
| $f\prime(x) < 0$ | Decreasing | Decreasing function |

* It is also important to note that $f\prime(x) > 0$ **does not always imply** $f(x) > 0$, vice versa.


### **Maximum point**

 ![](../../../assets/2204ed1bc3c8-66d2d1701b81613ff2c69f65d26e8a4f0ba95909d0797f91.59)Given a **maxima** with $x$ coordinate $c$:

| Left of maxima | Right of maxima |
|----|----|
| Increasing gradient, $f\prime(x) > 0$ | Decreasing gradient, $f\prime(x) < 0$ |
| Function is **increasing** | Function is **decreasing** |


### **Minimum point**

 ![](../../../assets/593465a7d1db-66d2d1701b81613ff2c69f6551a1b9cd8d184a0176cbe7fb.40)Given a **minima** with $x$ coordinate $c$:

| Left of minima | Right of minima |
|----|----|
| Decreasing gradient, $f\prime(x) < 0$ | Increasing gradient, $f\prime(x) > 0$ |
| Function is **decreasing** | Function is **increasing** |


---

**<center>Example 1</center>**

A function is defined by

$$

f(x) = \frac{5}{1 - 3x} ~ \text{for} ~ x \geq 1
$$

Determine wether $f$ is an increasing function, decreasing function, or neither.

**<center>Answer</center>**

First we find the first derivative, or the gradient function, of $f(x)$ using the chain rule.

$$

\frac{d}{dx} ~ 5(1 - 3x)^{-1} = -1 \times 5 \times -3 \times (1 - 3x)^{-2}
$$

$$

f\prime(x) = 15 \times (1 - 3x)^{-2}
$$

As:

* The 15 being multiplied is positive, it does not change the sign of the function.
* $(1 - 3x)^{-2}$ is always positive as it is squared, it does not change the sign of the function.

Using this logic, we can deduce that

$$

f\prime(x) > 0
$$

So $f(x)$ is an increasing function for all real values of $x$.


$$
\phantom{invis}
$$

**<center> Example 2</center>**

Find the set of values of $x$ for which the function $f(x) = \frac{(2x - 3)^3}{6} - 4x$ is increasing.

**<center> Answer</center>**

We start by finding the first derivative, or gradient function, of $f(x)$ using the chain rule.

$$

\frac{1}{6} \times \frac{d}{dx} ~ (2x - 3)^3 + \frac{d}{dx} -4x = \frac{1}{6}\left(3 \times 2 \times (2x - 3)^{2} \right) - 4
$$

$$

f\prime(x) = (2x - 3)^2 - 4
$$

The function is increasing when $f\prime(x) > 0$

$$

(2x - 3)^2 - 4 > 0 \implies x > \frac{5}{2} ~~ \text{or} ~~ x < \frac{1}{2}
$$



