## Compliance and Cloud Governance

### Azure Regions

Azure regions are geographical locations where the data is stored and processed.

- Regions offer flexibility for customers to deploy resources to regions that are close to their customers.
- Regions ensure data residency for customers.
- Regions offer compliance and resiliency options.
- When you deploy a resource in Azure, in most cases you will be asked to choose a region.
- Certain services are region specific, and the availability is limited to some regions when they are launched. Gradually, Microsoft will expand the service to other regions.
- Services like Azure AD, Azure Traffic Manager, and Azure DNS do not require a region. The region for these resources will be shown as Global in the Azure portal.
- Each Azure region is paired with another region within the same geography to form regional pairs.

**Regional Pairs**
An `Azure geography` is defined as an area of the world that consists of one or more Azure regions.

Similarly, the European Union has the `General Data Protection Regulation (GDPR)` where organizations cannot store personal data of the EU citizens outside EU member states.

Azure pairs one region with another region within the same geography. Regional pairs play a vital role in business continuity and disaster recovery (BCDR).

The following are some of the focus points about Azure regional pairs:
- Physical Separation: Three hundred miles is the preferred distance between datacenters that are part of the regional pair;
- Replication: Services like storage accounts provide georedundant storage (GRS). Using GRS, your data will be replicated to the paired region and thus provide reliability.
- Recovery Order
- Serialized Updates
- Data Residency
 

### Azure Accounts and Subscriptions

**Azure Accounts**: Subscriptions will always be mapped to an account. Any identity that is part of Azure AD or a directory trusted by Azure AD is referred to as an Azure account.

**Azure Subscriptions**: The user who created the Azure account is called the Account Administrator, and a user can have multiple subscriptions inside an account.

By default, only the **account administrator** will have access to the newly created subscription. If you would like to grant access to others, Microsoft recommends that you use **RBAC (role-based access control)** for granting access to users and external partners to your Azure resources.

![Azure Accounts and Subscriptions](./images/01.png)

#### Getting a Subscription
- Enterprise Agreements (EAs)
- Web Direct
- Reseller
- Partners

![Azure Subscription](./images/04.png)

#### Subscription Metering
- Free subscription
- Pay-As-You-Go
- Enterprise Agreement
- Azure for Students

![Azure Subscription](./images/05.png)

### Azure Cost Management
Azure Cost Management is the go tool for performing your billing administrative tasks and for monitoring costs.

**Cost Saving Techniques**
- Reservations: Reserved instances (RIs), or reservations, can be used by customers to save costs on selected services.
- Azure Hybrid Benefit: You can bring your own Windows Server or SQL Server or Linux licenses to use on Azure Virtual Machine, Azure SQL Database, and Azure Managed Instances.
- Azure Credits and Dev/Test Subscriptions
- Azure Regions
- Budgets
- Pricing Calculator

### Resource Groups
A resource group is a container used for the logical organization of resources in Azure.


### Management Groups
Using management groups, you can logically group subscriptions.

![Management Groups](./images/06.png)

### Azure Policy
Azure Policy constantly runs evaluations or scans on your resources to make sure they are compliant. Azure Policy can stop new resources from breaking the compliance requirements. Azure Policy cannot delete resources that are noncompliant.

![Azure Policy](./images/12.png)

Key features of Azure Policy include the following:
- Compliance and Enforcement: 
  - You can leverage the built-in policies or build custom policies to ensure that the compliance requirements are met.
- Apply Policies at Scale: 
  - You can apply policies at the management group level so that the policy is inherited to all subscriptions that are part of the management group.
- Mitigation and Remediation:
  
There are lot of **built-in policies** that come with the Azure Policy service. Nevertheless, administrators can always build custom policies to match your organizational requirements. Some of the use cases of Azure policies are as follows:
- Control the resource types that your organization can deploy to Azure.
- Restrict the deployment of virtual machines to a specific set of SKUs.
- Limit the deployment of resources to selected regions only.
- Enforce required tags and its value to resources during deployment.
- Audit that Azure Backup service is enabled for all virtual machines.

#### Implementing Azure Policy
Implementing an Azure policy comprises three main parts:
- Policy Definition
  - The definition is a JSON manifest that describes what action will be taken by the policy if it’s assigned. The policy contains the condition and effect.
- Policy Assignment and Scope
  - Supported scopes include management groups, subscriptions, and resource groups.
- Policy Evaluation

#### Implementing Initiatives
Using initiatives, you can chain or combine multiple policies, assign them on a scope, and manage them.

![Initiatives](./images/13.png)


### Role-Based Access Control
Role-based access control (RBAC) is used for the access management of cloud resources. RBAC has built-in roles that provide fine-grained access management of resources.

![RBAC](./images/07.png)

The following are some of the use case scenarios of Azure RBAC:
- Allow a user to perform all actions on resources
- Allow a group to manage virtual machines
- Allow a user to work as a help-desk agent and open cases with Microsoft Support
- Allow an application to manage IP addresses

RBAC assignment is all about the three Ws (who, what, and where): in simple terms, to whom you want to give the permission (who), the set of permissions you are providing (what), and the scope to which this role is assigned (where). Let’s comprehend these concepts.
- Security Principal (Who)
- Role Definition (What)
  - This definition is defined in a JSON file.
  - in Azure CLI, you can use `az role definition list --name Owner` to see the same output.
- Scope (Where)

In the figure illustrates how the security principal, role definition, and scope are combined to create a role assignment.
![RBAC](./images/02.png)

#### Azure RBAC Roles
There are four Azure fundamental roles that you should be aware of:
- Owner: 
  - Has full access to the scope to which this is assigned; also as an Owner you can delegate access to other users.
- Contributor: 
  - Has the same level of resource permissions as Owner; however, Contributor cannot delegate access to others.
- Reader: 
  - Assigns a read-only role
- User Access Administrator: 
  - Can delegate access to other users; however, this role cannot manage any resources.

![RBAC](./images/08.png)

![RBAC](./images/09.png)

#### Custom RBAC Roles
You can create custom RBAC roles to meet your specific needs.

- Custom RBAC roles can be used to create fine tuned roles for your environment, if the built-in roles doesn’t meet your specific needs
- Custom roles can be created from Azure Portal, Azure PowerShell, Azure CLI and REST API
- Each directory can have up to 5000 custom roles
- We can assign custom roles to users, groups, and service principals to any scope; same way we work with built-in roles.

#### Role Assignment

![Role Assignment](./images/03.png)

**Creating a Custom Role Using PowerShell**

```powershell
Get-AzRoleDefinition | FT  # List all roles

Get-AzResourceProvider | FT # List all resource providers
```

If you need to clone a built-in role and modify the JSON with the permissions in which you are interested, you can use the following command:

```powershell
Get-AzRoleDefinition -Name "Owner" | ConvertTo-Json | Out-File "Owner.json"
```


### Resource Locks
In Azure, administrators can use locks to lock a subscription, resource group, or resource from getting deleted or modified. The lock will override any permission that is granted to you via RBAC.

There are two lock levels: CanNotDelete and ReadOnly.
- **CanNotDelete** means that users are restricted from deleting the resource; however, the resource can be modified.
- **ReadOnly**, means you will be able to read the resource; deletion or modification of the resource is not permitted.

To create or delete locks, you need to be Owner or User Access Administrator. If you are using custom roles, then `Microsoft.Authorization/*` or `Microsoft.Authorization/ locks/*` should be there in your actions section.

![Resource Locks](./images/11.png)

### Resource Tags
Resource tags can be used to logically organize the resources in your environment. Each tag comprises a key-value pair, where you will be adding a name and a corresponding value.

![Resource Tags](./images/10.png)



