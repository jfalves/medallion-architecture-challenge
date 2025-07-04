from pyspark.sql.functions import col, count, sum as sum_, current_timestamp
import os

def gold_layer_processing(spark, base_path):
    """
    Process the gold layer of the data pipeline.
    This function is responsible for aggregating and transforming data
    to create the final output that is ready for reporting or analysis.
    """
    print("Processing gold layer...")

    # Paths
    silver_path = os.path.join(base_path, "silver")
    gold_path = os.path.join(base_path, "gold", "product_summary")

    # Read data from silver layer
    purchases_df = spark.read.parquet(os.path.join(silver_path, "purchases"))
    products_df = spark.read.parquet(os.path.join(silver_path, "products"))
    user_events_df = spark.read.parquet(os.path.join(silver_path, "user_events"))

    # Aggregate purchase data
    purchase_summary = purchases_df.groupBy("product_id") \
        .agg(
        count("*").alias("purchase_count"),
        sum_("amount").alias("total_revenue")
    )

    # Aggregate events: total views, clicks, logins, logouts per product
    event_summary = user_events_df.groupBy("user_id", "event_type") \
        .count()

    # Join with products
    final_df = products_df \
        .join(purchase_summary, on="product_id", how="left") \
        .fillna(0, subset=["purchase_count", "total_revenue"]) \
        .withColumn("generated_at", current_timestamp())

    # Write to gold layer
    final_df.write.mode("overwrite").parquet(gold_path)
    print(f"Gold layer written to: {gold_path}")

    pass