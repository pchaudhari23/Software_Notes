IAM:

- Users - long term credentials
- Groups
- IAM Roles:
- Assume an IAM Role - A particular resource can get an IAM role to use other AWS services.
- Short term credentials, role does not belong to any specific user or group, use roles for cross account access of AWS services, use roles by identity providers instead of IAM User for workforce
- If you have resources that are running inside AWS that need programmatic access to various AWS services, then the best practice is always to use IAM roles.
- However, applications running outside of an AWS environment will need access keys for programmatic access to AWS resources.
- We cannot modify the launch configuration of an ASG once it is created.
- Create a policy and use STS to assume an IAM role.
  Policies:

1. AWS managed policies
2. Customer managed policies
3. Inline policies
4. Resource based policies: To grant direct, cross-account access to some resources, such as Amazon S3 buckets.

- Policy - Version, Statement: Array of object. Object - Effect(Allow/Deny), Action(\* - Wildcard for all actions on a resource), Resource, Condition
- Use policies to grant permissions to perform an operation in AWS.
  Cross Account Access:
- Create an IAM role in destination account or desired account and modify its trust policy. Add the source resource as a trusted entity in the role's trust policy.
- Resource in the source account assumes the IAM role.
- Source account => Destination account

1. Create a role in the destination account.
2. Give permissions in source account to assume that role.

- Service assumes Role - Role has policies.

---

Compute:

- Security group rules
- EC2 instance types and use cases
- EC2 is a virtual machine!!! (Remember this)
- So it might be either a virtual machine OR cloud function OR a container
- EBS Volume types
- Auto Scaling groups: Target groups, scaling policies - how many instances will be added or removed - maximum capacity, desired capacity, minimum capacity, scaling policy, current capacity
- AWS ELB:Target Groups
- AWS Auto Scaling Group:Launch Template

---

- High scalability - Load Balancing and Auto scaling groups
- High availability - Multi AZ load balancing and Multi AZ auto scaling group
- Every load balancer has a set of instances to which it will redirect the requests.
- That set of instances, IP address or other load balancers is called target group.
- That target group can scale - Auto scaling group

---

- VPC - Private subnet and public subnet.
- Need a CIDR range to create subnet.
- Private subnets cannot be accessed from internet. Uses NAT Gateway.
- Public subnet can be accessed from internet. Uses Internet Gateway, VPC Endpoints

---

- Amazon SQS - Queue - Producer & Consumer. Consumers poll messages. Polling - Checking something again and again after particular time.
- Amazon SNS - Notification - Publisher & Subscriber. Send messages to SNS Topics
- RDS, Aurora, RDS Proxy - Read Replicas
- Amazon S3 - Buckets(directory), object(file)
- CloudFront - Edge locations, Cloudfront distributions
- ECS - Tasks, Task definition, Launch types - EC2 & Fargate, Task placement strategies
- ECS - Task, EKS - POD
- Elastic Beanstalk - Used to deploy applications, Deployment modes, CLI commands, EB Extensions
- ACM - Provision SSL certificates
- SAM Commands

---

Route 53:

- DNS Records, records type - A, AAAA, CNAME, NS. What is a DNS Record?, Hosted zone - Public and Private
- Records, Created EC2 instances in different AZs and used an ELB. Traffic redirected to different EC2 instances based on public IP of the instance. Route 53 record points to the ELB DNS.

---

AWS Kinesis:

- Kinesis data streams - Shards, capacity modes (similar to Dynamo DB Streams)
- Data Streams are divided into partitions called shards
- KCL - Kinesis Client Library - Uniquely identify a shard based on partition key
- KCL: 1 Shard - 1 KCL => No. of ec2 instance <= no. of shards
- 1 KCL - Multiple shards but 1 shard - 1 KCL

---

AWS REGIONS => ONE OR MORE AVAILABILITY ZONES => MULTIPLE DATA CENTERS

Elastic Beanstalk, SAM, CDK => Cloudformation => S3

CloudFormation:

- Template - YAML file - upload to S3, Template contains - Parameters, Conditions, Resources, Outputs, Mappings
- Resources
- Parameters - Dynamic inputs to template
- Mappings - Static variables in template.
  Fn::FindInMap OR !FindInMap [ MapName, TopLevelKey, SecondLevelKey ]
- Outputs - References to what is created - exported items
- Conditions - List of conditions to perform resource creation
- Condition Functions
  Fn::And
  Fn::Equals
  Fn::If
  Fn::Not
  Fn::Or
- Functions - Learn all the functions
  Fn::Ref
  Fn::GetAtt
  Fn::FindInMap
  Fn::ImportValue
  Fn::Join - !Join [ delimiter, [comma seperated list of values] ]
  Fn::Sub - substitute variable
- References - Reference a parameter - Fn:Ref OR !Ref,
- Nested stack - Reusable stack components
- Cross stack reference - Fn::ImportValue OR !ImportValue
- Changestack - see how the updated stack will behave before deploying it
- Stackset - Manage stacks across multiple accounts or regions with single operation

---

CloudFront:
Signed URL - Access to individual files - Premium users content
Signed cookies - Access to multiple files

---

S3 and Dynamo DB - Have VPC Endpoint, rest have to use ENI.

- Endpoint types - 1.Interface endpoints (ENI), 2.Gateway endpoints (Only S3 and DynamoDB)
  IAM - ECS - EC2 Launch type - EC2 Instance profile.

---

Containerization:

1. ECS
2. Fargate
3. ECR
4. EKS
5. Copilot - CLI for ECS

---

Integration:

- SQS:

1. Standard Queue
2. FIFO Queue
3. DLQ
4. Delay Queue

- SNS
- Kinesis:

1. Kinesis Data Streams
2. Kinesis Data Firehose
3. Kinesis Data Analytics - SQL Application

---

Monitoring:

- Cloudwatch

1. Cloudwatch Metrics
2. Cloudwatch Logs - Log groups, log streams, logs insights, log subscriptions - real time logs
3. Cloudwatch Alarms
4. Cloudwatch Events/EventBridge

- X-Ray
- CloudTrail

---

- CreateQueue (MessageRetentionPeriod), DeleteQueue
- PurgeQueue: delete all the messages in queue
- SendMessage (DelaySeconds), ReceiveMessage, DeleteMessage
- MaxNumberOfMessages: default 1, max 10 (for ReceiveMessage API)
- ReceiveMessageWaitTimeSeconds: Long Polling
- ChangeMessageVisibility: change the message timeout
- Batch APIs for SendMessage, DeleteMessage, ChangeMessageVisibility helps decrease your costs
- MessageGroupID: Message grouping in SQS FIFO Queue

---

Kinesis - Provisioned mode and On-demand mode

CDK(Constructs - Define infrastructure in a programming language) => CDK CLI (Compiler) => CloudFormation Template => CloudFormation

AWS Amplify: Backend As A Service - Similar to Firebase. Used by frontend and mobile devs to build full stack apps.

Interview question:

1. Why AWS, why not Azure or GCP?
2. How is AWS better choice than them?
3. Learn a bit of other cloud platforms as well

---

AWS: Learn CLI commands and know some sdk libraries - for lambda etc...
3 Ways to interact with any cloud platform: 1.Web console, 2.CLI, 3.SDK, 4.REST API(Azure)

Pub sub architecture - usually for event driven apps

---
