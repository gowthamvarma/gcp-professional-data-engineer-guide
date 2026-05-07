# PDE Practice Quiz #6 - May 2026

### 1. These primary tool in use, and the data format is Optimized Row Columnar (ORC). All ORC files have been successfully copied to a
Cloud Storage bucket. You need to replicate some data to the cluster's local Hadoop Distributed File System (HDFS) to maximize
performance. What are two ways to start using Hive in Cloud Dataproc? (Choose two.)
**Options:**
- Run the gsutil utility to transfer all ORC files from the Cloud Storage bucket to HDFS. Mount the Hive tables locally.
- Run the gsutil utility to transfer all ORC files from the Cloud Storage bucket to any node of the Dataproc cluster. Mount the Hive
tables locally.
- Run the gsutil utility to transfer all ORC files from the Cloud Storage bucket to the master node of the Dataproc cluster. Then run the
Hadoop utility to copy them do HDFS. Mount the Hive tables from HDFS.
- Leverage Cloud Storage connector for Hadoop to mount the ORC files as external Hive tables. Replicate external Hive tables to the
native ones.
- Load the ORC files into BigQuery. Leverage BigQuery connector for Hadoop to mount the BigQuery tables as external Hive tables.
Replicate external Hive tables to the native ones.

**Correct Answer:** B, C

---

### 2. You have uploaded 5 years of log data to Cloud Storage A user reported that some data points in the log data are outside of their
expected ranges, which indicates errors You need to address this issue and be able to run the process again in the future while keeping
the original data for compliance reasons What should you do?
**Options:**
- Import the data from Cloud Storage into BigQuery Create a new BigQuery table, and skip the rows with errors.
- Create a Compute Engine instance and create a new copy of the data in Cloud Storage Skip the rows with errors
- Create a Cloud Dataflow workflow that reads the data from Cloud Storage, checks for values outside the expected range, sets the
value to an appropriate default, and writes the updated records to a new dataset in
Cloud Storage
- Create a Cloud Dataflow workflow that reads the data from Cloud Storage, checks for values outside the expected range, sets the
value to an appropriate default, and writes the updated records to the same dataset in Cloud Storage

**Correct Answer:** C

---

### 3. MJTelco’s Google Cloud Dataflow pipeline is now ready to start receiving data from the 50,000 installations. You want to allow Cloud
Dataflow to scale its compute power up as required. Which Cloud Dataflow pipeline configuration setting should you update?
**Options:**
- The zone
- The number of workers
- The disk size per worker
- The maximum number of workers

**Correct Answer:** A

---

### 4. You are designing the database schema for a machine learning-based food ordering service that will predict what users want to eat.
Here is some of the information you need to store:
The user profile: What the user likes and doesn’t like to eat
The user account information: Name, address, preferred meal times
The order information: When orders are made, from where, to whom
The database will be used to store all the transactional data of the product. You want to optimize the data schem
a. Which Google Cloud Platform product should you use?
**Options:**
- BigQuery
- Cloud SQL
- Cloud Bigtable
- Cloud Datastore

**Correct Answer:** A

---

### 5. Suppose you have a table that includes a nested column called "city" inside a column called "person", but when you try to submit the
following query in BigQuery, it gives you an error.
SELECT person FROM `project1.example.table1` WHERE city = "London"
How would you correct the error?
**Options:**
- Add ', UNNEST(person)' before the WHERE clause.
- Change 'person' to 'person.city'.
- Change 'person' to 'city.person'.
- Add ', UNNEST(city)' before the WHERE clause.

**Correct Answer:** A

---

### 6. You are integrating one of your internal IT applications and Google BigQuery, so users can query BigQuery from the application’s
interface. You do not want individual users to authenticate to BigQuery and you do not want to give them access to the dataset. You
need to securely access BigQuery from your IT application.
What should you do?
**Options:**
- Create groups for your users and give those groups access to the dataset
- Integrate with a single sign-on (SSO) platform, and pass each user's credentials along with the query
request
- Create a service account and grant dataset access to that account. Use the service account's private key to access the dataset
- Create a dummy user and grant dataset access to that user. Store the username and password for that user in a file on the files
system, and use those credentials to access the BigQuery dataset

**Correct Answer:** C

---

### 7. Your company is using WHILECARD tables to query data across multiple tables with similar names. The SQL statement is currently
failing with the following error:
# Syntax error : Expected end of statement but got “-“ at [4:11]
SELECT age
FROM
bigquery-public-data.noaa_gsod.gsod
WHERE
age != 99
AND_TABLE_SUFFIX = ‘1929’
ORDER BY
age DESC
Which table name will make the SQL statement work correctly?
**Options:**
- 'bigquery-public-data.noaa_gsod.gsod'
- bigquery-public-data.noaa_gsod.gsod*
- 'bigquery-public-data.noaa_gsod.gsod'*
- 'bigquery-public-data.noaa_gsod.gsod*`

**Correct Answer:** B

---

### 8. Your company’s on-premises Apache Hadoop servers are approaching end-of-life, and IT has decided to migrate the cluster to Google
Cloud Dataproc. A like-for-like migration of the cluster would require 50 TB of Google Persistent Disk per node. The CIO is concerned
about the cost of using that much block storage. You want to minimize the storage cost of the migration. What should you do?
**Options:**
- Put the data into Google Cloud Storage.
- Use preemptible virtual machines (VMs) for the Cloud Dataproc cluster.
- Tune the Cloud Dataproc cluster so that there is just enough disk for all data.
- Migrate some of the cold data into Google Cloud Storage, and keep only the hot data in Persistent Disk.

**Correct Answer:** B

---

