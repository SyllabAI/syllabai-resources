## Components in a Network

1. **Network Interface Cards (NIC)**

   * Connects a device to a wired transmission medium (copper or fibre).

   * Sends and receives electrical or light signals at the physical layer.

   * Contains a unique MAC address for identification at the Data Link layer.

   * Exchanges data between the CPU and the network via internal buses.

   * Converts parallel data → serial data for transmission, and serial → parallel for receiving.

   * Organises outgoing data into frames; checks incoming frames using checksums.

   * When sending, the OS places data in a buffer; the NIC uses DMA to read it, creates the frame, transmits it, and then notifies the OS.

   * When receiving, the NIC monitors the medium, accepts only frames matching its MAC address, writes them into a buffer via DMA, and interrupts the OS when data is ready.

2. **Wireless network interface cards (WNIC)**

   * Connect a device to a radio-based wireless medium (Wi-Fi, Bluetooth, mobile).

   * Sends and receives radio signals using modulation and demodulation at the physical layer.

   * Has a unique MAC address for addressing frames.

   * Like wired NICs, it converts between parallel and serial data and exchanges data with the CPU via internal buses.

   * Adds extra information to frames to handle sharing radio frequencies, interference, and retries.

   * Supports ad hoc mode (device-to-device) and infrastructure mode (via a WAP).

   * Uses SSIDs and authentication to connect to a WAP; frames may be encrypted.

   * When sending, the WNIC packages data into frames, modulates them onto radio carrier waves, and transmits across multiple frequencies in newer Wi-Fi versions.

   * When receiving, it demodulates radio waves, examines all frames, discards those not addressed to it, and interrupts the CPU when a valid frame arrives.

3. **Network repeaters**

   * Extends the range of a network by connecting multiple network sections. Needed because signals on copper, fibre-optic, or wireless mediums weaken over distance or are blocked by obstructions.

   * Works at the physical layer; does not process data packets.

   * Receives signals from one network section and retransmits them identically to the next section.

   * In wired networks, repeaters regenerate electrical signals or light signals (in fibre-optic networks) to correct signal loss and timing errors.

   * Fibre-optic repeaters may convert light → electrical → light signals, though newer optical repeaters amplify light directly.

   * Wireless repeaters (Wi-Fi extenders) receive and retransmit radio signals, bypassing obstructions and extending coverage.

   * Multi-port repeaters (network hubs) replicate frames to multiple sections simultaneously.

   * Wireless repeaters can reduce bandwidth (up to 50%), add interference, and reduce network security.

   * Wired network repeaters have largely been replaced by hubs and switches.

   * Fibre-optic repeaters are expensive and complex due to high data rates and multiple wavelengths.

4. **Hubs**

   * Connect multiple devices in a Local Area Network (LAN) and extend network coverage. Act as multi-port repeaters, regenerating incoming signals for all connected network sections.

   * Works at the physical layer of the OSI model.

   * Receives frames, regenerates them, and broadcasts to all ports except the one it came from.

   * Does not process frames or determine the intended recipient, leading to potential collisions and inefficient use of network bandwidth.

   * All connected sections act as a single network; collisions are detected by nodes, not the hub.

   * Can capture frames for network analysis, though this may present security risks.

   * **Advantages:**

     * A simple and inexpensive way to connect multiple devices.

     * Useful in star topologies for sharing a single connection into the main network.

     * Can bridge different types of wiring at each port.

     **Disadvantages:**

     * Inefficient traffic management; all frames are sent to all devices, reducing performance.

     * High chance of collisions and network congestion.

     * Largely obsolete; replaced by switches and routers in modern networks.

5. **Switches**

   * Connect network devices and segments while managing traffic efficiently. Reduce unnecessary network load by sending data only to the intended recipient.

   * Works primarily at Layer 2 (Data Link layer), sometimes at Layer 3 (Network layer) or higher.

   * Uses MAC addresses to determine the correct port for each frame.

   * Frames are regenerated and sent only to the destination port; if unknown, frames are broadcast.

   * Can segment a LAN, manage traffic between segments, and reduce collisions.

   * The store-and-forward method allows adjustment for different segment speeds.

   * Switches can learn frequently used paths to improve efficiency.

   * Advanced switches (managed/smart) allow traffic prioritisation, VLAN creation, port control, and monitoring (port mirroring, packet sniffing).

   * **Advantages:**

     * Efficient traffic management reduces collisions.

     * Can improve data transfer rates.

     * Supports VLANs and network traffic prioritisation.

     * Can monitor and analyse network traffic.

     **Disadvantages:**

     * More expensive and complex than hubs.

     * Requires configuration and management for advanced features.

6. **Wireless access points (WAPs)**

   * Serve as bridges between wireless devices and wired networks, enabling mobility, internet access, and network services.

   * They manage traffic, security, and connectivity but have limitations in range, bandwidth, client capacity, and susceptibility to interference and security risks.

   * WAPs connect wireless-capable devices (laptops, tablets, smartphones, smart home devices) to a wired network or the internet.

   * They provide Wi-Fi connectivity for multiple devices simultaneously and share the wired network’s connection, often via a router.

   * WAPs enable mobility within a building or public space, allowing devices to remain connected while moving.

   * They manage security by authenticating devices using passphrases and encryption protocols (WPA, WPA2, WPA3).

   * In public places, WAPs can create wireless hotspots, enabling internet access for guests or customers.

   * WAPs use radio waves (2.4 GHz or 5 GHz) to transmit data.

   * Data is sent in frames, modulated onto carrier waves, and transmitted using spread spectrum for efficiency.

   * Devices and WAPs must connect to the same SSID for data exchange.

   * Full- or half-duplex communication occurs across channels, and encryption ensures secure transmission.

   * WAPs send beacon frames containing the SSID, timestamps, and connection information to inform devices of network availability.

   * **Limitations and Drawbacks:**

     * Signal range is limited and affected by obstacles, antenna positioning, building materials, and interference from other devices.

     * Bandwidth is lower than wired connections (typically 25–350 Mbit/s vs 1000 Mbit/s wired).

     * Device capacity is restricted; most WAPs support 100–200 clients per radio.

     * Multiple WAPs on overlapping channels can interfere with each other.

     * Security management introduces overhead; unsecured WAPs are vulnerable to interception.

     * Environmental factors (weather, power output, neighbouring devices) can reduce signal quality.

     * For maximum performance and security, WAPs require proper placement, encryption, and potentially multiple access points in larger networks.

7. **Network Gateway**

   * Connects two separate networks and allows devices on one network to access services on another, even if the networks use different protocols. Can be hardware, software, or a combination; often integrated into a router.

   * Enables communication between networks with different protocols.

   * Works with switches and routers to exchange data between networks.

   * Can perform network address translation (NAT) to allow multiple devices on a LAN to share a single external IP address.

   * May carry out additional functions such as firewalls or proxy server services.

   * A default gateway handles data packets whose destination is outside the local network.

   * Examines incoming data frames for source and destination addresses.

   * Repackages frames into a format suitable for the target network.

   * Adds information such as the gateway’s external address to outgoing frames.

   * Transmits frames to the external network and reverses the process for incoming frames.

   * Ensures proper communication between LANs and WANs, including the internet, while handling protocol differences.

8. **Network Bridge**

   * A multi-port device that connects several network sections together, extending a LAN while keeping it as a single network.

   * Connects multiple network segments to form a larger network.

   * Regenerates and forwards complete data frames using the store-and-forward method.

   * Examines frames to determine their destination.

   * Maintains a table or database of MAC addresses learnt from frames passing through.

   * Forwards frames only to the appropriate ports based on the destination MAC address, reducing unnecessary network traffic.

   * If the destination MAC address is unknown, the frame is sent to all ports.

   * Receives and stores complete frames before processing.

   * Regenerates frames for onwards transmission.

   * Builds and updates an internal MAC address table from incoming frames.

   * Controls the flow of data between network segments, improving network efficiency compared to hubs.

9. **Routers**

   * Connect two or more networks, enabling data to travel between them, including LANs, WANs, and the internet.

   * They use network interfaces (NICs) to connect different transmission media while maintaining IP-based communication.

   * Routers receive entire data frames before processing them (store-and-forward method).

   * They examine the destination IP address in the packet header to determine the route.

   * Routing decisions are based on static or dynamic routing tables.

   * Static routing tables are manually configured and follow predetermined paths.

   * Dynamic routing tables adapt automatically by learning from data packets and other routers’ information, allowing alternative routes when network issues occur.

   * Routing tables can contain default routes for unknown destinations, directing packets to another router.

   * Incoming frames are buffered in queues for processing.

   * Long queues can reduce performance, so routers may drop excess packets.

   * Quality of Service (QoS) prioritises critical traffic (e.g., VoIP) to maintain uninterrupted flow.

   * Routers often work with gateways and can include NAT, firewalls, or proxy server functions.

   * They regenerate frames but do not examine the user data inside the packets.

   * Routers operate at Layer 3 (Network layer), using IP addresses to forward packets.

   * Unlike switches (Layer 2), routers work with packet switching and network addresses rather than MAC addresses.

### **Network Components Working Together**

* Devices (nodes/hosts) use the same protocols (usually Ethernet \+ IP) to communicate.

* Data is sent in frames containing MAC addresses, IP info, and payload.

* NICs package and transmit frames over wired or wireless media.

* Switches, WAPs, routers, and gateways examine, forward, and regenerate frames toward the destination.

* Frames with unknown destinations go to the default gateway, which forwards them to the next network.

* Communication with the internet involves frames passing through home LAN → gateway/router → ISP → internet routers → destination server → return path.

* Latency occurs due to processing and transmission delays; buffering and QoS help maintain smooth real-time services.