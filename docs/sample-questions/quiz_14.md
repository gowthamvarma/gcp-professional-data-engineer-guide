# PDE Practice Quiz #14 - May 2026

### 1. You are implementing a chatbot to help an online retailer streamline their customer service. The
chatbot must be able to respond to both text and voice inquiries. You are looking for a low-code
or no-code option, and you want to be able to easily train the chatbot to provide answers to
keywords. What should you do?
**Options:**
- Use the Speech-to-Text API to build a Python application in App Engine.
- Use the Speech-to-Text API to build a Python application in a Compute Engine instance.
- Use Dialogﬂow for simple queries and the Speech-to-Text API for complex queries.
- Use Dialogﬂow to implement the chatbot. deﬁning the intents based on the most common
queries collected.

**Correct Answer:** D
**Explanation:** Dialogﬂow is a conversational AI platform that allows for easy implementation of chatbots without
needing to code. It has built-in integration for both text and voice input via APIs like Cloud
Speech-to-Text. Deﬁning intents and entity types allows you to map common queries and
keywords to responses. This would provide a low/no-code way to quickly build and iteratively
improve the chatbot capabilities.
https://cloud.google.com/dialogﬂow/docs Dialogﬂow is a natural language understanding platform
that makes it easy to design and integrate a conversational user interface into your mobile app,
web application, device, bot, interactive voice response system, and so on. Using Dialogﬂow, you
can provide new and engaging ways for users to interact with your product. Dialogﬂow can
analyze multiple types of input from your customers, including text or audio inputs (like from a
phone or voice recording). It can also respond to your customers in a couple of ways, either
through text or with synthetic speech.

---

### 2. You operate an IoT pipeline built around Apache Kafka that normally receives around 5000
messages per second. You want to use Google Cloud Platform to create an alert as soon as the
moving average over 1 hour drops below 4000 messages per second. What should you do?
**Options:**
- Consume the stream of data in Cloud Dataﬂow using Kafka IO. Set a sliding time window of 1
hour every 5 minutes. Compute the average when the window closes, and send an alert if the
average is less than 4000 messages.
- Consume the stream of data in Cloud Dataﬂow using Kafka IO. Set a ﬁxed time window of 1
hour. Compute the average when the window closes, and send an alert if the average is less than
4000 messages.
- Use Kafka Connect to link your Kafka message queue to Cloud Pub/Sub. Use a Cloud Dataﬂow
template to write your messages from Cloud Pub/Sub to Cloud Bigtable. Use Cloud Scheduler to
run a script every hour that counts the number of rows created in Cloud Bigtable in the last hour.
If that number falls below 4000, send an alert.
- Use Kafka Connect to link your Kafka message queue to Cloud Pub/Sub. Use a Cloud Dataﬂow
template to write your messages from Cloud Pub/Sub to BigQuery. Use Cloud Scheduler to run a
script every ﬁve minutes that counts the number of rows created in BigQuery in the last hour. If
that number falls below 4000, send an alert.

**Correct Answer:** C

---

### 3. You have terabytes of customer behavioral data streaming from Google Analytics into BigQuery
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

### 5. Your team is working on a binary classiﬁcation problem. You have trained a support vector
machine (SVM) classiﬁer with default parameters, and received an area under the Curve (AUC) of
0.87 on the validation set. You want to increase the AUC of the model. What should you do?
**Options:**
- Perform hyperparameter tuning
- Train a classiﬁer with deep neural networks, because neural networks would always beat SVMs
- Deploy the model and measure the real-world AUC; it's always higher because of
generalization
- Scale predictions you get out of the model (tune a scaling factor as a hyperparameter) in order
to get the highest AUC

**Correct Answer:** A
**Explanation:** https://towardsdatascience.com/understanding-hyperparameters-and-its-optimisation-techniques

-f0debba07568

---

### 6. You are developing a new deep teaming model that predicts a customer's likelihood to buy on
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

### 7. You are running a pipeline in Cloud Dataﬂow that receives messages from a Cloud Pub/Sub topic
and writes the results to a BigQuery dataset in the EU. Currently, your pipeline is located in
europe-west4 and has a maximum of 3 workers, instance type n1-standard-1. You notice that
during peak periods, your pipeline is struggling to process records in a timely fashion, when all 3
workers are at maximum CPU utilization. Which two actions can you take to increase
performance of your pipeline? (Choose two.)
**Options:**
- Increase the number of max workers
- Use a larger instance type for your Cloud Dataﬂow workers
- Change the zone of your Cloud Dataﬂow pipeline to run in us-central1
- Create a temporary table in Cloud Bigtable that will act as a buﬀer for new data. Create a new
step in your pipeline to write to this table ﬁrst, and then create a new pipeline to write from Cloud
Bigtable to BigQuery
- Create a temporary table in Cloud Spanner that will act as a buﬀer for new data. Create a new
step in your pipeline to write to this table ﬁrst, and then create a new pipeline to write from Cloud
Spanner to BigQuery

**Correct Answer:** A, B

---

### 8. You are using Cloud Bigtable to persist and serve stock market data for each of the major indices.
To serve the trading application, you need to access only the most recent stock prices that are
streaming in How should you design your row key and tables to ensure that you can access the
data with the most simple query?
**Options:**
- Create one unique table for all of the indices, and then use the index and timestamp as the
row key design
- Create one unique table for all of the indices, and then use a reverse timestamp as the row
key design.
- For each index, have a separate table and use a timestamp as the row key design
- For each index, have a separate table and use a reverse timestamp as the row key design

**Correct Answer:** A

---

### 9. Diﬀerent teams in your organization store customer and performance data in BigOuery. Each
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

### 10. You want to build a managed Hadoop system as your data lake. The data transformation process
is composed of a series of Hadoop jobs executed in sequence. To accomplish the design of
separating storage from compute, you decided to use the Cloud Storage connector to store all
input data, output data, and intermediary dat
a. However, you noticed that one Hadoop job runs very slowly with Cloud Dataproc, when
compared with the on-premises bare-metal Hadoop environment (8-core nodes with 100-GB
RAM). Analysis shows that this particular Hadoop job is disk I/O intensive. You want to resolve the
issue. What should you do?
**Options:**
- Allocate suﬃcient memory to the Hadoop cluster, so that the intermediary data of that
particular Hadoop job can be held in memory
- Allocate suﬃcient persistent disk space to the Hadoop cluster, and store the intermediate data
of that particular Hadoop job on native HDFS
- Allocate more CPU cores of the virtual machine instances of the Hadoop cluster so that the
networking bandwidth for each instance can scale up
- Allocate additional network interface card (NIC), and conﬁgure link aggregation in the
operating system to use the combined throughput when working with Cloud Storage

**Correct Answer:** A

---

### 11. One of your encryption keys stored in Cloud Key Management Service (Cloud KMS) was exposed.
You need to re-encrypt all of your CMEK-protected Cloud Storage data that used that key. and
then delete the compromised key. You also want to reduce the risk of objects getting written
without customer-managed encryption key (CMEK protection in the future. What should you do?
**Options:**
- Rotate the Cloud KMS key version. Continue to use the same Cloud Storage bucket.
- Create a new Cloud KMS key. Set the default CMEK key on the existing Cloud Storage bucket
to the new one.
- Create a new Cloud KMS key. Create a new Cloud Storage bucket. Copy all objects from the old
bucket to the new one bucket while specifying the new Cloud KMS key in the copy command.
- Create a new Cloud KMS key. Create a new Cloud Storage bucket conﬁgured to use the new
key as the default CMEK key. Copy all objects from the old bucket to the new bucket without
specifying a key.

**Correct Answer:** C
**Explanation:** To re-encrypt all of your CMEK-protected Cloud Storage data after a key has been exposed, and
to ensure future writes are protected with a new key, creating a new Cloud KMS key and a new
Cloud Storage bucket is the best approach. Here's why option C is the best choice:

Re-encryption of Data:
By creating a new Cloud Storage bucket and copying all objects from the old bucket to the new
bucket while specifying the new Cloud KMS key, you ensure that all data is re-encrypted with the
new key.
This process eﬀectively re-encrypts the data, removing any dependency on the compromised
key.
Ensuring CMEK Protection:
Creating a new bucket and setting the new CMEK as the default ensures that all future objects
written to the bucket are automatically protected with the new key.
This reduces the risk of objects being written without CMEK protection.
Deletion of Compromised Key:
Once the data has been copied and re-encrypted, the old key can be safely deleted from Cloud
KMS, eliminating the risk associated with the compromised key.
Steps to Implement:
Create a New Cloud KMS Key:
Create a new encryption key in Cloud KMS to replace the compromised key.
Create a New Cloud Storage Bucket:
Create a new Cloud Storage bucket and set the default CMEK to the new key.
Copy and Re-encrypt Data:
Use the gsutil tool to copy data from the old bucket to the new bucket while specifying the new
CMEK key:
gsutil -o 'GSUtil:gs_json_api_version=2' cp -r gs://old-bucket/* gs://new-bucket/
Delete the Old Key:
After ensuring all data is copied and re-encrypted, delete the compromised key from Cloud KMS.
Cloud KMS Documentation
Cloud Storage Encryption
Re-encrypting Data in Cloud Storage

---

### 12. You are designing a data mesh on Google Cloud with multiple distinct data engineering teams
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

