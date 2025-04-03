#End to End ELT Pipeline for Netflix Data

In this project, I built a comprehensive data engineering pipeline that handled real-time ingestion, transformation, and validation of Netflix's TV shows and movies data, providing high-quality, clean datasets for analytics and reporting. Databricks was central to the project, where I utilized Delta Lake for optimized storage and processing. Delta Lake provided scalable and fault-tolerant data storage, while Apache Spark enabled distributed data processing. Using Databricks Notebooks, I orchestrated the pipeline and implemented efficient data transformations. 

Azure Data Factory (ADF) automated the ETL workflows, ensuring seamless data movement between sources like Azure Data Lake Storage (ADLS). ADF made it possible to set up automated transformations, reducing manual intervention and enhancing the pipeline's efficiency. To handle real-time data ingestion, I implemented Autoloader, which automatically detected and ingested new data files from ADLS. This eliminated the need for scheduled batch loads, enabling continuous data updates.

The Medallion Architecture (Bronze, Silver, Gold layers) was employed to structure the data. Unity Catalog centralized metadata management, ensuring governance and consistent data access controls. This improved data security and compliance. Delta Live Tables (DLT) were utilized for automated transformations and ensuring data quality. DLT ensured only clean and validated data moved through the pipeline.

Autoloader enabled continuous data ingestion, minimizing processing delays. The Medallion Architecture and Delta Live Tables ensured consistent data transformation, cleaning, and validation. ADF automated the ETL process, reducing manual efforts and streamlining data processing. Unity Catalog provided centralized control over metadata and access, improving security.

<p align="center">
  <img width="1470" alt="N4" src="https://github.com/user-attachments/assets/45b46c1e-b889-4d39-ab28-1dd536936d7f" />
  <img width="1470" alt="N3" src="https://github.com/user-attachments/assets/b862f65c-ce62-472d-a154-9a46d6c1cbe7" />
  <img width="1470" alt="N2" src="https://github.com/user-attachments/assets/b9de7a85-bcc4-4965-9976-33a44556d26d" />
  <img width="1470" alt="N1" src="https://github.com/user-attachments/assets/cdb8b306-7c79-43f1-becc-fc80d47afeed" />
  <img width="1470" alt="DLT_GOLD" src="https://github.com/user-attachments/assets/ded51c50-7dec-4847-b656-7268ba0143db" />
</p>
