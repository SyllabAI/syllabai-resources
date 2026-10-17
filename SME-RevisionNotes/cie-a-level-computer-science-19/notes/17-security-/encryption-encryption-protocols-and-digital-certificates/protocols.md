---
note_id: "rn_sbjMVvQkqTS2g6xs"
title: "Protocols"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/17-security-/encryption-encryption-protocols-and-digital-certificates/protocols
path: 17-security-/encryption-encryption-protocols-and-digital-certificates/protocols
updated_at: "2025-06-01T18:42:38.443Z"
spec_point_ids: ["spcpt_jC32rTS6sZ6SmccB"]
spec_point_codes: []
guided_study: false
---

# Protocols

## SSL/TLS

> **Spec point** — `spcpt_jC32rTS6sZ6SmccB`

## SSL/TLS

### What is SSL?

- SSL (Secure Sockets Layer) is a **security protocol** used to **encrypt data sent over the internet**
- Helps to prevent **eavesdropping**, **tampering**, or **man-in-the-middle attacks**
- Commonly used for:

  - **Protecting websites**
  - **Online payments**
  - **Login credentials**
- Creates a **secure connection** between a web server and a browser

## What is TLS?

- TLS (Transport Layer Security) is the **successor to SSL**
- It performs the **same functions** but is **more secure and efficient**

  - Modern websites use **TLS**, although people often still refer to it as “SSL”
  - When you see **HTTPS** in the browser, it means **TLS/SSL encryption is active**

#### How SSL/TLS works with digital certificates

1. When you visit a secure website (e.g. `https://`), the server sends your browser its **digital certificate**
2. The certificate contains:

  - The server’s **public key**
  - Information about the website and Certificate Authority (CA)
  - A **digital signature** from the CA
3. Your browser checks that the **certificate is valid and trusted** using the CA’s public key
4. If trusted, a **secure connection is established**, often using a shared secret key (symmetric encryption) created during the handshake

#### Summary: What a digital certificate does

| Component | Purpose |
|---|---|
| Public key | Used by your browser to create secure communication |
| Website identity | Shows who owns the key |
| Certificate Authority | Signs the certificate to confirm it's trustworthy |
| Browser validation | Uses the CA’s public key to verify the certificate |

> **Exam Hint**
> - TLS has replaced SSL — but both are encryption protocols used with digital certificates
> - Always mention digital certificates when explaining how websites create secure connections
