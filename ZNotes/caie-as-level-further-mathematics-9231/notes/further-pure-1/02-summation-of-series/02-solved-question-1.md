## Solved question 1

**Question 1**

a) Use the relevant **standard results** in the List of Formulae to prove that

$$
{S}_{{N}} ~ {=}\sum_{n ~ = ~ 1}^{N} {(8}{n}^{{3}}{~ - ~ 6}{n}^{{2}}{)}{~ = N(N + 1)(2}{N}^{{2}}{- 1)}
$$

**<center>Solution:</center>**

Split both summations

$$
\sum_{{n ~ = ~ 1}}^{{N}}{{(8}{n}^{{3}}{- 6}{n}^{{2}}{)}}{~ = 8}\sum_{{n ~ = ~ 1}}^{{N}}{n}^{{3}}{~ - ~ 6}\sum_{{n ~ = ~ 1}}^{{N}}{n}^{{2}}
$$

Using the standard results of summations

$$
8 \left(\frac{N^2(N + 1)^2}{4} \right) ~ - ~ 6 \left(\frac{N(N + 1)(2N + 1)}{6} \right)
$$

$$
{ 2}{N}^{{2}}\left( {N + 1} \right)^{{2}}{~ - ~ N}\left( {N + 1} \right)\left( {2}{N + 1} \right)
$$

After we take $N(N + 1)$ as a common factor

$$
{N}\left( {N + 1} \right)\left[ {2}{N}\left( {N + 1} \right){-}\left( {2}{N + 1} \right) \right]
$$

**<center>So the answer for a) is</center>**

$$
S_{N} = { N(N + 1)(2}{N}^{{2}}{- 1)} 
$$


---

**b) Hence** show that

$$
\sum_{{n ~ = ~ N ~ + ~ 1}}^{{2}{N}}{{(8}{n}^{{3}}{~ - ~ 6}{n}^{{2}}{)}}
$$

Can be expressed in the form

$$
{N}\left( {a}{N}^{{3}}{+ b}{N}^{{2}}{+ cN + d} \right)
$$

Where the constants ${a,\ b,\ c,\ d}$ are to be determined.

**<center>Solution:</center>**

Using the property

$$

\sum_{n = N + 1}^{2N} f(n) = \sum_{n = 0}^{2N} f(n) - \sum_{n = 0}^{N + 1 - 1} f(n)
$$

$$

\sum_{{n ~ = ~ 1}}^{{2}{N}}\left( {8}{n}^{{3}}{~ - 6}{n}^{{2}} \right){~ -}\sum_{{n ~ = ~ 1}}^{{N  +  1  -  1}}\left( {8}{n}^{{3}}{~ - 6}{n}^{{2}} \right)
$$

Using our answer from $a)$, we simplify the summation to

$$

 {2}{N}\left( {2}{N + 1} \right)\left( {8}{N}^{{2}}{~ - 1} \right){~ - ~ N}\left( {N + 1} \right)\left( {2}{N}^{{2}}{~ - 1} \right)
$$

After taking $N$ as a common factor

$$

 {N}\left[ \left( {4}{N + 2} \right)\left( {{8}{N}}^{{2}}{- 1} \right){-}\left( {N + 1} \right)\left( {2}{N}^{{2}}{- 1} \right) \right]
$$

**<center>After expanding and simplifying, the solution of b) is</center>**

$$

{ N}\left( {30}{N}^{{3}}{~ + ~ 14}{N}^{{2}}{~ - ~ 3}{N ~ - ~ 1} \right)
$$



