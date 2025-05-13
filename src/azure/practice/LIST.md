# List 

- **IP flow verify**
   - A Network Watcher feature that checks if traffic is allowed or denied to/from a virtual machine based on current network security group rules. 
   - https://learn.microsoft.com/en-us/azure/network-watcher/ip-flow-verify-overview
- **Azure Event Grid**
   - You can monitor and respond to specific events that happen in Azure resources or external resources by using Azure Event Grid and Azure Logic Apps. 
   - https://learn.microsoft.com/en-us/azure/event-grid/monitor-virtual-machine-changes-logic-app
- **Azure Multi-Factor Authentication**
   - To secure user sign-in events in Microsoft Entra ID, you can require Microsoft Entra multifactor authentication (MFA). The recommendation is to use conditional access policies that can then be targeted to groups of users, specific applications, or other conditions. 
   - https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-userstates
- **Migrate on-premises machines to Azure**
   - We recommend that you migrate machines to Azure using the Azure Migrate service. Azure Migrate is purpose-built for server migration. Azure Migrate provides a centralized hub for discovery, assessment, and migration of on-premises machines to Azure. 
   - https://learn.microsoft.com/en-us/azure/site-recovery/migrate-tutorial-on-premises-azure
- **Create and configure a Recovery Services vault**
   - A Recovery Services vault is a management entity that stores recovery points that are created over time, and it provides an interface to perform backup-related operations. 
   - https://learn.microsoft.com/en-us/azure/backup/backup-create-recovery-services-vault
- **Microsoft Entra  Fundamentals**
   - Microsoft Entra tenants come with an initial domain name like `domainname.onmicrosoft.com`. You can't change or delete the initial domain name, but you can add your organization's DNS name as a custom domain name and set it as primary. By adding your domain name, you can add user names that are familiar to your users, such as `alain@contoso.com`. 
   - https://learn.microsoft.com/en-us/entra/fundamentals/add-custom-domain
- **Microsoft Entra pass-through authentication**
   - Microsoft Entra pass-through authentication allows your users to sign in to both on-premises and cloud-based applications by using the same passwords. Pass-through Authentication signs users in by validating their passwords directly against on-premises Active Directory.
   - https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-pta-quick-start

- **IdFix tool**
  - IdFix is used to perform discovery and remediation of identity objects and their attributes in an on-premises Active Directory environment in preparation for migration to Azure Active Directory. IdFix is intended for the Active Directory administrators responsible for directory synchronization with Azure Active Directory.
  - https://learn.microsoft.com/en-us/troubleshoot/entra/entra-id/user-prov-sync/objects-dont-sync-ad-sync-tool
  - Run IdFix to check for duplicates, missing attributes, and rule violations: Use the IdFix DirSync Error Remediation Tool to find objects and errors that prevent synchronization to Microsoft Entra ID.

- **Microsoft Entra seamless single sign-on**
  - Microsoft Entra seamless single sign-on (Seamless SSO) automatically signs in users when they're using their corporate desktops that are connected to your corporate network. Seamless SSO provides your users with easy access to your cloud-based applications without using any other on-premises components.
  - https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sso-quick-start

- **What is Azure Private DNS**
  - Azure Private DNS provides a reliable and secure DNS service for your virtual networks. Azure Private DNS manages and resolves domain names in the virtual network without the need to configure a custom DNS solution.
  - To resolve the records of a private DNS zone from your virtual network, you must link the virtual network with the zone. Linked virtual networks have full access and can resolve all DNS records published in the private zone.
  - https://learn.microsoft.com/en-us/azure/dns/private-dns-overview

- **Back up a virtual machine in Azure**
  - You can protect your data by taking backups at regular intervals. Azure Backup creates recovery points that can be stored in geo-redundant recovery vaults. 
  - https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-portal


- **Databases architecture design**
  - https://learn.microsoft.com/en-us/azure/architecture/databases/
  
- **What is Azure Table storage?**
  - Azure Table storage is a service that stores non-relational structured data (also known as structured NoSQL data) in the cloud, providing a key/attribute store with a schemaless design.
  - You can use Table storage to store flexible datasets like user data for web applications, address books, device information, or other types of metadata your service requires.
  - https://learn.microsoft.com/en-us/azure/storage/tables/table-storage-overview

- **What is Azure role-based access control (Azure RBAC)?**
  - Here are some examples of what you can do with Azure RBAC:
    - Allow one user to manage virtual machines in a subscription and another user to manage virtual networks
    - Allow a DBA group to manage SQL databases in a subscription
    - Allow a user to manage all resources in a resource group, such as virtual machines, websites, and subnets
    - Allow an application to access all resources in a resource group
  - https://learn.microsoft.com/en-us/azure/role-based-access-control/overview

- **Secure access and data for workflows in Azure Logic Apps**
  - https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-securing-a-logic-app?tabs=azure-portal
  
  | Role | Description |
  |------|-------------|
  | Logic App Contributor | You can manage logic app workflows, but you can't change access to them. |
  | Logic App Operator | You can read, enable, and disable logic app workflows, but you can't edit or update them. |
  | Contributor | You have full access to manage all resources, but you can't assign roles in Azure RBAC, manage assignments in Azure Blueprints, or share image galleries. |

- **Azure built-in roles**
  - https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles
  
  | Role | Description |
  |------|-------------|
  | Contributor | Grants full access to manage all resources, but does not allow you to assign roles in Azure RBAC, manage assignments in Azure Blueprints, or share image galleries |
  | Owner | Grants full access to manage all resources, including the ability to assign roles in Azure RBAC. |
  | Role Based Access Control Administrator | Manage access to Azure resources by assigning roles using Azure RBAC. This role does not allow you to manage access using other ways, such as Azure Policy. |
  | User Access Administrator | Lets you manage user access to Azure resources. |

- **Create, change, or delete a network interface**
  - A network interface (NIC) enables an Azure virtual machine (VM) to communicate with internet, Azure, and on-premises resources.
  - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-network-interface?tabs=azure-portal

- **Generate and export certificates for point-to-site using PowerShell**
  - Generate a client certificate: Each client computer that connects to a VNet using point-to-site must have a client certificate installed. You generate a client certificate from the self-signed root certificate, and then export and install the client certificate. If the client certificate isn't installed, authentication fails.
  - https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-certificates-point-to-site

- **Create a virtual machine with a static private IP address**
  - When you create a virtual machine (VM), it's automatically assigned a private IP address from a range that you specify. This IP address is based on the subnet in which the VM is deployed, and the VM keeps this address until the VM is deleted. Azure dynamically assigns the next available private IP address from the subnet you create a VM in. If you want to assign a specific IP address in this subnet for your VM, use a static IP address.
  - https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/virtual-networks-static-private-ip?tabs=azureportal

- **Create, change, or delete a network security group**
  - https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group?tabs=network-security-group-portal

- **Create, Change, or Delete Azure Virtual Network Peering**
  - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-peering?tabs=peering-portal
  - A peering is established between two virtual networks. Peerings by themselves aren't transitive. If you create peerings between:
    - VirtualNetwork1 and VirtualNetwork2
    - VirtualNetwork2 and VirtualNetwork3
    1. There's no connectivity between VirtualNetwork1 and VirtualNetwork3 through VirtualNetwork2. If you want VirtualNetwork1 and VirtualNetwork3 to directly communicate, you have to create an explicit peering between VirtualNetwork1 and VirtualNetwork3, or go through an NVA in the Hub network.
  - You can't resolve names in peered virtual networks using default Azure name resolution. To resolve names in other virtual networks, you must use Azure Private DNS or a custom DNS server.
  - Resources in peered virtual networks in the same region can communicate with each other with the same latency as if they were within the same virtual network.
  
- **Create an Azure DNS zone and record using the Azure portal**
  - https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-portal

- **Configure Azure Storage firewalls and virtual networks**
  - Azure Storage provides a layered security model. This model enables you to control the level of access to your storage accounts that your applications and enterprise environments demand, based on the type and subset of networks or resources that you use.
  - The Azure Storage firewall provides access control for the public endpoint of your storage account. You can also use the firewall to block all access through the public endpoint when you're using private endpoints. Your firewall configuration also enables trusted Azure platform services to access the storage account.
  - You can grant access to Azure services that operate from within a virtual network by allowing traffic from the subnet that hosts the service instance. You can also enable a limited number of scenarios through the exceptions mechanism that this article describes. 
  - https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal