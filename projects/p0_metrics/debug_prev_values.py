#!/usr/bin/env python3
"""
Step-by-step debugging script to identify why prev_month and prev_quarter values are zero
while prev_week values are correct.

Debugging Plan:
1. Test prev_week query and data flow (known working)
2. Test prev_month query and data flow (known broken)
3. Compare the two to identify the difference
4. Filter for specific metric + Overall cluster only for focused debugging
"""

import sys
import os
from pathlib import Path

# Add cursor_databricks directory to path for imports
cursor_databricks_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_dir)
from databricks import sql
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN

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
                return [dict(zip(columns, row)) for row in result]
            return []

# Test metric and cluster
TEST_METRIC = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
TEST_CLUSTER = 'Overall'

print("="*80)
print("DEBUGGING: Why prev_month and prev_quarter are zero")
print("="*80)
print(f"Test Metric: {TEST_METRIC}")
print(f"Test Cluster: {TEST_CLUSTER}")
print()

# ============================================================================
# STEP 1: Test prev_week (KNOWN WORKING)
# ============================================================================
print("="*80)
print("STEP 1: Testing prev_week (should work correctly)")
print("="*80)

# Use known weeks for testing
latest_week = '2025-W44'
prev_week = '2025-W43'
print(f"Latest week: {latest_week}")
print(f"Previous week: {prev_week}")

# Query current week data (simulating build_metrics_query with comparison_type='prev_period')
week_current_query = f"""
    SELECT 
        reporting_cluster,
        CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END AS business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        CASE 
          WHEN metric_name IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
          ELSE dimension_name 
        END AS dimension_name,
        dimension_value,
        flag_more_is_good,
        flag_is_p0,
        metric_type,
        SUM(current_metric_value_numerator) AS current_metric_value_numerator,
        SUM(current_metric_value_denominator) AS current_metric_value_denominator,
        SUM(prev_metric_value_numerator) AS prev_metric_value_numerator,
        SUM(prev_metric_value_denominator) AS prev_metric_value_denominator
    FROM payments_hf.payments_p0_metrics
    WHERE date_value = '{latest_week}'
      AND date_granularity = 'WEEK'
      AND reporting_cluster = '{TEST_CLUSTER}'
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{TEST_METRIC}'
      AND dimension_name = '_Overall'
    GROUP BY reporting_cluster,
        CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
        CASE 
          WHEN metric_name IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
          ELSE dimension_name 
        END,
        dimension_value,
        flag_more_is_good,
        flag_is_p0,
        metric_type
"""

print(f"\n📊 Querying prev_week current period data...")
week_current_data = execute_query(week_current_query)
print(f"   Found {len(week_current_data)} rows")

if week_current_data:
    row = week_current_data[0]
    current_num = row['current_metric_value_numerator']
    current_den = row['current_metric_value_denominator']
    prev_num = row['prev_metric_value_numerator']
    prev_den = row['prev_metric_value_denominator']
    
    current_ratio = (current_num / current_den * 100) if current_den > 0 else 0
    prev_ratio = (prev_num / prev_den * 100) if prev_den and prev_den > 0 else 0
    
    print(f"   ✅ prev_week data:")
    print(f"      current: {current_num} / {current_den} = {current_ratio:.2f}%")
    print(f"      prev: {prev_num} / {prev_den} = {prev_ratio:.2f}%")
    print(f"      ⚠️  NOTE: prev_week uses prev_metric_value columns from table (direct)")
else:
    print(f"   ❌ No data found")

# ============================================================================
# STEP 2: Test prev_month (KNOWN BROKEN)
# ============================================================================
print("\n" + "="*80)
print("STEP 2: Testing prev_month (should be broken)")
print("="*80)

# Define weeks for month comparison
current_weeks = ['2025-W41', '2025-W42', '2025-W43', '2025-W44']
prev_weeks = ['2025-W37', '2025-W38', '2025-W39', '2025-W40']

current_weeks_str = ','.join([f"'{w}'" for w in current_weeks])
prev_weeks_str = ','.join([f"'{w}'" for w in prev_weeks])

print(f"Current weeks: {current_weeks}")
print(f"Previous weeks: {prev_weeks}")

# Query current period (simulating build_metrics_query with comparison_type='current')
month_current_query = f"""
    SELECT 
        reporting_cluster,
        CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END AS business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        CASE 
          WHEN metric_name IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
          ELSE dimension_name 
        END AS dimension_name,
        dimension_value,
        flag_more_is_good,
        flag_is_p0,
        metric_type,
        SUM(current_metric_value_numerator) AS current_metric_value_numerator,
        SUM(current_metric_value_denominator) AS current_metric_value_denominator
    FROM payments_hf.payments_p0_metrics
    WHERE date_value IN ({current_weeks_str})
      AND date_granularity = 'WEEK'
      AND reporting_cluster = '{TEST_CLUSTER}'
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{TEST_METRIC}'
      AND dimension_name = '_Overall'
    GROUP BY reporting_cluster,
        CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
        CASE 
          WHEN metric_name IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
          ELSE dimension_name 
        END,
        dimension_value,
        flag_more_is_good,
        flag_is_p0,
        metric_type
"""

print(f"\n📊 Querying prev_month current period data...")
month_current_data = execute_query(month_current_query)
print(f"   Found {len(month_current_data)} rows")

if month_current_data:
    row = month_current_data[0]
    current_num = row['current_metric_value_numerator']
    current_den = row['current_metric_value_denominator']
    
    current_ratio = (current_num / current_den * 100) if current_den > 0 else 0
    
    print(f"   ✅ month current data:")
    print(f"      current: {current_num} / {current_den} = {current_ratio:.2f}%")
    print(f"      ⚠️  NOTE: No prev columns (comparison_type='current')")
else:
    print(f"   ❌ No data found")

# Query previous period (simulating build_metrics_query with comparison_type='current' for prev weeks)
month_prev_query = f"""
    SELECT 
        reporting_cluster,
        CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END AS business_unit,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
        CASE 
          WHEN metric_name IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
          ELSE dimension_name 
        END AS dimension_name,
        dimension_value,
        flag_more_is_good,
        flag_is_p0,
        metric_type,
        SUM(current_metric_value_numerator) AS prev_metric_value_numerator,
        SUM(current_metric_value_denominator) AS prev_metric_value_denominator
    FROM payments_hf.payments_p0_metrics
    WHERE date_value IN ({prev_weeks_str})
      AND date_granularity = 'WEEK'
      AND reporting_cluster = '{TEST_CLUSTER}'
      AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{TEST_METRIC}'
      AND dimension_name = '_Overall'
    GROUP BY reporting_cluster,
        CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END,
        CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
        CASE 
          WHEN metric_name IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
          ELSE dimension_name 
        END,
        dimension_value,
        flag_more_is_good,
        flag_is_p0,
        metric_type
"""

print(f"\n📊 Querying prev_month previous period data...")
month_prev_data = execute_query(month_prev_query)
print(f"   Found {len(month_prev_data)} rows")

if month_prev_data:
    row = month_prev_data[0]
    prev_num = row['prev_metric_value_numerator']
    prev_den = row['prev_metric_value_denominator']
    
    prev_ratio = (prev_num / prev_den * 100) if prev_den and prev_den > 0 else 0
    
    print(f"   ✅ month prev data:")
    print(f"      prev: {prev_num} / {prev_den} = {prev_ratio:.2f}%")
    print(f"      ⚠️  NOTE: This is renamed from current_metric_value (should be used in join)")
else:
    print(f"   ❌ No data found")

# ============================================================================
# STEP 3: Simulate the join logic
# ============================================================================
print("\n" + "="*80)
print("STEP 3: Simulating the join logic")
print("="*80)

if month_current_data and month_prev_data:
    current_row = month_current_data[0]
    prev_row = month_prev_data[0]
    
    # Join keys
    join_cols = ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'dimension_value', 
                 'flag_more_is_good', 'flag_is_p0', 'metric_type']
    
    print(f"\n🔍 Checking join keys:")
    all_match = True
    for col in join_cols:
        current_val = current_row.get(col)
        prev_val = prev_row.get(col)
        match = current_val == prev_val
        all_match = all_match and match
        status = "✅" if match else "❌"
        print(f"   {status} {col}: '{current_val}' == '{prev_val}'")
    
    if all_match:
        print(f"\n   ✅ All join keys match!")
        print(f"\n   📊 After join (simulated):")
        print(f"      current: {current_row['current_metric_value_numerator']} / {current_row['current_metric_value_denominator']} = {current_ratio:.2f}%")
        print(f"      prev: {prev_row['prev_metric_value_numerator']} / {prev_row['prev_metric_value_denominator']} = {prev_ratio:.2f}%")
        print(f"\n   ✅ Join should work! The data is there.")
        print(f"   ⚠️  The issue must be in the PySpark join or post-processing.")
    else:
        print(f"\n   ❌ Join keys don't match! This is the problem.")
else:
    print(f"   ⚠️  Cannot simulate join - missing data")

# ============================================================================
# STEP 4: Compare with prev_week approach
# ============================================================================
print("\n" + "="*80)
print("STEP 4: Key Difference Analysis")
print("="*80)

print(f"\n📋 prev_week approach:")
print(f"   - Uses single week query")
print(f"   - Query returns prev_metric_value_numerator/denominator directly from table")
print(f"   - No join needed - data comes from same row")

print(f"\n📋 prev_month approach:")
print(f"   - Uses multi-week aggregation (4 weeks)")
print(f"   - Query for current period: comparison_type='current' (no prev columns)")
print(f"   - Query for prev period: comparison_type='current' (renamed to prev)")
print(f"   - Requires JOIN between two separate queries")
print(f"   - ⚠️  This is where the issue likely occurs!")

print("\n" + "="*80)
print("CONCLUSION")
print("="*80)
print("The issue is likely in the PySpark join logic or how the data flows")
print("after the join. The SQL queries themselves return correct data.")
print("Next: Check the actual PySpark join in the notebook.")

