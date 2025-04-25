# 📚 Learning Data Engineering

This repository tracks my learning journey in Data Engineering. It includes multiple hands-on projects designed to apply concepts like batch processing, data modeling, orchestration, and streaming in real-world scenarios.

## 🚀 Projects in this repo:

| #  | Project Name                 | Description                                           |
|----|------------------------------|-------------------------------------------------------|
| 1  | PySpark CSV to Postgres      | Read CSV with PySpark, clean/transform, write to DB  |
| 2  | Airflow ETL Pipeline         | Build and schedule ETL jobs with Apache Airflow      |
| 3  | Data Modeling in PostgreSQL  | Implement star schema and Slowly Changing Dimensions |
| 4  | Real-Time Streaming          | Stream data using Kafka and PySpark                  |

---

## 💡 Goal

To learn and apply data engineering skills by building real-world mini-projects using open-source and cloud tools.

## 🧰 Tools & Tech

- PySpark
- PostgreSQL
- Apache Airflow
- Apache Kafka
- Docker
- Cloud Platforms (AWS, GCP, Azure)

---

## 📌 Notes

- This is a learning-focused repo — perfect for beginners exploring the data engineering path.
- Contributions or suggestions are welcome!

---

# 🛍️ Project 01: Retail Sales Data Ingestion with PySpark & PostgreSQL 🚀

## 📝 Project Overview

This project simulates a **retail sales analytics use case**, where transactional data from a store’s daily sales (in CSV format) is ingested using **Apache PySpark**, transformed, and then stored in a **PostgreSQL** database. The pipeline supports **batch ingestion**, making it suitable for nightly or periodic loads into a data warehouse or BI system.

The goal is to demonstrate a **real-world, production-ready data pipeline** as part of a broader Data Engineering portfolio.

---

## ⚙️ Tech Stack

- 🐍 Python 3.x
- 🔥 Apache PySpark
- 🐘 PostgreSQL
- 🛠️ VS Code
- 📁 Git & GitHub

---

## 📂 Folder Structure

retail_sales_ingestion_pipeline/
├── .env                         # PostgreSQL credentials (used instead of ini)
├── data/
│   └── raw/
│       └── scanner_data.csv     # Your input CSV file
├── scripts/
│   ├── db_config.py             # Loads credentials from .env
│   ├── ingest_sales.py          # Main batch ingestion script
│   └── transform_utils.py       # Transformation helper functions
├── requirements.txt
├── README.md
└── create_env_file.py           # Optional helper to generate .env
