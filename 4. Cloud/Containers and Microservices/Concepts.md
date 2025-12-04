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
