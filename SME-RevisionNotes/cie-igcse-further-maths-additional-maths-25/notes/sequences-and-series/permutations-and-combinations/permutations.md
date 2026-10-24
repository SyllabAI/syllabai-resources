---
note_id: "rn_zcmd4drQzqt5ZPtV"
title: "Permutations"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/sequences-and-series/permutations-and-combinations/permutations
path: sequences-and-series/permutations-and-combinations/permutations
updated_at: "2026-07-02T08:19:38.202Z"
spec_point_ids: ["spcpt_jYCdPVrS3gNFw5JW", "spcpt_8R5wf3qRTj6JYQj3", "spcpt_VkKccRJhrmwPw7tM"]
spec_point_codes: []
guided_study: false
---

# Permutations

## Arrangements

> **Spec point** — `spcpt_jYCdPVrS3gNFw5JW`

## Arrangements

### How many ways can n different objects be arranged?

- When arranging **different **objects in a row, consider how many of the objects can go in the first position, how many can go in the second and so on

  - For example, if $n=2$ there are two options for the first position and then there will only be one object left to go in the second position
  
    - So a total of 2 × 1 = 2 possible arrangements
    - To arrange the letters A and B we have
    
      - AB and BA
  - For example, if $n=3$ there are three options for the first position and then there will be two objects for the second position and one left to go in the third position
  
    - So a total of 3 × 2 × 1 = 6 possible arrangements
    - To arrange the letters A, B and C we have
    
      - ABC, ACB, BAC, BCA, CAB and CBA
- For *n* objects there are $n$ options for the first position, $n-1$ options for the second position and so on until there is only one object left to go in final position

  - The number of ways of arranging different objects is $n\times(n-1)\times(n-2)\times...\times2\times1$

> **Worked Example**
> By considering the number of options there are for each letter to go into each position, find how many distinct arrangements there are of the letters in the word MATHS.
> 
> *There are 5 different letters in the word MATHS, so there are 5 letters for the first space, then there will be four for the second, three for the third and so on.  *
> 
> $5\times4\times3\times2\times1$
> 
> **Final answer:** **120 distinct arrangements**

## Factorials

> **Spec point** — `spcpt_8R5wf3qRTj6JYQj3`

## Factorials

### What are factorials?

- Factorials are a type of mathematical operation (just like +, -, ×, ÷)
- The symbol for factorial is !

  - So to take a factorial of any non-negative integer, $n$ , it will be written $n$!  And pronounced ‘ $n$ *factorial’*
- The factorial function for any integer, $n$, is $n!=n\times(n-1)\times(n-2)\times...\times2\times1$

  - For example, 5 factorial is 5! = 5 × 4 × 3 × 2 × 1
- The factorial of a negative number is not defined

  - You cannot arrange a negative number of items
- 0! = 1

  - There are no positive integers less than zero, so zero items can only be arranged once
- Most normal calculators cannot handle numbers greater than about 70!, experiment with yours to see the greatest value of $x$ such that your calculator can handle $x!$

### How are factorials and arrangements linked?

- The number of arrangements of $n$ different objects is $n!$

  - Where $n!=n\times(n-1)\times(n-2)\times...\times2\times1$

### What are the key properties of using factorials?

- Some important relationships to be aware of are:

  - $n!=n\times(n-1)!$
  
    - Therefore

$\frac{n!}{(n-1)!}=n$

- $n!=n\times(n-1)\times(n-2)!$

  - Therefore

$\frac{n!}{(n-2)!}=n\times(n-1)$

- Expressions with factorials in can be simplified by considering which values cancel out in the fraction

  - Dividing a large factorial by a smaller one allows many values to cancel out

$\frac{7!}{4!}=\frac{7\times6\times5\times4\times3\times2\times1}{4\times3\times2\times1}=7\times6\times5$

> **Exam Hint**
> - Arrangements and factorials are tightly interlinked with permutations and combinations
> - Make sure you fully understand the concepts in this revision note as they will be fundamental to answering perms and combs exam questions!

> **Worked Example**
> (i) Show, by writing 8! and 5! in their full form and cancelling, that
> 
> $\frac{8!}{5!}=8\times7\times6$
> 
> (ii)$\begin{gathered} \\ \end{gathered}$ Hence, simplify  $\frac{n!}{(n-3)!}$
> 
> > *(i)   Write 5! and 8! in their full form.   *
> 
> $5!=5\times4\times3\times2\times1$
> 
> $8!=8\times7\times6\times5\times4\times3\times2\times1$
> 
> *Write them as a fraction and cancel out common terms*
> 
> $\frac{8!}{5!}=\frac{8\times7\times6\times5\times4\times3\times2\times1}{5\times4\times3\times2\times1}$
> 
> $\frac{8!}{5!}=8\times7\times6$
> 
> (ii) *'Hence' means using the information in the previous question. Let **n **be 8*
> 
> `n = 8 , (n factorial)/(( n - 3 ) factorial) = (8 factorial)/(( 8 - 3 ) factorial) = (8 factorial)/(5 factorial) and (8 factorial)/(5 factorial) = 8 x 7 x 6`
> 
> *Then 5 = **n **- 3 , 6 = **n **- 2, 7 = **n **- 1     *
> 
> $\frac{n!}{(n-3)!}=n(n-1)(n-2)$

## Permutations

> **Spec point** — `spcpt_VkKccRJhrmwPw7tM`

## Permutations

### Are permutations and arrangements the same thing?

- Mathematically speaking yes, a **permutation** is the number of possible arrangements of a set of objects when the **order **of the arrangements matters
- A permutation can either be finding the number of ways to arrange *n*  items or finding the number of ways to arrange *r*  out of *n* items
- The number of permutations of *n* **different **items is $n \text{factorial} = n \times ( n - 1 ) \times ( n - 2 ) \times... \times 2 \times 1$

  - For 5 **different **items there are 5! = 5 × 4 × 3 × 2 = 120 permutations
  - For 6 **different **items there are 6! = 6 × 5 × 4 × 3 × 2 = 720  permutations
  - It is easy to see how quickly the number of possible permutations of different items can increase
  - For 10 different items there are 10! = 3 628 800 possible permutations

### How do we find r  permutations of n items?

- If we only want to find the number of ways to arrange a few out of *n*  different objects, we should consider how many of the objects can go in the first position, how many can go in the second and so on
- If we wanted to arrange 3 out of 5 different objects, then we would have 3 positions to place the objects in, but we would have 5 options for the first position, 4 for the second and 3 for the third

  - This would be 5 × 4 × 3 ways of permutating 3 out of 5 different objects
  - This is equivalent to $\frac{5 factorial}{2 factorial} = \frac{5 factorial}{( 5 - 3 ) factorial}$
- If we wanted to arrange 4 out of 10 different objects, then we would have 4 positions to place the objects in, but we would have 10 options for the first position, 9 for the second, 8 for the third and 7 for the fourth

  - This would be 10 × 9 × 8 × 7 ways of permutating 4 out of 10 different objects
  - This is equivalent to $\frac{10!}{6!}=\frac{10!}{(10-4)!}$
- If we wanted to arrange *r* out of *n* different objects, then we would have *r* positions to place the objects in, but we would have *n* options for the first position, $( n - 1 )$ for the second, $( n - 2 )$ for the third and so on until we reach $( n - ( r - 1 ) )$

  - This would be $n \times ( n - 1 ) \times... \times ( n - r + 1 )$ ways of permutating r out of n different objects
  - This is equivalent to $\frac{n factorial}{( n - r ) factorial}$
- The function $\frac{n!}{(n-r)!}$can be written as $\mathrm{P} pre^{n}_{r}$

  - Make sure you can find and use this button on your calculator
- The same function works if we have *n *spaces into which we want to arrange *r *objects, consider

  - for example arranging five people into a row of ten empty chairs

### Permutations when two or more items must be together

- If two or more items must stay together within an arrangement, it is easiest to think of these items as ‘stuck’ together
- These items will become one within the arrangement
- Arrange this ‘one’ item with the others as normal
- Arrange the items within this ‘one’ item separately
- Multiply these two arrangements together

### Permutations when two or more items cannot be all together

- If **two** items must be **separated …**

  - consider the number of ways these two items would be together
  - subtract this from the total number of arrangements without restrictions
- If **more than two** items must be separated…

  - consider whether all of them must be **completely separate** (none can be next to each other) or whether they **cannot all be together** (but two could still be next to each other)
  - If they **cannot all be together** then we can treat it the same way as separating two items and subtract the number of ways they would all be together from the total number of permutations of the items, the final answer will include all permutations where two items are still together

### Permutations when more than two items must be separated

- If the items must all be **completely separate** then

  - lay out the rest of the items in a line with a space in between each of them where one of the items which cannot be together could go
  - remember that this could also include the space before the first and after the last item
  - You would then be able to fit the items which cannot be together into any of these spaces, using the *r *permutations of *n *items rule `equation`
  - You do not need to fill every space

### Permutations when two or more items must be in specific places

- Most commonly this would be arranging a word where specific letters would go in the first and last place
- Or arranging objects where specific items have to be at the ends/in the middle

  - Imagine these specific items are stuck in place, then you can find the number of ways to arrange the rest of the items around these ‘stuck’ items
- Sometimes the items must be grouped

  - For example all vowels must be before the consonants
  - Or all the red objects must be on one side and the blue objects must be on the other
  - Find the number of permutations within each group separately and multiply them together
  - Be careful to check whether the groups could be in either place
  
    - e.g. the vowels on one side and consonants on the other
    - or if they must be in specific places (the vowels **before** the consonants)
  - If the groups could be in either place than your answer would be multiplied by two
  - If there were *n* groups that could be in any order then your answer would be multiplied by *n*!

> **Exam Hint**
> - The wording is very important in permutations questions, just one word can change how you answer the question
> - Look out for specific details such as whether three items must all be separated or just cannot be all together (there is a difference)
> - Pay attention to whether items must be in alternating order (e.g. red and blue items must alternate, either RBRB… or BRBR…) or whether a particular item must come first (red **then **blue and so on)
> - If items should be at the ends, look out for whether they can be at either end or whether one must be at the beginning and the other at the end

> **Worked Example**
> a) How many ways are there to rearrange the letters in the word EXAMS if the E and the S must be at each end?
> 
> > *   *
> 
> *'Stick' the E and the S at each end.*  *Be careful here, the question says 'at each end' so the E and the S could each go at either end. *
> 
> > *   *
> 
> *E _ _ _ S*
> 
> *or*
> 
> *S _ _ _ E   *
> 
> > *Find the number of arrangements of the remaining letters. *
> 
> > *  *
> 
> $3!=3\times2\times1$
> 
> > *Multiply by 2 as there were two positions the E and the S could go in.*
> 
> > * *
> 
> $2\times3!=2\times3\times2\times1$
> 
> **Final answer:** **12**
> 
> (b) Find the number of distinct four digit codes that can be made from the digits 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, where none of the digits can be used more than once.
> 
> > *There are ten numbers available and we want to find the number of arrangements of four of them.*
> 
> > *There are 10 numbers for the first position, 9 for the second, 8 for the third and 7 for the fourth.*
> 
> > *  *
> 
> $10\times9\times8\times7$
> 
> > *This is the same as *<sup>*10*</sup>*P*<sub>*4*</sub>*, (**n **= 10, **r **= 4).*
> 
> **Final answer:** **5040**
