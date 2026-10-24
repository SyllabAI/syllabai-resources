# Mark Schemes — Differentiation
**Calculus** · Cambridge (CIE) IGCSE further-maths (0606)


## Exam Questions (32 questions)


### Q1
> *In general, the approximate change in *$y$* as *$x$* increases from *$a$* to *$a+h$* where *$h$* is small is *$\frac{dy}{dx}\timesh$* where *$\frac{dy}{dx}$* is at *$x=a$

> *Substitute *$a=-1$* and *$h=k$* into the expression above*

$\frac{dy}{dx}\timesk$* where *$\frac{dy}{dx}$* is at *$x=-1$

> *Find *$\frac{dy}{dx}$* using the chain rule, *$\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}$* where *$u=1+x^{4}$

$\begin{gathered} y = \ln u u = 1 + x^{4} \\ \frac{ \mathrm{d} y}{ \mathrm{d} u} & = \frac{1}{u} \frac{ \mathrm{d} u}{ \mathrm{d} x} = 4 x^{3} \end{gathered}$

> *This gives*

$\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{1}{u} \times 4 x^{3} \\ = \frac{1}{1 + x^{4} } \times 4 x^{3} \\ = \frac{4 x^{3}}{1 + x^{4} } \end{gathered}$

**[M1 A1]**

> *Substitute *$x=-1$* into *$\frac{dy}{dx}$

$\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{4 ( - 1 )^{3}}{1 + ( - 1 )^{4} } = - 2 \end{gathered}$

**[M1]**

> *Substitute *$\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} \end{gathered} = - 2$* into *$\frac{dy}{dx}\timesk$

$-2k$

**[A1]**

> **[mark-scheme]**
> **M1: **For having $\frac{1}{1+x^{4}}$ in your expression for $\frac{dy}{dx}$.
> 
> **A1: **For the fully correct expression for $\frac{dy}{dx}$.
> 
> **M1:** For substituting $x=-1$ into your expression for $\frac{dy}{dx}$.
> 
> **A1: **For $-2k$ as the final answer.

### Q2
> *The formula for the length of the arc in radians is *$rθ$

> *Find an expression for the total perimeter and set it equal to 4*

$\begin{gathered} r + r \\theta + r & = 4 \\ 2 r + r \\theta & = 4 \textcircled{1} \end{gathered}$

**[B1]**

> **[mark-scheme]**
> This mark is for any correct perimeter equation that uses 4 and $rθ$.

> *The formula for the area of the arc in radians is *$\frac{1}{2}r^{2}θ$

> *Find an expression for the area *$A$

$A = 1 \frac{1}{2} r^{2} \\theta \begin{gathered} \end{gathered} \begin{gathered} \end{gathered} \begin{gathered} \end{gathered} \begin{gathered} \end{gathered} \begin{gathered} \end{gathered} \begin{gathered} \end{gathered} \begin{gathered} \end{gathered} \begin{gathered} \end{gathered} \begin{gathered} \end{gathered} \begin{gathered} \end{gathered} \begin{gathered} \textcircled{2} \end{gathered}$

> *Eliminate *$r$*, e.g. make *$r$* the subject of equation 1 by first factorising it out*

$\begin{gathered} r ( 2 + \\theta ) & = 4 \\ r = \frac{4}{2 + \\theta } \end{gathered}$

**[M1]**

> *Then substitute this into equation 2*

$A = 1 \frac{1}{2} ( \frac{4}{2 + \\theta } )^{2} \times \\theta$

> *Simplify*

$A = 1 \frac{1}{2} \times \frac{16}{( 2 + \\theta )^{2}} \times \\theta$

$A = \frac{8 \\theta }{( 2 + \\theta )^{2}}$

**[A1]**

> **[mark-scheme]**
> The last mark is for showing the steps that get you from the substitution of $r$ into $A$ to the answer given (not for writing out the "show that" answer).
> *To differentiate *$A = \frac{8 \\theta }{( 2 + \\theta )^{2}}$* you need the quotient rule*

> *Substitute *$u=8θ$* and *$v = ( 2 + \\theta )^{2}$* into *$\frac{dA}{dθ}=\frac{v\frac{du}{dx}-u\frac{dv}{dx}}{v^{2}}$

> *You can use the chain rule to differentiate *$v = ( 2 + \\theta )^{2}$* (or expand the brackets then differentiate)*

$\begin{gathered} \frac{ \mathrm{d} v}{ \mathrm{d} x} & = 2 ( 2 + \\theta )^{1} \times 1 \\ = 2 ( 2 + \\theta ) \end{gathered}$

> *The quotient rule gives*

$\frac{ \mathrm{d} A}{ \mathrm{d} \\theta } = \frac{( 2 + \\theta )^{2} ( 8 ) - 8 \\theta \times 2 ( 2 + \\theta )}{[ ( 2 + \\theta )^{2} ]^{2}}$

**[M1 A1]**

> *Factorise out a *$( 2 + \\theta )$* from top and bottom of the fraction, then cancel*

`| ( d A)/( d theta) | = (8 ( 2 + theta ) ^2 - 16 theta ( 2 + theta ))/(( 2 + theta ) ^ 4) | | _ = (( 2 + theta ) [ 8 ( 2 + theta ) - 16 theta ])/(( 2 + theta ) ^ 4) | | _ = (/ ( 2 + theta ) [ 8 ( 2 + theta ) - 16 theta ])/(( 2 + theta ) ^ / 4 ^3) | | _ = (8 ( 2 + theta ) - 16 theta)/(( 2 + theta ) ^3) | |`

> *Write this in the form *$\frac{ \mathrm{d} A}{ \mathrm{d} \\theta } = \frac{p ( q - \\theta )}{( \\theta + 2 )^{3}}$* by simplifying and factorising the numerator*

$\begin{gathered} \frac{ \mathrm{d} A}{ \mathrm{d} \\theta } & = \frac{16 + 8 \\theta - 16 \\theta }{( 2 + \\theta )^{3}} \\ = \frac{16 - 8 \\theta }{( 2 + \\theta )^{3}} \\ = \frac{8 ( 2 - \\theta )}{( 2 + \\theta )^{3}} \end{gathered}$

$\begin{gathered} \frac{ \mathrm{d} A}{ \mathrm{d} \\theta } & = \frac{8 ( 2 - \\theta )}{( 2 + \\theta )^{3}} \end{gathered}$

**[A1]**
> *For the area to be at its maximum point, *$\frac{dA}{dθ}=0$

$\begin{gathered} \frac{8 ( 2 - \\theta )}{( 2 + \\theta )^{3}} & = 0 \end{gathered}$

> *This means the numerator must be equal to zero (then solve for *$θ$*)*

$\begin{gathered} 8 ( 2 - \\theta ) & = 0 \\ \\theta = 2 \end{gathered}$

**[B1]**

> *This is the angle, not the area, so substitute *$θ=2$* into *$A$

$\begin{gathered} A = \frac{8 \times 2}{( 2 + 2 )^{2}} \\ = \frac{16}{4^{2}} \\ = 1 \end{gathered}$

**[B1]**

> *This area, *$A=1$*, could be a maximum area or a minimum area*

**Method 1**

> *You can use a second-derivative test to show it is a maximum area*

> *Substitute *$u = 8 ( 2 - \\theta ) = 16 - 8 \\theta$* and *$v = ( 2 + \\theta )^{3}$* into the quotient rule (using the chain rule to find *$\frac{dv}{dx}$*)*

$\frac{ \mathrm{d}^{2} A}{ \mathrm{d} \\theta ^{2}} = \frac{( 2 + \\theta )^{3} ( - 8 ) - 8 ( 2 - \\theta ) \times 3 ( 2 + \\theta )^{2} \times 1}{[ ( 2 + \\theta )^{3} ]^{2}}$

> *No major simplifying is needed as you can now substitute *$θ=2$* into the messy  result and check the sign*

$\begin{gathered} \frac{ \mathrm{d}^{2} A}{ \mathrm{d} \\theta ^{2}} & = \frac{( 2 + 2 )^{3} ( - 8 ) - 8 \times 0}{[ ( 2 + 2 )^{3} ]^{2}} \\ = \frac{4^{3} ( - 8 )}{( 4^{3} )^{2}} \\ = - \frac{8}{4^{3}} < 0 \end{gathered}$

> *The second derivative is negative at *$θ=2$* so *$A=1$* is a maximum area*

**Final answer:** **The area of 1 square unit is a maximum area as **$\frac{d^{2}A}{dθ^{2}}<0$** at **$θ=2$

**[M1 A1]**

> **[mark-scheme]**
> **M1:** For attempting to find the second derivative using the quotient rule.
> 
> **A1: **For correctly showing that the second derivative is negative at $θ=2$ (no formal conclusion sentence needed).

**Method 2**

> *You can use a gradient test either side of *$θ=2$* to show it is a maximum area*

> *Substitute, for example, *$θ=1.9$* into *$\frac{dA}{dθ}$* and just look at its sign (no big simplifications are needed)*

$\begin{gathered} \frac{ \mathrm{d} A}{ \mathrm{d} \\theta } & = \frac{8 ( 2 - 1.9 )}{( 2 + 1.9 )^{3}} = \frac{8 \times 0.1}{( 3.9 )^{3}} > 0 \end{gathered}$

> *Substitute, for example, *$θ=2.1$* into *$\frac{dA}{dθ}$* and again just look at its sign*

$\begin{gathered} \frac{ \mathrm{d} A}{ \mathrm{d} \\theta } & = \frac{8 ( 2 - 2.1 )}{( 2 + 2.1 )^{3}} = \frac{8 \times ( - 0.1 )}{( 4.1 )^{3}} = - \frac{8 \times 0.1}{( 4.1 )^{3}} < 0 \end{gathered}$

**Final answer:** **The area of 1 square unit is a maximum area as the gradient **$\frac{dA}{dθ}$** goes from positive to negative**

**[M1 A1]**

> **[mark-scheme]**
> **M1:** For an attempt to find the value of $\frac{dA}{dθ}$ either side of $θ=2$.
> 
> **A1: **For correctly showing that the gradient goes from positive to negative from left of $θ=2$ to right of $θ=2$ (no formal conclusion sentence needed).

### Q3
> *Differentiate *$y = \mathrm{e}^{( 4 x - x^{2} )}$* using the chain rule*

> *i.e. substitute *$y=e^{u}$* and *$u=4x-x^{2}$* into *$\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}$

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \mathrm{e}^{u} \times ( 4 - 2 x )$

**[M1]**

> **[mark-scheme]**
> This mark is for attempting to use the chain rule.

> *Substitute back in *$u=4x-x^{2}$* to get the first derivative in *$x$

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( 4 - 2 x ) \mathrm{e}^{( 4 x - x^{2} )}$

> *Factorise out 2 from the first bracket*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = 2 ( 2 - x ) \mathrm{e}^{( 4 x - x^{2} )}$

**[A1]**
> *The first derivative from part (a) says that if *$y = \mathrm{e}^{( 4 x - x^{2} )}$* then*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = 2 ( 2 - x ) \mathrm{e}^{( 4 x - x^{2} )}$

> *Reverse the process to go from the first derivative back to the equation of the curve*

$\int 2 ( 2 - x ) \mathrm{e}^{( 4 x - x^{2} )} \mathrm{d} x = \mathrm{e}^{( 4 x - x^{2} )} + c$

> *The integral in the question is almost the same as this, but needs rearranging first*

$\begin{gathered} \int \frac{( 2 - x ) \mathrm{e}^{4 x} }{ \mathrm{e}^{x^{2}} } \mathrm{d} x & = \int ( 2 - x ) \mathrm{e}^{4 x - x^{2}} \mathrm{d} x \\ = 1 \frac{1}{2} \int 2 ( 2 - x ) \mathrm{e}^{4 x - x^{2}} \mathrm{d} x \end{gathered}$

> *Now substitute the reversed integral from above into the right-hand side here*

$\begin{gathered} \int \frac{( 2 - x ) \mathrm{e}^{4 x} }{ \mathrm{e}^{x^{2}} } \mathrm{d} x & = 1 \frac{1}{2} [ \mathrm{e}^{( 4 x - x^{2} )} + c ] \end{gathered}$

> *Expand (you can rename the unknown constant *$\frac{1}{2}c$* as *$c$* again)*

$\begin{gathered} \int \frac{( 2 - x ) \mathrm{e}^{4 x} }{ \mathrm{e}^{x^{2}} } \mathrm{d} x & = 1 \frac{1}{2} \mathrm{e}^{( 4 x - x^{2} )} + c \end{gathered}$

**[B1 B1]**

> **[mark-scheme]**
> **B1:** For at least $\frac{1}{2}e^{4x-x^{2}}$ (may not have $+c$).
> 
> **B1:** For $\frac{1}{2}e^{4x-x^{2}}+c$ (must have$+c$).

> **[exam-tip]**
> Always add $+c$ to your answers to indefinite integrals, otherwise you will lose a mark!
> *Differentiate *$\frac{ \mathrm{d} y}{ \mathrm{d} x} = 2 ( 2 - x ) \mathrm{e}^{( 4 x - x^{2} )}$* again to get *$\frac{d^{2}y}{dx^{2}}$* but this time using the product rule *$\frac{du}{dx}v+u\frac{dv}{dx}$

> *First find the derivatives of *$u = 2 ( 2 - x ) = 4 - 2 x$* and *$v = \mathrm{e}^{( 4 x - x^{2} )}$*  (note that *$\frac{dv}{dx}$*is the answer to part (a))*

$\frac{ \mathrm{d} u}{ \mathrm{d} x} = - 2
 \frac{ \mathrm{d} v}{ \mathrm{d} x} = 2 ( 2 - x ) \mathrm{e}^{( 4 x - x^{2} )}$

> *Then substitute these into *$\frac{d^{2}y}{dx^{2}}=\frac{du}{dx}v+u\frac{dv}{dx}$

$\frac{ \mathrm{d}^{2} y}{ \mathrm{d} x^{2}} = ( - 2 ) \times \mathrm{e}^{( 4 x - x^{2} )} + ( 4 - 2 x ) \times [ 2 ( 2 - x ) \mathrm{e}^{( 4 x - x^{2} )} ]$

**[M1]**

> **[mark-scheme]**
> This mark is for attempting to use the product rule.

> *Simplify*

$\frac{ \mathrm{d}^{2} y}{ \mathrm{d} x^{2}} = - 2 \mathrm{e}^{( 4 x - x^{2} )} + 4 ( 2 - x ) ( 2 - x ) \mathrm{e}^{( 4 x - x^{2} )}$

**[A1]**

> **[mark-scheme]**
> This mark is for the correct result after using the product rule (it can be unsimplified and messy).

> *Factorise out *$\mathrm{e}^{( 4 x - x^{2} )}$* because the answer must be written in the form *$( p + q x + r x^{2} ) y$* and *$y = \mathrm{e}^{( 4 x - x^{2} )}$

$\frac{ \mathrm{d}^{2} y}{ \mathrm{d} x^{2}} = [ - 2 + 4 ( 2 - x ) ( 2 - x ) ] \mathrm{e}^{( 4 x - x^{2} )}$

**[M1]**

> *Expand and simplify inside the brackets*

$\begin{gathered} \frac{ \mathrm{d}^{2} y}{ \mathrm{d} x^{2}} & = ( - 2 + 4 ( 4 - 4 x + x^{2} ) ) \mathrm{e}^{( 4 x - x^{2} )} \\ = ( - 2 + 16 - 16 x + 4 x^{2} ) \mathrm{e}^{( 4 \mathrm{x} - \mathrm{x}^{2} )} \\ = ( 14 - 16 x + 4 x^{2} ) \mathrm{e}^{( 4 x - x^{2} )} \end{gathered}$

> *The result is meant to have the form *$\frac{ \mathrm{d}^{2} y}{ \mathrm{d} x^{2}} = ( p + q x + r x^{2} ) y$

> *This is true, as *$y = \mathrm{e}^{( 4 x - x^{2} )}$

$\frac{ \mathrm{d}^{2} y}{ \mathrm{d} x^{2}} = ( 14 - 16 x + 4 x^{2} ) y$

**[A1]**

### Q4
> *The volume of a sphere is given in the exam*

$V=\frac{4}{3}πr^{3}$

> *This question requires connect rates of change (an application of the chain rule)*

$\frac{dV}{dt}=\frac{dV}{dr}\times\frac{dr}{dt}$

> *Find *$\frac{dV}{dr}$* by differentiating *$V=\frac{4}{3}πr^{3}$

$\begin{gathered} \frac{ \mathrm{d} V}{ \mathrm{d} r} & = \frac{4}{3} \pi ( 3 r^{2} ) \\ = 4 \pi r^{2} \end{gathered}$

**[B1]**

> *You know *$\frac{dV}{dt}=24$* from the question *

> *Substitute *$\frac{dV}{dt}=24$* and *$\begin{gathered} \frac{ \mathrm{d} V}{ \mathrm{d} r} & = 4 \pi r^{2} \end{gathered}$* into *$\frac{dV}{dt}=\frac{dV}{dr}\times\frac{dr}{dt}$

$24=4πr^{2}\times\frac{dr}{dt}$

**[M1]**

> **[mark-scheme]**
> This mark is for using a correct connected rate formula, e.g.  $\frac{dV}{dt}=\frac{dV}{dr}\times\frac{dr}{dt}$ or $\frac{dr}{dt}=\frac{dr}{dV}\times\frac{dV}{dt}$, with at least one correct substitution into the formula.

> *The question wants you to find *$\frac{dr}{dt}$* so make *$\frac{dr}{dt}$* the subject*

$\begin{gathered} \frac{ \mathrm{d} r}{ \mathrm{d} t} & = \frac{24}{4 \pi r^{2}} \\ = \frac{6}{\pi r^{2}} \end{gathered}$

> *You need the value of *$\frac{dr}{dt}$* when *$V=\frac{32π}{3}$* but *$\frac{dr}{dt}$* is in terms of *$r$* not *$V$

> *Use *$V=\frac{4}{3}πr^{3}$* to find *$r$* when *$V=\frac{32π}{3}$

$\begin{gathered} \frac{32 \pi }{3} & = \frac{4}{3} \pi r^{3} \\ 32 \pi & = 4 \pi r^{3} \\ 8 = r^{3} \\ r = 2 \end{gathered}$

**[A1]**

> *Substitute *$r=2$* into *$\frac{dr}{dt}$

$\begin{gathered} \frac{ \mathrm{d} r}{ \mathrm{d} t} & = \frac{6}{\pi ( 2 )^{2}} \\ = \frac{6}{4 \pi } \\ = \frac{3}{2 \pi } \end{gathered}$

> *The units are cm for *$r$* and seconds for *$t$*, so cm/s for *$\frac{dr}{dt}$

**Final answer:** $\frac{3}{2π}$** cm s**<sup>**-1**</sup>

**[A1]**

> **[mark-scheme]**
> The correct exact value gets this mark, even without the units.

> **[exam-tip]**
> Be careful: not all questions forgive units (for example, questions that ask for answers in different units or ask for an interpretation).

### Q5
> *Differentiate *$y = ( 2 x - 1 ) \sqrt{4 x + 3}$* using the product rule and chain rule.*

> $u=2x-1$*    *$v = ( 4 x + 3 )^{1 \frac{1}{2}}$

> $\frac{du}{dx}=2$*    *$\frac{ \mathrm{d} v}{ \mathrm{d} x} = 2 ( 4 x + 3 )^{- 1 \frac{1}{2}}$

$\frac{ \mathrm{d} v}{ \mathrm{d} x} = 2 ( 4 x + 3 )^{- 1 \frac{1}{2}}$** ****[1]**

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( 2 ) ( 4 x + 3 )^{1 \frac{1}{2}} + ( 2 x - 1 ) ( 2 ( 4 x + 3 )^{- 1 \frac{1}{2}} )$

**use of product rule ****[1]**
* ***all terms correct ****[1]**

> *Simplify - start by taking factors of *$2$* and *$( 4 x + 3 )^{- 1 \frac{1}{2}}$*.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = 2 ( 4 x + 3 )^{- 1 \frac{1}{2}} [ 4 x + 3 + 2 x - 1 ]$

**[1]**

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = 2 ( 4 x + 3 )^{- 1 \frac{1}{2}} [ 6 x + 2 ]$

> *Rewrite as a fraction.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( \frac{2}{( 4 x + 3 )^{1 \frac{1}{2}}} ) ( 6 x + 2 )$

> *Multiply the fractions.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{12 x + 4}{( 4 x + 3 )^{1 \frac{1}{2}} }$

> *Factorise the numerator, and rewrite the denominator to express as required.*

$\frac{dy}{dx}=\frac{4(3x+1)}{\sqrt{4x+3}}$* ***[1]**
> *At a stationary point, the gradient is 0, and therefore *$\frac{dy}{dx}=0$*.*

$\frac{4 ( 3 x + 1 )}{ \sqrt{4 x + 3} } = 0$

> *Rearrange and solve for *$x$*.*

$\begin{gathered} 4 ( 3 x + 1 ) & = 0 \\ 3 x + 1 & = 0 \\ x = - 1 \frac{1}{3} \end{gathered}$

> $x=-\frac{1}{3}$* [1]*
> *To determine the nature of the stationary point, we can find the gradient **just** either side of *$x=-\frac{1}{3}$*. When *$x=-\frac{1}{2}$* (to the left of the stationary point),*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{4 ( 3 ( - 1 \frac{1}{2} ) + 1 )}{ \sqrt{4 ( - 1 \frac{1}{2} ) + 3} } 
 \frac{ \mathrm{d} y}{ \mathrm{d} x} = - 2$

> *When *$x=-\frac{1}{4}$* (to the right of the stationary point),*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{4 ( 3 ( - 1 \frac{1}{4} ) + 1 )}{ \sqrt{4 ( - 1 \frac{1}{4} ) + 3} } 
 \frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{ \sqrt{2} }{2}$

**[1]**

> *The gradient goes from negative to positive through the point where *$x=-\frac{1}{3}$*, so the curve is "*$\cup$*-shaped".*

$\thereforex=-\frac{1}{3}$** is a minimum point**** **[1]

### Q6
> *Stationary points occur when *$\frac{dy}{dx}=0$* so first differentiate using the product rule, for *$y=uv,\frac{dy}{dx}=v\frac{du}{dx}+u\frac{dv}{dx}$*.*

$u = x v = ( 16 - x^{2} )^{1 \frac{1}{2}}$

$\frac{du}{dx}=1$

$\frac{d v}{d x} = 1 \frac{1}{2} ( 16 - x^{2} )^{- 1 \frac{1}{2}} \times - 2 x = - x ( 16 - x^{2} )^{- 1 \frac{1}{2}}$

**[1]**

> *Apply the product rule.*

$\frac{d y}{d x} = ( 16 - x^{2} )^{1 \frac{1}{2}} \times 1 + x \times ( - x ( 16 - x^{2} )^{- 1 \frac{1}{2}} )$

** ****use product rule ****[1] **
**fully correct ****[1]**

> *Simplify and set equal to 0.*

$0 = ( 16 - x^{2} )^{1 \frac{1}{2}} - x^{2} ( 16 - x^{2} )^{- 1 \frac{1}{2}}$

**[1]**

> *Adding *$x^{2} ( 16 - x^{2} )^{- 1 \frac{1}{2}}$* to both sides gives.*

$x^{2} ( 16 - x^{2} )^{- 1 \frac{1}{2} } = ( 16 - x^{2} )^{1 \frac{1}{2}}$

$\frac{x^{2}}{( 16 - x^{2} )^{1 \frac{1}{2}}} = ( 16 - x^{2} )^{1 \frac{1}{2}}$

> *Multiplying both sides by *$( 16 - x^{2} )^{1 \frac{1}{2}}$*.*

$x^{2}=16-x^{2}$

> *Adding *$x^{2}$* to both sides.*

$2x^{2}=16$

$x^{2}=8$

**[1]**

> *Finding the square root of both sides - disregard the negative root as it's outside the range given in the question.*

$x=\sqrt{8}=2\sqrt{2}$

> *Substituting this into the equation gives the y co-ordinate.*

$y=8$

$(2\sqrt{2},8)$* ***[1]**
> *Differentiating using the chain rule that states that *$\frac{dy}{dx}=\frac{du}{dx}\times\frac{dy}{du}$

> $y=u^{\frac{3}{2}}$*           *$u=16-x^{2}$

$\frac{dy}{du}=\frac{3}{2}u^{\frac{1}{2}}\frac{du}{dx}=-2x$

> *Substituting into the chain rule gives*

$\frac{dy}{dx}=-2x\times\frac{3}{2}u^{\frac{1}{2}}$

** ****attempt at chain rule ****[1]**

> *Substituting in the expression for *$u$

$\frac{d y}{d x} = - 2 x \times \frac{3}{2} ( 16 - x^{2} )^{1 \frac{1}{2}}$

**[1]**

> *Simplifying gives*

$\frac{d y}{d x} = - 3 x ( 16 - x^{2} )^{1 \frac{1}{2}}$

> *The area required is*

$\int_{1}^{3} x ( 16 - x^{2} )^{1 \frac{1}{2}} d x$

> *You have just differentiated *$( 16 - x^{2} )^{ \frac{3}{2} }$* to get *$- 3 x ( 16 - x^{2} )^{1 \frac{1}{2}}$*, which is almost what you are being asked to integrate to find the area. The area is minus-a-third of the result above, so you can write down*

$\int_{1}^{3} x ( 16 - x^{2} )^{1 \frac{1}{2}} d x = [ - 1 \frac{1}{3} ( 16 - x^{2} )^{ \frac{3}{2} } ]_{1}^{3}$

** ****for **$-\frac{1}{3}$**[1]**

**for **$k ( 16 - x^{2} )^{ \frac{3}{2} }$** [1]**

> *Applying the limits*

$( - 1 \frac{1}{3} ( 16 - 3^{2} )^{ \frac{3}{2} } ) - ( - 1 \frac{1}{3} ( 16 - 1^{2} )^{ \frac{3}{2} } )$

$13.2$* ***[1]**

### Q7
*We know that the curved surface area of a cone, *$S$*, is *$πrl$*.*
 $r$* in this case is actually *$x$* and the slant height *$l$* is given as *$\sqrt{x^{2}+y^{2}}$*. But the expression given for the curved surface are is in terms of *$x$* only.* 
*Therefore we need to find an expression for *$y$* in terms of *$x$*.*

> *We are given a value for the volume, '*$10π$*'. Therefore equate *$10π$* to the formula for volume of a cone in terms of the radius *$x$* and height *$y$*.*

$10π=\frac{1}{3}πx^{2}y$

> *Rearrange to get an expression for *$y$* in terms of *$x$*.*

$\begin{gathered} y = \frac{10 \pi }{1 \frac{1}{3} \pi x^{2}} \\ = \frac{30}{x^{2}} \end{gathered}$

**[1]**

> *Now substitute *$x=r$* and *$l=\sqrt{x^{2}+y^{2}}$* where *$y=\frac{30}{x^{2}}$* into *$S=πrl$*.*

$S = \pi x \sqrt{x^{2} + ( \frac{30}{x^{2}} )^{2}}$

**[1]**

> *This is starting to approach something that looks like the final answer. To get to the final answer, start by expanding the bracket inside the square root.*

$S=πx\sqrt{x^{2}+\frac{900}{x^{4}}}$

> *Note that there's no fraction inside the square root of the final answer. Rewrite '*$x^{2}+\frac{900}{x^{4}}$*' as a single fraction.*

$S=πx\sqrt{\frac{x^{6}+900}{x^{4}}}$

> *Now take the square root of the denominator of the fraction.*

$S=πx\frac{\sqrt{x^{6}+900}}{x^{2}}$

> *Cancel the *$x$* and the *$x^{2}$*.*

`S = pi / x (sqrt( x ^ 6 + 900 ))/(/ x ^2 )`

$S=\frac{π\sqrt{x^{6}+900}}{x}$**[1]**
> *We will need to differentiate *$S$* and then equate the derivative to 0 to find the minimum value of *$x$*. *
*As differentiation will be involved, rewrite the square root as a fractional power.*

$S = \frac{\pi \sqrt{x^{6 + 900} }{x} = \frac{\pi ( x^{6} + 900 )^{1} \frac{1}{2}} }{x}$

> *To differentiate *$S$* we need to use the quotient rule.*

`S = (pi ( x ^ 6 + 900 ) ^ 1 half )/(x) = u / v , where u = pi ( x ^ 6 + 900 ) ^ 1 half and v = x`

> *From here we need to find *$\frac{du}{dx}$* and *$\frac{dv}{dx}$*. However we need to use the chain rule to find *$\frac{du}{dx}$*.*

`u = pi ( x ^ 6 + 900 ) ^ 1 half , let u = pi w ^ 1 half and w = x ^ 6 + 900`

> *Now differentiate **u** and **w.*

$\frac{du}{dw}=π\times\frac{1}{2}w^{-\frac{1}{2}},\frac{dw}{dx}=6x^{5}$

> *And apply the chain rule, in this case *$\frac{du}{dx}=\frac{du}{dw}\times\frac{dw}{dx}$*.*

$\begin{gathered} \frac{ \mathrm{d} u}{ \mathrm{d} x} & = \pi 1 \frac{1}{2} w^{- 1 \frac{1}{2}} \times 6 x^{5 \\ = \pi 1 \frac{1}{2} ( x^{6} + 900 )^{-1} \frac{1}{2}} \times 6 x^{5} \end{gathered}$

** **$\begin{gathered} \pi 1 \frac{1}{2} ( x^{6 + 900 )^{-1} \frac{1}{2}} \end{gathered}$** ****[1]**

$\begin{gathered} = 3 \pi x^{5 ( x^{6} + 900 )^{-1} \frac{1}{2}} \end{gathered}$

**[1]**

> *Now we are ready to go back to *$S=\frac{u}{v}$* where *$u=π\sqrt{x^{6}+900}$* and *$v=x$*.*

`| u = pi ( x ^ 6 + 900 ) ^ 1 half and v = x | | ( d u)/( d x) | = 3 pi x ^ 5 ( x ^ 6 + 900 ) ^ - 1 half ( d v)/( d x) = 1 | |`

> *Apply the quotient rule, *$\frac{dy}{dx}=\frac{v\frac{du}{dx}-u\frac{dv}{dx}}{v^{2}}$*.*

$\frac{ \mathrm{d} S}{ \mathrm{d} x} = \frac{x ( 3 \pi x^{5 ( x^{6} + 900 )^{-1} \frac{1}{2}} ) - \pi ( x^{6 + 900 )^{1} \frac{1}{2}} }{x^{2}}$

**[1]**

> *At the minimum value of S, *$\frac{dS}{dx}=0$*, so equate this derivative to 0.*

$\frac{x ( 3 \pi x^{5 ( x^{6} + 900 )^{-1} \frac{1}{2}} ) - \pi ( x^{6 + 900 )^{1} \frac{1}{2}} }{x^{2}} = 0$

> *Solve - start by multiplying by the denominator, *$x^{2}$*.*

$x ( 3 \pi x^{5 ( x^{6} + 900 )^{-1} \frac{1}{2}} ) - \pi ( x^{6 + 900 )^{1} \frac{1}{2}} = 0$

**[1]**

> *Simplify.*

$3 \pi x^{6 ( x^{6} + 900 )^{-1} \frac{1}{2}} - \pi ( x^{6 + 900 )^{1} \frac{1}{2}} = 0$

> *Remove the negative power.*

$\begin{gathered} \frac{3 \pi x^{6}{( x^{6} + 900 )^{1} \frac{1}{2}} } - \pi ( x^{6 + 900 )^{1} \frac{1}{2}} & = 0 \\ \text{or} \frac{3 \pi x^{6} }{ \sqrt{x^{6} + 900} } - \pi \sqrt{x^{6} + 900} & = 0 \end{gathered}$

> *Multiply by *$\sqrt{x^{6}+900}$*.*

$3 \pi x^{6} - \pi ( x^{6} + 900 ) = 0$

> *Divide by *$π$* and complete the solution.*

$\begin{gathered} 3 x^{6} - ( x^{6} + 900 ) & = 0 \\ 3 x^{6} - x^{6} - 900 & = 0 \\ 2 x^{6} & = 900 \\ x^{6} & = 450 \end{gathered}$

** **`x = sqrt index 6 of 450 = 2 . 768229457 . . . or 2 . 77 stretchy ( 3 s. f. stretchy )`  **[1] **
**Note that **$x$** is a length therefore **`x not equal to negative root index 6 of 450`

### Q8
> *Use chain rule to differentiate *$\ln ( f ( x ) )$*. *

$\frac{d y}{d x} = \frac{1}{( \sin x + 3 \cos x )} \times ( \cos x - 3 \sin x )$

**differentiating ln**** [1] **
**chain rule**** [1]**

> *Simplify.*

$\frac{dy}{dx}=\frac{\mathrm{cos}x-3\mathrm{sin}x}{\mathrm{sin}x+3\mathrm{cos}x}$ **[1]**
> *Set *$\frac{dy}{dx}$* from part (a) equal to *$-\frac{1}{2}$*.*

$-\frac{1}{2}=\frac{\mathrm{cos}x-3\mathrm{sin}x}{\mathrm{sin}x+3\mathrm{cos}x}$

> *Multiply both sides by the denominators.*

$- ( \sin x + 3 \cos x ) = 2 \cos x - 6 \sin x$

> *Expand the brackets.*

$-\mathrm{sin}x-3\mathrm{cos}x=2\mathrm{cos}x-6\mathrm{sin}x$

**[1]**

> *Collect like terms.*

$5\mathrm{sin}x=5\mathrm{cos}x$

> *Dividing both sides by *$5\mathrm{cos}x$* and using the identity *$\frac{\mathrm{sin}x}{\mathrm{cos}x}=\mathrm{tan}x$*.*

$\mathrm{tan}x=1$

**[1]**

> *Solving for *$x$* using the range given in part (a).*

$x=\frac{π}{4}$ **[1]**

### Q9
> *Use the product rule, *$\frac{ \mathrm{d} }{ \mathrm{d} x} ( u v ) = u \frac{ \mathrm{d} v}{ \mathrm{d} x} + v \frac{ \mathrm{d} u}{ \mathrm{d} x}$*, and the chain rule.*

*Let *$u=x^{2}-1$* and *$v = ( 5 x + 2 )^{1 \frac{1}{2}}$

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( ( x^{2} - 1 ) \times 1 \frac{1}{2} ( 5 x + 2 )^{- 1 \frac{1}{2}} \times 5 ) + ( ( 5 x + 2 )^{1 \frac{1}{2}} \times 2 x )$

**for **$\frac{5}{2}(5x+2)^{-\frac{1}{2}}$**[1]**

**for differentiation of a product**** [1]**

**fully correct differentiation ****[1]**

> *Simplify each bracket.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( \frac{5}{2} ( x^{2} - 1 ) ( 5 x + 2 )^{- 1 \frac{1}{2}} ) + ( 2 x ( 5 x + 2 )^{1 \frac{1}{2}} )$

> *Take out common factor of *$1 \frac{1}{2} ( 5 x + 2 )^{- 1 \frac{1}{2}}$*.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = 1 \frac{1}{2} ( 5 x + 2 )^{- 1 \frac{1}{2}} ( 5 ( x^{2} - 1 ) + 4 x ( 5 x + 2 ) )$

**[1]**

> *Expand and simplify, writing as a fraction.*

$\frac{dy}{dx}=\frac{5x^{2}-5+20x^{2}+8x}{2\sqrt{5x+2}}$

> *Simplify.*

$\frac{dy}{dx}=\frac{25x^{2}+8x-5}{2\sqrt{5x+2}}$** [1]**
> *From part (a), *$\frac{dy}{dx}=\frac{25x^{2}+8x-5}{2\sqrt{5x+2}}$*.*

> *Stationary points occur when *$\frac{dy}{dx}=0$*.*

$\frac{25x^{2}+8x-5}{2\sqrt{5x+2}}=0\,25x^{2}+8x-5=0$

**[1]**

> *Use the quadratic formula (and/or calculator) to solve the quadratic equation.*

$x = \frac{- 8 \pm \sqrt{8^{2} - 4 ( 25 ) ( - 5 )} }{2 ( 25 )}$

$x=0.3149...\mathrm{or}-0.6349...$

$x>0\mathrm{so}x=0.3149...$

> *Find *$y$* by substituting *$x$* into the equation of the curve.*

$\begin{gathered} y = ( x^{2} - 1 ) \sqrt{5 x + 2} \\ y = ( 0.3149...^{2} - 1 ) \sqrt{5 ( 0.3149... ) + 2} \\ y = - 1.7031... \end{gathered}$

$x=0.315(3s.f.)$** [1]**

$y=-1.70(3s.f)$** [1]**
> *Consider the gradient of the curve either side of the stationary point*

> *From part (a), we know that *$\frac{dy}{dx}=\frac{25x^{2}+8x-5}{2\sqrt{5x+2}}$

> *The stationary point occurs at *$( 0.315 , - 1.70 )$* so look at the gradient either side of this point.*

> *When *$x=0.3$*,*

$\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{25 ( 0.3 )^{2} + 8 ( 0.3 ) - 5}{2 \sqrt{5 ( 0.3 ) + 2} } \\ \frac{ \mathrm{d} y}{ \mathrm{d} x} & = - 0.093... < 0 \end{gathered}$

> *When *$x=0.4$*,*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{25 ( 0.4 )^{2} + 8 ( 0.4 ) - 5}{2 \sqrt{5 ( 0.4 ) + 2} } 
 \frac{ \mathrm{d} y}{ \mathrm{d} x} = 0.55 > 0$

** [1]**

> *The gradient changes from positive to negative through the point *$( 0.315 , - 1.70 )$* so the curve is "*$\cup$*-shaped".*

$\therefore(0.315,-1.70)$** is a minimum point**** [1]**

### Q10
> *Differentiate using product rule, *$\frac{ \mathrm{d} }{ \mathrm{d} x} ( u v ) = u \frac{ \mathrm{d} v}{ \mathrm{d} x} + v \frac{ \mathrm{d} u}{ \mathrm{d} x}$*.*

> $u=x$*   *$v=\mathrm{cos}x$

> $\frac{du}{dx}=1$*  *$\frac{dv}{dx}=-\mathrm{sin}x$

**[1]**

> * *$\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( x ) ( - \sin x ) + ( 1 ) ( \cos x )$

$\frac{dy}{dx}=-x\mathrm{sin}x+\mathrm{cos}x$* ***[1]**
> *Find the gradient of the curve at the point *$x=π$*.*

$\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = - \pi \sin \pi + \cos \pi \\ \frac{ \mathrm{d} y}{ \mathrm{d} x} & = - 1 \end{gathered}$

**[1]**

> *The gradient of the normal is the negative reciprocal of this.*

$\thereforem=1$

**[1]**

> *Substitute *$x=π$* into the equation of the curve to find the corresponding *$y$*value.*

$y=π\mathrm{cos}π\,y=-π$

> *The normal passes through the point*

$( \pi , - \pi )$

**[1]**

> *We know the gradient and a point the normal passes through so use the point-gradient form for the equation of a line.*

$\begin{gathered} y - ( - \mathrm{\pi } ) & = 1 ( x - \mathrm{\pi } ) \end{gathered}$

> *Write in the form *$y=mx+c$* as required for the final answer.*

$y=x-2π$* ***[1]**

### Q11
> *This is a connected rates of change question - the rate of change of the radius is connected to the rate of change of the area.*

> *The radius of the circle is increasing with respect to time.*

$\frac{dr}{dt}=5$

**[1]**

> *To find the rate at which the area is increasing, use chain rule.*

$\frac{dA}{dt}=\frac{dr}{dt}\times\frac{dA}{dr}$

> *The area of a circle is given by *$A=πr^{2}$*, so,*

$\frac{dA}{dr}=2πr$

**[1]**

> *Substitute the two results into chain rule.*

$\begin{gathered} \frac{ \mathrm{d} A}{ \mathrm{d} t} & = 5 \times 2 \mathrm{\pi } r \\ \frac{ \mathrm{d} A}{ \mathrm{d} t} & = 10 \mathrm{\pi } r \end{gathered}$

**[1]**

> *Substitute the given value of **r.*

$\frac{dA}{dt}=10π\times3$

$\frac{dA}{dt}=30π\mathrm{cm}^{2}s^{-1}$ **[1]**

### Q12
> *Differentiate *$y=\mathrm{ln}(5--3x)$*.*

$\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{1}{5 - 3 x} \times ( - 3 ) \\ = \frac{- 3}{5 - 3 x} \end{gathered}$

$\frac{k}{5-3x}$** where **$k\neq-3$** ****[1]**

$\frac{-3}{5-3x}$** [1]**

> *Find the gradient of the tangent to *$y=\mathrm{ln}(5--3x)$* when *$x=-5$* by substituting *$x=-5$* into *$\frac{dy}{dx}$*.*

$\begin{array}{rcl} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{- 3}{5 - 3 ( - 5 )} \\ = - \frac{3}{20} \end{array}$

**[1]**

> *Divide this by -1 to find *$m$*, the gradient of the normal.*

$m=\frac{-1}{-\frac{3}{20}}=\frac{20}{3}$

**[1]**

> *Find *$y$* when *$x=-5$*.*

$y = \ln ( 5 - 3 ( 5 ) ) = \ln 20$

**[1]**

> *Substitute *$( - 5 , \ln 20 )$* and *$m=\frac{20}{3}$* into the equation of a straight line. Here we will use the point-gradient form, *$y - y_{1} = m ( x - x_{1} )$*.*

$y - \ln 20 = \frac{20}{3} ( x - ( - 5 ) )$

> *Therefore the equation of the normal is *

$y-\mathrm{ln}20=\frac{20}{3}(x+5)$**[1]**
 **Equivalent forms of the equation are acceptable**

> *Substitute *$y=0$* to find where line crosses the *$x$*-axis.*

$\begin{gathered} 0 - \ln 20 & = \frac{20}{3} ( x + 5 ) \\ - \ln 20 \div \frac{20}{3} & = x + 5 \\ \frac{- 3 \ln 20}{20} - 5 & = x \\ x = - 5.44935984... \end{gathered}$

$x=-\frac{3\mathrm{ln}20}{20}-5\mathrm{or}-5.45(3s.f.)$ **[1]**

### Q13
> *Differentiate using product rule, *$\frac{ \mathrm{d} }{ \mathrm{d} x} ( u v ) = u \frac{ \mathrm{d} v}{ \mathrm{d} x} + v \frac{ \mathrm{d} u}{ \mathrm{d} x}$*, and chain rule.*

> $u=x$*    *$v = ( x + 2 )^{1 \frac{1}{2}}$

> $\frac{du}{dx}=1$*   *$\frac{ \mathrm{d} v}{ \mathrm{d} x} = 1 \frac{1}{2} ( x + 2 )^{- 1 \frac{1}{2}}$

$[ 1 ]$

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( 1 ) ( x + 2 )^{1 \frac{1}{2}} + ( x ) ( 1 \frac{1}{2} ( x + 2 )^{- 1 \frac{1}{2}} )$

$[ 1 ]$

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = 1 \frac{1}{2} x ( x + 2 )^{- 1 \frac{1}{2}} + ( x + 2 )^{1 \frac{1}{2}}$

**[1]**

> *Simplify by taking factors of *$\frac{1}{2}$* and *$( x + 2 )^{- 1 \frac{1}{2}}$*.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = 1 \frac{1}{2} ( x + 2 )^{- 1 \frac{1}{2}} [ x + 2 ( x + 2 ) ]$

**[1]**

> *Rewrite as a fraction.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( 1 \frac{1}{2} ) ( \frac{1}{ \sqrt{x + 2} } ) ( 3 x + 4 )$

> *Simplify to get in the required form.*

$\frac{dy}{dx}=\frac{3x+4}{2\sqrt{x+2}}$* ***[1]**
*From part (a), *$\frac{dy}{dx}=\frac{3x+4}{2\sqrt{x+2}}$. 
*Stationary points occur when the gradient is 0, so substitute* $\frac{dy}{dx}=0$.

$\frac{3x+4}{2\sqrt{x+2}}=0$

> *Rearrange and solve.*

$\begin{gathered} 3 x + 4 & = 0 \end{gathered}$

**[1]**

$\begin{gathered} x = - \frac{4}{3} \end{gathered}$

**[1]**

> *Substitute into the equation of the curve to find the *$y$* coordinate.*

`y = ( - 4 / 3 ) ( sqrt( - 4 / 3 + 2 ) ) y = - (4 sqrt( 2)/(3 sqrt( 3)`

> *Rationalise the denominator.*

$y=-\frac{4\sqrt{2}}{3\sqrt{3}}\times\frac{\sqrt{3}}{\sqrt{3}}\,y=-\frac{4\sqrt{6}}{9}$

$(-\frac{4}{3},-\frac{4\sqrt{6}}{9})$* ***[1]**
> *The stationary point occurs at *$x=-\frac{4}{3}$*. *
*To find the nature of this point, we can find the gradient, **just** either side of *$x=-\frac{4}{3}$*. *
*When *$x=-1$*, (to the right of the stationary point),*

$\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{3 ( - 1 ) + 4}{2 \sqrt{( - 1 ) + 2} } \\ \frac{ \mathrm{d} y}{ \mathrm{d} x} & = 1 \frac{1}{2} \end{gathered}$

> *When *$x=-\frac{5}{3}$*, (to the left of the stationary point),*

`table columnalign right center left columnspacing 0px end | ( d y)/( d x) | = (3 ( - begin display style 5 / 3 ) + 4)/(2 sqrt( ( - begin display style 5 / 3 ) + 2 )) | | ( d y)/( d x) | = - (sqrt( 3)/(2) | |`

**[1]**

> *Since the gradient changes from negative to positive through the point where *$x=-\frac{4}{3}$* so the curve is "*$\cup$*-shaped".*

$\therefore(-\frac{4}{3},-\frac{4\sqrt{6}}{9})$** is a minimum point ****[1]**

### Q14
> *We know that the radius is increasing at a rate of 0.5*$\mathrm{cms}^{-1}$*.*

$\frac{dr}{dt}=0.5$

**[1]**

> *Differentiate the volume of the sphere with respect to **r.*

$\frac{dV}{dr}=3\times\frac{4}{3}πr^{2}$

$\frac{dV}{dr}=4πr^{2}$

**[1]**

> *We want to find the rate of change of the volume which is *$\frac{dV}{dt}$* so use the chain rule.*

$\begin{gathered} \frac{ \mathrm{d} V}{ \mathrm{d} t} & = \frac{ \mathrm{d} V}{ \mathrm{d} r} \times \frac{ \mathrm{d} r}{ \mathrm{d} t} \\ \frac{ \mathrm{d} V}{ \mathrm{d} t} & = 4 \mathrm{\pi } r^{2} \times 0.5 \\ \frac{ \mathrm{d} V}{ \mathrm{d} t} & = 2 \mathrm{\pi } r^{2} \end{gathered}$

**[1]**

> *Find *$\frac{dV}{dt}$* when *$r=\frac{1}{4}$*.*

`( d V)/( d t) = 2 pi x ( 1 fourth ) ^2 = pi / 8`

$\frac{π}{8}\mathrm{cm}^{3}s^{-1}$** [1]**

### Q15
> *We need to find the equation of the tangent to the curve so start by differentiating the curve to find the gradient of the tangent. *
*Use chain rule to differentiate *$\ln ( 3 x^{2} - 4 )$*.*

$\frac{dy}{dx}=\frac{6x}{3x^{2}-4}-\frac{3x^{2}}{6}$

$\frac{6x}{3x^{2}-4}$ **[1]**

> *Simplify.*

$\frac{dy}{dx}=\frac{6x}{3x^{2}-4}-\frac{x^{2}}{2}$

**[1]**

> *Find the gradient when *$x=2$*.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{6 ( 2 )}{3 ( 2 )^{2} - 4} - \frac{( 2 )^{2}}{2} 
 \frac{ \mathrm{d} y}{ \mathrm{d} x} = - 1 \frac{1}{2}$

**[1]**

> *To find the equation of the tangent, we also need a point and the gradient. So find *$y$* when *$x=2$*.*

$y = \ln ( 3 ( 2 )^{2} - 4 ) - \frac{( 2 )^{3}}{6}$

$y = \ln ( 8 ) - \frac{4}{3}$

**[1]**

> *Find the equation of the tangent using *$y - y_{1} = m ( x - x_{1} )$* with *`( x _ 1 , y _ 1 ) = ( 2 , ln ( 8 ) - 4 / 3 ) and m = - 1 half`*.*

$y - ( \ln ( 8 ) - \frac{4}{3} ) = - 1 \frac{1}{2} ( x - 2 )$

**[1]**

> *At P, *$x=0$* because it is the *$y$*-axis so substitute *$x=0$* into the equation of the tangent.*

$\begin{array}{rcl} y - ( \ln ( 8 ) - \frac{4}{3} ) & = - 1 \frac{1}{2} ( 0 - 2 ) \\ y - \ln ( 8 ) + \frac{4}{3} & = 1 \\ y = \ln ( 8 ) - 1 \frac{1}{3} \end{array}$

$( 0 , l n ( 8 ) - 1 \frac{1}{3} )$** [1]**

### Q16
> *Differentiate *$e^{\frac{x}{2}}$*.*

$\frac{1}{2}e^{\frac{x}{2}}$

**[1]**

> *Differentiate *$x\mathrm{cos}2x$* using the product rule.*

$u=x$* **and *$v=\mathrm{cos}2x$

$\frac{du}{dx}=1$* and *$\frac{dv}{dx}=-2\mathrm{sin}2x$

$( x \times - 2 \sin 2 x ) + ( 1 \times \cos 2 x )$

**for **$-2\mathrm{sin}2x$** ****[1]**

$=-2x\mathrm{sin}2x+\mathrm{cos}2x$

**[1]**

> *Combine the two results for *$\frac{dy}{dx}$*.*

$\frac{dy}{dx}=\frac{1}{2}e^{\frac{x}{2}}-2x\mathrm{sin}2x+\mathrm{cos}2x$

**[1]**

> *Substitute *$x=1$*.*

$\frac{dy}{dx}=\frac{1}{2}e^{\frac{1}{2}}-2\mathrm{sin}2+\mathrm{cos}2$

**[1]**

$=-1.410381055$

> *Change in *$y$* *$=\frac{dy}{dx}\times$* change in *$x$*.*

> *Change in *$x = ( 1 + h ) - ( 1 ) = h$*.*

*change in *$y$$=-1.410381055\timesh$

**Approximate change in **$y$** is **$-1.41h$* ***[1]**

### Q17
> *Recall that*

$\frac{ \mathrm{d} }{ \mathrm{d} x} ( e^{3 x} ) = 3 e^{3 x}$

**[1]**

> *Use the product rule to differentiate the numerator and then apply the quotient rule.*

> *When you differentiate the numerator using the product rule you will get*

$e^{3x}\mathrm{cos}x+3e^{3x}\mathrm{sin}x$

**[1]**

$\frac{ \mathrm{d} }{ \mathrm{d} x} ( \frac{e^{3 x} \sin x}{x^{2}} ) = \frac{x^{2} ( e^{3 x} \cos x + 3 e^{3 x} \sin x ) - 2 x ( e^{3 x} \sin x )}{( x^{2} )^{2}}$

**[1]**

$\frac{ \mathrm{d} }{ \mathrm{d} x} ( \frac{e^{3 x} \sin x}{x^{2}} ) = \frac{x^{2} e^{3 x} \cos x + 3 x^{2} e^{3 x} \sin x - 2 x e^{3 x} \sin x}{x^{4} }$

**[1]**

> *Evaluate the derivative above when *$x=0.5$* using the radian mode on your calculator.*

$\frac{ \mathrm{d} }{ \mathrm{d} x} ( \frac{e^{3 x} \sin x}{x^{2}} ) = 7.13766...$

**[1]**

> *As *$h$* is small, use *$"\mathrm{Change} \mathrm{in}y=\mathrm{Gradient}\times\mathrm{Change} \mathrm{in}x"$*.*

$7.14\timesh$

**Approximate change in **$y$** is**$7.14h$** [1]**

### Q18
> *Differentiate *$y$* with respect to *$x$*.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = 2 ( 2 - \sqrt{3} ) x + 1$

**[1]**

> *Stationary points are where *$\frac{dy}{dx}=0$*.*

$2 ( 2 - \sqrt{3} ) x + 1 = 0$

> *Rearrange to find *$x$*.*

$2 ( 2 - \sqrt{3} ) x = - 1$

$x = - \frac{1}{2 ( 2 - \sqrt{3} )}$

> *Rationalise the denominator.*

$\begin{gathered} x = - \frac{1}{2 ( 2 - \sqrt{3} )} \times \frac{( 2 + \sqrt{3} )}{( 2 + \sqrt{3} )} \\ x = - \frac{2 + \sqrt{3} }{2 ( 2 - \sqrt{3} ) ( 2 + \sqrt{3} )} \\ x = - \frac{2 + \sqrt{3} }{2 ( 4 - 3 )} \\ x = - \frac{2 + \sqrt{3} }{2} \end{gathered}$

**[1]**

> *Simplify.*

$x=-1-\frac{\sqrt{3}}{2}$* ***[1]**

### Q19
> *Differentiate *$y$* with respect to *$x$*.*

$y=\mathrm{sin}x+e^{-x}$

$\frac{dy}{dx}=\mathrm{cos}x-e^{-x}$

**at least one term correct**** [1]**
** ****all correct**** [1]**

> *Substitute *$x=\frac{π}{4}$* into *$\frac{dy}{dx}$*.*

`( d y)/( d x) = cos ( pi / 4 ) - e ^ - pi / 4`

> *Evaluate, ensuring your calculator is in radian mode.*

$\frac{dy}{dx}=0.2511...$

**[1]**

*As *$h$* is small, use* $"\mathrm{change} \mathrm{in}y=gradient\times\mathrm{change} \mathrm{in}x"$.

$\mathrm{change} \mathrm{in}y=0.251...\timesh$

**The approximate change in **$y$** is **$0.25h$ **[1]**

### Q20
> *We actually need to work with a 'third' cone - formed from the larger hollow cone described in the question but with a height that is determined by the (higher) water level. All three cones are similar and since the radius of the smaller cone is half its own height, the radius of the 'third' cone will be half its own height too.*

$\therefore R = 1 \frac{1}{2} ( w + 180 )$

**[1]**

> *The volume of the water can be found by subtracting the volume of the smaller cone from that of the 'third' cone.*

$V = 1 \frac{1}{3} \mathrm{\pi } ( 1 \frac{1}{2} ( w + 180 ) )^{2} ( w + 180 ) - 1 \frac{1}{3} \mathrm{\pi } ( 90 )^{2} ( 180 )$

**[1]**

> *Simplify.*

$\begin{gathered} V = 1 \frac{1}{3} \mathrm{\pi } ( 1 \frac{1}{2} )^{2} ( w + 180 )^{2} ( w + 180 ) - 1 \frac{1}{3} \mathrm{\pi } ( 90 )^{2} ( 180 ) \\ V = ( 1 \frac{1}{3} ) ( 1 \frac{1}{4} ) \mathrm{\pi } ( w + 180 )^{3} - 486000 \mathrm{\pi } \end{gathered}$

$V=\frac{π}{12}(w+180)^{3}-486000π$* ***[1]**
> *This is a connected rates of change question, we will need to use chain rule.  At time *$t$*,*

$\frac{dw}{dt}=\frac{dw}{dV}\times\frac{dV}{dt}$

> *The rate at which the volume (*$V$*) is changing with respect to the height of the water (*$w$*) is*

$\frac{ \mathrm{d} V}{ \mathrm{d} w} = 3 \frac{\pi }{12} ( w + 180 )^{2}$

**[1]**

> *We require *$\frac{dw}{dV}$*.*

> `( d w)/( d V) = (1)/( pi / 4 ( w + 180 ) ^2)`*   *

> *We know the rate at which water is poured into the container with respect to time.*

$\frac{dV}{dt}=10000$

> *Apply chain rule.*

$\frac{ \mathrm{d} w}{ \mathrm{d} t} = \frac{1}{\frac{pi}{4} ( w + 180 ) ^{2} } \times 10000$

**[1]**

$\frac{ \mathrm{d} w}{ \mathrm{d} t} = \frac{40000}{ \mathrm{\pi } ( w + 180 )^{2}}$

> *When *$w=10$*,*

$\frac{ \mathrm{d} w}{ \mathrm{d} t} = \frac{40000}{ \mathrm{\pi } ( 10 + 180 )^{2}}$

**[1]**

> *Simplify and evaluate.*

$\frac{ \mathrm{d} w}{ \mathrm{d} t} = \frac{40000}{ \mathrm{\pi } ( 190 )^{2}} 
 \frac{ \mathrm{d} w}{ \mathrm{d} t} = 0.3526...$

$\frac{dw}{dt}=0.353\mathrm{cm}s^{-1}(3s.f.)$* ***[1]**

### Q21
> *Substitute *$x=1$* into the equation to find the *$y$*-coordinate.*

$y = 1^{3} - 6 ( 1 )^{2} + 3 ( 1 ) + 10$

$y=8$

**[1]**

> *Differentiate the equation of the curve to find the gradient function.*

$\frac{dy}{dx}=3x^{2}-12x+3$

**[1]**

> *Substitute *$x=1$* to find the gradient at this point.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = 3 ( 1 )^{2} - 12 ( 1 ) + 3$

$\frac{dy}{dx}=-6$

**[1]**

*Find the equation of the tangent with point *$( 1 , 8 )$* and gradient *$-6$.

$y - 8 = - 6 ( x - 1 )$

$y-8=-6x+6$

$y=-6x+14$

$y=-6x+14$ **[1]**
> *From part (a), the equation of the tangent is *$y=-6x+14$*. Equate the tangent and the curve.*

$-6x+14=x^{3}-6x^{2}+3x+10$

> *Rearrange to get a cubic equation.*

$\begin{gathered} 14 = x^{3} - 6 x^{2} + 9 x + 10 \\ x^{3} - 6 x^{2} + 9 x - 4 & = 0 \end{gathered}$

**[1]**

> *From part (a) we know *$x=1$* is a solution.*

$( x - 1 )$* is a factor of the cubic*

**[1]**

> *Factorise the cubic using long division (or inspection).*

`long division by x - 1 yields none none none none 1 x ^2 none - 5 x none + 4 pile 1 x ^3 none - 6 x ^2 none + 9 x none - 4 1 x ^3 none - 1 x ^2 none + 0 x none + 0 none - horizontal line none none none - 5 x ^2 none + 9 x none - 4 none none none - 5 x ^2 none + 5 x none + 0 none - horizontal line none none none none none none none none 4 x none - 4 none none none none none none none none 4 x none - 4 none - horizontal line none none none none none none none none none none none none 0 end pile end long division`

> *The factorised cubic is*

$( x - 1 ) ( x^{2} - 5 x + 4 ) = 0$

**[1]**

> *Factorise the second bracket.*

$( x - 1 ) ( x - 1 ) ( x - 4 ) = 0$

**[1]**

> $( x - 1 )$* is a repeated factor and is the solution we already know from part (a). The other solution will give us the *$x$*-coordinate of where the tangent meets the curve again.*

$x-4=0$

$x=4$

> *Substitute *$x=4$* into the equation of the tangent to find the *$y$*-coordinate.*

$y = - 6 ( 4 ) + 14 = - 10$

**The tangent and curve meet again at the point**** **$(4,-10)$ **[1]**

### Q22
> *First note that *$h-\frac{π}{4}$* is the same as *$-\frac{π}{4}+h$*, so this is a small increment in *$x$*.*

> *Differentiate *$y=\mathrm{tan}x$*.*

$\frac{dy}{dx}=\mathrm{sec}^{2}x$

**[1]**

> *Substituting *$x=-\frac{π}{4}$* into *$\frac{dy}{dx}$* gives the gradient at of*$f$* at *$x=-\frac{π}{4}$*.*

`x = - pi / 4 , ( d y)/( d x) = sec ^2 ( - pi / 4 )`

**[1]**

> *Use your calculator to evaluate - make sure your calculator is in radians though! Enter the "*$\mathrm{sec}^{2}x$*"  into your calculator.*

`( (1)/(cos ( - pi / 4 )) ) ^2 = 2`

> *As *$h$* is small we can use this gradient to estimate *$y$* using *$"\mathrm{change} \mathrm{in}y=\mathrm{gradient}\times\mathrm{change} \mathrm{in}x"$*.*

$2\timesh=2h$

**Approximate change in **$y$** is **$2h$** [1]**

### Q23
> *Use Pythagoras' Theorem to find the length **AC **in terms of** *$x$*.*

$\begin{gathered} A C^{2} & = 300^{2} + x^{2} \\ A C & = \sqrt{90 000 + x^{2}} \end{gathered}$

**[1]**

> *Use *$"\mathrm{av}.\mathrm{speed}=\frac{\mathrm{distance}}{\mathrm{time}}"$*(rearranged) to find the time to walk **AC** (speed on the ploughed field).*

$\mathrm{Time} \mathrm{for}AC=\frac{\sqrt{90000+x^{2}}}{0.9}=\frac{10}{9}\sqrt{90000+x^{2}}$

**[1]**

> *Similarly for **CD** (speed on the path),*

$\text{Time} \text{for} C D = \frac{400 - x}{1.5} = \frac{2 ( 400 - x )}{3}$

> *Add the times together to find the total time, **T**.*

$T = \frac{10}{9} \sqrt{90 000 + x^{2}} + \frac{2 ( 400 - x )}{3}$

> $T=\frac{6(400-x)+10\sqrt{90000+x^{2}}}{9}$* [1] *
*Equivalent expressions are acceptable*
> *Rewrite **T **to make it easier to differentiate.*

$T = \frac{2}{9} ( 1200 - 3 x + 5 ( x^{2} + 90 000 )^{1 \frac{1}{2}} )$

> $\frac{2}{9}$* is a constant, differentiate using chain rule for *$( x^{2} + 90 000 )^{1 \frac{1}{2}}$*.*

$\frac{ \mathrm{d} T}{ \mathrm{d} x} = \frac{2}{9} ( - 3 + \frac{5}{2} ( x^{2} + 90 000 )^{- 1 \frac{1}{2}} \times 2 x )
 \frac{ \mathrm{d} T}{ \mathrm{d} x} = \frac{2}{9} ( \frac{5 x}{ \sqrt{x^{2} + 90 000} } - 3 )$

**for correct differentiation of **$( x^{2} + 90 000 )^{1 \frac{1}{2}}$** ****[1]**

**all correct ****[1]**

> *We are asked to find the minimum value, this is when *$\frac{dT}{dx}=0$*.*

$\frac{2}{9} ( \frac{5 x}{ \sqrt{x^{2} + 90 000} } - 3 ) = 0$

**[1]**

> *Rearrange and solve for *$x$*.*

$\begin{gathered} \frac{5 x}{ \sqrt{x^{2} + 90 000} } & = 3 \\ 5 x & = 3 \sqrt{x^{2} + 90 000} \end{gathered}$

> *Square both sides.*

$\begin{gathered} 25 x^{2} & = 9 ( x^{2} + 90 000 ) \\ 16 x^{2} & = 810 000 \\ x^{2} & = 50625 \\ x = \pm 225 \end{gathered}$

**[1]**

> *As *$x$* is a distance, it can only take a positive value.*

$\begin{array}{rcl} x = 225 \end{array}$

**[1]**

*Substitute *$x=225$ *into the equation for **T**.*

$T = \frac{2}{9} ( 1200 - 3 \times 225 + 5 \sqrt{225^{2} + 90 000} )
T = \frac{1600}{3}$

**The minimum value of **$T$** is **$\frac{1600}{3}$**(seconds)**** [1]**

### Q24
> *Differentiate the two terms separately.*

> *Differentiate *$\tan ( x + 4 )$* with respect to *$x$*.*

$\sec ^{2} ( x + 4 )$

> *Differentiate *$-3\mathrm{sin}x$* with respect to *$x$*.*

$-3\mathrm{cos}x$

* ***either correct ****[1]**

> *Put both parts together.*

$\mathrm{sec}^{2}(x+4)-3\mathrm{cos}x$* ***[1]**
> *Differentiate *$\frac{\ln ( 2 x + 5 )}{2 \mathrm{e}^{3 x} }$* using the quotient rule.*

$u = \ln ( 2 x + 5 )$* **and *$v=2e^{3x}$

$\frac{du}{dx}=\frac{2}{2x+5}$* and *$\frac{dv}{dx}=6e^{3x}$

**for **$\frac{2}{2x+5}$** ****[1]**

**for **$6e^{3x}$** ****[1]**

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{( 2 \mathrm{e}^{3 x} \times \frac{2}{2 x + 5} ) - ( 6 \mathrm{e}^{3 x} \times \ln ( 2 x + 5 ) )}{( 2 \mathrm{e}^{3 x} )^{2}}$

**[1]**

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{( 2 \mathrm{e}^{3 x} \times \frac{2}{2 x + 5} ) - ( 6 \mathrm{e}^{3 x} \times \ln ( 2 x + 5 ) )}{4 \mathrm{e}^{6 x}}$

**[1]**

> *Substitute *$x=1$* into the equation for *$\frac{dy}{dx}$*.*

$\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{( 2 \mathrm{e}^{3} \times \frac{2}{7} ) - ( 6 \mathrm{e}^{3} \times \ln 7 )}{4 \mathrm{e}^{6} } \\ = - 0.1382093041 \end{gathered}$

> *As *$h$* is small, use *$"\mathrm{change} \mathrm{in}y=\mathrm{gradient}\times\mathrm{change} \mathrm{in}x"$*.*

*change in *$y$$=-0.1382093041\timesh$

**[1] **
**The approximate change in **$y$** is **$-0.14h$* ***[1]**

### Q25
> *The volume of a cylinder is *$V=πr^{2}h$*.*

$1000=πr^{2}h$

> *Find *$h$* in terms of *$r$*.*

$h=\frac{1000}{πr^{2}}$

**[1]**

> *The cylinder is open at one end so its surface area is *$S=πr^{2}+2πrh$*, so substitute *$h$* into this so the surface area is in terms of *$r$* only.*

$S=πr^{2}+2πr\frac{1000}{πr^{2}}$

**[1]**

> *Simplify.*

$S=πr^{2}+\frac{2000}{r}$

**[1]**

> *Differentiate in order to find the minimum surface area.  First, rewrite *$S$* as powers of *$r$*.*

$S=πr^{2}+2000r^{-1}$

$\frac{dS}{dr}=2πr-2000r^{-2}$

**[1]**

> *When the surface area is at its minimum, *$\frac{dS}{dr}=0$*.*

$\frac{dS}{dr}=2πr-2000r^{-2}=0$

**[1]**

> *Solve to find *$r$*.*

$2πr-\frac{2000}{r^{2}}=0$

> *Multiply through by *$r^{2}$*.*

`| 2 pi r ^3 - 2000 | = 0 | 2 pi r ^3 | = 2000 | r = cbrt( 1000 / pi ) | |`

**[1]**

> *Substitute this value into the formula for *$S$*.*

`| S = pi ( cbrt( 1000 / pi ) ) ^2 + (2000)/(( cbrt( 1000 / pi ) )) | | S = 439.377 566 ... | |`

**[1]**

**The minimum surface area is **$439\mathrm{cm}^{2}$** ****(3 s.f.)**** ****[1]**

### Q26
> *Differentiate the equation using quotient rule and chain rule.*

> $u = \ln ( 3 x^{2} - 5 )$*    *$v=2x+1$

$\frac{ \mathrm{d} u}{ \mathrm{d} x} = ( \frac{1}{3 x^{2} - 5} ) \times 6 x$*    *$\frac{dv}{dx}=2$

**correct **$\frac{du}{dx}$**[1]**

> *Use quotient rule, *$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{( v ) ( \frac{ \mathrm{d} u}{ \mathrm{d} x} ) - ( u ) ( \frac{ \mathrm{d} v}{ \mathrm{d} x} )}{v^{2}}$*.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{( ( 2 x + 1 ) ( \frac{6 x}{3 x^{2} - 5} ) ) - ( 2 ) ( \ln ( 3 x^{2} - 5 ) )}{( 2 x + 1 )^{2}}$

** ****quotient rule**** [1]**
** ****all terms correct except **$\frac{6x}{3x^{2}-5}$** [1]**

> *When *$x=\sqrt{2}$*,*

$y = \frac{\ln ( 1 )}{2 \sqrt{2} + 1}$

> $\ln ( 1 ) = 0$*, therefore when *$x=\sqrt{2}$*,*

$y=0$

**[1]**

> *Substitute *$x=\sqrt{2}$* into *$\frac{dy}{dx}$* to find the gradient of the curve at this point.*

$\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{( 2 \sqrt{2} + 1 ) ( \frac{6 \sqrt{2} }{3 ( \sqrt{2} )^{2} - 5} ) - 2 \ln ( 3 ( \sqrt{2} )^{2} - 5 )}{( 2 \sqrt{2} + 1 )^{2}} \\ \\ = \frac{( \frac{( 2 \sqrt{2} + 1 ) ( 6 \sqrt{2} )}{1} ) - 2 \ln ( 1 )}{( 2 \sqrt{2} + 1 )^{2}} \\ \\ = \frac{( 2 \sqrt{2} + 1 ) ( 6 \sqrt{2} )}{( 2 \sqrt{2} + 1 )^{2}} \\ \\ = \frac{6 \sqrt{2} }{2 \sqrt{2} + 1} \end{gathered}$

> *Take the negative reciprocal to find the gradient of the normal.*

$\text{gradient} ( \text{normal} ) = - \frac{2 \sqrt{2} + 1}{6 \sqrt{2} }$

> *Substitute this gradient and the point *$( \sqrt{2} , 0 )$* into the equation of line, *$y - y_{1} = m ( x - x_{1} )$*.*

$\begin{gathered} y - 0 & = - \frac{2 \sqrt{2} + 1}{6 \sqrt{2} } ( x - \sqrt{2} ) \end{gathered}$

**[1]**

$\begin{gathered} y = - \frac{( 2 \sqrt{2} + 1 ) ( x - \sqrt{2} )}{6 \sqrt{2} } \\ \\ y = - 0.451 184... x + 0.638 071... \end{gathered}$

$y=-0.451x+0.638(3s.f.)$* ***[1]**
> *As is small, use *$"\mathrm{change} \mathrm{in}y=\mathrm{gradient}\times\mathrm{change} \mathrm{in}x"$*.*

$\begin{gathered} \text{change} \text{in} y & = \frac{6 \sqrt{2} }{2 \sqrt{2} + 1} \times h \\ = 2.216 388... \end{gathered}$

**The approximate change in **$y$** is **$2.2h$ **[1]**

### Q27
> *This function is in the form *$y=\frac{u}{v}$* so use the quotient rule, *$\frac{dy}{dx}=\frac{v\frac{du}{dx}-u\frac{dv}{dx}}{v^{2}}$*.*

$u=\mathrm{tan}3xv=\mathrm{sin}x$

$\frac{du}{dx}=3\mathrm{sec}^{2}3x\frac{dv}{dx}=\mathrm{cos}x$

** for **$3\mathrm{sec}^{2}3x$** [1]**

> *Substitute these into the quotient rule.*

$\frac{dy}{dx}=\frac{\mathrm{sin}x\times3\mathrm{sec}^{2}3x-\mathrm{tan}3x\times\mathrm{cos}x}{\mathrm{sin}^{2}x}$

** **** using the quotient rule ****[1]**
** ****all terms correct**** [1]**

> *Use *$\mathrm{sec}x=\frac{1}{\mathrm{cos}x}$* to evaluate *$\mathrm{sec}^{2}3x$*.  *

$\frac{d y}{d x} = \frac{\sin x \times 3 ( \frac{ 1 }{\cos ^{2} 3 x} ) - \tan 3 x \times \cos x}{\sin ^{2} x}$

> *Substitute *$x=\frac{π}{3}$*.*

$\frac{dy}{dx}=2\sqrt{3}$ **[1]**
> *As *$h$* is small, use *$"\mathrm{change} \mathrm{in}y=\mathrm{gradient}\times\mathrm{change} \mathrm{in}x"$*.*

> *From part (a), at *$x=\frac{π}{3}$*,*$\frac{dy}{dx}=2\sqrt{3}$*.*

$\mathrm{change} \mathrm{in}y=2\sqrt{3}\timesh=3.464101...$

**The approximate change in **$y$** is **$3.5h$ **[1]**
> *This is a connected rates of change question, so use chain rule.*

$\frac{dy}{dt}=\frac{dy}{dx}\times\frac{dx}{dt}$

> *The question states that *$x$* is increasing at the rate of 3 units per second.*

$\frac{dx}{dt}=3$

> *From part (a), at *$x=\frac{π}{3}$*.*

$\frac{dy}{dx}=2\sqrt{3}$

**[1]**

$\therefore\frac{dy}{dt}=2\sqrt{3}\times3$

$\frac{dy}{dt}=6\sqrt{3}$** [1]**

### Q28
*To differentiate *$y = \ln ( 1 + \sin x )$, *we can use the fact that the differential of *$\mathrm{ln}x$* is *$\frac{1}{x}$* and chain rule.*

$\frac{dy}{dx}=\frac{1}{1+\mathrm{sin}x}\times\mathrm{cos}x$

$\frac{1}{1+\mathrm{sin}x}$** [1]**

$\frac{dy}{dx}=\frac{\mathrm{cos}x}{1+\mathrm{sin}x}$* ***[1]**
*From part (**a)**, we know that* $\frac{dy}{dx}=\frac{\mathrm{cos}x}{1+\mathrm{sin}x}$.

*Substitute* $x=\frac{π}{6}$ *into *$\frac{dy}{dx}$*.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{ \text{cos} ( \frac{pi}{6} ) }{1 + \text{sin} ( \frac{pi}{6} ) }$

**[1]**

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{( \frac{ \sqrt{3} }{2} )}{ \frac{3}{2} } 
 \frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{ \sqrt{3} }{3}$

> *Rewrite in the form as specified in the question.*

$\frac{dy}{dx}=\frac{1}{\sqrt{3}}$* ***[1]**
*From part (a), we know that *$\frac{dy}{dx}=\frac{\mathrm{cos}x}{1+\mathrm{sin}x}$. *Equate to *$\mathrm{tan}x$* to form a trigonometric equation.*

$\frac{\mathrm{cos}x}{1+\mathrm{sin}x}=\mathrm{tan}x$

> *Use *$\mathrm{tan}x=\frac{\mathrm{sin}x}{\mathrm{cos}x}$* to simplify.*

$\frac{\mathrm{cos}x}{1+\mathrm{sin}x}=\frac{\mathrm{sin}x}{\mathrm{cos}x}$

**[1]**

> *Rearrange.*

$\frac{\cos x}{1 + \sin x} \times \cos x = \sin x
\cos ^{2} x = ( 1 + \sin x ) \sin x
\cos ^{2} x = \sin x + \sin ^{2} x$

> *Use *$\mathrm{cos}^{2}x=1-\mathrm{sin}^{2}x$* to make the equation in terms of *$\mathrm{sin}x$* only.*

$\begin{gathered} 1 - \sin ^{2} x & = \sin x + \sin ^{2} x \end{gathered}$

> *Rearrange.*

$2\mathrm{sin}^{2}x+\mathrm{sin}x-1=0$

**[1]**

> *Factorise this quadratic equation and solve.*

$( 2 \sin x - 1 ) ( \sin x + 1 ) = 0$

$\mathrm{sin}x=\frac{1}{2},\mathrm{sin}x=-1$

$\mathrm{sin}x=-1$* has no solutions in the range *$0<x<π$. $\mathrm{sin}x=\frac{1}{2}$* has two solutions in the range *$0<x<π$*.*

> $\sin ^{- 1} ( 1 \frac{1}{2} ) = \frac{\pi }{6}$* *

> *Considering the graph of *$y=\mathrm{sin}x$* or using *$\sin ( \mathrm{\pi } - x ) = \sin x$*, the second solution can be found.*

$π-\frac{π}{6}=\frac{5π}{6}$

$x=\frac{π}{6}$* and *$x=\frac{5π}{6}$** [2]*** *
**1 mark for each**

### Q29
> *Differentiate using the product rule, *$\frac{dy}{dx}=u\frac{dv}{dx}+v\frac{du}{dx}$*. *

$u=e^{3x}$ *and *$v = ( 2 x + 3 )^{6}$

$\frac{du}{dx}=3e^{3x}$

**[1]**

> *Use the chain rule for *$\frac{dv}{dx}$*.*

$\frac{d v}{d x} = 6 ( 2 x + 3 )^{5 } \times 2 = 12 ( 2 x + 3 )^{5}$

**[1]**

> *Apply product rule.*

$\frac{d y}{d x} = e^{3 x} \times 12 ( 2 x + 3 )^{5 + ( 2 x + 3 )^{6} \times 3 e^{3} x}$

**[1]**

> *Factorise a common factor of *$3e^{3x}$*.*

$\frac{d y}{d x} = 3 e^{3 x} ( 4 ( 2 x + 3 )^{5} + ( 2 x + 3 )^{6} )$

> *Factorise another common factor of *$( 2 x + 3 )^{5}$*.*

$\frac{d y}{d x} = 3 e^{3 x} ( 2 x + 3 )^{5} ( 2 x + 7 )$

**[1]**

> *Stationary points occur when *$\frac{dy}{dx}=0$*.*

$0 = 3 e^{3 x} ( 2 x + 3 )^{5} ( 2 x + 7 )$

> *Solve.*

> $\begin{gathered} 3 e^{3 x} & = 0 \text{no} \text{solutions} \\ ( 2 x + 3 )^{5} & = 0 x = - \frac{3}{2} \\ ( 2 x + 7 ) & = 0 x = - \frac{7}{2} \end{gathered}$*  *

**[1]**

$x=-1.5\mathrm{or}x=-3.5$** [1]**
> *Substituting each value of **x** into the second derivative.*

$\mathrm{f} '' ( 0.5 ) = 4 ( 0.5 ) - 7 = - 5 , - 5 < 0$

$\mathrm{f} '' ( 3 ) = 4 ( 3 ) - 7 = 5 , 5 > 0$

> *A maximum point occurs when *$\mathrm{f} '' ( x ) < 0$* and a minimum point occurs when *$\mathrm{f} '' ( x ) > 0$*.*

**Maximum point at **$x=0.5$ **[1]**

** Minimum point at **$x=3$ **[1]**
> *The volume of the cuboid is*

$4x^{2}h=40$

> *Write *$h$* in terms of *$r$*.*

$x^{2}h=10$

$h=\frac{10}{x^{2}}$

**[1]**

> *The surface area of the cuboid is*

$S = 2 ( 4 x^{2} ) + 2 x h + 2 ( 4 x h )$

$S=8x^{2}+10xh$

> *Substitute in the expression of *$h$*.*

$S = 8 x^{2} + 10 x ( \frac{10}{x^{2}} )$

**[1]**

> *Simplify.*

$S=8x^{2}+\frac{100}{x}$

> *Differentiate *$S$* to find the minimum value but first rewrite as powers of *$x$*.*

$\begin{gathered} S = 8 x^{2} + 100 x^{- 1} \\ \frac{ \mathrm{d} S}{ \mathrm{d} t} & = 16 x - 100 x^{- 2} \\ \frac{d S}{d x} & = 16 x - \frac{ 100}{x^{2}} \end{gathered}$

**[1]**

> *The minimum value occurs at *$\frac{dS}{dx}=0$*.*

$0=16x-\frac{100}{x^{2}}$

$\frac{100}{x^{2}}=16x$

$100=16x^{3}$

$\frac{25}{4}=x^{3}$

$\sqrt[3]{\frac{25}{4}} = x$

**[1]**

> *Substituting this value into the expression for the surface area.*

$S = 8 ( \sqrt[3]{\frac{25}{4}} ) ^{2} + \frac{ 100}{\sqrt[3]{\frac{25}{4}}}$

$81.4\mathrm{cm}^{2}(3s.f)$* ***[1]**

### Q30
> *Use the quotient rule, i.e. for *$y=\frac{u}{v},\frac{dy}{dx}=\frac{v\frac{du}{dx}-u\frac{dv}{dx}}{v^{2}}$*.*

$u = \ln ( 3 x^{2 } - 1 ) , v = x + 2$

> *Use the chain rule to differentiate the log function.*

$\frac{du}{dx}=\frac{6x}{3x^{2}-1}$

**[1]**

$\frac{dv}{dx}=1$

> *Apply the quotient rule.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{( x + 2 ) \frac{6 x}{3 x^{2 } - 1} - \ln ( 3 x^{2 } - 1 )}{( x + 2 )^{2}}$

**[1]**

> *The gradient at the point *$x=1$* is required.*

$\frac{dy}{dx}=\frac{9-\mathrm{ln}2}{9}=0.922983...$

**[1]**

> *Substitute *$x=1$* to the original equation to find the **y**-coordinate.*

$y=0.231049...$

**[1]**

> *Substitute these values into *$y=mx+c$* to find the equation of the tangent.*

$\begin{gathered} 0.231 049... & = 0.922 983... \times 1 + c \\ c = - 0.691 934... \end{gathered}$

**[1]**

> *Final answer requires values rounded to 3 decimal places.*

$y=0.923x-0.692$* ***[1]**

### Q31
> *Differentiate the equation using the quotient rule and chain rule.*

$u=e^{2x-3}$*    *$v=x^{2}+1$* *

$\frac{du}{dx}=2e^{2x-3}$*  *$\frac{dv}{dx}=2x$*  *

> *Substitute into the quotient rule, *$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{( v ) ( \frac{ \mathrm{d} u}{ \mathrm{d} x} ) - ( u ) ( \frac{ \mathrm{d} v}{ \mathrm{d} x} )}{v^{2}}$*.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{( x^{2} + 1 ) ( 2 \mathrm{e}^{2 x - 3} ) - ( 2 x ) ( \mathrm{e}^{2 x - 3} )}{( x^{2} + 1 )^{2}}$

$2e^{2x-1}$** ****[1] **
**[1]**

> *Split into two fractions and simplify.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{( x^{2} + 1 ) ( 2 \mathrm{e}^{2 x - 3} )}{( x^{2} + 1 )^{2}} - \frac{( 2 x ) ( \mathrm{e}^{2 x - 3} )}{( x^{2} + 1 )^{2}}$

$\frac{dy}{dx}=\frac{(2e^{2x-3})}{(x^{2}+1)}-\frac{(2xe^{2x-3})}{(x^{2}+1)^{2}}$* ***[1]**
> *This is a connected rates of change question, so we shall need chain rule.*

$\frac{dy}{dx}=\frac{dt}{dx}\times\frac{dy}{dt}$

> $y$* is increasing at a rate of 2 units per second, i.e. *$\frac{dy}{dt}=2$*. Substitute *$x=2$* into the equation for*$\frac{dy}{dx}$* from part (a).*

$\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{2 \mathrm{e}^{2 \times 2 - 3} }{2^{2} + 1} - \frac{2 \times 2 \times \mathrm{e}^{2 \times 2 - 3} }{( 2^{2} + 1 )^{2}} \\ \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{2 \mathrm{e} }{5} - \frac{4 \mathrm{e} }{25} \\ \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{6 \mathrm{e} }{25} \end{gathered}$

**[1]**

> *Keep this in terms of e as the question asks for an exact answer. Substitute into chain rule and solve for *$\frac{dt}{dx}$*.*

$\frac{6e}{25}=\frac{dt}{dx}\times2\,\frac{dt}{dx}=\frac{6e}{50}$

> *We want to find *$\frac{dx}{dt}$* so we need the reciprocal of *$\frac{dt}{dx}$*.*

$\frac{dx}{dt}=\frac{50}{6e}$

$\frac{dx}{dt}=\frac{25}{3e}$ **[1]**

### Q32
> *First, divide both sides of the given equation by 2 to make **y** the subject.*

$y=\frac{1}{2}\mathrm{tan}2x+\frac{7}{2}$

> *Differentiate to find the gradient function.*

$\frac{dy}{dx}=\mathrm{sec}^{2}2x$

**[1]**

> *Find the gradient when *$x=\frac{π}{8}$*.*

$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \sec ^{2} ( \frac{2 \mathrm{\pi } }{8} )$

$\frac{dy}{dx}=2$

**[1]**

> *Find *$y$* when *$x=\frac{π}{8}$* by substituting into the original equation.*

`| 2 y | = tan ( 2 x pi / 8 ) + 7 | | y = 4 |`

**[1]**

> *Use the gradient 2 and point *`( pi / 8 , 4 )`* to find the equation of the line. Using point-gradient form, *$" y - y_{1} = m ( x - x_{1} ) "$*,*

`y - 4 = 2 ( x - pi / 8 )`

**[1]**

> *Expand the bracket.*

$y-4=2x-\frac{π}{4}$

> *Subtract *$y$* and add *$\frac{π}{4}$* to both sides to obtain the required form *$ax-y=\frac{π}{b}+c$*.*

$2x-y=\frac{π}{4}-4$ **[1]**
> *From part (a), the equation of the tangent is *$2x-y=\frac{π}{4}-4$*. *
*The tangent will intersect the *$x$*-axis when *$y=0$*, so substitute *$y=0$* to find the *$x$*coordinate *$P$*.*

`| 2 x - 0 | = pi / 4 - 4 | | x = pi / 8 - 2 | |`

`P ( pi / 8 - 2 , 0 )`

> *The tangent will intersect the *$y$*-axis when *$x=0$*, so substitute *$x=0$* to find the *$y$* coordinate of *$Q$*.*

`| 0 - y | = pi / 4 - 4 | | y = 4 - pi / 4 | |`

`Q ( 0 , 4 - pi / 4 )`

> *Calculate the distance between the points to find the length of *$PQ$* using Pythagoras' theorem.*

`P Q = sqrt( ( pi / 8 - 2 ) ^2 + ( pi / 4 - 4 ) ^2 )`

**[1]**

$PQ=3.594...$

**The length of **$PQ$** is **$3.59(3s.f.)$ **[1]**
