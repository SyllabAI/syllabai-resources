# grade-3-3-18-frequency-trees — lesson

_Lane: `igcse-maths-edexcel` · grade 3 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What a frequency tree shows

![Frequency tree with total 120 splitting into male 58 and female 62, then tea and coffee totals on each branch](../assets/001-8f32f14b-19da-42e4-8d6c-5d273518cd7a.jpeg)

A frequency tree shows counts as a group splits into categories. Unlike a probability tree, the numbers are actual frequencies, so they do not add to 1.

Each parent total splits into two child totals that must add back to the parent. The starting number is the root, and the end numbers are joint frequencies because they satisfy two conditions at once.

## Finding a missing part

Most missing values come from whole, part, part. If 90 students split into 37 in Year 10 and the rest in Year 11, subtract to find the missing part.

$$$90 - 37 = 53$$

So 53 are in Year 11. A quick check is $37 + 53 = 90$, which matches the original total.

## Worked example: complete the tree

40 students took an English test and a science test. If 31 passed English, then the number who failed English is: $$40 - 31 = 9$$

Now stay inside the passed English branch. Of these 31 students, 27 passed science, so the number who failed science is: $$31 - 27 = 4$$

Next use the failed English branch total of 9. If 4 of these failed science, then the number who passed science is: $$9 - 4 = 5$$

The four end values are 27, 4, 5 and 4, so the tree is complete and they add to 40. Notice that the second and third subtractions used branch totals 31 and 9, not the overall total 40.

## When a total sits across both branches

![Completed frequency tree for 100 people split into male and female, then cats and dogs, with counts 46, 54, 13, 33, 32 and 22](../assets/002-3aa954dd-0664-486e-951d-7ef748450deb.jpeg)

Sometimes a clue such as "55 preferred dogs" is a total across both first branches, so you cannot place it on just one side straight away. First find the female total by subtracting the males from the grand total: $100 - 46 = 54$.

Now complete the female branch. If 32 females preferred cats, then females who preferred dogs are $54 - 32 = 22$. Using the overall dog total of 55, the males who preferred dogs are $55 - 22 = 33$.

Finally, the males who preferred cats are $46 - 33 = 13$. A quick check gives a cat total of $13 + 32 = 45$, and $45 + 55 = 100$. This check shows the tree is consistent.

## Turning a completed tree into probability

Once a tree is complete, you can answer probability questions by dividing a frequency by a total. For a random choice from the whole sample, the denominator is the root total.

In the cats and dogs example, $P(\text{dogs}) = \frac{55}{100} = \frac{11}{20}$. The numerator is the dog frequency, and the denominator is the whole sample of 100 people.

If the question says "given female", use the female branch total as the denominator instead. So $P(\text{cats} \mid \text{female}) = \frac{32}{54} = \frac{16}{27}$, not $\frac{32}{100}$.

## Fraction clues in a branch

A clue like $\frac{2}{3}$ of the boys refers only to the boys branch. Multiply the branch total by the fraction, not the overall total. If there are 72 students and 30 are boys, then boys who play football are:

$$$30 \times \frac{2}{3} = 20$$

So 20 boys play football and $30 - 20 = 10$ boys do not. If 18 girls play football, then the girls total is $72 - 30 = 42$ and girls who do not play football are $42 - 18 = 24$.

## Check yourself

1. In a frequency tree, what must be true at every split?

   - The two branch totals add to the parent total ✔

   - The two branch totals always add to 1

   - The left branch is always larger than the right branch

   - The end values must all be equal

   _Explanation:_ A frequency tree is built from counts, so the two child frequencies must add back to the parent total. The common wrong answer is B, which confuses a frequency tree with a probability tree, where probabilities from a split add to 1.

2. In the cats and dogs example, why do we calculate $55 - 22$?

   - To find the number of males who preferred dogs ✔

   - To find the number of females who preferred cats

   - To find the total number of males

   - To find the total number of people who preferred cats

   _Explanation:_ The 55 is the total number of people who preferred dogs, and 22 of these are females, so subtracting gives the males who preferred dogs. The common wrong answer is D, but the cat total would be found from $100 - 55 = 45$, not from $55 - 22$.

3. A survey has 84 people. 36 are adults, so 48 are children. $\frac{3}{4}$ of the children own a bike. How many children do not own a bike?

   - 12 ✔

   - 36

   - 16

   - 9

   _Explanation:_ $$\frac{3}{4}$ of 48 is 36, so 36 children own a bike and the remaining $48 - 36 = 12$ do not. The common wrong answer is B, which gives the number who own a bike instead of the number who do not.
