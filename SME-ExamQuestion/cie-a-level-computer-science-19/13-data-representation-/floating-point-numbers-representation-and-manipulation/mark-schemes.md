# Mark Schemes — Floating-point Numbers, Representation & Manipulation
**13. Data Representation** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (21 questions)


### Q1
The exponent `0110` is 6, so the binary point moves 6 places to the right. **[1]**

The mantissa begins with 1, so it is negative. Taking the two's complement of the whole mantissa gives `011001100000`, because flipping the bits gives `011001011111` and adding 1 gives `011001100000`. That is a magnitude of 0.796875. **[1]**

0.796875 × 64 = 51, so the value is -51. **[1]**

The student treated the leading 1 of the mantissa as a sign flag and read the remaining bits `00110100000` as the magnitude, giving 0.203125 × 64 = 13 and an answer of -13. In two's complement the leading bit is not a flag: it carries a place value of -1. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the exponent 6 // for evidence that the binary point moves 6 places
> 
> **1 mark** for the magnitude of the mantissa found correctly, either as the two's complement `011001100000` = 0.796875, or by place value as -1 + 1/8 + 1/16 + 1/64 = -0.796875
> 
> **1 mark** for the answer -51
> 
> **1 mark** for identifying the mistake as reading the mantissa in sign-and-magnitude form // for stating that the leading mantissa bit has a place value of -1 and is not a sign flag // for stating that the two's complement of the mantissa was not taken
> 
> Accept -51.0.
> 
> Do not accept 38.5 as the value. That comes from reading all 12 mantissa bits as an unsigned fraction.
> 
> Do not accept "the student used the wrong exponent" for the final mark. The exponent is 6 and the student applied 6 correctly, because 0.203125 × 64 = 13.
> 
> Do not accept "the student forgot the minus sign" for the final mark. The student's answer is already negative.

> **[exam-tip]**
> A two's complement mantissa has no separate sign flag. The leading bit is a place value worth -1, so `100110100000` is -1 + 0.203125 and not -0.203125. The gap between -51 and -13 comes entirely from that one misreading.
> 
> Pick one method and finish it. Either give the leading bit a place value of -1 and add the rest, or flip all 12 bits, add 1, read the result as a positive fraction and put the minus sign back at the end. Doing half of each, by flipping the bits and then also treating the leading bit as -1, gives a wrong answer every time.

### Q2
The exponent `111111` is in two's complement form, so it is -1 and not 63. **[1]**

The mantissa begins with 1, so it is negative. Its leading bit has a place value of -1, giving -1 + 1/4 + 1/8 = -0.625. **[1]**

A negative exponent moves the binary point to the left. Moving it 1 place to the left halves the mantissa, so the value is -0.625 / 2 = -0.3125. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the exponent -1 // for `111111` identified as a negative two's complement value
> 
> **1 mark** for the mantissa -0.625 // for -1 + 1/4 + 1/8 seen // for the two's complement route, flipping `1011000000` to `0100111111` and adding 1 to give `0101000000`, a magnitude of 0.625
> 
> **1 mark** for the answer -0.3125
> 
> Accept -5/16.
> 
> Do not accept -1.25. That comes from reading the exponent as +1 instead of -1.
> 
> Do not accept -0.1875. That comes from reading the mantissa as sign and magnitude, taking the bits after the sign bit as 0.375 instead of taking the two's complement.
> 
> Do not accept a very large negative answer of nineteen digits. That comes from reading the exponent `111111` as unsigned 63 instead of -1.

> **[exam-tip]**
> Both fields are two's complement, not just the mantissa. An exponent whose first bit is 1 is negative, so `111111` is -1. Students who read it as 63 produce an answer with nineteen digits and do not stop to ask whether that can be right.
> 
> A negative exponent makes the number smaller in magnitude. It does not make the number negative. The sign of the answer comes from the mantissa alone, and here both happen to be negative while doing two different jobs.

### Q3
The exponent `00000100` is 4, so the binary point moves 4 places to the right. **[1]**

The mantissa is `0.1101`, which is 1/2 + 1/4 + 1/16 = 0.8125. Moving the binary point 4 places gives `1101.0`, so the value is 13. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the exponent 4 // for evidence that the binary point moves 4 places // for 1/2 + 1/4 + 1/16 = 13/16 seen
> 
> **1 mark** for the answer 13
> 
> Accept 13.0 and `1101`.
> 
> Do not accept 6.5. That comes from reading the mantissa as `0.01101`, putting the binary point before the sign bit instead of after it.
> 
> Do not accept 26. That comes from moving the binary point 5 places instead of 4.

> **[exam-tip]**
> The sign bit is not part of the fraction. In `01101000` the binary point sits after the first bit, so the fraction is 0.1101 and not 0.01101. Reading it the wrong way halves every answer, which is why 6.5 turns up so often on this question type.
> 
> Trailing zeros in the mantissa are padding. Write out the shifted bit pattern first, then add up the place values, rather than trying to do both steps at once.

### Q4
45.5 in binary is `101101.1`, because 32 + 8 + 4 + 1 + 0.5 = 45.5. **[1]**

Moving the binary point 6 places to the left gives 0.1011011 × 2<sup>6</sup>, so the exponent is 6 in both systems. **[1]**

**System 1 mantissa**

| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|

**System 1 exponent**

| 0 | 0 | 0 | 1 | 1 | 0 |
|---|---|---|---|---|---|

**[1]**

**System 2 mantissa**

| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|

**System 2 exponent**

| 0 | 1 | 1 | 0 |
|---|---|---|---|

**[1]**

The seven fraction bits `1011011` are the same in both systems. Only the padding changes: the mantissa gains zeros on the right, and the exponent gains copies of its sign bit on the left.

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for converting 45.5 to binary as `101101.1` // for 32 + 8 + 4 + 1 + 0.5 seen
> 
> **1 mark** for the exponent 6 // for evidence that the binary point moves 6 places // for 0.1011011 × 2<sup>6</sup> seen
> 
> **1 mark** for the System 1 answer, mantissa `0101101100` with exponent `000110`
> 
> **1 mark** for the System 2 answer, mantissa `010110110000` with exponent `0110`
> 
> Accept 91/128 multiplied by 64 as working for the value of the mantissa.
> 
> Do not accept `0110` as the System 1 exponent or `000110` as the System 2 exponent. The exponent value is 6 in both, but the field is 6 bits wide in System 1 and 4 bits wide in System 2.
> 
> Do not accept a System 2 mantissa of `0101101100`. That is only 10 bits. System 2 needs 12, and the two extra zeros go on the right-hand end.

> **[exam-tip]**
> Convert the number once and find the exponent once. Changing the split does not change the arithmetic, so all that is left is to write the same fraction and the same exponent into fields of a different width.
> 
> Pad in the right direction. Zeros go on the right-hand end of the mantissa, because bits further past the binary point are worth less. The exponent is padded on the left with copies of its sign bit, so 6 becomes `000110` or `0110`, and a negative exponent such as -1 becomes `111111` or `1111`. Students who pad the exponent on the right turn 6 into 24.

### Q5
0.34375 in binary is `0.01011`, because 1/4 + 1/16 + 1/32 = 0.34375. **[1]**

A normalised mantissa must have its first two bits different, so the binary point moves 1 place to the right and the exponent is -1. In 6-bit two's complement, -1 is `111111`. **[1]**

The positive mantissa is `0101100000`. Take the two's complement of the whole mantissa: flip the bits to give `1010011111`, then add 1 to give `1010100000`. **[1]**

**Mantissa**

| 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|

**Exponent**

| 1 | 1 | 1 | 1 | 1 | 1 |
|---|---|---|---|---|---|

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for converting 0.34375 to binary as `0.01011` // for 1/4 + 1/16 + 1/32 seen // for 11/32 seen
> 
> **1 mark** for the exponent `111111` // for identifying the exponent as -1 // for evidence that the binary point moves 1 place
> 
> **1 mark** for the mantissa `1010100000`
> 
> Accept the mantissa reached by place value instead of by two's complement: -1 + 1/4 + 1/16 = -0.6875, and -0.6875 halved is -0.34375.
> 
> Do not accept `000001` for the exponent. That is +1 and makes the number -1.375.
> 
> Do not accept `1101100000` for the mantissa. That is a sign-and-magnitude pattern, it begins `11` so it is not normalised, and it stores -0.15625.
> 
> Do not accept `1010011111` for the mantissa. That is the flip step with the add 1 missing, and it stores -0.3447265625.

> **[exam-tip]**
> A number smaller than 0.5 needs a negative exponent, and this is where the marks go. Students convert the value correctly, then write a positive exponent out of habit. Decide the sign by asking which way the binary point moved: to the right means a negative exponent.
> 
> When you take the two's complement, complement all ten bits including the sign bit, then add 1. Flipping and stopping there leaves you one unit short in the last place. It produces -0.3447265625, an answer close enough to look right and worth no marks.

### Q6
5.5 in binary is `101.1`, because 4 + 1 + 0.5 = 5.5.

Moving the binary point 3 places to the left gives 0.1011 × 2<sup>3</sup>, so the exponent is 3.

**Mantissa**

| 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|

**[1]**

**Exponent**

| 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
|---|---|---|---|---|---|---|---|

**[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the mantissa `01011000`
> 
> **1 mark** for the exponent `00000011`
> 
> Accept working shown as 5.5 = `101.1` = 0.1011 × 2<sup>3</sup>, or as 4 + 1 + 0.5, or as 11/16 × 8.
> 
> Do not accept `10110000` for the mantissa. Dropping the sign bit shifts every digit one place to the left, and because the leading bit then has a place value of -1 the pattern stores -5, not +5.5.
> 
> Do not accept `11111101` for the exponent. That is -3 in two's complement and makes the number 0.0859375.

> **[exam-tip]**
> The binary point sits immediately after the sign bit, so a positive normalised mantissa always starts `01` and a negative one always starts `10`. Writing the fraction bits hard against the left-hand end, as `10110000`, is the most common error here and it silently turns a positive number into a negative one.
> 
> Count the exponent as the number of places the binary point moves, not as the number of digits in the binary number. Pad the mantissa with zeros on the right, never on the left.

### Q7
The mantissa begins `111`, so its first two bits are the same and the number is not normalised. The mantissa is moved 2 places left and 2 is subtracted from the exponent, which changes from 5 to 3. **[1]**

**Mantissa**

| 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|

**[1]**

**Exponent**

| 0 | 0 | 0 | 0 | 1 | 1 |
|---|---|---|---|---|---|

**[1]**

The leading bits that simply repeat the sign bit carry no information. Shifting them out lets the mantissa hold more significant bits, so the number is stored to the greatest precision the mantissa allows. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the mantissa begins `11` // the first two bits are the same, together with the mantissa being moved 2 places left or the exponent being reduced by 2
> 
> **1 mark** for mantissa `1011000000`
> 
> **1 mark** for exponent `000011`
> 
> **1 mark** for a reason: the mantissa holds more significant bits once the repeated leading bits are removed // the number is stored to the greatest precision available for that number of mantissa bits
> 
> Accept accuracy in place of precision. Accept for the last mark: each number then has only one stored form, which makes comparison and arithmetic simpler.
> 
> Do not accept mantissa `1101100000` with exponent `000100`. One shift keeps the value correct but the mantissa still begins `11`.
> 
> Do not accept mantissa `0110000000`. Shifting a third time pushes the sign bit out and turns a negative number into a positive one.
> 
> Do not accept the claim that normalising makes the number smaller or more compact. The stored value is unchanged by normalising.

> **[exam-tip]**
> A negative mantissa is where this goes wrong. Students see the leading 1s and stop shifting as soon as one disappears, or they keep shifting until the mantissa starts with a 0 and silently change the sign of the number. Shift until the first two bits differ, then stop: for a negative number that is `10`.
> 
> Check the exponent in the same direction every time. Two places left means 2 taken off the exponent, so 5 becomes 3.

### Q8
The mantissa is moved 3 places left, so 3 is subtracted from the exponent. The exponent changes from 7 to 4. **[1]**

**Mantissa**

| 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|

**[1]**

**Exponent**

| 0 | 0 | 0 | 1 | 0 | 0 |
|---|---|---|---|---|---|

**[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for working: mantissa moved 3 places left // exponent reduced by 3 // exponent 7 changed to 4
> 
> **1 mark** for mantissa `0110100000`
> 
> **1 mark** for exponent `000100`
> 
> Accept 4 written in denary for the exponent working, and accept zeros filled in from the right of the mantissa as shown.
> 
> Do not accept exponent `001010`. That is 10, from adding 3 instead of subtracting 3, and it stores 832 in place of the original value of 13.
> 
> Do not accept mantissa `0011010000` with exponent `000101`. Two shifts keeps the value correct but the mantissa still begins `00`, so it is not yet normalised.

> **[exam-tip]**
> Almost every lost mark here is the direction of the exponent change. Moving the mantissa left multiplies it, so the exponent must come down by the same number of places to keep the value the same. Adding instead of subtracting turns 13 into 832.
> 
> Keep shifting until the first two bits are different, not just until the leading zeros look tidy. Stopping one place early leaves `0011010000`, which is still not normalised.

### Q9
The first two bits of the mantissa are the same, both 1, so the mantissa does not begin `01` or `10`. **[1]**

The mantissa of a normalised negative number must begin `10`. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the mantissa does not begin `01` or `10` // the mantissa begins `11` // the first two digits are the same
> 
> **1 mark** for `10`
> 
> Accept for the second mark: the bit after the sign bit must be 0.
> 
> Do not accept the mantissa starts with a 1 so it is negative. Being negative does not stop a number being normalised; a normalised negative mantissa also starts with a 1.
> 
> Do not accept the number is too small. The size of the number is not the test; the two leading bits are.

> **[exam-tip]**
> The mistake here is checking only the sign bit. A mantissa starting `1` may be perfectly normalised, so long as the next bit is `0`. The test is always the same whatever the sign: the first two bits of the mantissa must be different.
> 
> Learn the two normalised openings as a pair, `01` for a positive number and `10` for a negative one. Anything starting `00` or `11` still has bits that repeat the sign and can be shifted left.

### Q10
System X has an 8-bit exponent, so its exponent runs from -128 to +127. **[1]**

System Y has a 4-bit exponent, so its exponent runs only from -8 to +7. **[1]**

System X can therefore represent a far wider range of numbers, because the exponent alone sets how large or how small a value can be. **[1]**

System Y holds 11 bits after the sign bit in its mantissa, against 7 in System X, so System Y represents a number to greater precision. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for System X exponent range -128 to +127
> 
> **1 mark** for System Y exponent range -8 to +7
> 
> **1 mark** for System X can represent a much wider range of numbers // System Y can represent only a narrow range
> 
> **1 mark** for System Y stores numbers to greater precision // System Y has more mantissa bits so it is more accurate
> 
> Accept accuracy in place of precision throughout.
> 
> Accept 11 and 7 for the number of mantissa bits after the sign bit, or 12 and 8 for the whole mantissa, provided the comparison is the right way round.
> 
> Do not accept the claim that System Y can store larger numbers because it has more mantissa bits. The mantissa is a fraction between -1 and 1; only the exponent sets the range.
> 
> Do not accept an answer that gives only one of the two effects. Both range and precision are needed.

> **[exam-tip]**
> Students often answer that more mantissa bits means bigger numbers. It does not. The mantissa is a fraction between -1 and 1, so it never makes the value larger on its own. Giving bits to the exponent buys range; giving bits to the mantissa buys precision, and with a fixed total you can only buy one by selling the other.
> 
> When the question asks for the exponent range, give both ends as denary numbers. An n-bit two's complement field runs from minus 2 to the power (n minus 1), up to 2 to the power (n minus 1) minus 1.

### Q11
The largest exponent is `0111`, which is +7, so both limits use a multiplier of 128. **[1]**

Largest positive value: the largest mantissa is `011111111111`, which is 2047/2048. 2047/2048 × 128 = 128 - 1/16 = **127.9375** **[1]**

Most negative value: the smallest mantissa is `100000000000`, which is exactly -1. -1 × 128 = **-128** **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for identifying the largest exponent as 7, or for a multiplier of 128 seen in the working
> 
> **1 mark** for 127.9375
> 
> **1 mark** for -128
> 
> Accept 2047/16 or 128 - 1/16 for 127.9375. Accept the bit patterns `011111111111` `0111` and `100000000000` `0111` as the working mark.
> 
> Do not accept 128 for the largest positive value. The mantissa is always smaller than 1, so the product is always smaller than 128.
> 
> Do not accept -127.9375 for the most negative value. The mantissa reaches exactly -1 on the negative side but only reaches 2047/2048 on the positive side, so the two limits are not a matching pair.
> 
> Do not accept 32752, which comes from reading the 4-bit exponent field as unsigned and using an exponent of 15.

> **[exam-tip]**
> The common mistake is to assume the two limits are symmetrical and write 128 and -128. Work with the mantissa as a fraction instead. The largest positive mantissa is one step below 1, so the largest positive value lands one step below 128, while the mantissa `100000000000` is exactly -1, so -128 is reached exactly.
> 
> The other mistake is treating the exponent field as unsigned. Four two's complement bits run from -8 to +7, not 0 to 15.

### Q12
Largest exponent: +31 **[1]**

Smallest exponent: -32 **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for largest exponent = 31
> 
> **1 mark** for smallest exponent = -32
> 
> Accept the bit patterns `011111` and `100000` in place of the denary values.
> 
> Do not accept 63 for the largest exponent. That is the largest value of six unsigned bits and it ignores the sign bit.
> 
> Do not accept -31 for the smallest exponent. A two's complement field is not symmetrical: it holds one more negative value than it holds values from zero upwards.

> **[exam-tip]**
> The mark is usually lost by reading the exponent field as an unsigned number and answering 0 to 63. Every Cambridge stem tells you the exponent is in two's complement form, so the leftmost bit of the field is a sign bit.
> 
> Watch the asymmetry as well. Six bits give 64 patterns, shared out as 32 negative exponents and 32 exponents from 0 upwards, so the field reaches -32 but only reaches +31.

### Q13
In normalised form the reading is 0.10101100111 x 2<sup>7</sup>, so the mantissa would need 11 significant binary digits plus a sign bit, which is 12 bits. **[1]**

The original mantissa holds only 10 bits, so the 2 least significant digits `11` are truncated. The value stored is 86.25 rather than 86.4375, which is a rounding error. **[1]**

With a 12-bit mantissa there is room for the sign bit and all 11 digits, so the reading is then stored exactly. **[1]**

The cost is range. A 6-bit two's complement exponent covers -32 to +31, but a 4-bit one covers only -8 to +7, so the system can no longer represent very large or very small numbers. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for stating that the normalised mantissa needs 11 significant digits plus a sign bit, which is 12 bits
> 
> **1 mark** for stating that the 10-bit mantissa truncates the least significant digits, so precision is lost or a rounding error occurs
> 
> **1 mark** for stating that a 12-bit mantissa holds every digit of this reading, so it would then be stored exactly
> 
> **1 mark** for stating that moving bits to the mantissa leaves fewer for the exponent, so the range of numbers the system can represent is reduced
> 
> Accept "the value stored becomes 86.25" or "the last two digits are lost" for the second mark.
> 
> Accept "very large and very small numbers can no longer be stored", or a reference to overflow or underflow occurring for numbers that could previously be held, for the fourth mark.
> 
> Do not accept "the exponent of +7 will no longer fit". A 4-bit two's complement exponent runs from -8 to +7, so +7 is still inside it and this reading survives the change.
> 
> Do not accept "the change has no disadvantage". Precision and range are traded against each other whenever the total number of bits is fixed.

> **[exam-tip]**
> When a question fixes the total number of bits, every bit given to the mantissa is taken from the exponent. Mantissa bits buy precision, exponent bits buy range, and you cannot have more of both.
> 
> The trap here is the exponent. Work out the new range before you claim the reading breaks: +7 is exactly the largest value a 4-bit two's complement exponent can hold, so this particular reading is fine. The loss is in what the system can represent in general, not in this one number.

### Q14
Each digit after the binary point stands for a negative power of two, so 1/2, 1/4, 1/8, 1/16 and so on. Only a fraction that is a sum of these values can be written exactly in binary. **[1]**

The fractional part of +9.25 is 1/4, which is one of those values, so +9.25 is `1001.01` in binary. That is 6 significant digits, well inside the 12-bit mantissa. **[1]**

The fractional part of +9.20 is 1/5, which cannot be made from negative powers of two, so its binary form recurs as `1001.00110011...` and has to be truncated to fit the mantissa. The value stored is therefore only an approximation and a rounding error occurs. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for stating that the digits after the binary point represent negative powers of two, so only fractions that are sums of 1/2, 1/4, 1/8, 1/16 and so on can be held exactly
> 
> **1 mark** for stating that 0.25 is such a fraction, so +9.25 has a short terminating binary form that fits inside the mantissa
> 
> **1 mark** for stating that 0.20 is not, so its binary form recurs and must be truncated, leaving an approximation or a rounding error
> 
> Accept 0.25 written as 1/4 and 0.20 written as 1/5, in either fraction or decimal form.
> 
> Accept "0.2 recurs in binary" or "0.2 never ends in binary" for the third mark.
> 
> Do not accept "+9.20 needs more bits than the mantissa has, so a larger mantissa would store it exactly". The binary expansion of 0.2 does not end, so no mantissa length stores it exactly. Extra bits only make the error smaller.
> 
> Do not accept "+9.20 is not a whole number". Neither is +9.25, and +9.25 is stored exactly.

> **[exam-tip]**
> The test for an exact fraction is simple: halve repeatedly and see whether you land on the value. 0.25 is reached in two halvings, 0.2 is never reached at all.
> 
> Students very often answer that a bigger mantissa would fix +9.20. It would not. In this system +9.20 is stored as 9.1953125, and widening the mantissa pushes the error further down the number without ever removing it.

### Q15
In normalised form the number is 0.11010110011011 x 2<sup>5</sup>, so the mantissa would need 14 significant binary digits plus a sign bit, which is 15 bits in total. **[1]**

The mantissa in this system holds only 12 bits, which is a sign bit and 11 digits, so the 3 least significant digits `011` are truncated and precision is lost. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for stating that the number needs more mantissa bits than the system provides, for example 14 significant digits, or 15 bits once the sign bit is included, against the 12 bits available
> 
> **1 mark** for stating that the least significant digits are therefore truncated, so precision is lost or a rounding error occurs
> 
> Accept "only 11 digits can be stored after the sign bit" for the first mark.
> 
> Accept "3 digits are lost", "the mantissa is cut short", "the number is rounded" or "the value stored is only an approximation" for the second mark.
> 
> Do not accept an answer that blames the exponent. The exponent here is +5, and a 4-bit two's complement exponent covers -8 to +7, so the exponent fits with room to spare.
> 
> Do not accept "the number is too large for the system". The magnitude is not the problem. A value of the same size with fewer significant digits, such as +26.75, is stored exactly.

> **[exam-tip]**
> Count the significant digits from the leading 1, not the digits after the binary point. `11010.110011011` has 14 significant digits, and because the sign bit uses one place, a 12-bit mantissa holds only 11 of them.
> 
> The most common error on this question is to blame the exponent. Check the exponent first: work out its value, compare it with the range the exponent bits allow, and only then look at the mantissa.

### Q16
> **[mark-scheme]**
> **One** mark per mark point (**Max 1**)
> 
> - conversion of −96.75 to binary e.g., positive 96.75, flip the bits + 1 to give 10011111.01 
> // –128 + 16 + 8 + 4 + 2 + 1 + 0.25 / ¼ seen
> 
> **One **mark per mark point (**Max 2**)
> 
> - correct mantissa
> - correct exponent
> 
> **Mantissa**
> 
> | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 1 |
> |---|---|---|---|---|---|---|---|---|---|
> 
> **Exponent**
> 
> | 0 | 0 | 0 | 1 | 1 | 1 |
> |---|---|---|---|---|---|
> **[mark-scheme]**
> **One **mark per mark point (**Max 3**)
> 
> MP1 Real numbers (can) have a fractional part (such as 1 /3 and ½) / (such as 0.4 and 0.25)
> 
> MP2 The fixed length of the storage means that you can’t store very large / very small numbers
> 
> MP3 Binary numbers represent numbers based on powers of 2, with limited fractional representations such as 1/2, 1/4, 1/8, 1/16, etc.
> 
> MP4 It isn’t possible to store all fractions with the level of precision provided by this system
> 
> MP5 …the fractional part of the number is as close as possible within these constraints.

### Q17
> **[mark-scheme]**
> **One **mark for working (**Max 1**)
> 
> - conversion of 65.25 to binary seen e.g. 1000001.01 = 65.25 // 64 + 1 + 0.25 / ¼
> 
> **One **mark per mark point (**Max 2**)
> 
> - correct mantissa
> - correct exponent
> 
> **Mantissa**
> 
> | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> 
> **Exponent**
> 
> | 0 | 1 | 1 | 1 |
> |---|---|---|---|
> **[mark-scheme]**
> **One **mark per mark point (**Max 2**)
> 
> MP1 the decimal fraction 0.20 cannot be represented **exactly **(the closest is 0.25 / 0.1875)
> 
> MP2 therefore, there will be a loss of precision due to a rounding error/truncation

### Q18
> **[mark-scheme]**
> **One** mark per mark point (**Max 2**)
> 
> MP1 When the number of bits in the mantissa is raised, the precision / accuracy of the number represented increases // when the number of bits in the mantissa is lowered, the precision / accuracy of the number represented reduces.
> 
> MP2 When the number of bits in the exponent is reduced, the range of numbers that can be represented is reduced // when the number of bits in the exponent is increased, the range of possible numbers that can be represented increases.
> 
> MP3 When the range increases the accuracy decreases // When the range decreases the accuracy increases.
> **[mark-scheme]**
> **One **mark per mark point (**Max 3**)
> 
> - number converted to binary e.g. 54.8125 = 00110110.1101 // Fractions method 1/2 + 1/4 + 1/16 + 1/32 + 1/128 + 1/256 + 1/1024 = 877/1024 // 32 + 16 + 4 + 2 + 0.5 + 0.25 + 0.0625 / (<sup>1/2</sup> +<sup> 1/4</sup> +<sup> 1/16</sup>)
> - exponent = 6 // Moving binary point the correct number of places
> - correct answer
> 
> **Mantissa**
> 
> | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> 
> **Exponent**
> 
> | 0 | 1 | 1 | 0 |
> |---|---|---|---|

### Q19
**One **mark per mark point (**Max 3**)

MP1 conversion of exponent 001001 to 9

MP2 application of exponent to mantissa to go from 0.100111100 to 100111100 // 256 + 32 + 16 + 8 + 4 seen // 64/128 + 8/128 + 4/128 + 2/128 + 1/128 = 79/128 // 1/2 + 1/16 + 1/32 + 1/64 + 1/128 = 79/128

MP3 correct answer = 316
> **[mark-scheme]**
> **One **mark per mark point (**Max 3**)
> 
> MP1 number converted to binary 10011001.01 // number converted to positive 102.75, reversed bits and 1 added. (0)1100110.11  ⇒ 10011001.00 ⇒10011001.01 // -128 + 16 + 8 + 1 + 0.25 = –102.75
> 
> MP2 exponent = 7 // Moving binary point the correct number of places
> 
> MP3 correct answer
> 
> **Mantissa**
> 
> | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 |
> |---|---|---|---|---|---|---|---|---|---|
> 
> **Exponent**
> 
> | 0 | 0 | 0 | 1 | 1 | 1 |
> |---|---|---|---|---|---|

### Q20
> **[mark-scheme]**
> **One** mark for working
> 
> application of exponent to mantissa to go from 0.10001110111 to 01000111.0111 // moving the binary point 7 places // multiplying by
> 2<sup>7</sup> /128 in the fractions method // 64 + 4 + 2 +1 + .25+ .125 + .0625 seen
> 
> **One **mark for correct answer
> 
> • 71.4375 // 71<sup>7 /16</sup>
> **[mark-scheme]**
> **One mark **per mark point (**Max 2**)
> 
> - correct mantissa – exact answer only
> - correct exponent – exact answer only
> 
> **Mantissa**
> 
> | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> 
> **Exponent**
> 
> | 0 | 1 | 1 | 0 |
> |---|---|---|---|
> 
> **One mark** per mark point for working (**Max 2**)
> 
> - number converted to binary e.g., positive binary version of 
> 49.1875 = 0110001.0011 // two’s complement version bits flipped and 1 added = 1001110.1101 // 
> –64 + 8 + 4 + 2 + .5 + .25 + .0625 //
>  –64 + 14.8125
> - use of the exponent e.g. moving the binary point 6 places / x 2 <sup>6</sup> .

### Q21
> **[mark-scheme]**
> **One **mark per mark point (**Max 1**)
> 
> - correct answer
> - statement regarding number losing precision/rounding error
> 
> **One** mark per mark point for working (**Max 2**)
> 
> - number converted to binary $201.125=11001001.001//\,128+64+8+1+0.125/\frac{1}{8}seen\,$
> - use of the exponent e.g. moving the binary point 8 places  / 2 <sup>8</sup> .
> 
> **Mantissa**
> 
> | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
> |---|---|---|---|---|---|---|---|---|---|
> 
> **Exponent**
> 
> | 0 | 0 | 1 | 0 | 0 | 0 |
> |---|---|---|---|---|---|
> **[mark-scheme]**
> **One **mark per mark point (**Max 2**)
> 
> - application of exponent to go from 1.010110011 to 101011.0011 // x 2<sup>5</sup> // movement of binary point 5 places seen
> - 
> 
> $--32+8+2+1+.125+.0625//--32+8+2+1+\frac{1}{8}+\frac{1}{16}seen\,//--1+\frac{1}{4}+\frac{1}{16}+\frac{1}{32}+\frac{1}{256}+\frac{1}{512}//--1+\frac{179}{512}//--\frac{333}{512}$
> 
> **One **mark for correct answer (**Max 1**)
> 
> - –20.8125 //
>  –20<sup>13/16</sup>
