# PDE Practice Quiz #7 - May 2026

### 1. You are migrating a large number of ﬁles from a public HTTPS endpoint to Cloud Storage. The
ﬁles are protected from unauthorized access using signed URLs. You created a TSV ﬁle that
contains the list of object URLs and started a transfer job by using Storage Transfer Service. You
notice that the job has run for a long time and eventually failed Checking the logs of the transfer
job reveals that the job was running ﬁne until one point, and then it failed due to HTTP 403 errors
on the remaining ﬁles You veriﬁed that there were no changes to the source system You need to
ﬁx the problem to resume the migration process. What should you do?
**Options:**
- Set up Cloud Storage FUSE, and mount the Cloud Storage bucket on a Compute Engine
Instance Remove the completed ﬁles from the TSV ﬁle Use a shell script to iterate through the
TSV ﬁle and download the remaining URLs to the FUSE mount point.
- Update the ﬁle checksums in the TSV ﬁle from using MD5 to SHA256. Remove the completed
ﬁles from the TSV ﬁle and rerun the Storage Transfer Service job.
- Renew the TLS certiﬁcate of the HTTPS endpoint Remove the completed ﬁles from the TSV ﬁle
and rerun the Storage Transfer Service job.
- Create a new TSV ﬁle for the remaining ﬁles by generating signed URLs with a longer validity
period. Split the TSV ﬁle into multiple smaller ﬁles and submit them as separate Storage Transfer
Service jobs in parallel.

**Correct Answer:** D
**Explanation:** A signed URL is a URL that provides limited permission and time to access a resource on a web
server. It is often used to grant temporary access to protected ﬁles without requiring
authentication. Storage Transfer Service is a service that allows you to transfer data from
external sources, such as HTTPS endpoints, to Cloud Storage buckets. You can use a TSV ﬁle to
specify the list of URLs to transfer. In this scenario, the most likely cause of the HTTP 403 errors
is that the signed URLs have expired before the transfer job could complete. This could happen if
the signed URLs have a short validity period or the transfer job takes a long time due to the large
number of ﬁles or network latency. To ﬁx the problem, you need to create a new TSV ﬁle for the
remaining ﬁles by generating new signed URLs with a longer validity period. This will ensure that
the URLs do not expire before the transfer job ﬁnishes. You can use the Cloud Storage tools or
your own program to generate signed URLs. Additionally, you can split the TSV ﬁle into multiple
smaller ﬁles and submit them as separate Storage Transfer Service jobs in parallel. This will

speed up the transfer process and reduce the risk of errors.

---

### 2. You work for a large ecommerce company. You are using Pub/Sub to ingest the clickstream data
to Google Cloud for analytics. You observe that when a new subscriber connects to an existing
topic to analyze data, they are unable to subscribe to older data for an upcoming yearly sale
event in two months, you need a solution that, once implemented, will enable any new subscriber
to read the last 30 days of dat
a. What should you do?
**Options:**
- Create a new topic, and publish the last 30 days of data each time a new subscriber connects
to an existing topic.
- Set the topic retention policy to 30 days.
- Set the subscriber retention policy to 30 days.
- Ask the source system to re-push the data to Pub/Sub, and subscribe to it.

**Correct Answer:** B
**Explanation:** By setting the topic retention policy to 30 days, you can ensure that any new subscriber can
access the messages that were published to the topic within the last 30 days1.This feature allows
you to replay previously acknowledged messages or initialize new subscribers with historical
data2.You can conﬁgure the topic retention policy by using the Cloud Console, the gcloud
command-line tool, or the Pub/Sub API1.

Option A is not eﬃcient, as it requires creating a new topic and duplicating the data for each new
subscriber, which would increase the storage costs and complexity.Option C is not eﬀective, as it
only aﬀects the unacknowledged messages in a subscription, and does not allow new subscribers
to access older data3. Option D is not feasible, as it depends on the source system's ability and
willingness to re-push the data, and it may cause data duplication or inconsistency.

---

### 3. Your company's data platform ingests CSV ﬁle dumps of booking and user proﬁle data from
upstream sources into Cloud Storage. The data analyst team wants to join these datasets on the
email ﬁeld available in both the datasets to perform analysis. However, personally identiﬁable
information (PII) should not be accessible to the analysts. You need to de-identify the email ﬁeld
in both the datasets before loading them into BigQuery for analysts. What should you do?
**Options:**
- 1. Create a pipeline to de-identify the email ﬁeld by using recordTransformations in Cloud Data
Loss Prevention (Cloud DLP) with masking as the de-identiﬁcation transformations type.
2. Load the booking and user proﬁle data into a BigQuery table.
- 1. Create a pipeline to de-identify the email ﬁeld by using recordTransformations in Cloud DLP
with format-preserving encryption with FFX as the de-identiﬁcation transformation type.
2. Load the booking and user proﬁle data into a BigQuery table.
- 1. Load the CSV ﬁles from Cloud Storage into a BigQuery table, and enable dynamic data
masking.
2. Create a policy tag with the email mask as the data masking rule.
3. Assign the policy to the email ﬁeld in both tables. A
4. Assign the Identity and Access Management bigquerydatapolicy.maskedReader role for the
BigQuery tables to the analysts.
- 1. Load the CSV ﬁles from Cloud Storage into a BigQuery table, and enable dynamic data
masking.
2. Create a policy tag with the default masking value as the data masking rule.
3. Assign the policy to the email ﬁeld in both tables.
4. Assign the Identity and Access Management bigquerydatapolicy.maskedReader role for the
BigQuery tables to the analysts

**Correct Answer:** B
**Explanation:** Cloud DLP is a service that helps you discover, classify, and protect your sensitive data. It
supports various de-identiﬁcation techniques, such as masking, redaction, tokenization, and
encryption. Format-preserving encryption (FPE) with FFX is a technique that encrypts sensitive
data while preserving its original format and length. This allows you to join the encrypted data on
the same ﬁeld without revealing the actual values. FPE with FFX also supports partial encryption,
which means you can encrypt only a portion of the data, such as the domain name of an email
address. By using Cloud DLP to de-identify the email ﬁeld with FPE with FFX, you can ensure that
the analysts can join the booking and user proﬁle data on the email ﬁeld without accessing the
PII. You can create a pipeline to de-identify the email ﬁeld by using recordTransformations in
Cloud DLP, which allows you to specify the ﬁelds and the de-identiﬁcation transformations to
apply to them. You can then load the de-identiﬁed data into a BigQuery table for
analysis.

---

### 4. You have a Standard Tier Memorystore for Redis instance deployed in a production environment.
You need to simulate a Redis instance failover in the most accurate disaster recovery situation,
and ensure that the failover has no impact on production dat
a. What should you do?
**Options:**
- Create a Standard Tier Memorystore for Redis instance in a development environment. Initiate
a manual failover by using the force-data-loss data protection mode.
- Initiate a manual tailover by using the limited-data-loss data protection mode to the
Memorystore for Redis instance in the

production environment.
- Increase one replica to Redis instance in production environment. Initiate a manual failover by
using the force-data-loss data
protection mode.
- Create a Standard Tier Memorystore for Redis instance in the development environment.
Initiate a manual failover by using the limited-data-loss data protection mode.

**Correct Answer:** D
**Explanation:** To simulate a Redis instance failover in a production-like environment without impacting
production data, the best approach is to use a development environment. Here's why option D is
the best choice:
Standard Tier Memorystore for Redis:
The Standard Tier provides high availability and automatic failover capabilities. It's suitable for
testing failover scenarios in a controlled environment.
Development Environment:
Using a development environment ensures that any potential data loss or impact from the
failover simulation does not aﬀect production data, maintaining the integrity and availability of
the production system.
Limited-Data-Loss Mode:
The limited-data-loss mode for manual failover ensures that data loss is minimized during the
failover process, making it a realistic simulation of a production failover scenario.
Steps to Implement:
Create a Development Environment:
Set up a development environment with a Standard Tier Memorystore for Redis instance that
mirrors the conﬁguration of your production instance.
Initiate Manual Failover:
Initiate a manual failover using the limited-data-loss data protection mode to simulate a failover
scenario:
gcloud redis instances failover INSTANCE_ID --data-protection-mode=limited-data-loss
Verify Failover:

Monitor and verify the failover process to ensure it behaves as expected, simulating the disaster
recovery scenario accurately.
Memorystore for Redis Documentation
Manual Failover in Memorystore

---

### 5. You are conﬁguring networking for a Dataﬂow job. The data pipeline uses custom container
images with the libraries that are required for the transformation logic preinstalled. The data
pipeline reads the data from Cloud Storage and writes the data to BigQuery. You need to ensure
cost-eﬀective and secure communication between the pipeline and Google APIs and services.
What should you do?
**Options:**
- Leave external IP addresses assigned to worker VMs while enforcing ﬁrewall rules.
- Disable external IP addresses and establish a Private Service Connect endpoint IP address.
- Disable external IP addresses from worker VMs and enable Private Google Access.
- Enable Cloud NAT to provide outbound internet connectivity while enforcing ﬁrewall rules.

**Correct Answer:** C
**Explanation:** Private Google Access allows VMs without external IP addresses to communicate with Google APIs
and services over internal routes. This reduces the cost and increases the security of the data
pipeline. Custom container images can be stored in Container Registry, which supports Private
Google Access. Dataﬂow supports Private Google Access for both batch and streaming
jobs.

---

### 6. You are designing the architecture to process your data from Cloud Storage to BigQuery by using
Dataﬂow. The network team provided you with the Shared VPC network and subnetwork to be
used by your pipelines. You need to enable the deployment of the pipeline on the Shared VPC
network. What should you do?
**Options:**
- Assign the compute. networkUser role to the Dataﬂow service agent.
- Assign the compute.networkUser role to the service account that executes the Dataﬂow
pipeline.
- Assign the dataﬂow, admin role to the Dataﬂow service agent.
- Assign the dataﬂow, admin role to the service account that executes the Dataﬂow pipeline.

**Correct Answer:** B
**Explanation:** To use a Shared VPC network for a Dataﬂow pipeline, you need to specify the subnetwork
parameter with the full URL of the subnetwork, and grant the service account that executes the
pipeline the compute.networkUser role in the host project. This role allows the service account to
use the subnetworks in the Shared VPC network. The Dataﬂow service agent does not need this
role, as it only creates and manages the resources for the pipeline, but does not execute it. The
dataﬂow.admin role is not related to the network access, but to the permissions to create and
delete Dataﬂow jobs and resources.

---

### 7. Your company is selecting a system to centralize data ingestion and delivery. You are considering

messaging and data integration systems to address the requirements. The key requirements are:
The ability to seek to a particular oﬀset in a topic, possibly back to the start of all data ever
captured
Support for publish/subscribe semantics on hundreds of topics
Retain per-key ordering
Which system should you choose?
**Options:**
- Apache Kafka
- Cloud Storage
- Cloud Pub/Sub
- Firebase Cloud Messaging

**Correct Answer:** A

---

### 8. You are designing a data mesh on Google Cloud with multiple distinct data engineering teams
building data products. The typical data curation design pattern consists of landing ﬁles in Cloud
Storage, transforming raw data in Cloud Storage and BigQuery datasets. and storing the ﬁnal
curated data product in BigQuery datasets You need to conﬁgure Dataplex to ensure that each
team can access only the assets needed to build their data products. You also need to ensure
that teams can easily share the curated data product. What should you do?
**Options:**
- 1 Create a single Dataplex virtual lake and create a single zone to contain landing, raw. and
curated data.
2 Provide each data engineering team access to the virtual lake.
- 1 Create a single Dataplex virtual lake and create a single zone to contain landing, raw. and
curated data. 2 Build separate assets for each data product within the zone.
3. Assign permissions to the data engineering teams at the zone level.
- 1 Create a Dataplex virtual lake for each data product, and create a single zone to contain
landing, raw, and curated data.

2. Provide the data engineering teams with full access to the virtual lake assigned to their data
product.
- 1 Create a Dataplex virtual lake for each data product, and create multiple zones for landing,
raw. and curated data.
2. Provide the data engineering teams with full access to the virtual lake assigned to their data
product.

**Correct Answer:** D
**Explanation:** This option is the best way to conﬁgure Dataplex for a data mesh architecture, as it allows each
data engineering team to have full ownership and control over their data products, while also
enabling easy discovery and sharing of the curated data across the organization12.By creating a
Dataplex virtual lake for each data product, you can isolate the data assets and resources for
each domain, and avoid conﬂicts and dependencies between diﬀerent teams3.By creating
multiple zones for landing, raw, and curated data, you can enforce diﬀerent security and
governance policies for each stage of the data curation process, and ensure that only authorized
users can access the data assets45. By providing the data engineering teams with full access to
the virtual lake assigned to their data product, you can empower them to manage and monitor
their data products, and leverage the Dataplex features such as tagging, quality, and lineage.
Option A is not suitable, as it creates a single point of failure and a bottleneck for the data mesh,
and does not allow for ﬁne-grained access control and governance for diﬀerent data
products2.Option B is also not suitable, as it does not isolate the data assets and resources for
each data product, and assigns permissions at the zone level, which may not reﬂect the diﬀerent
roles and responsibilities of the data engineering teams34.Option C is better than option A and B,
but it does not create multiple zones for landing, raw, and curated data, which may compromise
the security and quality of the data products5.

---

### 9. You are migrating an application that tracks library books and information about each book, such
as author or year published, from an on-premises data warehouse to BigQuery In your current
relational database, the author information is kept in a separate table and joined to the book
information on a common key Based on Google's recommended practice for schema design, how
would you structure the data to ensure optimal speed of queries about the author of each book
that has been borrowed?
**Options:**
- Keep the schema the same, maintain the diﬀerent tables for the book and each of the
attributes, and query as you are doing today
- Create a table that is wide and includes a column for each attribute, including the author's ﬁrst
name, last name, date of birth, etc
- Create a table that includes information about the books and authors, but nest the author
ﬁelds inside the author column
- Keep the schema the same, create a view that joins all of the tables, and always query the
view

**Correct Answer:** C

---

### 10. You are designing a system that requires an ACID-compliant database. You must ensure that the
system requires minimal human intervention in case of a failure. What should you do?
**Options:**
- Conﬁgure a Cloud SQL for MySQL instance with point-in-time recovery enabled.
- Conﬁgure a Cloud SQL for PostgreSQL instance with high availability enabled.
- Conﬁgure a Bigtable instance with more than one cluster.
- Conﬁgure a BJgQuery table with a multi-region conﬁguration.

**Correct Answer:** B
**Explanation:** The best option to meet the ACID compliance and minimal human intervention requirements is to
conﬁgure a Cloud SQL for PostgreSQL instance with high availability enabled. Key reasons: Cloud
SQL for PostgreSQL provides full ACID compliance, unlike Bigtable which provides only atomicity
and consistency guarantees. Enabling high availability removes the need for manual failover as
Cloud SQL will automatically failover to a standby replica if the leader instance goes down. Point-
in-time recovery in MySQL requires manual intervention to restore data if needed. BigQuery does
not provide transactional guarantees required for an ACID database. Therefore, a Cloud SQL for
PostgreSQL instance with high availability meets the ACID and minimal intervention requirements
best. The automatic failover will ensure availability and uptime without administrative eﬀort.

---

### 11. You receive data ﬁles in CSV format monthly from a third party. You need to cleanse this data,
but every third month the schema of the ﬁles changes. Your requirements for implementing
these transformations include:
Executing the transformations on a schedule
Enabling non-developer analysts to modify transformations
Providing a graphical tool for designing transformations
What should you do?
**Options:**
- Use Cloud Dataprep to build and maintain the transformation recipes, and execute them on a
scheduled basis
- Load each month's CSV data into BigQuery, and write a SQL query to transform the data to a
standard schema. Merge the transformed tables together with a SQL query
- Help the analysts write a Cloud Dataﬂow pipeline in Python to perform the transformation. The
Python code should be stored in a revision control system and modiﬁed as the incoming data's
schema changes
- Use Apache Spark on Cloud Dataproc to infer the schema of the CSV ﬁle before creating a

Dataframe. Then implement the transformations in Spark SQL before writing the data out to
Cloud Storage and loading into BigQuery

**Correct Answer:** A
**Explanation:** you can use dataprep for continuously changing target schema
In general, a target consists of the set of information required to deﬁne the expected data in a
dataset. Often referred to as a 'schema,' this target schema information can include:
Names of columns
Order of columns
Column data types
Data type format
Example rows of data
A dataset associated with a target is expected to conform to the requirements of the schema.
Where there are diﬀerences between target schema and dataset schema, a validation indicator
(or schema tag) is displayed.
https://cloud.google.com/dataprep/docs/html/Overview-of-RapidTarget_136155049

Engineer Visit
a-engineer
ata-engineer

---

