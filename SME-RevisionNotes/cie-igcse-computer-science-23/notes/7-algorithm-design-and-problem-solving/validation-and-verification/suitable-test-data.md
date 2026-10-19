---
note_id: "rn_S3JVbJYqjDTp5FfC"
title: "Suitable Test Data"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/7-algorithm-design-and-problem-solving/validation-and-verification/suitable-test-data
path: 7-algorithm-design-and-problem-solving/validation-and-verification/suitable-test-data
updated_at: "2024-11-28T11:57:58.642Z"
spec_point_ids: ["spcpt_YpvJsHgf4fknYnDy"]
spec_point_codes: []
guided_study: false
---

# Suitable Test Data

## Suitable Test Data

> **Spec point** — `spcpt_YpvJsHgf4fknYnDy` · 6 Suggest and apply suitable test data

## Suitable Test Data

### What is suitable test data?

- Suitable test data is** specially chosen to test the functionality** of a program or design
- Developers or test-users would pick** a selection of test data** from the following categories

  - **Normal**
  - **Abnormal**
  - **Extreme**
  - **Boundary**
- The results would be **compared to the expected results **to check if the algorithm/program works as intended
- Each category is explained within the context of a simple Python program below, comments have been added to help explain the processes

| Python |
|---|
|   |

#### Normal data

- Normal test data is data that **should be accepted **in the program
- An example would be a user entering their age as 16 into the age field of the program

#### Abnormal data

- Abnormal test data is data that is the **wrong data type**
- An example would be a user entering their age as "F" into the age field of the program

#### Extreme data

- Extreme test data is the **maximum** and **minimum **values of normal data that are **accepted **by the system
- An example would be a user entering their age as 18 or 12 into the age field of the program

#### Boundary data

- Boundary test data is similar to extreme data except that the values **on either side of** the **maximum **and **minimum **values are tested
- The largest and smallest acceptable value is tested as well as the largest and smallest unacceptable value
- An example would be a user entering their age as 11 or 19 into the age field of the program

### Selecting suitable test data

| **Type of Test** | **Input** | **Expected Output** |
|---|---|---|
| **Normal** | 14 | Accepted |
| **Normal** | 16 | Accepted |
| **Extreme** | 12 | Accepted |
| **Extreme** | 18 | Accepted |
| **Abnormal** | H | Rejected |
| **Abnormal** | @ | Rejected |
| **Boundary** | 11 | Rejected |
| **Boundary** | 19 | Rejected |

> **Worked Example**
> A programmer has written an algorithm to check that prices are less than \$10.00
> 
> These values are used as test data:     10.00     9.99     ten
> 
> State why each value was chosen as test data.
> 
> **[3]**
> 
> **Answers**
> 
> **Final answer:** **10.00 is boundary or abnormal data and should be rejected as it is out of range [1]**
> 
> **Final answer:** **9.99 is boundary, extreme and normal data and should be accepted as it is within the normal range [1]**
> 
> **Final answer:** **Ten is abnormal data and should be rejected as it is the wrong value type [1]**
