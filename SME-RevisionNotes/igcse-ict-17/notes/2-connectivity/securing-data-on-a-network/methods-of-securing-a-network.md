---
note_id: "rn_MJVshRTptpphchc3"
title: "Methods of Securing a Network"
source: https://www.savemyexams.com/igcse/ict/edexcel/17/revision-notes/2-connectivity/securing-data-on-a-network/methods-of-securing-a-network
path: 2-connectivity/securing-data-on-a-network/methods-of-securing-a-network
updated_at: "2024-06-06T10:01:30.109Z"
spec_point_ids: ["spcpt_TPScn6pDNHsdH5Dr", "spcpt_4qy7Mn5XyGxPKyjg", "spcpt_kjQQg6Jznnzk6V43", "spcpt_Yn9mhNZ8jSyR9fDG", "spcpt_ddx3BWGYZdp5wXWV", "spcpt_Yt7xJs4SJZHNqWDR", "spcpt_JQ6KRbKBkpCYFrXx"]
spec_point_codes: []
guided_study: false
---

# Methods of Securing a Network

## Usernames & Passwords

> **Spec point** — `spcpt_TPScn6pDNHsdH5Dr`

## Usernames & Passwords

### How does a password help?

- Passwords are a **digital lock** to prevent unauthorised access to an account
- Passwords are used to ***authenticate***** **a user to the network
- They are often stored as an **encrypted/ciphered** text entry in a database, ensuring that even with unauthorised access to a database, a hacker would not be able to gain access to the individual passwords of users
- **Strong passwords **and** regular password changes **are important to maintain security

![image-1-](../../../assets/e94d7475f65f-image-1.png)

## Firewalls

> **Spec point** — `spcpt_4qy7Mn5XyGxPKyjg`

## Firewalls

### What is a firewall?

- A firewall is a **barrier** between a network and the internet
- A firewall prevents **unwanted traffic** from entering a network by filtering requests to ensure they are **legitimate**
- It can be both **hardware** and **software** and they are often used together to provide stronger security to a network

  - **Hardware firewalls** will protect the **whole network** and prevent unauthorised traffic
  - **Software firewalls** will protect the** individual devices** on the network, monitoring the data going to and from each computer

## Encryption

> **Spec point** — `spcpt_kjQQg6Jznnzk6V43`

## Encryption

### What is encryption?

- Encryption is a method of **scrambling data **so that **unauthorised users cannot understand it **
- Encryption methods use **'keys'**, which are specialised programs designed to **scramble** or **unscramble** data
- Encryption uses **complex mathematical algorithms** to scramble the data
- There are two common methods of encryption:

  - **Symmetric**
  - **Public key**

#### Symmetric encryption

- The sender uses a key to **encrypt** the data before transmission
- The receiver **uses the same key** to **decrypt** the data
- It's usually **faster**, making it ideal for encrypting **large amounts of data**
- The significant downside is **the challenge of securely sharing this key** between the sender and receiver
- If an** unauthorised user** captures the key, they can **decrypt all messages intercepted** in transmission

![Image showing the structure of symmetric encryption](../../../assets/6af35e18c0be-20583-utility-software-file-encryption-alevel.avif)

*Structure of Symmetric Encryption*

#### Public key encryption

- Public key encryption uses **two keys**:

  - a **public key** for encryption
  - and a **private key** for decryption
- **Receivers** openly share** **their** public key**
- **Senders** use this public key to **encrypt** the data
- The **receiver's private key** is the **only key **that can decrypt the data and is kept locally on their side
- The public and private keys are created at the same time and are **designed to work together** in this way
- It is typically **slower than symmetric encryption**
- It is generally used for **more secure and smaller **data transactions, e.g. **passwords**, **bank details**

![Image showing the structure of public key encryption ](../../../assets/16f53a8cf94d-46907-asymmetric-encryption-public-key-private-k.avif)

*Structure of Public Key Encryption*

## WEP/WPA

> **Spec point** — `spcpt_Yn9mhNZ8jSyR9fDG`

## WEP/WPA

### What is WEP?

- **Wireless Encryption Protocol** (WEP) is a method of** encrypting data** being transmitted on a** wireless** network
- Each device on the network **uses the same key** to encrypt and decrypt data
- It is a **less secure** encryption method due to all devices on the network** sharing the same key**
- **Eavesdropping software** (packet sniffers) can be used to **intercept data packets **and** identify the key**

### What is WPA?

- **Wi-fi Protected Access** (WPA) is a **more secure** method of **encrypting data** being transmitted on a **wireless **network
- Each device connected to the network receives **a different key**
- New keys are used for** every packet** transmitted on the network

## Virtual private networks (VPN)

> **Spec point** — `spcpt_ddx3BWGYZdp5wXWV`

## Virtual private networks (VPN)

### What is a VPN?

- A VPN allows users to **remotely** connect to **private **local area networks** (LANs)**
- All **data sent and received** using a VPN is **encrypted**
- Common uses of a VPN include:

  - **Remotely accessing a companies network** (working from home)
  - Making **secure payments**
  - **Hiding web activities**
  - **Bypassing** *geolocation rights management* or **online censorship**

## File access rights

> **Spec point** — `spcpt_Yt7xJs4SJZHNqWDR`

## File access rights

### What are file access rights?

- File access rights can be set to determine** different levels of access **to specific files/folders
- Examples of file permissions include:

  - **Read **- can read the contents of a file only
  - **Write **- can make changes to file contents and/or create new files
  - **Delete **- can delete files
  - **Execute **- can run applications/launch software

## Transaction logs & backups

> **Spec point** — `spcpt_JQ6KRbKBkpCYFrXx`

## Transaction logs & backups

### What is a transaction log?

- A transaction log is **a secure file** on a network that keeps **a record of every action **performed by devices on a network
- Transactions logs include:

  - **Device & data access**
  - **Timestamps**
  - **User IDs**
  - **Successful/failed login attempts**
- Transaction logs** don't directly protect a network**, they help administrators **monitor any identify** any unusual activity
- **Backups **are another** indirect method of protecting a network**
- Keeping **copies of data in a secure place** on the network in the event of a **data breach/loss**

> **Worked Example**
> Describe one method that could be used to secure payment data transferred between a server and other computers
> 
> **[3]**
> 
> **Answer**
> 
> > *A description to include three linked points: *
> 
> - Encryption **[1]** encodes/scrambles data / makes data unreadable **[1]** using a key **[1]**
