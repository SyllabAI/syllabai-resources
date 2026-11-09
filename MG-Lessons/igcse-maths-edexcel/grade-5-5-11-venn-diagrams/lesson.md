# grade-5-5-11-venn-diagrams — lesson

_Lane: `igcse-maths-edexcel` · grade 5 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Sets, regions, and the universal set

![Two-set Venn diagram inside universal set E with regions A only, A intersection B, B only, and neither labelled.](../assets/001-1802974b-e798-438a-a1a6-24d2fb6271e5.jpeg)
A Venn diagram sorts members into sets. A set is a collection of items, and the rectangle is the universal set $E$, which contains everything being considered.

In a two-set diagram there are four main regions: A only, $A \cap B$, B only, and neither. The overlap $A \cap B$ belongs to both sets at the same time.

When placing items, start with the most specific region first. This helps you avoid double-counting later.

## Reading the symbols

$$A'$ means the complement of A, which is everything in the universal set that is not in A. In probability, this gives the rule $P(A') = 1 - P(A)$.

$$A \cap B$ means A and B, so shade only the overlap. $A \cup B$ means A or B or both, so the overlap must be included.

For example, $A' \cup B$ means outside A or inside B. The only region left out is A only.

## Worked example with two sets

When totals are given, remember that each circle total already includes the overlap. The key counting rule is:

$$$n(A \cup B)=n(A)+n(B)-n(A \cap B)$$

Let $I$ be students who have visited Italy and $G$ be students who have visited Germany. If $n(I)=21$, $n(G)=18$, $n(I \cap G)=7$, and there are 36 students altogether, put 7 in the overlap first.

Then work out the single-only regions: Italy only is $21-7=14$ and Germany only is $18-7=11$. So the number in at least one set is $14+7+11=32$.

Finally, the number in neither set is $36-32=4$. Check by adding back inside each circle: $14+7=21$ and $11+7=18$, so the diagram is consistent.

## Three-set diagrams: centre outwards

![Three-set Venn diagram labelled A, B, C and E with arrows showing centre first, then pair-only regions, then single-only regions, then outside.](../assets/002-ef4b82b7-4fb9-40f8-957e-3b474475109f.jpeg)

For three sets, always fill the centre first and then work outwards. The centre $A \cap B \cap C$ is included in every pair total and every single-set total, so leaving it until later causes mistakes.

Consider a survey of 60 students: 4 like art, basketball, and choir, 15 like art and basketball, 12 like basketball and choir, 14 like art and choir, 31 like art, 35 like basketball, and 28 like choir. Start by placing 4 in the centre.

The pair-only overlaps are found by subtracting the centre: art and basketball only is $15-4=11$, basketball and choir only is $12-4=8$, and art and choir only is $14-4=10$. Then the single-only regions are art only $31-11-10-4=6$, basketball only $35-11-8-4=12$, and choir only $28-10-8-4=6$.

Add the seven inside regions to get $4+11+8+10+6+12+6=57$. So the number who like none of the three activities is $60-57=3$.

## Using Venn diagrams for probability

Probability is defined as the ratio of favourable outcomes to the total number of possible outcomes:
$$
\frac{\text{favourable outcomes}}{\text{total outcomes}}
$$
In a Venn diagram question, the total outcomes are usually represented by the total number of members in the universal set.

Suppose $E=\{3,6,9,12,15,18,21,24,27,30\}$, $A=\{3,6,12,18,24\}$, and $B=\{6,15,18,21,30\}$. The overlap is $A \cap B=\{6,18\}$, so set A only has 3 unique members outside the intersection and B only has 3 unique members outside the intersection, making 8 members in $A \cup B$.

To find the probability of the union, we divide the count of elements in the combined region by the count of the universal set:
$$
P(A \cup B)=\frac{8}{10}=\frac{4}{5}
$$
Count how many members are in the region you want. Do not add the values of the numbers unless the question specifically asks for a sum.

## Check yourself

1. In a two-set Venn diagram, what does $A \cap B$ mean?

   - members in both A and B ✔

   - members in A or B or both

   - members not in A

   - members only in B

   _Explanation:_ $$A \cap B$ is the intersection, so it is the overlap only. The common wrong answer is "members in A or B or both", but that is $A \cup B$, the union.

2. 50 people are asked whether they have a brother or a sister. 28 have a brother, 24 have a sister, and 6 have neither. How many have both?

   - 8 ✔

   - 14

   - 20

   - 44

   _Explanation:_ First find how many have at least one: $50-6=44$. Then $28+24=52$, which counts the overlap twice, so the overlap is $52-44=8$. The common wrong answer is 44, but that is the number with at least one, not the number with both.

3. Stretch: Using the sets in the previous card, what is $P(A' \cup B)$?

   - $$\frac{7}{10}$ ✔

   - $$\frac{8}{10}$

   - $$\frac{5}{10}$

   - $$\frac{3}{10}$

   _Explanation:_ $$A' \cup B$ means outside A or in B. The only elements excluded are the A-only elements $\{3,12,24\}$, so 7 of the 10 elements are included. The common wrong answer is $\frac{8}{10}$, which is $P(A \cup B)$, not $P(A' \cup B)$. Hint: It can be quicker to work out which region is not included.
