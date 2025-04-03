A pipeline was designed and implemented to ensure seamless real-time ingestion, transformation, and processing of diverse datasets while maintaining data integrity and minimizing latency. Every aspect of the pipeline was optimized for scalability, automation, and robustness. The core of the pipeline was built using Microsoft Azure technologies.The architecture followed a layered approach, ensuring a seamless flow of data from ingestion to final analytics and reporting.

Azure DevOps served as the central hub for version control and CI/CD automation. Each component of the pipeline, including dataset definitions and pipeline configurations, was organized in Azure DevOps repositories. CI/CD pipelines were configured to automate validation, testing, and deployment of updates, significantly reducing errors and downtime.

Data ingestion was handled through multiple pipelines using Azure Data Factory. These pipelines managed the extraction, loading, and pre-processing of data in various formats like JSON, CSV, and Parquet. The pipelines were parameterized for flexibility, dynamically adapting to different data sources. This approach eliminated the need for manual intervention, ensuring efficient data processing. 
Validation steps were embedded within ADF to detect and handle missing values and inconsistencies. Delta Live Tables in Databricks ensured schema validation, error resolution.. Real-time incremental updates processed only new or modified data, reducing overhead. Once ingested, the data was transformed using PySpark within Databricks. The distributed processing capabilities of PySpark handled large-scale transformations efficiently.

Structured Streaming was used for real-time insights, minimizing processing delays. Automated orchestration using Databricks and ADF ensured efficient job scheduling and dependency management, keeping the pipeline running smoothly without manual intervention.
  
<div style="text-align: center;"> <img width="1470" alt="Screenshot 2025-03-31 at 3 38 47 PM" src="https://github.com/user-attachments/assets/88f01d7f-a455-4cbb-a4d2-c93ae465db7c" /> </div>

<div style="text-align: center;">
    <img width="1470" alt="Screenshot 2025-03-30 at 10 34 30 PM" src="https://github.com/user-attachments/assets/ba60657f-41ce-4f48-926c-04f4ec218b0d" />
</div>

<div style="text-align: center;">
    <img width="1470" alt="Screenshot 2025-03-31 at 1 59 50 PM" src="https://github.com/user-attachments/assets/78a43700-1d62-42a1-b8c2-270d6c969a32" />
</div>

<div style="text-align: center;">
    <img width="1470" alt="Screenshot 2025-03-31 at 9 35 35 PM" src="https://github.com/user-attachments/assets/bc6c8728-e1d5-404f-928e-ff44ea3e98d6" />
</div>

<div style="text-align: center;">
    <img width="1470" alt="Screenshot 2025-04-01 at 12 44 41 PM" src="https://github.com/user-attachments/assets/749b7884-9e34-4379-b207-c10feac22a3d" />
</div>

