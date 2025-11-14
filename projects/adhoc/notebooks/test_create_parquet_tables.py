# Databricks notebook source
# MAGIC %md
# MAGIC # Test create_parquet_tables Function
# MAGIC 
# MAGIC Testing the `create_parquet_tables` function with 7 days of data

# COMMAND ----------

import time
from datetime import datetime, timedelta
from typing import Optional, List, Union
from pyspark.sql import DataFrame

# COMMAND ----------

# MAGIC %md
# MAGIC ## Setup: Mock GenericETLArgs and Functions

# COMMAND ----------

# Simple mock class for testing
class GenericETLArgs:
    def __init__(self, spark):
        self.spark = spark

# Copy the read_parquet_time_filtered function
def read_parquet_time_filtered(
    generic_etl_args: GenericETLArgs,
    base_path: str,
    start_date_inclusive: Union[str, datetime],
    end_date_exclusive: Union[str, datetime],
    partition_format: str = "year={year}/month={month}/day={day}",
    additional_filters: Optional[List[str]] = None
) -> DataFrame:
    """
    Read partitioned parquet files from S3 for a given time period.
    """
    spark = generic_etl_args.spark
    
    # Convert string dates to datetime if needed
    if isinstance(start_date_inclusive, str):
        start_date = datetime.strptime(start_date_inclusive, "%Y-%m-%d")
    else:
        start_date = start_date_inclusive
    
    if isinstance(end_date_exclusive, str):
        end_date = datetime.strptime(end_date_exclusive, "%Y-%m-%d")
    else:
        end_date = end_date_exclusive
    
    # Generate list of dates between start and end (exclusive)
    date_list = []
    current_date = start_date
    while current_date < end_date:
        date_list.append(current_date)
        current_date += timedelta(days=1)
    
    if not date_list:
        raise ValueError(f"No dates in range {start_date_inclusive} to {end_date_exclusive}")
    
    # Generate list of paths for each date
    paths = []
    for date in date_list:
        path_suffix = partition_format.format(
            year=date.strftime("%Y"),
            month=date.strftime("%m"),
            day=date.strftime("%d")
        )
        full_path = f"{base_path}/{path_suffix}"
        paths.append(full_path)
    
    # Read and union dataframes
    print(f"Reading {len(paths)} date partitions from {base_path}")
    
    result_df = spark.read.parquet(paths[0])
    
    # Union with remaining paths if there are more than one
    for path in paths[1:]:
        try:
            df = spark.read.parquet(path)
            result_df = result_df.unionByName(df, allowMissingColumns=True)
        except Exception as e:
            print(f"Warning: Could not read {path}: {str(e)}")
    
    # Apply additional filters if provided
    if additional_filters:
        for filter_expr in additional_filters:
            result_df = result_df.filter(filter_expr)
    
    return result_df

# Copy the create_parquet_tables function
def create_parquet_tables(
    generic_etl_args: GenericETLArgs,
    parquet_configs: list,
    start_date: str,
    end_date_exclusive: str,
) -> list:
    """
    Create tables from multiple Parquet sources with time filtering.
    """
    spark = generic_etl_args.spark
    created_tables = []
    
    for config in parquet_configs:
        base_path = config["path"]
        table_name = config["table_name"]
        partition_format = config.get("partition_format", "year={year}/month={month}/day={day}")
        additional_filters = config.get("additional_filters", None)
        
        print(f"📖 Reading Parquet: {base_path}")
        print(f"   Creating table: {table_name}")
        
        df = read_parquet_time_filtered(
            generic_etl_args=generic_etl_args,
            base_path=base_path,
            start_date_inclusive=start_date,
            end_date_exclusive=end_date_exclusive,
            partition_format=partition_format,
            additional_filters=additional_filters,
        )
        
        # Count rows before writing (for logging)
        row_count = df.count()
        
        # Create table instead of temp view
        df.write.format("delta").mode("overwrite").saveAsTable(table_name)
        print(f"   ✅ Created table with {row_count:,} rows")
        created_tables.append(table_name)
    
    return created_tables

# COMMAND ----------

# MAGIC %md
# MAGIC ## Test Configuration

# COMMAND ----------

# Test with 7 days of data
end_date = datetime.now().date()
start_date = end_date - timedelta(days=6)  # 7 days total (inclusive)

start_date_str = str(start_date)
end_date_exclusive_str = str(end_date + timedelta(days=1))  # Exclusive end date

print("=" * 100)
print("TEST CONFIGURATION")
print("=" * 100)
print(f"Start Date (inclusive): {start_date_str}")
print(f"End Date (exclusive): {end_date_exclusive_str}")
print(f"Duration: 7 days")
print("=" * 100)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Initialize GenericETLArgs

# COMMAND ----------

# Create GenericETLArgs with current Spark session
generic_etl_args = GenericETLArgs(spark=spark)

print("✅ GenericETLArgs initialized")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Test: Create Parquet Tables

# COMMAND ----------

# Parquet configurations (same as production)
parquet_configs = [
    {
        "path": "s3://hf-dp-shared-proto-s3-sinker-non-pii-raw-live/events/kafka/parquet/topics/public.payment.method-listed.v1beta1",
        "table_name": "payments_hf.temp_payment_method_listed_test",
        "additional_filters": [
            "value.workflows = 'checkout'",
            "value.browser_version <> '51.0.2704'"
        ]
    },
    {
        "path": "s3://hf-dp-shared-proto-s3-sinker-non-pii-raw-live/events/kafka/parquet/topics/public.customer.checkout.v1beta2",
        "table_name": "payments_hf.temp_customer_checkout_test"
    },
    {
        "path": "s3://hf-dp-kts3-avro-pii-live/events/kafka/parquet/topics/public.fraud.checkout.customer.data.v2",
        "table_name": "payments_hf.temp_fraud_checkout_customer_data_test"
    }
]

print("\n" + "=" * 100)
print("STARTING TEST: create_parquet_tables")
print("=" * 100)
print(f"Number of tables to create: {len(parquet_configs)}")
print(f"Date range: {start_date_str} to {end_date_exclusive_str} (7 days)")
print("=" * 100)

# Start timing
start_time = time.time()

try:
    created_tables = create_parquet_tables(
        generic_etl_args=generic_etl_args,
        parquet_configs=parquet_configs,
        start_date=start_date_str,
        end_date_exclusive=end_date_exclusive_str,
    )
    
    elapsed_time = time.time() - start_time
    
    print("\n" + "=" * 100)
    print("✅ TEST COMPLETED SUCCESSFULLY")
    print("=" * 100)
    print(f"⏱️  Total execution time: {elapsed_time:.2f} seconds ({elapsed_time/60:.2f} minutes)")
    print(f"📊 Tables created: {len(created_tables)}")
    for table in created_tables:
        print(f"   - {table}")
    print("=" * 100)
    
    # Verify tables exist and get row counts
    print("\n📊 Verifying created tables:")
    print("-" * 100)
    for table_name in created_tables:
        try:
            row_count = spark.sql(f"SELECT COUNT(*) as cnt FROM {table_name}").collect()[0]['cnt']
            print(f"   ✅ {table_name}: {row_count:,} rows")
        except Exception as e:
            print(f"   ❌ {table_name}: Error - {str(e)}")
    
    result_summary = {
        "status": "SUCCESS",
        "execution_time_seconds": elapsed_time,
        "execution_time_minutes": elapsed_time / 60,
        "tables_created": len(created_tables),
        "table_names": created_tables,
        "start_date": start_date_str,
        "end_date_exclusive": end_date_exclusive_str,
        "duration_days": 7
    }
    
except Exception as e:
    elapsed_time = time.time() - start_time
    print("\n" + "=" * 100)
    print("❌ TEST FAILED")
    print("=" * 100)
    print(f"⏱️  Execution time before failure: {elapsed_time:.2f} seconds")
    print(f"❌ Error: {str(e)}")
    print("=" * 100)
    
    result_summary = {
        "status": "FAILED",
        "execution_time_seconds": elapsed_time,
        "error": str(e),
        "start_date": start_date_str,
        "end_date_exclusive": end_date_exclusive_str,
        "duration_days": 7
    }
    
    raise

# COMMAND ----------

# MAGIC %md
# MAGIC ## Cleanup: Drop Test Tables

# COMMAND ----------

print("\n" + "=" * 100)
print("🧹 CLEANUP: Dropping test tables")
print("=" * 100)

for table_name in created_tables:
    try:
        spark.sql(f"DROP TABLE IF EXISTS {table_name}")
        print(f"   🗑️  Dropped: {table_name}")
    except Exception as e:
        print(f"   ⚠️  Could not drop {table_name}: {str(e)}")

print("=" * 100)
print("✅ Cleanup completed")
print("=" * 100)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write Results to DBFS

# COMMAND ----------

output_file = "/tmp/test_create_parquet_tables_results.txt"

output_content = f"""
{'='*100}
TEST RESULTS: create_parquet_tables Function
{'='*100}

Status: {result_summary['status']}
Execution Time: {result_summary['execution_time_seconds']:.2f} seconds ({result_summary['execution_time_minutes']:.2f} minutes)
Date Range: {result_summary['start_date']} to {result_summary['end_date_exclusive']} ({result_summary['duration_days']} days)

Tables Created: {result_summary.get('tables_created', 0)}
"""

if result_summary['status'] == 'SUCCESS':
    output_content += "\nTable Names:\n"
    for table in result_summary.get('table_names', []):
        output_content += f"  - {table}\n"
else:
    output_content += f"\nError: {result_summary.get('error', 'Unknown error')}\n"

output_content += f"\n{'='*100}\n"

# Write to DBFS
dbutils.fs.put(output_file, output_content, overwrite=True)

print(f"✅ Results written to: {output_file}")
print("\n" + output_content)

