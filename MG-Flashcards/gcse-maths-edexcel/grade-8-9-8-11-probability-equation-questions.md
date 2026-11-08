# Probability Equation Questions Flashcards

_Lane: `gcse-maths-edexcel` · grade 8 · 16 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** Why do we multiply probabilities when a question asks for "both counters are blue"?

**Back:** Because the outcome requires the first counter is blue and the second counter is blue.

**Choices:**

- Because the outcome requires the first counter is blue and the second counter is blue. ✔
  - _why:_ Multiplication finds the probability of two events occurring together. The word “and” means both the first and second counter must be blue, so their probabilities are multiplied.
- Because the outcome requires the first counter is blue or the second counter is blue.
  - _why:_ Treating “both” as “or” confuses a joint event with alternative events. Both picks must be blue, so the first-blue and second-blue probabilities are multiplied.
- Because the outcome requires the first counter is blue minus the second counter is blue.
  - _why:_ Subtracting probabilities does not calculate two successive events both occurring. The requirement is first blue and second blue, so the relevant probabilities must be multiplied.
- Because the outcome requires the first counter is blue added to the second counter is blue.
  - _why:_ Adding is associated with mutually exclusive alternative outcomes, not two outcomes occurring together. Since both counters must be blue, multiply the probabilities for the two picks.

## Card 2 — `basic`

**Front:** In "with replacement" problems, how does the total number of counters change for the second pick?

**Back:** It stays the same (the counter is put back).

**Choices:**

- It stays the same (the counter is put back). ✔
  - _why:_ Replacement returns the selected counter to the bag before the second pick. Therefore, the second pick is made from the same total number of counters as the first.
- It becomes one less (the counter is kept out).
  - _why:_ Reducing the total by one describes sampling without replacement. With replacement, the selected counter is returned, so the total stays the same for the second pick.
- It becomes one more (another counter is put in).
  - _why:_ Replacement means returning the counter that was selected, not adding an extra counter. Consequently, the total remains the same rather than increasing by one.
- It becomes twice as large (the counters are doubled).
  - _why:_ Replacement does not duplicate the counters; it simply returns the selected one. The total number available for the second pick is therefore unchanged.

## Card 3 — `basic`

**Front:** If a bag has $x$ counters and one is taken without replacement, what is the new total for the second pick?

**Back:** $$x - 1$

**Choices:**

- $$x - 1$ ✔
  - _why:_ Without replacement, the selected counter remains outside the bag. Starting with $x$ counters therefore leaves $x - 1$ counters available for the second pick.
- $$x + 1$
  - _why:_ Adding one reverses the effect of removing a counter and would incorrectly increase the total. Without replacement, one counter is removed, leaving $x - 1$.
- $$x$
  - _why:_ Keeping the total at $x$ assumes that the selected counter was replaced. Since it is not returned, the total for the second pick is $x - 1$.
- $$2x$
  - _why:_ Doubling the original total has no connection to taking one counter from the bag. Without replacement, exactly one is removed, so the new total is $x - 1$.

## Card 4 — `basic`

**Front:** A bag has 3 red and $x$ blue counters. What is the probability that the first pick is blue?

**Back:** $$\frac{x}{x+3}$

**Choices:**

- $$\frac{x}{x+3}$ ✔
  - _why:_ There are $x$ blue counters out of $x+3$ counters altogether. Probability is favourable outcomes divided by total outcomes, giving $\frac{x}{x+3}$.
- $$\frac{3}{x+3}$
  - _why:_ Using 3 as the numerator calculates the probability of selecting a red counter. For blue, there are $x$ favourable counters out of $x+3$, giving $\frac{x}{x+3}$.
- $$\frac{x}{3}$
  - _why:_ The denominator must be the total number of counters, not the number of red counters. The total is $x+3$, so the blue probability is $\frac{x}{x+3}$.
- $$\frac{x+3}{x}$
  - _why:_ This reverses favourable outcomes and total outcomes, producing a value greater than 1 when $x$ is positive. The correct probability is $\frac{x}{x+3}$.

## Card 5 — `basic`

**Front:** A bag has 3 red and $x$ blue counters. If the first pick was blue and not replaced, what is the probability the second pick is blue?

**Back:** $$\frac{x-1}{x+2}$

**Choices:**

- $$\frac{x-1}{x+2}$ ✔
  - _why:_ After one blue counter is removed, $x-1$ blue counters remain. The total also falls from $x+3$ to $x+2$, so the probability is $\frac{x-1}{x+2}$.
- $$\frac{x}{x+3}$
  - _why:_ This incorrectly uses the original numbers as though the first counter were replaced. Without replacement, both the blue count and total decrease by one, giving $\frac{x-1}{x+2}$.
- $$\frac{x-1}{x+3}$
  - _why:_ Only reducing the blue numerator overlooks that the total number of counters also decreases. After the first blue pick, the correct denominator is $x+2$, giving $\frac{x-1}{x+2}$.
- $$\frac{x}{x+2}$
  - _why:_ Only reducing the denominator overlooks that one blue counter has been removed. The remaining blue count is $x-1$, so the correct probability is $\frac{x-1}{x+2}$.

## Card 6 — `basic`

**Front:** If the ratio of red to blue counters is $3:1$, how should you represent the counts algebraically using a multiplier $k$?

**Back:** Red: $3k$Blue: $k$

**Choices:**

- Red: $3k$Blue: $k$ ✔
  - _why:_ A $3:1$ ratio means the red count has three equal parts and the blue count has one. Multiplying each part by $k$ gives $3k$ red and $k$ blue.
- Red: $k$Blue: $3k$
  - _why:_ This reverses the order of the ratio and represents red to blue as $1:3$. For a $3:1$ ratio, the counts must be $3k$ red and $k$ blue.
- Red: $3+k$Blue: $1+k$
  - _why:_ Adding the same number does not generally preserve a $3:1$ ratio. Ratio parts must be scaled by a common multiplier, producing $3k$ red and $k$ blue.
- Red: $4k$Blue: $k$
  - _why:_ Using $4k$ for red confuses the total number of ratio parts with the red count. Red has three parts, so the counts are $3k$ red and $k$ blue.

## Card 7 — `basic`

**Front:** If the ratio of red to blue counters is $3:1$, what is the algebraic expression for the total number of counters?

**Back:** $$4k$

**Choices:**

- $$4k$ ✔
  - _why:_ The ratio contains three red parts and one blue part, making four equal parts altogether. Each part represents $k$ counters, so the total is $4k$.
- $$3k$
  - _why:_ This counts only the three red parts and omits the one blue part. Adding all ratio parts gives $3k+k=4k$ counters in total.
- $$k$
  - _why:_ This represents only one ratio part rather than the complete collection. The $3:1$ ratio contains four parts altogether, so the total is $4k$.
- $$3k^2$
  - _why:_ Multiplying the red and blue expressions creates $3k^2$, but totals are found by addition. Adding $3k$ and $k$ gives a total of $4k$.

## Card 8 — `basic`

**Front:** Why must you always use the positive square root when solving for numbers of counters or probabilities?

**Back:** The number of counters and probabilities cannot be negative.

**Choices:**

- The number of counters and probabilities cannot be negative. ✔
  - _why:_ Counter totals represent physical quantities, while probabilities lie between 0 and 1. A negative root is therefore invalid in this context, leaving only the positive square root.
- The number of counters and probabilities cannot be positive.
  - _why:_ This reverses the relevant restriction: valid counter totals are non-negative, and probabilities range from 0 to 1. Therefore, the positive root is used and the negative root rejected.
- The number of counters and probabilities must be negative.
  - _why:_ Negative values cannot represent a number of counters or a probability. When an equation produces positive and negative roots, only the positive root is meaningful in this setting.
- The number of counters and probabilities can have either sign.
  - _why:_ Although algebraic equations may have roots with either sign, the context restricts possible solutions. Counts and probabilities cannot be negative, so only the positive root is accepted.

## Card 9 — `basic`

**Front:** A quadratic for total counters $n$ gives $n = 21$ and $n = 4$. If there are 6 red counters in the bag, why is $n = 4$ rejected?

**Back:** The total number of counters cannot be less than the number of red counters already known to be inside.

**Choices:**

- The total number of counters cannot be less than the number of red counters already known to be inside. ✔
  - _why:_ There are already 6 red counters, so the bag must contain at least 6 counters altogether. Since 4 is less than 6, that root is impossible.
- The total number of counters cannot be greater than the number of red counters already known to be inside.
  - _why:_ This reverses the required inequality: the total can exceed the number of red counters. The root 4 is rejected because the total cannot be less than the 6 red counters.
- The total number of counters cannot be equal to the number of red counters already known to be inside.
  - _why:_ A bag could contain only red counters, so equality is possible in principle. Here, 4 is rejected because it is less than the 6 red counters already present.
- The total number of counters cannot be double the number of red counters already known to be inside.
  - _why:_ There is no rule preventing the total from being twice the red count. The relevant restriction is that the total cannot be below the 6 known red counters.

## Card 10 — `basic`

**Front:** In a ratio of red:blue = $3:2$, what is the initial probability of picking a blue counter?

**Back:** $$\frac{2k}{5k}$ (which simplifies to $\frac{2}{5}$)

**Choices:**

- $$\frac{2k}{5k}$ (which simplifies to $\frac{2}{5}$) ✔
  - _why:_ The ratio gives $3k$ red and $2k$ blue counters, making $5k$ counters altogether. Therefore, the probability of blue is $\frac{2k}{5k}=\frac{2}{5}$.
- $$\frac{3k}{5k}$ (which simplifies to $\frac{3}{5}$)
  - _why:_ This uses the red part of the ratio as the numerator, so it gives the probability of red. Blue accounts for $2k$ of the $5k$ counters, giving $\frac{2}{5}$.
- $$\frac{2k}{3k}$ (which simplifies to $\frac{2}{3}$)
  - _why:_ This divides the number of blue counters by the number of red counters rather than by the total. Probability requires $2k$ over $5k$, giving $\frac{2}{5}$.
- $$\frac{2k}{7k}$ (which simplifies to $\frac{2}{7}$)
  - _why:_ This incorrectly multiplies or combines the ratio parts to produce a total of $7k$. The actual total is $3k+2k=5k$, so the probability is $\frac{2}{5}$.

## Card 11 — `basic`

**Front:** In a ratio of red:blue = $3:2$, if one blue counter is removed, what is the probability the second counter is blue?

**Back:** $$\frac{2k-1}{5k-1}$

**Choices:**

- $$\frac{2k-1}{5k-1}$ ✔
  - _why:_ Removing one blue counter leaves $2k-1$ blue counters and reduces the total from $5k$ to $5k-1$. Their ratio gives the second-counter probability.
- $$\frac{2k}{5k-1}$
  - _why:_ This reduces the total but forgets that the removed counter was blue. Both the blue count and total decrease by 1, so the probability is $\frac{2k-1}{5k-1}$.
- $$\frac{2k-1}{5k}$
  - _why:_ This reduces the blue count but incorrectly keeps the original total. Without replacement, one counter has left the bag, so the denominator must also become $5k-1$.
- $$\frac{3k}{5k-1}$
  - _why:_ This uses the number of red counters as the numerator, confusing the requested colour. After one blue is removed, the blue probability is $\frac{2k-1}{5k-1}$.

## Card 12 — `basic`

**Front:** A bag has $n$ counters. 6 are red and the rest are blue. What is the algebraic expression for the number of blue counters?

**Back:** $$n - 6$

**Choices:**

- $$n - 6$ ✔
  - _why:_ The total $n$ consists of 6 red counters plus the blue counters. Subtracting the 6 red counters from the total leaves $n-6$ blue counters.
- $$n + 6$
  - _why:_ Adding 6 counts the red counters on top of a total that already includes them. The number of blue counters is found by subtracting: $n-6$.
- $$6 - n$
  - _why:_ This subtraction is reversed and would be negative whenever the bag contains more than 6 counters. Blue counters equal the total minus the red counters, so the expression is $n-6$.
- $$\frac{n}{6}$
  - _why:_ Dividing by 6 would only be relevant if the counters were split into six equal groups. Here, remove the 6 red counters from the total, giving $n-6$.

## Card 13 — `basic`

**Front:** In a "show that" question involving a quadratic, what should be your first line of working?

**Back:** The probability equation (the product of two fractions equal to the given probability).

**Choices:**

- The probability equation (the product of two fractions equal to the given probability). ✔
  - _why:_ Writing the probability equation first connects the information in the question to the required quadratic. The two event probabilities are multiplied and set equal to the stated probability.
- The expanded quadratic (the brackets multiplied out and all terms collected together).
  - _why:_ Expansion comes only after the probability relationship has been formed and denominators have been removed. The first line should be the product of the two probability fractions.
- The factorised quadratic (the two linear factors equal to the given probability).
  - _why:_ Factorisation is a later algebraic step and may not involve the given probability directly. Start by multiplying the two event probabilities and equating the product to the stated probability.
- The quadratic formula (the coefficients substituted directly into the standard formula).
  - _why:_ The quadratic formula cannot be used until a quadratic equation has been derived. The first line must state the probability equation from which that quadratic follows.

## Card 14 — `basic`

**Front:** When solving $\frac{x}{x+3} \times \frac{x-1}{x+2} = \frac{5}{14}$, what is the standard method to remove the fractions?

**Back:** Cross-multiply the numerators and denominators.

**Choices:**

- Cross-multiply the numerators and denominators. ✔
  - _why:_ Treating the left side as one fraction gives $\frac{x(x-1)}{(x+3)(x+2)}=\frac{5}{14}$. Cross-multiplication removes the denominators, producing $14x(x-1)=5(x+3)(x+2)$.
- Cross-add the numerators and denominators.
  - _why:_ Cross-addition is not a valid operation for solving an equation of two fractions. Cross-multiplication clears the denominators and gives $14x(x-1)=5(x+3)(x+2)$.
- Cancel the matching terms in the numerators and denominators.
  - _why:_ Terms cannot be cancelled across addition, so $x$ cannot cancel with $x+3$ or $x+2$. Cross-multiplication is needed to remove the fractional denominators correctly.
- Add the two denominators and then simplify.
  - _why:_ Adding denominators is not a valid way to multiply fractions or preserve the equation. Combine each side as a fraction, then cross-multiply to clear the denominators.

## Card 15 — `basic`

**Front:** A bag has $y$ blue and 6 red counters. Without replacement, what is the probability of picking blue then red?

**Back:** $$\frac{y}{y+6} \times \frac{6}{y+5}$

**Choices:**

- $$\frac{y}{y+6} \times \frac{6}{y+5}$ ✔
  - _why:_ Initially, $y$ of the $y+6$ counters are blue. After one blue is removed, 6 red counters remain among $y+5$ total counters, so the probabilities multiply.
- $$\frac{y}{y+6} \times \frac{6}{y+6}$
  - _why:_ This keeps the original total for the second pick, as though the first counter were replaced. Without replacement, the second denominator decreases to $y+5$.
- $$\frac{6}{y+6} \times \frac{y}{y+5}$
  - _why:_ This calculates red then blue by reversing the requested order. For blue then red, the first numerator is $y$ and the second is 6.
- $$\frac{y}{y+6} \times \frac{5}{y+5}$
  - _why:_ The first counter removed was blue, so the number of red counters remains 6 rather than decreasing to 5. The second fraction must therefore be $\frac{6}{y+5}$.

## Card 16 — `basic`

**Front:** Why does the denominator decrease in "without replacement" probability even if a different colour is picked second?

**Back:** The total number of counters in the bag has decreased by 1.

**Choices:**

- The total number of counters in the bag has decreased by 1. ✔
  - _why:_ Without replacement, the first counter remains outside the bag. Therefore, one fewer counter is available for the second pick, regardless of which colour is required next.
- The chosen colour of counters in the bag has decreased by 1.
  - _why:_ Only the colour selected first decreases, which may differ from the colour wanted second. The denominator represents all counters, so it decreases because the total has fallen by 1.
- The number of colours represented in the bag has decreased by 1.
  - _why:_ Removing one counter does not usually remove an entire colour category from the bag. The denominator decreases because there is one fewer counter in total, not one fewer colour.
- The second probability must always be smaller than the first.
  - _why:_ A second probability can be larger or smaller depending on the composition of the bag. The denominator decreases specifically because one counter has been removed from the total.
