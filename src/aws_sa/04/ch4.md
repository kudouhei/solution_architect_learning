# Ensuring Cost Optimization

**Well-Architected Framework (WAF)**
**Simple Notification Service (SNS)**

- Cost optimization principles
- Establishing governance with tagging
- Monitoring with alerts, notifications, and reports

### Cost optimization principles

- Consumption-based pricing model: the cloud simplifies the pricing of resources based solely on their consumption. 
- Setting up FinOps CoEs: Setting up FinOps CoEs (meaning financial operations centers of excellence) enforces collaboration and a sense of shared responsibility between teams when it comes to IT resources and costs to procure, run, and manage them. 
- Attribute expenses with owners: A FinOps CoE can define, as well as put in place, controls to monitor cost expenditure across the cloud by attributing each resource to a particular team, project, or user.
- Continuous measurement and monitoring: cost optimization is not a one-stop process but rather a continuous operation that involves constant measurement and monitoring of resources and usage patterns.
- Adopting cloud native: A key design principle of cost optimization is to look for opportunities to leverage as many cloud-native services as possible.


### Establishing governance with tagging
**what are tags?**
Tags are key-value pairs of metadata that help identify resources in your AWS account. Each tag’s key is a unique identifier and each key can have only one value associated with it. You can create tags and assign them to almost all AWS resources that you create throughout your AWS accounts, including IAM users, roles, EC2 instances, RDS databases, S3 buckets, and so on and so forth. 
- The most important tagging feature that AWS provides specifically for cost management is AWS cost allocation tags.
- A cost allocation tag is an AWS feature that helps monitor your resource usage and costs granularly. 

There are two types of cost allocation tags:
- AWS-generated: these tags are created and propagated by AWS for supported resources for cost-tracking purposes. Resources are tagged with the `createdBy` key automatically, and its corresponding value is one of the following attributes: `account-ID`, `access-key`, `user-name`, or `role`.

The following are some examples of this:
```bash
key = aws:createdBy
value = 1234567890:dummyUser
# or
key = aws:createdBy
value = AKIAUITOFQDN5EXAMPLE:dummyIamRole
```

- User-defined: These tags are created, applied, and managed by individual users, or in most cases, by a centralized FinOps team.

```bash
key = EnvironmentName
value = Production

# or
key = Department
value = DEV01
```

#### Tagging Strategies and Considerations
Once the team is created, start by defining consistent tagging values to be used across all workloads on the cloud. These values can be based on factors such as the following:
- `Owner of the resource`: Identifying who is responsible for the resource
- `Deployment stack`: Describing an environment such as development or staging
- `Cost center`: Identifying, tracking, and charging back the department that is utilizing the resources
- `Project/application`: Describing and grouping the resources required to run a particular project or application
- `Compliance`: An optional but important value that can help identify workloads based on security compliance requirements such as the `Health Insurance Portability and Accountability Act (HIPAA)` for healthcare data, and `Payment Card Industry Data Security Standard (PCI-DSS)` for handling credit card information
- Keep the tags consistent and up to date with the help of automation such as AWS CloudFormation templates or AWS Systems Manager Automation.

### Monitoring with alerts, notifications, and reports
Amazon CloudWatch is a monitoring and observability service that provides data and actionable insights to monitor applications, resources, and systems.


**Viewing reports**
AWS Cost Explorer provides you with out-of-the-box reports with insights into the most common usage and spending patterns, such as Daily costs, Monthly costs by service, Reserved Instance report, and Monthly EC2 running hours costs.



