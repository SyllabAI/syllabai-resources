## File Handling

* Files are needed to import contents (from a file) saved in secondary
  memory into the program, or to save the output of a program (in a
  file) into secondary memory, so that it is available for future use

**Pseudocode:**

* Opening a file: `OPENFILE <filename> FOR READ/WRITE/APPEND`
* Reading a file: `READFILE <filename>, <variable>`
* Writing a line of text to the file: `WRITEFILE <filename>, <string>`
* Closing a file: `CLOSEFILE <filename>`
* Testing for end of the file: `EOF(filename)`

**Python:**

* Opening a file: `variable = open(“filename”, “mode”)`

Where the mode can be:

| **Mode** | **Description** |
|----|----|
| r | Opens file for reading only. Pointer placed at the beginning of the file. |
| w | Opens a file for writing only. Overwrites file if file exists or creates new file if it doesn’t |
| a | Opens a file for appending. Pointer at end of file if it exists or creates a new file if not |

* Reading a file:
  * Read all characters: `variable.read()`
  * Read each line and store as list: `variable.readlines()`
* Writing to a file:
  * Write a fixed a sequence of characters to file: `variable.write(“Text”)`
  * Write a list of string to file: `variable.write(‘ ‘.join(‘Z’, ‘Notes’))`



