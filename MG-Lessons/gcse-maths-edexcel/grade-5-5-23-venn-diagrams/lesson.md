# grade-5-5-23-venn-diagrams — lesson

_Lane: `gcse-maths-edexcel` · grade 5 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## What a Venn diagram shows

![Two-circle Venn diagram inside a rectangle labelled universal set E, with regions A only, overlap, B only, and outside both](../assets/001-e879bc92-8f8d-432d-bf49-347f993ca472.jpeg)

A Venn diagram shows sets inside a rectangle called the universal set, written $\mathcal{E}$. Each separate area is a region, so in a two-circle diagram you can talk about A-only, B-only, the overlap, and the outside region.

The intersection, written $A \cap B$, means "in both sets". The union, written $A \cup B$, means "in A or B or both".

The complement of $A$, written $A'$, means everything in $\mathcal{E}$ that is not in $A$. If an item is either in $A$ or not in $A$, then the probabilities satisfy $P(A)+P(A')=1$.

## Shading regions correctly

When you shade a region, translate each symbol one step at a time. The symbol $\cap$ means "and", so look for the common part, while $\cup$ means "or", so include every region that fits at least one condition.

For example, $A \cap B'$ means in $A$ but not in $B$, so you shade only the A-only region. Also, $A' \cap B'$ means outside both circles.

For a mixed expression such as $A' \cup B$, begin with everything not in $A$ and then add all of $B$. The only region left unshaded is the A-only region.

## Completing a two-circle diagram from totals

In a survey of 48 pupils, 26 had visited Wales, 21 had visited Ireland, and 9 had visited both. Put 9 in the overlap first because it is the most specific information.

Subtract the overlap from each circle total to find the "only" regions. Wales only is $26-9=17$, and Ireland only is $21-9=12$.

Now find how many are in at least one circle: $17+9+12=38$. The number in neither is $48-38=10$, and the check $17+9+12+10=48$ confirms the diagram is complete.

## Three-circle diagrams from the centre out

![Three-circle Venn diagram inside a rectangle, with circles R, F, and C, showing the centre and the pair-only overlap regions](../assets/002-557585b7-e853-4e6c-aab6-5de3a1333279.jpeg)
In a survey of 60 students, 7 like rugby, football, and cricket. Put 7 in the centre first because every pair total includes this middle region.

Now find the pair-only regions by subtracting the centre. Rugby and football only is $18-7=11$, football and cricket only is $14-7=7$, and rugby and cricket only is $16-7=9$.

Use the circle totals next. Rugby only is $30-11-9-7=3$, football only is $34-11-7-7=9$, and cricket only is $28-9-7-7=5$.

Add every region inside the circles to get $51$. So the number who like none is $60-51=9$.

## Probability from a completed diagram

Sometimes the universal set and the sets are given as lists instead of totals. Let $\mathcal{E}=\{2,4,6,8,10,12,14,16,18\}$, $A=\{2,4,8,12,18\}$, and $B=\{4,6,12,14\}$.

The overlap is $\{4,12\}$, so A-only is $\{2,8,18\}$ and B-only is $\{6,14\}$. The numbers outside both sets are $\{10,16\}$.

If one element is chosen at random, the denominator is the whole universal set, which has 9 elements. Since $A \cup B$ contains 7 elements, $P(A \cup B)=\frac{7}{9}$.

## Check yourself

1. Which part of a two-circle Venn diagram represents $A \cap B$?

   - Only the overlapping middle region ✔

   - All regions inside either circle

   - Only the part inside $A$ but not $B$

   - The region outside both circles

   _Explanation:_ $$A \cap B$ means items in both sets, so only the overlapping middle region fits. The most common wrong answer is B, but that is the union $A \cup B$, which includes the A-only and B-only regions as well.

2. 50 people were asked whether they have a dog or a cat. 31 have a dog, 27 have a cat, and 8 have neither. How many have both?

   - 16 ✔

   - 4

   - 8

   - 42

   _Explanation:_ Since 8 have neither, $50-8=42$ have at least one pet. Adding the dog and cat totals gives $31+27=58$, which counts the overlap twice, so the number with both is $58-42=16$. The most common wrong answer is 42, but that is the number with at least one pet, not the overlap.

3. A universal set has 12 elements. Set $A$ has 7 elements, set $B$ has 6 elements, and $n(A \cap B)=3$. What is $P((A \cup B)')$?

   - $$\frac{1}{6}$ ✔

   - $$\frac{5}{6}$

   - $$\frac{1}{4}$

   - $$\frac{1}{2}$

   _Explanation:_ First find the union: $7+6-3=10$. That leaves $12-10=2$ elements outside the union, so $P((A \cup B)')=\frac{2}{12}=\frac{1}{6}$. The most common wrong answer is $\frac{5}{6}$, but that is $P(A \cup B)$, not the complement.
