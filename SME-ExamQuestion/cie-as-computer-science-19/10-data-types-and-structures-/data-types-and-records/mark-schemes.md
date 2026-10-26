# Mark Schemes — Data Types & Records
**10. Data Types & Structures** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (13 questions)


### Q1
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

### Q2
> **[mark-scheme]**
> | **Assignment statement** | **Data type** |
> |---|---|
> | `MyVar1 ← Total1 / Total2` | REAL |
> | `MyVar2 ← 27/10/2023` | DATE |
> | `MyVar3 ← "Sum1 / Sum2"` | STRING |
> | `MyVar4 ← Result1 AND Result2` | BOOLEAN |

### Q3
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

### Q4
> **[mark-scheme]**
> **One **mark per point:
> 
> - `ThisValue`:  **INTEGER **
> - `Check`:             **REAL **
> - `Level`:             **STRING**

### Q5
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

### Q6
> **[mark-scheme]**
> One mark for either:
> 
> - Set the `Item_ID `field to an empty string / NULL / invalid value
> - Set `Weight` to <= 0 / zero

### Q7
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

### Q8
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

### Q9
| **Variable** | **Example data value** | **Data type** |
|---|---|---|
| `Available` | `TRUE` | BOOLEAN |
| `Received` | `"18/04/2021"` | STRING |
| `Index` | `100` | INTEGER |

One mark per row

### Q10
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

### Q11
> **[mark-scheme]**
> One mark per row:
> 
> | **Variable name** | **Used to store** | **Data type** |
> |---|---|---|
> | `Name` | A customer name. | **STRING** |
> | `Index` | An array index. | **INTEGER** |
> | `Result` | The result of the division of any two non-zero numbers. | **REAL** |

### Q12
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

### Q13
> **[mark-scheme]**
> One mark per row:
> 
> | **Variable name** | **Data type** |
> |---|---|
> | `HighRate` | Boolean |
> | `TaxPayable` | Real |
