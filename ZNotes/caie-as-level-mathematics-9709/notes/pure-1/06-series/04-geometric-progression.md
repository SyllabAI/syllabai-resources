## Geometric Progression

* A geometric progression (GP) is a series of numbers that share a common ratio between consecutive terms.
  * An example of a geometric sequence is: $3, 9, 27, 81, \cdots$. Each term in this series is being multiplied by a common ratio of 3.
  * The **first term** is given by $a$, while the **common ratio** is denoted by $r$

$$

\text{1}^{st} ~~ \text{term} = u_1 = a
$$

$$

\text{2}^{nd} ~~ \text{term} = u_2 = ar
$$

$$

3^{rd} ~~ \text{term} = u_3 = ar^2
$$

$$

\cdots
$$

$$

(n - 1)^{th} ~~ \text{term} = u_{n ~ - ~ 1} = ar^{n ~ - ~ 2}
$$

$$

n^{th} ~~ \text{term} = u_n = ar^{n ~ - ~ 1}
$$

$$

(n + 1)^{th} ~~ \text{term} = u_{n ~ + ~ 1} =  ar^n
$$

* The formula for the $n^{th}$ term is also given in the MF19 formula sheet



### **Finding the common ratio**

As mentioned previously, the common ratio must be the same between consecutive terms.

This can be written as

$$

r = \frac{u_2}{u_1} = \frac{u_3}{u_2} = \cdots = \frac{u_n}{u_{n - 1}} = \frac{u_{n + 1}}{u_n}
$$

We can re-write this ratio as

$$

r = \frac{ar}{a} = \frac{ar^2}{ar} = \cdots = \frac{ar^{n ~ - ~ 1}}{ar^{n ~ - ~ 2}} = \frac{ar^{n}}{ar^{n ~ - ~ 1}}
$$

* Note that the denominator cancels all the terms of the numerator, and leaves $r$ as the only term.



### **Sum of Geometric Progression**

* The sum of a geometric progression is the sum of terms in a given sequence.
  * $S_n$ denotes the sum till the $n^{th}$ term.

It is given in MF19, and is denoted by

$$

S_n = \frac{a(1 - r^n)}{1 - r} ~~ [r < 1]
$$

<center>Another formula exists for the case r > 1 </center>

$$

S_n = \frac{a(r^n - 1)}{r - 1} ~~ [r > 1]
$$

* The **sum till infinity** of a geometric progression, given in MF19, is denoted by

$$

S_{\infty} = \frac{a}{1 - r}  \quad [-1 < r < 1]
$$

* The inequality, $-1 < r < 1$, is also written as |$r$| $ < 1$ but implies the same.
  * For a geometric progression to **converge**, or reach a finite value when the sum is taken till infinity, it **must** **satisfy** this inequality.


---

**<center>Example 1</center>**

Find the $10^{th}$ term of the geometric progression, with the first term $3$ and a ratio of $\frac{3}{4}$.

**<center>Answer</center>**

* From the question:
  * $a = 3$ and $r = \frac{3}{4}$, giving us $u_n = 3\left(\frac{3}{4}\right)^{n ~ - ~ 1}$

So to find the $10^{th}$ term,

$$

u_{10} = 3\left(\frac{3}{4}\right)^{10 ~ - ~ 1} \implies ~ 0.225
$$

$$
\phantom{invis}
$$

**<center>Example 2</center>**

The first 3 terms of a geometric progression are: $x+2$, $3x$, $\frac{9}{4}x^2$ ,where $x > 0$, show that $9x^3 -18x^2 = 0$ and find the value of $r$ and $x$.

**<center>Answer</center>**

We know the common ratio, $r$, is the ratio of any two consecutive terms

$$

r = \frac{3x}{x+2} = \frac{\frac{9}{4}x^2}{3x}
$$

Now we can begin simplifying our ratio

$$
\frac{9x^2}{x+2} = \frac{9}{4}x^2
$$

$$
4(9x^2) = 9x^2(x+2)
$$

$$
36x^2 = 9x^3+ 18x^2
$$

$$

\implies 9x^3 -18x^2 = 0
$$

We can now find the value of $r$ and $x$

$$
9x^3 = 18x^2
$$

$$
\frac{x^3}{x^2} = \frac{18}{9} \implies x = 2
$$

Substituting the value of $x$ back into the common ratio gives us:

$$
r = \frac{3(2)}{2+2} = \frac{3}{2}
$$



