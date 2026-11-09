# Binomial Expansion Flashcards

_Lane: `a-level-maths-edexcel` · grade — · 22 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** How is $\frac{1}{(2+3x)^2}$ expressed as a power of a binomial?

**Back:** $$(2+3x)^{-2}$

**Choices:**

- $$(2+3x)^{-2}$ ✔
  - _why:_ A reciprocal squared is equivalent to raising the entire bracket to the power $-2$: $(2+3x)^{-2}=\frac{1}{(2+3x)^2}$.
- $$(2+3x)^2$
  - _why:_ A positive power gives $(2+3x)^2$, not its reciprocal. Writing a denominator as a power requires a negative exponent, so the correct form is $(2+3x)^{-2}$.
- $$(2+3x)^{-1}$
  - _why:_ The exponent must match the denominator’s power as well as its reciprocal nature. A squared denominator therefore gives exponent $-2$, not $-1$.
- $$(2+3x)^{2}$
  - _why:_ A positive exponent represents multiplication by the bracket rather than division by its square. The reciprocal square is written with exponent $-2$: $(2+3x)^{-2}$.

## Card 2 — `basic`

**Front:** How is $\sqrt{1+6x}$ rewritten as a binomial power?

**Back:** $$(1+6x)^{\frac{1}{2}}$

**Choices:**

- $$(1+6x)^{\frac{1}{2}}$ ✔
  - _why:_ A square root is equivalent to raising an expression to the power $\frac{1}{2}$, so $\sqrt{1+6x}=(1+6x)^{\frac{1}{2}}$.
- $$(1+6x)^2$
  - _why:_ The power $2$ means squaring the expression, whereas a square root corresponds to the reciprocal power $\frac{1}{2}$. Thus the correct form is $(1+6x)^{\frac{1}{2}}$.
- $$(1+6x)^{-\frac{1}{2}}$
  - _why:_ The negative half-power represents the reciprocal of the square root. Since the original expression is a square root rather than its reciprocal, the exponent is $\frac{1}{2}$.
- $$(1+6x)^{\frac{1}{3}}$
  - _why:_ A power of $\frac{1}{3}$ represents a cube root, not a square root. Square roots use the exponent $\frac{1}{2}$, giving $(1+6x)^{\frac{1}{2}}$.

## Card 3 — `cloze`

**Front:** A binomial expansion is finite (stops) if the power $n$ is a [ ___ ].

**Back:** A binomial expansion is finite (stops) if the power $n$ is a non-negative integer.

**Choices:**

- non-negative integer ✔
  - _why:_ When $n$ is a non-negative integer, the binomial coefficients eventually contain a factor of zero, so all later terms vanish and the expansion stops.
- positive integer
  - _why:_ A positive integer does produce a finite expansion, but it excludes the valid case $n=0$. The complete condition is that $n$ is a non-negative integer.
- negative integer
  - _why:_ Negative integer powers generally produce an infinite expansion rather than one that stops. Finite binomial expansions require $n$ to be a non-negative integer.
- non-integer
  - _why:_ Fractional powers are not generally finite; their binomial expansions continue indefinitely. The expansion stops when $n$ is a non-negative integer.

## Card 4 — `basic`

**Front:** In the expansion of $(a+b)^n$, what is the formula for the binomial coefficient $\binom{n}{r}$?

**Back:** $$$\frac{n!}{r!(n-r)!}$$

**Choices:**

- $$$\frac{n!}{r!(n-r)!}$$ ✔
  - _why:_ The binomial coefficient counts the coefficient of the term involving $r$ factors of $b$ and is given by $\binom{n}{r}=\frac{n!}{r!(n-r)!}$.
- $$$\frac{n!}{r!(n+r)!}$$
  - _why:_ The factorial should contain $n-r$, because choosing $r$ factors leaves $n-r$ factors. Using $n+r$ gives the wrong coefficient; the correct denominator is $r!(n-r)!$.
- $$$\frac{r!}{n!(n-r)!}$$
  - _why:_ The factorial $n!$ belongs in the numerator, representing the total arrangements before dividing by repeated arrangements. The correct coefficient is $\frac{n!}{r!(n-r)!}$.
- $$$\frac{n!}{(n-r)!}$$
  - _why:_ This expression omits the factor $r!$, which is needed to account for repeated arrangements of the selected factors. The complete formula is $\frac{n!}{r!(n-r)!}$.

## Card 5 — `basic`

**Front:** State the first three terms of the general binomial expansion for $(1+u)^n$.

**Back:** $1$$nu$$\frac{n(n-1)}{2}u^2$

**Choices:**

- $1$$nu$$\frac{n(n-1)}{2}u^2$ ✔
  - _why:_ The general expansion begins with the constant term, then the first power of $u$, followed by the second-power term with coefficient $\binom{n}{2}=\frac{n(n-1)}{2}$.
- $1$$nu$$\frac{n(n+1)}{2}u^2$
  - _why:_ The second coefficient uses two consecutive descending factors, $n(n-1)$, not $n(n+1)$. Therefore the third term is $\frac{n(n-1)}{2}u^2$.
- $1$$nu^2$$\frac{n(n-1)}{2}u^3$
  - _why:_ Each successive term increases the power of $u$ by one, beginning with $u$ in the second term. The first three terms therefore end with $\frac{n(n-1)}{2}u^2$.
- $1$$(n-1)u$$\frac{n(n-1)}{2}u^2$
  - _why:_ The coefficient of the first-power term is $\binom{n}{1}=n$, not $n-1$. The correct first three terms are $1$, $nu$, and $\frac{n(n-1)}{2}u^2$.

## Card 6 — `cloze`

**Front:** For a fractional or negative power $n$, the expansion of $(1+u)^n$ is only valid when $\text{[...]}$.

**Back:** For a fractional or negative power $n$, the expansion of $(1+u)^n$ is only valid when $\boxed{|u|<1}$.

**Choices:**

- $$|u|<1$ ✔
  - _why:_ For fractional or negative powers, the general binomial series converges when the magnitude of $u$ is less than $1$, ensuring that successive terms decrease appropriately.
- $$|u|\leq 1$
  - _why:_ The endpoints $u=1$ or $u=-1$ are not generally included in the standard validity condition. The required condition is the strict inequality $|u|<1$.
- $$|u|>1$
  - _why:_ If $|u|>1$, powers of $u$ do not generally decrease, so the binomial series is not valid in the usual way. The condition is $|u|<1$.
- $$|u|<0$
  - _why:_ An absolute value cannot be negative, so $|u|<0$ is impossible. The convergence condition requires the non-negative magnitude of $u$ to be less than $1$: $|u|<1$.

## Card 7 — `basic`

**Front:** Why must $(9+6x)^{-\frac{1}{2}}$ be factored before using the general binomial expansion formula?

**Back:** The formula requires the constant term inside the bracket to be 1.

**Choices:**

- The formula requires the constant term inside the bracket to be 1. ✔
  - _why:_ The standard binomial formula is applied to $(1+u)^n$, so the expression must first be factored to make the constant inside the bracket equal to 1.
- The formula requires the constant term inside the bracket to be 0.
  - _why:_ A zero constant would not produce the standard form $(1+u)^n$. Factoring is needed to make the constant inside the bracket 1.
- The formula requires the coefficient of $x$ inside the bracket to be 1.
  - _why:_ The coefficient of $x$ may be any suitable value and becomes part of $u$. It is the constant term that must be normalised to 1.
- The formula requires the exponent outside the bracket to be 1.
  - _why:_ The exponent $-\frac{1}{2}$ is the value being expanded and must not be changed. Factoring makes the constant term inside the bracket equal to 1.

## Card 8 — `basic`

**Front:** Outline the two steps to factor $(a+bx)^n$ into standard binomial form.

**Back:** Factor $a$ out of the bracket: $a(1+\frac{b}{a}x)$Apply the power to both parts: $a^n(1+\frac{b}{a}x)^n$

**Choices:**

- Factor $a$ out of the bracket: $a(1+\frac{b}{a}x)$Apply the power to both parts: $a^n(1+\frac{b}{a}x)^n$ ✔
  - _why:_ Factoring $a$ rewrites the bracket with constant term $1$, then the power applies to both the extracted factor and the standard binomial bracket, giving $a^n(1+\frac{b}{a}x)^n$.
- Factor $b$ out of the bracket: $b(1+\frac{a}{b}x)$Apply the power to both parts: $b^n(1+\frac{a}{b}x)^n$
  - _why:_ Factoring $b$ in this way does not preserve the original expression’s terms: $b(1+\frac{a}{b}x)$ has constant term $b$ and changes the placement of $x$. Factor $a$ instead.
- Factor $a$ out of the bracket: $a(1+\frac{b}{a}x)$Apply the power only to the bracket: $a(1+\frac{b}{a}x)^n$
  - _why:_ The extracted factor is also raised to the power, by $(pq)^n=p^nq^n$. Omitting this gives $a$ instead of $a^n$, so the final form is $a^n(1+\frac{b}{a}x)^n$.
- Factor $a$ out of the bracket: $a(1+\frac{b}{a}x)$Apply the power to both parts: $a^n(1+\frac{b}{a}x)^{n+1}$
  - _why:_ Factoring does not alter the original exponent, so the bracket remains raised to $n$. Changing it to $n+1$ changes the expression; the correct result is $a^n(1+\frac{b}{a}x)^n$.

## Card 9 — `cloze`

**Front:** To expand $(9+6x)^{-\frac{1}{2}}$, it is factored into $\text{[...]}$ $\times$ $(1+\frac{2}{3}x)^{-\frac{1}{2}}$.

**Back:** To expand $(9+6x)^{-\frac{1}{2}}$, it is factored into $\boxed{9^{-\frac{1}{2}}}$ $\times$ $(1+\frac{2}{3}x)^{-\frac{1}{2}}$.

**Choices:**

- $$9^{-\frac{1}{2}}$ ✔
  - _why:_ Factoring gives $9+6x=9(1+\frac{2}{3}x)$. Raising both factors to the power $-\frac{1}{2}$ produces the required outside factor $9^{-\frac{1}{2}}$.
- $$9^{\frac{1}{2}}$
  - _why:_ The negative exponent has been omitted from the extracted factor. Since the entire bracket is raised to $-\frac{1}{2}$, the correct outside factor is $9^{-\frac{1}{2}}$.
- $$3^{-\frac{1}{2}}$
  - _why:_ This incorrectly replaces the extracted base 9 with its square root. Factoring out 9 before applying the exponent gives the outside factor $9^{-\frac{1}{2}}$.
- $$9^{-1}$
  - _why:_ This applies an exponent of $-1$ rather than the original exponent of $-\frac{1}{2}$. The extracted factor must therefore be $9^{-\frac{1}{2}}$.

## Card 10 — `cloze`

**Front:** To expand $(9+6x)^{-\frac{1}{2}}$, it is factored into $9^{-\frac{1}{2}}$ $\times$ $\text{[...]}$.

**Back:** To expand $(9+6x)^{-\frac{1}{2}}$, it is factored into $9^{-\frac{1}{2}}$ $\times$ $\boxed{(1+\frac{2}{3}x)^{-\frac{1}{2}}}$.

**Choices:**

- $$(1+\frac{2}{3}x)^{-\frac{1}{2}}$ ✔
  - _why:_ Because $9+6x=9(1+\frac{2}{3}x)$, applying the exponent $-\frac{1}{2}$ to each factor gives this standard binomial form.
- $$(1+6x)^{-\frac{1}{2}}$
  - _why:_ This fails to divide $6x$ by the extracted factor 9. The inner coefficient is $\frac{6}{9}=\frac{2}{3}$, so the correct bracket is $(1+\frac{2}{3}x)^{-\frac{1}{2}}$.
- $$(1+\frac{3}{2}x)^{-\frac{1}{2}}$
  - _why:_ The fraction has been inverted: extracting 9 requires dividing 6 by 9, not 9 by 6. The correct coefficient of $x$ is $\frac{2}{3}$.
- $$(1+\frac{2}{3}x)^{\frac{1}{2}}$
  - _why:_ The bracket retains the original negative exponent after factorisation. Changing it to $\frac{1}{2}$ changes the function, so the correct exponent is $-\frac{1}{2}$.

## Card 11 — `basic`

**Front:** What is the range of validity for the expansion of $(1-2x)^{-3}$?

**Back:** $$$|x| < \frac{1}{2}$$ or $$-\frac{1}{2} < x < \frac{1}{2}$$

**Choices:**

- $$$|x| < \frac{1}{2}$$ or $$-\frac{1}{2} < x < \frac{1}{2}$$ ✔
  - _why:_ A generalised binomial expansion in the form $(1+u)^n$ is valid for $|u|<1$. Here $u=-2x$, giving $|-2x|<1$ and hence $|x|<\frac{1}{2}$.
- $$$|x| \leq \frac{1}{2}$$ or $$-\frac{1}{2} \leq x \leq \frac{1}{2}$$
  - _why:_ The endpoints cannot be included because this infinite expansion does not converge there. Applying $|-2x|<1$ gives the strict range $|x|<\frac{1}{2}$.
- $$$|x| < 1$$ or $$-1 < x < 1$$
  - _why:_ This overlooks the coefficient 2 multiplying $x$. The condition is $|-2x|<1$, so dividing by 2 gives $|x|<\frac{1}{2}$, not $|x|<1$.
- $$$|x| < 2$$ or $$-2 < x < 2$$
  - _why:_ This multiplies the standard boundary by 2 instead of dividing by 2. Since the binomial variable is $-2x$, the correct range is $|x|<\frac{1}{2}$.

## Card 12 — `basic`

**Front:** When using an expansion to approximate a value, why are smaller values of $x$ more accurate?

**Back:** Higher powers of $x$ ($x^2, x^3, \dots$) become negligibly small, making the first few terms a closer fit.

**Choices:**

- Higher powers of $x$ ($x^2, x^3, \dots$) become negligibly small, making the first few terms a closer fit. ✔
  - _why:_ When $|x|$ is small, successive powers decrease rapidly in magnitude. Terms beyond those retained therefore contribute very little, reducing the truncation error in the approximation.
- Higher powers of $x$ ($x^2, x^3, \dots$) become increasingly large, making the first few terms a closer fit.
  - _why:_ Powers of a small $x$ decrease rather than increase, so later terms contribute less. The approximation improves because higher powers become negligibly small.
- Higher powers of $x$ ($x^2, x^3, \dots$) become exactly zero, making the first few terms a closer fit.
  - _why:_ The powers do not become exactly zero unless $x=0$. For small non-zero $x$, they are merely negligibly small, so omitting later terms causes only a small error.
- Higher coefficients of $x$ ($x^2, x^3, \dots$) become negligibly small, making the first few terms a closer fit.
  - _why:_ Small values of $x$ do not make the binomial coefficients vanish. Accuracy improves because the higher powers of $x$ become negligibly small, reducing the contribution of omitted terms.

## Card 13 — `cloze`

**Front:** In the term $6x^2$, the number 6 is the [ ___ ] and $6x^2$ is the term.

**Back:** In the term $6x^2$, the number 6 is the coefficient and $6x^2$ is the term.

**Choices:**

- coefficient ✔
  - _why:_ A coefficient is the numerical factor multiplying the variable part of a term. In $6x^2$, 6 multiplies $x^2$, so it is the coefficient.
- exponent
  - _why:_ The exponent is the raised number 2, which specifies the power of $x$. The number 6 multiplies $x^2$, so the correct term is coefficient.
- variable
  - _why:_ The variable is $x$, since its value may vary. The number 6 is the numerical multiplier of $x^2$, so it is called the coefficient.
- power
  - _why:_ The power in this expression is 2, as shown by the exponent on $x$. The number 6 is instead the coefficient multiplying the variable part.

## Card 14 — `cloze`

**Front:** In the term $6x^2$, the number 6 is the coefficient and $6x^2$ is the [ ___ ].

**Back:** In the term $6x^2$, the number 6 is the coefficient and $6x^2$ is the term.

**Choices:**

- term ✔
  - _why:_ A term is a complete part of an algebraic expression separated from other parts by addition or subtraction. Here the complete product $6x^2$ is one term.
- coefficient
  - _why:_ Only the numerical multiplier 6 is the coefficient. The complete product $6x^2$, including its variable and exponent, is called the term.
- variable
  - _why:_ The variable is $x$, not the whole product containing it. The complete algebraic component $6x^2$ is correctly described as the term.
- exponent
  - _why:_ The exponent is the raised number 2, which indicates the power of $x$. The entire expression $6x^2$ is the term.

## Card 15 — `basic`

**Front:** What does it mean to write an expansion in "ascending powers of $x$"?

**Back:** Terms are written in order of increasing powers: constant term first, then $x$, then $x^2$, etc.

**Choices:**

- Terms are written in order of increasing powers: constant term first, then $x$, then $x^2$, etc. ✔
  - _why:_ Ascending order means each successive term has a larger exponent of $x$. Since a constant is associated with $x^0$, it comes before $x^1$, $x^2$, and later powers.
- Terms are written in order of decreasing powers: highest power first, then $x^2$, then $x$, etc.
  - _why:_ This describes descending rather than ascending powers. Ascending order begins with the constant term, followed by $x$, then $x^2$, and so on.
- Terms are written in order of increasing coefficients: smallest coefficient first, then larger coefficients, etc.
  - _why:_ The coefficients do not determine whether powers are ascending. The exponents must increase, so the constant term comes first, followed by $x$, $x^2$, and later powers.
- Terms are written in alphabetical order of variables: first variable first, then later variables, etc.
  - _why:_ Alphabetical ordering is unrelated to powers of a variable. Ascending powers means ordering by increasing exponents, beginning with the constant term, then $x$, then $x^2$.

## Card 16 — `basic`

**Front:** Find the range of validity for the expansion of $(9+6x)^{-\frac{1}{2}}$.

**Back:** $$$|x| < \frac{3}{2}$$ or $$-\frac{3}{2} < x < \frac{3}{2}$$

**Choices:**

- $$$|x| < \frac{3}{2}$$ or $$-\frac{3}{2} < x < \frac{3}{2}$$ ✔
  - _why:_ After factorisation, the binomial variable is $u=\frac{2}{3}x$. Requiring $|u|<1$ gives $|\frac{2}{3}x|<1$, so $|x|<\frac{3}{2}$.
- $$$|x| < \frac{2}{3}$$ or $$-\frac{2}{3} < x < \frac{2}{3}$$
  - _why:_ This uses the reciprocal inequality incorrectly. From $|\frac{2}{3}x|<1$, multiplying by $\frac{3}{2}$ gives the correct boundary $|x|<\frac{3}{2}$.
- $$$|x| < 1$$ or $$-1 < x < 1$$
  - _why:_ This treats $x$ itself as the binomial variable and ignores its coefficient. Since the expanded bracket contains $\frac{2}{3}x$, the correct range is $|x|<\frac{3}{2}$.
- $$$|x| \leq \frac{3}{2}$$ or $$-\frac{3}{2} \leq x \leq \frac{3}{2}$$
  - _why:_ The endpoints are excluded because the generalised binomial series requires the bracket’s variable to have modulus strictly below 1. Thus the correct inequality is $|x|<\frac{3}{2}$.

## Card 17 — `cloze`

**Front:** To estimate $\sqrt{8.8}$ using $(9-2x)^{\frac{1}{2}}$, you must substitute $x = $ $\text{[...]}$.

**Back:** To estimate $\sqrt{8.8}$ using $(9-2x)^{\frac{1}{2}}$, you must substitute $x = $ $\boxed{0.1}$.

**Choices:**

- $$0.1$ ✔
  - _why:_ Setting $9-2x=8.8$ gives $2x=0.2$, so $x=0.1$. This makes the binomial expression exactly equal to $[8.8[0m$ before expansion.
- $$0.2$
  - _why:_ This comes from using $9-x=8.8$ and forgetting the coefficient $2$. Solving the actual equation $9-2x=8.8$ gives $x=0.1$.
- $$-0.1$
  - _why:_ This sign results from treating $8.8$ as greater than $9$. Since $9-2x$ must decrease to $8.8$, solving gives the positive value $x=0.1$.
- $$0.02$
  - _why:_ This confuses the required substitution with the difference $9-8.8$. That difference equals $2x$, so it must be halved to obtain $x=0.1$.

## Card 18 — `basic`

**Front:** When multiplying $(1+x)$ by an expansion to find terms up to $x^3$, which product involving $x^3$ is ignored?

**Back:** $$x \cdot x^3$ (or any term resulting in $x^4$ or higher).

**Choices:**

- $$x \cdot x^3$ (or any term resulting in $x^4$ or higher). ✔
  - _why:_ Multiplying the outside $x$ by an $x^3$ term produces an $x^4$ term. Since only terms through $x^3$ are required, it is ignored.
- $$1 \cdot x^3$ (or any term resulting in $x^3$ or higher).
  - _why:_ Multiplying by $1$ leaves the power unchanged, producing an $x^3$ term that must be retained. The ignored product is $x \cdot x^3$, which produces $x^4$.
- $$x \cdot x^2$ (or any term resulting in $x^3$ or higher).
  - _why:_ The product $x \cdot x^2$ contributes to the required $x^3$ coefficient, so omitting it would give an incorrect expansion. Only products producing $x^4$ or higher are ignored.
- $$1 \cdot x^2$ (or any term resulting in $x^2$ or higher).
  - _why:_ The product $1 \cdot x^2$ remains an $x^2$ term and lies within the requested range. The product $x \cdot x^3$ is ignored because it gives $x^4$.

## Card 19 — `basic`

**Front:** If the expansion of $\frac{a+bx}{\sqrt{4+x}}$ begins with $2+x$, how is the value of $a$ determined?

**Back:** Expand $(4+x)^{-\frac{1}{2}}$ to get $\frac{1}{2} - \dots$Multiply by $(a+bx)$ to find the constant term $\frac{a}{2}$Equate $\frac{a}{2} = 2$

**Choices:**

- Expand $(4+x)^{-\frac{1}{2}}$ to get $\frac{1}{2} - \dots$Multiply by $(a+bx)$ to find the constant term $\frac{a}{2}$Equate $\frac{a}{2} = 2$ ✔
  - _why:_ The denominator factor is expanded with exponent $-\frac{1}{2}$, whose constant term is $\frac{1}{2}$. Thus the product has constant term $\frac{a}{2}=2$, giving $a=4$.
- Expand $(4+x)^{-\frac{1}{2}}$ to get $\frac{1}{4} - \dots$Multiply by $(a+bx)$ to find the constant term $\frac{a}{4}$Equate $\frac{a}{4} = 2$
  - _why:_ This uses $\frac{1}{4}$ as the constant term, confusing $4^{-1}$ with $4^{-1/2}$. In fact, $4^{-1/2}=\frac{1}{2}$, so $\frac{a}{2}=2$.
- Expand $(4+x)^{\frac{1}{2}}$ to get $2 + \dots$Multiply by $(a+bx)$ to find the constant term $2a$Equate $2a = 2$
  - _why:_ This mistakenly uses exponent $\frac{1}{2}$, which expands the denominator rather than its reciprocal. The required exponent is $-\frac{1}{2}$, giving constant term $\frac{a}{2}$.
- Expand $(4+x)^{-\frac{1}{2}}$ to get $\frac{1}{2} - \dots$Add $(a+bx)$ to find the constant term $a+\frac{1}{2}$Equate $a+\frac{1}{2} = 2$
  - _why:_ The constant term of a product comes from multiplying the two constant terms, not adding them. It is $a \cdot \frac{1}{2}=\frac{a}{2}$, which must equal $2$.

## Card 20 — `basic`

**Front:** State the $x^3$ term in the general binomial expansion of $(1+u)^n$.

**Back:** $$$\frac{n(n-1)(n-2)}{6}u^3$$

**Choices:**

- $$$\frac{n(n-1)(n-2)}{6}u^3$$ ✔
  - _why:_ The coefficient of $u^3$ is $\binom{n}{3}=\frac{n(n-1)(n-2)}{3!}$. Since $3!=6$, the stated expression is the cubic term.
- $$$n(n-1)(n-2)u^3$$
  - _why:_ This omits the division by $3!=6$ in the binomial coefficient. The cubic term is $\frac{n(n-1)(n-2)}{6}u^3$.
- $$$\frac{n(n+1)(n+2)}{6}u^3$$
  - _why:_ This uses three increasing factors, whereas general binomial coefficients use falling factors from $n$. The cubic coefficient is $\frac{n(n-1)(n-2)}{6}$.
- $$$\frac{n(n-1)}{2}u^3$$
  - _why:_ This is the coefficient pattern for the quadratic term, with an extra $u$. The cubic term requires three falling factors and division by $3!=6$.

## Card 21 — `cloze`

**Front:** If $|u| \ge 1$, the infinite binomial expansion [ ___ ] (should not be used).

**Back:** If $|u| \ge 1$, the infinite binomial expansion is not valid (should not be used).

**Choices:**

- is not valid ✔
  - _why:_ The standard infinite binomial series has radius of convergence $1$, so it is used only when $|u|<1$. Values with $|u|\ge 1$ fall outside that condition.
- is always valid
  - _why:_ This reverses the convergence condition. The standard infinite binomial expansion is valid for $|u|<1$, not generally for $|u|\ge 1$.
- converges absolutely
  - _why:_ Absolute convergence is guaranteed inside the radius $|u|<1$, not for all values on or beyond its boundary. Therefore the expansion is not valid under the stated condition.
- can be used freely
  - _why:_ This ignores the series' radius of convergence. The infinite binomial expansion should be used when $|u|<1$, so it cannot be used without restriction here.

## Card 22 — `basic`

**Front:** How many terms are included when asked for an expansion "up to and including $x^3$"?

**Back:** Four terms: the constant, $x$, $x^2$, and $x^3$.

**Choices:**

- Four terms: the constant, $x$, $x^2$, and $x^3$. ✔
  - _why:_ Counting from the constant term $x^0$ through $x^3$ gives four powers: $x^0$, $x^1$, $x^2$, and $x^3$.
- Three terms: $x$, $x^2$, and $x^3$.
  - _why:_ This omits the constant term, a common counting error. Including powers from $x^0$ through $x^3$ gives four terms in total.
- Five terms: the constant, $x$, $x^2$, $x^3$, and $x^4$.
  - _why:_ This includes $x^4$, which lies beyond the requested highest power. Stopping at $x^3$ gives the constant term and three variable terms, making four.
- Three terms: the constant, $x$, $x^2$, and $x^3$.
  - _why:_ This incorrectly treats the constant as separate from the term count. The constant is itself the $x^0$ term, so there are four terms altogether.
