---
note_id: "rn_wGxjmXZHCbPk4KGr"
title: "Data protection"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/6-security-privacy-and-data-integrity-/data-security/data-protection
path: 6-security-privacy-and-data-integrity-/data-security/data-protection
updated_at: "2025-04-24T09:17:45.863Z"
spec_point_ids: ["spcpt_7jM928mhSzWFBWTz"]
spec_point_codes: []
guided_study: false
---

# Data protection

## Data security techniques

> **Spec point** — `spcpt_7jM928mhSzWFBWTz`

## Data security techniques

### Access rights

- Access rights control **what users can see or do** on a network
- They ensure that users can **access the files and resources they need** for their role, and **can’t access information they shouldn’t**
- Access rights are assigned based on a user’s **role**, **responsibilities**, or **security clearance**

| **Access right** | **What it means** |
|---|---|
| **Full access** | The user can **open, create, edit, and delete** files or folders |
| **Read-only access** | The user can **open and view** files but **cannot edit or delete** them |
| **No access** | The user **cannot see or interact with** the file or folder at all |

#### Example: access rights on a school network

| **User group** | **Access rights** |
|---|---|
| **Administrators** | **Unrestricted access** – Can access and control all files, folders, and settings |
| **Teaching Staff** | **Partially restricted access** – Can access student data but not other staff files |
| **Students** | **Restricted access** – Can only access **their own files and folders** |

- Users can be **grouped **(e.g. “Year 11”, “Staff”, “Admin”) and given access rights as a group
- Access rights can be assigned to **files**, **folders**, or **whole systems**
- This helps protect **confidential data**, improves **network security**, and supports **efficient collaboration**

### Encryption

- Encryption is a method of **scrambling data **before being transmitted across a network in order to protect the contents from **unauthorised access**
- While encryption is important on both **wired** and **wireless **networks, it's even more critical on wireless networks due to the data being transmitted over radio waves, making it easy to **intercept**

#### How is wireless data encrypted?

- Wireless networks are identified by a 'Service Set Identifier' (**SSID**) which along with a password is used to create a '**master key**'
- When devices connect to the **same wireless network** using the SSID and password they are given a copy of the master key
- The master key is used to **encrypt **data into '**cipher text**', before being transmitted
- The receiver uses the same master key to **decrypt **the cipher text back to '**plain text**'
- To guarantee the security of data, the **master key is never transmitted**. Without it, any intercepted data is rendered useless
- Wireless networks use dedicated ***protocols*** like **WPA2 **specifically designed for **Wi-Fi** security

![wireless-encryption](../../../assets/c502973bd7e4-wireless-encryption.png)

#### How is wired data encrypted?

- Wired networks are encrypted in a very similar way to a wireless network, using a **master key to encrypt** data and the **same key to decrypt** data
- Encryption on a wired network differs slightly as it is often left to **individual applications to decide** how encryption is used, for example **HTTPS**
