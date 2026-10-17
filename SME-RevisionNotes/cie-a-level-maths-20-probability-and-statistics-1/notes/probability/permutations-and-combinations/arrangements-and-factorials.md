---
note_id: "rn_99WzYCv7kmpHYv7D"
title: "Arrangements & Factorials"
source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/revision-notes/probability/permutations-and-combinations/arrangements-and-factorials
path: probability/permutations-and-combinations/arrangements-and-factorials
updated_at: "2026-07-02T08:19:38.466Z"
spec_point_ids: ["spcpt_7gKmB69fTvMSjrvw", "spcpt_v9GnPyX4sbCvf8Ff"]
spec_point_codes: []
guided_study: true
---

# Arrangements & Factorials

## Arrangements

> **Spec point** — `spcpt_7gKmB69fTvMSjrvw`

## Arrangements

#### How many ways can n different objects be arranged?

- When considering how many ways you can arrange a number of **different **objects in a row it’s a good idea to think of how many of the objects can go in the first position, how many can go in the second and so on
- For $n=2$ there are two options for the first position and then there will only be one object left to go in the second position so

  - To arrange the letters A and B we have
  
    - AB and BA
  - For $n=3$  there are three options for the first position and then there will be two objects for the second position and one left to go in the third position so
  
    - To arrange the letters A, B and C we have
    
      - ABC, ACB, BAC, BCA, CAB and CBA
    - For *n* objects there are $n$ options for the first position, $n-1$ options for the second position and so on until there is only one object left to go in final position
    - The number of ways of arranging different objects is $n\times(n-1)\times(n-2)\times...\times2\times1$

#### What happens if the objects are not all different?

- Consider arranging two identical objects, although there are still two different ways you could place the objects down next to each other, the arrangements would look exactly the same

- To arrange the letters A­<sub>1</sub> and A<sub>2</sub> we have

  - A­<sub>1 </sub>A<sub>2</sub> and A<sub>2 </sub>A­­<sub>­1</sub>
  - These are exactly the same, so there is only one way to arrange the letters A and A
- To arrange the letters A<sub>1</sub>, A<sub>2</sub> and C we have

  - A­<sub>1 </sub>A<sub>2 </sub>C, A­<sub>2 </sub>A­<sub>1 </sub>C, A­<sub>1 </sub>­­­C A­<sub>2</sub>, , A­<sub>2 </sub>C A<sub>1</sub>, C A­<sub>1 </sub>­­­A­<sub>2</sub>, C A­<sub>2 </sub>A­<sub>1</sub>
  - Although the two letter As were placed separately, they are identical and so each pattern has been repeated twice
  - There are 6 ways to arrange the letters A, A and C, but with some duplicates
  - There are $\frac{6}{2}=3$ different ways to arrange the letters A, A and C

- If there are two identical objects within a group of objects to be arranged, the number of ways of arranging different objects should be divided by 2

- Consider arranging three identical objects, although there are still six different ways you could place the objects down next to each other, the arrangements would look exactly the same

- To arrange the letters A<sub>1</sub>, A<sub>2</sub> and A<sub>3</sub>

  - A­<sub>1  </sub>A<sub>2</sub> A­<sub>3</sub> , A<sub>1  </sub>A<sub>3  </sub>A­<sub>2  </sub>, A­<sub>2  </sub>A<sub>1</sub> A­<sub>3</sub> , A<sub>2 </sub>A<sub>3 </sub>A­<sub>1</sub> , A­<sub>3 </sub>A<sub>1</sub> A­<sub>2</sub>  ,  A<sub>3 </sub>A<sub>2 </sub>A­<sub>1</sub>
  - However, if these were all A, we would have AAA repeated six times
- To find the number of arrangements of the letters A, A, A and C we would have to consider the number of ways of arranging four letters if they were all different and then divide by the number of ways AAA is repeated

  - Four different letters could be arranged $4\times3\times2\times1$ = 24 ways
  - AAA would be repeated six times so we would need to divide by 6
  - There are four **different** ways to arrange the letters A, A, A and C
- If there are three identical objects within a group of *n* objects to be arranged, the number of ways of arranging $n$ different objects should be divided by 6
- If there are *r*  identical objects within a group of *n* objects to be arranged, the number of ways of arranging $n$ different objects should be divided by the number of ways of arranging *r* different objects

  - If there are *r*  identical objects within a group of *n* objects to be arranged, the number of ways of arranging *n* the objects is $n\times(n-1)\times(n-2)\times...\times2\times1$  divided by  `r cross times open parentheses r minus 1 close parentheses cross times open parentheses r minus 2 close parentheses cross times... cross times 2 cross times 1`

> **Worked Example**
> By considering the number of options there are for each letter to go into each position, find how many different arrangements there are of the letters in the word REVISE.
> 
> **Answer:**
> 
> ![NMiqFoMp_2-2-1-arrangements-we-solution-1](assets/b5ff75195f3b-image.bin)

## Factorials

> **Spec point** — `spcpt_v9GnPyX4sbCvf8Ff`

## Factorials

#### What are factorials?

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

#### How are factorials and arrangements linked?

- The number of arrangements of $n$ different objects is $n!$

  - Where $n!=n\times(n-1)\times(n-2)\times...\times2\times1$
- The number of different arrangements of $n$objects with one object repeated $r$ times and the others all different is $\frac{n!}{r!}$
- The number of different arrangements of $n$objects with one object repeated $r$ times, another object repeated $s$times and the other objects all different is $\frac{n!}{r!s!}$

#### What are the key properties of using factorials?

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

> **Worked Example**
> (i) Show, by writing 8! and 5! in their full form and cancelling, that
> 
> $\frac{8!}{5!}=8\times7\times6$
> 
> (ii) Hence, simplify  $\frac{n!}{(n-3)!}$
> 
> (iii) The letters A, B, B, B, B, B, C and D are arranged in a row. How many different ways are there to arrange the 8 letters in a row?
> 
> **Answer:**
> 
> ![2-2-1-factorials-we-solution-2-](assets/688ef167496b-image.bin)

> **Exam Hint**
> - Arrangements and factorials are tightly interlinked with permutations and combinations
> - Make sure you fully understand the concepts in this revision note as they will be fundamental to answering perms and combs exam questions!
