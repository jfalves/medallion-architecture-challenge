from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp
import os

base_path = "C:/BI/roya-medallion-solution"

def process_products(spark, base_path):
    # Paths for bronze and silver layers
    bronze_path = os.path.join(base_path, "bronze", "products")
    silver_path = os.path.join(base_path, "silver", "products")

    # Read data from bronze layer
    df = spark.read.parquet(bronze_path)

    # Clean and transform data
    df_cleaned = df \
        .withColumn("price", col("price").cast("double")) \
        .filter(col("product_id").isNotNull()) \
        .filter(col("price").isNotNull()) \
        .withColumn("cleaned_at", current_timestamp())

    # Write cleaned data to silver layer
    df_cleaned.write.mode("overwrite").parquet(silver_path)
    print(f"products table written to {silver_path}")

def process_purchases(spark, base_path):
    """
        Cleans and processes the products table from bronze to silver.
    """

    bronze_path = os.path.join(base_path, "bronze", "purchases")
    silver_path = os.path.join(base_path, "silver", "purchases")

    df = spark.read.parquet(bronze_path)
    df_cleaned = df \
        .withColumn("amount", col("amount").cast("double")) \
        .filter(col("user_id").isNotNull()) \
        .filter(col("product_id").isNotNull()) \
        .withColumn("cleaned_at", current_timestamp())

    df_cleaned.write.mode("overwrite").parquet(silver_path)
    print(f"purchases table written to {silver_path}")

def process_user_events(spark, base_path):
    bronze_path = os.path.join(base_path, "bronze", "user_events")
    silver_path = os.path.join(base_path, "silver", "user_events")

    df = spark.read.parquet(bronze_path)
    df_cleaned = df \
        .filter(col("event_type").isNotNull()) \
        .filter(col("user_id").isNotNull()) \
        .withColumn("cleaned_at", current_timestamp())

    df_cleaned.write.mode("overwrite").parquet(silver_path)
    print(f"user_events table written to {silver_path}")


def silver_layer_processing(spark, base_path):
    """
    Process the silver layer of data.
    This function is a placeholder for the actual processing logic.
    """
    print("Processing silver layer...")
    process_products(spark, base_path)
    process_purchases(spark, base_path)
    process_user_events(spark, base_path)
    print("Silver layer processing completed.")
    pass