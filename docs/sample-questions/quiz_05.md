# PDE Practice Quiz #5 - May 2026

### 1. Your company built a TensorFlow neural-network model with a large number of neurons and layers. The model fits well for the training data. However, when tested against new data, it performs poorly. What method can you employ to address this?
**Options:**
- Threading
- Serialization
- Dropout Methods
- Dimensionality Reduction

**Correct Answer:** Dropout Methods
**Explanation:** The scenario describes "overfitting," where a model performs well on training data but poorly on unseen test data. Dropout is a regularization technique that randomly "drops" neurons during training, preventing them from co-adapting too much and forcing the model to learn more robust, generalizable patterns.

---

### 2. You are building a model to make clothing recommendations. You know a user's fashion preference is likely to change over time, so you build a data pipeline to stream new data back to the model as it becomes available. How should you use this data to train the model?
**Options:**
- Continuously retrain the model on just the new data.
- Continuously retrain the model on a combination of existing data and the new data.
- Train on the existing data while using the new data as your test set.
- Train on the new data while using the existing data as your test set.

**Correct Answer:** Continuously retrain the model on a combination of existing data and the new data.
**Explanation:** To adapt to changing preferences while maintaining the model's underlying knowledge, it should be retrained on a mixture of historical and fresh data. Training only on new data can lead to "catastrophic forgetting," where the model loses its ability to generalize from past patterns.

---

### 3. You designed a database for patient records as a pilot project to cover a few hundred patients in three clinics. Your design used a single database table to represent all patients and their visits, and you used self-joins to generate reports. Since then, the scope of the project has expanded. The database must now store 100 times more patient records. You can no longer run the reports because they take too long or encounter errors with insufficient compute resources. How should you adjust the database design?
**Options:**
- Add capacity (memory and disk space) to the database server by the order of 200.
- Shard the tables into smaller ones based on date ranges, and only generate reports with prespecified date ranges.
- Normalize the master patient-record table into the patient table and the visits table, and create other necessary tables to avoid self-join.
- Partition the table into smaller tables, with one for each clinic. Run queries against the smaller table pairs, and use unions for consolidated reports.

**Correct Answer:** Normalize the master patient-record table into the patient table and the visits table, and create other necessary tables to avoid self-join.
**Explanation:** The performance bottleneck is caused by using a single massive table and relying on expensive self-joins. Normalizing the schema (3rd Normal Form) reduces data redundancy and allows for more efficient joins between specialized tables, which scales much better than self-joining a single large table.

---

### 4. You create an important report for your large team in Looker Studio (formerly Data Studio). The report uses Google BigQuery as its data source. You notice that visualizations are not showing data that is less than 1 hour old. What should you do?
**Options:**
- Disable caching by editing the report settings.
- Disable caching in BigQuery by editing table details.
- Refresh your browser tab showing the visualizations.
- Clear your browser history for the past hour then reload the tab.

**Correct Answer:** Disable caching by editing the report settings.
**Explanation:** Looker Studio caches query results for performance. To ensure the report reflects the most recent data (stale by less than an hour), you must adjust the "Data freshness" or "Cache" settings in the report's data source configuration.

---

### 5. An external customer provides you with a daily dump of data from their database. The data flows into Google Cloud Storage (GCS) as CSV files. You want to analyze this data in BigQuery, but the data could have rows that are formatted incorrectly or corrupted. How should you build this pipeline?
**Options:**
- Use federated data sources, and check data in the SQL query.
- Enable BigQuery monitoring in Cloud Monitoring and create an alert.
- Import the data into BigQuery using the gcloud CLI and set max_bad_records to 0.
- Run a Google Cloud Dataflow batch pipeline to import the data into BigQuery, and push errors to another dead-letter table for analysis.

**Correct Answer:** Run a Google Cloud Dataflow batch pipeline to import the data into BigQuery, and push errors to another dead-letter table for analysis.
**Explanation:** Dataflow is the preferred tool for robust ETL processes. Using a dead-letter pattern allows the pipeline to isolate malformed records for debugging without stopping the ingestion of valid data, providing better control and visibility than simple load-job settings.

---

### 6. Your weather app queries a database every 15 minutes to get the current temperature. The frontend is powered by Google App Engine and serves millions of users. How should you design the frontend to respond to a database failure?
**Options:**
- Issue a command to restart the database servers.
- Retry the query with exponential backoff, up to a cap of 15 minutes.
- Retry the query every second until it comes back online to minimize staleness of data.
- Reduce the query frequency to once every hour until the database comes back online.

**Correct Answer:** Retry the query with exponential backoff, up to a cap of 15 minutes.
**Explanation:** Exponential backoff is a standard error-handling strategy that progressively increases the wait time between retries. This prevents the "thundering herd" problem where millions of instances overwhelm a recovering database while ensuring the app recovers as soon as possible.

---

### 7. You are creating a model to predict housing prices. Due to budget constraints, you must run it on a single resource-constrained virtual machine. Which learning algorithm should you use?
**Options:**
- Linear regression
- Logistic classification
- Recurrent neural network
- Feedforward neural network

**Correct Answer:** Linear regression
**Explanation:** Housing price prediction is a regression task (predicting a continuous value). Linear regression is computationally efficient, requires very little memory/CPU compared to neural networks, and is well-suited for single, resource-constrained VMs.

---

### 8. You are building a new real-time data warehouse for your company and will use Google BigQuery streaming inserts. There is no guarantee that data will only be sent in once, but you do have a unique ID for each row and an event timestamp. You want to ensure that duplicates are not included while interactively querying data. Which query type should you use?
**Options:**
- Include ORDER BY DESC on timestamp column and LIMIT to 1.
- Use GROUP BY on the unique ID column and timestamp column and SUM on the values.
- Use the LAG window function with PARTITION by unique ID along with WHERE LAG IS NOT NULL.
- Use the ROW_NUMBER window function with PARTITION by unique ID along with WHERE row equals 1.

**Correct Answer:** Use the ROW_NUMBER window function with PARTITION by unique ID along with WHERE row equals 1.
**Explanation:** This is the standard pattern for deduplicating streaming data in BigQuery. By partitioning the data by its unique ID and sorting by timestamp, the `ROW_NUMBER()` function allows you to select only the most recent (or first) instance of each record.

---

### 9. Your company is using wildcard tables to query data across multiple tables with similar names. The SQL statement is currently failing. Which table name syntax will make the SQL statement work correctly?
**Options:**
- 'bigquery-public-data.noaa_gsod.gsod'
- bigquery-public-data.noaa_gsod.gsod*
- 'bigquery-public-data.noaa_gsod.gsod'*
- \`bigquery-public-data.noaa_gsod.gsod*\`

**Correct Answer:** \`bigquery-public-data.noaa_gsod.gsod*\`
**Explanation:** In BigQuery Standard SQL, wildcard tables must be enclosed in backticks (\`) to be correctly parsed, especially when the table name or project ID contains special characters like hyphens.

---

### 10. Your company is in a highly regulated industry. One of your requirements is to ensure individual users have access only to the minimum amount of information required to do their jobs. You want to enforce this requirement with Google BigQuery. Which three approaches can you take? (Choose three.)
**Options:**
- Disable writes to certain tables.
- Restrict access to tables by role.
- Ensure that the data is encrypted at all times.
- Restrict BigQuery API access to approved users.
- Segregate data across multiple tables or datasets.
- Use Cloud Audit Logs to determine policy violations.

**Correct Answer:** Restrict access to tables by role; Segregate data across multiple tables or datasets; Use Cloud Audit Logs to determine policy violations.
**Explanation:** To enforce the principle of least privilege: (1) Use IAM roles to grant granular access to specific tables. (2) Segregate data logically so users only interact with relevant datasets. (3) Use Audit Logs to monitor access and ensure compliance with security policies.
