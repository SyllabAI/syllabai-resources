# Files

Course: cie-a-level-computer-science-19 · Section: 10. Data Types & Structures

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/10-data-types-and-structures-/files/


## Card 1 — keyword_definition (`fl_cT6wmr4hNFVJmDt4`)

**FRONT**

Define **file handling**.


**BACK**

File handling is **the use of programming techniques to work with information stored in text files**.


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 2 — question_and_answer (`fl_mw6pxGbfhKxckv2r`)

**FRONT**

Name the four main file handling techniques.


**BACK**

**Opening**, **reading**, **writing** and **closing** text files.


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 3 — question_and_answer (`fl_6Fy69Ghz4cZdMYQq`)

**FRONT**

Write the pseudocode to open a file called fruit.txt for reading.


**BACK**

`OPENFILE "fruit.txt" FOR READ`


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 4 — question_and_answer (`fl_B9dyKCRP5RHH2hW4`)

**FRONT**

Write the pseudocode to open a file called Shopping.txt for writing.


**BACK**

`OPENFILE "Shopping.txt" FOR WRITE`


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 5 — question_and_answer (`fl_KwCTwJH4GZtzF2W7`)

**FRONT**

Write the pseudocode to close a file called fruit.txt.


**BACK**

`CLOSEFILE "fruit.txt"`


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 6 — question_and_answer (`fl_tj55HFXgNZrhkh36`)

**FRONT**

Write the pseudocode to read a line from fruit.txt into `FruitName`.


**BACK**

`READFILE "fruit.txt", FruitName`


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 7 — question_and_answer (`fl_QrgPNVyDwqZnwDm3`)

**FRONT**

Write the pseudocode to write the word Oranges to fruit.txt.


**BACK**

`WRITEFILE "fruit.txt", "Oranges"`


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 8 — true_or_false (`fl_nv97rrSzNZCXS7DY`)

**FRONT**

**True or False?**

`READFILE` writes a line to a file.


**BACK**

**False.**

`READFILE` **reads** a line from a file. `WRITEFILE` is the command that writes a line to a file.


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 9 — question_and_answer (`fl_SgnJDbqvTKZN7y9G`)

**FRONT**

Write the pseudocode condition that checks the end of fruit.txt has not been reached.


**BACK**

`IF NOT EOF("fruit.txt") THEN`


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 10 — fill_in_the_blanks (`fl_Gg4f7gHX77Fj66Bt`)

**FRONT**

The function <u>**        **</u> returns TRUE when the end of a file has been reached.


**BACK**

The function **EOF** returns TRUE when the end of a file has been reached.


*Blanks: 1 — answers: []*

Spec links: `spcpt_t5QxGmPqkFwzJk84`

Flags: blank_answer_mismatch


## Card 11 — question_and_answer (`fl_yCJxjXyZvJkrhFsw`)

**FRONT**

How do you create a new file in pseudocode?


**BACK**

Use `OPENFILE "Shopping.txt" FOR WRITE`, which **overwrites the file or creates it** if it does not exist.


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 12 — question_and_answer (`fl_W9ntJ8yQyM2f4b65`)

**FRONT**

Which mode adds data to the end of an existing file?


**BACK**

`FOR APPEND`, written as `OPENFILE "Shopping.txt" FOR APPEND`.


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 13 — question_and_answer (`fl_K9BK85JQZ4CXB67X`)

**FRONT**

What is the difference between opening a file FOR WRITE and FOR APPEND?


**BACK**

`FOR WRITE` **overwrites or creates** the file, whereas `FOR APPEND` **adds to the end** of an existing file.


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 14 — question_and_answer (`fl_WpBz8NN286GHkPx2`)

**FRONT**

Which loop is used to read every line of a file until the end?


**BACK**

A `WHILE NOT EOF(...)` loop, closed with `ENDWHILE`.


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 15 — true_or_false (`fl_X6V6KTVH7cdPTXYq`)

**FRONT**

**True or False?**

A file should be closed before it has been fully read.


**BACK**

**False.**

The file is **closed after** the reading loop has finished, using `CLOSEFILE`.


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 16 — question_and_answer (`fl_3NtGsh4CM4NzygNT`)

**FRONT**

In the fruit-counting example, what does `FruitCount` store?


**BACK**

An **INTEGER** that keeps track of **how many fruits have been read** from the file.


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 17 — question_and_answer (`fl_66N5Tj6bBQQxQn9Z`)

**FRONT**

In the fruit-counting example, what does `FruitFile` store?


**BACK**

A **STRING** holding the **name of the file being read**, "fruit.txt".


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 18 — question_and_answer (`fl_PKBJqtYjc2NjK9d3`)

**FRONT**

A program reads 25 integers from Data.txt into an array.

Which two loop options are accepted?


**BACK**

A `WHILE NOT EOF("Data.txt") DO ... ENDWHILE` loop, or a `FOR Counter ← 1 TO 25 ... NEXT Counter` loop.


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 19 — question_and_answer (`fl_JPpVjDnCGJRzQdpf`)

**FRONT**

When reading a file into an array, how is each value stored?


**BACK**

`DataArray[Counter] ← LineData`, with `Counter` incremented on each pass of the loop.


Spec links: `spcpt_t5QxGmPqkFwzJk84`


## Card 20 — fill_in_the_blanks (`fl_nFNv7fMRxwFtgNS8`)

**FRONT**

When reading a file into an array with lower bound 1, `Counter` is initialised to <u>**        **</u> before the loop.


**BACK**

When reading a file into an array with lower bound 1, `Counter` is initialised to **1** before the loop.


*Blanks: 1 — answers: []*

Spec links: `spcpt_t5QxGmPqkFwzJk84`

Flags: blank_answer_mismatch

