# Mark Schemes — Poisson Distribution
**Statistical Distributions** · Cambridge (CIE) A-LEVEL maths (9709)


## Exam Questions (27 questions)


### Q1
State two of the Poisson conditions (randomly, independently, singly, at a constant average rate) in context

**Final answer:** **The smoke detector rings at random and independently, so one ring does not affect when the next happens**

**[B1]**

**Final answer:** **The smoke detector rings at a constant average rate throughout the day**

**[B1]**

> **[mark-scheme]**
> **B1**: One correct condition, in context. For example, the rings occur independently, or at random, or singly (one at a time), or at a constant average rate.
> 
> **B1**: A second, different correct condition, in context.
> 
> A rate condition must say "mean" or "rate". Two correct conditions that do not mention the smoke detector or its rings score 1 mark only.
(i)

Let $X$ be the number of rings in a day

`X \sim \text{Po}(5)`

Find the probability of exactly 3 rings on one day

$\text{P} ( X = 3 ) = \text{e}^{-5} \frac{5^{3}}{3!} = 0 . 140373 \dots$

The 4 days are independent, so multiply this probability 4 times

`\left(\text{e}^{-5}\dfrac{5^{3}}{3!}\right)^{4}`

**[M1]**

$= 0 . 000388280 \dots$

**Final answer:** $0 . 000388$** (3 s.f.)**

**[A1]**

(ii)

The mean for 4 days is 4 times the daily mean

$λ = 5 \times 4 = 20$

**[B1]**

Let $Y$ be the number of rings in 4 days

`Y \sim \text{Po}(20)`

To find the probability, use $\text{P} ( Y = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $r = 12$

$\text{P} ( Y = 12 ) = \text{e}^{-20} \frac{20^{12}}{12!}$

**[M1]**

$\text{P} ( Y = 12 ) = 0 . 0176251 \dots$

**Final answer:** $\text{P} ( Y = 12 ) = 0 . 0176$** (3 s.f.)**

**[A1]**

(iii)

Compare which outcomes each part counts

**Final answer:** **In (i) the 12 rings must be split as 3, 3, 3, 3, which is only one of the many ways of getting 12 rings in 4 days (for example 12, 0, 0, 0 or 5, 4, 2, 1), so (i) is part of (ii) and its probability is smaller**

**[B1]**

> **[mark-scheme]**
> **M1**: `\left(\text{P}(X = 3)\right)^{4}` with P(X = 3) from Po(5) written as an expression. Allow any λ.
> 
> **A1**: 0.000388, or answers which round to 0.000388. Accept $3 . 88 \times 10^{-4}$.
> 
> **B1**: λ = 20 for 4 days, seen or implied.
> 
> **M1**: A correct expression for P(Y = 12) with any λ.
> 
> **A1**: 0.0176, or answers which round to 0.0176.
> 
> **B1**: (i) is only one particular way of getting a total of 12 rings, while (ii) includes every way of getting a total of 12. Accept "(i) is a subset of (ii)" or an example of another split. "One is per day and one is in total" alone does not score.
6 hours is $\frac{6}{24}$ of a day, so scale the daily mean to find the mean number of rings in 6 hours

$λ = 5 \times \frac{6}{24} = 1 . 25$

**[B1]**

Let $W$ be the number of rings in 6 hours

`W \sim \text{Po}(1.25)`

Use the conditional probability formula

`\text{P}(W \leq 4 \mid W \geq 1) = \dfrac{\text{P}(W \leq 4 \text{ and } W \geq 1)}{\text{P}(W \geq 1)} = \dfrac{\text{P}(1 \leq W \leq 4)}{\text{P}(W \geq 1)}`

Find the numerator: $W = 1 ,  2 ,  3 \text{or} 4$

`\text{P}(1 \leq W \leq 4) = \text{e}^{-1.25}\left(1.25 + \dfrac{1.25^{2}}{2!} + \dfrac{1.25^{3}}{3!} + \dfrac{1.25^{4}}{4!}\right) = 0.704370\ldots`

**[M1]**

Find the denominator, then divide

$\text{P} ( W \geq 1 ) = 1 - \text{e}^{-1.25} = 0 . 713495 \dots$

`\text{P}(W \leq 4 \mid W \geq 1) = \dfrac{0.704370\ldots}{0.713495\ldots}`

**[M1]**

$= 0 . 987211 \dots$

**Final answer:** `\text{P}(W \leq 4 \mid W \geq 1) = 0.987`** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = 1.25 for 6 hours, seen or implied.
> 
> **M1**: P(1) + P(2) + P(3) + P(4) written out with any λ, or P(W ≤ 4) − P(W = 0). Allow one term missing or one extra term.
> 
> **M1**: The numerator divided by P(W ≥ 1) = $1 - \text{e}^{-λ}$.
> 
> **A1**: 0.987, or answers which round to 0.987.
> 
> Using P(W ≤ 4) (including W = 0) as the numerator scores the second M1 but not the A1.

### Q2
(i)

Write each probability using $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$

$\text{e}^{-α} \frac{α^{4}}{4!} = \text{e}^{-α} \frac{α^{2}}{2!} + \text{e}^{-α} \frac{α^{3}}{3!}$

Divide every term by $\text{e}^{-α} α^{2}$, which is not zero

$\frac{α^{2}}{24} = \frac{1}{2} + \frac{α}{6}$

**[M1]**

Multiply by 24 and rearrange to a quadratic equal to zero

$α^{2} - 4 α - 12 = 0$

**[M1]**

Factorise

$( α - 6 ) ( α + 2 ) = 0$

$α = 6$* or *$α = - 2$

$α$ is the mean of a Poisson distribution, so it must be positive; reject $α = - 2$

$α = 6$

**[A1]**

(ii)

"At least 1" is every outcome except $Y = 0$

$1 - \text{e}^{-β} = 0 . 314$

$\text{e}^{-β} = 0 . 686$

Take natural logarithms of both sides

`-\beta = \text{ln}\left(0.686\right)`

**[M1]**

`\beta = -\text{ln}\left(0.686\right) = 0.376877\ldots`

**Final answer:** $β = 0 . 377$** (3 s.f.)**

**[A1]**

(iii)

Write each probability using the Poisson formula

$\text{e}^{-γ} \frac{γ^{k+1}}{(k+1)!} = \text{e}^{-γ} \frac{γ^{k-1}}{(k-1)!}$

Divide both sides by $\text{e}^{-γ} γ^{k-1}$, which is not zero

$\frac{γ^{2}}{(k+1)!} = \frac{1}{(k-1)!}$

Multiply both sides by $( k + 1 ) !$, using $( k + 1 ) ! = ( k + 1 ) \times k \times ( k - 1 ) !$

$γ^{2} = \frac{(k+1)!}{(k-1)!} = k ( k + 1 )$

**[M1]**

$γ$ is a mean, so take the positive square root

$γ = \sqrt{k(k+1)}$

**[A1]**

> **[mark-scheme]**
> **M1**: Equating the Poisson expressions and cancelling $\text{e}^{-α}$ to reach an equation in α only.
> 
> **M1**: A correct three-term quadratic, $α^{2} - 4 α - 12 = 0$ or equivalent.
> 
> **A1**: α = 6 only, with −2 rejected.
> 
> **M1**: $\text{e}^{-β} = 0 . 686$ with logarithms taken, `-\beta = \text{ln}\left(0.686\right)` or equivalent.
> 
> **A1**: β = 0.377, or answers which round to 0.377. Accept `\text{ln}\left(\dfrac{500}{343}\right)`.
> 
> **M1**: $γ^{2} = k ( k + 1 )$, or $γ^{2} = \frac{(k+1)!}{(k-1)!}$.
> 
> **A1**: $γ = \sqrt{k(k+1)}$ or $\sqrt{k^{2}+k}$. A ± answer does not earn this mark.

### Q3
(i)

Let $X$ be the number of hits on a square

`X \sim \text{Po}\left(\dfrac{537}{576}\right)`

To find each probability from 0 to 4, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $λ = 0 . 932291 \dots$

$\text{P} ( X = 0 ) = \text{e}^{-λ} = 0 . 393650 \dots$

$\text{P} ( X = 1 ) = \text{e}^{-λ} λ = 0 . 366997 \dots$

**[M1]**

$\text{P} ( X = 2 ) = \text{e}^{-λ} \frac{λ^{2}}{2!} = 0 . 171074 \dots$

$\text{P} ( X = 3 ) = \text{e}^{-λ} \frac{λ^{3}}{3!} = 0 . 0531636 \dots$

$\text{P} ( X = 4 ) = \text{e}^{-λ} \frac{λ^{4}}{4!} = 0 . 0123910 \dots$

**[A1]**

"5 or more" is every outcome not already counted, so subtract the sum of the others from 1

`\text{P}(X \geq 5) = 1 - \left(\text{P}(X = 0) + \text{P}(X = 1) + \text{P}(X = 2) + \text{P}(X = 3) + \text{P}(X = 4)\right) = 0.00272335\ldots`

**[B1]**

The expected number of squares for each value is 576 times its probability

$576 \times 0 . 393650 \dots = 226 . 74 \dots$

**[M1]**

Do the same for each row

| **Number of hits** | **Probability** | **Expected number of squares** | **Actual number of squares** |
|---|---|---|---|
| 0 | 0.3937 | **Final answer:** **226.7** | 229 |
| 1 | 0.3670 | **Final answer:** **211.4** | 211 |
| 2 | 0.1711 | **Final answer:** **98.5** | 93 |
| 3 | 0.0532 | **Final answer:** **30.6** | 35 |
| 4 | 0.0124 | **Final answer:** **7.1** | 7 |
| 5 or more | 0.0027 | **Final answer:** **1.6** | 1 |

**[A1]**

(ii)

Compare the expected and actual numbers row by row: they are very close in every row (for example 211.4 and 211 for one hit, 7.1 and 7 for four hits)

**Final answer:** **The expected numbers are very close to the actual numbers, so Roger's model is appropriate**

**[B1]**

> **[mark-scheme]**
> **M1**: Correct use of the Poisson formula with λ = $\frac{537}{576}$ for at least two of the probabilities.
> 
> **A1**: All of P(X = 0) to P(X = 4) correct, to 3 s.f. or better.
> 
> **B1**: P(X ≥ 5) found as 1 minus the sum of the other five probabilities (0.00272).
> 
> **M1**: Multiplying the probabilities by 576.
> 
> **A1**: All six expected numbers correct: 226.7, 211.4, 98.5, 30.6, 7.1, 1.6 (accept whole numbers 227, 211, 99, 31, 7, 2).
> 
> **B1**: A comparison showing the expected and actual numbers are close, with the conclusion that the model is appropriate. Both the comparison and the conclusion are needed.

### Q4
The rate is constant, so in $n$ words the mean number of mistakes is

$λ = \frac{7n}{150}$

**[B1]**

"At least one mistake" is every outcome except none, so its probability is $1 - \text{e}^{-λ}$; this must not exceed 0.75

$1 - \text{e}^{-\frac{7n}{150}} \leq 0 . 75$

**[M1]**

Rearrange to make the exponential the subject

$\text{e}^{-\frac{7n}{150}} \geq 0 . 25$

Take natural logarithms of both sides

`-\dfrac{7n}{150} \geq \text{ln}\left(0.25\right)`

**[M1]**

Multiply by $- \frac{150}{7}$, which reverses the inequality

`n \leq -\dfrac{150}{7}\,\text{ln}\left(0.25\right) = 29.706\ldots`

$n$ is a whole number of words, so take the largest whole number below 29.706

**Final answer:** **29 words**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = $\frac{7n}{150}$, seen or implied.
> 
> **M1**: $1 - \text{e}^{-λ} \leq 0 . 75$ or $\text{e}^{-λ} \geq 0 . 25$ with any λ in terms of n. Condone "=" throughout.
> 
> **M1**: Logarithms taken correctly, `-\lambda = \text{ln}\left(0.25\right)` or `\lambda = \text{ln}\left(4\right)` or equivalent.
> 
> **A1**: 29. Accept n = 29 or n ≤ 29. Do not accept 29.7, n < 29, or 30.
> 
> Alternative method: trying n = 29 (probability 0.742) and n = 30 (probability 0.753) and concluding 29 scores full marks.
Find the mean number of mistakes in each essay, using 7 per 150 words

$λ_{1} = \frac{7\times100}{150} = \frac{14}{3}$

$λ_{2} = \frac{7\times200}{150} = \frac{28}{3}$

$λ_{3} = \frac{7\times250}{150} = \frac{35}{3}$

**[B1]**

1% of 100, 200 and 250 words is 1, 2 and 2.5. The number of mistakes is a whole number, so "more than 1, 2 and 2.5" means at least 2, 3 and 3. Let $X$, $Y$ and $Z$ be the numbers of mistakes in the three essays

$X \geq 2$*, *$Y \geq 3$* and *$Z \geq 3$

**[B1]**

Each probability is 1 minus the terms below the threshold

`\text{P}(X \geq 2) = 1 - \text{e}^{-\frac{14}{3}}\left(1 + \dfrac{14}{3}\right) = 0.946713\ldots`

**[M1]**

`\text{P}(Y \geq 3) = 1 - \text{e}^{-\frac{28}{3}}\left(1 + \dfrac{28}{3} + \dfrac{\left(\frac{28}{3}\right)^{2}}{2!}\right) = 0.995234\ldots`

`\text{P}(Z \geq 3) = 1 - \text{e}^{-\frac{35}{3}}\left(1 + \dfrac{35}{3} + \dfrac{\left(\frac{35}{3}\right)^{2}}{2!}\right) = 0.999307\ldots`

**[A1]**

The essays are independent, so multiply the three probabilities

$0 . 946713 \dots \times 0 . 995234 \dots \times 0 . 999307 \dots$

**[M1]**

$= 0 . 941549 \dots$

**Final answer:** $\text{P} ( \text{all three returned} ) = 0 . 942$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: All three means, $\frac{14}{3}$, $\frac{28}{3}$ and $\frac{35}{3}$, seen or implied. Accept 4.67, 9.33 and 11.7 or better.
> 
> **B1**: The thresholds X ≥ 2, Y ≥ 3 and Z ≥ 3, seen or implied. In particular, more than 2.5 mistakes means at least 3.
> 
> **M1**: At least one tail probability written out as 1 minus Poisson terms, with any λ. Allow one term missing or one extra term.
> 
> **A1**: All three tail probabilities correct: 0.947, 0.995 and 0.999 (or better).
> 
> **M1**: The product of the three tail probabilities.
> 
> **A1**: 0.942, or answers which round to 0.942.

### Q5
The two probabilities can only be multiplied if the two students' mistakes are independent

**Final answer:** **Priya and Qays make their mistakes independently of each other**

**[B1]**

Scale each mean to 1 hour: three 20-minute periods for Priya, two 30-minute periods for Qays

$λ_{P} = 1 . 2 \times 3 = 3 . 6$

$λ_{Q} = 2 . 2 \times 2 = 4 . 4$

**[B1]**

With `X \sim \text{Po}(3.6)` and `Y \sim \text{Po}(4.4)` the numbers of mistakes in an hour, multiply the two Poisson probabilities

$\text{P} ( X = 2 ) \times \text{P} ( Y = 1 ) = \text{e}^{-3.6} \frac{3.6^{2}}{2!} \times \text{e}^{-4.4} \frac{4.4^{1}}{1!}$

**[M1]**

Combine the exponentials, $\text{e}^{-3.6} \times \text{e}^{-4.4} = \text{e}^{-8}$, and write $3 . 6 = \frac{18}{5}$ and $4 . 4 = \frac{22}{5}$

`= \dfrac{1}{2}\left(\dfrac{18}{5}\right)^{2} \times \dfrac{22}{5} \times \text{e}^{-8}`

$= \frac{324}{50} \times \frac{22}{5} \times \text{e}^{-8}$

$\frac{3564}{125} \text{e}^{-8}$

**[A1]**

> **[mark-scheme]**
> **B1**: The numbers of mistakes made by Priya and Qays are independent (in context).
> 
> **B1**: Both hourly means, 3.6 and 4.4, seen or implied.
> 
> **M1**: The product of two Poisson expressions, P(X = 2) × P(Y = 1), with any λ.
> 
> **A1**: $\frac{3564}{125} \text{e}^{-8}$, or a = 3564, b = 125, c = −8. Accept an equivalent integer fraction such as $\frac{7128}{250} \text{e}^{-8}$. A decimal coefficient (28.512) or a decimal answer (0.00956) does not earn this mark.
Use the conditional probability formula. If the total is 9 and Priya makes 5, then Qays makes 4

`\text{P}(X = 5 \mid X + Y = 9) = \dfrac{\text{P}(X = 5 \text{ and } Y = 4)}{\text{P}(X + Y = 9)}`

Find the numerator, using independence

$\text{P} ( X = 5 ) \times \text{P} ( Y = 4 ) = \text{e}^{-3.6} \frac{3.6^{5}}{5!} \times \text{e}^{-4.4} \frac{4.4^{4}}{4!} = 0 . 0263982 \dots$

**[M1]**

The sum of independent Poisson variables is Poisson with the means added, so `X + Y \sim \text{Po}(8)`

$\text{P} ( X + Y = 9 ) = \text{e}^{-8} \frac{8^{9}}{9!} = 0 . 124076 \dots$

**[M1]**

Divide

`\text{P}(X = 5 \mid X + Y = 9) = \dfrac{0.0263982\ldots}{0.124076\ldots}`

**[M1]**

$= 0 . 212757 \dots$

**Final answer:** `\text{P}(X = 5 \mid X + Y = 9) = 0.213`** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: P(X = 5) × P(Y = 4) written as Poisson expressions, with any λ.
> 
> **M1**: P(X + Y = 9) using the combined mean 8.
> 
> **M1**: The numerator divided by P(X + Y = 9). Cancelling the exponentials first, $\frac{\frac{3.6^{5}}{5!}\times\frac{4.4^{4}}{4!}}{\frac{8^{9}}{9!}}$, scores all three method marks.
> 
> **A1**: 0.213, or answers which round to 0.213.
> 
> Alternative method: X given X + Y = 9 is B(9, 0.45), since 3.6 ÷ 8 = 0.45; `{}^{9}C_{5}(0.45)^{5}(0.55)^{4}` scores M1 M1 M1, then A1 for 0.213.
If Priya makes 5 and the total is 9, then Qays makes 4. Use the conditional probability formula

`\text{P}(X + Y = 9 \mid X = 5) = \dfrac{\text{P}(X = 5 \text{ and } Y = 4)}{\text{P}(X = 5)} = \dfrac{\text{P}(X = 5) \times \text{P}(Y = 4)}{\text{P}(X = 5)}`

$\text{P} ( X = 5 )$ cancels, because $X$ and $Y$ are independent

`\text{P}(X + Y = 9 \mid X = 5) = \text{P}(Y = 4) = \text{e}^{-4.4}\dfrac{4.4^{4}}{4!}`

**[M1]**

$= 0 . 191736 \dots$

**Final answer:** `\text{P}(X + Y = 9 \mid X = 5) = 0.192`** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: Recognising that the probability is P(Y = 4), written as a Poisson expression with λ = 4.4, or the ratio P(X = 5 and Y = 4) ÷ P(X = 5).
> 
> **A1**: 0.192, or answers which round to 0.192.
30 minutes is 1.5 twenty-minute periods, so scale Priya's mean to find her mean number of mistakes in 30 minutes

$λ = 1 . 2 \times 1 . 5 = 1 . 8$

**[B1]**

With `W \sim \text{Po}(1.8)` her number of mistakes in 30 minutes, the expected number of periods is 10 times $\text{P} ( W \geq 1 )$

`10 \times \text{P}(W \geq 1) = 10 \times \left(1 - \text{e}^{-1.8}\right)`

**[M1]**

$= 10 \times 0 . 834701 \dots = 8 . 347 \dots$

A number of revision periods is a whole number

**Final answer:** **8 revision periods**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = 1.8 for 30 minutes, seen or implied.
> 
> **M1**: 10 × (1 − e^−λ), with any λ.
> 
> **A1**: 8 revision periods. Accept 8.35 seen in the working followed by 8. A decimal final answer, or "about 8", does not score. Using P(W = 1) (exactly one mistake) scores M0.

### Q6
(i)

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $λ = 6$ and $r = 3$

$\text{P} ( X = 3 ) = \text{e}^{-6} \frac{6^{3}}{3!}$

**[M1]**

Simplify the fraction, since $6^{3} = 216$ and $3 ! = 6$

$\frac{6^{3}}{3!} = \frac{216}{6} = 36$

$\text{P} ( X = 3 ) = 36 \text{e}^{-6}$

**[A1]**

(ii)

Use the formula with $r = 4$

$\text{P} ( X = 4 ) = \text{e}^{-6} \frac{6^{4}}{4!}$

$\frac{6^{4}}{4!} = \frac{1296}{24} = 54$

$\text{P} ( X = 4 ) = 54 \text{e}^{-6}$

**[A1]**

(iii)

Use the formula with $r = 5$

$\text{P} ( X = 5 ) = \text{e}^{-6} \frac{6^{5}}{5!}$

$\frac{6^{5}}{5!} = \frac{7776}{120} = \frac{324}{5}$

$\text{P} ( X = 5 ) = \frac{324}{5} \text{e}^{-6}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the Poisson formula with λ = 6 for any one of the three probabilities.
> 
> **A1**: P(X = 3) = $36 \text{e}^{-6}$.
> 
> **A1**: P(X = 4) = $54 \text{e}^{-6}$.
> 
> **A1**: P(X = 5) = $\frac{324}{5} \text{e}^{-6}$. Accept $64 . 8 \text{e}^{-6}$.
> 
> The answers must be exact, in terms of e. A decimal answer alone does not earn the A1 for that sub-part.
(i)

Multiply the answer to (a)(i) by $\frac{6}{4}$

$\frac{6}{4} \text{P} ( X = 3 ) = \frac{6}{4} \times 36 \text{e}^{-6}$

$\frac{6}{4} \text{P} ( X = 3 ) = 54 \text{e}^{-6}$

**[B1]**

(ii)

Multiply the answer to (a)(ii) by $\frac{6}{5}$

$\frac{6}{5} \text{P} ( X = 4 ) = \frac{6}{5} \times 54 \text{e}^{-6}$

$\frac{6}{5} \text{P} ( X = 4 ) = \frac{324}{5} \text{e}^{-6}$

**[B1]**

> **[mark-scheme]**
> **B1**: $54 \text{e}^{-6}$. Follow through $\frac{6}{4}$ times your answer to (a)(i).
> 
> **B1**: $\frac{324}{5} \text{e}^{-6}$, or $64 . 8 \text{e}^{-6}$. Follow through $\frac{6}{5}$ times your answer to (a)(ii).
Comparing (a) and (b), multiplying each probability by $\frac{6}{k+1}$ gives the next probability along

$\frac{6}{4} \text{P} ( X = 3 ) = \text{P} ( X = 4 )$

$\frac{6}{5} \text{P} ( X = 4 ) = \text{P} ( X = 5 )$

So the pattern is

$\frac{6}{k+1} \text{P} ( X = k ) = \text{P} ( X = k + 1 )$

Write $\text{P} ( X = k + 1 )$ using the Poisson formula with $r = k + 1$

$\frac{6}{k+1} \text{P} ( X = k ) = \text{e}^{-6} \frac{6^{k+1}}{(k+1)!}$

**[B1]**

> **[exam-tip]**
> The same pattern holds for any Poisson distribution: if `X \sim \text{Po}(\lambda)`, then $\text{P} ( X = k + 1 ) = \frac{λ}{k+1} \text{P} ( X = k )$. It is a quick way to build a list of probabilities one term at a time, each from the one before.

> **[mark-scheme]**
> **B1**: $\text{e}^{-6} \frac{6^{k+1}}{(k+1)!}$. Accept $\text{P} ( X = k + 1 )$.

### Q7
For independent Poisson variables, add the means: if `X \sim \text{Po}(\lambda)` and `Y \sim \text{Po}(\mu)` are independent, then

`X + Y \sim \text{Po}(\lambda + \mu)`

(i)

$2 + 3 = 5$

`R + S \sim \text{Po}(5)`

**[B1]**

(ii)

$3 + 4 = 7$

`S + T \sim \text{Po}(7)`

**[B1]**

> **[mark-scheme]**
> **B1**: R + S ~ Po(5). Accept "Poisson with mean 5".
> 
> **B1**: S + T ~ Po(7). Accept "Poisson with mean 7".
(i)

$R$ and $T$ are independent Poisson variables, so add their means

$2 + 4 = 6$

`R + T \sim \text{Po}(6)`

**[B1]**

(ii)

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $λ = 6$ and $r = 5$

$\text{P} ( R + T = 5 ) = \text{e}^{-6} \frac{6^{5}}{5!}$

**[M1]**

$\text{P} ( R + T = 5 ) = 0 . 160623 \dots$

**Final answer:** $\text{P} ( R + T = 5 ) = 0 . 161$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: R + T ~ Po(6). Accept "Poisson with mean 6".
> 
> **M1**: A correct expression for P(X = 5) with λ = 6, $\text{e}^{-6} \frac{6^{5}}{5!}$. Follow through your mean from (i).
> 
> **A1**: P(R + T = 5) = 0.161, or answers which round to 0.161. Accept $\frac{324}{5} \text{e}^{-6}$.
> 
> Adding the probabilities P(R = …) and P(T = …) instead of the means scores M0.

### Q8
For `X \sim \text{Po}(\lambda)` the mean and the variance are both equal to $λ$

$μ = λ$

$σ^{2} = λ$

The standard deviation is the square root of the variance

$σ = \sqrt{λ}$

(i)

$σ = \sqrt{4} = 2$

$μ = 4 ,  σ = 2$

**[B1]**

(ii)

$σ = \sqrt{1} = 1$

$μ = 1 ,  σ = 1$

**[B1]**

(iii)

$σ = \sqrt{5.4} = 2 . 32379 \dots$

**Final answer:** $μ = 5 . 4 ,  σ = 2 . 32$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **B1**: μ = 4 and σ = 2. Both values are needed.
> 
> **B1**: μ = 1 and σ = 1. Both values are needed.
> 
> **B1**: μ = 5.4 and σ = 2.32, or answers which round to 2.32. Accept $σ = \sqrt{5.4}$. Both values are needed.
> 
> A variance given in place of a standard deviation (for example σ = 4 in (i)) does not score.

### Q9
The constant average rate is given, so state two of the other Poisson conditions (randomly, independently, singly) in context

**Final answer:** **The emails arrive independently of each other**

**[B1]**

**Final answer:** **The emails arrive singly, so two never arrive at exactly the same time**

**[B1]**

> **[mark-scheme]**
> **B1**: One correct assumption, in context. For example, emails arrive independently, or emails arrive singly, or emails arrive at random.
> 
> **B1**: A second, different correct assumption, in context.
> 
> "At a constant average rate" is given in the question, so it is not credited as one of the two assumptions. Two correct assumptions that are not in context (for example "events are independent") score 1 mark only.
The rate is constant, so scale the mean of 10 per hour to find the mean number of emails in each period

(i)

$λ = 10 \times 2$

$λ = 20$

**[B1]**

(ii)

15 minutes is $\frac{15}{60}$ of an hour

$λ = 10 \times \frac{15}{60}$

$λ = 2 . 5$

**[B1]**

(iii)

One hour and 10 minutes is 70 minutes, which is $\frac{70}{60}$ of an hour

$λ = 10 \times \frac{70}{60} = \frac{35}{3}$

**Final answer:** $λ = 11 . 7$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **B1**: λ = 20.
> 
> **B1**: λ = 2.5.
> 
> **B1**: λ = 11.7, or answers which round to 11.7. Accept $\frac{35}{3}$.

### Q10
To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $r = 0$; since $λ^{0} = 1$ and $0 ! = 1$, this is just $\text{e}^{-λ}$

$\text{P} ( X = 0 ) = \text{e}^{-λ} \frac{λ^{0}}{0!} = \text{e}^{-λ}$

(i)

$\text{P} ( X = 0 ) = \text{e}^{-7} = 0 . 000911882 \dots$

**Final answer:** $\text{P} ( X = 0 ) = 0 . 000912$** (3 s.f.)**

**[B1]**

(ii)

$\text{P} ( X = 0 ) = \text{e}^{-2.5} = 0 . 0820849 \dots$

**Final answer:** $\text{P} ( X = 0 ) = 0 . 0821$** (3 s.f.)**

**[B1]**

(iii)

$\text{P} ( X = 0 ) = \text{e}^{-0.01} = 0 . 990049 \dots$

**Final answer:** $\text{P} ( X = 0 ) = 0 . 990$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **B1**: P(X = 0) = 0.000912 when λ = 7, or answers which round to 0.000912. Accept $\text{e}^{-7}$.
> 
> **B1**: P(X = 0) = 0.0821 when λ = 2.5, or answers which round to 0.0821. Accept $\text{e}^{-2.5}$.
> 
> **B1**: P(X = 0) = 0.990 when λ = 0.01, or answers which round to 0.990. Accept $\text{e}^{-0.01}$.
To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $r = 1$; since $λ^{1} = λ$ and $1 ! = 1$, this is $λ \text{e}^{-λ}$

$\text{P} ( X = 1 ) = \text{e}^{-λ} \frac{λ^{1}}{1!} = λ \text{e}^{-λ}$

(i)

$\text{P} ( X = 1 ) = 7 \text{e}^{-7} = 0 . 00638317 \dots$

**Final answer:** $\text{P} ( X = 1 ) = 0 . 00638$** (3 s.f.)**

**[B1]**

(ii)

$\text{P} ( X = 1 ) = 2 . 5 \text{e}^{-2.5} = 0 . 205212 \dots$

**Final answer:** $\text{P} ( X = 1 ) = 0 . 205$** (3 s.f.)**

**[B1]**

(iii)

$\text{P} ( X = 1 ) = 0 . 01 \text{e}^{-0.01} = 0 . 00990049 \dots$

**Final answer:** $\text{P} ( X = 1 ) = 0 . 00990$** (3 s.f.)**

**[B1]**

> **[mark-scheme]**
> **B1**: P(X = 1) = 0.00638 when λ = 7, or answers which round to 0.00638. Accept $7 \text{e}^{-7}$.
> 
> **B1**: P(X = 1) = 0.205 when λ = 2.5, or answers which round to 0.205. Accept $2 . 5 \text{e}^{-2.5}$.
> 
> **B1**: P(X = 1) = 0.00990 when λ = 0.01, or answers which round to 0.00990. Accept $0 . 01 \text{e}^{-0.01}$.
(i)

Substitute $λ = k$ and $r = 0$ into $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$

$\text{P} ( X = 0 ) = \text{e}^{-k} \frac{k^{0}}{0!}$

Simplify using $k^{0} = 1$ and $0 ! = 1$

$\text{P} ( X = 0 ) = \text{e}^{-k}$

**[B1]**

(ii)

Substitute $λ = k$ and $r = 1$

$\text{P} ( X = 1 ) = \text{e}^{-k} \frac{k^{1}}{1!}$

Simplify using $k^{1} = k$ and $1 ! = 1$

$\text{P} ( X = 1 ) = k \text{e}^{-k}$

**[B1]**

> **[exam-tip]**
> It is worth knowing $\text{P} ( X = 0 ) = \text{e}^{-λ}$ and $\text{P} ( X = 1 ) = λ \text{e}^{-λ}$ by heart. They come up constantly, for example in "at least one" questions, where $\text{P} ( X \geq 1 ) = 1 - \text{e}^{-λ}$, and in questions that give you $\text{P} ( X = 0 )$ and ask you to find $λ$.

> **[mark-scheme]**
> **B1**: P(X = 0) = $\text{e}^{-k}$.
> 
> **B1**: P(X = 1) = $k \text{e}^{-k}$. Accept $\frac{k}{\text{e}^{k}}$.

### Q11
(i)

The possible values of $X$ are 0, 1, 2, 3, …, and these split into two groups: 0 to 7, which is $X \leq 7$, and 8 upwards, which is $X \geq 8$. Together the two groups cover every possible value exactly once, so their probabilities add to 1

$\text{P} ( X \leq 7 ) + \text{P} ( X \geq 8 ) = 1$

$\text{P} ( X \leq 7 ) = 1 - \text{P} ( X \geq 8 )$

$a = 8$

**[B1]**

(ii)

This time the values split into 0 to 2, which is $X \leq 2$, and 3 upwards, which is $X \geq 3$. Again the two groups cover every possible value exactly once

$\text{P} ( X \leq 2 ) + \text{P} ( X \geq 3 ) = 1$

$\text{P} ( X \geq 3 ) = 1 - \text{P} ( X \leq 2 )$

$b = 2$

**[B1]**

> **[mark-scheme]**
> **B1**: a = 8.
> 
> **B1**: b = 2.
(i)

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $λ = 5$ and $r = 4$

$\text{P} ( X = 4 ) = \text{e}^{-5} \frac{5^{4}}{4!}$

**[M1]**

$\text{P} ( X = 4 ) = 0 . 175467 \dots$

**Final answer:** $\text{P} ( X = 4 ) = 0 . 175$** (3 s.f.)**

**[A1]**

(ii)

$X \leq 2$ means $X = 0 ,  1 \text{or} 2$, so add those three terms

$\text{P} ( X \leq 2 ) = \text{P} ( X = 0 ) + \text{P} ( X = 1 ) + \text{P} ( X = 2 )$

$\text{P} ( X \leq 2 ) = \text{e}^{-5} \frac{5^{0}}{0!} + \text{e}^{-5} \frac{5^{1}}{1!} + \text{e}^{-5} \frac{5^{2}}{2!}$

**[M1]**

$\text{P} ( X \leq 2 ) = 0 . 124652 \dots$

**Final answer:** $\text{P} ( X \leq 2 ) = 0 . 125$** (3 s.f.)**

**[A1]**

(iii)

$X \geq 2$ is every outcome except $X = 0$ and $X = 1$, so subtract those two terms from 1

$\text{P} ( X \geq 2 ) = 1 - \text{P} ( X \leq 1 )$

`\text{P}(X \geq 2) = 1 - \left(\text{e}^{-5}\dfrac{5^{0}}{0!} + \text{e}^{-5}\dfrac{5^{1}}{1!}\right)`

**[M1]**

$\text{P} ( X \geq 2 ) = 0 . 959572 \dots$

**Final answer:** $\text{P} ( X \geq 2 ) = 0 . 960$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(X = 4), $\text{e}^{-5} \frac{5^{4}}{4!}$.
> 
> **A1**: P(X = 4) = 0.175, or answers which round to 0.175.
> 
> **M1**: P(0) + P(1) + P(2), with all three terms correct. Accept unsimplified, or `\text{e}^{-5}\left(1 + 5 + \dfrac{5^{2}}{2}\right)`.
> 
> **A1**: P(X ≤ 2) = 0.125, or answers which round to 0.125.
> 
> **M1**: 1 − (P(0) + P(1)), with both terms correct. Accept unsimplified.
> 
> **A1**: P(X ≥ 2) = 0.960, or answers which round to 0.960.
> 
> If 0.175, 0.125 or 0.960 is given with no working, for example straight from a calculator, award 1 mark only for that answer.

### Q12
(i)

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $λ = 3$ and $r = 5$

$\text{P} ( X = 5 ) = \text{e}^{-3} \frac{3^{5}}{5!}$

**[M1]**

Simplify the fraction, since $3^{5} = 243$ and $5 ! = 120$

$\frac{3^{5}}{5!} = \frac{243}{120} = \frac{81}{40}$

$\text{P} ( X = 5 ) = \frac{81}{40} \text{e}^{-3}$

**[A1]**

(ii)

$X \leq 1$ means $X = 0$ or $X = 1$, so add those two terms

$\text{P} ( X \leq 1 ) = \text{e}^{-3} \frac{3^{0}}{0!} + \text{e}^{-3} \frac{3^{1}}{1!}$

**[M1]**

Use $3^{0} = 1$ and $0 ! = 1 ! = 1$

$\text{P} ( X \leq 1 ) = \text{e}^{-3} + 3 \text{e}^{-3}$

$\text{P} ( X \leq 1 ) = 4 \text{e}^{-3}$

**[A1]**

(iii)

$X \geq 2$ is every outcome except $X \leq 1$, so subtract the answer to (ii) from 1

$\text{P} ( X \geq 2 ) = 1 - \text{P} ( X \leq 1 )$

$\text{P} ( X \geq 2 ) = 1 - 4 \text{e}^{-3}$

**[B1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(X = 5), $\text{e}^{-3} \frac{3^{5}}{5!}$.
> 
> **A1**: P(X = 5) = $\frac{81}{40} \text{e}^{-3}$, or an exact equivalent such as $2 . 025 \text{e}^{-3}$ or $\frac{243}{120} \text{e}^{-3}$.
> 
> **M1**: P(0) + P(1), with both terms correct. Accept unsimplified.
> 
> **A1**: P(X ≤ 1) = $4 \text{e}^{-3}$.
> 
> **B1**: P(X ≥ 2) = $1 - 4 \text{e}^{-3}$. Follow through 1 minus your answer to (ii).
> 
> The answers must be exact, in terms of e. A decimal answer alone (0.101, 0.199, 0.801) does not earn the final mark for that sub-part.

### Q13
(i)

Every term has a factor of $\text{e}^{-λ}$, so take it outside a bracket

`\text{e}^{-\lambda}\left(\dfrac{\lambda^{4}}{4!} + \dfrac{\lambda^{5}}{5!} + \dfrac{\lambda^{6}}{6!} + \dfrac{\lambda^{7}}{7!} + \dfrac{\lambda^{8}}{8!}\right)`

**[B1]**

(ii)

$\text{P} ( 4 \leq X \leq 8 )$ is the sum of the terms for $r = 4$ to $r = 8$, which is the expression in (i), so substitute $λ = 6 . 3$

`\text{P}(4 \leq X \leq 8) = \text{e}^{-6.3}\left(\dfrac{6.3^{4}}{4!} + \dfrac{6.3^{5}}{5!} + \dfrac{6.3^{6}}{6!} + \dfrac{6.3^{7}}{7!} + \dfrac{6.3^{8}}{8!}\right)`

**[M1]**

$\text{P} ( 4 \leq X \leq 8 ) = 0 . 688393 \dots$

**Final answer:** $\text{P} ( 4 \leq X \leq 8 ) = 0 . 688$** (3 s.f.)**

**[A1]**

> **[exam-tip]**
> When you add several Poisson probabilities with the same $λ$, take out the common factor $\text{e}^{-λ}$ first. You then only need $\text{e}^{-λ}$ once, and the bracket is quick to type into a calculator. This saves time on every "at most", "at least" and "between" question.

> **[mark-scheme]**
> **B1**: A correct factorised expression with $\text{e}^{-λ}$ outside the bracket. A factorisation that also takes out $λ^{4}$ or $\frac{λ^{4}}{4!}$ is also accepted.
> 
> **M1**: λ = 6.3 substituted into the factorised expression, or the sum of the five terms for r = 4 to 8 written out.
> 
> **A1**: P(4 ≤ X ≤ 8) = 0.688, or answers which round to 0.688.
> 
> If 0.688 is given with no working, for example straight from a calculator, award 1 mark only for (ii).
(i)

$X \leq 3$ means $X = 0 ,  1 ,  2 \text{or} 3$, so add those four terms of $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $λ = 6 . 3$

$\text{P} ( X \leq 3 ) = \text{e}^{-6.3} \frac{6.3^{0}}{0!} + \text{e}^{-6.3} \frac{6.3^{1}}{1!} + \text{e}^{-6.3} \frac{6.3^{2}}{2!} + \text{e}^{-6.3} \frac{6.3^{3}}{3!}$

**[M1]**

Take out the common factor $\text{e}^{-6.3}$

`\text{P}(X \leq 3) = \text{e}^{-6.3}\left(1 + 6.3 + \dfrac{6.3^{2}}{2} + \dfrac{6.3^{3}}{6}\right)`

$\text{P} ( X \leq 3 ) = 0 . 126373 \dots$

**Final answer:** $\text{P} ( X \leq 3 ) = 0 . 126$** (3 s.f.)**

**[A1]**

(ii)

$5 \leq X \leq 7$ means $X = 5 ,  6 \text{or} 7$, so add those three terms

$\text{P} ( 5 \leq X \leq 7 ) = \text{e}^{-6.3} \frac{6.3^{5}}{5!} + \text{e}^{-6.3} \frac{6.3^{6}}{6!} + \text{e}^{-6.3} \frac{6.3^{7}}{7!}$

**[M1]**

$\text{P} ( 5 \leq X \leq 7 ) = 0 . 454844 \dots$

**Final answer:** $\text{P} ( 5 \leq X \leq 7 ) = 0 . 455$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: P(0) + P(1) + P(2) + P(3), with all four terms correct. Accept unsimplified, or the factorised form `\text{e}^{-6.3}\left(1 + 6.3 + \dfrac{6.3^{2}}{2} + \dfrac{6.3^{3}}{6}\right)`.
> 
> **A1**: P(X ≤ 3) = 0.126, or answers which round to 0.126.
> 
> **M1**: P(5) + P(6) + P(7), with all three terms correct. Accept unsimplified, or the factorised form `\text{e}^{-6.3}\dfrac{6.3^{5}}{5!}\left(1 + \dfrac{6.3}{6} + \dfrac{6.3^{2}}{42}\right)`.
> 
> **A1**: P(5 ≤ X ≤ 7) = 0.455, or answers which round to 0.455.
> 
> If 0.126 or 0.455 is given with no working, for example straight from a calculator, award 1 mark only for that answer.

### Q14
(i)

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ for each side

$\text{e}^{-α} \frac{α^{3}}{3!} = \text{e}^{-α} \frac{α^{7}}{7!}$

Divide both sides by $\text{e}^{-α} α^{3}$, which is not zero

$\frac{1}{3!} = \frac{α^{4}}{7!}$

**[M1]**

Multiply both sides by $7 !$

$α^{4} = \frac{7!}{3!} = 4 \times 5 \times 6 \times 7 = 840$

**[M1]**

$α$ is a mean, so take the positive fourth root

`\alpha = \sqrt[4]{840} = 5.38356\ldots`

**Final answer:** $α = 5 . 38$** (3 s.f.)**

**[A1]**

(ii)

Use the formula with $r = 0$; since $β^{0} = 1$ and $0 ! = 1$, this is $\text{e}^{-β}$

$\text{e}^{-β} = 0 . 253$

Take natural logarithms of both sides

`-\beta = \text{ln}\left(0.253\right)`

**[M1]**

`\beta = -\text{ln}\left(0.253\right) = 1.37436\ldots`

**Final answer:** $β = 1 . 37$** (3 s.f.)**

**[A1]**

(iii)

For a Poisson distribution the mean and the variance are both equal to the parameter

$\text{E} ( Z ) = \text{Var} ( Z ) = γ$

Substitute into the given equation

$5 γ = γ^{2} - 6$

Rearrange to a quadratic equal to zero

$γ^{2} - 5 γ - 6 = 0$

**[M1]**

Factorise

$( γ - 6 ) ( γ + 1 ) = 0$

$γ = 6$* or *$γ = - 1$

$γ$ is the mean of a Poisson distribution, so it must be positive; reject $γ = - 1$

$γ = 6$

**[A1]**

> **[mark-scheme]**
> **M1**: Equating the two Poisson expressions and cancelling $\text{e}^{-α}$ to reach an equation in α only.
> 
> **M1**: $α^{4} = 840$, or $α^{4} = \frac{7!}{3!}$.
> 
> **A1**: α = 5.38, or answers which round to 5.38. Accept `\sqrt[4]{840}`.
> 
> **M1**: $\text{e}^{-β} = 0 . 253$ with logarithms taken, `-\beta = \text{ln}\left(0.253\right)` or equivalent.
> 
> **A1**: β = 1.37, or answers which round to 1.37. Accept `\text{ln}\left(\dfrac{1000}{253}\right)`.
> 
> **M1**: Using E(Z) = Var(Z) = γ to form a correct quadratic, $γ^{2} - 5 γ - 6 = 0$ or equivalent.
> 
> **A1**: γ = 6 only, with γ = −1 rejected. Giving both values does not earn this mark.

### Q15
For a Poisson distribution the mean equals the variance, and the variance is the square of the standard deviation

$\text{E} ( X ) = \text{Var} ( X ) = 2 . 25^{2}$

$\text{E} ( X ) = 5 . 0625$

**[B1]**

> **[mark-scheme]**
> **B1**: E(X) = 5.0625. Accept $\frac{81}{16}$ or 5.06. An answer of 2.25 or 1.5 does not score.
So `X \sim \text{Po}(5.0625)`. To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $r = 4$

$\text{P} ( X = 4 ) = \text{e}^{-5.0625} \frac{5.0625^{4}}{4!}$

**[M1]**

$\text{P} ( X = 4 ) = 0 . 173233 \dots$

**Final answer:** $\text{P} ( X = 4 ) = 0 . 173$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(X = 4) with any λ. Follow through your E(X) from (a).
> 
> **A1**: 0.173, or answers which round to 0.173.
> 
> If 0.173 is given with no working, for example straight from a calculator, award 1 mark only.
$X$ is discrete and takes only whole-number values, so the whole numbers from 1.5 up to (but not including) 5 are 2, 3 and 4

$\text{P} ( 1 . 5 \leq X < 5 ) = \text{P} ( X = 2 ) + \text{P} ( X = 3 ) + \text{P} ( X = 4 )$

**[B1]**

Write out each term with $λ = 5 . 0625$

`\text{P}(1.5 \leq X < 5) = \text{e}^{-5.0625}\left(\dfrac{5.0625^{2}}{2!} + \dfrac{5.0625^{3}}{3!} + \dfrac{5.0625^{4}}{4!}\right)`

**[M1]**

$\text{P} ( 1 . 5 \leq X < 5 ) = 0 . 391222 \dots$

**Final answer:** $\text{P} ( 1 . 5 \leq X < 5 ) = 0 . 391$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: Identifying the values X = 2, 3 and 4, seen or implied.
> 
> **M1**: P(2) + P(3) + P(4) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: 0.391, or answers which round to 0.391.
> 
> If 0.391 is given with no working, for example straight from a calculator, award 1 mark only.
Use the conditional probability formula

`\text{P}(X = 4 \mid X > 0) = \dfrac{\text{P}(X = 4 \text{ and } X > 0)}{\text{P}(X > 0)}`

If $X = 4$ then $X > 0$ automatically, so the numerator is just $\text{P} ( X = 4 )$, found in (b)

$\text{P} ( X = 4 \text{and} X > 0 ) = \text{P} ( X = 4 )$

$X > 0$ is every outcome except $X = 0$

$\text{P} ( X > 0 ) = 1 - \text{e}^{-5.0625}$

**[M1]**

Divide, using the unrounded values

`\text{P}(X = 4 \mid X > 0) = \dfrac{\text{e}^{-5.0625}\frac{5.0625^{4}}{4!}}{1 - \text{e}^{-5.0625}} = \dfrac{0.173233\ldots}{0.993670\ldots}`

**[M1]**

`\text{P}(X = 4 \mid X > 0) = 0.174337\ldots`

**Final answer:** `\text{P}(X = 4 \mid X > 0) = 0.174`** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: P(X > 0) = $1 - \text{e}^{-λ}$ with any λ.
> 
> **M1**: P(X = 4) divided by P(X > 0), where the denominator is a probability less than 1.
> 
> **A1**: 0.174, or answers which round to 0.174.
> 
> Giving P(X = 4) alone, or dividing the other way up, scores 0.

### Q16
The mean equals the variance, 3.14 per day, so multiply by 5 for a nursery week

$λ = 3 . 14 \times 5 = 15 . 7$

**[B1]**

Let $X$ be the number of tantrums in a week

`X \sim \text{Po}(15.7)`

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $r = 17$

$\text{P} ( X = 17 ) = \text{e}^{-15.7} \frac{15.7^{17}}{17!}$

**[M1]**

$\text{P} ( X = 17 ) = 0 . 0913697 \dots$

**Final answer:** $\text{P} ( X = 17 ) = 0 . 0914$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = 15.7 for a week, seen or implied.
> 
> **M1**: A correct expression for P(X = 17) with any λ.
> 
> **A1**: 0.0914, or answers which round to 0.0914.
> 
> If 0.0914 is given with no working, for example straight from a calculator, award 1 mark only, or 2 marks if λ = 15.7 is seen.
Double the daily mean for 2 days

$λ = 3 . 14 \times 2 = 6 . 28$

**[B1]**

Let $Y$ be the number of tantrums in 2 days

`Y \sim \text{Po}(6.28)`

"Fewer than 4" means $Y = 0 ,  1 ,  2 \text{or} 3$

`\text{P}(Y < 4) = \text{e}^{-6.28}\left(1 + 6.28 + \dfrac{6.28^{2}}{2!} + \dfrac{6.28^{3}}{3!}\right)`

**[M1]**

$\text{P} ( Y < 4 ) = 0 . 127912 \dots$

**Final answer:** $\text{P} ( Y < 4 ) = 0 . 128$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = 6.28 for 2 days, seen or implied.
> 
> **M1**: P(0) + P(1) + P(2) + P(3) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: 0.128, or answers which round to 0.128.
> 
> If 0.128 is given with no working, for example straight from a calculator, award 1 mark only, or 2 marks if λ = 6.28 is seen.
Let $T$ be the number of tantrums in a day

`T \sim \text{Po}(3.14)`

Use the conditional probability formula; $T = 0$ is already one of the outcomes with $T < 4$, so the numerator is just $\text{P} ( T = 0 )$

`\text{P}(T = 0 \mid T < 4) = \dfrac{\text{P}(T = 0)}{\text{P}(T < 4)}`

Find the numerator

$\text{P} ( T = 0 ) = \text{e}^{-3.14}$

**[B1]**

Find the denominator: "fewer than 4" means $T = 0 ,  1 ,  2 \text{or} 3$

`\text{P}(T < 4) = \text{e}^{-3.14}\left(1 + 3.14 + \dfrac{3.14^{2}}{2!} + \dfrac{3.14^{3}}{3!}\right)`

**[M1]**

Divide

`\text{P}(T = 0 \mid T < 4) = \dfrac{\text{e}^{-3.14}}{\text{e}^{-3.14}\left(1 + 3.14 + \dfrac{3.14^{2}}{2!} + \dfrac{3.14^{3}}{3!}\right)}`

**[M1]**

Cancel the common factor $\text{e}^{-3.14}$

`\text{P}(T = 0 \mid T < 4) = \dfrac{1}{1 + 3.14 + \dfrac{3.14^{2}}{2!} + \dfrac{3.14^{3}}{3!}} = 0.0702757\ldots`

**Final answer:** `\text{P}(T = 0 \mid T < 4) = 0.0703`** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: P(T = 0) = $\text{e}^{-3.14}$, or 0.0433, seen or implied.
> 
> **M1**: P(0) + P(1) + P(2) + P(3) written out with λ = 3.14. Allow one term missing or one extra term.
> 
> **M1**: P(T = 0) divided by P(T < 4). Accept 0.0433 ÷ 0.616.
> 
> **A1**: 0.0703, or answers which round to 0.0703.
> 
> Using λ = 6.28 or 15.7 here does not score the final mark: the condition is about one day.

### Q17
Find the sum of the values and the sum of their squares, using the numbers of days as frequencies

$\sum f x = 0 \times 51 + 1 \times 54 + 2 \times 36 + 3 \times 6 + 4 \times 3 = 156$

$\sum f x^{2} = 0^{2} \times 51 + 1^{2} \times 54 + 2^{2} \times 36 + 3^{2} \times 6 + 4^{2} \times 3 = 300$

**[B1]**

The unbiased estimate of the population mean is the sample mean, $\overline{x} = \frac{\sumfx}{n}$

$\overline{x} = \frac{156}{150}$

$\overline{x} = 1 . 04$

**[B1]**

Use the formula for the unbiased estimate of the population variance, `s^{2} = \dfrac{1}{n - 1}\left(\sum fx^{2} - \dfrac{\left(\sum fx\right)^{2}}{n}\right)`

`s^{2} = \dfrac{1}{149}\left(300 - \dfrac{156^{2}}{150}\right)`

**[M1]**

$s^{2} = \frac{3444}{3725} = 0 . 924563 \dots$

**Final answer:** $s^{2} = 0 . 925$** (3 s.f.)**

**[A1]**

A Poisson distribution has its mean equal to its variance, so compare the two estimates

$\overline{x} = 1 . 04$* and *$s^{2} = 0 . 925$

**Final answer:** **The estimates of the mean and the variance are approximately equal, so a Poisson distribution is an appropriate model**

**[B1]**

> **[mark-scheme]**
> **B1**: $\sum f x = 156$ and $\sum f x^{2} = 300$, seen or implied.
> 
> **B1**: Mean = 1.04. Accept $\frac{26}{25}$.
> 
> **M1**: Correct use of an unbiased variance formula, `\dfrac{1}{149}\left(300 - \dfrac{156^{2}}{150}\right)` or `\dfrac{150}{149}\left(\dfrac{300}{150} - 1.04^{2}\right)`. The biased variance (0.918) scores M0 A0.
> 
> **A1**: Variance = 0.925, or answers which round to 0.925. Accept $\frac{3444}{3725}$.
> 
> **B1**: The mean and variance are approximately equal (or "close"), with both values seen. Stating Poisson conditions (independently, singly) without comparing the estimates does not score.
Let $X$ be the number of detentions in a day

`X \sim \text{Po}(1.04)`

"At least 5" is every outcome except 0, 1, 2, 3 and 4, so subtract those five terms from 1

`\text{P}(X \geq 5) = 1 - \text{e}^{-1.04}\left(1 + 1.04 + \dfrac{1.04^{2}}{2!} + \dfrac{1.04^{3}}{3!} + \dfrac{1.04^{4}}{4!}\right)`

**[M1]**

$\text{P} ( X \geq 5 ) = 0 . 00431058 \dots$

**Final answer:** $\text{P} ( X \geq 5 ) = 0 . 00431$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: 1 − (P(0) + P(1) + P(2) + P(3) + P(4)) written out with any λ. Allow one term missing or one extra term. Follow through your mean from (a).
> 
> **A1**: 0.00431, or answers which round to 0.00431.
> 
> If 0.00431 is given with no working, for example straight from a calculator, award 1 mark only.
A school week is 5 days, so scale the daily mean to find the mean number of detentions in a week

$λ = 1 . 04 \times 5 = 5 . 2$

**[B1]**

Let $Y$ be the number of detentions in a week

`Y \sim \text{Po}(5.2)`

"Fewer than 3" means $Y = 0 ,  1 \text{or} 2$

`\text{P}(Y < 3) = \text{e}^{-5.2}\left(1 + 5.2 + \dfrac{5.2^{2}}{2!}\right)`

**[M1]**

$\text{P} ( Y < 3 ) = 0 . 108786 \dots$

**[A1]**

There are 40 weeks, so the expected number of weeks with fewer than 3 detentions is 40 times this probability

$40 \times 0 . 108786 \dots = 4 . 351 \dots$

A number of weeks is a whole number

**Final answer:** **4 weeks**

**[B1]**

> **[mark-scheme]**
> **B1**: λ = 5.2 for a week, seen or implied.
> 
> **M1**: P(0) + P(1) + P(2) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: P(Y < 3) = 0.1088, or better.
> 
> **B1**: 4 weeks. Follow through 40 × your probability, given as a single whole number. Accept 4.35 seen in the working followed by 4. A decimal final answer, or "about 4", does not score.

### Q18
State two of the Poisson conditions (randomly, independently, singly, at a constant average rate) in context

**Final answer:** **Blue's barks occur independently of each other**

**[B1]**

**Final answer:** **Blue barks at a constant average rate throughout the time he is observed**

**[B1]**

> **[mark-scheme]**
> **B1**: One correct assumption, in context. For example, the barks occur independently, or at random, or singly (one at a time), or at a constant average rate.
> 
> **B1**: A second, different correct assumption, in context.
> 
> A rate assumption must say "mean" or "rate". Two correct assumptions that do not mention Blue or the barks score 1 mark only.
(i)

10 minutes is $\frac{10}{60}$ of an hour, so scale the mean to find the mean number of barks in 10 minutes

$λ = 25 \times \frac{10}{60} = \frac{25}{6}$

**[B1]**

Let $X$ be the number of barks in 10 minutes

`X \sim \text{Po}\left(\dfrac{25}{6}\right)`

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $r = 5$

`\text{P}(X = 5) = \text{e}^{-\frac{25}{6}}\dfrac{\left(\frac{25}{6}\right)^{5}}{5!}`

**[M1]**

$\text{P} ( X = 5 ) = 0 . 162256 \dots$

**Final answer:** $\text{P} ( X = 5 ) = 0 . 162$** (3 s.f.)**

**[A1]**

(ii)

15 minutes is a quarter of an hour

$λ = 25 \times \frac{15}{60} = 6 . 25$

**[B1]**

Let $Y$ be the number of barks in 15 minutes

`Y \sim \text{Po}(6.25)`

"At most 4" means $Y = 0 ,  1 ,  2 ,  3 \text{or} 4$

`\text{P}(Y \leq 4) = \text{e}^{-6.25}\left(1 + 6.25 + \dfrac{6.25^{2}}{2!} + \dfrac{6.25^{3}}{3!} + \dfrac{6.25^{4}}{4!}\right)`

**[M1]**

$\text{P} ( Y \leq 4 ) = 0 . 252985 \dots$

**Final answer:** $\text{P} ( Y \leq 4 ) = 0 . 253$** (3 s.f.)**

**[A1]**

(iii)

2 hours is twice the hourly period

$λ = 25 \times 2 = 50$

**[B1]**

Let $W$ be the number of barks in 2 hours

`W \sim \text{Po}(50)`

"More than 47 but not more than 51" means $W = 48 ,  49 ,  50 \text{or} 51$

`\text{P}(48 \leq W \leq 51) = \text{e}^{-50}\left(\dfrac{50^{48}}{48!} + \dfrac{50^{49}}{49!} + \dfrac{50^{50}}{50!} + \dfrac{50^{51}}{51!}\right)`

**[M1]**

$\text{P} ( 48 \leq W \leq 51 ) = 0 . 223069 \dots$

**Final answer:** $\text{P} ( 48 \leq W \leq 51 ) = 0 . 223$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = $\frac{25}{6}$ for 10 minutes, seen or implied. Accept 4.17 or better.
> 
> **M1**: A correct expression for P(X = 5) with any λ.
> 
> **A1**: 0.162, or answers which round to 0.162.
> 
> **B1**: λ = 6.25 for 15 minutes, seen or implied.
> 
> **M1**: P(0) + P(1) + P(2) + P(3) + P(4) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: 0.253, or answers which round to 0.253.
> 
> **B1**: λ = 50 for 2 hours, seen or implied.
> 
> **M1**: P(48) + P(49) + P(50) + P(51) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: 0.223, or answers which round to 0.223. A normal approximation, N(50, 50) with a continuity correction, gives 0.222 and also earns full marks.
> 
> If 0.162, 0.253 or 0.223 is given with no working, for example straight from a calculator, award 1 mark only for that answer, or 2 marks if the correct λ is seen.

### Q19
Multiply the rate per minute by 5 to find the mean number of enemies in 5 minutes

$λ = 2 . 5 \times 5 = 12 . 5$

**[B1]**

Let $X$ be the number of enemies in 5 minutes

`X \sim \text{Po}(12.5)`

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $r = 10$

$\text{P} ( X = 10 ) = \text{e}^{-12.5} \frac{12.5^{10}}{10!}$

**[M1]**

$\text{P} ( X = 10 ) = 0 . 0956436 \dots$

**Final answer:** $\text{P} ( X = 10 ) = 0 . 0956$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = 12.5 for 5 minutes, seen or implied.
> 
> **M1**: A correct expression for P(X = 10) with any λ.
> 
> **A1**: 0.0956, or answers which round to 0.0956.
> 
> If 0.0956 is given with no working, for example straight from a calculator, award 1 mark only, or 2 marks if λ = 12.5 is seen.
90 seconds is 1.5 minutes

$λ = 2 . 5 \times 1 . 5 = 3 . 75$

**[B1]**

Let $Y$ be the number of enemies in 90 seconds

`Y \sim \text{Po}(3.75)`

"At least 3" is every outcome except 0, 1 and 2, so subtract those three terms from 1

`\text{P}(Y \geq 3) = 1 - \text{e}^{-3.75}\left(1 + 3.75 + \dfrac{3.75^{2}}{2!}\right)`

**[M1]**

$\text{P} ( Y \geq 3 ) = 0 . 722931 \dots$

**Final answer:** $\text{P} ( Y \geq 3 ) = 0 . 723$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = 3.75 for 90 seconds, seen or implied.
> 
> **M1**: 1 − (P(0) + P(1) + P(2)) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: 0.723, or answers which round to 0.723.
> 
> If 0.723 is given with no working, for example straight from a calculator, award 1 mark only, or 2 marks if λ = 3.75 is seen.
The mean in $k$ minutes is $2 . 5 k$, and "at least one" is every outcome except none

$1 - \text{e}^{-2.5k} = 0 . 999$

**[M1]**

Rearrange to make the exponential the subject

$\text{e}^{-2.5k} = 0 . 001$

Take natural logarithms of both sides

`-2.5k = \text{ln}\left(0.001\right)`

**[M1]**

Divide by $- 2 . 5$

`k = \dfrac{\text{ln}\left(0.001\right)}{-2.5} = 2.763102\ldots`

**Final answer:** $k = 2 . 76$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: $1 - \text{e}^{-2.5k} = 0 . 999$, or $\text{e}^{-λ} = 0 . 001$ with λ = 2.5k. Condone an inequality sign in place of "=".
> 
> **M1**: Logarithms taken correctly, `-2.5k = \text{ln}\left(0.001\right)` or equivalent.
> 
> **A1**: k = 2.76, or answers which round to 2.76. Accept `\dfrac{6}{5}\,\text{ln}\left(10\right)` or `\dfrac{\text{ln}\left(1000\right)}{2.5}`.

### Q20
State one of the Poisson conditions (randomly, independently, singly, at a constant average rate) in context

**Final answer:** **Danny's messages arrive independently of each other**

**[B1]**

The mean for 2 hours is twice the hourly mean

$λ = 1 . 7 \times 2 = 3 . 4$

**[B1]**

Let $D$ be the number of messages from Danny in 2 hours

`D \sim \text{Po}(3.4)`

"Fewer than 4" means $D = 0 ,  1 ,  2 \text{or} 3$

`\text{P}(D < 4) = \text{e}^{-3.4}\left(1 + 3.4 + \dfrac{3.4^{2}}{2!} + \dfrac{3.4^{3}}{3!}\right)`

**[M1]**

$\text{P} ( D < 4 ) = 0 . 558357 \dots$

**Final answer:** $\text{P} ( D < 4 ) = 0 . 558$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: One correct assumption, in context. For example, Danny's messages arrive independently, or at random, or singly, or at a constant average rate. Not in context (for example "events are independent") does not score.
> 
> **B1**: λ = 3.4 for 2 hours, seen or implied.
> 
> **M1**: P(0) + P(1) + P(2) + P(3) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: 0.558, or answers which round to 0.558.
> 
> If 0.558 is given with no working, for example straight from a calculator, award the assumption mark if earned, then 1 mark only for the answer, or 2 marks if λ = 3.4 is seen.
The means can only be added if the three numbers of messages are independent of each other

**Final answer:** **Danny, Jessica and Luke send their messages independently of each other**

**[B1]**

The sum of independent Poisson variables is Poisson, with the means added

$λ = 1 . 7 + 1 . 5 + 1 . 1 = 4 . 3$

Let $T$ be the total number of messages in 1 hour

`T \sim \text{Po}(4.3)`

To find the probability, use $\text{P} ( T = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $r = 6$

$\text{P} ( T = 6 ) = \text{e}^{-4.3} \frac{4.3^{6}}{6!}$

**[M1]**

$\text{P} ( T = 6 ) = 0 . 119127 \dots$

**Final answer:** $\text{P} ( T = 6 ) = 0 . 119$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: The messages from the three friends are independent of each other (in context).
> 
> **M1**: A correct expression for P(T = 6) using the combined mean, λ = 1.7 + 1.5 + 1.1. Adding probabilities instead of means scores M0.
> 
> **A1**: 0.119, or answers which round to 0.119.
"At least one message in total" is every outcome of $T$ except $T = 0$

$\text{P} ( T \geq 1 ) = 1 - \text{e}^{-4.3}$

**[M1]**

$\text{P} ( T \geq 1 ) = 0 . 986431 \dots$

**Final answer:** $\text{P} ( T \geq 1 ) = 0 . 986$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: $1 - \text{e}^{-λ}$ with any λ. Follow through your λ from (b).
> 
> **A1**: 0.986, or answers which round to 0.986.
For each friend, use $1 - \text{e}^{-λ}$ with that friend's hourly mean

$\text{P} ( \text{at least one from Danny} ) = 1 - \text{e}^{-1.7}$

**[M1]**

$\text{P} ( \text{at least one from Jessica} ) = 1 - \text{e}^{-1.5}$

$\text{P} ( \text{at least one from Luke} ) = 1 - \text{e}^{-1.1}$

The three friends are independent, so multiply the three probabilities

`\left(1 - \text{e}^{-1.7}\right)\left(1 - \text{e}^{-1.5}\right)\left(1 - \text{e}^{-1.1}\right)`

**[M1]**

$= 0 . 423592 \dots$

**Final answer:** $\text{P} ( \text{at least one from each} ) = 0 . 424$** (3 s.f.)**

**[A1]**

> **[exam-tip]**
> Do not use the total from part (b) here. Three messages in total could all come from Danny, so $\text{P} ( T \geq 3 )$ is not the same as one message from each friend. When a question says "from each", work with each person's own distribution and multiply.

> **[mark-scheme]**
> **M1**: $1 - \text{e}^{-λ}$ for at least one of the friends, with that friend's mean.
> 
> **M1**: The product of three probabilities, each of the form $1 - \text{e}^{-λ}$.
> 
> **A1**: 0.424, or answers which round to 0.424. Using P(T ≥ 3) from Po(4.3) scores 0.

### Q21
State two of the Poisson conditions (randomly, independently, singly, at a constant average rate) in context

**Final answer:** **Amber's hiccups occur independently of each other**

**[B1]**

**Final answer:** **Amber's hiccups occur at a constant average rate**

**[B1]**

> **[mark-scheme]**
> **B1**: One correct condition, in context. For example, hiccups occur independently, or at random, or singly (one at a time), or at a constant average rate.
> 
> **B1**: A second, different correct condition, in context.
> 
> A rate condition must say "mean" or "rate": "a constant number of hiccups" does not score. Two correct conditions that do not mention the hiccups score 1 mark only.
(i)

Let $X$ be the number of hiccups in 30 seconds

`X \sim \text{Po}(2.9)`

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $r = 3$

$\text{P} ( X = 3 ) = \text{e}^{-2.9} \frac{2.9^{3}}{3!}$

**[M1]**

$\text{P} ( X = 3 ) = 0 . 223660 \dots$

**Final answer:** $\text{P} ( X = 3 ) = 0 . 224$** (3 s.f.)**

**[A1]**

(ii)

15 seconds is half of 30 seconds, so halve the mean

$λ = 2 . 9 \div 2 = 1 . 45$

**[B1]**

Let $Y$ be the number of hiccups in 15 seconds

`Y \sim \text{Po}(1.45)`

"At least twice but not more than 5 times" means $Y = 2 ,  3 ,  4 \text{or} 5$

`\text{P}(2 \leq Y \leq 5) = \text{e}^{-1.45}\left(\dfrac{1.45^{2}}{2!} + \dfrac{1.45^{3}}{3!} + \dfrac{1.45^{4}}{4!} + \dfrac{1.45^{5}}{5!}\right)`

**[M1]**

$\text{P} ( 2 \leq Y \leq 5 ) = 0 . 421512 \dots$

**Final answer:** $\text{P} ( 2 \leq Y \leq 5 ) = 0 . 422$** (3 s.f.)**

**[A1]**

(iii)

1 minute is two 30-second periods, so double the mean

$λ = 2 . 9 \times 2 = 5 . 8$

**[B1]**

Let $W$ be the number of hiccups in 1 minute

`W \sim \text{Po}(5.8)`

"At least once" is every outcome except $W = 0$

$\text{P} ( W \geq 1 ) = 1 - \text{e}^{-5.8}$

**[M1]**

$\text{P} ( W \geq 1 ) = 0 . 996972 \dots$

**Final answer:** $\text{P} ( W \geq 1 ) = 0 . 997$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(X = 3), $\text{e}^{-2.9} \frac{2.9^{3}}{3!}$.
> 
> **A1**: 0.224, or answers which round to 0.224.
> 
> **B1**: λ = 1.45 for 15 seconds, seen or implied.
> 
> **M1**: P(2) + P(3) + P(4) + P(5) written out with any λ. Allow one term missing or one extra term. Accept P(Y ≤ 5) − P(Y ≤ 1) with both sums written out.
> 
> **A1**: 0.422, or answers which round to 0.422.
> 
> **B1**: λ = 5.8 for 1 minute, seen or implied.
> 
> **M1**: $1 - \text{e}^{-λ}$ with any λ. Allow 1 − (P(0) + P(1)) as one term too many.
> 
> **A1**: 0.997, or answers which round to 0.997.
> 
> If 0.224, 0.422 or 0.997 is given with no working, for example straight from a calculator, award 1 mark only for that answer, or 2 marks for (ii) or (iii) if the correct λ is seen.

### Q22
The disconnections are random events with a mean of 5 per day

`X \sim \text{Po}(5)`

**[B1]**

State one of the Poisson conditions (randomly, independently, singly, at a constant average rate) in context

**Final answer:** **The internet disconnects independently, so one disconnection does not affect when the next one happens**

**[B1]**

> **[mark-scheme]**
> **B1**: X ~ Po(5). Accept "Poisson with mean 5".
> 
> **B1**: One correct assumption, in context. For example, disconnections occur independently, or at random, or singly (one at a time), or at a constant average rate. An assumption that does not mention the internet or the disconnections does not score.
(i)

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $λ = 5$ and $r = 4$

$\text{P} ( X = 4 ) = \text{e}^{-5} \frac{5^{4}}{4!}$

**[M1]**

$\text{P} ( X = 4 ) = 0 . 175467 \dots$

**Final answer:** $\text{P} ( X = 4 ) = 0 . 175$** (3 s.f.)**

**[A1]**

(ii)

"At most 3 times" means $X = 0 ,  1 ,  2 \text{or} 3$, so add those four terms

`\text{P}(X \leq 3) = \text{e}^{-5}\left(\dfrac{5^{0}}{0!} + \dfrac{5^{1}}{1!} + \dfrac{5^{2}}{2!} + \dfrac{5^{3}}{3!}\right)`

**[M1]**

$\text{P} ( X \leq 3 ) = 0 . 265025 \dots$

**Final answer:** $\text{P} ( X \leq 3 ) = 0 . 265$** (3 s.f.)**

**[A1]**

(iii)

"At least 2 times" is every outcome except $X = 0$ and $X = 1$, so subtract those two terms from 1

`\text{P}(X \geq 2) = 1 - \text{e}^{-5}\left(\dfrac{5^{0}}{0!} + \dfrac{5^{1}}{1!}\right)`

**[M1]**

$\text{P} ( X \geq 2 ) = 0 . 959572 \dots$

**Final answer:** $\text{P} ( X \geq 2 ) = 0 . 960$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(X = 4), $\text{e}^{-5} \frac{5^{4}}{4!}$. Follow through your λ from (a).
> 
> **A1**: P(X = 4) = 0.175, or answers which round to 0.175.
> 
> **M1**: P(0) + P(1) + P(2) + P(3) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: P(X ≤ 3) = 0.265, or answers which round to 0.265.
> 
> **M1**: 1 − (P(0) + P(1)) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: P(X ≥ 2) = 0.960, or answers which round to 0.960.
> 
> If 0.175, 0.265 or 0.960 is given with no working, for example straight from a calculator, award 1 mark only for that answer.

### Q23
(i)

Find the sum of the values and the sum of their squares, using the frequencies

$\sum f x = 0 \times 3 + 1 \times 5 + 2 \times 17 + 3 \times 15 + 4 \times 10 = 124$

$\sum f x^{2} = 0^{2} \times 3 + 1^{2} \times 5 + 2^{2} \times 17 + 3^{2} \times 15 + 4^{2} \times 10 = 368$

**[B1]**

The unbiased estimate of the mean is the sample mean, $\overline{x} = \frac{\sumfx}{n}$

$\overline{x} = \frac{124}{50}$

$\overline{x} = 2 . 48$

**[B1]**

Use the formula for the unbiased estimate of the variance, `s^{2} = \dfrac{1}{n - 1}\left(\sum fx^{2} - \dfrac{\left(\sum fx\right)^{2}}{n}\right)`

`s^{2} = \dfrac{1}{49}\left(368 - \dfrac{124^{2}}{50}\right)`

**[M1]**

$s^{2} = \frac{216}{175} = 1 . 234285 \dots$

**Final answer:** $s^{2} = 1 . 23$** (3 s.f.)**

**[A1]**

(ii)

A Poisson distribution has its mean equal to its variance, so compare the two estimates

$\overline{x} = 2 . 48$* is not close to *$s^{2} = 1 . 23$

**Final answer:** **A Poisson distribution could not be used, because the mean and the variance are not approximately equal**

**[B1]**

> **[mark-scheme]**
> **B1**: $\sum f x = 124$ and $\sum f x^{2} = 368$, seen or implied.
> 
> **B1**: Mean = 2.48.
> 
> **M1**: Correct use of an unbiased variance formula, `\dfrac{1}{49}\left(368 - \dfrac{124^{2}}{50}\right)` or `\dfrac{50}{49}\left(\dfrac{368}{50} - 2.48^{2}\right)`. The biased variance (1.21) scores M0 A0.
> 
> **A1**: Variance = 1.23, or answers which round to 1.23. Accept $\frac{216}{175}$.
> 
> **B1**: "Not suitable", with a reason comparing the mean and variance (for example, 2.48 and 1.23 are not close). Both the verdict and the reason are needed.
(i)

Find the sum of the values and the sum of their squares, using the frequencies

$\sum f y = 0 \times 15 + 1 \times 19 + 2 \times 25 + 3 \times 21 + 4 \times 12 + 5 \times 8 = 220$

$\sum f y^{2} = 0^{2} \times 15 + 1^{2} \times 19 + 2^{2} \times 25 + 3^{2} \times 21 + 4^{2} \times 12 + 5^{2} \times 8 = 700$

**[B1]**

The unbiased estimate of the mean is the sample mean, $\overline{y} = \frac{\sumfy}{n}$

$\overline{y} = \frac{220}{100}$

$\overline{y} = 2 . 2$

**[B1]**

Use the formula for the unbiased estimate of the variance, `s^{2} = \dfrac{1}{n - 1}\left(\sum fy^{2} - \dfrac{\left(\sum fy\right)^{2}}{n}\right)`

`s^{2} = \dfrac{1}{99}\left(700 - \dfrac{220^{2}}{100}\right)`

**[M1]**

$s^{2} = \frac{24}{11} = 2 . 181818 \dots$

**Final answer:** $s^{2} = 2 . 18$** (3 s.f.)**

**[A1]**

(ii)

A Poisson distribution has its mean equal to its variance, so compare the two estimates

$\overline{y} = 2 . 2$* is close to *$s^{2} = 2 . 18$

**Final answer:** **A Poisson distribution could be used, because the mean and the variance are approximately equal**

**[B1]**

> **[mark-scheme]**
> **B1**: $\sum f y = 220$ and $\sum f y^{2} = 700$, seen or implied.
> 
> **B1**: Mean = 2.2.
> 
> **M1**: Correct use of an unbiased variance formula, `\dfrac{1}{99}\left(700 - \dfrac{220^{2}}{100}\right)` or `\dfrac{100}{99}\left(\dfrac{700}{100} - 2.2^{2}\right)`. The biased variance (2.16) scores M0 A0.
> 
> **A1**: Variance = 2.18, or answers which round to 2.18. Accept $\frac{24}{11}$.
> 
> **B1**: "Suitable", with a reason comparing the mean and variance (for example, 2.2 and 2.18 are close). Both the verdict and the reason are needed.

### Q24
The rate is constant, so scale the mean to 1 minute

$λ = 8 \times \frac{1}{15} = \frac{8}{15}$

**[B1]**

Let $X$ be the number of customers in 1 minute

`X \sim \text{Po}\left(\dfrac{8}{15}\right)`

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $r = 3$

`\text{P}(X = 3) = \text{e}^{-\frac{8}{15}}\dfrac{\left(\frac{8}{15}\right)^{3}}{3!}`

**[M1]**

$\text{P} ( X = 3 ) = 0 . 0148327 \dots$

**Final answer:** $\text{P} ( X = 3 ) = 0 . 0148$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = $\frac{8}{15}$ for 1 minute, seen or implied. Accept 0.533 or better.
> 
> **M1**: A correct expression for P(X = 3) with any λ.
> 
> **A1**: 0.0148, or answers which round to 0.0148.
> 
> If 0.0148 is given with no working, for example straight from a calculator, award 1 mark only, or 2 marks if λ = 8/15 is seen.
15 seconds is a quarter of a minute, so scale the mean to find the mean number of customers in 15 seconds

$λ = \frac{8}{15} \times \frac{1}{4} = \frac{2}{15}$

**[B1]**

Let $Y$ be the number of customers in 15 seconds

`Y \sim \text{Po}\left(\dfrac{2}{15}\right)`

"At least 1" is every outcome except $Y = 0$

$\text{P} ( Y \geq 1 ) = 1 - \text{P} ( Y = 0 )$

$\text{P} ( Y \geq 1 ) = 1 - \text{e}^{-\frac{2}{15}}$

**[M1]**

$\text{P} ( Y \geq 1 ) = 0 . 124826 \dots$

**Final answer:** $\text{P} ( Y \geq 1 ) = 0 . 125$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = $\frac{2}{15}$ for 15 seconds, seen or implied. Accept 0.133 or better.
> 
> **M1**: $1 - \text{e}^{-λ}$ with any λ. Allow 1 − (P(0) + P(1)) as one term too many.
> 
> **A1**: 0.125, or answers which round to 0.125.
> 
> If 0.125 is given with no working, for example straight from a calculator, award 1 mark only, or 2 marks if λ = 2/15 is seen.
10 minutes is $\frac{10}{15}$ of 15 minutes, so scale the mean to find the mean number of customers in 10 minutes

$λ = 8 \times \frac{10}{15} = \frac{16}{3}$

**[B1]**

Let $Z$ be the number of customers in 10 minutes

`Z \sim \text{Po}\left(\dfrac{16}{3}\right)`

"At most 3" means $Z = 0 ,  1 ,  2 \text{or} 3$, so add those four terms

`\text{P}(Z \leq 3) = \text{e}^{-\frac{16}{3}}\left(1 + \dfrac{16}{3} + \dfrac{\left(\frac{16}{3}\right)^{2}}{2!} + \dfrac{\left(\frac{16}{3}\right)^{3}}{3!}\right)`

**[M1]**

$\text{P} ( Z \leq 3 ) = 0 . 221310 \dots$

**Final answer:** $\text{P} ( Z \leq 3 ) = 0 . 221$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = $\frac{16}{3}$ for 10 minutes, seen or implied. Accept 5.33 or better.
> 
> **M1**: P(0) + P(1) + P(2) + P(3) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: 0.221, or answers which round to 0.221.
> 
> If 0.221 is given with no working, for example straight from a calculator, award 1 mark only, or 2 marks if λ = 16/3 is seen.
1 hour is four 15-minute periods, so the mean for 1 hour is

$λ = 8 \times 4 = 32$

For a Poisson distribution the variance equals the mean

$\text{Var} = λ$

$\text{Var} = 32$

**[B1]**

> **[mark-scheme]**
> **B1**: Variance = 32.

### Q25
Find the sum of the values and the sum of their squares, using the frequencies

$\sum f x = 0 \times 43 + 1 \times 44 + 2 \times 22 + 3 \times 8 + 4 \times 3 = 124$

$\sum f x^{2} = 0^{2} \times 43 + 1^{2} \times 44 + 2^{2} \times 22 + 3^{2} \times 8 + 4^{2} \times 3 = 252$

**[B1]**

The unbiased estimate of the population mean is the sample mean, $\overline{x} = \frac{\sumfx}{n}$

$\overline{x} = \frac{124}{120} = \frac{31}{30} = 1 . 0333 \dots$

**Final answer:** $\overline{x} = 1 . 03$** (3 s.f.)**

**[B1]**

Use the formula for the unbiased estimate of the population variance, `s^{2} = \dfrac{1}{n - 1}\left(\sum fx^{2} - \dfrac{\left(\sum fx\right)^{2}}{n}\right)`

`s^{2} = \dfrac{1}{119}\left(252 - \dfrac{124^{2}}{120}\right)`

**[M1]**

$s^{2} = \frac{1858}{1785} = 1 . 040896 \dots$

**Final answer:** $s^{2} = 1 . 04$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: $\sum f x = 124$ and $\sum f x^{2} = 252$, seen or implied.
> 
> **B1**: Mean = 1.03, or answers which round to 1.03. Accept $\frac{31}{30}$.
> 
> **M1**: Correct use of an unbiased variance formula, `\dfrac{1}{119}\left(252 - \dfrac{124^{2}}{120}\right)` or `\dfrac{120}{119}\left(\dfrac{252}{120} - \left(\dfrac{31}{30}\right)^{2}\right)`. The biased variance (1.03) scores M0 A0.
> 
> **A1**: Variance = 1.04, or answers which round to 1.04. Accept $\frac{1858}{1785}$.
A Poisson distribution has its mean equal to its variance, so compare the two estimates from part (a)

$\overline{x} = 1 . 03$* and *$s^{2} = 1 . 04$

**Final answer:** **The estimates of the mean and the variance are approximately equal, as they would be for a Poisson distribution**

**[B1]**

> **[exam-tip]**
> Notice the wording "suggest that … may be suitable". Equal mean and variance is what a Poisson model predicts, so it supports the model, but it does not prove it: the birds must also pass randomly, independently and singly, at a constant average rate.

> **[mark-scheme]**
> **B1**: The mean and variance are approximately equal (or "close", "similar"), referring to the values from part (a). Follow through your values from (a) if they are close.
(i)

30 minutes is three 10-minute periods

$λ = 1 \times 3 = 3$

**[B1]**

Let $X$ be the number of birds in 30 minutes

`X \sim \text{Po}(3)`

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $r = 2$

$\text{P} ( X = 2 ) = \text{e}^{-3} \frac{3^{2}}{2!}$

**[M1]**

$\text{P} ( X = 2 ) = 0 . 224041 \dots$

**Final answer:** $\text{P} ( X = 2 ) = 0 . 224$** (3 s.f.)**

**[A1]**

(ii)

1 minute is one tenth of 10 minutes

$λ = 1 \times \frac{1}{10} = 0 . 1$

**[B1]**

Let $Y$ be the number of birds in 1 minute

`Y \sim \text{Po}(0.1)`

"Fewer than 2" means $Y = 0 \text{or} 1$

`\text{P}(Y < 2) = \text{e}^{-0.1}\left(\dfrac{0.1^{0}}{0!} + \dfrac{0.1^{1}}{1!}\right)`

**[M1]**

$\text{P} ( Y < 2 ) = 0 . 995321 \dots$

**Final answer:** $\text{P} ( Y < 2 ) = 0 . 995$** (3 s.f.)**

**[A1]**

(iii)

1 hour is six 10-minute periods

$λ = 1 \times 6 = 6$

**[B1]**

Let $W$ be the number of birds in 1 hour

`W \sim \text{Po}(6)`

"At least 4" is every outcome except 0, 1, 2 and 3, so subtract those four terms from 1

`\text{P}(W \geq 4) = 1 - \text{e}^{-6}\left(\dfrac{6^{0}}{0!} + \dfrac{6^{1}}{1!} + \dfrac{6^{2}}{2!} + \dfrac{6^{3}}{3!}\right)`

**[M1]**

$\text{P} ( W \geq 4 ) = 0 . 848796 \dots$

**Final answer:** $\text{P} ( W \geq 4 ) = 0 . 849$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = 3 for 30 minutes, seen or implied.
> 
> **M1**: A correct expression for P(X = 2) with any λ.
> 
> **A1**: 0.224, or answers which round to 0.224.
> 
> **B1**: λ = 0.1 for 1 minute, seen or implied.
> 
> **M1**: P(0) + P(1) written out with any λ.
> 
> **A1**: 0.995, or answers which round to 0.995.
> 
> **B1**: λ = 6 for 1 hour, seen or implied.
> 
> **M1**: 1 − (P(0) + P(1) + P(2) + P(3)) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: 0.849, or answers which round to 0.849.
> 
> If 0.224, 0.995 or 0.849 is given with no working, for example straight from a calculator, award 1 mark only for that answer, or 2 marks if the correct λ is seen.

### Q26
Let $X$ be the number of times Lucy goes to the cinema in a week, so `X \sim \text{Po}(4)`

To find the probability, use $\text{P} ( X = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $λ = 4$ and $r = 5$

$\text{P} ( X = 5 ) = \text{e}^{-4} \frac{4^{5}}{5!}$

**[M1]**

$\text{P} ( X = 5 ) = 0 . 156293 \dots$

**Final answer:** $\text{P} ( X = 5 ) = 0 . 156$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(X = 5), $\text{e}^{-4} \frac{4^{5}}{5!}$.
> 
> **A1**: 0.156, or answers which round to 0.156.
> 
> If 0.156 is given with no working, for example straight from a calculator, award 1 mark only.
Double the weekly mean for 2 weeks

$λ = 4 \times 2 = 8$

**[B1]**

Let $Y$ be the number of times in 2 weeks

`Y \sim \text{Po}(8)`

"Not more than 4" means $Y = 0 ,  1 ,  2 ,  3 \text{or} 4$, so add those five terms

`\text{P}(Y \leq 4) = \text{e}^{-8}\left(\dfrac{8^{0}}{0!} + \dfrac{8^{1}}{1!} + \dfrac{8^{2}}{2!} + \dfrac{8^{3}}{3!} + \dfrac{8^{4}}{4!}\right)`

**[M1]**

$\text{P} ( Y \leq 4 ) = 0 . 0996324 \dots$

**Final answer:** $\text{P} ( Y \leq 4 ) = 0 . 0996$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = 8 for the 2-week period, seen or implied.
> 
> **M1**: P(0) + P(1) + P(2) + P(3) + P(4) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: 0.0996, or answers which round to 0.0996.
> 
> If 0.0996 is given with no working, for example straight from a calculator, award 1 mark only, or 2 marks if λ = 8 is seen.
Divide the weekly mean by 7 for one day

$λ = \frac{4}{7}$

**[B1]**

Let $W$ be the number of times in a day

`W \sim \text{Po}\left(\dfrac{4}{7}\right)`

"At least once" is every outcome except $W = 0$, so subtract $\text{P} ( W = 0 )$ from 1

$\text{P} ( W \geq 1 ) = 1 - \text{P} ( W = 0 )$

$\text{P} ( W \geq 1 ) = 1 - \text{e}^{-\frac{4}{7}}$

**[M1]**

$\text{P} ( W \geq 1 ) = 0 . 435281 \dots$

**Final answer:** $\text{P} ( W \geq 1 ) = 0 . 435$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: λ = $\frac{4}{7}$ for one day, seen or implied. Accept 0.571 or better.
> 
> **M1**: $1 - \text{e}^{-λ}$ with any λ. Allow 1 − (P(0) + P(1)) as one term too many.
> 
> **A1**: 0.435, or answers which round to 0.435.
> 
> If 0.435 is given with no working, for example straight from a calculator, award 1 mark only, or 2 marks if λ = 4/7 is seen.

### Q27
For independent Poisson variables, add the means: if `X \sim \text{Po}(\lambda)` and `Y \sim \text{Po}(\mu)` are independent, then

`X + Y \sim \text{Po}(\lambda + \mu)`

Add the means for the ham and the salami

$6 . 2 + 4 . 9 = 11 . 1$

Let $T$ be the total number of pieces of meat

`T \sim \text{Po}(11.1)`

**[B1]**

> **[mark-scheme]**
> **B1**: T ~ Po(11.1). Accept "Poisson with mean 11.1". Both the distribution and the parameter are needed.
To find the probability, use $\text{P} ( T = r ) = \text{e}^{-λ} \frac{λ^{r}}{r!}$ with $λ = 11 . 1$ and $r = 10$

$\text{P} ( T = 10 ) = \text{e}^{-11.1} \frac{11.1^{10}}{10!}$

**[M1]**

$\text{P} ( T = 10 ) = 0 . 118249 \dots$

**Final answer:** $\text{P} ( T = 10 ) = 0 . 118$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: A correct expression for P(T = 10) with any λ. Follow through your λ from (a).
> 
> **A1**: 0.118, or answers which round to 0.118.
> 
> If 0.118 is given with no working, for example straight from a calculator, award 1 mark only. Adding the probabilities for ham and salami, instead of the means, scores M0.
"More than 9 and fewer than 13" means $T = 10 ,  11 \text{or} 12$, so add those three terms

`\text{P}(10 \leq T \leq 12) = \text{e}^{-11.1}\left(\dfrac{11.1^{10}}{10!} + \dfrac{11.1^{11}}{11!} + \dfrac{11.1^{12}}{12!}\right)`

**[M1]**

$\text{P} ( 10 \leq T \leq 12 ) = 0 . 347948 \dots$

**Final answer:** $\text{P} ( 10 \leq T \leq 12 ) = 0 . 348$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: P(10) + P(11) + P(12) written out with any λ. Allow one term missing or one extra term.
> 
> **A1**: 0.348, or answers which round to 0.348.
> 
> If 0.348 is given with no working, for example straight from a calculator, award 1 mark only.
