# Exam Questions — Files
**10. Data Types & Structures** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 4 questions across 1 sets


## Exam Questions (4 questions)


### Q1 — very_hard — 6 marks

**Q1** [6 marks]

A weather station stores its temperature readings in the text file `Readings.txt`.

Each line of the file holds one reading as a numeric string, for example `18.4`. The number of readings in the file is not known, and the file may be empty.

Write pseudocode for a function `CountAbove()` that:

- takes one parameter `Limit` of type `REAL`
- opens `Readings.txt` for reading
- reads every line in the file
- counts the readings that are greater than `Limit`
- closes the file
- returns the count as an `INTEGER`, returning 0 if the file is empty.

You may use the built-in functions `EOF()` and STR<u>TO</u>NUM().

### Q2 — medium — 3 marks

**Q2** [3 marks]

A program writes a message to a log file each time an error occurs.

The text file `ErrorLog.txt` already exists and contains the messages from earlier runs of the program. These messages must not be lost.

The procedure `AddError()` takes one parameter `Message` of type `STRING`. It adds `Message` to `ErrorLog.txt` as a new line, then closes the file.

The first and last lines of the procedure are given.

Complete the procedure by writing the three pseudocode statements that are missing.

### Q3 — easy — 2 marks

**Q3** [2 marks]

A weather station records the total rainfall for each day.

At the end of each day the program adds one new line to the text file `Rainfall.txt`. This file already contains the totals for all the previous days. The totals for the previous days must not be lost.

Explain why the program stores the daily totals in a text file rather than in an array, and why the file is opened in `APPEND` mode rather than `WRITE` mode.

### Q4 — medium — 5 marks

**Q4** [4 marks]

An algorithm will output the last three lines from a text file `Result.txt `

The lines need to be output in the same order as they appear in the file.

Assume:

- Three variables `LineX, LineY` and `LineZ` will store the three lines. These are of type string and all three variables have been initialised to an empty string.
- The file exists and contains **at least** three lines.

The algorithm to output the lines is expressed in eight steps.

Complete the steps.

1. Open the file ...........................................................................
2. Loop until ...........................................................................
3. ........................................................................... and store in `ThisLine`
4. Assign `LineY` to `LineX`
5. Assign `LineZ` to `LineY `
6. Assign `ThisLine` to `LineZ `
7. After the loop, ...........................................................................
8. Output `LineX, LineY, LineZ`

*Source: November 2024 9618/21 Q3A*


**Q4** [1 mark]

The requirement changes, and the algorithm will now output three lines from the file, starting from a **given** line number.

The modified algorithm will be implemented as a function which will:

- be called with an integer parameter representing the given line number
- output three lines, starting at the given line
- return `TRUE` if the 3 lines are output, or `FALSE` if it was not possible to output the 3 lines.

Describe the changes that need to be made to **steps 2 to 8 **of the algorithm given in part **(a)**.

*Source: November 2024 9618/21 Q3B*

