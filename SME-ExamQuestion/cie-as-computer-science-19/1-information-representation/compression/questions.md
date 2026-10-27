# Exam Questions — Compression
**1. Information representation** · Cambridge (CIE) AS computer-science (9618)
> Source: [https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/) · 9 questions across 1 sets


## Exam Questions (9 questions)


### Q1 — medium — 3 marks

**Q1** [3 marks]

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


### Q2 — medium — 2 marks

**Q2** [2 marks]

The program is distributed by downloading the source code and its library files from a web server.

Explain the reasons for compressing the files.

*Source: Nov 2023 9618/13 Q5B(I)*


### Q3 — medium — 3 marks

**Q3** [3 marks]

A real-time video of a music concert needs to be streamed to subscribers.

Tick (✓) one box to identify the most appropriate type of compression and justify your answer.

| Lossy | Lossless |
|---|---|
|   |   |

*Source: Nov 2023 9618/12 Q6A*


### Q4 — medium — 2 marks

**Q4** [2 marks]

Explain why a bitmap image is often compressed before it is attached to an email.

*Source: Nov 2023 9618/11 Q1C*


### Q5 — medium — 5 marks

**Q5** [5 marks]

The photograph is compressed before being uploaded to a web server.

(i) Give **three **benefits of this photograph being compressed using lossy compression instead of lossless compression.

(3)

(ii) Explain how run-length encoding (RLE) will compress the photograph.

(2)

*Source: June 2024 9618/13 Q1B*


### Q6 — medium — 2 marks

**Q6** [2 marks]

The computer can transmit a video made from bitmap images and vector graphic animations to the VR headset.

The bitmap video is not compressed before transmission to the VR headset.

Give **two **reasons why the video does **not** need to be compressed.

*Source: June 2024 9618/12 Q2D(III)*


### Q7 — medium — 2 marks

**Q7** [2 marks]

The colour of each pixel in a bitmapped image is represented by 8 bits.

A bitmap image can be compressed using lossy compression.

Explain the reasons why lossy compression is often suitable for a bitmap image.

*Source: Nov 2024 9618/13 Q6B(III)*


### Q8 — medium — 1 marks

**Q8** [1 mark]

Identify **one **lossless method of compressing an image.

*Source: Nov 2024 9618/12 Q7A(III)*


### Q9 — medium — 6 marks

**Q9** [6 marks]

A student uses a laptop to write a program that is saved as a text file.

The student compresses the file before it is emailed to their teacher as an attachment.

(i) Explain the benefits to the teacher of the attachment being a compressed file.

(3)

(ii) Describe **one **lossless method of compressing a text file.

(3)

*Source: Nov 2024 9618/11 Q1B*

