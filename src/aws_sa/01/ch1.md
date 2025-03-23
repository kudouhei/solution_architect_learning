## Authentication and Access Control Strategy

- Identity and Access Management
- Examining access control
- Leveraging access delegation
- Considering user federation
- Reviewing AWS Directory Service

### Identity and Access Management
AWS Identity and Access Management (IAM) is used to define and control who can access which resources in an AWS environment.

Key concepts:  
Every new AWS account comes with a root user that has full access to all AWS services and all the resources in the account.

As a best practice, it is recommended to do the following:
- Immediately protect that root user with multi-factor authentication (MFA).
- Secure the root user credentials and only use them if you need to perform specific service and account management tasks that only the root user can perform.

#### IAM users 
IAM users are the individual users who need access to AWS resources. They can be assigned specific permissions to access certain resources and perform certain actions.
IAM users are given permissions either by being directly assigned IAM policies or by being assigned to an IAM user group.

#### MFA (multi-factor authentication)
MFA is a security feature that requires users to provide two forms of identification when signing in to AWS. This adds an additional layer of security to the authentication process.

- The first is identity credentials such as username/password or access key/secret access key. 
- The second form takes the shape of a temporary six-digit numeric code.

#### IAM User Groups
An IAM user group is a collection of IAM users. IAM user groups can be assigned IAM policies which are then applied to all users in the group.

#### IAM Roles
An IAM role is an identity that possesses specific permissions. IAM roles are used to provide temporary credentials to entities (individuals, AWS services, or applications).

#### IAM Policies
An IAM policy is an object that allows access control on AWS. It can be assigned either to an IAM identity (user, user group, or role) or to an AWS resource.

IAM supports multiple types of policies: 

- Identity-based policies
  - Identity-based policies are JavaScript Object Notation (JSON) policy documents that are attached to IAM identities (users, user groups, or roles).
  - Example: gives read-only access to all Simple Storage Service (S3) buckets and objects.
    ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "s3:Get*",
                        "s3:List*"
                    ],
                    "Resource": "*"
                }
            ]
        }
    ```

- Resource-based policies
  - Resource-based policies are JSON policy documents that are attached to AWS resources.
  - Example: provide permissions to any principal in the account to get any object from the S3 bucket identified by the Resource attribute.
    ```json
        {
            "Version": "2012-10-17",
            "Id": "Policy123456789",
            "Statement": [
                {
                "Sid": "",
                "Action": [
                    "s3:GetObject"
                ],
                "Effect": "Allow",
                "Resource": "arn:aws:s3:::my-bucket/*",
                "Principal": "*"
                }
            ]
        }
    ```

- Permissions boundaries
  - Permissions boundaries allow us to define the maximum permissions that identity-based policies can give to IAM entities (user or role).
  - Example: suppose that you have an IAM user with the following identity-based policy. The policy gives them the ability to change their user’s password.
    ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "iam:ChangePassword",
                    "Resource": "*"
                }
            ]
        }
    ```

- Organizations’ service control policies (SCPs)
  - AWS Organizations is a service that allows us to centrally manage multiple AWS accounts belonging to the same organization. It provides the ability to structure them according to a hierarchy of organizational units (OUs).

- Access control lists (ACLs)
  - ACLs are service policies that let you control which principals in another account are allowed to access a resource in the current account. Amazon S3 but also services such as AWS Web Application Firewall (WAF), and Amazon Virtual Private Cloud (VPC) support ACLs.

- Session policies
  - Session policies are policies passed as a parameter when programmatically creating a temporary session for a role or a federated user.


### Examining access control

- Role-Based Access Control (RBAC)
- Attribute-Based Access Control (ABAC)


### Leveraging Access Delegation
Access delegation is essentially used for the following reasons:
- Providing an entity temporary access to resources that they do not have access to with their current privileges. This could be one of the following:
  - A user that needs temporarily elevated privileges to perform a specific task
  - An application or AWS service that requires specific privileges
- Providing an entity access to resources located in another AWS account.

#### Temporary Access Delegation
AWS STS is the central AWS service for requesting temporary security credentials on AWS. In a nutshell, AWS STS creates a new session on AWS with temporary security credentials that include an access key pair (access key, secret access key) and a session token.

#### Accessing Resources from One Account to Another
Access across accounts is not permitted by default on AWS; resources in one account are fully isolated within the account and cannot be accessed from other AWS accounts unless specific permissions are explicitly given.

#### AWS Resource Access Manager (RAM)
AWS RAM is a central service that allows you to share resources you own in one account with multiple accounts either within your own AWS OU or beyond.


### Considering User Federation
You can leverage either AWS Single Sign-On (AWS SSO) or AWS IAM to enable user federation depending on the use case.
AWS SSO is well suited for cases where you want to establish user federation across multiple AWS accounts and leverage your existing corporate or a third-party IdP.

#### Reviewing AWS Directory Service
AWS Directory Service offers several choices for organizations to deploy existing applications on AWS that rely on Microsoft AD or Lightweight Directory Access Protocol (LDAP). 

AWS Directory Service proposes different options to use Microsoft AD with AWS services, as follows:
- Simple AD: A low-scale and low-cost directory with basic Microsoft AD compatibility
- AD Connector: A proxy service to connect to a remote Microsoft AD on-premises
- Managed Microsoft AD: A Microsoft AD environment managed by AWS

