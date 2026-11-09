# a-level-statistics-2-conditional-probability — lesson

_Lane: `a-level-maths-edexcel` · grade — · 5 content steps · 2 check questions (source: MathsGenie lessons)_

## Event notation and overlap

Probability questions use events such as $A$ and $B$. The complement $A'$ means $A$ does not happen, the intersection $A \cap B$ means both happen, and the union $A \cup B$ means at least one happens. For two events, the "or" formula is:

$$$P(A \cup B)=P(A)+P(B)-P(A \cap B)$$

This formula subtracts the intersection because the overlap is counted twice if you just add $P(A)$ and $P(B)$. If you want the probability of neither event, take the complement of the union:

$$$P(A' \cap B')=1-P(A \cup B)$$

This outside region often appears before a conditional probability question.

## Conditional probability means a smaller sample space

![Venn diagram with B shaded as the reduced sample space and overlap A intersect B darkened](../assets/001-e7f75fdd-28ec-45ab-be03-12d34508b381.jpeg)

$P(A \mid B)$ means the probability of $A$, given that $B$ has happened. Once $B$ is known, event $B$ becomes the whole sample space.

$$$P(A \mid B)=\frac{P(A \cap B)}{P(B)}$$

The event after the bar tells you the denominator, so "given $B$" means divide by $P(B)$, not by $P(A)$.

## Worked example: reverse conditionals

Suppose $P(A)=\frac{5}{18}$, $P(B)=\frac{2}{3}$ and $P(A \mid B)=\frac{1}{4}$. Start by reversing the conditional formula to find the overlap.
$$P(A \cap B)=P(A \mid B)P(B)=\frac{1}{4}\times \frac{2}{3}=\frac{1}{6}$$

To find $P(B' \mid A)$, we first need the part of $A$ that is not in $B$. Subtract the overlap from $P(A)$.
$$P(A \cap B')=P(A)-P(A \cap B)=\frac{5}{18}-\frac{1}{6}=\frac{1}{9}$$

Now condition on $A$, because the phrase is "given $A$". Divide by $P(A)$, not by $P(B')$.
$$P(B' \mid A)=\frac{P(A \cap B')}{P(A)}=\frac{\frac{1}{9}}{\frac{5}{18}}=\frac{2}{5}$$

For $P(A' \cup B)$, it is quicker to use a complement. The only region excluded is $A \cap B'$, so
$$P(A' \cup B)=1-P(A \cap B')=1-\frac{1}{9}=\frac{8}{9}$$

## Independence versus mutually exclusive

Independent events do not affect each other. You can test for independence using the following multiplication rule:

$$$P(A \cap B)=P(A)P(B)$$

Equivalently, you can check if $P(A \mid B)=P(A)$ when $P(B)>0$. On the other hand, mutually exclusive events are events that cannot happen together, meaning their intersection is empty.

$$$P(A \cap B)=0$$

Since there is no overlap, the union simplifies to $P(A \cup B)=P(A)+P(B)$. If $P(A)$ and $P(B)$ are non-zero and mutually exclusive, knowing $B$ happened makes $A$ impossible, so the events cannot be independent.

## Tree diagrams and reverse conditionals

![Probability tree showing machines A, B, and C leading to faulty and not faulty branches with probabilities labelled](../assets/002-ca73318d-58ba-40df-8fa1-bdffda2d0254.jpeg)
A tree diagram is useful when there are stages, such as choosing a machine and then checking whether a component is faulty. Multiply along each path, and add separate paths that end at the same outcome.

Here $P(A)=0.50$, $P(B)=0.30$, $P(C)=0.20$ and the faulty rates are $4\%$, $2\%$, and $5\%$. Multiply along the faulty paths:
$$P(A \cap F)=0.50 \times 0.04=0.020$$
$$P(B \cap F)=0.30 \times 0.02=0.006$$
$$P(C \cap F)=0.20 \times 0.05=0.010$$

Add these separate faulty paths to get the total probability:
$$P(F)=0.020+0.006+0.010=0.036$$
This is the probability that a randomly chosen component is faulty regardless of which machine produced it.

If the component is known to be faulty, only the faulty branches remain in the sample space. So
$$P(C \mid F)=\frac{P(C \cap F)}{P(F)}=\frac{0.010}{0.036}=\frac{5}{18}$$
This is larger than $0.20$ because machine $C$ has the highest faulty rate among the three.

## Check yourself

1. Which expression is always equal to $P(A \mid B)$, provided $P(B)>0$?

   - $$\frac{P(A \cap B)}{P(B)}$ ✔

   - $$\frac{P(A \cap B)}{P(A)}$

   - $$\frac{P(A \cup B)}{P(B)}$

   - $$P(A)+P(B)$

   _Explanation:_ The condition is $B$, so $B$ is the reduced sample space and the denominator must be $P(B)$. The most common wrong answer is B, but dividing by $P(A)$ would match a "given $A$" question instead.

2. Stretch: Events $A$ and $B$ satisfy $P(A)=\frac{5}{18}$, $P(B)=\frac{2}{3}$ and $P(A \mid B)=\frac{1}{4}$. What is $P(B' \mid A)$?

   - $$\frac{2}{5}$ ✔

   - $$\frac{1}{4}$

   - $$\frac{1}{6}$

   - $$\frac{3}{5}$

   _Explanation:_ First find $P(A \cap B)=\frac{1}{6}$, then $P(A \cap B')=\frac{5}{18}-\frac{1}{6}=\frac{1}{9}$. Finally divide by $P(A)=\frac{5}{18}$ to get $\frac{2}{5}$; the common wrong answer $\frac{1}{4}$ is just the original $P(A \mid B)$ and does not reverse the condition. Hint: Work inside event $A$.
