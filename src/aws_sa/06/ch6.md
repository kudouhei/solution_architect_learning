
#### The following presents a brief overview of some of those networking building blocks:

**Amazon Route 53**, an AWS DNS service, is both scalable and highly available out of the box. It provides domain name resolution, registration, and health checks. It is built as a globally distributed service that provides consistent and reliable DNS service, independently of local or regional network conditions. Route 53 uses Anycast routing technology to ensure requests are answered from the optimal location depending on network conditions. Route 53 will then provide the route to your AWS resources, such as EC2 instances, Elastic Load Balancing (ELB) load balancers, or Amazon S3 buckets. It can also be used to route requests to resources outside of AWS.

**Amazon CloudFront** is an AWS CDN service. It distributes your content across multiple edge locations across the AWS global network. It can significantly reduce the network latency by delivering content closer to the end users, improve the availability of your content thanks to the distributed nature of the service, and also limit access to your origin servers thanks to edge and regional caches. It is highly available due to its distributed nature.

The **ELB service** provides various types of load balancers: Classic Load Balancer (CLB), Application Load Balancer (ALB), Network Load Balancer (NLB), and Gateway Load Balancer (GWLB). The ELB service allows you to load balance IP-based traffic across multiple Availability Zones (AZs) within any given Region. The first three types (CLB, ALB, and NLB) offer an SLA of 99.99% availability. The availability of an SLA for the fourth type of load balancer (GWLB) actually depends on how you deploy the service since it relies on your implementation of third-party appliances.

**AWS Global Accelerator** is another service that builds on top of the Amazon global network. If you need to provide a service to end users globally, Global Accelerator offers a way to deliver that service through a set of static IP addresses and from the optimal endpoint based on your user’s location. Those IP addresses remain the same globally, but Global Accelerator will find out the optimal regional resource that can deliver the service. Those regional resources could be ALBs or NLBs, EC2 instances, or elastic IP addresses. It is also well suited for cross-region failover scenarios (single-region failover scenarios are usually better served by ELB load balancers). It is worth noting that, unlike CloudFront, Global Accelerator can also process non-HTTP requests.


#### Ensuring Business Continuity

- **Disaster recovery (DR)** is the process that tackles both the prevention of a disaster and the recovery from a disaster.
   - DR objectives are usually described with two specific KPIs: the recovery time objective (RTO) and the recovery point objective (RPO). 

- **High availability (HA)** addresses how a workload can keep functioning even though some of its components are impacted by a failure.