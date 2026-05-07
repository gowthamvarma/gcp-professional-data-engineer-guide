# PDE Practice Quiz #19 - May 2026

### 1. Your company built a TensorFlow neutral-network model with a large number of neurons and layers. The model fits well for the training
data. However, when tested against new data, it performs poorly. What method can you employ to address this?
**Options:**
- Threading
- Serialization
- Dropout Methods
- Dimensionality Reduction

**Correct Answer:** C
**Explanation:** Reference https://medium.com/mlreview/a-simple-deep-learning-model-for-stock-price-prediction-using-tensorflow-30505541d877

---

### 2. You are deploying a new storage system for your mobile application, which is a media streaming service. You decide the best fit is
Google Cloud Datastore. You have entities with multiple properties, some of which can take on multiple values. For example, in the
entity ‘Movie’ the property ‘actors’ and the property ‘tags’ have multiple values but the property ‘date released’ does not. A typical query
would ask for all movies with actor= ordered by date_released or all movies with tag=Comedy ordered by date_released. How should
you avoid a combinatorial explosion in the number of indexes?
**Options:**
- Option A
- Option
- C) Option C
- Option D

**Correct Answer:** A

---

### 3. Your company is performing data preprocessing for a learning algorithm in Google Cloud Dataflow. Numerous data logs are being are
being generated during this step, and the team wants to analyze them. Due to the dynamic nature of the campaign, the data is growing
exponentially every hour.
The data scientists have written the following code to read the data for a new key features in the logs.
BigQueryIO.Read
.named(“ReadLogData”)
.from(“clouddataflow-readonly:samples.log_data”)
You want to improve the performance of this data read. What should you do?
**Options:**
- Specify the TableReference object in the code.
- Use .fromQuery operation to read specific fields from the table.
- Use of both the Google BigQuery TableSchema and TableFieldSchema classes.
- Call a transform that returns TableRow objects, where each element in the PCollexction represents a single row in the table.

**Correct Answer:** D

---

### 4. You are working on a sensitive project involving private user data. You have set up a project on Google Cloud Platform to house your
work internally. An external consultant is going to assist with coding a complex transformation in a Google Cloud Dataflow pipeline for
your project. How should you maintain users’ privacy?
**Options:**
- Grant the consultant the Viewer role on the project.
- Grant the consultant the Cloud Dataflow Developer role on the project.
- Create a service account and allow the consultant to log on with it.
- Create an anonymized sample of the data for the consultant to work with in a different project.

**Correct Answer:** C

---

### 5. Your company’s customer and order databases are often under heavy load. This makes performing analytics against them difficult
without harming operations. The databases are in a MySQL cluster, with nightly backups taken using mysqldump. You want to perform
analytics with minimal impact on operations. What should you do?
**Options:**
- Add a node to the MySQL cluster and build an OLAP cube there.
- Use an ETL tool to load the data from MySQL into Google BigQuery.
- Connect an on-premises Apache Hadoop cluster to MySQL and perform ETL.
- Mount the backups to Google Cloud SQL, and then process the data using Google Cloud Dataproc.

**Correct Answer:** C

---

### 6. Flowlogistic’s management has determined that the current Apache Kafka servers cannot handle the data volume for their real-time
inventory tracking system. You need to build a new system on Google Cloud Platform (GCP) that will feed the proprietary tracking
software. The system must be able to ingest data from a variety of global sources, process and query in real-time, and store the data
reliably. Which combination of GCP products should you choose?
**Options:**
- Cloud Pub/Sub, Cloud Dataflow, and Cloud Storage
- Cloud Pub/Sub, Cloud Dataflow, and Local SSD
- Cloud Pub/Sub, Cloud SQL, and Cloud Storage
- Cloud Load Balancing, Cloud Dataflow, and Cloud Storage

**Correct Answer:** C

---

### 7. Flowlogistic’s CEO wants to gain rapid insight into their customer base so his sales team can be better informed in the field. This team is
not very technical, so they’ve purchased a visualization tool to simplify the creation of BigQuery reports. However, they’ve been
overwhelmed by all the data in the table, and are spending a lot of money on queries trying to find the data they need. You want to solve
their problem in the most cost-effective way. What should you do?
**Options:**
- Export the data into a Google Sheet for virtualization.
- Create an additional table with only the necessary columns.
- Create a view on the table to present to the virtualization tool.
- Create identity and access management (IAM) roles on the appropriate columns, so only they appear in a query.

**Correct Answer:** C

---

