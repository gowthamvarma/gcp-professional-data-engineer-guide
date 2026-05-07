# PDE Practice Quiz #22 - May 2026

### 1. Your car factory is pushing machine measurements as messages into a Pub/Sub topic in your
Google Cloud project. A Dataﬂow streaming job. that you wrote with the Apache Beam SDK, reads
these messages, sends acknowledgment lo Pub/Sub. applies some custom business logic in a
Doﬀs instance, and writes the result to BigQuery. You want to ensure that if your business logic
fails on a message, the message will be sent to a Pub/Sub topic that you want to monitor for
alerting purposes. What should you do?
**Options:**
- Use an exception handling block in your Data Flow's Doﬀs code to push the messages that
failed to be transformed through a side output
and to a new Pub/Sub topic. Use Cloud Monitoring to monitor the
topic/num_jnacked_messages_by_region metric on this new topic.
- Enable retaining of acknowledged messages in your Pub/Sub pull subscription. Use Cloud
Monitoring to monitor the
subscription/num_retained_acked_messages metric on this subscription.
- Enable dead lettering in your Pub/Sub pull subscription, and specify a new Pub/Sub topic as the
dead letter topic. Use Cloud Monitoring to
monitor the subscription/dead_letter_message_count metric on your pull subscription.
- Create a snapshot of your Pub/Sub pull subscription. Use Cloud Monitoring to monitor the
snapshot/numessages metric on this
snapshot.

**Correct Answer:** C
**Explanation:** To ensure that messages failing to process in your Dataﬂow job are sent to a Pub/Sub topic for
monitoring and alerting, the best approach is to use Pub/Sub's dead-letter topic feature. Here's
why option C is the best choice:
Dead-Letter Topic:
Pub/Sub's dead-letter topic feature allows messages that fail to be processed successfully to be
redirected to a speciﬁed topic. This ensures that these messages are not lost and can be
reviewed for debugging and alerting purposes.
Monitoring and Alerting:

By specifying a new Pub/Sub topic as the dead-letter topic, you can use Cloud Monitoring to track
metrics such as subscription/dead_letter_message_count, providing visibility into the number of
failed messages.
This allows you to set up alerts based on these metrics to notify the appropriate teams when
failures occur.
Steps to Implement:
Enable Dead-Letter Topic:
Conﬁgure your Pub/Sub pull subscription to enable dead lettering and specify the new Pub/Sub
topic for dead-letter messages.
Set Up Monitoring:
Use Cloud Monitoring to monitor the subscription/dead_letter_message_count metric on your pull
subscription.
Conﬁgure alerts based on this metric to notify the team of any processing failures.
Pub/Sub Dead Letter Policy
Cloud Monitoring with Pub/Sub

---

### 2. You are designing a data mesh on Google Cloud by using Dataplex to manage data in BigQuery
and Cloud Storage. You want to simplify data asset permissions. You are creating a customer
virtual lake with two user groups:
* Data engineers, which require lull data lake access
* Analytic users, which require access to curated data
You need to assign access rights to these two groups. What should you do?
**Options:**
- 1. Grant the dataplex.dataOwner role to the data engineer group on the customer data lake.
2. Grant the dataplex.dataReader role to the analytic user group on the customer curated zone.
- 1. Grant the dataplex.dataReader role to the data engineer group on the customer data lake.
2. Grant the dataplex.dataOwner to the analytic user group on the customer curated zone.
- 1. Grant the bigquery.dataownex role on BigQuery datasets and the storage.objectcreator role
on Cloud Storage buckets to data engineers.
2. Grant the bigquery.dataViewer role on BigQuery datasets and the storage.objectViewer role on
Cloud Storage buckets to analytic users.
- 1. Grant the bigquery.dataViewer role on BigQuery datasets and the storage.objectviewer role
on Cloud Storage buckets to data engineers.
2. Grant the bigquery.dataOwner role on BigQuery datasets and the storage.objectEditor role on
Cloud Storage buckets to analytic users.

**Correct Answer:** A
**Explanation:** When designing a data mesh on Google Cloud using Dataplex to manage data in BigQuery and
Cloud Storage, it is essential to simplify data asset permissions while ensuring that each user
group has the appropriate access levels. Here's why option A is the best choice:
Data Engineer Group:
Data engineers require full access to the data lake to manage and operate data assets
comprehensively. Granting the dataplex.dataOwner role to the data engineer group on the
customer data lake ensures they have the necessary permissions to create, modify, and delete
data assets within the lake.
Analytic User Group:
Analytic users need access to curated data but do not require full control over all data assets.
Granting the dataplex.dataReader role to the analytic user group on the customer curated zone
provides read-only access to the curated data, enabling them to analyze the data without the
ability to modify or delete it.
Steps to Implement:
Grant Data Engineer Permissions:
Assign the dataplex.dataOwner role to the data engineer group on the customer data lake to
ensure full access and management capabilities.
Grant Analytic User Permissions:
Assign the dataplex.dataReader role to the analytic user group on the customer curated zone to
provide read-only access to curated data.
Dataplex IAM Roles and Permissions

Managing Access in Dataplex

---

### 3. You want to encrypt the customer data stored in BigQuery. You need to implement for-user
crypto-deletion on data stored in your tables. You want to adopt native features in Google Cloud
to avoid custom solutions. What should you do?
**Options:**
- Create a customer-managed encryption key (CMEK) in Cloud KMS. Associate the key to the
table while creating the table.
- Create a customer-managed encryption key (CMEK) in Cloud KMS. Use the key to encrypt data
before storing in BigQuery.
- Implement Authenticated Encryption with Associated Data (AEAD) BigQuery functions while
storing your data in BigQuery.
- Encrypt your data during ingestion by using a cryptographic library supported by your ETL
pipeline.

**Correct Answer:** A
**Explanation:** To implement for-user crypto-deletion and ensure that customer data stored in BigQuery is
encrypted, using native Google Cloud features, the best approach is to use Customer-Managed
Encryption Keys (CMEK) with Cloud Key Management Service (KMS). Here's why:
Customer-Managed Encryption Keys (CMEK):
CMEK allows you to manage your own encryption keys using Cloud KMS. These keys provide
additional control over data access and encryption management.
Associating a CMEK with a BigQuery table ensures that data is encrypted with a key you manage.
For-User Crypto-Deletion:
For-user crypto-deletion can be achieved by disabling or destroying the CMEK. Once the key is
disabled or destroyed, the data encrypted with that key cannot be decrypted, eﬀectively
rendering it unreadable.

Native Integration:
Using CMEK with BigQuery is a native feature, avoiding the need for custom encryption solutions.
This simpliﬁes the management and implementation of encryption and decryption processes.
Steps to Implement:
Create a CMEK in Cloud KMS:
Set up a new customer-managed encryption key in Cloud KMS.
Associate the CMEK with BigQuery Tables:
When creating a new table in BigQuery, specify the CMEK to be used for encryption.
This can be done through the BigQuery console, CLI, or API.
BigQuery and CMEK
Cloud KMS Documentation
Encrypting Data in BigQuery

---

### 4. You recently deployed several data processing jobs into your Cloud Composer 2 environment.
You notice that some tasks are failing in Apache Airﬂow. On the monitoring dashboard, you see
an increase in the total workers' memory usage, and there were worker pod evictions. You need
to resolve these errors. What should you do?
Choose 2 answers
**Options:**
- Increase the directed acyclic graph (DAG) ﬁle parsing interval.
- Increase the memory available to the Airﬂow workers.
- Increase the maximum number of workers and reduce worker concurrency.
- Increase the memory available to the Airﬂow triggerer.
- Increase the Cloud Composer 2 environment size from medium to large.

**Correct Answer:** B, C
**Explanation:** To resolve issues related to increased memory usage and worker pod evictions in your Cloud
Composer 2 environment, the following steps are recommended:
Increase Memory Available to Airﬂow Workers:
By increasing the memory allocated to Airﬂow workers, you can handle more memory-intensive
tasks, reducing the likelihood of pod evictions due to memory limits.
Increase Maximum Number of Workers and Reduce Worker Concurrency:
Increasing the number of workers allows the workload to be distributed across more pods,
preventing any single pod from becoming overwhelmed.
Reducing worker concurrency limits the number of tasks that each worker can handle
simultaneously, thereby lowering the memory consumption per worker.
Steps to Implement:
Increase Worker Memory:
Modify the conﬁguration settings in Cloud Composer to allocate more memory to Airﬂow workers.
This can be done through the environment conﬁguration settings.
Adjust Worker and Concurrency Settings:
Increase the maximum number of workers in the Cloud Composer environment settings.
Reduce the concurrency setting for Airﬂow workers to ensure that each worker handles fewer
tasks at a time, thus consuming less memory per worker.
Cloud Composer Worker Conﬁguration
Scaling Airﬂow Workers

---

### 5. You are architecting a data transformation solution for BigQuery. Your developers are proﬁcient
with SOL and want to use the ELT development technique. In addition, your developers need an
intuitive coding environment and the ability to manage SQL as code. You need to identify a
solution for your developers to build these pipelines. What should you do?
**Options:**
- Use Cloud Composer to load data and run SQL pipelines by using the BigQuery job operators.
- Use Dataﬂow jobs to read data from Pub/Sub, transform the data, and load the data to
BigQuery.
- Use Dataform to build, manage, and schedule SQL pipelines.
- Use Data Fusion to build and execute ETL pipelines

**Correct Answer:** C
**Explanation:** To architect a data transformation solution for BigQuery that aligns with the ELT development
technique and provides an intuitive coding environment for SQL-proﬁcient developers, Dataform
is an optimal choice. Here's why:
ELT Development Technique:
ELT (Extract, Load, Transform) is a process where data is ﬁrst extracted and loaded into a data
warehouse, and then transformed using SQL queries. This is diﬀerent from ETL, where data is
transformed before being loaded into the data warehouse.
BigQuery supports ELT, allowing developers to write SQL transformations directly in the data
warehouse.
Dataform:
Dataform is a development environment designed speciﬁcally for data transformations in
BigQuery and other SQL-based warehouses.
It provides tools for managing SQL as code, including version control and collaborative
development.
Dataform integrates well with existing development workﬂows and supports scheduling and
managing SQL-based data pipelines.
Intuitive Coding Environment:
Dataform oﬀers an intuitive and user-friendly interface for writing and managing SQL queries.
It includes features like SQLX, a SQL dialect that extends standard SQL with features for
modularity and reusability, which simpliﬁes the development of complex transformation logic.
Managing SQL as Code:
Dataform supports version control systems like Git, enabling developers to manage their SQL

transformations as code.
This allows for better collaboration, code reviews, and version tracking.
Dataform Documentation
BigQuery Documentation
Managing ELT Pipelines with Dataform

---

### 6. You have a BigQuery dataset named "customers". All tables will be tagged by using a Data
Catalog tag template named "gdpr". The template contains one mandatory ﬁeld, "has sensitive
data~. with a boolean value. All employees must be able to do a simple search and ﬁnd tables in
the dataset that have either true or false in the "has sensitive data" ﬁeld. However, only the
Human Resources (HR) group should be able to see the data inside the tables for which "hass-
ensitive-data" is true. You give the all employees group the bigquery.metadataViewer and
bigquery.connectionUser roles on the dataset. You want to minimize conﬁguration overhead.
What should you do next?
**Options:**
- Create the 'gdpr' tag template with private visibility. Assign the bigquery -dataViewer role to
the HR group on the tables that contain sensitive data.
- Create the ~gdpr' tag template with private visibility. Assign the datacatalog.
tagTemplateViewer role on this tag to the all employees
group, and assign the bigquery.dataViewer role to the HR group on the tables that contain
sensitive data.
- Create the 'gdpr' tag template with public visibility. Assign the bigquery. dataViewer role to
the HR group on the tables that contain
sensitive data.
- Create the 'gdpr' tag template with public visibility. Assign the datacatalog.
tagTemplateViewer role on this tag to the all employees.
group, and assign the bijquery.dataViewer role to the HR group on the tables that contain
sensitive data.

**Correct Answer:** D
**Explanation:** To ensure that all employees can search and ﬁnd tables with GDPR tags while restricting data
access to sensitive tables only to the HR group, follow these steps:
Data Catalog Tag Template:
Use Data Catalog to create a tag template named 'gdpr' with a boolean ﬁeld 'has sensitive data'.
Set the visibility to public so all employees can see the tags.
Roles and Permissions:
Assign the datacatalog.tagTemplateViewer role to the all employees group. This role allows users
to view the tags and search for tables based on the 'has sensitive data' ﬁeld.
Assign the bigquery.dataViewer role to the HR group speciﬁcally on tables that contain sensitive
data. This ensures only HR can access the actual data in these tables.
Steps to Implement:
Create the GDPR Tag Template:
Deﬁne the tag template in Data Catalog with the necessary ﬁelds and set visibility to public.
Assign Roles:
Grant the datacatalog.tagTemplateViewer role to the all employees group for visibility into the
tags.
Grant the bigquery.dataViewer role to the HR group on tables marked as having sensitive data.
Data Catalog Documentation
Managing Access Control in BigQuery
IAM Roles in Data Catalog

---

### 7. A web server sends click events to a Pub/Sub topic as messages. The web server includes an
event Timestamp attribute in the messages, which is the time when the click occurred. You have
a Dataﬂow streaming job that reads from this Pub/Sub topic through a subscription, applies some
transformations, and writes the result to another Pub/Sub topic for use by the advertising
department. The advertising department needs to receive each message within 30 seconds of
the corresponding click occurrence, but they report receiving the messages late. Your Dataﬂow

job's system lag is about 5 seconds, and the data freshness is about 40 seconds. Inspecting a few
messages show no more than 1 second lag between their event Timestamp and publish Time.
What is the problem and what should you do?
**Options:**
- The advertising department is causing delays when consuming the messages. Work with the
advertising department to ﬁx this.
- Messages in your Dataﬂow job are processed in less than 30 seconds, but your job cannot
keep up with the backlog in the Pub/Sub
subscription. Optimize your job or increase the number of workers to ﬁx this.
- The web server is not pushing messages fast enough to Pub/Sub. Work with the web server
team to ﬁx this.
- Messages in your Dataﬂow job are taking more than 30 seconds to process. Optimize your job
or increase the number of workers to ﬁx this.

**Correct Answer:** B
**Explanation:** To ensure that the advertising department receives messages within 30 seconds of the click
occurrence, and given the current system lag and data freshness metrics, the issue likely lies in
the processing capacity of the Dataﬂow job. Here's why option B is the best choice:
System Lag and Data Freshness:
The system lag of 5 seconds indicates that Dataﬂow itself is processing messages relatively
quickly.
However, the data freshness of 40 seconds suggests a signiﬁcant delay before processing begins,
indicating a backlog.
Backlog in Pub/Sub Subscription:
A backlog occurs when the rate of incoming messages exceeds the rate at which the Dataﬂow job
can process them, causing delays.
Optimizing the Dataﬂow Job:
To handle the incoming message rate, the Dataﬂow job needs to be optimized or scaled up by
increasing the number of workers, ensuring it can keep up with the message inﬂow.
Steps to Implement:

Analyze the Dataﬂow Job:
Inspect the Dataﬂow job metrics to identify bottlenecks and ineﬃciencies.
Optimize Processing Logic:
Optimize the transformations and operations within the Dataﬂow pipeline to improve processing
eﬃciency.
Increase Number of Workers:
Scale the Dataﬂow job by increasing the number of workers to handle the higher load, reducing
the backlog.
Dataﬂow Monitoring
Scaling Dataﬂow Jobs

---

### 8. You are running your BigQuery project in the on-demand billing model and are executing a
change data capture (CDC) process that ingests dat
a. The CDC process loads 1 GB of data every 10 minutes into a temporary table, and then
performs a merge into a 10 TB target table. This process is very scan intensive and you want to
explore options to enable a predictable cost model. You need to create a BigQuery reservation
based on utilization information gathered from BigQuery Monitoring and apply the reservation to
the CDC process. What should you do?
**Options:**
- Create a BigQuery reservation for the job.
- Create a BigQuery reservation for the service account running the job.
- Create a BigQuery reservation for the dataset.
- Create a BigQuery reservation for the project.

**Correct Answer:** D
**Explanation:** https://cloud.google.com/blog/products/data-analytics/manage-bigquery-costs-with-custom-quota
s.
Here's why creating a BigQuery reservation for the project is the most suitable solution:
Project-Level Reservation: BigQuery reservations are applied at the project level. This means that
the reserved slots (processing capacity) are shared across all jobs and queries running within that
project. Since your CDC process is a signiﬁcant contributor to your BigQuery usage, reserving
slots for the entire project ensures that your CDC process always has access to the necessary
resources, regardless of other activities in the project.
Predictable Cost Model: Reservations provide a ﬁxed, predictable cost model. Instead of paying
the on-demand price for each query, you pay a ﬁxed monthly fee for the reserved slots. This
eliminates the variability of costs associated with on-demand billing, making it easier to budget
and forecast your BigQuery expenses.
BigQuery Monitoring: You can use BigQuery Monitoring to analyze the historical usage patterns of
your CDC process and other queries within your project. This information helps you determine the
appropriate amount of slots to reserve, ensuring that you have enough capacity to handle your
workload while optimizing costs.
Why other options are not suitable:
A . Create a BigQuery reservation for the job: BigQuery does not support reservations at the
individual job level. Reservations are applied at the project or assignment level.
B . Create a BigQuery reservation for the service account running the job: While you can create
reservations for assignments (groups of users or service accounts), it's less eﬃcient than a
project-level reservation in this scenario. A project-level reservation covers all jobs within the
project, regardless of the service account used.
C . Create a BigQuery reservation for the dataset: BigQuery does not support reservations at the
dataset level.
By creating a BigQuery reservation for your project based on your utilization analysis, you can
achieve a predictable cost model while ensuring that your CDC process and other queries have
the necessary resources to run smoothly.

---

### 9. You have important legal hold documents in a Cloud Storage bucket. You need to ensure that
these documents are not deleted or modiﬁed. What should you do?
**Options:**
- Set a retention policy. Lock the retention policy.
- Set a retention policy. Set the default storage class to Archive for long-term digital
preservation.
- Enable the Object Versioning feature. Add a lifecycle rule.
- Enable the Object Versioning feature. Create a copy in a bucket in a diﬀerent region.

**Correct Answer:** A
**Explanation:** To ensure that important legal hold documents in a Cloud Storage bucket are not deleted or
modiﬁed, the most eﬀective method is to set and lock a retention policy. Here's why this is the
best choice:
Retention Policy:
A retention policy deﬁnes a retention period during which objects in the bucket cannot be deleted
or modiﬁed. This ensures data immutability.
Once a retention policy is set and locked, it cannot be removed or reduced, providing strong
protection against accidental or malicious deletions.
Locking the Retention Policy:
Locking a retention policy ensures that the retention period cannot be changed. This action is
permanent and guarantees that the speciﬁed retention period will be enforced.
Steps to Implement:
Set the Retention Policy:
Deﬁne a retention period for the bucket to ensure that all objects are protected for the required
duration.
Lock the Retention Policy:
Lock the retention policy to prevent any modiﬁcations, ensuring the immutability of the
documents.
Cloud Storage Retention Policy Documentation
How to Set a Retention Policy

---

### 10. Your company operates in three domains: airlines, hotels, and ride-hailing services. Each domain
has two teams: analytics and data science, which create data assets in BigQuery with the help of
a central data platform team. However, as each domain is evolving rapidly, the central data
platform team is becoming a bottleneck. This is causing delays in deriving insights from data, and
resulting in stale data when pipelines are not kept up to date. You need to design a data mesh
architecture by using Dataplex to eliminate the bottleneck. What should you do?
**Options:**
- 1. Create one lake for each team. Inside each lake, create one zone for each domain.
2. Attach each of the BigQuery datasets created by the individual teams as assets to the
respective zone.
3. Have the central data platform team manage all zones' data assets.
- 1 Create one lake for each team. Inside each lake, create one zone for each domain.
2. Attach each to the BigQuory datasets created by the individual teams as assets to the
respective zone.
3. Direct each domain to manage their own zone's data assets.
- 1 Create one lake for each domain. Inside each lake, create one zone for each team.
2. Attach each of the BigQuery datasets created by the individual teams as assets to the
respective zone.
3. Direct each domain to manage their own lake's data assets.
- 1 Create one lake for each domain. Inside each lake, create one zone for each team.
2. Attach each of the BigQuery datasets created by the individual teams as assets to the
respective zone.
3. Have the central data platform team manage all lakes' data assets.

**Correct Answer:** B
**Explanation:** To design a data mesh architecture using Dataplex to eliminate bottlenecks caused by a central
data platform team, consider the following:
Data Mesh Architecture:
Data mesh promotes a decentralized approach where domain teams manage their own data

pipelines and assets, increasing agility and reducing bottlenecks.
Dataplex Lakes and Zones:
Lakes in Dataplex are logical containers for managing data at scale, and zones are subdivisions
within lakes for organizing data based on domains, teams, or other criteria.
Domain and Team Management:
By creating a lake for each team and zones for each domain, each team can independently
manage their data assets without relying on the central data platform team.
This setup aligns with the principles of data mesh, promoting ownership and reducing delays in
data processing and insights.
Implementation Steps:
Create Lakes and Zones:
Create separate lakes in Dataplex for each team (analytics and data science).
Within each lake, create zones for the diﬀerent domains (airlines, hotels, ride-hailing).
Attach BigQuery Datasets:
Attach the BigQuery datasets created by the respective teams as assets to their corresponding
zones.
Decentralized Management:
Allow each domain to manage their own zone's data assets, providing them with the autonomy to
update and maintain their pipelines without depending on the central team.
Dataplex Documentation
BigQuery Documentation
Data Mesh Principles

---

### 11. You are planning to load some of your existing on-premises data into BigQuery on Google Cloud.
You want to either stream or batch-load data, depending on your use case. Additionally, you want
to mask some sensitive data before loading into BigQuery. You need to do this in a programmatic
way while keeping costs to a minimum. What should you do?
**Options:**
- Use the BigQuery Data Transfer Service to schedule your migration. After the data is populated
in BigQuery. use the connection to the Cloud Data Loss Prevention {Cloud DLP} API to de-identify
the necessary data.
- Create your pipeline with Dataﬂow through the Apache Beam SDK for Python, customizing
separate options within your code for streaming.
batch processing, and Cloud DLP Select BigQuery as your data sink.
- Use Cloud Data Fusion to design your pipeline, use the Cloud DLP plug-in to de-identify data
within your pipeline, and then move the data
into BigQuery.
- Set up Datastream to replicate your on-premise data on BigQuery.

**Correct Answer:** B
**Explanation:** To load on-premises data into BigQuery while masking sensitive data, we need a solution that
oﬀers ﬂexibility for both streaming and batch processing, as well as data masking capabilities.
Here's a detailed explanation of why option B is the best choice:
Apache Beam and Dataﬂow:
Apache Beam SDK provides a uniﬁed programming model for both batch and stream data
processing.
Google Cloud Dataﬂow is a fully managed service for executing Apache Beam pipelines, oﬀering
scalability and ease of use.
Customization for Diﬀerent Use Cases:
By using the Apache Beam SDK, you can write custom pipelines that can handle both streaming
and batch processing within the same framework.
This allows you to switch between streaming and batch modes based on your use case without
changing the core logic of your data pipeline.
Data Masking with Cloud DLP:
Google Cloud Data Loss Prevention (DLP) API can be integrated into your Apache Beam pipeline
to de-identify and mask sensitive data programmatically before loading it into BigQuery.
This ensures that sensitive data is handled securely and complies with privacy requirements.
Cost Eﬃciency:

Using Dataﬂow can be cost-eﬀective because it is a fully managed service, reducing the
operational overhead associated with managing your own infrastructure.
The pay-as-you-go model ensures you only pay for the resources you consume, which can help
keep costs under control.
Implementation Steps:
Set up Apache Beam Pipeline:
Write a pipeline using the Apache Beam SDK for Python that reads data from your on-premises
storage.
Add transformations for data processing, including the integration with Cloud DLP for data
masking.
Conﬁgure Dataﬂow:
Deploy the Apache Beam pipeline on Google Cloud Dataﬂow.
Customize the pipeline options for both streaming and batch use cases.
Load Data into BigQuery:
Set BigQuery as the sink for your data in the Apache Beam pipeline.
Ensure the processed and masked data is loaded into the appropriate BigQuery tables.
Apache Beam Documentation
Google Cloud Dataﬂow Documentation
Google Cloud DLP Documentation
BigQuery Documentation

---

### 12. You need to create a SQL pipeline. The pipeline runs an aggregate SOL transformation on a
BigQuery table every two hours and appends the result to another existing BigQuery table. You
need to conﬁgure the pipeline to retry if errors occur. You want the pipeline to send an email
notiﬁcation after three consecutive failures. What should you do?
**Options:**
- Create a BigQuery scheduled query to run the SOL transformation with schedule options that
repeats every two hours, and enable email
notiﬁcations.
- Use the BigQueryUpsertTableOperator in Cloud Composer, set the retry parameter to three,
and set the email_on_failure parameter to
true.
- Use the BigQuerylnsertJobOperator in Cloud Composer, set the retry parameter to three, and
set the email_on_failure parameter to
true.
- Create a BigQuery scheduled query to run the SQL transformation with schedule options that
repeats every two hours, and enable
notiﬁcation to Pub/Sub topic. Use Pub/Sub and Cloud Functions to send an email after three tailed
executions.

**Correct Answer:** D
**Explanation:** To create a robust and resilient SQL pipeline in BigQuery that handles retries and failure
notiﬁcations, consider the following:
BigQuery Scheduled Queries: This feature allows you to schedule recurring queries in BigQuery. It
is a straightforward way to run SQL transformations on a regular basis without requiring
extensive setup.
Error Handling and Retries: While BigQuery Scheduled Queries can run at speciﬁed intervals, they
don't natively support complex retry logic or failure notiﬁcations directly. This is where additional
Google Cloud services like Pub/Sub and Cloud Functions come into play.
Pub/Sub for Notiﬁcations: By conﬁguring a BigQuery scheduled query to publish messages to a
Pub/Sub topic upon failure, you can create a decoupled and scalable notiﬁcation system.
Cloud Functions: Cloud Functions can subscribe to the Pub/Sub topic and implement logic to
count consecutive failures. After detecting three consecutive failures, the Cloud Function can
then send an email notiﬁcation using a service like SendGrid or Gmail API.
Implementation Steps:
Set up a BigQuery Scheduled Query:
Create a scheduled query in BigQuery to run your SQL transformation every two hours.
Conﬁgure the scheduled query to publish a notiﬁcation to a Pub/Sub topic in case of a failure.

Create a Pub/Sub Topic:
Create a Pub/Sub topic that will receive messages from the scheduled query.
Develop a Cloud Function:
Write a Cloud Function that subscribes to the Pub/Sub topic.
Implement logic in the Cloud Function to track failure messages. If three consecutive failure
messages are detected, the function sends an email notiﬁcation.
BigQuery Scheduled Queries
Pub/Sub Documentation
Cloud Functions Documentation
SendGrid Email API
Gmail API

Engineer Visit
a-engineer
ata-engineer

---

