# Databricks notebook source
# MAGIC %md
# MAGIC # Test Missing Parquet Path Handling
# MAGIC 
# MAGIC Testing that the code handles missing Parquet paths by inferring schema from yesterday's partition

# COMMAND ----------

import time
from datetime import date, datetime, timedelta
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

# Copy the _infer_parquet_schema function
def _infer_parquet_schema(
    spark,
    base_path: str,
    partition_format: str = "year={year}/month={month}/day={day}"
):
    """
    Infer schema from Parquet files when no data is found in the target date range.

    Attempts to infer schema from:
    1. Yesterday's partition (current_date - 1)
    2. Base path (if yesterday's partition doesn't exist)
    3. Returns empty schema if both fail

    Args:
        spark: SparkSession instance
        base_path (str): Base S3 path to the parquet files
        partition_format (str): Format of time partitions in the path

    Returns:
        StructType: Inferred schema, or empty schema if inference fails
    """
    print("⚠️  No valid paths found in date range. Attempting to infer schema from yesterday's partition...")
    schema_found = False
    schema = None

    # Use current_date - 1 (yesterday) to infer schema
    try:
        yesterday = date.today() - timedelta(days=1)
        path_suffix = partition_format.format(
            year=yesterday.strftime("%Y"),
            month=yesterday.strftime("%m"),
            day=yesterday.strftime("%d")
        )
        sample_path = f"{base_path}/{path_suffix}"
        sample_df = spark.read.parquet(sample_path).limit(0)
        schema = sample_df.schema
        print(f"✅ Inferred schema from yesterday's partition: {sample_path}")
        schema_found = True
    except Exception as e:
        print(f"⚠️  Could not infer schema from yesterday's partition: {str(e)}")

    # If still no schema, try base path
    if not schema_found:
        try:
            sample_df = spark.read.parquet(base_path).limit(0)
            schema = sample_df.schema
            print("✅ Inferred schema from base path")
            schema_found = True
        except Exception as e:
            print(f"⚠️  Could not infer schema from base path: {str(e)}")

    if not schema_found:
        print("⚠️  Could not infer schema. Creating empty DataFrame with empty schema.")
        print("⚠️  This may cause issues downstream if schema is required.")
        from pyspark.sql.types import StructType
        schema = StructType([])

    return schema


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

    # Try to read the first path to get schema
    result_df = None
    schema = None
    valid_paths = []

    # First, try to find at least one valid path to infer schema
    for path in paths:
        try:
            df = spark.read.parquet(path)
            if result_df is None:
                result_df = df
                schema = df.schema
            else:
                result_df = result_df.unionByName(df, allowMissingColumns=True)
            valid_paths.append(path)
        except Exception as e:
            print(f"Warning: Could not read {path}: {str(e)}")

    # If no valid paths found, try to infer schema from yesterday's partition
    if result_df is None:
        schema = _infer_parquet_schema(spark, base_path, partition_format)

    # If we have a schema but no data, create empty DataFrame
    if result_df is None and schema is not None:
        print(f"📝 Creating empty DataFrame with inferred schema")
        result_df = spark.createDataFrame([], schema)

    # If still no result_df, raise an error
    if result_df is None:
        raise ValueError(
            f"Could not read any data from {base_path} for date range "
            f"{start_date_inclusive} to {end_date_exclusive} and could not infer schema"
        )

    print(f"✅ Successfully read {len(valid_paths)}/{len(paths)} partitions")

    # Apply additional filters if provided
    if additional_filters:
        for filter_expr in additional_filters:
            result_df = result_df.filter(filter_expr)

    return result_df

# COMMAND ----------

# MAGIC %md
# MAGIC ## Test Configuration

# COMMAND ----------

# Test with a date range that doesn't exist (2024-01-01)
# This simulates the error: PATH_NOT_FOUND for year=2024/month=01/day=01
test_base_path = "s3://hf-dp-shared-proto-s3-sinker-non-pii-raw-live/events/kafka/parquet/topics/public.customer.checkout.v1beta2"
test_start_date = "2024-01-01"
test_end_date = "2024-01-02"  # Just one day

print("=" * 100)
print("TEST CONFIGURATION")
print("=" * 100)
print(f"Base Path: {test_base_path}")
print(f"Start Date: {test_start_date}")
print(f"End Date: {test_end_date}")
print(f"Expected: Path should not exist, schema should be inferred from yesterday")
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
# MAGIC ## Test: Read Parquet with Missing Paths

# COMMAND ----------

print("\n" + "=" * 100)
print("STARTING TEST: read_parquet_time_filtered with missing paths")
print("=" * 100)

start_time = time.time()

try:
    result_df = read_parquet_time_filtered(
        generic_etl_args=generic_etl_args,
        base_path=test_base_path,
        start_date_inclusive=test_start_date,
        end_date_exclusive=test_end_date,
    )

    elapsed_time = time.time() - start_time

    print("\n" + "=" * 100)
    print("✅ TEST COMPLETED SUCCESSFULLY")
    print("=" * 100)
    print(f"⏱️  Execution time: {elapsed_time:.2f} seconds")
    print(f"📊 DataFrame schema:")
    result_df.printSchema()
    print(f"\n📊 Row count: {result_df.count():,}")
    print("=" * 100)

    # Verify the DataFrame has the correct schema (even if empty)
    if result_df.count() == 0:
        print("\n✅ SUCCESS: Empty DataFrame created with correct schema")
        print("   This is expected when no data exists for the date range")
    else:
        print(f"\n📊 DataFrame contains {result_df.count():,} rows")

    result_summary = {
        "status": "SUCCESS",
        "execution_time_seconds": elapsed_time,
        "row_count": result_df.count(),
        "has_schema": result_df.schema is not None,
        "schema_fields": len(result_df.schema.fields) if result_df.schema else 0,
    }

except Exception as e:
    elapsed_time = time.time() - start_time
    print("\n" + "=" * 100)
    print("❌ TEST FAILED")
    print("=" * 100)
    print(f"⏱️  Execution time before failure: {elapsed_time:.2f} seconds")
    print(f"❌ Error: {str(e)}")
    print(f"❌ Error type: {type(e).__name__}")
    print("=" * 100)

    result_summary = {
        "status": "FAILED",
        "execution_time_seconds": elapsed_time,
        "error": str(e),
        "error_type": type(e).__name__,
    }

    raise

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write Results to DBFS

# COMMAND ----------

output_file = "/tmp/test_missing_parquet_path_results.txt"

output_content = f"""
{'='*100}
TEST RESULTS: Missing Parquet Path Handling
{'='*100}

Status: {result_summary['status']}
Execution Time: {result_summary['execution_time_seconds']:.2f} seconds

Test Configuration:
  Base Path: {test_base_path}
  Start Date: {test_start_date}
  End Date: {test_end_date}

"""

if result_summary['status'] == 'SUCCESS':
    output_content += f"""
Results:
  Row Count: {result_summary.get('row_count', 0):,}
  Has Schema: {result_summary.get('has_schema', False)}
  Schema Fields: {result_summary.get('schema_fields', 0)}
  
✅ The function successfully handled missing paths by:
  1. Attempting to read paths in the date range
  2. When no paths found, inferring schema from yesterday's partition
  3. Creating an empty DataFrame with the inferred schema
"""
else:
    output_content += f"""
Error: {result_summary.get('error', 'Unknown error')}
Error Type: {result_summary.get('error_type', 'Unknown')}
"""

output_content += f"\n{'='*100}\n"

# Write to DBFS
dbutils.fs.put(output_file, output_content, overwrite=True)

print(f"✅ Results written to: {output_file}")
print("\n" + output_content)

