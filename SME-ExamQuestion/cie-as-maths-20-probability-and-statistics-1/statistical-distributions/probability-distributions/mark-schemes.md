# Mark Schemes — Probability Distributions
**Statistical Distributions** · Cambridge (CIE) AS maths (9709)


## Exam Questions (29 questions)


### Q1
For a probability distribution, the probabilities must sum to 1. Find each probability

$\text{P} ( X = - 3 ) = \frac{1}{3\times9} = \frac{1}{27}$

$\text{P} ( X = - 1 ) = \frac{1}{3\times1} = \frac{1}{3}$

$\text{P} ( X = 1 ) = \frac{1}{3\times1} = \frac{1}{3}$

$\text{P} ( X = 3 ) = \frac{1}{3\times27} = \frac{1}{81}$

Add them

$\frac{1}{27} + \frac{1}{3} + \frac{1}{3} + \frac{1}{81} = \frac{3+27+27+1}{81} = \frac{58}{81}$

**[M1]**

**Final answer:** **The probabilities sum to 58/81, not 1, so this cannot be the probability distribution of X**

**[A1]**

> **[mark-scheme]**
> **M1**: The four probabilities found and added.
> 
> **A1**: A total of $\frac{58}{81}$ (or answers which round to 0.716), with the conclusion that the probabilities do not sum to 1.
The probabilities sum to 1

`\dfrac{k}{\left(-3\right)^{2}} + \dfrac{k}{\left(-1\right)^{2}} + \dfrac{k}{1^{3}} + \dfrac{k}{3^{3}} = 1`

**[M1]**

$\frac{k}{9} + k + k + \frac{k}{27} = \frac{58k}{27} = 1$

$k = \frac{27}{58}$

**[A1]**

> **[mark-scheme]**
> **M1**: Sum of the four probabilities in terms of $k$ set equal to 1, with the correct power in each term.
> 
> **A1**: $k = \frac{27}{58}$ exactly.
Only $X = 3$ fails $X < 2$, so subtract its probability from 1

$\text{P} ( X < 2 ) = 1 - \text{P} ( X = 3 ) = 1 - \frac{k}{27} = 1 - \frac{1}{58}$

**[M1]**

$\text{P} ( X < 2 ) = \frac{57}{58}$

**[A1]**

> **[mark-scheme]**
> **M1**: $1 - \text{P} ( X = 3 )$, or the sum of the other three probabilities, using the value of $k$ found.
> 
> **A1**: $\frac{57}{58}$, or answers which round to 0.983.

### Q2
Subtract the 2-dollar cost from each amount received (5, 3, 2, 1 or 0 dollars) to find the possible values of $W$

$W = 3 ,  1 ,  0 ,  - 1 \text{or} - 2$

**[B1]**

On each roll, $\text{P} ( \text{lucky number} ) = \frac{1}{6}$, and every earlier roll must not show it

$\text{P} ( W = 3 ) = \frac{1}{6}$

$\text{P} ( W = 1 ) = \frac{5}{6} \times \frac{1}{6} = \frac{5}{36}$

`\text{P}(W = 0) = \left(\dfrac{5}{6}\right)^{2} \times \dfrac{1}{6} = \dfrac{25}{216}`

**[M1]**

`\text{P}(W = -1) = \left(\dfrac{5}{6}\right)^{3} \times \dfrac{1}{6} = \dfrac{125}{1296}`

He receives nothing only if none of the four rolls shows his lucky number

`\text{P}(W = -2) = \left(\dfrac{5}{6}\right)^{4} = \dfrac{625}{1296}`

| $w$ | **Final answer:** **−2** | **Final answer:** **−1** | **Final answer:** **0** | **Final answer:** **1** | **Final answer:** **3** |
|---|---|---|---|---|---|
| $\text{P} ( W = w )$ | $\frac{625}{1296}$ | $\frac{125}{1296}$ | $\frac{25}{216}$ | $\frac{5}{36}$ | $\frac{1}{6}$ |

**[A1 A1]**

> **[mark-scheme]**
> **B1**: The values −2, −1, 0, 1 and 3 only, in a table or listed.
> 
> **M1**: A probability found as `\left(\dfrac{5}{6}\right)^{r-1} \times \dfrac{1}{6}` (the lucky number first appearing on roll $r$) for at least two values of $W$.
> 
> **A1**: At least three probabilities correct.
> 
> **A1**: All five probabilities correct, including `\text{P}(W = -2) = \left(\dfrac{5}{6}\right)^{4}`. Equivalent fractions over 1296 and decimals correct to 3 significant figures are accepted.
| $w$ | −2 | −1 | 0 | 1 | 3 |
|---|---|---|---|---|---|
| $\text{P} ( W = w )$ | $\frac{625}{1296}$ | $\frac{125}{1296}$ | $\frac{25}{216}$ | $\frac{5}{36}$ | $\frac{1}{6}$ |

(i)

Winning money means a positive profit, $W = 1$ or $W = 3$

$\text{P} ( W > 0 ) = \frac{5}{36} + \frac{1}{6} = \frac{5}{36} + \frac{6}{36}$

$\text{P} ( \text{wins money} ) = \frac{11}{36}$

**[B1]**

(ii)

Losing money means a negative profit, $W = - 1$ or $W = - 2$

$\text{P} ( W < 0 ) = \frac{625}{1296} + \frac{125}{1296} = \frac{750}{1296}$

$\text{P} ( \text{loses money} ) = \frac{125}{216}$

**[B1]**

(iii)

Breaking even means $W = 0$

$\text{P} ( \text{breaks even} ) = \frac{25}{216}$

**[B1]**

> **[mark-scheme]**
> **B1**: $\frac{11}{36}$, or answers which round to 0.306.
> 
> **B1**: $\frac{125}{216}$, or equivalent such as $\frac{750}{1296}$, or answers which round to 0.579.
> 
> **B1**: $\frac{25}{216}$, or answers which round to 0.116.
| $w$ | −2 | −1 | 0 | 1 | 3 |
|---|---|---|---|---|---|
| $\text{P} ( W = w )$ | $\frac{625}{1296}$ | $\frac{125}{1296}$ | $\frac{25}{216}$ | $\frac{5}{36}$ | $\frac{1}{6}$ |

Use $\text{E} ( W ) = \sum w p$, with every probability over 1296

$\text{E} ( W ) = - 2 \times \frac{625}{1296} - 1 \times \frac{125}{1296} + 0 \times \frac{150}{1296} + 1 \times \frac{180}{1296} + 3 \times \frac{216}{1296}$

**[M1]**

$\text{E} ( W ) = \frac{-1250-125+180+648}{1296} = - \frac{547}{1296} = - 0 . 42206 \dots$

**Final answer:** $\text{E} ( W ) = - 0 . 422$** dollars (3 s.f.), a loss of about 42 cents**

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum w p$ with all five terms from the table. Accept unsimplified.
> 
> **A1**: $- \frac{547}{1296}$, or answers which round to $- 0 . 422$. A loss of 0.422 dollars (or 42 cents) is equivalent. Units are not required.

### Q3
First find the probabilities for the number of heads, using $\text{P} ( \text{head} ) = \frac{1}{3}$ and $\text{P} ( \text{tail} ) = \frac{2}{3}$

$\text{P} ( 0 \text{heads} ) = \frac{2}{3} \times \frac{2}{3} = \frac{4}{9}$

$\text{P} ( 1 \text{head} ) = 2 \times \frac{1}{3} \times \frac{2}{3} = \frac{4}{9}$

$\text{P} ( 2 \text{heads} ) = \frac{1}{3} \times \frac{1}{3} = \frac{1}{9}$

Multiply each number of heads by each spinner score (1, 2 or 3) to find the possible values of $X$

*0 heads: X = 0*

*1 head: X = 1, 2 or 3*

*2 heads: X = 2, 4 or 6*

$X = 0 ,  1 ,  2 ,  3 ,  4 \text{or} 6$

**[B1]**

With no heads, $X = 0$ whatever the spinner shows

$\text{P} ( X = 0 ) = \frac{4}{9} = \frac{12}{27}$

Each other value needs a number of heads and a spinner score, each spinner score having probability $\frac{1}{3}$. A total of 2 can happen in two ways

$\text{P} ( X = 2 ) = \text{P} ( 1 \text{head, spinner} 2 ) + \text{P} ( 2 \text{heads, spinner} 1 ) = \frac{4}{9} \times \frac{1}{3} + \frac{1}{9} \times \frac{1}{3} = \frac{5}{27}$

**[M1]**

$\text{P} ( X = 1 ) = \frac{4}{9} \times \frac{1}{3} = \frac{4}{27}$

$\text{P} ( X = 3 ) = \frac{4}{9} \times \frac{1}{3} = \frac{4}{27}$

$\text{P} ( X = 4 ) = \frac{1}{9} \times \frac{1}{3} = \frac{1}{27}$

$\text{P} ( X = 6 ) = \frac{1}{9} \times \frac{1}{3} = \frac{1}{27}$

| $x$ | **Final answer:** **0** | **Final answer:** **1** | **Final answer:** **2** | **Final answer:** **3** | **Final answer:** **4** | **Final answer:** **6** |
|---|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{12}{27}$ | $\frac{4}{27}$ | $\frac{5}{27}$ | $\frac{4}{27}$ | $\frac{1}{27}$ | $\frac{1}{27}$ |

**[A1 A1]**

> **[mark-scheme]**
> **B1**: The values 0, 1, 2, 3, 4 and 6 only, in a table or listed.
> 
> **M1**: $\text{P} ( X = 2 )$ found by adding the two ways of scoring 2 (one head with a 2, or two heads with a 1).
> 
> **A1**: At least three of the six probabilities correct.
> 
> **A1**: All six probabilities correct. Decimals correct to 3 significant figures are accepted.

### Q4
Write each probability in terms of $p$ and set their sum equal to 1

$\frac{p^{2}+4p^{2}+9p^{2}+16p^{2}+25p^{2}}{495} = 1$

**[M1]**

$55 p^{2} = 495$

$p^{2} = 9$

$p$ is positive, so

$p = 3$

**[A1]**

The values of $X$ are 3, 6, 9, 12 and 15. Substitute each into $\frac{x^{2}}{495}$ and simplify, e.g. $\text{P} ( X = 3 ) = \frac{9}{495} = \frac{1}{55}$

| $x$ | **Final answer:** **3** | **Final answer:** **6** | **Final answer:** **9** | **Final answer:** **12** | **Final answer:** **15** |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{55}$ | $\frac{4}{55}$ | $\frac{9}{55}$ | $\frac{16}{55}$ | $\frac{25}{55}$ |

**[B1 B1]**

> **[mark-scheme]**
> **M1**: Sum of the five probabilities in terms of $p$ set equal to 1.
> 
> **A1**: $p = 3$ only (the negative root rejected, or not stated, because $p > 0$).
> 
> **B1**: Table with the values 3, 6, 9, 12 and 15 and at least one correct probability.
> 
> **B1**: All five probabilities correct. Unsimplified fractions such as $\frac{9}{495}$, or decimals correct to 3 significant figures, are accepted.
| $x$ | 3 | 6 | 9 | 12 | 15 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{55}$ | $\frac{4}{55}$ | $\frac{9}{55}$ | $\frac{16}{55}$ | $\frac{25}{55}$ |

(i)

Use $μ = \text{E} ( X ) = \sum x p$

$μ = \frac{3\times1+6\times4+9\times9+12\times16+15\times25}{55} = \frac{675}{55}$

**[M1]**

**Final answer:** $μ = \frac{135}{11} = 12 . 3$** (3 s.f.)**

**[A1]**

(ii)

Use $σ^{2} = \sum x^{2} p - μ^{2}$

`\sigma^{2} = \dfrac{3^{2} \times 1 + 6^{2} \times 4 + 9^{2} \times 9 + 12^{2} \times 16 + 15^{2} \times 25}{55} - \left(\dfrac{135}{11}\right)^{2}`

**[M1]**

`\sigma^{2} = \dfrac{8811}{55} - \left(\dfrac{135}{11}\right)^{2} = 160.2 - 150.6198\ldots = 9.58016\ldots`

$σ = \sqrt{9.58016\dots} = 3 . 09518 \dots$

**Final answer:** $σ = 3 . 10$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x p$ with all five terms from the table. Accept unsimplified.
> 
> **A1**: $μ = \frac{135}{11}$, or answers which round to 12.3.
> 
> **M1**: $\sum x^{2} p$ minus the square of the mean. Accept unsimplified.
> 
> **A1**: Standard deviation which rounds to 3.10.
| $x$ | 3 | 6 | 9 | 12 | 15 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{55}$ | $\frac{4}{55}$ | $\frac{9}{55}$ | $\frac{16}{55}$ | $\frac{25}{55}$ |

Find the ends of the interval with the unrounded values of $μ$ and $σ$

$μ - σ = 12 . 2727 \dots - 3 . 0951 \dots = 9 . 1775 \dots$

$μ + σ = 12 . 2727 \dots + 3 . 0951 \dots = 15 . 3679 \dots$

The only values of $X$ between 9.18 and 15.37 are 12 and 15

$\text{P} ( 9 . 18 < X < 15 . 37 ) = \text{P} ( X = 12 ) + \text{P} ( X = 15 ) = \frac{16}{55} + \frac{25}{55}$

**[M1]**

$\text{P} ( μ - σ < X < μ + σ ) = \frac{41}{55}$

**[A1]**

> **[mark-scheme]**
> **M1**: Both ends of the interval evaluated from the values of $μ$ and $σ$ in part (b), and the values of $X$ inside it identified.
> 
> **A1**: $\frac{41}{55}$, or answers which round to 0.745.

### Q5
Rearrange `\text{Var}(X) = \text{E}(X^{2}) - \left[\text{E}(X)\right]^{2}`

`\text{E}(X^{2}) = \text{Var}(X) + \left[\text{E}(X)\right]^{2} = 0.89 + 1.1^{2}`

$\text{E} ( X^{2} ) = 2 . 1$

**[B1]**

> **[mark-scheme]**
> **B1**: $\text{E} ( X^{2} ) = 2 . 1$.
Use $\text{E} ( X ) = \sum x p = 1 . 1$

$0 \times a + 1 \times b + 2 \times c = 1 . 1$

$b + 2 c = 1 . 1$

**[B1]**

Use $\text{E} ( X^{2} ) = \sum x^{2} p = 2 . 1$ from part (a)

$0^{2} \times a + 1^{2} \times b + 2^{2} \times c = 2 . 1$

$b + 4 c = 2 . 1$

**[B1]**

Subtract the first equation from the second

$2 c = 1$

**[M1]**

$c = 0 . 5$

$b = 1 . 1 - 2 \times 0 . 5 = 0 . 1$

The probabilities sum to 1

$a = 1 - 0 . 1 - 0 . 5 = 0 . 4$

$a = 0 . 4 ,  b = 0 . 1 ,  c = 0 . 5$

**[A1]**

> **[mark-scheme]**
> **B1**: $b + 2 c = 1 . 1$, or equivalent, from $\text{E} ( X ) = 1 . 1$.
> 
> **B1**: $b + 4 c = 2 . 1$, or equivalent, from the value of $\text{E} ( X^{2} )$ in part (a).
> 
> **M1**: Solving the two equations to find $b$ or $c$.
> 
> **A1**: $a = 0 . 4$, $b = 0 . 1$ and $c = 0 . 5$, with $a$ from the probabilities summing to 1.
| $x$ | 0 | 1 | 2 |
|---|---|---|---|
| $\text{P} ( X = x )$ | 0.4 | 0.1 | 0.5 |

(i)

$S$ can be 0, 1, 2, 3 or 4. List the ordered pairs of spins for each total

$\text{P} ( S = 0 ) = \text{P} ( 0 ,  0 ) = 0 . 4 \times 0 . 4 = 0 . 16$

$\text{P} ( S = 1 ) = \text{P} ( 0 ,  1 ) + \text{P} ( 1 ,  0 ) = 2 \times 0 . 4 \times 0 . 1 = 0 . 08$

$\text{P} ( S = 2 ) = \text{P} ( 0 ,  2 ) + \text{P} ( 1 ,  1 ) + \text{P} ( 2 ,  0 ) = 0 . 4 \times 0 . 5 + 0 . 1 \times 0 . 1 + 0 . 5 \times 0 . 4 = 0 . 41$

$\text{P} ( S = 3 ) = \text{P} ( 1 ,  2 ) + \text{P} ( 2 ,  1 ) = 2 \times 0 . 1 \times 0 . 5 = 0 . 1$

$\text{P} ( S = 4 ) = \text{P} ( 2 ,  2 ) = 0 . 5 \times 0 . 5 = 0 . 25$

| $s$ | **Final answer:** **0** | **Final answer:** **1** | **Final answer:** **2** | **Final answer:** **3** | **Final answer:** **4** |
|---|---|---|---|---|---|
| $\text{P} ( S = s )$ | **Final answer:** **0.16** | **Final answer:** **0.08** | **Final answer:** **0.41** | **Final answer:** **0.1** | **Final answer:** **0.25** |

**[B1 B1 B1]**

(ii)

$T$ is double one spin, so $T = 0 ,  2 \text{or} 4$ with the probabilities of $X = 0 ,  1 \text{or} 2$

| $t$ | **Final answer:** **0** | **Final answer:** **2** | **Final answer:** **4** |
|---|---|---|---|
| $\text{P} ( T = t )$ | **Final answer:** **0.4** | **Final answer:** **0.1** | **Final answer:** **0.5** |

**[B1]**

> **[mark-scheme]**
> **B1**: Table for $S$ with the values 0, 1, 2, 3 and 4 and at least one correct probability.
> 
> **B1**: Two further probabilities for $S$ correct. $\text{P} ( S = 2 )$ needs all three scenarios, (0, 2), (1, 1) and (2, 0).
> 
> **B1**: All five probabilities for $S$ correct.
> 
> **B1**: Table for $T$ with the values 0, 2 and 4 and the probabilities 0.4, 0.1 and 0.5.
| $s$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $\text{P} ( S = s )$ | 0.16 | 0.08 | 0.41 | 0.1 | 0.25 |

| $t$ | 0 | 2 | 4 |
|---|---|---|---|
| $\text{P} ( T = t )$ | 0.4 | 0.1 | 0.5 |

Find each player's probability of scoring more than 2

$\text{P} ( S > 2 ) = 0 . 1 + 0 . 25 = 0 . 35$

$\text{P} ( T > 2 ) = \text{P} ( T = 4 ) = 0 . 5$

Compare the two probabilities

$0 . 5 > 0 . 35$

**Final answer:** **Tommy is more likely to get a score greater than 2**

**[B1]**

> **[mark-scheme]**
> **B1**: Both probabilities, 0.35 and 0.5, compared, with the conclusion that Tommy is more likely. A conclusion with no probabilities seen does not score.

### Q6
The values and their probabilities are symmetrical about $- 1$

$\text{E} ( X ) = - 1$

**[B1]**

> **[mark-scheme]**
> **B1**: $\text{E} ( X ) = - 1$.
Use `\text{Var}(X) = \text{E}(X^{2}) - \left[\text{E}(X)\right]^{2}`

`\text{Var}(X) = 3.4 - \left(-1\right)^{2}`

$\text{Var} ( X ) = 2 . 4$

**[B1]**

> **[mark-scheme]**
> **B1**: 2.4, using the value of $\text{E} ( X )$ from part (a) in `3.4 - \left[\text{E}(X)\right]^{2}`.
The probabilities sum to 1

$p + q + 0 . 1 + q + p = 1$

$p + q = 0 . 45$

**[B1]**

Use $\text{E} ( X^{2} ) = \sum x^{2} p$ and set it equal to 3.4

`\left(-3\right)^{2}p + \left(-2\right)^{2}q + \left(-1\right)^{2} \times 0.1 + 0^{2} \times q + 1^{2} \times p = 3.4`

$10 p + 4 q + 0 . 1 = 3 . 4$

$5 p + 2 q = 1 . 65$

**[B1]**

Multiply the first equation by 2

$2 p + 2 q = 0 . 9$

Subtract this from $5 p + 2 q = 1 . 65$ to eliminate $q$

$3 p = 0 . 75$

**[M1]**

$p = 0 . 25$

Substitute into $p + q = 0 . 45$

$p = 0 . 25 ,  q = 0 . 2$

**[A1]**

> **[mark-scheme]**
> **B1**: $p + q = 0 . 45$, or any equivalent, from the probabilities summing to 1 or from $\text{E} ( X ) = - 1$.
> 
> **B1**: A correct equation from $\text{E} ( X^{2} ) = 3 . 4$, with all five terms, simplified or unsimplified (e.g. $10 p + 4 q + 0 . 1 = 3 . 4$).
> 
> **M1**: Solving the two equations by substitution or elimination to find one of the unknowns.
> 
> **A1**: $p = 0 . 25$ and $q = 0 . 2$.

### Q7
$X$ has six equally likely values, and the probabilities sum to 1

$6 p = 1$

$p = \frac{1}{6}$

**[B1]**

For $Y$, the probabilities also sum to 1

$\frac{q}{1} + \frac{q}{3} + \frac{q}{6} = 1$

**[M1]**

$\frac{3q}{2} = 1$

$q = \frac{2}{3}$

**[A1]**

> **[mark-scheme]**
> **B1**: $p = \frac{1}{6}$.
> 
> **M1**: Sum of the three probabilities for $Y$ in terms of $q$ set equal to 1.
> 
> **A1**: $q = \frac{2}{3}$.
Each value of $X$ has probability $\frac{1}{6}$. Substitute $q = \frac{2}{3}$ into $\frac{q}{y}$ to find the probabilities for $Y$

| $y$ | 1 | 3 | 6 |
|---|---|---|---|
| $\text{P} ( Y = y )$ | $\frac{2}{3}$ | $\frac{2}{9}$ | $\frac{1}{9}$ |

Split by the value of $Y$: for each one, count the values of $X$ that are bigger

$\text{P} ( Y = 1 \text{and} X > 1 ) = \frac{2}{3} \times \frac{5}{6} = \frac{30}{54}$

**[B1]**

$\text{P} ( Y = 3 \text{and} X > 3 ) = \frac{2}{9} \times \frac{3}{6} = \frac{6}{54}$

$\text{P} ( Y = 6 \text{and} X > 6 ) = \frac{1}{9} \times \frac{2}{6} = \frac{2}{54}$

Add the three scenarios

$\text{P} ( X > Y ) = \frac{30}{54} + \frac{6}{54} + \frac{2}{54} = \frac{38}{54}$

**[M1]**

$\text{P} ( X > Y ) = \frac{19}{27}$

**[A1]**

> **[exam-tip]**
> Splitting by the variable with fewer values keeps the number of cases down. Here conditioning on $Y$ gives three cases; listing by $X$ gives six, and it is easy to miss that $X = 8$ and $X = 11$ beat every value of $Y$.

> **[mark-scheme]**
> **B1**: One correct scenario probability, e.g. $\frac{2}{3} \times \frac{5}{6}$, or a single pair such as $\frac{1}{6} \times \frac{2}{3}$ for $X = 2 ,  Y = 1$.
> 
> **M1**: All the scenarios with $X > Y$ added, with none repeated or missing. Listing by the value of $X$ is equally valid.
> 
> **A1**: $\frac{19}{27}$, or answers which round to 0.704.

### Q8
The probabilities sum to 1

$\frac{5}{12} + p + \frac{1}{4} = 1$

$p = \frac{1}{3}$

**[B1]**

> **[mark-scheme]**
> **B1**: $p = \frac{1}{3}$.
| $x$ | −1 | 1 | 2 |
|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{5}{12}$ | $\frac{1}{3}$ | $\frac{1}{4}$ |

A total of −2, 2 or 4 needs the same value twice, so square that probability

`\text{P}(Y = -2) = \left(\dfrac{5}{12}\right)^{2} = \dfrac{25}{144}`

`\text{P}(Y = 2) = \left(\dfrac{1}{3}\right)^{2} = \dfrac{16}{144}`

`\text{P}(Y = 4) = \left(\dfrac{1}{4}\right)^{2} = \dfrac{9}{144}`

A total of 0, 1 or 3 needs two different values, which can come in either order, so double the product

$\text{P} ( Y = 0 ) = 2 \times \frac{5}{12} \times \frac{1}{3} = \frac{40}{144}$

$\text{P} ( Y = 1 ) = 2 \times \frac{5}{12} \times \frac{1}{4} = \frac{30}{144}$

$\text{P} ( Y = 3 ) = 2 \times \frac{1}{3} \times \frac{1}{4} = \frac{24}{144}$

| $y$ | −2 | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| $\text{P} ( Y = y )$ | $\frac{25}{144}$ | $\frac{40}{144}$ | $\frac{30}{144}$ | $\frac{16}{144}$ | $\frac{24}{144}$ | $\frac{9}{144}$ |

**[B1 B1 B1]**

> **[mark-scheme]**
> **B1**: At least one probability correct and linked to its value of $y$.
> 
> **B1**: At least three further probabilities correct. A total from two different values, such as $\text{P} ( Y = 0 )$, needs both orders ($2 \times$ the product).
> 
> **B1**: All six probabilities correct. Simplified fractions (such as $\frac{5}{18}$, $\frac{5}{24}$, $\frac{1}{9}$, $\frac{1}{6}$, $\frac{1}{16}$) and decimals correct to 3 significant figures are accepted.
| $y$ | −2 | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| $\text{P} ( Y = y )$ | $\frac{25}{144}$ | $\frac{40}{144}$ | $\frac{30}{144}$ | $\frac{16}{144}$ | $\frac{24}{144}$ | $\frac{9}{144}$ |

(i)

Subtract $\text{P} ( Y = 0 )$ from 1

$\text{P} ( Y \neq 0 ) = 1 - \frac{40}{144} = \frac{104}{144}$

$\text{P} ( Y \neq 0 ) = \frac{13}{18}$

**[B1]**

(ii)

$Y < 0$ or $Y \geq 2$ means $Y = - 2 ,  2 ,  3 \text{or} 4$

$\text{P} ( Y < 0 \text{or} Y \geq 2 ) = \frac{25}{144} + \frac{16}{144} + \frac{24}{144} + \frac{9}{144} = \frac{74}{144}$

**[M1]**

$\text{P} ( Y < 0 \text{or} Y \geq 2 ) = \frac{37}{72}$

**[A1]**

> **[mark-scheme]**
> **B1**: $\frac{13}{18}$, or equivalent such as $\frac{104}{144}$, or answers which round to 0.722.
> 
> **M1**: The probabilities for $y = - 2 ,  2 ,  3 \text{and} 4$ added, using the values in the table.
> 
> **A1**: $\frac{37}{72}$, or equivalent such as $\frac{74}{144}$, or answers which round to 0.514.

### Q9
For a probability distribution, the probabilities must sum to 1. Add the four probabilities

`\dfrac{\left(-1\right)^{2}}{30} + \dfrac{1^{2}}{30} + \dfrac{3^{2}}{30} + \dfrac{5^{2}}{30} = \dfrac{1 + 1 + 9 + 25}{30}`

**[M1]**

$= \frac{36}{30} = \frac{6}{5}$

**Final answer:** **The probabilities sum to 6/5, not 1, so this cannot be the probability distribution of X**

**[A1]**

> **[mark-scheme]**
> **M1**: The four probabilities added, with each value of $x$ substituted.
> 
> **A1**: A total of $\frac{36}{30}$ or $\frac{6}{5}$ (or 1.2), with the conclusion that the probabilities do not sum to 1.
The probabilities sum to 1

`\dfrac{\left(-1\right)^{2}}{k} + \dfrac{1^{2}}{k} + \dfrac{3^{2}}{k} + \dfrac{5^{2}}{k} = 1`

**[M1]**

$\frac{36}{k} = 1$

$k = 36$

**[A1]**

> **[mark-scheme]**
> **M1**: Sum of the four probabilities in terms of $k$ set equal to 1.
> 
> **A1**: $k = 36$.
Every value except $- 1$ is positive, so subtract $\text{P} ( X = - 1 )$ from 1

`\text{P}(X > 0) = 1 - \text{P}(X = -1) = 1 - \dfrac{\left(-1\right)^{2}}{36}`

**[M1]**

$\text{P} ( X > 0 ) = \frac{35}{36}$

**[A1]**

> **[mark-scheme]**
> **M1**: $1 - \text{P} ( X = - 1 )$, or $\text{P} ( X = 1 ) + \text{P} ( X = 3 ) + \text{P} ( X = 5 )$, using the value of $k$ found.
> 
> **A1**: $\frac{35}{36}$, or answers which round to 0.972.

### Q10
Look at how the values and their probabilities are arranged around 2

**Final answer:** **The values of x are symmetrical about 2 and so are their probabilities, so the distribution is symmetrical about 2 and E(X) = 2**

**[B1]**

> **[mark-scheme]**
> **B1**: A statement that the distribution (both the values and their probabilities) is symmetrical about 2.
The probabilities sum to 1

$p + \frac{2}{15} + \frac{1}{4} + \frac{2}{15} + p = 1$

$2 p + \frac{31}{60} = 1$

$p = \frac{29}{120}$

**[B1]**

> **[mark-scheme]**
> **B1**: $p = \frac{29}{120}$, or answers which round to 0.242.
| $x$ | −2 | 0 | 2 | 4 | 6 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{29}{120}$ | $\frac{2}{15}$ | $\frac{1}{4}$ | $\frac{2}{15}$ | $\frac{29}{120}$ |

Use `\text{Var}(X) = \sum x^{2}p - \left[\text{E}(X)\right]^{2}` with $\text{E} ( X ) = 2$

`\text{Var}(X) = \left(-2\right)^{2} \times \dfrac{29}{120} + 0^{2} \times \dfrac{2}{15} + 2^{2} \times \dfrac{1}{4} + 4^{2} \times \dfrac{2}{15} + 6^{2} \times \dfrac{29}{120} - 2^{2}`

**[M1]**

$\text{Var} ( X ) = \frac{64}{5} - 4$

$\text{Var} ( X ) = \frac{44}{5}$

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x^{2} p$ with the value of $p$ found, minus $2^{2}$. Accept unsimplified.
> 
> **A1**: $\frac{44}{5}$ or 8.8.
| $x$ | −2 | 0 | 2 | 4 | 6 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{29}{120}$ | $\frac{2}{15}$ | $\frac{1}{4}$ | $\frac{2}{15}$ | $\frac{29}{120}$ |

$\text{E} ( X ) = 2$, so the values greater than the mean are 4 and 6

$\text{P} ( X > 2 ) = \text{P} ( X = 4 ) + \text{P} ( X = 6 ) = \frac{2}{15} + \frac{29}{120}$

**[M1]**

$\text{P} ( X > 2 ) = \frac{16}{120} + \frac{29}{120} = \frac{45}{120}$

`\text{P}\left(X > \text{E}(X)\right) = \dfrac{3}{8}`

**[A1]**

> **[mark-scheme]**
> **M1**: $\text{P} ( X = 4 ) + \text{P} ( X = 6 )$ with the value of $p$ found.
> 
> **A1**: $\frac{3}{8}$ or 0.375.

### Q11
For each coin, $\text{P} ( \text{head} ) = \frac{3}{5}$ and $\text{P} ( \text{tail} ) = \frac{2}{5}$. List the outcomes by the number of heads, and find $X$ for each

*3 heads, 0 tails (HHH): X = 3*

*2 heads, 1 tail (HHT, HTH, THH): X = 1*

*1 head, 2 tails (HTT, THT, TTH): X = −1*

*0 heads, 3 tails (TTT): X = −3*

Multiply the probabilities for each outcome, and count the arrangements

`\text{P}(X = 3) = \left(\dfrac{3}{5}\right)^{3} = \dfrac{27}{125}`

`\text{P}(X = 1) = 3 \times \left(\dfrac{3}{5}\right)^{2} \times \dfrac{2}{5} = \dfrac{54}{125}`

`\text{P}(X = -1) = 3 \times \dfrac{3}{5} \times \left(\dfrac{2}{5}\right)^{2} = \dfrac{36}{125}`

`\text{P}(X = -3) = \left(\dfrac{2}{5}\right)^{3} = \dfrac{8}{125}`

| $x$ | **Final answer:** **−3** | **Final answer:** **−1** | **Final answer:** **1** | **Final answer:** **3** |
|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{8}{125}$ | $\frac{36}{125}$ | $\frac{54}{125}$ | $\frac{27}{125}$ |

**[B1 B1 B1]**

> **[mark-scheme]**
> **B1**: Table with the values −3, −1, 1 and 3 only, and at least one correct probability.
> 
> **B1**: Two of the four probabilities correct.
> 
> **B1**: All four probabilities correct, or four probabilities which sum to 1 with at least two correct. Decimals correct to 3 significant figures (0.064, 0.288, 0.432, 0.216) are accepted.

### Q12
Write $\text{P} ( X = 3 ) = 3 k$ and $\text{P} ( X = 6 ) = 6 k$, then set the sum of the six probabilities equal to 1

$0 . 21 + 0 . 21 + 3 k + 6 k + 0 . 11 + 0 . 11 = 1$

**[M1]**

$9 k + 0 . 64 = 1$

$k = 0 . 04$

**[A1]**

> **[mark-scheme]**
> **M1**: All six probabilities, with $3 k$ and $6 k$, added and set equal to 1. Accept unsimplified.
> 
> **A1**: $k = 0 . 04$.
Substitute $k = 0 . 04$ for $x = 3$ and $x = 6$

$\text{P} ( X = 3 ) = 3 \times 0 . 04 = 0 . 12$

$\text{P} ( X = 6 ) = 6 \times 0 . 04 = 0 . 24$

| $x$ | **Final answer:** **0** | **Final answer:** **1** | **Final answer:** **3** | **Final answer:** **6** | **Final answer:** **10** | **Final answer:** **15** |
|---|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | **Final answer:** **0.21** | **Final answer:** **0.21** | **Final answer:** **0.12** | **Final answer:** **0.24** | **Final answer:** **0.11** | **Final answer:** **0.11** |

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Table with all six values of $x$ and at least one correct probability.
> 
> **B1**: All six probabilities correct, using the value of $k$ found, if it gives a total of 1.
| $x$ | 0 | 1 | 3 | 6 | 10 | 15 |
|---|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | 0.21 | 0.21 | 0.12 | 0.24 | 0.11 | 0.11 |

$3 < X \leq 14$ excludes 3 and 15, so $X = 6 \text{or} 10$

$\text{P} ( 3 < X \leq 14 ) = 0 . 24 + 0 . 11$

$\text{P} ( 3 < X \leq 14 ) = 0 . 35$

**[B1]**

> **[mark-scheme]**
> **B1**: 0.35.

### Q13
The probabilities sum to 1

$p + p + 0 . 2 + 0 . 1 + q = 1$

$2 p + q = 0 . 7$

**[B1]**

Use $\text{E} ( X ) = \sum x p$ and set it equal to 2.45

$0 \times p + 1 \times p + 2 \times 0 . 2 + 3 \times 0 . 1 + 4 q = 2 . 45$

$p + 4 q = 1 . 75$

**[B1]**

Multiply the first equation by 4 and subtract the second to eliminate $q$

$8 p + 4 q - ( p + 4 q ) = 2 . 8 - 1 . 75$

$7 p = 1 . 05$

**[M1]**

$p = 0 . 15$

Substitute into $2 p + q = 0 . 7$

$q = 0 . 7 - 2 \times 0 . 15$

$p = 0 . 15 ,  q = 0 . 4$

**[A1]**

> **[mark-scheme]**
> **B1**: A correct equation from the probabilities summing to 1, simplified or unsimplified.
> 
> **B1**: A correct equation from $\text{E} ( X ) = 2 . 45$, simplified or unsimplified.
> 
> **M1**: Solving the two equations by substitution or elimination to find one of the unknowns.
> 
> **A1**: $p = 0 . 15$ and $q = 0 . 4$.
| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | 0.15 | 0.15 | 0.2 | 0.1 | 0.4 |

Use `\text{Var}(X) = \sum x^{2}p - \left[\text{E}(X)\right]^{2}`

$\text{Var} ( X ) = 0^{2} \times 0 . 15 + 1^{2} \times 0 . 15 + 2^{2} \times 0 . 2 + 3^{2} \times 0 . 1 + 4^{2} \times 0 . 4 - 2 . 45^{2}$

**[M1]**

$\text{Var} ( X ) = 8 . 25 - 6 . 0025$

$\text{Var} ( X ) = 2 . 2475$

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x^{2} p$ with the values of $p$ and $q$ found, minus $2 . 45^{2}$. Accept unsimplified.
> 
> **A1**: 2.2475, or answers which round to 2.25.
| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | 0.15 | 0.15 | 0.2 | 0.1 | 0.4 |

$\text{E} ( X ) = 2 . 45$, so the values less than the mean are 0, 1 and 2

$\text{P} ( X < 2 . 45 ) = \text{P} ( X = 0 ) + \text{P} ( X = 1 ) + \text{P} ( X = 2 ) = 0 . 15 + 0 . 15 + 0 . 2$

**[M1]**

`\text{P}\left(X < \text{E}(X)\right) = 0.5`

**[A1]**

> **[mark-scheme]**
> **M1**: $\text{P} ( X = 0 ) + \text{P} ( X = 1 ) + \text{P} ( X = 2 )$ with the value of $p$ found.
> 
> **A1**: 0.5.

### Q14
The game stops at the first 6, so each earlier roll must be "not 6", with probability $\frac{5}{6}$

$\text{P} ( X = 1 ) = \frac{1}{6} = \frac{36}{216}$

$\text{P} ( X = 2 ) = \frac{5}{6} \times \frac{1}{6} = \frac{5}{36} = \frac{30}{216}$

`\text{P}(X = 3) = \left(\dfrac{5}{6}\right)^{2} \times \dfrac{1}{6} = \dfrac{25}{216}`

The game always stops after the fourth roll, so $X = 4$ only needs the first three rolls to be "not 6"

`\text{P}(X = 4) = \left(\dfrac{5}{6}\right)^{3} = \dfrac{125}{216}`

| $x$ | **Final answer:** **1** | **Final answer:** **2** | **Final answer:** **3** | **Final answer:** **4** |
|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{6}$ | $\frac{5}{36}$ | $\frac{25}{216}$ | $\frac{125}{216}$ |

**[B1 B1 B1 B1]**

> **[exam-tip]**
> The fourth roll ends the game whether or not it is a 6, so there is no final $\frac{1}{6}$ in $\text{P} ( X = 4 )$. A quick check is that your four probabilities sum to 1; with an extra factor of $\frac{1}{6}$ they would not.

> **[mark-scheme]**
> **B1**: Table with the values 1, 2, 3 and 4 only, and at least one correct probability.
> 
> **B1**: $\text{P} ( X = 2 ) = \frac{5}{36}$ correct.
> 
> **B1**: $\text{P} ( X = 3 ) = \frac{25}{216}$ correct.
> 
> **B1**: $\text{P} ( X = 4 ) = \frac{125}{216}$ correct, or four probabilities which sum to 1. Decimals correct to 3 significant figures are accepted throughout.
| $x$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{6}$ | $\frac{5}{36}$ | $\frac{25}{216}$ | $\frac{125}{216}$ |

(i)

"At most 3 times" is every outcome except $X = 4$

$\text{P} ( X \leq 3 ) = 1 - \text{P} ( X = 4 ) = 1 - \frac{125}{216}$

$\text{P} ( X \leq 3 ) = \frac{91}{216}$

**[B1]**

(ii)

"At least 3 times" means $X = 3$ or $X = 4$

$\text{P} ( X \geq 3 ) = \frac{25}{216} + \frac{125}{216} = \frac{150}{216}$

$\text{P} ( X \geq 3 ) = \frac{25}{36}$

**[B1]**

> **[mark-scheme]**
> **B1**: $\frac{91}{216}$, or answers which round to 0.421.
> 
> **B1**: $\frac{25}{36}$, or equivalent such as $\frac{150}{216}$, or answers which round to 0.694.
| $x$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{6}$ | $\frac{5}{36}$ | $\frac{25}{216}$ | $\frac{125}{216}$ |

The mean of $X$ is its expected value, so use $\text{E} ( X ) = \sum x p$, with every probability over 216

$\text{E} ( X ) = 1 \times \frac{36}{216} + 2 \times \frac{30}{216} + 3 \times \frac{25}{216} + 4 \times \frac{125}{216}$

**[M1]**

**Final answer:** $\text{E} ( X ) = \frac{671}{216} = 3 . 11$** (3 s.f.)**

**[A1]**

Use `\text{Var}(X) = \sum x^{2}p - \left[\text{E}(X)\right]^{2}`

`\text{Var}(X) = 1^{2} \times \dfrac{36}{216} + 2^{2} \times \dfrac{30}{216} + 3^{2} \times \dfrac{25}{216} + 4^{2} \times \dfrac{125}{216} - \left(\dfrac{671}{216}\right)^{2}`

**[M1]**

`\text{Var}(X) = \dfrac{2381}{216} - \left(\dfrac{671}{216}\right)^{2} = 1.37292\ldots`

The standard deviation is the square root of the variance

$\sqrt{1.37292\dots} = 1 . 17171 \dots$

**Final answer:** $\text{Standard deviation} = 1 . 17$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x p$ with all four terms from the table. Accept unsimplified.
> 
> **A1**: Mean of $\frac{671}{216}$, or answers which round to 3.11.
> 
> **M1**: $\sum x^{2} p$ minus the square of the mean. Accept unsimplified.
> 
> **A1**: Standard deviation which rounds to 1.17.

### Q15
The six probabilities sum to 1

$\frac{6}{20} + p + \frac{3}{20} + \frac{5}{20} + \frac{3}{20} + \frac{1}{20} = 1$

$p + \frac{18}{20} = 1$

$p = \frac{2}{20}$

**[B1]**

> **[mark-scheme]**
> **B1**: $p = \frac{2}{20}$, or equivalent such as $\frac{1}{10}$ or 0.1.
| Number on sector | 0 | 1 | 1 | 2 | 3 | 5 |
|---|---|---|---|---|---|---|
| Probability | $\frac{6}{20}$ | $\frac{2}{20}$ | $\frac{3}{20}$ | $\frac{5}{20}$ | $\frac{3}{20}$ | $\frac{1}{20}$ |

(i)

"No more than 1" means $X = 0$ or $X = 1$, and a score of 1 comes from either sector labelled 1

$\text{P} ( X \leq 1 ) = \frac{6}{20} + \frac{2}{20} + \frac{3}{20}$

$\text{P} ( X \leq 1 ) = \frac{11}{20}$

**[B1]**

(ii)

"At least 3" means $X = 3$ or $X = 5$

$\text{P} ( X \geq 3 ) = \frac{3}{20} + \frac{1}{20}$

$\text{P} ( X \geq 3 ) = \frac{1}{5}$

**[B1]**

> **[mark-scheme]**
> **B1**: $\frac{11}{20}$ or 0.55.
> 
> **B1**: $\frac{1}{5}$, $\frac{4}{20}$ or 0.2.
Combine the two sectors labelled 1

$\text{P} ( X = 1 ) = \frac{2}{20} + \frac{3}{20} = \frac{5}{20}$

| Number on sector | 0 | 1 | 2 | 3 | 5 |
|---|---|---|---|---|---|
| Probability | $\frac{6}{20}$ | $\frac{5}{20}$ | $\frac{5}{20}$ | $\frac{3}{20}$ | $\frac{1}{20}$ |

The mean of $X$ is its expected value, so use $\text{E} ( X ) = \sum x p$

$\text{E} ( X ) = 0 \times \frac{6}{20} + 1 \times \frac{5}{20} + 2 \times \frac{5}{20} + 3 \times \frac{3}{20} + 5 \times \frac{1}{20}$

**[M1]**

$\text{E} ( X ) = \frac{29}{20} = 1 . 45$

**[A1]**

Use `\text{Var}(X) = \sum x^{2}p - \left[\text{E}(X)\right]^{2}`

$\text{Var} ( X ) = 0^{2} \times \frac{6}{20} + 1^{2} \times \frac{5}{20} + 2^{2} \times \frac{5}{20} + 3^{2} \times \frac{3}{20} + 5^{2} \times \frac{1}{20} - 1 . 45^{2}$

**[M1]**

$\text{Var} ( X ) = \frac{77}{20} - 2 . 1025 = 1 . 7475$

The standard deviation is the square root of the variance

$\sqrt{1.7475} = 1 . 32193 \dots$

**Final answer:** $\text{Standard deviation} = 1 . 32$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x p$ with all terms, using the value of $p$ found. Accept unsimplified.
> 
> **A1**: Mean of $\frac{29}{20}$ or 1.45.
> 
> **M1**: $\sum x^{2} p$ minus the square of the mean. Accept unsimplified.
> 
> **A1**: Standard deviation which rounds to 1.32. The exact form $\frac{\sqrt{699}}{20}$ is also accepted.
| Number on sector | 0 | 1 | 2 | 3 | 5 |
|---|---|---|---|---|---|
| Probability | $\frac{6}{20}$ | $\frac{5}{20}$ | $\frac{5}{20}$ | $\frac{3}{20}$ | $\frac{1}{20}$ |

A total of 5 comes from four ordered scenarios: (0, 5), (5, 0), (2, 3) and (3, 2)

$\text{P} ( 0 ,  5 ) = \text{P} ( 5 ,  0 ) = \frac{6}{20} \times \frac{1}{20} = \frac{6}{400}$

**[B1]**

$\text{P} ( 2 ,  3 ) = \text{P} ( 3 ,  2 ) = \frac{5}{20} \times \frac{3}{20} = \frac{15}{400}$

Add the four scenarios

$\text{P} ( \text{total} = 5 ) = \frac{6}{400} + \frac{6}{400} + \frac{15}{400} + \frac{15}{400} = \frac{42}{400}$

**[M1]**

$\text{P} ( \text{total} = 5 ) = \frac{21}{200}$

**[A1]**

> **[mark-scheme]**
> **B1**: One scenario probability correct, e.g. $\frac{6}{20} \times \frac{1}{20}$.
> 
> **M1**: The probabilities of all four scenarios added, with none repeated or missing.
> 
> **A1**: $\frac{21}{200}$ or 0.105.

### Q16
The six probabilities sum to 1

$0 . 23 + 0 . 23 + k + k + 0 . 13 + 0 . 13 = 1$

**[M1]**

$2 k + 0 . 72 = 1$

$k = 0 . 14$

**[A1]**

> **[mark-scheme]**
> **M1**: All six probabilities added and set equal to 1. Accept unsimplified.
> 
> **A1**: $k = 0 . 14$.
Use $k = 0 . 14$ for $x = 0$ and $x = 2$

| $x$ | **Final answer:** **−1** | **Final answer:** **0** | **Final answer:** **1** | **Final answer:** **2** | **Final answer:** **3** | **Final answer:** **4** |
|---|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | **Final answer:** **0.23** | **Final answer:** **0.14** | **Final answer:** **0.13** | **Final answer:** **0.14** | **Final answer:** **0.13** | **Final answer:** **0.23** |

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Table with all six values of $x$ and at least one correct probability.
> 
> **B1**: All six probabilities correct, using the value of $k$ found, if it gives a total of 1.
| $x$ | −1 | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | 0.23 | 0.14 | 0.13 | 0.14 | 0.13 | 0.23 |

$0 \leq X < 3$ includes 0 but excludes 3, so $X = 0 ,  1 \text{or} 2$

$\text{P} ( 0 \leq X < 3 ) = 0 . 14 + 0 . 13 + 0 . 14$

$\text{P} ( 0 \leq X < 3 ) = 0 . 41$

**[B1]**

> **[mark-scheme]**
> **B1**: 0.41.

### Q17
(i)

Only $X = 4$ fails $X < 4$, so subtract its probability from 1

$\text{P} ( X < 4 ) = 1 - \text{P} ( X = 4 ) = 1 - \frac{1}{8}$

$\text{P} ( X < 4 ) = \frac{7}{8}$

**[B1]**

(ii)

$X > 1$ means $X = 2 ,  3 \text{or} 4$

$\text{P} ( X > 1 ) = \frac{1}{4} + \frac{1}{12} + \frac{1}{8} = \frac{6}{24} + \frac{2}{24} + \frac{3}{24}$

$\text{P} ( X > 1 ) = \frac{11}{24}$

**[B1]**

(iii)

$2 < X \leq 4$ excludes 2 but includes 4, so $X = 3 \text{or} 4$

$\text{P} ( 2 < X \leq 4 ) = \frac{1}{12} + \frac{1}{8} = \frac{2}{24} + \frac{3}{24}$

$\text{P} ( 2 < X \leq 4 ) = \frac{5}{24}$

**[B1]**

(iv)

$0 < X < 4$ means $X = 1 ,  2 \text{or} 3$

$\text{P} ( 0 < X < 4 ) = \frac{1}{3} + \frac{1}{4} + \frac{1}{12} = \frac{8}{12}$

$\text{P} ( 0 < X < 4 ) = \frac{2}{3}$

**[B1]**

> **[mark-scheme]**
> **B1**: $\frac{7}{8}$ for $\text{P} ( X < 4 )$.
> 
> **B1**: $\frac{11}{24}$ for $\text{P} ( X > 1 )$.
> 
> **B1**: $\frac{5}{24}$ for $\text{P} ( 2 < X \leq 4 )$.
> 
> **B1**: $\frac{2}{3}$ for $\text{P} ( 0 < X < 4 )$.
> 
> Equivalent fractions, and decimals which round to the correct 3 significant figure values, are accepted throughout.

### Q18
Write each probability in terms of $k$ and set their sum equal to 1

$k + 3 k + 5 k + 7 k = 1$

**[M1]**

$16 k = 1$

$k = \frac{1}{16}$

**[A1]**

> **[mark-scheme]**
> **M1**: Sum of the four probabilities in terms of $k$ set equal to 1. Accept unsimplified.
> 
> **A1**: $k = \frac{1}{16}$ or 0.0625.
The values greater than 3 are 5 and 7

$\text{P} ( X > 3 ) = \text{P} ( X = 5 ) + \text{P} ( X = 7 ) = \frac{5}{16} + \frac{7}{16}$

**[M1]**

$\text{P} ( X > 3 ) = \frac{3}{4}$

**[A1]**

> **[mark-scheme]**
> **M1**: $\text{P} ( X = 5 ) + \text{P} ( X = 7 )$ using the value of $k$ from part (a), or $1 - \text{P} ( X = 1 ) - \text{P} ( X = 3 )$.
> 
> **A1**: $\frac{3}{4}$, or equivalent such as $\frac{12}{16}$ or 0.75.

### Q19
For each coin, $\text{P} ( \text{head} ) = \frac{2}{3}$ and $\text{P} ( \text{tail} ) = \frac{1}{3}$. List the 8 possible outcomes

*HHH, HHT, HTH, THH, HTT, THT, TTH, TTT*

Three heads can happen in one way

$\text{P} ( X = 3 ) = \frac{2}{3} \times \frac{2}{3} \times \frac{2}{3} = \frac{8}{27}$

Two heads can happen in three ways (HHT, HTH, THH), each with the same probability

$\text{P} ( X = 2 ) = 3 \times \frac{2}{3} \times \frac{2}{3} \times \frac{1}{3} = \frac{12}{27}$

One head can happen in three ways (HTT, THT, TTH)

$\text{P} ( X = 1 ) = 3 \times \frac{2}{3} \times \frac{1}{3} \times \frac{1}{3} = \frac{6}{27}$

No heads can happen in one way

$\text{P} ( X = 0 ) = \frac{1}{3} \times \frac{1}{3} \times \frac{1}{3} = \frac{1}{27}$

| $x$ | **Final answer:** **0** | **Final answer:** **1** | **Final answer:** **2** | **Final answer:** **3** |
|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{27}$ | $\frac{6}{27}$ | $\frac{12}{27}$ | $\frac{8}{27}$ |

**[B1 B1 B1]**

> **[exam-tip]**
> Each coin is an independent trial with the same probability of a head, so $X$ follows the binomial distribution `\text{B}\left(3, \; \dfrac{2}{3}\right)`. The "number of ways" in each line is `^{3}C_{r}`, which saves listing every outcome when there are more coins.

> **[mark-scheme]**
> **B1**: Table with the values 0, 1, 2 and 3 and at least one correct probability.
> 
> **B1**: Two of $\text{P} ( X = 0 )$, $\text{P} ( X = 1 )$ and $\text{P} ( X = 3 )$ correct.
> 
> **B1**: All four probabilities correct, or four probabilities which sum to 1 with $\text{P} ( X = 2 )$ correct. Equivalent fractions such as $\frac{2}{9}$ and $\frac{4}{9}$, or decimals correct to 3 significant figures, are accepted.

### Q20
Use $\text{E} ( X ) = \sum x p$ and set it equal to 0

$- 2 p + 0 \times \frac{1}{2} + 2 q + 4 \times \frac{1}{15} + 6 q = 0$

**[M1]**

$- 2 p + 8 q + \frac{4}{15} = 0$

Rearrange and divide by 2

$2 p - 8 q = \frac{4}{15}$

$p - 4 q = \frac{2}{15}$

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x p$ with all five terms set equal to 0. Accept unsimplified.
> 
> **A1**: $p - 4 q = \frac{2}{15}$ reached from that equation with no errors, since the result is given.
The probabilities sum to 1

$p + \frac{1}{2} + q + \frac{1}{15} + q = 1$

$p + 2 q = \frac{13}{30}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct equation from the probabilities summing to 1, simplified or unsimplified.
The equation from part (a) is

$p - 4 q = \frac{2}{15}$

The equation from part (b) is

$p + 2 q = \frac{13}{30}$

Subtract the equation from part (a) from the equation from part (b) to eliminate $p$

$( p + 2 q ) - ( p - 4 q ) = \frac{13}{30} - \frac{2}{15}$

$6 q = \frac{3}{10}$

**[M1]**

$q = \frac{1}{20}$

Substitute into $p + 2 q = \frac{13}{30}$

$p = \frac{13}{30} - \frac{2}{20} = \frac{13}{30} - \frac{3}{30}$

$p = \frac{1}{3} ,  q = \frac{1}{20}$

**[A1]**

> **[mark-scheme]**
> **M1**: Solving the two equations by substitution or elimination to find one of the unknowns.
> 
> **A1**: $p = \frac{1}{3}$ and $q = \frac{1}{20}$.
| $x$ | −2 | 0 | 2 | 4 | 6 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{3}$ | $\frac{1}{2}$ | $\frac{1}{20}$ | $\frac{1}{15}$ | $\frac{1}{20}$ |

Use `\text{Var}(X) = \sum x^{2}p - \left[\text{E}(X)\right]^{2}` with $\text{E} ( X ) = 0$

`\text{Var}(X) = \left(-2\right)^{2} \times \dfrac{1}{3} + 0^{2} \times \dfrac{1}{2} + 2^{2} \times \dfrac{1}{20} + 4^{2} \times \dfrac{1}{15} + 6^{2} \times \dfrac{1}{20} - 0^{2}`

**[M1]**

$\text{Var} ( X ) = \frac{4}{3} + \frac{1}{5} + \frac{16}{15} + \frac{9}{5}$

$\text{Var} ( X ) = \frac{22}{5}$

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x^{2} p$ with the values of $p$ and $q$ found, minus the square of the mean. Accept unsimplified.
> 
> **A1**: $\frac{22}{5}$ or 4.4.

### Q21
The probabilities sum to 1

$\frac{1}{4} + \frac{1}{3} + p + \frac{1}{6} + \frac{1}{12} = 1$

$p + \frac{10}{12} = 1$

$p = \frac{1}{6}$

**[B1]**

> **[mark-scheme]**
> **B1**: $p = \frac{1}{6}$, or an equivalent such as $\frac{2}{12}$.
| $x$ | 2 | 3 | 5 | 7 | 11 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{4}$ | $\frac{1}{3}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{12}$ |

Use $\text{E} ( X ) = \sum x p$

$\text{E} ( X ) = 2 \times \frac{1}{4} + 3 \times \frac{1}{3} + 5 \times \frac{1}{6} + 7 \times \frac{1}{6} + 11 \times \frac{1}{12}$

**[M1]**

$\text{E} ( X ) = \frac{6+12+10+14+11}{12}$

$\text{E} ( X ) = \frac{53}{12}$

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x p$ with all five products, using the value of $p$ found. Accept unsimplified.
> 
> **A1**: $\frac{53}{12}$, or answers which round to 4.42.
| $x$ | 2 | 3 | 5 | 7 | 11 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{4}$ | $\frac{1}{3}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{12}$ |

Use `\text{Var}(X) = \sum x^{2}p - \left[\text{E}(X)\right]^{2}`, starting with $\sum x^{2} p$

$\sum x^{2} p = 2^{2} \times \frac{1}{4} + 3^{2} \times \frac{1}{3} + 5^{2} \times \frac{1}{6} + 7^{2} \times \frac{1}{6} + 11^{2} \times \frac{1}{12} = \frac{317}{12}$

Subtract the square of the mean from part (b)

`\text{Var}(X) = \dfrac{317}{12} - \left(\dfrac{53}{12}\right)^{2}`

**[M1]**

$\text{Var} ( X ) = \frac{3804}{144} - \frac{2809}{144}$

$\text{Var} ( X ) = \frac{995}{144}$

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x^{2} p$ with all five terms, minus the square of the mean. Accept unsimplified.
> 
> **A1**: $\frac{995}{144}$, or answers which round to 6.91.

### Q22
The probabilities sum to 1

$\frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{5}{16} + p = 1$

$\frac{13}{16} + p = 1$

$p = \frac{3}{16}$

**[B1]**

> **[mark-scheme]**
> **B1**: All five probabilities, including $p$, added and set equal to 1, leading to $p = \frac{3}{16}$. Working `1 - \left(\dfrac{1}{4} + \dfrac{1}{8} + \dfrac{1}{8} + \dfrac{5}{16}\right)` is equivalent. Substituting $\frac{3}{16}$ to check the total does not score.
| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{4}$ | $\frac{1}{8}$ | $\frac{1}{8}$ | $\frac{5}{16}$ | $\frac{3}{16}$ |

Use $\text{E} ( X ) = \sum x p$

$\text{E} ( X ) = 0 \times \frac{1}{4} + 1 \times \frac{1}{8} + 2 \times \frac{1}{8} + 3 \times \frac{5}{16} + 4 \times \frac{3}{16}$

**[M1]**

$\text{E} ( X ) = \frac{0+2+4+15+12}{16}$

$\text{E} ( X ) = \frac{33}{16}$

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x p$ with all five products seen. Accept unsimplified.
> 
> **A1**: $\frac{33}{16}$, or 2.0625, or answers which round to 2.06.
| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{4}$ | $\frac{1}{8}$ | $\frac{1}{8}$ | $\frac{5}{16}$ | $\frac{3}{16}$ |

Use $\text{E} ( X^{2} ) = \sum x^{2} p$

$\text{E} ( X^{2} ) = 0^{2} \times \frac{1}{4} + 1^{2} \times \frac{1}{8} + 2^{2} \times \frac{1}{8} + 3^{2} \times \frac{5}{16} + 4^{2} \times \frac{3}{16}$

**[M1]**

$\text{E} ( X^{2} ) = \frac{0+2+8+45+48}{16}$

$\text{E} ( X^{2} ) = \frac{103}{16}$

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x^{2} p$ with all five products seen.
> 
> **A1**: $\frac{103}{16}$ reached from that sum. As the value is given, every term must be seen.
Use `\text{Var}(X) = \text{E}(X^{2}) - \left[\text{E}(X)\right]^{2}` with $\text{E} ( X^{2} ) = \frac{103}{16}$ from part (c) and $\text{E} ( X ) = \frac{33}{16}$ from part (b)

`\text{Var}(X) = \dfrac{103}{16} - \left(\dfrac{33}{16}\right)^{2}`

**[M1]**

$\text{Var} ( X ) = \frac{1648}{256} - \frac{1089}{256}$

$\text{Var} ( X ) = \frac{559}{256}$

**[A1]**

> **[mark-scheme]**
> **M1**: `\dfrac{103}{16} - \left[\text{E}(X)\right]^{2}`, using the mean from part (b). The square of the mean must be subtracted.
> 
> **A1**: $\frac{559}{256}$, or answers which round to 2.18.

### Q23
(i)

The two dice are independent, so multiply the probabilities of a six on each

$\text{P} ( \text{two sixes} ) = \frac{1}{6} \times \frac{1}{6}$

$\text{P} ( \text{two sixes} ) = \frac{1}{36}$

**[B1]**

(ii)

Two sixes is the event $X = 2$, so use part (i)

$\text{P} ( X = 2 ) = \frac{1}{36}$

The probabilities in the table sum to 1

$\text{P} ( X = 1 ) = 1 - \frac{25}{36} - \frac{1}{36} = \frac{10}{36}$

| $x$ | 0 | 1 | 2 |
|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{25}{36}$ | $\frac{10}{36}$ | $\frac{1}{36}$ |

**[B1 B1]**

> **[mark-scheme]**
> **B1**: $\frac{1}{36}$ for the probability of two sixes. Accept 0.0278.
> 
> **B1**: $\text{P} ( X = 1 ) = \frac{10}{36}$, or any equivalent such as $\frac{5}{18}$ or 0.278. It may come from $2 \times \frac{1}{6} \times \frac{5}{6}$ or from subtracting the other two probabilities from 1.
> 
> **B1**: $\text{P} ( X = 2 ) = \frac{1}{36}$ in the table, or a value which makes the three probabilities sum to 1.
| $x$ | 0 | 1 | 2 |
|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{25}{36}$ | $\frac{10}{36}$ | $\frac{1}{36}$ |

"At least one six" is every outcome except no sixes, so subtract $\text{P} ( X = 0 )$ from 1

$\text{P} ( X \geq 1 ) = 1 - \text{P} ( X = 0 ) = 1 - \frac{25}{36}$

**[M1]**

$\text{P} ( X \geq 1 ) = \frac{11}{36}$

**[A1]**

> **[mark-scheme]**
> **M1**: $1 - \text{P} ( X = 0 )$, or $\text{P} ( X = 1 ) + \text{P} ( X = 2 )$ using the values from the table.
> 
> **A1**: $\frac{11}{36}$, or answers which round to 0.306.

### Q24
Write each probability in terms of $k$ and set their sum equal to 1

$k ( 1 ) + \frac{1}{2} k ( 2 ) + k ( 3 ) + \frac{1}{2} k ( 4 ) = 1$

**[M1]**

$k + k + 3 k + 2 k = 1$

$7 k = 1$

$k = \frac{1}{7}$

**[A1]**

> **[mark-scheme]**
> **M1**: All four probabilities in terms of $k$ added and set equal to 1. Accept unsimplified.
> 
> **A1**: $k = \frac{1}{7}$ reached from that equation. As the value is given, substituting $k = \frac{1}{7}$ to check the probabilities sum to 1 does not score.
Substitute $k = \frac{1}{7}$ into $k x$ for the odd values

$\text{P} ( X = 1 ) = \frac{1}{7}$

$\text{P} ( X = 3 ) = \frac{3}{7}$

and into $\frac{1}{2} k x$ for the even values

$\text{P} ( X = 2 ) = \frac{1}{2} \times 2 \times \frac{1}{7} = \frac{1}{7}$

$\text{P} ( X = 4 ) = \frac{1}{2} \times 4 \times \frac{1}{7} = \frac{2}{7}$

| $x$ | **Final answer:** **1** | **Final answer:** **2** | **Final answer:** **3** | **Final answer:** **4** |
|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{7}$ | $\frac{1}{7}$ | $\frac{3}{7}$ | $\frac{2}{7}$ |

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Table with the values 1, 2, 3 and 4 and at least one correct probability.
> 
> **B1**: All four probabilities correct, as fractions.
| $x$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{7}$ | $\frac{1}{7}$ | $\frac{3}{7}$ | $\frac{2}{7}$ |

Add the probabilities for 1 and 2

$\text{P} ( X \leq 2 ) = \text{P} ( X = 1 ) + \text{P} ( X = 2 ) = \frac{1}{7} + \frac{1}{7} = \frac{2}{7}$

**[M1]**

Compare with the probability for 4 from the table

$\text{P} ( X = 4 ) = \frac{2}{7}$

$\text{P} ( X \leq 2 ) = \text{P} ( X = 4 ) = \frac{2}{7}$

**[A1]**

> **[mark-scheme]**
> **M1**: $\text{P} ( X = 1 ) + \text{P} ( X = 2 )$ evaluated. Working in terms of $k$ ($k + k = 2 k$) is equally valid.
> 
> **A1**: Both sides shown to equal $\frac{2}{7}$ (or $2 k$), with the conclusion that they are equal.

### Q25
Substitute each value of $x$ into $k x$ and set the sum of the probabilities equal to 1

$\text{P} ( X = 2 ) + \text{P} ( X = 3 ) = 1$

$2 k + 3 k = 1$

**[M1]**

$5 k = 1$

$k = \frac{1}{5} = 0 . 2$

**[A1]**

> **[mark-scheme]**
> **M1**: Equation $2 k + 3 k = 1$, or equivalent, from the probabilities summing to 1.
> 
> **A1**: $k = 0 . 2$ reached from that equation. As the value is given, substituting $k = 0 . 2$ to check it does not score.
(i)

The only value of $X$ with $2 \leq X < 3$ is 2

$\text{P} ( 2 \leq X < 3 ) = \text{P} ( X = 2 ) = 2 \times 0 . 2$

$\text{P} ( 2 \leq X < 3 ) = 0 . 4$

**[B1]**

(ii)

$X$ can only take the values 2 and 3, so 5 is impossible

$\text{P} ( X = 5 ) = 0$

**[B1]**

> **[mark-scheme]**
> **B1**: 0.4 for $\text{P} ( 2 \leq X < 3 )$. Accept $\frac{2}{5}$.
> 
> **B1**: 0 for $\text{P} ( X = 5 )$.

### Q26
Multiply each value of $x$ by its probability and add, using $\text{E} ( X ) = \sum x p$

$\text{E} ( X ) = 1 \times \frac{5}{12} + 2 \times \frac{2}{12} + 3 \times \frac{1}{12} + 4 \times \frac{3}{12} + 5 \times \frac{1}{12}$

**[M1]**

$\text{E} ( X ) = \frac{5+4+3+12+5}{12}$

$\text{E} ( X ) = \frac{29}{12}$

**[A1]**

> **[mark-scheme]**
> **M1**: All five products $x p$ written out and added.
> 
> **A1**: $\frac{29}{12}$ reached from that sum. As the value is given, every term must be seen.
Multiply each value of $x^{2}$ by its probability and add, using $\text{E} ( X^{2} ) = \sum x^{2} p$

$\text{E} ( X^{2} ) = 1^{2} \times \frac{5}{12} + 2^{2} \times \frac{2}{12} + 3^{2} \times \frac{1}{12} + 4^{2} \times \frac{3}{12} + 5^{2} \times \frac{1}{12}$

**[M1]**

$\text{E} ( X^{2} ) = \frac{5+8+9+48+25}{12}$

$\text{E} ( X^{2} ) = \frac{95}{12}$

**[A1]**

> **[mark-scheme]**
> **M1**: All five products $x^{2} p$ written out and added.
> 
> **A1**: $\frac{95}{12}$ reached from that sum. As the value is given, every term must be seen.
The variance is the mean of the squares minus the square of the mean

`\text{Var}(X) = \text{E}(X^{2}) - \left[\text{E}(X)\right]^{2}`

**[B1]**

> **[mark-scheme]**
> **B1**: `\text{Var}(X) = \text{E}(X^{2}) - \left[\text{E}(X)\right]^{2}`, or any equivalent form such as $\sum x^{2} p - μ^{2}$.
The formula from part (c) is

`\text{Var}(X) = \text{E}(X^{2}) - \left[\text{E}(X)\right]^{2}`

Substitute $\text{E} ( X^{2} ) = \frac{95}{12}$ from part (b) and $\text{E} ( X ) = \frac{29}{12}$ from part (a)

`\text{Var}(X) = \dfrac{95}{12} - \left(\dfrac{29}{12}\right)^{2}`

$\text{Var} ( X ) = \frac{1140}{144} - \frac{841}{144}$

$\text{Var} ( X ) = \frac{299}{144}$

**[B1]**

> **[mark-scheme]**
> **B1**: `\dfrac{95}{12} - \left(\dfrac{29}{12}\right)^{2}` seen, leading to $\frac{299}{144}$. Both fractions over a common denominator, or equivalent working, must be shown because the result is given.

### Q27
The probabilities sum to 1

$0 . 2 + 0 . 1 + p + p + q = 1$

$2 p + q = 0 . 7$

**[B1]**

> **[mark-scheme]**
> **B1**: All five probabilities added and set equal to 1, leading to $2 p + q = 0 . 7$.
Use $\text{E} ( X ) = \sum x p$ and set it equal to 3.3

$1 \times 0 . 2 + 2 \times 0 . 1 + 3 p + 4 p + 5 q = 3 . 3$

**[M1]**

$0 . 4 + 7 p + 5 q = 3 . 3$

$7 p + 5 q = 2 . 9$

**[A1]**

> **[mark-scheme]**
> **M1**: $\sum x p$ with all five terms, set equal to 3.3. Accept unsimplified.
> 
> **A1**: $7 p + 5 q = 2 . 9$ reached from that equation.
The equation from part (a) is

$2 p + q = 0 . 7$

The equation from part (b) is

$7 p + 5 q = 2 . 9$

Multiply the equation from part (a) by 5 so that $q$ can be eliminated

$10 p + 5 q = 3 . 5$

Subtract the equation from part (b)

$3 p = 0 . 6$

**[M1]**

$p = 0 . 2$

Substitute into $2 p + q = 0 . 7$ to find $q$

$q = 0 . 7 - 2 \times 0 . 2$

$p = 0 . 2 ,  q = 0 . 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Solving the two equations by substitution or elimination to find one of the unknowns.
> 
> **A1**: $p = 0 . 2$ and $q = 0 . 3$. Equivalent fractions are accepted.

### Q28
Set the sum of the five probabilities equal to 1

$\frac{2}{5} + \frac{1}{10} + \frac{1}{5} + p + \frac{1}{10} = 1$

**[M1]**

$p + \frac{4}{5} = 1$

$p = \frac{1}{5}$

**[A1]**

> **[mark-scheme]**
> **M1**: Sum of the five probabilities, including $p$, set equal to 1.
> 
> **A1**: $p = \frac{1}{5}$ or 0.2.
| $x$ | 2 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{2}{5}$ | $\frac{1}{10}$ | $\frac{1}{5}$ | $\frac{1}{5}$ | $\frac{1}{10}$ |

For each probability, pick out the values of $x$ that satisfy the inequality and add their probabilities

(i)

$\text{P} ( X \leq 4 ) = \text{P} ( X = 2 ) + \text{P} ( X = 4 ) = \frac{2}{5} + \frac{1}{10}$

$\text{P} ( X \leq 4 ) = \frac{1}{2}$

**[B1]**

(ii)

$\text{P} ( X > 7 ) = \text{P} ( X = 8 ) + \text{P} ( X = 10 ) = \frac{1}{5} + \frac{1}{10}$

$\text{P} ( X > 7 ) = \frac{3}{10}$

**[B1]**

(iii)

$\text{P} ( 2 \leq X \leq 6 ) = \text{P} ( X = 2 ) + \text{P} ( X = 4 ) + \text{P} ( X = 6 ) = \frac{2}{5} + \frac{1}{10} + \frac{1}{5}$

$\text{P} ( 2 \leq X \leq 6 ) = \frac{7}{10}$

**[B1]**

(iv)

The strict inequalities leave out 2 and 8, so only 4 and 6 are included

$\text{P} ( 3 < X < 7 ) = \text{P} ( X = 4 ) + \text{P} ( X = 6 ) = \frac{1}{10} + \frac{1}{5}$

$\text{P} ( 3 < X < 7 ) = \frac{3}{10}$

**[B1]**

> **[mark-scheme]**
> **B1**: $\frac{1}{2}$ for $\text{P} ( X \leq 4 )$.
> 
> **B1**: $\frac{3}{10}$ for $\text{P} ( X > 7 )$.
> 
> **B1**: $\frac{7}{10}$ for $\text{P} ( 2 \leq X \leq 6 )$.
> 
> **B1**: $\frac{3}{10}$ for $\text{P} ( 3 < X < 7 )$.
> 
> Equivalent decimals are accepted throughout.

### Q29
$X$ takes the values 0, 1, 2 and 3, each with probability $\frac{1}{4}$

| $x$ | **Final answer:** **0** | **Final answer:** **1** | **Final answer:** **2** | **Final answer:** **3** |
|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{4}$ | $\frac{1}{4}$ | $\frac{1}{4}$ | $\frac{1}{4}$ |

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Table with the values 0, 1, 2 and 3 and at least one correct probability.
> 
> **B1**: All four probabilities correct.
| $x$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| $\text{P} ( X = x )$ | $\frac{1}{4}$ | $\frac{1}{4}$ | $\frac{1}{4}$ | $\frac{1}{4}$ |

(i)

The values 1 and 2 satisfy $1 \leq X \leq 2$, so add their probabilities

$\text{P} ( 1 \leq X \leq 2 ) = \text{P} ( X = 1 ) + \text{P} ( X = 2 ) = \frac{1}{4} + \frac{1}{4}$

$\text{P} ( 1 \leq X \leq 2 ) = \frac{1}{2}$

**[B1]**

(ii)

Only $X = 3$ fails $X < 3$, so subtract its probability from 1

$\text{P} ( X < 3 ) = 1 - \text{P} ( X = 3 ) = 1 - \frac{1}{4}$

$\text{P} ( X < 3 ) = \frac{3}{4}$

**[B1]**

> **[mark-scheme]**
> **B1**: $\frac{1}{2}$ or 0.5 for $\text{P} ( 1 \leq X \leq 2 )$.
> 
> **B1**: $\frac{3}{4}$ or 0.75 for $\text{P} ( X < 3 )$. Adding the probabilities for 0, 1 and 2 is equally valid.
