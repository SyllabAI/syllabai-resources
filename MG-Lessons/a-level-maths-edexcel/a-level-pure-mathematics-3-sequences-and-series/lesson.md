# a-level-pure-mathematics-3-sequences-and-series — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Sequences, series and spotting the pattern

![Comparison diagram of arithmetic sequence 4, 7, 10, 13 with +3 arrows and geometric sequence 3, 6, 12, 24 with x2 arrows, with nth-term and sum formulas labelled](../assets/001-18a162df-a74b-49a3-9b0d-fdc7d1fcbc62.jpeg)
A sequence is an ordered list of terms, while a series is what you get when you add those terms. The notation $u_n$ means the nth term, and $\sum$ means "add up".

Sigma notation tells you exactly where to start and stop. For example,
$$\sum_{r=4}^{6}(5r-1)=19+24+29,$$
so the first term comes from $r=4$, not $r=1$.

Arithmetic sequences have a constant difference, while geometric sequences have a constant ratio. That one idea tells you which formula family to use.

## Arithmetic sequences

In an arithmetic sequence you add the same number each time. If the first term is $a$ and the common difference is $d$, then the $n$-th term is given by: $$u_n=a+(n-1)d.$$

In the sequence $6, 10, 14, 18, \dots$, we have $a=6$ and $d=4$. To find the 20th term, we apply the formula: $$u_{20}=6+19\cdot4=82.$$

Use $u_n$ when the question asks for one specific term, such as "the value in week 20". Do not use a sum formula unless the question asks for a total sum of multiple terms.

## Arithmetic series worked example

For arithmetic sums use $$S_n=\frac{n}{2}(2a+(n-1)d).$$ This formula is for calculating totals, while $u_n=a+(n-1)d$ is used for finding single terms.

Suppose $u_3=-2$ and $S_8=44$. The third term gives $a+2d=-2$, and applying the sum formula for the eighth term gives: $$44=\frac{8}{2}(2a+7d),\quad 2a+7d=11.$$

Solve the simultaneous equations by doubling $a+2d=-2$ to get $2a+4d=-4$. Subtracting this from $2a+7d=11$ gives $3d=15$, so $d=5$ and then $a=-12$.

Now write the sum formula: $$S_n=\frac{n}{2}(2(-12)+(n-1)5)=\frac{n}{2}(5n-29).$$ To find the greatest $n$ with $S_n<250$, check the boundary values $S_{13}=234$ and $S_{14}=287$, meaning the greatest value is $13$.

## Geometric sequences and finite sums

In a geometric sequence you multiply by the same factor each time. If the first term is $a$ and the common ratio is $r$, the general term $u_n$ and the finite sum $S_n$ are given by:

$$$u_n=ar^{n-1},\qquad S_n=\frac{a(1-r^n)}{1-r}\quad (r\ne1).$$

Suppose $u_5=18$ and $u_8=144$. By substituting these into the term formula, we get $ar^4=18$ and $ar^7=144$; dividing these two equations gives $r^3=8$, so $r=2$.

Substitute back to find the first term $a=\frac{18}{2^4}=\frac{9}{8}$. We then use the sum formula to find the value of $S_{12}$: $$S_{12}=\frac{\frac{9}{8}(1-2^{12})}{1-2}=\frac{36855}{8}\approx4607.$$

## Sum to infinity and percentage change

A geometric series has a sum to infinity only when $|r|<1$, because the terms must shrink towards 0. In that case, we use the formula:
$$S_\infty=\frac{a}{1-r}.$$

For example, if $a=12$ and $r=\frac{3}{4}$, then $S_\infty=\frac{12}{1-\frac{3}{4}}=48$. If $r=1.04$ or $r=-1.2$, there is no finite sum to infinity because the terms do not settle to 0.

Smallest $n$ questions use the finite sum formula with the same ratio. For $a=9$ and $r=\frac{2}{3}$, the sum of the first $n$ terms is represented as:
$$S_n=\frac{9\left(1-\left(\frac{2}{3}\right)^n\right)}{1-\frac{2}{3}}=27\left(1-\left(\frac{2}{3}\right)^n\right).$$

## Recurrence relations, periodic sequences and telescoping sums

A recurrence relation defines each term using earlier terms. If $x_1=3$ and $x_{n+1}=bx_n-4$, then $x_2=3b-4$ and $x_3=b(3b-4)-4=3b^2-4b-4$.

A periodic sequence repeats after a fixed number of terms. For $u_1=\frac{3}{5}$ and $u_{n+1}=\frac{1}{u_n}$, the terms alternate $\frac{3}{5}, \frac{5}{3}, \frac{3}{5}, \frac{5}{3}, \dots$, so the period is 2.

Telescoping sums collapse because middle terms cancel. For example, $$\sum_{r=1}^{15}\log_2\left(\frac{r+1}{r}\right)=\log_2\left(\frac{2}{1}\cdot\frac{3}{2}\cdots\frac{16}{15}\right)=\log_2(16)=4.$$

## Check yourself

1. In $\sum_{r=4}^{18}(5r-1)$, what is the first term?

   - 19 ✔

   - 4

   - 24

   - 89

   _Explanation:_ Substitute the lower limit $r=4$ into $5r-1$, giving $5(4)-1=19$. The common wrong answer 24 uses $r=5$, which gives the second term, not the first.

2. An arithmetic series has first term 500 and sixth term 250. What is the greatest possible value of $S_n$?

   - 2500

   - 2750 ✔

   - 3000

   - 3250

   _Explanation:_ Since $500+5d=250$, the common difference is $d=-50$. The terms stay positive up to $u_{10}=50$ and $u_{11}=0$, so the maximum total is $S_{10}$ or $S_{11}$, both equal to 2750. The common wrong answer 2500 comes from treating 0 as the last positive term and missing the extra 50.

3. For the geometric series with $a=9$ and $r=\frac{2}{3}$, what is the smallest $n$ such that $S_n>26$?

   - 8

   - 9 ✔

   - 10

   - 11

   _Explanation:_ Use $S_n=27\left(1-\left(\frac{2}{3}\right)^n\right)>26$, so $\left(\frac{2}{3}\right)^n<\frac{1}{27}$. Since $\left(\frac{2}{3}\right)^8\approx0.039$ is still larger than $\frac{1}{27}\approx0.037$, but $\left(\frac{2}{3}\right)^9\approx0.026$ is smaller, the first working value is 9. The common wrong answer 8 comes from rounding a calculator result like 8.13 down instead of up. Hint: Rearrange to isolate $\left(\frac{2}{3}\right)^n$.

4. A sequence is defined by $u_1=\frac{3}{5}$ and $u_{n+1}=\frac{1}{u_n}$. What is $\sum_{r=1}^{100}u_r$?

   - $$\frac{34}{15}$

   - $$\frac{170}{3}$

   - $$\frac{340}{3}$ ✔

   - $$\frac{680}{3}$

   _Explanation:_ The terms alternate $\frac{3}{5}, \frac{5}{3}, \frac{3}{5}, \frac{5}{3}, \dots$, so the period is 2. Each pair sums to $\frac{3}{5} + \frac{5}{3} = \frac{34}{15}$. Since there are 100 terms, there are 50 such pairs. The total sum is $50 \cdot \frac{34}{15} = \frac{10 \cdot 34}{3} = \frac{340}{3}$.
