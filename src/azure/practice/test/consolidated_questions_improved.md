# Azure Practice Questions (Consolidated)
*Generated from multiple sources with duplicates removed*
---
## Question 1
**Type:** Multiple Choice
**Question:** You have a Microsoft Entra tenant named contoso.com. Microsoft Entra Connect is configured to sync users to the tenant from an on-premises Active Directory Domain Services (AD DS) domain. You need to assign licenses to the users based on Microsoft Entra ID attributes. The solution must minimize administrative effort. Which two actions should you perform? Each correct answer presents part of the solution.
**Choices:**
- **A. Assign the licenses to the dynamic security groups.** ✅
- B. B. Assign a license to each user.
- C. C. Create an automatic assignment policy.
- **D. Create dynamic security groups.** ✅
- E. E. Create Administrative units.
---
## Question 2
**Type:** Single Choice
**Question:** You have a Microsoft Entra tenant. You create a new user named User1. You need to assign a Microsoft 365 E5 license to User1. Which user attribute should be configured for User1 before you can assign the license?
**Choices:**
- A. A. First name
- B. B. Last name
- C. C. Other email address
- **D. Usage location** ✅
- E. E. User type
---
## Question 3
**Type:** Multiple Choice
**Question:** You have an Azure subscription that contains multiple users and administrators. You are creating a new custom role by using the following JSON. ``` { "Name": "Custom Role", "Id": null, "IsCustom": true, "Description": "Custom Role description", "Actions": [ "Microsoft.Compute/*/read", “Microsoft.Compute/snapshots/write”, “Microsoft.Compute/snapshots/read”, "Microsoft.Support/*" ], "NotActions": [ “Microsoft.Compute/snapshots/delete” ], "AssignableScopes": [ "/subscriptions/00000000-0000-0000-0000-000000000000", "/subscriptions/11111111-1111-1111-1111-111111111111" ] } ``` Which three actions can be performed by a user that is assigned the custom role? Each correct answer presents a complete solution.
**Choices:**
- **A. Call Microsoft Support.** ✅
- B. B. Create and delete a snapshot.
- **C. Create and read a snapshot.** ✅
- D. D. Create virtual machines.
- **E. Read all virtual machine settings.** ✅
---
## Question 4
**Type:** Single Choice
**Question:** You have the following resource groups, management groups, and Azure subscriptions: - Two resource groups named RG1 and RG2 in a subscription named 111-222-333 and a management group named MG1. - Two resource groups named RG3 and RG4 in a subscription named 777-888-999 and a management group named MG1. - Two resource groups named RG5 and RG6 in a subscription named 444-555-666 and a management group named MG1. - Two resource group named RG10 and RG11 in a subscription named 222-333-444 and a management group named MG2. - Two resource group named RG11 and RG12 in a subscription named 555-666-888 and a management group named MG2. You need to assign a role to a user to ensure the user can view all the resources in the subscriptions. The solution must use the principle of least privilege. Which role should you assign?
**Choices:**
- A. A. the Billing Reader role for all the subscriptions
- B. B. the Billing Reader role for MG1 and MG2
- C. C. the Contributor role for MG1 and MG2
- **D. the Reader role for MG1 and MG2** ✅
---
## Question 5
**Type:** Single Choice
**Question:** You have an Azure subscription. You run the following command: `Get-AzRoleDefinition | Format-Table -Property Name, Id` The command output contains data that includes the following: ``` CustomRole1 111-222-333-444-555 Owner 8e3af657-a8ff-443c-a75c-2fe8c4bcb635 Contributor b24988ac-6180-42a0-ab88-20f7382dd24c Reader acdd72a7-3385-48ef-bd42-f606fba81ae7 ``` You have a script that manages access to resources at the resource group level. The assignment process is automated by running the following PowerShell script nightly. ``` $rg = "RG1" $RoleName = "111-222-333-444-555" $Role = Get-AzRoleDefinition -Name $RoleName New-AzRoleAssignment -SignInName user1@contoso.com -RoleDefinitionName $Role.Name ` -ResourceGroupName $rg ``` User1 is unable to access the RG1 resource group. You discover that the script fails to complete for User1. You need to modify the script to ensure that it does not fail. What should you change in the script?
**Choices:**
- A. A. `$Role = Add-AzRoleDefinition -Name $RoleName`
- B. B. `$Role = Get-AzRoleAssignment -Name $RoleName`
- C. C. `$Role = Set-AzRoleAssignment -Name $RoleName`
- **D. `$RoleName = "CustomRole1" `** ✅
---
## Question 6
**Type:** Single Choice
**Question:** You have an Azure subscription that contains multiple virtual machines. You need to ensure that a user named User1 can view all the resources in a resource group named RG1. You must use the principle of least privilege. Which role should you assign to User1?
**Choices:**
- A. A. Billing Reader
- B. B. Contributor
- **C. Reader** ✅
- D. D. Tag Contributor
---
## Question 7
**Type:** Single Choice
**Question:** You have an Azure subscription that contains several storage accounts. You need to provide a user with the ability to perform the following tasks: - Manage containers within the storage accounts. - View storage account access keys. The solution must use the principle of least privilege. Which role should you assign to the user?
**Choices:**
- A. A. Owner
- B. B. Reader
- **C. Storage Account Contributor** ✅
- D. D. Storage Blob Data Contributor
---
## Question 8
**Type:** Single Choice
**Question:** You have an Azure subscription and a user named User1. You need to assign User1 a role that allows the user to create and manage all types of resources in the subscription. The solution must prevent User1 from assigning roles to other users. Which Azure role should you assign to User1?
**Choices:**
- A. A. API Management Service Contributor
- **B. Contributor** ✅
- C. C. Owner
- D. D. Reader
---
## Question 9
**Type:** Single Choice
**Question:** You have an Azure subscription that contains hundreds of virtual machines that were migrated from a local datacenter. You need to identify which virtual machines are underutilized. Which Azure Advisor settings should you use?
**Choices:**
- **A. Cost** ✅
- B. B. High Availability
- C. C. Operational Excellence
- D. D. Performance
---
## Question 10
**Type:** Multiple Choice
**Question:** You have several management groups and Azure subscriptions. You want to prevent the accidental deletion of resources. To which three resource types can you apply delete locks? Each correct answer presents a complete solution.
**Choices:**
- A. A. management groups
- **B. resource groups** ✅
- C. C. storage account data
- **D. subscriptions** ✅
- **E. virtual machines** ✅
---
## Question 11
**Type:** Single Choice
**Question:** A financial institution is implementing Azure to enhance their infrastructure. They need to maintain strict access controls due to regulatory requirements. You need to ensure that the finance team can view costs and manage budgets for Azure services without the ability to modify resources. Which role should you assign to the finance team at the subscription scope?
**Choices:**
- A. A. Reader
- B. B. Billing Reader
- C. C. Contributor
- **D. Cost Management Contributor** ✅
---
## Question 12
**Type:** Multiple Choice
**Question:** You need to generate the shared access signature (SAS) token for an Azure storage account. Which two parameters are required for the SAS token? Each correct answer presents part of the solution
**Choices:**
- A. A. `SignedIP (sip)`
- **B. `SignedResourceTypes (srt)`** ✅
- **C. `SignedServices (ss)`** ✅
- D. D. `SignedStart (st)`
---
## Question 13
**Type:** Single Choice
**Question:** You need to create an Azure Storage account that meets the following requirements: - Stores data in multiple Azure regions - Supports reading the data from primary and secondary regions Which type of storage redundancy should you use?
**Choices:**
- A. A. geo-redundant storage (GRS)
- B. B. locally-redundant storage (LRS)
- **C. read-access geo-redundant storage (RA-GRS)** ✅
- D. D. zone-redundant storage (ZRS)
---
## Question 14
**Type:** Multiple Choice
**Question:** You have an Azure Storage account named corpimages and an on-premises shared folder named \\\server1\images. You need to migrate all the contents from \\\server1\images to corpimages. Which two commands can you use? Each correct answer presents a complete solution.
**Choices:**
- **A. `Azcopy copy \\server1\images https://corpimages.blob.core.windows.net/public -recursive`** ✅
- B. B. `Azcopy sync \\server1\images https://corpimages.blob.core.windows.net/public -recursive`
- **C. `Get-ChildItem -Path \\server1\images -Recurse | Set-AzStorageBlobContent -Container "corpimages"`** ✅
- D. D. `Set-AzStorageBlobContent -Container "ContosoUpload" -File "\\server1\images" -Blob "corporateimages"`
---
## Question 15
**Type:** Multiple Choice
**Question:** You have an Azure Storage account. You need to copy data to the storage account by using the AzCopy tool. Which two types of data storage are supported by AzCopy? Each correct answer presents a complete solution.
**Choices:**
- **A. blob** ✅
- **B. file** ✅
- C. C. queue
- D. D. table
---
## Question 16
**Type:** Multiple Choice
**Question:** You have two premium block blob Azure Storage accounts named storage1 and storage2. You need to configure object replication from storage1 to storage2. Which three features should be enabled before configuring object replication? Each correct answer presents part of the solution.
**Choices:**
- **A. blob versioning for storage1** ✅
- **B. blob versioning for storage2** ✅
- **C. change feed for storage1** ✅
- D. D. change feed for storage2
- E. E. point-in-time restore for the containers on storage1
- F. F. point-in-time restore for the containers on storage2
---
## Question 17
**Type:** Multiple Choice
**Question:** You have an Azure subscription that contains multiple storage accounts. A storage account named storage1 has a file share that stores marketing videos. Users reported that 99 percent of the assigned storage is used. You need to ensure that the file share can support large files and store up to 100 TiB. Which two PowerShell commands should you run? Each correct answer presents part of the solution.
**Choices:**
- A. A. `New-AzRmStorageShare -ResourceGroupName RG1 -Name -StorageAccountName storage1 -Name share1 -QuotaGiB 100GB `
- **B. `Set-AzStorageAccount -ResourceGroupName RG1 -Name storage1 -EnableLargeFileShare  `** ✅
- C. C. `Set-AzStorageAccount -ResourceGroupName RG1 -Name storage1 -Type "Standard_RAGRS" `
- **D. ` Update-AzRmStorageShare -ResourceGroupName RG1 -Name -StorageAccountName storage1 -Name share1 -QuotaGiB 102400 `** ✅
---
## Question 18
**Type:** Single Choice
**Question:** You create an Azure Storage account. You need to create a lifecycle management rule to move blobs to Cool storage if the blobs have not been used for 30 days. What should you do first?
**Choices:**
- **A. Enable access tracking.** ✅
- B. B. Enable versioning for blobs.
- C. C. Refresh the blob inventory.
- D. D. Rotate the storage account keys.
---
## Question 19
**Type:** Single Choice
**Question:** You have an Azure subscription and an on-premises Hyper-V virtual machine named VM1. VM1 contains a single virtual disk. You plan to use VM1 as a template to deploy 25 new Azure virtual machines. You need to upload VM1 to Azure. Which cmdlet should you run?
**Choices:**
- **A. `Add-AzVhd`** ✅
- B. B. `New-AzDataShare`
- C. C. `New-AzDisk`
- D. D. `New-AzVM`
---
## Question 20
**Type:** Single Choice
**Question:** You have an Azure subscription. You plan to create a storage account named storage1. You need to ensure that storage1 provides POSIX-compliant access control lists (ACLs). Which option should you configure when creating storage1?
**Choices:**
- A. A. access tier
- **B. hierarchical namespace** ✅
- C. C. SFTP
- D. D. version-level immutable support
---
## Question 21
**Type:** Single Choice
**Question:** You have an Azure Storage account named storage1. You plan to store long-term backups in storage1. The solution must minimize costs. Which storage tier should you use for the backups?
**Choices:**
- **A. Archive** ✅
- B. B. Cold
- C. C. Cool
- D. D. Hot
---
## Question 22
**Type:** Single Choice
**Question:** You have an Azure Resource Manager (ARM) template named deploy.json that is stored in an Azure Blob storage container. You plan to deploy the template by running the `New-AzDeployment` cmdlet. Which parameter should you use to reference the template?
**Choices:**
- A. A. `-Tag`
- B. B. `-Templatefile`
- C. C. `-TemplateSpecId`
- **D. `-TemplateUri`** ✅
---
## Question 23
**Type:** Single Choice
**Question:** You plan to deploy an Azure virtual machine based on a basic template stored in the Azure Resource Manager (ARM) library. What can you configure during the deployment of the template?
**Choices:**
- A. A. the disk assigned to virtual machine
- B. B. the operating system
- **C. the resource group** ✅
- D. D. the size of virtual machine
---
## Question 24
**Type:** Single Choice
**Question:** Your company has a set of resources deployed to an Azure subscription. The resources are deployed to a resource group named app-grp1 by using Azure Resource Manager (ARM) templates. You need to verify the date and the time that the resources in app-grp1 were created. Which blade should you review for app-grp1 in the Azure portal?
**Choices:**
- **A. Deployments** ✅
- B. B. Diagnostics setting
- C. C. Deployment stacks
- D. D. Policy
---
## Question 25
**Type:** Single Choice
**Question:** You are creating an Azure virtual machine that will run Windows Server. You need to ensure that VM1 will be part of a virtual machine scale set. Which setting should you configure during the creation of the virtual machine?
**Choices:**
- **A. Availability options** ✅
- B. B. Azure Spot instance
- C. C. Management
- D. D. Region
---
## Question 26
**Type:** Single Choice
**Question:** Your company plans to host an application on four Azure virtual machines. You need to ensure that at least two virtual machines are available if a single Azure datacenter fails. Which availability option should you select for the virtual machine?
**Choices:**
- A. A. an availability set
- **B. an availability zone** ✅
- C. C. scale sets
---
## Question 27
**Type:** Single Choice
**Question:** You are deploying a virtual machine by using an availability set in the East US Azure region. You have deployed 18 virtual machines in two fault domains and 10 update domains. Microsoft performed planned physical hardware maintenance in the East US region. What is the maximum number of virtual machines that will be unavailable?
**Choices:**
- **A. 2** ✅
- B. B. 8
- C. C. 9
- D. D. 18
---
## Question 28
**Type:** Single Choice
**Question:** You have an Azure subscription that contains an Azure Storage account named vmstorageaccount1. You create an Azure container instance named container1. You need to configure persistent storage for container1. What should you create in vmstorageaccount1?
**Choices:**
- A. A. a blob container
- **B. a file share** ✅
- C. C. a queue
- D. D. a table
---
## Question 29
**Type:** Single Choice
**Question:** You have an Azure subscription that contains an Azure container app named cont1. You plan to add scaling rules to cont1. You need to ensure that cont1 replicas are created based on received messages in Azure Service Bus. Which scale trigger should you use?
**Choices:**
- A. A. CPU usage
- **B. event-driven** ✅
- C. C. HTTP traffic
- D. D. memory usage
---
## Question 30
**Type:** Multiple Choice
**Question:** You have an Azure subscription that contains multiple resource groups and Azure App Service web apps. A resource group named RG1 hosts a web app named appservice1. The App Service uses a free App Service Managed SSL certificate. You create a resource group named RG2. You plan to move all the resources in RG1 to RG2. Which two actions should you perform? Each correct answer presents part of the solution.
**Choices:**
- A. A. Create a new App Service plan in RG2.
- B. B. Create a new web app in RG2.
- **C. Delete the SSL Certificate from RG1 and upload it to RG2.** ✅
- **D. Move all the resources from RG1 to RG2.** ✅
---
## Question 31
**Type:** Single Choice
**Question:** You need to create an Azure App Service web app that runs on Windows. The web app requires scaling to five instances, 45 GB of storage, and a custom domain name. The solution must minimize costs. Which App Service plan should you use?
**Choices:**
- A. A. Basic
- B. B. Free
- C. C. Premium
- **D. Standard** ✅
---
## Question 32
**Type:** Single Choice
**Question:** You have an Azure subscription. You plan to deploy a web app in a Linux-based Docker container. You need to recommend a solution for the deployment of the web app that meets the following requirements: - Supports a custom domain name - Provides the ability to scale out automatically based on demand. - Minimizes administrative effort - Minimizes costs Which solution should you recommend?
**Choices:**
- **A. Azure App Service** ✅
- B. B. Azure Container Instances
- C. C. Azure Kubernetes Service (AKS)
- D. D. Azure Virtual Machine Scale Sets
---
## Question 33
**Type:** Multiple Choice
**Question:** Your company has an Azure subscription that is linked to a Microsoft Entra tenant. You have been asked to limit the access to the Kubernetes API server. Which two options should you choose? Each correct answer presents a complete solution.
**Choices:**
- **A. API server authorized IP ranges** ✅
- B. B. public cluster
- **C. private cluster** ✅
- D. D. Azure tags
---
## Question 34
**Type:** Single Choice
**Question:** You have two Azure subscriptions named Sub1 and Sub2. Sub1 contains a virtual network named VNet1 and a VPN gateway. Sub2 contains a virtual network named VNet2. You have an on-premises device named Device1 that runs Windows and has a Point-to-Site (P2S) VPN client installed. You configure network peering between VNet1 and VNet2. You need to ensure that Device1 can access VNet2 when a VPN connection is established. What should you do?
**Choices:**
- A. A. Create a private endpoint in Sub2.
- B. B. Deploy Azure Front Door to Sub2.
- **C. Download and reinstall the P2S VPN client on Device1.** ✅
- D. D. Run the New-SelfSignedCertificate cmdlet on Device1.
---
## Question 35
**Type:** Single Choice
**Question:** You have an Azure subscription that contains two resource groups named RG1 and RG2. RG1 contains the following resources: - A virtual network named VNet1 located in the East US Azure region - A network security group (NSG) named NSG1 located in the West US Azure region RG2 contains the following resources: - A virtual network named VNet2 located in the East US Azure region - A virtual network named VNet3 located in the West US Azure region You need to associate NSG1. To which subnets can you associate NSG1?
**Choices:**
- A. A. the subnets of all the virtual networks
- B. B. the subnets of VNet1 only
- C. C. the subnets of VNet1 and VNet2
- **D. the subnets of VNet3 only** ✅
---
## Question 36
**Type:** Single Choice
**Question:** You create several Azure virtual machines that run Windows Server. You need to connect to the virtual machines without exposing RDP ports over the internet. Which Azure service should you deploy?
**Choices:**
- **A. Azure Bastion** ✅
- B. B. Azure Front Door
- C. C. Azure Network Watcher
- D. D. Azure Virtual Desktop
---
## Question 37
**Type:** Single Choice
**Question:** Your company plans to migrate servers from on-premises to Azure. There will be dev, test, and production virtual machines on a single virtual network. You need to restrict traffic between the dev, test, and production virtual machines to specific ports. What should you use?
**Choices:**
- **A. a network security group (NSG)** ✅
- B. B. an Azure firewall
- C. C. an Azure load balancer
- D. D. an Azure VPN gateway
---
## Question 38
**Type:** Multiple Choice
**Question:** You have an Azure subscription that contains an ASP.NET application. The application is hosted on four Azure virtual machines that run Windows Server. You have a load balancer named LB1 to load balances requests to the virtual machines. You need to ensure that site users connect to the same web server for all requests made to the application. Which two actions should you perform? Each correct answer presents part of the solution.
**Choices:**
- A. A. Configure an inbound NAT rule.
- **B. Set Session persistence to Client IP.** ✅
- C. C. Set Session persistence to __None__.
- **D. Set Session persistence to Protocol.** ✅
---
## Question 39
**Type:** Single Choice
**Question:** You have web app that is running in four Windows Server Azure virtual machines behind a load balancer. Users experience issues when accessing the web app. You suspect an issue with the web server and must check whether the server is listening on port 80. Which command should you run?
**Choices:**
- A. A. `Get-AzVirtualNetworkUsageList`
- B. B. `nbtstat -c`
- **C. `netstat -an`** ✅
- D. D. `Test-NetConnection localhost`
---
## Question 40
**Type:** Single Choice
**Question:** You have an Azure subscription that contains two virtual networks named VNet1 and VNet2. You need to ensure that the resources on both VNet1 and VNet2 can communicate seamlessly between both networks. What should you configure from the Azure portal?
**Choices:**
- A. A. connected devices
- B. B. firewall
- **C. peerings** ✅
- D. D. service endpoints
---
## Question 41
**Type:** Single Choice
**Question:** You have an Azure subscription that contains a virtual network named VNet1. You plan to deploy a virtual machine named VM1 to be used as a network inspection appliance. You need to ensure that all network traffic passes through VM1. What should you do?
**Choices:**
- **A. Configure a user-defined route.** ✅
- B. B. Create a virtual network gateway.
- C. C. Modify the default route.
- D. D. Modify the system route.
---
## Question 42
**Type:** Single Choice
**Question:** You have an Azure virtual network named VNet1. You create an Azure Private DNS zone named contoso.com. You need to ensure that the virtual machines on VNet1 register in the contoso.com private DNS zone. What should you do?
**Choices:**
- **A. Add a virtual network link to contoso.com.** ✅
- B. B. Add Azure DNS Private Resolver to VNet1.
- C. C. Configure each virtual machine to use a custom DNS server.
- D. D. Configure VNet1 to use a custom DNS server.
---
## Question 43
**Type:** Single Choice
**Question:** Your organization uses an Azure Load Balancer to manage traffic for VMs hosting a web application. Users experience uneven traffic distribution, with some VMs receiving more traffic than others. You need to configure the load balancer to ensure even traffic distribution across all VMs in the backend pool. What should you do?
**Choices:**
- A. A. Add more VMs to the pool.
- B. B. Adjust the load balancing rule settings.
- **C. Disable session persistence.** ✅
- D. D. Enable session persistence (source IP affinity).
---
## Question 44
**Type:** Single Choice
**Question:** You have a Kusto query that returns 1,000 events from the SecurityEvent table in Azure Monitor. You need to configure the query to aggregate the results by the Account column. Which operator should you use?
**Choices:**
- A. A. extend
- B. B. project
- **C. summarize** ✅
- D. D. where
---
## Question 45
**Type:** Single Choice
**Question:** You have an Azure virtual machine that runs Linux. The virtual machine hosts a custom application that outputs log data in the JSON format. You need to recommend a solution to collect the logs in Log Analytics workspace. What should you include in the recommendation?
**Choices:**
- A. A. the Azure VMAccess extension
- B. B. the Custom Script Extension Version 2 extension
- C. C. the DSC extension for Linux
- **D. the Azure Monitor agent for Linux** ✅
---
## Question 46
**Type:** Single Choice
**Question:** You have an Azure virtual machine named Server1 that runs Windows Server. You need to configure Azure Backup to back up files and folders. What should you install on Server1?
**Choices:**
- A. A. Microsoft Azure Backup Server (MABS)
- B. B. Microsoft Azure Site Recovery Provider
- C. C. the Azure Connected Machine agent
- **D. the Microsoft Azure Recovery Services (MARS) agent** ✅
---
## Question 47
**Type:** Single Choice
**Question:** You have an Azure virtual machine that you back up by using Azure Backup. The backup policy sub type is Standard, and the backup policy has the following configurations: - Backup schedule frequency: Weekly - Retain instant recovery snapshot(s) for: 5 days - Retention of weekly backup point: On Sunday at 8:00 AM for 12 weeks You plan to reduce the amount of storage used by Instant Restore. You need to instance recovery snapshots to be retained for only two days. What should you do first?
**Choices:**
- A. A. Change Policy sub type to Enhanced.
- B. B. Change Retention of weekly backup point to 1 week.
- **C. Change the backup schedule frequency to __Daily__.** ✅
- D. D. Provision an additional blob storage container.
---
## Question 48
**Type:** Multiple Choice
**Question:** You have an Azure virtual network named VNet1 that is deployed to the Azure East US region. You need to ensure that email is sent to an administrator when a virtual machine is connected to VNet1. What should you create?
**Choices:**
- **A. an action group** ✅
- B. B. an alert processing rule
- **C. an alert rule** ✅
- D. D. a mail-enabled security group
---
## Question 49
**Type:** Single Choice
**Question:** You have an Azure subscription that contains the following resources: - Eight virtual networks - 24 virtual machines - 16 storage accounts You need to implement a monitoring solution that provides the ability to view diagnostics and telemetry data generated by Azure resources. What should you include in the solution?
**Choices:**
- **A. a Log Analytics workspace** ✅
- B. B. an Azure Machine Learning workspace
- C. C. metrics logs
- D. D. resource logs
---
## Question 50
**Type:** Single Choice
**Question:** You plan to create an alert in Azure Monitor that will have an action group to send SMS messages. What is the maximum number of SMS messages that will be sent every hour if the alert gets triggered every minute?
**Choices:**
- A. A. 4
- B. B. 6
- **C. 12** ✅
- D. D. 60
---
## Question 51
**Type:** Single Choice
**Question:** You plan to configure object replication between two Azure Storage accounts. The Blob service of the source storage account has the following settings: - Hierarchical namespace: Disabled - Default access tier: Hot - Blob public access: Enabled - Blob soft delete: Enabled (7 days) - Container soft delete: Enabled (7 days) - Versioning: Disabled - Change feed: Enabled - NFS v3: Disabled - Allow cross-tenant replication: Enabled Which setting should be modified on the source storage account to support object replication?
**Choices:**
- A. A. Blob soft delete
- B. B. Change feed
- C. C. Hierarchical namespace
- **D. Versioning** ✅
---
## Question 52
**Type:** Single Choice
**Question:** You have an Azure Storage account named storageaccount1 with a blob container named container1 that stores confidential information. You need to ensure that content in container1 is not modified or deleted for six months after the last modification date. What should you configure?
**Choices:**
- A. A. a custom Azure role
- B. B. lifecycle management
- C. C. the change feed
- **D. the immutability policy** ✅
---
## Question 53
**Type:** Single Choice
**Question:** You have an Azure Storage account that contains a file share. Several users work from a secure location that limits outbound traffic to the internet. You need to ensure that the users at the secure location can access the file share in Azure by using SMB protocol. Which outbound port should you allow from the secure location?
**Choices:**
- A. A. 80
- B. B. 443
- **C. 445** ✅
- D. D. 5671
---
## Question 54
**Type:** Single Choice
**Question:** You have an Azure subscription that contains a storage account named storage1. You need to ensure that access to storage1 is disabled from the internet. What should you configure on storage1?
**Choices:**
- A. A. Access keys
- B. B. Data protection
- C. C. Encryption
- **D. Networking** ✅
---
## Question 55
**Type:** Multiple Choice
**Question:** You have an Azure subscription. You plan to create a storage account named storage1 to store images. You need to replicate the images to a new storage account. What are three requirements of storage1? Each correct answer presents part of a complete solution.
**Choices:**
- **A. a container** ✅
- B. B. a file share
- **C. blob versioning** ✅
- D. D. queues
- **E. standard general-purpose v2** ✅
---
## Question 56
**Type:** Multiple Choice
**Question:** You have an Azure subscription that contains a network security group (NSG) named NSG1. You plan to configure NSG1 to allow the following types of traffic: - Remote Desktop Management - Secured HTTPS Which two ports should you allow in NSG1? Each correct answer presents part of the solution.
**Choices:**
- A. A. 80
- B. B. 25
- **C. 443** ✅
- D. D. 587
- **E. 3389** ✅
---
## Question 57
**Type:** Single Choice
**Question:** You have an Azure virtual network that contains four subnets. Each subnet contains 10 virtual machines. You plan to configure a network security group (NSG) that will allow inbound traffic over TCP port 8080 to two virtual machines on each subnet. The NSG will be associated to each subnet. You need to recommend a solution to configure the inbound access by using the fewest number of NSG rules possible. What should you use as the destination in the NSG?
**Choices:**
- **A. an application security group** ✅
- B. B. a service tag
- C. C. the subnets of the virtual machines
---
## Question 58
**Type:** Multiple Choice
**Question:** You have an Azure subscription that contains a resource group named RG1. RG1 contains a virtual network named VNet3, a virtual machine named VM1, and a public IP address named PubIP1. All the resources are in the West US Azure region. You plan to create and configure a network security group (NSG) named NSG1 for the following types of traffic: - Remote Desktop Management - HTTP NSG1 will be used on the subnets of multiple virtual networks. Which two cmdlets should you run? Each correct answer presents part of the solution.
**Choices:**
- A. A. `Add-AzLoadBalancerFrontendIpConfig`
- B. B. `Add-AzNetworkInterfaceTapConfig`
- **C. `New-AzNetworkSecurityGroup`** ✅
- **D. `New-AzNetworkSecurityRuleConfig`** ✅
---
## Question 59
**Type:** Single Choice
**Question:** You have an Azure subscription that contains a virtual network named VNet1 and a virtual machine named VM1. VM1 can only be accessed from the internal network. An external contractor needs access to VM1. The solution must minimize administrative effort. What should you configure?
**Choices:**
- **A. a public IP address** ✅
- B. B. a second private IP address
- C. C. a Site-to-Site (S2S) VPN
- D. D. Azure Firewall
---
## Question 60
**Type:** Single Choice
**Question:** You have an Azure subscription that contains a virtual network named VNet1. You plan to enable VNet1 connectivity to on-premises resources by using an encrypted connection. What should you configure for VNet1?
**Choices:**
- A. A. a private endpoint connection
- B. B. a public IP address
- **C. a virtual network gateway** ✅
- D. D. internet routing
---
## Question 61
**Type:** Single Choice
**Question:** You have multiple Azure virtual machines and an Azure recovery services vault. Virtual machines are configured with the default backup policy. What is the retention period of virtual machine backups in the default backup policy?
**Choices:**
- A. A. 7 days
- B. B. 14 days
- **C. 30 days** ✅
- D. D. 90 days
---
## Question 62
**Type:** Multiple Choice
**Question:** You have an Azure subscription that contains two virtual machines named VM1 and VM2. VM1 and VM2 are backed up to a Recovery Service vault named Vault1 by using the same backup policy. Your company plans to create additional virtual machines and Recovery Services vaults. During this process, Vault1 will be decommissioned. You need to delete Vault1. Which three actions should you perform before you can delete Vault1? Each correct answer presents part of the solution.
**Choices:**
- A. A. Delete VM1 and VM2.
- **B. Disable the soft delete feature and delete all data.** ✅
- C. C. Enable a Read lock on Vault1.
- **D. Permanently remove any items in the soft delete state.** ✅
- **E. Stop the backup of VM1 and VM2.** ✅
---
## Question 63
**Type:** Single Choice
**Question:** You have an Azure virtual machine named VM1 that is protected by using Azure site recovery. You fail over VM1 from the primary region to the secondary region. You need to reprotect VM1 after the failover so that VM1 will replicate back to the primary region. What is the VM1 status before the reprotection?
**Choices:**
- A. A. Committing failover
- **B. Failover committed** ✅
- C. C. Failover confirmed
- D. D. Starting failover
---
## Question 64
**Type:** Multiple Choice
**Question:** You have an Azure subscription that contains a resource group named RG1. RG1 contains two virtual machines named VM1 and VM2. You need to inspect all the network traffic from VM1 to VM2.The solution must use Azure Monitor metrics. Which two actions should you perform? Each correct answer presents part of the solution.
**Choices:**
- A. A. Configure a log alert.
- B. B. Configure Network In and Network Out.
- **C. Install AzureNetworkWatcherExtension.** ✅
- **D. Use packet capture.** ✅
---
## Question 65
**Type:** Single Choice
**Question:** You plan to provision an Azure subscription that will contain the following virtual networks: - VNet1 in the East US Azure region with two subnets - VNet2 in the East US region with four subnets - VNet3 in the West Europe Azure region with four subnets - VNet4 in the West Europe region with two subnets How many Azure Network Watcher instances will be provisioned as part of the deployment?
**Choices:**
- A. A. 1
- **B. 2** ✅
- C. C. 4
- D. D. 12
---
## Question 66
**Type:** Multiple Choice
**Question:** You have a Microsoft Entra tenant that uses Microsoft Entra Connect to sync with an Active Directory Domain Services (AD DS) domain. You need to ensure that users can reset their AD DS password from the Azure portal. The users must be able to use two methods to reset their password. Which two actions should you perform? Each correct answer presents part of the solution.
**Choices:**
- **A. From Password reset in the Azure portal, configure the Authentication methods settings.** ✅
- B. B. From Password reset in the Azure portal, configure the Notifications settings.
- C. C. From Password reset in the Azure portal, configure the Registration settings.
- D. D. Run Microsoft Entra Connect and select Device writeback.
- **E. Run Microsoft Entra Connect and select Password writeback.** ✅
---
## Question 67
**Type:** Single Choice
**Question:** Your Microsoft Entra tenant and on-premises Active Directory domain contain multiple users. You need to configure self-service password reset (SSPR) password writeback functionality. The solution must minimize costs. Which Microsoft Entra ID edition should you use?
**Choices:**
- A. A. Microsoft Entra ID Free
- **B. Microsoft Entra ID P1** ✅
- C. C. Microsoft Entra ID P2
---
## Question 68
**Type:** Single Choice
**Question:** You have an Azure subscription that contains 25 virtual machines. You need to ensure that each virtual machine is associated to a specific department for reporting purposes. What should you use?
**Choices:**
- A. A. administrative units
- B. B. management groups
- C. C. storage accounts
- **D. tags** ✅
---
## Question 69
**Type:** Single Choice
**Question:** You have an Azure subscription that contains 200 virtual machines. You plan to use Azure Advisor to provide cost recommendations when underutilized virtual machines are detected. You need to ensure that all Azure admins are notified whenever an Advisor alert is generated. The solution must minimize administrative effort. What should you include in the solution?
**Choices:**
- **A. an action group** ✅
- B. B. an application security group
- C. C. an Azure Automation account
- D. D. a capacity reservation group
---
## Question 70
**Type:** Single Choice
**Question:** You have an Azure subscription. You plan to create an Azure Policy definition named Policy1. You need to include remediation information in Policy. To which definition section should you add remediation information for Policy1?
**Choices:**
- **A. metadata** ✅
- B. B. mode
- C. C. parameters
- D. D. policyRule
---
## Question 71
**Type:** Single Choice
**Question:** You have an Azure virtual network that contains two subnets named Subnet1 and Subnet2. You have a virtual machine named VM1 that is connected to Subnet1. VM1 runs Windows Server. You need to ensure that VM1 is connected directly to both subnets. What should you do first?
**Choices:**
- **A. From the Azure portal, add a network interface.** ✅
- B. B. From the Azure portal, create an IP group.
- C. C. From the Azure portal, modify the IP configurations of an existing network interface.
- D. D. Sign in to Windows Server and create a network bridge.
---
## Question 72
**Type:** Single Choice
**Question:** Your development team plans to deploy an Azure container instance. The container needs a persistent storage layer. Which service should you use?
**Choices:**
- A. A. Azure Blob storage
- **B. Azure Files** ✅
- C. C. Azure Queue Storage
- D. D. Azure SQL Database
---
## Question 73
**Type:** Multiple Choice
**Question:** You have a Basic Azure App Service plan that contains a web app. You need to ensure that the web app can scale automatically when the CPU percentage goes beyond 80 percent for a duration of 15 minutes. Which two actions should you perform? Each correct answer presents part of the solution.
**Choices:**
- A. A. Configure a deployment slot.
- **B. Configure a scaling condition to scale based on a metric, and then add the rules.** ✅
- C. C. Configure a scaling condition to scale based on an instance count, and then set the instance count.
- D. D. Scale out the App Service plan.
- **E. Scale up the App Service plan.** ✅
---
## Question 74
**Type:** Single Choice
**Question:** You have an Azure subscription that contains a container app named App1. App1 is configured to use cached data. You plan to create a new container. You need to ensure that the new container automatically refreshes the cache used by App1. Which type of container should you configure?
**Choices:**
- A. A. blob
- B. B. init
- C. C. privileged
- **D. sidecar** ✅
---
## Question 75
**Type:** Single Choice
**Question:** You have an Azure subscription that contains a resource group named RG1. RG1 contains an application named App1 and a container app named containerapp1. App1 is experiencing performance issues when attempting to add messages to the containerapp1 queue. You need to create a job to perform an application resource cleanup when a new message is added to a queue. Which command should you run?
**Choices:**
- **A. ```az containerapp job create \       --name "my-job" --resource-group "RG1" -trigger-type "Event" -replica-timeout 60 --replica-retry-limit 1 ...```** ✅
- B. B. ```az containerapp job create \       --name "my-job" --resource-group " RG1" -trigger-type "Manual" -replica-timeout 60 --replica-retry-limit 1 ...```
- C. C. ```az containerapp job start \       --name "my-job" --resource-group " RG1" -trigger-type "Schedule" -replica-timeout 60 --replica-retry-limit 1 ...```
- D. D. ```az containerapp job start \       --name "my-job" --resource-group " RG1" -trigger-type "Event" -replica-timeout 60 --replica-retry-limit 1 ...```
---
## Question 76
**Type:** Single Choice
**Question:** You have an Azure subscription that contains a web app named App1. You configure App1 with a custom domain name of webapp1.contoso.com. You need to create a DNS record for App1. The solution must ensure that App1 remains accessible if the IP address changes. Which type of DNS record should you create?
**Choices:**
- A. A. A
- **B. CNAME** ✅
- C. C. SOA
- D. D. SRV
- E. E. TXT
---
## Question 77
**Type:** Single Choice
**Question:** You are an Azure Administrator for Best For You Organics Company. The company uses ARM templates for deploying resources. You need to pass an array as an inline parameter during the deployment of a local template. What should you do?
**Choices:**
- A. A. Modify the template to include the array values.
- B. B. Use the --template-file switch to pass the array values.
- **C. Provide the array values in the --parameters switch in the deployment command.** ✅
- D. D. Create a separate parameters file that includes the array values.
---
