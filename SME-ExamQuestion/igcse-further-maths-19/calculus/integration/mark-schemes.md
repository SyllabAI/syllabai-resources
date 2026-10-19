# Mark Schemes — Integration
**Calculus** · Edexcel IGCSE Further Pure Maths (4PM1)


## Q1 — medium — 8 marks · exam-questions

### 11((a)) — 8 marks
The gradient function is given rather than the curve itself, so integrate to get back to `\text{f}\left(x\right)`

Integrating always introduces a constant, and a point on the curve is what fixes it

`y = \int \left(6 x^{2} - 26 x + 12\right) \textrm{ } \text{d} x`

Raise each power of $x$ by one and divide by the new power

$y = \frac{6x^{3}}{3} - \frac{26x^{2}}{2} + 12 x + c$

`\text{f}\left(x\right) = 2 x^{3} - 13 x^{2} + 12 x + c`

**[M1]**

Figure 3 shows the curve passing through `\left(- 1 , 0\right)`, so `\text{f}\left(- 1\right) = 0`

Substitute those coordinates to form an equation for $c$

`0 = 2 \left(- 1\right)^{3} - 13 \left(- 1\right)^{2} + 12 \left(- 1\right) + c`

**[M1]**

$0 = - 2 - 13 - 12 + c$

$c = 27$

`\text{f}\left(x\right) = 2 x^{3} - 13 x^{2} + 12 x + 27`

**[A1]**

The curve crosses the $x$-axis at `\left(- 1 , 0\right)`, so $x = - 1$ is a root and `\left(x + 1\right)` is a factor

Write the cubic as that factor times a quadratic, with $P$ and $Q$ to be found

`2 x^{3} - 13 x^{2} + 12 x + 27 = \left(x + 1\right)\left(2 x^{2} + P x + Q\right)`

Comparing the constant terms gives $Q$ straight away

$Q = 27$

Comparing the terms in $x^{2}$ gives $P + 2 = - 13$

$P = - 15$

Check with the terms in $x$, which must give $12$

$Q + P = 27 - 15$

`\text{f}\left(x\right) = \left(x + 1\right)\left(2 x^{2} - 15 x + 27\right)`

**[M1]**

Now factorise the quadratic

Two numbers multiplying to $2 \times 27 = 54$ and adding to $- 15$ are $- 6$ and $- 9$, so split the middle term

`2 x^{2} - 15 x + 27 = 2 x \left(x - 3\right) - 9 \left(x - 3\right)`

**[M1]**

`2 x^{2} - 15 x + 27 = \left(2 x - 9\right)\left(x - 3\right)`

`\text{f}\left(x\right) = \left(x + 1\right)\left(2 x - 9\right)\left(x - 3\right)`

**[A1]**

The curve meets the $x$-axis where `\text{f}\left(x\right) = 0`, so the three roots are $- 1$, $\frac{9}{2}$ and $3$

You are told that $0 < b < a$, so $a$ is the larger of the two positive roots and $b$ is the smaller

**(i)**

$a = \frac{9}{2}$

**[B1]**

**(ii)**

$b = 3$

**[B1]**

> **[mark-scheme]**
> **M1**: Integrates `\text{f}'\left(x\right)` term by term, raising each power of $x$ by one, and includes a constant of integration.
> 
> **M1**: Substitutes $x = - 1$ and $y = 0$ into the integrated expression to form an equation for that constant.
> 
> **A1**: The constant is $27$, giving `\text{f}\left(x\right) = 2 x^{3} - 13 x^{2} + 12 x + 27`.
> 
> **M1**: Takes out the factor `\left(x + 1\right)` to reach the quadratic factor $2 x^{2} - 15 x + 27$.
> 
> **M1**: Makes an acceptable attempt to factorise or to solve that quadratic.
> 
> **A1**: Correct factors `\left(2 x - 9\right)\left(x - 3\right)`, or the two correct roots of the quadratic.
> 
> **B1**: $a = \frac{9}{2}$.
> 
> **B1**: $b = 3$.
> 
> The official scheme marks parts (i) and (ii) together, so all eight marks are available across the whole of your working rather than being split between the two answers.
> 
> Long division of $2 x^{3} - 13 x^{2} + 12 x + 27$ by `\left(x + 1\right)` is equally acceptable in place of comparing coefficients, and earns the fourth mark in the same way. Using the quadratic formula on $2 x^{2} - 15 x + 27 = 0$ instead of factorising earns the fifth mark, with the accuracy mark then given for the two correct roots.
> 
> Accept $a = 4 . 5$ for the first B mark. This part has no marking notes in the official scheme, so its marks are printed a row at a time and the descriptors above follow those rows in order.

> **[exam-tip]**
> A gradient function on its own cannot fix a curve, because sliding a curve up or down leaves its gradient unchanged everywhere.
> 
> - Integrating `\text{f}'\left(x\right)` always leaves a constant behind, and one point on the curve is what pins it down
> - Here that point is `\left(- 1 , 0\right)`, which is printed on Figure 3 rather than written in the text
> 
> A root of `\text{f}\left(x\right)` and a factor of `\text{f}\left(x\right)` are the same piece of information written two ways.
> 
> - The curve crosses at `\left(- 1 , 0\right)`, so `\text{f}\left(- 1\right) = 0` and `\left(x + 1\right)` must be a factor
> - That is what lets you take a cubic you cannot factorise by inspection down to a quadratic you can
> 
> Read the condition $0 < b < a$ before you decide which root is which.
> 
> - The factorised form gives $\frac{9}{2}$ and $3$, and only the condition tells you which is $a$
> - Writing them the wrong way round loses both of the final marks even though every earlier step was right

## Q2 — medium — 7 marks · exam-questions

### 5((a)) — 2 marks
Both sides of this identity involve $A$ and $B$ separately on the right and combined on the left, so expand the two compound angles

Use the addition formulae for cosine, which differ only in the sign of the second term

`\text{cos} \left(A - B\right) = \text{cos} A \text{cos} B + \text{sin} A \text{sin} B`

`\text{cos} \left(A + B\right) = \text{cos} A \text{cos} B - \text{sin} A \text{sin} B`

**[M1]**

Subtract the second from the first, taking care with the signs inside the bracket

`\text{cos} \left(A - B\right) - \text{cos} \left(A + B\right) = \text{cos} A \text{cos} B + \text{sin} A \text{sin} B - \text{cos} A \text{cos} B + \text{sin} A \text{sin} B`

The two $\text{cos} A \text{cos} B$ terms cancel and the two $\text{sin} A \text{sin} B$ terms add

`\text{cos} \left(A - B\right) - \text{cos} \left(A + B\right) = 2 \text{sin} A \text{sin} B \textrm{ } \text{as required}`

**[A1]**

> **[mark-scheme]**
> **M1**: Expands both `\text{cos} \left(A - B\right)` and `\text{cos} \left(A + B\right)` correctly using the addition formulae.
> 
> **A1**: Subtracts them correctly and reaches the given result with no errors.
> 
> The result is given in the question, so every line has to be correct. Starting from the right-hand side and working back to the left is equally acceptable.

> **[exam-tip]**
> Both cosine addition formulae are on the formulae sheet, so quote them rather than trusting memory.
> 
> - The sign flips: `\text{cos} \left(A + B\right)` takes a minus and `\text{cos} \left(A - B\right)` takes a plus
> - That sign flip is the entire reason the subtraction leaves $2 \text{sin} A \text{sin} B$ behind
> 
> The bracket in the subtraction is where marks are lost.
> 
> - Subtracting $- \text{sin} A \text{sin} B$ gives $+ \text{sin} A \text{sin} B$, so the sine terms add rather than cancel
> - Write the second expansion inside brackets before you subtract, then remove them in a separate step
> 
> This identity is the product-to-sum result, and it is worth recognising.
> 
> - It turns a product of two sines into a difference of two cosines, which is exactly what makes part (c) integrable
> - A product of trigonometric functions cannot be integrated directly, so questions like this almost always convert first

### 5((b)) — 1 marks
The word "hence" means part (a) does the work, so match the two expressions up

Part (a) says `2 \text{sin} A \text{sin} B = \text{cos} \left(A - B\right) - \text{cos} \left(A + B\right)`, and here the product is $2 \text{sin} 5 x \text{sin} 3 x$

So take $A = 5 x$ and $B = 3 x$

$A - B = 5 x - 3 x$

$A - B = 2 x$

$A + B = 5 x + 3 x$

$A + B = 8 x$

Substitute those two angles into the result from part (a)

$2 \text{sin} 5 x \text{sin} 3 x = \text{cos} 2 x - \text{cos} 8 x$

**[B1]**

so $m = 2$ and $n = 8$

> **[mark-scheme]**
> **B1**: $\text{cos} 2 x - \text{cos} 8 x$, with both values identified.
> 
> The terms must be in this order, since the form given in the question is $\text{cos} m x - \text{cos} n x$. Writing $\text{cos} 8 x - \text{cos} 2 x$ has the sign the wrong way round and earns nothing.

> **[exam-tip]**
> "Hence" is an instruction, not a suggestion.
> 
> - The one mark here is for spotting that $A = 5 x$ and $B = 3 x$ turns part (a) straight into the answer
> - Expanding from scratch wastes several minutes and risks a sign slip
> 
> Check which of $m$ and $n$ is which before you write the answer down.
> 
> - The difference $A - B$ goes with the plus sign in the identity, so $\text{cos} 2 x$ comes first
> - Getting them the wrong way round changes the sign of the whole expression

### 5((c)) — 4 marks
**(i)**

A product of two sines cannot be integrated as it stands, so use part (b) to turn it into a sum

Part (b) gives $2 \text{sin} 5 x \text{sin} 3 x = \text{cos} 2 x - \text{cos} 8 x$, and here the coefficient is 4 rather than 2

So the integrand is twice the expression from part (b), with $θ$ in place of $x$

`\int 4 \text{sin} 5 \theta \text{sin} 3 \theta \text{d} \theta = 2 \int \left(\text{cos} 2 \theta - \text{cos} 8 \theta\right) \text{d} \theta`

**[M1]**

Integrating $\text{cos} k θ$ gives $\frac{\text{sin}kθ}{k}$, so divide each term by the multiple of $θ$ inside it

`\int 4 \text{sin} 5 \theta \text{sin} 3 \theta \text{d} \theta = 2 \left[\frac{\text{sin} 2 \theta}{2} - \frac{\text{sin} 8 \theta}{8}\right] + c`

**[A1]**

**(ii)**

"Hence" again, so use the integral you have just found and put the limits in

`\int_{0}^{\frac{\pi}{6}} 4 \text{sin} 5 \theta \text{sin} 3 \theta \text{d} \theta = 2 \left[\frac{\text{sin} 2 \theta}{2} - \frac{\text{sin} 8 \theta}{8}\right]_{0}^{\frac{\pi}{6}}`

At the upper limit the two angles are $\frac{π}{3}$ and $\frac{4π}{3}$

$\text{sin} \frac{π}{3} = \frac{\sqrt{3}}{2}$

$\text{sin} \frac{4π}{3} = - \frac{\sqrt{3}}{2}$

At the lower limit both sines are zero, so that whole bracket contributes nothing

`\int_{0}^{\frac{\pi}{6}} 4 \text{sin} 5 \theta \text{sin} 3 \theta \text{d} \theta = 2 \left[\frac{\sqrt{3}}{4} + \frac{\sqrt{3}}{16}\right]`

**[M1]**

Write both terms over 16 before adding

`\int_{0}^{\frac{\pi}{6}} 4 \text{sin} 5 \theta \text{sin} 3 \theta \text{d} \theta = 2 \times \frac{5 \sqrt{3}}{16}`

`\int_{0}^{\frac{\pi}{6}} 4 \text{sin} 5 \theta \text{sin} 3 \theta \text{d} \theta = \frac{5 \sqrt{3}}{8}`

**[A1]**

> **[mark-scheme]**
> **M1**: Uses part (b) to write the integrand as a multiple of $\text{cos} 2 θ - \text{cos} 8 θ$, and integrates to obtain terms of the form $p \text{sin} 2 θ + q \text{sin} 8 θ$.
> 
> **A1**: A fully correct integral, `2 \left[\frac{\text{sin} 2 \theta}{2} - \frac{\text{sin} 8 \theta}{8}\right] + c` or any equivalent form such as $\text{sin} 2 θ - \frac{1}{4} \text{sin} 8 θ + c$.
> 
> **M1**: Substitutes both limits into your integrated expression and subtracts.
> 
> **A1**: $\frac{5\sqrt{3}}{8}$.
> 
> The constant of integration is required in the first sub-part but is not needed in the second.
> 
> Working in degrees is equally acceptable, provided the limits are converted, so the upper limit becomes $30 \circ$ and the two angles become $60 \circ$ and $240 \circ$.
> 
> The final answer must be exact, so $1 . 08$ earns nothing on the last mark.

> **[exam-tip]**
> A product of trigonometric functions is a signal to convert before integrating.
> 
> - There is no product rule for integration, so `\int \text{sin} 5 \theta \text{sin} 3 \theta \text{d} \theta` cannot be started directly
> - Parts (a) and (b) exist purely to hand you the sum form, so use them
> 
> Match the coefficient carefully when you reuse part (b).
> 
> - Part (b) converts $2 \text{sin} 5 x \text{sin} 3 x$, and the integrand here is $4 \text{sin} 5 θ \text{sin} 3 θ$, which is twice as big
> - Forgetting that factor of 2 halves the final answer
> 
> When integrating $\text{cos} k θ$, divide by $k$ rather than multiplying.
> 
> - `\int \text{cos} 8 \theta \text{d} \theta = \frac{\text{sin} 8 \theta}{8}`, so the term with the larger angle ends up the smaller
> - Differentiating your answer back is a quick way to check the divisions
> 
> The negative sine at the upper limit is where the answer grows rather than shrinks.
> 
> - $\frac{4π}{3}$ is in the third quadrant, so $\text{sin} \frac{4π}{3} = - \frac{\sqrt{3}}{2}$
> - Subtracting that negative value adds $\frac{\sqrt{3}}{16}$ on, which is what turns $\frac{4\sqrt{3}}{16}$ into $\frac{5\sqrt{3}}{16}$
> 
> Both limits still have to be substituted, even when one of them gives zero.
> 
> - Show the lower limit producing $\text{sin} 0 = 0$ rather than silently dropping it

## Q3 — medium — 16 marks · exam-questions

### 11((a)) — 4 marks
**(i)**

A double angle is an angle added to itself, so start from the addition formula on the formulae sheet

Use `\text{cos} \left(A + B\right) = \text{cos} A \text{cos} B - \text{sin} A \text{sin} B` with both angles equal to $A$

$\text{cos} 2 A = \text{cos}^{2} A - \text{sin}^{2} A$

**[M1]**

The target has only cosines in it, so remove the sine using $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$

`\text{cos} 2 A = \text{cos}^{2} A - \left(1 - \text{cos}^{2} A\right)`

**[M1]**

Remove the bracket and collect the two cosine terms

$\text{cos} 2 A = 2 \text{cos}^{2} A - 1  \text{as required}$

**[A1]**

**(ii)**

Do the same with the sine addition formula, `\text{sin} \left(A + B\right) = \text{sin} A \text{cos} B + \text{cos} A \text{sin} B`

$\text{sin} 2 A = \text{sin} A \text{cos} A + \text{cos} A \text{sin} A$

The two terms are the same product written the other way round, so they add

$\text{sin} 2 A = 2 \text{sin} A \text{cos} A  \text{as required}$

**[B1]**

> **[mark-scheme]**
> **M1**: Correct use of the addition formula for `\text{cos} \left(A + A\right)`.
> 
> **M1**: Correct use of $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$ to eliminate $\text{sin}^{2} A$.
> 
> **A1**: Reaches the first given result with no errors.
> 
> **B1**: A complete derivation of the second given result from the addition formula for `\text{sin} \left(A + A\right)`.
> 
> Both answers are given, so both derivations must be complete.

> **[exam-tip]**
> The formulae sheet gives the addition formulae, not the double angle ones.
> 
> - Setting $B = A$ in `\text{cos} \left(A + B\right)` and `\text{sin} \left(A + B\right)` is what produces them
> - That is why these two derivations appear so often as opening parts
> 
> The sine version needs one step and the cosine version needs two.
> 
> - $\text{sin} 2 A$ is finished as soon as you collect the two identical products
> - $\text{cos} 2 A = \text{cos}^{2} A - \text{sin}^{2} A$ is correct but not the required form, so the Pythagorean identity has to follow
> 
> These two results are the engine for the rest of the question.
> 
> - Part (b) builds $\text{cos} 3 A$ out of both of them
> - Part (d) then uses part (b) to integrate a cube, which cannot be integrated directly

### 11((b)) — 4 marks
A triple angle is a double angle plus a single one, so split $3 A$ that way and use the cosine addition formula

$\text{cos} 3 A = \text{cos} 2 A \text{cos} A - \text{sin} 2 A \text{sin} A$

**[M1]**

Now substitute both results from part (a)

`\text{cos} 3 A = \left(2 \text{cos}^{2} A - 1\right) \text{cos} A - 2 \text{sin} A \text{cos} A \text{sin} A`

**[M1]**

Expand the first bracket, and write the two sines as a square

$\text{cos} 3 A = 2 \text{cos}^{3} A - \text{cos} A - 2 \text{sin}^{2} A \text{cos} A$

There is still a sine in the expression, so remove it with $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$

`\text{cos} 3 A = 2 \text{cos}^{3} A - \text{cos} A - 2 \left(1 - \text{cos}^{2} A\right) \text{cos} A`

Expand that bracket, taking care with the two minus signs

$\text{cos} 3 A = 2 \text{cos}^{3} A - \text{cos} A - 2 \text{cos} A + 2 \text{cos}^{3} A$

Collect the cubes and collect the single cosines

$\text{cos} 3 A = 4 \text{cos}^{3} A - 3 \text{cos} A$

**[M1]**

Rearrange to make $\text{cos}^{3} A$ the subject

$4 \text{cos}^{3} A = \text{cos} 3 A + 3 \text{cos} A$

$\text{cos}^{3} A = \frac{\text{cos}3A+3\text{cos}A}{4}  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Writes $\text{cos} 3 A$ as `\text{cos} \left(2 A + A\right)` and expands correctly with the addition formula.
> 
> **M1**: Substitutes both results from part (a).
> 
> **M1**: Uses $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$ and simplifies to $4 \text{cos}^{3} A - 3 \text{cos} A$.
> 
> **A1**: Rearranges to the given result with no errors.
> 
> Starting from the right-hand side and working back to the left is equally acceptable, and carries the same four marks in the same order.
> 
> Splitting $3 A$ as $A + 2 A$ rather than $2 A + A$ is also equally acceptable.

> **[exam-tip]**
> Any multiple angle can be broken down into ones you already have.
> 
> - $3 A = 2 A + A$ turns an unfamiliar triple angle into an addition formula plus the two results from part (a)
> - The same trick handles $4 A$ as $2 A + 2 A$, and so on
> 
> Expect to use the Pythagorean identity a second time.
> 
> - Substituting part (a) leaves a $\text{sin}^{2} A$ term behind, and the target has no sines in it at all
> - Whenever a proof is meant to end in one function only, that identity is how you get there
> 
> Watch the double minus in the expansion.
> 
> - `- 2 \left(1 - \text{cos}^{2} A\right) \text{cos} A` gives $- 2 \text{cos} A + 2 \text{cos}^{3} A$
> - Getting that sign wrong gives $- 3 \text{cos}^{3} A$ instead of $4 \text{cos}^{3} A$, and the proof will not close
> 
> This result is what makes parts (c) and (d) possible.
> 
> - A cubed cosine cannot be solved for or integrated directly, but a sum of ordinary cosines can
> - Reading ahead to see what the later parts need is a good way to understand why a proof is being asked for

### 11((c)) — 4 marks
The equation contains a cubed cosine and an ordinary cosine of the same angle, which is exactly the shape part (b) deals with

Part (b) rearranges to $4 \text{cos}^{3} A = \text{cos} 3 A + 3 \text{cos} A$, so doubling it gives the $8 \text{cos}^{3} A$ the equation needs

$8 \text{cos}^{3} A = 2 \text{cos} 3 A + 6 \text{cos} A$

Here the angle playing the part of $A$ is $\frac{θ}{2}$, so $3 A$ becomes $\frac{3θ}{2}$

Substitute into the equation

$2 \text{cos} \frac{3θ}{2} + 6 \text{cos} \frac{θ}{2} - 6 \text{cos} \frac{θ}{2} - 1 = 0$

**[M1]**

The two $\text{cos} \frac{θ}{2}$ terms cancel, which is the whole point of the substitution

$2 \text{cos} \frac{3θ}{2} = 1$

$\text{cos} \frac{3θ}{2} = \frac{1}{2}$

**[M1]**

Solve for $\frac{3θ}{2}$ rather than $θ$, and scale the range to match

Since $0 \leq θ \leq 2 π$, the angle $\frac{3θ}{2}$ runs from $0$ to $3 π$

The cosine is $\frac{1}{2}$ at $\frac{π}{3}$, and then at $\frac{π}{3}$ either side of every multiple of $2 π$

$\frac{3θ}{2} = \frac{π}{3} , \frac{5π}{3} , \frac{7π}{3}$

**[M1]**

The next one would be $\frac{11π}{3}$, which is beyond $3 π$

Multiply each value by $\frac{2}{3}$ to get back to $θ$

$θ = \frac{2π}{9} , \frac{10π}{9} , \frac{14π}{9}$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses part (b) to replace `8 \text{cos}^{3} \left(\frac{\theta}{2}\right)` by $2 \text{cos} \frac{3θ}{2} + 6 \text{cos} \frac{θ}{2}$.
> 
> **M1**: Rearranges to $\text{cos} \frac{3θ}{2} = \frac{1}{2}$.
> 
> **M1**: Finds at least one correct value for $\frac{3θ}{2}$, having scaled the range to $0 \leq \frac{3θ}{2} \leq 3 π$.
> 
> **A1**: All three values of $θ$, and no extra values inside the range.
> 
> The question asks for exact values in terms of $π$, so decimal answers earn nothing on the final mark.
> 
> Working in degrees throughout is equally acceptable, provided the answers are converted back, giving $40 \circ$, $200 \circ$ and $280 \circ$.

> **[exam-tip]**
> "Hence, or otherwise" is a strong hint that the previous part does most of the work.
> 
> - Without part (b) this is a cubic in `\text{cos} \left(\frac{\theta}{2}\right)` with no obvious factorisation
> - With it, the whole equation collapses to a single cosine in two lines
> 
> The angle inside the cosine is $\frac{θ}{2}$, so the identity's $3 A$ becomes $\frac{3θ}{2}$.
> 
> - Substituting $A = \frac{θ}{2}$ carefully is where most of the difficulty in this part sits
> - Writing $A = \frac{θ}{2}$ down explicitly before you start is worth the line
> 
> Scale the range by exactly the same factor as the angle.
> 
> - $θ$ becoming $\frac{3θ}{2}$ multiplies the range by $\frac{3}{2}$, so $2 π$ becomes $3 π$
> - That wider range is why there are three answers rather than two, and stopping early is the usual error
> 
> The cosine takes each value twice per revolution.
> 
> - $\text{cos} x = \frac{1}{2}$ at $\frac{π}{3}$ and at $2 π - \frac{π}{3} = \frac{5π}{3}$, then repeats every $2 π$
> - Listing the values of $\frac{3θ}{2}$ first and scaling at the end is far safer than scaling as you go

### 11((d)) — 4 marks
A cubed cosine cannot be integrated directly, so use part (b) to turn it into a sum of ordinary cosines

Multiplying part (b) by 4 gives $4 \text{cos}^{3} θ = \text{cos} 3 θ + 3 \text{cos} θ$

Call the integral $I$

`I = \int_{0}^{\frac{\pi}{6}} \left(\text{cos} 3 \theta + 3 \text{cos} \theta - \text{sin} 2 \theta\right) \text{d} \theta`

**[M1]**

Integrate term by term, dividing by the multiple of $θ$ inside each function

Note that integrating $- \text{sin} 2 θ$ gives $+ \frac{\text{cos}2θ}{2}$, because the minus signs cancel

`I = \left[\frac{\text{sin} 3 \theta}{3} + 3 \text{sin} \theta + \frac{\text{cos} 2 \theta}{2}\right]_{0}^{\frac{\pi}{6}}`

**[M1]**

At the upper limit the three angles are $\frac{π}{2}$, $\frac{π}{6}$ and $\frac{π}{3}$, all with exact values

$\frac{\text{sin}\frac{π}{2}}{3} + 3 \text{sin} \frac{π}{6} + \frac{\text{cos}\frac{π}{3}}{2} = \frac{1}{3} + \frac{3}{2} + \frac{1}{4}$

$\frac{1}{3} + \frac{3}{2} + \frac{1}{4} = \frac{25}{12}$

At the lower limit both sines are zero, but the cosine term is not

$\frac{\text{sin}0}{3} + 3 \text{sin} 0 + \frac{\text{cos}0}{2} = \frac{1}{2}$

Subtract the lower value from the upper one

$I = \frac{25}{12} - \frac{1}{2}$

**[M1]**

$I = \frac{19}{12}$

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces $4 \text{cos}^{3} θ$ by $\text{cos} 3 θ + 3 \text{cos} θ$ using part (b).
> 
> **M1**: Integrates to obtain terms of the form $p \text{sin} 3 θ + q \text{sin} θ + r \text{cos} 2 θ$.
> 
> **M1**: Substitutes both limits into your integrated expression and subtracts.
> 
> **A1**: $\frac{19}{12}$.
> 
> The lower limit does not vanish here, because $\text{cos} 0 = 1$. Dropping it gives $\frac{25}{12}$ and loses the final mark.
> 
> The question asks for an exact value, so $1 . 58$ earns nothing on the last mark.

> **[exam-tip]**
> A power of a trigonometric function is a signal to convert before integrating.
> 
> - There is no rule for integrating $\text{cos}^{3} θ$ as it stands
> - Every part of this question has been building towards this moment, so use part (b) rather than starting again
> 
> Two sign changes are easy to lose here.
> 
> - Integrating $- \text{sin} 2 θ$ gives $+ \frac{\text{cos}2θ}{2}$, since the integral of $\text{sin}$ is $- \text{cos}$
> - Differentiating your integrated expression back is the quickest way to check both the signs and the divisions
> 
> Never assume the lower limit contributes nothing.
> 
> - Two of the three terms do vanish at $θ = 0$, but $\frac{\text{cos}0}{2} = \frac{1}{2}$ does not
> - Writing out the lower bracket in full, even when most of it is zero, is what stops this being missed
> 
> Keep everything as fractions.
> 
> - The answer is exact, so $\frac{1}{3} + \frac{3}{2} + \frac{1}{4}$ should be put over 12 rather than turned into decimals
> - A common denominator at the end is much safer than rounding at each step

## Q4 — medium — 14 marks · exam-questions

### 9((a)) — 2 marks
A double angle is an angle added to itself, so start from the addition formula on the formulae sheet

Use `\text{cos} \left(A + B\right) = \text{cos} A \text{cos} B - \text{sin} A \text{sin} B` with both angles equal to $θ$

$\text{cos} 2 θ = \text{cos}^{2} θ - \text{sin}^{2} θ$

The target has only cosines in it, so replace the sine using $\text{sin}^{2} θ + \text{cos}^{2} θ \equiv 1$

`\text{cos} 2 \theta = \text{cos}^{2} \theta - \left(1 - \text{cos}^{2} \theta\right)`

**[M1]**

Remove the bracket and collect the two cosine terms

$\text{cos} 2 θ = 2 \text{cos}^{2} θ - 1  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Expands `\text{cos} \left(\theta + \theta\right)` to $\text{cos}^{2} θ - \text{sin}^{2} θ$ and replaces $\text{sin}^{2} θ$ by $1 - \text{cos}^{2} θ$.
> 
> **A1**: Reaches the given result with no errors.
> 
> The answer is given, so the working must be complete.

> **[exam-tip]**
> The formulae sheet gives the addition formulae, and setting the two angles equal produces the double angle ones.
> 
> - `\text{cos} 2 \theta = \text{cos} \left(\theta + \theta\right)` is the whole idea
> - The expansion $\text{cos}^{2} θ - \text{sin}^{2} θ$ is correct but is not the form asked for
> 
> Take care with the minus sign in front of the bracket.
> 
> - `\text{cos}^{2} \theta - \left(1 - \text{cos}^{2} \theta\right)` gives $2 \text{cos}^{2} θ - 1$
> - Writing the substitution inside brackets and removing them on a separate line is what keeps the sign right
> 
> This one line is what makes the whole question work.
> 
> - $2 \text{cos}^{2} θ - 1$ cannot be integrated as it stands, but $\text{cos} 2 θ$ can
> - Parts (b) and (c) both depend on making that swap first

### 9((b)) — 4 marks
$2 \text{cos}^{2} θ - 1$ cannot be integrated as it stands, but part (a) says it is exactly $\text{cos} 2 θ$, which can

Call the integral $I$ and make that swap first

`I = \int_{\frac{\pi}{3}}^{\frac{3 \pi}{4}} \text{cos} 2 \theta \text{d} \theta`

**[M1]**

Integrating $\text{cos} 2 θ$ gives $\frac{\text{sin}2θ}{2}$, dividing by the 2 inside the function

`I = \left[\frac{\text{sin} 2 \theta}{2}\right]_{\frac{\pi}{3}}^{\frac{3 \pi}{4}}`

**[M1]**

Substitute the limits, doubling each one before taking the sine

$I = \frac{\text{sin}\frac{3π}{2}}{2} - \frac{\text{sin}\frac{2π}{3}}{2}$

**[M1]**

$\text{sin} \frac{3π}{2} = - 1$ and $\text{sin} \frac{2π}{3} = \frac{\sqrt{3}}{2}$, both exact values

$I = - \frac{1}{2} - \frac{\sqrt{3}}{4}$

Put both terms over 4 and take out the minus sign

$I = - \frac{2+\sqrt{3}}{4}$

**[A1]**

so $a = 2$, $b = 3$ and $c = 4$

> **[mark-scheme]**
> **M1**: Replaces $2 \text{cos}^{2} θ - 1$ by $\text{cos} 2 θ$.
> 
> **M1**: Integrates to $\pm \frac{\text{sin}2θ}{2}$.
> 
> **M1**: Substitutes both limits correctly and subtracts.
> 
> **A1**: $- \frac{2+\sqrt{3}}{4}$, with the three values identified.
> 
> The answer is given in the question in the form $- \frac{a+\sqrt{b}}{c}$, so the working has to be complete.
> 
> Any equivalent correct set of values is accepted, so $a = 4$, $b = 12$, $c = 8$ would also be credited.

> **[exam-tip]**
> Part (a) is not decoration, it is the first line of part (b).
> 
> - A squared trigonometric function has no direct integral, so the double angle form is the only way in
> - Whenever a question proves an identity and then asks you to integrate, expect to use it immediately
> 
> Double the limits, not the answer.
> 
> - $\text{sin} 2 θ$ at $θ = \frac{3π}{4}$ means $\text{sin} \frac{3π}{2}$, not $\text{sin} \frac{3π}{4}$
> - Writing the doubled angle out before evaluating it is the habit that prevents this
> 
> A negative answer is expected here, so do not "correct" it.
> 
> - Between $\frac{π}{3}$ and $\frac{3π}{4}$ the curve $y = \text{cos} 2 θ$ lies below the axis
> - The question even prints a minus sign in the required form, which is a useful confirmation
> 
> Match your answer to the form asked for.
> 
> - The target is $- \frac{a+\sqrt{b}}{c}$ with integers, so $- \frac{1}{2} - \frac{\sqrt{3}}{4}$ has to be combined over a single denominator
> - Stopping one line early is the commonest way to lose the accuracy mark on a question like this

### 9((c)) — 8 marks
Read the region off Figure 3 first, because the limits come from the diagram rather than from the algebra

$R$ sits below the $θ$-axis, with $C_{1}$ as its lower boundary all the way from $B$ across to $A$

On the left it is closed off by $C_{2}$, between $B$ and $E$

$B$ is where the two curves meet, so equate them

$2 \text{cos}^{2} θ - 1 = - \text{cos} θ$

**[M1]**

Collect everything on one side to get a quadratic in $\text{cos} θ$

$2 \text{cos}^{2} θ + \text{cos} θ - 1 = 0$

`\left(2 \text{cos} \theta - 1\right) \left(\text{cos} \theta + 1\right) = 0`

**[M1]**

The second factor gives $\text{cos} θ = - 1$, which is $θ = π$, and Figure 3 puts $B$ well to the left of that

$\text{cos} θ = \frac{1}{2}$

$θ = \frac{π}{3}$

**[A1]**

Part (b) has already integrated $C_{1}$ between exactly these limits, $\frac{π}{3}$ at $B$ and $\frac{3π}{4}$ at $A$

That result is negative because the curve is below the axis, so the area it encloses with the axis is $\frac{2+\sqrt{3}}{4}$

That region is slightly too big, since it includes the strip between $C_{2}$ and the axis from $B$ across to $E$

Call that second integral $J$, running from $\frac{π}{3}$ to $\frac{π}{2}$

`J = \int_{\frac{\pi}{3}}^{\frac{\pi}{2}} - \text{cos} \theta \text{d} \theta`

**[M1]**

`J = \left[- \text{sin} \theta\right]_{\frac{\pi}{3}}^{\frac{\pi}{2}}`

**[M1]**

$J = - \text{sin} \frac{π}{2} + \text{sin} \frac{π}{3}$

$J = \frac{-2+\sqrt{3}}{2}$

**[M1]**

This is negative too, so the area of that strip is $\frac{2-\sqrt{3}}{2}$

Subtract the strip from the larger region

$\text{Area of}  R = \frac{2+\sqrt{3}}{4} - \frac{2-\sqrt{3}}{2}$

**[M1]**

Write both terms over 4 before subtracting

$\text{Area of}  R = \frac{-2+3\sqrt{3}}{4}$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets the two curve equations equal to each other.
> 
> **M1**: Reaches a three-term quadratic in $\text{cos} θ$ and attempts to solve it.
> 
> **A1**: $θ = \frac{π}{3}$ at $B$.
> 
> **M1**: Sets up a correct integral for the area between $C_{2}$ and the $θ$-axis, from your $θ$ at $B$ to $\frac{π}{2}$.
> 
> **M1**: Integrates $- \text{cos} θ$ to $- \text{sin} θ$.
> 
> **M1**: Substitutes both limits correctly and subtracts.
> 
> **A1**: A correct combination of your two areas. This mark depends on the previous method mark.
> 
> **A1**: $\frac{-2+3\sqrt{3}}{4}$, or any exact equivalent such as $\frac{3\sqrt{3}-2}{4}$.
> 
> Both integrals come out negative because both curves lie below the axis over these limits, so their sizes are what get combined.
> 
> Working with the difference of the two curves is equally acceptable, and is marked like this. Setting up `\int_{\frac{\pi}{3}}^{\frac{\pi}{2}} \left(- \text{cos} \theta - \text{cos} 2 \theta\right) \text{d} \theta + \int_{\frac{\pi}{2}}^{\frac{3 \pi}{4}} \left(- \text{cos} 2 \theta\right) \text{d} \theta` earns the fourth mark, integrating both earns the fifth, substituting all four limits earns the sixth, and combining them correctly earns the seventh. The final answer is the same.

> **[exam-tip]**
> Work out what the region actually is before writing any integral down.
> 
> - $R$ has three different boundaries, so no single integral covers it
> - Marking the two curves and the axis on the figure, and then asking which is on top over each stretch, is time well spent
> 
> The earlier parts hand you one of the two integrals.
> 
> - Part (b) integrates $C_{1}$ from $\frac{π}{3}$ to $\frac{3π}{4}$, and those are exactly the $θ$ values at $B$ and $A$
> - That is not a coincidence, so treat it as confirmation that $θ = \frac{π}{3}$ at $B$ is right
> 
> A negative integral is not a mistake when the curve is below the axis.
> 
> - Both integrals here come out negative, and it is their sizes that combine to give an area
> - Taking the size at the end, rather than dropping minus signs as you go, is what keeps the arithmetic honest
> 
> Choose the correct root from the quadratic.
> 
> - $\text{cos} θ = - 1$ gives $θ = π$, which is a genuine intersection of the two curves but is off to the right of $A$
> - Figure 3 is what tells you which root is $B$, so use the diagram rather than picking the first root you find
> 
> Subtracting is easier than adding here.
> 
> - Taking the whole region under $C_{1}$ and removing the strip under $C_{2}$ needs two integrals
> - Integrating the difference of the curves and then a second piece also works, but it needs four limits rather than three

## Q5 — medium — 17 marks · exam-questions

### 10((a)) — 3 marks
**(i)**

A double angle is an angle added to itself, so use the sine addition formula from the formulae sheet with both angles equal to $A$

$\text{sin} 2 A = \text{sin} A \text{cos} A + \text{cos} A \text{sin} A$

The two terms are the same product written the other way round, so they add

$\text{sin} 2 A = 2 \text{sin} A \text{cos} A  \text{as required}$

**[B1]**

**(ii)**

Do the same with the cosine addition formula, `\text{cos} \left(A + B\right) = \text{cos} A \text{cos} B - \text{sin} A \text{sin} B`

$\text{cos} 2 A = \text{cos}^{2} A - \text{sin}^{2} A$

The target has only cosines in it, so replace the sine using $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$

`\text{cos} 2 A = \text{cos}^{2} A - \left(1 - \text{cos}^{2} A\right)`

**[M1]**

Remove the bracket and collect the two cosine terms

$\text{cos} 2 A = 2 \text{cos}^{2} A - 1  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **B1**: A complete derivation of the first given result from the addition formula for `\text{sin} \left(A + A\right)`.
> 
> **M1**: Expands `\text{cos} \left(A + A\right)` correctly and replaces $\text{sin}^{2} A$ by $1 - \text{cos}^{2} A$.
> 
> **A1**: Reaches the second given result with no errors.
> 
> Both answers are given, so both derivations must be complete.

> **[exam-tip]**
> The formulae sheet carries the addition formulae, and the double angle ones follow in a line.
> 
> - Setting $B = A$ is the whole method, and it works for sine, cosine and tangent alike
> - The sine version finishes immediately, while the cosine version needs the Pythagorean identity as well
> 
> Watch the minus sign in front of the bracket.
> 
> - `\text{cos}^{2} A - \left(1 - \text{cos}^{2} A\right)` gives $2 \text{cos}^{2} A - 1$
> - Writing the bracket in and removing it on its own line is what keeps the sign right
> 
> These two results are used in every remaining part of the question.
> 
> - Part (b) needs the sine version, part (c) needs both, and part (d) needs part (b)
> - Two marks here unlock fourteen more, so it is worth doing carefully

### 10((b)) — 4 marks
The target is written in sines and cosines and the starting expression is written in tangents, so convert everything to sines and cosines first

Replace each $\text{tan} θ$ by $\frac{\text{sin}θ}{\text{cos}θ}$

`\text{f} \left(\theta\right) = \frac{2 \frac{\text{sin} \theta}{\text{cos} \theta}}{1 + \frac{\text{sin}^{2} \theta}{\text{cos}^{2} \theta}}`

**[M1]**

Write the denominator as a single fraction over $\text{cos}^{2} θ$

`\text{f} \left(\theta\right) = \frac{2 \frac{\text{sin} \theta}{\text{cos} \theta}}{\frac{\text{cos}^{2} \theta + \text{sin}^{2} \theta}{\text{cos}^{2} \theta}}`

**[M1]**

The numerator of that denominator is 1, by $\text{sin}^{2} θ + \text{cos}^{2} θ \equiv 1$

Dividing by $\frac{1}{\text{cos}^{2}θ}$ is the same as multiplying by $\text{cos}^{2} θ$

`\text{f} \left(\theta\right) = 2 \frac{\text{sin} \theta}{\text{cos} \theta} \times \text{cos}^{2} \theta`

**[M1]**

One $\text{cos} θ$ cancels with the denominator

`\text{f} \left(\theta\right) = 2 \text{sin} \theta \text{cos} \theta`

Part (a) says that is exactly $\text{sin} 2 θ$

`\text{f} \left(\theta\right) = \text{sin} 2 \theta \textrm{ } \text{as required}`

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces both tangents by $\frac{\text{sin}θ}{\text{cos}θ}$.
> 
> **M1**: Combines the denominator into a single fraction over $\text{cos}^{2} θ$, or uses $1 + \text{tan}^{2} θ = \frac{1}{\text{cos}^{2}θ}$ directly. This mark depends on the first method mark.
> 
> **M1**: Simplifies the compound fraction to $2 \text{sin} θ \text{cos} θ$. This mark depends on the previous method mark.
> 
> **A1**: Uses part (a) to reach the given result with no errors.
> 
> The answer is given, so the working must be complete.
> 
> Quoting $1 + \text{tan}^{2} θ = \frac{1}{\text{cos}^{2}θ}$ as a known identity is equally acceptable and reaches the same point in one step fewer.
> 
> Working from $\text{sin} 2 θ$ back to the given expression is also equally acceptable, and carries the same four marks in reverse order.

> **[exam-tip]**
> When one side is in tangents and the other is not, convert the tangents.
> 
> - $\text{tan} θ = \frac{\text{sin}θ}{\text{cos}θ}$ is almost always the opening line of a proof like this
> - It leaves you with a fraction inside a fraction, which looks worse but simplifies quickly
> 
> A fraction over a fraction is handled by multiplying by the reciprocal.
> 
> - The denominator collapses to $\frac{1}{\text{cos}^{2}θ}$, so dividing by it multiplies the top by $\text{cos}^{2} θ$
> - That single step is what removes every fraction at once
> 
> $1 + \text{tan}^{2} θ$ is worth recognising on sight.
> 
> - It always equals $\frac{1}{\text{cos}^{2}θ}$, which comes from dividing $\text{sin}^{2} θ + \text{cos}^{2} θ \equiv 1$ through by $\text{cos}^{2} θ$
> - Spotting it saves two lines and it appears again, disguised, in part (c)
> 
> Finish by naming part (a).
> 
> - $2 \text{sin} θ \text{cos} θ$ is not the same as writing $\text{sin} 2 θ$, and the last mark is for making that link
> - One extra line costs nothing and secures the accuracy mark

### 10((c)) — 6 marks
Every angle in this equation is $x + \frac{π}{6}$, so both earlier results apply to it directly

Divide both sides by `1 + \text{tan}^{2} \left(x + \frac{\pi}{6}\right)` to expose the expression from part (b)

The left-hand side is then $\frac{5}{2}$ times `\text{f} \left(x + \frac{\pi}{6}\right)`, which part (b) says is a sine

`\frac{5}{2} \text{sin} \left(2 x + \frac{\pi}{3}\right) = 1 - 2 \text{cos}^{2} \left(x + \frac{\pi}{6}\right)`

**[M1]**

Part (a) gives $2 \text{cos}^{2} A - 1 = \text{cos} 2 A$, and the right-hand side here is the negative of that

`1 - 2 \text{cos}^{2} \left(x + \frac{\pi}{6}\right) = - \text{cos} \left(2 x + \frac{\pi}{3}\right)`

**[M1]**

Put the two sides together

`\frac{5}{2} \text{sin} \left(2 x + \frac{\pi}{3}\right) = - \text{cos} \left(2 x + \frac{\pi}{3}\right)`

Divide through by `\text{cos} \left(2 x + \frac{\pi}{3}\right)` to turn it into a tangent equation

`\text{tan} \left(2 x + \frac{\pi}{3}\right) = - \frac{2}{5}`

**[M1]**

Solve for the whole angle $2 x + \frac{π}{3}$, and adjust the range to match

Since $- \frac{π}{2} \leq x \leq \frac{π}{2}$, the angle runs from $- \frac{2π}{3}$ to $\frac{4π}{3}$

The calculator gives $- 0 . 38050$, which is already inside that range, and adding $π$ gives the second value

$2 x + \frac{π}{3} = - 0 . 38050 \dots , 2 . 76108 \dots$

**[M1]**

Subtract $\frac{π}{3}$ from each, then halve

$x = - 0 . 71385 \dots$

**[A1]**

`x = - 0 . 714 , 0 . 857 \textrm{ } \left(3 s . f .\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Divides by `1 + \text{tan}^{2} \left(x + \frac{\pi}{6}\right)` and uses part (b) to write the left-hand side as `\frac{5}{2} \text{sin} \left(2 x + \frac{\pi}{3}\right)`.
> 
> **M1**: Uses part (a) to write `1 - 2 \text{cos}^{2} \left(x + \frac{\pi}{6}\right)` as `- \text{cos} \left(2 x + \frac{\pi}{3}\right)`.
> 
> **M1**: Rearranges to `\text{tan} \left(2 x + \frac{\pi}{3}\right) = - \frac{2}{5}`.
> 
> **M1**: Finds at least one correct value for $2 x + \frac{π}{3}$, having adjusted the range.
> 
> **A1**: One correct value of $x$.
> 
> **A1**: Both values, and no extra values inside the range.
> 
> The question asks for radians to 3 significant figures, so degree answers earn nothing on the final two marks.
> 
> Working in degrees and converting at the very end is acceptable, provided the final answers are given in radians to the required accuracy.

> **[exam-tip]**
> An equation this ugly is a signal to look back at what you have already proved.
> 
> - Every angle is $x + \frac{π}{6}$, and both earlier parts are about exactly that shape
> - Dividing by $1 + \text{tan}^{2}$ is the move that makes part (b) appear, and it is the hardest step to spot
> 
> The angle doubles, so the constant doubles too.
> 
> - `2 \left(x + \frac{\pi}{6}\right) = 2 x + \frac{\pi}{3}`, and forgetting to double the $\frac{π}{6}$ is the commonest error here
> - Write the doubled angle out in full every time rather than carrying it in your head
> 
> Treat $2 x + \frac{π}{3}$ as a single quantity throughout.
> 
> - Solve for it, list all its values in the adjusted range, and only then unpick it to find $x$
> - Adjusting the range is a two-step calculation: double the ends, then add $\frac{π}{3}$ to each
> 
> Make sure your calculator is in radians.
> 
> - The answers are wanted in radians to 3 significant figures, so the whole calculation should stay in radians
> - $- 0 . 38050$ in radians and $- 21 . 8 \circ$ in degrees are the same angle, and mixing the two is easy to do

### 10((d)) — 4 marks
The first term is twice the function from part (b), so it can be replaced by a sine straight away

Part (b) gives $\frac{2\text{tan}θ}{1+\text{tan}^{2}θ} = \text{sin} 2 θ$, so doubling both sides handles the $4 \text{tan} θ$ version

Call the integral $I$

`I = \int_{0}^{\frac{\pi}{2}} \left(2 \text{sin} 2 \theta - \text{cos} 5 \theta + 2\right) \text{d} \theta`

**[M1]**

Integrate term by term, dividing by the multiple of $θ$ inside each function

`I = \left[- \text{cos} 2 \theta - \frac{\text{sin} 5 \theta}{5} + 2 \theta\right]_{0}^{\frac{\pi}{2}}`

**[M1]**

At the upper limit the angles are $π$ and $\frac{5π}{2}$

$- \text{cos} π - \frac{\text{sin}\frac{5π}{2}}{5} + π = 1 - \frac{1}{5} + π$

At the lower limit both trigonometric terms are straightforward and the $2 θ$ term vanishes

$- \text{cos} 0 - \frac{\text{sin}0}{5} + 0 = - 1$

Subtract the lower value from the upper one

$I = 1 - \frac{1}{5} + π + 1$

**[M1]**

$I = \frac{9}{5} + π$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses part (b) to replace $\frac{4\text{tan}θ}{1+\text{tan}^{2}θ}$ by $2 \text{sin} 2 θ$.
> 
> **M1**: Integrates to obtain terms of the form $p \text{cos} 2 θ + q \text{sin} 5 θ + r θ$.
> 
> **M1**: Substitutes both limits into your integrated expression and subtracts.
> 
> **A1**: $\frac{9}{5} + π$, or any exact equivalent.
> 
> The lower limit does not vanish, because $\text{cos} 0 = 1$. Dropping it gives $\frac{4}{5} + π$ and loses the final mark.
> 
> The question asks for the exact value, so $4 . 94$ earns nothing on the last mark.

> **[exam-tip]**
> There is no way to integrate the tangent expression as it stands.
> 
> - $\frac{4\text{tan}θ}{1+\text{tan}^{2}θ}$ has no standard integral, which is the clue that part (b) is meant to be used
> - Match the coefficient carefully: part (b) converts the version with a 2 on top, and this one has a 4
> 
> $\text{sin} \frac{5π}{2}$ is not zero, so evaluate it properly.
> 
> - $\frac{5π}{2}$ is $2 π + \frac{π}{2}$, so its sine is 1, the same as $\text{sin} \frac{π}{2}$
> - Assuming a large multiple of $π$ makes a sine vanish is a quick way to lose the answer
> 
> The constant term is easy to forget.
> 
> - The $+ 2$ integrates to $2 θ$, which contributes $π$ at the upper limit and nothing at the lower one
> - That $π$ is most of the final answer, so leaving it out is not a small error
> 
> Both limits matter here.
> 
> - $- \text{cos} 0 = - 1$, so the lower bracket contributes $+ 1$ once it is subtracted
> - Writing the lower bracket out in full, even when parts of it are zero, is the habit that catches this
