# Mark Schemes — Binomial Expansion
**Series** · Cambridge (CIE) AS maths (9709)


## Exam Questions (38 questions)


### Q1
Use the binomial expansion up to the $x^{2}$ term, with $a = 5$, $b = 2 x$ and $n = 5$

`(5 + 2x)^5 = {}^{5}C_{0}\,5^5 + {}^{5}C_{1}\,5^4(2x) + {}^{5}C_{2}\,5^3(2x)^2 + \cdots`

Evaluate each binomial coefficient and simplify

$= ( 1 ) ( 3125 ) + ( 5 ) ( 625 ) ( 2 x ) + ( 10 ) ( 125 ) ( 4 x^{2} ) + \cdots$

$3125 + 6250 x + 5000 x^{2}$

**[B1 B1 B1]**

> **[mark-scheme]**
> **B1**: Correct constant term $3125$.
> 
> **B1**: Correct term in $x$, namely $6250 x$.
> 
> **B1**: Correct term in $x^{2}$, namely $5000 x^{2}$.
Compare $( 5 . 04 )^{5}$ with $( 5 + 2 x )^{5}$, so you need $5 + 2 x = 5 . 04$, giving $2 x = 0 . 04$ and $x = 0 . 02$

$( 5 . 04 )^{5} \approx 3125 + 6250 ( 0 . 02 ) + 5000 ( 0 . 02 )^{2}$

**[M1]**

Work out each term and add

$= 3125 + 125 + 2$

$( 5 . 04 )^{5} \approx 3252$

**[A1]**

> **[mark-scheme]**
> **M1**: You set $5 + 2 x = 5 . 04$ to get $x = 0 . 02$ and substitute it into your answer from part (a).
> 
> **A1**: Correct estimate $3252$. Answers which round to $3250$ (3 significant figures) are also accepted.

### Q2
Find the two coefficients using the binomial expansion, with $a = p$, $b = x$ and $n = 4$

The term in $x^{2}$ is the $r = 2$ term

`{}^{4}C_{2}\,p^{2}x^{2} = 6p^{2}x^{2}`

**[B1]**

The term in $x$ is the $r = 1$ term

`{}^{4}C_{1}\,p^{3}x = 4p^{3}x`

**[B1]**

The coefficient of $x^{2}$ is twice the coefficient of $x$, so form an equation in $p$

$6 p^{2} = 2 ( 4 p^{3} ) = 8 p^{3}$

**[M1]**

Divide both sides by $2 p^{2}$ (valid since $p \neq 0$) and solve

$3 = 4 p$

$p = \frac{3}{4}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{2}$, namely $6 p^{2}$.
> 
> **B1**: Correct coefficient of $x$, namely $4 p^{3}$.
> 
> **M1**: You form a correct equation from "the coefficient of $x^{2}$ is twice the coefficient of $x$", with the $x$ terms removed, for example $6 p^{2} = 2 ( 4 p^{3} )$.
> 
> **A1**: Correct value $p = \frac{3}{4}$.

### Q3
(i)

The factorial notation means you multiply the whole number by every positive integer below it

$4 ! = 4 \times 3 \times 2 \times 1$

$4 ! = 24$

**[B1]**

(ii)

Use the definition of a binomial coefficient, `{}^{n}C_{r} = \dfrac{n!}{r!(n - r)!}`, with $n = 5$ and $r = 2$

`{}^{5}C_{2} = \dfrac{5!}{2!(5 - 2)!} = \dfrac{120}{12}`

`{}^{5}C_{2} = 10`

**[B1]**

(iii)

Apply the same definition with $n = 6$ and $r = 3$

`{}^{6}C_{3} = \dfrac{6!}{3!(6 - 3)!} = \dfrac{720}{36}`

`{}^{6}C_{3} = 20`

**[B1]**

> **[mark-scheme]**
> **B1**: Correct value $4 ! = 24$, where $4 !$ means $4 \times 3 \times 2 \times 1$.
> 
> **B1**: Correct value `{}^{5}C_{2} = 10`. You can check this using the `{}^{n}C_{r}` button on your calculator.
> 
> **B1**: Correct value `{}^{6}C_{3} = 20`.

### Q4
Use the definition of a binomial coefficient, `{}^{n}C_{r} = \dfrac{n!}{r!(n - r)!}`, with $n = k$ and $r = 1$

`{}^{k}C_{1} = \dfrac{k!}{1!(k - 1)!}`

**[M1]**

Since $1 ! = 1$, write $k ! = k ( k - 1 ) !$ so that the $( k - 1 ) !$ factors cancel

`{}^{k}C_{1} = \dfrac{k(k - 1)!}{(k - 1)!}`

**Final answer:** `{}^{k}C_{1} = k`** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: You set up the binomial coefficient from its definition with $n = k$ and $r = 1$, giving $\frac{k!}{1!(k-1)!}$.
> 
> **A1**: You simplify correctly to reach the printed result `{}^{k}C_{1} = k`, for example by writing $k ! = k ( k - 1 ) !$ and cancelling the $( k - 1 ) !$. Because the answer is given, a concluding statement is expected.

### Q5
Expand using the binomial expansion, using the formula from the list of formulae

`(a + b)^n = a^n + {}^{n}C_{1}\,a^{n - 1}b + {}^{n}C_{2}\,a^{n - 2}b^2 + \cdots + b^n`

Here $a = x$, $b = 2$ and $n = 4$, so write out each term in turn

`(x + 2)^4 = {}^{4}C_{0}\,x^4 + {}^{4}C_{1}\,x^3(2) + {}^{4}C_{2}\,x^2(2)^2 + {}^{4}C_{3}\,x(2)^3 + {}^{4}C_{4}\,(2)^4`

Evaluate the coefficients $1 , 4 , 6 , 4 , 1$ and apply the index laws

$= x^{4} + 4 x^{3} ( 2 ) + 6 x^{2} ( 4 ) + 4 x ( 8 ) + 16$

$( x + 2 )^{4} = x^{4} + 8 x^{3} + 24 x^{2} + 32 x + 16$

**[B1 B1]**

> **[mark-scheme]**
> **B1**: At least three terms of the fully simplified expansion correct.
> 
> **B1**: Completely correct, simplified expansion $x^{4} + 8 x^{3} + 24 x^{2} + 32 x + 16$. This is marked B2,1,0 — one mark is lost for each error.

### Q6
Expand using the binomial expansion, with $a = 2 x$, $b = - 3$ and $n = 6$

$( 2 x - 3 )^{6} = C pre^{6}_{0} ( 2 x )^{6} + C pre^{6}_{1} ( 2 x )^{5} ( - 3 ) + C pre^{6}_{2} ( 2 x )^{4} ( - 3 )^{2} + C pre^{6}_{3} ( 2 x )^{3} ( - 3 )^{3} + C pre^{6}_{4} ( 2 x )^{2} ( - 3 )^{4} + C pre^{6}_{5} ( 2 x ) ( - 3 )^{5} + C pre^{6}_{6} ( - 3 )^{6}$

Evaluate the coefficients $1 , 6 , 15 , 20 , 15 , 6 , 1$ and simplify each term

$( 2 x - 3 )^{6} = 64 x^{6} - 576 x^{5} + 2160 x^{4} - 4320 x^{3} + 4860 x^{2} - 2916 x + 729$

**[B1 B1 B1]**

> **[mark-scheme]**
> **B1**: Correct terms $64 x^{6}$ and $- 576 x^{5}$.
> 
> **B1**: Correct terms $2160 x^{4}$ and $- 4320 x^{3}$.
> 
> **B1**: Correct terms $4860 x^{2}$, $- 2916 x$ and $729$, fully simplified. Marked B3,2,1,0 — one mark is lost for each error, so take care with the signs from the powers of $- 3$.

### Q7
The term in $x^{5}$ is the $r = 5$ term, with $a = p$, $b = x$ and $n = 12$

`{}^{12}C_{5}\,p^{7}x^{5} = 792\,p^{7}x^{5}`

So the coefficient of $x^{5}$ is $792 p^{7}$

**[B1]**

Set this equal to the given coefficient and simplify

$792 p^{7} = 12  976  128$

$p^{7} = 16  384$

**[M1]**

Take the seventh root of both sides

$p = 4$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{5}$, namely $792 p^{7}$, with `{}^{12}C_5` evaluated to $792$ rather than left symbolic.
> 
> **M1**: You form the equation $792 p^{7} = 12  976  128$ using your coefficient and rearrange it to $p^{7} = 16  384$.
> 
> **A1**: Correct value $p = 4$.

### Q8
The term in $x^{2}$ is the $r = 2$ term, with $a = 2$, $b = - x$ and $n = 5$

`{}^{5}C_{2}\,(2)^{5 - 2}(-x)^{2}`

**[B1]**

Evaluate the binomial coefficient and the powers

$= 10 \times 8 \times x^{2} = 80 x^{2}$

So the coefficient of $x^{2}$ is

$80$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct unsimplified term `{}^{5}C_{2}\,(2)^{3}(-x)^{2}` (or equivalent), which may be seen or implied.
> 
> **B1**: Correct coefficient $80$. The sign is positive because $( - x )^{2}$ is positive.

### Q9
Use the binomial expansion up to the $x^{2}$ term, with $a = 4$, $b = - 3 x$ and $n = 9$

`(4 - 3x)^9 = {}^{9}C_{0}\,4^9 + {}^{9}C_{1}\,4^8(-3x) + {}^{9}C_{2}\,4^7(-3x)^2 + \cdots`

Evaluate each binomial coefficient and simplify

$= ( 1 ) ( 262144 ) + ( 9 ) ( 65536 ) ( - 3 x ) + ( 36 ) ( 16384 ) ( 9 x^{2} ) + \cdots$

$262144 - 1769472 x + 5308416 x^{2}$

**[B1 B1 B1]**

> **[mark-scheme]**
> **B1**: Correct constant term $262144$.
> 
> **B1**: Correct term in $x$, namely $- 1769472 x$.
> 
> **B1**: Correct term in $x^{2}$, namely $5308416 x^{2}$.
Multiply your expansion from part (a) by $( 3 - 2 x^{2} )$, keeping only terms up to $x^{2}$

$( 3 - 2 x^{2} ) ( 262144 - 1769472 x + 5308416 x^{2} )$

Multiply out, ignoring $x^{3}$ and higher powers (so $- 2 x^{2}$ only multiplies the constant $262144$)

$= 786432 - 5308416 x + 15925248 x^{2} - 524288 x^{2} + \cdots$

**[M1]**

Collect the terms in $x$ and $x^{2}$

**Final answer:** $( 3 - 2 x^{2} ) ( 4 - 3 x )^{9} \approx 786432 - 5308416 x + 15400960 x^{2}$** as required**

**[A1 A1]**

> **[mark-scheme]**
> **M1**: You multiply your part (a) expansion by $( 3 - 2 x^{2} )$, noting that $- 2 x^{2}$ contributes to the $x^{2}$ term only (via the constant $262144$).
> 
> **A1**: Correct term in $x$, namely $3 ( - 1769472 x ) = - 5308416 x$.
> 
> **A1**: Correct term in $x^{2}$, namely $3 ( 5308416 ) - 2 ( 262144 ) = 15400960$, reaching the printed result.

### Q10
The term in $x^{3}$ is the $r = 3$ term, with $a = 1$, $b = - 3 x$ and power $n$

$C pre^{n}_{3}   ( 1 )^{n - 3} ( - 3 x )^{3} = - 27 \times   C pre^{n}_{3}   x^{3}$

So the coefficient of $x^{3}$ is $- 27   \times C pre^{n}_{3}$

**[B1]**

Set this equal to $- 3240$ and divide by $- 27$

$- 27 \times   C pre^{n}_{3} = - 3240$

`{}^{n}C_{3} = 120`

**[M1]**

Write `{}^{n}C_{3}` using the formula for a binomial coefficient

`{}^{n}C_{r} = \dfrac{n!}{r!(n - r)!}`

Apply it with $r = 3$ and simplify

`{}^{n}C_{3} = \dfrac{n!}{3!(n - 3)!} = \dfrac{n(n - 1)(n - 2)}{6}`

Clear the fraction

$\frac{n(n-1)(n-2)}{6} = 120$

$n ( n - 1 ) ( n - 2 ) = 720$

**[M1]**

Look for three consecutive integers with product 720; since $720 = 8 \times 9 \times 10$

$n = 10$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{3}$, namely `-27\,{}^{n}C_{3}` (from the factor $( - 3 )^{3}$).
> 
> **M1**: You reduce the equation to `{}^{n}C_{3} = 120`.
> 
> **M1**: You reach $n ( n - 1 ) ( n - 2 ) = 720$ and attempt to solve it.
> 
> **A1**: Correct value $n = 10$.

### Q11
The term in $x^{3}$ is the $r = 3$ term, with first term $m$, second term $- \frac{x}{4}$ and $n = 5$

`{}^{5}C_{3}\,m^{2}\left(-\dfrac{x}{4}\right)^{3} = 10m^2\left(-\dfrac{x^3}{64}\right) = -\dfrac{10m^2}{64}x^3`

So the coefficient of $x^{3}$ is $- \frac{10m^{2}}{64}$

**[B1]**

Set this equal to $- 10$ and solve for $m^{2}$

$- \frac{10m^{2}}{64} = - 10$

$m^{2} = 64$

**[M1]**

Take the square root

**Final answer:** $m = 8$** or **$m = - 8$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{3}$, namely $- \frac{10m^{2}}{64}$ (or the simplified $- \frac{5m^{2}}{32}$).
> 
> **M1**: You set your coefficient equal to $- 10$ and rearrange to $m^{2} = 64$.
> 
> **A1**: Both values $m = 8$ and $m = - 8$.

### Q12
Find each coefficient using the binomial expansion, with $a = p$, $b = q x$ and $n = 9$

The term in $x^{3}$ is the $r = 3$ term

`{}^{9}C_{3}\,p^{6}(qx)^{3} = 84p^{6}q^{3}x^{3}`

**[B1]**

The term in $x^{5}$ is the $r = 5$ term

`{}^{9}C_{5}\,p^{4}(qx)^{5} = 126p^{4}q^{5}x^{5}`

**[B1]**

The coefficient of $x^{3}$ is double the coefficient of $x^{5}$, so form an equation

$84 p^{6} q^{3} = 2 ( 126 p^{4} q^{5} )$

**[M1]**

Divide both sides by $84 p^{4} q^{3}$ (valid since $p , q \neq 0$)

$p^{2} = 3 q^{2}$

**Final answer:** $p = \sqrt{3}  q$** or **$p = - \sqrt{3}  q$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{3}$, namely $84 p^{6} q^{3}$.
> 
> **B1**: Correct coefficient of $x^{5}$, namely $126 p^{4} q^{5}$.
> 
> **M1**: You form a correct equation from "the coefficient of $x^{3}$ is double that of $x^{5}$", giving $84 p^{6} q^{3} = 2 ( 126 p^{4} q^{5} )$.
> 
> **A1**: Correct result $p = \pm \sqrt{3}  q$ (from $p^{2} = 3 q^{2}$).

### Q13
Find the coefficient of $x^{5}$ in $( a + b x )^{8}$ (the $r = 5$ term) and set it equal to $- 870  912$

`{}^{8}C_{5}\,a^{3}(bx)^{5} = 56a^{3}b^{5}x^{5}`

$56 a^{3} b^{5} = - 870912$

$a^{3} b^{5} = - 15552$

**[B1]**

Find the coefficient of $x^{3}$ in $( a + b x )^{12}$ (the $r = 3$ term) and set it equal to $- 1  557  135  360$

`{}^{12}C_{3}\,a^{9}(bx)^{3} = 220a^{9}b^{3}x^{3}`

$220 a^{9} b^{3} = - 1557135360$

$a^{9} b^{3} = - 7077888$

**[B1]**

From the second equation, make $b$ the subject

$b^{3} = \frac{-7077888}{a^{9}}$

Cube root

$b = \frac{-192}{a^{3}}$

**[M1]**

Substitute into the first equation and solve for $a$

`a^3\left(\dfrac{-192}{a^3}\right)^{5} = -15552`

$a^{12} = 16777216$

$a = 4   \text{or}   a = - 4$

**[M1]**

Find the matching $b$ from $b = \frac{-192}{a^{3}}$

**Final answer:** $a = 4 ,  b = - 3$** or **$a = - 4 ,  b = 3$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{5}$ in the first expansion, $56 a^{3} b^{5}$, giving $a^{3} b^{5} = - 15552$.
> 
> **B1**: Correct coefficient of $x^{3}$ in the second expansion, $220 a^{9} b^{3}$, giving $a^{9} b^{3} = - 7077888$.
> 
> **M1**: You make one unknown the subject, for example $b = \frac{-192}{a^{3}}$.
> 
> **M1**: You substitute and solve for $a$, obtaining $a^{12} = 16777216$, so $a = \pm 4$.
> 
> **A1**: Both pairs $a = 4 , b = - 3$ and $a = - 4 , b = 3$, with $a$ and $b$ having opposite signs.

### Q14
The term in $x^{4}$ is the $r = 4$ term, with $a = 4$, $b = - 3 x$ and $n = 7$

`{}^{7}C_{4}\,4^{3}(-3x)^{4}`

**[B1]**

Evaluate the binomial coefficient and the powers

$= 35 \times 64 \times 81  x^{4} = 181440 x^{4}$

So the coefficient of $x^{4}$ is

$181440$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct unsimplified term `{}^{7}C_{4}\,4^{3}(-3x)^{4}` (or equivalent), which may be seen or implied.
> 
> **B1**: Correct coefficient $181440$.

### Q15
Find each coefficient using the binomial expansion, with first term $3 a$, second term $\frac{x}{2}$ and $n = 6$

The term in $x^{3}$ is the $r = 3$ term

`{}^{6}C_{3}\,(3a)^{3}\left(\dfrac{x}{2}\right)^{3} = \dfrac{135a^3}{2}x^3`

**[B1]**

The term in $x^{5}$ is the $r = 5$ term

`{}^{6}C_{5}\,(3a)\left(\dfrac{x}{2}\right)^{5} = \dfrac{9a}{16}x^5`

**[B1]**

The two coefficients are equal, so form an equation in $a$

$\frac{135a^{3}}{2} = \frac{9a}{16}$

**[M1]**

Divide both sides by $a$ (valid since $a \neq 0$) and solve for $a^{2}$

$a^{2} = \frac{1}{120}$

Take the square root and rationalise into the form $\frac{\sqrt{m}}{n}$

**Final answer:** $a = \frac{\sqrt{30}}{60}$** or **$a = - \frac{\sqrt{30}}{60}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{3}$, namely $\frac{135a^{3}}{2}$.
> 
> **B1**: Correct coefficient of $x^{5}$, namely $\frac{9a}{16}$.
> 
> **M1**: You set the two coefficients equal and simplify to $a^{2} = \frac{1}{120}$.
> 
> **A1**: Correct values $a = \pm \frac{\sqrt{30}}{60}$, so $m = 30$ and $n = 60$.

### Q16
Find the first three terms of $( 3 - 5 x )^{4}$, with $a = 3$, $b = - 5 x$ and $n = 4$

`(3 - 5x)^4 = {}^{4}C_{0}\,3^4 + {}^{4}C_{1}\,3^3(-5x) + {}^{4}C_{2}\,3^2(-5x)^2 + \cdots`

$= 81 - 540 x + 1350 x^{2} + \cdots$

**[B1 B1 B1]**

To approximate $( 2 . 6 )^{4}$, set $3 - 5 x = 2 . 6$, giving $x = 0 . 08$, and substitute

$( 2 . 6 )^{4} \approx 81 - 540 ( 0 . 08 ) + 1350 ( 0 . 08 )^{2}$

**[M1]**

Work out each term and add

$= 81 - 43 . 2 + 8 . 64$

$( 2 . 6 )^{4} \approx 46 . 44$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct constant term $81$.
> 
> **B1**: Correct term in $x$, namely $- 540 x$.
> 
> **B1**: Correct term in $x^{2}$, namely $1350 x^{2}$.
> 
> **M1**: You set $3 - 5 x = 2 . 6$ to get $x = 0 . 08$ and substitute it into your first three terms.
> 
> **A1**: Correct estimate $46 . 44$.
The exact value is $( 2 . 6 )^{4} = 45 . 6976$; find the percentage error of the estimate from part (a)

$\frac{46.44-45.6976}{45.6976} \times 100$

**[M1]**

Evaluate

**Final answer:** `1.62\%`** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: You use the percentage error formula: the difference between your estimate and the exact value $45 . 6976$, divided by $45 . 6976$, all times $100$.
> 
> **A1**: Correct percentage error, answers which round to `1.62\%` (3 significant figures).

### Q17
Expand using the binomial expansion, with $a = 3$, $b = - 2 x$ and $n = 5$

`(3 - 2x)^5 = {}^{5}C_{0}\,3^5 + {}^{5}C_{1}\,3^4(-2x) + {}^{5}C_{2}\,3^3(-2x)^2 + {}^{5}C_{3}\,3^2(-2x)^3 + {}^{5}C_{4}\,3(-2x)^4 + {}^{5}C_{5}\,(-2x)^5`

Evaluate the coefficients $1 , 5 , 10 , 10 , 5 , 1$ and simplify each term

$( 3 - 2 x )^{5} = 243 - 810 x + 1080 x^{2} - 720 x^{3} + 240 x^{4} - 32 x^{5}$

**[B1 B1]**

> **[mark-scheme]**
> **B1**: At least four terms of the fully simplified expansion correct.
> 
> **B1**: Completely correct, simplified expansion. Marked B2,1,0 — one mark is lost for each error, so take care with the signs from the powers of $- 2 x$.

### Q18
Recall the formula for a binomial coefficient

`{}^{n}C_{r} = \dfrac{n!}{r!(n - r)!}`

Apply it with $r = 3$ and simplify

`{}^{n}C_{3} = \dfrac{n!}{3!(n - 3)!} = \dfrac{n(n - 1)(n - 2)}{6}`

Set this equal to 35

$\frac{n(n-1)(n-2)}{6} = 35$

**[B1]**

Multiply both sides by 6 to clear the fraction

$n ( n - 1 ) ( n - 2 ) = 210$

**[M1]**

Look for three consecutive integers with product 210; since $210 = 5 \times 6 \times 7$

$n = 7$

**[A1]**

> **[mark-scheme]**
> **B1**: You write `{}^{n}C_{3} = \dfrac{n(n - 1)(n - 2)}{6}` and set it equal to 35.
> 
> **M1**: You reach the equation $n ( n - 1 ) ( n - 2 ) = 210$ and attempt to solve it.
> 
> **A1**: Correct value $n = 7$.

### Q19
The term in $x^{4}$ is the $r = 4$ term, with $a = 4$, $b = - p x$ and $n = 6$

`{}^{6}C_{4}\,4^{2}(-px)^{4} = 240p^{4}x^{4}`

So the coefficient of $x^{4}$ is $240 p^{4}$

**[B1]**

Set this equal to $19  440$ and solve for $p^{4}$

$240 p^{4} = 19440$

$p^{4} = 81$

**[M1]**

Take the fourth root; since $p$ is a positive integer, take the positive value

$p = 3$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{4}$, namely $240 p^{4}$ (positive, since $( - p x )^{4}$ is positive).
> 
> **M1**: You set your coefficient equal to $19  440$ and rearrange to $p^{4} = 81$.
> 
> **A1**: Correct value $p = 3$.

### Q20
Use the binomial expansion up to the $x^{2}$ term, with $a = 2$, $b = - 3 x$ and $n = 7$

`(2 - 3x)^7 = {}^{7}C_{0}\,2^7 + {}^{7}C_{1}\,2^6(-3x) + {}^{7}C_{2}\,2^5(-3x)^2 + \cdots`

Evaluate each binomial coefficient and simplify

$= ( 1 ) ( 128 ) + ( 7 ) ( 64 ) ( - 3 x ) + ( 21 ) ( 32 ) ( 9 x^{2} ) + \cdots$

$128 - 1344 x + 6048 x^{2}$

**[B1 B1 B1]**

> **[mark-scheme]**
> **B1**: Correct constant term $128$.
> 
> **B1**: Correct term in $x$, namely $- 1344 x$.
> 
> **B1**: Correct term in $x^{2}$, namely $6048 x^{2}$.
Multiply your expansion from part (a) by $( 1 - 2 x )$, keeping only terms up to $x^{2}$

$( 1 - 2 x ) ( 128 - 1344 x + 6048 x^{2} )$

Multiply out, ignoring $x^{3}$ and higher powers

$= 128 - 1344 x + 6048 x^{2} - 256 x + 2688 x^{2} + \cdots$

**[M1]**

Collect the terms in $x$ and $x^{2}$

**Final answer:** $( 1 - 2 x ) ( 2 - 3 x )^{7} \approx 128 - 1600 x + 8736 x^{2}$** as required**

**[A1 A1]**

> **[mark-scheme]**
> **M1**: You multiply your part (a) expansion by $( 1 - 2 x )$, forming the products that contribute to the terms up to $x^{2}$.
> 
> **A1**: Correct term in $x$, namely $- 1344 x - 256 x = - 1600 x$.
> 
> **A1**: Correct term in $x^{2}$, namely $6048 x^{2} + 2688 x^{2} = 8736 x^{2}$, reaching the printed result.

### Q21
The term in $x^{4}$ is the $r = 4$ term, with $a = 3$, $b = 2 x$ and $n = 9$

`{}^{9}C_{4}\,3^{5}(2x)^{4}`

**[B1]**

Evaluate the binomial coefficient and the powers

$= 126 \times 243 \times 16  x^{4} = 489888 x^{4}$

So the coefficient of $x^{4}$ is

$489888$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct unsimplified term `{}^{9}C_{4}\,3^{5}(2x)^{4}` (or equivalent), which may be seen or implied.
> 
> **B1**: Correct coefficient $489888$.

### Q22
Find each coefficient using the binomial expansion, with first term $3 a$, second term $- 2 x$ and $n = 6$

The term in $x^{3}$ is the $r = 3$ term

`{}^{6}C_{3}\,(3a)^{3}(-2x)^{3} = -4320a^{3}x^{3}`

**[B1]**

The term in $x^{4}$ is the $r = 4$ term

`{}^{6}C_{4}\,(3a)^{2}(-2x)^{4} = 2160a^{2}x^{4}`

**[B1]**

The two coefficients are equal, so form an equation in $a$

$- 4320 a^{3} = 2160 a^{2}$

**[M1]**

Divide both sides by $2160 a^{2}$ (valid since $a \neq 0$) and solve

$- 2 a = 1$

$a = - \frac{1}{2}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{3}$, namely $- 4320 a^{3}$.
> 
> **B1**: Correct coefficient of $x^{4}$, namely $2160 a^{2}$.
> 
> **M1**: You set the two coefficients equal, giving $- 4320 a^{3} = 2160 a^{2}$.
> 
> **A1**: Correct value $a = - \frac{1}{2}$. The solution $a = 0$ is rejected, since it would make the expansion trivial.

### Q23
Find the coefficient of $x^{3}$ in $( a + b x )^{4}$ (the $r = 3$ term) and set it equal to 216

`{}^{4}C_{3}\,a(bx)^{3} = 4ab^{3}x^{3}`

$4 a b^{3} = 216$

$a b^{3} = 54$

**[B1]**

Find the coefficient of $x^{4}$ in $( a + b x )^{6}$ (the $r = 4$ term) and set it equal to 4860

`{}^{6}C_{4}\,a^{2}(bx)^{4} = 15a^{2}b^{4}x^{4}`

$15 a^{2} b^{4} = 4860$

$a^{2} b^{4} = 324$

**[B1]**

Eliminate $a$ by writing $a = \frac{54}{b^{3}}$ from the first equation and substituting into the second

`\left(\dfrac{54}{b^3}\right)^{2} b^4 = 324`

$\frac{2916}{b^{2}} = 324$

**[M1]**

Solve for $b$

$b^{2} = 9$

$b = 3   \text{or}   b = - 3$

**[M1]**

Find the matching $a$ from $a = \frac{54}{b^{3}}$; the sign of $a$ matches the sign of $b$

**Final answer:** $a = 2 ,  b = 3$** or **$a = - 2 ,  b = - 3$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{3}$ in the first expansion, $4 a b^{3}$, giving $a b^{3} = 54$.
> 
> **B1**: Correct coefficient of $x^{4}$ in the second expansion, $15 a^{2} b^{4}$, giving $a^{2} b^{4} = 324$.
> 
> **M1**: You eliminate one unknown (for example $a = \frac{54}{b^{3}}$) to obtain an equation in the other.
> 
> **M1**: You solve for $b$, obtaining $b^{2} = 9$.
> 
> **A1**: Both pairs $a = 2 , b = 3$ and $a = - 2 , b = - 3$, with $a$ and $b$ having the same sign.

### Q24
In $( 1 + x )^{n}$ the coefficient of $x^{3}$ is the binomial coefficient `{}^{n}C_{3}`; recall the formula for a binomial coefficient

`{}^{n}C_{r} = \dfrac{n!}{r!(n - r)!}`

Apply it with $r = 3$ and simplify

`{}^{n}C_{3} = \dfrac{n!}{3!(n - 3)!} = \dfrac{n(n - 1)(n - 2)}{6}`

Set this coefficient equal to 84 (given in the question)

$\frac{n(n-1)(n-2)}{6} = 84$

**[B1]**

Multiply both sides by 6 to clear the fraction

$n ( n - 1 ) ( n - 2 ) = 504$

**[M1]**

Look for three consecutive integers with product 504; since $504 = 7 \times 8 \times 9$

$n = 9$

**[A1]**

> **[mark-scheme]**
> **B1**: You identify the coefficient of $x^{3}$ as `{}^{n}C_{3} = \dfrac{n(n - 1)(n - 2)}{6}` and set it equal to 84.
> 
> **M1**: You reach the equation $n ( n - 1 ) ( n - 2 ) = 504$ and attempt to solve it (for example, by factorising or trial of consecutive integers).
> 
> **A1**: Correct value $n = 9$.

### Q25
Find each coefficient using the binomial expansion, with $a = p$, $b = q x$ and $n = 8$

The term in $x^{2}$ is the $r = 2$ term

`{}^{8}C_{2}\,p^{6}(qx)^{2} = 28p^{6}q^{2}x^{2}`

**[B1]**

The term in $x^{6}$ is the $r = 6$ term

`{}^{8}C_{6}\,p^{2}(qx)^{6} = 28p^{2}q^{6}x^{6}`

**[B1]**

The coefficients are equal (note `{}^{8}C_{2} = {}^{8}C_{6} = 28`), so form an equation

$28 p^{6} q^{2} = 28 p^{2} q^{6}$

**[M1]**

Divide both sides by $28 p^{2} q^{2}$ (valid since $p , q \neq 0$)

$p^{4} = q^{4}$

**Final answer:** $p = q$** or **$p = - q$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{2}$, namely $28 p^{6} q^{2}$.
> 
> **B1**: Correct coefficient of $x^{6}$, namely $28 p^{2} q^{6}$.
> 
> **M1**: You set the two coefficients equal, giving $28 p^{6} q^{2} = 28 p^{2} q^{6}$.
> 
> **A1**: Correct result $p = q$ or $p = - q$ (from $p^{4} = q^{4}$).

### Q26
Use the binomial expansion up to the $x^{2}$ term, with $a = 5$, $b = - 2 x$ and $n = 4$

`(5 - 2x)^4 = {}^{4}C_{0}\,5^4 + {}^{4}C_{1}\,5^3(-2x) + {}^{4}C_{2}\,5^2(-2x)^2 + \cdots`

Evaluate each binomial coefficient and simplify

$= ( 1 ) ( 625 ) + ( 4 ) ( 125 ) ( - 2 x ) + ( 6 ) ( 25 ) ( 4 x^{2} ) + \cdots$

$625 - 1000 x + 600 x^{2}$

**[B1 B1 B1]**

> **[mark-scheme]**
> **B1**: Correct constant term $625$.
> 
> **B1**: Correct term in $x$, namely $- 1000 x$.
> 
> **B1**: Correct term in $x^{2}$, namely $600 x^{2}$.
Compare $( 4 . 5 )^{4}$ with $( 5 - 2 x )^{4}$, so you need $5 - 2 x = 4 . 5$, giving $2 x = 0 . 5$ and $x = 0 . 25$

$( 4 . 5 )^{4} \approx 625 - 1000 ( 0 . 25 ) + 600 ( 0 . 25 )^{2}$

**[M1]**

Work out each term and add

$= 625 - 250 + 37 . 5$

$( 4 . 5 )^{4} \approx 412 . 5$

**[A1]**

> **[mark-scheme]**
> **M1**: You set $5 - 2 x = 4 . 5$ to get $x = 0 . 25$ and substitute it into your answer from part (a).
> 
> **A1**: Correct estimate $412 . 5$. (The true value is $410 . 0625$; because $x = 0 . 25$ is not very small, the first three terms give only a rough approximation.)

### Q27
Expand using the binomial expansion, with $a = 2$, $b = - \frac{x}{3}$ and $n = 4$

`\left(2 - \dfrac{x}{3}\right)^4 = 2^4 + {}^{4}C_{1}\,2^3\left(-\dfrac{x}{3}\right) + {}^{4}C_{2}\,2^2\left(-\dfrac{x}{3}\right)^2 + {}^{4}C_{3}\,2\left(-\dfrac{x}{3}\right)^3 + \left(-\dfrac{x}{3}\right)^4`

Evaluate the coefficients and simplify each term

`= 16 + 4(8)\left(-\dfrac{x}{3}\right) + 6(4)\left(\dfrac{x^2}{9}\right) + 4(2)\left(-\dfrac{x^3}{27}\right) + \dfrac{x^4}{81}`

`\left(2 - \dfrac{1}{3}x\right)^4 = 16 - \dfrac{32x}{3} + \dfrac{8x^2}{3} - \dfrac{8x^3}{27} + \dfrac{x^4}{81}`

**[B1 B1]**

> **[mark-scheme]**
> **B1**: At least three terms of the fully simplified expansion correct.
> 
> **B1**: Completely correct, simplified expansion. Marked B2,1,0 — one mark is lost for each error, so take care with the powers of $\frac{1}{3}$ in the denominators.

### Q28
Expand using the binomial expansion, with $a = 4$, $b = - x$ and $n = 4$

`(4 - x)^4 = {}^{4}C_{0}\,4^4 + {}^{4}C_{1}\,4^3(-x) + {}^{4}C_{2}\,4^2(-x)^2 + {}^{4}C_{3}\,4(-x)^3 + {}^{4}C_{4}\,(-x)^4`

Evaluate the coefficients $1 , 4 , 6 , 4 , 1$ and simplify each term

$( 4 - x )^{4} = 256 - 256 x + 96 x^{2} - 16 x^{3} + x^{4}$

**[B1 B1]**

> **[mark-scheme]**
> **B1**: At least three terms of the fully simplified expansion correct.
> 
> **B1**: Completely correct, simplified expansion $256 - 256 x + 96 x^{2} - 16 x^{3} + x^{4}$. Marked B2,1,0 — one mark is lost for each error.

### Q29
Find each coefficient using the binomial expansion, with first term $a$, second term $b x$ and $n = 4$

The term in $x^{2}$ is the $r = 2$ term

`{}^{4}C_{2}\,a^{2}(bx)^{2} = 6a^{2}b^{2}x^{2}`

**[B1]**

The term in $x^{3}$ is the $r = 3$ term

`{}^{4}C_{3}\,a(bx)^{3} = 4ab^{3}x^{3}`

**[B1]**

The coefficients are equal, so equate them and divide both sides by $2 a b^{2}$ (valid since $a , b \neq 0$)

$6 a^{2} b^{2} = 4 a b^{3}$

$6 a = 4 b$

**Final answer:** $\frac{a}{b} = \frac{2}{3}$** as required**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{2}$, namely $6 a^{2} b^{2}$.
> 
> **B1**: Correct coefficient of $x^{3}$, namely $4 a b^{3}$.
> 
> **B1**: You equate the two coefficients and simplify correctly to reach the printed result $\frac{a}{b} = \frac{2}{3}$.
From part (a), $\frac{a}{b} = \frac{2}{3}$, so

* *$3 a = 2 b$

For $a$ to be an integer, $b$ must be a multiple of $3$

The only multiple of $3$ with $10 < b < 15$ is $b = 12$, and then $3 a = 2 ( 12 )$

**[M1]**

Solve for $a$

$a = 8 ,  b = 12$

**[A1]**

> **[mark-scheme]**
> **M1**: You use $\frac{a}{b} = \frac{2}{3}$ with $10 < b < 15$ to identify that $b$ must be a multiple of $3$, so $b = 12$.
> 
> **A1**: Correct values $a = 8$ and $b = 12$.

### Q30
Find each coefficient using the binomial expansion, with $a = 3$, $b = p x$ and $n = 6$

The term in $x^{2}$ is the $r = 2$ term

`{}^{6}C_{2}\,3^{4}(px)^{2} = 1215p^{2}x^{2}`

**[B1]**

The term in $x^{4}$ is the $r = 4$ term

`{}^{6}C_{4}\,3^{2}(px)^{4} = 135p^{4}x^{4}`

**[B1]**

The coefficient of $x^{4}$ is four times the coefficient of $x^{2}$, so form an equation in $p$

$135 p^{4} = 4 ( 1215 p^{2} )$

**[M1]**

Divide both sides by $135 p^{2}$ (valid since $p \neq 0$) and solve

$p^{2} = 36$

**Final answer:** $p = 6$** or **$p = - 6$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{2}$, namely $1215 p^{2}$.
> 
> **B1**: Correct coefficient of $x^{4}$, namely $135 p^{4}$.
> 
> **M1**: You form a correct equation from "the coefficient of $x^{4}$ is four times the coefficient of $x^{2}$", with the $x$ terms removed, for example $135 p^{4} = 4 ( 1215 p^{2} )$.
> 
> **A1**: Both values $p = 6$ and $p = - 6$.

### Q31
Expand using the binomial expansion, with $a = 2$, $b = x$ and $n = 4$

`(2 + x)^4 = {}^{4}C_{0}\,2^4 + {}^{4}C_{1}\,2^3 x + {}^{4}C_{2}\,2^2 x^2 + {}^{4}C_{3}\,2x^3 + {}^{4}C_{4}\,x^4`

Evaluate the coefficients $1 , 4 , 6 , 4 , 1$ and simplify

$( 2 + x )^{4} = 16 + 32 x + 24 x^{2} + 8 x^{3} + x^{4}$

**[B1 B1]**

> **[mark-scheme]**
> **B1**: At least three terms of the fully simplified expansion correct.
> 
> **B1**: Completely correct, simplified expansion $16 + 32 x + 24 x^{2} + 8 x^{3} + x^{4}$. Marked B2,1,0 — one mark is lost for each error.

### Q32
Find each coefficient using the binomial expansion, with $a = p$, $b = q x$ and $n = 5$

The term in $x^{2}$ is the $r = 2$ term

`{}^{5}C_{2}\,p^{3}(qx)^{2} = 10p^{3}q^{2}x^{2}`

**[B1]**

The term in $x^{3}$ is the $r = 3$ term

`{}^{5}C_{3}\,p^{2}(qx)^{3} = 10p^{2}q^{3}x^{3}`

**[B1]**

The coefficients are equal, so form an equation

$10 p^{3} q^{2} = 10 p^{2} q^{3}$

**[M1]**

Divide both sides by $10 p^{2} q^{2}$ (valid since $p , q \neq 0$)

$p = q$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{2}$, namely $10 p^{3} q^{2}$.
> 
> **B1**: Correct coefficient of $x^{3}$, namely $10 p^{2} q^{3}$.
> 
> **M1**: You set the two coefficients equal, giving $10 p^{3} q^{2} = 10 p^{2} q^{3}$.
> 
> **A1**: Correct result $p = q$.

### Q33
Find each coefficient using the binomial expansion, with first term $a$, second term $- 2 x$ and $n = 5$

The term in $x^{2}$ is the $r = 2$ term

`{}^{5}C_{2}\,a^{3}(-2x)^{2} = 40a^{3}x^{2}`

**[B1]**

The term in $x^{3}$ is the $r = 3$ term

`{}^{5}C_{3}\,a^{2}(-2x)^{3} = -80a^{2}x^{3}`

**[B1]**

The two coefficients are equal, so form an equation in $a$

$40 a^{3} = - 80 a^{2}$

**[M1]**

Divide both sides by $40 a^{2}$ (valid since $a \neq 0$)

$a = - 2$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{2}$, namely $40 a^{3}$.
> 
> **B1**: Correct coefficient of $x^{3}$, namely $- 80 a^{2}$ (note the negative sign from $( - 2 x )^{3}$).
> 
> **M1**: You set the two coefficients equal, giving $40 a^{3} = - 80 a^{2}$.
> 
> **A1**: Correct value $a = - 2$. The solution $a = 0$ is rejected, since it would make the expansion trivial.

### Q34
The term in $x^{3}$ is the $r = 3$ term, with $a = 2$, $b = - x$ and $n = 8$

`{}^{8}C_{3}\,(2)^{8 - 3}(-x)^{3}`

**[B1]**

Evaluate the binomial coefficient and the powers

$= 56 \times 32 \times ( - x^{3} ) = - 1792 x^{3}$

So the coefficient of $x^{3}$ is

$- 1792$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct unsimplified term `{}^{8}C_{3}\,(2)^{5}(-x)^{3}` (or equivalent), which may be seen or implied.
> 
> **B1**: Correct coefficient $- 1792$. The coefficient is negative because $( - x )^{3}$ is negative.

### Q35
Use the binomial expansion up to the $x^{2}$ term, with $a = 3$, $b = x$ and $n = 4$

`(3 + x)^4 = {}^{4}C_{0}\,3^4 + {}^{4}C_{1}\,3^3 x + {}^{4}C_{2}\,3^2 x^2 + \cdots`

Evaluate each binomial coefficient and simplify

$= ( 1 ) ( 81 ) + ( 4 ) ( 27 ) x + ( 6 ) ( 9 ) x^{2} + \cdots$

$81 + 108 x + 54 x^{2}$

**[B1 B1 B1]**

> **[mark-scheme]**
> **B1**: Correct constant term $81$.
> 
> **B1**: Correct term in $x$, namely $108 x$.
> 
> **B1**: Correct term in $x^{2}$, namely $54 x^{2}$.
Compare $( 3 . 1 )^{4}$ with $( 3 + x )^{4}$, so you need $3 + x = 3 . 1$, giving $x = 0 . 1$

$( 3 . 1 )^{4} \approx 81 + 108 ( 0 . 1 ) + 54 ( 0 . 1 )^{2}$

**[M1]**

Work out each term and add

$= 81 + 10 . 8 + 0 . 54$

$( 3 . 1 )^{4} \approx 92 . 34$

**[A1]**

> **[mark-scheme]**
> **M1**: You set $3 + x = 3 . 1$ to get $x = 0 . 1$ and substitute it into your answer from part (a).
> 
> **A1**: Correct estimate $92 . 34$. Answers which round to $92 . 3$ (3 significant figures) are also accepted.

### Q36
Use the binomial expansion, taking the terms up to $x^{2}$, with $a = 3$, $b = 2 x$ and $n = 8$

`(3 + 2x)^8 = {}^{8}C_{0}\,3^8 + {}^{8}C_{1}\,3^7(2x) + {}^{8}C_{2}\,3^6(2x)^2 + \cdots`

Evaluate each binomial coefficient and simplify

$= ( 1 ) ( 6561 ) + ( 8 ) ( 2187 ) ( 2 x ) + ( 28 ) ( 729 ) ( 4 x^{2} ) + \cdots$

$6561 + 34992 x + 81648 x^{2}$

**[B1 B1 B1]**

> **[mark-scheme]**
> **B1**: Correct constant term $6561$.
> 
> **B1**: Correct term in $x$, namely $34992 x$.
> 
> **B1**: Correct term in $x^{2}$, namely $81648 x^{2}$.
Multiply your expansion from part (a) by $( 1 + x )$, keeping only terms up to $x^{2}$

$( 1 + x ) ( 6561 + 34992 x + 81648 x^{2} )$

Multiply out, ignoring $x^{3}$ and higher powers

$= 6561 + 34992 x + 81648 x^{2} + 6561 x + 34992 x^{2} + \cdots$

**[M1]**

Collect the terms in $x$ and $x^{2}$

**Final answer:** $( 1 + x ) ( 3 + 2 x )^{8} \approx 6561 + 41553 x + 116640 x^{2}$** as required**

**[A1 A1]**

> **[mark-scheme]**
> **M1**: You multiply your part (a) expansion by $( 1 + x )$, forming the products that contribute to the terms up to $x^{2}$.
> 
> **A1**: Correct term in $x$, namely $34992 x + 6561 x = 41553 x$.
> 
> **A1**: Correct term in $x^{2}$, namely $81648 x^{2} + 34992 x^{2} = 116640 x^{2}$, reaching the printed result.

### Q37
The coefficient of $x^{2}$ comes from the $r = 2$ term, with first term $a$, second term $- x$ and $n = 4$

`{}^{4}C_{2}\,a^{2}(-x)^{2} = 6a^{2}x^{2}`

So the coefficient of $x^{2}$ is $6 a^{2}$

**[B1]**

Set this equal to $96$ and solve for $a^{2}$

$6 a^{2} = 96$

$a^{2} = 16$

**[M1]**

Take the square root and choose the positive value since $a > 0$

$a = 4$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct coefficient of $x^{2}$, namely $6 a^{2}$.
> 
> **M1**: You set your coefficient equal to $96$ and rearrange to $a^{2} = 16$.
> 
> **A1**: Correct value $a = 4$. The negative root $a = - 4$ is rejected because $a > 0$.

### Q38
Use the binomial expansion up to the $x^{2}$ term, with $a = 9$, $b = - 2 x$ and $n = 5$

`(9 - 2x)^5 = {}^{5}C_{0}\,9^5 + {}^{5}C_{1}\,9^4(-2x) + {}^{5}C_{2}\,9^3(-2x)^2 + \cdots`

Evaluate each binomial coefficient and simplify

$= ( 1 ) ( 59049 ) + ( 5 ) ( 6561 ) ( - 2 x ) + ( 10 ) ( 729 ) ( 4 x^{2} ) + \cdots$

$59049 - 65610 x + 29160 x^{2}$

**[B1 B1 B1]**

> **[mark-scheme]**
> **B1**: Correct constant term $59049$.
> 
> **B1**: Correct term in $x$, namely $- 65610 x$.
> 
> **B1**: Correct term in $x^{2}$, namely $29160 x^{2}$.
Compare $( 8 . 9 )^{5}$ with $( 9 - 2 x )^{5}$, so you need $9 - 2 x = 8 . 9$, giving $2 x = 0 . 1$ and $x = 0 . 05$

$( 8 . 9 )^{5} \approx 59049 - 65610 ( 0 . 05 ) + 29160 ( 0 . 05 )^{2}$

**[M1]**

Work out each term and add

$= 59049 - 3280 . 5 + 72 . 9$

$( 8 . 9 )^{5} \approx 55841 . 4$

**[A1]**

> **[mark-scheme]**
> **M1**: You set $9 - 2 x = 8 . 9$ to get $x = 0 . 05$ and substitute it into your answer from part (a).
> 
> **A1**: Correct estimate $55841 . 4$. Answers which round to $55800$ (3 significant figures) are also accepted.
