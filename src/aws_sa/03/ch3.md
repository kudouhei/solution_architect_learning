# Designing a Multi-Account AWS Environment

- Deciding on resource and billing isolation
- Introducing AWS Organizations
- Setting up service control policies (SCPs)
- Leveraging AWS Control Tower

### Deciding on resource
The first decision that an organization needs to make when starting to use AWS is deciding how to organize its AWS resources. AWS provides several structures to help you with that, such as AWS Organizations, organizational units (OUs), accounts, virtual private clouds (VPCs), and subnets.

- business units (BUs)
- organizational units (OUs)
- virtual private clouds (VPCs)
- Availability Zones (AZs)

#### what is the best approach to resource isolation?
To start with, an AWS account provides the highest degree of isolation for resources on AWS. Therefore, it is strongly recommended, as a best practice, to distribute and separate your resources and workloads across multiple accounts. 

1. The first natural separation is between production and non-production resources.
2. A second method involves achieving strong isolation of resources at a network level, even within the same account, by assigning them to different VPCs—that is, different virtual networks.
   - By default, resources located in different VPCs cannot reach each other; there is no route that connects multiple VPCs by default.
   - If you need inter-VPC connectivity, you must enable it.
3. A third approach would be to distribute your AWS resources further across separate subnets within a given VPC.
   - Inter-subnet connectivity is enabled by default. 


### Introducing AWS Organizations
AWS Organizations is an account management service. Its role is to help large and complex organizations handle their AWS environment more efficiently.

**Managing Policies Across Accounts and Filtering out Unwanted Access**
- Authorization Policies
  - IAM policies
  - SCPs
The major difference between the two is that SCPs apply at the organization or OU level while permissions boundaries apply at the more granular level of IAM entities.

- Management policies
  - Artificial intelligence (AI) services opt-out policies: 
    - This type of policy lets you decide whether you allow AI services to collect data when they’re being used across your organization
  - Backup policies: 
    - Backup policies are meant to centrally manage and enforce backup plans across your entire organization, so that you don’t have to set this up account per account.
  - Tag policies: 
    - Tag policies provide a means to centrally decide which tags are attached to the AWS resources across your organization.
  
To check the effective policy applied to your account(s), you can, from the command line, run the command given below. This will yield the managed policy that would be applied on your account’s concerned resources:

```bash
aws organizations describe-effective-policy --policy-type <POLICY-TYPE>
```
Here, `<POLICY_TYPE>` is either `BACKUP_POLICY`, `TAG_POLICY`, or `AISERVICES_ OPT_OUT_POLICY`.


Notes:
- Simple Storage Service (S3)
- Amazon Elastic Block Storage (EBS)
- Amazon Elastic Compute Cloud (EC2)
- Amazon Elastic Container Service (ECS)
- Amazon Elastic Kubernetes Service (EKS)
- Amazon Elastic MapReduce (EMR)
- Amazon Elastic Transcoder (ET)

### Setting up service control policies (SCPs)
SCPs offer central control over that maximum set of permissions that accounts in an OU or across your entire organization can have. However, it is important to understand that SCPs do not grant any permission to IAM entities (users and roles) in your accounts; they can only limit what the entities are allowed to do.

In practice, SCPs are expressed in two ways, either as deny lists or as allow lists. The most common way of using SCPs is as deny lists, mostly because they are low maintenance. 

**Using SCPs as Deny Lists**
AWS Organizations, by default, attaches a managed SCP named FullAWSAccess to every root and OU structure upon creation.

For example, the following SCP blocks access to the Amazon RDS service:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyRDSAccess",
      "Effect": "Deny",
      "Action": "rds:*",
      "Resource": "*"
    }
  ]
}
```

**Using SCPs as Allow Lists**
If you want to use SCPs as allow lists, you must replace the AWS-managed FullAWSAccess SCP mentioned previously with one or more SCPs that explicitly allow only those services and actions you want to authorize. 

For example, the code in the following example grants explicit permissions to perform all actions on Amazon Elastic Compute Cloud (EC2) and Amazon S3 services, but implicitly denies access to any other service:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:*",
        "s3:*"
      ],
      "Resource": "*"
    }
  ]
}
```

### Leveraging AWS Control Tower
Control Tower is an AWS service that addresses all the aspects covered earlier in this chapter in a prescriptive way. It is an opinionated service that allows you to automate the setup of your baseline environment—in other words, your landing zone.

On top of these best practices, Control Tower relies on multiple other AWS services such as, but not limited to, `AWS Organizations`, `AWS Config`, `AWS Service Catalog`, `AWS SSO`, and `AWS CloudTrail`.

**What does Control Tower Deliver Exactly?**
- First and foremost, it will create what we call your landing zone—that is, your multi-account AWS environment set up according to AWS best practices
- Second, Control Tower will provide and enforce guardrails across your entire organization.
- Thirdly, Control Tower will create an account factory that you can configure and leverage to automatically provision new accounts with pre-approved configurations. 
- Finally, Control Tower comes with a dashboard that lets your AWS system administrators oversee the landing zone operations and control their status.

**How does Control Tower Operate?**
Upon setup, Control Tower deploys a certain number of resources in your organization. It leverages CloudFormation templates through stacks and stacksets to deploy and manage these resources.
- First, Control Tower will create a root for your new organization or reuse your existing organization root, depending on your specific case.
- It will then create two OUs, security (always) and sandbox (optional) under that root structure. 
- Control Tower will then set up AWS SSO with a user directory, preconfigured groups, and SSO access.
- Control Tower will apply a number of preventive guardrails to enforce best practices.
- Control Tower will also apply some mandatory detective guardrails to detect configuration violations.

Preventive guardrails are implemented using SCPs, while detective guardrails are implemented using `AWS Config` rules and `AWS Lambda` functions.

The following is an example of a mandatory preventive guardrail implemented by Control Tower using SCPs, which prevents any change to CloudTrail settings by Control Tower itself:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GRCLOUDTRAILENABLED",
      "Effect": "Deny",
      "Action": [
        "cloudtrail:DeleteTrail",
        "cloudtrail:PutEventSelectors",
        "cloudtrail:StopLogging",
        "cloudtrail:UpdateTrail"
      ],
      "Resource": ["arn:aws:cloudtrail:*:*:trail/awscontroltower-*"],
      "Condition": {
        "ArnNotLike": {
        "aws:PrincipalARN":"arn:aws:iam::*:role/
          AWSControlTowerExecution"
        }
      }
    }
  ]
}
```

The example below illustrates detective guardrails. It configures a mandatory guardrail implemented by Control Tower on the Security OU that detects whether public read access is enabled on the S3 buckets within the accounts belonging to that OU:

```
AWSTemplateFormatVersion: 2010-09-09
Description: Configure AWS Config rules to check that your S3
buckets do not allow public access
Parameters:
  ConfigRuleName:
    Type: 'String'
    Description: 'Name for the Config rule'
Resources:
  CheckForS3PublicRead:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: !Sub ${ConfigRuleName}
      Description: Checks that your S3 buckets do not allow public read access. If an S3 bucket policy or bucket ACL allows public read access, the bucket is noncompliant.
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_READ_PROHIBITED
      Scope:
        ComplianceResourceTypes:
          - AWS::S3::Bucket
```
