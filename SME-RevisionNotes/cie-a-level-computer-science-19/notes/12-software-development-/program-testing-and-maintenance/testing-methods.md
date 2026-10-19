---
note_id: "rn_BJfsGr6D4Gw5bcKJ"
title: "Testing Methods"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/12-software-development-/program-testing-and-maintenance/testing-methods
path: 12-software-development-/program-testing-and-maintenance/testing-methods
updated_at: "2026-10-01T12:32:45.883Z"
spec_point_ids: ["spcpt_fRKsxFstsrW5XrCd", "spcpt_2PC6sXWn2btbfPK7"]
spec_point_codes: []
guided_study: false
---

# Testing Methods

## Testing methods

> **Spec point** — `spcpt_fRKsxFstsrW5XrCd`

## Testing methods

### What are the different methods of testing?

- Testing takes place during the **testing stage** of the **program development life cycle**, once the program has been written and compiled

  - **Syntax errors** are usually detected during compilation
  - Testing focuses on checking for **logic errors**, **unexpected behaviour**, and **operational integrity**
  - A detailed **test plan**, outlining test cases and expected results, should be created during the **design stage**

#### Sample test plan

- Scenario: A program accepts a user's age between 0 and 120 inclusive

| **Test No.** | **Description** | **Input** | **Expected output** | **Type of test data** | **Actual outcome** |
|---|---|---|---|---|---|
| 1 | Valid age within accepted range | 25 | "Age accepted" | Normal |   |
| 2 | Input is not a number | "twenty" | "Invalid input: enter a number" | Abnormal |   |
| 3 | Age above the maximum allowed | 130 | "Age out of range" | Abnormal |   |
| 4 | Age exactly at the upper boundary | 120 | "Age accepted" | Boundary/Extreme |   |
| 5 | Age exactly at the lower boundary | 0 | "Age accepted" | Boundary/Extreme |   |
| 6 | Age just below lower boundary | -1 | "Age out of range" | Boundary/Extreme |   |
| 7 | Blank input | (blank) | "Please enter your age" | Abnormal |   |

### Common methods of testing

| **Testing method** | **Description** |
|---|---|
| **Dry run** | **Manually trace through** the code (e.g. on paper) to predict output and track variables |
| **Walkthrough** | Step-by-step review of the code **with others** to identify issues early |
| **White-box testing** | Tests the **internal logic** and code structure; the tester knows how the program works |
| **Black-box testing** | Tests the **inputs and expected outputs** without knowing the internal workings |
| **Integration testing** | Checks that different modules or components **work correctly together** |
| **Alpha testing** | Performed **in-house** by the developers during early testing |
| **Beta testing** | Carried out by **external users** in real-world environments |
| **Acceptance testing** | Final check to ensure the program meets the original **client requirements** |
| **Stub testing** | Uses temporary modules (stubs) to **simulate missing components** during early testing |

## Choosing test data

> **Spec point** — `spcpt_2PC6sXWn2btbfPK7`

## Choosing suitable test data

### What is suitable test data?

- Suitable test data is** specially chosen to test the functionality** of a program or design
- Developers or test-users would pick** a selection of test data** from the following categories

  - **Normal**
  - **Abnormal**
  - **Extreme/Boundary**
- The results would be **compared to the expected results **to check if the algorithm/program works as intended
- The results would be **stored in the test plan**
- Each category is explained within the context of a simple pseudocode program below

| **Pseudocode** |
|---|
|   |

#### Normal data

- Normal test data is data that **should be accepted **in the program
- An example would be a user entering their age as 16 into the age field of the program

#### Abnormal data

- Abnormal test data is data that **should be rejected** by the program, such as data of the **wrong data type** or a value **outside the acceptable range**
- Examples would be a user entering their age as "F", or as 45, into the age field of the program

#### Extreme data/Boundary data

- Boundary data (also called extreme data) tests values **at the edges of what the system accepts**
- This includes:

  - The **maximum **and **minimum acceptable **values
  - The **values just outside** those limits (the smallest and largest unacceptable values)
- Using the example of an age field that accepts 12–18:

  - **Boundary/extreme values:** 12 and 18 (the limits themselves)
  - **Just outside the boundary:** 11 and 19 (unacceptable values either side)

### Selecting suitable test data

| **Type of Test** | **Input** | **Expected Output** |
|---|---|---|
| **Normal** | 14 | Accepted |
| **Normal** | 16 | Accepted |
| **Abnormal** | H | Rejected |
| **Abnormal** | @ | Rejected |
| **Boundary/Extreme** | 12 | Accepted |
| **Boundary/Extreme** | 18 | Accepted |
| **Boundary/Extreme** | 11 | Rejected |
| **Boundary/Extreme** | 19 | Rejected |
