# Mark Schemes — Programming Basics
**11. Programming** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (8 questions)


### Q1
> **[mark-scheme]**
> | **Expression** | **Evaluates to** |
> |---|---|
> | `Fraction >= 0.2 AND NOT Active` | **FALSE** |
> | `INT((Fraction * 100) + 13.3)` | **33** |
> | `STR_TO_NUM(MID(Code, 4, 2)) + 5` | **28** |
> | `LENGTH("TRUE" & Code)` | **11** |

### Q2
> **[mark-scheme]**
> **One** mark per row
> 
> | **Expression** | **Evaluates to** |
> |---|---|
> | `(Total * DepRate) + 1.5` | **249.50** |
> | `RIGHT(Description, 7)` | **"(small)"** |
> | `(LENGTH(Description) - 8) > 16` | **TRUE** |
> | `NUM_TO_STR(INT(DepRate * 10)) & '%'` | **"20%"** |

### Q3
> **[mark-scheme]**
> | **Pseudocode expression** | **Evaluates to** |
> |---|---|
> | **MID**` ("Random", 2, 3)` | `"and"` |
> | `5 + `**DAY**` (10/11/2023)` | `15` |
> | **IS_NUM**` ("45000")` | `TRUE` |
> | `(20 `**MOD**` 3) + 1` | `3` |
> 
> One mark per row

### Q4
> **[mark-scheme]**
> | **Expression** |
> |---|
> | `MyInt` $\leftarrow$ **INT** `(3.1415926)` |
> | `MyChar` $\leftarrow$ **MID** `("Elwood", 3, 1)` |
> | `Any of: `<br><br>- `MyString` $\leftarrow$ **NUM_TO_STR **`(`**INT** `(27.509))  `<br>- `MyString` $\leftarrow$ **CHR** `(`**INT** `(27.509))`<br>- `MyString` $\leftarrow$ **TO_UPPER**`(` **NUM_TO_STR**`( 27.509)) `<br>- `MyString` $\leftarrow$ **TO_LOWER**`(` **NUM_TO_STR**`( 27.509))` |
> | `Any of: `<br><br>- `MyInt` $\leftarrow$ **STR_TO_NUM** `(` **RIGHT** `("ABC123", 3)) `<br>- `MyInt` $\leftarrow$ **LENGTH** `(` **RIGHT** `("ABC123", 3)) `<br>- `MyInt` $\leftarrow$ **LENGTH** `(` **LEFT** `("ABC123", 3))` |
> 
> One mark per row

### Q5
> **[mark-scheme]**
> One mark per point:
> 
> 1. A (variable of type) string will be input // by example e.g. “67,72”
> 2. A special / identified character would need to be used to separate each numeric value // all numbers are fixed length

### Q6
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

### Q7
> **[mark-scheme]**
> | **Expression** | **Evaluates to** |
> |---|---|
> | `Available AND NOT(Index > 100)` | TRUE |
> | `Index MOD 30` | 10 |
> | `NUM_TO_STR(Index + "33")` | ERROR |
> 
> One mark per row

### Q8
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
