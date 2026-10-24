---
note_id: "rn_bCTmd3kFGV9knYdQ"
title: "Combinations"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/sequences-and-series/permutations-and-combinations/combinations
path: sequences-and-series/permutations-and-combinations/combinations
updated_at: "2026-07-02T08:19:38.196Z"
spec_point_ids: ["spcpt_Mtg25yFQFXdCDYdC"]
spec_point_codes: []
guided_study: false
---

# Combinations

## Combinations

> **Spec point** — `spcpt_Mtg25yFQFXdCDYdC`

## Combinations

### What is the difference between permutations and combinations?

- A **combination** is the number of possible arrangements of a set of objects when the **order **of the arrangements **does not matter**

  - On the other hand a permutation is when the order of arrangement **does matter**
- A combination will be finding the number of ways to **choose** *r* out of *n* items

  - The order in which the *r *items are chosen is not important
  - For example if we are choosing two letters from the word CAB, AB and BA would be considered the same combination but different permutations

### How do we find r combinations of n items?

- If we want to find the number of ways to **choose*** *2 out of 3 different objects, but we don’t mind the order in which they are chosen, then we could find the number of **permutations of 2***** *****items from *****3 ***and then divide by the number of ways of arranging each combination

  - For example if we want to choose 2 letters from *A, B* and *C*
  
    - There are 6 permutations of 2 letters:
    - *AB, BA, AC, CA, BC, CB*
    - For each combination of 2 letters there are 2 (2 × 1) ways of arranging them
    - (for example, *AB* and *BA*)
    - So divide the total number of permutations (6) by the number of ways of arranging each combination (2) to get 3 combinations

- If we want to find the number of ways to **choose*** *3 out of 5 different objects, but we don’t mind the order in which they are chosen, then we could find the number of **permutations of 3***** *****items from *****5 ***and then divide by the number of ways of arranging each combination

  - For example if we want to choose 3 letters from *A, B, C, D* and *E*
  
    - There are 60 permutations of 3 letters:
    - *ABC, ACB, BAC, BCA, CAB, CBA, ABD, ADB*, etc
    - For each combination of 3 letters there are 6 (3 × 2 ×1) ways of arranging them (for example, *ABC, ACB, BAC, BCA, CAB* and *CBA*)
    - So divide the total number of permutations (60) by the number of ways of arranging each combination (3! = 6) to get 10 combinations

- If we want to find the number of ways to **choose** *r *items out of *n *different objects, but we don’t mind the order in which they are chosen, then we could find the number of **permutations of *****r *****items from *****n ***and then divide by the number of ways of arranging each combination
- Recall that the formula for *r *permutations of *n *items is

  - `P _ r _ _ ^ n = _ (n factorial)/(( n _ - _ r ) factorial)`
- This would include *r*! ways of repeating each combination
- The formula for *r ***combinations** of *n *items is

  - `( P _ r _ _ ^ n)/(r factorial) = _ (n factorial)/(( n _ - _ r ) factorial _ r factorial)`
- The function $\frac{n factorial}{( n - r ) \text{factorial} r factorial}$ can be written as `C _ r _ _ ^ n _`or $( \begin{gathered} n \\ r \end{gathered} )$ and is often read as ‘*n choose r’*

  - Make sure you can find and use this button on your calculator
- The formulae for permutations and combinations satisfy the following relationship:

- `C _ r _ _ ^ n = ( P _ r _ _ ^ n)/(r factorial) _`

### What do I need to know about combinations?

- The formula $C pre^{n}_{r} = \frac{n factorial}{( n - r ) \text{factorial} r factorial}$ is also known as a **binomial** coefficient
- `size 16px C presuperscript size 16px n subscript size 16px n size 16px equals size 16px C presuperscript size 16px n subscript size 16px 0 size 16px equals size 16px 1`

  - It is easy to see that there is only one way of arranging *n *objects out of *n *and also there can only be one way of arranging 0 objects out of *n*
  - By considering the formula for this, it reinforces the fact that 0! Must equal 1
- The binomial coefficients are symmetrical, so $\text{size} 16px C pre^{size} 16px n_{size 16px r \text{size} 16px = \text{size} 16px C pre^{size} 16px n_{size} 16px n \text{size} 16px - \text{size} 16px r}$

  - This can be seen by considering the formula for `C presuperscript n subscript r`
  - $C pre^{n}_{n - r} = \frac{n factorial}{( n - r ) \text{factorial} ( n - ( n - r ) ) factorial} = \frac{n factorial}{r \text{factorial} ( n - r ) factorial} = C pre^{n}_{r}$

### How do I know when to multiply or add?

- Many questions will ask you to find combinations of a group of different items from a bigger group of a specified number of those different items

  - For example, find the number of ways five questions could be chosen from a bank of twenty different pure and ten different statistics questions
  - The hint in this example is the word 'chosen', this tells you that the order in which the questions are chosen doesn't matter
- Sometimes questions will have restrictions,

  - For example there should be three pure and two statistics chosen from the bank of questions,
  - Or there must be at least two pure questions within the group
- If unsure about whether to add or multiply your options, ask yourself if A **and** B are both needed, or if A **or **B is needed

  - Always **multiply** if the answer is **and, **and **add **if the answer is **or**
  - For example if we needed exactly three pure **and** two statistics questions we would find the amount of each and multiply them
  - If we could have either five statistics **or** five pure questions we would find them separately and add the answers

- Probabilities can be found with combinations questions by finding the number of options a selection can be made in a particular way and dividing that by the total number of options

> **Exam Hint**
> - It is really important that you can tell whether a question is about permutations or combinations
> 
>   - Look out for key words such as **arrange **(for permutations)** **or **choose **or **select** (for combinations)
> - Don’t be confused if a question asks for the number of **ways**, this could be for either a permutations or a combinations question
> 
>   - Look out for other clues

> **Worked Example**
> Oscar has to choose four books from a reading list to take home over the summer.  There are four fantasy books, five historical fiction books and two classics available for him to choose from.  In how many ways can Oscar choose four books if he decides to have:
> 
> (i) two fantasy books and two historical fictions?
> 
> (ii) at least one of each type of book?
> 
> (iii) at least two fantasy books?
> 
> ![bzCSSNgD_2-2-3-combinations-we-solution](assets/b690c378b16e-bzcssngd-2-2-3-combinations-we-solution.png)
