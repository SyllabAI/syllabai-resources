# Mark Schemes — Program Testing & Maintenance
**12. Software Development** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (9 questions)


### Q1
> **[mark-scheme]**
> One mark per error:
> 
> Syntax:
> 
> 1. `NEXT Index `(should be `ENDWHILE`)
> 
> 2. '&' used to concatenate an integer (in `OUTPUT `statement)
> 
> Other:
> 
> 3. Accesses element outside range // Accesses element 0
> **[mark-scheme]**
> Run-time

### Q2
> **[mark-scheme]**
> One mark for method – two marks for the description
> 
> **MP1 **Stub testing
> 
> **MP2 **The modules `Test_A()`<u> and </u>`Test_B()`are replaced by dummy modules
> 
> **MP3 **... which return a known result // An output statement is displayed when called (to check it works) // gives expected output

### Q3
> **[mark-scheme]**
> **MP1**` Count ← INT(100 / Number)`
> Number could be zero (giving a divide by zero)
> 
> **MP2**` Index ← Data[Number]`
> Potential error: Value Number could be outside the range of array indices
> 
> **MP3 **`ReturnValue ← TO_UPPER(RIGHT(Label, Count))`
> Potential Error: Number to extract may be too big / negative / out of range for use in the RIGHT function // Label has insufficient characters
> 
> **MP4**` RETURN RetVal`
> Potential Error: There is no value to be returned // there is no variable named `RetVal`
> 
> Mark as follows:
> 1 mark for each statement <u>**and **</u>description
> **Max 3 marks**

### Q4
> **[mark-scheme]**
> (i) One mark per row
> 
> | Type of test data | Test data value | Expected result |
> |---|---|---|
> | Abnormal | 12 (< 23) | FALSE |
> | Abnormal / Boundary / Extreme | 23 | FALSE |
> | Boundary / Extreme | 24 | TRUE |
> | Boundary | 25 | TRUE |
> | Boundary | 36 | TRUE |
> | Boundary /Extreme | 37 | TRUE |
> | Abnormal / Boundary / Extreme | 38 | FALSE |
> | Abnormal | 99 (> 38) | FALSE |
> 
> **Max 4 marks**
> 
> (ii) Integration (testing)

### Q5
> **[mark-scheme]**
> One mark per point:
> 
> **Type**: Run-time error
> 
> **Cause**: A divide by zero operation is attempted // Attempt to convert a nonnumeric string to a number

### Q6
> **[mark-scheme]**
> One mark per point:
> 
> Error: The **calculation **of TaxPayable is incorrect
> 
> Correction: TaxPayable  (ItemCost * TaxRate) / 100

### Q7
> **[mark-scheme]**
> - **MP1**    Type: Adaptive
> - **MP2**   Reason: The (user) requirement(s) changes // to accommodate legislative changes

### Q8
> **[mark-scheme]**
> **One** mark per set, including stated purpose. Max 3 marks
> 
> Example answers:
> 
> 1   data set with (only) odd values, terminated with 99 
> 2   data set with (only) even values, terminated with 99 
> 3   data sets with same number of odd and even values, terminated with 99 
> 4   data sets with all even / all odd with just one odd/even value, terminated with 99 
> 5   data sets with no values just final 99 
> 6   data sets without (terminating) 99 // missing or incorrectly placed 99

### Q9
> **[mark-scheme]**
> - **MP1 **    `Num > Min` should be `Num < Min `
> - **MP2 **  `Count & 1 `should be `Count + 1 `
> - **MP3**` NextInput  "END"` should be `NextInput = "END"`
> **[mark-scheme]**
> (i)
> 
> - **MP1 **   If all the numeric input values are greater than 999 // If there are no numeric values in the sequence
> - **MP2**    then the minimum will be given as <u>**999 **</u>(and not one of the input values) (ii) Many possible correct answers, for example:
> - **MP1  **  Mixture non-numeric and numeric with 3 or 4 values - with all numerics 
> greater than 999 
> Examples: 1325, DOG, 7868, 7615 
> // SNAKE, 3478, SPIDER
> - **MP2**    Final value: END
