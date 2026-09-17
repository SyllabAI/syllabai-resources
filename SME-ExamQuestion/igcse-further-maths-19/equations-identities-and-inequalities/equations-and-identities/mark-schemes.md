# Mark Schemes — Equations & Identities
**Equations, Identities & Inequalities** · Edexcel IGCSE Further Pure Maths (4PM1)


## Q1 — medium — 10 marks · exam-questions

### 4((a)) — 6 marks
The factor theorem says that if `\left(x + 3\right)` is a factor then `\text{f}\left(- 3\right)` must be zero

Substitute $x = - 3$ into `\text{f}\left(x\right)` and set the result equal to zero

`2 \left(- 3\right)^{3} + p \left(- 3\right)^{2} + q \left(- 3\right) + 12 = 0`

**[M1]**

Work out the numerical parts

$- 54 + 9 p - 3 q + 12 = 0$

$9 p - 3 q = 42$

Divide every term by 3 to keep the numbers small

$3 p - q = 14$

**[M1]**

The second piece of information is about `\text{f}'\left(x\right)`, so differentiate `\text{f}\left(x\right)` term by term

`\text{f}'\left(x\right) = 6 x^{2} + 2 p x + q`

The remainder theorem says that the remainder on dividing by `\left(x + 3\right)` is the value of the function at $x = - 3$

Substitute $x = - 3$ into `\text{f}'\left(x\right)` and set the result equal to 37

`6 \left(- 3\right)^{2} + 2 p \left(- 3\right) + q = 37`

**[M1]**

Tidy this into a second equation connecting $p$ and $q$

$54 - 6 p + q = 37$

$q = 6 p - 17$

**[A1]**

There are now two equations in two unknowns, so solve them simultaneously

Substituting the expression for $q$ into the first equation is the quickest route

`3 p - \left(6 p - 17\right) = 14`

**[M1]**

Take care with the bracket, because subtracting $- 17$ gives $+ 17$

$- 3 p + 17 = 14$

$- 3 p = - 3$

$p = 1  \text{as required}$

Substitute $p = 1$ back into either equation to find $q$

`q = 6 \left(1\right) - 17`

$q = - 11$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitutes $x = - 3$ into `\text{f}\left(x\right)` and sets the result equal to zero.
> 
> **M1**: Reaches a correct equation connecting $p$ and $q$, such as $3 p - q = 14$, simplified or not.
> 
> **M1**: Differentiates to `\text{f}'\left(x\right) = 6 x^{2} + 2 p x + q`, then substitutes $x = - 3$ and sets the result equal to 37.
> 
> **A1**: Correct second equation connecting $p$ and $q$, such as $q = 6 p - 17$.
> 
> **M1**: Solves the two equations simultaneously, by any method.
> 
> **A1**: $q = - 11$, with $p = 1$ reached from working containing no errors.
> 
> Because $p = 1$ is printed in the question, the working leading to it has to be completely correct. The value of $q$ then follows through from your own pair of equations.
> 
> Elimination is equally acceptable and is marked in the same way, with the method mark for a complete attempt to eliminate one unknown between your two equations, and the final mark for both values correct.

> **[exam-tip]**
> The factor theorem and the remainder theorem are the same idea with different right-hand sides.
> 
> - A factor `\left(x - a\right)` means the function is zero at $x = a$
> - A remainder of $r$ on dividing by `\left(x - a\right)` means the function equals $r$ at $x = a$
> 
> The trap here is applying the remainder condition to `\text{f}\left(x\right)` instead of to `\text{f}'\left(x\right)`. Check which function each sentence is talking about before you substitute.
> 
> Once you have $p = 1$, use it rather than starting again.
> 
> - Substituting into $3 p - q = 14$ gives $3 - q = 14$, so $q = - 11$ in one line
> - The other equation gives the same value, which is a quick way of checking your answer

### 4((b)) — 2 marks
Part (a) gives $p = 1$ and $q = - 11$, so the cubic is now fully known

`\text{f}\left(x\right) = 2 x^{3} + x^{2} - 11 x + 12`

Dividing a cubic by a linear factor always leaves a quadratic, so write the factorisation with unknown coefficients

`2 x^{3} + x^{2} - 11 x + 12 = \left(x + 3\right) \left(a x^{2} + b x + c\right)`

Compare the $x^{3}$ terms on each side

- On the right the only $x^{3}$ term comes from $x \times a x^{2}$

$a = 2$

Compare the constant terms

- On the right the only constant comes from $3 \times c$

$3 c = 12$

$c = 4$

Compare the $x^{2}$ terms, which come from $x \times b x$ and from $3 \times a x^{2}$

$b + 3 a = 1$

$b + 6 = 1$

$b = - 5$

**[M1]**

Check whether the quadratic factor breaks down any further

- You would need two numbers multiplying to $2 \times 4 = 8$ and adding to $- 5$, and there is no such pair
- So the quadratic has no linear factors and the factorisation is complete

`\text{f}\left(x\right) = \left(x + 3\right) \left(2 x^{2} - 5 x + 4\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Compares coefficients, or divides `\text{f}\left(x\right)` by `\left(x + 3\right)`, reaching a quadratic factor of the form $2 x^{2} + b x + c$.
> 
> **A1**: `\text{f}\left(x\right) = \left(x + 3\right) \left(2 x^{2} - 5 x + 4\right)`.
> 
> Algebraic long division is equally acceptable and is marked in the same way, with the method mark for a division that reaches the first two terms of the quotient correctly, and the accuracy mark for the fully correct factorised form.
> 
> The quadratic factor cannot be broken down further, so no extra working is expected. The product must be written out as a product for the final mark, since simply stating the quadratic factor does not answer the question.

> **[exam-tip]**
> "Factorise completely" means keep going until nothing else will come apart.
> 
> - Always test the quadratic factor before writing your final line
> - Here $2 x^{2} - 5 x + 4$ has no factors, so the answer stays as a linear factor times a quadratic
> 
> Comparing coefficients and long division produce exactly the same quadratic, so use whichever you are more confident with.
> 
> - Comparing coefficients avoids the repeated subtractions where long division usually goes wrong
> - Whichever you choose, multiply your answer back out as a check

### 4((c)) — 2 marks
Use the factorised form from part (b)

`\left(x + 3\right) \left(2 x^{2} - 5 x + 4\right) = 0`

The linear factor gives one root immediately

$x = - 3$

Any other real roots would have to come from the quadratic factor, so test that with the discriminant

- Here $a = 2$, $b = - 5$ and $c = 4$

`b^{2} - 4 a c = \left(- 5\right)^{2} - 4 \left(2\right) \left(4\right)`

$b^{2} - 4 a c = - 7$

**[M1]**

The discriminant is negative, so the quadratic factor has no real roots

**Final answer:** **The discriminant is negative, so **$2 x^{2} - 5 x + 4 = 0$** has no real roots, and **$x = - 3$** is the only real root of **`\text{f}\left(x\right) = 0`

**[A1]**

> **[mark-scheme]**
> **M1**: Evaluates the discriminant of the quadratic factor, or applies the quadratic formula to it, or completes the square on it.
> 
> **A1**: Discriminant of $- 7$, together with a conclusion that the quadratic has no real roots and that $x = - 3$ is therefore the only real root.
> 
> The conclusion may be brief, but it has to refer to the discriminant being negative. "It does not factorise" on its own earns nothing, because a quadratic can have real roots without factorising neatly.
> 
> Completing the square is equally acceptable and is marked in the same way, with the method mark for reaching `2 \left(x - \frac{5}{4}\right)^{2} + \frac{7}{8}` or an equivalent form, and the accuracy mark for the conclusion drawn from the positive constant.

> **[exam-tip]**
> Every cubic has at least one real root, so "only one real root" is really a statement about the quadratic factor.
> 
> - The linear factor supplies the root you already know
> - All the work is in showing the quadratic supplies none
> 
> Say why, not just what.
> 
> - Quote the value of the discriminant and state that it is negative, because that is the reason being asked for
> - A negative discriminant also tells you the curve never crosses the $x$-axis a second time, which is a useful way to picture it

## Q2 — medium — 6 marks · exam-questions

### 1((a)) — 2 marks
The factor theorem says that a factor `\left(3 x - 2\right)` makes `\text{f}\left(x\right)` zero when $3 x - 2 = 0$

Solve that to find which value of $x$ to substitute

$x = \frac{2}{3}$

Substitute $x = \frac{2}{3}$ into `\text{f}\left(x\right)` and set the result equal to zero

`6 \left(\frac{2}{3}\right)^{3} - 13 \left(\frac{2}{3}\right)^{2} + a \left(\frac{2}{3}\right) - 10 = 0`

**[M1]**

Work out each numerical term separately, keeping everything in ninths

- $6 \times \frac{8}{27} = \frac{16}{9}$ and $13 \times \frac{4}{9} = \frac{52}{9}$

$\frac{16}{9} - \frac{52}{9} + \frac{2a}{3} - 10 = 0$

Combine the two fractions in ninths

$- 4 + \frac{2a}{3} - 10 = 0$

Collect the numbers and rearrange for $a$

$\frac{2a}{3} = 14$

$a = 21  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitutes $x = \frac{2}{3}$ into `\text{f}\left(x\right)` and sets the result equal to zero.
> 
> **A1**: Reaches $a = 21$ with no errors seen.
> 
> Substituting $x = - \frac{2}{3}$ still earns the method mark, but the accuracy mark needs $x = \frac{2}{3}$ used correctly.
> 
> Working backwards is also accepted: substituting $a = 21$ into `\text{f}\left(x\right)` earns the method mark, and showing that `\text{f}\left(\frac{2}{3}\right) = 0` earns the accuracy mark.
> 
> Algebraic long division is equally acceptable and is marked like this: dividing `\text{f}\left(x\right)` by `\left(3 x - 2\right)` and reaching a remainder condition such as $a - 6 = 15$ earns the method mark, and $a = 21$ with no errors earns the accuracy mark.

> **[exam-tip]**
> A factor of the form `\left(3 x - 2\right)` does not give $x = 2$ or $x = \frac{3}{2}$.
> 
> - Set the bracket equal to zero and solve it, which gives $x = \frac{2}{3}$
> - Getting this the wrong way up is the single most common error on this type of question
> 
> Fractional substitutions are much easier if you write every term over the same denominator.
> 
> - Here everything sits neatly over 9, so the two awkward terms combine to a whole number
> - Leave $a$ alone while you tidy the numbers, then rearrange once at the end

### 1((b)) — 4 marks
Intersections with the $x$-axis are the solutions of `\text{f}\left(x\right) = 0`, so start by factorising

Part (a) gives $a = 21$, so the cubic is now fully known

`\text{f}\left(x\right) = 6 x^{3} - 13 x^{2} + 21 x - 10`

Dividing a cubic by a linear factor leaves a quadratic, so write the factorisation with unknown coefficients

`6 x^{3} - 13 x^{2} + 21 x - 10 = \left(3 x - 2\right) \left(A x^{2} + B x + C\right)`

Compare the $x^{3}$ terms, which on the right come only from $3 x \times A x^{2}$

$3 A = 6$

$A = 2$

Compare the constant terms, which on the right come only from $- 2 \times C$

$- 2 C = - 10$

$C = 5$

Compare the $x^{2}$ terms, which come from $3 x \times B x$ and from $- 2 \times A x^{2}$

$3 B - 2 A = - 13$

$3 B - 4 = - 13$

$B = - 3$

**[M1]**

So the cubic factorises like this

`\text{f}\left(x\right) = \left(3 x - 2\right) \left(2 x^{2} - 3 x + 5\right)`

**[A1]**

The linear factor gives one intersection, at $x = \frac{2}{3}$

Any further intersections would come from the quadratic factor, so test it with the discriminant

- Here $a = 2$, $b = - 3$ and $c = 5$

`b^{2} - 4 a c = \left(- 3\right)^{2} - 4 \left(2\right) \left(5\right)`

$b^{2} - 4 a c = - 31$

**[M1]**

The discriminant is negative, so the quadratic factor is never zero

**Final answer:** **The discriminant is negative, so **$2 x^{2} - 3 x + 5 = 0$** has no real roots, and the only intersection with the **$x$**-axis is at **$x = \frac{2}{3}$

**[A1]**

> **[mark-scheme]**
> **M1**: Divides `\text{f}\left(x\right)` by `\left(3 x - 2\right)`, or compares coefficients, reaching a quadratic of the form $2 x^{2} + B x + C$.
> 
> **A1**: Correct quadratic factor $2 x^{2} - 3 x + 5$.
> 
> **M1**: Evaluates the discriminant of the quadratic factor, or completes the square on it. The discriminant may appear inside the quadratic formula, but it has to be worked out to a number.
> 
> **A1**: Value of $- 31$ together with a conclusion, which needs to say that the discriminant is negative so there are no real roots, and that the only intersection is at $x = \frac{2}{3}$.
> 
> Completing the square is equally acceptable and is marked in the same way, with the method mark for reaching `\left(x - \frac{3}{4}\right)^{2} = - \frac{31}{16}` or an equivalent form, and the accuracy mark for concluding from the negative right-hand side that there are no real roots.
> 
> The question says "show algebraically", so simply quoting the complex roots of the quadratic earns nothing. Complex roots have to be followed by a comment that they are not real, so give no intersections with the $x$-axis.

> **[exam-tip]**
> The word "hence" tells you the factor from part (a) is the way in.
> 
> - Do not start from scratch and try to solve the cubic
> - The factor you were given turns the problem into a quadratic in one step
> 
> A cubic crosses the $x$-axis once, twice or three times, so the question is really asking you to rule the quadratic out.
> 
> - A negative discriminant is the reason, so evaluate it and state that it is negative
> - Finish by naming the one intersection, since the question asks about the curve and not just about the quadratic
> 
> Sketching the curve, or saying it "looks like" it only crosses once, earns nothing here.
> 
> - "Show algebraically" means the discriminant or completing the square, not a graph

## Q3 — medium — 18 marks · exam-questions

### 10((a)) — 4 marks
The target form `A - B \left(x + C\right)^{2}` is a completed square, so complete the square on `\text{f}\left(x\right)`

Start by factorising $- 9$ out of the two terms containing $x$, leaving the constant outside

`3 - 9 \left(x^{2} + \frac{4}{9} x\right)`

Complete the square inside the bracket by halving the coefficient of $x$

- Half of $\frac{4}{9}$ is $\frac{2}{9}$, and `\left(\frac{2}{9}\right)^{2} = \frac{4}{81}`

`3 - 9 \left[\left(x + \frac{2}{9}\right)^{2} - \frac{4}{81}\right]`

**[M1]**

Multiply the $- 9$ through the square bracket, remembering that two negatives give a positive

`3 - 9 \left(x + \frac{2}{9}\right)^{2} + \frac{4}{9}`

Combine the two constants, writing 3 as $\frac{27}{9}$

`\frac{31}{9} - 9 \left(x + \frac{2}{9}\right)^{2}`

Compare this term by term with `A - B \left(x + C\right)^{2}`

$A=\frac{31}{9},B=9,C=\frac{2}{9}$

**[A1] [A1] [A1]**

> **[mark-scheme]**
> **M1**: A method to complete the square, reaching at least `3 - 9 \left[\left(x + \frac{2}{9}\right)^{2} + p\right]` or an equivalent arrangement, where $p$ is a constant.
> 
> **A1**: One of $A$, $B$ or $C$ correct.
> 
> **A1**: Two of $A$, $B$ or $C$ correct.
> 
> **A1**: All three correct.
> 
> The values may be stated explicitly or left embedded in a correct completed square, and a correct completed square implies all four marks. If they are embedded correctly and then stated wrongly, the correct embedded version is used. One or two correct values still need the method mark to have been earned first.
> 
> Expanding `A - B \left(x + C\right)^{2}` and equating coefficients is equally acceptable, and is marked like this: the method mark is for a correct expansion together with a correct attempt to equate at least one coefficient, for example $- B = - 9$ or $- 2 B C = - 4$, and the three accuracy marks are awarded exactly as above.

> **[exam-tip]**
> The printed form tells you the signs before you start.
> 
> - `A - B \left(x + C\right)^{2}` has a minus in front of the square, and all three constants are positive
> - So factorising out $- 9$ rather than $9$ is what makes the signs come out right
> 
> The accuracy marks are awarded one at a time, so a partly correct answer is still worth having.
> 
> - Getting only $B = 9$ right still earns a mark, so never leave this blank
> 
> Check by expanding your answer back out.
> 
> - `\frac{31}{9} - 9 \left(x + \frac{2}{9}\right)^{2}` expands to $\frac{31}{9} - 9 x^{2} - 4 x - \frac{4}{9}$, which is $3 - 4 x - 9 x^{2}$

### 10((b)) — 1 marks
Part (a) writes `\text{f}\left(x\right)` as `\frac{31}{9} - 9 \left(x + \frac{2}{9}\right)^{2}`

A square is never negative, so the term `- 9 \left(x + \frac{2}{9}\right)^{2}` is never positive

That means `\text{f}\left(x\right)` is largest when the square is zero, which happens at $x = - \frac{2}{9}$

- What is left at that point is the constant $A$

**Final answer:** **The maximum value of **`\text{f}\left(x\right)`** is **$\frac{31}{9}$

**[B1]**

> **[mark-scheme]**
> **B1**: $\frac{31}{9}$, or an equivalent value.
> 
> This follows through from your own value of $A$ in part (a), provided part (a) was written in the form `A - B \left(x + C\right)^{2}`.
> 
> Because the question says "hence", the value has to come from your part (a). A correct $\frac{31}{9}$ alongside incorrect working in part (a) does not earn the mark, although $\frac{31}{9}$ written down with no working in part (a) does.

> **[exam-tip]**
> Completed square form gives you the maximum or minimum without any calculus.
> 
> - The bracket squared is the only part that changes, and the smallest it can be is zero
> - With a minus in front of it, that zero gives the largest possible value
> 
> Read carefully whether the question wants the value or the point.
> 
> - "Maximum value" means the $y$ value alone, so $\frac{31}{9}$ is the complete answer
> - The coordinates of the maximum point would be `\left(- \frac{2}{9} , \frac{31}{9}\right)`, which is more than was asked for

### 10((c)) — 6 marks
Write the equation `\text{f}\left(x\right) = 0` in the standard quadratic form first

$9 x^{2} + 4 x - 3 = 0$

For $a x^{2} + b x + c = 0$, the sum of the roots is $- \frac{b}{a}$ and the product of the roots is $\frac{c}{a}$

$α + β = - \frac{4}{9}$

$α β = - \frac{1}{3}$

**[B1]**

Now build the sum of the two new roots, putting the fractions over a common denominator

`\frac{3 \alpha}{\beta} + \frac{3 \beta}{\alpha} = \frac{3 \left(\alpha^{2} + \beta^{2}\right)}{\alpha \beta}`

$α^{2} + β^{2}$ is not one of the standard results, so rewrite it using the identity `\alpha^{2} + \beta^{2} \equiv \left(\alpha + \beta\right)^{2} - 2 \alpha \beta`

`\frac{3 \alpha}{\beta} + \frac{3 \beta}{\alpha} = \frac{3 \left[\left(\alpha + \beta\right)^{2} - 2 \alpha \beta\right]}{\alpha \beta}`

**[M1]**

Substitute the values you have for $α + β$ and $α β$

`= \frac{3 \left[\left(- \frac{4}{9}\right)^{2} - 2 \left(- \frac{1}{3}\right)\right]}{- \frac{1}{3}}`

Work out the square bracket first, over a denominator of 81

- Writing $\frac{2}{3}$ as $\frac{54}{81}$ gives $\frac{16}{81} + \frac{54}{81}$, which is $\frac{70}{81}$

$= \frac{3\times\frac{70}{81}}{-\frac{1}{3}}$

Dividing by $- \frac{1}{3}$ is the same as multiplying by $- 3$

$\frac{3α}{β} + \frac{3β}{α} = - \frac{70}{9}$

**[A1]**

The product of the new roots is much easier, because $α$ and $β$ cancel

$\frac{3α}{β} \times \frac{3β}{α} = 9$

**[B1]**

A quadratic with a given sum and product of roots is `x^{2} - \left(\text{sum}\right) x + \left(\text{product}\right) = 0`

Subtracting a negative sum makes the middle term positive

$x^{2} + \frac{70}{9} x + 9 = 0$

**[M1]**

The question asks for integer coefficients, so multiply every term by 9

$9 x^{2} + 70 x + 81 = 0$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct values for $α + β$ and $α β$. These may be embedded in the later working rather than stated separately.
> 
> **M1**: Reaches a correct expression for the sum of the new roots, ready for your values of $α + β$ and $α β$ to be substituted.
> 
> **A1**: Correctly substitutes your values into a correct expression for the sum. Simplification is not necessary.
> 
> **B1**: Product of the new roots equal to 9.
> 
> **M1**: Uses `x^{2} - \left(\text{your sum}\right) x + \left(\text{your product}\right)`. The $= 0$ may be missing, and this mark is not dependent on the earlier ones, so a clear substitution of anything identifiable as your sum and product earns it.
> 
> **A1**: $9 x^{2} + 70 x + 81 = 0$, or any equivalent equation with integer coefficients. It must include $= 0$.
> 
> It is possible to reach the correct final equation from $α + β = + \frac{4}{9}$, because the sum only ever appears squared. That is a correct equation from incorrect working, so it does not earn the final accuracy mark.
> 
> The question says "without solving the equation", so finding $α$ and $β$ themselves and building the new equation from them is not a valid method here.

> **[exam-tip]**
> The whole method rests on two standard results, so write them down first.
> 
> - Sum of roots is $- \frac{b}{a}$ and product of roots is $\frac{c}{a}$, and there is a mark just for having them
> - Rearrange into $a x^{2} + b x + c = 0$ before reading them off, since $3 - 4 x - 9 x^{2}$ is written back to front
> 
> Anything of the form $α^{2} + β^{2}$ has to be converted before you can substitute.
> 
> - `\alpha^{2} + \beta^{2} \equiv \left(\alpha + \beta\right)^{2} - 2 \alpha \beta` is the identity that does it
> - Trying to substitute $α$ and $β$ individually defeats the point of the question
> 
> The sign of the middle term catches people out.
> 
> - The new equation is `x^{2} - \left(\text{sum}\right) x + \left(\text{product}\right) = 0`, and here the sum is negative, so the middle term comes out positive
> 
> Finish the job the question asks for.
> 
> - "Integer coefficients" means clearing the ninth, so $x^{2} + \frac{70}{9} x + 9 = 0$ is not yet the answer

### 10((d)) — 1 marks
Start from the left-hand side and expand it

- `\left(x + y\right)^{3}` can be done as `\left(x + y\right) \left(x + y\right)^{2}`, or straight from the binomial expansion

`\left(x + y\right)^{3} = x^{3} + 3 x^{2} y + 3 x y^{2} + y^{3}`

The two middle terms share a common factor of $3 x y$, so take it out

`3 x^{2} y + 3 x y^{2} = 3 x y \left(x + y\right)`

Putting that back gives the printed identity

`\left(x + y\right)^{3} = x^{3} + y^{3} + 3 x y \left(x + y\right) \textrm{ } \text{as required}`

**[B1]**

> **[mark-scheme]**
> **B1**: Complete and correct algebra showing the printed identity, with no errors and nothing omitted.
> 
> The minimum expected is the full expansion followed by the regrouping of the two middle terms. Extra steps are allowed and are checked.
> 
> Starting from the right-hand side and expanding `3 x y \left(x + y\right)` to arrive at the left-hand side is equally acceptable.
> 
> Where the brackets are expanded in full, missing brackets may be recovered if the following work is correct.

> **[exam-tip]**
> One mark does not mean one line, but it does mean nothing may be skipped.
> 
> - Show the full expansion and then the regrouping, since either half on its own leaves a gap
> 
> Work from the more complicated side towards the simpler one.
> 
> - Expanding `\left(x + y\right)^{3}` and tidying is easier to follow than trying to build the cube up from scratch
> 
> This identity is not decoration, it is the tool for part (e).
> 
> - Rearranged, it says `x^{3} + y^{3} = \left(x + y\right)^{3} - 3 x y \left(x + y\right)`, which turns a sum of cubes into the sum and product of the roots

### 10((e)) — 6 marks
The two new roots are $α^{2} - β$ and $β^{2} - α$, so find their sum first

`\left(\alpha^{2} - \beta\right) + \left(\beta^{2} - \alpha\right) = \alpha^{2} + \beta^{2} - \left(\alpha + \beta\right)`

Rewrite $α^{2} + β^{2}$ with the same identity used in part (c)

`= \left(\alpha + \beta\right)^{2} - 2 \alpha \beta - \left(\alpha + \beta\right)`

**[M1]**

Substitute $α + β = - \frac{4}{9}$ and $α β = - \frac{1}{3}$ from part (c)

`= \left(- \frac{4}{9}\right)^{2} - 2 \left(- \frac{1}{3}\right) - \left(- \frac{4}{9}\right)`

Work this out over a common denominator of 81

- $\frac{16}{81} + \frac{54}{81} + \frac{36}{81} = \frac{106}{81}$

`\left(\alpha^{2} - \beta\right) + \left(\beta^{2} - \alpha\right) = \frac{106}{81}`

**[A1]**

Now the product of the new roots, expanded term by term

`\left(\alpha^{2} - \beta\right) \left(\beta^{2} - \alpha\right) = \alpha^{2} \beta^{2} + \alpha \beta - \alpha^{3} - \beta^{3}`

**[M1]**

Every term except $α^{3} + β^{3}$ is already in terms of the sum and product, and that is what part (d) is for

Rearranging the identity with $x = α$ and $y = β$ gives `\alpha^{3} + \beta^{3} = \left(\alpha + \beta\right)^{3} - 3 \alpha \beta \left(\alpha + \beta\right)`

`\alpha^{3} + \beta^{3} = \left(- \frac{4}{9}\right)^{3} - 3 \left(- \frac{1}{3}\right) \left(- \frac{4}{9}\right)`

$α^{3} + β^{3} = - \frac{388}{729}$

**[M1]**

Substitute that, together with $α^{2} β^{2} = \frac{1}{9}$ and $α β = - \frac{1}{3}$

`\left(\alpha^{2} - \beta\right) \left(\beta^{2} - \alpha\right) = \frac{1}{9} - \frac{1}{3} + \frac{388}{729}`

Put everything over 729

`\left(\alpha^{2} - \beta\right) \left(\beta^{2} - \alpha\right) = \frac{226}{729}`

For $3 x^{2} + q x + r = 0$ the sum of the roots is $- \frac{q}{3}$ and the product is $\frac{r}{3}$

$- \frac{q}{3} = \frac{106}{81}$

$\frac{r}{3} = \frac{226}{729}$

**[M1]**

Solve each one, cancelling the fractions down

$q=-\frac{106}{27},r=\frac{226}{243}$

**[A1]**

> **[mark-scheme]**
> **M1**: Reaches a correct expression for the sum of the new roots, ready for your values of $α + β$ and $α β$ to be substituted.
> 
> **M1**: Correctly substitutes your values into that expression for the sum.
> 
> **M1**: Correct expanded expression for the product of the new roots, in any equivalent form ready for substitution.
> 
> **M1**: Uses the identity from part (d) to write $α^{3} + β^{3}$ in terms of $α + β$ and $α β$.
> 
> **M1**: Equates your sum of roots to $- \frac{q}{3}$, or your product of roots to $\frac{r}{3}$. This mark is only available once all three earlier method marks have been earned, and it can be implied by a correct value of $q$ or of $r$.
> 
> **A1**: Both $q = - \frac{106}{27}$ and $r = \frac{226}{243}$.
> 
> A value of $α^{2} + β^{2}$ carried across from part (c) is accepted and can imply the first two marks, provided it is correct for your own sum and product and the working for it is shown.
> 
> The expression for the product may be built up in stages, with the values substituted part way through rather than at the end.

> **[exam-tip]**
> "Using your answer to part (d)" is an instruction, not a suggestion.
> 
> - The only awkward term in the product is $α^{3} + β^{3}$, and part (d) is exactly what converts it
> - Spotting which term the identity is for is most of the battle
> 
> Expand the product carefully, because there are four terms and two of them are negative.
> 
> - `\left(\alpha^{2} - \beta\right) \left(\beta^{2} - \alpha\right)` gives $α^{2} β^{2}$, $- α^{3}$, $- β^{3}$ and $+ α β$
> - The cubes appear with a minus sign, so the $- \frac{388}{729}$ becomes a $+$ when it is substituted
> 
> Watch which coefficient goes with which formula.
> 
> - `\text{g}\left(x\right)` has a leading coefficient of 3, not 1, so the sum is $- \frac{q}{3}$ and the product is $\frac{r}{3}$
> - Forgetting to divide by 3 gives answers three times too small
> 
> Keep everything in fractions to the very end, since the question asks for exact form.
> 
> - Denominators of 81 and 729 look ugly, but they cancel down neatly to 27 and 243

## Q4 — medium — 16 marks · exam-questions

### 7((a)) — 2 marks
The factor theorem says `\left(4 x - 1\right)` is a factor exactly when `\text{f}\left(x\right)` is zero at the value of $x$ that makes the bracket zero

Solve $4 x - 1 = 0$ to find which value to substitute

$x = \frac{1}{4}$

Substitute $x = \frac{1}{4}$ into `\text{f}\left(x\right)`

`64 \left(\frac{1}{4}\right)^{3} - 64 \left(\frac{1}{4}\right)^{2} + 3`

**[M1]**

Work out each term, using `\left(\frac{1}{4}\right)^{3} = \frac{1}{64}` and `\left(\frac{1}{4}\right)^{2} = \frac{1}{16}`

$1 - 4 + 3$

This comes to zero, which is exactly the condition the factor theorem needs

**Final answer:** `\text{f}\left(\frac{1}{4}\right) = 0`**, so **`\left(4 x - 1\right)`** is a factor of **`\text{f}\left(x\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Substitutes $x = \frac{1}{4}$ into `\text{f}\left(x\right)`.
> 
> **A1**: Shows the result is zero and states a conclusion, with no errors seen. A very brief conclusion is accepted.
> 
> Substituting $x = - \frac{1}{4}$ still earns the method mark, but not the accuracy mark.
> 
> Dividing `\text{f}\left(x\right)` by `\left(4 x - 1\right)` is equally acceptable, and is marked like this: a division reaching at least $16 x^{2} - 12 x$ earns the method mark, and a remainder of zero together with a conclusion earns the accuracy mark.

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
> **M1**: Divides `\text{f}\left(x\right)` by `\left(4 x - 1\right)`, or compares coefficients, reaching the quadratic factor $16 x^{2} - 12 x - 3$.
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

## Q5 — medium — 9 marks · exam-questions

### 8() — 9 marks
You are given the gradient function, so integrate to get back to `\text{f}\left(x\right)`

Increase each index by one and divide by the new index

`\text{f}\left(x\right) = \frac{18 x^{3}}{3} - \frac{2 x^{2}}{2} + 13 x + c`

**[M1]**

Simplify the coefficients

`\text{f}\left(x\right) = 6 x^{3} - x^{2} + 13 x + c`

**[A1]**

The constant of integration is essential here, because it is the unknown the factor condition will find

A factor `\left(2 x - 1\right)` makes `\text{f}\left(x\right)` zero when $2 x - 1 = 0$, so substitute $x = \frac{1}{2}$

`6 \left(\frac{1}{2}\right)^{3} - \left(\frac{1}{2}\right)^{2} + 13 \left(\frac{1}{2}\right) + c = 0`

**[M1]**

Work out each numerical term

$\frac{3}{4} - \frac{1}{4} + \frac{13}{2} + c = 0$

Collect the numbers, which come to 7

$c = - 7$

**[A1]**

Put the constant back in to get the full cubic

`\text{f}\left(x\right) = 6 x^{3} - x^{2} + 13 x - 7`

**[A1]**

Intersections with the $x$-axis are the solutions of `\text{f}\left(x\right) = 0`, so factorise using the known factor

Write the cubic as `\left(2 x - 1\right)` multiplied by a quadratic

`6 x^{3} - x^{2} + 13 x - 7 = \left(2 x - 1\right) \left(A x^{2} + B x + C\right)`

Compare the $x^{3}$ terms, which on the right come only from $2 x \times A x^{2}$

$2 A = 6$

$A = 3$

Compare the constant terms, which on the right come only from $- 1 \times C$

$- C = - 7$

$C = 7$

Compare the $x^{2}$ terms, which come from $2 x \times B x$ and from $- 1 \times A x^{2}$

$2 B - 3 = - 1$

$B = 1$

**[M1]**

So the cubic factorises like this

`\text{f}\left(x\right) = \left(2 x - 1\right) \left(3 x^{2} + x + 7\right)`

**[A1]**

The linear factor gives one intersection, at $x = \frac{1}{2}$

Any further intersections would have to come from the quadratic factor, so test it with the discriminant

- Here $a = 3$, $b = 1$ and $c = 7$

`b^{2} - 4 a c = 1^{2} - 4 \left(3\right) \left(7\right)`

$b^{2} - 4 a c = - 83$

**[M1]**

The discriminant is negative, so the quadratic factor is never zero

**Final answer:** **The discriminant is negative, so **$3 x^{2} + x + 7 = 0$** has no real roots, and the only intersection with the **$x$**-axis is at **`\left(\frac{1}{2} , 0\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Integrates `\text{f}'\left(x\right)`, with at least two terms correct and no term differentiated instead. The constant of integration is not needed for this mark, and the expression may be left unsimplified.
> 
> **A1**: Correct integrated expression. Ignore the absence of $+ c$ here.
> 
> **M1**: Substitutes $x = \frac{1}{2}$ into your integrated expression, which must include $+ c$, and sets the result equal to zero.
> 
> **A1**: $c = - 7$.
> 
> **A1**: Fully correct `\text{f}\left(x\right) = 6 x^{3} - x^{2} + 13 x - 7`, written out on one line. The label `\text{f}\left(x\right) =` is not needed, and the expression is accepted where it appears as the dividend of a division or in an equating-coefficients statement.
> 
> **M1**: Divides your `\text{f}\left(x\right)` by `\left(2 x - 1\right)`, reaching at least $3 x^{2} + x$, or compares coefficients and obtains correct values for the first two coefficients. Allow this even without the correct constant of integration.
> 
> **A1**: Correct quadratic factor $3 x^{2} + x + 7$. Dividing instead by `\left(x - \frac{1}{2}\right)` gives $6 x^{2} + 2 x + 14$, which is equally acceptable.
> 
> **M1**: Uses $b^{2} - 4 a c$ on your quadratic factor, which must have three terms. The discriminant may appear inside the quadratic formula. Sight of the non-real roots $\frac{-1\pm\sqrt{83}\text{i}}{6}$ also earns this mark.
> 
> **A1**: Concludes that because $b^{2} - 4 a c$ is negative there is only one root, so only one intersection with the $x$-axis. This mark needs completely correct working throughout, including the constant of integration.
> 
> Statements such as "not possible" or "it will not factorise" are not accepted without a reference to the negative discriminant. A statement such as $1^{2} < 4 \times 3 \times 7$ is enough, and the discriminant may be left embedded in the formula rather than evaluated separately.
> 
> If you quote the non-real roots, you must add a comment that they are not real and so give no intersections with the $x$-axis. Quoting them alone earns nothing.
> 
> Algebraic long division is equally acceptable throughout and is marked in exactly the same way.

> **[exam-tip]**
> The constant of integration is the whole point of this question.
> 
> - Without $+ c$ there is nothing for the factor condition to find, and the final mark is lost even if everything else is right
> - The factor `\left(2 x - 1\right)` is not there to be factorised out, it is there to pin down $c$
> 
> A factor of `\left(2 x - 1\right)` means $x = \frac{1}{2}$, not $x = 2$.
> 
> - Set the bracket equal to zero and solve it every time
> 
> The question is really two questions joined together: find the cubic, then rule out extra roots.
> 
> - Once the cubic is known, everything else is the standard factor-and-discriminant routine
> - Quote the value of the discriminant and say that it is negative, because that is the reason the conclusion rests on

## Q6 — medium — 8 marks · exam-questions

### 3((a)) — 5 marks
You are given the gradient function, so integrate to get back to `\text{g}\left(x\right)`

Increase each index by one and divide by the new index

`\text{g}\left(x\right) = \frac{m x^{3}}{3} - 5 x^{2} - 37 x + c`

**[M1]**

The constant of integration matters here, because there are two unknowns to find

The curve passes through `\left(1 , 20\right)`, so substitute $x = 1$ and `\text{g}\left(x\right) = 20`

$\frac{m}{3} - 5 - 37 + c = 20$

$\frac{m}{3} + c = 62$

**[M1]**

The factor theorem gives a second equation, because a factor `\left(x - 5\right)` makes `\text{g}\left(5\right)` zero

$\frac{125m}{3} - 125 - 185 + c = 0$

$\frac{125m}{3} + c = 310$

**[M1]**

Subtract the first equation from the second, which eliminates $c$

$\frac{124m}{3} = 248$

$m = 6$

**[M1]**

Substitute $m = 6$ back into the first equation to find $c$

$2 + c = 62$

$c = 60$

Put both values into the integrated expression, noting that $\frac{6}{3} = 2$

`\text{g}\left(x\right) = 2 x^{3} - 5 x^{2} - 37 x + 60 \textrm{ } \text{as required}`

**[A1]**

> **[mark-scheme]**
> **M1**: Integrates `\text{g}'\left(x\right)`, with at least one index increased by one and divided by the new index. The constant of integration is not needed for this mark.
> 
> **M1**: Substitutes $x = 1$ and $y = 20$ to form an equation in $m$ and $c$. This mark is only available if the first method mark has been earned, and the equation does not have to be simplified.
> 
> **M1**: Uses the factor `\left(x - 5\right)` correctly, by substituting $x = 5$ and `\text{g}\left(x\right) = 0` into your own `\text{g}\left(x\right)`, which must be a cubic with four terms.
> 
> **M1**: Uses a valid and complete method to solve the two equations in $m$ and $c$. Allow up to two errors.
> 
> **A1**: The printed function reached with no errors anywhere in the working.
> 
> A fully correct equation with no incorrect working can imply either of the substitution marks, so the substitution itself need not be written out.
> 
> Writing `\text{g}\left(x\right)` as `\left(x - 5\right) \left(\frac{m}{3} x^{2} + b x - \frac{c}{5}\right)` and comparing coefficients is equally acceptable, and replaces the third and fourth method marks: the third is for a correct statement of that form for your own `\text{g}\left(x\right)`, and the fourth for a complete method solving the resulting equations in three unknowns.
> 
> Starting from the printed answer earns partial credit only. Differentiating it to recover $m = 6$, or substituting $x = 5$ or $x = 1$ into it to verify the given conditions, is worth one mark each up to a maximum of three, and cannot earn the final accuracy mark.

> **[exam-tip]**
> The constant of integration is the whole question here, not an afterthought.
> 
> - Without $+ c$ you have one unknown and two conditions, and the question becomes impossible
> - Two unknowns is exactly why you are given two separate pieces of information
> 
> Keep $m$ as a fraction over 3 rather than clearing it early.
> 
> - Subtracting the equations then removes $c$ in a single step
> - $\frac{125m}{3} - \frac{m}{3} = \frac{124m}{3}$, and $248 \div \frac{124}{3} = 6$
> 
> This is a show that question, so the final line must be reached rather than assumed.
> 
> - Verifying the printed answer instead of deriving it cannot score the accuracy mark

### 3((b)) — 3 marks
Part (a) gives the cubic, and `\left(x - 5\right)` is known to be a factor of it

Write the cubic as that factor multiplied by a quadratic

`2 x^{3} - 5 x^{2} - 37 x + 60 = \left(x - 5\right) \left(A x^{2} + B x + C\right)`

Compare the $x^{3}$ terms, which on the right come only from $x \times A x^{2}$

$A = 2$

Compare the constant terms, which on the right come only from $- 5 \times C$

$- 5 C = 60$

$C = - 12$

Compare the $x^{2}$ terms, which come from $x \times B x$ and from $- 5 \times A x^{2}$

$B - 10 = - 5$

$B = 5$

**[M1]**

Now factorise the quadratic, looking for two numbers that multiply to `2 \times \left(- 12\right) = - 24` and add to 5

- Those numbers are 8 and $- 3$, so split the middle term and factorise in pairs

$2 x^{2} + 8 x - 3 x - 12$

`2 x \left(x + 4\right) - 3 \left(x + 4\right)`

`2 x^{2} + 5 x - 12 = \left(2 x - 3\right) \left(x + 4\right)`

So the equation becomes a product of three linear factors

`\left(x - 5\right) \left(2 x - 3\right) \left(x + 4\right) = 0`

**[M1]**

Set each factor equal to zero in turn

$x=5,x=\frac{3}{2},x=-4$

**[A1]**

> **[mark-scheme]**
> **M1**: Reaches the quadratic factor $2 x^{2} + 5 x - 12$, by comparing coefficients or by division.
> 
> **M1**: A valid and complete attempt to solve that quadratic, by factorising, completing the square or the quadratic formula, giving two values of $x$ in addition to $x = 5$.
> 
> **A1**: All three values, $x = 5$, $x = \frac{3}{2}$ and $x = - 4$.
> 
> Algebraic long division is equally acceptable and earns the first method mark in the same way.
> 
> The second method mark follows through from an incorrect quadratic, provided the method used on it is correct. Accept $x = 1 . 5$ for $\frac{3}{2}$.
> 
> The question says to use algebra, so a set of three correct values obtained from a graph or written down with no supporting work does not earn the method marks.

> **[exam-tip]**
> "Hence, or otherwise" is a strong hint that part (a) is meant to be used.
> 
> - The cubic and one of its factors are both already available
> - Starting again from `\text{g}'\left(x\right)` wastes time and earns nothing extra
> 
> When the leading coefficient is not 1, factorising by splitting the middle term is the reliable route.
> 
> - Multiply the outer coefficients, `2 \times \left(- 12\right) = - 24`, then find the pair adding to the middle coefficient
> - If no pair works, the quadratic formula always will
> 
> The command word is solve, so give the values of $x$ rather than the factorised cubic.

## Q7 — medium — 13 marks · exam-questions

### 2((a)) — 4 marks
Perpendicular lines have gradients that multiply to give $- 1$, so start with the gradient of $A B$

Use $A ( - 5 , 3 )$ and $B ( 4 , 0 )$

$m_{AB} = \frac{0-3}{4-(-5)}$

$m_{AB} = - \frac{1}{3}$

**[M1]**

The gradient of $l$ is the negative reciprocal of this

$m_{l} = 3$

**[M1]**

Now use $y - y_{1} = m ( x - x_{1} )$ with gradient $3$ and the point $C ( - 1 , 5 )$

$y - 5 = 3 ( x + 1 )$

**[M1]**

Rearrange into the form asked for, with every term on one side and integer coefficients

$y - 5 = 3 x + 3$

$3 x - y + 8 = 0$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method for the gradient of $A B$.
> 
> **M1**: Negative reciprocal of your gradient of $A B$.
> 
> **M1**: Correct method for the equation of a line through $C ( - 1 , 5 )$ using your perpendicular gradient.
> 
> **A1**: Correct equation in the required form.
> 
> The first three marks all follow through from your own earlier values, so an arithmetic slip in the gradient does not stop you earning them.
> 
> For the final mark accept $3 x - y + 8 = 0$, or any equivalent equation with integer coefficients such as $- 3 x + y - 8 = 0$. The equation must be arranged with zero on one side, as the question requires.

> **[exam-tip]**
> The negative reciprocal is the step most often fumbled, especially with a fractional gradient.
> 
> - Turn the fraction upside down and change the sign, so $- \frac{1}{3}$ becomes $3$
> - Check it by multiplying: the two gradients must give $- 1$
> 
> Read the required form before you rearrange. Marks are lost here for stopping at $y = 3 x + 8$ when the question asked for $a x + b y + c = 0$ with integer coefficients.

### 2((b)) — 3 marks
$D$ is where $l$ meets $A B$, so you need the equation of $A B$ as well

$A B$ has gradient $- \frac{1}{3}$ from part (a) and passes through $B ( 4 , 0 )$

$y - 0 = - \frac{1}{3} ( x - 4 )$

$3 y = 4 - x$

**[M1]**

Solve this together with the equation of $l$

Part (a) gives $l$ as $y = 3 x + 8$, so substitute that in

$3 ( 3 x + 8 ) = 4 - x$

$9 x + 24 = 4 - x$

$10 x = - 20$

$x = - 2$

**[M1]**

Substitute back into either equation to find $y$

$y = 3 ( - 2 ) + 8$

$y = 2$

$D = ( - 2 , 2 )  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct equation for $A B$, which does not have to be simplified.
> 
> **M1**: Attempt to solve the two equations simultaneously, eliminating one variable and reaching a value for $x$ or $y$.
> 
> **A1**: Both coordinates obtained with no errors.
> 
> Allow one processing error in the solving for the second mark. The final mark needs completely correct working, because the answer is given in the question.
> 
> A verification is equally acceptable, and is marked like this: the first mark is still for a correct equation of $A B$. Substituting $( - 2 , 2 )$ correctly into either $A B$ or $l$ earns the second mark, and substituting it correctly into both, together with a brief conclusion, earns the third. The conclusion can be as short as "shown".

> **[exam-tip]**
> The equation of $l$ is already done, so do not start it again. Only $A B$ is new here.
> 
> When the answer is printed in the question, every line of working has to be right.
> 
> - A "show that" mark is not given for a correct answer that arrives through faulty working
> - Finish by stating the result, so it is clear you have reached it rather than assumed it
> 
> Substituting the given point into both equations is a legitimate alternative and is quicker. Do both equations though, since checking only one shows the point lies on that line, not that it is the intersection.

### 2((c)) — 2 marks
A perpendicular bisector of $A B$ has to do two things: meet $A B$ at right angles, and pass through the midpoint of $A B$

Part (a) built $l$ to be perpendicular to $A B$, so the first condition already holds

That leaves the midpoint to check

Find the midpoint of $A B$ from $A ( - 5 , 3 )$ and $B ( 4 , 0 )$

`\left(\frac{-5 + 4}{2}, \frac{3 + 0}{2}\right)`

`\left(-\frac{1}{2}, \frac{3}{2}\right)`

**[B1]**

Part (b) showed that $l$ crosses $A B$ at $D ( - 2 , 2 )$, so compare the two points

`\left(-\frac{1}{2}, \frac{3}{2}\right) \neq (-2, 2)`

**Final answer:** **So **$l$** does not pass through the midpoint of **$A B$**, and is therefore not its perpendicular bisector**

**[B1]**

> **[mark-scheme]**
> **B1**: Either coordinate of the midpoint of $A B$ correct.
> 
> **B1**: Both coordinates correct together with a conclusion.
> 
> The conclusion must be correct but can be very brief, and something as short as "shown" is accepted.
> 
> Comparing lengths instead is equally acceptable, and is marked like this: a correct method for either $A D$ or $B D$ earns the first mark, and correct values for both, with a conclusion, earns the second. Here $A D = \sqrt{10}$ and $B D = \sqrt{40}$, so $D$ is not the midpoint. Decimal values are accepted.

> **[exam-tip]**
> A perpendicular bisector needs both properties, so a question like this is really asking which one fails.
> 
> - The perpendicular property was given to you in part (a)
> - So the midpoint is the only thing that can be wrong, and that is what to test
> 
> You are told to show something is not true, so a comparison on its own is not enough. Write the sentence that draws the conclusion.

### 2((d)) — 4 marks
Parts (a) and (b) have already set this up: $l$ is perpendicular to $A B$ and meets it at $D$

So triangle $B D C$ has a right angle at $D$, and the tangent of the angle at $B$ is just opposite over adjacent

$D$ lies between $A$ and $B$, so the angle $D B C$ is the same angle as $A B C$

Find $B D$ from $B ( 4 , 0 )$ and $D ( - 2 , 2 )$

$B D = \sqrt{(4-(-2))^{2}+(0-2)^{2}}$

$B D = \sqrt{40}$

**[M1]**

Find $C D$ from $C ( - 1 , 5 )$ and $D ( - 2 , 2 )$

$C D = \sqrt{(-1-(-2))^{2}+(5-2)^{2}}$

$C D = \sqrt{10}$

**[M1]**

In triangle $B D C$, $C D$ is opposite the angle at $B$ and $B D$ is adjacent to it

`\text{tan} \angle ABC = \frac{\sqrt{10}}{\sqrt{40}}`

**[M1]**

Simplify, using $\sqrt{40} = 2 \sqrt{10}$

`\text{tan} \angle ABC = \frac{1}{2}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method for $B D$, which may already have been seen in part (c).
> 
> **M1**: Correct method for $C D$.
> 
> **M1**: Correct ratio for `\text{tan} \angle ABC` using your $C D$ and $B D$.
> 
> **A1**: Correct simplified value.
> 
> The third mark depends on both earlier method marks.
> 
> The cosine rule is equally acceptable, and is marked like this: a correct method for one of $A B$, $B C$ and $A C$ earns the first mark and a correct method for all three earns the second. A correct substitution into the cosine rule giving an expression for `\text{cos} \angle ABC` from your lengths earns the third, again dependent on both earlier method marks, and the correct simplified tangent earns the fourth.
> 
> Because the question does not specifically ask for an exact value, accept any value from $0 . 49989$ up to $\frac{1}{2}$. Any other valid method reaching a fully correct exact value earns all four marks.
> 
> A tangent ratio built from the wrong pair of lengths, such as $A B$, $B C$ or $A C$, earns nothing here, because those sides do not enclose a right angle. At least one of $B D$ and $C D$ must appear.

> **[exam-tip]**
> Earlier parts of a question like this are usually there to be used.
> 
> - The right angle at $D$ comes free from part (a), and the coordinates of $D$ come free from part (b)
> - That turns a cosine-rule problem into a single tangent ratio
> 
> The triangle you need is $B D C$, not $A B C$. Using $A B$ or $B C$ in a tangent ratio scores nothing, because the angle between them is not a right angle.
> 
> Leave surds unsimplified until the last line. Here $\frac{\sqrt{10}}{\sqrt{40}}$ collapses neatly to $\frac{1}{2}$, which is much tidier than converting to decimals first.

## Q8 — medium — 9 marks · exam-questions

### 4((a)) — 6 marks
Two pieces of information are given, and each one turns into an equation connecting $p$ and $q$

The factor theorem says that a factor `\left(x - 1\right)` makes `\text{f}\left(1\right)` equal to zero

`\left(1\right)^{3} + p \left(1\right)^{2} + q \left(1\right) + 6 = 0`

**[M1]**

The remainder theorem says that dividing by `\left(x + 1\right)` leaves the value of `\text{f}\left(- 1\right)`, which here is 8

`\left(- 1\right)^{3} + p \left(- 1\right)^{2} + q \left(- 1\right) + 6 = 8`

**[A1]**

Simplify each equation, taking care with the signs in the second one

$p + q = - 7$

$p - q = 3$

**[A1]**

**(i)**

Adding the two equations eliminates $q$ immediately

$2 p = - 4$

**[M1]**

$p = - 2  \text{as required}$

**[A1]**

**(ii)**

Substitute $p = - 2$ back into either equation

$- 2 + q = - 7$

$q = - 5$

**[B1]**

> **[mark-scheme]**
> **M1**: Substitutes either $x = 1$ into `\text{f}\left(x\right) = 0` or $x = - 1$ into `\text{f}\left(x\right) = 8`, fully correctly.
> 
> **A1**: Both substitutions fully correct. The bracketing around $- 1$ must be right, although it can be recovered in later working.
> 
> **A1**: Both equations correct, $p + q = - 7$ and $p - q = 3$, or equivalent unsimplified forms.
> 
> **M1**: Attempts to solve the two equations simultaneously, eliminating one unknown and reaching a value for $p$ or for $q$. Allow one processing error.
> 
> **A1**: $p = - 2$, from working containing no errors.
> 
> **B1**: $q = - 5$. This is an independent accuracy mark, so you can earn it by using the printed value $p = - 2$ even if your own value of $p$ was wrong.
> 
> A correct equation is enough to imply the substitution marks, so the substitution itself does not have to be written out in full.
> 
> Algebraic long division is equally acceptable, and is marked in the same way once the two equations have been reached. It has to be complete and fully correct to produce them, so it is the riskier route here.

> **[exam-tip]**
> A factor and a remainder give the same kind of equation, with a different right-hand side.
> 
> - `\left(x - 1\right)` being a factor means `\text{f}\left(1\right) = 0`
> - A remainder of 8 on dividing by `\left(x + 1\right)` means `\text{f}\left(- 1\right) = 8`
> 
> Brackets matter as soon as you substitute a negative number.
> 
> - `\left(- 1\right)^{3} = - 1` while `\left(- 1\right)^{2} = + 1`, and losing either sign wrecks the second equation
> 
> The value of $q$ carries its own independent mark, so use the printed $p = - 2$ even if your own working has gone astray.
> 
> - One line of substitution is all it takes, and it rescues a mark you would otherwise lose

### 4((b)) — 3 marks
Part (a) gives $p = - 2$ and $q = - 5$, so the cubic is now fully known

`\text{f}\left(x\right) = x^{3} - 2 x^{2} - 5 x + 6`

You already know `\left(x - 1\right)` is a factor, so write the cubic as that factor multiplied by a quadratic

`x^{3} - 2 x^{2} - 5 x + 6 = \left(x - 1\right) \left(x^{2} + B x + C\right)`

Compare the constant terms, which on the right come only from $- 1 \times C$

$- C = 6$

$C = - 6$

Compare the $x^{2}$ terms, which come from $x \times B x$ and from $- 1 \times x^{2}$

$B - 1 = - 2$

$B = - 1$

**[M1]**

Now factorise the quadratic, looking for two numbers that multiply to $- 6$ and add to $- 1$

- Those numbers are $- 3$ and $2$

`x^{2} - x - 6 = \left(x - 3\right) \left(x + 2\right)`

So the equation becomes a product of three linear factors

`\left(x - 1\right) \left(x - 3\right) \left(x + 2\right) = 0`

**[M1]**

Set each factor equal to zero in turn

$x=1,x=3,x=-2$

**[A1]**

> **[mark-scheme]**
> **M1**: Reaches `\left(x - 1\right) \left(x^{2} + A x - 6\right)` with $A$ non-zero, by comparing coefficients or by division. Sight of the quadratic factor on its own is enough.
> 
> **M1**: A valid attempt to solve the quadratic factor, by factorising, completing the square or the quadratic formula, giving two values of $x$ in addition to $x = 1$.
> 
> **A1**: All three values, $x = 1$, $x = 3$ and $x = - 2$.
> 
> Algebraic long division is equally acceptable and earns the first method mark in the same way.
> 
> The second method mark also follows through from an incorrect quadratic, provided a correct method is used on it. It is not necessary to write $= 0$ at the factorised stage.
> 
> The question does not ask you to show your working, so three correct values written down with no working still earn all three marks.

> **[exam-tip]**
> "Hence" means part (a) has already done most of the work.
> 
> - The factor `\left(x - 1\right)` and both constants are handed to you
> - A cubic with a known factor is really a quadratic in disguise
> 
> Do not stop at the factorised form.
> 
> - The command word is solve, so the answer is the three values of $x$, not the three brackets
> 
> Check one root by substituting it back. Putting $x = 3$ into the cubic gives $27 - 18 - 15 + 6$, which is zero.

## Q9 — medium — 9 marks · exam-questions

### 10((a)) — 4 marks
The curves meet where both equations hold at once, so solve them simultaneously

The parabola gives $x^{2}$ on its own, so rearrange it and substitute into the circle

$x^{2} = y - 1$

`\left(y - 1\right) + y^{2} = 11`

**[M1]**

Rearrange into a quadratic in $y$

$y^{2} + y - 12 = 0$

Factorise, looking for two numbers that multiply to $- 12$ and add to 1

- Those numbers are 4 and $- 3$

`\left(y + 4\right) \left(y - 3\right) = 0`

**[M1]**

So there are two possible values of $y$

$y = - 4$

$y = 3$

Convert each one back into $x$ using $x^{2} = y - 1$

$x^{2} = - 5$

$x^{2} = 2$

**[M1]**

A square can never be negative, so $y = - 4$ gives no points and is rejected

- Figure 2 agrees, since both intersections are drawn above the $x$-axis

Take the square root of the other value, keeping both signs

$x = \pm \sqrt{2}$

In Figure 2, $A$ is the left-hand intersection and $B$ is the right-hand one

$x_{A}=-\sqrt{2},x_{B}=\sqrt{2}$

**[A1]**

> **[mark-scheme]**
> **M1**: Rearranges to $x^{2} = y - 1$ and substitutes into the circle to reach a quadratic in $y$, or substitutes $y = x^{2} + 1$ into the circle, expands the square and reaches a quartic in $x$.
> 
> **M1**: A complete attempt to solve that quadratic or quartic by any valid method.
> 
> **A1**: Solves correctly and obtains a value or values for $x^{2}$ or for $x$. This mark is still awarded if you do not state or dismiss the negative value of $x^{2}$.
> 
> **A1**: The $x$ coordinate of $A$ is $- \sqrt{2}$ and the $x$ coordinate of $B$ is $\sqrt{2}$. Decimal equivalents are accepted.
> 
> Both routes are marked identically. The quartic route gives $x^{4} + 3 x^{2} - 10 = 0$, which factorises as `\left(x^{2} + 5\right) \left(x^{2} - 2\right) = 0`.
> 
> Both coordinates are needed for the final mark, and they must be assigned to the correct points.

> **[exam-tip]**
> Substituting to remove $x^{2}$ rather than $y$ turns this into an easy quadratic.
> 
> - $x^{2} = y - 1$ drops straight into the circle equation
> - Substituting $y = x^{2} + 1$ instead also works, but leaves you with a quartic
> 
> Always test both solutions against the picture.
> 
> - $y = - 4$ would need $x^{2} = - 5$, which is impossible
> - Keep both signs of the square root, since the two intersections are $x = - \sqrt{2}$ and $x = \sqrt{2}$
> 
> The labelling matters, and it is only in the figure.
> 
> - $A$ is drawn on the left, so it takes the negative value

### 10((b)) — 5 marks
The region is rotated about the $x$-axis, so use the volume of revolution formula

$R$ lies between two curves, so subtract the inner volume from the outer one

- The circle is the outer boundary and the parabola the inner boundary
- The limits are the $x$ coordinates of $A$ and $B$ from part (a)

`V = \pi \int_{- \sqrt{2}}^{\sqrt{2}} \left[\left(11 - x^{2}\right) - \left(x^{2} + 1\right)^{2}\right] \text{d} x`

**[M1]**

The circle gives $y^{2}$ ready made, since rearranging $x^{2} + y^{2} = 11$ gives $y^{2} = 11 - x^{2}$

Expand the square and collect the terms

`\left(x^{2} + 1\right)^{2} = x^{4} + 2 x^{2} + 1`

`V = \pi \int_{- \sqrt{2}}^{\sqrt{2}} \left(- x^{4} - 3 x^{2} + 10\right) \text{d} x`

**[A1]**

Integrate term by term

`V = \pi \left[- \frac{x^{5}}{5} - x^{3} + 10 x\right]_{- \sqrt{2}}^{\sqrt{2}}`

**[M1]**

Substitute the upper limit, using `\left(\sqrt{2}\right)^{5} = 4 \sqrt{2}` and `\left(\sqrt{2}\right)^{3} = 2 \sqrt{2}`

$- \frac{4\sqrt{2}}{5} - 2 \sqrt{2} + 10 \sqrt{2} = \frac{36\sqrt{2}}{5}$

Substitute the lower limit, where every term is an odd power and so changes sign

$\frac{4\sqrt{2}}{5} + 2 \sqrt{2} - 10 \sqrt{2} = - \frac{36\sqrt{2}}{5}$

**[M1]**

Subtract the lower value from the upper value

`V = \pi \left(\frac{36 \sqrt{2}}{5} + \frac{36 \sqrt{2}}{5}\right)`

$V = \frac{72\sqrt{2}π}{5}$

Evaluate this and round to 2 decimal places

`V equals 63.98 space open parentheses 2 space straight d. straight p. close parentheses`

**[A1]**

> **[mark-scheme]**
> **M1**: Sets up `\pi \int \left[\left(11 - x^{2}\right) - \left(x^{2} + 1\right)^{2}\right] \text{d} x`, or the same difference written the other way round, using your limits from part (a).
> 
> **A1**: Expands and simplifies the integrand to $- x^{4} - 3 x^{2} + 10$. The limits follow through from part (a), but the integrand itself must be correct.
> 
> **M1**: Integrates your expression correctly, with at least three terms and a term in $x^{4}$ or $y^{4}$ present. Neither $π$ nor the limits need appear for this mark.
> 
> **M1**: Substitutes both limits correctly into your integrated expression, each one used correctly at least once. Brackets must be right, although they can be recovered later.
> 
> **A1**: Answers which round to $63 . 98$, the unrounded value being $63 . 9775$. A negative value that is simply turned positive at the end does not earn this mark.
> 
> Integrating the two volumes separately and subtracting at the end is equally acceptable, and is marked in exactly the same way.
> 
> Using symmetry is also accepted, since $R$ is symmetrical about the $y$-axis. Integrating from 0 to $\sqrt{2}$ and doubling, or from $- \sqrt{2}$ to 0 and doubling, earns all five marks provided the factor of 2 is present or clearly implied by the final answer. Without it, the first two marks are lost.

> **[exam-tip]**
> For a region between two curves the formula subtracts the squares, not the curves themselves.
> 
> - `V = \pi \int \left(y_{2}^{2} - y_{1}^{2}\right) \text{d} x`, so square each boundary before subtracting
> - Squaring after subtracting is a common error and loses almost every mark
> 
> The circle gives you $y^{2}$ without any work.
> 
> - Rearranging $x^{2} + y^{2} = 11$ gives $y^{2} = 11 - x^{2}$, so only the parabola needs squaring
> 
> Stay in surds until the very last line.
> 
> - `\left(\sqrt{2}\right)^{5} = 4 \sqrt{2}` and `\left(\sqrt{2}\right)^{3} = 2 \sqrt{2}`, which keeps the arithmetic exact
> - The exact volume is $\frac{72\sqrt{2}π}{5}$, so round only once, right at the end
> 
> A negative answer means the two squares went the wrong way round.
> 
> - Swap them and redo the substitution rather than just dropping the minus sign, because changing the sign at the end scores nothing
