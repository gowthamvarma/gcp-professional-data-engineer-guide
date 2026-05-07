# PDE Practice Quiz #9 - May 2026

### 1. You are administering shared BigQuery datasets that contain views used by multiple teams in
your organization. The marketing team is concerned about the variability of their monthly
BigQuery analytics spend using the on-demand billing model. You need to help the marketing
team establish a consistent BigQuery analytics spend each month. What should you do?
**Options:**
- Create a BigQuery Standard pay-as-you go reservation with a baseline of 0 slots and
autoscaling set to 500 for the marketing team, and bill them back accordingly.
- Create a BigQuery reservation with a baseline of 500 slots with no autoscaling for the
marketing team, and bill them back accordingly.
- Establish a BigQuery quota for the marketing team, and limit the maximum number of bytes
scanned each day.
- Create a BigQuery Enterprise reservation with a baseline of 250 slots and autoscaling set to
500 for the marketing team, and bill them back accordingly.

**Correct Answer:** B
**Explanation:** To help the marketing team establish a consistent BigQuery analytics spend each month, you can
use BigQuery reservations to allocate dedicated slots for their queries. This provides predictable
costs by reserving a ﬁxed amount of compute resources.
BigQuery Reservations:
BigQuery Reservations allow you to purchase dedicated query processing capacity in the form of
slots.
By reserving slots, you can control costs and ensure that the marketing team has the necessary
resources for their queries without unexpected increases in spending.
Baseline Slots:
Setting a baseline of 500 slots without autoscaling ensures a consistent allocation of resources.
This provides a predictable monthly cost, as the marketing team will be billed for the reserved
slots regardless of actual usage.

Billing Back:
The marketing team's usage can be billed back based on the ﬁxed reservation cost, ensuring
budget predictability.
This approach avoids the variability associated with on-demand billing, where costs can ﬂuctuate
based on query volume and complexity.
No Autoscaling:
By not enabling autoscaling, you prevent additional costs from being incurred due to temporary
increases in query demand.
This ﬁxed reservation ensures that the marketing team only uses the allocated 500 slots,
maintaining a consistent monthly spend.
Google Data Engineer

---

### 2. You migrated your on-premises Apache Hadoop Distributed File System (HDFS) data lake to
Cloud Storage. The data scientist team needs to process the data by using Apache Spark and
SQL. Security policies need to be enforced at the column level. You need a cost-eﬀective solution
that can scale into a data mesh. What should you do?
**Options:**
- 1. Deploy a long-living Dalaproc cluster with Apache Hive and Ranger enabled.
2. Conﬁgure Ranger for column level security.
3. Process with Dataproc Spark or Hive SQL.
- 1. Deﬁne a BigLake table.
2. Create a taxonomy of policy tags in Data Catalog.
3. Add policy lags to columns.
4. Process with the Spark-BigQuery connector or BigQuery SOL.
- 1. Load the data to BigQuery tables.
2. Create a taxonomy of policy tags in Data Catalog.
3. Add policy tags to columns.
4. Procoss with the Spark-BigQuery connector or BigQuery SQL.
- 1 Apply an Identity and Access Management (IAM) policy at the ﬁle level in Cloud Storage
2. Deﬁne a BigQuery external table for SQL processing.
3. Use Dataproc Spark to process the Cloud Storage ﬁles.

**Correct Answer:** D
**Explanation:** For automating the CI/CD pipeline of DAGs running in Cloud Composer, the following approach
ensures that DAGs are tested and deployed in a streamlined and eﬃcient manner.
Use Cloud Build for Development Instance Testing:
Use Cloud Build to automate the process of copying the DAG code to the Cloud Storage bucket of
the development instance.
This triggers Cloud Composer to automatically pick up and test the new DAGs in the development
environment.
Testing and Validation:
Ensure that the DAGs run successfully in the development environment.
Validate the functionality and correctness of the DAGs before promoting them to production.
Deploy to Production:
If the DAGs pass all tests in the development environment, use Cloud Build to copy the tested
DAG code to the Cloud Storage bucket of the production instance.
This ensures that only validated and tested DAGs are deployed to production, maintaining the
stability and reliability of the production environment.
Simplicity and Reliability:
This approach leverages Cloud Build's capabilities for automation and integrates seamlessly with
Cloud Composer's reliance on Cloud Storage for DAG storage.
By using Cloud Storage for both development and production deployments, the process remains
simple and robust.
Google Data Engineer

---

### 3. You are creating the CI'CD cycle for the code of the directed acyclic graphs (DAGs) running in
Cloud Composer. Your team has two Cloud Composer instances: one instance for development
and another instance for production. Your team is using a Git repository to maintain and develop
the code of the DAGs. You want to deploy the DAGs automatically to Cloud Composer when a
certain tag is pushed to the Git repository. What should you do?
**Options:**
- 1. Use Cloud Build to build a container and the Kubemetes Pod Operator to deploy the code of
the DAG to the Google Kubernetes
Engine (GKE) cluster of the development instance for testing.
2. If the tests pass, copy the code to the Cloud Storage bucket of the production instance.
- 1 Use Cloud Build to copy the code of the DAG to the Cloud Storage bucket of the development
instance for DAG testing.
2. If the tests pass, use Cloud Build to build a container with the code of the DAG and the
KubernetesPodOperator to deploy the container to the Google Kubernetes Engine (GKE) cluster of
the production instance.
- 1 Use Cloud Build to build a container with the code of the DAG and the
KubernetesPodOperator to deploy the code to the Google Kubernetes Engine (GKE) cluster of the
development instance for testing.
2. If the tests pass, use the KubernetesPodOperator to deploy the container to the GKE cluster of
the production instance.
- 1 Use Cloud Build to copy the code of the DAG to the Cloud Storage bucket of the
development instance for DAG testing.
2. If the tests pass, use Cloud Build to copy the code to the bucket of the production instance.

**Correct Answer:** C

---

### 4. You need to connect multiple applications with dynamic public IP addresses to a Cloud SQL
instance. You conﬁgured users with strong passwords and enforced the SSL connection to your
Cloud SOL instance. You want to use Cloud SQL public IP and ensure that you have secured
connections. What should you do?
**Options:**
- Add all application networks to Authorized Network and regularly update them.
- Add CIDR 0.0.0.0/0 network to Authorized Network. Use Identity and Access Management
(1AM) to add users.
- Leave the Authorized Network empty. Use Cloud SQL Auth proxy on all applications.
- Add CIDR 0.0.0.0/0 network to Authorized Network. Use Cloud SOL Auth proxy on all
applications.

**Correct Answer:** C
**Explanation:** To securely connect multiple applications with dynamic public IP addresses to a Cloud SQL
instance using public IP, the Cloud SQL Auth proxy is the best solution. This proxy provides
secure, authorized connections to Cloud SQL instances without the need to conﬁgure authorized
networks or deal with IP whitelisting complexities.
Cloud SQL Auth Proxy:
The Cloud SQL Auth proxy provides secure, encrypted connections to Cloud SQL.
It uses IAM permissions and SSL to authenticate and encrypt the connection, ensuring data
security in transit.
By using the proxy, you avoid the need to constantly update authorized networks as the proxy
handles dynamic IP addresses seamlessly.
Authorized Network Conﬁguration:

Leaving the authorized network empty means no IP addresses are explicitly whitelisted, relying
solely on the Auth proxy for secure connections.
This approach simpliﬁes network management and enhances security by not exposing the Cloud
SQL instance to public IP ranges.
Dynamic IP Handling:
Applications with dynamic IP addresses can securely connect through the proxy without the need
to modify authorized networks.
The proxy authenticates connections using IAM, making it ideal for environments where
application IPs change frequently.
Google Data Engineer

---

### 5. Your infrastructure team has set up an interconnect link between Google Cloud and the on-
premises network. You are designing a high-throughput streaming pipeline to ingest data in
streaming from an Apache Kafka cluster hosted on-premises. You want to store the data in
BigQuery, with as minima! latency as possible. What should you do?
**Options:**
- Use a proxy host in the VPC in Google Cloud connecting to Kafka. Write a Dataﬂow pipeline,
read data from the proxy host, and write the data to BigQuery.
- Setup a Kafka Connect bridge between Kafka and Pub/Sub. Use a Google-provided Dataﬂow
template to read the data from Pub/Sub, and write the data to BigQuery.
- Setup a Kafka Connect bridge between Kafka and Pub/Sub. Write a Dataﬂow pipeline, read the
data from Pub/Sub, and write the data to
BigQuery.
- Use Dataﬂow, write a pipeline that reads the data from Kafka, and writes the data to BigQuery.

**Correct Answer:** C
**Explanation:** Here's a detailed breakdown of why this solution is optimal and why others fall short:
Why Option C is the Best Solution:
Kafka Connect Bridge: This bridge acts as a reliable and scalable conduit between your on-
premises Kafka cluster and Google Cloud's Pub/Sub messaging service. It handles the
complexities of securely transferring data over the interconnect link.
Pub/Sub as a Buﬀer: Pub/Sub serves as a highly scalable buﬀer, decoupling the Kafka producer
from the Dataﬂow consumer. This is crucial for handling ﬂuctuations in message volume and
ensuring smooth data ﬂow even during spikes.
Custom Dataﬂow Pipeline: Writing a custom Dataﬂow pipeline gives you the ﬂexibility to
implement any necessary transformations or enrichments to the data before it's written to
BigQuery. This is often required in real-world streaming scenarios.
Minimal Latency: By using Pub/Sub as a buﬀer and Dataﬂow for eﬃcient processing, you
minimize the latency between the data being produced in Kafka and being available for querying
in BigQuery.
Why Other Options Are Not Ideal:
Option A: Using a proxy host introduces an additional point of failure and can create a bottleneck,
especially with high-throughput streaming.
Option B: While Google-provided Dataﬂow templates can be helpful, they might lack the
customization needed for speciﬁc transformations or handling complex data structures.
Option D: Dataﬂow doesn't natively connect to on-premises Kafka clusters. Directly reading from
Kafka would require complex networking conﬁgurations and could lead to performance issues.
Additional Considerations:
Schema Management: Ensure that the schema of the data being produced in Kafka is compatible
with the schema expected in BigQuery. Consider using tools like Schema Registry for schema
evolution management.
Monitoring: Set up robust monitoring and alerting to detect any issues in the pipeline, such as
message backlogs or processing errors.
By following Option C, you leverage the strengths of Kafka Connect, Pub/Sub, and Dataﬂow to
create a high-throughput, low-latency streaming pipeline that seamlessly integrates your on-
premises Kafka data with BigQuery.

---

### 6. You work for a farming company. You have one BigQuery table named sensors, which is about
500 MB and contains the list of your 5000 sensors, with columns for id, name, and location. This
table is updated every hour. Each sensor generates one metric every 30 seconds along with a
timestamp. which you want to store in BigQuery. You want to run an analytical query on the data
once a week for monitoring purposes. You also want to minimize costs. What data model should
you use?
**Options:**
- 1. Create a retries column in the sensor? table.
2. Set record type and repeated mode for the metrics column.
3. Use an UPDATE statement every 30 seconds to add new metrics.
- 1. Create a metrics column in the sensors table.
2. Set RECORD type and REPEATED mode for the metrics column.
3. Use an INSERT statement every 30 seconds to add new metrics.
- 1. Create a metrics table partitioned by timestamp.
2. Create a sensorld column in the metrics table, that points to the id column in the sensors table.
3. Use an IHSEW statement every 30 seconds to append new metrics to the metrics table.
4. Join the two tables, if needed, when running the analytical query.
- 1. Create a metrics table partitioned by timestamp.
2. Create a sensor Id column in the metrics table, that points to the _d column in the sensors
table.
3. Use an UPDATE statement every 30 seconds to append new metrics to the metrics table.
4. Join the two tables, if needed, when running the analytical query.

**Correct Answer:** C
**Explanation:** For a farming company with a sensor data table updated every 30 seconds, the goal is to
minimize costs while facilitating weekly analytical queries. The best data model will eﬀectively
manage data storage, update frequency, and query performance.
Partitioned Metrics Table:
Creating a metrics table partitioned by timestamp optimizes query performance and storage

costs.
Partitioning by timestamp allows for eﬃcient querying, especially for time-based analyses.
Sensor ID

---

### 7. You have thousands of Apache Spark jobs running in your on-premises Apache Hadoop cluster.
You want to migrate the jobs to Google Cloud. You want to use managed services to run your jobs
instead of maintaining a long-lived Hadoop cluster yourself. You have a tight timeline and want to
keep code changes to a minimum. What should you do?
**Options:**
- Copy your data to Compute Engine disks. Manage and run your jobs directly on those
instances.
- Move your data to Cloud Storage. Run your jobs on Dataproc.
- Move your data to BigQuery. Convert your Spark scripts to a SQL-based processing approach.
- Rewrite your jobs in Apache Beam. Run your jobs in Dataﬂow.

**Correct Answer:** B
**Explanation:** Dataproc's Compatibility with Apache Spark: Dataproc is a managed service for running Hadoop
and Spark clusters on Google Cloud. This means it is designed to seamlessly run Apache Spark
jobs with minimal code changes. Your existing Spark jobs should run on Dataproc with little to no
modiﬁcation.
Cloud Storage as a Scalable Data Lake: Cloud Storage provides a highly scalable and durable
storage solution for your data. It's designed to handle large volumes of data that Spark jobs
typically process.
Minimizing Operational Overhead: By using Dataproc, you eliminate the need to manage and
maintain a Hadoop cluster yourself. Google Cloud handles the infrastructure, allowing you to
focus on your data processing tasks.
Tight Timeline and Minimal Code Changes: This option directly addresses the requirements of the
question. It oﬀers a quick and easy way to migrate your Spark jobs to Google Cloud with minimal
disruption to your existing codebase.
Why other options are not suitable:
A . Copy your data to Compute Engine disks. Manage and run your jobs directly on those
instances: This option requires you to manage the underlying infrastructure yourself, which
contradicts the requirement of using managed services.
C . Move your data to BigQuery. Convert your Spark scripts to a SQL-based processing approach:
While BigQuery is a powerful data warehouse, converting Spark scripts to SQL would require
substantial code changes and might not be feasible within a tight timeline.
D . Rewrite your jobs in Apache Beam. Run your jobs in Dataﬂow: Rewriting jobs in Apache Beam
would be a signiﬁcant undertaking and not suitable for a quick migration with minimal code
changes.

Engineer Visit
a-engineer
ata-engineer

---

