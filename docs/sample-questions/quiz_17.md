# PDE Practice Quiz #17 - May 2026

### 1. Your company's data platform ingests CSV ﬁle dumps of booking and user proﬁle data from
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

### 2. You have an Oracle database deployed in a VM as part of a Virtual Private Cloud (VPC) network.
You want to replicate and continuously synchronize 50 tables to BigQuery. You want to minimize
the need to manage infrastructure. What should you do?
**Options:**
- Create a Datastream service from Oracle to BigQuery, use a private connectivity conﬁguration
to the same VPC network, and a connection proﬁle to BigQuery.
- Create a Pub/Sub subscription to write to BigQuery directly Deploy the Debezium Oracle
connector to capture changes in the Oracle database, and sink to the Pub/Sub topic.
- Deploy Apache Kafka in the same VPC network, use Kafka Connect Oracle Change Data
Capture (CDC), and Dataﬂow to stream the Kafka topic to BigQuery.
- Deploy Apache Kafka in the same VPC network, use Kafka Connect Oracle change data
capture (CDC), and the Kafka Connect Google BigQuery Sink Connector.

**Correct Answer:** A
**Explanation:** Datastream is a serverless, scalable, and reliable service that enables you to stream data
changes from Oracle and MySQL databases to Google Cloud services such as BigQuery, Cloud

SQL, Google Cloud Storage, and Cloud Pub/Sub. Datastream captures and streams database
changes using change data capture (CDC) technology. Datastream supports private connectivity
to the source and destination systems using VPC networks. Datastream also provides a
connection proﬁle to BigQuery, which simpliﬁes the conﬁguration and management of the data
replication.

---

### 3. You want to store your team's shared tables in a single dataset to make data easily accessible to
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

### 4. You work for a large ecommerce company. You store your customers order data in Bigtable. You
have a garbage collection policy set to delete the data after 30 days and the number of versions
is set to 1. When the data analysts run a query to report total customer spending, the analysts
sometimes see customer data that is older than 30 days. You need to ensure that the analysts do
not see customer data older than 30 days while minimizing cost and overhead. What should you
do?
**Options:**
- Set the expiring values of the column families to 30 days and set the number of versions to 2.
- Use a timestamp range ﬁlter in the query to fetch the customer's data for a speciﬁc range.
- Set the expiring values of the column families to 29 days and keep the number of versions to
1.
- Schedule a job daily to scan the data in the table and delete data older than 30 days.

**Correct Answer:** B
**Explanation:** By using a timestamp range ﬁlter in the query, you can ensure that the analysts only see the
customer data that is within the desired time range, regardless of the garbage collection policy1.
This option is the most cost-eﬀective and simple way to avoid fetching data that is marked for
deletion by garbage collection, as it does not require changing the existing policy or creating
additional jobs.You can use the Bigtable client libraries or the cbt CLI to apply a timestamp range

ﬁlter to your read requests2.
Option A is not eﬀective, as it increases the number of versions to 2, which may cause more data
to be retained and increase the storage costs. Option C is not reliable, as it reduces the expiring
values to 29 days, which may not match the actual data arrival and usage patterns. Option D is
not eﬃcient, as it requires scheduling a job daily to scan and delete the data, which may incur
additional overhead and complexity.Moreover, none of these options guarantee that the data
older than 30 days will be immediately deleted, as garbage collection is an asynchronous process
that can take up to a week to remove the data3.

---

### 5. A data scientist has created a BigQuery ML model and asks you to create an ML pipeline to serve
predictions. You have a REST API application with the requirement to serve predictions for an
individual user ID with latency under 100 milliseconds. You use the following query to generate
predictions: SELECT predicted_label, user_id FROM ML.PREDICT (MODEL 'dataset.model', table
user_features). How should you create the ML pipeline?
**Options:**
- Add a WHERE clause to the query, and grant the BigQuery Data Viewer role to the application
service account.
- Create an Authorized View with the provided query. Share the dataset that contains the view
with the application service account.
- Create a Cloud Dataﬂow pipeline using BigQueryIO to read results from the query. Grant the
Dataﬂow Worker role to the application service account.
- Create a Cloud Dataﬂow pipeline using BigQueryIO to read predictions for all users from the
query. Write the results to Cloud Bigtable using BigtableIO. Grant the Bigtable Reader role to the
application service account so that the application can read predictions for individual users from
Cloud Bigtable.

**Correct Answer:** D

---

### 6. You are migrating an application that tracks library books and information about each book, such
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

### 7. You are running a streaming pipeline with Dataﬂow and are using hopping windows to group the
data as the data arrives. You noticed that some data is arriving late but is not being marked as
late data, which is resulting in inaccurate aggregations downstream. You need to ﬁnd a solution
that allows you to capture the late data in the appropriate window. What should you do?
**Options:**
- Change your windowing function to session windows to deﬁne your windows based on certain
activity.
- Change your windowing function to tumbling windows to avoid overlapping window periods.
- Expand your hopping window so that the late data has more time to arrive within the

grouping.
- Use watermarks to deﬁne the expected data arrival window Allow late data as it arrives.

**Correct Answer:** D
**Explanation:** Watermarks are a way of tracking the progress of time in a streaming pipeline. They are used to
determine when a window can be closed and the results emitted. Watermarks can be either
event-time based or processing-time based. Event-time watermarks track the progress of time
based on the timestamps of the data elements, while processing-time watermarks track the
progress of time based on the system clock. Event-time watermarks are more accurate, but they
require the data source to provide reliable timestamps. Processing-time watermarks are simpler,
but they can be aﬀected by system delays or backlogs.
By using watermarks, you can deﬁne the expected data arrival window for each windowing
function. You can also specify how to handle late data, which is data that arrives after the
watermark has passed. You can either discard late data, or allow late data and update the results
as new data arrives. Allowing late data requires you to use triggers to control when the results
are emitted.
In this case, using watermarks and allowing late data is the best solution to capture the late data
in the appropriate window. Changing the windowing function to session windows or tumbling
windows will not solve the problem of late data, as they still rely on watermarks to determine
when to close the windows. Expanding the hopping window might reduce the amount of late
data, but it will also change the semantics of the windowing function and the results.
Streaming pipelines | Cloud Dataﬂow | Google Cloud
Windowing | Apache Beam

---

### 8. You issue a new batch job to Dataﬂow. The job starts successfully, processes a few elements, and
then suddenly fails and shuts down. You navigate to the Dataﬂow monitoring interface where you
ﬁnd errors related to a particular DoFn in your pipeline. What is the most likely cause of the
errors?
**Options:**
- Exceptions in worker code
- Job validation
- Graph or pipeline construction
- Insuﬃcient permissions

**Correct Answer:** A
**Explanation:** https://cloud.google.com/dataﬂow/docs/guides/troubleshooting-your-pipeline#detect_an_exceptio
n_in_worker_code While your job is running, you might encounter errors or exceptions in your
worker code. These errors generally mean that the DoFns in your pipeline code have generated
unhandled exceptions, which result in failed tasks in your Dataﬂow job. Exceptions in user code
(for example, your DoFn instances) are reported in the Dataﬂow monitoring interface.

---

### 9. You are migrating your on-premises data warehouse to BigQuery. As part of the migration, you
want to facilitate cross-team collaboration to get the most value out of the organization's dat
a. You need to design an architecture that would allow teams within the organization to securely
publish, discover, and subscribe to read-only data in a self-service manner. You need to minimize
costs while also maximizing data freshness What should you do?
**Options:**
- Create authorized datasets to publish shared data in the subscribing team's project.
- Create a new dataset for sharing in each individual team's project. Grant the subscribing team
the bigquery. dataViewer role on the
dataset.
- Use BigQuery Data Transfer Service to copy datasets to a centralized BigQuery project for
sharing.
- Use Analytics Hub to facilitate data sharing.

**Correct Answer:** C
**Explanation:** To provide a cost-eﬀective storage and processing solution that allows data scientists to explore
data similarly to using the on-premises HDFS cluster with SQL on the Hive query engine,
deploying a Dataproc cluster is the best choice. Here's why:
Compatibility with Hive:
Dataproc is a fully managed Apache Spark and Hadoop service that provides native support for
Hive, making it easy for data scientists to run SQL queries on the data as they would in an on-
premises Hadoop environment.
This ensures that the transition to Google Cloud is smooth, with minimal changes required in the
workﬂow.
Cost-Eﬀective Storage:
Storing the ORC ﬁles in Cloud Storage is cost-eﬀective and scalable, providing a reliable and
durable storage solution that integrates seamlessly with Dataproc.
Cloud Storage allows you to store large datasets at a lower cost compared to other storage
options.
Hive Integration:
Dataproc supports running Hive directly, which is essential for data scientists familiar with SQL on
the Hive query engine.
This setup enables the use of existing Hive queries and scripts without signiﬁcant modiﬁcations.
Steps to Implement:
Copy ORC Files to Cloud Storage:
Transfer the ORC ﬁles from the on-premises HDFS cluster to Cloud Storage, ensuring they are
organized in a similar directory structure.
Deploy Dataproc Cluster:
Set up a Dataproc cluster conﬁgured to run Hive. Ensure that the cluster has access to the ORC
ﬁles stored in Cloud Storage.
Conﬁgure Hive:
Conﬁgure Hive on Dataproc to read from the ORC ﬁles in Cloud Storage. This can be done by
setting up external tables in Hive that point to the Cloud Storage location.

Provide Access to Data Scientists:
Grant the data scientist team access to the Dataproc cluster and the necessary permissions to
interact with the Hive tables.
Dataproc Documentation
Hive on Dataproc
Google Cloud Storage Documentation

---

### 10. You are working on a linear regression model on BigQuery ML to predict a customer's likelihood
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

### 11. Your organization has two Google Cloud projects, project A and project B. In project A, you have a
Pub/Sub topic that receives data from conﬁdential sources. Only the resources in project A should
be able to access the data in that topic. You want to ensure that project B and any future project

cannot access data in the project A topic. What should you do?
**Options:**
- Conﬁgure VPC Service Controls in the organization with a perimeter around the VPC of project
- B- Add ﬁrewall rules in project A so only traﬃc from the VPC in project A is permitted.
- Conﬁgure VPC Service Controls in the organization with a perimeter around project
- D- Use Identity and Access Management conditions to ensure that only users and service
accounts in project A can access resources in project.

**Correct Answer:** C
**Explanation:** Identity and Access Management (IAM) is the recommended way to control access to Pub/Sub
resources, such as topics and subscriptions. IAM allows you to grant roles and permissions to
users and service accounts at the project level or the individual resource level. You can also use
IAM conditions to specify additional attributes for granting or denying access, such as time, date,
or origin. By using IAM conditions, you can ensure that only the resources in project A can access
the data in the project A topic, regardless of the network conﬁguration or the VPC Service
Controls. You can also prevent project B and any future project from accessing the data in the
project A topic by not granting them any roles or permissions on the topic.
Option A is not a good solution, as VPC Service Controls are designed to prevent data exﬁltration
from Google Cloud resources to the public internet, not to control access between Google Cloud
projects. VPC Service Controls create a perimeter around the resources of one or more projects,
and restrict the communication with resources outside the perimeter. However, VPC Service
Controls do not apply to Pub/Sub, as Pub/Sub is not associated with any speciﬁc IP address or VPC
network. Therefore, conﬁguring VPC Service Controls with a perimeter around the VPC of project
A would not prevent project B or any future project from accessing the data in the project A topic,
if they have the necessary IAM roles and permissions.
Option B is not a good solution, as ﬁrewall rules are used to control the ingress and egress traﬃc
to and from the VPC network of a project. Firewall rules do not apply to Pub/Sub, as Pub/Sub is
not associated with any speciﬁc IP address or VPC network. Therefore, adding ﬁrewall rules in
project A to only permit traﬃc from the VPC in project A would not prevent project B or any future
project from accessing the data in the project A topic, if they have the necessary IAM roles and
permissions.
Option C is not a good solution, as VPC Service Controls are designed to prevent data exﬁltration
from Google Cloud resources to the public internet, not to control access between Google Cloud

projects. VPC Service Controls create a perimeter around the resources of one or more projects,
and restrict the communication with resources outside the perimeter. However, VPC Service
Controls do not apply to Pub/Sub, as Pub/Sub is not associated with any speciﬁc IP address or VPC
network. Therefore, conﬁguring VPC Service Controls with a perimeter around project A would not
prevent project B or any future project from accessing the data in the project A topic, if they have
the necessary IAM roles and permissions.

---

