# Algebraic Methods Flashcards

_Lane: `a-level-maths-edexcel` · grade — · 22 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** What defines an identity compared to a standard equation?

**Back:** It is true for all allowed values of the variable, often denoted by $\equiv$.

**Choices:**

- It is true for all allowed values of the variable, often denoted by $\equiv$. ✔
  - _why:_ An identity remains true for every value in the domain where both sides are defined. The symbol $\equiv$ is commonly used to distinguish this from an equation true only for particular values.
- It is true for one allowed value of the variable, often denoted by $\equiv$.
  - _why:_ A result holding for one value describes a particular solution, not an identity. An identity must hold for every allowed value, and $\equiv$ signals that universal relationship.
- It is true for all allowed values of the variable, often denoted by $=$.
  - _why:_ The universal condition is correct, but ordinary $=$ does not specifically indicate an identity. The notation $\equiv$ is used to show that the equality holds for all allowed values.
- It is true for no allowed values of the variable, often denoted by $\equiv$.
  - _why:_ An identity cannot be false throughout its domain. It is an equality satisfied by every allowed value, whereas an equation may have only selected solutions.

## Card 2 — `cloze`

**Front:** In an identity, equating coefficients involves comparing the coefficient of [ ___ ] on both sides.

**Back:** In an identity, equating coefficients involves comparing the coefficient of each power of $x$ on both sides.

**Choices:**

- each power of $x$ ✔
  - _why:_ For an identity, matching coefficients means comparing the coefficients attached to $1$, $x$, $x^2$, and every other corresponding power appearing on the two sides.
- each coefficient of $x$
  - _why:_ Only comparing coefficients of $x$ ignores the constant term and higher powers. The correct method compares the coefficient belonging to every corresponding power of $x$.
- the highest power of $x$
  - _why:_ The highest-degree term alone cannot establish an identity, because lower-degree terms must also match. Coefficients are compared for every power of $x$ present.
- the constant term only
  - _why:_ The constant term is just the coefficient of $x^0$ and is only one part of the comparison. An identity requires matching coefficients for every power of $x$.

## Card 3 — `basic`

**Front:** State the partial fraction form for $\frac{P(x)}{(x-a)(x-b)}$ where $P(x)$ is linear.

**Back:** $$\frac{A}{x-a} + \frac{B}{x-b}$

**Choices:**

- $$\frac{A}{x-a} + \frac{B}{x-b}$ ✔
  - _why:_ Two distinct linear factors in the denominator require one constant-over-factor term for each factor. Since the numerator is linear, these two constants provide the needed general form.
- $$\frac{A}{(x-a)^2} + \frac{B}{(x-b)^2}$
  - _why:_ The denominator contains distinct first-power factors, not repeated squared factors. Squaring the factors introduces the wrong denominator structure; each factor should appear to the first power.
- $$\frac{A}{x-a} + \frac{B}{(x-b)^2}$
  - _why:_ Only the first factor has been treated correctly. The second factor is not repeated, so its partial fraction term must have $x-b$, rather than its square, in the denominator.
- $$\frac{Ax+B}{(x-a)(x-b)}$
  - _why:_ This simply places a general linear numerator over the original denominator, rather than decomposing the fraction. Partial fractions require separate terms associated with the two linear factors.

## Card 4 — `basic`

**Front:** When solving for constants in partial fractions, what value of $x$ should be substituted for a factor $(3x - 1)$?

**Back:** $$x = \frac{1}{3}$

**Choices:**

- $$x = \frac{1}{3}$ ✔
  - _why:_ Set the linear factor equal to zero: $3x-1=0$. Solving gives $3x=1$ and therefore $x=\frac{1}{3}$, which isolates the corresponding partial fraction constant.
- $$x = 3$
  - _why:_ This value comes from using the coefficient of $x$ without solving the factor equation. The factor vanishes when $3x-1=0$, giving $x=\frac{1}{3}$.
- $$x = -\frac{1}{3}$
  - _why:_ The negative sign results from treating the constant term as if the factor were $3x+1$. For $3x-1=0$, the required substitution is $x=\frac{1}{3}$.
- $$x = 1$
  - _why:_ Substituting $x=1$ leaves the factor equal to $2$, so it does not eliminate that denominator term. The correct value makes $3x-1$ equal zero: $x=\frac{1}{3}$.

## Card 5 — `cloze`

**Front:** A rational function is proper if the degree of the [ ___ ] is less than the degree of the denominator.

**Back:** A rational function is proper if the degree of the numerator is less than the degree of the denominator.

**Choices:**

- numerator ✔
  - _why:_ A rational function is proper when the polynomial on top has lower degree than the polynomial underneath. This allows it to be decomposed directly into partial fractions.
- denominator
  - _why:_ Reversing the comparison would describe a fraction whose denominator has lower degree, which is not the definition of proper. Properness requires the numerator degree to be smaller.
- variable
  - _why:_ The variable itself does not have the degree being compared in a rational function. The comparison is between the degrees of the numerator and denominator polynomials.
- constant
  - _why:_ A constant has degree zero, but the definition concerns which polynomial appears above the fraction bar. The numerator must have lower degree than the denominator.

## Card 6 — `cloze`

**Front:** A rational function is proper if the degree of the numerator is less than the degree of the [ ___ ].

**Back:** A rational function is proper if the degree of the numerator is less than the degree of the denominator.

**Choices:**

- denominator ✔
  - _why:_ Properness requires the numerator polynomial to have lower degree than the denominator polynomial. This degree comparison determines whether polynomial division is needed first.
- numerator
  - _why:_ Putting the numerator on the right reverses the required degree comparison. A proper rational function has a numerator degree strictly less than the denominator degree.
- coefficient
  - _why:_ Coefficients affect the values of terms but do not provide the polynomial degree being compared here. Properness is defined using the denominator's degree.
- variable
  - _why:_ The degree belongs to a polynomial, not to the variable alone. The numerator degree must be compared with the degree of the denominator.

## Card 7 — `basic`

**Front:** Which partial fraction terms are required if the denominator contains the repeated factor $(x+2)^2$?

**Back:** $\frac{B}{x+2}$$\frac{C}{(x+2)^2}$

**Choices:**

- $\frac{B}{x+2}$$\frac{C}{(x+2)^2}$ ✔
  - _why:_ A repeated linear factor of multiplicity two requires terms for every power from one through two. Both the first-power and squared-denominator terms are therefore needed.
- $\frac{B}{x+2}$$\frac{C}{(x+2)^3}$
  - _why:_ The cubic denominator is an off-by-one error: the repeated factor has multiplicity two, so powers must run only from one to two. The squared term is the highest required power.
- $\frac{B}{(x+2)^2}$$\frac{C}{(x+2)^3}$
  - _why:_ Starting at the second power omits the essential first-power term and adds an unnecessary cubic term. A squared factor requires all powers from $(x+2)^{-1}$ through $(x+2)^{-2}$.
- $\frac{B}{x+2}$$\frac{C}{x+2}$
  - _why:_ Repeating the same first-power term does not represent the two different powers generated by a repeated factor. The second term must use the squared denominator.

## Card 8 — `basic`

**Front:** A denominator contains $(x+4)^3$. List the required partial fraction terms.

**Back:** $\frac{A}{x+4}$$\frac{B}{(x+4)^2}$$\frac{C}{(x+4)^3}$

**Choices:**

- $\frac{A}{x+4}$$\frac{B}{(x+4)^2}$$\frac{C}{(x+4)^3}$ ✔
  - _why:_ A factor repeated three times contributes one term for each denominator power from one through three. This accounts for all possible repeated-factor components in the partial fraction decomposition.
- $\frac{A}{x+4}$$\frac{B}{(x+4)^2}$$\frac{C}{(x+4)^4}$
  - _why:_ The fourth power is an off-by-one error because the factor has multiplicity three. The required sequence stops at the cubic denominator after including the first and second powers.
- $\frac{A}{(x+4)^2}$$\frac{B}{(x+4)^3}$$\frac{C}{(x+4)^4}$
  - _why:_ This sequence begins too late and extends too far, omitting the first-power term and adding an unnecessary fourth power. Repeated factors require every power from one to the multiplicity.
- $\frac{A}{x+4}$$\frac{B}{x+4}$$\frac{C}{(x+4)^2}$
  - _why:_ Duplicating the first-power term does not supply the distinct powers required by a cubic repetition. The decomposition must include first, second, and third powers exactly once.

## Card 9 — `cloze`

**Front:** If the numerator degree is equal to the denominator degree, the rational function is [ ___ ].

**Back:** If the numerator degree is equal to the denominator degree, the rational function is improper.

**Choices:**

- improper ✔
  - _why:_ When the numerator and denominator have equal degree, the fraction does not have a proper numerator degree below the denominator degree, so it is classified as improper.
- proper
  - _why:_ A proper rational function has numerator degree less than denominator degree. Equal degrees instead make the rational function improper, regardless of the leading coefficients.
- polynomial
  - _why:_ Equal numerator and denominator degrees do not make the whole rational function a polynomial. Polynomial division gives a constant polynomial part plus a proper fractional remainder, so it is improper.
- undefined
  - _why:_ Equal degrees do not by themselves make a rational function undefined; undefined values occur where the denominator is zero. The degree relationship makes the function improper.

## Card 10 — `basic`

**Front:** If an improper fraction has a numerator degree exactly one higher than the denominator, what is the form of the polynomial part?

**Back:** $$Ax + B$ (a linear expression).

**Choices:**

- $$Ax + B$ (a linear expression). ✔
  - _why:_ When the numerator degree is exactly one greater than the denominator degree, polynomial division produces a polynomial of degree one, written generally as $Ax + B$.
- $$A$ (a constant expression).
  - _why:_ A constant polynomial part occurs when the numerator and denominator have equal degree. Being one degree higher requires a linear part, $Ax + B$.
- $$Ax$ (a linear expression).
  - _why:_ The polynomial part is generally linear, but division can produce both an $x$ term and a constant term. Therefore the complete form is $Ax + B$.
- $$Ax^2 + B$ (a quadratic expression).
  - _why:_ The polynomial part cannot be quadratic when the numerator exceeds the denominator by only one degree. The degree difference gives a linear expression, $Ax + B$.

## Card 11 — `cloze`

**Front:** A proof by contradiction begins by assuming the statement to be proved is [ ___ ].

**Back:** A proof by contradiction begins by assuming the statement to be proved is false.

**Choices:**

- false ✔
  - _why:_ A proof by contradiction assumes the negation of the statement being proved. Showing that this assumption leads to an impossibility establishes that the original statement is true.
- true
  - _why:_ Assuming the statement is true is not contradiction proof; it is often part of a direct proof. Contradiction instead begins by assuming the statement is false.
- undecidable
  - _why:_ A contradiction proof does not begin by assuming the statement has no known truth value. It assumes the statement is false and derives an impossibility.
- equivalent
  - _why:_ Assuming an equivalent statement does not create the negation needed for contradiction. The required starting assumption is that the statement to be proved is false.

## Card 12 — `basic`

**Front:** How do you define a rational number?

**Back:** A number that can be written as $\frac{a}{b}$ where $a$ and $b$ are integers and $b \neq 0$.

**Choices:**

- A number that can be written as $\frac{a}{b}$ where $a$ and $b$ are integers and $b \neq 0$. ✔
  - _why:_ This is the definition of a rational number: it is a quotient of two integers with a non-zero denominator, ensuring the fraction is defined.
- A number that can be written as $\frac{a}{b}$ where $a$ and $b$ are natural numbers and $b \neq 0$.
  - _why:_ Restricting both values to natural numbers excludes negative rational numbers, such as $-\frac{1}{2}$. Rational numbers require integers for $a$ and $b$, with $b \neq 0$.
- A number that can be written as $\frac{a}{b}$ where $a$ and $b$ are integers and $b = 0$.
  - _why:_ A zero denominator makes the fraction undefined, so $b$ must not equal zero. Rational numbers are quotients of integers with $b \neq 0$.
- A number that can be written as $\frac{a}{b}$ where $a$ and $b$ are real numbers and $b \neq 0$.
  - _why:_ Allowing arbitrary real values makes every real number expressible as a quotient, so this is not the rational-number definition. Both $a$ and $b$ must be integers.

## Card 13 — `basic`

**Front:** In the contradiction proof that $\sqrt{5}$ is irrational, why must the initial fraction $\frac{a}{b}$ be in lowest terms?

**Back:** To establish that $a$ and $b$ are coprime, allowing a contradiction if a common factor is found.

**Choices:**

- To establish that $a$ and $b$ are coprime, allowing a contradiction if a common factor is found. ✔
  - _why:_ Writing $\frac{a}{b}$ in lowest terms guarantees that $a$ and $b$ have no common factor. The proof then contradicts this when both are shown divisible by 5.
- To establish that $a$ and $b$ are both odd, allowing a contradiction if an even factor is found.
  - _why:_ Lowest terms does not imply that both integers are odd; fractions such as $\frac{2}{3}$ are already reduced. Its purpose is to establish that $a$ and $b$ are coprime.
- To establish that $a$ and $b$ are both prime, allowing a contradiction if a composite factor is found.
  - _why:_ Numerator and denominator need not be prime in lowest terms. Reduction only guarantees that they are coprime, which is contradicted when both acquire a common factor of 5.
- To establish that $a$ and $b$ are positive, allowing a contradiction if a negative factor is found.
  - _why:_ Lowest terms concerns common factors, not signs; either integer may be negative. The needed consequence is that $a$ and $b$ are coprime, so a shared factor creates the contradiction.

## Card 14 — `cloze`

**Front:** If $a^2 = 5b^2$, then $a^2$ is a multiple of 5. Because 5 is [ ___ ], this implies $a$ is also a multiple of 5.

**Back:** If $a^2 = 5b^2$, then $a^2$ is a multiple of 5. Because 5 is prime, this implies $a$ is also a multiple of 5.

**Choices:**

- prime ✔
  - _why:_ Since 5 is prime, Euclid’s lemma says that if 5 divides $a^2$, then 5 divides $a$. Thus $a$ is a multiple of 5.
- odd
  - _why:_ Being odd does not imply that a divisor of $a^2$ must divide $a$; many odd composite numbers disprove that idea. The key property of 5 is that it is prime.
- positive
  - _why:_ Positivity gives no divisibility result: a positive number need not divide a number merely because it divides its square. The implication relies on 5 being prime.
- composite
  - _why:_ Composite numbers do not generally have the required divisibility property; for example, a composite divisor can divide a square without dividing its base. Here 5 is prime.

## Card 15 — `cloze`

**Front:** If $a^2 = 5b^2$, then $a^2$ is a multiple of 5. Because 5 is prime, this implies $a$ is also a [ ___ ].

**Back:** If $a^2 = 5b^2$, then $a^2$ is a multiple of 5. Because 5 is prime, this implies $a$ is also a multiple of 5.

**Choices:**

- multiple of 5 ✔
  - _why:_ Because 5 is prime and divides $a^2$, it must divide $a$. Therefore $a$ can be written as $5k$, so it is a multiple of 5.
- factor of 5
  - _why:_ The divisibility argument shows that 5 divides $a$, meaning $a$ is a multiple of 5. It does not show that $a$ divides 5, which would make $a$ a factor of 5.
- multiple of 25
  - _why:_ From 5 dividing $a^2$, the prime-factor argument establishes only that 5 divides $a$, not that 25 does. The correct conclusion is that $a$ is a multiple of 5.
- divisor of $b^2$
  - _why:_ The equation shows that 5 divides $a^2$, but it gives no conclusion that $a$ divides $b^2$. The prime-divisibility result instead makes $a$ a multiple of 5.

## Card 16 — `basic`

**Front:** Outline why $14m + 21n = 5$ has no integer solutions using contradiction.

**Back:** Assume solutions exist; factor LHS as $7(2m + 3n)$.LHS is a multiple of 7.This implies 5 is a multiple of 7, which is a contradiction.

**Choices:**

- Assume solutions exist; factor LHS as $7(2m + 3n)$.LHS is a multiple of 7.This implies 5 is a multiple of 7, which is a contradiction. ✔
  - _why:_ Factoring gives $14m + 21n = 7(2m + 3n)$, so the left-hand side must be divisible by 7. It cannot equal 5, producing the contradiction.
- Assume solutions exist; factor LHS as $5(14m + 21n)$.LHS is a multiple of 5.This implies 7 is a multiple of 5, which is a contradiction.
  - _why:_ The common factor of the left-hand side is 7, not 5; $14m + 21n = 7(2m + 3n)$. Therefore the correct contradiction is that 5 would have to be a multiple of 7.
- Assume solutions exist; factor LHS as $7(2m + 3n)$.LHS is a multiple of 5.This implies 7 is a multiple of 5, which is a contradiction.
  - _why:_ Although the factorisation is correct, it shows the left-hand side is divisible by 7, not 5. Since the equation sets it equal to 5, the contradiction concerns 5 being a multiple of 7.
- Assume solutions exist; factor LHS as $3(2m + 7n)$.LHS is a multiple of 3.This implies 5 is a multiple of 3, which is a contradiction.
  - _why:_ The proposed factorisation is invalid because $14m + 21n$ has common factor 7, not 3. The valid factorisation is $7(2m + 3n)$, leading to the multiple-of-7 contradiction.

## Card 17 — `basic`

**Front:** Prove that the sum of a rational $r$ and an irrational $s$ is irrational.

**Back:** Assume $r + s = q$ (where $q$ is rational).Then $s = q - r$.Difference of rationals is rational, so $s$ is rational, contradicting the fact $s$ is irrational.

**Choices:**

- Assume $r + s = q$ (where $q$ is rational).Then $s = q - r$.Difference of rationals is rational, so $s$ is rational, contradicting the fact $s$ is irrational. ✔
  - _why:_ Assuming the sum is rational makes $s$ the difference of two rational numbers, so $s$ would be rational. This contradicts the premise that $s$ is irrational, proving the sum is irrational.
- Assume $r + s = q$ (where $q$ is irrational).Then $s = q - r$.Difference of irrational and rational is irrational, so $s$ is irrational, confirming the fact $s$ is irrational.
  - _why:_ Assuming $q$ is irrational presupposes the conclusion rather than its opposite, so no contradiction is obtained. Instead, assume $q$ is rational; then $s=q-r$ would be rational, contradicting the premise.
- Assume $r + s = q$ (where $q$ is rational).Then $s = q + r$.Sum of rationals is rational, so $s$ is rational, contradicting the fact $s$ is irrational.
  - _why:_ Rearranging $r+s=q$ gives $s=q-r$, not $s=q+r$. The correct rearrangement makes $s$ a difference of rationals and hence rational, contradicting its stated irrationality.
- Assume $r + s = q$ (where $q$ is rational).Then $r = q - s$.Difference of rationals is rational, so $r$ is rational, confirming the fact $r$ is rational.
  - _why:_ The argument wrongly treats $s$ as rational when applying closure under subtraction, and confirming that $r$ is rational produces no contradiction. Correctly rearranging for $s$ yields the required contradiction.

## Card 18 — `cloze`

**Front:** A prime number is an integer greater than one with exactly [ ___ ] positive factors.

**Back:** A prime number is an integer greater than one with exactly two positive factors.

**Choices:**

- two ✔
  - _why:_ A prime number has precisely two positive factors: $1$ and the number itself. Having any additional positive factor would make the number composite.
- one
  - _why:_ An integer greater than one cannot have only one positive factor because both $1$ and the integer itself divide it. A prime therefore has exactly two positive factors.
- three
  - _why:_ Three positive factors do not define a prime; for example, a square of a prime has three. A prime has exactly two positive factors, namely $1$ and itself.
- infinitely many
  - _why:_ Having infinitely many positive factors is impossible for a fixed positive integer, since its factors cannot exceed it. A prime has exactly two positive factors.

## Card 19 — `basic`

**Front:** In Euclid's proof of infinite primes, how is the test number $N$ constructed from a finite list of primes $p_1, p_2, ..., p_n$?

**Back:** $$N = (p_1 p_2 ... p_n) + 1$

**Choices:**

- $$N = (p_1 p_2 ... p_n) + 1$ ✔
  - _why:_ Euclid multiplies every prime in the assumed finite list and adds $1$. Consequently, division by any listed prime leaves remainder $1$, forcing an unlisted prime factor.
- $$N = (p_1 p_2 ... p_n) - 1$
  - _why:_ Subtracting $1$ does not guarantee remainder $1$ on division by each listed prime; it gives remainder $-1$. Euclid’s standard test number is the product plus $1$.
- $$N = (p_1 + p_2 + ... + p_n) + 1$
  - _why:_ Adding the primes does not ensure that division by every listed prime leaves remainder $1$. The construction must multiply all listed primes and then add $1$.
- $$N = p_1 p_2 ... p_n$
  - _why:_ The product alone is divisible by every prime in the list and therefore creates no new prime factor. Adding $1$ makes it indivisible by each listed prime.

## Card 20 — `basic`

**Front:** Why does $N = (p_1 p_2 ... p_n) + 1$ lead to a contradiction in the proof of infinite primes?

**Back:** $N$ has a prime factor (as $N > 1$).Dividing $N$ by any prime in the finite list leaves remainder 1.Therefore, a prime factor exists outside the list.

**Choices:**

- $N$ has a prime factor (as $N > 1$).Dividing $N$ by any prime in the finite list leaves remainder 1.Therefore, a prime factor exists outside the list. ✔
  - _why:_ Every integer greater than $1$ has a prime factor, but no listed prime divides $N$ because each leaves remainder $1$. Thus at least one prime lies outside the supposedly complete list.
- $N$ has a prime factor (as $N > 1$).Dividing $N$ by any prime in the finite list leaves remainder 0.Therefore, every prime factor lies inside the list.
  - _why:_ The added $1$ means listed primes leave remainder $1$, not $0$, so none divides $N$. This forces a prime factor outside the finite list rather than keeping every factor within it.
- $N$ is itself prime (as $N > 1$).Dividing $N$ by any prime in the finite list leaves remainder 1.Therefore, $N$ is the only prime outside the list.
  - _why:_ Being greater than $1$ guarantees a prime factor, not that $N$ itself is prime; $N$ may be composite. Its prime factors must nevertheless be outside the assumed finite list.
- $N$ has a prime factor (as $N > 1$).Dividing $N$ by any prime in the finite list leaves remainder 1.Therefore, no prime factor exists outside the list.
  - _why:_ A remainder of $1$ shows that no listed prime divides $N$, so the conclusion is reversed. Since $N>1$ has a prime factor, that factor must be outside the list.

## Card 21 — `cloze`

**Front:** If the degree of the numerator is [ ___ ] the degree of the denominator, the fraction must be split into a polynomial part and partial fractions.

**Back:** If the degree of the numerator is greater than or equal to the degree of the denominator, the fraction must be split into a polynomial part and partial fractions.

**Choices:**

- greater than or equal to ✔
  - _why:_ A rational expression is improper when the numerator’s degree is at least the denominator’s degree. Polynomial division is then required before decomposing the proper remainder into partial fractions.
- less than
  - _why:_ A lower numerator degree makes the rational expression proper, so polynomial division is unnecessary. Splitting is required when the numerator’s degree is greater than or equal to the denominator’s.
- strictly greater than
  - _why:_ This excludes the equal-degree case, where polynomial division is also necessary because the fraction is improper. The correct condition is greater than or equal to.
- equal to
  - _why:_ Equal degrees do require polynomial division, but so does any case where the numerator has higher degree. The full condition is greater than or equal to.

## Card 22 — `basic`

**Front:** What are the four general steps of a contradiction proof?

**Back:** Assume the opposite.Apply algebra/logical facts.Reach a contradiction (impossibility).State the conclusion.

**Choices:**

- Assume the opposite.Apply algebra/logical facts.Reach a contradiction (impossibility).State the conclusion. ✔
  - _why:_ A contradiction proof negates the desired conclusion, reasons validly from that assumption, and derives an impossibility. The negated assumption must therefore be false, establishing the original conclusion.
- Assume the statement.Apply algebra/logical facts.Reach a confirmation (possibility).State the conclusion.
  - _why:_ Beginning by assuming the desired claim does not test whether its negation is impossible and risks circular reasoning. A contradiction proof must assume the opposite before deriving an impossibility.
- Assume the opposite.Test several numerical examples.Observe a pattern (regularity).State the conclusion.
  - _why:_ Checking examples can support a conjecture but cannot establish a universal statement by contradiction. The method requires assuming the opposite, applying valid reasoning, and reaching an impossibility.
- Assume the opposite.Apply algebra/logical facts.Reach a contradiction (impossibility).State the opposite.
  - _why:_ A contradiction shows that the assumed opposite is false, so the original statement must be concluded. Accepting the opposite reverses the final logical implication.
