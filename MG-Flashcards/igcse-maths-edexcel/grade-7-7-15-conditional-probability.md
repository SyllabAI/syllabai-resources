# Conditional Probability Flashcards

_Lane: `igcse-maths-edexcel` · grade 7 · 22 cards (source: MathsGenie flashcards)_

## Card 1 — `cloze`

**Front:** An [ ___ ] is one possible result; an [ ___ ] is a set of outcomes.

**Back:** An outcome is one possible result; an event is a set of outcomes.

**Choices:**

- An outcome is one possible result; an event is a set of outcomes. ✔
  - _why:_ An outcome is one individual result of an experiment, while an event contains one or more outcomes that satisfy a specified condition.
- An event is one possible result; an outcome is a set of outcomes.
  - _why:_ This reverses the two definitions. An outcome is one possible result, whereas an event is a set containing one or more outcomes.
- An experiment is one possible result; an event is a set of outcomes.
  - _why:_ An experiment is the process that generates results, not one possible result. The individual result is an outcome, and a set of outcomes is an event.
- An trial is one possible result; an sample space is a set of outcomes.
  - _why:_ A trial is one performance of an experiment, while the result it produces is an outcome. A set of outcomes is called an event.

## Card 2 — `basic`

**Front:** For equally likely outcomes, how do you calculate probability?

**Back:** Successful outcomes divided by total outcomes: $$\frac{\text{successful outcomes}}{\text{total outcomes}}$$

**Choices:**

- Successful outcomes divided by total outcomes: $$\frac{\text{successful outcomes}}{\text{total outcomes}}$$ ✔
  - _why:_ For equally likely outcomes, probability is the number of outcomes satisfying the event divided by the total number of possible outcomes.
- Total outcomes divided by successful outcomes: $$\frac{\text{total outcomes}}{\text{successful outcomes}}$$
  - _why:_ Reversing the fraction can produce a value greater than 1, which is impossible for probability. Successful outcomes must be divided by total outcomes.
- Unsuccessful outcomes divided by total outcomes: $$\frac{\text{unsuccessful outcomes}}{\text{total outcomes}}$$
  - _why:_ Counting unsuccessful outcomes gives the probability of the complementary event. The required probability uses successful outcomes divided by total outcomes.
- Successful outcomes divided by unsuccessful outcomes: $$\frac{\text{successful outcomes}}{\text{unsuccessful outcomes}}$$
  - _why:_ The denominator must count every possible outcome, not only failures. Probability is successful outcomes divided by the total number of outcomes.

## Card 3 — `cloze`

**Front:** A probability of 0 means [ ___ ]; a probability of 1 means [ ___ ].

**Back:** A probability of 0 means impossible; a probability of 1 means certain.

**Choices:**

- A probability of 0 means impossible; a probability of 1 means certain. ✔
  - _why:_ Probability 0 represents an event that cannot occur, while probability 1 represents an event guaranteed to occur under the stated conditions.
- A probability of 0 means certain; a probability of 1 means impossible.
  - _why:_ This reverses the endpoints of the probability scale. Probability 0 means impossible, while probability 1 means certain.
- A probability of 0 means unlikely; a probability of 1 means likely.
  - _why:_ “Unlikely” and “likely” describe probabilities near the endpoints, not exactly at them. Probability 0 means impossible and probability 1 means certain.
- A probability of 0 means less likely; a probability of 1 means more likely.
  - _why:_ Probability 0 is not merely less likely, and probability 1 is not merely more likely. They mean impossible and certain respectively.

## Card 4 — `cloze`

**Front:** $$P(B\mid A)$ means the probability of event $B$ [ ___ ].

**Back:** $$P(B\mid A)$ means the probability of event $B$ given event A.

**Choices:**

- given event A ✔
  - _why:_ The vertical bar means “given”, so $P(B\mid A)$ is the probability that $B$ occurs under the condition that event $A$ has occurred.
- given event B
  - _why:_ This reverses the conditioning event. $P(B\mid A)$ asks about $B$ given that $A$ has occurred, not $B$ given itself.
- independent of event A
  - _why:_ Conditional notation does not assert independence. It asks for the probability of $B$ after taking the information that event $A$ occurred into account.
- or event A
  - _why:_ The vertical bar denotes a condition, not the union word “or”. The expression means the probability of $B$ given event $A$.

## Card 5 — `basic`

**Front:** Without replacement, what happens to the second denominator?

**Back:** It is one less than the first denominator.

**Choices:**

- It is one less than the first denominator. ✔
  - _why:_ One object has already been removed, so the total number available for the second selection decreases by one, making its denominator one less.
- It is one more than the first denominator.
  - _why:_ The total cannot increase when an object is removed. Without replacement, one fewer object remains, so the second denominator is one less.
- It is the same as the first denominator.
  - _why:_ Keeping the denominator unchanged incorrectly treats the selection as replacement. Without replacement, one object is gone, so the denominator decreases by one.
- It is two less than the first denominator.
  - _why:_ Only one object has been selected before the second draw, so the total decreases by one rather than two. The second denominator is one less.

## Card 6 — `basic`

**Front:** A bag has 7 orange and 5 purple counters. First is purple and not replaced. What is $P(\text{orange second})$?

**Back:** $$\frac{7}{11}$

**Choices:**

- $$\frac{7}{11}$ ✔
  - _why:_ Removing a purple counter leaves all 7 orange counters among 11 counters in total. Therefore, the probability of orange on the second draw is $\frac{7}{11}$.
- $$\frac{7}{12}$
  - _why:_ Using 12 as the denominator incorrectly assumes the purple counter was replaced. Without replacement, only 11 counters remain, so the probability is $\frac{7}{11}$.
- $$\frac{6}{11}$
  - _why:_ This subtracts one from the orange count even though a purple counter was removed. All 7 orange counters remain, giving $\frac{7}{11}$.
- $$\frac{5}{11}$
  - _why:_ This uses the original number of purple counters as the numerator. The requested colour is orange, and 7 orange counters remain out of 11.

## Card 7 — `cloze`

**Front:** In a probability tree, [ ___ ] along a complete route and [ ___ ] different successful routes.

**Back:** In a probability tree, multiply along a complete route and add different successful routes.

**Choices:**

- In a probability tree, multiply along a complete route and add different successful routes. ✔
  - _why:_ Successive branches on one complete route represent events occurring together, so their probabilities are multiplied. Alternative successful routes are mutually exclusive, so their probabilities are added.
- In a probability tree, multiply along a complete route and multiply different successful routes.
  - _why:_ Multiplication is correct along each complete route, but alternative successful routes must be added because any one of those routes can produce the required event.
- In a probability tree, add along a complete route and multiply different successful routes.
  - _why:_ This reverses the probability-tree rules. Multiply successive probabilities along a complete route, then add the probabilities of different routes that produce the required result.
- In a probability tree, add along a complete route and add different successful routes.
  - _why:_ Adding along a route treats successive events as alternatives rather than a sequence. Multiply along each complete route, then add the different successful routes.

## Card 8 — `basic`

**Front:** A bag has 5 red and 3 blue counters. Two are chosen without replacement. What is $P(\text{red then blue})$?

**Back:** $$\frac{5}{8}\times\frac{3}{7}=\frac{15}{56}$

**Choices:**

- $$\frac{5}{8}\times\frac{3}{7}=\frac{15}{56}$ ✔
  - _why:_ The first draw is red with probability $\frac{5}{8}$. This leaves 3 blue counters among 7 counters, so multiplying gives $\frac{15}{56}$.
- $$\frac{5}{8}\times\frac{3}{8}=\frac{15}{64}$
  - _why:_ Keeping 8 as the second denominator incorrectly assumes replacement. After the red counter is removed, 7 counters remain, giving $\frac{5}{8}\times\frac{3}{7}=\frac{15}{56}$.
- $$\frac{5}{8}\times\frac{2}{7}=\frac{10}{56}$
  - _why:_ This incorrectly removes a blue counter after the first draw. The removed counter was red, so all 3 blue counters remain among the 7 counters.
- $$\frac{5}{8}+\frac{3}{7}=\frac{59}{56}$
  - _why:_ Adding treats the two draws as alternative routes, but “red then blue” requires both successive events. Their probabilities must be multiplied to obtain $\frac{15}{56}$.

## Card 9 — `basic`

**Front:** A bag has 5 red and 3 blue counters. Two are chosen without replacement. What is $P(\text{one of each colour})$?

**Back:** $$\frac{15}{28}$

**Choices:**

- $$\frac{15}{28}$ ✔
  - _why:_ There are 5 ways to choose red first and blue second, and 3 ways to choose blue first and red second, giving 15 favourable ordered outcomes out of 8 × 7 = 56, which simplifies to this fraction.
- $$\frac{15}{56}$
  - _why:_ This counts the 15 favourable ordered outcomes but uses 8 × 14 as the denominator. Without replacement, the second draw has 7 remaining counters, so the correct probability is $\frac{15}{28}$.
- $$\frac{3}{8}$
  - _why:_ This uses the proportion of red counters, $\frac{5}{8}$, without properly accounting for the second draw and the two possible colour orders. The correct probability is $\frac{15}{28}$.
- $$\frac{5}{14}$
  - _why:_ This includes only one colour order, such as red then blue, rather than both red-blue and blue-red. Including both orders gives the correct probability, $\frac{15}{28}$.

## Card 10 — `cloze`

**Front:** “One of each colour” usually means [ ___ ]; “both the same colour” means [ ___ ].

**Back:** “One of each colour” usually means different colours; “both the same colour” means matching pairs.

**Choices:**

- “One of each colour” usually means different colours; “both the same colour” means matching pairs. ✔
  - _why:_ “Different colours” means the two selected counters do not match, while “matching pairs” means both counters have the same colour. These phrases describe the two possible categories of outcomes.
- “One of each colour” usually means matching colours; “both the same colour” means matching pairs.
  - _why:_ The first phrase describes counters with the same colour, but “one of each colour” requires different colours. The correct meanings are different colours and matching pairs.
- “One of each colour” usually means different colours; “both the same colour” means different pairs.
  - _why:_ “One of each colour” is correctly identified, but “both the same colour” does not mean different pairs. It means matching pairs, because the two colours match.
- “One of each colour” usually means same colours; “both the same colour” means matching pairs.
  - _why:_ The first phrase has been reversed: one of each colour means different colours, not same colours. The second meaning is correct, but both meanings must be right.

## Card 11 — `basic`

**Front:** With red, blue and green counters, what routes give “both the same colour”?

**Back:** red-redblue-bluegreen-green

**Choices:**

- red-redblue-bluegreen-green ✔
  - _why:_ For both counters to have the same colour, they can be red-red, blue-blue or green-green. These are the three possible same-colour routes.
- red-blueblue-greengreen-red
  - _why:_ Each listed route uses two different colours, so these are routes for “one of each colour”, not “both the same colour”. The correct routes are red-red, blue-blue and green-green.
- red-redblue-greenred-green
  - _why:_ This includes only one valid same-colour route and two mixed-colour routes. A complete list must contain one route for each colour: red-red, blue-blue and green-green.
- red-blueblue-bluegreen-red
  - _why:_ The repeated colours are not paired correctly in these routes, and mixed-colour selections do not count as matching. The valid same-colour routes are red-red, blue-blue and green-green.

## Card 12 — `basic`

**Front:** A bag has 4 red, 4 blue and 2 green counters. Two are chosen without replacement. What is $P(\text{same colour})$?

**Back:** $$\frac{13}{45}$

**Choices:**

- $$\frac{13}{45}$ ✔
  - _why:_ There are $\binom{4}{2}=6$ red-red pairs, 6 blue-blue pairs and $\binom{2}{2}=1$ green-green pair, out of $\binom{10}{2}=45$ pairs. Thus the probability is $\frac{13}{45}$.
- $$\frac{17}{45}$
  - _why:_ This overcounts the green-green pairs as though there were more than two green counters. Only one green-green pair exists, so the correct total is 13 favourable pairs and probability $\frac{13}{45}$.
- $$\frac{7}{15}$
  - _why:_ This counts same-colour pairs using replacement, allowing a counter to be selected again. The counters are chosen without replacement, giving the correct probability $\frac{13}{45}$.
- $$\frac{2}{9}$
  - _why:_ This misses some of the red-red and blue-blue pairs by treating colours rather than individual counters as the outcomes. Counting individual pairs gives $\frac{13}{45}$.

## Card 13 — `cloze`

**Front:** If there are only two possible outcomes, their probabilities add to [ ___ ]; if black is 0.35, not black is [ ___ ].

**Back:** If there are only two possible outcomes, their probabilities add to 1; if black is 0.35, not black is 0.65.

**Choices:**

- If there are only two possible outcomes, their probabilities add to 1; if black is 0.35, not black is 0.65. ✔
  - _why:_ For two outcomes, the probabilities must account for every possibility, so they add to 1. The complement of black is $1-0.35=0.65$.
- If there are only two possible outcomes, their probabilities add to 2; if black is 0.35, not black is 0.65.
  - _why:_ The complement calculation is correct, but two exhaustive probabilities add to 1, not 2. The correct completed statement uses 1 and 0.65.
- If there are only two possible outcomes, their probabilities add to 1; if black is 0.35, not black is 0.35.
  - _why:_ Two possible outcomes add to 1, but the complement of 0.35 is found by subtracting from 1, giving 0.65 rather than repeating 0.35.
- If there are only two possible outcomes, their probabilities add to 0.99; if black is 0.35, not black is 0.75.
  - _why:_ Neither value follows the complement rule: exhaustive probabilities add to 1, and not black is $1-0.35=0.65$. The values 0.99 and 0.75 result from incorrect subtraction.

## Card 14 — `basic`

**Front:** In the tie example, what is $P(\text{different coloured ties})$?

**Back:** $$0.6775$

**Choices:**

- $$0.6775$ ✔
  - _why:_ The different-coloured tie outcomes together have probability 0.6775 in the tie example. This is found by adding the probabilities of all tie outcomes involving different colours.
- $$0.3225$
  - _why:_ This is the complement of the required probability, representing same-coloured rather than different-coloured ties. The probability of different-coloured ties is $0.6775$.
- $$0.675$
  - _why:_ This is a near-miss from rounding or copying one component of the calculation, but it does not equal the total of the relevant different-coloured tie outcomes. The correct value is $0.6775$.
- $$0.7225$
  - _why:_ This overestimates the total by including an outcome that is not a different-coloured tie. Adding only the required outcomes gives $0.6775$.

## Card 15 — `basic`

**Front:** Six number cards are chosen two at a time without replacement. How many ordered selections are possible?

**Back:** $$6\times5=30$

**Choices:**

- $$6\times5=30$ ✔
  - _why:_ The first card has 6 choices and, without replacement, the second has 5 remaining choices. Since order matters, the number of ordered selections is $6\times5=30$.
- $$6+5=11$
  - _why:_ Adding the numbers counts 6 plus 5 rather than forming ordered pairs. The multiplication rule is needed: 6 choices for the first card and 5 for the second, giving 30.
- $$6\times6=36$
  - _why:_ This allows the same card to be selected again, as though replacement occurred. Without replacement, the second choice has 5 possibilities, so the correct total is 30.
- $$5\times4=20$
  - _why:_ This starts with only 5 choices and then reduces to 4, omitting one possible first card. The correct calculation is 6 choices followed by 5 choices, giving 30.

## Card 16 — `basic`

**Front:** For cards 1, 1, 2, 3, 3, 4, how many ordered selections have the second number greater than the first?

**Back:** 13

**Choices:**

- 13 ✔
  - _why:_ Count each possible first card and the higher-valued second cards: the two 1s give 8 choices, the 2 gives 3, and the two 3s give 2. Altogether, $8+3+2=13$.
- 10
  - _why:_ This undercounts the repeated 1s or 3s by treating equal-valued cards as a single card. Ordered selections use individual cards, so the correct total is 13.
- 15
  - _why:_ This includes some selections where the second number is equal to or lower than the first. Only strictly greater second numbers count, giving 13 ordered selections.
- 6
  - _why:_ This counts only the distinct number values rather than the six individual cards, so it misses the extra choices created by the repeated 1s and 3s. The correct answer is 13.

## Card 17 — `basic`

**Front:** For cards 1, 1, 2, 3, 3, 4, what is $P(\text{second greater than first})$?

**Back:** $$\frac{13}{30}$

**Choices:**

- $$\frac{13}{30}$ ✔
  - _why:_ There are 30 ordered draws without replacement. Of these, 13 have a second card whose value is strictly greater than the first card’s value.
- $$\frac{1}{2}$
  - _why:_ This assumes symmetry gives half the outcomes, but equal-value draws involving the repeated 1s or 3s are possible. Excluding ties leaves the correct probability $\frac{13}{30}$.
- $$\frac{13}{15}$
  - _why:_ This counts the 13 favourable unordered pairs but fails to use the 30 equally likely ordered draws. The required probability is therefore $\frac{13}{30}$.
- $$\frac{17}{30}$
  - _why:_ This includes the four ordered outcomes where the two cards have equal values, so it represents “greater than or equal to”. Strictly greater gives $\frac{13}{30}$.

## Card 18 — `cloze`

**Front:** A Venn diagram uses overlapping circles to organise information about [ ___ ].

**Back:** A Venn diagram uses overlapping circles to organise information about sets.

**Choices:**

- sets ✔
  - _why:_ A Venn diagram represents sets using circles, with overlapping regions showing elements that belong to two or more sets simultaneously.
- outcomes
  - _why:_ Outcomes are possible results of an experiment and are usually organised in a sample space. Venn diagrams specifically use overlapping circles to organise sets.
- frequencies
  - _why:_ Frequencies record how often values occur and are commonly displayed in tables or charts. The objects organised by a Venn diagram are sets.
- coordinates
  - _why:_ Coordinates locate points using ordered pairs and are plotted on axes. Venn diagrams instead organise information about sets and their intersections.

## Card 19 — `basic`

**Front:** In the survey Venn example, 48 people were surveyed and 6 liked none. How many are inside the circles?

**Back:** $$48-6=42$

**Choices:**

- $$48-6=42$ ✔
  - _why:_ The 6 people who liked none are outside every circle, so subtracting them from all 48 surveyed people leaves 42 inside the circles.
- $$48+6=54$
  - _why:_ Adding the 6 people who liked none double-counts people outside the circles rather than removing them. The number inside is $48-6=42$.
- $$48-8=40$
  - _why:_ This subtracts the 8 people who liked all three, but they are inside the circles and must remain included. Subtracting the 6 who liked none gives $48-6=42$.
- $$48-17=31$
  - _why:_ The 17 people who liked tea and coffee are inside the circles, so they should not be removed. Only the 6 who liked none are subtracted, giving $48-6=42$.

## Card 20 — `basic`

**Front:** In the survey Venn example, 17 like tea and coffee altogether and 8 like all three. How many are tea-and-coffee-only?

**Back:** $$17-8=9$

**Choices:**

- $$17-8=9$ ✔
  - _why:_ The total of 17 includes the 8 people who like all three drinks. Removing those 8 leaves 9 who like tea and coffee only.
- $$17+8=25$
  - _why:_ Adding includes the all-three group twice rather than removing it from the tea-and-coffee total. The tea-and-coffee-only region is $17-8=9$.
- $$17-9=8$
  - _why:_ This reverses the required subtraction by removing the tea-and-coffee-only value from the total. Subtracting the 8 who like all three from 17 gives $17-8=9$.
- $$17-6=11$
  - _why:_ The 6 people who like none are unrelated to the tea-and-coffee overlap. The 8 who like all three must be removed from 17, giving $17-8=9$.

## Card 21 — `basic`

**Front:** In the survey Venn example, how many people like coffee after completing the diagram?

**Back:** 24

**Choices:**

- 24 ✔
  - _why:_ Adding every disjoint region contained within the coffee circle, including its overlaps with the other circles, gives a total of 24 people.
- 17
  - _why:_ The value 17 counts people who like both tea and coffee altogether, not everyone in the coffee circle. Summing all coffee regions gives 24.
- 8
  - _why:_ The value 8 counts only people in the three-way intersection, so it omits the other coffee-containing regions. The complete coffee total is 24.
- 42
  - _why:_ The value 42 is the number inside any of the circles, including people who may not like coffee. Only the coffee regions sum to 24.

## Card 22 — `basic`

**Front:** In the survey Venn example, 24 of 48 people like coffee. Two are chosen without replacement. What is $P(\text{both like coffee})$?

**Back:** $$\frac{24}{48}\times\frac{23}{47}=\frac{23}{94}$

**Choices:**

- $$\frac{24}{48}\times\frac{23}{47}=\frac{23}{94}$ ✔
  - _why:_ The first probability is $24/48$. After one coffee-liker is selected, 23 coffee-likers remain among 47 people, giving the product $\frac{23}{94}$.
- $$\frac{24}{48}\times\frac{24}{48}=\frac{1}{4}$
  - _why:_ This treats the selections as if the first person were replaced, leaving both numbers unchanged. Without replacement, the second probability is $23/47$, giving $\frac{23}{94}$.
- $$\frac{24}{48}\times\frac{24}{47}=\frac{12}{47}$
  - _why:_ This reduces the total from 48 to 47 but fails to reduce the number of coffee-likers from 24 to 23. The correct product is $\frac{24}{48}\times\frac{23}{47}=\frac{23}{94}$.
- $$\frac{24}{48}\times\frac{23}{48}=\frac{23}{96}$
  - _why:_ This removes one coffee-liker but incorrectly keeps the total at 48. Since one person has also left the survey group, the second denominator is 47, giving $\frac{23}{94}$.
