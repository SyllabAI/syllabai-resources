# File Processing & Exception Handling

Course: cie-a-level-computer-science-19 · Section: 20. Further Programming

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/20-further-programming-/file-processing-and-exception-handling/


## Card 1 — question_and_answer (`fl_qCDgwXZj46rkTs8J`)

**FRONT**

What does file processing involve?


**BACK**

File processing involves **interacting with external files stored on secondary storage**, such as hard drives and SSDs.


Spec links: `spcpt_bFkV2WZqZCzyH7vk`


## Card 2 — question_and_answer (`fl_NKvQy7cxFYp5M4Xn`)

**FRONT**

State the three stages a file must go through for data to be handled correctly.


**BACK**

A file must be properly **opened**, then **read from or written to**, and then **closed**.


Spec links: `spcpt_bFkV2WZqZCzyH7vk`


## Card 3 — question_and_answer (`fl_PR9kK7SDnHCC2pFZ`)

**FRONT**

Name the three modes a file can be opened in.


**BACK**

The three modes are **read**, to read data, **write**, to overwrite data, and **append**, to add new data to the end.


Spec links: `spcpt_bFkV2WZqZCzyH7vk`


## Card 4 — question_and_answer (`fl_hbh2kgr73R73VdSZ`)

**FRONT**

Why must a file be closed after use?


**BACK**

Closing the file **ends access to it and ensures all the data is saved properly**.


Spec links: `spcpt_bFkV2WZqZCzyH7vk`


## Card 5 — keyword_definition (`fl_8jDcD64w8kw8bn8G`)

**FRONT**

Define **serial access**.


**BACK**

In serial access, records are **stored one after another and accessed in the order they were added**, which makes it suited to logging.


Spec links: `spcpt_bFkV2WZqZCzyH7vk`


## Card 6 — keyword_definition (`fl_nYRw5RqnWNRF3n2y`)

**FRONT**

Define **sequential access**.


**BACK**

In sequential access, records are **read in order from the beginning of the file to the end**, which suits batch processing and text files.


Spec links: `spcpt_bFkV2WZqZCzyH7vk`


## Card 7 — keyword_definition (`fl_jz5FnH3ZdyZcv92p`)

**FRONT**

Define **random access**.


**BACK**

In random access, records can be **accessed directly using a key or file position**, which suits databases and indexed files.


Spec links: `spcpt_bFkV2WZqZCzyH7vk`


## Card 8 — fill_in_the_blanks (`fl_C27P4k8sBmt9mjr6`)

**FRONT**

Random access requires indexed files or records of a <u>**                **</u> length, so that the position of any record can be calculated.


**BACK**

Random access requires indexed files or records of a **fixed** length, so that the position of any record can be calculated.


*Blanks: 1 — answers: []*

Spec links: `spcpt_bFkV2WZqZCzyH7vk`

Flags: blank_answer_mismatch


## Card 9 — true_or_false (`fl_vcnNmDJ2N7jK5tSD`)

**FRONT**

**True or False?**

Opening a file in write mode adds the new data after the data already in the file.


**BACK**

**False.**

Write mode **overwrites** the existing data, and it is **append** mode that adds new data to the end.


Spec links: `spcpt_bFkV2WZqZCzyH7vk`


## Card 10 — question_and_answer (`fl_GsXyktWr3ZVjmmzp`)

**FRONT**

Which type of file access would you use to write an event log, and in which mode would the file be opened?


**BACK**

**Serial access** is used for a log, with the file opened in **APPEND** mode so each entry is added after the last.


Spec links: `spcpt_kkVZSM5jzGhgy9Jw`


## Card 11 — question_and_answer (`fl_y9QY5VR3Jy3qwMy4`)

**FRONT**

What does the `OPENFILE` command do, and what must follow it?


**BACK**

`OPENFILE` **opens a file in a specified mode**, written as `OPENFILE "file.txt" FOR READ`.


Spec links: `spcpt_kkVZSM5jzGhgy9Jw`


## Card 12 — question_and_answer (`fl_ZQMT7pSscxRStdt6`)

**FRONT**

What do `READFILE` and `WRITEFILE` each do?


**BACK**

`READFILE` **reads one line from a text file** into a variable, and `WRITEFILE` **writes one line to a text file**.


Spec links: `spcpt_kkVZSM5jzGhgy9Jw`


## Card 13 — question_and_answer (`fl_2CWx3zyktf6MD4fx`)

**FRONT**

What does the `EOF` function test, and where is it typically used?


**BACK**

`EOF` tests **whether the end of the file has been reached**, and is typically used as the condition of a loop, such as `WHILE NOT EOF("file.txt")`.


Spec links: `spcpt_kkVZSM5jzGhgy9Jw`


## Card 14 — fill_in_the_blanks (`fl_FB97BtNKvgRFrvfY`)

**FRONT**

The <u>**                **</u> command moves to a specific record in a file opened for random access.


**BACK**

The **SEEK** command moves to a specific record in a file opened for random access.


*Blanks: 1 — answers: []*

Spec links: `spcpt_kkVZSM5jzGhgy9Jw`

Flags: blank_answer_mismatch


## Card 15 — question_and_answer (`fl_KqcjWPQrbW9xqS6h`)

**FRONT**

What is the difference between `GETRECORD` and `PUTRECORD`?


**BACK**

`GETRECORD` **reads the record at the file pointer** into a variable, while `PUTRECORD` **writes a record at the file pointer**.


Spec links: `spcpt_kkVZSM5jzGhgy9Jw`


## Card 16 — question_and_answer (`fl_MwX3knF3QR888NXX`)

**FRONT**

A program must update the grade in the 5th record of a random access file. Why is `SEEK` used twice?


**BACK**

`SEEK` is used **once before reading the record and again before writing it back**, because reading the record moves the file pointer past it.


Spec links: `spcpt_kkVZSM5jzGhgy9Jw`


## Card 17 — true_or_false (`fl_GmQx5FpRT7p6WgYK`)

**FRONT**

**True or False?**

A user-defined record type is declared between `TYPE` and `ENDTYPE`.


**BACK**

**True.**

A record such as `Student`, holding a `Name` and a `Grade`, is declared between `**TYPE**` and `**ENDTYPE**` before it can be used.


Spec links: `spcpt_kkVZSM5jzGhgy9Jw`


## Card 18 — question_and_answer (`fl_Kh8sYdhgn3m7mfW5`)

**FRONT**

In Python, what is the advantage of opening a file with `with open(...)`?


**BACK**

The file is **closed automatically**, so there is no need for a separate `file.close()` call.


Spec links: `spcpt_kkVZSM5jzGhgy9Jw`


## Card 19 — question_and_answer (`fl_nBfhy2yRbwTVZZ4m`)

**FRONT**

In Java, how is a file opened for appending rather than overwriting?


**BACK**

By passing `**true**`** as the second argument to **`**FileWriter**`, as in `new FileWriter("file.txt", true)`.


Spec links: `spcpt_kkVZSM5jzGhgy9Jw`


## Card 20 — question_and_answer (`fl_wCqR864rYXddT7Mx`)

**FRONT**

Python and Java both simulate random access rather than using it directly. How?


**BACK**

The whole file is read into a **list of records**, the required record is changed **by its index**, and the list is then written back over the file.


Spec links: `spcpt_kkVZSM5jzGhgy9Jw`


## Card 21 — keyword_definition (`fl_K8jy6NjmkTwCjW9f`)

**FRONT**

Define **exception**.


**BACK**

An exception is an **unexpected event that disrupts the normal execution of a program**.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 22 — keyword_definition (`fl_dpfdS4Xz3KfX8n9C`)

**FRONT**

Define **exception handling**.


**BACK**

Exception handling is **how a program detects and responds to errors**, allowing it to recover or to shut down cleanly.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 23 — question_and_answer (`fl_dZnsfTfpkqcSCr36`)

**FRONT**

State three benefits of using exception handling.


**BACK**

It **prevents the program crashing unexpectedly**, allows **user-friendly error messages**, and makes the program more **robust and reliable**.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 24 — question_and_answer (`fl_wJ2bdPz9pfH8jBnM`)

**FRONT**

Give four problems that exception handling can deal with.


**BACK**

**Division by zero**, **a file not being found or an end-of-file error**, **hardware or device failure** such as a lost printer connection, and **invalid input from a user**.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 25 — question_and_answer (`fl_7DZCDzjNFs9zN6fp`)

**FRONT**

Name the three causes of exceptions, with an example of each.


**BACK**

**Programming errors**, such as an uninitialised variable; **user errors**, such as entering text instead of a number; and **hardware failure**, such as a lost connection to a printer.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 26 — question_and_answer (`fl_pcTwf9JZhSRx4Dgb`)

**FRONT**

What does the `TRY` keyword do?


**BACK**

`TRY` **starts a block of code that may raise an error**.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 27 — question_and_answer (`fl_CBbqgg4b7HQRC888`)

**FRONT**

When does the code in an `EXCEPT` block run?


**BACK**

It runs **only if an error occurs in the **`**TRY**`** block**.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 28 — fill_in_the_blanks (`fl_9Vk9XpkCMZjb6ms6`)

**FRONT**

The keyword <u>**                **</u> marks the end of the exception handling structure.


**BACK**

The keyword **ENDTRY** marks the end of the exception handling structure.


*Blanks: 1 — answers: []*

Spec links: `spcpt_fSKbbshqWdC8Mnnz`

Flags: blank_answer_mismatch


## Card 29 — true_or_false (`fl_CBSFXkfrnyfprb9k`)

**FRONT**

**True or False?**

The code inside an `EXCEPT` block runs every time the program is executed.


**BACK**

**False.**

The `EXCEPT` block runs **only when an error occurs** in the `TRY` block it belongs to.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 30 — question_and_answer (`fl_7cd9kwxCRZrDWcbJ`)

**FRONT**

In Python, which exception is raised when a program tries to open a file that does not exist?


**BACK**

A `**FileNotFoundError**` is raised.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 31 — question_and_answer (`fl_7skHr72SKXK96x5K`)

**FRONT**

In Python, which exception is raised by an attempt to divide by zero?


**BACK**

A `**ZeroDivisionError**` is raised.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 32 — question_and_answer (`fl_hbdP45Xdq6k3FY6B`)

**FRONT**

Why is more than one `except` branch written for a single `try` block?


**BACK**

So that **each type of error can be given its own specific handling and message**, rather than one message covering every possible fault.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 33 — question_and_answer (`fl_Wnx7gSynJ9svFVdC`)

**FRONT**

What is the purpose of a general `except Exception` branch at the end of the list?


**BACK**

It **catches any error that the earlier, more specific branches did not**, so an unexpected fault still leaves the program under control.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 34 — fill_in_the_blanks (`fl_C5Rt4rKXv5gtPRd9`)

**FRONT**

Code placed in a <u>**                **</u> block runs whether or not an exception was raised, so it is used to close the file.


**BACK**

Code placed in a **finally** block runs whether or not an exception was raised, so it is used to close the file.


*Blanks: 1 — answers: []*

Spec links: `spcpt_fSKbbshqWdC8Mnnz`

Flags: blank_answer_mismatch


## Card 35 — true_or_false (`fl_xwJJxfsBFxCZpRT3`)

**FRONT**

**True or False?**

In Java, dividing an integer by zero raises an `ArithmeticException`.


**BACK**

**True.**

Java raises an `**ArithmeticException**`, which is caught in its own `catch` branch.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 36 — question_and_answer (`fl_NGgBJ8G32PhqBgrR`)

**FRONT**

In Java, which keyword introduces the block that handles a particular type of exception?


**BACK**

The `**catch**` keyword, which names the exception type it handles, as in `catch (FileNotFoundException e)`.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`


## Card 37 — question_and_answer (`fl_DNFHXtfNWygvBFyH`)

**FRONT**

Why does the `finally` block itself contain error handling when it closes a file?


**BACK**

Because the **file may never have been opened successfully**, so the attempt to close it could raise an error of its own.


Spec links: `spcpt_fSKbbshqWdC8Mnnz`

