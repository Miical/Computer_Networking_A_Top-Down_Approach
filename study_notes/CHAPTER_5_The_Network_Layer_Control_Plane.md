# CHAPTER 5 - The Network Layer: Control Plane

## 5.1 Introduction 

There are two possible approaches for computing, maintaining and installing forwarding and flow tables.

- Per-router control. 	Both a forwarding and a routing function are contained within each router. 
- Logically centralized control.  The controller interacts with a control agent (CA) in each of the routers via a well-defined protocol to configure and manage that router's flow table.        

