# CHAPTER 6: The Link Layer and LANs

## 6.1 Introduction to the Link Layer

Over a given link, a transmitting node encapsulates the datagram in a **link-layer frame** and transmits the frame into the link.

### 6.1.1 The Services Provided by the Link Layer

Possible service that can be offered by a link-layer protocol include:

- Framing. 
- Link access.
- Reliable delivery. Similar to a transport-layer reliable delivery service, a link-layer reliable delivery service can be achieved with acknowledgments and retransmission.
- Error detection and correction. 

### 6.1.2 Where Is the Link Layer Implemented?

![image-20220402191941956](assets/image-20220402191941956.png)

For the most part, the link layer is implemented on a chip called the **network adapter**, also sometimes known as a **network interface controller (NIC)**.