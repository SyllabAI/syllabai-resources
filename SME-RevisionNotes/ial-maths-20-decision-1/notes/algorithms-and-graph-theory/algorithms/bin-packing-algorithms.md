---
note_id: "rn_wW2PXWfZy2fJGPgV"
title: "Bin Packing Algorithms"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/algorithms-and-graph-theory/algorithms/bin-packing-algorithms
path: algorithms-and-graph-theory/algorithms/bin-packing-algorithms
updated_at: "2026-07-02T08:19:38.465Z"
spec_point_ids: ["spcpt_gm4qdfZbrNvkCS3S", "spcpt_jFw8QgmRgsYPg89c", "spcpt_sQPhN4n7HWK9DRry", "spcpt_c2bwJnJzvYhj22vC"]
spec_point_codes: []
guided_study: false
---

# Bin Packing Algorithms

## Introduction to Bin Packing Algorithms

> **Spec point** — `spcpt_gm4qdfZbrNvkCS3S`

## Introduction to Bin Packing Algorithms

- **Bin packing algorithms** organise **objects **into as few **containers **as possible
- The **containers** are called **bins**

  - In problems **all bins** will be of equal **size**
  
    - **Size** may refer to **length, width, capacity** (volume), **weight**, etc.
- **'Packing'** is a loose term that could mean **'separating', 'cutting'** or similar
- Examples of bin packing problems include:

  - Loading **pallets (objects)** of varying weights into **lorries (bins)** without exceeding their weight **capacity**
  
    - The aim is to **minimise** the number of lorries required
  - Cutting short **strips of cable (objects)** from **large reels of cable (bins)**
  
    - The aim is to **minimise wastage** at the end of a reel
- There are **three** bin packing algorithms covered

  - The **first-fit bin packing** algorithm
  - The **first-fit decreasing bin packing** algorithm
  - The **full-bin packing** algorithm
  - All are **heuristic** algorithms - they will provide a (good) solution
  
    - but **not** necessarily an **optimal** solution
    - and **not** necessarily the **only** (good) solution

## First-Fit Bin Packing Algorithm

> **Spec point** — `spcpt_jFw8QgmRgsYPg89c`

## First-Fit Bin Packing Algorithm

### What is the first-fit bin packing algorithm?

- The **first-fit bin packing algorithm** packs **objects** into **bins** in the **order** in which they are **presented**

  - E.g.  Scattered boxes are organised in the order they are encountered
  - They are not organised beforehand

- The algorithm finds the number of bins required to pack all the objects

  - Ideally this would be the **minimum number** of bins required
  - However, the algorithm will not necessarily provide the **optimal** solution
- An **advantage** of using the first-fit bin packing algorithm is **speed**

  - The objects do not have to be **sorted** (into size or any other criteria) first
  - In many cases, the **solution** obtained, will be **sufficient** for **business** or **practical** purposes
  
    - I.e.  speed **(efficiency)** is more important than **optimisation**

### How do I apply the first-fit bin packing algorithm?

- Each **object**, in turn, is placed in the **first available bin** that has enough **capacity** (room) for it

  - Object 1 (the first on the list) will be placed into bin 1
  
    - If bin 1 then has enough spare capacity, object 2 (the second on the list) will also go into bin 1
    - If not, object 2 will need a new bin, bin 2
    - Object 3 would be considered for bin 1 first, then bin 2, and failing both, it would require a new bin, bin 3

- For each object, if an existing bin **does not** have enough capacity remaining, a **new bin** will be used

  - For example,
  
    - If a bin has capacity 10 and the first two objects are of capacity 6 and 3, the 6 will go into bin 1, then the 3 will go into bin 1 too
    (6 + 3 = 9 ≤ 10)
    - If the first two objects are of capacity 5 and 9, the 5 would go in bin 1, then the 9 would go into bin 2
    (5 + 9 = 14 > 10)
- The algorithm is **complete** when all **objects** have been placed in a **bin**

### How do I find the lower bound for the number of bins?

- The **lower bound** (LB) for the **number** of **bins** required in the first-fit bin packing problem is the **smallest integer** that **satisfies**

$\mathrm{LB}\geq\frac{\mathrm{Total} \mathrm{capacity} \mathrm{of} \mathrm{all} \mathrm{objects}}{\mathrm{Size} \mathrm{of} \mathrm{each} \mathrm{bin}}$

- As it is a **number** of bins, the **lower bound** will be an **integer**

  - The calculation should always be **rounded up** to the nearest** **integer
  - E.g. For a value of 3.01, more than 3 bins would be required and so the lower bound will be 4
- Note that this is exactly the same lower bound as for the first-fit decreasing and the full-bin packing algorithms

> **Exam Hint**
> - As you place values into bins, you may find it helpful to jot down next to each bin
> 
>   - either the **total capacity used** in the bin
>   - or the **remaining capacity** in the bin
> - However, **do not** include these as part of your **final answer**

> **Worked Example**
> A gym worker is tidying up by stacking weights on shelves.  The weights, given in kilograms, are stated below.
> 
> 12,  16,  18,  8,  16,  12,  10,  4,  6,  10,  12, 16,  20,  10,  24
> 
> Each shelf has a load capacity of 40 kg.
> 
> a) Find a lower bound for the number of shelves needed so all the weights can be stacked on the shelves.
> 
> **Answer:**
> 
> > *The lower bound will be (greater than or equal to) the total of the weights divided by the capacity (load) of one shelf*
> 
> `table attributes columnalign right center left columnspacing 0px end attributes row LB greater or equal than cell fraction numerator 12 plus 16 plus 18 plus 8 plus 16 plus 12 plus 10 plus 4 plus 6 plus 10 plus 12 plus 16 plus 20 plus 10 plus 24 over denominator 40 end fraction end cell row LB greater or equal than cell 194 over 40 end cell row LB greater or equal than cell 4.85 end cell end table`
> 
> > *The number of shelves (bins) will need to be an integer (hence the inequality)*
> *More than four shelves are needed so round up to five *
> 
> **Final answer:** **Lower bound for the number of shelves is 5**
> 
> b) Use the first-fit bin packing algorithm to find the number of shelves needed to stack all of the weights.
> 
> **Answer:**
> 
> > *In this case, a 'shelf' will be a 'bin'*
> 
> > *In the first-fit bin packing algorithm, we deal with each weight in turn as they are listed*
> 
> > *(The remaining capacity, written in brackets next to each shelf in the working area, is optional)*
> 
> > *The first weight, 12 kg, will go on the first shelf*
> 
> | *Shelf 1:* | *12* |   |   |   |   | [28] |
> |---|---|---|---|---|---|---|
> 
> > *The second weight, 16 kg will also fit on the first shelf*
> 
> | *Shelf 1:* | *12* | *16* |   |   |   | [12] |
> |---|---|---|---|---|---|---|
> 
> > *Next, the 18 kg will need to go on to a new shelf (shelf 2)*
> 
> | *Shelf 1:* | *12* | *16* |   |   |   | [12] |
> |---|---|---|---|---|---|---|
> | *Shelf 2:* | *18* |   |   |   |   | [22] |
> 
> > *The 8 kg weight will go on the first shelf*
> 
> | *Shelf 1:* | *12* | *16* | *8* |   |   | [4] |
> |---|---|---|---|---|---|---|
> | *Shelf 2:* | *18* |   |   |   |   | [22] |
> 
> > *Continuing in this manner, the 16 kg weight can go on shelf 2*
> *The second 12 kg weight will need a third shelf*
> 
> | *Shelf 1:* | *12* | *16* | *8* |   |   | [4] |
> |---|---|---|---|---|---|---|
> | *Shelf 2:* | *18* | *16* |   |   |   | [6] |
> | *Shelf 3:* | *12* |   |   |   |   | [28] |
> 
> > *A fourth shelf is needed for the third 12 kg weight*
> 
> > *The 20 kg and 24 kg weights require a shelf of their own*
> 
> > *When finished, double check each shelf does not exceed 40 kg in total*
> 
> > *Do not include the spare capacities with the final answer*
> 
> | **Final answer:** **Shelf 1:** | **Final answer:** **12** | **Final answer:** **16** | **Final answer:** **8** | **Final answer:** **4** |
> |---|---|---|---|---|
> | **Final answer:** **Shelf 2:** | **Final answer:** **18** | **Final answer:** **16** | **Final answer:** **6** | **Final answer:** ** ** |
> | **Final answer:** **Shelf 3:** | **Final answer:** **12** | **Final answer:** **10** | **Final answer:** **10** | **Final answer:** ** ** |
> | **Final answer:** **Shelf 4:** | **Final answer:** **12** | **Final answer:** **16** | **Final answer:** **10** | **Final answer:** ** ** |
> | **Final answer:** **Shelf 5:** | **Final answer:** **20** | **Final answer:** ** ** | **Final answer:** ** ** | **Final answer:** ** ** |
> | **Final answer:** **Shelf 6:** | **Final answer:** **24** | **Final answer:** ** ** | **Final answer:** ** ** | **Final answer:** ** ** |
> 
> > *Notice that, whilst the lower bound was 5 shelves, the algorithm used 6 shelves*

## First-Fit Decreasing Bin Packing Algorithm

> **Spec point** — `spcpt_sQPhN4n7HWK9DRry`

## First-Fit Decreasing Bin Packing Algorithm

### What is the first-fit decreasing bin packing algorithm?

- The **first-fit decreasing bin packing algorithm** packs **objects** into **bins** once they have been arranged into **decreasing (descending) order**

  - E.g. Scattered boxes are arranged in **descending order **of **size/weight**, starting with the **biggest/heaviest**
- The algorithm finds the **number of bins** required to pack all the objects

  - Ideally this would be the **minimum number** of bins required
  - However, the algorithm will not necessarily provide the **optimal** solution
- An **advantage** of using the first-fit decreasing bin packing algorithm is that it usually gets **close** to the **optimal** solution

  - This is good for situations where **minimising** the **number** of **bins** is more desirable than **speed**

### How do I apply the first-fit decreasing bin packing algorithm?

- Each **object**, in turn, is placed in the **first available bin** that has enough **capacity** (room) for it

  - Object 1 (the biggest) will be placed into bin 1
  
    - If bin 1 then has enough spare capacity, object 2 (the second biggest) will also go into bin 1
    - If not, object 2 will need a new bin, bin 2
    - Object 3 would be considered for bin 1 first, then bin 2, and failing both, it would require a new bin, bin 3
  - For each object, if any existing bin **does not** have enough capacity remaining, a **new bin** will be required
  - For example,
  
    - If a bin has capacity 15 and the first two objects are of capacity 13 and 10, the 13 will go into bin 1, then the 10 will go into bin 2
    (as 13 + 10 = 23 > 15)
    - If the first two objects are of capacity 8 and 6, the 8 would go in bin 1, then the 6 would go into bin 1 too
    (as 8 + 6 = 14 ≤ 15)
- The algorithm is **complete** when all **objects** have been placed in a **bin**

### How do I find the lower bound for the number of bins?

- The **lower bound** (LB) for the **number** of **bins** required in the first-fit decreasing bin packing problem is the **smallest integer** that **satisfies**

$\mathrm{LB}\geq\frac{\mathrm{Total} \mathrm{capacity} \mathrm{of} \mathrm{all} \mathrm{objects}}{\mathrm{Size} \mathrm{of} \mathrm{each} \mathrm{bin}}$

- As it is a **number** of bins, the **lower bound** will be an **integer**

  - The calculation should always be **rounded up** to the nearest integer
  - E.g. For a value 3.01, more than 3 bins would be required and so the lower bound will be 4
- Note that this is exactly the same lower bound as for the first-fit and full-bin packing algorithms

> **Exam Hint**
> - A question may have a previous part that asks you to arrange values into descending order
> 
>   - You may be asked to name a suitable algorithm that would sort values in this way
>   
>     - Suitable algorithms for this would be **'bubble sort'** or **'quick sort'**
>     - You may be asked to briefly explain these algorithms

> **Worked Example**
> A gym worker is tidying up by stacking weights on shelves.  A list of the weights at the gym, given in kilograms, in descending order is stated below.
> 
> 24,  20,  18,  16,  16,  16,  12,  12,  12,  10,  10,  10,  8,  6,  4
> 
> Each shelf has a load capacity of 40 kg.  The lower bound for the number of shelves required to stack all of the weights is 5.
> 
> Use the first-fit decreasing bin packing algorithm to stack the weights onto as few shelves as possible, explaining how you know your answer is optimal.
> 
> **Answer:**
> 
> > *A 'shelf' will be a 'bin'*
> *For the first-fit decreasing bin packing algorithm, assign the weights starting with the heaviest, in descending order*
> *The first weight, 24 kg, will go on the first shelf*
> *(The remaining capacity, in brackets next to each shelf in the working area, is optional)*
> 
> | *Shelf 1:* | *24* |   |   |   |   | [16] |
> |---|---|---|---|---|---|---|
> 
> > *The second weight, 20 kg will not fit on the first shelf so a new shelf is needed*
> 
> | *Shelf 1:* | *24* |   |   |   |   | [16] |
> |---|---|---|---|---|---|---|
> | *Shelf 2:* | *20* |   |   |   |   | [20] |
> 
> > *Shelf 2 has enough capacity to take the next, 18 kg weight*
> 
> | *Shelf 1:* | *24* |   |   |   |   | [16] |
> |---|---|---|---|---|---|---|
> | *Shelf 2:* | *20* | *18* |   |   |   | [2] |
> 
> > *The first of the 16 kg weights can fill shelf 1*
> 
> | *Shelf 1:* | *24* | *16* |   |   |   | [0] |
> |---|---|---|---|---|---|---|
> | *Shelf 2:* | *20* | *18* |   |   |   | [2] |
> 
> > *Thinking ahead we can now see that the lowest weight is 4 kg, but there is only 2 kg of spare capacity in the first two shelves*
> *Therefore we know we can no longer use shelves 1 or 2*
> *The other two 16 kg weights can both go on to shelf 3*
> 
> | *Shelf 1:* | *24* | *16* |   |   |   | [0] |
> |---|---|---|---|---|---|---|
> | *Shelf 2:* | *20* | *18* |   |   |   | [2] |
> | *Shelf 3:* | *16* | *16* |   |   |   | [8] |
> 
> > *A fourth shelf is needed for the three 12 kg weights (leaving 4 kg spare)*
> *So a fifth shelf is needed for the three 10 kg weights (leaving 10 kg spare)*
> *There is then spare capacity on shelves 3, 5 and 4 respectively for the 8 kg, 6 kg and 4 kg weights*
> *Double check your final answer and do not include the spare capacities*
> 
> | **Final answer:** **Shelf 1:** | **Final answer:** **24** | **Final answer:** **16** | **Final answer:** ** ** | **Final answer:** ** ** |
> |---|---|---|---|---|
> | **Final answer:** **Shelf 2:** | **Final answer:** **20** | **Final answer:** **18** | **Final answer:** ** ** | **Final answer:** ** ** |
> | **Final answer:** **Shelf 3:** | **Final answer:** **16** | **Final answer:** **16** | **Final answer:** **8** | **Final answer:** ** ** |
> | **Final answer:** **Shelf 4:** | **Final answer:** **12** | **Final answer:** **12** | **Final answer:** **12** | **Final answer:** **4** |
> | **Final answer:** **Shelf 5:** | **Final answer:** **10** | **Final answer:** **10** | **Final answer:** **10** | **Final answer:** **6** |
> 
> > *This uses the same number of bins as the lower bound stated in the question*
> 
> **Final answer:** **This solution is optimal as the number of bins required is the same as the lower bound given**
> 
> > *Other arrangements on 5 shelves may be possible*

## Full-Bin Packing Algorithm

> **Spec point** — `spcpt_c2bwJnJzvYhj22vC`

## Full-Bin Packing Algorithm

### What is the full-bin packing algorithm?

- The** full-bin packing algorithm **identifies **combinations of objects** that will **fill a bin**

  - Any objects that **cannot **be grouped to fill a bin will be packed using the **first-fit** bin packing algorithm
- This algorithm finds the number of bins required to pack all the objects

  - Ideally this would be the **minimum number **of bins required
- An **advantage **of the full-bin packing algorithm is that it generates a **good solution**

  - It will often produce the** optimal **solution
- Full-bin combinations are **identified by inspection**

  - This can be **time-consuming** for a situation with many objects
  - It is **not **suitable for situations where **speed** is important

### How do I apply the full-bin packing algorithm?

- The list of **objects **is inspected to identify combinations of objects that fill a bin

  - As many **combinations of full-bins **as possible from the original list should be identified and placed into bins
  
    - E.g. For the list of objects: 2, 6, 4, 9, 8, 8, 2, 5, 2 and a bin capacity of 10
    - A possible set of full-bin combinations is: 2 + 8, 6 + 4, 8 + 2
    - The remaining objects are 9, 5 and 2
  - Any **remaining objects** should be placed into bins using the **first-fit **bin packing algorithm
  
    - E.g. for the remaining objects above
    - 9 will be place in the next available bin
    - 5 and 2 will be placed in an additional bin
- The algorithm is **complete** when all **objects** have been placed in a **bin**

### How do I find the lower bound for the number of bins?

- The **lower bound** (LB) for the **number** of **bins** required in the full-bin packing problem is the **smallest integer** that **satisfies**

$\mathrm{LB}\geq\frac{\mathrm{Total} \mathrm{capacity} \mathrm{of} \mathrm{all} \mathrm{objects}}{\mathrm{Size} \mathrm{of} \mathrm{each} \mathrm{bin}}$

- As it is a **number** of bins, the **lower bound** will be an **integer**

  - The calculation should always be **rounded up** to the nearest integer
  - E.g. For a value 3.01, more than 3 bins would be required and so the lower bound will be 4
- Note that this is exactly the same lower bound as for the first-fit and the first-fit decreasing bin packing algorithms

> **Exam Hint**
> - As this algorithm is mostly done by inspection, be very careful as you find the full-bin combinations
> 
>   - Check off each item as it is included in a bin
>   - Check that you have the same number of objects in your bins as there are in the original list

> **Worked Example**
> A gym worker is tidying up by stacking weights on shelves.  The weights, given in kilograms, are stated below.
> 
> 12,  16,  18,  8,  16,  12,  10,  4,  6,  10,  12, 16,  20,  10,  24
> 
> Each shelf has a load capacity of 40 kg.
> 
> Use the full-bin packing algorithm to find the number of shelves needed to stack all of the weights.
> 
> **Answer:**
> 
> > *In this case, a 'shelf' will be a 'bin'*
> 
> > *In the full-bin packing algorithm, we inspect the original list for combinations equal to the capacity of each bin*
> 
> > *Find combinations of weights that add to 40 and place on shelves*
> 
> | *Shelf 1:* | *12* | *12* | *16* |   |   |
> |---|---|---|---|---|---|
> | *Shelf 2:* | *8* | *10* | *10* | *12* |   |
> | *Shelf 3:* | *16* | *24* |   |   |   |
> | *Shelf 4:* | *16* | *20* | *4* |   |   |
> 
> > *Sort the remaining objects in the order they appear using the first-fit algorithm*
> 
> > *The remaining objects, in order, are 18, 6 and 10*
> 
> > *These will all fit in a single bin*
> 
> | **Final answer:** **Shelf 1:** | **Final answer:** **12** | **Final answer:** **12** | **Final answer:** **16** | **Final answer:** ** ** | **Final answer:** ** ** |
> |---|---|---|---|---|---|
> | **Final answer:** **Shelf 2:** | **Final answer:** **8** | **Final answer:** **10** | **Final answer:** **10** | **Final answer:** **12** | **Final answer:** ** ** |
> | **Final answer:** **Shelf 3:** | **Final answer:** **16** | **Final answer:** **24** | **Final answer:** ** ** | **Final answer:** ** ** | **Final answer:** ** ** |
> | **Final answer:** **Shelf 4:** | **Final answer:** **16** | **Final answer:** **20** | **Final answer:** **4** | **Final answer:** ** ** | **Final answer:** ** ** |
> | **Final answer:** **Shelf 5:** | **Final answer:** **18** | **Final answer:** **6** | **Final answer:** **10** | **Final answer:** ** ** | **Final answer:** ** ** |
> 
> > *The lower bound is 5 shelves so the solution is optimal*
> *There are other possible 5-shelf solutions using the full-bin algorithm*
