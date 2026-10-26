# Mark Schemes — Constructs
**11. Programming** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (14 questions)


### Q1
> **[mark-scheme]**
> ![Spreadsheet with columns: Index, Value, Total, Mix[1-4]. Data boxes show numbers, calculations including sums, and borders highlighting specific data.](assets/001-spreadsheet-with-columns-index-value-total-mix-1.png)
> 
> **MP1** Row 1 (initialisation)
> 
> Each iteration (1 – 5): 
> **MP2**   1 – Total 2 
> **MP3**   2 – Total 5 
> **MP4   **3 – Total 10 
> **MP5   **4 – Total 15 
> **MP6**   5 – Total 28 **and** final `Mix[1]` = 56

### Q2
> **[mark-scheme]**
> Means that `Module-A` calls either one of `Module-X, Module-`Y or `ModuleZ `(which one is called is decided at runtime).
> 
> **One** mark for reference to selection 
> **One** mark for naming all four modules correctly

### Q3
> **[mark-scheme]**
> **One** mark per point:
> 
> 1. Name: (pre / post) conditional loop
> 2. Justification: the number of iterations is not known // loop ends following a specific input (in the loop)

### Q4
> **[mark-scheme]**
> **MP1**   An iterative construct // a (count-controlled) loop **MP2**  A selection construct // an IF statement

### Q5
> **[mark-scheme]**
> **One** mark per row:
> 
> |   | **Answer** |
> |---|---|
> | The value assigned to `Level` when `ThisValue` is 40 | **"Medium"** |
> | The value assigned to `Check` when `ThisValue` is 36 | **12** |
> | The value assigned to `Level` when `ThisValue` is 18 | **"Low"** |
> | The number of elements in array `Data` that may be incremented | **11** |
> **[mark-scheme]**
> One mark for identifying assignment:
> 
> **MP1**   `Level `$\leftarrow$` "Very Low"` // the level is assigned value “very low”
> 
> Explanation points:
> 
> **MP2**   because CASE clauses are checked in sequence // because of the order of the clauses
> 
> **MP3**   a value < 30 satisfies the first clause // Clause <u>'< 20'</u> will never be tested
> **[mark-scheme]**
> **MP1**   all of the possible values are addressed via all / four / three / the other clauses // there are no other possible values to map to `OTHERWISE`

### Q6
> **[mark-scheme]**
> One mark per point
> 
> - Count-controlled loop
> - the number of iterations is known

### Q7
> **[mark-scheme]**
> Example solution using AND
> 
> `    IF Batch[ThisIndex].Weight >= Min AND `
> `       Batch[ThisIndex].Weight <= Max THEN `
> 
> Alternative solution using OR
> 
> `    IF Batch[ThisIndex].Weight < Min OR `
> `       Batch[ThisIndex].Weight > Max THEN `
> 
> Mark as follows:
> 
> 1. Reference to `Batch[ThisIndex].Weight `
> 2. A valid check for one boundary
> 3. A valid check for other boundary with correct logic operator

### Q8
> **[mark-scheme]**
> One mark per point:
> 
> Construct: a <u>conditional</u> loop
> 
> Use: To keep repeating until the **end of the file is reached **
> 
> ALTERNATIVE:
> 
> Construct: a <u>selection</u> statement
> 
> Use: To test / check the value returned by the `EOF()` function

### Q9
> **[mark-scheme]**
> One mark per point:
> 
> Statement:
> 
> - The `OTHERWISE` statement
> 
> Explanation:
> 
> - The result of MOD 2 can only be 0 or 1

### Q10
> **[mark-scheme]**
> (i)
> 
> `OTHERWISE : CALL Error(C)`
> 
> (ii)
> 
> After the `'Z'` clause in the `CASE` construct // before the `ENDCASE`

### Q11
> **[mark-scheme]**
> **MP1**    Construct: Iteration / Repetition 
> **MP2**   Use: To loop through all <u>100</u> inputs // To loop <u>100</u> times
> 
> ALTERNATIVE:
> 
> **MP1**    Construct: Selection 
> **MP2**   Use: To test whether the value input is positive

### Q12
| **Pseudocode example** | ** Selection** | **Iteration** | **Subroutine** |
|---|---|---|---|
| `FOR Index ← 1 TO 3 `<br>`   IF Safe[Index] = TRUE THEN   `<br>              `Flap[Index] ← 0 `<br>`   ENDIF `<br>`NEXT Index` | ✓ | ✓ |   |
| `CASE OF Compound(3)` | ✓ |   | ✓ |
| `REPEAT UNTIL AllDone() = TRUE` |   | ✓ |   |
| `WHILE Result[3] <> FALSE` |   | ✓ |   |

### Q13
> **[mark-scheme]**
> **MP1**   Construct: A (pre/post) <u>conditional</u> loop
> 
> **MP2**   Explanation: The terminating condition is never satisfied
> **[mark-scheme]**
> Example solution:
> 
> `IF Index Mod 2 = 0 THEN `
> `   ReturnValue `$\leftarrow$` TO_UPPER(RIGHT(Label, Count))  `
> `ELSE  `
> `   ReturnValue `$\leftarrow$` "****" `
> `ENDIF `
> 
> Mark as follows: 
> **MP1**      `IF...THEN...ELSE...ENDIF `
> **MP2**     Both correct assignments **and** the correct test/logic `equation``equation`

### Q14
> **[mark-scheme]**
> OTHERWISE
