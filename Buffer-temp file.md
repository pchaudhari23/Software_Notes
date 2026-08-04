Tools, Platform, AI

Graphic Design: Canva

UI/UX Design: Figma

E-commerce: Shopify, Magento

ERP: SAP, Odoo

CRM: Salesforce

CMS: WordPress, Joomla, Drupal, DNN

Website builder: Wix

Hosting/ infrastructure: Hostinger, GoDaddy, Cloudflare

Stock images: Unsplash, Getty images, Pexels, Pixabay, Shutter stock, freepik, iStock

HRMS & Payroll softwares

Office productivity suite - Google Workspace, Microsoft 365, LibreOffice, Apple iWork, WPS, Zoho

Project management: JIRA

Note-taking: Notion, Evernote, Obsidian

Notes analysis: Turbo AI

TOOLS:

Website builder

E-commerce platforms

Business platforms/ ERP

CMS

CRM

Hosting/infrastructure

Automation & Integration

App builder

Digital skills:

UI/ UX, Web design

Graphic design

Digital marketing

Video editing

Data & automation

Copywriting & Content writing

AI influencer

Use case:

If mostly content - need a website - use website builder

If mostly logic - need a product - use front-end development frameworks (Angular, React, etc.)

Notes:

Builders - Used to do repetitive, low-value work.

No code => Low code => Full code

CMS: Static content - Hosted on CDN

---

Tools to interact with remote VM: (Add a section in lab handson - VM)

1. DBeaver
2. WinSCP (Uses port 22 to run SFTP protocol)
3. NoMachine client (Uses port 4000 to run NX protocol)
4. Termius - CLI based SSH client for connecting to VM
5. Filezilla - search in all repo and remove where not required.

Add - ways to access a vm from your system. You need - 1. VM IP, 2. VM Username, 3. VM Password. Also port number on which application is running. For DBeaver and NoMachine/WinSCP connection.

---

How to make github copilot in vs code access bitbucket PR and JIRA?

How to connect various plugins to llms?

Explore all the AI options in VS Code?

---

AWS Serverless: Prepare for interviews! And make section in lab notes

Typical setup:

Client => API Gateway => Lambda function => DynamoDB. Auth using Cognito, Storage in S3, Domain with Route53

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

Explore AWS Amplify and SAM for serverless!!

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
