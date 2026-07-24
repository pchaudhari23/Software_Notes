EC2 Instance purchase options and use cases:

1. On-Demand Instances – short workload, predictable pricing, pay by second
2. Reserved Instances (1 & 3 years) – long workloads
3. Convertible Reserved Instances – long workloads with flexible instances
4. Savings Plans (1 & 3 years) – commitment to an amount of usage, long workload
5. Spot Instances – short workloads, cheap, can lose instances (less reliable)
6. Dedicated Hosts – book an entire physical server, control instance placement
7. Dedicated Instances – no other customers will share your hardware
8. Capacity Reservations – reserve capacity in a specific AZ for any duration

---

EBS Volume types:

1. General Purpose SSD - gp3, gp2
2. Provisioned IOPS SSD - io1, io2, io2 Block Express
3. Throughput Optimized HDD - st1
4. Cold HDD - sc1

---

S3 Storage classes:

1. Standard
2. Standard IA
3. Intelligent Tiering
4. One-Zone IA
5. Glacier Instant Retrieval
6. Glacier Flexible Retrieval
7. Glacier Deep Archive

Retrieval options:

1. Standard retrieval
2. Bulk retrieval
3. Expedited retrieval
4. Ranged archive retrieval

---

Deployment methods:

1. All at once
2. Rolling
3. Rolling with additional batches
4. Immutable
5. Blue Green
6. Traffic Splitting/ Canary deployment

---

DynamoDB capacity unit formulas:
Write capacity units:

- 1 WCU = 1 write/sec for 1KB item
- WCUs = No of item writes/sec \* (Item size in KB/1 KB)
- Item size in decimal values get rounded to upper KB

Read capacity units:

- 1 RCU = 1 Strongly consistent read/sec OR 2 Eventually consistent read/sec for 4 KB item
- RCUs = No of Strongly consistent reads/sec \* (Item size in KB/4 KB)
- RCUs = (No of Eventually consistent reads/sec)/2 \* (Item size in KB/4 KB)
- Item size must be in multiple of 4. If not, it gets rounded to upper multiple of 4

---

Dynamo DB formula misc:

DynamoDB Capacity & Partition Formulas

1. Transactional Capacity

Transactional operations consume **2× the normal capacity**.

- **Transactional RCUs** = **Normal RCUs × 2**
- **Transactional WCUs** = **Normal WCUs × 2**

---

2. Partitions by Capacity

Each physical partition supports:

- **3,000 RCUs**
- **1,000 WCUs**

Read Partitions = Total RCUs / 3000

Write Partitions = Total WCUs / 1000

Partitions by Capacity = max(Read Partitions, Write Partitions)

or

Partitions by Capacity = max(RCUs / 3000, WCUs / 1000)

**Note:** Use **max()**, **not addition (+)**.

---

3. Partitions by Size

Each partition can store up to **10 GB**.

Partitions by Size = Total Table Size / 10 GB

---

4. Total Number of Partitions

Total Partitions = ceil(max(Partitions by Capacity, Partitions by Size))

where:

- `max()` = choose the larger value
- `ceil()` = round up to the nearest whole number

---

Example

Given:

- RCUs = 9,000
- WCUs = 1,500
- Table Size = 25 GB

Step 1: Capacity Partitions

Read Partitions = 9000 / 3000 = 3

Write Partitions = 1500 / 1000 = 1.5

Partitions by Capacity = max(3, 1.5) = 3

Step 2: Size Partitions

Partitions by Size = 25 / 10 = 2.5

Step 3: Final Partitions

Total Partitions = ceil(max(3, 2.5))
                 = ceil(3)
                 = 3

---

DynamoDB Cheat Sheet

| Formula                | Expression                                                |
| ---------------------- | --------------------------------------------------------- |
| Transactional Read     | `RCUs × 2`                                             |
| Transactional Write    | `WCUs × 2`                                             |
| Read Partitions        | `RCUs / 3000`                                           |
| Write Partitions       | `WCUs / 1000`                                           |
| Partitions by Capacity | `max(RCUs / 3000, WCUs / 1000)`                         |
| Partitions by Size     | `Table Size / 10 GB`                                    |
| Final Partitions       | `ceil(max(Partitions by Capacity, Partitions by Size))` |

---

ECS Task placement strategies: {type: "", field: ""}

1. binpack
2. random
3. spread
4. combination of above three

ECS Task Placement constraints:

1. distinctInstance: placed on seperate instances
2. memberOf: Instance which satisfy an expression of Cluster Query Language. {type: "", expression: ""}

---

SAM Commands:

1. sam build: fetch dependencies and create local deployment artifacts
2. sam package: package and upload to Amazon S3, generate CF template
3. sam deploy: deploy to CloudFormation

---

CDK Commands:

1. npm install -g aws-cdk-lib: Install the CDK CLI and libraries
2. cdk init app: Create a new CDK project from a specified template
3. cdk synth: Synthesizes and prints the CloudFormation template
4. cdk bootstrap: Deploys the CDK Toolkit staging Stack
5. cdk deploy: Deploy the Stack(s)
6. cdk diff: View differences of local CDK and deployed Stack
7. cdk destroy: Destroy the Stack(s)

---

CloudFormation:
Python scripts:

1. cfn-init: Use to retrieve and interpret resource metadata, install packages, create files, and start services.
2. cfn-signal: Use to signal with a CreationPolicy or WaitCondition, so you can synchronize other resources in the stack when the prerequisite resource or application is ready.
3. cfn-get-metadata: Use to retrieve metadata for a resource or path to a specific key.
4. cfn-hup: Use to check for updates to metadata and execute custom hooks when changes are detected.

Commands:
aws cloudformation package: packages the local artifacts and upload to S3
aws cloudformation deploy: deploy the template. The template must be stored in S3 only
aws cloudformation validate-template: check the template if it is a valid JSON or YAML file
aws cloudformation update-stack: update an existing stack

---
