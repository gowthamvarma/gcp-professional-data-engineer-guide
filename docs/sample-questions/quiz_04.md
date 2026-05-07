# PDE Practice Quiz #4 - Dataproc, Data Fusion & Composer

### 1. You are running a cost-sensitive batch processing job on Dataproc that can tolerate interruptions. Which feature should you use to reduce costs?
**Options:**
- High-memory machine types
- Secondary workers (Preemptible VMs)
- Reservation of Slots
- Autoscaling with Primary workers only

**Correct Answer:** Secondary workers (Preemptible VMs)
**Explanation:** Preemptible VMs (Secondary workers) offer significant cost savings for Dataproc clusters, though they can be reclaimed by Google Cloud at any time.

---

### 2. Which component acts as the default storage layer for a cloud-native Dataproc implementation, replacing the need for a persistent HDFS on local disks?
**Options:**
- Persistent Disk
- Filestore
- Google Cloud Storage
- Local SSD

**Correct Answer:** Google Cloud Storage
**Explanation:** Google Cloud Storage (GCS) is used as the storage layer in a cloud-native architecture, allowing for the decoupling of storage and compute.

---

### 3. A company wants to migrate their Hive Metastore to Google Cloud to be shared across multiple Dataproc clusters. What is the recommended managed service for this?
**Options:**
- Dataplex
- Dataproc Metastore
- Cloud SQL
- Bigtable

**Correct Answer:** Dataproc Metastore
**Explanation:** Dataproc Metastore is a fully managed, highly available Hive Metastore (HMS) that simplifies metadata management for data lakes.

---

### 4. When migrating Spark jobs to Dataproc, you notice performance degradation. You suspect the bottleneck is the connection to GCS. What should you check first?
**Options:**
- The version of the GCS connector installed on the cluster.
- The VPC network throughput limits.
- Whether the GCS bucket is in a different region than the Dataproc cluster.
- The number of Primary workers in the cluster.

**Correct Answer:** Whether the GCS bucket is in a different region than the Dataproc cluster.
**Explanation:** Inter-regional data transfer introduces latency and egress costs; keeping the Dataproc cluster and the GCS bucket in the same region is critical for performance.

---

### 5. To customize the software environment of a Dataproc cluster (e.g., installing specific Python libraries) during creation, which mechanism should you use?
**Options:**
- SSH into the master node after creation
- Initialization actions
- Custom Images
- Both B and C are valid

**Correct Answer:** Both B and C are valid
**Explanation:** Both Initialization actions (scripts run during startup) and Custom Images (pre-built disk images) are used to customize the cluster environment.

---

### 6. You need to run a complex sequence of Dataproc jobs where the output of one job is the input for the next. Which Dataproc feature automates this?
**Options:**
- Job Grouping
- Workflow Templates
- Cloud Scheduler
- Init Actions

**Correct Answer:** Workflow Templates
**Explanation:** Workflow Templates provide a way to manage and execute a directed acyclic graph (DAG) of jobs on a cluster.

---

### 7. You want to monitor Dataproc cluster metrics like CPU utilization and HDFS capacity. Which Google Cloud service provides this out of the box?
**Options:**
- Cloud Logging
- Cloud Monitoring (formerly Stackdriver)
- Error Reporting
- Cloud Trace

**Correct Answer:** Cloud Monitoring (formerly Stackdriver)
**Explanation:** Cloud Monitoring automatically collects and displays metrics for Dataproc clusters and jobs.

---

### 8. In Dataproc, what happens to the data stored in the default HDFS on the cluster's local disks when the cluster is deleted?
**Options:**
- It is moved to a 'deleted' bucket in GCS.
- It is permanently lost.
- It is snapshotted to a Persistent Disk.
- It is kept for 30 days by default.

**Correct Answer:** It is permanently lost.
**Explanation:** HDFS in Dataproc is typically backed by local disks or PDs attached to the cluster; when the cluster is deleted, that local storage is also destroyed.

---

### 9. A financial services company needs to migrate data from an on-premises SQL Server to BigQuery using Cloud Data Fusion. The migration must handle incremental updates based on a 'last_modified' timestamp. Which plugin is best suited for this requirement?
**Options:**
- SQL Server Batch Source
- SQL Server Incremental Source
- Change Data Capture (CDC) Plugin
- Database Source with a custom SQL query

**Correct Answer:** SQL Server Incremental Source
**Explanation:** The SQL Server Incremental Source plugin is specifically designed to fetch records based on a monotonically increasing column or timestamp, making it ideal for standard incremental loads without full CDC overhead.

---

### 10. What is the primary underlying execution engine used by Cloud Data Fusion to process data pipelines?
**Options:**
- Apache Flink
- Apache Spark
- Google Cloud Dataflow
- BigQuery Query Engine

**Correct Answer:** Apache Spark
**Explanation:** Cloud Data Fusion pipelines are translated into Apache Spark programs that run on Cloud Dataproc clusters.

---

### 11. You are designing a pipeline that processes PII data. You need to mask social security numbers before the data reaches the sink. Which transform plugin should you use for a low-code approach?
**Options:**
- Wrangler
- Python Transform
- JavaScript Transform
- Group By

**Correct Answer:** Wrangler
**Explanation:** The Wrangler transform provides an interactive UI to apply directives like 'mask-number' or 'hash' to specific columns without writing code.

---

### 12. A retail company wants to synchronize their MySQL production database with BigQuery in near real-time. They choose the Cloud Data Fusion Replication feature. What is a key requirement for the source MySQL database?
**Options:**
- The database must be in 'read-only' mode.
- Binary logging (binlog) must be enabled with ROW format.
- A static IP must be assigned to the Data Fusion instance.
- The database must not exceed 100GB in size.

**Correct Answer:** Binary logging (binlog) must be enabled with ROW format.
**Explanation:** Data Fusion Replication uses Change Data Capture (CDC), which for MySQL requires the binary log to be enabled in ROW format to capture row-level changes.

---

### 13. A health organization needs to ensure that Data Fusion does not have access to the public internet. Which networking configuration is required?
**Options:**
- Public IP with Firewall rules.
- Private IP configuration with VPC Peering.
- Cloud NAT setup on the Dataproc cluster.
- Standard Edition with HTTPS enabled.

**Correct Answer:** Private IP configuration with VPC Peering.
**Explanation:** A Private IP instance of Cloud Data Fusion uses VPC Peering to communicate with your VPC and other Google services without exposing traffic to the public internet.

---

### 14. During a massive data migration, you notice the Data Fusion pipeline is running slowly. Which optimization would have the most direct impact on performance?
**Options:**
- Changing the Data Fusion UI theme.
- Increasing the number of workers in the Dataproc Compute Config.
- Using the 'Validator' transform more frequently.
- Reducing the number of fields in the source schema.

**Correct Answer:** Increasing the number of workers in the Dataproc Compute Config.
**Explanation:** Since Data Fusion runs on Dataproc, increasing worker nodes or upgrading machine types provides more CPU/RAM for the Spark engine to process data in parallel.

---

### 15. Case Study: An IoT company has data arriving in Pub/Sub and needs to process it with 10-second windows and sink it to BigQuery. What type of pipeline should they build in Data Fusion?
**Options:**
- Batch Pipeline
- Replication Pipeline
- Real-time Pipeline (Streaming)
- Micro-batch Pipeline

**Correct Answer:** Real-time Pipeline (Streaming)
**Explanation:** Real-time pipelines in Data Fusion use Spark Streaming, which is suitable for consuming data from Pub/Sub with windowing requirements.

---

### 16. Which Google Cloud service is Cloud Composer built upon to manage the underlying infrastructure for Airflow environments?
**Options:**
- Compute Engine
- Google Kubernetes Engine (GKE)
- App Engine
- Cloud Run

**Correct Answer:** Google Kubernetes Engine (GKE)
**Explanation:** Cloud Composer uses GKE to deploy and manage the various components of the Airflow architecture, such as the scheduler, workers, and web server.

---

### 17. When migrating DAGs to Cloud Composer, you notice tasks are failing due to 'Permission Denied' when accessing a BigQuery dataset. What is the most likely cause?
**Options:**
- The Cloud Composer Service Agent is missing the 'Browser' role
- The environment's service account lacks the necessary IAM roles for BigQuery
- BigQuery does not support Airflow operators in a managed environment
- The DAG file needs to be encrypted with a CMEK before execution

**Correct Answer:** The environment's service account lacks the necessary IAM roles for BigQuery
**Explanation:** Cloud Composer executes tasks using a specific service account; this account must be granted appropriate IAM roles (like BigQuery Data Editor) to interact with other GCP services.

---

### 18. You are migrating a very large Airflow deployment to Cloud Composer and want to minimize cross-region latency and costs. What is a best practice for the Cloud Storage bucket associated with the environment?
**Options:**
- Use a Multi-Regional bucket for high availability
- Place the bucket in the same region as the Cloud Composer environment
- Use a Coldline storage class to reduce DAG storage costs
- Manually create a bucket in a different project for security isolation

**Correct Answer:** Place the bucket in the same region as the Cloud Composer environment
**Explanation:** The environment's bucket should be in the same region as the environment itself to ensure low latency for DAG parsing and to avoid inter-regional data transfer costs.

---

### 19. If you need to trigger a Cloud Composer DAG from an external system via an API, which Google Cloud component provides the endpoint?
**Options:**
- The Cloud Pub/Sub topic
- The Airflow Web Server
- The Cloud Functions trigger
- The IAP-protected Airflow REST API

**Correct Answer:** The IAP-protected Airflow REST API
**Explanation:** Cloud Composer environments expose the Airflow REST API, which is protected by Identity-Aware Proxy (IAP) and can be used to trigger DAGs programmatically.

---

### 20. What happens to the existing DAG runs and task history if you delete a Cloud Composer environment but keep the Cloud Storage bucket?
**Options:**
- History is preserved in the bucket's metadata
- History is lost because it is stored in the managed metadata database
- History is automatically migrated to a new environment
- History is stored in Cloud Logging indefinitely

**Correct Answer:** History is lost because it is stored in the managed metadata database
**Explanation:** The execution history is stored in the Cloud SQL metadata database, which is deleted along with the environment. The bucket only contains DAG files, logs, and plugins.
