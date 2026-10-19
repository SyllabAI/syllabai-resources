# Mark Schemes — Sequences & Series
**Series** · Cambridge (CIE) A-LEVEL maths (9709)


## Exam Questions (17 questions)


### Q1
The distance in the last (nth) week is $73$ miles, so use $S_{n} = \frac{n}{2} ( a + l )$ with last term $l = 73$ and total $S_{n} = 702$

$\frac{n}{2} ( a + 73 ) = 702$

**[M1]**

Multiply both sides by $2$

**Final answer:** $n ( a + 73 ) = 1404$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $S_{n} = \frac{n}{2} ( a + l )$ with $l = 73$ and $S_{n} = 702$.
> 
> **A1**: Correct multiplication by $2$ to reach the printed $n ( a + 73 ) = 1404$.
Write the distances in the last week and in the halfway week using $u_{k} = a + ( k - 1 ) d$

$a + ( n - 1 ) d = 73$

`a + \left(\dfrac{n}{2} - 1\right)d = 37`

**[B1]**

Subtract the halfway-week equation from the last-week equation to eliminate $a$

`\left(n - 1 - \dfrac{n}{2} + 1\right)d = 73 - 37 \implies \dfrac{n}{2}d = 36`

**[M1]**

**Final answer:** $n d = 72$** as required**

**[A1]**

> **[mark-scheme]**
> **B1**: Correct expression for the halfway-week distance, `a + \left(\dfrac{n}{2} - 1\right)d = 37`.
> 
> **M1**: Correct elimination of $a$ by subtracting the two term equations.
> 
> **A1**: Correct elimination reaching $n d = 72$.
From $n d = 72$, write $d = \frac{72}{n}$ and substitute into the last-week equation to express $a$ in terms of $n$

$a + ( n - 1 ) \frac{72}{n} = 73 \Rightarrow a = 1 + \frac{72}{n}$

**[M1]**

Substitute this into $n ( a + 73 ) = 1404$ to obtain an equation in $n$ only

`n\left(74 + \dfrac{72}{n}\right) = 1404 \implies 74n + 72 = 1404`

$n = 18$

**[A1]**

Use $n d = 72$ and $a = 1 + \frac{72}{n}$ to find $d$ and $a$

$d = \frac{72}{18} = 4$

$a = 1 + \frac{72}{18} = 5$

$a = 5 , d = 4 , n = 18$

**[A1 A1]**

> **[mark-scheme]**
> **M1**: Correct use of $n d = 72$ to write $d$ (or $a$) in terms of $n$, substituted into $n ( a + 73 ) = 1404$ to give an equation in $n$ only.
> 
> **A1**: $n = 18$.
> 
> **A1**: $a = 5$.
> 
> **A1**: $d = 4$.

### Q2
For the arithmetic progression, consecutive terms have a constant difference

$y - x = z - y \Rightarrow z = 2 y - x$

**[M1]**

For the geometric progression, consecutive terms have a constant ratio

$\frac{y}{x} = \frac{z}{y} \Rightarrow y^{2} = x z$

**[M1]**

Substitute $z = 2 y - x$ into $y^{2} = x z$ to eliminate $z$

$y^{2} = x ( 2 y - x ) = 2 x y - x^{2}$

$x^{2} - 2 x y + y^{2} = 0 \Rightarrow ( y - x )^{2} = 0$

**[M1]**

**Final answer:** $y = x$**, and hence **$z = 2 x - x = x$

**[A1]**

All three terms are equal, so describe each resulting progression (with $x \neq 0$ for the geometric progression to be defined)

**Final answer:** **The arithmetic progression is **$x , x , x , \dots$** with common difference 0, and the geometric progression is **$x , x , x , \dots$** with common ratio 1**

**[B1]**

> **[mark-scheme]**
> **M1**: Correct use of the constant-difference property of the arithmetic progression: $2 y = x + z$ (or $z = 2 y - x$).
> 
> **M1**: Correct use of the constant-ratio property of the geometric progression: $y^{2} = x z$ (or $\frac{y}{x} = \frac{z}{y}$).
> 
> **M1**: Correct substitution to eliminate $z$, forming $( y - x )^{2} = 0$ (or $y^{2} = 2 x y - x^{2}$).
> 
> **A1**: Correct conclusion $y = x$, and hence $z = x$.
> 
> **B1**: Correct full description of both progressions — each is the constant sequence $x , x , x , \dots$, the arithmetic one with common difference $0$ and the geometric one with common ratio $1$ (requiring $x \neq 0$).

### Q3
The common difference is the second term minus the first; set it equal to $- \frac{1}{7}$ and clear the fraction (multiply by $7$)

$\frac{6x}{7} - x^{2} = - \frac{1}{7}$

$6 x - 7 x^{2} = - 1 \Rightarrow 7 x^{2} - 6 x - 1 = 0$

**[M1]**

Factorise to find the possible values of $x$

$( 7 x + 1 ) ( x - 1 ) = 0$

**Final answer:** $x = 1$** or **$x = - \frac{1}{7}$

**[A1]**

Find the eighth term $u_{8} = a + 7 d = x^{2} - 1$ for each value of $x$

When $x = 1$

$u_{8} = 1^{2} - 1 = 0$

When $x = - \frac{1}{7}$

$u_{8} = \frac{1}{49} - 1 = - \frac{48}{49}$

**[M1]**

**Final answer:** $u_{8} = 0$** (when **$x = 1$**), **$u_{8} = - \frac{48}{49}$** (when **$x = - \frac{1}{7}$**)**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct formation of the common difference $\frac{6x}{7} - x^{2} = - \frac{1}{7}$, rearranged to a three-term quadratic.
> 
> **A1**: Both values $x = 1$ and $x = - \frac{1}{7}$.
> 
> **M1**: Correct substitution of an $x$ value into $u_{8} = a + 7 d = x^{2} - 1$.
> 
> **A1**: Both eighth terms, $0$ (when $x = 1$) and $- \frac{48}{49}$ (when $x = - \frac{1}{7}$).
(i)

The common ratio is the second term divided by the first; substitute $a = x^{2}$ and this ratio into the sum to infinity $\frac{a}{1-r} = 7$

$r = \frac{6x/7}{x^{2}} = \frac{6}{7x}$

$\frac{x^{2}}{1-\frac{6}{7x}} = 7 \Rightarrow \frac{7x^{3}}{7x-6} = 7$

**[M1]**

Simplify to a cubic in $x$

$x^{3} - 7 x + 6 = 0$

**[A1]**

The stem gives $x = 1$ as one solution, so $( x - 1 )$ is a factor; comparing coefficients gives the quadratic factor

$( x - 1 ) ( x^{2} + x - 6 ) = 0 \Rightarrow ( x - 1 ) ( x - 2 ) ( x + 3 ) = 0$

$x = 1 , x = 2 , x = - 3$

**[A1]**

(ii)

Find the first term $a = x^{2}$ and common ratio $r = \frac{6}{7x}$ for each value of $x$ (each ratio satisfies `\left| r \right| < 1`)

When $x = 1$

$a = 1 , r = \frac{6}{7}$

When $x = 2$

$a = 4 , r = \frac{3}{7}$

When $x = - 3$

$a = 9 , r = - \frac{2}{7}$

**[M1 A1]**

(iii)

Find the third term $u_{3} = a r^{2}$; in general it simplifies independently of $x$

`u_{3} = x^{2} \left(\frac{6}{7 x}\right)^{2} = x^{2} \cdot \frac{36}{49 x^{2}} = \frac{36}{49}`

**[M1]**

Confirm the same value for each progression

`1 \left(\frac{6}{7}\right)^{2} = 4 \left(\frac{3}{7}\right)^{2} = 9 \left(- \frac{2}{7}\right)^{2} = \frac{36}{49}`

**Final answer:** **All three progressions have third term **$\frac{36}{49}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct statement of $r = \frac{6}{7x}$, with $a = x^{2}$ and $r$ substituted into $\frac{a}{1-r} = 7$.
> 
> **A1**: Correct simplification to the printed cubic $x^{3} - 7 x + 6 = 0$.
> 
> **A1**: Correct factorisation, using the given $x = 1$ and comparing coefficients, giving the other roots $x = 2$ and $x = - 3$.
> 
> **M1**: Correct substitution of the $x$ values into $a = x^{2}$ and $r = \frac{6}{7x}$ to find the progression parameters.
> 
> **A1**: All three correct pairs — $( 1 , \frac{6}{7} )$, $( 4 , \frac{3}{7} )$, $( 9 , - \frac{2}{7} )$.
> 
> **M1**: Correct substitution into $u_{3} = a r^{2}$ (for the cases or in general).
> 
> **A1**: Correct demonstration that all three progressions give the same third term $\frac{36}{49}$.

### Q4
Separate the list by position: the terms in the odd positions and the terms in the even positions

The odd-position terms $3 , 6 , 9 , 12 , 15 , \dots$ increase by $3$ each time

**Final answer:** **Odd-position terms form an arithmetic progression **$3 , 6 , 9 , 12 , 15 , \dots$

**[B1]**

The even-position terms $1 , \frac{1}{2} , \frac{1}{4} , \dots$ are each half the previous

**Final answer:** **Even-position terms form a geometric progression **$1 , \frac{1}{2} , \frac{1}{4} , \frac{1}{8} , \dots$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct identification of the odd-position terms $3 , 6 , 9 , \dots$ as an arithmetic progression (constant addition of $3$).
> 
> **B1**: Correct identification of the even-position terms $1 , \frac{1}{2} , \frac{1}{4} , \dots$ as a geometric progression (constant multiplier $\frac{1}{2}$).
(i)

Check the differences between consecutive odd-position terms

$6 - 3 = 3 , 9 - 6 = 3 , 12 - 9 = 3$

**Final answer:** **Constant difference, so an arithmetic progression with **$a = 3$** and **$d = 3$

**[B1]**

(ii)

Use `S_m = \dfrac{m}{2}\left(2a + (m - 1)d\right)` with $a = 3$ and $d = 3$

`S_m = \dfrac{m}{2}\left(2(3) + (m - 1)(3)\right) = \dfrac{m}{2}(3m + 3)`

**[M1]**

$S_{m} = \frac{3m(m+1)}{2}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct demonstration of a constant difference of $3$, with first term $3$ and common difference $3$ stated.
> 
> **M1**: Correct use of `S_m = \dfrac{m}{2}\left(2a + (m - 1)d\right)` with $a = 3$ and $d = 3$.
> 
> **A1**: Correct simplified expression $\frac{3m(m+1)}{2}$.
The even-position terms form a geometric progression with $a = 1$ and $r = \frac{1}{2}$; use `S_n = \dfrac{a\left(1 - r^n\right)}{1 - r}`

`S_n = \dfrac{1\left(1 - \left(\frac{1}{2}\right)^n\right)}{1 - \frac{1}{2}}`

**[M1]**

`S_n = 2\left(1 - \left(\tfrac{1}{2}\right)^n\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of `S_n = \dfrac{a\left(1 - r^n\right)}{1 - r}` with $a = 1$ and $r = \frac{1}{2}$.
> 
> **A1**: Correct expression `2\left(1 - \left(\tfrac{1}{2}\right)^n\right)`. Allow accurate equivalents.
The first 20 terms are the first 10 odd-position (arithmetic) terms and the first 10 even-position (geometric) terms, so sum each with 10 terms

$S_{\text{AP}} = \frac{3(10)(11)}{2} = 165$

**[M1]**

`S_{\text{GP}} = 2\left(1 - \left(\tfrac{1}{2}\right)^{10}\right) = \dfrac{1023}{512} = 1.998046\ldots`

**[M1]**

Add the two sums

$165 + 1 . 998046 \dots$

**Final answer:** $166 . 9980$** (4 d.p.)**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct evaluation of the sum of the first 10 arithmetic terms ($165$).
> 
> **M1**: Correct evaluation of the sum of the first 10 geometric terms ($\frac{1023}{512} \approx 1 . 9980$).
> 
> **A1**: Total $166 . 9980$ to 4 decimal places.
Consider each component progression as the number of terms grows

**Final answer:** **No — the geometric part converges to 2, but the arithmetic part **$3 , 6 , 9 , \dots$** grows without bound, so the interleaved sequence has no sum to infinity**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct statement that the sum to infinity does not exist, because the arithmetic component diverges (its terms grow without bound), even though the geometric component converges.

### Q5
One lap of a lane is the two straight runs ($2 l$) plus the two semicircular ends, which together make one full circle of circumference $π d$ for the inner lane

$u_{1} = π d + 2 l$

**[B1]**

The $n$th lane has diameter $d + ( n - 1 ) e$ while the straight runs stay $2 l$, so its lap distance is

`u_n = \pi\left(d + (n - 1)e\right) + 2l = (\pi d + 2l) + (n - 1)\pi e`

**Final answer:** **This is an arithmetic progression with first term **$π d + 2 l$** and common difference **$π e$**, as required**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct inner-lane distance $π d + 2 l$ (two semicircles form a circle of circumference $π d$, plus two straight runs $2 l$).
> 
> **B1**: Correct $n$th lane distance $( π d + 2 l ) + ( n - 1 ) π e$, identifying the arithmetic progression with first term $π d + 2 l$ and common difference $π e$.
Sum the 12 lane distances using `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)`, with first term $a = π d + 2 l$ and common difference $π e$

`S_{12} = \dfrac{12}{2}\left(2(\pi d + 2l) + 11\pi e\right) = 6\left(4l + \pi(2d + 11e)\right)`

**[M1]**

Set this equal to the total distance and expand

`6\left(4l + \pi(2d + 11e)\right) = 96(4\pi + 5) = 480 + 384\pi`

$24 l + 6 π ( 2 d + 11 e ) = 480 + 384 π$

Since $l$, $d$ and $e$ are integers, equate the non-$π$ parts, then the $π$-coefficients

$24 l = 480 \Rightarrow l = 20$

**[A1]**

$6 ( 2 d + 11 e ) = 384$

**Final answer:** $2 d + 11 e = 64$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)` with $n = 12$, first term $π d + 2 l$ and common difference $π e$, set equal to $96 ( 4 π + 5 )$.
> 
> **A1**: Equating the non-$π$ (rational) parts to find $l = 20$.
> 
> **A1**: Equating the $π$-coefficients to reach the printed $2 d + 11 e = 64$ (justified by $l$, $d$, $e$ being integers).
A lane that is $2$ m wide adds $2$ m on each side, so the diameter of a lane grows by $2 \times 2$ m compared with the lane inside it

`e \geqslant 2 \times 2 = 4`

**[M1]**

The least value is $e = 4$; substitute into $2 d + 11 e = 64$

$2 d + 11 ( 4 ) = 64 \Rightarrow 2 d = 20$

$e = 4 , d = 10$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct reasoning that a lane at least $2$ m wide increases the diameter by $2$ m on each side, so `e \geqslant 4`.
> 
> **A1**: Least value $e = 4$ with associated $d = 10$.

### Q6
The bounce heights form a geometric progression with first term $x$ and common ratio $0 . 75$ (each is `25\%` shorter)

$a = x , r = 0 . 75$

**[B1]**

Since `|r| < 1`, the bounce heights have a sum to infinity; use $S_{\infty} = \frac{a}{1-r}$

$S_{\infty} = \frac{x}{1-0.75} = 4 x$

**[M1]**

On each bounce the ball rises to a height then falls back through the same distance, so the total distance is the initial drop $A$ plus twice the sum of the bounce heights

$D = A + 2 S_{\infty} = A + 2 ( 4 x )$

**[M1]**

**Final answer:** $D = A + 8 x$**, and fewer bounces travel less, so the total never exceeds **$( A + 8 x )$** metres, as required**

**[A1]**

> **[mark-scheme]**
> **B1**: Correct identification of the bounce heights as a geometric progression with first term $x$ and common ratio $0 . 75$.
> 
> **M1**: Correct use of $S_{\infty} = \frac{a}{1-r}$ with $a = x$ and $r = 0 . 75$ for the bounce heights.
> 
> **M1**: Correct expression for the total distance, $A + 2 \times$ (sum of the bounce heights).
> 
> **A1**: Correct result $A + 8 x$, with the conclusion that the total distance never exceeds it.
State a physical assumption underlying the model

**Final answer:** **The ball only ever moves vertically — it bounces straight up and down, with no horizontal motion**

**[B1]**

> **[mark-scheme]**
> **B1**: Any sensible physical assumption — for example, that the ball moves only vertically, that the height reduction stays exactly `25\%` for every bounce, that air resistance is negligible, or that the ball continues to bounce indefinitely.

### Q7
The tube lengths form a geometric progression: each tube is $0 . 9$ of the one to its left, so the common ratio is $0 . 9$ with first term $a$ (the tallest tube)

Because `|r| < 1`, the total length of all the tubes — however many are cut — cannot exceed the sum to infinity $S_{\infty} = \frac{a}{1-r}$

$S_{\infty} = \frac{a}{1-0.9}$

**[M1]**

$S_{\infty} = \frac{a}{0.1} = 10 a$

**Final answer:** **The total length never exceeds **$10 a$**, so the longer tube need not be longer than ten times the height of the tallest tube, as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $S_{\infty} = \frac{a}{1-r}$ with $r = 0 . 9$, identifying the tube lengths as a geometric progression.
> 
> **A1**: Correct value $10 a$, with the conclusion that, since any finite number of tubes sums to less than $10 a$, the longer tube need not exceed ten times the height of the tallest tube.
The tube lengths form an arithmetic progression with first term $a$ and common difference $- 1$ (each $1$ cm shorter); all of the longer tube, of length $10 a$, is used, so the sum of the $n$ tubes equals $10 a$

`\dfrac{n}{2}\left(2a + (n - 1)(-1)\right) = 10a`

**[M1]**

Multiply both sides by $2$ and expand

$n ( 2 a - n + 1 ) = 20 a \Rightarrow 2 a n - n^{2} + n = 20 a$

**[M1]**

Rearrange so that the coefficient of $n^{2}$ is positive

**Final answer:** $n^{2} - ( 2 a + 1 ) n + 20 a = 0$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)` with first term $a$ and common difference $d = - 1$, set equal to $10 a$.
> 
> **M1**: Correct expansion and rearrangement (e.g. $n ( 2 a - n + 1 ) = 20 a$ or $2 a n - n^{2} + n = 20 a$).
> 
> **A1**: Correct rearrangement to the printed quadratic $n^{2} - ( 2 a + 1 ) n + 20 a = 0$, with clear working.

### Q8
The common difference is the second term minus the first term; set this equal to $- 6$

$x^{2} - ( - 7 x ) = - 6$

$x^{2} + 7 x + 6 = 0$

**[M1]**

Factorise the quadratic to find the possible values of $x$

$( x + 1 ) ( x + 6 ) = 0$

**[M1]**

**Final answer:** $x = - 1$** or **$x = - 6$

**[A1]**

Find the fifth term $u_{5} = a + 4 d = - 7 x - 24$ for each value of $x$

When $x = - 1$

$u_{5} = - 7 ( - 1 ) - 24 = - 17$

When $x = - 6$

$u_{5} = - 7 ( - 6 ) - 24 = 18$

**Final answer:** $u_{5} = - 17$** (when **$x = - 1$**), **$u_{5} = 18$** (when **$x = - 6$**)**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct formation of the common difference $x^{2} + 7 x$, set equal to $- 6$, reaching a three-term quadratic.
> 
> **M1**: Correct method to solve the quadratic (factorising, formula or completing the square).
> 
> **A1**: Both values $x = - 1$ and $x = - 6$.
> 
> **A1**: Both corresponding fifth terms, $- 17$ (when $x = - 1$) and $18$ (when $x = - 6$).
The common ratio is the second term divided by the first

$r = \frac{x^{2}}{-7x} = - \frac{x}{7}$

Substitute $a = - 7 x$ and $r = - \frac{x}{7}$ into the sum to infinity $\frac{a}{1-r} = - 14$

$\frac{-7x}{1+\frac{x}{7}} = - 14$

**[M1]**

Multiply out and solve for $x$

$- 7 x = - 14 - 2 x \Rightarrow - 5 x = - 14$

$x = 2 . 8$

**[A1]**

The ratio $r = - 0 . 4$ satisfies `|r| < 1`, so evaluate the third term $u_{3} = a r^{2}$

$u_{3} = - 19 . 6 \times ( - 0 . 4 )^{2} = - 19 . 6 \times 0 . 16$

**[M1]**

**Final answer:** $u_{3} = - \frac{392}{125}$** (−3.14 to 3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct statement of $r = - \frac{x}{7}$, with $a = - 7 x$ substituted into $\frac{a}{1-r} = - 14$.
> 
> **A1**: $x = 2 . 8$ (or $\frac{14}{5}$).
> 
> **M1**: Correct substitution of your $x$ into $u_{3} = a r^{2}$ (your $r$ must satisfy `|r| < 1`).
> 
> **A1**: Third term $- \frac{392}{125}$ (accept $- 3 . 14$ or $- 3 . 136$).

### Q9
To find the amount at the end of the first year, increase the \$400 deposit by 3%, which multiplies it by $1 . 03$

$400 \times 1 . 03 = 412$

**Final answer:** **Amount at the end of year 1 = \$412 as required**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct calculation $400 \times 1 . 03$ (or $400 + 400 \times 0 . 03$) reaching \$412.
This \$400 is in the account for one year, so it earns a single year of interest at 3%

$400 \times 0 . 03 = 12$

**Final answer:** **\$12**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct interest of \$12.
The first \$400 stays in the account for two years, so it is multiplied by $1 . 03$ in each of those years

$( 400 \times 1 . 03 ) \times 1 . 03$

**[B1]**

The \$400 added at the start of the second year earns interest for one year only, so adding the two contributions gives the amount at the end of the second year

$400 \times 1 . 03$

**Final answer:** $( 400 \times 1 . 03 ) \times 1 . 03 + 400 \times 1 . 03$** as required**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct explanation that the first \$400 is multiplied by $1 . 03$ twice (interest for two years), giving $( 400 \times 1 . 03 ) \times 1 . 03$.
> 
> **B1**: Correct explanation that the second \$400 (added at the start of year 2) is multiplied by $1 . 03$ once, and that the two contributions are added.
Extending the pattern from part (c), each year's \$400 deposit compounds until the end of year $n$: the deposit at the start of year 1 grows for $n$ years, down to the deposit at the start of year $n$, which grows for one year

$400 \times 1 . 03^{n} + 400 \times 1 . 03^{n-1} + \dots + 400 \times 1 . 03$

**[M1]**

Take out the common factor of 400 and list the powers in increasing order to reach the printed form

**Final answer:** `400\left(1.03 + 1.03^2 + 1.03^3 + \ldots + 1.03^n\right)`** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct pattern of contributions — each year's \$400 deposit compounding to the end of year $n$, giving the powers $1 . 03^{n}$ down to $1 . 03$.
> 
> **A1**: Correct factorisation of 400 to reach the printed series.
This is a geometric progression with first term $a = 1 . 03$ and common ratio $r = 1 . 03$, so use `S_n = \dfrac{a\left(r^n - 1\right)}{r - 1}`

`S_n = \dfrac{1.03\left(1.03^n - 1\right)}{1.03 - 1}`

**[M1]**

Simplify the denominator, using $\frac{1.03}{0.03} = \frac{103}{3}$, to reach the printed form

**Final answer:** `S_n = \dfrac{103}{3}\left(1.03^n - 1\right)`** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of `S_n = \dfrac{a\left(r^n - 1\right)}{r - 1}` with $a = 1 . 03$, $r = 1 . 03$ and $n$ terms.
> 
> **A1**: Correct simplification of $\frac{1.03}{0.03}$ to $\frac{103}{3}$, reaching the printed result.
Combining parts (d) and (e), the amount after $n$ years is `400 \times \dfrac{103}{3}\left(1.03^n - 1\right)`; to find the amount after 12 years, substitute $n = 12$

`400 \times \dfrac{103}{3}\left(1.03^{12} - 1\right)`

**[M1]**

Evaluate, keeping full accuracy until the final rounding

`= 400 \times \dfrac{103}{3}\left(0.425760\ldots\right) = 5847.116\ldots`

**Final answer:** **\$5847.12 (to the nearest cent)**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct substitution of $n = 12$ into `400 \times \dfrac{103}{3}\left(1.03^n - 1\right)` (or the series summed and then multiplied by 400).
> 
> **A1**: \$5847.12 (accept \$5850 to 3 significant figures).

### Q10
(i)

The common difference is the second term minus the first term, so set this equal to $14$

$x^{2} - 5 x = 14$

**Final answer:** $x^{2} - 5 x - 14 = 0$** as required**

**[B1]**

(ii)

Factorise the quadratic to find the possible values of $x$

$( x - 7 ) ( x + 2 ) = 0$

**[M1]**

**Final answer:** $x = 7$** or **$x = - 2$

**[A1]**

Each value of $x$ gives its own progression, so find the third term $u_{3} = a + 2 d = 5 x + 28$ for each

When $x = 7$

$u_{3} = 5 ( 7 ) + 28 = 63$

When $x = - 2$

$u_{3} = 5 ( - 2 ) + 28 = 18$

**Final answer:** $u_{3} = 63$** (when **$x = 7$**), **$u_{3} = 18$** (when **$x = - 2$**)**

**[A1]**

> **[mark-scheme]**
> **B1**: Correct formation of the common difference $x^{2} - 5 x$, set equal to $14$, reaching the printed equation.
> 
> **M1**: Correct method to solve the three-term quadratic (factorising, formula or completing the square).
> 
> **A1**: Both values $x = 7$ and $x = - 2$.
> 
> **A1**: Both corresponding third terms, $63$ (when $x = 7$) and $18$ (when $x = - 2$).
(i)

Consider what happens to the first term when $x = 0$

**Final answer:** **If **$x = 0$** the first term **$5 x = 0$**, so every term is zero and the sum to infinity would be 0, not 10**

**[B1]**

(ii)

The common ratio is the second term divided by the first

$r = \frac{x^{2}}{5x} = \frac{x}{5}$

Substitute $a = 5 x$ and $r = \frac{x}{5}$ into the sum to infinity $\frac{a}{1-r} = 10$

**Final answer:** $\frac{5x}{1-\frac{x}{5}} = 10$** as required**

**[B1]**

(iii)

Multiply out and collect terms to solve the equation for $x$

`5x = 10\left(1 - \dfrac{x}{5}\right) = 10 - 2x`

$7 x = 10 \Rightarrow x = \frac{10}{7}$

**[M1]**

This gives $r = \frac{2}{7}$, which satisfies `|r| < 1`, so find the third term $u_{3} = a r^{2}$ with $a = 5 x$ and $r = \frac{x}{5}$

`u_3 = 5x\left(\dfrac{x}{5}\right)^2 = \dfrac{x^3}{5} = \dfrac{(10/7)^3}{5}`

**[M1]**

**Final answer:** $u_{3} = \frac{200}{343}$** (0.583 to 3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: Correct explanation that if $x = 0$ the first term is $0$, so there is no valid geometric progression with sum to infinity $10$ (or that the common ratio is undefined).
> 
> **B1**: Correct statement of $r = \frac{x}{5}$, with $a = 5 x$ and $r$ substituted into $\frac{a}{1-r}$ to reach the printed equation.
> 
> **M1**: Correct method to solve $\frac{5x}{1-\frac{x}{5}} = 10$, obtaining $x = \frac{10}{7}$.
> 
> **M1**: Correct substitution of your $x$ into $u_{3} = a r^{2}$.
> 
> **A1**: Third term $\frac{200}{343}$ (accept $0 . 583$).

### Q11
Model 1 is arithmetic with first term $25000$, and its eighth term is $7500$, so use $u_{8} = a + 7 d$ to form an equation in $d$

$25000 + 7 d = 7500$

**[M1]**

$7 d = - 17500$

$d = - 2500$

**[A1]**

Model 2 is geometric with first term $25000$, and its eighth term is $7500$, so use $u_{8} = a r^{7}$ to form an equation in $r$

$25000 r^{7} = 7500 \Rightarrow r^{7} = 0 . 3$

**[M1]**

Take the seventh root to find the common ratio

$r = 0 . 3^{\frac{1}{7}} = 0 . 8419 \dots$

**Final answer:** $r = 0 . 842$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $u_{8} = a + 7 d$ with $a = 25000$ and $u_{8} = 7500$ for Model 1.
> 
> **A1**: $d = - 2500$.
> 
> **M1**: Correct use of $u_{8} = a r^{7}$ with $a = 25000$ and $u_{8} = 7500$, reaching $r^{7} = 0 . 3$.
> 
> **A1**: $r = 0 . 3^{\frac{1}{7}}$ — answers which round to $0 . 842$.
First find the year in which Model 1 predicts \$5000, using $d = - 2500$ from part (a) in $u_{n} = 25000 + ( n - 1 ) ( - 2500 )$

$25000 + ( n - 1 ) ( - 2500 ) = 5000$

$( n - 1 ) ( - 2500 ) = - 20000 \Rightarrow n - 1 = 8$

$n = 9$

**[M1]**

Now evaluate Model 2 in that same year, using $r = 0 . 3^{\frac{1}{7}}$ from part (a) in $u_{9} = a r^{8}$

`u_9 = 25000 \times \left(0.3^{\frac{1}{7}}\right)^{8} = 25000 \times 0.25259\ldots`

**[M1]**

**Final answer:** **\$6315 (to the nearest dollar)**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method setting Model 1 equal to \$5000 and solving for the year, obtaining $n = 9$.
> 
> **M1**: Correct substitution of $n = 9$ into Model 2, $u_{9} = 25000 r^{8}$ (or $25000 \times 0 . 3^{\frac{8}{7}}$).
> 
> **A1**: \$6315 (accept \$6316 if the rounded $r = 0 . 842$ is used).
Compare what each model predicts once the car is old

**Final answer:** **Model 1 eventually predicts a negative value (it reaches \$0 at 11 years old and is negative after that), whereas Model 2 always stays positive, so Model 2 is more realistic for older cars**

**[B1]**

> **[mark-scheme]**
> **B1**: A valid benefit that refers to the context — for example, that Model 1 eventually predicts an impossible negative value, whereas Model 2 stays positive and only approaches \$0.

### Q12
(i)

Half the new value is 15 000 dollars; set Model A equal to this and solve for $n$

$30000 - 5000 n = 15000$

**[M1]**

$5000 n = 15000$

**Final answer:** $n = 3$** years**

**[A1]**

(ii)

Evaluate Model B at the end of the first and second years and compare each with the halved value of 15 000 dollars

$30000 \times ( 0 . 6 )^{1} = 18000$

$30000 \times ( 0 . 6 )^{2} = 10800$

**[M1]**

Locate the year in which the value passes \$15 000

**Final answer:** **\$18 000 > \$15 000 but \$10 800 < \$15 000, so Model B's value halves during the second year**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct equation setting Model A equal to \$15 000, $30000 - 5000 n = 15000$, solved for $n$.
> 
> **A1**: Age $n = 3$ years.
> 
> **M1**: Correct evaluation of Model B at the ends of years 1 and 2 (\$18 000 and \$10 800), compared with \$15 000.
> 
> **A1**: Correct values together with the conclusion that the value halves during the second year.
Evaluate Model A when $n = 5$

$30000 - 5000 ( 5 ) = 5000$

**[M1]**

Evaluate Model B when $n = 5$

$30000 \times ( 0 . 6 )^{5} = 2332 . 80$

**[M1]**

Compare the two predicted values

**Final answer:** **Model A predicts \$5000 and Model B predicts \$2332.80, so Model A predicts the greater value**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct evaluation of Model A at $n = 5$, giving \$5000.
> 
> **M1**: Correct evaluation of Model B at $n = 5$, giving \$2332.80 (accept \$2330 to 3 significant figures).
> 
> **A1**: Both values correct with the conclusion that Model A predicts the greater value.
(i)

Consider what Model A predicts once the car is old

**Final answer:** **Once the car is more than 6 years old, Model A gives a negative value, but a car cannot have a negative value**

**[B1]**

(ii)

Consider the sign of the geometric term for any $n$

**Final answer:** **A positive number raised to any power stays positive, so Model B's value is always greater than zero and only approaches \$0**

**[B1]**

> **[mark-scheme]**
> **B1**: A valid limitation of Model A that refers to the context — for example, that for $n > 6$ it predicts a negative value, which is impossible for a car. "It just keeps decreasing" is not enough.
> 
> **B1**: A correct reason that $( 0 . 6 )^{n}$ is always positive (a positive number to any power is positive), so $30000 \times ( 0 . 6 )^{n}$ never reaches \$0.

### Q13
For an arithmetic progression the third term is $a + 2 d$; use the given first and third terms to form an equation in $d$

$a + 2 d = 49$

$4 + 2 d = 49$

**[M1]**

Solve for the common difference, then use $u_{2} = a + d$ for the second term

$2 d = 45 \Rightarrow d = 22 . 5$

$u_{2} = 4 + 22 . 5$

$d = 22 . 5 , u_{2} = 26 . 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the arithmetic third-term expression $a + 2 d$ with $a = 4$ and third term $49$ to form an equation in $d$.
> 
> **A1**: Correct common difference $d = 22 . 5$ and second term $26 . 5$ (accept the exact fractions $\frac{45}{2}$ and $\frac{53}{2}$).
For a geometric progression the third term is $a r^{2}$; form an equation in $r^{2}$

$a r^{2} = 49$

$4 r^{2} = 49 \Rightarrow r^{2} = \frac{49}{4}$

**[M1]**

Take both square roots, since nothing in the question fixes the sign of $r$

$r = \pm \frac{7}{2} = \pm 3 . 5$

**[A1]**

Find the second term $u_{2} = a r$ for each ratio

When $r = 3 . 5$

$u_{2} = 4 \times 3 . 5 = 14$

When $r = - 3 . 5$

$u_{2} = 4 \times ( - 3 . 5 ) = - 14$

**Final answer:** $r = 3 . 5 , u_{2} = 14$** or **$r = - 3 . 5 , u_{2} = - 14$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the geometric third-term expression $a r^{2}$ with $a = 4$ and third term $49$ to form an equation in $r^{2}$ (e.g. $4 r^{2} = 49$).
> 
> **A1**: Both common ratios $r = \pm 3 . 5$ (accept $\pm \frac{7}{2}$).
> 
> **A1**: Both second terms correctly paired — $14$ with $r = 3 . 5$, and $- 14$ with $r = - 3 . 5$. Giving only the positive case scores this mark as $0$.

### Q14
The first-bounce height is the first term ($n = 1$) and the common ratio is the multiplier in the formula

$u_{1} = 2 \times ( 0 . 8 )^{0} = 2$

**Final answer:** $u_{1} = 2$** m, ratio **$r = 0 . 8$

**[B1]**

To find the fifth-bounce height, substitute $n = 5$ into the formula

$u_{5} = 2 \times ( 0 . 8 )^{4}$

**[M1]**

$u_{5} = 2 \times 0 . 4096 = 0 . 8192$

**Final answer:** $u_{5} = 0 . 819$** m (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **B1**: First-bounce height $2$ m and common ratio $0 . 8$ both stated.
> 
> **M1**: Correct substitution of $n = 5$ into the $n$th-term formula (or use of $a r^{4}$), i.e. $2 \times ( 0 . 8 )^{4}$.
> 
> **A1**: Height $0 . 819$ m — answers which round to $0 . 819$ (accept the exact $0 . 8192$ m).
(i)

The bounce heights form a geometric progression with $a = 2$ and $r = 0 . 8$; to sum the first 10 terms use `S_n = \dfrac{a\left(1 - r^n\right)}{1 - r}`

`S_{10} = \dfrac{2\left(1 - 0.8^{10}\right)}{1 - 0.8}`

**[M1]**

`S_{10} = \dfrac{2\left(1 - 0.10737\ldots\right)}{0.2} = 8.9262\ldots`

**Final answer:** $S_{10} = 8 . 93$** m (3 s.f.)**

**[A1]**

(ii)

Consider the motion the ball makes during each bounce

**Final answer:** **On each bounce the ball rises to the modelled height and then falls back through the same distance, so every bounce height is travelled twice — once up and once down — making the total distance twice the sum of the heights**

**[B1]**

> **[mark-scheme]**
> **M1**: Correct use of `S_n = \dfrac{a\left(1 - r^n\right)}{1 - r}` with $a = 2$, $r = 0 . 8$ and $n = 10$.
> 
> **A1**: Sum $8 . 93$ m — answers which round to $8 . 93$ (accept $8 . 926 \dots$).
> 
> **B1**: A clear explanation that each bounce height is travelled twice — once upward to the peak and once downward back to the floor — so the total vertical distance is twice the sum in part (i). "Because it goes up and down" alone is not enough.

### Q15
To find the first three distances, substitute $n = 1$, $n = 2$ and $n = 3$ into the formula

$u_{1} = 4 ( 1 ) - 1 = 3$

$u_{2} = 4 ( 2 ) - 1 = 7$

$u_{3} = 4 ( 3 ) - 1 = 11$

**Final answer:** $u_{1} = 3 , u_{2} = 7 , u_{3} = 11$** miles**

**[B1 B1]**

> **[mark-scheme]**
> **B1**: At least two of the three distances correct.
> 
> **B1**: All three distances correct — $u_{1} = 3$, $u_{2} = 7$, $u_{3} = 11$ miles.
To find the distance in the tenth week, substitute $n = 10$ into the formula

$u_{10} = 4 ( 10 ) - 1$

**Final answer:** $u_{10} = 39$** miles**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct distance of $39$ miles.
The weekly distances form an arithmetic progression with first term $a = 3$ and common difference $d = 4$; to find the total, use `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)` with $n = 10$

`S_{10} = \dfrac{10}{2}\left(2(3) + (10 - 1)(4)\right)`

**[M1]**

Evaluate to obtain the total distance

$S_{10} = 5 ( 6 + 36 ) = 5 \times 42$

**Final answer:** $S_{10} = 210$** miles**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)` with $a = 3$, $d = 4$ and $n = 10$ (or $S_{n} = \frac{n}{2} ( a + l )$ with $a = 3$ and $l = 39$).
> 
> **A1**: Correct total of $210$ miles.
Interpret the behaviour of the formula as the number of weeks increases

**Final answer:** **The weekly distance increases without limit as the number of weeks increases, so the model eventually predicts a weekly mileage far greater than a person could realistically run**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct explanation that refers to the context — for example, that the weekly distance increases without limit, so the predicted mileage eventually exceeds what a person could physically run. A vague statement such as "the formula stops working" is not enough.

### Q16
The laps completed each day form an arithmetic progression with first term $5$ and common difference $3$; use the $n$th-term formula $a + ( n - 1 ) d$

$u_{n} = 5 + ( n - 1 ) ( 3 )$

$u_{n} = 3 n + 2$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct formula for $u_{n}$, e.g. $3 n + 2$ or $5 + 3 ( n - 1 )$.
To find the laps on the tenth day, substitute $n = 10$ into the formula

$u_{10} = 5 + ( 10 - 1 ) ( 3 ) = 5 + 27$

**[M1]**

**Final answer:** $u_{10} = 32$** laps**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct substitution of $n = 10$ into the formula (or use of $a + 9 d$ with $a = 5$, $d = 3$).
> 
> **A1**: $32$ laps.
(i)

To find the total number of laps, sum the first 14 terms using `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)` with $a = 5$, $d = 3$ and $n = 14$

`S_{14} = \dfrac{14}{2}\left(2(5) + (14 - 1)(3)\right)`

**[M1]**

$S_{14} = 7 ( 10 + 39 ) = 7 \times 49$

**Final answer:** $S_{14} = 343$** laps**

**[A1]**

(ii)

Each lap is $600$ m, so multiply the total number of laps by $600$ to get the distance in metres

$343 \times 600 = 205800$

**[M1]**

Convert the distance to kilometres

$205800 \text{m} = 205 . 8 \text{km}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)` with $a = 5$, $d = 3$ and $n = 14$.
> 
> **A1**: $343$ laps.
> 
> **M1**: Correct multiplication of the total number of laps by $600$ m (or by $0 . 6$ km).
> 
> **A1**: $205 . 8$ km (accept $205800$ m, or $206$ km to 3 significant figures).

### Q17
The weekly amounts 1, 2, 3, … dollars form an arithmetic progression with first term $a = 1$ and common difference $d = 1$; to find the total, use `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)` with $n = 10$

`S_{10} = \dfrac{10}{2}\left(2(1) + (10 - 1)(1)\right)`

**[M1]**

Evaluate the sum

$S_{10} = 5 \times 11 = 55$

**Final answer:** **Total saved after 10 weeks = \$55**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)` with $a = 1$, $d = 1$ and $n = 10$ (or equivalent, e.g. pairing $1 + 2 + \dots + 10$).
> 
> **A1**: Correct total of \$55.
Using the same progression, apply `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)` with $a = 1$ and $d = 1$, leaving the answer in terms of $n$

`S_n = \dfrac{n}{2}\left(2(1) + (n - 1)(1)\right)`

**[M1]**

Simplify the bracket to reach the required form

$S_{n} = \frac{n}{2} ( 2 + n - 1 ) = \frac{n}{2} ( n + 1 )$

**Final answer:** $S_{n} = \frac{n}{2} ( n + 1 )$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)` with $a = 1$ and $d = 1$, written in terms of $n$.
> 
> **A1**: Correct simplification to the printed result $\frac{n}{2} ( n + 1 )$, showing the $\frac{n}{2} ( 2 + n - 1 )$ step. Jumping straight to the printed answer does not score.
Use the result from part (b), $S_{n} = \frac{n}{2} ( n + 1 )$, with $n = 20$ to find the total saved

$S_{20} = \frac{20}{2} ( 20 + 1 ) = 10 \times 21$

**[M1]**

Compare the total with the \$250 cost

$S_{20} = 210$

**Final answer:** **\$210 < \$250, so Bernie will not have saved enough**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct evaluation of the total saved after 20 weeks, $S_{20} = 210$ (using part (b) or `S_n = \dfrac{n}{2}\left(2a + (n - 1)d\right)`).
> 
> **A1**: Correct value \$210 together with a clear comparison to \$250 and the conclusion that he has not saved enough.
Interpret how the required weekly payment changes over time

**Final answer:** **The amount Bernie must add increases every week, so the weekly payments soon become large and difficult to sustain**

**[B1]**

> **[mark-scheme]**
> **B1**: A sensible reason that refers to the context — for example, that the required weekly payment keeps increasing and becomes unaffordable, or that saving a fixed larger amount each week would reach \$250 sooner. A vague statement such as "it is not a good way to save" does not score.
