---
note_id: "rn_KS3t3dzgYXmgf3Vx"
title: "Upper & Lower Bounds"
source: https://www.savemyexams.com/igcse/maths/edexcel/a-modular/24/higher-unit-1/revision-notes/number/rounding-estimation-and-bounds/upper-and-lower-bounds
path: number/rounding-estimation-and-bounds/upper-and-lower-bounds
updated_at: "2026-07-19T14:32:03.094Z"
spec_point_ids: ["spcpt_H8sZcbsSTbtsTTr5", "spcpt_M5rhN2mwnR2yddc6"]
spec_point_codes: []
guided_study: true
---

# Upper & Lower Bounds

## Bounds & Error Intervals

> **Spec point** — `spcpt_H8sZcbsSTbtsTTr5`

## Bounds & error intervals

### What are bounds?

- **Bounds** are the** **values that a **rounded number** can lie between

  - The** smallest value** that a number can take is the **lower bound (LB)**
  - The **largest value** that a number must be less than is the **upper bound (UB)**
- The bounds for a number, $x$, can be written as $\mathrm{LB}\leqx<\mathrm{UB}$

  - Note that the** lower bound** is **included** in the range of values $x$* *but the **upper bound is not**

### How do I find the upper and lower bounds for a rounded number?

- Identify the **degree of accuracy** to which the number has been **rounded**

  - E.g. 24 800 has been rounded correct to the nearest 100
- **Divide** the degree of accuracy by **2**

  - E.g. If an answer has been rounded to the nearest 100, half the value is 50
- **Add** this value to the number to find the **upper bound**

  - E.g. 24 800 + 50 = 24 850
- **Subtract** this value from the number to find the **lower bound**

  - E.g. 24 800 - 50 = 24 750
- The **error interval** is the range between the upper and lower bounds

  - Error interval:** LB ≤ *****x***** < UB**
  - E.g. 24 750 ≤ 24 800 < 24 850

> **Exam Hint**
> It can help to draw a number line. Identify the numbers with the same accuracy that come immediately before and after the rounded number.
> 
> - The lower bound is the midpoint between the rounded number and the previous number at that accuracy
> - The upper bound is the midpoint between the rounded number and the next number at that accuracy
> 
> ![Number line showing rounding of a number to 24,800, with previous 100 at 24,700 and next 100 at 24,900. Bounds are 24,750 to 24,850.](assets/378aa50cdd9d-41448-bounds.png)

> **Worked Example**
> The length of a road, $l$, is given as $l=3.6\mathrm{km}$, correct to 1 decimal place.
> 
> Find the lower and upper bounds for $l.$
> 
> **Answer:**
> 
> > *The degree of accuracy is 1 decimal place, or 0.1 km*
> *Divide this value by 2*
> 
> *0.1 ÷ 2 = 0.05*
> 
> > *The true value could be up to 0.05 km above or below the given value*
> 
> *Upper bound:  3.6 + 0.05 = 3.65 km*
> 
> *Lower bound:  3.6 - 0.05 =  3.55 km*
> 
> **Final answer:** **Upper bound: 3.65 km**
> **Lower bound: 3.55 km**
> 
> **Final answer:** **This could also be written as  **$3.55\leql<3.65$

## Calculations using Bounds

> **Spec point** — `spcpt_M5rhN2mwnR2yddc6`

## Calculations using bounds

### How do I find the bounds of a calculation?

- To find the **upper bound** of a calculation, consider how the result can be made as **large as possible**
- To find the **lower bound** of a calculation, consider how the result can be made as **small as possible**
- E.g. For an addition, $a+b$

  - The **upper **bound will be when both $a$ and $b$ are at their upper bounds
  - The **lower **bound will be when both $a$ and $b$are at their lower bounds
- Sometimes you need **different bounds** in the same question

  - The upper bound of $\frac{a}{b}$ is the upper bound of $a$ divided by the lower bound of $b$
  
    - **Increasing** the** numerator** makes the fraction **bigger**,  $\frac{2}{1}<\frac{3}{1}<\frac{4}{1}<...$
    - But** increasing** the** denominator** make the fraction **smaller**, $\frac{1}{2}>\frac{1}{3}>\frac{1}{4}>...$
- How to find the upper and lower bound for each operation is summarised in the table below

|   | Upper Bound | Lower Bound |
|---|---|---|
| $a+b$ | Upper + Upper | Lower + Lower |
| $a-b$ | Upper - Lower | Lower - Upper |
| $a\timesb$ | Upper × Upper | Lower × Lower |
| $\frac{a}{b}$ | Upper ÷ Lower | Lower ÷ Upper |

- You will need to use **more than one** of these if the expression includes **multiple operations**

  - E.g. consider the upper bound for $\frac{a}{b-c}$
  
    - You need the upper bound for $a$ and lower bound for $b-c$
    - This means you need the upper bound for $b$ and lower bound for $c$
  - E.g. consider the lower bound for $\frac{a}{b}-c$
  
    - You need the lower bound for $\frac{a}{b}$ and upper bound for $c$
    - This means you need the lower bound for $b$ and upper bound for $c$

### How do I use upper and lower bounds in contexts?

- Questions often give real-life** contexts** and ask about bounds

  - For example
  
    - To see if two cars will fit on the back of a truck
    - Use the upper bounds of the lengths of the two cars
    - This is like finding the upper bound of $a+b$
  - For example
  
    - To find the minimum speed (speed = distance $\div$ time)
    - Divide the lower bound of the distance by the upper bound of the time
    - This is like finding the lower bound of $\frac{a}{b}$

### How can bounds help with calculations?

- You can use bounds to determine the **level of accuracy** of a calculation

  - E.g. If a value has a lower bound of 8.33217... and upper bound of s 8.33198...
  
    - The true value is between 8.33217... and 8.33198...
  - Find the level of accuracy for which **both bounds** round to the **same number**
  
    - This happens at 4 sf (rounding to 8.332)
    - To 5 sf they are different (lower is 8.3322 and upper is 8.3320)
  - Therefore you know the original value rounds to 8.332 to 4 significant figures

> **Worked Example**
> A room measures 4 m by 7 m, where each measurement is made to the nearest metre.
> 
> Find the upper and lower bounds for the area of the room.
> 
> **Answer:**
> 
> > *Find the bounds for each dimension, you could write these as error intervals, or just write down the upper and lower bounds*
> 
> > *As they have been rounded to the nearest metre, the true values could be up to 0.5 m bigger or smaller*
> 
> *3.5 ≤ 4 < 4.5*
> *6.5 ≤ 7 < 7.5*
> 
> > *Calculate the lower bound of the area, using the two smallest measurements*
> 
> *3.5 × 6.5*
> 
> **Final answer:** **Lower Bound = 22.75 m**<sup>**2**</sup>
> 
> > *Calculate the upper bound of the area, using the two largest measurements*
> 
> *4.5 × 7.5*
> 
> **Final answer:** **Upper Bound = 33.75 m**<sup>**2**</sup>

> **Worked Example**
> David is trying to work out how many fencing panels he needs to buy in order to construct a fence along one side of his garden path.
> 
> Fencing panels are 50 cm long, measured to the nearest 10 cm.
> 
> The length of the path is 6 m, measured to the nearest 10 cm.
> 
> Find the minimum number of fencing panels David will need to buy.
> 
> **Answer:**
> 
> > *Find the bounds for each measurement*
> 
> > *As they have been rounded to the nearest 10 cm, the true values could be up to 5 cm bigger or smaller*
> 
> > *Change quantities into the same units*
> 
> *Length of the fencing panels: 45 ≤ 50 < 55 cm*
> *or in metres: 0.45 ≤ 0.5 < 0.55 m*
> 
> *Length of the path: 5.95 ≤ 6 < 6.05 m*
> 
> > *The minimum number of fencing panels needed will be when the path is as short as possible (5.95 m), and the panels are as long as possible (0.55 m)*
> 
> *Minimum number of fencing panels = *$\frac{5.95}{0.55}=10.8181...$
> 
> > *Assuming we can only purchase a whole number of fencing panels, round up to nearest integer*
> 
> **Final answer:** **The minimum number of fencing panels to be bought is 11**
