# Mark Schemes — File Processing & Exception Handling
**20. Further Programming** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (21 questions)


### Q1
Procedure heading with an integer parameter, and `ENDPROCEDURE` **[1]**

File opened in `RANDOM` mode before the loop and closed after it **[1]**

Loop through positions 1 to 500 **[1]**

`SEEK` to the position, then `GETRECORD` into a `TItem` variable, in the loop **[1]**

Quantity compared with reorder level, and `Amount` added **[1]**

`SEEK` the same position and `PUTRECORD` the updated record **[1]**

**[6 marks]**

> **[mark-scheme]**
> **Any six from:**
> 
> - MP1 Procedure heading with an integer parameter, and `ENDPROCEDURE`
> - MP2 `OPENFILE "Stock.dat" FOR RANDOM` and subsequent `CLOSEFILE "Stock.dat"`
> - MP3 Loop for positions 1 to 500
> - MP4 `SEEK` to the loop position and `GETRECORD` into a variable of type `TItem`, in the loop
> - MP5 Test `ThisItem.Quantity < ThisItem.ReorderLevel` and add `Amount` to `Quantity`, in the loop
> - MP6 `SEEK` the same position and `PUTRECORD` the updated record, in the loop
> - MP7 Count initialised to 0, incremented for each updated record, and output after the loop
> 
> **[6 marks]**
> 
> Accept a conditional loop that counts from 1 to 500
> 
> Accept the file name held in a variable or constant
> 
> Accept `PUTRECORD` for every record, not only the updated ones, as long as `Quantity` is changed only when the test is true
> 
> Do not accept `READFILE` or `WRITEFILE` for MP4 or MP6: these read and write lines of a text file, not records
> 
> Do not accept a test of "less than or equal to" for MP5: an item exactly at its reorder level is not below it

> **[exam-tip]**
> The mark most often lost here is MP6. Adding `Amount` to `ThisItem.Quantity` changes only the copy of the record in memory. Unless the record is written back with `PUTRECORD` at the same position, the file is exactly as it was.
> 
> Also watch where the file is opened and closed. Opening it inside the loop, or closing it before the loop ends, means the file is not open for the next `GETRECORD`.

### Q2
Opening the file: `OPENFILE LockerFile FOR RANDOM` **[1]**

Reading the record: `GETRECORD LockerFile, ThisLocker` **[1]**

Returning to the record's position: `SEEK LockerFile, LockerNum` **[1]**

Writing the changed record back: `PUTRECORD LockerFile, ThisLocker` **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for each correctly completed line (max 4)
> 
> Accept `"Lockers.dat"` in place of `LockerFile` in any line
> 
> Do not accept `READ`, `WRITE` or `APPEND` as the file mode: records are read and written at a chosen position, which needs `RANDOM` mode
> 
> Do not accept `READFILE` or `WRITEFILE`: these are text file commands

> **[exam-tip]**
> Changing `ThisLocker` changes only the copy in memory. The file does not change until `PUTRECORD` writes the record back, and a common error is to stop after the assignment and leave the file untouched.
> 
> Always `SEEK` to the position again before `PUTRECORD`, exactly as Cambridge's own random file examples do before every `GETRECORD` and `PUTRECORD`. Then the record is certain to go back to the place it came from.

### Q3
The `SEEK` statement moves the file pointer to position 12 **[1]**

The `GETRECORD` statement reads the record at the file pointer into `ThisMember` **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `SEEK "Members.dat", 12`
> 
> **1 mark** for `GETRECORD "Members.dat", ThisMember`, after the `SEEK`
> 
> Do not accept `READFILE "Members.dat", ThisMember`: `READFILE` reads one line of a text file, not a record from a random file
> 
> Do not accept `GETRECORD` before `SEEK`: the record read would be the one at the old file pointer position

> **[exam-tip]**
> Learn the exact order of the two items after each command. The file name always comes first, then a comma, then the position for `SEEK` or the variable for `GETRECORD`. Students who write `GETRECORD ThisMember, "Members.dat"` or `SEEK 12` lose the mark.

### Q4
| Position | ProductCode before | ProductCode after |
|---|---|---|
| 1 | A101 | **A101** |
| 2 | B202 | **P999** |
| 3 | C303 | **B202** |
| 4 | D404 | **B202** |
| 5 | E505 | **B202** |
| 6 | (empty) | **B202** |

Positions 1 and 2 hold A101 and P999 **[1]**

Positions 3, 4, 5 and 6 all hold B202 **[1]**

The loop works upwards from position 2, so each record is copied over the next record before that record has been moved. B202 is copied into every later position and C303, D404 and E505 are lost **[1]**

The loop must work downwards from the last record, for example `FOR Position ← 5 TO 2 STEP -1` **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for positions 1 and 2 correct: A101, P999
> 
> **1 mark** for positions 3 to 6 all correct: B202
> 
> **1 mark** for the explanation: a record is overwritten before it has been moved // B202 is copied forward into every later position // C303, D404 and E505 are overwritten and lost
> 
> **1 mark** for the change: the loop counts down from 5 to 2, for example `FOR Position ← 5 TO 2 STEP -1`
> 
> Accept a description of the change, for example "start the loop at 5 and go down to 2"
> 
> Do not accept `FOR Position ← 2 TO 5 STEP -1`: a loop from 2 to 5 with a negative step does not work from the last record down
> 
> Do not accept a change that starts at 6: position 6 is empty, and copying it to position 7 does not move any record

> **[exam-tip]**
> Students often assume the code works because every line is a correct file command. Trace the file itself, one iteration at a time, and write down what each position holds after every `PUTRECORD`. The overwrite shows up on the very first pass.
> 
> To make space in a file, always move the record furthest from the gap first. The Cambridge Pseudocode Guide's own example of inserting a record uses a loop with `STEP -1` for exactly this reason.

### Q5
`SEEK` moves the file pointer directly to record position 14 (the value of `RoomPosition`) in `Rooms.dat` **[1]**

`GETRECORD` reads the record at the file pointer and assigns it to the variable `ThisRoom` **[1]**

`PUTRECORD` writes the data in `ThisRoom` into the file at the file pointer, replacing the record that was stored there, so the file now holds the new status **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `SEEK`: moves the file pointer to the position / location / address given (record 14)
> 
> **1 mark** for `GETRECORD`: reads the record at the file pointer into the variable `ThisRoom`
> 
> **1 mark** for `PUTRECORD`: writes the record in `ThisRoom` to the file at the file pointer, replacing / overwriting the data that was there
> 
> Accept "record number 14" or "the 14th record" for the position
> 
> Do not accept "`SEEK` searches the file for the room": `SEEK` does not compare any values, it goes straight to the position it is given
> 
> Do not accept "`PUTRECORD` adds a new record to the end of the file": it replaces the record at the file pointer

> **[exam-tip]**
> Many students read `SEEK` as "search" and describe a loop that checks each record in turn. No checking happens. The program already knows the position, and `SEEK` moves there in one step.
> 
> Also keep the text file and random file commands apart. `READFILE` reads the next line of a text file; `GETRECORD` reads one whole record, with all its fields, from the position the file pointer is at.

### Q6
| Task | File mode |
|---|---|
| Add a new line of text to the end of an existing log file, keeping the lines already in it | **APPEND** |
| Go directly to record 250 in a file of fixed-length records and replace that record | **RANDOM** |
| Output every line of a text file of product names, in order | **READ** |
| Create a new text file to hold today's results, replacing any file with the same name | **WRITE** |

Two correct rows **[1]**

All four rows correct **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for any two rows correct
> 
> **1 mark** for all four rows correct
> 
> Accept the modes in lower case, for example append, random, read, write
> 
> Do not accept `WRITE` for the log file: `WRITE` mode creates a new file, so every line already in the log is lost
> 
> Do not accept `READ` or `WRITE` for record 250: the record must be read and then written back at the same position, and only `RANDOM` mode allows a record to be read or written at any position in the file

> **[exam-tip]**
> The most common error is writing `WRITE` for "add a line to an existing file". `WRITE` always starts an empty file, and `APPEND` is the mode that keeps the old data and adds after it.
> 
> A file is opened in only one mode at a time. If a task needs to both read and replace a record in the middle of a file, the answer is `RANDOM`, not "READ and WRITE".

### Q7
Three lines, each with a matching event, for example:

| Line number | Event that causes the exception |
|---|---|
| **04** **[1]** | **The file Location.txt does not exist or cannot be found** **[1]** |
| **11** **[1]** | **The user input 21 or more at line 08, so Index reaches 21 and Readings[21] is outside the array bounds** **[1]** |
| **14** **[1]** | **The user input 0 at line 08, so the program attempts to divide by zero** **[1]** |

**[6 marks]**

> **[mark-scheme]**
> For each of three different lines (maximum 3 lines):
> 
> **1 mark** for a line number where an exception could occur
> 
> **1 mark** for an event that would cause the exception on that line
> 
> Accepted lines and events
> 
> Line 04: the file does not exist // is not found // the file name is wrong // the storage device fails (hardware failure)
> 
> Line 05: the file is empty, so there is no line to read // the end of the file has been reached // the storage device fails (hardware failure)
> 
> Line 08: the user inputs data of the wrong type // a non-integer, for example letters or 2.5
> 
> Line 11: the value of NumReadings is greater than 20, so the array index goes out of bounds // the user inputs data of the wrong type for a reading
> 
> Line 14: NumReadings is 0, so there is a divide by zero
> 
> The event mark can only be awarded for an event that matches the line number given
> 
> Do not accept line 12 for the out-of-bounds event: the exception occurs at line 11, which accesses the missing element first, so line 12 is never reached
> 
> Do not accept line 10 for a negative number of readings: the loop runs zero times and no exception occurs. A negative value also gives no exception at line 14, because only 0 causes a divide by zero

> **[exam-tip]**
> Trace what the program does with an unusual value before you claim an exception. A common mistake is to say that a negative number of readings breaks the loop at line 10. It does not: a count-controlled loop from 1 to -3 simply runs zero times.
> 
> Choose the line where the problem first happens. If the user asks for 25 readings, the error happens at line 11, when the program tries to store a value in Readings[21]. Line 12 would use that element too, but the program never gets there.

### Q8
While the program is running, the text file might not be found, or the storage device that holds it might fail **[1]**

Exception handling would trap this run-time error, so the program does not halt unexpectedly and the screen keeps working **[1]**

It would also let the program output a meaningful error message, for example "Temperature file not found", instead of stopping with no explanation **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - An exception is an unexpected event that happens while the program is running // an event that disrupts the normal flow of instructions
> - An example of an exception in this program: the file is not found // the storage device fails // hardware failure // the file is empty, so the mean calculation attempts to divide by zero // the end of the file is reached unexpectedly
> - Exception handling traps (some) run-time errors // responds to the unexpected event
> - It prevents the program halting unexpectedly // the program can continue running and the display is not left blank
> - It allows a meaningful error message to be produced
> 
> **[3 marks]**
> 
> Maximum 2 marks if no point refers to this program, for example the file, the storage device or the mean calculation

> **[exam-tip]**
> Do not confuse exception handling with validation. Validation checks data that a user inputs. It cannot stop a file going missing or a storage device failing while the program runs. Those are the events exception handling exists for.
> 
> "Explain why" needs reasons, not just a definition. Give an exception that could happen in this program, then say what handling it achieves: the program does not halt unexpectedly, and it gives a meaningful error message.

### Q9
The user inputs 0 as the second number, so the program attempts to divide by zero **[1]**

The user inputs data of the wrong type, for example letters instead of a whole number **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for divide by zero // the second number input is 0
> 
> **1 mark** for an input of the wrong data type // a non-numeric input, for example typing "ten" when a whole number is expected
> 
> Accept "division by zero error" or "a run-time error caused by dividing by 0" for the first point
> 
> Accept "user error, typing an incorrect data type" for the second point
> 
> Do not accept "syntax error": a syntax error stops the program being translated, so it never runs and no exception can occur
> 
> Do not accept "logic error": a logic error gives a wrong result but does not interrupt the program
> 
> Do not award two marks for two versions of the same exception, for example "dividing by 0" and "the second number is zero"

> **[exam-tip]**
> Name the event that causes the exception, not what happens afterwards. "The program crashes" or "the program stops" is the result of an exception that is not handled, so it earns no mark on its own.
> 
> Make your two answers genuinely different. Both marks here come from two different inputs: a zero, and data of the wrong type.

### Q10
**One **mark for description, for example:

An exception is an event that occurs during the execution of a program that

disrupts the normal flow of instructions / causes the program to halt execution

**One **mark for example:

- Hardware failure // hard disk crash
- Programming error // trying to access out-of-bounds array element // divide by zero error // runtime error
- User error // typing incorrect filename / data type
One mark for each correctly completed blank (Max 7)

`DECLARE Customer : TAccount`

`DECLARE Location : INTEGER`

`DECLARE MaxSize : INTEGER`

`DECLARE: FoundFlag : BOOLEAN`

`DECLARE SearchCustomer : STRING`

`MaxSize `$\leftarrow$` 1000`

`OPENFILE "AccountRecord.dat" FOR RANDOM`

`Location  `$\leftarrow$` 1`

`FoundFlag  `$\leftarrow$` FALSE`

`OUTPUT "Enter the customer’s name"`

`INPUT SearchCustomer`

`WHILE NOT FoundFlag AND Location <= MaxSize`

`    SEEK "AccountRecord.dat", Location`

`    GETRECORD "AccountRecord.dat", Customer`

`    IF SearchCustomer = Customer.Name THEN`

`        OUTPUT "Customer found: "`

`        OUTPUT Customer`

`        FoundFlag  TRUE`

`    ENDIF`

`    Location  `$\leftarrow$` Location + 1`

`ENDWHILE`

`IF NOT FoundFlag THEN`

`    OUTPUT "Customer does not exist."`

`ENDIF`

### Q11
**One **mark for each correctly completed line **(Max 5)**

`DECLARE Customer : TAccount`

`DECLARE Location : INTEGER`

`DECLARE AccountFile : STRING`

`AccountFile `$\leftarrow$` "AccountRecords.dat"`

`OPENFILE AccountFile FOR RANDOM`

`OUTPUT "Please enter an account number"`

`INPUT Customer.AccountNumber`

`Location `$\leftarrow$` Hash(Customer.AccountNumber)`

`SEEK AccountFile, Location`

`GETRECORD AccountFile, Customer`

`OUTPUT Customer`

`CLOSEFILE AccountFile`
One mark for correct definition

(Exception handling is the process of) responding to an unexpected event when the program is running so it does not halt unexpectedly
**One **mark per mark point (**Max 2**), for example:

- Programming errors
- User errors
- Hardware failure
- Runtime errors

### Q12
`PROCEDURE ReceiveFile(FileName : STRING)`

`    DECLARE FileData : STRING`

`    DECLARE CharCount : INTEGER`

`    CONSTANT Terminator = "****"`

`    OPENFILE FileName FOR WRITE`

`    FileData ← GetData()`

`    CharCount ← 0`

`    WHILE FileData <> Terminator`

`        WRITEFILE FileName, FileData`

`        CharCount ← CharCount + LENGTH(FileData)`

`        FileData ← GetData()`

`    ENDWHILE`

`    CLOSEFILE FileName`

`    OUTPUT CharCount (, " characters were written to ", FileName)`

`ENDPROCEDURE`

Mark as follows:

MP1 OPEN file in WRITE mode and subsequently CLOSE 
MP2 Conditional loop until terminator received 
MP3 ‘Attempted’ use of GetData() – Ignore CALL … 
MP4 Fully correct use GetData()to return the data in a loop 
MP5 Maintain CharCount in a loop 
MP6 Write each line to the file - except the terminator in a loop 
MP7 Final output of message giving number of characters written outside loop
### Max 3 marks

**Problem:**

- If the file being sent contains a line equal to `"****"`
- Then the file written by `ReceiveFile()` will stop at that line and any subsequent lines will be lost.

**Solution:**

- Read the file at the sending end to count how many lines it contains.
- Send an initial message containing the number of lines to be transmitted.

**Alternative Solution:**

- The transmitter chooses a different terminator string/character that does *not* occur anywhere in the file.
- The transmitter sends this unique terminator *before* sending the first line of the file / before the transfer begins.

### Q13
> **[mark-scheme]**
> Example Solution
> 
> `PROCEDURE CreateFiles(NameRoot : STRING, NumFiles : INTEGER)`
> 
> `    DECLARE FileName, Suffix : STRING`
> 
> `    DECLARE Count : INTEGER`
> 
> `    FOR Count  1 TO NumFiles`
> 
> `        Suffix  NUM_TO_STR(Count)`
> 
> `        WHILE LENGTH(Suffix) <> 3`
> 
> `            Suffix  '0' & Suffix`
> 
> `        ENDWHILE`
> 
> `        FileName  NameRoot & '.' & Suffix`
> 
> `        OPENFILE FileName FOR WRITE`
> 
> `        WRITEFILE FileName, "This is File " & FileName`
> 
> `        CLOSEFILE FileName`
> 
> `    NEXT Count`
> 
> `ENDPROCEDURE`
> 
> **Mark as follows:**
> 
> 1. Procedure heading, including parameters, and ending
> 2. Loop for `NumFiles `iterations
> 3. Attempt to create **filename suffix** using NUM_TO_STR() **in a loop**
> 4. Completely correct filename
> 5. `OPENFILE `in `WRITE `mode and subsequent `CLOSE `**in a loop**
> 6. `WRITE `initial first line to the file** in a loop**
> **[mark-scheme]**
> Read

### Q14
Example:

`PROCEDURE FindModules(FileName : STRING)`

` DECLARE Line : STRING`

` DECLARE Index, LineNum : INTEGER`

` OPENFILE FileName FOR READ`

` Index  1`

` LineNum  0`

` WHILE NOT EOF(FileName)`

`  READFILE FileName, Line`

`  LineNum  LineNum + 1`

`  Line  Header(Line)`

`  IF Line <> "" THEN`

`   ModInfo[Index, 1]  NUM_TO_STR(LineNum)`

`   ModInfo[Index, 2]  LEFT(Line, 1)`

`   ModInfo[Index, 3]  RIGHT(Line, LENGTH(Line) - 1)`

`   Index  Index + 1`

`  ENDIF`

` ENDWHILE`

` CLOSEFILE FileName`

`ENDPROCEDURE`

Mark as follows:

1 Open file in `READ `mode **and **subsequently close

2 Loop to `EOF(FileName)`

3 Read a line from the file and maintain LineNum **in a loop**

4 Call `Header()` and use return value** in a loop**

5 Test return value for "" **in a loop**

6 Attempt at all three-array assignment for all columns in correct row

7 Correct values assigned to all columns of array

8 Maintain correct array row index

### Q15
One mark per point:

1. Open the file (in read mode and subsequently close)

2. Initialise an index variable (to 1 // 0)

3. Repeat (the next three steps) until the end of file is reached

4. Read a line from the file (into a string variable)

5. Store the line / variable in the array at the index

6. Increment the index** in a loop**

**Note: max 5 marks**

### Q16
Example:

`PROCEDURE Stage_2(F1, F2 : STRING)`

` DECLARE Line : STRING`

` DECLARE Count : INTEGER`

` Count `$\leftarrow$` 0`

` OPEN F1 FOR READ`

` OPEN F2 FOR APPEND`

` WHILE NOT EOF(F1)`

`  READFILE F1, Line`

`  Line `$\leftarrow$` DeleteSpaces(Line)`

`  Line `$\leftarrow$` DeleteComment(Line)`

`  IF Line <> "" THEN`

`   WRITEFILE F2, Line // skip blank lines`

`  ELSE`

`   Count `$\leftarrow$` Count + 1`

`  ENDIF`

` ENDWHILE`

` CLOSEFILE F1`

` CLOSEFILE F2`

` OUTPUT Count, " blank lines were removed"`

`ENDPROCEDURE`

Mark as follows:

1 Procedure heading, parameters, ending

2 Open both files in correct modes and subsequently close

3 Loop to `EOF(F1)`

4 Read a line from F1** in a loop**

5 Assign return values from `DeleteComment() `and `DeleteSpaces() `**in a loop**

6 Check return value following both MP5 function calls is not an empty string and if so write to F2 **in a loop**

7 Count the blank lines** in a loop**

8 Output number of blank lines removed following a reasonable attempt after the loop

### Q17
Example:

`FUNCTION Stage_1(StudentName : STRING) RETURNS INTEGER`

` DECLARE OldFile, NewFile, Line : STRING`

` DECLARE Count : INTEGER`

` OldFile `$\leftarrow$`StudentName & "_src.txt"`

` NewFile `$\leftarrow$` StudentName & "_S1.txt"`

` OPENFILE OldFile FOR READ`

` OPENFILE NewFile FOR WRITE`

` Count `$\leftarrow$` 0`

` WHILE NOT EOF(OldFile)`

`  READFILE OldFile, Line`

`  Line `$\leftarrow$` DeleteComment(Line)`

`  IF LENGTH(Line) <> 0 THEN`

`   WRITEFILE NewFile, Line`

`   Count `$\leftarrow$` Count + 1`

`  ENDIF`

` ENDWHILE`

` CLOSEFILE OldFile`

` CLOSEFILE NewFile`

` RETURN Count`

`ENDFUNCTION`

Mark as follows:

1 Generate filenames condone missing “_”

2 Open both files in correct modes **and **subsequently close

3 Loop to `EOF(OldFile)`

4 Read a line from `OldFile `**and **execute DeleteComment() in a loop

5 Skip blank lines after `DeleteComment()`** in a loop**

6 Write `Line `to stage 1 file **and **increment Count

7 Return the number of lines after a reasonable attempt at counting

### Q18
Example solution:

`PROCEDURE Restore()`

` DECLARE Index : INTEGER`

` DECLARE Line : STRING`

` OPENFILE "SaveFile.txt" FOR READ`

` FOR Index`$\leftarrow$` 1 TO 45`

`  READFILE "SaveFile.txt", Line`

`  Character[Index].Player `$\leftarrow$` STR_TO_NUM(Extract(Line, 1))`

`  Character[Index].Role `$\leftarrow$` Extract(Line, 2)`

`  Character[Index].Name`$\leftarrow$` Extract(Line, 3)`

`  Character[Index].Skill `$\leftarrow$` STR_TO_NUM(Extract(Line, 4))`

` NEXT Index`

` CLOSEFILE "SaveFile.txt"`

`ENDPROCEDURE`

Mark as follows:

**MP1** Open the file in read mode and subsequently close

**MP2** Loop through 45 elements

**MP3** Read a line from the file in a loop

**MP4** Attempt to use Extract() in a loop

**MP5** Correct use of Extract() for all fields in a loop

**MP6** Use of STR_TO_NUM() on Player and Skill in a loop

**MP7** Completely correct extraction and assignment of all fields in a loop
**MP1** The `Character `array / character data can be saved before the program is closed

**MP2** Allowing the **game to continue** using the same data / from the point it was saved

### Q19
Example solution:

`PROCEDURE Save()`

` DECLARE Index : INTEGER`

` DECLARE Line : STRING`

` CONSTANT SEP = '^'`

` OPENFILE "SaveFile.txt" FOR WRITE`

` FOR Index `$\leftarrow$` 1 TO 45`

`  Line `$\leftarrow$` NUM_TO_STR(Character[Index].Player) & SEP`

`  Line `$\leftarrow$` Line & Character[Index].Role & SEP`

`  Line `$\leftarrow$` Line & Character[Index].Name & SEP`

`  Line `$\leftarrow$` Line & NUM_TO_STR(Character[Index].Level)`

`  WRITEFILE "SaveFile.txt", Line`

` NEXT Index`

` CLOSEFILE "SaveFile.txt"`

`ENDPROCEDURE`

Mark as follows:

**MP1** Declaration of local integer for Index (and string type for Line)

**MP2** Open "SaveFile.txt" in write mode and subsequently close

**MP3** Loop through 45 elements

**MP4** Attempt to form Line - four fields in a loop

**MP5** Correct use of NUM_TO_STR()x2 (Player and Level) in a loop

**MP6 **Correct use of three &<separator>& strings in a loop

**MP7** Line from MP4 written to file in a loop
**MP1 **Encode Status as a character / string **MP2** Append the ‘^’ separator and the character/string

### Q20
> **[mark-scheme]**
> The file will need to be opened in <u>APPEND </u>mode

### Q21
> **[mark-scheme]**
> `PROCEDURE SendFile(FileName, DestID : STRING, Port : INTEGER) `
> 
> `        DECLARE FileData : STRING `
> 
> `        CONSTANT STX = CHR(02) `
> `        CONSTANT ETX = CHR(03) `
> 
> `        OPENFILE FileName FOR READ `
> 
> `        WHILE NOT EOF(FileName) `
> `                 READFILE FileName, FileData `
> `                 FileData `$\leftarrow$`STX & DestID & MyID & FileData & ETX `
> `                 CALL Transmit(FileData, Port) `
> `      ENDWHILE `
> 
> `      CLOSEFILE FileName `
> 
> `      CALL Transmit(STX &  DestID & MyID & "****" & ETX, Port) `
> 
> `ENDPROCEDURE`
> 
> Mark as follows:
> 
> - **MP1**   OPEN file in READ mode – using parameter - and subsequently CLOSE
> - **MP2**   Conditional loop to EOF()
> - **MP3**   Use of READFILE to get a line from the file
> - **MP4**   ‘Attempt’ to form a message (minimum is DestID, MyID, FileData)
> - **MP5**   Message formed is completely correct
> - **MP6**   Call Transmit() with correct MP4 string **in a loop **
> - **MP7**   Transmit the "****" message (all parts present) **after the loop**
> **[mark-scheme]**
> **Max 2 **marks
> 
> - **MP1**   Indicates that all the lines of the file have been sent // it is the end of the transmission / file transfer
> - **MP2**   So that the receiving program can stop waiting for further data
> - **MP3**   The file can be closed / saved
