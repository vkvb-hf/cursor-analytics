#!/usr/bin/env python3
"""
Test the join logic for month_prev and quarter_prev comparisons.

This script tests:
1. Querying current period data
2. Querying previous period data
3. Testing the join between them
4. Identifying why the join might be failing
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

def test_month_prev_join():
    """Test the join logic for month_prev comparison."""
    print("="*80)
    print("Testing Month vs Previous Month Join Logic")
    print("="*80)
    
    # Define weeks
    current_weeks = ['2025-W41', '2025-W42', '2025-W43', '2025-W44']
    prev_weeks = ['2025-W37', '2025-W38', '2025-W39', '2025-W40']
    
    current_weeks_str = ','.join([f"'{w}'" for w in current_weeks])
    prev_weeks_str = ','.join([f"'{w}'" for w in prev_weeks])
    
    # Test metric
    test_metric = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
    
    print(f"\nCurrent weeks: {current_weeks}")
    print(f"Previous weeks: {prev_weeks}")
    print(f"Test metric: {test_metric}")
    
    # Query current period
    query_current = f"""
        SELECT
            reporting_cluster,
            CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END AS business_unit,
            CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
            CASE 
              WHEN metric_name IN ('0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
              ELSE dimension_name 
            END AS dimension_name,
            dimension_value,
            flag_more_is_good,
            flag_is_p0,
            metric_type,
            SUM(current_metric_value_numerator) as current_numerator,
            SUM(current_metric_value_denominator) as current_denominator
        FROM payments_hf.payments_p0_metrics
        WHERE date_value IN ({current_weeks_str})
            AND date_granularity = 'WEEK'
            AND reporting_cluster = 'Overall'
            AND dimension_name = '_Overall'
            AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{test_metric}'
        GROUP BY reporting_cluster,
            CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END,
            CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
            CASE 
              WHEN metric_name IN ('0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
              ELSE dimension_name 
            END,
            dimension_value,
            flag_more_is_good,
            flag_is_p0,
            metric_type
    """
    
    print(f"\n📊 Querying current period data...")
    current_data = execute_query(query_current)
    print(f"   Found {len(current_data)} rows")
    
    if current_data:
        print(f"\n   Sample current data:")
        for key, value in current_data[0].items():
            print(f"     {key}: {value}")
    
    # Query previous period
    query_prev = f"""
        SELECT
            reporting_cluster,
            CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END AS business_unit,
            CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
            CASE 
              WHEN metric_name IN ('0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
              ELSE dimension_name 
            END AS dimension_name,
            dimension_value,
            flag_more_is_good,
            flag_is_p0,
            metric_type,
            SUM(current_metric_value_numerator) as prev_numerator,
            SUM(current_metric_value_denominator) as prev_denominator
        FROM payments_hf.payments_p0_metrics
        WHERE date_value IN ({prev_weeks_str})
            AND date_granularity = 'WEEK'
            AND reporting_cluster = 'Overall'
            AND dimension_name = '_Overall'
            AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{test_metric}'
        GROUP BY reporting_cluster,
            CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END,
            CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
            CASE 
              WHEN metric_name IN ('0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
              ELSE dimension_name 
            END,
            dimension_value,
            flag_more_is_good,
            flag_is_p0,
            metric_type
    """
    
    print(f"\n📊 Querying previous period data...")
    prev_data = execute_query(query_prev)
    print(f"   Found {len(prev_data)} rows")
    
    if prev_data:
        print(f"\n   Sample prev data:")
        for key, value in prev_data[0].items():
            print(f"     {key}: {value}")
    
    # Check join keys
    if current_data and prev_data:
        print(f"\n🔍 Analyzing join keys...")
        join_cols = ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'dimension_value', 
                     'flag_more_is_good', 'flag_is_p0', 'metric_type']
        
        current_keys = {col: current_data[0][col] for col in join_cols}
        prev_keys = {col: prev_data[0][col] for col in join_cols}
        
        print(f"\n   Current period join keys:")
        for col in join_cols:
            print(f"     {col}: {current_keys[col]} (type: {type(current_keys[col]).__name__})")
        
        print(f"\n   Previous period join keys:")
        for col in join_cols:
            print(f"     {col}: {prev_keys[col]} (type: {type(prev_keys[col]).__name__})")
        
        print(f"\n   Key comparison:")
        all_match = True
        for col in join_cols:
            match = current_keys[col] == prev_keys[col]
            all_match = all_match and match
            status = "✅" if match else "❌"
            print(f"     {status} {col}: {current_keys[col]} == {prev_keys[col]}")
        
        if all_match:
            print(f"\n   ✅ All join keys match! The join should work.")
            
            # Calculate ratios
            current_ratio = (current_data[0]['current_numerator'] / current_data[0]['current_denominator'] * 100) if current_data[0]['current_denominator'] > 0 else 0
            prev_ratio = (prev_data[0]['prev_numerator'] / prev_data[0]['prev_denominator'] * 100) if prev_data[0]['prev_denominator'] > 0 else 0
            
            print(f"\n   📈 Calculated ratios:")
            print(f"     Current: {current_ratio:.2f}%")
            print(f"     Previous: {prev_ratio:.2f}%")
        else:
            print(f"\n   ❌ Join keys don't match! This is why the join is failing.")
    else:
        print(f"\n   ⚠️  Missing data - cannot test join keys")
        if not current_data:
            print(f"     No current period data found")
        if not prev_data:
            print(f"     No previous period data found")

def test_quarter_prev_join():
    """Test the join logic for quarter_prev comparison."""
    print("\n" + "="*80)
    print("Testing Quarter vs Previous Quarter Join Logic")
    print("="*80)
    
    # Define weeks (first 3 weeks for testing)
    current_weeks = ['2025-W32', '2025-W33', '2025-W34', '2025-W35', '2025-W36', '2025-W37', 
                     '2025-W38', '2025-W39', '2025-W40', '2025-W41', '2025-W42', '2025-W43', '2025-W44']
    prev_weeks = ['2025-W19', '2025-W20', '2025-W21', '2025-W22', '2025-W23', '2025-W24', 
                  '2025-W25', '2025-W26', '2025-W27', '2025-W28', '2025-W29', '2025-W30', '2025-W31']
    
    current_weeks_str = ','.join([f"'{w}'" for w in current_weeks])
    prev_weeks_str = ','.join([f"'{w}'" for w in prev_weeks])
    
    # Test metric
    test_metric = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
    
    print(f"\nCurrent weeks: {len(current_weeks)} weeks (showing first 3: {current_weeks[:3]}...)")
    print(f"Previous weeks: {len(prev_weeks)} weeks (showing first 3: {prev_weeks[:3]}...)")
    print(f"Test metric: {test_metric}")
    
    # Query current period
    query_current = f"""
        SELECT
            reporting_cluster,
            CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END AS business_unit,
            CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
            CASE 
              WHEN metric_name IN ('0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
              ELSE dimension_name 
            END AS dimension_name,
            dimension_value,
            flag_more_is_good,
            flag_is_p0,
            metric_type,
            SUM(current_metric_value_numerator) as current_numerator,
            SUM(current_metric_value_denominator) as current_denominator
        FROM payments_hf.payments_p0_metrics
        WHERE date_value IN ({current_weeks_str})
            AND date_granularity = 'WEEK'
            AND reporting_cluster = 'Overall'
            AND dimension_name = '_Overall'
            AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{test_metric}'
        GROUP BY reporting_cluster,
            CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END,
            CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
            CASE 
              WHEN metric_name IN ('0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
              ELSE dimension_name 
            END,
            dimension_value,
            flag_more_is_good,
            flag_is_p0,
            metric_type
    """
    
    print(f"\n📊 Querying current period data...")
    current_data = execute_query(query_current)
    print(f"   Found {len(current_data)} rows")
    
    if current_data:
        current_ratio = (current_data[0]['current_numerator'] / current_data[0]['current_denominator'] * 100) if current_data[0]['current_denominator'] > 0 else 0
        print(f"   Current ratio: {current_ratio:.2f}%")
    
    # Query previous period
    query_prev = f"""
        SELECT
            reporting_cluster,
            CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END AS business_unit,
            CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) as metric_final_name,
            CASE 
              WHEN metric_name IN ('0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
              ELSE dimension_name 
            END AS dimension_name,
            dimension_value,
            flag_more_is_good,
            flag_is_p0,
            metric_type,
            SUM(current_metric_value_numerator) as prev_numerator,
            SUM(current_metric_value_denominator) as prev_denominator
        FROM payments_hf.payments_p0_metrics
        WHERE date_value IN ({prev_weeks_str})
            AND date_granularity = 'WEEK'
            AND reporting_cluster = 'Overall'
            AND dimension_name = '_Overall'
            AND CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name) = '{test_metric}'
        GROUP BY reporting_cluster,
            CASE WHEN reporting_cluster = 'Overall' THEN "Null" ELSE business_unit END,
            CONCAT(focus_group, ' - ', metric_group, ' - ', metric_name),
            CASE 
              WHEN metric_name IN ('0_ShipRate', '1_RecoveryW0', '2_Recovery_12wkCohort', '3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
              ELSE dimension_name 
            END,
            dimension_value,
            flag_more_is_good,
            flag_is_p0,
            metric_type
    """
    
    print(f"\n📊 Querying previous period data...")
    prev_data = execute_query(query_prev)
    print(f"   Found {len(prev_data)} rows")
    
    if prev_data:
        prev_ratio = (prev_data[0]['prev_numerator'] / prev_data[0]['prev_denominator'] * 100) if prev_data[0]['prev_denominator'] > 0 else 0
        print(f"   Previous ratio: {prev_ratio:.2f}%")
    
    # Check join keys
    if current_data and prev_data:
        print(f"\n🔍 Analyzing join keys...")
        join_cols = ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'dimension_value', 
                     'flag_more_is_good', 'flag_is_p0', 'metric_type']
        
        current_keys = {col: current_data[0][col] for col in join_cols}
        prev_keys = {col: prev_data[0][col] for col in join_cols}
        
        all_match = True
        for col in join_cols:
            match = current_keys[col] == prev_keys[col]
            all_match = all_match and match
            status = "✅" if match else "❌"
            print(f"     {status} {col}: {current_keys[col]} == {prev_keys[col]}")
        
        if all_match:
            print(f"\n   ✅ All join keys match!")
        else:
            print(f"\n   ❌ Join keys don't match!")

def main():
    """Run all tests."""
    test_month_prev_join()
    test_quarter_prev_join()
    
    print("\n" + "="*80)
    print("Test Complete")
    print("="*80)

if __name__ == "__main__":
    main()


