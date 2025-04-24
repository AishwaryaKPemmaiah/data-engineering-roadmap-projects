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
