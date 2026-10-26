# Exam Questions — Files
**10. Data Types & Structures** · Cambridge (CIE) AS computer-science (9618)
> Source: [https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/) · 1 questions across 1 sets


## Exam Questions (1 questions)


### Q1 — medium — 5 marks

**Q1** [4 marks]

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


**Q1** [1 mark]

The requirement changes, and the algorithm will now output three lines from the file, starting from a **given** line number.

The modified algorithm will be implemented as a function which will:

- be called with an integer parameter representing the given line number
- output three lines, starting at the given line
- return `TRUE` if the 3 lines are output, or `FALSE` if it was not possible to output the 3 lines.

Describe the changes that need to be made to **steps 2 to 8 **of the algorithm given in part **(a)**.

*Source: November 2024 9618/21 Q3B*

