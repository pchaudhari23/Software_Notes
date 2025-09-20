Distributed in memory cache:

- Redis, Memcached
- Store data in cache (primary memory or in processor memory) so that when application need the data it can be fetched from cache instead of making a query to the db.
- This reduces the computation time and cost as databases store data in HDD or SSD and fetching data by query from secondary memory takes more time.
- Amazon ElastiCache for Redis, Memcached - Cluster of nodes.
- Redis is the only service in Elasticache that supports replication.
- Two types of nodes in redis - primary and replica nodes.
- Memcached - Low latency, multi threaded
- RR : Redis - Replication, MM : Memcached - Multithreading
- Cache hit and miss, cache invalidation - TTL
  Caching startegies:

1. Lazy loading: write data to cache only when cache miss.
2. Write through: Every time write operation is done, write to cache and database both. (You can use TTL to invalidate stale cache data).

---

Data Streaming:

- Shard: Smallest unit of throughput in Data stream of Kinesis Data Streams.
- Shard is made up of sequence of records.
- A shard supports 1 MB/second and 1,000 records per second for writes and 2 MB/second for reads.
- Record is made up of 3 things:

1. Sequence number: Used to uniquely identify a record
2. Partition key: Used to segregate records into different shards
3. Data blob: Contains actual data of the record

- Kinesis capacity modes - Number of shards in a data stream.

1. Provisioned mode: Specify the number of shards beforehand.
2. On demand mode: No need to specify.

---

Content Delivery Network:

- Distributed file system cache.
- If user is located far away from origin server, he will experience latency on making request.
- Hence there is a group of CDN servers all around the world (at different Points of presence).
- Eg: Cloudflare - Provides CDN, DNS and VPN services.
- User might be far from origin server but he will be closer to any one CDN server hence the load time is reduced.
- On making request if static assets and resources of website are not available in local cache of CDN server, it is fetched from origin server and stored in the cache and served to the user.
- Caching policies:

1. FIFO
2. LRU
3. LFU - Least Frequently Used

---

Microservices:

- Break the application into small components based on the feature.
- Eg: In an e-commerce application: User authentication, Shopping cart, Payments, Products catalog etc
- Services are loosely coupled, autonomously developed and deployed.
- Different teams can work on different components and also use different tech stacks for different components.
- The services interact with each other with the help of API calls.
- Unlike monolithic architecture which is large and tighly coupled and slow to change, any change made in microservice is released fast.
- Making changes to one component does not break the other components. Also the complete application does not need to be redeployed.
- Microservices usually use containers.

---

Distributed system:

- Collection of separate and independent software/hardware components, called nodes, that are networked and work together coherently by coordinating and communicating through message passing or events, to fulfill one end goal.
- Nodes could be unstructured or highly structured, depending on the system requirements. And the complexities of the system are hidden to the end user, making the whole system appear as a single computer to it users.

---

CONTAINERS:

- Virtual Machines [Application, Dependencies, Guest OS] => Hypervisor => Infrastructure/Hardware
- Containers [Application, Dependencies] => Container Engine/Platform/Docker => Host OS => Infrastructure/Hardware
- Containers are lightweight.
- Application and its dependencies are packaged as a single unit called container and deployed on container platform. It makes them reusable.
- Multiple packages can be deployed on a container platform and all of them use the same OS and same hardware. Unlike VM which has a guest OS.
- Orchestration - Making automated tasks work with each other in a sequence.
- Container orchestration - Kubernetes - Automatically handle container deployment, scaling, availability etc.
- Microservices built using different technologies, different frameworks can be packaged as separate containers and those multiple containers can be deployed on single container platform.

---

WEB SERVER:

- Computer software installed on server hardware that serves HTTP requests.
- Apache HTTP server: Node
- Apache Tomcat: Java
- IIS (Internet Information Services): Microsoft .NET
- nginx
- WAMP server: PHP

---

STATIC WEBSITE:

- HTML, CSS, JS
- Web page may not necessarily be static. The page content might change by DOM updates.
- But the source code is same. The files used in website are same.

---

DYNAMIC WEBSITE:

- Web servers support server side scripting languages - Active Server Pages (ASP), Javascript (Node JS), PHP, Python, and Ruby.
- Web page is created in the server and then delivered to client. Server side rendering.
- Users see different content every time they use the application. Eg: YouTube

---

Lazy Loading:

- Don't load the complete assets of the webpage such as images beforehand, just load the necessary data required to display the page.
- Load the static assets when it is required. Be "lazy" while loading the page, do only what is necessary.
- Lazy loading is also used in caching. The data is filled in cache only when it is required avoiding unnecessary filling of data that is not requested.

---

HTTP API vs REST API:

- HTTP API is an API which uses HTTP protocol but REST API can use any protocol such as HTTP, FTP etc.
- REST : REpresentational State Transfer. All operations in REST API are stateless.
- REST API works in Client-Server architecture. Client state is stored in session and cookies of web browser.

---

Software Artifact:

- A software artifact is a by-product produced during the software development process. It may consist of the project source code, dependencies, binaries or resources.
- Artifacts are stored in an artifact repository.

1. Code artifact: Compiled code, setup scripts, test suites, generated objects and logs generated during testing.
2. Build artifact: Output of a build which can be an exe or tar or bin etc.
3. Project artifact: Minimum required standards, benchmarks, project vision statements, roadmaps, change logs, scope management plans and quality plans.
4. Documentation artifact: Relevant documents, including diagrams, end-user agreements, internal documentation or written guides.

---
