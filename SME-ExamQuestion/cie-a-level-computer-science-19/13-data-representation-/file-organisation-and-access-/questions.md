# Exam Questions — File Organisation & Access
**13. Data Representation** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 16 questions across 1 sets


## Exam Questions (16 questions)


### Q1 — hard — 5 marks

**Q1** [5 marks]

A random access file stores account records. Each record has a record key, which is a four-digit number.

The main area of the file has seven storage locations, with the addresses 0 to 6. The file also has a separate overflow area.

The hashing algorithm calculates the hash value as the record key modulus 7. The function modulus gives the remainder after integer division.

When a record is added and the address given by its hash value is already in use, the record is stored in the first free location in the overflow area.

The current contents of the main area are shown.

| Address | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Record key | 4802 | 3025 | 2571 | 8410 | 1236 | 1874 | 6089 |

The overflow area currently holds one record, with the record key 7318.

(i) A new record with the record key 9260 is added to the file.

Explain where this record is stored.

(2)

(ii) The program then searches the file for the record with the record key 7318.

Explain how this record is found.

(3)

### Q2 — medium — 4 marks

**Q2** [4 marks]

A random access file stores product records. Each record has a record key, which is a four-digit number.

The main area of the file has five storage locations, with the addresses 0, 1, 2, 3 and 4.

The hashing algorithm has two steps:

1. add together the four digits of the record key
2. the hash value is the answer to step 1 modulus 5

The function modulus gives the remainder after integer division.

If the address given by the hash value is already in use, the record is stored at the next free address after it.

The main area is empty. Four records are then added, in the order shown in the table.

The first row has been completed for you. The digits of 3142 add up to 10, and 10 modulus 5 = 0, so that record is stored at address 0.

Complete the table to show the hash value and the storage address for each of the remaining three records.

| Record key | Hash value | Address where the record is stored |
|---|---|---|
| 3142 | 0 | 0 |
| 2081 |   |   |
| 5230 |   |   |
| 4207 |   |   |

### Q3 — easy — 2 marks

**Q3** [2 marks]

A random access file stores customer records. Each record has a record key, which is a four-digit number.

A hashing algorithm is used to calculate the storage location of each record. It calculates hash values by using the function modulus 7.

The function modulus gives the remainder after integer division.

For example, 4021 modulus 7 = 3. Therefore, the record key 4021 gives a hash value of 3.

Complete the table to show the remaining hash values.

| Record key | Hash value |
|---|---|
| 4021 | 3 |
| 5009 |   |
| 6134 |   |

### Q4 — hard — 4 marks

**Q4** [4 marks]

A sequential file holds eight employee records. The records are ordered on the key field `EmployeeID`.

The `EmployeeID` values, in the order in which the records appear in the file, are:

104, 118, 127, 133, 141, 156, 160, 172

Sequential access is used to search this file.

(i) State the number of records that are read when the record with `EmployeeID` 133 is searched for.

(1)

(ii) A search is made for `EmployeeID` 147. There is no record with this value in the file.

State the number of records that are read, and explain why the search does not have to read every record in the file.

(3)

### Q5 — medium — 3 marks

**Q5** [3 marks]

An online store keeps a file of 400 000 customer records. The file uses random organisation. Each customer has a unique customer number, which is the key field of the record.

When a customer signs in, the store must display that customer's record without delay.

Explain why direct access, rather than sequential access, is the appropriate method of file access for this file.

### Q6 — easy — 2 marks

**Q6** [2 marks]

A company stores its data records in files. Different files on the company's system use different methods of file organisation.

Complete the table by writing the method of file access that can be used with each method of file organisation.

| Method of file organisation | Method of file access |
|---|---|
| Serial |   |
| Random |   |

### Q7 — hard — 4 marks

**Q7** [4 marks]

An online ticket agency stores one record for each booking. Each record has a unique booking reference, which is the key field. The records are currently held in a file that uses sequential file organisation.

The agency is changing its system. Customers will be able to amend their own bookings at any time of day, so amendments will be made continuously.

Explain why sequential file organisation is no longer suitable for this file, and describe how the records would be held in a file that uses random file organisation.

### Q8 — medium — 3 marks

**Q8** [3 marks]

A national library keeps one record for each book it holds. Each record has a unique catalogue number, which is the key field.

New books are added to the collection once a month, in a single batch.

Every week the library produces a printed list of all the books it holds, in catalogue-number order.

Identify the most appropriate method of file organisation for this file and explain your choice.

### Q9 — easy — 2 marks

**Q9** [2 marks]

A programmer is deciding how to store data records in a file.

Complete the table by describing how the records are placed in the file for each method of file organisation.

| Method of file organisation | How the records are placed in the file |
|---|---|
| Sequential |   |
| Random |   |

### Q10 — medium — 5 marks

**Q10** [2 marks]

The location of a record in a random file is determined using a hashing algorithm. A collision may occur during the process of adding a record.

Outline what is meant by the term **collision** in this context.

*Source: Nov 2023 9618/32 Q3A*


**Q10** [3 marks]

Explain how a collision can be dealt with when writing records to a random file.

*Source: Nov 2023 9618/32 Q3B*


### Q11 — medium — 6 marks

**Q11** [4 marks]

Describe sequential and random methods of file organisation.

*Source: Nov 2023 9618/31 Q4A*


**Q11** [2 marks]

Outline the process of sequential access for serial and sequential files.

*Source: Nov 2023 9618/31 Q4B*


### Q12 — medium — 6 marks

**Q12** [2 marks]

Outline what is meant by **direct access** as a method of file access.

*Source: June 2024 9618/32 Q7A*


**Q12** [4 marks]

Explain how direct access is used to locate a specific record in sequential files and random files.

(i) Sequential files

(2)

(ii) Random files

(2)

*Source: June 2024 9618/32 Q7B*


### Q13 — medium — 5 marks

**Q13** [2 marks]

Describe the sequential method of file access.

*Source: June 2024 9618/31 Q4A*


**Q13** [3 marks]

Explain how the sequential method of file access is applied to files with serial organisation and to files with sequential organisation.

*Source: June 2024 9618/31 Q4B*


### Q14 — medium — 3 marks

**Q14** [2 marks]

Describe **serial file organisation** as a method of storing data records in a file.

*Source: Nov 2024 9618/32 Q2A*


**Q14** [1 mark]

State **one **example of a use for serial file organisation.

*Source: Nov 2024 9618/32 Q2B*


### Q15 — medium — 5 marks

**Q15** [3 marks]

Explain what is meant by a hashing algorithm in the context of file access.

*Source: Nov 2024 9618/31 Q5A*


**Q15** [2 marks]

The use of a hashing algorithm can result in the same storage location being identified for more than one record.

Outline **two **methods of overcoming this issue.

*Source: Nov 2024 9618/31 Q5B*


### Q16 — medium — 2 marks

**Q16** [2 marks]

A program is being developed to implement a game for up to six players.

During the game, each player assembles a team of characters. At the start of the game there are 45 characters available.

Each character has four attributes, as follows:

| **Attribute** | Examples | Comment |
|---|---|---|
| **Player** | 0, 1, 3 | The player the character is assigned to. |
| **Role** | Builder, Teacher, Doctor | The job that the character will perform in the game. |
| **Name** | Bill, Lee, Farah, Mo | The name of the character. Several characters may perform the same role, but they will each have a unique name. |
| **Level** | 14, 23, 76 | The skill level of the character. An integer in the range 0 to 100 inclusive. |

The programmer has defined a record type to define each character.

The record type definition is shown in pseudocode as follows:

`TYPE CharacterType`
`       DECLARE Player : INTEGER `
`       DECLARE Role : STRING`
`       DECLARE Name : STRING `
`       DECLARE Level : INTEGER `
`ENDTYPE`

The `Player `field indicates the player to which the character is assigned (1 to 6). The field value is 0 if the character is **not **assigned to any player.

The programmer has defined a global array to store the character data as follows:

`DECLARE Character : ARRAY[1:45] OF CharacterType`

At the start of the game all record fields are initialised, and all `Player` field values are set to 0

The programmer has defined a program module as follows:

| **Module** | **Description** |
|---|---|
| `Assign()` | - called with two parameters:<br><br>  - an integer representing a player<br>  - a string representing a character role<br>- search the `Character` array for an unassigned character with the required role<br>- If found, assign the character to the given player and output a confirmation message, for example:  `"Bill the Builder has been assigned to player 3"`<br>- If no unassigned character with the required role is found, output a suitable message. |

The save operation is to be extended so that multiple files may be saved as the game progresses. This will allow the user to restore the game from any saved position. The filename must reflect the sequence in which the files are saved.

Describe a method that would allow multiple files to be saved **and **give an example of **two** consecutive filenames.

*Source: Nov 2024 9618/22 Q8D*

