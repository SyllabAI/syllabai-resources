# Sequences and Series Flashcards

_Lane: `a-level-maths-edexcel` · grade — · 20 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** In sigma notation $\sum_{r=k}^{n} f(r)$, how is the total number of terms calculated?

**Back:** $$n - k + 1$

**Choices:**

- $$n - k + 1$ ✔
  - _why:_ The summation includes every integer from $k$ through $n$, inclusive. Counting these values gives $n-k$ intervals, and adding one endpoint produces $n-k+1$ terms.
- $$n - k$
  - _why:_ This counts the intervals between $k$ and $n$, but not both endpoints as terms. Including the starting value gives the correct total, $n-k+1$.
- $$n - k + 2$
  - _why:_ This adds two to the interval count instead of one, overcounting the terms by one. Since both $k$ and $n$ are included, the correct total is $n-k+1$.
- $$n + k + 1$
  - _why:_ The starting index must be subtracted because the count measures the distance from $k$ to $n$. Including both endpoints gives $n-k+1$, not a sum of the indices.

## Card 2 — `basic`

**Front:** What is the difference between a sequence and a series?

**Back:** A sequence is an ordered list of terms.A series is the sum of terms in a sequence.

**Choices:**

- A sequence is an ordered list of terms.A series is the sum of terms in a sequence. ✔
  - _why:_ A sequence lists terms in a particular order, whereas a series is formed by adding the terms of a sequence. The distinction is between listing and summing.
- A sequence is the sum of terms.A series is an ordered list of terms.
  - _why:_ These definitions reverse the two concepts. A sequence is the ordered list, while a series is the sum formed from the terms in that sequence.
- A sequence has a constant difference.A series has a constant ratio.
  - _why:_ Constant differences and ratios describe particular types of sequences, not the general definitions. A sequence is an ordered list, while a series is the sum of its terms.
- A sequence is an unordered set of terms.A series is the final term in a sequence.
  - _why:_ Order matters in a sequence, and a series is not a single final term. The correct distinction is an ordered list versus the sum of its terms.

## Card 3 — `cloze`

**Front:** The $n$th term of an arithmetic sequence is given by the formula $u_n = \text{[...]}$.

**Back:** The $n$th term of an arithmetic sequence is given by the formula $u_n = \boxed{a + (n-1)d}$.

**Choices:**

- $$a + (n-1)d$ ✔
  - _why:_ An arithmetic sequence starts at $a$ and changes by $d$ each time. The $n$th term is reached after $n-1$ changes, giving $u_n=a+(n-1)d$.
- $$a + nd$
  - _why:_ Using $nd$ applies the common difference $n$ times, but the first term already equals $a$. Only $n-1$ changes are needed, so the correct formula is $a+(n-1)d$.
- $$a + (n+1)d$
  - _why:_ This applies two more changes than the first term requires, shifting the term number incorrectly. The $n$th term uses exactly $n-1$ differences: $a+(n-1)d$.
- $$ad^{n-1}$
  - _why:_ This is a geometric-style expression involving multiplication and powers, not the repeated addition used in an arithmetic sequence. The correct formula is $a+(n-1)d$.

## Card 4 — `basic`

**Front:** Briefly describe the method used to derive the arithmetic sum formula $S_n$.

**Back:** Write the sum forwards and backwards, then add the two equations together to get $n$ identical pairs.

**Choices:**

- Write the sum forwards and backwards, then add the two equations together to get $n$ identical pairs. ✔
  - _why:_ Writing the arithmetic sum in both orders makes corresponding terms add to the same first-plus-last value. There are $n$ identical pairs, which leads directly to the formula for $S_n$.
- Write the sum forwards twice, then multiply each term by $n$ to get $n$ identical pairs.
  - _why:_ Repeating the sum forwards does not create matching first-and-last pairs. Reversing one copy is essential, so corresponding terms become identical and the correct method uses forwards and backwards sums.
- Write the sum backwards and forwards, then subtract the two equations to leave $n$ identical pairs.
  - _why:_ Adding the two orders creates identical pairs; subtracting them causes corresponding terms to cancel or produce differences. The arithmetic sum method therefore adds, rather than subtracts, the equations.
- Pair the first and last terms, then divide their sum by $n$ to obtain $S_n$.
  - _why:_ Pairing the first and last terms is part of the idea, but dividing by $n$ is incorrect and does not form the derivation. The method writes both orders and adds them.

## Card 5 — `cloze`

**Front:** The sum of the first $n$ terms of an arithmetic series is $S_n = \text{[...]}$.

**Back:** The sum of the first $n$ terms of an arithmetic series is $S_n = \boxed{\frac{n}{2}(2a + (n-1)d)}$.

**Choices:**

- $$rac{n}{2}(2a + (n-1)d)$ ✔
  - _why:_ The first and $n$th terms are $a$ and $a+(n-1)d$. Using $S_n=rac n2(a+l)$ and substituting the final term gives this expression.
- $$rac{n}{2}(2a + nd)$
  - _why:_ The common difference is applied $n$ times instead of $n-1$ times, as though the first term required a step. The correct expression is $rac n2(2a+(n-1)d)$.
- $$n(2a + (n-1)d)$
  - _why:_ This omits the factor of $rac12$, which is needed because the sum is the number of terms multiplied by the average of the first and last terms.
- $$rac{n}{2}(a + (n-1)d)$
  - _why:_ The initial term has been included only once instead of contributing through $a+l=2a+(n-1)d$. The correct formula is $rac n2(2a+(n-1)d)$.

## Card 6 — `basic`

**Front:** In an arithmetic series where $d < 0$, when is the running total $S_n$ at its maximum?

**Back:** Just after the last positive term is added (before terms become negative).

**Choices:**

- Just after the last positive term is added (before terms become negative). ✔
  - _why:_ With $d<0$, terms decrease. Adding positive terms increases the running total, while adding negative terms decreases it, so the maximum occurs immediately after the last positive term.
- Just after the first positive term is added (before further terms are included).
  - _why:_ Later positive terms continue to increase the total, so stopping after the first positive term is too early. The maximum occurs just after the last positive term, before negative terms reduce it.
- Just after the first negative term is added (when the sequence starts decreasing).
  - _why:_ The terms decrease throughout when $d<0$, but the total only starts falling once negative terms are added. Therefore the maximum is just before this, after the last positive term.
- Just after the last non-zero term is added (when the sequence reaches zero).
  - _why:_ A zero term does not change the running total, and negative terms added afterwards lower it. The maximum is reached earlier, immediately after the last positive term.

## Card 7 — `cloze`

**Front:** The $n$th term of a geometric sequence is given by the formula $u_n = \text{[...]}$.

**Back:** The $n$th term of a geometric sequence is given by the formula $u_n = \boxed{ar^{n-1}}$.

**Choices:**

- $$ar^{n-1}$ ✔
  - _why:_ A geometric sequence starts at $a$ and multiplies by $r$ for each successive step. Reaching the $n$th term requires $n-1$ multiplications, giving $u_n=ar^{n-1}$.
- $$ar^n$
  - _why:_ This applies the common ratio $n$ times, but the first term already contains no multiplication by $r$. The $n$th term requires $n-1$ multiplications, so it is $ar^{n-1}$.
- $$a+(n-1)r$
  - _why:_ This adds a fixed amount each time, describing an arithmetic sequence rather than a geometric one. Geometric terms are multiplied by $r$, giving $ar^{n-1}$.
- $$(ar)^{n-1}$
  - _why:_ This raises the initial term $a$ to a power as well as applying the ratio, changing the first term unless $n=2$. Only the ratio is repeated, so the formula is $ar^{n-1}$.

## Card 8 — `cloze`

**Front:** The sum of the first $n$ terms of a geometric series is $S_n = \text{[...]}$.

**Back:** The sum of the first $n$ terms of a geometric series is $S_n = \boxed{\frac{a(1-r^n)}{1-r}}$.

**Choices:**

- $$rac{a(1-r^n)}{1-r}$ ✔
  - _why:_ Multiplying the finite geometric sum by $r$ and subtracting makes intermediate terms cancel. Solving the resulting equation gives $S_n=rac{a(1-r^n)}{1-r}$ for $r
e1$.
- $$rac{a(1-r^{n-1})}{1-r}$
  - _why:_ The exponent should reflect the final power appearing after multiplying the sum by $r$, which is $r^n$. Using $n-1$ omits one factor and gives the wrong number of terms.
- $$rac{a(r^n-1)}{1-r}$
  - _why:_ Reversing the numerator sign without also reversing the denominator changes the sign of the result. The consistent form is $rac{a(1-r^n)}{1-r}$.
- $$rac{a(1-r^n)}{1+r}$
  - _why:_ The denominator comes from subtracting the original sum from its ratio-multiplied version, producing $1-r$, not $1+r$. Thus the correct formula is $rac{a(1-r^n)}{1-r}$.

## Card 9 — `basic`

**Front:** What condition must the common ratio $r$ satisfy for a geometric series to have a sum to infinity?

**Back:** $$|r| < 1$ (or $-1 < r < 1$)

**Choices:**

- $$|r| < 1$ (or $-1 < r < 1$) ✔
  - _why:_ A geometric series converges only when the magnitude of its common ratio is less than 1, because its successive terms then tend towards zero.
- $$|r| \leq 1$ (or $-1 \leq r \leq 1$)
  - _why:_ Including $r=1$ or $r=-1$ allows terms that remain constant or alternate without decreasing. Convergence requires the strict condition $|r|<1$.
- $$|r| > 1$ (or $r 1$)
  - _why:_ A ratio with magnitude greater than 1 makes successive terms grow rather than approach zero. A geometric series has a sum to infinity only when $|r|<1$.
- $$0 < r < 1$
  - _why:_ Although positive ratios below 1 converge, this excludes convergent negative ratios such as $r=-0.5$. The complete condition is $|r|<1$, or $-1<r<1$.

## Card 10 — `cloze`

**Front:** The sum to infinity of a convergent geometric series is $S_\infty = \text{[...]}$.

**Back:** The sum to infinity of a convergent geometric series is $S_\infty = \boxed{\frac{a}{1-r}}$.

**Choices:**

- $$\frac{a}{1-r}$ ✔
  - _why:_ For first term $a$ and common ratio $r$ satisfying $|r|<1$, the limiting value of the geometric partial sums is $\frac{a}{1-r}$.
- $$\frac{a}{1+r}$
  - _why:_ Adding $r$ in the denominator is a sign error in the geometric-series formula. For a convergent series, the sum to infinity is $\frac{a}{1-r}$.
- $$\frac{ar}{1-r}$
  - _why:_ Multiplying the numerator by $r$ incorrectly omits the first term $a$ and instead starts from $ar$. The required sum is $\frac{a}{1-r}$.
- $$\frac{1}{1-r}$
  - _why:_ This treats the first term as 1 and therefore loses the factor $a$. A series beginning with $a$ has sum to infinity $\frac{a}{1-r}$.

## Card 11 — `basic`

**Front:** In a modelling question, what common ratio ($r$) represents a 15% decrease?

**Back:** $$r = 0.85$

**Choices:**

- $$r = 0.85$ ✔
  - _why:_ A 15% decrease leaves $100\%-15\%=85\%$ of the previous value. Converting 85% to a multiplier gives the common ratio $r=0.85$.
- $$r = 0.15$
  - _why:_ Using 0.15 gives the proportion removed rather than the proportion remaining. A 15% decrease retains 85%, so the common ratio is $r=0.85$.
- $$r = 1.15$
  - _why:_ Adding 0.15 to 1 models a 15% increase, not a decrease. Subtracting it from 1 gives the correct common ratio $r=0.85$.
- $$r = 0.985$
  - _why:_ Subtracting 15% as though it were 1.5% creates a decimal-place error. The multiplier for a 15% decrease is $1-0.15=0.85$.

## Card 12 — `basic`

**Front:** In a modelling question, what common ratio ($r$) represents a 4% increase?

**Back:** $$r = 1.04$

**Choices:**

- $$r = 1.04$ ✔
  - _why:_ A 4% increase produces $100\%+4\%=104\%$ of the previous value. Expressing 104% as a decimal multiplier gives the common ratio $r=1.04$.
- $$r = 0.96$
  - _why:_ Subtracting 0.04 from 1 models a 4% decrease rather than an increase. For an increase, add 0.04 to obtain $r=1.04$.
- $$r = 1.4$
  - _why:_ Writing 4% as 0.4 is a place-value error that models a 40% increase. Since $4\%=0.04$, the correct multiplier is $r=1.04$.
- $$r = 1.004$
  - _why:_ Writing 4% as 0.004 is a decimal-place error that models only a 0.4% increase. The correct common ratio is $1+0.04=1.04$.

## Card 13 — `basic`

**Front:** How is a recurrence relation defined?

**Back:** A rule that defines a term using earlier terms (e.g., $u_{n+1} = f(u_n)$) plus a starting value.

**Choices:**

- A rule that defines a term using earlier terms (e.g., $u_{n+1} = f(u_n)$) plus a starting value. ✔
  - _why:_ A recurrence relation generates each new term from one or more preceding terms. Initial value information is also required so that the sequence can begin.
- A rule that defines a term using its position (e.g., $u_n = f(n)$) without a starting value.
  - _why:_ Defining a term directly from its position is an explicit formula, not a recurrence relation. A recurrence uses earlier terms and needs at least one starting value.
- A rule that defines the sum using the number of terms (e.g., $S_n = f(n)$) without a starting value.
  - _why:_ A formula for the first $n$ terms’ total defines partial sums rather than a recurrence. A recurrence instead generates terms from earlier terms and starting values.
- A rule that defines a term using a fixed difference (e.g., $u_n = a + (n-1)d$) plus a final value.
  - _why:_ A constant difference is specifically the defining property of an arithmetic sequence, not recurrence relations generally. Recurrences may use many different functions of earlier terms.

## Card 14 — `basic`

**Front:** What defines a periodic sequence?

**Back:** A sequence that repeats its values in a fixed cycle.

**Choices:**

- A sequence that repeats its values in a fixed cycle. ✔
  - _why:_ In a periodic sequence, the same finite pattern of values recurs indefinitely. The number of terms in the shortest repeating cycle is called its period.
- A sequence that approaches its values towards a fixed limit.
  - _why:_ Approaching a fixed value defines a convergent sequence, whose terms need not repeat. A periodic sequence instead repeats its values in a fixed cycle.
- A sequence that increases its values by a fixed difference.
  - _why:_ Increasing by a constant amount defines an arithmetic sequence, which is generally not periodic. Periodicity requires the same values to recur in a fixed cycle.
- A sequence that multiplies its values by a fixed ratio.
  - _why:_ Multiplication by a constant defines a geometric sequence, but its values usually change indefinitely. A periodic sequence must repeat the same values in a fixed cycle.

## Card 15 — `basic`

**Front:** If $u_1 = \frac{3}{5}$ and $u_{n+1} = \frac{1}{u_n}$, what is the period of the sequence?

**Back:** 2 ($u_1 = \frac{3}{5}, u_2 = \frac{5}{3}, u_3 = \frac{3}{5}$)

**Choices:**

- 2 ($u_1 = \frac{3}{5}, u_2 = \frac{5}{3}, u_3 = \frac{3}{5}$) ✔
  - _why:_ Taking the reciprocal alternates the terms between $\frac35$ and $\frac53$. The original value first reappears after two steps, so the period is 2.
- 1 ($u_1 = \frac{3}{5}, u_2 = \frac{3}{5}, u_3 = \frac{3}{5}$)
  - _why:_ A period of 1 would require every term to equal $\frac35$, but taking its reciprocal gives $u_2=\frac53$. The actual period is 2.
- 3 ($u_1 = \frac{3}{5}, u_2 = \frac{5}{3}, u_3 = \frac{3}{5}$)
  - _why:_ Counting the three displayed terms confuses the number of terms listed with the cycle length. Since $u_3=u_1$, the two-term pattern has period 2.
- 4 ($u_1 = \frac{3}{5}, u_2 = \frac{5}{3}, u_3 = \frac{3}{5}, u_4 = \frac{5}{3}$)
  - _why:_ Counting two complete alternations gives four positions but not the shortest repeating cycle. The values already repeat after two terms, so the period is 2.

## Card 16 — `cloze`

**Front:** A sum where consecutive middle terms cancel out, leaving only terms at the start and end, is called a [ ___ ].

**Back:** A sum where consecutive middle terms cancel out, leaving only terms at the start and end, is called a telescoping sum.

**Choices:**

- telescoping sum ✔
  - _why:_ In a telescoping sum, terms cancel in succession across neighbouring expressions. This cancellation leaves only a small number of boundary terms from the beginning and end.
- geometric series
  - _why:_ A geometric series has a constant ratio between consecutive terms, but its middle terms do not necessarily cancel. Consecutive cancellation characterises a telescoping sum.
- arithmetic series
  - _why:_ An arithmetic series has a constant difference between consecutive terms, which does not produce the stated cancellation. A sum with cancelling middle terms is a telescoping sum.
- convergent series
  - _why:_ A convergent series approaches a finite value, but convergence alone does not imply cancellation of middle terms. The cancellation pattern specifically defines a telescoping sum.

## Card 17 — `basic`

**Front:** Evaluate $\sum_{k=0}^{n} f(k) - \sum_{k=0}^{n-1} f(k)$.

**Back:** $$f(n)$

**Choices:**

- $$f(n)$ ✔
  - _why:_ The two sums share all terms from $f(0)$ to $f(n-1)$, so these cancel when the sums are subtracted, leaving only the final term $f(n)$.
- $$f(n-1)$
  - _why:_ This mistakes the final shared term for the uncancelled term. Both sums contain $f(n-1)$, so it cancels; the first sum’s additional term is $f(n)$.
- $$f(n+1)$
  - _why:_ This off-by-one error extends the first sum beyond its upper limit. The first sum ends at $k=n$, so cancellation leaves $f(n)$, not $f(n+1)$.
- $$0$
  - _why:_ The sums would cancel completely only if they had identical limits. The first sum contains one extra term, $f(n)$, which remains after all shared terms cancel.

## Card 18 — `basic`

**Front:** In a worded problem, how do you decide between using $u_n$ or $S_n$?

**Back:** Use $u_n$ for an amount in a specific single term.Use $S_n$ for a cumulative total over time.

**Choices:**

- Use $u_n$ for an amount in a specific single term.Use $S_n$ for a cumulative total over time. ✔
  - _why:_ The notation $u_n$ identifies the value of one particular term, whereas $S_n$ represents the sum of terms up to term $n$, giving a cumulative total.
- Use $S_n$ for an amount in a specific single term.Use $u_n$ for a cumulative total over time.
  - _why:_ This reverses the meanings of the two notations. The term $u_n$ gives one specific amount, while $S_n$ adds all relevant terms to produce a cumulative total.
- Use $u_n$ for an amount in a specific single term.Use $u_n$ for a cumulative total over time.
  - _why:_ Using $u_n$ for both confuses an individual term with a sum. A specific single amount uses $u_n$, but a cumulative total over time requires $S_n$.
- Use $S_n$ for an amount in a specific single term.Use $S_n$ for a cumulative total over time.
  - _why:_ Using $S_n$ for both treats every quantity as a running total. A cumulative total uses $S_n$, whereas an amount belonging to one specific term uses $u_n$.

## Card 19 — `cloze`

**Front:** In the series $\sum_{r=4}^{18} (5r-1)$, the first term is found by substituting $r = \text{[...]}$.

**Back:** In the series $\sum_{r=4}^{18} (5r-1)$, the first term is found by substituting $r = \boxed{4}$.

**Choices:**

- 4 ✔
  - _why:_ The lower limit of the summation is $4$, so the series begins when $r=4$. Substituting this value into $5r-1$ produces the first term.
- 3
  - _why:_ This uses one less than the lower limit, an off-by-one error. The value beneath the summation sign is $4$, so the first substitution must be $r=4$.
- 5
  - _why:_ This begins with the value after the stated lower limit and therefore skips the first term. Since the sum starts at $r=4$, the required substitution is $4$.
- 18
  - _why:_ This confuses the upper limit with the lower limit. Substituting $r=18$ gives the final term, while the first term is obtained by substituting $r=4$.

## Card 20 — `basic`

**Front:** How many terms are in the series $\sum_{r=4}^{18} (5r-1)$?

**Back:** 15 terms ($18 - 4 + 1$)

**Choices:**

- 15 terms ($18 - 4 + 1$) ✔
  - _why:_ For consecutive integer values from $4$ through $18$, both endpoints are included. Therefore the number of terms is $18-4+1=15$.
- 14 terms ($18 - 4$)
  - _why:_ The calculation $18-4$ counts the gaps between the limits rather than the included values. Adding one for the inclusive endpoints gives $18-4+1=15$ terms.
- 18 terms ($18$)
  - _why:_ This treats the upper limit as the number of terms and ignores that the index begins at $4$. Inclusive counting gives $18-4+1=15$ terms.
- 22 terms ($18 + 4$)
  - _why:_ This incorrectly adds the two limits instead of finding their inclusive difference. The index runs through consecutive integers, so the count is $18-4+1=15$ terms.
