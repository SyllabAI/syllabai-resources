---
note_id: "rn_qV2BBjWR2xbPpM45"
title: "MAC Addresses & IP Addresses"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/3-hardware/network-hardware/mac-addresses-and-ip-addresses
path: 3-hardware/network-hardware/mac-addresses-and-ip-addresses
updated_at: "2025-09-09T11:45:14.501Z"
spec_point_ids: ["spcpt_3KZH24Gh7BtG9HWz", "spcpt_jzJ5C9rQFx3tx34W"]
spec_point_codes: []
guided_study: false
---

# MAC Addresses & IP Addresses

- Devices on a network send and receive data, a device needs an address to ensure it sends data to the correct place
- There are two types of network address systems:

  - **MAC Address **
  - **IP Address**

## MAC Addresses

> **Spec point** — `spcpt_3KZH24Gh7BtG9HWz` · "2 Understand what is meant by and the purpose of
a media access control (MAC) address, including
its structure"

## MAC Addresses

### What is a MAC address?

- A MAC (Media Access Control) address is a **unique identifier** given to devices which communicate over a local area network (**LAN**)
- A network interface card is given a MAC address at the point of manufacture
- MAC addresses are **static**, meaning they can never change
- MAC addresses make it possible for **switches **to efficiently **forward data** to the intended **recipient**
- Any device that contains a [Network Interface Card](https://www.savemyexams.com/gcse/computer-science/ocr/22/revision-notes/3-computer-networks-connections-and-protocols/networks-and-topologies/local-area-network-hardware/) (**NIC**) has a MAC address **assigned during manufacturing**
- A device connecting to a local network already has a MAC address, if it moves to a different network then the MAC address will stay the same

![mac-address-1](../../../assets/ab87ad8ffb5c-mac-address-1.png)

- A MAC address is represented as **12 hexadecimal digits** (48 bits), usually **grouped in pairs**
- The first three pairs are the **manufacturer ID number** (OUI) and the last three pairs are the **serial number **of the network interface card (**NIC**)
- There are enough unique MAC addresses for roughly **281 trillion devices**

## IP Addresses

> **Spec point** — `spcpt_jzJ5C9rQFx3tx34W` · "3 (a) Understand what is meant by and the
purpose of an internet protocol (IP) address
(b) Understand that there are different types of
IP address"

## IP Addresses

### What is an IP address?

- An IP (Internet Protocol) address is a **unique identifier** given to devices which communicate over the Internet (**WAN**)
- IP addresses can be **static**, meaning they stay the same or  **dynamic**, meaning they can change
- **Static IP** addresses are **commonly used for servers and websites** so they can always be found at the same address
- **Dynamic IP** addresses are **assigned automatically by a DHCP server** (Dynamic Host Configuration Protocol)
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

> **Worked Example**
> Computers in a network can be identified using both IP addresses and MAC addresses.
> 
> Describe two differences between IP addresses and MAC addresses **[2]**
> 
> **Answer**
> 
> - IP address is dynamic/can change // MAC address is static/cannot change
> - IP address is used to communicate on a WAN/Internet // MAC address is used to communicate on a LAN
