# Mark Schemes — Differentiation
**Calculus** · Edexcel IGCSE Further Pure Maths (4PM1)


## Q1 — medium — 8 marks · exam-questions

### 6() — 8 marks
$y$ is a product of two functions of $x$, so differentiate it with the product rule

Take $u = \text{e}^{x}$ and $v = x^{2} - 3 x$, so $\frac{\text{d}u}{\text{d}x} = \text{e}^{x}$ and $\frac{\text{d}v}{\text{d}x} = 2 x - 3$

- The derivative of $\text{e}^{x}$ is $\text{e}^{x}$, which is what makes every line here keep its exponential factor

`\frac{\text{d} y}{\text{d} x} = \text{e}^{x} \left(x^{2} - 3 x\right) + \text{e}^{x} \left(2 x - 3\right)`

**[M1] [M1]**

Both terms share a factor of $\text{e}^{x}$, so take it outside a single bracket and collect the terms inside

`\frac{\text{d} y}{\text{d} x} = \text{e}^{x} \left(x^{2} - x - 3\right)`

**[A1]**

Now differentiate again, using the product rule on this new product

Take $u = \text{e}^{x}$ and $v = x^{2} - x - 3$, so $\frac{\text{d}v}{\text{d}x} = 2 x - 1$

`\frac{\text{d}^{2} y}{\text{d} x^{2}} = \text{e}^{x} \left(x^{2} - x - 3\right) + \text{e}^{x} \left(2 x - 1\right)`

**[M1]**

Collect inside the bracket again

`\frac{\text{d}^{2} y}{\text{d} x^{2}} = \text{e}^{x} \left(x^{2} + x - 4\right)`

**[A1]**

Now build the left-hand side of the printed result from the three expressions

Every one of them has a factor of $\text{e}^{x}$, so take that outside one bracket

`y - 2 \frac{\text{d} y}{\text{d} x} + \frac{\text{d}^{2} y}{\text{d} x^{2}} = \text{e}^{x} \left[\left(x^{2} - 3 x\right) - 2 \left(x^{2} - x - 3\right) + \left(x^{2} + x - 4\right)\right]`

**[M1]**

Expand the middle bracket carefully, since the $- 2$ changes both signs inside it

`y - 2 \frac{\text{d} y}{\text{d} x} + \frac{\text{d}^{2} y}{\text{d} x^{2}} = \text{e}^{x} \left[x^{2} - 3 x - 2 x^{2} + 2 x + 6 + x^{2} + x - 4\right]`

**[M1]**

Collect the three groups of terms inside the bracket

- The terms in $x^{2}$ give $1 - 2 + 1$, which is 0
- The terms in $x$ give $- 3 + 2 + 1$, which is 0
- The numbers give $6 - 4$, which is 2

$y - 2 \frac{\text{d}y}{\text{d}x} + \frac{\text{d}^{2}y}{\text{d}x^{2}} = 2 \text{e}^{x}  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Applies the product rule to $y$, using the correct formula and differentiating both factors acceptably.
> 
> **M1**: Both differentiated factors correct, so that the two terms are `\text{e}^{x} \left(x^{2} - 3 x\right)` and `\text{e}^{x} \left(2 x - 3\right)`, added rather than subtracted.
> 
> **A1**: A correct first derivative, in any form. It need not be collected into a single bracket.
> 
> **M1**: Applies the product rule a second time to your first derivative.
> 
> **A1**: A correct second derivative, in any form.
> 
> **M1**: Forms $y - 2 \frac{\text{d}y}{\text{d}x} + \frac{\text{d}^{2}y}{\text{d}x^{2}}$ from your three expressions.
> 
> **M1**: Expands the brackets, with the $- 2$ applied to every term of the first derivative.
> 
> **A1**: Reaches $2 \text{e}^{x}$ with no errors anywhere in the working, and states that this is the required result.
> 
> The board's own route is different and earns the same eight marks in the same order. Instead of expanding, it reads `\text{e}^{x} \left(2 x - 3\right)` as $\frac{\text{d}y}{\text{d}x} - y$ from the first line, substitutes that into the second derivative, and rearranges to the printed form. Where that route is used, the sixth and seventh marks are for the substitution and the rearrangement.
> 
> This is a "show that", so the printed result cannot be assumed. The working has to arrive at it.

> **[exam-tip]**
> Take the exponential outside a bracket as soon as each derivative is formed.
> 
> - `\text{e}^{x} \left(x^{2} - 3 x\right) + \text{e}^{x} \left(2 x - 3\right)` becomes `\text{e}^{x} \left(x^{2} - x - 3\right)`, and every later line then has only one bracket to manage
> - Leaving the terms separate doubles the algebra at the last step
> 
> The derivative of $\text{e}^{x}$ is $\text{e}^{x}$, which is why the pattern repeats.
> 
> - Each differentiation keeps the same exponential factor and only changes the polynomial in the bracket
> - So the second derivative is found by the same rule applied to the same shape
> 
> Every term in $x$ has to vanish, and that is your check.
> 
> - The right-hand side is a number times $\text{e}^{x}$, so the $x^{2}$ terms and the $x$ terms must both cancel
> - If either is left over, the slip is almost always the $- 2$ not being applied to all three terms of the first derivative
> 
> Write the conclusion out.
> 
> - The final mark is for reaching the printed result with no errors, so finish with the statement rather than stopping at the bracket

## Q2 — medium — 7 marks · exam-questions

### 5() — 7 marks
$y$ is a product of two functions of $x$, so differentiate it with the product rule

Take $u = \text{e}^{2x}$ and $v = x^{2} - 5 x$, so $\frac{\text{d}u}{\text{d}x} = 2 \text{e}^{2x}$ and $\frac{\text{d}v}{\text{d}x} = 2 x - 5$

- Differentiating $\text{e}^{2x}$ brings down a factor of 2, because of the $2 x$ in the power

`\frac{\text{d} y}{\text{d} x} = 2 \text{e}^{2 x} \left(x^{2} - 5 x\right) + \text{e}^{2 x} \left(2 x - 5\right)`

**[M1] [A1]**

Take the common factor of $\text{e}^{2x}$ outside a single bracket and collect the terms inside

`\frac{\text{d} y}{\text{d} x} = \text{e}^{2 x} \left(2 x^{2} - 8 x - 5\right)`

**[A1]**

Now differentiate again, applying the product rule to this new product

Take $u = \text{e}^{2x}$ and $v = 2 x^{2} - 8 x - 5$, so $\frac{\text{d}v}{\text{d}x} = 4 x - 8$

`\frac{\text{d}^{2} y}{\text{d} x^{2}} = 2 \text{e}^{2 x} \left(2 x^{2} - 8 x - 5\right) + \text{e}^{2 x} \left(4 x - 8\right)`

**[M1]**

Collect inside the bracket again

`\frac{\text{d}^{2} y}{\text{d} x^{2}} = \text{e}^{2 x} \left(4 x^{2} - 12 x - 18\right)`

**[A1]**

Now build the right-hand side of the printed result from the three expressions

Every one of them has a factor of $\text{e}^{2x}$, so take that outside one bracket

`\frac{\text{d}^{2} y}{\text{d} x^{2}} - 4 \frac{\text{d} y}{\text{d} x} + 4 y = \text{e}^{2 x} \left[\left(4 x^{2} - 12 x - 18\right) - 4 \left(2 x^{2} - 8 x - 5\right) + 4 \left(x^{2} - 5 x\right)\right]`

**[M1]**

Expand the two brackets that are being multiplied, watching the signs in the middle one

- `- 4 \left(2 x^{2} - 8 x - 5\right)` is $- 8 x^{2} + 32 x + 20$
- `4 \left(x^{2} - 5 x\right)` is $4 x^{2} - 20 x$

Collect the three groups of terms inside the bracket

- The terms in $x^{2}$ give $4 - 8 + 4$, which is 0
- The terms in $x$ give $- 12 + 32 - 20$, which is 0
- The numbers give $- 18 + 20$, which is 2

$\frac{\text{d}^{2}y}{\text{d}x^{2}} - 4 \frac{\text{d}y}{\text{d}x} + 4 y = 2 \text{e}^{2x}  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Applies the product rule to $y$, differentiating both factors acceptably and adding the two terms.
> 
> **A1**: One term of the product rule correct.
> 
> **A1**: A fully correct first derivative, in any form. It need not be collected into a single bracket.
> 
> **M1**: Differentiates your first derivative a second time. Where the result is left as four separate terms, at least two of them must be correct.
> 
> **A1**: A fully correct second derivative, in any form.
> 
> **M1**: Forms $\frac{\text{d}^{2}y}{\text{d}x^{2}} - 4 \frac{\text{d}y}{\text{d}x} + 4 y$ from your three expressions and rearranges it towards the printed form.
> 
> **A1**: Reaches $2 \text{e}^{2x}$ with no errors anywhere in the working.
> 
> The board's main route substitutes rather than expands: it reads `\text{e}^{2 x} \left(2 x - 5\right)` as $\frac{\text{d}y}{\text{d}x} - 2 y$ from the first line and puts that into the second derivative. It earns the same seven marks in the same order, with the sixth mark for the substitution.
> 
> Implicit differentiation is also completely acceptable and is marked in the same way.
> 
> This is a "show that", so the final mark needs everything correct.

> **[exam-tip]**
> Differentiating $\text{e}^{2x}$ brings a 2 down each time.
> 
> - $\text{e}^{2x}$ differentiates to $2 \text{e}^{2x}$, not to $\text{e}^{2x}$
> - Missing that factor is the single commonest way to lose the first three marks here
> 
> Collect into one bracket before differentiating again.
> 
> - `\text{e}^{2 x} \left(2 x^{2} - 8 x - 5\right)` is far easier to differentiate than the two separate terms it came from
> 
> Every term in $x$ has to disappear, which gives you a free check.
> 
> - The printed answer is a number times $\text{e}^{2x}$, so the $x^{2}$ and $x$ terms must both cancel
> - If they do not, check the signs when the $- 4$ was multiplied through
> 
> There is a quicker route if you spot it.
> 
> - The first line contains `\text{e}^{2 x} \left(2 x - 5\right)`, which is exactly $\frac{\text{d}y}{\text{d}x} - 2 y$, so it can be substituted straight into the second derivative
> - It earns the same marks, so use whichever you see first

## Q3 — medium — 5 marks · exam-questions

### 3() — 5 marks
$y$ is a product of two functions of $x$, so differentiate it with the product rule

Take $u = \text{e}^{3x}$ and `v = \left(2 x - 1\right)^{4}`

- $\frac{\text{d}u}{\text{d}x} = 3 \text{e}^{3x}$, bringing down the 3 from the power
- `\frac{\text{d} v}{\text{d} x} = 4 \left(2 x - 1\right)^{3} \times 2`, by the chain rule, so it is `8 \left(2 x - 1\right)^{3}`

`\frac{\text{d} y}{\text{d} x} = 8 \left(2 x - 1\right)^{3} \text{e}^{3 x} + 3 \text{e}^{3 x} \left(2 x - 1\right)^{4}`

**[M1] [A1] [A1]**

The gradient of the tangent at a point is the value of the derivative there, so substitute $x = 1$

- `2 \left(1\right) - 1 = 1`, and every power of 1 is 1, so both brackets are simply 1

`\frac{\text{d} y}{\text{d} x} = 8 \left(2 \left(1\right) - 1\right)^{3} \text{e}^{3} + 3 \text{e}^{3} \left(2 \left(1\right) - 1\right)^{4}`

**[M1]**

Both terms now carry the same factor of $\text{e}^{3}$, so add them

$\frac{\text{d}y}{\text{d}x} = 11 \text{e}^{3}$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the product rule to give an expression of the form `p \text{e}^{3 x} \left(2 x - 1\right)^{3} + q \text{e}^{3 x} \left(2 x - 1\right)^{4}`, with $p$ and $q$ both positive and a plus sign between the terms.
> 
> **A1**: Either term correct.
> 
> **A1**: Both terms correct.
> 
> **M1**: Substitutes $x = 1$ into your derivative. This mark depends on the previous method mark. Where no substitution is written down, it is still earned if your derivative is correct and an answer which rounds to 221 is seen.
> 
> **A1**: The correct exact value $11 \text{e}^{3}$.
> 
> Expanding `\left(2 x - 1\right)^{4}` first is equally acceptable and is marked in the same way. That route gives $16 x^{4} - 32 x^{3} + 24 x^{2} - 8 x + 1$, whose derivative is $64 x^{3} - 96 x^{2} + 48 x - 8$, so the first two marks look for `\frac{\text{d} y}{\text{d} x} = \text{e}^{3 x} \left(64 x^{3} - 96 x^{2} + 48 x - 8\right) + 3 \text{e}^{3 x} \left(2 x - 1\right)^{4}`.
> 
> The question says "exact", so a decimal such as $220 . 9$ does not earn the final mark.

> **[exam-tip]**
> Two rules are needed here, one inside the other.
> 
> - The product rule handles $\text{e}^{3x}$ times the bracket
> - The chain rule handles the bracket itself, giving `4 \left(2 x - 1\right)^{3} \times 2`, and forgetting that inner 2 is the usual slip
> 
> Substitute before you simplify.
> 
> - At $x = 1$ the bracket $2 x - 1$ is just 1, so both powers of it disappear and the arithmetic is $8 + 3$
> - Expanding or factorising first works, but it is far more writing for the same five marks
> 
> "Exact" rules out the calculator value.
> 
> - $11 \text{e}^{3}$ is the answer; $220 . 9$ is not, even though it is what your calculator shows
> - Use the decimal only as a check that you have not slipped
> 
> Factorising is a neat middle step if you want one.
> 
> - The derivative is `\text{e}^{3 x} \left(2 x - 1\right)^{3} \left(6 x + 5\right)`, which at $x = 1$ gives $\text{e}^{3} \times 1 \times 11$ directly
> - It is not required, and the accuracy marks are for the two separate terms

## Q4 — medium — 5 marks · exam-questions

### 2() — 5 marks
$y$ is a product of two functions of $x$, so differentiate it with the product rule

Write the square root as a power first, so the chain rule can be applied to it

- $\sqrt{3+2x}$ is `\left(3 + 2 x\right)^{\frac{1}{2}}`

Take $u = \text{sin} 2 x$ and `v = \left(3 + 2 x\right)^{\frac{1}{2}}`

- $\frac{\text{d}u}{\text{d}x} = 2 \text{cos} 2 x$
- `\frac{\text{d} v}{\text{d} x} = \frac{1}{2} \times 2 \times \left(3 + 2 x\right)^{- \frac{1}{2}}`, by the chain rule

`\frac{\text{d} y}{\text{d} x} = \text{sin} 2 x \times \frac{1}{2} \times 2 \times \left(3 + 2 x\right)^{- \frac{1}{2}} + \left(3 + 2 x\right)^{\frac{1}{2}} \times 2 \times \text{cos} 2 x`

**[M1] [A1] [A1]**

The printed form is a single fraction over $\sqrt{3+2x}$, so write both terms over that denominator

- A negative index means a reciprocal, so `\left(3 + 2 x\right)^{- \frac{1}{2}}` is $\frac{1}{\sqrt{3+2x}}$ and the first term is already over it
- The second term is multiplied above and below by $\sqrt{3+2x}$, and $\sqrt{3+2x} \times \sqrt{3+2x}$ is $3 + 2 x$

`\frac{\text{d} y}{\text{d} x} = \frac{\text{sin} 2 x + 2 \left(3 + 2 x\right) \text{cos} 2 x}{\sqrt{3 + 2 x}}`

**[M1]**

Expand the bracket multiplying $\text{cos} 2 x$, which puts it in the printed form

`\frac{\text{d} y}{\text{d} x} = \frac{\text{sin} 2 x + \left(6 + 4 x\right) \text{cos} 2 x}{\sqrt{3 + 2 x}}`

**[A1]**

Comparing this with the printed form gives the two integers, $A = 6$ and $B = 4$

> **[mark-scheme]**
> **M1**: Applies the product rule with the correct formula, differentiating $\text{sin} 2 x$ to $k \text{cos} 2 x$ and $\sqrt{3+2x}$ to `l \left(3 + 2 x\right)^{- \frac{1}{2}}` for some positive $k$ and $l$.
> 
> **A1**: One term correct, with the other minimally acceptable. Simplification is not required.
> 
> **A1**: A fully correct derivative. Simplification is not required.
> 
> **M1**: Correct use of $\sqrt{3+2x}$, or of `\left(3 + 2 x\right)^{\frac{1}{2}}`, as a common denominator. This mark depends on the first method mark.
> 
> **A1**: The printed form reached with no erroneous or missing working.
> 
> The values $A = 6$ and $B = 4$ carry no separate mark. The final accuracy mark is for reaching the printed expression, and the two integers may be read from it or given embedded in it.
> 
> Rewriting the root as a power before differentiating is expected, but any correct equivalent derivative is accepted.

> **[exam-tip]**
> Turn the root into a power before you differentiate it.
> 
> - $\sqrt{3+2x}$ is `\left(3 + 2 x\right)^{\frac{1}{2}}`, which the chain rule handles in one step
> - The inner derivative is 2, and leaving it out is the commonest error here
> 
> The negative index is what puts the first term over the root.
> 
> - `\left(3 + 2 x\right)^{- \frac{1}{2}}` is $\frac{1}{\sqrt{3+2x}}$, so that term needs no adjusting at all
> - Only the second term has to be rewritten over the common denominator
> 
> Let the printed form tell you what to aim for.
> 
> - It is a single fraction over $\sqrt{3+2x}$ with $\text{sin} 2 x$ alone at the front, which is exactly what the two coefficients of $\frac{1}{2} \times 2$ collapse to
> 
> Read $A$ and $B$ off at the end.
> 
> - `2 \left(3 + 2 x\right)` expands to $6 + 4 x$, so $A = 6$ and $B = 4$
> - Both are integers, which is the check the question builds in

## Q5 — medium — 8 marks · exam-questions

### 8((a)) — 5 marks
$y$ is one function of $x$ divided by another, so differentiate it with the quotient rule

Take $u = 2 \text{e}^{3x+1}$ and $v = 5 x^{2}$

- $\frac{\text{d}u}{\text{d}x} = 6 \text{e}^{3x+1}$, since differentiating the power $3 x + 1$ brings down a 3
- $\frac{\text{d}v}{\text{d}x} = 10 x$

The quotient rule is $\frac{\text{d}y}{\text{d}x} = \frac{v\frac{\text{d}u}{\text{d}x}-u\frac{\text{d}v}{\text{d}x}}{v^{2}}$

`\frac{\text{d} y}{\text{d} x} = \frac{5 x^{2} \times 6 \text{e}^{3 x + 1} - 2 \text{e}^{3 x + 1} \times 10 x}{\left(5 x^{2}\right)^{2}}`

**[M1] [A1] [A1]**

The required form has a single bracket on top, so take the common factors out of the numerator

- Both terms contain $\text{e}^{3x+1}$ and both contain $x$, so $10 x \text{e}^{3x+1}$ comes out
- $30 x^{2} \text{e}^{3x+1} - 20 x \text{e}^{3x+1}$ becomes `10 x \text{e}^{3 x + 1} \left(3 x - 2\right)`

`\frac{\text{d} y}{\text{d} x} = \frac{10 x \text{e}^{3 x + 1} \left(3 x - 2\right)}{25 x^{4}}`

**[M1]**

Now cancel, dividing the numbers by 5 and cancelling one power of $x$

`\frac{\text{d} y}{\text{d} x} = \frac{2 \text{e}^{3 x + 1} \left(3 x - 2\right)}{5 x^{3}}`

**[A1]**

Comparing this with the required form gives $A = 2$, $B = 3$ and $C = 5$, which are all prime

> **[mark-scheme]**
> **M1**: Attempts the quotient rule. The denominator must be correct and the two terms in the numerator must be subtracted, either way round.
> 
> **A1**: At least one fully correct term on the numerator, simplified or unsimplified.
> 
> **A1**: A fully correct unsimplified derivative.
> 
> **M1**: Correctly takes out the common factors of $x$ and $\text{e}^{3x+1}$ and attempts to simplify. A numerical factor does not need to be taken out at this point. This mark depends on the first method mark.
> 
> **A1**: The correct derivative in the required form.
> 
> The product rule is equally acceptable and is marked in the same way, writing $y$ as `2 \text{e}^{3 x + 1} \left(5 x^{2}\right)^{- 1}` and reaching `M \text{e}^{3 x + 1} x \left(5 x^{2}\right)^{- 2} + N \text{e}^{3 x + 1} \left(5 x^{2}\right)^{- 1}` with $M$ negative and $N$ positive.
> 
> The values $A = 2$, $B = 3$ and $C = 5$ carry no separate mark. The final accuracy mark is for the derivative in the printed form.

> **[exam-tip]**
> Differentiating $\text{e}^{3x+1}$ brings down a 3, not a $3 x + 1$.
> 
> - Only the coefficient of $x$ in the power comes down, so $2 \text{e}^{3x+1}$ differentiates to $6 \text{e}^{3x+1}$
> - The $+ 1$ in the power never changes anything
> 
> Square the whole denominator, not just the $x$.
> 
> - `\left(5 x^{2}\right)^{2}` is $25 x^{4}$, and writing $5 x^{4}$ instead loses the last two marks
> 
> The printed form tells you to factorise before cancelling.
> 
> - Taking $10 x \text{e}^{3x+1}$ out of the numerator turns it into a single bracket, which is the only way to reach `\frac{A \text{e}^{3 x + 1} \left(B x - A\right)}{C x^{3}}`
> - Notice the same letter $A$ appears twice in that form, which is a check that the number outside and the number in the bracket really do match
> 
> Use "prime" as your final check.
> 
> - $A = 2$, $B = 3$ and $C = 5$ are all prime, so a value such as 10 or 25 left anywhere means the cancelling is not finished

### 8((b)) — 3 marks
A small change in $x$ produces a small change in $y$, and the derivative connects the two

- For a small increase, $δ y \approx \frac{\text{d}y}{\text{d}x} \times δ x$

An increase of 2% means $δ x$ is 2% of $x$

$δ x = 0 . 02 x$

The percentage change in $y$ is $δ y$ as a percentage of $y$, so divide by $y$ and multiply by 100

`\frac{\delta y}{y} \times 100 = \frac{2 \text{e}^{3 x + 1} \left(3 x - 2\right)}{5 x^{3}} \times 0 . 02 x \times \frac{100}{y}`

**[M1]**

Now put in $y = \frac{2\text{e}^{3x+1}}{5x^{2}}$

- Dividing by that fraction is the same as multiplying by $\frac{5x^{2}}{2\text{e}^{3x+1}}$

`\frac{\delta y}{y} \times 100 = \frac{2 \text{e}^{3 x + 1} \left(3 x - 2\right)}{5 x^{3}} \times 0 . 02 x \times 100 \times \frac{5 x^{2}}{2 \text{e}^{3 x + 1}}`

**[M1]**

Everything cancels except the bracket and the numbers

- The exponentials cancel, and $\frac{2}{5} \times \frac{5}{2}$ is 1
- $\frac{x\timesx^{2}}{x^{3}}$ is 1, so no power of $x$ is left outside the bracket
- $0 . 02 \times 100$ is 2

`\frac{\delta y}{y} \times 100 = 2 \left(3 x - 2\right)`

So the percentage change in $y$ is

$6 x - 4$

**[A1]**

This is of the form `\left(P x - Q\right)` with $P = 6$ and $Q = 4$, which are both integers

> **[mark-scheme]**
> **M1**: Any correct statement of the percentage change using your answer to part (a), which must be of the form `\frac{A \text{e}^{3 x + 1} \left(B x - C\right)}{D x^{3}}`. An expression not quite in the form given in part (a) is allowed. This mark may be implied by later correct working.
> 
> **M1**: Substitutes in the expression for $y$ and makes a correct attempt to simplify. This mark depends on the previous one.
> 
> **A1**: The correct expression $6 x - 4$.
> 
> Writing $δ x$ as $0 . 02 x$ is what the 2% means, and either $δ y$ or $\frac{δy}{y} \times 100$ may be formed first.
> 
> Writing 100 as 100% is condoned, provided the multiplication by 100 is genuinely being done.

> **[exam-tip]**
> Percentage change needs three things: the derivative, the step, and a division by $y$.
> 
> - $δ y \approx \frac{\text{d}y}{\text{d}x} \times δ x$ gives the change itself
> - Dividing by $y$ and multiplying by 100 turns it into a percentage, and skipping that division is the commonest error
> 
> Write the 2% as $0 . 02 x$, not as 2.
> 
> - The increase is 2% of $x$, so it depends on $x$
> - Using 2 instead leaves an answer 50 times too big
> 
> Expect everything to cancel.
> 
> - The exponential appears in both the derivative and $y$, so it must disappear, and so must every power of $x$ outside the bracket
> - If an $\text{e}^{3x+1}$ survives, the substitution for $y$ has gone in the wrong way up
> 
> The answer is an estimate, not an exact change.
> 
> - It comes from $δ y \approx \frac{\text{d}y}{\text{d}x} \times δ x$, which treats the curve as straight over the small step
> - That is why the question says "an estimate"

## Q6 — medium — 9 marks · exam-questions

### 7((a)) — 4 marks
$y$ is a product of two functions of $x$, so differentiate it with the product rule

Take $u = \text{e}^{2x}$ and $v = \text{cos} 2 x$

- $\frac{\text{d}u}{\text{d}x} = 2 \text{e}^{2x}$, since the power $2 x$ brings down a 2
- $\frac{\text{d}v}{\text{d}x} = - 2 \text{sin} 2 x$, since differentiating a cosine gives a negative sine

$\frac{\text{d}y}{\text{d}x} = 2 \text{e}^{2x} \text{cos} 2 x - 2 \text{e}^{2x} \text{sin} 2 x$

**[M1] [A1] [A1]**

Now look back at what $y$ is

- $y = \text{e}^{2x} \text{cos} 2 x$, so the first term $2 \text{e}^{2x} \text{cos} 2 x$ is exactly $2 y$

Replacing that first term gives the printed result

$\frac{\text{d}y}{\text{d}x} = 2 y - 2 \text{e}^{2x} \text{sin} 2 x  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Attempts the product rule, using the correct formula and differentiating both factors, with the two terms added.
> 
> **A1**: One term correct.
> 
> **A1**: Both terms correct.
> 
> **A1**: Obtains the given result with no errors seen.
> 
> Minimally acceptable differentiation for the method mark is $\text{cos} 2 x$ going to $\pm 2 \text{sin} 2 x$ and $\text{e}^{2x}$ going to $2 \text{e}^{2x}$.
> 
> Recognising that $\text{e}^{2x} \text{cos} 2 x$ is $y$ is the whole of the last step, so a solution that stops at the two-term derivative does not earn the final mark.

> **[exam-tip]**
> Differentiating a cosine introduces a minus sign.
> 
> - $\text{cos} 2 x$ differentiates to $- 2 \text{sin} 2 x$, so the product rule's plus sign and that minus sign combine into the subtraction you see
> - Losing one of the two is what turns the answer into a sum
> 
> The printed form is telling you to spot $y$ inside your own answer.
> 
> - $2 \text{e}^{2x} \text{cos} 2 x$ is just $2 y$, because $y$ was defined as $\text{e}^{2x} \text{cos} 2 x$
> - Part (b) depends on this, so it is worth writing the substitution out rather than doing it in your head
> 
> Both factors give a 2.
> 
> - $\text{e}^{2x}$ gives a 2 and $\text{cos} 2 x$ gives a 2, so every term in the answer has a coefficient of 2

### 7((b)) — 5 marks
"Hence" means start from the answer to part (a), so differentiate that

- $\frac{\text{d}y}{\text{d}x} = 2 \text{e}^{2x} \text{cos} 2 x - 2 \text{e}^{2x} \text{sin} 2 x$

Apply the product rule to each of the two terms separately

- $2 \text{e}^{2x} \text{cos} 2 x$ differentiates to $4 \text{e}^{2x} \text{cos} 2 x - 4 \text{e}^{2x} \text{sin} 2 x$
- $- 2 \text{e}^{2x} \text{sin} 2 x$ differentiates to $- 4 \text{e}^{2x} \text{sin} 2 x - 4 \text{e}^{2x} \text{cos} 2 x$

$\frac{\text{d}^{2}y}{\text{d}x^{2}} = 4 \text{e}^{2x} \text{cos} 2 x - 4 \text{e}^{2x} \text{sin} 2 x - 4 \text{e}^{2x} \text{sin} 2 x - 4 \text{e}^{2x} \text{cos} 2 x$

**[M1] [A1]**

The two cosine terms cancel and the two sine terms combine

$\frac{\text{d}^{2}y}{\text{d}x^{2}} = - 8 \text{e}^{2x} \text{sin} 2 x$

**[M1]**

Now bring in part (a) to remove the exponential

- Part (a) gives $\frac{\text{d}y}{\text{d}x} = 2 y - 2 \text{e}^{2x} \text{sin} 2 x$, so $2 \text{e}^{2x} \text{sin} 2 x = 2 y - \frac{\text{d}y}{\text{d}x}$
- The second derivative is $- 4$ times that

`\frac{\text{d}^{2} y}{\text{d} x^{2}} = - 4 \left(2 y - \frac{\text{d} y}{\text{d} x}\right)`

**[M1]**

Expand the bracket

$\frac{\text{d}^{2}y}{\text{d}x^{2}} = 4 \frac{\text{d}y}{\text{d}x} - 8 y  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Attempts to differentiate your first derivative to obtain the second derivative, applying the same rules as in part (a).
> 
> **A1**: A correct second derivative, in any form.
> 
> **M1**: Simplifies the second derivative to $- 8 \text{e}^{2x} \text{sin} 2 x$. This mark depends on the first method mark.
> 
> **M1**: Uses part (a) to replace the remaining exponential term by an expression in $y$ and $\frac{\text{d}y}{\text{d}x}$. This mark depends on both previous method marks.
> 
> **A1**: A conclusion. Reaching the printed result and stating that it is shown is sufficient.
> 
> An equally acceptable route differentiates the first derivative in its part (a) form, $2 y - 2 \text{e}^{2x} \text{sin} 2 x$, giving $\frac{\text{d}^{2}y}{\text{d}x^{2}} = 2 \frac{\text{d}y}{\text{d}x} - 4 \text{e}^{2x} \text{sin} 2 x - 4 \text{e}^{2x} \text{cos} 2 x$ and then substituting for both trigonometric terms. It earns the same five marks in the same order.

> **[exam-tip]**
> The cosine terms cancel, which is the point of the whole question.
> 
> - Differentiating the sine term produces a cosine term that exactly kills the one already there
> - If your four terms do not collapse to a single sine term, one of the four signs is wrong
> 
> "Hence" means you must use part (a).
> 
> - Starting again from $y = \text{e}^{2x} \text{cos} 2 x$ reaches the same place, but the last two marks are specifically for using part (a) to remove the exponential
> - Rearranging part (a) into $2 \text{e}^{2x} \text{sin} 2 x = 2 y - \frac{\text{d}y}{\text{d}x}$ is the step that makes it work
> 
> Watch the factor of $- 4$.
> 
> - $- 8 \text{e}^{2x} \text{sin} 2 x$ is $- 4 \times 2 \text{e}^{2x} \text{sin} 2 x$, and it is the $2 \text{e}^{2x} \text{sin} 2 x$ that part (a) gives you
> - Trying to substitute for $8 \text{e}^{2x} \text{sin} 2 x$ directly is where the arithmetic goes wrong
> 
> Say that it is shown.
> 
> - The final mark is for the conclusion, so finish the line rather than leaving the bracket unexpanded

## Q7 — medium — 14 marks · exam-questions

### 11((a)) — 3 marks
**(i)**

The curve crosses the $y$-axis at $A$, and every point on the $y$-axis has $x = 0$

Substitute $x = 0$ into the equation of $C$, remembering that $\text{e}^{0} = 1$

$y = 4 - \text{e}^{0}$

$y = 3$

**[B1]**

**(ii)**

The curve crosses the $x$-axis at $B$, and every point on the $x$-axis has $y = 0$

$0 = 4 - \text{e}^{2x}$

$\text{e}^{2x} = 4$

To bring the power down, take natural logarithms of both sides

$2 x = \text{ln} 4$

**[M1]**

Now use the fact that $4 = 2^{2}$, so $\text{ln} 4 = 2 \text{ln} 2$, and the twos cancel

$x = \text{ln} 2  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **B1**: $y = 3$.
> 
> **M1**: $2 x = \text{ln} 4$, or $\sqrt{4} = \sqrt{\text{e}^{2x}}$, seen explicitly.
> 
> **A1**: $x = \text{ln} 2$.
> 
> Part (ii) is a "show that", so the intermediate line has to be seen. Writing down $x = \text{ln} 2$ with no working earns neither mark.
> 
> Halving the logarithm and square rooting the exponential are the two accepted routes, and either may be used.

> **[exam-tip]**
> Each axis crossing sets the other coordinate to zero.
> 
> - On the $y$-axis $x = 0$, and on the $x$-axis $y = 0$
> - Mixing the two up is the easiest mark in the question to throw away
> 
> $\text{e}^{0}$ is 1, not 0.
> 
> - So $A$ is at a height of 3, not 4
> 
> Two routes get from $\text{e}^{2x} = 4$ to $x = \text{ln} 2$.
> 
> - Take logarithms to get $2 x = \text{ln} 4$, then use $\text{ln} 4 = 2 \text{ln} 2$
> - Or square root first, giving $\text{e}^{x} = 2$ and so $x = \text{ln} 2$ in one step
> 
> Show the middle line.
> 
> - The answer is printed in the question, so the marks are entirely for the working that reaches it

### 11((b)) — 4 marks
A normal is perpendicular to the tangent, so start by differentiating $C$

- $4$ differentiates to 0, and $\text{e}^{2x}$ differentiates to $2 \text{e}^{2x}$

$\frac{\text{d}y}{\text{d}x} = - 2 \text{e}^{2x}$

**[M1]**

At $B$ the $x$ coordinate is $\text{ln} 2$, so substitute that in

- $\text{e}^{2\text{ln}2} = \text{e}^{\text{ln}4}$, which is 4

$\frac{\text{d}y}{\text{d}x} = - 2 \times 4$

$\frac{\text{d}y}{\text{d}x} = - 8$

**[M1]**

That is the gradient of the tangent, so take the negative reciprocal for the normal

$m = \frac{1}{8}$

Use `y - y_{1} = m \left(x - x_{1}\right)` through `B \left(\text{ln} 2 , 0\right)`

`y - 0 = \frac{1}{8} \left(x - \text{ln} 2\right)`

**[M1]**

Multiply out to reach the required form

$y = \frac{1}{8} x - \frac{1}{8} \text{ln} 2$

**[A1]**

> **[mark-scheme]**
> **M1**: Differentiates the equation of $C$. This must be correct, giving $\frac{\text{d}y}{\text{d}x} = - 2 \text{e}^{2x}$.
> 
> **M1**: Substitutes $\text{ln} 2$ into your derivative, reaching $- 8$.
> 
> **M1**: A correct method for finding the equation of a straight line, using your numerical perpendicular gradient together with $y = 0$ and $x = \text{ln} 2$. Where the form $y = m x + c$ is used, a value of $c$ must be found, and a decimal value which rounds to $- 0 . 087$ is accepted for this mark.
> 
> **A1**: $y = \frac{1}{8} x - \frac{1}{8} \text{ln} 2$, or the equivalent $y = \frac{x}{8} - \frac{\text{ln}2}{8}$, in exact form only.
> 
> The gradient of the normal must be the negative reciprocal of the tangent's gradient. Using $- 8$ itself in the equation of the line earns the third method mark but not the accuracy mark.

> **[exam-tip]**
> $\text{e}^{2\text{ln}2}$ is 4, and it is worth seeing why.
> 
> - $2 \text{ln} 2$ is $\text{ln} 4$, and $\text{e}$ to the power $\text{ln} 4$ is just 4
> - Equally, part (a) already told you $\text{e}^{2x} = 4$ at this point, so no new work is needed
> 
> Normal, not tangent.
> 
> - The tangent gradient is $- 8$, so the normal gradient is $\frac{1}{8}$
> - Two of the four marks here depend on making that switch
> 
> $B$ has a $y$ coordinate of 0.
> 
> - It is the crossing with the $x$-axis, so the point is `\left(\text{ln} 2 , 0\right)` and the $y - y_{1}$ term disappears
> 
> Leave $\text{ln} 2$ as it is.
> 
> - The final mark is for the exact form, so $- \frac{1}{8} \text{ln} 2$ must not be replaced by $- 0 . 087$

### 11((c)) — 7 marks
Picture the region first

- $R$ is bounded above by the curve $C$, which runs from `A \left(0 , 3\right)` down to `B \left(\text{ln} 2 , 0\right)`
- It is bounded below by the normal $l$, which meets the $y$-axis below the origin
- The $y$-axis closes it on the left

So the area splits into the part above the $x$-axis and the triangle below it

Take the curve first, integrating between the two $x$ values found in part (a)

`A_{C} = \int_{0}^{\text{ln} 2} \left(4 - \text{e}^{2 x}\right) \text{d} x`

**[M1]**

Integrate each term, remembering that $\text{e}^{2x}$ integrates to $\frac{1}{2} \text{e}^{2x}$

`A_{C} = \left[4 x - \frac{1}{2} \text{e}^{2 x}\right]_{0}^{\text{ln} 2}`

**[M1]**

Substitute both limits, using $\text{e}^{2\text{ln}2} = 4$ at the top and $\text{e}^{0} = 1$ at the bottom

`A_{C} = \left(4 \text{ln} 2 - 2\right) - \left(0 - \frac{1}{2}\right)`

**[M1]**

$A_{C} = 4 \text{ln} 2 - \frac{3}{2}$

Now the piece below the $x$-axis, which is a triangle

- Its vertices are the origin, `B \left(\text{ln} 2 , 0\right)`, and the point where $l$ crosses the $y$-axis
- Putting $x = 0$ into $l$ gives $y = - \frac{1}{8} \text{ln} 2$, so the depth below the origin is $\frac{1}{8} \text{ln} 2$
- The base along the $x$-axis is $\text{ln} 2$

$A_{T} = \frac{1}{2} \times \text{ln} 2 \times \frac{1}{8} \text{ln} 2$

**[M1]**

`A_{T} = \frac{1}{16} \left(\text{ln} 2\right)^{2}`

**[M1]**

Add the two pieces, since both lie inside $R$

`A = 4 \text{ln} 2 - \frac{3}{2} + \frac{1}{16} \left(\text{ln} 2\right)^{2}`

**[M1]**

Work that out, keeping full accuracy until the last line

- $4 \text{ln} 2 - \frac{3}{2} = 1 . 27258 \dots$ and `\frac{1}{16} \left(\text{ln} 2\right)^{2} = 0 . 03002 \ldots`

`A equals 1.3 space open parentheses 1 space straight d. straight p. close parentheses`

**[A1]**

> **[mark-scheme]**
> **M1**: A correct statement for the area under the curve with the correct limits, `\int_{0}^{\text{ln} 2} \left(4 - \text{e}^{2 x}\right) \text{d} x`. The limits may be either way around, poor notation is ignored, and this mark may be implied by later correct work.
> 
> **M1**: A minimally acceptable attempt to integrate, reaching `\left[4 x \pm \frac{\text{e}^{2 x}}{2}\right]`.
> 
> **M1**: Substitutes both limits into your integral of the curve.
> 
> **M1**: A statement of the area of the triangle, either as $\frac{1}{2} \times \text{ln} 2 \times \frac{1}{8} \text{ln} 2$ or as `\frac{1}{8} \int_{0}^{\text{ln} 2} \left(x - \text{ln} 2\right) \text{d} x` following through from your equation of the line, with the limits either way around.
> 
> **M1**: A correct method to evaluate the area of the triangle, reaching `\frac{1}{16} \left(\text{ln} 2\right)^{2}`. Where the integration route is used, the integration and substitution must both be correct.
> 
> **M1**: The total final area formed from your two values.
> 
> **A1**: An answer which rounds to $1 . 3$. The exact value `4 \text{ln} 2 - \frac{3}{2} + \frac{1}{16} \left(\text{ln} 2\right)^{2}` is also accepted.
> 
> Note that there is no accuracy mark for the area under the curve on its own. Six of the seven marks here are method marks, so a complete and correct strategy carries almost all of the credit even if the final arithmetic slips.
> 
> Integrating the line rather than treating the region as a triangle is equally acceptable and earns the same two marks.

> **[exam-tip]**
> Sketch the region before integrating anything.
> 
> - The curve is above the $x$-axis over the whole interval, and the normal is below it, so the two pieces are added rather than subtracted
> - Subtracting them is the commonest way to lose the last two marks
> 
> The triangle needs no calculus at all.
> 
> - Its base is $\text{ln} 2$ along the $x$-axis and its height is $\frac{1}{8} \text{ln} 2$ below the origin
> - Integrating the line works too and earns the same marks, but the triangle is quicker and harder to get wrong
> 
> Both limits came out of part (a).
> 
> - $x = 0$ at $A$ and $x = \text{ln} 2$ at $B$, so nothing new has to be found here
> 
> `\left(\text{ln} 2\right)^{2}` is not $\text{ln} 4$.
> 
> - $\text{ln} 2$ squared is about $0 . 48$, whereas $\text{ln} 4$ is about $1 . 39$
> - The triangle contributes only $0 . 03$ to the total, so treating it as $\text{ln} 4$ changes the answer to one decimal place
> 
> Keep the exact form until the end.
> 
> - `4 \text{ln} 2 - \frac{3}{2} + \frac{1}{16} \left(\text{ln} 2\right)^{2}` is worth writing down before rounding, since it is accepted as a final answer in its own right
