---
note_id: "rn_3ShZ5GNbHFWwBgzK"
title: "Paper 3: Advanced Theory"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/paper-guides/paper-3-advanced-theory
path: 21-exam-skills/paper-guides/paper-3-advanced-theory
updated_at: "2026-10-16T12:02:50.381Z"
spec_point_ids: ["spcpt_gKhFm7x3R2GddbCP", "spcpt_3P5cYc3rF8fgX8m9", "spcpt_sSHSh82h7NJV5PpB", "spcpt_xKyzM9cQ92hCFpSK"]
spec_point_codes: []
guided_study: false
---

# Paper 3: Advanced Theory

## Paper 3 overview

> **Spec point** — `spcpt_gKhFm7x3R2GddbCP`

## Paper 3 overview

### What is in Paper 3?

- Paper 3 Advanced Theory is a **1 hour 30 minute written paper** worth **75 marks**
- It is **25% of the A Level** and is only sat by A Level students
- It covers syllabus sections 13 to 20:

  - data representation (including floating-point numbers)
  - communication and internet technologies
  - hardware and virtual machines (including Boolean algebra and Karnaugh maps)
  - system software (including Reverse Polish Notation (RPN) and Backus-Naur Form (BNF))
  - security
  - artificial intelligence
  - computational thinking and problem-solving
  - further programming
- You answer **all** questions, and **calculators are not allowed**
- Many questions are **multi-step methods** where the working earns marks; examiner reports remind students that if a question asks for working, it must be shown to gain full credit
- Questions that need pseudocode must follow the Cambridge pseudocode guide
- For general 9618 advice and the Paper 1 skills that Paper 3 builds on, see:

  - [CIE A Level Computer Science exam tips](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/exam-technique/exam-tips/)
  - [9618 command words](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/exam-technique/command-words/)
  - [Writing Cambridge pseudocode in the exam](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/key-exam-skills/writing-pseudocode-in-the-exam/)
  - [How to answer Paper 1: Theory Fundamentals](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/paper-guides/paper-1-theory-fundamentals/)

## Question types and how to answer them

> **Spec point** — `spcpt_3P5cYc3rF8fgX8m9`

## Question types and how to answer them

### How do you answer floating-point questions?

- Typical stems include:

  - "Calculate the normalised floating-point representation of +54.8125 in this system. Show your working."
  - "Calculate the denary value of the given normalised binary floating-point number"
- The system is given in the question; for example, **12 bits for the mantissa and 4 bits for the exponent**, both in **two's complement**
- Mark schemes credit each stage separately:

  - converting the number to binary
  - working out the exponent (how many places the binary point moves)
  - the correct final mantissa and exponent
- Examiners report students losing marks on the exponent: errors in calculating it, or not showing how it was worked out and applied to the mantissa
- Check that the result is normalised: a positive mantissa starts `01` and a negative mantissa starts `10`
- Fill **every bit** of the mantissa and exponent, padding with zeros where needed
- For questions about range or precision, link the bits to the effect: more mantissa bits give greater precision and more exponent bits give a greater range; examiners credited answers that said how many bits the mantissa had, why that was too few, and that precision would be lost

### How do you answer Boolean algebra and Karnaugh map questions?

- Typical stems include:

  - "Write the Boolean expression that corresponds to the logic circuit as a sum-of-products"
  - "Complete the Karnaugh map (K-map) for the given truth table"
  - "Draw loop(s) around appropriate group(s) in the K-map to produce an optimal sum-of-products"
- **Fill every cell** of a K-map with a 0 or a 1; examiners only award marks for a complete map using 0s and 1s
- Loops must contain 1, 2, 4, 8 or 16 cells and can wrap around the edges; use the **largest** groups possible
- Give the answer in the form asked for

  - If the question asks for a **sum-of-products**, do not simplify it further; examiners report many wrong answers that gave simplified expressions the question did not ask for
  - If the question asks you to simplify, **show all the stages** and name the law used where you can
  - When you apply De Morgan's laws, change the operator as well as splitting the bar: NOT (A AND B) becomes (NOT A) OR (NOT B); examiners report answers that split the bar but left AND as AND

### How do you answer Reverse Polish Notation (RPN) questions?

- Typical stems include:

  - "Evaluate this RPN expression"
  - "Show the changing contents of the stack as the RPN expression is evaluated"
  - Converting between infix and RPN
- When showing the stack during RPN evaluation, only operands go on the stack; examiners report a common error of putting the **operators** on the stack
- Show the stack after **every** push and pop, not only the final value
- When converting RPN to infix, **include brackets**; examiners report that leaving them out changes the order of operations and makes the answer wrong

### How do you answer BNF and syntax diagram questions?

- Typical stems include "Complete the Backus-Naur Form (BNF) for the given syntax diagrams" and "Draw a syntax diagram for..."
- Use exact BNF notation: `<name>` for each *non-terminal*, `::=` for "is defined as" and `|` between alternatives
- Examiners report that students often understood the syntax diagram but lost marks for **BNF that was not fully correct**
- For recursion (for example, a code made of one or more digits), define the item in terms of itself, such as `<code> ::= <digit> | <digit><code>`

### How do you answer graph algorithm questions?

- Typical stems include "Calculate the shortest distance between the base and each of the other towns in the diagram using Dijkstra's algorithm" and "Describe the purpose of both the A* algorithm and Dijkstra's algorithm"
- For a Dijkstra trace, show the working the examiners look for:

  - set the start node to 0 and every other node to infinity (∞)
  - update each distance as shorter routes are found
  - record which nodes have been visited
- For "purpose" questions, the purpose of both algorithms is to find the **shortest (optimum) path between two nodes**; the A* algorithm also uses a ***heuristic*** to guide the search

### How do you answer declarative programming questions?

- Typical stems describe a set of facts (for example, students and the subjects they choose) and ask you to write extra clauses, or to give the result of a *goal*
- Examiners report that the highest marks went to students who remembered that:

  - **every clause ends with a full stop**
  - **facts use lower-case letters only**
  - clauses are written in the correct order with no spelling errors
- When giving the output of a goal, do not add capital letters or a full stop to the list of results

### How do you answer object-oriented programming questions?

- Typical stems include "Outline the structure of a class", "Give three differences between an object and a class" and writing pseudocode for a class with a constructor
- In pseudocode, close every class with `ENDCLASS`; examiners report that missing `ENDCLASS` was a typical error
- Use **the identifiers already given** in the question for attributes and parameters; examiners report marks lost for using different variable names in declarations or the constructor
- For definitions, be specific: "inheritance is when a new class **derives** attributes and methods from a parent class" scores, where a vague phrase does not

### How do you answer user-defined data type questions?

- Typical stems include "Write pseudocode statements to declare the record data type...", or to declare an enumerated, set or pointer type
- Declare every user-defined type with the keyword `TYPE`; a record type ends with `ENDTYPE`. Examiners report marks lost for starting the definition with `DECLARE`, or for not beginning it with `TYPE`
- Use the type names, field names and data types given in the question

### How do you answer "purpose" questions?

- Some Paper 3 questions ask for the **purpose** of something, such as asymmetric key cryptography or quantum cryptography
- Examiners report that describing **how it works** or listing its features does not answer a purpose question; say **what it is for** and **why it is used**

## Showing working on multi-step questions

> **Spec point** — `spcpt_sSHSh82h7NJV5PpB`

## Showing working on multi-step questions

### What should your working include?

- In Paper 3, the method often earns more marks than the final answer

| Question type | What your working should show |
|---|---|
| Floating-point to binary | The number in binary, the number of places the point moves, then the final mantissa and exponent |
| Floating-point to denary | The exponent in denary, where the point moves to, then the denary value |
| K-map | Every cell filled with 0 or 1, the loops drawn, then one product term per loop |
| Boolean simplification | Every stage of the simplification |
| RPN evaluation | The stack after every push and every operation |
| Dijkstra's algorithm | Starting values (0 and ∞) and each updated distance |

- If you run out of time on a multi-step question, write down the stages you have completed; examiners report that students earned credit for **correct methods** even when the final answer was wrong

> **Worked Example**
> Real numbers are stored in a computer using floating-point representation with:
> 
> - 12 bits for the mantissa
> - 4 bits for the exponent
> - two's complement form for both the mantissa and the exponent
> 
> Calculate the normalised floating-point representation of +27.375 in this system. Show your working.
> 
> **[3]**
> 
> **Answer**:
> 
> - 27.375 converted to binary: 11011.011 **[1 mark]**
> - The binary point moves 5 places to the left to give 0.11011011, so the exponent is 5 **[1 mark]**
> - Mantissa: 011011011000, Exponent: 0101 **[1 mark]**
> 
> The mantissa starts with 01, which shows it is a normalised positive number; the remaining bits are padded with zeros to fill all 12 bits.

> **Exam Hint**
> - Write the exponent as a denary number in your working before converting it to binary, because examiners report marks lost on the exponent step

## Common mistakes in Paper 3

> **Spec point** — `spcpt_xKyzM9cQ92hCFpSK`

## Common mistakes in Paper 3

- Getting the exponent wrong, or not showing how it was calculated, in floating-point questions
- Leaving K-map cells blank or using symbols other than 0 and 1
- Simplifying a sum-of-products when the question did not ask for it
- Putting operators on the stack when evaluating RPN
- Leaving out brackets when converting RPN to infix
- Using capital letters in facts or in the output of a goal, or missing the full stop at the end of a clause
- Describing how something works when the question asks for its purpose
