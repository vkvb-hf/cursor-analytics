# Databricks notebook source
# MAGIC %md
# MAGIC # Delete Partition event_date = '2023-12-31'
# MAGIC 
# MAGIC This notebook deletes the partition with event_date = '2023-12-31' from checkout_funnel_backend table

# COMMAND ----------

table_name = "payments_hf.checkout_funnel_backend"
partition_date = "2023-12-31"

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Check if partition exists

# COMMAND ----------

print("=" * 100)
print("CHECKING PARTITION BEFORE DELETION")
print("=" * 100)

# Check if partition exists and get row count
check_query = f"""
SELECT 
    COUNT(*) AS row_count,
    COUNT(DISTINCT customer_id) AS distinct_customers
FROM {table_name}
WHERE event_date = '{partition_date}'
"""

check_result = spark.sql(check_query).collect()[0]

print(f"\n📊 Partition {partition_date} status:")
print(f"   Row count: {check_result['row_count']:,}")
print(f"   Distinct customers: {check_result['distinct_customers']:,}")

if check_result['row_count'] == 0:
    print(f"\n⚠️  Partition {partition_date} has no data - nothing to delete")
else:
    print(f"\n✅ Partition {partition_date} exists with {check_result['row_count']:,} rows")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Delete the partition

# COMMAND ----------

if check_result['row_count'] > 0:
    print("\n" + "=" * 100)
    print("DELETING PARTITION")
    print("=" * 100)
    
    delete_query = f"""
    DELETE FROM {table_name}
    WHERE event_date = '{partition_date}'
    """
    
    print(f"\n🗑️  Executing DELETE for event_date = '{partition_date}'...")
    print(f"   Query: DELETE FROM {table_name} WHERE event_date = '{partition_date}'")
    
    try:
        spark.sql(delete_query)
        print(f"\n✅ Successfully deleted partition {partition_date}")
    except Exception as e:
        print(f"\n❌ Error deleting partition: {str(e)}")
        raise
else:
    print("\n⏭️  Skipping deletion - partition has no data")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Verify deletion

# COMMAND ----------

print("\n" + "=" * 100)
print("VERIFYING DELETION")
print("=" * 100)

# Check again after deletion
verify_result = spark.sql(check_query).collect()[0]

print(f"\n📊 Partition {partition_date} status after deletion:")
print(f"   Row count: {verify_result['row_count']:,}")
print(f"   Distinct customers: {verify_result['distinct_customers']:,}")

if verify_result['row_count'] == 0:
    print(f"\n✅ Partition {partition_date} successfully deleted (0 rows remaining)")
else:
    print(f"\n⚠️  WARNING: Partition still has {verify_result['row_count']:,} rows")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write Results

# COMMAND ----------

output_file = "/tmp/delete_partition_2023_12_31_results.txt"

output_content = f"""
{'='*100}
DELETE PARTITION RESULTS: {table_name}
{'='*100}

Partition: event_date = '{partition_date}'

Before Deletion:
  Row count: {check_result['row_count']:,}
  Distinct customers: {check_result['distinct_customers']:,}

After Deletion:
  Row count: {verify_result['row_count']:,}
  Distinct customers: {verify_result['distinct_customers']:,}

Status: {'✅ Successfully deleted' if verify_result['row_count'] == 0 and check_result['row_count'] > 0 else '⚠️  No action taken or deletion incomplete'}

{'='*100}
"""

dbutils.fs.put(output_file, output_content, overwrite=True)
print(f"\n✅ Results written to: {output_file}")
print("\n" + output_content)

