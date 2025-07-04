from pyspark.sql import SparkSession
from layers.bronze import bronze_layer_processing
from layers.silver import silver_layer_processing
from layers.gold import gold_layer_processing
import os

def main():

    # Build SparkSession once
    spark = SparkSession.builder \
        .appName("MedallionArchitecturePipeline") \
        .getOrCreate()

    # Define base path
    base_path = "C:/BI/roya-medallion-solution"
    data_source_path = os.path.join(base_path, "data_source")

    print("Starting Medallion pipeline...")

    # Run Bronze Layer
    for file_name in os.listdir(data_source_path):
        if file_name.endswith((".csv", ".json")):
            bronze_layer_processing(spark, base_path, file_name)

    # Run Silver Layer
    silver_layer_processing(spark, base_path)

    # Run Gold Layer
    gold_layer_processing(spark, base_path)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
