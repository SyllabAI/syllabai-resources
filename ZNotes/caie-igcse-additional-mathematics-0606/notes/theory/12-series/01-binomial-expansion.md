# Series

## Binomial Expansion

The binomial theorem allows expansion of any expression in the form
$\left( x + y \right)^{n}$

The binomial expansion of  $(x + y)^n$ is:

$$
(x + y)^n = \binom{n}{0} x^n + \binom{n}{1} x^{n-1} y + \binom{n}{2} x^{n-2} y^2 + \ldots + \binom{n}{n} y^n
$$

**Example: Expand** $(2x - 1)^4$ :

$$
(2x - 1)^4 = \binom{4}{0}(2x)^4(-1)^0 + \binom{4}{1}(2x)^3(-1)^1 + \binom{4}{2}(2x)^2(-1)^2 +\binom{4}{3}(2x)^1(-1)^3 + \binom{4}{4}(-1)^4
$$

$$
= 1 \cdot 16x^4 + 4 \cdot 8x^3(-1) + 6 \cdot 4x^2(1) + 4 \cdot 2x(-1) + 1 \cdot 1
$$

$$
= 16x^4 - 32x^3 + 24x^2 - 8x + 1
$$

* The powers of $x$ are in descending order

**General term (rth)** in the expansion of $(a+b)^n$:

$$
T_{r+1} = \binom{n}{r} a^{n - r} b^r \quad \text{for } 0 \leq r \leq n
$$

### **Finding a Specific Term**

* Independent term $\rightarrow$ A term without a variable (independent of $x$)

**Example: Find the term containing $x^2$ in the expansion of $(3x - 2)^5$.**

* Use the general term formula:

$
T_{r+1} = \binom{5}{r} (3x)^{5 - r} (-2)^r = \binom{5}{r} \cdot 3^{5 - r} \cdot x^{5 - r} \cdot (-2)^r
$

* We want the term with $x^2$, so:

$
5 - r = 2 \Rightarrow r = 3
$

* Substitute $r = 3$ into the general term:

$
T_4 = \binom{5}{3} \cdot 3^2 \cdot (-2)^3 \cdot x^2 = 10 \cdot 9 \cdot (-8) \cdot x^2 = -720x^2
$

* So, the required term is:

$
-720x^2
$

Therefore, the coefficient of $x^2$ is $-720$.