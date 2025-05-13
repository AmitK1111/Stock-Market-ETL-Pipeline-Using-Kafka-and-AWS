# 📈 Stock Market ETL Pipeline Using Kafka and AWS

This repository contains a real-time stock market data simulation pipeline using **Apache Kafka**, deployed on **Amazon EC2**, that streams data from a simulated producer to a consumer. The consumer writes data to **Amazon S3**, catalogs it using **AWS Glue**, and enables querying through **Amazon Athena**.

---

## 🖼️ Architecture Overview

![Architecture Diagram](Architecture.jpg)

---

## 🧰 Technologies Used

| Component          | Description |
|--------------------|-------------|
| **Apache Kafka**    | Message broker for producer-consumer communication |
| **Amazon EC2**      | Kafka broker host |
| **Python**          | Simulation logic and producer/consumer |
| **Amazon S3**       | Data lake for raw data |
| **AWS Glue**        | Crawls and catalogs S3 data |
| **Amazon Athena**   | Query service for analyzing data |
| **Boto3 SDK**       | AWS interaction via Python |
| **CSV Dataset**     | Static stock market data used for simulation |

---

## 🔁 Project Flow

### 1. **Dataset Source**
- A historical stock market dataset in `.csv` format is used.

### 2. **Stock Market Simulation**
- A **Python-based simulation app** reads the CSV data and mimics real-time market updates.
- It uses **Kafka Producer** to send these records to a Kafka topic.

### 3. **Kafka Broker**
- Kafka is hosted on **Amazon EC2** and acts as a broker between producer and consumer.

### 4. **Kafka Consumer**
- Another Python app (consumer) reads data from the Kafka topic.
- It writes the data to **Amazon S3** in JSON format.

### 5. **AWS Glue**
- A **Glue Crawler** scans the S3 bucket and adds metadata to the **AWS Glue Data Catalog**.

### 6. **Amazon Athena**
- Athena queries the cataloged data directly from S3 using SQL.
- Enables analysis of real-time streaming stock data.

---

## 🗃️ S3 Bucket Structure

