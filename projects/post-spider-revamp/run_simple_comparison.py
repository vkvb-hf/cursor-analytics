#!/usr/bin/env python3
"""
Run simple comparison query for specific weeks
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from databricks_api import DatabricksAPI
from datetime import datetime

def run_simple_comparison():
    db = DatabricksAPI()
    
    # Test with specific weeks that we know have data
    test_weeks = ["2025-W46", "2025-W45", "2025-W44", "2025-W43", "2025-W42", "2025-W41"]
    week_list_str = ','.join([f"'{w}'" for w in test_weeks])
    
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

# Query with OLD table
print("\\n📊 Running query with OLD table...")
query_old = '''
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
  and dd.iso_year_week IN ({week_list_str})
group by all
order by 1,2,3
'''

result_old = spark.sql(query_old)
count_old = result_old.count()
print(f"✅ OLD table results: {{count_old:,}} records")

# Query with NEW table
print("\\n📊 Running query with NEW table...")
query_new = '''
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
  and dd.iso_year_week IN ({week_list_str})
group by all
order by 1,2,3
'''

result_new = spark.sql(query_new)
count_new = result_new.count()
print(f"✅ NEW table results: {{count_new:,}} records")

# Show results
print("\\n" + "=" * 100)
print("📊 RESULTS - OLD TABLE")
print("=" * 100)
result_old.show(100, truncate=False)

print("\\n" + "=" * 100)
print("📊 RESULTS - NEW TABLE")
print("=" * 100)
result_new.show(100, truncate=False)

# Summary
print("\\n" + "=" * 100)
print("📊 SUMMARY")
print("=" * 100)
print(f"\\nOLD table: {{count_old:,}} records")
print(f"NEW table: {{count_new:,}} records")
print(f"Difference: {{count_new - count_old:,}} records")

# Write summary to DBFS
output_lines = [
    "=" * 100,
    "GLOBAL COMPARISON QUERY RESULTS",
    "=" * 100,
    f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    "",
    f"Weeks analyzed: {', '.join(test_weeks)}",
    "",
    f"Total records:",
    f"  OLD table: {{count_old:,}}",
    f"  NEW table: {{count_new:,}}",
    f"  Difference: {{count_new - count_old:,}}",
    "",
    "=" * 100
]

output_path = f"/tmp/notebook_outputs/simple_comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
dbutils.fs.mkdirs("/tmp/notebook_outputs")
dbutils.fs.put(output_path, "\\n".join(output_lines), overwrite=True)
print(f"\\n✅ Summary written to: {{output_path}}")
"""
    
    job_name = f"simple_comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/_temp_simple_comparison"
    
    result = db.run_notebook_job(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        auto_inject_output=True,
        auto_read_output=True
    )
    
    return result

if __name__ == "__main__":
    run_simple_comparison()






