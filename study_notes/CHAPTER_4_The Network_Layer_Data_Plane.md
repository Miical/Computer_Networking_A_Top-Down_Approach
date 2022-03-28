# CHAPTER 4 - The Network Layer: Data Plane

## 4.1 Overview of Network Layer 

### 4.1.1 Forwarding and Routing: The Data and Control Planes 

Two important network-layer functions:

- Forwarding 

- Routing 

A key element in every network router is its **forwarding table**.



**Control Plane: The Traditional Approach**

There is a algorithm to determine the forwarding table.



**Control Plane: The SDN Approach**

The routing device performs forwarding only, while the remote controller computes and distributes forwarding tables.

`software-defined networking(SDN)`, where the network is "software-defined" because the controller that computes forwarding tables and interacts with routers is implemented in software.



### 4.1.2 Network Service Model 

Consider some 0possible services that the network layer could provide. These services could include:

- Guaranteed delivery
- Guaranteed delivery with bounded delay.
- In-order packet delivery.
- Guaranteed minimal bandwidth. 
- Security

The Internet's network layer provides a single service, known as **best-effort service**.

