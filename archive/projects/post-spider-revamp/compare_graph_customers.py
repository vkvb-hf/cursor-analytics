#!/usr/bin/env python3
"""
Compare payments_hf.graph_customers_with_match_reasons_20251121 
with payments_hf.graph_customers_with_match_reasons
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from databricks_api import DatabricksAPI
from datetime import datetime

def compare_tables():
    db = DatabricksAPI()
    
    notebook_content = f"""
# Databricks notebook source
from pyspark.sql import functions as F

print("=" * 100)
print("COMPARISON: graph_customers_with_match_reasons vs graph_customers_with_match_reasons_20251121")
print("=" * 100)

# Refresh tables
spark.sql("REFRESH TABLE payments_hf.graph_customers_with_match_reasons")
spark.sql("REFRESH TABLE payments_hf.graph_customers_with_match_reasons_20251121")

# Load both tables
old_table = spark.table("payments_hf.graph_customers_with_match_reasons")
new_table = spark.table("payments_hf.graph_customers_with_match_reasons_20251121")

print("\\n📊 BASIC STATISTICS")
print("=" * 100)

# Total customers
old_count = old_table.count()
new_count = new_table.count()
print(f"\\nTotal customers:")
print(f"  Old table: {{old_count:,}}")
print(f"  New table: {{new_count:,}}")
print(f"  Difference: {{new_count - old_count:,}} ({{(new_count - old_count)/old_count*100:.2f}}%)")

# Duplicate counts
old_duplicates = old_table.filter(F.col("is_duplicate_in_business_unit")).count()
new_duplicates = new_table.filter(F.col("is_duplicate_in_business_unit")).count()
print(f"\\nDuplicates in business unit:")
print(f"  Old table: {{old_duplicates:,}}")
print(f"  New table: {{new_duplicates:,}}")
print(f"  Difference: {{new_duplicates - old_duplicates:,}} ({{(new_duplicates - old_duplicates)/old_duplicates*100:.2f}}%)")

old_duplicates_cluster = old_table.filter(F.col("is_duplicate_in_cluster")).count()
new_duplicates_cluster = new_table.filter(F.col("is_duplicate_in_cluster")).count()
print(f"\\nDuplicates in cluster:")
print(f"  Old table: {{old_duplicates_cluster:,}}")
print(f"  New table: {{new_duplicates_cluster:,}}")
print(f"  Difference: {{new_duplicates_cluster - old_duplicates_cluster:,}} ({{(new_duplicates_cluster - old_duplicates_cluster)/old_duplicates_cluster*100:.2f}}%)")

old_cross_bu = old_table.filter(F.col("is_cross_business_unit_duplicate")).count()
new_cross_bu = new_table.filter(F.col("is_cross_business_unit_duplicate")).count()
print(f"\\nCross-business-unit duplicates:")
print(f"  Old table: {{old_cross_bu:,}}")
print(f"  New table: {{new_cross_bu:,}}")
print(f"  Difference: {{new_cross_bu - old_cross_bu:,}} ({{(new_cross_bu - old_cross_bu)/old_cross_bu*100:.2f}}%)")

# Cluster sizes
print(f"\\n📊 CLUSTER SIZE DISTRIBUTION")
print("=" * 100)
old_cluster_sizes = old_table.groupBy("cluster_size").agg(F.count("*").alias("count")).orderBy("cluster_size")
new_cluster_sizes = new_table.groupBy("cluster_size").agg(F.count("*").alias("count")).orderBy("cluster_size")

print("\\nOld table cluster sizes (top 10):")
old_cluster_sizes.show(10, truncate=False)

print("\\nNew table cluster sizes (top 10):")
new_cluster_sizes.show(10, truncate=False)

# Business unit breakdown
print(f"\\n📊 DUPLICATES BY BUSINESS UNIT")
print("=" * 100)
old_bu_dups = old_table.filter(F.col("is_duplicate_in_business_unit")).groupBy("business_unit").agg(F.count("*").alias("count")).orderBy(F.desc("count"))
new_bu_dups = new_table.filter(F.col("is_duplicate_in_business_unit")).groupBy("business_unit").agg(F.count("*").alias("count")).orderBy(F.desc("count"))

print("\\nOld table duplicates by BU (top 10):")
old_bu_dups.show(10, truncate=False)

print("\\nNew table duplicates by BU (top 10):")
new_bu_dups.show(10, truncate=False)

# Sample comparison
print(f"\\n📊 SAMPLE RECORDS")
print("=" * 100)
print("\\nSample from old table (duplicates):")
old_table.filter(F.col("is_duplicate_in_business_unit")).select(
    "business_unit", "customer_id", "is_duplicate_in_business_unit", 
    "direct_parent_in_business_unit", "match_reasons"
).limit(5).show(truncate=False)

print("\\nSample from new table (duplicates):")
new_table.filter(F.col("is_duplicate_in_business_unit")).select(
    "business_unit", "customer_id", "is_duplicate_in_business_unit", 
    "direct_parent_in_business_unit", "match_reasons"
).limit(5).show(truncate=False)

# Write summary to DBFS
output_lines = [
    "=" * 100,
    "COMPARISON SUMMARY",
    "=" * 100,
    f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    "",
    "Total customers:",
    f"  Old: {{old_count:,}}",
    f"  New: {{new_count:,}}",
    f"  Difference: {{new_count - old_count:,}}",
    "",
    "Duplicates in business unit:",
    f"  Old: {{old_duplicates:,}}",
    f"  New: {{new_duplicates:,}}",
    f"  Difference: {{new_duplicates - old_duplicates:,}}",
    "",
    "Duplicates in cluster:",
    f"  Old: {{old_duplicates_cluster:,}}",
    f"  New: {{new_duplicates_cluster:,}}",
    f"  Difference: {{new_duplicates_cluster - old_duplicates_cluster:,}}",
    "",
    "=" * 100
]

output_path = f"/tmp/notebook_outputs/compare_graph_customers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
dbutils.fs.mkdirs("/tmp/notebook_outputs")
dbutils.fs.put(output_path, "\\n".join(output_lines), overwrite=True)
print(f"\\n✅ Summary written to: {{output_path}}")
"""
    
    job_name = f"compare_graph_customers_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/_temp_compare_graph_customers"
    
    result = db.run_notebook_job(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        auto_inject_output=True,
        auto_read_output=True
    )
    
    return result

if __name__ == "__main__":
    compare_tables()

