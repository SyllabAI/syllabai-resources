# Mark Schemes — Differential Equations
**Integration** · Cambridge (CIE) A-LEVEL maths (9709)


## Exam Questions (27 questions)


### Q1
(i)

Inversely proportional to the volume means the rate of change equals a constant divided by $V$

$\frac{\text{d}V}{\text{d}t} = \frac{k}{V}$

**[B1]**

(ii)

Substitute the given rate and the given volume into the differential equation

$10 = \frac{k}{20}$

**[M1]**

Multiply both sides by 20

$k = 200$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct differential equation. The constant may be given any letter, but it must appear in the numerator over $V$; writing $\frac{\text{d}V}{\text{d}t} = k V$ describes direct proportion and does not earn this mark.
> 
> **M1**: Substitution of the rate 10 and the volume 20 into a differential equation of the form $\frac{\text{d}V}{\text{d}t} = \frac{k}{V}$.
> 
> **A1**: Correct constant of proportionality.
Using the constant found in part (a), the differential equation is $\frac{\text{d}V}{\text{d}t} = \frac{200}{V}$, so separate the variables by multiplying both sides by $V$

$V \frac{\text{d}V}{\text{d}t} = 200$

Integrate each side with respect to $t$

`\int V\dfrac{\text{d}V}{\text{d}t} \; \text{d}t = \int 200 \; \text{d}t`

$\frac{\text{d}V}{\text{d}t}  \text{d} t$ becomes $\text{d} V$

`\int V \; \text{d}V = \int 200 \; \text{d}t`

**[M1]**

Integrate each side, calling the constant of integration $c_{0}$ so that it can be adjusted at the end

$\frac{V^{2}}{2} = 200 t + c_{0}$

**[A1]**

Multiply through by 2 to clear the fraction

$V^{2} = 400 t + 2 c_{0}$

Since $2 c_{0}$ is itself just a constant, write it as $c$

$V^{2} = 400 t + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with $V$ on one side and the constant on the other, and an attempt to integrate at least one side.
> 
> **A1**: Correct integrated equation $\frac{V^{2}}{2} = 200 t + c_{0}$, with a constant of integration present.
> 
> **A1**: The given result reached, with the doubling of the constant handled correctly. Writing the constant as $c$ from the start and leaving it unchanged through the multiplication by 2 does not earn this mark, because the two constants are not the same.
(i)

Stored flat initially means $V = 0$ when $t = 0$, so substitute both values into the general solution

`0^{2} = 400\left(0\right) + c`

$c = 0$

$V^{2} = 400 t$

**[B1]**

(ii)

Substitute $t = 25$ into the particular solution

`V^{2} = 400\left(25\right)`

$V^{2} = 10000$

**[M1]**

Take the positive square root, since a volume cannot be negative

$V = 100 \text{m}^{3}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct particular solution. The equivalent form $V = 20 \sqrt{t}$ is also accepted.
> 
> **M1**: Substitution of $t = 25$ into their particular solution.
> 
> **A1**: Correct volume. The units are not required for this mark, but a negative root does not earn it.

### Q2
Water is leaking out, so the volume is falling and the rate of change must be negative

**Final answer:** **The negative sign makes the right hand side negative, so the volume decreases over time**

Since $V$ is a volume it is positive, so for $- k V$ to be negative the constant itself must be positive

**Final answer:** **This means **$k$** is positive**

**[B1]**

> **[mark-scheme]**
> **B1**: Both ideas needed: that the negative sign makes the rate of change negative because the volume is decreasing, and that $k$ is therefore positive. Stating only that $k > 0$ without explaining the sign does not earn this mark.
Separate the variables by dividing both sides by $V$, which is allowed because the volume is positive

$\frac{1}{V} \frac{\text{d}V}{\text{d}t} = - k$

Integrate each side with respect to $t$

`\int \dfrac{1}{V}\dfrac{\text{d}V}{\text{d}t} \; \text{d}t = \int -k \; \text{d}t`

$\frac{\text{d}V}{\text{d}t}  \text{d} t$ becomes $\text{d} V$, and the constant comes outside the integral on the right

`\int \dfrac{1}{V} \; \text{d}V = -k \int \text{d}t`

**[B1]**

Now integrate each side, using the result that `\int \dfrac{1}{V} \; \text{d}V = \text{ln} \left| V \right|`

`\text{ln} \left| V \right| = -kt + c`

**[M1]**

The volume is positive, so the modulus signs can be dropped, and taking exponentials of both sides makes $V$ the subject

$V = \text{e}^{-kt+c}$

Split the exponential using the law of indices $a^{m} \times a^{n} = a^{m+n}$

$V = \text{e}^{-kt} \times \text{e}^{c}$

Since $\text{e}^{c}$ is just a constant, write it as $A$

$V = A \text{e}^{-kt}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct separation of the variables reaching the given form. Because the result is printed, the working must show how it was obtained.
> 
> **M1**: Integration of both sides, with a constant of integration on one side. $\text{ln}  V$ without the modulus signs is condoned.
> 
> **A1**: Correct general solution in the form $V = A \text{e}^{-kt}$. An equivalent such as $V = \text{e}^{-kt+c}$ is accepted provided the constant has been correctly carried through.
Initial means at $t = 0$, so substitute $t = 0$ and $V = 300$ into the general solution from part (b)

`300 = A\text{e}^{-k \left(0\right)}`

Any number raised to the power zero is 1, so the constant is the initial volume

$A = 300$

**[M1]**

Substitute this constant and the given value $k = 0 . 02$ into the general solution

$V = 300 \text{e}^{-0.02t}$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitution of $t = 0$ and $V = 300$ into a general solution of the form $V = A \text{e}^{-kt}$, and a correct method to find the constant.
> 
> **A1**: Correct final answer with $V$ as the subject. Both the constant 300 and the value $- 0 . 02$ in the exponent are needed.

### Q3
Each variable already sits with its own differential, so write an integral sign on each side

`\int \text{d}x = \int \left(9t^{2} + 4t\right) \text{d}t`

Integrate each side, raising each power by one and dividing by the new power

$x = \frac{9t^{3}}{3} + \frac{4t^{2}}{2} + c$

**[M1]**

Simplify each coefficient

$x = 3 t^{3} + 2 t^{2} + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Integration of at least one term, raising the power by one and dividing by the new power.
> 
> **A1**: Correct solution with both coefficients simplified. Unsimplified equivalents such as $\frac{9t^{3}}{3}$ are accepted, but the constant of integration must be present or this mark is lost.
Each side involves only one variable, so write an integral sign on each side

`\int \text{d}S = \int 4\text{e}^{2x} \; \text{d}x`

Integrate, dividing by the coefficient of $x$ in the exponent

$S = \frac{4\text{e}^{2x}}{2} + c$

**[M1]**

Simplify the coefficient

$S = 2 \text{e}^{2x} + c$

The solution is only particular once the constant is known, so substitute $x = 0$ and $S = 5$

$5 = 2 \text{e}^{0} + c$

Any number raised to the power zero is 1

$5 = 2 + c$

Rearrange for the constant

$c = 3$

**[M1]**

Substitute the constant back into the solution

$S = 2 \text{e}^{2x} + 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct integration to an expression of the form $k \text{e}^{2x} + c$, with the constant of integration present.
> 
> **M1**: Substitution of $x = 0$ and $S = 5$ into an integrated expression containing a constant, and a correct method to find that constant.
> 
> **A1**: Correct final answer, written explicitly with $S$ as the subject. An implicit form such as $S - 2 \text{e}^{2x} = 3$ does not earn this mark. Unsimplified equivalents such as $\frac{4}{2} \text{e}^{2x} + 3$ are accepted.

### Q4
The variables are already grouped, with $y$ on the left and $x$ on the right, so integrate each side with respect to $x$

`\int \dfrac{1}{y - 1}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int 6x^{2} \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{1}{y - 1} \; \text{d}y = \int 6x^{2} \; \text{d}x`

Integrate each side, using the result that `\int \dfrac{1}{y - 1} \; \text{d}y = \text{ln}\left|y - 1\right|`

`\text{ln}\left|y - 1\right| = \dfrac{6x^{3}}{3} + c`

**[M1]**

Simplify the coefficient on the right

`\text{ln}\left|y - 1\right| = 2x^{3} + c`

The question states $y > 1$, so $y - 1$ is positive and the modulus signs can be dropped

`\text{ln}\left(y - 1\right) = 2x^{3} + c`

**[A1]**

Take exponentials of both sides

$y - 1 = \text{e}^{2x^{3}+c}$

Split the exponential using the law of indices $a^{m} \times a^{n} = a^{m+n}$

$y - 1 = \text{e}^{2x^{3}} \times \text{e}^{c}$

Since $\text{e}^{c}$ is a constant, write it as $A$

$y - 1 = A \text{e}^{2x^{3}}$

Add 1 to both sides to reach the required form

$y = A \text{e}^{2x^{3}} + 1$

**[A1]**

> **[mark-scheme]**
> **M1**: Integration of both sides to obtain a logarithm on the left and a cubic term on the right, with a constant of integration included.
> 
> **A1**: Correct integrated equation `\text{ln}\left(y - 1\right) = 2x^{3} + c`. The modulus signs may be kept or dropped, and the unsimplified $\frac{6x^{3}}{3}$ is accepted.
> 
> **A1**: Correct final answer in the required form. The exponential must be split correctly so that the constant multiplies $\text{e}^{2x^{3}}$ rather than sitting in the exponent.
Separate the variables by dividing both sides by $y + 2$, which is positive because $y > - 2$

$\frac{1}{y+2} \frac{\text{d}y}{\text{d}x} = 9 x^{\frac{1}{2}}$

Integrate each side with respect to $x$

`\int \dfrac{1}{y + 2}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int 9x^{\frac{1}{2}} \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{1}{y + 2} \; \text{d}y = \int 9x^{\frac{1}{2}} \; \text{d}x`

Integrate each side, raising the power of $x$ by one and dividing by the new power

`\text{ln}\left|y + 2\right| = \dfrac{9x^{\frac{3}{2}}}{\frac{3}{2}} + c`

**[M1]**

Dividing by $\frac{3}{2}$ is the same as multiplying by $\frac{2}{3}$

`\text{ln}\left|y + 2\right| = 6x^{\frac{3}{2}} + c`

Since $y > - 2$, the quantity $y + 2$ is positive and the modulus signs can be dropped

`\text{ln}\left(y + 2\right) = 6x^{\frac{3}{2}} + c`

**[A1]**

Take exponentials of both sides

$y + 2 = \text{e}^{6x^{\frac{3}{2}}+c}$

Split the exponential using the law of indices $a^{m} \times a^{n} = a^{m+n}$

$y + 2 = \text{e}^{6x^{\frac{3}{2}}} \times \text{e}^{c}$

Since $\text{e}^{c}$ is a constant, write it as $A$

$y + 2 = A \text{e}^{6x^{\frac{3}{2}}}$

Subtract 2 from both sides to reach the required form

$y = A \text{e}^{6x^{\frac{3}{2}}} - 2$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables and integration of both sides, with a constant of integration included.
> 
> **A1**: Correct integrated equation `\text{ln}\left(y + 2\right) = 6x^{\frac{3}{2}} + c`. The modulus signs may be kept or dropped, and the unsimplified $\frac{9x^{\frac{3}{2}}}{\frac{3}{2}}$ is accepted.
> 
> **A1**: Correct final answer in the required form, with the constant multiplying the exponential.

### Q5
Divide both sides by $y$, which is allowed because $y > 0$

$\frac{1}{y} \frac{\text{d}y}{\text{d}x} = 2 x$

**[M1]**

Integrate each side with respect to $x$

`\int \dfrac{1}{y}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int 2x \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{1}{y} \; \text{d}y = \int 2x \; \text{d}x`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the $y$ terms on the left and the $x$ terms on the right.
> 
> **A1**: The given result reached correctly. Because the answer is printed in the question, your working must show the integral signs being introduced, not just the separated equation.
Integrate each side, using the result that `\int \dfrac{1}{y} \; \text{d}y = \text{ln} \left| y \right|`

`\text{ln} \left| y \right| = \dfrac{2x^{2}}{2} + c`

**[M1]**

Simplify the coefficient on the right

`\text{ln} \left| y \right| = x^{2} + c`

The question states $y > 0$, so the modulus signs can be dropped

$\text{ln}  y = x^{2} + c$

**[A1]**

Take exponentials of both sides to make $y$ the subject

$\text{e}^{\text{ln}y} = \text{e}^{x^{2}+c}$

The exponential and the natural logarithm are inverse functions, so the left side is simply $y$

$y = \text{e}^{x^{2}+c}$

**[A1]**

> **[mark-scheme]**
> **M1**: Integration of both sides, with a constant of integration included on one side.
> 
> **A1**: Correct integrated equation. Either `\text{ln} \left| y \right| = x^{2} + c` or $\text{ln}  y = x^{2} + c$ is accepted, and the unsimplified $\frac{2x^{2}}{2}$ is also accepted.
> 
> **A1**: Correct use of exponentials on both sides to reach the given result. Since the answer is printed, this step must be visible.
Use the law of indices $a^{m} \times a^{n} = a^{m+n}$ in reverse to split the exponential into two factors

$y = \text{e}^{x^{2}} \times \text{e}^{c}$

**[M1]**

Replace $\text{e}^{c}$ by $A$, as the question directs

$y = A \text{e}^{x^{2}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the law of indices to write the exponential as a product of $\text{e}^{x^{2}}$ and $\text{e}^{c}$.
> 
> **A1**: The substitution $A = \text{e}^{c}$ made and the given result reached.

### Q6
Multiply both sides by $\text{e}^{kt}$ to make the derivative the subject, remembering that $\frac{1}{\text{e}^{-kt}} = \text{e}^{kt}$

$\frac{\text{d}N}{\text{d}t} = \frac{2}{5} \text{e}^{kt}$

Multiply both sides by 5 to clear the fraction

$5 \frac{\text{d}N}{\text{d}t} = 2 \text{e}^{kt}$

**[M1]**

Integrate each side with respect to $t$

`\int 5\dfrac{\text{d}N}{\text{d}t} \; \text{d}t = \int 2\text{e}^{kt} \; \text{d}t`

$\frac{\text{d}N}{\text{d}t}  \text{d} t$ becomes $\text{d} N$

`\int 5 \; \text{d}N = \int 2\text{e}^{kt} \; \text{d}t`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct rearrangement so that the variables are separated, with the exponential moved to the right hand side.
> 
> **A1**: The given result reached, with an integral sign introduced on each side. Because the answer is printed, this step must be visible.
Integrate each side, dividing by the coefficient of $t$ in the exponent, and call the constant of integration $c_{0}$ so that it can be adjusted at the end

$5 N = \frac{2\text{e}^{kt}}{k} + c_{0}$

**[M1]**

Divide every term by 5

$N = \frac{2\text{e}^{kt}}{5k} + \frac{c_{0}}{5}$

Since $\frac{c_{0}}{5}$ is itself just a constant, write it as $c$

$N = \frac{2\text{e}^{kt}}{5k} + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct integration of both sides, with the exponential divided by $k$ and a constant of integration present.
> 
> **A1**: The given result reached, with the division of the constant by 5 handled correctly.
Substitute $k = 0 . 1$ into the general solution from part (b)

$N = \frac{2\text{e}^{0.1t}}{5\times0.1} + c$

The denominator is 0.5, and dividing by 0.5 is the same as multiplying by 2

$N = 4 \text{e}^{0.1t} + c$

**[M1]**

Four trees were infected when the disease was discovered, so $N = 4$ when $t = 0$

$4 = 4 \text{e}^{0} + c$

Any number raised to the power zero is 1

$4 = 4 + c$

$c = 0$

**[M1]**

Substitute the constant back into the solution

$N = 4 \text{e}^{0.1t}$

**[A1]**

To estimate the number of infected trees after 30 days, substitute $t = 30$

$N = 4 \text{e}^{0.1\times30}$

$N = 4 \text{e}^{3} = 80 . 342 \dots$

A number of trees must be a whole number

**Final answer:** **About 80 trees are infected after 30 days**

**[A1]**

> **[mark-scheme]**
> **M1**: Substitution of $k = 0 . 1$ into the general solution and correct simplification of the coefficient to 4.
> 
> **M1**: Use of $N = 4$ when $t = 0$ in an expression containing a constant, and a correct method to find that constant.
> 
> **A1**: Correct particular solution with $N$ as the subject.
> 
> **A1**: Correct estimate. The unrounded value 80.342 must be rounded down to a whole number of trees, so 80 is required; answers of 80.3 or 80.34 do not earn this mark because the model is counting trees.

### Q7
The right hand side depends only on $x$, so the equation can be integrated directly, and $\text{sec}^{2}  x$ is the derivative of $\text{tan}  x$

`y = \int \text{sec}^{2} \; x \; \text{d}x`

**[M1]**

$y = \text{tan}  x + c$

**[A1]**

To find the constant, substitute $x = \frac{π}{3}$ and $y = 2 \sqrt{3}$

`2\sqrt{3} = \text{tan}\left(\dfrac{\pi}{3}\right) + c`

Use the exact value `\text{tan}\left(\dfrac{\pi}{3}\right) = \sqrt{3}`

$2 \sqrt{3} = \sqrt{3} + c$

**[M1]**

Subtract $\sqrt{3}$ from both sides

$c = \sqrt{3}$

Substitute the constant back into the solution

$y = \sqrt{3} + \text{tan}  x$

**[A1]**

> **[mark-scheme]**
> **M1**: Recognition that the equation integrates directly, with an attempt at `\int \text{sec}^{2} \; x \; \text{d}x`.
> 
> **A1**: Correct integration to $y = \text{tan}  x + c$, with the constant of integration present.
> 
> **M1**: Substitution of $x = \frac{π}{3}$ and $y = 2 \sqrt{3}$ into an integrated expression containing a constant, together with the correct exact value for `\text{tan}\left(\dfrac{\pi}{3}\right)`.
> 
> **A1**: Correct final answer with $y$ as the subject. The order of the two terms does not matter, so $y = \text{tan}  x + \sqrt{3}$ is equally acceptable. A decimal such as 1.73 in place of $\sqrt{3}$ does not earn this mark, because the boundary values are exact.
Use the definitions $\text{sec}  x = \frac{1}{\text{cos}x}$ and $\text{cosec}  y = \frac{1}{\text{sin}y}$ to write the equation in terms of sine and cosine

$\frac{1}{\text{cos}x} \frac{\text{d}y}{\text{d}x} = \frac{1}{\text{sin}y}$

Multiply both sides by $\text{sin}  y$ and by $\text{cos}  x$ to gather each variable on its own side

$\text{sin}  y \frac{\text{d}y}{\text{d}x} = \text{cos}  x$

**[M1]**

Integrate each side with respect to $x$

`\int \text{sin} \; y \dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int \text{cos} \; x \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \text{sin} \; y \; \text{d}y = \int \text{cos} \; x \; \text{d}x`

**[A1]**

Integrate each side, remembering that the integral of sine carries a negative sign

$- \text{cos}  y = \text{sin}  x + c$

**[A1]**

To find the constant, substitute $x = 0$ and $y = \frac{π}{2}$

`-\text{cos}\left(\dfrac{\pi}{2}\right) = \text{sin}\left(0\right) + c`

Both of these trigonometric values are 0

$0 = 0 + c$

$c = 0$

**[M1]**

Substitute the constant back into the integrated equation

$- \text{cos}  y = \text{sin}  x$

Multiply through by $- 1$ to reach the required form

$\text{cos}  y = - \text{sin}  x$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the reciprocal trigonometric definitions to reach an equation in sine and cosine, with the variables separated.
> 
> **A1**: Correct separated form with an integral sign on each side.
> 
> **A1**: Correct integration of both sides, including the negative sign on $\text{cos}  y$ and a constant of integration.
> 
> **M1**: Substitution of $x = 0$ and $y = \frac{π}{2}$ into an integrated expression containing a constant, and a correct method to find that constant.
> 
> **A1**: Correct final answer in the required form. An answer left as $- \text{cos}  y = \text{sin}  x$ does not earn this mark, because the question asks for $\text{cos}  y$ as the subject.

### Q8
Rearrange to make the derivative the subject, dividing through by 2

$\frac{\text{d}x}{\text{d}t} = - \frac{1}{4} \text{sec}^{2}  3 t$

Integrate, using `\int \text{sec}^{2} \; \theta \; \text{d}\theta = \text{tan} \; \theta` and dividing by the coefficient of $t$ in the argument

$x = - \frac{1}{12} \text{tan}  3 t + c$

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Correct rearrangement to make $\frac{\text{d}x}{\text{d}t}$ the subject, followed by an attempt to integrate a secant squared term to a tangent.
> 
> **A1**: Fully correct solution, including both the factor of $\frac{1}{4}$ from the rearrangement and the $\frac{1}{3}$ from the argument, with the constant of integration present.
Rearrange to make the derivative the subject

$\frac{\text{d}V}{\text{d}x} = \frac{2}{3} x \text{e}^{4x} - \frac{1}{3}$

**[M1]**

Integrate term by term. The constant term is straightforward, but $x \text{e}^{4x}$ is a product of two functions, so it needs integration by parts

`V = -\dfrac{1}{3}x + \dfrac{2}{3}\int x\text{e}^{4x} \; \text{d}x`

Quote the formula for integration by parts before using it

`\int u\dfrac{\text{d}v}{\text{d}x} \; \text{d}x = uv - \int v\dfrac{\text{d}u}{\text{d}x} \; \text{d}x`

Choose $u = x$, so that differentiating it removes the $x$ entirely

$u = x ,  \frac{\text{d}v}{\text{d}x} = \text{e}^{4x}$

$\frac{\text{d}u}{\text{d}x} = 1 ,  v = \frac{1}{4} \text{e}^{4x}$

**[M1]**

Substitute into the formula

`\int x\text{e}^{4x} \; \text{d}x = \dfrac{1}{4}x\text{e}^{4x} - \int \dfrac{1}{4}\text{e}^{4x} \; \text{d}x`

$= \frac{1}{4} x \text{e}^{4x} - \frac{1}{16} \text{e}^{4x}$

**[A1]**

Substitute this back and multiply through by $\frac{2}{3}$

$V = - \frac{1}{3} x + \frac{1}{6} x \text{e}^{4x} - \frac{1}{24} \text{e}^{4x} + c$

**[A1]**

To find the constant, substitute $x = 0$ and $V = 2$

$2 = - \frac{1}{24} \text{e}^{0} + c$

$c = 2 + \frac{1}{24} = \frac{49}{24}$

**[M1]**

Substitute the constant back and write the answer over a common denominator of 24

`V = \dfrac{\left(4x - 1\right)\text{e}^{4x} - 8x + 49}{24}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct rearrangement to make $\frac{\text{d}V}{\text{d}x}$ the subject, with both terms divided by 3.
> 
> **M1**: Integration by parts attempted on $x \text{e}^{4x}$, with $u = x$ and $\frac{\text{d}v}{\text{d}x} = \text{e}^{4x}$ or equivalent. Choosing $u$ and $v$ the other way round does not lead anywhere and does not earn this mark.
> 
> **A1**: Correct result of the integration by parts, including the factor of $\frac{1}{16}$ on the second term.
> 
> **A1**: Correct general solution with all three terms and a constant of integration present.
> 
> **M1**: Substitution of $x = 0$ and $V = 2$ into an integrated expression containing a constant, and a correct method to find that constant.
> 
> **A1**: Correct final answer with $V$ as the subject. The expanded form $V = \frac{1}{6} x \text{e}^{4x} - \frac{1}{24} \text{e}^{4x} - \frac{1}{3} x + \frac{49}{24}$ is equally acceptable; there is no requirement to write it over a common denominator.

### Q9
Separate the variables by dividing both sides by `N\left(N - 1\right)`, which is positive because $N > 1$

`\dfrac{1}{N\left(N - 1\right)}\dfrac{\text{d}N}{\text{d}t} = k`

Integrate each side with respect to $t$

`\int \dfrac{1}{N\left(N - 1\right)}\dfrac{\text{d}N}{\text{d}t} \; \text{d}t = \int k \; \text{d}t`

$\frac{\text{d}N}{\text{d}t}  \text{d} t$ becomes $\text{d} N$

`\int \dfrac{1}{N\left(N - 1\right)} \; \text{d}N = \int k \; \text{d}t`

**[M1]**

The denominator is a product of two linear factors, so split the fraction into partial fractions

`\dfrac{1}{N\left(N - 1\right)} = \dfrac{1}{N - 1} - \dfrac{1}{N}`

**[M1 A1]**

Integrate each side, taking each term on the left to a logarithm

`\text{ln}\left(N - 1\right) - \text{ln} \; N = kt + c`

Combine the two logarithms using `\text{ln} \; a - \text{ln} \; b = \text{ln}\left(\dfrac{a}{b}\right)`. Both $N$ and $N - 1$ are positive, so no modulus signs are needed

`\text{ln}\left(\dfrac{N - 1}{N}\right) = kt + c`

**[A1]**

Take exponentials of both sides and split using the law of indices, writing $\text{e}^{c}$ as $A$. Since $\text{e}^{c}$ is positive for every value of $c$, the constant $A$ is positive

$\frac{N-1}{N} = A \text{e}^{kt}$

**[M1]**

Multiply through by $N$ and collect the $N$ terms on one side

$N - 1 = N A \text{e}^{kt}$

`N\left(1 - A\text{e}^{kt}\right) = 1`

Divide both sides by the bracket

$N = \frac{1}{1-A\text{e}^{kt}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the $N$ terms on one side and the constant on the other.
> 
> **M1**: A correct method seen or implied for splitting into partial fractions. The form is not given in the question, so selecting it is part of the method.
> 
> **A1**: The correct decomposition $\frac{1}{N-1} - \frac{1}{N}$.
> 
> **A1**: Correct integration of both sides and combination into a single logarithm, with a constant of integration present.
> 
> **M1**: Correct use of exponentials, with the constant written as a multiplier.
> 
> **A1**: The given result reached, with $N$ correctly collected and factorised out. Because the answer is printed, the rearrangement must be visible. An explanation of why $A$ is positive is not required for this mark but is good practice.
Initially means $t = 0$, when $N = 2$, so substitute both values into the general solution

$2 = \frac{1}{1-A\text{e}^{0}}$

Take the reciprocal of both sides and rearrange

$1 - A = \frac{1}{2}$

$A = \frac{1}{2}$

**[B1]**

A fortnight is 14 days, so substitute $t = 14$ and $N = 4$

$4 = \frac{1}{1-\frac{1}{2}\text{e}^{14k}}$

Take the reciprocal of both sides and rearrange for the exponential

$1 - \frac{1}{2} \text{e}^{14k} = \frac{1}{4}$

$\text{e}^{14k} = \frac{3}{2}$

**[M1]**

Take natural logarithms of both sides

`k = \dfrac{1}{14}\text{ln}\left(\dfrac{3}{2}\right)`

**[A1]**

> **[mark-scheme]**
> **B1**: Correct value of $A$, obtained by using $N = 2$ when $t = 0$.
> 
> **M1**: Use of $N = 4$ when $t = 14$ in the general solution, and a correct method reaching an exponential on its own. Using $t = 2$ for a fortnight does not earn this mark.
> 
> **A1**: Correct value of $k$. The decimal equivalent 0.0290, or answers which round to it, is accepted.
The solution is a fraction, so it fails where its denominator does. If $1 - A \text{e}^{kt} = 0$ then $N$ is undefined, and if $1 - A \text{e}^{kt} < 0$ then $N$ is negative, which is impossible for a number of trees

$1 - A \text{e}^{kt} > 0$

Rearrange for the exponential, then take natural logarithms of both sides, which preserves the direction because every step uses a positive quantity

$\text{e}^{kt} < \frac{1}{A}$

`t < \dfrac{1}{k}\text{ln}\left(\dfrac{1}{A}\right)`

**[M1]**

Substitute $A = \frac{1}{2}$ and `k = \dfrac{1}{14}\text{ln}\left(\dfrac{3}{2}\right)` from part (b)

`t < \dfrac{14\,\text{ln}\left(2\right)}{\text{ln}\left(\dfrac{3}{2}\right)} = 23.93\ldots`

**[M1]**

Only whole days are meaningful here, and the model breaks down before 23.9 days is reached

**Final answer:** **The model might be considered reliable for values of **$t$** between 0 and 23 days**

**[A1]**

> **[mark-scheme]**
> **M1**: Recognition that the denominator must stay positive for $N$ to be a sensible number of trees, leading to the inequality $1 - A \text{e}^{kt} > 0$ or equivalent.
> 
> **M1**: The values of $A$ and $k$ from part (b) substituted, and logarithms used correctly to reach a numerical bound on $t$.
> 
> **A1**: A correct range stated. Answers of $0 \leq t < 23 . 9$ days, or between 0 and 23 whole days, both earn this mark. A bare value of 23.9 with no range and no reference to the model does not, because the question asks for a range of values for which the model is reliable.

### Q10
The rate of cooling is proportional to the difference between the two temperatures, and the object is cooling, so the rate of change is negative

`\dfrac{\text{d}T}{\text{d}t} = -k\left(T - T_{amb}\right)`

**[M1]**

Separate the variables by dividing both sides by $T - T_{amb}$, which is positive because the object is warmer than its surroundings

$\frac{1}{T-T_{amb}} \frac{\text{d}T}{\text{d}t} = - k$

**[M1]**

Integrate each side with respect to $t$

`\int \dfrac{1}{T - T_{amb}}\dfrac{\text{d}T}{\text{d}t} \; \text{d}t = \int -k \; \text{d}t`

$\frac{\text{d}T}{\text{d}t}  \text{d} t$ becomes $\text{d} T$

`\int \dfrac{1}{T - T_{amb}} \; \text{d}T = \int -k \; \text{d}t`

**[A1]**

Integrate each side. The ambient temperature is constant, so differentiating $T - T_{amb}$ gives 1 and no compensating factor is needed

`\text{ln}\left(T - T_{amb}\right) = -kt + c`

**[A1]**

Take exponentials of both sides, then split using the law of indices $a^{m} \times a^{n} = a^{m+n}$

$T - T_{amb} = \text{e}^{-kt} \times \text{e}^{c}$

Since $\text{e}^{c}$ is a constant, write it as $A$

$T - T_{amb} = A \text{e}^{-kt}$

**[M1]**

Add the ambient temperature to both sides

$T = T_{amb} + A \text{e}^{-kt}$

**[A1]**

> **[mark-scheme]**
> **M1**: A differential equation with the rate of change proportional to the difference $T - T_{amb}$, including the negative sign. Writing $\frac{\text{d}T}{\text{d}t} = - k T$ uses the temperature rather than the difference and does not earn this mark.
> 
> **M1**: Correct separation of the variables.
> 
> **A1**: Correct separated form with an integral sign on each side.
> 
> **A1**: Correct integration of both sides, with a constant of integration present. The modulus signs are condoned if included.
> 
> **M1**: Correct use of exponentials, with the exponential split so that the constant becomes a multiplier.
> 
> **A1**: The given result reached. Because the answer is printed, the step turning $\text{e}^{c}$ into $A$ must be visible.
The freezer is the surroundings, so the ambient temperature is −4, and the general solution from part (a) becomes

$T = - 4 + A \text{e}^{-kt}$

The product enters the freezer at 7 °C, so $T = 7$ when $t = 0$

$7 = - 4 + A \text{e}^{0}$

$A = 11$

**[M1]**

One minute later the temperature is 4.7 °C, so substitute $T = 4 . 7$ and $t = 1$

$4 . 7 = - 4 + 11 \text{e}^{-k}$

Rearrange to isolate the exponential

$\text{e}^{-k} = \frac{8.7}{11}$

Take natural logarithms of both sides

`k = \text{ln}\left(\dfrac{11}{8.7}\right) = 0.2345722\ldots`

**[M1]**

The policy allows 6 minutes, so substitute $t = 6$ using the unrounded value of $k$

$T = - 4 + 11 \text{e}^{-6\times0.2345722\dots}$

$T = - 1 . 3075 \dots$

$T = - 1 . 31$* °C (3 s.f.)*

**[A1]**

Compare this with the threshold, since the product must be below −1 °C after 6 minutes

**Final answer:** **After 6 minutes the temperature is below −1 °C, so the product will not need to be discarded**

**[A1]**

> **[mark-scheme]**
> **M1**: Use of the ambient temperature −4 together with $T = 7$ when $t = 0$ to find the constant $A$.
> 
> **M1**: Use of $T = 4 . 7$ when $t = 1$ together with logarithms to find $k$. Taking logarithms of both sides must be visible.
> 
> **A1**: Correct temperature after 6 minutes, or answers which round to −1.31 °C. Rounding $k$ before substituting risks losing this mark, because the answer sits close to the threshold.
> 
> **A1**: Correct verdict with the comparison made explicit. Stating that the product is not discarded without comparing the temperature to −1 °C does not earn this mark. An alternative method finding the time to reach −1 °C, which is 5.54 minutes, and comparing that with 6 minutes is equally acceptable.

### Q11
(i)

Define the variables before writing anything down, since the answer depends on the units chosen

*Let V be the volume of water, in litres, at time t minutes*

**[B1]**

The rate of change is proportional to the square of the volume, and the container is leaking, so the rate is negative, where $k$ is a positive constant

$\frac{\text{d}V}{\text{d}t} = - k V^{2}$

**[M1]**

Separate the variables by dividing both sides by $- V^{2}$

$- \frac{1}{V^{2}} \frac{\text{d}V}{\text{d}t} = k$

Integrate each side with respect to $t$

`\int -\dfrac{1}{V^{2}}\dfrac{\text{d}V}{\text{d}t} \; \text{d}t = \int k \; \text{d}t`

$\frac{\text{d}V}{\text{d}t}  \text{d} t$ becomes $\text{d} V$

`\int -\dfrac{1}{V^{2}} \; \text{d}V = \int k \; \text{d}t`

Integrate each side, using `\int -V^{-2} \; \text{d}V = V^{-1}`

$\frac{1}{V} = k t + c$

**[M1]**

The initial volume is 4000 litres, so $V = 4000$ when $t = 0$

`\dfrac{1}{4000} = k\left(0\right) + c`

$c = \frac{1}{4000}$

**[M1]**

A drop of 30% leaves 70% of the water, so after 10 minutes the volume is $0 . 7 \times 4000 = 2800$ litres

$\frac{1}{2800} = 10 k + \frac{1}{4000}$

Subtract and combine the fractions over a common denominator

$10 k = \frac{1}{2800} - \frac{1}{4000} = \frac{3}{28000}$

$k = \frac{3}{280000}$

**[M1]**

Substitute both constants back into the general solution and combine the right hand side over a common denominator

$\frac{1}{V} = \frac{3t}{280000} + \frac{70}{280000} = \frac{3t+70}{280000}$

Take the reciprocal of both sides

$V = \frac{280000}{3t+70}$

**[A1]**

(ii)

As $t$ becomes large the denominator grows without limit, so the fraction shrinks towards zero, although it is never actually equal to zero

**Final answer:** **The volume gets closer and closer to 0 litres but never actually reaches it**

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Variables defined, including units. The choice of minutes or seconds is free provided it is stated and used consistently.
> 
> **M1**: Correct differential equation showing the rate proportional to $V^{2}$ with a negative sign, since the container is leaking.
> 
> **M1**: Correct separation of the variables and integration of both sides to reach $\frac{1}{V} = k t + c$, with a constant of integration present.
> 
> **M1**: Use of $V = 4000$ when $t = 0$ to find the constant of integration.
> 
> **M1**: The 30% drop correctly interpreted as $V = 2800$, and used with $t = 10$ to find $k$. Using $V = 1200$ does not earn this mark.
> 
> **A1**: Correct particular solution. The equivalent forms `V = 4000\left(\dfrac{70}{3t + 70}\right)` and $\frac{1}{V} = \frac{3t+70}{280000}$ are accepted, as is `V = 4000\left(\dfrac{1400}{t + 1400}\right)` if $t$ was defined in seconds.
> 
> **B1**: Recognition that the volume tends towards zero as $t$ becomes large.
> 
> **B1**: Recognition that the volume never actually reaches zero. Saying only that the container empties does not earn this mark.

### Q12
The right hand side is not yet a product, so group the first two terms and the last two terms and take out a common factor from each pair

`\dfrac{\text{d}y}{\text{d}x} = 2x\left(y + 1\right) - \left(y + 1\right)`

Both terms now share a factor of $y + 1$

`\dfrac{\text{d}y}{\text{d}x} = \left(2x - 1\right)\left(y + 1\right)`

**[M1]**

Separate the variables by dividing both sides by $y + 1$, which is positive because $y > - 1$

$\frac{1}{y+1} \frac{\text{d}y}{\text{d}x} = 2 x - 1$

Integrate each side with respect to $x$

`\int \dfrac{1}{y + 1}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int \left(2x - 1\right) \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{1}{y + 1} \; \text{d}y = \int \left(2x - 1\right) \text{d}x`

**[M1]**

Integrate each side, using the result that `\int \dfrac{1}{y + 1} \; \text{d}y = \text{ln}\left|y + 1\right|`

`\text{ln}\left|y + 1\right| = x^{2} - x + c`

**[A1]**

Take exponentials of both sides, then split using the law of indices $a^{m} \times a^{n} = a^{m+n}$

`\left|y + 1\right| = \text{e}^{c} \times \text{e}^{x^{2} - x}`

Since $y > - 1$ the quantity $y + 1$ is positive, so the modulus signs can be dropped, and $\text{e}^{c}$ is written as $A$

$y + 1 = A \text{e}^{x^{2}-x}$

**[M1]**

Subtract 1 from both sides

$y = - 1 + A \text{e}^{x^{2}-x}$

**[A1]**

> **[exam-tip]**
> If a differential equation does not look separable, try factorising the right hand side before deciding it cannot be done. Grouping terms in pairs and taking out a common factor from each pair is the usual way in, and a right hand side with four terms in two variables is a strong hint that it will work. Here the equation is only separable after the factorisation, so spotting it is worth the whole question rather than just the first mark.

> **[mark-scheme]**
> **M1**: Correct factorisation of the right hand side into `\left(2x - 1\right)\left(y + 1\right)`, however the grouping is arranged.
> 
> **M1**: Correct separation of the variables, with the $y$ terms on one side and the $x$ terms on the other.
> 
> **A1**: Correct integration of both sides, with a constant of integration present. The modulus signs may be kept or dropped.
> 
> **M1**: Correct use of exponentials, with the exponential split so that the constant becomes a multiplier.
> 
> **A1**: Correct final answer with $y$ as the subject. Writing it as $y = A \text{e}^{x^{2}-x} - 1$ is equally acceptable.

### Q13
Separate the variables by dividing both sides by $2 x y$, which is allowed for non zero $x$ and $y$

$\frac{1}{y} \frac{\text{d}y}{\text{d}x} = \frac{3}{2} k x^{2}$

**[M1]**

Integrate each side with respect to $x$

`\int \dfrac{1}{y}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int \dfrac{3}{2}kx^{2} \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{1}{y} \; \text{d}y = \int \dfrac{3}{2}kx^{2} \; \text{d}x`

**[A1]**

Integrate each side, treating $k$ as a constant. The question allows $y$ to be negative, so keep the modulus signs

`\text{ln}\left|y\right| = \dfrac{3k}{2} \times \dfrac{x^{3}}{3} + c`

Simplify the coefficient, since the 3 in the numerator cancels the 3 in the denominator

`\text{ln}\left|y\right| = \dfrac{1}{2}kx^{3} + c`

**[A1]**

Take exponentials of both sides, then split using the law of indices $a^{m} \times a^{n} = a^{m+n}$

`\left|y\right| = \text{e}^{c} \times \text{e}^{\frac{1}{2}kx^{3}}`

**[M1]**

Removing the modulus allows either sign, so write $A = \pm \text{e}^{c}$, which is a non zero constant

$y = A \text{e}^{\frac{1}{2}kx^{3}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the $y$ terms on one side and the $x$ terms on the other.
> 
> **A1**: Correct separated form with an integral sign on each side.
> 
> **A1**: Correct integration of both sides, with the coefficient simplified to $\frac{1}{2} k$ and a constant of integration present. The modulus signs are condoned if missing.
> 
> **M1**: Correct use of exponentials, with the exponential split so that the constant becomes a multiplier.
> 
> **A1**: The given result reached. Because the answer is printed, the step turning $\text{e}^{c}$ into $A$ must be visible.
Setting $x = 0$ gives $y = A \text{e}^{0} = A$, so both curves start on the $y$-axis at `\left(0 , A\right)`

When $k > 0$ the exponent grows as $x$ increases, so the curve rises, slowly at first and then very steeply

When $k < 0$ the exponent becomes more negative as $x$ increases, so the curve decays towards the $x$-axis without ever reaching it

![Two separate sketches side by side, each drawn for x greater than or equal to zero with A positive. The left sketch, for k greater than zero, starts on the y-axis at the point (0, A), stays almost flat for small x, then curves upwards steeply. The right sketch, for k less than zero, starts on the y-axis at the same point (0, A), stays almost flat for small x, then decreases and flattens towards the x-axis without touching it. Both y-axis intercepts are labelled (0, A).](assets/001-two-separate-sketches-side-by-side-each-drawn-fo.png)

**[B1 B1]**

**Final answer:** **Both graphs intercept the y-axis at (0, A)**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct shape for $k > 0$: starting at a positive value on the $y$-axis and increasing, with the growth becoming steeper as $x$ increases.
> 
> **B1**: Correct shape for $k < 0$, on a separate diagram: starting at the same positive value and decreasing towards the $x$-axis without meeting it.
> 
> **B1**: Both $y$-axis intercepts identified as `\left(0 , A\right)`. Labelling them on the diagrams earns this mark just as well as writing them out.

### Q14
Factorise the right hand side so that the $y$ terms can be moved across

`\dfrac{2y - 1}{3}\dfrac{\text{d}y}{\text{d}x} = x^{2}\left(y^{2} - y\right)`

Divide both sides by $y^{2} - y$ and multiply by 3, which is allowed because $y > 1$ makes `y^{2} - y = y\left(y - 1\right)` positive

$\frac{2y-1}{y^{2}-y} \frac{\text{d}y}{\text{d}x} = 3 x^{2}$

**[M1]**

Integrate each side with respect to $x$

`\int \dfrac{2y - 1}{y^{2} - y}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int 3x^{2} \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{2y - 1}{y^{2} - y} \; \text{d}y = \int 3x^{2} \; \text{d}x`

**[A1]**

The numerator on the left is exactly the derivative of the denominator, so the integral takes the form `\int \dfrac{\text{f}'\left(y\right)}{\text{f}\left(y\right)} \; \text{d}y = \text{ln}\left|\text{f}\left(y\right)\right|`

`\text{ln}\left|y^{2} - y\right| = x^{3} + c`

**[M1]**

Since $y > 1$ the quantity $y^{2} - y$ is positive, so take exponentials of both sides and write the constant $\text{e}^{c}$ as $A$

$y^{2} - y = A \text{e}^{x^{3}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the $y$ terms on one side and the $x$ terms on the other.
> 
> **A1**: Correct separated form with an integral sign on each side.
> 
> **M1**: Recognition that the left side integrates to a logarithm because the numerator is the derivative of the denominator. Reaching the same integral by splitting into partial fractions is equally acceptable.
> 
> **A1**: Correct general solution. The equivalent `y\left(y - 1\right) = A\text{e}^{x^{3}}` is accepted, and there is no need to solve for $y$.
The right hand side contains no $x$, so separate the variables by multiplying both sides by `\dfrac{y^{2}}{\text{cosec}\left(y^{3}\right)}`

`\dfrac{3y^{2}}{\text{cosec}\left(y^{3}\right)}\dfrac{\text{d}y}{\text{d}x} = 1`

Integrate each side with respect to $x$

`\int \dfrac{3y^{2}}{\text{cosec}\left(y^{3}\right)}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{3y^{2}}{\text{cosec}\left(y^{3}\right)} \; \text{d}y = \int \text{d}x`

Use the definition $\text{cosec}  θ = \frac{1}{\text{sin}θ}$, so dividing by a cosecant is the same as multiplying by a sine

`\int 3y^{2}\,\text{sin}\left(y^{3}\right) \; \text{d}y = \int \text{d}x`

**[M1 A1]**

Consider differentiating `-\text{cos}\left(y^{3}\right)`, which brings out a `\text{sin}\left(y^{3}\right)` from the cosine and a $3 y^{2}$ from the chain rule on the argument

`\dfrac{\text{d}}{\text{d}y}\left(-\text{cos}\left(y^{3}\right)\right) = 3y^{2}\,\text{sin}\left(y^{3}\right)`

The derivative is exactly the integrand, so no compensating factor is needed, and the right side integrates to $x$

`-\text{cos}\left(y^{3}\right) + c = x`

**[M1]**

Write the result with $x$ as the subject, as the question requires

`x = -\text{cos}\left(y^{3}\right) + c`

**[A1]**

> **[exam-tip]**
> Read $\text{cosec}  y^{3}$ carefully. It means `\text{cosec}\left(y^{3}\right)`, the cosecant of $y$ cubed, and not $\text{cosec}^{3}  y$, which would be the cosecant cubed.

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the $y$ terms gathered on the left and the right side reduced to 1.
> 
> **A1**: The cosecant correctly converted to a sine, so that the left side reads `\int 3y^{2}\,\text{sin}\left(y^{3}\right) \; \text{d}y`.
> 
> **M1**: Correct integration by the reverse chain rule, recognising $3 y^{2}$ as the derivative of $y^{3}$.
> 
> **A1**: Correct answer with $x$ as the subject and a constant of integration present. Inverting the equation at the start to work with $\frac{\text{d}x}{\text{d}y}$ reaches the same integral and is equally acceptable. Leaving the answer as `-\text{cos}\left(y^{3}\right) + c = x` does not earn this mark, because the question names the form.

### Q15
Separate the variables by dividing both sides by $y$, which is allowed because $y \neq 0$

$\frac{1}{y} \frac{\text{d}y}{\text{d}x} = 3 x^{2}$

**[M1]**

Integrate each side with respect to $x$

`\int \dfrac{1}{y}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int 3x^{2} \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{1}{y} \; \text{d}y = \int 3x^{2} \; \text{d}x`

**[A1]**

Integrate each side. The question allows $y$ to be negative, so the modulus signs must be kept here

`\text{ln}\left|y\right| = x^{3} + c`

**[A1]**

Take exponentials of both sides

`\left|y\right| = \text{e}^{x^{3} + c}`

Split the exponential using the law of indices $a^{m} \times a^{n} = a^{m+n}$

`\left|y\right| = \text{e}^{c} \times \text{e}^{x^{3}}`

**[M1]**

Removing the modulus allows either sign, so write $A = \pm \text{e}^{c}$, which is a non zero constant of either sign

$y = A \text{e}^{x^{3}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the $y$ terms on one side and the $x$ terms on the other.
> 
> **A1**: Correct separated form with an integral sign on each side.
> 
> **A1**: Correct integration of both sides, with a constant of integration present. The modulus signs are condoned if missing.
> 
> **M1**: Correct use of exponentials, with the exponential split so that the constant becomes a multiplier.
> 
> **A1**: The given result reached. Because $y$ may be negative, the constant $A$ must be allowed to take either sign; a solution that assumes $y > 0$ throughout still earns this mark, but the sign must not be stated as necessarily positive.

### Q16
The question asks for the variables to be defined, so state what each one represents before writing the equation

*Let V be the volume of water in the container, in litres, at time t seconds*

The rate of change of volume is directly proportional to the volume itself, so the two are linked by a constant

$\frac{\text{d}V}{\text{d}t} = k V$

**[B1]**

The container is leaking, so the volume is falling and the rate of change must be negative, where $k$ is a positive constant

$\frac{\text{d}V}{\text{d}t} = - k V$

**[B1]**

> **[mark-scheme]**
> **B1**: Both variables defined, and a differential equation showing direct proportion between $\frac{\text{d}V}{\text{d}t}$ and $V$ with a constant of proportionality. Any letters may be used provided they are defined.
> 
> **B1**: The negative sign present, so that the equation models a decreasing volume. Writing $\frac{\text{d}V}{\text{d}t} = k V$ and stating that $k$ is negative is equally acceptable.
Separate the variables by dividing both sides by $V$, which is positive because the container holds water

$\frac{1}{V} \frac{\text{d}V}{\text{d}t} = - k$

Integrate each side with respect to $t$

`\int \dfrac{1}{V}\dfrac{\text{d}V}{\text{d}t} \; \text{d}t = \int -k \; \text{d}t`

$\frac{\text{d}V}{\text{d}t}  \text{d} t$ becomes $\text{d} V$

`\int \dfrac{1}{V} \; \text{d}V = \int -k \; \text{d}t`

**[M1]**

Integrate each side, using the result that `\int \dfrac{1}{V} \; \text{d}V = \text{ln} \; V` for positive $V$

$\text{ln}  V = - k t + c$

**[A1]**

Take exponentials of both sides, then split the result using the law of indices $a^{m} \times a^{n} = a^{m+n}$

$V = \text{e}^{-kt} \times \text{e}^{c}$

Since $\text{e}^{c}$ is a constant, write it as $A$

$V = A \text{e}^{-kt}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with $\frac{1}{V}$ on one side and the constant on the other, and an attempt to integrate at least one side.
> 
> **A1**: Correct integration of both sides, with a constant of integration present. Keeping the modulus signs as `\text{ln}\left|V\right|` is accepted.
> 
> **A1**: Correct general solution with $V$ as the subject and the constant written as a multiplier. Leaving the answer as $V = \text{e}^{-kt+c}$ is accepted, since the constant has been carried through correctly.

### Q17
Separate the variables by dividing both sides by $y^{2} + 3$ and by $\text{cot}  x$, using the definition $\text{cot}  x = \frac{1}{\text{tan}x}$ on the right

$\frac{y}{y^{2}+3} \frac{\text{d}y}{\text{d}x} = \text{tan}  x$

**[M1]**

Integrate each side with respect to $x$

`\int \dfrac{y}{y^{2} + 3}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int \text{tan} \; x \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{y}{y^{2} + 3} \; \text{d}y = \int \text{tan} \; x \; \text{d}x`

Multiply both sides by 2, so that the numerator on the left becomes the derivative of its denominator

`\int \dfrac{2y}{y^{2} + 3} \; \text{d}y = 2\int \text{tan} \; x \; \text{d}x`

**[A1]**

Integrate the left side as `\int \dfrac{\text{f}'\left(y\right)}{\text{f}\left(y\right)} \; \text{d}y = \text{ln}\left|\text{f}\left(y\right)\right|`, and the right using the standard result `\int \text{tan} \; x \; \text{d}x = \text{ln}\left|\text{sec} \; x\right|`

`\text{ln}\left|y^{2} + 3\right| = 2\,\text{ln}\left|\text{sec} \; x\right| + c`

**[M1 A1]**

Use the law `k\,\text{ln} \; a = \text{ln}\left(a^{k}\right)` on the first term, and write the constant as `c = \text{ln}\left(\text{e}^{c}\right)` so that every term is a logarithm

`\text{ln}\left|y^{2} + 3\right| = \text{ln}\left(\left|\text{sec} \; x\right|^{2}\right) + \text{ln}\left(\text{e}^{c}\right)`

Combine the right hand side using `\text{ln} \; a + \text{ln} \; b = \text{ln}\left(ab\right)`, then remove the logarithms from both sides

`\left|y^{2} + 3\right| = \text{e}^{c}\left|\text{sec} \; x\right|^{2}`

Squaring removes the modulus on the right, and $y^{2} + 3$ is always positive so its modulus can be dropped. Writing $\text{e}^{c}$ as $A$ gives the required form

$y^{2} + 3 = A  \text{sec}^{2}  x$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the cotangent converted to a tangent.
> 
> **A1**: Correct separated form, arranged so that the left numerator is the derivative of the denominator. Keeping `\int \dfrac{y}{y^{2} + 3} \; \text{d}y` and carrying a factor of $\frac{1}{2}$ instead is equally acceptable.
> 
> **M1**: An attempt to integrate both sides, taking the left to a logarithm and the right to a multiple of `\text{ln}\left|\text{sec} \; x\right|`.
> 
> **A1**: Fully correct integration with a constant of integration present. The modulus signs are condoned if missing.
> 
> **A1**: The given result reached, with the laws of logarithms used correctly to turn the constant into a multiplier. Because the answer is printed, the log law steps must be visible; jumping straight from the logarithmic equation to $A  \text{sec}^{2}  x$ does not earn this mark.
Separate the variables by dividing both sides by $\text{cosec}  3 y$ and by $\text{e}^{x^{2}}$

$\frac{1}{\text{cosec}3y} \frac{\text{d}y}{\text{d}x} = \frac{2x}{\text{e}^{x^{2}}}$

**[M1]**

Integrate each side with respect to $x$

`\int \dfrac{1}{\text{cosec} \; 3y}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int \dfrac{2x}{\text{e}^{x^{2}}} \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{1}{\text{cosec} \; 3y} \; \text{d}y = \int \dfrac{2x}{\text{e}^{x^{2}}} \; \text{d}x`

Use the definition $\text{cosec}  θ = \frac{1}{\text{sin}θ}$ on the left, and $\frac{1}{\text{e}^{x^{2}}} = \text{e}^{-x^{2}}$ on the right

`\int \text{sin} \; 3y \; \text{d}y = \int 2x\text{e}^{-x^{2}} \; \text{d}x`

**[A1]**

Multiply through by $- 3$, so that each side becomes exactly a derivative

`\int -3\,\text{sin} \; 3y \; \text{d}y = 3\int -2x\text{e}^{-x^{2}} \; \text{d}x`

Both sides now integrate by the reverse chain rule, since $- 3  \text{sin}  3 y$ is the derivative of $\text{cos}  3 y$ and $- 2 x \text{e}^{-x^{2}}$ is the derivative of $\text{e}^{-x^{2}}$

$\text{cos}  3 y = 3 \text{e}^{-x^{2}} + c$

**[M1 A1]**

To find the constant, substitute $x = 0$ and $y = \frac{π}{3}$

`\text{cos}\left(\pi\right) = 3\text{e}^{0} + c`

Since `\text{cos}\left(\pi\right) = -1` and $\text{e}^{0} = 1$

$- 1 = 3 + c$

$c = - 4$

**[M1]**

Substitute the constant back into the general solution

$\text{cos}  3 y = 3 \text{e}^{-x^{2}} - 4$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the $y$ terms on one side and the $x$ terms on the other.
> 
> **A1**: Correct separated form, with the cosecant converted to a sine and the exponential written with a negative index.
> 
> **M1**: An attempt to integrate both sides by the reverse chain rule.
> 
> **A1**: Fully correct integration with a constant of integration present. Carrying fractions instead of multiplying through by $- 3$ is acceptable provided the result is equivalent.
> 
> **M1**: Substitution of the boundary values into an integrated expression containing a constant, using the correct exact values, and a correct method to find that constant.
> 
> **A1**: Correct particular solution. Equivalent arrangements are accepted, and there is no need to solve for $y$ because the question does not name a subject.

### Q18
The derivative is not yet the subject, so rearrange the equation first

$\frac{\text{d}x}{\text{d}t} = \text{sin}  2 t - 5$

Integrate the right hand side, dividing the sine term by the coefficient of $t$ in its argument and remembering that the integral of sine carries a negative sign

$x = - \frac{1}{2} \text{cos}  2 t - 5 t + c$

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Correct rearrangement to make $\frac{\text{d}x}{\text{d}t}$ the subject, followed by integration of at least one term.
> 
> **A1**: Fully correct solution, including the negative sign and the factor of $\frac{1}{2}$ on the cosine term, with the constant of integration present.
Rearrange to make the derivative the subject

$\frac{\text{d}V}{\text{d}x} = 3 \text{e}^{4x} - 2$

Integrate the right hand side, dividing the exponential by the coefficient of $x$ in its exponent

$V = \frac{3}{4} \text{e}^{4x} - 2 x + c$

**[M1]**

To find the constant, substitute $x = 0$ and $V = - 4$

`-4 = \dfrac{3}{4}\text{e}^{0} - 2\left(0\right) + c`

Any number raised to the power zero is 1

$- 4 = \frac{3}{4} + c$

$c = - \frac{19}{4}$

**[M1]**

Substitute the constant back into the solution

$V = \frac{3}{4} \text{e}^{4x} - 2 x - \frac{19}{4}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct rearrangement and integration, with the exponential divided by 4 and the constant of integration present. The $- 2 x$ term must not be lost.
> 
> **M1**: Substitution of $x = 0$ and $V = - 4$ into an integrated expression containing a constant, and a correct method to find that constant.
> 
> **A1**: Correct final answer with $V$ as the subject. The decimal equivalents $0 . 75$ and $- 4 . 75$ are accepted.

### Q19
The question asks for the variables to be defined, so state what each one represents before writing the equation

*Let V be the volume of the bar of soap, in cubic centimetres, at time t minutes*

**[B1]**

The rate of decrease is proportional to the volume, so the rate of change itself is negative, where $k$ is a positive constant

$\frac{\text{d}V}{\text{d}t} = - k V$

**[M1]**

Separate the variables by dividing both sides by $V$, which is positive because it is a volume

$\frac{1}{V} \frac{\text{d}V}{\text{d}t} = - k$

Integrate each side with respect to $t$

`\int \dfrac{1}{V}\dfrac{\text{d}V}{\text{d}t} \; \text{d}t = \int -k \; \text{d}t`

$\frac{\text{d}V}{\text{d}t}  \text{d} t$ becomes $\text{d} V$

`\int \dfrac{1}{V} \; \text{d}V = \int -k \; \text{d}t`

Integrate each side

$\text{ln}  V = - k t + c$

**[M1]**

Take exponentials of both sides, split using the law of indices, and write the constant $\text{e}^{c}$ as $A$

$V = A \text{e}^{-kt}$

**[A1]**

The soap is a cuboid, so multiply its three dimensions to get the volume

$V = 3 \times 6 \times 10 = 180$

This is the volume before the soap enters the water, so $V = 180$ when $t = 0$

$180 = A \text{e}^{0}$

$A = 180$

**[M1]**

Do the same with the second set of dimensions

$V = 2 . 85 \times 5 . 7 \times 9 . 5 = 154 . 3275$

This is the volume after two minutes, so substitute $t = 2$

$154 . 3275 = 180 \text{e}^{-2k}$

Divide both sides by 180, then take natural logarithms of both sides

`-2k = \text{ln}\left(\dfrac{154.3275}{180}\right)`

`k = -\dfrac{1}{2}\text{ln}\left(\dfrac{154.3275}{180}\right) = 0.0769399\ldots`

**[M1]**

Substitute both constants back into the general solution

$V = 180 \text{e}^{-0.0769t}$

**[A1]**

> **[mark-scheme]**
> **B1**: Variables defined, including their units. The choice of minutes or seconds for $t$ is free, provided it is stated and used consistently.
> 
> **M1**: Correct differential equation showing direct proportion with a negative sign, since the volume is decreasing.
> 
> **M1**: Correct separation of the variables and integration of both sides, with a constant of integration present.
> 
> **A1**: Correct general solution of the form $V = A \text{e}^{-kt}$.
> 
> **M1**: The initial volume calculated as 180 from the three given dimensions, and used to find the constant.
> 
> **M1**: The second volume calculated as 154.3275 and used with logarithms to find $k$. Taking logarithms of both sides must be visible.
> 
> **A1**: Correct particular solution, with $k$ given to at least 3 significant figures. If $t$ was defined in seconds, the equivalent answer $V = 180 \text{e}^{-0.00128t}$ earns this mark instead.
As $t$ increases the exponent $- 0 . 0769 t$ becomes more and more negative, so the exponential term shrinks towards zero without ever reaching it

**Final answer:** **The volume approaches zero but never actually reaches it**

**[B1]**

A real bar of soap does eventually dissolve completely, so the model describes something that does not happen

**Final answer:** **The model predicts the soap never fully dissolves, which is not what happens in reality**

**[B1]**

> **[mark-scheme]**
> **B1**: Recognition that the volume tends to zero as $t$ becomes large, without ever equalling zero. Saying only that the volume decreases does not earn this mark.
> 
> **B1**: The criticism made explicit: a real bar of soap would dissolve completely in a finite time, whereas the model keeps a small volume for ever. Any answer making that contrast earns the mark.

### Q20
The question asks for the variables to be defined, so state what each one represents before writing the equation

*Let V be the volume of the balloon, in cubic metres, at time t seconds*

**[B1]**

Inversely proportional to the square of the volume means the rate of change equals a constant divided by $V^{2}$

$\frac{\text{d}V}{\text{d}t} = \frac{k}{V^{2}}$

**[B1]**

> **[mark-scheme]**
> **B1**: Both variables defined, with their units stated. Any letters may be used provided they are defined.
> 
> **B1**: Correct differential equation, with the constant in the numerator over $V^{2}$. Writing $\frac{\text{d}V}{\text{d}t} = k V^{-2}$ is equally acceptable, but $\frac{k}{V}$ describes the wrong proportionality and does not earn this mark.
Separate the variables by multiplying both sides by $V^{2}$

$V^{2} \frac{\text{d}V}{\text{d}t} = k$

Integrate each side with respect to $t$

`\int V^{2}\dfrac{\text{d}V}{\text{d}t} \; \text{d}t = \int k \; \text{d}t`

$\frac{\text{d}V}{\text{d}t}  \text{d} t$ becomes $\text{d} V$

`\int V^{2} \; \text{d}V = \int k \; \text{d}t`

**[M1]**

Integrate each side, calling the constant of integration $c_{0}$ so that it can be adjusted at the end

$\frac{V^{3}}{3} = k t + c_{0}$

Multiply through by 3, and write the constant $3 c_{0}$ as $c$

$V^{3} = 3 k t + c$

**[A1]**

The balloon starts with zero volume, so $V = 0$ when $t = 0$

`0^{3} = 3k\left(0\right) + c`

$c = 0$

**[M1]**

Now use the second condition, that $V = 600$ when $t = 400$

`600^{3} = 3k\left(400\right)`

$216000000 = 1200 k$

**[M1]**

Divide both sides by 1200

$k = 180000$

**[A1]**

The coefficient of $t$ in the solution is $3 k$, so substitute the constant back

`V^{3} = 3\left(180000\right)t`

$V^{3} = 540000 t$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with $V^{2}$ on one side and the constant on the other.
> 
> **A1**: Correct integration of both sides, with a constant of integration present.
> 
> **M1**: Use of $V = 0$ when $t = 0$ to show that the constant of integration is zero.
> 
> **M1**: Use of $V = 600$ when $t = 400$ in an expression containing $k$.
> 
> **A1**: Correct value of the constant of proportionality.
> 
> **A1**: Correct particular solution. The equivalent `V = \sqrt[3]{540000t}` is accepted.
Substitute the release volume into the particular solution and rearrange for the time

$1250^{3} = 540000 t$

$t = \frac{1250^{3}}{540000} = 3616 . 89 \dots$

**[M1]**

An hour is 3600 seconds, so convert the inflating time into hours, minutes and seconds

$3617 - 3600 = 17$

$t = 1 \text{hour and} 17 \text{seconds}$

Count that back from midday to get the latest possible start

**Final answer:** **The balloon must start being inflated by about 10:59 am**

**[A1]**

> **[mark-scheme]**
> **M1**: Substitution of $V = 1250$ into their particular solution and a correct method to find $t$.
> 
> **A1**: Correct time of day, identifying that inflating takes 1 hour and 17 seconds and counting back from midday. Answers of 10:59 am or "17 seconds before 11 am" both earn this mark. A bare time in seconds does not, because the question asks for the latest starting time.

### Q21
The derivative is not yet the subject, so rearrange the equation first

$\frac{\text{d}x}{\text{d}t} = 4 - 9 t^{2}$

The right hand side depends only on $t$, so integrate it directly

$x = 4 t - \frac{9t^{3}}{3} + c$

**[M1]**

Simplify the coefficient

$x = 4 t - 3 t^{3} + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct rearrangement to make $\frac{\text{d}x}{\text{d}t}$ the subject, followed by integration of at least one term.
> 
> **A1**: Fully correct solution with the constant of integration included. Unsimplified equivalents such as $\frac{9t^{3}}{3}$ are accepted, and the two terms may be written in either order, but the constant must be present.
Rearrange to make the derivative the subject

$\frac{\text{d}V}{\text{d}x} = 2 \text{e}^{x} + 4$

Integrate the right hand side with respect to $x$

$V = 2 \text{e}^{x} + 4 x + c$

**[M1]**

To find the constant, substitute $x = 0$ and $V = 3$

`3 = 2\text{e}^{0} + 4\left(0\right) + c`

Any number raised to the power zero is 1

$3 = 2 + c$

$c = 1$

**[M1]**

Substitute the constant back into the solution

$V = 2 \text{e}^{x} + 4 x + 1$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct rearrangement and integration to give an expression of the form $2 \text{e}^{x} + 4 x + c$, with the constant of integration present. The $4 x$ term must not be lost.
> 
> **M1**: Substitution of $x = 0$ and $V = 3$ into an integrated expression containing a constant, and a correct method to find that constant.
> 
> **A1**: Correct final answer with $V$ as the subject.

### Q22
Separate the variables by dividing both sides by $y$, which is allowed because $y > 0$

$\frac{1}{y} \frac{\text{d}y}{\text{d}x} = 4 x$

**[M1]**

Integrate each side with respect to $x$

`\int \dfrac{1}{y}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int 4x \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{1}{y} \; \text{d}y = \int 4x \; \text{d}x`

Use the result that `\int \dfrac{1}{y} \; \text{d}y = \text{ln} \; y` for positive $y$

$\text{ln}  y = \frac{4x^{2}}{2} + c$

Simplify the coefficient on the right

$\text{ln}  y = 2 x^{2} + c$

**[A1]**

Take exponentials of both sides

$\text{e}^{\text{ln}y} = \text{e}^{2x^{2}+c}$

The exponential and the natural logarithm are inverse functions, so the left side is simply $y$

$y = \text{e}^{2x^{2}+c}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the $y$ terms on one side and the $x$ terms on the other.
> 
> **A1**: Correct integration of both sides to $\text{ln}  y = 2 x^{2} + c$, with a constant of integration present. Keeping the modulus signs as `\text{ln} \left|y\right|` is also accepted, and the unsimplified $\frac{4x^{2}}{2}$ is condoned.
> 
> **A1**: The given result reached by taking exponentials of both sides. Because the answer is printed, this step must be visible.
> 
> Splitting the exponential a step early and reaching $y = A \text{e}^{2x^{2}}$, where $A$ is a constant, is an equally valid general solution and earns full marks here, provided the working shows how it was obtained. Part (b) then only needs the connection $A = \text{e}^{c}$ to be identified.
(i)

Use the law of indices $a^{m} \times a^{n} = a^{m+n}$ in reverse to split the exponential into two factors

$y = \text{e}^{2x^{2}} \times \text{e}^{c}$

Replace $\text{e}^{c}$ by $A$, as the question directs

$y = A \text{e}^{2x^{2}}$

**[B1]**

(ii)

To see what $A$ controls, substitute $x = 0$, since $\text{e}^{0} = 1$

$y = A \text{e}^{0} = A$

**Final answer:** **A is the value of y when x = 0**

**Final answer:** **If x represents time in a model, then A is the initial value of y**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct use of the law of indices together with the given substitution to reach the printed form.
> 
> **B1**: Both ideas needed: that $A$ is the value of $y$ when $x = 0$, and that in a model where $x$ is time this is the starting or initial value of $y$. Saying only that $A$ is a constant does not earn this mark.

### Q23
Separate the variables by dividing both sides by $y - 2$, which is positive because $y > 2$

$\frac{1}{y-2} \frac{\text{d}y}{\text{d}x} = x^{2}$

Integrate each side with respect to $x$

`\int \dfrac{1}{y - 2}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int x^{2} \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{1}{y - 2} \; \text{d}y = \int x^{2} \; \text{d}x`

**[M1]**

Integrate each side, using the result that `\int \dfrac{1}{y - 2} \; \text{d}y = \text{ln}\left|y - 2\right|`

`\text{ln}\left|y - 2\right| = \dfrac{1}{3}x^{3} + c`

**[A1]**

Take exponentials of both sides

`\left|y - 2\right| = \text{e}^{\frac{1}{3}x^{3} + c}`

Split the exponential using the law of indices $a^{m} \times a^{n} = a^{m+n}$

`\left|y - 2\right| = \text{e}^{\frac{1}{3}x^{3}} \times \text{e}^{c}`

Since $\text{e}^{c}$ is a constant, write it as $A$

`\left|y - 2\right| = A\text{e}^{\frac{1}{3}x^{3}}`

**[M1]**

Because $y > 2$, the quantity $y - 2$ is positive, so the modulus signs can be dropped

$y - 2 = A \text{e}^{\frac{1}{3}x^{3}}$

Add 2 to both sides

$y = 2 + A \text{e}^{\frac{1}{3}x^{3}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the $y$ terms on one side and the $x$ terms on the other.
> 
> **A1**: Correct integration of both sides, with a constant of integration present. The modulus signs may be kept or dropped.
> 
> **M1**: Correct use of exponentials on both sides, with the exponential split so that the constant becomes a multiplier rather than staying in the exponent.
> 
> **A1**: Correct final answer with $y$ as the subject. Writing it as $y = A \text{e}^{\frac{1}{3}x^{3}} + 2$ is equally acceptable, and $\text{e}^{\frac{x^{3}}{3}}$ is accepted for the exponential.
The right hand side contains no $x$, so separate the variables by dividing both sides by $\text{sin}^{2}  2 y$

$\frac{1}{\text{sin}^{2}2y} \frac{\text{d}y}{\text{d}x} = 1$

Integrate each side with respect to $x$

`\int \dfrac{1}{\text{sin}^{2} \; 2y}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{1}{\text{sin}^{2} \; 2y} \; \text{d}y = \int \text{d}x`

Use the definition $\text{cosec}  θ = \frac{1}{\text{sin}θ}$ to put the left side into a standard form

`\int \text{cosec}^{2} \; 2y \; \text{d}y = \int \text{d}x`

**[M1]**

Consider differentiating $\text{cot}  2 y$, which brings out a factor of $- 1$ from the cotangent and a 2 from the chain rule on the argument

`\dfrac{\text{d}}{\text{d}y}\left(\text{cot} \; 2y\right) = -2\,\text{cosec}^{2} \; 2y`

So integrating $\text{cosec}^{2}  2 y$ gives $\text{cot}  2 y$ with a compensating factor of $- \frac{1}{2}$, and the right side integrates to $x$

$- \frac{1}{2} \text{cot}  2 y + c = x$

**[A1]**

Write the result with $x$ as the subject, as the question requires

$x = - \frac{1}{2} \text{cot}  2 y + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the left side written in terms of $\text{cosec}^{2}  2 y$ or left as $\frac{1}{\text{sin}^{2}2y}$.
> 
> **A1**: Correct integration of both sides, including the factor of $- \frac{1}{2}$ and a constant of integration.
> 
> **A1**: Answer presented in the required form with $x$ as the subject. Leaving it as $- \frac{1}{2} \text{cot}  2 y + c = x$ does not earn this mark.

### Q24
(i)

Inversely proportional to the volume means the rate of change equals a constant divided by $V$

$\frac{\text{d}V}{\text{d}t} = \frac{k}{V}$

**[B1]**

(ii)

Substitute the given rate and the given volume into the differential equation

$5 = \frac{k}{48}$

**[M1]**

Multiply both sides by 48

$k = 240$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct differential equation, with the constant in the numerator over $V$. Any letter may be used for the constant. Writing $\frac{\text{d}V}{\text{d}t} = k V$ describes direct proportion and does not earn this mark.
> 
> **M1**: Substitution of the rate 5 and the volume 48 into a differential equation of the form $\frac{\text{d}V}{\text{d}t} = \frac{k}{V}$.
> 
> **A1**: Correct constant of proportionality.
Using the constant found in part (a), the differential equation is $\frac{\text{d}V}{\text{d}t} = \frac{240}{V}$, so separate the variables by multiplying both sides by $V$

$V \frac{\text{d}V}{\text{d}t} = 240$

Integrate each side with respect to $t$

`\int V\dfrac{\text{d}V}{\text{d}t} \; \text{d}t = \int 240 \; \text{d}t`

$\frac{\text{d}V}{\text{d}t}  \text{d} t$ becomes $\text{d} V$

`\int V \; \text{d}V = \int 240 \; \text{d}t`

**[M1]**

Integrate each side, calling the constant of integration $c_{0}$ so that it can be adjusted at the end

$\frac{V^{2}}{2} = 240 t + c_{0}$

**[A1]**

Multiply through by 2 to clear the fraction

$V^{2} = 480 t + 2 c_{0}$

**[M1]**

Since $2 c_{0}$ is itself just a constant, write it as $c$

$V^{2} = 480 t + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with $V$ on one side and the constant on the other, and an attempt to integrate at least one side.
> 
> **A1**: Correct integrated equation with a constant of integration present.
> 
> **M1**: Multiplication through by 2 to remove the fraction.
> 
> **A1**: Correct general solution. Leaving the constant as $2 c$ is accepted, as is the explicit form $V = \sqrt{480t+c}$.
(i)

Stored flat initially means $V = 0$ when $t = 0$, so substitute both values into the general solution

`0^{2} = 480\left(0\right) + c`

$c = 0$

$V^{2} = 480 t$

**[B1]**

(ii)

The model measures $t$ in seconds, so convert 50 minutes before substituting

$t = 50 \times 60 = 3000$

`V^{2} = 480\left(3000\right) = 1440000`

**[M1]**

Take the positive square root, since a volume cannot be negative

$V = 1200 \text{m}^{3}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct particular solution. The equivalent $V = \sqrt{480t}$ or $V = 4 \sqrt{30t}$ is also accepted.
> 
> **M1**: Conversion of 50 minutes to 3000 seconds and substitution into their particular solution. Substituting 50 directly does not earn this mark.
> 
> **A1**: Correct volume. The units are not required for this mark.

### Q25
Separate the variables by dividing both sides by $\text{cos}^{2}  y$ and by $\text{sin}^{2}  x$

$\frac{1}{\text{cos}^{2}y} \frac{\text{d}y}{\text{d}x} = \frac{1}{\text{sin}^{2}x}$

**[M1]**

Integrate each side with respect to $x$

`\int \dfrac{1}{\text{cos}^{2} \; y}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int \dfrac{1}{\text{sin}^{2} \; x} \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \dfrac{1}{\text{cos}^{2} \; y} \; \text{d}y = \int \dfrac{1}{\text{sin}^{2} \; x} \; \text{d}x`

Use the definitions $\text{sec}  θ = \frac{1}{\text{cos}θ}$ and $\text{cosec}  θ = \frac{1}{\text{sin}θ}$ to put both sides into standard integrable forms

`\int \text{sec}^{2} \; y \; \text{d}y = \int \text{cosec}^{2} \; x \; \text{d}x`

**[A1]**

Integrate each side, using the standard results `\int \text{sec}^{2} \; \theta \; \text{d}\theta = \text{tan} \; \theta` and `\int \text{cosec}^{2} \; \theta \; \text{d}\theta = -\text{cot} \; \theta`

$\text{tan}  y = - \text{cot}  x + c$

**[M1 A1]**

To find the constant, substitute $x = \frac{π}{4}$ and $y = 0$

`\text{tan}\left(0\right) = -\text{cot}\left(\dfrac{\pi}{4}\right) + c`

Both `\text{tan}\left(0\right) = 0` and `\text{cot}\left(\dfrac{\pi}{4}\right) = 1`

$0 = - 1 + c$

$c = 1$

**[M1]**

Substitute the constant back into the integrated equation

$\text{tan}  y = 1 - \text{cot}  x$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the $y$ terms on one side and the $x$ terms on the other.
> 
> **A1**: Both sides correctly written in terms of $\text{sec}^{2}  y$ and $\text{cosec}^{2}  x$, with an integral sign on each side. Leaving them as $\frac{1}{\text{cos}^{2}y}$ and $\frac{1}{\text{sin}^{2}x}$ is accepted.
> 
> **M1**: An attempt to integrate both sides, with each side taken to a tangent or cotangent.
> 
> **A1**: Fully correct integration, including the negative sign on the cotangent, with a constant of integration present.
> 
> **M1**: Substitution of the boundary values into an integrated expression containing a constant, using the correct exact values, and a correct method to find that constant.
> 
> **A1**: Correct final answer. The equivalent $\text{tan}  y + \text{cot}  x = 1$ is accepted, and there is no need to rearrange for $y$ because the question does not ask for it.
Separate the variables by dividing both sides by $\text{e}^{y}$ and by $\text{e}^{-3x}$, remembering that $\frac{1}{\text{e}^{-3x}} = \text{e}^{3x}$

$\text{e}^{-y} \frac{\text{d}y}{\text{d}x} = 2 \text{e}^{3x}$

**[M1]**

Integrate each side with respect to $x$

`\int \text{e}^{-y}\dfrac{\text{d}y}{\text{d}x} \; \text{d}x = \int 2\text{e}^{3x} \; \text{d}x`

$\frac{\text{d}y}{\text{d}x}  \text{d} x$ becomes $\text{d} y$

`\int \text{e}^{-y} \; \text{d}y = \int 2\text{e}^{3x} \; \text{d}x`

**[A1]**

Integrating an exponential divides it by the coefficient of the variable in the exponent, which is $- 1$ on the left and 3 on the right

$- \text{e}^{-y} = \frac{2}{3} \text{e}^{3x} + c$

**[M1 A1]**

To find the constant, substitute $x = 0$ and $y = 0$

$- \text{e}^{0} = \frac{2}{3} \text{e}^{0} + c$

Any number raised to the power zero is 1

$- 1 = \frac{2}{3} + c$

$c = - \frac{5}{3}$

**[M1]**

Substitute the constant back in, then collect the two exponential terms on one side

$\frac{2}{3} \text{e}^{3x} + \text{e}^{-y} = \frac{5}{3}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the exponential in $x$ moved to the right hand side as $\text{e}^{3x}$.
> 
> **A1**: Correct separated form with an integral sign on each side.
> 
> **M1**: An attempt to integrate both sides, with each exponential divided by the coefficient of the variable in its exponent.
> 
> **A1**: Fully correct integration with a constant of integration present. The negative sign in front of $\text{e}^{-y}$ is required.
> 
> **M1**: Substitution of $x = 0$ and $y = 0$ into an integrated expression containing a constant, and a correct method to find that constant.
> 
> **A1**: Correct final answer. Any equivalent arrangement is accepted, including $- \text{e}^{-y} = \frac{2}{3} \text{e}^{3x} - \frac{5}{3}$ and the explicit form `y = \text{ln}\left(\dfrac{3}{5 - 2\text{e}^{3x}}\right)`, since the question does not name a subject.

### Q26
The rate of change of volume is directly proportional to the volume itself, so the two are linked by a constant

$\frac{\text{d}V}{\text{d}t} = k V$

**[B1]**

The container is leaking, so the volume is falling and the rate of change must be negative

$\frac{\text{d}V}{\text{d}t} = - k V$

**[B1]**

> **[mark-scheme]**
> **B1**: A differential equation showing direct proportion between $\frac{\text{d}V}{\text{d}t}$ and $V$, with a constant of proportionality. Any letter may be used for the constant.
> 
> **B1**: The negative sign present, so that the equation models a decreasing volume. Writing $\frac{\text{d}V}{\text{d}t} = k V$ and stating that $k$ is negative is equally acceptable.
(i)

To see what $A$ controls, substitute $t = 0$, since $\text{e}^{0} = 1$

$V = A \text{e}^{0} = A$

**Final answer:** **A is the volume of water in the container at the start, when t = 0**

**[B1]**

(ii)

Because $k$ is positive, the exponent $- k t$ becomes more negative as time increases, so the exponential decays

**Final answer:** **The negative sign makes **$V$** a decreasing function of time, which is what a leaking container requires**

**Final answer:** **Without it the volume would increase, and the container would be filling rather than leaking**

**[B1]**

> **[mark-scheme]**
> **B1**: $A$ identified as the initial volume of water in the container. An answer that says only "$A$ is a constant" or "$A$ is the value of $V$ when $t = 0$" without connecting it to the volume of water does not earn this mark, because the question asks for the significance in context.
> 
> **B1**: The negative sign explained as making the volume decrease over time. Reference to the water leaking out, or to the contrast with what would happen without the sign, both earn this mark.

### Q27
Multiply both sides by $t$ and divide by $N$ to gather each variable on its own side

$\frac{1}{N} \frac{\text{d}N}{\text{d}t} = k t$

**[M1]**

Integrate each side with respect to $t$

`\int \dfrac{1}{N}\dfrac{\text{d}N}{\text{d}t} \; \text{d}t = \int kt \; \text{d}t`

$\frac{\text{d}N}{\text{d}t}  \text{d} t$ becomes $\text{d} N$

`\int \dfrac{1}{N} \; \text{d}N = \int kt \; \text{d}t`

**[A1]**

Integrate each side, treating $k$ as a constant

$\text{ln}  N = \frac{1}{2} k t^{2} + c$

**[A1]**

The modulus signs are not needed because $N$ counts trees and cannot be negative. Take exponentials of both sides and split the result using the law of indices

$N = \text{e}^{c} \times \text{e}^{\frac{1}{2}kt^{2}}$

Since $\text{e}^{c}$ is a constant, write it as $A$

$N = A \text{e}^{\frac{1}{2}kt^{2}}$

**[M1]**

Three trees were infected when the disease was discovered, so $N = 3$ when $t = 0$

$3 = A \text{e}^{0} = A$

**[M1]**

Ten trees were infected after ten days, so substitute $N = 10$ and $t = 10$ into the solution

`10 = 3\text{e}^{\frac{1}{2}k\left(10\right)^{2}} = 3\text{e}^{50k}`

Divide both sides by 3

$\frac{10}{3} = \text{e}^{50k}$

Take natural logarithms of both sides, since the logarithm undoes the exponential

`\text{ln}\left(\dfrac{10}{3}\right) = 50k`

`k = \dfrac{1}{50}\text{ln}\left(\dfrac{10}{3}\right)`

**[M1]**

The exponent needs $\frac{1}{2} k$, so halve this value and substitute it back

`N = 3\text{e}^{\frac{1}{100}\text{ln}\left(\frac{10}{3}\right)t^{2}}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct separation of the variables, with the $N$ terms on one side and the $t$ terms on the other.
> 
> **A1**: Correct separated form with an integral sign on each side.
> 
> **A1**: Correct integration of both sides, with a constant of integration present. Keeping the modulus signs as `\text{ln}\left|N\right|` is accepted.
> 
> **M1**: Correct use of exponentials, with the constant written as a multiplier rather than left in the exponent.
> 
> **M1**: Use of $N = 3$ when $t = 0$ to find the constant.
> 
> **M1**: Use of $N = 10$ when $t = 10$ together with logarithms to find $k$. Taking logarithms of both sides must be visible.
> 
> **A1**: Correct particular solution. The decimal form $N = 3 \text{e}^{0.0120t^{2}}$ is accepted, as is any equivalent exact form such as `N = 3\left(\dfrac{10}{3}\right)^{\frac{t^{2}}{100}}`.
Action must come before 30 trees are infected, so the model must satisfy $N < 30$

`3\text{e}^{\frac{1}{100}\text{ln}\left(\frac{10}{3}\right)t^{2}} < 30`

Divide both sides by 3

`\text{e}^{\frac{1}{100}\text{ln}\left(\frac{10}{3}\right)t^{2}} < 10`

**[M1]**

Take natural logarithms of both sides, which preserves the direction because the logarithm is an increasing function

`\dfrac{1}{100}\text{ln}\left(\dfrac{10}{3}\right)t^{2} < \text{ln}\left(10\right)`

**[M1]**

Rearrange for $t^{2}$

`t^{2} < \dfrac{100\,\text{ln}\left(10\right)}{\text{ln}\left(\dfrac{10}{3}\right)} = 191.249\ldots`

Take the positive square root, since time cannot be negative

$t < 13 . 8$* days (3 s.f.)*

**[A1]**

Only whole days are useful to the scientists, and acting once the time has passed is too late

**Final answer:** **The scientists have about 13 days to act, since acting on day 14 would be too late**

**[A1]**

> **[exam-tip]**
> Carry the exact value of $k$ through this question rather than the rounded 0.0120. Using the rounded value gives 13.9 days instead of 13.8, and although both round to 14 they are different answers to 3 significant figures.

> **[mark-scheme]**
> **M1**: The particular solution set against 30 and divided through by 3, reaching an exponential on its own.
> 
> **M1**: Natural logarithms taken of both sides, correctly bringing the exponent down.
> 
> **A1**: Correct value of 13.8 days, or answers which round to it. Because premature rounding of $k$ leads to 13.9, that value is also accepted here.
> 
> **A1**: Correct conclusion in context, identifying 13 whole days. An answer of 13.8 days alone does not earn this mark, because the question asks how many days the scientists have.
