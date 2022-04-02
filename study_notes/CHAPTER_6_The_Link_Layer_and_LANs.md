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