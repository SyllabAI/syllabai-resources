---
note_id: "rn_dCtWdyR97ZNMp5Nk"
title: "Use of Buffers"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/3-hardware-/computers-and-components/use-of-buffers
path: 3-hardware-/computers-and-components/use-of-buffers
updated_at: "2025-09-03T13:31:59.033Z"
spec_point_ids: ["spcpt_Mn5JDq5Pgp3sbfZC"]
spec_point_codes: []
guided_study: false
---

# Use of Buffers

## Buffers

> **Spec point** — `spcpt_Mn5JDq5Pgp3sbfZC`

## Buffers

### What is a buffer?

- A buffer is a **temporary storage area** that holds data **while it is being transferred** between two devices or processes
- Buffers help** manage speed differences** between components, ensuring smooth data flow

#### How buffers work

- Data is collected in the buffer **before **being processed or output
- When the **receiving device is ready**, it takes data from the buffer
- This **prevents data loss** and allows devices with **different speeds** to communicate effectively

#### Examples

| Buffer | Description |
|---|---|
| **Keyboard** | Stores keystrokes until the processor is ready to handle them |
| **Print** | Holds print jobs so the processor can move on while the printer outputs the data at its own speed |
| **Video** | Stores a portion of data before playback to prevent pauses caused by network delays |

> **Exam Hint**
> **Key points**
> 
> - Buffers are used to synchronise data transfer between fast and slow devices
> - They improve efficiency and avoid bottlenecks
> - Without buffers, data could be lost or delayed if one device is not ready to process information
