# Mark Schemes — Arithmetic & Geometric Series
**Series** · Edexcel IGCSE Further Pure Maths (4PM1)


## Q1 — medium — 9 marks · exam-questions

### 8((a)) — 1 marks
The sum of the first one term is just the first term itself

So substitute $n = 1$ into the given formula for $S_{n}$

`S_{1} = 2 \left(1\right) \left(1 + 3\right)`

$a = 8$

**[B1]**

> **[mark-scheme]**
> **B1**: A first term of 8.
> 
> No working is required, so the value on its own earns the mark.
> 
> Building the series from the formula another way is equally acceptable, for example by comparing `2 n \left(n + 3\right)` with `\frac{n}{2} \left[2 a + \left(n - 1\right) d\right]` and reading off the first term.

> **[exam-tip]**
> The sum to one term and the first term are the same thing.
> 
> - $S_{1} = a$ always, so substituting $n = 1$ is all this part needs
> - There is no need to expand the formula or to find the common difference first
> 
> Take care with the bracket.
> 
> - `2 \times 1 \times \left(1 + 3\right)` is $8$, not $2 \times 1 \times 1 + 3$

### 8((b)) — 2 marks
The common difference is the gap between consecutive terms, so find the second term first

Substitute $n = 2$ into the formula to get the sum of the first two terms

`S_{2} = 2 \left(2\right) \left(2 + 3\right)`

$S_{2} = 20$

The sum of the first two terms is the first term plus the second, so subtract the first term to leave the second

$T_{2} = 20 - 8$

$T_{2} = 12$

**[M1]**

The common difference is the second term minus the first

$d = 12 - 8$

$d = 4$

**[A1]**

> **[mark-scheme]**
> **M1**: Finds $S_{2} = 20$ and subtracts your first term to obtain the second term, or uses an equivalent complete method for the common difference.
> 
> **A1**: $d = 4$.
> 
> The method mark follows through from your first term in part (a).
> 
> Comparing the given formula with the standard sum formula is equally acceptable. Expanding `2 n \left(n + 3\right)` to $2 n^{2} + 6 n$ and comparing with `\frac{d}{2} n^{2} + \left(a - \frac{d}{2}\right) n` gives $\frac{d}{2} = 2$, so $d = 4$, and earns both marks.
> 
> Setting `\frac{2}{2} \left[2 a + d\right]` equal to 20 and solving for $d$ with your value of $a$ is also accepted.

> **[exam-tip]**
> A sum formula gives you individual terms by subtraction.
> 
> - Any term is the sum to that point minus the sum to the point before, so $T_{2} = S_{2} - S_{1}$
> - That idea is used again in part (c), so it is worth being comfortable with it here
> 
> Do not confuse the second term with the common difference.
> 
> - $T_{2} = 12$ is the second term, and the common difference is $12 - 8 = 4$
> - Stopping at 12 is the most common error in this part
> 
> Check by rebuilding the start of the series.
> 
> - With $a = 8$ and $d = 4$ the first two terms are 8 and 12, which add to 20, matching $S_{2}$

### 8((c)) — 6 marks
Both sides of the given equation need writing in terms of $n$ before it can be solved

Start with the left, replacing $n$ by $n - 4$ in the formula for $S_{n}$

- The bracket $n + 3$ becomes `\left(n - 4\right) + 3`, which is $n - 1$

`S_{n - 4} = 2 \left(n - 4\right) \left(n - 1\right)`

**[M1]**

Now the right, using `T_{n} = a + \left(n - 1\right) d` with the values from parts (a) and (b)

- Replacing $n$ by $n + 3$ makes the bracket `\left(n + 3\right) - 1`, which is $n + 2$

`T_{n + 3} = 8 + 4 \left(n + 2\right)`

$T_{n+3} = 4 n + 16$

**[M1]**

Put both into the equation given in the question

`6 \times 2 \left(n - 4\right) \left(n - 1\right) = 7 \left(4 n + 16\right)`

**[M1]**

Expand the two brackets on the left, then multiply by 12

`12 \left(n^{2} - 5 n + 4\right) = 28 n + 112`

$12 n^{2} - 60 n + 48 = 28 n + 112$

Collect every term on the left, then divide through by 4

$3 n^{2} - 22 n - 16 = 0$

**[A1]**

Factorise, looking for two numbers multiplying to `3 \times \left(- 16\right) = - 48` and adding to $- 22$

- Those numbers are 2 and $- 24$

`\left(n - 8\right) \left(3 n + 2\right) = 0`

**[M1]**

Setting each bracket to zero gives $n = 8$ or $n = - \frac{2}{3}$

$n$ counts terms, so it must be a positive whole number and the negative fraction is rejected

$n = 8$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the given formula for $S_{n}$ with $n - 4$ in place of $n$.
> 
> **M1**: Uses `T_{n} = a + \left(n - 1\right) d` with your values of $a$ and $d$ and with $n + 3$ in place of $n$.
> 
> **M1**: Substitutes both expressions into $6 S_{n-4} = 7 T_{n+3}$ and expands to reach a three term quadratic.
> 
> **A1**: The correct quadratic, $3 n^{2} - 22 n - 16 = 0$ or any equivalent such as $12 n^{2} - 88 n - 64 = 0$.
> 
> **M1**: A complete and correct method for solving that quadratic, by factorising, completing the square or the quadratic formula.
> 
> **A1**: $n = 8$.
> 
> Both method marks for the substitutions follow through from your own values of $a$ and $d$.
> 
> Finding the $n$th term as $S_{n} - S_{n-1}$ rather than from `a + \left(n - 1\right) d` is equally acceptable. That gives $T_{n} = 4 n + 4$ and so $T_{n+3} = 4 n + 16$, which is the same expression, and it earns the second method mark in the same way.
> 
> The negative root does not have to be written down or explicitly rejected, but $n = 8$ must be the value given as the answer.

> **[exam-tip]**
> Replacing $n$ by something else means replacing it everywhere.
> 
> - In $S_{n-4}$ the bracket $n + 3$ becomes $n - 1$, and forgetting to change it is the commonest error here
> - In $T_{n+3}$ the bracket $n - 1$ becomes $n + 2$
> 
> Write each side out separately before combining them.
> 
> - One expression is a quadratic and the other is linear, so trying to do both at once in a single line is where the algebra usually breaks down
> 
> Divide through before factorising.
> 
> - $12 n^{2} - 88 n - 64 = 0$ becomes $3 n^{2} - 22 n - 16 = 0$, and the smaller numbers are much easier to split
> 
> Sanity-check the answer against what $n$ means.
> 
> - $n$ is a position in the series, so a negative fraction is discarded without comment
> - Substituting back, $S_{4} = 56$ and $T_{11} = 48$, and six times 56 and seven times 48 both come to 336

## Q2 — medium — 5 marks · exam-questions

### 1() — 5 marks
Substitute $n = 1$ into the expression for the $n$th term to get the first term

`a = 3 \text{e}^{\left(1 - 2\right)}`

$a = 3 \text{e}^{-1}$

**[B1]**

Now substitute $n = 2$ to get the second term

`3 \text{e}^{\left(1 - 4\right)} = 3 \text{e}^{- 3}`

The common ratio is the second term divided by the first, and dividing powers of $\text{e}$ means subtracting the indices

$r = \frac{3\text{e}^{-3}}{3\text{e}^{-1}}$

$r = \text{e}^{-2}$

**[B1]**

Since $\text{e} > 1$, the value of $\text{e}^{-2}$ lies between 0 and 1, so the series converges and the sum to infinity exists

Use $S_{\infty} = \frac{a}{1-r}$ with these values

$S_{\infty} = \frac{3\text{e}^{-1}}{1-\text{e}^{-2}}$

**[M1]**

The required form has no negative indices, so multiply the top and the bottom by $\text{e}^{2}$

- On the top, $3 \text{e}^{-1} \times \text{e}^{2} = 3 \text{e}$
- On the bottom, $1 \times \text{e}^{2} = \text{e}^{2}$ and $\text{e}^{-2} \times \text{e}^{2} = 1$

`S_{\infty} = \frac{3 \text{e}^{- 1} \times \text{e}^{2}}{\left(1 - \text{e}^{- 2}\right) \times \text{e}^{2}}`

**[M1]**

$S_{\infty} = \frac{3\text{e}}{\text{e}^{2}-1}$

**[A1]**

so $a = 3$ and $b = 2$

> **[mark-scheme]**
> **B1**: A first term of $3 \text{e}^{-1}$, or any equivalent such as $\frac{3}{\text{e}}$.
> 
> **B1**: A common ratio of $\text{e}^{-2}$, or any equivalent such as $\frac{1}{\text{e}^{2}}$.
> 
> **M1**: Uses the correct sum to infinity formula with your values of $a$ and $r$.
> 
> **M1**: A correct attempt to clear the negative indices, by multiplying the top and the bottom by $\text{e}^{2}$ or by an equivalent manipulation of the fraction.
> 
> **A1**: $\frac{3\text{e}}{\text{e}^{2}-1}$, so $a = 3$ and $b = 2$.
> 
> The two values do not have to be written out separately. A correct final expression in the required form earns the last mark on its own.
> 
> Finding the common ratio by dividing the third term by the second, or by comparing the general term with $a r^{n-1}$, is equally acceptable.

> **[exam-tip]**
> An $n$th term written as a power is a geometric series in disguise.
> 
> - Substituting $n = 1$ and $n = 2$ is the quickest way to get the first term and the ratio
> - Writing $3 \text{e}^{1-2n}$ as `3 \text{e} \times \left(\text{e}^{- 2}\right)^{n}` also shows the ratio is $\text{e}^{-2}$, if you prefer to see it algebraically
> 
> Take care with the index when $n = 2$.
> 
> - `1 - 2 \left(2\right) = - 3`, so the second term is $3 \text{e}^{-3}$ and not $3 \text{e}^{-2}$
> 
> The printed form tells you what to do with the negative indices.
> 
> - $\frac{a\text{e}}{\text{e}^{b}-1}$ has no negative powers, so multiplying the top and the bottom by $\text{e}^{2}$ is the step being asked for
> - Leaving the answer as $\frac{3\text{e}^{-1}}{1-\text{e}^{-2}}$ is correct but does not answer the question
> 
> Check that the series really converges before using the formula.
> 
> - $\text{e}^{-2}$ is about $0 . 135$, which lies between $- 1$ and 1, so the sum to infinity exists

## Q3 — medium — 11 marks · exam-questions

### 8((a)) — 4 marks
Write the expression using index notation, so that the binomial series formula can be applied

`\frac{3}{\sqrt{1 - 2 x}} = 3 \left(1 - 2 x\right)^{- \frac{1}{2}}`

**[B1]**

The constant term inside the bracket is already 1, so the formula can be applied directly

- Keep the factor of 3 outside the bracket until the last step

Use the binomial series formula from the formula sheet with $n = - \frac{1}{2}$, substituting $- 2 x$ everywhere that $x$ appears

`3 \left(1 - 2 x\right)^{- \frac{1}{2}} = 3 \left[1 + \left(- \frac{1}{2}\right) \left(- 2 x\right) + \frac{\left(- \frac{1}{2}\right) \left(- \frac{3}{2}\right)}{2 !} \left(- 2 x\right)^{2} + \frac{\left(- \frac{1}{2}\right) \left(- \frac{3}{2}\right) \left(- \frac{5}{2}\right)}{3 !} \left(- 2 x\right)^{3} + \ldots\right]`

**[M1 A1]**

Now simplify each term in turn

- Take care with the signs, and remember that the power applies to the whole of $- 2 x$

`\left(- \frac{1}{2}\right) \left(- 2 x\right) = x`

`\frac{\left(- \frac{1}{2}\right) \left(- \frac{3}{2}\right)}{2 !} \left(- 2 x\right)^{2} = \frac{3}{2} x^{2}`

`\frac{\left(- \frac{1}{2}\right) \left(- \frac{3}{2}\right) \left(- \frac{5}{2}\right)}{3 !} \left(- 2 x\right)^{3} = \frac{5}{2} x^{3}`

This gives the expansion inside the bracket

`3 \left(1 - 2 x\right)^{- \frac{1}{2}} = 3 \left[1 + x + \frac{3}{2} x^{2} + \frac{5}{2} x^{3} + \ldots\right]`

Finally multiply every term inside the bracket by 3

$\frac{3}{\sqrt{1-2x}} = 3 + 3 x + \frac{9}{2} x^{2} + \frac{15}{2} x^{3}$

**[A1]**

> **[mark-scheme]**
> **B1**: Writes the expression in index form as `3 \left(1 - 2 x\right)^{- \frac{1}{2}}`.
> 
> **M1**: Uses the binomial series formula with $n = - \frac{1}{2}$, substituting $- 2 x$ in place of $x$. The structure of at least the first three terms must be correct.
> 
> **A1**: Correct unsimplified expansion, including the factor of 3.
> 
> **A1**: Fully simplified answer $3 + 3 x + \frac{9}{2} x^{2} + \frac{15}{2} x^{3}$. Accept $4 . 5 x^{2}$ for $\frac{9}{2} x^{2}$ and $7 . 5 x^{3}$ for $\frac{15}{2} x^{3}$.

> **[exam-tip]**
> The binomial series formula is given on the formula sheet, so you do not need to memorise it, but you do need to substitute into it accurately.
> 
> - The commonest slip is substituting $x$ where the whole of $- 2 x$ belongs, which loses both the sign and the powers of 2
> 
> Raise the whole bracket to the power each time, so `\left(- 2 x\right)^{2} = 4 x^{2}` and `\left(- 2 x\right)^{3} = - 8 x^{3}`.
> 
> - Two negatives multiply to give a positive, so check the sign of every coefficient as you go

### 8((b)) — 1 marks
The binomial series formula is valid only when the quantity substituted in place of $x$ has modulus less than 1

Here that quantity is $- 2 x$, not $x$ itself

`\left|- 2 x\right| < 1`

Divide both sides by 2

`\left|x\right| < \frac{1}{2}`

Write this as a range of values

$- \frac{1}{2} < x < \frac{1}{2}$

**[B1]**

> **[mark-scheme]**
> **B1**: States $- \frac{1}{2} < x < \frac{1}{2}$. Accept the equivalent form `\left|x\right| < \frac{1}{2}`.

> **[exam-tip]**
> The validity condition applies to whatever you substituted into the formula, not to $x$ on its own.
> 
> - So start from `\left|- 2 x\right| < 1` and solve it, rather than writing down `\left|x\right| < 1`
> 
> You will need this range again in part (e), to check that the value of $x$ you choose is allowed.

### 8((c)) — 1 marks
Write $0 . 9$ as a fraction, so that the square root can be simplified

$0 . 9 = \frac{9}{10}$

Take the square root of the numerator and of the denominator separately

$\sqrt{0.9} = \frac{3}{\sqrt{10}}$

Substitute this into the left-hand side

- Dividing by a fraction is the same as multiplying by its reciprocal

$\frac{3}{\sqrt{0.9}} = 3 \times \frac{\sqrt{10}}{3}$

The threes cancel

$\frac{3}{\sqrt{0.9}} = \sqrt{10}  \text{as required}$

**[B1]**

> **[mark-scheme]**
> **B1**: Shows a complete chain from $\frac{3}{\sqrt{0.9}}$ to $\sqrt{10}$, for example by using $\sqrt{0.9} = \frac{3}{\sqrt{10}}$. The printed result must be reached with no errors seen.

> **[exam-tip]**
> Turning a decimal into a fraction is often what makes a surd simplify.
> 
> - Here $0 . 9 = \frac{9}{10}$ has a perfect square on top, which is what produces the whole number 3

### 8((d)) — 2 marks
Rationalise the denominator by multiplying the numerator and the denominator by $\sqrt{10} + 3$

- This is the denominator with the sign of the surd term reversed

$\frac{1}{\sqrt{10}-3} = \frac{1}{\sqrt{10}-3} \times \frac{\sqrt{10}+3}{\sqrt{10}+3}$

**[M1]**

Multiply out the denominator, which is a difference of two squares

`\left(\sqrt{10} - 3\right) \left(\sqrt{10} + 3\right) = 10 - 9`

That denominator is equal to 1, so the fraction simplifies immediately

$\frac{1}{\sqrt{10}-3} = \sqrt{10} + 3$

**[A1]**

so $a = 1$ and $b = 3$

> **[mark-scheme]**
> **M1**: Multiplies the numerator and the denominator by $\sqrt{10} + 3$.
> 
> **A1**: Correct answer $\sqrt{10} + 3$, that is $a = 1$ and $b = 3$.

> **[exam-tip]**
> To rationalise a denominator of the form $\sqrt{n} - k$, multiply the top and the bottom by $\sqrt{n} + k$.
> 
> - The surd terms then cancel, because `\left(\sqrt{n} - k\right) \left(\sqrt{n} + k\right) = n - k^{2}`
> 
> Here that denominator works out to exactly 1, which is why the answer comes out so cleanly.
> 
> - If your denominator is not 1, divide every term of the numerator by it

### 8((e)) — 3 marks
Parts (c) and (d) tell you what to aim for

- Part (d) gives $\frac{1}{\sqrt{10}-3} = \sqrt{10} + 3$, and part (c) gives $\sqrt{10} = \frac{3}{\sqrt{0.9}}$

So choose the value of $x$ that makes $1 - 2 x$ equal to $0 . 9$

$1 - 2 x = 0 . 9$

$x = 0 . 05$

**[B1]**

Check this value lies inside the range found in part (b), so that the expansion may be used

- $0 . 05$ lies between $- \frac{1}{2}$ and $\frac{1}{2}$

Substitute $x = 0 . 05$ into the expansion from part (a), which now approximates $\sqrt{10}$

`\sqrt{10} \approx 3 + 3 \left(0 . 05\right) + \frac{9}{2} \left(0 . 05\right)^{2} + \frac{15}{2} \left(0 . 05\right)^{3}`

**[M1]**

$\sqrt{10} \approx 3 . 1621875$

Add 3, using the result from part (d)

**Final answer:** $\frac{1}{\sqrt{10}-3} \approx 6 . 16219$** (5 d.p.)**

**[A1]**

> **[mark-scheme]**
> **B1**: Finds $x = 0 . 05$, from $1 - 2 x = 0 . 9$.
> 
> **M1**: Substitutes your value of $x$ into your expansion from part (a). Allow follow-through from an incorrect expansion in part (a).
> 
> **A1**: Correct answer $6 . 16219$. Accept answers which round to this value.

> **[exam-tip]**
> The word "hence" means you must use your earlier answers rather than start again.
> 
> - Work backwards from what is asked for: part (d) turns it into $\sqrt{10} + 3$, and part (c) turns $\sqrt{10}$ into something your expansion can produce
> 
> Always check that your chosen value of $x$ lies inside the valid range before you substitute.
> 
> - If it does not, the approximation is not reliable, and it usually means something has gone wrong earlier

## Q4 — medium — 8 marks · exam-questions

### 3((a)) — 3 marks
Write out the first few terms to see what kind of series this is

- Putting $r = 1 , 2 , 3$ into $5 r - 3$ gives $2$, $7$, $12$
- Each term is 5 more than the one before, so this is an arithmetic series

Identify the first term and the common difference

$a = 2 , d = 5$

**[B1]**

Use the sum formula for an arithmetic series, `S_{n} = \frac{n}{2} \left[2 a + \left(n - 1\right) d\right]`

`\sum_{r = 1}^{n} \left(5 r - 3\right) = \frac{n}{2} \left[2 \left(2\right) + \left(n - 1\right) 5\right]`

**[M1]**

Simplify inside the bracket

`= \frac{n}{2} \left(4 + 5 n - 5\right)`

`\sum_{r = 1}^{n} \left(5 r - 3\right) = \frac{n}{2} \left(5 n - 1\right) \textrm{ } \text{as required}`

**[A1]**

> **[mark-scheme]**
> **B1**: Identifies $a = 2$ and $d = 5$, either stated or clearly used.
> 
> **M1**: Uses a correct arithmetic sum formula with your values of $a$ and $d$.
> 
> **A1**: Reaches the printed result with no errors seen.
> 
> The standard results route is equally acceptable and is marked like this: splitting the sum as `5 \sum_{r = 1}^{n} r - 3 \sum_{r = 1}^{n} 1` earns the first mark, using `\sum_{r = 1}^{n} r = \frac{n}{2} \left(n + 1\right)` earns the method mark, and reaching $\frac{5n^{2}-n}{2}$ and factorising it to the printed form earns the accuracy mark.
> 
> Because the result is printed, at least one correct intermediate line has to be shown. Jumping from the formula straight to the answer does not earn the accuracy mark.

> **[exam-tip]**
> A sum of a linear expression in $r$ is always an arithmetic series.
> 
> - The coefficient of $r$ is the common difference, so $d = 5$ can be read straight off
> - Substituting $r = 1$ gives the first term, so $a = 2$
> 
> Two routes are available and both are fully accepted.
> 
> - The arithmetic sum formula is quicker here
> - Splitting into $5 \sum r - 3 \sum 1$ works just as well if you prefer standard results
> 
> On a show that question, the last line has to be reached rather than written down.
> 
> - Show the bracket before it is tidied, so the $4 + 5 n - 5$ step is visible

### 3((b)) — 2 marks
The sum you want starts at $r = 31$, but the formula from part (a) always starts at $r = 1$

- Summing to 60 and then subtracting the sum to 30 leaves exactly the terms from 31 to 60

`\sum_{r = 31}^{60} \left(5 r - 3\right) = \frac{60}{2} \left(5 \times 60 - 1\right) - \frac{30}{2} \left(5 \times 30 - 1\right)`

**[M1]**

Work out each bracket, giving $30 \times 299$ and $15 \times 149$

$= 8970 - 2235$

`\sum_{r = 31}^{60} \left(5 r - 3\right) = 6735`

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the result from part (a) with $n = 60$ and $n = 30$ and subtracts, or an equivalent complete method.
> 
> **A1**: $6735$.
> 
> Treating the terms from 31 to 60 as an arithmetic series in their own right is equally acceptable and is marked in the same way. There are 30 terms, the first is $5 \times 31 - 3 = 152$ and the last is $5 \times 60 - 3 = 297$, so `\frac{30}{2} \left(152 + 297\right) = 6735`.
> 
> Using the arithmetic sum formula twice from first principles rather than the part (a) result is also accepted.

> **[exam-tip]**
> Subtracting sums is the standard way to shift a starting value.
> 
> - The sum from 31 to 60 is the sum to 60 minus the sum to 30
> - Subtracting the sum to 31 instead is the classic error, because that removes the $r = 31$ term you want to keep
> 
> Count the terms if you use the direct route.
> 
> - From 31 to 60 inclusive there are $60 - 31 + 1 = 30$ terms, not 29
> 
> The word "evaluate" means a number is wanted.
> 
> - Leaving the answer as a difference of two expressions does not finish the job

### 3((c)) — 3 marks
Set the result from part (a) equal to the given total

`\frac{n}{2} \left(5 n - 1\right) = 3783`

Multiply both sides by 2 and expand

$5 n^{2} - n = 7566$

Collect everything on one side to get a quadratic in $n$

$5 n^{2} - n - 7566 = 0$

**[M1]**

Factorise, looking for two numbers multiplying to `5 \times \left(- 7566\right)` and adding to $- 1$

- Those numbers are $194$ and $- 195$, which gives the factors below

`\left(5 n + 194\right) \left(n - 39\right) = 0`

**[M1]**

Setting each factor to zero gives $n = - \frac{194}{5}$ or $n = 39$

$n$ counts terms, so it must be a positive whole number and the negative fraction is rejected

$n = 39$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets the result of part (a) equal to $3783$ and rearranges to a three-term quadratic in $n$.
> 
> **M1**: A complete and correct method for solving that quadratic, by factorising, completing the square or the quadratic formula.
> 
> **A1**: $n = 39$.
> 
> The quadratic formula gives a discriminant of $151321$, whose square root is exactly $389$, so the roots come out exactly either way.
> 
> The negative root does not have to be written down or explicitly rejected for the accuracy mark, but $n = 39$ must be the value given as the answer.

> **[exam-tip]**
> Using part (a) turns a sum into an ordinary quadratic equation.
> 
> - There is no need to write out any terms, and no need to guess and check
> 
> The numbers look forbidding but the quadratic does factorise.
> 
> - If you cannot spot the factors quickly, go straight to the formula
> - $1 + 4 \times 5 \times 7566 = 151321$ and $389^{2} = 151321$, so the root is exact
> 
> Always sanity-check the answer against what $n$ means.
> 
> - $n$ is a number of terms, so a negative or fractional value is discarded without comment
> - Substituting back, $\frac{39}{2} \times 194 = 3783$, which confirms it

## Q5 — medium — 12 marks · exam-questions

### 8((a)) — 4 marks
Write each statement using the first term $a$ and the common ratio $r$

The first two terms are $a$ and $a r$

$a + a r = 400$

**[B1]**

The second and third terms are $a r$ and $a r^{2}$

$a r + a r^{2} = 100$

**[B1]**

Look at the second equation next to the first

- Taking a factor of $r$ out of $a r + a r^{2}$ leaves $a + a r$, which is exactly the left hand side of the first equation

`r \left(a + a r\right) = 100`

**[M1]**

The bracket is worth 400, so replace it

$400 r = 100$

$r = \frac{1}{4}  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **B1**: A correct equation from the first and second terms, $a + a r = 400$ or an equivalent.
> 
> **B1**: A correct equation from the second and third terms, $a r + a r^{2} = 100$ or an equivalent.
> 
> **M1**: A complete method to eliminate $a$ and reach a value for $r$. Taking a factor of $r$ out of the second equation, dividing one equation by the other, or substituting $a = \frac{400}{1+r}$ into the second all count. One processing error is allowed.
> 
> **A1**: Reaches $r = \frac{1}{4}$ with no errors seen.
> 
> The substitution route is equally acceptable and is marked in the same way. There $a = \frac{400}{1+r}$ gives $4 r^{2} + 3 r - 1 = 0$, which factorises as `\left(4 r - 1\right) \left(r + 1\right) = 0`, and $r = - 1$ is rejected because it would make the first two terms cancel to zero rather than 400.
> 
> Working in terms of $a$ instead, by writing $r = \frac{400-a}{a}$, is also accepted and leads to $a = 320$ and then $r = \frac{1}{4}$.
> 
> Because the value of $r$ is printed in the question, the working has to reach it rather than assume it.

> **[exam-tip]**
> Look for the earlier expression hiding inside the later one.
> 
> - $a r + a r^{2}$ is just $r$ times $a + a r$, so the whole of the first equation can be substituted in one step
> - Spotting that turns four marks into about two lines of work
> 
> Dividing one equation by the other does the same job.
> 
> - $\frac{ar+ar^{2}}{a+ar} = \frac{100}{400}$ cancels to $r = \frac{1}{4}$ immediately
> 
> If you go the long way round, watch for the second root.
> 
> - Substituting for $a$ gives $4 r^{2} + 3 r - 1 = 0$, whose roots are $\frac{1}{4}$ and $- 1$
> - $r = - 1$ has to be rejected, since it would make the first two terms add to zero, not 400
> 
> A printed answer means the working is what earns the marks.
> 
> - Writing $r = \frac{1}{4}$ with nothing before it scores nothing at all here

### 8((b)) — 2 marks
Go back to the equation for the first two terms, and take out a factor of $a$

`a \left(1 + r\right) = 400`

Substitute the value of $r$ found in part (a)

`a \left(1 + \frac{1}{4}\right) = 400`

**[M1]**

The bracket is $\frac{5}{4}$, so divide 400 by $\frac{5}{4}$, which is the same as multiplying by $\frac{4}{5}$

$a = 400 \times \frac{4}{5}$

$a = 320  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitutes $r = \frac{1}{4}$ into either of the equations from part (a), or into the sum of the first two terms written another way.
> 
> **A1**: Reaches 320 with no errors seen.
> 
> Any of the three starting points is equally acceptable: $\frac{400}{1+\frac{1}{4}}$, `\frac{100}{\frac{1}{4} + \left(\frac{1}{4}\right)^{2}}` using the second and third terms, or `\frac{300}{1 - \left(\frac{1}{4}\right)^{2}}` using the difference of the two given sums.
> 
> Because the value of $a$ is printed in the question, the working has to reach it rather than assume it.

> **[exam-tip]**
> Any of the equations from part (a) will do, so pick the one with the smallest numbers.
> 
> - `a \left(1 + \frac{1}{4}\right) = 400` is the simplest, since it uses the first two terms directly
> 
> Dividing by a fraction means multiplying by its reciprocal.
> 
> - $400 \div \frac{5}{4}$ is $400 \times \frac{4}{5}$, which is 320
> - Multiplying by $\frac{5}{4}$ instead gives 500, which is the classic slip here
> 
> Check against the other equation.
> 
> - With $a = 320$ and $r = \frac{1}{4}$ the second and third terms are 80 and 20, which add to 100

### 8((c)) — 2 marks
The common ratio is $\frac{1}{4}$, which lies between $- 1$ and 1, so the series converges and a sum to infinity exists

Use $S_{\infty} = \frac{a}{1-r}$ with the values from parts (a) and (b)

$S_{\infty} = \frac{320}{1-\frac{1}{4}}$

**[M1]**

The bottom is $\frac{3}{4}$, and dividing by $\frac{3}{4}$ is the same as multiplying by $\frac{4}{3}$

$S_{\infty} = 320 \times \frac{4}{3}$

$S_{\infty} = \frac{1280}{3}$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the correct sum to infinity formula with $a = 320$ and $r = \frac{1}{4}$.
> 
> **A1**: $\frac{1280}{3}$, or a decimal of $426 . 67$ or better.
> 
> An exact answer is preferred, but a decimal given to at least this accuracy is accepted.

> **[exam-tip]**
> Both values needed here are given to you in the question itself.
> 
> - Parts (a) and (b) print $r = \frac{1}{4}$ and $a = 320$, so this part is available even if the earlier working went wrong
> 
> Leave the answer as a fraction where it does not terminate.
> 
> - $\frac{1280}{3}$ is exact, whereas $426 . 7$ has been rounded
> - The next part compares $S_{n}$ with $426 . 6$, which is only just below this total, so precision matters
> 
> The sum to infinity is the ceiling the running total creeps up to.
> 
> - Every $S_{n}$ is below $\frac{1280}{3}$, which is about $426 . 67$, and that is why part (d) has an answer at all

### 8((d)) — 4 marks
Write the sum to $n$ terms using `S_{n} = \frac{a \left(1 - r^{n}\right)}{1 - r}` and set up the inequality

`\frac{320 \left(1 - \left(\frac{1}{4}\right)^{n}\right)}{1 - \frac{1}{4}} > 426 . 6`

**[M1]**

The fraction in front simplifies, since $320$ divided by $\frac{3}{4}$ is $\frac{1280}{3}$

`\frac{1280}{3} \left(1 - \left(\frac{1}{4}\right)^{n}\right) > 426 . 6`

Multiply both sides by $\frac{3}{1280}$, which is positive so the inequality is unchanged

`1 - \left(\frac{1}{4}\right)^{n} > \frac{1279 . 8}{1280}`

Rearranging leaves the power on its own

`\left(\frac{1}{4}\right)^{n} < \frac{1}{6400}`

**[M1]**

Take logarithms of both sides, then use the power law to bring $n$ down

`n \text{log} \left(\frac{1}{4}\right) < \text{log} \left(\frac{1}{6400}\right)`

**[M1]**

Divide both sides by `\text{log} \left(\frac{1}{4}\right)`

- That value is negative, so dividing by it reverses the inequality sign

`n > \frac{\text{log} \left(\frac{1}{6400}\right)}{\text{log} \left(\frac{1}{4}\right)}`

$n > 6 . 32 \dots$

$n$ counts terms, so it must be a whole number, and the least whole number greater than $6 . 32 \dots$ is 7

$n = 7$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses a correct formula for the sum of a geometric series to set up an inequality or equation in $n$, using $a = 320$ and $r = \frac{1}{4}$.
> 
> **M1**: Simplifies to the form `\left(\frac{1}{4}\right)^{n} < \frac{1}{6400}`, or an equivalent such as $4^{n} > 6400$. Errors in simplification are allowed, and $<$, $>$ or $=$ are all accepted at this stage. This mark depends on the previous one.
> 
> **M1**: Takes logarithms of both sides correctly, in any base, and uses the power law to bring the index down. Solving directly with a base $\frac{1}{4}$ logarithm is equally acceptable. This mark depends on both previous method marks.
> 
> **A1**: $n = 7$.
> 
> The inequality does not have to have been reversed at the earlier stages, but the final answer must be the least value that satisfies it. A final answer of 7 implies the reversal was handled correctly.
> 
> Reaching $n = 7$ by trial, without logarithms, does not earn the marks, because the question says to use logarithms.

> **[exam-tip]**
> Dividing an inequality by a negative number flips it.
> 
> - `\text{log} \left(\frac{1}{4}\right)` is negative, so `n \text{log} \left(\frac{1}{4}\right) < \text{log} \left(\frac{1}{6400}\right)` becomes $n > 6 . 32 \dots$
> - Forgetting to flip gives $n < 6 . 32 \dots$ and an answer of 6, which is the commonest error in this question
> 
> Turning the fractions upside down avoids the negative logarithm altogether.
> 
> - `\left(\frac{1}{4}\right)^{n} < \frac{1}{6400}` is the same as $4^{n} > 6400$
> - Then $n \text{log} 4 > \text{log} 6400$, and $\text{log} 4$ is positive, so nothing needs reversing
> 
> "Least value of $n$" means round up, never to the nearest whole number.
> 
> - $n > 6 . 32 \dots$ gives $n = 7$, and rounding $6 . 32$ down to 6 would not satisfy the inequality
> 
> Check the two neighbouring values.
> 
> - `\left(\frac{1}{4}\right)^{6}` is about $0 . 000244$, which is bigger than $\frac{1}{6400}$, so 6 fails
> - `\left(\frac{1}{4}\right)^{7}` is about $0 . 000061$, which is smaller, so 7 works

## Q6 — medium — 13 marks · exam-questions

### 2((a)) — 5 marks
Write every term named in the question using the first term $a$ and the common difference $d$

- The fifth, sixth and seventh terms are $a + 4 d$, $a + 5 d$ and $a + 6 d$
- The first and second terms are $a$ and $a + d$

Now turn "is nine times" into an equation, with the nine multiplying the smaller sum

`\left(a + 4 d\right) + \left(a + 5 d\right) + \left(a + 6 d\right) = 9 \left(a + a + d\right)`

**[M1]**

Collect the like terms on each side

$3 a + 15 d = 18 a + 9 d$

Gather the $a$ terms on one side and the $d$ terms on the other

$6 d = 15 a$

Both sides divide by 3

$2 d = 5 a$

The third term gives a second equation

$a + 2 d = 12$

**[B1]**

Rearrange this one to make $a$ the subject, then substitute it into $2 d = 5 a$

$a = 12 - 2 d$

`2 d = 5 \left(12 - 2 d\right)`

**[M1]**

Expand the bracket and collect the terms in $d$

$2 d = 60 - 10 d$

$12 d = 60$

$d = 5$

**[A1]**

Substitute back into $a = 12 - 2 d$

$a=2,d=5$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses `a + \left(n - 1\right) d` to form an equation from the statement that the fifth, sixth and seventh terms together are nine times the first two together.
> 
> **B1**: The correct equation from the third term, $a + 2 d = 12$.
> 
> **M1**: Attempts to solve the two equations simultaneously, eliminating one variable.
> 
> **A1**: $d = 5$.
> 
> **A1**: $a = 2$.
> 
> The first equation may be left in any correct form, so $3 a + 15 d = 18 a + 9 d$, $15 a = 6 d$ and $5 a = 2 d$ are all accepted.
> 
> Noticing that the fifth, sixth and seventh terms add to three times the sixth term is equally acceptable, giving `3 \left(a + 5 d\right) = 9 \left(2 a + d\right)` and the same equation after simplifying.
> 
> The two accuracy marks are independent, so a correct value for one of $a$ and $d$ earns its mark even if the other is wrong.

> **[exam-tip]**
> Put the multiplier on the correct side of the equation.
> 
> - The larger sum is nine times the smaller, so the 9 multiplies the first and second terms
> - Writing `9 \left(a + 4 d + a + 5 d + a + 6 d\right) = a + a + d` has it the wrong way round and loses the method mark
> 
> Count the steps carefully when writing each term.
> 
> - The fifth term is $a + 4 d$, not $a + 5 d$, because it takes four steps of $d$ to reach it
> 
> The third term gives you the second equation, and it is only worth one mark, so bank it early.
> 
> - $a + 2 d = 12$ takes one line and is independent of everything else
> 
> Check both statements once you have your values.
> 
> - With $a = 2$ and $d = 5$ the fifth, sixth and seventh terms are 22, 27 and 32, which add to 81
> - The first two terms are 2 and 7, which add to 9, and nine times 9 is 81

### 2((b)) — 4 marks
The sum you want starts at $r = 15$, but the sum formula always starts at the first term

- Summing to 60 and then subtracting the sum to 14 leaves exactly the terms from 15 to 60

Work out the sum to 60 terms first, using $a = 2$ and $d = 5$ from part (a)

`S_{60} = \frac{60}{2} \left[2 \left(2\right) + \left(60 - 1\right) 5\right]`

`S_{60} = 30 \left(299\right)`

$S_{60} = 8970$

**[M1]**

Now the sum to 14 terms

`S_{14} = \frac{14}{2} \left[2 \left(2\right) + \left(14 - 1\right) 5\right]`

`S_{14} = 7 \left(69\right)`

$S_{14} = 483$

**[M1]**

Subtract the second total from the first

`\sum_{r = 15}^{60} u_{r} = 8970 - 483`

**[M1]**

`\sum_{r = 15}^{60} u_{r} = 8487`

**[A1]**

> **[mark-scheme]**
> **M1**: Uses a correct sum formula with $n = 60$ and your values of $a$ and $d$.
> 
> **M1**: Uses a correct sum formula with $n = 14$, or finds the 14th term, with your values of $a$ and $d$.
> 
> **M1**: Subtracts the two totals the correct way round. This mark depends on both previous method marks.
> 
> **A1**: $8487$.
> 
> The first plus last route is equally acceptable. There the 15th term is 72 and the 60th is 297, and `\frac{46}{2} \left(72 + 297\right) = 8487`, with the first two method marks earned for those two terms.
> 
> Treating the terms from 15 to 60 as a series in their own right is also accepted: `\frac{46}{2} \left(2 \times 72 + \left(46 - 1\right) 5\right) = 8487`. This route needs the 15th term found first, and using 45 terms rather than 46 still earns the method marks.

> **[exam-tip]**
> Subtracting sums is the standard way to shift a starting value.
> 
> - The sum from 15 to 60 is the sum to 60 minus the sum to 14
> - Subtracting the sum to 15 instead is the classic error, because that removes the $r = 15$ term you want to keep
> 
> Count the terms if you use the direct route.
> 
> - From 15 to 60 inclusive there are $60 - 15 + 1 = 46$ terms, not 45
> 
> Keep the two totals visible.
> 
> - Writing 8970 and 483 down separately makes the subtraction easy to check
> - It also means a slip in one of them does not hide the method

### 2((c)) — 4 marks
Write both parts of the given equation in terms of $n$, using $a = 2$ and $d = 5$ from part (a)

- The sum to $n$ terms is `\frac{n}{2} \left[2 \left(2\right) + \left(n - 1\right) 5\right]`
- The $n$th term is `2 + \left(n - 1\right) 5`, which simplifies to $5 n - 3$

Substitute both into $2 S_{n} - 5 u_{n} = 10$

`2 \times \frac{n}{2} \left[2 \left(2\right) + \left(n - 1\right) 5\right] - 5 \left(5 n - 3\right) = 10`

**[M1]**

The 2 outside cancels with the 2 underneath, and the square bracket simplifies to $5 n - 1$

`n \left(5 n - 1\right) - 5 \left(5 n - 3\right) = 10`

Expand both brackets, taking care that $- 5 \times - 3$ gives $+ 15$

$5 n^{2} - n - 25 n + 15 = 10$

Collect the terms and move the 10 across

$5 n^{2} - 26 n + 5 = 0$

**[A1]**

Factorise, looking for two numbers multiplying to $5 \times 5 = 25$ and adding to $- 26$

- Those numbers are $- 1$ and $- 25$

`\left(5 n - 1\right) \left(n - 5\right) = 0`

**[M1]**

Setting each bracket to zero gives $n = \frac{1}{5}$ or $n = 5$

$n$ counts terms, so it must be a positive whole number and the fraction is rejected

$n = 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitutes a correct sum formula and a correct $n$th term, both with your values of $a$ and $d$, into $2 S_{n} - 5 u_{n} = 10$.
> 
> **A1**: The correct three term quadratic, $5 n^{2} - 26 n + 5 = 0$ or any equivalent.
> 
> **M1**: A complete and correct method for solving that quadratic, by factorising, completing the square or the quadratic formula.
> 
> **A1**: $n = 5$.
> 
> The method marks follow through from your values of $a$ and $d$ in part (a).
> 
> The root $n = \frac{1}{5}$ does not have to be written down or explicitly rejected, but $n = 5$ must be the value given as the answer, since $n$ is a whole number of terms.

> **[exam-tip]**
> Simplify the sum formula before multiplying anything out.
> 
> - The 2 in front cancels with the 2 underneath straight away, leaving `n \left(5 n - 1\right)`
> - Expanding `\frac{n}{2} \left[4 + 5 n - 5\right]` first and then doubling it works too, but creates fractions on the way
> 
> Watch the two minus signs meeting.
> 
> - `- 5 \left(5 n - 3\right)` is $- 25 n + 15$
> - Writing $- 25 n - 15$ shifts the constant by 30 and the quadratic will not factorise
> 
> This quadratic has a fractional root, which is a useful check.
> 
> - $5 n^{2} - 26 n + 5 = 0$ gives $n = \frac{1}{5}$ and $n = 5$, and their product is 1
> - Only whole numbers count as positions in a series, so the fraction is discarded
> 
> Substitute back to be sure.
> 
> - With $n = 5$ the sum is $S_{5} = 60$ and the fifth term is $u_{5} = 22$, and $2 \times 60 - 5 \times 22 = 10$

## Q7 — medium — 16 marks · exam-questions

### 7((a)) — 2 marks
The factor theorem says `\left(4 x - 1\right)` is a factor exactly when `\text{f} \left(x\right)` is zero at the value of $x$ that makes the bracket zero

Solve $4 x - 1 = 0$ to find which value to substitute

$x = \frac{1}{4}$

Substitute $x = \frac{1}{4}$ into `\text{f} \left(x\right)`

`64 \left(\frac{1}{4}\right)^{3} - 64 \left(\frac{1}{4}\right)^{2} + 3`

**[M1]**

Work out each term, using `\left(\frac{1}{4}\right)^{3} = \frac{1}{64}` and `\left(\frac{1}{4}\right)^{2} = \frac{1}{16}`

$1 - 4 + 3$

This comes to zero, which is exactly the condition the factor theorem needs

**Final answer:** `\text{f} \left(\frac{1}{4}\right) = 0`**, so **`\left(4 x - 1\right)`** is a factor of **`\text{f} \left(x\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Substitutes $x = \frac{1}{4}$ into `\text{f} \left(x\right)`.
> 
> **A1**: Shows the result is zero and states a conclusion, with no errors seen. A very brief conclusion is accepted.
> 
> Substituting $x = - \frac{1}{4}$ still earns the method mark, but not the accuracy mark.
> 
> Dividing `\text{f} \left(x\right)` by `\left(4 x - 1\right)` is equally acceptable, and is marked like this: a division reaching at least $16 x^{2} - 12 x$ earns the method mark, and a remainder of zero together with a conclusion earns the accuracy mark.

> **[exam-tip]**
> A factor of the form `\left(4 x - 1\right)` gives $x = \frac{1}{4}$, not $x = 1$ or $x = 4$.
> 
> - Set the bracket equal to zero and solve it every time, rather than trying to read the value off
> 
> The conclusion is worth writing, even though it feels obvious.
> 
> - The accuracy mark is for the zero and the conclusion together, so a page of correct arithmetic with no sentence at the end is not enough
> - One line such as "so `\left(4 x - 1\right)` is a factor" is all that is needed

### 7((b)) — 4 marks
Part (a) gives one factor, so write the cubic as that factor multiplied by a quadratic

`64 x^{3} - 64 x^{2} + 3 = \left(4 x - 1\right) \left(A x^{2} + B x + C\right)`

Compare the $x^{3}$ terms, which on the right come only from $4 x \times A x^{2}$

$4 A = 64$

$A = 16$

Compare the constant terms, which come only from $- 1 \times C$

$- C = 3$

$C = - 3$

Compare the $x^{2}$ terms, which come from $4 x \times B x$ and from $- 1 \times A x^{2}$

$4 B - 16 = - 64$

$B = - 12$

**[M1]**

So the equation splits into a linear factor and a quadratic factor

`\left(4 x - 1\right) \left(16 x^{2} - 12 x - 3\right) = 0`

The linear factor gives the first root straight away

$x = \frac{1}{4}$

**[B1]**

The quadratic has no factor pair, so use the quadratic formula with $a = 16$, $b = - 12$ and $c = - 3$

`x = \frac{12 \pm \sqrt{\left(- 12\right)^{2} - 4 \left(16\right) \left(- 3\right)}}{2 \left(16\right)}`

**[M1]**

Work out the number under the root, taking care that `- 4 \times 16 \times \left(- 3\right)` is positive

$x = \frac{12\pm\sqrt{336}}{32}$

Simplify the surd, since $336 = 16 \times 21$

$x = \frac{12\pm4\sqrt{21}}{32}$

Cancel the common factor of 4 from the numerator and the denominator

$x = \frac{3\pm\sqrt{21}}{8}$

Collect all three roots together

$x = \frac{1}{4} , x = \frac{3+\sqrt{21}}{8} , x = \frac{3-\sqrt{21}}{8}$

**[A1]**

> **[mark-scheme]**
> **M1**: Divides `\text{f} \left(x\right)` by `\left(4 x - 1\right)`, or compares coefficients, reaching the quadratic factor $16 x^{2} - 12 x - 3$.
> 
> **M1**: A fully correct method for solving that quadratic. This mark is only available once the first method mark has been earned.
> 
> **B1**: $x = \frac{1}{4}$, or any equivalent value.
> 
> **A1**: $x = \frac{3\pm\sqrt{21}}{8}$, or any equivalent exact form.
> 
> If you compare coefficients, a correct comparison must be written down and followed by an attempt to find the constant term. Correct solutions of a correct quadratic imply the second method mark.
> 
> The question asks for exact roots, so decimal values do not earn the final accuracy mark. An unsimplified $\frac{12\pm4\sqrt{21}}{32}$ is accepted.

> **[exam-tip]**
> "Exact" is an instruction about the form of the answer, not just its accuracy.
> 
> - Leave the surd alone rather than reaching for the calculator
> - $0 . 948$ and $- 0 . 198$ are the same numbers, but they earn nothing here
> 
> Simplify the surd before you cancel, not after.
> 
> - $336 = 16 \times 21$, so $\sqrt{336}$ becomes $4 \sqrt{21}$, and only then does the 4 cancel with the 32
> - Cancelling straight from $\frac{12\pm\sqrt{336}}{32}$ is where marks get thrown away, because the $\sqrt{336}$ has no factor of 4 visible
> 
> Watch the double negative inside the square root.
> 
> - `- 4 \times 16 \times \left(- 3\right) = + 192`, so the discriminant is $144 + 192$, not $144 - 192$

### 7((c)) — 3 marks
Turn each piece of information into an equation, using the standard geometric series formulas

- The $n$th term is $a r^{n-1}$, so the third term is $a r^{2}$
- The sum to infinity is $\frac{a}{1-r}$

$a r^{2} = 9$

$\frac{a}{1-r} = 192$

**[B1]**

The target equation contains only $r$, so eliminate $a$ between the two equations

Rearranging the second one gives $a$ in terms of $r$

`a = 192 \left(1 - r\right)`

Substitute that into the first equation

`192 \left(1 - r\right) r^{2} = 9`

**[M1]**

Expand the left-hand side

$192 r^{2} - 192 r^{3} = 9$

Every term divides by 3, which brings the numbers down to the size in the printed equation

$64 r^{2} - 64 r^{3} = 3$

Collect everything on the side that makes the $r^{3}$ term positive

$64 r^{3} - 64 r^{2} + 3 = 0  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **B1**: Either correct equation, $a r^{2} = 9$ or $\frac{a}{1-r} = 192$, or an equivalent form.
> 
> **M1**: Both equations correct, together with any correct step that eliminates $a$.
> 
> **A1**: A fully correct solution with no errors, showing at least one correct intermediate line leading to the printed equation.
> 
> Eliminating $r$ the other way round is equally acceptable, so substituting $a = \frac{9}{r^{2}}$ into the sum to infinity earns the method mark in the same way.
> 
> Because the equation is printed in the question, the accuracy mark needs every line to be correct. Jumping straight from the substitution to the answer does not show the intermediate line the mark requires.

> **[exam-tip]**
> Two facts about a geometric series almost always mean two equations and an elimination.
> 
> - Write both equations down before doing anything else, since one of the marks is just for having them
> - The equation you are heading for tells you which letter to get rid of, and here it contains no $a$
> 
> Make $a$ the subject of the simpler equation.
> 
> - $\frac{a}{1-r} = 192$ rearranges in one step to `a = 192 \left(1 - r\right)`, with no fraction left to carry
> 
> On a show that question, dividing through at the right moment saves you from large numbers.
> 
> - The printed equation has 64 rather than 192 in it, which is the hint that a division by 3 is coming

### 7((d)) — 1 marks
Part (c) shows that $r$ satisfies $64 r^{3} - 64 r^{2} + 3 = 0$, and part (b) has already solved that equation

So $r$ must be one of the three roots found there

Two of those roots contain $\sqrt{21}$, which is irrational, so neither of them can be the value wanted

$r = \frac{1}{4}$

**[B1]**

> **[mark-scheme]**
> **B1**: $r = \frac{1}{4}$, or an equivalent value such as $0 . 25$.
> 
> The command word is "write down", so no working is required and none is expected.

> **[exam-tip]**
> The word "rational" is doing all the work in this part.
> 
> - A rational number can be written as one integer over another, and $\frac{1}{4}$ is the only root that can
> - $\sqrt{21}$ is irrational, so any root containing it is ruled out
> 
> It is worth noticing what does not decide it here.
> 
> - A sum to infinity exists only when `\left|r\right| < 1`, but all three roots satisfy that, since they are about $0 . 25$, $0 . 948$ and $- 0 . 198$
> - So the condition you need is the one you are given, not the convergence condition

### 7((e)) — 2 marks
Now that $r$ is known, either of the equations from part (c) will give $a$

The third term equation is the quicker one, because there is no bracket to expand

`a \left(\frac{1}{4}\right)^{2} = 9`

**[M1]**

Work out the square

$\frac{a}{16} = 9$

Multiply both sides by 16

$a = 144  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitutes your value of $r$ correctly into either equation from part (c) in order to find $a$.
> 
> **A1**: $a = 144$, from working containing no errors.
> 
> Using the sum to infinity is equally acceptable and is marked in the same way, with $\frac{a}{1-\frac{1}{4}} = 192$ earning the method mark.
> 
> Because the value is printed in the question, the accuracy mark needs completely correct working. Simply asserting $a = 144$ with no substitution shown earns nothing.

> **[exam-tip]**
> When either equation will do, pick the one with the simpler arithmetic.
> 
> - $a r^{2} = 9$ needs one square and one multiplication
> - $\frac{a}{1-r} = 192$ needs a subtraction inside a denominator first
> 
> Use the other equation as a check, since it costs one line.
> 
> - $1 - \frac{1}{4} = 0 . 75$, and $144 \div 0 . 75$ gives 192, which confirms the value

### 7((f)) — 4 marks
The sum to $n$ terms of a geometric series is `S_{n} = \frac{a \left(1 - r^{n}\right)}{1 - r}`

Substitute $a = 144$ and $r = 0 . 25$, and write the condition as an inequality

`\frac{144 \left(1 - 0 . 25^{n}\right)}{1 - 0 . 25} > 191 . 9`

**[M1]**

The denominator is $0 . 75$, and $144 \div 0 . 75 = 192$

`192 \left(1 - 0 . 25^{n}\right) > 191 . 9`

Divide both sides by 192, which is positive so the inequality is unchanged

$1 - 0 . 25^{n} > \frac{1919}{1920}$

Rearrange to leave the power on its own

- Subtracting 1 and then multiplying by $- 1$ reverses the inequality sign

$0 . 25^{n} < \frac{1}{1920}$

**[M1]**

Take logarithms of both sides, then use the power law to bring $n$ down in front

$n \text{log} 0 . 25 < \text{log} \frac{1}{1920}$

Divide by $\text{log} 0 . 25$, which is negative, so the inequality reverses again

$n > \frac{\text{log}\frac{1}{1920}}{\text{log}0.25}$

**[M1]**

Evaluate the right-hand side, which is $5 . 4534$ to 4 decimal places

$n > 5 . 4534$

$n$ counts terms, so it has to be a whole number, and the smallest whole number greater than $5 . 4534$ is 6

$n = 6$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the sum to $n$ terms formula with $a = 144$ and $r = \frac{1}{4}$, or with your own values, to set up an equation or an inequality.
> 
> **M1**: Rearranges to isolate the power, reaching $0 . 25^{n} < k$ or an equivalent form. This mark is only available once the first method mark has been earned.
> 
> **M1**: Correct use of logarithms with an attempt to evaluate them. This can be implied by a value which rounds to $5 . 5$.
> 
> **A1**: $n = 6$, reached by working with inequalities throughout and handling them without error.
> 
> Working in equations rather than inequalities is accepted for all three method marks, but not for the accuracy mark. A solution that only ever solves an equation, and then states $n = 6$, does not earn the final mark.
> 
> Any base of logarithm is accepted, so natural logarithms give the same value.

> **[exam-tip]**
> The inequality signs are worth a mark on their own, so keep them from the very first line.
> 
> - Solving the matching equation and then writing $n = 6$ loses the accuracy mark even though the answer is right
> 
> Two separate steps reverse the sign here, and missing either one gives $n < 5 . 45$ and no valid answer.
> 
> - Multiplying or dividing by a negative number reverses the inequality
> - $\text{log} 0 . 25$ is negative, because $0 . 25$ is less than 1
> 
> Round in the direction the question needs, not the usual way.
> 
> - $n > 5 . 4534$ with $n$ a whole number means $n = 6$, since 5 would not be large enough
> - Rounding $5 . 4534$ down to 5 out of habit is the single most common error on this type of question

## Q8 — medium — 5 marks · exam-questions

### 1((a)) — 3 marks
Write out the first few terms to see what kind of series this is

- Putting $r = 1 , 2 , 3$ into $3 r + 2$ gives $5$, $8$, $11$
- Each term is 3 more than the one before, so this is an arithmetic series

Identify the first term and the common difference

$a = 5 , d = 3$

**[B1]**

Use the sum formula for an arithmetic series, `S_{n} = \frac{n}{2} \left[2 a + \left(n - 1\right) d\right]`

`\sum_{r = 1}^{n} \left(3 r + 2\right) = \frac{n}{2} \left[2 \left(5\right) + \left(n - 1\right) 3\right]`

**[M1]**

Simplify inside the bracket

`= \frac{n}{2} \left(10 + 3 n - 3\right)`

`\sum_{r = 1}^{n} \left(3 r + 2\right) = \frac{n}{2} \left(3 n + 7\right) \textrm{ } \text{as required}`

**[A1]**

> **[mark-scheme]**
> **B1**: Identifies $a = 5$ and $d = 3$, either stated or clearly used.
> 
> **M1**: Uses a correct arithmetic sum formula with your values of $a$ and $d$.
> 
> **A1**: Reaches the printed result with no errors seen.
> 
> The first plus last route is equally acceptable and is marked like this: the first mark is for $a = 5$ together with a last term of $3 n + 2$, the method mark is for `\frac{n}{2} \left(5 + \left[3 n + 2\right]\right)`, and the accuracy mark is for reaching the printed form.
> 
> The standard results route is also equally acceptable: the first mark is for writing the sum as `3 \sum_{r = 1}^{n} r + 2 \sum_{r = 1}^{n} 1`, the method mark is for using `\frac{3}{2} n \left(n + 1\right) + 2 n`, and the accuracy mark is for simplifying that to the printed form.
> 
> Because the result is printed, at least one correct intermediate line has to be shown. Jumping from the formula straight to the answer does not earn the accuracy mark.

> **[exam-tip]**
> A sum of a linear expression in $r$ is always an arithmetic series.
> 
> - The coefficient of $r$ is the common difference, so $d = 3$ can be read straight off
> - Substituting $r = 1$ gives the first term, so $a = 5$
> 
> Three routes are available and all of them are fully accepted.
> 
> - The arithmetic sum formula is the most direct
> - First plus last works well because the last term, $3 n + 2$, is easy to write down
> - Splitting into $3 \sum r + 2 \sum 1$ suits you if you prefer standard results
> 
> On a show that question the last line has to be reached, not written down.
> 
> - Show the bracket before it is tidied, so the $10 + 3 n - 3$ step is visible

### 1((b)) — 2 marks
The sum you want starts at $r = 10$, but the formula from part (a) always starts at $r = 1$

- Summing to 40 and then subtracting the sum to 9 leaves exactly the terms from 10 to 40

`\sum_{r = 10}^{40} \left(3 r + 2\right) = \frac{40}{2} \left(3 \times 40 + 7\right) - \frac{9}{2} \left(3 \times 9 + 7\right)`

**[M1]**

Work out each bracket, giving $20 \times 127$ and $4 . 5 \times 34$

$= 2540 - 153$

`\sum_{r = 10}^{40} \left(3 r + 2\right) = 2387`

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the result from part (a) with $n = 40$ and $n = 9$ and subtracts. Using $n = 10$ for the second value also earns this mark, though it leads to 2355 rather than the correct total.
> 
> **A1**: $2387$.
> 
> Treating the terms from 10 to 40 as an arithmetic series in their own right is equally acceptable. There are 31 terms, the first is $3 \times 10 + 2 = 32$ and the last is $3 \times 40 + 2 = 122$, so `\frac{31}{2} \left(32 + 122\right) = 2387`. Using 30 terms instead of 31 still earns the method mark but gives 2310.
> 
> Using the arithmetic sum formula on the shifted series is also accepted: `\frac{31}{2} \left(2 \times 32 + \left(31 - 1\right) 3\right) = 2387`, with 30 again allowed for the method mark only.

> **[exam-tip]**
> Subtracting sums is the standard way to shift a starting value.
> 
> - The sum from 10 to 40 is the sum to 40 minus the sum to 9
> - Subtracting the sum to 10 instead is the classic error, because that removes the $r = 10$ term you want to keep
> 
> Count the terms if you use the direct route.
> 
> - From 10 to 40 inclusive there are $40 - 10 + 1 = 31$ terms, not 30
> 
> The word "evaluate" means a number is wanted.
> 
> - Leaving the answer as a difference of two expressions does not finish the job

## Q9 — medium — 6 marks · exam-questions

### 2() — 6 marks
Substitute $n = 1$ into the expression for the $n$th term to get the first term

`a = 8^{\left(1 - 2\right)}`

$a = 8^{-1}$

**[B1]**

Now substitute $n = 2$ to get the second term

`8^{\left(1 - 4\right)} = 8^{- 3}`

The common ratio is the second term divided by the first, and dividing powers of 8 means subtracting the indices

$r = \frac{8^{-3}}{8^{-1}}$

$r = 8^{-2}$

**[M1 A1]**

The question says the series is convergent, and $8^{-2} = \frac{1}{64}$ does lie between $- 1$ and 1, so the sum to infinity exists

Use $S_{\infty} = \frac{a}{1-r}$ with these values

$S_{\infty} = \frac{8^{-1}}{1-8^{-2}}$

**[M1]**

Write both powers as fractions so the division can be carried out

- $8^{-1} = \frac{1}{8}$ and $8^{-2} = \frac{1}{64}$
- The bottom becomes $1 - \frac{1}{64}$, which is $\frac{63}{64}$

$S_{\infty} = \frac{\frac{1}{8}}{\frac{63}{64}}$

Dividing by a fraction is the same as multiplying by its reciprocal

$S_{\infty} = \frac{1}{8} \times \frac{64}{63}$

**[M1]**

$S_{\infty} = \frac{8}{63}$

**[A1]**

so $p = 8$ and $q = 63$

> **[mark-scheme]**
> **B1**: A first term of $8^{-1}$, or any equivalent such as $\frac{1}{8}$.
> 
> **M1**: Substitutes $n = 2$ to find $a r$ and divides by $a$ to find $r$. A correct value of $r$ implies this mark.
> 
> **A1**: A common ratio of $8^{-2}$, or any equivalent such as $\frac{1}{64}$.
> 
> **M1**: Uses the correct sum to infinity formula for a convergent geometric series with your values of $a$ and $r$, provided your $r$ satisfies `\left|r\right| < 1`. The values used must be ones you have found or stated.
> 
> **M1**: A correct attempt either to use an index law to reach the required form, or to divide your two fractions. This mark depends on the previous method mark.
> 
> **A1**: $\frac{8}{63}$, so $p = 8$ and $q = 63$. Any equivalent with $p$ and $q$ integers is acceptable.
> 
> Where no working is shown, a correct substitution of your own values of $a$ and $r$, evaluated correctly, implies the second method mark. So $r = \frac{1}{4}$ with $a = \frac{1}{8}$ leading to $\frac{1}{6}$ earns both method marks but not the accuracy mark, because $\frac{1}{6}$ is correct for those values.
> 
> Reading the ratio straight off by writing $8^{1-2n}$ as `8 \times \left(8^{- 2}\right)^{n}` is equally acceptable.

> **[exam-tip]**
> An $n$th term written as a single power is a geometric series in disguise.
> 
> - Substituting $n = 1$ and $n = 2$ gives the first term and the second, and their quotient is the ratio
> 
> The index at $n = 2$ is the usual slip.
> 
> - `1 - 2 \left(2\right) = - 3`, so the second term is $8^{-3}$ and not $8^{-2}$
> - The ratio then comes out as $8^{-2}$, because `- 3 - \left(- 1\right) = - 2`
> 
> Turn the negative powers into fractions before dividing.
> 
> - $\frac{1}{8}$ divided by $\frac{63}{64}$ becomes $\frac{1}{8} \times \frac{64}{63}$, and the 8 cancels into the 64
> - Working with $\frac{8^{-1}}{1-8^{-2}}$ all the way to the end is possible but much easier to get wrong
> 
> Check the answer looks sensible.
> 
> - The first term is $0 . 125$ and the ratio is small, so a total a little above $0 . 125$ is expected, and $\frac{8}{63}$ is about $0 . 127$

## Q10 — medium — 9 marks · exam-questions

### 7((a)) — 2 marks
In a geometric series each term is the one before it multiplied by $r$, so the third term is $a r^{2}$

Dividing the third term by the first leaves $r^{2}$ on its own

$r^{2} = \frac{2704}{625} \div 16$

**[M1]**

Dividing by 16 multiplies the denominator by 16, and $625 \times 16 = 10000$

$r^{2} = \frac{2704}{10000}$

Both parts of the fraction are square numbers, since $2704 = 52^{2}$ and $10000 = 100^{2}$

Take the square root of each, remembering that a square root has two signs

$r = \pm \frac{52}{100}$

$r = \pm \frac{13}{25}$

**[A1]**

> **[mark-scheme]**
> **M1**: Divides the third term by the first to reach $r^{2}$, giving $\frac{2704}{625} \div 16$ or an equivalent.
> 
> **A1**: Both values, $r = \pm \frac{13}{25}$, or any equivalent such as $\pm 0 . 52$.
> 
> Both signs are required, because the question asks for the two possible values.
> 
> Forming and solving $16 r^{2} = \frac{2704}{625}$ is the same method written another way and is equally acceptable.

> **[exam-tip]**
> Dividing one term by another is the quickest way to isolate the ratio.
> 
> - The third term is $a r^{2}$ and the first is $a$, so the $a$ cancels and only $r^{2}$ is left
> - There is no need to find the second term first
> 
> A square root always has two values unless something rules one out.
> 
> - The question asks for two values, which is the clue that both signs are wanted here
> - Part (b) is where one of them gets ruled out
> 
> Look for square numbers before reaching for the calculator.
> 
> - $\frac{2704}{10000}$ has $52^{2}$ on top and $100^{2}$ underneath, so the root is exactly $\frac{52}{100}$
> - Cancelling by 4 gives $\frac{13}{25}$, which is the form the mark scheme uses

### 7((b)) — 2 marks
A sum to infinity only exists when $- 1 < r < 1$, and both values from part (a) satisfy that

The extra condition $r > 0$ picks out the positive one

$r = \frac{13}{25}$

Use $S_{\infty} = \frac{a}{1-r}$ with the first term 16

$S_{\infty} = \frac{16}{1-\frac{13}{25}}$

**[M1]**

The bottom is $\frac{12}{25}$, and dividing by $\frac{12}{25}$ is the same as multiplying by $\frac{25}{12}$

$S_{\infty} = 16 \times \frac{25}{12}$

$S_{\infty} = \frac{100}{3}$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the correct sum to infinity formula with the first term 16 and your positive value of $r$.
> 
> **A1**: $\frac{100}{3}$, or an equivalent exact form.
> 
> The question asks for an exact value, so a recurring decimal must be shown as recurring: $33 . 3 \dots$ or a dotted `33 . \dot{3}` are accepted, but a terminating decimal such as $33 . 3$ is not.
> 
> The method mark follows through from your value of $r$ in part (a).

> **[exam-tip]**
> The condition $r > 0$ is there to choose between your two answers, not to add work.
> 
> - Both $\frac{13}{25}$ and $- \frac{13}{25}$ would give a convergent series, so the sign has to be handed to you
> 
> Dividing by a fraction means multiplying by its reciprocal.
> 
> - $16 \div \frac{12}{25}$ is $16 \times \frac{25}{12}$, and the 4 in 16 cancels into the 12
> 
> Leave a non-terminating answer as a fraction.
> 
> - $\frac{100}{3}$ is exact; $33 . 3$ is not, and it does not earn the mark
> - If you do write a decimal, show that it recurs

### 7((c)) — 5 marks
Write the sum to $n$ terms using `S_{n} = \frac{a \left(1 - r^{n}\right)}{1 - r}`, with $a = 16$ and $r = \frac{13}{25}$

`\frac{16 \left(1 - \left(\frac{13}{25}\right)^{n}\right)}{1 - \frac{13}{25}} > 33`

**[M1]**

The fraction in front is the sum to infinity from part (b), which is $\frac{100}{3}$

`\frac{100}{3} \left(1 - \left(\frac{13}{25}\right)^{n}\right) > 33`

Multiply both sides by $\frac{3}{100}$, which is positive so the inequality is unchanged

`1 - \left(\frac{13}{25}\right)^{n} > \frac{99}{100}`

Rearranging leaves the power on its own

`\left(\frac{13}{25}\right)^{n} < 0 . 01`

**[M1]**

Take logarithms of both sides, then use the power law to bring $n$ down

`n \text{log} \left(\frac{13}{25}\right) < \text{log} \left(0 . 01\right)`

**[M1]**

Divide both sides by `\text{log} \left(\frac{13}{25}\right)`

- $\frac{13}{25}$ is less than 1, so its logarithm is negative and dividing by it reverses the inequality

`n > \frac{\text{log} \left(0 . 01\right)}{\text{log} \left(\frac{13}{25}\right)}`

$n > 7 . 04 \dots$

**[M1]**

$n$ counts terms, so it must be a whole number, and the least whole number greater than $7 . 04 \dots$ is 8

$n = 8$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses a correct formula for the sum of a geometric series to set up an inequality or equation in $n$, following through from your positive $r$ and using $a = 16$. Any of $<$, $>$ or $=$ is accepted at this stage.
> 
> **M1**: Simplifies to the form `\left(\frac{13}{25}\right)^{n} < d` for some non-zero $d$, here $0 . 01$. Errors in the simplification are allowed. This mark depends on the previous one.
> 
> **M1**: Takes logarithms of both sides correctly, in any base, and uses the power law to reach a statement of the form $n \text{log} a < \text{log} b$. Removing the power by using a logarithm to base $\frac{13}{25}$ directly is equally acceptable. This mark does not depend on the earlier marks, but the logarithms must be taken correctly.
> 
> **M1**: Reaches a value for $n$ from a correctly set up inequality, with the inequality sign reversed at the appropriate point. This mark depends on all three previous method marks. A final answer of 8 implies it even where the reversal is not shown.
> 
> **A1**: $n = 8$.
> 
> The inequality does not have to be reversed at the intermediate stages, but the final answer must be the least value that satisfies it.
> 
> Turning both fractions over first is equally acceptable and avoids the negative logarithm: `\left(\frac{25}{13}\right)^{n} > 100` leads to $n > \frac{\text{log}100}{\text{log}\frac{25}{13}}$ and the same value.
> 
> The question says to use logarithms, so reaching 8 by trying values does not earn the method marks.

> **[exam-tip]**
> Dividing an inequality by a negative number flips it.
> 
> - `\text{log} \left(\frac{13}{25}\right)` is negative, because $\frac{13}{25}$ is less than 1
> - Forgetting to flip gives $n < 7 . 04 \dots$ and an answer of 7, which is the commonest error here
> 
> Turning the fractions upside down avoids the problem completely.
> 
> - `\left(\frac{13}{25}\right)^{n} < 0 . 01` is the same as `\left(\frac{25}{13}\right)^{n} > 100`
> - `\text{log} \left(\frac{25}{13}\right)` is positive, so nothing needs reversing
> 
> Use part (b) to shortcut the algebra.
> 
> - The fraction $\frac{16}{1-\frac{13}{25}}$ is exactly the sum to infinity you already found, so it is $\frac{100}{3}$
> - That also explains why the answer exists at all: the total creeps up towards $33 . 3 \dots$, so it passes 33 but would never pass 34
> 
> "Least possible value" means round up, not to the nearest whole number.
> 
> - $n > 7 . 04 \dots$ gives $n = 8$
> - Checking either side confirms it, since `\left(\frac{13}{25}\right)^{7}` is about $0 . 0103$, which is bigger than $0 . 01$, while `\left(\frac{13}{25}\right)^{8}` is about $0 . 0053$

## Q11 — medium — 10 marks · exam-questions

### 8((a)) — 6 marks
Turn each piece of given information into an equation in $a$ and $d$

The sum of the first four terms uses `S_{n} = \frac{n}{2} \left[2 a + \left(n - 1\right) d\right]` with $n = 4$

`\frac{4}{2} \left[2 a + \left(4 - 1\right) d\right] = 42`

Simplify the left hand side

$4 a + 6 d = 42$

**[B1]**

The fifth term uses `a + \left(n - 1\right) d` with $n = 5$

$a + 4 d = 23$

**[B1]**

Rearrange the second equation to make $a$ the subject, then substitute it into the first

$a = 23 - 4 d$

`4 \left(23 - 4 d\right) + 6 d = 42`

**[M1]**

Expand and collect the terms in $d$

$92 - 16 d + 6 d = 42$

$- 10 d = - 50$

Solving gives $d = 5$, and substituting back gives $a = 23 - 20$

$a = 3 , d = 5$

**[A1]**

Now build the $n$th term from these values

`U_{n} = 3 + \left(n - 1\right) 5`

$U_{n} = 5 n - 2$

**[M1]**

$S_{n}$ is the total of the first $n$ terms, so it is the sum of $U_{r}$ as $r$ runs from 1 to $n$

`S_{n} = \sum_{r = 1}^{n} \left(5 r - 2\right) \textrm{ } \text{as required}`

**[A1]**

Comparing this with `\sum_{r = 1}^{n} \left(P r - Q\right)` gives $P = 5$ and $Q = 2$, and both of those are prime

> **[mark-scheme]**
> **B1**: A correct equation from the sum of the first four terms, such as $4 a + 6 d = 42$, simplified or unsimplified.
> 
> **B1**: A correct equation from the fifth term, $a + 4 d = 23$.
> 
> **M1**: Attempts to solve the two equations simultaneously, eliminating one variable.
> 
> **A1**: Both $a = 3$ and $d = 5$.
> 
> **M1**: Uses your values to form the $n$th term, reaching $5 n - 2$ or an equivalent.
> 
> **A1**: Reaches the printed summation form with no errors seen, so that $P = 5$ and $Q = 2$.
> 
> The two values do not have to be stated separately, since they can be read from a correct summation. There is no need to comment on the fact that they are prime.
> 
> Using `S_{4} = \frac{4}{2} \left(U_{1} + U_{4}\right)` for the first equation is equally acceptable and earns the first mark in the same way.
> 
> Because the form of the answer is printed, the $n$th term has to be seen. A summation written down with no supporting working does not earn the final mark.

> **[exam-tip]**
> Two pieces of information mean two equations in $a$ and $d$.
> 
> - "The sum of the first four terms" needs the sum formula
> - "The fifth term" needs the $n$th term formula, and mixing the two up is the usual error
> 
> The link between the $n$th term and the summation is the whole point of this question.
> 
> - Adding up the first $n$ terms is exactly what `\sum_{r = 1}^{n} U_{r}` means
> - So once you have $U_{n} = 5 n - 2$, replacing $n$ by $r$ inside a summation sign finishes the job
> 
> Use the word "prime" as a check on your answer.
> 
> - $P = 5$ and $Q = 2$ are both prime, which confirms the values are right
> - If your two constants are not prime, something has gone wrong earlier
> 
> Check the values against the original statements.
> 
> - With $a = 3$ and $d = 5$ the first four terms are 3, 8, 13 and 18, which add to 42, and the fifth is 23

### 8((b)) — 4 marks
Write each part of the given equation in terms of $n$, using $a = 3$ and $d = 5$ from part (a)

The sum to $2 n$ terms uses the sum formula with $2 n$ in place of $n$

`S_{2 n} = \frac{2 n}{2} \left[2 \left(3\right) + \left(2 n - 1\right) 5\right]`

Simplify inside the bracket, where $6 + 10 n - 5$ becomes $10 n + 1$

`S_{2 n} = n \left(10 n + 1\right)`

**[M1]**

The $n$th term was found in part (a)

$U_{n} = 5 n - 2$

Substitute both into the equation given in the question

`n \left(10 n + 1\right) - 3 \left(5 n - 2\right) = 1062`

**[M1]**

Expand both brackets, taking care that subtracting $- 6$ gives $+ 6$

$10 n^{2} + n - 15 n + 6 = 1062$

Collect the terms and move 1062 across

$10 n^{2} - 14 n - 1056 = 0$

**[M1]**

Every term divides by 2, which makes the numbers easier to handle

$5 n^{2} - 7 n - 528 = 0$

Factorise, looking for two numbers multiplying to `5 \times \left(- 528\right) = - 2640` and adding to $- 7$

- Those numbers are 48 and $- 55$

`\left(5 n + 48\right) \left(n - 11\right) = 0`

Setting each bracket to zero gives $n = - \frac{48}{5}$ or $n = 11$

$n$ counts terms, so it must be a positive whole number and the negative fraction is rejected

$n = 11$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the sum formula with $2 n$ in place of $n$, together with your $n$th term from part (a).
> 
> **M1**: Substitutes both expressions into $S_{2n} - 3 U_{n} = 1062$.
> 
> **M1**: Expands and collects to form a three term quadratic in $n$, then makes a complete attempt to solve it. Any correct method of solution is accepted.
> 
> **A1**: $n = 11$.
> 
> The negative root does not have to be seen, and many students reject it automatically. However, the accuracy mark is withheld if $- \frac{48}{5}$ is offered as a value of $n$ alongside 11.
> 
> All three method marks follow through from your values of $a$ and $d$ in part (a).

> **[exam-tip]**
> Substituting $2 n$ into the sum formula catches people out.
> 
> - Every $n$ in `\frac{n}{2} \left[2 a + \left(n - 1\right) d\right]` becomes $2 n$, including the one outside the bracket
> - The $\frac{2n}{2}$ then cancels to $n$, which keeps the working tidy
> 
> Watch the sign when the bracket is subtracted.
> 
> - `- 3 \left(5 n - 2\right)` is $- 15 n + 6$, and treating it as $- 15 n - 6$ shifts the constant by 12
> 
> Divide through before factorising.
> 
> - $10 n^{2} - 14 n - 1056 = 0$ halves to $5 n^{2} - 7 n - 528 = 0$
> - The discriminant is $10609$, whose square root is exactly $103$, so the formula works cleanly if you cannot spot the factors
> 
> Say explicitly that you are rejecting the other root.
> 
> - The mark is lost if $- \frac{48}{5}$ is left standing as a possible value of $n$, so make clear that only 11 is the answer

## Q12 — medium — 4 marks · exam-questions

### 1() — 4 marks
Every term of an arithmetic series can be written using the first term $a$ and the common difference $d$

- The $n$th term is `a + \left(n - 1\right) d`, so the 10th term is $a + 9 d$ and not $a + 10 d$

Write the first statement in terms of $a$ and $d$

`\left(a + 9 d\right) + \left(a + 10 d\right) + \left(a + 11 d\right) = 129`

Collect the like terms

$3 a + 30 d = 129$

**[M1]**

Do the same with the second statement, using the 19th, 20th and 21st terms

`\left(a + 18 d\right) + \left(a + 19 d\right) + \left(a + 20 d\right) = 237`

$3 a + 57 d = 237$

**[M1]**

Both equations contain $3 a$, so subtracting the first from the second removes $a$ altogether

$27 d = 108$

$d = 4$

**[M1]**

Put $d = 4$ back into the first equation

`3 a + 30 \left(4\right) = 129`

$3 a = 9$

$a_{1} = 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses `a + \left(n - 1\right) d` correctly to form an equation from either the 10th, 11th and 12th terms or the 19th, 20th and 21st terms. Simplified or unsimplified.
> 
> **M1**: Correct equations formed from both sets of three terms.
> 
> **M1**: Attempts to solve the two equations simultaneously, eliminating one variable and reaching a value for $a$ or $d$. One processing error is allowed.
> 
> **A1**: $a_{1} = 3$.
> 
> The first term may be called $a$ or $a_{1}$ throughout, and mixing the two is not penalised.
> 
> Working from the 10th term rather than the first is equally acceptable and earns the same four marks. There the two equations are $3 a_{10} + 3 d = 129$ and $3 a_{10} + 30 d = 237$, which give $27 d = 108$ in the same way, and the final mark still requires the value of the first term.
> 
> Noticing that three consecutive terms add to three times the middle one is also fully acceptable. That route gives $a_{11} = 43$ and $a_{20} = 79$ for the first two marks, $9 d = 36$ for the third, and $a_{1} = 3$ for the last.

> **[exam-tip]**
> Three consecutive terms of an arithmetic series always add up to three times the middle term.
> 
> - The 10th, 11th and 12th terms come to $3 a_{11}$, so $a_{11} = 43$ in one step
> - In the same way $a_{20} = 79$, and there are nine steps from the 11th term to the 20th, so $9 d = 36$
> - This is quicker than forming two equations, but the longer route is safer if you cannot see it
> 
> Count the steps, not the terms.
> 
> - The 10th term is $a + 9 d$ because you take nine steps of $d$ to get there from the first term
> - Writing $a + 10 d$ shifts every term along by one and loses the method marks
> 
> Check your two values against both of the original statements.
> 
> - With $a = 3$ and $d = 4$ the 10th, 11th and 12th terms are 39, 43 and 47, which add to 129
> - The 19th, 20th and 21st terms are 75, 79 and 83, which add to 237

## Q13 — medium — 8 marks · exam-questions

### 6((a)) — 5 marks
In a geometric series each term is the one before it multiplied by the common ratio

That means dividing any term by the one before it gives the same value both times

$\frac{U_{2}}{U_{1}} = \frac{U_{3}}{U_{2}}$

Substitute the three given expressions

`\frac{q \left(2 p + 3\right)}{q \left(4 p + 1\right)} = \frac{q \left(2 p - 3\right)}{q \left(2 p + 3\right)}`

**[M1]**

Every term contains a factor of $q$, so the $q$s cancel and $p$ can be found on its own

Cross-multiply to clear the fractions

`\left(2 p + 3\right)^{2} = \left(4 p + 1\right) \left(2 p - 3\right)`

**[M1]**

Expand each side, taking care with the middle term on the left

- `\left(2 p + 3\right)^{2} = 4 p^{2} + 12 p + 9`
- `\left(4 p + 1\right) \left(2 p - 3\right) = 8 p^{2} - 10 p - 3`

$4 p^{2} + 12 p + 9 = 8 p^{2} - 10 p - 3$

Collect everything on the side that keeps the $p^{2}$ term positive, then divide through by 2

$2 p^{2} - 11 p - 6 = 0$

**[A1]**

Factorise, looking for two numbers multiplying to `2 \times \left(- 6\right) = - 12` and adding to $- 11$

- Those numbers are 1 and $- 12$

`\left(2 p + 1\right) \left(p - 6\right) = 0`

**[M1]**

Set each bracket equal to zero in turn

$p=-\frac{1}{2},p=6$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the fact that the ratio of consecutive terms is constant, equating $\frac{U_{2}}{U_{1}}$ with $\frac{U_{3}}{U_{2}}$ or an equivalent statement.
> 
> **M1**: Cross-multiplies to clear the fractions, reaching `\left(2 p + 3\right)^{2} = \left(4 p + 1\right) \left(2 p - 3\right)` or an equivalent.
> 
> **A1**: The correct three term quadratic, $2 p^{2} - 11 p - 6 = 0$ or any equivalent such as $4 p^{2} - 22 p - 12 = 0$.
> 
> **M1**: A complete and correct method for solving that quadratic, by factorising, completing the square or the quadratic formula.
> 
> **A1**: Both values, $p = - \frac{1}{2}$ and $p = 6$.
> 
> Using the property $U_{2}^{2} = U_{1} U_{3}$ directly is equally acceptable and earns the first two marks together with the same working from there.
> 
> The factor of $q$ cancels throughout, so it does not need to be mentioned. Cancelling it at any stage, or never writing it, is not penalised.
> 
> Both values are required for the final mark, because the question asks for the possible values of $p$. Neither is rejected in this part.

> **[exam-tip]**
> Three consecutive terms of a geometric series are linked by one equation.
> 
> - The ratio from the first to the second must equal the ratio from the second to the third
> - Written the other way round, $U_{2}^{2} = U_{1} U_{3}$, which avoids fractions altogether if you prefer
> 
> The $q$ never matters here, so do not let it slow you down.
> 
> - Every term has $q$ as a factor, so it cancels on both sides
> - Part (b) is where $q$ is actually found
> 
> Expanding a squared bracket needs the middle term.
> 
> - `\left(2 p + 3\right)^{2}` is $4 p^{2} + 12 p + 9$, and the $12 p$ comes from $2 \times 2 p \times 3$
> 
> Both answers are wanted here, so do not discard one yet.
> 
> - The question asks for the possible values, so both go down
> - One of them is ruled out in part (b), but only because of the extra condition given there

### 6((b)) — 3 marks
A geometric series converges only when its common ratio satisfies `\left|r\right| < 1`, so test each value of $p$ from part (a)

Take $p = 6$ first, and work out the first two terms

- Putting $p = 6$ into `q \left(4 p + 1\right)` gives $U_{1} = 25 q$
- Putting $p = 6$ into `q \left(2 p + 3\right)` gives $U_{2} = 15 q$

The common ratio is the second term divided by the first

$r = \frac{15q}{25q}$

$r = \frac{3}{5}$

**[M1]**

Now check $p = - \frac{1}{2}$, which gives $U_{1} = - q$ and $U_{2} = 2 q$, so $r = - 2$

Since `\left|- 2\right| > 1` that series does not converge, so $p = 6$ is the value to use

Substitute $U_{1} = 25 q$ and $r = \frac{3}{5}$ into $S_{\infty} = \frac{a}{1-r}$, and set it equal to 250

$\frac{25q}{1-\frac{3}{5}} = 250$

**[M1]**

The bottom is $\frac{2}{5}$, and dividing by $\frac{2}{5}$ is the same as multiplying by $\frac{5}{2}$

$25 q \times \frac{5}{2} = 250$

$\frac{125q}{2} = 250$

$q = 4$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses $p = 6$ to find the common ratio $\frac{3}{5}$ and the first term $25 q$, either stated or clearly used.
> 
> **M1**: Substitutes those into a correct sum to infinity formula and sets the result equal to 250. This mark depends on the previous one.
> 
> **A1**: $q = 4$.
> 
> The value $p = - \frac{1}{2}$ gives a common ratio of $- 2$, so that series diverges and no sum to infinity exists. Rejecting it does not have to be written down, but $p = 6$ must be the value used.
> 
> Any correct route to the first term is accepted, including finding it as `q \left(2 p + 3\right) \div r`.

> **[exam-tip]**
> The word "convergent" is doing real work in this question.
> 
> - It is what rules out $p = - \frac{1}{2}$, whose ratio is $- 2$
> - A sum to infinity only exists when $- 1 < r < 1$, so a series with $r = - 2$ has none
> 
> Check both values rather than assuming the positive one is wanted.
> 
> - $p = - \frac{1}{2}$ gives terms $- q$, $2 q$, $- 4 q$, which grow without limit
> - Showing that briefly is good practice even though the mark scheme does not insist on it
> 
> Keep $q$ as a symbol all the way through.
> 
> - The first term is $25 q$, not 25, and the sum to infinity is $\frac{25q}{1-\frac{3}{5}}$
> - Dropping the $q$ gives $62 . 5$ rather than an equation to solve
> 
> Check the answer by rebuilding the series.
> 
> - With $q = 4$ the terms are 100, 60, 36 and so on, and $\frac{100}{1-\frac{3}{5}} = 250$
