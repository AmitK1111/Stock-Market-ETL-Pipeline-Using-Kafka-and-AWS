# 📈 Stock Market Streaming Pipeline using Kafka and AWS

This project is a simulation of a **real-time data streaming pipeline** that emulates a stock market feed. It leverages **Apache Kafka** for message streaming and **AWS services** like **EC2**, **S3**, **Glue**, and **Athena** to process, store, catalog, and query the data. This setup is ideal for building real-time analytics dashboards or data lakes.

---

## 🧠 Project Objective

To simulate a stock market app that streams data continuously into an AWS-based data lake using Kafka as the backbone for real-time ingestion and AWS services for ELT (Extract, Load, Transform) operations and querying.

---

## 🔧 Technologies Used

| Component         | Tool/Service                          |
|-------------------|----------------------------------------|
| Programming       | Python (with `boto3`, `kafka-python`) |
| Streaming Broker  | Apache Kafka                          |
| Broker Host       | AWS EC2 (Amazon Linux / Ubuntu)       |
| Storage           | Amazon S3                             |
| ETL Catalog       | AWS Glue Crawler + Data Catalog       |
| Query Engine      | Amazon Athena                         |

---

## 🔄 Architecture Diagram

![Architecture](Stock_Market_Architecture.jpg)

---

## ⚙️ System Workflow

### 1. **Dataset Preparation**
- A stock market CSV file simulates a live data feed.
- Contains fields like `symbol`, `open`, `close`, `volume`, `timestamp`, etc.

### 2. **Producer (Python + Kafka)**
- Reads the dataset line by line and sends it to a Kafka topic (`stock-topic`).
- Uses `kafka-python` and `boto3` SDK.
- Simulates real-time publishing using time delays (e.g., `sleep(1)`).

### 3. **Kafka Broker (Apache Kafka on EC2)**
- Deployed on an AWS EC2 instance.
- Receives and brokers messages between producer and consumer.

### 4. **Consumer (Python + Kafka)**
- Subscribes to the Kafka topic.
- Consumes messages in real time.
- Writes the data to a designated S3 bucket in a structured format (e.g., JSON or CSV).

### 5. **Amazon S3 (Data Lake)**
- Stores incoming streaming data in a structured folder format.
- Partitioning can be done by date or symbol for optimization.

### 6. **AWS Glue Crawler**
- Scans the S3 bucket.
- Infers schema and creates a table in the AWS Glue Data Catalog.

### 7. **Amazon Athena**
- Queries the S3-based table using standard SQL.
- Supports exploratory data analysis and report generation.

---

## 📂 Folder Structure

```text
.
├── kafka_producer.py           # Produces stock data to Kafka
├── kafka_consumer.py           # Consumes Kafka data and stores in S3
├── stock_data.csv              # Stock dataset used in the simulation
├── Architecture.jpg            # Architecture diagram
└── README.md                   # You are here

