---
note_id: "rn_Kjq96m6hwB37bMxg"
title: "Check Digits"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/2-data-transmission/methods-of-error-detection/check-digits
path: 2-data-transmission/methods-of-error-detection/check-digits
updated_at: "2024-10-07T09:02:49.712Z"
spec_point_ids: ["spcpt_nzr2RVhWmZ9KRVyN"]
spec_point_codes: []
guided_study: false
---

# Check Digits

## Check Digits

> **Spec point** — `spcpt_nzr2RVhWmZ9KRVyN` · "3 Describe how a check digit is used to detect
errors in data entry and identify examples of
when a check digit is used, including international
standard book numbers (ISBN) and bar codes"

## Check Digits

### What is a check digit?

- A check digit is the** last digit** included in a code or sequence, used to **detect errors **in **numeric data entry**
- Examples of errors that a check digit can help to identify are:

  - **Incorrect digits entered**
  - **Omitted or extra digits**
  - **Phonetic errors**
- Added to the **end of a numerical sequence** they ensure **validity **of the data
- Calculated  using **standardised algorithms **to ensure widespread **compatibility**
- Examples of where check digits can be used include:

  - **ISBN book numbers**
  - **Barcodes**

#### ISBN book numbers

- Each book has a **unique **ISBN number that **identifies **the book
- A standard ISBN number may be ten digits, for example, 965-448-765-9
- The check digit value is the** final digit** (9 in this example).
- This number is chosen specifically so that when the algorithm is completed the result is a whole number (an integer) with no remainder parts
- A check digit algorithm is performed on the ISBN number and **if the result is a whole number,** then the **ISBN is valid**

#### Barcodes

- Barcodes consist of **black and white lines** which can be scanned using barcode scanners
- Barcode scanners** shine a laser** on the black and white lines which **reflect light** into the scanner
- The scanner reads the **distance between these lines as numbers** and can identify the item
- Barcodes also use a** set of digits** to **uniquely identify each item**
- The** final digit** on a barcode is usually the** check digit**, this can be used to **validate **and **authenticate **an item

> **Worked Example**
> Check digit algorithms are used to determine whether an error has occurred in transmitted data.
> 
> **State **the names of two examples of a check digit algorithm.
> 
> **[2]**
> 
> **Answer**
> 
> - **ISBN [1]**
> - **Barcode [1]**
