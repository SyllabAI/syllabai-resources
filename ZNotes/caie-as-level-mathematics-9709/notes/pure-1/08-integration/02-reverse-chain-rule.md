## Reverse Chain Rule

- The reverse chain rule helps us integrate **linear functions** that are raised to an exponent.

Consider $g(f(x))$ such that
$$
\frac{d}{dx} g(~f(x)~) = g\prime(~f(x)~) \times f\prime(x)
$$
We can integrate the result as such
$$
\int g\prime(~f(x)~) \times f\prime(x) \~dx = g(~f(x)~) + c
$$

<center>An important application of the reverse chain rule is shown below.</center>
<center>[a and b are constant real numbers]</center>

$$
\int (ax + b)^n , dx
= \frac{(ax + b)^{n + 1}}
{\left[ \frac{d}{dx}(ax + b) \right] \times (n + 1)} + C
$$

$$
\text{This simplifies to}
$$

$$
\int (ax + b)^n , dx
= \frac{(ax + b)^{n + 1}}{a \times (n + 1)} + C
$$

- This is valid for all real numbers $n \neq -1$

---

**<center>Example</center>**
Integrate $\frac{1}{(2x + 3)^{2}}$.
**<center> Answer</center>**
Using the reverse chain rule
$$
\int (2x + 3)^{-2} = \frac{(2x + 3)^{-2 + 1}}{[\frac{d}{dx} (2x + 3)] \times (-2 + 1)} + c
$$
This simplifies to
$$
\frac{1}{4x + 6} + c
$$