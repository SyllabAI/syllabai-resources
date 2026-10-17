---
note_id: "rn_jwpNRvbwwqs2RNb5"
title: "Automatic Repeat Query (ARQ)"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/2-data-transmission/methods-of-error-detection/automatic-repeat-query-arq
path: 2-data-transmission/methods-of-error-detection/automatic-repeat-query-arq
updated_at: "2024-04-11T14:56:53.920Z"
spec_point_ids: ["spcpt_8wrfXRgP6N49Zc73"]
spec_point_codes: []
guided_study: false
---

# Automatic Repeat Query (ARQ)

## Automatic Repeat Query (ARQ)

> **Spec point** — `spcpt_8wrfXRgP6N49Zc73` · "4 Describe how an automatic repeat query (ARQ)
can be used to establish that data is received
without error"

## Automatic Repeat reQuests(ARQ)

### What is an automatic repeat request(ARQ)?

- An automatic repeat request is a *protocol* that **notifies the sender that an error has occurred** and that the **data received is incorrect**
- It works as follows:

  - If an error is detected the receiver sends a** negative acknowledgement transmission** to **indicate the data is corrupted**
  - If no error is detected the receiver sends a **positive acknowledgement transmission** meaning **the data is correct**
  - If the receiver** does not send any acknowledgement transmission **then the sender waits for a certain time period known as a **time-out** before **automatically resending** the data
  - This process is repeated until all data has been **received **and **acknowledged**

> **Exam Hint**
> In this specification ARQ is referred to as** Automatic Repeat Query** but in past exam questions it has been referred to as **Automatic Repeat reQuests**
> 
> Both words are **interchangeable **and should not cause any confusion!

> **Worked Example**
> Explain how Automatic Repeat reQuests (ARQ) are used in data transmission and storage
> 
> **[2]**
> 
> **Answer**
> 
> Any **two **from:
> 
> - **Set of rules for controlling error checking/detection // it’s an error detection method // used to detect errors**
> - **Uses acknowledgement and timeout**
> - **Request is sent (with data) requiring acknowledgement**
> - **If no response/acknowledgment within certain time frame data package is resent**
> - **When data received contains an error a request is sent (automatically) to resend the data**
> - **The resend request is repeatedly sent until packet is received error free/limit is reached/acknowledgement received**
