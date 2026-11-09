# grade-6-6-3-the-product-rule-for-counting — lesson

_Lane: `gcse-maths-edexcel` · grade 6 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Stages, options and outcomes

![Tree diagram with two wraps branching to three drinks each, showing six complete lunch outcomes](../assets/001-8d74a5b9-159c-400d-a462-7153c488591d.jpeg)

Counting problems often happen in stages. In the tree diagram, choosing a wrap is one stage and choosing a drink is another.

An option is one possible choice at a single stage, and an outcome is one complete result after all stages are chosen. Each full path on the tree is one lunch outcome.

If every first-stage option can go with every second-stage option, use the product rule. For two stages with $a$ options and $b$ options, total outcomes are $a \times b$, so here $2 \times 3 = 6$.

## Worked example: one from each group

Suppose a club chooses one boy from 11 boys and one girl from 13 girls. This is a two-stage choice, with one student taken from each group.

There are 11 choices for the boy. For each of those, there are 13 choices for the girl.

$$$11 \times 13 = 143$$

There are 143 possible pairs in total. Adding $11 + 13$ would only count the students altogether, not the different pairs.

## More than two stages

The product rule also works for more than two stages. If you choose a starter and a main and a dessert, you take one from each group to form a complete combination.

For 4 starters, 6 mains, and 3 desserts, multiply all three stage counts:
$$4 \times 6 \times 3 = 72$$
So there are 72 different three-course meals.

The word "and" is a clue that you are making separate choices, not adding the menu sizes. This works directly only when every starter can be paired with every main and every dessert.

## Unknown numbers of options

Sometimes the total number of outcomes is given, but one stage has an unknown number of options. In these cases, we can use the product rule to form and solve an algebraic equation.

For example, if there are 8 sandwich choices and $x$ drink choices for a total of 90 meal deals, then $8 \times x = 90$. Solving this gives $x = 90 \div 8 = 11.25$.

In real-world scenarios, a number of choices must be a whole number. Since 11.25 drinks is impossible, the claim of 90 available meal deals would be logically incorrect.

## When choices are used up

Sometimes you choose more than once from the same group, so the number of options goes down. This is called choosing without replacement.

If Maya gets one card from a deck of 52, Leo can only get one of the 51 cards left. So the number of possible deals is:

$$$52 \times 51 = 2652$$

There are 2652 different allocations. Do not divide by 2 here. Maya getting the ace and Leo the king is different from Maya getting the king and Leo the ace because the people are named.

## Pairs, matches and handshakes

![4 by 4 team-vs-team table showing mirrored duplicate matches above and below the diagonal, with matching colours on pairs such as A-B and B-A](../assets/002-801cded0-0aee-4d08-b705-d8e1a861a494.jpeg)

If you first count an ordered pair, there are $n$ choices for the first item and $n-1$ for the second. That gives $n(n-1)$ ordered outcomes.

For ordinary pairs or matches, order does not matter, so each pair appears twice: once as $A,B$ and once as $B,A$. The number of unordered pairs is therefore calculated by dividing the total permutations by the number of ways to arrange the pair.

$$$
\frac{n(n-1)}{2}
$$
This removes the double counting. For 9 teams playing each other once, the number of games is found by applying this formula.

$$$
\frac{9 \times 8}{2} = 36
$$
Team $A$ vs Team $B$ is the same game as Team $B$ vs Team $A$, so dividing by 2 is essential to avoid counting the same match twice.

## Check yourself

1. A cafe offers 4 sandwiches and 5 drinks. One sandwich and one drink are chosen. How many different meal deals are possible?

   - 9

   - 20 ✔

   - 10

   - 25

   _Explanation:_ You choose one from each group, so multiply the numbers of options: $4 \times 5 = 20$. The common wrong answer 9 comes from adding the options, but $4 + 5$ counts menu items, not complete sandwich-and-drink outcomes.

2. A restaurant has 2 starters, 5 mains and 4 desserts. How many different 3-course meals are possible?

   - 11

   - 20

   - 40 ✔

   - 54

   _Explanation:_ There are 3 stages, so multiply: $2 \times 5 \times 4 = 40$. The common wrong answer 11 comes from adding the numbers of dishes instead of counting complete meals.

3. A meal deal has 4 snack choices and $x$ drink choices. A student says there are 50 possible meal deals. Which statement is correct?

   - Yes, because $x = 12$

   - Yes, because $x = 12.5$

   - No, because $x = 12.5$ and the number of drink choices must be a whole number ✔

   - No, because you should add 4 and $x$

   _Explanation:_ Use the product rule to set up $4x = 50$, so $x = 12.5$. The correct answer is no because a number of choices must be a whole number; the common wrong answer B forgets that you cannot have 12.5 drink options. Hint: Solve for $x$ and then ask whether the answer makes sense.

4. 8 students each shake hands with every other student once. How many handshakes are there?

   - 56

   - 28 ✔

   - 16

   - 64

   _Explanation:_ Start by counting ordered pairs: $8 \times 7 = 56$. Each handshake is counted twice, so divide by 2 to get 28; the common wrong answer 56 forgets the double counting.
