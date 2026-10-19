# Mark Schemes — Arrays
**10. Data Types & Structures** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (22 questions)


### Q1
**[6 marks]**

> **[mark-scheme]**
> **1 mark** for the procedure heading with no parameters, and `ENDPROCEDURE`
> 
> **1 mark** for an outer conditional loop that resets the flag at the start of every pass and ends when a pass makes no swaps
> 
> **1 mark** for an inner count-controlled loop from 1 to `Boundary`, with `Boundary` set to 49 before the first pass
> 
> **1 mark** for comparing the two adjacent elements with `<`, which gives descending order, inside the loop
> 
> **1 mark** for a complete swap of the two elements using a temporary variable, inside the loop
> 
> **1 mark** for setting the flag to `FALSE` when a swap is made and for reducing `Boundary` by 1 in the outer loop
> 
> Accept any identifier names for the flag, the boundary and the temporary variable.
> 
> Accept `Rainfall[Index + 1] > Rainfall[Index]` for the comparison.
> 
> Accept a `WHILE` loop in place of `REPEAT ... UNTIL`, provided the flag is given a value before the condition is first tested.
> 
> Do not accept `>` as the comparison. That sorts the array into ascending order, so `Rainfall[1]` would hold the smallest value.
> 
> Do not accept two nested `FOR` loops with no flag. The array is sorted, but the sort is not efficient, so the second and sixth marking points are not earned.

> **[exam-tip]**
> The word **efficient** is worth two of these six marks and it has a fixed meaning. First, a flag that ends the sort as soon as a pass makes no swaps. Second, a boundary that shrinks by one after each pass, because the value pushed to the end of the array on each pass is already in its final place. Write both in, every time you see the word.
> 
> The direction of the sort is the other trap. For descending order a swap is needed when the earlier element is **smaller** than the later one, so the comparison is `<`. Read the requirement again before you choose the operator.

### Q2
**[3 marks]**

> **[mark-scheme]**
> **1 mark** for a loop running from 1 to 24
> 
> **1 mark** for comparing the two adjacent elements with `>` inside the loop
> 
> **1 mark** for a complete swap of the two elements using `Temp`, all three statements correct
> 
> Accept this equivalent form, which shifts the index by one:
> 
> Accept a `WHILE` or `REPEAT` loop that makes the same 24 comparisons.
> 
> Accept `Height[Index + 1] < Height[Index]` for the comparison.
> 
> Do not accept a loop running from 1 to 25. `Height[Index + 1]` would then read `Height[26]`, which is outside the declared bounds of the array.
> 
> Do not accept a two-statement swap such as `Height[Index] ← Height[Index + 1]` followed by `Height[Index + 1] ← Height[Index]`. The first value is overwritten before it is copied, so both elements end up holding the same value.

> **[exam-tip]**
> The loop bound is where most marks go. The array is `ARRAY[1:25]`, so the last pair you can compare is `Height[24]` and `Height[25]`, and the loop must therefore stop at 24. Always write the declaration down and work out the final comparison before you choose the bound.
> 
> The other frequent error is a swap without `Temp`. Three statements are needed, and the temporary variable must be assigned first.

### Q3
|   | `Score[1]` | `Score[2]` | `Score[3]` | `Score[4]` | `Score[5]` | `Score[6]` |
|---|---|---|---|---|---|---|
| Start | 7 | 3 | 9 | 2 | 8 | 5 |
| After the first pass | **3** | **7** | **2** | **8** | **5** | **9** |
| After the second pass | **3** | **2** | **7** | **5** | **8** | **9** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the first pass row, all six values correct: 3, 7, 2, 8, 5, 9
> 
> **1 mark** for the second pass row, all six values correct: 3, 2, 7, 5, 8, 9
> 
> Do not accept a partly correct row. Each row is marked as a whole, because one missed swap changes every value that follows it.
> 
> Do not accept 2, 3, 5, 7, 8, 9 on the first pass row. That is the fully sorted array, and one pass of a bubble sort only guarantees that the largest remaining value has reached the end.

> **[exam-tip]**
> After one pass only the largest value, 9, is certain to be in its final position. Writing the completely sorted list on the first row is the most common error here.
> 
> Work along the array in pairs and rewrite the whole array after every swap. A swap changes which value you compare next: after 9 and 2 swap, the next comparison is between 9 and 8, not between 2 and 8.

### Q4
**[6 marks]**

> **[mark-scheme]**
> **1 mark** for the procedure heading with one parameter of type `STRING`, and `ENDPROCEDURE`
> 
> **1 mark** for an outer loop covering all 20 rows
> 
> **1 mark** for a nested inner loop covering all 6 seats in a row
> 
> **1 mark** for comparing `Seat[Row, Col]` with the parameter inside the nested loop
> 
> **1 mark** for outputting both the row number and the seat number when a match is found, inside the loop
> 
> **1 mark** for a flag that is set when a match is found and tested after both loops, so that `"Reference not found"` is output once only
> 
> Accept `WHILE` or `REPEAT` loops in place of the two `FOR` loops, provided every element from `Seat[1, 1]` to `Seat[20, 6]` is tested.
> 
> Do not accept `OUTPUT "Reference not found"` placed inside either loop. It would then be output for every seat that does not match, which is 119 times for a coach with one matching seat.
> 
> Do not accept `Seat[Row][Col]`. In 9618 pseudocode a 2D array element is written with one pair of square brackets and a comma.

> **[exam-tip]**
> The last marking point is the one most often lost. A `BOOLEAN` flag set to `FALSE` before the loops, set to `TRUE` on a match, and tested once after `NEXT Row` is the only reliable way to output the message exactly once.
> 
> Check the loop bounds against the declaration. The array is `ARRAY[1:20, 1:6]`, so the row loop ends at 20 and the seat loop ends at 6. Writing `TO 19` or `TO 5` leaves a whole row or a whole column unsearched, and it is a silent error because the algorithm still runs.

### Q5
| Index | Found | OUTPUT |
|---|---|---|
| **1** | **FALSE** |   |
| **2** |   |   |
| **3** |   |   |
| **4** |   |   |
|   | **TRUE** |   |
|   |   | **4** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the initialisation row, `Index` 1 together with `Found` `FALSE`
> 
> **1 mark** for `Index` then taking the values 2, 3 and 4, in that order
> 
> **1 mark** for `Found` changing to `TRUE` and an `OUTPUT` of 4
> 
> Accept a trace that repeats every value on every row rather than showing only the changes, provided the sequence of values is the same.
> 
> Accept `Found` shown as `F` and `T`, or as `0` and `1`.
> 
> Do not accept an `OUTPUT` of 33. That is the value being searched for, not the position it was found at.
> 
> Do not accept `Index` continuing to 5 or 6. The loop condition includes `Found = FALSE`, so the loop stops as soon as the value is found.

> **[exam-tip]**
> Look carefully at where `Index` is incremented: it is inside the `ELSE`, so it only changes when the element does not match. On the iteration that finds the value, `Index` stays at 4 and `Found` becomes `TRUE`. Students who increment on every iteration finish with `Index` 5 and output the wrong position.
> 
> Once `Found` is `TRUE` the pre-condition loop is not entered again.

### Q6
**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the first gap, comparing the current element with the parameter: `PlateNumber[Bay] = Plate`
> 
> **1 mark** for the second gap, moving on to the next bay: `Bay ← Bay + 1`
> 
> Accept the first gap written the other way round, as `Plate = PlateNumber[Bay]`.
> 
> Do not accept any increment other than 1 in the second gap, such as `Bay ← Bay + 2`. Every bay from 1 to 12 must be checked.
> 
> Do not accept `PlateNumber = Plate` in the first gap, which compares the whole array with one string instead of comparing a single element.
> 
> Do not accept `PlateNumber[Plate]`, which uses the number plate as an array index. The index must be the bay number.

> **[exam-tip]**
> `PlateNumber[Bay]` is the number plate stored in a bay, and `Bay` is the bay number. The comparison must use `PlateNumber[Bay]`, not `Bay`, and this is the single most common mistake on gap-fill questions like this one.
> 
> The second gap is outside the `IF`, so it runs on every turn of the loop. If you leave it out, or write something that does not change `Bay`, the `WHILE` loop never ends when the number plate is not in the array.

### Q7
The two nested loops visit all 4 x 20 = 80 elements of the array.

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for a function heading with no parameters and `RETURNS INTEGER`, together with `ENDFUNCTION`
> 
> **1 mark** for declaring a counter and setting it to `0` before the loops
> 
> **1 mark** for an outer loop from `1` to `4` and an inner loop from `1` to `20`, correctly nested, each closed by its own `NEXT`
> 
> **1 mark** for testing the element inside the inner loop, using both loop counters as subscripts in the order floor then room
> 
> **1 mark** for incrementing the counter only when the room is free, and returning the counter after both loops have finished
> 
> Accept `IF Occupied[Floor, Room] = FALSE THEN`, `IF NOT Occupied[Floor, Room] THEN` and a test on `TRUE` whose two branches are the other way round.
> 
> Accept any identifier names, and accept the two loops written in the other order, with rooms outside and floors inside, provided the subscripts stay as floor then room.
> 
> Accept `REPEAT ... UNTIL` or `WHILE ... ENDWHILE` loops with correct start values and correct end conditions.
> 
> Do not accept `Occupied[Room, Floor]`, which reverses the two subscripts.
> 
> Do not accept loop bounds of `0 TO 3` and `0 TO 19`, or a single loop of `1 TO 80`.
> 
> Do not accept a `RETURN` placed inside either loop, because the function would then finish before every element had been examined.

> **[exam-tip]**
> Take the loop bounds straight from the declaration. `ARRAY[1:4, 1:20]` gives you `1 TO 4` for the outer loop and `1 TO 20` for the inner loop, and the first subscript in the declaration is the first subscript in your element reference.
> 
> Set the counter to `0` before the outer loop, not inside it. A counter reset inside the outer loop is wiped at the start of every floor, so the function returns the free rooms on the fourth floor only. This is the most common way to lose marks on a counting question.

### Q8
(i) The loop counter starts at `0`, but the lowest index in the array is `1`, so line 42 tries to read `Rainfall[0]`, which does not exist. **[1]**

The error is on line `41`. **[1]**

(ii) The corrected line is `FOR Day ← 1 TO 31` **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for stating that the loop starts at `0` while the array is declared from `1`, so an index outside the bounds of the array is used
> 
> **1 mark** for the line number `41`
> 
> Accept line `10` as an alternative location, because the mismatch is between the declaration and the loop.
> 
> Do not accept "the array is too small" on its own. The array holds one element for each of the 31 days, which is what the program needs.
> 
> Do not accept an answer that names line 42 only, because line 42 is correct once the loop bounds are corrected.
> 
> **1 mark** for `FOR Day ← 1 TO 31`
> 
> Accept the line written with or without the line number `41` in front of it.
> 
> Do not accept `FOR Day ← 0 TO 30`. That visits 31 elements but still starts at index `0` and never reads `Rainfall[31]`.

> **[exam-tip]**
> A 9618 array is declared with both of its bounds shown, and `ARRAY[1:31]` means the indices run from `1` to `31`. There is no element `0`. Students who have used a language that numbers from zero start the loop at `0` out of habit and lose the mark every time.
> 
> When you are asked for a line number, check that the line you name is the line that is actually wrong. Line 42 reads `Rainfall[Day]`, which is exactly right. It only fails because the wrong value has been put in `Day` on the line above.

### Q9
| Statement | Answer |
|---|---|
| The number of elements in the array | **96** |
| The array element that stores the reading taken by sensor 3 in hour 17 | **Reading[3, 17]** |

The array has 4 rows and 24 columns, so it holds 4 x 24 = 96 elements. **[1]**

The first subscript selects the sensor and the second subscript selects the hour. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `96`
> 
> Accept the working `4 x 24` shown alongside the value `96`.
> 
> Do not accept `28`, which adds the two upper bounds instead of multiplying them.
> 
> Do not accept `24` or `4`, which give the size of one dimension only.
> 
> **1 mark** for `Reading[3, 17]`
> 
> Accept `Reading[3,17]` written without a space.
> 
> Do not accept `Reading[17, 3]`. The first subscript selects the first dimension declared, which is the sensor, so the sensor number must be written first.
> 
> Do not accept `Reading(3, 17)` with round brackets, or `Reading[3][17]` with two pairs of square brackets. Neither form is used in 9618 pseudocode.

> **[exam-tip]**
> The number of elements in a 2D array is the two dimension sizes multiplied, never added. Students who write `28` here have added `4` and `24`.
> 
> Read the declaration to decide the order of the subscripts, not the wording of the question. The declaration says `[1:4, 1:24]`, so the sensor comes first and the hour comes second, whichever order the question happens to mention them in.

### Q10
> **[mark-scheme]**
> **One** mark for simplified logical expression:
> 
> **MP1 **Result[x + 1] <= Result[x]
> 
> ALTERNATIVE SOLUTION:
> 
> `Result[x] >= Result[x + 1]`

### Q11
> **[mark-scheme]**
> **MP1**   Simplifies the algorithm // easier to write / understand / test / debug 
> **MP2**   It is possible to iterate through the values // can use a loop // allows the storage of many values using a single identifier
> **[mark-scheme]**
> **One** mark per underlined section
> 
> `DECLARE Data : ARRAY[1:120] OF REAL`

### Q12
> **[mark-scheme]**
> Solution using a loop
> 
> Example solution – using a loop
> 
> `FUNCTION GetPort(ThisDest : STRING) RETURNS INTEGER `
> `   DECLARE Index, DNum, Port : INTEGER `
> 
> `   DNum `$\leftarrow$` STR_TO_NUM(ThisDest) `
> `   Index `$\leftarrow$` 1 `
> `   Port `$\leftarrow$` -1 `
> 
> `   REPEAT `
> `      IF RouteTable[Index, 1] <> -1 THEN `
> `         IF DNum >= RouteTable[Index, 1] AND __ `
> `            DNum <= RouteTable[Index, 2] THEN `
> `               Port `$\leftarrow$` RouteTable[Index, 3] `
> `         ENDIF `
> `      ENDIF `
> `      Index `$\leftarrow$` Index + 1 `
> `   UNTIL Index = 7 OR Port <> -1 // end of array or range found `
> `   RETURN Port `
> `ENDFUNCTION `
> 
> Mark as follows **Max 7: **
> 
> 1. Function heading and ending **including** parameter and return type
> 2. Convert **parameter **to a number
> 3. (Conditional) loop through array
> 4. Skip unused element **in a loop**
> 5. Attempt to check one range with destination **in a loop**
> 6. Test **all **ranges correctly with destination **in a loop**
> 7. Store port value if destination matched **in a loop** (and exit loop)
> 8. Return port value including -1 if no match found
> 
> Solution using selection statement(s)
> 
> Example solution
> 
> `FUNCTION GetPort(ThisDest : STRING) RETURNS INTEGER `
> `   DECLARE Index, DNum, Port : INTEGER DNum `$\leftarrow$` STR_TO_NUM(ThisDest) `
> `   Port `$\leftarrow$` -1 `
> 
> `   IF RouteTable[1, 1] <> -1 AND RouteTable[1, 1] >= DNum AND RouteTable[1, 2] <= DNum THEN`
> `      Port `$\leftarrow$` RouteTable[1, 3] `
> `   END IF `
> `   IF RouteTable[2, 1] <> -1 AND RouteTable[2, 1] >= DNum AND  RouteTable[2, 2] <= DNum THEN `
> `      Port `$\leftarrow$` RouteTable[2, 3] `
> `   END IF `
> `   IF RouteTable[3, 1] <> -1 AND RouteTable[3, 1] >= DNum AND  RouteTable[3, 2] <= DNum THEN `
> `      Port `$\leftarrow$` RouteTable[3, 3] `
>         `END IF `
>         `IF RouteTable[4, 1] <> -1 AND RouteTable[4, 1] >= DNum AND  RouteTable[4, 2] <= DNum THEN `
> `      Port `$\leftarrow$` RouteTable[4, 3] `
>        `END IF `
>        `IF RouteTable[5, 1] <> -1 AND RouteTable[5, 1] >= DNum AND  RouteTable[5, 2] <= DNum THEN `
> `      Port `$\leftarrow$` RouteTable[5, 3] `
>        `END IF `
>        `IF RouteTable[6, 1] <> -1 AND RouteTable[6, 1] >= DNum AND __ RouteTable[6, 2] <= DNum THEN `
> `      Port `$\leftarrow$` RouteTable[6, 3] `
>       `END IF `
>       `RETURN Port `
> `ENDFUNCTION `
> 
> Mark as follows **Max 7: **
> 
> 1. Function heading and ending **including** parameter and return type
> 2. Convert **parameter** to a number
> 3. Skip **all** unused elements
> 4. Attempt to check one range
> 5. Check two ranges with destination correctly
> 6. Check all ranges with destination correctly
> 7. Store port value if destination matched
> 8. 8 Return port value including -1 if no match found

### Q13
> **[mark-scheme]**
> ![A grid showing rows and columns labelled 'Index', 'Value', 'Count', and 'Mix[1]' to 'Mix[4]', with assorted numerical data filled in the grid cells.](assets/002-a-grid-showing-rows-and-columns-labelled-index-v.png)
> 
> **One **mark for:
> 
> - Initialisation row
> - Each iteration of Count 1 to 4 with correct `Index, Count `and array `Mix` as shown
> - Final iteration, Count = 5, correct `Index, Count `and array `Mix` as shown plus `Mix[4]` assignment

### Q14
> **[mark-scheme]**
> **MP1**   Test for row being even number 
> **MP2**   Test for either column value equal to `Search`
> 
> `IF Row MOD 2 = 0 AND __ `
> `       (Data[Row, 1] = Search OR Data[Row, 2] = Search) THEN `
> 
> ALTERNATIVE using nested `IFs`:
> 
> `IF Row MOD 2 = 0 THEN `
> `   IF Data[Row, 1] = Search OR Data[Row, 2] = Search THEN `
> 
> **MP3 **Selection structure is either:
> 
> - Single IF statement using AND, or
> - Two nested IFs using AND, or
> - Single IF and the use of a two-iteration loop
> 
> Either of these structures correctly formed scores the mark
> 
> ALTERNATIVE SOLUTION: A FOR loop using ‘STEP 2’
> 
> `FOR Row `$\leftarrow$` 2 TO 150 / NEXT Row    STEP 2 `
> `   Data[Row, 1] = Search OR Data[Row, 2] = Search) THEN`

### Q15
> **[mark-scheme]**
> (i)
> 
> (1D) <u>array</u> of <u>20 reals</u>
> 
> Marks as follows: 
> 1 mark for array 
> 1 mark for 20 reals
> 
> (ii)
> 
> One mark per point:
> 
> 1. (Multiple instances referenced via a single identifier so) **fewer identifiers needed **
> 2. Easier to process / search / organise / access the data // Values may be accessed via a loop-controlled variable /an index //An array / data can be iterated through
> 3. Makes the program/algorithm easier to write / design / understand / maintain / modify // Simplifies the program // Easier to debug / test

### Q16
> **[mark-scheme]**
> `DECLARE Item : ARRAY [1:2000] OF Component// `
> `DECLARE Item : ARRAY [2000] OF Component// `
> `DECLARE Item : ARRAY [0:1999] OF Component `
> 
> One mark per underlined phrase

### Q17
> **[mark-scheme]**
> Max 2 marks for 'Variables':
> 
> | The two variables will be of type **Integer** |
> |---|
> | The two variables will be used as **pointers / indexes** to the arrays. |
> | The values stored in the two variables will indicate **the first element in each list** |
> | The first 1D array will be of type **String** |
> | The first 1D array will be used to **store the values // data items // User IDs** |
> | The second 1D array will be of type **Integer** |
> | The second 1D array will be used to **store the pointers // point to next item** |
> 
> Mark as follows:
> 
> One mark for **each** of the first three rows 
> One mark for **both** Array 1 rows 
> One mark for **both** Array 2 rows

### Q18
> **[mark-scheme]**
> **MP1**   Use `Mark` as the <u>index </u>to the Check array // to specify an array element
> 
> **MP2**   If value of indexed element is `TRUE`, then the paper will need to be checked

### Q19
> **[mark-scheme]**
> `0` to `200`

### Q20
> **[mark-scheme]**
> `DECLARE CardNumber : ARRAY [1:100, 1:2] OF STRING `
> 
> **MP1**    Correct dimensions 
> **MP2**   All other parts of the statement correct

### Q21
> **[mark-scheme]**
> Loop example solution
> 
> `FUNCTION CheckMark(Mark : INTEGER) RETURNS BOOLEAN `
> `   DECLARE Index, Lower, Upper : INTEGER `
> 
> `   FOR Index `$\leftarrow$` 1 TO 5 `
> `      Lower `$\leftarrow$` GradeBoundary[Index] - 2 `
> `      Upper `$\leftarrow$` GradeBoundary[Index] + 2 `
> `      IF Mark >= Lower AND Mark <= Upper THEN `
> `         RETURN TRUE `
> `      ENDIF `
> `    NEXT Index `
> 
> `    RETURN FALSE `
> `ENDFUNCTION `
> 
> Mark as follows:
> 
> 1. Loop through all elements in `GradeBoundary` array
> 2. Attempt to calculate range, both `Lower` and `Upper`, **in a loop**
> 3. Completely correct range calculation **in a loop**
> 4. Test if given mark / parameter, is within range **in a loop**
> 5. Set variable / immediate RETURN if recheck required **in a loop**
> 6. Return Boolean in both cases following a reasonable attempt
> 
> Selection example solution
> 
> `FUNCTION CheckMark(Mark : INTEGER) RETURNS BOOLEAN `
> 
> `   CASE OF Mark `
>                  `GradeBoundary[1] – 2 TO GradeBoundary[1] + 2 : RETURN TRUE    `
> `      GradeBoundary[2] – 2 TO GradeBoundary[2] + 2 : RETURN TRUE `
> `      GradeBoundary[3] – 2 TO GradeBoundary[3] + 2 : RETURN TRUE `
> `      GradeBoundary[4] – 2 TO GradeBoundary[4] + 2 : RETURN TRUE `
> `      GradeBoundary[5] – 2 TO GradeBoundary[5] + 2 : RETURN TRUE       `
> `      OTHERWISE : RETURN FALSE `
>       `ENDCASE `
> 
> `ENDFUNCTION `
> 
> Mark as follows:
> 
> 1. Correct syntax used for selection structure(s)
> 2. Correct checks for two ranges
> 3. Correct checks for three ranges
> 4. Correct checks for four ranges
> 5. Correct checks for all five ranges
> 6. Return Boolean in both cases following a reasonable
> **[mark-scheme]**
> Example Solution:
> 
> `PROCEDURE CheckAll(CNum : INTEGER) `
> `   DECLARE Index, Count, ThisMark: INTEGER `
> 
> `   Count `$\leftarrow$` 0 `
> `   OPENFILE "GRList.txt" FOR WRITE `
> `   FOR Index`$\leftarrow$` 1 to CNum `
> `      ThisMark `$\leftarrow$` Result[Index, 1] // 2D array: mark + ID `
> `      IF CheckMark(ThisMark) = TRUE THEN `
> `         WRITE "GRList.txt", NUM_TO_STR(Result[Index, 2]) `
> `         Count`$\leftarrow$` Count + 1 `
> `      ENDIF `
> `    NEXT Index `
> `    CLOSEFILE "GRList.txt" `
> `    OUTPUT "There are ", Count, " papers to check" `
> 
> `ENDPROCEDURE `
> 
> Mark as follows:
> 
> 1. Procedure heading, parameter and ending.
> 2. Open file in write mode and subsequently close
> 3. Loop through all CNum candidates
> 4. Extract candidate mark from Result array **in a loop**
> 5. Use of CheckMark() with candidate mark as parameter **in a loop**
> 6. Test return value and if TRUE then increment Count **in a loop **
> 7. ... write ID to file ...
> 8. ... after conversion to a string **in a loop**
> 9. Final output of message giving number of papers to check **not in a loop **
> 
> **Max 8 marks**

### Q22
> **[mark-scheme]**
> One mark per point:
> 
> 1. Fewer lines of code are needed
> 2. The program is simpler/ less complex // Program is easier to design / code / maintain / modify / test / debug
> 3. Direct access to days in a month / data (using month number as index) // Can use index / month to (directly) access days in month / data
> 
> **Max 2 marks**
> **[mark-scheme]**
> Example Solution
> 
> `FUNCTION GetDate(ProductionDate : DATE, ShelfLife : INTEGER) RETURNS DATE `
> `   DECLARE NewDate : DATE `
> `   DECLARE DD, MM, YY, LastDay : INTEGER `
> 
> `   DD `$\leftarrow$` DAY(ProductionDate) `
> `   MM `$\leftarrow$` MONTH(ProductionDate) `
> `   YY `$\leftarrow$` YEAR(ProductionDate) `
> 
> `   DD `$\leftarrow$` DD + ShelfLife `
> `   LastDay `$\leftarrow$` DaysInMonth[MM] `
> 
> `   IF DD > LastDay THEN `
> `      MM `$\leftarrow$` MM + 1 `
> `      DD `$\leftarrow$` DD – LastDay `
> `      IF MM = 13 THEN `
> `         MM `$\leftarrow$` 1 `
> `         YY `$\leftarrow$` YY + 1 `
> `      ENDIF `
> `   ENDIF `
> `   NewDate `$\leftarrow$` SETDATE(DD, MM, YY) `
> `   RETURN NewDate `
> `ENDFUNCTION `
> 
> Mark as follows:
> 
> 1. Declare three variables of `TYPE INTEGER` to store `DD, MM` and `YY`
> 2. Correct use of date functions from Insert to extract three integer values representing DD, MM and YY and use/assign to a variable
> 3. Add parameter `ShelfLife` to `DD` and use / assign result to a variable
> 4. Extract `LastDay` from `DaysInMonth` using `MM` as `Index`
> 5. Test for new `DD` after end of month / `DaysInMonth[MM]` 
>            … and if `DD > DaysInMonth[MM]:`
> 6. `    MM` is incremented by 1 and `DD` is set to `DD – DaysInMonth[MM]`
> 7. If `MM = 13 / MM > 12` then increment `YY` **and** set `MM` to 1
> 8. Use of `SETDATE` to assign value to `NewDate, NewDate` must have been delared as a type `DATE `
> 9. Return date
> 
> **Max 7 marks**
