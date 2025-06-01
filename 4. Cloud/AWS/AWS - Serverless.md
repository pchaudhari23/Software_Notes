API Gateway:

- Override status codes
- Enforce validation rules
- Response transformation
- Method requests and response
- Integration request and response
- Body mapping templates
- Caches
- Throttling
- Resources
- Create API, Create Methods, Create Resources
- Models
- Deployment stages and stage variables (also learn Lambda alias and version with this)

---

Request - Response cycle

- Method Request: Request object schema validation
- Integration Request: Connecting API to lambda, Body mapping template
- Integration Response: Assign value - '\*' to Access-Control-Allow-Origin header, Body mapping template
- Method Response: Add response header for CORS - Access-Control-Allow-Origin

Cache-Control: max-age=0

- JSON Schema - JSON-schema.org
  BODY MAPPING TEMPLATE:
- $input: variable which gives request data (body, params...)
- json():a method on $input which will retrieve a JSON representation of the data you access. $ here stands for the request body as a whole
- mapping template extracts data from model if we don't want to pass whole model

---

Lambda Functions:

- Synchronous invocations
- Asynchronous invocations
- Trigger events
- Concurrency, Provisioned and Reserved
- Throttling
- Lambda@Edge
- Storage
- Versions and Aliases
- Layers and dependencies

---

event - contains the request object
callback: used to return something from the lambda function.
two properties:

1. Error
2. Response object

---

- Event triggers - Push and poll based
- Account concurrency: 1000
- Minimum 100 must be unreserved
- Rest 900 can be divided among all functions in the account as reserverd concurrency
- For above 1000 concurrency limit, request to AWS to increase the limit.

Poll based source: Kinesis, SQS, Dynamo DB streams
Concurrency execution = Number of shards sending the data to lambda function

Push based source: Amazon S3, API Gateway
Concurrency execution = No. of events/ sec x No. of sec required for processing every event

- Reserved concurrency
- Unreserved concurrency - Used for functions that do not have a limit explicitly set to them.
- Provisioned concurrency
- Beyond concurrency: Requests are throttled. To prevent many requests at a time. Error code 429 is returned. Incoming request is rejected.

Provisioned concurrency:

- Scale the function without fluctuations in latency
- The functions which are allocated provisioned concurrency, the requests are served by initialized instances with low latency.

---

Exceptions:

1. InvalidParameterValueException - parameters in the request is invalid. Eg: Lambda is unable to assume an IAM role
2. CodeStorageExceededException - exceeded your maximum total code size per account
3. ResourceConflictException - the resource already exists
4. ServiceException - encountered an internal error

Execution Context - Temporary runtime environment that initializes any external dependencies of your Lambda function code, such as database connections or HTTP endpoints.

exports.fn = (event, context, callback) => {
callback(null, {message: 'Hi world from lambda!!!'});
}

---

exports.handler = (event, context, callback) => {
callback(null, 'Hello from lambda');
}

---

Dynamo DB - NoSQL data storage:

- Partition key - Must be unique, it is like a partition. Partition key is primary key in dynamo db
- Stores data in SSD by making partions
- Partion key + Sort key can be another primary key. Both partition and sort keys must be unique.
- Partition key + Sort key = Composite key
- create a dynamo db instance in lambda function and call api methods on that instance.
- putItem() - to create a single record
- scan() - to retrive multiple records
- getItem() - to retrive a single record
- deleteItem() - to delete a record

const params = {
Item:{}
TableName:'.....'
}

Writing to database:
1.Conditional write expression

Reading from database:

1. Scan - Scans the entire table or secondary index. Filter is used after scanning. Scan operation uses eventually consistent reads when accessing the data in a table.
2. Query - Finds the values based on primary key. Query the secondary index or table based on composite primary key.

---

Primary key = partition key + sort key
Primary key - High cardinality attributes
GSI - Different partion and sort key
LSI - Same partition key but different sort key

Global Secondary Index:

- Eventual consistency
- you can add a GSI to an already existing table
- Queries or scans on this index consume capacity units from the index, not from the base table.
- 20 GSI per table
- The provisioned write capacity for a global secondary index should be equal to or greater than the write capacity of the base table
- If writes are throttled on index, the main table will be throttled.

Local Secondary Index:

- Eventual consistency and strong consistency.
- Queries or scans on this index consume read capacity units from the base table.
- Local secondary indexes are created at the same time that you create a table. You cannot add a local secondary index to an existing table, nor can you delete any local secondary indexes that currently exist.
- 5 LSI per table
- Queries or scans on this index consume read capacity units from the base table
- For each partition key value, the total size of all indexed items must be 10 GB or less.

---

- Conditional writes and filtered reads
- Projection Expression - Used to retrieve only certain attributes in scan operation
- PartiQL
- Optimistic locking
- Capacity Modes - Provisioned - RCU, WCU and On Demand
- What is table throttling?
- Hot partition? And fix hot partition with exponential backoff.

---

Streams:

- A DynamoDB stream is an ordered flow of information about changes to items in an Amazon DynamoDB table.
- When you enable a stream on a table, DynamoDB captures information about every modification to data items in the table.
- A stream record contains information about a data modification to a single item in a DynamoDB table.
- StreamViewType => NEW_AND_OLD_IMAGES: before and after modification, NEW_IMAGE: after modification, OLD_IMAGE: before modification
- All data in DynamoDB Streams is subject to a 24-hour lifetime.

---

Cognito:

- Identity pool - Temporary credentials for unathenticated users/guest users/ user using 3rd party sign in option such as facebook or amazon or google or also use cognito user pool - to use AWS Services
- User pool - User directory - sign up & sign in
- Federated Indentity Pools
- Cognito sync - Cross device syncing

Cognito tokens:

1. Identity token - Authetication of requests
2. Access token - To define access of particular users to application based on roles???
3. Refresh token - Get new identity and access token after some definite time

- Identity, Access and refresh tokens are JWT Tokens

AWS Cognito - User Authentication :

- Manage user pools - Creates a pool of users and stores it in authentication database
- Manage federated identities - Use third party platforms like Facebook or Google for authentication
- You can use AWS Cognito user pool OR authentication can also be done using custom authorizers which are lambda functions to protect the API gateways.
- You can use codepen playground to test the backend from frontend while development.
