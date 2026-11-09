# grade-3-3-19-frequency-trees — lesson

_Lane: `gcse-maths-edexcel` · grade 3 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Totals, parts, and frequencies

A frequency is a count, and a frequency tree shows how one total is split into categories such as boys and girls or tea and coffee. The first node is usually the grand total, and each new split breaks a group into smaller parts.

At every split, the two child numbers add back to the parent number. If one child is missing, use the following calculation to find the value:

$$$\text{missing child} = \text{parent total} - \text{known child}$$

For example, if $90$ students are split into set A and set B, and $34$ are in set A, then set B has $90 - 34 = 56$. This same add-then-subtract idea is the backbone of every frequency tree question.

## Reading a tree from left to right

![Frequency tree with total 80 splitting into boys 43 and girls 37, then to drink A and drink B with end counts 31, 12, 21, and 16](../assets/001-da0264cd-6812-4069-94c9-aa3f90179ade.jpeg)

Read a frequency tree from left to right. The end numbers tell you the combined groups, such as boys who choose drink A or girls who choose drink B.

In this tree, $43 + 37 = 80$, so the first split matches the total. The next split happens inside each group, so $31 + 12 = 43$ for boys and $21 + 16 = 37$ for girls.

Be careful with a statement like "52 choose drink A". That total belongs to drink A across both boys and girls, not just one branch. A common mistake is to place an overall total on only one subgroup.

## Worked example: complete missing frequencies

Suppose $80$ students choose either drink A or drink B. The tree splits first into boys and girls, and you know there are $37$ girls, $52$ students choosing drink A in total, and $21$ girls choosing drink A.

Start with the first split: boys $= 80 - 37 = 43$. On the girls branch, girls choosing drink B $= 37 - 21 = 16$.

Now use the overall drink A total: boys choosing drink A $= 52 - 21 = 31$. Then boys choosing drink B $= 43 - 31 = 12$.

Finish with two checks: $31 + 21 = 52$ for all drink A students, and $31 + 12 + 21 + 16 = 80$ overall. If both checks work, the tree is complete.

## Fraction clues: watch the words "of the"

When a question says "$\frac{3}{4}$ of the football students", the group after "of the" is the total you must use. The rule is $$\text{part} = \text{group total} \times \text{fraction}$$ so you multiply the football total, not the grand total.

Example: there are $72$ students in total, $48$ go to football, and $54$ go on Saturday altogether. So rugby $= 72 - 48 = 24$. If $\frac{3}{4}$ of the football students go on Saturday, then football Saturday $= 48 \times \frac{3}{4} = 36$.

Now finish the other branches using subtraction. Football Sunday $= 48 - 36 = 12$. Since there are $54$ Saturday students altogether, rugby Saturday $= 54 - 36 = 18$. Then rugby Sunday $= 24 - 18 = 6$.

Check both routes at the end: $36 + 18 = 54$ for all Saturday students, and $18 + 6 = 24$ for rugby students. This shows the fraction was applied to the correct group.

## Probability from a completed tree

Once the tree is complete, probability is $\frac{\text{number wanted}}{\text{number possible}}$. The key skill is choosing the correct denominator, because it must match the group you are selecting from.

If there are $70$ people in total and $12$ are left-handed females, then choosing one person from everybody gives probability $\frac{12}{70} = \frac{6}{35}$. The denominator is $70$ because every person is possible.

If the question changes to "one of the left-handed people is chosen", the denominator changes as well. Then the probability is $\frac{12}{30} = \frac{2}{5}$, because only the $30$ left-handed people are possible now.

In exams, circle the words that tell you the starting group, such as "one of the girls" or "one of the people who do not like football". That one number decides the denominator.

## Check yourself

1. In any frequency tree split, which statement is always true?

   - The parent frequency equals the two child frequencies added together ✔

   - The parent frequency equals the larger child minus the smaller child

   - The two child frequencies must be equal

   - The branch label gives the frequency

   _Explanation:_ The correct answer is A because a split divides one whole group into all of its parts, so the child frequencies must add back to the parent. The most common wrong answer is B, because subtraction is only a method for finding a missing part; once the tree is complete, the relationship is still addition.

2. In the worked example above, what does the 52 students choosing drink A represent?

   - All students who choose drink A, boys and girls together ✔

   - Boys who choose drink A only

   - Girls who choose drink A only

   - All students who choose drink B

   _Explanation:_ The correct answer is A because 52 is the overall total on the drink A category, so it must include both boys choosing A and girls choosing A. The most common wrong answer is B, which treats the overall total as if it belonged to one branch only and ignores the girls who also choose A.

3. A frequency tree starts with 75 students. It splits into boys and girls, then bus and walk. There are 35 boys. $\frac{2}{5}$ of the girls go by bus. 28 students go by bus in total. If one boy is chosen at random, what is the probability he goes by bus?

   - $$\frac{12}{35}$ ✔

   - $$\frac{12}{75}$

   - $$\frac{28}{75}$

   - $$\frac{16}{40}$

   _Explanation:_ There are $75 - 35 = 40$ girls, so girls by bus $= 40 \times \frac{2}{5} = 16$. That means boys by bus $= 28 - 16 = 12$, and because the question says one boy is chosen, the probability is $\frac{12}{35}$. The most common wrong answer is $\frac{12}{75}$, which uses the grand total even though the choice is restricted to boys.
