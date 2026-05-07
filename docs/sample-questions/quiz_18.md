# PDE Practice Quiz #18 - May 2026

### 1. Your startup has a web application that currently serves customers out of a single region in Asi
a. You are targeting funding that will allow your startup lo serve customers globally. Your current
goal is to optimize for cost, and your post-funding goat is to optimize for global presence and
performance. You must use a native JDBC driver. What should you do?
**Options:**
- Use Cloud Spanner to conﬁgure a single region instance initially. and then conﬁgure multi-
region C oud Spanner instances after securing funding.
- Use a Cloud SQL for PostgreSQL highly available instance ﬁrst, and 8gtable with US. Europe,
and Asia
replication alter securing funding
- Use a Cloud SQL for PostgreSQL zonal instance ﬁrst and Bigtable with US. Europe, and Asia
after securing funding.
- Use a Cloud SOL for PostgreSQL zonal instance ﬁrst, and Cloud SOL for PostgreSQL with highly
available conﬁguration after securing funding.

**Correct Answer:** A
**Explanation:** https://cloud.google.com/spanner/docs/instance-conﬁgurations#tradeoﬀs_regional_versus_multi-r
egion_conﬁgurations

---

### 2. You orchestrate ETL pipelines by using Cloud Composer One of the tasks in the Apache Airﬂow
directed acyclic graph (DAG) relies on a third-party service. You want to be notiﬁed when the task
does not succeed. What should you do?
**Options:**
- Conﬁgure a Cloud Monitoring alert on the sla_missed metric associated with the task at risk to
trigger a notiﬁcation.
- Assign a function with notiﬁcation logic to the sla_miss_callback parameter for the operator
responsible for the task at risk.
- Assign a function with notiﬁcation logic to the on_retry_callback parameter for the operator
responsible for the task at risk.
- Assign a function with notiﬁcation logic to the on_failure_callback parameter for the operator
responsible for the task at risk.

**Correct Answer:** D
**Explanation:** By assigning a function with notiﬁcation logic to the on_failure_callback parameter, you can
customize the action that is taken when a task fails in your DAG1.For example, you can send an
email, a Slack message, or a PagerDuty alert to notify yourself or your team about the task
failure2.This option is more ﬂexible and reliable than conﬁguring a Cloud Monitoring alert on the
sla_missed metric, which only triggers when a task misses its scheduled deadline3.The
sla_miss_callback parameter is also related to the sla_missed metric, and it is executed when the
task instance has not succeeded and the time is past the task's scheduled execution date plus its
sla4.The on_retry_callback parameter is executed before a task is retried4. These options are not
suitable for notifying when a task does not succeed, as they depend on the task's schedule and
retry settings, which may not reﬂect the actual task completion status.

---

### 3. You are designing a pipeline that publishes application events to a Pub/Sub topic. You need to
aggregate events across hourly intervals before loading the results to BigQuery for analysis. Your
solution must be scalable so it can process and load large volumes of events to BigQuery. What

should you do?
**Options:**
- Create a streaming Dataﬂow job to continually read from the Pub/Sub topic and perform the
necessary aggregations using tumbling windows
- Schedule a batch Dataﬂow job to run hourly, pulling all available messages from the Pub-Sub
topic and performing the necessary aggregations
- Schedule a Cloud Function to run hourly, pulling all avertable messages from the Pub/Sub topic
and performing the necessary aggregations
- Create a Cloud Function to perform the necessary data processing that executes using the
Pub/Sub trigger every time a new message is published to the topic.

**Correct Answer:** A

---

### 4. You want to store your team's shared tables in a single dataset to make data easily accessible to
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

### 5. You are a BigQuery admin supporting a team of data consumers who run ad hoc queries and
downstream reporting in tools such as Looker. All data and users are combined under a single
organizational project. You recently noticed some slowness in query results and want to
troubleshoot where the slowdowns are occurring. You think that there might be some job queuing
or slot contention occurring as users run jobs, which slows down access to results. You need to
investigate the query job information and determine where performance is being aﬀected. What
should you do?
**Options:**
- Use Cloud Monitoring to view BigQuery metrics and set up alerts that let you know when a
certain percentage of slots were used.
- Use slot reservations for your project to ensure that you have enough query processing
capacity and are able to allocate available slots to the slower queries.
- Use Cloud Logging to determine if any users or downstream consumers are changing or
deleting access grants on tagged resources.
- Use available administrative resource charts to determine how slots are being used and how
jobs are performing over time. Run a query on the INFORMATION_SCHEMA to review query
performance.

**Correct Answer:** D
**Explanation:** To troubleshoot query performance issues related to job queuing or slot contention in BigQuery,
using administrative resource charts along with querying the INFORMATION_SCHEMA is the best
approach. Here's why option D is the best choice:
Administrative Resource Charts:
BigQuery provides detailed resource charts that show slot usage and job performance over time.
These charts help identify patterns of slot contention and peak usage times.
INFORMATION_SCHEMA Queries:
The INFORMATION_SCHEMA tables in BigQuery provide detailed metadata about query jobs,
including execution times, slots consumed, and other performance metrics.
Running queries on INFORMATION_SCHEMA allows you to pinpoint speciﬁc jobs causing
contention and analyze their performance characteristics.
Comprehensive Analysis:
Combining administrative resource charts with detailed queries on INFORMATION_SCHEMA
provides a holistic view of the system's performance.
This approach enables you to identify and address the root causes of performance issues,
whether they are due to slot contention, ineﬃcient queries, or other factors.
Steps to Implement:
Access Administrative Resource Charts:
Use the Google Cloud Console to view BigQuery's administrative resource charts. These charts
provide insights into slot utilization and job performance metrics over time.
Run INFORMATION_SCHEMA Queries:
Execute queries on BigQuery's INFORMATION_SCHEMA to gather detailed information about job
performance. For example:
SELECT
creation_time,
job_id,
user_email,

query,
total_slot_ms / 1000 AS slot_seconds,
total_bytes_processed / (1024 * 1024 * 1024) AS processed_gb,
total_bytes_billed / (1024 * 1024 * 1024) AS billed_gb
FROM
`region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
WHERE
creation_time > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY)
AND state = 'DONE'
ORDER BY
slot_seconds DESC
LIMIT 100;
Analyze and Optimize:
Use the information gathered to identify bottlenecks, optimize queries, and adjust resource
allocations as needed to improve performance.
Monitoring BigQuery Slots
BigQuery INFORMATION_SCHEMA
BigQuery Performance Best Practices

---

### 6. You have a streaming pipeline that ingests data from Pub/Sub in production. You need to update
this streaming pipeline with improved business logic. You need to ensure that the updated
pipeline reprocesses the previous two days of delivered Pub/Sub messages. What should you do?
Choose 2 answers
**Options:**
- Use Pub/Sub Seek with a timestamp.
- Use the Pub/Sub subscription clear-retry-policy ﬂag.
- Create a new Pub/Sub subscription two days before the deployment.
- Use the Pub/Sub subscription retain-asked-messages ﬂag.
- Use Pub/Sub Snapshot capture two days before the deployment.

**Correct Answer:** A, E
**Explanation:** To update a streaming pipeline with improved business logic and reprocess the previous two
days of delivered Pub/Sub messages, you should use Pub/Sub Seek with a timestamp and
Pub/Sub Snapshot capture two days before the deployment. Pub/Sub Seek allows you to replay or
purge messages in a subscription based on a time or a snapshot. Pub/Sub Snapshot allows you to
capture the state of a subscription at a given point in time and replay messages from that point.
By using these features, you can ensure that the updated pipeline can process the messages that
were delivered in the past two days without losing any data.

---

### 7. You are designing the architecture of your application to store data in Cloud Storage. Your
application consists of pipelines that read data from a Cloud Storage bucket that contains raw
data, and write the data to a second bucket after processing. You want to design an architecture
with Cloud Storage resources that are capable of being resilient if a Google Cloud regional failure
occurs. You want to minimize the recovery point objective (RPO) if a failure occurs, with no
impact on applications that use the stored dat
a. What should you do?
**Options:**
- Adopt two regional Cloud Storage buckets, and update your application to write the output on
both buckets.
- Adopt multi-regional Cloud Storage buckets in your architecture.
- Adopt two regional Cloud Storage buckets, and create a daily task to copy from one bucket to
the other.
- Adopt a dual-region Cloud Storage bucket, and enable turbo replication in your architecture.

**Correct Answer:** D
**Explanation:** To ensure resilience and minimize the recovery point objective (RPO) with no impact on
applications, using a dual-region bucket with turbo replication is the best approach. Here's why
option D is the best choice:
Dual-Region Buckets:
Dual-region buckets store data redundantly across two distinct geographic regions, providing
high availability and durability.
This setup ensures that data remains available even if one region experiences a failure.
Turbo Replication:
Turbo replication ensures that data is replicated between the two regions within 15 minutes,
aligning with the requirement to minimize the recovery point objective (RPO).
This feature provides near real-time replication, signiﬁcantly reducing the risk of data loss.
No Impact on Applications:
Applications continue to access the dual-region bucket without any changes, ensuring seamless
operation even during a regional failure.
The dual-region setup transparently handles failover, providing uninterrupted access to data.
Steps to Implement:
Create a Dual-Region Bucket:
Create a dual-region Cloud Storage bucket in the Google Cloud Console, selecting appropriate
regions (e.g., us-central1 and us-east1).
Enable Turbo Replication:
Enable turbo replication to ensure rapid data replication between the selected regions.
Conﬁgure Applications:
Ensure that applications read and write to the dual-region bucket, beneﬁting from its high
availability and durability.

Test Failover:
Simulate a regional failure to verify that the dual-region bucket and turbo replication meet the
required RPO and ensure data resilience.
Google Cloud Storage Dual-Region
Turbo Replication in Google Cloud Storage

Engineer Visit
a-engineer
ata-engineer

---

