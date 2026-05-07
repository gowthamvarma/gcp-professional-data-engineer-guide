# PDE Practice Quiz #12 - May 2026

### 1. You want to store your team's shared tables in a single dataset to make data easily accessible to
various analysts. You want to make this data readable but unmodiﬁable by analysts. At the same
time, you want to provide the analysts with individual workspaces in the same project, where
they can create and store tables for their own use, without the tables being accessible by other
analysts. What should you do?
**Options:**
- Give analysts the BigQuery Data Viewer role at the project level Create one other dataset, and
give the analysts the BigQuery Data Editor role on that dataset.
- Give analysts the BigQuery Data Viewer role at the project level Create a dataset for each
analyst, and give each analyst the BigQuery Data Editor role at the project level.
- Give analysts the BigQuery Data Viewer role on the shared dataset. Create a dataset for each
analyst, and give each analyst the BigQuery Data Editor role at the dataset level for their
assigned dataset
- Give analysts the BigQuery Data Viewer role on the shared dataset Create one other dataset
and give the analysts the BigQuery Data Editor role on that dataset.

**Correct Answer:** C
**Explanation:** The BigQuery Data Viewer role allows users to read data and metadata from tables and views,
but not to modify or delete them. By giving analysts this role on the shared dataset, you can
ensure that they can access the data for analysis, but not change it. The BigQuery Data Editor
role allows users to create, update, and delete tables and views, as well as read and write data.
By giving analysts this role at the dataset level for their assigned dataset, you can provide them
with individual workspaces where they can store their own tables and views, without aﬀecting the
shared dataset or other analysts' datasets. This way, you can achieve both data protection and
data isolation for your team.

---

### 2. You want to schedule a number of sequential load and transformation jobs Data ﬁles will be
added to a Cloud Storage bucket by an upstream process There is no ﬁxed schedule for when the
new data arrives Next, a Dataproc job is triggered to perform some transformations and write the
data to BigQuery. You then need to run additional transformation jobs in BigQuery The
transformation jobs are diﬀerent for every table These jobs might take hours to complete You
need to determine the most eﬃcient and maintainable workﬂow to process hundreds of tables
and provide the freshest data to your end users. What should you do?
**Options:**
- 1Create an Apache Airﬂow directed acyclic graph (DAG) in Cloud Composer with sequential
tasks by using the Cloud Storage. Dataproc. and BigQuery operators
2 Use a single shared DAG for all tables that need to go through the pipeline
3 Schedule the DAG to run hourly
- 1 Create an Apache Airﬂow directed acyclic graph (DAG) in Cloud Composer with sequential
tasks by using the Dataproc and BigQuery operators.
2 Create a separate DAG for each table that needs to go through the pipeline
3 Use a Cloud Storage object trigger to launch a Cloud Function that triggers the DAG
- 1 Create an Apache Airﬂow directed acyclic graph (DAG) in Cloud Composer with sequential
tasks by using the Cloud Storage, Dataproc. and BigQuery operators
2 Create a separate DAG for each table that needs to go through the pipeline
3 Schedule the DAGs to run hourly
- 1 Create an Apache Airﬂow directed acyclic graph (DAG) in Cloud Composer with sequential
tasks by using the Dataproc and BigQuery operators
2 Use a single shared DAG for all tables that need to go through the pipeline.
3 Use a Cloud Storage object trigger to launch a Cloud Function that triggers the DAG

**Correct Answer:** B
**Explanation:** This option is the most eﬃcient and maintainable workﬂow for your use case, as it allows you to
process each table independently and trigger the DAGs only when new data arrives in the Cloud
Storage bucket.By using the Dataproc and BigQuery operators, you can easily orchestrate the
load and transformation jobs for each table, and leverage the scalability and performance of
these services12.By creating a separate DAG for each table, you can customize the
transformation logic and parameters for each table, and avoid the complexity and overhead of a

single shared DAG3.By using a Cloud Storage object trigger, you can launch a Cloud Function that
triggers the DAG for the corresponding table, ensuring that the data is processed as soon as
possible and reducing the idle time and cost of running the DAGs on a ﬁxed schedule4.
Option A is not eﬃcient, as it runs the DAG hourly regardless of the data arrival, and it uses a
single shared DAG for all tables, which makes it harder to maintain and debug. Option C is also
not eﬃcient, as it runs the DAGs hourly and does not leverage the Cloud Storage object trigger.
Option D is not maintainable, as it uses a single shared DAG for all tables, and it does not use the
Cloud Storage operator, which can simplify the data ingestion from the bucket.

---

### 3. You are building an ELT solution in BigQuery by using Dataform. You need to perform uniqueness
and null value checks on your ﬁnal tables. What should you do to eﬃciently integrate these
checks into your pipeline?
**Options:**
- Build Dataform assertions into your code
- Write a Spark-based stored procedure.
- Build BigQuery user-deﬁned functions (UDFs).
- Create Dataplex data quality tasks.

**Correct Answer:** A
**Explanation:** Dataform assertions are data quality tests that ﬁnd rows that violate one or more rules speciﬁed
in the query. If the query returns any rows, the assertion fails. Dataform runs assertions every
time it updates your SQL workﬂow and alerts you if any assertions fail. You can create assertions
for all Dataform table types: tables, incremental tables, views, and materialized views. You can
add built-in assertions to the conﬁg block of a table, such as nonNull and rowConditions, or create
manual assertions with SQLX for advanced use cases. Dataform automatically creates views in
BigQuery that contain the results of compiled assertion queries, which you can inspect to debug
failing assertions. Dataform assertions are an eﬃcient way to integrate data quality checks into
your ELT solution in BigQuery by using Dataform.

---

### 4. You have a data pipeline with a Cloud Dataﬂow job that aggregates and writes time series
metrics to Cloud Bigtable. This data feeds a dashboard used by thousands of users across the
organization. You need to support additional concurrent users and reduce the amount of time
required to write the dat
a. Which two actions should you take? (Choose two.)
**Options:**
- Conﬁgure your Cloud Dataﬂow pipeline to use local execution
- Increase the maximum number of Cloud Dataﬂow workers by setting maxNumWorkers in
PipelineOptions
- Increase the number of nodes in the Cloud Bigtable cluster
- Modify your Cloud Dataﬂow pipeline to use the Flatten transform before writing to Cloud
Bigtable
- Modify your Cloud Dataﬂow pipeline to use the CoGroupByKey transform before writing to
Cloud Bigtable

**Correct Answer:** B, C

---

### 5. You are troubleshooting your Dataﬂow pipeline that processes data from Cloud Storage to
BigQuery. You have discovered that the Dataﬂow worker nodes cannot communicate with one
another Your networking team relies on Google Cloud network tags to deﬁne ﬁrewall rules You
need to identify the issue while following Google-recommended networking security practices.
What should you do?
**Options:**
- Determine whether your Dataﬂow pipeline has a custom network tag set.
- Determine whether there is a ﬁrewall rule set to allow traﬃc on TCP ports 12345 and 12346 for
the Dataﬂow network tag.
- Determine whether your Dataﬂow pipeline is deployed with the external IP address option
enabled.
- Determine whether there is a ﬁrewall rule set to allow traﬃc on TCP ports 12345 and 12346 on
the subnet used by Dataﬂow workers.

**Correct Answer:** D
**Explanation:** Dataﬂow worker nodes need to communicate with each other and with the Dataﬂow service on
TCP ports 12345 and 12346. These ports are used for data shuﬄing and streaming engine
communication. By default, Dataﬂow assigns a network tag called dataﬂow to the worker nodes,
and creates a ﬁrewall rule that allows traﬃc on these ports for the dataﬂow network tag.
However, if you use a custom network tag for your Dataﬂow pipeline, you need to create a
ﬁrewall rule that allows traﬃc on these ports for your custom network tag. Otherwise, the worker
nodes will not be able to communicate with each other and the Dataﬂow service, and the pipeline
will fail.
Therefore, the best way to identify the issue is to determine whether there is a ﬁrewall rule set to
allow traﬃc on TCP ports 12345 and 12346 for the Dataﬂow network tag. If there is no such
ﬁrewall rule, or if the ﬁrewall rule does not match the network tag used by your Dataﬂow
pipeline, you need to create or update the ﬁrewall rule accordingly.
Option A is not a good solution, as determining whether your Dataﬂow pipeline has a custom
network tag set does not tell you whether there is a ﬁrewall rule that allows traﬃc on the
required ports for that network tag. You need to check the ﬁrewall rule as well.
Option C is not a good solution, as determining whether your Dataﬂow pipeline is deployed with
the external IP address option enabled does not tell you whether there is a ﬁrewall rule that
allows traﬃc on the required ports for the Dataﬂow network tag. The external IP address option

determines whether the worker nodes can access resources on the public internet, but it does not
aﬀect the internal communication between the worker nodes and the Dataﬂow service.
Option D is not a good solution, as determining whether there is a ﬁrewall rule set to allow traﬃc
on TCP ports 12345 and 12346 on the subnet used by Dataﬂow workers does not tell you whether
the ﬁrewall rule applies to the Dataﬂow network tag. The ﬁrewall rule should be based on the
network tag, not the subnet, as the network tag is more speciﬁc and secure.

---

### 6. You are testing a Dataﬂow pipeline to ingest and transform text ﬁles. The ﬁles are compressed
gzip, errors are written to a dead-letter queue, and you are using Sidelnputs to join data You
noticed that the pipeline is taking longer to complete than expected, what should you do to
expedite the Dataﬂow job?
**Options:**
- Switch to compressed Avro ﬁles
- Reduce the batch size
- Retry records that throw an error
- Use CoGroupByKey instead of the Sidelnput

**Correct Answer:** B

---

### 7. You are designing a Dataﬂow pipeline for a batch processing job. You want to mitigate multiple
zonal failures at job submission time. What should you do?
**Options:**
- Specify a worker region by using the ---region ﬂag.
- Set the pipeline staging location as a regional Cloud Storage bucket.
- Submit duplicate pipelines in two diﬀerent zones by using the ---zone ﬂag.
- Create an Eventarc trigger to resubmit the job in case of zonal failure when submitting the job.

**Correct Answer:** B
**Explanation:** By specifying a worker region, you can run your Dataﬂow pipeline in a multi-zone or multi-region
conﬁguration, which provides higher availability and resilience in case of zonal failures1.The ---
region ﬂag allows you to specify the regional endpoint for your pipeline, which determines the
location of the Dataﬂow service and the default location of the Compute Engine resources1.If you
do not specify a zone by using the ---zone ﬂag, Dataﬂow automatically selects a zone within the
region for your job workers1. This option is recommended over submitting duplicate pipelines in
two diﬀerent zones, which would incur additional costs and complexity.Setting the pipeline
staging location as a regional Cloud Storage bucket does not aﬀect the availability of your
pipeline, as the staging location only stores the pipeline code and dependencies2. Creating an
Eventarc trigger to resubmit the job in case of zonal failure is not a reliable solution, as it
depends on the availability of the Eventarc service and the zonal resources at the time of
resubmission.

---

### 8. You are migrating your data warehouse to BigQuery. You have migrated all of your data into
tables in a dataset. Multiple users from your organization will be using the dat
a. They should only see certain tables based on their team membership. How should you set user
permissions?
**Options:**
- Assign the users/groups data viewer access at the table level for each table
- Create SQL views for each team in the same dataset in which the data resides, and assign the
users/groups data viewer access to the SQL views
- Create authorized views for each team in the same dataset in which the data resides, and
assign the users/groups data viewer access to the authorized views
- Create authorized views for each team in datasets created for each team. Assign the
authorized views data viewer access to the dataset in which the data resides. Assign the
users/groups data viewer access to the datasets in which the authorized views reside

**Correct Answer:** A

---

### 9. You are designing a system that requires an ACID-compliant database. You must ensure that the
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

### 10. You are migrating a large number of ﬁles from a public HTTPS endpoint to Cloud Storage. The
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

### 11. Diﬀerent teams in your organization store customer and performance data in BigOuery. Each
team needs to keep full control of their collected data, be able to query data within their projects,
and be able to exchange their data with other teams. You need to implement an organization-
wide solution, while minimizing operational tasks and costs. What should you do?
**Options:**
- Create a BigQuery scheduled query to replicate all customer data into team projects.
- Enable each team to create materialized views of the data they need to access in their
projects.
- Ask each team to publish their data in Analytics Hub. Direct the other teams to subscribe to
them.
- Ask each team to create authorized views of their data. Grant the biquery. jobUser role to each
team.

**Correct Answer:** C
**Explanation:** To enable diﬀerent teams to manage their own data while allowing data exchange across the
organization, using Analytics Hub is the best approach. Here's why option C is the best choice:
Analytics Hub:

Analytics Hub allows teams to publish their data as data exchanges, making it easy for other
teams to discover and subscribe to the data they need.
This approach maintains each team's control over their data while facilitating easy and secure
data sharing across the organization.
Data Publishing and Subscribing:
Teams can publish datasets they control, allowing them to manage access and updates
independently.
Other teams can subscribe to these published datasets, ensuring they have access to the latest
data without duplicating eﬀorts.
Minimized Operational Tasks and Costs:
This method reduces the need for complex replication or data synchronization processes,
minimizing operational overhead.
By centralizing data sharing through Analytics Hub, it also reduces storage costs associated with
duplicating large datasets.
Steps to Implement:
Set Up Analytics Hub:
Enable Analytics Hub in your Google Cloud project.
Provide training to teams on how to publish and subscribe to data exchanges.
Publish Data:
Each team publishes their datasets in Analytics Hub, conﬁguring access controls and metadata as
needed.
Subscribe to Data:
Teams that need access to data from other teams can subscribe to the relevant data exchanges,
ensuring they always have up-to-date data.
Analytics Hub Documentation
Publishing Data in Analytics Hub
Subscribing to Data in Analytics Hub

---

### 12. Your company is selecting a system to centralize data ingestion and delivery. You are considering
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

