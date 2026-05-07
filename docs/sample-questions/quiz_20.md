# PDE Practice Quiz #20 - May 2026

### 1. You work for an advertising company, and you've developed a Spark ML model to predict click-
through rates at advertisement blocks. You've been developing everything at your on-premises
data center, and now your company is migrating to Google Cloud. Your data center will be
migrated to BigQuery. You periodically retrain your Spark ML models, so you need to migrate
existing training pipelines to Google Cloud. What should you do?
**Options:**
- Use Cloud ML Engine for training existing Spark ML models
- Rewrite your models on TensorFlow, and start using Cloud ML Engine
- Use Cloud Dataproc for training existing Spark ML models, but start reading data directly from
BigQuery
- Spin up a Spark cluster on Compute Engine, and train Spark ML models on the data exported
from BigQuery

**Correct Answer:** C
**Explanation:** https://cloud.google.com/dataproc/docs/tutorials/bigquery-sparkml

---

### 2. A data scientist has created a BigQuery ML model and asks you to create an ML pipeline to serve
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

### 3. You are migrating your data warehouse to BigQuery. You have migrated all of your data into
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

### 4. You have Google Cloud Dataﬂow streaming pipeline running with a Google Cloud Pub/Sub
subscription as the source. You need to make an update to the code that will make the new Cloud
Dataﬂow pipeline incompatible with the current version. You do not want to lose any data when
making this update. What should you do?
**Options:**
- Update the current pipeline and use the drain ﬂag.
- Update the current pipeline and provide the transform mapping JSON object.
- Create a new pipeline that has the same Cloud Pub/Sub subscription and cancel the old
pipeline.
- Create a new pipeline that has a new Cloud Pub/Sub subscription and cancel the old pipeline.

**Correct Answer:** D

---

### 5. You are using Cloud Bigtable to persist and serve stock market data for each of the major indices.
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

### 7. How can you get a neural network to learn about relationships between categories in a
categorical feature?
**Options:**
- Create a multi-hot column
- Create a one-hot column
- Create a hash bucket
- Create an embedding column

**Correct Answer:** D
**Explanation:** There are two problems with one-hot encoding. First, it has high dimensionality, meaning that
instead of having just one value, like a continuous feature, it has many values, or dimensions.
This makes computation more time-consuming, especially if a feature has a very large number of
categories. The second problem is that it doesn't encode any relationships between the
categories. They are completely independent from each other, so the network has no way of
knowing which ones are similar to each other.
Both of these problems can be solved by representing a categorical feature with an embedding
column. The idea is that each category has a smaller vector with, let's say, 5 values in it. But
unlike a one-hot vector, the values are not usually 0. The values are weights, similar to the
weights that are used for basic features in a neural network. The diﬀerence is that each category
has a set of weights (5 of them in this case).
You can think of each value in the embedding vector as a feature of the category. So, if two
categories are very similar to each other, then their embedding vectors should be very similar
too.

---

### 8. You plan to deploy Cloud SQL using MySQL. You need to ensure high availability in the event of a
zone failure. What should you do?
**Options:**
- Create a Cloud SQL instance in one zone, and create a failover replica in another zone within
the same region.
- Create a Cloud SQL instance in one zone, and create a read replica in another zone within the
same region.
- Create a Cloud SQL instance in one zone, and conﬁgure an external read replica in a zone in a
diﬀerent region.
- Create a Cloud SQL instance in a region, and conﬁgure automatic backup to a Cloud Storage
bucket in the same region.

**Correct Answer:** C

---

