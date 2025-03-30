In this project, I developed a real-time, scalable data pipeline that ingests, processes, and analyzes weather data using AWS services and Snowflake. First, Data is automatically fetched from an external Weather API at scheduled intervals using AWS Lambda. The ingested weather data is stored in Amazon DynamoDB, a NoSQL database, for efficient querying and storage. Using DynamoDB Streams, I processed the stored data in real-time as changes occurred, enabling continuous updates to the data. The processed data is streamed into Amazon S3 for long-term, secure storage. Finally, the processed data is loaded into Snowflake, a cloud data warehouse, where I can perform advanced analytics and extract insights.

AWS Lambda: For serverless data ingestion and automation.
Event triggers that automate the execution of Lambda functions on a schedule.
Amazon DynamoDB: For storing and querying the weather data. DynamoDB Streams For real-time data processing as changes occur in DynamoDB.
Amazon S3: For scalable and secure data storage.
Snowflake: For cloud data warehousing and in-depth analysis.

This project demonstrates how to integrate AWS serverless services and Snowflake to build a real-time, efficient data pipeline for weather data ingestion, processing, storage, and analysis.
In this project, I developed a real-time, scalable data pipeline that ingests, processes, and analyzes weather data using AWS services and Snowflake. First, Data is automatically fetched from an external Weather API at scheduled intervals using AWS Lambda. The ingested weather data is stored in Amazon DynamoDB, a NoSQL database, for efficient querying and storage. Using DynamoDB Streams, I processed the stored data in real-time as changes occurred, enabling continuous updates to the data. The processed data is streamed into Amazon S3 for long-term, secure storage. Finally, the processed data is loaded into Snowflake, a cloud data warehouse, where I can perform advanced analytics and extract insights. AWS Lambda: For serverless data ingestion and automation. Event triggers that automate the execution of Lambda functions on a schedule. Amazon DynamoDB: For storing and querying the weather data. DynamoDB Streams For real-time data processing as changes occur in DynamoDB. Amazon S3: For scalable and secure data storage. Snowflake: For cloud data warehousing and in-depth analysis. This project demonstrates how to integrate AWS serverless services and Snowflake to build a real-time, efficient data pipeline for weather data ingestion, processing, storage, and analysis.

<p align="center">
<img width="1470" alt="W5" src="https://github.com/user-attachments/assets/1d826bb3-28ac-48a9-aff0-600afc9f8a41" />
<img width="1470" alt="W4" src="https://github.com/user-attachments/assets/cc0a1221-8418-4ad8-af3d-5759b72947e0" />
<img width="918" alt="W3" src="https://github.com/user-attachments/assets/07101df5-9d87-4b99-aa39-f78116730154" />
<img width="1470" alt="W2" src="https://github.com/user-attachments/assets/53165abd-6875-4ee8-a8fe-7148eec1f900" />
<img width="935" alt="W1" src="https://github.com/user-attachments/assets/bfcd93b7-ad41-4de3-822f-aa69f16c622a" />
</p>
