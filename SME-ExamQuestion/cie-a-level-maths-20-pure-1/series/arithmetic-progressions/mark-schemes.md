# Mark Schemes — Arithmetic Progressions
**Series** · Cambridge (CIE) A-LEVEL maths (9709)


## Exam Questions (33 questions)


### Q1
Write each range-sum as a difference of sums, using the given $S_{6} = - 13 d$

$S_{12} - S_{6} = 6 ( 2 a + 11 d ) - ( - 13 d ) = 12 a + 79 d = - 69$

**[M1 A1]**

$S_{16} - S_{6} = 8 ( 2 a + 15 d ) - ( - 13 d ) = 16 a + 133 d = - 175$

**[A1]**

Solve the two equations simultaneously — from the first, $a = \frac{-69-79d}{12}$; substitute into the second

`16\left(\dfrac{-69 - 79d}{12}\right) + 133d = -175 \implies -92 + \dfrac{83}{3}d = -175`

**[M1]**

Solve for $d$, then back-substitute for $a$

$\frac{83}{3} d = - 83 \Rightarrow d = - 3$

$a = 14 ,  d = - 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Express the range-sums as differences of sums and use $S_{6} = - 13 d$ (e.g. sum of the seventh to twelfth terms $= S_{12} - S_{6}$).
> 
> **A1**: Correct first equation $12 a + 79 d = - 69$.
> 
> **A1**: Correct second equation $16 a + 133 d = - 175$.
> 
> **M1**: Solve your two equations simultaneously by a valid method.
> 
> **A1**: Correct values $a = 14$ and $d = - 3$.

### Q2
Since the $k$th term is $0$, use $u_{k} = a + ( k - 1 ) d = 0$ to express $a$

$a = - ( k - 1 ) d$

**[M1]**

The sum of the first $n$ terms is $0$ and $n \neq 0$, so the bracket in $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$ must be zero

$2 a + ( n - 1 ) d = 0 \Rightarrow a = - \frac{(n-1)d}{2}$

**[M1]**

Equate the two expressions for $a$; the common difference $d \neq 0$ cancels, leaving an equation for $n$

$- ( k - 1 ) d = - \frac{(n-1)d}{2} \Rightarrow 2 ( k - 1 ) = n - 1$

$n = 2 k - 1$

**[A1]**

> **[mark-scheme]**
> **M1**: Use $u_{k} = 0$ to obtain $a = - ( k - 1 ) d$.
> 
> **M1**: Use $S_{n} = 0$ with $n \neq 0$ to obtain $2 a + ( n - 1 ) d = 0$.
> 
> **A1**: Equate and solve to reach $n = 2 k - 1$. Alternatively, argue by symmetry: since the $k$th term is $0$, the terms pair off symmetrically about it (each pair summing to $0$), so there are $k - 1$ terms on each side, giving $n = 2 ( k - 1 ) + 1 = 2 k - 1$.

### Q3
Read the first term and common difference from $u_{k} = 89 - 5 k$: $a = 84$ and $d = - 5$

**[B1]**

Substitute into $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$ and set it equal to $- 35$

`\dfrac{n}{2}\left(2(84) + (n-1)(-5)\right) = -35`

**[M1]**

Clear the fraction and simplify to a three-term quadratic in $n$

$168 n - 5 n^{2} + 5 n = - 70 \Rightarrow 5 n^{2} - 173 n - 70 = 0$

**[A1]**

Factorise; $n$ must be a positive integer, so reject $n = - \frac{2}{5}$

$( 5 n + 2 ) ( n - 35 ) = 0$

$n = 35$

**[A1]**

> **[mark-scheme]**
> **B1**: State $a = 84$ and $d = - 5$ from $u_{k} = 89 - 5 k$ (seen or implied).
> 
> **M1**: Substitute your $a$ and $d$ into a correct sum formula and set it equal to $- 35$.
> 
> **A1**: Correct three-term quadratic $5 n^{2} - 173 n - 70 = 0$.
> 
> **A1**: Correct value $n = 35$. You must reject the negative root $n = - \frac{2}{5}$ (factorising or the formula is fine).

### Q4
Write each sum using $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$ to form two equations

$S_{20} = 10 ( 2 a + 19 d ) = 290 \Rightarrow 2 a + 19 d = 29$

$S_{24} = 12 ( 2 a + 23 d ) = - 180 \Rightarrow 2 a + 23 d = - 15$

**[B1]**

Subtract to eliminate $a$ and find $d$

$4 d = - 44 \Rightarrow d = - 11$

**[M1]**

Back-substitute into $2 a + 19 d = 29$ to find $a$

$2 a + 19 ( - 11 ) = 29 \Rightarrow a = 119$

**[A1]**

Since $d < 0$ the terms decrease, so the sum is greatest at the last non-negative term; solve $u_{n} \geq 0$

$u_{n} = 130 - 11 n \geq 0 \Rightarrow n \leq \frac{130}{11} = 11 . 8 \dots$

**[M1]**

The last positive term is the $11$th, so $S_{n}$ is greatest at $n = 11$; evaluate $S_{11}$

`S_{11} = \dfrac{11}{2}\left(2(119) + 10(-11)\right) = \dfrac{11}{2}(128)`

**[M1]**

$S_{11} = 704$

**[A1]**

> **[mark-scheme]**
> **B1**: Form a correct equation in $a$ and $d$ from at least one sum, e.g. $2 a + 19 d = 29$ or $2 a + 23 d = - 15$.
> 
> **M1**: Solve your two equations simultaneously (subtracting to eliminate $a$).
> 
> **A1**: Correct $a = 119$ and $d = - 11$.
> 
> **M1**: Identify that the maximum occurs at the last non-negative term, e.g. by solving $u_{n} = 130 - 11 n \geq 0$.
> 
> **M1**: Substitute $n = 11$ into a correct sum formula.
> 
> **A1**: Correct greatest value $704$.

### Q5
The common difference is constant, so equate the gap between the first pair of terms with the gap between the second pair

$1 - ( 2 q - p ) = ( p - q ) - 1$

$1 - 2 q + p = p - q - 1$

**[M1]**

Solve for $q$

$q = 2$

**[A1]**

Equate another pair of gaps to form an equation linking $p$ and $q$

$1 - ( 2 q - p ) = ( 3 p - 4 q ) - ( p - q )$

$1 - 2 q + p = 2 p - 3 q \Rightarrow p = 1 + q$

**[M1]**

Substitute $q = 2$

$p = 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Use the common difference to form an equation from the first three terms, $1 - ( 2 q - p ) = ( p - q ) - 1$.
> 
> **A1**: Correct value $q = 2$.
> 
> **M1**: Form a second equation using another pair of consecutive terms, leading to $p = 1 + q$.
> 
> **A1**: Correct value $p = 3$.

### Q6
The common difference is $d = 3 q^{2} - 2$; use $u_{3} = q = a + 2 d$ to form an equation in $q$

$q = 2 + 2 ( 3 q^{2} - 2 ) = 6 q^{2} - 2$

$6 q^{2} - q - 2 = 0$

**[M1]**

Factorise and solve; the terms must all be positive, so reject the negative root

$( 3 q - 2 ) ( 2 q + 1 ) = 0$

$q = \frac{2}{3}$

**[A1]**

Find the common difference

`d = 3\left(\dfrac{2}{3}\right)^2 - 2 = -\dfrac{2}{3}`

**[M1]**

Use $u_{40} = a + 39 d$ with $a = 2$

`u_{40} = 2 + 39\left(-\dfrac{2}{3}\right)`

$u_{40} = - 24$

**[A1]**

> **[mark-scheme]**
> **M1**: Use the common difference to form a quadratic in $q$, $6 q^{2} - q - 2 = 0$.
> 
> **A1**: Correct value $q = \frac{2}{3}$, rejecting $q = - \frac{1}{2}$ because the terms must be positive.
> 
> **M1**: Find $d = - \frac{2}{3}$ and substitute into $u_{40} = a + 39 d$.
> 
> **A1**: Correct fortieth term $- 24$.

### Q7
Form an equation from $S_{24} = 9 S_{2}$ using $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$

$12 ( 2 a + 23 d ) = 9 ( 2 a + d )$

**[M1]**

Expand and simplify to a relationship between $a$ and $d$

$24 a + 276 d = 18 a + 9 d \Rightarrow 6 a = - 267 d$

**[A1]**

For the sum of $90$ terms, $S_{90} = 45 ( 2 a + 89 d )$; substitute $2 a = - 89 d$ (from $6 a = - 267 d$)

`S_{90} = 45\left(-89d + 89d\right)`

**[M1]**

$S_{90} = 0$

**[A1]**

> **[mark-scheme]**
> **M1**: Use $S_{24} = 9 S_{2}$ to form an equation, $12 ( 2 a + 23 d ) = 9 ( 2 a + d )$.
> 
> **A1**: Simplify to a correct relationship, $6 a = - 267 d$ (or $2 a = - 89 d$).
> 
> **M1**: Substitute into $S_{90} = 45 ( 2 a + 89 d )$.
> 
> **A1**: Correct value $S_{90} = 0$.

### Q8
Read the first term and common difference from $u_{k} = 16 + 7 k$: $a = u_{1} = 23$ and $d = 7$

The required sum is $S_{25} - S_{14}$

`S_{25} = \dfrac{25}{2}\left(2(23) + 24(7)\right) = 2675`

**[M1]**

Find $S_{14}$ and subtract to isolate the fifteenth to twenty-fifth terms

`S_{14} = \dfrac{14}{2}\left(2(23) + 13(7)\right) = 959`

$S_{25} - S_{14} = 2675 - 959$

**[M1]**

$1716$

**[A1]**

> **[mark-scheme]**
> **M1**: Using $a = 23$ and $d = 7$, find $S_{25}$ (or $S_{14}$) with a correct sum formula.
> 
> **M1**: Form $S_{25} - S_{14}$ to isolate the fifteenth to twenty-fifth terms.
> 
> **A1**: Correct value $1716$.
Each term of the new progression is $3$ less than the matching term of the original, so its sum of $25$ terms is $S_{25}$ reduced by $25 \times 3$

$S_{25} - 3 ( 25 ) = 2675 - 75$

**[M1]**

$2600$

**[A1]**

> **[mark-scheme]**
> **M1**: Recognise the new sum is $S_{25} - 3 \times 25$ (or sum a new progression with $a = 20$ and $d = 7$).
> 
> **A1**: Correct value $2600$.

### Q9
Find the common difference from the first two terms

$d = 3 - ( p + 15 ) = - p - 12$

Use $u_{4} = a + 3 d$ (with $a = p + 15$), which equals $3 p - 16$

$( p + 15 ) + 3 ( - p - 12 ) = 3 p - 16$

**[M1]**

Simplify the left-hand side to a linear equation in $p$

$- 2 p - 21 = 3 p - 16$

**[A1]**

Solve for $p$

$- 5 = 5 p$

$p = - 1$

**[A1]**

> **[mark-scheme]**
> **M1**: Find $d = - p - 12$ and substitute into $u_{4} = a + 3 d = 3 p - 16$.
> 
> **A1**: A correct simplified linear equation, such as $- 2 p - 21 = 3 p - 16$.
> 
> **A1**: Correct value $p = - 1$.

### Q10
The odd numbers form an arithmetic progression with first term $a = 1$ and common difference $d = 2$

**[B1]**

Substitute into $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$ and simplify

`S_n = \dfrac{n}{2}\left(2(1) + (n-1)(2)\right) = \dfrac{n}{2}(2n)`

**[M1]**

**Final answer:** $S_{n} = n^{2}$** as required**

**[A1]**

> **[mark-scheme]**
> **B1**: Identify the odd numbers as an arithmetic progression with $a = 1$ and $d = 2$ (seen or implied).
> 
> **M1**: Substitute into a correct sum formula, $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$.
> 
> **A1**: Simplify convincingly to the printed result $n^{2}$.
(i)

The first term is $a = 7 k$ and the common difference is $d = 7 k$; use $u_{n} = a + ( n - 1 ) d = 1008$

$7 k + ( n - 1 ) ( 7 k ) = 1008 \Rightarrow 7 k n = 1008$

$n = \frac{144}{k}$

**[B1]**

(ii)

Since $n = \frac{144}{k}$ must be a positive whole number of terms, $k$ must divide $144$ and be positive

$k > 0$

**Final answer:** $k$** is a factor of **$144$

**[B1]**

(iii)

Use $S_{n} = \frac{n}{2} ( a + l )$ with $a = 7 k$, $l = 1008$ and $n = \frac{144}{k}$

`S_n = \dfrac{1}{2} \cdot \dfrac{144}{k}(7k + 1008)`

**[M1]**

Expand to split the expression into two terms

$S_{n} = \frac{72}{k} ( 7 k + 1008 ) = 504 + \frac{72\times1008}{k}$

**[M1]**

**Final answer:** $S_{n} = 504 + \frac{72576}{k}$** as required**

**[A1]**

> **[mark-scheme]**
> **B1**: Correct number of terms, $n = \frac{144}{k}$ (accept an unsimplified equivalent).
> 
> **B1**: Both further conditions stated — $k > 0$ and $k$ is a factor of $144$.
> 
> **M1**: Substitute $a = 7 k$, $l = 1008$ (or $d = 7 k$) and your $n$ into a correct sum formula.
> 
> **M1**: Expand to split the expression into two terms.
> 
> **A1**: Reach the printed result $504 + \frac{72576}{k}$ with no errors.

### Q11
Substitute $a = r^{2}$ and $d = 2 r$ into $u_{4} = a + 3 d = 4$

$r^{2} + 3 ( 2 r ) = 4$

**[M1]**

$r^{2} + 6 r - 4 = 0$

**[A1]**

This does not factorise, so use the quadratic formula

$r = \frac{-6\pm\sqrt{6^{2}-4(1)(-4)}}{2} = \frac{-6\pm\sqrt{52}}{2} = - 3 \pm \sqrt{13}$

**[M1]**

Since $r > 0$ and $- 3 - \sqrt{13} < 0$, take the positive root

$r = - 3 + \sqrt{13}$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitute $a = r^{2}$ and $d = 2 r$ into $u_{4} = a + 3 d = 4$.
> 
> **A1**: Correct quadratic $r^{2} + 6 r - 4 = 0$.
> 
> **M1**: Solve using the quadratic formula (or completing the square), reaching $r = - 3 \pm \sqrt{13}$.
> 
> **A1**: Correct exact value $r = - 3 + \sqrt{13}$ (accept $\sqrt{13} - 3$). You must reject the negative root and leave the answer in exact surd form — a rounded decimal loses this mark.

### Q12
Write the seventh term and the sum of the first nine terms in terms of $a$ and $d$

$u_{7} = a + 6 d = 3 k$

**[B1]**

$S_{9} = \frac{9}{2} ( 2 a + 8 d ) = 9 ( a + 4 d ) = 4 k - 3$

**[B1]**

From the first equation $a = 3 k - 6 d$; substitute into the second to eliminate $a$

`9\left((3k - 6d) + 4d\right) = 4k - 3 \implies 27k - 18d = 4k - 3`

**[M1]**

Solve for $d$

$d = \frac{23k+3}{18}$

**[A1]**

Substitute back into $a = 3 k - 6 d$ to find $a$

`a = 3k - 6\left(\dfrac{23k + 3}{18}\right)`

$a = - \frac{14k+3}{3}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct seventh-term equation, $a + 6 d = 3 k$.
> 
> **B1**: Correct sum equation, $9 ( a + 4 d ) = 4 k - 3$ (or $\frac{9}{2} ( 2 a + 8 d ) = 4 k - 3$).
> 
> **M1**: Eliminate $a$ (or $d$) from your two equations by a valid method.
> 
> **A1**: Correct $d = \frac{23k+3}{18}$ (or exact equivalent).
> 
> **A1**: Correct $a = - \frac{14k+3}{3}$ (or exact equivalent).
Use $u_{19} = a + 18 d = 57$ with the expressions from part (a)

`-\dfrac{14k + 3}{3} + 18\left(\dfrac{23k + 3}{18}\right) = 57`

**[M1]**

Multiply through by $3$, then simplify and solve for $k$

$- ( 14 k + 3 ) + 3 ( 23 k + 3 ) = 171$

$55 k + 6 = 171 \Rightarrow 55 k = 165$

$k = 3$

**[A1]**

With $k = 3$, $a = - 15$ and $d = 4$; substitute into $S_{25} = \frac{25}{2} ( 2 a + 24 d )$

`S_{25} = \dfrac{25}{2}\left(2(-15) + 24(4)\right) = \dfrac{25}{2}(66)`

**[M1]**

$S_{25} = 825$

**[A1]**

> **[mark-scheme]**
> **M1**: Form $a + 18 d = 57$ using your expressions from part (a).
> 
> **A1**: Correct value $k = 3$ (leading to $a = - 15$ and $d = 4$).
> 
> **M1**: Substitute your numerical $a$, $d$ and $n = 25$ into a correct sum formula.
> 
> **A1**: Correct value $825$.

### Q13
Use $u_{n} = a + ( n - 1 ) d$ to turn the third and eleventh terms into two equations

$a + 2 d = 32$

$a + 10 d = 0$

**[M1]**

Subtract to find $d$, then back-substitute for $a$

$8 d = - 32 \Rightarrow d = - 4 ,  a = 40$

**[A1]**

Substitute $a$, $d$ and $S_{n} = - 44$ into $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$

`\dfrac{n}{2}\left(80 + (n-1)(-4)\right) = -44`

**[M1]**

Clear the fraction and simplify to a three-term quadratic in $n$

$n ( 84 - 4 n ) = - 88 \Rightarrow 4 n^{2} - 84 n - 88 = 0$

$n^{2} - 21 n - 22 = 0$

**[M1]**

Factorise; $n$ must be a positive integer, so reject $n = - 1$

$( n - 22 ) ( n + 1 ) = 0$

$n = 22$

**[A1]**

> **[mark-scheme]**
> **M1**: Use $u_{n} = a + ( n - 1 ) d$ to form two correct equations, $a + 2 d = 32$ and $a + 10 d = 0$.
> 
> **A1**: Correct values $a = 40$ and $d = - 4$.
> 
> **M1**: Substitute your $a$, $d$ and $S_{n} = - 44$ into a correct sum formula.
> 
> **M1**: Simplify to the three-term quadratic $n^{2} - 21 n - 22 = 0$ and attempt to solve.
> 
> **A1**: Correct value $n = 22$. You must reject the negative root $n = - 1$.

### Q14
The first term is $a = k + 13$ and the common difference is $d = ( 2 k + 9 ) - ( k + 13 ) = k - 4$; write $u_{n} = a + ( n - 1 ) d$

$u_{n} = ( k + 13 ) + ( n - 1 ) ( k - 4 ) = 17 + n ( k - 4 )$

**[M1]**

Make $n$ the subject

$n = \frac{u_{n}-17}{k-4}$

**[A1]**

> **[mark-scheme]**
> **M1**: Find $d = k - 4$ and form $u_{n} = ( k + 13 ) + ( n - 1 ) ( k - 4 )$, simplifying towards $u_{n} = 17 + n ( k - 4 )$.
> 
> **A1**: Correct expression $n = \frac{u_{n}-17}{k-4}$.
Substitute $u_{n} = - 16$ into the expression from part (a)

$n = \frac{-16-17}{k-4} = \frac{-33}{k-4}$

**[M1]**

Use $S_{n} = \frac{n}{2} ( a + u_{n} )$ with $a = k + 13$ and $u_{n} = - 16$, set equal to $- 11$

`\dfrac{n}{2}\left((k + 13) + (-16)\right) = \dfrac{n}{2}(k - 3) = -11`

**[M1]**

Substitute $n = \frac{-33}{k-4}$ and clear the fractions

$\frac{-33}{k-4} ( k - 3 ) = - 22 \Rightarrow - 33 ( k - 3 ) = - 22 ( k - 4 )$

**[M1]**

Expand and solve for $k$

$- 33 k + 99 = - 22 k + 88 \Rightarrow 11 k = 11$

**[A1]**

$k = 1$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitute $u_{n} = - 16$ into your expression to get $n = \frac{-33}{k-4}$.
> 
> **M1**: Use a correct sum formula (for example $S_{n} = \frac{n}{2} ( a + u_{n} )$) with $S_{n} = - 11$.
> 
> **M1**: Substitute your $n$ and clear the fractions to reach an equation in $k$ only.
> 
> **A1**: Reach a correct linear equation, such as $11 k = 11$.
> 
> **A1**: Correct value $k = 1$.

### Q15
The common difference is constant, so the second term minus the first equals the third minus the second

$q^{2} - ( q - 2 ) = ( 4 q + 5 ) - q^{2}$

**[M1]**

Rearrange into a quadratic equation in $q$

$q^{2} - q + 2 = - q^{2} + 4 q + 5 \Rightarrow 2 q^{2} - 5 q - 3 = 0$

**[A1]**

Factorise and solve; both values give a valid progression, so keep both

$( 2 q + 1 ) ( q - 3 ) = 0$

**Final answer:** $q = - \frac{1}{2}$** or **$q = 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Use the common difference to form an equation, $q^{2} - ( q - 2 ) = ( 4 q + 5 ) - q^{2}$ (or $2 q^{2} = ( q - 2 ) + ( 4 q + 5 )$).
> 
> **A1**: A correct three-term quadratic, $2 q^{2} - 5 q - 3 = 0$.
> 
> **A1**: Both correct values, $q = - \frac{1}{2}$ and $q = 3$. Both give valid progressions, so both are required; giving only one scores A0.

### Q16
Write each sum using $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$ to form two equations in $a$ and $d$

$S_{12} = 6 ( 2 a + 11 d ) = 654 \Rightarrow 2 a + 11 d = 109$

$S_{20} = 10 ( 2 a + 19 d ) = 530 \Rightarrow 2 a + 19 d = 53$

**[M1 A1]**

Subtract to eliminate $a$ and find $d$, then back-substitute for $a$

$8 d = - 56 \Rightarrow d = - 7 ,  2 a = 186 \Rightarrow a = 93$

**[M1]**

Find the twenty-first term using $u_{21} = a + 20 d$

$u_{21} = 93 + 20 ( - 7 )$

$u_{21} = - 47$

**[A1]**

> **[mark-scheme]**
> **M1**: Use $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$ to form an equation in $a$ and $d$ from at least one sum.
> 
> **A1**: Both correct simplified equations, $2 a + 11 d = 109$ and $2 a + 19 d = 53$.
> 
> **M1**: Solve your two equations simultaneously to find $a = 93$ and $d = - 7$.
> 
> **A1**: Correct twenty-first term, $u_{21} = - 47$.

### Q17
The common difference is constant, so the second term minus the first equals the third minus the second

$( q + 1 ) - ( - 1 ) = q^{2} - ( q + 1 )$

**[M1]**

Rearrange into a quadratic equation in $q$

$q + 2 = q^{2} - q - 1$

$q^{2} - 2 q - 3 = 0$

**[A1]**

Factorise and solve; both values give a valid progression, so keep both

$( q - 3 ) ( q + 1 ) = 0$

**Final answer:** $q = 3$** or **$q = - 1$

**[A1]**

> **[mark-scheme]**
> **M1**: Use the common difference to form an equation, $( q + 1 ) - ( - 1 ) = q^{2} - ( q + 1 )$ (or $2 ( q + 1 ) = - 1 + q^{2}$).
> 
> **A1**: A correct three-term quadratic, $q^{2} - 2 q - 3 = 0$ (or an exact multiple of it).
> 
> **A1**: Both correct values, $q = 3$ and $q = - 1$. Both give valid progressions ($d = 5$ and $d = 1$), so both are required; giving only one value scores A0.

### Q18
Write each sum condition using `S_n = \dfrac{n}{2}\left(2a + (n-1)d\right)` to form two equations in $a$ and $d$

$S_{10} = 5 ( 2 a + 9 d ) = 40 \Rightarrow 2 a + 9 d = 8$

$S_{20} = 10 ( 2 a + 19 d ) = 280 \Rightarrow 2 a + 19 d = 28$

**[M1]**

Subtract the first equation from the second to eliminate $a$ and find $d$

$10 d = 20 \Rightarrow d = 2$

**[M1]**

Substitute $d = 2$ back into $2 a + 9 d = 8$ to find $a$

$2 a + 18 = 8$

$a = - 5 ,  d = 2$

**[A1]**

> **[mark-scheme]**
> **M1**: Use $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$ to form two correct equations, $2 a + 9 d = 8$ and $2 a + 19 d = 28$.
> 
> **M1**: A valid method to solve your two equations simultaneously (for example, subtracting to eliminate $a$).
> 
> **A1**: Both values correct — $a = - 5$ and $d = 2$.

### Q19
Use $u_{n} = a + ( n - 1 ) d$ to turn the third and twelfth terms into two equations

$a + 2 d = 2$

$a + 11 d = 65$

**[M1]**

Subtract to find $d$, then back-substitute to find $a$

$9 d = 63 \Rightarrow d = 7$

$a + 2 ( 7 ) = 2 \Rightarrow a = - 12$

**[A1]**

Substitute $a = - 12$ and $d = 7$ into $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$ and set it equal to $390$

`\dfrac{n}{2}\left(2(-12) + (n-1)(7)\right) = 390`

**[M1]**

Clear the fraction and expand the bracket to reach the required form

$n ( - 24 + 7 n - 7 ) = 780 \Rightarrow 7 n^{2} - 31 n = 780$

**Final answer:** $7 n^{2} - 31 n - 780 = 0$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Use $u_{n} = a + ( n - 1 ) d$ to form two correct equations, $a + 2 d = 2$ and $a + 11 d = 65$.
> 
> **A1**: Correct values $a = - 12$ and $d = 7$.
> 
> **M1**: Substitute your $a$ and $d$ into a correct sum formula and set it equal to $390$.
> 
> **A1**: Convincingly reach the printed quadratic $7 n^{2} - 31 n - 780 = 0$, showing a clear intermediate step (such as $n ( 7 n - 31 ) = 780$).
Factorise the quadratic

$( n - 13 ) ( 7 n + 60 ) = 0$

Since $n$ is the number of terms it must be a positive integer, so reject $n = - \frac{60}{7}$

$n = 13$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct value $n = 13$. You must reject the negative fractional root $n = - \frac{60}{7}$; leaving both values scores B0.

### Q20
In an arithmetic progression consecutive terms share a common difference, so the second term minus the first equals the third minus the second

$( - 7 ) - ( p - 9 ) = ( 9 - 3 p ) - ( - 7 )$

**[M1]**

Simplify each side to a linear equation in $p$

$2 - p = 16 - 3 p$

$2 p = 14$

**[A1]**

Solve for $p$

$p = 7$

**[A1]**

> **[mark-scheme]**
> **M1**: Use the common difference to form an equation, $( - 7 ) - ( p - 9 ) = ( 9 - 3 p ) - ( - 7 )$ (or $2 ( - 7 ) = ( p - 9 ) + ( 9 - 3 p )$).
> 
> **A1**: A correct simplified linear equation, such as $2 - p = 16 - 3 p$ or $2 p = 14$.
> 
> **A1**: Correct value $p = 7$.

### Q21
Read the first term and common difference from $u_{k} = 26 - 3 k$: $a = u_{1} = 23$ and $d = - 3$; substitute into $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$

`S_{10} = \dfrac{10}{2}\left(2(23) + (10-1)(-3)\right)`

**[M1]**

Work through the arithmetic

$S_{10} = 5 ( 46 - 27 )$

$S_{10} = 95$

**[A1]**

> **[mark-scheme]**
> **M1**: Identify $a = 23$ and $d = - 3$ from $u_{k} = 26 - 3 k$ and substitute into a correct sum formula.
> 
> **A1**: Correct value $S_{10} = 95$.
The sum of the eleventh to fifteenth terms is $S_{15} - S_{10}$; first find $S_{15}$

`S_{15} = \dfrac{15}{2}\left(2(23) + (15-1)(-3)\right) = \dfrac{15}{2}(46 - 42) = 30`

**[M1]**

Subtract the value of $S_{10}$ found in part (a)

$S_{15} - S_{10} = 30 - 95$

**[M1]**

$- 65$

**[A1]**

> **[mark-scheme]**
> **M1**: Find $S_{15}$ using a correct sum formula with $a = 23$ and $d = - 3$, obtaining $30$.
> 
> **M1**: Subtract your $S_{10}$ from your $S_{15}$ to isolate the eleventh to fifteenth terms.
> 
> **A1**: Correct value $- 65$. Alternatively, treat these terms as a new progression with first term $u_{11} = - 7$, common difference $- 3$ and $5$ terms.

### Q22
(i)

Substitute $a = r^{2}$ and $d = 3 r$ into $u_{5} = a + 4 d = 85$ to form an equation in $r$

$r^{2} + 4 ( 3 r ) = 85$

$r^{2} + 12 r - 85 = 0$

**[M1]**

Factorise and solve the quadratic

$( r - 5 ) ( r + 17 ) = 0$

**[M1]**

Since $r > 0$, reject $r = - 17$

$r = 5$

**[A1]**

(ii)

With $r = 5$ the first term is $a = 25$ and the common difference is $d = 15$; use $u_{9} = a + 8 d$

$u_{9} = 25 + 8 ( 15 )$

$u_{9} = 145$

**[B1]**

> **[mark-scheme]**
> **M1**: Substitute $a = r^{2}$ and $d = 3 r$ into $u_{5} = a + 4 d = 85$ to form the quadratic $r^{2} + 12 r - 85 = 0$.
> 
> **M1**: Solve your three-term quadratic by factorising, using the formula, or completing the square.
> 
> **A1**: Correct value $r = 5$. You must reject $r = - 17$ because $r > 0$; leaving both values scores A0.
> 
> **B1**: Correct ninth term $u_{9} = 145$ (follow-through using your positive value of $r$).

### Q23
This is an arithmetic progression with $a = 1$, $d = 2$ and last term $149$; find the number of terms from $u_{n} = 149$ using `u subscript n equals a plus open parentheses n minus 1 close parentheses d`

$1 + ( n - 1 ) ( 2 ) = 149 \Rightarrow n = 75$

**[B1]**

Use $S_{n} = \frac{n}{2} ( a + l )$ with $n = 75$

$S_{75} = \frac{75}{2} ( 1 + 149 )$

**[M1]**

$S_{75} = 5625$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct number of terms, $n = 75$ (seen or implied).
> 
> **M1**: Substitute $a = 1$, $l = 149$ and your $n$ into a correct sum formula.
> 
> **A1**: Correct value $5625$. (This equals $75^{2}$ — the sum of the first $m$ odd numbers is always $m^{2}$.)
(i)

The first term is $a = k$, the common difference is $d = k$ and the last term is $360$; the last term is the $n$th multiple of $k$

$n k = 360$

$n = \frac{360}{k}$

**[B1]**

(ii)

Use $S_{n} = \frac{n}{2} ( a + l )$ with $a = k$, $l = 360$ and $n = \frac{360}{k}$

`S_n = \dfrac{1}{2} \cdot \dfrac{360}{k}(k + 360)`

**[M1]**

Expand to split the expression into two terms

$S_{n} = \frac{180}{k} ( k + 360 ) = 180 + \frac{180\times360}{k}$

**[M1]**

**Final answer:** $S_{n} = 180 + \frac{64800}{k}$** as required**

**[A1]**

> **[mark-scheme]**
> **B1**: Correct number of terms, $n = \frac{360}{k}$ (accept an unsimplified equivalent).
> 
> **M1**: Substitute $a = k$, $l = 360$ and your $n$ into a correct sum formula.
> 
> **M1**: Expand to split the expression into two terms.
> 
> **A1**: Reach the printed result $180 + \frac{64800}{k}$ with no errors.
Find the common difference using the fact that the difference between consecutive terms is the same

$d = ( 5 q - 4 ) - ( 3 q - 7 ) = 2 q + 3$

Use $u_{100} = a + 99 d$ with $a = 3 q - 7$

$u_{100} = ( 3 q - 7 ) + 99 ( 2 q + 3 )$

**[M1]**

Expand and collect like terms

$u_{100} = 201 q + 290$

**[A1]**

> **[mark-scheme]**
> **M1**: Find $d = 2 q + 3$ and substitute $a$ and $d$ into $u_{100} = a + 99 d$.
> 
> **A1**: Correct term $201 q + 290$, in simplest form.

### Q24
Write the fifth term and the sum of the first eight terms in terms of $a$ and $d$

$u_{5} = a + 4 d = k$

$S_{8} = \frac{8}{2} ( 2 a + 7 d ) = 4 ( 2 a + 7 d ) = 2 k$

**[M1]**

From the first equation $d = \frac{k-a}{4}$; substitute into the second to eliminate $d$

`4\left(2a + 7 \cdot \dfrac{k - a}{4}\right) = 2k \implies 8a + 7(k - a) = 2k`

**[M1]**

Simplify to make $a$ the subject

$a + 7 k = 2 k$

**Final answer:** $a = - 5 k$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Write both conditions algebraically — $u_{5} = a + 4 d = k$ and $S_{8} = 4 ( 2 a + 7 d ) = 2 k$ — with at least one fully correct.
> 
> **M1**: Eliminate $d$ (or $a$) from your two equations by a valid method.
> 
> **A1**: Reach the printed $a = - 5 k$, showing an intermediate step (such as $d = \frac{3k}{2}$ or $a + 7 k = 2 k$).
Substitute $a = - 5 k$ into $k = a + 4 d$ from part (a) to isolate $d$

$4 d = k - ( - 5 k ) = 6 k$

**[M1]**

$d = \frac{3k}{2}$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitute $a = - 5 k$ into $k = a + 4 d$ (or use $d = \frac{k-a}{4}$) to isolate $d$.
> 
> **A1**: Correct expression $d = \frac{3k}{2}$ (accept $1 . 5 k$).
Use $u_{9} = a + 8 d = 14$ with $a = - 5 k$ and $d = \frac{3k}{2}$

`-5k + 8\left(\dfrac{3k}{2}\right) = 14`

**[M1]**

Simplify and solve

$- 5 k + 12 k = 14 \Rightarrow 7 k = 14$

$k = 2$

**[A1]**

> **[mark-scheme]**
> **M1**: Form $a + 8 d = 14$ using your expressions in terms of $k$, giving $- 5 k + 12 k = 14$.
> 
> **A1**: Correct value $k = 2$.
With $k = 2$ the first term is $a = - 5 ( 2 ) = - 10$ and the common difference is $d = \frac{3(2)}{2} = 3$

Substitute into $S_{30} = \frac{30}{2} ( 2 a + 29 d )$

`S_{30} = 15\left(2(-10) + 29(3)\right)`

**[M1]**

$S_{30} = 15 ( - 20 + 87 )$

$S_{30} = 1005$

**[A1]**

> **[mark-scheme]**
> **M1**: Find $a = - 10$ and $d = 3$ and substitute $n = 30$ into a correct sum formula.
> 
> **A1**: Correct value $1005$.

### Q25
The first term is $a = k + 7$ and the common difference is $d = ( 2 k + 18 ) - ( k + 7 ) = k + 11$; substitute into $u_{n} = a + ( n - 1 ) d = 36$

$( k + 7 ) + ( n - 1 ) ( k + 11 ) = 36$

**[M1]**

Make $( n - 1 ) ( k + 11 )$ the subject, then divide and add $1$

$( n - 1 ) ( k + 11 ) = 29 - k \Rightarrow n - 1 = \frac{29-k}{k+11}$

**Final answer:** $n = \frac{29-k}{k+11} + 1 = \frac{40}{k+11}$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Find $d = k + 11$ and substitute $a$ and $d$ into $u_{n} = a + ( n - 1 ) d = 36$.
> 
> **A1**: Rearrange convincingly to the printed $n = \frac{40}{k+11}$, showing the intermediate step $n - 1 = \frac{29-k}{k+11}$.
Use $S_{n} = \frac{n}{2} ( a + l )$ with first term $a = k + 7$, last term $l = 36$ and $n = \frac{40}{k+11}$ from part (a)

`S_n = \dfrac{1}{2} \cdot \dfrac{40}{k+11}\left((k+7) + 36\right)`

**[M1]**

Simplify the numerator

$S_{n} = \frac{20}{k+11} ( k + 43 ) = \frac{20(k+43)}{k+11}$

**[M1]**

Expand the numerator to reach the required form

**Final answer:** $S_{n} = \frac{20k+860}{k+11}$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Substitute your $a$, $l = 36$ (or $d$) and $n$ from part (a) into a correct sum formula.
> 
> **M1**: Simplify to $\frac{20(k+43)}{k+11}$ (or equivalent single fraction).
> 
> **A1**: Reach the printed $\frac{20k+860}{k+11}$ with no errors.
Set the sum from part (b) equal to $180$ and clear the fraction

$\frac{20k+860}{k+11} = 180 \Rightarrow 20 k + 860 = 180 ( k + 11 )$

Expand and solve for $k$

$20 k + 860 = 180 k + 1980 \Rightarrow 160 k = - 1120$

$k = - 7$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct value $k = - 7$.

### Q26
Substitute $n = 1 , 2 , 3 , 4$ into $u_{n} = 2 n + 3$ to list the first four terms

$u_{1} = 5 ,  u_{2} = 7 ,  u_{3} = 9 ,  u_{4} = 11$

Add the four terms to find the required sum

$5 + 7 + 9 + 11 = 32$

**[B1]**

A sequence is arithmetic when the difference between consecutive terms is constant, so compare those differences

$7 - 5 = 9 - 7 = 11 - 9 = 2$

State the conclusion, referring to the common difference

**Final answer:** **The difference between consecutive terms is a constant (equal to 2), so the sequence is arithmetic**

**[B1]**

> **[mark-scheme]**
> **B1**: The first four terms are $5 ,  7 ,  9 ,  11$ and their sum is $32$.
> 
> **B1**: A correct justification that the sequence is arithmetic — the difference between consecutive terms is constant (here it is $2$). Stating that there is a common difference is enough for the mark.

### Q27
(i)

The same common difference separates consecutive terms, so find it from the first two terms

$d = 18 - 30 = - 12$

Continue subtracting $12$ from each term in turn

$- 6 ,  - 18 ,  - 30$

**[B1]**

(ii)

Rewriting each term with a common denominator of $12$ makes the common difference clear

$\frac{3}{12} ,  \frac{5}{12} ,  \frac{7}{12} ,  \frac{9}{12} ,  \dots$

Each term increases by $\frac{2}{12} = \frac{1}{6}$, so continue adding $\frac{2}{12}$

$\frac{11}{12} ,  \frac{13}{12} ,  \frac{5}{4}$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct next three terms for part (i): $- 6 ,  - 18 ,  - 30$. The common difference is $- 12$.
> 
> **B1**: Correct next three terms for part (ii): $\frac{11}{12} ,  \frac{13}{12} ,  \frac{5}{4}$. Writing the terms over a denominator of $12$ helps you see the common difference of $\frac{1}{6}$; accept $\frac{15}{12}$ for the last term.

### Q28
Using $u_{n} = a + ( n - 1 ) d$, turn the fourth and eighth terms into two equations

$a + 3 d = 20$

$a + 7 d = 64$

**[M1]**

Subtract the first equation from the second to eliminate $a$ and find $d$

$4 d = 44 \Rightarrow d = 11$

**[M1]**

Substitute $d = 11$ back into $a + 3 d = 20$ to find the first term

$a + 33 = 20$

$a = - 13 ,  d = 11$

**[A1]**

> **[mark-scheme]**
> **M1**: Set up two correct equations from the given terms using $u_{n} = a + ( n - 1 ) d$: $a + 3 d = 20$ and $a + 7 d = 64$.
> 
> **M1**: A valid method to solve your two equations simultaneously (for example, subtracting to eliminate $a$).
> 
> **A1**: Both values correct — $a = - 13$ and $d = 11$.
The twelfth and sixteenth terms are four common differences apart, and "differ by $20$" allows this gap to be positive or negative

$u_{16} - u_{12} = 4 d = \pm 20$

**[M1]**

Divide by $4$; both signs give a valid common difference

**Final answer:** $d = 5$** or **$d = - 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Form a correct equation for the difference of the two terms, $4 d = \pm 20$ (or $4 d = 20$). The four-term gap between the twelfth and sixteenth terms is $4 d$.
> 
> **A1**: Both values of the common difference — $d = 5$ and $d = - 5$. Award A0 if only one value is given.

### Q29
Substitute $a = 3$, $d = 4$ and $n = 20$ into the sum formula `S_n = \dfrac{n}{2}\left(2a + (n-1)d\right)`

`S_{20} = \dfrac{20}{2}\left(2(3) + (20-1)(4)\right)`

**[M1]**

Work through the arithmetic

$S_{20} = 10 ( 6 + 76 )$

$S_{20} = 820$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitute $a = 3$, $d = 4$ and $n = 20$ into a correct sum formula, $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$.
> 
> **A1**: Correct value $S_{20} = 820$.

### Q30
(i)

Read off the first term and common difference

$a = 16 ,  d = 20 - 16 = 4$

Use $u_{n} = a + ( n - 1 ) d$

$u_{n} = 16 + ( n - 1 ) ( 4 )$

$u_{n} = 4 n + 12$

**[B1]**

(ii)

Substitute $a = 3$ and $d = - 3$ into $u_{n} = a + ( n - 1 ) d$

$u_{n} = 3 + ( n - 1 ) ( - 3 )$

$u_{n} = 6 - 3 n$

**[B1]**

(iii)

Substitute $a = 2$ and $d = 6$ into $u_{n} = a + ( n - 1 ) d$

$u_{n} = 2 + ( n - 1 ) ( 6 )$

$u_{n} = 6 n - 4$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct nth-term formula for part (i): $u_{n} = 4 n + 12$. Any equivalent form, such as $u_{n} = 16 + 4 ( n - 1 )$, is acceptable.
> 
> **B1**: Correct nth-term formula for part (ii): $u_{n} = 6 - 3 n$ (or equivalent).
> 
> **B1**: Correct nth-term formula for part (iii): $u_{n} = 6 n - 4$ (or equivalent).

### Q31
The first term is $a = k$ and the common difference is $d = 2 k - k = k$; substitute into $u_{n} = a + ( n - 1 ) d$

$u_{n} = k + ( n - 1 ) k$

$u_{n} = k n$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct nth-term formula $u_{n} = k n$. Accept an unsimplified equivalent such as $k + ( n - 1 ) k$.
Substitute $a = k$ and $d = k$ into `S_n = \dfrac{n}{2}\left(2a + (n-1)d\right)`

`S_n = \dfrac{n}{2}\left(2k + (n-1)k\right)`

**[M1]**

Take out the common factor $k$ inside the bracket, since $2 k + ( n - 1 ) k = k ( n + 1 )$

`S_n = \dfrac{n}{2}\left(k(n + 1)\right)`

**Final answer:** $S_{n} = \frac{kn}{2} ( n + 1 )$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Substitute $a = k$ and $d = k$ into a correct sum formula, $S_{n} = \frac{n}{2} ( 2 a + ( n - 1 ) d )$.
> 
> **A1**: Convincingly simplify to the printed result $\frac{kn}{2} ( n + 1 )$, showing the factor of $k$ taken out of the bracket. As this is a "show that", each step must be visible.
Substitute $n = 12$ into the sum formula from part (b) and set it equal to $39$

$\frac{12k}{2} ( 12 + 1 ) = 39$

$78 k = 39$

**[M1]**

Solve for $k$

$k = \frac{1}{2}$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitute $n = 12$ into your sum expression and equate to $39$, reaching $78 k = 39$.
> 
> **A1**: Correct value $k = \frac{1}{2}$ (accept $0 . 5$). Do not accept a rounded decimal.

### Q32
The tenth term gives an equation in $d$; substitute $a = 3$ and $n = 10$ into $u_{n} = a + ( n - 1 ) d$

$3 + 9 d = 30$

**[M1]**

Solve for the common difference

$9 d = 27$

$d = 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Use the tenth term to form a correct equation in $d$: $3 + 9 d = 30$ (from $u_{10} = a + 9 d$ with $a = 3$).
> 
> **A1**: Correct common difference $d = 3$.
Substitute $a = 3$ and $d = 3$ into `S_n = \dfrac{n}{2}\left(2a + (n-1)d\right)` and set it equal to $630$

`\dfrac{n}{2}\left(2(3) + (n-1)(3)\right) = 630`

**[M1]**

Simplify the bracket, clear the fraction, then divide by the common factor to reach the required form

$\frac{n}{2} ( 3 n + 3 ) = 630 \Rightarrow n ( 3 n + 3 ) = 1260$

$3 n^{2} + 3 n = 1260 \Rightarrow n^{2} + n = 420$

**Final answer:** $n^{2} + n - 420 = 0$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Substitute $a = 3$ and your $d$ into a correct sum formula and equate to $630$.
> 
> **A1**: Convincingly reach the printed result $n^{2} + n - 420 = 0$. You must show a clear intermediate step (such as $n ( 3 n + 3 ) = 1260$ or $n ( n + 1 ) = 420$); jumping straight to the answer loses this mark.
Factorise the quadratic — two numbers with product $- 420$ and sum $1$ are $- 20$ and $21$

$( n - 20 ) ( n + 21 ) = 0$

**[M1]**

Since $n$ is the number of terms it must be a positive integer, so reject $n = - 21$

$n = 20$

**[A1]**

> **[mark-scheme]**
> **M1**: Solve the three-term quadratic by factorising (or using the formula) to obtain the two roots.
> 
> **A1**: Correct value $n = 20$. You must reject the negative root $n = - 21$; leaving both values as the final answer scores A0.

### Q33
(i)

Substitute $n = 10$ and $n = 20$ into $u_{n} = 4 + 5 n$

$u_{10} = 4 + 5 ( 10 ) = 54$

$u_{20} = 4 + 5 ( 20 ) = 104$

$u_{10} = 54 ,  u_{20} = 104$

**[B1]**

(ii)

Substitute $n = 10$ and $n = 20$ into $u_{n} = \frac{1}{2} - \frac{1}{4} n$

$u_{10} = \frac{1}{2} - \frac{1}{4} ( 10 ) = \frac{1}{2} - \frac{5}{2} = - 2$

$u_{20} = \frac{1}{2} - \frac{1}{4} ( 20 ) = \frac{1}{2} - 5 = - \frac{9}{2}$

$u_{10} = - 2 ,  u_{20} = - \frac{9}{2}$

**[B1]**

(iii)

Substitute $n = 10$ and $n = 20$ into $u_{n} = 50 - 5 n$

$u_{10} = 50 - 5 ( 10 ) = 0$

$u_{20} = 50 - 5 ( 20 ) = - 50$

$u_{10} = 0 ,  u_{20} = - 50$

**[B1]**

> **[mark-scheme]**
> **B1**: Both terms correct for part (i): $u_{10} = 54$ and $u_{20} = 104$.
> 
> **B1**: Both terms correct for part (ii): $u_{10} = - 2$ and $u_{20} = - \frac{9}{2}$ (accept $- 4 . 5$).
> 
> **B1**: Both terms correct for part (iii): $u_{10} = 0$ and $u_{20} = - 50$.
