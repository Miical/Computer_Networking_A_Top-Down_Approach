# CHAPTER 5 - The Network Layer: Control Plane

## 5.1 Introduction 

There are two possible approaches for computing, maintaining and installing forwarding and flow tables.

- Per-router control. 	Both a forwarding and a routing function are contained within each router. 
- Logically centralized control.  The controller interacts with a control agent (CA) in each of the routers via a well-defined protocol to configure and manage that router's flow table.        

## 5.2 Routing Algorithms

Routing algorithms' goal is to determine good paths, from senders to receivers, through the network of routers.

Graph

An edge also has a value representing tis cost. Typically, an edge's cost may reflect the physical length of the corresponding link(for example, a transoceanic link might have a higher cost than a short-haul terrestrial link), the link speed, or the monetary cost associated with a link.

We denote c(x, y) as the cost of the edge between nodes x and y. If the pair (x, y) does not belong to E, we set $c(x, y) = \infin$ .

The shortest path.

Broadly, one way in which we can classify routing algorithms is according to whether they are centralized or decentralized. 

- **A centralized routing algorithm.**      Algorithms with global state information are often referred to as **link-state (LS) algorithms**.
- **decentralized routing algorithm**.



A second broad way to classify routing algorithm is according to whether they are static or dynamic. In **static routing algorithms**, routers change very slowly over time, often as a result of human intervention. **Dynamic routing algorithms** change the routing paths as the network traffic loads or topology change.

A third way to classify routing algorithms is according to whether they are load-sensitive or load-insensitive. In a **Load-sensitive algorithm**, link costs vary dynamically to reflect the current level of congestion in the underlying link. Today's Internet routing algorithm are **load-insensitive**，as a link's cost does not explicitly reflect it's current level of congestion. 

### 5.2.1 The Link-State (LS) Routing Algorithm

The link-state routing algorithm we present below is known as Dijkstra's algorithm.



What can be done to prevent such oscillations?  Another solution is to ensure that not all routers run the LS algorithm at the same time. ... One way to avoid such self-synchronization is for each router to randomize the time it sends out a link advertisement.

### 5.2.2 The Distance-Vector (DV) Routing Algorithm

Whereas the LS algorithm is an algorithm using global information the distance vector algorithm si iterative, asynchronous, and distributed. 

$d_x(y) = min_v\{c(x, v) + d_v(y)\}$

With the DV algorithm, each node x maintains the following routing information:

- For each neighbor v, the cost c(x, v) from x to directly attached neighbor, v
- Node x's distance vector, that is, $D_x = [D_x(y): y\ in\ N]$, containing x's estimate of its cost to all destinations, y in N .
- The distance vectors of each of its neighbors, that is, $D_v = [D_v(y): y\ in\ N]$  for each neighbor v of x.

In the distributed asynchronous algorithm, from time to time, each node sends a copy of its distance vector to its neighbors. When a node x receives a new distance vector form any of its neighbors. When a node x receives a new distance vector from any of  its neighbors w, it saves w's distance vector, and then uses the Bellman-Ford equation to update its own distance vector as follows:

$D_x(y) = min_v\{c(x, v) + D_v(y)\}\ for\ each\ node\ y\ in\ N$



**Distance-Vector Algorithm: Link-Cost Changes and Link Failure**

When some link cost changes, the noted that connected to it will update its distance table and send it to its neighbors. 

...

But there is a problem that it will fall into a loop.



**Distance-Vector Algorithm: Adding Poisoned Reverse**

The idea is simple -- if z routers through y to get to destination x, then z will advertise to y that its distance to x is infinity, that is z will advertise to y that $D_z(x) = \infin$ .

But if that loop involve three or more nodes, it will not be detected by the poisoned reverse technique.



**A Comparison of LS and DV Routing Algorithms**

- Message complexity. 
- Speed of convergence. 
- Robustness. 

