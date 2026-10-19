# Mark Schemes — Calculus for Kinematics
**Calculus** · Edexcel IGCSE Further Pure Maths (4PM1)


## Q1 — medium — 9 marks · exam-questions

### 4((a)) — 2 marks
Instantaneously at rest means the velocity is zero at that instant, so set $v = 0$

$4 t^{2} - 19 t + 12 = 0$

Two numbers multiplying to $4 \times 12 = 48$ and adding to $- 19$ are $- 3$ and $- 16$, so split the middle term

$4 t^{2} - 16 t - 3 t + 12 = 0$

`4 t \left(t - 4\right) - 3 \left(t - 4\right) = 0`

`\left(4 t - 3\right)\left(t - 4\right) = 0`

**[M1]**

Both roots are positive, so both are allowed by the condition $t \geq 0$

$t = \frac{3}{4}  \text{or}  4$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets $v = 0$ and makes an acceptable attempt to solve the resulting quadratic.
> 
> **A1**: Both values, $t = \frac{3}{4}$ and $t = 4$.
> 
> The quadratic formula and completing the square are equally acceptable in place of factorising, and earn the same method mark. Accept $0 . 75$ for the first value.
> 
> Both values are needed for the accuracy mark, and there are no marks for stopping at one of them. This part has no marking notes in the official scheme, so its two marks are printed on a single row and the descriptors above follow that row in order.

> **[exam-tip]**
> "Instantaneously at rest" is a phrase to translate straight into an equation.
> 
> - It means the velocity is zero at that moment, so write $v = 0$ and solve
> - It does not mean the acceleration is zero, which is a different question entirely and is what part (c) asks
> 
> Check both roots against the domain before you write them down.
> 
> - Here $t \geq 0$, and $\frac{3}{4}$ and $4$ are both positive, so neither is rejected
> - A negative root would have to be discarded, and saying so is what shows you checked

### 4((b)) — 4 marks
Displacement is the integral of velocity with respect to time

`s = \int \left(4 t^{2} - 19 t + 12\right) \textrm{ } \text{d} t`

Raise each power of $t$ by one and divide by the new power, remembering the constant

$s = \frac{4t^{3}}{3} - \frac{19t^{2}}{2} + 12 t + c$

**[M1]**

The constant is fixed by the displacement given at $t = 0$

Substituting $t = 0$ makes every term in $t$ vanish, so $s = c$ at that instant

$- 4 = c$

**[M1]**

$s = \frac{4t^{3}}{3} - \frac{19t^{2}}{2} + 12 t - 4$

**[A1]**

Now substitute $t = 6$

$s = \frac{4\times6^{3}}{3} - \frac{19\times6^{2}}{2} + 12 \times 6 - 4$

$s = 288 - 342 + 72 - 4$

$s = 14  \text{m}$

**[A1]**

> **[mark-scheme]**
> **M1**: Integrates $v$ with respect to $t$, raising each power of $t$ by one. The constant of integration need not be present for this mark.
> 
> **M1**: Uses $t = 0$ and $s = - 4$ to find the constant of integration.
> 
> **A1**: A fully correct expression for the displacement, $s = \frac{4t^{3}}{3} - \frac{19t^{2}}{2} + 12 t - 4$.
> 
> **A1**: $s = 14$.
> 
> The unit is not required for the final mark. The displacement is asked for rather than the distance, so a signed answer is what is wanted, and here it happens to be positive.
> 
> This part has no marking notes in the official scheme, so its marks are printed a row at a time and the descriptors above follow those rows in order.

> **[exam-tip]**
> Every kinematics integration needs its constant, and the question always gives you what fixes it.
> 
> - Here that is the displacement of $- 4$ m at $t = 0$
> - Substituting $t = 0$ kills every other term, so the constant is simply the displacement at that instant
> 
> Displacement and distance are different quantities and the command word tells you which is wanted.
> 
> - Displacement is measured from the origin and carries a sign
> - Distance travelled would mean checking whether the particle turns round in the interval, which is a longer calculation
> 
> The particle really does turn round twice between $t = 0$ and $t = 6$, which is why the answer is smaller than it looks.
> 
> - The velocity is zero at $t = \frac{3}{4}$ and again at $t = 4$, so the motion reverses at each
> - Integrating straight through handles that automatically for a displacement, which is exactly why no interval splitting is needed here

### 4((c)) — 3 marks
Acceleration is the rate of change of velocity, so differentiate $v$ with respect to $t$

$a = \frac{\text{d}v}{\text{d}t}$

$a = 8 t - 19$

**[M1]**

Now set that equal to zero

$8 t - 19 = 0$

**[M1]**

$t = \frac{19}{8}$

**[A1]**

> **[mark-scheme]**
> **M1**: Differentiates $v$ with respect to $t$, with no power of $t$ increasing.
> 
> **M1**: Sets your expression for $a$ equal to zero and solves for $t$.
> 
> **A1**: $t = \frac{19}{8}$.
> 
> Accept $2 . 375$ or any exact equivalent. Integrating instead of differentiating earns nothing here.

> **[exam-tip]**
> Differentiating takes you towards acceleration and integrating takes you towards displacement.
> 
> - Velocity sits between them, so from $v$ you differentiate for $a$ and integrate for $s$
> - Getting the direction wrong is the single commonest error in this topic, and it costs every mark in the part
> 
> Zero acceleration is not the same as zero velocity.
> 
> - Part (a) found the times when the particle is at rest, $\frac{3}{4}$ and $4$
> - This part finds when it stops speeding up or slowing down, and $\frac{19}{8}$ sits neatly between those two, which is the turning point of the velocity

## Q2 — medium — 9 marks · exam-questions

### 5((a)) — 3 marks
Velocity is the integral of acceleration with respect to time

`v = \int \left(3 t - 4\right) \textrm{ } \text{d} t`

$v = \frac{3t^{2}}{2} - 4 t + c$

**[M1]**

$P$ is at rest when $t = 0$, so $v = 0$ there, and substituting $t = 0$ leaves $v = c$

$c = 0$

$v = \frac{3t^{2}}{2} - 4 t$

Now substitute $t = 4$

$v = \frac{3\times4^{2}}{2} - 4 \times 4$

**[M1]**

$v = 24 - 16$

$v = 8  \text{m s}^{-1}$

**[A1]**

> **[mark-scheme]**
> **M1**: An acceptable attempt to integrate the given expression for $a$, with at least one term correctly integrated and no power of $t$ decreasing. The terms need not be simplified.
> 
> **M1**: Substitutes $t = 4$ into your integrated expression. This may be implied by a correct answer.
> 
> **A1**: $v = 8$.
> 
> The calculation of $c = 0$ does not have to be seen. The unit is not required for the final mark.
> 
> The official scheme carries an explicit warning here: substituting $t = 4$ into the expression for $a$ also gives $8$, and that must not be credited, because it is the acceleration at that instant rather than the velocity.

> **[exam-tip]**
> This question hides a coincidence that the examiners are told to watch for.
> 
> - Substituting $t = 4$ straight into $a = 3 t - 4$ also gives $8$
> - That is the acceleration, not the velocity, and it scores nothing, so make the integration visible before you substitute anything
> 
> "At rest" at $t = 0$ is the condition that fixes the constant.
> 
> - It tells you $v = 0$ when $t = 0$, which forces $c = 0$
> - A constant of zero still has to be justified rather than assumed, even though it disappears from the final expression

### 5((b)) — 2 marks
Instantaneously at rest means the velocity is zero, so set the expression from part (a) equal to zero

$\frac{3t^{2}}{2} - 4 t = 0$

There is no constant term, so take out the common factor of $t$ rather than reaching for the formula

`t \left(\frac{3 t}{2} - 4\right) = 0`

**[M1]**

That gives $t = 0$, which is the instant the particle starts from rest, and one other solution

You are told $T > 0$, so it is the other solution that is wanted

$\frac{3T}{2} = 4$

$T = \frac{8}{3}$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets your expression for $v$ equal to zero and makes a fully correct attempt to solve it, leading to a value for $t$. A correct value can imply this mark, but if the quadratic is not the correct one the method must be shown.
> 
> **A1**: $T = \frac{8}{3}$. Ignore $t = 0$ if it is also given.
> 
> Accept answers which round to $2 . 7$, or a clear indication of $2 . 6$ recurring.

> **[exam-tip]**
> A quadratic with no constant term factorises in one step.
> 
> - $\frac{3t^{2}}{2} - 4 t = 0$ becomes `t \left(\frac{3 t}{2} - 4\right) = 0` immediately
> - Never divide through by $t$, because that throws away the solution $t = 0$
> 
> Here $t = 0$ is a genuine solution and still not the answer.
> 
> - It is the instant the particle starts, which the question already told you about
> - The condition $T > 0$ is there precisely to tell you which root to report, so quote it as your reason

### 5((c)) — 4 marks
Displacement is the integral of velocity, so integrate the expression from part (a)

`x = \int \left(\frac{3 t^{2}}{2} - 4 t\right) \textrm{ } \text{d} t`

$x = \frac{t^{3}}{2} - 2 t^{2} + c$

**[M1]**

At $t = 0$ the particle is at `\left(- 10 , 0\right)`, so its displacement from the origin is $- 10$ at that instant

Substituting $t = 0$ leaves $x = c$

$c = - 10$

**[M1]**

$x = \frac{t^{3}}{2} - 2 t^{2} - 10$

Now substitute $t = 3$

$x = \frac{3^{3}}{2} - 2 \times 3^{2} - 10$

**[M1]**

$x = \frac{27}{2} - 18 - 10$

$x = - \frac{29}{2}  \text{m}$

**[A1]**

> **[mark-scheme]**
> **M1**: An acceptable attempt to integrate your expression for $v$, giving at least two terms, with no power of $t$ decreasing. The constant need not be present for this mark.
> 
> **M1**: Correct substitution of $t = 0$ and a position of $- 10$ to find the constant of integration. Seeing $- 10$ anywhere will usually imply this mark, and it is still available if the rearrangement afterwards is wrong.
> 
> **M1**: Substitutes $t = 3$ into your changed expression, using your constant. This mark depends on the first method mark.
> 
> **A1**: $x = - \frac{29}{2}$.
> 
> The answer must be the signed displacement. Giving $\frac{29}{2}$ as a distance does not earn the final mark, and correcting it later does not recover it.

> **[exam-tip]**
> The sign of the answer is the mark here, so do not tidy it away.
> 
> - The official scheme awards nothing for $\frac{29}{2}$ given as a distance
> - Displacement from the origin carries a direction, and $- \frac{29}{2}$ says the particle is $14 . 5$ m on the negative side of it
> 
> A starting point given as coordinates is still just a displacement.
> 
> - `\left(- 10 , 0\right)` on the $x$-axis means $x = - 10$ when $t = 0$
> - That is what fixes the constant of integration, exactly as a plain "$P$ is 10 m from the origin" would
> 
> Notice how far the particle has actually moved.
> 
> - It starts at $- 10$ and is at $- 14 . 5$ after 3 seconds, so it has moved 4.5 m in the negative direction
> - Part (b) showed it is still travelling backwards at $t = 3$, since it does not come to rest until $t = \frac{8}{3}$ and then speeds up again

## Q3 — medium — 10 marks · exam-questions

### 5((a)) — 3 marks
Instantaneously at rest means the velocity is zero at that instant, so set $v = 0$

$3 t^{2} - 16 t + 5 = 0$

Two numbers multiplying to $3 \times 5 = 15$ and adding to $- 16$ are $- 1$ and $- 15$, so split the middle term

$3 t^{2} - 15 t - t + 5 = 0$

`3 t \left(t - 5\right) - 1 \left(t - 5\right) = 0`

`\left(3 t - 1\right)\left(t - 5\right) = 0`

**[M1]**

Both roots satisfy $t \geq 0$, so both are kept

$t = \frac{1}{3}  \text{or}  5$

**[M1] [A1]**

> **[mark-scheme]**
> **M1**: Sets $v = 0$ and makes an acceptable attempt to solve, leading to a value of $t$.
> 
> **M1**: One correct value of $t$.
> 
> **A1**: Both correct values of $t$.
> 
> The last two marks are staged, which is why a single indicator box carries them both against the line holding the two roots: the method mark is earned by either root on its own, and the accuracy mark only once both are correct. Either correct value will imply the first method mark as well, and both correct values will imply all three marks even with no working.
> 
> The quadratic formula and completing the square are equally acceptable in place of factorising. For the first root accept a value rounding to $0 . 33$, or a clear indication that the decimal is 0.3 recurring.

> **[exam-tip]**
> The two marks for the answers here are earned in stages rather than together.
> 
> - One correct root earns the second method mark on its own
> - The accuracy mark needs both, so an answer stopping at $t = 5$ throws away only the last mark rather than two
> 
> Writing $3 t^{2} - 16 t + 5$ as a product is quicker than the formula.
> 
> - The two numbers you need multiply to $15$ and add to $- 16$, and $- 1$ and $- 15$ are easy to spot
> - The formula gives the same marks, so use whichever you trust under pressure

### 5((b)) — 2 marks
Acceleration is the rate of change of velocity, so differentiate and then impose the condition

$a = \frac{\text{d}v}{\text{d}t}$

$a = 6 t - 16$

$6 t - 16 > 0$

**[M1]**

This is a linear inequality, so solve it exactly as you would the equation

$6 t > 16$

$t > \frac{8}{3}$

**[A1]**

> **[mark-scheme]**
> **M1**: An attempt to differentiate $v$, with at least one term correct and no power of $t$ increasing, and their expression set greater than zero. Setting it equal to zero instead is allowed as a concession for this mark.
> 
> **A1**: $t > \frac{8}{3}$, or any equivalent form.
> 
> Accept a decimal rounded to one decimal place or better, such as $2 . 7$, $2 . 67$ or $2 . 667$, or a clear indication of $2 . 6$ recurring with at least three dots.

> **[exam-tip]**
> The answer is a range, so the inequality sign has to survive to the end.
> 
> - The official scheme allows you to write $= 0$ while you work, as a concession
> - It does not allow the final answer to be an equation, so convert back to $>$ before you stop
> 
> Dividing an inequality by a positive number leaves the sign alone.
> 
> - Here you divide by $6$, which is positive, so $>$ stays as $>$
> - Only multiplying or dividing by a negative number reverses it, which is worth checking every time rather than remembering case by case
> 
> There is a quick sense check available from part (a).
> 
> - The velocity is a positive quadratic, so its lowest point is where the acceleration is zero
> - That is $t = \frac{8}{3}$, which sits between the two roots $\frac{1}{3}$ and $5$, exactly as the midpoint of the roots should

### 5((c)) — 5 marks
Distance travelled is not the same as displacement, so first check whether the particle turns round inside the interval

Part (a) found that the velocity is zero only at $t = \frac{1}{3}$ and $t = 5$, and neither of those lies between $1$ and $4$

So the velocity keeps the same sign throughout, and testing one value tells you which sign

$3 \times 2^{2} - 16 \times 2 + 5 = - 15$

The velocity is negative across the whole interval, so the particle moves steadily in one direction

That means the distance is the size of the displacement, and one integral will do

`\int_{1}^{4} \left(3 t^{2} - 16 t + 5\right) \textrm{ } \text{d} t`

**[M1]**

`\left[t^{3} - 8 t^{2} + 5 t\right]_{1}^{4}`

**[A1]**

Substitute the upper limit, then subtract the value at the lower limit

`\left(4^{3} - 8 \times 4^{2} + 5 \times 4\right) - \left(1^{3} - 8 \times 1^{2} + 5 \times 1\right)`

**[M1]**

`\left(- 44\right) - \left(- 2\right) = - 42`

**[A1]**

The negative sign records the direction of travel, and a distance cannot be negative

$\text{distance} = 42  \text{m}$

**[A1]**

> **[mark-scheme]**
> **M1**: An acceptable attempt to integrate the given expression for $v$, with no power of $t$ decreasing. The limits need not be present for this mark.
> 
> **A1**: Correct integration. The limits need not be present for this mark either.
> 
> **M1**: Correct substitution of the limits into your changed expression, which must have at least two terms. If the final answer is wrong, both limits must be seen substituted correctly at least once. A subtraction has to be present, so $- 44$ and $- 2$ on their own do not earn it.
> 
> **A1**: $- 42$, or $42$.
> 
> **A1**: The correct positive distance stated.
> 
> The official scheme is blunt about the method here: a candidate who does not show the step of integration scores zero for the whole part, however good the answer.
> 
> An arbitrary constant may be carried through the working and will cancel in the subtraction, and that is accepted.

> **[exam-tip]**
> Always check for a change of direction before turning a displacement into a distance.
> 
> - The velocity is zero only at $t = \frac{1}{3}$ and $t = 5$, and neither is inside $1 \leq t \leq 4$
> - Had one been inside, the interval would have to be split at it and the two pieces added as positive amounts
> 
> The last two marks are separate, so finish the sentence.
> 
> - One is for reaching $- 42$ and the other for stating the distance as $42$
> - Stopping at $- 42$ leaves a mark on the table, and so does writing $42$ with no sign of where it came from
> 
> There are no marks at all for an answer produced without integrating.
> 
> - The official scheme says a candidate not showing the step of integration scores zero for this part
> - So write the integrated expression down even if your calculator gives you the value directly

## Q4 — medium — 10 marks · exam-questions

### 4((a)) — 2 marks
Acceleration is the rate of change of velocity, so differentiate $v$ with respect to $t$

$a = \frac{\text{d}v}{\text{d}t}$

$a = 4 t - 16$

Now substitute $t = 5$

$a = 4 \times 5 - 16$

**[M1]**

$a = 4  \text{m s}^{-2}$

**[A1]**

> **[mark-scheme]**
> **M1**: An attempt to differentiate the given expression for $v$ and substitute $t = 5$.
> 
> **A1**: $a = 4$.
> 
> An expression with any term integrated rather than differentiated earns nothing, so the method mark is lost if the direction is wrong. The unit is not required.

> **[exam-tip]**
> Differentiate for acceleration and integrate for displacement, every time.
> 
> - The official scheme states that no term may be integrated for the method mark here
> - Writing $a = \frac{\text{d}v}{\text{d}t}$ before you start is a cheap way of committing to the right direction
> 
> Substitute only after differentiating.
> 
> - Putting $t = 5$ into $v$ first gives a number, and the derivative of a number is zero
> - The same trap appears in almost every connected-rates and kinematics question on this paper

### 4((b)) — 8 marks
$M$ and $N$ are where the particle is instantaneously at rest, so start by finding those two times

$2 t^{2} - 16 t + 30 = 0$

Divide through by $2$ to make the factorising easier

$t^{2} - 8 t + 15 = 0$

`\left(t - 3\right)\left(t - 5\right) = 0`

**[M1]**

You are told $t_{2} > t_{1}$, so the smaller root is $t_{1}$

$t_{1} = 3 ,  t_{2} = 5$

**[A1] [A1]**

$M N$ is the distance between the two positions, so integrate the velocity between those times

`\int_{3}^{5} \left(2 t^{2} - 16 t + 30\right) \textrm{ } \text{d} t`

**[M1]**

`\left[\frac{2 t^{3}}{3} - 8 t^{2} + 30 t\right]_{3}^{5}`

**[A1]**

Substitute the upper limit, then subtract the value at the lower limit

`\left(\frac{2 \times 5^{3}}{3} - 8 \times 5^{2} + 30 \times 5\right) - \left(\frac{2 \times 3^{3}}{3} - 8 \times 3^{2} + 30 \times 3\right)`

**[M1]**

$\frac{100}{3} - 36$

$- \frac{8}{3}$

**[A1]**

The velocity does not change sign between $t = 3$ and $t = 5$, so the distance is the size of that displacement

$M N = \frac{8}{3}  \text{m}$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets $v = 0$ and attempts to solve the quadratic by a correct method.
> 
> **A1**: Either $t_{1} = 3$ or $t_{2} = 5$.
> 
> **A1**: Both $t_{1} = 3$ and $t_{2} = 5$.
> 
> **M1**: An attempt to integrate the given expression for $v$, with or without limits. Poor or absent integral notation is ignored, but no term may be differentiated.
> 
> **A1**: The correct integrated expression, simplified or not. A constant of integration is accepted, and the limits are ignored for this mark.
> 
> **M1**: Substitutes your two times into your integrated expression and attempts to evaluate. The subtraction may be either way round.
> 
> **A1**: $- \frac{8}{3}$. The negative value has to be seen for this mark. Accept answers which round to $- 2 . 67$.
> 
> **A1**: The distance $\frac{8}{3}$ m, or an exact equivalent. This mark follows through from your own displacement, but only where that displacement is negative and the final distance positive, so $2 . 67$ is not accepted while $2 . 6$ recurring is.
> 
> The two answer marks near the start are staged, which is why one indicator box carries them both: the first is earned by either time on its own and the second only once both are correct. Solving on a calculator with only $t = 3$ and $t = 5$ seen still earns all three of the opening marks.
> 
> If a final answer of $\frac{8}{3}$ appears with no evidence of algebraic integration, only the last mark is available.

> **[exam-tip]**
> Eight marks for a short answer means almost all of them are for the working.
> 
> - Three are for finding the two times, four for the integration and its evaluation, and one for the final distance
> - An unsupported $\frac{8}{3}$ earns one mark out of eight, which the official scheme states outright
> 
> The negative displacement is worth a mark on its own, so do not hide it.
> 
> - The official scheme says the negative value must be seen before the distance is credited
> - Write $- \frac{8}{3}$ as a line of working, then convert it to a distance in a separate line
> 
> Divide through before factorising when every coefficient shares a factor.
> 
> - $2 t^{2} - 16 t + 30 = 0$ becomes $t^{2} - 8 t + 15 = 0$, which factorises by inspection
> - The velocity itself is unchanged by this, since you are solving an equation rather than rewriting $v$
> 
> Check for a change of direction before calling a displacement a distance.
> 
> - The particle is at rest at both ends of the interval and nowhere in between, so it travels one way throughout
> - That is what makes $M N$ equal to the size of the displacement here, rather than a sum of two pieces

## Q5 — medium — 7 marks · exam-questions

### 3() — 4 marks
**(i)**

Velocity is the integral of acceleration with respect to time

`v = \int \left(6 t - 16\right) \textrm{ } \text{d} t`

$v = 3 t^{2} - 16 t + c$

**[M1]**

The velocity is $12  \text{m s}^{-1}$ when $t = 0$, and substituting $t = 0$ leaves $v = c$

$c = 12$

$v = 3 t^{2} - 16 t + 12$

**[A1]**

**(ii)**

Displacement is the integral of velocity, so integrate the expression just found

`s = \int \left(3 t^{2} - 16 t + 12\right) \textrm{ } \text{d} t`

$s = t^{3} - 8 t^{2} + 12 t + k$

**[M1]**

$P$ is at the origin when $t = 0$, so $s = 0$ there, and substituting $t = 0$ leaves $s = k$

$k = 0$

$s = t^{3} - 8 t^{2} + 12 t$

**[A1]**

> **[mark-scheme]**
> **M1**: Integrates the given expression for $a$, with no term differentiated. The constant of integration is not required for this mark.
> 
> **A1**: Finds the value of the constant and gives the correct expression for $v$.
> 
> **M1**: An acceptable attempt to integrate your expression for $v$, with no term differentiated. The second constant is not required for this mark.
> 
> **A1**: The correct expression for the displacement.
> 
> The official scheme is unusually strict about the final mark: the expression for the displacement must come from explicitly establishing that the second constant is zero, and without that constant appearing in your integration the mark is automatically lost, even though its value turns out to be zero.

> **[exam-tip]**
> A constant of integration that turns out to be zero still has to be written down.
> 
> - The official scheme says that without $+ k$ in your integration the final mark is automatically lost
> - Write the constant in, then show the line that makes it zero, rather than leaving it out because you can see it will vanish
> 
> Each integration needs its own constant and its own condition.
> 
> - The first uses the velocity of $12  \text{m s}^{-1}$ at $t = 0$ to give $c = 12$
> - The second uses the particle being at the origin at $t = 0$ to give $k = 0$
> 
> Use different letters for the two constants.
> 
> - Reusing $c$ makes it look as though the same constant has two values
> - The official scheme itself writes $c$ and then $k$, which is worth copying

### 3((b)) — 3 marks
At the origin the displacement is zero, so set the expression from part (a) equal to zero

$t^{3} - 8 t^{2} + 12 t = 0$

**[M1]**

Every term has a factor of $t$, so take it out rather than trying to solve a cubic directly

`t \left(t^{2} - 8 t + 12\right) = 0`

Two numbers multiplying to $12$ and adding to $- 8$ are $- 2$ and $- 6$

`t \left(t - 2\right) \left(t - 6\right) = 0`

**[M1]**

$t = 0  ,  2  \text{or}  6$

$t = 0$ is the instant the particle sets off from the origin, so the first return is the next root

$t = 2  \text{seconds}$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets your expression for $s$, which must be a cubic, equal to zero.
> 
> **M1**: Solves the cubic. A minimally acceptable attempt takes out the factor of $t$ and reaches two brackets whose constants multiply to $12$. This mark depends on the previous method mark.
> 
> **A1**: $t = 2$, explicitly stated.
> 
> Because the candidate is told that one value is $t = 0$, factorising straight to two brackets is also accepted. Any method of solving the resulting quadratic is acceptable, including the formula and completing the square.
> 
> Where no working is seen and either the times or the expression for $s$ is wrong, the second method mark is given only if a correct method for solving the equation is seen.

> **[exam-tip]**
> "Returns to the origin" means the displacement is zero again, not the velocity.
> 
> - Set $s = 0$, not $v = 0$
> - The velocity being zero would tell you when the particle turns round, which happens at a different time
> 
> The word "first" is doing real work in this question.
> 
> - The cubic has roots $0$, $2$ and $6$, and all three are valid times
> - $t = 0$ is the start rather than a return, and $t = 6$ is the second return, so the answer is $t = 2$
> 
> A cubic with no constant term is really a quadratic in disguise.
> 
> - Take out the common factor of $t$ first and the rest factorises by inspection
> - The official scheme accepts going straight to the two brackets, because the question has already told you that $t = 0$ is one of the roots
