# Mark Schemes — Recursion
**19. Computational thinking & Problem-solving** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (7 questions)


### Q1
(i) 5, 3, 1 **[1]**

then 10, 30, 50 **[1]**

(ii) Each time `Show()` calls itself, the return address and the value of `N` are pushed onto the stack **[1]**

This winding continues until the base case is reached, when `N` is -1 and the condition `N > 0` is false, so nothing more is output **[1]**

The stack then unwinds, popping the most recent call first. The value of `N` is restored from the stack before the statement after the call runs, so `N * 10` is output for 1, then 3, then 5 **[1]**

**[5 marks]**

> **[mark-scheme]**
> (i)
> 
> **1 mark** for 5, 3, 1 in this order at the start
> 
> **1 mark** for 10, 30, 50 in this order after them
> 
> (ii) **Max 3 from:**
> 
> - Return address / value of `N` / values of local variables pushed onto the stack with each recursive call // winding
> - Calls continue until the base case is reached // until `N` is not greater than 0 // when `N` is -1
> - After the base case, return addresses / values of `N` are popped off the stack // unwinding
> - The stack is last in, first out, so the most recent call (`N = 1`) finishes first
> - The value of `N` popped for each call is the one used by the `OUTPUT` after the recursive call
> 
> **[3 marks]**
> 
> Do not accept an answer that says the values are output in reverse "because the procedure goes backwards" with no reference to the stack
> 
> Do not award the first mark of (i) for 5, 3, 1, -1; the value -1 is never output

> **[exam-tip]**
> Students often output all six values in the order the calls are made, for example 5, 50, 3, 30, 1, 10. The second `OUTPUT` cannot run until the call before it has completely finished, and that call makes its own calls first. Trace every call down to the base case before writing anything that comes after a recursive call.
> 
> A second error is to output -1, or 0, from the base case. When `N` is -1 the condition is false and the procedure does nothing at all.

### Q2
(i)

| Stack position | Return address | Value of N |
|---|---|---|
| 1 (top) | **05** | **1** |
| 2 | **05** | **3** |
| 3 | **05** | **6** |
| 4 | **20** | **12** |
| 5 |   |   |

Value of N column correct, 1, 3, 6, 12 from the top **[1]**

Return address column correct, 20 at the bottom and 05 in the three positions above it **[1]**

(ii) 3 **[1]**

**[3 marks]**

> **[mark-scheme]**
> (i)
> 
> **1 mark** for the Value of N column: 1, 3, 6, 12 from top to bottom, with position 5 empty
> 
> **1 mark** for the Return address column: 05, 05, 05, 20 from top to bottom
> 
> Do not accept the stack in reverse order, with 12 and 20 in position 1; position 1 is the top of the stack, where the most recent call sits
> 
> (ii)
> 
> **1 mark** for 3
> 
> Do not accept 4 (the number of calls) or 0 (the value returned by the base case)

> **[exam-tip]**
> A frequent error is to put 05 as the return address of the first call. The first call was made from line 20, so that is where control goes back to when it finishes, and it sits at the bottom of the stack. Only the calls made by the function itself return to line 05.
> 
> In (ii), many students give 4 because there are four items on the stack. Count the values returned instead: 0, then 1, 2 and 3 as the stack unwinds.

### Q3
(i) Winding **[1]**

(ii) Unwinding **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for (i) winding
> 
> **1 mark** for (ii) unwinding
> 
> Do not accept "pushing" or "popping" on their own; these name the stack operations, not the process

> **[exam-tip]**
> Students often reverse the two terms. Winding happens first, on the way down to the base case, as each new call adds more to the stack. Unwinding happens after the base case, on the way back up, as each call finishes and the stack gets smaller.

### Q4
(i)

| Call number | Function call | Number | Result | Return value |
|---|---|---|---|---|
| 1 | DigitSum(4739) | 4739 | 9 + DigitSum(473) |   |
| **2** | **DigitSum(473)** | **473** | **3 + DigitSum(47)** |   |
| **3** | **DigitSum(47)** | **47** | **7 + DigitSum(4)** |   |
| **4** | **DigitSum(4)** | **4** | **4** | **4** |
| **(3)** | **DigitSum(47)** | **47** | **7 + 4** | **11** |
| **(2)** | **DigitSum(473)** | **473** | **3 + 11** | **14** |
| **(1)** | **DigitSum(4739)** | **4739** | **9 + 14** | **23** |

Call number, Function call and Number columns correct **[1]**

Result column correct down to the base case, rows 2 to 4 **[1]**

Result column correct back up from the base case, the last three rows **[1]**

Return value column correct, ending in 23 **[1]**

(ii) It returns the sum of the digits of the integer passed to it **[1]**

**[5 marks]**

> **[mark-scheme]**
> (i)
> 
> **1 mark** for the Call number, Function call and Number columns all correct
> 
> **1 mark** for the Result column correct in rows 2 to 4 (winding down to the base case)
> 
> **1 mark** for the Result column correct in the last three rows (unwinding from the base case)
> 
> **1 mark** for the Return value column correct: 4, 11, 14, 23
> 
> Accept the base-case row with an empty Result cell if the Return value is 4
> 
> Accept call numbers on the last three rows without brackets if they are 3, 2, 1 in that order
> 
> (ii)
> 
> **1 mark** for: it adds together / totals the digits of the number
> 
> Do not accept "it adds up the numbers" or "it counts the digits"; the answer must refer to the digits of the one number passed in

> **[exam-tip]**
> The most common error in a recursive trace is to fill the Return value column on the way down. No call can return a value until the call below it has finished, so rows 1 to 3 stay empty in that column. Values only appear once the base case is reached and the calls unwind.
> 
> A second error is to list the unwinding rows in the same order as the winding rows. The most recent call finishes first, so the unwinding rows run 3, 2, 1.

### Q5
The test `IF Exponent = 0` identifies the base case **[1]**

The base case returns 1 without a recursive call **[1]**

The general case calls `Power()` with `Exponent - 1` **[1]**

The general case multiplies the value returned by `Base` and returns the result **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for a test that identifies the base case, `Exponent = 0` or `Exponent = 1`
> 
> **1 mark** for returning the matching base value: 1 when `Exponent = 0`, or `Base` when `Exponent = 1`
> 
> **1 mark** for a recursive call `Power(Base, Exponent - 1)`
> 
> **1 mark** for `Base * Power(Base, Exponent - 1)` returned in the general case
> 
> Accept an equivalent structure that assigns to a local variable and returns it once at the end, for example `Result ← Base * Power(Base, Exponent - 1)` followed by `RETURN Result`
> 
> Do not accept a solution that still contains a loop; this is not a recursive solution
> 
> Do not award the third mark if the recursive call does not reduce `Exponent`, as the base case would never be reached

> **[exam-tip]**
> Many students write `Power(Base - 1, Exponent)`, reducing the wrong parameter. Ask yourself which value gets closer to the base case on each call: here it is `Exponent`, so that is the one that must change.
> 
> Another frequent error is to write the recursive call on its own line, for example `CALL Power(Base, Exponent - 1)`. A function is never called with `CALL`, and its return value must be used in an expression, otherwise the result is lost.

### Q6
Base case: line 03 (reached when `N = 1`, it returns without making a recursive call) **[1]**

General case: line 05 (the function calls itself with `N - 1`) **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for base case: line 03
> 
> **1 mark** for general case: line 05
> 
> Accept line 02 or lines 02 and 03 for the base case, since line 02 holds the test that selects it
> 
> Accept lines 04 and 05 for the general case
> 
> Do not accept line 01 or line 07 for either answer; these are the function heading and ending

> **[exam-tip]**
> A common error is to give line 05 as the base case because it is the line that "does the work". The base case is the one that returns a value **without** a recursive call. Look for the line that does not mention `Total` on the right-hand side.

### Q7
> **[mark-scheme]**
> **One** mark per mark point **(Max 1)**
> 
> - MP1    The compiler must produce object code to
> 
> **One** mark per mark point **(Max 3) **
> 
> - MP2    …push return addresses / values of local variables onto a stack
> - MP3    …with each recursive call // … to set up winding
> - MP4    …pop return addresses / values of local variables off the stack …
> - MP5    …after the base case is reached // … to implement unwinding.
