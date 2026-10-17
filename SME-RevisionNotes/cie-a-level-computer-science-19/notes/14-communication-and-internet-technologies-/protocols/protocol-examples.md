---
note_id: "rn_s3Mqfghfj6VFdqkk"
title: "Protocol Examples"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/14-communication-and-internet-technologies-/protocols/protocol-examples
path: 14-communication-and-internet-technologies-/protocols/protocol-examples
updated_at: "2026-10-01T13:14:07.867Z"
spec_point_ids: ["spcpt_yBvfCkxCYJPX6n34"]
spec_point_codes: []
guided_study: false
---

# Protocol Examples

## Standard protocols

> **Spec point** — `spcpt_yBvfCkxCYJPX6n34`

## Standard protocols

- A protocol is a **set of rules** that govern **communication **on a network
- There are protocols for different purposes, such as:

  - **HTTP & HTTPS**
  - **FTP**
  - **POP3, IMAP & SMTP**
  - **BitTorrent**

### HTTP & HTTPS

- Hypertext Transfer Protocol (**HTTP**) allows communication between clients and servers for **website viewing**
- HTTP allows clients to **receive data** from the server (fetching a webpage) and **send data** to the server (submitting a form, uploading a file)
- **HTTPS **works in the same way as HTTP but with an **added layer of security**
- All data sent and received using HTTPS is **encrypted**
- HTTPS is used to **protect sensitive information **such as passwords, financial information and personal data

![http](../../../assets/89eaa5dc4237-http.png)

### FTP

- File Transfer Protocol (**FTP**) allows **sending and receiving files between computers**
- Uploading and downloading files** to/from a web server** is often completed using FTP
- FTP offers **greater efficiency** and support for **bulk transfers and large files** such as resuming interrupted transfers
- **FTP clients **are software applications that use the FTP protocol to make the process easier for users

![ftp](../../../assets/7c4154c7f60d-ftp.png)

### POP3, IMAP & SMTP

- A family of protocols that handle **sending and receiving of email** across the internet (WAN)

![imapi-1](../../../assets/30ade2c2fb10-imapi-1.png)

#### SMTP

- SMTP is a **push protocol**: it is used for **sending (uploading) emails**
- In the diagram above, **SMTP** is used to transfer the senders email to their email providers server and SMTP is used to transfer the email to the recipients email server

#### POP3

- POP3 is a **pull protocol**: it is used for **receiving (downloading) emails** from a mail server
- Once the email has been retrieved **it is removed from the server**

#### IMAP

- IMAP is also a **pull protocol** used for **receiving (downloading) emails** from a mail server
- Once the email has been retrieved, **a copy is retained on the mail server**

### BitTorrent

- BitTorrent is a protocol for **peer-to-peer file sharing** over a network
- It allows files to be shared between **thousands of users** who are connected together over the internet
- Users **share files directly with each other**: the users' computers act as **peers**
- **No web server or central device** is used, and all users are of **equal status**
- This makes it efficient for sharing **large files**, as no single server has to supply the whole file to everyone
- While BitTorrent is a legal technology, it is sometimes used for sharing **copyrighted content illegally**, so ethical and legal use is important
