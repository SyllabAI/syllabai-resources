## Common Errors & Fixes

### i. Unmatched Braces

$\Rightarrow$Mistake: `$x^{2+3$` $\rightarrow$ `Invalid Equation`

$\Rightarrow$Fix: `$x^{2+3}$` $\rightarrow$ $x^{2+3}$

### ii. Using \left with \right

$\Rightarrow$`\left` and `\right` must be used together

$\Rightarrow$Mistake: `$\left( x+1 )$` $\rightarrow$ `Invalid Equation`

$\Rightarrow$Fix: `$\left(x+1\right)$` $\rightarrow$ $\left(x+1\right)$

### iii. Using Text in Math Mode without \text{}

$\Rightarrow$Mistake: `$x = 2 or x = \sqrt{5}$` $\rightarrow$ $x = 2 or x =\sqrt{5}$

$\Rightarrow$Fix: `$x = 2 \text{ or } x = \sqrt{5}$` $\rightarrow$ $x = 2 \text{ or } x = \sqrt{5}$

### iv. Forgetting Closing Dollar Sign

$\Rightarrow$`$x + y = z` $\rightarrow$ x + y = z (not in Math mode)

$\Rightarrow$Fix: `$x + y = z$` $\rightarrow$ $x + y = z$

### v. Mixing Inline & Display Math

$\Rightarrow$ `$x^2$` $\rightarrow$ `$x^2$$`