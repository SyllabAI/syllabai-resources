# Mark Schemes — Binomial & Geometric Distribution
**Statistical Distributions** · Cambridge (CIE) AS maths (9709)


## Exam Questions (33 questions)


### Q1
The people are independent, each with the same probability 0.05 of stopping, so $X$, the number of people who walk past up to and including the first person to stop, follows a geometric distribution

`X \sim \text{Geo}(0.05)`

Use $\text{E} ( X ) = \frac{1}{p}$

$\text{E} ( X ) = \frac{1}{0.05} = 20$

$X$ includes the person who stops, so subtract 1 for the number who walk past without stopping

$20 - 1 = 19$

**[B1]**

> **[mark-scheme]**
> **B1**: 19.
(i)

Each of the first 20 people does not stop, with probability 0.95 each

`\text{P}(X > 20) = \left(0.95\right)^{20} = 0.358485\ldots`

**Final answer:** $\text{P} ( X > 20 ) = 0 . 358$** (3 s.f.)**

**[B1]**

(ii)

The only way to fail is for none of the first 100 people to stop, so subtract that from 1

`\text{P}(X \leq 100) = 1 - \left(0.95\right)^{100}`

**[M1]**

$\text{P} ( X \leq 100 ) = 1 - 0 . 00592052 \dots = 0 . 994079 \dots$

**Final answer:** $\text{P} ( X \leq 100 ) = 0 . 994$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: 0.358, or answers which round to 0.358.
> 
> **M1**: `1 - \left(0.95\right)^{100}`. Accept `1 - \left(0.95\right)^{99}` or `1 - \left(0.95\right)^{101}` for this mark only.
> 
> **A1**: 0.994, or answers which round to 0.994.
The first 20 people are known not to have stopped, and each person decides independently, so at least one of people 21 to 100 must stop. That is 80 people

`\text{P}(\text{at least one of the next 80 stops}) = 1 - \left(0.95\right)^{80}`

**[M1]**

`1 - \left(0.95\right)^{80} = 1 - 0.0165153\ldots = 0.983484\ldots`

**Final answer:** $\text{Probability} = 0 . 983$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `1 - \left(0.95\right)^{80}`, or the conditional-probability ratio `\dfrac{\left(0.95\right)^{20} - \left(0.95\right)^{100}}{\left(0.95\right)^{20}}`.
> 
> **A1**: 0.983, or answers which round to 0.983.
People 1 to 9 do not stop, person 10 stops, people 11 to 19 do not stop and person 20 stops. These 20 outcomes are independent, so multiply

`\text{P} = \left(0.95\right)^{9}(0.05) \times \left(0.95\right)^{9}(0.05) = \left(0.95\right)^{18}\left(0.05\right)^{2}`

**[M1]**

$\text{P} = 0 . 000993035 \dots$

**Final answer:** $\text{P} = 0 . 000993$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `\left(0.95\right)^{18}\left(0.05\right)^{2}`, or the product of two terms `\left(0.95\right)^{9}(0.05)`.
> 
> **A1**: 0.000993, or answers which round to 0.000993. Accept 9.93 × 10⁻⁴.
For $n$ people, at least one stops unless none of them does

`1 - \left(0.95\right)^{n} \geq 0.999`

**[M1]**

Rearrange

`\left(0.95\right)^{n} \leq 0.001`

Take logarithms of both sides. $\text{ln}  0 . 95$ is negative, so dividing by it reverses the inequality

$n  \text{ln}  0 . 95 \leq \text{ln}  0 . 001$

$n \geq \frac{\text{ln}0.001}{\text{ln}0.95} = 134 . 67 \dots$

**[M1]**

$n$ must be a whole number

$n = 135$

**[A1]**

> **[mark-scheme]**
> **M1**: `1 - \left(0.95\right)^{n} \geq 0.999`, or `\left(0.95\right)^{n} \leq 0.001`. Allow "=" throughout.
> 
> **M1**: Taking logarithms of both sides, or evaluating `1 - \left(0.95\right)^{n}` for both n = 134 (0.99896…) and n = 135 (0.99902…).
> 
> **A1**: n = 135 only, as a single integer.

### Q2
(i)

Each person needs at least one throw, so list the ways to split a total of 4 throws as (Anand, Beatrix)

*(1, 3), (2, 2) or (3, 1)*

**[M1]**

Use `\text{P}(\text{first hit on throw } r) = p\left(1 - p\right)^{r - 1}` for each person and multiply, since they are independent

`(1, \; 3): \; p \times p\left(1 - p\right)^{2} = p^{2}\left(1 - p\right)^{2}`

`(2, \; 2): \; p(1 - p) \times p(1 - p) = p^{2}\left(1 - p\right)^{2}`

`(3, \; 1): \; p\left(1 - p\right)^{2} \times p = p^{2}\left(1 - p\right)^{2}`

**[M1]**

Add the three cases

`\text{P}(\text{total of 4 throws}) = 3p^{2}\left(1 - p\right)^{2}`

$k = 3$

**[A1]**

(ii)

Set the result from (i) equal to 0.1875

`3p^{2}\left(1 - p\right)^{2} = 0.1875`

Divide by 3

`\left[p(1 - p)\right]^{2} = 0.0625`

**[M1]**

Take the square root. $p$ and $1 - p$ are both probabilities, so $p ( 1 - p )$ cannot be negative

$p ( 1 - p ) = 0 . 25$

Rearrange and factorise

$p^{2} - p + 0 . 25 = 0$

`\left(p - 0.5\right)^{2} = 0`

$p = 0 . 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Identifying the three cases (1, 3), (2, 2) and (3, 1), and no others.
> 
> **M1**: A correct product of two geometric probabilities for at least one case, e.g. `p \times p\left(1 - p\right)^{2}`.
> 
> **A1**: `3p^{2}\left(1 - p\right)^{2}` with k = 3 stated. All three cases must be shown, as the form is given.
> 
> **M1**: `3p^{2}\left(1 - p\right)^{2} = 0.1875`, simplified to an equation in $p ( 1 - p )$, or expanded to a quartic.
> 
> **A1**: p = 0.5 only. A negative value of $p ( 1 - p )$ must be rejected, or not given.
The $n$ games are independent, each with the same probability 0.2 of a win, so $Y$ follows a binomial distribution

`Y \sim \text{B}(n, \; 0.2)`

Chen wins at least one game unless he loses all $n$, each with probability 0.8

`\text{P}(Y \geq 1) = 1 - \left(0.8\right)^{n} < 0.9`

**[M1]**

Rearrange

`\left(0.8\right)^{n} > 0.1`

Take logarithms of both sides. $\text{ln}  0 . 8$ is negative, so dividing by it reverses the inequality

$n  \text{ln}  0 . 8 > \text{ln}  0 . 1$

$n < \frac{\text{ln}0.1}{\text{ln}0.8} = 10 . 318 \dots$

**[M1]**

$n$ must be a whole number

$n = 10$

**[A1]**

> **[mark-scheme]**
> **M1**: `1 - \left(0.8\right)^{n} < 0.9`, or `\left(0.8\right)^{n} > 0.1`. Allow "=" throughout.
> 
> **M1**: Taking logarithms of both sides, or evaluating `1 - \left(0.8\right)^{n}` for both n = 10 (0.8926…) and n = 11 (0.9141…).
> 
> **A1**: n = 10 only, as a single integer.

### Q3
A binomial model needs a constant probability of success and independent trials

**Final answer:** **The probability that a female mosquito carries the parasite is 0.8 for every female mosquito in the sample**

**[B1]**

**Final answer:** **Whether one female mosquito carries the parasite is independent of whether any other one does**

**[B1]**

> **[mark-scheme]**
> **B1**: The probability of a female mosquito carrying the parasite is constant (0.8), in context.
> 
> **B1**: Female mosquitoes carry the parasite independently of each other, in context.
> 
> The two assumptions are marked independently. "A fixed number of trials" or "two outcomes" do not score.
A mosquito can transmit the parasite only if it is female and carries the parasite

`\text{P}(\text{can transmit}) = \text{P}(\text{female}) \times \text{P}(\text{carries parasite} \mid \text{female}) = 0.5 \times 0.8`

**[M1]**

$\text{P} ( \text{can transmit} ) = 0 . 4$

**[A1]**

Subtract from 1 for the probability that one mosquito cannot transmit

$\text{P} ( \text{cannot transmit} ) = 1 - 0 . 4 = 0 . 6 = \frac{3}{5}$

**[M1]**

The six mosquitoes are independent, so the number that can transmit has distribution $\text{B} ( 6 ,  0 . 4 )$, and none can transmit with probability

`\text{P}(\text{none of the six can transmit}) = \left(\dfrac{3}{5}\right)^{6}`

**[M1]**

$\text{P} ( \text{none of the six can transmit} ) = \frac{729}{15625}$

**[A1]**

> **[mark-scheme]**
> **M1**: P(can transmit) = 0.5 × 0.8.
> 
> **A1**: 0.4.
> 
> **M1**: P(cannot transmit) = 0.6, or 0.5 + 0.5 × 0.2.
> 
> **M1**: `\left(0.6\right)^{6}`, using your value for one mosquito.
> 
> **A1**: $\frac{729}{15625}$, or the exact decimal 0.046656.
> 
> Alternative method: summing, over the number of females n = 0 to 6, the probability of n females with none of them carrying the parasite, `{}^{6}C_{n}\left(0.5\right)^{6}\left(0.2\right)^{n}`, scores full marks if all seven terms are present and correctly evaluated.

### Q4
(i)

Of the 36 equally likely outcomes, six give a sum of 7 and two give a sum of 11

$\text{P} ( \text{sum is 7 or 11} ) = \frac{6+2}{36} = \frac{8}{36}$

Subtract from 1 to find the probability that the sum is not 7 or 11

$p = 1 - \frac{8}{36} = \frac{28}{36} = \frac{7}{9}$

`X \sim \text{B}\left(18, \; \dfrac{7}{9}\right)`

**[B1]**

(ii)

A binomial model needs a constant probability of success and independent trials

**Final answer:** **The probability that the sum is not 7 or 11 is the same each time the dice are rolled**

**[B1]**

**Final answer:** **The result of each roll of the two dice is independent of the results of the other rolls**

**[B1]**

> **[mark-scheme]**
> **B1**: B(18, 7/9), or "binomial with n = 18 and p = 7/9". Accept p = 0.778.
> 
> **B1**: The probability is constant for each roll of the two dice, in context.
> 
> **B1**: The rolls are independent of each other, in context.
> 
> The two assumptions are marked independently. "A fixed number of trials" or "two outcomes" are already given in the question, so they do not score.
Use `\text{P}(X = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $n = 18$, $p = \frac{7}{9}$ and $r = 14$

`\text{P}(X = 14) = {}^{18}C_{14}\left(\dfrac{7}{9}\right)^{14}\left(\dfrac{2}{9}\right)^{4}`

**[M1]**

$\text{P} ( X = 14 ) = 0 . 221232 \dots$

**Final answer:** $\text{P} ( X = 14 ) = 0 . 221$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `{}^{18}C_{14}\,p^{14}\left(1 - p\right)^{4}` with your value of p from (a), or 3060 × (7/9)¹⁴ × (2/9)⁴.
> 
> **A1**: 0.221, or answers which round to 0.221.

### Q5
The primes on the die are 2, 3 and 5, and the squares are 1 and 4. That leaves only the 6, so subtract from 1

$\text{P} ( 6 ) = 1 - \frac{1}{2} - \frac{5}{16} = \frac{3}{16}$

**[M1]**

The rolls are independent, each with the same probability $\frac{3}{16}$ of a 6, so the number of rolls up to and including the first 6 is `X \sim \text{Geo}\left(\dfrac{3}{16}\right)`. Use $\text{E} ( X ) = \frac{1}{p}$

$\text{E} ( X ) = \frac{1}{\frac{3}{16}}$

$\text{E} ( X ) = \frac{16}{3}$

**[A1]**

> **[mark-scheme]**
> **M1**: P(6) = 1 − 1/2 − 5/16 = 3/16.
> 
> **A1**: $\frac{16}{3}$, or answers which round to 5.33. Not 1/(3/16) left unevaluated.
(i)

The 20 rolls are independent, each with the same probability $\frac{3}{16}$ of a 6, so $Y$, the number of 6s, follows a binomial distribution

`Y \sim \text{B}\left(20, \; \dfrac{3}{16}\right)`

Use `\text{P}(Y = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 4$

`\text{P}(Y = 4) = {}^{20}C_{4}\left(\dfrac{3}{16}\right)^{4}\left(\dfrac{13}{16}\right)^{16}`

**[M1]**

$\text{P} ( Y = 4 ) = 0 . 216009 \dots$

**Final answer:** $\text{P} ( Y = 4 ) = 0 . 216$** (3 s.f.)**

**[A1]**

(ii)

All four 6s are in the first $k$ rolls, and none of the remaining $20 - k$ rolls is a 6

$\text{P} = \text{P} ( \text{four 6s in the first} k \text{rolls} ) \times \text{P} ( \text{no 6s in the last} 20 - k \text{rolls} )$

**[M1]**

The first factor is a binomial term with $n = k$

`\text{P} = {}^{k}C_{4}\left(\dfrac{3}{16}\right)^{4}\left(\dfrac{13}{16}\right)^{k - 4} \times \left(\dfrac{13}{16}\right)^{20 - k}`

**[M1]**

Add the powers of $\frac{13}{16}$, since $( k - 4 ) + ( 20 - k ) = 16$

`\text{P} = {}^{k}C_{4}\left(\dfrac{3}{16}\right)^{4}\left(\dfrac{13}{16}\right)^{16}`

**[A1 A1]**

> **[mark-scheme]**
> **M1**: `{}^{20}C_{4}\left(\dfrac{3}{16}\right)^{4}\left(\dfrac{13}{16}\right)^{16}`, using your p from (a).
> 
> **A1**: 0.216, or answers which round to 0.216.
> 
> **M1**: Recognising four 6s in the first k rolls and no 6s in the remaining 20 − k rolls.
> 
> **M1**: `{}^{k}C_{4}\,p^{4}\left(1 - p\right)^{k - 4} \times \left(1 - p\right)^{20 - k}`, unsimplified.
> 
> **A1**: The powers of $\frac{13}{16}$ combined correctly to 16.
> 
> **A1**: `{}^{k}C_{4}\left(\dfrac{3}{16}\right)^{4}\left(\dfrac{13}{16}\right)^{16}`, fully correct. Accept the equivalent `\dfrac{{}^{k}C_{4}}{{}^{20}C_{4}}` × the answer to (i).

### Q6
(i)

The 10 routines are independent, each with the same probability 0.2 of a mistake, so $X$ follows a binomial distribution

`X \sim \text{B}(10, \; 0.2)`

Use $\text{E} ( X ) = n p$

$\text{E} ( X ) = 10 \times 0 . 2$

$\text{E} ( X ) = 2$

**[B1]**

(ii)

Use $\text{Var} ( X ) = n p ( 1 - p )$, then take the square root

$\text{Var} ( X ) = 10 \times 0 . 2 \times 0 . 8 = 1 . 6$

**[M1]**

$\text{standard deviation} = \sqrt{1.6} = 1 . 26491 \dots$

**Final answer:** $\text{standard deviation} = 1 . 26$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: E(X) = 2.
> 
> **M1**: Var(X) = 10 × 0.2 × 0.8 = 1.6, seen or implied.
> 
> **A1**: 1.26, or answers which round to 1.26. Accept $\sqrt{1.6}$.
(i)

None means no mistake in all 10 routines, each with probability 0.8

`\text{P}(X = 0) = \left(0.8\right)^{10}`

**[M1]**

$\text{P} ( X = 0 ) = 0 . 107374 \dots$

**Final answer:** $\text{P} ( X = 0 ) = 0 . 107$** (3 s.f.)**

**[A1]**

(ii)

Use `\text{P}(X = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 2$

`\text{P}(X = 2) = {}^{10}C_{2}\left(0.2\right)^{2}\left(0.8\right)^{8}`

**[M1]**

$\text{P} ( X = 2 ) = 0 . 301989 \dots$

**Final answer:** $\text{P} ( X = 2 ) = 0 . 302$** (3 s.f.)**

**[A1]**

(iii)

No more than two means $X = 0$, 1 or 2, so add those three terms

`\text{P}(X \leq 2) = \left(0.8\right)^{10} + {}^{10}C_{1}(0.2)\left(0.8\right)^{9} + {}^{10}C_{2}\left(0.2\right)^{2}\left(0.8\right)^{8}`

**[M1]**

$\text{P} ( X \leq 2 ) = 0 . 107374 \dots + 0 . 268435 \dots + 0 . 301989 \dots = 0 . 677799 \dots$

**Final answer:** $\text{P} ( X \leq 2 ) = 0 . 678$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `\left(0.8\right)^{10}`.
> 
> **A1**: 0.107, or answers which round to 0.107.
> 
> **M1**: `{}^{10}C_{2}\left(0.2\right)^{2}\left(0.8\right)^{8}`.
> 
> **A1**: 0.302, or answers which round to 0.302.
> 
> **M1**: P(0) + P(1) + P(2), with all three terms correct. Accept unsimplified.
> 
> **A1**: 0.678, or answers which round to 0.678.
> 
> If 0.107, 0.302 or 0.678 is given with no working, for example straight from a calculator, award 1 mark only for that answer.
Use the definition of conditional probability

`\text{P}(X = 3 \mid X \geq 2) = \dfrac{\text{P}(X = 3 \cap X \geq 2)}{\text{P}(X \geq 2)}`

$X = 3$ already satisfies $X \geq 2$, so the numerator is $\text{P} ( X = 3 )$

`\text{P}(X = 3) = {}^{10}C_{3}\left(0.2\right)^{3}\left(0.8\right)^{7} = 0.201326\ldots`

**[M1]**

The denominator is every outcome except $X = 0$ and $X = 1$

`\text{P}(X \geq 2) = 1 - \left[\left(0.8\right)^{10} + {}^{10}C_{1}(0.2)\left(0.8\right)^{9}\right] = 0.624190\ldots`

**[M1]**

`\text{P}(X = 3 \mid X \geq 2) = \dfrac{0.201326\ldots}{0.624190\ldots} = 0.322540\ldots`

**Final answer:** `\text{P}(X = 3 \mid X \geq 2) = 0.323`** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: P(X = 3) = `{}^{10}C_{3}\left(0.2\right)^{3}\left(0.8\right)^{7}`, seen as the numerator of a fraction.
> 
> **M1**: P(X ≥ 2) = 1 − [P(0) + P(1)], seen as the denominator of a fraction.
> 
> **A1**: 0.323, or answers which round to 0.323.
Use the mean and standard deviation from part (a)

$2 - \sqrt{1.6} < X < 2 + \sqrt{1.6}$

$0 . 735 \dots < X < 3 . 26 \dots$

$X$ is a whole number, so this means $X = 1 ,  2 \text{or} 3$

**[M1]**

`\text{P}(1 \leq X \leq 3) = {}^{10}C_{1}(0.2)\left(0.8\right)^{9} + {}^{10}C_{2}\left(0.2\right)^{2}\left(0.8\right)^{8} + {}^{10}C_{3}\left(0.2\right)^{3}\left(0.8\right)^{7}`

**[M1]**

$\text{P} ( 1 \leq X \leq 3 ) = 0 . 771751 \dots$

**Final answer:** $\text{P} ( 1 \leq X \leq 3 ) = 0 . 772$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: Identifying X = 1, 2, 3 from 2 ± 1.26.
> 
> **M1**: P(1) + P(2) + P(3), with all three terms correct. Accept unsimplified.
> 
> **A1**: 0.772, or answers which round to 0.772.

### Q7
(i)

$X > 3$ is every outcome except $X = 1$, 2 or 3

`\text{P}(X > 3) = 1 - \text{P}(X \leq 3) = 1 - \left[\text{P}(X = 1) + \text{P}(X = 2) + \text{P}(X = 3)\right]`

Use `\text{P}(X = r) = p\left(1 - p\right)^{r - 1}` with $p = 0 . 2$ for each term

`\text{P}(X > 3) = 1 - \left[0.2 + 0.2(0.8) + 0.2\left(0.8\right)^{2}\right]`

**[M1]**

$\text{P} ( X > 3 ) = 1 - 0 . 488$

$\text{P} ( X > 3 ) = 0 . 512$

**[A1]**

(ii)

$X > 4$ is every outcome except $X = 1$, 2, 3 or 4

`\text{P}(X > 4) = 1 - \left[0.2 + 0.2(0.8) + 0.2\left(0.8\right)^{2} + 0.2\left(0.8\right)^{3}\right]`

**[M1]**

$\text{P} ( X > 4 ) = 1 - 0 . 5904$

$\text{P} ( X > 4 ) = 0 . 4096$

**[A1]**

> **[mark-scheme]**
> **M1**: 1 minus the sum of the three terms for X = 1, 2 and 3. Accept unsimplified.
> 
> **A1**: P(X > 3) = 0.512.
> 
> **M1**: 1 minus the sum of the four terms for X = 1 to 4, or the answer to (i) minus P(X = 4). Accept unsimplified.
> 
> **A1**: P(X > 4) = 0.4096. Accept 0.410.
> 
> If 0.512 or 0.4096 is given with no working, for example straight from a calculator, award 1 mark only for that answer.
Part (a) gave `\text{P}(X > 3) = 0.512 = \left(0.8\right)^{3}` and `\text{P}(X > 4) = 0.4096 = \left(0.8\right)^{4}`. $X > k$ means the first $k$ trials are all failures, each with probability 0.8

`\text{P}(X > k) = \left(0.8\right)^{k}`

(i)

$a = 11$

**[B1]**

(ii)

Write $X \geq 20$ in the form $X > k$

`\text{P}(X \geq 20) = \text{P}(X > 19) = \left(0.8\right)^{19}`

$b = 19$

**[B1]**

> **[mark-scheme]**
> **B1**: $a = 11$.
> 
> **B1**: $b = 19$.
> 
> No working is required. The two values are marked independently.

### Q8
(i)

Use `\text{P}(X = r) = p\left(1 - p\right)^{r - 1}` with $p = 0 . 15$ and $r = 4$

`\text{P}(X = 4) = (0.15)\left(0.85\right)^{3}`

**[M1]**

$\text{P} ( X = 4 ) = 0 . 0921187 \dots$

**Final answer:** $\text{P} ( X = 4 ) = 0 . 0921$** (3 s.f.)**

**[A1]**

(ii)

$X$ counts the trials up to and including the first success, so its smallest value is 1, not 0

$\text{P} ( X \leq 2 ) = \text{P} ( X = 1 ) + \text{P} ( X = 2 )$

$\text{P} ( X \leq 2 ) = 0 . 15 + ( 0 . 15 ) ( 0 . 85 )$

**[M1]**

$\text{P} ( X \leq 2 ) = 0 . 2775$

**[A1]**

(iii)

$X \geq 3$ is every outcome except $X \leq 2$, so subtract the answer to (ii) from 1

$\text{P} ( X \geq 3 ) = 1 - 0 . 2775$

$\text{P} ( X \geq 3 ) = 0 . 7225$

**[B1]**

> **[mark-scheme]**
> **M1**: (0.15)(0.85)³ for P(X = 4). Accept unsimplified.
> 
> **A1**: P(X = 4) = 0.0921, or answers which round to 0.0921.
> 
> **M1**: P(1) + P(2), with both terms correct. Accept unsimplified, or 1 − (0.85)².
> 
> **A1**: P(X ≤ 2) = 0.2775, or 0.278.
> 
> **B1**: P(X ≥ 3) = 0.7225, or 0.723. Accept (0.85)² directly. Follow through 1 minus your answer to (ii).

### Q9
(i)

The 8 alpacas are independent, each with the same probability 0.95 of testing negative, so $N$ follows a binomial distribution

`N \sim \text{B}(8, \; 0.95)`

**[B1]**

(ii)

Each alpaca that does not test negative tests positive, with probability $1 - 0 . 95 = 0 . 05$

`T \sim \text{B}(8, \; 0.05)`

**[B1]**

> **[mark-scheme]**
> **B1**: B(8, 0.95), or "binomial with n = 8 and p = 0.95".
> 
> **B1**: B(8, 0.05), or "binomial with n = 8 and p = 0.05".
> 
> Both parameters are needed for each mark. The two distributions are marked independently.
(i)

Use `T \sim \text{B}(8, \; 0.05)`: none positive means all 8 test negative

`\text{P}(T = 0) = \left(0.95\right)^{8} = 0.663420\ldots`

**Final answer:** $\text{P} ( T = 0 ) = 0 . 663$** (3 s.f.)**

**[B1]**

(ii)

$T > 2$ is every outcome except $T = 0$, 1 or 2, so subtract those three terms from 1

`\text{P}(T > 2) = 1 - \left[\left(0.95\right)^{8} + {}^{8}C_{1}(0.05)\left(0.95\right)^{7} + {}^{8}C_{2}\left(0.05\right)^{2}\left(0.95\right)^{6}\right]`

**[M1 A1]**

$\text{P} ( T > 2 ) = 1 - 0 . 994211 \dots = 0 . 005788 \dots$

**Final answer:** $\text{P} ( T > 2 ) = 0 . 00579$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **B1**: 0.663, or answers which round to 0.663.
> 
> **M1**: At least one binomial term of the form `{}^{8}C_{x}\left(0.05\right)^{x}\left(0.95\right)^{8 - x}`.
> 
> **A1**: A correct expression for P(T > 2), written in full with no terms missing: 1 minus the terms for 0, 1 and 2, or the sum of the six terms from 3 to 8. Accept unsimplified.
> 
> **B1**: 0.00579, or answers which round to 0.00579.
> 
> Working with N instead of T is equally valid (more than 2 positive is fewer than 6 negative).
> 
> If 0.00579 is given with no working, for example straight from a calculator, award 1 mark only.

### Q10
(i)

Use `\text{P}(X = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $n = 20$, $p = 0 . 15$ and $r = 4$

`\text{P}(X = 4) = {}^{20}C_{4}\left(0.15\right)^{4}\left(0.85\right)^{16}`

**[M1]**

$\text{P} ( X = 4 ) = 0 . 182121 \dots$

**Final answer:** $\text{P} ( X = 4 ) = 0 . 182$** (3 s.f.)**

**[A1]**

(ii)

$X \leq 1$ means $X = 0$ or $X = 1$, so add those two terms

`\text{P}(X \leq 1) = \left(0.85\right)^{20} + {}^{20}C_{1}(0.15)\left(0.85\right)^{19}`

**[M1]**

$\text{P} ( X \leq 1 ) = 0 . 175557 \dots$

**Final answer:** $\text{P} ( X \leq 1 ) = 0 . 176$** (3 s.f.)**

**[A1]**

(iii)

$X \geq 2$ is every outcome except $X \leq 1$, so subtract the unrounded answer to (ii) from 1

$\text{P} ( X \geq 2 ) = 1 - 0 . 175557 \dots = 0 . 824442 \dots$

**Final answer:** $\text{P} ( X \geq 2 ) = 0 . 824$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(X = 4), with `{}^{20}C_{4}`, `\left(0.15\right)^{4}` and `\left(0.85\right)^{16}`. Accept unsimplified.
> 
> **A1**: P(X = 4) = 0.182, or answers which round to 0.182.
> 
> **M1**: P(0) + P(1), with both terms correct. Accept unsimplified.
> 
> **A1**: P(X ≤ 1) = 0.176, or answers which round to 0.176.
> 
> **B1**: P(X ≥ 2) = 0.824, or answers which round to 0.824. Follow through 1 minus your answer to (ii).
> 
> If 0.182 or 0.176 is given with no working, for example straight from a calculator, award 1 mark only for that answer.

### Q11
(i)

A binomial model needs a constant probability of success and independent trials, so state one of these in context

**Final answer:** **The probability that the snowboarder completes the trick is 0.25 on every attempt**

**[B1]**

(ii)

**Final answer:** **The snowboarder is likely to improve with practice, so the probability of success may increase from one attempt to the next**

**[B1]**

> **[mark-scheme]**
> **B1**: One assumption in context: the probability of completing the trick is constant (0.25) for every attempt, or the attempts are independent of each other.
> 
> **B1**: A reason in context why the assumption may fail, e.g. the snowboarder improves with practice or gets tired, or a fall on one attempt affects the next. The reason must match the assumption given in (i).
> 
> An assumption with no reference to the snowboarder or the trick does not score.
(i)

Let $X$ be the number of successful attempts out of 12

`X \sim \text{B}(12, \; 0.25)`

$X > 2$ is every outcome except $X = 0$, 1 or 2, so subtract those three terms from 1

`\text{P}(X > 2) = 1 - \left[\text{P}(X = 0) + \text{P}(X = 1) + \text{P}(X = 2)\right]`

`\text{P}(X > 2) = 1 - \left[\left(0.75\right)^{12} + {}^{12}C_{1}(0.25)\left(0.75\right)^{11} + {}^{12}C_{2}\left(0.25\right)^{2}\left(0.75\right)^{10}\right]`

**[M1 A1]**

$\text{P} ( X > 2 ) = 1 - 0 . 390675 \dots = 0 . 609324 \dots$

**Final answer:** $\text{P} ( X > 2 ) = 0 . 609$** (3 s.f.)**

**[B1]**

(ii)

No successes means all 12 attempts fail, each with probability 0.75

`\text{P}(X = 0) = \left(0.75\right)^{12} = 0.0316763\ldots`

**Final answer:** $\text{P} ( X = 0 ) = 0 . 0317$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **M1**: At least one binomial term of the form `{}^{12}C_{x}\left(0.25\right)^{x}\left(0.75\right)^{12 - x}`.
> 
> **A1**: A correct expression for P(X > 2), written in full with no terms missing: 1 minus the terms for 0, 1 and 2, or the sum of the ten terms from 3 to 12. Accept unsimplified.
> 
> **B1**: P(X > 2) = 0.609, or answers which round to 0.609.
> 
> **B1**: P(X = 0) = 0.0317, or answers which round to 0.0317.
> 
> If 0.609 is given with no working, for example straight from a calculator, award 1 mark only.

### Q12
(i)

Use `\text{P}(X = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 5$

`\text{P}(X = 5) = {}^{9}C_{5}\left(0.6\right)^{5}\left(0.4\right)^{4}`

**[M1]**

$\text{P} ( X = 5 ) = 0 . 250822 \dots$

**Final answer:** $\text{P} ( X = 5 ) = 0 . 251$** (3 s.f.)**

**[A1]**

(ii)

$X \leq 7$ leaves out only $X = 8$ and $X = 9$, so subtract those two from 1

`\text{P}(X \leq 7) = 1 - \left[\text{P}(X = 8) + \text{P}(X = 9)\right]`

`\text{P}(X \leq 7) = 1 - \left[{}^{9}C_{8}\left(0.6\right)^{8}(0.4) + \left(0.6\right)^{9}\right]`

**[M1]**

$\text{P} ( X \leq 7 ) = 1 - 0 . 070543 \dots = 0 . 929456 \dots$

**Final answer:** $\text{P} ( X \leq 7 ) = 0 . 929$** (3 s.f.)**

**[A1]**

(iii)

$X \geq 3$ leaves out $X = 0$, $X = 1$ and $X = 2$, so subtract those three from 1

`\text{P}(X \geq 3) = 1 - \left[\text{P}(X = 0) + \text{P}(X = 1) + \text{P}(X = 2)\right]`

`\text{P}(X \geq 3) = 1 - \left[\left(0.4\right)^{9} + {}^{9}C_{1}(0.6)\left(0.4\right)^{8} + {}^{9}C_{2}\left(0.6\right)^{2}\left(0.4\right)^{7}\right]`

**[M1]**

$\text{P} ( X \geq 3 ) = 1 - 0 . 025034 \dots = 0 . 974965 \dots$

**Final answer:** $\text{P} ( X \geq 3 ) = 0 . 975$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(X = 5), with `{}^{9}C_{5}`, `\left(0.6\right)^{5}` and `\left(0.4\right)^{4}`. Accept unsimplified.
> 
> **A1**: P(X = 5) = 0.251, or answers which round to 0.251.
> 
> **M1**: A correct expression for P(X ≤ 7), either 1 minus the terms for 8 and 9, or the sum of all eight terms from 0 to 7, with no terms missing. Accept unsimplified.
> 
> **A1**: P(X ≤ 7) = 0.929, or answers which round to 0.929.
> 
> **M1**: A correct expression for P(X ≥ 3), either 1 minus the terms for 0, 1 and 2, or the sum of all seven terms from 3 to 9, with no terms missing. Accept unsimplified.
> 
> **A1**: P(X ≥ 3) = 0.975, or answers which round to 0.975.
> 
> If 0.251, 0.929 or 0.975 is given with no working, for example straight from a calculator, award 1 mark only for that answer.

### Q13
A binomial model needs a constant probability of success and independent trials

**Final answer:** **The probability that a bulb lasts less than 5000 hours is 0.1 for every bulb in the sample**

**[B1]**

**Final answer:** **The lifetime of each bulb is independent of the lifetimes of the other bulbs**

**[B1]**

> **[mark-scheme]**
> **B1**: The probability of a bulb lasting less than 5000 hours is constant (0.1) for every bulb, in context.
> 
> **B1**: The lifetimes of the bulbs are independent of each other, in context.
> 
> The two assumptions are marked independently. "A fixed number of trials" or "two outcomes" are already given in the question, so they do not score.
(i)

Let $X$ be the number of bulbs in the sample with a lifetime of less than 5000 hours

`X \sim \text{B}(30, \; 0.1)`

Use `\text{P}(X = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 1$

`\text{P}(X = 1) = {}^{30}C_{1}(0.1)\left(0.9\right)^{29}`

**[M1]**

$\text{P} ( X = 1 ) = 0 . 141303 \dots$

**Final answer:** $\text{P} ( X = 1 ) = 0 . 141$** (3 s.f.)**

**[A1]**

(ii)

"No more than three" means $X = 0$, 1, 2 or 3, so add those four terms

`\text{P}(X \leq 3) = \left(0.9\right)^{30} + {}^{30}C_{1}(0.1)\left(0.9\right)^{29} + {}^{30}C_{2}\left(0.1\right)^{2}\left(0.9\right)^{28} + {}^{30}C_{3}\left(0.1\right)^{3}\left(0.9\right)^{27}`

**[M1 A1]**

$\text{P} ( X \leq 3 ) = 0 . 647439 \dots$

**Final answer:** $\text{P} ( X \leq 3 ) = 0 . 647$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **M1**: `{}^{30}C_{1}(0.1)\left(0.9\right)^{29}`, or 30 × 0.1 × 0.9²⁹.
> 
> **A1**: 0.141, or answers which round to 0.141.
> 
> **M1**: At least one binomial term of the form `{}^{30}C_{x}\left(0.1\right)^{x}\left(0.9\right)^{30 - x}`.
> 
> **A1**: A correct expression for P(X ≤ 3), written in full with no terms missing. Accept unsimplified.
> 
> **B1**: 0.647, or answers which round to 0.647.
> 
> If 0.141 or 0.647 is given with no working, for example straight from a calculator, award 1 mark only for that answer.

### Q14
For a binomial distribution, use $\text{E} ( X ) = n p$ for the mean and $\text{Var} ( X ) = n p ( 1 - p )$ for the variance

(i)

Here $n = 100$ and $p = 0 . 2$, so $1 - p = 0 . 8$

$\text{E} ( X ) = 100 \times 0 . 2 = 20$

**[B1]**

$\text{Var} ( X ) = 100 \times 0 . 2 \times 0 . 8 = 16$

**[B1]**

(ii)

Here $n = 40$ and $p = 0 . 5$, so $1 - p = 0 . 5$

$\text{E} ( X ) = 40 \times 0 . 5 = 20$

**[B1]**

$\text{Var} ( X ) = 40 \times 0 . 5 \times 0 . 5 = 10$

**[B1]**

(iii)

Here $n = 30$ and $p = 0 . 15$, so $1 - p = 0 . 85$

$\text{E} ( X ) = 30 \times 0 . 15 = 4 . 5$

**[B1]**

$\text{Var} ( X ) = 30 \times 0 . 15 \times 0 . 85 = 3 . 825$

**[B1]**

> **[mark-scheme]**
> **B1**: Mean 20 for B(100, 0.2).
> 
> **B1**: Variance 16 for B(100, 0.2).
> 
> **B1**: Mean 20 for B(40, 0.5).
> 
> **B1**: Variance 10 for B(40, 0.5).
> 
> **B1**: Mean 4.5 for B(30, 0.15).
> 
> **B1**: Variance 3.825 for B(30, 0.15). Accept 3.83.
> 
> Each value is marked independently.
For a geometric distribution, use $\text{E} ( X ) = \frac{1}{p}$ for the mean

(i)

$\text{E} ( X ) = \frac{1}{0.2} = 5$

**[B1]**

(ii)

$\text{E} ( X ) = \frac{1}{0.5} = 2$

**[B1]**

(iii)

$\text{E} ( X ) = \frac{1}{0.15}$

$\text{E} ( X ) = \frac{20}{3}$

**[B1]**

> **[mark-scheme]**
> **B1**: Mean 5 for Geo(0.2).
> 
> **B1**: Mean 2 for Geo(0.5).
> 
> **B1**: Mean $\frac{20}{3}$ for Geo(0.15). Accept 6.67 or 6.7, but not 1/0.15 left unevaluated.

### Q15
A geometric model needs a constant probability of success and independent trials

**Final answer:** **The probability that Gregg breaks the yolk is 0.05 for every egg**

**[B1]**

**Final answer:** **Whether Gregg breaks the yolk of one egg is independent of what happens with any other egg**

**[B1]**

> **[mark-scheme]**
> **B1**: The probability of breaking the yolk is constant (0.05) for every egg, in context.
> 
> **B1**: Breaking the yolk of one egg is independent of the other eggs, in context.
> 
> The two assumptions are marked independently. An assumption with no reference to Gregg, eggs or yolks does not score.
(i)

Let $X$ be the number of eggs Gregg cracks open up to and including the first broken yolk

`X \sim \text{Geo}(0.05)`

Use `\text{P}(X = r) = p\left(1 - p\right)^{r - 1}`: the first 9 yolks stay whole, then the 10th breaks

`\text{P}(X = 10) = \left(0.95\right)^{9}(0.05)`

**[M1]**

$\text{P} ( X = 10 ) = 0 . 0315124 \dots$

**Final answer:** $\text{P} ( X = 10 ) = 0 . 0315$** (3 s.f.)**

**[A1]**

(ii)

The only way to fail is for all of the first 4 yolks to stay whole, so subtract that from 1

`\text{P}(X \leq 4) = 1 - \left(0.95\right)^{4}`

**[M1]**

$\text{P} ( X \leq 4 ) = 1 - 0 . 81450 \dots = 0 . 185493 \dots$

**Final answer:** $\text{P} ( X \leq 4 ) = 0 . 185$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `\left(0.95\right)^{9}(0.05)`, or `\left(1 - p\right)^{9}p` with 0 < p < 1.
> 
> **A1**: 0.0315, or answers which round to 0.0315.
> 
> **M1**: `1 - \left(0.95\right)^{4}`, or the sum P(1) + P(2) + P(3) + P(4). Accept `1 - \left(0.95\right)^{3}` or `1 - \left(0.95\right)^{5}` for this mark only.
> 
> **A1**: 0.185, or answers which round to 0.185.
> 
> If 0.0315 or 0.185 is given with no working, for example straight from a calculator, award 1 mark only for that answer.

### Q16
(i)

Use `\text{P}(X = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $n = 25$, $p = 0 . 3$ and $r = 12$

`\text{P}(X = 12) = {}^{25}C_{12}\left(0.3\right)^{12}\left(0.7\right)^{13}`

**[M1]**

$\text{P} ( X = 12 ) = 0 . 0267767 \dots$

**Final answer:** $\text{P} ( X = 12 ) = 0 . 0268$** (3 s.f.)**

**[A1]**

(ii)

$X \leq 2$ means $X = 0$, 1 or 2, so add those three terms

`\text{P}(X \leq 2) = \left(0.7\right)^{25} + {}^{25}C_{1}(0.3)\left(0.7\right)^{24} + {}^{25}C_{2}\left(0.3\right)^{2}\left(0.7\right)^{23}`

**[M1]**

$\text{P} ( X \leq 2 ) = 0 . 00896052 \dots$

**Final answer:** $\text{P} ( X \leq 2 ) = 0 . 00896$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(X = 12), with `{}^{25}C_{12}`, `\left(0.3\right)^{12}` and `\left(0.7\right)^{13}`. Accept unsimplified.
> 
> **A1**: P(X = 12) = 0.0268, or answers which round to 0.0268.
> 
> **M1**: P(0) + P(1) + P(2), with all three terms correct. Accept unsimplified.
> 
> **A1**: P(X ≤ 2) = 0.00896, or answers which round to 0.00896.
> 
> If 0.0268 or 0.00896 is given with no working, for example straight from a calculator, award 1 mark only for that answer.
(i)

Use `\text{P}(Y = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $n = 25$, $p = 0 . 7$ and $r = 13$

`\text{P}(Y = 13) = {}^{25}C_{13}\left(0.7\right)^{13}\left(0.3\right)^{12}`

**[M1]**

$\text{P} ( Y = 13 ) = 0 . 0267767 \dots$

**Final answer:** $\text{P} ( Y = 13 ) = 0 . 0268$** (3 s.f.)**

**[A1]**

(ii)

$Y \geq 23$ means $Y = 23$, 24 or 25, so add those three terms

`\text{P}(Y \geq 23) = {}^{25}C_{23}\left(0.7\right)^{23}\left(0.3\right)^{2} + {}^{25}C_{24}\left(0.7\right)^{24}(0.3) + \left(0.7\right)^{25}`

**[M1]**

$\text{P} ( Y \geq 23 ) = 0 . 00896052 \dots$

**Final answer:** $\text{P} ( Y \geq 23 ) = 0 . 00896$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(Y = 13), with `{}^{25}C_{13}`, `\left(0.7\right)^{13}` and `\left(0.3\right)^{12}`. Accept unsimplified.
> 
> **A1**: P(Y = 13) = 0.0268, or answers which round to 0.0268.
> 
> **M1**: P(23) + P(24) + P(25), with all three terms correct. Accept unsimplified.
> 
> **A1**: P(Y ≥ 23) = 0.00896, or answers which round to 0.00896.
> 
> If 0.0268 or 0.00896 is given with no working, for example straight from a calculator, award 1 mark only for that answer.
The answers to (a) and (b) match because the probabilities of success and failure are swapped: 12 successes and 13 failures for $X$ is 13 successes and 12 failures for $Y$

$\text{P} ( X = r ) = \text{P} ( Y = 25 - r )$

(i)

$\text{P} ( X = 10 ) = \text{P} ( Y = 25 - 10 )$

$a = 15$

**[B1]**

(ii)

$X$ takes the values 20 to 25, which match $Y$ taking the values 5 down to 0

$\text{P} ( X \geq 20 ) = \text{P} ( Y \leq 25 - 20 )$

$b = 5$

**[B1]**

> **[mark-scheme]**
> **B1**: $a = 15$.
> 
> **B1**: $b = 5$.
> 
> No working is required. The two values are marked independently.

### Q17
The 24 cans are a random sample, so they are independent, each with the same probability 0.0296 of containing less than 320 ml

`L \sim \text{B}(24, \; 0.0296)`

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Binomial, or B.
> 
> **B1**: n = 24 and p = 0.0296.
(i)

None means all 24 cans contain at least 320 ml, each with probability $1 - 0 . 0296 = 0 . 9704$

`\text{P}(L = 0) = \left(0.9704\right)^{24} = 0.486204\ldots`

**Final answer:** $\text{P} ( L = 0 ) = 0 . 486$** (3 s.f.)**

**[B1]**

(ii)

Use `\text{P}(L = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 2$

`\text{P}(L = 2) = {}^{24}C_{2}\left(0.0296\right)^{2}\left(0.9704\right)^{22} = 0.124856\ldots`

**Final answer:** $\text{P} ( L = 2 ) = 0 . 125$** (3 s.f.)**

**[B1]**

(iii)

At least two is every outcome except $L = 0$ and $L = 1$

`\text{P}(L \geq 2) = 1 - \left[\left(0.9704\right)^{24} + {}^{24}C_{1}(0.0296)\left(0.9704\right)^{23}\right]`

**[M1]**

$\text{P} ( L \geq 2 ) = 1 - ( 0 . 486204 \dots + 0 . 355935 \dots ) = 0 . 157860 \dots$

**Final answer:** $\text{P} ( L \geq 2 ) = 0 . 158$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: 0.486, or answers which round to 0.486.
> 
> **B1**: 0.125, or answers which round to 0.125.
> 
> **M1**: 1 − [P(0) + P(1)], with both terms correct. Accept unsimplified.
> 
> **A1**: 0.158, or answers which round to 0.158.
> 
> If 0.158 is given with no working, for example straight from a calculator, award 1 mark only.

### Q18
The throws are independent, each with the same probability $p$ of a hit, so `X \sim \text{Geo}(p)` and $\text{E} ( X ) = \frac{1}{p}$

$\frac{1}{p} = \frac{4}{3}$

$p = \frac{3}{4}$

**[B1]**

> **[mark-scheme]**
> **B1**: $p = \frac{3}{4}$, or 0.75.
(i)

$X > 6$ means Ravi misses with each of his first 6 throws, each with probability $1 - 0 . 75 = 0 . 25$

`\text{P}(X > 6) = \left(0.25\right)^{6}`

**[M1]**

$\text{P} ( X > 6 ) = \frac{1}{4096} = 0 . 000244140 \dots$

**Final answer:** $\text{P} ( X > 6 ) = 0 . 000244$** (3 s.f.)**

**[A1]**

(ii)

$X \leq 5$ is every outcome except missing with all of the first 5 throws

`\text{P}(X \leq 5) = 1 - \left(0.25\right)^{5} = \dfrac{1023}{1024}`

**Final answer:** $\text{P} ( X \leq 5 ) = 0 . 999$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **M1**: `\left(0.25\right)^{6}`, or `\left(1 - p\right)^{6}` using the value of p from part (a). Accept a power of 5 or 7 for this mark only.
> 
> **A1**: 0.000244, or answers which round to 0.000244. Accept $\frac{1}{4096}$.
> 
> **B1**: 0.999, or $\frac{1023}{1024}$, or answers which round to 0.999.
The school days are independent, each with the same probability 0.4 of the bus arriving late, so `Y \sim \text{B}(n, \; 0.4)` and $\text{E} ( Y ) = n p$

$0 . 4 n = 12$

$n = 30$

**[B1]**

> **[mark-scheme]**
> **B1**: n = 30.
(i)

Use the model from part (c)

`Y \sim \text{B}(30, \; 0.4)`

$8 < Y < 12$ means $Y = 9$, 10 or 11, so add those three terms

`\text{P}(8 < Y < 12) = {}^{30}C_{9}\left(0.4\right)^{9}\left(0.6\right)^{21} + {}^{30}C_{10}\left(0.4\right)^{10}\left(0.6\right)^{20} + {}^{30}C_{11}\left(0.4\right)^{11}\left(0.6\right)^{19}`

**[M1 A1]**

$\text{P} ( 8 < Y < 12 ) = 0 . 337079 \dots$

**Final answer:** $\text{P} ( 8 < Y < 12 ) = 0 . 337$** (3 s.f.)**

**[B1]**

(ii)

Use $\text{Var} ( Y ) = n p ( 1 - p )$

$\text{Var} ( Y ) = 30 \times 0 . 4 \times 0 . 6$

$\text{Var} ( Y ) = 7 . 2$

**[B1]**

> **[mark-scheme]**
> **M1**: At least one binomial term of the form `{}^{30}C_{x}\left(0.4\right)^{x}\left(0.6\right)^{30 - x}`.
> 
> **A1**: The correct expression P(9) + P(10) + P(11), written in full with no terms missing. Accept unsimplified.
> 
> **B1**: 0.337, or answers which round to 0.337.
> 
> **B1**: Var(Y) = 7.2.
> 
> If 0.337 is given with no working, for example straight from a calculator, award 1 mark only.

### Q19
The rolls are independent, each with the same probability 0.25 of a two, so $X$, the number of rolls up to and including the first two, follows a geometric distribution

`X \sim \text{Geo}(0.25)`

Use `\text{P}(X = r) = p\left(1 - p\right)^{r - 1}`: the first 10 rolls are not a two, then the 11th is

`\text{P}(X = 11) = \left(0.75\right)^{10}(0.25)`

**[M1]**

$\text{P} ( X = 11 ) = 0 . 0140783 \dots$

**Final answer:** $\text{P} ( X = 11 ) = 0 . 0141$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `\left(0.75\right)^{10}(0.25)`, or `\left(1 - p\right)^{10}p` with 0 < p < 1.
> 
> **A1**: 0.0141, or answers which round to 0.0141.
The 10 rolls are independent, each with the same probability 0.25 of a two, so $Y$, the number of twos, follows a binomial distribution

`Y \sim \text{B}(10, \; 0.25)`

Use `\text{P}(Y = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 4$

`\text{P}(Y = 4) = {}^{10}C_{4}\left(0.25\right)^{4}\left(0.75\right)^{6}`

**[M1]**

$\text{P} ( Y = 4 ) = 0 . 145998 \dots$

**Final answer:** $\text{P} ( Y = 4 ) = 0 . 146$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `{}^{10}C_{4}\left(0.25\right)^{4}\left(0.75\right)^{6}`, or 210 × 0.25⁴ × 0.75⁶.
> 
> **A1**: 0.146, or answers which round to 0.146.

### Q20
A binomial model needs a constant probability of success and independent trials

**Final answer:** **The probability that a resident prefers Woostershire sauce is 0.9 for every resident in the sample**

**[B1]**

**Final answer:** **Each resident's preference is independent of the other residents' preferences**

**[B1]**

> **[mark-scheme]**
> **B1**: The probability of preferring Woostershire sauce is constant (0.9) for every resident, in context.
> 
> **B1**: The residents' preferences are independent of each other, in context.
> 
> The two assumptions are marked independently. "A fixed number of trials" or "two outcomes" do not score.
(i)

`X \sim \text{B}(30, \; 0.9)`

90% of 30 is 27, so "more than 90%" means $X = 28$, 29 or 30

`\text{P}(X > 27) = {}^{30}C_{28}\left(0.9\right)^{28}\left(0.1\right)^{2} + {}^{30}C_{29}\left(0.9\right)^{29}(0.1) + \left(0.9\right)^{30}`

**[M1]**

$\text{P} ( X > 27 ) = 0 . 411351 \dots$

**Final answer:** $\text{P} ( X > 27 ) = 0 . 411$** (3 s.f.)**

**[A1]**

(ii)

None prefer the other brand means all 30 prefer Woostershire sauce

`\text{P}(X = 30) = \left(0.9\right)^{30} = 0.0423911\ldots`

**Final answer:** $\text{P} ( X = 30 ) = 0 . 0424$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **M1**: P(28) + P(29) + P(30), with all three terms correct. Accept unsimplified.
> 
> **A1**: 0.411, or answers which round to 0.411.
> 
> **B1**: 0.0424, or answers which round to 0.0424.
> 
> If 0.411 is given with no working, for example straight from a calculator, award 1 mark only.
(i)

Use $\text{E} ( X ) = n p$

$\text{E} ( X ) = 30 \times 0 . 9$

$\text{E} ( X ) = 27$

**[B1]**

(ii)

Use $\text{Var} ( X ) = n p ( 1 - p )$

$\text{Var} ( X ) = 30 \times 0 . 9 \times 0 . 1$

$\text{Var} ( X ) = 2 . 7$

**[B1]**

> **[mark-scheme]**
> **B1**: E(X) = 27.
> 
> **B1**: Var(X) = 2.7.

### Q21
A binomial model needs a constant probability of success and independent trials

**Final answer:** **The probability that a jellyfish contains microplastic particles is 0.95 for every jellyfish in the sample**

**[B1]**

**Final answer:** **Whether one jellyfish contains microplastic particles is independent of whether any other jellyfish does**

**[B1]**

> **[mark-scheme]**
> **B1**: The probability of a jellyfish containing microplastic particles is constant (0.95), in context.
> 
> **B1**: Jellyfish contain microplastic particles independently of each other, in context.
> 
> The two assumptions are marked independently. "A fixed number of trials" or "two outcomes" do not score.
(i)

Let $X$ be the number of jellyfish in the sample that contain microplastic particles

`X \sim \text{B}(40, \; 0.95)`

Use `\text{P}(X = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 38$

`\text{P}(X = 38) = {}^{40}C_{38}\left(0.95\right)^{38}\left(0.05\right)^{2}`

**[M1]**

$\text{P} ( X = 38 ) = 0 . 277671 \dots$

**Final answer:** $\text{P} ( X = 38 ) = 0 . 278$** (3 s.f.)**

**[A1]**

(ii)

All 40 means every jellyfish contains particles

`\text{P}(X = 40) = \left(0.95\right)^{40} = 0.128512\ldots`

**Final answer:** $\text{P} ( X = 40 ) = 0 . 129$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **M1**: `{}^{40}C_{38}\left(0.95\right)^{38}\left(0.05\right)^{2}`, or 780 × 0.95³⁸ × 0.05².
> 
> **A1**: 0.278, or answers which round to 0.278.
> 
> **B1**: 0.129, or answers which round to 0.129.

### Q22
The 5 days are independent, each with the same probability 0.6 of a taxi, so $X$, the number of days on which Yussuf catches a taxi, follows a binomial distribution

`X \sim \text{B}(5, \; 0.6)`

Use $\text{E} ( X ) = n p$

$\text{E} ( X ) = 5 \times 0 . 6$

$\text{E} ( X ) = 3$

**[B1]**

> **[mark-scheme]**
> **B1**: 3.
Never means no taxi on any of the 5 days, each with probability $1 - 0 . 6 = 0 . 4$

`\text{P}(X = 0) = \left(0.4\right)^{5}`

**[M1]**

$\text{P} ( X = 0 ) = 0 . 01024$

**[A1]**

> **[mark-scheme]**
> **M1**: `\left(0.4\right)^{5}`, or `{}^{5}C_{0}\left(0.6\right)^{0}\left(0.4\right)^{5}`.
> 
> **A1**: 0.01024. Accept 0.0102.
At most once means $X = 0$ or $X = 1$, so add those two terms

`\text{P}(X \leq 1) = \left(0.4\right)^{5} + {}^{5}C_{1}(0.6)\left(0.4\right)^{4}`

**[M1]**

$\text{P} ( X \leq 1 ) = 0 . 01024 + 0 . 0768$

$\text{P} ( X \leq 1 ) = 0 . 08704$

**[A1]**

> **[mark-scheme]**
> **M1**: P(0) + P(1), with both terms correct. Accept unsimplified.
> 
> **A1**: 0.08704. Accept 0.0870.
> 
> If 0.08704 is given with no working, for example straight from a calculator, award 1 mark only.

### Q23
The cars are independent, each with the same probability 0.25 of being blue, so $X$, the number of cars that pass up to and including the first blue car, follows a geometric distribution

`X \sim \text{Geo}(0.25)`

Use `\text{P}(X = r) = p\left(1 - p\right)^{r - 1}`: the first 7 cars are not blue, then the 8th is

`\text{P}(X = 8) = \left(0.75\right)^{7}(0.25)`

**[M1]**

$\text{P} ( X = 8 ) = 0 . 0333709 \dots$

**Final answer:** $\text{P} ( X = 8 ) = 0 . 0334$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `\left(0.75\right)^{7}(0.25)`, or `\left(1 - p\right)^{7}p` with 0 < p < 1.
> 
> **A1**: 0.0334, or answers which round to 0.0334.
The only way to fail is for none of the first 8 cars to be blue, so subtract that from 1

`\text{P}(X \leq 8) = 1 - \left(0.75\right)^{8}`

**[M1]**

$\text{P} ( X \leq 8 ) = 1 - 0 . 100112 \dots = 0 . 899887 \dots$

**Final answer:** $\text{P} ( X \leq 8 ) = 0 . 900$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `1 - \left(0.75\right)^{8}`, or the sum of the eight terms P(1) + … + P(8). Accept `1 - \left(0.75\right)^{7}` or `1 - \left(0.75\right)^{9}` for this mark only.
> 
> **A1**: 0.900, or answers which round to 0.900. Accept 0.8999.
Use $\text{E} ( X ) = \frac{1}{p}$ for a geometric distribution

$\text{E} ( X ) = \frac{1}{0.25}$

$\text{E} ( X ) = 4$

**[B1]**

> **[mark-scheme]**
> **B1**: 4.

### Q24
A binomial model needs a constant probability of success and independent trials

**Final answer:** **The probability of the coin landing heads up is 0.5 on every toss**

**[B1]**

**Final answer:** **The result of each toss is independent of the results of the other tosses**

**[B1]**

> **[mark-scheme]**
> **B1**: The probability of heads is constant (0.5) for every toss, in context.
> 
> **B1**: The tosses are independent of each other, in context.
> 
> The two assumptions are marked independently. "A fixed number of trials" or "two outcomes" are already given in the question, so they do not score.
The coin is fair, so the probability of heads is 0.5 on each of the 20 tosses

`X \sim \text{B}(20, \; 0.5)`

Use `\text{P}(X = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 15$

`\text{P}(X = 15) = {}^{20}C_{15}\left(0.5\right)^{15}\left(0.5\right)^{5}`

**[M1]**

$\text{P} ( X = 15 ) = \frac{15504}{1048576} = 0 . 0147857 \dots$

**Final answer:** $\text{P} ( X = 15 ) = 0 . 0148$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `{}^{20}C_{15}\left(0.5\right)^{15}\left(0.5\right)^{5}`, or `{}^{20}C_{15}\left(0.5\right)^{20}`.
> 
> **A1**: 0.0148, or answers which round to 0.0148. Accept $\frac{969}{65536}$.

### Q25
(i)

"Fewer than 3" means $X = 0$, 1 or 2, so add those three terms

`\text{P}(X < 3) = \left(0.65\right)^{20} + {}^{20}C_{1}(0.35)\left(0.65\right)^{19} + {}^{20}C_{2}\left(0.35\right)^{2}\left(0.65\right)^{18}`

**[M1]**

$\text{P} ( X < 3 ) = 0 . 0121177 \dots$

**Final answer:** $\text{P} ( X < 3 ) = 0 . 0121$** (3 s.f.)**

**[A1]**

(ii)

"No more than 3" means $X \leq 3$, which is the answer to (i) plus the term for $X = 3$

`\text{P}(X \leq 3) = 0.0121177\ldots + {}^{20}C_{3}\left(0.35\right)^{3}\left(0.65\right)^{17} = 0.0443756\ldots`

**Final answer:** $\text{P} ( X \leq 3 ) = 0 . 0444$** (3 s.f.)**

**[B1]**

(iii)

"At least 3" means $X \geq 3$, which is every outcome except $X < 3$

$\text{P} ( X \geq 3 ) = 1 - 0 . 0121177 \dots = 0 . 987882 \dots$

**Final answer:** $\text{P} ( X \geq 3 ) = 0 . 988$** (3 s.f.)**

**[B1]**

(iv)

"At most 3" means $X \leq 3$, the same event as (ii)

**Final answer:** $\text{P} ( X \leq 3 ) = 0 . 0444$** (3 s.f.)**

**[B1]**

(v)

"More than 3" means $X > 3$, which is every outcome except $X \leq 3$

$\text{P} ( X > 3 ) = 1 - 0 . 0443756 \dots = 0 . 955624 \dots$

**Final answer:** $\text{P} ( X > 3 ) = 0 . 956$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **M1**: P(0) + P(1) + P(2), with all three terms correct. Accept unsimplified.
> 
> **A1**: P(X < 3) = 0.0121, or answers which round to 0.0121.
> 
> **B1**: P(X ≤ 3) = 0.0444, or answers which round to 0.0444.
> 
> **B1**: P(X ≥ 3) = 0.988, or answers which round to 0.988.
> 
> **B1**: P(X ≤ 3) = 0.0444 for "at most 3".
> 
> **B1**: P(X > 3) = 0.956, or answers which round to 0.956.
> 
> Follow through from earlier answers for the last four marks. If 0.0121 is given with no working, for example straight from a calculator, award 1 mark only.

### Q26
(i)

The attempts are independent, each with the same probability 0.16 of a pass, so $X$, the number of attempts Bucky takes up to and including the one he passes, follows a geometric distribution

`X \sim \text{Geo}(0.16)`

Use `\text{P}(X = r) = p\left(1 - p\right)^{r - 1}`: he fails 4 times, then passes

`\text{P}(X = 5) = \left(0.84\right)^{4}(0.16)`

**[M1]**

$\text{P} ( X = 5 ) = 0 . 0796594 \dots$

**Final answer:** $\text{P} ( X = 5 ) = 0 . 0797$** (3 s.f.)**

**[A1]**

(ii)

At least 5 attempts means he fails each of his first 4 attempts

`\text{P}(X \geq 5) = \text{P}(X > 4) = \left(0.84\right)^{4} = 0.497871\ldots`

**Final answer:** $\text{P} ( X \geq 5 ) = 0 . 498$** (3 s.f.)**

**[B1]**

(iii)

The only way to fail is to fail all of the first 10 attempts, so subtract that from 1

`\text{P}(X \leq 10) = 1 - \left(0.84\right)^{10}`

**[M1]**

$\text{P} ( X \leq 10 ) = 1 - 0 . 174901 \dots = 0 . 825098 \dots$

**Final answer:** $\text{P} ( X \leq 10 ) = 0 . 825$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `\left(0.84\right)^{4}(0.16)`, or `\left(1 - p\right)^{4}p` with 0 < p < 1.
> 
> **A1**: 0.0797, or answers which round to 0.0797.
> 
> **B1**: 0.498, or answers which round to 0.498.
> 
> **M1**: `1 - \left(0.84\right)^{10}`, or the sum of the ten terms P(1) + … + P(10). Accept `1 - \left(0.84\right)^{9}` or `1 - \left(0.84\right)^{11}` for this mark only.
> 
> **A1**: 0.825, or answers which round to 0.825.
Use $\text{E} ( X ) = \frac{1}{p}$

$\text{E} ( X ) = \frac{1}{0.16}$

$\text{E} ( X ) = 6 . 25$

**[B1]**

> **[mark-scheme]**
> **B1**: 6.25, or $\frac{25}{4}$.
**Final answer:** **Bucky is likely to improve as he becomes more familiar with the examination, so the probability of passing is unlikely to stay at 0.16 for every attempt**

**[B1]**

> **[mark-scheme]**
> **B1**: A reason in context why the probability may not be constant (e.g. Bucky improves with practice, or becomes discouraged), or why attempts may not be independent. A statement such as "the events are not independent" with no reference to Bucky or the examination does not score.

### Q27
The rolls are independent, each with the same probability $\frac{2}{11}$ of a 5, so $X$, the number of rolls up to and including the first 5, follows a geometric distribution

`X \sim \text{Geo}\left(\dfrac{2}{11}\right)`

Use `\text{P}(X = r) = p\left(1 - p\right)^{r - 1}`: the first 20 rolls are not a 5, then the 21st is

`\text{P}(X = 21) = \left(\dfrac{9}{11}\right)^{20}\left(\dfrac{2}{11}\right)`

**[M1]**

$\text{P} ( X = 21 ) = 0 . 00328574 \dots$

**Final answer:** $\text{P} ( X = 21 ) = 0 . 00329$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `\left(\dfrac{9}{11}\right)^{20}\left(\dfrac{2}{11}\right)`, or `\left(1 - p\right)^{20}p` with 0 < p < 1.
> 
> **A1**: 0.00329, or answers which round to 0.00329.
(i)

The 20 rolls are independent, each with the same probability $\frac{2}{11}$ of a 5, so $Y$, the number of 5s, follows a binomial distribution

`Y \sim \text{B}\left(20, \; \dfrac{2}{11}\right)`

Use `\text{P}(Y = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 4$

`\text{P}(Y = 4) = {}^{20}C_{4}\left(\dfrac{2}{11}\right)^{4}\left(\dfrac{9}{11}\right)^{16}`

**[M1]**

$\text{P} ( Y = 4 ) = 0 . 213520 \dots$

**Final answer:** $\text{P} ( Y = 4 ) = 0 . 214$** (3 s.f.)**

**[A1]**

(ii)

The final 5 is not on the 20th roll, so all four 5s come in the first 19 rolls and the 20th roll is not a 5

$\text{P} = \text{P} ( \text{four 5s in the first 19 rolls} ) \times \text{P} ( \text{20th roll is not a 5} )$

**[M1]**

The first factor is a binomial term with $n = 19$

`\text{P} = {}^{19}C_{4}\left(\dfrac{2}{11}\right)^{4}\left(\dfrac{9}{11}\right)^{15} \times \dfrac{9}{11}`

**[M1]**

$\text{P} = 0 . 170816 \dots$

**Final answer:** $\text{P} = 0 . 171$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `{}^{20}C_{4}\left(\dfrac{2}{11}\right)^{4}\left(\dfrac{9}{11}\right)^{16}`.
> 
> **A1**: 0.214, or answers which round to 0.214.
> 
> **M1**: Recognising that all four 5s are in the first 19 rolls and the 20th roll is not a 5.
> 
> **M1**: `{}^{19}C_{4}\left(\dfrac{2}{11}\right)^{4}\left(\dfrac{9}{11}\right)^{15} \times \dfrac{9}{11}`, or equivalently `{}^{19}C_{4}\left(\dfrac{2}{11}\right)^{4}\left(\dfrac{9}{11}\right)^{16}`.
> 
> **A1**: 0.171, or answers which round to 0.171.
> 
> Alternative method: $\frac{16}{20}$ × the answer to (i) scores full marks for (ii).

### Q28
The probability outside the range is split equally between the two tails

$\text{P} ( \text{bar weighs less than 297 g} ) = \frac{1-0.9596}{2} = 0 . 0202$

**[B1]**

The 25 bars are a random sample, so they are independent, each with the same probability 0.0202 of weighing less than 297 g

`U \sim \text{B}(25, \; 0.0202)`

**[B1]**

> **[mark-scheme]**
> **B1**: The probability 0.0202, seen or implied.
> 
> **B1**: B(25, 0.0202), or "binomial with n = 25 and p = 0.0202". Follow through your value of p.
(i)

24 of the 25 bars are needed, so there is enough for everyone when at most 1 bar is underweight

`\text{P}(U \leq 1) = \left(0.9798\right)^{25} + {}^{25}C_{1}(0.0202)\left(0.9798\right)^{24}`

**[M1]**

$\text{P} ( U \leq 1 ) = 0 . 909842 \dots$

**Final answer:** $\text{P} ( U \leq 1 ) = 0 . 910$** (3 s.f.)**

**[A1]**

(ii)

Enough for exactly 23 people means exactly 2 bars are underweight

`\text{P}(U = 2) = {}^{25}C_{2}\left(0.0202\right)^{2}\left(0.9798\right)^{23}`

$\text{P} ( U = 2 ) = 0 . 0765570 \dots$

**Final answer:** $\text{P} ( U = 2 ) = 0 . 0766$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **M1**: P(0) + P(1), with both terms correct for their p. Accept unsimplified.
> 
> **A1**: 0.910, or answers which round to 0.910.
> 
> **B1**: 0.0766, or answers which round to 0.0766.
> 
> If 0.910 is given with no working, for example straight from a calculator, award 1 mark only.

### Q29
(i)

$X \geq 3$ means the first 2 trials are both failures

`\text{P}(X \geq 3) = \text{P}(X > 2) = \left(1 - p\right)^{2}`

`\left(1 - p\right)^{2} = 0.09`

**[M1]**

Take the square root of both sides

$1 - p = 0 . 3$* or *$1 - p = - 0 . 3$

$1 - p$ is a probability, so it cannot be negative

$p = 0 . 7$

**[A1]**

(ii)

Use `\text{P}(X = r) = p\left(1 - p\right)^{r - 1}` with $r = 2$

$p ( 1 - p ) = 0 . 2275$

**[M1]**

Rearrange into a quadratic in $p$

$p^{2} - p + 0 . 2275 = 0$

Solve, using the quadratic formula

$p = \frac{1\pm\sqrt{1-4(0.2275)}}{2} = \frac{1\pm0.3}{2}$

**Final answer:** $p = 0 . 35$** or **$p = 0 . 65$

**[A1]**

> **[mark-scheme]**
> **M1**: `\left(1 - p\right)^{2} = 0.09`.
> 
> **A1**: p = 0.7 only. The value 1.3 must be rejected, or not given.
> 
> **M1**: $p ( 1 - p ) = 0 . 2275$.
> 
> **A1**: p = 0.35 and p = 0.65. Both values are needed. Accept solving by factorising or completing the square.
(i)

Use $\text{E} ( Y ) = n p$ with $n = 5$

$5 p = 3$

$p = 0 . 6$

**[B1]**

(ii)

$Y = 5$ means all 5 trials are successes

`\text{P}(Y = 5) = {}^{5}C_{5} \, p^{5}\left(1 - p\right)^{0} = p^{5}`

$p^{5} = 0 . 32768$

`p = \left(0.32768\right)^{\frac{1}{5}}`

$p = 0 . 8$

**[B1]**

(iii)

Use $\text{Var} ( Y ) = n p ( 1 - p )$ with $n = 5$

$5 p ( 1 - p ) = 1 . 05$

**[M1]**

Divide by 5 and rearrange into a quadratic in $p$

$p^{2} - p + 0 . 21 = 0$

Factorise

$( p - 0 . 3 ) ( p - 0 . 7 ) = 0$

**[M1]**

**Final answer:** $p = 0 . 3$** or **$p = 0 . 7$

**[A1]**

> **[mark-scheme]**
> **B1**: p = 0.6.
> 
> **B1**: p = 0.8.
> 
> **M1**: $5 p ( 1 - p ) = 1 . 05$.
> 
> **M1**: Solving the resulting three-term quadratic by any valid method.
> 
> **A1**: p = 0.3 and p = 0.7. Both values are needed.

### Q30
A binomial model needs a constant probability of success and independent trials

**Final answer:** **The probability that a squirrel is local is 0.92 for every squirrel in the sample**

**[B1]**

**Final answer:** **Whether one squirrel is local is independent of whether any other squirrel is local**

**[B1]**

> **[mark-scheme]**
> **B1**: The probability of a squirrel being local is constant (0.92), in context.
> 
> **B1**: Squirrels are local independently of each other, in context.
> 
> The two assumptions are marked independently. "A fixed number of trials" or "two outcomes" do not score.
(i)

Let $X$ be the number of local squirrels in the sample

`X \sim \text{B}(50, \; 0.92)`

Use `\text{P}(X = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 45$

`\text{P}(X = 45) = {}^{50}C_{45}\left(0.92\right)^{45}\left(0.08\right)^{5}`

**[M1]**

$\text{P} ( X = 45 ) = 0 . 162923 \dots$

**Final answer:** $\text{P} ( X = 45 ) = 0 . 163$** (3 s.f.)**

**[A1]**

(ii)

All but one of the 50 means $X = 49$

`\text{P}(X = 49) = {}^{50}C_{49}\left(0.92\right)^{49}(0.08)`

**[M1]**

$\text{P} ( X = 49 ) = 0 . 0672455 \dots$

**Final answer:** $\text{P} ( X = 49 ) = 0 . 0672$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `{}^{50}C_{45}\left(0.92\right)^{45}\left(0.08\right)^{5}`.
> 
> **A1**: 0.163, or answers which round to 0.163.
> 
> **M1**: Recognising "all but one" as X = 49: `{}^{50}C_{49}\left(0.92\right)^{49}(0.08)`, or 50 × 0.92⁴⁹ × 0.08.
> 
> **A1**: 0.0672, or answers which round to 0.0672.

### Q31
A binomial model needs a constant probability of success and independent trials

**Final answer:** **The probability of the die landing on a 4 is the same on every roll**

**[B1]**

**Final answer:** **The result of each roll is independent of the results of the other rolls**

**[B1]**

> **[mark-scheme]**
> **B1**: The probability of a 4 is constant for every roll, in context.
> 
> **B1**: The rolls are independent of each other, in context.
> 
> The two assumptions are marked independently. "A fixed number of trials" or "two outcomes" are already given in the question, so they do not score.
The die is fair, so the probability of a 4 on each roll is $\frac{1}{6}$

`X \sim \text{B}\left(24, \; \dfrac{1}{6}\right)`

Use `\text{P}(X = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 4$

`\text{P}(X = 4) = {}^{24}C_{4}\left(\dfrac{1}{6}\right)^{4}\left(\dfrac{5}{6}\right)^{20}`

**[M1]**

$\text{P} ( X = 4 ) = 0 . 213865 \dots$

**Final answer:** $\text{P} ( X = 4 ) = 0 . 214$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `{}^{24}C_{4}\left(\dfrac{1}{6}\right)^{4}\left(\dfrac{5}{6}\right)^{20}`, or 10626 × (1/6)⁴ × (5/6)²⁰.
> 
> **A1**: 0.214, or answers which round to 0.214.

### Q32
(i)

The 40 residents are a random sample, so they are independent, each with the same probability 0.85 of being familiar with the rules, and $X$, the number who are, follows a binomial distribution

`X \sim \text{B}(40, \; 0.85)`

Fewer than 38 means $X \leq 37$. The upper tail $X = 38$, 39, 40 is much shorter, so subtract it from 1

`\text{P}(X < 38) = 1 - \left[\text{P}(X = 38) + \text{P}(X = 39) + \text{P}(X = 40)\right]`

`\text{P}(X < 38) = 1 - \left[{}^{40}C_{38}\left(0.85\right)^{38}\left(0.15\right)^{2} + {}^{40}C_{39}\left(0.85\right)^{39}(0.15) + \left(0.85\right)^{40}\right]`

**[M1]**

$\text{P} ( X < 38 ) = 1 - ( 0 . 0364918 \dots + 0 . 0106044 \dots + 0 . 0015023 \dots ) = 1 - 0 . 0485986 \dots$

**Final answer:** $\text{P} ( X < 38 ) = 0 . 951$** (3 s.f.)**

**[A1]**

(ii)

No more than 38 means $X \leq 38$, so only $X = 39$ and $X = 40$ are excluded

$\text{P} ( X \leq 38 ) = 1 - ( 0 . 0106044 \dots + 0 . 0015023 \dots ) = 1 - 0 . 0121067 \dots = 0 . 987893 \dots$

**Final answer:** $\text{P} ( X \leq 38 ) = 0 . 988$** (3 s.f.)**

**[B1]**

(iii)

More than 38 means $X = 39$ or $X = 40$, the two terms just excluded in (ii)

$\text{P} ( X > 38 ) = 0 . 0106044 \dots + 0 . 0015023 \dots = 0 . 0121067 \dots$

**Final answer:** $\text{P} ( X > 38 ) = 0 . 0121$** (3 s.f.)**

**[B1]**

(iv)

At least 36 but at most 38 means $X = 36$, 37 or 38

`\text{P}(36 \leq X \leq 38) = {}^{40}C_{36}\left(0.85\right)^{36}\left(0.15\right)^{4} + {}^{40}C_{37}\left(0.85\right)^{37}\left(0.15\right)^{3} + {}^{40}C_{38}\left(0.85\right)^{38}\left(0.15\right)^{2}`

$\text{P} ( 36 \leq X \leq 38 ) = 0 . 251213 \dots$

**Final answer:** $\text{P} ( 36 \leq X \leq 38 ) = 0 . 251$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(X < 38): 1 minus the terms for 38, 39 and 40, or the sum of the terms from 0 to 37. Accept unsimplified.
> 
> **A1**: 0.951, or answers which round to 0.951.
> 
> **B1**: P(X ≤ 38) = 0.988, or answers which round to 0.988.
> 
> **B1**: P(X > 38) = 0.0121, or answers which round to 0.0121.
> 
> **B1**: P(36 ≤ X ≤ 38) = 0.251, or answers which round to 0.251.
> 
> If 0.951 is given with no working, for example straight from a calculator, award 1 mark only.

### Q33
(i)

The 40 seeds are independent, each with the same probability 0.15 of failing to germinate, so $X$ follows a binomial distribution

`X \sim \text{B}(40, \; 0.15)`

Use $\text{E} ( X ) = n p$

$\text{E} ( X ) = 40 \times 0 . 15$

$\text{E} ( X ) = 6$

**[B1]**

(ii)

Use $\text{Var} ( X ) = n p ( 1 - p )$

$\text{Var} ( X ) = 40 \times 0 . 15 \times 0 . 85$

$\text{Var} ( X ) = 5 . 1$

**[B1]**

> **[mark-scheme]**
> **B1**: E(X) = 6.
> 
> **B1**: Var(X) = 5.1.
(i)

Use `\text{P}(X = r) = {}^{n}C_{r} \, p^{r}\left(1 - p\right)^{n - r}` with $r = 5$

`\text{P}(X = 5) = {}^{40}C_{5}\left(0.15\right)^{5}\left(0.85\right)^{35}`

**[M1]**

$\text{P} ( X = 5 ) = 0 . 169180 \dots$

**Final answer:** $\text{P} ( X = 5 ) = 0 . 169$** (3 s.f.)**

**[A1]**

(ii)

At least 3 is every outcome except $X = 0$, 1 or 2, so subtract those three terms from 1

`\text{P}(X \geq 3) = 1 - \left[\left(0.85\right)^{40} + {}^{40}C_{1}(0.15)\left(0.85\right)^{39} + {}^{40}C_{2}\left(0.15\right)^{2}\left(0.85\right)^{38}\right]`

**[M1]**

$\text{P} ( X \geq 3 ) = 1 - 0 . 0485986 \dots = 0 . 951401 \dots$

**Final answer:** $\text{P} ( X \geq 3 ) = 0 . 951$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: `{}^{40}C_{5}\left(0.15\right)^{5}\left(0.85\right)^{35}`.
> 
> **A1**: 0.169, or answers which round to 0.169.
> 
> **M1**: 1 − [P(0) + P(1) + P(2)], with all three terms correct. Accept unsimplified.
> 
> **A1**: 0.951, or answers which round to 0.951.
> 
> If 0.169 or 0.951 is given with no working, for example straight from a calculator, award 1 mark only for that answer.
Use the definition of conditional probability

`\text{P}(X = 5 \mid X \geq 3) = \dfrac{\text{P}(X = 5 \cap X \geq 3)}{\text{P}(X \geq 3)}`

$X = 5$ already satisfies $X \geq 3$, so the numerator is just $\text{P} ( X = 5 )$. Use the unrounded answers to (b)

`\text{P}(X = 5 \mid X \geq 3) = \dfrac{0.169180\ldots}{0.951401\ldots}`

**[M1]**

`\text{P}(X = 5 \mid X \geq 3) = 0.177822\ldots`

**Final answer:** `\text{P}(X = 5 \mid X \geq 3) = 0.178`** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: P(X = 5) divided by P(X ≥ 3), using the answers to (b) or correct values. Both numerator and denominator must be seen.
> 
> **A1**: 0.178, or answers which round to 0.178.
