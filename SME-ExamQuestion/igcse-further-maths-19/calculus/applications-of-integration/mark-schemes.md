# Mark Schemes — Applications of Integration
**Calculus** · Edexcel IGCSE Further Pure Maths (4PM1)


## Q1 — medium — 5 marks · exam-questions

### 11((b)) — 5 marks
The shading in Figure 3 is in two separate pieces, and they lie on opposite sides of the $x$-axis

One piece runs from the $y$-axis across to `\left(b , 0\right)` and is above the axis

The other runs from `\left(b , 0\right)` to `\left(a , 0\right)` and is below the axis

A definite integral over a region below the axis comes out negative, so take the size of that one and add it, rather than adding the two integrals as they stand

With $b = 3$ and $a = \frac{9}{2}$, the limits are $0$ to $3$ for the first piece

`A_{1} = \int_{0}^{3} \left(2 x^{3} - 13 x^{2} + 12 x + 27\right) \textrm{ } \text{d} x`

**[M1]**

The second piece runs from $3$ to $\frac{9}{2}$, and its integral is made positive

`A_{2} = \left|\int_{3}^{\frac{9}{2}} \left(2 x^{3} - 13 x^{2} + 12 x + 27\right) \textrm{ } \text{d} x\right|`

**[M1]**

Integrate once, because the same integrated expression serves both pieces

`\int \left(2 x^{3} - 13 x^{2} + 12 x + 27\right) \textrm{ } \text{d} x = \frac{x^{4}}{2} - \frac{13 x^{3}}{3} + 6 x^{2} + 27 x`

**[A1]**

Substitute the limits of the first piece, upper value minus lower value

`A_{1} = \left(\frac{81}{2} - 117 + 54 + 81\right) - 0`

$A_{1} = \frac{117}{2}$

Now the second piece, where the upper limit is $\frac{9}{2}$

`A_{2} = \left|\left(\frac{6561}{32} - \frac{3159}{8} + \frac{243}{2} + \frac{243}{2}\right) - \frac{117}{2}\right|`

`A_{2} = \left|\frac{1701}{32} - \frac{1872}{32}\right|`

$A_{2} = \frac{171}{32}$

**[M1]**

Add the two areas, writing both over $32$

$\text{Area} = \frac{1872}{32} + \frac{171}{32}$

$\text{Area} = \frac{2043}{32}$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets up the integral of `\text{f}\left(x\right)` between $0$ and $3$ for the piece above the $x$-axis.
> 
> **M1**: Sets up the integral of `\text{f}\left(x\right)` between $3$ and $\frac{9}{2}$, treating the piece below the $x$-axis as a positive area.
> 
> **A1**: Correct integration, giving $\frac{x^{4}}{2} - \frac{13x^{3}}{3} + 6 x^{2} + 27 x$.
> 
> **M1**: Substitutes the limits into the integrated expression the correct way round, with at least one clear substitution in each integral.
> 
> **A1**: Total area $\frac{2043}{32}$.
> 
> The official scheme prints both integrals on a single line and awards a method mark for each, so setting one piece up correctly still earns a mark when the other is wrong. Neither integral has to be evaluated for those first two marks.
> 
> Taking the second integral as it stands and changing its sign at the end is equally acceptable, as is subtracting the smaller region from the larger provided the final total is positive.
> 
> Accept any exact equivalent of $\frac{2043}{32}$, such as $63 \frac{27}{32}$. A decimal answer is not exact and does not earn the final mark. An answer of $\frac{117}{2} - \frac{171}{32}$, which subtracts the second region instead of adding it, does not earn it either. This part has no marking notes in the official scheme, so its marks are printed a row at a time and the descriptors above follow those rows in order.

> **[exam-tip]**
> A definite integral gives a signed area rather than an area.
> 
> - Between $3$ and $\frac{9}{2}$ the curve is below the $x$-axis, so that integral is negative
> - Integrating straight from $0$ to $\frac{9}{2}$ in one go lets the two pieces partly cancel, which is the single commonest way to lose this question
> 
> Read the shading, not the crossing points, when you choose your limits.
> 
> - The shaded region starts at the $y$-axis, so the lower limit is $0$ and not $- 1$
> - `\left(- 1 , 0\right)` is marked on Figure 3 because it is a root of `\text{f}\left(x\right)`, not because it bounds the shading
> 
> The question asks for an exact value, so leave the answer as a fraction.
> 
> - $\frac{2043}{32}$ is exact and $63 . 8$ is not
> - As a check it is $63 . 84375$, which is a quick way to confirm you combined the two fractions correctly

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

## Q3 — medium — 13 marks · exam-questions

### 9((a)) — 3 marks
The target form `P \left(x + Q\right)^{2} + R` is a completed square, so complete the square on `\text{f} \left(x\right)`

Factorise $- 2$ out of the two terms containing $x$, leaving the 7 outside the bracket

`7 - 2 \left(x^{2} - 2 x\right)`

Complete the square inside the bracket by halving the coefficient of $x$

- Half of $- 2$ is $- 1$, so the bracket becomes `\left(x - 1\right)^{2}`
- Squaring that bracket introduces an extra $+ 1$, so subtract 1 inside to keep the value unchanged

`7 - 2 \left[\left(x - 1\right)^{2} - 1\right]`

**[M1]**

Multiply the $- 2$ through the square bracket, remembering that two negatives give a positive

`7 - 2 \left(x - 1\right)^{2} + 2`

Combine the two constants, and write the squared term first so it matches the printed form

`- 2 \left(x - 1\right)^{2} + 9`

**[A1]**

Compare this term by term with `P \left(x + Q\right)^{2} + R`

- The bracket is `\left(x - 1\right)^{2}`, which is `\left(x + Q\right)^{2}` with $Q = - 1$

$P=-2,Q=-1,R=9$

**[A1]**

> **[mark-scheme]**
> **M1**: A complete method to complete the square, reaching `7 - 2 \left[\left(x - 1\right)^{2} - 1\right]` or any equivalent arrangement.
> 
> **A1**: A correct completed square, `- 2 \left(x - 1\right)^{2} + 9` or an equivalent form.
> 
> **A1**: All three values, $P = - 2$, $Q = - 1$ and $R = 9$.
> 
> The values may be stated separately or left embedded in a correct completed square, and a correct completed square implies both accuracy marks. Where they are embedded correctly and then written out wrongly, the embedded version is the one used.
> 
> Expanding `P \left(x + Q\right)^{2} + R` and comparing coefficients is equally acceptable. Marked that way, the method mark is for a correct expansion together with a correct attempt to compare at least one coefficient, for example $P = - 2$ or $2 P Q = 4$, and the two accuracy marks are awarded exactly as above.

> **[exam-tip]**
> The printed form tells you what to factorise out before you start.
> 
> - In `P \left(x + Q\right)^{2} + R` the whole squared bracket is multiplied by $P$, so $P$ has to be the coefficient of $x^{2}$, which is $- 2$
> - Taking out $+ 2$ instead leaves $- x^{2}$ inside the bracket and the method breaks down
> 
> Only the two terms containing $x$ go inside the bracket.
> 
> - The constant 7 stays outside, and is combined at the end with whatever comes out of the bracket
> 
> $Q$ comes out negative here, which is easy to miss.
> 
> - The required form is `\left(x + Q\right)^{2}` and the answer is `\left(x - 1\right)^{2}`, so $Q = - 1$ rather than 1
> 
> Check your answer by expanding it back out.
> 
> - `- 2 \left(x - 1\right)^{2} + 9` expands to $- 2 x^{2} + 4 x - 2 + 9$, which is $7 + 4 x - 2 x^{2}$

### 9((b)) — 2 marks
**(i)**

Part (a) writes `\text{f} \left(x\right)` as `- 2 \left(x - 1\right)^{2} + 9`

A square is never negative, so the term `- 2 \left(x - 1\right)^{2}` is never positive

That makes `\text{f} \left(x\right)` largest when the squared term is zero, and all that is left is the constant

**Final answer:** **The maximum value of **`\text{f} \left(x\right)`** is 9**

**[B1]**

**(ii)**

The squared term is zero exactly when the bracket inside it is zero

$x - 1 = 0$

$x = 1$

**[B1]**

> **[mark-scheme]**
> **B1**: A maximum value of 9.
> 
> **B1**: The maximum occurs at $x = 1$.
> 
> Both marks follow through from your own completed square in part (a), so a maximum value equal to your $R$ and an $x$ value equal to $- Q$ earn them.
> 
> The question says "hence", so the values are expected to come from part (a). Differentiating `\text{f} \left(x\right)` and solving `\text{f} ' \left(x\right) = 0` reaches the same two answers and is accepted, provided both are correct.
> 
> In part (ii) accept $x = 1$ written on its own. A pair of coordinates `\left(1 , 9\right)` is accepted for the two marks together, provided each value is clearly matched to the right sub part.

> **[exam-tip]**
> Completed square form hands you the maximum with no calculus at all.
> 
> - The only part of `- 2 \left(x - 1\right)^{2} + 9` that changes is the squared term, and the closest it can get to zero is zero itself
> - With a minus sign in front of it, that zero gives the largest possible value
> 
> Read carefully which of the two things each sub part wants.
> 
> - "Maximum value" means the value of `\text{f} \left(x\right)`, which is 9
> - The value of $x$ where the maximum happens is 1, and that is what part (ii) asks for
> 
> The sign of the $x$ value is the usual trap.
> 
> - The bracket is `\left(x - 1\right)^{2}`, so it vanishes at $x = 1$, not at $x = - 1$
> 
> "Write down" tells you no working is required.
> 
> - One mark each, and both answers can be read straight off part (a), so this is the fastest pair of marks in the question

### 9((c)) — 3 marks
The curve and the line meet where their $y$ values are equal, so set the two expressions equal

$7 + 4 x - 2 x^{2} = 4 - x$

**[M1]**

Collect every term on one side, choosing the side that leaves the $x^{2}$ term positive

- Adding $2 x^{2}$ and $x$ to both sides and then subtracting 7 moves everything to the right

$0 = 2 x^{2} - 5 x - 3$

Factorise the quadratic

- The two $x$ terms must multiply to give $2 x^{2}$, so one bracket starts with $2 x$ and the other with $x$
- The two constants must multiply to give $- 3$, and choosing $+ 1$ and $- 3$ gives a middle term of $x - 6 x$, which is $- 5 x$

`\left(2 x + 1\right) \left(x - 3\right) = 0`

**[M1]**

Set each bracket equal to zero in turn

$x=-\frac{1}{2},x=3$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets the equation of the curve equal to the equation of the line, eliminating $y$.
> 
> **M1**: Rearranges to a three term quadratic and makes a complete attempt to solve it.
> 
> **A1**: Both values, $x = - \frac{1}{2}$ and $x = 3$.
> 
> The quadratic may be written either way round, so $- 2 x^{2} + 5 x + 3 = 0$ is equally acceptable and is marked identically.
> 
> Any complete method of solution earns the second method mark: factorising, the quadratic formula, or completing the square. A pair of correct values written down with no method shown earns all three marks.
> 
> The question asks only for the $x$ coordinates, so no $y$ values are needed. Giving them as well is not penalised.

> **[exam-tip]**
> Two graphs meet where they give the same $y$ for the same $x$, so equate the right hand sides.
> 
> - That eliminates $y$ in one step and leaves a single equation in $x$
> 
> Rearrange so that the $x^{2}$ coefficient comes out positive.
> 
> - $2 x^{2} - 5 x - 3 = 0$ is far easier to factorise than $- 2 x^{2} + 5 x + 3 = 0$
> - Moving everything to the other side is the same as multiplying through by $- 1$
> 
> A leading coefficient of 2 means the constants are not simply a factor pair of the constant term.
> 
> - Test each arrangement by expanding the middle term, since $+ 1$ with $- 3$ gives $- 5 x$ but $- 1$ with $+ 3$ gives $+ 5 x$
> 
> These two values are the limits of integration in part (d).
> 
> - An error here carries through, so check them by substituting back into both equations

### 9((d)) — 5 marks
Rotating about the $x$-axis, the volume swept out by a graph is `\pi \int y^{2} \text{d} x`

The region lies between the curve and the line, so subtract the volume the line generates from the volume the curve generates

- The curve is above the line all the way between the two intersections, so the curve gives the outer surface
- The limits are the two $x$ coordinates found in part (c)

`V = \pi \int_{- \frac{1}{2}}^{3} \left(7 + 4 x - 2 x^{2}\right)^{2} \text{d} x - \pi \int_{- \frac{1}{2}}^{3} \left(4 - x\right)^{2} \text{d} x`

**[M1]**

Expand the curve's square, treating it as `\left(7 + 4 x - 2 x^{2}\right) \left(7 + 4 x - 2 x^{2}\right)`

- Squaring each term in turn gives 49, $16 x^{2}$ and $4 x^{4}$
- Each pair of different terms appears twice, giving $56 x$, $- 28 x^{2}$ and $- 16 x^{3}$

`\left(7 + 4 x - 2 x^{2}\right)^{2} = 4 x^{4} - 16 x^{3} - 12 x^{2} + 56 x + 49`

Expand the line's square as well

`\left(4 - x\right)^{2} = x^{2} - 8 x + 16`

**[M1]**

Combine into a single integral and subtract term by term

`V = \pi \int_{- \frac{1}{2}}^{3} \left(4 x^{4} - 16 x^{3} - 13 x^{2} + 64 x + 33\right) \text{d} x`

**[A1]**

Integrate each term, raising the power by one and dividing by the new power

`V = \pi \left[\frac{4 x^{5}}{5} - 4 x^{4} - \frac{13 x^{3}}{3} + 32 x^{2} + 33 x\right]_{- \frac{1}{2}}^{3}`

**[M1]**

Substitute the upper limit $x = 3$

`\frac{4 \left(243\right)}{5} - 4 \left(81\right) - \frac{13 \left(27\right)}{3} + 32 \left(9\right) + 33 \left(3\right) = \frac{702}{5}`

Substitute the lower limit $x = - \frac{1}{2}$, taking care with the signs of the odd powers

$- \frac{1}{40} - \frac{1}{4} + \frac{13}{24} + 8 - \frac{33}{2} = - \frac{247}{30}$

Subtract the lower value from the upper value

`V = \pi \left(\frac{702}{5} + \frac{247}{30}\right)`

$V = \frac{4459π}{30}$

Evaluate this and round to 3 significant figures

$V = 466 . 945 \dots$

`V equals 467 space open parentheses 3 space straight s. straight f. close parentheses`

**[A1]**

> **[mark-scheme]**
> **M1**: Sets up the difference of the two volumes of revolution, `\pi \int \left(y_{C}^{2} - y_{l}^{2}\right) \text{d} x`, using your limits from part (c).
> 
> **M1**: Attempts to expand both squares, with at least one of them fully correct.
> 
> **A1**: A correct integrand, $4 x^{4} - 16 x^{3} - 13 x^{2} + 64 x + 33$ or any equivalent.
> 
> **M1**: Integrates your expression correctly, with every power raised by one and divided by the new power. Neither $π$ nor the limits need appear for this mark.
> 
> **A1**: Answers which round to 467, the unrounded value being $466 . 945$.
> 
> Integrating the two volumes separately and subtracting the results at the end is equally acceptable and is marked in exactly the same way.
> 
> The factor of $π$ may be left out of the working and reinstated at the end. The limits follow through from part (c), but the integrand itself must be correct for the accuracy mark.
> 
> A negative answer that is simply made positive at the end does not earn the final mark.

> **[exam-tip]**
> For a region between two graphs, the formula subtracts the squares, not the graphs.
> 
> - `V = \pi \int \left(y_{\text{outer}}^{2} - y_{\text{inner}}^{2}\right) \text{d} x`, so square each boundary first and subtract afterwards
> - Subtracting first and squaring the result is a common error and scores almost nothing
> 
> Squaring a three term expression needs six products, not three.
> 
> - The three squares are 49, $16 x^{2}$ and $4 x^{4}$
> - The three cross terms each appear twice, which is where $56 x$, $- 28 x^{2}$ and $- 16 x^{3}$ come from
> 
> The limits have already been found for you.
> 
> - They are the intersections from part (c), so there is no new equation to solve here
> 
> Keep everything in fractions until the very last line.
> 
> - The exact volume is $\frac{4459π}{30}$, so round only once, right at the end
> - Rounding the two limit substitutions first is enough to lose the final significant figure

## Q4 — medium — 10 marks · exam-questions

### 6((a)) — 3 marks
The two curves meet where they give the same $y$ for the same $x$, so set the two expressions equal

$2 x^{2} = \frac{1}{4x}$

Multiply both sides by $4 x$ to clear the fraction

$8 x^{3} = 1$

$x^{3} = \frac{1}{8}$

**[M1]**

Take the cube root of both sides

$x = \frac{1}{2}$

**[A1]**

Substitute back to find $y$, using $y = 2 x^{2}$ because it is the easier of the two

`y = 2 \left(\frac{1}{2}\right)^{2}`

$y = \frac{1}{2}$

`A equals open parentheses 1 half comma space 1 half close parentheses`

**[B1]**

> **[mark-scheme]**
> **M1**: Sets the two equations equal and attempts to find a value for $x$. The least that is accepted is reaching $x^{3} = \frac{1}{8}$.
> 
> **A1**: $x = \frac{1}{2}$.
> 
> **B1**: The correct $y$ coordinate, $y = \frac{1}{2}$.
> 
> Substituting into either curve is equally acceptable, since $\frac{1}{4\times\frac{1}{2}}$ also gives $\frac{1}{2}$.
> 
> The stem restricts both curves to positive $x$, so only the one intersection exists and no other roots need to be discussed.

> **[exam-tip]**
> Clear the fraction before doing anything else.
> 
> - Multiplying $2 x^{2} = \frac{1}{4x}$ by $4 x$ turns it straight into $8 x^{3} = 1$
> - Trying to square or rearrange with the fraction still there makes the algebra much harder than it needs to be
> 
> A cubic in this form has only one useful root.
> 
> - $x^{3} = \frac{1}{8}$ has a single real solution, $x = \frac{1}{2}$, so there is nothing to reject
> - Figure 3 confirms it, since the two curves cross only once
> 
> Pick the easier equation when you substitute back.
> 
> - $y = 2 x^{2}$ needs one squaring, whereas $y = \frac{1}{4x}$ needs the reciprocal of a fraction
> - Substituting into the other one is a quick check that your $x$ is right
> 
> The $y$ coordinate is worth its own mark, so do not stop at $x$.
> 
> - The question asks for coordinates, so both numbers are needed

### 6((b)) — 7 marks
The rotation is about the $y$-axis, so the volume formula uses $x^{2}$ and integrates with respect to $y$

`V = \pi \int x^{2} \text{d} y`

$R$ lies between the two curves, so subtract the inner volume from the outer one

- Reading across $R$ at any height, the curve $S$ gives the outer boundary and the curve $C$ gives the inner one

Rearrange each equation to give $x^{2}$ in terms of $y$, starting with $S$

$x^{2} = \frac{y}{2}$

**[B1]**

Now $C$, where $y = \frac{1}{4x}$ rearranges to $x = \frac{1}{4y}$

$x^{2} = \frac{1}{16y^{2}}$

**[B1]**

The limits are the $y$ values at the bottom and the top of $R$

- The lowest point of $R$ is $A$, where $y = \frac{1}{2}$ from part (a)
- The top edge is the straight line $y = 4$

`V = \pi \int_{\frac{1}{2}}^{4} \frac{y}{2} \text{d} y - \pi \int_{\frac{1}{2}}^{4} \frac{1}{16 y^{2}} \text{d} y`

**[M1]**

Integrate each one, writing the second as $\frac{1}{16} y^{-2}$ so the power rule can be applied

`V = \pi \left[\frac{y^{2}}{4}\right]_{\frac{1}{2}}^{4} - \pi \left[- \frac{1}{16 y}\right]_{\frac{1}{2}}^{4}`

**[M1] [A1]**

Substitute the limits into the first bracket, upper value first

`\frac{4^{2}}{4} - \frac{\left(\frac{1}{2}\right)^{2}}{4} = \frac{63}{16}`

Now do the same with the second bracket

`- \frac{1}{16 \left(4\right)} + \frac{1}{16 \left(\frac{1}{2}\right)} = \frac{7}{64}`

**[M1]**

Put the two together, keeping the minus sign that sits in front of the second integral

`V = \pi \left(\frac{63}{16} - \frac{7}{64}\right)`

Write both fractions over 64

`V = \pi \left(\frac{252}{64} - \frac{7}{64}\right)`

$V = \frac{245π}{64}$

**[A1]**

> **[mark-scheme]**
> **B1**: Rearranges the equation of $S$ to $x^{2} = \frac{y}{2}$, either stated or embedded in later working.
> 
> **B1**: Rearranges the equation of $C$ to $x^{2} = \frac{1}{16y^{2}}$, or an equivalent such as $\frac{y^{-2}}{16}$ or `\left(\frac{1}{4 y}\right)^{2}`, again stated or embedded.
> 
> **M1**: A correct expression for the volume with the correct limits and with $π$ present. The lower limit follows through from your $y$ coordinate in part (a). The two expressions may be written either way round, and $π$ may be introduced at the end instead. Poor notation is ignored as long as the intention is clear, so a missing $\text{d} y$ is not penalised.
> 
> **M1**: An attempt to integrate at least one of the two expressions. Limits and $π$ are ignored for this mark.
> 
> **A1**: A fully correct integrated expression for the volume.
> 
> **M1**: Substitutes the limits into your integrated expression the correct way round. This must be seen where either the integration or the limits are incorrect. Where everything is correct, the correct volume seen in exact or decimal form earns it on its own, and partly processed forms are accepted provided all four separate calculations are visible.
> 
> **A1**: $\frac{245π}{64}$.
> 
> The decimal equivalent is $12 . 0264 \dots$, but the question asks for the exact volume, so the fraction is required.
> 
> A solution that rotates about the $x$-axis instead can still earn some credit, but it caps at four of the seven marks: neither of the two opening marks and neither accuracy mark is available, and only the three method marks can be given, for a correct expression using the $x$ limits $\frac{1}{16}$ and $\sqrt{2}$, for an attempt to integrate one of the two expressions, and for substituting the values correctly.

> **[exam-tip]**
> Rotating about the $y$-axis swaps the roles of the two variables.
> 
> - The formula becomes `V = \pi \int x^{2} \text{d} y`, so every equation has to be rearranged to give $x^{2}$ in terms of $y$
> - The limits become $y$ values, not $x$ values, which is why part (a) matters here
> 
> Those two rearrangements carry a mark each before any integration happens.
> 
> - $y = 2 x^{2}$ gives $x^{2} = \frac{y}{2}$ in one step
> - $y = \frac{1}{4x}$ has to be inverted first to $x = \frac{1}{4y}$, and only then squared
> 
> Work out which curve is on the outside.
> 
> - At any height in $R$, the curve $S$ is further from the $y$-axis than the curve $C$, so $S$ gives the outer radius
> - Getting them the wrong way round produces a negative volume
> 
> Watch the sign when the second integral is subtracted.
> 
> - `\int \frac{1}{16} y^{- 2} \text{d} y` integrates to $- \frac{1}{16y}$, and that minus sign then meets the minus in front of the integral
> - Two minus signs make the second contribution positive, which is where $\frac{7}{64}$ comes from
> 
> "Exact volume" rules out a decimal answer.
> 
> - $12 . 0$ scores nothing for the final mark, however many figures it is given to

## Q5 — medium — 10 marks · exam-questions

### 9() — 10 marks
The region $R$ is bounded by three different things, so you need three $x$-values before you can integrate

Those are where the curve meets the line, and where each of them meets the $x$-axis

Start with the curve and the line, and rearrange each to give $x$

$x = y^{2} + 1$

$x = 4 - 2 y$

Set the two expressions for $x$ equal

$4 - 2 y = y^{2} + 1$

**[M1]**

$y^{2} + 2 y - 3 = 0$

**[A1]**

Two numbers multiplying to $- 3$ and adding to $2$ are $3$ and $- 1$

`\left(y + 3\right)\left(y - 1\right) = 0`

**[M1]**

$y = - 3  \text{or}  1$

Figure 3 shows $R$ above the $x$-axis, so take $y = 1$ and substitute into the line

`x = 4 - 2 \left(1\right)`

$x = 2$

**[A1]**

Now find where each boundary crosses the $x$-axis, which is where $y = 0$

The curve gives the left-hand end of the region

$x = 0^{2} + 1$

$x = 1$

The line gives the right-hand end

`x = 4 - 2 \left(0\right)`

$x = 4$

**[B1] [B1]**

So the solid is made of two pieces: the curve sweeps out the part from $x = 1$ to $x = 2$, and the line sweeps out the part from $x = 2$ to $x = 4$

Rotating about the $x$-axis uses `V = \pi \int y^{2} \textrm{ } \text{d} x`, and the curve is already given as $y^{2}$

For the line, make $y$ the subject and square it

$y = 2 - \frac{x}{2}$

$y^{2} = 4 - 2 x + \frac{x^{2}}{4}$

Add the two volumes, each with its own limits

`V = \pi \int_{1}^{2} \left(x - 1\right) \textrm{ } \text{d} x + \pi \int_{2}^{4} \left(4 - 2 x + \frac{x^{2}}{4}\right) \textrm{ } \text{d} x`

**[M1]**

Integrate each bracket term by term

`V = \pi \left[\frac{x^{2}}{2} - x\right]_{1}^{2} + \pi \left[4 x - x^{2} + \frac{x^{3}}{12}\right]_{2}^{4}`

**[M1]**

Substitute the limits into each bracket, upper value minus lower value

`V = \pi \left[\left(2 - 2\right) - \left(\frac{1}{2} - 1\right)\right] + \pi \left[\left(16 - 16 + \frac{16}{3}\right) - \left(8 - 4 + \frac{2}{3}\right)\right]`

**[M1]**

$V = \frac{1}{2} π + \frac{2}{3} π$

$V = \frac{7}{6} π$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets the equation of the curve equal to the equation of the line and rearranges towards a quadratic equal to zero, in either $x$ or $y$. The quadratic does not have to be correct for this mark.
> 
> **A1**: The correct three-term quadratic, $y^{2} + 2 y - 3 = 0$, or $x^{2} - 12 x + 20 = 0$ if you work in $x$.
> 
> **M1**: Solves that quadratic by an acceptable method.
> 
> **A1**: $x = 2$ where the curve meets the line.
> 
> **B1**: Either $x = 1$ or $x = 4$ for one of the two crossings of the $x$-axis.
> 
> **B1**: Both $x = 1$ and $x = 4$.
> 
> **M1**: Correct expression for the two volumes of revolution, `\pi \int_{1}^{2} \left(x - 1\right) \textrm{ } \text{d} x + \pi \int_{2}^{4} \left(2 - \frac{x}{2}\right)^{2} \textrm{ } \text{d} x`, using your own limits.
> 
> **M1**: Acceptable attempt to integrate at least two terms, with no power of $x$ decreasing. Neither $π$ nor the limits need to be present for this mark.
> 
> **M1**: Substitutes the limits into the changed expressions, with each limit substituted correctly at least once.
> 
> **A1**: $V = \frac{7}{6} π$.
> 
> The two B marks are staged, exactly as the official scheme has them: the first is earned as soon as either one of the two crossings is correct, and the second only once both are. That is why a single box carries both codes in the working above, rather than one box on each line.
> 
> The third method mark depends on both of the earlier method marks and on your having attempted to find where the curve and the line cross the $x$-axis. Your own values may be used as the limits provided that attempt is clear.
> 
> The official scheme replaces the second integral with the cone `\frac{1}{3} \pi \times 1^{2} \times \left(4 - 2\right)` and marks it identically. The mark for integrating is not dependent, so it is still available where an incorrect cone formula has been written down, or where the two expressions have been combined incorrectly. Accept any exact equivalent of $\frac{7}{6} π$.

> **[exam-tip]**
> A region bounded by three different things needs three $x$-values before any integration can start.
> 
> - The curve and the line meet at $x = 2$, and they cross the $x$-axis at $x = 1$ and at $x = 4$
> - Those give the two intervals, $1$ to $2$ under the curve and $2$ to $4$ under the line
> 
> Solving in $y$ is quicker here than solving in $x$.
> 
> - The curve is already $x = y^{2} + 1$ and the line rearranges to $x = 4 - 2 y$, so no squaring is needed
> - Working in $x$ also earns full marks, but it gives $x^{2} - 12 x + 20 = 0$ and the root $x = 10$ then has to be rejected against the diagram
> 
> The second solid is a cone, which gives you a free check on half of the answer.
> 
> - Its radius is the value of $y$ at $x = 2$, which is $1$, and its height is $4 - 2 = 2$
> - That gives $\frac{1}{3} π \times 1^{2} \times 2 = \frac{2}{3} π$, matching the second integral
> 
> Only the sphere and the curved surface of a cone appear on the formulae sheet issued with the exam.
> 
> - The volume of a cone is on neither that sheet nor the list of formulae to learn, so use it as a check rather than as your method here
> - The question asks for algebraic integration in any case, which is what the working above does

## Q6 — medium — 14 marks · exam-questions

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

## Q7 — medium — 14 marks · exam-questions

### 11((a)) — 4 marks
The target form `A \left(x + B\right)^{2} + C` is a completed square, so complete the square on `\text{f} \left(x\right)`

Factorise $- 1$ out of the two terms containing $x$, leaving the 10 outside the bracket

`- \left(x^{2} - 6 x\right) + 10`

The number in front of the squared bracket is $A$, so it can be read off straight away

$A = - 1$

**[B1]**

Complete the square inside the bracket by halving the coefficient of $x$

- Half of $- 6$ is $- 3$, so the bracket becomes `\left(x - 3\right)^{2}`
- Squaring that bracket introduces an extra $+ 9$, so subtract 9 inside to keep the value unchanged

`- \left[\left(x - 3\right)^{2} - 9\right] + 10`

**[M1]**

Multiply the $- 1$ through the square bracket, remembering that two negatives give a positive

`- \left(x - 3\right)^{2} + 9 + 10`

Combine the two constants

`- \left(x - 3\right)^{2} + 19`

**[A1]**

Compare this term by term with `A \left(x + B\right)^{2} + C`

- The bracket is `\left(x - 3\right)^{2}`, which is `\left(x + B\right)^{2}` with $B = - 3$

$A=-1,B=-3,C=19$

**[A1]**

> **[mark-scheme]**
> **B1**: Factorises $- 1$ out of the terms in $x$ and finds $A = - 1$.
> 
> **M1**: An attempt to complete the square on the resulting bracket.
> 
> **A1**: Either $B = - 3$ or $C = 19$.
> 
> **A1**: Both $B = - 3$ and $C = 19$.
> 
> All of the values are accepted embedded in a correct completed square rather than stated separately.
> 
> Correct values written down with no working at all earn full marks in this part.
> 
> Expanding `A \left(x + B\right)^{2} + C` and comparing coefficients is equally acceptable. Marked that way, the first mark is for $A = - 1$ from comparing the $x^{2}$ terms, the method mark is for a correct expansion together with a correct attempt to compare a further coefficient, such as $2 A B = 6$, and the two accuracy marks are awarded exactly as above.

> **[exam-tip]**
> The first mark is for a single step, so take it before anything else.
> 
> - $10 + 6 x - x^{2}$ has a coefficient of $- 1$ on the $x^{2}$ term, so $A = - 1$
> - Writing `- \left(x^{2} - 6 x\right) + 10` shows the factorising and banks that mark
> 
> Signs are where this question is won or lost.
> 
> - Taking out $- 1$ flips both terms inside the bracket, so $6 x$ becomes $- 6 x$
> - Multiplying the $- 1$ back through turns the $- 9$ into $+ 9$, which is what makes $C = 19$ rather than 1
> 
> $B$ is negative even though the form shows a plus sign.
> 
> - `\left(x + B\right)^{2}` matched against `\left(x - 3\right)^{2}` gives $B = - 3$
> 
> Check by expanding your answer back out.
> 
> - `- \left(x - 3\right)^{2} + 19` expands to $- x^{2} + 6 x - 9 + 19$, which is $10 + 6 x - x^{2}$

### 11((b)) — 2 marks
**(i)**

Part (a) writes `\text{f} \left(x\right)` as `- \left(x - 3\right)^{2} + 19`

A square is never negative, so the term `- \left(x - 3\right)^{2}` is never positive

That makes `\text{f} \left(x\right)` greatest when the squared term is zero, which happens when the bracket is zero

$x - 3 = 0$

$x = 3$

**[B1]**

**(ii)**

At that value of $x$ the squared term contributes nothing, so all that is left is the constant

**Final answer:** **The greatest value of **`\text{f} \left(x\right)`** is 19**

**[B1]**

> **[mark-scheme]**
> **B1**: $x = 3$.
> 
> **B1**: A greatest value of 19.
> 
> Both marks follow through from your own completed square in part (a), so an $x$ value equal to $- B$ and a greatest value equal to your $C$ earn them.
> 
> Correct values are accepted even where they are not obviously derived from the working shown, so a pair of answers written straight down earns both marks.
> 
> Differentiating `\text{f} \left(x\right)` and solving `\text{f} ' \left(x\right) = 0` is an equally acceptable route to the value of $x$ in part (i).
> 
> In part (ii) accept $y = 19$ as well as `\text{f} \left(x\right) = 19`.

> **[exam-tip]**
> Completed square form gives both answers with no calculus at all.
> 
> - The bracket squared is the only part that changes, and the smallest it can be is zero
> - With a minus sign in front of it, that zero produces the greatest value
> 
> Check which sub part wants which answer.
> 
> - Part (i) asks for the value of $x$, which is 3
> - Part (ii) asks for the value of `\text{f} \left(x\right)`, which is 19
> - The two are asked in that order here, and swapping them costs both marks
> 
> The sign of $x$ is the trap.
> 
> - The bracket is `\left(x - 3\right)^{2}`, so it vanishes at $x = 3$, not at $x = - 3$
> 
> These marks follow through, so an error in part (a) is not fatal.
> 
> - Answers consistent with your own $B$ and $C$ still earn both marks, so always write something down

### 11((c)) — 3 marks
The two curves meet where they give the same $y$ for the same $x$, so set the two expressions equal

$x^{2} - x + 13 = 10 + 6 x - x^{2}$

**[M1]**

Collect every term on the left, so that the $x^{2}$ term stays positive

- Adding $x^{2}$, subtracting $6 x$ and subtracting 10 moves everything across

$2 x^{2} - 7 x + 3 = 0$

Factorise the quadratic

- The two $x$ terms must multiply to give $2 x^{2}$, so one bracket starts with $2 x$ and the other with $x$
- The two constants must multiply to give $+ 3$, and choosing $- 1$ and $- 3$ gives a middle term of $- 6 x - x$, which is $- 7 x$

`\left(2 x - 1\right) \left(x - 3\right) = 0`

**[M1]**

Set each bracket equal to zero in turn

$x=\frac{1}{2},x=3$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets the equations of the two curves equal to each other, eliminating $y$.
> 
> **M1**: Rearranges to a three term quadratic and makes a complete attempt to solve it.
> 
> **A1**: Both values, $x = \frac{1}{2}$ and $x = 3$.
> 
> The quadratic may be written either way round, so $- 2 x^{2} + 7 x - 3 = 0$ is equally acceptable and is marked identically.
> 
> Any complete method of solution earns the second method mark: factorising, the quadratic formula, or completing the square.
> 
> The question asks only for the $x$ coordinates, so no $y$ values are required. Giving them as well is not penalised.

> **[exam-tip]**
> Equating the two right hand sides removes $y$ in a single step.
> 
> - Both equations are already written as $y =$ something, so there is nothing to rearrange first
> 
> Move everything to whichever side keeps the $x^{2}$ coefficient positive.
> 
> - Here that is the left, giving $2 x^{2} - 7 x + 3 = 0$ rather than $- 2 x^{2} + 7 x - 3 = 0$
> - The two $- x^{2}$ and $+ x^{2}$ terms combine rather than cancelling, which is easy to miss
> 
> With a leading coefficient of 2, test the middle term before committing.
> 
> - $- 1$ with $- 3$ gives $- 6 x - x$, which is $- 7 x$, whereas $- 3$ with $- 1$ gives $- 2 x - 3 x$, which is $- 5 x$
> 
> These two values become the limits of integration in part (d).
> 
> - Check them by substituting back into both equations, since an error here carries all the way through

### 11((d)) — 5 marks
The area between two curves is the integral of the upper curve minus the lower one

Decide which is which by testing a value between the two intersections, say $x = 1$

- $C$ gives $10 + 6 - 1 = 15$ and $S$ gives $1 - 1 + 13 = 13$, so $C$ is on top

The limits are the two $x$ coordinates found in part (c)

`A = \int_{\frac{1}{2}}^{3} \left(10 + 6 x - x^{2}\right) \text{d} x - \int_{\frac{1}{2}}^{3} \left(x^{2} - x + 13\right) \text{d} x`

**[M1]**

Combine into a single integral and subtract term by term

- The two $x^{2}$ terms give $- 2 x^{2}$, the two $x$ terms give $7 x$, and the constants give $- 3$

`A = \int_{\frac{1}{2}}^{3} \left(- 2 x^{2} + 7 x - 3\right) \text{d} x`

Integrate each term, raising the power by one and dividing by the new power

`A = \left[- \frac{2 x^{3}}{3} + \frac{7 x^{2}}{2} - 3 x\right]_{\frac{1}{2}}^{3}`

**[M1] [A1]**

Substitute the upper limit $x = 3$

`- \frac{2 \left(27\right)}{3} + \frac{7 \left(9\right)}{2} - 3 \left(3\right) = \frac{9}{2}`

Now the lower limit $x = \frac{1}{2}$

`- \frac{2 \left(\frac{1}{8}\right)}{3} + \frac{7 \left(\frac{1}{4}\right)}{2} - 3 \left(\frac{1}{2}\right) = - \frac{17}{24}`

**[M1]**

Subtract the lower value from the upper value

$A = \frac{9}{2} + \frac{17}{24}$

Write both fractions over 24

$A = \frac{108}{24} + \frac{17}{24}$

$A = \frac{125}{24}$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets up the difference of the two integrals with the correct limits, in either the two integral form or as a single integral of the difference. The limits follow through from part (c).
> 
> **M1**: Integrates your expression, with at least one term correctly integrated.
> 
> **A1**: A fully correct integrated expression.
> 
> **M1**: Substitutes both limits into your integrated expression and subtracts them the correct way round.
> 
> **A1**: $\frac{125}{24}$, or any equivalent exact value.
> 
> Integrating the two curves separately and subtracting the results at the end is equally acceptable and is marked in exactly the same way.
> 
> The question asks for the exact area, so a decimal answer such as $5 . 21$ does not earn the final mark.
> 
> Subtracting the curves the wrong way round gives $- \frac{125}{24}$. Simply changing the sign at the end does not recover the final mark.

> **[exam-tip]**
> Work out which curve is on top before you write the integral down.
> 
> - Substitute any value between the limits into both equations and compare, which here gives 15 against 13 at $x = 1$
> - Getting the order wrong turns the whole answer negative
> 
> Subtract first, then integrate.
> 
> - `\left(10 + 6 x - x^{2}\right) - \left(x^{2} - x + 13\right)` simplifies to $- 2 x^{2} + 7 x - 3$, which is one short integral instead of two long ones
> - Watch the bracket, because subtracting $- x$ gives $+ x$ and subtracting 13 from 10 gives $- 3$
> 
> The limits are already done for you.
> 
> - They are the intersections from part (c), so there is no new equation to solve here
> 
> Keep everything in fractions, since the question asks for the exact area.
> 
> - $\frac{9}{2}$ and $- \frac{17}{24}$ combine cleanly over a denominator of 24
> - Subtracting a negative lower value is what makes the two contributions add rather than cancel

## Q8 — medium — 8 marks · exam-questions

### 4((a)) — 4 marks
**(i)**

$A$ and $B$ are where the curve and the line meet, so their equations are equal there

First rearrange $2 y - x - 4 = 0$ to make $y$ the subject

$y = \frac{x+4}{2}$

Now set this equal to the equation of $S$

$\frac{x^{2}}{4} + 2 = \frac{x+4}{2}$

**[M1]**

Multiply every term by $4$ to clear the fractions

$x^{2} + 8 = 2 x + 8$

$x^{2} - 2 x = 0$

Factorise rather than using the quadratic formula, since there is no constant term

`x \left(x - 2\right) = 0`

$x = 0  \text{or}  2$

**[M1]**

From the diagram, $A$ is the intersection on the $y$-axis, so it is the one with $x = 0$

Substitute $x = 0$ into either equation

$y = \frac{0^{2}}{4} + 2$

$y = 2$

`A = \left(0 , 2\right) \textrm{ } \text{as required}`

**[A1]**

**(ii)**

$B$ is the other intersection, so use $x = 2$

$y = \frac{2+4}{2}$

$y = 3$

`B = \left(2 , 3\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correctly equates the equation of $S$ with the equation of $l$.
> 
> **M1**: Forms a quadratic and makes an acceptable attempt to solve it.
> 
> **A1**: Correct substitution of $x = 0$ to show that $A$ is `\left(0 , 2\right)`.
> 
> **A1**: Coordinates of $B$ as `\left(2 , 3\right)`.
> 
> For the second mark your quadratic must be correct. Since it has two terms only, the zero solution does not have to be written down, because it is obvious from the given diagram.
> 
> The first accuracy mark needs completely correct working, because the coordinates of $A$ are given in the question.
> 
> Coordinates may be written without brackets. If you do not label your answers (i) and (ii), the marks are still available provided the coordinates appear in the correct order, or are labelled $A$ and $B$. Where that is ambiguous and both are correct, only one accuracy mark is given, and where it is ambiguous and only one is correct, neither is.

> **[exam-tip]**
> A quadratic with no constant term factorises immediately, so reach for the formula only when you have to.
> 
> - $x^{2} - 2 x = 0$ gives `x \left(x - 2\right) = 0` in one step
> - Never divide through by $x$, as that throws away the solution $x = 0$, which here is the whole of part (i)
> 
> Use the diagram to decide which root belongs to which point. $A$ is drawn on the $y$-axis, so it must be the root $x = 0$.
> 
> Substitute back into the simpler of the two equations. The line $y = \frac{x+4}{2}$ is quicker than the curve, and either will do.

### 4((b)) — 4 marks
The rotation is about the $y$-axis, so integrate with respect to $y$ and use `V = \pi \int x^{2} \textrm{ } \text{d} y`

That means you need $x^{2}$ in terms of $y$ for each of the two boundaries

Rearrange the curve $y = \frac{x^{2}}{4} + 2$

$x^{2} = 4 y - 8$

Rearrange the line $2 y - x - 4 = 0$

$x = 2 y - 4$

$x^{2} = 4 y^{2} - 16 y + 16$

The limits are the $y$-coordinates of $A$ and $B$, so $y$ runs from $2$ to $3$

For every $y$ between those limits the curve lies further from the $y$-axis than the line, so subtract the line's integral from the curve's

`V = \pi \int_{2}^{3} \left[\left(4 y - 8\right) - \left(4 y^{2} - 16 y + 16\right)\right] \textrm{ } \text{d} y`

**[M1]**

Simplify inside the bracket before integrating

`V = \pi \int_{2}^{3} \left(- 4 y^{2} + 20 y - 24\right) \textrm{ } \text{d} y`

Integrate term by term, raising each power of $y$ by one

`V = \pi \left[- \frac{4 y^{3}}{3} + 10 y^{2} - 24 y\right]_{2}^{3}`

**[M1]**

Substitute the upper limit, then subtract the lower limit

`V = \pi \left[\left(- 36 + 90 - 72\right) - \left(- \frac{32}{3} + 40 - 48\right)\right]`

`V = \pi \left(- 18 + \frac{56}{3}\right)`

**[M1]**

$V = \frac{2}{3} π$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct statement for the volume of revolution, including $π$, with a lower limit of $2$ and your upper limit used the right way round.
> 
> **M1**: Acceptable attempt to integrate, with no power of $y$ increasing and at least two terms integrated.
> 
> **M1**: Substitutes your limits into your integrated expression the correct way round, with at least one clear substitution of each.
> 
> **A1**: $V = \frac{2}{3} π$.
> 
> The lower limit must be $2$. Neither $π$ nor the limits need to be present to earn the second mark, and $π$ need not be present for the third.
> 
> Subtracting a cone is equally acceptable, and is marked like this: the first mark is for a correct volume-of-revolution statement for the curve, including $π$, with lower limit $2$, minus the correct cone formula, and it is available even if the subtraction is the wrong way round. The remaining marks then follow the same pattern, with the cone's $- \frac{4}{3} π$ not needing to be present for the second and third. Here the curve gives $2 π$ and the cone, of radius $2$ and height $1$, gives $\frac{4}{3} π$.
> 
> For the final mark accept `0 . 6 \overset{\cdot}{6} \pi` or $0 . 67 π$ or better. A negative value that is simply made positive at the end does not earn it.
> 
> If you rotate about the $x$-axis instead, the second and third method marks are still available for integrating an expression and substituting limits, but the first and the accuracy mark are not.

> **[exam-tip]**
> Rotating about the $y$-axis changes everything about the setup.
> 
> - Integrate with respect to $y$, so rearrange each equation to give $x^{2}$ in terms of $y$
> - The limits become $y$-coordinates, here $2$ and $3$, not $x$-coordinates
> 
> Decide which boundary is the outer one before you subtract. Test a value between the limits: at $y = 2 . 5$ the curve gives $x = \sqrt{2}$ and the line gives $x = 1$, so the curve is further out and its integral comes first.
> 
> A negative volume is a signal that you have subtracted the wrong way round. Go back and swap them rather than dropping the minus sign, because the mark is lost if you simply make the answer positive at the end.
> 
> Here the line makes a cone when it is rotated, so you can check the answer without integrating it: the cone has radius $2$ and height $1$, giving $\frac{4}{3} π$, and the curve alone gives $2 π$. The difference is $\frac{2}{3} π$, as required.

## Q9 — medium — 11 marks · exam-questions

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

## Q10 — medium — 8 marks · exam-questions

### 5() — 8 marks
The region is enclosed between the curve and the line, so start by finding where the two meet

Rearrange the line to make $y$ the subject

$y = \frac{x}{3} + 1$

Set that equal to the equation of the curve

$\sqrt{2x+6} = \frac{x}{3} + 1$

Square both sides, expanding the right-hand side in full

$2 x + 6 = \frac{x^{2}}{9} + \frac{2x}{3} + 1$

Multiply every term by $9$ to clear the fractions

$18 x + 54 = x^{2} + 6 x + 9$

$x^{2} - 12 x - 45 = 0$

**[M1]**

Two numbers multiplying to $- 45$ and adding to $- 12$ are $3$ and $- 15$

`\left(x + 3\right)\left(x - 15\right) = 0`

**[M1]**

$x = - 3  \text{or}  15$

**[A1]**

Both values are genuine solutions of the original equation, so they are the limits of the region

Rotating about the $x$-axis uses `V = \pi \int y^{2} \textrm{ } \text{d} x`, and the curve gives $y^{2}$ immediately

`V_{1} = \pi \int_{- 3}^{15} \left(2 x + 6\right) \textrm{ } \text{d} x`

**[M1]**

The line sweeps out the solid that has to be taken away, so square its equation too

`V_{2} = \pi \int_{- 3}^{15} \left(\frac{x}{3} + 1\right)^{2} \textrm{ } \text{d} x`

**[M1]**

The two integrals share their limits, so subtract first and integrate once

`V = \pi \int_{- 3}^{15} \left[\left(2 x + 6\right) - \left(\frac{x^{2}}{9} + \frac{2 x}{3} + 1\right)\right] \textrm{ } \text{d} x`

`V = \pi \int_{- 3}^{15} \left(- \frac{x^{2}}{9} + \frac{4 x}{3} + 5\right) \textrm{ } \text{d} x`

Integrate term by term

`V = \pi \left[- \frac{x^{3}}{27} + \frac{2 x^{2}}{3} + 5 x\right]_{- 3}^{15}`

**[M1]**

Substitute the upper limit, then subtract the value at the lower limit

`V = \pi \left[\left(- 125 + 150 + 75\right) - \left(1 + 6 - 15\right)\right]`

`V = \pi \left[100 - \left(- 8\right)\right]`

**[M1]**

$V = 108 π$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets the equation of the curve equal to the equation of the line and forms a three-term quadratic equal to zero, including an attempt to expand `\left(\frac{x}{3} + 1\right)^{2}`.
> 
> **M1**: Solves that three-term quadratic by a complete method to find two values.
> 
> **A1**: $x = - 3$ and $x = 15$.
> 
> **M1**: Correct expression for the volume of revolution under the curve, including $π$, with your two values as the limits.
> 
> **M1**: Correct expression for the volume of revolution under the straight line, including $π$, with the same limits.
> 
> **M1**: Acceptable attempt to integrate, with no power of $x$ decreasing. Neither $π$ nor the limits need to be present for this mark.
> 
> **M1**: Substitutes your limits into your integrated expression and evaluates, with a subtraction present.
> 
> **A1**: $V = 108 π$.
> 
> The second method mark does not depend on the first, so a three-term quadratic that is not of the required form can still earn it provided a complete solving method is shown. All three of the opening marks are available if both correct values are simply written down with no working.
> 
> The official scheme's main route replaces the second solid with a cone instead of integrating it, since rotating the line produces a cone of radius $6$ and height $18$. That route is marked in exactly the same pattern: the fifth mark is then for the correct cone expression `\frac{1}{3} \pi \times 6^{2} \times \left(15 - \left(- 3\right)\right)` using your own values, and the remaining marks follow as above. The board's own alternative integrates both solids, which is what is shown here, and carries the identical eight marks.
> 
> Where the two expressions have been combined into a single integral, the fourth and fifth marks are given together for `\pm \pi \int_{- 3}^{15} \left(\frac{x^{2}}{9} - \frac{4 x}{3} - 5\right) \textrm{ } \text{d} x`.
> 
> The final mark is not given if the subtraction is done the wrong way round and the sign of the answer is simply changed at the end.

> **[exam-tip]**
> The question says to use algebraic integration, so integrate both solids rather than reaching for a formula.
> 
> - Rotating the straight line about the $x$-axis produces a cone, and the official scheme does accept $\frac{1}{3} π r^{2} h$ for it
> - The formulae sheet issued with the exam gives the surface area and volume of a sphere and the curved surface area of a cone, so the volume of a cone is not provided and would have to be remembered
> 
> Squaring both sides of an equation can introduce a solution that does not fit the original, so check the ones you get.
> 
> - At $x = - 3$ both sides of $\sqrt{2x+6} = \frac{x}{3} + 1$ are $0$
> - At $x = 15$ both sides are $6$, so both values are genuine and both are used
> 
> Subtract before you integrate wherever the two expressions share their limits.
> 
> - One integral of $- \frac{x^{2}}{9} + \frac{4x}{3} + 5$ replaces two separate integrations and two sets of substitutions
> - It also removes the commonest error here, which is subtracting the two volumes the wrong way round
> 
> There is a check on the answer that costs almost nothing.
> 
> - The curve alone gives `\pi \left[x^{2} + 6 x\right]_{- 3}^{15} = 324 \pi`
> - The cone from the line has radius $6$ and height $18$, giving $216 π$, and $324 π - 216 π$ is $108 π$

## Q11 — medium — 11 marks · exam-questions

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

$a = 2 , b = 5$

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

`\int_{0}^{0 . 2} \text{g} \left(x\right) \textrm{ } \text{d} x \approx 0 . 5324 \textrm{ } \left(4 s . f .\right)`

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

## Q12 — medium — 9 marks · exam-questions

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

## Q13 — medium — 14 marks · exam-questions

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
