# grade-5-5-22-probability-trees — lesson

_Lane: `gcse-maths-edexcel` · grade 5 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Reading a probability tree

A probability tree shows events happening in stages. Each split represents the possible outcomes of one event.

At any split, the branch probabilities must add to 1. If one branch is missing, use the complement rule $P(\text{not }A)=1-P(A)$.

A split can have two branches or three, such as win, draw, lose, but the labels from one point still add to 1. Then read the question language carefully: multiply along a route for both, and add route totals when the event can happen in more than one way.

## Labelling a two-stage tree from counts

![Two-stage probability tree for Bag A and Bag B with branches labelled Red 1/4 and Blue 3/4 for Bag A, then Red 4/5 and Blue 1/5 for Bag B, ending with the four colour outcomes](../assets/001-e0a63106-c79a-4455-b660-1de6fc8ff8fe.jpeg)

This tree shows Sofia taking one counter from Bag A, then one from Bag B. The first split represents Bag A, and the second split is copied after both first branches because Bag B is a separate event.

Bag A has 2 red and 6 blue counters, so there are 8 in total. Its first branches are calculated as $P(\text{red from A})=\frac{2}{8}=\frac{1}{4}$ and $P(\text{blue from A})=\frac{6}{8}=\frac{3}{4}$.

Bag B has 4 red and 1 blue counter, so its branches are $P(\text{red from B})=\frac{4}{5}$ and $P(\text{blue from B})=\frac{1}{5}$. Always check that the probabilities in each split add up to 1 before you proceed with calculations.

## Multiply along one route for both

When a question says both or and, follow one complete route from start to finish. That means you multiply the branch probabilities on that route.

Amira has $P(\text{win badminton}) = \frac{3}{5}$ and $P(\text{win table tennis}) = \frac{7}{10}$. To find the probability that she wins both, we multiply along the win-win path: $$P(\text{both wins}) = \frac{3}{5} \times \frac{7}{10} = \frac{21}{50}$$

A common mistake is to add the two win probabilities. Adding is for different routes, not for calculating a single outcome along one route.

## Add routes for different results

Sometimes the answer can happen in more than one way. If Eli wears different colours on Monday and Tuesday, the successful routes are navy then grey or grey then navy.

First find the missing probability: $P(\text{grey})=1-\frac{5}{9}=\frac{4}{9}$. Then multiply along each route: $P(\text{navy then grey})=\frac{5}{9} \times \frac{4}{9}=\frac{20}{81}$ and $P(\text{grey then navy})=\frac{4}{9} \times \frac{5}{9}=\frac{20}{81}$.

Now add the successful route probabilities together to find the final result. In this example, $P(\text{different})=\frac{20}{81}+\frac{20}{81}=\frac{40}{81}$.

## Use a complement for at least one

At least one means one or more. In probability problems, it is often much quicker to find the probability of the opposite event, which is "none", and subtract that value from 1.

Consider a train that is late with probability $0.3$ on each of two days. The probability it is not late is $0.7$, so the probability it is late on neither day is $P(\text{none late}) = 0.7 \times 0.7 = 0.49$.

Now use the complement rule: $P(\text{at least one late}) = 1 - 0.49 = 0.51$. Using this shortcut is usually faster than listing every successful route on a tree diagram and summing them.

## Trees with three outcomes

A tree does not have to be restricted to binary outcomes at each split. It can have three or more branches, such as win, draw, and lose, provided the probabilities of all branches at a single node sum to 1.

If $P(\text{win})=0.5$ and $P(\text{draw})=0.2$, then the probability of the remaining outcome is $P(\text{lose})=1-0.5-0.2=0.3$. In this scenario, each round split consists of three distinct branches: win (0.5), draw (0.2), and lose (0.3).

The standard multiplication rules for independent events still apply regardless of the number of branches. For example, the probability of winning both rounds in a sequence is calculated as $P(\text{win both rounds})=0.5 \times 0.5=0.25$.

## Check yourself

1. The probability of winning a game is 0.65. What label should go on the not win branch of a tree?

   - 0.35 ✔

   - 0.65

   - 0.30

   - 1.65

   _Explanation:_ At one split the probabilities must total 1, so $P(\text{not win})=1-0.65=0.35$. The common wrong answer 0.65 just repeats the given branch and ignores the complement.

2. Amira wins badminton with probability $\frac{3}{5}$ and table tennis with probability $\frac{7}{10}$. What is the probability she wins both?

   - $$\frac{13}{10}$

   - $$\frac{21}{50}$ ✔

   - $$\frac{1}{2}$

   - $$\frac{1}{10}$

   _Explanation:_ Wins both is one route, so you multiply: $\frac{3}{5} \times \frac{7}{10}=\frac{21}{50}$. The common wrong answer $\frac{13}{10}$ comes from adding, and it is impossible anyway because a probability cannot be greater than 1.

3. A player has $P(\text{win})=0.5$, $P(\text{draw})=0.2$, and $P(\text{lose})=0.3$ in each round. What is the probability of at least one draw in two rounds?

   - 0.04

   - 0.36 ✔

   - 0.64

   - 0.40

   _Explanation:_ The chance of no draw in one round is $0.8$, so the chance of no draws in two rounds is $0.8 \times 0.8=0.64$. Therefore $P(\text{at least one draw})=1-0.64=0.36$; the common wrong answer 0.04 is only the probability of drawing both rounds.
