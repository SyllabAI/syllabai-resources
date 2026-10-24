---
note_id: "rn_YHyj6pPn3VYnZDgD"
title: "Internal Rate of Return (IRR)"
source: https://www.savemyexams.com/a-level/accounting/cie/21/revision-notes/cost-and-management-accounting/investment-appraisal/internal-rate-of-return-irr
path: cost-and-management-accounting/investment-appraisal/internal-rate-of-return-irr
updated_at: "2026-04-15T16:31:04.150Z"
spec_point_ids: ["spcpt_PcFc9YXbDYhm6d7d"]
spec_point_codes: []
guided_study: false
---

# Internal Rate of Return (IRR)

## Internal rate of return (IRR)

> **Spec point** — `spcpt_PcFc9YXbDYhm6d7d` · how to apply the following capital investment appraisal techniques:
– internal rate of return (IRR)
the advantages and disadvantages of these capital investment appraisal techniques

## Internal rate of return (IRR)

### What is the internal rate of return (IRR)?

- The **internal rate of return** is the discount rate at which the NPV of a project equals **zero**
- It is found by **interpolation** between two discount rates

  - One which gives a negative NPV and one which gives a positive NPV
- Owners usually prefer investments which have a **higher** internal rate of return
- If the internal rate of return is **higher** than the cost of capital, then the project is usually **accepted**
- If the internal rate of return is **lower **than the cost of capital, then the project is usually **rejected**

### How do I calculate the internal rate of return?

- **STEP 1**
Calculate the **[net cash flow](https://www.savemyexams.com/a-level/accounting/cie/21/revision-notes/cost-and-management-accounting/investment-appraisal/net-cash-flows/)** for each year
- **STEP 2**
Calculate the **[net present values](https://www.savemyexams.com/a-level/accounting/cie/21/revision-notes/cost-and-management-accounting/investment-appraisal/net-present-value-npv-/)** using both the **lower** and **higher **cost of capital

  - You will likely be asked to find one of these in an earlier question part
  - The NPV at the higher rate will be negative
- **STEP 3**
**Add** together the two net present values and **divide** the **NPV **at the **lower cost of capital** by this amount

  - $\frac{\mathrm{NPV} \mathrm{at} \mathrm{lower} \mathrm{rate}}{\mathrm{NPV} \mathrm{at} \mathrm{lower} \mathrm{rate}+\mathrm{NPV} \mathrm{at} \mathrm{higher} \mathrm{rate}}$
  - Ignore the fact that the NPV at the higher rate is negative
- **STEP 4**
**Multiply** this by the **difference** between the **two discount rates** and **add** this to the **lower** discount rate

  - $\frac{NPV \text{at} \text{lower} rate}{NPV \text{at} \text{lower} \text{rate} + \text{NPV} \text{at} \text{higher} rate} \times ( \text{higher} \text{rate} - \text{lower} \text{rate} ) + \text{lower} \text{rate}$
  
    - Write as a percentage

> **Exam Hint**
> This formula can look confusing. Make sure the number on top of the fraction is the NPV using the lower cost of capital. It is not necessarily the smallest number. See the worked example for more help.

### What are the advantages and disadvantages of the internal rate of return method?

#### Advantages

- It accounts for the time value of money
- It does not require a specific discount rate to be chosen in advance
- It is expressed as a percentage

  - This makes it easy to compare against the cost of capital

#### Disadvantages

- It requires the calculation of two net present values
- It ignores the scale of investment

  - A small project can have a high IRR
- Interpolation gives an approximation

  - It is not an exact figure

> **Worked Example**
> The directors of D plc are considering the purchase of a new machine, costing \$220 000, to manufacture a newly developed product, Product Omega. The directors intend to manufacture the product for only four years, after which the machine will have zero residual value.
> 
> The directors have estimated the following net cash flows arising from the project:
> 
> | **Year** | **Net cash flow (\$)** |
> |---|---|
> | 1 | 45 000 |
> | 2 | 60 000 |
> | 3 | 105 000 |
> | 4 | 30 000 |
> 
> Relevant discount factors are as follows:
> 
> |   | Discount rate |   |
> |---|---|---|
> | **Year** | **3%** | 5% |
> | 1 | 0.971 | 0.952 |
> | 2 | 0.943 | 0.907 |
> | 3 | 0.915 | 0.864 |
> | 4 | 0.888 | 0.823 |
> 
> Calculate the internal rate of return (IRR) to two decimal places.
> 
> **Answer**:
> 
> Calculate the NPV using the lower discount rate of 3%
> 
> | **Year** | **Net cash flow (\$)** |   | **Discounted net cash flow (\$)** |
> |---|---|---|---|
> | 0 | (220 000) | *(220 000) × 1.000* | (220 000) |
> | 1 | 45 000 | *45 000 × 0.971* | 43 695 |
> | 2 | 60 000 | *60 000 × 0.943* | 56 580 |
> | 3 | 105 000 | *105 000 × 0.915* | 96 075 |
> | 4 | 30 000 | *30 000 × 0.888* | <u>26 640</u> |
> |   |   |   | <u>2 990</u> |
> 
> Calculate the NPV using the higher discount rate of 5%
> 
> | **Year** | **Net cash flow (\$)** |   | **Discounted net cash flow (\$)** |
> |---|---|---|---|
> | 0 | (220 000) | *(220 000) × 1.000* | (220 000) |
> | 1 | 45 000 | *45 000 × 0.952* | 42 840 |
> | 2 | 60 000 | *60 000 × 0.907* | 54 420 |
> | 3 | 105 000 | *105 000 × 0.864* | 90 720 |
> | 4 | 30 000 | *30 000 × 0.823* | <u>24 690</u> |
> |   |   |   | <u>(7 330)</u> |
> 
> Use the formula
> 
> - Add the two NPVs
> - Divide the NPV at the lower rate by this value
> - Multiply by the difference between the two rates
> - Add this to the lower rate
> 
> $\frac{2 990}{2 990 + 7 330} \times ( 5 \% - 3 \% ) + 3 \% = 3.579... \%$
> 
> Round to 2 decimal places
> 
> **Final answer:** **IRR = 3.58%**
