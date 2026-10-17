---
note_id: "rn_NX7ZwKn4XB78gbzd"
title: "Digital Certificates"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/17-security-/encryption-encryption-protocols-and-digital-certificates/digital-certificates
path: 17-security-/encryption-encryption-protocols-and-digital-certificates/digital-certificates
updated_at: "2025-05-19T10:47:07.270Z"
spec_point_ids: ["spcpt_9HZjnCMwpRjvrzpc"]
spec_point_codes: []
guided_study: false
---

# Digital Certificates

## Digital certificates

> **Spec point** — `spcpt_9HZjnCMwpRjvrzpc`

## Digital certificates

### What is a digital certificate?

- A digital certificate is an **electronic file** that** confirms someone’s identity** and proves that a **public key** belongs to them
- It is issued by a trusted third party called a **Certificate Authority (CA)**
- A digital certificate includes:

  - The owner’s **public key**
  - The owner’s **identity details** (e.g. name, email, company)
  - The **expiry date** of the certificate
  - The **Certificate Authority’s digital signature**

#### Hash function

- A hash function is a one-way algorithm that takes an input (e.g. a message) and produces a fixed-length output, called a **hash value** or **message-digest**
- **Key features:**

  - The output is always the same length, regardless of input size
  - It is **one-way** — you cannot reverse it to get the original input
  - Even a small change in input produces a completely different output
  - Commonly used in digital signatures and password storage
- Think of it as a fingerprint for data

#### Message-digest

- A message-digest is the **output (the hash value) produced **when a message is processed through a hash function
- **It is:**

  - A fixed-length summary of the original message
  - Unique to the message (ideally – collisions are rare)
  - Used to check whether a message has been altered
- Think of it as the unique ID or checksum of a message

### How is a digital certificate acquired?

1. **Leila** wants to be able to sign documents digitally
2. She generates a **key pair** – one private key and one public key
3. Leila sends a **Certificate Signing Request (CSR)** to a **Certificate Authority (CA)**

  1. This includes her **public key** and identity details
4. The CA **verifies Leila’s identity** using documents or other checks
5. If approved, the CA **digitally signs** a certificate and sends it back to Leila

  1. This certificate contains Leila’s **public key**, identity, and the CA’s signature

### How is a digital certificate used to produce a digital signature?

1. Leila writes a message she wants to send to **Jonas**
2. She applies a **hash function** to the message to create a **message-digest**
3. Leila then **encrypts the message-digest using her private key**

  1. This becomes her **digital signature**
4. She sends Jonas:

  - The **original message**
  - Her **digital signature**
  - Her **digital certificate**
5. Jonas:

  - Uses Leila’s **public key** (from the certificate) to **verify the digital signature**
  - Uses the CA’s **public key** to verify that the certificate is genuine and hasn’t been forged

#### Summary

| Step | Purpose |
|---|---|
| Certificate issued by a CA | Proves the public key belongs to the sender |
| Certificate includes public key | Lets others verify digital signatures |
| CA’s digital signature on certificate | Shows it was issued by a trusted third party |
| Public verifies sender and message | Ensures authenticity and integrity of the message |

> **Exam Hint**
> - The digital certificate **proves ownership** of a public key
> - The digital signature** proves a message came from the claimed sender** and wasn’t altered
> 
> Don't mix them up!
