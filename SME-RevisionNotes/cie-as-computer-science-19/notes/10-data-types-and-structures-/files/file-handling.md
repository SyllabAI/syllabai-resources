---
note_id: "rn_vRsrCDTxKxjCf9Rv"
title: "File handling"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/10-data-types-and-structures-/files/file-handling
path: 10-data-types-and-structures-/files/file-handling
updated_at: "2026-10-01T11:20:02.265Z"
spec_point_ids: ["spcpt_t5QxGmPqkFwzJk84"]
spec_point_codes: []
guided_study: false
---

# File handling

## Purpose of files

> **Spec point** — `spcpt_t5QxGmPqkFwzJk84`

## Purpose of files

### What is file handling?

- File handling is **the use of programming techniques** to work with information stored in **text files**
- Examples of file handing techniques are:

  - **opening **text files
  - **reading **text files
  - **writing **text files
  - **closing **text files

| **Concept** | **CIE A Level Pseudocode** |
|---|---|
| **Open file for reading** | `OPENFILE "fruit.txt" FOR READ` |
| **Open file for writing** | `OPENFILE "Shopping.txt" FOR WRITE` |
| **Close file** | `CLOSEFILE "fruit.txt"` |
| **Read line** | `READFILE "fruit.txt", FruitName` |
| **Write line** | `WRITEFILE "fruit.txt", "Oranges"` |
| **Check end of file** | `IF NOT EOF("fruit.txt") THEN` |
| **Create new file** | `OPENFILE "Shopping.txt" FOR WRITE` (same as writing – it overwrites or creates) |
| **Append to file** | `OPENFILE "Shopping.txt" FOR APPEND` |

- An example program written in pseudocode to:

  - **Opens **a text file for reading
  - **Reads **each line (a fruit name)
  - **Counts **how many fruits are in the file
  - **Outputs **the total
  - **Closes **the file

#### Identifier table

| **Identifier** | **Data type** | **Description** |
|---|---|---|
| `FruitName` | STRING | Stores the name of each fruit read from the file |
| `FruitCount` | INTEGER | Keeps track of how many fruits have been read |
| `FruitFile` | STRING | Holds the name of the file being read, "fruit.txt" |

> **Worked Example**
> A program is required to read the contents of a text file `Data.txt` into a 1D array `DataArray`. The file contains 25 integer values, one per line.
> 
> Write pseudocode to:
> 
> - open the file for reading
> - read each value into the array
> - close the file
> 
> **[4]**
> 
> **Final answer:** **Answer**
> 
> - Correct use of `OPENFILE "Data.txt" FOR READ` … **[1 mark]**
> - Loop using `WHILE NOT EOF("Data.txt") … ENDWHILE` or `FOR Counter ← 1 TO 25 … NEXT Counter` **[1 mark]**
> - Correct use of `READFILE "Data.txt", LineData` storing into array with index `DataArray[Counter] ← LineData` … **[1 mark]**
> - Correct use of `READFILE "Data.txt", LineData` storing into the array with `DataArray[Counter] ← STR_TO_NUM(LineData)` **[1 mark]**
> 
> Model answer:
