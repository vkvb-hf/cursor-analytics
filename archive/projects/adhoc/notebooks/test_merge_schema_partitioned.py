# Databricks notebook source
# MAGIC %md
# MAGIC # Test mergeSchema with Partitioned Delta Table
# MAGIC 
# MAGIC This notebook tests adding new columns to a partitioned Delta table using mergeSchema + replaceWhere

# COMMAND ----------

# Step 1: Create a temporary test table with event_date partition
print("=" * 100)
print("STEP 1: Creating initial test table with sample data")
print("=" * 100)

# Create sample data with multiple date partitions
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType
from datetime import datetime, timedelta

# Sample data for different dates
test_data = [
    Row(customer_id=1, country="US", event_date="2024-01-01", value1=100, value2="A"),
    Row(customer_id=2, country="US", event_date="2024-01-01", value1=200, value2="B"),
    Row(customer_id=3, country="UK", event_date="2024-01-02", value1=300, value2="C"),
    Row(customer_id=4, country="UK", event_date="2024-01-02", value1=400, value2="D"),
    Row(customer_id=5, country="DE", event_date="2024-01-03", value1=500, value2="E"),
    Row(customer_id=6, country="DE", event_date="2024-01-03", value1=600, value2="F"),
]

# Create DataFrame
df_initial = spark.createDataFrame(test_data)

# Convert event_date to DateType
from pyspark.sql.functions import to_date
df_initial = df_initial.withColumn("event_date", to_date("event_date"))

# Use the actual table path and name
save_path = "s3://hf-payments-data-lake-live-main/payments_hf/checkout_funnel_backend_test_20251112"
database = "payments_hf"
table_name = "checkout_funnel_backend_test_20251112"
temp_table_name = f"{database}.{table_name}"

# Drop table if exists
spark.sql(f"DROP TABLE IF EXISTS {temp_table_name}")

# Write initial table with partition - using same config as production
print(f"\n📝 Creating table with production-like configuration:")
print(f"   Table: {temp_table_name}")
print(f"   Path: {save_path}")
print(f"   Partitioned by: event_date")
print(f"   Using: partitionOverwriteMode='dynamic'")

df_initial.write.format("delta") \
    .mode("overwrite") \
    .option("path", save_path) \
    .partitionBy(["event_date"]) \
    .option("spark.databricks.delta.autoCompact.enabled", "true") \
    .option("spark.databricks.delta.optimizeWrite.enabled", "true") \
    .option("spark.databricks.delta.vacuum.parallelDelete.enabled", "true") \
    .option("partitionOverwriteMode", "dynamic") \
    .saveAsTable(temp_table_name)

print(f"\n✅ Created table: {temp_table_name}")
print(f"   Path: {save_path}")
print(f"   Partitioned by: event_date")

# Show initial data
print("\n📊 Initial table data:")
spark.table(temp_table_name).show(truncate=False)

# Show schema
print("\n📋 Initial schema:")
spark.table(temp_table_name).printSchema()

# Count partitions
partition_count = spark.sql(f"SELECT COUNT(DISTINCT event_date) as partition_count FROM {temp_table_name}").collect()[0]['partition_count']
print(f"\n📦 Number of partitions: {partition_count}")

# COMMAND ----------

# Step 2: Verify initial state
print("\n" + "=" * 100)
print("STEP 2: Verifying initial state")
print("=" * 100)

# Get all data
all_data = spark.table(temp_table_name).orderBy("event_date", "customer_id").collect()
print(f"\n✅ Total rows in table: {len(all_data)}")

# Show data by partition
for row in all_data:
    print(f"   Partition {row['event_date']}: customer_id={row['customer_id']}, country={row['country']}, value1={row['value1']}, value2={row['value2']}")

# COMMAND ----------

# Step 3: Add new column using mergeSchema + replaceWhere
print("\n" + "=" * 100)
print("STEP 3: Adding new column using mergeSchema + replaceWhere")
print("=" * 100)

# Create new DataFrame with additional column for specific date range
# We'll only update 2024-01-02 partition
new_data = [
    Row(customer_id=3, country="UK", event_date="2024-01-02", value1=300, value2="C", new_column="NEW_VALUE_1"),
    Row(customer_id=4, country="UK", event_date="2024-01-02", value1=400, value2="D", new_column="NEW_VALUE_2"),
]

df_with_new_column = spark.createDataFrame(new_data)
df_with_new_column = df_with_new_column.withColumn("event_date", to_date("event_date"))

print(f"\n📝 New data to write (with new_column):")
df_with_new_column.show(truncate=False)

# Date range for replaceWhere
start_date = "2024-01-02"
end_date = "2024-01-02"

print(f"\n🔄 Writing with mergeSchema=true and replaceWhere='event_date >= {start_date} AND event_date <= {end_date}'")

# Write with mergeSchema and replaceWhere (replacing partitionOverwriteMode)
# Note: mergeSchema and partitionOverwriteMode cannot be used together
df_with_new_column.write.format("delta") \
    .mode("overwrite") \
    .option("path", save_path) \
    .partitionBy(["event_date"]) \
    .option("mergeSchema", "true") \
    .option("replaceWhere", f"event_date >= '{start_date}' AND event_date <= '{end_date}'") \
    .option("spark.databricks.delta.autoCompact.enabled", "true") \
    .option("spark.databricks.delta.optimizeWrite.enabled", "true") \
    .option("spark.databricks.delta.vacuum.parallelDelete.enabled", "true") \
    .saveAsTable(temp_table_name)

print("✅ Write completed!")

# COMMAND ----------

# Step 4: Verify results
print("\n" + "=" * 100)
print("STEP 4: Verifying results after schema merge")
print("=" * 100)

# Show updated schema
print("\n📋 Updated schema (should include new_column):")
spark.table(temp_table_name).printSchema()

# Show all data
print("\n📊 All table data after merge:")
result_df = spark.table(temp_table_name).orderBy("event_date", "customer_id")
result_df.show(truncate=False)

# Verify each partition
print("\n🔍 Partition-by-partition verification:")

# Check 2024-01-01 partition (should have NULL for new_column)
partition_2024_01_01 = spark.sql(f"""
    SELECT * FROM {temp_table_name} 
    WHERE event_date = '2024-01-01'
    ORDER BY customer_id
""").collect()

print(f"\n   Partition 2024-01-01 (should have NULL new_column):")
for row in partition_2024_01_01:
    try:
        new_col_val = row['new_column']
    except (KeyError, AttributeError):
        new_col_val = 'COLUMN_NOT_FOUND'
    print(f"      customer_id={row['customer_id']}, new_column={new_col_val}")

# Check 2024-01-02 partition (should have values for new_column)
partition_2024_01_02 = spark.sql(f"""
    SELECT * FROM {temp_table_name} 
    WHERE event_date = '2024-01-02'
    ORDER BY customer_id
""").collect()

print(f"\n   Partition 2024-01-02 (should have values for new_column):")
for row in partition_2024_01_02:
    try:
        new_col_val = row['new_column']
    except (KeyError, AttributeError):
        new_col_val = 'COLUMN_NOT_FOUND'
    print(f"      customer_id={row['customer_id']}, new_column={new_col_val}")

# Check 2024-01-03 partition (should have NULL for new_column)
partition_2024_01_03 = spark.sql(f"""
    SELECT * FROM {temp_table_name} 
    WHERE event_date = '2024-01-03'
    ORDER BY customer_id
""").collect()

print(f"\n   Partition 2024-01-03 (should have NULL new_column):")
for row in partition_2024_01_03:
    try:
        new_col_val = row['new_column']
    except (KeyError, AttributeError):
        new_col_val = 'COLUMN_NOT_FOUND'
    print(f"      customer_id={row['customer_id']}, new_column={new_col_val}")

# COMMAND ----------

# Step 5: Summary and output
print("\n" + "=" * 100)
print("STEP 5: Test Summary")
print("=" * 100)

# Build output summary
output_lines = []
output_lines.append("=" * 100)
output_lines.append("TEST RESULTS: mergeSchema + replaceWhere on Partitioned Delta Table")
output_lines.append("=" * 100)
output_lines.append("")

# Schema check
schema = spark.table(temp_table_name).schema
has_new_column = "new_column" in [field.name for field in schema.fields]
output_lines.append(f"✅ Schema includes new_column: {has_new_column}")

if has_new_column:
    output_lines.append("")
    output_lines.append("Schema fields:")
    for field in schema.fields:
        output_lines.append(f"   - {field.name}: {field.dataType}")

# Data check
total_rows = spark.table(temp_table_name).count()
output_lines.append("")
output_lines.append(f"✅ Total rows in table: {total_rows}")

# Partition check
partitions = spark.sql(f"SELECT DISTINCT event_date FROM {temp_table_name} ORDER BY event_date").collect()
output_lines.append("")
output_lines.append(f"✅ Partitions: {[str(p['event_date']) for p in partitions]}")

# Verify new_column values
null_count = spark.sql(f"SELECT COUNT(*) as cnt FROM {temp_table_name} WHERE new_column IS NULL").collect()[0]['cnt']
not_null_count = spark.sql(f"SELECT COUNT(*) as cnt FROM {temp_table_name} WHERE new_column IS NOT NULL").collect()[0]['cnt']

output_lines.append("")
output_lines.append(f"✅ Rows with NULL new_column (preserved partitions): {null_count}")
output_lines.append(f"✅ Rows with values in new_column (updated partition): {not_null_count}")

# Final verification
output_lines.append("")
if has_new_column and null_count == 4 and not_null_count == 2:
    output_lines.append("🎉 TEST PASSED: Schema merge worked correctly!")
    output_lines.append("   - New column added to schema")
    output_lines.append("   - Only specified partition (2024-01-02) was overwritten")
    output_lines.append("   - Other partitions (2024-01-01, 2024-01-03) preserved with NULL new_column")
else:
    output_lines.append("❌ TEST FAILED: Unexpected results")
    output_lines.append(f"   - Has new_column: {has_new_column}")
    output_lines.append(f"   - NULL count: {null_count} (expected 4)")
    output_lines.append(f"   - NOT NULL count: {not_null_count} (expected 2)")

output_lines.append("")
output_lines.append("=" * 100)

# Write output to DBFS for retrieval
output_text = "\n".join(output_lines)
output_file = "/tmp/test_merge_schema_output.txt"
dbutils.fs.put(output_file, output_text, overwrite=True)

# Also print for UI visibility
print(output_text)

# COMMAND ----------

# Cleanup (optional - comment out if you want to inspect the table)
# spark.sql(f"DROP TABLE IF EXISTS {temp_table_name}")
# print("\n🧹 Cleaned up test table")

