# PDE Practice Quiz #16 - May 2026

### 1. You are designing a data warehouse in BigQuery to analyze sales data for a telecommunication
service provider. You need to create a data model for customers, products, and subscriptions All
customers, products, and subscriptions can be updated monthly, but you must maintain a
historical record of all dat
a. You plan to use the visualization layer for current and historical reporting. You need to ensure
that the data model is simple, easy-to-use. and cost-eﬀective. What should you do?
**Options:**
- Create a normalized model with tables for each entity. Use snapshots before updates to track
historical data
- Create a normalized model with tables for each entity. Keep all input ﬁles in a Cloud Storage
bucket to track historical data
- Create a denormalized model with nested and repeated ﬁelds Update the table and use
snapshots to track historical data
- Create a denormalized, append-only model with nested and repeated ﬁelds Use the ingestion
timestamp to track historical data.

**Correct Answer:** D
**Explanation:** - A denormalized, append-only model simpliﬁes query complexity by eliminating the need for
joins. - Adding data with an ingestion timestamp allows for easy retrieval of both current and
historical states. - Instead of updating records, new records are appended, which maintains
historical information without the need to create separate snapshots.

---

### 2. You have data pipelines running on BigQuery, Cloud Dataﬂow, and Cloud Dataproc. You need to
perform health checks and monitor their behavior, and then notify the team managing the
pipelines if they fail. You also need to be able to work across multiple projects. Your preference is

to use managed products of features of the platform. What should you do?
**Options:**
- Export the information to Cloud Stackdriver, and set up an Alerting policy
- Run a Virtual Machine in Compute Engine with Airﬂow, and export the information to
Stackdriver
- Export the logs to BigQuery, and set up App Engine to read that information and send emails if
you ﬁnd a failure in the logs
- Develop an App Engine application to consume logs using GCP API calls, and send emails if
you ﬁnd a failure in the logs

**Correct Answer:** B

---

### 3. You are working on a linear regression model on BigQuery ML to predict a customer's likelihood
of purchasing your company's products. Your model uses a city name variable as a key predictive
component in order to train and serve the model your data must be organized in columns. You
want to prepare your data using the least amount of coding while maintaining the predictable
variables. What should you do?
**Options:**
- Use SQL in BigQuery to transform the stale column using a one-hot encoding method, and
make each city a column with binary values.
- Create a new view with BigQuery that does not include a column which city information.
- Cloud Data Fusion to assign each city to a region that is labeled as 1, 2 3, 4, or 5, and then use
that number to represent the city in the model.
- Use TensorFlow to create a categorical variable with a vocabulary list. Create the vocabulary
ﬁle and upload that as part of your model to BigQuery ML.

**Correct Answer:** C

---

### 4. You want to create a machine learning model using BigQuery ML and create an endpoint foe
hosting the model using Vertex Al. This will enable the processing of continuous streaming data
in near-real time from multiple vendors. The data may contain invalid values. What should you
do?
**Options:**
- Create a new BigOuery dataset and use streaming inserts to land the data from multiple
vendors. Conﬁgure your BigQuery ML model to use the 'ingestion' dataset as the training data.
- Use BigQuery streaming inserts to land the data from multiple vendors whore your BigQuery
dataset ML model is deployed.
- Create a Pub'Sub topic and send all vendor data to it Connect a Cloud Function to the topic to
process the data and store it in BigQuery.
- Create a Pub/Sub topic and send all vendor data to it Use Dataﬂow to process and sanitize the
Pub/Sub data and stream it to BigQuery.

**Correct Answer:** D
**Explanation:** Dataﬂow provides a scalable and ﬂexible way to process and clean the incoming data in real-time
before loading it into BigQuery.

---

### 5. Diﬀerent teams in your organization store customer and performance data in BigOuery. Each
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

### 6. You are conﬁguring networking for a Dataﬂow job. The data pipeline uses custom container
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

### 7. You've migrated a Hadoop job from an on-premises cluster to Dataproc and Good Storage. Your
Spark job is a complex analytical workload ﬁat consists of many shuﬄing operations, and initial
data are parquet toes (on average 200-400 MB size each) You see some degradation in
performance after the migration to Dataproc so you'd like to optimize for it. Your organization is
very cost-sensitive so you'd Idee to continue using Dataproc on preemptibles (with 2 non-
preemptibles workers only) for this workload. What should you do?
**Options:**
- Switch from HODs to SSDs override the preemptible VMs conﬁguration to increase the boot
disk size
- Increase the see of your parquet ﬁles to ensure them to be 1 GB minimum
- Switch to TFRecords format (appr 200 MB per We) instead of parquet ﬁles
- Switch from HDDs to SSDs. copy initial data from Cloud Storage to Hadoop Distributed File
System (HDFS) run the Spark job and copy results back to Cloud Storage

**Correct Answer:** A

---

### 8. Your company's customer_order table in BigOuery stores the order history for 10 million
customers, with a table size of 10 PB. You need to create a dashboard for the support team to
view the order history. The dashboard has two ﬁlters, countryname and username. Both are

string data types in the BigQuery table. When a ﬁlter is applied, the dashboard fetches the order
history from the table and displays the query results. However, the dashboard is slow to show the
results when applying the ﬁlters to the following query:
How should you redesign the BigQuery table to support faster access?
**Options:**
- Cluster the table by country ﬁeld, and partition by username ﬁeld.
- Partition the table by country and username ﬁelds.
- Cluster the table by country and username ﬁelds
- Partition the table by _PARTITIONTIME.

**Correct Answer:** C
**Explanation:** To improve the performance of querying a large BigQuery table with ﬁlters on countryname and
username, clustering the table by these ﬁelds is the most eﬀective approach. Here's why option
C is the best choice:
Clustering in BigQuery:
Clustering organizes data based on the values in speciﬁed columns. This can signiﬁcantly
improve query performance by reducing the amount of data scanned during query execution.
Clustering by countryname and username means that data is physically sorted and stored
together based on these ﬁelds, allowing BigQuery to quickly locate and read only the relevant
data for queries using these ﬁlters.
Filter Eﬃciency:
With the table clustered by countryname and username, queries that ﬁlter on these columns can
beneﬁt from eﬃcient data retrieval, reducing the amount of data processed and speeding up
query execution.
This directly addresses the performance issue of the dashboard queries that apply ﬁlters on these
ﬁelds.
Steps to Implement:

Redesign the Table:
Create a new table with clustering on countryname and username:
CREATE TABLE project.dataset.new_table
CLUSTER BY countryname, username AS
SELECT * FROM project.dataset.customer_order;
Migrate Data:
Transfer the existing data from the original table to the new clustered table.
Update Queries:
Modify the dashboard queries to reference the new clustered table.
BigQuery Clustering Documentation
Optimizing Query Performance

---

### 9. Your company is implementing a data warehouse using BigQuery, and you have been tasked with
designing the data model You move your on-premises sales data warehouse with a star data
schema to BigQuery but notice performance issues when querying the data of the past 30 days
Based on Google's recommended practices, what should you do to speed up the query without
increasing storage costs?
**Options:**
- Denormalize the data
- Shard the data by customer ID
- Materialize the dimensional data in views
- Partition the data by transaction date

**Correct Answer:** C

---

### 10. You are using BigQuery with a regional dataset that includes a table with the daily sales volumes.
This table is updated multiple times per day. You need to protect your sales table in case of
regional failures with a recovery point objective (RPO) of less than 24 hours, while keeping costs
to a minimum. What should you do?
**Options:**
- Schedule a daily BigQuery snapshot of the table.
- Schedule a daily export of the table to a Cloud Storage dual or multi-region bucket.
- Schedule a daily copy of the dataset to a backup region.
- Modify ETL job to load the data into both the current and another backup region.

**Correct Answer:** A
**Explanation:** To apply complex business logic on a JSON response using Python's standard library within a
Workﬂow, invoking a Cloud Function is the most eﬃcient and straightforward approach. Here's
why option A is the best choice:
Cloud Functions:
Cloud Functions provide a lightweight, serverless execution environment for running code in
response to events. They support Python and can easily integrate with Workﬂows.
This approach ensures simplicity and speed of execution, as Cloud Functions can be invoked
directly from a Workﬂow and handle the complex logic required.
Flexibility and Simplicity:
Using Cloud Functions allows you to leverage Python's extensive standard library and ecosystem,
making it easier to implement and maintain the complex business logic.
Cloud Functions abstract the underlying infrastructure, allowing you to focus on the application
logic without worrying about server management.
Performance:
Cloud Functions are optimized for fast execution and can handle the processing of the JSON

response eﬃciently.
They are designed to scale automatically based on demand, ensuring that your workﬂow remains
performant.
Steps to Implement:
Write the Cloud Function:
Develop a Cloud Function in Python that processes the JSON response and applies the necessary
business logic.
Deploy the function to Google Cloud.
Invoke Cloud Function from Workﬂow:
Modify your Workﬂow to call the Cloud Function using an HTTP request or Google Cloud Function
connector.
steps:
- callCloudFunction:
call: http.post
args:
url: https://REGION-PROJECT_ID.cloudfunctions.net/FUNCTION_NAME
body:
key: value
Process Results:
Handle the response from the Cloud Function and proceed with the next steps in the Workﬂow,
such as loading data into BigQuery.
Google Cloud Functions Documentation
Using Workﬂows with Cloud Functions
Workﬂows Standard Library

---

### 11. You are migrating a table to BigQuery and are deeding on the data model. Your table stores

information related to purchases made across several store locations and includes information
like the time of the transaction, items purchased, the store ID and the city and state in which the
store is located You frequently query this table to see how many of each item were sold over the
past 30 days and to look at purchasing trends by state city and individual store. You want to
model this table to minimize query time and cost. What should you do?
**Options:**
- Partition by transaction time; cluster by state ﬁrst, then city then store ID
- Partition by transaction tome cluster by store ID ﬁrst, then city, then stale
- Top-level cluster by stale ﬁrst, then city then store
- Top-level cluster by store ID ﬁrst, then city then state.

**Correct Answer:** C

---

