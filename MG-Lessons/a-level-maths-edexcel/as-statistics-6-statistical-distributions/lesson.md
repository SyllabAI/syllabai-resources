# as-statistics-6-statistical-distributions — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 3 check questions (source: MathsGenie lessons)_

## Discrete random variables

A random variable is a quantity whose value depends on chance. It is discrete if it can only take separate countable values, such as $0, 1, 2, 3$.

A discrete probability distribution lists each possible value and its probability $P(X=x)$. Every probability must be between 0 and 1, and the probabilities must add to 1.

If a table contains an unknown constant, start with the total probability rule. It is often the quickest route to the missing value.

$$$\sum P(X=x)=1$$

## Worked example with a discrete inequality

Suppose $X$ can take $0, 1, 2, 3$ with probabilities $0.18, 0.20, 0.27, 0.35$. The missing value came from making the total $1$, so the table is now complete.

To find $P(X>1.4)$, do not think of $X$ as continuous. Because $X$ only takes integer values here, "$X>1.4$" means $X=2$ or $X=3$.

$$$P(X>1.4)=P(X=2)+P(X=3)=0.27+0.35=0.62$$

A common mistake is to include part of the probability at $1$ or $2$, but discrete probabilities come in whole jumps.

## Cumulative distribution functions

![Side-by-side bar chart for a discrete distribution with probabilities 0.10, 0.25, 0.40, 0.25 at x=1,2,3,4 and matching cumulative step graph rising to 0.10, 0.35, 0.75, 1.00.](../assets/001-e29a2c9f-92ce-447d-9bb6-22ad7501b639.jpeg)

The cumulative distribution function is defined by $F(x)=P(X\le x)$. It is a running total, so for a discrete variable it rises in jumps rather than smoothly.

If $P(X=1)=0.10$, $P(X=2)=0.25$, $P(X=3)=0.40$ and $P(X=4)=0.25$, then the corresponding cumulative values are found by summing the probabilities:

$$$F(1)=0.10,\quad F(2)=0.35,\quad F(3)=0.75,\quad F(4)=1.00$$

Each new value is the previous total plus the next probability. A quick check is that cumulative probabilities never go down, and the final value must always be 1.

## Discrete uniform distributions

A discrete uniform distribution has equally likely outcomes. If there are $n$ possible values, each one has probability $\frac{1}{n}$.

For a fair spinner labelled $1,2,3,4$, the random variable $Y$ follows a uniform distribution where each result is equally probable:

$$$P(Y=1)=P(Y=2)=P(Y=3)=P(Y=4)=\frac{1}{4}$$

The four probabilities add to 1, as they should. This confirms that the probability mass is correctly distributed across all possible outcomes.

## Binomial distributions

We write $X\sim B(n,p)$ when $X$ counts successes in $n$ trials. Each trial must have two outcomes, the success probability must stay constant, and the trials must be independent.

The probability of exactly $r$ successes is $$P(X=r)=\binom{n}{r}p^r(1-p)^{n-r}$$ The factor $\binom{n}{r}$ counts how many ways the $r$ successes can be arranged.

If a student answers 12 independent questions, each correct with probability 0.3, then $X\sim B(12,0.3)$. For exactly 4 correct answers, $$P(X=4)=\binom{12}{4}(0.3)^4(0.7)^8\approx 0.231$$ This is an exact probability because we are asking for one specific value of $X$.

## Binomial inequalities and expected counts

Because binomial variables are discrete, inequalities need careful boundaries. For example, $P(X<3)=P(X\le 2)$ and $P(X>4)=P(X\ge 5)$.

Complements often save time when calculating probabilities. If $X\sim B(12,0.3)$, we calculate the upper tail by subtracting the cumulative probability from the total:

$$$P(X\ge 5)=1-P(X\le 4)\approx 0.276$$

Similarly, $P(X<3)=P(X\le 2)\approx 0.253$. If an event has probability $p$ on each of $N$ independent occasions, the expected number of times it occurs is $Np$.

For example, if $P(X=0)\approx 0.134$ in one match, then over 30 matches the expected number is $30\times 0.134\approx 4.02$. An expected number is a long-run average, so it need not be a whole number.

## Independence and transformations

When two games or attempts are independent, multiply probabilities along one route and add different routes that give the same result. If $T$ is the total score and the only score pairs making 20 are $(5,15)$, $(10,10)$ and $(15,5)$, those are the only routes you add.

Using probabilities $0.30$, $0.20$ and $0.25$ for scores 5, 10 and 15 respectively, we calculate the total probability for the outcome $T=20$. We do this by identifying all independent combinations that sum to the target value.

$$$P(T=20)=0.30\times 0.25+0.20\times 0.20+0.25\times 0.30=0.190$$

So the chance of a total of 20 is 0.190. Transformations work by rewriting the condition in terms of the original variable. If $Y=9-3X$, then $Y+X\ge 2$ becomes $9-3X+X\ge 2$, leading to $X\le 3.5$. For a discrete variable taking values $1,2,3,4$, that means $X=1,2,3$.

## Check yourself

1. A discrete random variable $X$ has probabilities $0.18$, $a$, $0.27$ and $0.35$ for $x=0,1,2,3$ respectively. What is $a$?

   - 0.20 ✔

   - 0.80

   - 0.18

   - 0.62

   _Explanation:_ The known probabilities sum to $0.18+0.27+0.35=0.80$, so the missing value is $1-0.80=0.20$. The common wrong answer 0.80 is just the sum of the given probabilities, not the missing amount.

2. A fair six-sided die is thrown once. If $Y$ is the score, what is $P(Y>4)$?

   - $$\frac{1}{6}$

   - $$\frac{1}{3}$ ✔

   - $$\frac{1}{2}$

   - $$\frac{2}{3}$

   _Explanation:_ Only scores 5 and 6 are greater than 4, so there are 2 successful outcomes out of 6 and $P(Y>4)=\frac{2}{6}=\frac{1}{3}$. The common wrong answer $\frac{1}{2}$ comes from wrongly including 4 and treating the question as $Y \ge 4$.

3. (Stretch) Let $X$ take the values $1, 2, 3, 4$ and let $Y = 9 - 3X$. Which condition on $X$ is equivalent to $Y + X \ge 2$?

   - $$X \ge 3.5$

   - $$X \le 3.5$ ✔

   - $$X \le 2$

   - $$X \ge 2$

   _Explanation:_ Substitute $Y = 9 - 3X$ to get $9 - 3X + X \ge 2$, so $-2X \ge -7$ and then $X \le 3.5$ after reversing the inequality when dividing by $-2$. The common wrong answer $X \ge 3.5$ comes from forgetting that inequalities flip when you divide by a negative number.
