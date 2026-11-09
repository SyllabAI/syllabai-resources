# Probability Trees Flashcards

_Lane: `igcse-maths-edexcel` · grade 6 · 22 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** What must the probabilities on all branches originating from a single point (split) add up to?

**Back:** 1

**Choices:**

- 1 ✔
  - _why:_ The branches represent every possible outcome after that split, so their probabilities must total 1, corresponding to certainty that one of those outcomes occurs.
- 0
  - _why:_ A total of 0 would mean that none of the possible outcomes can occur. Since the branches cover all outcomes at the split, their probabilities must add to 1.
- 0.5
  - _why:_ The total is not automatically 0.5 when there are two branches; individual probabilities may vary. All branches from a single split must add to 1.
- 100
  - _why:_ This confuses a probability with a percentage value. Probabilities written as decimals or fractions add to 1, while probabilities written as percentages add to 100%.

## Card 2 — `basic`

**Front:** If the probability of an event happening is $p$, what is the probability of the event not happening?

**Back:** $$1 - p$

**Choices:**

- $$1 - p$ ✔
  - _why:_ An event and its complement cover all possible outcomes, so their probabilities add to 1. Therefore, the probability that the event does not happen is $1-p$.
- $$1 + p$
  - _why:_ Adding $p$ can produce a value greater than 1, which is impossible for a probability. The complementary probability is found by subtracting $p$ from 1.
- $$p - 1$
  - _why:_ Reversing the subtraction usually produces a negative value, which cannot be a probability. The probability of the event not happening is $1-p$.
- $$rac{1}{p}$
  - _why:_ Taking the reciprocal does not find a complementary probability and may give a result greater than 1. The event and its complement must sum to 1, giving $1-p$.

## Card 3 — `cloze`

**Front:** The general formula for the probability of an event is: $\text{[...]}$

**Back:** The general formula for the probability of an event is: $\boxed{\frac{\text{number of successful outcomes}}{\text{total number of outcomes}}}$

**Choices:**

- $$\frac{\text{number of successful outcomes}}{\text{total number of outcomes}}$ ✔
  - _why:_ For equally likely outcomes, probability is calculated by dividing the number of outcomes that satisfy the event by the total number of possible outcomes.
- $$\frac{\text{total number of outcomes}}{\text{number of successful outcomes}}$
  - _why:_ This reverses the fraction and can produce a value greater than 1. Probability is successful outcomes divided by the total number of outcomes.
- $$\frac{\text{number of unsuccessful outcomes}}{\text{total number of outcomes}}$
  - _why:_ This calculates the probability of the event not occurring by counting unsuccessful outcomes. The required probability uses the number of successful outcomes as the numerator.
- $$\frac{\text{number of successful outcomes}}{\text{number of unsuccessful outcomes}}$
  - _why:_ This compares successful outcomes only with unsuccessful ones, rather than with every possible outcome. The denominator must be the total number of outcomes.

## Card 4 — `basic`

**Front:** When is a probability tree diagram preferred over a simple probability calculation?

**Back:** When there is a sequence of events or more than one stage.

**Choices:**

- When there is a sequence of events or more than one stage. ✔
  - _why:_ A probability tree clearly represents successive stages and shows how each event branches into later possibilities, making multi-stage probability calculations easier to organise.
- When there is a single event or only one possible outcome.
  - _why:_ A single event or one possible outcome does not usually need a branching diagram. Probability trees are preferred for a sequence of events or more than one stage.
- When there are equally likely outcomes or no later stages.
  - _why:_ Equally likely outcomes alone do not require a tree, especially when there are no subsequent stages. Trees are useful when events occur in sequence across multiple stages.
- When there is a single calculation or only one stage.
  - _why:_ A one-stage calculation can normally be completed directly without a tree. A probability tree is preferred when there is a sequence of events or more than one stage.

## Card 5 — `basic`

**Front:** How do you calculate the probability of a single complete path through a probability tree?

**Back:** Multiply the probabilities along the branches of that path.

**Choices:**

- Multiply the probabilities along the branches of that path. ✔
  - _why:_ A complete path represents events occurring together in sequence, so the multiplication rule is used to find the probability of following every branch on that path.
- Add the probabilities along the branches of that path.
  - _why:_ Adding is used to combine probabilities from separate alternative paths, not branches within one path. For a single complete path, multiply the branch probabilities.
- Subtract the probabilities along the branches of that path.
  - _why:_ Subtraction is associated with complements, such as finding a probability from 1. A complete path represents successive events, so its branch probabilities are multiplied.
- Divide the probabilities along the branches of that path.
  - _why:_ Division does not combine the successive events represented by a path. To find the probability that all stages on that path occur, multiply their branch probabilities.

## Card 6 — `basic`

**Front:** What defines two events as being independent?

**Back:** The outcome of the first event does not change the probabilities of the second event.

**Choices:**

- The outcome of the first event does not change the probabilities of the second event. ✔
  - _why:_ Independent events do not influence one another, so knowing the outcome of the first event leaves the probabilities at the second stage unchanged.
- The outcome of the first event does change the probabilities of the second event.
  - _why:_ This describes dependent events, where the first result affects later probabilities. For independent events, the first outcome does not change the probabilities of the second event.
- The outcome of the first event determines exactly the outcome of the second event.
  - _why:_ If the first outcome fixes the second, the events are strongly dependent rather than independent. Independence means the first event does not change second-event probabilities.
- The outcome of the first event must match the outcome of the second event.
  - _why:_ Matching outcomes are not a requirement for independence and may indicate a relationship between events. Independent events are defined by one outcome not changing the other’s probabilities.

## Card 7 — `cloze`

**Front:** If an item is taken from a bag and not replaced, the probabilities for the next stage of the tree will [ ___ ].

**Back:** If an item is taken from a bag and not replaced, the probabilities for the next stage of the tree will change.

**Choices:**

- change ✔
  - _why:_ Without replacement, the bag’s contents and total number of items are altered. This changes the fractions used for the probabilities at the next stage.
- stay constant
  - _why:_ Probabilities stay constant when replacement restores the original contents. Without replacement, both the available outcomes and total number of items change, so the next probabilities change.
- remain equal
  - _why:_ The next-stage probabilities are not necessarily equal because one item has been removed. Without replacement, the composition of the bag changes, so the probabilities change.
- return to zero
  - _why:_ Removing an item does not make all later outcomes impossible. The remaining items still have positive probabilities, but those probabilities change because the bag’s contents have changed.

## Card 8 — `basic`

**Front:** If a question asks for the probability of "different colours" over two stages, how do you combine the relevant paths?

**Back:** Add the individual path probabilities together.

**Choices:**

- Add the individual path probabilities together. ✔
  - _why:_ Different colours can occur through alternative complete paths, such as red then blue or blue then red. Add these mutually exclusive path probabilities to obtain the overall probability.
- Multiply the individual path probabilities together.
  - _why:_ Multiplication finds the probability along each individual path, not the total across alternative paths. After calculating each different-colour path, add their probabilities together.
- Subtract the individual path probabilities from one another.
  - _why:_ The relevant paths are alternative ways to obtain different colours, so neither should be removed from the other. Calculate each path probability and add them together.
- Divide the individual path probabilities by one another.
  - _why:_ Division does not combine alternative outcomes on a probability tree. Different-colour paths are separate mutually exclusive possibilities, so their individual probabilities must be added together.

## Card 9 — `basic`

**Front:** What is the most efficient way to calculate the probability of at least one success over multiple trials?

**Back:** Calculate $1 - P(\text{none})$.

**Choices:**

- Calculate $1 - P(\text{none})$. ✔
  - _why:_ The event “at least one success” is the complement of no successes. Therefore, subtracting the probability of no successes from 1 gives the required probability.
- Calculate $P(\text{none})$.
  - _why:_ This finds the probability of no successes, not at least one success. The required complementary probability is calculated using $1 - P(\text{none})$.
- Calculate $1 - P(\text{exactly one})$.
  - _why:_ Exactly one success is not the complement of at least one success, because two or more successes are also included. The complement is no successes, so use $1 - P(\text{none})$.
- Add the probability of success on every trial.
  - _why:_ Simply adding individual success probabilities can double-count outcomes and may produce a value above 1. The efficient method is to calculate $1 - P(\text{none})$.

## Card 10 — `cloze`

**Front:** The [ ___ ] of an event refers to the probability that the event does not happen.

**Back:** The complement of an event refers to the probability that the event does not happen.

**Choices:**

- complement ✔
  - _why:_ An event and its complement cover all possible outcomes without overlapping. Their probabilities therefore add to 1, so the complement represents the event not happening.
- intersection
  - _why:_ An intersection describes two or more events occurring together, usually represented by AND. The probability that an event does not happen is called its complement.
- union
  - _why:_ A union describes outcomes belonging to either of two events and is associated with OR. The probability that a particular event does not happen is its complement.
- sample space
  - _why:_ The sample space is the set of all possible outcomes, rather than the probability of an event not occurring. That non-occurrence is represented by the complement.

## Card 11 — `cloze`

**Front:** The complement of an event refers to the probability that the event [ ___ ].

**Back:** The complement of an event refers to the probability that the event does not happen.

**Choices:**

- does not happen ✔
  - _why:_ The complement contains every outcome outside the original event. It therefore represents the probability that the specified event does not occur.
- does happen
  - _why:_ This describes the original event rather than its complement. The complement refers to all outcomes for which the event does not happen.
- must happen
  - _why:_ An event that must happen is a certain event with probability 1, not a general complement. A complement describes the event not happening.
- cannot happen
  - _why:_ An event that cannot happen is an impossible event with probability 0. A complement instead gives the probability that the original event does not happen.

## Card 12 — `basic`

**Front:** A bag contains 5 red and 3 blue counters. Why is the probability of picking red $\frac{5}{8}$ and not $\frac{5}{3}$?

**Back:** Probabilities must be calculated using the total number of outcomes ($5 + 3 = 8$).

**Choices:**

- Probabilities must be calculated using the total number of outcomes ($5 + 3 = 8$). ✔
  - _why:_ There are eight counters altogether, and five of these are red. Probability is favourable outcomes divided by total outcomes, giving $P(\text{red})=\frac{5}{8}$.
- Probabilities must be calculated using the number of blue outcomes ($3$).
  - _why:_ Using only the three blue counters as the denominator confuses unfavourable outcomes with total outcomes. The denominator must be all eight counters, giving $\frac{5}{8}$.
- Probabilities must be calculated using the number of red outcomes ($5$).
  - _why:_ Using the five red counters as both numerator and denominator would incorrectly give probability 1. The denominator is the total of eight counters, so the probability is $\frac{5}{8}$.
- Probabilities must be calculated using the product of the outcomes ($5 \times 3 = 15$).
  - _why:_ Multiplying the red and blue counts does not give the number of possible single-counter outcomes. Add the counts to get eight, making the probability $\frac{5}{8}$.

## Card 13 — `basic`

**Front:** Calculate the probability of picking two blue counters if Bag A has $P(\text{blue}) = \frac{2}{5}$ and Bag B has $P(\text{blue}) = \frac{3}{5}$.

**Back:** $$\frac{2}{5} \times \frac{3}{5} = \frac{6}{25}$

**Choices:**

- $$\frac{2}{5} \times \frac{3}{5} = \frac{6}{25}$ ✔
  - _why:_ Both blue selections must occur, so the probabilities along the relevant tree path are multiplied. Thus $\frac{2}{5}\times\frac{3}{5}=\frac{6}{25}$.
- $$\frac{2}{5} + \frac{3}{5} = 1$
  - _why:_ Adding is used to combine alternative paths, not two events that must both occur. For blue from A and blue from B, multiply to obtain $\frac{6}{25}$.
- $$\frac{2}{5} \times \frac{3}{5} = \frac{6}{10}$
  - _why:_ The numerators have been multiplied but the denominators have been added. Multiplying fractions requires multiplying both parts, so the denominator is $5\times5=25$ and the answer is $\frac{6}{25}$.
- $$\frac{2}{5} \times \frac{2}{5} = \frac{4}{25}$
  - _why:_ This incorrectly uses Bag A’s blue probability for both selections. Bag B has blue probability $\frac{3}{5}$, so the correct product is $\frac{2}{5}\times\frac{3}{5}=\frac{6}{25}$.

## Card 14 — `cloze`

**Front:** In probability tree problems, AND situations usually require [ ___ ] while OR situations require addition.

**Back:** In probability tree problems, AND situations usually require multiplication while OR situations require addition.

**Choices:**

- multiplication ✔
  - _why:_ An AND situation follows a complete path through the probability tree. Multiplying the branch probabilities gives the joint probability that every event on that path occurs.
- addition
  - _why:_ Addition usually combines alternative, mutually exclusive paths associated with OR. When events on one path must both happen, their branch probabilities are combined by multiplication.
- subtraction
  - _why:_ Subtracting probabilities is generally used for complements or differences, not for events that must occur together. AND probabilities along a tree path are found by multiplication.
- division
  - _why:_ Division can be relevant when finding conditional probabilities from known values, but it does not combine branches along a path. AND situations normally require multiplication.

## Card 15 — `cloze`

**Front:** In probability tree problems, AND situations usually require multiplication while OR situations require [ ___ ].

**Back:** In probability tree problems, AND situations usually require multiplication while OR situations require addition.

**Choices:**

- addition ✔
  - _why:_ An OR situation combines alternative outcomes or complete paths. When those alternatives are mutually exclusive, their probabilities are added to find the overall probability.
- multiplication
  - _why:_ Multiplication combines successive events along one path and therefore represents AND. Alternative mutually exclusive paths representing OR are combined using addition.
- subtraction
  - _why:_ Subtraction is useful for complements, such as finding $1-P(A)$, but it does not combine alternative successful paths. OR situations normally require addition.
- division
  - _why:_ Division is not the standard operation for combining alternative outcomes in a probability tree. The probabilities of mutually exclusive OR paths are added together.

## Card 16 — `basic`

**Front:** If $P(\text{Win}) = 0.5$ and $P(\text{Draw}) = 0.2$ for a game, what is the probability of losing?

**Back:** $$1 - 0.5 - 0.2 = 0.3$

**Choices:**

- $$1 - 0.5 - 0.2 = 0.3$ ✔
  - _why:_ Winning, drawing and losing are mutually exclusive and exhaustive, so their probabilities total 1. Subtracting $0.5$ and $0.2$ leaves a losing probability of $0.3$.
- $$0.5 + 0.2 = 0.7$
  - _why:_ Adding $0.5$ and $0.2$ gives the probability of winning or drawing, not losing. Losing is the complement, so its probability is $1-0.7=0.3$.
- $$1 - 0.5 = 0.5$
  - _why:_ This subtracts only the winning probability and incorrectly includes draws with losses. Both winning and drawing must be removed from 1, leaving $0.3$.
- $$1 - 0.2 = 0.8$
  - _why:_ This subtracts only the drawing probability and incorrectly includes wins with losses. Subtract both $0.5$ and $0.2$ from 1 to obtain $0.3$.

## Card 17 — `basic`

**Front:** The probability of a train being late is 0.3. Calculate the probability it is late on at least one of two days.

**Back:** $P(\text{not late}) = 0.7$$P(\text{never late}) = 0.7 \times 0.7 = 0.49$$1 - 0.49 = 0.51$

**Choices:**

- $P(\text{not late}) = 0.7$$P(\text{never late}) = 0.7 \times 0.7 = 0.49$$1 - 0.49 = 0.51$ ✔
  - _why:_ The complement of being late at least once is never being late. Assuming the days are independent, this has probability $0.7^2=0.49$, so the required probability is $1-0.49=0.51$.
- $P(\text{late}) = 0.3$$P(\text{late twice}) = 0.3 \times 0.3 = 0.09$$P(\text{at least once}) = 0.09$
  - _why:_ Multiplying $0.3$ by $0.3$ finds the probability that the train is late on both days, not at least one day. Using the complement gives $1-0.7^2=0.51$.
- $P(\text{late}) = 0.3$$P(\text{late on either day}) = 0.3 + 0.3 = 0.6$$P(\text{at least once}) = 0.6$
  - _why:_ Adding the two daily probabilities double-counts the outcome in which the train is late on both days. The complement method avoids this overlap and gives $1-0.7^2=0.51$.
- $P(\text{late}) = 0.3$$P(\text{late twice}) = 0.3 \times 0.3 = 0.09$$1 - 0.09 = 0.91$
  - _why:_ Subtracting the probability of two late days finds the probability that the train is not late on both days. The required complement is never late, so the answer is $1-0.7^2=0.51$.

## Card 18 — `basic`

**Front:** What should you check at every "split" in a probability tree before starting calculations?

**Back:** Check that the probabilities of the branches coming out add to 1.

**Choices:**

- Check that the probabilities of the branches coming out add to 1. ✔
  - _why:_ Branches leaving the same split represent all mutually exclusive possible outcomes. Their probabilities must therefore total 1, allowing a missing branch probability to be found by subtraction.
- Check that the probabilities of the branches coming out multiply to 1.
  - _why:_ Multiplication is used along a path through successive events, not between branches at one split. Probabilities leaving any single split must add to 1 because they cover all outcomes.
- Check that the probabilities of the branches coming out add to 0.
  - _why:_ A total of 0 would mean that none of the outcomes can occur. Since the branches represent every possible outcome at that split, their probabilities must add to 1.
- Check that the probabilities of the branches coming out are all equal.
  - _why:_ Branches are equal only when the outcomes are equally likely, which is not generally true. The universal check is that all probabilities leaving the same split add to 1.

## Card 19 — `cloze`

**Front:** For two trials, the opposite (complement) of "at least one success" is [ ___ ].

**Back:** For two trials, the opposite (complement) of "at least one success" is no successes.

**Choices:**

- no successes ✔
  - _why:_ The event “at least one success” includes exactly one success and two successes. Its complement contains the only remaining possibility, which is obtaining no successes in the two trials.
- two successes
  - _why:_ Two successes is included within “at least one success”, so it cannot be its complement. The opposite event must exclude every success outcome and is therefore no successes.
- one success
  - _why:_ Exactly one success is one of the outcomes covered by “at least one success”, rather than its opposite. The complement is no successes across the two trials.
- at least one failure
  - _why:_ At least one failure can occur alongside one success, so it overlaps with “at least one success”. The true complement contains no overlap and is no successes.

## Card 20 — `basic`

**Front:** Sofia wears a blue scarf with $P = \frac{3}{7}$ or a white scarf. Calculate the probability she wears different colours on Monday and Tuesday.

**Back:** $P(\text{Blue, White}) = \frac{3}{7} \times \frac{4}{7} = \frac{12}{49}$$P(\text{White, Blue}) = \frac{4}{7} \times \frac{3}{7} = \frac{12}{49}$$\frac{12}{49} + \frac{12}{49} = \frac{24}{49}$

**Choices:**

- $P(\text{Blue, White}) = \frac{3}{7} \times \frac{4}{7} = \frac{12}{49}$$P(\text{White, Blue}) = \frac{4}{7} \times \frac{3}{7} = \frac{12}{49}$$\frac{12}{49} + \frac{12}{49} = \frac{24}{49}$ ✔
  - _why:_ Different colours can occur in two mutually exclusive orders: blue then white, or white then blue. Each has probability $\frac{12}{49}$, so adding them gives $\frac{24}{49}$.
- $P(\text{Blue, Blue}) = \frac{3}{7} \times \frac{3}{7} = \frac{9}{49}$$P(\text{White, White}) = \frac{4}{7} \times \frac{4}{7} = \frac{16}{49}$$\frac{9}{49} + \frac{16}{49} = \frac{25}{49}$
  - _why:_ These paths describe wearing the same colour on both days, the complement of the required event. The two different-colour paths total $\frac{12}{49}+\frac{12}{49}=\frac{24}{49}$.
- $P(\text{Blue, White}) = \frac{3}{7} \times \frac{4}{7} = \frac{12}{49}$$P(\text{White, Blue}) = \frac{4}{7} \times \frac{3}{7} = \frac{12}{49}$$\frac{12}{49} \times \frac{12}{49} = \frac{144}{2401}$
  - _why:_ Multiplication is used along each path, but alternative mutually exclusive paths must be added. Adding blue-white and white-blue gives $\frac{12}{49}+\frac{12}{49}=\frac{24}{49}$.
- $P(\text{Blue, White}) = \frac{3}{7} \times \frac{4}{6} = \frac{2}{7}$$P(\text{White, Blue}) = \frac{4}{7} \times \frac{3}{6} = \frac{2}{7}$$\frac{2}{7} + \frac{2}{7} = \frac{4}{7}$
  - _why:_ Changing the denominator to 6 incorrectly treats the scarf choice as sampling without replacement. The daily probabilities remain $\frac{3}{7}$ and $\frac{4}{7}$, giving $\frac{24}{49}$ overall.

## Card 21 — `basic`

**Front:** What do probabilities of 0 and 1 represent respectively?

**Back:** 0 = impossible1 = certain

**Choices:**

- 0 = impossible1 = certain ✔
  - _why:_ Probability 0 means an event cannot occur, while probability 1 means it must occur. All probabilities lie between these endpoints, inclusive.
- 0 = certain1 = impossible
  - _why:_ This reverses the probability scale. A probability of 0 represents an impossible event, whereas a probability of 1 represents an event that is certain to occur.
- 0 = unlikely1 = likely
  - _why:_ “Unlikely” and “likely” describe probabilities near the endpoints, not the endpoints themselves. Exactly 0 means impossible, and exactly 1 means certain.
- 0 = even chance1 = certain
  - _why:_ An even chance has probability $0.5$, not 0. Probability 0 means impossible, while probability 1 correctly represents certainty.

## Card 22 — `basic`

**Front:** Amir wins table tennis with $P = 0.6$ and darts with $P = 0.75$. Calculate the probability he wins both games.

**Back:** $$0.6 \times 0.75 = 0.45$

**Choices:**

- $$0.6 \times 0.75 = 0.45$ ✔
  - _why:_ Winning both games means following the win branch for table tennis and the win branch for darts. Multiplying the independent probabilities gives $0.6\times0.75=0.45$.
- $$0.6 + 0.75 = 1.35$
  - _why:_ Adding the probabilities does not find the chance of both events and produces a value above 1, which is impossible for a probability. Multiply instead to obtain $0.45$.
- $$0.6 \times 0.75 = 0.045$
  - _why:_ The multiplication has a decimal-place error: $6\times75=450$, with three decimal places in total, giving $0.450$. Therefore, the probability is $0.45$.
- $$1 - (0.4 \times 0.25) = 0.9$
  - _why:_ This subtracts the probability of losing both games, so it finds winning at least one game. Winning both requires multiplying the two win probabilities, giving $0.6\times0.75=0.45$.
