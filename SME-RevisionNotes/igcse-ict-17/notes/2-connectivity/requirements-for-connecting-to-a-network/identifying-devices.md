---
note_id: "rn_jFBRQSZD44DJSGg6"
title: "Identifying Devices"
source: https://www.savemyexams.com/igcse/ict/edexcel/17/revision-notes/2-connectivity/requirements-for-connecting-to-a-network/identifying-devices
path: 2-connectivity/requirements-for-connecting-to-a-network/identifying-devices
updated_at: "2024-06-05T08:29:15.012Z"
spec_point_ids: ["spcpt_fW54wQ3yjfQjHsgj", "spcpt_B8WrjnygkcNHC7NV", "spcpt_gfhYywxSGzQHXYkz"]
spec_point_codes: []
guided_study: false
---

# Identifying Devices

## IP Addresses

> **Spec point** — `spcpt_fW54wQ3yjfQjHsgj`

## IP Addresses

### What is an IP address?

- An IP (Internet Protocol) address is a **unique identifier** given to devices which communicate over the Internet (**WAN**)
- IP addresses can be allocated** by a network administrator** or assigned *dynamically* by a *Dynamic Host Configuration Protocol server* (**DHCP**)
- IP addresses make it possible to **deliver data to the right device**
- A device connecting to a network will be given an IP address, if it moves to a different network then the **IP address will change**

#### IPv4

- Internet Protocol version 4 is represented as **4 blocks of denary numbers** between **0 **and **255**, separated by **full stops**
- Each block is **one byte **(8 bits), each address is** 4 bytes** (32 bits)

![ipv4](../../../assets/c81a55b31bc4-ipv4.png)

- IPv4 provides over** 4 billion unique addresses **(2<sup>32</sup>), however, with over **7 billion** people and **countless devices per person**, a solution was needed

#### IPv6

- Internet Protocol version 6 is represented as **8 blocks of 4 hexadecimal digits**, separated by **colons**
- Each block is **2 bytes** (16 bits), each address is **16 bytes** (128 bits)

![-ipv6](../../../assets/4b6b55d41177-ipv6.png)

- IPv6 could provide over **one** **billion unique addresses** for **every person** on the planet (2<sup>128</sup>)

## MAC Addresses

> **Spec point** — `spcpt_B8WrjnygkcNHC7NV`

## MAC Addresses

### What is a MAC address?

- A MAC (Media Access Control) address is a **universally** **unique identifier** given to devices which communicate over a local area network (**LAN**)
- MAC addresses are **static**, they can never change
- MAC addresses make it possible for **switches **to efficiently **forward data** to the intended **recipient**
- Any device that contains a Network Interface Card (**NIC**) has a MAC address **assigned during manufacturing**
- A device connecting to a local network already has a MAC address, if it moves to a different network then the **MAC address will stay the same**

![mac-address-1](../../../assets/ab87ad8ffb5c-mac-address-1.png)

- A MAC address is represented as **12 hexadecimal digits** (48 bits), usually **grouped in pairs**
- The first three pairs are the **manufacturer ID number** (OUI) and the last three pairs are the **serial number **of the network interface card (**NIC**)
- There are enough unique MAC addresses for roughly **281 trillion devices**
- MAC addresses can be used to:

  - **Restrict or allow access to a network**
  - **Identify a device on a network**
  - **Track a device**
  - **Assign 'static' or 'fixed' IP addresses **

## Device name

> **Spec point** — `spcpt_gfhYywxSGzQHXYkz`

## Device name

### What is a device name?

- A device name is a way for users to **describe/name a device** so that it is **easier to identify on a network**
- Device names are not used by devices to communicate as **they are not always unique**
- Device names are** set by users** in the devices operating system or from a router

> **Worked Example**
> Computers in a network can be identified using both IP addresses and MAC addresses.
> 
> Describe two differences between IP addresses and MAC addresses
> 
> **[2]**
> 
> **Answer**
> 
> - IP address is dynamic/can change // MAC address is static/cannot change **[1]**
> - IP address is used to communicate on a WAN/Internet // MAC address is used to communicate on a LAN **[1]**
