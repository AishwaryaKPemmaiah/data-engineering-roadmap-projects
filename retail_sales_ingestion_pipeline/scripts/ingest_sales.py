from pyspark.sql import SparkSession
import os
import sys

# Append the root directory of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.transform_utils import clean_sales_data, cast_columns
from scripts.db_config import get_postgres_config

def main():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("Retail Sales Ingestion") \
        .config("spark.jars.packages", "org.postgresql:postgresql:42.6.0") \
        .getOrCreate()
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Define the schema explicitly
    schema = StructType([
        StructField("Row_ID", IntegerType(), True),
        StructField("Date", StringType(), True),
        StructField("Customer_ID", IntegerType(), True),
        StructField("Transaction_ID", IntegerType(), True),
        StructField("SKU_Category", StringType(), True),
        StructField("SKU", StringType(), True),
        StructField("Quantity", IntegerType(), True),
        StructField("Sales_Amount", FloatType(), True)
    ])

# Read the CSV file with the explicit schema
    df = spark.read.option("header", "true").schema(schema).csv("data/raw/scanner_data.csv")

    # Check the schema after reading the file
    df.printSchema()

    df.show()

    # Verify that Row_ID exists in the schema
    if "Row_ID" not in df.columns:
        raise ValueError("Row_ID column not found in the CSV data")

    # Clean and transform the data
    df_cleaned = clean_sales_data(df)
    df_transformed = cast_columns(df_cleaned)

    # Get PostgreSQL configuration
    config = get_postgres_config()

    # Write the data to PostgreSQL
    df_transformed.write \
        .format("jdbc") \
        .option("url", f"jdbc:postgresql://{config['host']}:{config['port']}/{config['dbname']}") \
        .option("dbtable", "retail_sales") \
        .option("user", config["user"]) \
        .option("password", config["password"]) \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()
