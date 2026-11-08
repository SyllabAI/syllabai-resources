# Conditional Probability Flashcards

_Lane: `gcse-maths-edexcel` · grade 7 · 20 cards (source: MathsGenie flashcards)_

## Card 1 — `cloze`

**Front:** In a probability tree diagram, all branches originating from the same point must sum to [ ___ ].

**Back:** In a probability tree diagram, all branches originating from the same point must sum to 1.

**Choices:**

- 1 ✔
  - _why:_ Probabilities for all possible outcomes from one point must total 1 because those branches collectively represent every outcome that can occur next.
- 0
  - _why:_ A total of 0 would mean that none of the possible outcomes can occur. The branches must instead sum to 1, representing certainty.
- 2
  - _why:_ This confuses the number of branches with their total probability. Regardless of how many branches there are, their probabilities must sum to 1.
- 0.5
  - _why:_ Probabilities may be written as percentages, but 50% is not the required total. All branches from the same point must sum to 1, or 100%.

## Card 2 — `basic`

**Front:** What does the notation $P(B \mid A)$ represent?

**Back:** The conditional probability of B occurring given that A has already occurred.

**Choices:**

- The conditional probability of B occurring given that A has already occurred. ✔
  - _why:_ The vertical bar means “given that”, so this notation describes the probability that B occurs under the condition that A has already occurred.
- The conditional probability of A occurring given that B has already occurred.
  - _why:_ This reverses the condition and describes $P(A \mid B)$. In $P(B \mid A)$, B is the event being considered after A has already occurred.
- The combined probability of A and B both occurring.
  - _why:_ The notation for both events occurring is $P(A \cap B)$ or $P(A \text{ and } B)$. The vertical bar instead indicates B occurring given A.
- The total probability of A or B occurring independently.
  - _why:_ The probability of either event is represented using a union, such as $P(A \cup B)$. Here the vertical bar specifies the condition that A has occurred.

## Card 3 — `basic`

**Front:** How do you calculate the probability of a specific sequence of events (a single route) in a tree diagram?

**Back:** Multiply the probabilities along the branches.

**Choices:**

- Multiply the probabilities along the branches. ✔
  - _why:_ A route represents successive events that must all occur, so the multiplication rule is used to combine the probabilities on its branches.
- Add the probabilities along the branches.
  - _why:_ Adding is used to combine separate mutually exclusive routes, not successive branches on one route. For a specific sequence, multiply the branch probabilities.
- Subtract the probabilities along the branches.
  - _why:_ Subtracting branch probabilities does not represent successive events. A specific sequence requires every event on its route to occur, so multiply the probabilities.
- Divide the probabilities along the branches.
  - _why:_ Dividing the branch probabilities is not the tree-diagram rule for a sequence. Since all events along the route must occur, their probabilities are multiplied.

## Card 4 — `cloze`

**Front:** The rule for finding the probability of a sequence of events is $$P(A \text{ and } B) = \text{[...]}$$.

**Back:** The rule for finding the probability of a sequence of events is $$P(A \text{ and } B) = \boxed{P(A) \times P(B \mid A)}$$.

**Choices:**

- $$P(A) \times P(B \mid A)$ ✔
  - _why:_ For A and B to occur in sequence, multiply the probability of A by the conditional probability that B occurs after A has occurred.
- $$P(A) + P(B \mid A)$
  - _why:_ Adding these probabilities combines alternatives rather than successive events. The probability of the sequence is $P(A) \times P(B \mid A)$.
- $$P(A) \times P(B)$
  - _why:_ This incorrectly treats B as unaffected by A. The general multiplication rule uses B’s conditional probability, giving $P(A) \times P(B \mid A)$.
- $$P(A) \times P(A \mid B)$
  - _why:_ This reverses which event is conditioned on while retaining $P(A)$. The matching rule is $P(A) \times P(B \mid A)$.

## Card 5 — `basic`

**Front:** In a "without replacement" scenario, what two things change for the second choice?

**Back:** The total number of items (denominator) decreases by 1.The number of items of the chosen category (numerator) decreases by 1.

**Choices:**

- The total number of items (denominator) decreases by 1.The number of items of the chosen category (numerator) decreases by 1. ✔
  - _why:_ Because the selected item is not returned, one fewer item remains overall and one fewer remains in the category that was selected.
- The total number of items (denominator) stays the same.The number of items of the chosen category (numerator) stays the same.
  - _why:_ This describes replacement rather than selection without replacement. The denominator must decrease by 1, and the chosen category’s numerator must also decrease by 1.
- The total number of items (denominator) increases by 1.The number of items of the chosen category (numerator) increases by 1.
  - _why:_ Removing an item reduces rather than increases the available quantities. Both the total and the count for the selected category decrease by 1.
- The total number of items (denominator) stays the same.The number of items of the chosen category (numerator) decreases by 1.
  - _why:_ The denominator cannot stay unchanged because one item has been removed. It decreases by 1, as does the numerator for the category selected first.

## Card 6 — `basic`

**Front:** When should you add separate routes together in a probability problem?

**Back:** When the routes are mutually exclusive outcomes (e.g. "Red-Red" OR "Green-Green").

**Choices:**

- When the routes are mutually exclusive outcomes (e.g. "Red-Red" OR "Green-Green"). ✔
  - _why:_ Mutually exclusive routes cannot happen simultaneously, so their probabilities are added when either route would satisfy the required outcome.
- When the routes are independent outcomes (e.g. "Red-Red" AND "Green-Green").
  - _why:_ Independent events do not automatically correspond to routes that should be added. Separate routes are added when they are mutually exclusive alternatives satisfying the required outcome.
- When the routes are consecutive outcomes (e.g. "Red" THEN "Green").
  - _why:_ Successive outcomes on one route are combined by multiplication, not addition. Addition applies to separate mutually exclusive routes that represent alternative successful outcomes.
- When the routes are equally likely outcomes (e.g. "Red-Blue" AND "Blue-Red").
  - _why:_ Equally likely routes need not be relevant alternatives, and equality is not the reason for adding. Add routes when they are mutually exclusive successful outcomes.

## Card 7 — `basic`

**Front:** How do you calculate the probability of picking "one of each color" from a bag of red and blue counters?

**Back:** Calculate the probability of Red-Blue and Blue-Red separately, then add them together.

**Choices:**

- Calculate the probability of Red-Blue and Blue-Red separately, then add them together. ✔
  - _why:_ One of each colour can occur in either order. These two mutually exclusive routes must be calculated separately and then added to obtain the total probability.
- Calculate the probability of Red-Blue and Blue-Red separately, then multiply them together.
  - _why:_ Multiplying the completed route probabilities would mean both mutually exclusive orders occur at once. Calculate Red-Blue and Blue-Red separately, then add their probabilities.
- Calculate the probability of Red-Red and Blue-Blue separately, then add them together.
  - _why:_ Red-Red and Blue-Blue represent two counters of the same colour, not one of each. Use the Red-Blue and Blue-Red routes and add them.
- Calculate the probability of Red-Blue and Blue-Red separately, then subtract them.
  - _why:_ Subtracting the two orders can cancel valid outcomes and does not represent either order occurring. Calculate both mixed-colour routes and add their probabilities.

## Card 8 — `cloze`

**Front:** If the probability of picking a blue pen on Monday is 0.65, the probability of picking a black pen is [ ___ ].

**Back:** If the probability of picking a blue pen on Monday is 0.65, the probability of picking a black pen is $1 - 0.65 = 0.35$.

**Choices:**

- $$1 - 0.65 = 0.35$ ✔
  - _why:_ Blue and black are complementary outcomes, so their probabilities total 1. Subtracting 0.65 from 1 gives a black-pen probability of 0.35.
- $$0.65 - 1 = -0.35$
  - _why:_ This subtraction is reversed, producing a negative value, which cannot be a probability. The complement is found using $1 - 0.65 = 0.35$.
- $$1 + 0.65 = 1.65$
  - _why:_ Adding complementary probabilities is the wrong operation and gives a result above 1. The black probability is the complement, $1 - 0.65 = 0.35$.
- $$1 - 0.35 = 0.65$
  - _why:_ This treats the blue and black probabilities as equal. Since they are complementary, the black probability must be $1 - 0.65 = 0.35$.

## Card 9 — `basic`

**Front:** A bag has 5 red and 3 blue counters. If a red is picked first and not replaced, what is $P(\text{red second} \mid \text{red first})$?

**Back:** $$\frac{4}{7}$

**Choices:**

- $$\frac{4}{7}$ ✔
  - _why:_ After the first red counter is removed, 4 red counters remain out of 7 counters altogether. Therefore, the conditional probability of another red is $\frac{4}{7}$.
- $$\frac{5}{7}$
  - _why:_ This keeps all 5 red counters in the numerator despite one already being removed. Only 4 of the 7 remaining counters are red, so the answer is $\frac{4}{7}$.
- $$\frac{4}{8}$
  - _why:_ This treats the first counter as though it were replaced, leaving 8 counters altogether. Without replacement, 4 red counters remain among 7, giving $\frac{4}{7}$.
- $$\frac{3}{7}$
  - _why:_ This uses the original number of blue counters as the numerator. After a red is removed, there are 4 red counters among 7 remaining, so the probability is $\frac{4}{7}$.

## Card 10 — `cloze`

**Front:** When picking two counters without replacement from a bag of 12, the denominator for the second branch will be [ ___ ].

**Back:** When picking two counters without replacement from a bag of 12, the denominator for the second branch will be 11.

**Choices:**

- 11 ✔
  - _why:_ Without replacement, the first pick removes one counter from the original total of 12. Every second branch therefore has a denominator of $12-1=11$.
- 12
  - _why:_ This incorrectly keeps the original total, as if the first counter were replaced. Without replacement, only 11 counters remain, so the second-branch denominator is 11.
- 10
  - _why:_ This subtracts both picks before calculating the second pick. At the moment of the second pick, only one counter has been removed, so the denominator is 11.
- 13
  - _why:_ This mistakenly increases the total after the first pick. Removing one counter from a bag of 12 leaves 11, so every second-branch denominator is 11.

## Card 11 — `basic`

**Front:** What does it mean for two routes to be "mutually exclusive"?

**Back:** They cannot both happen at the same time.

**Choices:**

- They cannot both happen at the same time. ✔
  - _why:_ Mutually exclusive routes have no shared outcomes, so one route occurring prevents the other from occurring simultaneously. Their intersection therefore has probability zero.
- They must both happen at the same time.
  - _why:_ This describes routes that always occur together, not mutually exclusive routes. Mutually exclusive routes share no outcomes and therefore cannot both happen at the same time.
- They do not affect each other when one happens.
  - _why:_ This confuses mutually exclusive events with independent events. Independence means one event does not affect the other, whereas mutually exclusive routes cannot both happen at the same time.
- They cover every possible outcome in the sample space.
  - _why:_ This describes exhaustive routes, which together cover the whole sample space. Mutually exclusive routes instead have no overlap, meaning they cannot both happen at the same time.

## Card 12 — `basic`

**Front:** A bag has 7 red and 5 green counters. How do you set up the calculation for "both counters are the same color" (without replacement)?

**Back:** $$(\frac{7}{12} \times \frac{6}{11}) + (\frac{5}{12} \times \frac{4}{11})$

**Choices:**

- $$(\frac{7}{12} \times \frac{6}{11}) + (\frac{5}{12} \times \frac{4}{11})$ ✔
  - _why:_ The two valid routes are red then red and green then green. Their branch probabilities are multiplied within each route, then the two mutually exclusive routes are added.
- $$(\frac{7}{12} \times \frac{7}{11}) + (\frac{5}{12} \times \frac{5}{11})$
  - _why:_ This fails to reduce each colour count after the first pick, effectively treating the counters as replaced. The second numerators should be 6 and 4, giving the correct sum.
- $$(\frac{7}{12} \times \frac{5}{11}) + (\frac{5}{12} \times \frac{7}{11})$
  - _why:_ These routes represent red then green and green then red, so they calculate different colours. For the same colour, use red-red and green-green instead.
- $$(\frac{7}{12} \times \frac{6}{11}) \times (\frac{5}{12} \times \frac{4}{11})$
  - _why:_ This multiplies the red-red and green-green routes as though both routes must occur together. They are alternative outcomes, so their separate products must be added.

## Card 13 — `basic`

**Front:** Why is the calculation for "different colors" usually more complex than for a specific sequence like "Black then Red"?

**Back:** It usually involves two different orders (BR and RB) that must be added.

**Choices:**

- It usually involves two different orders (BR and RB) that must be added. ✔
  - _why:_ Different colours can occur as Black then Red or Red then Black. Each order is a separate route whose probabilities are multiplied, and the two route probabilities are then added.
- It usually involves two different orders (BR and RB) that must be multiplied.
  - _why:_ Different colours do not require both orders to occur together. BR and RB are alternative routes, so their probabilities must be calculated separately and then added, not multiplied.
- It usually involves only one possible order (BR but not RB) in the calculation.
  - _why:_ This overlooks the reverse order, Red then Black. Different colours can occur through either BR or RB, so both route probabilities must be calculated and added.
- It usually involves replacing the first counter before the second counter is selected.
  - _why:_ Replacement affects the branch probabilities but does not explain the extra complexity. The key issue is that different colours includes both BR and RB, whose probabilities must be added.

## Card 14 — `cloze`

**Front:** In a Venn diagram, the region representing "Tea and Coffee but not Juice" excludes the [ ___ ] where all three meet.

**Back:** In a Venn diagram, the region representing "Tea and Coffee but not Juice" excludes the triple overlap where all three meet.

**Choices:**

- triple overlap ✔
  - _why:_ The triple overlap contains people who are in Tea, Coffee and Juice. Excluding it leaves only those who are in both Tea and Coffee but not Juice.
- pairwise overlap
  - _why:_ The pairwise Tea and Coffee overlap includes the required region, so excluding all of it would remove the desired people. Only the triple overlap with Juice must be excluded.
- union
  - _why:_ The union contains everyone in at least one of the three sets, far beyond the region being excluded. Only the triple overlap belongs to all three sets.
- outside region
  - _why:_ The region outside the circles represents people in none of the sets, not people in all three. Tea and Coffee but not Juice excludes the triple overlap.

## Card 15 — `basic`

**Front:** If 17 people like Tea and Coffee, and 12 of those also like Juice, how many people like Tea and Coffee only?

**Back:** $$17 - 12 = 5$

**Choices:**

- $$17 - 12 = 5$ ✔
  - _why:_ The 17 people counted in Tea and Coffee include the 12 who also like Juice. Subtracting those 12 leaves 5 who like Tea and Coffee only.
- $$17 + 12 = 29$
  - _why:_ Adding double-counts the 12 people because they are already included among the 17 who like Tea and Coffee. Subtracting them gives $17-12=5$.
- $$17 - 5 = 12$
  - _why:_ This subtracts the number sought rather than the 12 people known to also like Juice. Tea and Coffee only is found directly using $17-12=5$.
- $$17 - 17 = 0$
  - _why:_ This assumes all 17 Tea-and-Coffee people also like Juice, although only 12 do. Removing those 12 from 17 leaves $17-12=5$ people.

## Card 16 — `cloze`

**Front:** If there are 5 cards (1, 1, 2, 2, 4) and a 1 is picked first, the probability that the second card is greater than the first is [ ___ ].

**Back:** If there are 5 cards (1, 1, 2, 2, 4) and a 1 is picked first, the probability that the second card is greater than the first is $\frac{3}{4}$.

**Choices:**

- $$\frac{3}{4}$ ✔
  - _why:_ After one 1 is removed, four cards remain: 1, 2, 2 and 4. Three of these are greater than 1, so the probability is $\frac{3}{4}$.
- $$\frac{1}{2}$
  - _why:_ This counts only the two cards labelled 2 and overlooks that 4 is also greater than 1. Three of the four remaining cards are favourable, giving $\frac{3}{4}$.
- $$\frac{3}{5}$
  - _why:_ This retains the original denominator of 5 as if the first card were replaced. Only four cards remain, and three are greater than 1, giving $\frac{3}{4}$.
- $$\frac{1}{4}$
  - _why:_ This counts the one remaining card labelled 1, which is the only unfavourable outcome. The other three cards exceed 1, so the required probability is $\frac{3}{4}$.

## Card 17 — `basic`

**Front:** What is the 3-step strategy for calculating probability for "second card greater than first" using a tree?

**Back:** Identify routes where second > first.Multiply along those specific branches.Add the resulting probabilities.

**Choices:**

- Identify routes where second > first.Multiply along those specific branches.Add the resulting probabilities. ✔
  - _why:_ Each valid route represents a mutually exclusive outcome. Multiplying gives the probability of each route, and adding those route probabilities gives the overall probability that the second card is greater.
- Identify routes where second > first.Add along those specific branches.Multiply the resulting probabilities.
  - _why:_ This reverses the tree rules. Probabilities are multiplied along each valid route, then the probabilities of the separate valid routes are added together.
- Identify routes where second Multiply along those specific branches.Add the resulting probabilities.
  - _why:_ This selects the opposite event, where the second card is smaller. The correct method selects routes where second > first, multiplies along them, then adds their probabilities.
- Identify routes where second > first.Multiply all branches in the tree.Add the resulting probabilities.
  - _why:_ Including every branch counts outcomes that do not satisfy the condition. Only routes where second > first should be multiplied individually before their probabilities are added.

## Card 18 — `basic`

**Front:** In a Venn-style probability question, how do you handle picking "two people" from a group?

**Back:** Treat it as conditional probability without replacement; the total group size decreases for the second pick.

**Choices:**

- Treat it as conditional probability without replacement; the total group size decreases for the second pick. ✔
  - _why:_ Once the first person has been chosen, that person is unavailable for the second choice. Therefore, the second probability is conditional and uses a total reduced by one.
- Treat it as independent probability with replacement; the total group size stays the same for the second pick.
  - _why:_ This incorrectly assumes the first person is returned to the group. People are normally chosen without replacement, so the second probability depends on the first pick and has a smaller total.
- Treat it as independent probability without replacement; the total group size decreases for the second pick.
  - _why:_ Although the group size decreases, the events are not independent because the first selection changes the second selection’s probabilities. It is conditional probability without replacement.
- Treat it as conditional probability with replacement; the total group size increases for the second pick.
  - _why:_ Replacement would keep the group size unchanged, not increase it, and is not normally used when choosing two different people. The correct model is conditional probability without replacement.

## Card 19 — `cloze`

**Front:** To find the probability of a complement (the event not happening), you subtract the probability of the event from [ ___ ].

**Back:** To find the probability of a complement (the event not happening), you subtract the probability of the event from 1.

**Choices:**

- 1 ✔
  - _why:_ The probabilities of an event and its complement sum to 1. Therefore, the probability that the event does not happen is $1-P(A)$.
- 0
  - _why:_ Subtracting from 0 confuses the minimum possible probability with the total probability. An event and its complement exhaust all outcomes, so their probabilities add to 1.
- $$-1$
  - _why:_ Probabilities cannot be negative, so $-1$ cannot represent the total probability. Complement probabilities are found by subtracting the event’s probability from 1.
- 2
  - _why:_ A total of 2 lies outside the probability scale, which runs from 0 to 1. The event and its complement together have probability 1.

## Card 20 — `basic`

**Front:** If 29 students like coffee out of 40 total, what is the probability two chosen students both like coffee?

**Back:** $$\frac{29}{40} \times \frac{28}{39}$

**Choices:**

- $$\frac{29}{40} \times \frac{28}{39}$ ✔
  - _why:_ The first coffee-liker is chosen with probability $\frac{29}{40}$. Without replacement, 28 coffee-likers remain among 39 students for the second choice.
- $$\frac{29}{40} \times \frac{29}{40}$
  - _why:_ This treats the selections as if the first student were replaced. Without replacement, both the number of coffee-likers and the total number of students decrease by one.
- $$\frac{29}{40} \times \frac{28}{40}$
  - _why:_ This reduces the number of coffee-likers but forgets to reduce the total group size. After one student is chosen, only 39 students remain.
- $$\frac{29}{40} \times \frac{29}{39}$
  - _why:_ This reduces the total group size but not the number of coffee-likers. After choosing a student who likes coffee, only 28 such students remain among the other 39.
