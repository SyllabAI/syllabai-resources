# Mark Schemes — Data Representation
**1. Information representation** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (43 questions)


### Q1
Step 1, A - B. The two's complement of `00011110` is `11100010`. **[1]**

The carry out of the leftmost column is discarded, so A - B is `01000110`, which is 70. **[1]**

Step 2, subtract C from that result. The two's complement of `01001011` is `10110101`. **[1]**

The final answer is `11111011`, which is -5. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the two's complement of `00011110` given as `11100010`
> 
> **1 mark** for the first result `01000110` // 70
> 
> **1 mark** for the two's complement of `01001011` given as `10110101`
> 
> **1 mark** for the final answer `11111011` and -5
> 
> Accept follow-through into step 2 where the first result is wrong but `10110101` is added to it correctly
> 
> Accept a denary check showing 100 - 30 - 75 = -5
> 
> Accept direct column subtraction with borrows as the working for either step
> 
> Do not accept 251, which is `11111011` read as an unsigned integer
> 
> Do not accept B and C added together first and subtracted in one step, because a mark is set aside for each two's complement

> **[exam-tip]**
> Work one subtraction at a time and carry the 8-bit result forward. Students who convert everything to denary, subtract in denary and then convert the answer back often get the right number but lose the working marks, because two of the four marks are for the two's complements themselves.
> 
> Watch the second step. The intermediate result 70 is smaller than 75, so the final answer must be negative and its leftmost bit must be 1. If your result starts with a 0, check the carries again before you write it down.

### Q2
The two's complement of `01111010` is found by inverting every bit and then adding 1:

**[1]**

The answer as an 8-bit two's complement binary number is `10110010`. **[1]**

The leftmost bit is 1, so the value is negative. `10110010` in denary is -78. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the two's complement of `01111010` given as `10000110`
> 
> **1 mark** for the binary answer `10110010`
> 
> **1 mark** for the denary answer -78
> 
> Accept a direct column subtraction with borrows as the working
> 
> Accept a denary check showing 44 - 122 = -78
> 
> Do not accept 178, which is `10110010` read as an unsigned integer
> 
> Do not accept 78 written without the minus sign

> **[exam-tip]**
> When the number being subtracted is the larger of the two, the answer has to come out negative. Check the leftmost bit of your result is 1 before you go any further; if it is 0, you have made a slip in the addition.
> 
> To turn `10110010` back into denary, take its two's complement (`01001110`, which is 78) and put a minus sign in front. Reading the bits straight off as 178 is the error examiners see most often on this question type.

### Q3
The two's complement of `00010011` is found by inverting every bit and then adding 1:

**[1]**

The carry out of the leftmost column is discarded, so the answer is `01000011`. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the two's complement of `00010011` given as `11101101`
> 
> **1 mark** for the answer `01000011`
> 
> Accept a direct column subtraction with borrows as the working, provided the answer is `01000011`
> 
> Accept a denary check showing 86 - 19 = 67
> 
> Do not accept `11101100`, which is the bits inverted without adding 1
> 
> Do not accept `101000011`, which keeps the ninth bit that should be discarded

> **[exam-tip]**
> Two steps, two marks. Invert every bit, then add 1. Stopping after the inversion is the most common way to lose the first mark, and it also makes the final answer wrong by 1.
> 
> Then remember that the carry falling out of the leftmost column is thrown away, so the answer stays 8 bits long. A 9-bit answer tells the examiner you have not understood that the register is a fixed size.

### Q4
Extended ASCII has only 256 codes, which is far too few for the characters of these four writing systems, while 16-bit Unicode has 65 536 codes **[1]**

Unicode gives every character in every major writing system its own unique code, so a message written in Arabic or Japanese can be stored at all **[1]**

The code for a character is the same everywhere, so a message shows the same characters on the sender's device and on the receiver's device **[1]**

The first 128 Unicode codes are the same as the ASCII codes, so messages already stored in English are still read correctly **[1]**

The drawback is that each character now needs 16 bits instead of 8, so every message takes twice as much storage and twice as much data to transmit **[1]**

**[5 marks]**

> **[mark-scheme]**
> Any five from, and at least one drawback is needed for full marks:
> 
> **1 mark** for extended ASCII having only `256` codes, or for 16-bit Unicode having `65 536`
> 
> **1 mark** for 256 codes being too few for the characters used by Greek, Arabic, Hindi and Japanese together
> 
> **1 mark** for Unicode giving a unique code to the characters of all major writing systems
> 
> **1 mark** for the same code meaning the same character on every device, so the receiver sees the message correctly
> 
> **1 mark** for the first 128 Unicode codes matching ASCII, so messages already stored are unaffected
> 
> **1 mark** for each character needing 16 bits instead of 8
> 
> **1 mark** for the storage needed for a message doubling
> 
> **1 mark** for more data being transmitted, so messages take longer to send or use more bandwidth
> 
> Accept a named example of a character Unicode adds that extended ASCII cannot store, such as an emoji
> 
> Do not accept "Unicode is better" on its own. Accept "Unicode can represent more / a wider range of characters than extended ASCII" for the first marking point
> 
> Do not accept the claim that Unicode makes the application run faster. There is more data to handle, not less

> **[exam-tip]**
> The question asks for benefits and drawbacks, so an answer listing five advantages cannot reach full marks. Plan at least one drawback, and the doubled storage is the obvious one.
> 
> Be precise about what Unicode actually solves. The problem is not that extended ASCII displays foreign text badly; it is that a character with no code cannot be stored at all. Greek, Arabic, Hindi and Japanese together use far more than 256 distinct characters, so extended ASCII has no code to give most of them.
> 
> Avoid vague comparisons such as "Unicode is more modern" or "Unicode is universal". Marks are given for the number of codes, the writing systems covered, or the extra bits per character.

### Q5
**Final answer:** **Addition P causes an overflow. Addition Q does not.**

Addition P:

The value `01011001` is 89 and `00110100` is 52, so the correct sum is 141. **[1]**

Addition Q:

The value `11010011` is -45 and `10110101` is -75, so the correct sum is -120. **[1]**

Addition P overflows. An 8-bit two's complement number can hold -128 to 127, and 141 is greater than 127. Two positive numbers have been added, but the stored result `10001101` has a 1 in the leftmost column, so it reads as -115. **[1]**

Addition Q does not overflow. The value -120 lies inside the range -128 to 127, and the stored result `10001000` is correct. The carry out of the leftmost column is discarded and is not an overflow. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the result of Addition P as `10001101`, or for the correct sum given as 141
> 
> **1 mark** for the result of Addition Q as `10001000`, or for the correct sum given as -120
> 
> **1 mark** for identifying P as the overflow with a reason: 141 is outside the range -128 to 127 // two positive numbers have produced a negative result
> 
> **1 mark** for stating that Q does not overflow with a reason: -120 is inside the range -128 to 127 // the carry out of the leftmost column is discarded and is not an overflow
> 
> Accept the range written as -2<sup>7 to 2</sup>7 - 1
> 
> Accept "the carry into the leftmost column is different from the carry out of it" as the reason for P
> 
> Do not accept "Q overflows because there is a carry out of the leftmost column", because a carry out on its own is not an overflow in two's complement
> 
> Do not accept P being called correct on the grounds that the result still fits in 8 bits, because the value stored is -115 and not 141

> **[exam-tip]**
> The most common error on this topic is treating a carry out of the leftmost column as proof of overflow. In two's complement that carry is discarded and the answer is often still correct, as Addition Q shows.
> 
> Two checks that do work. Adding two positive numbers must give a positive result, and adding two negative numbers must give a negative result, so a wrong sign on the answer means an overflow. A positive number added to a negative number can never overflow at all, so that case needs no test.

### Q6
**(a)**

The range is -128 to +127 **[1]**

**(b)**

8 bits give 2 to the power 8 = 256 different bit patterns, and each pattern stands for exactly one value.

In two's complement only one pattern, 00000000, represents zero. **[1]**

That leaves 255 patterns for the other values. The 128 patterns with a most significant bit of 1 hold the negative values and the remaining 127 patterns hold the positive values, so there is one more negative value than positive value. **[1]**

**(c)**

The range is -127 to +127

In one's complement two patterns represent zero, 00000000 and 11111111, so one pattern fewer is left for the negative values. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the range -128 to +127
> 
> **1 mark** for stating that 8 bits give 256 different patterns and that only one of them, 00000000, represents zero
> 
> **1 mark** for the split of the remaining 255 patterns into 128 negative and 127 positive values
> 
> **1 mark** for the range -127 to +127 together with the reason that one's complement has two representations of zero
> 
> Accept 2 to the power 8 in place of 256
> 
> Accept the answer to part (c) written as -127 to 127
> 
> Accept "zero is counted once and sits on the positive side of the split" for the third mark
> 
> Do not accept -128 to +128, which would need 257 different patterns
> 
> Do not accept -127 to +128 for the two's complement range
> 
> Do not accept "because the most significant bit is negative" on its own for part (b), which does not count the patterns

> **[exam-tip]**
> Count the patterns, not the columns. 8 bits give 256 patterns, zero uses one of them, and 255 does not divide evenly, which is the whole reason the range is lopsided. The commonest wrong answer here is -128 to +128, which quietly asks 8 bits to hold 257 different values.
> 
> It is worth knowing the consequence as well: -128 has no positive partner in 8-bit two's complement. Invert 10000000 and add 1 and you get 10000000 back again, so negating -128 overflows. Examiners like to ask about that in the part that follows.

### Q7
**Final answer:** **8 000 bytes**

The total number of bits is 4 000 x 16 = 64 000 bits **[1]**

There are 8 bits in 1 byte, so divide by 8 **[1]**

64 000 / 8 = 8 000 bytes **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `64 000` bits, or for working shown as `4000 x 16`
> 
> **1 mark** for dividing by `8` to convert bits to bytes
> 
> **1 mark** for the answer `8 000` bytes
> 
> Accept the whole calculation shown on one line as `4000 x 16 / 8`
> 
> Accept `4000 x 2` as the working, since 16 bits is 2 bytes per character
> 
> Award full marks for a correct answer of `8 000` bytes with valid working shown
> 
> Do not award the final mark for `64 000` alone. That is the answer in bits, not in bytes
> 
> Do not accept `4 000` bytes, from using 8 bits per character instead of 16

> **[exam-tip]**
> The mark most often lost here is the last one, from stopping at 64 000 and forgetting the unit conversion. Underline the unit the question asks for before you start, then check your final line carries that unit.
> 
> A fast check is that 16 bits is exactly 2 bytes, so a 16-bit Unicode document always has twice as many bytes as it has characters. 4 000 characters must give 8 000 bytes. If your answer is not double the character count, you have made a slip.

### Q8
The value `11001010` is 202 and `01101001` is 105, so the correct sum is 307. **[1]**

The largest unsigned integer that 8 bits can hold is 255, so 307 cannot be stored in the register. **[1]**

The sum needs 9 bits (`100110011`). The ninth bit is lost, so the register keeps `00110011`, which is 51 and not 307. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the correct sum, given as 307 in denary or as `100110011` in binary
> 
> **1 mark** for stating that the largest unsigned value 8 bits can hold is 255 and that 307 is greater than this
> 
> **1 mark** for the ninth bit being lost, leaving the incorrect value `00110011` // 51
> 
> Accept 2^8 - 1 written in place of 255
> 
> Accept "a carry is produced out of the leftmost column and there is no ninth bit to hold it" for the third mark
> 
> Do not accept 51 offered as the answer to the addition, because the question asks why the addition overflows
> 
> Do not accept a reason based on the range -128 to 127, because these values are unsigned integers

> **[exam-tip]**
> Check whether the integers are unsigned or two's complement before you decide the range. Unsigned 8 bits reach 255, but two's complement 8 bits only reach 127, and the same pair of values can overflow in one representation and not in the other.
> 
> For unsigned addition the test is simple: a carry out of the leftmost column means an overflow has occurred. Do not carry that rule across to two's complement, where a carry out of the leftmost column is normal and is discarded.

### Q9
(a) 16 bits **[1]**

(b) 65 536 characters **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `8`, `16` or `32` in part (a), since Unicode encodings can use 8, 16 or 32 bits per character
> 
> **1 mark** for the number of characters that matches the number of bits given in part (a): `256` for 8 bits, `65 536` for 16 bits, `2^32` for 32 bits
> 
> Accept `2^8`, `2^16` or `2^32` in place of the figure in part (b)
> 
> Accept `65536` written without a space, or with a comma

> **[exam-tip]**
> Unicode can use 8, 16 or 32 bits per character, so more than one answer to part (a) is correct. Whichever you give, part (b) must match it: 8 bits gives 256 characters, 16 bits gives 65 536 and 32 bits gives 2^32.
> 
> If you cannot recall 65 536, work it up from a number you do know. Each extra bit doubles the total, so from 256 at 8 bits you get 512, 1024, 2048, 4096, 8192, 16 384, 32 768 and 65 536 at 16 bits.

### Q10
**(a)**

In two's complement the most significant bit carries a negative place value. For 8 bits that column is -128.

-128 + 32 + 16 + 4 + 2 **[1]**

= -74 **[1]**

**(b)**

In one's complement a most significant bit of 1 shows the value is negative, so invert every bit and read the result as the size of the number.

10110110 inverted is 01001001, which is 73

The value is -73 **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for working that uses -128 as the place value of the most significant bit, or for the alternative method of inverting, adding 1 and then making the result negative
> 
> **1 mark** for -74
> 
> **1 mark** for -73
> 
> Accept working for part (a) that inverts 10110110 to 01001001, adds 1 to give 01001010 = 74, and writes -74
> 
> Do not accept 182, which is the pattern read as an unsigned binary integer
> 
> Do not accept -182, where the 128 column has been treated as positive and a minus sign added at the end
> 
> Do not accept -74 for part (b), as one's complement and two's complement give different denary values for the same negative pattern

> **[exam-tip]**
> The two systems agree on positive numbers and never on negative ones. Once the most significant bit is 1, the two's complement value is always exactly one less than the one's complement value, so -74 and -73 is the pattern to expect. If your two answers come out the same, you have used the same method twice.
> 
> The other frequent error in part (a) is adding 128 + 32 + 16 + 4 + 2 to get 182 and then writing a minus sign in front of it. The most significant column is -128, not 128, so it is subtracted, not negated at the end.

### Q11
An overflow happens when the result of the addition needs more bits than the register has available. **[1]**

The bit that does not fit cannot be stored, so the value that is kept is not the correct answer. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the result needing more bits than are available // the result being larger than the largest value that can be stored in the number of bits available
> 
> **1 mark** for the consequence: the extra bit is lost, so the value stored is incorrect
> 
> Accept "the answer is smaller than the most negative number that can be stored" for the first mark
> 
> Accept "a carry is produced out of the leftmost column and there is no column to hold it" for the first mark
> 
> Do not accept "the number is too big" on its own, because it does not refer to the fixed number of bits, which is what causes the overflow
> 
> Do not accept a description of memory or storage filling up, which is a different idea

> **[exam-tip]**
> Overflow is always about a fixed number of bits, so name that limit in your answer. Write "more bits than the register holds" or "larger than the largest value 8 bits can store", not just "too big", because every number is small enough somewhere.
> 
> The second mark is for saying what goes wrong as a result, so always add the consequence: the stored value is not the correct answer. An answer that stops at the definition scores 1 out of 2.

### Q12
(a) ASCII has only 128 codes, and these are used for the letters, digits, punctuation and control codes needed for English, so no code is left for an accented letter **[1]**

Extended ASCII uses an eighth bit, which gives 256 codes, and the extra 128 codes are used for characters such as accented letters **[1]**

(b) Extended ASCII has a maximum of 256 codes in total, and all of them are already used: 128 for the standard ASCII characters and 128 for extra characters such as accented letters **[1]**

Japanese is written using thousands of different characters, so there are far too few codes available to give every character its own unique code **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Part (a), any two from:**
> 
> - ASCII having only `128` codes, or using 7 bits
> - those 128 codes already being used by English letters, digits, punctuation and control codes
> - extended ASCII using 8 bits, giving `256` codes
> - the extra 128 codes being used for accented or other non-English characters
> 
> **[2 marks]**
> 
> **Part (b), any two from:**
> 
> - extended ASCII having a maximum of `256` codes
> - Japanese using thousands of characters
> - there being more characters than available codes, so each character cannot be given a unique code
> - Unicode being needed instead, as it can use up to 32 bits per character and so provides far more codes, enough for the characters of all languages
> 
> **[2 marks]**
> 
> Accept `2^7` and `2^8` in place of `128` and `256`
> 
> Do not accept "extended ASCII is only for English" in part (a), because extended ASCII does store accented letters; in part (b) accept "extended ASCII only covers a limited set of (European) languages"
> 
> Do not accept an answer to part (b) that says extended ASCII is too slow or uses too much storage. The problem is the number of available codes

> **[exam-tip]**
> An "explain" question needs the reason as well as the fact. Writing "extended ASCII has 256 codes" states a fact; adding "and Japanese uses thousands of characters, so there are not enough codes" is what earns the second mark.
> 
> A common wrong answer to part (b) blames storage space or processing speed. Nothing here is too slow or too large. The code simply runs out of numbers, and a character with no code cannot be stored at all.

### Q13
+37 as an 8-bit unsigned binary integer is 00100101

**(a) One's complement**

Invert every bit.

-37 = 11011010 **[1]**

**(b) Two's complement**

Invert every bit, then add 1.

11011010 + 1 = 11011011

-37 = 11011011 **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for 11011010
> 
> **1 mark** for 11011011
> 
> Accept the two's complement answer reached by the alternative method of copying the bits of 00100101 from the right up to and including the first 1, then inverting the rest
> 
> Do not accept 10100101, which is sign and magnitude, not a complement
> 
> Do not accept the same value given for both parts
> 
> Do not accept 00100101, which is the positive value

> **[exam-tip]**
> The two answers differ by exactly one bit, so it is easy to write the same thing twice or to add the 1 too early. Do the inversion once, write that down as the one's complement answer, and only then add 1 to it for the two's complement answer.
> 
> Check the two's complement answer by adding it to the positive value: 11011011 + 00100101 gives 00000000 in 8 bits, with the carry out of the top column discarded. A negative number and its positive partner must always add to zero.

### Q14
One hexadecimal digit represents exactly 4 bits, so the whole 128-bit address is written as 128 / 4 = 32 hexadecimal digits. **[1]**

The address is divided into eight groups of 16 bits, so each group needs only 4 hexadecimal digits and has a largest value of FFFF. **[1]**

Writing the same address in binary would need all 128 digits, which is far too long for a person to read or type without making a mistake. **[1]**

Hexadecimal maps onto binary exactly, 4 bits to one digit, so any group can be converted back to binary on its own. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for one hexadecimal digit representing 4 bits, giving 32 hexadecimal digits for 128 bits
> 
> **1 mark** for each of the eight groups being 16 bits, so 4 hexadecimal digits per group, with a largest value of FFFF
> 
> **1 mark** for binary needing 128 digits, which is too long for a person to read, write or type accurately
> 
> **1 mark** for the exact mapping of 4 bits to one hexadecimal digit making conversion between the two straightforward
> 
> Accept "an IPv6 address has eight groups whereas an IPv4 address has four groups" as part of the second marking point
> 
> Accept "each group holds a value from 0 to FFFF" for the second marking point
> 
> Do not accept "hexadecimal makes the address smaller", as the address is 128 bits however it is written down
> 
> Do not accept a comparison of how many addresses IPv4 and IPv6 can provide, as the question asks about the notation and not about the size of the address space

> **[exam-tip]**
> A very common answer here explains why IPv6 exists, that it provides more addresses than IPv4, instead of explaining why it is written in hexadecimal. Those are different questions and the address space answer earns nothing. The figures are what earn the marks: 128 bits, 32 hexadecimal digits, eight groups of 4 digits, each group from 0 to FFFF. On a 4-mark "explain" about notation, an answer with no numbers in it rarely gets past two marks.

### Q15
First addition, A + B:

The carry out of the leftmost column is discarded. **[1]**

`01011010` is 90 and `11100111` is -25, so the first result is `01000001`, which is 65. **[1]**

Second addition, the first result + C:

**[1]**

`10111101` is -67, so the second result is `11111110`, which is -2. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for working shown for the first addition, with carries indicated and the carry out of the leftmost column discarded
> 
> **1 mark** for the first result as `01000001` and 65
> 
> **1 mark** for working shown for the second addition, using your own first result
> 
> **1 mark** for the second result as `11111110` and -2
> 
> Accept follow-through on the second addition where the first result is wrong but is added to `10111101` correctly
> 
> Do not accept 254 as the final denary value, which comes from reading `11111110` as an unsigned integer
> 
> Do not accept the three values added in a single column sum, because the question asks for two separate additions

> **[exam-tip]**
> Convert each operand to denary first and keep those values beside your working. That gives you a running check: if the binary result of the first addition does not come to 65, you know to look again before the error is carried into the second addition.
> 
> The second result is the one that catches people out. `11111110` has a 1 in the leftmost column, so it is negative, and it is -2 rather than 254. To convert it, take its two's complement (`00000010`, which is 2) and put a minus sign in front.

### Q16
**(a)**

In BCD each group of four bits represents one denary digit, so each group can only hold a value from 0 to 9. **[1]**

The second group is 1011, which is 8 + 2 + 1 = 11 in denary. There is no denary digit 11, so this group is not a BCD code and the pattern cannot be BCD. **[1]**

**(b)**

Using BCD, the 12 bits hold three denary digits, and the largest denary digit is 9, so the largest value is 999, stored as 1001 1001 1001 **[1]**

Using unsigned binary, all 12 bits are weighted together, so the largest value is 2 to the power 12, minus 1, which is 4095 **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for stating that in BCD each group of four bits represents a single denary digit in the range 0 to 9
> 
> **1 mark** for identifying the group 1011 and giving its denary value of 11
> 
> **1 mark** for 999
> 
> **1 mark** for 4095
> 
> Accept "the codes 1010 to 1111 are not used in BCD" for the first mark
> 
> Accept 2 to the power 12, minus 1, shown as working for 4095
> 
> Do not accept "one of the groups is too big" on its own, which does not identify 1011 or give its value
> 
> Do not accept 4096, which is the number of different bit patterns and not the largest value
> 
> Do not accept 9999, which would need 16 bits in BCD

> **[exam-tip]**
> Name the group and give its value. An answer that says "one of the nibbles is invalid" earns nothing, because the examiner is looking for 1011 and for the number 11. Say which group is at fault and say what it comes to.
> 
> The other reliable mark loss in part (b) is writing 4096 instead of 4095. Twelve bits give 4096 different patterns, but one of those patterns is zero, so the largest value is one less than the number of patterns.

### Q17
An eighth bit is used for each character, so each character is stored in 8 bits instead of 7 **[1]**

The number of different characters that can be stored doubles from 128 to 256 **[1]**

The 128 extra codes are used for characters ASCII does not have, such as accented letters, mathematical operators, symbols such as the copyright sign, and line drawing characters **[1]**

**[3 marks]**

> **[mark-scheme]**
> Any three from:
> 
> **1 mark** for an eighth bit being used, so each character takes 8 bits instead of 7
> 
> **1 mark** for the number of characters doubling, or for `128` becoming `256`
> 
> **1 mark** for naming a type of character the extra codes provide: accented or non-English letters, mathematical operators, symbols such as the copyright sign, or line drawing characters
> 
> **1 mark** for the first 128 codes staying the same as in ASCII, so text already stored is unaffected
> 
> Accept a named example of an accented letter in place of the general term
> 
> Accept "it can store more characters" for the second marking point; a figure (128 to 256) is not required
> 
> Do not accept the claim that all languages can now be stored. 256 codes is not enough for that

> **[exam-tip]**
> "Describe" asks for detail, so a single sentence saying the editor can now store more characters scores only one of the three marks. Put a number in the answer, then say what the new codes are actually used for.
> 
> Be careful not to overclaim. Extended ASCII adds 128 codes, which is enough for the accented letters used in several European languages, but nowhere near enough for a writing system such as Chinese or Japanese. That is what Unicode is for.

### Q18
One hexadecimal digit represents exactly 4 bits, so the 48 bits are written as only 12 hexadecimal digits. **[1]**

A 12-digit value is much shorter than a 48-digit value, so it is easier for a person to read and to write down. **[1]**

Because there are fewer digits, the technician is less likely to copy the address incorrectly. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for one hexadecimal digit representing 4 bits, so 48 bits becomes 12 hexadecimal digits
> 
> **1 mark** for hexadecimal being shorter, so it is easier for a person to read or to write down
> 
> **1 mark** for fewer digits meaning fewer copying errors
> 
> Accept "48 / 4 = 12" as the working for the first marking point
> 
> Accept "takes up less space on the screen or on paper" for the second marking point
> 
> Do not accept "hexadecimal uses less memory" or "the address is stored in hexadecimal", as the device still holds all 48 bits and hexadecimal is only how the value is displayed to a person

> **[exam-tip]**
> The mark most often lost here is the first one, because students answer "hexadecimal is shorter" without saying why. The reason is the exact 4 bits to 1 digit mapping, and quoting the two digit counts, 48 and 12, proves you know it. Be careful with the word "stores" as well. Hexadecimal is a way of writing a value down for a person, not a way of storing it, and an answer that says the computer stores the address in hexadecimal will not gain credit.

### Q19
Only 8 bits are stored, so the carry out of the leftmost column is discarded. **[1]**

The answer as an 8-bit two's complement binary number is `00011101`. **[1]**

`00011101` in denary is 29. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for working shown, with the carry out of the leftmost column discarded
> 
> **1 mark** for the binary answer `00011101`
> 
> **1 mark** for the denary answer 29
> 
> Accept a denary check as the working, showing 105 + (-76) = 29
> 
> Accept the binary answer written in nibbles as `0001 1101`
> 
> Do not accept `100011101`, which keeps the ninth bit when only 8 bits are stored
> 
> Do not accept 285, which comes from reading `10110100` as the unsigned value 180 instead of -76

> **[exam-tip]**
> The carry out of the leftmost column here is not an overflow. Adding a positive number to a negative number can never overflow in two's complement, so that ninth bit is simply thrown away and the 8-bit answer is correct. Writing a 9-bit answer loses the mark.
> 
> Convert the negative operand before you start. `10110100` has a 1 in the leftmost column, so it is negative and equal to -76, not 180. Students who skip that check add 105 and 180 and get an answer that cannot fit in 8 bits at all.

### Q20
**Final answer:** **128 more characters**

Extended ASCII can represent 2<sup>8 = 256 characters, and ASCII can represent 2</sup>7 = 128 characters **[1]**

256 - 128 = 128 more characters **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for both totals, `256` and `128`, or for working shown as 2<sup>8 - 2</sup>7
> 
> **1 mark** for the answer `128`
> 
> Accept `2^7` as the final answer
> 
> Do not accept `1`, from subtracting the number of bits instead of the number of characters
> 
> Do not accept `256` on its own. That is the total number of characters, not the increase

> **[exam-tip]**
> Read whether the question wants the total or the increase. Here it asks how many more characters, so a bare `256` earns nothing.
> 
> Adding one bit doubles the number of codes, it does not add one code. Each extra bit multiplies the number of possible codes by 2, so 7 bits gives 128 and 8 bits gives 256.

### Q21
**(a)**

Each group of four bits is one denary digit.

0111 = 7, 0011 = 3, 0000 = 0, 1001 = 9

The BCD value is 7309 **[1]**

**(b)**

Read as a single unsigned binary integer, every bit has a place value across the whole 16 bits.

16384 + 8192 + 4096 + 512 + 256 + 8 + 1 **[1]**

= 29449 **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for 7309
> 
> **1 mark** for working that shows the correct place values, either the binary column values 16384, 8192, 4096, 512, 256, 8 and 1, or the grouped form (7 x 4096) + (3 x 256) + (0 x 16) + 9
> 
> **1 mark** for 29449
> 
> Accept 28672 + 768 + 0 + 9 as the working
> 
> Accept working that reads the four groups as the hexadecimal value 7309 and then converts that to denary
> 
> Do not accept 7309 as the answer to part (b), which reads the register as BCD a second time
> 
> Do not accept 29449 as the answer to part (a)

> **[exam-tip]**
> The same 16 bits mean two completely different numbers here, and the register itself does not record which one is meant. That is the whole point of the question, so do not carry the grouping from part (a) into part (b).
> 
> In BCD there is no place value of 4096. The bits are grouped, not weighted across the register, which is why 7309 in BCD and 29449 in unsigned binary come from an identical pattern. Students who answer 7309 twice lose two of the three marks.

### Q22
| Hexadecimal value | What it represents |
|---|---|
| 00-1B-44-11-3A-B7 | **A MAC address** |
| #3C8DBC | **A colour code** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for MAC address in the first row
> 
> **1 mark** for colour code in the second row
> 
> Accept "the physical address of a network interface card" for the first row
> 
> Accept "a colour used in a web page" or "an RGB colour value" for the second row
> 
> Do not accept "IP address" for the first row, as an IPv4 address is written in denary separated by full stops and an IPv6 address is written as eight groups separated by colons

> **[exam-tip]**
> Learn to recognise these by their shape and their length. Six pairs of hexadecimal digits separated by hyphens or colons is a MAC address, which is 48 bits. Six hexadecimal digits after a hash is a colour code, which is 24 bits, one byte each for red, green and blue. Eight groups separated by colons is an IPv6 address, which is 128 bits.

### Q23
The carry into each column is shown on the top row. **[1]**

The answer is `10000011`. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for working shown, with the carry into each column indicated
> 
> **1 mark** for the answer `10000011`
> 
> Accept the carry row written above or below the columns, and accept a single carry mark placed against each column
> 
> Accept the answer written in nibbles as `1000 0011`
> 
> Do not accept `10000011` with no working shown, because the working carries its own mark
> 
> Do not accept `01111011`, which is what you get by adding each column and ignoring every carry

> **[exam-tip]**
> The marks split evenly between the working and the answer, so write the carry row down even when you can do the sum in your head. The place students lose the mark is the carry chain that starts in the third column from the right. There `1 + 1` gives `0` carry `1`, and in each of the next four columns one digit is `1`, so that `1` plus the carry again gives `0` carry `1`. It is easy to drop the carry partway along and write `1` instead of `0`. Add one column at a time from the right and note the carry before you move on.

### Q24
(a) `'e'` is 4 letters after `'a'`, so the denary code is 97 + 4 = 101 **[1]**

101 in 7-bit binary is `1100101` **[1]**

(b) An upper-case letter has a code 32 lower than the matching lower-case letter, so `'E'` is 101 - 32 = 69 **[1]**

69 in 7-bit binary is `1000101` **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the denary code `101` for `'e'`, or for working shown as `97 + 4`
> 
> **1 mark** for the binary code `1100101`
> 
> **1 mark** for subtracting `32`, or for the denary code `69` for `'E'`
> 
> **1 mark** for the binary code `1000101`
> 
> Accept working in part (b) that reaches 69 as `65 + 4` instead of `101 - 32`
> 
> Accept a description in part (b) of changing the bit with place value 32 from `1` to `0`
> 
> Accept binary answers padded to 8 bits, `01100101` and `01000101`
> 
> Allow the binary marks to follow through from an incorrect denary value, provided the conversion itself is correct
> 
> Do not accept `5` as the code for `'e'`, which uses the position of the letter in the alphabet
> 
> Do not accept adding 32 in part (b). Upper-case codes are lower than lower-case codes

> **[exam-tip]**
> Getting the direction of the 32 wrong is a common error. Lower case comes second in the ASCII table, so its codes are the higher ones: to go from lower case to upper case you subtract 32, and to go the other way you add 32. Check the direction against the table in the question, where `'A'` is 65 and `'a'` is 97.
> 
> Watch the off-by-one as well. `'e'` is the fifth letter of the alphabet but it is only 4 places after `'a'`, so the code is `97 + 4`, not `97 + 5`.
> 
> The row for `'0'` is in the table as a reminder of a separate trap: the character `'0'` has the ASCII code 48, not the binary value 0. A digit typed on a keyboard is a character like any other.

### Q25
**(a)**

Each denary digit is written as its own 4-bit code.

5 = 0101, 0 = 0000, 7 = 0111

507 = 0101 0000 0111 **[1]**

**(b)**

Each group of four bits is read as one denary digit.

1000 = 8, 0010 = 2, 0110 = 6

1000 0010 0110 = 826 **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for 0101 0000 0111
> 
> **1 mark** for 826
> 
> Accept the BCD answer written without spaces as 010100000111
> 
> Do not accept 111111011, which is 507 written as a pure unsigned binary integer rather than in BCD
> 
> Do not accept 2086, which is the 12 bits of part (b) read as a single unsigned binary integer
> 
> Do not accept any answer to part (a) where a leading zero has been dropped from a 4-bit code, for example 101 0 111

> **[exam-tip]**
> BCD is not the same as converting the whole number into binary. Work on one denary digit at a time, and always write four bits for every digit including the leading zeros: the digit 0 is 0000, not a gap, and the digit 5 is 0101, not 101. Dropping one leading zero shifts every group after it and loses the mark.
> 
> Count your bits before you finish. A three-digit denary number must give exactly 12 bits in BCD, and a 12-bit BCD value must give exactly three denary digits.

### Q26
Each of the four denary digits is stored in its own group of 4 bits. **[1]**

Each group of 4 bits can be sent straight to one digit of the display, so the value does not have to be converted from pure binary into denary before it is shown. **[1]**

This makes the circuit that drives the display simpler and faster. **[1]**

One disadvantage is that BCD needs more bits than pure binary to store the same value. In 16 bits, BCD can hold values from 0 to 9999, but unsigned binary can hold values from 0 to 65535. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for each denary digit being stored in its own group of 4 bits
> 
> **1 mark** for each group being sent directly to one digit of the display, with no conversion from binary to denary needed
> 
> **1 mark** for the benefit that follows: the display circuitry is simpler, faster or cheaper
> 
> **1 mark** for one correct disadvantage, from:
> 
> - BCD uses more bits than pure binary for the same value, for example 16 bits holds up to 9999 in BCD but up to 65535 in unsigned binary
> - 6 of the 16 possible 4-bit codes, 1010 to 1111, are never used, so storage is wasted
> - arithmetic on BCD values is more complex and slower than arithmetic on pure binary
> 
> Do not accept "BCD is harder to read" as the disadvantage, as BCD is easier for a person to read than pure binary
> 
> Do not accept a disadvantage that only restates one of the first three marking points

> **[exam-tip]**
> The disadvantage is the mark most often dropped, because students write that BCD is less accurate. BCD is more accurate for denary values, not less. Its real costs are wasted storage and slower arithmetic, and a figure makes the point land: four digits take 16 bits in BCD, and those same 16 bits would hold any value up to 65535 in pure binary.

### Q27
One hexadecimal digit represents exactly four binary digits, because 16 = 2 to the power 4. The bits must therefore be taken in groups of four. **[1]**

The grouping must start from the right-hand end, so that any zeros added to fill a group are added at the left, where they do not change the value. Adding two zeros on the right multiplies the value by 4. **[1]**

1011011110 in denary is 512 + 128 + 64 + 16 + 8 + 4 + 2 = 734

B78 in denary is (11 x 256) + (7 x 16) + 8 = 2936, and 2936 = 4 x 734, so the student's value is four times too large **[1]**

Grouping correctly from the right and padding at the left gives 0010 1101 1110

0010 = 2, 1101 = 13 = D, 1110 = 14 = E

1011011110 = 2DE **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for stating that one hexadecimal digit represents four bits, or that 16 = 2 to the power 4
> 
> **1 mark** for stating that the grouping starts from the right and that padding zeros go at the left
> 
> **1 mark** for showing the student's answer is wrong by value, either by converting both to denary (734 against 2936) or by stating that two zeros added on the right multiply the value by 4
> 
> **1 mark** for 2DE
> 
> Accept 0x2DE or 2DE with a subscript 16
> 
> Accept the third mark for converting B78 back to binary as 101101111000 and pointing out that it has 12 bits, two more than the number given
> 
> Do not accept "the student grouped from the wrong end" on its own for the third mark, as this repeats the stem without showing that the value has changed
> 
> Do not accept B72, which comes from the same wrong grouping with the final group read as 10

> **[exam-tip]**
> Always group binary digits from the right-hand end. If the number of bits is not a multiple of four, the zeros you add to complete the last group belong at the left. A zero written on the right is not padding, it is a shift, and every zero added there doubles the number.
> 
> The safe check takes ten seconds: convert your hexadecimal answer back into denary and convert the original binary into denary as well. If the two do not match you have grouped from the wrong end.

### Q28
| Character | ASCII code (denary) | ASCII code (7-bit binary) |
|---|---|---|
| 'A' | 65 | 1000001 |
| 'C' | 67 | **1000011** **[1]** |
| 'H' | **72** **[1]** | 1001000 |
| 'J' | 74 | **1001010** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `1000011` as the binary code for `'C'`
> 
> **1 mark** for `72` as the denary code for `'H'`
> 
> **1 mark** for `1001010` as the binary code for `'J'`
> 
> Accept a binary answer written with a space, `100 0011` and `100 1010`
> 
> Accept a binary answer padded to 8 bits with a leading zero, `01000011` and `01001010`
> 
> Do not accept `3`, `8` or `10` as the denary codes, which use the position of the letter in the alphabet instead of the ASCII code

> **[exam-tip]**
> Two errors cost most of the marks on this type of question. The first is giving the position of the letter in the alphabet, so `'C'` becomes `3` rather than `67`. The second is counting from the wrong place when working out a code: `'H'` is 7 letters after `'A'`, not 8, so it is `65 + 7 = 72`.
> 
> Convert the denary value to binary in the usual way using the column headings 64, 32, 16, 8, 4, 2, 1. Every upper-case letter in this table starts with a `1` in the 64 column, which is a quick check that you have not made a mistake.

### Q29
Each denary digit of the amount is stored in its own group of 4 bits. **[1]**

This means the amount is held as the exact denary digits that the customer sees, so a value such as an amount of money is stored exactly. **[1]**

In pure binary it is difficult to represent decimal values exactly, so small rounding errors would build up over many transactions. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for each denary digit being held in its own group of 4 bits
> 
> **1 mark** for the amount being stored exactly, with no loss of accuracy in the denary digits
> 
> **1 mark** for pure binary not representing decimal values exactly, so errors would accumulate over many calculations
> 
> Accept "money must be accurate to two decimal places and BCD keeps that accuracy" for the second marking point
> 
> Accept "rounding errors are avoided" for the third marking point
> 
> Do not accept "BCD is faster than binary", as arithmetic on BCD values is slower than arithmetic on pure binary
> 
> Do not accept "BCD uses less storage", as BCD uses more bits than pure binary to store the same value

> **[exam-tip]**
> The answer that loses marks here is "BCD is used because it is easier for the computer". It is the other way round. BCD is easier for people and for displays and harder for the processor, and it is chosen for money in spite of being less efficient, because getting the digits exactly right matters more than speed or storage. Say what is stored in each group of 4 bits, then say what pure binary would get wrong.

### Q30
**8-bit unsigned binary**

Take each column value in turn, largest first:

173 - 128 = 45, so the 128 column holds 1

45 is smaller than 64, so the 64 column holds 0

45 - 32 = 13, so the 32 column holds 1

13 is smaller than 16, so the 16 column holds 0

13 - 8 = 5, so the 8 column holds 1

5 - 4 = 1, so the 4 column holds 1

1 is smaller than 2, so the 2 column holds 0

1 - 1 = 0, so the 1 column holds 1

173 = 10101101 **[1]**

**Hexadecimal**

173 / 16 = 10 remainder 13 **[1]**

10 is written as A and 13 is written as D

173 = AD **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for 10101101
> 
> **1 mark** for working that divides by 16 to give 10 remainder 13, or that splits the binary answer into the nibbles 1010 and 1101
> 
> **1 mark** for AD
> 
> Accept the hexadecimal answer written as 0xAD or with a subscript 16
> 
> Accept a place-value table in place of the repeated subtraction, provided the 1 bits are in the 128, 32, 8, 4 and 1 columns
> 
> Do not accept 1013 or 10 13, where the quotient and the remainder have been written as denary numbers rather than converted to single hexadecimal digits
> 
> Do not accept DA, the two hexadecimal digits in the wrong order

> **[exam-tip]**
> The error to avoid is finishing the division and stopping there. 173 / 16 gives 10 remainder 13, and both of those numbers still have to become single hexadecimal digits, A and D, before you write the answer down. An answer of 1013 is the most common wrong response to this question.
> 
> If you have already produced the binary answer, use it. Split 10101101 into 1010 and 1101, read each nibble as a denary value of 10 and 13, and write A and D. It is faster than dividing and it gives you a second check on the binary answer at the same time.

### Q31
(a) 7 bits **[1]**

(b) 128 characters **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `7` in part (a)
> 
> **1 mark** for `128` in part (b)
> 
> Accept `2^7` in place of `128` in part (b)
> 
> Accept `8` in part (a), since ASCII can be stored using 7 or 8 bits per character
> 
> Accept `256` in part (b) only as follow-through from `8` bits in part (a)

> **[exam-tip]**
> ASCII is a 7-bit code, although a character is usually stored in one 8-bit byte, so 7 or 8 bits is credited. Keep the two pairs of numbers together in your memory as pairs: 7 bits gives 128 characters, 8 bits (extended ASCII) gives 256 characters. Mixing the pairs, such as 7 bits with 256 characters, loses a mark.
> 
> Note also that 128 is the total number of different codes in the set, not the number of letters. Digits, punctuation and control codes all take up codes as well.

### Q32
An electronic calculator **[1]**

A digital clock **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for each of two correct applications, to a maximum of 2
> 
> Accept a digital watch // a digital display that shows separate denary digits, such as a weighing scale // a banking or financial system that stores amounts of money // the storage of the date and time in the BIOS of a computer
> 
> Accept a till or a point of sale terminal as a financial system
> 
> Do not accept MAC addresses, colour codes or memory addresses, which are applications of hexadecimal and not of BCD
> 
> Do not accept "a computer" on its own, as it does not name an application

> **[exam-tip]**
> BCD and hexadecimal are taught together, and the two lists of applications get swapped in the exam more often than any other pair on this topic. Fix the split in your head: BCD is used where separate denary digits have to be shown or stored exactly, so calculators, clocks and money. Hexadecimal is used where a long binary value has to be written down for a person to read, so MAC addresses, colour codes and IPv6 addresses.

### Q33
| Value | Written in | Convert to | Answer |
|---|---|---|---|
| 00110110 | unsigned binary | denary | **54** |
| 2F | hexadecimal | 8-bit unsigned binary | **00101111** |

32 + 16 + 4 + 2 = 54 **[1]**

2 = 0010 and F = 1111, so 2F = 00101111 **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for 54
> 
> **1 mark** for 00101111
> 
> Accept 101111 for the second answer only if the two leading zeros are shown elsewhere in the working, as the question asks for 8 bits
> 
> Do not accept 47 as the second answer, which is the denary value of 2F and not its binary form
> 
> Do not accept 110110 read as a denary number

> **[exam-tip]**
> For hexadecimal to binary, do not go through denary. One hexadecimal digit is always exactly four binary digits, so convert each digit on its own and join the two nibbles together. The mark is most often lost by dropping the leading zero of the first nibble and writing a 6-bit answer when the question asked for 8 bits.

### Q34
The manufacturer uses the decimal prefix giga, so 1 GB means 10^9 bytes. **[1]**

The operating system uses the binary prefix gibi, so 1 GiB means 2^30 = 1 073 741 824 bytes. **[1]**

The drive holds the same number of bytes in both cases. Only the size of the unit has changed, so the number in front of it changes.

500 x 10^9 = 500 000 000 000 bytes **[1]**

500 000 000 000 / 1 073 741 824 = 465.66... **[1]**

which rounds to 466 GiB

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for stating the manufacturer uses a decimal prefix, 1 GB = 10^9 bytes
> 
> **1 mark** for stating the operating system uses a binary prefix, 1 GiB = 2^30 = 1 073 741 824 bytes
> 
> **1 mark** for converting the advertised capacity to 500 000 000 000 bytes
> 
> **1 mark** for dividing by 1 073 741 824 to reach a value of approximately 465.7
> 
> Accept any answer in the range 465 to 466 for the final value
> 
> Accept an explanation that the drive is not faulty and no storage has been lost, provided the decimal and binary prefix definitions are both given
> 
> Do not credit an answer that says the missing space is used by the operating system or by formatting, as this does not explain the figures given

> **[exam-tip]**
> This is the one place where the prefix distinction has a consequence students actually notice, and examiners like it for that reason. The trap is answering that the difference is caused by system files taking up space. That is a real effect but it is not what this question is about: the same physical drive is being measured in two different units, and no bytes have gone anywhere.

### Q35
**Final answer:** **3 MiB**

First write down the number of bytes in 1 MiB

1 MiB = 2^20 = 1 048 576 bytes

Then divide the file size by that value

3 145 728 / 1 048 576

3

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for stating 1 MiB = 2^20 or 1 048 576 bytes
> 
> **1 mark** for dividing 3 145 728 by 1 048 576
> 
> **1 mark** for the answer 3 MiB
> 
> Accept the working shown as 3 145 728 / 2^20
> 
> Award full marks for a correct answer of 3 MiB with valid working shown
> 
> Do not award the final mark for an answer of 3 alone, with no unit

> **[exam-tip]**
> Dividing by 1 000 000 instead of 1 048 576 gives 3.145728, which looks like a plausible answer and earns nothing. If the question says MiB, KiB or GiB, you must divide by a power of 2. A quick sanity check is that the answer in MiB should always be slightly smaller than the answer in MB.

### Q36
| Prefix | Symbol | Value as a power of 2 | Value in bytes |
|---|---|---|---|
| kibi | KiB | **2^10** | **1024** |
| mebi | MiB | **2^20** | **1 048 576** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for 2^10 and 1024 in the kibi row
> 
> **1 mark** for 2^20 and 1 048 576 in the mebi row
> 
> Both cells in a row must be correct for the mark
> 
> Accept 1 048 576 written with or without spaces or commas
> 
> Do not accept 1000 or 1 000 000, which are the values of the decimal prefixes kilo and mega

> **[exam-tip]**
> The binary prefixes all end in -bi and are powers of 2, while the decimal prefixes kilo, mega and giga are powers of 10. The two are close enough to look interchangeable and far enough apart to lose you the mark, so read the symbol carefully: KiB is not KB.

### Q37
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

### Q38
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

### Q39
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

### Q40
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

### Q41
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

### Q42
> **[mark-scheme]**
> **1 mark** for identification **1 mark** for matching description
> 
> e.g.
> 
> - ASCII
> - 7/8 bits per character // represents 128/256 characters // represents all characters from Latin alphabet
> - UNICODE
> - 8/16/32 bits per character // represents 256/65536+ characters // represents all characters in all languages

### Q43
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
