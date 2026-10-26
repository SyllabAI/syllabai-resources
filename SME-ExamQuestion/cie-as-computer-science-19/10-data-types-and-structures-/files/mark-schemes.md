# Mark Schemes — Files
**10. Data Types & Structures** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (1 questions)


### Q1
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
