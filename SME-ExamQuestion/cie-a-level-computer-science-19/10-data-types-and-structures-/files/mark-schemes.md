# Mark Schemes — Files
**10. Data Types & Structures** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (4 questions)


### Q1
The `WHILE` loop tests for the end of the file before it reads. If `Readings.txt` is empty then `EOF("Readings.txt")` is `TRUE` on the first test, the loop body never runs, and the function returns 0.

**[6 marks]**

> **[mark-scheme]**
> **1 mark** for a function header naming the parameter and the return type, `FUNCTION CountAbove(Limit : REAL) RETURNS INTEGER`, with a matching `ENDFUNCTION`
> 
> **1 mark** for a counter set to 0 before the loop
> 
> **1 mark** for `OPENFILE "Readings.txt" FOR READ`
> 
> **1 mark** for a pre-condition loop controlled by the end of the file, `WHILE NOT EOF("Readings.txt")` with `ENDWHILE`
> 
> **1 mark** for `READFILE "Readings.txt", ThisLine` inside the loop, then a test of the form IF STR<u>TO</u>NUM(ThisLine) > Limit THEN, and adding 1 to the counter
> 
> **1 mark** for `CLOSEFILE "Readings.txt"` followed by `RETURN Count`
> 
> Accept a `STRING` variable holding the file name in place of the literal `"Readings.txt"`, used consistently.
> 
> Do not accept `REPEAT ... UNTIL EOF("Readings.txt")`. A post-condition loop reads a line before it tests for the end of the file, so it fails on an empty file and cannot return 0.
> 
> Do not accept a comparison written without a conversion, such as `IF ThisLine > Limit THEN`. `READFILE` stores a `STRING`, and a `STRING` cannot be compared with a `REAL`.
> 
> Do not accept the comparison written with `>=`. A reading equal to `Limit` is not greater than `Limit`.
> 
> Accept `OPEN` for `OPENFILE` and `CLOSE` for `CLOSEFILE`. Do not accept `READ` in place of `READFILE`.

> **[exam-tip]**
> The empty file is what this question is testing, and `REPEAT ... UNTIL EOF()` is the answer that fails it. A post-condition loop always runs its body once, so it calls `READFILE` on a file that has no lines. Use `WHILE NOT EOF(...)` whenever the number of lines is unknown, and keep `REPEAT` for loops that must run at least once.
> 
> `READFILE` always gives you a `STRING`, even when the line looks like a number. Convert it with STR<u>TO</u>NUM() before any numeric comparison or arithmetic. Check the spelling on the Insert. It is STR<u>TO</u>NUM, and there is no `ROUND`, `ABS` or `SPLIT` on this paper.

### Q2
**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `OPENFILE "ErrorLog.txt" FOR APPEND`
> 
> **1 mark** for `WRITEFILE "ErrorLog.txt", Message`
> 
> **1 mark** for `CLOSEFILE "ErrorLog.txt"` written after the `WRITEFILE` statement
> 
> Accept a `STRING` variable holding the file name in place of the literal `"ErrorLog.txt"`, provided the same variable is used in all three statements.
> 
> Do not accept `OPENFILE "ErrorLog.txt" FOR WRITE`. `WRITE` mode creates a new file and the earlier messages would be lost.
> 
> Do not accept `WRITEFILE Message` without the file name. The file name is the first argument of `WRITEFILE`.
> 
> Accept `OPEN` for `OPENFILE`, `WRITE` for `WRITEFILE` and `CLOSE` for `CLOSEFILE`, provided the file name and the mode or the data are correct; Cambridge mark schemes use these short forms in their own model answers and marking points.

> **[exam-tip]**
> The commonest loss here is dropping the file name. `WRITEFILE` and `CLOSEFILE` both need it, because a program may have more than one file open at the same time. Write `WRITEFILE "ErrorLog.txt", Message`, not `WRITEFILE Message`.
> 
> The second commonest loss is forgetting `CLOSEFILE` altogether. A procedure that opens a file and never closes it leaves the file open in `APPEND` mode, so the next part of the program cannot open it for reading.

### Q3
An array is held in memory while the program is running, so the daily totals would be lost when the program ends or the computer is switched off. A text file stores the totals permanently, so the earlier days are still there the next time the program is run. **[1]**

`WRITE` mode creates a new file, so the totals already in `Rainfall.txt` would be lost. `APPEND` mode adds the new line after the data that is already in the file, so the earlier totals are kept. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the data in an array is lost when the program ends / when the computer is switched off, but a file stores the data permanently
> 
> **1 mark** for `WRITE` mode would create a new file / overwrite the data already in `Rainfall.txt`, while `APPEND` mode adds the new line after the existing data
> 
> Accept for the first mark: "a file is non-volatile storage", or "the totals do not have to be entered again each time the program runs".
> 
> Accept for the second mark: "`APPEND` keeps the existing data" on its own.
> 
> Do not accept "a file can hold more data than an array" for the first mark. Capacity is not the reason the data is stored in a file here; losing the data when the program ends is.
> 
> Do not accept "a file is faster than an array". Reading from a file is slower than reading from memory, so this is not true.

> **[exam-tip]**
> Many students write only "so the data is saved". That sentence does not say what would be lost, so it rarely earns the mark. Say where an array lives and when it disappears: an array is in memory, and memory contents go when the program stops.
> 
> Learn the three text file modes by what they do to the data that is already in the file. `READ` does not change it, `WRITE` throws it away and starts the file again, and `APPEND` keeps it and adds after it. Any question that says the file already contains data that must not be lost is asking for `APPEND`.

### Q4
> **[mark-scheme]**
> One mark per emboldened part:
> 
> 1. Open the file **(Result.txt) in **<u>**read**</u>** mode **
> 2. Loop until **EOF(Result.txt) // EOF // end of file **
> 3. <u>**Read a / the / next line**</u>** (from the file) **and store in `ThisLine `
> 4. Assign `LineY` to `LineX`
> 5. Assign `LineZ` to `LineY`
> 6. Assign `ThisLine` to `LineZ`
> 7. After the loop, **close the file (Result.txt)**
> 8. Output `LineX, LineY, LineZ`
> **[mark-scheme]**
> Two loop solution
> 
> One mark per point:
> 
> 1. Loop until given line number (-1) / `<parameter>  (-1) `(lines have been read)
> 2. ... if end of file is reached then return FALSE
> 3. Loop for three lines // Read three lines // Repeat of 4 and 5 for three lines
> 4. Read a line and output it
> 5. ... if end of file is reached then return FALSE
> 6. After outputting the (required) lines return TRUE
> 7. Ordering of lines no longer needed
> 
> **Max 4 marks **
> 
> Alternative solution
> 
> **One loop solution mark scheme that reads to given line number + 2 **
> 
> One mark per point
> 
> 1. Loop until given line number + 2 / `<parameter>`  `+ 2 `(lines have been read)
> 2. **OR** end of file is reached
> 3. Return FALSE if EOF reached
> 4. Read a line from the file **in the loop**
> 5. Continue to order the last three lines read **in the loop** // Steps 4 to 6 stay the same
> 6. (If FALSE has **not **been returned) output the required three lines (in the correct order)
> 7. … **and** Return TRUE
> 
> **Max 4 marks**
