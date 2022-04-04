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



## 6.2 Error-Detection and -Correction Techniques

![image-20220402192850431](assets/image-20220402192850431.png)

### 6.2.1 Parity Checks

In an even parity scheme, the sender simply includes one additional bit and chooses its value such that the total number of 1s in the d + 1 bits (the original information plus a parity bit) is even.

...

With this **two-dimensional parity** scheme, the parity of both the column and the row containing the flipped bit will be in error. The receiver can thus not only detect the fact that a single bit error has occurred, but can use the column and row indices of the column and row with parity errors to actually identify the bit that was corrupted and correct that error.

The ability of the receiver to both detect and correct errors is known as **forward error correction (FEC)**. 

### 6.2.2 Checksumming Methods

Why is checksumming used at the transport layer and cyclic redundancy check used at the link layer? Recall that the transport layer is typically implemented in software in a host as part of the host's  operating system. Because transport-layer error detection is implemented in software, it is important to have a simple and fast error-detection scheme such as checksumming. On the other hand, error detection at the link layer is implemented in dedicated hardware in adapters, which can rapidly perform the more complex CRC operations.  

###  6.2.3 Cyclic Redundancy Check (CRC)

CRC codes are also known as **polynomial codes**, since it is possible to view the bit string to be sent as a polynomial whose coefficients are the 0 and 1 values in the bit string, with operations on the bit string interpreted as polynomial arithmetic.

![image-20220402204414744](assets/image-20220402204414744.png)

Consider the d-bit piece of data, D, that the sending node wants to send to the receiving node. The sender and receiver must first agree on an r+1 bit pattern, known as a **generator**, which we will denote as G. We will require that the most significant (leftmost) bit of G be 1. The key idea behind CRC codes is shown in Figure 6.6. For a given piece of data, D, the sender will choose r additional bits, R, and append them to D such that the resulting d + r bit pattern is exactly divisible by G. using modulo-2 arithmetic. The process of error checking with CRCs is thus  simple:  The process of error checking with CRCs is thus simple: The receiver divides the d + r received bits by G. If the remainder is nonzero, the receiver knows that an error has occurred; otherwise the data is accepted as being correct.

All CRC calculations are done in modulo-2 arithmetic without carries in addition or borrows in subtraction. This means that addition and subtraction are identical, and both are equivalent to the bitwise exclusive-or of the operands. 



![image-20220402210317229](assets/image-20220402210317229.png)



## 6.3 Multiple Access Links and Protocols

There are two types of network links:

- **point-to-point link**. 
- **broadcast link**

How to coordinate the access of multiple sending and receiving nodes to a shared broadcast channel--the **multiple access problem **.

Computer networks similarly have protocols-so-called **multiple access protocols** -- by which nodes regulate their transmission into the shared broadcast channel. 

We can classify just about any multiple access protocol as belonging to one of three categories: **channel partitioning protocols, random access protocols, and  taking-turns protocols**.

### 6.3.1 Channel Partitioning Protocols

TDM has two major drawbacks. First, a node is limited to an average rate of R/N bps even when it is the only node with packets to send. A second drawback is that a node must always wait for its turn in the transmission sequence--again, even when it is the only node with a frame to send. 

FDM divides the R bps channel into different frequencies (each with a bandwidth of R/N) and assigns each frequency to one to the N nodes. It avoids collisions and divides the bandwidth fairly among the N nodes. However, FDM also shares a principal disadvantage with TDM--anode is limited to bandwidth of R/N, even when it is only node with packets to send.

 A third channel partitioning protocol is **code division multiple access (CDMA)**. CDMA assigns a different code to each node. Each node then uses its unique code to encode the data bits it sends. 



### 6.3.2 Random Access Protocols

**Slotted ALOHA**

The operation of slotted ALOHA in each node is imple:

- When the node has a fresh frame to send, it waits until the beginning of the next slot and transmits the entire frame in the slot.
- If there isn't a collision, the node has successfully transmitted its frame and thus need not consider retransmitting the frame. 
- If there is a collision, the node detects the collision before the end of the slot. The node retransmits its frame in each subsequent slot with probability p until the frame is transmitted without a collision.

When there are multiple active nodes, a certain fraction of the slots will have collisions and will therefore be "wasted." The second concern is that another fraction of the slots will be empty because all active nodes refrain from transmitting as a result of the probabilistic transmission policy. 

**ALOHA**

**Carrier Sense Multiple Access (CSMA)**

Specifically, there are two important rules for polite human conversation:

- Listen before speaking. If someone else is speaking, wait until they are finished. In the networking world, this is called **carrier sensing** -- a node listens to the channel before transmitting. 
- If some one else begins talking at the same time, stop talking. In the networking world, this is called **collision detection** -- a transmitting node listens to the channel while it is transmitting. 

These two rules are embodied in the family of **carrier sense multiple access** **(CSMA)** and **CSMA with collision detection (CSMA/CD)** 

### Carrier Sense Multiple Access with Collision Detection (CSMA/CD)

![image-20220403224844714](assets/image-20220403224844714.png)

It's operation from the perspective of an adapter attached to a broadcast channel:

- The adapter obtains a datagram from the network layer, prepares a link-layer frame, and puts the frame adapter buffer.
- If the adapter senses that the channel is idle, it starts to transmit the frame. 
- While transmitting, the adapter monitors for the presence of signal energy coming form other adapters using the broadcast channel.
- If the adapter transmits the entire frame without detecting signal energy from other adapters, the adapter is finished with the frame. If, on the other hand, the adapter detects signal energy from other adapters while transmitting, it aborts the transmission (that is, it stops transmitting its frame).
- After aborting, the adapter waits a random amount of time and then returns to step 2.

To determine interval

The **binary exponential backoff** algorithm, 

Specifically, when transmitting a frame that has already experienced n collisions, a node chooses the value of K at random from {0, 1, 2, ..., 2^n-1}

**CSMA/CD Efficiency**

### 6.3.3 Taking-Turns Protocols

Two important protocols

- **polling protocol**.

​		main node -> other nodes send data by turn. eg. Bluetooth

- **token-passing protocol**

​	When a token is passed to a node, the node begin to transmit. 

### 6.3.4 DOCSIS: The Link-Layer Protocol for Cable Internet Access

Data-Over Cable Service Interface Specifications

DOCSIS uses FDM to divide the downstream and upstream network segments into multiple frequecncy channels. 

Frames transmitted on downstream channel by the CMTS are received by all cable modems receiving that channel; however, multiple cable modems share the same upstream channel to the CMTS, and thus collisions can potentially occur.

A cable access network thus serves as a terrific example of multiple access protocols in action -- FDM, TDM, random access, and centrally allocated time slots all within one network!
