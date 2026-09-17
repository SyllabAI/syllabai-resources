# Mark Schemes — Binomial Series
**Series** · Edexcel IGCSE Further Pure Maths (4PM1)


## Q1 — medium — 7 marks · exam-questions

### 7((a)) — 3 marks
The power is negative and fractional, so use the general binomial series, which works for any power

`( 1 + u )^{n} = 1 + n u + \frac{n \left(n - 1\right)}{2 !} u^{2} + \frac{n \left(n - 1\right) \left(n - 2\right)}{3 !} u^{3} + \ldots`

Here $n = - \frac{3}{4}$ and $u = 2 x^{2}$

- Because $u$ is already a term in $x^{2}$, the three terms shown give powers up to $x^{6}$, which is exactly what is asked for

Write it out before simplifying anything, keeping the brackets around $2 x^{2}$

`\left(1 + 2 x^{2}\right)^{- \frac{3}{4}} = 1 + \left(- \frac{3}{4}\right) \left(2 x^{2}\right) + \frac{\left(- \frac{3}{4}\right) \left(- \frac{7}{4}\right)}{2 !} \left(2 x^{2}\right)^{2} + \frac{\left(- \frac{3}{4}\right) \left(- \frac{7}{4}\right) \left(- \frac{11}{4}\right)}{3 !} \left(2 x^{2}\right)^{3}`

**[M1]**

Now simplify one term at a time

The $x^{2}$ term is a single multiplication

`\left(- \frac{3}{4}\right) \left(2 x^{2}\right) = - \frac{3}{2} x^{2}`

For the $x^{4}$ term the coefficient is $\frac{21}{32}$ and `\left(2 x^{2}\right)^{2}` is $4 x^{4}$

$\frac{21}{32} \times 4 x^{4} = \frac{21}{8} x^{4}$

**[A1]**

For the $x^{6}$ term the coefficient is $- \frac{77}{128}$ and `\left(2 x^{2}\right)^{3}` is $8 x^{6}$

$- \frac{77}{128} \times 8 x^{6} = - \frac{77}{16} x^{6}$

Collect the four terms together

`\left(1 + 2 x^{2}\right)^{- \frac{3}{4}} = 1 - \frac{3}{2} x^{2} + \frac{21}{8} x^{4} - \frac{77}{16} x^{6}`

**[A1]**

> **[mark-scheme]**
> **M1**: A correct binomial expansion in unsimplified form, with $n = - \frac{3}{4}$, the correct denominators $2 !$ and $3 !$, and the correct powers of $2 x^{2}$.
> 
> **A1**: At least one of the simplified terms after the first two correct.
> 
> **A1**: The fully correct simplified expansion, $1 - \frac{3}{2} x^{2} + \frac{21}{8} x^{4} - \frac{77}{16} x^{6}$.
> 
> The brackets around $2 x^{2}$ must be present, or recovered later, for the method mark.
> 
> Any terms in powers above $x^{6}$ are ignored throughout.
> 
> The question asks for exact fractions in their lowest terms, so decimal coefficients do not earn the final mark.

> **[exam-tip]**
> Substituting a term in $x^{2}$ doubles every power you get out.
> 
> - $u = 2 x^{2}$, so $u^{2}$ is a term in $x^{4}$ and $u^{3}$ is a term in $x^{6}$
> - That is why three terms of the formula are enough to reach $x^{6}$, and writing four would be wasted work
> 
> The brackets are where most marks are lost.
> 
> - `\left(2 x^{2}\right)^{2}` is $4 x^{4}$, not $2 x^{4}$, and `\left(2 x^{2}\right)^{3}` is $8 x^{6}$, not $2 x^{6}$
> 
> Watch the pattern of the numerators.
> 
> - Each new factor drops by 1 from $- \frac{3}{4}$, giving $- \frac{7}{4}$ then $- \frac{11}{4}$, since $- \frac{3}{4} - 1 = - \frac{7}{4}$
> - With three negative factors the $x^{6}$ coefficient comes out negative, so the signs alternate
> 
> Keep everything as fractions from the start.
> 
> - Turning $\frac{21}{32}$ into a decimal early makes the final tidy fractions almost impossible to recover

### 7((b)) — 2 marks
The denominator is the same bracket as in part (a), so rewrite `\text{f} \left(x\right)` as a product

`\text{f} \left(x\right) = \left(2 + k x\right) \left(1 + 2 x^{2}\right)^{- \frac{3}{4}}`

Substitute the expansion from part (a)

`\text{f} \left(x\right) = \left(2 + k x\right) \left(1 - \frac{3}{2} x^{2} + \frac{21}{8} x^{4} - \frac{77}{16} x^{6}\right)`

Multiply the two brackets, keeping only the products that land on $x^{5}$ or below

- The 2 multiplies each term to give $2$, $- 3 x^{2}$ and $\frac{21}{4} x^{4}$
- The $k x$ multiplies each term to give $k x$, $- \frac{3k}{2} x^{3}$ and $\frac{21k}{8} x^{5}$

`\text{f} \left(x\right) = 2 - 3 x^{2} + \frac{21}{4} x^{4} + k x - \frac{3 k}{2} x^{3} + \frac{21 k}{8} x^{5}`

**[M1]**

Collect the six terms in ascending powers

`\text{f} \left(x\right) = 2 + k x - 3 x^{2} - \frac{3 k}{2} x^{3} + \frac{21}{4} x^{4} + \frac{21 k}{8} x^{5}`

**[A1]**

> **[mark-scheme]**
> **M1**: Multiplies your expansion from part (a) by `\left(2 + k x\right)`, with at least two terms of differing powers correctly obtained.
> 
> **A1**: The fully correct expansion as far as the term in $x^{5}$.
> 
> The method mark follows through from your expansion in part (a).
> 
> Terms above $x^{5}$ are ignored, so leaving the $- \frac{77}{16} x^{6}$ products in is not penalised.

> **[exam-tip]**
> Work out which products you need before multiplying anything.
> 
> - Only two terms of `\left(2 + k x\right)` exist, so each term of the expansion produces exactly two products
> - Anything involving $x^{6}$ is already past $x^{5}$ and can be ignored from the start
> 
> The two halves of the bracket give you the two halves of the answer.
> 
> - The 2 produces every even power, and the $k x$ produces every odd power
> - So every term containing $k$ has an odd power of $x$, which is a quick way to check your work
> 
> There is no $x$ term from the first bracket and no constant from the second.
> 
> - That is why the $x$ term is simply $k x$ and the constant is simply 2

### 7((c)) — 2 marks
Read the two coefficients off the expansion from part (b)

- The coefficient of $x^{2}$ is $- 3$
- The coefficient of $x^{5}$ is $\frac{21k}{8}$

Turn "is fourteen times" into an equation, with the 14 multiplying the smaller-power coefficient

`\frac{21 k}{8} = 14 \times \left(- 3\right)`

**[M1]**

Work out the right hand side, then multiply both sides by $\frac{8}{21}$

$\frac{21k}{8} = - 42$

$k = \frac{-42\times8}{21}$

$k = - 16$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets your coefficient of $x^{5}$ equal to 14 times your coefficient of $x^{2}$ and attempts to solve for $k$.
> 
> **A1**: $k = - 16$.
> 
> The method mark follows through from your expansion in part (b), so a wrong coefficient there does not stop you earning it.
> 
> The question states that $k \neq 0$, so no second solution needs discussing.

> **[exam-tip]**
> Both coefficients are already sitting in part (b), so there is nothing new to expand.
> 
> - The $x^{2}$ coefficient is the one with no $k$ in it, and the $x^{5}$ coefficient is the one with $k$
> 
> Put the multiplier on the correct side.
> 
> - The $x^{5}$ coefficient is the larger one, so it equals 14 times the other
> - Writing $- 3 = 14 \times \frac{21k}{8}$ inverts the relationship and gives $k = - \frac{4}{49}$
> 
> A negative answer is expected here, so do not assume a sign error.
> 
> - The $x^{2}$ coefficient is negative and the $x^{5}$ coefficient must therefore be negative too, which forces $k$ negative

## Q2 — medium — 12 marks · exam-questions

### 6((a)) — 2 marks
The binomial series only applies to a bracket that starts with 1, so a factor has to come out of $4 + b x$

Take out the 4, which leaves the bracket in the form the series needs

`\frac{a}{\sqrt{4 + b x}} = \frac{a}{\sqrt{4 \left(1 + \frac{b x}{4}\right)}}`

**[M1]**

A square root of a product is the product of the square roots, and $\sqrt{4} = 2$

$\frac{a}{\sqrt{4+bx}} = \frac{a}{2\sqrt{1+\frac{bx}{4}}}$

A square root in the denominator is a power of $- \frac{1}{2}$ in the numerator

`\frac{a}{\sqrt{4 + b x}} = \frac{a}{2} \left(1 + \frac{b x}{4}\right)^{- \frac{1}{2}} \textrm{ } \text{as required}`

**[A1]**

> **[mark-scheme]**
> **M1**: Takes a factor of 4 out of the square root, or an equivalent first step such as writing the whole expression as `a \left(4 + b x\right)^{- \frac{1}{2}}` and then factorising.
> 
> **A1**: Reaches the printed form with no errors seen.
> 
> Several equivalent routes earn the same two marks: $\frac{a}{\sqrt{4}\sqrt{1+\frac{bx}{4}}}$, `\frac{a}{4^{\frac{1}{2}} \left(1 + \frac{b x}{4}\right)^{\frac{1}{2}}}`, `a \left(4^{- \frac{1}{2}}\right) \left(1 + \frac{b x}{4}\right)^{- \frac{1}{2}}` and `a \left(4 \left(1 + \frac{b x}{4}\right)\right)^{- \frac{1}{2}}` are all accepted.
> 
> Because the result is printed in the question, every intermediate step has to be correct.

> **[exam-tip]**
> The binomial series needs a bracket starting with 1, and that is the whole purpose of this part.
> 
> - `\left(1 + u\right)^{n}` is the only form the expansion applies to, so a 4 in front has to be dealt with first
> - Every later part depends on this, so the factor of $\frac{a}{2}$ carries all the way to part (d)
> 
> The factor comes out to the same power as the bracket.
> 
> - Under a square root, 4 becomes $\sqrt{4} = 2$, not 4 and not 16
> - That 2 then sits in the denominator, which is where the $\frac{a}{2}$ comes from
> 
> Dividing by a square root is the same as multiplying by a power of $- \frac{1}{2}$.
> 
> - $\frac{1}{\sqrt{X}} = X^{-\frac{1}{2}}$, which is the last step of the rearrangement

### 6((b)) — 4 marks
Part (a) has already put the expression in the form the binomial series needs

`( 1 + u )^{n} = 1 + n u + \frac{n \left(n - 1\right)}{2 !} u^{2} + \frac{n \left(n - 1\right) \left(n - 2\right)}{3 !} u^{3} + \ldots`

Here $n = - \frac{1}{2}$ and $u = \frac{bx}{4}$, and the whole expansion is multiplied by $\frac{a}{2}$

`\frac{a}{2} \left[1 + \left(- \frac{1}{2}\right) \left(\frac{b x}{4}\right) + \frac{\left(- \frac{1}{2}\right) \left(- \frac{3}{2}\right)}{2 !} \left(\frac{b x}{4}\right)^{2} + \frac{\left(- \frac{1}{2}\right) \left(- \frac{3}{2}\right) \left(- \frac{5}{2}\right)}{3 !} \left(\frac{b x}{4}\right)^{3}\right]`

**[M1]**

Simplify inside the bracket one term at a time

- The coefficients work out as $- \frac{1}{2}$, $\frac{3}{8}$ and $- \frac{5}{16}$
- The powers of $\frac{bx}{4}$ give $\frac{bx}{4}$, $\frac{b^{2}x^{2}}{16}$ and $\frac{b^{3}x^{3}}{64}$

`\frac{a}{2} \left[1 - \frac{b x}{8} + \frac{3}{128} b^{2} x^{2} - \frac{5}{1024} b^{3} x^{3}\right]`

**[M1]**

Now multiply every term inside the bracket by $\frac{a}{2}$

$\frac{a}{2} - \frac{ab}{16} x + \frac{3ab^{2}}{256} x^{2} - \frac{5ab^{3}}{2048} x^{3}$

**[A1]**

Compare this term by term with $P + Q x + R x^{2} + S x^{3}$

- The coefficient of $x$ is $- \frac{ab}{16}$ and the coefficient of $x^{3}$ is $- \frac{5ab^{3}}{2048}$, which are the two printed results

$P=\frac{a}{2},Q=-\frac{ab}{16},R=\frac{3ab^{2}}{256},S=-\frac{5ab^{3}}{2048}$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the binomial series with $n = - \frac{1}{2}$ and $\frac{bx}{4}$ substituted, with the correct denominators $2 !$ and $3 !$.
> 
> **M1**: Simplifies the coefficients inside the bracket, or multiplies through by $\frac{a}{2}$, with at least two terms correct.
> 
> **A1**: A fully correct expansion as far as the term in $x^{3}$.
> 
> **A1**: All four values correct, with $Q$ and $S$ matching the printed forms.
> 
> Multiplying the $\frac{a}{2}$ in at the start rather than at the end is equally acceptable and is marked in the same way.
> 
> Because $Q$ and $S$ are printed in the question, every intermediate step has to be checked for errors. Writing the simplified bracket before multiplying through is not necessary, but it must be correct if it is seen.
> 
> $P$ and $R$ must be given as fractions in their lowest terms.

> **[exam-tip]**
> Keep the $\frac{a}{2}$ outside the bracket until the very end.
> 
> - Carrying it through every term from the start means four fractions to simplify instead of one multiplication at the finish
> - It also makes the printed forms of $Q$ and $S$ easier to recognise when you get there
> 
> The powers of $\frac{bx}{4}$ are the usual trap.
> 
> - `\left(\frac{b x}{4}\right)^{2}` is $\frac{b^{2}x^{2}}{16}$, so both the $b$ and the 4 are squared
> - `\left(\frac{b x}{4}\right)^{3}` is $\frac{b^{3}x^{3}}{64}$, and forgetting to cube the 4 is what turns 2048 into 512
> 
> Two of the four answers are printed, which makes this part self-checking.
> 
> - If your $Q$ is not $- \frac{ab}{16}$, something has gone wrong before you reach $R$ and $S$
> - Use that as a checkpoint rather than pressing on
> 
> The signs alternate, because $n$ is negative.
> 
> - $P$ and $R$ are positive, $Q$ and $S$ are negative

### 6((c)) — 3 marks
Substitute the expressions for $Q$ and $S$ from part (b) into the relationship given

`- \frac{a b}{16} = \frac{128}{5} \left(- \frac{5 a b^{3}}{2048}\right)`

**[M1]**

Simplify the right hand side

- The 5 in the numerator cancels the 5 in the denominator
- $\frac{128}{2048} = \frac{1}{16}$

$- \frac{ab}{16} = - \frac{ab^{3}}{16}$

Both sides have a factor of $- \frac{ab}{16}$, and $a$ and $b$ are positive so that factor is not zero

Dividing through by it leaves a simple equation in $b$

$b^{2} = 1$

$b$ is a positive integer, so the negative root is rejected

$b = 1$

**[A1]**

Now use the other given value, with $R = \frac{3ab^{2}}{256}$ from part (b)

$\frac{3a\times1^{2}}{256} = \frac{9}{256}$

Multiply both sides by 256

$3 a = 9$

$a = 3$

**[B1]**

> **[mark-scheme]**
> **M1**: Substitutes your expressions for $Q$ and $S$ into $Q = \frac{128}{5} S$ and simplifies towards an equation in $b$ alone.
> 
> **A1**: $b = 1$, with the minimum steps shown and no errors or omissions.
> 
> **B1**: A correct equation in $a$ leading to $a = 3$, with no errors or omissions.
> 
> Both results are printed in the question, so the working has to reach them rather than assume them. Although B marks are normally independent of method, this is a show that question and the final mark is not awarded if there are errors in the work.
> 
> Rearranging as $\frac{5}{128} Q = S$ is equally acceptable and gives the same equation.
> 
> The negative root of $b^{2} = 1$ does not have to be written down, since the question states that $b$ is a positive integer.

> **[exam-tip]**
> The two given facts do different jobs, and the order matters.
> 
> - The relationship between $Q$ and $S$ contains both $a$ and $b$, but the $a$ cancels, so it gives you $b$ on its own
> - Only then does $R = \frac{9}{256}$ give you $a$
> - Starting with $R$ instead leaves two unknowns in one equation and goes nowhere
> 
> Cancelling is what makes this work, so look for the common factor.
> 
> - Both sides come out as a multiple of $\frac{ab}{16}$, and dividing by it collapses the whole thing to $b^{2} = 1$
> - $a$ and $b$ are positive integers, so you are never dividing by zero
> 
> Both answers are printed, so the working is what earns the marks.
> 
> - Writing $a = 3$ and $b = 1$ with no supporting algebra scores nothing here
> 
> Check the values against part (b).
> 
> - With $a = 3$ and $b = 1$, $Q = - \frac{3}{16}$ and $S = - \frac{15}{2048}$, and `\frac{128}{5} \times \left(- \frac{15}{2048}\right)` is indeed $- \frac{3}{16}$

### 6((d)) — 3 marks
With $a = 3$ and $b = 1$ the original expression is $\frac{3}{\sqrt{4+x}}$

Choose the value of $x$ that turns it into the quantity you want

$\frac{3}{\sqrt{4+x}} = \frac{\sqrt{6}}{2}$

Rearranging gives $\sqrt{4+x} = \frac{6}{\sqrt{6}}$, and $\frac{6}{\sqrt{6}}$ is $\sqrt{6}$

$4 + x = 6$

$x = 2$

**[M1]**

Check this value is allowed, since the expansion is only valid for `\left|\frac{x}{4}\right| < 1`, that is $- 4 < x < 4$

- $x = 2$ lies inside that range

Substitute $a = 3$, $b = 1$ and $x = 2$ into the expansion from part (b)

$\frac{3}{2} - \frac{3\times1}{16} \times 2 + \frac{3\times3\times1^{2}}{256} \times 2^{2} - \frac{5\times3\times1^{3}}{2048} \times 2^{3}$

**[M1]**

Work out the four terms, keeping full accuracy

$1 . 5 - 0 . 375 + 0 . 140625 - 0 . 05859375$

`\frac{\sqrt{6}}{2} \approx 1 . 207 \textrm{ } \left(3 d . p .\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Sets $\frac{3}{\sqrt{4+x}}$ equal to $\frac{\sqrt{6}}{2}$, or an equivalent such as $\sqrt{6} = \sqrt{4+x}$, and solves to find $x = 2$.
> 
> **M1**: Substitutes your value of $x$ into your expansion from part (b), using your values of $a$ and $b$. This mark depends on the previous one.
> 
> **A1**: $1 . 207$.
> 
> Reaching $x = 2$ by inspection, without the intermediate rearrangement, is accepted provided the value is correct.
> 
> The question asks for 3 decimal places, so the four terms should be kept exact or to full calculator accuracy until the final line. The unrounded value is $1 . 20703125$.

> **[exam-tip]**
> Work backwards from the quantity you are asked to approximate.
> 
> - You need $\frac{3}{\sqrt{4+x}}$ to equal $\frac{\sqrt{6}}{2}$, so ask what makes $\sqrt{4+x}$ into $\sqrt{6}$
> - That gives $x = 2$ almost by inspection, once you notice $\frac{6}{\sqrt{6}} = \sqrt{6}$
> 
> Always check the value lies inside the valid range.
> 
> - The expansion needs `\left|\frac{x}{4}\right| < 1`, so $x$ must be between $- 4$ and 4
> - $x = 2$ is inside it, but only just over half way, which is why the estimate is good to about three figures
> 
> The approximation is not exact, and it is not meant to be.
> 
> - $\frac{\sqrt{6}}{2}$ is $1 . 2247 \dots$ against the estimate $1 . 207$, because the series was cut off after four terms
> - The question asks for the value the expansion gives, not the true value, so do not be tempted to write $1 . 225$
> 
> Keep the terms exact until the last line.
> 
> - The four contributions are $\frac{3}{2}$, $- \frac{3}{8}$, $\frac{9}{64}$ and $- \frac{15}{256}$, which combine exactly to $1 . 20703125$

## Q3 — medium — 11 marks · exam-questions

### 7((a)) — 3 marks
Use the general binomial expansion, which works for any power including a negative one

`( 1 + u )^{n} = 1 + n u + \frac{n \left(n - 1\right)}{2 !} u^{2} + \frac{n \left(n - 1\right) \left(n - 2\right)}{3 !} u^{3} + \ldots`

Here $n = - 3$ and $u = \frac{x}{3}$

Write each term out before simplifying anything, keeping the brackets around $\frac{x}{3}$ so the powers apply to the whole of it

`\left(1 + \frac{x}{3}\right)^{- 3} = 1 + \left(- 3\right) \left(\frac{x}{3}\right) + \frac{\left(- 3\right) \left(- 4\right)}{2} \left(\frac{x}{3}\right)^{2} + \frac{\left(- 3\right) \left(- 4\right) \left(- 5\right)}{6} \left(\frac{x}{3}\right)^{3}`

**[M1]**

Now simplify one term at a time

The $x$ term is straightforward

`\left(- 3\right) \left(\frac{x}{3}\right) = - x`

The $x^{2}$ coefficient is `\frac{\left(- 3\right) \left(- 4\right)}{2}`, which is $6$, and `\left(\frac{x}{3}\right)^{2}` is $\frac{x^{2}}{9}$

$6 \times \frac{x^{2}}{9} = \frac{2}{3} x^{2}$

The $x^{3}$ coefficient is `\frac{\left(- 3\right) \left(- 4\right) \left(- 5\right)}{6}`, which is $- 10$, and `\left(\frac{x}{3}\right)^{3}` is $\frac{x^{3}}{27}$

$- 10 \times \frac{x^{3}}{27} = - \frac{10}{27} x^{3}$

**[A1]**

Collect the four terms together

`\left(1 + \frac{x}{3}\right)^{- 3} = 1 - x + \frac{2}{3} x^{2} - \frac{10}{27} x^{3}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct binomial expansion in unsimplified form.
> 
> **A1**: $1 - x$ together with at least one of the $x^{2}$ and $x^{3}$ terms correct and simplified.
> 
> **A1**: Fully correct and simplified expansion.
> 
> For the method mark the expansion must begin with $1$, the next term must be correct, the powers of $\frac{x}{3}$ must be correct, written for example as `\left(\frac{x}{3}\right)^{2}`, and the denominators must be right. Missing brackets are not allowed unless they are recovered later.
> 
> Both accuracy marks follow the method mark, so they cannot be earned without it. Any terms in powers above $x^{3}$ are ignored throughout.

> **[exam-tip]**
> The brackets around $\frac{x}{3}$ are what most marks are lost on.
> 
> - `\left(\frac{x}{3}\right)^{2}` is $\frac{x^{2}}{9}$, not $\frac{x^{2}}{3}$
> - Write the unsimplified expansion out in full first, then simplify, so the brackets are never dropped
> 
> With a negative $n$ the signs alternate in a pattern worth checking. Each new factor `\left(n - 1\right)`, `\left(n - 2\right)` is also negative, so the coefficients here go $- 3$, $+ 6$, $- 10$.
> 
> The question asks for exact fractions in lowest terms, so leave $\frac{2}{3}$ and $\frac{10}{27}$ as they are rather than converting to decimals.

### 7((b)) — 1 marks
The expansion of $( 1 + u )^{n}$ is only valid when `\left|u\right| < 1`

Here $u = \frac{x}{3}$, so that condition becomes

`\left|\frac{x}{3}\right| < 1`

Multiply through by $3$

$- 3 < x < 3$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct range of validity.
> 
> Accept $- 3 < x < 3$ or `\left|x\right| < 3`.

> **[exam-tip]**
> The condition is on the whole of $u$, not on $x$ by itself.
> 
> - With $u = \frac{x}{3}$ the range widens to $- 3 < x < 3$, rather than staying at $- 1 < x < 1$
> 
> A quick sense check: the bracket $1 + \frac{x}{3}$ is zero at $x = - 3$, and an expansion can never be valid where the original expression is undefined. That is exactly where the range stops.

### 7((c)) — 2 marks
The required form starts with $1$ inside the bracket, so take a factor of $3$ out of $3 + x$

`( 3 + x )^{- 3} = \left[3 \left(1 + \frac{x}{3}\right)\right]^{- 3}`

A power outside a product applies to each factor separately

`( 3 + x )^{- 3} = 3^{- 3} \left(1 + \frac{x}{3}\right)^{- 3}`

Since $3^{-3} = \frac{1}{27}$, compare this with $P ( 1 + Q x )^{-3}$

$P = \frac{1}{27}$

**[B1]**

$Q = \frac{1}{3}$

**[B1]**

> **[mark-scheme]**
> **B1**: $P = \frac{1}{27}$.
> 
> **B1**: $Q = \frac{1}{3}$.
> 
> Both marks are available from a correct statement of `\frac{1}{27} \left(1 + \frac{x}{3}\right)^{- 3}`, even if $P$ and $Q$ are not written out separately.

> **[exam-tip]**
> Taking the factor out is the step that makes the binomial expansion usable, and it is worth practising until it is automatic.
> 
> - The bracket must be left starting with $1$, because that is the only form the expansion applies to
> - The factor comes out to the same power as the bracket, so $3$ becomes $3^{-3}$, not $3^{3}$
> 
> A negative power flips the fraction, so $3^{-3}$ is $\frac{1}{27}$ and not $- 27$.

### 7((d)) — 2 marks
Rewrite the denominator using part (c), so the expansion from part (a) can be used

`\text{f} \left(x\right) = \frac{1}{27} \left(1 + 4 x\right) \left(1 + \frac{x}{3}\right)^{- 3}`

Substitute the expansion from part (a), keeping only the terms up to $x^{2}$

`\text{f} \left(x\right) = \frac{1}{27} \left(1 + 4 x\right) \left(1 - x + \frac{2}{3} x^{2}\right)`

Multiply the two brackets out, discarding anything that would give a power above $x^{2}$

The $x$ terms are $- x$ and $4 x$, and the $x^{2}$ terms are $\frac{2}{3} x^{2}$ and $- 4 x^{2}$

`\left(1 + 4 x\right) \left(1 - x + \frac{2}{3} x^{2}\right) = 1 + 3 x - \frac{10}{3} x^{2}`

**[M1]**

Now multiply every term by $\frac{1}{27}$

`\text{f} \left(x\right) = \frac{1}{27} + \frac{x}{9} - \frac{10 x^{2}}{81}`

**[A1]**

> **[mark-scheme]**
> **M1**: Multiplies `\left(1 + 4 x\right)` by your expansion from part (a), with at least three terms of the product found.
> 
> **A1**: Correct expansion as far as the term in $x^{2}$.
> 
> Equivalent coefficients are accepted, so $\frac{1}{27} + \frac{1}{9} x - \frac{10}{81} x^{2}$ and `\frac{1}{27} \left(1 + 3 x - \frac{10}{3} x^{2}\right)` are both fine.
> 
> Allow follow-through from your expansion in part (a).

> **[exam-tip]**
> Do not multiply out every pair of terms. You only need those that land on $x^{0}$, $x^{1}$ or $x^{2}$.
> 
> - $4 x \times \frac{2}{3} x^{2}$ gives an $x^{3}$ term, so it can be ignored from the start
> - Working out which products you need first saves time and avoids errors
> 
> Keep the $\frac{1}{27}$ outside the brackets until the very end. Multiplying it in early gives three awkward fractions to carry through the expansion instead of one at the finish.

### 7((e)) — 3 marks
The series from part (d) is a polynomial, so integrate it term by term

Raise each power of $x$ by one and divide by the new power

`\int_{0}^{0 . 2} \text{f} \left(x\right) \textrm{ } \text{d} x \approx \left[\frac{x}{27} + \frac{x^{2}}{18} - \frac{10 x^{3}}{243}\right]_{0}^{0 . 2}`

**[M1]**

Substitute the upper limit, then subtract the lower limit

Every term has a factor of $x$, so the lower limit contributes nothing

`\int_{0}^{0 . 2} \text{f} \left(x\right) \textrm{ } \text{d} x \approx \frac{0 . 2}{27} + \frac{0 . 04}{18} - \frac{10 \times 0 . 008}{243}`

**[M1]**

Work this out, keeping full accuracy until the end

`\int_{0}^{0 . 2} \text{f} \left(x\right) \textrm{ } \text{d} x \approx 0 . 009300411 \ldots`

Round to 5 significant figures, counting from the first non-zero digit

`\int_{0}^{0 . 2} \text{f} \left(x\right) \textrm{ } \text{d} x \approx 0 . 0093004`

**[A1]**

> **[mark-scheme]**
> **M1**: Attempt to integrate your expression from part (d), with at least one constant term and one algebraic term, and no power of $x$ decreasing.
> 
> **M1**: Substitutes $0 . 2$ into your integrated expression and subtracts the correct way round.
> 
> **A1**: $0 . 0093004$.
> 
> The explicit substitution of $0 . 2$ must be seen at least once if your final answer is wrong, though it can be implied by a correct answer. Substituting $0$ does not have to be shown.
> 
> Accept the exact value $\frac{113}{12150}$ if it is seen.

> **[exam-tip]**
> This is an estimate rather than an exact value, and the question says so.
> 
> - The series was cut off after the $x^{2}$ term, so the integral of that series is only close to the real one
> - The true value of this integral is about $0 . 0093316$, so the estimate is right to about two significant figures despite being quoted to five
> 
> Counting significant figures in a small decimal trips people up. In $0 . 009300411$ the leading zeros do not count, so the five significant figures are $9$, $3$, $0$, $0$ and $4$, giving $0 . 0093004$.
> 
> A question that says "hence" is telling you to use the previous part. Integrating $\frac{1+4x}{(3+x)^{3}}$ directly is far harder and earns nothing here.

## Q4 — medium — 11 marks · exam-questions

### 9((a)) — 3 marks
The power is negative and fractional, so use the general binomial series

`( 1 + u )^{n} = 1 + n u + \frac{n \left(n - 1\right)}{2 !} u^{2} + \frac{n \left(n - 1\right) \left(n - 2\right)}{3 !} u^{3} + \ldots`

Here $n = - \frac{1}{2}$ and $u = - 8 x^{2}$

- The whole of $- 8 x^{2}$ is substituted, including its minus sign

Write it out before simplifying anything

`\left(1 - 8 x^{2}\right)^{- \frac{1}{2}} = 1 + \left(- \frac{1}{2}\right) \left(- 8 x^{2}\right) + \frac{\left(- \frac{1}{2}\right) \left(- \frac{3}{2}\right)}{2 !} \left(- 8 x^{2}\right)^{2} + \frac{\left(- \frac{1}{2}\right) \left(- \frac{3}{2}\right) \left(- \frac{5}{2}\right)}{3 !} \left(- 8 x^{2}\right)^{3}`

**[M1]**

Now simplify one term at a time

Two negatives make the $x^{2}$ term positive

`\left(- \frac{1}{2}\right) \left(- 8 x^{2}\right) = 4 x^{2}`

For the $x^{4}$ term the coefficient is $\frac{3}{8}$, and squaring $- 8 x^{2}$ gives $64 x^{4}$

$\frac{3}{8} \times 64 x^{4} = 24 x^{4}$

**[A1]**

For the $x^{6}$ term the coefficient is $- \frac{5}{16}$, and cubing $- 8 x^{2}$ gives $- 512 x^{6}$

`- \frac{5}{16} \times \left(- 512 x^{6}\right) = 160 x^{6}`

Collect the four terms together

`\left(1 - 8 x^{2}\right)^{- \frac{1}{2}} = 1 + 4 x^{2} + 24 x^{4} + 160 x^{6}`

**[A1]**

> **[mark-scheme]**
> **M1**: A correct binomial expansion in unsimplified form, with $n = - \frac{1}{2}$, the correct denominators and the correct powers of $- 8 x^{2}$.
> 
> **A1**: At least one of the simplified terms after the first correct.
> 
> **A1**: The fully correct simplified expansion, $1 + 4 x^{2} + 24 x^{4} + 160 x^{6}$.
> 
> The brackets around $- 8 x^{2}$ must be present, or recovered later, for the method mark.
> 
> Every coefficient here is a positive integer, which is what the question means by giving each coefficient as an integer.

> **[exam-tip]**
> The minus sign belongs to the substitution, not to the formula.
> 
> - $1 - 8 x^{2}$ is $1 + u$ with $u = - 8 x^{2}$, so every $u$ carries that minus sign
> - Substituting $8 x^{2}$ and trying to patch the signs afterwards is where this goes wrong
> 
> Every term comes out positive here, which is a useful check.
> 
> - The odd powers of $u$ pair a negative coefficient with a negative $u$, and the even power pairs a positive with a positive
> - If any of your four terms is negative, a sign has been dropped
> 
> Cubing a negative number keeps it negative.
> 
> - `\left(- 8 x^{2}\right)^{3} = - 512 x^{6}`, and it is the minus in $- \frac{5}{16}$ that turns the result positive
> 
> Substituting a term in $x^{2}$ doubles the powers.
> 
> - Three terms of the formula reach $x^{6}$, so there is no need to write a fourth

### 9((b)) — 4 marks
The denominator is the bracket expanded in part (a), so write `\text{g} \left(x\right)` as a product

`\text{g} \left(x\right) = \left(a + b x\right) \left(1 + 4 x^{2} + 24 x^{4} + 160 x^{6}\right)`

**[M1]**

Multiply out, keeping the terms in ascending powers of $x$

- The $a$ gives the even powers and the $b x$ gives the odd powers

`\text{g} \left(x\right) = a + b x + 4 a x^{2} + 4 b x^{3} + 24 a x^{4} + \ldots`

**[A1]**

Count along to find which term is which

- The first four terms are $a$, $b x$, $4 a x^{2}$ and $4 b x^{3}$, so the fourth is the one in $x^{3}$
- The fifth is $24 a x^{4}$

Set the fourth term equal to the value given

$4 b = 20$

$b = 5$

**[A1]**

Now the fifth term

$24 a = 48$

$a = 2$

**[A1]**

Both values are prime, as the question requires

$a=2,b=5$

> **[mark-scheme]**
> **M1**: Multiplies `\left(a + b x\right)` by your expansion from part (a).
> 
> **A1**: A correct expansion in terms of $a$ and $b$, at least as far as the term in $x^{4}$. This follows through from your part (a).
> 
> **A1**: $b = 5$, from $4 b = 20$.
> 
> **A1**: $a = 2$, from $24 a = 48$.
> 
> The two accuracy marks for the values are independent, so a correct value for one earns its mark even if the other is wrong.
> 
> Counting the terms is the step that has to be right: the fourth term in ascending powers is the one in $x^{3}$ and the fifth is the one in $x^{4}$, because the expansion starts with a constant term.
> 
> There is no need to comment on the fact that 2 and 5 are prime, though the condition is a useful check.

> **[exam-tip]**
> "Fourth and fifth terms" means counting from the constant, not from the term in $x$.
> 
> - The first term is $a$, so the fourth is the one in $x^{3}$ and the fifth is the one in $x^{4}$
> - Reading them as the $x^{4}$ and $x^{5}$ terms is the commonest error, and it gives no consistent answer
> 
> Only two products reach each power, which keeps the multiplication short.
> 
> - The constant $a$ hits the even powers and the $b x$ hits the odd ones, so each term of the answer has just one source
> 
> Use the word "prime" as a check.
> 
> - $a = 2$ and $b = 5$ are both prime, so the condition is satisfied
> - If your values are not prime, go back and check which terms you counted
> 
> Notice that $a$ and $b$ never interact.
> 
> - The $x^{3}$ equation involves only $b$ and the $x^{4}$ equation only $a$, so there are no simultaneous equations to solve

### 9((c)) — 4 marks
Substitute $a = 2$ and $b = 5$ into the expansion from part (b), and keep the first five terms

`\text{g} \left(x\right) \approx 2 + 5 x + 8 x^{2} + 20 x^{3} + 48 x^{4}`

**[M1]**

That is a polynomial, so integrate it term by term between the given limits

Raise each power of $x$ by one and divide by the new power

`\int_{0}^{0 . 2} \text{g} \left(x\right) \textrm{ } \text{d} x \approx \left[2 x + \frac{5 x^{2}}{2} + \frac{8 x^{3}}{3} + \frac{20 x^{4}}{4} + \frac{48 x^{5}}{5}\right]_{0}^{0 . 2}`

**[M1]**

Substitute the upper limit

- Every term contains a factor of $x$, so the lower limit contributes nothing

`\int_{0}^{0 . 2} \text{g} \left(x\right) \textrm{ } \text{d} x \approx 2 \left(0 . 2\right) + \frac{5 \left(0 . 2\right)^{2}}{2} + \frac{8 \left(0 . 2\right)^{3}}{3} + \frac{20 \left(0 . 2\right)^{4}}{4} + \frac{48 \left(0 . 2\right)^{5}}{5}`

**[M1]**

Work this out, keeping full accuracy until the end

`\int_{0}^{0 . 2} \text{g} \left(x\right) \textrm{ } \text{d} x \approx 0 . 5324053 \ldots`

`integral subscript 0 superscript 0.2 end superscript text g end text open parentheses x close parentheses text end text text d end text x almost equal to 0.5324 text end text open parentheses 4 space straight s. straight f. close parentheses`

**[A1]**

> **[mark-scheme]**
> **M1**: Writes the first five terms of the expansion using your values of $a$ and $b$.
> 
> **M1**: Integrates your polynomial, with no power of $x$ decreasing and at least two terms correct.
> 
> **M1**: Substitutes $0 . 2$ into your integrated expression the correct way round.
> 
> **A1**: $0 . 5324$.
> 
> All three method marks follow through from your earlier answers.
> 
> The substitution of $0 . 2$ must be seen at least once if the final answer is wrong, though a correct answer implies it. Substituting $0$ does not have to be shown.

> **[exam-tip]**
> "The first five terms" means five terms of the series, not terms up to $x^{5}$.
> 
> - Those five run from the constant to the term in $x^{4}$
> - Including the $x^{5}$ term as well is not penalised, but it is extra work for nothing
> 
> This is an estimate, and the question says so, because the series was cut short.
> 
> - The true value of this integral is about $0 . 5348$, against the estimate of $0 . 5324$
> - So the two agree to only two significant figures, even though four are asked for, which is the nature of a truncated series
> 
> Integrating the original function directly is not possible at this level.
> 
> - $\frac{2+5x}{\sqrt{1-8x^{2}}}$ has no elementary antiderivative you are expected to find, which is precisely why the expansion is used
> 
> Keep full accuracy to the last line.
> 
> - Rounding each of the five terms before adding can shift the fourth significant figure

## Q5 — medium — 7 marks · exam-questions

### 6((a)) — 2 marks
The binomial series only applies to a bracket that starts with 1, so a factor has to come out of $8 + 3 x$

Take out the 8, since that is the constant term

`8 + 3 x = 8 \left(1 + \frac{3 x}{8}\right)`

Now take the cube root of both sides, and use the fact that a root of a product is the product of the roots

`\left(8 + 3 x\right)^{\frac{1}{3}} = 8^{\frac{1}{3}} \left(1 + \frac{3 x}{8}\right)^{\frac{1}{3}}`

The cube root of 8 is 2, so comparing this with `p \left(1 + q x\right)^{\frac{1}{3}}` gives both values

$p=2,q=\frac{3}{8}$

**[B1] [B1]**

> **[mark-scheme]**
> **B1**: Either $p = 2$ or $q = \frac{3}{8}$.
> 
> **B1**: Both $p = 2$ and $q = \frac{3}{8}$.
> 
> Leaving the first value as $8^{\frac{1}{3}}$ rather than evaluating it to 2 is accepted for both marks.
> 
> No working is required, so correct values written straight down earn both marks.

> **[exam-tip]**
> The factor you take out is always the constant term, so that what is left starts with 1.
> 
> - $8 + 3 x$ becomes `8 \left(1 + \frac{3 x}{8}\right)`, and dividing $3 x$ by 8 is what produces $q$
> 
> The factor comes out to the same power as the bracket, and here that power is a cube root.
> 
> - $8$ becomes $8^{\frac{1}{3}} = 2$, not 8 and not 24
> - Getting $p = 8$ is the commonest error, and it comes from forgetting that the whole bracket was cube rooted
> 
> $q$ is the coefficient of $x$ divided by the constant.
> 
> - $\frac{3}{8}$ here, and it stays a fraction, since $q$ is not required to be an integer
> 
> This part sets up everything that follows.
> 
> - The $p$ multiplies the whole expansion in part (b), and the $q$ is what gets substituted into the series

### 6((b)) — 3 marks
Part (a) rewrote the expression as `2 \left(1 + \frac{3 x}{8}\right)^{\frac{1}{3}}`, which is ready for the binomial series

`( 1 + u )^{n} = 1 + n u + \frac{n \left(n - 1\right)}{2 !} u^{2} + \ldots`

Here $n = \frac{1}{3}$ and $u = \frac{3x}{8}$, and only terms up to $x^{2}$ are needed

- So two terms of the formula after the 1 are enough

`2 \left[1 + \frac{1}{3} \left(\frac{3 x}{8}\right) + \frac{\frac{1}{3} \left(- \frac{2}{3}\right)}{2 !} \left(\frac{3 x}{8}\right)^{2}\right]`

**[M1]**

Simplify inside the bracket

- The $x$ term is $\frac{1}{3} \times \frac{3x}{8} = \frac{x}{8}$
- The $x^{2}$ coefficient is $- \frac{1}{9}$, and `\left(\frac{3 x}{8}\right)^{2}` is $\frac{9x^{2}}{64}$, so the term is $- \frac{x^{2}}{64}$

`2 \left[1 + \frac{x}{8} - \frac{x^{2}}{64}\right]`

**[A1]**

Multiply every term inside the bracket by 2

`\left(8 + 3 x\right)^{\frac{1}{3}} = 2 + \frac{1}{4} x - \frac{1}{32} x^{2}`

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the binomial series with $n = \frac{1}{3}$ and your $q x$ substituted, with the correct denominator $2 !$ on the third term.
> 
> **A1**: A correct expansion, following through from your value of $q$ in part (a).
> 
> **A1**: The fully correct simplified answer, $2 + \frac{1}{4} x - \frac{1}{32} x^{2}$.
> 
> The factor of $p$ may be multiplied in at the start or at the end; both are accepted.
> 
> The question asks for exact fractions in their lowest terms, so decimal coefficients do not earn the final mark.
> 
> Expanding without the factor of 2 and never reinstating it earns the method mark and the follow-through mark only.

> **[exam-tip]**
> Only two terms of the formula are needed, because the question stops at $x^{2}$.
> 
> - $u = \frac{3x}{8}$ is a term in $x$, so $u^{2}$ is the $x^{2}$ term and there is nothing beyond it to write
> 
> Square the whole of $\frac{3x}{8}$, not just the $x$.
> 
> - `\left(\frac{3 x}{8}\right)^{2}` is $\frac{9x^{2}}{64}$, and it is the 9 on top that cancels with the 9 in $- \frac{1}{9}$ to give the tidy $- \frac{x^{2}}{64}$
> 
> Do not lose the factor of 2 from part (a).
> 
> - Every term inside the bracket doubles, so $\frac{x}{8}$ becomes $\frac{x}{4}$ and $- \frac{x^{2}}{64}$ becomes $- \frac{x^{2}}{32}$
> - Leaving it out gives an expansion starting with 1 instead of 2, and `\left(8 + 0\right)^{\frac{1}{3}} = 2` is an instant check that the constant term must be 2
> 
> With $n = \frac{1}{3}$ the second coefficient is negative.
> 
> - $n - 1 = - \frac{2}{3}$, so the product `\frac{1}{3} \times \left(- \frac{2}{3}\right)` is negative and the $x^{2}$ term subtracts

### 6((c)) — 2 marks
The expansion approximates `\left(8 + 3 x\right)^{\frac{1}{3}}`, so choose the value of $x$ that makes the inside equal to 9

$8 + 3 x = 9$

$x = \frac{1}{3}$

**[M1]**

Check the value is allowed, since the expansion needs `\left|\frac{3 x}{8}\right| < 1`, that is $- \frac{8}{3} < x < \frac{8}{3}$

- $\frac{1}{3}$ lies comfortably inside that range

Substitute $x = \frac{1}{3}$ into the expansion from part (b)

`2 + \frac{1}{4} \times \frac{1}{3} - \frac{1}{32} \times \left(\frac{1}{3}\right)^{2}`

Work out each term, then write all three over a common denominator of 288

- $2 = \frac{576}{288}$, $\frac{1}{12} = \frac{24}{288}$ and $\frac{1}{288}$ is already there

$\frac{576+24-1}{288}$

`\sqrt[3]{9} \approx \frac{599}{288} \textrm{ } \text{as required}`

**[A1]**

> **[mark-scheme]**
> **M1**: Substitutes $x = \frac{1}{3}$ into your expansion from part (b).
> 
> **A1**: Reaches the printed fraction $\frac{599}{288}$ with no errors seen.
> 
> Because the result is printed in the question, the working has to arrive at it rather than assume it, and every intermediate step must be correct.
> 
> Any correct route to the common denominator is accepted, as is combining the three terms in any order.

> **[exam-tip]**
> Work backwards from the number you are asked to approximate.
> 
> - You want `\sqrt[3]{9}`, and the expansion gives `\left(8 + 3 x\right)^{\frac{1}{3}}`, so set $8 + 3 x = 9$
> - Writing 9 as $8 + 1$ makes it obvious that $3 x = 1$
> 
> A small value of $x$ is what makes the approximation good.
> 
> - $\frac{1}{3}$ is well inside the valid range, so three terms already give five figure accuracy
> - $\frac{599}{288}$ is $2 . 0798 \dots$ against the true `\sqrt[3]{9} = 2 . 0800 \ldots`
> 
> Keep everything as fractions, since the answer is printed as one.
> 
> - Converting to decimals part way through makes the exact $\frac{599}{288}$ impossible to recover
> - The denominator 288 comes from $4 \times 3$ and $32 \times 9$, so it is the lowest common multiple of 12 and 288
> 
> A printed answer means the working earns the marks.
> 
> - Writing $\frac{599}{288}$ with no substitution shown scores nothing here
