## Trigonometry in series

* Trigonometric functions can be included in series and sequences.
  * They make use of identities such as $tan(\theta) = \frac{sin(\theta)}{cos(\theta)}$ and $sin^2(x) + cos^2(x) = 1$
  * These series can also exist for a specific domain, such as $0 \leq x \leq \pi$, but questions will usually specify the value of $x$ or $\theta$ to use.


### **Trigonometric Arithmetic Progression**

**<center> Example 1 </center>**

Given an arithmetic sequence with first term $sin^2(\theta)$, where $0 < \theta < \frac{\pi}{2}$, and second term $sin^2(\theta)cos^2(\theta)$, find the common difference in terms of $sin(\theta)$

**<center>Answer</center>**

* From the question
  * $a = sin^2(\theta)$ and $a + d = sin^2(\theta)cos^2(\theta)$

$$

\text{Using the fact that} ~ u_{n - 1} - u_n = d
$$

$$

sin^2(\theta)cos^2(\theta) - sin^2(\theta) \implies sin^2(\theta)(cos^2(\theta) - 1)
$$

$$

\text{After noticing that} ~ cos^2(\theta) - 1 = -sin^2(\theta)
$$

$$

sin^2(\theta)(-sin^2(\theta)) \implies d = -sin^4(\theta)
$$


$$
\phantom{invis}
$$

**<center> Example 2 </center>**

Given an arithmetic sequence with the $n^{th}$ term $u_n = sin^2(\theta) + (n - 1)(-sin^4(\theta))$, find the sum of the first 16 terms when $\theta = \frac{\pi}{3}$.

**<center>Answer</center>**

Using $\theta = \frac{\pi}{3}$, we get

$$

a = sin^2\left(\frac{\pi}{3}\right) = \frac{3}{4}
$$

$$

d = -sin^4\left(\frac{\pi}{3}\right) = -\frac{9}{16}
$$

Now we can use the formula for the sum till the $n^{th}$ term

$$

S_n = \frac{n}{2}[2a + (n - 1)d]
$$

$$

S_{16} = \frac{16}{2}[2\left(\frac{3}{4}\right) + (16 - 1)\left(-\frac{9}{16}\right)] = -\frac{111}{2}
$$

### **Trigonometric Geometric Progression**

**<center>Example</center>**

Given a geometric progression with first term $sin^2(\theta)$, where $0 < \theta < \frac{\pi}{2}$, and second term $sin^2(\theta)cos^2(\theta)$, find the sum till infinity.

**<center>Answer</center>**

* From the question
  * We know that $a = sin^2(\theta)$ and $ar = sin^2(\theta)cos^2(\theta)$

<center>To find the common ratio r:</center>

$$

r = \frac{sin^2(\theta)cos^2(\theta)}{sin^2(\theta)} = cos^2(\theta)
$$

<center>We can now use the sum till infinity formula for a geometric progression </center>

$$

S_{\infty} = \frac{sin^2(\theta)}{1 - cos^2(\theta)}
$$

$$

\text{After noticing that} ~ 1 - cos^2(\theta) = sin^2(\theta)
$$

$$

S_{\infty} = \frac{sin^2(\theta)}{sin^2(\theta)} = 1
$$



