## Solved question 2

<span class="underline">Question 2:</span>

a)  Given that

$$

{f}\left( {r} \right){~ = ~}\frac{{1}}{\left( {r + 1} \right)\left( {r + 2} \right)}
$$

show that

$$
{f}\left( {r - 1} \right){~ - ~ f}\left( {r} \right){~ = ~}\frac{{2}}{{r}\left( {r + 1} \right)\left( {r + 2} \right)}
$$

**<center>Solution:</center>**

a) Using the values of $f(r - 1)$ and $f(r)$, we get

$$

f(r - 1) - f(r) = \frac{{1}}{{r}\left( {r + 1} \right)}{~ - ~}\frac{{1}}{\left( {r + 1} \right)\left( {r + 2} \right)}
$$

This simplifies to

$$

\frac{{2}}{{r}\left( {r + 1} \right)\left( {r + 2} \right)}
$$


---

b)  **Hence** find

$$
\sum_{{r ~ = ~ 1}}^{{n}}\frac{{1}}{{r}\left( {r + 1} \right)\left( {r + 2} \right)}
$$

**<center>Solution:</center>**

Using our answer from part $a)$, we can re-write the summation using partial fractions as

$$

\sum_{r ~ = ~ 1}^{n} \frac{1}{r(r + 1)(r + 2)} \implies \frac{1}{2} \sum_{r ~ = ~ 1}^{n} \frac{1}{r(r + 1)} - \frac{1}{(r + 1)(r + 2)}
$$

We can now use the **method of differences** to simplify the summation as such

$$

\frac{1}{2} \left(\frac{1}{2} - \frac{1}{6} + \frac{1}{6} - \frac{1}{12} + \frac{1}{12} - \frac{1}{20} + \cdots + \frac{1}{(n - 1)n} - \frac{1}{n(n + 1)} + \frac{1}{n(n + 1)} - \frac{1}{(n + 1)(n + 2)} \right)
$$

It is clear that the consecutive terms in the series cancel out

$$

\frac{1}{2} \left(\frac{1}{2} \cancel{~ - ~ \frac{1}{6} + \frac{1}{6}} \cancel{~ - ~ \frac{1}{12} + \frac{1}{12}} \cancel{~ - ~ \frac{1}{20}} + \cdots \cancel{+ ~ \frac{1}{(n - 1)n}} \cancel{~ - ~ \frac{1}{n(n + 1)} ~ + ~ \frac{1}{n(n + 1)}} - \frac{1}{(n + 1)(n + 2)} \right)
$$

<center>Thus our final answer to b) is </center>

$$

\sum_{r ~ = ~ 1}^{n} \frac{1}{r(r + 1)(r + 2)} = \frac{1}{2} \left(\frac{1}{2} - \frac{1}{(n + 1)(n + 2)} \right)
$$


---

c)  Deduce the value of

$$
\sum_{{r ~ = ~ 1}}^{{\infty}}\frac{{1}}{{r}\left( {r + 1} \right)\left( {r + 2} \right)}
$$

**<center>Solution:</center>**

To find the value that the summation converges to when it goes to infinity, take the limit till infinity for the upper bound

$$
\lim_{n \rightarrow \infty} \sum_{r ~ = ~ 1}^{n} \frac{1}{r(r + 1)(r + 2)}  = \lim_{n \rightarrow \infty} \left( \frac{1}{4} - \frac{1}{2(n + 1)(n + 2)} \right)
$$

As $n$ approaches infinity, the fraction will become a small value that is negligible.

<center>Thus our final answer to c) is </center>

$$
\lim_{n \rightarrow \infty} \sum_{r ~ = ~1}^{n} \frac{1}{r(r + 1)(r + 2)} = \frac{{1}}{{4}}{\quad}
$$



