# Databricks notebook source
# MAGIC %md
# MAGIC # Debug: Exact Replication of bucket_by_percentage Issue
# MAGIC 
# MAGIC This notebook exactly replicates the data flow to identify why buckets are empty.

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# Exact data for HF-INTL BUs that should be in all_significant_bu_deep
# Based on SQL query results
all_significant_bu_deep = [
    {'business_unit': 'LU', 'relative_change_pct': 9.09, 'abs_rel_change': 9.09, 'volume_impacted': 5.55, 'prev_ratio': 0.917, 'current_ratio': 1.0, 'metric_type': 'ratio'},
    {'business_unit': 'CH', 'relative_change_pct': -6.03, 'abs_rel_change': 6.03, 'volume_impacted': 12.47, 'prev_ratio': 0.905, 'current_ratio': 0.850, 'metric_type': 'ratio'},
    {'business_unit': 'AT', 'relative_change_pct': -2.70, 'abs_rel_change': 2.70, 'volume_impacted': 18.78, 'prev_ratio': 0.949, 'current_ratio': 0.924, 'metric_type': 'ratio'},
    {'business_unit': 'NL', 'relative_change_pct': 2.69, 'abs_rel_change': 2.69, 'volume_impacted': 35.49, 'prev_ratio': 0.944, 'current_ratio': 0.969, 'metric_type': 'ratio'},
    {'business_unit': 'NZ', 'relative_change_pct': -2.53, 'abs_rel_change': 2.53, 'volume_impacted': 21.59, 'prev_ratio': 0.700, 'current_ratio': 0.683, 'metric_type': 'ratio'},
    {'business_unit': 'FR', 'relative_change_pct': -2.29, 'abs_rel_change': 2.29, 'volume_impacted': 245.89, 'prev_ratio': 0.943, 'current_ratio': 0.922, 'metric_type': 'ratio'},
    {'business_unit': 'GB', 'relative_change_pct': -2.21, 'abs_rel_change': 2.21, 'volume_impacted': 236.42, 'prev_ratio': 0.918, 'current_ratio': 0.897, 'metric_type': 'ratio'},
    {'business_unit': 'DE', 'relative_change_pct': -1.02, 'abs_rel_change': 1.02, 'volume_impacted': 96.48, 'prev_ratio': 0.940, 'current_ratio': 0.930, 'metric_type': 'ratio'},
]

print(f"all_significant_bu_deep count: {len(all_significant_bu_deep)}")
print(f"Type of first item: {type(all_significant_bu_deep[0])}")

# COMMAND ----------

# Create DataFrame exactly as the code does
bu_df_deep = pd.DataFrame(all_significant_bu_deep)
print(f"bu_df_deep shape: {bu_df_deep.shape}")
print(f"bu_df_deep columns: {list(bu_df_deep.columns)}")
print(f"bu_df_deep dtypes:\n{bu_df_deep.dtypes}")
print(f"\nbu_df_deep:\n{bu_df_deep}")

# COMMAND ----------

# Exact bucket_by_percentage function from the code
def bucket_by_percentage(items_df, item_type='business_unit', metric_full_name=None, comparison_type='week_prev'):
    # For LL0, min_threshold is 2.5
    min_threshold = 2.5
    
    buckets = {
        'high': [],
        'medium': [],
        'low': []
    }
    
    if items_df is None or items_df.empty:
        print("items_df is None or empty!")
        return buckets
    
    print(f"\nProcessing {len(items_df)} items with min_threshold={min_threshold}")
    
    for idx, row in items_df.iterrows():
        print(f"\n--- Row {idx}: {row['business_unit']} ---")
        print(f"  row type: {type(row)}")
        print(f"  row.index: {list(row.index)}")
        
        # Check 'in' behavior
        in_row_check = 'abs_rel_change' in row
        in_index_check = 'abs_rel_change' in row.index
        print(f"  'abs_rel_change' in row: {in_row_check}")
        print(f"  'abs_rel_change' in row.index: {in_index_check}")
        
        # Use abs_rel_change if available, otherwise calculate from relative_change_pct
        if 'abs_rel_change' in row and pd.notna(row['abs_rel_change']):
            abs_rel_change = row['abs_rel_change']
            print(f"  Using abs_rel_change directly: {abs_rel_change}")
        else:
            rel_change = row['relative_change_pct']
            abs_rel_change = abs(rel_change) if pd.notna(rel_change) else 0
            print(f"  Calculated abs_rel_change from relative_change_pct: {abs_rel_change}")
        
        # Check volume_impacted
        if 'volume_impacted' in row.index:
            volume_impacted = row['volume_impacted'] if pd.notna(row['volume_impacted']) else 0
        else:
            volume_impacted = 0
        print(f"  volume_impacted: {volume_impacted}")
        
        # Bucket logic
        print(f"  Checking: abs_rel_change >= 50: {abs_rel_change >= 50}")
        print(f"  Checking: abs_rel_change >= 20: {abs_rel_change >= 20}")
        print(f"  Checking: abs_rel_change >= {min_threshold}: {abs_rel_change >= min_threshold}")
        print(f"  Checking: volume_impacted > 30: {volume_impacted > 30}")
        
        if abs_rel_change >= 50:
            buckets['high'].append(row)
            print(f"  -> Added to HIGH bucket")
        elif abs_rel_change >= 20:
            buckets['medium'].append(row)
            print(f"  -> Added to MEDIUM bucket")
        elif abs_rel_change >= min_threshold or volume_impacted > 30:
            buckets['low'].append(row)
            print(f"  -> Added to LOW bucket")
        else:
            print(f"  -> NOT added to any bucket!")
    
    return buckets

# COMMAND ----------

# Run the function
bu_buckets_deep = bucket_by_percentage(bu_df_deep, 'business_unit', '3_Active - 1_2_Loyalty: LL0 (Initial charges) - 2_PreDunningAR', 'week_prev')

print(f"\n" + "="*60)
print("FINAL BUCKET COUNTS:")
print(f"  HIGH: {len(bu_buckets_deep.get('high', []))}")
print(f"  MEDIUM: {len(bu_buckets_deep.get('medium', []))}")
print(f"  LOW: {len(bu_buckets_deep.get('low', []))}")
print("="*60)

# COMMAND ----------

# Save results to table
results = []
for bucket_name, items in bu_buckets_deep.items():
    for item in items:
        results.append({
            'bucket': bucket_name,
            'business_unit': item['business_unit'],
            'abs_rel_change': float(item['abs_rel_change']),
            'volume_impacted': float(item['volume_impacted']),
        })

if results:
    results_df = spark.createDataFrame(results)
    results_df.write.mode("overwrite").saveAsTable("hive_metastore.visal_debug.bucket_exact_test")
    print(f"\nSaved {len(results)} items to hive_metastore.visal_debug.bucket_exact_test")
else:
    print("\nNo items in any bucket - nothing to save!")
    # Save empty result to indicate test ran
    empty_df = spark.createDataFrame([{'bucket': 'EMPTY', 'business_unit': 'NONE', 'abs_rel_change': 0.0, 'volume_impacted': 0.0}])
    empty_df.write.mode("overwrite").saveAsTable("hive_metastore.visal_debug.bucket_exact_test")
