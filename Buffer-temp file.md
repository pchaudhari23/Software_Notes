Infrastructure As A Code - Use YAML file - Dockerfile, Kubernetes, Cloud formation, Elastic beanstalk

Access locally running project in vs code through internet via port forwarding. Copy port of project in ports tab.

---

How to make github copilot in vs code access bitbucket PR and JIRA?

How to connect various plugins to llms?

Explore all the AI options in VS Code?

Github copilot vs M365 Copilot vs Copilot

---

- Maximum number of your instances can be equal to the number of open shards of the Kinesis stream
- Any real time changes to dynamodb - DynamoDB streams
- The execution context is a temporary runtime environment that initializes any external dependencies of your Lambda function code, such as database connections or HTTP endpoints.

---

Gray areas/revise:
Dynamo DB Capacity calculations

1. Write:

- Standard write:
  WCU = item_size_in_KB rounded up to nearest 1 KB
- Transactional write:
  WCU = (item_size_in_KB rounded up to nearest 1 KB) × 2

2. Read:
   Blocks = (item_size_in_KB rounded up to nearest 4 KB) ÷ 4

- Strongly consistent reads:
  RCU = Blocks
- Eventually consistent reads:
  RCU = Blocks ÷ 2
- Transactional reads:
  RCU = Blocks x 2

---

Lambda function concurrency calculations

1. Event based invocations - S3, API Gateway:
   Concurrent executions = (invocations per second) x (average execution duration in seconds)
2. Stream based invocations - Kinesis data stream, DynamoDB stream:
   Concurrent executions = Number of shards
3. Poll based invocations:
   Concurrent executions = Number of active batches being processed = (Messages received per second × Processing time) / Batch size

- Deployment techniques

---

Project study:

1. Project use case
2. Technologies, libraries, versions
3. Repository structure
4. Entry point
5. Components, modules
6. Data flow
7. Code snippets, functions, library classes and APIs
8. Improvements, Challenges, tradeoffs, tech decisions
