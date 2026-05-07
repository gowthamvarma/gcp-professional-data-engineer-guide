# PDE Practice Quiz #23 - May 2026

### 1. You've migrated a Hadoop job from an on-premises cluster to Dataproc and Good Storage. Your
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

### 2. You have a data pipeline with a Dataﬂow job that aggregates and writes time series metrics to
Bigtable. You notice that data is slow to update in Bigtable. This data feeds a dashboard used by
thousands of users across the organization. You need to support additional concurrent users and
reduce the amount of time required to write the dat
a. What should you do?
Choose 2 answers
**Options:**
- Conﬁgure your Dataﬂow pipeline to use local execution.
- Modify your Dataﬂow pipeline lo use the Flatten transform before writing to Bigtable.
- Modify your Dataﬂow pipeline to use the CoGrcupByKey transform before writing to Bigtable.
- Increase the maximum number of Dataﬂow workers by setting maxNumWorkers in
PipelineOptions.
- Increase the number of nodes in the Bigtable cluster.

**Correct Answer:** D, E
**Explanation:** https://cloud.google.com/bigtable/docs/performance#performance-write-throughput
https://cloud.google.com/dataﬂow/docs/reference/pipeline-options

---

### 3. You are conﬁguring networking for a Dataﬂow job. The data pipeline uses custom container
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

### 4. Your company currently runs a large on-premises cluster using Spark Hive and Hadoop
Distributed File System (HDFS) in a colocation facility. The duster is designed to support peak
usage on the system, however, many jobs are batch n nature, and usage of the cluster ﬂuctuates
quite dramatically.
Your company is eager to move to the cloud to reduce the overhead associated with on-premises
infrastructure and maintenance and to beneﬁt from the cost savings. They are also hoping to
modernize their existing infrastructure to use more servers oﬀerings m order to take advantage
of the cloud Because of the tuning of their contract renewal with the colocation facility they have
only 2 months for their initial migration How should you recommend they approach thee
upcoming migration strategy so they can maximize their cost savings in the cloud will still
executing the migration in time?
**Options:**
- Migrate the workloads to Dataproc plus HOPS, modernize later
- Migrate the workloads to Dataproc plus Cloud Storage modernize later
- Migrate the Spark workload to Dataproc plus HDFS, and modernize the Hive workload for
BigQuery
- Modernize the Spark workload for Dataﬂow and the Hive workload for BigQuery

**Correct Answer:** D

---

### 5. You are implementing a chatbot to help an online retailer streamline their customer service. The
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

### 6. You are building an ELT solution in BigQuery by using Dataform. You need to perform uniqueness
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

