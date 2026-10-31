## Solved question 3

Question 3:

Let $u_r = e^{rx}(e^{2x} - 2e^x + 1)$

a) Using the method of differences, or otherwise, find

$$

\sum_{r \ = \ 1}^{n} u_r
$$

in terms of n and x.

**<center>Solution:</center>**

Let’s first begin by expanding $u_r$ to get

$$

u_r = e^{(2 + r)x} - 2e^{(1 + r)x} + e^{rx}
$$

Starting the sum from $r \ = \ 1$ till $n$, we get

$$

e^{(2 \ + \  1)x} - 2e^{(1 \ + \ 1)x} + e^x 
$$

$$
+ \ e^{(2 \ + \ 2)x} - 2e^{(1 \ + \ 2)x} + e^{2x} 
$$

$$

+ \ e^{(2 \ + \ 3)x} - 2e^{(1 \ + \ 3)x} + e^{3x}
$$

$$
+ \ e^{(2 \ + \ n)x} - 2e^{(1 \ + \ n)x} + e^{nx}
$$

$$

+ \ e^{(2 \ + \ (n \ + \ 1))x} - 2e^{(1 \ + \  (n \ + \ 1))x} + e^{(n \ + \ 1)x}
$$

We can now simplify this result

$$

e^{3x} - 2e^{2x} + e^x
$$

$$

+ \ e^{4x} - 2e^{3x} + e^{2x}
$$

$$

+ \ e^{5x} - 2e^{4x} + e^{3x}
$$

$$

+ \ e^{(2 \ + \ n)x} - 2e^{(1 \ + \ n)x} + e^{nx}
$$

$$

+ \ e^{(3 \ + \ n)x} - 2e^{(2 \ + \ n)x} + e^{(n \ + \ 1)x}
$$

Using the method of differences, it is clear that diagonals in this series cancel out

$$

\cancel{e^{3x}} \ - \ \cancel{2}e^{2x} \ + \ e^x
$$

$$

\cancel{\ e^{4x}} \quad \cancel{- \quad 2e^{3x}} \quad \cancel{+ \quad e^{2x}}
$$

$$

\cancel{e^{5x}} \quad \cancel{- \quad 2e^{4x}} \quad \cancel{+ \quad e^{3x}}
$$

$$

\cancel{e^{(2 \ + \ n)x}} \quad \cancel{- \quad 2e^{(1 \ + \ n)x}} \quad \cancel{+ \quad e^{nx}}
$$

$$

e^{(3 \ + \ n)x} \ - \ \cancel{2}e^{(2 \ + \ n)x} \quad \cancel{+ \quad e^{(n \ + \ 1)x}}
$$

**<center>So part a)’s answer is:</center>**

$$

\sum_{r \ = \ 1}^{n} u_r = e^x - e^{2x} - e^{(2 \ + \ n)x} + e^{(3 \ + \ n)x}
$$


---

bi) Deduce the set of non-zero values of $x$ for which the infinite series

$$

u_1 + u_2 + u_3 \cdots
$$

is convergent and bii) give the sum to infinity when this exists.

**<center>Solution:</center>**

We must first find the common ratio of this series, by using:

$$

\frac{{u_{r \ + \ 1}}}{u_r}
$$

For our series:

$$

\frac{e^{(r \ + \ 1)x}\cancel{(e^{2x} - 2e^x + 1)}}{e^{rx}\cancel{(e^{2x} - 2e^x + 1)}}
$$

$$

 \frac{e^{rx}e^x}{e^{rx}}
$$

$$

\implies \ r \ = \frac{\cancel{e^{rx}}e^x}{\cancel{e^{rx}}} = e^x
$$

We now must find the values of $x$ such that

$$

-1 < r < 1
$$

$$

-1 < e^x < 1
$$

Now we take the natural log of both sides of the inequality to get

$$

ln(e^x) < ln(1) 
$$

$$

x < 0
$$

**<center>So the only values for which this series will converge is**</center>

$$

x < 0
$$

bii) To find the sum to infinity, we first write

$$

\lim_{N \rightarrow \infty} \quad \sum_{r \ = \ 1}^{N} e^x - e^{2x} - e^{(2 \ + \ n)x} + e^{(3 \ + \ n)x}
$$

As we need $x < 0$ for the series to converge, the terms $-e^{(2 \ + \ n)x} + e^{(3 \ + \ n)x}$ will become smaller and smaller as $N \rightarrow \infty$. This means the two terms will be negligible to our sum.

**<center>Thus our final answer for bii) is**</center>

$$
\sum_{r \ = \ 1}^{\infty} u_r = e^x - e^{2x}
$$



