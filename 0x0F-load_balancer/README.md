**Load Balancer Algorithms:<br>**

1. Weighted Scheduling Algo<br>![weighted_scheduling_algo](https://i.imgur.com/LvjwmwI.png)
1. Round Robin Scheduling<br>![round_robin_algo](https://i.imgur.com/hGJdtsT.png)
1. Least Connection First Scheduling<br>

**Load Balancer Software:<br>**

1. **HAProxy**: TCP load balancer
2. **NGINX**: HTTP load balancer with SSL termination support
3. **mod_athena**: Apache based HTTP load balancer

**Load Balancers Implementation:<br>**
Hardware load balancers are implemented on EITHER Layer 4 (Transport Layer) OR Layer 7 (Application Layer) of OSI model (Open Systems Interconnection).<br>![layer4_layer7](https://i.imgur.com/9xoYhPB.png)

#### &emsp; A- Layer 4 Based Configurations:<br>

1. network address translators (NATs).
2. DNS load balancing.
3. Direct routing.
4. Tunnel or a IP tunneling.

- In this type it makes use of TCP, UDP or SCTP transport layer protocols (network-layer information), and distribute traffic based on IP addresses and port numbers.<br>

#### &emsp; B- Layer 7 Based Configurations:<br>

1. Application delivery network (ADN).

- In this type it makes use of HTTP exists on the layer7 and make the decision according to the actual content of the message (URLs, cookies, scripts).<br>
- For example, if the request coming is for image, it will got to the image server, and if the request is for PHP, it will go to the PHP server, and so on.
- And Layer 7 load balancers are using 3 techniques for that:
  1. URL parsing: To know different type of contents
  2. Cookie Sniffing: This helps for session aware routing
  3. HTTP reading: To look for HTTP header information.![layer7](https://i.imgur.com/7G5rxxd.png)

Sources:<br>
https://www.thegeekstuff.com/2016/01/load-balancer-intro/ <br>
