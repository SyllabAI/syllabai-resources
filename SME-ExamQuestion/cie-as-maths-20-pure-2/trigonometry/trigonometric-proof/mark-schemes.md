# Mark Schemes — Trigonometric Proof
**Trigonometry** · Cambridge (CIE) AS maths (9709)


## Exam Questions (27 questions)


### Q1
Start from the left-hand side and use the definitions $\text{cosec}  2 x = \frac{1}{\text{sin}2x}$ and $\text{cot}  x = \frac{\text{cos}x}{\text{sin}x}$

$2  \text{cosec}  2 x  \text{cot}  x \equiv \frac{2}{\text{sin}2x} \times \frac{\text{cos}x}{\text{sin}x}$

**[M1 A1]**

Write the double angle in terms of $x$ alone, using $\text{sin}  2 x \equiv 2  \text{sin}  x  \text{cos}  x$

$\equiv \frac{2}{2\text{sin}x\text{cos}x} \times \frac{\text{cos}x}{\text{sin}x}$

**[M1]**

Cancel the factor of $2$ and the factor $\text{cos}  x$, both non-zero because $x \neq \frac{kπ}{2}$

$\equiv \frac{1}{\text{sin}^{2}x}$

**[A1]**

Use the definition $\text{cosec}  x = \frac{1}{\text{sin}x}$

`\equiv \left( \dfrac{1}{\text{sin} \; x} \right)^2 \equiv \text{cosec}^2 \; x`

This is the required result

$2  \text{cosec}  2 x  \text{cot}  x \equiv \text{cosec}^{2}  x$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the definitions of $\text{cosec}  2 x$ and $\text{cot}  x$ to write the left-hand side in terms of sine and cosine.
> 
> **A1**: Correct resulting product.
> 
> **M1**: Correct use of $\text{sin}  2 x \equiv 2  \text{sin}  x  \text{cos}  x$.
> 
> **A1**: Correct cancellation to $\frac{1}{\text{sin}^{2}x}$.
> 
> **A1**: Correct use of the definition of $\text{cosec}  x$ to reach the printed result, from full and correct working.
> 
> Because the result is given, the cancellation must be visible; jumping from the product straight to $\text{cosec}^{2}  x$ loses the final two marks. Reference to the condition on $x$ is not required.

### Q2
Start from the left-hand side, which is the more complicated one, and use the definitions $\text{sec}  θ = \frac{1}{\text{cos}θ}$ and $\text{cosec}  θ = \frac{1}{\text{sin}θ}$

`\text{sin}^2 \; \theta \; (\text{sec}^2 \; \theta + \text{cosec}^2 \; \theta) \equiv \text{sin}^2 \; \theta \left( \dfrac{1}{\text{cos}^2 \; \theta} + \dfrac{1}{\text{sin}^2 \; \theta} \right)`

**[M1]**

Multiply out the bracket

$\equiv \frac{\text{sin}^{2}θ}{\text{cos}^{2}θ} + \frac{\text{sin}^{2}θ}{\text{sin}^{2}θ}$

**[A1]**

Use the definition $\text{tan}  θ = \frac{\text{sin}θ}{\text{cos}θ}$ on the first term, and cancel the second

$\equiv \text{tan}^{2}  θ + 1$

**[A1]**

Finish with the identity $1 + \text{tan}^{2}  θ \equiv \text{sec}^{2}  θ$

$\equiv \text{sec}^{2}  θ$

This is the required result

$\text{sin}^{2}  θ  ( \text{sec}^{2}  θ + \text{cosec}^{2}  θ ) \equiv \text{sec}^{2}  θ$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $\text{sec}^{2}  θ \equiv \frac{1}{\text{cos}^{2}θ}$ and $\text{cosec}^{2}  θ \equiv \frac{1}{\text{sin}^{2}θ}$.
> 
> **A1**: Correct expansion of the bracket.
> 
> **A1**: Correct simplification to $\text{tan}^{2}  θ + 1$, or to $\frac{\text{sin}^{2}θ}{\text{cos}^{2}θ} + 1$.
> 
> **A1**: Correct use of $1 + \text{tan}^{2}  θ \equiv \text{sec}^{2}  θ$ to reach the printed result, from full and correct working.
> 
> Working from the right-hand side towards the left is equally acceptable. Because the result is given, each expression in the chain must be seen; an algebraic slip anywhere loses the final mark even if the last line is correct.

### Q3
Start from the left-hand side and use the double angle formula $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$

$3  \text{sin}  2 θ - 2  \text{sin}  θ \equiv 3 ( 2  \text{sin}  θ  \text{cos}  θ ) - 2  \text{sin}  θ$

**[M1]**

Multiply out the first term

$\equiv 6  \text{sin}  θ  \text{cos}  θ - 2  \text{sin}  θ$

**[A1]**

Both terms share a factor of $2  \text{sin}  θ$, so take it outside a bracket

$3  \text{sin}  2 θ - 2  \text{sin}  θ \equiv 2  \text{sin}  θ  ( 3  \text{cos}  θ - 1 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$.
> 
> **A1**: Correct expansion to $6  \text{sin}  θ  \text{cos}  θ - 2  \text{sin}  θ$.
> 
> **A1**: Correct factorisation to reach the printed result, from full and correct working.
> 
> Expanding the right-hand side to meet the left is equally acceptable. Because the result is given, the expanded form must be seen before the factorised one.

### Q4
Compare `4 \; \text{sin} \left( \theta + \dfrac{\pi}{4} \right)` with $R  \text{sin}  ( θ + α )$ to read off the two constants

$R = 4$

$α = \frac{π}{4}$

Substitute these into the right-hand side of the given identity

`4 \; \text{sin} \left( \theta + \dfrac{\pi}{4} \right) \equiv 4 \; \text{cos} \; \dfrac{\pi}{4} \; \text{sin} \; \theta + 4 \; \text{sin} \; \dfrac{\pi}{4} \; \text{cos} \; \theta`

**[M1]**

Use the exact values $\text{cos}  \frac{π}{4} = \text{sin}  \frac{π}{4} = \frac{\sqrt{2}}{2}$

`\equiv 4 \left( \dfrac{\sqrt{2}}{2} \right) \text{sin} \; \theta + 4 \left( \dfrac{\sqrt{2}}{2} \right) \text{cos} \; \theta`

Simplify each coefficient

$\equiv 2 \sqrt{2}  \text{sin}  θ + 2 \sqrt{2}  \text{cos}  θ$

**[A1]**

Both terms share the factor $2 \sqrt{2}$, so take it outside a bracket

`4 \; \text{sin} \left( \theta + \dfrac{\pi}{4} \right) \equiv 2\sqrt{2} \; (\text{sin} \; \theta + \text{cos} \; \theta)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct substitution of $R = 4$ and $α = \frac{π}{4}$ into the given identity.
> 
> **A1**: Correct use of the exact values of $\text{cos}  \frac{π}{4}$ and $\text{sin}  \frac{π}{4}$, simplified to coefficients of $2 \sqrt{2}$.
> 
> **A1**: Correct factorisation to reach the printed result, from full and correct working.
> 
> Accept $\frac{1}{\sqrt{2}}$ in place of $\frac{\sqrt{2}}{2}$. Because the result is given, the unsimplified substituted form must be seen before the final answer.

### Q5
(i)

Use the definition $\text{cosec}  x = \frac{1}{\text{sin}x}$ to write the function as a quotient

$\text{cosec}  x = \frac{1}{\text{sin}x}$

Identify the numerator and differentiate it

$u = 1 \Rightarrow \frac{\text{d}u}{\text{d}x} = 0$

Do the same for the denominator

$v = \text{sin}  x \Rightarrow \frac{\text{d}v}{\text{d}x} = \text{cos}  x$

**[M1]**

Use the quotient rule, $\frac{\text{d}y}{\text{d}x} = \frac{v\frac{\text{d}u}{\text{d}x}-u\frac{\text{d}v}{\text{d}x}}{v^{2}}$

`\dfrac{\text{d}}{\text{d}x} \left[ \text{cosec} \; x \right] = \dfrac{(\text{sin} \; x)(0) - (1)(\text{cos} \; x)}{(\text{sin} \; x)^2}`

**[M1]**

Simplify the numerator

`\dfrac{\text{d}}{\text{d}x} \left[ \text{cosec} \; x \right] = \dfrac{- \text{cos} \; x}{\text{sin}^2 \; x}`

**[A1]**

(ii)

Split the single fraction into two factors, so that each can be recognised

$\frac{-\text{cos}x}{\text{sin}^{2}x} = - \frac{\text{cos}x}{\text{sin}x} \times \frac{1}{\text{sin}x}$

**[M1]**

Use the definitions $\text{cot}  x = \frac{\text{cos}x}{\text{sin}x}$ and $\text{cosec}  x = \frac{1}{\text{sin}x}$

$= - \text{cot}  x  \text{cosec}  x$

This is the required result

`\dfrac{\text{d}}{\text{d}x} \left[ \text{cosec} \; x \right] = - \text{cot} \; x \; \text{cosec} \; x`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $\text{cosec}  x = \frac{1}{\text{sin}x}$ together with correct $u$, $v$ and their derivatives.
> 
> **M1**: Correct substitution into the quotient rule.
> 
> **A1**: Correct simplification to the first printed result.
> 
> **M1**: Correct splitting of $\frac{-\text{cos}x}{\text{sin}^{2}x}$ into a product of two fractions.
> 
> **A1**: Correct use of the definitions of $\text{cot}  x$ and $\text{cosec}  x$ to reach the second printed result.
> 
> Both results are given, so the substitution into the quotient rule and the split into a product must both be visible. In (ii), writing $\text{cosec}^{2}  x  \text{cos}  x$ and then converting is equally acceptable.

### Q6
Begin with the left-hand side and use the double angle formula $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$

$\frac{\text{sin}2θ}{2\text{sin}θ} \equiv \frac{2\text{sin}θ\text{cos}θ}{2\text{sin}θ}$

**[M1]**

Cancel the factor $2  \text{sin}  θ$, which is non-zero because $θ \neq k π$

$\frac{\text{sin}2θ}{2\text{sin}θ} \equiv \text{cos}  θ$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$ in the numerator.
> 
> **A1**: Correct cancellation to reach the printed result, from full and correct working.
> 
> Because the result is given, the substituted form must be seen before the cancellation. Reference to the condition $θ \neq k π$ is not required for the mark.

### Q7
The target is written in $\frac{x}{2}$, so start from the definition of $\text{cosec}  x$ and expand $\text{sin}  x$ as a double angle in $\frac{x}{2}$, using $\text{sin}  2 A \equiv 2  \text{sin}  A  \text{cos}  A$ with $A = \frac{x}{2}$

$\text{cosec}  x \equiv \frac{1}{\text{sin}x} \equiv \frac{1}{2\text{sin}\frac{x}{2}\text{cos}\frac{x}{2}}$

**[M1 A1]**

The answer contains $\text{sec}^{2}  \frac{x}{2}$ and $\text{tan}  \frac{x}{2}$, both of which have $\text{cos}  \frac{x}{2}$ underneath, so divide numerator and denominator by $\text{cos}^{2}  \frac{x}{2}$

`\equiv \dfrac{\dfrac{1}{\text{cos}^2 \; \dfrac{x}{2}}}{2 \left( \dfrac{\text{sin} \; \dfrac{x}{2}}{\text{cos} \; \dfrac{x}{2}} \right)}`

**[M1]**

Use the definitions $\text{sec}  \frac{x}{2} = \frac{1}{\text{cos}\frac{x}{2}}$ and $\text{tan}  \frac{x}{2} = \frac{\text{sin}\frac{x}{2}}{\text{cos}\frac{x}{2}}$, then move the $2$ into the numerator

$\equiv \frac{\text{sec}^{2}\frac{x}{2}}{2\text{tan}\frac{x}{2}} \equiv \frac{\frac{1}{2}\text{sec}^{2}\frac{x}{2}}{\text{tan}\frac{x}{2}}$

This is the required result

$\text{cosec}  x \equiv \frac{\frac{1}{2}\text{sec}^{2}\frac{x}{2}}{\text{tan}\frac{x}{2}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the definition of $\text{cosec}  x$ together with the double angle formula applied with $A = \frac{x}{2}$.
> 
> **A1**: Correct expression $\frac{1}{2\text{sin}\frac{x}{2}\text{cos}\frac{x}{2}}$.
> 
> **M1**: Correct division of numerator and denominator by $\text{cos}^{2}  \frac{x}{2}$.
> 
> **A1**: Correct use of the definitions of $\text{sec}  \frac{x}{2}$ and $\text{tan}  \frac{x}{2}$ to reach the printed result, from full and correct working.
> 
> Accept the equivalent intermediate form $\frac{\text{sec}^{2}\frac{x}{2}}{2\text{tan}\frac{x}{2}}$ before the $2$ is moved. Working from the right-hand side towards the left earns the same marks.

### Q8
Start from the left-hand side and use the definitions $\text{cot}  θ = \frac{\text{cos}θ}{\text{sin}θ}$ and $\text{tan}  θ = \frac{\text{sin}θ}{\text{cos}θ}$

$\text{cot}^{2}  θ - \text{tan}^{2}  θ \equiv \frac{\text{cos}^{2}θ}{\text{sin}^{2}θ} - \frac{\text{sin}^{2}θ}{\text{cos}^{2}θ}$

**[M1]**

Combine the two fractions over the common denominator $\text{sin}^{2}  θ  \text{cos}^{2}  θ$

$\equiv \frac{\text{cos}^{4}θ-\text{sin}^{4}θ}{\text{sin}^{2}θ\text{cos}^{2}θ}$

**[A1]**

The numerator is a difference of two squares, so factorise it

$\equiv \frac{(\text{cos}^{2}θ-\text{sin}^{2}θ)(\text{cos}^{2}θ+\text{sin}^{2}θ)}{\text{sin}^{2}θ\text{cos}^{2}θ}$

The second bracket is $1$ by the identity $\text{sin}^{2}  θ + \text{cos}^{2}  θ \equiv 1$

$\equiv \frac{\text{cos}^{2}θ-\text{sin}^{2}θ}{\text{sin}^{2}θ\text{cos}^{2}θ}$

**[M1]**

The target is in $2 θ$, and $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$ squares to $4  \text{sin}^{2}  θ  \text{cos}^{2}  θ$, so multiply numerator and denominator by $4$

$\equiv \frac{4(\text{cos}^{2}θ-\text{sin}^{2}θ)}{(2\text{sin}θ\text{cos}θ)^{2}}$

Apply $\text{cos}  2 θ \equiv \text{cos}^{2}  θ - \text{sin}^{2}  θ$ to the numerator and $\text{sin}  2 θ$ to the denominator

$\equiv \frac{4\text{cos}2θ}{\text{sin}^{2}2θ}$

**[A1]**

Split into two factors and use the definitions of $\text{cot}  2 θ$ and $\text{cosec}  2 θ$

`\equiv 4 \left( \dfrac{\text{cos} \; 2\theta}{\text{sin} \; 2\theta} \right) \left( \dfrac{1}{\text{sin} \; 2\theta} \right) \equiv 4 \; \text{cot} \; 2\theta \; \text{cosec} \; 2\theta`

This is the required result

$\text{cot}^{2}  θ - \text{tan}^{2}  θ \equiv 4  \text{cot}  2 θ  \text{cosec}  2 θ$

**[A1]**

> **[exam-tip]**
> The step that unlocks this one is multiplying top and bottom by $4$. It looks like it comes from nowhere, but the target is written in $2 θ$, and squaring $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$ produces exactly $4  \text{sin}^{2}  θ  \text{cos}^{2}  θ$. When an answer is in $2 θ$ and your working is in $θ$, ask what constant you need to manufacture the double angle form.

> **[mark-scheme]**
> **M1**: Correct use of the definitions of $\text{cot}  θ$ and $\text{tan}  θ$.
> 
> **A1**: Correct combination into a single fraction with numerator $\text{cos}^{4}  θ - \text{sin}^{4}  θ$.
> 
> **M1**: Correct factorisation of the difference of two squares together with correct use of $\text{sin}^{2}  θ + \text{cos}^{2}  θ \equiv 1$.
> 
> **A1**: Correct conversion to $\frac{4\text{cos}2θ}{\text{sin}^{2}2θ}$.
> 
> **A1**: Correct split into $\text{cot}  2 θ$ and $\text{cosec}  2 θ$ to reach the printed result, from full and correct working.
> 
> Because the result is given, the factorised numerator and the $2 θ$ form must both be seen. Working from the right-hand side towards the left earns the same marks.

### Q9
Split $3 θ$ into $2 θ + θ$ so the compound angle formula applies, using $\text{sin}  ( A + B ) \equiv \text{sin}  A  \text{cos}  B + \text{cos}  A  \text{sin}  B$

$\text{sin}  3 θ \equiv \text{sin}  2 θ  \text{cos}  θ + \text{cos}  2 θ  \text{sin}  θ$

**[M1 A1]**

Replace both double angles, taking $\text{cos}  2 θ$ in its sine form since the target is in sine only

$\equiv ( 2  \text{sin}  θ  \text{cos}  θ ) \text{cos}  θ + ( 1 - 2  \text{sin}^{2}  θ ) \text{sin}  θ$

**[M1]**

Multiply out both products

$\equiv 2  \text{sin}  θ  \text{cos}^{2}  θ + \text{sin}  θ - 2  \text{sin}^{3}  θ$

Remove the last cosine term using $\text{cos}^{2}  θ \equiv 1 - \text{sin}^{2}  θ$

$\equiv 2  \text{sin}  θ  ( 1 - \text{sin}^{2}  θ ) + \text{sin}  θ - 2  \text{sin}^{3}  θ$

Expand both brackets

$\equiv 2  \text{sin}  θ - 2  \text{sin}^{3}  θ + \text{sin}  θ - 2  \text{sin}^{3}  θ$

Collect like terms

$\text{sin}  3 θ \equiv 3  \text{sin}  θ - 4  \text{sin}^{3}  θ$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the compound angle formula on $\text{sin}  ( 2 θ + θ )$.
> 
> **A1**: Correct expansion to $\text{sin}  2 θ  \text{cos}  θ + \text{cos}  2 θ  \text{sin}  θ$.
> 
> **M1**: Correct use of both double angle formulae.
> 
> **A1**: Correct use of $\text{cos}^{2}  θ \equiv 1 - \text{sin}^{2}  θ$ and correct collection of terms to reach the printed result, from full and correct working.
> 
> Any of the three forms of the double angle formula for cosine may be used, provided every term is in sine before the final line. Splitting $3 θ$ as $θ + 2 θ$ is equally acceptable. Because the result is given, the expanded form must be seen before the collected one.

### Q10
Start from the right-hand side, which is the more complicated one, and use $\text{cosec}  x = \frac{1}{\text{sin}x}$ and $\text{cot}  x = \frac{\text{cos}x}{\text{sin}x}$

$\frac{1}{\text{cosec}x+\text{cot}x} \equiv \frac{1}{\frac{1}{\text{sin}x}+\frac{\text{cos}x}{\text{sin}x}}$

**[M1]**

Combine the denominator into a single fraction

$\equiv \frac{1}{\frac{1+\text{cos}x}{\text{sin}x}}$

Dividing by a fraction is the same as multiplying by its reciprocal

$\equiv \frac{\text{sin}x}{1+\text{cos}x}$

**[A1]**

The target is in $\frac{x}{2}$, so expand both $\text{sin}  x$ and $\text{cos}  x$ as double angles in $\frac{x}{2}$, choosing the cosine form that will cancel the $1$

`\equiv \dfrac{2 \; \text{sin} \; \dfrac{x}{2} \; \text{cos} \; \dfrac{x}{2}}{1 + \left( 2 \; \text{cos}^2 \; \dfrac{x}{2} - 1 \right)}`

**[M1]**

Simplify the denominator, where the $+ 1$ and $- 1$ cancel

$\equiv \frac{2\text{sin}\frac{x}{2}\text{cos}\frac{x}{2}}{2\text{cos}^{2}\frac{x}{2}}$

Cancel the factor of $2$ and one factor of $\text{cos}  \frac{x}{2}$

$\equiv \frac{\text{sin}\frac{x}{2}}{\text{cos}\frac{x}{2}}$

**[A1]**

Use the definition $\text{tan}  \frac{x}{2} = \frac{\text{sin}\frac{x}{2}}{\text{cos}\frac{x}{2}}$

$\equiv \text{tan}  \frac{x}{2}$

This is the required result

$\text{tan}  \frac{x}{2} \equiv \frac{1}{\text{cosec}x+\text{cot}x}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the definitions of $\text{cosec}  x$ and $\text{cot}  x$.
> 
> **A1**: Correct simplification to $\frac{\text{sin}x}{1+\text{cos}x}$.
> 
> **M1**: Correct use of both double angle formulae with $A = \frac{x}{2}$.
> 
> **A1**: Correct cancellation to $\frac{\text{sin}\frac{x}{2}}{\text{cos}\frac{x}{2}}$.
> 
> **A1**: Correct use of the definition of $\text{tan}  \frac{x}{2}$ to reach the printed result, from full and correct working.
> 
> Any of the three forms of $\text{cos}  2 A$ may be used; $2  \text{cos}^{2}  \frac{x}{2} - 1$ is the most direct, as the other two need the Pythagorean identity applied to the denominator first. Because the result is given, the cancellation must be visible.

### Q11
Use $\text{tan}  x = \frac{\text{sin}x}{\text{cos}x}$ in the numerator, and expand the denominator with $\text{cos}  2 x \equiv \text{cos}^{2}  x - \text{sin}^{2}  x$

$\frac{1-\text{tan}^{2}x}{\text{cos}2x} \equiv \frac{1-\frac{\text{sin}^{2}x}{\text{cos}^{2}x}}{\text{cos}^{2}x-\text{sin}^{2}x}$

**[M1 A1]**

Write the numerator as a single fraction over $\text{cos}^{2}  x$

$\equiv \frac{\frac{\text{cos}^{2}x-\text{sin}^{2}x}{\text{cos}^{2}x}}{\text{cos}^{2}x-\text{sin}^{2}x}$

**[M1]**

Dividing by $\text{cos}^{2}  x - \text{sin}^{2}  x$ cancels the matching factor, which is non-zero because $x \neq \frac{(2k+1)π}{4}$

$\equiv \frac{1}{\text{cos}^{2}x}$

**[A1]**

Use the definition $\text{sec}  x = \frac{1}{\text{cos}x}$

`\equiv \left( \dfrac{1}{\text{cos} \; x} \right)^2 \equiv \text{sec}^2 \; x`

This is the required result

$\frac{1-\text{tan}^{2}x}{\text{cos}2x} \equiv \text{sec}^{2}  x$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $\text{tan}  x = \frac{\text{sin}x}{\text{cos}x}$ in the numerator.
> 
> **A1**: Correct use of $\text{cos}  2 x \equiv \text{cos}^{2}  x - \text{sin}^{2}  x$ in the denominator.
> 
> **M1**: Correct combination of the numerator into a single fraction over $\text{cos}^{2}  x$.
> 
> **A1**: Correct cancellation to $\frac{1}{\text{cos}^{2}x}$.
> 
> **A1**: Correct use of the definition of $\text{sec}  x$ to reach the printed result, from full and correct working.
> 
> Choosing the $\text{cos}^{2}  x - \text{sin}^{2}  x$ form of the double angle formula is what produces the cancellation; the other two forms do not lead anywhere useful here. Because the result is given, the cancellation must be visible. Reference to the condition on $x$ is not required.

### Q12
(i)

The given identity holds for any two angles, so choose $A = B = θ$ to create the angle $2 θ$

$\text{cos}  ( θ + θ ) \equiv \text{cos}  θ  \text{cos}  θ - \text{sin}  θ  \text{sin}  θ$

**[M1]**

Simplify both sides

$\text{cos}  2 θ \equiv \text{cos}^{2}  θ - \text{sin}^{2}  θ$

**[A1]**

(ii)

The target is in terms of sine only, so replace $\text{cos}^{2}  θ$ using $\text{cos}^{2}  θ \equiv 1 - \text{sin}^{2}  θ$

$\text{cos}  2 θ \equiv ( 1 - \text{sin}^{2}  θ ) - \text{sin}^{2}  θ$

Collect the two sine terms

$\text{cos}  2 θ \equiv 1 - 2  \text{sin}^{2}  θ$

**[B1]**

(iii)

This target is in terms of cosine only, so replace $\text{sin}^{2}  θ$ using $\text{sin}^{2}  θ \equiv 1 - \text{cos}^{2}  θ$

$\text{cos}  2 θ \equiv \text{cos}^{2}  θ - ( 1 - \text{cos}^{2}  θ )$

Collect the two cosine terms

$\text{cos}  2 θ \equiv 2  \text{cos}^{2}  θ - 1$

**[B1]**

> **[mark-scheme]**
> **M1**: Correct substitution of $A = B = θ$ into the given identity.
> 
> **A1**: Correct simplification to the first printed result.
> 
> **B1**: Correct use of $\text{cos}^{2}  θ \equiv 1 - \text{sin}^{2}  θ$ to reach the second printed result.
> 
> **B1**: Correct use of $\text{sin}^{2}  θ \equiv 1 - \text{cos}^{2}  θ$ to reach the third printed result.
> 
> In (ii) and (iii) the substituted form must be seen before the collected one. Starting each of (ii) and (iii) from $\text{cos}^{2}  θ - \text{sin}^{2}  θ$ rather than from $\text{cos}  2 θ$ is equally acceptable.

### Q13
Replace the constant term with its exact value, $\text{cos}  \frac{π}{3} = \frac{1}{2}$

$\text{cos}  4 θ + \text{cos}  \frac{π}{3} \equiv \text{cos}  4 θ + \frac{1}{2}$

**[B1]**

The answer is in sine only, so treat $4 θ$ as double the angle $2 θ$ and choose the sine form $\text{cos}  2 A \equiv 1 - 2  \text{sin}^{2}  A$

$\equiv 1 - 2  \text{sin}^{2}  2 θ + \frac{1}{2}$

**[M1]**

Replace $\text{sin}  2 θ$ using $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$

$\equiv 1 - 2 ( 2  \text{sin}  θ  \text{cos}  θ )^{2} + \frac{1}{2}$

**[M1]**

Square the bracket

$\equiv 1 - 2 ( 4  \text{sin}^{2}  θ  \text{cos}^{2}  θ ) + \frac{1}{2}$

Multiply out

$\equiv 1 - 8  \text{sin}^{2}  θ  \text{cos}^{2}  θ + \frac{1}{2}$

**[A1]**

Remove the cosine term using $\text{cos}^{2}  θ \equiv 1 - \text{sin}^{2}  θ$

$\equiv 1 - 8  \text{sin}^{2}  θ  ( 1 - \text{sin}^{2}  θ ) + \frac{1}{2}$

Expand the bracket

$\equiv 1 - 8  \text{sin}^{2}  θ + 8  \text{sin}^{4}  θ + \frac{1}{2}$

Collect the constants

$\text{cos}  4 θ + \text{cos}  \frac{π}{3} \equiv 8  \text{sin}^{4}  θ - 8  \text{sin}^{2}  θ + \frac{3}{2}$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct exact value $\text{cos}  \frac{π}{3} = \frac{1}{2}$.
> 
> **M1**: Correct expression of $\text{cos}  4 θ$ as a double angle in $2 θ$.
> 
> **M1**: Correct use of $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$, including squaring the whole bracket.
> 
> **A1**: Correct simplification to $1 - 8  \text{sin}^{2}  θ  \text{cos}^{2}  θ + \frac{1}{2}$.
> 
> **A1**: Correct use of $\text{cos}^{2}  θ \equiv 1 - \text{sin}^{2}  θ$, with expansion and collection to reach the printed result, from full and correct working.
> 
> Any of the three forms of the double angle formula for cosine may be used, provided every term is in sine before the final line. Deriving $\text{cos}  4 θ$ on its own and adding $\frac{1}{2}$ at the end earns the same marks. A common error is squaring only part of $2  \text{sin}  θ  \text{cos}  θ$, which loses the second mark.

### Q14
Treat $4 θ$ as double the angle $2 θ$ and apply $\text{tan}  2 A \equiv \frac{2\text{tan}A}{1-\text{tan}^{2}A}$ with $A = 2 θ$

$\text{tan}  4 θ \equiv \frac{2\text{tan}2θ}{1-\text{tan}^{2}2θ}$

**[M1]**

Apply the same formula again with $A = θ$ to replace every $\text{tan}  2 θ$

`\equiv \dfrac{2 \left( \dfrac{2 \; \text{tan} \; \theta}{1 - \text{tan}^2 \; \theta} \right)}{1 - \left( \dfrac{2 \; \text{tan} \; \theta}{1 - \text{tan}^2 \; \theta} \right)^2}`

**[M1]**

Multiply numerator and denominator by $( 1 - \text{tan}^{2}  θ )^{2}$ to clear the compound fraction

$\equiv \frac{4\text{tan}θ(1-\text{tan}^{2}θ)}{(1-\text{tan}^{2}θ)^{2}-(2\text{tan}θ)^{2}}$

**[A1]**

Expand the denominator

$\equiv \frac{4\text{tan}θ(1-\text{tan}^{2}θ)}{1-2\text{tan}^{2}θ+\text{tan}^{4}θ-4\text{tan}^{2}θ}$

Collect the like terms in the denominator

$\text{tan}  4 θ \equiv \frac{4\text{tan}θ(1-\text{tan}^{2}θ)}{1-6\text{tan}^{2}θ+\text{tan}^{4}θ}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the double angle formula for tangent with $A = 2 θ$.
> 
> **M1**: Correct use of the double angle formula for tangent with $A = θ$, substituted into both the numerator and the denominator.
> 
> **A1**: Correct clearing of the compound fraction to give denominator $( 1 - \text{tan}^{2}  θ )^{2} - ( 2  \text{tan}  θ )^{2}$.
> 
> **A1**: Correct expansion to reach the printed result, from full and correct working.
> 
> The numerator is left factorised throughout, matching the printed form. Because the result is given, the unexpanded denominator must be seen before the collected one; a sign slip in $( 1 - \text{tan}^{2}  θ )^{2}$ loses the final mark.

### Q15
Split $3 θ$ into $2 θ + θ$ so the compound angle formula applies, using $\text{sin}  ( A + B ) \equiv \text{sin}  A  \text{cos}  B + \text{cos}  A  \text{sin}  B$

$\text{sin}  3 θ \equiv \text{sin}  2 θ  \text{cos}  θ + \text{cos}  2 θ  \text{sin}  θ$

**[M1 A1]**

Replace both double angles, taking $\text{cos}  2 θ$ in the form $\text{cos}^{2}  θ - \text{sin}^{2}  θ$ since the answer keeps both functions

$\equiv ( 2  \text{sin}  θ  \text{cos}  θ ) \text{cos}  θ + ( \text{cos}^{2}  θ - \text{sin}^{2}  θ ) \text{sin}  θ$

**[M1]**

Multiply out both products

$\equiv 2  \text{sin}  θ  \text{cos}^{2}  θ + \text{sin}  θ  \text{cos}^{2}  θ - \text{sin}^{3}  θ$

Collect the two matching terms

$\text{sin}  3 θ \equiv 3  \text{sin}  θ  \text{cos}^{2}  θ - \text{sin}^{3}  θ$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the compound angle formula on $\text{sin}  ( 2 θ + θ )$.
> 
> **A1**: Correct expansion to $\text{sin}  2 θ  \text{cos}  θ + \text{cos}  2 θ  \text{sin}  θ$.
> 
> **M1**: Correct use of both double angle formulae.
> 
> **A1**: Correct expansion and collection of terms to reach the printed result, from full and correct working.
> 
> The $\text{cos}^{2}  θ - \text{sin}^{2}  θ$ form of the double angle formula leads most directly to the printed answer. Another form may be used, provided it is converted back so that both functions appear. Because the result is given, the expanded form must be seen before the collected one.
Deal with the numerator first, splitting $3 θ$ into $2 θ + θ$ and applying $\text{cos}  ( A + B ) \equiv \text{cos}  A  \text{cos}  B - \text{sin}  A  \text{sin}  B$

$\text{cos}  3 θ \equiv \text{cos}  2 θ  \text{cos}  θ - \text{sin}  2 θ  \text{sin}  θ$

Now replace both double angles. Of the three forms of $\text{cos}  2 θ$, choose $1 - 2  \text{sin}^{2}  θ$, because it is the one that leaves a lone $\text{cos}  θ$, and that term will cancel against the $-  \text{cos}  θ$ subtracted next

$\equiv ( 1 - 2  \text{sin}^{2}  θ ) \text{cos}  θ - ( 2  \text{sin}  θ  \text{cos}  θ ) \text{sin}  θ$

**[M1]**

Multiply out both products

$\equiv \text{cos}  θ - 2  \text{sin}^{2}  θ  \text{cos}  θ - 2  \text{sin}^{2}  θ  \text{cos}  θ$

Collect the two matching terms

$\text{cos}  3 θ \equiv \text{cos}  θ - 4  \text{sin}^{2}  θ  \text{cos}  θ$

Subtract $\text{cos}  θ$ from both sides to build the numerator of the quotient

$\text{cos}  3 θ - \text{cos}  θ \equiv - 4  \text{sin}^{2}  θ  \text{cos}  θ$

**[A1]**

Turn to the denominator, and multiply the result from part (a), $\text{sin}  3 θ \equiv 3  \text{sin}  θ  \text{cos}^{2}  θ - \text{sin}^{3}  θ$, by $\text{sin}  θ$

$\text{sin}  3 θ  \text{sin}  θ \equiv ( 3  \text{sin}  θ  \text{cos}^{2}  θ - \text{sin}^{3}  θ ) \text{sin}  θ$

Multiply out

$\equiv 3  \text{sin}^{2}  θ  \text{cos}^{2}  θ - \text{sin}^{4}  θ$

Both terms share a factor of $\text{sin}^{2}  θ$, so take it outside a bracket

$\equiv \text{sin}^{2}  θ  ( 3  \text{cos}^{2}  θ - \text{sin}^{2}  θ )$

Now form the quotient from the two results

$\frac{\text{cos}3θ-\text{cos}θ}{\text{sin}3θ\text{sin}θ} \equiv \frac{-4\text{sin}^{2}θ\text{cos}θ}{\text{sin}^{2}θ(3\text{cos}^{2}θ-\text{sin}^{2}θ)}$

Cancel the factor $\text{sin}^{2}  θ$, which is non-zero because $θ \neq k π$

$\equiv \frac{-4\text{cos}θ}{3\text{cos}^{2}θ-\text{sin}^{2}θ}$

**[M1]**

The answer is in cosine only, so replace $\text{sin}^{2}  θ$ using $\text{sin}^{2}  θ \equiv 1 - \text{cos}^{2}  θ$

$\equiv \frac{-4\text{cos}θ}{3\text{cos}^{2}θ-(1-\text{cos}^{2}θ)}$

Simplify the denominator

$\equiv \frac{-4\text{cos}θ}{4\text{cos}^{2}θ-1}$

**[A1]**

Multiply numerator and denominator by $- 1$ to match the printed form

$\frac{\text{cos}3θ-\text{cos}θ}{\text{sin}3θ\text{sin}θ} \equiv \frac{4\text{cos}θ}{1-4\text{cos}^{2}θ}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the compound angle formula on $\text{cos}  ( 2 θ + θ )$ with both double angle formulae substituted.
> 
> **A1**: Correct simplification of the numerator to $- 4  \text{sin}^{2}  θ  \text{cos}  θ$.
> 
> **M1**: Correct use of the part (a) result to factorise the denominator, followed by cancellation of $\text{sin}^{2}  θ$.
> 
> **A1**: Correct use of $\text{sin}^{2}  θ \equiv 1 - \text{cos}^{2}  θ$ to give a denominator in cosine only.
> 
> **A1**: Correct handling of the sign to reach the printed result, from full and correct working.
> 
> The form $\frac{-4\text{cos}θ}{4\text{cos}^{2}θ-1}$ is equivalent to the printed answer, but the final line must match the form given in the question. Because the result is given, the cancellation of $\text{sin}^{2}  θ$ must be visible. Any of the three forms of $\text{cos}  2 θ$ may be used, provided the working is carried through correctly; the $1 - 2  \text{sin}^{2}  θ$ form is simply the one that reaches the answer most directly.

### Q16
Expand the numerator using $\text{cos}  ( A + B ) \equiv \text{cos}  A  \text{cos}  B - \text{sin}  A  \text{sin}  B$, and the denominator using $\text{sin}  ( A - B ) \equiv \text{sin}  A  \text{cos}  B - \text{cos}  A  \text{sin}  B$

`\equiv \dfrac{\sqrt{2} \left( \text{cos} \; \theta \; \text{cos} \; \dfrac{\pi}{4} - \text{sin} \; \theta \; \text{sin} \; \dfrac{\pi}{4} \right)}{\text{sin} \; \theta \; \text{cos} \; \dfrac{\pi}{2} - \text{cos} \; \theta \; \text{sin} \; \dfrac{\pi}{2}}`

**[M1 A1]**

Substitute the exact values $\text{cos}  \frac{π}{4} = \text{sin}  \frac{π}{4} = \frac{\sqrt{2}}{2}$, $\text{cos}  \frac{π}{2} = 0$ and $\text{sin}  \frac{π}{2} = 1$

`\equiv \dfrac{\sqrt{2} \left( \dfrac{\sqrt{2}}{2} \; \text{cos} \; \theta - \dfrac{\sqrt{2}}{2} \; \text{sin} \; \theta \right)}{(0) \text{sin} \; \theta - (1) \text{cos} \; \theta}`

**[M1]**

Simplify each part, noting that $\sqrt{2} \times \frac{\sqrt{2}}{2} = 1$, and take the minus sign from the denominator into the numerator

$\equiv \frac{\text{cos}θ-\text{sin}θ}{-\text{cos}θ} \equiv \frac{\text{sin}θ-\text{cos}θ}{\text{cos}θ}$

Split into two terms and use the definition $\text{tan}  θ = \frac{\text{sin}θ}{\text{cos}θ}$

$\equiv \frac{\text{sin}θ}{\text{cos}θ} - 1 \equiv \text{tan}  θ - 1$

This is the required result

`\dfrac{\sqrt{2} \; \text{cos} \left( \theta + \dfrac{\pi}{4} \right)}{\text{sin} \left( \theta - \dfrac{\pi}{2} \right)} \equiv \text{tan} \; \theta - 1`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of a compound angle formula on the numerator or the denominator.
> 
> **A1**: Both expansions correct.
> 
> **M1**: Correct substitution of the exact values at $\frac{π}{4}$ and $\frac{π}{2}$.
> 
> **A1**: Correct simplification and split to reach the printed result, from full and correct working.
> 
> Accept $\frac{1}{\sqrt{2}}$ in place of $\frac{\sqrt{2}}{2}$. The denominator simplifies to $- \text{cos}  θ$, so mishandling that minus sign produces $1 - \text{tan}  θ$ and loses the final mark. Recognising `\text{sin} \left( \theta - \dfrac{\pi}{2} \right) \equiv - \text{cos} \; \theta` directly is equally acceptable.

### Q17
Expand the bracket using $\text{cos}  ( A - B ) \equiv \text{cos}  A  \text{cos}  B + \text{sin}  A  \text{sin}  B$, keeping the whole expansion squared

`4 \; \text{cos}^2 \left( x - \dfrac{\pi}{6} \right) \equiv 4 \left( \text{cos} \; x \; \text{cos} \; \dfrac{\pi}{6} + \text{sin} \; x \; \text{sin} \; \dfrac{\pi}{6} \right)^2`

**[M1]**

Substitute the exact values $\text{cos}  \frac{π}{6} = \frac{\sqrt{3}}{2}$ and $\text{sin}  \frac{π}{6} = \frac{1}{2}$

`\equiv 4 \left( \dfrac{\sqrt{3}}{2} \; \text{cos} \; x + \dfrac{1}{2} \; \text{sin} \; x \right)^2`

**[A1]**

Square the bracket

`\equiv 4 \left( \dfrac{3}{4} \; \text{cos}^2 \; x + \dfrac{\sqrt{3}}{2} \; \text{sin} \; x \; \text{cos} \; x + \dfrac{1}{4} \; \text{sin}^2 \; x \right)`

Multiply through by $4$

$\equiv 3  \text{cos}^{2}  x + 2 \sqrt{3}  \text{sin}  x  \text{cos}  x + \text{sin}^{2}  x$

**[M1]**

The middle term contains $2  \text{sin}  x  \text{cos}  x$, which is $\text{sin}  2 x$, and the answer is in sine only, so also use $\text{cos}^{2}  x \equiv 1 - \text{sin}^{2}  x$

$\equiv 3 ( 1 - \text{sin}^{2}  x ) + \text{sin}^{2}  x + \sqrt{3}  \text{sin}  2 x$

**[A1]**

Expand the bracket

$\equiv 3 - 3  \text{sin}^{2}  x + \text{sin}^{2}  x + \sqrt{3}  \text{sin}  2 x$

Collect the sine terms

`4 \; \text{cos}^2 \left( x - \dfrac{\pi}{6} \right) \equiv 3 - 2 \; \text{sin}^2 \; x + \sqrt{3} \; \text{sin} \; 2x`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the compound angle formula for $\text{cos}  ( A - B )$, with the expansion squared.
> 
> **A1**: Correct exact values of $\text{cos}  \frac{π}{6}$ and $\text{sin}  \frac{π}{6}$.
> 
> **M1**: Correct squaring of the bracket, including the cross term, and multiplication by $4$.
> 
> **A1**: Correct use of $\text{sin}  2 x \equiv 2  \text{sin}  x  \text{cos}  x$ and $\text{cos}^{2}  x \equiv 1 - \text{sin}^{2}  x$.
> 
> **A1**: Correct collection of terms to reach the printed result, from full and correct working.
> 
> Omitting the cross term when squaring is the most common error and loses the third mark onwards. Because the result is given, the expanded square must be seen before the collected answer.

### Q18
Split the argument into two angles so the addition formula applies

`\text{tan} \left( \dfrac{2x + \pi}{4} \right) \equiv \text{tan} \left( \dfrac{x}{2} + \dfrac{\pi}{4} \right)`

Apply $\text{tan}  ( A + B ) \equiv \frac{\text{tan}A+\text{tan}B}{1-\text{tan}A\text{tan}B}$

$\equiv \frac{\text{tan}\frac{x}{2}+\text{tan}\frac{π}{4}}{1-\text{tan}\frac{x}{2}\text{tan}\frac{π}{4}}$

**[M1]**

Use the exact value $\text{tan}  \frac{π}{4} = 1$

$\equiv \frac{1+\text{tan}\frac{x}{2}}{1-\text{tan}\frac{x}{2}}$

**[A1]**

Write the tangent in terms of sine and cosine

$\equiv \frac{1+\frac{\text{sin}\frac{x}{2}}{\text{cos}\frac{x}{2}}}{1-\frac{\text{sin}\frac{x}{2}}{\text{cos}\frac{x}{2}}}$

Clear the inner fractions by multiplying numerator and denominator through by $\text{cos}  \frac{x}{2}$

$\equiv \frac{\text{cos}\frac{x}{2}+\text{sin}\frac{x}{2}}{\text{cos}\frac{x}{2}-\text{sin}\frac{x}{2}}$

**[M1]**

Multiply numerator and denominator by $\text{cos}  \frac{x}{2} + \text{sin}  \frac{x}{2}$

`\equiv \dfrac{\left( \text{cos} \; \dfrac{x}{2} + \text{sin} \; \dfrac{x}{2} \right) \left( \text{cos} \; \dfrac{x}{2} + \text{sin} \; \dfrac{x}{2} \right)}{\left( \text{cos} \; \dfrac{x}{2} - \text{sin} \; \dfrac{x}{2} \right) \left( \text{cos} \; \dfrac{x}{2} + \text{sin} \; \dfrac{x}{2} \right)}`

Expand both, where the denominator is a difference of two squares

$\equiv \frac{\text{cos}^{2}\frac{x}{2}+\text{sin}^{2}\frac{x}{2}+2\text{sin}\frac{x}{2}\text{cos}\frac{x}{2}}{\text{cos}^{2}\frac{x}{2}-\text{sin}^{2}\frac{x}{2}}$

**[M1]**

Take the numerator one identity at a time. It opens with $\text{cos}^{2}  \frac{x}{2} + \text{sin}^{2}  \frac{x}{2}$, which is $1$ by the Pythagorean identity

$\equiv \frac{1+2\text{sin}\frac{x}{2}\text{cos}\frac{x}{2}}{\text{cos}^{2}\frac{x}{2}-\text{sin}^{2}\frac{x}{2}}$

The term left in the numerator is a double angle, since $\text{sin}  2 A \equiv 2  \text{sin}  A  \text{cos}  A$ with $A = \frac{x}{2}$

$\equiv \frac{1+\text{sin}x}{\text{cos}^{2}\frac{x}{2}-\text{sin}^{2}\frac{x}{2}}$

The denominator is a double angle too, since $\text{cos}  2 A \equiv \text{cos}^{2}  A - \text{sin}^{2}  A$ with $A = \frac{x}{2}$

$\equiv \frac{1+\text{sin}x}{\text{cos}x}$

**[A1]**

Split into two fractions and use the definitions of $\text{sec}  x$ and $\text{tan}  x$

$\equiv \frac{1}{\text{cos}x} + \frac{\text{sin}x}{\text{cos}x} \equiv \text{sec}  x + \text{tan}  x$

This is the required result

`\text{tan} \left( \dfrac{2x + \pi}{4} \right) \equiv \text{sec} \; x + \text{tan} \; x`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct splitting of the argument as $\frac{x}{2} + \frac{π}{4}$ with the tangent addition formula applied.
> 
> **A1**: Correct simplification to $\frac{1+\text{tan}\frac{x}{2}}{1-\text{tan}\frac{x}{2}}$ using $\text{tan}  \frac{π}{4} = 1$.
> 
> **M1**: Correct conversion to sine and cosine of $\frac{x}{2}$.
> 
> **M1**: Correct multiplication of numerator and denominator by $\text{cos}  \frac{x}{2} + \text{sin}  \frac{x}{2}$, with both products expanded.
> 
> **A1**: Correct use of the Pythagorean identity and both double angle formulae to give $\frac{1+\text{sin}x}{\text{cos}x}$.
> 
> **A1**: Correct split into $\text{sec}  x$ and $\text{tan}  x$ to reach the printed result, from full and correct working.
> 
> Because the result is given, the conjugate multiplication and the resulting expansion must both be visible. Working backwards from $\text{sec}  x + \text{tan}  x$ to the left-hand side earns the same marks.

### Q19
Start from the left-hand side and use $\text{cot}  2 θ = \frac{\text{cos}2θ}{\text{sin}2θ}$ and $\text{cosec}  2 θ = \frac{1}{\text{sin}2θ}$

$- 16  \text{cot}  2 θ  \text{cosec}^{3}  2 θ \equiv \frac{-16\text{cos}2θ}{\text{sin}^{4}2θ}$

**[M1]**

Expand both double angles, using $\text{cos}  2 θ \equiv \text{cos}^{2}  θ - \text{sin}^{2}  θ$ and $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$

$\equiv \frac{-16(\text{cos}^{2}θ-\text{sin}^{2}θ)}{(2\text{sin}θ\text{cos}θ)^{4}}$

**[M1]**

Raising the bracket to the fourth power gives $16  \text{sin}^{4}  θ  \text{cos}^{4}  θ$, so the $16$ cancels, and the minus sign reverses the numerator

$\equiv \frac{\text{sin}^{2}θ-\text{cos}^{2}θ}{\text{sin}^{4}θ\text{cos}^{4}θ}$

**[A1]**

The answer needs fourth powers, so multiply the numerator by $\text{sin}^{2}  θ + \text{cos}^{2}  θ$, which equals $1$ and so changes nothing

$\equiv \frac{(\text{sin}^{2}θ-\text{cos}^{2}θ)(\text{sin}^{2}θ+\text{cos}^{2}θ)}{\text{sin}^{4}θ\text{cos}^{4}θ}$

The numerator is now a difference of two squares, so expand it

$\equiv \frac{\text{sin}^{4}θ-\text{cos}^{4}θ}{\text{sin}^{4}θ\text{cos}^{4}θ}$

**[A1]**

Split into two fractions, cancelling in each, then use the definitions of $\text{sec}  θ$ and $\text{cosec}  θ$

$\equiv \frac{1}{\text{cos}^{4}θ} - \frac{1}{\text{sin}^{4}θ} \equiv \text{sec}^{4}  θ - \text{cosec}^{4}  θ$

This is the required result

$- 16  \text{cot}  2 θ  \text{cosec}^{3}  2 θ \equiv \text{sec}^{4}  θ - \text{cosec}^{4}  θ$

**[A1]**

> **[exam-tip]**
> Multiplying by $\text{sin}^{2}  θ + \text{cos}^{2}  θ$ looks like it achieves nothing, since that expression is just $1$. It is the key step. Whenever you have a difference of squares but need a difference of fourth powers, inserting the Pythagorean identity as the missing factor is what gets you there.

> **[mark-scheme]**
> **M1**: Correct use of the definitions of $\text{cot}  2 θ$ and $\text{cosec}  2 θ$ to give $\frac{-16\text{cos}2θ}{\text{sin}^{4}2θ}$.
> 
> **M1**: Correct use of both double angle formulae.
> 
> **A1**: Correct cancellation of the $16$ with correct handling of the sign.
> 
> **A1**: Correct use of $\text{sin}^{2}  θ + \text{cos}^{2}  θ \equiv 1$ to produce the numerator $\text{sin}^{4}  θ - \text{cos}^{4}  θ$.
> 
> **A1**: Correct splitting into two fractions and use of the reciprocal definitions to reach the printed result, from full and correct working.
> 
> Losing the minus sign when cancelling is the most common error and loses the third mark onwards. Because the result is given, the split into two fractions must be visible.

### Q20
The coefficients $\frac{\sqrt{3}}{2}$ and $\frac{1}{2}$ are the exact values of $\text{cos}  \frac{π}{6}$ and $\text{sin}  \frac{π}{6}$, so rewrite the first bracket with those in place

$\frac{\sqrt{3}}{2}  \text{cos}  θ - \frac{1}{2}  \text{sin}  θ \equiv \text{cos}  \frac{π}{6}  \text{cos}  θ - \text{sin}  \frac{π}{6}  \text{sin}  θ$

**[M1]**

This is the expansion of $\text{cos}  ( A + B )$ read backwards

`\equiv \text{cos} \left( \theta + \dfrac{\pi}{6} \right)`

**[A1]**

Treat the second bracket the same way

$\frac{\sqrt{3}}{2}  \text{sin}  θ + \frac{1}{2}  \text{cos}  θ \equiv \text{cos}  \frac{π}{6}  \text{sin}  θ + \text{sin}  \frac{π}{6}  \text{cos}  θ$

**[M1]**

This time it is the expansion of $\text{sin}  ( A + B )$

`\equiv \text{sin} \left( \theta + \dfrac{\pi}{6} \right)`

**[A1]**

Substitute both back into the original expression, restating the left hand side in full

`\dfrac{1}{\left( \dfrac{\sqrt{3}}{2} \; \text{cos} \; \theta - \dfrac{1}{2} \; \text{sin} \; \theta \right)^2} + \dfrac{1}{\left( \dfrac{\sqrt{3}}{2} \; \text{sin} \; \theta + \dfrac{1}{2} \; \text{cos} \; \theta \right)^2} \equiv \dfrac{1}{\text{cos}^2 \left( \theta + \dfrac{\pi}{6} \right)} + \dfrac{1}{\text{sin}^2 \left( \theta + \dfrac{\pi}{6} \right)}`

Combine over a common denominator

`\equiv \dfrac{\text{sin}^2 \left( \theta + \dfrac{\pi}{6} \right) + \text{cos}^2 \left( \theta + \dfrac{\pi}{6} \right)}{\text{cos}^2 \left( \theta + \dfrac{\pi}{6} \right) \text{sin}^2 \left( \theta + \dfrac{\pi}{6} \right)}`

**[M1]**

The numerator is $1$ by the Pythagorean identity, and the denominator is a single square

`\equiv \dfrac{1}{\left( \text{cos} \left( \theta + \dfrac{\pi}{6} \right) \text{sin} \left( \theta + \dfrac{\pi}{6} \right) \right)^2}`

**[A1]**

The product of a sine and cosine of the same angle is half the sine of the double angle, so use $\text{sin}  2 A \equiv 2  \text{sin}  A  \text{cos}  A$ with $A = θ + \frac{π}{6}$

`\equiv \dfrac{1}{\left( \dfrac{1}{2} \; \text{sin} \left( 2\theta + \dfrac{\pi}{3} \right) \right)^2}`

**[M1]**

Square the bracket, so the $\frac{1}{4}$ in the denominator becomes a factor of $4$

`\equiv \dfrac{4}{\text{sin}^2 \left( 2\theta + \dfrac{\pi}{3} \right)}`

**[A1]**

Use the definition $\text{cosec}  A = \frac{1}{\text{sin}A}$

`\equiv 4 \; \text{cosec}^2 \left( 2\theta + \dfrac{\pi}{3} \right)`

This is the required result

`\dfrac{1}{\left( \dfrac{\sqrt{3}}{2} \; \text{cos} \; \theta - \dfrac{1}{2} \; \text{sin} \; \theta \right)^2} + \dfrac{1}{\left( \dfrac{\sqrt{3}}{2} \; \text{sin} \; \theta + \dfrac{1}{2} \; \text{cos} \; \theta \right)^2} \equiv 4 \; \text{cosec}^2 \left( 2\theta + \dfrac{\pi}{3} \right)`

**[A1]**

> **[exam-tip]**
> Seeing $\frac{\sqrt{3}}{2}$ and $\frac{1}{2}$ sitting next to a sine and a cosine should make you think of the compound angle formulae running backwards. Exact values of common angles turning up as coefficients is nearly always the setter telling you to compress two terms into one.

> **[mark-scheme]**
> **M1**: Correct identification of $\frac{\sqrt{3}}{2}$ and $\frac{1}{2}$ as $\text{cos}  \frac{π}{6}$ and $\text{sin}  \frac{π}{6}$ in the first bracket.
> 
> **A1**: First bracket correctly written as `\text{cos} \left( \theta + \dfrac{\pi}{6} \right)`.
> 
> **M1**: The same identification applied to the second bracket.
> 
> **A1**: Second bracket correctly written as `\text{sin} \left( \theta + \dfrac{\pi}{6} \right)`.
> 
> **M1**: Correct combination of the two fractions over a common denominator.
> 
> **A1**: Correct use of the Pythagorean identity to reduce the numerator to $1$.
> 
> **M1**: Correct use of $\text{sin}  2 A \equiv 2  \text{sin}  A  \text{cos}  A$ with $A = θ + \frac{π}{6}$.
> 
> **A1**: Correct squaring to give `\dfrac{4}{\text{sin}^2 \left( 2\theta + \dfrac{\pi}{3} \right)}`.
> 
> **A1**: Correct use of the definition of $\text{cosec}$ to reach the printed result, from full and correct working.
> 
> Writing each bracket in the R form, as `\text{cos} \left( \theta + \dfrac{\pi}{6} \right)` and `\text{sin} \left( \theta + \dfrac{\pi}{6} \right)` found by comparing coefficients, is equally acceptable and earns the first four marks. Because the result is given, the combined fraction and the double angle step must both be visible.

### Q21
The denominator is the only term in $2 θ$, so rewrite it using $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$

$\frac{4\text{sin}^{4}θ}{\text{sin}^{2}2θ} \equiv \frac{4\text{sin}^{4}θ}{(2\text{sin}θ\text{cos}θ)^{2}}$

**[M1]**

Square out the denominator

$\equiv \frac{4\text{sin}^{4}θ}{4\text{sin}^{2}θ\text{cos}^{2}θ}$

Cancel the factor of $4$ and two factors of $\text{sin}  θ$, which are non-zero because $θ \neq k π$

$\equiv \frac{\text{sin}^{2}θ}{\text{cos}^{2}θ}$

**[A1]**

Use the definition $\text{tan}  θ = \frac{\text{sin}θ}{\text{cos}θ}$

`\equiv \left( \dfrac{\text{sin} \; \theta}{\text{cos} \; \theta} \right)^2 \equiv \text{tan}^2 \; \theta`

This is the required result

$\frac{4\text{sin}^{4}θ}{\text{sin}^{2}2θ} \equiv \text{tan}^{2}  θ$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$ in the denominator, including squaring the whole expression.
> 
> **A1**: Correct cancellation to $\frac{\text{sin}^{2}θ}{\text{cos}^{2}θ}$.
> 
> **A1**: Correct use of the definition of $\text{tan}  θ$ to reach the printed result, from full and correct working.
> 
> A common error is squaring only part of the denominator, giving $2  \text{sin}^{2}  θ  \text{cos}^{2}  θ$, which loses the first mark. Reference to the condition on $θ$ is not required.

### Q22
Expand the bracket using $\text{sin}  ( A - B ) \equiv \text{sin}  A  \text{cos}  B - \text{cos}  A  \text{sin}  B$ with $A = θ$ and $B = \frac{π}{4}$

`\sqrt{2} \; \text{sin} \left( \theta - \dfrac{\pi}{4} \right) \equiv \sqrt{2} \left( \text{sin} \; \theta \; \text{cos} \; \dfrac{\pi}{4} - \text{cos} \; \theta \; \text{sin} \; \dfrac{\pi}{4} \right)`

**[M1]**

Use the exact values $\text{cos}  \frac{π}{4} = \text{sin}  \frac{π}{4} = \frac{\sqrt{2}}{2}$

`\equiv \sqrt{2} \left( \dfrac{\sqrt{2}}{2} \; \text{sin} \; \theta - \dfrac{\sqrt{2}}{2} \; \text{cos} \; \theta \right)`

**[A1]**

Multiply through by $\sqrt{2}$, noting that $\sqrt{2} \times \frac{\sqrt{2}}{2} = 1$

$\equiv \text{sin}  θ - \text{cos}  θ$

This is the required result

`\sqrt{2} \; \text{sin} \left( \theta - \dfrac{\pi}{4} \right) \equiv \text{sin} \; \theta - \text{cos} \; \theta`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the compound angle formula for $\text{sin}  ( A - B )$ with $B = \frac{π}{4}$.
> 
> **A1**: Correct use of the exact values of $\text{cos}  \frac{π}{4}$ and $\text{sin}  \frac{π}{4}$.
> 
> **A1**: Correct simplification to reach the printed result, from full and correct working.
> 
> Accept $\frac{1}{\sqrt{2}}$ in place of $\frac{\sqrt{2}}{2}$. Because the result is given, the substituted form must be seen before the final line; a sign error in the expansion loses the last two marks.

### Q23
The numerator contains $\text{cos}  2 x$, so expand $\text{sin}  4 x$ as a double angle in $2 x$

$\text{sin}  4 x \equiv 2  \text{sin}  2 x  \text{cos}  2 x$

**[M1]**

Substitute this into the denominator and cancel the common factor $\text{cos}  2 x$

$\frac{4\text{cot}x\text{cos}2x}{2\text{sin}2x\text{cos}2x} \equiv \frac{2\text{cot}x}{\text{sin}2x}$

**[A1]**

Now expand the remaining double angle with $\text{sin}  2 x \equiv 2  \text{sin}  x  \text{cos}  x$, and use $\text{cot}  x = \frac{\text{cos}x}{\text{sin}x}$

`\equiv \dfrac{2 \left( \dfrac{\text{cos} \; x}{\text{sin} \; x} \right)}{2 \; \text{sin} \; x \; \text{cos} \; x}`

**[M1]**

Cancel the factor of $2$ and the factor $\text{cos}  x$

$\equiv \frac{1}{\text{sin}^{2}x}$

**[A1]**

Use the definition $\text{cosec}  x = \frac{1}{\text{sin}x}$

`\equiv \left( \dfrac{1}{\text{sin} \; x} \right)^2 \equiv \text{cosec}^2 \; x`

This is the required result

$\frac{4\text{cot}x\text{cos}2x}{\text{sin}4x} \equiv \text{cosec}^{2}  x$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $\text{sin}  4 x \equiv 2  \text{sin}  2 x  \text{cos}  2 x$.
> 
> **A1**: Correct cancellation of $\text{cos}  2 x$ to give $\frac{2\text{cot}x}{\text{sin}2x}$.
> 
> **M1**: Correct use of $\text{sin}  2 x \equiv 2  \text{sin}  x  \text{cos}  x$ together with the definition of $\text{cot}  x$.
> 
> **A1**: Correct simplification to $\frac{1}{\text{sin}^{2}x}$.
> 
> **A1**: Correct use of the definition of $\text{cosec}  x$ to reach the printed result, from full and correct working.
> 
> Converting everything to sine and cosine at the start reaches the same result and earns the same marks. Because the result is given, the cancellations must be visible.

### Q24
Only the first term needs expanding, so split $3 θ$ into $2 θ + θ$ and apply $\text{sin}  ( A + B ) \equiv \text{sin}  A  \text{cos}  B + \text{cos}  A  \text{sin}  B$ to it

$\text{sin}  3 θ + \text{sin}  θ \equiv \text{sin}  2 θ  \text{cos}  θ + \text{cos}  2 θ  \text{sin}  θ + \text{sin}  θ$

**[M1 A1]**

Replace both double angles, using $\text{sin}  2 θ \equiv 2  \text{sin}  θ  \text{cos}  θ$ and $\text{cos}  2 θ \equiv 2  \text{cos}^{2}  θ - 1$

$\equiv ( 2  \text{sin}  θ  \text{cos}  θ ) \text{cos}  θ + ( 2  \text{cos}^{2}  θ - 1 ) \text{sin}  θ + \text{sin}  θ$

**[M1]**

Multiply out both products

$\equiv 2  \text{sin}  θ  \text{cos}^{2}  θ + 2  \text{sin}  θ  \text{cos}^{2}  θ - \text{sin}  θ + \text{sin}  θ$

The two single sine terms cancel, leaving the matching terms to collect

$\equiv 4  \text{sin}  θ  \text{cos}^{2}  θ$

**[A1]**

Write the result in sine only, using $\text{cos}^{2}  θ \equiv 1 - \text{sin}^{2}  θ$

$\equiv 4  \text{sin}  θ  ( 1 - \text{sin}^{2}  θ )$

Expand the bracket

$\text{sin}  3 θ + \text{sin}  θ \equiv 4  \text{sin}  θ - 4  \text{sin}^{3}  θ$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the compound angle formula on $\text{sin}  ( 2 θ + θ )$.
> 
> **A1**: Correct expansion, with the $+  \text{sin}  θ$ term retained.
> 
> **M1**: Correct use of both double angle formulae.
> 
> **A1**: Correct simplification to $4  \text{sin}  θ  \text{cos}^{2}  θ$, the two single sine terms having cancelled.
> 
> **A1**: Correct use of $\text{cos}^{2}  θ \equiv 1 - \text{sin}^{2}  θ$ and expansion to reach the printed result, from full and correct working.
> 
> Any of the three forms of the double angle formula for cosine may be used, provided every term is converted to sine before the final line. Deriving $\text{sin}  3 θ \equiv 3  \text{sin}  θ - 4  \text{sin}^{3}  θ$ separately and then adding $\text{sin}  θ$ earns the same marks. Because the result is given, the expanded form must be seen before the collected one.

### Q25
Start from the left-hand side and use the definition $\text{cosec}  θ = \frac{1}{\text{sin}θ}$

`\text{sin} \; \theta \; (\text{cosec}^2 \; \theta - 2) \equiv \text{sin} \; \theta \left( \dfrac{1}{\text{sin}^2 \; \theta} - 2 \right)`

**[M1]**

Multiply out the bracket

$\equiv \frac{1}{\text{sin}θ} - 2  \text{sin}  θ$

**[A1]**

Combine the two terms over the common denominator $\text{sin}  θ$

$\equiv \frac{1-2\text{sin}^{2}θ}{\text{sin}θ}$

**[M1]**

Use the double angle formula in the form $\text{cos}  2 θ \equiv 1 - 2  \text{sin}^{2}  θ$ on the numerator

$\equiv \frac{\text{cos}2θ}{\text{sin}θ}$

This is the required result

$\text{sin}  θ  ( \text{cosec}^{2}  θ - 2 ) \equiv \frac{\text{cos}2θ}{\text{sin}θ}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of $\text{cosec}^{2}  θ \equiv \frac{1}{\text{sin}^{2}θ}$.
> 
> **A1**: Correct expansion to $\frac{1}{\text{sin}θ} - 2  \text{sin}  θ$.
> 
> **M1**: Correct combination into a single fraction with denominator $\text{sin}  θ$.
> 
> **A1**: Correct use of $\text{cos}  2 θ \equiv 1 - 2  \text{sin}^{2}  θ$ to reach the printed result, from full and correct working.
> 
> Starting from the right-hand side and working towards the left earns the same marks, with the double angle formula applied first and the single fraction split into two terms. Because the result is given, the form $\frac{1-2\text{sin}^{2}θ}{\text{sin}θ}$ must be seen.

### Q26
Write $4 θ$ as double the angle $2 θ$

$\text{cos}  4 θ \equiv \text{cos}  ( 2 \times 2 θ )$

Apply $\text{cos}  2 A \equiv 2  \text{cos}^{2}  A - 1$ with $A = 2 θ$, choosing the form in cosine only

$\equiv 2  \text{cos}^{2}  2 θ - 1$

**[B1]**

Apply the same formula again with $A = θ$

$\equiv 2 ( 2  \text{cos}^{2}  θ - 1 )^{2} - 1$

**[B1]**

Expand the square inside the bracket

$\equiv 2 ( 4  \text{cos}^{4}  θ - 4  \text{cos}^{2}  θ + 1 ) - 1$

**[B1]**

Multiply out the bracket

$\equiv 8  \text{cos}^{4}  θ - 8  \text{cos}^{2}  θ + 2 - 1$

Collect the constants

$\text{cos}  4 θ \equiv 8  \text{cos}^{4}  θ - 8  \text{cos}^{2}  θ + 1$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct expression of $\text{cos}  4 θ$ in terms of $\text{cos}  2 θ$.
> 
> **B1**: Correct expression of $\text{cos}  2 θ$ in terms of $\text{cos}  θ$. This may be seen anywhere in the working.
> 
> **B1**: Correct expansion to an expression in $\text{cos}  θ$.
> 
> **B1**: Correct reduction to the printed result, from full and correct working.
> 
> Any of the three forms of the double angle formula may be used, provided the sine terms are converted to cosine before the final line. Because the result is given, the expanded form must be seen before the collected one.

### Q27
(i)

The target involves $\text{sec}  θ$ and $\text{tan}  θ$, both of which have $\text{cos}  θ$ in the denominator, so divide the given identity through by $\text{cos}^{2}  θ$

$\frac{\text{sin}^{2}θ+\text{cos}^{2}θ}{\text{cos}^{2}θ} \equiv \frac{1}{\text{cos}^{2}θ}$

**[M1]**

Split the left-hand side into separate terms

`\left( \dfrac{\text{sin} \; \theta}{\text{cos} \; \theta} \right)^2 + 1 \equiv \left( \dfrac{1}{\text{cos} \; \theta} \right)^2`

Use the definitions $\text{tan}  θ = \frac{\text{sin}θ}{\text{cos}θ}$ and $\text{sec}  θ = \frac{1}{\text{cos}θ}$

$\equiv 1 + \text{tan}^{2}  θ$

This is the required result

$\text{sec}^{2}  θ \equiv 1 + \text{tan}^{2}  θ$

**[A1]**

(ii)

This time the target involves $\text{cosec}  θ$ and $\text{cot}  θ$, which have $\text{sin}  θ$ in the denominator, so divide through by $\text{sin}^{2}  θ$ instead

$\frac{\text{sin}^{2}θ+\text{cos}^{2}θ}{\text{sin}^{2}θ} \equiv \frac{1}{\text{sin}^{2}θ}$

**[M1]**

Split the left-hand side into separate terms

`1 + \left( \dfrac{\text{cos} \; \theta}{\text{sin} \; \theta} \right)^2 \equiv \left( \dfrac{1}{\text{sin} \; \theta} \right)^2`

Use the definitions $\text{cot}  θ = \frac{\text{cos}θ}{\text{sin}θ}$ and $\text{cosec}  θ = \frac{1}{\text{sin}θ}$

$\equiv 1 + \text{cot}^{2}  θ$

This is the required result

$\text{cosec}^{2}  θ \equiv 1 + \text{cot}^{2}  θ$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct division of the given identity by $\text{cos}^{2}  θ$.
> 
> **A1**: Correct use of the definitions of $\text{tan}  θ$ and $\text{sec}  θ$ to reach the first printed result.
> 
> **M1**: Correct division of the given identity by $\text{sin}^{2}  θ$.
> 
> **A1**: Correct use of the definitions of $\text{cot}  θ$ and $\text{cosec}  θ$ to reach the second printed result.
> 
> Both results are given, so the divided form must be seen in each case. Working from the printed result back to $\text{sin}^{2}  θ + \text{cos}^{2}  θ \equiv 1$ is equally acceptable.
