# Mark Schemes — User-defined Data Types
**13. Data Representation** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (12 questions)


### Q1
Declaring the counter and setting it to zero before the loop earns the first mark. **[1]**

The count-controlled loop running from 1 to 200, closed with `NEXT`, earns the second mark. **[1]**

Reaching the category of the current array element with dot notation earns the third mark. **[1]**

Comparing that category with `Senior` and increasing the counter earn the fourth mark. **[1]**

Closing the `IF` and outputting the count after the loop earn the fifth mark. **[1]**

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for declaring a counter and setting it to 0 before the loop
> 
> **1 mark** for a loop covering 1 to 200 inclusive, correctly closed
> 
> **1 mark** for `Members[Index].Category`, using the loop variable as the array index
> 
> **1 mark** for the comparison with `Senior` and `SeniorCount ← SeniorCount + 1`
> 
> **1 mark** for `ENDIF` present and `OUTPUT SeniorCount` placed after the loop
> 
> Accept a `WHILE` loop or a `REPEAT` loop that covers indices 1 to 200 inclusive and handles its own counter correctly.
> 
> Accept any sensible identifier for the counter and for the loop variable.
> 
> Accept the `DECLARE` statements being left out, provided the counter is still set to 0 before the loop.
> 
> Do not accept `Members.Category[Index]`. The array subscript selects the record first, and dot notation then selects a field inside that record.
> 
> Do not accept `OUTPUT SeniorCount` written inside the loop, which outputs 200 values instead of one.
> 
> Do not accept a loop running `1 TO 199` or `0 TO 200`. The array is declared `ARRAY[1:200]`, so both bounds are included.

> **[exam-tip]**
> The order of the subscript and the dot is what this question is really testing. `Members[Index]` is one whole record, and `.Category` then picks one field out of that record. Writing the dot first asks for a field of the array itself, which does not exist.
> 
> Two easy marks sit outside the loop. Set the counter to zero before the loop starts, and put the `OUTPUT` after `NEXT`. If you write a perfect loop and then output inside it, you lose a mark you never needed to risk.

### Q2
Opening with `TYPE ClubMember` and closing with `ENDTYPE` earns the first mark. **[1]**

The two fields that use built-in data types earn the second mark. **[1]**

The field whose data type is the user-defined type `Membership` earns the third mark. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `TYPE ClubMember` and `ENDTYPE` both correct
> 
> **1 mark** for `DECLARE FamilyName : STRING` and `DECLARE DateJoined : DATE`
> 
> **1 mark** for `DECLARE Category : Membership`
> 
> Accept any sensible identifier for each of the three fields.
> 
> Accept the three `DECLARE` statements in any order.
> 
> Accept `STRING` for the date field, although `DATE` is the expected type.
> 
> Do not accept `DECLARE Category : (Junior, Adult, Senior)`. The type already exists and must be named.
> 
> Do not accept an answer with no `ENDTYPE`, or one using `ENDDECLARE` or `END TYPE`.

> **[exam-tip]**
> The mark most likely to cost you here is the third one. When a question hands you an existing user-defined type and tells you to use it, the data type of that field is the type's name, copied exactly as printed. Repeating the list of values instead defines a second, unnamed type and earns nothing.
> 
> A record is the only user-defined type on this course that needs `ENDTYPE`. Write `TYPE` and `ENDTYPE` first and fill in the fields between them, so that running short of time cannot cost you that mark.

### Q3
| Requirement | Composite data type |
|---|---|
| A collection of the valid currency symbols used by a program. Every symbol is a CHAR and the order of the symbols does not matter. | **Set** |
| A group of related items about one employee: family name, salary and start date. | **Record** |
| A template that groups data together with the procedures and functions that operate on that data. | **Class** |

Set, for an unordered collection whose elements are all of one data type. **[1]**

Record, for a fixed number of related items that may be of different data types. **[1]**

Class, for data grouped with the operations that act on it. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for Set in the first row
> 
> **1 mark** for Record in the second row
> 
> **1 mark** for Class in the third row
> 
> Accept object for the third row.
> 
> Do not accept array in the first row. An array is a built-in structure, not a user-defined composite data type, and its elements are ordered by index.
> 
> Do not accept enumerated or pointer in any row. Both are non-composite.

> **[exam-tip]**
> Set and array are easy to confuse because both hold many items of one data type. The deciding words in a question are order and index. If the question says the order does not matter, or mentions union and intersection, it is a set. If the items are reached by position, it is an array.
> 
> Read the word composite in the question before you answer. Enumerated and pointer are user-defined too, but they are non-composite, so neither can ever be the answer to a question phrased like this one.

### Q4
The assignment of the enumerated value earns the first mark. **[1]**

The condition testing both qualifying values earns the second mark. **[1]**

The output inside the `THEN` branch earns the third mark. **[1]**

The `ELSE` branch with its output, and `ENDIF`, earn the fourth mark. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for `ThisMember ← Silver`
> 
> **1 mark** for an `IF` whose condition is true for `Gold` and for `Platinum` and false for the other two values
> 
> **1 mark** for `OUTPUT "Discount applies"` inside the `THEN` branch
> 
> **1 mark** for `ELSE`, `OUTPUT "No discount"` and `ENDIF`
> 
> Accept `ThisMember >= Gold` as the condition, because the values of an enumerated type are ordered and `Gold` and `Platinum` are the last two in the list.
> 
> Accept the two outputs the other way round with the condition reversed, for example testing for `Basic` or `Silver` first.
> 
> Do not accept `ThisMember ← "Silver"`. The value is an identifier from the type definition, not a `STRING`.
> 
> Do not accept `ThisMember = Gold OR Platinum`. The second half of the condition has nothing to compare.
> 
> Do not accept an answer with no `ENDIF`.

> **[exam-tip]**
> The condition `ThisMember = Gold OR Platinum` reads correctly in English and is the single most common wrong answer on questions of this shape. Pseudocode compares one thing with one thing, so the variable has to be named on both sides of the `OR`.
> 
> There is no else-if keyword in this course's pseudocode, so do not reach for one. A single `IF` with an `ELSE` is all this task needs.

### Q5
The keyword `TYPE` with the type name earns the first mark. **[1]**

The pointer symbol followed by the data type held at the memory location earns the second mark. **[1]**

The variable declaration, using the new type name, earns the third mark. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `TYPE TTempPointer =`
> 
> **1 mark** for the right-hand side written as the pointer symbol followed by REAL, exactly as shown in the model answer
> 
> **1 mark** for `DECLARE TempStore : TTempPointer`
> 
> Accept any spelling of the two identifiers, provided the name used in the `DECLARE` statement matches the name used in the `TYPE` statement.
> 
> Do not accept the pointer symbol in the `DECLARE` statement. Declaring a variable of a pointer type does not use it.
> 
> Do not accept a right-hand side naming a type other than REAL, because the stored temperature is a `REAL` value.

> **[exam-tip]**
> Two marks are commonly lost together here. The first is writing the pointer symbol in the variable declaration as well as in the type definition. It belongs only in the `TYPE` line, which is where the pointer type is created.
> 
> The second is naming the pointer type itself on the right-hand side, giving a definition that refers to itself. The data type on the right is the type of the data sitting at the memory location, which the question tells you is `REAL`.

### Q6
The keyword `TYPE` and the type name earn the first mark. **[1]**

The five values, in brackets and separated by commas, earn the second mark. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `TYPE SkyState =`
> 
> **1 mark** for `(Clear, Cloudy, Rain, Snow, Fog)`
> 
> Accept the five values in any order.
> 
> Accept a different capitalisation of the type name and of the values.
> 
> Do not accept the values written as strings, for example `("Clear", "Cloudy")`. The values of an enumerated type are identifiers, not `STRING` literals.
> 
> Do not accept `DECLARE SkyState = (Clear, Cloudy, Rain, Snow, Fog)`. A type is defined with `TYPE`; `DECLARE` creates a variable.
> 
> Do not accept `ENDTYPE` on a following line. `ENDTYPE` closes a record definition only.

> **[exam-tip]**
> The commonest loss of a mark here is putting quotation marks round the values. If you have met `STRING` arrays first, you may reach for `"Clear"` out of habit. An enumerated value is a name the program invents, so it is written bare.
> 
> The second habit to break is adding `ENDTYPE`. An enumerated definition is one line and ends at the closing bracket. Only a record definition, which starts with `TYPE` on its own line, needs `ENDTYPE`.

### Q7
**One mark** per mark point – composite (**Max 2**)

MP1 A (user defined) data type that is a collection of data that can consist of multiple elements

MP2 …of different or the same **data types **

MP3 …grouped under a single identifier.

**One mark **per mark point – non-composite (**Max 2**)

MP4 It can be defined without referencing another data type.

MP5 It can be a primitive type available in a programming language, or a user- defined type.

### Q8
> **[mark-scheme]**
> **One mark** per mark point – enumerated type (**Max 2**)
> 
> MP1 A user-defined non-composite (data type) (only award once)
> 
> MP2 …with a list of all possible values
> 
> MP3 …that is ordered.
> 
> **One mark** per mark point – pointer type (**Max 2**)
> 
> MP4 A user-defined non-composite (data type) (only award once)
> 
> MP5 …that stores addresses/memory locations only
> 
> MP6 …and indicates the type of data stored in the memory location.

### Q9
> **[mark-scheme]**
> **One mark **per mark point (**Max 3**)
> 
> MP1 A data type that is defined without referencing another data type.
> 
> MP2 It can be a primitive data type found in a programming language **or** a user-defined data type.
> 
> MP3 Example – enumerated data type / pointer data type / allow a correct example of an enumerated or pointer data type declaration.
> **[mark-scheme]**
> **One mark** per mark point (**Max 4**)
> 
> MP1 Type statement fully correct
> 
> MP2` DEFINE EvenNumbers `
> 
> MP3 Correct list of values in brackets
> 
> MP4 :`<set identifier>`  from Type statement used
> 
> **Example answer**
> 
> `TYPE Numbers = SET OF INTEGER `
> `DEFINE EvenNumbers (2, 4, 6, 8, 10, 12): Numbers`

### Q10
> **[mark-scheme]**
> One mark per mark point (**Max 2**)
> 
> *non-composite data types*
> 
> MP1 Non-composite data types can both be user-defined or primitive
> 
> MP2 Non-composite data types do not refer to other data types in their definition / contain one data type in their definition
> 
> MP3 Non-composite data types can be primitive/enumerated/pointer
> 
> **One **mark per mark point (**Max 2**)
> 
> *composite data types*
> 
> MP4 Composite data types can be user-defined or primitive
> 
> MP5 Composite data types refer to other data types in their definition/contain more than one data type in their definition
> 
> MP6 Composite data types can be record/set/class

### Q11
> **[mark-scheme]**
> **One mark** per mark point (**Max 3**)
> 
> MP1 A user-defined record data type is a composite data type
> 
> MP2 It uses other data types in its definition to form a single new data type
> 
> MP3 The data types referenced may be primitive data types from a programming language or they may be other userdefined data types.
> 
> MP4 Includes related items
> 
> MP5 Includes a fixed number of items.
> **[mark-scheme]**
> **One **mark for `TYPE Order `and `ENDTYPE` correct
> 
> **One **mark for correct use of `DECLARE` in all declarations seen
> 
> **One **mark for the **two **shaded declarations
> 
> **One **mark for the **two **unshaded declarations
> 
> Example answer
> 
> `TYPE Order`
> 
> `            DECLARE AccountNumber : INTEGER `
> 
> `            DECLARE OrderNumber : INTEGER `
> 
> `            DECLARE OrderPrice : REAL `
> 
> `           DECLARE OrderDate : DATE`
> 
> `ENDTYPE`

### Q12
> **[mark-scheme]**
> **One **mark per mark point (**Max 3**)
> 
> MP1 A set user-defined data type is a composite data type
> 
> MP2 … which includes a list of unordered elements
> 
> MP3 Set theory operations, such as intersection and union, can be applied to these elements
> 
> MP4 A set data type includes the type of data/data type it uses as part of its definition
> 
> MP5 All the elements are of the same data type.
> **[mark-scheme]**
> **One mark** for each mark point (**Max 4**)
> 
> MP1 `TYPE SymbolSet/Operators = `
> 
> MP2 `SET OF CHAR `
> 
> MP3 `DEFINE Operators/SymbolSet `
> 
> MP4 `('+', '–', '*', '/', '^')`
> 
> MP5 : `SymbolSet/Operators`
> 
> Example answers
> 
> `TYPE SymbolSet = SET OF CHAR `
> `DEFINE Operators ('+', '–', '*', '/', '^') : SymbolSet `
> 
> `TYPE Operators = SET OF CHAR `
> `DEFINE SymbolSet ('+', '–', '*', '/', '^') : Operators`
