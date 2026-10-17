# Exam Questions — File Processing & Exception Handling
**20. Further Programming** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 21 questions across 1 sets


## Exam Questions (21 questions)


### Q1 — very_hard — 6 marks

**Q1** [6 marks]

A shop stores data about its stock in the random file `Stock.dat`. The file holds exactly 500 records, at positions 1 to 500. Each record uses this user-defined data type.

A procedure `Restock()` is needed. The procedure:

- takes one parameter of type integer, `Amount`
- checks every record in the file
- for each item whose quantity is less than its reorder level, adds `Amount` to the quantity and writes the updated record back to the same position in the file
- outputs the number of records that were updated, after all the records have been checked.

Write pseudocode for the procedure `Restock()`.

### Q2 — medium — 4 marks

**Q2** [4 marks]

A sports centre has 60 lockers. The random file `Lockers.dat` stores one record for each locker. The record for locker number 1 is at position 1, the record for locker number 2 is at position 2, and so on.

Each record uses this user-defined data type.

This pseudocode algorithm assigns a locker to a member. It reads the record for the locker, changes it, and writes it back to the same position in the file.

Complete the file handling pseudocode.

### Q3 — easy — 2 marks

**Q3** [2 marks]

A club stores data about its members in the random file `Members.dat`. Each record uses the user-defined data type `TMember`.

The file has already been opened in `RANDOM` mode. The variable `ThisMember` has been declared as type `TMember`.

Write **two** pseudocode statements to read the record at position 12 of the file into `ThisMember`.

### Q4 — hard — 4 marks

**Q4** [4 marks]

The random file `Products.dat` stores one record at each position. Each record uses the user-defined data type `TProduct`. Only the `ProductCode` field is shown in the table.

Positions 1 to 5 hold records and position 6 is empty. The variable `NewItem` already holds a complete record with the `ProductCode` "P999".

A programmer wants to move the records at positions 2 to 5 up by one position each, and then insert `NewItem` at position 2. The programmer writes this pseudocode.

Complete the table to show the `ProductCode` at each position after the pseudocode has run. Then explain why the pseudocode does not do what the programmer intended, and state the change needed to the `FOR` statement.

| Position | ProductCode before | ProductCode after |
|---|---|---|
| 1 | A101 |   |
| 2 | B202 |   |
| 3 | C303 |   |
| 4 | D404 |   |
| 5 | E505 |   |
| 6 | (empty) |   |

### Q5 — medium — 3 marks

**Q5** [3 marks]

A hotel stores one record for each room in the random file `Rooms.dat`. Each record uses the user-defined data type `TRoom`.

This pseudocode changes the status of one room.

Describe the purpose of each of these commands in the pseudocode:

- `SEEK`
- `GETRECORD`
- `PUTRECORD`

### Q6 — easy — 2 marks

**Q6** [2 marks]

A program uses four different files. For each task, complete the table by writing the file mode that the `OPENFILE` statement must use.

| Task | File mode |
|---|---|
| Add a new line of text to the end of an existing log file, keeping the lines already in it |   |
| Go directly to record 250 in a file of fixed-length records and replace that record |   |
| Output every line of a text file of product names, in order |   |
| Create a new text file to hold today's results, replacing any file with the same name |   |

### Q7 — hard — 6 marks

**Q7** [6 marks]

A program uses this pseudocode to find the average of some readings entered by a user. Line numbers are shown on the left.

Identify **three** different line numbers where an exception could occur when this pseudocode is run.

For each line, describe an event that would cause the exception.

### Q8 — medium — 3 marks

**Q8** [3 marks]

A weather station program runs every hour. It reads the temperature readings stored in a text file on a separate storage device. It calculates the mean of the readings and displays the result on a screen in a public building.

Explain why exception handling should be used in this program.

### Q9 — easy — 2 marks

**Q9** [2 marks]

A program asks the user to input two whole numbers. It then divides the first number by the second number and outputs the result.

Identify **two** different exceptions that could be caused by the data the user inputs while this program is running.

### Q10 — medium — 9 marks

**Q10** [2 marks]

Describe, with an example, what is meant by an **exception**.

*Source: Nov 2023 9618/32 Q12A*


**Q10** [7 marks]

A pseudocode algorithm searches for a customer record in a random file `AccountRecord.dat`. A user inputs the name of the customer.

The records are stored using the user‑defined data type `TAccount`.

`TYPE TAccount`

`    DECLARE AccountNumber : INTEGER`

`    DECLARE Name : STRING`

`    DECLARE Address : STRING`

`    DECLARE Telephone : STRING`

`ENDTYPE`

If the record is found, it is output, otherwise an error message is displayed.

Complete the file handling pseudocode.

`DECLARE Customer : TAccount`

`DECLARE Location : INTEGER`

`DECLARE MaxSize : INTEGER`

`DECLARE FoundFlag : BOOLEAN`

`DECLARE SearchCustomer : STRING`

`MaxSize `$\leftarrow$`1000`

`OPENFILE ...............................................................................................................`

`Location `$\leftarrow$ `1`

`............................................................................................................... `$\leftarrow$ `FALSE`

`OUTPUT "Enter the customer’s name"`

`...............................................................................................................`

`................................................................................... AND Location <= MaxSize`

`................................... "AccountRecord.dat", ............................................`

`GETRECORD "AccountRecord.dat", Customer`

`IF SearchCustomer = Customer.Name THEN`

`    OUTPUT "Customer found: "`

`    OUTPUT Customer // output customer record`

`    FoundFlag `$\leftarrow$ `TRUE`

`ENDIF`

`Location `$\leftarrow$` Location + 1`

`ENDWHILE`

`IF NOT FoundFlag THEN`

`    OUTPUT ".........................................................................................................."`

`ENDIF`

*Source: Nov 2023 9618/32 Q12B*


### Q11 — medium — 8 marks

**Q11** [5 marks]

A pseudocode algorithm finds a customer account record in a random file and outputs it. The records are stored using the user-defined data type `TAccount`.

`TYPE TAccount`

`    DECLARE AccountNumber   : INTEGER`

`    DECLARE LastName        : STRING`

`    DECLARE FirstName       : STRING`

`    DECLARE Address         : STRING`

`    DECLARE ContactNumber   : STRING`

`ENDTYPE`

Complete the file handling pseudocode.

The function `Hash() `takes the customer account number as a parameter, calculates and returns the hash value.

`DECLARE Customer : TAccount`

`DECLARE Location : INTEGER`

`DECLARE AccountFile : STRING`

`.................................................................................................. `$\leftarrow$`"AccountRecords.dat"`

`............................................................... AccountFile ..........................................................`

`OUTPUT "Please enter an account number"`

`INPUT Customer.AccountNumber`

`Location `$\leftarrow$` Hash( .............................................................................................................. )`

`SEEK ..................................................................................................................... , Location`

`............................................................. AccountFile, ..........................................................`

`OUTPUT Customer  // output customer record`

`CLOSEFILE AccountFile`

*Source: Nov 2023 9618/31 Q8A*


**Q11** [1 mark]

Define the term **exception handling**.

*Source: Nov 2023 9618/31 Q8B*


**Q11** [2 marks]

State **two **possible causes of an exception.

*Source: Nov 2023 9618/31 Q8C*


### Q12 — medium — 10 marks

**Q12** [7 marks]

A class of students are developing a program to send data between computers. Many computers are connected together to form a wired network. Serial ports are used to connect one computer to another.

Each computer:

- is assigned a unique three-digit ID
- has three ports, each identified by an integer value
- is connected to between one and three other computers.

Messages are sent between computers as a string of characters organised into fields as shown:

<STX><DestinationID><SourceID><Data><ETX>

| Field name | Description |
|---|---|
| STX | a single character marking the start of the message (ASCII value 02) |
| DestinationID | three numeric characters identifying the destination computer |
| SourceID | three numeric characters identifying the source computer |
| Data | a variable length string containing the data being sent (Minimum length is 1 character) |
| ETX | a single character marking the end of the message (ASCII value 03) |

For example, the following message contains the data "Hello Jack" being sent from computer "202" to computer "454":

`<STX> "454202Hello Jack" <ETX>`

Each computer will run a copy of the same program. Each program will contain a global variable MyID of type string which contains the unique ID of the computer in which the program is running.

The first two program modules are defined as follows:

| Module | Description |
|---|---|
| `GetData()` (already written) | - returns the data field from a message that has been received<br>- If no message is available, the module waits until one has been received. |
| `ReceiveFile()` | - takes a file name as a parameter of type string<br>- creates a text file with the given file name (no checking required)<br>- writes the data field returned by GetData() to the file<br>- repeats until the data field is "****", which is not written to the file<br>- outputs a final message giving the total number of characters written to the file, for example: `132456 characters were written to newfile.txt` |

Write pseudocode for module `ReceiveFile()`.

Module GetData() has already been written and must be used.

*Source: Nov 2023 9618/23 Q8A*


**Q12** [3 marks]

The use of the string "****" as explained in the module description for ReceiveFile() may cause a problem.

Explain the problem and suggest a solution.

Problem .....................................................

Solution ........................................................

*Source: Nov 2023 9618/23 Q8B*


### Q13 — medium — 7 marks

**Q13** [6 marks]

A procedure CreateFiles() will take two parameters:

- a string representing a file name
- an integer representing the number of files to be created.

The procedure will create the number of text files specified.

Each file is given a different name. Each file name is formed by concatenating the file name with a suffix based on the file number. The suffix is always three characters.

For example, the call `CreateFiles("TestData", 3)` would result in the creation of the three files, TestData.001, TestData.002 and TestData.003.

Each file will contain a single line. For example, file TestData.002 would contain the string:

`This is File TestData.002 `

Write pseudocode for `CreateFiles()`.

Assume both parameters are valid and that the integer value is between 1 and 999, inclusive.

*Source: Nov 2023 9618/22 Q6A*


**Q13** [1 mark]

A module CheckFiles() will count the number of files produced by CreateFiles() in part (a).

CheckFiles() will take a string representing a file name and return the number of files found.

State the file mode that should be used in `CheckFiles()`.

*Source: Nov 2023 9618/23 Q8B*


### Q14 — medium — 8 marks

**Q14** [8 marks]

A new module is required:

| Module | Description |
|---|---|
| FindModules() | - called with a parameter of type string representing a student project file name<br>- uses module Header() to check each line of the project<br>- assigns values to the ModInfo array for each module declaration in the student project |

As a reminder, the previous example of part of the array is repeated below:

|   | x = 1 | x = 2 | x = 3 |
|---|---|---|---|
| ModInfo[10, x] | "27" | "P" | "MyProc(Z : CHAR)" |
| ModInfo[11, x] | "35" | "F" | "MyFun(Y : CHAR) RETURNS BOOLEAN" |

Write pseudocode for module `FindModules()`.

Assume that the array contains enough rows for the number of modules in each project.

*Source: June 2024 9618/23 Q8B*


### Q15 — medium — 5 marks

**Q15** [5 marks]

A program uses a global 1D array of type string and a text file.

An algorithm that forms part of the program is expressed as follows:

- copy the first line from the file into the first element of the array
- copy the second line from the file into the second element of the array
- continue until all lines in the file have been copied into the array

Stepwise refinement is applied to the algorithm.

Outline **five **steps for this algorithm that could be used to produce pseudocode.

Assume there are more elements in the array than lines in the file.

Do **not **use pseudocode statements in your answer.

Step 1 ...............................................

Step 2 ...........................................

Step 3 ............................................

Step 4 ................................................

Step 5 ................................................

*Source: June 2024 9618/23 Q2A*


### Q16 — medium — 8 marks

**Q16** [8 marks]

Two modules are defined:

| Module | Description |
|---|---|
| `DeleteComment() `(already written) | - called with a parameter of type string representing a line of pseudocode from a student’s project file<br>- returns the line after removing any comment |
| `Stage_2()` | - called with two parameters:<br><br>  - a string representing an input file name<br>  - a string representing an output file name<br>- copies each line from the input file to the existing output file having first removed all leading spaces and comments from that line<br>- does not write blank lines to the output file<br>- outputs a final message giving the number of blank lines removed |

Write pseudocode for module `Stage_2()`. Modules `DeleteComment()` and `DeleteSpaces()` must be used in your solution.

*Source: June 2024 9618/22 Q8C*


### Q17 — medium — 7 marks

**Q17** [7 marks]

A second module is defined:

| Module | Description |
|---|---|
| `Stage_1()` | - called with a parameter of type string representing a student name<br>- creates a new stage 1 file<br>- copies each line from the student’s project file to the stage 1 file after removing any comment from each line<br>- does not write blank lines to the stage 1 file<br>- returns the number of lines written to the stage 1 file |
|   |   |

Write pseudocode for module `Stage_1()`.

Module `DeleteComment()` must be used in your solution

*Source: June 2024 9618/21 Q8B*


### Q18 — medium — 9 marks

**Q18** [7 marks]

The Character array data has been saved in the text file SaveFile.txt Each line of the file contains one element of the array (one record).

New modules are defined:

| Module | Description |
|---|---|
| `Extract()` (already written) | - called with two parameters:<br><br>  - a string representing a complete line from the text file<br>  - an integer representing a field number (see structure below)<br>  - returns a string representing the required field |
| `Restore()` | - opens the text file SaveFile.txt<br>- reads lines from the file and assigns values to each record in the Character array using data from each line of the file |

As a reminder, the record structure is repeated here:

`TYPE CharacterType`

` DECLARE Player : INTEGER //Field number 1`

` DECLARE Role : STRING //Field number 2`

` DECLARE Name : STRING //Field number 3`

` DECLARE SkillLevel : INTEGER //Field number 4`

`ENDTYPE`

Write pseudocode for module `Restore()`.

You must use the module `Extract()`.

*Source: Nov 2024 9618/23 Q8B*


**Q18** [2 marks]

The game can last for several days and users often find that they have to close and rerun the game program many times in order to complete it.

Describe the benefit of using the file `SaveFile.txt` as described above.

*Source: Nov 2024 9618/23 Q8C*


### Q19 — medium — 9 marks

**Q19** [7 marks]

A program is being developed to implement a game for up to six players.

During the game, each player assembles a team of characters. At the start of the game there are 45 characters available.

Each character has four attributes, as follows:

| Attribute | Examples | Comment |
|---|---|---|
| Player | 0, 1, 3 | The player the character is assigned to. |
| Role | Builder, Teacher, Doctor | The job that the character will perform in the game. |
| Name | Bill, Lee, Farah, Mo | The name of the character. Several characters may perform the same role, but they will each have a unique name. |
| Level | 14, 23, 76 | The skill level of the character. An integer in the range 0 to 100 inclusive. |

The programmer has defined a record type to define each character.

A new module will store the contents of the Character array in a text file.

The module is defined as follows:

| Module | Description |
|---|---|
| `Save()` | - form a string from each record with fields separated by the character '^'<br>- write each string to a separate line of the new file named SaveFile.txt |

Complete the pseudocode for module `Save()`.

`PROCEDURE Save()`

*Source: Nov 2024 9618/22 Q8B*


**Q19** [2 marks]

The program is changed and the record type definition is modified as follows:

`TYPE CharacterType`

` DECLARE Player : INTEGER`

` DECLARE Role : STRING`

` DECLARE Name : STRING`

` DECLARE Level : INTEGER`

` DECLARE Status : BOOLEAN`

`ENDTYPE`

Describe how the additional Boolean field may be stored with the rest of the fields on one line of a text file.

*Source: Nov 2024 9618/22 Q8C*


### Q20 — medium — 1 marks

**Q20** [1 mark]

| Module | Description |
|---|---|
| `CheckAll()` | - called with a parameter of type integer representing the number of candidate marks in the `Result `array<br>- uses `CheckMark()` to check each candidate mark<br>- for each paper that needs to be checked, write the corresponding candidate ID on a separate line in a new file named `GRList.txt `<br>- outputs a message with a count of how many papers need to be checked |
|   |   |

The requirement changes. Instead of a new file, the module described above needs to add the corresponding candidate ID for each paper that needs to be checked to an existing file.

Explain the change that will need to be made to `CheckAll().`

*Source: Nov 2024 9618/21 Q8C*


### Q21 — medium — 9 marks

**Q21** [7 marks]

A class of students are developing a program to send data between computers. Many computers are connected together to form a wired network. Serial ports are used to connect one computer to another.

Each computer:

• is assigned a unique three-digit ID 
• has three ports, each identified by an integer value 
• is connected to between one and three other computers.

Messages are sent between computers as a string of characters organised into fields as shown:

`<STX><DestinationID><SourceID><Data><ETX>`

| **Field number** | **Field name** | **Description** |
|---|---|---|
| n/a | `STX` | a single character marking the start of the message (ASCII value 02 |
| 1 | `DestinationID` | three numeric characters that identify the destination computer |
| 2 | `SourceID ` | three numeric characters that identify the source computer |
| 3 | `Data` | a variable length string containing the data being sent (Minimum length is 1 character) |
| n/a | `ETX` | a single character marking the end of the message (ASCII value 03 |

For example, the following message contains the data "Hello Kevin" being sent from computer "101" to computer "232":

`<STX>"232101Hello Kevin"<ETX> `

Each computer will run a copy of the same program. Each program will contain a global variable, `MyID` of type string, that contains the unique ID of the computer in which the program is running.

The programmer has defined the first two program modules as follows:

| **Module** | **Description** |
|---|---|
| `Transmit()` (already written) | • takes two parameters:<br><br>o a string containing a message <br>        o an integer containing a port number<br><br>• transmits the message using the given port |
| `SendFile()` | • takes three parameters: <br>         o a string containing a text file name <br>         o a string containing a Destination ID <br>         o an integer containing a Port number <br>• transmits the file one line at a time <br>• transmits a final message with data string "****" |

Write pseudocode for module `SendFile(). `

Assume:

- module `Transmit() `has already been written and is used to transmit a message
- the value of `MyID` may be used as `SourceID `
- the file specified contains no blank lines
- e file specified does not contain the line "****"

*Source: November 2023 9618/21 Q8A*


**Q21** [2 marks]

Module `SendFile()` is used to copy a file from one computer to another.

A module within the program running on the destination computer will receive the data and write it to a new file.

Explain why module `SendFile() `transmits the message with data string "****" after the last line of the file.

*Source: November 2023 9618/21 Q8B*

