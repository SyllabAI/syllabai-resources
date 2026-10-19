# Mark Schemes — Further Differentiation
**Differentiation** · Cambridge (CIE) A-LEVEL maths (9709)


## Exam Questions (35 questions)


### Q1
(i)

Differentiate each term using its standard derivative

`\dfrac{\text{d}}{\text{d}x}\left(\text{tan} \; x + \text{ln} \; x\right)`

$= \text{sec}^{2}  x + \frac{1}{x}$

**[B1 B1]**

(ii)

Apply the product rule, `\dfrac{\text{d}}{\text{d}x}\left(uv\right) = u\dfrac{\text{d}v}{\text{d}x} + v\dfrac{\text{d}u}{\text{d}x}`

$u = \text{e}^{x} ,  v = \text{cos}  x$

$\frac{\text{d}u}{\text{d}x} = \text{e}^{x} ,  \frac{\text{d}v}{\text{d}x} = - \text{sin}  x$

Substitute these into the product rule

`\dfrac{\text{d}y}{\text{d}x} = \text{e}^{x}\left(-\text{sin} \; x\right) + \text{cos} \; x \cdot \text{e}^{x}`

**[M1]**

Factor out $\text{e}^{x}$

`\dfrac{\text{d}y}{\text{d}x} = \text{e}^{x}\left(\text{cos} \; x - \text{sin} \; x\right)`

**[A1]**

(iii)

Apply the quotient rule, `\dfrac{\text{d}}{\text{d}x}\left(\dfrac{u}{v}\right) = \dfrac{v\dfrac{\text{d}u}{\text{d}x} - u\dfrac{\text{d}v}{\text{d}x}}{v^{2}}`

$u = \text{sin}  x ,  v = x$

$\frac{\text{d}u}{\text{d}x} = \text{cos}  x ,  \frac{\text{d}v}{\text{d}x} = 1$

Substitute these into the quotient rule

$\frac{\text{d}y}{\text{d}x} = \frac{x\text{cos}x-\text{sin}x}{x^{2}}$

**[M1 A1]**

(iv)

Apply the chain rule, $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$, with $u = x^{2} - 3 x + 17$

$u = x^{2} - 3 x + 17 ,  y = \text{e}^{u}$

$\frac{\text{d}u}{\text{d}x} = 2 x - 3 ,  \frac{\text{d}y}{\text{d}u} = \text{e}^{u}$

Substitute these into the chain rule

`\dfrac{\text{d}y}{\text{d}x} = \text{e}^{u}\left(2x - 3\right)`

**[M1]**

Substitute $u = x^{2} - 3 x + 17$ back in

`\dfrac{\text{d}y}{\text{d}x} = \left(2x - 3\right)\text{e}^{x^{2} - 3x + 17}`

**[A1]**

> **[exam-tip]**
> The derivatives of $\text{tan}  x$, $\text{ln}  x$, $\text{e}^{x}$, $\text{sin}  x$ and $\text{cos}  x$, together with the product and quotient rules, are all given to you in the List of Formulae. The chain rule is not listed there, so it is the one tool in this question you must have memorised.

> **[mark-scheme]**
> **B1**: For $\text{sec}^{2}  x$ as the derivative of $\text{tan}  x$.
> 
> **B1**: For $\frac{1}{x}$ as the derivative of $\text{ln}  x$.
> 
> **M1**: Correct use of the product rule in part (ii), with $u = \text{e}^{x}$ and $v = \text{cos}  x$ and both derivatives correct.
> 
> **A1**: For `\text{e}^{x}\left(\text{cos} \; x - \text{sin} \; x\right)`, or the unfactored equivalent.
> 
> **M1**: Correct use of the quotient rule in part (iii), with $u = \text{sin}  x$ and $v = x$ and both derivatives correct.
> 
> **A1**: For $\frac{x\text{cos}x-\text{sin}x}{x^{2}}$.
> 
> **M1**: Correct use of the chain rule in part (iv), differentiating $\text{e}^{u}$ and multiplying by $\frac{\text{d}u}{\text{d}x} = 2 x - 3$.
> 
> **A1**: For `\left(2x - 3\right)\text{e}^{x^{2} - 3x + 17}`.

### Q2
Apply the product rule, $\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$

$u = x^{3} - 2 x ,  v = \text{ln}  x$

$\frac{\text{d}u}{\text{d}x} = 3 x^{2} - 2 ,  \frac{\text{d}v}{\text{d}x} = \frac{1}{x}$

Substitute these into the product rule

`\dfrac{\text{d}y}{\text{d}x} = \left(x^{3} - 2x\right)\dfrac{1}{x} + \text{ln} \; x\left(3x^{2} - 2\right)`

**[M1 A1]**

Simplify the first term, since $\frac{x^{3}-2x}{x} = x^{2} - 2$

`\dfrac{\text{d}y}{\text{d}x} = x^{2} - 2 + \left(3x^{2} - 2\right)\text{ln} \; x`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the product rule in part (a), with $u = x^{3} - 2 x$ and $v = \text{ln}  x$ and both derivatives correct.
> 
> **A1**: For a fully correct unsimplified derivative, `\left(x^{3} - 2x\right)\dfrac{1}{x} + \left(3x^{2} - 2\right)\text{ln} \; x`.
> 
> **A1**: For the simplified form `x^{2} - 2 + \left(3x^{2} - 2\right)\text{ln} \; x`.
Apply the product rule, $\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$, differentiating $v = \text{cos}  2 x$ by the chain rule

$u = \text{e}^{x} ,  v = \text{cos}  2 x$

$\frac{\text{d}u}{\text{d}x} = \text{e}^{x} ,  \frac{\text{d}v}{\text{d}x} = - 2 \text{sin}  2 x$

Substitute these into the product rule

`\dfrac{\text{d}y}{\text{d}x} = \text{e}^{x}\left(-2\text{sin} \; 2x\right) + \text{cos} \; 2x \cdot \text{e}^{x}`

**[M1 A1]**

Factor out $\text{e}^{x}$

`\dfrac{\text{d}y}{\text{d}x} = \text{e}^{x}\left(\text{cos} \; 2x - 2\text{sin} \; 2x\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the product rule in part (b), with $u = \text{e}^{x}$ and $v = \text{cos}  2 x$.
> 
> **A1**: For both derivatives correct, including $\frac{\text{d}}{\text{d}x} \text{cos}  2 x = - 2 \text{sin}  2 x$ from the chain rule.
> 
> **A1**: For `\text{e}^{x}\left(\text{cos} \; 2x - 2\text{sin} \; 2x\right)`, or the unfactored equivalent.

### Q3
(i)

Use the standard result $\frac{\text{d}}{\text{d}x} \text{sec}  x = \text{sec}  x  \text{tan}  x$, with the chain-rule factor $5$ from the $5 x$

$\frac{\text{d}y}{\text{d}x} = 5 \text{sec}  5 x  \text{tan}  5 x$

**[B1]**

(ii)

Use the standard result $\frac{\text{d}}{\text{d}x} \text{cosec}  x = - \text{cosec}  x  \text{cot}  x$, with the chain-rule factor $3$ from the $3 x$

$\frac{\text{d}y}{\text{d}x} = - 3 \text{cosec}  3 x  \text{cot}  3 x$

**[B1]**

> **[mark-scheme]**
> **B1**: For $5 \text{sec}  5 x  \text{tan}  5 x$.
> 
> **B1**: For $- 3 \text{cosec}  3 x  \text{cot}  3 x$.

### Q4
Apply the chain rule, $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$, with $u = a x$ so that $y = \text{tan}^{-1} u$

$y = \text{tan}^{-1} u ,  \frac{\text{d}y}{\text{d}u} = \frac{1}{1+u^{2}}$

$u = a x ,  \frac{\text{d}u}{\text{d}x} = a$

Substitute these into the chain rule

$\frac{\text{d}y}{\text{d}x} = \frac{1}{1+u^{2}} \times a = \frac{a}{1+(ax)^{2}}$

**[M1]**

Expand $( a x )^{2} = a^{2} x^{2}$

$\frac{\text{d}y}{\text{d}x} = \frac{a}{1+a^{2}x^{2}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the chain rule with $u = a x$, multiplying the given derivative $\frac{1}{1+u^{2}}$ by $\frac{\text{d}u}{\text{d}x} = a$.
> 
> **A1**: Reaches the given result $\frac{a}{1+a^{2}x^{2}}$, showing $( a x )^{2} = a^{2} x^{2}$. Because the answer is given, the working must be visible.
A gradient of $1$ means $\frac{\text{d}y}{\text{d}x} = 1$. From part (a) with $a = 2$, the derivative of $\text{tan}^{-1} ( 2 x )$ is $\frac{2}{1+4x^{2}}$, so set this equal to $1$

$\frac{2}{1+4x^{2}} = 1$

Solve for $x$

$2 = 1 + 4 x^{2} \Rightarrow 4 x^{2} = 1 \Rightarrow x^{2} = \frac{1}{4}$

$x = \pm \frac{1}{2}$

**[M1 A1]**

Find the $y$-coordinate at each $x$, using the exact values $\text{tan}^{-1} ( 1 ) = \frac{π}{4}$ and $\text{tan}^{-1} ( - 1 ) = - \frac{π}{4}$

$x = \frac{1}{2} :  y = \text{tan}^{-1} ( 1 ) = \frac{π}{4}$

$x = - \frac{1}{2} :  y = \text{tan}^{-1} ( - 1 ) = - \frac{π}{4}$

**Final answer:** `\left(\dfrac{1}{2}, \dfrac{\pi}{4}\right)`** and **`\left(-\dfrac{1}{2}, -\dfrac{\pi}{4}\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Sets their derivative from part (a), with $a = 2$, equal to $1$ and solves for $x$.
> 
> **A1**: For $x = \pm \frac{1}{2}$ (both values).
> 
> **A1**: For both points `\left(\dfrac{1}{2}, \dfrac{\pi}{4}\right)` and `\left(-\dfrac{1}{2}, -\dfrac{\pi}{4}\right)`, with exact $y$-values. Accept $y = \text{tan}^{-1} ( \pm 1 )$ evaluated to $\pm \frac{π}{4}$.

### Q5
Apply the quotient rule, $\frac{\text{d}y}{\text{d}x} = \frac{v\frac{\text{d}u}{\text{d}x}-u\frac{\text{d}v}{\text{d}x}}{v^{2}}$

$u = \text{cos}  x ,  v = \text{sin}  x$

$\frac{\text{d}u}{\text{d}x} = - \text{sin}  x ,  \frac{\text{d}v}{\text{d}x} = \text{cos}  x$

Substitute these into the quotient rule

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{sin} \; x\left(-\text{sin} \; x\right) - \text{cos} \; x\;\text{cos} \; x}{\text{sin}^{2} \; x} = \dfrac{-\text{sin}^{2} \; x - \text{cos}^{2} \; x}{\text{sin}^{2} \; x}`

**[M1 A1]**

Factor out $- 1$ and use $\text{sin}^{2}  x + \text{cos}^{2}  x = 1$

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{-\left(\text{sin}^{2} \; x + \text{cos}^{2} \; x\right)}{\text{sin}^{2} \; x} = \dfrac{-1}{\text{sin}^{2} \; x}`

$\frac{\text{d}y}{\text{d}x} = - \text{cosec}^{2}  x$

**[A1]**

> **[exam-tip]**
> In part (a), $\frac{\text{cos}x}{\text{sin}x}$ is just $\text{cot}  x$, and the derivative $\frac{\text{d}}{\text{d}x} \text{cot}  x = - \text{cosec}^{2}  x$ is given in the List of Formulae, so you can write the answer down in one line. The quotient rule is the safe fallback if you do not spot this, or if a question tells you to use it.

> **[mark-scheme]**
> **M1**: Correct use of the quotient rule in part (a), with $u = \text{cos}  x$, $v = \text{sin}  x$ and both derivatives correct.
> 
> **A1**: For the unsimplified derivative $\frac{-\text{sin}^{2}x-\text{cos}^{2}x}{\text{sin}^{2}x}$.
> 
> **A1**: For $- \text{cosec}^{2}  x$, reached using $\text{sin}^{2}  x + \text{cos}^{2}  x = 1$. Accept $\text{cot}  x$ differentiated directly.
Apply the quotient rule, $\frac{\text{d}y}{\text{d}x} = \frac{v\frac{\text{d}u}{\text{d}x}-u\frac{\text{d}v}{\text{d}x}}{v^{2}}$, differentiating $v = \text{sin}  3 x$ by the chain rule

$u = 2 x^{2} - 3 x + 4 ,  v = \text{sin}  3 x$

$\frac{\text{d}u}{\text{d}x} = 4 x - 3 ,  \frac{\text{d}v}{\text{d}x} = 3 \text{cos}  3 x$

Substitute these into the quotient rule

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{\left(4x - 3\right)\text{sin} \; 3x - 3\left(2x^{2} - 3x + 4\right)\text{cos} \; 3x}{\text{sin}^{2} \; 3x}`

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Correct use of the quotient rule in part (b), with $u = 2 x^{2} - 3 x + 4$ and $v = \text{sin}  3 x$.
> 
> **A1**: For both derivatives correct, including $\frac{\text{d}v}{\text{d}x} = 3 \text{cos}  3 x$ from the chain rule.
> 
> **A1**: For the fully correct expression. There is no need to simplify further.

### Q6
(i)

Apply the chain rule, $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$, with $u = 3 x^{2}$

$y = \text{sin}  u ,  \frac{\text{d}y}{\text{d}u} = \text{cos}  u$

$u = 3 x^{2} ,  \frac{\text{d}u}{\text{d}x} = 6 x$

Substitute these into the chain rule

`\dfrac{\text{d}y}{\text{d}x} = \text{cos}\left(3x^{2}\right) \times 6x`

**[M1]**

`\dfrac{\text{d}y}{\text{d}x} = 6x\;\text{cos}\left(3x^{2}\right)`

**[A1]**

(ii)

Apply the chain rule, $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$, with $u = x^{3}$

$y = 2  \text{ln}  u ,  \frac{\text{d}y}{\text{d}u} = \frac{2}{u}$

$u = x^{3} ,  \frac{\text{d}u}{\text{d}x} = 3 x^{2}$

Substitute these in, then simplify

$\frac{\text{d}y}{\text{d}x} = \frac{2}{x^{3}} \times 3 x^{2} = \frac{6x^{2}}{x^{3}}$

**[M1]**

$\frac{\text{d}y}{\text{d}x} = \frac{6}{x}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the chain rule in part (i): `\text{cos}\left(3x^{2}\right)` multiplied by the derivative of the inner function $6 x$.
> 
> **A1**: For `6x\;\text{cos}\left(3x^{2}\right)`, or equivalent.
> 
> **M1**: Correct use of the chain rule in part (ii): $\frac{2}{x^{3}}$ multiplied by $3 x^{2}$ (or equivalently differentiating $6  \text{ln}  x$).
> 
> **A1**: For $\frac{6}{x}$. Accept $6 x^{-1}$.

### Q7
(i)

Apply the chain rule, $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$, with $u = x^{2} - 9$

$y = \text{e}^{u} ,  \frac{\text{d}y}{\text{d}u} = \text{e}^{u}$

$u = x^{2} - 9 ,  \frac{\text{d}u}{\text{d}x} = 2 x$

Substitute these into the chain rule

$\frac{\text{d}y}{\text{d}x} = \text{e}^{x^{2}-9} \times 2 x$

**[M1]**

$\frac{\text{d}y}{\text{d}x} = 2 x  \text{e}^{x^{2}-9}$

**[A1]**

(ii)

Find the gradient of the tangent by substituting $x = - 3$ into $\frac{\text{d}y}{\text{d}x}$

$\frac{\text{d}y}{\text{d}x} = 2 ( - 3 )  \text{e}^{(-3)^{2}-9} = - 6 \text{e}^{0} = - 6$

**[M1]**

Use the point-gradient form $y - y_{1} = m ( x - x_{1} )$ with $m = - 6$ and $( x_{1} , y_{1} ) = ( - 3 , 1 )$

$y - 1 = - 6 ( x + 3 )$

$y = - 6 x - 17$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the chain rule in part (i), giving a result of the form $k x  \text{e}^{x^{2}-9}$.
> 
> **A1**: For $\frac{\text{d}y}{\text{d}x} = 2 x  \text{e}^{x^{2}-9}$.
> 
> **M1**: Substitutes $x = - 3$ into their $\frac{\text{d}y}{\text{d}x}$ to find the tangent gradient, using $\text{e}^{0} = 1$ to reach $- 6$.
> 
> **A1**: For the tangent equation $y = - 6 x - 17$, or any correct equivalent (for example $6 x + y + 17 = 0$).

### Q8
On the $x$-axis $y = 0$, so set $\text{f} ( x ) = 0$

`\left(x^{2} - 4x + 4\right)\text{ln} \; x = 0`

**[B1]**

A product is zero when one of its factors is zero, so $x^{2} - 4 x + 4 = 0$ or $\text{ln}  x = 0$

**[M1]**

Factorise the quadratic, since $x^{2} - 4 x + 4 = ( x - 2 )^{2}$, and solve

$( x - 2 )^{2} = 0 \Rightarrow x = 2$

so the graph meets the $x$-axis at

$( 2 , 0 )$

**[A1]**

Solve the other factor, using $\text{ln}  1 = 0$

$\text{ln}  x = 0 \Rightarrow x = 1$

so the graph meets the $x$-axis at

$( 1 , 0 )$

**[A1]**

> **[mark-scheme]**
> **B1**: States that $y = 0$ on the $x$-axis and forms `\left(x^{2} - 4x + 4\right)\text{ln} \; x = 0`.
> 
> **M1**: Sets each factor to zero: $x^{2} - 4 x + 4 = 0$ or $\text{ln}  x = 0$.
> 
> **A1**: Solves $( x - 2 )^{2} = 0$ to reach $x = 2$, giving $( 2 , 0 )$.
> 
> **A1**: Solves $\text{ln}  x = 0$ to reach $x = 1$, giving $( 1 , 0 )$. Because the points are given, both routes to zero must be shown.
Notice that $x^{2} - 4 x + 4 = ( x - 2 )^{2}$, then apply the product rule with $u = ( x - 2 )^{2}$ and $v = \text{ln}  x$

$\frac{\text{d}u}{\text{d}x} = 2 ( x - 2 ) ,  \frac{\text{d}v}{\text{d}x} = \frac{1}{x}$

**[B1 B1]**

Substitute into the product rule $\text{f} ' ( x ) = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$

`\text{f}'(x) = (x-2)^{2}\cdot\dfrac{1}{x} + \text{ln} \; x \cdot 2(x-2)`

**[M1]**

$\text{f} ' ( x ) = \frac{(x-2)^{2}}{x} + 2 ( x - 2 ) \text{ln}  x$

**[A1]**

> **[mark-scheme]**
> **B1**: For $\frac{\text{d}}{\text{d}x} ( x - 2 )^{2} = 2 ( x - 2 )$ (or $2 x - 4$).
> 
> **B1**: For $\frac{\text{d}}{\text{d}x} \text{ln}  x = \frac{1}{x}$.
> 
> **M1**: Correct use of the product rule structure with their two derivatives.
> 
> **A1**: For $\text{f} ' ( x ) = \frac{(x-2)^{2}}{x} + 2 ( x - 2 ) \text{ln}  x$, or the unfactored equivalent.
Substitute $x = 1$ into $\text{f} ' ( x )$, using $\text{ln}  1 = 0$

$\text{f} ' ( 1 ) = \frac{(1-2)^{2}}{1} + 2 ( 1 - 2 ) \text{ln}  1 = 1 + 0$

**[M1]**

$\text{f} ' ( 1 ) = 1$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitutes $x = 1$ into their $\text{f} ' ( x )$, using $\text{ln}  1 = 0$.
> 
> **A1**: For a gradient of $1$.
Use the point-gradient form $y - y_{1} = m ( x - x_{1} )$ with $m = 1$ and $( x_{1} , y_{1} ) = ( 1 , 0 )$

$y - 0 = 1 ( x - 1 )$

**[M1]**

Rearrange into the form $a x + b y + c = 0$

$x - y - 1 = 0$

**[A1]**

> **[mark-scheme]**
> **M1**: Uses the point-gradient form with their gradient and the point $( 1 , 0 )$.
> 
> **A1**: For $x - y - 1 = 0$, or any integer multiple (for example $- x + y + 1 = 0$).

### Q9
Differentiate, using the standard result $\frac{\text{d}}{\text{d}x} \text{e}^{ax} = a \text{e}^{ax}$

$\frac{\text{d}y}{\text{d}x} = 5 \times ( - 2 ) \text{e}^{-2x}$

**[M1]**

$\frac{\text{d}y}{\text{d}x} = - 10 \text{e}^{-2x}$

**[A1]**

> **[mark-scheme]**
> **M1**: Differentiates $5 \text{e}^{-2x}$, bringing down the factor $- 2$ from the exponent (an answer of the form $k \text{e}^{-2x}$).
> 
> **A1**: For $\frac{\text{d}y}{\text{d}x} = - 10 \text{e}^{-2x}$.
(i)

The gradient of the tangent is $\frac{\text{d}y}{\text{d}x}$ evaluated at $x = 1$

$\frac{\text{d}y}{\text{d}x} = - 10 \text{e}^{-2(1)}$

$\frac{\text{d}y}{\text{d}x} = - 10 \text{e}^{-2}$

**[B1]**

(ii)

The normal is perpendicular to the tangent, so its gradient is $- \frac{1}{m}$, where $m$ is the gradient of the tangent

$\text{gradient of normal} = - \frac{1}{-10\text{e}^{-2}} = \frac{1}{10\text{e}^{-2}}$

**[M1]**

Since $\frac{1}{\text{e}^{-2}} = \text{e}^{2}$, this gives

$\text{gradient of normal} = \frac{1}{10} \text{e}^{2}$

**[A1]**

> **[mark-scheme]**
> **B1**: For a tangent gradient of $- 10 \text{e}^{-2}$ (so $a = 10$). Follow through on their $\frac{\text{d}y}{\text{d}x}$.
> 
> **M1**: Uses the perpendicular relationship, taking the negative reciprocal $- \frac{1}{m}$ of their tangent gradient.
> 
> **A1**: Correctly reaches the given normal gradient $\frac{1}{10} \text{e}^{2}$, with the index step $\frac{1}{\text{e}^{-2}} = \text{e}^{2}$ shown. Because the answer is given, the working must be visible.

### Q10
Generate the first few functions by repeated differentiation, using $\frac{\text{d}}{\text{d}x} \text{sin} ( x \sqrt{2} ) = \sqrt{2}  \text{cos} ( x \sqrt{2} )$ and the chain rule

$u_{1} = \text{sin} ( x \sqrt{2} )$

$u_{2} = \sqrt{2}  \text{cos} ( x \sqrt{2} ) ,  u_{3} = - 2 \text{sin} ( x \sqrt{2} )$

$u_{4} = - 2 \sqrt{2}  \text{cos} ( x \sqrt{2} ) ,  u_{5} = 4 \text{sin} ( x \sqrt{2} )$

**[M1 A1]**

Substitute $x = \frac{π\sqrt{2}}{4}$, so the argument is $x \sqrt{2} = \frac{π}{2}$, giving $\text{sin} \frac{π}{2} = 1$ and $\text{cos} \frac{π}{2} = 0$

$u_{1} = 1 ,  u_{2} = 0 ,  u_{3} = - 2 ,  u_{4} = 0 ,  u_{5} = 4 ,  \dots$

**[M1]**

Every cosine term (the even-numbered functions up to $u_{40}$) is zero. The nonzero terms are the $21$ sine terms $u_{1} , u_{3} , \dots , u_{41}$, which form a geometric sequence with first term $a = 1$, common ratio $r = - 2$ and $n = 21$

$1 ,  - 2 ,  4 ,  - 8 ,  \dots$

Use the formula for the sum of the first $n$ terms of a geometric progression, $S_{n} = \frac{a(1-r^{n})}{1-r}$

`S_{21} = \dfrac{1\left(1 - (-2)^{21}\right)}{1 - (-2)} = \dfrac{1 - (-2097152)}{3} = \dfrac{2097153}{3}`

**[M1]**

`\text{f}_{41}\left(\dfrac{\pi\sqrt{2}}{4}\right) = 699051`

**[A1]**

> **[exam-tip]**
> The whole question is engineered around the value $x = \frac{π\sqrt{2}}{4}$, which makes every argument equal to $\frac{π}{2}$.
> 
> Spotting this early is the key: it kills all the cosine terms and turns a daunting sum of $41$ derivatives into a short geometric series. Whenever a recurrence produces a repeating cycle of functions, look for the value that simplifies them all at once.

> **[mark-scheme]**
> **M1**: Differentiates repeatedly to generate the sequence of functions, using the chain rule.
> 
> **A1**: For a correct pattern, for example $u_{1} = \text{sin} ( x \sqrt{2} )$, $u_{2} = \sqrt{2}  \text{cos} ( x \sqrt{2} )$, $u_{3} = - 2 \text{sin} ( x \sqrt{2} )$, $u_{4} = - 2 \sqrt{2}  \text{cos} ( x \sqrt{2} )$.
> 
> **M1**: Substitutes $x = \frac{π\sqrt{2}}{4}$, recognising the argument is $\frac{π}{2}$, so the cosine terms are $0$ and the sine terms are $1 , - 2 , 4 , \dots$.
> 
> **M1**: Identifies the geometric series ($a = 1$, $r = - 2$, $n = 21$) and applies the sum formula.
> 
> **A1**: For $699051$.

### Q11
Write each term in exponential form, using $a^{x} = \text{e}^{x\mathrm{ln}a}$

$y = 3^{x} + 2^{-x} = \text{e}^{x\mathrm{ln}3} + \text{e}^{-x\mathrm{ln}2}$

Differentiate using the chain rule, treating $\text{ln}  3$ and $\text{ln}  2$ as constants

$\frac{\text{d}y}{\text{d}x} = \text{ln}  3  \text{e}^{x\mathrm{ln}3} - \text{ln}  2  \text{e}^{-x\mathrm{ln}2} = 3^{x} \text{ln}  3 - 2^{-x} \text{ln}  2$

**[M1 A1]**

Find the gradient of the tangent at $x = 1$, using $3^{1} = 3$ and $2^{-1} = \frac{1}{2}$, then take the negative reciprocal for the normal

$\frac{\text{d}y}{\text{d}x} = 3 \text{ln}  3 - \frac{1}{2} \text{ln}  2$

$m_{\text{normal}} = \frac{-1}{3\text{ln}3-\frac{1}{2}\text{ln}2}$

**[M1]**

Multiply numerator and denominator by $- 2$

$m_{\text{normal}} = \frac{2}{\text{ln}2-6\text{ln}3}$

**[A1]**

> **[mark-scheme]**
> **M1**: Differentiates, writing $a^{x}$ as $\text{e}^{x\mathrm{ln}a}$ (or quoting $\frac{\text{d}}{\text{d}x} a^{x} = a^{x} \text{ln}  a$).
> 
> **A1**: For $\frac{\text{d}y}{\text{d}x} = 3^{x} \text{ln}  3 - 2^{-x} \text{ln}  2$.
> 
> **M1**: Substitutes $x = 1$ to get $3 \text{ln}  3 - \frac{1}{2} \text{ln}  2$, and forms the negative reciprocal for the normal.
> 
> **A1**: Reaches the given result $\frac{2}{\text{ln}2-6\text{ln}3}$, showing the multiplication by $- 2$. Because the answer is given, this step must be visible.

### Q12
(i)

Differentiate each term using the chain rule

`\dfrac{\text{d}}{\text{d}x}\left(\text{tan} \; 3x + \text{e}^{7 - 2x^{2}}\right) = 3\text{sec}^{2} \; 3x + (-4x)\text{e}^{7 - 2x^{2}}`

$= 3 \text{sec}^{2}  3 x - 4 x  \text{e}^{7-2x^{2}}$

**[M1 A1]**

(ii)

Apply the product rule, $\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$, differentiating $v = \text{cos} ( 3 - x )$ by the chain rule

$u = x^{2} + 2 x - 8 ,  v = \text{cos} ( 3 - x )$

$\frac{\text{d}u}{\text{d}x} = 2 ( x + 1 ) ,  \frac{\text{d}v}{\text{d}x} = \text{sin} ( 3 - x )$

Substitute these into the product rule

`\dfrac{\text{d}y}{\text{d}x} = \left(x^{2} + 2x - 8\right)\text{sin}(3 - x) + 2(x + 1)\text{cos}(3 - x)`

**[M1 A1]**

(iii)

Apply the quotient rule, $\frac{\text{d}y}{\text{d}x} = \frac{v\frac{\text{d}u}{\text{d}x}-u\frac{\text{d}v}{\text{d}x}}{v^{2}}$, using $\frac{\text{d}}{\text{d}x} \text{ln}  7 x = \frac{1}{x}$ and the chain rule on $v$

$u = \text{ln}  7 x ,  v = \text{sin} ( x^{2} + 5 )$

$\frac{\text{d}u}{\text{d}x} = \frac{1}{x} ,  \frac{\text{d}v}{\text{d}x} = 2 x  \text{cos} ( x^{2} + 5 )$

Substitute, then multiply numerator and denominator by $x$

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{sin}(x^{2} + 5)\cdot\dfrac{1}{x} - \text{ln} \; 7x\cdot 2x\;\text{cos}(x^{2} + 5)}{\text{sin}^{2}(x^{2} + 5)}`

**[M1]**

$\frac{\text{d}y}{\text{d}x} = \frac{\text{sin}(x^{2}+5)-2x^{2}\text{ln}7x\text{cos}(x^{2}+5)}{x\text{sin}^{2}(x^{2}+5)}$

**[A1]**

(iv)

Write $\sqrt{\text{cos}4x} = ( \text{cos}  4 x )^{\frac{1}{2}}$ and apply the chain rule

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{1}{2}(\text{cos} \; 4x)^{-\frac{1}{2}}\cdot(-4\text{sin} \; 4x)`

**[M1]**

$\frac{\text{d}y}{\text{d}x} = - 2 \text{sin}  4 x  ( \text{cos}  4 x )^{-\frac{1}{2}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Chain rule used on both terms of part (i).
> 
> **A1**: For $3 \text{sec}^{2}  3 x - 4 x  \text{e}^{7-2x^{2}}$.
> 
> **M1**: Correct use of the product rule in part (ii), with $\frac{\text{d}v}{\text{d}x} = \text{sin} ( 3 - x )$ from the chain rule.
> 
> **A1**: For `\left(x^{2} + 2x - 8\right)\text{sin}(3 - x) + 2(x + 1)\text{cos}(3 - x)`.
> 
> **M1**: Correct use of the quotient rule in part (iii), with $\frac{\text{d}u}{\text{d}x} = \frac{1}{x}$ and $\frac{\text{d}v}{\text{d}x} = 2 x  \text{cos} ( x^{2} + 5 )$.
> 
> **A1**: For the fully correct expression, in any equivalent form (accept the unsimplified form before multiplying by $x$).
> 
> **M1**: Correct use of the chain rule in part (iv), giving $\frac{1}{2} ( \text{cos}  4 x )^{-\frac{1}{2}}$ times $- 4 \text{sin}  4 x$.
> 
> **A1**: For $- 2 \text{sin}  4 x  ( \text{cos}  4 x )^{-\frac{1}{2}}$, or equivalently $\frac{-2\text{sin}4x}{\sqrt{\text{cos}4x}}$.

### Q13
Apply the product rule, $\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$

$u = 5 + \text{sin}^{2}  3 x ,  v = \text{e}^{x^{2}-3x+2}$

Differentiate $u$ (chain rule on $\text{sin}^{2}  3 x$, then the double angle $\text{sin}  6 x = 2 \text{sin}  3 x  \text{cos}  3 x$)

$\frac{\text{d}u}{\text{d}x} = 6 \text{sin}  3 x  \text{cos}  3 x = 3 \text{sin}  6 x ,  \frac{\text{d}v}{\text{d}x} = ( 2 x - 3 ) \text{e}^{x^{2}-3x+2}$

Substitute these into the product rule

`\dfrac{\text{d}y}{\text{d}x} = \left(5 + \text{sin}^{2} \; 3x\right)(2x - 3)\text{e}^{x^{2} - 3x + 2} + \text{e}^{x^{2} - 3x + 2}\left(3\text{sin} \; 6x\right)`

**[M1 A1]**

Factor out $\text{e}^{x^{2}-3x+2}$

`\dfrac{\text{d}y}{\text{d}x} = \text{e}^{x^{2} - 3x + 2}\left[\left(5 + \text{sin}^{2} \; 3x\right)(2x - 3) + 3\text{sin} \; 6x\right]`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the product rule, with $\frac{\text{d}u}{\text{d}x} = 3 \text{sin}  6 x$ (or $6 \text{sin}  3 x  \text{cos}  3 x$) and $\frac{\text{d}v}{\text{d}x} = ( 2 x - 3 ) \text{e}^{x^{2}-3x+2}$.
> 
> **A1**: For a correct derivative in any unsimplified form.
> 
> **A1**: For the factored form `\text{e}^{x^{2} - 3x + 2}\left[\left(5 + \text{sin}^{2} \; 3x\right)(2x - 3) + 3\text{sin} \; 6x\right]`.
Apply the product rule, $\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$, with $u = 3^{\sqrt{x}}$ and $v = \sqrt{x} - \frac{1}{\sqrt{x}}$

To differentiate $u$, first write it in exponential form, using $3 = \text{e}^{\text{ln}3}$

$u = 3^{\sqrt{x}} = \text{e}^{\sqrt{x}\text{ln}3}$

Differentiate by the chain rule, multiplying $\text{e}^{\sqrt{x}\text{ln}3}$ by the derivative of the exponent $\sqrt{x}  \text{ln}  3$

`\dfrac{\text{d}u}{\text{d}x} = \text{e}^{\sqrt{x}\;\text{ln} \; 3}\cdot\dfrac{\text{d}}{\text{d}x}\left(\sqrt{x}\;\text{ln} \; 3\right)`

Treat $\text{ln}  3$ as a constant and use $\frac{\text{d}}{\text{d}x} x^{\frac{1}{2}} = \frac{1}{2} x^{-\frac{1}{2}}$

`\dfrac{\text{d}}{\text{d}x}\left(\sqrt{x}\;\text{ln} \; 3\right) = \dfrac{1}{2}x^{-\frac{1}{2}}\text{ln} \; 3`

Substitute this in, and rewrite $\text{e}^{\sqrt{x}\text{ln}3}$ back as $3^{\sqrt{x}}$

$\frac{\text{d}u}{\text{d}x} = \frac{1}{2} x^{-\frac{1}{2}} ( \text{ln}  3 )  3^{\sqrt{x}}$

Differentiate $v = x^{\frac{1}{2}} - x^{-\frac{1}{2}}$ term by term

$\frac{\text{d}v}{\text{d}x} = \frac{1}{2} x^{-\frac{1}{2}} + \frac{1}{2} x^{-\frac{3}{2}}$

Substitute these into the product rule

`\dfrac{\text{d}y}{\text{d}x} = 3^{\sqrt{x}}\left(\dfrac{1}{2}x^{-\frac{1}{2}} + \dfrac{1}{2}x^{-\frac{3}{2}}\right) + \left(x^{\frac{1}{2}} - x^{-\frac{1}{2}}\right)\dfrac{1}{2}x^{-\frac{1}{2}}(\text{ln} \; 3)\;3^{\sqrt{x}}`

**[M1 A1]**

Factor out $\frac{3^{\sqrt{x}}}{2}$ and simplify `(\text{ln} \; 3)x^{-\frac{1}{2}}\left(x^{\frac{1}{2}} - x^{-\frac{1}{2}}\right) = \text{ln} \; 3 - (\text{ln} \; 3)x^{-1}`

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{3^{\sqrt{x}}}{2}\left(x^{-\frac{1}{2}} + x^{-\frac{3}{2}} + \text{ln} \; 3 - (\text{ln} \; 3)x^{-1}\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the product rule, with $\frac{\text{d}u}{\text{d}x} = \frac{1}{2} x^{-\frac{1}{2}} ( \text{ln}  3 )  3^{\sqrt{x}}$ and $\frac{\text{d}v}{\text{d}x} = \frac{1}{2} x^{-\frac{1}{2}} + \frac{1}{2} x^{-\frac{3}{2}}$.
> 
> **A1**: For a correct derivative in any unsimplified form.
> 
> **A1**: For the simplified form `\dfrac{3^{\sqrt{x}}}{2}\left(x^{-\frac{1}{2}} + x^{-\frac{3}{2}} + \text{ln} \; 3 - (\text{ln} \; 3)x^{-1}\right)`.

### Q14
At the stationary points $A$ and $B$, the gradient is zero. Differentiate using the quotient rule

$u = \text{sin}  3 x ,  v = \text{e}^{2x-3}$

$\frac{\text{d}u}{\text{d}x} = 3 \text{cos}  3 x ,  \frac{\text{d}v}{\text{d}x} = 2 \text{e}^{2x-3}$

`\text{f}'(x) = \dfrac{\text{e}^{2x - 3}\left(3\text{cos} \; 3x\right) - \text{sin} \; 3x\left(2\text{e}^{2x - 3}\right)}{\left(\text{e}^{2x - 3}\right)^{2}} = 0`

**[M1 A1]**

The denominator is never zero, so set the numerator to zero and divide through by $\text{e}^{2x-3}$

$3 \text{cos}  3 x - 2 \text{sin}  3 x = 0 \Rightarrow \text{tan}  3 x = \frac{3}{2}$

**[M1]**

Solve for $x$ in $0 \leq x \leq \frac{2π}{3}$; the smaller root gives the maximum $A$, the larger gives the minimum $B$

`3x = \text{tan}^{-1}\left(\dfrac{3}{2}\right) = 0.9828\ldots \implies x = 0.3276\ldots`

`3x = \text{tan}^{-1}\left(\dfrac{3}{2}\right) + \pi = 4.1244\ldots \implies x = 1.3748\ldots`

**[A1]**

Evaluate $\text{f}$ at each stationary point to find the maximum value (at $A$) and the minimum value (at $B$)

$y_{A} = \text{f} ( 0 . 3276 \dots ) = 8 . 679$

$y_{B} = \text{f} ( 1 . 3748 \dots ) = - 1 . 069$

**[M1]**

The range is the set of values from the minimum (at $B$) up to the maximum (at $A$)

**Final answer:** $- 1 . 069 \leq \text{f} ( x ) \leq 8 . 679$** (3 d.p.)**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the quotient rule, with $u = \text{sin}  3 x$, $v = \text{e}^{2x-3}$ and both derivatives correct.
> 
> **A1**: For a correct $\text{f} ' ( x )$.
> 
> **M1**: Sets the numerator to zero and reaches $\text{tan}  3 x = \frac{3}{2}$.
> 
> **A1**: For both $x$-values in range, $x = 0 . 3276 \dots$ and $x = 1 . 3748 \dots$.
> 
> **M1**: Evaluates $\text{f}$ at both stationary points, giving the maximum $8 . 679$ and minimum $- 1 . 069$.
> 
> **A1**: States the range as $- 1 . 069 \leq \text{f} ( x ) \leq 8 . 679$. Accept answers which round to these values. The range is the interval of output values, not the difference between them.

### Q15
The derivative of $\text{tan}^{-1} x$ is given in the List of Formulae as

$\frac{\text{d}}{\text{d}x} \text{tan}^{-1} x = \frac{1}{1+x^{2}}$

Differentiate the `\text{tan}^{-1}\left(\dfrac{2x}{3}\right)` term by the chain rule, with $u = \frac{2x}{3}$ so that $\frac{\text{d}u}{\text{d}x} = \frac{2}{3}$. Substitute into the formula, multiplying by $\frac{\text{d}u}{\text{d}x}$

`\dfrac{\text{d}}{\text{d}x}\text{tan}^{-1}\left(\dfrac{2x}{3}\right) = \dfrac{1}{1 + \left(\frac{2x}{3}\right)^{2}}\cdot\dfrac{2}{3}`

Differentiate $y$ term by term, using `\dfrac{\text{d}}{\text{d}x}\left(\dfrac{x}{3}\right) = \dfrac{1}{3}`

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{1}{3} - \dfrac{2}{3}\cdot\dfrac{1}{1 + \left(\frac{2x}{3}\right)^{2}}`

**[M1 A1]**

Set the gradient to zero and solve

`\dfrac{1}{3} = \dfrac{2}{3\left(1 + \frac{4x^{2}}{9}\right)} \implies 1 + \dfrac{4x^{2}}{9} = 2`

$\frac{4x^{2}}{9} = 1 \Rightarrow x^{2} = \frac{9}{4} \Rightarrow x = \pm \frac{3}{2}$

**[M1]**

Find the $y$-coordinate at each, using $\text{tan}^{-1} ( 1 ) = \frac{π}{4}$ and $\text{tan}^{-1} ( - 1 ) = - \frac{π}{4}$

$x = \frac{3}{2} :  y = \frac{1}{2} - \text{tan}^{-1} ( 1 ) = \frac{1}{2} - \frac{π}{4}$

$x = - \frac{3}{2} :  y = - \frac{1}{2} - \text{tan}^{-1} ( - 1 ) = - \frac{1}{2} + \frac{π}{4}$

**[A1]**

Classify each point with the second derivative

`\dfrac{\text{d}^{2}y}{\text{d}x^{2}} = \dfrac{16x}{27}\left(1 + \dfrac{4x^{2}}{9}\right)^{-2}`

**[M1]**

The factor `\left(1 + \frac{4x^{2}}{9}\right)^{-2}` is always positive, so the sign of $\frac{\text{d}^{2}y}{\text{d}x^{2}}$ matches the sign of $x$

$x = \frac{3}{2} > 0 \Rightarrow \frac{\text{d}^{2}y}{\text{d}x^{2}} > 0$

$x = - \frac{3}{2} < 0 \Rightarrow \frac{\text{d}^{2}y}{\text{d}x^{2}} < 0$

**Final answer:** **Minimum at **`\left(\dfrac{3}{2}, \dfrac{1}{2} - \dfrac{\pi}{4}\right)`**, maximum at **`\left(-\dfrac{3}{2}, -\dfrac{1}{2} + \dfrac{\pi}{4}\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Differentiates, using the given tan⁻¹ derivative with the chain rule on $\frac{2x}{3}$.
> 
> **A1**: For `\dfrac{\text{d}y}{\text{d}x} = \dfrac{1}{3} - \dfrac{2}{3}\cdot\dfrac{1}{1 + \left(\frac{2x}{3}\right)^{2}}`.
> 
> **M1**: Sets $\frac{\text{d}y}{\text{d}x} = 0$ and solves to $x = \pm \frac{3}{2}$.
> 
> **A1**: For both points, `\left(\dfrac{3}{2}, \dfrac{1}{2} - \dfrac{\pi}{4}\right)` and `\left(-\dfrac{3}{2}, -\dfrac{1}{2} + \dfrac{\pi}{4}\right)`, with exact $y$-values.
> 
> **M1**: Finds the second derivative and considers its sign at each stationary point.
> 
> **A1**: Correctly classifies the minimum at `\left(\dfrac{3}{2}, \dfrac{1}{2} - \dfrac{\pi}{4}\right)` and the maximum at `\left(-\dfrac{3}{2}, -\dfrac{1}{2} + \dfrac{\pi}{4}\right)`.

### Q16
Start with the innermost function and work outwards. Differentiate `\text{ln}\left(\dfrac{1}{x}\right)` by the chain rule

`\dfrac{\text{d}}{\text{d}x}\text{ln}\left(\dfrac{1}{x}\right) = \dfrac{1}{\frac{1}{x}}\cdot\left(-x^{-2}\right) = -x^{-1} = -\dfrac{1}{x}`

**[M1 A1]**

Differentiate the middle layer `\text{cos}\left(\text{ln}\left(\dfrac{1}{x}\right)\right)`, multiplying by the inner derivative

`\dfrac{\text{d}}{\text{d}x}\text{cos}\left(\text{ln}\left(\dfrac{1}{x}\right)\right) = -\text{sin}\left(\text{ln}\left(\dfrac{1}{x}\right)\right)\cdot\left(-\dfrac{1}{x}\right) = \dfrac{\text{sin}\left(\text{ln}\left(\frac{1}{x}\right)\right)}{x}`

Differentiate the outer layer $\text{sin} ( \dots )$, multiplying by this result

`\text{f}'(x) = \text{cos}\left(\text{cos}\left(\text{ln}\left(\dfrac{1}{x}\right)\right)\right)\cdot\dfrac{\text{sin}\left(\text{ln}\left(\frac{1}{x}\right)\right)}{x}`

**[M1]**

`\text{f}'(x) = \dfrac{\text{sin}\left(\text{ln}\left(\frac{1}{x}\right)\right)\text{cos}\left(\text{cos}\left(\text{ln}\left(\frac{1}{x}\right)\right)\right)}{x}`

**[A1]**

> **[mark-scheme]**
> **M1**: Differentiates the innermost function `\text{ln}\left(\dfrac{1}{x}\right)` using the chain rule.
> 
> **A1**: For `\dfrac{\text{d}}{\text{d}x}\text{ln}\left(\dfrac{1}{x}\right) = -\dfrac{1}{x}` (or equivalently from `\text{ln}\left(\dfrac{1}{x}\right) = -\text{ln} \; x`).
> 
> **M1**: Differentiates outwards through the $\text{cos}$ and $\text{sin}$ layers, multiplying each outer derivative by the layer inside it.
> 
> **A1**: For the fully correct `\text{f}'(x) = \dfrac{\text{sin}\left(\text{ln}\left(\frac{1}{x}\right)\right)\text{cos}\left(\text{cos}\left(\text{ln}\left(\frac{1}{x}\right)\right)\right)}{x}`.

### Q17
Write $4^{-x^{4}}$ in exponential form, using $4 = \text{e}^{\text{ln}4}$

`y = 4^{-x^{4}} = \left(\text{e}^{\text{ln} \; 4}\right)^{-x^{4}} = \text{e}^{-x^{4}\text{ln} \; 4}`

**[M1]**

Differentiate using the chain rule, treating $\text{ln}  4$ as a constant

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{d}}{\text{d}x}\left(-x^{4}\text{ln} \; 4\right)\cdot\text{e}^{-x^{4}\text{ln} \; 4} = -4x^{3}\text{ln} \; 4\cdot\text{e}^{-x^{4}\text{ln} \; 4}`

**[M1 A1]**

Group the factor of $4$ with the exponential, since `4\;\text{e}^{-x^{4}\text{ln} \; 4} = 4\cdot 4^{-x^{4}} = 4^{1 - x^{4}}`

$\frac{\text{d}y}{\text{d}x} = - ( \text{ln}  4 ) x^{3}  4^{1-x^{4}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Writes $4^{-x^{4}}$ as $\text{e}^{-x^{4}\text{ln}4}$ (or quotes `\dfrac{\text{d}}{\text{d}x}a^{u} = a^{u}\text{ln} \; a \cdot \dfrac{\text{d}u}{\text{d}x}`).
> 
> **M1**: Differentiates using the chain rule, bringing down $- 4 x^{3} \text{ln}  4$.
> 
> **A1**: For $- 4 x^{3} \text{ln}  4  \text{e}^{-x^{4}\text{ln}4}$, or equivalent.
> 
> **A1**: Groups to reach the given result $- ( \text{ln}  4 ) x^{3}  4^{1-x^{4}}$, showing $4  \text{e}^{-x^{4}\text{ln}4} = 4^{1-x^{4}}$. Because the answer is given, this must be visible.
Find the gradient at $x = 1$, using part (a) and $4^{1-1^{4}} = 4^{0} = 1$

$m = - ( \text{ln}  4 ) ( 1 )^{3}  4^{1-1^{4}} = - \text{ln}  4$

**[M1]**

Use the point-gradient form with `\left(1, \dfrac{1}{4}\right)`, then rearrange

$y - \frac{1}{4} = - ( \text{ln}  4 ) ( x - 1 )$

`y = -(\text{ln} \; 4)x + \left(\text{ln} \; 4 + \dfrac{1}{4}\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Substitutes $x = 1$ into part (a) to find $m = - \text{ln}  4$, and applies the point-gradient form.
> 
> **A1**: For `y = -(\text{ln} \; 4)x + \left(\text{ln} \; 4 + \dfrac{1}{4}\right)`, so $a = - \text{ln}  4$ and $b = \text{ln}  4 + \frac{1}{4}$.

### Q18
Apply the product rule to `y = \text{f}(x)\left[\text{g}(x)\right]^{-1}`, with $\frac{\text{d}v}{\text{d}x}$ found by the chain rule

`u = \text{f}(x), \quad v = \left[\text{g}(x)\right]^{-1}`

`\dfrac{\text{d}u}{\text{d}x} = \text{f}'(x), \quad \dfrac{\text{d}v}{\text{d}x} = -\left[\text{g}(x)\right]^{-2}\text{g}'(x)`

**[M1]**

Substitute into the product rule $\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$

`\dfrac{\text{d}y}{\text{d}x} = \text{f}(x)\left(-\left[\text{g}(x)\right]^{-2}\text{g}'(x)\right) + \left[\text{g}(x)\right]^{-1}\text{f}'(x)`

`= \dfrac{-\text{f}(x)\text{g}'(x)}{\left(\text{g}(x)\right)^{2}} + \dfrac{\text{f}'(x)}{\text{g}(x)}`

**[A1]**

Write the second term over the common denominator `\left(\text{g}(x)\right)^{2}` by multiplying by $\frac{\text{g}(x)}{\text{g}(x)}$

`= \dfrac{-\text{f}(x)\text{g}'(x)}{\left(\text{g}(x)\right)^{2}} + \dfrac{\text{f}'(x)\text{g}(x)}{\left(\text{g}(x)\right)^{2}}`

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{g}(x)\text{f}'(x) - \text{f}(x)\text{g}'(x)}{\left(\text{g}(x)\right)^{2}}`

**[A1]**

> **[mark-scheme]**
> **M1**: Applies the product rule to `\text{f}(x)\left[\text{g}(x)\right]^{-1}`, using the chain rule to obtain `\dfrac{\text{d}v}{\text{d}x} = -\left[\text{g}(x)\right]^{-2}\text{g}'(x)`.
> 
> **A1**: For a correct expression for $\frac{\text{d}y}{\text{d}x}$ before combining, for example `\dfrac{-\text{f}(x)\text{g}'(x)}{\left(\text{g}(x)\right)^{2}} + \dfrac{\text{f}'(x)}{\text{g}(x)}`.
> 
> **A1**: Combines over the common denominator to reach the given quotient rule. Because the answer is given, the common-denominator step must be shown.

### Q19
Apply the product rule, $\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$

$u = 2 \text{sin}  3 x - \text{cos}  3 x ,  v = \text{e}^{6-x}$

$\frac{\text{d}u}{\text{d}x} = 6 \text{cos}  3 x + 3 \text{sin}  3 x ,  \frac{\text{d}v}{\text{d}x} = - \text{e}^{6-x}$

Substitute these into the product rule

`\dfrac{\text{d}y}{\text{d}x} = \left(2\text{sin} \; 3x - \text{cos} \; 3x\right)\left(-\text{e}^{6 - x}\right) + \text{e}^{6 - x}\left(6\text{cos} \; 3x + 3\text{sin} \; 3x\right)`

**[M1 A1]**

Factor out $\text{e}^{6-x}$ and collect like terms

`= \text{e}^{6 - x}\left(-2\text{sin} \; 3x + \text{cos} \; 3x + 6\text{cos} \; 3x + 3\text{sin} \; 3x\right)`

`\dfrac{\text{d}y}{\text{d}x} = \text{e}^{6 - x}\left(\text{sin} \; 3x + 7\text{cos} \; 3x\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the product rule, with $u = 2 \text{sin}  3 x - \text{cos}  3 x$, $v = \text{e}^{6-x}$ and both derivatives correct.
> 
> **A1**: For a correct derivative in any unsimplified form.
> 
> **A1**: For the simplified form `\text{e}^{6 - x}\left(\text{sin} \; 3x + 7\text{cos} \; 3x\right)`.
Apply the product rule. Expand $u$, and use $\text{ln}  5 x = \text{ln}  5 + \text{ln}  x$ so that $\frac{\text{d}v}{\text{d}x} = \frac{1}{x}$

`u = \left(x^{2} - x\right)^{2} = x^{4} - 2x^{3} + x^{2}, \quad v = \text{ln} \; 5x`

$\frac{\text{d}u}{\text{d}x} = 4 x^{3} - 6 x^{2} + 2 x ,  \frac{\text{d}v}{\text{d}x} = \frac{1}{x}$

Substitute these into the product rule

`\dfrac{\text{d}y}{\text{d}x} = \left(x^{4} - 2x^{3} + x^{2}\right)\dfrac{1}{x} + \text{ln} \; 5x\left(4x^{3} - 6x^{2} + 2x\right)`

**[M1 A1]**

Simplify the first term, since $\frac{x^{4}-2x^{3}+x^{2}}{x} = x^{3} - 2 x^{2} + x$

`\dfrac{\text{d}y}{\text{d}x} = x^{3} - 2x^{2} + x + \left(4x^{3} - 6x^{2} + 2x\right)\text{ln} \; 5x`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the product rule, with $v ' = \frac{1}{x}$ from $\text{ln}  5 x$.
> 
> **A1**: For a correct derivative in any unsimplified form.
> 
> **A1**: For the simplified form `x^{3} - 2x^{2} + x + \left(4x^{3} - 6x^{2} + 2x\right)\text{ln} \; 5x`.

### Q20
(i)

Differentiate each term using the chain rule

`\dfrac{\text{d}}{\text{d}x}\left(\text{sin} \; 2x - \text{e}^{7x}\right)`

$= 2 \text{cos}  2 x - 7 \text{e}^{7x}$

**[M1 A1]**

(ii)

Apply the product rule, $\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$

$u = x^{2} ,  v = \text{ln}  x$

$\frac{\text{d}u}{\text{d}x} = 2 x ,  \frac{\text{d}v}{\text{d}x} = \frac{1}{x}$

Substitute these in, then simplify

`\dfrac{\text{d}y}{\text{d}x} = x^{2}\cdot\dfrac{1}{x} + \text{ln} \; x\cdot 2x = x + 2x\;\text{ln} \; x`

**[M1]**

Factor out $x$

`\dfrac{\text{d}y}{\text{d}x} = x\left(1 + 2\text{ln} \; x\right)`

**[A1]**

(iii)

Apply the quotient rule, $\frac{\text{d}y}{\text{d}x} = \frac{v\frac{\text{d}u}{\text{d}x}-u\frac{\text{d}v}{\text{d}x}}{v^{2}}$, differentiating each of $u$ and $v$ by the chain rule

$u = \text{cos}  3 x ,  v = \text{tan}  2 x$

$\frac{\text{d}u}{\text{d}x} = - 3 \text{sin}  3 x ,  \frac{\text{d}v}{\text{d}x} = 2 \text{sec}^{2}  2 x$

Substitute these into the quotient rule

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{tan} \; 2x\left(-3\text{sin} \; 3x\right) - \text{cos} \; 3x\left(2\text{sec}^{2} \; 2x\right)}{\text{tan}^{2} \; 2x}`

**[M1]**

$\frac{\text{d}y}{\text{d}x} = \frac{-3\text{sin}3x\text{tan}2x-2\text{sec}^{2}2x\text{cos}3x}{\text{tan}^{2}2x}$

**[A1]**

(iv)

Apply the chain rule, $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$, with $u = \text{tan}  x$

$y = \text{ln}  u ,  \frac{\text{d}y}{\text{d}u} = \frac{1}{u}$

$u = \text{tan}  x ,  \frac{\text{d}u}{\text{d}x} = \text{sec}^{2}  x$

Substitute these into the chain rule

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{1}{\text{tan} \; x}\cdot\text{sec}^{2} \; x`

**[M1]**

$\frac{\text{d}y}{\text{d}x} = \frac{\text{sec}^{2}x}{\text{tan}x}$

**[A1]**

> **[mark-scheme]**
> **M1**: Chain rule used on both terms of part (i).
> 
> **A1**: For $2 \text{cos}  2 x - 7 \text{e}^{7x}$.
> 
> **M1**: Correct use of the product rule in part (ii).
> 
> **A1**: For `x\left(1 + 2\text{ln} \; x\right)`, or any correct equivalent form (for example $x + 2 x  \text{ln}  x$).
> 
> **M1**: Correct use of the quotient rule in part (iii), with $\frac{\text{d}v}{\text{d}x} = 2 \text{sec}^{2}  2 x$ from the chain rule.
> 
> **A1**: For a fully correct expression over $\text{tan}^{2}  2 x$, in any equivalent form.
> 
> **M1**: Correct use of the chain rule in part (iv), giving $\frac{1}{\text{tan}x}$ times $\text{sec}^{2}  x$.
> 
> **A1**: For $\frac{\text{sec}^{2}x}{\text{tan}x}$, or any equivalent form.

### Q21
At a maximum point the gradient is zero

$\frac{\text{d}y}{\text{d}x} = 0$

**[B1]**

Differentiate $\text{f} ( x )$ using the quotient rule, $\frac{\text{d}y}{\text{d}x} = \frac{v\frac{\text{d}u}{\text{d}x}-u\frac{\text{d}v}{\text{d}x}}{v^{2}}$

$u = \text{sin}  x ,  v = 1 - \text{e}^{x}$

$\frac{\text{d}u}{\text{d}x} = \text{cos}  x ,  \frac{\text{d}v}{\text{d}x} = - \text{e}^{x}$

Substitute these into the quotient rule

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{\left(1 - \text{e}^{x}\right)\text{cos} \; x - \text{sin} \; x\left(-\text{e}^{x}\right)}{\left(1 - \text{e}^{x}\right)^{2}}`

**[M1 A1]**

Expand the numerator, and expand the denominator using `\left(1 - \text{e}^{x}\right)^{2} = \text{e}^{2x} - 2\text{e}^{x} + 1`

$\frac{\text{d}y}{\text{d}x} = \frac{\text{cos}x-\text{e}^{x}\text{cos}x+\text{e}^{x}\text{sin}x}{\text{e}^{2x}-2\text{e}^{x}+1}$

**[M1]**

Group the terms containing $\text{e}^{x}$ in the numerator and set the gradient to zero

`\dfrac{\text{cos} \; x + \text{e}^{x}\left(\text{sin} \; x - \text{cos} \; x\right)}{\text{e}^{2x} - 2\text{e}^{x} + 1} = 0`

**[A1]**

> **[mark-scheme]**
> **B1**: States that at the maximum $A$ the gradient is zero, $\frac{\text{d}y}{\text{d}x} = 0$.
> 
> **M1**: Correct use of the quotient rule, with $u = \text{sin}  x$, $v = 1 - \text{e}^{x}$ and both derivatives correct.
> 
> **A1**: For a correct $\frac{\text{d}y}{\text{d}x}$ before expanding, for example `\dfrac{\left(1 - \text{e}^{x}\right)\text{cos} \; x + \text{e}^{x}\text{sin} \; x}{\left(1 - \text{e}^{x}\right)^{2}}`.
> 
> **M1**: Expands the numerator, and the denominator to $\text{e}^{2x} - 2 \text{e}^{x} + 1$.
> 
> **A1**: Groups the $\text{e}^{x}$ terms to reach the given equation. Because the answer is given, the grouping must be shown.

### Q22
Write $x = \text{sec}  7 y = \frac{1}{\text{cos}7y}$ and differentiate with respect to $y$ by the quotient rule, $\frac{\text{d}x}{\text{d}y} = \frac{v\frac{\text{d}u}{\text{d}y}-u\frac{\text{d}v}{\text{d}y}}{v^{2}}$, with $u = 1$ and $v = \text{cos}  7 y$

$u = 1 ,  v = \text{cos}  7 y$

$\frac{\text{d}u}{\text{d}y} = 0 ,  \frac{\text{d}v}{\text{d}y} = - 7 \text{sin}  7 y$

Substitute into the quotient rule and simplify, using $\frac{\text{sin}7y}{\text{cos}7y} = \text{tan}  7 y$ and $\frac{1}{\text{cos}7y} = \text{sec}  7 y$

`\dfrac{\text{d}x}{\text{d}y} = \dfrac{\text{cos} \; 7y \cdot 0 - 1\cdot\left(-7\text{sin} \; 7y\right)}{\left(\text{cos} \; 7y\right)^{2}} = \dfrac{7\text{sin} \; 7y}{\left(\text{cos} \; 7y\right)^{2}} = 7\text{tan} \; 7y\;\text{sec} \; 7y`

**[M1]**

Then $\frac{\text{d}y}{\text{d}x}$ is the reciprocal of $\frac{\text{d}x}{\text{d}y}$

$\frac{\text{d}y}{\text{d}x} = \frac{1}{7\text{tan}7y\text{sec}7y}$

**[A1]**

> **[mark-scheme]**
> **M1**: Differentiates $x = \text{sec}  7 y$ with respect to $y$ by any valid method (the quotient rule on $\frac{1}{\text{cos}7y}$, or the standard derivative of $\text{sec}$), reaching $\frac{\text{d}x}{\text{d}y} = 7 \text{tan}  7 y  \text{sec}  7 y$ or equivalent.
> 
> **A1**: For $\frac{\text{d}y}{\text{d}x} = \frac{1}{7\text{tan}7y\text{sec}7y}$, using the reciprocal.
From part (a), $\frac{\text{d}y}{\text{d}x} = \frac{1}{7\text{tan}7y\text{sec}7y}$. Since $x = \text{sec}  7 y$, replace $\text{sec}  7 y$ with $x$

$\frac{\text{d}y}{\text{d}x} = \frac{1}{7x\text{tan}7y}$

**[M1]**

Use the identity $\text{tan}^{2}  θ + 1 = \text{sec}^{2}  θ$, so $\text{tan}  7 y = \sqrt{\text{sec}^{2}7y-1}$, and $\text{sec}  7 y = x$

$\text{tan}  7 y = \sqrt{\text{sec}^{2}7y-1} = \sqrt{x^{2}-1}$

**[M1 A1]**

Substitute this in

$\frac{\text{d}y}{\text{d}x} = \frac{1}{7x\sqrt{x^{2}-1}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces $\text{sec}  7 y$ with $x$ to give $\frac{1}{7x\text{tan}7y}$.
> 
> **M1**: Uses $\text{tan}^{2}  θ + 1 = \text{sec}^{2}  θ$ to write $\text{tan}  7 y$ in terms of $\text{sec}  7 y$.
> 
> **A1**: For $\text{tan}  7 y = \sqrt{x^{2}-1}$.
> 
> **A1**: For $\frac{\text{d}y}{\text{d}x} = \frac{1}{7x\sqrt{x^{2}-1}}$.

### Q23
Find the $y$-coordinate at $x = 1$, using $\text{ln}  1 = 0$

$y = \text{e}^{-3(1)} + \text{ln}  1 = \text{e}^{-3}$

so the tangent passes through $( 1 , \text{e}^{-3} )$

**[B1]**

Differentiate to find the gradient function

$\frac{\text{d}y}{\text{d}x} = - 3 \text{e}^{-3x} + \frac{1}{x}$

**[M1 A1]**

Find the gradient at $x = 1$

$m = - 3 \text{e}^{-3(1)} + \frac{1}{1} = 1 - 3 \text{e}^{-3}$

**[M1]**

Use the point-gradient form $y - y_{1} = m ( x - x_{1} )$ with $( 1 , \text{e}^{-3} )$, then expand

`y - \text{e}^{-3} = \left(1 - 3\text{e}^{-3}\right)(x - 1)`

`y = \left(1 - 3\text{e}^{-3}\right)x + 3\text{e}^{-3} - 1 + \text{e}^{-3} = \left(1 - 3\text{e}^{-3}\right)x + 4\text{e}^{-3} - 1`

**[M1]**

Write $\text{e}^{-3} = \frac{1}{\text{e}^{3}}$ and combine each bracket over $\text{e}^{3}$

$1 - 3 \text{e}^{-3} = \frac{\text{e}^{3}-3}{\text{e}^{3}}$

$4 \text{e}^{-3} - 1 = \frac{4-\text{e}^{3}}{\text{e}^{3}}$

`y = \left(\dfrac{\text{e}^{3} - 3}{\text{e}^{3}}\right)x + \dfrac{4 - \text{e}^{3}}{\text{e}^{3}}`

**[A1]**

> **[mark-scheme]**
> **B1**: Finds $y = \text{e}^{-3}$ at $x = 1$, identifying the point $( 1 , \text{e}^{-3} )$.
> 
> **M1**: Differentiates the curve, using the chain rule on $\text{e}^{-3x}$.
> 
> **A1**: For $\frac{\text{d}y}{\text{d}x} = - 3 \text{e}^{-3x} + \frac{1}{x}$, in any correct form.
> 
> **M1**: Substitutes $x = 1$ to find the gradient $1 - 3 \text{e}^{-3}$.
> 
> **M1**: Applies the point-gradient form with their point and gradient, and expands.
> 
> **A1**: Correctly rewrites in the given form, showing $\text{e}^{-3} = \frac{1}{\text{e}^{3}}$. Because the answer is given, the conversion to $\text{e}^{3}$ form must be visible.

### Q24
Use the laws of logarithms to split $y$ before differentiating, since `\text{ln}(ax^{n}) = \text{ln} \; a + \text{ln}\left(x^{n}\right)`

`y = \text{ln}\left(ax^{n}\right) = \text{ln} \; a + n\;\text{ln} \; x`

**[M1 A1]**

Differentiate. The term $\text{ln}  a$ is a constant, so its derivative is $0$

`\dfrac{\text{d}y}{\text{d}x} = 0 + n\cdot\dfrac{1}{x}`

$\frac{\text{d}y}{\text{d}x} = \frac{n}{x}$

**[A1]**

Alternatively, by the chain rule with $u = a x^{n}$: `\dfrac{\text{d}y}{\text{d}x} = \dfrac{1}{ax^{n}}\cdot anx^{n-1} = nx^{-1} = \dfrac{n}{x}`

> **[mark-scheme]**
> **M1**: Uses the laws of logarithms to write `\text{ln}\left(ax^{n}\right)` as a sum, or sets up the chain rule with $u = a x^{n}$. Either method earns this mark.
> 
> **A1**: For $\text{ln}  a + n  \text{ln}  x$ (or a correct chain-rule expression $\frac{anx^{n-1}}{ax^{n}}$).
> 
> **A1**: Differentiates to the given result $\frac{n}{x}$, noting $\text{ln}  a$ differentiates to $0$. Because the answer is given, the working must be visible.

### Q25
The derivative of $\text{tan}^{-1} x$ is $\frac{1}{1+x^{2}}$, given in the List of Formulae. Apply the chain rule with $u = \frac{x}{a}$

$y = \text{tan}^{-1} u ,  \frac{\text{d}y}{\text{d}u} = \frac{1}{1+u^{2}}$

$u = \frac{x}{a} ,  \frac{\text{d}u}{\text{d}x} = \frac{1}{a}$

Substitute these into the chain rule

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{1}{1 + \left(\frac{x}{a}\right)^{2}}\cdot\dfrac{1}{a} = \dfrac{1}{a\left(1 + \frac{x^{2}}{a^{2}}\right)}`

**[M1]**

Multiply numerator and denominator by $a$ to clear the inner fraction

$\frac{\text{d}y}{\text{d}x} = \frac{a}{a^{2}+x^{2}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the chain rule with $u = \frac{x}{a}$, multiplying the given derivative $\frac{1}{1+u^{2}}$ by $\frac{1}{a}$.
> 
> **A1**: Reaches the given result $\frac{a}{a^{2}+x^{2}}$, clearing the inner fraction. Because the answer is given, the working must be visible.
Using part (a) with $a = 2$, differentiate and set the gradient to zero

$\frac{\text{d}y}{\text{d}x} = - \frac{1}{4} + \frac{2}{4+x^{2}} = 0$

Solve for $x$

$\frac{2}{4+x^{2}} = \frac{1}{4} \Rightarrow 8 = 4 + x^{2} \Rightarrow x^{2} = 4$

$x = \pm 2$

**[M1 A1]**

Find the $y$-coordinate at each, using $\text{tan}^{-1} ( 1 ) = \frac{π}{4}$ and $\text{tan}^{-1} ( - 1 ) = - \frac{π}{4}$

$x = 2 :  y = - \frac{2}{4} + \text{tan}^{-1} ( 1 ) = \frac{π}{4} - \frac{1}{2}$

$x = - 2 :  y = \frac{2}{4} + \text{tan}^{-1} ( - 1 ) = \frac{1}{2} - \frac{π}{4}$

**Final answer:** `\left(2, \dfrac{\pi}{4} - \dfrac{1}{2}\right)`** and **`\left(-2, \dfrac{1}{2} - \dfrac{\pi}{4}\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Differentiates $y$ using part (a) with $a = 2$, sets $\frac{\text{d}y}{\text{d}x} = 0$ and solves.
> 
> **A1**: For $x = \pm 2$.
> 
> **A1**: For both points `\left(2, \dfrac{\pi}{4} - \dfrac{1}{2}\right)` and `\left(-2, \dfrac{1}{2} - \dfrac{\pi}{4}\right)`, with exact $y$-values.

### Q26
Differentiate using the chain rule, $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$, with $u = \text{e}^{x} - \frac{π}{2}$

$y = 5 \text{cos}  u ,  \frac{\text{d}y}{\text{d}u} = - 5 \text{sin}  u$

$u = \text{e}^{x} - \frac{π}{2} ,  \frac{\text{d}u}{\text{d}x} = \text{e}^{x}$

Substitute these into the chain rule

`\dfrac{\text{d}y}{\text{d}x} = -5\text{sin}\left(\text{e}^{x} - \dfrac{\pi}{2}\right)\text{e}^{x}`

**[M1 A1]**

Find the gradient of the tangent at $x = 0$, using $\text{e}^{0} = 1$, then take the negative reciprocal for the normal

`\dfrac{\text{d}y}{\text{d}x} = -5\text{sin}\left(1 - \dfrac{\pi}{2}\right) = 2.7015\ldots`

$m_{\text{normal}} = - \frac{1}{2.7015\dots}$

**[M1]**

**Final answer:** $m_{\text{normal}} = - 0 . 370$** (3 d.p.)**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the chain rule, giving `-5\text{sin}\left(\text{e}^{x} - \dfrac{\pi}{2}\right)` multiplied by $\text{e}^{x}$.
> 
> **A1**: For `\dfrac{\text{d}y}{\text{d}x} = -5\text{e}^{x}\text{sin}\left(\text{e}^{x} - \dfrac{\pi}{2}\right)`, in any correct form.
> 
> **M1**: Substitutes $x = 0$ to find the tangent gradient $2 . 7015 \dots$ (radians), then takes the negative reciprocal.
> 
> **A1**: For $- 0 . 370$. Accept answers which round to $- 0 . 370$ to 3 decimal places.

### Q27
Differentiate, using the chain rule on $\text{e}^{-3x}$ and the standard derivative of $\text{ln}  x$

$\frac{\text{d}y}{\text{d}x} = - 3 \text{e}^{-3x} + \frac{1}{x}$

**[M1 A1]**

Find the gradient of the tangent by substituting $x = 1$

$\frac{\text{d}y}{\text{d}x} = - 3 \text{e}^{-3(1)} + \frac{1}{1} = 1 - 3 \text{e}^{-3}$

The normal is perpendicular to the tangent, so take the negative reciprocal

$m_{\text{normal}} = - \frac{1}{1-3\text{e}^{-3}}$

**[M1]**

**Final answer:** $m_{\text{normal}} = - 1 . 176$** (3 d.p.)**

**[A1]**

> **[mark-scheme]**
> **M1**: Differentiates the curve, using the chain rule on $\text{e}^{-3x}$ to obtain a term $k \text{e}^{-3x}$ and $\frac{1}{x}$ from $\text{ln}  x$.
> 
> **A1**: For $\frac{\text{d}y}{\text{d}x} = - 3 \text{e}^{-3x} + \frac{1}{x}$.
> 
> **M1**: Substitutes $x = 1$ to find the tangent gradient $1 - 3 \text{e}^{-3}$, then takes the negative reciprocal for the normal.
> 
> **A1**: For $- 1 . 176$ (answers which round to this to 3 decimal places).

### Q28
(i)

Differentiate each term using its standard derivative

`\dfrac{\text{d}}{\text{d}x}\left(4\text{cos} \; x - 3\text{sin} \; x\right)`

$= - 4 \text{sin}  x - 3 \text{cos}  x$

**[B1 B1]**

(ii)

Apply the product rule, `\dfrac{\text{d}}{\text{d}x}\left(uv\right) = u\dfrac{\text{d}v}{\text{d}x} + v\dfrac{\text{d}u}{\text{d}x}`

$u = \text{e}^{x} ,  v = \text{ln}  x$

$\frac{\text{d}u}{\text{d}x} = \text{e}^{x} ,  \frac{\text{d}v}{\text{d}x} = \frac{1}{x}$

Substitute these into the product rule

`\dfrac{\text{d}y}{\text{d}x} = \text{e}^{x}\cdot\dfrac{1}{x} + \text{ln} \; x \cdot \text{e}^{x}`

**[M1]**

Factor out $\text{e}^{x}$

`\dfrac{\text{d}y}{\text{d}x} = \text{e}^{x}\left(\dfrac{1}{x} + \text{ln} \; x\right)`

**[A1]**

(iii)

Apply the quotient rule, `\dfrac{\text{d}}{\text{d}x}\left(\dfrac{u}{v}\right) = \dfrac{v\dfrac{\text{d}u}{\text{d}x} - u\dfrac{\text{d}v}{\text{d}x}}{v^{2}}`

$u = \text{tan}  x ,  v = x$

$\frac{\text{d}u}{\text{d}x} = \text{sec}^{2}  x ,  \frac{\text{d}v}{\text{d}x} = 1$

Substitute these into the quotient rule

$\frac{\text{d}y}{\text{d}x} = \frac{x\text{sec}^{2}x-\text{tan}x}{x^{2}}$

**[M1 A1]**

(iv)

Apply the chain rule, $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$, with $u = x^{2} - 7 x + 1$

$y = \text{cos}  u ,  \frac{\text{d}y}{\text{d}u} = - \text{sin}  u$

$u = x^{2} - 7 x + 1 ,  \frac{\text{d}u}{\text{d}x} = 2 x - 7$

Substitute these into the chain rule

`\dfrac{\text{d}y}{\text{d}x} = -\text{sin} \; u\left(2x - 7\right) = \left(7 - 2x\right)\text{sin} \; u`

**[M1]**

Substitute $u = x^{2} - 7 x + 1$ back in

`\dfrac{\text{d}y}{\text{d}x} = \left(7 - 2x\right)\text{sin}\left(x^{2} - 7x + 1\right)`

**[A1]**

> **[mark-scheme]**
> **B1**: For $- 4 \text{sin}  x$ as the derivative of $4 \text{cos}  x$.
> 
> **B1**: For $- 3 \text{cos}  x$ as the derivative of $- 3 \text{sin}  x$.
> 
> **M1**: Correct use of the product rule in part (ii), with $u = \text{e}^{x}$, $v = \text{ln}  x$ and both derivatives correct.
> 
> **A1**: For `\text{e}^{x}\left(\dfrac{1}{x} + \text{ln} \; x\right)`, or the unfactored equivalent.
> 
> **M1**: Correct use of the quotient rule in part (iii), with $u = \text{tan}  x$ and $v = x$.
> 
> **A1**: For $\frac{x\text{sec}^{2}x-\text{tan}x}{x^{2}}$.
> 
> **M1**: Correct use of the chain rule in part (iv), giving `-\text{sin}\left(x^{2} - 7x + 1\right)` multiplied by $2 x - 7$.
> 
> **A1**: For `\left(7 - 2x\right)\text{sin}\left(x^{2} - 7x + 1\right)`, or equivalent such as `-\left(2x - 7\right)\text{sin}\left(x^{2} - 7x + 1\right)`.

### Q29
Apply the product rule, $\text{f} ' ( x ) = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$, with $v = \text{ln} ( x + 3 )$ differentiated by the chain rule

$u = x^{2} - 1 ,  v = \text{ln} ( x + 3 )$

$\frac{\text{d}u}{\text{d}x} = 2 x ,  \frac{\text{d}v}{\text{d}x} = \frac{1}{x+3}$

**[B1 B1]**

Substitute these into the product rule

`\text{f}'(x) = \left(x^{2} - 1\right)\dfrac{1}{x + 3} + \text{ln}(x + 3)\cdot 2x`

**[M1]**

$\text{f} ' ( x ) = \frac{x^{2}-1}{x+3} + 2 x  \text{ln} ( x + 3 )$

**[A1]**

> **[mark-scheme]**
> **B1**: For $\frac{\text{d}u}{\text{d}x} = 2 x$.
> 
> **B1**: For $\frac{\text{d}v}{\text{d}x} = \frac{1}{x+3}$.
> 
> **M1**: Correct use of the product rule structure with their two derivatives.
> 
> **A1**: For $\text{f} ' ( x ) = \frac{x^{2}-1}{x+3} + 2 x  \text{ln} ( x + 3 )$.
At $A$ the curve meets the $x$-axis, so set $\text{f} ( x ) = 0$

`\left(x^{2} - 1\right)\text{ln}(x + 3) = 0`

A product is zero when a factor is zero, so consider each factor in turn

$x^{2} - 1 = 0$* or *$\text{ln} ( x + 3 ) = 0$

Solve each factor

$x = \pm 1$* *

*or *$x + 3 = 1 \Rightarrow x = - 2$

**[M1]**

The three intersections are at $x = - 2 , - 1 , 1$. Point $A$ is the furthest to the left, so it has the most negative $x$-coordinate

$A = ( - 2 , 0 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Sets $\text{f} ( x ) = 0$ and solves each factor, obtaining $x = - 2$ from $\text{ln} ( x + 3 ) = 0$ (and $x = \pm 1$).
> 
> **A1**: Identifies $A$ as the left-most intersection, so $A = ( - 2 , 0 )$. Because the point is given, both routes to zero must be shown.
Find the gradient at $A$ by substituting $x = - 2$ into $\text{f} ' ( x )$, using $\text{ln}  1 = 0$

$m = \text{f} ' ( - 2 ) = \frac{(-2)^{2}-1}{-2+3} + 2 ( - 2 ) \text{ln} ( - 2 + 3 ) = \frac{3}{1} + 0 = 3$

**[M1 A1]**

Use the point-gradient form $y - y_{1} = m ( x - x_{1} )$ with $m = 3$ and $( x_{1} , y_{1} ) = ( - 2 , 0 )$

$y - 0 = 3 ( x + 2 )$

$y = 3 x + 6$

**[A1]**

> **[mark-scheme]**
> **M1**: Substitutes $x = - 2$ into their $\text{f} ' ( x )$, using $\text{ln}  1 = 0$.
> 
> **A1**: For the gradient $m = 3$.
> 
> **A1**: For the tangent equation $y = 3 x + 6$.

### Q30
Apply the quotient rule, $\frac{\text{d}y}{\text{d}x} = \frac{v\frac{\text{d}u}{\text{d}x}-u\frac{\text{d}v}{\text{d}x}}{v^{2}}$, differentiating $v = \text{sin}  2 x$ by the chain rule

$u = 5 x^{7} ,  v = \text{sin}  2 x$

$\frac{\text{d}u}{\text{d}x} = 35 x^{6} ,  \frac{\text{d}v}{\text{d}x} = 2 \text{cos}  2 x$

Substitute these into the quotient rule

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{sin} \; 2x \cdot 35x^{6} - 5x^{7}\cdot 2\text{cos} \; 2x}{\left(\text{sin} \; 2x\right)^{2}}`

**[M1]**

Simplify

$\frac{\text{d}y}{\text{d}x} = \frac{35x^{6}\text{sin}2x-10x^{7}\text{cos}2x}{\text{sin}^{2}2x}$

**[A1 A1]**

> **[mark-scheme]**
> **M1**: Correct use of the quotient rule structure, with $u = 5 x^{7}$, $v = \text{sin}  2 x$ and the two derivatives substituted.
> 
> **A1**: Both derivatives correct, including $2 \text{cos}  2 x$ from the chain rule.
> 
> **A1**: For $\frac{35x^{6}\text{sin}2x-10x^{7}\text{cos}2x}{\text{sin}^{2}2x}$, or an equivalent unsimplified form.

### Q31
Differentiate term by term, applying the chain rule to each

For the first term the outer function is $\text{cos}$ and the inner is $x^{2} - 3 x + 7$

`\dfrac{\text{d}}{\text{d}x}\text{cos}\left(x^{2} - 3x + 7\right) = -\text{sin}\left(x^{2} - 3x + 7\right)\times(2x - 3)`

**[M1 A1]**

For the second term the outer function is $\text{sin}$ and the inner is $\text{e}^{x}$

`\dfrac{\text{d}}{\text{d}x}\text{sin}\left(\text{e}^{x}\right) = \text{cos}\left(\text{e}^{x}\right)\times\text{e}^{x}`

**[M1 A1]**

Add the two derivatives

`\dfrac{\text{d}y}{\text{d}x} = -(2x - 3)\text{sin}\left(x^{2} - 3x + 7\right) + \text{e}^{x}\text{cos}\left(\text{e}^{x}\right)`

> **[mark-scheme]**
> **M1**: Correct use of the chain rule on `\text{cos}\left(x^{2} - 3x + 7\right)`, giving `-\text{sin}\left(x^{2} - 3x + 7\right)` times the inner derivative.
> 
> **A1**: For `-(2x - 3)\text{sin}\left(x^{2} - 3x + 7\right)`.
> 
> **M1**: Correct use of the chain rule on `\text{sin}\left(\text{e}^{x}\right)`, giving `\text{cos}\left(\text{e}^{x}\right)` times the inner derivative.
> 
> **A1**: For `\text{e}^{x}\text{cos}\left(\text{e}^{x}\right)`, and hence the correct sum.
Apply the chain rule, $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$, with $u = 2 x^{3}$

$y = \text{ln}  u ,  \frac{\text{d}y}{\text{d}u} = \frac{1}{u}$

$u = 2 x^{3} ,  \frac{\text{d}u}{\text{d}x} = 6 x^{2}$

Substitute these in, then simplify

$\frac{\text{d}y}{\text{d}x} = \frac{1}{2x^{3}} \times 6 x^{2} = \frac{6x^{2}}{2x^{3}}$

**[M1]**

$\frac{\text{d}y}{\text{d}x} = \frac{3}{x}$

**[A1]**

Alternatively, simplify first with the laws of logarithms, `\text{ln}\left(2x^{3}\right) = \text{ln} \; 2 + 3\text{ln} \; x`, so differentiating gives $\frac{3}{x}$ directly

> **[mark-scheme]**
> **M1**: Correct use of the chain rule with $u = 2 x^{3}$, or simplifying via log laws to $\text{ln}  2 + 3 \text{ln}  x$.
> 
> **A1**: For $\frac{3}{x}$, correctly simplified.

### Q32
Write $\text{cosec}  2 x$ as a fraction so the quotient rule applies

$y = \text{cosec}  2 x = \frac{1}{\text{sin}2x}$

**[B1]**

Apply the quotient rule, $\frac{\text{d}y}{\text{d}x} = \frac{v\frac{\text{d}u}{\text{d}x}-u\frac{\text{d}v}{\text{d}x}}{v^{2}}$, with $u = 1$ and $v = \text{sin}  2 x$

$u = 1 ,  v = \text{sin}  2 x$

$\frac{\text{d}u}{\text{d}x} = 0 ,  \frac{\text{d}v}{\text{d}x} = 2 \text{cos}  2 x$

Substitute these into the quotient rule

`\dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{sin} \; 2x \cdot 0 - 1\cdot 2\text{cos} \; 2x}{\left(\text{sin} \; 2x\right)^{2}} = \dfrac{-2\text{cos} \; 2x}{\left(\text{sin} \; 2x\right)^{2}}`

**[M1 A1]**

Split the fraction, using $\frac{\text{cos}2x}{\text{sin}2x} = \text{cot}  2 x$ and $\frac{1}{\text{sin}2x} = \text{cosec}  2 x$

`\dfrac{\text{d}y}{\text{d}x} = -2\cdot\dfrac{\text{cos} \; 2x}{\text{sin} \; 2x}\cdot\dfrac{1}{\text{sin} \; 2x}`

**[M1]**

$\frac{\text{d}y}{\text{d}x} = - 2 \text{cosec}  2 x  \text{cot}  2 x$

**[A1]**

> **[mark-scheme]**
> **B1**: Writes $y = \frac{1}{\text{sin}2x}$, ready to apply the quotient rule.
> 
> **M1**: Correct use of the quotient rule with $u = 1$, $v = \text{sin}  2 x$, $\frac{\text{d}u}{\text{d}x} = 0$ and $\frac{\text{d}v}{\text{d}x} = 2 \text{cos}  2 x$.
> 
> **A1**: For `\dfrac{-2\text{cos} \; 2x}{\left(\text{sin} \; 2x\right)^{2}}`, or equivalent.
> 
> **M1**: Rewrites in terms of $\text{cosec}  2 x$ and $\text{cot}  2 x$, using $\frac{\text{cos}2x}{\text{sin}2x} = \text{cot}  2 x$ and $\frac{1}{\text{sin}2x} = \text{cosec}  2 x$.
> 
> **A1**: Reaches the given result $- 2 \text{cosec}  2 x  \text{cot}  2 x$. Because the answer is given, the working must be visible.
Substitute $x = \frac{π}{3}$, using the exact values $\text{cosec}  \frac{2π}{3} = \frac{2}{\sqrt{3}}$ and $\text{cot}  \frac{2π}{3} = - \frac{1}{\sqrt{3}}$

`\dfrac{\text{d}y}{\text{d}x} = -2\left(\dfrac{2}{\sqrt{3}}\right)\left(-\dfrac{1}{\sqrt{3}}\right)`

$\frac{\text{d}y}{\text{d}x} = \frac{4}{3}$

**[B1]**

> **[mark-scheme]**
> **B1**: For a gradient of $\frac{4}{3}$, using exact values of the trigonometric functions at $\frac{2π}{3}$.

### Q33
Differentiate using the chain rule, $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$, with $u = 3 x^{2} + 5 x - 2$

$y = \text{e}^{u} ,  \frac{\text{d}y}{\text{d}u} = \text{e}^{u}$

$u = 3 x^{2} + 5 x - 2 ,  \frac{\text{d}u}{\text{d}x} = 6 x + 5$

Substitute these into the chain rule

$\frac{\text{d}y}{\text{d}x} = ( 6 x + 5 ) \text{e}^{3x^{2}+5x-2}$

**[M1 A1]**

Find the gradient of the tangent by substituting $x = - 2$

`\dfrac{\text{d}y}{\text{d}x} = \left(6(-2) + 5\right)\text{e}^{3(-2)^{2} + 5(-2) - 2} = -7\text{e}^{0} = -7`

**[M1]**

Use the point-gradient form $y - y_{1} = m ( x - x_{1} )$ with $m = - 7$ and $( x_{1} , y_{1} ) = ( - 2 , 1 )$

$y - 1 = - 7 ( x + 2 )$

$y - 1 = - 7 x - 14$

$7 x + y + 13 = 0$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the chain rule, giving a result of the form $( 6 x + 5 ) \text{e}^{3x^{2}+5x-2}$.
> 
> **A1**: For $\frac{\text{d}y}{\text{d}x} = ( 6 x + 5 ) \text{e}^{3x^{2}+5x-2}$.
> 
> **M1**: Substitutes $x = - 2$ into their $\frac{\text{d}y}{\text{d}x}$, using $\text{e}^{0} = 1$ to find the gradient $- 7$, and applies the point-gradient form.
> 
> **A1**: For $7 x + y + 13 = 0$, or any integer multiple of this equation.

### Q34
Apply the product rule, $\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$

$u = 4 \text{cos}  x - 3 \text{sin}  x ,  v = \text{e}^{3x-5}$

$\frac{\text{d}u}{\text{d}x} = - 4 \text{sin}  x - 3 \text{cos}  x ,  \frac{\text{d}v}{\text{d}x} = 3 \text{e}^{3x-5}$

Substitute these into the product rule

`\dfrac{\text{d}y}{\text{d}x} = \left(4\text{cos} \; x - 3\text{sin} \; x\right)3\text{e}^{3x - 5} + \text{e}^{3x - 5}\left(-4\text{sin} \; x - 3\text{cos} \; x\right)`

**[M1 A1]**

Factor out $\text{e}^{3x-5}$ and collect like terms

`= \text{e}^{3x - 5}\left(12\text{cos} \; x - 9\text{sin} \; x - 4\text{sin} \; x - 3\text{cos} \; x\right)`

`\dfrac{\text{d}y}{\text{d}x} = \text{e}^{3x - 5}\left(9\text{cos} \; x - 13\text{sin} \; x\right)`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the product rule, with $u = 4 \text{cos}  x - 3 \text{sin}  x$, $v = \text{e}^{3x-5}$ and both derivatives correct.
> 
> **A1**: For a correct unsimplified derivative.
> 
> **A1**: For the simplified form `\text{e}^{3x - 5}\left(9\text{cos} \; x - 13\text{sin} \; x\right)`.
Apply the product rule, $\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$

$u = x^{3} - 4 x^{2} + 7 ,  v = \text{ln}  x$

$\frac{\text{d}u}{\text{d}x} = 3 x^{2} - 8 x ,  \frac{\text{d}v}{\text{d}x} = \frac{1}{x}$

Substitute these into the product rule

`\dfrac{\text{d}y}{\text{d}x} = \left(x^{3} - 4x^{2} + 7\right)\dfrac{1}{x} + \text{ln} \; x\left(3x^{2} - 8x\right)`

**[M1 A1]**

Simplify the first term, since $\frac{x^{3}-4x^{2}+7}{x} = x^{2} - 4 x + \frac{7}{x}$

`\dfrac{\text{d}y}{\text{d}x} = x^{2} - 4x + \dfrac{7}{x} + \left(3x^{2} - 8x\right)\text{ln} \; x`

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the product rule, with $u = x^{3} - 4 x^{2} + 7$ and $v = \text{ln}  x$.
> 
> **A1**: For a correct unsimplified derivative.
> 
> **A1**: For the simplified form `x^{2} - 4x + \dfrac{7}{x} + \left(3x^{2} - 8x\right)\text{ln} \; x`.

### Q35
The derivative of $\text{tan}^{-1} x$ is $\frac{1}{1+x^{2}}$, given in the List of Formulae. Apply the chain rule, $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$, with $u = a x$

$y = \text{tan}^{-1} u ,  \frac{\text{d}y}{\text{d}u} = \frac{1}{1+u^{2}}$

$u = a x ,  \frac{\text{d}u}{\text{d}x} = a$

Substitute these into the chain rule

$\frac{\text{d}}{\text{d}x} \text{tan}^{-1} ( a x ) = \frac{1}{1+(ax)^{2}} \times a$

**[M1]**

$\frac{\text{d}}{\text{d}x} \text{tan}^{-1} ( a x ) = \frac{a}{1+a^{2}x^{2}}$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the chain rule with $u = a x$, multiplying the given derivative $\frac{1}{1+u^{2}}$ by $a$.
> 
> **A1**: For $\frac{a}{1+a^{2}x^{2}}$.
Stationary points occur where $\frac{\text{d}y}{\text{d}x} = 0$. Using part (a) with $a = 3$

$\frac{\text{d}y}{\text{d}x} = \frac{3}{1+9x^{2}} = 0$

**[M1]**

The numerator is $3$, which is never zero, and the denominator $1 + 9 x^{2}$ is always positive, so the derivative can never equal zero

**Final answer:** **The curve has no stationary points**

**[A1]**

> **[mark-scheme]**
> **M1**: Sets the derivative (with $a = 3$) equal to zero: $\frac{3}{1+9x^{2}} = 0$.
> 
> **A1**: Concludes there are no stationary points, justified by the numerator being non-zero (or the fraction never being zero).
