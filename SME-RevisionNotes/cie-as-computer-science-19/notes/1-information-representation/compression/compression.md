---
note_id: "rn_yXms9PZTq9fDHnnF"
title: "Compression"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/1-information-representation/compression/compression
path: 1-information-representation/compression/compression
updated_at: "2025-04-01T10:41:28.760Z"
spec_point_ids: ["spcpt_jvdKMHxvtM9crtGx", "spcpt_87TFdzgnwr8ybjNV"]
spec_point_codes: []
guided_study: false
---

# Compression

## The need for compression

> **Spec point** — `spcpt_jvdKMHxvtM9crtGx`

## The need for compression

### What is compression?

- Compression is **reducing the the size of a file** so that it **takes up less space on secondary storage**
- There are scenarios where compression may be needed, such as:

  - **Maximise the amount of data you can store** on a digital device such as a mobile phone or tablet
  - **Minimise the transfer time** of data being uploaded, downloaded or streamed across a network such as the Internet
- Compression can be achieved using two methods, **lossy **and **lossless**

## Lossy vs lossless

> **Spec point** — `spcpt_87TFdzgnwr8ybjNV`

## Lossy vs lossless

### What is lossy compression?

- Lossy compression is when** data is lost **in order to **reduce the size** on secondary storage
- Lossy compression is ***irreversible***
- Lossy can** greatly reduce the size** of a file but at the **expense of losing quality**
- Lossy is only suitable for data **where reducing quality is acceptable**, for example images, video and sound
- In photographs, lossy compression **will try to group similar colours together**, reducing the amount of colours in the image without compromising the overall quality of the image

![lossy-images](../../../assets/24b51f018c49-lossy-images.png)

- In the images above, lossy compression is applied to a photograph and **dramatically reduces the file size**
- **Data has been removed** and the **overall quality has been reduced**, however it is acceptable as it is difficult to visually see a difference
- Lossy compressed photographs** take up less storage space** which means you can store more and they are quicker to share across a network

### What is lossless compression?

- Lossless compression is when data is ***encoded*** in order to **reduce the size on secondary storage**
- Lossless compression is **reversible**, the file** can be returned to its original state**
- Lossless can reduce the size of a file but not as dramatically as lossy
- Lossless can be used on all data but is more suitable for data where **a loss in quality is unacceptable**, for example documents
- In a document, lossless compression uses algorithms to analyse the contents looking for **patterns **and **repetition**

![lossless-compression-demo---word-vs-pdf](../../../assets/8b39b5eae7eb-lossless-compression-demo-word-vs-pdf.png)

- In the image above, lossless compression is **automatically applied **to document formats such as **DOCX** and **PDF **with a different rate of success
- When you open a lossless compressed document the **decompression process reverses the algorithms** and returns the data back to its **original state**
- Lossless compressed documents **take up less storage space** which means you can store more and they are quicker to share across a network
