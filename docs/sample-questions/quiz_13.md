# PDE Practice Quiz #13 - May 2026

### 1. You are developing an Apache Beam pipeline to extract data from a Cloud SQL instance by using JdbclO. You have two projects
running in Google Cloud. The pipeline will be deployed and executed on Dataflow in Project
**Options:**
- The Cloud SQL instance is running jn Project B and does not have a public IP address. After deploying the pipeline, you noticed that
the pipeline failed to extract data from the Cloud SQL instance due to connection failure. You verified that VPC Service Controls and
shared VPC are not in use in these projects. You want to resolve this error while ensuring that the data does not go through the public
internet. What should you do?
- Set up VPC Network Peering between Project A and Project
- Add a firewall rule to allow the peered subnet range to access all
instances on the network.
- Turn off the external IP addresses on the Dataflow worker. Enable Cloud NAT in Project
- C) Set up VPC Network Peering between Project A and Project
- Create a Compute Engine instance without external IP address in
Project B on the peered subnet to serve as a proxy server to the Cloud SQL database.
- Add the external IP addresses of the Dataflow worker as authorized networks in the Cloud SOL instance.

**Correct Answer:** C
**Explanation:** Option A is incorrect because VPC Network Peering alone does not enable connectivity to Cloud SQL instances with private IP
addresses.You also need to configure private services access and allocate an IP address range for the service producer network1.
Option B is incorrect because Cloud NAT does not support Cloud SQL instances with private IP addresses.Cloud NAT only provides
outbound connectivity for resources that do not have public IP addresses, such as VMs, GKE clusters, and serverless instances2.
Option C is correct because it allows you to use a Compute Engine instance as a proxy server to connect to the Cloud SQL database
over the peered network. The proxy server does not need an external IP address because it can communicate with the Dataflow workers
and the Cloud SQL instance using internal IP addresses. You need to install the Cloud SQL Auth proxy on the proxy server and
configure it to use a service account that has the Cloud SQL Client role.
Option D is incorrect because it requires you to assign public IP addresses to the Dataflow workers, which exposes the data to the public
internet. This violates the requirement of ensuring that the data does not go through the public internet. Moreover, adding authorized
networks does not work for Cloud SQL instances with private IP addresses.

---

### 2. Your company built a TensorFlow neutral-network model with a large number of neurons and layers. The model fits well for the training
data. However, when tested against new data, it performs poorly. What method can you employ to address this?
**Options:**
- Threading
- Serialization
- Dropout Methods
- Dimensionality Reduction

**Correct Answer:** C
**Explanation:** Reference https://medium.com/mlreview/a-simple-deep-learning-model-for-stock-price-prediction-using-tensorflow-30505541d877

---

### 3. Suppose you have a table that includes a nested column called "city" inside a column called "person", but when you try to submit the
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

### 4. You are deploying a new storage system for your mobile application, which is a media streaming service. You decide the best fit is
Google Cloud Datastore. You have entities with multiple properties, some of which can take on multiple values. For example, in the
entity ‘Movie’ the property ‘actors’ and the property ‘tags’ have multiple values but the property ‘date released’ does not. A typical query
would ask for all movies with actor= ordered by date_released or all movies with tag=Comedy ordered by date_released. How should
you avoid a combinatorial explosion in the number of indexes?
Image not found or type unknown
Image not found or type unknown
**Options:**
- Option A
- Option
- C) Option C
- Option D

**Correct Answer:** A

---

### 5. You are designing the database schema for a machine learning-based food ordering service that will predict what users want to eat.
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

### 6. Your company’s customer and order databases are often under heavy load. This makes performing analytics against them difficult
without harming operations. The databases are in a MySQL cluster, with nightly backups taken using mysqldump. You want to perform
analytics with minimal impact on operations. What should you do?
**Options:**
- Add a node to the MySQL cluster and build an OLAP cube there.
- Use an ETL tool to load the data from MySQL into Google BigQuery.
- Connect an on-premises Apache Hadoop cluster to MySQL and perform ETL.
- Mount the backups to Google Cloud SQL, and then process the data using Google Cloud Dataproc.

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

### 8. You are developing an Apache Beam pipeline to extract data from a Cloud SQL instance by using JdbclO. You have two projects
running in Google Cloud. The pipeline will be deployed and executed on Dataflow in Project
**Options:**
- The Cloud SQL instance is running jn Project B and does not have a public IP address. After deploying the pipeline, you noticed that
the pipeline failed to extract data from the Cloud SQL instance due to connection failure. You verified that VPC Service Controls and
shared VPC are not in use in these projects. You want to resolve this error while ensuring that the data does not go through the public
internet. What should you do?
- Set up VPC Network Peering between Project A and Project
- Add a firewall rule to allow the peered subnet range to access all
instances on the network.
- Turn off the external IP addresses on the Dataflow worker. Enable Cloud NAT in Project
- C) Set up VPC Network Peering between Project A and Project
- Create a Compute Engine instance without external IP address in
Project B on the peered subnet to serve as a proxy server to the Cloud SQL database.
- Add the external IP addresses of the Dataflow worker as authorized networks in the Cloud SOL instance.

**Correct Answer:** C
**Explanation:** Option A is incorrect because VPC Network Peering alone does not enable connectivity to Cloud SQL instances with private IP
addresses.You also need to configure private services access and allocate an IP address range for the service producer network1.
Option B is incorrect because Cloud NAT does not support Cloud SQL instances with private IP addresses.Cloud NAT only provides
outbound connectivity for resources that do not have public IP addresses, such as VMs, GKE clusters, and serverless instances2.
Option C is correct because it allows you to use a Compute Engine instance as a proxy server to connect to the Cloud SQL database
over the peered network. The proxy server does not need an external IP address because it can communicate with the Dataflow workers
and the Cloud SQL instance using internal IP addresses. You need to install the Cloud SQL Auth proxy on the proxy server and
configure it to use a service account that has the Cloud SQL Client role.
Option D is incorrect because it requires you to assign public IP addresses to the Dataflow workers, which exposes the data to the public
internet. This violates the requirement of ensuring that the data does not go through the public internet. Moreover, adding authorized
networks does not work for Cloud SQL instances with private IP addresses.

---

### 9. You are integrating one of your internal IT applications and Google BigQuery, so users can query BigQuery from the application’s
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

### 10. Your company’s on-premises Apache Hadoop servers are approaching end-of-life, and IT has decided to migrate the cluster to Google
Cloud Dataproc. A like-for-like migration of the cluster would require 50 TB of Google Persistent Disk per node. The CIO is concerned
about the cost of using that much block storage. You want to minimize the storage cost of the migration. What should you do?
**Options:**
- Put the data into Google Cloud Storage.
- Use preemptible virtual machines (VMs) for the Cloud Dataproc cluster.
- Tune the Cloud Dataproc cluster so that there is just enough disk for all data.
- Migrate some of the cold data into Google Cloud Storage, and keep only the hot data in Persistent Disk.

**Correct Answer:** B

---

