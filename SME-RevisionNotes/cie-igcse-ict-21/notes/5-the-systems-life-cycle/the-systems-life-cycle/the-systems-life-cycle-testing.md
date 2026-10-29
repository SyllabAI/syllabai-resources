---
note_id: "rn_7gYhps9XjZHXrHbX"
title: "The Systems Life Cycle: Testing"
source: https://www.savemyexams.com/igcse/ict/cie/21/revision-notes/5-the-systems-life-cycle/the-systems-life-cycle/the-systems-life-cycle-testing
path: 5-the-systems-life-cycle/the-systems-life-cycle/the-systems-life-cycle-testing
updated_at: "2024-10-10T09:40:02.040Z"
spec_point_ids: ["spcpt_5MrD3DMtXc7pZkZf", "spcpt_kPr3d6DspMYB7hWt"]
spec_point_codes: []
guided_study: false
---

# The Systems Life Cycle: Testing

### What is the system life cycle?

- The system life cycle** **is **a structured process** that guides the **planning**, **creation**, **testing**, and **deployment **of an information system
- Ensures systems are** systematically developed**, meeting needs of stakeholders, **minimising **risks and **maximising **efficiency
- The third stage is **testing**, the purpose is to:

  - **Verify **that the system **meets all requirements**, **functions correctly**, and is **free of bugs** through various testing methods.

## Test Strategies

> **Spec point** — `spcpt_5MrD3DMtXc7pZkZf`

## Test Strategies

### What are test strategies?

- A test strategy is** a method of testing a completed system **to ensure **all parts work as intended**
- Systems are designed in a *modular* format
- Each module needs to be** tested independently**
- Testing **is done again **once** **all **modules are joined together**
- The results of testing **may indicate changes** need to be made, **testing is repeated **once all changes have been made

#### Test designs

| Test design | Why? |
|---|---|
| Data structures | Test all data is stored correctly |
| File structures | Test all data is stored in the correct format |
| Input formats | Test that data can be entered correctly |
| Output formats | Tests that screen output and reports are in the correct format |
| Validation routines | Tests that the system rejects unreasonable data being inputted |

#### Test plans

- A test plan is designed and implemented **to ensure thorough testing of a system**, it includes:

  - **Test data**: specific data used for testing purposes
  - **Expected outcomes**: predicted results based on test data
  - **Actual outcomes**: results obtained from testing
  - **Remedial action**: steps taken to fix identified issues

## Test Data

> **Spec point** — `spcpt_kPr3d6DspMYB7hWt`

## Test Data

### What is test data?

- Test data is specific data used for testing purposes
- There are **four **main categories of test data that would be used whilst performing final testing on a system

  - **Normal **
  - **Extreme**
  - **Abnormal **
  - **Live**

#### Normal data

- Normal test data is data that **should be accepted **in the system
- Normal data **has a known outcome**

#### Extreme data

- Extreme data is **data that is on the limits of what is acceptable **

#### Abnormal data

- Abnormal data is data **outside of the limits of what is acceptable**
- Abnormal data should be rejected by the system

#### Live data

- Live data is **data from the old system used on the new system**
- Live data **has known outcomes**, so it can be compared to the new system to ensure the new system works

> **Worked Example**
> The European Space Agency (ESA) is building a new space telescope to orbit the Earth and search for distant galaxies. The ESA is using computer controlled robots to build the lens of the telescope. A new computer system will operate the space telescope; the new computer system is made up of several modules.
> 
> Describe how the new computer system is to be tested before it is fully operational.
> 
> **[4]**
> 
> **Answer**
> 
> four of:
> 
> **Final answer:** **Each module has to be tested independently to ensure it functions correctly [1]**
> **Modules need to be tested together [1]**
> **Data needs to be transferred from module to module to check for data clashes [1]**
> **Errors need to be noted and corrections made [1]**
> **Then tested again [1]**
> **The system as a whole needs to be fully tested under controlled conditions [1]**
