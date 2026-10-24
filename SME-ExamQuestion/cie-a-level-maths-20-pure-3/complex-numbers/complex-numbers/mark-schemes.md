# Mark Schemes — Complex Numbers
**Complex Numbers** · Cambridge (CIE) A-LEVEL maths (9709)


## Exam Questions (36 questions)


### Q1
(i)

The coefficients of the cubic are real, so its non-real roots occur in conjugate pairs, and the third root is the conjugate of $z_{2}$

$z_{3} = 3 + i$

**[B1]**

(ii)

Deal with the two complex roots first, since their product gives a quadratic with real coefficients

`(z - z_{2})(z - z_{3}) = \left(z - (3 - i)\right)\left(z - (3 + i)\right)`

$= z^{2} - ( 3 + i ) z - ( 3 - i ) z + ( 3 - i ) ( 3 + i )$

**[M1]**

The imaginary parts of the middle terms cancel, and the last product is a complex number times its conjugate

$= z^{2} - 6 z + 9 - i^{2} = z^{2} - 6 z + 10$

**[A1]**

Now multiply by the factor coming from the real root $z_{1} = 3$

$f ( z ) = ( z - 3 ) ( z^{2} - 6 z + 10 ) = z ( z^{2} - 6 z + 10 ) - 3 ( z^{2} - 6 z + 10 )$

$= z^{3} - 6 z^{2} + 10 z - 3 z^{2} + 18 z - 30$

**[M1]**

Collect like terms and compare with $z^{3} - 9 z^{2} + c z + d$

$f ( z ) = z^{3} - 9 z^{2} + 28 z - 30$

$c = 28 ,  d = - 30$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct third root $z_{3} = 3 + i$ stated. This mark is independent, and no working is required.
> 
> **M1**: A complete valid method for the quadratic factor with zeros $3 - i$ and $3 + i$. Accept multiplying the two linear factors, or using the sum and product of that pair of roots.
> 
> **A1**: Correct quadratic factor $z^{2} - 6 z + 10$, with $i^{2} = - 1$ used so that the coefficients are real.
> 
> **M1**: Correct method for multiplying the quadratic factor by the linear factor $( z - 3 )$, with all six terms attempted.
> 
> **A1**: Both values correct, $c = 28$ and $d = - 30$. Accept the answer given as the expanded cubic $z^{3} - 9 z^{2} + 28 z - 30$ provided $c$ and $d$ are identified.

### Q2
Square the complex number by writing it as a product of two brackets and expanding

$( 6 - i )^{2} = ( 6 - i ) ( 6 - i ) = 36 - 6 i - 6 i + i^{2}$

Replace $i^{2}$ by $- 1$ and collect

$( 6 - i )^{2} = 36 - 12 i - 1 = 35 - 12 i$

**[M1]**

Now substitute $z = 6 - i$ into $f ( z )$, using the square just found

$f ( 6 - i ) = ( 35 - 12 i ) - 12 ( 6 - i ) + 37 = ( 35 - 12 i ) - 72 + 12 i + 37$

Group the real terms and the imaginary terms to see that both vanish

$= ( 35 - 72 + 37 ) + ( - 12 + 12 ) i = 0 + 0 i$

**Final answer:** $f ( 6 - i ) = 0$**, so **$z = 6 - i$** is a solution**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct expansion of $( 6 - i )^{2}$ with $i^{2} = - 1$ used, reaching $35 - 12 i$.
> 
> **A1**: Correct substitution into $f ( z )$ and a complete verification that the result is zero, with a conclusion stated. Both the real and the imaginary parts must be shown to cancel; stopping at $35 - 72 + 37$ without dealing with the imaginary terms does not complete the argument.
The conjugate reverses the sign of the imaginary part, so first write down the number being tested

$( 6 - i )^{\ast} = 6 + i$

Square it, exactly as in part (a)

$( 6 + i )^{2} = ( 6 + i ) ( 6 + i ) = 36 + 6 i + 6 i + i^{2} = 35 + 12 i$

**[M1]**

Substitute $z = 6 + i$ into $f ( z )$

$f ( 6 + i ) = ( 35 + 12 i ) - 12 ( 6 + i ) + 37 = ( 35 + 12 i ) - 72 - 12 i + 37$

Group the real terms and the imaginary terms

$= ( 35 - 72 + 37 ) + ( 12 - 12 ) i = 0 + 0 i$

**Final answer:** $f ( 6 + i ) = 0$**, so **$( 6 - i )^{\ast} = 6 + i$** is another solution**

**[A1]**

> **[mark-scheme]**
> **M1**: Correct conjugate $( 6 - i )^{\ast} = 6 + i$ stated, and $( 6 + i )^{2} = 35 + 12 i$ obtained with $i^{2} = - 1$ used.
> 
> **A1**: Correct substitution into $f ( z )$ and a complete verification that the result is zero, with a conclusion stated.

### Q3
(i)

Square $β$ by expanding the brackets and using $i^{2} = - 1$

$β^{2} = ( 1 + 2 i ) ( 1 + 2 i ) = 1 + 2 i + 2 i + 4 i^{2} = 1 + 4 i - 4$

$β^{2} = - 3 + 4 i$

**[B1]**

To find the cube, multiply the square just found by $β$ again

$β^{3} = ( - 3 + 4 i ) ( 1 + 2 i ) = - 3 - 6 i + 4 i + 8 i^{2} = - 3 - 2 i - 8$

$β^{3} = - 11 - 2 i$

**[B1]**

(ii)

Substitute $z = β$ into the cubic, using the two powers from part (i)

$β^{3} + β^{2} - β + 15 = ( - 11 - 2 i ) + ( - 3 + 4 i ) - ( 1 + 2 i ) + 15$

Group the real terms and the imaginary terms

$= ( - 11 - 3 - 1 + 15 ) + ( - 2 + 4 - 2 ) i = 0 + 0 i$

**Final answer:** **The result is zero, so **$β = 1 + 2 i$** is a root of the equation**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct value $β^{2} = - 3 + 4 i$, with $i^{2} = - 1$ used.
> 
> **B1**: Correct value $β^{3} = - 11 - 2 i$. Any valid route earns this, including multiplying $β$ by $β^{2}$ or expanding $( 1 + 2 i )^{3}$ directly.
> 
> **B1**: Correct substitution into the cubic showing that both the real part and the imaginary part are zero, with a conclusion stated. Because the result is given, the substitution must be visible; a bare assertion that it works scores nothing.
(i)

The cubic has real coefficients, so its non-real roots occur in conjugate pairs, and $γ$ is the conjugate of $β$

$γ = 1 - 2 i$

**[B1]**

(ii)

Write each factor with its root kept inside a bracket, then expand

`(z - \beta)(z - \gamma) = \left(z - (1 + 2i)\right)\left(z - (1 - 2i)\right)`

$= z^{2} - ( 1 - 2 i ) z - ( 1 + 2 i ) z + ( 1 + 2 i ) ( 1 - 2 i )$

The imaginary parts of the two middle terms cancel, and the final product is a complex number times its conjugate

$= z^{2} - 2 z + 1 - 4 i^{2}$

Replace $i^{2}$ by $- 1$

$( z - β ) ( z - γ ) = z^{2} - 2 z + 5$

**[M1]**

(iii)

Since $β$, $γ$ and $δ$ are the three roots, the cubic factorises as the product of the quadratic just found and the remaining linear factor

$z^{3} + z^{2} - z + 15 = ( z^{2} - 2 z + 5 ) ( z - δ )$

Compare the constant terms

$5 \times ( - δ ) = 15$

**[M1]**

Solve for $δ$, then put it back into the bracket to give the full factorisation

$δ = - 3$

$z^{3} + z^{2} - z + 15 = ( z^{2} - 2 z + 5 ) ( z + 3 )$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct conjugate root $γ = 1 - 2 i$ stated. This mark is independent, and no working is required.
> 
> **M1**: Correct expansion of `\left(z - (1 + 2i)\right)\left(z - (1 - 2i)\right)` with $i^{2} = - 1$ used, reaching the printed quadratic. Because the result is given, the expansion must be shown.
> 
> **M1**: A complete valid method for the remaining linear factor, reaching an equation in $δ$. Accept comparing coefficients in $( z^{2} - 2 z + 5 ) ( z - δ )$, or dividing $z^{3} + z^{2} - z + 15$ by $z^{2} - 2 z + 5$, or using the product of the three roots.
> 
> **A1**: Both answers correct, $δ = - 3$ and the full factorisation $( z^{2} - 2 z + 5 ) ( z + 3 )$. Note the sign: the factor is $z + 3$, so the root is $- 3$.

### Q4
The conjugate of a complex number keeps the real part and reverses the sign of the imaginary part

$z_{1}^{\ast} = 3 + 2 i$

$z_{2}^{\ast} = 4 - 3 i$

**[B1]**

> **[mark-scheme]**
> **B1**: Both conjugates correct. Only the sign of the imaginary part changes, so the real parts stay as $3$ and $4$.
Using $z_{2}^{\ast} = 4 - 3 i$ from part (a), expand the first product

$z_{1} \times z_{2}^{\ast} = ( 3 - 2 i ) ( 4 - 3 i ) = 12 - 9 i - 8 i + 6 i^{2}$

Replace $i^{2}$ by $- 1$ and collect the terms

$= 12 - 9 i - 8 i - 6$

$z_{1} \times z_{2}^{\ast} = 6 - 17 i$

**[M1]**

Now expand the second product, which pairs $z_{2}$ with its own conjugate

$z_{2} \times z_{2}^{\ast} = ( 4 + 3 i ) ( 4 - 3 i ) = 16 - 12 i + 12 i - 9 i^{2}$

The two imaginary terms cancel, and $- 9 i^{2}$ becomes $+ 9$

$= 16 + 9$

$z_{2} \times z_{2}^{\ast} = 25$

**[A1]**

> **[exam-tip]**
> Multiplying any complex number by its own conjugate always gives a real answer, because the imaginary terms cancel in pairs.

> **[mark-scheme]**
> **M1**: Correct expansion of $( 3 - 2 i ) ( 4 - 3 i )$ with $i^{2} = - 1$ used, leading to $6 - 17 i$.
> 
> **A1**: Correct expansion of $( 4 + 3 i ) ( 4 - 3 i )$ leading to $25$. Both printed results are given in the question, so the expansions must be shown in full; unsupported answers score nothing.
Separating the right-hand side into two fractions shows what has actually been multiplied in

$\frac{z_{1}\timesz_{2}^{\ast}}{z_{2}\timesz_{2}^{\ast}} = \frac{z_{1}}{z_{2}} \times \frac{z_{2}^{\ast}}{z_{2}^{\ast}}$

Since $z_{2}^{\ast}$ is not zero, the second fraction is equal to $1$

**Final answer:** **Multiplying the numerator and the denominator by the same non-zero number does not change the value of the fraction, since **$\frac{z_{2}^{\ast}}{z_{2}^{\ast}} = 1$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct explanation identifying that numerator and denominator have both been multiplied by $z_{2}^{\ast}$, and that this leaves the value unchanged because $z_{2}^{\ast} / z_{2}^{\ast} = 1$. Accept any equivalent wording, such as multiplying by $1$ written in a different form, or referring to equivalent fractions.
Part (c) allows the quotient to be rewritten, and part (b) supplies both of the products needed

$\frac{z_{1}}{z_{2}} = \frac{z_{1}\timesz_{2}^{\ast}}{z_{2}\timesz_{2}^{\ast}} = \frac{6-17i}{25}$

**[M1]**

The denominator is now real, so divide each part of the numerator by it to reach the required form

$\frac{z_{1}}{z_{2}} = \frac{6}{25} - \frac{17}{25} i$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of parts (b) and (c) to obtain $\frac{6-17i}{25}$, or the equivalent with the numerator and denominator written out in full.
> 
> **A1**: Correct answer $\frac{6}{25} - \frac{17}{25} i$. Accept any exact equivalent, such as $0 . 24 - 0 . 68 i$ or the parts stated separately as $a = \frac{6}{25}$ and $b = - \frac{17}{25}$. The answer must be split into real and imaginary parts, so $\frac{6-17i}{25}$ alone does not score this mark.

### Q5
Rearrange to make $z^{2}$ the subject, then take the square root of both sides, remembering both signs

$z^{2} = - 16$* so *$z = \pm \sqrt{-16}$

Split the surd so that the negative sign is isolated in a factor of $\sqrt{-1}$

$z = \pm \sqrt{16} \sqrt{-1} = \pm 4 i$

**Final answer:** $z = 4 i$** or **$z = - 4 i$

**[B1]**

> **[mark-scheme]**
> **B1**: Both solutions correct. Accept the answer written as $z = \pm 4 i$. Only one of the two values does not score, since the question asks for both solutions.
(i)

Use the formula for the solutions of a quadratic equation, $z = \frac{-b\pm\sqrt{b^{2}-4ac}}{2a}$, with $a = 1$, $b = - 4$ and $c = 13$

$z = \frac{-(-4)\pm\sqrt{(-4)^{2}-4(1)(13)}}{2(1)} = \frac{4\pm\sqrt{-36}}{2}$

**[M1]**

The quantity under the root is negative, so split off $\sqrt{-1}$ as in part (a)

$\sqrt{-36} = \sqrt{36} \sqrt{-1} = 6 i$

**[A1]**

Substitute this back and divide each term by $2$ to reach the required form

$z = \frac{4\pm6i}{2}$

**Final answer:** $z = 2 + 3 i$** or **$z = 2 - 3 i$

**[A1]**

(ii)

Complete the square on the first two terms, subtracting the square of the halved coefficient of $z$

$z^{2} - 4 z + 13 = ( z - 2 )^{2} - ( - 2 )^{2} + 13 = 0$

Simplify the constant terms

$( z - 2 )^{2} - 4 + 13 = 0$* so *$( z - 2 )^{2} + 9 = 0$

**[M1]**

Isolate the squared bracket and take the square root of both sides, again with both signs

$( z - 2 )^{2} = - 9$* so *$z - 2 = \pm \sqrt{9} \sqrt{-1} = \pm 3 i$

Add $2$ to both sides

**Final answer:** $z = 2 + 3 i$** or **$z = 2 - 3 i$

**[A1]**

Comparing the two answers confirms what the question asked for

**Final answer:** **Both methods give the same pair of solutions**

> **[mark-scheme]**
> **M1**: Correct substitution of $a = 1$, $b = - 4$ and $c = 13$ into the quadratic formula. Allow a slip in one term provided the structure of the formula is right.
> 
> **A1**: Correct handling of the negative square root, giving $\sqrt{-36} = 6 i$ or equivalent.
> 
> **A1**: Both solutions $2 + 3 i$ and $2 - 3 i$ obtained from the formula, in the form $a + b i$. Accept $z = 2 \pm 3 i$.
> 
> **M1**: Correct completed square form for the second method, reaching $( z - 2 )^{2} + 9 = 0$ or equivalent.
> 
> **A1**: Both solutions obtained again from the completed square form, with a statement that the two methods agree. The comparison itself carries no separate mark, but the second method must be worked through independently rather than the answer simply being copied from part (i).

### Q6
To find $z_{2}$ on its own, subtract $z_{1}$ from both sides of the given sum

$z_{2} = ( 1 - 3 i ) - z_{1} = ( 1 - 3 i ) - ( - 7 + 6 i )$

Collect the real parts and the imaginary parts, watching the double negative

$z_{2} = ( 1 + 7 ) + ( - 3 - 6 ) i = 8 - 9 i$

**[M1]**

Comparing this with $z_{2} = a + b i$ gives the two real numbers directly

$a = 8 ,  b = - 9$

**[A1]**

> **[mark-scheme]**
> **M1**: A correct method for $z_{2}$, by any valid route. Either subtract $z_{1}$ from $1 - 3 i$, or form $( a - 7 ) + ( b + 6 ) i = 1 - 3 i$ and equate real and imaginary parts to give $a - 7 = 1$ and $b + 6 = - 3$.
> 
> **A1**: Both $a = 8$ and $b = - 9$ correct. Accept the answer written as $z_{2} = 8 - 9 i$ provided the values of $a$ and $b$ are clear. The value of $b$ must be the real number $- 9$, not $- 9 i$.

### Q7
Write the negative as a factor of $- 1$, then square each factor separately

$( - w )^{2} = ( - 1 \times w )^{2} = ( - 1 )^{2} \times w^{2} = 1 \times w^{2}$

$( - w )^{2} = w^{2}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct and complete argument. Accept the index-law route shown, or expanding both sides in terms of $a$ and $b$ to obtain $a^{2} + 2 a b i + b^{2} i^{2}$ from each and comparing them. A bare restatement of the result does not score.
(i)

By the definition given, it is enough to square $2 - 3 i$ and check the result against $z$

$( 2 - 3 i )^{2} = ( 2 - 3 i ) ( 2 - 3 i ) = 4 - 6 i - 6 i + 9 i^{2}$

**[M1]**

Replace $i^{2}$ by $- 1$ and collect the terms

$= 4 - 12 i - 9 = - 5 - 12 i$

**Final answer:** $( 2 - 3 i )^{2} = z$**, so **$2 - 3 i$** is a square root of **$z$

**[A1]**

(ii)

Part (a) shows that negating a complex number leaves its square unchanged, so the negative of a square root is also a square root

`\left(-(2 - 3i)\right)^{2} = (2 - 3i)^{2} = z`

**Final answer:** **The other square root of z is **$- 2 + 3 i$

**[B1]**

> **[mark-scheme]**
> **M1**: Correct expansion of $( 2 - 3 i )^{2}$ giving all four terms, with $i^{2} = - 1$ used.
> 
> **A1**: Correct simplification to $- 5 - 12 i$ together with a statement that this equals $z$, so $2 - 3 i$ is a square root. Because the result is given, the full expansion must be shown.
> 
> **B1**: Other square root given as $- 2 + 3 i$. Accept $- ( 2 - 3 i )$, and accept the answer following through from an incorrect first root.

### Q8
(i)

The coefficients of the equation are real, so any non-real roots occur in conjugate pairs, and the second root is the conjugate of the first

$z = 5 + 3 i$

**[B1]**

(ii)

A quadratic with these two roots can be written as the product of the corresponding linear factors, so keep each root inside a bracket

`\left(z - (5 - 3i)\right)\left(z - (5 + 3i)\right) = 0`

**[M1]**

Expand the brackets, keeping the two complex terms together for now

$z^{2} - ( 5 + 3 i ) z - ( 5 - 3 i ) z + ( 5 - 3 i ) ( 5 + 3 i ) = 0$

The two middle terms combine, and the final product is a complex number multiplied by its conjugate

$z^{2} - 10 z + ( 25 - 9 i^{2} ) = 0$

Replace $i^{2}$ by $- 1$, so the constant term becomes real

$z^{2} - 10 z + 34 = 0$

Comparing with $z^{2} + b z + c = 0$ gives the two constants

$b = - 10 ,  c = 34$

**[A1 A1]**

> **[mark-scheme]**
> **B1**: Other root stated as $5 + 3 i$. This mark is independent, and no working is required.
> 
> **M1**: A complete valid method for forming the quadratic. Either multiply the linear factors `\left(z - (5 - 3i)\right)\left(z - (5 + 3i)\right)`, or use the sum and product of the roots to write $z^{2} - ( \text{sum} ) z + ( \text{product} ) = 0$. Either method earns this mark.
> 
> **A1**: Correct value $b = - 10$. A sign error here is the common slip, since the coefficient of $z$ is the negative of the sum of the roots.
> 
> **A1**: Correct value $c = 34$. This requires $i^{2} = - 1$ to have been used, so that the product of the two roots is real.

### Q9
(i)

To add two complex numbers, collect the real parts and the imaginary parts separately

$z_{1} + z_{2} = ( 3 + i ) + ( - 5 + 2 i ) = ( 3 - 5 ) + ( 1 + 2 ) i$

$z_{1} + z_{2} = - 2 + 3 i$

Subtract in the same way, taking care with the double negative in the real part

$z_{1} - z_{2} = ( 3 + i ) - ( - 5 + 2 i ) = ( 3 + 5 ) + ( 1 - 2 ) i$

$z_{1} - z_{2} = 8 - i$

**[B1]**

(ii)

For a complex number written as $z = a + b i$, the real part is $a$ and the imaginary part is $b$, so read each one off the answers above

$\text{Re} ( z_{1} + z_{2} ) = - 2$

$\text{Im} ( z_{1} - z_{2} ) = - 1$

**[B1]**

> **[mark-scheme]**
> **B1**: Both $z_{1} + z_{2} = - 2 + 3 i$ and $z_{1} - z_{2} = 8 - i$ correct. Award this mark only when both are right, and accept the answers written in either order.
> 
> **B1**: Both $\text{Re} ( z_{1} + z_{2} ) = - 2$ and $\text{Im} ( z_{1} - z_{2} ) = - 1$ correct, following through from part (i). The imaginary part must be given as a real number, so $- i$ does not score.
Expand the two brackets in the usual way, treating $i$ as an algebraic symbol for the moment

$z_{1} \times z_{2} = ( 3 + i ) ( - 5 + 2 i ) = - 15 + 6 i - 5 i + 2 i^{2}$

**[M1]**

Replace $i^{2}$ by $- 1$, which is what turns the last term into a real number

$= - 15 + 6 i - 5 i + 2 ( - 1 ) = - 15 + 6 i - 5 i - 2$

Collect the real terms and the imaginary terms

$= ( - 15 - 2 ) + ( 6 - 5 ) i$

$z_{1} \times z_{2} = - 17 + i$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct expansion of $( 3 + i ) ( - 5 + 2 i )$ giving all four terms, with $i^{2} = - 1$ used at least once. Small arithmetic slips in a single term may still earn this mark provided the expansion is complete.
> 
> **A1**: Correct collection of the real and imaginary parts to reach the printed result $- 17 + i$. Because the answer is given in the question, the expansion and the use of $i^{2} = - 1$ must both be visible, and a bare statement of the answer scores nothing.

### Q10
The coefficients of $f ( z )$ are real, so the non-real roots occur in conjugate pairs

$( 3 - 4 i )^{\ast} = 3 + 4 i \text{is also a root}$

**[B1]**

These two roots give a quadratic factor with real coefficients

`\left(z - (3 - 4i)\right)\left(z - (3 + 4i)\right) = z^{2} - 6z + (9 + 16) = z^{2} - 6z + 25`

**[M1]**

A quartic has four roots, so the remaining factor is another quadratic, which can be written with unknown coefficients

$f ( z ) = ( z^{2} - 6 z + 25 ) ( z^{2} + b z + c )$

Compare the coefficients of $z^{3}$

$b - 6 = - 2$

$b = 4$

Compare the constant terms

$25 c = 125$

$c = 5$

**[M1]**

Check against the coefficient of $z^{2}$, which must come out as the given $6$

$c - 6 b + 25 = 5 - 24 + 25 = 6$

**Final answer:** $z^{2} + 4 z + 5$** is a factor of **$f ( z )$

**[A1]**

> **[mark-scheme]**
> **B1**: Conjugate root identified as $3 + 4 i$. This mark is independent, and no working is required.
> 
> **M1**: A complete valid method for the quadratic factor with zeros $3 - 4 i$ and $3 + 4 i$, reaching $z^{2} - 6 z + 25$.
> 
> **M1**: A complete method for the second quadratic factor. Accept comparing coefficients in $( z^{2} - 6 z + 25 ) ( z^{2} + b z + c )$, or dividing $f ( z )$ by $z^{2} - 6 z + 25$ by algebraic long division.
> 
> **A1**: The printed factor $z^{2} + 4 z + 5$ obtained correctly, with the consistency of at least one further coefficient shown. Because the result is given, the working must be visible throughout.
The coefficient of $z$ was the one term not yet used, so compare it now using the two factors from part (a)

$p = 25 b - 6 c = 25 ( 4 ) - 6 ( 5 ) = 100 - 30$

$p = 70$

**[B1]**

The remaining two roots are the solutions of the second quadratic factor, which does not factorise, so complete the square

$z^{2} + 4 z + 5 = 0$* so *$( z + 2 )^{2} - 4 + 5 = 0$

$( z + 2 )^{2} = - 1$* so *$z + 2 = \pm \sqrt{-1} = \pm i$

**[M1]**

Subtract $2$ from both sides to get the remaining pair of roots, then collect all four

$z = - 2 + i$* or *$z = - 2 - i$

$z = 3 - 4 i ,  3 + 4 i ,  - 2 + i ,  - 2 - i$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct value $p = 70$. Accept it obtained by comparing the coefficients of $z$, or by substituting a known root into $f ( z )$.
> 
> **M1**: A complete valid method for solving $z^{2} + 4 z + 5 = 0$. Accept completing the square or the quadratic formula.
> 
> **A1**: All four roots given, $3 - 4 i$, $3 + 4 i$, $- 2 + i$ and $- 2 - i$. All four are required, since the question asks for the equation to be solved completely.

### Q11
(i)

Add the two fractions over their common denominator, which keeps everything in terms of $z$ and $z^{\ast}$

$\frac{1}{z} + \frac{1}{z^{\ast}} = \frac{z^{\ast}+z}{zz^{\ast}}$

**[M1]**

The numerator is the sum of a complex number and its conjugate, so the imaginary parts cancel

$z + z^{\ast} = ( x + i y ) + ( x - i y ) = 2 x$

The denominator is a complex number times its conjugate, which is always real

$z z^{\ast} = ( x + i y ) ( x - i y ) = x^{2} - i^{2} y^{2} = x^{2} + y^{2}$

Putting the two together gives a fraction with a real numerator and a real denominator

**Final answer:** $\frac{1}{z} + \frac{1}{z^{\ast}} = \frac{2x}{x^{2}+y^{2}}$**, so **`\text{Re}\left(\dfrac{1}{z} + \dfrac{1}{z^{*}}\right) = \dfrac{2x}{x^{2} + y^{2}}`

**[A1]**

(ii)

Since $x$ and $y$ are both real, the expression found above is entirely real and has no imaginary part

`\text{Im}\left(\dfrac{1}{z} + \dfrac{1}{z^{*}}\right) = 0`

**[B1]**

> **[mark-scheme]**
> **M1**: The two fractions combined over a common denominator, giving $\frac{z+z^{\ast}}{zz^{\ast}}$ or the equivalent in terms of $x$ and $y$. Accept instead rationalising $\frac{1}{z}$ and $\frac{1}{z^{\ast}}$ separately by multiplying each by the conjugate of its denominator, and then adding.
> 
> **A1**: Both $z + z^{\ast} = 2 x$ and $z z^{\ast} = x^{2} + y^{2}$ obtained, with $i^{2} = - 1$ used, reaching the printed result. Because the result is given, the working must be visible.
> 
> **B1**: A correct statement that the expression is real, because $x$ and $y$ are real, so the imaginary part is zero. Accept any equivalent reasoning. Simply restating the printed result does not score.

### Q12
The unknown is in the denominator, so rearrange to make $z_{2}$ the subject

$z_{2} = \frac{2z_{1}}{-1-7i} = \frac{2(3-4i)}{-1-7i} = \frac{6-8i}{-1-7i}$

Multiply the numerator and the denominator by the conjugate of the denominator so the denominator becomes real

$z_{2} = \frac{6-8i}{-1-7i} \times \frac{-1+7i}{-1+7i}$

**[M1]**

Expand the numerator and the denominator separately, using $i^{2} = - 1$

$z_{2} = \frac{-6+42i+8i-56i^{2}}{1-49i^{2}} = \frac{-6+50i+56}{1+49}$

$z_{2} = \frac{50+50i}{50}$

**[A1]**

Divide each part of the numerator by the real denominator, then compare with $z_{2} = a + b i$

$z_{2} = 1 + i$

$a = 1 ,  b = 1$

**[A1]**

> **[mark-scheme]**
> **M1**: The equation rearranged to make $z_{2}$ the subject, with a clear intention to multiply the numerator and the denominator by the conjugate of the denominator.
> 
> **A1**: Correct numerator $50 + 50 i$ or correct denominator $50$, with $i^{2} = - 1$ used.
> 
> **A1**: Both values correct, $a = 1$ and $b = 1$. Accept the answer given as $z_{2} = 1 + i$ provided $a$ and $b$ are identified. A correct answer with no working scores nothing, since the syllabus requires full details of the working for division. The alternative method of substituting $z_{2} = a + b i$ and equating real and imaginary parts earns the marks equally.

### Q13
Since $3$ is a root, $( z - 3 )$ is a factor, and the other factor must be a quadratic whose roots are $β$ and $γ$

$z^{3} + ( b - 3 ) z^{2} + ( 7 - 3 b ) z - 21 = ( z - 3 ) ( z^{2} + p z + q )$

Compare the constant terms

$- 3 q = - 21$

$q = 7$

Compare the coefficients of $z^{2}$

$p - 3 = b - 3$

$p = b$

**[M1]**

So the two non-real roots are the roots of the quadratic factor

$z^{2} + b z + 7 = 0$

**[A1]**

This quadratic has distinct non-real roots exactly when its discriminant is negative

$b^{2} - 4 ( 1 ) ( 7 ) < 0$

**[M1]**

Simplify and isolate $b^{2}$

$b^{2} - 28 < 0$* so *$b^{2} < 28$

Take the square root of both sides, remembering that $b$ may be negative, and simplify the surd using $\sqrt{28} = \sqrt{4\times7} = 2 \sqrt{7}$

$- 2 \sqrt{7} < b < 2 \sqrt{7}$

**[A1]**

> **[mark-scheme]**
> **M1**: A complete valid method for the quadratic factor, using the fact that $( z - 3 )$ is a factor. Accept comparing coefficients, algebraic long division, or using the sum and product of the roots.
> 
> **A1**: Correct quadratic factor $z^{2} + b z + 7$, or equivalently the pair of results $p = b$ and $q = 7$.
> 
> **M1**: Discriminant of the quadratic factor used with the correct inequality, $b^{2} - 4 ( 1 ) ( 7 ) < 0$. Using `\leqslant` or $= 0$ does not earn this mark, since the roots must be non-real.
> 
> **A1**: Correct range $- 2 \sqrt{7} < b < 2 \sqrt{7}$. Accept any equivalent form, including $- \sqrt{28} < b < \sqrt{28}$ or `|b| < 2\sqrt{7}`. Both bounds are needed and the inequalities must be strict.

### Q14
Complete the square on the first two terms, halving the coefficient of $z$ and subtracting the square of what was added

$z^{2} - 6 i z - 14 = ( z - 3 i )^{2} - 9 i^{2} - 14$

**[M1]**

Since $- 9 i^{2} = + 9$, the constant terms combine

$= ( z - 3 i )^{2} + 9 - 14 = ( z - 3 i )^{2} - 5$

**[A1]**

Set this equal to zero and isolate the squared bracket

$( z - 3 i )^{2} - 5 = 0$* so *$( z - 3 i )^{2} = 5$

Take the square root of both sides, keeping both signs

$z - 3 i = \pm \sqrt{5}$

**[M1]**

Add $3 i$ to both sides

**Final answer:** $z = \sqrt{5} + 3 i$** or **$z = - \sqrt{5} + 3 i$

**[A1]**

> **[mark-scheme]**
> **M1**: Completing the square attempted, reaching $( z - 3 i )^{2}$ together with a correction term.
> 
> **A1**: Correct completed square form $( z - 3 i )^{2} - 5$, with $i^{2} = - 1$ used. Accept the equivalent obtained from the quadratic formula.
> 
> **M1**: The squared bracket isolated and the square root taken with both signs.
> 
> **A1**: Both solutions correct and exact, $\sqrt{5} + 3 i$ and $- \sqrt{5} + 3 i$. Accept $z = 3 i \pm \sqrt{5}$. The surd must be left exact, so decimals do not score. Note that the coefficient $- 6 i$ is not real, so the two solutions are not a conjugate pair; an answer of the form $\sqrt{5} \pm 3 i$ does not score.

### Q15
The coefficients of the equation are real, so the non-real roots occur in conjugate pairs, even though $q$ is not yet known

$( 3 + q i )^{\ast} = 3 - q i$

**[B1]**

Both roots are now known in terms of $q$, so the quadratic is the product of the two linear factors

`z^{2} - 12pz + 58 = \left(z - (3 + qi)\right)\left(z - (3 - qi)\right)`

Expand, keeping the complex terms bracketed

`= z^{2} - \left((3 - qi) + (3 + qi)\right)z + (3 + qi)(3 - qi)`

The imaginary parts cancel in both places, and the final product uses $i^{2} = - 1$

$= z^{2} - 6 z + ( 9 - q^{2} i^{2} ) = z^{2} - 6 z + ( 9 + q^{2} )$

**[M1]**

Comparing the coefficients of $z$ on each side gives an equation for $p$

$- 12 p = - 6$

$p = \frac{1}{2}$

**[A1]**

Comparing the constant terms gives an equation for $q$

$9 + q^{2} = 58$* so *$q^{2} = 49 , \text{giving} q = 7$* or *$q = - 7$

The question states that $q$ is positive, so only one value is possible

$q = 7$

**[A1]**

> **[mark-scheme]**
> **B1**: Conjugate root stated as $3 - q i$. This mark is independent, and no working is required.
> 
> **M1**: A complete valid method leading to the quadratic in terms of $q$, reaching $z^{2} - 6 z + ( 9 + q^{2} )$ or equivalent. Accept multiplying the linear factors, using the sum and product of the roots, or substituting $3 + q i$ into the equation and equating real and imaginary parts to zero.
> 
> **A1**: Correct value $p = \frac{1}{2}$. Accept $0 . 5$.
> 
> **A1**: Correct value $q = 7$, with $q = - 7$ rejected on the grounds that $q$ is positive. Giving $q = \pm 7$ without resolving the sign does not earn this mark.

### Q16
Write $z$ in Cartesian form so that both sides can be compared

$z = x + i y$* and *$z^{\ast} = x - i y$* where *$x , y \in ℝ$

Square the left-hand side, using $i^{2} = - 1$

$z^{2} = ( x + i y )^{2} = ( x^{2} - y^{2} ) + 2 x y  i$

The right-hand side is already in Cartesian form

$4 z^{\ast} = 4 x - 4 y  i$

Two complex numbers are equal only when both parts match, so equate them separately

$( x^{2} - y^{2} ) + 2 x y  i = 4 x - 4 y  i$

$x^{2} - y^{2} = 4 x$* and *$2 x y = - 4 y$

**[M1 A1]**

Rearrange the imaginary equation and factorise rather than dividing, so that no solutions are lost

$2 x y + 4 y = 0$* so *$2 y ( x + 2 ) = 0$

This gives two separate cases to follow through

$y = 0$* or *$x = - 2$

**[M1]**

In the first case, substitute $y = 0$ into the real equation

$x^{2} = 4 x$* so *$x ( x - 4 ) = 0 , \text{giving} x = 0$* or *$x = 4$

In the second case, substitute $x = - 2$ into the real equation

$4 - y^{2} = - 8$* so *$y^{2} = 12 , \text{giving} y = \pm 2 \sqrt{3}$

Combining the four pairs of values gives the complete set of solutions

$z = 0 ,  z = 4 ,  z = - 2 + 2 \sqrt{3}  i ,  z = - 2 - 2 \sqrt{3}  i$

**[A1]**

> **[exam-tip]**
> Resist the temptation to divide $2 x y = - 4 y$ through by $y$. Doing so assumes $y \neq 0$ and throws away two of the four answers, including $z = 0$. Factorising instead keeps both cases.

> **[mark-scheme]**
> **M1**: Substitution of $z = x + i y$ and $z^{\ast} = x - i y$, with $z^{2}$ expanded and real and imaginary parts equated.
> 
> **A1**: Both equations correct, $x^{2} - y^{2} = 4 x$ and $2 x y = - 4 y$, or equivalent.
> 
> **M1**: The imaginary equation factorised to give both cases, $y = 0$ and $x = - 2$, with at least one case substituted back into the real equation. Dividing by $y$ and considering only $x = - 2$ does not earn this mark.
> 
> **A1**: All four solutions correct, $0$, $4$, $- 2 + 2 \sqrt{3}  i$ and $- 2 - 2 \sqrt{3}  i$. The surds must be exact, so decimals do not score. All four are required, and any additional incorrect solution loses this mark. A modulus-argument or exponential-form method reaching the same four solutions earns full marks.

### Q17
Write the real and imaginary parts of $z$ as single letters to keep the algebra readable

$\text{Re} ( z ) = a$* and *$\text{Im} ( z ) = b$* so *$z = a + b i$

Squaring the definition of the principal square root must return $z$

`z = \left(\sqrt{z}\right)^{2} = (x + iy)^{2} = (x^{2} - y^{2}) + 2xy\,i = a + bi`

Two complex numbers are equal only when both parts match, so equate them separately

$x^{2} - y^{2} = a$* and *$2 x y = b$

**[M1 A1]**

Make $y$ the subject of the second equation so it can be removed from the first

$y = \frac{b}{2x}$

Substitute into the first equation and clear the fraction by multiplying through by $4 x^{2}$

`x^{2} - \left(\dfrac{b}{2x}\right)^{2} = a`* so *$4 x^{4} - 4 a x^{2} - b^{2} = 0$

**[M1]**

This is a quadratic in $x^{2}$, so apply the quadratic formula with the variable $x^{2}$

$x^{2} = \frac{4a\pm\sqrt{16a^{2}+16b^{2}}}{8} = \frac{a\pm\sqrt{a^{2}+b^{2}}}{2}$

**[A1]**

Now decide the sign. Since $x$ is real, $x^{2}$ cannot be negative, and `\sqrt{a^{2} + b^{2}} \geqslant |a| \geqslant a`, so the version with the minus sign is never positive and must be rejected

$x^{2} = \frac{a+\sqrt{a^{2}+b^{2}}}{2}$

Take the positive square root, which is the one the definition requires since `x \geqslant 0`, and put $a$ and $b$ back in terms of $z$

`x = \sqrt{\dfrac{\text{Re}(z) + \sqrt{\left(\text{Re}(z)\right)^{2} + \left(\text{Im}(z)\right)^{2}}}{2}}`

**[A1]**

> **[mark-scheme]**
> **M1**: Squaring $x + i y$ and equating real and imaginary parts to $\text{Re} ( z )$ and $\text{Im} ( z )$ respectively.
> 
> **A1**: Both equations correct, $x^{2} - y^{2} = \text{Re} ( z )$ and $2 x y = \text{Im} ( z )$.
> 
> **M1**: One variable eliminated to give an equation in $x$ alone. Accept the substitution $y = \frac{\text{Im}(z)}{2x}$ shown here, or the alternative route using $( x^{2} + y^{2} )^{2} = ( x^{2} - y^{2} )^{2} + ( 2 x y )^{2}$, or completing the square.
> 
> **A1**: Correct expression for $x^{2}$, namely $\frac{a\pm\sqrt{a^{2}+b^{2}}}{2}$ or the equivalent obtained without the $\pm$.
> 
> **A1**: The negative version rejected with a reason, and the printed result reached with the positive square root taken. The reason must refer to $x$ being real, so that `x^{2} \geqslant 0`. Because the result is given, the working must be visible throughout.
The second equation from part (a) already links $y$ to $x$ and the imaginary part, so rearrange it

$2 x y = \text{Im} ( z )$

$y = \frac{\text{Im}(z)}{2x}$

**[B1]**

Since $x > 0$, the denominator $2 x$ is positive, so dividing by it cannot change a sign

**Final answer:** **y is Im(z) divided by a positive number, so y takes the same sign as Im(z)**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct formula $y = \frac{\text{Im}(z)}{2x}$, or equivalent.
> 
> **B1**: A correct explanation identifying that $2 x$ is positive because $x > 0$, so dividing by it preserves the sign. Accept any equivalent wording, including treating the three cases of $\text{Im} ( z )$ positive, negative and zero separately.
Rearranging the first equation from part (a) gives $y^{2}$ in terms of $x^{2}$

$y^{2} = x^{2} - a$

Substitute the expression for $x^{2}$ found in part (a)

$y^{2} = \frac{a+\sqrt{a^{2}+b^{2}}}{2} - a = \frac{a+\sqrt{a^{2}+b^{2}}-2a}{2}$

Simplify the numerator

$y^{2} = \frac{-a+\sqrt{a^{2}+b^{2}}}{2}$

**[M1]**

Taking the square root introduces both signs, since $y$ may be positive or negative, and part (b) shows which one applies

`y = \pm\sqrt{\dfrac{-\text{Re}(z) + \sqrt{\left(\text{Re}(z)\right)^{2} + \left(\text{Im}(z)\right)^{2}}}{2}}`

**[A1]**

> **[mark-scheme]**
> **M1**: A correct method reaching $y^{2}$, by substituting the result of part (a) into $y^{2} = x^{2} - \text{Re} ( z )$ or by eliminating $x$ from the two original equations.
> 
> **A1**: The printed result obtained, with the $\pm$ present and justified by $y$ being able to take either sign. Because the result is given, the working must be visible.
(i)

Rather than working backwards through the formulae, put each case into $\sqrt{z} = x + i y$ and square. With $x = 0$ the square root is purely imaginary

$\sqrt{z} = i y$* so *$z = ( i y )^{2} = i^{2} y^{2} = - y^{2}$

Since $y$ is real and non-zero, $y^{2}$ is positive, so $- y^{2}$ is negative

**Final answer:** $z$** is a negative real number**

**[B1]**

(ii)

With $y = 0$ the square root is purely real

$\sqrt{z} = x$* so *$z = x^{2}$

Since $x$ is real and non-zero, $x^{2}$ is positive

**Final answer:** $z$** is a positive real number**

**[B1]**

(iii)

With both parts zero the square root itself is zero

$\sqrt{z} = 0$* so *$z = 0$

**Final answer:** $z$** is equal to zero**

**[B1]**

> **[exam-tip]**
> It is much quicker to square the square root than to unpick the formulae from parts (a) and (c). Each case makes $\sqrt{z}$ either purely imaginary, purely real, or zero, and squaring immediately tells you what $z$ must be.

> **[mark-scheme]**
> **B1**: $z$ identified as a negative real number. Accept $z < 0$ with $z$ real, or $\text{Im} ( z ) = 0$ with $\text{Re} ( z ) < 0$.
> 
> **B1**: $z$ identified as a positive real number. Accept $z > 0$ with $z$ real, or $\text{Im} ( z ) = 0$ with $\text{Re} ( z ) > 0$.
> 
> **B1**: $z$ identified as zero.

### Q18
Square $α$, using $i^{2} = - 1$

$α^{2} = ( 1 - 3 i ) ( 1 - 3 i ) = 1 - 3 i - 3 i + 9 i^{2} = 1 - 6 i - 9$

$α^{2} = - 8 - 6 i$

**[B1]**

Multiply by $α$ again to reach the cube

$α^{3} = ( - 8 - 6 i ) ( 1 - 3 i ) = - 8 + 24 i - 6 i + 18 i^{2} = - 8 + 18 i - 18$

$α^{3} = - 26 + 18 i$

**[B1]**

Since $α$ satisfies the equation, substituting it must give zero

$( - 26 + 18 i ) + 4 ( - 8 - 6 i ) + k ( 1 - 3 i ) + m = 0$

Remove the brackets and gather the real terms and the imaginary terms

$( - 26 - 32 + k + m ) + ( 18 - 24 - 3 k ) i = 0$

For a complex number to be zero, both parts must be zero separately, which gives two equations

$k + m = 58$* and *$- 6 - 3 k = 0$

**[M1]**

The imaginary equation involves only $k$, so solve it first

$k = - 2$

**[A1]**

Substitute this value into the real equation

$- 2 + m = 58$

$m = 60$

**[A1]**

> **[mark-scheme]**
> **B1**: Correct value $α^{2} = - 8 - 6 i$, with $i^{2} = - 1$ used.
> 
> **B1**: Correct value $α^{3} = - 26 + 18 i$.
> 
> **M1**: Substitution into the cubic with real and imaginary parts equated to zero, giving two equations in $k$ and $m$.
> 
> **A1**: Correct value $k = - 2$.
> 
> **A1**: Correct value $m = 60$.
With $k$ and $m$ now known the cubic has real coefficients, so the conjugate of $α$ is also a root

$α^{\ast} = 1 + 3 i$

**[B1]**

These two roots give a quadratic factor with real coefficients

`\left(z - (1 - 3i)\right)\left(z - (1 + 3i)\right) = z^{2} - 2z + (1 + 9) = z^{2} - 2z + 10`

The cubic is this quadratic multiplied by the factor coming from the remaining root

$z^{3} + 4 z^{2} - 2 z + 60 = ( z^{2} - 2 z + 10 ) ( z - δ )$

Compare the constant terms

$10 \times ( - δ ) = 60$

$δ = - 6$

**[M1]**

Put $δ$ back into the bracket, so the remaining factor is $z - ( - 6 )$

$z^{3} + 4 z^{2} - 2 z + 60 = ( z^{2} - 2 z + 10 ) ( z + 6 )$

Setting the linear factor to zero gives the third root

**Final answer:** **The other two roots are **$1 + 3 i$** and **$- 6$

**[A1]**

> **[mark-scheme]**
> **B1**: Conjugate root stated as $1 + 3 i$. This mark is independent, and no working is required.
> 
> **M1**: A complete valid method for the third root. Accept forming the quadratic factor $z^{2} - 2 z + 10$ and then comparing coefficients or dividing the cubic by it, or using the sum or product of the three roots.
> 
> **A1**: Both remaining roots given, $1 + 3 i$ and $- 6$. Follow through from an incorrect $k$ or $m$ in part (a) provided the method here is correct.

### Q19
(i)

Complete the square on the first two terms, halving the coefficient of $z$ and subtracting the square of what was added

$z^{2} + 2 i z - 10 = ( z + i )^{2} - i^{2} - 10$

**[M1]**

The subtracted term is $- i^{2}$, which is $+ 1$, so the constant simplifies

$= ( z + i )^{2} - ( - 1 ) - 10 = ( z + i )^{2} - 9$

**Final answer:** $f ( z ) = ( z + i )^{2} - 9$**, so **$a = 1$** and **$b = - 9$

**[A1]**

(ii)

Set the completed square form equal to zero and isolate the squared bracket

$( z + i )^{2} - 9 = 0$* so *$( z + i )^{2} = 9$

Take the square root of both sides, keeping both signs

$z + i = \pm 3$

**[M1]**

Subtract $i$ from both sides

$z = - i \pm 3$

**Final answer:** $z = 3 - i$** or **$z = - 3 - i$

**[A1]**

> **[exam-tip]**
> Look carefully at these two solutions: they are not complex conjugates of each other. The rule that non-real roots come in conjugate pairs applies only when every coefficient is real, and here the coefficient of $z$ is $2 i$.

> **[mark-scheme]**
> **M1**: Completing the square attempted, reaching $( z + i )^{2}$ together with a correction term.
> 
> **A1**: Correct form $( z + i )^{2} - 9$, with $i^{2} = - 1$ used, and the values $a = 1$ and $b = - 9$ identified. Because the form is given in the question, the working must be visible.
> 
> **M1**: The squared bracket isolated and the square root taken with both signs, giving $z + i = \pm 3$. Accept instead using the quadratic formula on $z^{2} + 2 i z - 10 = 0$.
> 
> **A1**: Both solutions correct, $3 - i$ and $- 3 - i$. Both are required. Note these are not a conjugate pair, so an answer of the form $3 \pm i$ does not score.

### Q20
A quadratic with real coefficients has non-real roots exactly when its discriminant is negative, and a negative discriminant automatically gives two distinct roots, so use $b^{2} - 4 a c < 0$ with $a = 1$ and $c = 18$

$b^{2} - 4 ( 1 ) ( 18 ) < 0$

**[M1]**

Simplify and isolate $b^{2}$

$b^{2} - 72 < 0$* so *$b^{2} < 72$

**[A1]**

Taking the square root of both sides gives a two-sided inequality, since $b$ may be negative

$- \sqrt{72} < b < \sqrt{72}$

Simplify the surd, using $\sqrt{72} = \sqrt{36\times2} = 6 \sqrt{2}$

$- 6 \sqrt{2} < b < 6 \sqrt{2}$

**[A1]**

> **[mark-scheme]**
> **M1**: Discriminant used with the correct inequality, $b^{2} - 4 ( 1 ) ( 18 ) < 0$. Using `\leqslant` or $= 0$ does not earn this mark, since the roots must be non-real.
> 
> **A1**: Correct simplified inequality $b^{2} < 72$, or equivalent.
> 
> **A1**: Correct range $- 6 \sqrt{2} < b < 6 \sqrt{2}$. Accept any equivalent form, including $- \sqrt{72} < b < \sqrt{72}$, the interval $( - 6 \sqrt{2} , 6 \sqrt{2} )$, or `|b| < 6\sqrt{2}`. Both bounds are needed, and the inequalities must be strict.

### Q21
Multiply out the left-hand side, keeping the unknown term together

$( 2 + 5 i ) z + ( 2 + 5 i ) ( 2 i ) = - 7 - 32 i$

Expand the second product and use $i^{2} = - 1$

$( 2 + 5 i ) z + 4 i + 10 i^{2} = - 7 - 32 i$* so *$( 2 + 5 i ) z + 4 i - 10 = - 7 - 32 i$

**[M1]**

Collect the known terms on the right-hand side

$( 2 + 5 i ) z = - 7 - 32 i + 10 - 4 i = 3 - 36 i$

**[A1]**

Divide by $2 + 5 i$, multiplying numerator and denominator by the conjugate so the denominator becomes real

$z = \frac{3-36i}{2+5i} \times \frac{2-5i}{2-5i} = \frac{6-15i-72i+180i^{2}}{4+25}$

**[M1]**

Simplify the numerator using $i^{2} = - 1$, then divide through

$z = \frac{6-87i-180}{29} = \frac{-174-87i}{29}$

$z = - 6 - 3 i$

**[A1]**

> **[mark-scheme]**
> **M1**: Left-hand side expanded with $i^{2} = - 1$ used, so that the term in $z$ is separated from the constant terms.
> 
> **A1**: Correct simplified equation $( 2 + 5 i ) z = 3 - 36 i$, or equivalent.
> 
> **M1**: Clear intention to multiply the numerator and the denominator by the conjugate of the denominator, with working shown for the numerator or the denominator. Accept instead writing $z = x + i y$, expanding, and equating real and imaginary parts to form two simultaneous equations.
> 
> **A1**: Correct answer $z = - 6 - 3 i$. A correct answer with no working scores nothing, since no marks are given for unsupported answers from a calculator.

### Q22
A cubic has three roots, and since the coefficients are real the non-real ones occur in conjugate pairs, so the third root is the conjugate of $- 2 - 3 i$

$( - 2 - 3 i )^{\ast} = - 2 + 3 i$

**[B1]**

Take the two complex roots together, because their linear factors multiply to a quadratic with real coefficients

`\left(z - (-2 - 3i)\right)\left(z - (-2 + 3i)\right) = z^{2} + 4z + (4 - 9i^{2})`

**[M1]**

Replace $i^{2}$ by $- 1$

$= z^{2} + 4 z + 13$

**[A1]**

The real root $3$ contributes the factor $( z - 3 )$, so multiply the two factors together

$f ( z ) = ( z - 3 ) ( z^{2} + 4 z + 13 ) = z^{3} + 4 z^{2} + 13 z - 3 z^{2} - 12 z - 39$

**[M1]**

Collect like terms and compare with $z^{3} + z^{2} + c z + d$

$f ( z ) = z^{3} + z^{2} + z - 39$

$c = 1 ,  d = - 39$

**[A1]**

> **[mark-scheme]**
> **B1**: Third root identified as $- 2 + 3 i$. This mark is independent, and no working is required.
> 
> **M1**: A complete valid method for the quadratic factor with zeros $- 2 - 3 i$ and $- 2 + 3 i$. Accept multiplying the linear factors, or using the sum and product of that pair.
> 
> **A1**: Correct quadratic factor $z^{2} + 4 z + 13$, with $i^{2} = - 1$ used so that the coefficients are real.
> 
> **M1**: Correct method for multiplying the quadratic factor by $( z - 3 )$, with all six terms attempted. Accept instead substituting $z = 3$ into $f ( z )$ and using a second equation from one of the complex roots.
> 
> **A1**: Both values correct, $c = 1$ and $d = - 39$.

### Q23
The coefficients are real, so the non-real roots occur in conjugate pairs and the second root follows at once

$( - 3 + 2 i )^{\ast} = - 3 - 2 i$

**[B1]**

With both roots known, the quadratic is the product of the two corresponding linear factors

`z^{2} + bz + c = \left(z - (-3 + 2i)\right)\left(z - (-3 - 2i)\right)`

**[M1]**

Expand, keeping the complex terms bracketed

$= z^{2} - ( - 3 - 2 i ) z - ( - 3 + 2 i ) z + ( - 3 + 2 i ) ( - 3 - 2 i )$

The imaginary parts of the middle terms cancel, and the final product is a complex number times its conjugate

$= z^{2} + 6 z + ( 9 - 4 i^{2} )$

Replace $i^{2}$ by $- 1$, which makes the constant term real

$z^{2} + b z + c = z^{2} + 6 z + 13$

Compare the coefficients

$b = 6 ,  c = 13$

**[A1 A1]**

> **[mark-scheme]**
> **B1**: Conjugate root stated as $- 3 - 2 i$. This mark is independent, and no working is required.
> 
> **M1**: A complete valid method for forming the quadratic. Accept multiplying the two linear factors, or using the sum and product of the roots, or substituting $- 3 + 2 i$ into the equation and equating real and imaginary parts to zero.
> 
> **A1**: Correct value $b = 6$. The coefficient of $z$ is the negative of the sum of the roots, so a sign error here is the common slip.
> 
> **A1**: Correct value $c = 13$. This requires $i^{2} = - 1$ to have been used, so that the product of the two roots is real.

### Q24
Expand the square of the general square root

$( x + i y )^{2} = ( x + i y ) ( x + i y ) = x^{2} + x y i + x y i + i^{2} y^{2}$

Use $i^{2} = - 1$ and gather into real and imaginary parts

$= ( x^{2} - y^{2} ) + 2 x y  i$

**[M1]**

This must equal $- 21 - 20 i$, and two complex numbers are equal only when both parts match

$( x^{2} - y^{2} ) + 2 x y  i = - 21 - 20 i$

$x^{2} - y^{2} = - 21$* and *$2 x y = - 20$

**[A1]**

Make $y$ the subject of the simpler equation so that one variable can be removed

$y = - \frac{10}{x}$

Substitute into the first equation

`x^{2} - \left(-\dfrac{10}{x}\right)^{2} = -21`* so *$x^{2} - \frac{100}{x^{2}} = - 21$

**[M1]**

Multiply through by $x^{2}$ and collect on one side, which leaves a quadratic in $x^{2}$

$x^{4} + 21 x^{2} - 100 = 0$

**[A1]**

Factorise, treating $x^{2}$ as the variable

$( x^{2} - 4 ) ( x^{2} + 25 ) = 0$* so *$x^{2} = 4$* or *$x^{2} = - 25$

Only $x^{2} = 4$ can be used, because $x$ is a real number

$x = 2$* or *$x = - 2$

Each value of $x$ gives its own value of $y$ from $y = - \frac{10}{x}$

$x = 2 ,  y = - 5$* and *$x = - 2 ,  y = 5$

**[A1]**

Each pair gives a square root of the form $x + i y$

**Final answer:** **The two square roots are **$2 - 5 i$** and **$- 2 + 5 i$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct expansion of $( x + i y )^{2}$ with $i^{2} = - 1$ used, giving three terms when simplified.
> 
> **A1**: Real and imaginary parts equated to $- 21$ and $- 20$ respectively, giving both equations. Condone $+ 20$ in place of $- 20$ at this stage.
> 
> **M1**: One variable eliminated between the two equations, giving a single equation in $x$ or in $y$. Substituting $y = - 10 x$ rather than $y = - \frac{10}{x}$ is a serious algebraic error and does not earn this mark.
> 
> **A1**: Correct equation $x^{4} + 21 x^{2} - 100 = 0$, or equivalently $y^{4} - 21 y^{2} - 100 = 0$. Accept three-term equivalents, and condone a missing "$= 0$" if implied by later working.
> 
> **A1**: Both pairs found and correctly paired, $x = 2$ with $y = - 5$, and $x = - 2$ with $y = 5$. The rejection of $x^{2} = - 25$ must be justified by $x$ being real.
> 
> **A1**: Both square roots given in exact Cartesian form, $2 - 5 i$ and $- 2 + 5 i$. Accept $\pm ( 2 - 5 i )$. Both are required, and any additional incorrect root loses this mark.

### Q25
(i)

Subtract, taking care with the signs in the second bracket

$z_{2} - z_{1} = ( - 3 + 5 i ) - ( 1 - 2 i ) = - 4 + 7 i$

The real part is the term without $i$

$\text{Re} ( z_{2} - z_{1} ) = - 4$

**[B1]**

(ii)

Expand the product, then use $i^{2} = - 1$

$z_{1} z_{2} = ( 1 - 2 i ) ( - 3 + 5 i ) = - 3 + 5 i + 6 i - 10 i^{2}$

$= - 3 + 11 i + 10 = 7 + 11 i$

**[M1]**

The imaginary part is the real number multiplying $i$

$\text{Im} ( z_{1} z_{2} ) = 11$

**[A1]**

(iii)

To divide, multiply the numerator and the denominator by the conjugate of the denominator, which makes the denominator real

$\frac{z_{1}}{z_{2}} = \frac{1-2i}{-3+5i} \times \frac{-3-5i}{-3-5i}$

**[M1]**

Expand the numerator and the denominator separately

$= \frac{-3-5i+6i+10i^{2}}{9+25} = \frac{-3+i-10}{34}$

Divide each part of the numerator by the real denominator

$\frac{z_{1}}{z_{2}} = \frac{-13+i}{34} = - \frac{13}{34} + \frac{1}{34} i$

**[A1]**

Finally take the conjugate, which reverses the sign of the imaginary part

`\left(\dfrac{z_{1}}{z_{2}}\right)^{*} = -\dfrac{13}{34} - \dfrac{1}{34}i`

**[A1]**

> **[mark-scheme]**
> **B1**: Correct value $- 4$. The answer must be the real number alone.
> 
> **M1**: Correct expansion of $( 1 - 2 i ) ( - 3 + 5 i )$ with $i^{2} = - 1$ used, reaching $7 + 11 i$.
> 
> **A1**: Correct value $11$. The answer must be the real number alone, so $11 i$ does not score.
> 
> **M1**: Clear intention to multiply the numerator and the denominator by the conjugate of the denominator, with working shown for the numerator or the denominator.
> 
> **A1**: Correct quotient $- \frac{13}{34} + \frac{1}{34} i$, or equivalent.
> 
> **A1**: Correct conjugate $- \frac{13}{34} - \frac{1}{34} i$. The answer must be split into real and imaginary parts, so $\frac{-13-i}{34}$ alone does not score. A correct answer with no working scores nothing for the division marks, since the syllabus requires full details of the working.

### Q26
Substituting $α$ into the cubic needs its square and its cube, so work those out first

$α^{2} = ( - 1 + 4 i ) ( - 1 + 4 i ) = 1 - 4 i - 4 i + 16 i^{2}$

**[M1]**

Replace $i^{2}$ by $- 1$ and collect

$α^{2} = 1 - 8 i - 16 = - 15 - 8 i$

Multiply by $α$ again to reach the cube

$α^{3} = ( - 15 - 8 i ) ( - 1 + 4 i ) = 15 - 60 i + 8 i - 32 i^{2} = 15 - 52 i + 32 = 47 - 52 i$

**[M1]**

Now substitute all three into the left-hand side of the equation

$α^{3} + 5 α^{2} + 23 α + 51 = ( 47 - 52 i ) + 5 ( - 15 - 8 i ) + 23 ( - 1 + 4 i ) + 51$

Remove the brackets

$= 47 - 52 i - 75 - 40 i - 23 + 92 i + 51$

Group the real terms and the imaginary terms

$= ( 47 - 75 - 23 + 51 ) + ( - 52 - 40 + 92 ) i = 0 + 0 i$

**Final answer:** **The result is zero, so **$α = - 1 + 4 i$** is a root of the equation**

**[A1]**

> **[mark-scheme]**
> **M1**: Substitution of $- 1 + 4 i$ into the equation with expansions of $α^{2}$ and $α^{3}$ attempted. All the working must be seen; allow small slips in one expansion.
> 
> **M1**: Use of $i^{2} = - 1$ correctly at least once.
> 
> **A1**: Verification completed correctly, showing that both the real part and the imaginary part are zero, with a conclusion stated. Because the result is given, an unsupported assertion scores nothing.
The cubic has real coefficients, so the conjugate of $α$ is also a root

$α^{\ast} = - 1 - 4 i$

**[B1]**

These two roots give a quadratic factor with real coefficients, so multiply their linear factors

`\left(z - (-1 + 4i)\right)\left(z - (-1 - 4i)\right) = z^{2} + 2z + (1 - 16i^{2})`

$= z^{2} + 2 z + 17$

The cubic is this quadratic multiplied by the factor from the remaining root

$z^{3} + 5 z^{2} + 23 z + 51 = ( z^{2} + 2 z + 17 ) ( z - δ )$

Compare the constant terms

$17 \times ( - δ ) = 51$

$δ = - 3$

**[M1]**

So the remaining factor is $z - ( - 3 )$

$z^{3} + 5 z^{2} + 23 z + 51 = ( z^{2} + 2 z + 17 ) ( z + 3 )$

Setting the linear factor to zero gives the third root

**Final answer:** **The other two roots are **$- 1 - 4 i$** and **$- 3$

**[A1]**

> **[mark-scheme]**
> **B1**: Conjugate root stated as $- 1 - 4 i$. This mark is independent, and no working is required.
> 
> **M1**: A complete valid method for the third root. Accept forming the quadratic factor $z^{2} + 2 z + 17$ and then comparing coefficients or dividing the cubic by it, or using the sum or product of the three roots.
> 
> **A1**: Both remaining roots given, $- 1 - 4 i$ and $- 3$. Stating the conjugate and then the third root with no supporting algebra does not earn the method mark, since no marks are given for unsupported answers.

### Q27
Expand the product, keeping $a$ and $b$ as unknowns

$z_{1} z_{2} = ( a - 6 i ) ( 1 + b i ) = a + a b i - 6 i - 6 b i^{2}$

Use $i^{2} = - 1$, then gather into real and imaginary parts

$= ( a + 6 b ) + ( a b - 6 ) i$

Two complex numbers are equal only when both parts match, so compare with $- 17 - 9 i$

$( a + 6 b ) + ( a b - 6 ) i = - 17 - 9 i$

$a + 6 b = - 17$* and *$a b - 6 = - 9$

**[M1]**

The second equation gives a simple relationship between the unknowns

$a b = - 3$* so *$b = - \frac{3}{a}$

**[A1]**

Substitute this into the first equation to eliminate $b$

`a + 6\left(-\dfrac{3}{a}\right) = -17`* so *$a - \frac{18}{a} = - 17$

Multiply through by $a$ and collect everything on one side

$a^{2} - 18 = - 17 a$* so *$a^{2} + 17 a - 18 = 0$

**[M1]**

Factorise and read off the two possibilities, taking the matching value of $b$ each time

$( a + 18 ) ( a - 1 ) = 0$* so *$a = - 18$* or *$a = 1$

$a = 1 ,  b = - 3$

$a = - 18 ,  b = \frac{1}{6}$

**[A1]**

> **[mark-scheme]**
> **M1**: Product expanded with $i^{2} = - 1$ used, and real and imaginary parts equated to give two equations in $a$ and $b$.
> 
> **A1**: Both equations correct, $a + 6 b = - 17$ and $a b = - 3$, or equivalent.
> 
> **M1**: One variable eliminated to give a three-term quadratic in the other, $a^{2} + 17 a - 18 = 0$ or $6 b^{2} + 17 b - 3 = 0$.
> 
> **A1**: Both pairs found and correctly paired, $a = 1$ with $b = - 3$, and $a = - 18$ with $b = \frac{1}{6}$. The question asks for the possible values, so only one pair does not score this mark.
Look at the second pair from part (a), where $z_{1} = - 18 - 6 i$, because that number has $3 + i$ hidden inside it

$- 18 - 6 i = - 6 ( 3 + i )$

So the product from part (a) can be rewritten with the factor of $- 6$ pulled out

`(-18 - 6i)\left(1 + \dfrac{1}{6}i\right) = -(3 + i) \times 6\left(1 + \dfrac{1}{6}i\right) = -17 - 9i`

**[M1]**

Multiplying the $6$ into the second bracket gives the number in the required form

`6\left(1 + \dfrac{1}{6}i\right) = 6 + i`

$c = 6 ,  d = 1$

**[A1]**

> **[mark-scheme]**
> **M1**: The link to part (a) identified, for example by writing $- 18 - 6 i = - 6 ( 3 + i )$, or by rearranging to $( 3 + i ) ( c + d i ) = 17 + 9 i$ and working from there.
> 
> **A1**: Both values correct, $c = 6$ and $d = 1$. The command is to state the values, so this mark is available for a correct pair seen on its own without supporting working.

### Q28
Add the two complex numbers, keeping the real and imaginary parts separate

$z_{1} + z_{2} = ( 3 + a i ) + ( b - 7 i ) = ( 3 + b ) + ( a - 7 ) i$

Two complex numbers are equal only when their real parts match and their imaginary parts match, so compare with $14 + i$

$( 3 + b ) + ( a - 7 ) i = 14 + i$

$3 + b = 14$* and *$a - 7 = 1$

**[M1]**

Solve each equation separately

$a = 8 ,  b = 11$

**[A1]**

> **[mark-scheme]**
> **M1**: Real and imaginary parts equated to give two equations, $3 + b = 14$ and $a - 7 = 1$, or equivalent. Accept the equations obtained by subtracting $z_{1}$ from $14 + i$ instead.
> 
> **A1**: Both values correct, $a = 8$ and $b = 11$. Take care not to swap them, since $a$ belongs to the imaginary part and $b$ to the real part.
(i)

Square $3 - 5 i$ first, since that is the only part of $f ( z )$ that needs expanding

$( 3 - 5 i )^{2} = ( 3 - 5 i ) ( 3 - 5 i ) = 9 - 15 i - 15 i + 25 i^{2}$

Replace $i^{2}$ by $- 1$ and collect

$= 9 - 30 i - 25 = - 16 - 30 i$

**[M1]**

Substitute into $f ( z )$, using the square just found

$f ( 3 - 5 i ) = ( - 16 - 30 i ) - 6 ( 3 - 5 i ) + 34 = - 16 - 30 i - 18 + 30 i + 34$

Group the real terms and the imaginary terms to see that both vanish

$= ( - 16 - 18 + 34 ) + ( - 30 + 30 ) i = 0 + 0 i$

**Final answer:** $f ( 3 - 5 i ) = 0$**, so **$z = 3 - 5 i$** is a root**

**[A1]**

(ii)

The coefficients of $f ( z )$ are real, so its non-real roots occur in conjugate pairs

$z = 3 + 5 i$

**[B1]**

> **[mark-scheme]**
> **M1**: Correct expansion of $( 3 - 5 i )^{2}$ with $i^{2} = - 1$ used, reaching $- 16 - 30 i$.
> 
> **A1**: Correct substitution into $f ( z )$ and a complete verification that the result is zero, with a conclusion stated. Both the real and the imaginary parts must be shown to cancel.
> 
> **B1**: Other root stated as $3 + 5 i$. This mark is independent, and no working is required.

### Q29
(i)

The equation has real coefficients, so its non-real roots occur in conjugate pairs

$7 + i$

**[B1]**

(ii)

Both roots are known, so the equation can be built as the product of the two corresponding linear factors

`\left(z - (7 - i)\right)\left(z - (7 + i)\right) = 0`

**[M1]**

Expand, keeping the complex terms bracketed

$z^{2} - ( 7 + i ) z - ( 7 - i ) z + ( 7 - i ) ( 7 + i ) = 0$

The imaginary parts of the middle terms cancel, and the last product is a complex number times its conjugate

$z^{2} - 14 z + 49 - i^{2} = 0$

**[A1]**

Replace $i^{2}$ by $- 1$, which makes the constant term real, then compare with $z^{2} + b z + c = 0$

$b = - 14 ,  c = 50$

$z^{2} - 14 z + 50 = 0$

**[A1]**

> **[mark-scheme]**
> **B1**: Other root stated as $7 + i$. This mark is independent, and no working is required.
> 
> **M1**: A complete valid method for forming the quadratic. Accept multiplying the two linear factors, or using the sum and product of the roots to write $z^{2} - ( \text{sum} ) z + ( \text{product} ) = 0$.
> 
> **A1**: Correct expansion with the middle terms combined and the conjugate product formed, reaching $z^{2} - 14 z + 49 - i^{2} = 0$ or equivalent.
> 
> **A1**: Correct equation $z^{2} - 14 z + 50 = 0$, with $i^{2} = - 1$ used so that both coefficients are real. The equation must be given in the requested form, so a factorised answer alone does not score this mark.

### Q30
The conjugate reverses the sign of the imaginary part

$z_{2}^{\ast} = 2 + i$

Expand the first product

$z_{1} \times z_{2}^{\ast} = ( 5 + 7 i ) ( 2 + i ) = 10 + 5 i + 14 i + 7 i^{2}$

**[M1]**

Replace $i^{2}$ by $- 1$ and collect

$= 10 + 19 i - 7$

$z_{1} \times z_{2}^{\ast} = 3 + 19 i$

**[A1]**

Now expand the second product, which pairs $z_{2}$ with its own conjugate

$z_{2} \times z_{2}^{\ast} = ( 2 - i ) ( 2 + i ) = 4 + 2 i - 2 i - i^{2} = 4 + 1$

$z_{2} \times z_{2}^{\ast} = 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct conjugate $z_{2}^{\ast} = 2 + i$ used, with a complete expansion of $( 5 + 7 i ) ( 2 + i )$ attempted.
> 
> **A1**: Correct product $3 + 19 i$, with $i^{2} = - 1$ used.
> 
> **A1**: Correct product $5$. The imaginary terms cancel, so the answer must be a real number.
Multiplying numerator and denominator by $z_{2}^{\ast}$ makes the denominator real, so part (a) supplies both products

$\frac{z_{1}}{z_{2}} = \frac{z_{1}\timesz_{2}^{\ast}}{z_{2}\timesz_{2}^{\ast}} = \frac{3+19i}{5}$

**[M1]**

The denominator is real, so divide each part of the numerator by it

$\frac{z_{1}}{z_{2}} = \frac{3}{5} + \frac{19}{5} i$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct use of the conjugate to obtain $\frac{3+19i}{5}$. Because the question says "hence or otherwise", the direct route also earns this mark: multiplying numerator and denominator of $\frac{5+7i}{2-i}$ by $2 + i$, with working shown for the numerator or the denominator.
> 
> **A1**: Correct answer $\frac{3}{5} + \frac{19}{5} i$. Accept $0 . 6 + 3 . 8 i$ or the parts stated separately. The answer must be split into real and imaginary parts, so $\frac{3+19i}{5}$ alone does not score. A correct answer with no working scores nothing, since the syllabus requires full details of the working for division.

### Q31
Expand the square of the general square root

$( x + i y )^{2} = ( x + i y ) ( x + i y ) = x^{2} + i x y + i x y + i^{2} y^{2}$

**[M1]**

Replace $i^{2}$ by $- 1$ and gather the terms into real and imaginary parts

$= ( x^{2} - y^{2} ) + 2 x y  i$

**[A1]**

This must equal $z = - 3 + 4 i$, and two complex numbers are equal only when their real parts match and their imaginary parts match

$( x^{2} - y^{2} ) + 2 x y i = - 3 + 4 i$

$x^{2} - y^{2} = - 3$

$2 x y = 4$

**[A1]**

> **[mark-scheme]**
> **M1**: Correct expansion of $( x + i y )^{2}$ attempted, giving the four terms or the three terms after collecting.
> 
> **A1**: Correct simplified form $( x^{2} - y^{2} ) + 2 x y  i$, with $i^{2} = - 1$ used.
> 
> **A1**: Real and imaginary parts equated to $- 3$ and $4$ respectively, giving both printed equations. Because both results are given, the equating step must be visible.
(i)

Make $y$ the subject of the simpler equation so that one variable can be removed

$2 x y = 4$* so *$y = \frac{2}{x}$

Substitute this into $x^{2} - y^{2} = - 3$

`x^{2} - \left(\dfrac{2}{x}\right)^{2} = -3`* so *$x^{2} - \frac{4}{x^{2}} = - 3$

**[M1]**

Multiply through by $x^{2}$ to clear the fraction, which leaves a quadratic in $x^{2}$

$x^{4} - 4 = - 3 x^{2}$* so *$x^{4} + 3 x^{2} - 4 = 0$

**[A1]**

Factorise, treating $x^{2}$ as the variable

$( x^{2} - 1 ) ( x^{2} + 4 ) = 0$* so *$x^{2} = 1$* or *$x^{2} = - 4$

Only $x^{2} = 1$ can be used, because $x$ is a real number

$x = 1$* or *$x = - 1$

Each value of $x$ gives its own value of $y$ from $y = \frac{2}{x}$

$x = 1 ,  y = 2$

$x = - 1 ,  y = - 2$

**[A1]**

(ii)

Each pair of values gives a square root of the form $x + i y$

**Final answer:** **The two square roots are **$1 + 2 i$** and **$- 1 - 2 i$

**[A1]**

> **[mark-scheme]**
> **M1**: One variable eliminated between the two equations, giving a single equation in $x$ or in $y$.
> 
> **A1**: Correct equation obtained, $x^{4} + 3 x^{2} - 4 = 0$ or equivalently $y^{4} - 3 y^{2} - 4 = 0$. Accept three-term equivalents, and condone a missing "$= 0$" if the later working implies it.
> 
> **A1**: Both pairs found and correctly paired, $x = 1$ with $y = 2$, and $x = - 1$ with $y = - 2$. The rejection of $x^{2} = - 4$ must be justified by $x$ being real. Values stated separately are acceptable provided the pairing is clear.
> 
> **A1**: Both square roots given, $1 + 2 i$ and $- 1 - 2 i$. Accept $\pm ( 1 + 2 i )$. Both are required, and any additional incorrect root loses this mark.

### Q32
(i)

Expand the brackets, then use $i^{2} = - 1$ to make the last term real

$z_{1} \times z_{2} = ( 2 - 3 i ) ( - 7 + i ) = - 14 + 2 i + 21 i - 3 i^{2}$

$= - 14 + 23 i - 3 ( - 1 ) = - 14 + 23 i + 3$

$z_{1} \times z_{2} = - 11 + 23 i$

**[B1]**

(ii)

Add the two numbers first, collecting real and imaginary parts

$z_{1} + z_{2} = ( 2 - 3 i ) + ( - 7 + i ) = - 5 - 2 i$

The real part is the term without $i$

$\text{Re} ( z_{1} + z_{2} ) = - 5$

**[B1]**

(iii)

Subtract, taking care with the signs in the second bracket

$z_{2} - z_{1} = ( - 7 + i ) - ( 2 - 3 i ) = - 9 + 4 i$

The imaginary part is the real number multiplying $i$

$\text{Im} ( z_{2} - z_{1} ) = 4$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct product $- 11 + 23 i$, with the expansion shown and $i^{2} = - 1$ used. The syllabus requires full details of the working for multiplication, so an unsupported answer does not score.
> 
> **B1**: Correct value $- 5$. The answer must be the real number alone, not the whole complex number $- 5 - 2 i$.
> 
> **B1**: Correct value $4$. The answer must be the real number alone, so $4 i$ does not score.

### Q33
(i)

Write down the conjugate, which reverses the sign of the imaginary part

$z = x + i y$* and *$z^{\ast} = x - i y$

Add the two, so that the imaginary parts cancel

$z + z^{\ast} = ( x + i y ) + ( x - i y ) = 2 x$

**[B1]**

Divide by $2$, and recognise that $x$ is the real part of $z$

$\frac{z+z^{\ast}}{2} = \frac{2x}{2} = x$

$\text{Re} ( z ) = \frac{z+z^{\ast}}{2}$

**[B1]**

(ii)

Subtract instead, so that the real parts cancel and the imaginary parts double

$z - z^{\ast} = ( x + i y ) - ( x - i y ) = 2 i y$

Divide by $2 i$, and recognise that $y$ is the imaginary part of $z$

$\frac{z-z^{\ast}}{2i} = \frac{2iy}{2i} = y$

$\text{Im} ( z ) = \frac{z-z^{\ast}}{2i}$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct conjugate $z^{\ast} = x - i y$ used, and $z + z^{\ast} = 2 x$ obtained.
> 
> **B1**: Division by $2$ completed and the result identified as $\text{Re} ( z )$, with a conclusion. Both results are printed in the question, so the working must be shown.
> 
> **B1**: Correct $z - z^{\ast} = 2 i y$, division by $2 i$ completed, and the result identified as $\text{Im} ( z )$, with a conclusion. Dividing by $2$ rather than $2 i$ does not score.

### Q34
(i)

Square $β$ by expanding the brackets and using $i^{2} = - 1$

$β^{2} = ( - 2 - 3 i ) ( - 2 - 3 i ) = 4 + 6 i + 6 i + 9 i^{2} = 4 + 12 i - 9$

$β^{2} = - 5 + 12 i$

**[B1]**

Multiply the square by $β$ again to reach the cube

$β^{3} = ( - 5 + 12 i ) ( - 2 - 3 i ) = 10 + 15 i - 24 i - 36 i^{2} = 10 - 9 i + 36$

$β^{3} = 46 - 9 i$

**[B1]**

(ii)

Substitute $z = β$ into the cubic, using the two powers from part (i)

$β^{3} - β^{2} - 7 β - 65 = ( 46 - 9 i ) - ( - 5 + 12 i ) - 7 ( - 2 - 3 i ) - 65$

Remove the brackets

$= 46 - 9 i + 5 - 12 i + 14 + 21 i - 65$

Group the real terms and the imaginary terms

$= ( 46 + 5 + 14 - 65 ) + ( - 9 - 12 + 21 ) i = 0 + 0 i$

**Final answer:** **The result is zero, so **$β = - 2 - 3 i$** is a root of the equation**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct value $β^{2} = - 5 + 12 i$, with $i^{2} = - 1$ used.
> 
> **B1**: Correct value $β^{3} = 46 - 9 i$. Any valid route earns this mark.
> 
> **B1**: Correct substitution into the cubic showing that both the real part and the imaginary part are zero, with a conclusion stated. Because the result is given, the substitution must be visible.
The cubic has real coefficients, so the conjugate of $β$ is also a root

$β^{\ast} = - 2 + 3 i$

**[B1]**

These two roots give a quadratic factor with real coefficients, so multiply their linear factors together

`\left(z - (-2 - 3i)\right)\left(z - (-2 + 3i)\right) = z^{2} + 4z + (4 + 9)`

$= z^{2} + 4 z + 13$

The cubic is therefore this quadratic multiplied by the factor coming from the third root

$z^{3} - z^{2} - 7 z - 65 = ( z^{2} + 4 z + 13 ) ( z - δ )$

Comparing the constant terms gives $13 \times ( - δ ) = - 65$

$\begin{gathered} 13 \times ( - \\delta ) & = - 65 \\ \\delta = 5 \end{gathered}$

**[M1]**

$z^{3} - z^{2} - 7 z - 65 = ( z^{2} + 4 z + 13 ) ( z - 5 )$

Setting the remaining factor to zero gives the third root

$z = 5$

**[A1]**

> **[mark-scheme]**
> **B1**: Conjugate root stated as $- 2 + 3 i$. This mark is independent, and no working is required.
> 
> **M1**: A complete valid method for the third root. Accept forming the quadratic factor $z^{2} + 4 z + 13$ and then comparing coefficients or dividing the cubic by it, or using the sum or product of the three roots.
> 
> **A1**: Correct third root $z = 5$. Both remaining roots must be given for full credit. Stating the conjugate and then the answer with no supporting algebra does not earn the method mark, since no marks are given for unsupported answers.

### Q35
(i)

The coefficients of the cubic are real, so its non-real roots occur in conjugate pairs

$4 + i$

**[B1]**

(ii)

Take the two complex roots together first, since their linear factors multiply to give a quadratic with real coefficients

`\left(z - (4 - i)\right)\left(z - (4 + i)\right) = z^{2} - (4 + i)z - (4 - i)z + (4 - i)(4 + i)`

**[M1]**

The imaginary parts of the middle terms cancel, and the final product is a complex number times its conjugate

$= z^{2} - 8 z + ( 16 + 1 )$

$= z^{2} - 8 z + 17$

**[A1]**

The real root $- 2$ contributes the factor $( z + 2 )$, so multiply the two factors together

$f ( z ) = ( z + 2 ) ( z^{2} - 8 z + 17 ) = z^{3} - 8 z^{2} + 17 z + 2 z^{2} - 16 z + 34$

**[M1]**

Collect like terms and compare with $z^{3} - 6 z^{2} + c z + d$

$f ( z ) = z^{3} - 6 z^{2} + z + 34$

$c = 1 ,  d = 34$

**[A1]**

> **[mark-scheme]**
> **B1**: Other complex root stated as $4 + i$. This mark is independent, and no working is required.
> 
> **M1**: A complete valid method for the quadratic factor with zeros $4 - i$ and $4 + i$. Accept multiplying the linear factors, or using the sum and product of that pair.
> 
> **A1**: Correct quadratic factor $z^{2} - 8 z + 17$, with $i^{2} = - 1$ used so that the coefficients are real.
> 
> **M1**: Correct method for multiplying the quadratic factor by $( z + 2 )$, with all six terms attempted. Accept instead substituting $z = - 2$ into $f ( z )$ and using a second equation from one of the complex roots.
> 
> **A1**: Both values correct, $c = 1$ and $d = 34$.

### Q36
(i)

Rearrange and take the square root of both sides, keeping both signs

$z^{2} = - 13$* so *$z = \pm \sqrt{-13}$

Split the surd to isolate $\sqrt{-1}$

$z = \pm \sqrt{13} \sqrt{-1}$

**Final answer:** $z = \sqrt{13}  i$** or **$z = - \sqrt{13}  i$

**[B1]**

(ii)

This quadratic does not factorise, so use the formula for the solutions of a quadratic equation, $z = \frac{-b\pm\sqrt{b^{2}-4ac}}{2a}$, with $a = 1$, $b = - 14$ and $c = 53$

$z = \frac{-(-14)\pm\sqrt{(-14)^{2}-4(1)(53)}}{2(1)} = \frac{14\pm\sqrt{-16}}{2}$

**[M1]**

The quantity under the root is negative, so write it as a multiple of $i$

$z = \frac{14\pm\sqrt{16}\sqrt{-1}}{2} = \frac{14\pm4i}{2}$

Divide each term by $2$

**Final answer:** $z = 7 + 2 i$** or **$z = 7 - 2 i$

**[A1]**

> **[mark-scheme]**
> **B1**: Both solutions correct and exact, $\pm \sqrt{13}  i$. The answer must be left in surd form, so a decimal such as $\pm 3 . 61 i$ does not score. Only one of the two values does not score.
> 
> **M1**: A complete valid method for the second equation. Accept correct substitution into the quadratic formula, or completing the square to reach $( z - 7 )^{2} = - 4$.
> 
> **A1**: Both solutions correct, $7 + 2 i$ and $7 - 2 i$. Accept $z = 7 \pm 2 i$. A correct answer with no working scores nothing, since no marks are given for unsupported answers from a calculator.
