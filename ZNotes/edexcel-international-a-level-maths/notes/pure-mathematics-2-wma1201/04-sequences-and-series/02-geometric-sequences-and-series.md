## Geometric Sequences

* Geometric sequences can be written in the form of:

$$
a, ar, ar^2, ar^3 ....
$$

They can be simplified and written in the standard form of:

$$
ar^{n-1}
$$

* This is where:

  
  1. a = first term
  2. r = the common ratio
  3. n = the nth term

→ the common ratio can be found as $\frac{t_2}{t_1} \ or \ \frac{t_3}{t_2} \ or \  \frac{t_4}{t_3} …$

## Geometric Series

The standard formula of a geometric series is:

$$
\frac{a[1-r^n]}{1-r}
$$

→ The proof of this series can be shown as:


1. Let equation 1 be: $ a \ + \ ar \ + \ ar^2 \ + \ … \ + \ ar^{n-2} \ + \ ar^{n-1}$
2. Let equation 2 be: $ar \ + \ ar^2 \ + \ ar^3 \ + \ … \ + \ ar^{n-1} \ + \ ar^n$

   (Multiply equation 1 by r)
3. Subtract equation 2 from 1 giving: $S_n - r(S_n) = a - ar^n$
4. Factorize both sides to get $S_n [1-r] = a[1-r^n]$
5. Therefore $S_n = \frac{a(1-r^n)}{1-r}$

→**Note:**


1. A geometric series only converges if |r| is -1 < r < 1
2. If a, b, and c are 3 consecutive terms in a geometric sequence $\frac{b}{a} = \frac{c}{b}$


---

Example Question:

* Find the least value of n in the geometric series: 3 + 6 + 12 + 24 … n that exceeds 1.5 million


---

Solution:


1. We can find a=3 and r = 2
2. Therefore $S_n>1.5 \, \text{million}$
3. $\frac{a[1-r^n]}{1-r} > 1,500,000$
4. $\frac{3(1-2^n)}{1-2} > 1,500,000$
5. This simplifies to $3[2^n -1] >150,000$
6. $2^n -1 > 500,000$
7. Take logs of both sides to solve for n to get n > 19 finally



