## Different types of Functions

### **Square root function**

* Consider a function $f(x) = \sqrt{ax + b}$
  * The **domain** must be chosen such that $ax + b > 0$ always. In this case the domain is $x > \frac{-b}{a}$.
  * The **range** of such a function is always $y > 0$
* For a more general way of solving, consider a function $f(x) = \sqrt{g(x)}$  \[where $g(x)$ is any function such as a linear function, quadratic, or even a higher degree polynomial\]
  * The **domain** must be chosen such that $g(x) \geq 0$ always
  * The **range** of function is always a positive, non-zero, interval.


### **Rational function**

* A rational function is a function written in the form $\frac{f(x)}{g(x)}$, where $g(x) ~ \cancel{=} ~ 0$.
* To find the domain
  * Find the values of $x$ for which $g(x) = 0$. These values of $x$ cannot be inputted into the function and must be excluded in the domain.
* To find the range
  * Input a large $x$ value, such as $999$ and $-999$. This will help you find the $y$ value which the rational function is approaching, but never reaches. This limits the range of the rational function.

If the function is written in the form

$$

f(x) = a + \frac{g(x)}{h(x)} ~~ \text{for} ~~ x \in \mathbb{R}
$$

Where $a$ is a non-zero constant, and $g(x)$ and $h(x)$ are functions.

* Then the **range** is $f(x) < a$ or $f(x) > a$ depending on if the function is approaching the value $a$ from above or below the line $y = a$. This can be checked by inputting a large $x$ value and seeing if the output is greater than or less than $a$.
  * Note that the inequality can change if the domain changes.


---

**<center>Example</center>**

Find the range of

$$

f(x) = \frac{2}{3} + \frac{2}{3(3x - 1)} ~~ \text{for} ~~ x > \frac{1}{3}
$$

**<center>Answer</center>**

Inputting in a large $x$ value, such as 999, gives us

$$

f(999) = \frac{2}{3} + \frac{2}{3(3(999) - 1)} 

$$

Which is greater than $\frac{2}{3}$, so the function is approaching this value from above. This gives us the range of the function as

$$

y > \frac{2}{3}

$$