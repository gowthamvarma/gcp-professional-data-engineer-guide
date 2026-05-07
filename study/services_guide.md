# GCP Professional Data Engineer - Study Guide 2026

This guide organizes key Google Cloud services and the specific concepts you need to master for the Professional Data Engineer exam.

---

## 1. Data Ingestion & Messaging

### **Pub/Sub**
*   **Description:** A global, asynchronous messaging service that decouples senders and receivers, ideal for real-time data streaming and event-driven architectures.
*   **Key Topics to Learn:**
    *   **Dead Letter Topics:** Handling messages that fail to be processed after multiple attempts.
    *   **Snapshot and Seek:** Replaying acknowledged messages or resetting subscription states.
    *   **Message Retention:** Configuring how long messages are kept (up to 31 days).
    *   **Ordering Keys:** Ensuring sequential delivery for messages with the same key.
    *   **Subscription Filtering:** Reducing costs by filtering messages service-side.
    *   **BigQuery Subscriptions:** Direct streaming from Pub/Sub to BigQuery without Dataflow.
*   **Documentation:** [Pub/Sub Documentation](https://cloud.google.com/pubsub/docs)

### **Datastream**
*   **Description:** A serverless change data capture (CDC) and replication service that synchronizes data across heterogeneous databases and storage systems.
*   **Key Topics to Learn:**
    *   **Change Data Capture (CDC):** Capturing row-level changes from MySQL, PostgreSQL, and Oracle.
    *   **Connection Profiles:** Reusable configurations for source and destination credentials.
    *   **Backfill vs. Streaming:** Understanding initial data load vs. ongoing change capture.
    *   **Private Connectivity:** Setting up VPC peering for secure database access.
*   **Documentation:** [Datastream Documentation](https://cloud.google.com/datastream/docs)

### **Storage Transfer Service**
*   **Description:** A managed service for moving large volumes of data from other cloud providers, online locations, or on-premises storage to Cloud Storage.
*   **Key Topics to Learn:**
    *   **Large-scale Migration:** Moving PBs of data from AWS S3, Azure Blob, or HTTP locations.
    *   **Scheduling:** Setting up periodic transfer jobs.
    *   **Filtering:** Including/Excluding objects based on prefixes or modification times.
*   **Documentation:** [Storage Transfer Service Documentation](https://cloud.google.com/storage-transfer/docs)

---

## 2. Data Storage & Warehousing

### **BigQuery**
*   **Description:** A fully managed, serverless enterprise data warehouse that enables scalable, cost-effective analysis over petabytes of data using SQL.
*   **Key Topics to Learn:**
    *   **Partitioning & Clustering:** Optimizing query performance and reducing costs.
    *   **BigLake:** Querying data in GCS, AWS, or Azure as if it were local BigQuery tables.
    *   **Nested and Repeated Fields:** Using Structs and Arrays to avoid expensive joins.
    *   **Materialized Views:** Speeding up aggregate queries with automatic refresh.
    *   **Authorized Views/Datasets:** Controlling access to specific rows/columns.
    *   **BigQuery ML:** Training and running models (Linear/Logistic, K-means, Time-series) using SQL.
*   **Documentation:** [BigQuery Documentation](https://cloud.google.com/bigquery/docs)

### **Cloud Storage (GCS)**
*   **Description:** A highly durable and available object storage service for unstructured data, serving as the foundation for data lakes on Google Cloud.
*   **Key Topics to Learn:**
    *   **Retention Policies & Bucket Lock:** Meeting regulatory compliance (WORM).
    *   **Lifecycle Management:** Automatically moving data to cheaper storage classes (Nearline, Coldline, Archive).
    *   **Object Versioning:** Recovering from accidental deletions or overwrites.
    *   **Signed URLs:** Providing temporary, account-less access to private objects.
*   **Documentation:** [Cloud Storage Documentation](https://cloud.google.com/storage/docs)

### **Cloud Bigtable**
*   **Description:** A high-performance, fully managed NoSQL database service designed for large-scale operational and analytical workloads with sub-10ms latency.
*   **Key Topics to Learn:**
    *   **Row Key Design:** Avoiding "hotspots" and ensuring even distribution of data.
    *   **Garbage Collection Policies:** Managing data retention at the cell level.
    *   **Replication:** Configuring Multi-cluster routing for high availability.
*   **Documentation:** [Cloud Bigtable Documentation](https://cloud.google.com/bigtable/docs)

### **Lakehouse Architecture (BigLake)**
*   **Description:** A storage engine that unifies data lakes and warehouses by allowing BigQuery to query data in open formats across multi-cloud storage with consistent security.
*   **Key Topics to Learn:**
    *   **Unified Storage:** Using BigLake to provide a consistent management layer over GCS (Parquet/Avro), AWS S3, and Azure Data Lake.
    *   **Fine-grained Access Control:** Applying row-level and column-level security across different storage backends.
    *   **Performance Optimization:** Leveraging metadata caching and file-level statistics.
*   **Documentation:** [BigLake Introduction](https://cloud.google.com/bigquery/docs/biglake-intro)

---

## 3. Data Processing & Transformation

### **Dataflow (Apache Beam)**
*   **Description:** A unified stream and batch data processing service that provides high-throughput, low-latency execution for large-scale data pipelines.
*   **Key Topics to Learn:**
    *   **Windowing:** Fixed, Sliding, and Session windows for streaming data.
    *   **Watermarks:** Tracking progress relative to event time and handling late data.
    *   **Side Inputs:** Injecting slowly-changing lookup data into a processing stream.
    *   **Horizontal Autoscaling:** Dynamically scaling workers based on CPU and throughput.
    *   **Exactly-once Processing:** Ensuring data integrity during failures and retries.
*   **Documentation:** [Dataflow Documentation](https://cloud.google.com/dataflow/docs)

### **Dataproc**
*   **Description:** A fully managed service for running Apache Spark, Flink, and Hadoop clusters in a cost-efficient and scalable manner.
*   **Key Topics to Learn:**
    *   **Ephemeral Clusters:** Running clusters only for the duration of a job to save costs.
    *   **Preemptible VMs:** Using secondary workers for non-critical, cost-sensitive processing.
    *   **Component Gateway:** Securely accessing web UIs like Spark History Server and Jupyter.
    *   **Workflow Templates:** Orchestrating a sequence of Spark/Hive jobs.
*   **Documentation:** [Dataproc Documentation](https://cloud.google.com/dataproc/docs)

### **Cloud Data Fusion**
*   **Description:** A cloud-native data integration service that provides a visual interface for building and managing ETL/ELT pipelines without writing code.
*   **Key Topics to Learn:**
    *   **Visual ETL/ELT:** Building pipelines using a low-code/no-code interface.
    *   **Wrangler:** Using the interactive UI for data cleaning and transformation.
    *   **CDC Replication:** Synchronizing operational databases (SQL Server, MySQL) with BigQuery in real-time.
    *   **Incremental Loads:** Fetching only new or changed records using timestamps or offsets.
*   **Documentation:** [Cloud Data Fusion Documentation](https://cloud.google.com/data-fusion/docs)

---

## 4. Orchestration & Governance

### **Cloud Composer (Apache Airflow)**
*   **Description:** A fully managed workflow orchestration service built on Apache Airflow, used to author, schedule, and monitor complex data pipelines.
*   **Key Topics to Learn:**
    *   **DAG Design:** Creating robust Directed Acyclic Graphs for complex workflows.
    *   **Operators:** Using specialized operators for BigQuery, Dataflow, and GCS.
    *   **XComs:** Passing small amounts of data between tasks.
    *   **Environment Scaling:** Adjusting worker counts and resource allocation.
*   **Documentation:** [Cloud Composer Documentation](https://cloud.google.com/composer/docs)

### **Dataplex (Knowledge Catalog)**
*   **Description:** An intelligent data fabric that enables unified governance, monitoring, and management of data across lakes, warehouses, and databases.
*   **Key Topics to Learn:**
    *   **Lakes & Zones:** Logically organizing data across GCS and BigQuery.
    *   **Data Discovery:** Automatically scanning and registering metadata.
    *   **Data Quality:** Running automated checks to ensure data integrity.
    *   **Attribute-based Access Control:** Managing permissions across the data mesh.
*   **Documentation:** [Dataplex Documentation](https://cloud.google.com/dataplex/docs)

---

## 5. Security & Machine Learning

### **IAM & Security**
*   **Description:** The core security framework for Google Cloud that manages identities and controls access to resources based on the principle of least privilege.
*   **Key Topics to Learn:**
    *   **Principle of Least Privilege:** Granting only necessary roles (e.g., `roles/bigquery.dataViewer`).
    *   **Service Accounts:** Providing secure identities for automated applications and pipelines.
    *   **Sensitive Data Protection (Cloud DLP):** Inspecting and masking PII.
*   **Documentation:** [IAM Documentation](https://cloud.google.com/iam/docs)

### **Vertex AI**
*   **Description:** A comprehensive machine learning platform that unifies AI workflows, allowing you to build, deploy, and scale ML models faster.
*   **Key Topics to Learn:**
    *   **Feature Store:** Managing and serving ML features at scale.
    *   **Model Registry:** Tracking model versions and lineage.
    *   **Pipelines:** Orchestrating end-to-end ML workflows using Kubeflow.
*   **Documentation:** [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
