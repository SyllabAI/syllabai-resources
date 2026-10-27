---
note_id: "rn_ymfKNwgpVgqXFSJq"
title: "Pseudocode"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/9-algorithm-design-and-problem-solving-/algorithms/pseudocode
path: 9-algorithm-design-and-problem-solving-/algorithms/pseudocode
updated_at: "2025-06-03T13:40:39.512Z"
spec_point_ids: ["spcpt_ky6dXSQyCVpC8pHf", "spcpt_bFTK3SSwQbzFc56K"]
spec_point_codes: []
guided_study: false
---

# Pseudocode

## Input, process, output

> **Spec point** — `spcpt_ky6dXSQyCVpC8pHf`

## Input, process, output

### What is an input?

- An input is **data or information being entered/taken into a program** before it is processed in the algorithm
- An input can come from a variety of sources, such as:

  - **User **- keyboard, mouse, controller, microphone
  - **Sensors **- temperature, pressure, movement
- Values are input using the `INPUT` command

### What is a process?

- A process is **a doing action performed in the algorithm **that transforms inputs into the desired output. The central processing unit (**CPU**) executes the instructions that define the process
- An example would be:

  - **Comparing two numbers**
  - **Calculating an average**

### What is an output?

- An output is **the result of the processing in an algorithm** and usually the way a user can see if an algorithm works as intended
- An output can take various forms, such as:

  - **Numbers **- result of calculations
  - **Text**
  - **Images**
  - **Actions** - triggering events
- Values are output using the `OUTPUT` command

More than one value can be output in the same command when separated by commas

#### Example 1 - Area of a shape

- A user wants to write a program to calculate the area of a shape

| **Input** | **Process** | **Output** |
|---|---|---|
| - Length<br>- Width | - Length X width | - Area |

#### Example 2 - Average test score

- A teacher wants to calculate the average mark achieved on a test amongst students in a class
- The teacher needs to enter how many students in the class and for each students a score out of 50

| **Input** | **Process** | **Output** |
|---|---|---|
| - Number of students<br>- Score per student | - TotalScore = TotalScore + score per student<br>- Average = TotalScore / Number of students | - Average mark |

## Programming constructs

> **Spec point** — `spcpt_bFTK3SSwQbzFc56K`

## Programming constructs

### What is sequence?

- Sequence refers to lines of code which are run **one line at a time**
- The lines of code are run in the **order** that they written from the first line of code to the last line of code
- Sequence is **crucial to the flow** of a program, any instructions out of sequence can lead to **unexpected behaviour or errors**

#### Example

- A simple program to ask a user to input two numbers, number two is subtracted from number one and the result is outputted

| **Line** | **Pseudocode** |
|---|---|
| **01** | `INPUT NumberOne` |
| **02** | `INPUT NumberTwo` |
| **03** | `Result ← NumberOne - NumberTwo` |
| **04** | `OUTPUT "The result is ", Result` |

### What is selection?

- Selection is when the **flow of a program is changed, **depending on a** set of conditions**
- The outcome of this condition will then determine **which lines or block of code is run next**
- Selection is used for **validation**, **calculation** and making sense of a **user's choices**
- There are two ways to write selection statements:

  - **if**... **then**... **else**...
  - **case**...

| **Structure** | **IF...THEN...ELSE example** | **CASE statement example** |
|---|---|---|
| **Purpose** | Used for **binary decisions** (true/false) | Used for **multiple specific options** |
| **Scenario** | Check if a user is old enough to vote | Perform an action based on the direction entered |
| **Pseudocode example** |   |   |

### What is iteration?

- Iteration means **repeating a line or block of code** using a **loop**
- It allows a program to perform a task **multiple times** until a condition is met

#### Types of iteration

| **Type** | **Description** | **Pseudocode Format** |
|---|---|---|
| **Count-controlled** | Repeats a fixed number of times | `FOR ... TO ... NEXT` |
| **Post-condition** | Repeats **at least once**, checks the condition **after** running the block | `REPEAT ... UNTIL` |
| **Pre-condition** | Checks the condition **before** running the block | `WHILE ... ENDWHILE` |

> **Worked Example**
> A teacher uses a paper-based system to store marks for a class test. The teacher requires a program to assign grades based on these results.
> 
> The program will output the grades together with the average mark.
> 
> Write a detailed description of the algorithm that will be needed.**[6]**
> 
> **Final answer:** **Answer**
> 
> **Marks awarded for a description of each of the following steps of the algorithm:**
> 
> 1. Reference variables for Count of students and Total marks **[1 mark]**
> 2. Loop through all students (Count) **[1 mark]**
> 3. Input individual mark (in loop) **[1 mark]**
> 4. Compare mark with threshold / boundary values to determine grade (in loop) **[1 mark]**
> 5. Output the grade for a student (in loop) **[1 mark]**
> 6. Maintain a Total (and Count if required) (in loop) **[1 mark]**
> 7. Calculate average by dividing Total by Count and Output (after loop) **[1 mark]**
