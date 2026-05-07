# PDE Practice Quiz #3 - BigQuery ML & AI

### 1. Which SQL statement is used to initiate the training of a machine learning model in BigQuery ML?
**Options:**
- TRAIN MODEL
- CREATE MODEL
- BUILD MODEL
- INSERT MODEL

**Correct Answer:** CREATE MODEL
**Explanation:** The CREATE OR REPLACE MODEL statement is the standard syntax used in BigQuery ML to define and train a model using SQL.

---

### 2. When creating a model, you want to specify the column that the model should predict. Which 'model_option' do you use in the SQL statement?
**Options:**
- target_col
- predict_column
- input_label_cols
- label_value

**Correct Answer:** input_label_cols
**Explanation:** The 'input_label_cols' option in the OPTIONS clause is used to specify a list of column names that the model is trying to predict.

---

### 3. What is the default behavior of BigQuery ML regarding data splitting for training and evaluation?
**Options:**
- It uses 100% of data for training and requires a separate table for evaluation.
- It automatically splits the data into training and evaluation sets.
- It requires the user to manually add a 'split' column to the dataset.
- It uses cross-validation by default for all model types.

**Correct Answer:** It automatically splits the data into training and evaluation sets.
**Explanation:** By default, BigQuery ML automatically reserves a portion of the input data for evaluation to prevent overfitting, though this can be customized using the 'data_split_method' option.

---

### 4. You are using ML.PREDICT to generate results. What is the structure of the output table?
**Options:**
- Only the predicted value column.
- The predicted value column followed by the primary key of the input table.
- All columns from the input data plus the prediction columns prefixed with 'predicted_'.
- A nested JSON object containing all input features and the result.

**Correct Answer:** All columns from the input data plus the prediction columns prefixed with 'predicted_'.
**Explanation:** ML.PREDICT returns all columns from the input 'table_name' or 'query_statement', along with the prediction results, allowing for easy joining and analysis.

---

### 5. How does BigQuery ML handle categorical (string) features during the training of a Linear Regression model?
**Options:**
- It ignores all non-numeric columns automatically.
- It performs automatic one-hot encoding for string columns.
- It requires the user to manually convert strings to integers using CASE statements.
- It uses label encoding based on alphabetical order.

**Correct Answer:** It performs automatic one-hot encoding for string columns.
**Explanation:** BigQuery ML performs automatic preprocessing, including one-hot encoding for categorical features, which converts string labels into a format the algorithm can process.

---

### 6. Which function allows you to see the underlying weights assigned to each feature after training a linear model?
**Options:**
- ML.FEATURE_INFO
- ML.WEIGHTS
- ML.COEFFICIENTS
- ML.EXPLAIN_PREDICT

**Correct Answer:** ML.WEIGHTS
**Explanation:** ML.WEIGHTS returns the underlying weights (coefficients) for each feature in a linear or logistic regression model.

---

### 7. In a K-means clustering model, how can you determine the optimal number of clusters if you don't specify 'num_clusters'?
**Options:**
- BigQuery will always default to 5 clusters.
- BigQuery ML can automatically determine the number of clusters if 'use_auto_class' is set to true.
- It is not possible; the query will fail if 'num_clusters' is omitted.
- You must use Hyperparameter Tuning to iterate through cluster counts.

**Correct Answer:** BigQuery ML can automatically determine the number of clusters if 'use_auto_class' is set to true.
**Explanation:** For K-means, BigQuery ML can automatically find the optimal number of clusters based on the Davies-Bouldin index if the user doesn't provide a specific count.

---

### 8. What is the purpose of the 'TRANSFORM' clause in BigQuery ML?
**Options:**
- To move a model from one dataset to another.
- To define manual feature engineering logic that is saved with the model and applied during prediction.
- To convert a BigQuery ML model into a TensorFlow SavedModel format.
- To automatically normalize all numeric inputs to a range of 0 to 1.

**Correct Answer:** To define manual feature engineering logic that is saved with the model and applied during prediction.
**Explanation:** The TRANSFORM clause allows users to specify feature engineering (like scaling or bucketizing) that becomes part of the model, ensuring the same logic is applied during both training and inference.

---

### 9. True or False: BigQuery ML supports the import and use of pre-trained TensorFlow models for inference.
**Options:**
- True
- False

**Correct Answer:** True
**Explanation:** BigQuery ML allows you to import TensorFlow models stored in Cloud Storage and use them for prediction directly within BigQuery using SQL.

---

### 10. What is the primary benefit of using BigQuery ML over exporting data to a separate ML platform?
**Options:**
- BQML models are always more accurate than Python models.
- It eliminates the need to move data, reducing latency and increasing security.
- It is free to use, whereas other platforms charge for training.
- It supports more languages than just SQL.

**Correct Answer:** It eliminates the need to move data, reducing latency and increasing security.
**Explanation:** The core value of BQML is 'bringing the model to the data,' which avoids the time-consuming and risky process of data egress.

---

### 11. You want to convert a large collection of unstructured text into numerical vectors for a semantic search application. Which function should you use?
**Options:**
- ML.GENERATE_TEXT
- ML.UNDERSTAND_TEXT
- ML.GENERATE_EMBEDDING
- ML.TEXT_VECTORIZE

**Correct Answer:** ML.GENERATE_EMBEDDING
**Explanation:** ML.GENERATE_EMBEDDING is used to call text embedding models that transform text into high-dimensional vectors representing semantic meaning.

---

### 12. What is a prerequisite for running any BigQuery AI function that interacts with a Vertex AI LLM?
**Options:**
- A BigQuery Reservation with an Enterprise edition
- A Cloud Resource connection and an associated service account
- The data must be stored in a Parquet format
- A Dataproc cluster running in the same region

**Correct Answer:** A Cloud Resource connection and an associated service account
**Explanation:** Remote models in BigQuery require a Cloud Resource connection to securely delegate permissions to Vertex AI via a service account.

---

### 13. You need to translate a column of product reviews from French to English within a BigQuery table. Which function is most appropriate?
**Options:**
- ML.TRANSLATE
- ML.GENERATE_TEXT
- ML.TRANSLATE_TEXT
- ML.LANGUAGE_CONVERT

**Correct Answer:** ML.TRANSLATE
**Explanation:** ML.TRANSLATE is the specific function that utilizes the Cloud Translation API for batch translation of text within BigQuery.

---

### 14. To perform vector similarity searches in BigQuery (like K-nearest neighbors) after generating embeddings, which function is typically used?
**Options:**
- ML.DISTANCE
- VECTOR_SEARCH
- ML.SIMILARITY
- ML.NEIGHBORS

**Correct Answer:** VECTOR_SEARCH
**Explanation:** VECTOR_SEARCH is the optimized BigQuery function for finding the top-K similar items between a query dataset and a base dataset of embeddings.

---

### 15. Which argument is used to specify the input text for BigQuery LLM functions?
**Options:**
- input_column
- prompt
- struct_input
- table_data

**Correct Answer:** prompt
**Explanation:** The 'prompt' argument can be a literal string or a reference to a column name in the source table (or a combination thereof).

---

### 16. Which BigQuery AI function would you use to transcribe audio files stored in a Cloud Storage bucket via a BigQuery Object Table?
**Options:**
- ML.TRANSCRIBE_AUDIO
- ML.ANNOTATE_AUDIO
- ML.TRANSCRIBE
- ML.GENERATE_TEXT

**Correct Answer:** ML.TRANSCRIBE
**Explanation:** ML.TRANSCRIBE allows users to process audio data stored in object tables using the Google Cloud Speech-to-Text API directly via SQL.

---

### 17. Which function is used to extract structured information (like form fields or tables) from PDF documents stored in an object table?
**Options:**
- ML.DOCUMENT_AI
- ML.EXTRACT_DOCUMENT
- ML.PROCESS_DOCUMENT
- ML.READ_PDF

**Correct Answer:** ML.PROCESS_DOCUMENT
**Explanation:** ML.PROCESS_DOCUMENT integrates with Document AI to analyze and extract information from documents stored in Cloud Storage.

---

### 18. Which BigQuery function is used to convert images into descriptive text labels?
**Options:**
- ML.DESCRIBE_IMAGE
- ML.ANNOTATE_IMAGE
- ML.IMAGE_TO_TEXT
- ML.VISION_AI

**Correct Answer:** ML.ANNOTATE_IMAGE
**Explanation:** ML.ANNOTATE_IMAGE uses the Cloud Vision API to perform label detection, face detection, and other visual analysis tasks.

---

### 19. In the context of BigQuery AI, what does 'Remote Model' specifically imply?
**Options:**
- The model is stored on a local hard drive
- The model is executed on Vertex AI or an external API rather than BigQuery's internal engine
- The model is only available in other Google Cloud regions
- The model is managed by a third-party provider like Snowflake

**Correct Answer:** The model is executed on Vertex AI or an external API rather than BigQuery's internal engine
**Explanation:** A remote model refers to an abstraction in BigQuery that points to an endpoint outside of BigQuery, such as a Vertex AI model or a Cloud AI API.

---

### 20. Which BigQuery ML function provides insights into which features contributed most to a specific prediction?
**Options:**
- ML.FEATURE_IMPORTANCE
- ML.EXPLAIN_PREDICT
- ML.GLOBAL_EXPLAIN
- ML.DESCRIBE_MODEL

**Correct Answer:** ML.EXPLAIN_PREDICT
**Explanation:** ML.EXPLAIN_PREDICT returns the prediction results along with the feature attributions (Shapley values) for each row.
