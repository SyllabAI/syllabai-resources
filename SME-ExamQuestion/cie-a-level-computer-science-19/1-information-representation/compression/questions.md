# Exam Questions — Compression
**1. Information representation** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 21 questions across 1 sets


## Exam Questions (21 questions)


### Q1 — hard — 5 marks

**Q1** [5 marks]

One row of a bitmap photograph has a colour depth of 8 bits per pixel. The colour of each pixel is written as a two-digit hexadecimal value:

`1C 4E 90 22 FD 07 B3 6A`

The photograph is compressed using run-length encoding (RLE). Each RLE pair is written as the number of repeats followed by the colour value. In the compressed file, the count and the colour value are each stored in one byte.

(i) Write the RLE compressed data for this row.

(1)

(ii) Calculate the size of this row in bytes before compression and after compression.

(2)

(iii) Explain why run-length encoding is **not** appropriate for this row.

(2)

### Q2 — medium — 3 marks

**Q2** [3 marks]

One row of a bitmap image is stored with a colour depth of 8 bits per pixel. The row has been compressed using run-length encoding (RLE):

`4D2 2A7 6D2 1FF`

Each RLE pair is written as the number of repeats followed by the two-digit hexadecimal colour value. In the compressed file, the count and the colour value are each stored in one byte.

(i) Write the uncompressed data for this row.

(1)

(ii) Calculate the number of bytes saved by compressing this row using RLE.

Show your working.

(2)

### Q3 — easy — 2 marks

**Q3** [2 marks]

A bitmap image is stored with a colour depth of 8 bits per pixel. The colour of each pixel is written as a two-digit hexadecimal value.

The image is compressed using run-length encoding (RLE). Each RLE pair is written as the number of repeats followed by the colour value. For example, `33A` means three pixels of colour `3A`.

Complete the table. The first row has been completed for you.

| Uncompressed image data | RLE compressed image data |
|---|---|
| `3A 3A 3A B7 B7` | `33A 2B7` |
| `C4 C4 09 09 09 09 5E` |   |
|   | `2FF 1A0 3FF` |

### Q4 — hard — 6 marks

**Q4** [6 marks]

A publisher produces an online magazine. Three files are stored for each page of the magazine:

- a text file containing the article
- a bitmap photograph
- a vector graphic of the magazine logo

All three files are compressed before they are uploaded to the web server.

Complete the table by describing how each file can be compressed.

| File | Description of how the file can be compressed |
|---|---|
| Text file |   |
| Bitmap photograph |   |
| Vector graphic |   |

### Q5 — medium — 3 marks

**Q5** [3 marks]

A bitmap image is 2400 pixels wide and 1800 pixels high. The colour depth is 24 bits.

(i) Calculate an estimate for the size of the uncompressed image in megabytes (MB).

Show your working.

(2)

(ii) The image is compressed. The compressed image is 3.24 MB.

Calculate the percentage reduction in the size of the image.

(1)

### Q6 — easy — 2 marks

**Q6** [2 marks]

A music streaming service stores each song as a sound file. The sound files are compressed before they are stored on the company's servers.

Describe **two** ways in which compression can reduce the size of a sound file.

### Q7 — hard — 4 marks

**Q7** [4 marks]

A software company stores two files on a cloud server.

- **File A** is the installation program for the company's software. Customers download this file and run it to install the software.
- **File B** is a set of photographs of the company's products. The photographs are displayed on the company's website.

Both files are compressed before they are stored.

For each file, identify the most suitable type of compression and justify your choice.

### Q8 — medium — 3 marks

**Q8** [3 marks]

A student writes a long report. The report is saved as a text file.

The file is compressed before it is uploaded to a school website.

Explain why lossless compression must be used for this file and not lossy compression.

### Q9 — easy — 2 marks

**Q9** [2 marks]

State **two** differences between lossy compression and lossless compression.

### Q10 — hard — 4 marks

**Q10** [4 marks]

An online learning platform stores video lessons on a server. A student downloads a video lesson before watching it.

One uncompressed video lesson has a file size of 900 MB.

The platform compresses each video lesson to 30% of its original file size.

The student downloads at a data transfer rate of 12 megabits per second (Mb/s).

Use these values:

- 1 byte = 8 bits
- 1 MB = 1 000 000 bytes
- 1 Mb = 1 000 000 bits

Calculate the time, in seconds, that the student saves by downloading the compressed video lesson instead of the uncompressed video lesson.

Show your working.

### Q11 — medium — 3 marks

**Q11** [3 marks]

A weather station is in a remote area. It has no cable connection.

The weather station sends its sensor readings to a central server using a satellite link. The satellite link has a low data transfer rate and the owner pays for every megabyte that is sent.

The readings are stored in a large text file. The file is compressed before it is sent.

Explain why the file is compressed before it is sent.

### Q12 — easy — 2 marks

**Q12** [2 marks]

Files are compressed when they are stored and when they are sent across a network.

Define the term **compression**.

### Q13 — medium — 3 marks

**Q13** [3 marks]

Music is stored as a sequence of digital samples.

Each digital sample is a denary value in the range 0 to 99999999 (8 digits).

The samples are to be stored in a text file. Each sample is converted to a numeric string and 32 samples are concatenated (joined) to form a single line of the text file.

Each numeric string is 8 characters in length; leading ‘0’ characters are added as required.

Example:

| Sample | Denary value | String |
|---|---|---|
| 1 | `456` | `"00000456"` |
| 2 | `48` | `"00000048"` |
| 3 | `37652` | `"00037652"` |
| ![Simple black curved line on a white background, resembling an abstract shape with one gentle bend at the midpoint, creating an S-like form.](assets/001-simple-black-curved-line-on-a-white-background-r.png) | ![Simple black curved line on a white background, resembling an abstract shape with one gentle bend at the midpoint, creating an S-like form.](assets/001-simple-black-curved-line-on-a-white-background-r.png) | ![Simple black curved line on a white background, resembling an abstract shape with one gentle bend at the midpoint, creating an S-like form.](assets/001-simple-black-curved-line-on-a-white-background-r.png) |
| 32 | `673` | `"00000673"` |

The example samples will be stored in the text file as a single line:

`"000004560000004800037652...00000673"`

(i) Identify one drawback of adding leading ‘0’ characters to each numeric string.

(1)

(ii) Suggest an alternative method of storing the samples which does **not **involve adding leading ‘0’ characters but which would still allow each individual sample to be extracted.

(1)

(iii) State **one **drawback of the alternative method given in part **(b)(ii)**.

(1)

*Source: June 2024 9618/22 Q6B*


### Q14 — medium — 2 marks

**Q14** [2 marks]

The program is distributed by downloading the source code and its library files from a web server.

Explain the reasons for compressing the files.

*Source: Nov 2023 9618/13 Q5B(I)*


### Q15 — medium — 3 marks

**Q15** [3 marks]

A real-time video of a music concert needs to be streamed to subscribers.

Tick (✓) one box to identify the most appropriate type of compression and justify your answer.

| Lossy | Lossless |
|---|---|
|   |   |

*Source: Nov 2023 9618/12 Q6A*


### Q16 — medium — 2 marks

**Q16** [2 marks]

Explain why a bitmap image is often compressed before it is attached to an email.

*Source: Nov 2023 9618/11 Q1C*


### Q17 — medium — 5 marks

**Q17** [5 marks]

The photograph is compressed before being uploaded to a web server.

(i) Give **three **benefits of this photograph being compressed using lossy compression instead of lossless compression.

(3)

(ii) Explain how run-length encoding (RLE) will compress the photograph.

(2)

*Source: June 2024 9618/13 Q1B*


### Q18 — medium — 2 marks

**Q18** [2 marks]

The computer can transmit a video made from bitmap images and vector graphic animations to the VR headset.

The bitmap video is not compressed before transmission to the VR headset.

Give **two **reasons why the video does **not** need to be compressed.

*Source: June 2024 9618/12 Q2D(III)*


### Q19 — medium — 2 marks

**Q19** [2 marks]

The colour of each pixel in a bitmapped image is represented by 8 bits.

A bitmap image can be compressed using lossy compression.

Explain the reasons why lossy compression is often suitable for a bitmap image.

*Source: Nov 2024 9618/13 Q6B(III)*


### Q20 — medium — 1 marks

**Q20** [1 mark]

Identify **one **lossless method of compressing an image.

*Source: Nov 2024 9618/12 Q7A(III)*


### Q21 — medium — 6 marks

**Q21** [6 marks]

A student uses a laptop to write a program that is saved as a text file.

The student compresses the file before it is emailed to their teacher as an attachment.

(i) Explain the benefits to the teacher of the attachment being a compressed file.

(3)

(ii) Describe **one **lossless method of compressing a text file.

(3)

*Source: Nov 2024 9618/11 Q1B*

