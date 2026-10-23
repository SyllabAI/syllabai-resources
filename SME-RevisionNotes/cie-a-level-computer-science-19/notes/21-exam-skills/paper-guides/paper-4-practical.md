---
note_id: "rn_PqVfqcDcBzskBKyY"
title: "Paper 4: Practical"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/paper-guides/paper-4-practical
path: 21-exam-skills/paper-guides/paper-4-practical
updated_at: "2026-10-16T12:05:06.151Z"
spec_point_ids: ["spcpt_W4FPw5fkNDr5FZyd", "spcpt_xPtjNx65G5JGdV2N", "spcpt_wsHCt8x2VP2RbrnX", "spcpt_6XQf9yqqt8DdKdmY", "spcpt_HrfrgxY9QVk5pKYz"]
spec_point_codes: []
guided_study: false
---

# Paper 4: Practical

## How the Paper 4 practical exam works

> **Spec point** — `spcpt_W4FPw5fkNDr5FZyd`

## How the Paper 4 practical exam works

### What happens in Paper 4?

- Paper 4 is the **practical programming paper** for Cambridge International A Level Computer Science (9618)
- It lasts **2 hours 30 minutes**, is worth **75 marks** and makes up **25% of the A Level**
- It is taken **on a computer**, with **no internet or email access**
- Programs must be written in one of three languages, in console mode:

  - Java
  - Python
  - Visual Basic
- A mark of zero is given if any other language is used
- All 75 marks are for **assessment objective 3 (AO3): design, programming and evaluation**

### What does a Paper 4 question look like?

- The paper has **three questions**, each built around **one scenario**, such as a queue of jobs, a set of trains and stations or a file of toy records
- The scenario is split into **many small parts**, usually worth 1 to 8 marks each
- Later parts build on earlier ones; for example, you write a class in part (a), use it in the main program in part (b) and extend the main program in part (c)
- Some parts give **pseudocode** or a description of the algorithm to turn into program code; others only describe what the subroutine must do
- You may be given **source files**, such as a text file of data or starter code, to use

## The evidence document

> **Spec point** — `spcpt_xPtjNx65G5JGdV2N`

## The evidence document

### Why does the evidence document matter so much?

- The syllabus is explicit: "If there is no evidence of work in the evidence document, the work will not receive any marks"
- Examiners **only see the evidence document**, not your program files, so a perfect program that is not pasted in scores zero
- Each task tells you which part of the evidence document to paste into, for example "Copy and paste the program code into part 1(b) in the evidence document"

### Program code evidence

- **Copy and paste code as text**, not as a screenshot

  - Examiners report that screenshots of code from an integrated development environment (IDE), especially coloured text on a dark background, are often unreadable and cannot gain marks
- Paste the code into the **correct box** for that question part
- Check that **all of the code is visible**, including the first line of each subroutine and the lines at the right-hand edge of the page
- In Python, check that the **indentation** has survived the paste; examiner reports stress that it must be included and accurate
- If you change code from an earlier part, **update the earlier evidence** as well

### Testing evidence

- When a part says "Test your program", take a **screenshot of the output** and paste it into the named box
- The screenshot must show **every input** as well as the output, so the examiner can check that one produced the other
- Use **black text on a white background**, and make the screenshot large enough to read
- If the output is too long for one screenshot, **use two or more**
- Testing parts are usually worth only 1 or 2 marks each, between 4 and 8 marks per paper in recent series, but they are among the most accessible marks on the paper

## Question types in Paper 4

> **Spec point** — `spcpt_wsHCt8x2VP2RbrnX`

## Question types in Paper 4

### Which topics come up most?

- Paper 4 papers from 2021 to 2026 repeatedly test the same small set of topics:

| Question type | What you are typically asked to write | Marks often given for |
|---|---|---|
| Abstract data types (ADTs): stack, queue, linked list, binary tree | Declare the array and pointers; write `Push()`/`Pop()`, `Enqueue()`/`Dequeue()` or insert and remove routines | Checking for full or empty; updating the pointer; returning the correct value |
| Object-oriented programming (OOP) | Declare a class with private attributes, a constructor and get/set methods; create objects; sometimes inheritance; in Python, declare the attributes using comments when the question asks for it | Correct attribute types; constructor parameters assigned to attributes; methods returning values |
| File handling | Read data from a text file into an array or objects; sometimes write data to a file | Opening the file; looping to the end of the file; storing each line; closing the file; *exception handling* |
| Recursion | Write a recursive subroutine, such as an in-order tree traversal or a recursive search | A base case; a recursive call with a changed parameter; using the returned value |
| Sorting and searching | Write a bubble sort, insertion sort, linear search or binary search on an array | Correct loop limits; the comparison and swap; returning the found index or a "not found" value |

- If you write in Python, include the attribute declarations as comments; every Paper 4 from 2024 to 2026 asks for this, because examiners want to see your declarations and data types even though Python does not need them

### Exception handling

- Many file-handling parts give a mark for **exception handling**, for example `try` and `except` in Python or `try` and `catch` in Java and Visual Basic
- Examiner reports note that some students did not attempt it at all, losing an easy mark
- Put the file-opening and reading statements **inside** the `try` block, and output a suitable message in the `except` or `catch` block

### Turning pseudocode into program code

- When a question gives pseudocode, it is **not written in any one language**, so it may need adapting
- Examiner reports give the example of loop conditions that had to be changed in Python to run the correct number of times

  - The pseudocode `FOR Count ← 1 TO 10` runs 10 times, so in Python it needs `range(1, 11)`, not `range(1, 10)`
- Python also needs the `global` keyword inside a subroutine that assigns a new value to a global variable, such as a pointer
- **Test each subroutine as soon as you write it**, even when the question does not ask for a screenshot

## How to manage your time in Paper 4

> **Spec point** — `spcpt_6XQf9yqqt8DdKdmY`

## How to manage your time in Paper 4

### How long should each part take?

- With 150 minutes for 75 marks, you have about **2 minutes per mark**

  - A 6-mark subroutine is worth about 12 minutes
  - A 1-mark test screenshot should take about 2 minutes
- Spend the first few minutes **reading each whole question**, including all its parts, before you write any code

  - Examiner reports point out that knowing the later parts can change how you write the earlier ones
- Save your work regularly using the file names given in the question

### What if you get stuck on one part?

- **Move on and attempt the later parts**: they are often marked independently
- Examiner reports describe students gaining marks for calling a subroutine in the main program even though they had not managed to write the subroutine
- Leave yourself time at the end to **check the evidence document** against every "Copy and paste" instruction in the paper

## Common mistakes in Paper 4

> **Spec point** — `spcpt_HrfrgxY9QVk5pKYz`

## Common mistakes in Paper 4

- These mistakes appear repeatedly in Cambridge examiner reports for Paper 4:

  - Mixing up **parameters** and **inputs**: taking a value as an input when the question says it is passed as a parameter, or the other way round
  - Calling a function but **not storing or using the value it returns**, when the question asks for the return value to be output
  - Using extra arrays when the question asks for a single array, so the solution **does not meet the requirements** given
  - Leaving out the **constructor parameters** that the question specifies for a class, or writing get methods that take a parameter or output a value instead of returning it
  - Submitting files other than the evidence document, or a zipped evidence document

> **Worked Example**
> A program uses a stack to store integers. The stack is stored in the global 1D array `Stack`, which has space for 5 integers. The global variable `TopPointer` stores the index of the top item in the stack and is initialised to −1. Each element of `Stack` is initialised to −1.
> 
> The function `Push()` takes an integer as a parameter. If the stack is full, the function returns `FALSE`. Otherwise, it adds the integer to the top of the stack and returns `TRUE`.
> 
> (a) Write program code for `Push()`.
> 
> **[4]**
> 
> (b) The main program attempts to push the integers 10, 20, 30, 40, 50 and 60 onto the stack, in that order. After each attempt, it outputs whether the integer was pushed.
> 
> Write program code for the main program and test it.
> 
> **[3]**
> 
> **Answer**:
> 
> Example answer in Python (the same marks are available in Java and Visual Basic):
> 
> - **(a)** Function header with one parameter **[1 mark]**
> - Checking whether the stack is full and returning `FALSE` if it is **[1 mark]**
> - Incrementing `TopPointer` **[1 mark]**
> - Storing the parameter at the new `TopPointer` position and returning `TRUE` **[1 mark]**
> - **(b)** Calling `Push()` with each of the six integers in order **[1 mark]**
> - Using the return value to output a suitable message for each integer **[1 mark]**
> - Screenshot showing 10, 20, 30, 40 and 50 pushed and 60 not pushed **[1 mark]**
> 
> In Python, the `global` statement is needed so that `Push()` updates the global `TopPointer` rather than creating a new local variable.

> **Exam Hint**
> - When a question gives you an algorithm, such as a bubble sort, keep that algorithm and the data structures it uses; examiners expect it to be retained, not rewritten as a different sort or redesigned
