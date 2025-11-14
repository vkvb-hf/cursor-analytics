# Databricks notebook source
# MAGIC %md
# MAGIC # Create Checkout Funnel Backend Temp Table
# MAGIC 
# MAGIC This notebook creates a temp table `payments_hf.checkout_funnel_backend_temp` 
# MAGIC for date 2025-11-01 using the checkout_funnel_backend logic.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Setup and Imports

# COMMAND ----------

from datetime import date
from ddi_framework.core.spark.transformation import DataFramePatch
from ddi_pays_pipelines.generic_etl_runner.generic_etl_args import GenericETLArgs
from ddi_pays_pipelines.generic_etls.checkout_funnel_backend import checkout_funnel_backend

# Apply DataFramePatch for custom DataFrame methods
DataFramePatch.patch()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

# Set the date for the temp table
etl_start_date = date(2025, 11, 1)
etl_end_date = date(2025, 11, 1)

# Table configuration
table_name = "checkout_funnel_backend_temp"
save_path = "s3://hf-payments-data-lake-live-main/payments_hf/checkout_funnel_backend_temp"

print(f"Creating temp table: payments_hf.{table_name}")
print(f"Date range: {etl_start_date} to {etl_end_date}")
print(f"Save path: {save_path}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create GenericETLArgs

# COMMAND ----------

# Create GenericETLArgs using the existing Spark session
# In Databricks, spark is already available
generic_etl_args = GenericETLArgs(
    spark=spark,
    environment="live",  # Adjust if needed
    etl_start_date_inclusive=etl_start_date,
    etl_end_date_inclusive=etl_end_date,
    settings=None
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Run Checkout Funnel Backend ETL

# COMMAND ----------

# Call the checkout_funnel_backend function with temp table parameters
checkout_funnel_backend(
    generic_etl_args=generic_etl_args,
    table_name=table_name,
    save_path=save_path
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verify Table Creation

# COMMAND ----------

# Verify the table was created and check row count
table_full_name = f"payments_hf.{table_name}"
row_count = spark.sql(f"SELECT COUNT(*) as count FROM {table_full_name}").collect()[0]['count']
print(f"✅ Table {table_full_name} created successfully!")
print(f"📊 Total rows: {row_count}")

# Show sample data
print("\n📋 Sample data:")
spark.sql(f"SELECT * FROM {table_full_name} LIMIT 5").show(truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC 
# MAGIC Temp table `payments_hf.checkout_funnel_backend_temp` has been created for date 2025-11-01.

