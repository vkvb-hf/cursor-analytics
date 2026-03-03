# Databricks notebook source
# MAGIC %md
# MAGIC # Debug: Test bucket_by_percentage Bug
# MAGIC 
# MAGIC This notebook tests the suspected bug in `bucket_by_percentage` function.
# MAGIC 
# MAGIC **Suspected Bug**: In pandas, `'key' in series` checks VALUES, not INDEX.
# MAGIC So `'abs_rel_change' in row` is always False.

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC ## Test 1: Verify the 'in' behavior bug

# COMMAND ----------

# Create test data simulating LL0 significant BUs
test_data = [
    {'business_unit': 'AT', 'relative_change_pct': -2.70, 'abs_rel_change': 2.70, 'volume_impacted': 18.78},
    {'business_unit': 'CH', 'relative_change_pct': -6.03, 'abs_rel_change': 6.03, 'volume_impacted': 12.47},
    {'business_unit': 'FR', 'relative_change_pct': -2.29, 'abs_rel_change': 2.29, 'volume_impacted': 245.89},
    {'business_unit': 'NL', 'relative_change_pct': 2.69, 'abs_rel_change': 2.69, 'volume_impacted': 35.49},
]

df = pd.DataFrame(test_data)
min_threshold = 2.5

# COMMAND ----------

# Test the 'in' behavior and bucket assignment
results = []

for idx, row in df.iterrows():
    # Check 'in' behavior - THIS IS THE BUG
    in_row_buggy = 'abs_rel_change' in row  # Checks VALUES (wrong!)
    in_row_correct = 'abs_rel_change' in row.index  # Checks INDEX (correct!)
    
    # Simulate BUGGY logic (current code)
    if 'abs_rel_change' in row and pd.notna(row['abs_rel_change']):
        abs_rel_change_buggy = row['abs_rel_change']
        source_buggy = 'direct'
    else:
        rel_change = row['relative_change_pct']
        abs_rel_change_buggy = abs(rel_change) if pd.notna(rel_change) else 0
        source_buggy = 'calculated'
    
    # Simulate FIXED logic
    if 'abs_rel_change' in row.index and pd.notna(row['abs_rel_change']):
        abs_rel_change_fixed = row['abs_rel_change']
        source_fixed = 'direct'
    else:
        rel_change = row['relative_change_pct']
        abs_rel_change_fixed = abs(rel_change) if pd.notna(rel_change) else 0
        source_fixed = 'calculated'
    
    # Determine bucket with BUGGY logic
    if abs_rel_change_buggy >= 50:
        bucket_buggy = 'high'
    elif abs_rel_change_buggy >= 20:
        bucket_buggy = 'medium'
    elif abs_rel_change_buggy >= min_threshold or row['volume_impacted'] > 30:
        bucket_buggy = 'low'
    else:
        bucket_buggy = 'none'
    
    # Determine bucket with FIXED logic
    if abs_rel_change_fixed >= 50:
        bucket_fixed = 'high'
    elif abs_rel_change_fixed >= 20:
        bucket_fixed = 'medium'
    elif abs_rel_change_fixed >= min_threshold or row['volume_impacted'] > 30:
        bucket_fixed = 'low'
    else:
        bucket_fixed = 'none'
    
    results.append({
        'business_unit': row['business_unit'],
        'abs_rel_change_original': float(row['abs_rel_change']),
        'volume_impacted': float(row['volume_impacted']),
        'in_row_buggy': str(in_row_buggy),
        'in_row_correct': str(in_row_correct),
        'abs_rel_change_buggy': float(abs_rel_change_buggy),
        'source_buggy': source_buggy,
        'bucket_buggy': bucket_buggy,
        'abs_rel_change_fixed': float(abs_rel_change_fixed),
        'source_fixed': source_fixed,
        'bucket_fixed': bucket_fixed,
    })

# COMMAND ----------

# Save results to table
results_df = spark.createDataFrame(results)
results_df.write.mode("overwrite").saveAsTable("hive_metastore.visal_debug.bucket_bug_test")

# COMMAND ----------

# Display results
display(results_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC 
# MAGIC Check the `bucket_bug_test` table:
# MAGIC - `in_row_buggy` should be `False` for all rows (the bug)
# MAGIC - `in_row_correct` should be `True` for all rows (the fix)
# MAGIC - `source_buggy` shows whether the buggy code used direct or calculated value
# MAGIC - `bucket_buggy` vs `bucket_fixed` shows if the bug affects bucket assignment

# COMMAND ----------

# Query the results
spark.sql("SELECT * FROM hive_metastore.visal_debug.bucket_bug_test").show(truncate=False)
