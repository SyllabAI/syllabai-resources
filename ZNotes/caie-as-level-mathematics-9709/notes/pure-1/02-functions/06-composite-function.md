## Composite Function

* A composite function is a combination of two functions
  * Commonly denoted by $g( ~f(x)~ )$ or $gf(x)$.
* Inputting a $x$ value into the function $f$ outputs $f(x)$. The same value, $f(x)$, is then inputted into another function $g$ which outputs $g(x)$.

A summary of the process has been described in the image

 ![Credits to YUMNA!!](../../../assets/880f3b7ffdf5-66c4f71d4d8df67a3b98c224dd08aec80d3c0bc887d85894.51)

* It is also important to note that $g( ~f(x)~)$ does not always equal $f(~g(x)~)$
* $f^2(x)$ implies $f( ~f(x)~ )$, unless stated otherwise.

### **Domain and Range of a Composite Function**

* As $f(x)$, or the $y$-value output of the function $f$, is inputted into the function $g$ as a $x$-value input
  * The domain and range of $g$ depends on the range of $f$.
* If the interval of **range values** for $f(x)$ is not included in the interval of **domain values** for $g(x)$, the composite function **cannot exist.**
  * If the range of $f(x)$ is included in the domain of $g(x)$, but is a smaller interval, then the domain of the composite function becomes a smaller interval too.


---

**<center>Example 1</center>**

Given

$$

f(x) = 2(x + 3)^2 - 7 ~~ \text{for} ~~ x \leq -4
$$

$$

g(x) = 2x - 3 ~~ \text{for} ~~ x \leq k
$$

Find the largest value of $k$ for which the composite function $f(~g(x)~)$ is defined.

**<center>Answer</center>**

* For a composite function $f(~g(x)~)$ to exist, the range of $g(x)$ must be included in the domain of $f(x)$.

The domain of $f(x)$ is $x \leq -4$, so we must find a value of $k$ for which the range of $g(x)$ is $y \leq -4$

Letting $g(x) = -4$, we get

$$

2x - 3 = - 4 \implies x = -\frac{1}{2}
$$

So the largest value of $k$ is

$$

k = -\frac{1}{2}
$$

$$

\phantom{invis}
$$

**<center>Example 2 </center>**

Given

$$

f(x) = -2x^2 + 12x - 3 ~~\text{for}~~ x \in \mathbb{R}
$$

$$

g(x) = 2x + 5 ~~\text{for}~~ x \in \mathbb{R}
$$

Find the values of $x$ for which $g(~f(x)~) + 1= 0$.

**<center>Answer</center>**

We can find the function $g(~f(x)~)$ by inputting $f(x)$ into $g(x)$

$$

g(~f(x)~) = 2(-2x^2 + 12x - 3) + 5 \implies -4x^2 + 24x - 1
$$

Now we can input this value into the equation we need to solve, $f( ~g(x)~ ) + 1 = 0$

$$

-4x^2 + 24x - 1 + 1 = 0 \implies 4x(-x + 6) = 0
$$

So the values of $x$ which satisfy the equation are

$$

x = 0 ~~\text{or}~~ x = 6
$$



