# Mark Schemes — Data Integrity
**6. Security, privacy & data integrity** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (15 questions)


### Q1
Byte 3 contains seven 1s. Seven is odd, so byte 3 does not match the agreed even parity and the error is in this row. Every other row contains four 1s and is correct. **[1]**

Column 5 contains three 1s. Three is odd, so column 5 does not match the agreed even parity and the error is in this column. Every other column contains an even number of 1s and is correct. **[1]**

The bit that was changed is where the failing row and the failing column cross, so it is the bit in byte 3, column 5. **[1]**

That bit was received as 1 and should be 0. **[1]**

Byte 3 should have been received as **11100111**. **[1]**

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for identifying byte 3 as the row whose parity is wrong, supported by the count of seven 1s being odd
> 
> **1 mark** for identifying column 5 as the column whose parity is wrong, supported by the count of three 1s being odd
> 
> **1 mark** for stating that the changed bit lies at the intersection of that row and that column
> 
> **1 mark** for stating that the bit was received as 1 and should be 0
> 
> **1 mark** for the corrected byte 11100111
> 
> Accept "the fifth bit from the left" in place of "column 5"
> 
> Accept the corrected byte written with the bits spaced out, as 1 1 1 0 0 1 1 1
> 
> Do not accept an answer that identifies only the row or only the column. A single parity check on one byte shows that an error has occurred but cannot locate it; the block check needs both directions
> 
> Do not accept 11101110 or 11100110. Only one bit was changed, and the parity bit in column 8 is correct as received

> **[exam-tip]**
> Count the 1s in every row first and write the count beside each row, then do the same underneath every column. Do not try to spot the error by eye. With even parity you are looking for the one row and the one column whose count is odd, and the answer is where they cross.
> 
> A common mistake is to change the parity bit instead of the data bit. The parity bit in column 8 of byte 3 is part of the failing row, but it is not in the failing column, so it is not the bit that flipped. Only the cell that fails in both directions can be the error.

### Q2
Add the five values: 214 + 97 + 180 + 63 + 145 = **699** **[1]**

Divide by 256 and take the remainder: 699 divided by 256 is 2 remainder **187**, so the checksum is **187**. **[1]**

The printer adds the denary values of the five bytes it receives, works out the remainder after division by 256 in the same way, and compares its result with the checksum it received. If the two values are different, an error has occurred during transmission. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the total 699
> 
> **1 mark** for the checksum 187
> 
> **1 mark** for the receiver repeating the same calculation on the data it received and comparing the two values, with the conclusion that different values mean an error has occurred
> 
> Accept "if the two values are the same, no error has been detected" as the conclusion
> 
> Accept the working written on one line as 699 MOD 256 = 187
> 
> Do not accept 699 as the checksum. Step 2 of the algorithm has not been carried out
> 
> Do not accept "the checksum tells the printer which bit is wrong". A checksum shows only that the data has changed, not where

> **[exam-tip]**
> The third mark is lost by students who stop at "the printer checks the checksum". The printer cannot check anything until it has recalculated the checksum from the data it actually received, so say that the calculation is repeated and then the two values are compared.
> 
> Do not claim that a checksum locates the error. That is what a parity block does. A checksum, like a single parity check, tells you only that something has changed.

### Q3
Visual check: the receptionist compares the passport number shown on the screen with the number printed in the passport and confirms that the two are the same. **[1]**

Double entry: the passport number is typed in a second time and the software compares the two entries, showing an error message if they do not match. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for visual check, described as manually comparing the number entered, or shown on the screen, with the number on the source document
> 
> **1 mark** for double entry, described as entering the number twice and the computer comparing the two entries
> 
> Accept "double entry check", and accept the second entry being made by a second person.
> 
> Do not accept a parity check or a checksum. Both are methods of verification during data transfer, and here the number is being typed in.
> 
> Do not accept any validation check, such as a length check, a format check or a check digit.

> **[exam-tip]**
> The syllabus splits verification into two groups and the question tells you which group it wants. "When the passport number is entered" means data entry, so only a visual check and double entry can score. Parity and checksum belong to data transfer.
> 
> Naming a method is not describing it. Add what is compared with what, and one word becomes one mark.

### Q4
Multiply each digit by its weight:

| Digit | 3 | 1 | 4 | 0 | 2 | 6 | 8 |
|---|---|---|---|---|---|---|---|
| Weight | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
| Product | **24** | **7** | **24** | **0** | **8** | **18** | **16** |

All seven products correct **[1]**

Add the products: 24 + 7 + 24 + 0 + 8 + 18 + 16 = **97** **[1]**

Divide by 11 and take the remainder: 97 divided by 11 is 8 remainder **9** **[1]**

Subtract the remainder from 11: 11 - 9 = **2** **[1]**

The check digit is **2**, so the complete book code is **31402682**.

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the seven products 24, 7, 24, 0, 8, 18, 16
> 
> **1 mark** for the total 97
> 
> **1 mark** for the remainder 9
> 
> **1 mark** for the check digit 2
> 
> Accept follow-through: if the total is wrong but steps 3 and 4 are then carried out correctly on that wrong total, award the last two marks.
> 
> Accept the answer written as the full code 31402682 provided the working is shown.
> 
> Do not accept 9 as the check digit. That is the remainder from step 3, and step 4 has not been carried out.
> 
> Do not accept a check digit worked out with the weights applied from the right-hand end. The stem states that the left-hand digit has the weight of 8.

> **[exam-tip]**
> Two errors cost almost all the marks here. The first is stopping at the remainder and writing 9; step 4 is part of the algorithm, so always carry it out. The second is applying the weights the wrong way round, so read the stem again and write the weights above the digits before you multiply anything.
> 
> Set your working out as a row of digits with a row of weights underneath. Examiners award the products mark from that layout even when the arithmetic that follows goes wrong, so it is worth the thirty seconds.

### Q5
A presence check tests only that something has been typed into the course code field, so that the booking cannot be submitted with the field left empty. **[1]**

An existence check tests that the course code that was typed is actually held by the system, by comparing it with the course codes already stored. **[1]**

So a course code such as ZZ99 passes the presence check, because characters were entered, but fails the existence check, because no course is stored with that code. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for presence check: tests that data has been entered // that the field is not left blank or empty
> 
> **1 mark** for existence check: tests that the value entered is held by the system // matches a course code already stored // is one of the values on the stored list
> 
> **1 mark** for an example that separates the two, such as a course code that is not blank but is not stored, passing the presence check and failing the existence check
> 
> Accept "look-up check" as an alternative name for the existence check.
> 
> Do not accept "an existence check makes sure the field is filled in". That is the presence check, and this is the confusion the question is testing.
> 
> Do not accept "a presence check makes sure the course code is valid". A presence check tests nothing about the value that was entered.

> **[exam-tip]**
> These two names sound alike and students swap them constantly. Separate them by what each one looks at: a presence check looks at the box, an existence check looks at the stored data. A presence check never reads the value; it only asks whether the box is empty.
> 
> Give an example that fails one check and passes the other. An example that fails both, such as leaving the field blank, does not show the examiner that you know the difference.

### Q6
| Description | Validation check |
|---|---|
| Checks that data has been entered and that the field has not been left empty | Presence check |
| Checks that a value falls between a stated lower boundary and a stated upper boundary | **Range check** **[1]** |
| Checks that the data entered contains the correct number of characters | Length check |
| Checks that the data entered follows a stated pattern of letters and digits | **Format check** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for Range check in the second row
> 
> **1 mark** for Format check in the fourth row
> 
> Accept "range" and "format" written without the word "check"
> 
> Do not accept "limit check" in the second row. A limit check tests a single boundary, and the description gives both a lower and an upper boundary
> 
> Do not accept "type check" in the fourth row. A type check tests the data type, not the pattern of characters

> **[exam-tip]**
> Range check and limit check are the pair students mix up. A range check has two boundaries, one at each end. A limit check has only one, so it is the right answer for "no more than 5 items per customer" and the wrong answer for "between 0 and 100".
> 
> Format check and type check are the other pair. "Must be three letters followed by four digits" is a format check. "Must be a whole number" is a type check.

### Q7
Validation only tests whether a tracking number is reasonable and follows the rules set for the field, so it cannot tell whether the number is the right one for that parcel. **[1]**

The tracking number of a different parcel has the same length and the same pattern of characters, so it passes all three checks and is stored. **[1]**

The terminal never compares what was typed with the number printed on the parcel, so a verification method such as a visual check or double entry is also needed during data entry. **[1]**

Bits can also be changed by interference while the data travels over the network, and the three checks are not repeated after transmission, so a verification method such as a parity check or a checksum is needed during data transfer. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - validation only tests whether the data is reasonable // of the correct form // within the rules set for the field
> - a tracking number belonging to a different parcel has the same length and the same format, so it passes all three checks
> - the terminal does not compare the number typed with the number printed on the parcel, so validation cannot detect a wrong entry
> - a verification method during data entry, named as a visual check or double entry, is needed to compare the entry with the source
> - bits can be changed by interference while the data is transmitted over the network
> - the three validation checks are not repeated after transmission, so an error introduced in transit is not detected
> - a verification method during data transfer, named as a parity check or a checksum, is needed to detect a transmission error
> 
> **[4 marks]**
> 
> Accept "the data could be corrupted on its way to the server" for the transmission point.
> 
> Do not accept answers about hacking, malware or unauthorised access. This question is about data integrity, not data security.
> 
> Do not accept "the validation was not strong enough" unless you also say what validation cannot do.

> **[exam-tip]**
> This question has two separate stages in it, and it is easy to answer only one. Marks are available for what can go wrong when the number is typed in, and for what can go wrong while it travels to the server. Deal with both stages and name a verification method for each.
> 
> Watch the boundary with data security. Firewalls, encryption and passwords earn nothing here, because nobody has attacked the system. The data is wrong, not stolen.

### Q8
Validation only tests whether the data entered is reasonable and follows the rules set for the field. **[1]**

The number the clerk typed has the pattern of characters the format check expects and the number of characters the length check expects, so it is accepted even though it is the wrong number for this customer. **[1]**

A visual check would detect the error, because the clerk compares the number shown on the screen with the number on the original document and confirms that the two match. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for stating that validation only checks that the data is reasonable // of the correct form // within the rules set for the field
> 
> **1 mark** for explaining that the number entered satisfies both the format rule and the length rule, so it is accepted even though it is the wrong number for this customer
> 
> **1 mark** for one verification method, named and with what it compares:
> 
> visual check, the clerk compares the number on the screen with the number on the original document
> 
> OR double entry, the number is typed a second time and the software compares the two entries
> 
> Accept "the data entered is never compared with the source document" as an alternative route to the first mark.
> 
> Do not accept a range check, a presence check, an existence check or a check digit for the third mark. All of these are validation, not verification.
> 
> Do not accept "the clerk should be more careful" or "use a stricter validation rule". No validation rule can separate this number from the right one.

> **[exam-tip]**
> Most students answer this by inventing a tighter validation rule. There is no rule that helps, because the data entered is a genuine telephone number in the expected format. The only way to catch the error is to go back to the source document, and that is verification.
> 
> When you name a verification method, always say what is compared with what. "Double entry" written on its own is two words and no marks; "the number is typed twice and the software compares the two entries" earns the mark.

### Q9
Data validation is an automatic check carried out by the software to test whether the data entered is reasonable and follows the rules set for that field. **[1]**

Data verification is a check that the data entered, or the data received, matches the original source data and has not been changed. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for validation: a check made by the computer or the software that the data entered is reasonable // sensible // within the accepted bounds // follows the rules set for the field
> 
> **1 mark** for verification: a check that the data matches the original // matches the source document // has not been changed during entry or during transfer
> 
> Accept "checks the data is sensible" for validation
> 
> Accept "checks the data is the same as the original" for verification
> 
> Do not accept "validation checks that the data is correct" or "validation checks that the data is accurate". Validation cannot test accuracy, only reasonableness
> 
> Do not accept "verification checks that the data is accurate" on its own. Verification compares a copy with the source; it cannot show that the source itself was right

> **[exam-tip]**
> The word "correct" is what loses this mark. Validation asks "could this be right?"; verification asks "is this the same as what I was given?". Neither asks "is this true?".
> 
> Write your two definitions so that the word "reasonable" appears in the validation one and the word "matches" appears in the verification one. Those are the words the mark scheme is built around.

### Q10
> **[mark-scheme]**
> (i) **MP1** A message cannot contain a zero-length data field
> 
> **MP2** … so a blank line cannot be sent // there is no way to send a blank line
> 
> (ii) **MP1 **Append a (special) character to the start of the message text
> 
> **MP2 **interpret the new field data as a blank line
> 
> ALTERNATIVE
> 
> **MP1 **Change the message protocol and use an additional field to act as an indicator
> 
> **MP2 **Interpret the new field data

### Q11
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - Validation // a validation method named or described
> - …protects the data by ensuring that the data is reasonable / sensible and within specified bounds.

### Q12
> **[mark-scheme]**
> 1 mark for each bullet point.
> 
> - The administrator completes a visual check / checks by eye
> - …that the tutor identifier input matches the tutor identifier on the **original** document
> - Double entry check // the administrator (or a second person) enters the number a second time
> - …and the **system **compares it with the first entry

### Q13
> **[mark-scheme]**
> **1 mark** for each correct method and
> 
> **1 mark** for corresponding description to **max 4**:
> 
> | Method | Description |
> |---|---|
> | Parity byte | An additional bit is added to make the number of 1s in the byte odd or even to match the parity. If a byte with an odd number of 1 bits is received when even parity is used, there is an error. |
> | Parity block | Parity is calculated horizontally and vertically. A parity byte is created from the bits produced by the vertical parity check. This is sent with the data. The parity is re-checked when received and the position of an incorrect bit can be determined. |
> | Checksum | A calculation is made from the data and the result transmitted with the data. The receiver repeats the calculation and compares the result with the value received. If the two are different, there is an error. |

### Q14
**1 mark** for each bullet point each (**max 3**)

- Referential integrity is enforced
- … such as cascade update/delete // if the data is changed in one place it is updated in every other place
- ... and ensures each foreign key has a corresponding primary key

### Q15
> **[mark-scheme]**
> **1 mark** for each correctly completed term:
> 
> - odd or even
> - 7-bits
> - odd
> - block
> - byte
> 
> Computer A and Computer B agree on whether to use **odd or even** parity. Computer A divides the data into groups of **7-bits**. The number of 1s in each group is counted. If the agreed parity is **odd** and the group has an even number of 1s a parity bit of 1 is appended, otherwise a parity bit of 0 is appended.
> 
> In a parity **block **check the bytes are grouped together, for example in a grid. The number of 1s in each column (bit position) is counted. A bit is assigned to each column to make the column match the parity. These parity bits are transmitted with the data as a parity **byte**.
