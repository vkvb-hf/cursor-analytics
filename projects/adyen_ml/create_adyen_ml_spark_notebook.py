# Databricks notebook source
# MAGIC %md
# MAGIC # Create Adyen ML Test Data Table using PySpark
# MAGIC 
# MAGIC This notebook reads all CSV files in parallel and creates a Delta table.
# MAGIC Much faster than sequential SQL INSERTs!

# COMMAND ----------

# Risk profile mapping
RISK_PROFILE_MAPPING = {
    'THLH73H2VSWDN842': 'Jade1314 CANADA ML',
    'QNN7MK9V6T5T87F3': 'Very_High_ecomm',
    'TBDLJCJZX8LLWWF3': 'Medium_ecomm',
    'J2M3VKGZMHZNZ4Q9': 'Medium',
    'DXPLDK9V6T5T87F3': 'High_ecomm',
    'QLKKNG4S2Q9428Q9': 'Very_High',
    'ZDGX3H4S2Q9428Q9': 'High'
}

workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test"
table_name = "payments_hf.adyen_ml_test_data"
drop_if_exists = True

print("=" * 80)
print("Create Table using PySpark (Fast Parallel Processing)")
print("=" * 80)
print(f"\n📁 Workspace path: {workspace_path}")
print(f"🎯 Table name: {table_name}")
print("=" * 80)

# COMMAND ----------

# Step 1: Get CSV file paths using dbutils
print("\n📋 Step 1: Getting CSV file paths...")

files = dbutils.fs.ls(workspace_path)
csv_paths = [f.path for f in files if f.name.endswith('.csv')]

if not csv_paths:
    raise Exception("No CSV files found!")

print(f"✅ Found {len(csv_paths)} CSV files")

# Show files
print("\n📄 Files to process:")
for i, csv_path in enumerate(csv_paths[:10], 1):
    filename = csv_path.split('/')[-1]
    print(f"   [{i:2d}] {filename}")
if len(csv_paths) > 10:
    print(f"   ... and {len(csv_paths) - 10} more files")

# COMMAND ----------

# Step 2: Read all CSV files in parallel with Spark
print(f"\n📥 Step 2: Reading {len(csv_paths)} CSV files in parallel...")
print("   ⚡ Spark will automatically parallelize this operation...")

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "false") \
    .option("comment", "#") \
    .option("multiLine", "false") \
    .option("ignoreLeadingWhiteSpace", "true") \
    .option("ignoreTrailingWhiteSpace", "true") \
    .csv(csv_paths)

row_count = df.count()
print(f"\n✅ Successfully read DataFrame")
print(f"   📊 Total rows: {row_count:,}")
print(f"   📋 Columns: {len(df.columns)}")
print(f"   📝 Columns: {', '.join(df.columns)}")

# COMMAND ----------

# Step 3: Add custom columns
print("\n🔧 Step 3: Adding custom columns...")

from pyspark.sql.functions import (
    col, 
    input_file_name, 
    regexp_extract,
    when,
    lit
)

# Get filename from input_file_name() - extract just the filename
df = df.withColumn(
    "source_filename",
    regexp_extract(input_file_name(), r"([^/]+\.csv)$", 1)
)

# Extract profile reference from filename
df = df.withColumn(
    "profile_reference",
    regexp_extract(col("source_filename"), r"_([A-Z0-9]{13})_", 1)
)

# Map risk profile based on profile_reference
risk_profile_expr = when(
    col("profile_reference") == "THLH73H2VSWDN842", lit("Jade1314 CANADA ML")
).when(
    col("profile_reference") == "QNN7MK9V6T5T87F3", lit("Very_High_ecomm")
).when(
    col("profile_reference") == "TBDLJCJZX8LLWWF3", lit("Medium_ecomm")
).when(
    col("profile_reference") == "J2M3VKGZMHZNZ4Q9", lit("Medium")
).when(
    col("profile_reference") == "DXPLDK9V6T5T87F3", lit("High_ecomm")
).when(
    col("profile_reference") == "QLKKNG4S2Q9428Q9", lit("Very_High")
).when(
    col("profile_reference") == "ZDGX3H4S2Q9428Q9", lit("High")
).otherwise(lit("Unknown"))

df = df.withColumn("risk_profile", risk_profile_expr)

print("✅ Added columns: source_filename, profile_reference, risk_profile")

# COMMAND ----------

# Step 4: Sanitize column names
print("\n🧹 Step 4: Sanitizing column names...")

for col_name in df.columns:
    if ' ' in col_name or any(char in col_name for char in [',', ';', '{', '}', '(', ')']):
        new_name = col_name.replace(' ', '_').replace(',', '_').replace(';', '_') \
            .replace('{', '_').replace('}', '_').replace('(', '_').replace(')', '_')
        df = df.withColumnRenamed(col_name, new_name)

print("✅ Column names sanitized")
print(f"   Columns: {', '.join(df.columns[:10])}...")

# COMMAND ----------

# Step 5: Remove duplicates
print("\n🔍 Step 5: Removing duplicates...")

row_count_before = df.count()
print(f"   Rows before deduplication: {row_count_before:,}")

df = df.dropDuplicates()
row_count_after = df.count()
duplicates_removed = row_count_before - row_count_after

print(f"✅ Removed {duplicates_removed:,} duplicate rows")
print(f"   Remaining rows: {row_count_after:,}")

# COMMAND ----------

# Step 6: Create Delta table
print(f"\n💾 Step 6: Creating Delta table '{table_name}'...")

schema, table = table_name.split('.') if '.' in table_name else ('default', table_name)
table_location = f"s3://hf-payments-data-lake-live-main/{schema}/{table}_v2"

if drop_if_exists:
    print("   Dropping existing table if it exists...")
    spark.sql(f"DROP TABLE IF EXISTS {table_name}")

# Write to Delta table partitioned by source_filename for better performance
print(f"   Writing to: {table_location}")
print(f"   Partitioned by: source_filename")
print("   ⚡ Spark will write in parallel...")

df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("path", table_location) \
    .option("overwriteSchema", "true") \
    .partitionBy("source_filename") \
    .saveAsTable(table_name)

print("✅ Delta table created successfully!")

# COMMAND ----------

# Step 7: Verification
print("\n📊 Step 7: Verification...")

result_df = spark.table(table_name)
total_rows = result_df.count()
distinct_files = result_df.select("source_filename").distinct().count()

print(f"✅ Table verification:")
print(f"   Total rows: {total_rows:,}")
print(f"   Distinct files: {distinct_files}")
print(f"   Columns: {len(result_df.columns)}")

# Show sample data
print("\n📋 Sample data:")
result_df.select("source_filename", "profile_reference", "risk_profile").distinct().show(20, truncate=False)

# COMMAND ----------

print("\n" + "=" * 80)
print("✅ SUCCESS! Table created using PySpark")
print(f"📊 Query your table: SELECT * FROM {table_name} LIMIT 10")
print("=" * 80)

