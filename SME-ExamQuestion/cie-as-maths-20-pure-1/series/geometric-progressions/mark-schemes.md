# Mark Schemes — Geometric Progressions
**Series** · Cambridge (CIE) AS maths (9709)


## Exam Questions (30 questions)


### Q1
Write both sides of the given relationship using the formula for the $n$th term of a geometric progression, $u_{n} = a r^{n-1}$

$a r^{n+3} = 9 a r^{n-1}$

**[M1]**

Divide both sides by $a r^{n-1}$, valid since neither $a$ nor $r$ can be zero, and subtract the indices

$r^{(n+3)-(n-1)} = 9 \Rightarrow r^{4} = 9$

Take the fourth root, which gives two real values

$r = \sqrt{3}$* or *$r = - \sqrt{3}$

A negative ratio would make the terms alternate in sign, but the question states they are all positive, so reject the negative root

$r = \sqrt{3}$

**[M1]**

Use the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$, with $r = \sqrt{3}$ and $n = 12$

`S_{12} = \dfrac{a\left(1-\left(\sqrt{3}\right)^{12}\right)}{1-\sqrt{3}}`

Simplify the surd power using index laws, since a square root is a power of $\frac{1}{2}$

`\left(\sqrt{3}\right)^{12} = \left(3^{\frac{1}{2}}\right)^{12} = 3^{6} = 729`

Substitute that back, and evaluate the numerator

`S_{12} = \dfrac{a\left(1-729\right)}{1-\sqrt{3}} = \dfrac{-728a}{1-\sqrt{3}}`

Rationalise the denominator by multiplying top and bottom by $1 + \sqrt{3}$

`S_{12} = \dfrac{-728a\left(1+\sqrt{3}\right)}{\left(1-\sqrt{3}\right)\left(1+\sqrt{3}\right)} = \dfrac{-728a\left(1+\sqrt{3}\right)}{-2}`

**[M1]**

Divide, the two negatives cancel, giving a positive integer coefficient as required

**Final answer:** `S_{12} = 364a\left(\sqrt{3}+1\right)`** as required, with **$k = 364 ,  n = 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $u_{n} = a r^{n-1}$ on both sides of the given relationship, forming $a r^{n+3} = 9 a r^{n-1}$ or equivalent.
> 
> **M1**: Correct reduction to $r^{4} = 9$ and correct selection of $r = \sqrt{3}$. The fourth root gives $r = \pm \sqrt{3}$; the negative value must be rejected, because a negative common ratio would make the terms alternate in sign and the question states they are all positive. Accept $r^{2} = 3$ as an intermediate step.
> 
> **M1**: Correct use of the sum formula with $n = 12$, the surd power simplified as $( \sqrt{3} )^{12} = 3^{6} = 729$, and a correct method to rationalise the denominator. Writing $( \sqrt{3} )^{12}$ as $3^{12}$ is the common slip.
> 
> **A1**: Correct printed form $S_{12} = 364 a ( \sqrt{3} + 1 )$, with both $k = 364$ and $n = 3$ stated. The question asks for positive integers, so both values must appear. Because the answer is given, the rationalising step must be seen.

### Q2
Substitute $k = 1$ into the given formula to find the first term of the geometric progression, and read off the common ratio

$a = ( - 2 )^{0} = 1$

$r = - 2$

**[M1]**

Each $v_{k}$ is a term of the progression plus a fixed $\sqrt{13}$, so the sequence $v_{k}$ is not itself geometric, split the sum into the geometric part and the constant part

`\sum_{k=11}^{23} v_{k} = \sum_{k=11}^{23} u_{k} + 13\sqrt{13}`

There are $23 - 11 + 1 = 13$ terms in the run, which is where the $13 \sqrt{13}$ comes from

**[M1]**

For the geometric part, take the first 23 terms and remove the first 10, that leaves terms 11 to 23, keeping the eleventh

`\sum_{k=11}^{23} u_{k} = S_{23} - S_{10}`

**[M1]**

Use the formula in the form $S_{n} = \frac{a(r^{n}-1)}{r-1}$ with $a = 1$ and $r = - 2$

$S_{23} - S_{10} = \frac{(-2)^{23}-1}{-3} - \frac{(-2)^{10}-1}{-3}$

Evaluate each, noting that $( - 2 )^{23}$ is negative because 23 is odd, while $( - 2 )^{10}$ is positive

$S_{23} - S_{10} = 2796203 - ( - 341 )$

`\sum_{k=11}^{23} u_{k} = 2796544`

**[A1]**

Add the 13 lots of $\sqrt{13}$, the surd cannot be combined with the integer, so the exact answer keeps both parts

$2796544 + 13 \sqrt{13}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct first term $a = 1$ and common ratio $r = - 2$. Note $u_{1} = ( - 2 )^{0} = 1$, not $- 2$.
> 
> **M1**: Correct method to split the sum, recognising that $v_{k}$ is a geometric progression plus a constant, so the sum is the sum of the $u_{k}$ terms plus $13 \sqrt{13}$. There are $23 - 11 + 1 = 13$ terms in the run; using 12 is the common slip. No geometric sum formula may be applied to $v_{k}$ directly, because $v_{k}$ is not a geometric progression.
> 
> **M1**: Correct structure $S_{23} - S_{10}$ for the sum of terms 11 to 23. Subtracting $S_{11}$ instead is the common slip, the eleventh term must be kept.
> 
> **A1**: Correct geometric sum $2796544$.
> 
> **A1**: Correct exact answer $2796544 + 13 \sqrt{13}$. The question asks for an exact value, so the surd must be left in, a decimal such as $2796591 . 9$ does not earn this mark. The order of the two terms does not matter.

### Q3
A geometric progression converges only when its common ratio lies strictly between $- 1$ and 1

$- 1 < r < 1$

**[B1]**

Find the common ratio by dividing the third term by the second, the numerator is a difference of two squares, so it factorises and the $( x - 1 )$ cancels

$r = \frac{x^{2}-1}{x-1} = \frac{(x-1)(x+1)}{x-1}$

**[M1]**

$r = x + 1$

**[A1]**

Substitute into the convergence condition

$- 1 < x + 1 < 1$

Subtract 1 from every part

$- 2 < x < 0$

**[M1]**

The question excludes $x = - 1$, which sits inside this range, so it must be cut out, leaving two separate intervals

**Final answer:** $- 2 < x < - 1$** or **$- 1 < x < 0$

**[A1]**

> **[mark-scheme]**
> **B1**: The correct condition for convergence, $- 1 < r < 1$, or the equivalent `|r| < 1`.
> 
> **M1**: Correct method to find the common ratio, dividing the third term by the second and factorising $x^{2} - 1$ as $( x - 1 ) ( x + 1 )$ so the $( x - 1 )$ cancels.
> 
> **A1**: Correct common ratio $r = x + 1$.
> 
> **M1**: Correct substitution into the convergence condition and rearrangement to $- 2 < x < 0$.
> 
> **A1**: The range with $x = - 1$ excluded: $- 2 < x < - 1$ or $- 1 < x < 0$. The unqualified $- 2 < x < 0$ does not earn this mark. The question rules out $x = - 1$, and it has to, because $x = - 1$ would give $r = 0$, which does not define a geometric progression. Interval notation is also accepted.
Only the second term is given, so work back to the first term by dividing it by the common ratio from part (a)

$a = \frac{u_{2}}{r} = \frac{x-1}{x+1}$

**[M1]**

Substitute into the formula for the sum to infinity of a convergent geometric progression, $S_{\infty} = \frac{a}{1-r}$ and set it equal to $- 6$, the denominator simplifies, since $1 - ( x + 1 ) = - x$

$- 6 = \frac{x-1}{(x+1)(-x)} = \frac{x-1}{-x^{2}-x}$

**[M1]**

Multiply both sides by the denominator and collect every term on one side

$6 x^{2} + 6 x = x - 1 \Rightarrow 6 x^{2} + 5 x + 1 = 0$

**[M1]**

Factorise and solve

$( 3 x + 1 ) ( 2 x + 1 ) = 0$

**Final answer:** $x = - \frac{1}{3}$** or **$x = - \frac{1}{2}$

**[A1]**

Both values lie in the range found in part (a), so both are valid

> **[mark-scheme]**
> **M1**: Correct method to find the first term, dividing the given second term by the common ratio, $a = \frac{x-1}{x+1}$. Taking $a = x - 1$ is the common slip: $x - 1$ is the second term, not the first.
> 
> **M1**: Correct substitution into $S_{\infty} = \frac{a}{1-r}$ with the expression set equal to $- 6$, simplifying the denominator using $1 - ( x + 1 ) = - x$.
> 
> **M1**: Correct rearrangement to the quadratic $6 x^{2} + 5 x + 1 = 0$.
> 
> **A1**: Both values, $x = - \frac{1}{3}$ and $x = - \frac{1}{2}$. Both are needed. As a check, both lie within the range found in part (a), neither is $- 1$, and both are between $- 1$ and 0, so neither is rejected. Accept the decimals $- 0 . 5$ and answers which round to $- 0 . 333$.

### Q4
In a geometric progression the ratio of consecutive terms is constant, so the second term divided by the first equals the third divided by the second

$\frac{k}{2k+6} = \frac{k-4}{k}$

**[M1]**

Cross-multiply, then expand the right-hand side

$k^{2} = ( 2 k + 6 ) ( k - 4 ) = 2 k^{2} - 8 k + 6 k - 24$

Collect every term on one side

$k^{2} - 2 k - 24 = 0$

**[M1]**

Factorise the quadratic, two numbers multiplying to $- 24$ and adding to $- 2$ are $- 6$ and $4$

$( k - 6 ) ( k + 4 ) = 0$

**[M1]**

Solve, the question places no restriction on $k$, so both values are possible

**Final answer:** $k = 6$** or **$k = - 4$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the constant-ratio property to form $\frac{k}{2k+6} = \frac{k-4}{k}$. The equivalent $k^{2} = ( 2 k + 6 ) ( k - 4 )$ is also acceptable, since the syllabus states that $a$, $b$, $c$ are in geometric progression if $b^{2} = a c$ (or equivalent).
> 
> **M1**: Correct expansion and rearrangement to $k^{2} - 2 k - 24 = 0$.
> 
> **M1**: Correct factorisation $( k - 6 ) ( k + 4 ) = 0$, or correct use of the quadratic formula.
> 
> **A1**: Both values, $k = 6$ and $k = - 4$. Both are needed, unlike similar questions, this one places no condition on $k$, so neither value can be rejected at this stage. Rejecting one here loses the mark.
A geometric progression converges, and so has a sum to infinity, only when its common ratio lies strictly between $- 1$ and 1, so this condition will decide which value of $k$ applies

$- 1 < r < 1$

**[B1]**

Test $k = - 4$ by finding the common ratio it gives

$r = \frac{k}{2k+6} = \frac{-4}{2(-4)+6} = 2$

This lies outside the range, so that progression diverges and $k = - 4$ must be rejected

**[M1]**

Test $k = 6$ in the same way

$r = \frac{6}{2(6)+6} = \frac{1}{3}$

This lies inside the range, so $k = 6$ is the value that applies, now find the first term

$a = 2 k + 6 = 18$

**[M1]**

Use the formula for the sum to infinity of a convergent geometric progression, $S_{\infty} = \frac{a}{1-r}$

$S_{\infty} = \frac{18}{1-\frac{1}{3}}$

$S_{\infty} = 27$

**[A1]**

> **[mark-scheme]**
> **B1**: The correct condition for convergence, $- 1 < r < 1$, or the equivalent `|r| < 1`.
> 
> **M1**: Correct common ratio $r = 2$ for $k = - 4$, together with the conclusion that it is rejected because `|2| > 1`. The progression $- 2 , - 4 , - 8 , \dots$ diverges, so it has no sum to infinity.
> 
> **M1**: Correct common ratio $r = \frac{1}{3}$ and first term $a = 18$ for $k = 6$. Note the first term is the bracket $2 k + 6 = 18$, not $k = 6$.
> 
> **A1**: Correct sum to infinity $S_{\infty} = 27$. Both values of $k$ must be tested for full credit, the question gives no direct constraint on $k$, so it is the convergence condition itself that selects $k = 6$.

### Q5
Write the sum of the first four terms using the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$

$S_{4} = \frac{a(1-r^{4})}{1-r} = 27 . 2$

Write the sum of the first eight terms in the same way

$S_{8} = \frac{a(1-r^{8})}{1-r} = 164 . 9$

Divide $S_{8}$ by $S_{4}$. Both the $a$ and the $( 1 - r )$ cancel

$\frac{S_{8}}{S_{4}} = \frac{1-r^{8}}{1-r^{4}} = \frac{164.9}{27.2}$

**[M1]**

The numerator is a difference of two squares, since $1 - r^{8} = ( 1 - r^{4} ) ( 1 + r^{4} )$. Factorising it exposes a common factor with the denominator

$\frac{(1-r^{4})(1+r^{4})}{1-r^{4}} = 1 + r^{4}$

**[M1]**

Simplify the numerical fraction: multiplying top and bottom by 10 gives $\frac{1649}{272}$, and both share a factor of 17. Then rearrange

$1 + r^{4} = \frac{97}{16} \Rightarrow 16 r^{4} = 81$

Take the fourth root, remembering that an even root has both a positive and a negative value

$r = \pm \frac{3}{2}$

**[A1]**

To choose between them, rearrange the first equation to make $a$ the subject

$a = \frac{27.2(1-r)}{1-r^{4}}$

Both roots give $r^{4} = \frac{81}{16} > 1$, so the denominator $1 - r^{4}$ is negative either way. Therefore, for $a$ to be positive, the numerator must be negative too

$1 - r < 0 \Rightarrow r > 1$

**[M1]**

Only one of the two roots is greater than 1

$r = \frac{3}{2}$

**[A1]**

> **[mark-scheme]**
> **M1**: Both sums written correctly using $S_{n} = \frac{a(1-r^{n})}{1-r}$, and one divided by the other so that $a$ and $( 1 - r )$ cancel, giving $\frac{1-r^{8}}{1-r^{4}} = \frac{164.9}{27.2}$.
> 
> **M1**: Correct use of the difference of two squares to factorise $1 - r^{8}$ as $( 1 - r^{4} ) ( 1 + r^{4} )$, leaving $1 + r^{4}$.
> 
> **A1**: Both values $r = \pm \frac{3}{2}$. The numerical step is $\frac{164.9}{27.2} = \frac{1649}{272} = \frac{97}{16}$, cancelling the common factor of 17. Accept $\pm 1 . 5$.
> 
> **M1**: A correct argument using the sign of the first term to choose between the roots. Since $r^{4} = \frac{81}{16} > 1$ for both values, the denominator of $a = \frac{27.2(1-r)}{1-r^{4}}$ is negative in either case, so $a > 0$ requires $1 - r < 0$. Substituting each root and evaluating $a$ is equally acceptable: $r = \frac{3}{2}$ gives $a \approx 3 . 35 > 0$, while $r = - \frac{3}{2}$ gives $a \approx - 16 . 7 < 0$.
> 
> **A1**: Correct common ratio $r = \frac{3}{2}$. Giving both values, or selecting $- \frac{3}{2}$, does not earn this mark, because the question's condition that the first term is positive exists precisely to rule one of them out.

### Q6
Write the first few terms of $S$ using $u_{n} = a r^{n-1}$, then square each one to get the terms of $T$

$T = a^{2} + a^{2} r^{2} + a^{2} r^{4} + \dots$

**[M1]**

Divide consecutive terms of $T$ to test whether the ratio is constant

$\frac{a^{2}r^{2}}{a^{2}} = \frac{a^{2}r^{4}}{a^{2}r^{2}} = r^{2}$

The ratio is the same constant every time, so $T$ is a geometric progression with first term $a^{2}$ and common ratio $r^{2}$

**[M1]**

The sum to infinity of $S$ exists, so its common ratio satisfies $- 1 < r < 1$, squaring a number of magnitude less than 1 gives a smaller, non-negative result

`|r| < 1 \Rightarrow r^{2} < 1`

**[M1]**

The common ratio of $T$ therefore also lies strictly between $- 1$ and 1, which is exactly the condition for its sum to infinity to exist

**Final answer:** $0 \leq r^{2} < 1$**, so **$T$** converges and **$T_{\infty}$** exists, as required**

**[A1]**

> **[mark-scheme]**
> **M1**: The terms of $T$ written correctly by squaring the terms of $S$, giving $a^{2}$, $a^{2} r^{2}$, $a^{2} r^{4}$, … or equivalent.
> 
> **M1**: Correct demonstration that the ratio of consecutive terms of $T$ is the constant $r^{2}$, concluding that $T$ is a geometric progression with first term $a^{2}$ and common ratio $r^{2}$.
> 
> **M1**: Correct use of the fact that $S_{\infty}$ exists, so `|r| < 1`, to deduce $r^{2} < 1$.
> 
> **A1**: A correct conclusion that $T_{\infty}$ exists, because the common ratio of $T$ satisfies the convergence condition. Note $r^{2}$ cannot be negative, so the condition $- 1 < r^{2} < 1$ reduces to $r^{2} < 1$.
Use the formula for the sum to infinity of a convergent geometric progression, $S_{\infty} = \frac{a}{1-r}$ on the progression $T$, whose first term is $a^{2}$ and common ratio $r^{2}$

$T_{\infty} = \frac{a^{2}}{1-r^{2}}$

**[M1]**

Divide by $S_{\infty}$, dividing by a fraction multiplies by its reciprocal

$\frac{T_{\infty}}{S_{\infty}} = \frac{a^{2}}{1-r^{2}} \times \frac{1-r}{a}$

**[M1]**

The denominator is a difference of two squares, so $1 - r^{2} = ( 1 - r ) ( 1 + r )$, the $( 1 - r )$ cancels, and one factor of $a$ cancels too

$\frac{T_{\infty}}{S_{\infty}} = \frac{a}{1+r}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct sum to infinity of $T$, $T_{\infty} = \frac{a^{2}}{1-r^{2}}$, using the first term and common ratio found in part (a).
> 
> **M1**: Correct method to form the ratio $\frac{T_{\infty}}{S_{\infty}}$, dividing by $\frac{a}{1-r}$, or equivalently multiplying by $\frac{1-r}{a}$.
> 
> **A1**: Correct simplified ratio $\frac{a}{1+r}$. The key step is factorising $1 - r^{2}$ as $( 1 - r ) ( 1 + r )$ so the $( 1 - r )$ cancels. An unsimplified answer such as $\frac{a^{2}(1-r)}{a(1-r^{2})}$ does not earn this mark, the question asks for it simplified as far as possible.
If the two sums to infinity are equal, their ratio is 1, so set the answer to part (b) equal to 1

$\frac{a}{1+r} = 1 \Rightarrow a = 1 + r$

Substitute this into $u_{n} = a r^{n-1}$ to get a formula for any term in terms of $r$ alone

$u_{n} = ( 1 + r ) r^{n-1}$

**[M1]**

Take the left-hand side first, square the $k$th term, doubling its index

`\text{LHS} = u_{k}^{2} = \left((1+r)r^{k-1}\right)^{2} = (1+r)^{2}r^{2k-2}`

**[M1]**

Now build the right-hand side by substituting $n = 2 k - 1$ and $n = 2 k$ in turn

$\text{RHS} = ( 1 + r ) r^{2k-2} + ( 1 + r ) r^{2k-1}$

**[M1]**

Factor out the common $( 1 + r ) r^{2k-2}$, the second term carries one extra factor of $r$

$\text{RHS} = ( 1 + r ) r^{2k-2} ( 1 + r )$

**[M1]**

Collect the two brackets, and the right-hand side matches the left

**Final answer:** $\text{RHS} = ( 1 + r )^{2} r^{2k-2} = \text{LHS}$** as required**

**[A1]**

Reading the identity across the two progressions: the $k$th term of $T$ is $u_{k}^{2}$, and this says it equals a pair of consecutive terms of $S$, so $u_{1}^{2} = u_{1} + u_{2}$, $u_{2}^{2} = u_{3} + u_{4}$, and so on

**Final answer:** **Each term of **$T$** is equal to the sum of a corresponding pair of consecutive terms of **$S$

**[B1]**

> **[mark-scheme]**
> **M1**: Correct deduction that $T_{\infty} = S_{\infty}$ makes the ratio from part (b) equal to 1, giving $a = 1 + r$, and hence the general term $u_{n} = ( 1 + r ) r^{n-1}$.
> 
> **M1**: Correct left-hand side, $u_{k}^{2} = ( 1 + r )^{2} r^{2k-2}$. Squaring $r^{k-1}$ gives $r^{2k-2}$, writing $r^{k^{2}-1}$ or similar is the common index slip.
> 
> **M1**: Correct right-hand side terms, $u_{2k-1} = ( 1 + r ) r^{2k-2}$ and $u_{2k} = ( 1 + r ) r^{2k-1}$. Note $u_{2k-1}$ has index $( 2 k - 1 ) - 1 = 2 k - 2$.
> 
> **M1**: Correct factorisation of the right-hand side, taking out $( 1 + r ) r^{2k-2}$ to leave a factor of $( 1 + r )$.
> 
> **A1**: A correct conclusion that the two sides are equal. Working the two sides separately and meeting in the middle, as here, is the clearest route; working from one side throughout is equally acceptable.
> 
> **B1**: A correct comment identifying that each term of $T$ equals the sum of a corresponding pair of consecutive terms of $S$, the first term of $T$ is the sum of the first two terms of $S$, the second term of $T$ is the sum of the next two, and so on. Illustrating with $u_{1}^{2} = u_{1} + u_{2}$ and $u_{2}^{2} = u_{3} + u_{4}$ is enough.

### Q7
In a geometric progression the ratio of consecutive terms is constant, so the second term divided by the first equals the third divided by the second

$\frac{5x}{x+11} = \frac{3x^{2}}{5x}$

**[M1]**

Cross-multiply, then expand the right-hand side

$25 x^{2} = 3 x^{2} ( x + 11 ) = 3 x^{3} + 33 x^{2}$

Collect the terms on one side and factorise, taking out the common factor $x^{2}$

$0 = 3 x^{3} + 8 x^{2} = x^{2} ( 3 x + 8 )$

**[M1]**

Solve, then use the condition that $x$ is non-zero to reject $x = 0$

$x = - \frac{8}{3}$

**[A1]**

Substitute $x = - \frac{8}{3}$ into the first term to find $a$

$a = x + 11 = - \frac{8}{3} + 11 = \frac{25}{3}$

Divide the second term by the first to find the common ratio

$r = \frac{5x}{x+11} = \frac{-\frac{40}{3}}{\frac{25}{3}} = - \frac{8}{5}$

**[M1]**

Use the formula for the $n$th term of a geometric progression, $u_{n} = a r^{n-1}$ with $n = 6$, so the index is 5, an odd power, so the negative ratio keeps the term negative

`u_{6} = \dfrac{25}{3}\left(-\dfrac{8}{5}\right)^{5}`

$u_{6} = - \frac{32768}{375}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the constant-ratio property to form $\frac{5x}{x+11} = \frac{3x^{2}}{5x}$. The equivalent $( 5 x )^{2} = 3 x^{2} ( x + 11 )$ is also acceptable, since the syllabus states that $a$, $b$, $c$ are in geometric progression if $b^{2} = a c$ (or equivalent).
> 
> **M1**: Correct expansion and factorisation reaching $x^{2} ( 3 x + 8 ) = 0$ or equivalent.
> 
> **A1**: Correct value $x = - \frac{8}{3}$. The root $x = 0$ must be rejected because the question states $x$ is non-zero, and it would in any case give the terms $11 , 0 , 0$, which is not a geometric progression.
> 
> **M1**: Correct first term $a = \frac{25}{3}$ and common ratio $r = - \frac{8}{5}$. Keep these as exact fractions, rounding here will not produce the exact fraction the question asks for.
> 
> **A1**: Correct sixth term $u_{6} = - \frac{32768}{375}$. Two things to watch: the index is $6 - 1 = 5$, not 6; and since 5 is odd, the negative ratio leaves the answer negative. Accept the equivalent $- 87 \frac{143}{375}$.

### Q8
In a geometric progression the ratio of consecutive terms is constant, so the second term divided by the first equals the third divided by the second

$\frac{k}{2k+3} = \frac{k-2}{k}$

**[M1]**

Cross-multiply to clear the fractions

$k^{2} = ( k - 2 ) ( 2 k + 3 )$

Expand the right-hand side

$k^{2} = 2 k^{2} + 3 k - 4 k - 6$

**[M1]**

Collect every term on one side

$k^{2} - k - 6 = 0$

**[A1]**

Factorise the quadratic: two numbers multiplying to $- 6$ and adding to $- 1$ are $- 3$ and $2$

$( k - 3 ) ( k + 2 ) = 0$

**[M1]**

Solve, then use the condition that $k$ is negative to reject $k = 3$

$k = - 2$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the constant-ratio property to form $\frac{k}{2k+3} = \frac{k-2}{k}$. The equivalent $k^{2} = ( 2 k + 3 ) ( k - 2 )$ is also acceptable, since the syllabus states that $a$, $b$, $c$ are in geometric progression if $b^{2} = a c$ (or equivalent).
> 
> **M1**: Correct expansion of the brackets, giving $k^{2} = 2 k^{2} + 3 k - 4 k - 6$ or equivalent.
> 
> **A1**: Correct quadratic $k^{2} - k - 6 = 0$.
> 
> **M1**: Correct factorisation $( k - 3 ) ( k + 2 ) = 0$. The quadratic formula is equally acceptable.
> 
> **A1**: Correct value $k = - 2$, with $k = 3$ rejected because the question states $k$ is negative. Giving both values without rejecting $k = 3$ does not earn this mark.
Substitute $k = - 2$ into the first two terms, noting that the first term is the bracket $( 2 k + 3 )$, not $k$, and it comes out negative

$a = 2 k + 3 = 2 ( - 2 ) + 3 = - 1$

Divide the second term by the first to find the common ratio

$r = \frac{k}{2k+3} = \frac{-2}{-1} = 2$

**[M1]**

Use the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $a = - 1$, $r = 2$ and $n = 12$

`S_{12} = \dfrac{(-1)\left(1-2^{12}\right)}{1-2}`

**[M1]**

Evaluate. The progression is $- 1 , - 2 , - 4 , \dots$, with every term negative, so the sum is negative

$S_{12} = - 4095$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct first term $a = - 1$ and common ratio $r = 2$, obtained by substituting $k = - 2$. The first term is $2 k + 3 = - 1$, not $k = - 2$; using $a = - 2$ is the common slip here.
> 
> **M1**: Correct use of the sum formula $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $a = - 1$, $r = 2$ and $n = 12$. The equivalent form $\frac{a(r^{n}-1)}{r-1}$ is acceptable.
> 
> **A1**: Correct sum $S_{12} = - 4095$. The answer must be negative: every term of the progression $- 1 , - 2 , - 4 , \dots$ is negative, so a positive answer of 4095 indicates a lost sign and does not earn this mark.

### Q9
There are only three terms to add, so write them out using the formula for the $n$th term of a geometric progression, $u_{n} = a r^{n-1}$, with $a = 9$

$9 ,  9 r ,  9 r^{2}$

**[M1]**

Add the three terms and set the total equal to 19

$9 + 9 r + 9 r^{2} = 19$

**[M1]**

Subtract 19 from both sides to collect every term on one side, and obtain the required result

**Final answer:** $9 r^{2} + 9 r - 10 = 0$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: The first three terms written correctly as $9$, $9 r$ and $9 r^{2}$, using $u_{n} = a r^{n-1}$ with $a = 9$.
> 
> **M1**: The three terms added and set equal to 19, giving $9 + 9 r + 9 r^{2} = 19$. Using the formula for the sum of the first $n$ terms is equally acceptable: $\frac{9(1-r^{3})}{1-r} = 19$, where factorising $1 - r^{3}$ as $( 1 - r ) ( 1 + r + r^{2} )$ lets the $( 1 - r )$ cancel and leaves $9 ( 1 + r + r^{2} ) = 19$, which is the same equation.
> 
> **A1**: Correct rearrangement reaching the printed answer $9 r^{2} + 9 r - 10 = 0$. Because the answer is given, the step $9 + 9 r + 9 r^{2} = 19$ must be seen.
Factorise the quadratic from part (a)

$( 3 r + 5 ) ( 3 r - 2 ) = 0$

**[M1]**

Set each factor to zero and solve

**Final answer:** $r = - \frac{5}{3}$** or **$r = \frac{2}{3}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct factorisation $( 3 r + 5 ) ( 3 r - 2 ) = 0$, or correct use of the quadratic formula on $9 r^{2} + 9 r - 10 = 0$.
> 
> **A1**: Both values, $r = - \frac{5}{3}$ and $r = \frac{2}{3}$. Both are needed, because the question asks for two values and neither is rejected at this stage. Accept the decimals $- 1 . 67$ (or answers which round to it) and $0 . 667$.
A geometric progression converges only when its common ratio lies strictly between $- 1$ and 1

$- 1 < r < 1$

**[B1]**

Test the two values from part (b). Since $- \frac{5}{3}$ lies outside this range, that progression diverges and only one value survives

$r = \frac{2}{3}$

Use the formula for the sum to infinity of a convergent geometric progression, $S_{\infty} = \frac{a}{1-r}$, with $a = 9$

$S_{\infty} = \frac{9}{1-\frac{2}{3}}$

**[M1]**

Divide, remembering that dividing by $\frac{1}{3}$ multiplies by 3

$S_{\infty} = 27$

**[A1]**

> **[mark-scheme]**
> **B1**: The correct condition for convergence, $- 1 < r < 1$, or the equivalent `|r| < 1`.
> 
> **M1**: Correct selection of $r = \frac{2}{3}$, rejecting $r = - \frac{5}{3}$ because `\left|-\frac{5}{3}\right| > 1`, and substitution into $S_{\infty} = \frac{a}{1-r}$ with $a = 9$. Using $r = - \frac{5}{3}$ here does not earn the mark, because that progression has no sum to infinity.
> 
> **A1**: Correct sum to infinity $S_{\infty} = 27$.

### Q10
Use the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$, with $r = \sqrt{5}$ and $n = 10$

`S_{10} = \dfrac{a\left(1-\left(\sqrt{5}\right)^{10}\right)}{1-\sqrt{5}}`

**[M1]**

Simplify the surd power using index laws. A square root is a power of $\frac{1}{2}$, so raising it to the tenth power gives $5^{5}$

`\left(\sqrt{5}\right)^{10} = \left(5^{\frac{1}{2}}\right)^{10} = 5^{5} = 3125`

**[M1]**

Substitute back. The numerator is now a plain integer, and it is negative

$S_{10} = \frac{-3124a}{1-\sqrt{5}}$

Rationalise the denominator by multiplying top and bottom by $1 + \sqrt{5}$

`S_{10} = \dfrac{-3124a\left(1+\sqrt{5}\right)}{\left(1-\sqrt{5}\right)\left(1+\sqrt{5}\right)}`

**[M1]**

Expand the denominator. The two surd terms cancel, leaving $1 - 5 = - 4$

`S_{10} = \dfrac{-3124a\left(1+\sqrt{5}\right)}{-4}`

Divide, and note the two negatives cancel to give a positive result, as the question requires

**Final answer:** `S_{10} = 781a\left(\sqrt{5}+1\right)`** as required, with **$k = 781$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum formula $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $r = \sqrt{5}$ and $n = 10$. The equivalent form $\frac{a(r^{n}-1)}{r-1}$ is acceptable and avoids one of the sign changes.
> 
> **M1**: Correct simplification of the surd power, $( \sqrt{5} )^{10} = 5^{5} = 3125$. Writing $( \sqrt{5} )^{10}$ as $5^{10}$ is the common slip and does not earn this mark.
> 
> **M1**: Correct method to rationalise the denominator, multiplying top and bottom by the conjugate $1 + \sqrt{5}$.
> 
> **A1**: Correct printed form $S_{10} = 781 a ( \sqrt{5} + 1 )$, with $k = 781$ stated. The question asks for $k$ to be determined, so the value must appear. Watch the signs: the numerator $1 - 3125 = - 3124$ is negative and the rationalised denominator $( 1 - \sqrt{5} ) ( 1 + \sqrt{5} ) = - 4$ is also negative, and it is the two cancelling that makes $k$ positive. Because the answer is given, the rationalising step must be seen.

### Q11
Write the second term using the formula for the $n$th term of a geometric progression, $u_{n} = a r^{n-1}$

$a r = 13 . 44$

Write the fifth term in the same way

$a r^{4} = 5 . 67$

**[M1]**

Divide the second equation by the first. The $a$ cancels, which leaves an equation in $r$ alone

$\frac{ar^{4}}{ar} = r^{3} = \frac{5.67}{13.44}$

**[M1]**

Take the cube root to find the common ratio

$r = \frac{3}{4}$

**[A1]**

Substitute $r = 0 . 75$ back into $a r = 13 . 44$ to find the first term

$a ( 0 . 75 ) = 13 . 44$

**[M1]**

$a = 17 . 92$

**[A1]**

The common ratio satisfies $- 1 < 0 . 75 < 1$, so the progression converges and the formula for the sum to infinity of a convergent geometric progression, $S_{\infty} = \frac{a}{1-r}$, applies

$S_{\infty} = \frac{17.92}{1-0.75}$

$S_{\infty} = 71 . 68$

**[A1]**

> **[mark-scheme]**
> **M1**: Both terms written correctly using $u_{n} = a r^{n-1}$, giving $a r = 13 . 44$ and $a r^{4} = 5 . 67$. Using $a r^{2}$ and $a r^{5}$ is the common slip and does not earn this mark.
> 
> **M1**: Correct method to eliminate $a$, with one equation divided by the other to reach $r^{3} = \frac{5.67}{13.44}$.
> 
> **A1**: Correct common ratio $r = \frac{3}{4}$. Accept $0 . 75$.
> 
> **M1**: Correct back-substitution of your $r$ into either original equation to find $a$.
> 
> **A1**: Correct first term $a = 17 . 92$.
> 
> **A1**: Correct sum to infinity $S_{\infty} = 71 . 68$. Accept the exact fraction $\frac{1792}{25}$.
Use the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $a = 17 . 92$, $r = 0 . 75$ and $n = 20$

`S_{20} = \dfrac{17.92\left(1-0.75^{20}\right)}{1-0.75} = 71.4527\ldots`

**[M1]**

Subtract from the sum to infinity, keeping full accuracy until the final rounding. The two values agree to 3 significant figures, so rounding early would destroy the answer

$S_{\infty} - S_{20} = 71 . 68 - 71 . 4527 \dots = 0 . 2273 \dots$

**Final answer:** $0 . 23$** (2 d.p.)**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum formula with $a = 17 . 92$, $r = 0 . 75$ and $n = 20$, giving $S_{20} = 71 . 4527 \dots$
> 
> **A1**: Answers which round to $0 . 23$. Do not round the intermediate working: $S_{\infty}$ and $S_{20}$ agree to 3 significant figures, so using a rounded $S_{20} = 71 . 5$ gives $0 . 18$ and loses this mark. A neat alternative avoids the problem entirely: the terms beyond the 20th are the whole progression scaled by $r^{20}$, so $S_{\infty} - S_{20} = S_{\infty} \times r^{20} = 71 . 68 \times 0 . 75^{20} = 0 . 2273 \dots$

### Q12
Substitute $k = 1$ to find the first term. The index here is $k$, not $k - 1$, so the first term is not 2401

`a = u_{1} = 2401\left(\dfrac{2}{7}\right)^{1} = 686`

The common ratio is the number being raised to the power, and $- 1 < \frac{2}{7} < 1$, so the progression converges

$r = \frac{2}{7}$

The terms from the seventh onwards are everything the progression has, minus the first six, so subtract $S_{6}$ from the sum to infinity

$S_{7\rightarrow\infty} = S_{\infty} - S_{6}$

**[M1]**

Use $S_{\infty} = \frac{a}{1-r}$ for the whole progression, and $S_{n} = \frac{a(r^{n}-1)}{r-1}$ with $n = 6$ for the part being removed

`S_{7 \to \infty} = \dfrac{686}{1-\dfrac{2}{7}} - \dfrac{686\left(\left(\dfrac{2}{7}\right)^{6}-1\right)}{\dfrac{2}{7}-1}`

**[M1]**

Evaluate each part exactly, then subtract over a common denominator of 245

$S_{7\rightarrow\infty} = \frac{4802}{5} - \frac{47034}{49}$

$S_{7\rightarrow\infty} = \frac{128}{245}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct first term $a = 686$ and common ratio $r = \frac{2}{7}$, together with a correct structure for the sum from the seventh term, $S_{\infty} - S_{6}$. Taking $a = 2401$ is the common slip: the given formula has index $k$, so $u_{1} = 2401 \times \frac{2}{7} = 686$. Subtracting $S_{7}$ rather than $S_{6}$ is the other common slip: the seventh term must be kept.
> 
> **M1**: Correct evaluation of both sums, giving $\frac{4802}{5}$ and $\frac{47034}{49}$ or equivalent.
> 
> **A1**: Correct exact value $\frac{128}{245}$. The question asks for an exact value, so a decimal does not earn this mark. An equally valid alternative is to treat the seventh term as the first term of a new progression: $u_{7} = \frac{128}{343}$, so $\frac{u_{7}}{1-r} = \frac{128/343}{5/7} = \frac{128}{245}$.
Setting $k = 1$ shows that this new progression is the original one with its first four terms stripped off. Its first term is $u_{5}$, and its common ratio is unchanged

$v_{1} = u_{5}$

So subtract the first four terms from the sum to infinity

$S_{\infty} ( v ) = S_{\infty} - S_{4}$

**[M1]**

Evaluate $S_{4}$ using $S_{n} = \frac{a(r^{n}-1)}{r-1}$ with $n = 4$, then subtract

$S_{\infty} ( v ) = \frac{4802}{5} - 954$

$S_{\infty} ( v ) = \frac{32}{5}$

**[A1]**

> **[mark-scheme]**
> **M1**: Recognition that $v_{k} = u_{k+4}$ shifts the progression along by four places, so $v_{1} = u_{5}$ and the sum to infinity is $S_{\infty} - S_{4}$. Subtracting $S_{5}$ is the common slip: the shift removes the first **four** terms and keeps $u_{5}$.
> 
> **A1**: Correct exact value $\frac{32}{5}$. Accept $6 . 4$ only if the exact form is also seen, since the question asks for an exact value. An equally valid alternative is $\frac{v_{1}}{1-r} = \frac{u_{5}}{1-r} = \frac{32/7}{5/7} = \frac{32}{5}$.

### Q13
In a geometric progression the ratio of consecutive terms is constant, so the second term divided by the first equals the third divided by the second

$\frac{3x}{x+12} = \frac{x^{2}}{3x}$

**[M1]**

Cross-multiply, then expand the right-hand side

$9 x^{2} = x^{2} ( x + 12 ) = x^{3} + 12 x^{2}$

Collect the terms on one side and factorise, taking out the common factor $x^{2}$

$0 = x^{3} + 3 x^{2} = x^{2} ( x + 3 )$

**[M1]**

Solve, then use the condition that $x$ is non-zero to reject $x = 0$

$x = - 3$

**[A1]**

Substitute $x = - 3$ into the first two terms to find the first term and the common ratio

$a = x + 12 = 9$

$r = \frac{3x}{x+12} = \frac{-9}{9} = - 1$

**[M1]**

A common ratio of $- 1$ makes the progression simply alternate in sign, so writing out the first few terms shows the whole pattern

$9 ,  - 9 ,  9 ,  - 9 ,  \dots$

Every odd-numbered term is $9$ and every even-numbered term is $- 9$, and 102 is even

$u_{102} = - 9$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the constant-ratio property to form $\frac{3x}{x+12} = \frac{x^{2}}{3x}$. The equivalent $( 3 x )^{2} = x^{2} ( x + 12 )$ is also acceptable, since the syllabus states that $a$, $b$, $c$ are in geometric progression if $b^{2} = a c$ (or equivalent).
> 
> **M1**: Correct expansion and factorisation reaching $x^{2} ( x + 3 ) = 0$ or equivalent.
> 
> **A1**: Correct value $x = - 3$. The root $x = 0$ must be rejected because the question states $x$ is non-zero, and in any case $x = 0$ would give the terms $12 , 0 , 0$, which is not a geometric progression.
> 
> **M1**: Correct first term $a = 9$ and common ratio $r = - 1$.
> 
> **A1**: Correct term $u_{102} = - 9$. Since $r = - 1$ the progression alternates $9 , - 9 , 9 , - 9 , \dots$, so every even-numbered term is $- 9$. Using the formula instead is equally acceptable: $u_{102} = 9 ( - 1 )^{101} = - 9$. Take care with the index: $9 ( - 1 )^{102} = 9$ is the common slip.

### Q14
Write the sum of the first three terms using the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$

$S_{3} = \frac{a(1-r^{3})}{1-r} = 8 . 75$

Write the sum of the first six terms in the same way

$S_{6} = \frac{a(1-r^{6})}{1-r} = 13 . 23$

Divide $S_{6}$ by $S_{3}$. Both the $a$ and the $( 1 - r )$ cancel, which leaves an expression in $r$ alone

$\frac{S_{6}}{S_{3}} = \frac{1-r^{6}}{1-r^{3}} = \frac{13.23}{8.75}$

**[M1]**

The numerator is a difference of two squares, since $1 - r^{6} = ( 1 - r^{3} ) ( 1 + r^{3} )$. Factorising it exposes a common factor with the denominator

$\frac{(1-r^{3})(1+r^{3})}{1-r^{3}} = 1 + r^{3}$

**[M1]**

Simplify the numerical fraction: multiplying top and bottom by 100 gives $\frac{1323}{875}$, and both share a factor of 7. Then subtract 1

$1 + r^{3} = \frac{189}{125} \Rightarrow r^{3} = \frac{64}{125}$

**[A1]**

Take the cube root. A cube root gives a single real value, so there is only one possible common ratio

$r = \frac{4}{5}$

**[A1]**

> **[mark-scheme]**
> **M1**: Both sums written correctly using $S_{n} = \frac{a(1-r^{n})}{1-r}$, and one divided by the other so that $a$ and $( 1 - r )$ cancel, giving $\frac{1-r^{6}}{1-r^{3}} = \frac{13.23}{8.75}$.
> 
> **M1**: Correct use of the difference of two squares to factorise $1 - r^{6}$ as $( 1 - r^{3} ) ( 1 + r^{3} )$, allowing the $( 1 - r^{3} )$ to cancel and leaving $1 + r^{3}$.
> 
> **A1**: Correct value $r^{3} = \frac{64}{125}$. The numerical step is $\frac{13.23}{8.75} = \frac{1323}{875} = \frac{189}{125}$, cancelling the common factor of 7. Accept the decimal $r^{3} = 0 . 512$.
> 
> **A1**: Correct common ratio $r = \frac{4}{5}$. Accept $0 . 8$. Unlike a square root, a cube root has only one real value, so there is no second answer here.

### Q15
Use the formula for the sum to infinity of a convergent geometric progression, $S_{\infty} = \frac{a}{1-r}$ with $a = 64$ and $S_{\infty} = 384$

$\frac{64}{1-r} = 384$

**[M1]**

Multiply by $1 - r$ and divide by 384 to isolate the bracket

$1 - r = \frac{64}{384} = \frac{1}{6}$

Rearrange to make $r$ the subject and obtain the required result

**Final answer:** $r = \frac{5}{6}$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum to infinity formula $S_{\infty} = \frac{a}{1-r}$, with $a = 64$ and $S_{\infty} = 384$ substituted to give $\frac{64}{1-r} = 384$.
> 
> **A1**: Correct rearrangement reaching the printed answer $r = \frac{5}{6}$. Because the answer is given, the intermediate step $1 - r = \frac{1}{6}$ must be seen.
Write both terms using the formula for the $n$th term of a geometric progression, $u_{n} = a r^{n-1}$, and subtract the tenth from the ninth, taking that order because the progression is decreasing, so the ninth term is the larger

`u_{9} - u_{10} = ar^{8} - ar^{9} = a\left(r^{8} - r^{9}\right)`

**[M1]**

Substitute $a = 64$ and $r = \frac{5}{6}$, keeping full accuracy until the final rounding

`64\left(\left(\dfrac{5}{6}\right)^{8} - \left(\dfrac{5}{6}\right)^{9}\right) = 2.4807\ldots`

Round to 3 significant figures as instructed

**Final answer:** $2 . 48$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: Both terms written correctly using $u_{n} = a r^{n-1}$, so `u_9 = 64\left(\frac{5}{6}\right)^{8}` and `u_{10} = 64\left(\frac{5}{6}\right)^{9}`, and one subtracted from the other. Using $r^{9}$ and $r^{10}$ is the common slip and does not earn this mark.
> 
> **A1**: Answers which round to $2 . 48$. Subtracting the other way round gives $- 2 . 48$; since the question asks for the difference between the two terms, the positive value 2.48 is the answer, but reaching $- 2 . 48$ and then stating the difference as 2.48 is equally acceptable.
Use the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $a = 64$, $r = \frac{5}{6}$ and $n = 8$

`S_{8} = \dfrac{64\left(1-\left(\dfrac{5}{6}\right)^{8}\right)}{1-\dfrac{5}{6}}`

**[M1]**

The denominator is $\frac{1}{6}$, so dividing by it multiplies the 64 up to 384

`S_{8} = 384\left(1-\left(\dfrac{5}{6}\right)^{8}\right) = 294.69\ldots`

Round to 3 significant figures as instructed

**Final answer:** $S_{8} = 295$** (3 s.f.)**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum formula $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $a = 64$, $r = \frac{5}{6}$ and $n = 8$.
> 
> **A1**: Answers which round to $295$. The unrounded value is $294 . 69 \dots$. Do not round the intermediate working before the end. As a sense check, $S_{8}$ must be less than the sum to infinity of 384, and it is.
Write the sum of the first $k$ terms using the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$, with $a = 64$ and $r = \frac{5}{6}$, and set it greater than 380

`\dfrac{64\left(1-\left(\dfrac{5}{6}\right)^{k}\right)}{1-\dfrac{5}{6}} > 380`

**[M1]**

Simplify the denominator, since $1 - \frac{5}{6} = \frac{1}{6}$

`\dfrac{64\left(1-\left(\dfrac{5}{6}\right)^{k}\right)}{\dfrac{1}{6}} > 380`

Dividing by $\frac{1}{6}$ is the same as multiplying by 6, so the 64 becomes $64 \times 6 = 384$

`384\left(1-\left(\dfrac{5}{6}\right)^{k}\right) > 380`

Divide both sides by 384, which is positive, so the inequality sign is unchanged

`1-\left(\dfrac{5}{6}\right)^{k} > \dfrac{380}{384} = \dfrac{95}{96}`

Rearrange to isolate the power. Subtracting from both sides and multiplying by $- 1$ reverses the inequality, and $1 - \frac{95}{96} = \frac{1}{96}$

**Final answer:** `\left(\dfrac{5}{6}\right)^{k} < \dfrac{1}{96}`** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct sum of the first $k$ terms formed and set greater than 380, giving `\frac{64\left(1-\left(\frac{5}{6}\right)^{k}\right)}{1-\frac{5}{6}} > 380`. Simplifying the denominator to $\frac{1}{6}$ turns this into `384\left(1-\left(\frac{5}{6}\right)^{k}\right) > 380`, since dividing by $\frac{1}{6}$ multiplies the 64 by 6.
> 
> **A1**: Correct rearrangement reaching the printed answer `\left(\frac{5}{6}\right)^{k} < \frac{1}{96}`. The key step is that multiplying through by $- 1$ reverses the inequality sign, turning the $>$ into a $<$. Because the answer is given, the step `1-\left(\frac{5}{6}\right)^{k} > \frac{95}{96}` must be seen.

### Q16
Substitute $k = 1$ to find the first term. The index here is $k$, not $k - 1$, so the first term is not 162

`a = u_{1} = 162\left(\dfrac{1}{3}\right)^{1} = 54`

The common ratio is the number being raised to the power

$r = \frac{1}{3}$

Use the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $n = 9$

`S_{9} = \dfrac{54\left(1-\left(\dfrac{1}{3}\right)^{9}\right)}{1-\dfrac{1}{3}}`

**[M1]**

Evaluate exactly. Dividing by $\frac{2}{3}$ multiplies the 54 up to 81, and $81 \times \frac{1}{19683} = \frac{1}{243}$

$S_{9} = \frac{19682}{243}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct first term $a = 54$ and common ratio $r = \frac{1}{3}$, substituted into $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $n = 9$. Taking $a = 162$ is the common slip: the given formula has index $k$, not $k - 1$, so $u_{1} = 162 \times \frac{1}{3} = 54$.
> 
> **A1**: Correct exact sum $S_{9} = \frac{19682}{243}$. The question asks for an exact value, so the decimal $80 . 99 \dots$ does not earn this mark. Accept the equivalent $81 - \frac{1}{243}$.
The terms from the tenth onwards are everything the full progression has, minus the first nine, so subtract $S_{9}$ from the sum to infinity

$S_{10\rightarrow\infty} = S_{\infty} - S_{9}$

The common ratio satisfies $- 1 < \frac{1}{3} < 1$, so the progression converges. Use $S_{\infty} = \frac{a}{1-r}$ with $a = 54$

$S_{\infty} = \frac{54}{1-\frac{1}{3}} = 81$

**[M1]**

Subtract the sum from part (a), writing 81 over the same denominator so the fractions combine

$S_{10\rightarrow\infty} = \frac{19683}{243} - \frac{19682}{243}$

**[M1]**

$S_{10\rightarrow\infty} = \frac{1}{243}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct sum to infinity of the whole progression, $S_{\infty} = \frac{54}{1-\frac{1}{3}} = 81$.
> 
> **M1**: Correct method of subtracting the first nine terms from the sum to infinity, $S_{\infty} - S_{9}$. An equally valid alternative is to treat the tenth term as the first term of a new geometric progression with the same common ratio: `u_{10} = 162\left(\frac{1}{3}\right)^{10} = \frac{2}{729}`, so $\frac{u_{10}}{1-r} = \frac{2/729}{2/3} = \frac{1}{243}$.
> 
> **A1**: Correct exact value $\frac{1}{243}$. The question asks for an exact value, so a decimal does not earn this mark. Writing $81$ as $\frac{19683}{243}$ first is what makes the subtraction land exactly.

### Q17
Use the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $n = 3$ on the first progression, which has first term $a$ and common ratio 5

$S_{3} = \frac{a(1-5^{3})}{1-5}$

**[M1]**

Evaluate the numerical parts, noting that both $1 - 125$ and $1 - 5$ are negative, so the two minus signs cancel

$S_{3} = \frac{-124a}{-4} = 31 a$

**[A1]**

Apply the same formula to the second progression, which has first term $b$ and common ratio 3

$S_{3} = \frac{b(1-3^{3})}{1-3} = \frac{-26b}{-2} = 13 b$

**[A1]**

The question states the two sums are equal, so set the expressions equal and rearrange into the ratio asked for

$31 a = 13 b$

$\frac{a}{b} = \frac{13}{31}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum formula $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $n = 3$ for at least one of the progressions. Simply adding the three terms, $a + 5 a + 25 a$ and $b + 3 b + 9 b$, is equally acceptable and often quicker here.
> 
> **A1**: Correct sum for the first progression, $S_{3} = 31 a$.
> 
> **A1**: Correct sum for the second progression, $S_{3} = 13 b$.
> 
> **A1**: Correct ratio $\frac{a}{b} = \frac{13}{31}$. Take care with the inversion: $31 a = 13 b$ rearranges to $\frac{a}{b} = \frac{13}{31}$, so answering $\frac{31}{13}$ does not earn this mark. The fraction is already in its simplest form, as 13 and 31 are both prime.

### Q18
Write the sum of the first two terms using the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$

$S_{2} = \frac{a(1-r^{2})}{1-r} = 9 . 31$

Write the sum of the first four terms in the same way

$S_{4} = \frac{a(1-r^{4})}{1-r} = 11 . 02$

Divide $S_{4}$ by $S_{2}$. Both the $a$ and the $( 1 - r )$ cancel, which leaves an expression in $r$ alone

$\frac{S_{4}}{S_{2}} = \frac{1-r^{4}}{1-r^{2}} = \frac{11.02}{9.31}$

**[M1]**

Simplify the numerical fraction: multiplying top and bottom by 100 gives $\frac{1102}{931}$, and both share a factor of 19

**Final answer:** $\frac{1-r^{4}}{1-r^{2}} = \frac{58}{49}$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Both sums written correctly using $S_{n} = \frac{a(1-r^{n})}{1-r}$, and one divided by the other so that $a$ and $( 1 - r )$ cancel, giving $\frac{1-r^{4}}{1-r^{2}} = \frac{11.02}{9.31}$.
> 
> **A1**: Correct simplification reaching the printed answer $\frac{58}{49}$. The numerical step is $\frac{11.02}{9.31} = \frac{1102}{931} = \frac{58}{49}$, cancelling the common factor of 19. Because the answer is given, the division of the two sums must be seen.
The numerator is a difference of two squares, since $1 - r^{4} = ( 1 - r^{2} ) ( 1 + r^{2} )$. Factorising it exposes a common factor with the denominator

$\frac{(1-r^{2})(1+r^{2})}{1-r^{2}} = \frac{58}{49}$

**[M1]**

Cancel the $( 1 - r^{2} )$, then subtract 1 from both sides

$1 + r^{2} = \frac{58}{49} \Rightarrow r^{2} = \frac{9}{49}$

Take the square root, remembering that a square root has both a positive and a negative value

$r = \pm \frac{3}{7}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the difference of two squares to factorise $1 - r^{4}$ as $( 1 - r^{2} ) ( 1 + r^{2} )$, allowing the $( 1 - r^{2} )$ to cancel. This may be implied by $1 + r^{2} = \frac{58}{49}$ appearing.
> 
> **A1**: Both values of the common ratio, $r = \frac{3}{7}$ and $r = - \frac{3}{7}$. Both are needed for this mark, because the question asks for two values, and nothing rules out a negative ratio. Accept answers which round to $\pm 0 . 429$.

### Q19
A geometric progression converges, and so has a sum to infinity, exactly when its common ratio lies strictly between $- 1$ and 1

$- 1 < r < 1$

**[B1]**

Find the common ratio by dividing the second term by the first

$r = \frac{3x}{-1} = - 3 x$

Substitute this into the inequality

$- 1 < - 3 x < 1$

**[M1]**

Divide every part by $- 3$, remembering that dividing by a negative number reverses both inequality signs

$\frac{1}{3} > x > - \frac{1}{3}$

Rewrite with the smaller bound on the left, which is the conventional way round

$- \frac{1}{3} < x < \frac{1}{3}$

One value inside this range has to be cut out. Setting $x = 0$ would make the common ratio zero, and a progression $- 1 , 0 , 0 , \dots$ has no common ratio at all, since dividing the third term by the second gives $\frac{0}{0}$

**Final answer:** $- \frac{1}{3} < x < 0$** or **$0 < x < \frac{1}{3}$

**[A1]**

> **[mark-scheme]**
> **B1**: The correct condition for convergence, $- 1 < r < 1$. Accept the equivalent `|r| < 1`.
> 
> **M1**: Correct common ratio $r = - 3 x$, substituted into your inequality to give $- 1 < - 3 x < 1$. Checking against the third term confirms the ratio: $\frac{-9x^{2}}{3x} = - 3 x$ as well.
> 
> **A1**: The correct range with $x = 0$ excluded: $- \frac{1}{3} < x < 0$ or $0 < x < \frac{1}{3}$. Two things are being tested. First, dividing through by $- 3$ **reverses** both inequality signs; forgetting this gives the impossible $- \frac{1}{3} > x > \frac{1}{3}$. Second, $x = 0$ must be removed: it would make every term after the first zero, and such a sequence has no common ratio, so it is not a geometric progression. Accept the equivalent `|x| < \frac{1}{3}`, $x \neq 0$. Give your answer as inequalities, not in interval notation.
The progression is convergent, so use the formula for the sum to infinity of a convergent geometric progression, $S_{\infty} = \frac{a}{1-r}$ with $a = - 1$ and $r = - 3 x$, noting that subtracting a negative gives an addition

$S_{\infty} = \frac{-1}{1-(-3x)}$

$S_{\infty} = \frac{-1}{1+3x}$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct expression $S_{\infty} = \frac{-1}{1+3x}$. The double negative in $1 - ( - 3 x )$ becomes $1 + 3 x$. Leaving it as $1 - 3 x$ is the common slip and does not earn this mark. Accept the equivalent forms $- \frac{1}{1+3x}$ and $\frac{1}{-1-3x}$.

### Q20
(i)

In a geometric progression the ratio of consecutive terms is constant, so the second term divided by the first equals the third divided by the second

$\frac{k}{k-3} = \frac{2k+8}{k}$

**[M1]**

Cross-multiply to clear the fractions

$k^{2} = ( 2 k + 8 ) ( k - 3 )$

Expand the right-hand side

$k^{2} = 2 k^{2} - 6 k + 8 k - 24$

**[M1]**

Collect every term on one side to obtain the required result

**Final answer:** $k^{2} + 2 k - 24 = 0$** as required**

**[A1]**

(ii)

Factorise the quadratic: two numbers multiplying to $- 24$ and adding to $2$ are $- 4$ and $6$

$( k - 4 ) ( k + 6 ) = 0$

**[M1]**

Solve to find the two roots

$k = 4$* or *$k = - 6$

The question states that $k$ is positive, so reject $k = - 6$

$k = 4$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the constant-ratio property in part (i) to form $\frac{k}{k-3} = \frac{2k+8}{k}$. The equivalent form $k^{2} = ( k - 3 ) ( 2 k + 8 )$ is also acceptable, since the syllabus states that $a$, $b$, $c$ are in geometric progression if $b^{2} = a c$ (or equivalent).
> 
> **M1**: Correct expansion of the brackets in part (i), giving $k^{2} = 2 k^{2} - 6 k + 8 k - 24$ or equivalent.
> 
> **A1**: Correct rearrangement in part (i) reaching the printed answer $k^{2} + 2 k - 24 = 0$. Because the answer is given, the expanded line must be seen.
> 
> **M1**: Correct factorisation of the quadratic in part (ii), $( k - 4 ) ( k + 6 ) = 0$. The quadratic formula is equally acceptable.
> 
> **A1**: Correct value $k = 4$ in part (ii), with $k = - 6$ rejected because the question states $k$ is positive. Giving both values without rejecting $- 6$ does not earn this mark.
Substitute $k = 4$ from part (a) into the first two terms and divide the second by the first

$r = \frac{k}{k-3} = \frac{4}{4-3}$

$r = 4$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct common ratio $r = 4$. Any correct pair of consecutive terms may be used, since the progression is $1 , 4 , 16 , \dots$, so dividing the third term by the second gives the same answer.
Substitute $k = 4$ from part (a) into the first term, remembering that the first term is the bracket $( k - 3 )$, not $k$

$a = k - 3 = 1$

Use the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $a = 1$, $r = 4$ and $n = 12$

$S_{12} = \frac{1(1-4^{12})}{1-4}$

**[M1]**

Evaluate, noting that both the numerator and the denominator are negative, so the sum is positive

$S_{12} = 5592405$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum formula $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $a = 1$, $r = 4$ and $n = 12$. The first term is $k - 3 = 1$, not $k = 4$. Using $a = 4$ is the common slip here and does not earn this mark. The equivalent form $\frac{a(r^{n}-1)}{r-1}$ is acceptable.
> 
> **A1**: Correct sum $S_{12} = 5592405$.

### Q21
In a geometric progression the ratio of consecutive terms is constant, so the second term divided by the first must equal the third divided by the second

$\frac{4x}{x^{2}} = \frac{x+14}{4x}$

**[M1]**

Cross-multiply to clear the fractions

$16 x^{2} = x^{2} ( x + 14 )$

Expand the right-hand side

$16 x^{2} = x^{3} + 14 x^{2}$

Collect every term on one side to obtain the required result

**Final answer:** $x^{3} - 2 x^{2} = 0$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the constant-ratio property to form an equation, $\frac{4x}{x^{2}} = \frac{x+14}{4x}$. The equivalent "square the middle term" form $( 4 x )^{2} = x^{2} ( x + 14 )$ is also acceptable, since the syllabus states that $a$, $b$, $c$ are in geometric progression if $b^{2} = a c$ (or equivalent).
> 
> **A1**: Correct expansion and rearrangement reaching the printed answer $x^{3} - 2 x^{2} = 0$. Because the answer is given, the expanded line $16 x^{2} = x^{3} + 14 x^{2}$ must be seen. Accept the equivalent $0 = x^{3} - 2 x^{2}$.
Factorise the cubic from part (a), taking out the common factor $x^{2}$

$x^{2} ( x - 2 ) = 0$

Solve to find the two possible values of $x$

$x = 0$* or *$x = 2$

The question states that $x > 0$, so reject $x = 0$

$x = 2$

**[M1]**

Substitute $x = 2$ into the first two terms to find the first term and the common ratio

$a = x^{2} = 4$

$r = \frac{4x}{x^{2}} = \frac{8}{4} = 2$

**[M1]**

Use the formula for the $n$th term of a geometric progression, $u_{n} = a r^{n-1}$ with $n = 15$

$u_{15} = 4 ( 2 )^{14}$

$u_{15} = 65536$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct factorisation and solution of $x^{3} - 2 x^{2} = 0$, reaching $x = 2$. The root $x = 0$ must be rejected using the condition $x > 0$ given in the question, noting that $x = 0$ would also make every term zero, which is not a geometric progression.
> 
> **M1**: Correct first term $a = 4$ and common ratio $r = 2$, obtained by substituting $x = 2$.
> 
> **A1**: Correct fifteenth term $u_{15} = 65536$. Using $4 ( 2 )^{15}$ instead of $4 ( 2 )^{14}$ is the common slip and gives 131 072.
Set the nth term equal to 8192, using $u_{n} = a r^{n-1}$ with $a = 4$ and $r = 2$ from part (b)

$4 ( 2 )^{n-1} = 8192$

Divide by 4, then write 2048 as a power of 2 so the indices can be compared

$2^{n-1} = 2048 = 2^{11}$

Equate the indices and solve for $n$

$n - 1 = 11 \Rightarrow n = 12$

A value of $n$ only counts as a term if it is a positive whole number, and it is

**Final answer:** **Yes, **$n = 12$** is a positive integer, so 8192 is the twelfth term of the progression**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct conclusion that 8192 **is** a term, supported by a reason. You need to solve $4 ( 2 )^{n-1} = 8192$ to get $n = 12$ and then state that $n$ is a positive integer. Answering "yes" with no supporting value of $n$ does not earn this mark, because the reason is what is being marked. Verifying instead that $4 \times 2^{11} = 8192$ directly is equally acceptable.

### Q22
Substitute $k = 1 , 2 , 3 , 4 , 5$ into the given formula in turn

$u_{1} = 5 \times 2^{0} ,  u_{2} = 5 \times 2^{1} ,  u_{3} = 5 \times 2^{2}$

**[M1]**

Evaluate each power of 2 and multiply by 5, each term is double the one before, so the common ratio is 2

$5 ,  10 ,  20 ,  40 ,  80$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct substitution of at least the first two values of $k$ into $u_{k} = 5 \times 2^{k-1}$. Note the index is $k - 1$, so the first term is $5 \times 2^{0} = 5$, not $5 \times 2^{1} = 10$, starting at 10 is the common slip and does not earn this mark.
> 
> **A1**: All five terms correct: $5 , 10 , 20 , 40 , 80$. All five are needed for this mark.
Part (a) has already given the five terms, so add them directly

$S_{5} = 5 + 10 + 20 + 40 + 80$

**[M1]**

Evaluate the sum

$S_{5} = 155$

**[A1]**

> **[mark-scheme]**
> **M1**: A correct sum of the five terms, $5 + 10 + 20 + 40 + 80$. Using the formula for the sum of the first $n$ terms of a geometric progression is equally acceptable: $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $a = 5$, $r = 2$ and $n = 5$, giving $\frac{5(1-2^{5})}{1-2}$. Either method earns this mark.
> 
> **A1**: Correct sum $S_{5} = 155$.

### Q23
The first term, common ratio and number of terms are all given, so use the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $a = 5$, $r = \frac{3}{2}$ and $n = 12$

`S_{12} = \dfrac{5\left(1-\left(\dfrac{3}{2}\right)^{12}\right)}{1-\dfrac{3}{2}}`

**[M1]**

Evaluate, keeping full accuracy until the final rounding

$S_{12} = 1287 . 46 \dots$

Round to the nearest whole number as instructed

$S_{12} = 1287$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum formula $S_{n} = \frac{a(1-r^{n})}{1-r}$, with $a = 5$, $r = \frac{3}{2}$ and $n = 12$ all correctly substituted. The equivalent form $S_{n} = \frac{a(r^{n}-1)}{r-1}$ is equally acceptable and gives the same value.
> 
> **A1**: Correct sum $S_{12} = 1287$. The unrounded value is $1287 . 46 \dots$, so rounding to the nearest whole number gives 1287. An answer of 1287.46 (unrounded) does not earn this mark, as the question asks for the nearest whole number.
The common ratio satisfies $- 1 < \frac{1}{8} < 1$, so the progression converges and the formula for the sum to infinity of a convergent geometric progression, $S_{\infty} = \frac{a}{1-r}$ applies with $a = 4$

$S_{\infty} = \frac{4}{1-\frac{1}{8}}$

**[M1]**

Simplify the denominator and divide

$S_{\infty} = \frac{32}{7}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum to infinity formula $S_{\infty} = \frac{a}{1-r}$, with $a = 4$ and $r = \frac{1}{8}$ substituted to give $\frac{4}{1-\frac{1}{8}}$.
> 
> **A1**: Correct sum to infinity $S_{\infty} = \frac{32}{7}$. Accept the mixed number $4 \frac{4}{7}$, or answers which round to $4 . 57$.

### Q24
(i)

Substitute $n = 5$ into the given formula

$u_{5} = 2 ( 3 )^{5}$

$u_{5} = 486$

Substitute $n = 10$ into the given formula

$u_{10} = 2 ( 3 )^{10}$

$u_{10} = 118  098$

**[B1]**

(ii)

Substitute $n = 5$ into the given formula

$u_{5} = 10  000 ( 1 . 02 )^{5}$

**Final answer:** $u_{5} = 11  040 . 81$** (2 d.p.)**

Substitute $n = 10$ into the given formula

$u_{10} = 10  000 ( 1 . 02 )^{10}$

**Final answer:** $u_{10} = 12  189 . 94$** (2 d.p.)**

**[B1]**

A progression like this one models a starting amount of $10  000$ growing by `2\%` each period, so 2 decimal places is the natural accuracy for a money value

(iii)

Substitute $n = 5$ into the given formula, and write the negative power as a fraction

$u_{5} = 3^{-5}$

$u_{5} = \frac{1}{243}$

Substitute $n = 10$ into the given formula

$u_{10} = 3^{-10}$

$u_{10} = \frac{1}{59049}$

**[B1]**

> **[mark-scheme]**
> **B1**: Both terms correct for part (i): $u_{5} = 486$ and $u_{10} = 118  098$. Both are needed for this mark.
> 
> **B1**: Both terms correct for part (ii): answers which round to $11  040 . 81$ and $12  189 . 94$. Both are needed for this mark. The question does not state an accuracy, so any reasonable rounding of the correct values is acceptable.
> 
> **B1**: Both terms correct for part (iii): $u_{5} = \frac{1}{243}$ and $u_{10} = \frac{1}{59049}$. Both are needed. Accept the equivalent forms $3^{-5}$ and $3^{-10}$, or the decimals $0 . 00412$ and $0 . 0000169$.

### Q25
The sum to infinity is given, so use the formula for the sum to infinity of a convergent geometric progression, $S_{\infty} = \frac{a}{1-r}$ with $a = 6$

$\frac{6}{1-r} = 8$

**[M1]**

Multiply both sides by $1 - r$ to clear the fraction

$6 = 8 ( 1 - r )$

Divide both sides by 8 to isolate the bracket

$\frac{3}{4} = 1 - r$

Rearrange to make $r$ the subject and obtain the required result

**Final answer:** $r = 0 . 25$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum to infinity formula $S_{\infty} = \frac{a}{1-r}$, with $a = 6$ and $S_{\infty} = 8$ substituted to give $\frac{6}{1-r} = 8$.
> 
> **A1**: Correct rearrangement reaching the printed answer $r = 0 . 25$, with the working shown. Accept $r = \frac{1}{4}$. Because the answer is given, you must show the intermediate rearrangement, writing down $r = 0 . 25$ with no working does not earn this mark.
A geometric progression has a sum to infinity only when it converges, and that happens exactly when the common ratio lies strictly between $- 1$ and 1

**Final answer:** **Since **$- 1 < 0 . 25 < 1$** the progression converges, so the sum to infinity exists**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct explanation referring to the size of the common ratio. You need to state that $- 1 < 0 . 25 < 1$ (or equivalently that `|r| < 1`) **and** draw the conclusion that the progression converges, so the sum to infinity exists. Saying only "because $r$ is small" or "because $r$ is less than 1" is not enough, the ratio must be shown to lie strictly between $- 1$ and 1.

### Q26
(i)

Divide consecutive terms to find the common ratio, and read off the first term

$r = \frac{12}{3} = 4$

$a = 3$

Substitute $a = 3$ and $r = 4$ into $u_{n} = a r^{n-1}$

$u_{n} = 3 ( 4 )^{n-1}$

**[B1]**

(ii)

Substitute $a = 5$ and $r = - 2$ into $u_{n} = a r^{n-1}$

$u_{n} = 5 ( - 2 )^{n-1}$

**[B1]**

(iii)

Substitute $a = 16$ and $r = \frac{1}{2}$ into $u_{n} = a r^{n-1}$

`u_n = 16\left(\dfrac{1}{2}\right)^{n-1}`

Write the power of a half as a single fraction to tidy the formula

$u_{n} = \frac{16}{2^{n-1}}$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct nth-term formula for part (i): $u_{n} = 3 ( 4 )^{n-1}$. You must find the common ratio $r = 4$ from the given terms first. Any equivalent form is acceptable.
> 
> **B1**: Correct nth-term formula for part (ii): $u_{n} = 5 ( - 2 )^{n-1}$. The brackets around $- 2$ are needed, $u_{n} = 5 \times - 2^{n-1}$ does not earn this mark, as it means something different.
> 
> **B1**: Correct nth-term formula for part (iii): $u_{n} = \frac{16}{2^{n-1}}$, or the equivalent unsimplified form `u_n = 16\left(\frac{1}{2}\right)^{n-1}`. Either is acceptable, as is $u_{n} = 2^{5-n}$.

### Q27
Write the third term using the formula for the $n$th term of a geometric progression, $u_{n} = a r^{n-1}$

$a r^{2} = 10$

Write the sixth term in the same way

$a r^{5} = 270$

Divide the second equation by the first, the $a$ cancels, leaving an equation in $r$ alone

$\frac{ar^{5}}{ar^{2}} = \frac{270}{10} \Rightarrow r^{3} = 27$

**[M1]**

Take the cube root to find the common ratio

$r = 3$

**[A1]**

Substitute $r = 3$ back into $a r^{2} = 10$ to find the first term

$a ( 3 )^{2} = 10 \Rightarrow 9 a = 10$

$a = \frac{10}{9}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method to eliminate $a$. You need both terms written using $u_{n} = a r^{n-1}$, giving $a r^{2} = 10$ and $a r^{5} = 270$, then one equation divided by the other to reach an equation in $r$ only. This may be implied by $r^{3} = 27$ appearing.
> 
> **A1**: Correct common ratio $r = 3$.
> 
> **A1**: Correct first term $a = \frac{10}{9}$. Accept the exact equivalent $1 \frac{1}{9}$, or answers which round to $1 . 11$.
Write both terms using $u_{n} = a r^{n-1}$ and set the twelfth equal to 16 times the eighth

$a r^{11} = 16 a r^{7}$

**[M1]**

Divide both sides by $a r^{7}$, valid because neither $a$ nor $r$ can be zero in a geometric progression

$r^{4} = 16$

Take the fourth root, remembering that an even root has both a positive and a negative value

$r = \pm 2$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $u_{n} = a r^{n-1}$ to form the relationship $a r^{11} = 16 a r^{7}$, or an equivalent equation reducing to the form $r^{4} = k$. This may be implied by $r^{4} = 16$ appearing.
> 
> **A1**: Both values of the common ratio, $r = 2$ and $r = - 2$. Both are needed for this mark. Nothing in the question rules out a negative ratio, so omitting or rejecting $r = - 2$ does not earn it.

### Q28
A progression is geometric only if the ratio of consecutive terms is always the same, so test that ratio in each case

$r = \frac{u_{n+1}}{u_{n}}$

(i)

Divide consecutive terms to test whether the ratio is constant

$\frac{8}{3} \neq \frac{13}{8}$

The ratios are not equal, so there is no common ratio. Here the terms increase by 5 each time, so this is an arithmetic progression

**Final answer:** **Not a geometric progression**

**[B1]**

(ii)

Divide consecutive terms to test whether the ratio is constant

$\frac{15}{5} = \frac{45}{15} = \frac{135}{45} = 3$

The ratio is constant, so this is a geometric progression, so read off the first term and the common ratio

$a = 5 ,  r = 3$

**[B1]**

(iii)

Divide consecutive terms to test whether the ratio is constant

$\frac{-10}{5} = \frac{20}{-10} = \frac{-40}{20} = - 2$

The ratio is constant, so this is a geometric progression, and the ratio being negative is what makes the terms alternate in sign

$a = 5 ,  r = - 2$

**[B1]**

(iv)

Divide consecutive terms to test whether the ratio is constant

$\frac{1}{6} \div \frac{1}{3} = \frac{1}{12} \div \frac{1}{6} = \frac{1}{2}$

The ratio is constant, so this is a geometric progression

$a = \frac{1}{3} ,  r = \frac{1}{2}$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct identification that $3 , 8 , 13 , 18 , \dots$ is not a geometric progression. You need to show that the ratio of consecutive terms is not constant, for example that $\frac{8}{3} \neq \frac{13}{8}$. Noting that it is an arithmetic progression instead is not required for the mark.
> 
> **B1**: Correct identification of $5 , 15 , 45 , 135 , \dots$ as a geometric progression, with $a = 5$ and $r = 3$. Both values are needed for this mark.
> 
> **B1**: Correct identification of $5 , - 10 , 20 , - 40 , \dots$ as a geometric progression, with $a = 5$ and $r = - 2$. The negative sign on the common ratio is needed.
> 
> **B1**: Correct identification of $\frac{1}{3} , \frac{1}{6} , \frac{1}{12} , \dots$ as a geometric progression, with $a = \frac{1}{3}$ and $r = \frac{1}{2}$. Accept $r = 0 . 5$.

### Q29
Read off the first term

$a = k ( k + 1 )$

Divide the second term by the first to find the common ratio, the $k ( k + 1 )$ cancels

$r = \frac{k(k+1)^{2}}{k(k+1)} = k + 1$

Substitute both into the formula for the $n$th term of a geometric progression, $u_{n} = a r^{n-1}$

$u_{n} = k ( k + 1 ) ( k + 1 )^{n-1}$

Add the indices, since $( k + 1 )^{1} \times ( k + 1 )^{n-1} = ( k + 1 )^{1+(n-1)}$

$u_{n} = k ( k + 1 )^{n}$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct nth-term formula $u_{n} = k ( k + 1 )^{n}$. You need the common ratio $r = k + 1$ first, found by dividing consecutive terms. The unsimplified form $u_{n} = k ( k + 1 ) ( k + 1 )^{n-1}$ is acceptable.
The progression is convergent, so the formula for the sum to infinity of a convergent geometric progression, $S_{\infty} = \frac{a}{1-r}$ applies, substitute $a = k ( k + 1 )$ and $r = k + 1$

$S_{\infty} = \frac{k(k+1)}{1-(k+1)}$

**[M1]**

Simplify the denominator, the $1$ and the $+ 1$ cancel, leaving just $- k$

$S_{\infty} = \frac{k(k+1)}{-k}$

Cancel the common factor of $k$ to obtain the required result

**Final answer:** $S_{\infty} = - ( k + 1 )$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum to infinity formula $S_{\infty} = \frac{a}{1-r}$, with $a = k ( k + 1 )$ and $r = k + 1$ substituted to give $\frac{k(k+1)}{1-(k+1)}$.
> 
> **A1**: Correct simplification reaching the printed answer $- ( k + 1 )$. Because the answer is given, the simplification of the denominator to $- k$ must be seen. Accept the equivalent form $- k - 1$.
Set the expression from part (b) equal to the given sum to infinity

$- ( k + 1 ) = - \frac{1}{4}$

**[M1]**

Multiply both sides by $- 1$, then subtract 1 to make $k$ the subject

$k + 1 = \frac{1}{4}$

$k = - \frac{3}{4}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct equation formed by setting your answer to part (b) equal to $- \frac{1}{4}$, giving $- ( k + 1 ) = - \frac{1}{4}$.
> 
> **A1**: Correct value $k = - \frac{3}{4}$. Accept $- 0 . 75$. As a check, this gives a common ratio of $r = k + 1 = \frac{1}{4}$, which does lie between $- 1$ and 1, so the progression is convergent as the question requires.

### Q30
Write the sixth term using the formula for the $n$th term of a geometric progression, $u_{n} = a r^{n-1}$, with $a = 2$

$2 r^{5} = 486$

**[M1]**

Divide by 2, then take the fifth root to find the common ratio

$r^{5} = 243$

$r = 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $u_{n} = a r^{n-1}$ to form $2 r^{5} = 486$, using $a = 2$ and $n = 6$. Using $r^{6}$ rather than $r^{5}$ is the common slip and does not earn this mark.
> 
> **A1**: Correct common ratio $r = 3$.
Use the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $a = 2$ and, from part (a), $r = 3$, and set it equal to the given sum

$177146 = \frac{2(1-3^{n})}{1-3}$

**[M1]**

Simplify the right-hand side, the denominator is $- 2$, so dividing $2$ by $- 2$ flips the sign of the bracket

$177146 = 3^{n} - 1$

Add 1 to both sides to obtain the required result

**Final answer:** $3^{n} = 177147$** as required**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum formula $S_{n} = \frac{a(1-r^{n})}{1-r}$ with $a = 2$, $r = 3$ and $S_{n} = 177146$, giving $177146 = \frac{2(1-3^{n})}{1-3}$. The equivalent form $\frac{2(3^{n}-1)}{3-1}$ is equally acceptable.
> 
> **A1**: Correct simplification reaching the printed answer $3^{n} = 177147$. Because the answer is given, the simplification to $3^{n} - 1$ must be seen. Jumping straight to $3^{n} = 177147$ does not earn this mark.
