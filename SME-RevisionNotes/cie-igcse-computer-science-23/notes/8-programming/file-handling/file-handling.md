---
note_id: "rn_TjX4sdSgSJB3dgS3"
title: "File Handling"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/8-programming/file-handling/file-handling
path: 8-programming/file-handling/file-handling
updated_at: "2026-06-11T12:26:20.601Z"
spec_point_ids: ["spcpt_g6bDb6MVnB3Kz5vT"]
spec_point_codes: []
guided_study: true
---

# File Handling

## File Handling

> **Spec point** — `spcpt_g6bDb6MVnB3Kz5vT` · "1 Understand the purpose of storing data in a file
to be used by a program
2 Open, close and use a file for reading and writing"

## File Handling

### What is file handling?

- File handling is **the use of programming techniques** to work with information stored in **text files**
- Examples of file handing techniques are:

  - **opening **text files
  - **reading **text files
  - **writing **text files
  - **closing **text files

| **Concept** | **OCR exam reference** | **Python** |
|---|---|---|
| **Open** | `OPENFILE "fruit.txt" FOR READ` | `file = open("fruit.txt","r")` |
| **Close** | `CLOSEFILE "fruit.txt"` | `file.close()` |
| **Read line** | `READFILE "fruit.txt", LineOfText` | `file.readline()` |
| **Write line** | `OPENFILE "fruit.txt" FOR WRITE `<br><br>`WRITEFILE "fruit.txt", "Oranges"` | `file = open("fruit.txt","w")`<br><br>`file.write("Oranges")` |
| **Append a file** | `OPENFILE "fruit.txt" FOR APPEND ` | `file = open("fruit.txt","a")` |

#### Pseudocode example (reading data)

| **Employees** | **Text file** |
|---|---|
|   | Greg<br>Sales<br>39000<br>43<br>Lucy<br>Human resources<br>26750<br>28<br>Jordan<br>Payroll<br>45000<br>31 |

#### Python example (reading data)

| **Employees** | **Text file** |
|---|---|
|   | Greg<br>Sales<br>39000<br>43<br>Lucy<br>Human resources<br>26750<br>28<br>Jordan<br>Payroll<br>45000<br>31 |

#### Pseudocode example (writing new data)

| **Employees** | **Text file** |
|---|---|
|   | Greg<br>Sales<br>39000<br>43<br>Lucy<br>Human resources<br>26750<br>28<br>Jordan<br>Payroll<br>45000<br>31<br><br>*Polly*<br>*Sales*<br>*26000*<br>*32* |

#### Python example (writing new data)

| **Employees** | ** Text file** |
|---|---|
|   | Greg<br>Sales<br>39000<br>43<br>Lucy<br>Human resources<br>26750<br>28<br>Jordan<br>Payroll<br>45000<br>31<br>*Polly*<br>*Sales*<br>*26000*<br>*32* |

> **Exam Hint**
> When opening files it is really important to make sure you use the correct letter in the open command
> 
> - "**r**" is for reading from a file only
> - "**w**" is for writing to a new file, if the file does not exist it will be created. If a file with the same name exists the contents will be overwritten
> - "**a**" is for writing to the end of an existing file only
> 
> Always make a backup of text files you are working with, one mistake and you can lose the contents!

> **Worked Example**
> Use pseudocode to write an algorithm that does the following :
> 
> - Inputs the title and year of a book from the user.
> - Permanently stores the book title and year to the existing text file *books.txt ***[4]**
> 
> **How to answer this question**
> 
> - Write two input statements (title and year of book)
> - Open the file
> - Write inputs to file
> - Close the file
> 
> **Final answer:** **Example answer**
> 
> **Guidance**
> 
> |   | **Final answer:** **1 mark** |
> |---|---|
> |   |   |
> |   | **Final answer:** **1 mark** |
> |   | **Final answer:** **1 mark** |
> |   |   |
> |   | **Final answer:** **1 mark** |
