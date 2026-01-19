#!/usr/bin/env python3
"""
Complete normalization verification script.
Compares CSV output with Spider output to ensure all columns match correctly.
"""

# This script should be run in Databricks notebook format
# Adding as a notebook cell for execution

notebook_cell = """
# COMMAND ----------

# MAGIC %md
# MAGIC ## Verification: Complete Normalization Check
# MAGIC 
# MAGIC This cell verifies that CSV normalization produces the same structure as Spider processing.

# COMMAND ----------

print("=" * 100)
print("COMPLETE NORMALIZATION VERIFICATION")
print("=" * 100)

# Step 1: Process a sample of CSV data through normalization
print("\n" + "=" * 100)
print("STEP 1: CSV Data Normalization")
print("=" * 100)

# Read sample CSV edges
sample_csv_edges = csv_edges_df.limit(100)

# Apply normalization logic (same as in main notebook)
csv_sample = sample_csv_edges.select(
    F.col("~from").alias("src"),
    F.col("~to").alias("dst"),
    F.col("~label").alias("identifier_source")
)

# Extract business_unit and customer_id
csv_sample = csv_sample.withColumn(
    "src_parts",
    F.split(F.col("src"), "_", 2)
).withColumn(
    "business_unit",
    F.col("src_parts")[0]
).withColumn(
    "customer_id",
    F.when(
        F.size(F.col("src_parts")) > 1,
        F.col("src_parts")[1]
    ).otherwise(F.lit(None))
).drop("src_parts")

csv_sample = csv_sample.withColumn(
    "customer_id",
    F.col("customer_id").cast("string")
)

# Join with customer table
spark.sql("REFRESH TABLE public_edw_base_grain_live.customer")
customer_lookup = (
    spark.table("public_edw_base_grain_live.customer")
    .select(
        F.col("bob_entity_code").alias("business_unit"),
        F.cast(F.col("customer_id"), "string").alias("customer_id"),
        F.col("customer_uuid")
    )
    .distinct()
)

csv_sample = csv_sample.join(
    customer_lookup,
    on=["business_unit", "customer_id"],
    how="left"
)

# Join with vertices for created_at
customer_vertices_sample = vertices_df.filter(
    (F.col("~label") == "customer") & F.col("created_at").isNotNull()
).select(
    F.col("~id").alias("src_original"),
    F.col("created_at")
)

csv_sample = csv_sample.withColumn(
    "src_original",
    F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))
).join(
    customer_vertices_sample,
    on="src_original",
    how="left"
).drop("src_original")

# Normalize src
csv_sample = csv_sample.withColumn(
    "src",
    F.when(
        F.col("customer_uuid").isNotNull(),
        F.concat(F.lit("customer:"), F.col("business_unit"), F.lit("_"), F.col("customer_uuid"))
    ).otherwise(F.col("src"))
)

# Add other required columns (matching Spider output structure)
csv_sample = csv_sample.withColumn(
    "subscribed_at_local",
    F.to_timestamp(F.col("created_at"))
)

# Calculate count_connections (simplified for sample)
window_spec_identifier = Window.partitionBy("dst")
csv_sample = csv_sample.withColumn(
    "count_connections",
    F.count("*").over(window_spec_identifier)
)

# Calculate parent relationships (simplified for sample)
identifier_key_array = ["dst"]
csv_sample = csv_sample.withColumn(
    "created_at_ts",
    F.to_timestamp(F.col("created_at"))
)

window_spec = (
    Window.partitionBy(*identifier_key_array)
    .orderBy("created_at_ts")
    .rowsBetween(Window.unboundedPreceding, -1)
)

window_spec_bu = (
    Window.partitionBy(*(["business_unit"] + identifier_key_array))
    .orderBy("created_at_ts")
    .rowsBetween(Window.unboundedPreceding, -1)
)

self_id_col = F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))

csv_sample = csv_sample.withColumn(
    "has_direct_parent_in_business_unit",
    F.first(F.lit(True)).over(window_spec_bu).isNotNull(),
).withColumn(
    "direct_parent_in_business_unit",
    F.first(
        F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))
    ).over(window_spec_bu),
).withColumn(
    "has_direct_parent", 
    F.first(F.lit(True)).over(window_spec).isNotNull()
).withColumn(
    "direct_parent",
    F.first(
        F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))
    ).over(window_spec),
).drop("created_at_ts")

# Nullify self-references
csv_sample = csv_sample.withColumn(
    "direct_parent_in_business_unit",
    F.when(
        self_id_col == F.col("direct_parent_in_business_unit"), 
        F.lit(None)
    ).otherwise(F.col("direct_parent_in_business_unit"))
).withColumn(
    "direct_parent",
    F.when(
        self_id_col == F.col("direct_parent"), 
        F.lit(None)
    ).otherwise(F.col("direct_parent"))
)

# Select final columns (matching Spider output)
csv_sample_final = csv_sample.select(
    "business_unit",
    "customer_id",
    "customer_uuid",
    "created_at",
    "subscribed_at_local",
    "src",
    "dst",
    "identifier_source",
    "has_direct_parent_in_business_unit",
    "direct_parent_in_business_unit",
    "has_direct_parent",
    "direct_parent",
    "count_connections"
)

print("\n📊 CSV Sample Output Schema:")
csv_sample_final.printSchema()

print("\n📊 CSV Sample Output (first 10 records):")
csv_sample_final.show(10, truncate=False)

# Step 2: Process a sample of Spider data
print("\n" + "=" * 100)
print("STEP 2: Spider Data Processing (Reference)")
print("=" * 100)

# Get sample Spider data
spark.sql("REFRESH TABLE payments_hf.checkout_customer_details_spider")
spider_sample_df = (
    spark.table("payments_hf.checkout_customer_details_spider")
    .limit(10)
    .select(
        'customer_uuid', 'business_unit', 'customer_id', 'subscribed_at_local', 
        'first_name', 'last_name', 'phone', 'postcode', 'address', 
        'account_email', 'card_first_6', 'card_last_2', 'shopper_email', 'ip'
    )
)

# Process through AttributeProcessor (same as main notebook)
cd_df_sample = (
    spider_sample_df.join(spark.table("payments_hf.business_units_view"), "business_unit", "left")
    .withColumn("checkout_time_utc_iso", F.col("subscribed_at_local").cast('string'))
    .where("checkout_time_utc_iso is not null")
    .withColumn("country", F.col("country"))
    .withColumn("language", F.col("language"))
)

cd_df_sample = process_all(cd_df_sample)

cd1_df_sample = cd_df_sample.withColumn("customer_node", F.col('customer'))
cd2_df_sample = cd1_df_sample.withColumn("attribute_nodes", F.col('identifiers')).withColumn(
    "attribute_nodes",
    F.filter("attribute_nodes", lambda x: x["identifier"].isNotNull()),
)
cd3_df_sample = cd2_df_sample.withColumn("attribute_node", F.explode("attribute_nodes"))

# Calculate relationships (simplified for sample)
identifier_key_array_spider = ["attribute_node.identifier"]
window_spec_spider = (
    Window.partitionBy(*identifier_key_array_spider)
    .orderBy("subscribed_at_local")
    .rowsBetween(Window.unboundedPreceding, -1)
)
window_spec_bu_spider = (
    Window.partitionBy(*(["business_unit"] + identifier_key_array_spider))
    .orderBy("subscribed_at_local")
    .rowsBetween(Window.unboundedPreceding, -1)
)

cd4_df_sample = (
    cd3_df_sample.withColumn(
        "has_direct_parent_in_business_unit",
        F.first(F.lit(True)).over(window_spec_bu_spider).isNotNull(),
    )
    .withColumn(
        "direct_parent_in_business_unit",
        F.first(
            F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))
        ).over(window_spec_bu_spider),
    )
    .withColumn(
        "has_direct_parent", 
        F.first(F.lit(True)).over(window_spec_spider).isNotNull()
    )
    .withColumn(
        "direct_parent",
        F.first(
            F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))
        ).over(window_spec_spider),
    )
    .withColumn(
        "count_connections",
        F.approxCountDistinct("customer_node").over(
            Window.partitionBy(*identifier_key_array_spider)
        ),
    )
)

spider_sample_final = cd4_df_sample.select(
    "business_unit",
    "customer_id",
    "customer_uuid",
    "created_at",
    "subscribed_at_local",
    F.col("customer_node").alias("src"),
    F.col("attribute_node.identifier").alias("dst"),
    "attribute_node.identifier_source",
    "has_direct_parent_in_business_unit",
    "direct_parent_in_business_unit",
    "has_direct_parent",
    "direct_parent",
    "count_connections",
)

print("\n📊 Spider Sample Output Schema:")
spider_sample_final.printSchema()

print("\n📊 Spider Sample Output (first 10 records):")
spider_sample_final.show(10, truncate=False)

# Step 3: Compare schemas and structures
print("\n" + "=" * 100)
print("STEP 3: Schema Comparison")
print("=" * 100)

csv_columns = set(csv_sample_final.columns)
spider_columns = set(spider_sample_final.columns)

print(f"\n📋 CSV Columns ({len(csv_columns)}): {sorted(csv_columns)}")
print(f"📋 Spider Columns ({len(spider_columns)}): {sorted(spider_columns)}")

if csv_columns == spider_columns:
    print("\n✅ Column names match perfectly!")
else:
    print("\n⚠️  Column name differences:")
    only_csv = csv_columns - spider_columns
    only_spider = spider_columns - csv_columns
    if only_csv:
        print(f"   Only in CSV: {only_csv}")
    if only_spider:
        print(f"   Only in Spider: {only_spider}")

# Compare data types
print("\n📊 Data Type Comparison:")
csv_schema = {field.name: field.dataType for field in csv_sample_final.schema.fields}
spider_schema = {field.name: field.dataType for field in spider_sample_final.schema.fields}

for col in sorted(csv_columns & spider_columns):
    csv_type = str(csv_schema[col])
    spider_type = str(spider_schema[col])
    match = "✅" if csv_type == spider_type else "⚠️"
    print(f"   {match} {col}: CSV={csv_type}, Spider={spider_type}")

# Step 4: Check specific normalization points
print("\n" + "=" * 100)
print("STEP 4: Normalization Verification")
print("=" * 100)

# Check src format
csv_src_formats = csv_sample_final.select("src").distinct().collect()
spider_src_formats = spider_sample_final.select("src").distinct().collect()

print("\n📊 src Format Check:")
print(f"   CSV src formats (sample): {[row['src'] for row in csv_src_formats[:5]]}")
print(f"   Spider src formats (sample): {[row['src'] for row in spider_src_formats[:5]]}")

csv_customer_prefix = csv_sample_final.filter(F.col("src").rlike("^customer:")).count()
csv_total = csv_sample_final.count()
spider_customer_prefix = spider_sample_final.filter(F.col("src").rlike("^customer:")).count()
spider_total = spider_sample_final.count()

print(f"\n   CSV: {csv_customer_prefix}/{csv_total} records have 'customer:' prefix ({csv_customer_prefix/csv_total*100:.1f}%)")
print(f"   Spider: {spider_customer_prefix}/{spider_total} records have 'customer:' prefix ({spider_customer_prefix/spider_total*100:.1f}%)")

if csv_customer_prefix == csv_total and spider_customer_prefix == spider_total:
    print("   ✅ All src formats match!")
else:
    print("   ⚠️  Some src formats don't match")

# Check customer_uuid presence
csv_with_uuid = csv_sample_final.filter(F.col("customer_uuid").isNotNull()).count()
spider_with_uuid = spider_sample_final.filter(F.col("customer_uuid").isNotNull()).count()

print(f"\n📊 customer_uuid Check:")
print(f"   CSV: {csv_with_uuid}/{csv_total} records have customer_uuid ({csv_with_uuid/csv_total*100:.1f}%)")
print(f"   Spider: {spider_with_uuid}/{spider_total} records have customer_uuid ({spider_with_uuid/spider_total*100:.1f}%)")

# Check created_at format
print(f"\n📊 created_at Format Check:")
csv_created_at_sample = csv_sample_final.select("created_at").limit(3).collect()
spider_created_at_sample = spider_sample_final.select("created_at").limit(3).collect()
print(f"   CSV created_at (sample): {[str(row['created_at']) for row in csv_created_at_sample]}")
print(f"   Spider created_at (sample): {[str(row['created_at']) for row in spider_created_at_sample]}")

# Step 5: Summary
print("\n" + "=" * 100)
print("STEP 5: Summary")
print("=" * 100)

issues = []
if csv_columns != spider_columns:
    issues.append("Column names don't match")
if csv_customer_prefix < csv_total:
    issues.append(f"Some CSV records don't have 'customer:' prefix ({csv_total - csv_customer_prefix} records)")
if csv_with_uuid < csv_total:
    issues.append(f"Some CSV records missing customer_uuid ({csv_total - csv_with_uuid} records)")

if issues:
    print("\n⚠️  Issues Found:")
    for issue in issues:
        print(f"   - {issue}")
else:
    print("\n✅ All normalization checks passed!")
    print("   - Column names match")
    print("   - src formats match")
    print("   - customer_uuid present")
    print("   - Schema structures compatible")

print("\n" + "=" * 100)
"""

# Write as a notebook file that can be added to the main notebook
with open("/Users/visal.kumar/Documents/databricks/cursor_databricks/projects/post-spider-revamp/VERIFICATION_CELL.md", "w") as f:
    f.write("# Verification Cell for Notebook\n\n")
    f.write("Add this cell to the notebook after Step 2 (CSV normalization) to verify all normalization works correctly.\n\n")
    f.write("```python\n")
    f.write(notebook_cell)
    f.write("\n```\n")

print("✅ Verification script created!")
print("📝 Add the content from VERIFICATION_CELL.md to your notebook as a new cell")
print("   This will verify that CSV normalization produces the same structure as Spider processing")






