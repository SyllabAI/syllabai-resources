# Mark Schemes — Arrays
**10. Data Types & Structures** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (13 questions)


### Q1
> **[mark-scheme]**
> **One** mark for simplified logical expression:
> 
> **MP1 **Result[x + 1] <= Result[x]
> 
> ALTERNATIVE SOLUTION:
> 
> `Result[x] >= Result[x + 1]`

### Q2
> **[mark-scheme]**
> **MP1**   Simplifies the algorithm // easier to write / understand / test / debug 
> **MP2**   It is possible to iterate through the values // can use a loop // allows the storage of many values using a single identifier
> **[mark-scheme]**
> **One** mark per underlined section
> 
> `DECLARE Data : ARRAY[1:120] OF REAL`

### Q3
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

### Q4
> **[mark-scheme]**
> ![A grid showing rows and columns labelled 'Index', 'Value', 'Count', and 'Mix[1]' to 'Mix[4]', with assorted numerical data filled in the grid cells.](assets/002-a-grid-showing-rows-and-columns-labelled-index-v.png)
> 
> **One **mark for:
> 
> - Initialisation row
> - Each iteration of Count 1 to 4 with correct `Index, Count `and array `Mix` as shown
> - Final iteration, Count = 5, correct `Index, Count `and array `Mix` as shown plus `Mix[4]` assignment

### Q5
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

### Q6
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

### Q7
> **[mark-scheme]**
> `DECLARE Item : ARRAY [1:2000] OF Component// `
> `DECLARE Item : ARRAY [2000] OF Component// `
> `DECLARE Item : ARRAY [0:1999] OF Component `
> 
> One mark per underlined phrase

### Q8
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

### Q9
> **[mark-scheme]**
> **MP1**   Use `Mark` as the <u>index </u>to the Check array // to specify an array element
> 
> **MP2**   If value of indexed element is `TRUE`, then the paper will need to be checked

### Q10
> **[mark-scheme]**
> `0` to `200`

### Q11
> **[mark-scheme]**
> `DECLARE CardNumber : ARRAY [1:100, 1:2] OF STRING `
> 
> **MP1**    Correct dimensions 
> **MP2**   All other parts of the statement correct

### Q12
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

### Q13
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
