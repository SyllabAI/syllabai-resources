# as-statistics-5-probability — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 2 check questions (source: MathsGenie lessons)_

## Probability basics

Probability measures how likely an event is, with $0$ representing an impossible outcome and $1$ representing a certain one. The sample space is the set of all possible outcomes, and an event is any chosen outcome or group of outcomes.

If all outcomes are equally likely, we use the formula below to calculate the probability. Note that every probability must satisfy the range constraint $0 \le P(A) \le 1$.

$$P(A)=\frac{\text{number of favourable outcomes}}{\text{total number of equally likely outcomes}}$$

The complement of $A$, written $A'$, means "not $A$". It is often quicker to use the complement rule than to count the unwanted outcomes directly:

$$P(A')=1-P(A)$$

## Venn diagrams and set notation

![Two-event Venn diagram inside a universal set showing A only, B only, the overlap A intersection B, and the outside region for neither event](../assets/001-35f01c73-f8b6-4918-8a58-b63911372494.jpeg)

A Venn diagram shows how events overlap inside the universal set. The overlap is $A \cap B$, while everything in either circle is $A \cup B$.

In probability, "or" is inclusive unless the question says otherwise. So $A \cup B$ includes outcomes in $A$ only, in $B$ only, and in both. This is represented by the key two-event formula:

$$$P(A \cup B)=P(A)+P(B)-P(A \cap B)$$

You subtract the overlap because it is counted twice when you add $P(A)$ and $P(B)$. This ensures that the probability of the union correctly counts each outcome only once.

## Mutually exclusive or independent?

Mutually exclusive events cannot happen at the same time. That means

$$P(A \cap B)=0$$

and a simple example is getting "red" and "blue" on one draw.

Independent events do not affect one another. For independent events,

$$P(A \cap B)=P(A)P(B)$$

and a typical example is "first coin toss is heads" and "second coin toss is heads".

These ideas are different. To test independence, compare the actual overlap with $P(A)P(B)$; if two events are mutually exclusive and both have positive probability, they cannot be independent.

## Worked example: filling a two-event Venn diagram

Suppose $P(A)=0.6$, $P(B)=0.5$, and the probability of neither event is $0.1$. First find the probability of being in at least one circle:
$$P(A \cup B)=1-0.1=0.9$$

Now use the Venn formula to find the overlap:
$$P(A \cap B)=0.6+0.5-0.9=0.2$$
Then the $A$-only region is $0.6-0.2=0.4$.

Similarly, the $B$-only region is $0.5-0.2=0.3$, and the outside region is $0.1$. A final check is
$$0.4+0.2+0.3+0.1=1$$
which confirms every region has been accounted for.

## Three-set Venn diagrams

In a three-set Venn diagram, start with the middle. The value in all three sets must be placed first, because each pairwise total includes that centre region.

Suppose 6 people are in all three categories, 10 in football and golf, 9 in golf and hockey, and 8 in football and hockey. To find the overlap, subtract 6 from each pairwise total first.

$$$10-6=4,\quad 9-6=3,\quad 8-6=2$$

Next, use each set total to find the single-set-only regions. For example, if 28 watch football altogether, then football only is $28-4-2-6=16$, and the none region comes last.

## Tree diagrams and routes

![Probability tree diagram for two draws without replacement from a bag with 3 red and 2 blue counters, with branches labelled and end outcomes RR, RB, BR, and BB](../assets/002-5091fb19-9287-49bc-85bf-fa27c6cb838b.jpeg)

A tree diagram breaks a probability problem into stages. Multiply along one route for "and", and add separate routes for "or".

In the tree above, $P(RB)=\frac{3}{5}\times\frac{2}{4}=\frac{3}{10}$. The denominator changes from $5$ to $4$ because one counter has already been removed.

One of each colour can happen as $RB$ or $BR$. So calculation for the total probability is:

$$P(\text{one of each})=\frac{3}{5}\times\frac{2}{4}+\frac{2}{5}\times\frac{3}{4}=\frac{3}{5}$$

## Total probability and conditional probability

Sometimes the same outcome can happen through several routes. When that happens, work out each route probability and then add them. For example, if machine A makes 40% of components and 3% of its components are faulty:

$$$P(\text{A and faulty})=(0.40)(0.03)=0.012$$

This is one route to a faulty component. If machines A, B, and C make 40%, 35%, and 25% of the items with fault rates 3%, 2%, and 1%, we sum the individual route probabilities:

$$$P(\text{faulty})=(0.40)(0.03)+(0.35)(0.02)+(0.25)(0.01)=0.0215$$

You add because the faulty item could have come from A, B, or C. Conditional probability is written $P(B \mid A)$, which represents the probability of $B$ occurring given that $A$ has already happened.

## Check yourself

1. If $P(A)=0.6$, $P(B)=0.5$ and $P(A \cap B)=0.2$, what is $P(A \cup B)$?

   - $$0.9$ ✔

   - $$1.1$

   - $$0.8$

   - $$0.3$

   _Explanation:_ Use $P(A \cup B)=P(A)+P(B)-P(A \cap B)=0.6+0.5-0.2=0.9$. The common wrong answer $1.1$ comes from adding $0.6$ and $0.5$ without subtracting the overlap, so the shared region is counted twice.

2. Stretch: A box contains 10 milk chocolates and 8 dark chocolates. Two chocolates are taken at random without replacement. What is the probability of taking one of each type?

   - $$\frac{80}{153}$ ✔

   - $$\frac{40}{153}$

   - $$\frac{28}{153}$

   - $$\frac{80}{289}$

   _Explanation:_ "One of each" can happen in two orders, milk then dark or dark then milk. So the probability is $$\frac{10}{18} \times \frac{8}{17} + \frac{8}{18} \times \frac{10}{17} = \frac{80}{153}$$. The common wrong answer $\frac{40}{153}$ counts only one of the two valid routes. Hint: Write both possible orders before you calculate.
