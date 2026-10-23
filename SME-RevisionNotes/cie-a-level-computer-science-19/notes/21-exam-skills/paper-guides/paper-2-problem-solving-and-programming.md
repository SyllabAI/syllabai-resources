---
note_id: "rn_TTfQbtKsQ6zy7NGT"
title: "Paper 2: Problem-solving and Programming"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/paper-guides/paper-2-problem-solving-and-programming
path: 21-exam-skills/paper-guides/paper-2-problem-solving-and-programming
updated_at: "2026-10-16T12:00:36.926Z"
spec_point_ids: ["spcpt_zZrvwv5Vp3nHcGtj", "spcpt_zjk5YF9GZFd27Nkb", "spcpt_Pgp6GZDW95KywxNb", "spcpt_6NZzQgKB3GQvVM82"]
spec_point_codes: []
guided_study: false
---

# Paper 2: Problem-solving and Programming

## Paper 2 overview

> **Spec point** — `spcpt_zZrvwv5Vp3nHcGtj`

## Paper 2 overview

### What is in Paper 2?

- Paper 2 is **Fundamental Problem-solving and Programming Skills**
- It is a **2-hour written paper worth 75 marks**: 50% of the AS Level and 25% of the A Level
- It assesses syllabus sections 9 to 12: algorithm design, data types and structures, programming, and software development
- Most marks (60%) are for **designing and writing solutions** (assessment objective 3, AO3), with the rest (40%, AO2) for applying knowledge to a scenario; there are no marks for straight recall
- Answers that involve code must be written in **Cambridge pseudocode**, not in a programming language
- An **Insert** is provided with the paper, listing the built-in functions and operators you may use
- Calculators are not allowed

### How is Paper 2 different from Paper 4?

- Both papers test programming, but in different ways

| Feature | Paper 2 | Paper 4 |
|---|---|---|
| Where | On paper | On a computer, with no internet |
| Language | Cambridge pseudocode only | Java, Visual Basic or Python (console mode) |
| Level | AS Level (and part of the A Level) | A Level only |
| Code checked by | An examiner reading your pseudocode | An examiner reading your copied code and test evidence |
| Built-in functions | Only those listed in the Insert | Those of your chosen language |

- Examiners warn that students who practise in a programming language for Paper 4 often carry its syntax into Paper 2, which loses marks; see [Writing Pseudocode in the Exam](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/key-exam-skills/writing-pseudocode-in-the-exam/)

## Using the Insert

> **Spec point** — `spcpt_zjk5YF9GZFd27Nkb`

## Using the Insert

### What is in the Insert?

- The Insert is a separate booklet that lists every built-in pseudocode function and operator you can use in your answers, with an example of each

  - **String functions**: `LEFT`, `RIGHT`, `MID`, `LENGTH`, `TO_UPPER`, `TO_LOWER`, `NUM_TO_STR`, `STR_TO_NUM`, `IS_NUM`, `ASC`, `CHR`
  - **Numeric functions**: `INT`, `RAND`
  - **Date functions**: `DAY`, `MONTH`, `YEAR`, `DAYINDEX`, `SETDATE`, `TODAY`
  - **Text file function**: `EOF`
  - **Operators**: `&` (concatenation), `AND`, `OR`, `NOT`, `MOD`, `DIV` and the comparison operators
- Some questions tell you to use a function from the Insert, for example "Date functions from the insert should be used in your solution"

### How should you use the Insert?

- **Only use functions that are in the Insert**: examiners state that language-specific functions or methods that are not in it will not gain credit
- If the Insert and the Pseudocode Guide use different names for the same function, use the Insert's name; for example, use `TO_UPPER` from the Insert rather than `UCASE` from the Guide
- Check the **parameter order and return type** before you use a function; for example, `MID(ThisString, x, y)` returns `y` characters starting at position `x`
- Use the date functions when a question involves dates; in one recent series many students lost marks for not using the correct date function from the Insert to assign a date
- You may annotate the Insert and plan on it, but answers written on the Insert are not marked

## Question types in Paper 2

> **Spec point** — `spcpt_Pgp6GZDW95KywxNb`

## Question types in Paper 2

### What kinds of question come up?

- Every Paper 2 has questions that ask you to **write pseudocode**; most also include several of the types below

### Short questions on the Insert and data types

- Most Paper 2s open with short tables: give the data type of a variable or an example value, or evaluate an expression that uses Insert functions, such as `MID(CharList, MONTH(FlagDay), 1)`

### Writing a module

- The most valuable questions ask you to write a whole **procedure or function** from a description, often worth 6 to 8 marks
- The description is usually a table with a bullet point for each thing the module must do; these bullets are the basis of the mark scheme (see "How to plan a 6 to 8 mark algorithm question")

### Describing an algorithm in steps

- Some questions ask you to describe the steps of an algorithm without writing the code, for example "Describe the steps that the algorithm should perform. Do not include pseudocode statements in your answer."
- Write numbered steps that each do **one thing** (initialise a total, start a loop, input a value, test it, update the total, output the result)
- Examiners report vague steps that deal with all the values at once (such as "find all marks less than 20"); describe what happens to one value at a time inside a loop

### Completing or correcting code

- You may be given pseudocode with **gaps to fill** or **errors to find and correct**
- When correcting errors, write the original line and the corrected line, both clearly labelled; examiners describe this as the clearest way to answer, and adding the line number makes it clearer still
- See [Test Data and Finding Errors](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/key-exam-skills/test-data-and-finding-errors/) for how to spot each type of error

### Trace tables and dry runs

- You may be asked to *dry run* an algorithm and complete a trace table
- See [Trace Tables](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/key-exam-skills/trace-tables/) for the step-by-step method

### Design diagrams

- Structure charts appear in more than half of the Paper 2s set from 2021 to 2024 (12 of 21); you may be asked to draw one or to complete one with modules, parameters and the direction they are passed
- Examiners report marks lost for missing parameter labels, for not shading the arrow of a Boolean parameter, and for leaving out the selection diamond when one module calls either one module or another
- **Program flowcharts** come up often, either to draw from pseudocode or to convert into pseudocode
- **State-transition diagrams** appear less often (6 of the 21 papers); you are usually asked to complete a table of inputs, outputs and next states from a diagram, or to complete the diagram from a table

### Data structures and files

- Questions on **stacks, queues and linked lists** usually ask how they are **implemented using arrays and pointers**, not just how they behave

  - Examiners noted that many students missed the word "implemented" in one question and described a linked list in general terms, scoring few marks
- Most Paper 2s include **text file handling**, such as reading every line of a file or writing results to a new file

## How to plan a 6 to 8 mark algorithm question

> **Spec point** — `spcpt_6NZzQgKB3GQvVM82`

## How to plan a 6 to 8 mark algorithm question

### How are algorithm questions marked?

- Algorithm questions are marked **per feature**, not as all-or-nothing
- The mark scheme lists **mark points**, and each one is awarded if your pseudocode does that thing, even if other parts are wrong
- For example, in a recent 8-mark question to write a procedure that checks candidates' marks and writes some IDs to a file, the mark points included:

  - the procedure heading, parameter and ending
  - opening the file in **write** mode and closing it
  - a loop through all the candidates
  - calling the given function with the candidate's mark as the parameter
  - incrementing a count when the function returns `TRUE`
  - writing the ID to the file after converting it to a string
  - outputting the count **after** the loop

### Step-by-step method

1. **Underline each requirement** in the question or the module description table; each bullet usually maps to one or more mark points
2. **Write the header first**: `PROCEDURE` or `FUNCTION`, the identifier, the parameters with data types and, for a function, `RETURNS` and the data type
3. **Declare and initialise** the variables you need, such as a count set to 0
4. **Choose the loop**: `FOR` when you know how many times (for example, the size of an array), `WHILE NOT EOF(...)` for reading a file of unknown length
5. **Write the body** one requirement at a time, ticking each underlined bullet as you cover it
6. **Finish** by closing any file, then add the output or `RETURN` and the end statement (`ENDPROCEDURE` or `ENDFUNCTION`); nothing after `RETURN` is executed
7. **Check** that you have used the identifier names given in the question, not your own versions; examiners report marks lost for not using the array or variable names stated in the question

### How can you still pick up marks if your code isn't perfect?

- Examiners say in report after report that even the hardest pseudocode questions **contain accessible marks**
- If you cannot see the whole solution, still write:

  - the header and end statement
  - the variable declarations and initialisation
  - the loop structure
  - the file open and close
  - the final `RETURN` or `OUTPUT`
- Do not add things the question did not ask for, such as storing every input in an array; they gain nothing and take time

> **Worked Example**
> A text file `Scores.txt` stores one test score per line as a string. The number of lines in the file is not known.
> 
> A function `CountAbove()` will:
> 
> - take an integer parameter `Threshold`
> - read each score from the file
> - count how many scores are greater than `Threshold`
> - return the count
> 
> Write pseudocode for the function `CountAbove()`.
> 
> **[6]**
> 
> **Answer**:
> 
> - Function header with the parameter, `RETURNS INTEGER` and `ENDFUNCTION` **[1 mark]**
> - Open the file in `READ` mode and close it after the loop **[1 mark]**
> - Conditional loop that ends when `EOF` is reached **[1 mark]**
> - Read a line from the file inside the loop **[1 mark]**
> - Convert the line to a number and compare it with `Threshold`, incrementing `Count` if it is greater **[1 mark]**
> - Initialise `Count` to 0 before the loop and return it after the loop **[1 mark]**
> 
> Each bullet in the description maps to at least one mark point, so a student who could not work out the comparison would still score 5 out of 6.

> **Exam Hint**
> - If a question asks for a function, end with `RETURN`, not `OUTPUT`; examiners regularly see `OUTPUT` used where the value should be returned
> - If your answer runs out of space, continue on an additional page and write the question number clearly, rather than squeezing pseudocode into the margins where the examiner may not be able to read it
