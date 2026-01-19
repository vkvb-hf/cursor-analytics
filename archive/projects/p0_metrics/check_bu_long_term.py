#!/usr/bin/env python3
"""
Check if business units with >10% changes exist in month_prev and quarter_prev data
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
print("Checking Business Units in Long-Term Impact Data")
print("="*80)

# Define weeks for month and quarter
month_current_weeks = ['2025-W41', '2025-W42', '2025-W43', '2025-W44']
month_prev_weeks = ['2025-W37', '2025-W38', '2025-W39', '2025-W40']

quarter_current_weeks = ['2025-W32', '2025-W33', '2025-W34', '2025-W35', '2025-W36', '2025-W37', 
                         '2025-W38', '2025-W39', '2025-W40', '2025-W41', '2025-W42', '2025-W43', '2025-W44']
quarter_prev_weeks = ['2025-W19', '2025-W20', '2025-W21', '2025-W22', '2025-W23', '2025-W24', 
                      '2025-W25', '2025-W26', '2025-W27', '2025-W28', '2025-W29', '2025-W30', '2025-W31']

month_current_str = ','.join([f"'{w}'" for w in month_current_weeks])
month_prev_str = ','.join([f"'{w}'" for w in month_prev_weeks])
quarter_current_str = ','.join([f"'{w}'" for w in quarter_current_weeks])
quarter_prev_str = ','.join([f"'{w}'" for w in quarter_prev_weeks])

# Test metric
test_metric = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'

print(f"\n📊 Checking Month vs Previous Month (4 weeks)")
print(f"   Current: {month_current_weeks}")
print(f"   Previous: {month_prev_weeks}")

# Query month current period
month_current_query = f"""
    SELECT 
        reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        dimension_name,
        dimension_value,
        SUM(current_metric_value_numerator) AS current_numerator,
        SUM(current_metric_value_denominator) AS current_denominator
    FROM payments_hf.payments_p0_metrics
    WHERE date_value IN ({month_current_str})
      AND date_granularity = 'WEEK'
      AND reporting_cluster = 'bu_level'
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{test_metric}'
      AND dimension_name = '_Overall'
    GROUP BY reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
        dimension_name,
        dimension_value
"""

month_current_df = execute_query(month_current_query)
print(f"   Found {len(month_current_df)} business units in current period")

# Query month previous period
month_prev_query = f"""
    SELECT 
        reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        dimension_name,
        dimension_value,
        SUM(current_metric_value_numerator) AS prev_numerator,
        SUM(current_metric_value_denominator) AS prev_denominator
    FROM payments_hf.payments_p0_metrics
    WHERE date_value IN ({month_prev_str})
      AND date_granularity = 'WEEK'
      AND reporting_cluster = 'bu_level'
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{test_metric}'
      AND dimension_name = '_Overall'
    GROUP BY reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
        dimension_name,
        dimension_value
"""

month_prev_df = execute_query(month_prev_query)
print(f"   Found {len(month_prev_df)} business units in previous period")

# Join and calculate changes
if not month_current_df.empty and not month_prev_df.empty:
    month_merged = month_current_df.merge(
        month_prev_df,
        on=['business_unit', 'metric_final_name', 'dimension_name', 'dimension_value'],
        how='inner'
    )
    
    if not month_merged.empty:
        month_merged['current_ratio'] = (month_merged['current_numerator'] / month_merged['current_denominator']) * 100
        month_merged['prev_ratio'] = (month_merged['prev_numerator'] / month_merged['prev_denominator']) * 100
        month_merged['abs_change'] = abs(month_merged['current_ratio'] - month_merged['prev_ratio'])
        month_merged['rel_change_pct'] = ((month_merged['current_ratio'] - month_merged['prev_ratio']) / month_merged['prev_ratio']) * 100
        month_merged['abs_rel_change'] = abs(month_merged['rel_change_pct'])
        
        month_filtered = month_merged[month_merged['abs_rel_change'] > 10]
        print(f"   Found {len(month_filtered)} business units with >10% change")
        
        if not month_filtered.empty:
            print(f"\n   ✅ Business units with >10% change in month_prev:")
            for _, row in month_filtered.head(10).iterrows():
                print(f"      {row['business_unit']}: {row['prev_ratio']:.2f}% to {row['current_ratio']:.2f}% ({row['abs_rel_change']:.2f}% change)")
        else:
            print(f"   ⚠️  No business units with >10% change in month_prev")
    else:
        print(f"   ⚠️  No matching business units between current and previous period")

print(f"\n📊 Checking Quarter vs Previous Quarter (13 weeks)")
print(f"   Current: {len(quarter_current_weeks)} weeks")
print(f"   Previous: {len(quarter_prev_weeks)} weeks")

# Query quarter current period
quarter_current_query = f"""
    SELECT 
        reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        dimension_name,
        dimension_value,
        SUM(current_metric_value_numerator) AS current_numerator,
        SUM(current_metric_value_denominator) AS current_denominator
    FROM payments_hf.payments_p0_metrics
    WHERE date_value IN ({quarter_current_str})
      AND date_granularity = 'WEEK'
      AND reporting_cluster = 'bu_level'
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{test_metric}'
      AND dimension_name = '_Overall'
    GROUP BY reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
        dimension_name,
        dimension_value
"""

quarter_current_df = execute_query(quarter_current_query)
print(f"   Found {len(quarter_current_df)} business units in current period")

# Query quarter previous period
quarter_prev_query = f"""
    SELECT 
        reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        dimension_name,
        dimension_value,
        SUM(current_metric_value_numerator) AS prev_numerator,
        SUM(current_metric_value_denominator) AS prev_denominator
    FROM payments_hf.payments_p0_metrics
    WHERE date_value IN ({quarter_prev_str})
      AND date_granularity = 'WEEK'
      AND reporting_cluster = 'bu_level'
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{test_metric}'
      AND dimension_name = '_Overall'
    GROUP BY reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
        dimension_name,
        dimension_value
"""

quarter_prev_df = execute_query(quarter_prev_query)
print(f"   Found {len(quarter_prev_df)} business units in previous period")

# Join and calculate changes
if not quarter_current_df.empty and not quarter_prev_df.empty:
    quarter_merged = quarter_current_df.merge(
        quarter_prev_df,
        on=['business_unit', 'metric_final_name', 'dimension_name', 'dimension_value'],
        how='inner'
    )
    
    if not quarter_merged.empty:
        quarter_merged['current_ratio'] = (quarter_merged['current_numerator'] / quarter_merged['current_denominator']) * 100
        quarter_merged['prev_ratio'] = (quarter_merged['prev_numerator'] / quarter_merged['prev_denominator']) * 100
        quarter_merged['abs_change'] = abs(quarter_merged['current_ratio'] - quarter_merged['prev_ratio'])
        quarter_merged['rel_change_pct'] = ((quarter_merged['current_ratio'] - quarter_merged['prev_ratio']) / quarter_merged['prev_ratio']) * 100
        quarter_merged['abs_rel_change'] = abs(quarter_merged['rel_change_pct'])
        
        quarter_filtered = quarter_merged[quarter_merged['abs_rel_change'] > 10]
        print(f"   Found {len(quarter_filtered)} business units with >10% change")
        
        if not quarter_filtered.empty:
            print(f"\n   ✅ Business units with >10% change in quarter_prev:")
            for _, row in quarter_filtered.head(10).iterrows():
                print(f"      {row['business_unit']}: {row['prev_ratio']:.2f}% to {row['current_ratio']:.2f}% ({row['abs_rel_change']:.2f}% change)")
        else:
            print(f"   ⚠️  No business units with >10% change in quarter_prev")
    else:
        print(f"   ⚠️  No matching business units between current and previous period")

print(f"\n" + "="*80)
print("Summary")
print("="*80)
print("If business units with >10% changes exist but are not in the file,")
print("there may be an issue with the filtering or deduplication logic.")


