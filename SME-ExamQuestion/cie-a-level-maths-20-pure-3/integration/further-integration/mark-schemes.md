# Mark Schemes — Further Integration
**Integration** · Cambridge (CIE) A-LEVEL maths (9709)


## Exam Questions (61 questions)


### Q1
The index $a x + b$ has derivative $a$, so integrating brings out a factor of $\frac{1}{a}$. This is where the condition $a \neq 0$ is needed

`\int_{0}^{1} \text{e}^{ax+b} \, \text{d}x = \dfrac{1}{a}\left[\text{e}^{ax+b}\right]_{0}^{1}`

**[M1]**

Substitute the limits

`= \dfrac{1}{a}\left(\text{e}^{a(1)+b} - \text{e}^{a(0)+b}\right) \\ = \dfrac{1}{a}\left(\text{e}^{a+b} - \text{e}^{b}\right)`

**[A1]**

Both terms share a factor of $\text{e}^{b}$, since $\text{e}^{a+b} = \text{e}^{a} \text{e}^{b}$, so factorise it out to reach the required form

`\int_{0}^{1} \text{e}^{ax + b} \, \text{d}x = \text{e}^{b}\left(\frac{\text{e}^{a} - 1}{a}\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct integration, reaching $\frac{1}{a} \text{e}^{ax+b}$ with the limits attached.
> 
> **A1**: Correct substitution of both limits, giving `\dfrac{1}{a}\left(\text{e}^{a+b} - \text{e}^{b}\right)` or equivalent.
> 
> **A1**: Correct factorisation to reach the given result, using $\text{e}^{a+b} = \text{e}^{a} \text{e}^{b}$. Because the answer is printed, the unfactorised form must be seen first. You are not required to comment on the condition $a \neq 0$.
The integrand and the lower limit are unchanged, so the integrated expression from part (a) still applies. Only the upper limit is different

`\int_{0}^{c} \text{e}^{ax+b} \, \text{d}x = \dfrac{1}{a}\left[\text{e}^{ax+b}\right]_{0}^{c} = \dfrac{1}{a}\left(\text{e}^{ac+b} - \text{e}^{b}\right)`

**[M1]**

Factor out $\text{e}^{b}$ exactly as before

`\int_{0}^{c} \text{e}^{ax + b} \, \text{d}x = \text{e}^{b}\left(\frac{\text{e}^{ac} - 1}{a}\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the integrated expression with the new upper limit, reaching `\dfrac{1}{a}\left(\text{e}^{ac+b} - \text{e}^{b}\right)` or equivalent. Re-deriving the integral from scratch is equally acceptable.
> 
> **A1**: Correct answer `\text{e}^{b}\left(\dfrac{\text{e}^{ac} - 1}{a}\right)`. Accept any equivalent form, including the unfactorised $\frac{\text{e}^{ac+b}-\text{e}^{b}}{a}$.

### Q2
Write the tangent as a fraction so that the logarithmic form appears

`\int \text{tan} \; kx \, \text{d}x = \int \frac{\text{sin} \; kx}{\text{cos} \; kx} \, \text{d}x`

The denominator differentiates to $- k  \text{sin}  k x$, so insert that on the top and compensate with $- \frac{1}{k}$ outside

`= -\dfrac{1}{k}\int \frac{-k\,\text{sin} \; kx}{\text{cos} \; kx} \, \text{d}x`

**[M1]**

The integrand now has the form $\frac{\text{f}'(x)}{\text{f}(x)}$, so it integrates to the logarithm of the denominator

`= -\dfrac{1}{k}\,\text{ln} \; |\text{cos} \; kx| + c`

**[A1]**

Move the minus sign inside using the power law, then use $\text{sec}  A \equiv \frac{1}{\text{cos}A}$ to reach the required form

`= \dfrac{1}{k}\,\text{ln} \; \left|\dfrac{1}{\text{cos} \; kx}\right| + c`

`\int \text{tan} \; kx \, \text{d}x = \frac{1}{k}\,\text{ln} \; |\text{sec} \; kx| + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $\text{tan}  k x \equiv \frac{\text{sin}kx}{\text{cos}kx}$ together with a correct adjustment for the constant $k$.
> 
> **A1**: Correct integration to `-\dfrac{1}{k}\,\text{ln} \; |\text{cos} \; kx| + c`, or equivalent. Modulus signs are condoned.
> 
> **A1**: Correct conversion to the printed secant form. Because the answer is given, the step moving the minus sign inside the logarithm must be visible.
The denominator contains $\text{cot}  3 θ$, so differentiate it and compare with the numerator

$\text{f} ( θ ) = \text{cot}  3 θ  \Rightarrow  \text{f} ' ( θ ) = - 3  \text{cosec}^{2}  3 θ$

**[M1]**

The numerator is $\text{cosec}^{2}  3 θ$, which is $- \frac{1}{3}$ of that derivative, and the denominator already carries a 3. Adjust and compensate with $- \frac{1}{9}$ outside

`\int_{\frac{1}{18}\pi}^{\frac{1}{9}\pi} \frac{\text{cosec}^{2} \; 3\theta}{3\,\text{cot} \; 3\theta} \, \text{d}\theta = -\dfrac{1}{9}\int_{\frac{1}{18}\pi}^{\frac{1}{9}\pi} \frac{-3\,\text{cosec}^{2} \; 3\theta}{\text{cot} \; 3\theta} \, \text{d}\theta`

**[M1]**

The integrand now has the form $\frac{\text{f}'}{\text{f}}$, so it integrates to a logarithm

`= -\dfrac{1}{9}\left[\text{ln} \; |\text{cot} \; 3\theta|\right]_{\frac{1}{18}\pi}^{\frac{1}{9}\pi}`

**[A1]**

Substitute the limits

`= -\dfrac{1}{9}\left(\text{ln} \; \left|\text{cot} \; 3\left(\frac{1}{9}\pi\right)\right| - \text{ln} \; \left|\text{cot} \; 3\left(\frac{1}{18}\pi\right)\right|\right) \\ = -\dfrac{1}{9}\left(\text{ln} \; \left|\text{cot} \; \frac{\pi}{3}\right| - \text{ln} \; \left|\text{cot} \; \frac{\pi}{6}\right|\right) \\ = -\dfrac{1}{9}\left(\text{ln} \; \dfrac{1}{\sqrt{3}} - \text{ln} \; \sqrt{3}\right)`

**[M1]**

Write $\text{ln}  \frac{1}{\sqrt{3}}$ as $- \text{ln}  \sqrt{3}$, so the bracket becomes $- 2  \text{ln}  \sqrt{3}$, then use the power law to turn $2  \text{ln}  \sqrt{3}$ into $\text{ln}  3$

`= -\dfrac{1}{9}\left(-2\,\text{ln} \; \sqrt{3}\right) = \dfrac{1}{9}\,\text{ln} \; \left(\sqrt{3}\right)^{2}`

`\int_{\frac{1}{18}\pi}^{\frac{1}{9}\pi} \frac{\text{cosec}^{2} \; 3\theta}{3 \, \text{cot} \; 3\theta} \, \text{d}\theta = \frac{1}{9}\,\text{ln} \; 3`

**[A1]**

> **[exam-tip]**
> Resist the urge to simplify the integrand with trigonometric identities before integrating: it looks inviting, but it leads somewhere much harder. Differentiating the denominator first and checking it against the numerator is the quicker route.

> **[mark-scheme]**
> **M1**: Correct differentiation of $\text{cot}  3 θ$ to give $- 3  \text{cosec}^{2}  3 θ$.
> 
> **M1**: Correct adjustment so the integrand takes the form $\frac{\text{f}'}{\text{f}}$, with $- \frac{1}{9}$ outside.
> 
> **A1**: Correct integration to `-\dfrac{1}{9}\,\text{ln} \; |\text{cot} \; 3\theta|` with the limits attached. Modulus signs are condoned.
> 
> **M1**: Correct substitution of both limits, with the exact cotangent values used.
> 
> **A1**: Correct exact value $\frac{1}{9}  \text{ln}  3$, identifying $a = \frac{1}{9}$ and $b = 3$. Accept any exact equivalent, such as $\frac{2}{9}  \text{ln}  \sqrt{3}$, provided the required rational form is also stated. A decimal does not earn this mark.

### Q3
Take the left-hand side first. The denominator has derivative $a$, and the numerator is $2 a$, so the integral is $2  \text{ln}$ of the denominator

`\int_{0}^{1} \frac{2a}{ax+b} \, \text{d}x = \left[2\,\text{ln} \; |ax+b|\right]_{0}^{1} = 2\,\text{ln} \; |a+b| - 2\,\text{ln} \; |b|`

**[M1]**

Use the power law to move each 2 inside, then the subtraction law to combine into one logarithm

`= \text{ln} \; (a+b)^{2} - \text{ln} \; b^{2} = \text{ln} \; \left(\frac{a+b}{b}\right)^{2}`

**[A1]**

Now the right-hand side, which is the standard logarithmic integral

`\int_{b}^{2a} \frac{1}{x} \, \text{d}x = \left[\text{ln} \; |x|\right]_{b}^{2a} = \text{ln} \; |2a| - \text{ln} \; |b|`

**[M1]**

Combine these into a single logarithm as well

`= \text{ln} \; \left|\frac{2a}{b}\right|`

**[A1]**

Setting the two sides equal, the logarithms can be removed because the logarithm function takes each value only once

`\left(\frac{a+b}{b}\right)^{2} = \left|\frac{2a}{b}\right|`

**[M1]**

Now use the assumption being tested: if $a$ and $b$ are both positive then $\frac{2a}{b}$ is positive, so the modulus can be removed. Multiply through by $b^{2}$ and expand

$\frac{a^{2}+2ab+b^{2}}{b^{2}} = \frac{2a}{b}  \Rightarrow  a^{2} + 2 a b + b^{2} = 2 a b$

**[M1]**

The $2 a b$ terms cancel from both sides

$a^{2} + b^{2} = 0$

A sum of two squares is zero only when both are zero, so the only solution is $a = 0$ and $b = 0$, and neither is positive. That contradicts the assumption

**Final answer:** **Since a squared and b squared are both non-negative, a = 0 and b = 0 is the only solution, so there are no positive values of a and b that satisfy the equation**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct integration of the left-hand side, reaching a multiple of `\text{ln} \; |ax+b|` with the limits used.
> 
> **A1**: Correct left-hand side as a single logarithm, `\text{ln} \; \left(\dfrac{a+b}{b}\right)^{2}`, or any equivalent form.
> 
> **M1**: Correct integration of the right-hand side, reaching `\text{ln} \; |x|` with the limits used.
> 
> **A1**: Correct right-hand side as a single logarithm, `\text{ln} \; \left|\dfrac{2a}{b}\right|`, or equivalent.
> 
> **M1**: Correct removal of the logarithms to equate the two arguments.
> 
> **M1**: Correct expansion and simplification, using the positivity of $a$ and $b$ to remove the modulus.
> 
> **A1**: Correct conclusion that $a^{2} + b^{2} = 0$ forces $a = b = 0$, together with a clear statement that this means no positive values exist. Reaching $a^{2} + b^{2} = 0$ without drawing the conclusion does not earn this mark.

### Q4
Write $A = θ + \frac{π}{8}$ to keep the working readable. The two brackets are a sum and a difference of the same pair, so their product is a difference of two squares

`\left(\text{cos} \; A + \text{sin} \; A\right)\left(\text{sin} \; A - \text{cos} \; A\right) = \text{sin}^{2} A - \text{cos}^{2} A`

**[M1]**

The double-angle formula gives $\text{cos}  2 A \equiv \text{cos}^{2} A - \text{sin}^{2} A$, which is the negative of the expression above

`\text{sin}^{2} A - \text{cos}^{2} A = -\left(\text{cos}^{2} A - \text{sin}^{2} A\right) = -\text{cos} \; 2A`

**[M1]**

Substitute back, so that $2 A = 2 θ + \frac{π}{4}$

`\left(\text{cos} \left(\theta + \frac{\pi}{8}\right) + \text{sin} \left(\theta + \frac{\pi}{8}\right)\right)\left(\text{sin} \left(\theta + \frac{\pi}{8}\right) - \text{cos} \left(\theta + \frac{\pi}{8}\right)\right) \equiv -\text{cos} \left(2\theta + \frac{\pi}{4}\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct expansion of the product, either as a difference of two squares or by multiplying out in full, reaching $\text{sin}^{2} A - \text{cos}^{2} A$ or its expanded equivalent.
> 
> **M1**: Correct use of a double-angle formula, recognising the expression as $- \text{cos}  2 A$.
> 
> **A1**: Correct substitution back to reach the given result, with the doubled angle written as $2 θ + \frac{π}{4}$. Because the result is given, the intermediate form must be visible.
The integrand is exactly the expanded form from part (a), so replace it with the single cosine term

`\int_{0}^{\frac{1}{8}\pi} \left(\text{sin}^{2} \left(\theta + \frac{\pi}{8}\right) - \text{cos}^{2} \left(\theta + \frac{\pi}{8}\right)\right) \text{d}\theta = \int_{0}^{\frac{1}{8}\pi} -\text{cos} \left(2\theta + \frac{\pi}{4}\right) \text{d}\theta`

**[M1]**

The bracket has derivative 2, so insert that factor and compensate with $- \frac{1}{2}$ outside, then integrate

`= -\dfrac{1}{2}\int_{0}^{\frac{1}{8}\pi} 2\,\text{cos} \left(2\theta + \frac{\pi}{4}\right) \text{d}\theta = -\dfrac{1}{2}\left[\text{sin} \left(2\theta + \frac{\pi}{4}\right)\right]_{0}^{\frac{1}{8}\pi}`

**[M1]**

Substitute the limits

`= -\dfrac{1}{2}\left(\text{sin} \left(2\left(\frac{1}{8}\pi\right) + \frac{\pi}{4}\right) - \text{sin} \left(2(0) + \frac{\pi}{4}\right)\right) \\ = -\dfrac{1}{2}\left(\text{sin} \; \frac{\pi}{2} - \text{sin} \; \frac{\pi}{4}\right) \\ = -\dfrac{1}{2}\left(1 - \frac{\sqrt{2}}{2}\right)`

Multiply out and write over a common denominator

`\int_{0}^{\frac{1}{8}\pi} \left(\text{sin}^{2} \left(\theta + \frac{\pi}{8}\right) - \text{cos}^{2} \left(\theta + \frac{\pi}{8}\right)\right) \text{d}\theta = -\frac{2 - \sqrt{2}}{4}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the result from part (a) to replace the integrand with `-\text{cos} \left(2\theta + \dfrac{\pi}{4}\right)`, or an equivalent correct use of a double-angle formula.
> 
> **M1**: Correct integration, reaching a multiple of `\text{sin} \left(2\theta + \dfrac{\pi}{4}\right)` with the limits attached.
> 
> **A1**: Correct exact value $- \frac{2-\sqrt{2}}{4}$. Accept any exact equivalent, such as $\frac{\sqrt{2}-2}{4}$ or $\frac{\sqrt{2}}{4} - \frac{1}{2}$. Because the question asks for the exact value, a decimal such as -0.146 does not earn this mark.

### Q5
Nothing can be integrated while it sits inside a squared bracket, so expand it first

`\left(2\,\text{tan} \; x + 3\,\text{sec} \; x\right)^{2} = 4\,\text{tan}^{2} x + 12\,\text{tan} \; x \, \text{sec} \; x + 9\,\text{sec}^{2} x`

**[M1 A1]**

There is no standard integral for $\text{tan}^{2} x$, so use the identity $\text{tan}^{2} x + 1 \equiv \text{sec}^{2} x$ to replace it

`4\,\text{tan}^{2} x = 4\left(\text{sec}^{2} x - 1\right)`

**[M1]**

Substitute that in and collect the two $\text{sec}^{2} x$ terms, which gives $4 + 9 = 13$

`\int \left(2\,\text{tan} \; x + 3\,\text{sec} \; x\right)^{2} \text{d}x = \int \left(13\,\text{sec}^{2} x + 12\,\text{tan} \; x \, \text{sec} \; x - 4\right) \text{d}x`

**[A1]**

The list of formulae gives the integral of the first term directly

`\int \text{sec}^{2} x \, \text{d}x = \text{tan} \; x + c`

For the second term it gives the derivative of secant, and integrating reverses that

`\dfrac{\text{d}}{\text{d}x}\left(\text{sec} \; x\right) = \text{sec} \; x \, \text{tan} \; x`

`\int \text{tan} \; x \, \text{sec} \; x \, \text{d}x = \text{sec} \; x + c`

Integrate all three terms, with the constant giving $- 4 x$

`\int \left(2 \, \text{tan} \; x + 3 \, \text{sec} \; x\right)^{2} \text{d}x = 13\,\text{tan} \; x + 12\,\text{sec} \; x - 4x + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method to expand the squared bracket, producing three terms including the cross term.
> 
> **A1**: Correct expansion $4  \text{tan}^{2} x + 12  \text{tan}  x  \text{sec}  x + 9  \text{sec}^{2} x$.
> 
> **M1**: Correct use of the identity $\text{tan}^{2} x \equiv \text{sec}^{2} x - 1$.
> 
> **A1**: Correct simplified integrand $13  \text{sec}^{2} x + 12  \text{tan}  x  \text{sec}  x - 4$, or equivalent.
> 
> **A1**: Correct integral $13  \text{tan}  x + 12  \text{sec}  x - 4 x + c$, including the $- 4 x$ term. Reaching the $12  \text{sec}  x$ term by rewriting the integrand as $\frac{12\text{sin}x}{\text{cos}^{2}x}$ and using the reverse chain rule is equally acceptable. Any letter may be used for the constant.

### Q6
The integrand is a power of $\text{cos}  4 x$ multiplied by something close to its derivative, so start by differentiating the cube to see what the reverse chain rule produces

`\dfrac{\text{d}}{\text{d}x}\left(\text{cos}^{3} 4x\right) = 3\,\text{cos}^{2} 4x \times \left(-4\,\text{sin} \; 4x\right) = -12\,\text{cos}^{2} 4x \, \text{sin} \; 4x`

**[M1]**

That is $- 12$ times the integrand's trigonometric part, so insert the factor $- 12$ inside and compensate with $- \frac{5}{12}$ outside

`y = -\dfrac{5}{12}\int -12\,\text{cos}^{2} 4x \, \text{sin} \; 4x \, \text{d}x`

**[M1]**

Integrate and add the constant

$y = - \frac{5}{12} \text{cos}^{3} 4 x + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, recognising that the integrand is a multiple of the derivative of $\text{cos}^{3} 4 x$, or an equivalent substitution such as $u = \text{cos}  4 x$.
> 
> **M1**: Correct adjustment of the constant, reaching a multiple of $\text{cos}^{3} 4 x$.
> 
> **A1**: Correct expression $y = - \frac{5}{12} \text{cos}^{3} 4 x + c$, with the minus sign and both parts of the fraction right. Any letter may be used for the constant.
Integrating a bracket to the fourth power produces a fifth power

Consider differentiating `\left(5x^{2}+4\right)^{5}`, which brings down a 5 from the power and a $10 x$ from the chain rule on the bracket

`\dfrac{\text{d}}{\text{d}x}\left[\left(5x^{2}+4\right)^{5}\right] = 5 \times 10x \times \left(5x^{2}+4\right)^{4} \\ = 50x\left(5x^{2}+4\right)^{4}`

**[M1]**

The integrand has $3 x$ in front rather than $50 x$, so insert that factor and compensate with $\frac{3}{50}$ outside

`\int 3x\left(5x^{2}+4\right)^{4} \, \text{d}x = \dfrac{3}{50}\int 50x\left(5x^{2}+4\right)^{4} \, \text{d}x`

**[M1]**

The integrand is now the derivative of `\left(5x^{2}+4\right)^{5}`, so integrate and add the constant

`\int 3x\left(5x^{2} + 4\right)^{4} \, \text{d}x = \dfrac{3}{50}\left(5x^{2} + 4\right)^{5} + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, recognising that $3 x$ is a multiple of the derivative of $5 x^{2} + 4$, or an equivalent substitution such as $u = 5 x^{2} + 4$.
> 
> **M1**: Correct adjustment of the constant, reaching a multiple of `\left(5x^{2}+4\right)^{5}`.
> 
> **A1**: Correct integral `\dfrac{3}{50}\left(5x^{2}+4\right)^{5} + c`. Accept the expanded form. Any letter may be used for the constant.

### Q7
The integrand is a product, so use the formula for integration by parts, taking $u$ to be the power of $x$ since differentiating reduces its degree

`\int u \dfrac{\text{d}v}{\text{d}x} \, \text{d}x = uv - \int v \dfrac{\text{d}u}{\text{d}x} \, \text{d}x`

$u = x^{2} ,  \frac{\text{d}v}{\text{d}x} = \text{sin}  3 x ,  \frac{\text{d}u}{\text{d}x} = 2 x ,  v = - \frac{1}{3} \text{cos}  3 x$

**[M1]**

Substitute into the formula, and the two minus signs in the second term give a plus

`\int x^{2}\,\text{sin} \; 3x \, \text{d}x = -\dfrac{1}{3}x^{2}\,\text{cos} \; 3x + \dfrac{2}{3}\int x\,\text{cos} \; 3x \, \text{d}x`

**[A1]**

The remaining integral is still a product, so apply parts a second time with $u = x$

$u = x ,  \frac{\text{d}v}{\text{d}x} = \text{cos}  3 x ,  \frac{\text{d}u}{\text{d}x} = 1 ,  v = \frac{1}{3} \text{sin}  3 x$

`\int x\,\text{cos} \; 3x \, \text{d}x = \dfrac{1}{3}x\,\text{sin} \; 3x - \int \dfrac{1}{3}\text{sin} \; 3x \, \text{d}x`

**[M1]**

Substitute that back, keeping it in a bracket so the $\frac{2}{3}$ multiplies both terms

`= -\dfrac{1}{3}x^{2}\,\text{cos} \; 3x + \dfrac{2}{9}x\,\text{sin} \; 3x - \dfrac{2}{9}\int \text{sin} \; 3x \, \text{d}x`

**[A1]**

The last integral is standard, giving $- \frac{1}{3} \text{cos}  3 x$, so the two minus signs combine to a plus

$= - \frac{1}{3} x^{2}  \text{cos}  3 x + \frac{2}{9} x  \text{sin}  3 x + \frac{2}{27} \text{cos}  3 x + c$

**[A1]**

Write every term over a denominator of 27 and factorise, collecting the two cosine terms

`\int x^{2} \, \text{sin} \; 3x \, \text{d}x = \dfrac{1}{27}\left(\left(2 - 9x^{2}\right)\text{cos} \; 3x + 6x\,\text{sin} \; 3x\right) + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct first application of integration by parts, with $u = x^{2}$. A sign error in the parts formula is condoned for this mark.
> 
> **A1**: Correct result of the first application, reaching `-\dfrac{1}{3}x^{2}\,\text{cos} \; 3x + \dfrac{2}{3}\displaystyle\int x\,\text{cos} \; 3x \, \text{d}x`.
> 
> **M1**: Correct second application of integration by parts to the remaining integral.
> 
> **A1**: Correct expression after the second application, with the $\frac{2}{3}$ correctly distributed.
> 
> **A1**: Correct integration of the final standard integral, giving the $\frac{2}{27} \text{cos}  3 x$ term with the right sign.
> 
> **A1**: Correct final answer. Accept the unfactorised form $- \frac{1}{3} x^{2}  \text{cos}  3 x + \frac{2}{9} x  \text{sin}  3 x + \frac{2}{27} \text{cos}  3 x + c$; you are not required to factorise. Any letter may be used for the constant.
There is no standard integral for a logarithm, so treat this as a product and take $u = \text{ln}  x$, leaving the power of $x$ to be integrated

$u = \text{ln}  x ,  \frac{\text{d}v}{\text{d}x} = x^{-3} ,  \frac{\text{d}u}{\text{d}x} = \frac{1}{x} ,  v = - \frac{1}{2x^{2}}$

**[M1]**

Substitute into the parts formula

`\int \frac{\text{ln} \; x}{x^{3}} \, \text{d}x = -\frac{\text{ln} \; x}{2x^{2}} - \int \left(-\frac{1}{2x^{2}}\right)\left(\frac{1}{x}\right) \text{d}x`

**[A1]**

The two fractions inside the integral combine, and the double minus becomes a plus

`= -\frac{\text{ln} \; x}{2x^{2}} + \frac{1}{2}\int \frac{1}{x^{3}} \, \text{d}x = -\frac{\text{ln} \; x}{2x^{2}} + \frac{1}{2}\left(-\frac{1}{2x^{2}}\right) + c`

**[M1]**

Simplify, then factor out $- \frac{1}{4x^{2}}$

$= - \frac{\text{ln}x}{2x^{2}} - \frac{1}{4x^{2}} + c$

`\int \frac{\text{ln} \; x}{x^{3}} \, \text{d}x = -\frac{1}{4x^{2}}\left(1 + 2 \, \text{ln} \; x\right) + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct choice of $u = \text{ln}  x$ and $\frac{\text{d}v}{\text{d}x} = x^{-3}$, with correct $\frac{\text{d}u}{\text{d}x}$ and $v$.
> 
> **A1**: Correct substitution into the parts formula.
> 
> **M1**: Correct simplification of the remaining integral and correct integration of it.
> 
> **A1**: Correct final answer. Accept the unfactorised form $- \frac{\text{ln}x}{2x^{2}} - \frac{1}{4x^{2}} + c$ or any equivalent. Any letter may be used for the constant.

### Q8
The first two fractions have the same variable part, so simplify before integrating

$\frac{1}{x} + \frac{4}{2x} = \frac{1}{x} + \frac{2}{x} = \frac{3}{x}$

**[M1]**

In the third fraction the numerator 3 is already the derivative of $3 x - 2$, so it integrates to a logarithm with no adjusting

`\int_{2}^{6} \left(\frac{3}{x} + \frac{3}{3x-2}\right) \text{d}x = \left[3\,\text{ln} \; |x| + \text{ln} \; |3x-2|\right]_{2}^{6}`

**[A1]**

Substitute the limits, upper minus lower

`= \left(3\,\text{ln} \; |6| + \text{ln} \; |3(6)-2|\right) - \left(3\,\text{ln} \; |2| + \text{ln} \; |3(2)-2|\right) \\ = \left(3\,\text{ln} \; 6 + \text{ln} \; 16\right) - \left(3\,\text{ln} \; 2 + \text{ln} \; 4\right)`

**[M1]**

The answer must be in terms of prime bases, so break each logarithm down using the addition and power laws

$\text{ln}  6 = \text{ln}  2 + \text{ln}  3$

$\text{ln}  16 = \text{ln}  2^{4} = 4  \text{ln}  2$

$\text{ln}  4 = \text{ln}  2^{2} = 2  \text{ln}  2$

**[M1]**

Substitute these in and collect the $\text{ln}  2$ terms, which give $3 + 4 - 3 - 2 = 2$

`= 3\left(\text{ln} \; 2 + \text{ln} \; 3\right) + 4\,\text{ln} \; 2 - 3\,\text{ln} \; 2 - 2\,\text{ln} \; 2`

`\int_{2}^{6} \left(\frac{1}{x} + \frac{4}{2x} + \frac{3}{3x - 2}\right) \text{d}x = 3 \, \text{ln} \; 3 + 2 \, \text{ln} \; 2`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct simplification of $\frac{1}{x} + \frac{4}{2x}$ to $\frac{3}{x}$, or equivalent handling of the first two terms.
> 
> **A1**: Correct integration to `3\,\text{ln} \; |x| + \text{ln} \; |3x-2|`, with the limits attached. Modulus signs are condoned.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **M1**: Correct use of the logarithm laws to express the terms in prime bases, breaking down at least two of $\text{ln}  6$, $\text{ln}  16$ and $\text{ln}  4$.
> 
> **A1**: Correct final answer $3  \text{ln}  3 + 2  \text{ln}  2$, identifying $p = 3$ and $q = 2$. An answer left in an uncollected form such as $3  \text{ln}  6 + \text{ln}  16 - 3  \text{ln}  2 - \text{ln}  4$ does not earn this mark, because the question asks for the prime form. Accept the two terms in either order.

### Q9
The denominator is not yet fully factorised. $4 x^{2} - 1$ is a difference of two squares, so it splits into two linear factors, giving three in total

`\frac{8x^{2}-8x-1}{\left(4x^{2}-1\right)(x-2)} = \frac{8x^{2}-8x-1}{(2x+1)(2x-1)(x-2)} \equiv \frac{A}{2x+1} + \frac{B}{2x-1} + \frac{C}{x-2}`

**[B1]**

Multiply through by the denominator and compare numerators

$A ( 2 x - 1 ) ( x - 2 ) + B ( 2 x + 1 ) ( x - 2 ) + C ( 2 x + 1 ) ( 2 x - 1 ) \equiv 8 x^{2} - 8 x - 1$

Substitute the value of $x$ that makes two of the three brackets vanish, taking each factor in turn

$x = - \frac{1}{2} :  5 A = 5  \Rightarrow  A = 1$

$x = \frac{1}{2} :  - 3 B = - 3  \Rightarrow  B = 1$

**[M1]**

$x = 2 :  15 C = 15  \Rightarrow  C = 1$

All three constants are 1, so the decomposition is

`\frac{8x^{2}-8x-1}{\left(4x^{2}-1\right)(x-2)} = \frac{1}{2x+1} + \frac{1}{2x-1} + \frac{1}{x-2}`

**[A1]**

Now integrate. The first two denominators have derivative 2, so each needs adjusting and compensating, while the third needs nothing

`\int \left(\frac{1}{2x+1} + \frac{1}{2x-1} + \frac{1}{x-2}\right) \text{d}x = \int \left(\frac{1}{2}\left(\frac{2}{2x+1}\right) + \frac{1}{2}\left(\frac{2}{2x-1}\right) + \frac{1}{x-2}\right) \text{d}x`

**[M1]**

Each term is now in the form $\frac{\text{f}'(x)}{\text{f}(x)}$, so each integrates to a logarithm

`= \frac{1}{2}\,\text{ln} \; |2x+1| + \frac{1}{2}\,\text{ln} \; |2x-1|`

**[A1]**

Add the third term and the constant of integration

`\int \frac{8x^{2} - 8x - 1}{\left(4x^{2} - 1\right)(x - 2)} \, \text{d}x = \frac{1}{2}\,\text{ln} \; |2x + 1| + \frac{1}{2}\,\text{ln} \; |2x - 1| + \text{ln} \; |x - 2| + c`

**[A1]**

> **[mark-scheme]**
> **B1**: Correct form chosen, with $4 x^{2} - 1$ factorised into $( 2 x + 1 ) ( 2 x - 1 )$ and a constant numerator over each of the three linear factors.
> 
> **M1**: Correct method for finding the constants, either by substituting values of $x$ or by comparing coefficients. Either method is fully acceptable.
> 
> **A1**: All three constants correct, each equal to 1.
> 
> **M1**: Correct method for integrating the decomposition, adjusting for the coefficient of 2 in the first two denominators.
> 
> **A1**: Both half-logarithm terms correct, `\dfrac{1}{2}\,\text{ln} \; |2x+1|` and `\dfrac{1}{2}\,\text{ln} \; |2x-1|`.
> 
> **A1**: Fully correct answer, including `\text{ln} \; |x-2|` and the constant. Modulus signs are condoned throughout. A further simplification into a single logarithm, such as `\text{ln}\left(A|x-2|\sqrt{\left|4x^{2}-1\right|}\right)`, is acceptable but not required.

### Q10
The denominator must be factorised before it can be decomposed. Look for two brackets whose product gives $12 y^{2}$ and $36$ with a middle term of $43 y$

$12 y^{2} + 43 y + 36 = ( 3 y + 4 ) ( 4 y + 9 )$

**[M1]**

Two distinct linear factors, so each contributes a term with a constant numerator

$\frac{7y+13}{(3y+4)(4y+9)} \equiv \frac{A}{3y+4} + \frac{B}{4y+9}$

**[B1]**

Multiply through by the denominator and compare numerators

$7 y + 13 \equiv A ( 4 y + 9 ) + B ( 3 y + 4 )$

Substitute the values of $y$ that make each bracket vanish in turn

`y = -\dfrac{4}{3}: \quad 7\left(-\dfrac{4}{3}\right) + 13 = B\left(-4 + 4\right) + A\left(-\dfrac{16}{3} + 9\right) \quad \Rightarrow \quad \dfrac{11}{3} = \dfrac{11}{3}A \quad \Rightarrow \quad A = 1`

**[M1]**

`y = -\dfrac{9}{4}: \quad 7\left(-\dfrac{9}{4}\right) + 13 = B\left(-\dfrac{27}{4} + 4\right) \quad \Rightarrow \quad -\dfrac{11}{4} = -\dfrac{11}{4}B \quad \Rightarrow \quad B = 1`

Both constants are 1

$\frac{7y+13}{12y^{2}+43y+36} = \frac{1}{3y+4} + \frac{1}{4y+9}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct factorisation of the denominator into $( 3 y + 4 ) ( 4 y + 9 )$.
> 
> **B1**: Correct form chosen, with a constant numerator over each of the two linear factors.
> 
> **M1**: Correct method for finding the constants, either by substituting values of $y$ or by comparing coefficients. Either method is fully acceptable.
> 
> **A1**: Both constants correct, each equal to 1.
The integrand is part (a) with $y$ replaced by $x^{2}$ throughout, so the same decomposition applies

`\int \frac{7x^{2}+13}{12x^{4}+43x^{2}+36} \, \text{d}x = \int \left(\frac{1}{3x^{2}+4} + \frac{1}{4x^{2}+9}\right) \text{d}x`

**[M1]**

Both terms have a sum of two squares in the denominator, which looks like the standard result that integrates to an inverse tangent

`\int \frac{1}{x^{2}+a^{2}} \, \text{d}x = \frac{1}{a}\,\text{tan}^{-1}\left(\frac{x}{a}\right) + c`

That result needs a coefficient of 1 in front of $x^{2}$, so factor out of each denominator

`\frac{1}{3x^{2}+4} = \frac{1}{3}\left(\frac{1}{x^{2} + \left(\frac{2}{\sqrt{3}}\right)^{2}}\right)`

`\frac{1}{4x^{2}+9} = \frac{1}{4}\left(\frac{1}{x^{2} + \left(\frac{3}{2}\right)^{2}}\right)`

**[M1]**

Apply the result to the first term, with $a = \frac{2}{\sqrt{3}}$

`\frac{1}{3} \times \frac{\sqrt{3}}{2}\,\text{tan}^{-1}\left(\frac{\sqrt{3}}{2}x\right) = \frac{\sqrt{3}}{6}\,\text{tan}^{-1}\left(\frac{\sqrt{3}}{2}x\right)`

**[A1]**

Do the same for the second term, with $a = \frac{3}{2}$, then add the constant of integration

`\frac{1}{4} \times \frac{2}{3}\,\text{tan}^{-1}\left(\frac{2}{3}x\right) = \frac{1}{6}\,\text{tan}^{-1}\left(\frac{2}{3}x\right)`

`\int \frac{7x^{2} + 13}{12x^{4} + 43x^{2} + 36} \, \text{d}x = \frac{\sqrt{3}}{6}\,\text{tan}^{-1}\left(\frac{\sqrt{3}}{2}x\right) + \frac{1}{6}\,\text{tan}^{-1}\left(\frac{2}{3}x\right) + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the result from part (a) with $y = x^{2}$, giving $\frac{1}{3x^{2}+4} + \frac{1}{4x^{2}+9}$. This mark follows through from your answer to part (a).
> 
> **M1**: Correct method to rewrite at least one denominator in the form `k\left(x^{2}+a^{2}\right)`.
> 
> **A1**: One inverse tangent term fully correct, including its coefficient.
> 
> **A1**: Both inverse tangent terms fully correct, with the constant of integration. Accept $\text{arctan}$ notation and any equivalent exact form of the coefficients, such as $\frac{1}{2\sqrt{3}}$ in place of $\frac{\sqrt{3}}{6}$. Any letter may be used for the constant.

### Q11
The index of the exponential is $x^{3}$, so differentiate it to see what the reverse chain rule needs

`\dfrac{\text{d}}{\text{d}x}\left(x^{3}\right) = 3x^{2}`

**[M1]**

The integrand has $6 x^{2}$, which is exactly twice that, so write it as $2 \times 3 x^{2}$

`y = 2\int 3x^{2}\text{e}^{x^{3}} \, \text{d}x`

**[M1]**

The integrand is now the derivative of $\text{e}^{x^{3}}$, so integrate and add the constant

$y = 2 \text{e}^{x^{3}} + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, recognising that $6 x^{2}$ is a multiple of the derivative of the index $x^{3}$, or an equivalent substitution such as $u = x^{3}$.
> 
> **M1**: Correct adjustment of the constant, reaching a multiple of $\text{e}^{x^{3}}$.
> 
> **A1**: Correct expression $y = 2 \text{e}^{x^{3}} + c$. Any letter may be used for the constant.
The angle inside the sine is $( 4 x - 2 )^{2}$, so differentiate it, using the chain rule on the squared bracket

`\dfrac{\text{d}}{\text{d}x}\left[(4x-2)^{2}\right] = 2(4x-2) \times 4 = 32x - 16`

**[M1]**

Integrating a sine produces a cosine, so consider differentiating the cosine of that same angle. The cosine differentiates to minus a sine, and the chain rule brings down the derivative of the angle

`\dfrac{\text{d}}{\text{d}x}\left(\text{cos}\left[(4x-2)^{2}\right]\right) = -\text{sin}\left[(4x-2)^{2}\right] \times (32x-16) \\ = (16-32x)\,\text{sin}\left[(4x-2)^{2}\right]`

**[M1]**

That is exactly the integrand, so the integral needs no adjusting at all

`\int (16 - 32x) \, \text{sin} \left[(4x - 2)^{2}\right] \text{d}x = \text{cos} \left[(4x - 2)^{2}\right] + c`

**[A1]**

> **[exam-tip]**
> Read `\text{sin}\left[(4x-2)^2\right]` carefully: the squaring happens to the bracket, not to the sine, and the two mean entirely different things.

> **[mark-scheme]**
> **M1**: Correct differentiation of the angle $( 4 x - 2 )^{2}$ to give $32 x - 16$, or equivalent, by any valid route including a substitution $u = ( 4 x - 2 )^{2}$ or $u = 4 x - 2$.
> 
> **M1**: Correct method reaching a multiple of `\text{cos}\left[(4x-2)^{2}\right]` with the sign handled, either by differentiating the cosine of the angle and comparing the result with the integrand, or by recognising that $16 - 32 x$ is the negative of the derivative of the angle.
> 
> **A1**: Correct integral `\text{cos}\left[(4x-2)^{2}\right] + c`, with no fraction and a positive sign. Any letter may be used for the constant.

### Q12
Write $A = 2 θ + \frac{π}{4}$ to keep the working readable. The brackets are a sum and a difference of the same pair, so the product is a difference of two squares

`\left(1 + \text{cot} \; A\right)\left(1 - \text{cot} \; A\right) = 1 - \text{cot}^{2} A`

**[M1]**

The Pythagorean identity for cotangent gives $1 + \text{cot}^{2} A \equiv \text{cosec}^{2} A$, so rearrange it to replace $\text{cot}^{2} A$

$\text{cot}^{2} A \equiv \text{cosec}^{2} A - 1$

**[M1]**

Substitute that in, and the two constants combine

`1 - \text{cot}^{2} A = 1 - \left(\text{cosec}^{2} A - 1\right) = 2 - \text{cosec}^{2} A`

Replace $A$ to reach the required form

`\left(1 + \text{cot} \left(2\theta + \frac{\pi}{4}\right)\right)\left(1 - \text{cot} \left(2\theta + \frac{\pi}{4}\right)\right) \equiv 2 - \text{cosec}^{2} \left(2\theta + \frac{\pi}{4}\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct expansion of the product, reaching $1 - \text{cot}^{2} A$ or its equivalent in full.
> 
> **M1**: Correct use of the identity $1 + \text{cot}^{2} A \equiv \text{cosec}^{2} A$, rearranged to replace $\text{cot}^{2} A$.
> 
> **A1**: Correct simplification to reach the given result. Because the result is given, the substitution step must be visible.
Each bracket has a factor of 2, so take both out and the expression becomes 4 times the product from part (a)

`\text{f}'(\theta) = 4\left(1 + \text{cot} \left(2\theta + \frac{\pi}{4}\right)\right)\left(1 - \text{cot} \left(2\theta + \frac{\pi}{4}\right)\right) = 4\left(2 - \text{cosec}^{2} \left(2\theta + \frac{\pi}{4}\right)\right)`

**[M1]**

To recover $\text{f} ( θ )$, integrate. The list of formulae gives the derivative of cotangent

`\dfrac{\text{d}}{\text{d}x}\left(\text{cot} \; x\right) = -\text{cosec}^{2} x`

Apply the chain rule to the bracket $2 θ + \frac{π}{4}$, which has derivative 2

`\dfrac{\text{d}}{\text{d}\theta}\left(\text{cot} \left(2\theta + \frac{\pi}{4}\right)\right) = -2\,\text{cosec}^{2} \left(2\theta + \frac{\pi}{4}\right)`

So write $- 4  \text{cosec}^{2}$ as `2 \times \left(-2\,\text{cosec}^{2}\right)`, which is 2 times that derivative

`\text{f}(\theta) = \int \left(8 + 2\left(-2\,\text{cosec}^{2} \left(2\theta + \frac{\pi}{4}\right)\right)\right) \text{d}\theta`

**[M1]**

Integrate both terms and add the constant

`\text{f}(\theta) = 8\theta + 2 \, \text{cot} \left(2\theta + \frac{\pi}{4}\right) + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the result from part (a), taking the factor of 4 out to reach `8 - 4\,\text{cosec}^{2}\left(2\theta + \dfrac{\pi}{4}\right)`, or an equivalent correct expansion.
> 
> **M1**: Correct method for integrating the $\text{cosec}^{2}$ term, reaching a multiple of `\text{cot}\left(2\theta + \dfrac{\pi}{4}\right)`, with the constant adjusted for the chain rule.
> 
> **A1**: Correct expression `\text{f}(\theta) = 8\theta + 2\,\text{cot}\left(2\theta + \dfrac{\pi}{4}\right) + c`, with both terms and the sign right. Any letter may be used for the constant.

### Q13
The derivative cannot be integrated as it stands, so factor the 3 out of the denominator and use the Pythagorean identity $1 - \text{sin}^{2} A \equiv \text{cos}^{2} A$

`\text{f}'(\theta) = \frac{9}{3\left(1 - \text{sin}^{2}\left(3\theta - \frac{\pi}{6}\right)\right)} = \frac{3}{\text{cos}^{2}\left(3\theta - \frac{\pi}{6}\right)}`

**[M1]**

A reciprocal of a squared cosine is a squared secant

`\text{f}'(\theta) = 3\,\text{sec}^{2}\left(3\theta - \frac{\pi}{6}\right)`

**[A1]**

Now integrate. Since $\text{sec}^{2}$ integrates to $\text{tan}$ and the bracket has derivative 3, the coefficient 3 cancels exactly

`\text{f}(\theta) = \int 3\,\text{sec}^{2}\left(3\theta - \frac{\pi}{6}\right) \text{d}\theta = \text{tan}\left(3\theta - \frac{\pi}{6}\right) + c`

**[M1]**

Evaluate at the two given values, using the exact tangent values

`\text{f}\left(\frac{\pi}{6}\right) = \text{tan} \; \frac{\pi}{3} + c = \sqrt{3} + c`

`\text{f}\left(\frac{\pi}{9}\right) = \text{tan} \; \frac{\pi}{6} + c = \frac{\sqrt{3}}{3} + c`

**[M1]**

The question stated that `\left[\text{f}\left(\frac{\pi}{6}\right)\right]^{2} - \left[\text{f}\left(\frac{\pi}{9}\right)\right]^{2} = \frac{8}{3}\left(1 - \sqrt{3}\right)`

So square each and subtract. The $c^{2}$ terms appear in both and cancel, leaving an expression that is linear in $c$

`\left(3 + 2\sqrt{3}c + c^{2}\right) - \left(\frac{1}{3} + \frac{2\sqrt{3}}{3}c + c^{2}\right) = \frac{8}{3} + \frac{4\sqrt{3}}{3}c`

**[M1]**

Set this equal to the given value and solve for $c$

$\frac{8}{3} + \frac{4\sqrt{3}}{3} c = \frac{8}{3} - \frac{8\sqrt{3}}{3}  \Rightarrow  \frac{4\sqrt{3}}{3} c = - \frac{8\sqrt{3}}{3}  \Rightarrow  c = - 2$

Substitute the constant back

`\text{f}(\theta) = \text{tan}\left(3\theta - \frac{\pi}{6}\right) - 2`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method to simplify the derivative, factorising the 3 out and using $1 - \text{sin}^{2} A \equiv \text{cos}^{2} A$.
> 
> **A1**: Correct simplified derivative `3\,\text{sec}^{2}\left(3\theta - \dfrac{\pi}{6}\right)`, or equivalent.
> 
> **M1**: Correct integration, reaching `\text{tan}\left(3\theta - \dfrac{\pi}{6}\right) + c` with the coefficient handled.
> 
> **M1**: Correct evaluation of both function values, with the exact tangent values used.
> 
> **M1**: Correct expansion and subtraction of the two squares, reaching an expression linear in $c$.
> 
> **A1**: Correct value $c = - 2$ and correct final expression `\text{f}(\theta) = \text{tan}\left(3\theta - \dfrac{\pi}{6}\right) - 2`.

### Q14
To recover $\text{f} ( x )$, integrate the derivative. Write the tangent as a fraction so the logarithmic form appears

`\text{f}(x) = \int \frac{1}{4}\,\text{tan}\left(\frac{x}{2}\right) \text{d}x = \frac{1}{4}\int \frac{\text{sin}\left(\frac{x}{2}\right)}{\text{cos}\left(\frac{x}{2}\right)} \, \text{d}x`

The denominator differentiates to `-\dfrac{1}{2}\text{sin}\left(\dfrac{x}{2}\right)`, so insert that on the top and compensate with $- 2$, giving $\frac{1}{4} \times ( - 2 ) = - \frac{1}{2}$ outside

`= -\frac{1}{2}\int \frac{-\frac{1}{2}\text{sin}\left(\frac{x}{2}\right)}{\text{cos}\left(\frac{x}{2}\right)} \, \text{d}x`

**[M1]**

The integrand now has the form $\frac{\text{f}'(x)}{\text{f}(x)}$, so it integrates to a logarithm

`= -\frac{1}{2}\,\text{ln} \; \left|\text{cos}\left(\frac{x}{2}\right)\right| + c`

**[A1]**

Use the power law to move the minus sign inside, then $\text{sec}  A \equiv \frac{1}{\text{cos}A}$, then the power law again to turn the half into a square root

`-\frac{1}{2}\,\text{ln} \; \left|\text{cos}\left(\frac{x}{2}\right)\right| = \frac{1}{2}\,\text{ln} \; \left|\text{sec}\left(\frac{x}{2}\right)\right| = \text{ln} \; \sqrt{\left|\text{sec}\left(\frac{x}{2}\right)\right|}`

**[M1]**

Now apply the condition. Writing the given value as a square-root logarithm puts both sides in the same form, and $\text{sec}  \frac{π}{3} = 2$

`\text{f}\left(\frac{2\pi}{3}\right) = \text{ln} \; \sqrt{\left|\text{sec}\left(\frac{\pi}{3}\right)\right|} + c = \text{ln} \; \sqrt{2} + c`

$\frac{1}{2}  \text{ln}  6 = \text{ln}  \sqrt{6}$

**[M1]**

Equate and use the subtraction law to find the constant

$c = \text{ln}  \sqrt{6} - \text{ln}  \sqrt{2} = \text{ln}  \frac{\sqrt{6}}{\sqrt{2}} = \text{ln}  \sqrt{3}$

**[A1]**

Substitute the constant back and combine the two logarithms with the addition law

`\text{f}(x) = \text{ln} \; \sqrt{\left|\text{sec}\left(\frac{x}{2}\right)\right|} + \text{ln} \; \sqrt{3} = \text{ln} \; \left(\sqrt{3}\,\sqrt{\left|\text{sec}\left(\frac{x}{2}\right)\right|}\right)`

Bring the two square roots together under one sign

`\text{f}(x) = \text{ln} \; \sqrt{\left|3 \, \text{sec}\left(\frac{x}{2}\right)\right|}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method for integrating `\dfrac{1}{4}\,\text{tan}\left(\dfrac{x}{2}\right)`, writing it as a fraction and adjusting for the chain rule.
> 
> **A1**: Correct integral `-\dfrac{1}{2}\,\text{ln}\,\left|\text{cos}\left(\dfrac{x}{2}\right)\right| + c`, or equivalent. Modulus signs are condoned.
> 
> **M1**: Correct conversion into secant form and then into a square-root logarithm, using the power law.
> 
> **M1**: Correct substitution of the given condition, with $\text{sec}  \frac{π}{3} = 2$ used.
> 
> **A1**: Correct constant $c = \text{ln}  \sqrt{3}$, or any exact equivalent such as $\frac{1}{2}  \text{ln}  3$.
> 
> **A1**: Correct combination of the logarithms to reach the given result. Because the answer is printed, the step bringing the two square roots under one sign must be visible. An equivalent route that keeps everything as halves outside the logarithms and converts only at the end is acceptable.

### Q15
Neither factor gets simpler when differentiated, so name the integral before starting, since it will reappear

`I = \int \text{e}^{x} \, \text{sin} \; x \, \text{d}x`

Apply integration by parts, taking $u = \text{sin}  x$

$u = \text{sin}  x ,  \frac{\text{d}v}{\text{d}x} = \text{e}^{x} ,  \frac{\text{d}u}{\text{d}x} = \text{cos}  x ,  v = \text{e}^{x}$

**[M1]**

Substitute into the formula

`I = \text{e}^{x}\,\text{sin} \; x - \int \text{e}^{x}\,\text{cos} \; x \, \text{d}x`

**[A1]**

The new integral is no simpler, so apply parts again, keeping the same choice of which factor plays $u$

$u = \text{cos}  x ,  \frac{\text{d}v}{\text{d}x} = \text{e}^{x} ,  \frac{\text{d}u}{\text{d}x} = - \text{sin}  x ,  v = \text{e}^{x}$

**[M1]**

Substitute this in, keeping it inside a bracket so the minus sign reaches both terms

`I = \text{e}^{x}\,\text{sin} \; x - \left(\text{e}^{x}\,\text{cos} \; x - \int -\text{e}^{x}\,\text{sin} \; x \, \text{d}x\right)`

**[A1]**

Expand the bracket. The final integral is the original one back again

`I = \text{e}^{x}\,\text{sin} \; x - \text{e}^{x}\,\text{cos} \; x - \int \text{e}^{x}\,\text{sin} \; x \, \text{d}x = \text{e}^{x}\,\text{sin} \; x - \text{e}^{x}\,\text{cos} \; x - I`

**[M1]**

Both sides now contain $I$, so treat it as an unknown and collect it on one side

$2 I = \text{e}^{x}  \text{sin}  x - \text{e}^{x}  \text{cos}  x$

**[A1]**

Divide by 2 and factorise. The constant of integration is introduced at this point, since the indefinite integrals absorb into a single arbitrary constant

`\int \text{e}^{x} \, \text{sin} \; x \, \text{d}x = \frac{1}{2}\text{e}^{x}\left(\text{sin} \; x - \text{cos} \; x\right) + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct first application of integration by parts, with a valid choice of $u$ and $\frac{\text{d}v}{\text{d}x}$. A sign error in the parts formula is condoned for this mark.
> 
> **A1**: Correct result of the first application, `\text{e}^{x}\,\text{sin} \; x - \displaystyle\int \text{e}^{x}\,\text{cos} \; x \, \text{d}x`.
> 
> **M1**: Correct second application of integration by parts, consistent with the first.
> 
> **A1**: Correct expression after the second application, with the bracket handled so the minus sign reaches both terms.
> 
> **M1**: Correct recognition that the original integral has reappeared, and correct collection of the two occurrences onto one side.
> 
> **A1**: Correct rearranged equation $2 I = \text{e}^{x}  \text{sin}  x - \text{e}^{x}  \text{cos}  x$, or equivalent.
> 
> **A1**: Correct division by 2 and factorisation to reach the given result. Because the answer is printed, the rearrangement must be visible. Taking $u = \text{e}^{x}$ in both applications is an equally valid route and scores the same marks.

### Q16
Differentiate the denominator to see whether the integrand has the logarithmic form. The chain rule on the index gives $- 6 x$, and the $- 2$ in front reverses the sign again

`\dfrac{\text{d}}{\text{d}x}\left(3 - 2\text{e}^{-3x^{2}}\right) = -2 \times \left(-6x\right)\text{e}^{-3x^{2}} = 12x\text{e}^{-3x^{2}}`

**[M1]**

The numerator is $3 x \text{e}^{-3x^{2}}$, which is a quarter of this, so insert the factor 4 on the top and compensate with $\frac{1}{4}$ outside

`\int_{0}^{1} \frac{3x\text{e}^{-3x^{2}}}{3 - 2\text{e}^{-3x^{2}}} \, \text{d}x = \dfrac{1}{4}\int_{0}^{1} \frac{12x\text{e}^{-3x^{2}}}{3 - 2\text{e}^{-3x^{2}}} \, \text{d}x`

**[M1]**

The integrand now has the form $\frac{\text{f}'(x)}{\text{f}(x)}$, so it integrates to the logarithm of the denominator

`= \dfrac{1}{4}\left[\text{ln} \; \left|3 - 2\text{e}^{-3x^{2}}\right|\right]_{0}^{1}`

**[A1]**

Substitute the limits

`= \dfrac{1}{4}\left(\text{ln} \; \left|3 - 2\text{e}^{-3(1)^{2}}\right| - \text{ln} \; \left|3 - 2\text{e}^{-3(0)^{2}}\right|\right) \\ = \dfrac{1}{4}\left(\text{ln} \; \left|3 - 2\text{e}^{-3}\right| - \text{ln} \; |3 - 2|\right) \\ = \dfrac{1}{4}\left(\text{ln} \; \left(3 - 2\text{e}^{-3}\right) - \text{ln} \; 1\right)`

**[M1]**

Since $\text{ln}  1 = 0$ the second term vanishes, and $3 - 2 \text{e}^{-3}$ is positive so the modulus signs can be dropped

`\int_{0}^{1} \frac{3x\text{e}^{-3x^{2}}}{3 - 2\text{e}^{-3x^{2}}} \, \text{d}x = \frac{1}{4}\,\text{ln} \; \left(3 - 2\text{e}^{-3}\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct differentiation of the denominator, reaching $12 x \text{e}^{-3x^{2}}$, with both sign changes handled.
> 
> **M1**: Correct adjustment so that the numerator becomes the derivative of the denominator, with $\frac{1}{4}$ outside.
> 
> **A1**: Correct integration to `\dfrac{1}{4}\,\text{ln} \; \left|3 - 2\text{e}^{-3x^{2}}\right|` with the limits attached. Modulus signs are condoned, present or absent.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct simplification to the given result. Because the answer is printed, the step showing that the lower limit gives $\text{ln}  1 = 0$ must be visible. You are not required to comment on the sign of $3 - 2 \text{e}^{-3}$.

### Q17
A sum of two squares in the denominator looks like the standard result that integrates to an inverse tangent

`\int \frac{1}{x^{2}+a^{2}} \, \text{d}x = \frac{1}{a}\,\text{tan}^{-1}\left(\frac{x}{a}\right) + c`

That result needs a coefficient of 1 in front of $x^{2}$, so factor the 2 out of the denominator

`\frac{4}{9+2x^{2}} = \frac{4}{2}\left(\frac{1}{x^{2} + \frac{9}{2}}\right) = 2\left(\frac{1}{x^{2} + \left(\frac{3}{\sqrt{2}}\right)^{2}}\right)`

**[M1]**

Read $a$ off as the square root of the constant, which is irrational here

$a = \sqrt{\frac{9}{2}} = \frac{3}{\sqrt{2}}$

**[A1]**

Apply the result, then rationalise $\frac{1}{a} = \frac{\sqrt{2}}{3}$ and simplify $\frac{x}{a} = \frac{\sqrt{2}}{3} x$

`\int_{0}^{\sqrt{\frac{3}{2}}} \frac{4}{9+2x^{2}} \, \text{d}x = 2\left[\frac{\sqrt{2}}{3}\,\text{tan}^{-1}\left(\frac{\sqrt{2}}{3}x\right)\right]_{0}^{\sqrt{\frac{3}{2}}}`

**[M1]**

Substitute the limits

`= \frac{2\sqrt{2}}{3}\left(\text{tan}^{-1}\left(\frac{\sqrt{2}}{3}\sqrt{\frac{3}{2}}\right) - \text{tan}^{-1}\left(\frac{\sqrt{2}}{3}(0)\right)\right) \\ = \frac{2\sqrt{2}}{3}\left(\text{tan}^{-1}\frac{1}{\sqrt{3}} - \text{tan}^{-1} 0\right) \\ = \frac{2\sqrt{2}}{3}\left(\frac{\pi}{6} - 0\right)`

**[M1]**

Multiply out and cancel the factor of 2

$= \frac{2π\sqrt{2}}{18}$

`\int_{0}^{\sqrt{\frac{3}{2}}} \frac{4}{9 + 2x^{2}} \, \text{d}x = \frac{\pi\sqrt{2}}{9}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method to rewrite the denominator in the form `k\left(x^{2} + a^{2}\right)`, factorising the 2 out.
> 
> **A1**: Correct identification of $a = \frac{3}{\sqrt{2}}$, or equivalent such as $\frac{3\sqrt{2}}{2}$.
> 
> **M1**: Correct application of the standard inverse tangent result, reaching a multiple of `\text{tan}^{-1}\left(\dfrac{\sqrt{2}}{3}x\right)` with the limits attached.
> 
> **M1**: Correct substitution of both limits, with the exact value $\text{tan}^{-1} \frac{1}{\sqrt{3}} = \frac{π}{6}$ used.
> 
> **A1**: Correct simplification to the given result. Because the answer is printed, the unsimplified form such as $\frac{2π\sqrt{2}}{18}$ must be seen before the final line.

### Q18
The numerator has a common factor of 2, and the bracket that remains is the Pythagorean identity rearranged, since $\text{sin}^{2} θ \equiv 1 - \text{cos}^{2} θ$

`\frac{2 - 2\,\text{cos}^{2}\theta}{\text{sin} \; 2\theta} = \frac{2\left(1 - \text{cos}^{2}\theta\right)}{\text{sin} \; 2\theta} = \frac{2\,\text{sin}^{2}\theta}{\text{sin} \; 2\theta}`

**[M1]**

Expand the denominator with the double-angle formula $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$

$= \frac{2\text{sin}^{2}θ}{2\text{sin}θ\text{cos}θ}$

**[M1]**

Cancel the 2 and one factor of $\text{sin}  θ$ from top and bottom, which is valid because the condition $θ \neq k π$ guarantees $\text{sin}  θ \neq 0$

$= \frac{\text{sin}θ}{\text{cos}θ}$

Recognise this as the definition of the tangent

$\frac{2-2\text{cos}^{2}θ}{\text{sin}2θ} = \text{tan}  θ$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the Pythagorean identity to turn $1 - \text{cos}^{2} θ$ into $\text{sin}^{2} θ$, after factorising out the 2.
> 
> **M1**: Correct use of the double-angle formula to write $\text{sin}  2 θ$ as $2  \text{sin}  θ  \text{cos}  θ$.
> 
> **A1**: Correct cancellation leading to the given result, using $\text{tan}  θ \equiv \frac{\text{sin}θ}{\text{cos}θ}$. Because the result is given, the intermediate fraction $\frac{\text{sin}θ}{\text{cos}θ}$ must be visible. You are not required to comment on the condition $θ \neq k π$.
Part (a) replaces the whole integrand with a single tangent, which is a standard integral

`\int_{\frac{1}{6}\pi}^{\frac{1}{3}\pi} \frac{2 - 2\,\text{cos}^{2}\theta}{\text{sin} \; 2\theta} \, \text{d}\theta = \int_{\frac{1}{6}\pi}^{\frac{1}{3}\pi} \text{tan} \; \theta \, \text{d}\theta`

**[M1]**

Use the standard result that $\text{tan}  θ$ integrates to `\text{ln} \; |\text{sec} \; \theta|`

`= \left[\text{ln} \; |\text{sec} \; \theta|\right]_{\frac{1}{6}\pi}^{\frac{1}{3}\pi}`

**[A1]**

Evaluate the secant at each limit from its definition as the reciprocal of the cosine

$\text{sec}  \frac{π}{3} = \frac{1}{\text{cos}\frac{π}{3}} = 2$

$\text{sec}  \frac{π}{6} = \frac{1}{\text{cos}\frac{π}{6}} = \frac{2}{\sqrt{3}}$

Substitute both, upper minus lower

$= \text{ln}  2 - \text{ln}  \frac{2}{\sqrt{3}}$

**[M1]**

Split the second logarithm using the subtraction law, so the two $\text{ln}  2$ terms cancel

`= \text{ln} \; 2 - \left(\text{ln} \; 2 - \text{ln} \; \sqrt{3}\right) = \text{ln} \; \sqrt{3} = \text{ln} \; 3^{\frac{1}{2}}`

Bring the power down using the power law to reach the required form

`\int_{\frac{1}{6}\pi}^{\frac{1}{3}\pi} \frac{2 - 2 \, \text{cos}^{2} \theta}{\text{sin} \; 2\theta} \, \text{d}\theta = \frac{1}{2} \, \text{ln} \; 3`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the result from part (a) to replace the integrand with $\text{tan}  θ$.
> 
> **A1**: Correct integration to `\text{ln} \; |\text{sec} \; \theta|`, with the limits attached. Accept the equivalent form `-\text{ln} \; |\text{cos} \; \theta|`. Modulus signs are condoned.
> 
> **M1**: Correct substitution of both limits, with the exact secant or cosine values used.
> 
> **A1**: Correct use of the logarithm laws to reach the given result. Because the answer is printed, the step showing $\text{ln}  \sqrt{3} = \frac{1}{2} \text{ln}  3$ must be visible.

### Q19
A fraction of the form $\frac{1}{ax+b}$ integrates to a logarithm. The denominator has derivative 2, so insert that on the top and compensate with $\frac{1}{2}$ outside

`\text{f}(x) = \dfrac{5}{2}\int \frac{2}{2x+3} \, \text{d}x`

**[M1]**

The numerator is now the derivative of the denominator, so the integral is the logarithm of the denominator

`\text{f}(x) = \dfrac{5}{2}\,\text{ln} \; |2x + 3| + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, reaching a multiple of `\text{ln} \; |2x+3|`.
> 
> **A1**: Correct expression `\dfrac{5}{2}\,\text{ln} \; |2x+3| + c`. Modulus signs are condoned, present or absent. Accept `2.5\,\text{ln} \; |2x+3| + c` or `\text{ln} \; |2x+3|^{\frac{5}{2}} + c`. Any letter may be used for the constant.
To recover $y$, integrate each term separately. For the first, the index $3 x - 5$ has derivative 3, so integrating brings out a factor of $\frac{1}{3}$

`\int 2\text{e}^{3x-5} \, \text{d}x = \dfrac{2}{3}\text{e}^{3x-5}`

**[M1]**

For the second, the index $5 x$ has derivative 5, and the coefficient 5 cancels that factor exactly, so no fraction survives

`\int 5\text{e}^{5x} \, \text{d}x = 5 \times \dfrac{1}{5}\text{e}^{5x} = \text{e}^{5x}`

**[M1]**

Combine the two terms, keeping the subtraction, and add the constant of integration

$y = \frac{2}{3} \text{e}^{3x-5} - \text{e}^{5x} + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct integration of the first term, reaching a multiple of $\text{e}^{3x-5}$.
> 
> **M1**: Correct integration of the second term, reaching a multiple of $\text{e}^{5x}$.
> 
> **A1**: Fully correct expression $y = \frac{2}{3} \text{e}^{3x-5} - \text{e}^{5x} + c$, with both coefficients and the minus sign right. Any letter may be used for the constant.

### Q20
Integrating $\text{e}^{5x}$ brings out a factor of $\frac{1}{5}$, and integrating $\text{e}^{-5x}$ brings out $- \frac{1}{5}$. The coefficient 5 cancels both

`\int 5\left(\text{e}^{5x} - \text{e}^{-5x}\right) \text{d}x = 5\left(\dfrac{1}{5}\text{e}^{5x} - \left(-\dfrac{1}{5}\text{e}^{-5x}\right)\right)`

**[M1]**

The two minus signs in the second term combine to a plus

`\int 5\left(\text{e}^{5x} - \text{e}^{-5x}\right) \text{d}x = \text{e}^{5x} + \text{e}^{-5x} + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, reaching multiples of both $\text{e}^{5x}$ and $\text{e}^{-5x}$.
> 
> **A1**: Correct integral $\text{e}^{5x} + \text{e}^{-5x} + c$. The plus sign in front of the second term is needed. Any letter may be used for the constant.
Integrate each term, remembering that $\text{sin}  x$ integrates to $- \text{cos}  x$ and $\text{cos}  x$ integrates to $\text{sin}  x$

$y = - \text{cos}  x + \text{sin}  x + c$

**[M1]**

Write the terms in the conventional order and add the constant of integration

$y = \text{sin}  x - \text{cos}  x + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct integration of at least one of the two terms.
> 
> **A1**: Correct expression $y = \text{sin}  x - \text{cos}  x + c$, with both signs right. Accept the terms in either order. Any letter may be used for the constant.
Both limits are negative, so the modulus signs in the standard result matter here: without them the logarithm would be undefined at these values

`\int_{-8}^{-2} \frac{1}{x} \, \text{d}x = \left[\text{ln} \; |x|\right]_{-8}^{-2}`

**[M1]**

Substitute the limits, upper minus lower, taking the modulus of each

`= \text{ln} \; |-2| - \text{ln} \; |-8| = \text{ln} \; 2 - \text{ln} \; 8`

**[M1]**

Apply the subtraction law for logarithms to combine into one logarithm

`\int_{-8}^{-2} \frac{1}{x} \, \text{d}x = \text{ln} \; \frac{1}{4}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct integration of $\frac{1}{x}$ to a logarithm, with the limits attached.
> 
> **M1**: Correct substitution of both limits, upper minus lower, reaching $\text{ln}  2 - \text{ln}  8$ or equivalent.
> 
> **A1**: Correct single logarithm $\text{ln}  \frac{1}{4}$. Accept any exact equivalent, such as $- \text{ln}  4$ or $\text{ln}  0 . 25$. Modulus signs are condoned throughout, so working that omits them but reaches the correct value still earns full marks. An answer left as $\text{ln}  2 - \text{ln}  8$ does not earn this mark, because the question asks for a single logarithm.

### Q21
A product of a sine and a cosine at the same angle is exactly the right-hand side of the double-angle formula, so replace it with a single trigonometric term

$2  \text{sin}  x  \text{cos}  x \equiv \text{sin}  2 x$

`\int 2 \, \text{sin} \; x \, \text{cos} \; x \, \text{d}x = \int \text{sin} \; 2x \, \text{d}x`

**[M1]**

The bracket $2 x$ has derivative 2, so insert that factor and compensate with $- \frac{1}{2}$ outside, since $\text{cos}  2 x$ differentiates to $- 2  \text{sin}  2 x$

`\int 2 \, \text{sin} \; x \, \text{cos} \; x \, \text{d}x = -\dfrac{1}{2}\text{cos} \; 2x + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method by any valid route, either applying the double-angle formula, or recognising the integrand as a constant multiple of $\text{f} ' ( x ) \text{f} ( x )$.
> 
> **A1**: Correct integral. Accept any of the equivalent forms $- \frac{1}{2} \text{cos}  2 x + c$, $\text{sin}^{2} x + c$, or $- \text{cos}^{2} x + c$, since they differ only by a constant which the constant of integration absorbs. Any letter may be used for the constant.
Integrating a fifth power of a bracket produces a sixth power

Consider differentiating $( 4 x + 1 )^{6}$, which brings down a 6 from the power and a 4 from the chain rule on the bracket

`\dfrac{\text{d}}{\text{d}x}\left[(4x+1)^{6}\right] = 6 \times 4 \times (4x+1)^{5} \\ = 24(4x+1)^{5}`

Insert that factor of 24 inside the integral and compensate with $\frac{1}{24}$ outside

`\int_{1}^{3} (4x+1)^{5} \, \text{d}x = \dfrac{1}{24}\int_{1}^{3} 24(4x+1)^{5} \, \text{d}x`

**[M1]**

Integrate

`= \dfrac{1}{24}\left[(4x+1)^{6}\right]_{1}^{3}`

**[A1]**

Substitute the limits

`= \dfrac{1}{24}\left(\left(4(3)+1\right)^{6} - \left(4(1)+1\right)^{6}\right) \\ = \dfrac{1}{24}\left(13^{6} - 5^{6}\right) \\ = \dfrac{4811184}{24}`

**[M1]**

Evaluate

`\int_{1}^{3} (4x + 1)^{5} \, \text{d}x = 200466`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the reverse chain rule, reaching a multiple of $( 4 x + 1 )^{6}$.
> 
> **A1**: Correct integrated expression `\dfrac{1}{24}\left[(4x+1)^{6}\right]` with the limits still attached. Expanding the bracket and integrating term by term is a valid alternative method and earns this mark if correct.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct value $200466$.

### Q22
Differentiate the given substitution, recalling that $\text{ln}  x$ differentiates to $\frac{1}{x}$

$u = 2 + \text{ln}  x  \Rightarrow  \frac{\text{d}u}{\text{d}x} = \frac{1}{x}  \Rightarrow  \text{d} u = \frac{1}{x}  \text{d} x$

**[M1]**

The integrand already contains a factor of $\frac{1}{x}$, so group it with $\text{d} x$ and write the bracket as a negative power

`\int \frac{1}{x(2+\text{ln} \; x)^{3}} \, \text{d}x = \int (2 + \text{ln} \; x)^{-3}\left(\dfrac{1}{x} \, \text{d}x\right)`

**[M1]**

Replace $2 + \text{ln}  x$ by $u$ and $\frac{1}{x}  \text{d} x$ by $\text{d} u$, which leaves a simple power of $u$

`= \int u^{-3} \, \text{d}u`

**[A1]**

Integrate by raising the power by one and dividing by the new power

$= \frac{u^{-2}}{-2} + c = - \frac{1}{2} u^{-2} + c$

**[M1]**

Reverse the substitution and write the negative power as a fraction to reach the required form

$= - \frac{1}{2} ( 2 + \text{ln}  x )^{-2} + c$

`\int \frac{1}{x(2 + \text{ln} \; x)^{3}} \, \text{d}x = \frac{-1}{2(\text{ln} \; x + 2)^{2}} + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct differentiation of the substitution to give $\text{d} u = \frac{1}{x}  \text{d} x$, or equivalent.
> 
> **M1**: Correct rearrangement of the integrand so that $\frac{1}{x}  \text{d} x$ appears as a factor, with the bracket written as a negative power.
> 
> **A1**: Correct integral in $u$, `\displaystyle\int u^{-3} \, \text{d}u`, with no $x$ remaining.
> 
> **M1**: Correct integration of the power, reaching a multiple of $u^{-2}$.
> 
> **A1**: Correct reversal of the substitution and conversion to the printed form. Because the answer is given, the step from $- \frac{1}{2} ( 2 + \text{ln}  x )^{-2}$ to the fractional form must be visible. Note that $2 + \text{ln}  x$ and $\text{ln}  x + 2$ are the same, so either order in the bracket is acceptable.

### Q23
The denominator has a distinct linear factor and a repeated one. A repeated factor needs a term for each power, so the decomposition has three terms

$\frac{x^{2}-4x+7}{(x-1)(x-3)^{2}} \equiv \frac{A}{x-1} + \frac{B}{x-3} + \frac{C}{(x-3)^{2}}$

**[B1]**

Multiply through by the denominator and compare numerators

$x^{2} - 4 x + 7 \equiv A ( x - 3 )^{2} + B ( x - 1 ) ( x - 3 ) + C ( x - 1 )$

**[M1]**

Substituting $x = 1$ kills both terms containing $( x - 1 )$, and $x = 3$ kills both containing $( x - 3 )$

$x = 1 :  4 A = 4  \Rightarrow  A = 1$

$x = 3 :  2 C = 4  \Rightarrow  C = 2$

**[A1]**

No substitution isolates $B$, so use any third value of $x$ with the two known constants. Taking $x = 0$

$9 A + 3 B - C = 7  \Rightarrow  9 ( 1 ) + 3 B - 2 = 7  \Rightarrow  3 B = 0  \Rightarrow  B = 0$

Since $B = 0$, the middle term disappears from the decomposition

$\frac{x^{2}-4x+7}{(x-1)(x-3)^{2}} = \frac{1}{x-1} + \frac{2}{(x-3)^{2}}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct form chosen, with three terms including both $\frac{B}{x-3}$ and $\frac{C}{(x-3)^{2}}$ for the repeated factor.
> 
> **M1**: Correct method for finding the constants, either by substituting values of $x$ or by comparing coefficients. Either method is fully acceptable.
> 
> **A1**: Two constants correct.
> 
> **A1**: All three constants correct, giving the final decomposition $\frac{1}{x-1} + \frac{2}{(x-3)^{2}}$. Writing $\frac{0}{x-3}$ explicitly is acceptable.
Replace the integrand with the partial fractions from part (a). The two terms need different techniques, so treat them separately

`\int \frac{x^{2}-4x+7}{(x-1)(x-3)^{2}} \, \text{d}x = \int \left(\frac{1}{x-1} + \frac{2}{(x-3)^{2}}\right) \text{d}x`

**[M1]**

The first term has a numerator equal to the derivative of its denominator, so it integrates to a logarithm

`\int \frac{1}{x-1} \, \text{d}x = \text{ln} \; |x-1|`

**[A1]**

The second term is a power, not a logarithmic form, so write it as $2 ( x - 3 )^{-2}$ and use the rule for integrating powers

`\int 2(x-3)^{-2} \, \text{d}x = \frac{2(x-3)^{-1}}{-1} = -\frac{2}{x-3}`

Combine the two terms and add the constant of integration

`\int \frac{x^{2} - 4x + 7}{(x - 1)(x - 3)^{2}} \, \text{d}x = \text{ln} \; |x - 1| - \frac{2}{x - 3} + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the partial fractions from part (a) as the integrand. This mark follows through from your answer to part (a).
> 
> **A1**: Correct integration of the linear-denominator term to `\text{ln} \; |x-1|`. Modulus signs are condoned, present or absent.
> 
> **A1**: Correct integration of the squared term to $- \frac{2}{x-3}$, with the sign right, and a fully correct final answer. Accept $- 2 ( x - 3 )^{-1}$. Integrating this term to a logarithm does not earn this mark. Any letter may be used for the constant.

### Q24
The integrand is a product, so use the formula for integration by parts, taking $u$ to be the quadratic since differentiating reduces its degree

`\int u \dfrac{\text{d}v}{\text{d}x} \, \text{d}x = uv - \int v \dfrac{\text{d}u}{\text{d}x} \, \text{d}x`

$u = 2 x^{2} - 1 ,  \frac{\text{d}v}{\text{d}x} = \text{e}^{x} ,  \frac{\text{d}u}{\text{d}x} = 4 x ,  v = \text{e}^{x}$

**[M1]**

Substitute into the formula

`\int \left(2x^{2}-1\right)\text{e}^{x} \, \text{d}x = \left(2x^{2}-1\right)\text{e}^{x} - \int 4x\text{e}^{x} \, \text{d}x`

**[A1]**

The remaining integral is still a product, so apply parts a second time, now with $u = 4 x$

$u = 4 x ,  \frac{\text{d}v}{\text{d}x} = \text{e}^{x} ,  \frac{\text{d}u}{\text{d}x} = 4 ,  v = \text{e}^{x}$

`\int 4x\text{e}^{x} \, \text{d}x = 4x\text{e}^{x} - \int 4\text{e}^{x} \, \text{d}x`

The remaining integral is a standard exponential

$= 4 x \text{e}^{x} - 4 \text{e}^{x}$

**[M1]**

Substitute this back, keeping it in a bracket so the subtraction applies to both terms

`= \left(2x^{2}-1\right)\text{e}^{x} - \left(4x\text{e}^{x} - 4\text{e}^{x}\right) + c = \left(2x^{2}-1\right)\text{e}^{x} - 4x\text{e}^{x} + 4\text{e}^{x} + c`

**[A1]**

Every term has a factor of $\text{e}^{x}$, so factorise and collect the terms in the bracket

`\int \left(2x^{2} - 1\right)\text{e}^{x} \, \text{d}x = \left(2x^{2} - 4x + 3\right)\text{e}^{x} + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct first application of integration by parts, with $u$ taken as the quadratic. A sign error in the parts formula is condoned for this mark.
> 
> **A1**: Correct result of the first application, `\left(2x^{2}-1\right)\text{e}^{x} - \displaystyle\int 4x\text{e}^{x} \, \text{d}x`.
> 
> **M1**: Correct second application of integration by parts to the remaining integral.
> 
> **A1**: Correct expanded expression, with the minus sign correctly applied to both terms of the bracket.
> 
> **A1**: Correct factorised answer `\left(2x^{2} - 4x + 3\right)\text{e}^{x} + c`. Accept the unfactorised equivalent. Any letter may be used for the constant.
There is no standard integral for $\text{ln}  x$, so treat it as a product by writing it as $1 \times \text{ln}  x$, which makes integration by parts available

`\int \text{ln} \; x \, \text{d}x = \int 1 \times \text{ln} \; x \, \text{d}x`

**[M1]**

Take $u = \text{ln}  x$, since differentiating it gives something simpler, and let the 1 be the part that is integrated

$u = \text{ln}  x ,  \frac{\text{d}v}{\text{d}x} = 1 ,  \frac{\text{d}u}{\text{d}x} = \frac{1}{x} ,  v = x$

**[A1]**

Substitute into the parts formula

`= x \, \text{ln} \; x - \int x \times \dfrac{1}{x} \, \text{d}x`

**[M1]**

The $x$ terms cancel inside the remaining integral, leaving `\displaystyle\int 1 \, \text{d}x = x`

`\int \text{ln} \; x \, \text{d}x = x \, \text{ln} \; x - x + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, writing the integrand as $1 \times \text{ln}  x$ so that integration by parts can be used.
> 
> **A1**: Correct choice of $u = \text{ln}  x$ and $\frac{\text{d}v}{\text{d}x} = 1$, with correct $\frac{\text{d}u}{\text{d}x} = \frac{1}{x}$ and $v = x$.
> 
> **M1**: Correct substitution into the parts formula, reaching `x \, \text{ln} \; x - \displaystyle\int x \times \dfrac{1}{x} \, \text{d}x`.
> 
> **A1**: Correct simplification of the remaining integral to reach the given result. Because the answer is printed, the cancellation inside the integral must be visible.

### Q25
Take the constant $\frac{3}{2}$ outside, then differentiate the denominator to compare it with the numerator

`\text{f}(x) = \dfrac{3}{2}\int \frac{8x^{3}+3x}{4x^{4}+3x^{2}+5} \, \text{d}x`

`\dfrac{\text{d}}{\text{d}x}\left(4x^{4}+3x^{2}+5\right) = 16x^{3}+6x`

The derivative is exactly twice the numerator, so insert the missing factor of 2 and compensate, which turns $\frac{3}{2}$ into $\frac{3}{4}$

`\text{f}(x) = \dfrac{3}{4}\int \frac{16x^{3}+6x}{4x^{4}+3x^{2}+5} \, \text{d}x`

**[M1]**

The integrand now has the form $\frac{\text{f}'(x)}{\text{f}(x)}$, so it integrates to the logarithm of the denominator

`\text{f}(x) = \dfrac{3}{4}\,\text{ln} \; \left|4x^{4} + 3x^{2} + 5\right| + c`

**[A1]**

Substitute the given point, using $4 ( 1 )^{4} + 3 ( 1 )^{2} + 5 = 12$

$\frac{3}{4}  \text{ln}  12 + c = \text{ln}  144$

**[M1]**

Since $144 = 12^{2}$, the power law rewrites the right-hand side in terms of $\text{ln}  12$ so the two sides can be combined

$\text{ln}  144 = \text{ln}  12^{2} = 2  \text{ln}  12$

$\frac{3}{4}  \text{ln}  12 + c = 2  \text{ln}  12  \Rightarrow  c = \frac{5}{4}  \text{ln}  12$

**[M1]**

Substitute the constant back. Note that $4 x^{4} + 3 x^{2} + 5$ is positive for every $x$, so the modulus signs are optional here

`\text{f}(x) = \frac{3}{4}\,\text{ln} \; \left|4x^{4} + 3x^{2} + 5\right| + \frac{5}{4}\,\text{ln} \; 12`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct adjustment so that the numerator becomes the derivative of the denominator, with the resulting constant outside.
> 
> **A1**: Correct integral `\dfrac{3}{4}\,\text{ln} \; \left|4x^{4}+3x^{2}+5\right| + c`. Modulus signs are condoned, present or absent.
> 
> **M1**: Correct substitution of the point $( 1 ,  \text{ln}  144 )$ to form an equation in the constant.
> 
> **M1**: Correct use of the power law to write $\text{ln}  144$ as $2  \text{ln}  12$, or an equivalent route that expresses both sides in the same logarithm.
> 
> **A1**: Correct final expression, with $c = \frac{5}{4}  \text{ln}  12$. Accept any exact equivalent, such as $\text{ln}  12^{\frac{5}{4}}$, or a fully combined single logarithm. A decimal value for the constant does not earn this mark.

### Q26
The rule for integrating powers of $x$ needs every term written as a power, so rewrite the fraction using $\frac{1}{x^{n}} = x^{-n}$

`\int \left(x^{2} + 5 - \frac{3}{x^{2}}\right) \text{d}x = \int \left(x^{2} + 5 - 3x^{-2}\right) \text{d}x`

**[M1]**

Integrate term by term, using `\displaystyle\int x^{n} \, \text{d}x = \frac{x^{n+1}}{n+1} + c` for each power and `\displaystyle\int k \, \text{d}x = kx + c` for the constant

`= \frac{x^{3}}{3} + 5x - 3\left(\frac{x^{-1}}{-1}\right) + c`

**[A1]**

Dividing by $- 1$ turns the last term positive. Convert it back to a fraction to finish

`\int \left(x^{2} + 5 - \frac{3}{x^{2}}\right) \text{d}x = \frac{1}{3}x^{3} + 5x + \frac{3}{x} + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct conversion of $\frac{3}{x^{2}}$ to $3 x^{-2}$, or equivalent, so that the powers rule can be applied.
> 
> **A1**: Correct integration of all three terms, in any form. Accept the unsimplified version with $\frac{x^{-1}}{-1}$ still shown.
> 
> **A1**: Correct final answer $\frac{1}{3} x^{3} + 5 x + \frac{3}{x} + c$, with the sign of the last term correct. Accept $3 x^{-1}$ in place of $\frac{3}{x}$, and $\frac{x^{3}}{3}$ in place of $\frac{1}{3} x^{3}$. Any letter may be used for the constant.
The chain rule gives `\dfrac{\text{d}}{\text{d}x}\left(\text{e}^{3x}\right) = 3\text{e}^{3x}`, which is exactly the integrand, so the integral can be written down directly

`\int 3\text{e}^{3x} \, \text{d}x = \text{e}^{3x} + c`

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Correct method, reaching a multiple of $\text{e}^{3x}$.
> 
> **A1**: Correct integral $\text{e}^{3x} + c$. Because the question says to write the answer down, no working is required and a correct answer alone earns both marks. Any letter may be used for the constant.

### Q27
The double-angle formula $\text{cos}  2 A \equiv 1 - 2  \text{sin}^{2} A$ applies for any angle $A$, so take $A = 3 x + 2$, which makes $2 A = 6 x + 4$

$\text{cos}  ( 6 x + 4 ) \equiv 1 - 2  \text{sin}^{2} ( 3 x + 2 )$

**[M1]**

Rearrange to make the squared sine the subject, then divide by 2

$2  \text{sin}^{2} ( 3 x + 2 ) \equiv 1 - \text{cos}  ( 6 x + 4 )$

`\text{sin}^{2} (3x + 2) \equiv \frac{1}{2}\left(1 - \text{cos} \; (6x + 4)\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the double-angle formula with $A = 3 x + 2$, so that the doubled angle appears as $6 x + 4$.
> 
> **A1**: Correct rearrangement to reach the given result. Because the result is given, the rearrangement must be visible.
A squared sine cannot be integrated directly, so replace it using part (a) and split the bracket into two terms

`\int \text{sin}^{2}(3x+2) \, \text{d}x = \int \frac{1}{2}\left(1 - \text{cos} \; (6x+4)\right) \text{d}x = \int \left(\frac{1}{2} - \frac{1}{2}\text{cos} \; (6x+4)\right) \text{d}x`

**[M1]**

The bracket $6 x + 4$ has derivative 6, so insert that factor in the cosine term and compensate, giving $\frac{1}{2} \times \frac{1}{6} = \frac{1}{12}$ outside

`= \int \left(\frac{1}{2} - \frac{1}{12}\left(6\,\text{cos} \; (6x+4)\right)\right) \text{d}x`

**[M1]**

Integrate both terms and add the constant

`\int \text{sin}^{2} (3x + 2) \, \text{d}x = \frac{1}{2}x - \frac{1}{12}\text{sin} \; (6x + 4) + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the result from part (a) to replace the integrand, or an equivalent correct use of a double-angle formula.
> 
> **M1**: Correct method for integrating the cosine term, reaching a multiple of $\text{sin}  ( 6 x + 4 )$.
> 
> **A1**: Correct expression $\frac{1}{2} x - \frac{1}{12} \text{sin}  ( 6 x + 4 ) + c$, with both coefficients and the minus sign right. Any letter may be used for the constant.

### Q28
Multiply each term inside the bracket by $\text{e}^{2x}$, adding indices each time since $\text{e}^{a} \times \text{e}^{b} = \text{e}^{a+b}$

`\text{e}^{2x}\left(1 + \text{e}^{2x} + \text{e}^{2}\right) = \text{e}^{2x} + \text{e}^{2x}\text{e}^{2x} + \text{e}^{2x}\text{e}^{2}`

**[M1]**

Each index is now linear in $x$, as required

`\text{e}^{2x}\left(1 + \text{e}^{2x} + \text{e}^{2}\right) = \text{e}^{2x} + \text{e}^{4x} + \text{e}^{2x + 2}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct expansion of the bracket, multiplying each of the three terms by $\text{e}^{2x}$.
> 
> **A1**: All three indices correct, giving $\text{e}^{2x} + \text{e}^{4x} + \text{e}^{2x+2}$. Accept the terms in any order.
A product of exponentials cannot be integrated as it stands, which is why part (a) is needed: it turns the integrand into a sum of three standard exponentials

`\int_{0}^{1} \text{e}^{2x}\left(1 + \text{e}^{2x} + \text{e}^{2}\right) \text{d}x = \int_{0}^{1} \left(\text{e}^{2x} + \text{e}^{4x} + \text{e}^{2x+2}\right) \text{d}x`

**[M1]**

Integrate each term, dividing by the coefficient of $x$ in its index, so by 2, then 4, then 2

`= \left[\dfrac{1}{2}\text{e}^{2x} + \dfrac{1}{4}\text{e}^{4x} + \dfrac{1}{2}\text{e}^{2x+2}\right]_{0}^{1}`

**[A1]**

Substitute the limits

`= \left(\dfrac{1}{2}\text{e}^{2(1)} + \dfrac{1}{4}\text{e}^{4(1)} + \dfrac{1}{2}\text{e}^{2(1)+2}\right) - \left(\dfrac{1}{2}\text{e}^{2(0)} + \dfrac{1}{4}\text{e}^{4(0)} + \dfrac{1}{2}\text{e}^{2(0)+2}\right) \\ = \left(\dfrac{1}{2}\text{e}^{2} + \dfrac{1}{4}\text{e}^{4} + \dfrac{1}{2}\text{e}^{4}\right) - \left(\dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{2}\text{e}^{2}\right)`

**[M1]**

The two $\frac{1}{2} \text{e}^{2}$ terms cancel, and the remaining $\text{e}^{4}$ terms combine to give $\frac{3}{4} \text{e}^{4}$

$= \frac{3}{4} \text{e}^{4} - \frac{3}{4}$

Factor out $\frac{3}{4}$ to reach the required form

`\int_{0}^{1} \text{e}^{2x}\left(1 + \text{e}^{2x} + \text{e}^{2}\right) \text{d}x = \frac{3}{4}\left(\text{e}^{4} - 1\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the expansion from part (a) to replace the integrand with a sum of exponentials.
> 
> **A1**: Correct integration of all three terms, giving $\frac{1}{2} \text{e}^{2x} + \frac{1}{4} \text{e}^{4x} + \frac{1}{2} \text{e}^{2x+2}$ with the limits attached.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct simplification to the given result. Because the answer is printed, the cancellation of the $\text{e}^{2}$ terms and the collection of the $\text{e}^{4}$ terms must be visible.

### Q29
The denominator mixes a single and a double angle, so use the double-angle formula $\text{cos}  2 x \equiv 1 - 2  \text{sin}^{2} x$ to put everything in terms of $x$

`1 - \text{cos} \; 2x = 1 - \left(1 - 2\,\text{sin}^{2}x\right) = 2\,\text{sin}^{2}x`

**[M1]**

Substitute this back, and the 2 on the top cancels the 2 on the bottom

`\int_{\frac{1}{2}\pi}^{\frac{5}{6}\pi} \frac{2\,\text{cos} \; x}{1 - \text{cos} \; 2x} \, \text{d}x = \int_{\frac{1}{2}\pi}^{\frac{5}{6}\pi} \frac{2\,\text{cos} \; x}{2\,\text{sin}^{2}x} \, \text{d}x = \int_{\frac{1}{2}\pi}^{\frac{5}{6}\pi} \frac{\text{cos} \; x}{\text{sin}^{2}x} \, \text{d}x`

**[A1]**

Split the fraction into two factors, each of which is a reciprocal trigonometric function

$\frac{\text{cos}x}{\text{sin}^{2}x} = \frac{1}{\text{sin}x} \times \frac{\text{cos}x}{\text{sin}x}$

Apply $\text{cosec}  x \equiv \frac{1}{\text{sin}x}$ and $\text{cot}  x \equiv \frac{\text{cos}x}{\text{sin}x}$ to write the integrand as a single product

`= \int_{\frac{1}{2}\pi}^{\frac{5}{6}\pi} \text{cosec} \; x \, \text{cot} \; x \, \text{d}x`

**[M1]**

The list of formulae gives the derivative of cosecant

`\dfrac{\text{d}}{\text{d}x}\left(\text{cosec} \; x\right) = -\text{cosec} \; x \, \text{cot} \; x`

Integrating reverses that, so the integral is minus cosecant

`= \left[-\text{cosec} \; x\right]_{\frac{1}{2}\pi}^{\frac{5}{6}\pi} = \left[-\frac{1}{\text{sin} \; x}\right]_{\frac{1}{2}\pi}^{\frac{5}{6}\pi}`

**[A1]**

Substitute the limits, using $\text{sin}  \frac{5π}{6} = \frac{1}{2}$ and $\text{sin}  \frac{π}{2} = 1$

`= \left(-\frac{1}{\frac{1}{2}}\right) - \left(-\frac{1}{1}\right) \\ = -2 + 1`

**[M1]**

Evaluate

`\int_{\frac{1}{2}\pi}^{\frac{5}{6}\pi} \frac{2 \, \text{cos} \; x}{1 - \text{cos} \; 2x} \, \text{d}x = -1`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of a double-angle formula to write $1 - \text{cos}  2 x$ as $2  \text{sin}^{2} x$.
> 
> **A1**: Correct simplified integrand $\frac{\text{cos}x}{\text{sin}^{2}x}$, with the 2 cancelled.
> 
> **M1**: Correct rewriting of the integrand as $\text{cosec}  x  \text{cot}  x$, using the reciprocal identities. Writing it instead as `\left(\text{sin} \; x\right)^{-2}\text{cos} \; x`, ready for the reverse chain rule, is an equally valid route and earns this mark.
> 
> **A1**: Correct integrated expression $- \text{cosec}  x$, or the equivalent $- \frac{1}{\text{sin}x}$, with the limits attached. The derivative of $\text{cosec}  x$ is given in the list of formulae, so quoting it and reversing it is enough; you are not required to derive it. By the reverse chain rule route, raising the power of `\left(\text{sin} \; x\right)^{-2}` by one and dividing by the new power reaches the same expression.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct exact value $- 1$. The negative sign is needed.

### Q30
Differentiate the given substitution. Because it is not linear, the derivative still involves $x$

$u = 3 x^{2} + 1  \Rightarrow  \frac{\text{d}u}{\text{d}x} = 6 x  \Rightarrow  \text{d} u = 6 x  \text{d} x$

**[M1]**

The substitution needs $6 x  \text{d} x$ to appear, and the integrand has $8 x$, so split it as $\frac{4}{3} \times 6 x$

`\int 8x \, \text{sin} \; (3x^{2}+1) \, \text{d}x = \dfrac{4}{3}\int \text{sin} \; (3x^{2}+1) \times 6x \, \text{d}x`

**[M1]**

Replace $3 x^{2} + 1$ by $u$ and $6 x  \text{d} x$ by $\text{d} u$, which removes the $x$ entirely

`= \dfrac{4}{3}\int \text{sin} \; u \, \text{d}u`

**[A1]**

Integrate, remembering that $\text{sin}  u$ integrates to $- \text{cos}  u$

$= - \frac{4}{3} \text{cos}  u + c$

**[M1]**

Reverse the substitution to give the answer in terms of $x$

`\int 8x \, \text{sin} \; (3x^{2} + 1) \, \text{d}x = -\dfrac{4}{3}\text{cos} \; (3x^{2} + 1) + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct differentiation of the substitution to give $\text{d} u = 6 x  \text{d} x$, or equivalent such as $\text{d} x = \frac{\text{d}u}{6x}$.
> 
> **M1**: Correct handling of the coefficient so that $6 x  \text{d} x$ appears as a factor, or equivalent cancellation of the $x$ terms.
> 
> **A1**: Correct integral in $u$, `\dfrac{4}{3}\displaystyle\int \text{sin} \; u \, \text{d}u`, with no $x$ remaining.
> 
> **M1**: Correct integration, reaching a multiple of $\text{cos}  u$ with the sign handled.
> 
> **A1**: Correct final answer $- \frac{4}{3} \text{cos}  ( 3 x^{2} + 1 ) + c$, in terms of $x$. Reaching this directly by the reverse chain rule, without a substitution, is a valid method and scores full marks. Any letter may be used for the constant.

### Q31
To recover $\text{f} ( x )$, integrate the derivative. Write the tangent as a fraction so that the logarithmic form appears

`\text{f}(x) = \int 2\,\text{tan} \; 3x \, \text{d}x = 2\int \frac{\text{sin} \; 3x}{\text{cos} \; 3x} \, \text{d}x`

The denominator differentiates to $- 3  \text{sin}  3 x$, so insert that on the top and compensate with $- \frac{1}{3}$, which combines with the 2 already outside to give $- \frac{2}{3}$

`= -\dfrac{2}{3}\int \frac{-3\,\text{sin} \; 3x}{\text{cos} \; 3x} \, \text{d}x = -\dfrac{2}{3}\,\text{ln} \; |\text{cos} \; 3x| + c`

**[M1]**

The printed answer uses secant, so move the minus sign inside using the power law and apply $\text{sec}  A \equiv \frac{1}{\text{cos}A}$

`-\dfrac{2}{3}\,\text{ln} \; |\text{cos} \; 3x| = \dfrac{2}{3}\,\text{ln} \; \left|\dfrac{1}{\text{cos} \; 3x}\right| = \dfrac{2}{3}\,\text{ln} \; |\text{sec} \; 3x|`

`\text{f}(x) = \dfrac{2}{3}\,\text{ln} \; |\text{sec} \; 3x| + c`

**[A1]**

Use the given condition to find the constant, noting that $\text{sec}  0 = 1$ so the logarithm term vanishes

`\dfrac{2}{3}\,\text{ln} \; |\text{sec} \; 0| + c = \dfrac{2}{3} \quad \Rightarrow \quad \dfrac{2}{3}\,\text{ln} \; 1 + c = \dfrac{2}{3} \quad \Rightarrow \quad c = \dfrac{2}{3}`

**[M1]**

Substitute the constant back and factor out $\frac{2}{3}$ to reach the required form

`\text{f}(x) = \dfrac{2}{3}\,\text{ln} \; |\text{sec} \; 3x| + \dfrac{2}{3}`

`\text{f}(x) = \frac{2}{3}\left(1 + \text{ln} \; |\text{sec} \; 3x|\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method for integrating $2  \text{tan}  3 x$, reaching a multiple of `\text{ln} \; |\text{cos} \; 3x|` or `\text{ln} \; |\text{sec} \; 3x|`.
> 
> **A1**: Correct integral `\dfrac{2}{3}\,\text{ln} \; |\text{sec} \; 3x| + c`, or the equivalent `-\dfrac{2}{3}\,\text{ln} \; |\text{cos} \; 3x| + c`. Modulus signs are condoned.
> 
> **M1**: Correct substitution of $\text{f} ( 0 ) = \frac{2}{3}$ to form an equation in the constant, using $\text{ln}  1 = 0$.
> 
> **A1**: Correct value $c = \frac{2}{3}$ and correct factorisation to reach the given result. Because the answer is printed, the unfactorised form must be seen before the final line.

### Q32
Write the tangent in terms of sine and cosine, using $\text{tan}  A \equiv \frac{\text{sin}A}{\text{cos}A}$, so that the integrand becomes a fraction

`\int \text{tan} \; x \, \text{d}x = \int \frac{\text{sin} \; x}{\text{cos} \; x} \, \text{d}x`

**[M1]**

The denominator differentiates to $- \text{sin}  x$, so insert that minus sign on the top and compensate outside. The integrand then has the form $\frac{\text{f}'(x)}{\text{f}(x)}$

`= -\int \frac{-\text{sin} \; x}{\text{cos} \; x} \, \text{d}x = -\text{ln} \; |\text{cos} \; x| + c`

**[A1]**

The printed answer is in terms of secant, so use the power law for logarithms to move the minus sign into the argument

`= \text{ln} \; \left(|\text{cos} \; x|^{-1}\right) + c = \text{ln} \; \left(\frac{1}{|\text{cos} \; x|}\right) + c`

**[M1]**

Since $\text{sec}  A \equiv \frac{1}{\text{cos}A}$, this is the required form

`\int \text{tan} \; x \, \text{d}x = \text{ln} \; |\text{sec} \; x| + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $\text{tan}  x \equiv \frac{\text{sin}x}{\text{cos}x}$ to rewrite the integrand as a fraction.
> 
> **A1**: Correct integration to `-\text{ln} \; |\text{cos} \; x| + c`, or equivalent. Modulus signs are condoned, present or absent.
> 
> **M1**: Correct use of the power law for logarithms to move the minus sign inside, reaching a logarithm of `\dfrac{1}{|\text{cos} \; x|}` or of `|\text{cos} \; x|^{-1}`.
> 
> **A1**: Correct conversion to `\text{ln} \; |\text{sec} \; x| + c`, using $\text{sec}  x \equiv \frac{1}{\text{cos}x}$. Because the answer is printed, going straight from `-\text{ln} \; |\text{cos} \; x|` to the given result without showing the reciprocal step does not earn this mark.

### Q33
A fraction whose numerator is the derivative of its denominator integrates to a logarithm

`\int \frac{\text{f}'(x)}{\text{f}(x)} \, \text{d}x = \text{ln} \; |\text{f}(x)| + c`

Here $\text{f} ( x ) = 2 x + 3$ has derivative 2, so insert that 2 on the top and compensate with $\frac{1}{2}$ outside

`\int \frac{1}{2x+3} \, \text{d}x = \dfrac{1}{2}\int \frac{2}{2x+3} \, \text{d}x`

**[M1]**

The integrand now matches the standard form exactly

`\int \frac{1}{2x + 3} \, \text{d}x = \dfrac{1}{2}\,\text{ln} \; |2x+3| + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, reaching a multiple of `\text{ln} \; |2x+3|`.
> 
> **A1**: Correct integral `\dfrac{1}{2}\,\text{ln} \; |2x+3| + c`. Modulus signs are condoned, so $\frac{1}{2}  \text{ln}  ( 2 x + 3 ) + c$ also earns this mark. Accept `\text{ln} \; |2x+3|^{\frac{1}{2}}` as an equivalent form. Any letter may be used for the constant.
To recover $y$, integrate the derivative with respect to $x$

`y = \int 3\text{e}^{3x+1} \, \text{d}x`

The chain rule gives `\dfrac{\text{d}}{\text{d}x}\left(\text{e}^{3x+1}\right) = 3\text{e}^{3x+1}`, which is exactly the integrand, so the integral follows directly

$y = 3 \times \frac{1}{3} \text{e}^{3x+1}$

**[M1]**

Simplify and add the constant of integration

$y = \text{e}^{3x+1} + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, integrating to reach a multiple of $\text{e}^{3x+1}$.
> 
> **A1**: Correct expression $y = \text{e}^{3x+1} + c$. Any letter may be used for the constant.

### Q34
Consider differentiating $\text{e}^{2x-4}$, which brings out a 2 from the chain rule on the exponent

`\dfrac{\text{d}}{\text{d}x}\left(\text{e}^{2x-4}\right) = 2\text{e}^{2x-4}`

The coefficient 4 is $2 \times 2$, so insert that derivative inside the integral and compensate with the remaining 2 outside

`\int_{2}^{5} 4\text{e}^{2x-4} \, \text{d}x = 2\int_{2}^{5} 2\text{e}^{2x-4} \, \text{d}x`

**[M1]**

Integrate

`= 2\left[\text{e}^{2x-4}\right]_{2}^{5}`

**[A1]**

Substitute the limits

`= 2\left(\text{e}^{2(5)-4} - \text{e}^{2(2)-4}\right) \\ = 2\left(\text{e}^{6} - \text{e}^{0}\right)`

Since $\text{e}^{0} = 1$, this gives the required result

`\int_{2}^{5} 4\text{e}^{2x - 4} \, \text{d}x = 2\left(\text{e}^{6} - 1\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the reverse chain rule, reaching a multiple of $\text{e}^{2x-4}$.
> 
> **A1**: Correct integrated expression `2\left[\text{e}^{2x-4}\right]` with the limits still attached.
> 
> **A1**: Correct substitution of both limits leading to the given result. Because the answer is printed, the step showing $\text{e}^{0} = 1$ must be visible, either as $\text{e}^{0}$ written out or as an explicit statement that it equals 1.

### Q35
The bracket $2 x$ has derivative 2, so insert that factor and compensate with $\frac{1}{2}$ outside

`\int \text{cos} \; 2x \, \text{d}x = \dfrac{1}{2}\int 2 \, \text{cos} \; 2x \, \text{d}x`

**[M1]**

The integrand is now the derivative of $\text{sin}  2 x$, so integrate and add the constant

`\int \text{cos} \; 2x \, \text{d}x = \dfrac{1}{2}\,\text{sin} \; 2x + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, reaching a multiple of $\text{sin}  2 x$.
> 
> **A1**: Correct integral $\frac{1}{2}  \text{sin}  2 x + c$. Any letter may be used for the constant.
Integrating a cubed bracket produces a fourth power

Consider differentiating $( 3 x - 1 )^{4}$, which brings down a 4 from the power and a 3 from the chain rule on the bracket

`\dfrac{\text{d}}{\text{d}x}\left[(3x-1)^{4}\right] = 4 \times 3 \times (3x-1)^{3}`

$= 12 ( 3 x - 1 )^{3}$

So insert that factor of 12 inside the integral and compensate with $\frac{1}{12}$ outside

`\int_{0}^{2} (3x-1)^{3} \, \text{d}x = \dfrac{1}{12}\int_{0}^{2} 12(3x-1)^{3} \, \text{d}x`

**[M1]**

Integrate

`= \dfrac{1}{12}\left[(3x-1)^{4}\right]_{0}^{2}`

**[A1]**

Substitute the limits

`equals 1 over 12 open parentheses open parentheses 3 open parentheses 2 close parentheses minus 1 close parentheses to the power of 4 minus open parentheses 3 open parentheses 0 close parentheses minus 1 close parentheses to the power of 4 close parentheses
equals 1 over 12 open parentheses 5 to the power of 4 minus open parentheses negative 1 close parentheses to the power of 4 close parentheses
equals 624 over 12`

**[M1]**

Evaluate

`\int_{0}^{2} (3x - 1)^{3} \, \text{d}x = 52`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the reverse chain rule, reaching a multiple of $( 3 x - 1 )^{4}$.
> 
> **A1**: Correct integrated expression `\dfrac{1}{12}\left[(3x-1)^{4}\right]` with the limits still attached. Accept the expanded-then-integrated route as an equivalent method.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct value 52.
To recover $y$, integrate the derivative, and integrating $\text{e}^{5x}$ brings out a factor of $\frac{1}{5}$

`y = \int \text{e}^{5x} \, \text{d}x`

**[M1]**

Add the constant of integration

$y = \frac{1}{5} \text{e}^{5x} + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, reaching a multiple of $\text{e}^{5x}$.
> 
> **A1**: Correct expression $y = \frac{1}{5} \text{e}^{5x} + c$. Accept $\frac{\text{e}^{5x}}{5} + c$. Any letter may be used for the constant.

### Q36
The integrand is a product of a linear factor and an exponential, so use the formula for integration by parts

`\int u \dfrac{\text{d}v}{\text{d}x} \, \text{d}x = uv - \int v \dfrac{\text{d}u}{\text{d}x} \, \text{d}x`

Take $u$ to be the linear factor, which becomes a constant when differentiated

$u = 5 x - 4 ,  \frac{\text{d}v}{\text{d}x} = \text{e}^{3x}$

$\frac{\text{d}u}{\text{d}x} = 5 ,  v = \frac{1}{3} \text{e}^{3x}$

**[M1]**

Work the indefinite integral first, substituting into the formula

`\int (5x-4)\text{e}^{3x} \, \text{d}x = \dfrac{1}{3}(5x-4)\text{e}^{3x} - \int \dfrac{5}{3}\text{e}^{3x} \, \text{d}x`

**[A1]**

The remaining integral is a standard exponential, bringing out another factor of $\frac{1}{3}$

`\int \dfrac{5}{3}\text{e}^{3x} \, \text{d}x = \dfrac{5}{9}\text{e}^{3x}`

**[M1]**

Combine the two terms over a common factor of $\frac{1}{9} \text{e}^{3x}$

`\int (5x-4)\text{e}^{3x} \, \text{d}x = \dfrac{1}{9}\left(3(5x-4)\text{e}^{3x} - 5\text{e}^{3x}\right) = \dfrac{1}{9}\text{e}^{3x}\left(15x - 17\right)`

**[A1]**

Substitute the limits

`\int_{0}^{1} (5x-4)\text{e}^{3x} \, \text{d}x = \dfrac{1}{9}\left[\text{e}^{3x}(15x-17)\right]_{0}^{1} \\ = \dfrac{1}{9}\left(\text{e}^{3}\left(15(1)-17\right) - \text{e}^{0}\left(15(0)-17\right)\right) \\ = \dfrac{1}{9}\left(-2\text{e}^{3} + 17\right)`

**[M1]**

Simplify

`\int_{0}^{1} (5x - 4)\text{e}^{3x} \, \text{d}x = \dfrac{17 - 2\text{e}^{3}}{9}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct choice of $u$ and $\frac{\text{d}v}{\text{d}x}$, with $u$ taken as the linear factor, together with correct $\frac{\text{d}u}{\text{d}x}$ and $v$. A sign error in the parts formula is condoned for this mark.
> 
> **A1**: Correct application of the formula, reaching `\dfrac{1}{3}(5x-4)\text{e}^{3x} - \displaystyle\int \dfrac{5}{3}\text{e}^{3x} \, \text{d}x`.
> 
> **M1**: Correct integration of the remaining integral, reaching a multiple of $\text{e}^{3x}$.
> 
> **A1**: Correct integrated expression. Accept the unfactorised form $\frac{1}{3} ( 5 x - 4 ) \text{e}^{3x} - \frac{5}{9} \text{e}^{3x}$; you are not required to factorise.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct exact value $\frac{17-2\text{e}^{3}}{9}$. Accept any exact equivalent, such as $\frac{17}{9} - \frac{2\text{e}^{3}}{9}$. Because the question asks for the exact value in terms of $\text{e}$, a decimal such as $- 2 . 57$ does not earn this mark.

### Q37
The bracket $2 x + 1$ has derivative 2, so integrating brings out a factor of $\frac{1}{2}$, and $\text{sin}$ integrates to $- \text{cos}$

`\text{f}(x) = \dfrac{1}{2} \times \left(-\text{cos} \; (2x+1)\right)`

**[M1]**

Tidy the expression and add the constant of integration

$\text{f} ( x ) = - \frac{1}{2}  \text{cos}  ( 2 x + 1 ) + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, reaching a multiple of $\text{cos}  ( 2 x + 1 )$.
> 
> **A1**: Correct expression $- \frac{1}{2}  \text{cos}  ( 2 x + 1 ) + c$. Both the sign and the $\frac{1}{2}$ are needed. Any letter may be used for the constant.
To recover $y$, integrate the derivative. The bracket $3 x + 5$ has derivative 3, which the coefficient 3 cancels exactly

`y = \int 3 \, \text{cos} \; (3x+5) \, \text{d}x = 3 \times \dfrac{1}{3}\,\text{sin} \; (3x+5)`

**[M1]**

Simplify and add the constant of integration

$y = \text{sin}  ( 3 x + 5 ) + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, reaching a multiple of $\text{sin}  ( 3 x + 5 )$.
> 
> **A1**: Correct expression $y = \text{sin}  ( 3 x + 5 ) + c$. Any letter may be used for the constant.
The bracket $x - π$ has derivative 1, so no adjusting is needed here. Since $\text{tan}$ differentiates to $\text{sec}^{2}$, the integral follows directly

`\int_{\frac{7\pi}{6}}^{\frac{4\pi}{3}} \text{sec}^{2} \; (x - \pi) \, \text{d}x = \left[\text{tan} \; (x - \pi)\right]_{\frac{7\pi}{6}}^{\frac{4\pi}{3}}`

**[M1]**

Substitute the limits

`= \text{tan} \; \left(\frac{4\pi}{3} - \pi\right) - \text{tan} \; \left(\frac{7\pi}{6} - \pi\right) \\ = \text{tan} \; \frac{\pi}{3} - \text{tan} \; \frac{\pi}{6} \\ = \sqrt{3} - \dfrac{\sqrt{3}}{3}`

**[M1]**

Evaluate

`\int_{\frac{7\pi}{6}}^{\frac{4\pi}{3}} \text{sec}^{2} \; (x - \pi) \, \text{d}x = \dfrac{2\sqrt{3}}{3}`

**[A1]**

> **[exam-tip]**
> Because the bracket is $x - π$ rather than $a x + b$ with $a \neq 1$, there is no fraction to bring out, and inserting one out of habit is a common error here. Check the derivative of the bracket before you adjust anything: if it is 1, the integral is as simple as the standard result.

> **[mark-scheme]**
> **M1**: Correct integration to $\text{tan}  ( x - π )$, with the limits attached.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct exact value $\frac{2\sqrt{3}}{3}$. Accept any exact equivalent, such as $\frac{2}{\sqrt{3}}$. Because the question asks for the exact value, a decimal such as $1 . 15$ does not earn this mark.

### Q38
Differentiate the given substitution. Here the derivative is 1, so $\text{d} u$ and $\text{d} x$ are interchangeable

$u = x + 4  \Rightarrow  \frac{\text{d}u}{\text{d}x} = 1  \Rightarrow  \text{d} u = \text{d} x$

**[M1]**

Change the limits to values of $u$, so the whole integral can be worked in $u$ without converting back

$x = 1  \Rightarrow  u = 5 ,  x = 2  \Rightarrow  u = 6$

**[M1]**

The numerator is still in terms of $x$, so rearrange the substitution to replace it

$x = u - 4$

`\int_{1}^{2} \frac{x}{x+4} \, \text{d}x = \int_{5}^{6} \frac{u - 4}{u} \, \text{d}u`

**[A1]**

Split the fraction into two terms, each of which integrates on sight

`= \int_{5}^{6} \left(1 - \frac{4}{u}\right) \text{d}u`

**[M1]**

Integrate, using the fact that $\frac{1}{u}$ integrates to a logarithm. Both limits are positive, so the modulus signs are not needed

`= \left[u - 4 \, \text{ln} \; u\right]_{5}^{6}`

**[A1]**

Substitute the limits, upper minus lower

`= \left(6 - 4 \, \text{ln} \; 6\right) - \left(5 - 4 \, \text{ln} \; 5\right) \\ = 1 + 4 \, \text{ln} \; 5 - 4 \, \text{ln} \; 6`

**[M1]**

Factor out the 4 and apply the subtraction law for logarithms to reach the required form

`\int_{1}^{2} \frac{x}{x + 4} \, \text{d}x = 1 + 4 \, \text{ln} \; \frac{5}{6}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct differentiation of the substitution to give $\text{d} u = \text{d} x$, or equivalent.
> 
> **M1**: Correct change of limits to $u = 5$ and $u = 6$. Keeping the original limits and converting back to $x$ after integrating is equally acceptable.
> 
> **A1**: Correct integral in $u$, `\displaystyle\int_{5}^{6} \frac{u-4}{u} \, \text{d}u`, with the numerator correctly rewritten.
> 
> **M1**: Correct split of the fraction into $1 - \frac{4}{u}$, or equivalent.
> 
> **A1**: Correct integration to $u - 4  \text{ln}  u$. Modulus signs are condoned, present or absent.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct use of the logarithm laws to reach the given result. Because the answer is printed, the step combining $4  \text{ln}  5 - 4  \text{ln}  6$ into $4  \text{ln}  \frac{5}{6}$ must be visible.

### Q39
The expression has the shape $\text{sin}  A  \text{cos}  A$ with the half angle in place of $A$, so set $A = \frac{θ}{2}$, which makes $2 A = θ$

$4  \text{sin}  \frac{θ}{2}  \text{cos}  \frac{θ}{2} = 4  \text{sin}  A  \text{cos}  A$

Factor out a 2 so that the identity can be applied to what remains

`= 2\left(2 \, \text{sin} \; A \, \text{cos} \; A\right) \equiv 2 \, \text{sin} \; 2A`

**[M1]**

Replace $2 A$ by $θ$ to reach the required form

$4  \text{sin}  \frac{θ}{2}  \text{cos}  \frac{θ}{2} \equiv 2  \text{sin}  θ$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the given identity with $A = \frac{θ}{2}$, including factorising out the 2 so that $2  \text{sin}  A  \text{cos}  A$ appears.
> 
> **A1**: Correct substitution of $2 A = θ$ to reach the given result. Because the result is given, the intermediate step in terms of $A$ must be visible.
The integrand is exactly the left-hand side of part (a), so replace it with the simpler equivalent

`\int 4 \, \text{sin} \; \frac{\theta}{2} \, \text{cos} \; \frac{\theta}{2} \, \text{d}\theta = \int 2 \, \text{sin} \; \theta \, \text{d}\theta`

**[M1]**

Since $\text{cos}  θ$ differentiates to $- \text{sin}  θ$, insert that minus sign inside and compensate outside

`= -2\int -\text{sin} \; \theta \, \text{d}\theta`

**[M1]**

Integrate and add the constant

`\int 4 \, \text{sin} \; \frac{\theta}{2} \, \text{cos} \; \frac{\theta}{2} \, \text{d}\theta = -2 \, \text{cos} \; \theta + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the result from part (a) to replace the integrand with $2  \text{sin}  θ$.
> 
> **M1**: Correct integration method, reaching a multiple of $\text{cos}  θ$.
> 
> **A1**: Correct integral $- 2  \text{cos}  θ + c$. The minus sign is needed. Any letter may be used for the constant.

### Q40
To recover $\text{f} ( x )$, integrate the derivative. First take the $\frac{1}{2}$ outside, so that the remaining fraction can be compared with the standard logarithmic form

`\text{f}(x) = \dfrac{1}{2}\int \frac{12x^{2}+7}{4x^{3}+7x+4} \, \text{d}x`

Differentiating the denominator gives exactly the numerator, so the integrand has the form $\frac{\text{f}'(x)}{\text{f}(x)}$

`\dfrac{\text{d}}{\text{d}x}\left(4x^{3}+7x+4\right) = 12x^{2}+7`

**[M1]**

So the integral is the natural logarithm of the denominator

`\text{f}(x) = \dfrac{1}{2}\,\text{ln} \; |4x^{3}+7x+4| + c`

**[A1]**

The curve passes through $( 0 , 4 )$, so substitute $x = 0$ and $\text{f} ( 0 ) = 4$ to find the constant

`\dfrac{1}{2}\,\text{ln} \; |4(0)^{3} + 7(0) + 4| + c = 4`

$\frac{1}{2}  \text{ln}  4 + c = 4  \Rightarrow  c = 4 - \frac{1}{2}  \text{ln}  4$

**[M1]**

Substitute the constant back to give the full expression

`\text{f}(x) = \dfrac{1}{2}\,\text{ln} \; |4x^{3} + 7x + 4| + 4 - \dfrac{1}{2}\,\text{ln} \; 4`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct identification that the integrand has the form $\frac{\text{f}'(x)}{\text{f}(x)}$, after taking the $\frac{1}{2}$ outside. This may be implied by going straight to a logarithm of the cubic.
> 
> **A1**: Correct integral `\dfrac{1}{2}\,\text{ln} \; |4x^{3}+7x+4| + c`. Modulus signs are condoned, present or absent.
> 
> **M1**: Correct substitution of the point $( 0 , 4 )$ to form an equation in the constant.
> 
> **A1**: Correct final expression. Accept any equivalent exact form, including the combined version `\text{ln} \; \sqrt{\left|x^{3} + \dfrac{7}{4}x + 1\right|} + 4`. You are not required to simplify, and a decimal value for the constant does not earn this mark.
The answer to part (a) contains a logarithm of the cubic, so check what the cubic does at this value of $x$

`4\left(-\dfrac{1}{2}\right)^{3} + 7\left(-\dfrac{1}{2}\right) + 4 = -\dfrac{1}{2} - \dfrac{7}{2} + 4 = 0`

Since the logarithm of zero is undefined, the function has no value there

**Final answer:** **The cubic inside the logarithm equals 0 when x = -1/2, and ln 0 is undefined, so f(x) does not exist at this value**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct explanation that $4 x^{3} + 7 x + 4 = 0$ when $x = - \frac{1}{2}$, together with the statement that the logarithm of zero is undefined. Both halves are needed: showing the cubic is zero without saying why that matters, or asserting that the logarithm is undefined without showing the cubic vanishes, does not earn this mark. Accept a factorised argument, noting that `4x^{3}+7x+4 = (2x+1)\left(2x^{2}-x+4\right)` so $2 x + 1$ is a factor.

### Q41
A squared cosine cannot be integrated directly, so rearrange the given identity to make $\text{cos}^{2} θ$ the subject

$\text{cos}  2 θ \equiv 2  \text{cos}^{2} θ - 1  \Rightarrow  \text{cos}^{2} θ \equiv \frac{1}{2} \text{cos}  2 θ + \frac{1}{2}$

**[M1]**

Replace the integrand, which leaves two terms that each integrate straightforwardly

`\int_{\frac{1}{4}\pi}^{\frac{1}{2}\pi} \text{cos}^{2} \theta \, \text{d}\theta = \int_{\frac{1}{4}\pi}^{\frac{1}{2}\pi} \left(\dfrac{1}{2}\text{cos} \; 2\theta + \dfrac{1}{2}\right) \text{d}\theta`

**[A1]**

For the cosine term, the bracket $2 θ$ has derivative 2, so insert that factor and compensate with $\frac{1}{4}$ outside

`\int \dfrac{1}{2}\text{cos} \; 2\theta \, \text{d}\theta = \dfrac{1}{4}\int 2 \, \text{cos} \; 2\theta \, \text{d}\theta`

Integrating $\text{cos}  2 θ$ gives $\frac{1}{2} \text{sin}  2 θ$, which leaves the 2 in front of it

`= \dfrac{1}{4}\left(2 \times \dfrac{1}{2}\text{sin} \; 2\theta\right) \\ = \dfrac{1}{4}\text{sin} \; 2\theta`

**[M1]**

The constant term integrates to $\frac{1}{2} θ$

`\int \dfrac{1}{2} \, \text{d}\theta = \dfrac{1}{2}\theta`

Put the two integrated terms together and attach the limits

`\int_{\frac{1}{4}\pi}^{\frac{1}{2}\pi} \text{cos}^{2} \theta \, \text{d}\theta = \left[\dfrac{1}{4}\text{sin} \; 2\theta + \dfrac{1}{2}\theta\right]_{\frac{1}{4}\pi}^{\frac{1}{2}\pi}`

**[A1]**

Substitute the limits

`= \left(\dfrac{1}{4}\text{sin} \; \pi + \dfrac{1}{2}\left(\dfrac{1}{2}\pi\right)\right) - \left(\dfrac{1}{4}\text{sin} \; \dfrac{\pi}{2} + \dfrac{1}{2}\left(\dfrac{1}{4}\pi\right)\right) \\ = \left(\dfrac{1}{4}(0) + \dfrac{\pi}{4}\right) - \left(\dfrac{1}{4}(1) + \dfrac{\pi}{8}\right)`

**[M1]**

Collect the $π$ terms and the numerical terms separately

`\int_{\frac{1}{4}\pi}^{\frac{1}{2}\pi} \text{cos}^{2} \theta \, \text{d}\theta = \dfrac{\pi}{8} - \dfrac{1}{4}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct rearrangement of the given identity to make $\text{cos}^{2} θ$ the subject.
> 
> **A1**: Correct rewritten integrand $\frac{1}{2} \text{cos}  2 θ + \frac{1}{2}$, or equivalent.
> 
> **M1**: Correct integration of the cosine term, reaching a multiple of $\text{sin}  2 θ$.
> 
> **A1**: Correct integrated expression $\frac{1}{4} \text{sin}  2 θ + \frac{1}{2} θ$, with the limits still attached. Accept the unsimplified form.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct exact value $\frac{π}{8} - \frac{1}{4}$. Accept any exact equivalent, such as $\frac{π-2}{8}$. Because the question asks for the exact value, a decimal such as $0 . 143$ does not earn this mark.

### Q42
(i)

Differentiate term by term

$\text{f} ' ( x ) = 6 x^{2} + 4$

**[B1]**

(ii)

Compare the numerator of the integrand with part (i). It is not $\text{f} ' ( x )$ itself, but $\text{f} ' ( x )$ has a common factor of 2

`\text{f}'(x) = 6x^{2} + 4 = 2\left(3x^{2} + 2\right)`

**[M1]**

So the numerator is exactly half of $\text{f} ' ( x )$. Insert the missing factor of 2 on the top and compensate with $\frac{1}{2}$ outside

`\int \frac{3x^{2}+2}{2x^{3}+4x} \, \text{d}x = \dfrac{1}{2}\int \frac{2\left(3x^{2}+2\right)}{2x^{3}+4x} \, \text{d}x = \dfrac{1}{2}\int \frac{6x^{2}+4}{2x^{3}+4x} \, \text{d}x`

**[M1]**

The integrand now has the form $\frac{\text{f}'(x)}{\text{f}(x)}$, which integrates to the natural logarithm of the denominator

`\int \frac{3x^{2} + 2}{2x^{3} + 4x} \, \text{d}x = \dfrac{1}{2}\,\text{ln} \; |2x^{3} + 4x| + c`

**[A1]**

> **[mark-scheme]**
> **B1**: Correct derivative $\text{f} ' ( x ) = 6 x^{2} + 4$.
> 
> **M1**: Correct identification that the numerator of the integrand is a constant multiple of $\text{f} ' ( x )$, using the answer to part (i).
> 
> **M1**: Correct adjustment, reaching an integrand of the form $\frac{\text{f}'(x)}{\text{f}(x)}$ with $\frac{1}{2}$ outside.
> 
> **A1**: Correct integral `\dfrac{1}{2}\,\text{ln} \; |2x^{3}+4x| + c`. Modulus signs are condoned, present or absent. Accept `\text{ln} \; |2x^{3}+4x|^{\frac{1}{2}}` as an equivalent form. Any letter may be used for the constant.

### Q43
Differentiate the given substitution so that $\text{d} x$ can be replaced

$u = 5 x - 2  \Rightarrow  \frac{\text{d}u}{\text{d}x} = 5  \Rightarrow  \text{d} u = 5  \text{d} x$

**[M1]**

The substitution needs $5  \text{d} x$ to appear, so split the coefficient as $- 15 = - 3 \times 5$ and group the 5 with $\text{d} x$

`\int -15 \, \text{sin} \; (5x-2) \, \text{d}x = \int -3 \, \text{sin} \; (5x-2) \times 5 \, \text{d}x`

**[M1]**

Replace $5 x - 2$ by $u$ and $5  \text{d} x$ by $\text{d} u$

`= \int -3 \, \text{sin} \; u \, \text{d}u`

**[A1]**

Integrate, remembering that $\text{sin}  u$ integrates to $- \text{cos}  u$, so the two minus signs cancel

`= -3\left(-\text{cos} \; u\right) + c = 3 \, \text{cos} \; u + c`

**[M1]**

Reverse the substitution to give the answer in terms of $x$

`\int -15 \, \text{sin} \; (5x - 2) \, \text{d}x = 3 \, \text{cos} \; (5x - 2) + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct differentiation of the substitution to give $\text{d} u = 5  \text{d} x$, or equivalent.
> 
> **M1**: Correct rearrangement of the integrand so that $5  \text{d} x$ appears as a factor, or equivalent handling of the constant.
> 
> **A1**: Correct integral in $u$, `\displaystyle\int -3 \, \text{sin} \; u \, \text{d}u`.
> 
> **M1**: Correct integration, reaching a multiple of $\text{cos}  u$ with the sign handled.
> 
> **A1**: Correct final answer $3  \text{cos}  ( 5 x - 2 ) + c$, in terms of $x$. Any letter may be used for the constant. Reaching this answer directly by the reverse chain rule, without a substitution, is a valid method and scores full marks.

### Q44
The denominator is a product of two distinct linear factors, so each contributes a term with a constant numerator

$\frac{11}{(2x-3)(x+4)} \equiv \frac{A}{2x-3} + \frac{B}{x+4}$

**[B1]**

Combine the right-hand side over the common denominator and compare numerators

$11 \equiv A ( x + 4 ) + B ( 2 x - 3 )$

Choosing $x = \frac{3}{2}$ makes the second bracket vanish, isolating $A$

`11 = A\left(\dfrac{3}{2} + 4\right) \quad \Rightarrow \quad \dfrac{11}{2}A = 11 \quad \Rightarrow \quad A = 2`

**[M1]**

Choosing $x = - 4$ makes the first bracket vanish, isolating $B$

$11 = B ( - 8 - 3 )  \Rightarrow  - 11 B = 11  \Rightarrow  B = - 1$

Write the decomposition with both constants substituted

$\text{f} ( x ) = \frac{2}{2x-3} - \frac{1}{x+4}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct form chosen for the decomposition, with a constant numerator over each of the two distinct linear factors.
> 
> **M1**: Correct method for finding the constants, either by substituting values of $x$ that make a bracket vanish or by comparing coefficients. Either method is fully acceptable.
> 
> **A1**: Both constants correct, giving $\frac{2}{2x-3} - \frac{1}{x+4}$. Accept $\frac{2}{2x-3} + \frac{-1}{x+4}$.
Replace the integrand by the partial fractions from part (a)

`\int \frac{11}{(2x-3)(x+4)} \, \text{d}x = \int \left(\frac{2}{2x-3} - \frac{1}{x+4}\right) \text{d}x`

**[M1]**

In the first term the denominator has derivative 2, which is exactly the numerator, and in the second the denominator has derivative 1. So both integrate straight to logarithms with no adjusting needed

`= \text{ln} \; |2x-3| - \text{ln} \; |x+4| + c`

**[A1]**

Apply the subtraction law for logarithms to combine the two terms into one

`\int \text{f}(x) \, \text{d}x = \text{ln} \; \left|\frac{2x - 3}{x + 4}\right| + c`

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Correct use of the partial fractions from part (a), integrating to obtain terms of the form `p \, \text{ln} \; |2x-3| + q \, \text{ln} \; |x+4|`. This mark follows through from your answer to part (a).
> 
> **A1**: Both logarithms correct, `\text{ln} \; |2x-3|` and `-\text{ln} \; |x+4|`. Modulus signs are condoned, present or absent.
> 
> **M1**: Correct use of a logarithm law to combine the two terms into one.
> 
> **A1**: Correct single logarithm. Accept either `\text{ln} \; \left|\dfrac{2x-3}{x+4}\right| + c` with the constant kept separate, or `\text{ln} \; \left|\dfrac{c(2x-3)}{x+4}\right|` with the constant absorbed. Both are single logarithms and both score. An answer left as a difference of two logarithms does not earn this mark.

### Q45
A sum of two squares in the denominator looks like the standard result that integrates to an inverse tangent

`\int \frac{1}{x^{2}+a^{2}} \, \text{d}x = \frac{1}{a}\,\text{tan}^{-1}\left(\frac{x}{a}\right) + c`

That result needs a coefficient of 1 in front of $x^{2}$, so factor the 9 out of the denominator

`\frac{1}{4+9x^{2}} = \frac{1}{9\left(\frac{4}{9} + x^{2}\right)} = \frac{1}{9}\left(\frac{1}{x^{2} + \left(\frac{2}{3}\right)^{2}}\right)`

**[M1]**

The integrand now matches, with $a = \frac{2}{3}$ read off as the square root of the constant

`\int_{2}^{4} \frac{1}{4+9x^{2}} \, \text{d}x = \frac{1}{9}\left[\frac{3}{2}\,\text{tan}^{-1}\left(\frac{3}{2}x\right)\right]_{2}^{4}`

**[A1]**

Take the constants outside the bracket

`= \frac{1}{9} \times \frac{3}{2}\left[\text{tan}^{-1}\left(\frac{3}{2}x\right)\right]_{2}^{4} \\ = \frac{1}{6}\left[\text{tan}^{-1}\left(\frac{3}{2}x\right)\right]_{2}^{4}`

Substitute the limits

`= \frac{1}{6}\left(\text{tan}^{-1}\left(\frac{3}{2}(4)\right) - \text{tan}^{-1}\left(\frac{3}{2}(2)\right)\right) \\ = \frac{1}{6}\left(\text{tan}^{-1} 6 - \text{tan}^{-1} 3\right)`

**[M1]**

Evaluate in radians, keeping full accuracy until the final rounding

`= \frac{1}{6}\left(1.40565\ldots - 1.24905\ldots\right) \\ = 0.0261003\ldots`

**Final answer:** `\int_{2}^{4} \frac{1}{4 + 9x^{2}} \, \text{d}x = 0.0261`** (3 s.f.)**

**[A1]**

> **[exam-tip]**
> Make sure your calculator is in radian mode before evaluating the inverse tangents.

> **[mark-scheme]**
> **M1**: Correct method to rewrite the denominator in the form `k\left(x^{2} + a^{2}\right)`, factorising the 9 out.
> 
> **A1**: Correct integrated expression, a multiple of `\text{tan}^{-1}\left(\dfrac{3x}{2}\right)` with the limits attached. Accept the unsimplified form.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct value $0 . 0261$. Accept answers which round to $0 . 0261$. The inverse tangents must be evaluated in radians; a degree-mode answer such as $1 . 48$ does not earn this mark.

### Q46
Integrating reverses differentiating, and $\text{cos}  x$ differentiates to $- \text{sin}  x$, so the integral of $\text{sin}  x$ carries a minus sign

`\int \text{sin} \; x \, \text{d}x = -\text{cos} \; x + c`

**[B1]**

> **[mark-scheme]**
> **B1**: Correct integral $- \text{cos}  x + c$. The minus sign is needed. The constant is condoned if omitted. Any letter may be used for the constant.
Although $\frac{1}{x}$ can be written as $x^{-1}$, the rule for integrating powers of $x$ cannot be used here because it would require dividing by zero. Instead use the standard result that $\frac{1}{x}$ integrates to a logarithm

`\int_{1}^{4} \frac{1}{x} \, \text{d}x = \left[\text{ln} \; x\right]_{1}^{4}`

**[M1]**

Both limits are positive, so the modulus signs are not needed. Substitute them, upper minus lower

$= \text{ln}  4 - \text{ln}  1$

**[M1]**

Since $\text{ln}  1 = 0$, the second term vanishes

`\int_{1}^{4} \frac{1}{x} \, \text{d}x = \text{ln} \; 4`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct integration of $\frac{1}{x}$ to $\text{ln}  x$, with the limits attached. Modulus signs are condoned, present or absent.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct exact value $\text{ln}  4$. Accept any exact equivalent, such as $2  \text{ln}  2$. Because the question asks for the exact value, a decimal such as $1 . 39$ does not earn this mark.
Integrating $\text{e}^{7x}$ brings out a factor of $\frac{1}{7}$, which the coefficient 7 cancels exactly

$y = 7 \times \frac{1}{7} \text{e}^{7x}$

**[M1]**

Simplify and add the constant of integration

$y = \text{e}^{7x} + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method, reaching a multiple of $\text{e}^{7x}$.
> 
> **A1**: Correct expression $y = \text{e}^{7x} + c$. Any letter may be used for the constant.

### Q47
Differentiate the given substitution, which conveniently produces the $\text{cos}  x  \text{d} x$ already sitting in the integral

$u = \text{sin}  x  \Rightarrow  \frac{\text{d}u}{\text{d}x} = \text{cos}  x  \Rightarrow  \text{d} u = \text{cos}  x  \text{d} x$

Change the limits to values of $u$ so that the whole integral can be worked in $u$

$x = 0  \Rightarrow  u = \text{sin}  0 = 0$

$x = \frac{1}{2} π  \Rightarrow  u = \text{sin}  \frac{1}{2} π = 1$

**[M1]**

The remaining $\text{cos}^{2} 2 x$ must also be written in terms of $u$, and the double-angle identity is what links $\text{cos}  2 x$ to $\text{sin}  x$

$\text{cos}  2 x \equiv 1 - 2  \text{sin}^{2} x = 1 - 2 u^{2}$

**[M1]**

Square that to get $\text{cos}^{2} 2 x$, and expand

`\text{cos}^{2} 2x = \left(1 - 2u^{2}\right)^{2} = 1 - 4u^{2} + 4u^{4}`

**[A1]**

The integral is now a polynomial in $u$

`\int_{0}^{\frac{1}{2}\pi} \text{cos}^{2} 2x \, \text{cos} \; x \, \text{d}x = \int_{0}^{1} \left(1 - 4u^{2} + 4u^{4}\right) \text{d}u`

Integrate term by term

`= \left[u - \dfrac{4}{3}u^{3} + \dfrac{4}{5}u^{5}\right]_{0}^{1}`

**[A1]**

Substitute the limits

`= \left(1 - \dfrac{4}{3}(1)^{3} + \dfrac{4}{5}(1)^{5}\right) - \left(0 - \dfrac{4}{3}(0)^{3} + \dfrac{4}{5}(0)^{5}\right) \\ = \left(1 - \dfrac{4}{3} + \dfrac{4}{5}\right) - 0`

**[M1]**

Write the three terms over a common denominator of 15

`\int_{0}^{\frac{1}{2}\pi} \text{cos}^{2} 2x \, \text{cos} \; x \, \text{d}x = \dfrac{7}{15}`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct differentiation of the substitution to give $\text{d} u = \text{cos}  x  \text{d} x$, together with the limits changed to 0 and 1. Keeping the original limits and converting back to $x$ at the end is equally acceptable.
> 
> **M1**: Correct use of a double-angle identity to express $\text{cos}  2 x$ in terms of $u$.
> 
> **A1**: Correct expansion $\text{cos}^{2} 2 x = 1 - 4 u^{2} + 4 u^{4}$.
> 
> **A1**: Correct integration to $u - \frac{4}{3} u^{3} + \frac{4}{5} u^{5}$. Accept the unsimplified form.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct exact value $\frac{7}{15}$. Because the question asks for the exact value, a decimal such as 0.467 does not earn this mark.

### Q48
(i)

The bracket $2 x + 1$ has derivative 2, so insert that factor inside the integral and compensate with $- \frac{1}{2}$ outside, which sets up the reverse chain rule

`\int \text{sin} \; (2x+1) \, \text{d}x = -\dfrac{1}{2} \int -2 \, \text{sin} \; (2x+1) \, \text{d}x`

**[M1]**

The bracket now integrates directly, since $- 2  \text{sin}  ( 2 x + 1 )$ is the derivative of $\text{cos}  ( 2 x + 1 )$

`\int \text{sin} \; (2x+1) \, \text{d}x = -\dfrac{1}{2} \, \text{cos} \; (2x+1) + c`

**[A1]**

(ii)

The bracket $2 θ - \frac{π}{6}$ has derivative 2, so adjust and compensate in the same way

`\int_{\frac{\pi}{6}}^{\frac{\pi}{4}} \text{sec}^{2} \left(2\theta - \frac{\pi}{6}\right) \text{d}\theta = \dfrac{1}{2} \int_{\frac{\pi}{6}}^{\frac{\pi}{4}} 2 \, \text{sec}^{2} \left(2\theta - \frac{\pi}{6}\right) \text{d}\theta`

**[M1]**

Integrate, using the fact that $\text{sec}^{2}$ integrates to $\text{tan}$

`= \dfrac{1}{2} \left[\text{tan} \left(2\theta - \frac{\pi}{6}\right)\right]_{\frac{\pi}{6}}^{\frac{\pi}{4}}`

**[A1]**

Substitute the limits

`= \dfrac{1}{2}\left[\text{tan} \left(2\left(\frac{\pi}{4}\right) - \frac{\pi}{6}\right) - \text{tan} \left(2\left(\frac{\pi}{6}\right) - \frac{\pi}{6}\right)\right] \\ = \dfrac{1}{2}\left[\text{tan} \; \frac{\pi}{3} - \text{tan} \; \frac{\pi}{6}\right] \\ = \dfrac{1}{2}\left(\sqrt{3} - \dfrac{1}{\sqrt{3}}\right)`

**[M1]**

Write both terms over $\sqrt{3}$ so they can be combined

`= \dfrac{1}{2} \left(\dfrac{3}{\sqrt{3}} - \dfrac{1}{\sqrt{3}}\right) \\ = \dfrac{1}{2} \times \dfrac{2}{\sqrt{3}}`

Rationalise the denominator to give the exact value

`\int_{\frac{\pi}{6}}^{\frac{\pi}{4}} \text{sec}^{2} \left(2\theta - \frac{\pi}{6}\right) \text{d}\theta = \dfrac{\sqrt{3}}{3}`

**[A1]**

(iii)

The bracket $5 x + 2$ has derivative 5, so adjust and compensate before integrating

`\dfrac{\text{d}y}{\text{d}x} = 4 \times \dfrac{1}{5} \left[5 \, \text{cos} \; (5x+2)\right]`

**[M1]**

Integrate, using the fact that $5  \text{cos}  ( 5 x + 2 )$ is the derivative of $\text{sin}  ( 5 x + 2 )$, and add the constant of integration

$y = \frac{4}{5}  \text{sin}  ( 5 x + 2 ) + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the reverse chain rule in part (i), reaching a multiple of $\text{cos}  ( 2 x + 1 )$.
> 
> **A1**: Correct integral $- \frac{1}{2}  \text{cos}  ( 2 x + 1 ) + c$. The sign and the $\frac{1}{2}$ must both be right.
> 
> **M1**: Correct use of the reverse chain rule in part (ii), reaching a multiple of `\text{tan} \left(2\theta - \dfrac{\pi}{6}\right)`.
> 
> **A1**: Correct integrated expression `\dfrac{1}{2} \left[\text{tan} \left(2\theta - \dfrac{\pi}{6}\right)\right]` with the limits still attached.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct exact value. Accept any equivalent exact form, such as $\frac{1}{\sqrt{3}}$ or $\frac{\sqrt{3}}{3}$. Because the question asks for the exact value, a decimal such as 0.577 does not earn this mark.
> 
> **M1**: Correct use of the reverse chain rule in part (iii), reaching a multiple of $\text{sin}  ( 5 x + 2 )$.
> 
> **A1**: Correct expression $y = \frac{4}{5}  \text{sin}  ( 5 x + 2 ) + c$. Any letter may be used for the constant.

### Q49
The exponent $3 x + 2$ has derivative 3, so insert that factor inside the integral and compensate with $\frac{1}{3}$ outside

`\int_{1}^{2} \text{e}^{3x+2} \, \text{d}x = \dfrac{1}{3}\int_{1}^{2} 3\text{e}^{3x+2} \, \text{d}x`

**[M1]**

Integrate, since $3 \text{e}^{3x+2}$ is the derivative of $\text{e}^{3x+2}$

`= \dfrac{1}{3}\left[\text{e}^{3x+2}\right]_{1}^{2}`

**[A1]**

Substitute the limits

`= \dfrac{1}{3}\left(\text{e}^{3(2)+2} - \text{e}^{3(1)+2}\right) \\ = \dfrac{1}{3}\left(\text{e}^{8} - \text{e}^{5}\right)`

**[M1 A1]**

Both terms share a factor of $\text{e}^{5}$, so the answer can also be written more compactly

`\int_{1}^{2} \text{e}^{3x + 2} \, \text{d}x = \dfrac{1}{3}\text{e}^{5}\left(\text{e}^{3} - 1\right)`

> **[mark-scheme]**
> **M1**: Correct use of the reverse chain rule, reaching a multiple of $\text{e}^{3x+2}$.
> 
> **A1**: Correct integrated expression `\dfrac{1}{3}\left[\text{e}^{3x+2}\right]` with the limits still attached.
> 
> **M1**: Correct substitution of both limits, upper minus lower, giving exponents of 8 and 5.
> 
> **A1**: Correct exact value. Accept either `\dfrac{1}{3}\left(\text{e}^{8} - \text{e}^{5}\right)` or the factorised form `\dfrac{1}{3}\text{e}^{5}\left(\text{e}^{3} - 1\right)`, or any exact equivalent such as $\frac{\text{e}^{8}-\text{e}^{5}}{3}$. You are not required to factorise. Because the question asks for the exact value, a decimal such as 944 does not earn this mark.

### Q50
The identity has $\text{sin}^{2} A$ on the right, so rearrange to collect that term on its own side

$\text{cos}  2 A \equiv 1 - 2  \text{sin}^{2} A$

$2  \text{sin}^{2} A \equiv 1 - \text{cos}  2 A$

**[M1]**

Divide both sides by 2 to reach the required form

`\text{sin}^{2} A \equiv \frac{1}{2}\left(1 - \text{cos} \; 2A\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct rearrangement of the given identity to isolate the $\text{sin}^{2} A$ term, reaching $2  \text{sin}^{2} A \equiv 1 - \text{cos}  2 A$.
> 
> **A1**: Correct division by 2 to reach the given result. Because the result is given, both rearrangement steps must be visible. Accept $\frac{1-\text{cos}2A}{2}$ as an equivalent form.
A power of sine cannot be integrated directly, so use the result from part (a) with $A = x$ to replace $\text{sin}^{2} x$, then split the bracket into two terms that each integrate on sight

`\int_{\frac{1}{2}\pi}^{\pi} \text{sin}^{2} x \, \text{d}x = \int_{\frac{1}{2}\pi}^{\pi} \frac{1}{2}\left(1 - \text{cos} \; 2x\right) \text{d}x = \int_{\frac{1}{2}\pi}^{\pi} \left(\frac{1}{2} - \frac{1}{2}\text{cos} \; 2x\right) \text{d}x`

Integrate each term, remembering that $\text{cos}  2 x$ integrates to $\frac{1}{2} \text{sin}  2 x$

`= \left[\frac{1}{2}x - \frac{1}{4}\text{sin} \; 2x\right]_{\frac{1}{2}\pi}^{\pi}`

**[M1]**

Substitute the limits

`= \left(\frac{1}{2}\pi - \frac{1}{4}\text{sin} \; 2\pi\right) - \left(\frac{1}{2}\left(\frac{1}{2}\pi\right) - \frac{1}{4}\text{sin} \; \pi\right) \\ = \left(\frac{\pi}{2} - 0\right) - \left(\frac{\pi}{4} - 0\right)`

**[M1]**

Subtract to give the exact value

`\int_{\frac{1}{2}\pi}^{\pi} \text{sin}^{2} x \, \text{d}x = \frac{\pi}{4}`

**[A1]**

> **[exam-tip]**
> No power of sine or cosine can be integrated as it stands, so whenever you meet $\text{sin}^{2}$ or $\text{cos}^{2}$ in an integral your first move should be the double-angle identity, even when the question does not prompt you. In a real exam this question would appear without part (a) at all, so practise spotting the rearrangement yourself rather than waiting to be handed it.

> **[mark-scheme]**
> **M1**: Correct use of the double-angle result from part (a) followed by correct integration, reaching $p x + q  \text{sin}  2 x$ where $p$ and $q$ are both non-zero. Accept the unsimplified form.
> 
> **M1**: Correct substitution of both limits into an integrated expression of that form, upper minus lower. The limits need to be stated, but it is condoned if the zero terms are not written out in the substitution.
> 
> **A1**: Correct exact value $\frac{π}{4}$. Accept any exact equivalent, including $\frac{1}{4} π$. Because the question asks for the exact value, a decimal such as 0.785 does not earn this mark.

### Q51
(i)

Integrating a cubed bracket produces a fourth power

Consider differentiating $( 2 x - 1 )^{4}$, which brings down a 4 from the power and a 2 from the chain rule on the bracket

`\dfrac{\text{d}}{\text{d}x}\left[(2x-1)^{4}\right] = 4 \times 2 \times (2x-1)^{3} \\ = 8(2x-1)^{3}`

**[M1]**

That is exactly the integrand, so the integral needs no adjusting at all. Integrate and add the constant

`\int 8(2x-1)^{3} \, \text{d}x = (2x-1)^{4} + c`

**[A1]**

(ii)

The bracket $2 x$ has derivative 2, so insert that factor and compensate with $- \frac{1}{2}$ outside

`\int_{0}^{\frac{\pi}{4}} \text{sin} \; 2x \, \text{d}x = -\dfrac{1}{2}\int_{0}^{\frac{\pi}{4}} -2 \, \text{sin} \; 2x \, \text{d}x`

**[M1]**

Integrate, since $- 2  \text{sin}  2 x$ is the derivative of $\text{cos}  2 x$

`= -\dfrac{1}{2}\left[\text{cos} \; 2x\right]_{0}^{\frac{\pi}{4}}`

**[A1]**

Substitute the limits

`= -\dfrac{1}{2}\left(\text{cos} \; 2\left(\frac{\pi}{4}\right) - \text{cos} \; 2(0)\right) \\ = -\dfrac{1}{2}\left(\text{cos} \; \frac{\pi}{2} - \text{cos} \; 0\right) \\ = -\dfrac{1}{2}\left(0 - 1\right)`

**[M1]**

Evaluate to give the exact value

`\int_{0}^{\frac{\pi}{4}} \text{sin} \; 2x \, \text{d}x = \dfrac{1}{2}`

**[A1]**

(iii)

The integral of $\text{e}^{3x}$ brings a factor of $\frac{1}{3}$, and here the coefficient 3 cancels it exactly

`y = \int 3\text{e}^{3x} \, \text{d}x = 3 \times \dfrac{1}{3}\text{e}^{3x}`

**[M1]**

Simplify and add the constant of integration

$y = \text{e}^{3x} + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the reverse chain rule in part (i), reaching a multiple of $( 2 x - 1 )^{4}$.
> 
> **A1**: Correct integral $( 2 x - 1 )^{4} + c$. Accept the expanded form.
> 
> **M1**: Correct use of the reverse chain rule in part (ii), reaching a multiple of $\text{cos}  2 x$.
> 
> **A1**: Correct integrated expression `-\dfrac{1}{2}\left[\text{cos} \; 2x\right]` with the limits still attached.
> 
> **M1**: Correct substitution of both limits, upper minus lower.
> 
> **A1**: Correct exact value $\frac{1}{2}$. Accept 0.5.
> 
> **M1**: Correct integration of $3 \text{e}^{3x}$ in part (iii), reaching a multiple of $\text{e}^{3x}$.
> 
> **A1**: Correct expression $y = \text{e}^{3x} + c$. Any letter may be used for the constant.

### Q52
The integrand is a product, so use the formula for integration by parts

`\int u \dfrac{\text{d}v}{\text{d}x} \, \text{d}x = uv - \int v \dfrac{\text{d}u}{\text{d}x} \, \text{d}x`

Take $u$ to be the factor that gets simpler when differentiated, and keep the 2 with the exponential so that integrating it leaves no fraction

$u = x ,  \frac{\text{d}v}{\text{d}x} = 2 \text{e}^{2x}$

$\frac{\text{d}u}{\text{d}x} = 1 ,  v = \text{e}^{2x}$

**[M1]**

Substitute into the formula

`\int 2x\text{e}^{2x} \, \text{d}x = x\text{e}^{2x} - \int \text{e}^{2x} \, \text{d}x`

**[A1]**

The remaining integral is a standard exponential, bringing out a factor of $\frac{1}{2}$

$= x \text{e}^{2x} - \frac{1}{2} \text{e}^{2x} + c$

**[M1]**

Both terms share a factor of $\frac{1}{2} \text{e}^{2x}$, so factorise to reach the required form

`\int 2x\text{e}^{2x} \, \text{d}x = \frac{1}{2}\text{e}^{2x}\left(2x - 1\right) + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct choice of $u$ and $\frac{\text{d}v}{\text{d}x}$, with $u$ taken as the linear factor, together with correct $\frac{\text{d}u}{\text{d}x}$ and $v$. A sign error in the parts formula is condoned for this mark.
> 
> **A1**: Correct substitution into the formula, reaching `x\text{e}^{2x} - \displaystyle\int \text{e}^{2x} \, \text{d}x`.
> 
> **M1**: Correct integration of the remaining integral, reaching a multiple of $\text{e}^{2x}$.
> 
> **A1**: Correct factorisation to reach the given result. Because the answer is printed, the unfactorised form $x \text{e}^{2x} - \frac{1}{2} \text{e}^{2x} + c$ must be seen before it, and the factorising step must be visible.

### Q53
Differentiate the given substitution so that $\text{d} x$ can be replaced

$u = 4 x + 1  \Rightarrow  \frac{\text{d}u}{\text{d}x} = 4  \Rightarrow  \text{d} u = 4  \text{d} x$

Because the integral is definite, convert the limits to values of $u$ as well, which avoids having to return to $x$ at the end

$x = 2  \Rightarrow  u = 4 ( 2 ) + 1 = 9$

$x = 6  \Rightarrow  u = 4 ( 6 ) + 1 = 25$

The integrand carries a factor of 4 alongside $\text{d} x$, so that whole group becomes $\text{d} u$ and the surd becomes $u^{\frac{1}{2}}$

`\int_{2}^{6} 4\sqrt{4x + 1} \, \text{d}x = \int_{9}^{25} u^{\frac{1}{2}} \, \text{d}u`

**[M1 A1]**

Integrate by increasing the power by one and dividing by the new power

`= \left[\dfrac{2u^{\frac{3}{2}}}{3}\right]_{9}^{25}`

Substitute the limits

`= \dfrac{2\left(25^{\frac{3}{2}}\right)}{3} - \dfrac{2\left(9^{\frac{3}{2}}\right)}{3} \\ = \dfrac{2(125)}{3} - \dfrac{2(27)}{3} \\ = \dfrac{250}{3} - \dfrac{54}{3}`

**[M1]**

Subtract to give the exact value

`\int_{2}^{6} 4\sqrt{4x + 1} \, \text{d}x = \dfrac{196}{3}`

**[A1]**

> **[exam-tip]**
> Changing the limits to values of $u$ at the start is usually quicker than integrating and converting back to $x$, because it saves you rewriting the integrated expression. Both are fully acceptable, so pick one and be consistent, but never mix them: substituting $x$ limits into an expression still written in $u$ is the single most common way marks are lost here.

> **[mark-scheme]**
> **M1**: Correct use of the substitution, replacing both $4 x + 1$ by $u$ and $4  \text{d} x$ by $\text{d} u$.
> 
> **A1**: Correct integral in $u$, `\displaystyle\int u^{\frac{1}{2}} \, \text{d}u`, with the limits changed to 9 and 25. If instead you keep the original limits and plan to convert back to $x$ after integrating, that is equally acceptable and earns this mark.
> 
> **M1**: Correct integration to a multiple of $u^{\frac{3}{2}}$, followed by correct use of the limits, upper minus lower. Using $x$ limits of 2 and 6 in an expression converted back to $x$ is equally acceptable.
> 
> **A1**: Correct exact value $\frac{196}{3}$. Accept any exact equivalent, such as $65 \frac{1}{3}$. Because the question asks for the exact value, a decimal such as 65.3 does not earn this mark.

### Q54
The integrand matches the standard result for an integral with a sum of two squares in the denominator, which gives an inverse tangent

`\int \frac{1}{x^{2}+a^{2}} \, \text{d}x = \frac{1}{a}\,\text{tan}^{-1}\left(\frac{x}{a}\right) + c`

The denominator is already written as $x^{2} + 5^{2}$, so apply the result with $a = 5$

`\int \frac{1}{x^{2} + 5^{2}} \, \text{d}x = \frac{1}{5}\,\text{tan}^{-1}\left(\frac{x}{5}\right) + c`

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Correct use of the standard inverse tangent integral with $a = 5$, reaching a multiple of `\text{tan}^{-1}\left(\dfrac{x}{5}\right)`.
> 
> **A1**: Correct integral `\dfrac{1}{5}\,\text{tan}^{-1}\left(\dfrac{x}{5}\right) + c`. Accept $\text{arctan}$ notation. Any letter may be used for the constant.
(i)

Every term in the denominator is divisible by 4, so factorise it out

`\frac{4}{4x^{2}+36} = \frac{4}{4\left(x^{2}+9\right)}`

Cancel the common factor of 4, and write 9 as $3^{2}$ so that the expression matches the standard form

$\frac{4}{4x^{2}+36} = \frac{1}{x^{2}+3^{2}}$

**[B1]**

(ii)

Part (i) has put the derivative into the standard form, so integrate using the same inverse tangent result, now with $a = 3$

`y = \int \frac{1}{x^{2}+3^{2}} \, \text{d}x`

**[M1]**

Apply the result and add the constant of integration

`y = \frac{1}{3}\,\text{tan}^{-1}\left(\frac{x}{3}\right) + c`

**[A1]**

> **[mark-scheme]**
> **B1**: Correct factorisation of 4 from the denominator and cancellation to reach the given result. Because the result is given, the factorised intermediate step must be visible.
> 
> **M1**: Correct use of the standard inverse tangent integral with $a = 3$, following the result of sub-part (i), reaching a multiple of `\text{tan}^{-1}\left(\dfrac{x}{3}\right)`.
> 
> **A1**: Correct expression `y = \dfrac{1}{3}\,\text{tan}^{-1}\left(\dfrac{x}{3}\right) + c`. Accept $\text{arctan}$ notation. Any letter may be used for the constant.

### Q55
(i)

Differentiate the given substitution with respect to $x$

$u = 3 x + 2  \Rightarrow  \frac{\text{d}u}{\text{d}x} = 3$

Treat the derivative as a fraction and multiply through by $\text{d} x$ to reach the required form

$\text{d} u = 3  \text{d} x$

**[B1]**

(ii)

The integrand contains a factor of 3 alongside $\text{d} x$, so group those together to make $3  \text{d} x$ appear

`\int 3 \, \text{cos} \; (3x+2) \, \text{d}x = \int \text{cos} \; (3x+2) \times 3 \, \text{d}x`

**[M1]**

Replace $3 x + 2$ by $u$ and $3  \text{d} x$ by $\text{d} u$, using the result from sub-part (i)

`\int 3 \, \text{cos} \; (3x+2) \, \text{d}x = \int \text{cos} \; u \, \text{d}u`

**[A1]**

> **[mark-scheme]**
> **B1**: Correct differentiation of the substitution to give $\frac{\text{d}u}{\text{d}x} = 3$, leading to the given result $\text{d} u = 3  \text{d} x$. Because the result is given, the differentiation must be visible.
> 
> **M1**: Correct regrouping of the integrand so that $3  \text{d} x$ appears as a single factor.
> 
> **A1**: Correct substitution of both $u$ for $3 x + 2$ and $\text{d} u$ for $3  \text{d} x$, reaching the given integral. Because the result is given, both replacements must be seen.
Part (a) has turned the integral into one in $u$, which integrates directly since $\text{cos}  u$ integrates to $\text{sin}  u$

`\int 3 \, \text{cos} \; (3x+2) \, \text{d}x = \int \text{cos} \; u \, \text{d}u`

**[M1]**

Integrate and add the constant of integration

$= \text{sin}  u + c$

**[A1]**

The question asks for the answer in terms of $x$, so reverse the substitution using $u = 3 x + 2$

`\int 3 \, \text{cos} \; (3x+2) \, \text{d}x = \text{sin} \; (3x+2) + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the result from part (a), integrating $\text{cos}  u$ to reach $\text{sin}  u$.
> 
> **A1**: Correct integral in terms of $u$, $\text{sin}  u + c$.
> 
> **A1**: Correct final answer in terms of $x$, $\text{sin}  ( 3 x + 2 ) + c$. An answer left in terms of $u$ does not earn this mark, because the question asks for an expression in $x$. Any letter may be used for the constant.

### Q56
The denominator is a product of two distinct linear factors, so each contributes a term with a constant numerator

$\frac{2x-1}{(x+1)(x-2)} \equiv \frac{A}{x+1} + \frac{B}{x-2}$

**[B1]**

Multiply through by the denominator $( x + 1 ) ( x - 2 )$ to clear the fractions

$2 x - 1 \equiv A ( x - 2 ) + B ( x + 1 )$

Substituting the value of $x$ that makes one bracket vanish isolates each constant in turn, so let $x = 2$

$2 ( 2 ) - 1 = B ( 2 + 1 )  \Rightarrow  3 = 3 B  \Rightarrow  B = 1$

**[M1]**

Now let $x = - 1$ to isolate $A$

$2 ( - 1 ) - 1 = A ( - 1 - 2 )  \Rightarrow  - 3 = - 3 A  \Rightarrow  A = 1$

Write the decomposition with both constants substituted

$\text{f} ( x ) = \frac{1}{x+1} + \frac{1}{x-2}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct form chosen for the decomposition, with a constant numerator over each of the two distinct linear factors.
> 
> **M1**: Correct method for finding the constants, either by substituting values of $x$ that make a bracket vanish or by comparing coefficients. Either method is fully acceptable.
> 
> **A1**: Both constants correct, giving $\frac{1}{x+1} + \frac{1}{x-2}$.
Replace the integrand by the partial fractions from part (a), which turns one awkward integral into two standard ones

`\int \frac{2x-1}{(x+1)(x-2)} \, \text{d}x = \int \left(\frac{1}{x+1} + \frac{1}{x-2}\right) \text{d}x`

In each term the numerator is the derivative of the denominator, so each integrates straight to a logarithm

`= \text{ln} \; |x+1| + \text{ln} \; |x-2| + \text{ln} \; c`

**[M1 A1]**

Because the question restricts to $x > 2$, both $x + 1$ and $x - 2$ are positive, so the modulus signs can be written as brackets. Writing the constant as $\text{ln}  c$ then lets all three terms combine

$= \text{ln}  ( x + 1 ) + \text{ln}  ( x - 2 ) + \text{ln}  c$

**[M1]**

Apply the addition law for logarithms to reach a single logarithm

`\int \text{f}(x) \, \text{d}x = \text{ln} \; c(x + 1)(x - 2)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the partial fractions from part (a), integrating to obtain terms of the form $p  \text{ln}  ( x + 1 ) + q  \text{ln}  ( x - 2 )$. This mark follows through from your answer to part (a).
> 
> **A1**: Both logarithms correct, $\text{ln}  ( x + 1 )$ and $\text{ln}  ( x - 2 )$. Modulus signs are condoned, present or absent.
> 
> **M1**: Correct use of a logarithm law to combine the terms, with the constant written as $\text{ln}  c$ so that it can be absorbed.
> 
> **A1**: Correct single logarithm. Accept either $\text{ln}  c ( x + 1 ) ( x - 2 )$ with the constant absorbed, or $\text{ln}  ( x + 1 ) ( x - 2 ) + c$ with the constant kept separate. Both contain a single logarithm and both score. Accept an expanded bracket, such as $\text{ln}  c ( x^{2} - x - 2 )$, and any letter for the constant. An answer left as a sum of two separate logarithms does not earn this mark.

### Q57
(i)

Writing the denominator with the $x$ term first makes the standard $\frac{1}{ax+b}$ shape easier to see

`\int \frac{1}{2-3x} \, \text{d}x = \int \frac{1}{-3x+2} \, \text{d}x`

The denominator has derivative $- 3$, so insert that on the top and compensate with $- \frac{1}{3}$ outside

`= -\dfrac{1}{3}\int \frac{-3}{-3x+2} \, \text{d}x`

**[M1]**

The numerator is now the derivative of the denominator, so the integral is a logarithm

`\int \frac{1}{2 - 3x} \, \text{d}x = -\dfrac{1}{3}\,\text{ln} \; |2-3x| + c`

**[A1]**

(ii)

Rewrite the second fraction so that its numerator can be compared with the derivative of its denominator

`y = \int \left(\frac{2}{2x+1} + \frac{-1}{-x+3}\right) \text{d}x`

In each term the numerator is exactly the derivative of the denominator, so each integrates straight to a logarithm with no adjusting needed

`y = \text{ln} \; |2x+1| + \text{ln} \; |3-x| + \text{ln} \; A`

**[M1 A1]**

Writing the constant of integration as $\text{ln}  A$ allows all three terms to be combined using the addition law for logarithms

`y = \text{ln} \; A\left|(2x+1)(3-x)\right|`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct method in sub-part (i), reaching a multiple of `\text{ln} \; |2-3x|`.
> 
> **A1**: Correct integral `-\dfrac{1}{3}\,\text{ln} \; |2-3x| + c`. The sign and the $\frac{1}{3}$ must both be right. Modulus signs are condoned, and the constant is condoned if omitted here.
> 
> **M1**: Correct method in sub-part (ii), integrating both terms to logarithms.
> 
> **A1**: Both logarithms correct, `\text{ln} \; |2x+1|` and `\text{ln} \; |3-x|`, with the correct signs. Accept `\text{ln} \; |x-3|` as an equivalent, since the modulus makes the two the same.
> 
> **A1**: Correct combination into a single logarithm. Accept either `\text{ln} \; A\left|(2x+1)(3-x)\right|` with the constant absorbed, or `\text{ln} \; \left|(2x+1)(3-x)\right| + c` with the constant kept separate. Both contain a single logarithm and both score. Accept an expanded bracket. An answer left as a sum of two separate logarithms does not earn this mark.

### Q58
(i)

Differentiate term by term, using the fact that a constant differentiates to zero

$\text{f} ' ( x ) = 4 x$

**[B1]**

(ii)

Compare the integrand with part (i): the numerator is exactly $\text{f} ' ( x )$ and the denominator is $\text{f} ( x )$, so the integral has the standard logarithmic form

`\int \frac{4x}{2x^{2}+5} \, \text{d}x = \int \frac{\text{f}'(x)}{\text{f}(x)} \, \text{d}x`

**[M1]**

The standard result for that form is the natural logarithm of the denominator

`\int \frac{\text{f}'(x)}{\text{f}(x)} \, \text{d}x = \text{ln} \; |\text{f}(x)| + c`

Apply it with $\text{f} ( x ) = 2 x^{2} + 5$

`= \text{ln} \; |2x^{2}+5| + c`

**[M1]**

Since $2 x^{2} + 5$ is positive for every value of $x$, the modulus signs make no difference here and can be written as brackets

`\int \frac{4x}{2x^{2} + 5} \, \text{d}x = \text{ln} \; (2x^{2}+5) + c`

**[A1]**

> **[mark-scheme]**
> **B1**: Correct derivative $\text{f} ' ( x ) = 4 x$.
> 
> **M1**: Correct identification that the integrand has the form $\frac{\text{f}'(x)}{\text{f}(x)}$, using the answer to part (i). This may be implied by going straight to a logarithm of the denominator.
> 
> **M1**: Correct application of the standard result, reaching a logarithm of $2 x^{2} + 5$.
> 
> **A1**: Correct integral $\text{ln}  ( 2 x^{2} + 5 ) + c$. Modulus signs are condoned either way, so `\text{ln} \; |2x^{2}+5| + c` is equally acceptable and you are not required to comment on the sign of the denominator. Any letter may be used for the constant.

### Q59
The integrand is a product of $- 3 x$, which simplifies when differentiated, and a trigonometric factor that is easy to integrate, so use the formula for integration by parts

`\int u \dfrac{\text{d}v}{\text{d}x} \, \text{d}x = uv - \int v \dfrac{\text{d}u}{\text{d}x} \, \text{d}x`

Choose $u$ to be the part that gets simpler when differentiated, and take the minus sign into the other factor so that no negative has to be carried through

$u = 3 x ,  \frac{\text{d}v}{\text{d}x} = - \text{sin}  x$

**[M1]**

Differentiate $u$ and integrate $\frac{\text{d}v}{\text{d}x}$, using the fact that $- \text{sin}  x$ integrates to $\text{cos}  x$

$\frac{\text{d}u}{\text{d}x} = 3 ,  v = \text{cos}  x$

**[A1]**

Substitute these four expressions into the formula

`\int -3x \, \text{sin} \; x \, \text{d}x = (3x)(\text{cos} \; x) - \int (\text{cos} \; x)(3) \, \text{d}x`

**[M1]**

Tidy the two terms

`= 3x \, \text{cos} \; x - \int 3 \, \text{cos} \; x \, \text{d}x`

**[A1]**

The remaining integral is now a standard one, since $\text{cos}  x$ integrates to $\text{sin}  x$

`\int 3 \, \text{cos} \; x \, \text{d}x = 3 \, \text{sin} \; x`

**[M1]**

Combine the two parts and add the constant of integration

`\int -3x \, \text{sin} \; x \, \text{d}x = 3x \, \text{cos} \; x - 3 \, \text{sin} \; x + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct choice of $u$ and $\frac{\text{d}v}{\text{d}x}$ for integration by parts, taking $u$ to be the linear factor. A sign error in the parts formula is condoned for this mark.
> 
> **A1**: Correct $\frac{\text{d}u}{\text{d}x}$ and $v$ for the chosen split.
> 
> **M1**: Correct substitution into the parts formula, reaching an expression of the form `px \, \text{cos} \; x \pm \displaystyle\int q \, \text{cos} \; x \, \text{d}x`.
> 
> **A1**: Correct expression `3x \, \text{cos} \; x - \displaystyle\int 3 \, \text{cos} \; x \, \text{d}x`, with both the sign and the coefficients right.
> 
> **M1**: Correct integration of the remaining integral to give a multiple of $\text{sin}  x$.
> 
> **A1**: Correct final answer $3 x  \text{cos}  x - 3  \text{sin}  x + c$. Any letter may be used for the constant. An equivalent form such as `3\left(x \, \text{cos} \; x - \text{sin} \; x\right) + c` is acceptable.

### Q60
(i)

The exponent $3 x - 4$ has derivative 3, so insert that factor and compensate with $\frac{1}{3}$ outside

$\frac{\text{d}y}{\text{d}x} = 7 \times \frac{1}{3} \times 3 \text{e}^{3x-4}$

**[M1]**

Integrate, since $3 \text{e}^{3x-4}$ is the derivative of $\text{e}^{3x-4}$, and add the constant of integration

$y = \frac{7}{3} \text{e}^{3x-4} + c$

**[A1]**

(ii)

An integrand of the form $\frac{1}{ax+b}$ integrates to a logarithm, so insert the derivative 4 on the top and compensate with $\frac{1}{4}$ outside

`\int \dfrac{1}{4x+9} \, \text{d}x = \dfrac{1}{4}\int \dfrac{4}{4x+9} \, \text{d}x`

**[M1]**

The top is now the derivative of the bottom, so the integral is the natural logarithm of the denominator

`\int \frac{1}{4x + 9} \, \text{d}x = \dfrac{1}{4}\,\text{ln} \; |4x+9| + c`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the reverse chain rule in part (i), reaching a multiple of $\text{e}^{3x-4}$.
> 
> **A1**: Correct expression $y = \frac{7}{3} \text{e}^{3x-4} + c$. Any letter may be used for the constant.
> 
> **M1**: Correct method in part (ii), reaching a multiple of `\text{ln} \; |4x+9|`.
> 
> **A1**: Correct integral `\dfrac{1}{4}\,\text{ln} \; |4x+9| + c`. The modulus signs are condoned, so $\frac{1}{4}  \text{ln}  ( 4 x + 9 ) + c$ also earns this mark. Accept `\text{ln} \; |4x+9|^{\frac{1}{4}}` as an equivalent form.

### Q61
(i)

Integrating is the reverse of differentiating, so look for the function whose derivative is $\frac{1}{x}$

`\dfrac{\text{d}}{\text{d}x}\left(\text{ln} \; x\right) = \dfrac{1}{x}`

**[M1]**

Reversing this gives the integral, and an indefinite integral needs a constant of integration

`\int \frac{1}{x} \text{d}x = \text{ln} \; |x| + c`

**[A1]**

(ii)

The integral of $\text{e}^{x}$ is itself, since `\dfrac{\text{d}}{\text{d}x}\left(\text{e}^{x}\right) = \text{e}^{x}`, so integrate and write the result in brackets with the limits

`\int_{0}^{1} \text{e}^{x} \text{d}x = \left[\text{e}^{x}\right]_{0}^{1}`

**[M1]**

Substitute the limits

$= \text{e}^{1} - \text{e}^{0}$

Since $\text{e}^{0} = 1$

`\int_{0}^{1} \text{e}^{x} \, \text{d}x = \text{e} - 1`

**[A1]**

(iii)

The integral of $\text{cos}  θ$ is $\text{sin}  θ$, and the constant multiple of 3 carries through

`\int 3 \, \text{cos} \; \theta \, \text{d}\theta = 3 \, \text{sin} \; \theta`

**[M1]**

Add the constant of integration to complete the expression for $y$

$y = 3  \text{sin}  θ + c$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the fact that $\frac{1}{x}$ integrates to a logarithm, in part (i).
> 
> **A1**: Correct integral `\text{ln} \; |x| + c`. The modulus signs are condoned, so $\text{ln}  x + c$ also earns this mark.
> 
> **M1**: Correct integration of $\text{e}^{x}$ in part (ii), with the limits attached, giving `\left[\text{e}^{x}\right]_{0}^{1}`.
> 
> **A1**: Correct exact value $\text{e} - 1$. Because the question says to use calculus, a decimal such as 1.72 does not earn this mark on its own.
> 
> **M1**: Correct integration of $3  \text{cos}  θ$ to give $3  \text{sin}  θ$ in part (iii).
> 
> **A1**: Correct expression $y = 3  \text{sin}  θ + c$. Any letter may be used for the constant.
