# Azure Virtual Machines

## Virtual Machine Planning

#### Virtual Network
“Virtual Networking,” before deploying a virtual machine, you should plan a virtual network from which the VM gets the private IP address.

You should be planning the virtual network and subnets based on the number of hosts required. Changing the virtual network configuration at a later point is a management overhead. Therefore, always plan your virtual networks and subnets before deploying the virtual machine.

#### Name
The VM name will be used as the computer name or host name for the VM you are creating. For a Windows VM, it can be up to 15 characters, and Linux VMs can support up to 64 characters.

- Environment: This is used to identify the environment the resource belongs to.
- Location: Including the location in the name helps you understand the VM location by looking at the name.
- Role: You can add the role of the VM.
- Application: If you have an application name, add the name of the application.
- Instance: If you have multiple instances created to improve the high availability, then start numbering them as 01, 02, etc.

#### Location and Pricing
When you create a VM in Azure, you can choose to which region you need to deploy this VM. This helps in keeping the VMs closer to your customer base.

While planning the location, you need to take into account the following considerations:
- **Availability of Services** Not all services are supported in all regions.
- **Pricing** The price of Azure services varies by region.
- **Compliance** Verify if your organization has any location restrictions or policies that limit the deployment to a certain region.

When it comes to pricing, the following are the costs associated with a VM:
- **Compute Costs** This is the cost for the compute resources (CPU and memory), and this is billed on an hourly basis.
- **License Cost** When you are choosing an operating system that requires a license (Windows Server, RHEL, SUSE), then you will see the license cost for your VM. You can use your existing licenses purchased from Software Assurance to cut down this cost.
  - This reduction method is called Azure Hybrid Benefit (AHUB). AHUB can be used for Windows, Linux (RHEL and SUSE), and SQL virtual machine licenses.
- **Storage Cost** This is the cost for the storage that your VM consumes.
- **Network Cost** This includes the cost for the public IP address if your VM is using a public IP address. In Azure Cost Management, you will see that the cost of the public IP address is mapped to the public IP resource.


Two payment methods are available when it comes to purchasing virtual machines:
- **Consumption-Based** In a consumption-based model, you pay for what you use; this is called the `pay-as-you-go` model. This is ideal for virtual machines that you deploy for a short term or for testing purposes.
- **Reserved Instances** This is ideal for production workloads meant to run for a longer period, at least for a year. Using reserved instances (RIs), you can pay the cost of the compute in an upfront or monthly manner. Since you are making this commitment, you will see up to a 72 percent discount in the cost compared to the consumption-based model.

#### Size
The OS disk capacity and the temp disk capacity will be decided by the size.

Azure also allows you to change the size of the virtual machines per your business requirements. This process is called VM resizing, and you can resize to any supported size.

#### Storage
Your Azure virtual machine requires storage to install the operating system files. We call this storage disks in Azure.

All virtual machines have at least two disks: `an OS disk` and a `temporary disk`.

You can have additional disks added to the virtual machines to store data; these additional disks are called `data disks`. All the disks use Azure Storage for storing the virtual hard disk (VHD) files.

**Type of Data**
- **Operating System Disks (OS Disks)**
  - Every virtual machine requires an operating system to run. Every virtual machine will have one disk that is labeled as an OS disk from which the VM boots.
- **Temporary Disks**
  - These disks are used to store pages or swap files and are not intended to be a persistent storage for your critical files.
- **Data Disks**
  - Data disks are used to store application data or any other data that you don’t want to keep in the OS disk.
  - The maximum supported size is 4 TB. The size of the virtual machine is what determines how many data disks can be attached to a VM.

**Performance**
- **Standard HDD**: Offers the lowest cost and is backed by the HDD drives. This is ideal for disks that require fewer I/O operations such as backup storage. The maximum IOPS is 2,000, and the maximum throughput is 500 MB per second.
- **Standard SSD**: Offers lower latency compared to Standard HDD as these drives are using SSDs under the hood. This is ideal for web servers and medium I/O-intensive workloads. The maximum IOPS is 6,000, and the maximum throughput is 750 MB per second.
- **Premium SSD**: Excellent choice for production and I/O-intensive workloads. As the name suggests, these disks are also using SSDs; however, they are faster than Standard SSD. The maximum IOPS is 20,000, and the maximum throughput is 900 MB per second.
- **Ultra disk**: Perfect for transaction-heavy workloads such as SAP HANA, SQL, Oracle, etc. This offers massive IOPS up to 160,000 and a maximum throughput of 2,000 MB per second.


**Management**
- Managed Disks
- Unmanaged Disks


## Connecting to Virtual Machines

#### Windows Connections
You can connect to Windows machines using two options, namely, Remote Desktop Protocol (RDP) and Windows Remote Management (WinRM).

**Windows Remote Management**
The communication is facilitated over TCP port 5986, so you need to ensure that this port is opened for communication in your NSG.

#### Linux Connections
In Linux, you use SSH to establish connectivity to your VMs. The classification here is based on whether you are using SSH key pair authentication or password-based authentication.

**Password-Based Authentication**

**SSH Key Pair**
The most preferred and secured method of connecting to a Linux VM is using an SSH key pair.

Azure uses a 2048-bit key length and SSH format for public and private keys.

#### Azure Bastion
With Azure Bastion, you can connect to Azure virtual machines without the need to have public IP addresses.

To work with Azure Bastion, you need to deploy the Bastion host to the virtual network where your VM is deployed. Azure Bastion requires a dedicated subnet of size (minimum /27) called AzureBastionSubnet.

Using Azure Bastion, without the need of any client or public IP address, you can seamlessly establish RDP/SSH connections directly from browser.

## Scaling Concepts
Scaling is one of the features of cloud. You can use the scalability of the cloud to control the infrastructure. When it comes scaling, you have two types of scaling: vertical scaling and horizontal scaling.

#### Vertical Scaling
In vertical scaling, you increase or decrease the size of the virtual machine. This process is also known as `scale up` and `scale down`. Using size, you are making the virtual machine more powerful (`scale up`) or less powerful (`scale down`).

The following are the use-case scenarios of vertical scaling:
- Changing the size of the virtual machine to a larger size to accommodate larger demand
- Reducing the size of underutilized virtual machines

#### Horizontal Scaling
Horizontal scaling is also known as `scale out` and `scale in`, where the number of instances is increased or decreased based on the demand. The increasing process is called `scale out`, and the decreasing process is called `scale in`.

Horizontal scaling is ideal in scenarios where you have unexpected load and the infrastructure needs to be scaled based on the load. In Azure, you can use virtual machine scale sets (VMSS) to increase or decrease the number of VM instances based on the load. Let’s understand more about VMSS.


## Virtual Machine Scale Sets
Virtual machine scale sets can be used to deploy and manage a group of identical VMs. Earlier, virtual machines supported identical instances only; this is called `uniform orchestration`.

For VMSS, no pre-provisioning of the VM is required. VMSS targets major workloads such as parallel processing, big data, and containerized workloads. VMSS is being used as nodes for the Azure Kubernetes Service because of the scalability. In short, as demand grows, more instances will be added based on the rules or a schedule. You can accomplish the scaling manually or using automation.

The following are the benefits offered by VMSS:
- Under uniform orchestration, all VMs that are part of the scale set are created using the VM configuration and OS image.
- All VMs in a scale set will have only private IP addresses, and the scale set can be placed as a backend pool for Azure Load Balancer or Azure Application Gateway.
- Based on the demand, the number of instances can be increased or decreased. VMSS is ideal for all kinds of unexpected demand.
- VMSS supports up to 1,000 VMs in a scale set. If you are using custom images, you can have up to 600 VMs.
