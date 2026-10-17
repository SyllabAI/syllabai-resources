---
note_id: "rn_73mKxFyPvcjk2zKw"
title: "Validation & Verification"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/7-algorithm-design-and-problem-solving/validation-and-verification/validation-and-verification
path: 7-algorithm-design-and-problem-solving/validation-and-verification/validation-and-verification
updated_at: "2025-12-10T14:01:21.154Z"
spec_point_ids: ["spcpt_NNNzT3vsdXS97q4S", "spcpt_XNYvx8XttSPbzSFg"]
spec_point_codes: []
guided_study: false
---

# Validation & Verification

## Validation

> **Spec point** — `spcpt_NNNzT3vsdXS97q4S` · " (a) Understand the need for validation checks
to be made on input data and the different
types of validation check"

## Validation

### What is validation?

- Validation is an **automated process** where **a computer checks** if a user input is **sensible **and meets the program's requirements.
- There are **six categories** of validation which can be carried out on **fields** and **data types,** these are

  - **Range check**
  - **Length check**
  - **Type check**
  - **Presence check**
  - **Format check**
  - **Check digit**
- There can be occasions where **more than one type of validation will be used **on a field
- An example of this could be a password field which could have a **length**, **presence **and **type** check on it

![input-validation](../../../assets/b2181ebc9b26-input-validation.png)

#### Range check

- Ensures the data entered as a number **falls within a particular range**

| Pseudocode | Ensures a percentage number is between 0-100 inclusive |
|---|---|
|   |   |

| Python | Ensures a user's age has been entered and falls between the digits of **0-110 inclusive** |
|---|---|
|   |   |

#### Length check

- Checks the **length of a string**

| Pseudocode | Ensures a pin number can only contain 4 digits |
|---|---|
|   |   |

| Python | Ensures a password is 8 characters or more |
|---|---|
|   |   |

#### Type check

- Check the **data type** of a field

| Pseudocode | Ensures an age should be entered as an integer (whole number) |
|---|---|
|   |   |

| Python | Ensures an age should be entered as an integer (whole number) |
|---|---|
|   |   |

#### Presence check

- Looks to see if **any data has been entered** in a field

| Pseudocode | Ensures username and password are both entered |
|---|---|
|   |   |

| Python | Ensures when registering for a website the name field is not left blank |
|---|---|
|   |   |

#### Format check

- Ensures that the data has been entered in the **correct format**
- Format checks are done using **pattern matching** and string handling

| Pseudocode | Ensures a six digit ID number is entered against the format "XX9999" where X is an uppercase alphabetical letter and 9999 is a four digit number |
|---|---|
|   |   |
| **Explanation** |   |
| - The first two characters are checked against a list of approved characters<br>- The first character is compared one at a time to each valid character in the ValidChars array<br>- If it finds a match it stops looping and sets ValidChar to True<br>- The second character is then compared one at a time to each valid character in the ValidChars array<br>- If it finds a match then it also stops looping and sets ValidChar to True<br>- Casting is used on the digits to turn the digit characters into numbers<br>- Once the digits are considered a proper integer they can be checked to see if they are in the appropriate range of 0-9999<br>- If any of these checks fail then an appropriate message is output |   |

| Python | Ensures an email contains a '@' and ' full stop (.) which follows the format "email@address.com" |
|---|---|
|   |   |

#### Check digits

- Check digits are **numerical values** that are the **final digit of a larger code** such as a **barcode **or an International Standard Book Number (**ISBN**)
- They are calculated by **applying an algorithm** to the code and are then attached to the overall code

## Verification

> **Spec point** — `spcpt_XNYvx8XttSPbzSFg` · "(b) Understand the need for verification checks
to be made on input data and the different
types of verification check"

## Verification

### What is verification?

- Verification is the act of checking data** is accurate** when entered into a system
- Mistakes such as creating a new account and entering a password incorrectly mean being locked out of the account immediately
- Verification methods include:

  - **double entry checking**
  - **visual checks**

#### Double entry checking

- Double entry checking involves** entering the data twice **in separate input boxes and then comparing the data to ensure they both match
- If they do not, an error message is shown

| Pseudocode |
|---|
|   |

#### Visual checks

- Visual checks involve the user **visually checking the data on the screen**
- A popup or message then asks if the data is correct before proceeding
- If it isn’t the user then enters the data again

| Pseudocode |
|---|
|   |

> **Worked Example**
> Describe the purpose of validation and verification checks during data entry. Include an example for each.
> 
> **[4]**
> 
> **Answers**
> 
> **Validation check **
> 
> [1] for description:
> 
> - **To test if the data entered is possible / reasonable / sensible**
> - **A range check tests that data entered fits within specified values**
> 
> [1]  for example:
> 
> - **Range / length / type / presence / format**
> 
> **Verification check **
> 
> [1]  for description:
> 
> - **To test if the data input is the same as the data that was intended to be input**
> - **A double entry check expects each item of data to be entered twice and compares both entries to check they are the same**
> 
> [1]  for example:
> 
> - **Visual / double entry**
