# Probability Trees Flashcards

_Lane: `gcse-maths-edexcel` · grade 5 · 24 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** If $P(\text{win}) = 0.65$, what probability is assigned to the complement branch?

**Back:** $$1 - 0.65 = 0.35$

**Choices:**

- $$1 - 0.65 = 0.35$ ✔
  - _why:_ An event and its complement have probabilities summing to 1. Subtracting the winning probability from 1 therefore gives $P(\text{not win}) = 0.35$.
- $$1 - 0.65 = 0.45$
  - _why:_ This contains a subtraction error: $1.00 - 0.65$ is $0.35$, not $0.45$. Complementary branches must have probabilities that add exactly to 1.
- $$1 - 0.65 = 0.65$
  - _why:_ This incorrectly assumes that the two branches are equally likely. The complement is found by subtraction, so its probability is $1 - 0.65 = 0.35$.
- $$1 + 0.65 = 1.65$
  - _why:_ This adds the event probability instead of subtracting it from 1. A complement probability cannot exceed 1 and is $1 - 0.65 = 0.35$.

## Card 2 — `cloze`

**Front:** The sum of an event and its [ ___ ] (not that event) always equals 1.

**Back:** The sum of an event and its complement (not that event) always equals 1.

**Choices:**

- complement ✔
  - _why:_ The complement of an event includes every outcome where that event does not happen. Together, an event and its complement cover all outcomes, so their probabilities sum to 1.
- intersection
  - _why:_ An intersection contains outcomes shared by two events; it is not the set of outcomes where an event does not occur. The required term is complement.
- union
  - _why:_ A union combines outcomes belonging to either of two events, rather than describing all outcomes outside one event. The term for “not that event” is complement.
- frequency
  - _why:_ Frequency records how often an outcome occurs and is not the opposite of an event. The event consisting of all outcomes where it does not happen is its complement.

## Card 3 — `cloze`

**Front:** The sum of an event and its complement (not that event) always equals [ ___ ].

**Back:** The sum of an event and its complement (not that event) always equals 1.

**Choices:**

- 1 ✔
  - _why:_ An event and its complement cover every possible outcome without overlapping. Their probabilities therefore account for the whole sample space and must sum to 1.
- 0
  - _why:_ A total of 0 would mean that neither the event nor its complement could occur, although together they cover every outcome. Their probabilities must sum to 1.
- 0.5
  - _why:_ This assumes the event and its complement account for only half of all outcomes. Together they cover the complete sample space, so their probabilities always sum to 1.
- 2
  - _why:_ This treats both probabilities as if each must equal 1. Although either probability can individually reach 1, an event and its complement must have a combined probability of 1.

## Card 4 — `basic`

**Front:** What is the rule for the sum of probabilities at any single split in a tree?

**Back:** They must add to 1.

**Choices:**

- They must add to 1. ✔
  - _why:_ The branches at one split represent all mutually exclusive next outcomes. Since one of those outcomes must occur, their probabilities must add to 1.
- They must add to 0.
  - _why:_ Probabilities at a split cannot total 0 because that would make every next outcome impossible. The branches cover all possible next outcomes, so they add to 1.
- They must multiply to 1.
  - _why:_ Multiplication is used along a complete route, not between alternative branches at one split. Probabilities on branches leaving the same point must add to 1.
- They must multiply to 0.
  - _why:_ This confuses combining outcomes at a split with calculating a route probability. Alternative branches are added and must total 1; multiplication is used along successive branches.

## Card 5 — `basic`

**Front:** Define independent events in the context of probability trees.

**Back:** Events where the result of the first does not change the probabilities for the second.

**Choices:**

- Events where the result of the first does not change the probabilities for the second. ✔
  - _why:_ For independent events, knowing the first result gives no new information about the second. Consequently, the probabilities on the second-stage branches remain unchanged after every first result.
- Events where the result of the first always changes the probabilities for the second.
  - _why:_ This describes dependent events, where the first result affects what can happen next. For independent events, the probabilities for the second event do not change.
- Events where the result of the first determines exactly the result of the second.
  - _why:_ If the first result fixes the second result, the events are strongly dependent. Independent events require the second event’s probabilities to remain unaffected by the first result.
- Events where the result of the first equals the probability of the second.
  - _why:_ This incorrectly compares an outcome with a probability, which are different quantities. Independence means the first result does not alter the probabilities assigned to the second event.

## Card 6 — `basic`

**Front:** A bag contains 2 red and 6 blue counters. What labels go on the first set of branches?

**Back:** $P(\text{Red}) = \frac{2}{8}$ (or $\frac{1}{4}$)$P(\text{Blue}) = \frac{6}{8}$ (or $\frac{3}{4}$)

**Choices:**

- $P(\text{Red}) = \frac{2}{8}$ (or $\frac{1}{4}$)$P(\text{Blue}) = \frac{6}{8}$ (or $\frac{3}{4}$) ✔
  - _why:_ There are 8 counters altogether. Probability is the number of counters of the required colour divided by 8, giving $2/8$ for red and $6/8$ for blue.
- $P(\text{Red}) = \frac{6}{8}$ (or $\frac{3}{4}$)$P(\text{Blue}) = \frac{2}{8}$ (or $\frac{1}{4}$)
  - _why:_ This swaps the colour frequencies. Only 2 of the 8 counters are red and 6 are blue, so the correct probabilities are $2/8$ and $6/8$ respectively.
- $P(\text{Red}) = \frac{2}{6}$ (or $\frac{1}{3}$)$P(\text{Blue}) = \frac{6}{6}$ (or $1$)
  - _why:_ This uses the number of blue counters as the denominator instead of the total number of counters. Both probabilities need denominator 8, giving $2/8$ and $6/8$.
- $P(\text{Red}) = \frac{2}{10}$ (or $\frac{1}{5}$)$P(\text{Blue}) = \frac{6}{10}$ (or $\frac{3}{5}$)
  - _why:_ This incorrectly adds the two colour counts to each numerator when forming the denominator. There are $2 + 6 = 8$ counters, so the denominator must be 8.

## Card 7 — `basic`

**Front:** How do you calculate the probability of one complete route (e.g. "win and win")?

**Back:** Multiply the probabilities along the branches of that route.

**Choices:**

- Multiply the probabilities along the branches of that route. ✔
  - _why:_ A complete route represents events happening together in sequence, such as win and win. The multiplication rule gives its probability by multiplying all branch probabilities along that route.
- Add the probabilities along the branches of that route.
  - _why:_ Adding is used to combine different alternative routes representing “or”. For events occurring along one route, representing “and”, multiply the branch probabilities instead.
- Subtract the probabilities along the branches of that route.
  - _why:_ Subtraction is used to find a complement from 1, not to combine successive events. A complete route uses the multiplication rule, so its branch probabilities are multiplied.
- Divide the probabilities along the branches of that route.
  - _why:_ Division is not the standard rule for finding the probability of successive events on one route. Since the route represents “and”, multiply its branch probabilities.

## Card 8 — `cloze`

**Front:** In probability trees, the word "and" implies you should [ ___ ] along branches, while "or" implies you should add different routes.

**Back:** In probability trees, the word "and" implies you should multiply along branches, while "or" implies you should add different routes.

**Choices:**

- multiply ✔
  - _why:_ Events joined by “and” occur along the same complete route, so their branch probabilities are multiplied. Probabilities of alternative routes joined by “or” are then added.
- add
  - _why:_ Adding along one route confuses the “and” and “or” rules. Probabilities are multiplied along branches for “and”, while separate alternative routes are added for “or”.
- divide
  - _why:_ Division is not used to combine branch probabilities for successive events. The word “and” identifies one complete route, whose probabilities must be multiplied together.
- subtract
  - _why:_ Subtraction is mainly used to calculate a complementary probability from 1. Events joined by “and” lie on one route, so their branch probabilities are multiplied.

## Card 9 — `cloze`

**Front:** In probability trees, the word "and" implies you should multiply along branches, while "or" implies you should [ ___ ] different routes.

**Back:** In probability trees, the word "and" implies you should multiply along branches, while "or" implies you should add different routes.

**Choices:**

- add ✔
  - _why:_ Separate routes represent alternative ways an outcome can occur, so their probabilities are added after the probability of each complete route has been found by multiplication.
- multiply
  - _why:_ Multiplication is used for events joined by "and" along a single route. Alternative routes joined by "or" must instead be combined by adding their probabilities.
- subtract
  - _why:_ Subtraction is sometimes used for complements, such as finding an event from $1-P(\text{not event})$. Different routes leading to the required outcome are added.
- divide
  - _why:_ Division is not the rule for combining alternative routes in a probability tree. Calculate each route by multiplication, then add the routes representing the required outcome.

## Card 10 — `basic`

**Front:** Why should you NOT add probabilities when a question asks for "both" events to happen?

**Back:** Adding signifies "one or the other"; "both" requires following one full route via multiplication.

**Choices:**

- Adding signifies "one or the other"; "both" requires following one full route via multiplication. ✔
  - _why:_ Both events occur consecutively along one complete path through the tree. The branch probabilities on that path are therefore multiplied rather than added.
- Multiplying signifies "one or the other"; "both" requires combining separate routes via addition.
  - _why:_ This reverses the probability-tree rules. Multiplication follows consecutive events along one route, whereas addition combines separate routes that can each produce the required outcome.
- Adding is unsuitable only for dependent events; independent events can use direct addition for "both".
  - _why:_ Independence affects which probabilities appear on later branches, not the operation for both events. Their probabilities are still multiplied along the relevant complete route.
- Adding gives the complement of "both"; "both" requires subtracting route probabilities from 1.
  - _why:_ Complements are found by subtracting an opposite event from 1, but that is not the general meaning of both. Both events are found by multiplying along one route.

## Card 11 — `cloze`

**Front:** A probability of [ ___ ] represents an impossible event, while a probability of 1 represents a certain event.

**Back:** A probability of 0 represents an impossible event, while a probability of 1 represents a certain event.

**Choices:**

- 0 ✔
  - _why:_ Probability values range from 0 to 1 inclusive. A value of 0 means the event has no chance of occurring, so it is impossible.
- 1
  - _why:_ A probability of 1 means the event is guaranteed, not impossible. An impossible event has probability 0 because it has no chance of occurring.
- 0.5
  - _why:_ A probability of 0.5 represents an event with an equal chance of occurring or not occurring. An impossible event must have probability 0.
- -1
  - _why:_ Probabilities cannot be negative; they must lie between 0 and 1 inclusive. The valid probability representing an impossible event is 0.

## Card 12 — `cloze`

**Front:** A probability of 0 represents an impossible event, while a probability of [ ___ ] represents a certain event.

**Back:** A probability of 0 represents an impossible event, while a probability of 1 represents a certain event.

**Choices:**

- 1 ✔
  - _why:_ A probability of 1 means the event must occur, so it represents certainty. Probability values run from 0 for impossible to 1 for certain.
- 0
  - _why:_ A probability of 0 represents an event that cannot occur, which is the opposite of certainty. A certain event has probability 1.
- 0.5
  - _why:_ A probability of 0.5 indicates an even chance rather than certainty. An event that is guaranteed to occur has the maximum probability, 1.
- 100
  - _why:_ This confuses a percentage with a probability written as a decimal. Certainty is 100%, but on the probability scale from 0 to 1 it is written as 1.

## Card 13 — `basic`

**Front:** A result can happen via two different routes. Outline the steps to find the total probability.

**Back:** Multiply along each individual routeAdd the resulting probabilities together

**Choices:**

- Multiply along each individual routeAdd the resulting probabilities together ✔
  - _why:_ Multiplication finds the probability of all events along one complete route. Because either route produces the required result, the two route probabilities are then added.
- Add along each individual routeMultiply the resulting probabilities together
  - _why:_ This reverses the two probability-tree operations. Events along a route are joined by "and", so multiply them; alternative routes are joined by "or", so add them.
- Multiply along each individual routeSubtract the resulting probabilities together
  - _why:_ Multiplying along each route is correct, but subtracting would wrongly remove one valid route. Since either route gives the result, their probabilities must be added.
- Add along each individual routeAdd the resulting probabilities together
  - _why:_ Adding at both stages treats consecutive events as alternatives. Multiply the branch probabilities along each route first, then add the probabilities of the two valid routes.

## Card 14 — `basic`

**Front:** If $P(\text{navy}) = \frac{5}{9}$, what are the two specific routes for wearing different colours over two days (Navy or Grey)?

**Back:** Navy then GreyGrey then Navy

**Choices:**

- Navy then GreyGrey then Navy ✔
  - _why:_ Different colours means one day must be Navy and the other Grey. Either order is possible, producing the two routes Navy-Grey and Grey-Navy.
- Navy then NavyGrey then Grey
  - _why:_ These routes both produce matching colours on the two days. Different colours requires one Navy and one Grey, in either possible order.
- Navy then GreyNavy then Navy
  - _why:_ The second route gives Navy on both days, so it does not satisfy different colours. The missing valid route is Grey then Navy.
- Grey then NavyGrey then Grey
  - _why:_ The second route gives Grey on both days, so it does not satisfy different colours. The missing valid route is Navy then Grey.

## Card 15 — `basic`

**Front:** What does the term at least one include when looking at two events?

**Back:** First event onlySecond event onlyBoth events

**Choices:**

- First event onlySecond event onlyBoth events ✔
  - _why:_ At least one means one or more events occur. It therefore includes either event occurring alone as well as the case where both events occur.
- First event onlySecond event onlyNeither event
  - _why:_ Neither event means zero events occur, so it cannot be included in at least one. The third included possibility should be both events occurring.
- First event onlyBoth eventsNeither event
  - _why:_ This wrongly includes zero events and omits the case where only the second event occurs. At least one includes first only, second only, and both.
- Second event onlyBoth eventsNeither event
  - _why:_ This wrongly includes zero events and omits the case where only the first event occurs. At least one includes first only, second only, and both.

## Card 16 — `cloze`

**Front:** The shortcut to calculate the probability of "at least one" success is $1 - P(\text{\text{[...]}})$.

**Back:** The shortcut to calculate the probability of "at least one" success is $1 - P(\text{\boxed{none}})$.

**Choices:**

- none ✔
  - _why:_ The complement of at least one success is no successes. Their probabilities total 1, so subtracting the probability of none gives the probability of at least one.
- one
  - _why:_ Subtracting the probability of one success does not generally leave the probability of at least one, because outcomes with multiple successes would be handled incorrectly. Subtract $P(\text{none})$ instead.
- all
  - _why:_ All successes is not the complement of at least one success. The only outcomes excluded from at least one are those with no successes, so use $P(\text{none})$.
- exactly one
  - _why:_ At least one includes exactly one and any larger number of successes. Its complement is therefore no successes, so the shortcut subtracts $P(\text{none})$ from 1.

## Card 17 — `basic`

**Front:** The probability a train is late is 0.3. Use the shortcut to find the probability it is late on at least one of two days.

**Back:** $P(\text{not late}) = 0.7$$P(\text{none late}) = 0.7 \times 0.7 = 0.49$$1 - 0.49 = 0.51$

**Choices:**

- $P(\text{not late}) = 0.7$$P(\text{none late}) = 0.7 \times 0.7 = 0.49$$1 - 0.49 = 0.51$ ✔
  - _why:_ The shortcut finds the complement: calculate the probability that neither day is late, then subtract it from 1. This gives the probability of at least one late day.
- $P(\text{not late}) = 0.3$$P(\text{none late}) = 0.3 \times 0.3 = 0.09$$1 - 0.09 = 0.91$
  - _why:_ This uses the late probability for the ‘not late’ branches, reversing the event. The correct complement is 0.7, giving $0.7 \times 0.7 = 0.49$ and a final probability of 0.51.
- $P(\text{not late}) = 0.7$$P(\text{none late}) = 0.7 + 0.7 = 1.4$$1 - 1.4 = -0.4$
  - _why:_ Probabilities along a sequence of independent branches are multiplied, not added. Multiplying the two 0.7 branches gives 0.49, so the probability of at least one late day is 0.51.
- $P(\text{not late}) = 0.7$$P(\text{none late}) = 0.3 \times 0.3 = 0.09$$1 - 0.09 = 0.91$
  - _why:_ The second line incorrectly uses 0.3, which is the probability of being late, for both ‘none late’ branches. Using 0.7 twice gives 0.49, so the required result is 0.51.

## Card 18 — `basic`

**Front:** In a three-outcome game, $P(\text{win}) = 0.5$ and $P(\text{draw}) = 0.2$. How do you find $P(\text{lose})$?

**Back:** $$1 - 0.5 - 0.2 = 0.3$

**Choices:**

- $$1 - 0.5 - 0.2 = 0.3$ ✔
  - _why:_ The three outcomes are exhaustive, so their probabilities add to 1. Subtracting the win and draw probabilities leaves $1 - 0.5 - 0.2 = 0.3$ for losing.
- $$1 - 0.5 + 0.2 = 0.7$
  - _why:_ The draw probability must also be subtracted because it is another non-losing outcome. Removing both known outcomes from 1 gives $1 - 0.5 - 0.2 = 0.3$.
- $$0.5 + 0.2 = 0.7$
  - _why:_ Adding the win and draw probabilities finds the chance of either winning or drawing, not losing. The remaining probability is found by subtracting that total from 1, giving 0.3.
- $$1 - 0.2 = 0.8$
  - _why:_ This only removes the draw outcome and forgets to remove wins as well. Since win and draw are both separate from losing, calculate $1 - 0.5 - 0.2 = 0.3$.

## Card 19 — `cloze`

**Front:** If an item is taken from a bag [ ___ ], the probabilities on the second set of branches will change.

**Back:** If an item is taken from a bag without replacement, the probabilities on the second set of branches will change.

**Choices:**

- without replacement ✔
  - _why:_ Without replacement means the first item is not returned to the bag. The contents therefore change, so the probabilities on the second set of branches change too.
- with replacement
  - _why:_ With replacement means the first item is returned, leaving the bag’s contents unchanged. The probabilities on the second branches therefore stay the same, unlike the required phrase.
- at random
  - _why:_ Taking an item at random describes how it is selected, not whether the bag’s contents change afterwards. The relevant condition is that the item is taken without replacement.
- in pairs
  - _why:_ Taking items in pairs does not specifically state whether the first item is returned. The second branch probabilities change only when the item is taken without replacement.

## Card 20 — `cloze`

**Front:** If an item is taken from a bag without replacement, the probabilities on the second set of branches will [ ___ ].

**Back:** If an item is taken from a bag without replacement, the probabilities on the second set of branches will change.

**Choices:**

- change ✔
  - _why:_ Without replacement alters the contents of the bag after the first selection. Since the numbers of items change, the probabilities on the second set of branches change.
- stay constant
  - _why:_ The probabilities stay constant when an item is replaced after selection. Without replacement changes the bag’s composition, so the correct word is change.
- cancel
  - _why:_ Branch probabilities do not cancel when an item is removed. Removing an item changes the total and possibly the colour counts, so the probabilities change.
- double
  - _why:_ Removing one item does not generally double every second-branch probability. The probabilities may increase or decrease depending on the item removed, so they simply change.

## Card 21 — `basic`

**Front:** A player plays two rounds where $P(\text{win}) = 0.5$. Calculate the probability they win both.

**Back:** $$0.5 \times 0.5 = 0.25$

**Choices:**

- $$0.5 \times 0.5 = 0.25$ ✔
  - _why:_ The two rounds are treated as independent, so multiply the probability of winning each round. This gives $0.5 \times 0.5 = 0.25$ for winning both.
- $$0.5 + 0.5 = 1$
  - _why:_ Adding probabilities finds neither the probability of both independent wins nor a valid result here. Probabilities along a route are multiplied, giving $0.5 \times 0.5 = 0.25$.
- $$0.5 \times 2 = 1$
  - _why:_ Multiplying by 2 counts the two rounds but does not calculate both events occurring. For consecutive independent wins, multiply the two branch probabilities to obtain 0.25.
- $$1 - (0.5 \times 0.5) = 0.75$
  - _why:_ Subtracting the product from 1 finds the probability of not winning both, rather than winning both. The required probability is directly $0.5 \times 0.5 = 0.25$.

## Card 22 — `basic`

**Front:** What is the definition of a route in a probability tree?

**Back:** A complete path from the start of the tree to an end outcome.

**Choices:**

- A complete path from the start of the tree to an end outcome. ✔
  - _why:_ A route follows one branch at every stage, beginning at the start and finishing at one end outcome. It is therefore a complete path through the tree.
- A single branch from the start of the tree to an end outcome.
  - _why:_ A single branch represents one step between outcomes, not the whole sequence. A route includes every branch needed to form a complete path from start to an end outcome.
- A probability label beside each branch of the tree.
  - _why:_ Probability labels give the chance of individual branches, but they are not routes. A route is the complete sequence of branches from the tree’s start to an end outcome.
- A pair of outcomes at the same stage of the tree.
  - _why:_ Outcomes at one stage do not describe a full journey through the tree. A route must connect the start to an end outcome by following a complete path.

## Card 23 — `cloze`

**Front:** To find the probability of two independent events happening together, you [ ___ ] their individual probabilities.

**Back:** To find the probability of two independent events happening together, you multiply their individual probabilities.

**Choices:**

- multiply ✔
  - _why:_ For independent events happening together, the probability of one event does not affect the other. Their individual probabilities are therefore multiplied to find the combined probability.
- add
  - _why:_ Adding probabilities is used for suitable ‘either-or’ outcomes, not independent events happening together. For two events both occurring, multiply their individual probabilities.
- subtract
  - _why:_ Subtraction is commonly used with complements, such as finding an event from ‘not the event’. Two independent events occurring together require multiplication instead.
- divide
  - _why:_ Dividing probabilities does not combine independent events occurring together. The probability along a route is found by multiplying the probabilities of its branches.

## Card 24 — `basic`

**Front:** If $P(\text{win badminton}) = \frac{3}{5}$ and $P(\text{win tennis}) = \frac{7}{10}$, calculate $P(\text{win both})$.

**Back:** $$\frac{3}{5} \times \frac{7}{10} = \frac{21}{50}$

**Choices:**

- $$\frac{3}{5} \times \frac{7}{10} = \frac{21}{50}$ ✔
  - _why:_ Winning both independent sports requires both events to occur, so multiply their probabilities. The product is $\frac{21}{50}$ after multiplying the numerators and denominators.
- $$\frac{3}{5} + \frac{7}{10} = \frac{13}{10}$
  - _why:_ Adding finds a combined ‘either’ quantity and produces a value above 1, which cannot be a probability. For winning both, multiply to get $\frac{21}{50}$.
- $$\frac{3}{5} \times \frac{7}{10} = \frac{21}{100}$
  - _why:_ The numerators are multiplied correctly, but the denominator calculation is wrong: $5 \times 10 = 50$, not 100. Therefore the product is $\frac{21}{50}$.
- $$\frac{3}{5} \times \frac{7}{10} = \frac{10}{15}$
  - _why:_ This adds the numerators and denominators rather than multiplying the fractions. Multiplying corresponding parts gives $\frac{3 \times 7}{5 \times 10} = \frac{21}{50}$.
