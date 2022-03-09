# CHAPTER 3 · Transport Layer

## 3.1 Introduction and Transport-Layer Services

A transport-layer protocol provides for **logical communication** between application processes running on different hosts. Processes can use it without considering the details of connection.

It will convert the messages into transport-layer packets by breaking them into several chunks and add headers.

### 3.1.1 Relationship Between Transport and Network Layers

Transport-layer protocol is analogy to Ann and Bill who collect and distribute the letter to each kid. The network-layer protocol is analogy to postal service.

### 3.1.2 Overview of the Transport Layer in the Internet

- **UDP** (User Datagram Protocol)

  connectionless, best-effort service

- **TCP** (Transmission Control Protocol)

  reliable, flow-and congestion-controlled connection-oriented transport 

IP is said to be an **unreliable service**, but TCP could convert it to a reliable data transport service. 

Extending host-to-host delivery to process-to-process is called **transport-layer multiplexing** and **demultiplexing**



## 3.2 Multiplexing and Demultiplexing

In sending end, the transport layer gathers data chunks from different sockets and adds header to create segments, then passes it to the network layer, and this action is called **Multiplexing**.

Similarly, in receiving end, the transport receives data from the network layers, and directs the segment to specific socket. This is called **Demultiplexing**.

---

**transport-layer multiplexing requires**

1. that sockets have unique identifiers
2. that each segment have special fields that indicate the socket to which the segment is to be delivered. Those are the **source port number field** and the **destination port number field** as shown below.

<img src="assets/image-20220309145801839.png" alt="image-20220309145801839" style="zoom:50%;" />

Each port number is a 16-bit number, ranging from 0 t0 65535.

**well-know port numbers**： 0 ~ 1023

#### Connectionless Multiplexing and Demultiplexing

When we use this command

```python
clientSocket = socket(AF_INET, SOCK_DGRAM)
```

The transport layer assign a port number in the range 1-24 to 65535 that is currently not used by any other UDP port in the host.

We can also to assign a specific port number using the command below.

```python
clientSocket.bind(('', 19157))
```

UDP socket is fully identified a two-tuple `(destination IP, destination port number)` 

**What is the purpose of the source port number ?**

The server will send a new segment to the client, with the extracted source port number serving as the destination port number in this new segment.

<img src="assets/image-20220309164808135.png" alt="image-20220309164808135" style="zoom:50%;" />

#### Connection-Oriented Multiplexing and Demultiplexing

TCP socket is identified by a four-tuple `(source IP address, source port number, destination P address, destionation port number)`

When server receives the incoming connection-request segment with specific port number, it will create a new socket:

```python
connectionSocket, addr = serverSocket.accept()
```

if the next request has a different 'four-tuple', a new connect will be created on this port.

<img src="assets/image-20220309170408511.png" alt="image-20220309170408511" style="zoom: 67%;" />

> **Security**
>
> Determining which applications are listening on which ports is a relatively easy task. Indeed there are a number of public domain programs, called port scanners, that do just that. Perhaps the most widely used of these is `nmap`, freely available at http://nmap.org and included in most Linux distributions. For TCP, `nmap` sequentially scans ports, looking for ports that are accepting TCP connections. For UDP, `nmap` again sequentially scans ports, looking for UDP ports that respond to transmitted UDP segments. 

#### Web Server and TCP

Figure 3.5 shows a Web server that spawns a new process for each connection. However, today's Web server often process each connection with different thread of the same process.



## 3.3 Connectionless Transport: UDP

**The reason to use UDP**

- *Finer application-level control over what data is sent, and when.* It could meet the real-time  applications' requirement.
- *No connection establishment* 
- *No connection state* 
- *Small packet header overhead.* The TCP segment has 20 bytes of header overhead in every segment, whereas UDP has only 8 bytes of overhead.

The most recent versions of HTTP run over UDP, providing their own error control and congestion control at the application layer.

### 3.3.1 UDP Segment Structure

![image-20220309230218067](assets/image-20220309230218067.png)

UDP header has only four fields,  each consisting of two bytes.

`Length` field specifies the number of bytes in the UDP segment(header plus data).

`Checksum` field is used by the receiving host to check whether errors have been introduced into the segment.

### 3.3.2 UDP Checksum

The checksum is used to determine whether bits within the UDP segment have been altered as it moved from source to destination.

- **sender side: **performing the 1 complement of the sum of all the 16-bit words in the segment.
- **receiver side: **all four 16-bit words are added, including the checksum. if overflow occurs, it will be wrapped around. If no errors are introduced into the packet, then the sum at the receiver will be 1111111111111111.

