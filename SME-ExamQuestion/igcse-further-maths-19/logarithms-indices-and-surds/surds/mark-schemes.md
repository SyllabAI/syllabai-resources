# Mark Schemes — Surds
**Logarithms, Indices & Surds** · Edexcel IGCSE Further Pure Maths (4PM1)


## Q1 — medium — 11 marks · exam-questions

### 8((a)) — 4 marks
Write the expression using index notation, so that the binomial series formula can be applied

`\frac{3}{\sqrt{1 - 2x}} = 3\left(1 - 2x\right)^{-\frac{1}{2}}`

**[B1]**

The constant term inside the bracket is already 1, so the formula can be applied directly

- Keep the factor of 3 outside the bracket until the last step

Use the binomial series formula from the formula sheet with $n = - \frac{1}{2}$, substituting $- 2 x$ everywhere that $x$ appears

`3\left(1 - 2x\right)^{-\frac{1}{2}} = 3\left[1 + \left(-\frac{1}{2}\right)\left(-2x\right) + \frac{\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)}{2!}\left(-2x\right)^{2} + \frac{\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)\left(-\frac{5}{2}\right)}{3!}\left(-2x\right)^{3} + \ldots\right]`

**[M1 A1]**

Now simplify each term in turn

- Take care with the signs, and remember that the power applies to the whole of $- 2 x$

`\left(-\frac{1}{2}\right)\left(-2x\right) = x`

`\frac{\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)}{2!}\left(-2x\right)^{2} = \frac{3}{2}x^{2}`

`\frac{\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)\left(-\frac{5}{2}\right)}{3!}\left(-2x\right)^{3} = \frac{5}{2}x^{3}`

This gives the expansion inside the bracket

`3\left(1 - 2x\right)^{-\frac{1}{2}} = 3\left[1 + x + \frac{3}{2}x^{2} + \frac{5}{2}x^{3} + \ldots\right]`

Finally multiply every term inside the bracket by 3

$\frac{3}{\sqrt{1-2x}} = 3 + 3 x + \frac{9}{2} x^{2} + \frac{15}{2} x^{3}$

**[A1]**

> **[mark-scheme]**
> **B1**: Writes the expression in index form as `3\left(1 - 2x\right)^{-\frac{1}{2}}`.
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
> Raise the whole bracket to the power each time, so `\left(-2x\right)^{2} = 4x^{2}` and `\left(-2x\right)^{3} = -8x^{3}`.
> 
> - Two negatives multiply to give a positive, so check the sign of every coefficient as you go

### 8((b)) — 1 marks
The binomial series formula is valid only when the quantity substituted in place of $x$ has modulus less than 1

Here that quantity is $- 2 x$, not $x$ itself

`\left|-2x\right| < 1`

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
> - So start from `\left|-2x\right| < 1` and solve it, rather than writing down `\left|x\right| < 1`
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

`\left(\sqrt{10} - 3\right)\left(\sqrt{10} + 3\right) = 10 - 9`

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
> - The surd terms then cancel, because `\left(\sqrt{n} - k\right)\left(\sqrt{n} + k\right) = n - k^{2}`
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

`\sqrt{10} \approx 3 + 3\left(0.05\right) + \frac{9}{2}\left(0.05\right)^{2} + \frac{15}{2}\left(0.05\right)^{3}`

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

## Q2 — medium — 5 marks · exam-questions

### 1() — 5 marks
Rationalise the denominator on the left-hand side by multiplying the numerator and the denominator by $3 + \sqrt{5}$

- This is the denominator with the sign of the surd term reversed

$\frac{a+2\sqrt{5}}{3-\sqrt{5}} = \frac{a+2\sqrt{5}}{3-\sqrt{5}} \times \frac{3+\sqrt{5}}{3+\sqrt{5}}$

Expand the numerator, and use the difference of two squares on the denominator

$\frac{a+2\sqrt{5}}{3-\sqrt{5}} = \frac{3a+a\sqrt{5}+6\sqrt{5}+10}{9-5}$

**[M1]**

Collect the rational terms and the surd terms separately in the numerator

`\frac{a + 2 \sqrt{5}}{3 - \sqrt{5}} = \frac{\left(3 a + 10\right) + \left(a + 6\right) \sqrt{5}}{4}`

Both sides are now a rational part plus a multiple of $\sqrt{5}$, so the two sides can be compared

- Since $a$ and $b$ are whole numbers, the rational parts must match each other and the multiples of $\sqrt{5}$ must match each other

$\frac{3a+10}{4} = \frac{11}{2}$

$\frac{a+6}{4} = \frac{b}{2}$

**[M1]**

Solve the first equation to find $a$

$3 a + 10 = 22$

$a = 4$

**[M1 A1]**

Substitute this value into the second equation to find $b$

$\frac{4+6}{4} = \frac{b}{2}$

$b = 5$

Check this against the condition given in the question

- 5 is a prime number, as required

$a = 4 , b = 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Multiplies the numerator and the denominator of the left-hand side by $3 + \sqrt{5}$, reaching $\frac{3a+a\sqrt{5}+6\sqrt{5}+10}{9-5}$. Allow one error in the numerator, but the denominator must be correct.
> 
> **M1**: Correctly equates their rational parts, and their multiples of $\sqrt{5}$, with those of $\frac{11+b\sqrt{5}}{2}$. There must be at least one equation in $a$ and $b$, although this mark does not depend on the first method mark being earned.
> 
> **M1**: A complete and correct attempt to solve one of their equations, to find a value for $a$ or a value for $b$. Again there must be at least one equation in $a$ and $b$, although this mark does not depend on the earlier method marks.
> 
> **A1**: Either $a = 4$ or $b = 5$.
> 
> **A1**: Both $a = 4$ and $b = 5$.
> 
> Multiplying instead by $- 3 - \sqrt{5}$ makes every term negative but is otherwise identical, and is marked to exactly the same principles.
> 
> Both approved methods earn full marks. If instead you clear the denominators first, the last four marks above are unchanged and the first method mark is awarded as follows.
> 
> **M1**: Correctly removes the denominators from the given equation and multiplies out, reaching $2 a + 4 \sqrt{5} = 33 + 3 b \sqrt{5} - 11 \sqrt{5} - 5 b$. Allow one error.

> **[exam-tip]**
> There is a quicker alternative that earns exactly the same marks, so use whichever you find safer.
> 
> - Cross-multiply first to get `2 \left(a + 2 \sqrt{5}\right) = \left(3 - \sqrt{5}\right) \left(11 + b \sqrt{5}\right)`, expand both sides, then compare parts as before
> 
> Comparing parts works because $\sqrt{5}$ is irrational, so a rational number can never equal a multiple of $\sqrt{5}$ unless both are zero.
> 
> - That is what lets you split a single equation into two separate ones
> 
> The fact that $b$ is prime is a check on your answer rather than something you need in order to find it.

## Q3 — medium — 4 marks · exam-questions

### 1() — 4 marks
The right angle is at $B$, so $A B$ and $B C$ are the base and the height of the triangle

Write down the area using half the base times the height

`34 + 11 \sqrt{5} = \frac{1}{2} \left(2 + 4 \sqrt{5}\right) \left(a + b \sqrt{5}\right)`

**[M1]**

Multiply both sides by 2 to clear the fraction

`68 + 22 \sqrt{5} = \left(2 + 4 \sqrt{5}\right) \left(a + b \sqrt{5}\right)`

Expand the brackets on the right-hand side

- Use `\left(\sqrt{5}\right)^{2} = 5` to simplify the last term

$68 + 22 \sqrt{5} = 2 a + 2 b \sqrt{5} + 4 a \sqrt{5} + 20 b$

**[M1]**

Collect the rational terms and the surd terms separately

`68 + 22 \sqrt{5} = \left(2 a + 20 b\right) + \left(4 a + 2 b\right) \sqrt{5}`

Since $a$ and $b$ are integers, the rational parts must match each other and the multiples of $\sqrt{5}$ must match each other

$2 a + 20 b = 68$

$4 a + 2 b = 22$

Divide each equation by 2 to make the numbers easier to work with

$a + 10 b = 34$

$2 a + b = 11$

Solve the pair of simultaneous equations, here by making $b$ the subject of the second equation

$b = 11 - 2 a$

Substitute that into the first equation

`a + 10 \left(11 - 2 a\right) = 34`

$a + 110 - 20 a = 34$

$- 19 a = - 76$

$a = 4$

**[M1]**

Substitute this value back to find $b$

$b = 11 - 2 \times 4$

The two values can now be stated together

$a=4,b=3$

**[A1]**

> **[mark-scheme]**
> **M1**: A fully correct statement for the area of the triangle. This may be written explicitly or implied by later working. Allow $a + b \sqrt{5}$ to be written as $B C$, or denoted by another letter.
> 
> **M1**: Multiplies out the brackets correctly. If the factor of $\frac{1}{2}$ is missing from the area statement, this mark may still be awarded for $34 + 11 \sqrt{5} = 2 a + 2 b \sqrt{5} + 4 a \sqrt{5} + 20 b$.
> 
> **M1**: Correctly equates the rational parts, and the multiples of $\sqrt{5}$, and then uses any valid complete method to solve the resulting pair of simultaneous equations. Allow one error. A missing $\frac{1}{2}$ does not count as that one error.
> 
> **A1**: $a = 4$ and $b = 3$. Accept the answer written as $4 + 3 \sqrt{5}$.
> 
> Both approved methods earn full marks. If instead you rearrange first and then rationalise, the first method mark and the accuracy mark above are unchanged, and the two middle method marks are awarded as follows.
> 
> **M1**: Correctly rearranges to make $a + b \sqrt{5}$ the subject, reaching `a + b \sqrt{5} = \frac{2 \left(34 + 11 \sqrt{5}\right)}{2 + 4 \sqrt{5}}` or the equivalent form $a + b \sqrt{5} = \frac{34+11\sqrt{5}}{1+2\sqrt{5}}$. This mark is also available if the $\frac{1}{2}$ was missing from the area statement.
> 
> **M1**: Multiplies the numerator and the denominator by that denominator with the sign of its surd term reversed, for example $\frac{34+11\sqrt{5}}{1+2\sqrt{5}} \times \frac{1-2\sqrt{5}}{1-2\sqrt{5}}$. Allow one error in multiplying out, and allow the 2 to remain factorised.
> 
> The question tells you not to use a calculator, so the method must be shown for any of these marks.

> **[exam-tip]**
> Comparing parts works because $\sqrt{5}$ is irrational, so a rational number can never equal a multiple of $\sqrt{5}$ unless both are zero.
> 
> - That is what lets you split one equation into two, which is the key step in the whole question
> 
> There is an alternative route: rearrange first to make $a + b \sqrt{5}$ the subject, then rationalise the denominator.
> 
> - It earns exactly the same marks, but the numbers become much larger, so expanding and comparing parts is usually the safer choice here
> 
> Check your answer at the end by multiplying `\left(2 + 4 \sqrt{5}\right)` and `\left(4 + 3 \sqrt{5}\right)` and halving.
