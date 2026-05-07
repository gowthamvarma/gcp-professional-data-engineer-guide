# PDE Practice Quiz #8 - May 2026

### 1. You need to create a new transaction table in Cloud Spanner that stores product sales dat
a. You are deciding what to use as a primary key. From a performance perspective, which
strategy should you choose?
**Options:**
- The current epoch time
- A concatenation of the product name and the current epoch time
- A random universally unique identiﬁer number (version 4 UUID)
- The original order identiﬁcation number from the sales system, which is a monotonically
increasing integer

**Correct Answer:** C

---

### 2. You have a table that contains millions of rows of sales data, partitioned by date Various
applications and users query this data many times a minute. The query requires aggregating
values by using avg. max. and sum, and does not require joining to other tables. The required
aggregations are only computed over the past year of data, though you need to retain full
historical data in the base tables You want to ensure that the query results always include the
latest data from the tables, while also reducing computation cost, maintenance overhead, and
duration. What should you do?
**Options:**
- Create a materialized view to aggregate the base table data Conﬁgure a partition expiration
on the base table to retain only the last one year of partitions.
- Create a materialized view to aggregate the base table data include a ﬁlter clause to specify
the last one year of partitions.
- Create a new table that aggregates the base table data include a ﬁlter clause to specify the
last year of partitions. Set up a scheduled query to recreate the new table every hour.
- Create a view to aggregate the base table data Include a ﬁlter clause to specify the last year
of partitions.

**Correct Answer:** C
**Explanation:** A materialized view is a database object that contains the results of a query, which can be
updated periodically. It can improve the performance and eﬃciency of queries that involve
aggregations, joins, or ﬁlters. By creating a materialized view to aggregate the base table data
and include a ﬁlter clause to specify the last one year of partitions, you can ensure that the query
results always include the latest data from the tables, while also reducing computation cost,
maintenance overhead, and duration. The materialized view will automatically refresh when the
base table data changes, and will only use the partitions that match the ﬁlter clause. Option A is
incorrect because it will delete the historical data from the base table, which is not desired.
Option C is incorrect because it will create a redundant table that needs to be updated manually
by a scheduled query, which is more complex and costly than using a materialized view. Option D
is incorrect because a view does not store any data, but only references the base table data,
which means it will not reduce the computation cost or duration of the query.

---

### 3. You are updating the code for a subscriber to a Put/Sub feed. You are concerned that upon
deployment the subscriber may erroneously acknowledge messages, leading to message loss.
You subscriber is not set up to retain acknowledged messages. What should you do to ensure
that you can recover from errors after deployment?
**Options:**
- Use Cloud Build for your deployment if an error occurs after deployment, use a Seek operation
to locate a tmestamp logged by Cloud Build at the start of the deployment
- Create a Pub/Sub snapshot before deploying new subscriber code. Use a Seek operation to re-
deliver messages that became available after the snapshot was created
- Set up the Pub/Sub emulator on your local machine Validate the behavior of your new
subscriber togs before deploying it to production
- Enable dead-lettering on the Pub/Sub topic to capture messages that aren't successful
acknowledged if an error occurs after deployment, re-deliver any messages captured by the
dead-letter queue

**Correct Answer:** B

---

### 4. You are developing a new deep teaming model that predicts a customer's likelihood to buy on
your ecommerce site. Alter running an evaluation of the model against both the original training
data and new test data, you ﬁnd that your model is overﬁtting the dat
a. You want to improve the accuracy of the model when predicting new data. What should you
do?
**Options:**
- Increase the size of the training dataset, and increase the number of input features.
- Increase the size of the training dataset, and decrease the number of input features.
- Reduce the size of the training dataset, and increase the number of input features.
- Reduce the size of the training dataset, and decrease the number of input features.

**Correct Answer:** B
**Explanation:** https://machinelearningmastery.com/impact-of-dataset-size-on-deep-learning-model-skill-and-per
formance-estimates/

---

### 5. You are planning to use Cloud Storage as pad of your data lake solution. The Cloud Storage
bucket will contain objects ingested from external systems. Each object will be ingested once,
and the access patterns of individual objects will be random. You want to minimize the cost of
storing and retrieving these objects. You want to ensure that any cost optimization eﬀorts are
transparent to the users and applications. What should you do?
**Options:**
- Create a Cloud Storage bucket with Autoclass enabled.
- Create a Cloud Storage bucket with an Object Lifecycle Management policy to transition
objects from Standard to Coldline storage class if an object age reaches 30 days.
- Create a Cloud Storage bucket with an Object Lifecycle Management policy to transition
objects from Standard to Coldline storage class if an object is not live.
- Create two Cloud Storage buckets. Use the Standard storage class for the ﬁrst bucket, and use
the Coldline storage class for the second bucket. Migrate objects from the ﬁrst bucket to the
second bucket after 30 days.

**Correct Answer:** A
**Explanation:** To minimize the cost of storing and retrieving objects in a Cloud Storage bucket while ensuring
that cost optimization eﬀorts are transparent to the users and applications, enabling Autoclass is
the best approach. Here's why:
Autoclass Feature:
Autoclass automatically transitions objects between diﬀerent storage classes (Standard, Nearline,
Coldline, and Archive) based on their access patterns.
It ensures that frequently accessed data is kept in lower-latency, higher-cost storage classes and
infrequently accessed data is moved to higher-latency, lower-cost storage classes.
Cost Optimization:
Autoclass optimizes storage costs by automatically moving objects to the most cost-eﬀective
storage class based on actual usage patterns, without manual intervention.
This feature ensures that objects are stored in the most economical class appropriate for their
access frequency, reducing storage costs over time.
Transparency to Users:

The transition of objects between storage classes is handled automatically by Cloud Storage,
making the process transparent to users and applications.
Users and applications interact with the objects in the same way, regardless of the underlying
storage class, ensuring seamless access.
Steps to Implement:
Create a Cloud Storage Bucket:
When creating a new Cloud Storage bucket, enable the Autoclass feature.
Conﬁgure Autoclass:
Autoclass conﬁguration is typically a straightforward process in the Google Cloud Console, where
you enable it during bucket creation.
Monitor and Adjust:
Monitor the storage and access patterns through the Google Cloud Console to ensure that
Autoclass is optimizing costs as expected.
Google Cloud Storage Autoclass
Optimizing Storage Costs with Autoclass

---

### 6. You are designing a real-time system for a ride hailing app that identiﬁes areas with high demand
for rides to eﬀectively reroute available drivers to meet the demand. The system ingests data
from multiple sources to Pub/Sub. processes the data, and stores the results for visualization and
analysis in real-time dashboards. The data sources include driver location updates every 5
seconds and app-based booking events from riders. The data processing involves real-time
aggregation of supply and demand data for the last 30 seconds, every 2 seconds, and storing the
results in a low-latency system for visualization. What should you do?
**Options:**
- Group the data by using a tumbling window in a Dataﬂow pipeline, and write the aggregated
data to Memorystore
- Group the data by using a hopping window in a Dataﬂow pipeline, and write the aggregated
data to Memorystore
- Group the data by using a session window in a Dataﬂow pipeline, and write the aggregated

data to BigQuery.
- Group the data by using a hopping window in a Dataﬂow pipeline, and write the aggregated
data to BigQuery.

**Correct Answer:** B
**Explanation:** A hopping window is a type of sliding window that advances by a ﬁxed period of time, producing
overlapping windows. This is suitable for the scenario where the system needs to aggregate data
for the last 30 seconds, every 2 seconds, and provide real-time updates. A Dataﬂow pipeline can
implement the hopping window logic using Apache Beam, and process both streaming and batch
data sources. Memorystore is a low-latency, in-memory data store that can serve the aggregated
data to the visualization layer. BigQuery is not a good choice for this scenario, as it is not
optimized for low-latency queries and frequent updates.

---

### 7. You need ads data to serve Al models and historical data tor analytics longtail and outlier data
points need to be identiﬁed You want to cleanse the data n near-reel time before running it
through Al models What should you do?
**Options:**
- Use BigQuery to ingest prepare and then analyze the data and then run queries to create
views
- Use Cloud Storage as a data warehouse shell scripts tor processing, and BigQuery to create
views tor desired datasets
- Use Dataﬂow to identity longtail and outber data points programmatically with BigQuery as a
sink
- Use Cloud Composer to identify longtail and outlier data points, and then output a usable
dataset to BigQuery

**Correct Answer:** A

---

### 8. You have 100 GB of data stored in a BigQuery table. This data is outdated and will only be
accessed one or two times a year for analytics with SQL. For backup purposes, you want to store
this data to be immutable for 3 years. You want to minimize storage costs. What should you do?
**Options:**
- 1 Create a BigQuery table clone.
2. Query the clone when you need to perform analytics.
- 1 Create a BigQuery table snapshot.
2 Restore the snapshot when you need to perform analytics.
- 1. Perform a BigQuery export to a Cloud Storage bucket with archive storage class.
2 Enable versionmg on the bucket.
3. Create a BigQuery external table on the exported ﬁles.
- 1 Perform a BigQuery export to a Cloud Storage bucket with archive storage class.
2 Set a locked retention policy on the bucket.
3. Create a BigQuery external table on the exported ﬁles.

**Correct Answer:** D
**Explanation:** This option will allow you to store the data in a low-cost storage option, as the archive storage
class has the lowest price per GB among the Cloud Storage classes. It will also ensure that the
data is immutable for 3 years, as the locked retention policy prevents the deletion or overwriting
of the data until the retention period expires. You can still query the data using SQL by creating a
BigQuery external table that references the exported ﬁles in the Cloud Storage bucket. Option A
is incorrect because creating a BigQuery table clone will not reduce the storage costs, as the
clone will have the same size and storage class as the original table. Option B is incorrect
because creating a BigQuery table snapshot will also not reduce the storage costs, as the
snapshot will have the same size and storage class as the original table. Option C is incorrect
because enabling versioning on the bucket will not make the data immutable, as the versions can
still be deleted or overwritten by anyone with the appropriate permissions. It will also increase
the storage costs, as each version of the ﬁle will be charged separately.

---

### 9. You have designed an Apache Beam processing pipeline that reads from a Pub/Sub topic. The
topic has a message retention duration of one day, and writes to a Cloud Storage bucket. You
need to select a bucket location and processing strategy to prevent data loss in case of a regional
outage with an RPO of 15 minutes. What should you do?
**Options:**
- 1 Use a regional Cloud Storage bucket
2 Monitor Dataﬂow metrics with Cloud Monitoring to determine when an outage occurs
3 Seek the subscription back in time by one day to recover the acknowledged messages
4 Start the Dataﬂow job in a secondary region and write in a bucket in the same region
- 1 Use a multi-regional Cloud Storage bucket
2 Monitor Dataﬂow metrics with Cloud Monitoring to determine when an outage occurs
3 Seek the subscription back in time by 60 minutes to recover the acknowledged messages
4 Start the Dataﬂow job in a secondary region
- 1. Use a dual-region Cloud Storage bucket.
2. Monitor Dataﬂow metrics with Cloud Monitoring to determine when an outage occurs
3 Seek the subscription back in time by 15 minutes to recover the acknowledged messages
4 Start the Dataﬂow job in a secondary region
- 1. Use a dual-region Cloud Storage bucket with turbo replication enabled
2 Monitor Dataﬂow metrics with Cloud Monitoring to determine when an outage occurs
3 Seek the subscription back in time by 60 minutes to recover the acknowledged messages
4 Start the Dataﬂow job in a secondary region.

**Correct Answer:** C
**Explanation:** A dual-region Cloud Storage bucket is a type of bucket that stores data redundantly across two
regions within the same continent. This provides higher availability and durability than a regional
bucket, which stores data in a single region. A dual-region bucket also provides lower latency and

higher throughput than a multi-regional bucket, which stores data across multiple regions within
a continent or across continents. A dual-region bucket with turbo replication enabled is a
premium option that oﬀers even faster replication across regions, but it is more expensive and
not necessary for this scenario.
By using a dual-region Cloud Storage bucket, you can ensure that your data is protected from
regional outages, and that you can access it from either region with low latency and high
performance. You can also monitor the Dataﬂow metrics with Cloud Monitoring to determine
when an outage occurs, and seek the subscription back in time by 15 minutes to recover the
acknowledged messages. Seeking a subscription allows you to replay the messages from a
Pub/Sub topic that were published within the message retention duration, which is one day in this
case. By seeking the subscription back in time by 15 minutes, you can meet the RPO of 15
minutes, which means the maximum amount of data loss that is acceptable for your business.
You can then start the Dataﬂow job in a secondary region and write to the same dual-region
bucket, which will resume the processing of the messages and prevent data loss.
Option A is not a good solution, as using a regional Cloud Storage bucket does not provide any
redundancy or protection from regional outages. If the region where the bucket is located
experiences an outage, you will not be able to access your data or write new data to the bucket.
Seeking the subscription back in time by one day is also unnecessary and ineﬃcient, as it will
replay all the messages from the past day, even though you only need to recover the messages
from the past 15 minutes.
Option B is not a good solution, as using a multi-regional Cloud Storage bucket does not provide
the best performance or cost-eﬃciency for this scenario. A multi-regional bucket stores data
across multiple regions within a continent or across continents, which provides higher availability
and durability than a dual-region bucket, but also higher latency and lower throughput. A multi-
regional bucket is more suitable for serving data to a global audience, not for processing data
with Dataﬂow within a single continent. Seeking the subscription back in time by 60 minutes is
also unnecessary and ineﬃcient, as it will replay more messages than needed to meet the RPO of
15 minutes.
Option D is not a good solution, as using a dual-region Cloud Storage bucket with turbo
replication enabled does not provide any additional beneﬁt for this scenario, but only increases
the cost. Turbo replication is a premium option that oﬀers faster replication across regions, but it
is not required to meet the RPO of 15 minutes. Seeking the subscription back in time by 60
minutes is also unnecessary and ineﬃcient, as it will replay more messages than needed to meet
the RPO of 15 minutes.

---

### 10. You have a streaming pipeline that ingests data from Pub/Sub in production. You need to update
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

