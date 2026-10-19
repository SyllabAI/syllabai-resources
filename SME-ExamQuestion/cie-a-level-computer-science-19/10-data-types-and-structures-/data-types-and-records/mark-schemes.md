# Mark Schemes — Data Types & Records
**10. Data Types & Structures** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (19 questions)


### Q1
One mark per row. **[4]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for `INT`
> 
> **1 mark** for `CHR`
> 
> **1 mark** for `TO_UPPER`
> 
> **1 mark** for STR<u>TO</u>NUM and `LEFT`, in that order, both correct
> 
> Accept function names written in lower case.
> 
> Do not accept STR<u>TO</u>NUM on the first row. Its parameter must be a `CHAR` or a `STRING`, and `56.89` is a `REAL`.
> 
> Do not accept `LENGTH` on the last row. It returns the length of the shortened string, which is 2, not 42.
> 
> Do not accept `MID` on the last row. `MID` takes three parameters and only two are shown.

> **[exam-tip]**
> Work backwards from the declared data type of the variable on the left of the arrow. `Total` is an `INTEGER`, so the outermost function on those two rows must return an `INTEGER`. `Symbol` is a `CHAR`, and `CHR` is the only function on the insert that turns a number into a `CHAR`.
> 
> On the last row the value starts as a `STRING` and must end as an `INTEGER`, so two separate things have to happen: shorten the string, then convert it to a number. Students often hold the two functions in the right order in their head and then write them the wrong way round. Read your answer from the inside out and check what data type each step hands to the next.

### Q2
| `Index` | `Added` | `Machine[1].Quantity` | `Machine[2].Quantity` | `Machine[3].Quantity` | OUTPUT |
|---|---|---|---|---|---|
|   | 0 | 0 | 5 | 1 |   |
| **1** | **1** | **4** |   |   | **"A1"** |
| **2** |   |   |   |   |   |
| **3** | **2** |   |   | **5** | **"C3"** |
|   |   |   |   |   | **2** |

The loop runs three times. Slot 2 is skipped because its `Refill` field holds `FALSE`, so its `Quantity` never changes. **[5]**

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for `Index` taking the values 1, 2 and 3, in that order, on three separate rows
> 
> **1 mark** for `Added` taking the value 1 and then the value 2
> 
> **1 mark** for `Machine[1].Quantity` becoming 4
> 
> **1 mark** for `Machine[3].Quantity` becoming 5, with `Machine[2].Quantity` left unchanged at 5
> 
> **1 mark** for the OUTPUT column holding "A1", then "C3", then 2, in that order
> 
> Accept a value repeated on every following row rather than written once when it changes.
> 
> Accept `A1` and `C3` written without the quotation marks.
> 
> Do not accept any value in `Machine[2].Quantity` other than 5. The `Refill` field of slot 2 holds `FALSE`, so the `IF` statement is never entered for that element.
> 
> Do not accept a final OUTPUT of 3. `Added` is only incremented inside the `IF` statement.

> **[exam-tip]**
> The trap here is slot 2. It is easy to read the `FOR` loop, see that it visits all three elements, and update all three quantities. The loop does visit element 2, but the `IF` statement blocks every line inside it, so nothing about slot 2 changes. Test the `IF` condition separately for each element before you change any value.
> 
> The second trap is `Added`. It counts the slots that were actually refilled, not the number of times round the loop, so it ends on 2 and not 3.

### Q3
The clause reaches a field of one element of the array of records, so it needs the array name, the index, a full stop and the field name. **[1]**

The seat is free when the `Booked` field holds `FALSE`. **[1]**

The price test uses `<=`, because the stem says "no more than" the budget, and the two tests are joined with `AND`. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for referring to `Screen[ThisIndex].Booked` and `Screen[ThisIndex].Price`
> 
> **1 mark** for a valid test that the seat is free, `Screen[ThisIndex].Booked = FALSE`
> 
> **1 mark** for a valid price test, `Screen[ThisIndex].Price <= Budget`, joined to the first test with `AND`
> 
> Accept `NOT Screen[ThisIndex].Booked` or `Screen[ThisIndex].Booked <> TRUE` for the first test.
> 
> Accept `Screen[ThisIndex].Price < Budget OR Screen[ThisIndex].Price = Budget` for the second test.
> 
> Accept the clause written with or without `IF` and `THEN`.
> 
> Do not accept `Screen.Booked[ThisIndex]`, which puts the index in the wrong place.
> 
> Do not accept `Screen[ThisIndex].Price < Budget` on its own, because a seat priced at exactly the budget is still affordable.
> 
> Do not accept `OR` in place of `AND`.

> **[exam-tip]**
> The order is array, then index, then field: `Screen[ThisIndex].Price`. If you write `Screen.Price[ThisIndex]`, you are still thinking of two separate arrays, and that is exactly the design the record replaced.
> 
> The second common loss is the boundary. "No more than the budget" includes the budget itself, so the operator is `<=`. Match the operator to the wording of the stem before you write anything.

### Q4
The statement that saves the value into the field: **[1]**

The statement that reads the value out of the field: **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `TodayReading.Temperature ← 18.5`
> 
> **1 mark** for `OUTPUT TodayReading.StationID`
> 
> Accept the two statements written in either order.
> 
> Do not accept `Reading.Temperature ← 18.5`, which names the data type instead of the variable.
> 
> Do not accept `TodayReading[Temperature]` or `TodayReading["Temperature"]`. A field is not an array element and is never reached with square brackets.

> **[exam-tip]**
> The mark is lost far more often on the left of the arrow than the right. `Reading` is the name of the data type, not a variable, so nothing can be stored in it. Always write the variable name, then a full stop, then the field name.
> 
> Watch the dot as well. A record field is reached with dot notation, `TodayReading.Temperature`, and never with square brackets. Square brackets belong to arrays.

### Q5
The declaration earns one mark, calling `SETDATE` with `1` as the day earns one mark, and taking the month and the year from `JoinDate` earns the third. **[3]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `DECLARE BillDate : DATE`
> 
> **1 mark** for an assignment to `BillDate` that calls `SETDATE` with `1` as the day parameter
> 
> **1 mark** for `MONTH(JoinDate)` as the month parameter and `YEAR(JoinDate)` as the year parameter
> 
> Accept the work split across extra statements, for example `ThisMonth ← MONTH(JoinDate)` followed by `BillDate ← SETDATE(1, ThisMonth, YEAR(JoinDate))`.
> 
> Accept `01` in place of `1` for the day parameter.
> 
> Do not accept a declaration of any type other than `DATE`, such as `DECLARE BillDate : STRING`.
> 
> Do not accept a value built as text, for example joining the characters `"01/"` to the month and the year with the `&` operator. That produces a `STRING`, not a `DATE`.
> 
> Do not accept the parameters of `SETDATE` in any other order. The insert defines the order as day, month, year.

> **[exam-tip]**
> The commonest error here is building the date as a string and joining the parts with `&`. It looks right when printed, but the variable then holds a `STRING`, and every date function on the insert expects a value of type `DATE`.
> 
> `DATE` is a single value, not three numbers. To change part of a date you have to pull the parts out with `DAY`, `MONTH` and `YEAR`, which each return an `INTEGER`, and then build a new date with `SETDATE`. Learn the order of the three `SETDATE` parameters, because day, month, year is not the order every country writes dates in.

### Q6
| **Assignment statement** | **Error** |
|---|---|
| `Grade ← LEFT(StudentID, 2)` | A string of length 2 is returned, and a string longer than one character cannot be assigned to a CHAR variable **[1]** |
| `StudentID ← Grade` | NO ERROR **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for stating that `LEFT(StudentID, 2)` returns a `STRING` of length 2, which cannot be assigned to a `CHAR`
> 
> **1 mark** for `NO ERROR`
> 
> Accept for the first mark: the value returned is too long for a `CHAR`, or a `CHAR` can hold only one character.
> 
> Accept for the second mark: valid, correct, or no error.
> 
> Do not accept for the first mark: `LEFT` is the wrong function. The function call itself is properly formed. The error is the data type of the value it returns.
> 
> Do not accept an error for the second statement. The insert states that a `CHAR` may be assigned to a `STRING`.

> **[exam-tip]**
> Students throw this mark away by assuming `CHAR` and `STRING` are interchangeable. The insert allows the conversion in one direction only. A `CHAR` may be assigned to a `STRING`, but a `STRING` of more than one character may not be assigned to a `CHAR`.
> 
> `LEFT`, `RIGHT` and `MID` always return a `STRING`. A string of length 1 may be treated as either type, so `LEFT(StudentID, 1)` would be accepted here. Always check the length of the value returned before you decide whether the assignment is legal.

### Q7
> **[mark-scheme]**
> `TYPE MyType `
> `   DECLARE RA : INTEGER `
> `   DECLARE RB : STRING `
> `   DECLARE RC : BOOLEAN `
> `ENDTYPE `
> 
> **MP1   **`TYPE MyType... ENDTYPE` 
> **MP2  **`RA `as integer and `RB3` as string 
> **MP3  **`RC` as Boolean

### Q8
> **[mark-scheme]**
> | **Assignment statement** | **Data type** |
> |---|---|
> | `MyVar1 ← Total1 / Total2` | REAL |
> | `MyVar2 ← 27/10/2023` | DATE |
> | `MyVar3 ← "Sum1 / Sum2"` | STRING |
> | `MyVar4 ← Result1 AND Result2` | BOOLEAN |

### Q9
> **[mark-scheme]**
> **One** mark for each row with appropriate variable name and data type
> 
> | **Example value** | **Explanation** | **Variable name** | **Data type** |
> |---|---|---|---|
> | `"Mr Khan"` | The name of the customer | **CustomerName** | **STRING** |
> | `3` | The number of items in the order | **NumItems** | **INTEGER** |
> | `TRUE` | To indicate whether this is a new customer | **NewCustomer** | **BOOLEAN** |
> | `15.75` | The deposit paid by the customer | **Deposit** | **REAL** |
> **[mark-scheme]**
> **One** mark per point **Max 3 **marks
> 
> Declaration 
> 1.  Declare a composite / record (type) 
> 2. Declare an array of the given composite / record (type)
> 
> Expansion of record: 
> 3.  … containing all data items required // containing items of different data types
> 
> Expansion of array: 
> 4.  … where **each array element** represents data for one order / customer (order)

### Q10
> **[mark-scheme]**
> **One **mark per point:
> 
> - `ThisValue`:  **INTEGER **
> - `Check`:             **REAL **
> - `Level`:             **STRING**

### Q11
> **[mark-scheme]**
> **One** mark for `TYPE FootballClub` and `ENDTYPE` correct 
> **One** mark for every two correct declarations
> 
> Example answer 
> `TYPE FootballClub `
> `    DECLARE TeamName : STRING `
> `    DECLARE DateOfJoining : DATE `
> `    DECLARE MainTelephone : STRING `
> `    DECLARE ManagerName : STRING `
> `    DECLARE NumberOfMembers : INTEGER `
> `    DECLARE LeaguePosition : INTEGER`
> ` ENDTYPE`

### Q12
> **[mark-scheme]**
> One mark for either:
> 
> - Set the `Item_ID `field to an empty string / NULL / invalid value
> - Set `Weight` to <= 0 / zero

### Q13
> **[mark-scheme]**
> Pseudocode:
> 
> `TYPE Component `
> `   DECLARE Item_Num : INTEGER `
> `   DECLARE Reject   : BOOLEAN `
> `   DECLARE Stage    : CHAR `
> `   DECLARE Limit_1  : REAL `
> `   DECLARE Limit_2  : REAL `
> `ENDTYPE `
> 
> Mark as follows:
> 
> 1. One mark for` TYPE` and `ENDTYPE` statements
> 2. One mark for `Item_Num` and `Reject` fields
> 3. One mark for `Stage` field
> 4. One mark for Limit fields as `REAL`
> **[mark-scheme]**
> One mark per point:
> 
> 1. Allows for iteration / can use a loop **to access the records / data items **
> 2. Use of index to directly access a **record** in the array // Example of simplification of code e.g. use of dot notation Item[1].Stage
> 3. Simplifies the code / algorithm // Reduces duplication of code // **Program** easier to write / understand / maintain / test / debug // **Data items**/**record** easier to search / sort / manipulate

### Q14
> **[mark-scheme]**
> Example solution
> 
> `PROCEDURE Count(ThisPlayer : INTEGER, ThisRole : STRING) `
> `   DECLARE Index, Num, Total : INTEGER `
> 
> `   Num `$\leftarrow$` 0 `
> `   Total `$\leftarrow$` 0 `
> 
> `   FOR Index `$\leftarrow$` 1 TO 45 `
> `      IF Character[Index].Player = ThisPlayer AND __`
> `         Character[Index].Role = ThisRole THEN `
> `         Num `$\leftarrow$` Num + 1 `
> `         Total `$\leftarrow$` Total + Character[Index].SkillLevel `
> `   NEXT Index `
> 
> `   IF Num > 0 THEN `
> `      OUTPUT "Player ", ThisPlayer, __  `
> `             " has ", Num, " characters with the role of `
>                                      `",ThisRole, " and the total skill level is `
>                                      `",Total `
> `   ELSE `
> 
> `          OUTPUT "No characters with that role are assigned to this player" `
> 
> `ENDIF `
> 
> `ENDPROCEDURE `
> 
> **MP1**    Initialisation of local integers for `Num` and `Total `
> **MP2**   Loop through 45 elements 
> **MP3**   Attempt to check Player and Role fields **in a loop** 
> **MP4**   Correctly compare `Player` field with parameter **in a loop** 
> **MP5**   Correctly compare `Role` field with parameter in a loop 
> **MP6**    ... if player and role found, increment `Num` **an**d sum Skill Total in a loop 
> **MP7**    Test for any matches **after the loop** 
> **MP8**   ** Both** possible OUTPUT statements correctly formed following an attempt at MP6 but outputting one only
> 
> **Max 7 marks**

### Q15
| **Variable** | **Example data value** | **Data type** |
|---|---|---|
| `Available` | `TRUE` | BOOLEAN |
| `Received` | `"18/04/2021"` | STRING |
| `Index` | `100` | INTEGER |

One mark per row

### Q16
> **[mark-scheme]**
> Example solution:
> 
> `PROCEDURE Assign(ThisRole : STRING, ThisPlayer : INTEGER) `
> `   DECLARE Index : INTEGER `
> `   DECLARE Done : BOOLEAN `
> 
> `   Done `$\leftarrow$` FALSE    `
> `   Index `$\leftarrow$` 1 `
> 
> `WHILE Index < 46 AND Done = FALSE `
> `   IF Character[Index].Player = 0 AND __  `
> `      Character[Index].Role = ThisRole THEN `
> `      Character[Index].Player `$\leftarrow$` ThisPlayer `
> `      Done `$\leftarrow$` TRUE `
> `   ELSE `
> `      Index `$\leftarrow$` Index + 1 `
> `   ENDIF `
> `ENDWHILE `
> 
> `IF Done = TRUE THEN `
> `   OUTPUT Character[Index].Name, " the ", __`
> `          Character[Index].Role, __ `
> `          " has been assigned to player ", ThisPlayer `
> `ELSE `
> `   OUTPUT "No characters with this role are available" ENDIF `
> `ENDPROCEDURE `
> 
> Mark as follows: 
> **MP1**    Loop until ‘found’ or all 45 elements considered 
> **MP2**   Test of` Player` field – i.e. not value **in a loop **
> **MP3**   `... AND Role` – i.e. match for **ThisRole** parameter **in a loop **
> **MP4**   If available character found, assign `ThisPlayer` to the character **in a loop** 
> **MP5 **  When character found set termination condition/flag 
> **MP6**   **Both** OUTPUT messages logically <u>correctly placed</u> 
> **MP7**   **Both** OUTPUT statements <u>correctly formed</u>

### Q17
> **[mark-scheme]**
> One mark per row:
> 
> | **Variable name** | **Used to store** | **Data type** |
> |---|---|---|
> | `Name` | A customer name. | **STRING** |
> | `Index` | An array index. | **INTEGER** |
> | `Result` | The result of the division of any two non-zero numbers. | **REAL** |

### Q18
> **[mark-scheme]**
> Example solution:
> 
> `FUNCTION Evaluate(NumStr1, NumStr2 : STRING) RETURNS Result `
> `   DECLARE RetVal : Result `
> `   DECLARE Num1, Num2 : REAL `
> 
> `   RetVal.Done `$\leftarrow$` FALSE `
> 
> `   IF IS_NUM(NumStr1) = TRUE AND IS_NUM(NumStr2) = TRUE THEN `
> `      Num1 `$\leftarrow$` STR_TO_NUM(NumStr1) `
> `      Num2 `$\leftarrow$` STR_TO_NUM(NumStr2) `
> `      IF Num2 <> 0 THEN `
> `         RetVal.Value `$\leftarrow$` (Num1 / Num2) `
> `         RetVal.Done `$\leftarrow$` TRUE `
> `      ENDIF `
> `   ENDIF `
> 
> `RETURN RetVal `
> 
> `ENDFUNCTION `
> 
> Note that order of parameters is not specified so divisor could be either parameter.
> 
> Mark as follows:
> 
> 1. Function heading, parameters, ending
> 2. ... Correct return type of `Result `
> 3. Local declaration of type `Result`
> 4. Attempt at using `IS_NUM()` to check **both** parameters/strings
> 5. Attempt at using of `STR_TO_NUM()` to convert **both** parameters/strings
> 6. Check if the divisor, is non-zero ...
> 7. … **and** if so correct calculation **and** assignment to `Value` field
> 8. Return variable of type `Result` having assigned <u>both</u> fields
> 
> **Max 6 marks**

### Q19
> **[mark-scheme]**
> One mark per row:
> 
> | **Variable name** | **Data type** |
> |---|---|
> | `HighRate` | Boolean |
> | `TaxPayable` | Real |
