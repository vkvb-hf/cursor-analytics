# Databricks notebook source
# MAGIC %md
# MAGIC # Check what "Unknown" dimension_value represents in payments_p0_metrics

# COMMAND ----------

from databricks_api import DatabricksAPI

# COMMAND ----------

# Query to see what "Unknown" represents for PaymentProvider dimension
query = """
SELECT DISTINCT
    dimension_name,
    dimension_value,
    COUNT(*) as row_count,
    MIN(date_value) as earliest_date,
    MAX(date_value) as latest_date
FROM payments_hf.payments_p0_metrics
WHERE dimension_name = 'PaymentProvider'
  AND dimension_value = 'Unknown'
  AND date_granularity = 'WEEK'
  AND flag_is_p0 = 'TRUE'
GROUP BY dimension_name, dimension_value
ORDER BY row_count DESC
LIMIT 100
"""

# COMMAND ----------

# Also check all PaymentProvider dimension values to see what else exists
query_all_pp = """
SELECT DISTINCT
    dimension_name,
    dimension_value,
    COUNT(*) as row_count
FROM payments_hf.payments_p0_metrics
WHERE dimension_name = 'PaymentProvider'
  AND date_granularity = 'WEEK'
  AND flag_is_p0 = 'TRUE'
GROUP BY dimension_name, dimension_value
ORDER BY row_count DESC
LIMIT 50
"""

# COMMAND ----------

# Check for AR Pre Dunning metric specifically with PaymentProvider Unknown
query_ar_predunning_unknown = """
SELECT 
    metric_name,
    dimension_name,
    dimension_value,
    reporting_cluster,
    date_value,
    current_metric_value_numerator,
    current_metric_value_denominator,
    CASE 
        WHEN current_metric_value_denominator > 0 
        THEN current_metric_value_numerator / current_metric_value_denominator * 100
        ELSE 0 
    END as metric_percentage
FROM payments_hf.payments_p0_metrics
WHERE metric_name = '2_PreDunningAR'
  AND dimension_name = 'PaymentProvider'
  AND dimension_value = 'Unknown'
  AND date_granularity = 'WEEK'
  AND flag_is_p0 = 'TRUE'
  AND date_value >= '2025-W33'
ORDER BY date_value DESC, reporting_cluster
LIMIT 20
"""

print("Query 1: Check Unknown PaymentProvider values")
print("=" * 80)
print(query)
print("\n")

print("Query 2: Check all PaymentProvider dimension values")
print("=" * 80)
print(query_all_pp)
print("\n")

print("Query 3: Check AR Pre Dunning with PaymentProvider Unknown")
print("=" * 80)
print(query_ar_predunning_unknown)

