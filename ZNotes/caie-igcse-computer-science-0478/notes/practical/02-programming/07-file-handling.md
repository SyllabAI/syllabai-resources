## File Handling

* ## Computer programs store data that will be needed again in a file.
* Data stored in RAM is volatile and will be lost when the computer is powered off.
* Data saved to a file is stored permanently, allowing it to be accessed by the same program at a later date or by other programs.
* Stored data in a file can be transferred and used on other computers.
* The storage of data in files is a commonly used feature in programming.

***Key point: When writing in a file, the program is outputing the data to the file, and when reading a file, the program in inputing the data from the file***

\n There are 3 ways a file can be opened in a program i.e. to write, to read and to append

## Writing in a file

```javascript
OPENFILE "filename.txt" FOR WRITE

//When opening a file to write, all the data already existing in the file is OVERWRITTEN


WRITEFILE "filename.txt" , Value

// The next command of WRITEFILE would be writen on next line of the file

CLOSEFILE "filename.txt"
```

## Reading a file:

```javascript
OPENFILE "filename.txt" FOR READ
READFILE "filename.txt" , Variable
// The value in the line (which is identified by the number of times this is being run) is stored in the variable
CLOSEFILE "filename.txt"
```

## Reading a file till EOF:

```javascript
OPENFILE "filename.txt" FOR READ
DECLARE DataVariable : STRING
WHILE NOT EOF("filename.txt) DO
 READFILE "filename.txt", DataVariable
 // here the line can be outputted or stored in an array. This process will repeat until every line
 //before the file ends has been read
ENDWHILE
```