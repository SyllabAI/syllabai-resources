---
note_id: "rn_Jv4GfCgyDvx8ycVB"
title: "Calculating File Sizes"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/1-data-representation/data-storage-and-compression/calculating-file-sizes
path: 1-data-representation/data-storage-and-compression/calculating-file-sizes
updated_at: "2024-05-13T08:56:04.391Z"
spec_point_ids: ["spcpt_9chWxVfYNtCVTVhy"]
spec_point_codes: []
guided_study: false
---

# Calculating File Sizes

## Calculating File Sizes

> **Spec point** — `spcpt_9chWxVfYNtCVTVhy` · "2 Calculate the file size of an image file and a
sound file, using information given"

## Calculating File Sizes

### How do you calculate the size of a bitmap image?

- Calculating the size of a bitmap image can be carried out with either of the following formulas:

  - **Resolution x colour depth**
  - **Image width x image height x colour depth**

#### Example

| **Image Files** |
|---|
| (Resolution) **x** (Colour Depth) |
| \| **Size of bitmap image = ** \|   \|   \|<br>\|---\|---\|---\|<br>\| Resolution \| **250,000** \| Resolution = width x height \|<br>\| Colour Depth \| **24 bits (3 bytes)** \| 24 bits = 3 bytes \|<br>\| **250,000 x 24** \| **=**<br><br>***(bit to bytes)  /8***<br><br>***(bytes to KiB) /1024*** \| **6,000,000 bits**<br><br>**750,000 bytes**<br><br>**Final answer:** **732 KiB** \|<br>\| **250000  x 3** \| =<br><br>***(bytes to KiB) /1024*** \| **750,000 bytes**<br><br>**Final answer:** **732 KiB** \| |

**OR**

| **Image Files** |
|---|
| (Image width) **x** (Image height) **x** (Colour Depth) |
| \| **Size of bitmap image = ** \|   \|   \|<br>\|---\|---\|---\|<br>\| Image width \| **500** \|   \|<br>\| Image height \| **500** \|   \|<br>\| Colour Depth \| **24 bits** \| 24 bits = 3 bytes \|<br>\| **(500 x 500 x 24)** \| **=**<br><br>***(bit to bytes)  /8***<br><br>***(bytes to KiB) /1024*** \| **6,000,000 bits**<br><br>**750,000 bytes**<br><br>**Final answer:** **732 KiB** \|<br>\| **(500 x 500 x 3)** \| =<br><br>***(bytes to KiB) /1024*** \| **750,000 bytes**<br><br>**Final answer:** **732 KiB** \| |

### How do you calculate the size of a sound file?

- Calculating the size of a sound file is carried out with the following formula:

  - **Sample rate x duration x sample resolution**

#### Example

| **Sound Files** |
|---|
| (Sample Rate) **x** (Duration in seconds) **x **(Sample Resolution) |
| \| **Size of sound file = ** \|   \|   \|<br>\|---\|---\|---\|<br>\| Sample rate \| **100** \| Samples per second \|<br>\| Duration \| **60** \| Seconds \|<br>\| Sample resolution \| **24** \| Number of bits stored per sample \|<br>\| **100 x 60 x 24** \| **=**<br><br>***(bit to bytes)  /8***<br><br>***(bytes to KiB) /1024*** \| **144,000 bits**<br><br>**18,000 bytes**<br><br>**18 KiB** \| |
