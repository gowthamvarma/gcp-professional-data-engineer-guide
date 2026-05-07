# PDE Practice Quiz #2 - May 2026

### 1. During the lifecycle of a PTransform using ParDo, which method is called for every individual input element?
**Options:**
- startBundle()
- finishBundle()
- processElement()
- setup()

**Correct Answer:** processElement()
**Explanation:** The @ProcessElement method contains the actual processing logic that is executed for every element in the input PCollection.

---

### 2. Why is it discouraged to perform heavy resource initialization (like opening a network connection) inside processElement()?
**Options:**
- It is executed for every single element, leading to massive performance overhead.
- It causes the pipeline to automatically switch to batch mode.
- It is not technically possible to open connections in ParDo.
- It violates the principle of immutability in Apache Beam.

**Correct Answer:** It is executed for every single element, leading to massive performance overhead.
**Explanation:** Since processElement runs for every record, performing heavy tasks inside it creates significant latency and can overwhelm external systems.

---

### 3. Which of the following is true regarding the 'startBundle' method?
**Options:**
- It is called exactly once per pipeline execution.
- It is called before the runner starts processing a group of elements.
- It is only used in Batch pipelines.
- It is used to define the schema of the output PCollection.

**Correct Answer:** It is called before the runner starts processing a group of elements.
**Explanation:** startBundle() is the initialization hook for a bundle of elements, allowing setup for operations that apply to that specific batch.

---

### 4. Which Beam feature allows a PTransform to access additional data sets that are not part of the main input PCollection?
**Options:**
- CoGroupByKey
- Side Inputs
- Windowing
- Flatten

**Correct Answer:** Side Inputs
**Explanation:** Side inputs provide a way to inject additional data (like a lookup table) into a ParDo transform alongside the main element stream.

---

### 5. What is the primary difference between Map and FlatMap PTransforms?
**Options:**
- Map is for streaming, FlatMap is for batch.
- Map produces exactly one output for each input; FlatMap can produce zero, one, or many.
- Map is faster than FlatMap.
- Map is a primitive transform, FlatMap is a composite transform.

**Correct Answer:** Map produces exactly one output for each input; FlatMap can produce zero, one, or many.
**Explanation:** Map is a 1-to-1 transformation, whereas FlatMap allows for 1-to-N transformations (including filtering by returning an empty list).

---

### 6. An organization is struggling with 'Late Data'—events arriving after the main processing window has closed. How does Apache Beam's model solve this without losing data?
**Options:**
- By rejecting any data that arrives after the system clock deadline.
- By manually restarting the pipeline every hour.
- Using Watermarks and allowed lateness.
- By using only Fixed Windows of 1 second.

**Correct Answer:** Using Watermarks and allowed lateness.
**Explanation:** Watermarks track progress relative to event time, and 'allowed lateness' enables the pipeline to update previously closed windows when late data arrives.

---

### 7. Your team needs to enrich a massive stream of telemetry data with a small, slowly-changing lookup table of 'Customer Metadata'. What is the most efficient Beam pattern to use?
**Options:**
- Perform a SQL JOIN in a BigQuery sink.
- Use a Side Input to broadcast the lookup table to all workers.
- Use a CoGroupByKey on every element.
- Store the metadata in a local text file on each worker VM.

**Correct Answer:** Use a Side Input to broadcast the lookup table to all workers.
**Explanation:** Side inputs are ideal for providing additional, smaller datasets to a ParDo transform without the overhead of a full shuffle or CoGroupByKey.

---

### 8. A data engineer wants to ensure that a Dataflow pipeline can handle a sudden 10x spike in traffic during a holiday sale without manual intervention. Which feature should be prioritized?
**Options:**
- Vertical Autoscaling
- Horizontal Autoscaling
- Static Allocation
- Manual Scaling

**Correct Answer:** Horizontal Autoscaling
**Explanation:** Horizontal Autoscaling allows Dataflow to dynamically add or remove workers based on CPU utilization and throughput needs.

---

### 9. A company requires 'exactly-once' processing for financial transactions. Why is Dataflow often preferred over other stream processors for this requirement?
**Options:**
- It is the only service that supports SQL.
- It integrates with Pub/Sub and utilizes checkpointing and shuffle-service state to ensure unique IDs are tracked.
- It uses a single worker to avoid concurrency issues.
- It automatically retries only failed elements.

**Correct Answer:** It integrates with Pub/Sub and utilizes checkpointing and shuffle-service state to ensure unique IDs are tracked.
**Explanation:** Dataflow provides exactly-once semantics by tracking record IDs through the shuffle service and persistent state, ensuring no duplicates are produced even during retries.

---

### 10. A retail company wants to calculate 'Cumulative Daily Sales' that update every time a new transaction occurs. Which windowing strategy is appropriate?
**Options:**
- Slidings Windows of 1 hour.
- Session Windows with 10-minute gaps.
- Fixed Windows of 24 hours with Repeating Triggers.
- Global Window with no triggers.

**Correct Answer:** Fixed Windows of 24 hours with Repeating Triggers.
**Explanation:** For a cumulative total that resets only once a day (or doesn't reset), a Fixed Windows of 24 hours combined with a trigger that fires per-element or periodically is the standard approach.

---

### 11. A company needs to join a high-velocity stream of 'User Clicks' with a stream of 'Ad Impressions' to calculate click-through rates. Which transform is required?
**Options:**
- Combine.globally()
- CoGroupByKey
- Partition
- GroupByKey

**Correct Answer:** CoGroupByKey
**Explanation:** CoGroupByKey is used to perform a join between two or more PCollections that share the same key, which is necessary for joining disparate streams.

---

### 12. An organization notices their Dataflow job is taking too long due to 'Shuffle' operations. Which optimization should they consider?
**Options:**
- Use more GroupByKeys.
- Enable Dataflow Shuffle (service-based shuffle).
- Increase the number of small worker VMs.
- Disable windowing.

**Correct Answer:** Enable Dataflow Shuffle (service-based shuffle).
**Explanation:** Dataflow Shuffle offloads the shuffle operation to a dedicated service backend, which is faster and more scalable than performing it on the worker VMs' local disks.

---

### 13. A data scientist is running an Apache Spark job on a large dataset stored in Cloud Storage. The job is performing multiple joins and aggregations. They notice that a single task is taking significantly longer than others (straggler). What is the most likely cause?
**Options:**
- Low network bandwidth between nodes.
- Data skew on the join key.
- The use of too many executors.
- The storage class of the GCS bucket.

**Correct Answer:** Data skew on the join key.
**Explanation:** Data skew occurs when one partition has significantly more data than others, causing the executor processing that partition to take much longer than the rest.

---

### 14. In an Apache Beam pipeline, you need to enrich a main stream of sensor data with metadata from a small, slowly-changing database table. What is the most efficient Beam pattern to achieve this without a massive join?
**Options:**
- CoGroupByKey
- Side Inputs
- MapElements
- Flatten

**Correct Answer:** Side Inputs
**Explanation:** Side inputs allow a ParDo to access additional data (like metadata) that is small enough to fit in memory on each worker, avoiding the overhead of a full shuffle join.

---

### 15. A Dataflow pipeline is failing with 'Out of Memory' errors on the workers. The pipeline involves a GroupByKey operation on a dataset where one key has millions of associated values. How should you refactor the pipeline?
**Options:**
- Increase the number of workers.
- Use Combine.perKey() with a lifting-compatible CombineFn.
- Switch from streaming to batch mode.
- Use a larger machine type for the workers.

**Correct Answer:** Use Combine.perKey() with a lifting-compatible CombineFn.
**Explanation:** Using Combine.perKey allows for partial aggregation (combining) on the worker side before the shuffle, significantly reducing the amount of data buffered in memory for a single key.

---

### 16. You need to ensure that messages published to Google Pub/Sub are processed in the exact order they were sent for each specific user ID. Which feature should you use?
**Options:**
- Ordering keys
- Snapshot and Seek
- Dead-letter topics
- Exactly-once delivery

**Correct Answer:** Ordering keys
**Explanation:** Ordering keys ensure that messages with the same key are delivered to the subscriber in the order they were received by the Pub/Sub service.

---

### 17. An Apache Beam pipeline needs to write data to two different BigQuery tables based on the value of a 'priority' field in the record. Which PTransform is designed for this?
**Options:**
- ParDo with Multi-output (Tags)
- CoGroupByKey
- Partition
- Flatten

**Correct Answer:** ParDo with Multi-output (Tags)
**Explanation:** A ParDo can use TupleTags to emit elements to different PCollections (side outputs) based on logic within the process element method.

---

### 18. You want to reduce costs for a Pub/Sub subscription where the subscriber only cares about messages where 'region' equals 'US-East'. Where should this logic be placed for maximum cost efficiency?
**Options:**
- Filter within the subscriber application code.
- Use Pub/Sub Subscription Filtering.
- Create multiple topics for each region.
- Use a Dataflow job to filter the messages.

**Correct Answer:** Use Pub/Sub Subscription Filtering.
**Explanation:** Subscription filtering happens service-side, meaning the subscriber doesn't receive (or pay for the egress of) messages that don't meet the criteria.

---

### 19. When developing an Apache Beam pipeline, why is it important to ensure that your DoFns are idempotent?
**Options:**
- Because Beam may retry the execution of a bundle of elements upon worker failure.
- To ensure that the code runs faster.
- Because it is a requirement for using BigQuery as a sink.
- To prevent the pipeline from entering an infinite loop.

**Correct Answer:** Because Beam may retry the execution of a bundle of elements upon worker failure.
**Explanation:** Distributed runners provide fault tolerance by retrying work. If a DoFn is not idempotent, retries could lead to duplicate side effects or incorrect data.

---

### 20. A system uses Pub/Sub to trigger Cloud Functions. Some messages fail to process and are retried indefinitely, blocking the queue. What is the recommended Pub/Sub feature to handle these 'poison pill' messages?
**Options:**
- Seek to timestamp
- Dead-letter topics
- Message retention
- Acknowledgment deadline

**Correct Answer:** Dead-letter topics
**Explanation:** Dead-letter topics allow you to redirect messages that fail to be acknowledged after a certain number of delivery attempts to a separate topic for investigation.
