# Databricks notebook source
# MAGIC %md
# MAGIC # Test: Create Graph Customers with Successful Conversions Only

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.window import Window
from datetime import datetime

# Configuration
base_s3_path = "s3://hf-payments-data-lake-live-main/payments_hf/duplicate_customer_graph"
output_table = "payments_hf.customer_identifiers_20251121"

def save(df, name):
    """Save DataFrame to S3 and register as table in Glue."""
    s3_path = f"{base_s3_path}/{name}"
    table_name = f"payments_hf.{name}"
    print(f'\n💾 Dropping table if exists: {table_name}')
    spark.sql(f'drop table if exists {table_name}')
    print(f"📤 Writing dataframe to S3 at {s3_path}")
    print(f"📋 Registering as table {table_name} in Glue")

    df.write.mode("overwrite") \
        .option("path", s3_path) \
        .saveAsTable(table_name)
    
    print(f"✅ Successfully saved {table_name}")
    print(f"   Row count: {df.count():,}")

# COMMAND ----------

print("\n🔍 Step 10: Creating gc_checkout_success_20251121 (all customers, but parent relationships only from successful conversions)...")

# Refresh checkout_funnel_backend table
spark.sql("REFRESH TABLE payments_hf.checkout_funnel_backend")

# Load the FULL graph (all customers)
all_graph_customers_df = spark.table("payments_hf.graph_customers_20251121")

print(f"   Total customers in full graph: {all_graph_customers_df.count():,}")

# Load checkout_funnel_backend and filter for successful conversions
checkout_success_df = (
    spark.table("payments_hf.checkout_funnel_backend")
    .filter(
        (F.col("event_successful_conversion") == 1) | 
        (F.col("event_checkout_success") == 1)
    )
    .select("customer_id", "country")
    .distinct()
)

print(f"   Customers with successful conversions: {checkout_success_df.count():,}")

# Step 1: Get all customers with successful conversions (for parent relationship calculation)
# This is the subset we'll use to determine parents and duplicate flags
customers_with_success = (
    all_graph_customers_df.alias("gc")
    .join(
        checkout_success_df.alias("cs"),
        on=(
            (F.col("gc.business_unit") == F.col("cs.country")) &
            (F.col("gc.customer_id").cast("bigint") == F.col("cs.customer_id"))
        ),
        how="inner"
    )
    .select("gc.*")
)

print(f"   Customers in graph with successful conversions: {customers_with_success.count():,}")

# Step 2: Get all components that have at least one successful conversion
# This ensures we include all customers in components that have any successful conversions
successful_components = (
    customers_with_success
    .select("component")
    .distinct()
)

print(f"   Unique components with at least one successful conversion: {successful_components.count():,}")

# Step 3: Get ALL customers in these components (from the full graph)
# This is the final output - includes all customers, not just those with successful conversions
all_customers_in_success_components = (
    all_graph_customers_df.alias("gc_full")
    .join(
        successful_components.alias("sc"),
        on=F.col("gc_full.component") == F.col("sc.component"),
        how="inner"
    )
    .select("gc_full.*")
)

print(f"   All customers in components with successful conversions: {all_customers_in_success_components.count():,}")

# Step 4: Recalculate parent relationships - same as fraud_service_model_invoke_handler.py
# 1. Use the full graph (all customers) - already have this in all_customers_in_success_components
# 2. For each customer, find parents from the graph
# 3. Filter parents to only those with checkout_success == 'true' and same business_unit

# Create window functions for ordering (based on successful conversions only)
window_root_cluster = Window.partitionBy("component").orderBy("subscribed_at_local")
window_root_business_unit = Window.partitionBy("business_unit", "component").orderBy("subscribed_at_local")
window_cluster = Window.partitionBy("component")
window_business_unit_window = Window.partitionBy("business_unit", "component")

# Calculate window functions on successful conversions only (this is our "parents_with_checkout_success" filter)
customers_with_success_ranked = (
    customers_with_success
    .withColumn("nth_in_cluster_success", F.row_number().over(window_root_cluster))
    .withColumn("cluster_size_success", F.count("*").over(window_cluster))
    .withColumn("nth_in_business_unit_success", F.row_number().over(window_root_business_unit))
    .withColumn("business_unit_cluster_size_success", F.count("*").over(window_business_unit_window))
    .withColumn(
        "root_in_cluster_success",
        F.first(
            F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))
        ).over(window_cluster)
    )
    .withColumn(
        "root_in_business_unit_success",
        F.first(
            F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))
        ).over(window_business_unit_window)
    )
    .withColumn(
        "direct_parent_in_business_unit_success",
        F.when(
            F.col("nth_in_business_unit_success") > 1,
            F.lag(F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))).over(window_root_business_unit)
        ).otherwise(None)
    )
    .withColumn(
        "direct_parent_success",
        F.when(
            F.col("nth_in_cluster_success") > 1,
            F.lag(F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))).over(window_root_cluster)
        ).otherwise(None)
    )
)

# Step 5: For ALL customers, apply the same logic as fraud_service_model_invoke_handler.py
# Pattern: query graph -> filter parents_with_checkout_success (checkout_success == 'true' AND same business_unit)
# For each customer, find the most recent parent with successful conversion before them

# First, get calculated values for customers with successful conversions
# Drop the original parent columns since we'll recalculate them
all_customers_with_success_calc = (
    all_customers_in_success_components.alias("all")
    .join(
        customers_with_success_ranked.alias("success"),
        on=(
            (F.col("all.component") == F.col("success.component")) &
            (F.col("all.business_unit") == F.col("success.business_unit")) &
            (F.col("all.customer_id") == F.col("success.customer_id"))
        ),
        how="left"
    )
    .select(
        "all.business_unit",
        "all.customer_id",
        "all.component",
        "all.subscribed_at_local",
        "success.nth_in_cluster_success",
        "success.cluster_size_success",
        "success.nth_in_business_unit_success",
        "success.business_unit_cluster_size_success",
        "success.root_in_cluster_success",
        "success.root_in_business_unit_success",
        "success.direct_parent_in_business_unit_success",
        "success.direct_parent_success"
    )
)

# For each customer, find the most recent parent with successful conversion before them
# This mimics: parents_with_checkout_success = [i for i in all_parents if checkout_success == 'true' and same business_unit]
graph_customers_success_recalc = (
    all_customers_with_success_calc.alias("all")
    .join(
        customers_with_success_ranked.alias("success_parent"),
        on=(
            (F.col("all.component") == F.col("success_parent.component")) &
            (F.col("all.business_unit") == F.col("success_parent.business_unit")) &
            (F.col("all.subscribed_at_local") > F.col("success_parent.subscribed_at_local"))
        ),
        how="left"
    )
    .withColumn(
        "rank",
        F.row_number().over(
            Window.partitionBy("all.business_unit", "all.customer_id", "all.component")
            .orderBy(F.col("success_parent.subscribed_at_local").desc())
        )
    )
    .filter((F.col("rank") == 1) | (F.col("rank").isNull()))
    # Parent logic: if customer has successful conversion, use their calculated parent
    # Otherwise, use the most recent successful conversion customer before them (filtered by checkout_success == 'true')
    .withColumn(
        "direct_parent_in_business_unit",
        F.coalesce(
            F.col("all.direct_parent_in_business_unit_success"),
            F.when(
                F.col("success_parent.customer_id").isNotNull(),
                F.concat(F.col("success_parent.business_unit"), F.lit("_"), F.col("success_parent.customer_id"))
            ).otherwise(None)
        )
    )
    .withColumn(
        "direct_parent",
        F.coalesce(
            F.col("all.direct_parent_success"),
            F.when(
                F.col("success_parent.customer_id").isNotNull(),
                F.concat(F.col("success_parent.business_unit"), F.lit("_"), F.col("success_parent.customer_id"))
            ).otherwise(None)
        )
    )
    .withColumn(
        "nth_in_cluster",
        F.col("all.nth_in_cluster_success")
    )
    .withColumn(
        "cluster_size",
        F.coalesce(F.col("all.cluster_size_success"), F.lit(0))
    )
    .withColumn(
        "nth_in_business_unit",
        F.col("all.nth_in_business_unit_success")
    )
    .withColumn(
        "business_unit_cluster_size",
        F.coalesce(F.col("all.business_unit_cluster_size_success"), F.lit(0))
    )
    .withColumn(
        "root_in_cluster",
        F.coalesce(F.col("all.root_in_cluster_success"), F.concat(F.col("all.business_unit"), F.lit("_"), F.col("all.customer_id")))
    )
    .withColumn(
        "root_in_business_unit",
        F.coalesce(F.col("all.root_in_business_unit_success"), F.concat(F.col("all.business_unit"), F.lit("_"), F.col("all.customer_id")))
    )
    .withColumn(
        "has_direct_parent_in_business_unit",
        F.col("direct_parent_in_business_unit").isNotNull()
    )
    .withColumn(
        "has_direct_parent",
        F.col("direct_parent").isNotNull()
    )
    .withColumn(
        "is_root_in_business_unit",
        F.col("all.nth_in_business_unit_success") == 1
    )
    .withColumn(
        "is_root_in_cluster",
        F.col("all.nth_in_cluster_success") == 1
    )
    .withColumn(
        "is_duplicate_in_business_unit",
        (F.col("all.nth_in_business_unit_success") > 1) & (F.col("all.nth_in_business_unit_success").isNotNull())
    )
    .withColumn(
        "is_cross_business_unit_duplicate",
        (F.col("all.nth_in_business_unit_success") > 1) & 
        (F.col("all.nth_in_business_unit_success").isNotNull()) &
        (~F.col("has_direct_parent_in_business_unit"))
    )
    .withColumn(
        "is_duplicate_in_cluster",
        (F.col("all.nth_in_cluster_success") > 1) & (F.col("all.nth_in_cluster_success").isNotNull())
    )
    .select(
        "all.business_unit",
        "all.customer_id",
        "all.component",
        "all.subscribed_at_local",
        "direct_parent_in_business_unit",
        "direct_parent",
        "nth_in_cluster",
        "cluster_size",
        "nth_in_business_unit",
        "business_unit_cluster_size",
        "root_in_cluster",
        "root_in_business_unit",
        "has_direct_parent_in_business_unit",
        "has_direct_parent",
        "is_root_in_business_unit",
        "is_root_in_cluster",
        "is_duplicate_in_business_unit",
        "is_cross_business_unit_duplicate",
        "is_duplicate_in_cluster"
    )
    .orderBy("component", "subscribed_at_local")
)

print(f"   Recalculated graph customers (success only): {graph_customers_success_recalc.count():,}")

# Step 3: Create temp view from DataFrame for SQL processing
graph_customers_success_recalc.createOrReplaceTempView("graph_customers_success_recalc")

# Step 4: Recalculate match_reasons using SQL (same logic as original)
spark.sql(f"""
    CREATE OR REPLACE TEMP VIEW graph_customers_success_match_reasons_temp AS
    WITH i AS (
    SELECT 
        CONCAT(business_unit, '_', customer_id) AS business_unit_customer_id,
        ARRAY_AGG(STRUCT(identifier_source, dst)) AS identifiers
      FROM
        {output_table}
      WHERE
        count_connections > 1
      GROUP BY
        business_unit_customer_id
    ),
    d AS (
      SELECT
        g.*,
        CONCAT(g.business_unit, '_', g.customer_id) AS child_id,
        g.direct_parent_in_business_unit AS parent_id
      FROM
        graph_customers_success_recalc g
    )
    SELECT 
      d.*,
      array_sort(
        array_distinct(
          FILTER(
            TRANSFORM(
              ic.identifiers,
              ci -> CASE
                WHEN EXISTS(ip.identifiers, pi -> pi.dst = ci.dst) THEN ci.identifier_source
                ELSE NULL
              END
            ),
            x -> x IS NOT NULL
          )
        )
      ) AS match_reasons
    FROM
      d
        LEFT JOIN i ic
          ON d.direct_parent_in_business_unit IS NOT NULL
          AND d.child_id = ic.business_unit_customer_id
        LEFT JOIN i ip
          ON d.direct_parent_in_business_unit IS NOT NULL
          AND d.parent_id = ip.business_unit_customer_id
""")

# Save as final table
gc_checkout_success_df = spark.table("graph_customers_success_match_reasons_temp")
save(gc_checkout_success_df, "gc_checkout_success_20251121")

print(f"✅ Saved gc_checkout_success_20251121")
print(f"   Total customers in graph: {gc_checkout_success_df.count():,}")
print(f"   Note: All customers are included, but parent relationships are calculated based on successful conversions only")

# Write output to DBFS for visibility
output_lines = [
    "=" * 100,
    "GC CHECKOUT SUCCESS 20251121 - SUMMARY",
    "=" * 100,
    f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    "",
    f"Total customers in graph: {gc_checkout_success_df.count():,}",
    f"Note: All customers included, parent relationships based on successful conversions only",
    "",
    "=" * 100
]

output_path = f"/tmp/notebook_outputs/gc_checkout_success_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
dbutils.fs.put(output_path, "\n".join(output_lines), overwrite=True)
print(f"\n✅ Summary written to DBFS: {output_path}")

print("\n" + "=" * 80)
print("✅ STEP 10 COMPLETE!")
print("=" * 80)

