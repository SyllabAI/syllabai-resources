## Finding probabilities

* The probability, $P(X = x)$, for a PGF can be found using 2 methods.
  * Binomial expansion
  * Maclaurin’s series
* The coefficient of $t^x$ gives us the probability for $P(X = x)$ in both methods.




### **Method 1**

Method 1 involves the use of the binomial expansion.

**<center>Example</center>**

Let $X$ be a discrete random variable taking the values **0, 2, 4,** $\cdots$. The PGF is given by:

$$
G_{X}(t) = \frac{1}{3 - 2t^2}
$$

Find $P(X = 4)$.

**<center>Answer</center>**

Using binomial expansion:

$$

\frac{1}{3}\left(1 - \frac{2t^2}{3} \right)^{-1} \implies \frac{1}{3}\left(1 + \frac{2t^2}{3} + \left(\frac{2t^2}{3} \right)^2 + \cdots \right)
$$

Looking for the coefficient of $t^4$, we get

$$

\frac{1}{3}\left(\frac{4}{9} \right) \implies \frac{4}{27}
$$

<center>So</center>

$$

P(X = 4) = \frac{4}{27}
$$

$$

\phantom{invis}
$$



### **Method 2**

Method 2 involves the use of Maclaurin’s series. We will use the same example.

**<center>Example</center>**

Let $X$ be a discrete random variable taking the values **0, 2, 4,** $\cdots$. The PGF is given by:

$$

G_{X}(t) = \frac{1}{3 - 2t^2}
$$

Find $P(X = 4)$.

**<center>Answer</center>**

Using Maclaurin’s series:

$$

G_{X}(t) = G_{X}(0) + G\prime_{X}(0)t + \frac{G\prime\prime_{X}(0)t^2}{2!} + \frac{G\prime\prime\prime_{X}(0)t^3}{3!} + \frac{G\prime\prime\prime\prime_{X}(0)t^4}{4!} + \cdots
$$

$$
G\prime\prime\prime\prime_{X}(t) = \frac{-96(20x^4 + 60x^2 + 9)}{(2x^2 - 3)^5}
$$

$$

\frac{G\prime\prime\prime\prime_{X}(0)}{4!} = \frac{-96(20(0)^4 + 60(0)^2 + 9)}{(2(0)^2 - 3)^5} \times \frac{1}{4!} \implies \frac{4}{27}
$$

<center>So</center>

$$

P(X = 4) = \frac{4}{27}
$$



