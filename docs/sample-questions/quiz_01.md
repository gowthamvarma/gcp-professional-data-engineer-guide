# PDE Practice Quiz #1 - May 2026

### 1. You have a transactional database (Cloud SQL) and a data warehouse (BigQuery). How should you architect a solution for joined reporting on historical and active data?
**Options:**
- Migrate all active transactional data into BigQuery every 5 seconds.
- Use BigQuery Cloud SQL Federated Queries to join historical BigQuery data with live Cloud SQL data.
- Move all historical data back into Cloud SQL to ensure consistency.
- Perform the join manually in a Google Sheet.

**Correct Answer:** Use BigQuery Cloud SQL Federated Queries to join historical BigQuery data with live Cloud SQL data.
**Explanation:** Federated queries allow BigQuery to query data residing in Cloud SQL in real-time, enabling joins between historical warehouse data and live transactional data without moving it.

---

### 2. A Pub/Sub subscriber is failing to process a specific message repeatedly. Which feature prevents this 'poison pill' from blocking the queue indefinitely?
**Options:**
- Flow Control
- Exactly-once delivery
- Dead Letter Topics
- Filtering

**Correct Answer:** Dead Letter Topics
**Explanation:** Dead Letter Topics allow Pub/Sub to move messages that cannot be processed after a certain number of attempts to a separate topic for debugging.

---

### 3. You want to prevent a file in Cloud Storage from being deleted for a period of 5 years to meet regulatory compliance. Which feature should you use?
**Options:**
- Soft Delete
- Retention Policy with Retention Lock
- Object Versioning
- Lifecycle Management delete rule

**Correct Answer:** Retention Policy with Retention Lock
**Explanation:** A Retention Policy defines how long objects must be kept, and a Retention Lock prevents the policy from being removed or shortened, even by administrators.

---

### 4. In Dataflow, what is the primary purpose of a 'Watermark' in a streaming context?
**Options:**
- To measure the physical data volume in the pipeline.
- To track the pipeline's notion of progress relative to event time.
- To act as a unique identifier for deduplication.
- To trigger an immediate shutdown if latency exceeds a threshold.

**Correct Answer:** To track the pipeline's notion of progress relative to event time.
**Explanation:** Watermarks are the system's way of estimating how complete the data is for a given event-time window, helping handle late-arriving data.

---

### 5. What is a benefit of using 'Nested and Repeated' fields in BigQuery compared to traditional table joins?
**Options:**
- It allows for 3rd Normal Form compliance.
- It reduces data duplication while maintaining high query performance through localized data storage.
- It is the only way to store JSON data.
- It automatically encrypts the columns at the application level.

**Correct Answer:** It reduces data duplication while maintaining high query performance through localized data storage.
**Explanation:** Nested and repeated fields allow you to represent one-to-many relationships within a single row, avoiding the compute-heavy shuffle required by standard SQL joins.

---

### 6. When defining a partitioned table based on a TIMESTAMP column, what is the maximum number of partitions allowed per table?
**Options:**
- 1,000
- 4,000
- 10,000
- Unlimited

**Correct Answer:** 10,000
**Explanation:** BigQuery currently enforces a limit of 10,000 partitions per table to ensure performance and manageability.

---

### 7. If you cluster a table by 'customer_id' and 'order_date', in what order should you place the columns in the CLUSTER BY clause to optimize queries filtering by 'order_date' only?
**Options:**
- The order does not matter.
- Put 'order_date' first.
- Put 'customer_id' first.
- Both columns must be used in the query for clustering to work.

**Correct Answer:** Put 'order_date' first.
**Explanation:** The order of clustered columns determines the sort priority; queries filtering by the first clustered column are more efficient than those filtering only by subsequent ones.

---

### 8. Which statement about BigQuery clustering is TRUE?
**Options:**
- Clustering automatically re-sorts data in the background at no additional cost.
- You must manually run a RECLUSTER command every week.
- Clustering is only effective on tables smaller than 1GB.
- Clustering requires you to define a range of values manually.

**Correct Answer:** Clustering automatically re-sorts data in the background at no additional cost.
**Explanation:** BigQuery performs automatic re-clustering in the background as new data is added to maintain the performance of the table without user intervention.

---

### 9. You need to move 500 TB of data from an AWS S3 bucket to a Google Cloud Storage bucket. Which service is designed to automate and manage this large-scale transfer without requiring you to set up your own transfer appliances?
**Options:**
- Storage Transfer Service
- Transfer Appliance
- gsutil rsync
- Compute Engine with custom scripts

**Correct Answer:** Storage Transfer Service
**Explanation:** Storage Transfer Service allows you to quickly import online data from other cloud providers or HTTP/HTTPS locations into Google Cloud Storage.

---

### 10. You must ensure that once an object is uploaded to a bucket, it cannot be deleted or overwritten by anyone—including the project owner—for a period of 5 years to meet compliance requirements. What should you use?
**Options:**
- IAM Roles only
- Bucket Lock with a Retention Policy
- Object Versioning
- Customer-Managed Encryption Keys (CMEK)

**Correct Answer:** Bucket Lock with a Retention Policy
**Explanation:** Bucket Lock allows you to configure a data retention policy for a Cloud Storage bucket that governs how long objects in the bucket must be retained; once locked, the policy cannot be removed or shortened.

---

### 11. To provide a user temporary access to a specific private object in a bucket without requiring them to have a Google account, which mechanism is best?
**Options:**
- Signed URLs
- Public Access Prevention
- Identity-Aware Proxy (IAP)
- Uniform Bucket-Level Access

**Correct Answer:** Signed URLs
**Explanation:** Signed URLs give time-limited read or write access to anyone in possession of the URL, regardless of whether they have a Google account.

---

### 12. Within Dataplex, what is the logical container used to group data into functional sets, such as 'Sales' or 'Finance'?
**Options:**
- Asset
- Lake
- Zone
- Bucket

**Correct Answer:** Lake
**Explanation:** A 'Lake' is the highest-level logical container in Dataplex, usually representing a specific domain or department's data environment.

---

### 13. What happens when Dataplex 'Discovery' is enabled on a zone containing Cloud Storage buckets with Parquet files?
**Options:**
- The files are moved to BigQuery storage automatically.
- Dataplex scans the files, infers the schema, and automatically creates tables in the Dataplex metadata catalog and BigQuery.
- The files are converted to CSV for easier reading.
- The files are deleted if they do not match the zone's governance policy.

**Correct Answer:** Dataplex scans the files, infers the schema, and automatically creates tables in the Dataplex metadata catalog and BigQuery.
**Explanation:** Dataplex Discovery automatically identifies structured and semi-structured data in GCS and registers it as tables in the metadata store.

---

### 14. When using MySQL as a source for Datastream, which global variable must be set to 'ON' to allow for Change Data Capture?
**Options:**
- innodb_buffer_pool_size
- log_bin
- max_connections
- query_cache_type

**Correct Answer:** log_bin
**Explanation:** The 'log_bin' variable enables binary logging, which is required for Datastream to read the transaction logs and capture changes from a MySQL database.

---

### 15. In the context of Datastream, what is a 'Connection Profile'?
**Options:**
- A user profile for logging into the Google Cloud Console
- A reusable configuration containing the credentials and connection details for a source or destination
- A billing report showing the cost of a specific stream
- A firewall rule set for the VPC

**Correct Answer:** A reusable configuration containing the credentials and connection details for a source or destination
**Explanation:** Connection Profiles store the hostname, port, and authentication credentials for databases or storage buckets, allowing them to be reused across multiple streams.

---

### 16. When monitoring a Datastream stream, what does the 'System Lag' metric represent?
**Options:**
- The time since the last source database backup
- The time difference between when a change happened at the source and when it was processed by Datastream
- The physical distance between the data centers
- The latency of the Google Cloud Console UI

**Correct Answer:** The time difference between when a change happened at the source and when it was processed by Datastream
**Explanation:** System lag is a critical performance indicator showing how 'real-time' the replication is by measuring the delay in processing captured changes.

---

### 17. You are scaling a subscriber that uses 'Pull'. You notice many 'duplicate' messages even though the application is processing them within 10 seconds. What is the likely cause?
**Options:**
- The topic has multiple publishers.
- The Acknowledgment Deadline on the subscription is set too low (e.g., default 10s).
- The subscriber is not using an ordering key.
- The 'Message Retention' is too long.

**Correct Answer:** The Acknowledgment Deadline on the subscription is set too low (e.g., default 10s).
**Explanation:** If the processing time is close to or exceeds the Acknowledgment Deadline, Pub/Sub will redeliver the message before the first instance can finish and ACK it.

---

### 18. A Data Engineer needs to replay messages from a Pub/Sub subscription that were already acknowledged 2 hours ago. Which feature allows this?
**Options:**
- Snapshot and Seek
- Exactly Once Delivery
- Dead Letter Topic
- Message Storage Policy

**Correct Answer:** Snapshot and Seek
**Explanation:** The 'Seek' feature allows you to reset a subscription's state to a previous point in time or a snapshot, effectively allowing message replay.

---

### 19. When configuring a Pub/Sub topic for cross-project access, which IAM role should be granted to the Service Account of the subscriber in the 'publisher' project?
**Options:**
- roles/pubsub.publisher
- roles/pubsub.subscriber
- roles/pubsub.admin
- roles/pubsub.viewer

**Correct Answer:** roles/pubsub.subscriber
**Explanation:** To consume messages from a subscription in a different project, the identity needs the 'Subscriber' role on that specific subscription or the parent topic.

---

### 20. When using a BigQuery subscription, what happens if the schema of the incoming Pub/Sub message does not match the schema of the destination BigQuery table?
**Options:**
- The message is automatically dropped to prevent table corruption.
- The subscription is paused until the schemas are manually aligned.
- The message is sent to a dead-letter topic if one is configured; otherwise, it remains in the subscription.
- BigQuery creates a new column on the fly to accommodate the unexpected data.

**Correct Answer:** The message is sent to a dead-letter topic if one is configured; otherwise, it remains in the subscription.
**Explanation:** Schema mismatches result in delivery failure. If a dead-letter topic is configured, the message is sent there; if not, Pub/Sub retries delivery, which can result in the message being stuck.
