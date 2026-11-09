# Functions and Graphs Flashcards

_Lane: `a-level-maths-edexcel` · grade — · 22 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** What defines a function compared to a general mapping?

**Back:** It gives exactly one output for each allowed input.

**Choices:**

- It gives exactly one output for each allowed input. ✔
  - _why:_ A function assigns every input in its domain to one and only one output, although several different inputs may share the same output.
- It gives at least one output for each allowed input.
  - _why:_ Allowing several outputs for one input describes a one-to-many relation, not a function. A function must give exactly one output for each allowed input.
- It gives exactly one input for each allowed output.
  - _why:_ This reverses the defining condition and instead resembles a one-to-one requirement. A function is defined by giving exactly one output for each allowed input.
- It gives different outputs for all allowed inputs.
  - _why:_ Requiring different outputs would unnecessarily exclude many-to-one functions, such as $f(x)=x^2$. A function only requires exactly one output for each allowed input.

## Card 2 — `basic`

**Front:** Contrast the domain and range of a function.

**Back:** Domain: set of allowed inputs.Range: set of outputs produced.

**Choices:**

- Domain: set of allowed inputs.Range: set of outputs produced. ✔
  - _why:_ The domain contains the inputs for which the function is defined, while the range contains the output values actually produced from those inputs.
- Domain: set of outputs produced.Range: set of allowed inputs.
  - _why:_ This swaps the two definitions. The domain is the set of allowed inputs, whereas the range is the set of outputs the function actually produces.
- Domain: set of distinct inputs.Range: set of allowed outputs.
  - _why:_ The domain is not restricted to inputs that give distinct outputs, since many-to-one functions are valid. It contains all allowed inputs, while the range contains outputs produced.
- Domain: set of possible outputs.Range: set of excluded inputs.
  - _why:_ The range is not the set of excluded inputs; it consists of output values actually attained. The domain is the set of inputs permitted by the function.

## Card 3 — `basic`

**Front:** What is the restriction on the expression $f(x)$ for the function $\ln(f(x))$ to be valid?

**Back:** $$f(x) > 0$

**Choices:**

- $$f(x) > 0$ ✔
  - _why:_ The real natural logarithm is defined only for strictly positive arguments, so every permitted input must make $f(x)$ greater than zero.
- $$f(x) \ge 0$
  - _why:_ Including zero is the common error: $ln 0$ is undefined. The logarithm requires a strictly positive argument, so the condition is $f(x)>0$.
- $$f(x) < 0$
  - _why:_ This is the condition often associated with an unrestricted square root, not a logarithm. For $ln(f(x))$ to be real, the required condition is $f(x)>0$.
- $$f(x) \neq 0$
  - _why:_ This includes negative arguments, for which the real logarithm is undefined. The argument must be strictly positive, giving the restriction $f(x)>0$.

## Card 4 — `basic`

**Front:** Why does the expression $f(x)$ in $\frac{1}{\sqrt{f(x)}}$ require $f(x) > 0$ rather than $f(x) \ge 0$?

**Back:** The denominator cannot equal zero.

**Choices:**

- The denominator cannot equal zero. ✔
  - _why:_ If $f(x)=0$, then $sqrt{f(x)}=0$ and the fraction would involve division by zero. Therefore $f(x)$ must be strictly positive.
- The numerator cannot equal zero.
  - _why:_ A numerator may equal zero without making a fraction undefined. Here the square root is in the denominator, so $f(x)=0$ must be excluded.
- The square root cannot equal zero.
  - _why:_ A real square root may equal zero, but it cannot do so when used as a denominator. Division by zero is why $f(x)>0$ is required.
- The fraction cannot equal zero.
  - _why:_ The fraction itself is allowed to take positive or negative values where defined. The strict inequality arises because its denominator must not equal zero.

## Card 5 — `cloze`

**Front:** For the function $\arcsin x$, the maximum possible domain is $\text{[...]}$.

**Back:** For the function $\arcsin x$, the maximum possible domain is $\boxed{-1 \le x \le 1}$.

**Choices:**

- $$-1 \le x \le 1$ ✔
  - _why:_ The sine function produces values only from $-1$ to $1$, inclusive. Consequently, the real inverse sine function accepts precisely inputs satisfying $-1\le x\le1$.
- $$0 \le x \le 1$
  - _why:_ This interval omits negative sine values, even though inverse sine is defined for them. The maximum real domain is the full interval $-1\le x\le1$.
- $$-1 < x < 1$
  - _why:_ The endpoints are valid because $arcsin(-1)$ and $arcsin(1)$ both exist. The maximum domain therefore includes them: $-1\le x\le1$.
- $$-\frac{\pi}{2} \le x \le \frac{\pi}{2}$
  - _why:_ Confusing the domain with the principal range leads to an interval involving angles. The inputs to $arcsin x$ must instead satisfy $-1\le x\le1$.

## Card 6 — `basic`

**Front:** In the composite function $fg(x)$, which function is applied to $x$ first?

**Back:** $$g(x)$

**Choices:**

- $$g(x)$ ✔
  - _why:_ By convention, $fg(x)$ means $f(g(x))$. The inner function acts first, so $g(x)$ is evaluated before $f$ is applied.
- $$f(x)$
  - _why:_ Choosing $f(x)$ first reverses the order of composition. Since $fg(x)=f(g(x))$, the inner function $g(x)$ is applied to $x$ first.
- $$x$
  - _why:_ The original input is not itself one of the functions being composed. In $fg(x)=f(g(x))$, $g(x)$ is the first function applied.
- $$fg(x)$
  - _why:_ This names the entire composite rather than the function applied first. Reading $fg(x)$ as $f(g(x))$ shows that $g(x)$ acts first.

## Card 7 — `cloze`

**Front:** In general, the relationship between composite functions $fg(x)$ and $gf(x)$ is that $\text{[...]}$.

**Back:** In general, the relationship between composite functions $fg(x)$ and $gf(x)$ is that $\boxed{fg(x) \neq gf(x)}$.

**Choices:**

- $$fg(x) \neq gf(x)$ ✔
  - _why:_ Function composition is generally not commutative: applying $g$ and then $f$ usually produces a different result from applying $f$ and then $g$.
- $$fg(x) = gf(x)$
  - _why:_ This incorrectly assumes composition is commutative, as multiplication is. In general, changing the order changes the result, so $fg(x)\neq gf(x)$.
- $$fg(x) = -gf(x)$
  - _why:_ Reversing composition does not generally negate every output; the two composites can differ in many ways. The valid general statement is $fg(x)\neq gf(x)$.
- $$fg(x) = f(x) + g(x)$
  - _why:_ Composition is not the same as adding function values. Because order usually matters when functions are composed, the general relationship is $fg(x)\neq gf(x)$.

## Card 8 — `basic`

**Front:** What condition must a function $f(x)$ satisfy for an inverse function $f^{-1}(x)$ to exist?

**Back:** It must be one-to-one.

**Choices:**

- It must be one-to-one. ✔
  - _why:_ A one-to-one function assigns distinct outputs to distinct inputs, so each output identifies a unique original input and the inverse is itself a function.
- It must be many-to-one.
  - _why:_ A many-to-one function sends multiple inputs to the same output, so its inverse would assign several outputs to one input. The original function must be one-to-one.
- It must be strictly decreasing.
  - _why:_ An increasing function is one-to-one, but being decreasing is not required because increasing functions also have inverses. The essential condition is that it be one-to-one.
- It must be continuous.
  - _why:_ Continuity alone does not prevent repeated output values, as $f(x)=x^2$ demonstrates on the real numbers. An inverse function requires $f$ to be one-to-one.

## Card 9 — `cloze`

**Front:** The domain of $f^{-1}$ is the [ ___ ] of $f$, and the range of $f^{-1}$ is the domain of $f$.

**Back:** The domain of $f^{-1}$ is the range of $f$, and the range of $f^{-1}$ is the domain of $f$.

**Choices:**

- range ✔
  - _why:_ Taking an inverse swaps the input and output roles, so the allowable inputs of the inverse are exactly the original function’s outputs, namely its range.
- domain
  - _why:_ The domain belongs to the original function’s inputs, not the inverse’s inputs. Inverting swaps domain and range, so the correct term here is range.
- codomain
  - _why:_ The codomain is the declared target set and need not equal the values the function actually produces. The inverse’s domain is the original range.
- image
  - _why:_ The image can describe actual outputs, but it is not the standard term required here. The inverse’s domain is the range of the original function.

## Card 10 — `cloze`

**Front:** The domain of $f^{-1}$ is the range of $f$, and the range of $f^{-1}$ is the [ ___ ] of $f$.

**Back:** The domain of $f^{-1}$ is the range of $f$, and the range of $f^{-1}$ is the domain of $f$.

**Choices:**

- domain ✔
  - _why:_ An inverse function swaps the original inputs and outputs. Therefore, the inverse’s range consists of the original function’s allowable inputs, its domain.
- range
  - _why:_ The original range becomes the inverse’s domain, not its range. Swapping input and output sets means the correct term here is domain.
- codomain
  - _why:_ The codomain is the target set specified for the original function and may include values never reached. The inverse’s range is the original domain.
- image
  - _why:_ The image refers to values produced by a function and corresponds to the original range. The inverse’s range instead consists of the original domain.

## Card 11 — `cloze`

**Front:** The graphs of $y=f(x)$ and $y=f^{-1}(x)$ are reflections in the line $\text{[...]}$.

**Back:** The graphs of $y=f(x)$ and $y=f^{-1}(x)$ are reflections in the line $\boxed{y=x}$.

**Choices:**

- $$y=x$ ✔
  - _why:_ Interchanging the coordinates of every point on a function produces its inverse, and reflecting a point $(x,y)$ in $y=x$ gives $(y,x)$.
- $$y=-x$
  - _why:_ Reflection in $y=-x$ changes $(x,y)$ to $(-y,-x)$, introducing sign changes as well as swapping coordinates. Inverse graphs reflect in $y=x$.
- $$y=0$
  - _why:_ Reflection in the $x$-axis changes the sign of the $y$-coordinate but does not interchange input and output. Inverse graphs reflect in $y=x$.
- $$x=0$
  - _why:_ Reflection in the $y$-axis changes the sign of the $x$-coordinate but does not swap coordinates. The correct line of symmetry is $y=x$.

## Card 12 — `basic`

**Front:** How does the function $f^{-1}(x)$ differ from $[f(x)]^{-1}$?

**Back:** $f^{-1}(x)$ is the inverse function.$[f(x)]^{-1}$ is the reciprocal ($\frac{1}{f(x)}$).

**Choices:**

- $f^{-1}(x)$ is the inverse function.$[f(x)]^{-1}$ is the reciprocal ($\frac{1}{f(x)}$). ✔
  - _why:_ The inverse function reverses the mapping between inputs and outputs, whereas the reciprocal raises the function value to the power $-1$, giving $\frac{1}{f(x)}$.
- $f^{-1}(x)$ is the reciprocal ($\frac{1}{f(x)}$).$[f(x)]^{-1}$ is the inverse function.
  - _why:_ This reverses the meanings of the two notations. The inverse function swaps inputs and outputs, while the bracketed power $-1$ means the reciprocal $\frac{1}{f(x)}$.
- $f^{-1}(x)$ is the inverse function.$[f(x)]^{-1}$ is the negative function ($-f(x)$).
  - _why:_ A power of $-1$ means reciprocal, not multiplication by $-1$. The inverse function reverses the mapping, while $[f(x)]^{-1}=\frac{1}{f(x)}$.
- $f^{-1}(x)$ is the reciprocal function ($\frac{1}{f(x)}$).$[f(x)]^{-1}$ is the inverse function.
  - _why:_ This combines a notation error with a reversal of the definitions. The function inverse swaps domain and range; the bracketed expression means the reciprocal $\frac{1}{f(x)}$.

## Card 13 — `basic`

**Front:** Where does the vertex of a modulus graph $y = |f(x)|$ occur?

**Back:** Where the expression inside the modulus equals zero ($f(x) = 0$).

**Choices:**

- Where the expression inside the modulus equals zero ($f(x) = 0$). ✔
  - _why:_ The modulus changes the sign of negative values, so a corner or vertex occurs where the inside changes sign, which is where $f(x)=0$.
- Where the expression inside the modulus is at its maximum ($f(x)$ is largest).
  - _why:_ A maximum of $f(x)$ does not generally create the corner of the modulus graph. The vertex occurs where the inside expression crosses zero, so $f(x)=0$.
- Where the expression inside the modulus equals one ($f(x) = 1$).
  - _why:_ The modulus has no special turning point specifically at value one. The key point is where the expression changes from negative to positive, namely $f(x)=0$.
- Where the expression inside the modulus has a stationary point ($f'(x) = 0$).
  - _why:_ A stationary point of $f$ may remain smooth after applying the modulus and need not be a vertex. The modulus vertex occurs where $f(x)=0$.

## Card 14 — `basic`

**Front:** State the inequality equivalent to $|A| 0$).

**Back:** $$-k < A < k$

**Choices:**

- $$-k < A < k$ ✔
  - _why:_ The inequality $|A|<k$ means that $A$ is less than $k$ units from zero, placing it strictly between $-k$ and $k$.
- $$Ak$
  - _why:_ This describes values more than $k$ units from zero, which corresponds to $|A|>k$. For $|A|<k$, the correct result is $-k<A<k$.
- $$-k\leq A\leq k$
  - _why:_ The non-strict symbols incorrectly include the endpoints. Since the original inequality is strict, the equivalent result is $-k<A<k$.
- $$k<A<-k$
  - _why:_ For positive $k$, this orders the bounds incorrectly and leaves no possible values. The interval centred on zero is $-k<A<k$.

## Card 15 — `basic`

**Front:** Describe the transformation $y = f(x + a)$.

**Back:** A horizontal shift left by $a$ units.

**Choices:**

- A horizontal shift left by $a$ units. ✔
  - _why:_ Replacing $x$ with $x+a$ means the same output is reached at an input $a$ smaller than before, shifting the graph horizontally left by $a$ units.
- A horizontal shift right by $a$ units.
  - _why:_ A rightward shift is produced by $f(x-a)$, not $f(x+a)$. The positive sign inside the function shifts the graph left by $a$ units.
- A vertical shift up by $a$ units.
  - _why:_ Adding $a$ outside the function, as in $f(x)+a$, produces a vertical shift. Changing the input to $x+a$ causes a horizontal shift left.
- A vertical stretch with scale factor $a$.
  - _why:_ Multiplying the function output by $a$, as in $af(x)$, creates a vertical stretch. Altering the input to $x+a$ shifts the graph left.

## Card 16 — `cloze`

**Front:** The transformation $y = cf(x)$ is a [ ___ ] with scale factor $c$.

**Back:** The transformation $y = cf(x)$ is a vertical stretch with scale factor $c$.

**Choices:**

- vertical stretch ✔
  - _why:_ Multiplying every output by $c$ changes the graph’s vertical coordinates while leaving $x$ unchanged, giving a vertical stretch with scale factor $c$.
- horizontal stretch
  - _why:_ A horizontal stretch is produced by replacing $x$ with $\frac{x}{c}$, as in $f\left(\frac{x}{c}\right)$. Multiplying the output gives a vertical stretch.
- vertical translation
  - _why:_ A vertical translation adds a constant outside the function, such as $f(x)+c$. Multiplication by $c$ scales the vertical coordinates instead.
- horizontal translation
  - _why:_ A horizontal translation changes the input, using forms such as $f(x+c)$. Multiplying the function value affects vertical scale, not horizontal position.

## Card 17 — `cloze`

**Front:** The transformation $y = cf(x)$ is a vertical stretch with scale factor $\text{[...]}$.

**Back:** The transformation $y = cf(x)$ is a vertical stretch with scale factor $\boxed{c}$.

**Choices:**

- $$c$ ✔
  - _why:_ Multiplying $f(x)$ by $c$ multiplies every y-coordinate by $c$, producing a vertical stretch with scale factor $c$.
- $$\frac{1}{c}$
  - _why:_ The reciprocal scale factor applies to the horizontal transformation $f(cx)$, not the vertical transformation $cf(x)$. Here every y-coordinate is multiplied by $c$, so the scale factor is $c$.
- $$c^2$
  - _why:_ Squaring the multiplier would incorrectly apply the vertical scaling twice. Since the function values are multiplied once by $c$, the vertical scale factor is $c$.
- $$-c$
  - _why:_ A negative multiplier would introduce a reflection in the x-axis as well as changing vertical scale. The stated multiplier is $c$, so the required scale factor is $c$.

## Card 18 — `basic`

**Front:** Describe the transformation $y = f(cx)$.

**Back:** A horizontal stretch with scale factor $\frac{1}{c}$.

**Choices:**

- A horizontal stretch with scale factor $\frac{1}{c}$. ✔
  - _why:_ Multiplying the input by $c$ means each original x-coordinate must be divided by $c$. Therefore the graph undergoes a horizontal stretch with scale factor $\frac{1}{c}$.
- A horizontal stretch with scale factor $c$.
  - _why:_ Using $c$ directly as the horizontal scale factor overlooks the inverse effect of transformations inside a function. For $f(cx)$, x-coordinates are divided by $c$, giving scale factor $\frac{1}{c}$.
- A vertical stretch with scale factor $c$.
  - _why:_ A vertical stretch with scale factor $c$ is produced by $y=cf(x)$, where the output is multiplied. Multiplying the input instead creates a horizontal stretch with scale factor $\frac{1}{c}$.
- A vertical stretch with scale factor $\frac{1}{c}$.
  - _why:_ The reciprocal is correct only as a horizontal scale factor. The transformation changes x-coordinates rather than y-coordinates, so it is a horizontal stretch with scale factor $\frac{1}{c}$.

## Card 19 — `basic`

**Front:** How is the graph $y = |f(x)|$ formed from $y = f(x)$?

**Back:** Reflect all parts of the graph below the x-axis upwards into the positive y-region.

**Choices:**

- Reflect all parts of the graph below the x-axis upwards into the positive y-region. ✔
  - _why:_ Taking the absolute value leaves non-negative function values unchanged and changes negative values to positive ones. Thus only the portions below the x-axis are reflected upwards.
- Reflect all parts of the graph above the x-axis downwards into the negative y-region.
  - _why:_ Reflecting the part above the x-axis would produce non-positive outputs, corresponding to $-|f(x)|$. For $|f(x)|$, the parts below the x-axis are reflected upwards.
- Reflect all parts of the graph left of the y-axis rightwards into the positive x-region.
  - _why:_ This confuses an absolute value applied to the output with one applied to the input. For $|f(x)|$, negative y-values are reflected in the x-axis, not across the y-axis.
- Reflect all parts of the graph in the x-axis downwards into the opposite y-region.
  - _why:_ Reflecting the entire graph would give $y=-f(x)$ rather than $y=|f(x)|$. Non-negative parts remain fixed, while only parts below the x-axis are reflected upwards.

## Card 20 — `basic`

**Front:** How is the graph $y = f(|x|)$ formed from $y = f(x)$?

**Back:** Discard the left side ($x < 0$) and reflect the right side ($x \ge 0$) in the y-axis.

**Choices:**

- Discard the left side ($x < 0$) and reflect the right side ($x \ge 0$) in the y-axis. ✔
  - _why:_ The absolute value makes the inputs $x$ and $-x$ produce the same output. The right-hand half is therefore retained and mirrored across the y-axis.
- Discard the right side ($x > 0$) and reflect the left side ($x \le 0$) in the y-axis.
  - _why:_ This reverses which half determines the transformed graph. Since $|x|$ is always non-negative, $f(|x|)$ uses the original right side and reflects it into the left side.
- Discard the left side ($x < 0$) and reflect the right side ($x \ge 0$) in the x-axis.
  - _why:_ The graph must be mirrored in the y-axis because the absolute value affects the input, or x-coordinate. Reflection in the x-axis instead changes output signs and does not produce $f(|x|)$.
- Discard the lower side ($y < 0$) and reflect the upper side ($y \ge 0$) in the x-axis.
  - _why:_ This describes the effect of $|f(x)|$, where negative outputs are reflected upwards. For $f(|x|)$, the right side is reflected in the y-axis after the left side is discarded.

## Card 21 — `basic`

**Front:** A point $(6, -2)$ is on $y=f(x)$. Find its coordinates on $y=3f(2x)$.

**Back:** $$(3, -6)$

**Choices:**

- $$(3, -6)$ ✔
  - _why:_ In $f(2x)$, set $2x=6$, giving $x=3$. The outer factor $3$ multiplies the original y-coordinate, giving $3(-2)=-6$, so the point is $(3,-6)$.
- $$(12, -6)$
  - _why:_ Multiplying the original x-coordinate by $2$ ignores the inverse effect of an input transformation. The new x-coordinate is $6\div2=3$, while the y-coordinate becomes $3(-2)=-6$.
- $$(3, -\frac{2}{3})$
  - _why:_ The horizontal coordinate is correctly divided by $2$, but the output has been divided by $3$ instead of multiplied. The factor outside the function gives $3(-2)=-6$, so the point is $(3,-6)$.
- $$(12, -\frac{2}{3})$
  - _why:_ Both transformations have been applied in the wrong directions. The input factor halves the x-coordinate to $3$, while the output factor triples the y-coordinate to $-6$.

## Card 22 — `basic`

**Front:** Find the range of $f(x) = (x-2)^2 + 2$ for $x \in \mathbb{R}$.

**Back:** $$f(x) \ge 2$

**Choices:**

- $$f(x) \ge 2$ ✔
  - _why:_ The squared term $(x-2)^2$ is always non-negative and equals zero when $x=2$. Hence the minimum value of $f(x)$ is $2$, so $f(x)\ge 2$.
- $$f(x) \le 2$
  - _why:_ This reverses the inequality and treats the vertex as a maximum. The parabola opens upwards, so $2$ is its minimum value and the range is $f(x)\ge 2$.
- $$f(x) \ge -2$
  - _why:_ The sign inside $(x-2)^2$ shifts the graph horizontally and does not make the minimum output negative. The vertex is $(2,2)$, so the range is $f(x)\ge 2$.
- $$f(x) > 2$
  - _why:_ A strict inequality wrongly excludes the minimum value. At $x=2$, the function equals exactly $2$, so the endpoint is included and the range is $f(x)\ge 2$.
