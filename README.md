## Load Balancer

#### **Load Balancer Algorithms:<br>**

1. Weighted Scheduling Algo<br>![weighted_scheduling_algo](https://i.imgur.com/LvjwmwI.png)
2. Round Robin Scheduling<br>![round_robin_algo](https://i.imgur.com/hGJdtsT.png)
3. Least Connection First Scheduling:<br> It's like the round robin, but it forward the requests to the server with least requests not roundly.
   <br>&emsp;**There are other algos beside those!**<br>

**Load Balancer Software:<br>**

1. **HAProxy**: TCP or HTTP (Default is TCP).
2. **NGINX**: HTTP load balancer with SSL termination support and TCP, UDP too (Default is HTTP).
3. **mod_athena**: Apache based HTTP load balancer (Default is HTTP).

**Load Balancers Implementation:<br>**
Hardware load balancers are implemented on EITHER Layer 4 (Transport Layer) OR Layer 7 (Application Layer) of OSI model (Open Systems Interconnection).<br>![layer4_layer7](https://i.imgur.com/9xoYhPB.png)

**&emsp; A- Layer 4 Based Configurations:**<br>

1. network address translators (NATs).
2. DNS load balancing.
3. Direct routing.
4. Tunnel or a IP tunneling.

- In this type it makes use of TCP, UDP or SCTP transport layer protocols (network-layer information), and distribute traffic based on IP addresses and port numbers.<br>

**&emsp; B- Layer 7 Based Configurations:**<br>

1. Application delivery network (ADN).

- In this type it makes use of HTTP exists on the layer7 and make the decision according to the actual content of the message (URLs, cookies, scripts).<br>
- For example, if the request coming is for image, it will got to the image server, and if the request is for PHP, it will go to the PHP server, and so on.
- And Layer 7 load balancers are using 3 techniques for that:
  1. URL parsing: To know different type of contents
  2. Cookie Sniffing: This helps for session aware routing
  3. HTTP reading: To look for HTTP header information.![layer7](https://i.imgur.com/7G5rxxd.png)

**Sources:**
https://www.thegeekstuff.com/2016/01/load-balancer-intro/ <br>

<hr><hr>

## HAProxy

### Basic components that are used in load balancing:

**Access Control List (ACL):**<br>

- ACL is a rule or condition that's created to make decision about how to handle the incoming requests, like checking matching URL path, evaluating the HTTP headers, checking the IP address or a custom defined pattern.

```
acl url_blog path_beg /blog

  url_blog: The name of the ACL.
  path_blog: Is a keyword in HAProxy representing the path beginning.
  ** This acl rule is checking if the path_beg is /blog **
```

```
use_backend blog_backend if url_blog

  Usage of ACL: Here iam using the acl url_blog to rout the coming request to blog_servers
  if the acl condition is TRUE
```

<br>

**Backend:**<br>

- Is a set of servers that receives the requests and they are defined in the backend section in the HAProxy configuration.

```
backend web-backend
  balance roundrobin
  server web1 web01.your_domain.com:80 check
  server web2 web01.you_domain.com:80 check

backend blog-backend
  balance roundrobin
  mode http
  server blog1 blog1.your_domain.com:80 check
  server blog2 blog2.your_domain.com:80 check

    balance: Specifying the load balancing algo used
    mode: Specifying the mode used, wether HTTP (Layer 7) or TCP (Layer 4)
    check: Checking wether the servers are healthy or not, so if it's not healthy
            it will stop sending requests to it until it become healthy again.
```

<br>

**Frontend:**<br>

- Defines how requests should be forwarded to backends. and it's defined in the frontend section in the HAProxy Configurations.
- It consists of:
  - Set of IP addresses & a port
  - ACLs
  - _use_back_ rules, which defines which backend server to process the request, And/Or default_backend rule that handles the default route

### Basic types of load balancing:

**No Loading Balance:**<br>![no_load_balancing](https://i.imgur.com/wNWeqaB.png)

- In this case the user connects directly to the web server with no load balancing, which can cause many issues like the server will not be able to handle the load alone and can goes down, or the experience will be so slow.

**Layer 4 Loading Balance:**<br>![layer_4_load_balancing](https://i.imgur.com/c9GlvoX.png)

- In this case we will multiple the servers and use load balancer to balance the requests between them using Layer 4. and the backend section in HAProxy (for example) will handle this and send the request to the specified server.
- It will forward the requests based on the IP range and port (If request comes in for http://yourdomain.com/anything) then
  the traffic will forward to the backend that handles the yourdomain.com on port 80 and it's simpler than Layer 7.

**Layer 7 Loading Balance:**<br>![layer_7_load_balancing](https://i.imgur.com/cufyamd.png)

- In this case we will multiple the servers and use load balancer to balance the requests between them using Layer 4. and the backend section in HAProxy (for example) will handle this and send the request to the specified server.
- It forwards the coming requests bases on the content need of the request, and the mode here is HTTP

  ```
  frontend http
    bind *:80
    mode http

    acl url_blog path_beg /blog
    use_backend blog-backend if url_blog

    default_backend  web-backend
  ```

### Load balancing Algorithms:

**roundrobin Algorithm**
**leastconn Algorithm** (Lease Connection First Scheduling)
**Weighted Scheduling Algorithm**
**roundrobin Algorithm** (This will insure that the same user will connect to the same server, this is achieved through appsession)

### High Availability:

- In the previous designs the load balancer was a SOF (Single Point of Failure), so we have to redundant the load balancer like in the coming image to achieve the high availability.
- Here we are achieving the Active/Passive HA by using two load balancers, one is active and another is passive with a health detector in between and once the health detector detects that one load balancer is not working properly, it will forward the requests to the another one until the first back to work normally, then it will forward the requests to it again.
  ![ha-diagram-animated](https://i.imgur.com/Rr2Hk6t.gif)

<br>

**Source:**
https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts#high-availability
