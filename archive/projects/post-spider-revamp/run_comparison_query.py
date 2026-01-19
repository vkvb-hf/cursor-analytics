#!/usr/bin/env python3
"""
Run comparison query for 2025-W46 comparing old and new graph_customers_with_match_reasons tables
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from databricks_api import DatabricksAPI
from datetime import datetime

def run_comparison_query():
    db = DatabricksAPI()
    
    notebook_content = f"""
# Databricks notebook source
from pyspark.sql import functions as F

print("=" * 100)
print("COMPARISON QUERY: 2025-W46 - Old vs New graph_customers_with_match_reasons")
print("=" * 100)

# Refresh tables
spark.sql("REFRESH TABLE payments_hf_staging.spider_last_attempts")
spark.sql("REFRESH TABLE dimensions.date_dimension")
spark.sql("REFRESH TABLE payments_hf.graph_customers_with_match_reasons")
spark.sql("REFRESH TABLE payments_hf.graph_customers_with_match_reasons_20251121")
spark.sql("REFRESH TABLE payments_hf.checkout_customer_details_bob")

# Query with OLD table
print("\\n📊 Running query with OLD table (payments_hf.graph_customers_with_match_reasons)...")
query_old = '''
select
  case when d.account_email like '%gdpr%' then 1 else 0 end as gdpr,
  struct(d.*) AS bob_data,
  a.*
from (
  select 
    get_json_object(raw_payload, '$.parent_ids_with_checkout_success') as parent_ids_with_checkout_success,
    ARRAY_DISTINCT(
      FLATTEN(
        TRANSFORM(
          FROM_JSON(
            raw_payload,
            'struct<parent_ids_with_checkout_success:array<struct<matching_attributes:array<struct<attribute_name:string>>>>>'
          ).parent_ids_with_checkout_success,
          x -> TRANSFORM(x.matching_attributes, y -> y.attribute_name)
        )
      )
    ) AS matching_attributes,
    transform(
      from_json(
        get_json_object(raw_payload, '$.parent_ids_with_checkout_success'),
        'array<struct<id:string>>'
      ),
      x -> regexp_extract(x.id, 'customer:[A-Z]+_(.*)', 1)
    ) as parent_ids_list,
    a.*
  FROM
    payments_hf_staging.spider_last_attempts AS a
    LEFT JOIN dimensions.date_dimension dd
      ON date(a.event_timestamp_utc) = DATE(dd.date_string_backwards)
    left join payments_hf.graph_customers_with_match_reasons cc
      on a.customer_id = cc.customer_id and a.business_unit = cc.business_unit
  WHERE
    1=1
    and a.business_unit = 'NL'
    and dd.iso_year_week = '2025-W46'
    and not(cc.is_duplicate_in_business_unit)
    and a.is_duplicate
  group by all
) a
  left JOIN payments_hf.checkout_customer_details_bob d
    ON element_at(a.parent_ids_list, 1) = d.customer_uuid
where array_size(parent_ids_list)=1
order by 2,3
'''

result_old = spark.sql(query_old)
count_old = result_old.count()
print(f"✅ OLD table results: {{count_old:,}} records")

# Query with NEW table
print("\\n📊 Running query with NEW table (payments_hf.graph_customers_with_match_reasons_20251121)...")
query_new = '''
select
  case when d.account_email like '%gdpr%' then 1 else 0 end as gdpr,
  struct(d.*) AS bob_data,
  a.*
from (
  select 
    get_json_object(raw_payload, '$.parent_ids_with_checkout_success') as parent_ids_with_checkout_success,
    ARRAY_DISTINCT(
      FLATTEN(
        TRANSFORM(
          FROM_JSON(
            raw_payload,
            'struct<parent_ids_with_checkout_success:array<struct<matching_attributes:array<struct<attribute_name:string>>>>>'
          ).parent_ids_with_checkout_success,
          x -> TRANSFORM(x.matching_attributes, y -> y.attribute_name)
        )
      )
    ) AS matching_attributes,
    transform(
      from_json(
        get_json_object(raw_payload, '$.parent_ids_with_checkout_success'),
        'array<struct<id:string>>'
      ),
      x -> regexp_extract(x.id, 'customer:[A-Z]+_(.*)', 1)
    ) as parent_ids_list,
    a.*
  FROM
    payments_hf_staging.spider_last_attempts AS a
    LEFT JOIN dimensions.date_dimension dd
      ON date(a.event_timestamp_utc) = DATE(dd.date_string_backwards)
    left join payments_hf.graph_customers_with_match_reasons_20251121 cc
      on a.customer_id = cc.customer_id and a.business_unit = cc.business_unit
  WHERE
    1=1
    and a.business_unit = 'NL'
    and dd.iso_year_week = '2025-W46'
    and not(cc.is_duplicate_in_business_unit)
    and a.is_duplicate
  group by all
) a
  left JOIN payments_hf.checkout_customer_details_bob d
    ON element_at(a.parent_ids_list, 1) = d.customer_uuid
where array_size(parent_ids_list)=1
order by 2,3
'''

result_new = spark.sql(query_new)
count_new = result_new.count()
print(f"✅ NEW table results: {{count_new:,}} records")

# Comparison
print("\\n" + "=" * 100)
print("📊 COMPARISON RESULTS")
print("=" * 100)
print(f"\\nOLD table: {{count_old:,}} records")
print(f"NEW table: {{count_new:,}} records")
print(f"Difference: {{count_new - count_old:,}} records")
if count_old > 0:
    print(f"Percentage change: {{(count_new - count_old)/count_old*100:.2f}}%")

# Show sample from old (just count and basic info)
print("\\n📊 Sample from OLD table (first 5 records - basic columns only):")
try:
    result_old.select("gdpr", "business_unit", "customer_id", "is_duplicate").limit(5).show(truncate=False)
except:
    print("   (Could not display sample - ambiguous columns)")

# Show sample from new (just count and basic info)
print("\\n📊 Sample from NEW table (first 5 records - basic columns only):")
try:
    result_new.select("gdpr", "business_unit", "customer_id", "is_duplicate").limit(5).show(truncate=False)
except:
    print("   (Could not display sample - ambiguous columns)")

# Write summary to DBFS
output_lines = [
    "=" * 100,
    "COMPARISON QUERY RESULTS - 2025-W46",
    "=" * 100,
    f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    "",
    "Business Unit: NL",
    "Week: 2025-W46",
    "",
    "Results:",
    f"  OLD table: {{count_old:,}} records",
    f"  NEW table: {{count_new:,}} records",
    f"  Difference: {{count_new - count_old:,}} records",
]
# Add percentage change if count_old > 0
pct_change_line = ""
if count_old > 0:
    pct_change = (count_new - count_old) / count_old * 100
    pct_change_line = f"  Percentage change: {{pct_change:.2f}}%"
    output_lines.append(pct_change_line)

output_lines.append("")
output_lines.append("=" * 100)

output_path = f"/tmp/notebook_outputs/comparison_query_w46_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
dbutils.fs.mkdirs("/tmp/notebook_outputs")
dbutils.fs.put(output_path, "\\n".join(output_lines), overwrite=True)
print(f"\\n✅ Summary written to: {{output_path}}")
"""
    
    job_name = f"comparison_query_w46_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/_temp_comparison_query_w46"
    
    result = db.run_notebook_job(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        auto_inject_output=True,
        auto_read_output=True
    )
    
    return result

if __name__ == "__main__":
    run_comparison_query()

