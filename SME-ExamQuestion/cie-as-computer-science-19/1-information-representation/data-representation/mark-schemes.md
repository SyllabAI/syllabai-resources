# Mark Schemes — Data Representation
**1. Information representation** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (7 questions)


### Q1
> **[mark-scheme]**
> **1 mark** for:
> 
> Either
> 
> - kibibyte = 1,024 bytes // 210 bytes **and **
> megabyte = 1000 kilobytes //1 000 000 bytes // 103 kilobytes // 106 bytes
> 
> Or
> 
> - kibi is binary prefix **and **mega is denary prefix
> **[mark-scheme]**
> (i) 1111 0011 1100
> 
> (ii) 865
> 
> (iii) 470
> **[mark-scheme]**
> **1 mark** for a correct application
> 
> **1 mark** for a corresponding justification
> 
> - An application that performs financial / banking calculations
> - ... because it is difficult to represent decimal values exactly in normal binary and financial transactions use only two decimal places and must be accurate, no accumulating errors
> 
> Or
> 
> - Electronic displays, e.g. calculators, digital clocks
> - ... because visual displays only need to show individual digits
> - ... because conversion between denary and BCD is easier
> 
> Or
> 
> - The storage of the date and time in the BIOS of a PC
> - ... because conversion with denary is easier

### Q2
> **[mark-scheme]**
> 1 mark for each correct answer:
> 
> - binary
> - 3072
> - denary/decimal
> - 2000
> 
> A kibibyte has a **binary **prefix. Three kibibytes is the same as **3072** bytes. A megabyte has a **decimal/denary** prefix. Two terabytes is the same as **2000** gigabytes.
> **[mark-scheme]**
> **1 mark **for correct answer:
> 
> **F1**
> **[mark-scheme]**
> **1 mark** for a correct answer:
> 
> The answer is too long to be represented in **the same number of bits **as the binary numbers being added
> **[mark-scheme]**
> **1 mark** for all 3 answers correct:
> 
> | Character set | Number of bits |
> |---|---|
> | ASCII | **7** |
> | extended ASCII | **8** |
> | Unicode | **16/32** |
> 
> **1 mark **each:
> 
> - Each character has a **unique** binary code
> - The binary code for each character is stored in sequence

### Q3
> **[mark-scheme]**
> **1 mark** for:
> 
> 3300 kibibytes
> **[mark-scheme]**
> **1 mark** each:
> 
> - Converting 100 to binary** 0110 0100 **and 10 to binary **0000 1010 **
> - Subtraction method - converting 10 to – 10 and adding // direct subtraction …
> - … correct answer **0101   1010**
> 
> Method 1: Converting to -10 and adding:
> 
> Binary for +10 is 0000 1010
> 
> Binary for –10 is 1111 0110
> 
> Binary for 100 is 0110 0100
> 
> 100 + (-10):
> 
> 0 1 10 0 1 0 0 
> <u>+  1  1 1 1 0 1  1 0</u>
> (1) 0 1 0 1 1 0 1 0
> Carries: 1 1 0 0 1 0 0 0
> 
> Method 2: Direct Subtraction
> 
> Borrows:
> 
> 0 0 0 1 1 0 1 0 
>     0 1 1 0 0 1 0 0 
> <u>– 0 0 0 0 1 0 1 0</u>
> 0 1 0 1 1 0 1 0
> **[mark-scheme]**
> **1 mark** for working:
> 
> 1100 0000 1111 // 2048 + 1024 + 8 + 4 + 2 + 1
> 
> // (12** 16*<sup>*2*</sup>*) + 15 // (12 * 16 * 16) + 15 // 3072 + 15
> 
> **1 mark** for correct answer:
> 
> 3087

### Q4
> **[mark-scheme]**
> 1 mark each:
> 
> - Working – carried values clearly indicted
> - Correct answer 0001 1000
> - Overflow clearly indicated as overflow
> 
> Example:
> 
> 1 0 0 1  1   1   1 0
>     0 1 1 0 0 0 0 1
> <u>+ 0 0 0 1 1 0 0 1</u>
> <u>(1) 0 0 0 1 1000</u>
>        1   1   1   1   1   1   1 ........................(carries)

### Q5
> **[mark-scheme]**
> **1 mark** for:
> 
> Denary value: 8107
> **[mark-scheme]**
> **1 mark **for each bullet point for the method **(max 2)**
> 
> e.g.
> 
> - Flip each bit then add 1 …
> - … method of converting the new binary number into denary
> - Most significant 1 bit is treated as the corresponding negative denary value …
> - … add the other positive corresponding denary values
> 
> **1 mark** for correct conversion
> 
> Denary value: −97

### Q6
> **[mark-scheme]**
> **1 mark** for identification **1 mark** for matching description
> 
> e.g.
> 
> - ASCII
> - 7/8 bits per character // represents 128/256 characters // represents all characters from Latin alphabet
> - UNICODE
> - 8/16/32 bits per character // represents 256/65536+ characters // represents all characters in all languages

### Q7
> **[mark-scheme]**
> 1 mark for:
> 
> - A tebibyte = 1024 gibibytes / 1 048 576 kibibytes / 240 bytes whereas a gigabyte = 1000 megabytes / 1 000 000 kilobytes / 109 bytes
> - Tebi is binary prefix giga is denary prefix
> **[mark-scheme]**
> (i)** 1 mark** for:
> 
> C67
> 
> (ii)** 1 mark** for:
> 
> −1641
> 
> (iii) **1 mark** for:
> 
> 573
> **[mark-scheme]**
> **1 mark **for working **1 mark **for answer.
> 
> Working 
> Using the two’s complement and adding:
> 
> 23 in binary = 00010111 so minus 23 is 11101001
> 
> 0100 1010
> <u>+  1110 1001</u>
> (1)0011 0011
> 
> Direct subtraction:
> 
> 0100 1010
> <u>- 0001 0111</u>
>     0011 0011
> 
> Answer: 0011 0011
> **[mark-scheme]**
> **1 mark** from:
> 
> - The answer cannot be represented in the number of bits available
> - The answer is larger than the maximum positive number that can be stored in the register
> - The answer is smaller than the most negative number that can be stored in the register
