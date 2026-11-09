# grade-6-6-17-probability-trees — lesson

_Lane: `igcse-maths-edexcel` · grade 6 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Probability and complements

Probability is a number from $0$ to $1$, where $0$ means impossible and $1$ means certain. For equally likely outcomes such as counters or cards, use the following formula:

$$$P(\text{event}) = \frac{\text{number of successful outcomes}}{\text{total number of outcomes}}$$

A probability tree is a branching diagram for events that happen in stages. At each split, the branch probabilities must add to $1$.

A complement means "does not happen". If $P(A)=p$, then the probability of the event not occurring is $P(\text{not }A)=1-p$.

## How to read a tree

To draw a two-stage tree, start with the first event and label its branches. From the end of each first branch, draw the possible outcomes of the second event.

If the events are independent, the second-stage probabilities stay the same on every branch. If something is taken and not replaced, the later probabilities can change.

Read the wording before calculating. "And" usually means multiply one complete path, while "or" usually means add separate successful paths after multiplying each one.

## Worked example: two blue counters

![Two-stage probability tree for Bag A and Bag B with the blue then blue path highlighted and labelled 2/5 times 3/5 equals 6/25](../assets/001-88031edb-0a34-427e-a5e2-b4cb301bf570.jpeg)

Bag A has $6$ red and $4$ blue counters. Bag B has $2$ red and $3$ blue counters, and one counter is chosen from each bag. We want to find $P(\text{blue from A and blue from B})$.

First find the blue probabilities for each bag. In Bag A, $P(\text{blue from A}) = \frac{4}{10} = \frac{2}{5}$, and in Bag B, $P(\text{blue from B}) = \frac{3}{5}$.

The event "two blue counters" is one complete path through the tree: blue from A, then blue from B. To calculate this outcome, we multiply the probabilities along that specific path.

$$$\frac{2}{5} \times \frac{3}{5} = \frac{6}{25}$$

There is only one successful path here, so we stop after multiplying. This is the pattern for questions that say "both" or "and".

## Worked example: different colours

![Two-stage probability tree for Monday and Tuesday scarf colours with blue then white and white then blue paths highlighted and added to 24/49](../assets/002-12e3365e-8df5-4feb-9ce1-a089c3162ed6.jpeg)

Sofia wears a blue scarf with probability $\frac{3}{7}$ on any day, so the probability of a white scarf is $1-\frac{3}{7}=\frac{4}{7}$. Different colours can happen in two ways: blue then white, or white then blue.

Find each path first. Each complete route is multiplied separately.
$$\frac{3}{7}\times\frac{4}{7}=\frac{12}{49}$$
$$\frac{4}{7}\times\frac{3}{7}=\frac{12}{49}$$

Now add the matching path probabilities:
$$\frac{12}{49}+\frac{12}{49}=\frac{24}{49}$$

A very common mistake is to stop at $\frac{12}{49}$. That counts only one order and misses the second successful path.

## At least one is often quickest by complement

"At least one" means one or more. In a two-stage tree, you can add several successful paths, but the complement rule is usually a much quicker method.

Suppose a train is delayed with probability $0.3$ on any day. Then the probability of the train being on time is $P(\text{not delayed}) = 1 - 0.3 = 0.7$.

The complement of "delayed on at least one day" is "not delayed on either day". That is a single path, calculated as:
$$0.7 \times 0.7 = 0.49$$

Now subtract from $1$ to find the final probability:
$$1 - 0.49 = 0.51$$
So the probability of at least one delay occurring is $0.51$.

## Three branches and changing probabilities

Not every split has two branches. A tree can have three outcomes such as win, draw or lose, and those branch probabilities must still add to $1$.

If $P(\text{win})=0.5$ and $P(\text{draw})=0.2$, then $P(\text{lose})=1-0.5-0.2=0.3$. To find the probability of winning both games, follow the single path win then win:

$$$0.5\times 0.5=0.25$$

Watch for wording like "not replaced". Then the first result changes what is left, so the probabilities on the second split may be different.

## Check yourself

1. A spinner lands on green with probability $\frac{3}{8}$. If green and purple are the only outcomes, what is $P(\text{purple})$?

   - $$\frac{5}{8}$ ✔

   - $$\frac{3}{8}$

   - $$\frac{3}{5}$

   - $$\frac{1}{8}$

   _Explanation:_ $$\frac{5}{8}$ is correct because purple is the complement of green, so $1-\frac{3}{8}=\frac{5}{8}$. The common wrong answer $\frac{3}{8}$ just repeats the green probability instead of finding what is left to make the total $1$.

2. Sofia wears blue with probability $\frac{3}{7}$ each day and white otherwise. What is the probability she wears different colours on Monday and Tuesday?

   - $$\frac{12}{49}$

   - $$\frac{24}{49}$ ✔

   - $$\frac{25}{49}$

   - $$\frac{6}{7}$

   _Explanation:_ $$\frac{24}{49}$ is correct because "different colours" includes two paths: blue then white ($P = \frac{3}{7} \times \frac{4}{7} = \frac{12}{49}$) and white then blue ($P = \frac{4}{7} \times \frac{3}{7} = \frac{12}{49}$). Summing these mutually exclusive events gives $\frac{24}{49}$. The common wrong answer $\frac{12}{49}$ finds only one of those paths and forgets to add the second order.

3. Nina plays two games. In each game, $P(\text{win})=0.5$, $P(\text{draw})=0.2$ and $P(\text{lose})=0.3$. What is the probability of one win and one draw?

   - $$0.1$

   - $$0.2$ ✔

   - $$0.7$

   - $$0.25$

   _Explanation:_ $$0.2$ is correct because there are two successful paths, win then draw and draw then win, so $0.5\times 0.2 + 0.2\times 0.5 = 0.1 + 0.1 = 0.2$. The common wrong answer $0.1$ counts only one order and misses the second successful path.
