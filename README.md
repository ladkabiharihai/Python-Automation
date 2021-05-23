<img src="https://github.com/jokker99/Python-Automation/blob/master/index.jpg" width="70%">


# Python-Automation
I automated some commands and docker with help of python

## Running this script
  1 put Docker.py and linux_commands.py in cgi-bin folder <br>
  2 run command: 
  ```bash
    setenforce 0
    python iice-python.py
  ```
  
  The following Four Use Case are been sloved by our project :

 Hadoop is designed to handle the three V’s of Big Data: volume, variety, velocity. First lets look at volume, Hadoop is a distributed architecture that scales cost effectively. … Because of the flexibility of the system, you are able to avoid many network and processing bottlenecks associated with loading raw data.
    AWS CLI gives you the ability to automate the entire process of controlling and managing AWS services through scripts. These scripts make it easy for users to fully automate cloud infrastructure. Prior to AWS CLI, users needed a dedicated CLI tool for just the EC2 service.
    LVM is a tool for logical volume management which includes allocating disks, striping, mirroring and resizing logical volumes. With LVM, a hard drive or set of hard drives is allocated to one or more physical volumes. LVM physical volumes can be placed on other block devices which might span two or more disks.
    Docker allows you to run containers locally, eliminating disparity between your development and production environments, and everything in between. There is no need to install software packages locally. Everything you need for your development environment can simply run on the Docker engine as containers.

Our Automated “Python Menu” States as follow:
    AWS Python Menu integration is Done by Balwinder Pal Singh and Swetha
    Docker Python Menu Part is Done by Abhishek
    LVM Python Menu integration is Done by Anil Yadav
    Hadoop Python Menu integration is Done by Ashish

The whole Program integration comes up with TUI with Voice control based Mini-Project. Lets jump to the working of individual part of Project:-

# Python Menu interface:-

1 : To manage Hadoop

Hadoop works on a Distributed Storage Concept. In Distributed storage concept we make master-slave topology or we can also say it cluster as its a collection of nodes. In this master slave or name node splits the data and store in into slave nodes (i.e. data nodes) at a same time. Master nodes and slave nodes are connected with each other through networking and whenever users requests for a data that this master node directs to every slave node using the metadata table with Hadoop name node and helps in reading and writing data in fast I/O Speed.

To setup Hadoop cluster follow following step:

    MASTER NODE : Run program and said setup Hadoop | Enter user IP address | Enter your AWS security key (.pem file)| Enter no. to run name node.

    SALVE NODE : ENTER no. Salve required | Enter your AWS Security key (.pem file)| ENTER your Salve node IP Address | ENTER your LVM partition size, if you want to create with LVM.

2 : To manage AWS

AWS (Amazon Cloud Services) provides pubic cloud computing services in an automated way to their tenants, so that requirements of infrastructure, Software, Platform could be provided on the fly without paying for Upfront amount and just pay for the Services tenants use.

AWS services could be accessed easily by Web-UI / Web-App, CLI and Programable Files. Web-UI have pros and cons like a tenant to began on Cloud interacting with the service and go on choosing step by step requirement and activating those resources on cloud. Challenge using Web-UI is that user can’t be able to create resources with different configuration at the same time i.e. every time they have to follow the steps for individual creating resources with different environment. As companies use cloud to manage their backend services and they require a strategy so that a number of services could be managed at one go, for this they need to use tools for custom program Code or CLI based tool.

    The only prerequisite needed is that awscli should be downloaded as well as configuring aws using aws configure in the command prompt.

We have provided various services of AWS as follows:

1. Create a key pair

2. Delete a key pair

3. Create an EBS volume

4. Delete an EBS volume

5. Create a security group

6. Delete a security group

7. Launching your instance

8. Attaching EBS volume to you instance

9. Create S3 bucket

10. Delete bucket

11. Place object inside S3

12. Stop instance

13. Start instance

14. Terminate instance

Some of the outputs we get are listed below
Creating a key pair

A key pair, consisting of a private key and a public key, is a set of security credentials that you use to prove your identity when connecting to an instance. Amazon EC2 stores the public key, and you store the private key. You use the private key, instead of a password, to securely access your instances. Anyone who possesses your private keys can connect to your instances, so it’s important that you store your private keys in a secure place.

So just after pressing 1 a key pair with your desired name will be created.

Output
Creating a EBS volume

An Amazon EBS volume is a durable, block-level storage device that you can attach to your instances. After you attach a volume to an instance, you can use it as you would use a physical hard drive. EBS volumes are flexible. For current-generation volumes attached to current-generation instance types, you can dynamically increase size, modify the provisioned IOPS capacity, and change volume type on live production volumes.

So just after pressing 3 new EBS volume with the volume type you will give will be created.

Output
Creating security group

After said create security group a new security group will be created as shown
Launching instance

All the code associated with the above mentioned services are given in git hub — Github.com

Kindly go through this and give your valuable suggestions. Thank you for your patient reading.
3 : To manage Docker

In the world of automation to automate the installation and provisioning of our Operating System and Shipping it to our environment we are here with Docker Technology. To start the docker service in our OS we need to run a command that seems different in all the OS flavors to manage this in our Python Menu Program we are with a number that if pressed by user can easily start service for him. And Other choices to run a container, pull an image and stopping of container and all could be done by TUI.

The Docker demo of our Python Menu:-

    DOCKER : Said “Run docker” | Enter your IP address | Enter your “.ssh file name” | Provide “.ssh file name” | Enter password

4 : Logical Volume Management

The Elasticity and Flexibility of Data Storage can be achived by this concept of Logial Partitioning. The two things that contribute to help the user in doing the LV partitioning are as follows :-

1) Create “Volume Group” Class Which will Manage Volume Group

A volume group (VG) is the central unit of the Logical Volume Manager (LVM) architecture. It is what we create when we combine multiple physical volumes to create a single storage structure, equal to the storage capacity of the combined physical devices. Physical volumes are devices that are initialized using LVM, i.e., hard disk drives, solid-state drives, partitions, etc.

2) Create “Logical Volume” Class Which will Manage Logical Volume

Logical Volume Manager (LVM) is a device mapper framework that provides logical volume management for the Linux kernel. Most modern Linux distributions are LVM-aware to the point of being able to have their root file systems on a logical volume. LVM can also be understood as a thin software layer on top of the hard disks and partitions, which creates an abstraction of continuity and ease-of-use for managing hard drive replacement, repartitioning and backup.

The LVM demo of our Python Menu:-

    Resize to Attach space with LV : Run program again | Said “resize lvm” | ENTER your “Security key(.pem)” | ENTER your IP address | ENter extend size.



