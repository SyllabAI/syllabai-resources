---
note_id: "rn_Tp4XJBmxcYf6HzHP"
title: "Searching Algorithms"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/algorithms-and-graph-theory/algorithms/searching-algorithms
path: algorithms-and-graph-theory/algorithms/searching-algorithms
updated_at: "2026-07-02T08:19:38.464Z"
spec_point_ids: ["spcpt_Zmf4G8ptrjJTyQzz"]
spec_point_codes: []
guided_study: false
---

# Searching Algorithms

## Binary Search

> **Spec point** — `spcpt_Zmf4G8ptrjJTyQzz`

## Binary Search

### What is the binary search algorithm?

- The** binary search algorithm** inspects an **ordered **list to determine if a **specified item** is in the list

  - If the item **is in the list**, the search algorithm will find and **locate** the item

### How does the binary search algorithm work?

- The **binary search algorithm **works by finding a **pivot **that splits an ordered** sub-list **into** two halves**

  - In the first search, the sub-list is the complete **original list**
- The item being searched for is** compared to the pivot**

  - If the item is the** same** as the pivot then the item has been **found**
  - If the item comes **before** the pivot, the search continues in the **sub-list before** the pivot
  - If the item comes **after **the pivot, the search continues in the **sub-list after** the pivot
- The algorithm is **complete** when

  - the item has been **located **or
  - the item is identified as **not being in the list**

### Which item is the pivot in the binary search algorithm?

- The** pivot** is the value in the middle of a **sub-list** of items

  - To find the **position **of the pivot
  
    - Add the positions of the **first and last items** in the sub-list
    - Divide the value by 2
    - Round up to the **next integer value** if necessary

> **Exam Hint**
> - If the items in the list are not numbered, it is a good idea to **number** them in **ascending order **as a first step
> - Make a clear statement at the end of the algorithm to show that it is complete
> 
>   - If the item has been found: 'The search is complete, ..... has been found in the list'
>   - If the item has not been found: '..... is not in the list'

> **Worked Example**
> Below is a list of names.
> 
> 1. Becky
> 2. Jason
> 3. Juan
> 4. Kia
> 5. Lorcan
> 6. Ryan
> 7. Samira
> 8. Selina
> 
> Use the binary search algorithm to find the following names in the list.
> 
> a) Jason
> 
> **Answer:**
> 
> > *Find the pivot *
> 
> `fraction numerator open parentheses 1 plus 8 close parentheses over denominator 2 end fraction equals 4.5 space rightwards arrow 5`*th item*
> 
> | *5. Lorcan* |
> |---|
> 
> > *Compare 'Jason' to the pivot*
> 
> *Jason comes before Lorcan*
> *Reject items 5 to 10*
> 
> > *Write down the reduced list*
> 
> | *1. Becky*<br>*2. Jason*<br>*3. Juan*<br>*4. Kia* |
> |---|
> 
> > *Find the pivot of the reduced list*
> 
> `fraction numerator open parentheses 1 plus 4 close parentheses over denominator 2 end fraction equals 2.5 space rightwards arrow space 3`*rd item*
> 
> | *3. Juan* |
> |---|
> 
> > *Compare 'Jason' to the pivot*
> 
> *Jason comes before Juan*
> *Reject items 3 to 4*
> 
> > *Write down the reduced list*
> 
> | *1. Becky*<br>*2. Jason* |
> |---|
> 
> > *Find the pivot of the reduced list*
> 
> `fraction numerator open parentheses 1 plus 2 close parentheses over denominator 2 end fraction equals 1.5 space rightwards arrow space 2`*nd item*
> 
> | *2. Jason* |
> |---|
> 
> > *The name has been found so write a final statement*
> 
> **Final answer:** **The search is complete**
> **Jason has been found**
> 
> ** **
> 
> b) Michelle
> 
> **Answer:**
> 
> > *Find the pivot*
> 
> `fraction numerator open parentheses 1 plus 8 close parentheses over denominator 2 end fraction equals 4.5 space rightwards arrow 5`*th item*
> 
> | *5. Lorcan* |
> |---|
> 
> > *Compare 'Michelle' to the pivot*
> 
> *Michelle comes after Lorcan*
> *Reject items 1 to 5*
> 
> > *Write down the reduced list*
> 
> | *6. Ryan*<br>*7. Samira*<br>*8. Selina* |
> |---|
> 
> > *Find the pivot of the reduced list*
> 
> `fraction numerator open parentheses 6 plus 8 close parentheses over denominator 2 end fraction equals 7`*th item*
> 
> | *7. Samira* |
> |---|
> 
> > *Compare Michelle to the pivot*
> 
> *Michelle comes before Samira*
> *Reject items 7 to 8*
> 
> > *Write down the reduced list*
> 
> > *The list has been reduced to one name, which is not Michelle*
> 
> | *6. Ryan* |
> |---|
> 
> *Reject item 6*
> 
> > *Write a final statement*
> 
> **Final answer:** **Michelle is not in the list**
