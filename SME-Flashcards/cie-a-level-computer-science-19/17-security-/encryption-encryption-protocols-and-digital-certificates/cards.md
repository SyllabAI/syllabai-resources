# Encryption, Encryption Protocols & Digital Certificates

Course: cie-a-level-computer-science-19 · Section: 17. Security

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/17-security-/encryption-encryption-protocols-and-digital-certificates/


## Card 1 — keyword_definition (`fl_96NKXTWB355HKcGR`)

**FRONT**

Define **encryption**.


**BACK**

Encryption is a method of **scrambling data before it is transmitted across a network**, protecting the contents from unauthorised access by **making the data meaningless**.


Spec links: `spcpt_YKWdkZyRCKkV3zsj`


## Card 2 — question_and_answer (`fl_yVfvXwsmw5XXzvKB`)

**FRONT**

Why is encryption even more critical on wireless networks?


**BACK**

Data is transmitted over **radio waves**, which makes it **easy to intercept**.


Spec links: `spcpt_YKWdkZyRCKkV3zsj`


## Card 3 — question_and_answer (`fl_fGRg2hm77Tzb226v`)

**FRONT**

What is the master key created from on a wireless network?


**BACK**

The **SSID** together with the **password**.


Spec links: `spcpt_YKWdkZyRCKkV3zsj`


## Card 4 — keyword_definition (`fl_Q33XnjZSWyzDbKGb`)

**FRONT**

Define **cipher text**.


**BACK**

Cipher text is data that has been **encrypted using the master key**, before it is transmitted.


Spec links: `spcpt_YKWdkZyRCKkV3zsj`


## Card 5 — true_or_false (`fl_RGwwMkjtv5FjGDQN`)

**FRONT**

**True or False?**

The master key is transmitted along with the data.


**BACK**

**False.**

The master key is **never transmitted**. Without it, any intercepted data is rendered useless.


Spec links: `spcpt_YKWdkZyRCKkV3zsj`


## Card 6 — question_and_answer (`fl_4jsTtR89j7h6xYdT`)

**FRONT**

How does wired encryption differ from wireless encryption?


**BACK**

It is often left to **individual applications to decide** how encryption is used, for example HTTPS.


Spec links: `spcpt_YKWdkZyRCKkV3zsj`


## Card 7 — question_and_answer (`fl_MjBTf6MysTDnfPtS`)

**FRONT**

How does symmetric encryption work?


**BACK**

The sender uses a key to **encrypt** the data before transmission, and the receiver **uses the same key** to **decrypt** it.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 8 — question_and_answer (`fl_ZgWVfh4GY5VwP3x9`)

**FRONT**

Why is symmetric encryption ideal for large amounts of data?


**BACK**

It is usually **faster**.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 9 — question_and_answer (`fl_j76gKTM56RvSwjdp`)

**FRONT**

What is the significant downside of symmetric encryption?


**BACK**

The challenge of **securely sharing the key** between the sender and the receiver.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 10 — fill_in_the_blanks (`fl_F8fmhVjRxNGMVmp9`)

**FRONT**

Symmetric encryption is fast but has key-<u>**              **</u> issues.


**BACK**

Symmetric encryption is fast but has key-**sharing** issues.


*Blanks: 1 — answers: []*

Spec links: `spcpt_Kff6dyNm2C3y8JYR`

Flags: blank_answer_mismatch


## Card 11 — question_and_answer (`fl_QpZJBwBrBJkxWwCc`)

**FRONT**

What happens if a bad actor captures a symmetric key?


**BACK**

They can **decrypt all messages intercepted** in transmission.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 12 — question_and_answer (`fl_cDbNQ7WKZfKbgR8R`)

**FRONT**

How does asymmetric encryption work?


**BACK**

It uses **two keys**: a **public key for encryption** and a **private key for decryption**.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 13 — true_or_false (`fl_nmgSH2nSQxNn8HkH`)

**FRONT**

**True or False?**

Asymmetric encryption uses the same key to encrypt and decrypt.


**BACK**

**False.**

It uses a **public key to encrypt** and a **private key to decrypt**. It is **symmetric** encryption that uses the same key for both.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 14 — question_and_answer (`fl_3j6pzrzv2nVRSFXD`)

**FRONT**

Who shares the public key, and who keeps the private key?


**BACK**

**Receivers openly share their public key**. The **receiver's private key** is kept locally and is the only key that can decrypt the data.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 15 — question_and_answer (`fl_zc3NZcDnpc9TnTYF`)

**FRONT**

How are the public and private keys created?


**BACK**

**At the same time**, and they are **designed to work together**.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 16 — question_and_answer (`fl_DXS397T3WSddjzvY`)

**FRONT**

How does asymmetric encryption compare with symmetric for speed?


**BACK**

It is typically **slower than symmetric encryption**.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 17 — question_and_answer (`fl_DNRQY5NFqwVWr7W2`)

**FRONT**

What is asymmetric encryption generally used for?


**BACK**

**More secure and smaller data transactions**, such as passwords and bank details.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 18 — question_and_answer (`fl_76YhTQr8PN2t7zrc`)

**FRONT**

When would you choose symmetric encryption?


**BACK**

For **large files and databases**, because it is fast and efficient for bulk data, and where **the same person encrypts and decrypts**, such as backing up data.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 19 — question_and_answer (`fl_pVXyfGrqxmjMDTDv`)

**FRONT**

When would you choose asymmetric encryption?


**BACK**

For **confidential or secret communications**, such as passwords or government communications.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 20 — question_and_answer (`fl_CTfmFNnqNhJyGbgc`)

**FRONT**

Describe the purpose of asymmetric key cryptography.


**BACK**

To provide **better security** by using **two different keys**, a public key and a private key. **One key encrypts** the message and **the matching key decrypts** it.


Spec links: `spcpt_Kff6dyNm2C3y8JYR`


## Card 21 — keyword_definition (`fl_2KCGDsYcdgsDzvq5`)

**FRONT**

Define **quantum cryptography**.


**BACK**

Quantum cryptography uses **quantum mechanics to securely transmit encryption keys**.


Spec links: `spcpt_cNf6KNtZmJ4yMYZD`


## Card 22 — question_and_answer (`fl_WKPcPFhXX4MSHqSV`)

**FRONT**

What is the main goal of quantum cryptography?


**BACK**

To enable **unbreakable communication** by **detecting any attempt to intercept or tamper with the key**.


Spec links: `spcpt_cNf6KNtZmJ4yMYZD`


## Card 23 — keyword_definition (`fl_s69FgvnmDtxNN3ng`)

**FRONT**

Define **Quantum Key Distribution (QKD)**.


**BACK**

QKD uses **quantum particles, such as photons, to share a secret key** between two parties securely.


Spec links: `spcpt_cNf6KNtZmJ4yMYZD`


## Card 24 — fill_in_the_blanks (`fl_f3tfqYsGZY2RxgsB`)

**FRONT**

The best known quantum method is Quantum <u>**        **</u> Distribution.


**BACK**

The best known quantum method is Quantum **Key** Distribution.


*Blanks: 1 — answers: []*

Spec links: `spcpt_cNf6KNtZmJ4yMYZD`

Flags: blank_answer_mismatch


## Card 25 — question_and_answer (`fl_fDVdvqQFTF26QJVR`)

**FRONT**

Why is quantum key transmission unbreakable?


**BACK**

**Measuring a quantum state disturbs it**, so any eavesdropping is **detectable** and alerts the users.


Spec links: `spcpt_cNf6KNtZmJ4yMYZD`


## Card 26 — keyword_definition (`fl_fqn8FfnKjggzPpSK`)

**FRONT**

Define **perfect forward secrecy**.


**BACK**

Keys are **used once and then discarded**, which reduces the impact of future key leaks.


Spec links: `spcpt_cNf6KNtZmJ4yMYZD`


## Card 27 — question_and_answer (`fl_fTXzrMFTt2d7P4rJ`)

**FRONT**

Why is quantum cryptography stronger than classical encryption?


**BACK**

It is **not based on mathematical problems** like factoring large primes, so it is not vulnerable to advances in computing such as quantum computers.


Spec links: `spcpt_cNf6KNtZmJ4yMYZD`


## Card 28 — question_and_answer (`fl_QzYnV7tXcGX5yS3K`)

**FRONT**

Name three drawbacks of quantum cryptography.


**BACK**

It is **expensive and complex**, works only over **short distances**, has a **slow transmission speed**, is **still evolving**, and **only secures key exchange**.


Spec links: `spcpt_cNf6KNtZmJ4yMYZD`


## Card 29 — true_or_false (`fl_CmywvMkkSSbKbvqg`)

**FRONT**

**True or False?**

Quantum cryptography encrypts the message itself.


**BACK**

**False.**

It secures the **key** used in encryption. **Traditional algorithms are still needed** for the actual data encryption.


Spec links: `spcpt_cNf6KNtZmJ4yMYZD`


## Card 30 — keyword_definition (`fl_VKHm6DCcmsYFhJQh`)

**FRONT**

Define **SSL**.


**BACK**

Secure Sockets Layer is a **security protocol used to encrypt data sent over the internet**.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 31 — question_and_answer (`fl_RMG9mbFfHZrfgmNt`)

**FRONT**

Which three attacks does SSL help prevent?


**BACK**

**Eavesdropping**, **tampering** and **man-in-the-middle attacks**.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 32 — question_and_answer (`fl_JVnP4WqXzrSTjrDY`)

**FRONT**

Name three common uses of SSL.


**BACK**

**Protecting websites**, **online payments** and **login credentials**.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 33 — question_and_answer (`fl_xKFGwH73m2TBKQPd`)

**FRONT**

What does SSL create?


**BACK**

A **secure connection between a web server and a browser**.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 34 — keyword_definition (`fl_QsWFRZGkPDPWJjx9`)

**FRONT**

Define **TLS**.


**BACK**

Transport Layer Security is the **successor to SSL**. It performs the same functions but is **more secure and efficient**.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 35 — true_or_false (`fl_WjsM5ss5dgCSvxFh`)

**FRONT**

**True or False?**

TLS and SSL are unrelated protocols.


**BACK**

**False.**

**TLS is the successor to SSL** and performs the same functions, more securely and efficiently.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 36 — question_and_answer (`fl_zsH4QWwPzXwPr5jg`)

**FRONT**

Which do modern websites use, SSL or TLS?


**BACK**

**TLS**, although people often still refer to it as 'SSL'.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 37 — question_and_answer (`fl_HjrPfxBgzkY7ZK3j`)

**FRONT**

What does HTTPS in the browser mean?


**BACK**

That **TLS/SSL encryption is active**.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 38 — question_and_answer (`fl_PjkHTSPjzztThnTm`)

**FRONT**

What is the first step when you visit a secure website?


**BACK**

The server sends your browser its **digital certificate**.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 39 — question_and_answer (`fl_zD7234x85cqhQ96g`)

**FRONT**

Name the three things a digital certificate contains.


**BACK**

The server's **public key**, information about the **website and the Certificate Authority (CA)**, and a **digital signature from the CA**.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 40 — question_and_answer (`fl_fqh2xm7TP7ZB3TQQ`)

**FRONT**

How does the browser check the certificate?


**BACK**

It checks that the certificate is **valid and trusted**, using the **CA's public key**.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 41 — fill_in_the_blanks (`fl_QpmKrVc6PwP22dJ2`)

**FRONT**

The browser uses the CA's <u>**            **</u> key to verify the certificate.


**BACK**

The browser uses the CA's **public** key to verify the certificate.


*Blanks: 1 — answers: []*

Spec links: `spcpt_jC32rTS6sZ6SmccB`

Flags: blank_answer_mismatch


## Card 42 — question_and_answer (`fl_cpqKvPpJFv59Z4j2`)

**FRONT**

What happens if the certificate is trusted?


**BACK**

A **secure connection is established**, often using a **shared secret key** created during the handshake.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 43 — question_and_answer (`fl_ZG9ppJgDffXZRH9d`)

**FRONT**

Which type of encryption is used for the shared secret key?


**BACK**

**Symmetric** encryption.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 44 — question_and_answer (`fl_gv5CQ5Bdv2bndy8b`)

**FRONT**

What is the purpose of the public key in a certificate?


**BACK**

It is **used by the browser to create secure communication**.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 45 — question_and_answer (`fl_2j2t9n73vpqQTBXb`)

**FRONT**

What does the Certificate Authority do?


**BACK**

It **signs the certificate** to confirm that it is trustworthy.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 46 — true_or_false (`fl_j3Q6ZpRg2tGvrxg6`)

**FRONT**

**True or False?**

The website identity in a certificate shows who owns the public key.


**BACK**

**True.**

The website identity **shows who owns the key**.


Spec links: `spcpt_jC32rTS6sZ6SmccB`


## Card 47 — keyword_definition (`fl_cWGdskpDnNRQ9cBQ`)

**FRONT**

Define **digital certificate**.


**BACK**

A digital certificate is an **electronic file that confirms someone's identity** and proves that a **public key belongs to them**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 48 — question_and_answer (`fl_FDprc2gWZS9ZJHRQ`)

**FRONT**

Who issues a digital certificate?


**BACK**

A trusted third party called a **Certificate Authority (CA)**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 49 — fill_in_the_blanks (`fl_QnB36n2Jfd955VGY`)

**FRONT**

A digital certificate is issued by a trusted third party called a Certificate <u>**                  **</u>.


**BACK**

A digital certificate is issued by a trusted third party called a Certificate **Authority**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_9HZjnCMwpRjvrzpc`

Flags: blank_answer_mismatch


## Card 50 — question_and_answer (`fl_kGxGtwTM87M9hCkf`)

**FRONT**

Name the four things a digital certificate includes.


**BACK**

The owner's **public key**, the owner's **identity details**, the **expiry date**, and the **Certificate Authority's digital signature**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 51 — keyword_definition (`fl_VtF2Ts9f3HdKsz4j`)

**FRONT**

Define **hash function**.


**BACK**

A hash function is a **one-way algorithm** that takes an input and produces a **fixed-length output**, called a hash value or message-digest.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 52 — question_and_answer (`fl_gZSBpzBy7fQy35Rt`)

**FRONT**

Name three key features of a hash function.


**BACK**

The output is **always the same length** regardless of input size, it is **one-way** so cannot be reversed, and **even a small change in input produces a completely different output**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 53 — true_or_false (`fl_BD7V4NMgJ5srMj68`)

**FRONT**

**True or False?**

A hash function can be reversed to recover the original message.


**BACK**

**False.**

It is **one-way**. You cannot reverse it to get the original input.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 54 — question_and_answer (`fl_49ZpTxjXb34YjtHG`)

**FRONT**

Why is a hash function like a fingerprint for data?


**BACK**

Because the output is **unique to the input**, and even a small change in the input produces a completely different output.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 55 — question_and_answer (`fl_hfH43CGmRwC6Yb7v`)

**FRONT**

Name two common uses of hash functions.


**BACK**

**Digital signatures** and **password storage**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 56 — keyword_definition (`fl_Vh78Gx5QpKtmjHVP`)

**FRONT**

Define **message-digest**.


**BACK**

A message-digest is the **output, or hash value, produced when a message is processed through a hash function**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 57 — question_and_answer (`fl_krPvHXxtShBkSJkh`)

**FRONT**

Name three properties of a message-digest.


**BACK**

It is a **fixed-length summary** of the original message, it is **unique to the message**, and it is used to **check whether a message has been altered**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 58 — question_and_answer (`fl_JbXRJXcPHHpTmnx8`)

**FRONT**

What is the first step in acquiring a digital certificate?


**BACK**

The person **generates a key pair**: one private key and one public key.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 59 — keyword_definition (`fl_z2fBv3kV6PwQJ77g`)

**FRONT**

Define **Certificate Signing Request (CSR)**.


**BACK**

A request sent to a Certificate Authority containing the sender's **public key and identity details**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 60 — question_and_answer (`fl_2CT8pGRgSsFSWm2q`)

**FRONT**

What does the CA do with a Certificate Signing Request?


**BACK**

It **verifies the identity** using documents or other checks. If approved, it **digitally signs a certificate** and sends it back.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 61 — question_and_answer (`fl_zZQKBjXnGyt27FFp`)

**FRONT**

What does the returned certificate contain?


**BACK**

The owner's **public key**, their **identity**, and the **CA's signature**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 62 — question_and_answer (`fl_Gk9Tb7k4MFKwNybK`)

**FRONT**

How is a digital signature produced?


**BACK**

A **hash function** is applied to the message to create a **message-digest**, which is then **encrypted using the sender's private key**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 63 — fill_in_the_blanks (`fl_NvgWthCG7ywCXFKC`)

**FRONT**

The digital signature is the message-digest encrypted with the sender's <u>**              **</u> key.


**BACK**

The digital signature is the message-digest encrypted with the sender's **private** key.


*Blanks: 1 — answers: []*

Spec links: `spcpt_9HZjnCMwpRjvrzpc`

Flags: blank_answer_mismatch


## Card 64 — question_and_answer (`fl_3VPBh25FR3RGZChk`)

**FRONT**

What three things does the sender send?


**BACK**

The **original message**, their **digital signature**, and their **digital certificate**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 65 — question_and_answer (`fl_9x9k2zrb3fZCmSry`)

**FRONT**

How does the recipient verify the digital signature?


**BACK**

Using the **sender's public key**, taken from the digital certificate.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 66 — question_and_answer (`fl_jMWM56D7RfGrRYmq`)

**FRONT**

How does the recipient verify that the certificate is genuine?


**BACK**

Using the **CA's public key**, which confirms the certificate has not been forged.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 67 — question_and_answer (`fl_dbQnRWDrtkrwNNNJ`)

**FRONT**

What is the difference between a digital certificate and a digital signature?


**BACK**

A **certificate proves ownership of a public key**. A **signature proves a message came from the claimed sender** and was not altered.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`


## Card 68 — true_or_false (`fl_bdJdNDQYZGsjzBJy`)

**FRONT**

**True or False?**

A digital certificate proves that a message has not been altered.


**BACK**

**False.**

That is what a **digital signature** does. A **certificate proves ownership of a public key**.


Spec links: `spcpt_9HZjnCMwpRjvrzpc`

