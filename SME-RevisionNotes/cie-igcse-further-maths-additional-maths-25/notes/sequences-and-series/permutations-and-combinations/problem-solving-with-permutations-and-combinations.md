---
note_id: "rn_5xbjfTrRsdvfx6NX"
title: "Problem Solving with Permutations & Combinations"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/sequences-and-series/permutations-and-combinations/problem-solving-with-permutations-and-combinations
path: sequences-and-series/permutations-and-combinations/problem-solving-with-permutations-and-combinations
updated_at: "2026-07-02T08:19:38.511Z"
spec_point_ids: ["spcpt_5CR4bZZmb6VNWxVT"]
spec_point_codes: []
guided_study: false
---

# Problem Solving with Permutations & Combinations

## Problem Solving with Permutations & Combinations

> **Spec point** — `spcpt_5CR4bZZmb6VNWxVT`

## Problem-solving with permutations & combinations

### How will I know whether to use Permutations or Combinations?

- In **permutation **problems, the **order **of arrangement matters

  - For example, guessing who's going to win first, second and third prize in a competition
- In **combination **problems, the **order **of arrangement doesn't matter

  - For example, guessing the top three high scorers from a group of students
- Look out for **keywords **in a problem

  - **Permutation **questions will most likely use the words **'arrange'**, **'order'**, **'sequence'**
  - **Combination **questions will most likely use the words **'select'**, **'choose'**, **'group'**
- Pay close attention to the **context **of the problem to determine if the order matters or not

### How should I approach perms and combs questions?

- Identify whether the question is a permutations or a combinations question
- Identify the total number of options available (*n*) and the number to be arranged or selected (*r*)
- Consider whether objects taken from each list can be repeated or not

  - For example a four digit PIN from ten numbers where each number can be used repeatedly would be 10 × 10 × 10 × 10
  
    - There are 10 options for the first and ten options for the second number and so on
  - If the numbers could only be used once then the number of options for each digit would **reduce **with each digit
  
    - There are 10 options for the first, nine options for the second, eight for the third and so on
- Look out for any limitations or conditions in the problem

  - Do some items need to be kept together or separate?
  - Does a code or a number need to begin or end in a particular value?

### How will I know whether to add or multiply?

- If a question requires you to choose an item from one list **AND **an item from another list you should **multiply** the number of options in each list
- In general if you see the word 'AND' you will most likely need to 'MULTIPLY'

  - For example if you are choosing a pen and a pencil from 4 pens and 5 pencils:
  
    - You can choose 1 item from 4 pens AND 1 item from 5 pencils
    - You will have 4 × 5 different options to choose from
- If a question requires you to choose an item from one list **OR **an item from another list you should **add** the number of options in each list
- In general if you see the word 'OR' you will most likely need to 'ADD'

  - For example if you are choosing a pen or a pencil from 4 pens and 5 pencils:
  
    - You can choose 1 item from 4 pens OR 1 item from 5 pencils
    - You will have 4 + 5 different options to choose from
- If a question has a restriction, such as 'four items containing at least one yellow and no more than three reds' you will need to

  - Find all of the possibilities  (one yellow **and **three reds **or **two yellows **and **two reds etc)
  - Multiply for each of the 'and' statements (one yellow **and** three reds)
  - Add together each of the 'or' statements at the end (one yellow and three reds **or **two yellows and two reds etc)

> **Exam Hint**
> - Read the question twice, taking note of the key areas outlined in this revision note and looking out for any keywords
> - If you're unsure, try writing down a few of the possible options to look for clues

> **Worked Example**
> A password must be 5 characters long and consist of 2 letters from the letters A, B, C, D, and E followed by 3 digits from the numbers 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Each letter or number may only be used once within the password. Find how many ways the password can be formed.
> 
> *There are no keywords to help us here so we must consider to context of the question.* *The context is about a password so the **order** of the arrangement matters, this is a **permutations **question. *
> 
> > *The 2 letters must be **followed** by the three digits, so we must treat these separately. *
> 
> > *For the first letter there are five possible options (A, B, C, D or E) For the second letter there are four possible options as no letter can be repeated. *
> 
> $P pre^{5}_{2} = ( 5 \times 4 )$
> 
> > *For the first number there are ten possible options (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) For the second number there are nine possible options as no number can be repeated.  For the third number there are eight possible options. *
> 
> $P pre^{10}_{3} = ( 10 \times 9 \times 8 )$
> 
> > *We want two letters **AND **three numbers so we will multiply the options.*
> 
> $P pre^{5}_{2} \times P pre^{10}_{3}$
> 
> **Final answer:** **14400 passwords**
