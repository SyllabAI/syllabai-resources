# Exam Questions — Constructs
**11. Programming** · Cambridge (CIE) AS computer-science (9618)
> Source: [https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/) · 14 questions across 1 sets


## Exam Questions (14 questions)


### Q1 — medium — 6 marks

**Q1** [6 marks]

A global 1D array of integers contains four elements, which are assigned values as shown:

`  Mix[1] `$\leftarrow$` 4`
`  Mix[2] `$\leftarrow$` 2 `
`  Mix[3] `$\leftarrow$` 3 `
`  Mix[4] `$\leftarrow$` 5 `

A procedure `Process()` manipulates the values in the array.

The procedure is written in pseudocode as follows:

`    PROCEDURE Process(Start : INTEGER) `
                     `DECLARE Value, Index, Total : INTEGER `

`       Index `$\leftarrow$` Start `
`       Total `$\leftarrow$` 0 `

`       WHILE Total < 20 `
`          Value `$\leftarrow$` Mix[Index] `
`          Total `$\leftarrow$`Total + Value `

`          IF Index < 4 THEN `
`             Mix[Index] `$\leftarrow$` Mix[Index] + Mix[Index+1] `
`          ELSE `
`             Mix[Index] `$\leftarrow$` Mix[Index] + Mix[1] `
`          ENDIF `
`          Index `$\leftarrow$` (Value MOD 4) + 1 `

`       ENDWHILE `

`       Mix[1] `$\leftarrow$` Total * Index `

`    ENDPROCEDURE `

Complete the trace table on the opposite page by dry running the procedure when it is called as follows:

`     CALL Process(2)`

| **Index** | **Value** | **Total** | **Mix[1]** | **Mix[2]** | **Mix[3]** | **Mix[4]** |
|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |

*Source: November 2023 9618/23 Q5*


### Q2 — medium — 2 marks

**Q2** [2 marks]

A program contains six modules:

| **Pseudocode module header** |
|---|
| `PROCEDURE Module-A()` |
| `PROCEDURE Module-X(T1 : INTEGER, S2 : REAL)` |
| `PROCEDURE Reset(BYREF Code : INTEGER)` |
| `FUNCTION Restore(OldCode : INTEGER) RETURNS BOOLEAN` |
| `FUNCTION Module-Y(RA : INTEGER, RB : BOOLEAN) RETURNS BOOLEAN` |
| `FUNCTION Module-Z(SA : INTEGER) RETURNS INTEGER` |

`Module-X()`   calls   `Reset() `
`Module-Y() `calls   `Restore()`

![Flowchart with Module-A at the top, splitting into three branches with rectangles, arrows, circles, and a diamond.](assets/002-flowchart-with-module-a-at-the-top-splitting-int.png)

Explain the meaning of the diamond symbol as used in the diagram in part **(a).**

*Source: November 2023 9618/22 Q7B*


### Q3 — medium — 2 marks

**Q3** [2 marks]

An algorithm will:

1. input a sequence of integer values, one at a time
2. ignore all values until the value 27 is input, then sum the remaining values in the sequence
3. stop summing values when the value 0 is input and then output the sum of the values.

The solution to the algorithm includes iteration.

Give the name of a suitable loop structure that could be used.

Justify your answer.

Name .....................................................................................................................

Justification ............................................................................................................

*Source: November 2023 9618/22 Q2B*


### Q4 — medium — 2 marks

**Q4** [2 marks]

Sequence is one programming construct.

Identify **two other** programming constructs that will be required when the algorithm is converted into pseudocode.

Construct 1 ..........................................................................................................

Construct 2 .........................................................................................................

*Source: November 2023 9618/21 Q2B*


### Q5 — medium — 8 marks

**Q5** [4 marks]

Refer to the [insert ](https://cdn.savemyexams.com/uploads/2025/11/34786-9618_w23_in_21.pdf)for the list of pseudocode functions and operators.

The following pseudocode represents part of the algorithm for a program:

`CASE OF ThisValue `
         `< 30      :  Level `$\leftarrow$`"Low"         // less than 30`
                                              `Check `$\leftarrow$` 1`
         `< 20      :  Level `$\leftarrow$`"Very Low"    // less than 20`
`                Check `$\leftarrow$` ThisValue / 2`
`   30 TO 40  :  Level `$\leftarrow$`"Medium"      // between 30 and 40`
`                Check `$\leftarrow$` ThisValue / 3 `
`                Data[ThisValue] `$\leftarrow$` Data[ThisValue] + 1`
     `> 40       :  Level `$\leftarrow$` "High" `
`ENDCASE`

Complete the table by writing the answer for each row:

|   | **Answer** |
|---|---|
| The value assigned to `Level` when `ThisValue` is 40 |   |
| The value assigned to `Check` when `ThisValue` is 36 |   |
| The value assigned to `Level` when `ThisValue` is 18 |   |
| The number of elements in array `Data` that may be incremented |   |

*Source: November 2023 9618/21 Q1A*


**Q5** [3 marks]

The pseudocode contains four assignments to variable `Level.` One of these assignments will never be performed.

Identify this assignment **and** explain why this is the case.

*Source: November 2023 9618/21 Q1B*


**Q5** [1 mark]

The following line is added immediately before the `ENDCASE `statement:

`    OTHERWISE : Level `$\leftarrow$` "Undefined"`

State why this assignment is never performed.

*Source: November 2023 9618/21 Q1C*


### Q6 — medium — 2 marks

**Q6** [2 marks]

A program is being designed in pseudocode.

The program contains the following declaration:

`    DECLARE Data : ARRAY[1:1000] OF STRING `

A procedure ArrayInitialise() is written to initialise the values in the array:

`     PROCEDURE ArrayInitialise(Label : STRING) `
`        DECLARE Index : INTEGER `
`        Index`$\leftarrow$`1 `
`        WHILE Index <= 1000 `
`           CASE OF (Index MOD 2) `
`              0 : Data[Index]`$\leftarrow$` FormatA(Label) `
`                  Index `$\leftarrow$`Index + 1 `
`              1 : Data[Index]`$\leftarrow$` FormatB(Label) `
`                  Index `$\leftarrow$`Index + 1 `
`           ENDCASE `
`        ENDWHILE `
`     ENDPROCEDURE `

Functions `FormatA()` and `FormatB()` apply fixed format case changes to the parameter string.

The design of the procedure does **not** use the most appropriate loop construct.

Suggest a **more appropriate** construct that could be used **and **explain your choice.

Construct ........................................................................................................

Explanation ......................................................................................................

*Source: June 2024 9618/23 Q5A*


### Q7 — medium — 3 marks

**Q7** [3 marks]

A record structure is declared to hold data relating to components being produced in a factory:

`TYPE Component `
`   DECLARE Item_ID : STRING `
`   DECLARE Reject : BOOLEAN `
`   DECLARE Weight : REAL `
`ENDTYPE `

The factory normally produces a batch (or set) of 1000 components at a time. A global array is declared to store 1000 records for a batch:

`    DECLARE Batch : ARRAY [1:1000] OF Component `

Two global variables contain the minimum and maximum acceptable weight for each component. The values represent an inclusive range and are declared as:

`    DECLARE Min, Max : REAL `

A program uses a variable `ThisIndex` as the array index to access a record.

Write a pseudocode clause to check whether or **not** the weight of an individual component is within the acceptable range.

*Source: June 2024 9618/23 Q3AI*


### Q8 — medium — 2 marks

**Q8** [2 marks]

A program uses a global 1D array of type string and a text file.

An algorithm that forms part of the program is expressed as follows:

- copy the first line from the file into the first element of the array
- copy the second line from the file into the second element of the array
- continue until all lines in the file have been copied into the array.

Sequence is one programming construct. Identify **one other** programming construct that will be required when the algorithm from part **(a)** is converted into pseudocode **and** explain its use.

Construct..........................................................................................................

Use....................................................................................................................

*Source: June 2024 9618/23 Q2B*


### Q9 — medium — 2 marks

**Q9** [2 marks]

A program is being designed in pseudocode.

The program contains a global 1D array `Data` of type string containing 200 elements.

The first element has the index value 1.

A procedure `Process()` is written to initialise the values in the array:

`PROCEDURE Process(Label : STRING) `
         `DECLARE Index : INTEGER `
         `Index `$\leftarrow$`0 `
         `INPUT Data[Index] `
         `WHILE Index < 200 `
                 `Index `$\leftarrow$`Index + 1 `
                 `CASE OF (Index MOD 2) `
                         `0 : Data[Index] `$\leftarrow$`TO_UPPER(Label) `
                         `1 : Data[Index] `$\leftarrow$`TO_LOWER(Label) `
                         `OTHERWISE : OUTPUT "Alarm 1201"  `
`      ENDCASE `
      `NEXT Index `
     `OUTPUT "Completed " & Index & " times" `
`ENDPROCEDURE`

`equation`The procedure contains a statement that is not needed.

Identify the pseudocode statement **and** explain why it is not needed.

Statement ..........................................................................................

Explanation .........................................................................................

*Source: June 2024 9618/22 Q5AII*


### Q10 — medium — 2 marks

**Q10** [2 marks]

A global 1D array of strings contains three elements which are assigned values as shown:` `

`Data[1] `$\leftarrow$`"aaaaaa" `
`Data[2] `$\leftarrow$`"bbbbbb" `
`Data `$\leftarrow$`[3] "cccccc" `

Procedure` Process() `manipulates the values in the array.` `

The procedure is written in pseudocode as follows:` `

`PROCEDURE Process(Format : STRING) `
`   DECLARE Count, Index, L : INTEGER `
`   DECLARE Result : STRING `
`   DECLARE C : CHAR `

`   Result`$\leftarrow$` "****" `

`   FOR `$\leftarrow$`Count 1 TO LENGTH(Format) STEP 2 `
`      C`$\leftarrow$`MID(Format, Count, 1) `
`      L`$\leftarrow$`STR_TO_NUM(MID(Format, Count + 1, 1)) `

`      Index (Count + 1) DIV 2 `

`      CASE OF C `
`         'X' : `$\leftarrow$`Result TO_UPPER(Data[Index]) `
`         'Y' : `$\leftarrow$`Result TO_LOWER(Data[Index]) `
`         'Z' : `$\leftarrow$`Result "**" & Data[Index] `
`       ENDCASE `

`       Data[Index] LEFT(Result, L) `
`    NEXT Count `

`ENDPROCEDURE`

The procedure is to be modified. If variable `C` is assigned a value other than` 'X', 'Y'` or` 'Z'`, then procedure `Error()` is called and passed the value of variable `C` as a parameter.

This modification can be implemented by adding a **single** **line** of pseudocode.

(i) Write the single line of pseudocode.

[1]

(ii) State where this new line should be placed.

[1]

*Source: June 2024 9618/21 Q5BI,BII*


### Q11 — medium — 2 marks

**Q11** [2 marks]

An algorithm will:

1. prompt and input a sequence of 100 integer values, one at a time
2. sum the positive integers
3. output the result of the sum.

The algorithm requires the use of basic constructs. One of these is sequence.

Identify **one other** basic construct required by the algorithm **and **describe how it is used.

Construct....................................................................................................

Use..............................................................................................................

*Source: November 2024 9618/23 Q2B*


### Q12 — medium — 4 marks

**Q12** [4 marks]

Refer to the** **[insert](https://cdn.savemyexams.com/uploads/2025/11/32550-9618_w24_in_23.pdf) for the list of pseudocode functions and operators.

The following table contains pseudocode examples.

Each example may contain statements that relate to one or more of the following:

- selection
- iteration (repetition)
- subroutine (procedure or function).

Complete the table by placing **one or more** ticks ('**✓**') in each row.

| **Pseudocode example** | ** Selection** | **Iteration** | **Subroutine** |
|---|---|---|---|
| `FOR Index ← 1 TO 3 `<br>`   IF Safe[Index] = TRUE THEN   `<br>              `Flap[Index] ← 0 `<br>`   ENDIF `<br>`NEXT Index` |   |   |   |
| `CASE OF Compound(3)` |   |   |   |
| `REPEAT UNTIL AllDone() = TRUE` |   |   |   |
| `WHILE Result[3] <> FALSE` |   |   |   |

*Source: November 2024 9618/23 Q1A*


### Q13 — medium — 4 marks

**Q13** [2 marks]

One type of run-time error can cause a program to stop responding (‘freezing’).

Identify a particular type of programming construct that can generate this type of error and explain why it occurs.

Construct .......................................................................................................

Explanation.....................................................................................................

*Source: November 2024 9618/22 Q5B*


**Q13** [2 marks]

The function `Process() `contains a selection construct using a `CASE` structure.

Write pseudocode using a single selection construct with the same functionality **without** using a `CASE` structure.

*Source: November 2024 9618/22 Q5C*


### Q14 — medium — 1 marks

**Q14** [1 mark]

The final `CASE` condition `(> 200)` in the pseudocode example could be replaced with a keyword.

Give the keyword.

*Source: November 2024 9618/21 Q1D*

