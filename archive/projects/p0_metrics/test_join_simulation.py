#!/usr/bin/env python3
"""
Simulate the exact join logic used in steering_output_generation_parametrized.py
to see where the issue is.
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

def test_month_prev_join_simulation():
    """Simulate the exact join logic from the script."""
    print("="*80)
    print("Simulating Month vs Previous Month Join (exact script logic)")
    print("="*80)
    
    current_weeks = ['2025-W41', '2025-W42', '2025-W43', '2025-W44']
    prev_weeks = ['2025-W37', '2025-W38', '2025-W39', '2025-W40']
    
    current_weeks_str = ','.join([f"'{w}'" for w in current_weeks])
    prev_weeks_str = ','.join([f"'{w}'" for w in prev_weeks])
    
    # Query current period (simulating build_metrics_query with comparison_type='current')
    query_current = f"""
        SELECT 
        '2025-W41-2025-W44' as date_value,
        '4WEEKS' as date_granularity,
        'current' as comparison_type,
        'Current' as comparison_label,
        a.reporting_cluster,
        CASE WHEN a.reporting_cluster = 'Overall' THEN "Null" ELSE a.business_unit END AS business_unit,
        CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name) as metric_final_name,
        CASE 
          WHEN a.metric_name IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
          ELSE dimension_name 
        END AS dimension_name,
        a.dimension_value,
        a.flag_more_is_good,
        a.flag_is_p0,
        a.metric_type,
        SUM(a.current_metric_value_numerator) AS current_metric_value_numerator,
        SUM(a.current_metric_value_denominator) AS current_metric_value_denominator
        FROM payments_hf.payments_p0_metrics a
        WHERE 1=1
          AND metric_type IN ('ratio', 'dollar-ratio')
          AND metric_name not in ('5_DunningBadDebtRate_12wkCohort','6_TotalBadDebtRate_12wkCohort','3_PaymentProcessingFees%','1_ChargeBackRate','3_PostDunningAR')
          AND flag_is_p0 = 'TRUE'
          AND date_granularity = 'WEEK'
          AND dimension_name NOT LIKE '%DeclineReason%'
          AND dimension_name not in ('LoyaltySegment','PaymentMethod_OrderType')
          AND (
            (a.metric_name not IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort')) 
            OR (a.metric_name IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort') AND dimension_value in ('Good'))
            )
          AND date_value IN ({current_weeks_str})
        GROUP BY a.reporting_cluster,
          CASE WHEN a.reporting_cluster = 'Overall' THEN "Null" ELSE a.business_unit END,
          CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name),
          CASE 
            WHEN a.metric_name IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort') THEN '_Overall' 
            ELSE dimension_name 
          END,
          a.dimension_value,
          a.flag_more_is_good,
          a.flag_is_p0,
          a.metric_type
        UNION ALL
        SELECT 
        '2025-W41-2025-W44' as date_value,
        '4WEEKS' as date_granularity,
        'current' as comparison_type,
        'Current' as comparison_label,
        'bu_level' AS reporting_cluster,
        a.business_unit,
        CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name) as metric_final_name,
        a.dimension_name,
        a.dimension_value,
        a.flag_more_is_good,
        a.flag_is_p0,
        a.metric_type,
        SUM(a.current_metric_value_numerator) AS current_metric_value_numerator,
        SUM(a.current_metric_value_denominator) AS current_metric_value_denominator
        FROM payments_hf.payments_p0_metrics a
        WHERE 1=1
          AND metric_type IN ('ratio', 'dollar-ratio')
          AND metric_name not in ('5_DunningBadDebtRate_12wkCohort','6_TotalBadDebtRate_12wkCohort','3_PaymentProcessingFees%','1_ChargeBackRate','3_PostDunningAR')
          AND flag_is_p0 = 'TRUE'
          AND date_granularity = 'WEEK'
          AND (
            (a.dimension_name = '_Overall' AND a.metric_name not IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort')) 
            OR (a.metric_name IN ('0_ShipRate','1_RecoveryW0','2_Recovery_12wkCohort','3_DunningAvgNetProfit_12wkCohort') AND dimension_value in ('Good'))
            )
          AND reporting_cluster = 'Overall'
          AND date_value IN ({current_weeks_str})
        GROUP BY a.business_unit,
          CONCAT(a.focus_group, ' - ', a.metric_group, ' - ',a.metric_name),
          a.dimension_name,
          a.dimension_value,
          a.flag_more_is_good,
          a.flag_is_p0,
          a.metric_type
    """
    
    print(f"\n📊 Querying current period (simulating build_metrics_query)...")
    data_current = execute_query(query_current)
    print(f"   Found {len(data_current)} rows")
    print(f"   Reporting clusters: {data_current['reporting_cluster'].unique().tolist() if len(data_current) > 0 else 'N/A'}")
    
    # Query previous period
    query_prev = query_current.replace(current_weeks_str, prev_weeks_str).replace('2025-W41-2025-W44', '2025-W37-2025-W40')
    
    print(f"\n📊 Querying previous period (simulating build_metrics_query)...")
    data_prev = execute_query(query_prev)
    print(f"   Found {len(data_prev)} rows")
    print(f"   Reporting clusters: {data_prev['reporting_cluster'].unique().tolist() if len(data_prev) > 0 else 'N/A'}")
    
    # Simulate the join logic
    print(f"\n🔗 Simulating join logic...")
    
    # Filter to 'Overall' reporting_cluster
    data_current_overall = data_current[data_current['reporting_cluster'] == 'Overall'].copy()
    data_prev_overall = data_prev[data_prev['reporting_cluster'] == 'Overall'].copy()
    
    print(f"   Current Overall rows: {len(data_current_overall)}")
    print(f"   Prev Overall rows: {len(data_prev_overall)}")
    
    if len(data_current_overall) > 0 and len(data_prev_overall) > 0:
        # Rename prev columns (simulating the script logic)
        data_prev_overall = data_prev_overall.rename(columns={
            'current_metric_value_numerator': 'prev_metric_value_numerator',
            'current_metric_value_denominator': 'prev_metric_value_denominator'
        })
        
        # Join keys
        join_cols = ['reporting_cluster', 'business_unit', 'metric_final_name', 'dimension_name', 'dimension_value', 
                     'flag_more_is_good', 'flag_is_p0', 'metric_type']
        
        # Select only needed columns
        data_current_clean = data_current_overall[[c for c in data_current_overall.columns if c not in ['prev_metric_value_numerator', 'prev_metric_value_denominator']]]
        data_prev_selected = data_prev_overall[join_cols + ['prev_metric_value_numerator', 'prev_metric_value_denominator']]
        
        # Perform join
        data_joined = data_current_clean.merge(
            data_prev_selected,
            on=join_cols,
            how='left'
        )
        
        print(f"   After join: {len(data_joined)} rows")
        matched_count = data_joined['prev_metric_value_numerator'].notna().sum()
        print(f"   Rows with prev values: {matched_count}")
        
        if matched_count > 0:
            # Calculate ratio for a sample metric
            test_metric = '1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess'
            metric_row = data_joined[data_joined['metric_final_name'] == test_metric]
            
            if len(metric_row) > 0:
                row = metric_row.iloc[0]
                current_ratio = (row['current_metric_value_numerator'] / row['current_metric_value_denominator'] * 100) if row['current_metric_value_denominator'] > 0 else 0
                prev_ratio = (row['prev_metric_value_numerator'] / row['prev_metric_value_denominator'] * 100) if pd.notna(row['prev_metric_value_denominator']) and row['prev_metric_value_denominator'] > 0 else 0
                
                print(f"\n   ✅ Join successful!")
                print(f"   Sample metric: {test_metric}")
                print(f"   Current ratio: {current_ratio:.2f}%")
                print(f"   Previous ratio: {prev_ratio:.2f}%")
            else:
                print(f"\n   ⚠️  Test metric not found in joined data")
        else:
            print(f"\n   ❌ No matches in join!")
            print(f"   Checking why...")
            
            # Check join keys
            if len(data_current_clean) > 0 and len(data_prev_selected) > 0:
                current_keys = set(tuple(data_current_clean[join_cols].iloc[0]))
                prev_keys = set(tuple(data_prev_selected[join_cols].iloc[0]))
                print(f"   Current keys sample: {dict(zip(join_cols, data_current_clean[join_cols].iloc[0]))}")
                print(f"   Prev keys sample: {dict(zip(join_cols, data_prev_selected[join_cols].iloc[0]))}")
    else:
        print(f"   ⚠️  Missing data for join")

def main():
    """Run the simulation."""
    test_month_prev_join_simulation()
    
    print("\n" + "="*80)
    print("Simulation Complete")
    print("="*80)

if __name__ == "__main__":
    main()


