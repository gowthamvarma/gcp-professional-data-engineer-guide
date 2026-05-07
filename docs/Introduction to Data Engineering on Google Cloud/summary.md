# Course Summary: Introduction to Data Engineering on Google Cloud

This course provides a comprehensive overview of data engineering on Google Cloud, covering roles, tasks, components, and common architectural patterns.

## 1. The Role of a Data Engineer
A data engineer builds data pipelines to enable data-driven decisions. Their primary responsibilities include:
*   **Ingestion & Storage**: Getting raw data to where it can be useful.
*   **Transformation**: Converting data into a usable condition.
*   **Provisioning & Enrichment**: Adding new value to data.
*   **Management**: Ensuring security, privacy, discovery, and governance.
*   **Productionization**: Monitoring and automating pipelines for operational excellence.

## 2. Core Concepts
*   **Data Lake vs. Data Warehouse**:
    *   **Data Lake**: Stores raw, native format data (unstructured/structured) for data science and flexible use. Primary service: **Cloud Storage**.
    *   **Data Warehouse**: Stores pre-processed, aggregated data for long-term business analysis. Primary service: **BigQuery**.
*   **Dataplex**: Centrally discover, manage, monitor, and govern distributed data across lakes and warehouses.
*   **Analytics Hub**: A platform for securely sharing and monetizing datasets both within and outside an organization.

## 3. Data Replication and Migration
Tools for onboarding data into Google Cloud:
*   **gcloud storage**: For small to medium-sized transfers.
*   **Storage Transfer Service**: For medium to large online transfers from on-premises, multicloud (S3/Azure), or other Google Cloud locations.
*   **Transfer Appliance**: For massive offline data migrations (7TB to 300TB).
*   **Datastream**: A serverless Change Data Capture (CDC) and replication service for relational databases (Oracle, MySQL, PostgreSQL, SQL Server).

## 4. Data Pipeline Patterns

### Pattern A: Extract and Load (EL)
Focuses on making data accessible without upfront transformation.
*   **Tools**: `bq load`, BigQuery Data Transfer Service.
*   **BigLake**: Allows querying data stored in Cloud Storage or other cloud providers directly within BigQuery with fine-grained security and metadata caching.

### Pattern B: Extract, Load, and Transform (ELT)
Loads data into a staging area first, then transforms it using the destination's compute power.
*   **BigQuery SQL Scripting**: Supports procedural language (IF, WHILE, variables, transactions).
*   **Dataform**: A serverless framework to develop and operationalize SQL-based ELT pipelines using SQLX, enabling version control and data quality assertions.

### Pattern C: Extract, Transform, and Load (ETL)
Transforms data before loading it into the final destination.
*   **Dataprep by Trifacta**: No-code visual tool for data wrangling.
*   **Cloud Data Fusion**: GUI-based enterprise integration service based on CDAP.
*   **Dataproc**: Managed Hadoop and Spark service for batch processing. Supports "Serverless Spark" to eliminate cluster management.
*   **Dataflow**: Based on Apache Beam; provides a unified programming model for both batch and streaming data.
*   **Bigtable**: Often used as a sink for streaming pipelines requiring millisecond latency for large-scale NoSQL workloads.

## 5. Automation Techniques
*   **Cloud Scheduler**: Triggers workloads at recurring intervals using cron format.
*   **Workflows**: Orchestrates Google Cloud services and HTTP APIs with low-latency execution.
*   **Cloud Composer**: Managed Apache Airflow for complex workflow orchestration across systems.
*   **Cloud Run functions**: Event-driven serverless code execution (e.g., triggered by GCS file uploads).
*   **Eventarc**: Provides a unified event-driven architecture for loosely coupled services.
