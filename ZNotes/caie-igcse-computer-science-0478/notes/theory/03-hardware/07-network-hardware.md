## Network Hardware

### **Network Interface Card (NIC)**

* A network interface card (NIC) is needed to allow a device to connect to a network (such as the Internet).

* The NIC allows the computer to send out data to the network and receive data coming in from the network.

* The NIC takes the network data and changes it into the electrical/radio signals so it can be send over the network and when NIC receives electrical/radio signals it is converted to network data so it can be understood by the computer.

* Other purposes include : 

  * **Transmit**/**send** data to the network/devices // **Receive** data from the

    network/devices

  * To allow a **physical** connection

  * Convert network data so it can be understood by the computer

  * Convert computer data to be transmitted over the network

  * To be assigned an IP address

### **Media Access Control (MAC)**

A MAC address comprises 48 bits which are shown as six groups of hexadecimal digits. The first six display the manufacturer’s code, and the second half shows the device serial number.

* These do not change and are primarily constant for every device
* there are two types of MAC addresses: the Universally Administered MAC Address (UAA) and the Locally Administered MAC Address (LAA)

The only difference between the two types is that UAA is made Universally and cannot be changed, but it is the opposite for LAA.

### **IP Addresses**

* IP address allocation:
  * The network allocates IP addresses.
  * Two types of IP addresses: static and dynamic.
* Static IP addresses:
  * Assigned manually to a device.
  * Does not change over time.
* Dynamic IP addresses:
  * Assigned automatically by a DHCP (Dynamic Host Configuration Protocol) server.
  * Changes periodically or when the device connects to a different network.
* IPv4 (Internet Protocol version 4):
  * Widely used protocol.
  * Consists of four groups of decimal numbers separated by dots (e.g., 192.168.0.1).
  * Provides approximately 4.3 billion unique addresses.
* IPv6 (Internet Protocol version 6):
  * Developed to address the limitations of IPv4.
  * Uses eight groups of hexadecimal numbers separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
  * Provides an extremely large number of unique addresses (approximately 340 undecillion).
* Differences between IPv4 and IPv6:
  * Address format: IPv4 uses a 32-bit address, while IPv6 uses a 128-bit address.
  * Address space: IPv4 provides approximately 4.3 billion addresses, whereas IPv6 offers around 340 undecillion addresses.
  * Address allocation: IPv4 addresses are allocated manually using DHCP, while IPv6 addresses are primarily assigned using stateless autoconfiguration.

### **Routers**

* Router functionality:
  * A router is a networking device that directs data packets between different networks.
  * It determines the most efficient path for data transmission.
* Sending data to a specific destination on a network:
  * A router examines the destination IP address of incoming data packets.
  * It uses routing tables to determine the next hop or the next router on the path to the destination.
  * The router forwards the data packet to the appropriate next hop.
* Router's role in IP address assignment:
  * A router can act as a DHCP server (Dynamic Host Configuration Protocol) and assign IP addresses to devices on a local network.
  * It dynamically allocates IP addresses from a predefined range to connected devices.
  * DHCP allows for automatic IP address configuration and simplifies network management.
* Connecting a local network to the Internet:
  * A router serves as the gateway between a local network and the internet.
  * It connects the local network to an internet service provider (ISP) network.
  * The router receives data packets from devices on the local network and forwards them to the internet.
  * It also receives incoming data packets from the internet and routes them to the appropriate devices on the local network.