# PDE Practice Quiz #15 - May 2026

### 1. You work for a mid-sized enterprise that needs to move its operational system transaction data
from an on-premises database to GCP. The database is about 20 TB in size. Which database
should you choose?
**Options:**
- Cloud SQL
- Cloud Bigtable
- Cloud Spanner
- Cloud Datastore

**Correct Answer:** A

---

### 2. You need to deploy additional dependencies to all of a Cloud Dataproc cluster at startup using an
existing initialization action. Company security policies require that Cloud Dataproc nodes do not
have access to the Internet so public initialization actions cannot fetch resources. What should
you do?
**Options:**
- Deploy the Cloud SQL Proxy on the Cloud Dataproc master
- Use an SSH tunnel to give the Cloud Dataproc cluster access to the Internet
- Copy all dependencies to a Cloud Storage bucket within your VPC security perimeter
- Use Resource Manager to add the service account used by the Cloud Dataproc cluster to the
Network User role

**Correct Answer:** C

---

### 3. You need to migrate a Redis database from an on-premises data center to a Memorystore for
Redis instance. You want to follow Google-recommended practices and perform the migration for
minimal cost. time, and eﬀort. What should you do?
**Options:**
- Make a secondary instance of the Redis database on a Compute Engine instance, and then
perform a live cutover.
- Write a shell script to migrate the Redis data, and create a new Memorystore for Redis
instance.
- Create a Dataﬂow job to road the Redis database from the on-premises data center. and write
the data to a Memorystore for Redis instance
- Make an RDB backup of the Redis database, use the gsutil utility to copy the RDB ﬁle into a
Cloud Storage bucket, and then import the RDB tile into the Memorystore for Redis instance.

**Correct Answer:** D
**Explanation:** The import and export feature uses the native RDB snapshot feature of Redis to import data into
or export data out of a Memorystore for Redis instance. The use of the native RDB format
prevents lock-in and makes it very easy to move data within Google Cloud or outside of Google
Cloud. Import and export uses Cloud Storage buckets to store RDB ﬁles.

---

### 4. You need to create a new transaction table in Cloud Spanner that stores product sales dat
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

### 5. You need to look at BigQuery data from a speciﬁc table multiple times a day. The underlying
table you are querying is several petabytes in size, but you want to ﬁlter your data and provide
simple aggregations to downstream users. You want to run queries faster and get up-to-date
insights quicker. What should you do?
**Options:**
- Run a scheduled query to pull the necessary data at speciﬁc intervals daily.
- Create a materialized view based oﬀ of the query being run.
- Use a cached query to accelerate time to results.
- Limit the query columns being pulled in the ﬁnal result.

**Correct Answer:** A
**Explanation:** Materialized views are precomputed views that periodically cache the results of a query for
increased performance and eﬃciency. BigQuery leverages precomputed results from
materialized views and whenever possible reads only changes from the base tables to compute
up-to-date results. Materialized views can signiﬁcantly improve the performance of workloads
that have the characteristic of common and repeated queries. Materialized views can also
optimize queries with high computation cost and small dataset results, such as ﬁltering and
aggregating large tables. Materialized views are refreshed automatically when the base tables
change, so they always return fresh data. Materialized views can also be used by the BigQuery

optimizer to process queries to the base tables, if any part of the query can be resolved by
querying the materialized view.

---

### 6. You've migrated a Hadoop job from an on-premises cluster to Dataproc and Good Storage. Your
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

### 7. You are migrating an application that tracks library books and information about each book, such
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

### 8. You are working on a linear regression model on BigQuery ML to predict a customer's likelihood
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

### 9. You have terabytes of customer behavioral data streaming from Google Analytics into BigQuery
daily Your customers' information, such as their preferences, is hosted on a Cloud SQL for MySQL
database Your CRM database is hosted on a Cloud SQL for PostgreSQL instance. The marketing
team wants to use your customers' information from the two databases and the customer
behavioral data to create marketing campaigns for yearly active customers. You need to ensure
that the marketing team can run the campaigns over 100 times a day on typical days and up to
300 during sales. At the same time you want to keep the load on the Cloud SQL databases to a
minimum. What should you do?
**Options:**
- Create BigQuery connections to both Cloud SQL databases Use BigQuery federated queries on
the two databases and the Google Analytics data on BigQuery to run these queries.
- Create streams in Datastream to replicate the required tables from both Cloud SQL databases
to BigQuery for these queries.
- Create a Dataproc cluster with Trino to establish connections to both Cloud SQL databases and
BigQuery, to execute the queries.
- Create a job on Apache Spark with Dataproc Serverless to query both Cloud SQL databases
and the Google Analytics data on BigQuery for these queries.

**Correct Answer:** B
**Explanation:** Datastream is a serverless Change Data Capture (CDC) and replication service that allows you to
stream data changes from Oracle and MySQL databases to Google Cloud services such as
BigQuery, Cloud Storage, Cloud SQL, and Pub/Sub. Datastream captures and delivers database
changes in real-time, with minimal impact on the source database performance. Datastream also
preserves the schema and data types of the source database, and automatically creates and
updates the corresponding tables in BigQuery.
By using Datastream, you can replicate the required tables from both Cloud SQL databases to
BigQuery, and keep them in sync with the source databases. This way, you can reduce the load
on the Cloud SQL databases, as the marketing team can run their queries on the BigQuery tables
instead of the Cloud SQL tables. You can also leverage the scalability and performance of

BigQuery to query the customer behavioral data from Google Analytics and the customer
information from the replicated tables. You can run the queries as frequently as needed, without
worrying about the impact on the Cloud SQL databases.
Option A is not a good solution, as BigQuery federated queries allow you to query external data
sources such as Cloud SQL databases, but they do not reduce the load on the source databases.
In fact, federated queries may increase the load on the source databases, as they need to
execute the query statements on the external data sources and return the results to BigQuery.
Federated queries also have some limitations, such as data type mappings, quotas, and
performance issues.
Option C is not a good solution, as creating a Dataproc cluster with Trino would require more
resources and management overhead than using Datastream. Trino is a distributed SQL query
engine that can connect to multiple data sources, such as Cloud SQL and BigQuery, and execute
queries across them. However, Trino requires a Dataproc cluster to run, which means you need to
provision, conﬁgure, and monitor the cluster nodes. You also need to install and conﬁgure the
Trino connector for Cloud SQL and BigQuery, and write the queries in Trino SQL dialect. Moreover,
Trino does not replicate or sync the data from Cloud SQL to BigQuery, so the load on the Cloud
SQL databases would still be high.
Option D is not a good solution, as creating a job on Apache Spark with Dataproc Serverless
would require more coding and processing power than using Datastream. Apache Spark is a
distributed data processing framework that can read and write data from various sources, such
as Cloud SQL and BigQuery, and perform complex transformations and analytics on them.
Dataproc Serverless is a serverless Spark service that allows you to run Spark jobs without
managing clusters. However, Spark requires you to write code in Python, Scala, Java, or R, and
use the Spark connector for Cloud SQL and BigQuery to access the data sources. Spark also does
not replicate or sync the data from Cloud SQL to BigQuery, so the load on the Cloud SQL
databases would still be high.

---

### 10. You are creating a data model in BigQuery that will hold retail transaction dat
a. Your two largest tables, sales_transation_header and sales_transation_line. have a tightly
coupled immutable relationship. These tables are rarely modiﬁed after load and are frequently
joined when queried. You need to model the sales_transation_header and sales_transation_line
tables to improve the performance of data analytics queries. What should you do?
**Options:**
- Create a sal es_transaction table that Stores the sales_tran3action_header and
sales_transaction_line data as a JSON data type.
- Create a sale3_transaction table that holds the sales_transaction_header information as rows
and the
sales_transaction_line rows as nested and repeated ﬁelds.
- Create a sale_transaction table that holds the sales_transaction_header and
sales_transaction_line information as rows, duplicating the sales_transaction_header data for
each line.
- Create separate sales_transation_header and sales_transation_line tables and. when querying,
specify the sales transition line ﬁrst in the WHERE clause.

**Correct Answer:** B
**Explanation:** BigQuery supports nested and repeated ﬁelds, which are complex data types that can represent
hierarchical and one-to-many relationships within a single table. By using nested and repeated
ﬁelds, you can denormalize your data model and reduce the number of joins required for your
queries. This can improve the performance and eﬃciency of your data analytics queries, as joins
can be expensive and require shuﬄing data across nodes. Nested and repeated ﬁelds also
preserve the data integrity and avoid data duplication. In this scenario, the
sales_transaction_header and sales_transaction_line tables have a tightly coupled immutable
relationship, meaning that each header row corresponds to one or more line rows, and the data is
rarely modiﬁed after load. Therefore, it makes sense to create a single sales_transaction table
that holds the sales_transaction_header information as rows and the sales_transaction_line rows
as nested and repeated ﬁelds. This way, you can query the sales transaction data without joining
two tables, and use dot notation or array functions to access the nested and repeated ﬁelds. For
example, the sales_transaction table could have the following schema:
Table
Field name
Type
Mode
id
INTEGER
NULLABLE

order_time
TIMESTAMP
NULLABLE
customer_id
INTEGER
NULLABLE
line_items
RECORD
REPEATED
line_items.sku
STRING
NULLABLE
line_items.quantity
INTEGER
NULLABLE
line_items.price
FLOAT
NULLABLE
To query the total amount of each order, you could use the following SQL statement:
SQL
SELECT id, SUM(line_items.quantity * line_items.price) AS total_amount
FROM sales_transaction
GROUP BY id;
AI-generated code. Review and use carefully.More info on FAQ.
Use nested and repeated ﬁelds
BigQuery explained: Working with joins, nested & repeated data
Arrays in BigQuery --- How to improve query performance and optimise storage

---

### 11. You have a table that contains millions of rows of sales data, partitioned by date Various
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

### 12. You are building a report-only data warehouse where the data is streamed into BigQuery via the
streaming API Following Google's best practices, you have both a staging and a production table
for the data How should you design your data loading to ensure that there is only one master
dataset without aﬀecting performance on either the ingestion or reporting pieces?
**Options:**
- Have a staging table that is an append-only model, and then update the production table
every three hours
with the changes written to staging
- Have a staging table that is an append-only model, and then update the production table
every ninety
minutes with the changes written to staging
- Have a staging table that moves the staged data over to the production table and deletes the
contents of the
staging table every three hours
- Have a staging table that moves the staged data over to the production table and deletes the
contents of the staging table every thirty minutes

**Correct Answer:** D

---

