## Arithmetic Progression

* An arithmetic progression (AP) is a series of numbers that share a common difference between consecutive terms
  * An example of an arithmetic progression is: $2, 4, 6, 8, \cdots$. Each consecutive term in this series has a common difference of $2$.
  * The first term is denoted by $a$ and the common difference is denoted by $d$

$$

\text{1}^{st} ~~ \text{term} = u_1 = a
$$

$$

\text{2}^{nd} ~~ \text{term} = u_2 = a + d
$$

$$

3^{rd} ~~ \text{term} = u_3 = a + 2d
$$

$$

\cdots
$$

$$

(n - 1)^{th} ~~ \text{term} = u_{n ~ - ~ 1} = a + (n - 2)d
$$

$$

n^{th} ~~ \text{term} = u_n = a + (n - 1)d
$$

$$

(n + 1)^{th} ~~ \text{term} = u_{n ~ + ~ 1} =  a + (n + 1)d
$$

* The formula for the $n^{th}$ term is also given in the MF19 formula sheet.




### **Finding the common difference**

As mentioned previously, the common ratio must be the same between consecutive terms.

This can be written as

$$
d = u_2 - u_1 = u_3 - u_2 = \cdots = u_n - u_{n ~ - ~ 1} = u_{n ~ + ~ 1} - u_n
$$

<center>We can re-write this as</center>

$$

d = a + d - a = a + 2d - (a + d) 
$$

$$

\cdots
$$

$$

d = a + (n - 1)d - [a + (n - 2)d] = a + (n + 1)d - [a + (n - 1)d]
$$

* Note that the difference of two consecutive terms results in $d$ being the only term left.




### **Sum of Arithmetic Progression**

* The sum of a geometric progression is the sum of terms in a given sequence.
  * $S_n$ denotes the sum till the $n^{th}$ term.

It is given in MF19, and is denoted by

$$

S_n = \frac{n}{2}\left[2a + (n - 1)d\right]
$$

<center>An alternate formula also exists</center>

$$

S_n = \frac{n}{2}(a + l)
$$

Where $l$ denotes the last term in the series

* The use of both formulae depends on the context, and information about the variables.


---

**<center> Example 1</center>**

Find the $120^{th}$ term of the arithmetic progression: $2, 4, 6, 8, 10…$

**<center> Answer </center>**

* From the question
  * The first term is equal to $a$, which is $2$ in this question.
  * The common difference, $d$, is equal to the difference between consecutive terms, $4 - 2 = 2$.

So to find the $120^{th}$ term

$$

u_{120} = 2 +(120-1)2 = 240
$$

$$
\phantom{invis}
$$

**<center> Example 2 </center>**

Find the sum of the first 20 terms of the arithmetic progression, which has its first term equal to 7 and its $8^{th}$ term being 28.

**<center> Answer </center>**

From the question, we can deduce that $a = 7$ as it is the first term. Using the general formula for the $n^{th}$ term for an AP

$$
u_{8} = 28 = 7 +(8-1)d
$$

$$
d = \frac{28-7}{7} = 3
$$

Thus, we can use the sum till the $n^{th}$ to find the sum of the first 20 terms.

$$

S_{20} = \frac{20}{2}[2(7)+(20-1)3] = 710
$$



