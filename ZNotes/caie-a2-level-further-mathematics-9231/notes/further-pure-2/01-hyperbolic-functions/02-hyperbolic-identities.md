## Hyperbolic Identities

* Osborne’s Rule:

  “To move from a trig identity to a hyperbolic identity: change cos to cosh and change the sign a product of sinhs.”
* List of identities:
  * $cosh^2x - sinh^2x ≡ 1$
  * $tanh^2x + sech^2x ≡ 1$
  * $coth^2x - csch^2x ≡ 1$
  * $sinh(A+B) ≡ sinhAcoshB + coshAsinhB$
  * $cosh(A+B) ≡ coshAcoshB + sinhAsinhB$
  * $coshx + sinhx = e^x$
  * $coshx - sinhx = e^{-x}$

| 9231/02/SP/20                                                                                     Question 7: |
|----|
| a) Starting from the definition of tanh in terms of exponentials, prove that $tanh^{-1}x = \frac{1}{2} ln \frac{1+x}{1-x}$ |
| b) Given that $y = tanh^{-1}{\frac{1-x}{2+x}}$, show that $(2x+1)\frac{dy}{dx} + 1 = 0$ |
| **Solution:** |
| a) Using $tanhx = \frac{e^{2x}-1}{e^{2x}+1}$ we have: |
| $y =\frac{e^{2x}-1}{e^{2x}+1}$ |
| Substitute $u$ = $e^x$ and solve for $u$ |
| $y = \frac{u^2-1}{u^2+1}$ |
| $yu^2+y=u^2-1$ |
| $(y-1)u^2=-y-1$ |
| $u^2 = \frac{1+y}{1-y}$ |
| Substitute back and solve for $x$: |
| $e^{2x} = \frac{1+y}{1-y}$ |
| → $2x = ln(\frac{1+y}{1-y})$ |
| → $x = \frac{1}{2}ln(\frac{1+y}{1-y})$ |
| Switch all $x$ with $y$ |
| $y = \frac{1}{2}ln(\frac{1+x}{1-x})$ (answer) |
| b) Use the Logarithmic definition for $tanh^{-1}(x)$ and substitute in: |
| $y = \frac{1}{2}ln(\frac{1+ \frac{1+x}{1-x}}{1- \frac{1+x}{1-x}})$ |
| Simplify it: |
| $y = \frac{1}{2}ln(\frac{3}{1+2x})$ |
| Differentiate |
| $\frac{dy}{dx}$ = $\frac{1}{2} \times -2(\frac{3}{(1+2x)^2}) \times \frac{1+2x}{3}$ |
| → $\frac{dy}{dx}$ = $- \frac{1}{1+2x}$ |
| → $(1+2x) \frac{dy}{dx} = -1$ |
| → $(1+2x)\frac{dy}{dx} +1 =0$ |
| (Answer) |



