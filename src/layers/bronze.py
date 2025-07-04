from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
import os

def bronze_layer_processing(spark, base_path, file_name):
    """
    Process the bronze layer of data.
    This function is responsible for initial data ingestion and basic transformations.
    """
    print("Processing bronze layer...")

    # Build the full path to the input file
    data_source_path = os.path.join(base_path, "data_source")
    bronze_path = os.path.join(base_path, "bronze")
    input_path = os.path.join(data_source_path, file_name)

    # Extract the table name by removing the file extension
    table_name = os.path.splitext(file_name)[0]

    # Build the output path for the bronze layer as bronze/<table_name>
    output_path = os.path.join(bronze_path, table_name)

    # Ensure the bronze directory exists
    os.makedirs(output_path, exist_ok=True)

    # Detect the file format based on the file extension
    file_format = file_name.split('.')[-1].lower()

    if file_format == 'csv':
        df = spark.read.option("header", True).csv(input_path)
    elif file_format == 'json':
        df = spark.read.json(input_path)
    else:
        raise ValueError("Unsupported format")

    df = df.withColumn("ingest_time", current_timestamp())
    df.write.mode("overwrite").parquet(output_path)
    print(f"{file_name} written to {output_path}")

    pass