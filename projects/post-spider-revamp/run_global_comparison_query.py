#!/usr/bin/env python3
"""
Run comparison query for global data and latest weeks comparing old and new graph_customers_with_match_reasons tables
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from databricks_api import DatabricksAPI
from datetime import datetime

def run_global_comparison():
    db = DatabricksAPI()
    
    notebook_content = f"""
# Databricks notebook source
from pyspark.sql import functions as F

print("=" * 100)
print("GLOBAL COMPARISON: Old vs New graph_customers_with_match_reasons")
print("=" * 100)

# Refresh tables
spark.sql("REFRESH TABLE payments_hf_staging.spider_last_attempts")
spark.sql("REFRESH TABLE dimensions.date_dimension")
spark.sql("REFRESH TABLE payments_hf.graph_customers_with_match_reasons")
spark.sql("REFRESH TABLE payments_hf.graph_customers_with_match_reasons_20251121")

# Get latest weeks (last 10 weeks)
latest_weeks_df = spark.sql('''
    SELECT DISTINCT iso_year_week
    FROM dimensions.date_dimension
    WHERE iso_year_week IS NOT NULL
    ORDER BY iso_year_week DESC
    LIMIT 10
''')

latest_week_list = [row['iso_year_week'] for row in latest_weeks_df.collect()]
week_list_str = ','.join([f"{{repr(w)}}" for w in latest_week_list])
print(f"\\n📅 Latest weeks to analyze: {{latest_week_list}}")
print(f"\\n📅 Week list string for SQL: {{week_list_str}}")

# Check if there's any data in spider_last_attempts for these weeks
print("\\n📊 Checking data availability...")
data_check = spark.sql(f'''
    SELECT 
        dd.iso_year_week,
        COUNT(*) as attempt_count
    FROM payments_hf_staging.spider_last_attempts AS a
    LEFT JOIN dimensions.date_dimension dd
        ON date(a.event_timestamp_utc) = DATE(dd.date_string_backwards)
    WHERE dd.iso_year_week IN ({{week_list_str}})
    GROUP BY dd.iso_year_week
    ORDER BY dd.iso_year_week DESC
''')
print("\\nData availability by week:")
data_check.show(100, truncate=False)

# Query with OLD table - Global
print("\\n📊 Running GLOBAL query with OLD table...")
query_old_global = f'''
select 
  dd.iso_year_week,
  COALESCE(a.is_duplicate, FALSE) as pre_checkout_spider,
  cc.is_duplicate_in_business_unit as post_checkout_spider,
  count(*) as count
FROM
  payments_hf_staging.spider_last_attempts AS a
  LEFT JOIN dimensions.date_dimension dd
    ON date(a.event_timestamp_utc) = DATE(dd.date_string_backwards)
  left join payments_hf.graph_customers_with_match_reasons cc
    on a.customer_id = cc.customer_id and a.business_unit = cc.business_unit
WHERE
  1=1
  and dd.iso_year_week IN ({{week_list_str}})
group by all
order by 1,2,3
'''

result_old_global = spark.sql(query_old_global)
print(f"✅ OLD table global results: {{result_old_global.count():,}} records")

# Query with NEW table - Global
print("\\n📊 Running GLOBAL query with NEW table...")
query_new_global = f'''
select 
  dd.iso_year_week,
  COALESCE(a.is_duplicate, FALSE) as pre_checkout_spider,
  cc.is_duplicate_in_business_unit as post_checkout_spider,
  count(*) as count
FROM
  payments_hf_staging.spider_last_attempts AS a
  LEFT JOIN dimensions.date_dimension dd
    ON date(a.event_timestamp_utc) = DATE(dd.date_string_backwards)
  left join payments_hf.graph_customers_with_match_reasons_20251121 cc
    on a.customer_id = cc.customer_id and a.business_unit = cc.business_unit
WHERE
  1=1
  and dd.iso_year_week IN ({{week_list_str}})
group by all
order by 1,2,3
'''

result_new_global = spark.sql(query_new_global)
print(f"✅ NEW table global results: {{result_new_global.count():,}} records")

# Show results
print("\\n" + "=" * 100)
print("📊 GLOBAL RESULTS - OLD TABLE")
print("=" * 100)
result_old_global.show(100, truncate=False)

print("\\n" + "=" * 100)
print("📊 GLOBAL RESULTS - NEW TABLE")
print("=" * 100)
result_new_global.show(100, truncate=False)

# Create comparison by joining on key columns
print("\\n" + "=" * 100)
print("📊 COMPARISON - Side by Side")
print("=" * 100)

comparison = (
    result_old_global.alias("old")
    .join(
        result_new_global.alias("new"),
        on=[
            F.col("old.iso_year_week") == F.col("new.iso_year_week"),
            F.col("old.pre_checkout_spider") == F.col("new.pre_checkout_spider"),
            F.col("old.post_checkout_spider") == F.col("new.post_checkout_spider")
        ],
        how="full_outer"
    )
    .select(
        F.coalesce(F.col("old.iso_year_week"), F.col("new.iso_year_week")).alias("iso_year_week"),
        F.coalesce(F.col("old.pre_checkout_spider"), F.col("new.pre_checkout_spider")).alias("pre_checkout_spider"),
        F.coalesce(F.col("old.post_checkout_spider"), F.col("new.post_checkout_spider")).alias("post_checkout_spider"),
        F.coalesce(F.col("old.count"), F.lit(0)).alias("old_count"),
        F.coalesce(F.col("new.count"), F.lit(0)).alias("new_count"),
        (F.coalesce(F.col("new.count"), F.lit(0)) - F.coalesce(F.col("old.count"), F.lit(0))).alias("difference"),
        F.when(
            F.coalesce(F.col("old.count"), F.lit(0)) > 0,
            ((F.coalesce(F.col("new.count"), F.lit(0)) - F.coalesce(F.col("old.count"), F.lit(0))) / F.col("old.count") * 100)
        ).otherwise(F.lit(None)).alias("pct_change")
    )
    .orderBy("iso_year_week", "pre_checkout_spider", "post_checkout_spider")
)

comparison.show(100, truncate=False)

# Summary statistics
print("\\n" + "=" * 100)
print("📊 SUMMARY STATISTICS")
print("=" * 100)

total_old = result_old_global.agg(F.sum("count")).collect()[0][0] or 0
total_new = result_new_global.agg(F.sum("count")).collect()[0][0] or 0

print(f"\\nTotal records:")
print(f"  OLD table: {{total_old:,}}")
print(f"  NEW table: {{total_new:,}}")
print(f"  Difference: {{total_new - total_old:,}}")
if total_old > 0:
    print(f"  Percentage change: {{(total_new - total_old)/total_old*100:.2f}}%")

# Breakdown by duplicate status
print("\\n📊 Breakdown by duplicate status (OLD table):")
result_old_global.groupBy("pre_checkout_spider", "post_checkout_spider").agg(
    F.sum("count").alias("total_count")
).orderBy("pre_checkout_spider", "post_checkout_spider").show(truncate=False)

print("\\n📊 Breakdown by duplicate status (NEW table):")
result_new_global.groupBy("pre_checkout_spider", "post_checkout_spider").agg(
    F.sum("count").alias("total_count")
).orderBy("pre_checkout_spider", "post_checkout_spider").show(truncate=False)

# Write summary to DBFS
output_lines = [
    "=" * 100,
    "GLOBAL COMPARISON QUERY RESULTS",
    "=" * 100,
    f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    "",
    "Weeks analyzed: Latest 10 weeks",
    "",
    "Total records:",
    f"  OLD table: {{total_old:,}}",
    f"  NEW table: {{total_new:,}}",
    f"  Difference: {{total_new - total_old:,}}",
]
# Add percentage change if total_old > 0
if total_old > 0:
    pct = (total_new - total_old) / total_old * 100
    output_lines.append(f"  Percentage change: {{pct:.2f}}%")

output_lines.append("")
output_lines.append("=" * 100)

output_path = f"/tmp/notebook_outputs/global_comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
dbutils.fs.mkdirs("/tmp/notebook_outputs")
dbutils.fs.put(output_path, "\\n".join(output_lines), overwrite=True)
print(f"\\n✅ Summary written to: {{output_path}}")
"""
    
    job_name = f"global_comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/_temp_global_comparison"
    
    result = db.run_notebook_job(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        auto_inject_output=True,
        auto_read_output=True
    )
    
    return result

if __name__ == "__main__":
    run_global_comparison()

