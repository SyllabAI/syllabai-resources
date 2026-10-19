# Exam Questions — Recursion
**19. Computational thinking & Problem-solving** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 7 questions across 1 sets


## Exam Questions (7 questions)


### Q1 — hard — 5 marks

**Q1** [5 marks]

The following recursive procedure is written in pseudocode.

The procedure is called with the statement `CALL Show(5)`

(i) Write the output, in order, from this call.

(ii) The second group of values is output in the reverse order of the first. Explain, with reference to the stack, why this happens.

### Q2 — medium — 3 marks

**Q2** [3 marks]

The following pseudocode shows a recursive function and a statement that calls it. The line numbers are for reference only.

In this function, `DIV` returns the whole-number quotient.

Each time `Steps()` is called, the return address (the line number the call was made from) and the value of the parameter `N` are pushed onto a stack.

(i) Complete the table to show the contents of the stack at the moment the base case is reached. Row 1 is the top of the stack. You may not need all the rows.

| Stack position | Return address | Value of N |
|---|---|---|
| 1 (top) |   |   |
| 2 |   |   |
| 3 |   |   |
| 4 |   |   |
| 5 |   |   |

(ii) State the value assigned to `Answer` on line 20.

### Q3 — easy — 2 marks

**Q3** [2 marks]

A compiler translates a recursive function. When the program runs, the object code uses a stack to handle the recursive calls.

Name the process in which:

(i) the return address and the values of the local variables are pushed onto the stack with each recursive call, until the base case is reached

(ii) the return addresses and the values of the local variables are popped off the stack after the base case is reached.

### Q4 — hard — 5 marks

**Q4** [5 marks]

The following recursive function is written in pseudocode.

In this function, `MOD` returns the remainder after integer division. `DIV` returns the whole-number quotient.

(i) Complete the trace table for the function when it is called as `DigitSum(4739)`. The first row has been completed for you. Rows where a call returns to an earlier call are shown with its call number in brackets.

| Call number | Function call | Number | Result | Return value |
|---|---|---|---|---|
| 1 | DigitSum(4739) | 4739 | 9 + DigitSum(473) |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |

(ii) State the purpose of the function `DigitSum()`.

### Q5 — medium — 4 marks

**Q5** [4 marks]

The following function uses iteration to calculate the value of `Base` raised to the power `Exponent`. For example, `Power(3, 4)` returns 81.

`Exponent` is always 1 or greater.

Write pseudocode for a **recursive** version of the function `Power()`. The function heading must stay the same.

### Q6 — easy — 2 marks

**Q6** [2 marks]

The following recursive function is written in pseudocode. The line numbers are for reference only.

Identify the line number of the **base case** and the line number of the **general case** in the function `Total()`.

### Q7 — medium — 4 marks

**Q7** [4 marks]

Explain how a compiler makes use of a stack when translating recursive programming code.

*Source: November 2023 9618/32 Q9C*

