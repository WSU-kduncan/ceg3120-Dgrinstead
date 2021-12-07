# Create a VPC

* ![image](https://user-images.githubusercontent.com/59849834/136311627-c74adb85-2ecc-4c85-8d10-4edd84d80ad2.png)

* A VPC is most commonly used in the context of cloud infrastructure as a service



# Create a subnet


* ![image](https://user-images.githubusercontent.com/59849834/136313222-bccda115-ab25-41f6-a1dc-19744fd1fe54.png)

* A subnet is basically a network inside a network. They make networking more efficient. When you create a subnet this allows network traffic to travel a shorter distance without passing through the unnecessary routers.


# Create an internet gateway

![image](https://user-images.githubusercontent.com/59849834/136315870-04b1f8e4-4c70-4178-9552-e95219842af1.png)

* A internet gateway is so that the traffic from a wokstation is routed to the outside network wihich is houw you get the webpages.

# Create a route table


![image](https://user-images.githubusercontent.com/59849834/136316291-8a5e58ae-0a72-4aca-9437-fe2bab040a9d.png)

* The routing table is going to contain information necessary to forward a packet along the nearest path towards its destination.

# Part 2 - EC2 instances

* Default username of the instance type selected

* Amazon Linux 2 AMI (HVM) - ami-02e136e904f3da870

* The way I added the inctance to my vpc was at the bottom it told me to hit next and 
"Configure Instance Details"

* The volume is already attached. I just used the General Purpose SSD (gp2) 

* My instance is GRINSTEAD-Instance. Just had to click add a tag

* What I had to do was click add a new security group. And then in the Source Box I had
to start typing in my GRINSTEAD-sg ID into the box so it could know to pull that group.

* When Reserving an ip address I had to go under the netowrk and security tab, and select
elastic IP's and then allocate an Elastic IP. Once i hit allocate you have to select Amazons pool of IPv4 addresses and then click allocate. After that you can assign the IP address to
The running instance.

* When I was doing the routing table i had to attach subnet mask to have it associated with the routing table. as well as adding the rule that sends traffic to all destinations which is 0.0.0.0/0.

![image](https://user-images.githubusercontent.com/59849834/136489554-9c1f627b-8d41-40a5-b338-0026e3600e3d.png)



## This is going to be when I am instanced into the instance actually using the name instead of the IP address 

![image](https://user-images.githubusercontent.com/59849834/137232131-98bc7d2a-2511-4f58-9cac-79b0d379441e.png)



