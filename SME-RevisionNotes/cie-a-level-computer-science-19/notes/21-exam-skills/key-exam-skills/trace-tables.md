---
note_id: "rn_DG3KJVJR3bzNHrNw"
title: "Trace Tables"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/key-exam-skills/trace-tables
path: 21-exam-skills/key-exam-skills/trace-tables
updated_at: "2026-10-16T12:08:52.916Z"
spec_point_ids: ["spcpt_g79hZzF2G9RPjDkW", "spcpt_yqFvS9p2V6VGgdkb", "spcpt_P9kBrfg8bk36kw9Y", "spcpt_4M8K3phHgPzQrwtX"]
spec_point_codes: []
guided_study: false
---

# Trace Tables

## What a trace table question tests

> **Spec point** — `spcpt_g79hZzF2G9RPjDkW`

## What a trace table question tests

### What is a trace table question in 9618?

- A **trace table** records the value of each variable, and any output, as an algorithm is **dry run** one statement at a time
- In 9618, trace tables for pseudocode appear in **Paper 2**, usually worth **5 or 6 marks**

  - **Paper 1** also asks you to trace an assembly language program, and **Paper 3** has asked for a trace of a recursive function
- The question gives the pseudocode, the starting data and a table with the column headings already filled in
- The command word is almost always **Complete**, for example:

  - "Complete the trace table by dry running the procedure when it is called as follows: `CALL Process("X3Y2W4")`"
  - "Complete the trace table below by dry running the procedure `Encode()` when the following values are input: 12, 24, 57, 43, 56, 22, 31, 32, 47, 99, 0"
- The question tests whether you can follow the **exact** logic of the code, including loops, selection, array indexes and string functions

### How are trace tables marked?

- Mark schemes split the table into **zones** or **groups of rows** and award one mark per zone

  - For example, one 6-mark trace table was marked as: one mark for the initialisation row, one mark for each of the first four iterations and one mark for the final iteration
- A mistake in one zone does not lose every mark, but an error that is **carried forward** into later rows can make those zones wrong too
- Marks are only given when every value in the zone is correct, so accuracy matters more than speed

## Step-by-step method

> **Spec point** — `spcpt_yqFvS9p2V6VGgdkb`

## Step-by-step method

### How do you complete a trace table?

- Follow these steps for every trace table question:

  1. **Read the whole algorithm first** and find the loop, what ends it and which variables change inside it
  2. **Fill in the initial values** on the first row, exactly as the code assigns them, before the loop starts
  3. **Work through one statement at a time**, in the order the code runs, not the order of the columns
  4. **Only write a value when it changes**; leave a cell empty if the variable keeps its value
  5. **Start a new row** when a variable that already has a value on the current row changes again
  6. **Check the loop condition every time** the loop is about to repeat, using the current values
  7. **Record output exactly as it would be displayed**
- Leave the left-over blank rows empty; the number of rows printed is not a clue to the number of iterations

### Example: a simple FOR loop

- The pseudocode below adds the numbers 1 to 3

| Count | Total | OUTPUT |
|---|---|---|
|   | 0 |   |
| 1 | 1 |   |
| 2 | 3 |   |
| 3 | 6 |   |
|   |   | 6 |

- The first row holds the initial value of `Total`; `Count` has no value yet
- **Never add a row for a FOR loop counter going past its end value**: the loop stops after `Count` reaches 3, so `Count` is never shown as 4

> **Exam Hint**
> - Before you write anything in the table, find the statement that ends the loop and predict how many times it will run, then check your table matches

## Tracing loops, arrays and functions

> **Spec point** — `spcpt_P9kBrfg8bk36kw9Y`

## Tracing loops, arrays and functions

### What changes when the loop is a WHILE or REPEAT loop?

- A **WHILE** loop checks its condition **before** each iteration, so the loop body may never run at all
- A **REPEAT ... UNTIL** loop checks its condition **after** each iteration, so the body always runs at least once
- When the condition ends the loop, nothing changes, so **no new row is needed** just for the check
- With **input values** (for example "12, 24, 57, ... 0"), use each value once, in order, and stop when the loop ends, even if values are left over

### Tracing nested loops

- The inner loop runs **completely** for every single iteration of the outer loop
- Write both counters as columns and update the inner counter on every row
- The outer counter only changes when the inner loop has finished

### Tracing arrays

- Each array element in the table gets **its own column**, such as `Mix[1]` to `Mix[4]`
- When the index is a variable, work out the index **first**, then find the element

  - If `Index` is 3, `Mix[Index] ← Mix[Index] - 1` changes `Mix[3]` only
- An element keeps its value until the code changes it, so look back up the column for its latest value

### Tracing functions and string handling

- Use the **Insert** to check exactly what each built-in function returns; the [Paper 2 guide](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/paper-guides/paper-2-problem-solving-and-programming/) explains how to use it

  - `MID("X3Y2W4", 3, 1)` returns `"Y"`, the 1 character starting at position 3
  - `LEFT(Result, 3)` returns the first 3 characters of `Result`
  - `STR_TO_NUM("3")` returns the number 3, not the string "3"
- Keep data types consistent with the question: strings in quotation marks, characters in single quotes, numbers without quotes

  - The **OUTPUT** column is different: write output exactly as it is displayed, without quotation marks
- When a function is called, trace its parameters as the values passed in, and write the **returned value** in the column of the variable that receives it

## Common mistakes in trace tables

> **Spec point** — `spcpt_4M8K3phHgPzQrwtX`

## Common mistakes in trace tables

- Examiner reports for 9618 identify these mistakes:

  - **Missing the initial values**: one series' report noted that otherwise good answers "missed the initial values", which is a full mark lost
  - **Merging iterations**: the same report stressed that students must "keep the values of variables distinct for each iteration of the loop"
  - **Quotation marks around output**: in assembly language traces in Paper 1, otherwise correct tables lost marks for putting quotation marks around the output
  - **Missing the final value**: examiners noted answers that left out the final value of a loop counter (`Index` = 11) after a conditional loop ended
- Other mistakes that cost marks:

  - Running a loop one time too many or one time too few (an **off-by-one error**), often by checking the loop condition with old values
  - Using `/` and `DIV` interchangeably: `DIV` gives the whole-number part only, so `583 DIV 10` is 58

> **Worked Example**
> The procedure `Process()` is written in pseudocode:
> 
> Complete the trace table by dry running the procedure when it is called as follows:
> 
> `CALL Process(5837)`
> 
> **[5]**
> 
> **Answer**:
> 
> | Num | Digit | Total | Count | OUTPUT |
> |---|---|---|---|---|
> | 5837 |   | 0 | 0 |   |
> | 583 | 7 |   | 1 |   |
> | 58 | 3 |   | 2 |   |
> | 5 | 8 | 8 |   |   |
> | 0 | 5 |   | 3 |   |
> |   |   |   |   | Even total: 8, odd digits: 3 |
> 
> One mark for each of:
> 
> - the initialisation row **[1 mark]**
> - the first two iterations **[1 mark]**
> - the third iteration **[1 mark]**
> - the fourth iteration, with `Num` reaching 0 **[1 mark]**
> - the output **[1 mark]**
> 
> `MOD 10` takes the last digit and `DIV 10` removes it, so the digits are processed from right to left: 7, 3, 8, 5. The loop ends when `Num` is 0, so there is no fifth iteration. See [Writing Pseudocode in the Exam](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/key-exam-skills/writing-pseudocode-in-the-exam/) for how `MOD` and `DIV` work.

> **Exam Hint**
> - When you finish, run your eye down each column: a variable should only change on rows where the code actually assigns it a new value
