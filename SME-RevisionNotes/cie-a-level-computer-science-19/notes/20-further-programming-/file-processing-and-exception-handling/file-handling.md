---
note_id: "rn_gYWVW6pg6pGDpnN7"
title: "File Handling"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/20-further-programming-/file-processing-and-exception-handling/file-handling
path: 20-further-programming-/file-processing-and-exception-handling/file-handling
updated_at: "2026-08-31T10:52:55.885Z"
spec_point_ids: ["spcpt_bFkV2WZqZCzyH7vk", "spcpt_kkVZSM5jzGhgy9Jw"]
spec_point_codes: []
guided_study: false
---

# File Handling

## File operations

> **Spec point** — `spcpt_bFkV2WZqZCzyH7vk`

## File operations

### What are file-processing operations?

- File-processing involves **interacting with external files **stored on  secondary storage (e.g. hard drives, SSDs)
- In programming, files must be properly **opened**, **read/written**, and **closed** to ensure data is handled correctly
- Different **types of file access** are also used

#### Common file operations

| **Operation** | **Description** |
|---|---|
| `Open` | The file is opened in a specific **mode**: <br>• `read` – to read data <br>• `write` – to overwrite data <br>• `append` – to add new data to the end |
| `Read` | Data (e.g. lines or records) is read from the file into memory |
| `Write` | Data is written to the file (overwriting or appending depending on mode) |
| `Close` | Ends access to the file and ensures all data is saved properly |

#### Types of file access

| **Access type** | **Description** |
|---|---|
| **Serial access** | Records are **stored one after another**, and accessed in the **order they were added**. Often used for logging |
| **Sequential access** | Records are **read from the beginning to the end**, in order. Common for batch processing and text files |
| **Random access** | Records can be **accessed directly** using a **key or file position**. Common in databases or indexed files |

## Programming file-operations

> **Spec point** — `spcpt_kkVZSM5jzGhgy9Jw`

## Programming file-operations

### Pseudocode

#### Basic file operations

#### Serial access (e.g. logging events)

- Data is written **one after another** (no specific order)
- Often used with **APPEND** mode

**Example**: Writing logs serially

#### Sequential access (e.g. reading through all records)

- Records are **read in order** from start to end
- Common for reports or summaries

**Example**: Reading student grades sequentially

#### Random access (e.g. accessing specific records by key)

- Accesses records **directly using a key** (e.g. record number or unique ID)
- Requires **indexed files** or fixed-length records

**Example**: Update a student’s grade by record position

#### Summary

| **Command** | **Purpose** | **Example** |
|---|---|---|
| `OPENFILE` | Opens a file in a specified mode | `OPENFILE "file.txt" FOR READ` |
| `READFILE` | Reads one line from a text file | `READFILE student FROM "file.txt"` |
| `WRITEFILE` | Writes one line to  a text file | `WRITEFILE student TO "file.txt"` |
| `CLOSEFILE` | Closes the file | `CLOSEFILE "file.txt"` |
| `SEEK` | Moves to a specific record (random access) | `SEEK "file.txt", 5` |
| `EOF` | Tests whether the end of the file has been reached | `WHILE NOT EOF("file.txt")` |
| `GETRECORD` | Reads the record at the file pointer | `GETRECORD "file.dat", ThisStudent` |
| `PUTRECORD` | Writes a record at the file pointer | `PUTRECORD "file.dat", ThisStudent` |

### Python

#### Basic file operations

#### Serial access (e.g. logging events)

**Example**: Appending log entries to a file (serial write)

#### Sequential access (e.g. reading through all records)

**Example**: Reading through each student line by line

#### Random access (e.g. accessing specific records by key)

**Example**: Update a student’s grade by index (record number)

#### Summary

| **Operation** | **Python Example** |
|---|---|
| Open | `open("file.txt", "r")` |
| Read | `file.readline()` / `for line in file:` |
| Write | `file.write("text")` |
| Close | `file.close()` or use `with open(...)` |
| Random access | `lines = file.readlines()` + list indexing |

### Java

#### Basic file operations

#### Serial access (e.g. logging events)

**Example**: Appending log entries to a file (serial write)

#### Sequential access (e.g. reading through all records)

**Example**: Reading through each student line by line

#### Random access (e.g. accessing specific records by key)

**Example**: Update a student’s grade by index (record number)

#### Summary

| **Operation** | **Java Example** |
|---|---|
| Open (read) | `BufferedReader reader = new BufferedReader(...)` |
| Read | `reader.readLine()` or `while ((line = ...) != null)` |
| Write | `BufferedWriter writer = new BufferedWriter(...)` |
| Append | `new FileWriter("file.txt", true)` |
| Close | `reader.close()` / `writer.close()` |
| Random access | `RandomAccessFile` (complex) or simulate with `List` |
