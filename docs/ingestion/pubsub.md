# Pub/Sub: Messaging and Streaming

Pub/Sub is a global, asynchronous messaging service that decouples senders and receivers. It's the "glue" that holds many real-time data pipelines together.

## High-Signal Summary
If you see "real-time," "streaming," or "decoupling" on the exam, your first thought should be Pub/Sub. It's a many-to-many, asynchronous messaging service that handles the heavy lifting of scale and durability for you.

## Key Concepts

### Dead Letter Topics 💡 **PRO TIP**
Sometimes, a message just can't be processed. Instead of letting it clog up your subscription and retrying forever, you can configure a **Dead Letter Topic**. After a certain number of delivery attempts, Pub/Sub will move the "bad" message to this topic for later manual investigation.

### Snapshot and Seek
Ever wished you could "rewind" time? **Snapshot and Seek** lets you do just that. You can take a snapshot of a subscription state and then "seek" back to it if you need to replay messages that were already acknowledged.

### BigQuery Subscriptions 🚀 **FAST FACT**
As of 2026, you don't always need Dataflow! You can stream data directly from Pub/Sub to BigQuery using **BigQuery Subscriptions**. This is simpler and often more cost-effective for simple ingestion patterns.

### Message Filtering 🕵️ **EXAM ALERT**
Pub/Sub allows you to filter messages at the subscription level. This means a subscriber only receives messages that match a specific attribute or data payload, reducing unnecessary processing and network costs. You can use filtering for selective data processing or routing to different downstream systems.

---
*More content to come in the next task!*
