## **Distribution of a Function of a Random Variable**

* We can deduce the distribution of a simple function of X either
  increasing or decreasing with this procedure:

$$
f_{X} \rightarrow F_{X} \rightarrow F_{Y} \rightarrow f_{Y}
$$



---



**<span class="underline">Example:</span>**

The random variable $X$ has pdf $f_{X}\left( x \right)$ given by,

$$
f_X\left( x \right) = \left\{ \begin{matrix}
1 \\
0 \\
\end{matrix} \right.\ \text{\ \ \ \ \ }\begin{matrix}
2 < x < 3\\
otherwise \\
\end{matrix}
$$

The random variable $Y$ is given by $Y = 2X + 3$. Determine the pdf
and cdf of $Y$.

**<span class="underline">Solution:</span>**

First we find $F_{X}(x)$ 
$$
F_X\left( x \right) = \left\{ \begin{matrix}
0 \\
x - 2 \\
1 \\
\end{matrix} \right.\ \text{\ \ \ \ \ }\begin{matrix}
x \leq 2 \\
1 \leq x \leq 3 \\
x \geq 3 \\
\end{matrix}
$$

Next, we find the ranges for $Y$

$$
\left( 2 \times 2 \right) + 3 \leq y \leq \left( 3 \times 2 \right) + 3
$$

$$
7 \leq y \leq 9
$$

Convert the CDF from $X$ to $Y$ using the given relationship

$$F_{Y}\left( y \right) = P\left( Y \leq y \right) = P\left( 2X + 3 \leq y \right)$$

$$\implies P\left( X \leq \frac{1}{2}\left( y - 3 \right) \right)$$

Now substitute $\frac{1}{2}\left( y - 3 \right)$ for x in $F_X$

$$\left( \frac{1}{2}\left( y - 3 \right) \right) - 2 \Longrightarrow \frac{1}{2}\left( y - 7 \right)$$

Express the CDF of $Y$ with the ranges 
$$
F_Y\left( x \right) = \left\{ \begin{matrix}
0 \\
\frac{1}{2}(y-7) \\
1 \\
\end{matrix} \right.\ \text{\ \ \ \ \ }\begin{matrix}
x \leq 7 \\
7 \leq y \leq 9 \\
x \geq 9 \\
\end{matrix}
$$

Differentiate function to find PDF
$$
f_Y\left( x \right) = \left\{ \begin{matrix}
\frac{1}{2}(y-7) \\
0 \\
\end{matrix} \right.\ \text{\ \ \ \ \ }\begin{matrix}
7 \leq y \leq 9 \\
otherwise \\
\end{matrix}
$$


* Method can be used for both increasing and decreasing functions as
  well as functions with powers (e.g. $W = X^{2}$)



