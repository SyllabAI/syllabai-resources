## Validation and Verification

To ensure the acceptance of reasonable and accurate data inputs, computer systems must thoroughly examine each data item before accepting it, and this is where Validation and Verification come into play!

### **Validation**

Validation in computer systems involves automated checks to ensure the reasonableness of data before accepting it. If the data is invalid, the system should provide an explanatory message for rejection and allow another chance to enter the data.

**There are multiple types of validation. These include:**

**Range check**

A range check verifies that a numerical value falls within specified upper and lower limits.

```javascript
REPEAT
 INPUT Value
 IF Value < MinimumValue OR Value > MaximumValue
  THEN
  OUTPUT "The student's mark should be in the range", MinimumValue ," to ", MaximumValue
 ENDIF
UNTIL Value >= MinimumValue AND Value <= MaximumValue
```

### **Length check**

This can either ensure that data consists of a precise number of characters.

```javascript
OUTPUT "Please enter your value of ", Limit , "  characters "
REPEAT
 INPUT Value
 IF LENGTH(Value) <> Limit
  THEN
  OUTPUT "Your value must be exactly" , Limit ," characters, please re-enter "
 ENDIF
UNTIL LENGTH(Value) = Limit
```

It can also check if the data entered is a reasonable number of characters or not

```javascript
OUTPUT "Please enter your value "
REPEAT
 INPUT Value
 IF LENGTH(Value) > UpperLimit OR LENGTH(Value) < LowerLimit
  THEN
   OUTPUT "Too short or too long, please re-enter "
 ENDIF
UNTIL LENGTH(Value) <= UpperLimit AND LENGTH(Value) >= LowerLimit
```

### **Type check**

A type check verifies that the entered data corresponds to a specific data type.

```javascript
OUTPUT "Enter the value "
REPEAT
 INPUT Value
 IF Value <> DIV(Value, 1)
  THEN
   OUTPUT "This must be a whole number, please re-enter"
 ENDIF
UNTIL Value = DIV(Value, 1)
```

### **Presence check**

A presence check checks to ensure that some data has been entered and the value has not been left blank

```javascript
OUTPUT "Please enter the value "
REPEAT
 INPUT Value
 IF Value = ""
  THEN
   OUTPUT "*=Required "
 ENDIF
UNTIL Value <> ""
```

### **Format Check**

A format check checks that the characters entered conform to a pre-defined pattern.

### **Check Digit**

* A check digit is the final digit included in a code; it is calculated from all the other digits.
* Check digits are used for barcodes, product codes, International Standard Book Numbers (ISBN), and Vehicle Identification Numbers (VIN).

### **Verification**

Verification is checking that data has been accurately copied from one source to another

**There are 2 methods to verify data during entry** ( there are other methods during data transfer, but they are in paper 1)

### **1. Double Entry**

* Data is inputted twice, potentially by different operators.
* The computer system compares both entries and if they differ, an error message is displayed, prompting the data to be reentered.

### **2. Screen/Visual check**

* A screen/visual check involves the user manually reviewing the entered data.
* After data entry, the system displays the data on the screen and prompts the user to confirm its accuracy before proceeding.
* The user can compare the displayed data against a paper document used as an input form or rely on their own knowledge to verify correctness.