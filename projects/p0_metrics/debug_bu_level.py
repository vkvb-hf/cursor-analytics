#!/usr/bin/env python3
"""
Debug: Check if bu_level rows exist in the processed data
"""

import sys
import os
from pathlib import Path

# Add cursor_databricks directory to path for imports
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)
from databricks import sql
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN
import pandas as pd

def execute_query(query_str):
    """Execute a SQL query and return results as a list of dictionaries."""
    with sql.connect(
        server_hostname=SERVER_HOSTNAME,
        http_path=HTTP_PATH,
        access_token=TOKEN
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query_str)
            result = cursor.fetchall()
            
            # Convert to list of dictionaries
            if result:
                columns = [desc[0] for desc in cursor.description]
                return pd.DataFrame([dict(zip(columns, row)) for row in result])
            return pd.DataFrame()

print("="*80)
print("Debug: Checking if bu_level rows exist in the query results")
print("="*80)

# Simulate what the notebook query would return for month_prev
month_current_weeks = ['2025-W41', '2025-W42', '2025-W43', '2025-W44']
month_prev_weeks = ['2025-W37', '2025-W38', '2025-W39', '2025-W40']

month_current_str = ','.join([f"'{w}'" for w in month_current_weeks])
month_prev_str = ','.join([f"'{w}'" for w in month_prev_weeks])

test_metric = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'

# Query that simulates the notebook's UNION ALL for bu_level
bu_level_query = f"""
    SELECT 
        'bu_level' AS reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        dimension_name,
        dimension_value,
        SUM(current_metric_value_numerator) AS current_metric_value_numerator,
        SUM(current_metric_value_denominator) AS current_metric_value_denominator
    FROM payments_hf.payments_p0_metrics
    WHERE date_value IN ({month_current_str})
      AND date_granularity = 'WEEK'
      AND reporting_cluster = 'Overall'
      AND business_unit IS NOT NULL
      AND business_unit != 'Null'
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{test_metric}'
      AND dimension_name = '_Overall'
    GROUP BY business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
        dimension_name,
        dimension_value
"""

bu_level_current = execute_query(bu_level_query)
print(f"\n📊 bu_level rows in current period: {len(bu_level_current)}")
if not bu_level_current.empty:
    print(f"   Sample: {bu_level_current.head(5).to_string()}")

# Query previous period
bu_level_prev_query = f"""
    SELECT 
        'bu_level' AS reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        dimension_name,
        dimension_value,
        SUM(current_metric_value_numerator) AS prev_metric_value_numerator,
        SUM(current_metric_value_denominator) AS prev_metric_value_denominator
    FROM payments_hf.payments_p0_metrics
    WHERE date_value IN ({month_prev_str})
      AND date_granularity = 'WEEK'
      AND reporting_cluster = 'Overall'
      AND business_unit IS NOT NULL
      AND business_unit != 'Null'
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{test_metric}'
      AND dimension_name = '_Overall'
    GROUP BY business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
        dimension_name,
        dimension_value
"""

bu_level_prev = execute_query(bu_level_prev_query)
print(f"\n📊 bu_level rows in previous period: {len(bu_level_prev)}")

# Join and calculate
if not bu_level_current.empty and not bu_level_prev.empty:
    merged = bu_level_current.merge(
        bu_level_prev,
        on=['business_unit', 'metric_final_name', 'dimension_name', 'dimension_value'],
        how='inner',
        suffixes=('_current', '_prev')
    )
    
    if not merged.empty:
        merged['current_ratio'] = merged['current_metric_value_numerator'] / merged['current_metric_value_denominator']
        merged['prev_ratio'] = merged['prev_metric_value_numerator'] / merged['prev_metric_value_denominator']
        merged['rel_change_pct'] = ((merged['current_ratio'] - merged['prev_ratio']) / merged['prev_ratio']) * 100
        merged['abs_rel_change'] = abs(merged['rel_change_pct'])
        
        filtered = merged[merged['abs_rel_change'] > 10]
        print(f"\n✅ bu_level rows with >10% change: {len(filtered)}")
        if not filtered.empty:
            print(f"\n   Sample filtered rows:")
            print(filtered[['business_unit', 'current_ratio', 'prev_ratio', 'abs_rel_change']].head(10).to_string())
        else:
            print(f"   ⚠️  No bu_level rows with >10% change after filtering")
    else:
        print(f"   ⚠️  No matching bu_level rows between periods")

print(f"\n" + "="*80)
print("Conclusion")
print("="*80)
print("If bu_level rows exist with >10% changes, they should appear in the file.")
print("If they don't, the issue might be in the join or filtering logic in the notebook.")


