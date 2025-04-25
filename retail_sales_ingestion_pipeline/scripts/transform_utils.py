from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def clean_sales_data(df: DataFrame) -> DataFrame:
    return df.dropna().dropDuplicates()

def cast_columns(df: DataFrame) -> DataFrame:
    return df.withColumn("Quantity", col("Quantity").cast("integer")) \
             .withColumn("Sales_Amount", col("Sales_Amount").cast("float"))
