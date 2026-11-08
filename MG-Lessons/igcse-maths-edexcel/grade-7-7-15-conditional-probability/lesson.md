# grade-7-7-15-conditional-probability — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## What conditional probability means

Conditional probability asks for the chance of event $B$ given that event $A$ has already happened. It is written $P(B|A)$. The words "given that" tell you that the sample space has been restricted to outcomes where $A$ occurs.

When $P(A)>0$, the conditional probability formula is $P(B|A)=\frac{P(A \cap B)}{P(A)}$.

In many IGCSE questions, you can work this out from a tree diagram or by counting the outcomes left in the new sample space. This often happens in questions about selection without replacement.

Example: a bag has 7 orange and 5 purple counters. If the first counter was purple, then 11 counters remain and 7 of them are orange. So the probability that the second counter is orange is $\frac{7}{11}$. The denominator changes from 12 to 11 because one counter has been removed.

## Reading a tree diagram

![Probability tree for two draws without replacement from a bag with 5 red and 3 blue counters, labelled with 5/8, 3/8, 4/7, 3/7, 5/7, and 2/7](../assets/001-53143562-8cf0-41c2-a245-91c44ff5bd4a.jpeg)
A probability tree shows each stage of the experiment as branches. The probability on a second branch is worked out after the first outcome has happened, so it may change.

For one complete route, multiply along the branches. If there are only two outcomes at a stage, their branch probabilities add to 1.

If more than one route matches the event, add those route probabilities at the end. In this tree, $P(\text{red then blue}) = \frac{5}{8} \times \frac{3}{7}$, and "one of each colour" means adding red then blue and blue then red.

## Worked example: one of each colour

A bag contains 5 red and 3 blue counters. Two counters are chosen without replacement, and we want one of each colour. For same-colour questions you list matching routes, but here the successful routes are the two mixed-colour orders.

For red then blue, multiply along that route. You get:
$$\frac{5}{8}\times\frac{3}{7}=\frac{15}{56}$$

For blue then red, multiply along that route as well. You get:
$$\frac{3}{8}\times\frac{5}{7}=\frac{15}{56}$$

Now add the successful routes. You get:
$$\frac{15}{56}+\frac{15}{56}=\frac{30}{56}=\frac{15}{28}$$
The answer is not $\frac{15}{56}$ because that would count only one of the two possible orders.

## Using a Venn diagram before probability

Sometimes the information is given as overlapping sets before you are asked for a probability. In that case, fill in the Venn diagram first, then do the probability calculation.

Start with the centre, because totals such as tea and coffee already include the people who like all three. In a survey of 48 people, if 6 like none and 8 like all three, then $48-6=42$ people are inside the circles. If 17 like tea and coffee in total, then the tea and coffee only region is $17-8=9$.

After using the other totals, coffee only is 4 and coffee with the third drink only is 3. Together with 9 in tea and coffee only and 8 in the centre, the number who like coffee is $4+9+3+8=24$.

The probability that two people chosen without replacement both like coffee is $\frac{24}{48}\times\frac{23}{47}=\frac{23}{94}$.

## Stretch: when order matters

Be careful with wording. "The second number is greater than the first" is an ordered condition, so $1$ then $3$ counts but $3$ then $1$ does not.

With cards 1, 1, 2, 3, 3, 4, there are $6\times5=30$ ordered selections altogether. We now count how many ordered pairs have the second value greater than the first.

If the first card is 1, there are $2\times4=8$ successes. If the first card is 2, there are $1\times3=3$ successes, and if the first card is 3, there are $2\times1=2$ successes.

A first card of 4 gives no successes, so the total is $8+3+2=13$. The probability is $$P(\text{second}>\text{first})=\frac{13}{30}.$$

## Check yourself

1. A bag has 6 green and 4 yellow counters. One counter is chosen and not replaced. Given that the first counter was yellow, what is the probability that the second counter is green?

   - $$\frac{6}{10}$

   - $$\frac{6}{9}$ ✔

   - $$\frac{5}{9}$

   - $$\frac{4}{9}$

   _Explanation:_ There are 9 counters left and still 6 green counters, so the probability is $\frac{6}{9}$. The common wrong answer $\frac{6}{10}$ uses the original total and ignores that one counter was not replaced.

2. A bag contains 5 red and 3 blue counters. Two are chosen without replacement. What is the probability of getting one red and one blue?

   - $$\frac{15}{56}$

   - $$\frac{15}{28}$ ✔

   - $$\frac{5}{8}$

   - $$\frac{3}{7}$

   _Explanation:_ One red and one blue can happen in two orders, and each route has probability $\frac{15}{56}$, so adding them gives $\frac{15}{28}$. The common wrong answer $\frac{15}{56}$ counts only one successful route instead of both.

3. Two cards are chosen without replacement from 1, 1, 2, 3, 3, 4. What is the probability that the second number is greater than the first?

   - $$\frac{13}{30}$ ✔

   - $$\frac{13}{15}$

   - $$\frac{8}{30}$

   - $$\frac{17}{30}$

   _Explanation:_ There are 30 ordered selections altogether and 13 of them have second greater than first, so the probability is $\frac{13}{30}$. The common wrong answer $\frac{13}{15}$ is the probability of getting different numbers, which ignores the condition that the second must be larger. Hint: Count ordered selections, not just different pairs.
