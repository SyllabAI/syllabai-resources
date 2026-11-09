# Conditional Probability Flashcards

_Lane: `a-level-maths-edexcel` · grade — · 21 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** What event is represented by the notation $A \cap B$?

**Back:** The intersection (both $A$ and $B$ happen).

**Choices:**

- The intersection (both $A$ and $B$ happen). ✔
  - _why:_ An intersection contains outcomes belonging to both events simultaneously. Therefore, $A \cap B$ occurs precisely when $A$ and $B$ both happen.
- The union (at least one of $A$ or $B$ happens).
  - _why:_ A union is represented by $A \cup B$, not $A \cap B$. The intersection $A \cap B$ means that both $A$ and $B$ happen.
- The complement (neither $A$ nor $B$ happens).
  - _why:_ The complement of $A$ is written $A'$ and contains outcomes outside $A$. The notation $A \cap B$ instead represents both events happening.
- The symmetric difference (exactly one of $A$ or $B$ happens).
  - _why:_ Exactly one event happening describes the symmetric difference, not the intersection. The event $A \cap B$ consists of outcomes where both $A$ and $B$ happen.

## Card 2 — `basic`

**Front:** What event is represented by the notation $A \cup B$?

**Back:** The union (at least one of $A$ or $B$ happens).

**Choices:**

- The union (at least one of $A$ or $B$ happens). ✔
  - _why:_ A union includes every outcome in either event, including outcomes in their overlap. Thus, $A \cup B$ occurs when at least one of $A$ or $B$ happens.
- The intersection (both $A$ and $B$ happen).
  - _why:_ An intersection is written $A \cap B$ and requires both events to happen. The notation $A \cup B$ is the union, meaning at least one event happens.
- The symmetric difference (exactly one of $A$ or $B$ happens).
  - _why:_ Restricting the event to exactly one outcome wrongly excludes the overlap where both events happen. The union includes outcomes in $A$, in $B$, or in both.
- The complement (neither $A$ nor $B$ happens).
  - _why:_ Neither event happening is the complement of the union, written $(A \cup B)'$. The event $A \cup B$ means at least one of the events happens.

## Card 3 — `cloze`

**Front:** The general formula for the union of two events is $\text{[...]}$.

**Back:** The general formula for the union of two events is $\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$.

**Choices:**

- $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ✔
  - _why:_ Adding $P(A)$ and $P(B)$ counts their intersection twice, so subtracting $P(A \cap B)$ once gives the probability of every outcome in the union exactly once.
- $$P(A \cup B) = P(A) + P(B)$
  - _why:_ Simply adding the two probabilities double-counts outcomes in the intersection. The general formula must subtract the overlap: $P(A \cup B)=P(A)+P(B)-P(A \cap B)$.
- $$P(A \cup B) = P(A) + P(B) + P(A \cap B)$
  - _why:_ Adding the intersection counts overlapping outcomes three times rather than once. The overlap must be subtracted, giving $P(A \cup B)=P(A)+P(B)-P(A \cap B)$.
- $$P(A \cup B) = P(A) + P(B) - P(A)P(B)$
  - _why:_ Subtracting $P(A)P(B)$ assumes that the overlap equals the product, which is only guaranteed for independent events. The general formula subtracts $P(A \cap B)$ itself.

## Card 4 — `basic`

**Front:** Why must $P(A \cap B)$ be subtracted when calculating $P(A \cup B)$?

**Back:** The overlap is counted twice when adding $P(A)$ and $P(B)$.

**Choices:**

- The overlap is counted twice when adding $P(A)$ and $P(B)$. ✔
  - _why:_ Every outcome in the intersection appears once within $P(A)$ and once within $P(B)$. Subtracting the overlap once ensures that these outcomes contribute only once to the union.
- The exterior is counted twice when adding $P(A)$ and $P(B)$.
  - _why:_ Outcomes outside both events are not included when $P(A)$ and $P(B)$ are added. The subtraction is needed because the overlap is counted twice, not because the exterior is counted.
- The non-overlap is counted twice when adding $P(A)$ and $P(B)$.
  - _why:_ The non-overlapping parts each appear only once in $P(A)+P(B)$. It is the overlapping part $A \cap B$ that appears twice and must be subtracted once.
- The overlap is not counted when adding $P(A)$ and $P(B)$.
  - _why:_ If the overlap were omitted, it would need to be added rather than subtracted. In fact, it is included in both probabilities and therefore counted twice.

## Card 5 — `basic`

**Front:** How can $P(A' \cap B')$ be calculated using $P(A \cup B)$?

**Back:** $$1 - P(A \cup B)$

**Choices:**

- $$1 - P(A \cup B)$ ✔
  - _why:_ By De Morgan’s law, $A' \cap B'$ is the complement of $A \cup B$. Complementary probabilities sum to $1$, so its probability is $1-P(A \cup B)$.
- $$1 - P(A \cap B)$
  - _why:_ This calculates the complement of both events happening, which is $P(A' \cup B')$. For neither event to happen, use the complement of the union: $1-P(A \cup B)$.
- $$P(A \cup B)$
  - _why:_ The union is the event that at least one of $A$ or $B$ happens. The required event is neither happening, so its probability is $1-P(A \cup B)$.
- $$P(A') + P(B')$
  - _why:_ Adding the two complement probabilities can double-count outcomes outside both events and may exceed $1$. De Morgan’s law gives $P(A' \cap B')=1-P(A \cup B)$.

## Card 6 — `cloze`

**Front:** The formula for conditional probability is $P(A|B) = $ $\text{[...]}$.

**Back:** The formula for conditional probability is $P(A|B) = $ $\boxed{\frac{P(A \cap B)}{P(B)}}$.

**Choices:**

- $$\frac{P(A \cap B)}{P(B)}$ ✔
  - _why:_ Conditioning on $B$ restricts the sample space to outcomes in $B$. The favourable outcomes are those in both events, so divide $P(A \cap B)$ by $P(B)$.
- $$\frac{P(A \cap B)}{P(A)}$
  - _why:_ Dividing by $P(A)$ conditions on $A$, producing $P(B|A)$ rather than $P(A|B)$. Conditioning on $B$ requires the denominator $P(B)$.
- $$\frac{P(A \cup B)}{P(B)}$
  - _why:_ Using the union includes outcomes where only one event happens, but conditional probability requires outcomes where both happen. The numerator must be $P(A \cap B)$.
- $$P(A \cap B)P(B)$
  - _why:_ Conditional probability is formed by dividing the intersection by the probability of the conditioning event, not multiplying them. The correct expression is $P(A \cap B)/P(B)$.

## Card 7 — `basic`

**Front:** When calculating $P(B|A)$, which probability is used as the denominator?

**Back:** $$P(A)$

**Choices:**

- $$P(A)$ ✔
  - _why:_ The event after the conditioning bar defines the restricted sample space. Since $P(B|A)$ means the probability of $B$ given $A$, the denominator is $P(A)$.
- $$P(B)$
  - _why:_ Using $P(B)$ as the denominator reverses the conditioning and corresponds to $P(A|B)$. For $P(B|A)$, the given event is $A$, so use $P(A)$.
- $$P(A \cap B)$
  - _why:_ The intersection belongs in the numerator because it represents outcomes satisfying both events. The denominator is the probability of the given event, which is $P(A)$.
- $$1 - P(A)$
  - _why:_ This uses the probability that $A$ does not happen, so it conditions on $A'$ rather than $A$. The denominator for $P(B|A)$ is $P(A)$.

## Card 8 — `basic`

**Front:** How is the intersection $P(A \cap B)$ calculated using a conditional probability?

**Back:** $$P(A|B) \times P(B)$

**Choices:**

- $$P(A|B) \times P(B)$ ✔
  - _why:_ Rearranging $P(A|B)=P(A \cap B)/P(B)$ gives $P(A \cap B)=P(A|B)P(B)$. This multiplies the conditional probability by the probability of its conditioning event.
- $$P(A|B) \times P(A)$
  - _why:_ The multiplier must be the probability of the conditioning event $B$, not the target event $A$. Therefore, the intersection is $P(A|B)P(B)$.
- $$P(A|B) \div P(B)$
  - _why:_ Multiplying by $P(B)$ gives the intersection, whereas dividing by $P(B)$ moves in the wrong direction when rearranging the conditional probability formula.
- $$P(A|B) + P(B)$
  - _why:_ Adding probabilities is not the multiplication rule for an intersection and can even produce a value above $1$. The correct calculation is $P(A|B)P(B)$.

## Card 9 — `cloze`

**Front:** Two events $A$ and $B$ are independent if $\text{[...]}$.

**Back:** Two events $A$ and $B$ are independent if $\boxed{P(A \cap B) = P(A)P(B)}$.

**Choices:**

- $$P(A \cap B) = P(A)P(B)$ ✔
  - _why:_ Independence means that the occurrence of either event does not affect the other. Therefore, the probability that both occur equals the product of their individual probabilities.
- $$P(A \cap B) = P(A)+P(B)$
  - _why:_ Adding probabilities is associated with unions, not intersections of independent events. For independent events, the multiplication rule gives $P(A \cap B)=P(A)P(B)$.
- $$P(A \cap B) = P(A \cup B)$
  - _why:_ Equating the intersection with the union confuses “both events” with “at least one event”. Independence requires $P(A \cap B)=P(A)P(B)$.
- $$P(A \cap B) = P(A)-P(A)P(B)$
  - _why:_ Subtracting the product appears in the general addition rule for a union. The defining relationship for independent events is instead $P(A \cap B)=P(A)P(B)$.

## Card 10 — `basic`

**Front:** What is the value of $P(A \cap B)$ if events $A$ and $B$ are mutually exclusive?

**Back:** 0

**Choices:**

- 0 ✔
  - _why:_ Mutually exclusive events cannot occur together, so their intersection is empty. Consequently, the probability of both $A$ and $B$ occurring is 0.
- 1
  - _why:_ A probability of 1 would mean the two events always occur together, contradicting mutual exclusivity. Since they cannot occur together, $P(A \cap B)=0$.
- $$P(A)$
  - _why:_ The probability of the intersection is not generally the probability of $A$ alone. Mutual exclusivity means the events cannot occur together, so $P(A \cap B)=0$.
- $$P(B)$
  - _why:_ The probability of the intersection is not generally the probability of $B$ alone. Mutually exclusive events have no shared outcomes, so $P(A \cap B)=0$.

## Card 11 — `basic`

**Front:** If $A$ and $B$ are independent, what is the relationship between $P(A|B)$ and $P(A)$?

**Back:** $$P(A|B) = P(A)$

**Choices:**

- $$P(A|B) = P(A)$ ✔
  - _why:_ Independence means that learning $B$ has occurred provides no information that changes the probability of $A$. Thus the conditional and unconditional probabilities are equal.
- $$P(A|B) = P(B)$
  - _why:_ Equating the conditional probability with $P(B)$ swaps the roles of the events. Independence means conditioning on $B$ leaves $A$ unchanged, so $P(A|B)=P(A)$.
- $$P(A|B) = P(A)P(B)$
  - _why:_ Multiplying by $P(B)$ gives the intersection probability for independent events, not the conditional probability. Dividing that intersection by $P(B)$ gives $P(A|B)=P(A)$.
- $$P(A|B) = P(A)+P(B)$
  - _why:_ A conditional probability is not found by adding the individual probabilities. If $A$ and $B$ are independent, knowledge of $B$ changes nothing, so $P(A|B)=P(A)$.

## Card 12 — `basic`

**Front:** If events have non-zero probabilities and are mutually exclusive, why can they not be independent?

**Back:** Knowing one happens makes the probability of the other zero (it changes the probability).

**Choices:**

- Knowing one happens makes the probability of the other zero (it changes the probability). ✔
  - _why:_ Mutual exclusivity means that once one event occurs, the other is impossible, so its conditional probability becomes zero. This differs from its original non-zero probability, contradicting independence.
- Knowing one happens leaves the probability of the other unchanged (it keeps the same probability).
  - _why:_ Leaving the other event’s probability unchanged is precisely the condition for independence. Mutual exclusivity instead makes its conditional probability zero, which differs from its non-zero original probability.
- Knowing one happens makes the probability of the other one (it changes the probability).
  - _why:_ Mutual exclusivity does not make the other event certain; it makes that event impossible. Its conditional probability becomes zero rather than one, so the events cannot be independent.
- Knowing one happens makes the probability of the other smaller (it reduces the probability).
  - _why:_ Mutually exclusive events cannot occur simultaneously, so observing one does not merely reduce the other’s probability. It makes the other event’s conditional probability exactly zero.

## Card 13 — `basic`

**Front:** In a tree diagram, what operation is used to find the probability of a specific path?

**Back:** Multiplication along the branches.

**Choices:**

- Multiplication along the branches. ✔
  - _why:_ A path represents a sequence of events occurring together. The multiplication rule combines the successive branch probabilities to give the probability of that complete path.
- Addition along the branches.
  - _why:_ Adding is used to combine probabilities from separate alternative paths, not successive branches on one path. A specific path’s probability is found by multiplication along its branches.
- Division along the branches.
  - _why:_ Division is used when forming a conditional probability from a joint probability, not when following a tree path. Probabilities along a specific path are multiplied.
- Subtraction along the branches.
  - _why:_ Subtraction may find a complementary probability, but it does not combine successive stages of a path. The probability of a specific tree path is found using multiplication.

## Card 14 — `basic`

**Front:** In a tree diagram, how do you find the total probability of an outcome that occurs on multiple separate paths?

**Back:** Add the probabilities of those paths.

**Choices:**

- Add the probabilities of those paths. ✔
  - _why:_ Separate paths represent mutually exclusive ways for the outcome to occur. After calculating each path probability, add them to obtain the outcome’s total probability.
- Multiply the probabilities of those paths.
  - _why:_ Multiplication combines probabilities along successive branches within one path. When the same outcome occurs on separate alternative paths, their completed path probabilities must be added.
- Subtract the probabilities of those paths.
  - _why:_ Subtracting path probabilities would remove one possible way the outcome can occur. Because the paths are separate alternatives, their probabilities should be added to find the total.
- Average the probabilities of those paths.
  - _why:_ Averaging treats the paths as repeated measurements rather than distinct ways an outcome can happen. The total probability is found by adding all relevant path probabilities.

## Card 15 — `cloze`

**Front:** To calculate $P(\text{Machine } C|\text{Faulty})$ from a tree diagram, you divide $\text{[...]}$ by the total $P(\text{Faulty})$.

**Back:** To calculate $P(\text{Machine } C|\text{Faulty})$ from a tree diagram, you divide $\boxed{P(\text{Machine } C \cap \text{Faulty})}$ by the total $P(\text{Faulty})$.

**Choices:**

- $$P(\text{Machine } C \cap \text{Faulty})$ ✔
  - _why:_ Conditional probability uses the joint event in the numerator. Here, the relevant joint event is that the item came from Machine $C$ and is faulty.
- $$P(\text{Machine } C)$
  - _why:_ Using $P(\text{Machine } C)$ includes both faulty and non-faulty items from Machine $C$. The numerator must count only items satisfying both conditions: $P(\text{Machine } C \cap \text{Faulty})$.
- $$P(\text{Faulty})$
  - _why:_ Using $P(\text{Faulty})$ in both numerator and denominator would give 1. The numerator must be the joint probability $P(\text{Machine } C \cap \text{Faulty})$.
- $$P(\text{Machine } C \cup \text{Faulty})$
  - _why:_ The union includes items that came from Machine $C$ or are faulty, including those meeting only one condition. Conditional probability requires the intersection in the numerator.

## Card 16 — `cloze`

**Front:** To calculate $P(\text{Machine } C|\text{Faulty})$ from a tree diagram, you divide $P(\text{Machine } C \cap \text{Faulty})$ by the [ ___ ].

**Back:** To calculate $P(\text{Machine } C|\text{Faulty})$ from a tree diagram, you divide $P(\text{Machine } C \cap \text{Faulty})$ by the total $P(\text{Faulty})$.

**Choices:**

- total $P(\text{Faulty})$ ✔
  - _why:_ Conditioning on an item being faulty restricts the sample space to all faulty items. Therefore, the joint probability is divided by the total probability of being faulty.
- total $P(\text{Machine } C)$
  - _why:_ Dividing by the probability of Machine $C$ would calculate $P(\text{Faulty}|\text{Machine } C)$, reversing the condition. The required denominator is the total $P(\text{Faulty})$.
- total $P(\text{Machine } C \cap \text{Faulty})$
  - _why:_ Dividing the joint probability by itself would always give 1. The denominator must represent the conditioning event, so it is the total $P(\text{Faulty})$.
- total $P(\text{not Faulty})$
  - _why:_ Using the probability of not being faulty conditions on the opposite event. Since the question assumes the item is faulty, divide by the total $P(\text{Faulty})$.

## Card 17 — `basic`

**Front:** How do probabilities change on branches if a selection is made without replacement?

**Back:** Both the favourable outcomes and the total outcomes decrease for the second selection.

**Choices:**

- Both the favourable outcomes and the total outcomes decrease for the second selection. ✔
  - _why:_ Without replacement, the selected item is not returned. Consequently, one favourable item and one item overall are removed before the probability for the second selection is calculated.
- Both the favourable outcomes and the total outcomes remain unchanged for the second selection.
  - _why:_ Keeping both counts unchanged incorrectly models selection with replacement. Without replacement, the selected favourable item is removed, reducing both the favourable count and the total count.
- Both the favourable outcomes and the total outcomes increase for the second selection.
  - _why:_ Removing an item cannot increase either count. Without replacement, the selected favourable item is removed, so both the favourable outcomes and total outcomes decrease.
- The favourable outcomes decrease but the total outcomes increase for the second selection.
  - _why:_ The total cannot increase because an item has been removed rather than added. Both the favourable count and the overall total decrease before the second selection.

## Card 18 — `basic`

**Front:** When filling a three-event Venn diagram, which region should be filled first?

**Back:** The centre overlap (where all three events happen).

**Choices:**

- The centre overlap (where all three events happen). ✔
  - _why:_ The centre belongs to all three events and contributes to every pairwise overlap. Filling it first prevents its members from being counted repeatedly in surrounding regions.
- The single-event regions (where only one event happens).
  - _why:_ Starting with single-event regions ignores the contributions from overlapping sets and can lead to incorrect subtraction. The centre shared by all three events should be filled first.
- The pairwise overlaps (where exactly two events happen).
  - _why:_ Each pairwise total may include the central three-way overlap, so entering these regions first risks double-counting it. The centre overlap should therefore be filled first.
- The outside region (where none of the events happen).
  - _why:_ The number outside all events is normally found after the event regions have been completed. Begin with the centre overlap, which affects all three sets.

## Card 19 — `basic`

**Front:** A Venn diagram shows 14 people watch Football and Golf. 6 people watch Football, Golf, and Hockey. How many watch only Football and Golf?

**Back:** 8 ($14 - 6$).

**Choices:**

- 8 ($14 - 6$). ✔
  - _why:_ The 14-person Football-and-Golf intersection includes the six people who also watch Hockey. Removing that centre overlap leaves $14-6=8$ who watch only Football and Golf.
- 14 ($14$).
  - _why:_ This retains the entire Football-and-Golf intersection and fails to remove the six people also watching Hockey. Subtracting the three-way overlap gives $14-6=8$.
- 20 ($14 + 6$).
  - _why:_ Adding the three-way overlap double-counts people who are already included among the 14 watching Football and Golf. It must be subtracted, giving $14-6=8$.
- 6 ($6$).
  - _why:_ Six is the number in the three-way overlap, not the number watching only Football and Golf. Removing those six from the total of 14 leaves eight.

## Card 20 — `cloze`

**Front:** The event $A' \cup B'$ is equivalent to not having [ ___ ] ($P(A' \cup B') = 1 - P(A \cap B)$).

**Back:** The event $A' \cup B'$ is equivalent to not having both $A$ and $B$ ($P(A' \cup B') = 1 - P(A \cap B)$).

**Choices:**

- both $A$ and $B$ ✔
  - _why:_ By De Morgan’s law, $A'\cup B'=(A\cap B)'$. Thus the union of the complements means that $A$ and $B$ do not both occur.
- exactly one of $A$ and $B$
  - _why:_ Not having exactly one includes cases where both events occur, so it cannot describe $A'\cup B'$. By De Morgan’s law, the missing term is both $A$ and $B$.
- at least one of $A$ and $B$
  - _why:_ Not having at least one of the events means neither event occurs, which is $A'\cap B'$. The required complement is instead not having both $A$ and $B$.
- both $A'$ and $B'$
  - _why:_ Not having both complements is $(A'\cap B')'=A\cup B$, which reverses the required relationship. $A'\cup B'$ means not having both $A$ and $B$.

## Card 21 — `basic`

**Front:** What is the most efficient way to calculate the probability of "at least one" event occurring?

**Back:** $$1 - P(\text{none})$

**Choices:**

- $$1 - P(\text{none})$ ✔
  - _why:_ At least one occurring is the complement of none occurring. Complementary probabilities sum to one, so subtracting $P(\text{none})$ from one is usually most efficient.
- $$P(\text{none})$
  - _why:_ This calculates the probability that no events occur, which is the complement of the required outcome. At least one therefore has probability $1-P(\text{none})$.
- $$1 - P(\text{all})$
  - _why:_ The complement of all events occurring includes many outcomes, not specifically those where at least one occurs. The useful complementary event is none occurring, giving $1-P(\text{none})$.
- $$P(\text{all})$
  - _why:_ The probability that all events occur counts only their common outcome and omits cases where some but not all occur. Use the complement formula $1-P(\text{none})$.
