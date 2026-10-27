---
note_id: "rn_CdFdXG8bK83R9DKB"
title: "Security measures"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/6-security-privacy-and-data-integrity-/data-security/security-measures
path: 6-security-privacy-and-data-integrity-/data-security/security-measures
updated_at: "2026-05-07T08:22:11.357Z"
spec_point_ids: ["spcpt_XDpr3szNcPW7PdyK", "spcpt_dTCKSSntqmpQVQ4j"]
spec_point_codes: []
guided_study: false
---

# Security measures

## Security, privacy, integrity

> **Spec point** — `spcpt_XDpr3szNcPW7PdyK`

## Security, privacy, integrity

### What is the difference between data security, privacy and integrity?

| Term | Definition | Key focus | Example |
|---|---|---|---|
| **Data Security** | Protecting data against **loss**, **damage**, or **corruption** | **Preventing **data from being lost or destroyed | Using backups, firewalls, and anti-malware to prevent data loss |
| **Data Privacy** | Protecting data against **unauthorised access** | **Controlling **who is allowed to access personal data | Using passwords, access rights, and encryption so only authorised users can read the data |
| **Data Integrity** | Ensuring data is **accurate**, **complete**, and **unaltered **during storage or transfer | **Maintaining **correctness and reliability | Using checksums or validation rules to detect accidental or unauthorised changes |

- **Security** = keeping data safe from being lost
- **Privacy** = keeping data safe from being seen by the wrong people
- **Integrity** = keeping data accurate and unchanged

## Protection techniques

> **Spec point** — `spcpt_dTCKSSntqmpQVQ4j`

## Protection techniques

### User accounts

- User accounts are designed to **control access** to computer systems
- They help protect data and system resources by ensuring only **authorised individuals** can log in and perform specific tasks

#### Passwords

- Passwords are a **digital lock** to prevent unauthorised access to an account
- They are often stored as an **encrypted/ciphered** text entry in a database, ensuring that even with unauthorised access to a database, a hacker would not be able to gain access to the individual passwords of users

### Authentication

- Authentication is the process of **ensuring that a system is secure** by asking the user to **complete tasks to prove they are an authorised** user of the system
- Authentication is done because **bots can submit data in online forms**
- Authentication can be done in several ways, including:

  - **Digital signatures**
  - **Biometrics**

#### Digital signatures

- A digital signature is a secure way to **prove that a digital message or document was sent by a specific person** and that it **has not been altered**
- It acts like a **digital stamp of approval**, confirming:

  - **Who sent the data** (authentication)
  - **That the data hasn’t been changed** (integrity)

#### Biometrics

- Biometrics are an individuals **personal characteristics used to identify them**, such as

  - **Fingerprints**
  - **Iris/retina scans (eyes)**
  - **Voice recognition**
- Biometrics provide a **very secure method** of confirming a users **identity **before allowing access/permission to a computer system
- Biometric measures are often **used on mobile devices **to provide secure access

### Firewall

- A firewall is a **barrier** between a network and the internet
- A firewall prevents **unwanted traffic** from entering a network by filtering requests to ensure they are **legitimate**
- It can be both **hardware** and **software** and they are often used together to provide stronger security to a network

  - **Hardware firewalls** will protect the whole network and prevent unauthorised traffic
  - **Software firewalls** will protect the individual devices on the network, monitoring the data going to and from each computer

### Anti-virus software

- Anti-virus software is a term used to describe a combination of different software to prevent computers from being susceptible to **viruses** and other **malicious software**
- Anti-virus **scans** through **email** attachments, **websites** and downloaded **files** to search for issues
- Anti-virus software has a list of known malware **signatures to block** immediately if they try to access your device in any way
- Anti-virus will also perform **checks for updates** to ensure the database of known issues is up to date

### Anti-spyware software

- Anti-spyware is a type of **security software** designed to **detect, block, and remove spyware** from a computer system
- Spyware is a type of **malicious software (malware)** that secretly gathers information about a user without their knowledge
- It can:

  - **Record keystrokes** (e.g. passwords, credit card numbers)
  - **Monitor browsing habits**
  - **Access files** and send them to a third party

### Encryption

- Encryption is the process of **converting data into a secret code** so that **only authorised users** can read it
- It protects sensitive information (like passwords, personal data, or messages) from **unauthorised access**, especially when data is stored or sent over a network

| **Type** | **Description** |
|---|---|
| **Symmetric** | The **same key** is used to encrypt and decrypt. Fast but key must be shared securely |
| **Asymmetric** | Uses a **public key** for encryption and a **private key** for decryption. More secure for sending data |

> **Worked Example**
> A company has several security measures in place to prevent unauthorised access to the data on its computers.
> 
> Describe the difference between the security and privacy of data.**[2]**
> 
> **Final answer:** **Answer**
> 
> - Security protects data against loss **[1 mark]**
> - Privacy protects data against unauthorised access  **[1 mark]**
