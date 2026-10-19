# Mark Schemes — Programming Basics
**11. Programming** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (14 questions)


### Q1
Line 08: `DIV` gives only the whole number part of a division, so the fractional part of the average is thrown away. It should be the division operator, giving `Average ← Total / Count`. **[1]**

Line 09: `OR` is the wrong logical operator and makes the condition `TRUE` for every possible average. It should be `Valid ← (Average >= 40) AND (Average <= 100)`. **[1]**

Line 10: `>` leaves out an average of exactly 90, which should count as a top mark. It should be `Top ← Average >= 90`. **[1]**

Line 11: `+` adds two numbers and cannot join two strings. It should be the concatenation operator, giving: **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for line 08: `DIV` should be `/`
> 
> **1 mark** for line 09: `OR` should be `AND`
> 
> **1 mark** for line 10: `>` should be `>=`
> 
> **1 mark** for line 11: `+` should be `&`
> 
> Each mark needs the line to be identified and the correction to be given. Accept the corrected statement written out in full instead of naming the operator on its own.
> 
> Accept "integer division" or "whole number division" as a description of `DIV`.
> 
> Do not accept a correction of line 08 that uses `INT()`. That also throws the fractional part away.
> 
> Do not accept a change to line 02. `Average` is correctly declared as `REAL`, and the fault is the operator used on line 08.
> 
> Do not accept `Top ← Average > 89` as the correction on line 10. `Average` is a `REAL`, so an average of 89.5 would then be treated as a top mark.
> 
> Do not accept a fifth error. Lines 06, 07 and 12 are correct.

> **[exam-tip]**
> Work from the list of requirements, not from the code. Each error is only an error because the code does something different from what the list says, and line 09 proves it: `(Average >= 40) OR (Average <= 100)` is perfectly legal pseudocode, it is just always `TRUE`, so `Valid` never becomes `FALSE`.
> 
> Two habits picked up from other languages cost marks here. `+` joins text in many programming languages, but in this pseudocode `+` is arithmetic only and `&` is the operator that joins strings. And `DIV` is not a neater way of writing `/`, it is a different operator that discards the remainder, so 290 `DIV` 7 gives 41 while 290 `/` 7 gives 41.428571.

### Q2
**[3 marks]**

> **[mark-scheme]**
> **1 mark** for testing that the seat number is even, using `SeatNum MOD 2 = 0`
> 
> **1 mark** for testing that the seat has not been booked, using `NOT Booked`
> 
> **1 mark** for testing the two ranges with `OR` inside brackets, and joining all three tests with `AND`
> 
> Accept `Booked = FALSE` in place of `NOT Booked`.
> 
> Accept `SeatNum MOD 2 <> 1` in place of `SeatNum MOD 2 = 0`.
> 
> Accept the three tests written in any order, and the whole condition written inside an `IF ... THEN` statement.
> 
> Do not accept `SeatNum MOD 2 = 1`. That is `TRUE` for odd seat numbers.
> 
> Do not accept `(SeatNum < 50) AND (SeatNum > 150)`. No seat number can be both, so the condition would never be `TRUE`.
> 
> Do not accept `Booked` on its own in place of `NOT Booked`.
> 
> The brackets around the `OR` test are part of the third marking point. This pseudocode sets no order of precedence for `AND`, `OR` and `NOT`, so without brackets the condition can be read in two different ways.

> **[exam-tip]**
> The word "either" in the third rule means `OR`, and students write `AND` there because the three rules above it are joined by "all three of the following are true". Read carefully: the three rules are joined by `AND`, but the two halves of the third rule are joined by `OR`.
> 
> `MOD` gives the remainder, so an even number is one where `SeatNum MOD 2` gives 0. Write that comparison with 0 out in full. `SeatNum MOD 2` on its own is a number, not a `BOOLEAN`, so it cannot be joined to the rest of the condition with `AND`.

### Q3
Condition 1: `Count >= Limit` **[1]**

Condition 2: `Count < Limit` **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `Count >= Limit`
> 
> **1 mark** for `Count < Limit`
> 
> Accept the operands written the other way round, so `Limit <= Count` for condition 1 and `Limit > Count` for condition 2.
> 
> Do not accept `Count > Limit` for condition 1. That answer is `FALSE` when the two values are equal, but the original condition is `TRUE`.
> 
> Do not accept `Count <= Limit` for condition 2. That answer is `TRUE` when the two values are equal, but the original condition is `FALSE`.
> 
> Do not accept an answer that still contains `NOT`, `AND` or `OR`. The question asks for one comparison operator only.

> **[exam-tip]**
> Both marks turn on the case where the two values are equal, and that is exactly the case students skip. Test every answer you write three times: once with `Count` below `Limit`, once with the two equal, and once with `Count` above.
> 
> `NOT` in front of a comparison flips it completely, it does not simply relax it. The opposite of `>=` is `<`, never `<=`. Getting this wrong builds an off by one error into the program that shows up on only one value in a million inputs.

### Q4
**[5 marks]**

> **[mark-scheme]**
> **1 mark** for declaring every variable used, each with a suitable data type
> 
> **1 mark** for a prompt followed by an input of the start reading
> 
> **1 mark** for a prompt followed by an input of the end reading
> 
> **1 mark** for calculating the units used as the end reading minus the start reading
> 
> **1 mark** for calculating the total cost using `UnitCost`, and outputting it with a message
> 
> Accept the declarations written as four separate `DECLARE` statements.
> 
> Accept the two calculations combined into one statement, for example:
> 
> Where the calculations are combined, the variable `UnitsUsed` is not needed and does not have to be declared.
> 
> Accept any sensible identifiers, and any sensible wording for the prompts and the message.
> 
> Do not accept `TotalCost` declared as `INTEGER`. An `INTEGER` multiplied by a `REAL` gives a `REAL`, so a cost such as 38.25 would be lost.
> 
> Do not accept a declaration of `UnitCost`. It is already declared as a constant, and declaring it again as a variable would allow its value to change.
> 
> Do not accept an `INPUT` statement with no `OUTPUT` prompt before it.
> 
> Do not accept `UnitsUsed ← StartReading - EndReading`. That subtraction is the wrong way round and gives a negative number of units.

> **[exam-tip]**
> The most expensive mistake here is multiplying a meter reading by the unit cost. A meter reading is a running total of everything the household has ever used, so only the difference between the two readings belongs to this month.
> 
> The other mark that goes missing is the prompt. In this pseudocode `INPUT` takes an identifier and nothing else, so `INPUT "Enter the reading", StartReading` is not valid. Write the prompt as a separate `OUTPUT` statement on the line above.

### Q5
| Example value | Explanation | Variable name | Data type |
|---|---|---|---|
| "Kigali" | The city in which the library branch is located | **BranchCity** | **STRING** |
| TRUE | A value that shows whether the book is on loan at the moment | **OnLoan** | **BOOLEAN** |
| 14/03/2026 | The day on which the book must be returned | **DueDate** | **DATE** |
| 2.75 | The fine in dollars charged for each day a book is returned late | **DailyFine** | **REAL** |

Row 1: a suitable identifier such as `BranchCity`, with data type `STRING`. **[1]**

Row 2: a suitable identifier such as `OnLoan`, with data type `BOOLEAN`. **[1]**

Row 3: a suitable identifier such as `DueDate`, with data type `DATE`. **[1]**

Row 4: a suitable identifier such as `DailyFine`, with data type `REAL`. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for row 1: a suitable identifier together with the data type `STRING`
> 
> **1 mark** for row 2: a suitable identifier together with the data type `BOOLEAN`
> 
> **1 mark** for row 3: a suitable identifier together with the data type `DATE`
> 
> **1 mark** for row 4: a suitable identifier together with the data type `REAL`
> 
> Each mark needs both the identifier and the data type to be correct.
> 
> Accept any identifier that describes the value it holds and follows the naming rules, so letters, digits and the underscore character only, starting with a letter.
> 
> Do not accept `CHAR` for row 1. A `CHAR` holds exactly one character and `"Kigali"` holds six.
> 
> Do not accept `STRING` for row 3. The `DATE` data type exists in this pseudocode, and a date held as a string cannot be used with the date functions on the insert.
> 
> Do not accept `INTEGER` for row 4. The value 2.75 has a fractional part.
> 
> Do not accept a single letter such as `C` as an identifier here. The identifier must describe the value it holds.

> **[exam-tip]**
> Two rows lose marks again and again. The date is written as `STRING` because it contains slashes and looks like text, and the fine is written as `INTEGER` because money often is. Ask yourself what the program will need to do with the value: if it has to work out which month a date falls in, it must be a `DATE`, and if a value can end in 75 cents, it must be a `REAL`.
> 
> Give the variable a name that says what it holds. `DueDate` earns the mark, `D` does not, and a name with a space in it such as `Due Date` is not a legal identifier.

### Q6
**[2 marks]**

> **[mark-scheme]**
> **1 mark** for a constant declaration of the fill character, in the form `CONSTANT <identifier> = '*'`
> 
> **1 mark** for a constant declaration of the label width, in the form `CONSTANT <identifier> = 4.5`
> 
> Accept any identifier that describes the value it holds and follows the naming rules, so letters, digits and the underscore character only, starting with a letter.
> 
> Accept `"*"` written in double quotes. A string of length 1 may be treated as either `CHAR` or `STRING`.
> 
> Do not accept a declaration that uses the assignment arrow, such as `CONSTANT FillChar ← '*'`. A constant declaration uses `=`.
> 
> Do not accept `DECLARE FillChar : CHAR` followed by a separate assignment statement. That creates a variable, and its value could then be changed while the program runs.
> 
> Do not accept a value that is not a literal, such as `CONSTANT LabelWidth = MaxWidth / 2`. Only a literal may be used as the value of a constant.

> **[exam-tip]**
> A constant is declared in one single statement, and the value is part of that statement. Students very often write the name on one line and the value on the next, the way they would set up a variable, and lose the mark because a value written that way can be changed later.
> 
> Watch the quote marks and the decimal point. One character goes between single quotes, such as `'*'`, and text of more than one character between double quotes, such as `"Label"`. A real number must have at least one digit on each side of the decimal point, so write `4.5`, never `4.` or `.5`.

### Q7
> **[mark-scheme]**
> | **Expression** | **Evaluates to** |
> |---|---|
> | `Fraction >= 0.2 AND NOT Active` | **FALSE** |
> | `INT((Fraction * 100) + 13.3)` | **33** |
> | `STR_TO_NUM(MID(Code, 4, 2)) + 5` | **28** |
> | `LENGTH("TRUE" & Code)` | **11** |

### Q8
> **[mark-scheme]**
> **One** mark per row
> 
> | **Expression** | **Evaluates to** |
> |---|---|
> | `(Total * DepRate) + 1.5` | **249.50** |
> | `RIGHT(Description, 7)` | **"(small)"** |
> | `(LENGTH(Description) - 8) > 16` | **TRUE** |
> | `NUM_TO_STR(INT(DepRate * 10)) & '%'` | **"20%"** |

### Q9
> **[mark-scheme]**
> | **Pseudocode expression** | **Evaluates to** |
> |---|---|
> | **MID**` ("Random", 2, 3)` | `"and"` |
> | `5 + `**DAY**` (10/11/2023)` | `15` |
> | **IS_NUM**` ("45000")` | `TRUE` |
> | `(20 `**MOD**` 3) + 1` | `3` |
> 
> One mark per row

### Q10
> **[mark-scheme]**
> | **Expression** |
> |---|
> | `MyInt` $\leftarrow$ **INT** `(3.1415926)` |
> | `MyChar` $\leftarrow$ **MID** `("Elwood", 3, 1)` |
> | `Any of: `<br><br>- `MyString` $\leftarrow$ **NUM_TO_STR **`(`**INT** `(27.509))  `<br>- `MyString` $\leftarrow$ **CHR** `(`**INT** `(27.509))`<br>- `MyString` $\leftarrow$ **TO_UPPER**`(` **NUM_TO_STR**`( 27.509)) `<br>- `MyString` $\leftarrow$ **TO_LOWER**`(` **NUM_TO_STR**`( 27.509))` |
> | `Any of: `<br><br>- `MyInt` $\leftarrow$ **STR_TO_NUM** `(` **RIGHT** `("ABC123", 3)) `<br>- `MyInt` $\leftarrow$ **LENGTH** `(` **RIGHT** `("ABC123", 3)) `<br>- `MyInt` $\leftarrow$ **LENGTH** `(` **LEFT** `("ABC123", 3))` |
> 
> One mark per row

### Q11
> **[mark-scheme]**
> One mark per point:
> 
> 1. A (variable of type) string will be input // by example e.g. “67,72”
> 2. A special / identified character would need to be used to separate each numeric value // all numbers are fixed length

### Q12
> **[mark-scheme]**
> | **Assignment statement** | **Data type** |
> |---|---|
> | `A `$\leftarrow$`LEFT(MyName, 1)` | CHAR / STRING |
> | `B `$\leftarrow$` Total * 2` | INTEGER / REAL |
> | `C `$\leftarrow$`INT(ItemCost) / 3` | REAL |
> | `D `$\leftarrow$`"Odd OR Even"` | STRING |
> 
> One mark per row
> **[mark-scheme]**
> | **Expression** | **Evaluates to** |
> |---|---|
> | `Tries < 10 AND NOT Sorted` | TRUE |
> | `Tries MOD 4` | 1 |
> | `TO_LOWER(MID(ID, 3, 1))` | 'a' // "a" |
> | `LENGTH(ID & "xx") >= Tries` | TRUE |
> 
> One mark per row

### Q13
> **[mark-scheme]**
> | **Expression** | **Evaluates to** |
> |---|---|
> | `Available AND NOT(Index > 100)` | TRUE |
> | `Index MOD 30` | 10 |
> | `NUM_TO_STR(Index + "33")` | ERROR |
> 
> One mark per row

### Q14
> **[mark-scheme]**
> (i)
> 
> Use constants (to represent the tax rate values)
> 
> (ii)
> 
> One mark per bullet point (or equivalent to max 3):
> 
> 1. **Tax rates** are entered once only
> 2. Avoids / Minimise (input) error(s) / changing the Tax rates accidentally // avoids different values for tax rates at different points in the program
> 3. When required, the constant value (representing a tax rate) is changed (once) // Easier to maintain / update the program (when the tax rates change)
> 4. Makes the program / code easier to understand
