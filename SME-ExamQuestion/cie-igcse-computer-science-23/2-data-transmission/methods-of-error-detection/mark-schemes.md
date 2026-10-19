# Mark Schemes — Methods of Error Detection
**2. Data Transmission** · Cambridge (CIE) IGCSE computer-science (0478 & 0984)


## Exam Questions (10 questions)


### Q1
Examples of error detection methods that could be used include:

Any **two **of the following:

- Echo check **[1 mark]**
- Checksum **[1 mark]**
- Even parity check **[1 mark]**
- Negative ARQ **[1 mark]**

### Q2
(i)

Examples of how the error detection system operates include:

Any **six **of the following:

- The 1s are counted (in each byte) **[1 mark]**
- Each byte has a parity bit **[1 mark]**
- If the number of 1s is odd, the parity bit is 0 (otherwise it is 1) **[1 mark]**
- (The first packet of) data is sent and a timer is started **[1 mark]**
- The receiving device counts the number of 1s (in each byte) **[1 mark]**
- If the number of 1s is odd/data meets odd parity, an acknowledgement is sent to say the data is error free… **[1 mark]**
- … the sender then sends the next packet of data… **[1 mark]**
- … and the timer is restarted **[1 mark]**
- If the number of 1s is even, an acknowledgement is not sent **[1 mark]**
- If no acknowledgement is received within a set timeframe/before timeout… **[1 mark]**
- … the data packet is resent **[1 mark]**

(ii)

Examples of other error detection methods include:

Any **two **of the following:

- Echo check **[1 mark]**
- Checksum **[1 mark]**
- Even parity check **[1 mark]**
- Negative ARQ **[1 mark]**

### Q3
Examples of how the data might have errors after transmission include:

Any **three **of the following:

- Data could be lost **[1 mark]**
- Data could be gained/added **[1 mark]**
- Data could be changed **[1 mark]**
- Bits could be reassembled in the wrong order **[1 mark]**
- Interference could occur **[1 mark]**
- Crosstalk could occur **[1 mark]**
- Data collisions could occur **[1 mark]**
- Data packets could time out/reach their hop count **[1 mark]**
- Network could be infected with malware **[1 mark]**

### Q4
Automatic Repeat reQuest protocol ensures data integrity by:

Any **four **of the following:

- Requiring the receiver to send acknowledgements (ACK) back to confirm data was received correctly **[1 mark]**
- Sending a negative acknowledgement (NACK) if the data is corrupted or an error is detected **[1 mark]**
- Resending the data when a NACK is received to ensure data integrity **[1 mark]**
- Using a time-out feature; if no acknowledgement is received in time, the data is resent automatically **[1 mark]**
- Continuing the process until a positive acknowledgement (ACK) is received, ensuring all data is correctly transmitted **[1 mark]**

> **[exam-tip]**
> - An example four mark response could include:
> 
> *The ARQ protocol ensures data integrity by requiring the receiver to send an acknowledgement (ACK) when data is received correctly. If an error is detected, the receiver sends a negative acknowledgement (NACK) back to the sender, requesting the data be resent. If no acknowledgement is received within a set time frame, the sender automatically resends the data. This process continues until the sender receives an ACK, confirming that all data has been successfully transmitted.*

### Q5
Errors can occur by:

- Interference **[1 mark]**
- Bad weather conditions **[1 mark]**
- Physical obstruction / barriers (e.g. walls / ceilings / concrete) **[1 mark]**
- Distance from source causing weak / unstable signal **[1 mark]**

> *Award any two distinct valid reasons, up to 2 marks*

> **[exam-tip]**
> You can get full marks by giving valid examples of each
> 
> Name physical causes of wireless errors, not security issues (e.g. interception) or general transmission consequences (e.g. out-of-order packets)

### Q6
It is important to ensure data is in the correct format because if not:

Any **one** of the following:

- It can lead to misunderstandings or errors in processing the data** [1 mark]**
- Makes it difficult or impossible for computers to use the data correctly **[1 mark]**

Some common examples of where format errors occur could include:

Any **one** of the following, this list is not exhaustive:

- Data format **[1 mark]**
- Phone number format **[1 mark]**
- email address format **[1 mark]**
- currency format **[1 mark]**
- Post code / zip code format **[1 mark]**

### Q7
A checksum can be used by:

Any** five** of the following:

- A value is calculated from the data** ****[1 mark]**
- The value is calculated using an algorithm  **[1 mark] **
- The value is appended to the data to be transmitted **[1 mark] **
- Value is recalculated after transmission **[1 mark] **
- Values are compared **[1 mark] **
- If the values match the data is correct **/ **if the values do not match the data is incorrect **[1 mark] **

> **[exam-tip]**
> - An example five mark response could be:
> 
> *A checksum is a method used to verify that data has been transmitted correctly. First, a value is calculated from the original data using an algorithm. This checksum value is then attached to the data before it is transmitted. After the data is received, the system recalculates the checksum value from the received data. The original checksum and the recalculated one are compared. If the values don't match, it indicates an error occurred during transmission.*
> 
> Be clear that the recalculated checksum is compared with the originally sent checksum, not with the original data.
> 
> A checksum is recalculated from the received data, not decrypted or run backwards — don't confuse it with encryption.

### Q8
A check digit can be used to make sure the data entered is correct by:

Any** four** of the following:

- Data is** **input with check digit **[1 mark]**
- A calculation is performed on the (inputted) data **[1 mark] **
- The calculated digit is compared to a stored value** [1 mark] **
- If it matches, the data entered is correct** [1 mark]**
- If it does not match, the data entered is incorrect **[1 mark]**

### Q9
> **[mark-scheme]**
> - A = **1**` `**[1 mark]**
> - B = **1**` `**[1 mark]**
> - C = **1**` `**[1 mark]**
> 
> Even parity means the total number of 1s (including the parity bit) must be even for no error to be detected.
> 
> - Register A has three 1s in the data (`0100101`), so the parity bit must be 1 to make the total even (4). No error detected.
> - Register B has two 1s in the data (`1000001`), so the parity bit must be 1 to make the total odd (3). This means an error is detected because the total is not even.
> - Register C has three 1s in the data (`1000011`), so the parity bit must be 1 to make the total even (4). No error detected.

> **[exam-tip]**
> Remember that with even parity, the total number of 1s (data bits plus the parity bit) should be even when no error is present. For Register B, you need to choose a parity bit that results in an odd total number of 1s, since the question states that an error has been detected. Many students forget that the question asks you to show a specific outcome — read carefully whether the register should pass or fail the parity check before deciding on the parity bit.

**[3 marks]**

### Q10
The completed table shows the odd or even parity:

| **8-bit binary value** | **Type of parity** |
|---|---|
| 01100100 | Odd **[1 mark]** |
| 10010001 | Odd **[1 mark]** |
| 00000011 | Even **[1 mark]** |
| 10110010 | Even **[1 mark]** |
