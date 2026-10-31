## Sum of a series

As introduced previously, the sum of a series adds up each term in a sequence till the $n^{th}$ term.

Using the general definition of the sum, we obtain

$$

S_{n ~ - ~ 1} = u_1 + u_2 + \cdots + u_{n ~ - ~ 3} + u_{n ~ - ~ 2}
$$

$$

S_n = u_1 + u_2 + \cdots + u_{n ~ - ~ 2} + u_{n ~ - ~ 1}
$$

$$
S_{n ~ + ~ 1} = u_1 + u_2 + \cdots + u_{n ~ - ~ 1} + u_n
$$

<center>Using these basic definitions we can derive two important results </center>

$$

S_n - S_{n ~ - ~1} = u_{n ~ - ~ 1}
$$

$$

S_{n ~ + ~ 1} - S_n = u_{n}
$$

* This can help you determine the common difference or ratio of a sequence

It is also important to note that:

$$

S_1 = a ~~[a ~ \text{denotes the first term of the sequence here}]
$$




### **Sum of a series given in quadratic form**

* Many questions may give you the sum in terms of a quadratic

$$

S_n = An^2 + Bn ~~ [\text{Where A and B are constants}]
$$

* A sum given in this form is **always** an **arithmetic progression**.

One of the methods to solve such questions is using the definitions and results that arise from the sum of a series.

* An alternate way is to **compare the coefficients** with the sum of an arithmetic progression

$$

S_n = \frac{n}{2}[2a + (n - 1)d] = An^2 + Bn
$$

$$

\frac{dn^2}{2}  - \frac{dn}{2} + an = An^2 + Bn
$$


**<center>Upon comparing coefficients, we get:</center>**
$$
\frac{d}{2} = A \implies d = 2A
$$

$$

-\frac{d}{2} + a = B \implies a = B + A
$$

* Where $a$ is the first term of the arithmetic sequence and $d$ is the common difference.




### **Finding sum in-between 2 terms**

* Recall that the formula for the sum of a series gives you the sum **till** the $n^{th}$ term.

To find the sum in-between two terms, say $a$ and $b$ \[where $b > a$\], we can use the fact that $S_b$ includes $S_a$ to some extent.

* To take an **example**, the sum of numbers **between** the $20^{th}$ and $100^{th}$ term for a sequence is given by:

$$

S_{100} = u_1 + u_2 + \cdots + u_{19} + u_{20} + \cdots + u_{99} + u_{100}
$$

$$

S_{19} = u_1 + u_2 + \cdots + u_{18} + u_{19}
$$

<center>We can clearly deduce that</center>

$$

S_{100} - S_{19} = u_{20} + u_{21} + \cdots u_{99} + u_{100}
$$

Another way to think about this is

$$

S_{100} = S_{19} + u_{20} + u_{21} + \cdots + u_{99} + u_{100}
$$

So subtracting $S_{19}$ from $S_{100}$ gives us the sum between the $20^{th}$ and $100^{th}$ term.