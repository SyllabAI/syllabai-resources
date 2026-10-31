## **Obtaining f(x) from F(x)**

  - $F$ is obtained by integrating $f$, and $f$ can be
    obtained by differentiating $F$



---



**<span class="underline">Example:</span>**

The random variable $X$ has CDF given by

$$
F\left( x \right) = \left\{ \begin{matrix}
0 \\
\frac{\left( x - 1 \right)^{3}}{8} \\
1 \\
\end{matrix} \right.\ \text{\ \ \ \ \ }\begin{matrix}
x \leq 1 \\
1 \leq x \leq 3 \\
x \geq 3 \\
\end{matrix}
$$

Find the form of the PDF of $X$

**<span class="underline">Solution:</span>**

$F(x)$ is unchanging for $x < 1$ and for $x > 3$, therefore
$f(x)$ is equal to $0$ for that interval. Hence, we must find the derivative of the function between the interval $1 < x < 3$

$$f\left( x \right) = F\prime\left( x \right)$$

$$f\left( x \right) = \frac{d}{{dx}}\left( \frac{\left( x - 1 \right)^{3}}{8} \right) = \frac{3}{8}\left( x - 1 \right)^{2}$$

Hence:
$$
f\left( x \right) = \left\{ \begin{matrix}
\frac{3}{8} (x-1)^2 \\
0 \
\end{matrix} \right.\ \text{\ \ \ \ \ }\begin{matrix}
1 < x < 3 \\
otherwise \
\end{matrix}
$$
