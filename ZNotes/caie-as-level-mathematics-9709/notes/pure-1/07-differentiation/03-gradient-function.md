## Gradient function

* The first derivative is also called the gradient function. It gives us the gradient of the tangent to the curve at a specific point.

A general equation of a tangent can be found using

$$
y = f\prime(x)x + c
$$

<center>To find the gradient of the tangent at the point (a, b), input x = a into the first derivative. </center>

$$
f\prime(a)
$$

Using this, we can re-write the **equation of the tangent** to the curve at the point (a, b) as

$$
y = f\prime(a)x + c
$$




### **Equation of perpendicular**

* To find the equation of a perpendicular to a point, we must first find the equation of the gradient of the tangent at that point on the curve.

We can consider the gradient of the tangent at $(x, y)$ to be $f\prime(x)$

Using the fact that the gradients of a perpendicular and a tangent follow the relation:

$$
m_1 \times m_2 = -1
$$

We can re-write the gradient of the perpendicular as

$$
f\prime(x) \times m_2 = -1 \implies m_2 = - \frac{1}{f\prime(x)}
$$


---

**<center> Example 1</center>**

Find the gradient of the tangent to the curve $y = 5x^2 + 3x$ at the point $x = 2$.

**<center>Answer</center>**

We first start by finding the gradient function, or the first derivative.

$$
\frac{d}{dx} ~ 5x^2 + 3x = 10x + 3
$$

Now we can input $x = 2$ into $f\prime(x)$

$$
f\prime(2) = 10(2) + 3 = 23
$$

So the gradient of the tangent to the curve at $x = 2$ is 23.

$$
\phantom{invis}
$$

**<center>Example 2</center>**

A curve is described by the equation

$$
f(x) = \frac{1}{\sqrt{x}} ~ \text{for} ~ x > 0
$$

The point $A$ is on the curve such that the normal to the curve at $A$ also passes through the origin. Find the coordinates of the point $A$

**<center>Answer</center>**

* With the given information, the point $A$ can be considered the point of intersection of the curve $f(x)$ and the perpendicular to the curve at that point.

To find the gradient of the normal, we first find the general gradient of a tangent to the curve by differentiating the curve once.

$$
f\prime(x) = \frac{d}{dx} ~ x^{- \frac{1}{2}} = - \frac{1}{2x^{\frac{3}{2}}}
$$

Now we can use the relationship between the gradients of a perpendicular and a tangent

$$
- \frac{1}{2x^{\frac{3}{2}}}  \times ~ m_2 = -1 \implies m_2 = -\frac{1}{- \frac{1}{2x^{\frac{3}{2}}}}
$$

So the gradient of the normal is

$$
m_2 = 2x^{\frac{3}{2}}
$$

Using this gradient, and the $y$-intercept as 0 (due to the question stating that the normal passes through the origin), we get the equation of the normal as

$$
y = mx + c \implies y = 2x^{\frac{3}{2}} \times x + 0
$$

$$
y = 2x^{\frac{5}{2}}
$$

Equating $f(x)$ and the equation of the perpendicular will give us the $x$ coordinate of $A$.

$$
x^{-\frac{1}{2}} = 2x^{\frac{5}{2}} \implies x = 2^{-\frac{1}{3}}
$$

Inputting this $x$-value into any one equation will give us the corresponding $y$-coordinate of $A$.

$$
 y = \left(2^{-\frac{1}{3}} \right)^{-\frac{1}{2}} \implies y = 2^{\frac{1}{6}}
$$

So the coordinates of $A$ are

$$
\left(2^{-\frac{1}{3}}, 2^{\frac{1}{6}} \right)
$$



