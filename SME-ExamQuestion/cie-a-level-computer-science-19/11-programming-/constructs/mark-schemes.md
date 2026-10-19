# Mark Schemes — Constructs
**11. Programming** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (26 questions)


### Q1
**[6 marks]**

> **[mark-scheme]**
> **1 mark** for the function heading with two `INTEGER` parameters and `RETURNS INTEGER`, together with the closing `ENDFUNCTION`
> 
> **1 mark** for declaring both local variables as `INTEGER`
> 
> **1 mark** for setting the running cell count to the starting value and the hour count to 0 before the loop
> 
> **1 mark** for a conditional loop that continues while the running cell count is not greater than `Target`
> 
> **1 mark** for doubling the running cell count inside the loop
> 
> **1 mark** for increasing the hour count by 1 inside the loop and returning it after the loop
> 
> Accept `WHILE NOT (Cells > Target)` in place of `WHILE Cells <= Target`. The two conditions are logically equivalent.
> 
> Accept `Cells ← Cells + Cells` in place of `Cells ← Cells * 2`.
> 
> Accept the parameter `StartCells` used directly as the running value, with no separate local variable for it.
> 
> Do not accept a post-condition loop such as `REPEAT ... UNTIL Cells > Target`. Its body always runs once, so a colony that already exceeds the target returns 1 rather than 0.
> 
> Do not accept `WHILE Cells < Target`. That stops while the count is still only equal to the target, and equal is not greater. `HoursToReach(5, 10)` then returns 1 instead of 2.
> 
> Do not accept a `FOR` loop. The number of hours is not known before the function runs, so a count-controlled loop cannot be used here.

> **[exam-tip]**
> Test your loop condition against the case where the loop must not run at all. This function has to return 0 when the colony already exceeds the target, and only a pre-condition loop can do that. `REPEAT ... UNTIL` returns 1 in that case and costs two marks, because the body runs before the condition is ever tested.
> 
> The other trap is writing `<` where `<=` is needed. The function counts the hours until the colony becomes greater than the target, so a colony that exactly equals the target has not finished growing and must double once more. Read the wording of the task twice before choosing between the two operators.

### Q2
Gap (i) is `Tries ← 0` **[1]**

Gap (ii) is `Tries ← Tries + 1` **[1]**

Gap (iii) is `Temp >= -40 AND Temp <= 60` **[1]**

The completed post-condition loop is:

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for gap (i) setting the attempt counter to 0 before the loop, as `Tries ← 0`
> 
> **1 mark** for gap (ii) increasing the attempt counter by 1 inside the loop, as `Tries ← Tries + 1`
> 
> **1 mark** for gap (iii) giving a condition that is TRUE only for a reading from -40 to 60 inclusive, as `Temp >= -40 AND Temp <= 60`
> 
> Accept `NOT (Temp < -40 OR Temp > 60)` or `Temp > -41 AND Temp < 61` in gap (iii). For a whole number, all three forms accept exactly the same set of values.
> 
> Do not accept `Temp < -40 OR Temp > 60` in gap (iii). `UNTIL` ends the loop when its condition is TRUE, so that form ends the loop on every reading that should be rejected and repeats for every reading that should be accepted.
> 
> Do not accept `Temp > -40 AND Temp < 60` in gap (iii). The range is inclusive, so -40 and 60 must both be accepted.
> 
> Do not accept gap (i) written inside the loop. `Tries` would return to 0 on every pass and the final output would always be 1.

> **[exam-tip]**
> `UNTIL` states when the loop stops, not when it carries on. Students write the rejection test here out of habit, because `WHILE` takes the opposite condition. Read the line as "keep going until this becomes true", then check it once with an acceptable value and once with an unacceptable value before moving on.
> 
> A post-condition loop suits input validation because the operator has to be asked at least once. A pre-condition loop would test `Temp` before any value had been entered at all.

### Q3
**[4 marks]**

> **[mark-scheme]**
> **1 mark** for a selector that isolates the first digit using integer division, written as `Code DIV 1000`
> 
> **1 mark** for the three clause values `1`, `2` and `3` assigning `"Books"`, `"Music"` and `"Films"` respectively
> 
> **1 mark** for a final clause covering the first digits 4 to 9, for example `4 TO 9`, assigning `"Warehouse"`
> 
> **1 mark** for `CASE OF` closed by `ENDCASE`, with `Dept` assigned a value in every clause
> 
> Accept the selector written with or without the brackets, so `CASE OF Code DIV 1000` is also correct.
> 
> Accept `INT(Code / 1000)` as the selector. `INT()` takes the integer part, which for a code in the range 1000 to 9999 gives the same digit as `DIV`.
> 
> Accept `OTHERWISE : Dept ← "Warehouse"` in place of the `4 TO 9` clause. Every code is in the range 1000 to 9999, so the only first digits that can reach that clause are 4 to 9.
> 
> Accept a selector that takes the first character of the code as a string, with the clause values written as characters and an `OTHERWISE` clause for the rest:
> 
> Do not accept `Code MOD 1000`. `MOD` gives the remainder after division, which is the last three digits, so the code 3456 would give 456 and match no clause.
> 
> Do not accept `Code DIV 100`. That gives 34 for the code 3456, not 3.
> 
> Do not accept clause values written as ranges such as `1000 TO 1999` alongside a selector of `Code DIV 1000`. The selector has already reduced the code to a single digit.

> **[exam-tip]**
> When every clause of a CASE would otherwise be a range of the same width, look for an expression that turns the value into the single number the clause needs. `DIV` is the operator that does this and it is listed on the insert you are given in the exam. The usual error is to reach for `MOD`: `MOD` keeps the digits at the right-hand end of a number and `DIV` keeps the digits at the left-hand end.
> 
> A range clause includes both of its end values, so `4 TO 9` covers the first digits 4 and 9 as well as everything between them.

### Q4
Case 1: the value output is 3 **[1]**

Case 2: the value output is 0 **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for 3 in Case 1
> 
> **1 mark** for 0 in Case 2
> 
> Accept working shown alongside either answer, for example `Stock` taking the values 35, 25, 15 and then 5.
> 
> Do not accept 4 in Case 1. After three subtractions `Stock` holds 5, the condition `Stock >= 10` is FALSE, and the loop stops without a fourth pack.
> 
> Do not accept 1 in Case 2. `WHILE` is a pre-condition loop, so the condition is tested before the first pass. `7 >= 10` is FALSE, the body never runs, and `Packs` keeps the value 0 it was given before the loop.

> **[exam-tip]**
> Case 2 is the one students get wrong, because they assume every loop runs at least once. That is true of a post-condition loop, written `REPEAT ... UNTIL`, and false of a pre-condition loop, written `WHILE ... ENDWHILE`. If this loop were written as `REPEAT ... UNTIL Stock < 10` instead, an input of 7 would output 1 and leave `Stock` holding -3.
> 
> Before tracing any pre-condition loop, test the condition once using the starting values. If it is already FALSE, the answer is simply whatever the variables held before the loop.

### Q5
**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `CASE OF Command` with a matching `ENDCASE`, and the `'F'` and `'B'` clauses each written as a character value, a colon and a correct statement
> 
> **1 mark** for the `'H'` clause carrying both of its statements
> 
> **1 mark** for an `OTHERWISE` clause, written last, that adds 1 to `Errors`
> 
> Accept the character values written in double quotes, for example `"F"`.
> 
> Accept the `'F'` and `'B'` clauses in either order.
> 
> Accept `Position ← Position - 1` written as `Position ← Position + (-1)`.
> 
> Do not accept a `BREAK` or `EXIT` statement at the end of a clause. A 9618 CASE clause needs none, and neither keyword exists in this pseudocode.
> 
> Do not accept `OTHERWISE` placed anywhere other than last. An `OTHERWISE` clause runs when no earlier clause applies, so it must be the final clause.
> 
> Do not accept the `'H'` clause written with only one of its two statements.

> **[exam-tip]**
> A CASE clause may carry as many statements as it needs, written one under the next and lined up after the colon. Students who have met other languages often add a break or exit line at the end of every clause, or move the two `'H'` statements into a separate IF construct. Neither is needed here, and neither earns the mark.
> 
> `Command` holds a single character, so each clause value is a character literal in single quotes. Remember that a lower case `f` is a different character from `'F'`, so it would fall through to the `OTHERWISE` clause and be counted as an error.

### Q6
**[6 marks]**

> **[mark-scheme]**
> **1 mark** for the procedure heading `PROCEDURE MonthTotals()` together with the closing `ENDPROCEDURE`
> 
> **1 mark** for declaring every local variable used, as `INTEGER`
> 
> **1 mark** for an outer count-controlled loop running from 1 to 12
> 
> **1 mark** for setting the running total to 0 inside the outer loop, before the inner loop
> 
> **1 mark** for an inner count-controlled loop running from 1 to 4 that adds `Bookings[Month, RoomType]` to the running total
> 
> **1 mark** for outputting the month number and that month's total together, inside the outer loop and after the inner loop
> 
> Accept either loop, or both, written as a conditional loop, provided the control variable is set before the loop and increased inside it. For example:
> 
> Accept any `OUTPUT` statement that gives the month number and that month's total on the same line, with or without a message.
> 
> Do not accept `Total ← 0` placed before the outer loop. The total then carries over from one month to the next, so only the first month's figure is correct.
> 
> Do not accept the `OUTPUT` statement placed inside the inner loop. That produces 48 lines of output instead of 12.
> 
> Do not accept the two loops swapped so that `RoomType` is the outer loop. That gives a total for each room type across the whole year, which is not what the procedure must do.
> 
> Do not accept index ranges of 0 to 11 and 0 to 3. The array is declared `ARRAY[1:12, 1:4]`, so both indices start at 1.

> **[exam-tip]**
> The mark lost most often in a nested count-controlled loop is the one for resetting the running total. Ask yourself how many times the total must go back to zero. It must go back to zero once for every month, so it belongs inside the outer loop and above the inner loop, never before the outer loop.
> 
> Decide what one line of output looks like before you write any code, then place the `OUTPUT` statement where exactly that happens once per month. Inside the inner loop it gives four lines per month; after `NEXT Month` it gives a single line for the whole year.

### Q7
The first missing clause value is `50 TO 69` **[1]** and the second is `70 TO 89` **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `50 TO 69`
> 
> **1 mark** for `70 TO 89`
> 
> Accept each clause value written with or without its colon.
> 
> Accept a comparison in place of a range where it gives the same award for every mark from 0 to 100, for example `<= 69` as the second clause value and `<= 89` as the third. The earlier clauses have already dealt with the lower marks.
> 
> Do not accept `50 TO 70` or `70 TO 90`. A range in a CASE clause includes both of its end values, so these overlap the clause that follows, and the marks 70 and 90 would be given the wrong award.
> 
> Do not accept `50 TO 68` or `70 TO 88`. The marks 69 and 89 would then match no clause at all and `Award` would keep whatever value it already held.

> **[exam-tip]**
> A range in a CASE clause includes both of its end values, so `50 TO 69` and `70 TO 89` must not share a number. Writing `50 TO 70` is the usual slip and it produces no error message at all: the mark 70 simply gets the wrong award, because the clauses are tested in order and the first clause that applies is the one that runs.
> 
> Check your bands against the table by listing the end values, here 49, 50, 69, 70, 89 and 90. Every mark from 0 to 100 should match exactly one clause, with no mark left out and no mark in two clauses.

### Q8
| Statement | Answer |
|---|---|
| The number of times the statement `Total ← Total + Position` is executed | **4** |
| The last value taken by `Position` inside the loop | **11** |
| The value that is output | **26** |

`Position` takes the values 2, 5, 8 and 11, so the loop body runs 4 times. **[1]**

The last of those values is 11, because the next value would be 14, which is past the end value. **[1]**

The total is 2 + 5 + 8 + 11, which is 26. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for 4 in the first row
> 
> **1 mark** for 11 in the second row
> 
> **1 mark** for 26 in the third row
> 
> Accept the list 2, 5, 8, 11 written in the first row in place of the number 4.
> 
> Do not accept 10 in the first row. That is the answer when `STEP 3` is ignored and `Position` is treated as counting up in ones.
> 
> Do not accept 14 in the second row. `Position` reaches 14 only by passing the end value of 11, and the loop stops before the body runs again.
> 
> Do not accept 65 in the third row, which is the total of every whole number from 2 to 11.

> **[exam-tip]**
> `STEP` changes the size of each jump, not the end value. The loop body runs for every value from the start value upwards that has not passed the end value, so here it runs for 2, 5, 8 and 11 and then stops. Write the values out as a list before you count them, because working the number of iterations out in your head from 2, 11 and 3 is where most marks are lost.
> 
> The end value does not have to be reached exactly. If the end value had been 12 instead of 11, `Position` would still take the values 2, 5, 8 and 11, and all three answers would be unchanged.

### Q9
**[6 marks]**

> **[mark-scheme]**
> **1 mark** for declaring `Mass` and `Cost` as `REAL` and `Zone` as `STRING`
> 
> **1 mark** for inputting a mass and a delivery zone
> 
> **1 mark** for `IF Mass > 30 THEN` outputting `"Parcel refused"`, followed by an `ELSE`
> 
> **1 mark** for a selection inside the `ELSE` that assigns 5.00 when the mass is 10 or less and 9.00 otherwise
> 
> **1 mark** for a further selection inside the `ELSE` that doubles `Cost` when `Zone` is `"International"`
> 
> **1 mark** for outputting `Cost` inside the `ELSE`, with every IF construct closed by `ENDIF`
> 
> Accept two separate IF constructs, `IF Mass > 30 THEN` and then `IF Mass <= 30 THEN`, in place of the `ELSE`. This produces the same output for every mass.
> 
> Accept `Cost ← Cost + Cost` or `Cost ← Cost * 2.0` for the doubling.
> 
> Accept a prompt before each `INPUT` statement, or no prompt at all.
> 
> Accept the cost output with or without a message.
> 
> Do not accept `Mass` declared as `INTEGER`. A mass of 12.4 kilograms could not then be stored.
> 
> Do not accept `Mass >= 30` for the refusal test. A parcel of exactly 30 kilograms is accepted and costs 9.00.
> 
> Do not accept `Mass < 10` for the 5.00 band. A parcel of exactly 10 kilograms costs 5.00.
> 
> Do not accept the doubling or the final output placed after the last `ENDIF`. A refused parcel must not have a cost worked out or output.

> **[exam-tip]**
> The marks most often lost here are about where a statement sits, not about what it says. The doubling and the final output both belong inside the `ELSE`. A student who writes them after the last `ENDIF` prices a parcel the company has already refused, and a program that both refuses a parcel and quotes a price for it cannot gain the final mark.
> 
> Check the two boundary values the question names, 10 and 30, against your conditions before you finish. `>` and `>=` give different answers for exactly those two masses, and the question tells you which one it wants with the wording "greater than 30" and "10 or less".

### Q10
Gap (i) is `14` **[1]**

Gap (ii) is `Day` **[1]**

The completed count-controlled loop is:

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for gap (i) given as `14`
> 
> **1 mark** for gap (ii) given as `Day`
> 
> Accept `Day` in gap (ii) written with any capitalisation, because it must match the control variable named in the `FOR` and `NEXT` lines.
> 
> Do not accept `13` in gap (i). The array is declared as `ARRAY[1:14]`, so its indices run from 1 to 14 and the loop must reach 14.
> 
> Do not accept `1` in gap (ii). That adds the value of `Sold[1]` fourteen times and ignores the other 13 elements.
> 
> Do not accept `Total` in gap (ii).

> **[exam-tip]**
> 9618 arrays are declared with both bounds, as in `ARRAY[1:14]`, and the first element is index 1, not index 0. Students who have written Python often put `0 TO 13` here, which reads `Sold[0]`, an element that does not exist.
> 
> Read the `NEXT` line before you fill in the `FOR` line. `NEXT Day` tells you that the control variable is `Day`, so `Day` is what belongs inside the square brackets.

### Q11
**[3 marks]**

> **[mark-scheme]**
> **1 mark** for an outer `IF WindSpeed > 80 THEN` that outputs `"Station closed"`
> 
> **1 mark** for an `ELSE` containing a second IF construct that tests `Visibility < 200` and outputs `"Restricted access"`
> 
> **1 mark** for the inner `ELSE` outputting `"Station open"`, with both constructs closed by `ENDIF`
> 
> Accept the outer test written as `IF WindSpeed <= 80 THEN` with the two branches swapped over, provided the nesting still produces exactly one message.
> 
> Accept the messages written with or without a preceding prompt.
> 
> Do not accept `WindSpeed >= 80`. A wind speed of exactly 80 is not greater than 80, so the station is not closed.
> 
> Do not accept `Visibility <= 200`. A visibility of exactly 200 metres is not less than 200, so the station is open.
> 
> Do not accept three separate IF constructs in place of the nesting. The question requires nested IF statements.

> **[exam-tip]**
> Each "otherwise" in a specification is an `ELSE`, and every "otherwise" after the first opens a new IF construct inside that `ELSE`. 9618 pseudocode has no `ELSE IF` keyword, so you cannot join the two tests on one line, and each `IF` you write needs its own `ENDIF`. Count your `ENDIF` lines against your `IF` lines before you move on.
> 
> Then check the two boundary values named in the question. A wind speed of 80 and a visibility of 200 must both leave the station open, so the conditions are `> 80` and `< 200`, not `>= 80` and `<= 200`.

### Q12
Error: the message `"Access denied"` is output every time this pseudocode runs, including when `CardValid` is `TRUE`, because the second `OUTPUT` statement is outside the IF construct. **[1]**

Correction: put the second `OUTPUT` statement in an `ELSE` clause of the same IF construct. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for identifying that `"Access denied"` is output whatever the value of `CardValid` // that both messages are output when `CardValid` is `TRUE` // that the final `OUTPUT` statement is not inside the IF construct
> 
> **1 mark** for a correction that places `OUTPUT "Access denied"` in an `ELSE` clause of the existing IF construct
> 
> Accept a correction that adds a second IF construct testing the opposite condition, for example `IF CardValid = FALSE THEN`, then `OUTPUT "Access denied"`, then `ENDIF`. This gives the same output for both possible values of `CardValid`.
> 
> Accept `IF CardValid THEN` in place of `IF CardValid = TRUE THEN`.
> 
> Do not accept a correction that simply deletes the second `OUTPUT` statement. The program must still report a card that is not valid.
> 
> Do not accept "the indentation is wrong". Indentation does not decide which statements belong to an IF construct in 9618 pseudocode. `ENDIF` does.

> **[exam-tip]**
> Trace a selection construct with every possible value, not only the value the question seems to be about. The fault here shows up when `CardValid` is `TRUE`, which is the case most students check last.
> 
> Look for the `ENDIF`, not for the indentation. In 9618 pseudocode the indentation is there to help you read the code, and it may be left out when line numbers are used. `ENDIF` is what actually closes an IF construct, so anything written after it runs every time.

### Q13
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

### Q14
> **[mark-scheme]**
> Means that `Module-A` calls either one of `Module-X, Module-`Y or `ModuleZ `(which one is called is decided at runtime).
> 
> **One** mark for reference to selection 
> **One** mark for naming all four modules correctly

### Q15
> **[mark-scheme]**
> **One** mark per point:
> 
> 1. Name: (pre / post) conditional loop
> 2. Justification: the number of iterations is not known // loop ends following a specific input (in the loop)

### Q16
> **[mark-scheme]**
> **MP1**   An iterative construct // a (count-controlled) loop **MP2**  A selection construct // an IF statement

### Q17
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

### Q18
> **[mark-scheme]**
> One mark per point
> 
> - Count-controlled loop
> - the number of iterations is known

### Q19
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

### Q20
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

### Q21
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

### Q22
> **[mark-scheme]**
> (i)
> 
> `OTHERWISE : CALL Error(C)`
> 
> (ii)
> 
> After the `'Z'` clause in the `CASE` construct // before the `ENDCASE`

### Q23
> **[mark-scheme]**
> **MP1**    Construct: Iteration / Repetition 
> **MP2**   Use: To loop through all <u>100</u> inputs // To loop <u>100</u> times
> 
> ALTERNATIVE:
> 
> **MP1**    Construct: Selection 
> **MP2**   Use: To test whether the value input is positive

### Q24
| **Pseudocode example** | ** Selection** | **Iteration** | **Subroutine** |
|---|---|---|---|
| `FOR Index ← 1 TO 3 `<br>`   IF Safe[Index] = TRUE THEN   `<br>              `Flap[Index] ← 0 `<br>`   ENDIF `<br>`NEXT Index` | ✓ | ✓ |   |
| `CASE OF Compound(3)` | ✓ |   | ✓ |
| `REPEAT UNTIL AllDone() = TRUE` |   | ✓ |   |
| `WHILE Result[3] <> FALSE` |   | ✓ |   |

### Q25
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

### Q26
> **[mark-scheme]**
> OTHERWISE
