#!/usr/bin/env python3
"""
Check business units in the actual data structure (reporting_cluster = 'Overall' with business_unit column)
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
print("Checking Business Units in Actual Table Structure")
print("="*80)

# Define weeks
month_current_weeks = ['2025-W41', '2025-W42', '2025-W43', '2025-W44']
month_prev_weeks = ['2025-W37', '2025-W38', '2025-W39', '2025-W40']

month_current_str = ','.join([f"'{w}'" for w in month_current_weeks])
month_prev_str = ','.join([f"'{w}'" for w in month_prev_weeks])

test_metric = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'

# Get business unit to reporting cluster mapping
mapping_query = """
    SELECT
      business_unit,
      explode(reporting_cluster_array) AS reporting_cluster
    FROM payments_hf.business_units
"""
mapping_df = execute_query(mapping_query)
print(f"\n📊 Loaded {len(mapping_df)} business unit mappings")
print(f"   Sample: {mapping_df.head(10).to_string()}")

# Query month current - business units are in reporting_cluster = 'Overall' with business_unit column
month_current_query = f"""
    SELECT 
        'Overall' as reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        dimension_name,
        dimension_value,
        SUM(current_metric_value_numerator) AS current_numerator,
        SUM(current_metric_value_denominator) AS current_denominator
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

month_current_df = execute_query(month_current_query)
print(f"\n📊 Month Current: Found {len(month_current_df)} business units")
if not month_current_df.empty:
    print(f"   Sample: {month_current_df.head(5).to_string()}")

# Query month previous
month_prev_query = f"""
    SELECT 
        'Overall' as reporting_cluster,
        business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        dimension_name,
        dimension_value,
        SUM(current_metric_value_numerator) AS prev_numerator,
        SUM(current_metric_value_denominator) AS prev_denominator
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

month_prev_df = execute_query(month_prev_query)
print(f"📊 Month Previous: Found {len(month_prev_df)} business units")

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
        month_merged['rel_change_pct'] = ((month_merged['current_ratio'] - month_merged['prev_ratio']) / month_merged['prev_ratio']) * 100
        month_merged['abs_rel_change'] = abs(month_merged['rel_change_pct'])
        
        month_filtered = month_merged[month_merged['abs_rel_change'] > 10]
        print(f"\n✅ Found {len(month_filtered)} business units with >10% change in month_prev")
        
        if not month_filtered.empty:
            print(f"\n   Top business units with >10% change:")
            month_sorted = month_filtered.sort_values('abs_rel_change', ascending=False)
            for _, row in month_sorted.head(10).iterrows():
                # Get reporting cluster for this business unit
                bu_clusters = mapping_df[mapping_df['business_unit'] == row['business_unit']]['reporting_cluster'].tolist()
                cluster_str = ', '.join(bu_clusters) if bu_clusters else 'Unknown'
                print(f"      {row['business_unit']} ({cluster_str}): {row['prev_ratio']:.2f}% to {row['current_ratio']:.2f}% ({row['abs_rel_change']:.2f}% change)")
        else:
            print(f"   ⚠️  No business units with >10% change in month_prev")
    else:
        print(f"   ⚠️  No matching business units between current and previous period")

print(f"\n" + "="*80)
print("Conclusion")
print("="*80)
print("If business units with >10% changes exist, they should appear in the file.")
print("If they don't appear, check the filtering logic in the notebook.")


