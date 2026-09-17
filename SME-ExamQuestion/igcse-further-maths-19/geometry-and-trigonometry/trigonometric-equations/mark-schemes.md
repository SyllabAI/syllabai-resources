# Mark Schemes — Trigonometric Equations
**Geometry & Trigonometry** · Edexcel IGCSE Further Pure Maths (4PM1)


## Q1 — medium — 6 marks · exam-questions

### 3() — 6 marks
Every angle in the equation is `\left(2 \theta + 30\right)^{\circ}`, so treat that whole expression as a single unknown angle

Write $\text{tan}$ as $\frac{\text{sin}}{\text{cos}}$, so the equation contains only $\text{sin}$ and $\text{cos}$

`2 \text{cos} \left(2 \theta + 30\right)^{\circ} + \frac{\text{sin} \left(2 \theta + 30\right)^{\circ}}{\text{cos} \left(2 \theta + 30\right)^{\circ}} = 0`

Multiply every term by `\text{cos} \left(2 \theta + 30\right)^{\circ}` to clear the fraction

`2 \text{cos}^{2} \left(2 \theta + 30\right)^{\circ} + \text{sin} \left(2 \theta + 30\right)^{\circ} = 0`

**[M1]**

Use the identity $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$ to replace the squared cosine term

`2 \left(1 - \text{sin}^{2} \left(2 \theta + 30\right)^{\circ}\right) + \text{sin} \left(2 \theta + 30\right)^{\circ} = 0`

Expand the bracket and multiply through by $- 1$ so the squared term is positive

`2 \text{sin}^{2} \left(2 \theta + 30\right)^{\circ} - \text{sin} \left(2 \theta + 30\right)^{\circ} - 2 = 0`

**[M1] [A1]**

This is a quadratic in `\text{sin} \left(2 \theta + 30\right)^{\circ}`, and it does not factorise, so use the quadratic formula with $a = 2$, $b = - 1$ and $c = - 2$

`\text{sin} \left(2 \theta + 30\right)^{\circ} = \frac{1 \pm \sqrt{1 + 16}}{4}`

`\text{sin} \left(2 \theta + 30\right)^{\circ} = 1.28077 \ldots`

`\text{sin} \left(2 \theta + 30\right)^{\circ} = - 0.78077 \ldots`

**[M1]**

The first value is impossible, because $\text{sin}$ of any angle lies between $- 1$ and 1, so only the second value gives solutions

Adjust the interval before solving. $0 \leq θ < 180$ gives $30 \leq 2 θ + 30 < 390$

The calculator returns $- 51 . 33 \dots$, which is outside that interval, so use the symmetry of the sine curve instead

$\text{sin}$ is negative in the third and fourth quadrants

$2 θ + 30 = 180 + 51 . 33167 \dots$

$2 θ + 30 = 231 . 33167 \dots$

$θ = 100 . 66583 \dots$

$θ = 100 . 7$

**[A1]**

$2 θ + 30 = 360 - 51 . 33167 \dots$

$2 θ + 30 = 308 . 66833 \dots$

$θ = 139 . 33416 \dots$

$θ = 139 . 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Writes $\text{tan}$ as $\frac{\text{sin}}{\text{cos}}$ and multiplies through by `\text{cos} \left(2 \theta + 30\right)^{\circ}` to clear the fraction.
> 
> **M1**: Uses $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$ to write the equation in `\text{sin} \left(2 \theta + 30\right)^{\circ}` alone.
> 
> **A1**: For a correct three-term quadratic, in any equivalent arrangement.
> 
> **M1**: A correct method for solving your own three-term quadratic.
> 
> **A1**: For either value of $θ$ correct to 1 decimal place.
> 
> **A1**: For both values correct to 1 decimal place, with no extra values inside the interval.
> 
> Accept any answers which round to 100.7 and 139.3.
> 
> Showing the value $1 . 28 \dots$ before rejecting it costs nothing. It only has to be rejected, not avoided.
> 
> Values of $θ$ outside $0 \leq θ < 180$ are ignored rather than penalised.
> 
> The substitution $u = 2 θ + 30$ is equally acceptable, provided the interval is changed to $30 \leq u < 390$ before the solutions are found.

> **[exam-tip]**
> Change the interval before you change anything else.
> 
> - $0 \leq θ < 180$ becomes $30 \leq 2 θ + 30 < 390$, and forgetting this is the commonest way to lose the second answer
> - Write the new interval down at the top of your working so it is in front of you when you list the angles
> 
> A calculator gives you one angle, and the sine curve gives you the rest.
> 
> - Here the inverse sine returns $- 51 . 3 ^{\circ}$, which is not in the interval at all, so both answers come from the symmetry rather than from the calculator
> - $\text{sin}$ is negative in the third and fourth quadrants, so use $180 + 51 . 3$ and $360 - 51 . 3$
> 
> Reject the impossible root explicitly rather than ignoring it.
> 
> - $\frac{1+\sqrt{17}}{4}$ is greater than 1, and the sine of a real angle never is, so it produces no solutions

## Q2 — medium — 17 marks · exam-questions

### 10((a)) — 3 marks
**(i)**

A double angle is an angle added to itself, so use the sine addition formula from the formulae sheet with both angles equal to $A$

$\text{sin} 2 A = \text{sin} A \text{cos} A + \text{cos} A \text{sin} A$

The two terms are the same product written the other way round, so they add

$\text{sin} 2 A = 2 \text{sin} A \text{cos} A  \text{as required}$

**[B1]**

**(ii)**

Do the same with the cosine addition formula, $\text{cos} ( A + B ) = \text{cos} A \text{cos} B - \text{sin} A \text{sin} B$

$\text{cos} 2 A = \text{cos}^{2} A - \text{sin}^{2} A$

The target has only cosines in it, so replace the sine using $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$

$\text{cos} 2 A = \text{cos}^{2} A - ( 1 - \text{cos}^{2} A )$

**[M1]**

Remove the bracket and collect the two cosine terms

$\text{cos} 2 A = 2 \text{cos}^{2} A - 1  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **B1**: A complete derivation of the first given result from the addition formula for $\text{sin} ( A + A )$.
> 
> **M1**: Expands $\text{cos} ( A + A )$ correctly and replaces $\text{sin}^{2} A$ by $1 - \text{cos}^{2} A$.
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
> - $\text{cos}^{2} A - ( 1 - \text{cos}^{2} A )$ gives $2 \text{cos}^{2} A - 1$
> - Writing the bracket in and removing it on its own line is what keeps the sign right
> 
> These two results are used in every remaining part of the question.
> 
> - Part (b) needs the sine version, part (c) needs both, and part (d) needs part (b)
> - Two marks here unlock fourteen more, so it is worth doing carefully

### 10((b)) — 4 marks
The target is written in sines and cosines and the starting expression is written in tangents, so convert everything to sines and cosines first

Replace each $\text{tan} θ$ by $\frac{\text{sin}θ}{\text{cos}θ}$

$\text{f} ( θ ) = \frac{2\frac{\text{sin}θ}{\text{cos}θ}}{1+\frac{\text{sin}^{2}θ}{\text{cos}^{2}θ}}$

**[M1]**

Write the denominator as a single fraction over $\text{cos}^{2} θ$

$\text{f} ( θ ) = \frac{2\frac{\text{sin}θ}{\text{cos}θ}}{\frac{\text{cos}^{2}θ+\text{sin}^{2}θ}{\text{cos}^{2}θ}}$

**[M1]**

The numerator of that denominator is 1, by $\text{sin}^{2} θ + \text{cos}^{2} θ \equiv 1$

Dividing by $\frac{1}{\text{cos}^{2}θ}$ is the same as multiplying by $\text{cos}^{2} θ$

$\text{f} ( θ ) = 2 \frac{\text{sin}θ}{\text{cos}θ} \times \text{cos}^{2} θ$

**[M1]**

One $\text{cos} θ$ cancels with the denominator

$\text{f} ( θ ) = 2 \text{sin} θ \text{cos} θ$

Part (a) says that is exactly $\text{sin} 2 θ$

$\text{f} ( θ ) = \text{sin} 2 θ  \text{as required}$

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

$x=-0.714,0.857(3s.f.)$

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
> - $- 0 . 38050$ in radians and $- 21 . 8 ^{\circ}$ in degrees are the same angle, and mixing the two is easy to do

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

## Q3 — medium — 11 marks · exam-questions

### 8((a)) — 2 marks
The formulae sheet gives the addition formula for tangent, and a double angle is just an angle added to itself

Write $2 A$ as $A + A$, then use $\text{tan} ( A + B ) = \frac{\text{tan}A+\text{tan}B}{1-\text{tan}A\text{tan}B}$ with $B$ replaced by $A$

$\text{tan} 2 A = \frac{\text{tan}A+\text{tan}A}{1-\text{tan}A\text{tan}A}$

**[M1]**

Collect the two identical terms on the top, and write the product on the bottom as a square

$\text{tan} 2 A = \frac{2\text{tan}A}{1-\text{tan}^{2}A}  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Writes $\text{tan} 2 A$ as $\text{tan} ( A + A )$ and substitutes into the addition formula, reaching $\frac{\text{tan}A+\text{tan}A}{1-\text{tan}A\text{tan}A}$.
> 
> **A1**: Simplifies to the given result with no errors or omitted steps.
> 
> The answer is given, so the working must be complete. Simply quoting the double angle formula earns nothing, since quoting it is what the question asks you to prove.

> **[exam-tip]**
> Every double angle formula comes from an addition formula with the two angles made equal.
> 
> - $\text{tan} 2 A = \text{tan} ( A + A )$ is the whole idea, and the same trick gives the sine and cosine versions
> - The formulae sheet has the addition formulae, so you never have to remember the double angle ones separately
> 
> Show both simplifications separately.
> 
> - $\text{tan} A + \text{tan} A$ becoming $2 \text{tan} A$ and $\text{tan} A \text{tan} A$ becoming $\text{tan}^{2} A$ are two different steps
> - On a two-mark "show that" the accuracy mark is for exactly this kind of completeness

### 8((b)) — 5 marks
"Hence" means part (a) is the way in, so substitute the result you have just proved

$\text{tan} A - \frac{2\text{tan}A}{1-\text{tan}^{2}A} = 0$

**[M1]**

Clear the fraction by multiplying every term by $1 - \text{tan}^{2} A$

$\text{tan} A ( 1 - \text{tan}^{2} A ) - 2 \text{tan} A = 0$

**[M1]**

Expand the bracket

$\text{tan} A - \text{tan}^{3} A - 2 \text{tan} A = 0$

Collect the two $\text{tan} A$ terms

$- \text{tan}^{3} A - \text{tan} A = 0$

Multiply through by $- 1$ to make the leading term positive

$\text{tan}^{3} A + \text{tan} A = 0$

Every term has a factor of $\text{tan} A$, so factorise rather than dividing by it, since dividing would lose solutions

$\text{tan} A ( \text{tan}^{2} A + 1 ) = 0$

**[M1]**

A product is zero when one of its factors is zero, so consider each in turn

The second factor gives $\text{tan}^{2} A = - 1$, and no square can be negative, so that factor produces nothing

$\text{tan} A = 0$

$A = 0$

**[A1]**

The tangent graph repeats every $180 ^{\circ}$, so add $180$ to reach the only other value in range

$A=0,180$

**[A1]**

> **[mark-scheme]**
> **M1**: Correctly substitutes the result of part (a) into the given equation.
> 
> **M1**: Multiplies through by $1 - \text{tan}^{2} A$, or reaches a correct single fraction and eliminates $1 - \text{tan}^{2} A$ as the denominator.
> 
> **M1**: A correct rearrangement of your equation, factorised correctly into a linear factor and a quadratic factor equal to zero.
> 
> **A1**: Either $A = 0$ or $A = 180$. This mark depends on all three method marks.
> 
> **A1**: Both $A = 0$ and $A = 180$, with no other values inside the range. Values outside the range are ignored. This mark depends on all three method marks.
> 
> An answer reached by trial and improvement scores nothing on this question, however many correct values it lists.
> 
> Working from a correct single fraction is equally acceptable, so `\text{tan} A \left(1 - \frac{2}{1 - \text{tan}^{2} A}\right) = 0` leading to $1 - \text{tan}^{2} A - 2 = 0$ earns the second and third marks.

> **[exam-tip]**
> Factorise rather than divide, or you will lose the solutions you are being asked for.
> 
> - Cancelling $\text{tan} A$ from $\text{tan}^{3} A + \text{tan} A = 0$ throws away $\text{tan} A = 0$, which is where both answers come from
> - The habit to build is that a trigonometric equation equal to zero always wants factorising
> 
> A quadratic factor with no real roots is still worth a line of writing.
> 
> - $\text{tan}^{2} A + 1 = 0$ needs $\text{tan}^{2} A = - 1$, which is impossible for a real angle
> - Say so explicitly rather than ignoring the factor, so the examiner can see you considered it
> 
> Check the endpoints of the range carefully.
> 
> - The range here is $0 \leq A \leq 180$ and both ends are included, so $0$ and $180$ both count
> - A range written with strict inequalities would have left this equation with no solutions at all
> 
> Note where the equation is undefined.
> 
> - $\text{tan} 90 ^{\circ}$ does not exist, so $A = 90$ could never be a solution whatever the algebra suggested
> - Neither of the answers is affected here, but it is worth a glance on any question involving tangents

### 8((c)) — 4 marks
The angles on the two sides are different, so expand the compound angle to get everything in terms of $x$

The formulae sheet gives $\text{cos} ( A - B ) = \text{cos} A \text{cos} B + \text{sin} A \text{sin} B$

$\text{cos} x \text{cos} \frac{π}{6} + \text{sin} x \text{sin} \frac{π}{6} = \text{sin} x$

**[M1]**

$\text{cos} \frac{π}{6} = \frac{\sqrt{3}}{2}$ and $\text{sin} \frac{π}{6} = \frac{1}{2}$, both exact values worth knowing

$\frac{\sqrt{3}}{2} \text{cos} x + \frac{1}{2} \text{sin} x = \text{sin} x$

Multiply through by 2 to clear the fractions

$\sqrt{3} \text{cos} x + \text{sin} x = 2 \text{sin} x$

$\sqrt{3} \text{cos} x = \text{sin} x$

Divide both sides by $\text{cos} x$, using $\text{tan} x = \frac{\text{sin}x}{\text{cos}x}$

$\text{tan} x = \sqrt{3}$

**[M1]**

$\sqrt{3}$ is an exact value, so the base angle is one to recognise rather than look up

$x = \frac{π}{3}$

**[A1]**

The tangent graph repeats every $π$, so subtract $π$ and add $π$ to sweep the whole range $- π \leq x \leq 2 π$

Adding $π$ twice would give $\frac{7π}{3}$, which is outside the range

$x=-\frac{2π}{3},\frac{π}{3},\frac{4π}{3}$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the formula for $\text{cos} ( A - B )$ to expand the left-hand side correctly.
> 
> **M1**: Rearranges to $\text{tan} x = \sqrt{3}$, or to $\text{tan} x = a$ for their value of $a$. This mark depends on the first method mark.
> 
> **A1**: One correct value in range.
> 
> **A1**: All three correct values, and no extra values inside the range.
> 
> The question asks for exact values, so decimal answers such as $1 . 05$ earn nothing on the final two marks.
> 
> Working in degrees and converting back is equally acceptable, giving $60 ^{\circ}$, and the range becomes $- 180 ^{\circ} \leq x \leq 360 ^{\circ}$.

> **[exam-tip]**
> Different angles on the two sides always means expanding first.
> 
> - You cannot compare `\text{cos} \left(x - \frac{\pi}{6}\right)` with $\text{sin} x$ until both are written in terms of $x$ alone
> - Once expanded, the sine terms collect and the equation collapses to a tangent
> 
> Dividing by $\text{cos} x$ is safe here, but it is worth knowing why.
> 
> - If $\text{cos} x$ were zero then $\sqrt{3} \text{cos} x = \text{sin} x$ would force $\text{sin} x = 0$ too, and they are never both zero
> - So no solutions are lost, unlike the factorising situation in part (b)
> 
> Count how many solutions the range should hold before you write any down.
> 
> - The range $- π \leq x \leq 2 π$ is three lots of $π$ wide and $\text{tan}$ repeats every $π$, so expect three answers
> - Getting only one is the commonest way to lose the last mark here
> 
> Exact values mean surds and multiples of $π$ throughout.
> 
> - $\text{tan} x = \sqrt{3}$ gives $\frac{π}{3}$ exactly, so there is never a need for the calculator
> - Keep the answers as fractions of $π$ rather than converting to decimals at the end

## Q4 — medium — 16 marks · exam-questions

### 11((a)) — 4 marks
**(i)**

A double angle is an angle added to itself, so start from the addition formula on the formulae sheet

Use $\text{cos} ( A + B ) = \text{cos} A \text{cos} B - \text{sin} A \text{sin} B$ with both angles equal to $A$

$\text{cos} 2 A = \text{cos}^{2} A - \text{sin}^{2} A$

**[M1]**

The target has only cosines in it, so remove the sine using $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$

$\text{cos} 2 A = \text{cos}^{2} A - ( 1 - \text{cos}^{2} A )$

**[M1]**

Remove the bracket and collect the two cosine terms

$\text{cos} 2 A = 2 \text{cos}^{2} A - 1  \text{as required}$

**[A1]**

**(ii)**

Do the same with the sine addition formula, $\text{sin} ( A + B ) = \text{sin} A \text{cos} B + \text{cos} A \text{sin} B$

$\text{sin} 2 A = \text{sin} A \text{cos} A + \text{cos} A \text{sin} A$

The two terms are the same product written the other way round, so they add

$\text{sin} 2 A = 2 \text{sin} A \text{cos} A  \text{as required}$

**[B1]**

> **[mark-scheme]**
> **M1**: Correct use of the addition formula for $\text{cos} ( A + A )$.
> 
> **M1**: Correct use of $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$ to eliminate $\text{sin}^{2} A$.
> 
> **A1**: Reaches the first given result with no errors.
> 
> **B1**: A complete derivation of the second given result from the addition formula for $\text{sin} ( A + A )$.
> 
> Both answers are given, so both derivations must be complete.

> **[exam-tip]**
> The formulae sheet gives the addition formulae, not the double angle ones.
> 
> - Setting $B = A$ in $\text{cos} ( A + B )$ and $\text{sin} ( A + B )$ is what produces them
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

$\text{cos} 3 A = ( 2 \text{cos}^{2} A - 1 ) \text{cos} A - 2 \text{sin} A \text{cos} A \text{sin} A$

**[M1]**

Expand the first bracket, and write the two sines as a square

$\text{cos} 3 A = 2 \text{cos}^{3} A - \text{cos} A - 2 \text{sin}^{2} A \text{cos} A$

There is still a sine in the expression, so remove it with $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$

$\text{cos} 3 A = 2 \text{cos}^{3} A - \text{cos} A - 2 ( 1 - \text{cos}^{2} A ) \text{cos} A$

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
> **M1**: Writes $\text{cos} 3 A$ as $\text{cos} ( 2 A + A )$ and expands correctly with the addition formula.
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
> - $- 2 ( 1 - \text{cos}^{2} A ) \text{cos} A$ gives $- 2 \text{cos} A + 2 \text{cos}^{3} A$
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
> Working in degrees throughout is equally acceptable, provided the answers are converted back, giving $40 ^{\circ}$, $200 ^{\circ}$ and $280 ^{\circ}$.

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

## Q5 — medium — 13 marks · exam-questions

### 10((a)) — 5 marks
**(i)**

A double angle is an angle added to itself, so start from the addition formula on the formulae sheet

Use $\text{sin} ( A + B ) = \text{sin} A \text{cos} B + \text{cos} A \text{sin} B$ with both angles equal to $θ$

$\text{sin} 2 θ = \text{sin} θ \text{cos} θ + \text{cos} θ \text{sin} θ$

**[M1]**

The two terms are the same product written in the opposite order, so they add

$\text{sin} 2 θ = 2 \text{sin} θ \text{cos} θ  \text{as required}$

**[A1]**

**(ii)**

Do the same with the cosine addition formula, $\text{cos} ( A + B ) = \text{cos} A \text{cos} B - \text{sin} A \text{sin} B$

$\text{cos} 2 θ = \text{cos} θ \text{cos} θ - \text{sin} θ \text{sin} θ$

$\text{cos} 2 θ = \text{cos}^{2} θ - \text{sin}^{2} θ$

**[M1]**

The target has only cosines in it, so replace the sine using $\text{sin}^{2} θ + \text{cos}^{2} θ \equiv 1$

$\text{cos} 2 θ = \text{cos}^{2} θ - ( 1 - \text{cos}^{2} θ )$

**[M1]**

Remove the bracket and collect the two cosine terms

$\text{cos} 2 θ = 2 \text{cos}^{2} θ - 1  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the addition formula for sine with both angles equal to $θ$.
> 
> **A1**: Reaches the first given result with no errors.
> 
> **M1**: Uses the addition formula for cosine with both angles equal to $θ$, reaching $\text{cos}^{2} θ - \text{sin}^{2} θ$.
> 
> **M1**: Replaces $\text{sin}^{2} θ$ by $1 - \text{cos}^{2} θ$.
> 
> **A1**: Reaches the second given result with no errors.
> 
> Both answers are given, so both derivations must be complete. Quoting the double angle formulae directly earns nothing, since deriving them is what is being asked.

> **[exam-tip]**
> Every double angle formula is an addition formula with the two angles made the same.
> 
> - The formulae sheet gives you $\text{sin} ( A + B )$ and $\text{cos} ( A + B )$, and setting $B = A$ does the rest
> - That is worth knowing even once you have memorised the double angle forms, because it lets you rebuild them under pressure
> 
> The cosine version needs one extra step that the sine version does not.
> 
> - $\text{cos}^{2} θ - \text{sin}^{2} θ$ is a correct expansion, but it is not the required form
> - The Pythagorean identity is what converts it, and which function you eliminate decides which of the three versions you end up with
> 
> Write the substitution in brackets first.
> 
> - $\text{cos}^{2} θ - ( 1 - \text{cos}^{2} θ )$ becomes $2 \text{cos}^{2} θ - 1$, and the minus sign in front of the bracket is where marks are lost
> - Removing the bracket as its own separate line makes the sign change visible

### 10((b)) — 4 marks
Replace both terms with things you can work with, using part (a) for the first and the definition of tangent for the second

$\text{sin} 2 θ - \text{tan} θ = 2 \text{sin} θ \text{cos} θ - \frac{\text{sin}θ}{\text{cos}θ}$

**[M1]**

The target is a product with $\text{tan} θ$ in it, and $\text{tan} θ$ contains $\text{sin} θ$, so take out a factor of $\text{sin} θ$

`\text{sin} 2 \theta - \text{tan} \theta = \text{sin} \theta \left(2 \text{cos} \theta - \frac{1}{\text{cos} \theta}\right)`

**[M1]**

Write the bracket as a single fraction over $\text{cos} θ$

`\text{sin} 2 \theta - \text{tan} \theta = \text{sin} \theta \left(\frac{2 \text{cos}^{2} \theta - 1}{\text{cos} \theta}\right)`

**[M1]**

Two things now fall out at once

The numerator $2 \text{cos}^{2} θ - 1$ is exactly $\text{cos} 2 θ$ from part (a), and $\frac{\text{sin}θ}{\text{cos}θ}$ is $\text{tan} θ$

$\text{sin} 2 θ - \text{tan} θ = \text{tan} θ \text{cos} 2 θ  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $\text{sin} 2 θ = 2 \text{sin} θ \text{cos} θ$ and $\text{tan} θ = \frac{\text{sin}θ}{\text{cos}θ}$.
> 
> **M1**: Takes out a factor of $\text{sin} θ$, or reaches a correct single fraction over $\text{cos} θ$.
> 
> **M1**: Reaches `\text{sin} \theta \left(\frac{2 \text{cos}^{2} \theta - 1}{\text{cos} \theta}\right)` or the equivalent. This mark depends on the previous method mark.
> 
> **A1**: Identifies the numerator as $\text{cos} 2 θ$ and reaches the given result with no errors.
> 
> Putting everything over the common denominator $\text{cos} θ$ first is equally acceptable, giving $\frac{2\text{sin}θ\text{cos}^{2}θ-\text{sin}θ}{\text{cos}θ}$ before the factorisation.
> 
> Working on both sides and meeting in the middle is also acceptable, provided each side is developed independently and the two are shown to agree.
> 
> The condition $θ \neq 90 ^{\circ} + 180 ^{\circ} n$ is given because $\text{tan} θ$ is undefined there and $\text{cos} θ$ is zero, so it does not need proving.

> **[exam-tip]**
> Look at what the target contains and work towards it.
> 
> - The answer is a product containing $\text{tan} θ$ and $\text{cos} 2 θ$, so you need a factor of $\frac{\text{sin}θ}{\text{cos}θ}$ and a factor of $2 \text{cos}^{2} θ - 1$
> - Knowing what you are aiming for is what tells you to factorise out $\text{sin} θ$ rather than expanding further
> 
> Turn tangents into sines over cosines at the very start.
> 
> - Almost every proof of this shape begins by writing $\text{tan} θ$ as $\frac{\text{sin}θ}{\text{cos}θ}$
> - It puts everything into two functions instead of three, which is what makes the factorising visible
> 
> The condition on $θ$ in the question is a hint as well as a restriction.
> 
> - It excludes the angles where $\text{cos} θ = 0$, which is exactly the denominator you are about to create
> - So you can divide by $\text{cos} θ$ freely without worrying about losing solutions
> 
> Part (b) is the engine for part (c).
> 
> - Turning a difference into a product is what lets you solve the equation by setting each factor to zero
> - Difference equals zero tells you nothing on its own, while product equals zero tells you everything

### 10((c)) — 4 marks
Part (b) turns the left-hand side into a product, and that is what makes the equation solvable

$\text{tan} x \text{cos} 2 x = 0$

A product is zero exactly when one of its factors is zero, so take each factor in turn

Start with the first factor

$\text{tan} x = 0$

The tangent is zero at $0$, $180$ and $360$, but the range $0 < x < 360$ excludes both endpoints

$x = 180$

**[B1]**

Now the second factor

$\text{cos} 2 x = 0$

Solve for $2 x$ rather than $x$, and double the range to match, so $2 x$ runs from $0$ to $720$

The cosine is zero every $180$ degrees, starting at $90$

$2x=90,270,450,630$

**[M1]**

Halve each one

$x=45,135,225,315$

**[A1] [A1]**

> **[mark-scheme]**
> **B1**: $x = 180$ from $\text{tan} x = 0$.
> 
> **M1**: Sets $\text{cos} 2 x = 0$ and finds at least one correct value for $2 x$, having doubled the range.
> 
> **A1**: For any two correct values from $x = 45$, $135$, $225$ and $315$.
> 
> **A1**: For all four correct values from from $x = 45$, $135$, $225$ and $315$.
> 
> Values outside the range are ignored rather than penalised.
> 
> Solving $\text{cos} x = 0$ instead of $\text{cos} 2 x = 0$ gives only $x = 90$ and $x = 270$, which are not solutions of the original equation, and earns nothing.

> **[exam-tip]**
> The whole point of part (b) is that it turns a difference into a product.
> 
> - $\text{sin} 2 x - \text{tan} x = 0$ cannot be attacked directly, but $\text{tan} x \text{cos} 2 x = 0$ splits into two easy equations
> - Whenever a question proves an identity and then asks you to solve, expect to use it
> 
> Double the range whenever you double the angle.
> 
> - $0 < x < 360$ becomes $0 < 2 x < 720$, which is why there are four values of $2 x$ rather than two
> - Stopping at $2 x = 90$ and $270$ loses half the answers, and it is the single commonest error here
> 
> Check the strictness of the inequalities at the ends.
> 
> - $\text{tan} x = 0$ has solutions at $0$, $180$ and $360$, but the range is strict at both ends
> - So only $180$ survives, and quoting $0$ or $360$ as well would cost the final mark

## Q6 — medium — 13 marks · exam-questions

### 9((a)) — 4 marks
**(i)**

Both results come from the same starting point, the double angle formula for cosine

Write $2 A$ as $A + A$ and use $\text{cos} ( A + B ) = \text{cos} A \text{cos} B - \text{sin} A \text{sin} B$ from the formulae sheet

$\text{cos} 2 A = \text{cos}^{2} A - \text{sin}^{2} A$

This still has both functions in it, so remove the sine using $\text{sin}^{2} A + \text{cos}^{2} A \equiv 1$

$\text{cos} 2 A = \text{cos}^{2} A - ( 1 - \text{cos}^{2} A )$

**[M1]**

$\text{cos} 2 A = 2 \text{cos}^{2} A - 1$

Now make $\text{cos}^{2} A$ the subject

$2 \text{cos}^{2} A = \text{cos} 2 A + 1$

$\text{cos}^{2} A = \frac{\text{cos}2A+1}{2}  \text{as required}$

**[A1]**

**(ii)**

Start from the same expansion, but this time remove the cosine instead, using $\text{cos}^{2} A = 1 - \text{sin}^{2} A$

$\text{cos} 2 A = ( 1 - \text{sin}^{2} A ) - \text{sin}^{2} A$

**[M1]**

$\text{cos} 2 A = 1 - 2 \text{sin}^{2} A$

Make $\text{sin}^{2} A$ the subject

$2 \text{sin}^{2} A = 1 - \text{cos} 2 A$

$\text{sin}^{2} A = \frac{1-\text{cos}2A}{2}  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses $\text{cos} ( A + B )$ with $B = A$ to reach $\text{cos}^{2} A - \text{sin}^{2} A$, then replaces $\text{sin}^{2} A$ by $1 - \text{cos}^{2} A$.
> 
> **A1**: Rearranges correctly to the first given result, with no errors.
> 
> **M1**: Replaces $\text{cos}^{2} A$ by $1 - \text{sin}^{2} A$ instead, reaching $1 - 2 \text{sin}^{2} A$.
> 
> **A1**: Rearranges correctly to the second given result, with no errors.
> 
> Both answers are given, so both derivations must be complete.
> 
> Quoting $\text{cos} 2 A = 2 \text{cos}^{2} A - 1$ or $\text{cos} 2 A = 1 - 2 \text{sin}^{2} A$ as a known result earns the method mark, since the question directs you to the formulae sheet rather than to a proof from first principles.
> 
> Deriving the second result from the first is equally acceptable, by substituting $\text{cos}^{2} A = 1 - \text{sin}^{2} A$ into it.

> **[exam-tip]**
> These two results are the same identity wearing different clothes.
> 
> - Both start from $\text{cos} 2 A = \text{cos}^{2} A - \text{sin}^{2} A$, and the only choice is which function you eliminate
> - Eliminating the sine leaves everything in cosines, and eliminating the cosine leaves everything in sines
> 
> They are the formulae that make squared trigonometric terms integrable, so they are worth memorising in both directions.
> 
> - $\text{cos}^{2} A$ and $\text{sin}^{2} A$ cannot be integrated directly, but $\text{cos} 2 A$ can
> - Part (b) then uses them the other way, to collapse a product of brackets into a single double angle expression
> 
> Watch the bracket when you substitute.
> 
> - $\text{cos}^{2} A - ( 1 - \text{cos}^{2} A )$ gives $2 \text{cos}^{2} A - 1$, not $1$
> - Writing the substitution inside brackets first, and removing them as a separate step, is what stops the sign error

### 9((b)) — 5 marks
The right-hand side is written in double angles, so expand the left-hand side first and convert afterwards

Multiply the two brackets out term by term

$( 2 \text{sin} x - \text{cos} x ) ( \text{sin} x - 3 \text{cos} x ) = 2 \text{sin}^{2} x - 6 \text{sin} x \text{cos} x - \text{sin} x \text{cos} x + 3 \text{cos}^{2} x$

**[M1]**

Collect the two middle terms

$( 2 \text{sin} x - \text{cos} x ) ( \text{sin} x - 3 \text{cos} x ) = 2 \text{sin}^{2} x - 7 \text{sin} x \text{cos} x + 3 \text{cos}^{2} x$

Now convert each piece into double angles, taking the squared terms from part (a) with $x$ in place of $A$

$2 \text{sin}^{2} x = 1 - \text{cos} 2 x$

**[M1]**

$3 \text{cos}^{2} x = \frac{3\text{cos}2x+3}{2}$

**[M1]**

The middle term is not a square, so it needs the sine double angle formula instead

Since $\text{sin} 2 x = 2 \text{sin} x \text{cos} x$, the product $\text{sin} x \text{cos} x$ is half of $\text{sin} 2 x$

$7 \text{sin} x \text{cos} x = \frac{7\text{sin}2x}{2}$

**[M1]**

Put the three converted pieces back together

$( 2 \text{sin} x - \text{cos} x ) ( \text{sin} x - 3 \text{cos} x ) = 1 - \text{cos} 2 x - \frac{7\text{sin}2x}{2} + \frac{3\text{cos}2x+3}{2}$

Collect the constants, $1 + \frac{3}{2}$, and the two $\text{cos} 2 x$ terms, $- 1 + \frac{3}{2}$

$( 2 \text{sin} x - \text{cos} x ) ( \text{sin} x - 3 \text{cos} x ) = \frac{1}{2} \text{cos} 2 x - \frac{7}{2} \text{sin} 2 x + \frac{5}{2}$

Take out the factor of $\frac{1}{2}$

$( 2 \text{sin} x - \text{cos} x ) ( \text{sin} x - 3 \text{cos} x ) = \frac{1}{2} ( \text{cos} 2 x - 7 \text{sin} 2 x + 5 )  \text{as required}$

**[A1]**

> **[mark-scheme]**
> **M1**: Expands the two brackets correctly to reach $2 \text{sin}^{2} x - 7 \text{sin} x \text{cos} x + 3 \text{cos}^{2} x$, or the unsimplified equivalent.
> 
> **M1**: Substitutes for $\text{sin}^{2} x$ using part (a).
> 
> **M1**: Substitutes for $\text{cos}^{2} x$ using part (a).
> 
> **M1**: Replaces $\text{sin} x \text{cos} x$ by $\frac{1}{2} \text{sin} 2 x$.
> 
> **A1**: Collects the terms correctly and reaches the given result with no errors.
> 
> The answer is given, so the working has to be complete throughout.
> 
> Starting from the right-hand side and working back to the left is equally acceptable, and is marked with the same five marks in reverse order.

> **[exam-tip]**
> Work from the messier side towards the tidier one.
> 
> - The left-hand side has brackets to expand, so it gives you something to do, while the right-hand side does not
> - That is the general rule for proving an identity, and it applies here even though both sides look equally involved
> 
> Three separate conversions are needed, and it is easy to do only two.
> 
> - The squared terms come from part (a), but the $\text{sin} x \text{cos} x$ term needs $\text{sin} 2 x = 2 \text{sin} x \text{cos} x$ instead
> - Part (a) does not mention that formula at all, which is exactly why it gets forgotten
> 
> Keep the fractions rather than switching to decimals.
> 
> - The target has a factor of $\frac{1}{2}$ outside a bracket, so halves are what you are aiming for throughout
> - Collect the constants and the $\text{cos} 2 x$ terms separately, then factorise at the very end
> 
> Part (b) is doing more than it appears.
> 
> - Rewriting $y$ in double angles is what makes part (c) a one-line differentiation
> - Differentiating the original product would need the product rule and a good deal more algebra

### 9((c)) — 4 marks
Part (b) has already rewritten $y$ in a form that differentiates in one line, so use that rather than the original product

`y = \frac{1}{2} \left(\text{cos} 2 x - 7 \text{sin} 2 x + 5\right)`

Differentiating $\text{cos} 2 x$ gives $- 2 \text{sin} 2 x$, and differentiating $\text{sin} 2 x$ gives $2 \text{cos} 2 x$, with the constant differentiating to zero

`\frac{\text{d} y}{\text{d} x} = \frac{1}{2} \left(- 2 \text{sin} 2 x - 14 \text{cos} 2 x\right)`

$\frac{\text{d}y}{\text{d}x} = - \text{sin} 2 x - 7 \text{cos} 2 x$

**[M1]**

Set the derivative equal to zero, as the question asks

$- \text{sin} 2 x - 7 \text{cos} 2 x = 0$

$- \text{sin} 2 x = 7 \text{cos} 2 x$

Divide both sides by $\text{cos} 2 x$, using $\text{tan} 2 x = \frac{\text{sin}2x}{\text{cos}2x}$

$\text{tan} 2 x = - 7$

**[M1]**

Solve for $2 x$ rather than $x$, and widen the range to match

Since $0 \circ \leq x \leq 180 \circ$, the angle $2 x$ runs from $0^{\circ}$ to $360^{\circ}$

The calculator returns $- 81 . 869 \dots \circ$, which is outside that range, so add $180$ to bring it in

$2x=98.130\dots^{\circ}$

**[A1]**

The tangent graph repeats every $180 \circ$, so add $180$ again for the second value

$2x=278.130\dots^{\circ}$

Halve both values to get back to $x$

$x=49^{\circ},139^{\circ}$

**[A1]**

> **[mark-scheme]**
> **M1**: An attempt to differentiate the given equation. As a minimum you must reach $\frac{\text{d}y}{\text{d}x} = \pm k \text{sin} 2 x \pm l \text{cos} 2 x$, with $k$ and $l$ integers and no other terms.
> 
> **M1**: Uses $\text{tan} 2 x = \frac{\text{sin}2x}{\text{cos}2x}$, dividing correctly by $\text{cos} 2 x$ throughout. This mark is independent but must be used correctly.
> 
> **A1**: At least one correct value for $2 x$, so any of $- 81 . 869 \dots$, $98 . 130 \dots$ or $278 . 130 \dots$. Accept $- 81$, $98$ or $278$.
> 
> **A1**: $x = 49$ and $x = 139$, rounded to the nearest whole number or better.
> 
> Differentiating the original product with the product rule is equally acceptable, and reaches the same equation.

> **[exam-tip]**
> The earlier parts of a question like this are there to be used.
> 
> - Part (b) hands you a form with no products in it, so the differentiation is a single line
> - Going back to `\left(2 \text{sin} x - \text{cos} x\right) \left(\text{sin} x - 3 \text{cos} x\right)` and using the product rule is valid but much longer
> 
> Change the range before you solve, not after.
> 
> - Doubling the angle doubles the range, so $0 \circ \leq x \leq 180 \circ$ becomes $0 \circ \leq 2 x \leq 360 \circ$
> - Finding the values of $2 x$ first and halving at the end is far safer than halving as you go
> 
> A negative tangent means the calculator value is outside almost any exam range.
> 
> - `\text{tan}^{- 1} \left(- 7\right)` gives $- 81 . 869 \circ$, which is not an answer, it is a starting point
> - Add $180 \circ$ until you are inside the range, then keep adding $180 \circ$ until you leave it
> 
> Keep the unrounded values of $2 x$ until the halving.
> 
> - Rounding $98 . 130 \circ$ to $98 \circ$ first gives $x = 49 \circ$, which happens to be right here, but the habit will cost marks elsewhere
