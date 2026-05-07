# PDE Practice Quiz #21 - May 2026

### 1. An online brokerage company requires a high volume trade processing architecture. You need to
create a secure queuing system that triggers jobs. The jobs will run in Google Cloud and cat the
company's Python API to execute trades. You need to eﬃciently implement a solution. What
should you do?
**Options:**
- Use Cloud Composer to subscribe to a Pub/Sub tope and can the Python API.
- Use a Pub/Sub push subscription to trigger a Cloud Function to pass the data to tie Python API.
- Write an application that makes a queue in a NoSQL database
- Write an application hosted on a Compute Engine instance that makes a push subscription to
the Pub/Sub topic

**Correct Answer:** C

---

### 2. You use a dataset in BigQuery for analysis. You want to provide third-party companies with
access to the same dataset. You need to keep the costs of data sharing low and ensure that the
data is current. Which solution should you choose?
**Options:**
- Create an authorized view on the BigQuery table to control data access, and provide third-
party companies with access to that view.
- Use Cloud Scheduler to export the data on a regular basis to Cloud Storage, and provide third-
party companies with access to the bucket.
- Create a separate dataset in BigQuery that contains the relevant data to share, and provide
third-party companies with access to the new dataset.
- Create a Cloud Dataﬂow job that reads the data in frequent time intervals, and writes it to the
relevant BigQuery dataset or Cloud Storage bucket for third-party companies to use.

**Correct Answer:** B

---

### 3. You are planning to use Google's Dataﬂow SDK to analyze customer data such as displayed
below. Your project requirement is to extract only the customer name from the data source and
then write to an output PCollection.
Tom,555 X street
Tim,553 Y street
Sam, 111 Z street
Which operation is best suited for the above data processing requirement?
**Options:**
- ParDo
- Sink API
- Source API
- Data extraction

**Correct Answer:** A
**Explanation:** In Google Cloud dataﬂow SDK, you can use the ParDo to extract only a customer name of each
element in your PCollection.

---

### 4. Cloud Bigtable is Google's ______ Big Data database service.
**Options:**
- Relational
- mySQL
- NoSQL
- SQL Server

**Correct Answer:** C
**Explanation:** Cloud Bigtable is Google's NoSQL Big Data database service. It is the same database that Google
uses for services, such as Search, Analytics, Maps, and Gmail.
It is used for requirements that are low latency and high throughput including Internet of Things
(IoT), user analytics, and ﬁnancial data analysis.

---

### 5. Flowlogistic's CEO wants to gain rapid insight into their customer base so his sales team can be
better informed in the ﬁeld. This team is not very technical, so they've purchased a visualization
tool to simplify the creation of BigQuery reports. However, they've been overwhelmed by all the
data in the table, and are spending a lot of money on queries trying to ﬁnd the data they need.
You want to solve their problem in the most cost-eﬀective way. What should you do?
**Options:**
- Export the data into a Google Sheet for virtualization.
- Create an additional table with only the necessary columns.
- Create a view on the table to present to the virtualization tool.
- Create identity and access management (IAM) roles on the appropriate columns, so only they
appear in a query.

**Correct Answer:** C

---

### 6. Cloud Bigtable is a recommended option for storing very large amounts of
____________________________?
**Options:**
- multi-keyed data with very high latency
- multi-keyed data with very low latency
- single-keyed data with very low latency
- single-keyed data with very high latency

**Correct Answer:** C
**Explanation:** Cloud Bigtable is a sparsely populated table that can scale to billions of rows and thousands of
columns, allowing you to store terabytes or even petabytes of data. A single value in each row is
indexed; this value is known as the row key. Cloud Bigtable is ideal for storing very large
amounts of single-keyed data with very low latency. It supports high read and write throughput at
low latency, and it is an ideal data source for MapReduce operations.

---

### 7. Which option operations can you perform from the BigQuery Web UI?
**Options:**
- Upload a ﬁle in SQL format.
- Load data with nested and repeated ﬁelds.
- Upload a 20 MB ﬁle.
- Upload multiple ﬁles using a wildcard.

**Correct Answer:** B
**Explanation:** You can load data with nested and repeated ﬁelds using the Web UI.
You cannot use the Web UI to:
- Upload a ﬁle greater than 10 MB in size
- Upload multiple ﬁles at the same time
- Upload a ﬁle in SQL format
All three of the above operations can be performed using the 'bq' command.

---

### 8. The Dataﬂow SDKs have been recently transitioned into which Apache service?
**Options:**
- Apache Spark
- Apache Hadoop
- Apache Kafka
- Apache Beam

**Correct Answer:** D
**Explanation:** Dataﬂow SDKs are being transitioned to Apache Beam, as per the latest Google directive

---

### 9. You need to create a data pipeline that copies time-series transaction data so that it can be
queried from within BigQuery by your data science team for analysis. Every hour, thousands of
transactions are updated with a new status. The size of the intitial dataset is 1.5 PB, and it will
grow by 3 TB per day. The data is heavily structured, and your data science team will build
machine learning models based on this dat
a. You want to maximize performance and usability for your data science team. Which two
strategies should you adopt? Choose 2 answers.
**Options:**
- Denormalize the data as must as possible.
- Preserve the structure of the data as much as possible.
- Use BigQuery UPDATE to further reduce the size of the dataset.
- Develop a data pipeline where status updates are appended to BigQuery instead of updated.
- Copy a daily snapshot of transaction data to Cloud Storage and store it as an Avro ﬁle. Use
BigQuery's support for external data sources to query.

**Correct Answer:** A, E

---

